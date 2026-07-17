#!/usr/bin/env python3
"""Drive Codex CLI as the audit-lane independent auditor.

Pulls the top-N rows from `docs/audit/data/audit_queue.json`, constructs
the prompt from `docs/audit/AUDIT_AGENT_PROMPT_TEMPLATE.md` for each, runs
`codex exec` (which uses the local ChatGPT subscription, no per-call API
billing), captures the JSON verdict, validates it, adds auditor metadata,
and pipes it through `docs/audit/scripts/apply_audit.py`. Each successful
verdict triggers `apply_audit.py`'s built-in propagation slice so the
pipeline stays consistent.

Usage:
  python3 scripts/codex_audit_runner.py [--n 10] [--dry-run] [--criticality critical]
                                        [--auditor-name codex-batch-2026-05-04]
                                        [--timeout-sec 300]

Fresh-look rule: the audit lane uses the best available Codex GPT model
at maximum reasoning because most ledger notes were authored by Claude.
This wrapper auto-selects the strongest full GPT model from Codex's local
model cache when possible, records the exact `auditor_family` it invoked,
and records independence per row: first-pass Claude/human-authored rows
are `cross_family`, while same-family second passes are `fresh_context`.
Do NOT change that policy without re-reading
`docs/audit/FRESH_LOOK_REQUIREMENTS.md`.

Restricted-inputs rule: each codex exec runs with --skip-git-repo-check
in an empty workdir under /tmp/codex-audit-isolated/<run-id>/, so the
auditor sees ONLY the prompt content (claim note + cited authorities +
runner stdout) and not the broader repo. This satisfies the audit lane's
fresh-look requirement.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path

# Shared SHA-pinned runner cache. The audit prompt's Section 3 (runner
# stdout) is sourced from logs/runner-cache/<stem>.txt; cache freshness
# is keyed on the runner's content SHA-256.
sys.path.insert(0, str(Path(__file__).resolve().parent))
import runner_cache as rc

REPO_ROOT = Path(__file__).resolve().parent.parent
AUDIT_DIR = REPO_ROOT / "docs" / "audit"

# Centralized accepted-premise policy (axioms + explicitly approved framework
# primitives). Shared with compute_effective_status / audit_lint /
# compute_reaudit_candidates via docs/audit/scripts/premise_nodes.py so the
# prompt and the deterministic pipeline cannot drift.
sys.path.insert(0, str(AUDIT_DIR / "scripts"))
import premise_nodes
import ledger_io
import no_go_discipline_gate
import audit_invocation
import compute_audit_dispatch_queue

LEDGER_PATH = AUDIT_DIR / "data" / "audit_ledger.json"
QUEUE_PATH = AUDIT_DIR / "data" / "audit_queue.json"
REAUDIT_CANDIDATES_PATH = AUDIT_DIR / "data" / "reaudit_candidates.json"
DISPATCH_QUEUE_PATH = AUDIT_DIR / "data" / "audit_dispatch_queue.json"
CANONICAL_DISPATCH_QUEUE_PATH = DISPATCH_QUEUE_PATH
PROMPT_TEMPLATE_PATH = AUDIT_DIR / "AUDIT_AGENT_PROMPT_TEMPLATE.md"
APPLY_AUDIT_SCRIPT = AUDIT_DIR / "scripts" / "apply_audit.py"
PIPELINE_SCRIPT = AUDIT_DIR / "scripts" / "run_pipeline.sh"
ISOLATED_BASE = Path("/tmp/codex-audit-isolated")
LOG_DIR = REPO_ROOT / "logs" / "codex-audit-runs"
DISPATCH_ALLOWED_PROCESS_PATHS = {
    "docs/audit/README.md",
    "docs/audit/FRESH_LOOK_REQUIREMENTS.md",
    "docs/audit/AUDIT_AGENT_PROMPT_TEMPLATE.md",
    "docs/audit/ALGEBRAIC_DECORATION_POLICY.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/audit/data/derivation_obligations.json",
}

# These fields are NOT controlled by the LLM; we set them on the runner side.
# The runner selects the best available full Codex model at xhigh and records
# the exact model/family. The numeric floor is stable while newer frontier
# models are adopted automatically, as required by FRESH_LOOK_REQUIREMENTS.
# Independence is determined PER ROW (see determine_audit_role) because it
# depends on whether this is a first-pass (typically cross_family vs Claude
# autopilot authors) or a same-family second-pass (must be fresh_context).
AUDIT_REASONING_EFFORT = "xhigh"
MODEL_FALLBACK = "gpt-5.6-sol"
SUPPORTED_AUDIT_MODEL_RE = re.compile(
    r"gpt-(?P<version>\d+(?:\.\d+)*)(?:-sol)?$"
)

# Minimum audit-model rank (numeric tuple). The audit lane refuses to
# run on anything below this unless --allow-low-model is passed (a
# break-glass for testing only). A stale model cache, a misconfigured
# CODEX_AUDIT_MODEL env var, or a forced env override that points
# below the floor will all be rejected. Setting this to (5, 5) means
# only gpt-5.5 and newer are accepted.
MIN_AUDIT_MODEL_RANK = (5, 6)

# The prompt template promises source visibility, and several current
# runner-artifact blockers hinge on elided load-bearing functions. Keep the
# packet bounded, but high enough to include the largest ordinary runners and
# helpers now used by the audit queue.
RUNNER_SOURCE_CHAR_LIMIT = 40_000
HELPER_SOURCE_CHAR_LIMIT = 40_000
NOTE_BODY_CHAR_LIMIT = 30_000
AUTHORITY_TOTAL_CHAR_LIMIT = 60_000
AUTHORITY_PER_NOTE_MAX = 10_000
AUTHORITY_PER_NOTE_MIN = 2_000
CLIPPED_EVIDENCE_MARKERS = (
    "... [packet-clipped ",
    "... [truncated; runner is ",
    "... [truncated; helper is ",
    "[runner stdout clipped; ",
    "[runner cache excerpt clipped; ",
)
INDEPENDENT_N7_RESOLUTION_MARKER = "N7_STEELMAN_RESOLUTION"
# Roles whose evidence must be complete (unclipped) before an audited_clean
# verdict may rest on it. Keep in sync with
# docs/audit/scripts/apply_audit.py LOAD_BEARING_EVIDENCE_ROLES.
LOAD_BEARING_EVIDENCE_ROLES = {
    "source", "authority", "runner", "helper", "runner_stdout",
    "runner_stdout_cache_eligible", "runner_stdout_independent",
}

# Codex rejects turn input above 1,048,576 characters. Keep a safety margin
# for transport framing. Only the rendered N8 candidate list may be bounded;
# validate/apply receive that exact rendered subset plus a digest/count
# commitment that reauthenticates it as the deterministic prefix of the
# complete orchestrator index. The fallback is explicitly non-clean.
CODEX_INPUT_CHAR_LIMIT = 1_000_000
CODEX_HARD_INPUT_CHAR_LIMIT = 1_048_576
OUTPUT_INSTRUCTIONS_MARKER = "\n\n---\nOUTPUT INSTRUCTIONS (binding):"


def prompt_exceeds_hard_input_limit(prompt: str) -> bool:
    return len(prompt) > CODEX_HARD_INPUT_CHAR_LIMIT


def clip_packet_text(text: str, limit: int, label: str) -> str:
    """Deterministically retain head/tail evidence within a packet budget."""
    if len(text) <= limit:
        return text
    head = text[: limit // 2]
    tail = text[-limit // 2 :]
    return (
        f"{head}\n\n... [packet-clipped {label}; {len(text)} chars total] ...\n\n"
        f"{tail}"
    )


def _meets_floor(model: str | None) -> bool:
    """True if model parses to a rank >= MIN_AUDIT_MODEL_RANK."""
    if not model or not SUPPORTED_AUDIT_MODEL_RE.fullmatch(model):
        return False
    rank = _model_rank(model)
    if not rank:
        return False
    floor = MIN_AUDIT_MODEL_RANK
    width = max(len(rank), len(floor))
    rank_padded = rank + (0,) * (width - len(rank))
    floor_padded = floor + (0,) * (width - len(floor))
    return rank_padded >= floor_padded


def codex_family_for_model(model: str) -> str:
    """Return the canonical ledger family while preserving model detail elsewhere.

    Audit model slugs may carry a serving/runtime suffix (for example
    "gpt-5.6-sol"), but apply_audit.py deliberately validates the stable
    numeric family namespace (for example "codex-gpt-5.6"). The exact slug
    is still written separately as "auditor_model" on every audit row.
    """
    match = SUPPORTED_AUDIT_MODEL_RE.fullmatch(model)
    if match:
        return f"codex-gpt-{match.group('version')}"
    return f"codex-{model}"


def canonicalize_existing_auditor_family(family: str | None) -> str | None:
    """Normalize a previously recorded Codex family for role comparison."""
    if not family or not family.startswith("codex-"):
        return family
    return codex_family_for_model(family.removeprefix("codex-"))


def _model_rank(model: str) -> tuple[int, ...]:
    """Extract a numeric GPT rank, e.g. gpt-5.5 -> (5, 5)."""
    m = re.match(r"gpt-(\d+(?:\.\d+)*)", model)
    if not m:
        return ()
    return tuple(int(part) for part in m.group(1).split("."))


def _model_newer_than(left: str, right: str) -> bool:
    left_rank = _model_rank(left)
    right_rank = _model_rank(right)
    if not left_rank or not right_rank:
        return False
    width = max(len(left_rank), len(right_rank))
    left_padded = left_rank + (0,) * (width - len(left_rank))
    right_padded = right_rank + (0,) * (width - len(right_rank))
    return left_padded > right_padded


def _reasoning_efforts(model_info: dict) -> set[str]:
    levels = model_info.get("reasoning_levels") or model_info.get("supported_reasoning_levels") or []
    efforts = set()
    for level in levels:
        if isinstance(level, dict) and level.get("effort"):
            efforts.add(str(level["effort"]))
        elif isinstance(level, str):
            efforts.add(level)
    return efforts


def _is_full_gpt_audit_model(model_info: dict) -> bool:
    slug = str(model_info.get("slug") or "")
    if not SUPPORTED_AUDIT_MODEL_RE.fullmatch(slug):
        return False
    lowered = slug.lower()
    if any(part in lowered for part in ("mini", "spark", "auto-review")):
        return False
    return AUDIT_REASONING_EFFORT in _reasoning_efforts(model_info)


def best_cached_codex_model() -> tuple[str | None, str | None]:
    """Return the strongest cached full GPT model by numeric GPT version."""
    codex_home = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex"))
    cache_path = codex_home / "models_cache.json"
    try:
        cache = json.loads(cache_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return None, f"could not read {cache_path}: {exc}"

    models = cache.get("models") or []
    if not isinstance(models, list):
        return None, f"{cache_path} has no models list"
    candidates: list[tuple[tuple[int, ...], int, int, str]] = []
    for index, model_info in enumerate(models):
        if not isinstance(model_info, dict) or not _is_full_gpt_audit_model(model_info):
            continue
        slug = str(model_info["slug"])
        rank = _model_rank(slug)
        if not rank:
            continue
        try:
            priority = int(model_info.get("priority", index))
        except (TypeError, ValueError):
            priority = index
        candidates.append((rank, -priority, -index, slug))
    if candidates:
        _, _, _, slug = max(candidates)
        return slug, f"selected from {cache_path}"
    return None, f"no full GPT model with {AUDIT_REASONING_EFFORT} reasoning found in {cache_path}"


def resolve_audit_model() -> tuple[str, str, str, list[str]]:
    """Return the best available full audit model and provenance contract."""
    warnings: list[str] = []
    detected, detected_note = best_cached_codex_model()
    configured = os.environ.get("CODEX_AUDIT_MODEL")
    forced = os.environ.get("CODEX_AUDIT_FORCE_MODEL")

    selected = detected
    source = detected_note or "local model cache"
    if forced:
        selected = forced
        source = "CODEX_AUDIT_FORCE_MODEL break-glass override"
        warnings.append(f"Using explicit break-glass model override {forced!r}.")
    elif configured:
        if selected is None or _model_newer_than(configured, selected):
            selected = configured
            source = "CODEX_AUDIT_MODEL newer than cached best"
        elif configured != selected:
            warnings.append(
                f"Ignoring stale CODEX_AUDIT_MODEL={configured!r}; cached best is "
                f"{selected!r}."
            )
    if selected is None:
        selected = MODEL_FALLBACK
        source = f"fallback after cache discovery failure: {detected_note}"
        warnings.append(f"Falling back to {MODEL_FALLBACK!r}; cache discovery failed.")
    return selected, codex_family_for_model(selected), source, warnings


# Statuses where this runner SHOULD NOT proceed automatically. Disagreements
# and three-way disagreements need a judicial third-auditor pass that the
# operator runs manually (per docs/audit/FRESH_LOOK_REQUIREMENTS.md and
# apply_audit.py's apply_judicial_review path).
SKIP_BLOCKERS = {
    "cross_confirmation_disagreement",
    "third_auditor_disagreement",
    "judicial_review_irresolvable",
}

REQUIRED_VERDICT_FIELDS = {
    "claim_id",
    "load_bearing_step",
    "load_bearing_step_class",
    "claim_type",
    "claim_scope",
    "chain_closes",
    "chain_closure_explanation",
    "verdict",
    "verdict_rationale",
    "negative_assertion_classes",
}

# A validator-guided correction pass may repair evidence locators in the
# already-present structured N1-N8 packet, but it is not a second scientific
# audit.  Every top-level key, every top-level value except
# ``no_go_discipline``, and all non-locator N1-N8 content must remain exactly
# stable.  This also prevents the correction pass from injecting optional
# apply controls such as ``pre_audit_prose_fix`` or
# ``cross_confirmation_role``.
VALIDATION_REPAIR_MUTABLE_FIELD = "no_go_discipline"
VALIDATION_REPAIR_LOCATOR_FIELDS = {
    "evidence_path",
    "evidence_locator",
}

# Map JSON-extracted-from-stdout to apply_audit.py's input schema. apply_audit
# expects `verdict` etc. plus the runner-side fields auditor/auditor_family/
# independence/audit_date. Independence is determined per-row by the role.
def add_auditor_metadata(verdict_blob: dict, auditor_name: str,
                         auditor_family: str, independence: str,
                         auditor_model: str,
                         auditor_reasoning_effort: str) -> dict:
    blob = dict(verdict_blob)
    # Runner-side fields are authoritative — overwrite anything the model
    # may have placed in the JSON for these. The prompt schema does not
    # ask codex to return these, but a hallucination should not leak
    # through.
    blob["auditor"] = auditor_name
    blob["auditor_family"] = auditor_family
    # Stamp the exact model + reasoning effort the runner used. apply_audit
    # validates the stable numeric family against this exact model slug.
    blob["auditor_model"] = auditor_model
    blob["auditor_reasoning_effort"] = auditor_reasoning_effort
    blob["independence"] = independence
    blob["audit_date"] = datetime.now(timezone.utc).isoformat()
    # Some downstream callers want runner_check_breakdown even when missing.
    blob.setdefault("runner_check_breakdown", {"A": 0, "B": 0, "C": 0, "D": 0, "total_pass": 0})
    return blob


def row_auditor_identity(
    auditor_name_base: str, run_id: str, claim_id: str, row_index: int
) -> str:
    return f"{auditor_name_base}-{run_id}-{claim_id[:24]}-{row_index:03d}"


def determine_audit_role(led_row: dict, auditor_family: str,
                         is_reaudit_candidate: bool = False,
                         is_dispatch_target: bool = False) -> tuple[str, str | None]:
    """Decide what role this audit attempt plays for the given row.

    The runner only audits rows that genuinely need an audit. Re-auditing
    already-clean / already-conditional / already-failed / already-confirmed
    rows is a waste of subscription messages and produces churn — all
    existing audits in this repo were already done at xhigh, so re-doing
    them adds no quality. We skip them.

    EXCEPTION: when ``is_reaudit_candidate=True``, the caller has explicitly
    pulled this row from ``reaudit_candidates.json`` because either its
    deps have strengthened or its runner SHA has drifted. The new audit
    supersedes the prior verdict; we record independence relative to the
    recorded author family when known, and otherwise against the prior
    auditor for ordinary queue re-audits. Blind dispatches with unknown
    authorship are conservatively marked weak.

    Returns (role, reason_or_independence):
      - ("skip", "<reason>")              row should be skipped
      - ("first", "cross_family")         row is unaudited; Codex on a
                                          Claude/human-authored note is
                                          cross-family
      - ("second", "fresh_context")       row is awaiting cross-confirmation
                                          and the first auditor was Codex
                                          (same model family)
      - ("second", "cross_family")        row is awaiting cross-confirmation
                                          and the first auditor was a
                                          different family (Claude / human)
      - ("reaudit", "fresh_context"|"cross_family"|"weak")
                                          re-audit candidate; supersedes
                                          prior verdict. Independence is
                                          fresh_context vs same-family
                                          prior auditor, cross_family vs
                                          different-family prior auditor

    apply_audit.py validates the independence rule; we precompute here so
    the metadata is always correct on the first try.
    """
    audit_status = led_row.get("audit_status") or "unknown"
    blocker = led_row.get("blocker") or ""
    cc = led_row.get("cross_confirmation") or {}
    if not isinstance(cc, dict):
        cc = {}
    cc_status = cc.get("status")

    # Skip rows that need judicial / human resolution.
    if blocker in SKIP_BLOCKERS:
        return "skip", f"blocker={blocker} (judicial review needed; manual)"
    if cc_status in {"disagreement", "three_way_disagreement", "disagreement_irresolvable"}:
        return "skip", f"cross_confirmation.status={cc_status} (judicial review needed; manual)"

    # Second-pass on a critical-row first audit that is awaiting cross-confirmation.
    if audit_status == "audit_in_progress" and cc_status == "awaiting_second":
        first_audit = cc.get("first_audit") or {}
        first_family = first_audit.get("auditor_family") if isinstance(first_audit, dict) else None
        if (
            canonicalize_existing_auditor_family(first_family)
            == canonicalize_existing_auditor_family(auditor_family)
        ):
            return "second", "fresh_context"
        return "second", "cross_family"

    # Re-audit pass: the caller pulled this row from reaudit_candidates.json
    # because deps strengthened or runner SHA drifted. The new audit
    # supersedes the prior verdict. Independence is determined against
    # whichever auditor produced the prior verdict.
    prior_family = led_row.get("auditor_family")
    if not prior_family:
        for prior in reversed(led_row.get("previous_audits") or []):
            if isinstance(prior, dict) and prior.get("auditor_family"):
                prior_family = prior["auditor_family"]
                break
    author_family = led_row.get("author_family")
    if is_reaudit_candidate and (prior_family or is_dispatch_target):
        if is_dispatch_target and not author_family:
            has_prior_audit = bool(
                prior_family
                or led_row.get("previous_audits")
                or audit_status != "unaudited"
            )
            return ("reaudit" if has_prior_audit else "first"), "weak"
        comparison_family = author_family or prior_family
        if (
            canonicalize_existing_auditor_family(comparison_family)
            == canonicalize_existing_auditor_family(auditor_family)
        ):
            return "reaudit", "fresh_context"
        return "reaudit", "cross_family"

    # First-pass: row has never been audited, including a dispatch target that
    # carries no live or archived prior auditor provenance.
    if audit_status == "unaudited":
        return "first", "cross_family"

    # Anything else — already at a terminal verdict (audited_clean,
    # audited_conditional, audited_failed, audited_renaming,
    # audited_decoration, audited_numerical_match), or already in a
    # confirmed cross_confirmation state, or in some other in-progress
    # state we don't auto-handle — SKIP. Re-auditing settled rows wastes
    # subscription messages without adding quality (existing audits were
    # already done at xhigh).
    cc_note = f" cc.status={cc_status}" if cc_status else ""
    return "skip", f"already at audit_status={audit_status}{cc_note}; not re-auditing"


def load_queue(criticality_filter: str | None = None,
               ready_only: bool = True) -> list[dict]:
    """Load the queue, optionally filtering to rows whose deps are all retained-grade.

    ready_only=True is the default: auditing a row whose deps are not
    retained-grade deterministically yields audited_conditional and burns a
    Codex call without compounding progress. The 'ready' flag in the queue
    encodes the dep-readiness condition computed by compute_audit_queue.py.
    Pass --allow-blocked to opt into auditing blocked rows anyway.
    """
    q = json.loads(QUEUE_PATH.read_text(encoding="utf-8"))
    rows = q.get("queue", [])
    if criticality_filter:
        rows = [r for r in rows if (r.get("criticality") or "") == criticality_filter]
    if ready_only:
        rows = [r for r in rows if r.get("ready")]
    # rows are already pre-sorted by descending score in audit_queue.json
    return rows


def select_named_targets(queue: list[dict], claim_ids: list[str]) -> list[dict]:
    """Select exact queue rows in caller order, rejecting missing/duplicate ids."""
    if len(claim_ids) != len(set(claim_ids)):
        duplicates = sorted({cid for cid in claim_ids if claim_ids.count(cid) > 1})
        raise ValueError(f"duplicate --claim-id values: {', '.join(duplicates)}")
    by_id = {row.get("claim_id"): row for row in queue if row.get("claim_id")}
    missing = [cid for cid in claim_ids if cid not in by_id]
    if missing:
        raise ValueError(
            "requested claim ids are absent from the selected queue/filter: "
            + ", ".join(missing)
        )
    return [by_id[cid] for cid in claim_ids]


def load_reaudit_candidates(criticality_filter: str | None = None,
                            include_runner_drift: bool = True) -> list[dict]:
    """Load rows from reaudit_candidates.json, sorted by leverage.

    The pipeline writes two streams to that file:

    - `candidates`: rows whose audit was non-clean and where every current
      dep is now retained-grade. Re-audit may now close the chain.
    - `runner_drift_candidates`: rows whose audit cited a runner_artifact_issue
      and whose runner SHA has changed since audit time.

    Both are valid re-audit triggers. Each entry is normalized into the
    same shape as audit_queue.json rows (claim_id, note_path, runner_path,
    deps, criticality, etc.) so the rest of the runner can treat them
    uniformly. The `ready` flag is set to True because this alternate source
    has already been prefiltered by the re-audit-candidate producer; runner
    drift rows may still get a non-clean verdict if a different blocker
    remains.
    """
    payload = json.loads(REAUDIT_CANDIDATES_PATH.read_text(encoding="utf-8"))
    streams: list[dict] = []
    streams.extend(payload.get("candidates", []))
    if include_runner_drift:
        streams.extend(payload.get("runner_drift_candidates", []))

    if criticality_filter:
        streams = [
            r for r in streams
            if (r.get("criticality") or "") == criticality_filter
        ]

    # Normalize: ensure each row has the queue-shape fields the audit
    # runner expects. Most are already present; ready=True is implied.
    normalized: list[dict] = []
    seen_ids: set[str] = set()
    for r in streams:
        cid = r.get("claim_id")
        if not cid or cid in seen_ids:
            continue
        seen_ids.add(cid)
        out = dict(r)
        out["ready"] = True
        out.setdefault("queue_reason", "reaudit_candidate")
        out.setdefault("audit_status", r.get("audit_status") or "unaudited")
        normalized.append(out)

    # Sort by criticality_rank desc, then transitive_descendants desc,
    # then load_bearing_score desc — matches compute_audit_queue ordering.
    normalized.sort(
        key=lambda e: (
            -(e.get("criticality_rank") or 0),
            -(e.get("transitive_descendants") or 0),
            -(e.get("load_bearing_score") or 0.0),
        )
    )
    return normalized


def load_dispatch_targets(
    ledger_rows: dict[str, dict],
    criticality_filter: str | None = None,
    ready_only: bool = True,
    selected_claim_ids: set[str] | None = None,
    limit: int | None = None,
) -> list[dict]:
    """Load live targeted re-audits without exposing the dispatch manifest.

    Dispatch metadata selects the claim. Its operator question remains log
    metadata and is never rendered into the auditor packet. The restricted
    evidence packet is built exclusively from the ledger row,
    source/dependencies, runner surfaces, and standard audit context.
    """
    payload = json.loads(DISPATCH_QUEUE_PATH.read_text(encoding="utf-8"))
    if payload.get("schema") != "audit_dispatch_queue.v1":
        raise ValueError("dispatch queue has unsupported or missing schema")
    if payload.get("policy") != "target_selection_only_not_audit_evidence":
        raise ValueError("dispatch queue has unsupported or missing policy")
    actual_live = payload.get("live")
    if not isinstance(actual_live, list):
        raise ValueError("dispatch queue live entries must be a list")
    if DISPATCH_QUEUE_PATH.resolve() == CANONICAL_DISPATCH_QUEUE_PATH.resolve():
        expected_payload = compute_audit_dispatch_queue.build_output(ledger_rows)
        if actual_live != expected_payload.get("live", []):
            raise ValueError(
                "canonical dispatch live entries do not exactly match current "
                "sidecars and ledger"
            )
        expected_live = {
            entry.get("claim_id"): entry
            for entry in expected_payload.get("live", [])
            if isinstance(entry, dict) and entry.get("claim_id")
        }
        actual_selected: dict[str, dict] = {}
        for entry in actual_live:
            if not isinstance(entry, dict):
                continue
            cid = entry.get("claim_id")
            if not cid or (
                selected_claim_ids is not None and cid not in selected_claim_ids
            ):
                continue
            if cid in actual_selected:
                raise ValueError(f"dispatch queue repeats selected claim_id {cid}")
            actual_selected[cid] = entry
        ids_to_authenticate = (
            selected_claim_ids
            if selected_claim_ids is not None
            else set(expected_live)
        )
        for cid in ids_to_authenticate:
            if actual_selected.get(cid) != expected_live.get(cid):
                raise ValueError(
                    f"dispatch target {cid} does not match current sidecars and ledger"
                )
    normalized: list[dict] = []
    seen_ids: set[str] = set()
    for entry in payload.get("live", []):
        if not isinstance(entry, dict):
            continue
        cid = entry.get("claim_id")
        if not cid or cid in seen_ids:
            continue
        if selected_claim_ids is not None and cid not in selected_claim_ids:
            continue
        if ready_only and not entry.get("ready"):
            continue
        ledger_row = ledger_rows.get(cid)
        if not isinstance(ledger_row, dict):
            continue
        if criticality_filter and ledger_row.get("criticality") != criticality_filter:
            continue
        if limit is not None and len(normalized) >= limit:
            break
        row = dict(ledger_row)
        row["claim_id"] = cid
        row["dispatch_target"] = True
        row["dispatch_question"] = str(entry.get("audit_question") or "").strip()
        row["ready"] = bool(entry.get("ready"))
        row["ready_blocker"] = entry.get("ready_blocker")
        row["source_json_path"] = entry.get("source_json_path")
        row["source_schema"] = entry.get("source_schema")
        row["queue_reason"] = "targeted_dispatch"
        allowed_context_paths = entry.get("allowed_context_paths") or []
        if not isinstance(allowed_context_paths, list) or not all(
            isinstance(path, str) and path for path in allowed_context_paths
        ):
            raise ValueError(f"dispatch target {cid} has malformed allowed_context_paths")
        permitted_paths = set(DISPATCH_ALLOWED_PROCESS_PATHS)
        permitted_paths.update(filter(None, (
            ledger_row.get("note_path"),
            ledger_row.get("runner_path"),
        )))
        permitted_paths.update(ledger_row.get("helper_runner_paths") or [])
        for dep_id in ledger_row.get("deps") or []:
            dep_path = (ledger_rows.get(dep_id) or {}).get("note_path")
            if dep_path:
                permitted_paths.add(dep_path)
        try:
            premise_registry = json.loads(
                (AUDIT_DIR / "data" / "axiom_premise_nodes.json").read_text(
                    encoding="utf-8"
                )
            )
        except (OSError, json.JSONDecodeError) as exc:
            raise ValueError("cannot validate dispatch allowed_context_paths") from exc
        permitted_paths.update(
            str(node.get("current_path"))
            for node in (premise_registry.get("nodes") or {}).values()
            if node.get("current_path")
        )
        unexpected_paths = sorted(set(allowed_context_paths) - permitted_paths)
        if unexpected_paths:
            raise ValueError(
                f"dispatch target {cid} requests nonstandard context paths: "
                + ", ".join(unexpected_paths)
            )
        row["allowed_context_paths"] = list(allowed_context_paths)
        normalized.append(row)
        seen_ids.add(cid)
    return normalized


def load_ledger_rows() -> dict[str, dict]:
    ledger_io.ensure_cache()
    return json.loads(LEDGER_PATH.read_text(encoding="utf-8"))["rows"]


def only_awaiting_cross_confirmation(rows: list[dict],
                                     ledger_rows: dict[str, dict]) -> list[dict]:
    """Keep rows that are ready for an independent second audit only."""
    out: list[dict] = []
    for row in rows:
        cid = row.get("claim_id")
        if not cid:
            continue
        led_row = ledger_rows.get(cid, {})
        cc = led_row.get("cross_confirmation") or {}
        if (
            led_row.get("audit_status") == "audit_in_progress"
            and led_row.get("blocker") == "awaiting_cross_confirmation"
            and isinstance(cc, dict)
            and cc.get("status") == "awaiting_second"
        ):
            out.append(row)
    return out


def read_note_body(note_path: str) -> str | None:
    p = REPO_ROOT / note_path
    if not p.exists():
        return None
    return p.read_text(encoding="utf-8", errors="replace")


def prior_claim_scope_for_row(row: dict) -> str | None:
    scope = row.get("claim_scope")
    if isinstance(scope, str) and scope.strip():
        return scope
    for archived in reversed(row.get("previous_audits") or []):
        if not isinstance(archived, dict):
            continue
        scope = archived.get("claim_scope")
        if isinstance(scope, str) and scope.strip():
            return scope
    return None


# Timeout resolution is shared with the precompute helper. It honors
# `AUDIT_TIMEOUT_SEC = N` declared at the top of the runner, falling
# back to a small legacy substring map and finally to default_sec.

def runner_timeout_for(runner_path: str, default_sec: int) -> int:
    return rc.runner_timeout_for(runner_path, default_sec=default_sec)


def canonical_runner_path(runner_path: str | Path) -> str:
    """Map legacy runner references to checked-out repo-local runners.

    Historical ledger rows may carry bare script names or absolute paths from
    temporary worktrees. For audit prompt rendering, use the current checkout's
    ``scripts/<basename>.py`` when it exists; truly absent historical runners
    remain missing.
    """
    raw = str(runner_path).strip()
    if not raw:
        return raw
    raw_path = Path(raw)
    basename = raw_path.name

    candidates: list[str] = []
    if raw_path.is_absolute():
        if basename.endswith(".py"):
            candidates.append(f"scripts/{basename}")
    elif raw.startswith("scripts/"):
        candidates.append(raw)
    else:
        candidates.extend([raw, f"scripts/{raw}"])
    if basename.endswith(".py"):
        candidates.append(f"scripts/{basename}")

    seen: set[str] = set()
    for candidate in candidates:
        if candidate in seen:
            continue
        seen.add(candidate)
        p = REPO_ROOT / candidate
        if p.exists():
            return p.relative_to(REPO_ROOT).as_posix()
    return raw


def find_cached_runner_output(runner_path: str) -> str | None:
    """Return cached runner stdout via the SHA-pinned cache layout
    (`logs/runner-cache/<stem>.txt`). Returns None if no cache exists or
    if the cache header's `runner_sha256` does not match the runner's
    current SHA — a stale cache is treated as if absent. Refresh via
    `python3 scripts/precompute_audit_runners.py`.
    """
    if not runner_path:
        return None
    runner_path = canonical_runner_path(runner_path)
    return rc.cache_excerpt_for_audit(runner_path)


def get_runner_stdout(runner_path: str | None, default_timeout_sec: int,
                      use_cache: bool = False) -> str:
    """Get runner output, live by default.

    Source-SHA caches do not authenticate mutable note/data/registry inputs,
    so authority-bearing audit callers must keep ``use_cache=False``. The
    opt-in cache path remains for non-authoritative diagnostics.
    """
    if not runner_path:
        return ""
    runner_path = canonical_runner_path(runner_path)
    if use_cache:
        cached = find_cached_runner_output(runner_path)
        if cached:
            return cached
    p = REPO_ROOT / runner_path
    if not p.exists():
        return f"[runner missing on disk: {runner_path}]"
    timeout_sec = runner_timeout_for(runner_path, default_timeout_sec)
    try:
        res = subprocess.run(
            [sys.executable, str(p)],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            timeout=timeout_sec,
            env={**os.environ, "PYTHONPATH": str(REPO_ROOT / "scripts")},
        )
        if res.returncode != 0:
            return f"[runner exit={res.returncode}]\n{res.stdout[-3000:]}\n--- stderr ---\n{res.stderr[-1500:]}"
        if len(res.stdout) > 6000:
            return (
                f"[runner stdout clipped; {len(res.stdout)} chars total]\n"
                f"{res.stdout[-6000:]}"
            )
        return res.stdout
    except subprocess.TimeoutExpired:
        return f"[runner timed out at {timeout_sec}s — likely needs compute-rerun]"
    except Exception as e:
        return f"[runner error: {e}]"


def repo_local_helper_runner_path(runner_path: str) -> tuple[str, Path] | None:
    """Resolve a helper to a regular ``scripts/`` file contained by the repo."""
    canonical = canonical_runner_path(runner_path)
    relative = Path(canonical)
    if (
        relative.is_absolute()
        or not relative.parts
        or relative.parts[0] != "scripts"
        or ".." in relative.parts
    ):
        return None
    try:
        root = REPO_ROOT.resolve()
        scripts_root = (root / "scripts").resolve()
        resolved = (root / relative).resolve()
        # Fail closed on symlinked helpers: the resolved target must stay
        # inside BOTH the repo root and the resolved scripts/ directory, so a
        # lexically valid scripts/ entry cannot point elsewhere in the repo.
        resolved.relative_to(root)
        resolved.relative_to(scripts_root)
    except (OSError, ValueError):
        return None
    if not resolved.is_file():
        return None
    return canonical, resolved


def get_independent_runner_stdout(
    runner_path: str,
    default_timeout_sec: int,
) -> tuple[str, bool]:
    """Execute an N7 helper live and authenticate stdout after exit zero."""
    local_runner = repo_local_helper_runner_path(runner_path)
    if local_runner is None:
        return "[runner path rejected: not a repo-local scripts file]", False
    runner_path, path = local_runner
    timeout_sec = runner_timeout_for(runner_path, default_timeout_sec)
    try:
        result = subprocess.run(
            [sys.executable, str(path)],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            timeout=timeout_sec,
            env={**os.environ, "PYTHONPATH": str(REPO_ROOT / "scripts")},
        )
        if result.returncode != 0:
            return (
                f"[runner exit={result.returncode}]\n"
                f"{result.stdout[-3000:]}\n--- stderr ---\n"
                f"{result.stderr[-1500:]}",
                False,
            )
        if len(result.stdout) > 6000:
            return (
                f"[runner stdout clipped; {len(result.stdout)} chars total]\n"
                f"{result.stdout[-6000:]}",
                True,
            )
        return result.stdout, True
    except subprocess.TimeoutExpired:
        return f"[runner timed out at {timeout_sec}s — likely needs compute-rerun]", False
    except Exception as error:
        return f"[runner error: {error}]", False


def render_prompt(row: dict, ledger_rows: dict[str, dict],
                  template: str, runner_timeout_sec: int,
                  use_cache: bool = False,
                  skip_runner_stdout: bool = False,
                  evidence_manifest_out: dict[str, dict] | None = None,
                  audit_invocation_id: str | None = None) -> str:
    """Substitute the prompt template's variables for one queue row.

    If ``skip_runner_stdout`` is True, do NOT invoke the runner subprocess
    or read a cached log; instead substitute a placeholder. Section 3a
    (runner source code) is still rendered so the auditor retains code
    visibility — only the live stdout block is suppressed.
    """
    cid = row["claim_id"]
    note_path = row.get("note_path") or ledger_rows.get(cid, {}).get("note_path") or ""
    raw_runner_path = row.get("runner_path") or ledger_rows.get(cid, {}).get("runner_path") or ""
    runner_path = canonical_runner_path(raw_runner_path) if raw_runner_path else ""
    ledger_claim_type = (
        row.get("claim_type")
        or ledger_rows.get(cid, {}).get("claim_type")
        or ""
    )
    claim_type_hint = (
        "(withheld for fresh context)"
        if row.get("dispatch_target")
        else ledger_claim_type
    )

    full_note_body = read_note_body(note_path) or f"[note missing on disk: {note_path}]"
    no_go_required = no_go_discipline_gate.source_requires_no_go_discipline(
        note_path,
        full_note_body,
        "" if row.get("dispatch_target") else ledger_claim_type,
    )
    no_go_artifact = no_go_discipline_gate.source_is_no_go_artifact(
        note_path,
        full_note_body,
        "" if row.get("dispatch_target") else ledger_claim_type,
    )
    note_body = clip_packet_text(full_note_body, NOTE_BODY_CHAR_LIMIT, note_path)

    # Cited authorities: one-hop deps from the ledger row
    led_row = ledger_rows.get(cid, {})
    if row.get("dispatch_target"):
        prior_claim_scope = no_go_discipline_gate.BLIND_REAUDIT_PRIOR_SCOPE
    else:
        prior_claim_scope = prior_claim_scope_for_row(led_row) or "(none recorded)"
    packet_row = {**led_row, **row, "claim_id": cid}
    if row.get("dispatch_target"):
        # Fresh dispatch packets may use operational ledger state for target
        # selection, but not as auditor evidence or search seeding.
        packet_row = no_go_discipline_gate.blind_reaudit_row_projection(
            packet_row
        )
    evidence_manifest = no_go_discipline_gate.build_evidence_manifest(
        packet_row, ledger_rows, REPO_ROOT
    )
    if row.get("dispatch_target"):
        no_go_discipline_gate.set_packet_evidence(
            evidence_manifest,
            path=no_go_discipline_gate.blind_reaudit_control_path(cid),
            role="blind_reaudit_control",
            text=(
                "Fresh-context dispatch: prior claim scope and audit judgments "
                "are withheld from the auditor."
            ),
        )
    no_go_discipline_gate.set_packet_evidence(
        evidence_manifest, path=note_path, role="source", text=note_body,
        invocation_bound_rendered_text=True,
    )
    premise_context = no_go_discipline_gate.render_framework_premise_context(
        evidence_manifest
    )
    deps = led_row.get("deps", [])
    authority_limit = min(
        AUTHORITY_PER_NOTE_MAX,
        max(AUTHORITY_PER_NOTE_MIN, AUTHORITY_TOTAL_CHAR_LIMIT // max(1, len(deps))),
    )
    cited_blocks = []
    for dep_cid in deps:
        dep_row = ledger_rows.get(dep_cid, {})
        dep_path = dep_row.get("note_path") or ""
        dep_body = clip_packet_text(
            read_note_body(dep_path) or f"[dep note missing: {dep_path}]",
            authority_limit,
            dep_path,
        )
        no_go_discipline_gate.set_packet_evidence(
            evidence_manifest,
            path=dep_path,
            role="authority",
            text=dep_body,
            effective_status=dep_row.get("effective_status"),
            premise_type=no_go_discipline_gate.premise_type_for_id(REPO_ROOT, dep_cid),
            invocation_bound_rendered_text=True,
        )
        eff = dep_row.get("effective_status") or "unaudited"
        ct = dep_row.get("claim_type") or "?"
        accepted = False
        accepted_type = "none"
        bounds_downstream = False
        if premise_nodes.is_axiom_premise(dep_cid):
            accepted = True
            accepted_type = "axiom_or_approved_primitive"
        premise_lines = (
            f"=== Cited authority accepted_premise: {str(accepted).lower()} ===\n"
            f"=== Cited authority accepted_premise_type: {accepted_type} ===\n"
            f"=== Cited authority bounds_downstream: {str(bounds_downstream).lower()} ===\n"
            f"=== Cited authority axiom_premise: "
            f"{str(accepted_type == 'axiom_or_approved_primitive').lower()} ===\n"
        )
        cited_blocks.append(
            f"=== BEGIN CITED AUTHORITY: {dep_path} ===\n"
            f"=== Cited authority effective_status: {eff} ===\n"
            f"=== Cited authority claim_type: {ct} ===\n"
            f"{premise_lines}"
            f"{dep_body}\n"
            f"=== END CITED AUTHORITY: {dep_path} ==="
        )
    cited_str = "\n\n".join(cited_blocks) if cited_blocks else "(no cited authorities — load-bearing step must derive from axiom)"

    if skip_runner_stdout:
        # --no-runner mode: do not run the subprocess and do not consult the
        # cache. The auditor still gets Section 3a (runner source code) and
        # may return COMPUTE_REQUIRED if the missing stdout is load-bearing.
        runner_stdout = "(stdout suppressed by --no-runner)"
    else:
        # Negative authority requires evidence from this audit cycle. A
        # runner-SHA cache is useful for ordinary review, but it does not bind
        # transitive inputs and therefore cannot certify N1/N5 execution.
        runner_stdout = get_runner_stdout(
            runner_path,
            runner_timeout_sec,
            use_cache=(use_cache and not no_go_required),
        )
    runner_stdout_path = no_go_discipline_gate.runner_stdout_evidence_path(cid)
    if skip_runner_stdout:
        runner_stdout_role = "runner_stdout_suppressed"
    elif no_go_required or not use_cache:
        runner_stdout_role = "runner_stdout"
    else:
        # Conservative provenance: this call may have used the SHA-only cache.
        # If the model later emits an output-side negative claim, N1/N5 must
        # reject this surface and the row must be rerun with --no-cache.
        runner_stdout_role = "runner_stdout_cache_eligible"
    no_go_discipline_gate.set_packet_evidence(
        evidence_manifest,
        path=runner_stdout_path,
        role=runner_stdout_role,
        text=runner_stdout or "(no stdout captured)",
    )

    # Read the runner source code so the auditor can inspect what the runner
    # actually does, not just what it printed. Catches fake-pass runners
    # (hard-coded PASS lines, trivial assertions) and lets the auditor
    # validate class C/A/B/D against the actual code rather than trusting
    # the static heuristic in classify_runner_passes.py.
    runner_source = ""
    if runner_path:
        rp = REPO_ROOT / runner_path
        if rp.exists():
            try:
                src = rp.read_text(encoding="utf-8", errors="replace")
                if len(src) > RUNNER_SOURCE_CHAR_LIMIT:
                    head = src[: RUNNER_SOURCE_CHAR_LIMIT // 2]
                    tail = src[-RUNNER_SOURCE_CHAR_LIMIT // 2 :]
                    runner_source = (
                        f"{head}\n\n"
                        f"... [truncated; runner is {len(src)} chars total] ...\n\n"
                        f"{tail}"
                    )
                else:
                    runner_source = src
            except OSError as e:
                runner_source = f"[could not read runner: {e}]"
        else:
            runner_source = f"[runner missing on disk: {runner_path}]"
    if runner_path:
        no_go_discipline_gate.set_packet_evidence(
            evidence_manifest,
            path=runner_path,
            role="runner",
            text=runner_source or "(no source available)",
            invocation_bound_rendered_text=True,
        )

    # Read each transitive helper script the primary runner imports (via
    # build_citation_graph's helper_runner_paths field on the ledger row).
    # Without including these, the auditor sees opaque imports and is forced
    # into class (C) on packet-incompleteness grounds even when the chain is
    # sound. See AUDIT_AGENT_PROMPT_TEMPLATE.md §3b for the auditor-side
    # protocol.
    raw_helper_runner_paths = (
        row.get("helper_runner_paths")
        or ledger_rows.get(cid, {}).get("helper_runner_paths")
        or []
    )
    # Canonical-deduplicate helper paths before execution. Two declarations of
    # the same helper resolve to one independent-stdout evidence surface, so a
    # second (possibly failing) invocation would re-render that entry's text
    # while the first invocation's authenticated role stays attached — leaving
    # an authenticated `runner_stdout_independent` role beside a markerless
    # failure tail. Dedup keeps each helper's authenticated role bound to
    # exactly one live invocation. The citation-graph producer already emits
    # unique helper lists, but this must not depend on that convention.
    helper_runner_paths: list[str] = []
    _seen_helper_canonical: set[str] = set()
    for _hp_raw in raw_helper_runner_paths:
        _hp_canonical = canonical_runner_path(_hp_raw)
        if _hp_canonical in _seen_helper_canonical:
            continue
        _seen_helper_canonical.add(_hp_canonical)
        helper_runner_paths.append(_hp_raw)
    helper_sources_blocks: list[str] = []
    for hp_raw in helper_runner_paths:
        hp = canonical_runner_path(hp_raw)
        local_helper = repo_local_helper_runner_path(hp)
        if local_helper is None:
            rejected_path = (
                "audit-packet://rejected-helper/"
                f"{cid}/"
                f"{hashlib.sha256(str(hp).encode('utf-8')).hexdigest()[:16]}"
            )
            helper_block = (
                f"=== BEGIN REJECTED HELPER: {rejected_path} ===\n"
                "[helper rejected: path is not a repo-local scripts file]\n"
                f"=== END REJECTED HELPER: {rejected_path} ==="
            )
            helper_sources_blocks.append(helper_block)
            no_go_discipline_gate.set_packet_evidence(
                evidence_manifest,
                path=rejected_path,
                role="helper_rejected",
                text=helper_block,
                invocation_bound_rendered_text=True,
            )
            continue
        hp, full_hp = local_helper
        try:
            hsrc = full_hp.read_text(encoding="utf-8", errors="replace")
            helper_declares_independent_resolution = (
                INDEPENDENT_N7_RESOLUTION_MARKER in hsrc
            )
            if len(hsrc) > HELPER_SOURCE_CHAR_LIMIT:
                head = hsrc[: HELPER_SOURCE_CHAR_LIMIT // 2]
                tail = hsrc[-HELPER_SOURCE_CHAR_LIMIT // 2 :]
                hsrc = (
                    f"{head}\n\n"
                    f"... [truncated; helper is {len(hsrc)} chars total] ...\n\n"
                    f"{tail}"
                )
            independent_stdout_block = ""
            # The explicit marker opts into live independent N7 evidence for
            # no-go artifacts and supplied development-tier packets.  A
            # forensic positive row remains unable to self-certify this way.
            if helper_declares_independent_resolution and (
                no_go_artifact or not no_go_required
            ):
                independent_stdout_path = (
                    no_go_discipline_gate.independent_runner_stdout_evidence_path(
                        cid, hp
                    )
                )
                if skip_runner_stdout:
                    independent_stdout = (
                        "(independent helper stdout suppressed by --no-runner)"
                    )
                    independent_stdout_role = (
                        "runner_stdout_independent_suppressed"
                    )
                else:
                    independent_stdout, independent_stdout_authenticated = (
                        get_independent_runner_stdout(hp, runner_timeout_sec)
                    )
                    independent_stdout_role = (
                        "runner_stdout_independent"
                        if independent_stdout_authenticated
                        else "runner_stdout_independent_failed"
                    )
                no_go_discipline_gate.set_packet_evidence(
                    evidence_manifest,
                    path=independent_stdout_path,
                    role=independent_stdout_role,
                    text=independent_stdout or "(no stdout captured)",
                )
                independent_stdout_block = (
                    "\n=== BEGIN INDEPENDENT HELPER STDOUT: "
                    f"{independent_stdout_path} ===\n"
                    f"{independent_stdout or '(no stdout captured)'}\n"
                    "=== END INDEPENDENT HELPER STDOUT: "
                    f"{independent_stdout_path} ==="
                )
            hcache = (
                "(helper cache is not audit authority; current helper source "
                "is inspected and marked N7 helpers are executed live)"
            )
            helper_block = (
                f"=== BEGIN HELPER RUNNER: {hp} ===\n"
                f"{hsrc}\n"
                f"=== BEGIN HELPER RUNNER CACHE: {hp} ===\n"
                f"{hcache}\n"
                f"=== END HELPER RUNNER CACHE: {hp} ===\n"
                f"{independent_stdout_block}\n"
                f"=== END HELPER RUNNER: {hp} ==="
            )
            helper_sources_blocks.append(helper_block)
            no_go_discipline_gate.set_packet_evidence(
                evidence_manifest, path=hp, role="helper", text=helper_block,
                invocation_bound_rendered_text=True,
            )
        except OSError as e:
            helper_block = (
                f"=== BEGIN HELPER RUNNER: {hp} ===\n"
                f"[could not read helper: {e}]\n"
                f"=== END HELPER RUNNER: {hp} ==="
            )
            helper_sources_blocks.append(helper_block)
            no_go_discipline_gate.set_packet_evidence(
                evidence_manifest, path=hp, role="helper", text=helper_block,
                invocation_bound_rendered_text=True,
            )
    helper_runner_sources = (
        "\n\n".join(helper_sources_blocks)
        if helper_sources_blocks
        else "(no helper runner imports detected)"
    )

    cross_cycle_path = no_go_discipline_gate.cross_cycle_index_path(cid)
    cross_cycle_context = str(evidence_manifest[cross_cycle_path]["text"])
    partial_closure_path = no_go_discipline_gate.partial_closure_index_path(cid)
    partial_closure_context = str(evidence_manifest[partial_closure_path]["text"])
    evidence_manifest_text = no_go_discipline_gate.render_evidence_manifest(
        evidence_manifest
    )
    if evidence_manifest_out is not None:
        evidence_manifest_out.clear()
        evidence_manifest_out.update(evidence_manifest)

    # Render every template token in one regex pass. Python's ``re.sub`` does
    # not rescan replacement text, so literal template-looking strings inside
    # notes, runner output/source, helper source, authorities, or registry
    # context remain raw evidence instead of being expanded as another field.
    replacements = {
        "{{CLAIM_ID}}": cid,
        "{{AUDIT_INVOCATION_ID}}": audit_invocation_id or "",
        "{{NOTE_PATH}}": note_path,
        "{{CLAIM_TYPE_HINT}}": claim_type_hint or "(none)",
        "{{RUNNER_PATH}}": runner_path or "(none)",
        "{{NO_GO_DISCIPLINE_REQUIRED}}": "true" if no_go_required else "false",
        "{{PRIOR_CLAIM_SCOPE}}": prior_claim_scope,
        "{{NO_GO_EVIDENCE_MANIFEST}}": evidence_manifest_text,
        "{{NOTE_BODY}}": note_body,
        "{{RUNNER_STDOUT}}": runner_stdout or "(no stdout captured)",
        "{{RUNNER_STDOUT_EVIDENCE_PATH}}": runner_stdout_path,
        "{{RUNNER_SOURCE}}": runner_source or "(no source available)",
        "{{HELPER_RUNNER_SOURCES}}": helper_runner_sources,
        "{{FRAMEWORK_PREMISE_CONTEXT}}": premise_context,
        "{{NO_GO_PARTIAL_CLOSURE_INDEX}}": partial_closure_context,
        "{{NO_GO_CROSS_CYCLE_INDEX}}": cross_cycle_context,
    }
    foreach_pattern = (
        r"\{\{FOREACH cited_authority IN CITED_AUTHORITIES\}\}"
        r".*?\{\{ENDFOREACH\}\}"
    )
    token_pattern = "|".join(re.escape(token) for token in replacements)
    render_re = re.compile(f"(?:{foreach_pattern})|(?:{token_pattern})", re.DOTALL)

    def render_token(match: re.Match[str]) -> str:
        token = match.group(0)
        return replacements.get(token, cited_str)

    prompt = render_re.sub(render_token, template)

    # Append a tightening footer so we get clean JSON back. We DELIBERATELY
    # do not suppress the COMPUTE_REQUIRED escape — the audit-lane policy
    # in AUDIT_AGENT_PROMPT_TEMPLATE.md says runner timeouts / missing
    # compute must NOT be converted to terminal verdicts. If codex returns
    # COMPUTE_REQUIRED, the wrapper detects it and skips the row (no
    # apply, no commit, logged for compute-rerun follow-up).
    if row.get("dispatch_target"):
        prompt += (
            "\n\n---\n"
            "TARGETED DISPATCH TASK (neutral selection metadata; not evidence):\n"
            "Independently determine the claim type, exact scope, chain "
            "closure, and verdict from the authenticated framework packet. "
            "No dispatcher-authored question, suggested classification, prior "
            "rationale, status, or outcome is present in this auditor context. "
            "Decide the claim type, scope, and verdict only from the packet.\n"
        )
    prompt += (
        "\n\n---\n"
        "OUTPUT INSTRUCTIONS (binding):\n"
        "If the runner output is missing only because of timeout, missing\n"
        "stdout, or compute-budget exhaustion AND the load-bearing step\n"
        "cannot be judged without that completed run, return EXACTLY one\n"
        "line of the form:\n"
        "    COMPUTE_REQUIRED: <one sentence naming the missing run / cached\n"
        "    certificate / independent derivation needed>\n"
        "and nothing else. Do NOT fabricate a terminal verdict in that case.\n"
        "\n"
        "Otherwise, respond with EXACTLY one JSON object matching the schema\n"
        "in section 5. No markdown fences, no preamble, no explanation\n"
        "outside the JSON.\n"
    )
    return prompt


def fit_prompt_to_transport_limit(
    prompt: str,
    evidence_manifest: dict[str, dict],
    claim_id: str,
    *,
    max_chars: int = CODEX_INPUT_CHAR_LIMIT,
    forensic_bound: bool = True,
) -> tuple[str, dict[str, int] | None]:
    """Fit an oversized no-go prompt by bounding only rendered N8 records.

    Validation and apply receive the exact rendered subset plus a digest/count
    commitment to the complete orchestrator index. In the forensic tier, the
    inserted binding notice requires an incomplete N8 FAIL packet and forbids
    ``audited_clean``. In the development tier it only forbids exhaustive N8
    claims from the omitted records and does not force a verdict. If even an
    empty rendered candidate list cannot fit, fail closed instead of clipping
    source/runner evidence.
    """
    if len(prompt) <= max_chars:
        return prompt, None
    cross_path = no_go_discipline_gate.cross_cycle_index_path(claim_id)
    entry = evidence_manifest.get(cross_path)
    full_text = str((entry or {}).get("text") or "")
    if not full_text or prompt.count(full_text) != 1:
        raise ValueError(
            f"prompt is {len(prompt)} chars and has no uniquely rendered "
            "authenticated N8 index to transport-bound"
        )
    try:
        payload = json.loads(full_text)
    except json.JSONDecodeError as exc:
        raise ValueError("authenticated N8 index is not valid JSON") from exc
    candidates = payload.get("candidates")
    if not isinstance(candidates, list):
        raise ValueError("authenticated N8 index has no candidate list")

    def render(candidate_count: int) -> str:
        bounded = dict(payload)
        bounded["candidates"] = candidates[:candidate_count]
        bounded_text = json.dumps(bounded, indent=2, sort_keys=True)
        forensic_notice = (
            "Therefore set N8_cross_cycle_echo.packet_complete=false, keep "
            "N8_cross_cycle_echo.unresolved nonempty, set the overall "
            "no_go_discipline.status=FAIL, and do not return audited_clean. "
            if forensic_bound
            else
            "This development-tier transport bound does not force a verdict "
            "when the final classification carries no negative assertion. If "
            "you classify claim_type=no_go or declare any nonempty "
            "negative_assertion_classes, set "
            "N8_cross_cycle_echo.packet_complete=false, keep its unresolved "
            "list nonempty, set no_go_discipline.status=FAIL, and do not return "
            "audited_clean. Otherwise, scope any N8 judgment to the rendered "
            "records. "
        )
        notice = (
            "\n\n---\n"
            "N8 TRANSPORT BOUND (binding; transport metadata, not evidence):\n"
            f"The authenticated repository scan found {len(candidates)} "
            f"cross-cycle candidates; this transport renders the first "
            f"{candidate_count} in the orchestrator's relevance order while "
            "retaining the complete no-go-row universe count and digest. "
            f"{forensic_notice}"
            "Use only verbatim locators from rendered authenticated records.\n"
        )
        fitted = prompt.replace(full_text, bounded_text, 1)
        if OUTPUT_INSTRUCTIONS_MARKER not in fitted:
            raise ValueError("binding output-instructions marker is absent")
        return fitted.replace(
            OUTPUT_INSTRUCTIONS_MARKER,
            notice + OUTPUT_INSTRUCTIONS_MARKER,
            1,
        )

    low, high = 0, len(candidates)
    best: tuple[int, str] | None = None
    while low <= high:
        mid = (low + high) // 2
        fitted = render(mid)
        if len(fitted) <= max_chars:
            best = (mid, fitted)
            low = mid + 1
        else:
            high = mid - 1
    if best is None:
        zero = render(0)
        raise ValueError(
            f"prompt remains {len(zero)} chars after removing rendered N8 "
            "candidates; source/runner packet must be repaired or split"
        )
    shown, fitted_prompt = best
    bounded_payload = dict(payload)
    bounded_payload["candidates"] = candidates[:shown]
    bounded_text = json.dumps(bounded_payload, indent=2, sort_keys=True)
    # Validation/apply must authenticate exactly what the auditor saw, not the
    # omitted records. Preserve a digest/count commitment to the complete
    # orchestrator index so apply_audit can reauthenticate this deterministic
    # prefix against the current full index without claiming it was rendered.
    entry["text"] = bounded_text
    entry["transport_bounded_full_content_sha256"] = hashlib.sha256(
        full_text.encode("utf-8")
    ).hexdigest()
    entry["transport_bounded_full_candidate_count"] = len(candidates)
    entry["transport_bounded_rendered_candidate_count"] = shown
    entry["transport_bounded_rendered_candidate_ids"] = [
        str(candidate.get("candidate_id"))
        for candidate in candidates[:shown]
    ]
    return fitted_prompt, {
        "authenticated_candidates": len(candidates),
        "rendered_candidates": shown,
        "prompt_chars_before": len(prompt),
        "prompt_chars_after": len(fitted_prompt),
    }


def run_codex(prompt: str, isolated_dir: Path, timeout_sec: int,
              reasoning_effort: str | None = None,
              model: str | None = None) -> tuple[bool, str, str]:
    """Run `codex exec` in an isolated workdir. Returns (ok, stdout, stderr).

    reasoning_effort: low | medium | high | xhigh. Controls Codex internal
    reasoning depth. Lower = cheaper rate-limit cost per call. Default of
    None falls back to ~/.codex/config.toml (typically xhigh).
    """
    isolated_dir.mkdir(parents=True, exist_ok=True)
    cmd = ["codex", "exec", "--skip-git-repo-check"]
    last_message_path = isolated_dir / "codex-last-message.txt"
    cmd += ["--output-last-message", str(last_message_path)]
    if reasoning_effort:
        cmd += ["-c", f"model_reasoning_effort={reasoning_effort!r}"]
    if model:
        cmd += ["-c", f"model={model!r}"]
    cmd.append("-")
    try:
        # --skip-git-repo-check lets us run outside a repo.
        # We deliberately do NOT pass --cd because in our smoke test that
        # combination hung; running from the isolated dir as cwd is enough
        # to keep codex from reading the surrounding repo.
        proc = subprocess.run(
            cmd,
            input=prompt,
            cwd=isolated_dir,
            capture_output=True,
            text=True,
            timeout=timeout_sec,
        )
        if proc.returncode != 0:
            return False, proc.stdout, proc.stderr
        if last_message_path.exists():
            reply = last_message_path.read_text(
                encoding="utf-8", errors="replace"
            )
            return True, reply, proc.stderr
        return True, proc.stdout, proc.stderr
    except subprocess.TimeoutExpired:
        return False, "", f"[codex timed out at {timeout_sec}s]"
    except FileNotFoundError:
        return False, "", "[codex CLI not on PATH; install or `codex login`]"


# Files that the audit pipeline regenerates and that should be committed
# alongside any verdict-write to keep main internally consistent.
# Pipeline-generated caches that are deliberately UNTRACKED (gitignored)
# since the 2026-07-13 ledger sharding: they are materialized locally by
# run_pipeline.sh / ledger_io.py and must never be staged or demanded as
# committed surfaces. The sharded ledger under docs/audit/data/ledger/ is
# the tracked source of truth and is covered by the docs/audit/data prefix.
GENERATED_UNTRACKED_FILES = [
    "docs/audit/AUDIT_LEDGER.md",
    "docs/audit/data/audit_ledger.json",
    "docs/audit/data/ledger_cache_manifest.json",
    "docs/audit/data/citation_graph.json",
    "docs/audit/data/audit_queue.json",
    "docs/audit/data/runner_classification.json",
]

AUDIT_DATA_FILES = [
    "docs/audit/AUDIT_DISPATCH_QUEUE.md",
    "docs/audit/AUDIT_QUEUE.md",
    "docs/audit/data",
    "docs/publication/ci3_z3/CLAIMS_TABLE_EFFECTIVE_STATUS.md",
    "docs/publication/ci3_z3/DERIVATION_ATLAS_EFFECTIVE_STATUS.md",
    "docs/publication/ci3_z3/PUBLICATION_MATRIX_EFFECTIVE_STATUS.md",
    "docs/publication/ci3_z3/FULL_CLAIM_LEDGER_EFFECTIVE_STATUS.md",
    "docs/publication/ci3_z3/USABLE_DERIVED_VALUES_INDEX_EFFECTIVE_STATUS.md",
    "docs/publication/ci3_z3/RESULTS_INDEX_EFFECTIVE_STATUS.md",
    "docs/publication/ci3_z3/QUANTITATIVE_SUMMARY_TABLE_EFFECTIVE_STATUS.md",
    "docs/publication/ci3_z3/DERIVATION_VALIDATION_MAP_EFFECTIVE_STATUS.md",
    "docs/publication/ci3_z3/PUBLICATION_AUDIT_DIVERGENCE.md",
    "docs/publication/ci3_z3/ARXIV_DRAFT_EFFECTIVE_STATUS.md",
    "docs/repo/FRONT_DOOR_STATUS.md",
    "docs/repo/RETAINED_BACKBONE.md",
]


def git(*args: str, check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", *args],
        cwd=REPO_ROOT, capture_output=True, text=True, check=check,
    )


def assert_main_and_clean() -> str | None:
    """Return None if we're on main with a clean tree; else a reason string."""
    branch = git("rev-parse", "--abbrev-ref", "HEAD").stdout.strip()
    if branch != "main":
        return f"not on main (currently on {branch!r})"
    # Allow audit-data files to be dirty (we'll commit them); fail on
    # other dirty paths.
    porcelain = git("status", "--porcelain").stdout
    other_dirty = []
    for line in porcelain.splitlines():
        path = line[3:]
        if not any(path == f or path.startswith(f + "/") or path.startswith(f) for f in AUDIT_DATA_FILES):
            other_dirty.append(path)
    if other_dirty:
        return f"working tree dirty outside audit-data files: {other_dirty[:5]}"
    return None


def commit_and_push_to_main(message: str, max_attempts: int = 3) -> tuple[bool, str]:
    """Stage audit-data files, commit, push to main with rebase-on-conflict retry."""
    # Stage every audit-data path that exists
    paths = [p for p in AUDIT_DATA_FILES if (REPO_ROOT / p).exists()]
    add = git("add", *paths, check=False)
    if add.returncode != 0:
        return False, f"git add failed: {add.stderr.strip()[:200]}"
    diff = git("diff", "--cached", "--quiet", check=False)
    if diff.returncode == 0:
        return True, "no audit-data changes to commit"
    commit = git("commit", "-m", message, check=False)
    if commit.returncode != 0:
        return False, f"git commit failed: {(commit.stderr or commit.stdout).strip()[:200]}"
    for attempt in range(1, max_attempts + 1):
        push = git("push", "origin", "main", check=False)
        if push.returncode == 0:
            return True, f"pushed (attempt {attempt})"
        # Try fetch + rebase
        git("fetch", "origin", "main", check=False)
        rebase = git("rebase", "origin/main", check=False)
        if rebase.returncode != 0:
            git("rebase", "--abort", check=False)
            return False, f"push attempt {attempt} failed and rebase conflicted: {(push.stderr or push.stdout).strip()[:200]}"
    return False, f"push failed after {max_attempts} attempts"


CODEX_RESPONSE_RE = re.compile(
    r"(?:^|\n)codex\n(.*?)(?:\ntokens used\b|\Z)", re.DOTALL
)


def extract_response(stdout: str) -> str | None:
    """Pull the model's actual reply out of `codex exec` stdout.

    Output format:
      <metadata block>
      --------
      user
      <prompt>
      codex
      <reply>
      tokens used
      <count>

    Falls back to returning the whole stdout so JSON-extract can still try.
    """
    m = CODEX_RESPONSE_RE.search(stdout)
    if m:
        return m.group(1).strip()
    # Fallback: return the whole stdout; parse_verdict_json will regex-find
    # the JSON object inside.
    return stdout if stdout.strip() else None


def parse_verdict_json(reply: str) -> dict | None:
    """Best-effort extract a JSON object from the codex reply.

    Codex output may include a leading metadata block, the prompt echo, a
    "codex" header, the actual reply, and a "tokens used" trailer. The
    audit verdict is always the LAST JSON object in the reply, so we
    search backward from the last `}` and try progressively earlier `{`
    starts until something parses.
    """
    reply = reply.strip()
    # Drop any tokens-used trailer
    if "\ntokens used" in reply:
        reply = reply.split("\ntokens used", 1)[0].rstrip()
    # Try direct parse first
    try:
        parsed = json.loads(reply)
        return parsed if isinstance(parsed, dict) else None
    except json.JSONDecodeError:
        pass
    # Strip markdown fences if present
    if reply.startswith("```"):
        stripped = reply.strip("`").lstrip("json").strip()
        try:
            parsed = json.loads(stripped)
            return parsed if isinstance(parsed, dict) else None
        except json.JSONDecodeError:
            pass

    # Find the last `}` in the reply and try every `{` start before it
    last_close = reply.rfind("}")
    if last_close == -1:
        return None
    cursor = 0
    while True:
        first_open = reply.find("{", cursor)
        if first_open == -1 or first_open > last_close:
            return None
        candidate = reply[first_open : last_close + 1]
        try:
            parsed = json.loads(candidate)
            if isinstance(parsed, dict):
                return parsed
            cursor = first_open + 1
        except json.JSONDecodeError:
            cursor = first_open + 1


def validate_verdict(
    blob: dict,
    expected_cid: str,
    *,
    source_requires_no_go: bool = False,
    evidence_manifest: dict[str, dict] | None = None,
    prior_claim_scope: str | None = None,
    expected_invocation_id: str | None = None,
    transport_bounded_n8: bool = False,
) -> str | None:
    """Return an error string if the verdict is unusable, else None."""
    if not isinstance(blob, dict):
        return "verdict must be a JSON object"
    missing = REQUIRED_VERDICT_FIELDS - set(blob)
    if missing:
        return f"missing fields: {sorted(missing)}"
    if blob.get("claim_id") != expected_cid:
        return f"claim_id mismatch: expected {expected_cid!r}, got {blob.get('claim_id')!r}"
    invocation_error = audit_invocation.validation_error(
        blob.get("audit_invocation_id"), required=expected_invocation_id is not None
    )
    if invocation_error:
        return invocation_error
    if expected_invocation_id is not None and blob.get("audit_invocation_id") != expected_invocation_id:
        return "audit_invocation_id is absent or does not match the prompt-bound invocation"
    forensic_tier = bool(
        source_requires_no_go
        or blob.get("claim_type") == "no_go"
        or no_go_discipline_gate.forensic_mode()
    )
    transport_bound_is_dispositive = bool(
        forensic_tier or blob.get("negative_assertion_classes")
    )
    if transport_bounded_n8 and transport_bound_is_dispositive:
        packet = blob.get("no_go_discipline")
        n8 = packet.get("N8_cross_cycle_echo") if isinstance(packet, dict) else None
        if blob.get("verdict") == "audited_clean":
            return "transport-bounded N8 evidence forbids audited_clean"
        if not isinstance(packet, dict) or packet.get("status") != "FAIL":
            return "transport-bounded N8 evidence requires no_go_discipline.status=FAIL"
        if not isinstance(n8, dict) or n8.get("packet_complete") is not False:
            return "transport-bounded N8 evidence requires packet_complete=false"
        unresolved = n8.get("unresolved") if isinstance(n8, dict) else None
        if not isinstance(unresolved, list) or not unresolved:
            return "transport-bounded N8 evidence requires a nonempty unresolved list"
    if (
        blob.get("verdict") == "audited_clean"
        and evidence_manifest is not None
    ):
        clipped_paths = sorted(
            path
            for path, entry in evidence_manifest.items()
            if any(
                marker in str(entry.get("text") or "")
                for marker in CLIPPED_EVIDENCE_MARKERS
            )
            and set(entry.get("roles") or []) & LOAD_BEARING_EVIDENCE_ROLES
        )
        if clipped_paths:
            return (
                "audited_clean requires complete load-bearing packet surfaces; "
                f"clipped evidence: {clipped_paths}"
            )
    no_go_error = no_go_discipline_gate.validate_no_go_discipline(
        blob,
        source_required=source_requires_no_go,
        evidence_manifest=evidence_manifest if forensic_tier else None,
        prior_claim_scope=prior_claim_scope,
        structural_only=not forensic_tier,
        require_declaration=True,
    )
    if no_go_error:
        return no_go_error
    return None


AUTHENTICATED_OCCURRENCE_FIELDS = (
    "occurrence_group_id",
    "occurrence_count",
    "occurrence_locator_sha256",
)


def bind_authenticated_casefold_evidence_paths(
    blob: dict,
    evidence_manifest: dict[str, dict] | None,
) -> list[dict[str, object]]:
    """Canonicalize N1-N8 evidence-path casing drift after a unique match.

    Evidence paths are orchestrator-owned packet metadata. The auditor owns all
    cited content and scientific judgment. Restrict traversal to
    ``no_go_discipline`` and replace an out-of-manifest ``evidence_path`` when
    its casefold matches exactly one authenticated manifest path. Exact,
    unrelated, ambiguous, and non-string paths remain untouched and fail
    closed in the validator.
    """
    if evidence_manifest is None:
        return []
    packet = blob.get("no_go_discipline")
    if not isinstance(packet, dict):
        return []
    paths_by_casefold: dict[str, list[str]] = {}
    for path in evidence_manifest:
        if isinstance(path, str) and path:
            paths_by_casefold.setdefault(path.casefold(), []).append(path)
    changes: list[dict[str, object]] = []

    def visit(value: object, location: str) -> None:
        if isinstance(value, dict):
            current = value.get("evidence_path")
            if (
                isinstance(current, str)
                and current
                and current not in evidence_manifest
            ):
                matches = paths_by_casefold.get(current.casefold(), [])
                if len(matches) == 1:
                    canonical = matches[0]
                    changes.append({
                        "location": location,
                        "field": "evidence_path",
                        "from": current,
                        "to": canonical,
                    })
                    value["evidence_path"] = canonical
            for key, item in value.items():
                if key != "evidence_path":
                    visit(item, f"{location}.{key}")
        elif isinstance(value, list):
            for index, item in enumerate(value, 1):
                visit(item, f"{location}[{index}]")

    visit(packet, "no_go_discipline")
    return changes


def bind_authenticated_n8_universe_metadata(
    blob: dict,
    evidence_manifest: dict[str, dict] | None,
) -> list[dict[str, object]]:
    """Bind orchestrator-owned N8 no-go-universe count and digest."""
    if not isinstance(evidence_manifest, dict):
        return []
    packet = blob.get("no_go_discipline")
    if not isinstance(packet, dict):
        return []
    section = packet.get("N8_cross_cycle_echo")
    if not isinstance(section, dict):
        return []
    path = section.get("evidence_path")
    if not isinstance(path, str) or not path:
        return []
    entry = evidence_manifest.get(path)
    if not isinstance(entry, dict):
        return []
    roles = entry.get("roles")
    # Fail closed on malformed role metadata: only a list of strings can
    # authenticate the cross-cycle index role. `in` on the checked list never
    # raises on unhashable members, and non-list shapes (int, str, mapping)
    # are refused outright instead of aborting the runner with TypeError.
    if not isinstance(roles, list) or "cross_cycle_index" not in [
        role for role in roles if isinstance(role, str)
    ]:
        return []
    universe = no_go_discipline_gate._cross_cycle_no_go_universe(entry)
    if universe is None:
        return []
    count, digest = universe
    changes: list[dict[str, object]] = []
    for field, authenticated in (
        ("no_go_row_universe_count", count),
        ("no_go_row_universe_sha256", digest),
    ):
        current = section.get(field)
        if current == authenticated:
            continue
        changes.append({
            "location": "no_go_discipline.N8_cross_cycle_echo",
            "field": field,
            "from": current,
            "to": authenticated,
        })
        section[field] = authenticated
    return changes


def bind_authenticated_occurrence_metadata(
    blob: dict,
    evidence_manifest: dict[str, dict] | None,
) -> list[dict[str, object]]:
    """Bind orchestrator-owned N3/N5 occurrence metadata after a unique match.

    The auditor owns classification, rationale, tested resolutions, walls, and
    verdict content. The orchestrator owns the occurrence IDs/counts/digests.
    Bind those three metadata fields only when the auditor's exact
    (evidence_path, phrase, evidence_locator) selects one authenticated
    full_phrase_groups record. Zero or multiple matches remain untouched and
    fail closed in the ordinary validator.
    """
    if evidence_manifest is None:
        return []
    packet = blob.get("no_go_discipline")
    if not isinstance(packet, dict):
        return []
    changes: list[dict[str, object]] = []
    for section_name, collection_name in (
        ("N3_hidden_wall_scan", "hits"),
        ("N5_rhetoric_audit", "statements"),
    ):
        section = packet.get(section_name)
        if not isinstance(section, dict):
            continue
        items = section.get(collection_name)
        if not isinstance(items, list):
            continue
        for index, item in enumerate(items, 1):
            if not isinstance(item, dict):
                continue
            path = item.get("evidence_path")
            phrase = item.get("phrase")
            locator = item.get("evidence_locator")
            if not all(isinstance(value, str) and value for value in (path, phrase, locator)):
                continue
            entry = evidence_manifest.get(path)
            if not isinstance(entry, dict):
                continue
            matches = [
                group
                for group in entry.get("full_phrase_groups") or []
                if isinstance(group, dict)
                and group.get("phrase") == phrase
                and group.get("evidence_locator") == locator
            ]
            if len(matches) != 1:
                continue
            group = matches[0]
            for field in AUTHENTICATED_OCCURRENCE_FIELDS:
                expected = group.get(field)
                if expected is None or item.get(field) == expected:
                    continue
                changes.append({
                    "section": section_name,
                    "index": index,
                    "field": field,
                    "from": item.get(field),
                    "to": expected,
                })
                item[field] = expected
    return changes


def bind_authenticated_n6_candidate_locators(
    blob: dict,
    evidence_manifest: dict[str, dict] | None,
) -> list[dict[str, object]]:
    """Bind an invalid N6 locator to its unique authenticated candidate id.

    The auditor owns candidate selection, indexed basis, wall mapping,
    mechanism, disposition, and verdict content. The orchestrator owns the
    serialized partial-closure index. When an N6 object already names one
    exact candidate id from that index but supplies a locator that is absent
    from the serialized text (commonly because quoted basis text is JSON
    escaped), replace only ``evidence_locator`` with the unique candidate id.
    Ambiguous, missing, cross-index, or already valid locators remain untouched
    and fail closed in the ordinary validator.
    """
    if evidence_manifest is None:
        return []
    packet = blob.get("no_go_discipline")
    n6 = packet.get("N6_partial_closure_scan") if isinstance(packet, dict) else None
    candidates = n6.get("candidates") if isinstance(n6, dict) else None
    if not isinstance(candidates, list):
        return []
    changes: list[dict[str, object]] = []
    for index, candidate in enumerate(candidates, 1):
        if not isinstance(candidate, dict):
            continue
        path = candidate.get("evidence_path")
        candidate_id = candidate.get("candidate_id")
        locator = candidate.get("evidence_locator")
        if not all(
            isinstance(value, str) and value
            for value in (path, candidate_id, locator)
        ):
            continue
        entry = evidence_manifest.get(path)
        if not isinstance(entry, dict):
            continue
        if "partial_closure_index" not in set(entry.get("roles") or []):
            continue
        text = str(entry.get("text") or "")
        if locator in text:
            continue
        try:
            payload = json.loads(text)
        except json.JSONDecodeError:
            continue
        if not isinstance(payload, dict):
            continue
        indexed = payload.get("candidates")
        if not isinstance(indexed, list):
            continue
        matches = [
            item
            for item in indexed
            if isinstance(item, dict) and item.get("candidate_id") == candidate_id
        ]
        if len(matches) != 1 or candidate_id not in text:
            continue
        changes.append({
            "section": "N6_partial_closure_scan",
            "index": index,
            "field": "evidence_locator",
            "from": locator,
            "to": candidate_id,
        })
        candidate["evidence_locator"] = candidate_id
    return changes


def compute_required_reason(reply: str | None) -> str | None:
    """Accept only the exact one-line COMPUTE_REQUIRED escape protocol."""
    if not reply:
        return None
    match = re.fullmatch(
        r"COMPUTE_REQUIRED:\s*([^\r\n]+)",
        reply.strip(),
        re.IGNORECASE,
    )
    return match.group(1).strip()[:300] if match else None


def render_validation_repair_prompt(
    original_prompt: str,
    verdict_blob: dict,
    validation_error: str,
    attempt: int,
) -> str:
    """Ask the same restricted-packet auditor to correct invalid JSON.

    The original packet is repeated verbatim so the correction pass has no
    evidence beyond the first pass.  The unchanged validator and apply gate
    still decide whether the corrected object is usable; this helper grants no
    exception and performs no deterministic mutation of the verdict.
    """
    prior_json = json.dumps(verdict_blob, indent=2, sort_keys=True)
    return (
        f"{original_prompt}\n\n"
        "---\n"
        f"VALIDATOR-GUIDED CORRECTION PASS {attempt} (binding):\n"
        "Your preceding JSON object was rejected before apply. Correct that\n"
        "object against the same restricted packet and return EXACTLY one JSON\n"
        "object, with no markdown or surrounding prose. The ordinary validator\n"
        "and apply gate remain unchanged. Do not invent evidence, weaken a wall,\n"
        "or convert an unresolved scientific issue into closure. Preserve the\n"
        "scientific judgment, the complete top-level key set, and every\n"
        "top-level value except no_go_discipline exactly. Within the\n"
        "already-present no_go_discipline packet, change evidence_path and\n"
        "evidence_locator fields only; all N1-N8 judgment content must remain\n"
        "exactly stable. This pass may not add a top-level field or change the\n"
        "verdict itself. The rejected JSON is an untrusted correction target,\n"
        "not evidence.\n"
        "Every evidence_locator must be a 12+ character verbatim substring of\n"
        "the content at its evidence_path in the restricted packet; copy it\n"
        "exactly. Do not revise any classification or internal N1-N8\n"
        "reference.\n\n"
        f"VALIDATION ERROR:\n{validation_error}\n\n"
        f"REJECTED JSON TO CORRECT:\n{prior_json}\n"
    )


def fresh_schema_retry_eligible(validation_error: str | None) -> bool:
    """Allow a new isolated audit for structured N1-N8 disposition rejects."""
    if not validation_error:
        return False
    return bool(re.match(
        r"^(?:N[1-8]\b|No-Go Discipline\b|no_go_discipline\b|transport-bounded N8\b)",
        validation_error,
    ))


def fresh_schema_retry_code(validation_error: str) -> str:
    """Reduce validator text to a conclusion-free control-plane code."""
    if (
        validation_error.startswith("N3 hit ")
        and "occurrence_" in validation_error
    ) or validation_error.startswith(
        "N3.hits must exactly disposition orchestrator phrase scan"
    ):
        return "N3_AUTHENTICATED_GROUP_TUPLE_MISMATCH"
    if (
        validation_error.startswith("N5 statement ")
        and "occurrence_" in validation_error
    ) or validation_error.startswith(
        "N5.statements must exactly disposition orchestrator rhetoric scan"
    ):
        return "N5_AUTHENTICATED_GROUP_TUPLE_MISMATCH"
    if validation_error.startswith("N3 retained_authority hit "):
        return "N3_RETAINED_AUTHORITY_PROVENANCE_MISMATCH"
    if validation_error in {
        "N7.argument is not evidenced at its N1 execution path",
        "N7.resolution is not evidenced at resolution_evidence_path",
        "N7.argument must name the steelmanned route mechanism",
        "N7.argument must name the steelmanned route attempt",
    }:
        return "N7_EXECUTION_EVIDENCE_VERBATIM_MISMATCH"
    if validation_error.startswith("transport-bounded N8"):
        return "N8_TRANSPORT_BOUND_DISPOSITION_MISMATCH"
    if (
        validation_error.startswith("N5 statement ")
        and "tested resolution is not evidenced at resolution_evidence_path"
        in validation_error
    ):
        return "N5_TESTED_RESOLUTION_VERBATIM_MISMATCH"
    if (
        validation_error.startswith("N1 route ")
        and ".route_class=" in validation_error
        and "is not supported by its evidenced" in validation_error
    ):
        return "N1_ROUTE_CLASS_MARKER_MISMATCH"
    if validation_error.startswith("N4 witness "):
        return "N4_WITNESS_SCHEMA_MISMATCH"
    if validation_error.startswith("N5 contains unknown fields") and any(
        field in validation_error
        for field in (
            "resolution_classes_checked",
            "tested_resolutions",
            "untested_resolutions",
            "resolution_evidence_path",
            "resolution_evidence_locator",
        )
    ):
        return "N5_STATEMENT_FIELD_NESTING_MISMATCH"
    if (
        validation_error.startswith("N6 candidate ")
        and ".closure_mechanism must use its indexed_basis" in validation_error
    ):
        return "N6_INDEXED_BASIS_VERBATIM_MISMATCH"
    if (
        validation_error.startswith("N6 candidate ")
        and ".disposition must name its affected_wall" in validation_error
    ):
        return "N6_AFFECTED_WALL_VERBATIM_MISMATCH"
    return "AUDIT_SCHEMA_REJECT"


def fresh_schema_retry_error(
    current_error: str | None,
    initial_validation_error: str | None,
) -> str | None:
    """Keep a structured reject eligible after a failed locator repair.

    Locator repair cannot change N1-N8 judgment content. A repair that
    violates that rule, fails parsing, or fails operationally must not erase
    the original structured validator reject and suppress the independent
    fresh-schema retry.
    """
    if current_error is None:
        return None
    if fresh_schema_retry_eligible(current_error):
        return current_error
    if fresh_schema_retry_eligible(initial_validation_error):
        return initial_validation_error
    return current_error


def render_fresh_schema_retry_prompt(
    original_prompt: str,
    validation_code: str,
    attempt: int,
) -> str:
    """Request a fresh judgment without exposing the rejected JSON.

    Unlike locator repair, this starts a distinct isolated Codex context and
    discards the prior object completely. The generic validator code reveals
    no failed section, scientific framing, or prior conclusion.
    """
    guidance = {
        "N3_RETAINED_AUTHORITY_PROVENANCE_MISMATCH": (
            "Static N3 invariant: retained_authority describes path provenance, "
            "not phrase semantics. Use it exactly when the hit path has an "
            "authority/framework_premise/premise_registry role and retained-grade "
            "status or accepted axiom/approved-primitive type. A source-role path "
            "must instead be classified from its actual load-bearing use.\n"
        ),
        "N1_ROUTE_CLASS_MARKER_MISMATCH": (
            "Static N1 invariant: the joined mechanism, attempt, and outcome must "
            "contain a documented literal marker for the selected route_class. "
            "At least one of those fields must itself copy the marker. When a "
            "check label lacks it, use an evidenced marker-bearing live section "
            "header that genuinely names the same route; do not duplicate fields "
            "unless stdout supplies the same text for distinct semantic roles.\n"
        ),
        "N3_AUTHENTICATED_GROUP_TUPLE_MISMATCH": (
            "Static N3 invariant: copy phrase, occurrence_group_id, "
            "occurrence_count, occurrence_locator_sha256, and evidence_locator "
            "from one same full_phrase_groups record. Separate authenticated "
            "phrase records may share a context-derived id or digest; reproduce "
            "that sharing only when each complete phrase record is listed. Never "
            "infer an unlisted phrase from a shared id or cross-label a count, "
            "digest, or locator from another record.\n"
        ),
        "N5_AUTHENTICATED_GROUP_TUPLE_MISMATCH": (
            "Static N5 invariant: copy phrase, occurrence_group_id, "
            "occurrence_count, occurrence_locator_sha256, and evidence_locator "
            "from one same full_phrase_groups record. Never cross-label a group "
            "id, count, digest, or locator under another phrase.\n"
        ),
        "N5_TESTED_RESOLUTION_VERBATIM_MISMATCH": (
            "Static N5 invariant: copy every complete tested_resolutions entry, "
            "including its canonical class prefix and body, byte-for-byte as a "
            "contiguous line from the cited live current-cycle runner_stdout. "
            "Do not summarize, shorten, or paraphrase those five lines.\n"
        ),
        "N7_EXECUTION_EVIDENCE_VERBATIM_MISMATCH": (
            "Static N7 invariant: copy argument byte-for-byte as one complete "
            "contiguous live-execution line from the selected N1 route surface; "
            "that line must contain the route mechanism and attempt verbatim. "
            "Copy resolution byte-for-byte as one complete contiguous line from "
            "the cited independent execution or retained/accepted authority, "
            "and choose a line that names an evidenced N2 wall. Do not paraphrase "
            "either field.\n"
        ),
        "N4_WITNESS_SCHEMA_MISMATCH": (
            "Static N4 invariant: when no N1 route is RULED OUT BY PRIOR, emit "
            "witnesses as an empty list with a substantive none_found_reason; "
            "never fabricate a placeholder witness. Otherwise every witness "
            "must include witness_residual_id and claim_residual_id as stable "
            "residual:<id> strings, plus separate authority evidence_path and "
            "evidence_locator fields and separate source claim_evidence_path and "
            "claim_evidence_locator fields. The witness surface must have the "
            "authority role and the claim surface must have the source role. Copy "
            "each residual text and ID verbatim from its own cited packet surface.\n"
        ),
        "N5_STATEMENT_FIELD_NESTING_MISMATCH": (
            "Static N5 invariant: resolution_classes_checked, "
            "tested_resolutions, untested_resolutions, resolution_evidence_path, "
            "and resolution_evidence_locator belong inside each statements[] "
            "object, never on the N5_rhetoric_audit section object. Preserve all "
            "statement content while placing each field at that documented level.\n"
        ),
        "N6_INDEXED_BASIS_VERBATIM_MISMATCH": (
            "Static N6 invariant: copy indexed_basis exactly from the candidate "
            "record and include that complete text verbatim inside the same "
            "candidate's closure_mechanism before the explanation of how it could "
            "affect the named wall. Do not paraphrase or shorten indexed_basis.\n"
        ),
        "N6_AFFECTED_WALL_VERBATIM_MISMATCH": (
            "Static N6 invariant: copy affected_wall exactly from the same "
            "candidate and include that complete text verbatim inside its "
            "disposition before explaining why the candidate does or does not "
            "close the wall. Do not paraphrase or shorten affected_wall.\n"
        ),
    }.get(validation_code, "")
    return (
        f"{original_prompt}\n\n"
        "---\n"
        f"FRESH SCHEMA RETRY {attempt} (binding):\n"
        "A separate restricted-context attempt was rejected before apply by "
        "the unchanged deterministic audit schema validator. You are not given its "
        "JSON or conclusion. Reperform the scientific audit from the supplied "
        "evidence and return a wholly fresh JSON object. The validator error "
        "below is a sanitized control-plane schema code only, not scientific evidence. "
        "Do not infer or preserve any prior verdict. Recheck the complete "
        "output schema and every invariant already stated in the original "
        "restricted packet before responding.\n\n"
        f"VALIDATOR CODE:\n{validation_code}\n"
        f"{guidance}"
    )


def validation_repair_preservation_error(
    rejected_blob: dict,
    repaired_blob: dict,
) -> str | None:
    """Reject a format correction that changes the scientific judgment."""
    rejected_fields = set(rejected_blob)
    repaired_fields = set(repaired_blob)
    if repaired_fields != rejected_fields:
        added = sorted(repaired_fields - rejected_fields)
        removed = sorted(rejected_fields - repaired_fields)
        return (
            "validation repair changed the top-level field set "
            f"(added={added}, removed={removed})"
        )
    for field in sorted(rejected_fields - {VALIDATION_REPAIR_MUTABLE_FIELD}):
        if repaired_blob.get(field) != rejected_blob.get(field):
            return (
                "validation repair changed preserved scientific field "
                f"{field!r}"
            )
    def without_locator_fields(value: object) -> object:
        if isinstance(value, dict):
            return {
                key: without_locator_fields(item)
                for key, item in value.items()
                if key not in (
                    VALIDATION_REPAIR_LOCATOR_FIELDS
                    | set(AUTHENTICATED_OCCURRENCE_FIELDS)
                )
            }
        if isinstance(value, list):
            return [without_locator_fields(item) for item in value]
        return value

    rejected_packet = without_locator_fields(
        rejected_blob.get(VALIDATION_REPAIR_MUTABLE_FIELD)
    )
    repaired_packet = without_locator_fields(
        repaired_blob.get(VALIDATION_REPAIR_MUTABLE_FIELD)
    )
    if repaired_packet != rejected_packet:
        return "validation repair changed preserved no-go judgment content"
    return None


def validation_repair_eligible(
    rejected_blob: dict,
    expected_cid: str,
    validation_error: str | None,
) -> bool:
    """True only for a complete verdict with an N1-N8 locator failure."""
    if not validation_error:
        return False
    locator_error = validation_error.casefold()
    if not any(
        marker in locator_error
        for marker in ("evidence_path", "evidence path", "evidence_locator")
    ):
        return False
    return (
        REQUIRED_VERDICT_FIELDS.issubset(rejected_blob)
        and rejected_blob.get("claim_id") == expected_cid
        and isinstance(rejected_blob.get(VALIDATION_REPAIR_MUTABLE_FIELD), dict)
    )


def apply_one(
    verdict_blob: dict,
    propagate: bool,
    evidence_manifest: dict[str, dict] | None = None,
) -> tuple[bool, str]:
    """Pipe a verdict blob through apply_audit.py via stdin."""
    verdict_blob = dict(verdict_blob)
    invocation_id = verdict_blob.get("audit_invocation_id")
    invocation_error = audit_invocation.validation_error(invocation_id, required=True)
    if invocation_error:
        return False, invocation_error
    verdict_blob["audit_invocation_id"] = invocation_id
    cmd = [sys.executable, str(APPLY_AUDIT_SCRIPT)]
    if not propagate:
        cmd.append("--no-propagate")
    with tempfile.TemporaryDirectory(prefix="codex-audit-evidence-") as tmp:
        env = dict(os.environ)
        if evidence_manifest is not None:
            manifest_path = Path(tmp) / "manifest.json"
            manifest_path.write_text(json.dumps({
                "schema": "codex_audit_trusted_manifest_v1",
                "claim_id": verdict_blob.get("claim_id"),
                "audit_invocation_id": invocation_id,
                "issued_at": datetime.now(timezone.utc).isoformat(),
                "entries": evidence_manifest,
            }, sort_keys=True), encoding="utf-8")
            env["CODEX_AUDIT_TRUSTED_EVIDENCE_MANIFEST"] = str(manifest_path)
        proc = subprocess.run(
            cmd,
            input=json.dumps(verdict_blob),
            text=True,
            capture_output=True,
            cwd=REPO_ROOT,
            env=env,
        )
    output = (proc.stdout + proc.stderr).strip()
    if proc.returncode == 4:
        return False, (
            "AUDIT_APPLIED_PROPAGATION_FAILED: the ledger transition is "
            "already committed; do not reapply this verdict. Repair/rerun "
            f"propagation only.\n{output}"
        )
    return proc.returncode == 0, output


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--n", type=int, default=5,
                   help="How many top-of-queue rows to audit this run (default 5).")
    p.add_argument("--claim-id", action="append", default=[],
                   help="Audit this exact claim id from the selected queue. "
                        "Repeat to preserve an explicit audit order; when set, "
                        "--n is ignored. Use --allow-blocked only when the "
                        "named row is intentionally dependency-blocked.")
    p.add_argument("--criticality",
                   choices=["critical", "high", "medium", "leaf"],
                   help="Restrict to one criticality tier.")
    p.add_argument("--dry-run", action="store_true",
                   help="Build prompts but do NOT call codex or apply_audit.")
    p.add_argument("--auditor-name", default=None,
                   help="Auditor identity recorded in the ledger. Default: "
                        "codex-cli-<model>-<utc-yyyymmdd-hhmm>-<run-id>")
    p.add_argument("--codex-timeout-sec", type=int, default=600,
                   help="Per-row codex exec timeout (default 600).")
    p.add_argument("--validation-repair-attempts", type=int, default=1,
                   help="After a complete parsed verdict fails strict N1-N8 "
                        "evidence-locator validation, ask "
                        "the same restricted-packet auditor for this many "
                        "validator-guided JSON corrections (default 1; 0 "
                        "disables). Every correction must pass the unchanged "
                        "validator and apply gate.")
    p.add_argument("--fresh-schema-retry-attempts", type=int, default=2,
                   help="After a complete verdict fails an N1-N8 structural "
                        "schema rule that is not eligible for locator-only "
                        "repair, rerun the full restricted audit in this many "
                        "new isolated contexts (default 2; 0 disables). The "
                        "rejected JSON/conclusion is never passed forward.")
    p.add_argument("--runner-timeout-sec", type=int, default=120,
                   help="Per-row primary-runner timeout (default 120).")
    p.add_argument("--no-propagate", action="store_true",
                   help="Pass --no-propagate to apply_audit; run the pipeline once at end.")
    p.add_argument("--no-runner", action="store_true",
                   help="Skip running each row's primary runner (faster; uses empty stdout).")
    p.add_argument("--no-cache-runner", action="store_true",
                   help="Don't use logs/<runner-name>*.txt cache; always re-run "
                        "the runner. Slower but freshest output.")
    p.add_argument("--push-mode",
                   choices=["per-verdict", "batch", "none"],
                   default="batch",
                   help="When to commit and push audit-data to main: "
                        "'per-verdict' (commit+push after each apply), "
                        "'batch' (one commit covering the whole run; default), "
                        "'none' (no auto-commit; for testing).")
    p.add_argument("--allow-non-main", action="store_true",
                   help="Permit running from a branch other than main. "
                        "Default refuses unless the runner can push to main "
                        "directly. Use only for testing.")
    p.add_argument("--allow-blocked", action="store_true",
                   help="Audit rows whose deps are not retained-grade. "
                        "Default skips them: auditing a blocked row "
                        "deterministically yields audited_conditional and "
                        "burns a Codex call without compounding progress. "
                        "Pass this when you specifically need to populate "
                        "verdicts in a deeply chained subtree.")
    p.add_argument("--require-runner-output", dest="require_runner_output",
                   action="store_true", default=True,
                   help="Refuse to audit rows whose primary runner has no "
                        "logged stdout in logs/ (per the audit policy that "
                        "runner stdout is part of the load-bearing evidence). "
                        "On by default; pass --no-require-runner-output to "
                        "fall back to running the runner inline.")
    p.add_argument("--no-require-runner-output", dest="require_runner_output",
                   action="store_false",
                   help="Disable the --require-runner-output check; let the "
                        "runner subprocess be invoked inline as fallback.")
    p.add_argument("--from-reaudit-candidates", action="store_true",
                   help="Pull rows from docs/audit/data/reaudit_candidates.json "
                        "instead of audit_queue.json. These are rows whose prior "
                        "audit was non-clean (conditional/renaming/etc.) but "
                        "whose deps have since become retained-grade, OR whose "
                        "cited runner SHA has drifted. Each row gets a fresh "
                        "audit pass that can now potentially close the chain. "
                        "--allow-blocked is ignored for this alternate source; "
                        "the candidate producer owns eligibility.")
    p.add_argument("--from-dispatch", action="store_true",
                   help="Pull live targeted re-audits from "
                        "docs/audit/data/audit_dispatch_queue.json. Only the "
                        "claim id selects the audit. The operator question is "
                        "retained only as log metadata and is never auditor "
                        "context or evidence.")
    p.add_argument("--allow-weak-dispatch", action="store_true",
                   help="Permit a dispatch whose author provenance is unknown. "
                        "Such a run is demotion-capable only: audited_clean "
                        "cannot be applied under weak independence.")
    p.add_argument("--no-runner-drift-candidates", action="store_true",
                   help="With --from-reaudit-candidates, skip the "
                        "runner_drift_candidates stream (only re-audit on "
                        "dependency-strengthening). Default includes both.")
    p.add_argument("--only-awaiting-cross-confirmation", action="store_true",
                   help="Restrict audit_queue.json selection to rows already "
                        "holding a first clean audit and waiting for an "
                        "independent second audit. This excludes ordinary "
                        "unaudited rows.")
    p.add_argument("--allow-low-model", action="store_true",
                   help="Permit running with an audit model below the "
                        "MIN_AUDIT_MODEL_RANK floor (currently gpt-5.6). "
                        "Break-glass for testing only — verdicts produced "
                        "this way will be tagged with the actual sub-floor "
                        "family and won't satisfy the standard "
                        "independence rule for clean verdicts.")
    args = p.parse_args()

    if not 0 <= args.validation_repair_attempts <= 3:
        print("REFUSING: --validation-repair-attempts must be between 0 and 3.")
        return 2
    if not 0 <= args.fresh_schema_retry_attempts <= 3:
        print("REFUSING: --fresh-schema-retry-attempts must be between 0 and 3.")
        return 2
    if args.from_dispatch and args.from_reaudit_candidates:
        print("REFUSING: choose only one of --from-dispatch and --from-reaudit-candidates.")
        return 2
    if args.allow_weak_dispatch and not args.from_dispatch:
        p.error("--allow-weak-dispatch requires --from-dispatch")
    if args.no_propagate and args.push_mode != "none":
        p.error("--no-propagate is allowed only with --push-mode none")

    # Reasoning-effort policy: per repo audit-lane decision (2026-05-04),
    # ALL audits run at xhigh. We do not expose a knob to lower it.
    reasoning_effort = AUDIT_REASONING_EFFORT
    audit_model, auditor_family, model_source, model_warnings = resolve_audit_model()

    # Defense in depth beneath best-available model selection.
    if not _meets_floor(audit_model) and not args.allow_low_model:
        floor_str = ".".join(str(x) for x in MIN_AUDIT_MODEL_RANK)
        print(
            f"\nREFUSING to run: resolved audit model {audit_model!r} "
            f"is below the MIN_AUDIT_MODEL_RANK floor (gpt-{floor_str}+).\n"
            f"  Source: {model_source}\n"
            f"  Refresh Codex access to a full gpt-{floor_str}+ model at xhigh.\n"
            f"  models_cache.json, or pass --allow-low-model for testing only.\n"
            f"  Existing audits at sub-floor model versions will be re-audited\n"
            f"  on the next batch once this is resolved."
        )
        return 2
    if not _meets_floor(audit_model):
        floor_str = ".".join(str(x) for x in MIN_AUDIT_MODEL_RANK)
        print(
            f"WARNING: --allow-low-model: running below gpt-{floor_str} floor "
            f"(model={audit_model!r}). Verdicts WILL be tagged with this "
            f"family in the ledger and will not satisfy the standard "
            f"cross_family / fresh_context independence rule for clean "
            f"verdicts. Use only for testing."
        )

    LOG_DIR.mkdir(parents=True, exist_ok=True)
    run_uuid = uuid.uuid4().hex
    run_id = run_uuid[:8]
    auditor_name_base = args.auditor_name or (
        f"codex-cli-{audit_model}-"
        f"{datetime.now(timezone.utc).strftime('%Y%m%d-%H%M%S')}-{run_id}"
    )
    run_log = LOG_DIR / f"run-{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}-{run_id}.jsonl"
    print(f"Run log: {run_log}")
    print(f"Auditor (base): {auditor_name_base}  ({auditor_family})")
    print(f"Codex model: {audit_model}  reasoning_effort={reasoning_effort}")
    print(f"Model policy source: {model_source}")
    for warning in model_warnings:
        print(f"MODEL POLICY WARNING: {warning}")
    with run_log.open("a", encoding="utf-8") as f:
        f.write(json.dumps({
            "phase": "model_policy",
            "model": audit_model,
            "auditor_family": auditor_family,
            "reasoning_effort": reasoning_effort,
            "source": model_source,
            "warnings": model_warnings,
        }) + "\n")
    print("Per-row independence is determined from each row's existing cross_confirmation:")
    print("  first-pass with no prior audit                    -> cross_family")
    print("  second-pass after a prior audit by a different family -> cross_family")
    print("  second-pass after a prior audit by Codex            -> fresh_context")
    print("  rows in disagreement / awaiting-judicial-review     -> skipped (manual)")
    if args.from_dispatch:
        print("Source: audit_dispatch_queue.json (live targeted re-audits)")
        print(f"  ready_only={not args.allow_blocked}")
    elif args.from_reaudit_candidates:
        print("Source: reaudit_candidates.json (rows whose chain may now close "
              "after dependency strengthening or runner SHA drift)")
        print(f"  include_runner_drift={not args.no_runner_drift_candidates}")
    else:
        print(f"Source: audit_queue.json")
        print(f"  ready_only={not args.allow_blocked}  "
              f"require_runner_output={args.require_runner_output}")

    # Verify branch + cleanliness before any push-capable operation.
    if args.push_mode != "none" and not args.dry_run:
        reason = assert_main_and_clean()
        if reason and not args.allow_non_main:
            print(f"REFUSING to run with --push-mode={args.push_mode}: {reason}")
            print("Either checkout main and clean the worktree, or pass --allow-non-main "
                  "(local-only; verdicts will be applied but NOT pushed to main).")
            return 2
        if reason and args.allow_non_main:
            print(f"WARNING: {reason}; --allow-non-main forces push-mode=none for safety.")
            args.push_mode = "none"
        else:
            # Pull in any remote audit-bot commits before we start. If the
            # rebase conflicts, abort and bail — silently continuing on a
            # half-rebased worktree would push tangled history to main.
            git("fetch", "origin", "main", check=False)
            rebase = git("rebase", "origin/main", check=False)
            if rebase.returncode != 0:
                git("rebase", "--abort", check=False)
                print("REFUSING to run with --push-mode=" + args.push_mode + ":")
                print("  pre-run `git rebase origin/main` failed with conflicts.")
                print("  Resolve the conflict on main manually, then re-run.")
                print(f"  rebase stderr: {(rebase.stderr or rebase.stdout).strip()[:300]}")
                return 2

    if (
        not args.from_dispatch
        and not args.from_reaudit_candidates
        and not QUEUE_PATH.exists()
    ):
        print("Derived audit caches missing (fresh clone); running the pipeline once.")
        bootstrap = subprocess.run(
            ["bash", str(PIPELINE_SCRIPT)],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            timeout=1800,
            check=False,
        )
        if bootstrap.returncode != 0:
            detail = (bootstrap.stderr or bootstrap.stdout).strip()[-500:]
            print(f"REFUSING: audit pipeline bootstrap failed: {detail}")
            return 2

    run_commit = git("rev-parse", "HEAD", check=False).stdout.strip()
    ledger_rows = load_ledger_rows()
    if args.from_dispatch:
        try:
            queue = load_dispatch_targets(
                ledger_rows,
                args.criticality,
                ready_only=not args.allow_blocked,
                selected_claim_ids=set(args.claim_id) if args.claim_id else None,
                limit=None if args.claim_id else args.n,
            )
        except ValueError as exc:
            print(f"REFUSING dispatch selection: {exc}")
            return 2
    elif args.from_reaudit_candidates:
        queue = load_reaudit_candidates(
            args.criticality,
            include_runner_drift=not args.no_runner_drift_candidates,
        )
    else:
        queue = load_queue(args.criticality, ready_only=not args.allow_blocked)
    if args.only_awaiting_cross_confirmation:
        if args.from_reaudit_candidates or args.from_dispatch:
            print("REFUSING: --only-awaiting-cross-confirmation applies only to audit_queue.json.")
            return 2
        queue = only_awaiting_cross_confirmation(queue, ledger_rows)
    if args.claim_id:
        try:
            targets = select_named_targets(queue, args.claim_id)
        except ValueError as exc:
            print(f"REFUSING targeted selection: {exc}")
            if not args.allow_blocked and not args.from_reaudit_candidates and not args.from_dispatch:
                print("A named row may be dependency-blocked; rerun with "
                      "--allow-blocked only if auditing that blocked state is intended.")
            return 2
    else:
        targets = queue[: args.n]
    if not targets:
        if args.from_dispatch:
            print("No live dispatch targets in this filter. Run the audit pipeline "
                  "to refresh readiness or inspect ready_blocker metadata.")
        elif args.from_reaudit_candidates:
            print("No re-audit candidates in this filter. Either no upstream "
                  "deps have ratified since prior audits, or the candidates "
                  "stream is empty. Run `bash docs/audit/scripts/run_pipeline.sh` "
                  "to recompute, or fall back to the regular audit queue.")
        elif args.allow_blocked:
            print("Queue empty for this filter; nothing to do.")
        else:
            full_queue = load_queue(args.criticality, ready_only=False)
            print(f"No ready rows in this filter (deps must be retained-grade). "
                  f"{len(full_queue)} blocked rows exist; pass --allow-blocked "
                  f"to audit them anyway.")
        return 0

    print(f"Selected {len(targets)} rows from the queue.")
    print(f"Push mode: {args.push_mode}  Reasoning: {reasoning_effort}")
    print(f"Top of selection:")
    for r in targets[:5]:
        print(f"  - {r['claim_id']}  [{r.get('criticality')}, "
              f"score={r.get('score','?')}, audit_status={r.get('audit_status','?')}]")

    template = PROMPT_TEMPLATE_PATH.read_text(encoding="utf-8")

    applied = 0
    failed = 0
    skipped = 0
    push_failed = False
    propagation_failed = False
    for i, row in enumerate(targets, 1):
        cid = row["claim_id"]
        fresh_retry_dirs: list[Path] = []
        print(f"\n[{i}/{len(targets)}] {cid}")
        try:
            # Determine first-pass vs second-pass vs skip BEFORE invoking codex.
            # This avoids burning a codex call on a row apply_audit will reject,
            # and ensures the verdict's independence matches the row's history.
            full_led_row = ledger_rows.get(cid, {})
            role, role_info = determine_audit_role(
                full_led_row,
                auditor_family,
                is_reaudit_candidate=(
                    args.from_reaudit_candidates or args.from_dispatch
                ),
                is_dispatch_target=args.from_dispatch,
            )
            if role == "skip":
                print(f"  SKIP: {role_info}")
                skipped += 1
                with run_log.open("a", encoding="utf-8") as f:
                    f.write(json.dumps({
                        "claim_id": cid, "phase": "skip_role",
                        "reason": role_info,
                    }) + "\n")
                continue
            row_independence = role_info  # cross_family or fresh_context
            if args.from_dispatch:
                question = str(row.get("dispatch_question") or "")
                with run_log.open("a", encoding="utf-8") as f:
                    f.write(json.dumps({
                        "claim_id": cid,
                        "phase": "dispatch_selection",
                        "source_json_path": row.get("source_json_path"),
                        "source_schema": row.get("source_schema"),
                        "dispatch_question_sha256": hashlib.sha256(
                            question.encode("utf-8")
                        ).hexdigest(),
                        "repository_commit": run_commit,
                    }) + "\n")
            if (
                args.from_dispatch
                and row_independence == "weak"
                and not args.allow_weak_dispatch
            ):
                print(
                    "  SKIP: dispatch author provenance is unknown; pass "
                    "--allow-weak-dispatch only for a demotion-capable run"
                )
                skipped += 1
                continue
            # Per-row auditor identity to guarantee uniqueness across passes.
            # Always include this process's run id even when --auditor-name is
            # reused, so fresh-context provenance cannot collide with a live
            # or archived auditor identity.
            row_auditor = row_auditor_identity(
                auditor_name_base, run_uuid, cid, i
            )
            prior_auditor_ids = {
                str(full_led_row.get("author") or ""),
                str(full_led_row.get("auditor") or ""),
                *{
                    str(prior.get("auditor") or "")
                    for prior in full_led_row.get("previous_audits") or []
                    if isinstance(prior, dict)
                },
            }
            prior_auditor_ids.discard("")
            if row_auditor in prior_auditor_ids:
                print("  SKIP: generated auditor identity collides with prior provenance")
                skipped += 1
                continue
            print(f"  role={role}  independence={row_independence}")

            # Refuse rows whose primary runner has no logged stdout. The audit
            # policy treats runner output as part of the load-bearing evidence
            # (see AUDIT_AGENT_PROMPT_TEMPLATE.md sections 3 and 3a). With the
            # runner-logging worker producing logs/<runner>-<utc>.txt files,
            # the cached-log path is the canonical source. If a row's runner
            # has no log, the audit cannot judge load-bearing class without
            # invoking the runner inline — which breaks the "fresh-look in an
            # isolated workdir" model.
            raw_runner_path = row.get("runner_path") or full_led_row.get("runner_path")
            runner_path = canonical_runner_path(raw_runner_path) if raw_runner_path else raw_runner_path
            if (
                args.require_runner_output
                and runner_path
                and not args.no_runner
                and not args.dry_run
            ):
                cached = find_cached_runner_output(runner_path)
                if cached is None:
                    print(f"  SKIP: runner {runner_path} has no logged stdout in logs/; "
                          f"the runner-logging worker must produce one before this row "
                          f"is auditable. (Pass --no-require-runner-output to bypass.)")
                    skipped += 1
                    with run_log.open("a", encoding="utf-8") as f:
                        f.write(json.dumps({
                            "claim_id": cid, "phase": "skip_no_runner_log",
                            "runner_path": runner_path,
                        }) + "\n")
                    continue

            # Cache files remain readiness/performance artifacts, but their
            # identity is source-SHA-only and cannot authenticate mutable data
            # inputs. Authority-bearing audit prompts therefore execute the
            # current primary runner rather than consuming cached stdout.
            use_cache = False
            exact_evidence_manifest: dict[str, dict] = {}
            audit_invocation_id = uuid.uuid4().hex
            if args.no_runner:
                # Skip the runner subprocess + cache, but keep Section 3a
                # (runner source code) so the auditor can still inspect what
                # the runner does. Pass timeout=0 since it is unused.
                prompt = render_prompt(row, ledger_rows, template, 0,
                                       use_cache=False, skip_runner_stdout=True,
                                       evidence_manifest_out=exact_evidence_manifest,
                                       audit_invocation_id=audit_invocation_id)
            else:
                prompt = render_prompt(row, ledger_rows, template, args.runner_timeout_sec,
                                       use_cache=use_cache,
                                       evidence_manifest_out=exact_evidence_manifest,
                                       audit_invocation_id=audit_invocation_id)

            transport_note_path = (
                row.get("note_path") or full_led_row.get("note_path") or ""
            )
            transport_note_body = read_note_body(transport_note_path) or ""
            transport_source_required = (
                no_go_discipline_gate.source_requires_no_go_discipline(
                    transport_note_path,
                    transport_note_body,
                    (
                        ""
                        if args.from_dispatch
                        else row.get("claim_type") or full_led_row.get("claim_type")
                    ),
                )
            )
            transport_forensic = bool(
                transport_source_required
                or (
                    not args.from_dispatch
                    and (row.get("claim_type") or full_led_row.get("claim_type"))
                    == "no_go"
                )
                or no_go_discipline_gate.forensic_mode()
            )
            try:
                prompt, transport_bound = fit_prompt_to_transport_limit(
                    prompt,
                    exact_evidence_manifest,
                    cid,
                    forensic_bound=transport_forensic,
                )
            except ValueError as exc:
                print(f"  SKIP prompt transport: {exc}")
                skipped += 1
                with run_log.open("a", encoding="utf-8") as f:
                    f.write(json.dumps({
                        "claim_id": cid,
                        "phase": "skip_prompt_transport",
                        "reason": str(exc),
                    }) + "\n")
                continue
            if transport_bound:
                transport_disposition = (
                    "clean forbidden"
                    if transport_forensic
                    else "development-tier structural bound; verdict not forced"
                )
                print(
                    "  N8 transport-bound: "
                    f"{transport_bound['rendered_candidates']}/"
                    f"{transport_bound['authenticated_candidates']} candidates, "
                    f"{transport_bound['prompt_chars_before']} -> "
                    f"{transport_bound['prompt_chars_after']} chars; "
                    f"{transport_disposition}"
                )

            if args.dry_run:
                print(f"  [dry-run] prompt size: {len(prompt)} chars")
                with run_log.open("a", encoding="utf-8") as f:
                    f.write(json.dumps({
                        "claim_id": cid, "phase": "dry-run", "prompt_size": len(prompt),
                        "transport_bound": transport_bound,
                    }) + "\n")
                continue

            isolated = ISOLATED_BASE / f"{run_id}-{i:03d}"
            t0 = time.time()
            ok, stdout, stderr = run_codex(
                prompt, isolated, args.codex_timeout_sec,
                reasoning_effort=reasoning_effort,
                model=audit_model,
            )
            elapsed = time.time() - t0

            if not ok:
                print(f"  FAIL codex exec: {stderr.strip()[:300]}")
                with run_log.open("a", encoding="utf-8") as f:
                    f.write(json.dumps({
                        "claim_id": cid, "phase": "codex_failed",
                        "elapsed_sec": elapsed, "stderr": stderr[:500]
                    }) + "\n")
                failed += 1
                continue

            reply = extract_response(stdout)
            if not reply:
                print("  FAIL: could not extract codex reply from stdout")
                failed += 1
                with run_log.open("a", encoding="utf-8") as f:
                    f.write(json.dumps({
                        "claim_id": cid, "phase": "extract_failed",
                        "elapsed_sec": elapsed, "stdout_tail": stdout[-2000:]
                    }) + "\n")
                continue

            # COMPUTE_REQUIRED escape per AUDIT_AGENT_PROMPT_TEMPLATE.md:
            # if codex says the load-bearing step needs a missing run, do
            # NOT apply a verdict. Skip the row and log it for compute-rerun.
            reason = compute_required_reason(reply)
            if reason:
                print(f"  COMPUTE_REQUIRED: {reason[:200]}")
                skipped += 1
                with run_log.open("a", encoding="utf-8") as f:
                    f.write(json.dumps({
                        "claim_id": cid, "phase": "compute_required",
                        "elapsed_sec": elapsed, "reason": reason,
                    }) + "\n")
                continue

            blob = parse_verdict_json(reply)
            if blob is None:
                print(f"  FAIL: codex reply not valid JSON")
                failed += 1
                with run_log.open("a", encoding="utf-8") as f:
                    f.write(json.dumps({
                        "claim_id": cid, "phase": "json_parse_failed",
                        "reply": reply[:2000]
                    }) + "\n")
                continue

            casefold_path_bindings = bind_authenticated_casefold_evidence_paths(
                blob, exact_evidence_manifest
            )
            if casefold_path_bindings:
                with run_log.open("a", encoding="utf-8") as f:
                    f.write(json.dumps({
                        "claim_id": cid,
                        "phase": "authenticated_casefold_evidence_paths_bound",
                        "bindings": casefold_path_bindings,
                    }) + "\n")
            n8_universe_bindings = bind_authenticated_n8_universe_metadata(
                blob, exact_evidence_manifest
            )
            if n8_universe_bindings:
                with run_log.open("a", encoding="utf-8") as f:
                    f.write(json.dumps({
                        "claim_id": cid,
                        "phase": "authenticated_n8_universe_metadata_bound",
                        "bindings": n8_universe_bindings,
                    }) + "\n")
            occurrence_bindings = bind_authenticated_occurrence_metadata(
                blob, exact_evidence_manifest
            )
            if occurrence_bindings:
                with run_log.open("a", encoding="utf-8") as f:
                    f.write(json.dumps({
                        "claim_id": cid,
                        "phase": "authenticated_occurrence_metadata_bound",
                        "bindings": occurrence_bindings,
                    }) + "\n")
            n6_locator_bindings = bind_authenticated_n6_candidate_locators(
                blob, exact_evidence_manifest
            )
            if n6_locator_bindings:
                with run_log.open("a", encoding="utf-8") as f:
                    f.write(json.dumps({
                        "claim_id": cid,
                        "phase": "authenticated_n6_candidate_locators_bound",
                        "bindings": n6_locator_bindings,
                    }) + "\n")

            note_path = row.get("note_path") or full_led_row.get("note_path") or ""
            note_body = read_note_body(note_path) or ""
            source_requires_no_go = (
                no_go_discipline_gate.source_requires_no_go_discipline(
                    note_path,
                    note_body,
                    (
                        ""
                        if args.from_dispatch
                        else row.get("claim_type") or full_led_row.get("claim_type")
                    ),
                )
            )
            err = validate_verdict(
                blob,
                cid,
                source_requires_no_go=source_requires_no_go,
                evidence_manifest=exact_evidence_manifest,
                prior_claim_scope=prior_claim_scope_for_row(full_led_row),
                expected_invocation_id=audit_invocation_id,
                transport_bounded_n8=transport_bound is not None,
            )
            initial_validation_error = err
            initial_rejected_blob = blob
            repair_elapsed = 0.0
            repair_eligible = validation_repair_eligible(blob, cid, err)
            if err and args.validation_repair_attempts > 0 and repair_eligible:
                for repair_attempt in range(1, args.validation_repair_attempts + 1):
                    print(
                        f"  validation repair {repair_attempt}/"
                        f"{args.validation_repair_attempts}: {err}"
                    )
                    repair_prompt = render_validation_repair_prompt(
                        prompt, blob, err, repair_attempt
                    )
                    if prompt_exceeds_hard_input_limit(repair_prompt):
                        print(
                            "  validation repair skipped: complete prompt "
                            "exceeds the Codex hard input limit"
                        )
                        with run_log.open("a", encoding="utf-8") as f:
                            f.write(json.dumps({
                                "claim_id": cid,
                                "phase": "validation_repair_transport_skipped",
                                "attempt": repair_attempt,
                                "prompt_chars": len(repair_prompt),
                            }) + "\n")
                        break
                    repair_dir = isolated / f"validation-repair-{repair_attempt:02d}"
                    repair_t0 = time.time()
                    repair_ok, repair_stdout, repair_stderr = run_codex(
                        repair_prompt,
                        repair_dir,
                        args.codex_timeout_sec,
                        reasoning_effort=reasoning_effort,
                        model=audit_model,
                    )
                    repair_elapsed += time.time() - repair_t0
                    if not repair_ok:
                        err = f"validation repair codex exec failed: {repair_stderr.strip()[:300]}"
                        with run_log.open("a", encoding="utf-8") as f:
                            f.write(json.dumps({
                                "claim_id": cid,
                                "phase": "validation_repair_codex_failed",
                                "attempt": repair_attempt,
                                "error": err,
                            }) + "\n")
                        continue
                    repair_reply = extract_response(repair_stdout)
                    repair_blob = parse_verdict_json(repair_reply or "")
                    if repair_blob is None:
                        err = "validation repair reply not valid JSON"
                        with run_log.open("a", encoding="utf-8") as f:
                            f.write(json.dumps({
                                "claim_id": cid,
                                "phase": "validation_repair_json_parse_failed",
                                "attempt": repair_attempt,
                                "reply": (repair_reply or "")[:2000],
                            }) + "\n")
                        continue
                    repair_casefold_path_bindings = (
                        bind_authenticated_casefold_evidence_paths(
                            repair_blob, exact_evidence_manifest
                        )
                    )
                    if repair_casefold_path_bindings:
                        with run_log.open("a", encoding="utf-8") as f:
                            f.write(json.dumps({
                                "claim_id": cid,
                                "phase": (
                                    "validation_repair_authenticated_casefold_"
                                    "evidence_paths_bound"
                                ),
                                "attempt": repair_attempt,
                                "bindings": repair_casefold_path_bindings,
                            }) + "\n")
                    repair_n8_universe_bindings = (
                        bind_authenticated_n8_universe_metadata(
                            repair_blob, exact_evidence_manifest
                        )
                    )
                    if repair_n8_universe_bindings:
                        with run_log.open("a", encoding="utf-8") as f:
                            f.write(json.dumps({
                                "claim_id": cid,
                                "phase": (
                                    "validation_repair_authenticated_n8_"
                                    "universe_metadata_bound"
                                ),
                                "attempt": repair_attempt,
                                "bindings": repair_n8_universe_bindings,
                            }) + "\n")
                    repair_bindings = bind_authenticated_occurrence_metadata(
                        repair_blob, exact_evidence_manifest
                    )
                    if repair_bindings:
                        with run_log.open("a", encoding="utf-8") as f:
                            f.write(json.dumps({
                                "claim_id": cid,
                                "phase": (
                                    "validation_repair_authenticated_"
                                    "occurrence_metadata_bound"
                                ),
                                "attempt": repair_attempt,
                                "bindings": repair_bindings,
                            }) + "\n")
                    repair_n6_locator_bindings = (
                        bind_authenticated_n6_candidate_locators(
                            repair_blob, exact_evidence_manifest
                        )
                    )
                    if repair_n6_locator_bindings:
                        with run_log.open("a", encoding="utf-8") as f:
                            f.write(json.dumps({
                                "claim_id": cid,
                                "phase": (
                                    "validation_repair_authenticated_n6_"
                                    "candidate_locators_bound"
                                ),
                                "attempt": repair_attempt,
                                "bindings": repair_n6_locator_bindings,
                            }) + "\n")
                    preservation_error = validation_repair_preservation_error(
                        initial_rejected_blob, repair_blob
                    )
                    repair_error = preservation_error
                    if repair_error is None:
                        repair_error = validate_verdict(
                            repair_blob,
                            cid,
                            source_requires_no_go=source_requires_no_go,
                            evidence_manifest=exact_evidence_manifest,
                            prior_claim_scope=prior_claim_scope_for_row(full_led_row),
                            expected_invocation_id=audit_invocation_id,
                            transport_bounded_n8=transport_bound is not None,
                        )
                    with run_log.open("a", encoding="utf-8") as f:
                        f.write(json.dumps({
                            "claim_id": cid,
                            "phase": (
                                "validation_repair_passed"
                                if repair_error is None
                                else "validation_repair_failed"
                            ),
                            "attempt": repair_attempt,
                            "initial_error": initial_validation_error,
                            "error": repair_error,
                        }) + "\n")
                    if preservation_error is None:
                        blob = repair_blob
                    err = repair_error
                    if err is None:
                        print(
                            f"  validation repair passed "
                            f"({repair_elapsed:.1f}s cumulative)"
                        )
                        break
                elapsed += repair_elapsed
            err = fresh_schema_retry_error(err, initial_validation_error)
            schema_retry_compute_required: str | None = None
            if (
                err
                and args.fresh_schema_retry_attempts > 0
                and fresh_schema_retry_eligible(err)
            ):
                schema_elapsed = 0.0
                for schema_attempt in range(1, args.fresh_schema_retry_attempts + 1):
                    retry_code = fresh_schema_retry_code(err)
                    print(
                        f"  fresh schema retry {schema_attempt}/"
                        f"{args.fresh_schema_retry_attempts}: {retry_code}"
                    )
                    schema_prompt = render_fresh_schema_retry_prompt(
                        prompt, retry_code, schema_attempt
                    )
                    if prompt_exceeds_hard_input_limit(schema_prompt):
                        err = "fresh schema retry prompt exceeds Codex hard input limit"
                        break
                    schema_dir = ISOLATED_BASE / (
                        f"{run_id}-{i:03d}-fresh-schema-{schema_attempt:02d}"
                    )
                    fresh_retry_dirs.append(schema_dir)
                    schema_t0 = time.time()
                    schema_ok, schema_stdout, schema_stderr = run_codex(
                        schema_prompt,
                        schema_dir,
                        args.codex_timeout_sec,
                        reasoning_effort=reasoning_effort,
                        model=audit_model,
                    )
                    schema_elapsed += time.time() - schema_t0
                    if not schema_ok:
                        err = (
                            "fresh schema retry codex exec failed: "
                            f"{schema_stderr.strip()[:300]}"
                        )
                        continue
                    schema_reply = extract_response(schema_stdout)
                    schema_retry_compute_required = compute_required_reason(schema_reply)
                    if schema_retry_compute_required:
                        break
                    schema_blob = parse_verdict_json(schema_reply or "")
                    if schema_blob is None:
                        err = "fresh schema retry reply not valid JSON"
                        continue
                    schema_casefold_path_bindings = (
                        bind_authenticated_casefold_evidence_paths(
                            schema_blob, exact_evidence_manifest
                        )
                    )
                    if schema_casefold_path_bindings:
                        with run_log.open("a", encoding="utf-8") as f:
                            f.write(json.dumps({
                                "claim_id": cid,
                                "phase": (
                                    "fresh_schema_retry_authenticated_casefold_"
                                    "evidence_paths_bound"
                                ),
                                "attempt": schema_attempt,
                                "bindings": schema_casefold_path_bindings,
                            }) + "\n")
                    schema_n8_universe_bindings = (
                        bind_authenticated_n8_universe_metadata(
                            schema_blob, exact_evidence_manifest
                        )
                    )
                    if schema_n8_universe_bindings:
                        with run_log.open("a", encoding="utf-8") as f:
                            f.write(json.dumps({
                                "claim_id": cid,
                                "phase": (
                                    "fresh_schema_retry_authenticated_n8_"
                                    "universe_metadata_bound"
                                ),
                                "attempt": schema_attempt,
                                "bindings": schema_n8_universe_bindings,
                            }) + "\n")
                    schema_bindings = bind_authenticated_occurrence_metadata(
                        schema_blob, exact_evidence_manifest
                    )
                    if schema_bindings:
                        with run_log.open("a", encoding="utf-8") as f:
                            f.write(json.dumps({
                                "claim_id": cid,
                                "phase": (
                                    "fresh_schema_retry_authenticated_"
                                    "occurrence_metadata_bound"
                                ),
                                "attempt": schema_attempt,
                                "bindings": schema_bindings,
                            }) + "\n")
                    schema_n6_locator_bindings = (
                        bind_authenticated_n6_candidate_locators(
                            schema_blob, exact_evidence_manifest
                        )
                    )
                    if schema_n6_locator_bindings:
                        with run_log.open("a", encoding="utf-8") as f:
                            f.write(json.dumps({
                                "claim_id": cid,
                                "phase": (
                                    "fresh_schema_retry_authenticated_n6_"
                                    "candidate_locators_bound"
                                ),
                                "attempt": schema_attempt,
                                "bindings": schema_n6_locator_bindings,
                            }) + "\n")
                    schema_error = validate_verdict(
                        schema_blob,
                        cid,
                        source_requires_no_go=source_requires_no_go,
                        evidence_manifest=exact_evidence_manifest,
                        prior_claim_scope=prior_claim_scope_for_row(full_led_row),
                        expected_invocation_id=audit_invocation_id,
                        transport_bounded_n8=transport_bound is not None,
                    )
                    with run_log.open("a", encoding="utf-8") as f:
                        f.write(json.dumps({
                            "claim_id": cid,
                            "phase": (
                                "fresh_schema_retry_passed"
                                if schema_error is None
                                else "fresh_schema_retry_failed"
                            ),
                            "attempt": schema_attempt,
                            "error": schema_error,
                        }) + "\n")
                    blob = schema_blob
                    err = schema_error
                    if err is None:
                        print(
                            "  fresh schema retry passed "
                            f"({schema_elapsed:.1f}s cumulative)"
                        )
                        break
                elapsed += schema_elapsed
            if schema_retry_compute_required is not None:
                print(f"  COMPUTE_REQUIRED: {schema_retry_compute_required[:200]}")
                skipped += 1
                with run_log.open("a", encoding="utf-8") as f:
                    f.write(json.dumps({
                        "claim_id": cid,
                        "phase": "compute_required",
                        "elapsed_sec": elapsed,
                        "reason": schema_retry_compute_required,
                    }) + "\n")
                continue
            if err:
                print(f"  FAIL validate: {err}")
                failed += 1
                with run_log.open("a", encoding="utf-8") as f:
                    f.write(json.dumps({
                        "claim_id": cid, "phase": "validate_failed",
                        "error": err, "blob": blob
                    }) + "\n")
                continue

            if row_independence == "weak" and blob.get("verdict") == "audited_clean":
                print(
                    "  SKIP: audited_clean cannot be applied under weak "
                    "independence; provenance repair or an independent seat is required"
                )
                skipped += 1
                with run_log.open("a", encoding="utf-8") as f:
                    f.write(json.dumps({
                        "claim_id": cid,
                        "phase": "weak_clean_unratifiable",
                        "verdict": "audited_clean",
                    }) + "\n")
                continue

            full_blob = add_auditor_metadata(
                blob, row_auditor, auditor_family, row_independence,
                auditor_model=audit_model,
                auditor_reasoning_effort=reasoning_effort,
            )
            ok, msg = apply_one(
                full_blob,
                propagate=not args.no_propagate,
                evidence_manifest=exact_evidence_manifest,
            )
            if ok:
                print(f"  OK ({elapsed:.1f}s)  verdict={blob.get('verdict')}  "
                      f"class={blob.get('load_bearing_step_class')}  "
                      f"role={role}/{row_independence}")
                applied += 1
                with run_log.open("a", encoding="utf-8") as f:
                    f.write(json.dumps({
                        "claim_id": cid, "phase": "applied",
                        "elapsed_sec": elapsed,
                        "verdict": blob.get("verdict"),
                        "claim_type": blob.get("claim_type"),
                        "lb_class": blob.get("load_bearing_step_class"),
                        "role": role,
                        "independence": row_independence,
                    }) + "\n")

                # Per-verdict push mode: commit + push immediately
                if args.push_mode == "per-verdict":
                    msg = (
                        f"audit: {cid} -> {blob.get('verdict')} "
                        f"(codex-cli, {audit_model}, xhigh, {role}/{row_independence})"
                    )
                    pushed, push_msg = commit_and_push_to_main(msg)
                    if pushed:
                        print(f"    pushed to main: {push_msg}")
                    else:
                        print(f"    FAIL push: {push_msg}")
                        failed += 1
                        push_failed = True
                        with run_log.open("a", encoding="utf-8") as f:
                            f.write(json.dumps({
                                "claim_id": cid, "phase": "push_failed",
                                "msg": push_msg
                            }) + "\n")
            elif msg.startswith("AUDIT_APPLIED_PROPAGATION_FAILED:"):
                print(f"  FAIL propagation after applied verdict: {msg[:500]}")
                applied += 1
                failed += 1
                propagation_failed = True
                with run_log.open("a", encoding="utf-8") as f:
                    f.write(json.dumps({
                        "claim_id": cid,
                        "phase": "applied_propagation_failed",
                        "verdict": blob.get("verdict"),
                        "message": msg,
                    }) + "\n")
            else:
                print(f"  FAIL apply_audit: {msg[:300]}")
                failed += 1
                with run_log.open("a", encoding="utf-8") as f:
                    f.write(json.dumps({
                        "claim_id": cid, "phase": "apply_failed",
                        "msg": msg[:500], "blob": full_blob
                    }) + "\n")

        finally:
            iso = ISOLATED_BASE / f"{run_id}-{i:03d}"
            if iso.exists():
                shutil.rmtree(iso, ignore_errors=True)
            for retry_dir in fresh_retry_dirs:
                if retry_dir.exists():
                    shutil.rmtree(retry_dir, ignore_errors=True)

    # Batch push mode: one commit covering the whole run
    if (
        args.push_mode == "batch"
        and applied > 0
        and not args.dry_run
        and not propagation_failed
    ):
        crit = f" {args.criticality}" if args.criticality else ""
        msg = (
            f"audit: codex-cli batch {applied} verdict(s){crit} "
            f"({audit_model}, xhigh, {auditor_name_base})"
        )
        pushed, push_msg = commit_and_push_to_main(msg)
        if pushed:
            print(f"\nBatch pushed to main: {push_msg}")
        else:
            print(f"\nBatch push FAILED: {push_msg}")
            print("Local state has the verdicts; run `git push origin main` manually after resolving.")
            push_failed = True
    elif propagation_failed:
        print(
            "\nBatch push suppressed: at least one verdict was applied before "
            "propagation failed. Rerun the pipeline; do not reapply the verdict."
        )

    print(f"\nDone. applied={applied} failed={failed} skipped={skipped}  "
          f"(of {len(targets)} attempted)")
    print(f"Run log: {run_log}")
    if args.no_propagate and applied > 0:
        print("\nNote: --no-propagate was set; run "
              "`bash docs/audit/scripts/run_pipeline.sh` to refresh effective_status.")
    return 0 if failed == 0 and not push_failed else 1


if __name__ == "__main__":
    raise SystemExit(main())
