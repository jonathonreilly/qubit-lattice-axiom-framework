#!/usr/bin/env python3
"""Apply an audit result to a row in the ledger.

Usage:
  echo '<json audit blob>' | python3 apply_audit.py
  python3 apply_audit.py --file path/to/audit.json
  python3 apply_audit.py --batch path/to/dir_of_audit_jsons/

The audit blob must include claim_id, auditor, auditor_family, and the
fields produced by AUDIT_AGENT_PROMPT_TEMPLATE.md. Enforces the hard
rules:
  - independence='weak' may not land audited_clean
  - independence='fresh_context' may land audited_clean when the audit was
    performed in a distinct clean-room session with the restricted audit inputs
  - audited_clean records the audit verdict plus auditor-owned claim_type;
    compute_effective_status.py promotes from claim_type
  - auditor identity must differ from author identity for audited_clean
  - the row's note_hash must match disk (otherwise the audit is stale)
  - fresh-context second passes over existing high/critical terminal verdicts
    record a cross-confirmation comparison before any retraction can cascade
  - non-clean re-audits of confirmed legacy clean rows record a real
    disagreement instead of treating migration-only confirmation as authority
  - ordinary single-auditor passes cannot resolve cross-confirmation
    disagreements; those require the governed five-judge panel path
  - judicial panel reviews may ratify an applyable first, second, or hybrid
    tuple; a panel majority siding with neither is never applied
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import no_go_discipline_gate
import audit_invocation

import ledger_io

# Shared constants/validation for the blocker_fingerprint_v1 stamp: the
# writer imports the comparator's required-keys table so the two can never
# drift (dispatch-retarget design note, 2026-07-16, section 3b).
import classify_runner_passes
import compute_audit_queue

REPO_ROOT = Path(__file__).resolve().parents[3]
LEDGER_PATH = REPO_ROOT / "docs" / "audit" / "data" / "audit_ledger.json"
AXIOM_PREMISE_NODES_PATH = REPO_ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"

sys.path.insert(0, str(REPO_ROOT / "scripts"))
import runner_cache  # noqa: E402  (SHA-pinned runner cache headers)

_AXIOM_PREMISE_IDS: set[str] | None = None
CLIPPED_EVIDENCE_MARKERS = (
    "... [packet-clipped ",
    "... [truncated; runner is ",
    "... [truncated; helper is ",
    "[runner stdout clipped; ",
    "[runner cache excerpt clipped; ",
)
LOAD_BEARING_EVIDENCE_ROLES = {
    "source", "authority", "runner", "helper", "runner_stdout",
    "runner_stdout_cache_eligible", "runner_stdout_independent",
}


def forensic_tier_for(claim_type: str | None, source_required: bool) -> bool:
    """Two-tier assurance: forensic packet plumbing (manifest-backed
    containment, live-stdout citation, snapshot authentication, transport)
    binds no-go rows and freeze/certification runs; development-tier rows
    validate packets structurally (evidence_manifest=None semantics)."""
    return bool(
        source_required
        or (claim_type or "") == "no_go"
        or no_go_discipline_gate.forensic_mode()
    )


def trusted_evidence_manifest(
    expected_claim_id: str | None = None,
    expected_invocation_id: str | None = None,
) -> dict[str, dict] | None:
    """Read orchestrator evidence from the process environment, never audit JSON."""
    raw_path = os.environ.get("CODEX_AUDIT_TRUSTED_EVIDENCE_MANIFEST")
    if not raw_path:
        return None
    try:
        value = json.loads(Path(raw_path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"trusted evidence manifest transport failed: {exc}") from exc
    if not isinstance(value, dict):
        raise ValueError("trusted evidence manifest transport must contain an object")
    if value.get("schema") != "codex_audit_trusted_manifest_v1":
        raise ValueError("trusted evidence manifest transport has no current invocation envelope")
    claim_id = value.get("claim_id")
    invocation_id = value.get("audit_invocation_id")
    issued_at = value.get("issued_at")
    entries = value.get("entries")
    if expected_claim_id is not None and claim_id != expected_claim_id:
        raise ValueError("trusted evidence manifest claim_id mismatch")
    if expected_invocation_id is not None and invocation_id != expected_invocation_id:
        raise ValueError("trusted evidence manifest audit_invocation_id mismatch")
    if audit_invocation.validation_error(invocation_id, required=True):
        raise ValueError("trusted evidence manifest audit_invocation_id is malformed")
    if not isinstance(issued_at, str):
        raise ValueError("trusted evidence manifest issued_at is missing")
    try:
        issued = datetime.fromisoformat(issued_at)
    except ValueError as exc:
        raise ValueError("trusted evidence manifest issued_at is malformed") from exc
    if issued.tzinfo is None:
        raise ValueError("trusted evidence manifest issued_at must be timezone-aware")
    now = datetime.now(timezone.utc)
    if issued > now + timedelta(minutes=5) or now - issued > timedelta(hours=2):
        raise ValueError("trusted evidence manifest invocation envelope is expired")
    if not isinstance(entries, dict):
        raise ValueError("trusted evidence manifest entries must contain an object")
    return entries


def audit_invocation_seen(row: dict, invocation_id: str | None) -> bool:
    if not invocation_id:
        return False
    if row.get("audit_invocation_id") == invocation_id:
        return True
    if invocation_id in (row.get("audit_invocation_history") or []):
        return True
    return f'"audit_invocation_id": "{invocation_id}"' in json.dumps(
        {
            "cross_confirmation": row.get("cross_confirmation"),
            "previous_audits": row.get("previous_audits"),
        },
        sort_keys=True,
    )


def resolved_audit_invocation_id(blob: dict) -> str:
    """Return an explicit one-use id or a stable replay fingerprint."""
    explicit = blob.get("audit_invocation_id")
    if isinstance(explicit, str) and explicit:
        return explicit
    canonical = json.dumps(blob, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()[:32]


def clipped_clean_evidence_error(manifest: dict[str, dict]) -> str | None:
    clipped_paths = sorted(
        path
        for path, entry in manifest.items()
        if set(entry.get("roles") or []) & LOAD_BEARING_EVIDENCE_ROLES
        and any(
            marker in str(entry.get("text") or "")
            for marker in CLIPPED_EVIDENCE_MARKERS
        )
    )
    if clipped_paths:
        return (
            "audited_clean requires complete load-bearing packet surfaces; "
            f"clipped evidence: {clipped_paths}"
        )
    return None


def consume_audit_invocation(row: dict, invocation_id: str | None) -> None:
    """Record accepted invocation IDs append-only before updating the live ID."""
    if not invocation_id:
        return
    history = list(row.get("audit_invocation_history") or [])
    prior = row.get("audit_invocation_id")
    for value in (prior, invocation_id):
        if value and value not in history:
            history.append(value)
    row["audit_invocation_history"] = history
    row["audit_invocation_id"] = invocation_id


def audit_invocation_error(blob: dict) -> str | None:
    """Validate the one-use invocation envelope for orchestrated audits.

    Human/external audits may still be applied without an orchestrator.  Once
    the trusted-manifest transport is present, however, omitting the id would
    detach the evidence snapshot from its one-use invocation and permit replay.
    Any id that is supplied is therefore validated, and the trusted transport
    makes it mandatory for both ordinary and judicial inputs.
    """
    invocation_id = blob.get("audit_invocation_id")
    if invocation_id is None:
        if os.environ.get("CODEX_AUDIT_TRUSTED_EVIDENCE_MANIFEST"):
            return "trusted evidence manifest requires audit_invocation_id"
        return None
    return audit_invocation.validation_error(invocation_id, required=True)


def trusted_manifest_current_error(
    packet: dict,
    trusted_manifest: dict[str, dict],
    row: dict,
    rows: dict[str, dict],
    *,
    dynamic_index_drift_invalidates: bool = True,
) -> str | None:
    """Reject replayed evidence after stable-content or governed index drift."""
    probe_packet = dict(packet)
    probe_packet["evidence_snapshot"] = (
        no_go_discipline_gate.build_evidence_snapshot(
            probe_packet, trusted_manifest
        )
    )
    current_row = row
    if no_go_discipline_gate.manifest_has_blind_reaudit_control(trusted_manifest):
        current_row = no_go_discipline_gate.blind_reaudit_row_projection(row)
    current_manifest = no_go_discipline_gate.build_evidence_manifest(
        current_row, rows, REPO_ROOT
    )
    return no_go_discipline_gate.evidence_snapshot_current_error(
        probe_packet,
        current_manifest,
        dynamic_index_drift_invalidates=dynamic_index_drift_invalidates,
    )


def cross_summary_no_go_error(
    summary: dict,
    *,
    source_required: bool,
    current_evidence_manifest: dict[str, dict],
) -> str | None:
    """Validate a prior cross-confirmation seat before it can be ratified."""
    packet = summary.get("no_go_discipline")
    required = (
        source_required
        or no_go_discipline_gate.output_requires_no_go_discipline(summary)
        or bool(summary.get("negative_assertion_classes"))
    ) and no_go_discipline_gate.packet_requirement_binds(
        summary, source_required=source_required
    )
    if packet is None:
        return (
            "No-Go Discipline N1-N8 packet is required for the prior seat"
            if required
            else None
        )
    snapshot_manifest = no_go_discipline_gate.evidence_manifest_from_snapshot(
        packet if isinstance(packet, dict) else {}
    )
    _forensic = forensic_tier_for(summary.get("claim_type"), source_required)
    if not _forensic:
        # Development tier: structural validation of the prior seat's packet.
        return no_go_discipline_gate.validate_no_go_discipline(
            {
                **summary,
                "verdict": summary.get("verdict"),
                "chain_closes": summary.get("verdict") == "audited_clean",
            },
            source_required=source_required,
            evidence_manifest=None,
            structural_only=True,
        )
    if snapshot_manifest is None:
        return "authenticated evidence_snapshot is required"
    snapshot_error = no_go_discipline_gate.evidence_snapshot_current_error(
        packet, current_evidence_manifest
    )
    if snapshot_error:
        return snapshot_error
    return no_go_discipline_gate.validate_no_go_discipline(
        {
            **summary,
            "verdict": summary.get("verdict"),
            "chain_closes": summary.get("verdict") == "audited_clean",
        },
        source_required=source_required,
        evidence_manifest=snapshot_manifest,
    )


def prior_claim_scope_for_row(row: dict) -> str | None:
    if isinstance(row.get("claim_scope"), str) and row["claim_scope"].strip():
        return row["claim_scope"]
    for archived in reversed(row.get("previous_audits") or []):
        if isinstance(archived, dict) and isinstance(archived.get("claim_scope"), str):
            scope = archived["claim_scope"]
            if scope.strip():
                return scope
    return None


def archive_replaced_cross_confirmation_first(row: dict, first: dict) -> None:
    archived = dict(first)
    archived["audit_status"] = first.get("verdict")
    archived["archived_at"] = datetime.now(timezone.utc).isoformat()
    archived["invalidation_reason"] = (
        "no_go_discipline_cross_confirmation_packet_invalid"
    )
    history = list(row.get("previous_audits") or [])
    history.append(archived)
    row["previous_audits"] = history


def archive_invalid_first_and_require_fresh_packet(row: dict, first: dict) -> None:
    """Persist invalid history before asking a new first seat to disposition it."""
    archive_replaced_cross_confirmation_first(row, first)
    row.pop("cross_confirmation", None)
    row.pop("no_go_discipline", None)
    row.pop("negative_assertion_classes", None)
    row["audit_status"] = "unaudited"
    row["blocker"] = "invalid_cross_confirmation_first_archived_reaudit_required"


def axiom_premise_ids() -> set[str]:
    """Canonical axiom-premise claim_ids (see axiom_premise_nodes.json)."""
    global _AXIOM_PREMISE_IDS
    if _AXIOM_PREMISE_IDS is None:
        try:
            data = json.loads(AXIOM_PREMISE_NODES_PATH.read_text(encoding="utf-8"))
            _AXIOM_PREMISE_IDS = set(data.get("canonical_ids") or [])
        except Exception:
            _AXIOM_PREMISE_IDS = set()
    return _AXIOM_PREMISE_IDS

REQUIRED_FIELDS = {
    "claim_id",
    "verdict",
    "claim_type",
    "claim_scope",
    "auditor",
    "auditor_family",
    "auditor_model",
    "auditor_reasoning_effort",
    "independence",
}
JUDICIAL_REQUIRED_FIELDS = {
    "claim_id",
    "third_auditor",
    "auditor_family",
    "auditor_model",
    "auditor_reasoning_effort",
    "independence",
    "sided_with",
    "ratified_verdict",
    "ratified_claim_type",
    "ratified_claim_scope",
    "ratified_load_bearing_step_class",
    "judgment_rationale",
    "first_auditor_error",
    "second_auditor_error",
}

# Reasoning-effort policy for incoming audits. The audit lane runs at xhigh
# only; weaker effort levels are not accepted as ratifying evidence.
REQUIRED_REASONING_EFFORT = "xhigh"
ALLOWED_VERDICTS = {
    "audited_clean",
    "audited_renaming",
    "audited_conditional",
    "audited_decoration",
    "audited_failed",
    "audited_numerical_match",
}

ALLOWED_CLAIM_TYPES = {
    "positive_theorem",
    "bounded_theorem",
    "no_go",
    "open_gate",
    "decoration",
    "meta",
}

ALLOWED_INDEPENDENCE = {"weak", "fresh_context", "cross_family", "strong", "external", "judicial_review"}
CLEAN_INDEPENDENCE = ALLOWED_INDEPENDENCE - {"weak"}

# Vocabulary-drift status, orthogonal to audit_status. See
# docs/repo/VOCABULARY_HYGIENE_DESIGN.md and
# docs/repo/controlled_vocabulary.yaml. prose_status records whether the
# source note's vocabulary is compliant; it does NOT propagate into
# effective_status (physics ≠ prose).
ALLOWED_PROSE_STATUS = {
    "clean",
    "auto_corrected",
    "needs_human_vocab_decision",
    "not_evaluated_pre_vocab_lint",
    "queue_backpressure_exceeded",
}
PROSE_FIX_REQUIRED_FIELDS = {"old_hash", "new_hash", "prose_status", "prose_corrections"}

# Minimum auditor-family rank for incoming Codex audits. Existing ledger rows
# are not invalidated by this script, but every new audit blob applied after
# this policy must meet the floor. This catches manual `apply_audit.py`
# invocations that bypass the runner's model floor, e.g. a hand-written audit
# blob with auditor_family=codex-gpt-5. The current audit authority is pinned
# to GPT-5.6-sol, so older Codex families must fail even for non-clean
# verdicts; non-Codex human/judicial families remain independently admissible.
MIN_NEW_AUDIT_FAMILY_RANK = (5, 6)
_FAMILY_RANK_RE = re.compile(r"codex-gpt-(\d+(?:\.\d+)*)$")
_SUPPORTED_CODEX_MODEL_RE = re.compile(
    r"gpt-(?P<version>\d+(?:\.\d+)*)(?:-sol)?$"
)


def _family_rank(family: str | None) -> tuple[int, ...] | None:
    if not family:
        return None
    m = _FAMILY_RANK_RE.match(family)
    if not m:
        return None
    return tuple(int(p) for p in m.group(1).split("."))


def _family_meets_floor(family: str | None) -> bool:
    """True if family parses to a rank >= MIN_NEW_AUDIT_FAMILY_RANK.

    Non-codex families (e.g. claude-* manual reviews, legacy-confirmed-clean)
    pass the floor — only codex-gpt-* families are rank-checked. This
    keeps the door open for human / Claude judicial reviews which are
    not bound by the codex model schedule.
    """
    if not family or not family.startswith("codex-gpt-"):
        return True
    rank = _family_rank(family)
    if not rank:
        # Unparseable codex-gpt-* — refuse to bless something we can't measure.
        return False
    floor = MIN_NEW_AUDIT_FAMILY_RANK
    width = max(len(rank), len(floor))
    rank_padded = rank + (0,) * (width - len(rank))
    floor_padded = floor + (0,) * (width - len(floor))
    return rank_padded >= floor_padded


def _canonical_codex_family_for_model(model: str) -> str:
    """Map an accepted exact model slug to its stable numeric family."""
    match = _SUPPORTED_CODEX_MODEL_RE.fullmatch(model)
    if match:
        return f"codex-gpt-{match.group('version')}"
    return f"codex-{model}"


def _canonicalize_existing_auditor_family(family: str | None) -> str | None:
    """Normalize legacy suffix-bearing Codex families for independence checks."""
    if not family or not family.startswith("codex-"):
        return family
    return _canonical_codex_family_for_model(family.removeprefix("codex-"))


ALLOWED_JUDICIAL_SIDES = {"first", "second", "hybrid", "neither"}
AUDIT_TUPLE_AGREEMENT_SCHEMA = "audit_tuple_v2"
JUDICIAL_REVIEWABLE_STATUSES = {
    "disagreement",
    "third_confirmed_first",
    "third_confirmed_second",
    "third_confirmed_hybrid",
}
TERMINAL_CROSS_CONFIRM_VERDICTS = {
    "audited_renaming",
    "audited_numerical_match",
    "audited_failed",
}


def clean_independence_error(independence: str, criticality: str | None = None) -> str | None:
    if independence in CLEAN_INDEPENDENCE:
        return None
    if criticality in {"critical", "high"}:
        return f"criticality={criticality} requires independence >= fresh_context for audited_clean"
    return "audited_clean requires independence != 'weak'"


def cross_confirmation_error(first: dict, audit: dict) -> str | None:
    """Return a rejection reason when the second critical audit is not independent."""
    first_auditor = first.get("auditor")
    auditor = audit.get("auditor")
    if first_auditor and first_auditor == auditor:
        return "second auditor must have a distinct auditor identity/session from the first"

    same_family = (
        _canonicalize_existing_auditor_family(first.get("auditor_family"))
        == _canonicalize_existing_auditor_family(audit.get("auditor_family"))
    )
    if same_family and audit.get("independence") != "fresh_context":
        return (
            "same-family second audit requires independence='fresh_context' "
            "to document a restricted-input clean-room session"
        )
    return None


def normalized_negative_assertion_classes(blob: dict) -> tuple[str, ...]:
    """Return the declaration as a stable component of the audit tuple.

    Missing legacy declarations are treated as the historical equivalent of an
    empty declaration. New audit inputs are separately required to carry an
    explicit validated list before they reach any comparison path.
    """
    declared = blob.get("negative_assertion_classes")
    if not isinstance(declared, list):
        return ()
    return tuple(sorted({item for item in declared if isinstance(item, str)}))


def normalized_claim_scope(blob: dict) -> str:
    """Normalize insignificant whitespace without weakening scoped agreement."""
    scope = blob.get("claim_scope")
    if not isinstance(scope, str):
        return ""
    return " ".join(scope.split())


def audit_tuples_match(first: dict, second: dict) -> bool:
    """Compare every field whose disagreement requires governed resolution."""
    return (
        first.get("verdict") == second.get("verdict")
        and first.get("claim_type") == second.get("claim_type")
        and first.get("load_bearing_step_class")
        == second.get("load_bearing_step_class")
        and normalized_claim_scope(first) == normalized_claim_scope(second)
        and normalized_negative_assertion_classes(first)
        == normalized_negative_assertion_classes(second)
    )


def audit_summary_tuple_schema_error(summary: object) -> str | None:
    """Require a complete typed tuple before minting ``audit_tuple_v2``."""
    if not isinstance(summary, dict) or not summary:
        return "audit summary must be a non-empty object"
    required = {
        "verdict",
        "claim_type",
        "claim_scope",
        "load_bearing_step_class",
        "negative_assertion_classes",
    }
    missing = required - set(summary)
    if missing:
        return f"audit summary missing tuple fields: {sorted(missing)}"
    verdict = summary.get("verdict")
    if verdict not in ALLOWED_VERDICTS:
        return f"audit summary has non-terminal verdict {verdict!r}"
    claim_type = summary.get("claim_type")
    if claim_type not in ALLOWED_CLAIM_TYPES:
        return f"audit summary has invalid claim_type {claim_type!r}"
    scope = summary.get("claim_scope")
    if not isinstance(scope, str) or not scope.strip():
        return "audit summary claim_scope must be a non-empty string"
    step_class = summary.get("load_bearing_step_class")
    if not isinstance(step_class, str) or not step_class.strip():
        return "audit summary load_bearing_step_class must be a non-empty string"
    declared = summary.get("negative_assertion_classes")
    if not isinstance(declared, list) or not all(
        isinstance(item, str) for item in declared
    ):
        return "audit summary negative_assertion_classes must be a list of strings"
    unknown = sorted(
        set(declared) - no_go_discipline_gate.POLICY_NEGATIVE_CLASSES
    )
    if unknown:
        return f"audit summary has unknown negative_assertion_classes: {unknown}"
    return None


def legacy_tuple_upgrade_error(label: str, summary: object) -> str | None:
    """Explain why an old seat cannot be relabeled as exact v2 agreement."""
    error = audit_summary_tuple_schema_error(summary)
    if error is None:
        return None
    return (
        f"{label} cannot be upgraded to {AUDIT_TUPLE_AGREEMENT_SCHEMA}: "
        f"{error}; fresh re-audit required"
    )


def third_confirmation_error(cross_confirmation: dict, audit: dict) -> str | None:
    """Return a rejection reason when the third audit is not independent."""
    prior_auditors = {
        (cross_confirmation.get("first_audit") or {}).get("auditor"),
        (cross_confirmation.get("second_audit") or {}).get("auditor"),
    }
    prior_auditors.discard(None)
    auditor = audit.get("auditor")
    if auditor in prior_auditors:
        return "third auditor must have a distinct auditor identity/session from both prior auditors"

    prior_families = {
        _canonicalize_existing_auditor_family(
            (cross_confirmation.get("first_audit") or {}).get("auditor_family")
        ),
        _canonicalize_existing_auditor_family(
            (cross_confirmation.get("second_audit") or {}).get("auditor_family")
        ),
    }
    prior_families.discard(None)
    current_family = _canonicalize_existing_auditor_family(
        audit.get("auditor_family")
    )
    if current_family in prior_families and audit.get("independence") != "fresh_context":
        return (
            "same-family third audit requires independence='fresh_context' "
            "to document a restricted-input clean-room session"
        )
    return None


def audit_summary_from_row(row: dict) -> dict:
    """Build the restricted summary used for later comparison."""
    summary = {
        "auditor": row.get("auditor"),
        "auditor_family": row.get("auditor_family"),
        "auditor_model": row.get("auditor_model"),
        "auditor_reasoning_effort": row.get("auditor_reasoning_effort"),
        "independence": row.get("independence"),
        "audit_date": row.get("audit_date"),
        "claim_type": row.get("claim_type"),
        "claim_scope": row.get("claim_scope"),
        "load_bearing_step": row.get("load_bearing_step"),
        "load_bearing_step_class": row.get("load_bearing_step_class"),
        "chain_closes": row.get("chain_closes"),
        "chain_closure_explanation": row.get("chain_closure_explanation"),
        "verdict_rationale": row.get("verdict_rationale"),
        "notes_for_re_audit_if_any": row.get("notes_for_re_audit_if_any"),
        "runner_check_breakdown": row.get("runner_check_breakdown"),
        "open_dependency_paths": row.get("open_dependency_paths"),
        "decoration_parent_claim_id": row.get("decoration_parent_claim_id"),
        "negative_assertion_classes": list(
            normalized_negative_assertion_classes(row)
        ),
        "verdict": row.get("audit_status"),
        "audit_invocation_id": row.get("audit_invocation_id"),
    }
    if row.get("no_go_discipline") is not None:
        summary["no_go_discipline"] = row.get("no_go_discipline")
    return summary


def audit_summary_from_blob(audit: dict) -> dict:
    summary = {
        "auditor": audit.get("auditor"),
        "auditor_family": audit.get("auditor_family"),
        "auditor_model": audit.get("auditor_model"),
        "auditor_reasoning_effort": audit.get("auditor_reasoning_effort"),
        "independence": audit.get("independence"),
        "audit_date": audit.get("audit_date") or datetime.now(timezone.utc).isoformat(),
        "claim_type": audit.get("claim_type"),
        "claim_scope": audit.get("claim_scope"),
        "load_bearing_step": audit.get("load_bearing_step"),
        "load_bearing_step_class": audit.get("load_bearing_step_class"),
        "chain_closes": audit.get("chain_closes"),
        "chain_closure_explanation": audit.get("chain_closure_explanation"),
        "verdict_rationale": audit.get("verdict_rationale"),
        "notes_for_re_audit_if_any": audit.get("notes_for_re_audit_if_any"),
        "runner_check_breakdown": audit.get("runner_check_breakdown"),
        "open_dependency_paths": audit.get("open_dependency_paths"),
        "decoration_parent_claim_id": audit.get("decoration_parent_claim_id"),
        "negative_assertion_classes": list(
            normalized_negative_assertion_classes(audit)
        ),
        "verdict": audit.get("verdict"),
        "audit_invocation_id": audit.get("audit_invocation_id"),
    }
    if audit.get("no_go_discipline") is not None:
        summary["no_go_discipline"] = audit.get("no_go_discipline")
    return summary


def judicial_summary_from_blob(judgment: dict) -> dict:
    summary = {
        "auditor": judgment.get("third_auditor"),
        "auditor_family": judgment.get("auditor_family"),
        "auditor_model": judgment.get("auditor_model"),
        "auditor_reasoning_effort": judgment.get("auditor_reasoning_effort"),
        "independence": judgment.get("independence"),
        "audit_date": judgment.get("audit_date") or datetime.now(timezone.utc).isoformat(),
        "claim_type": judgment.get("ratified_claim_type"),
        "claim_scope": judgment.get("ratified_claim_scope"),
        "load_bearing_step_class": judgment.get("ratified_load_bearing_step_class"),
        "negative_assertion_classes": list(
            normalized_negative_assertion_classes(judgment)
        ),
        "verdict": judgment.get("ratified_verdict"),
        "audit_invocation_id": judgment.get("audit_invocation_id"),
        "sided_with": judgment.get("sided_with"),
        "judgment_rationale": judgment.get("judgment_rationale"),
        "first_auditor_error": judgment.get("first_auditor_error"),
        "second_auditor_error": judgment.get("second_auditor_error"),
    }
    decoration_parent = (
        judgment.get("ratified_decoration_parent_claim_id")
        or judgment.get("decoration_parent_claim_id")
    )
    if decoration_parent:
        summary["decoration_parent_claim_id"] = decoration_parent
    if "runner_check_breakdown" in judgment:
        summary["runner_check_breakdown"] = judgment["runner_check_breakdown"]
    if judgment.get("no_go_discipline") is not None:
        summary["no_go_discipline"] = judgment.get("no_go_discipline")
    return summary


# Verdicts whose snapshot must carry the complete versioned
# blocker_fingerprint_v1 baseline set (dispatch-retarget design note,
# 2026-07-16, section 3b). These are the owner-ruled non-terminal resting
# states that re-enter the pending queue; the shadow would-park comparator
# (compute_audit_queue._live_conditional_would_park) reads the live row's
# top-level audit_state_snapshot for exactly this population. Stamping is
# reporting-side enablement only: no dispatch decision reads the v1 fields,
# and legacy rows are never rewritten (their next organic verdict stamps).
FINGERPRINT_STAMP_VERDICTS = {"audited_conditional", "audited_failed"}


def _sha256_file(path: Path) -> str | None:
    """SHA-256 of a file's bytes; None when unreadable/missing."""
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError:
        return None


def _fingerprint_policy_versions() -> dict:
    """Packet/prompt/gate policy versions in force at verdict-write time.

    Computed from the live policy surfaces during this apply pass — never
    from a cached report. Content hashes are used where no declared version
    constant exists, so any policy movement is visible as a channel delta.
    """
    return {
        "audit_tuple_agreement_schema": AUDIT_TUPLE_AGREEMENT_SCHEMA,
        "n8_source_corpus_version": no_go_discipline_gate.N8_SOURCE_CORPUS_VERSION,
        "no_go_discipline_gate_sha256": _sha256_file(
            Path(no_go_discipline_gate.__file__)
        ),
        "audit_prompt_template_sha256": _sha256_file(
            REPO_ROOT / "docs" / "audit" / "AUDIT_AGENT_PROMPT_TEMPLATE.md"
        ),
    }


def _fingerprint_premise_registry_epoch() -> str:
    """Content identity of the premise registry at verdict-write time.

    The registry (axiom_premise_nodes.json) carries no epoch counter, so the
    honest epoch marker is its content hash: it changes exactly when the
    registry changes, and never otherwise (deterministic, timestamp-free).
    """
    digest = _sha256_file(
        REPO_ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
    )
    return digest if digest is not None else "premise_registry_absent"


def _fingerprint_runner_cache_state(row: dict) -> dict:
    """Per-path runner-cache identity for the row's runner and helpers.

    Records the SHA-pinned cache header fields plus freshness, read from
    disk during this apply pass (logs/runner-cache is the canonical cache
    surface; see runner_cache.py). Header fields carry no timestamps, so
    the recorded state is deterministic for a given repo state.
    """
    state: dict[str, dict] = {}
    paths = [
        p
        for p in [row.get("runner_path"), *(row.get("helper_runner_paths") or [])]
        if p
    ]
    for path in sorted(set(paths)):
        _cache_path, header, _body = runner_cache.load_cache(path)
        header = header or {}
        state[path] = {
            "cache_freshness": runner_cache.cache_status(path),
            "cache_runner_sha256": header.get("runner_sha256"),
            "cache_status": header.get("status"),
            "cache_exit_code": header.get("exit_code"),
        }
    return state


def _fingerprint_artifact_classifier_state(row: dict) -> dict:
    """Static classifier view of the row's runner at verdict-write time.

    Recomputed from the runner source via classify_runner_passes (the same
    routines the pipeline classifier uses), never read from the generated
    runner_classification.json — that file may be stale relative to this
    apply pass. Mirrors the per_runner entry shape.
    """
    runner_path = row.get("runner_path")
    if not runner_path:
        return {}
    p = REPO_ROOT / runner_path
    if not p.exists():
        return {"runner_path": runner_path, "exists": False}
    try:
        source = p.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return {"runner_path": runner_path, "exists": True, "read_error": True}
    counts = classify_runner_passes.classify_source(source)
    dominant = max(counts, key=lambda k: counts[k]) if any(counts.values()) else None
    return {
        "runner_path": runner_path,
        "exists": True,
        "counts": counts,
        "assert_count": classify_runner_passes.count_assert_pass_lines(source),
        "dominant_class": dominant,
        "decoration_candidate": (
            counts["D"] == 0 and counts["C"] == 0 and counts["A"] + counts["B"] > 0
        ),
    }


def snapshot_audit_state(row: dict, rows: dict[str, dict]) -> dict:
    deps = sorted(row.get("deps", []))
    runner_hash_value: str | None = None
    runner_path = row.get("runner_path")
    if runner_path:
        rp = REPO_ROOT / runner_path
        if rp.exists():
            import hashlib as _hashlib
            try:
                runner_hash_value = _hashlib.sha256(rp.read_bytes()).hexdigest()
            except OSError:
                runner_hash_value = None
    helper_runner_hashes: dict[str, str | None] = {}
    for helper_path in sorted(set(row.get("helper_runner_paths") or [])):
        hp = REPO_ROOT / helper_path
        helper_hash: str | None = None
        if hp.exists():
            try:
                helper_hash = hashlib.sha256(hp.read_bytes()).hexdigest()
            except OSError:
                pass
        helper_runner_hashes[helper_path] = helper_hash
    snapshot = {
        "deps": deps,
        "dep_effective_status": {
            d: rows.get(d, {}).get("effective_status") or "unaudited"
            for d in deps
        },
        # Per-dep claim_type and claim_scope, so invalidate_stale_audits
        # can detect upstream audit-side narrowing or retyping that
        # happens without a note-text edit (silent w.r.t. note-hash
        # drift and dep_effective_status weakening when both before and
        # after live in the retained tier).
        "dep_claim_type": {
            d: rows.get(d, {}).get("claim_type")
            for d in deps
        },
        "dep_claim_scope": {
            d: rows.get(d, {}).get("claim_scope")
            for d in deps
        },
        # Note-hash of any axiom-premise dep at audit time. An axiom-premise
        # node stays effective_status=meta across content edits, so a change
        # to the axiom prose is invisible to the dep_effective_status /
        # dep_claim_type / dep_claim_scope triggers above. Recording its hash
        # lets invalidate_stale_audits re-look at direct citers when the axiom
        # text actually changes.
        "dep_axiom_premise_note_hash": {
            d: rows.get(d, {}).get("note_hash")
            for d in deps
            if d in axiom_premise_ids()
        },
        "criticality": row.get("criticality"),
        "load_bearing_score": row.get("load_bearing_score"),
        "transitive_descendants": row.get("transitive_descendants"),
        "runner_hash": runner_hash_value,
        "helper_runner_hashes": helper_runner_hashes,
    }
    # v1 blocker-fingerprint stamp for NEW conditional/failed verdict writes
    # only (dispatch-retarget design note, 2026-07-16, section 3b). Callers
    # set row["audit_status"] to the just-applied verdict before snapshotting,
    # so gating on it here covers both the ordinary and the judicial path.
    # Existing ledger rows are never rewritten — legacy snapshots stay
    # honestly fail-open in the shadow comparator until organically
    # re-audited. Every channel value above and below is computed during
    # this apply pass; nothing is copied from a stale cache or report.
    if row.get("audit_status") in FINGERPRINT_STAMP_VERDICTS:
        snapshot["schema"] = compute_audit_queue.BLOCKER_FINGERPRINT_V1
        snapshot["runner_cache_state"] = _fingerprint_runner_cache_state(row)
        snapshot["artifact_classifier_state"] = (
            _fingerprint_artifact_classifier_state(row)
        )
        snapshot["policy_versions"] = _fingerprint_policy_versions()
        snapshot["premise_registry_epoch"] = _fingerprint_premise_registry_epoch()
        # Writer-side mirror of the comparator's validation matrix: a v1
        # writer that omits or ill-types a required baseline is a bug and
        # must fail LOUDLY at write time, never land a snapshot the
        # comparator would explode on (FingerprintV1Invalid downstream).
        problems = [
            key
            for key, typ in compute_audit_queue.FINGERPRINT_V1_REQUIRED_KEYS.items()
            if key not in snapshot or not isinstance(snapshot.get(key), typ)
        ]
        if problems:
            raise compute_audit_queue.FingerprintV1Invalid(
                "refusing to write an incomplete/ill-typed v1 snapshot "
                f"(missing/ill-typed baselines {problems}) on "
                f"{row.get('note_path') or row.get('claim_id')}"
            )
    return snapshot


def legacy_confirmed_clean_claim_type_reaudit(row: dict, verdict: str, xc_status: str | None) -> bool:
    """Return true when a legacy clean row only needs scoped claim typing.

    PR291 made claim_type part of the audit verdict. Older critical clean
    rows can already have confirmed cross-confirmation whose summaries predate
    claim_type, so comparing a new scoped re-audit against those missing fields
    would create a false disagreement. In that migration-only case, keep the
    existing clean cross-confirmation and let the new restricted-input audit
    own claim_type and claim_scope.

    Some rows were later left at audited_conditional while still carrying an
    already-confirmed legacy clean cross-confirmation. If the new restricted
    audit is clean and the prior confirmed summaries are clean but claim-type
    blind, treat that the same way; the current source prose/status is not the
    authority under the PR291 regime.
    """
    if row.get("claim_type_provenance") != "backfilled_pending_reaudit":
        return False
    if row.get("audit_status") not in {"audited_clean", "audited_conditional"}:
        return False
    if verdict != "audited_clean":
        return False
    if xc_status not in {"confirmed", "third_confirmed_first", "third_confirmed_second", "third_confirmed_hybrid"}:
        return False
    xc = row.get("cross_confirmation") or {}
    first = xc.get("first_audit") or {}
    second = xc.get("second_audit") or {}
    third = xc.get("third_audit") or {}
    if xc_status == "third_confirmed_first":
        return (
            first.get("verdict") == "audited_clean"
            and third.get("verdict") == "audited_clean"
            and first.get("claim_type") is None
            and third.get("claim_type") is None
        )
    if xc_status == "third_confirmed_second":
        return (
            second.get("verdict") == "audited_clean"
            and third.get("verdict") == "audited_clean"
            and second.get("claim_type") is None
            and third.get("claim_type") is None
        )
    if xc_status == "third_confirmed_hybrid":
        return third.get("verdict") == "audited_clean" and third.get("claim_type") is None
    return (
        first.get("verdict") == "audited_clean"
        and second.get("verdict") == "audited_clean"
        and first.get("claim_type") is None
        and second.get("claim_type") is None
    )


def legacy_confirmed_clean_verdict_reaudit(row: dict, verdict: str, xc_status: str | None) -> bool:
    """Return true when a scoped legacy clean re-audit changes the verdict."""
    if row.get("claim_type_provenance") != "backfilled_pending_reaudit":
        return False
    if row.get("audit_status") not in {"audited_clean", "audited_conditional"}:
        return False
    if verdict == "audited_clean":
        return False
    if xc_status not in {"confirmed", "third_confirmed_first", "third_confirmed_second", "third_confirmed_hybrid"}:
        return False
    xc = row.get("cross_confirmation") or {}
    first = xc.get("first_audit") or {}
    second = xc.get("second_audit") or {}
    third = xc.get("third_audit") or {}
    if xc_status == "third_confirmed_first":
        return first.get("verdict") == "audited_clean" and third.get("verdict") == "audited_clean"
    if xc_status == "third_confirmed_second":
        return second.get("verdict") == "audited_clean" and third.get("verdict") == "audited_clean"
    if xc_status == "third_confirmed_hybrid":
        return third.get("verdict") == "audited_clean"
    return first.get("verdict") == "audited_clean" and second.get("verdict") == "audited_clean"


def legacy_clean_consensus_summary(row: dict, audit: dict, xc_status: str | None) -> dict:
    """Collapse old clean confirmations into the side opposed to a new verdict."""
    xc = row.get("cross_confirmation") or {}
    if xc_status == "third_confirmed_first":
        winning = [xc.get("first_audit") or {}, xc.get("third_audit") or {}]
    elif xc_status == "third_confirmed_second":
        winning = [xc.get("second_audit") or {}, xc.get("third_audit") or {}]
    elif xc_status == "third_confirmed_hybrid":
        winning = [xc.get("third_audit") or {}]
    else:
        winning = [xc.get("first_audit") or {}, xc.get("second_audit") or {}]

    dates = [w.get("audit_date") for w in winning if w.get("audit_date")]
    auditors = [w.get("auditor") for w in winning if w.get("auditor")]
    families = sorted({w.get("auditor_family") for w in winning if w.get("auditor_family")})
    return {
        "auditor": "legacy-confirmed-clean-cross-confirmation",
        "auditor_family": "legacy-confirmed-clean",
        "independence": "fresh_context",
        "audit_date": max(dates) if dates else row.get("audit_date"),
        "claim_type": audit.get("claim_type"),
        "claim_scope": audit.get("claim_scope") or row.get("claim_scope"),
        "load_bearing_step_class": row.get("load_bearing_step_class"),
        "verdict": "audited_clean",
        "legacy_auditors": auditors,
        "legacy_auditor_families": families,
    }


def note_hash_drift_error(row: dict) -> str | None:
    on_disk_path = REPO_ROOT / row.get("note_path", "")
    if not on_disk_path.exists():
        return None
    import hashlib
    on_disk_hash = hashlib.sha256(
        on_disk_path.read_text(encoding="utf-8", errors="replace").encode("utf-8")
    ).hexdigest()
    if on_disk_hash != row.get("note_hash"):
        return "note_hash drift; rerun seed_audit_ledger.py before applying audit"
    return None


def apply_pre_audit_prose_fix(row: dict, prose_fix: dict) -> str | None:
    """Atomically refresh note_hash and write prose_status / prose_corrections.

    The envelope carries {old_hash, new_hash, prose_status, prose_corrections}.
    Verifies the envelope's old_hash matches the row's current note_hash (the
    envelope was computed against the correct base), then refreshes
    note_hash to envelope's new_hash and records the prose fields. Returns
    an error string on validation failure, None on success.

    Required when an audit chain runs `vocab_lint --fix` on the source note
    before applying the verdict: the fix changes note content and therefore
    note_hash, which would otherwise trigger the hash-drift rejection in
    note_hash_drift_error(). The envelope is the atomic refresh path. See
    docs/repo/VOCABULARY_HYGIENE_DESIGN.md §Auto-correct mechanism.
    """
    if not isinstance(prose_fix, dict):
        return "pre_audit_prose_fix must be a dict"
    missing = PROSE_FIX_REQUIRED_FIELDS - set(prose_fix)
    if missing:
        return f"pre_audit_prose_fix missing fields: {sorted(missing)}"
    if prose_fix["old_hash"] != row.get("note_hash"):
        return (
            f"pre_audit_prose_fix.old_hash {prose_fix['old_hash']!r} does not "
            f"match row.note_hash {row.get('note_hash')!r}"
        )
    prose_status = prose_fix["prose_status"]
    if prose_status not in ALLOWED_PROSE_STATUS:
        return (
            f"prose_status {prose_status!r} not in {sorted(ALLOWED_PROSE_STATUS)}"
        )
    if not isinstance(prose_fix["prose_corrections"], list):
        return "prose_corrections must be a list of {rule_id, before, after} dicts"
    on_disk_path = REPO_ROOT / row.get("note_path", "")
    if on_disk_path.exists():
        import hashlib

        on_disk_hash = hashlib.sha256(
            on_disk_path.read_text(encoding="utf-8", errors="replace").encode("utf-8")
        ).hexdigest()
        if on_disk_hash != prose_fix["new_hash"]:
            return (
                f"pre_audit_prose_fix.new_hash {prose_fix['new_hash']!r} does not "
                f"match current source note hash {on_disk_hash!r}"
            )
    # All checks pass — apply the refresh atomically.
    row["note_hash"] = prose_fix["new_hash"]
    row["prose_status"] = prose_status
    row["prose_corrections"] = prose_fix["prose_corrections"]
    return None


def validate_prose_fields(audit: dict) -> str | None:
    """Validate optional prose_status / prose_corrections on an incoming audit.

    Both fields are optional. If present, prose_status must be in
    ALLOWED_PROSE_STATUS and prose_corrections must be a list of dicts.
    """
    if "prose_status" in audit:
        ps = audit["prose_status"]
        if ps not in ALLOWED_PROSE_STATUS:
            return f"prose_status {ps!r} not in {sorted(ALLOWED_PROSE_STATUS)}"
    if "prose_corrections" in audit:
        pc = audit["prose_corrections"]
        if not isinstance(pc, list):
            return "prose_corrections must be a list of {rule_id, before, after} dicts"
    return None


def validate_auditor_provenance(audit: dict) -> str | None:
    """Validate model and reasoning-effort provenance on an incoming audit."""
    auditor_model = audit.get("auditor_model")
    if not isinstance(auditor_model, str) or not auditor_model.strip():
        return "auditor_model must be a non-empty string (e.g. 'gpt-5.6-sol')"
    auditor_reasoning = audit.get("auditor_reasoning_effort")
    if not isinstance(auditor_reasoning, str) or not auditor_reasoning.strip():
        return "auditor_reasoning_effort must be a non-empty string (e.g. 'xhigh')"
    declared_family = audit.get("auditor_family")
    is_codex = auditor_model.startswith("gpt-") or (
        isinstance(declared_family, str) and declared_family.startswith("codex-gpt-")
    )
    if is_codex and auditor_reasoning != REQUIRED_REASONING_EFFORT:
        return (
            f"auditor_reasoning_effort={auditor_reasoning!r} must equal "
            f"{REQUIRED_REASONING_EFFORT!r}: the audit lane only accepts "
            f"verdicts produced at {REQUIRED_REASONING_EFFORT} reasoning "
            "effort. Re-run the audit with the correct setting."
        )
    if auditor_model.startswith("gpt-"):
        if not _SUPPORTED_CODEX_MODEL_RE.fullmatch(auditor_model):
            return (
                f"auditor_model={auditor_model!r} is not an accepted full GPT "
                "audit-model slug; expected a numeric GPT model with optional "
                "'-sol' serving suffix."
            )
        expected = _canonical_codex_family_for_model(auditor_model)
        if declared_family != expected:
            return (
                f"auditor_family={declared_family!r} does not match "
                f"auditor_model={auditor_model!r}: expected family "
                f"{expected!r}. Either fix the family label or fix the "
                "model field; they must agree."
            )
    elif isinstance(declared_family, str) and declared_family.startswith("codex-gpt-"):
        return (
            f"auditor_family={declared_family!r} requires a supported GPT "
            f"auditor_model, got {auditor_model!r}."
        )
    return None


def apply_judicial_review(ledger: dict, judgment: dict) -> tuple[bool, str]:
    missing = JUDICIAL_REQUIRED_FIELDS - set(judgment)
    if missing:
        return False, f"missing required judicial fields: {sorted(missing)}"

    cid = judgment["claim_id"]
    rows = ledger.get("rows", {})
    if cid not in rows:
        return False, f"unknown claim_id: {cid!r}"
    # Work on a detached row copy. Rejected audits must not leak early
    # pre_audit_prose_fix or packet mutations into the live ledger. Paths that
    # intentionally record a disagreement explicitly assign this copy back.
    row = copy.deepcopy(rows[cid])
    invocation_id = resolved_audit_invocation_id(judgment)
    invocation_error = audit_invocation_error(judgment)
    if invocation_error:
        return False, invocation_error
    if audit_invocation_seen(row, invocation_id):
        return False, "audit_invocation_id has already been consumed for this claim"
    if judgment.get("independence") != "judicial_review":
        return False, "judicial third-auditor review requires independence='judicial_review'"
    provenance_error = validate_auditor_provenance(judgment)
    if provenance_error:
        return False, provenance_error
    side = judgment.get("sided_with")
    if side not in ALLOWED_JUDICIAL_SIDES:
        return False, f"sided_with {side!r} not in {sorted(ALLOWED_JUDICIAL_SIDES)}"
    if side == "neither":
        return False, (
            "judicial side='neither' is a panel-escalation outcome and cannot "
            "be applied; run a fresh five-judge panel with the prior votes"
        )
    ratified_verdict = judgment.get("ratified_verdict")
    if ratified_verdict not in ALLOWED_VERDICTS:
        return False, f"ratified_verdict {ratified_verdict!r} not in {sorted(ALLOWED_VERDICTS)}"
    ratified_claim_type = judgment.get("ratified_claim_type")
    if ratified_claim_type not in ALLOWED_CLAIM_TYPES:
        return False, f"ratified_claim_type {ratified_claim_type!r} not in {sorted(ALLOWED_CLAIM_TYPES)}"
    ratified_claim_scope = judgment.get("ratified_claim_scope")
    if not isinstance(ratified_claim_scope, str) or not ratified_claim_scope.strip():
        return False, "ratified_claim_scope must be a non-empty string"

    err = note_hash_drift_error(row)
    if err:
        return False, err

    cross_confirmation = row.get("cross_confirmation")
    if (
        not isinstance(cross_confirmation, dict)
        or cross_confirmation.get("status") not in JUDICIAL_REVIEWABLE_STATUSES
    ):
        return False, (
            "judicial review requires cross_confirmation.status in "
            f"{sorted(JUDICIAL_REVIEWABLE_STATUSES)}"
        )
    first = cross_confirmation.get("first_audit") or {}
    second = cross_confirmation.get("second_audit") or {}
    if not first or not second:
        return False, "judicial review requires first_audit and second_audit summaries"
    for label, summary in (("first_audit", first), ("second_audit", second)):
        tuple_error = legacy_tuple_upgrade_error(label, summary)
        if tuple_error:
            return False, tuple_error

    prior_auditors = {first.get("auditor"), second.get("auditor")}
    if judgment.get("third_auditor") in prior_auditors:
        return False, "judicial third auditor must differ from both prior auditors"

    chosen_claim_type = None
    chosen: dict = {}
    if side == "hybrid":
        if not judgment.get("hybrid_resolution_note"):
            return False, "hybrid judicial review requires hybrid_resolution_note"
        ratified_scope = ratified_claim_scope
    if side in {"first", "second"}:
        chosen = first if side == "first" else second
        chosen_label = "first" if side == "first" else "second"
        if ratified_verdict != chosen.get("verdict"):
            return False, (
                f"ratified_verdict {ratified_verdict!r} does not match "
                f"{chosen_label}_audit verdict {chosen.get('verdict')!r}"
            )
        chosen_claim_type = chosen.get("claim_type")
        if (
            ratified_claim_type is not None
            and chosen_claim_type is not None
            and ratified_claim_type != chosen_claim_type
        ):
            return False, (
                f"ratified_claim_type {ratified_claim_type!r} does not match "
                f"{chosen_label}_audit claim_type {chosen_claim_type!r}"
            )
        if (
            normalized_negative_assertion_classes(judgment)
            != normalized_negative_assertion_classes(chosen)
        ):
            return False, (
                "negative_assertion_classes does not match the ratified "
                f"{chosen_label}_audit declaration"
            )
        if (
            judgment.get("ratified_load_bearing_step_class")
            != chosen.get("load_bearing_step_class")
        ):
            return False, (
                "ratified_load_bearing_step_class does not match the ratified "
                f"{chosen_label}_audit class"
            )
        if (
            normalized_claim_scope({"claim_scope": ratified_claim_scope})
            != normalized_claim_scope(chosen)
        ):
            return False, (
                "ratified_claim_scope does not match the ratified "
                f"{chosen_label}_audit scope; use sided_with='hybrid' to "
                "ratify a different scope"
            )
    ratified_decoration_parent = (
        judgment.get("ratified_decoration_parent_claim_id")
        or judgment.get("decoration_parent_claim_id")
    )
    if ratified_verdict == "audited_decoration" and not ratified_decoration_parent:
        return False, "judicial audited_decoration requires decoration_parent_claim_id"
    ratified_class = judgment.get("ratified_load_bearing_step_class")
    final_claim_type = ratified_claim_type or chosen_claim_type or row.get("claim_type")
    note_path = row.get("note_path") or ""
    note_body = ""
    if note_path:
        try:
            note_body = (REPO_ROOT / note_path).read_text(encoding="utf-8")
        except OSError:
            pass
    gate_blob = {
        "claim_type": final_claim_type,
        "verdict": ratified_verdict,
        "claim_scope": (
            judgment.get("ratified_claim_scope")
            or chosen.get("claim_scope")
            or row.get("claim_scope")
        ),
        "chain_closes": ratified_verdict == "audited_clean",
        "load_bearing_step": judgment.get("ratified_load_bearing_step"),
        "chain_closure_explanation": judgment.get("judgment_rationale"),
        "verdict_rationale": judgment.get("judgment_rationale"),
        "notes_for_re_audit_if_any": judgment.get("notes_for_re_audit_if_any"),
        "no_go_discipline": judgment.get("no_go_discipline"),
        "negative_assertion_classes": judgment.get("negative_assertion_classes"),
    }
    try:
        evidence_manifest = trusted_evidence_manifest(cid, invocation_id)
    except ValueError as exc:
        return False, str(exc)
    trusted_transport = evidence_manifest is not None
    source_required_probe = no_go_discipline_gate.source_requires_no_go_discipline(
        note_path, note_body, final_claim_type
    )
    forensic_probe = bool(
        forensic_tier_for(final_claim_type, source_required_probe)
        or (row.get("claim_type") or "") == "no_go"
    )
    if (
        evidence_manifest is None
        and forensic_probe
    ):
        if judgment.get("no_go_discipline") is None:
            preliminary_error = no_go_discipline_gate.validate_no_go_discipline(
                gate_blob,
                source_required=source_required_probe,
                structural_only=True,
                require_declaration=True,
            )
            if preliminary_error:
                return False, preliminary_error
        return False, "No-Go Discipline apply requires trusted orchestrator evidence transport"
    if evidence_manifest is None:
        evidence_manifest = no_go_discipline_gate.build_evidence_manifest(
            row, rows, REPO_ROOT
        )
    if ratified_verdict == "audited_clean":
        clipped_error = clipped_clean_evidence_error(evidence_manifest)
        if clipped_error:
            return False, clipped_error
    if trusted_transport:
        manifest_error = trusted_manifest_current_error(
            judgment.get("no_go_discipline") or {},
            evidence_manifest,
            row,
            rows,
            dynamic_index_drift_invalidates=forensic_probe,
        )
        if manifest_error:
            return False, f"trusted evidence manifest is stale: {manifest_error}"
    source_requires_no_go = no_go_discipline_gate.source_requires_no_go_discipline(
        note_path,
        note_body,
        (
            ""
            if no_go_discipline_gate.manifest_has_blind_reaudit_control(
                evidence_manifest
            )
            else final_claim_type
        ),
    )
    _forensic = bool(
        forensic_tier_for(final_claim_type, source_requires_no_go)
        or (row.get("claim_type") or "") == "no_go"
    )
    if side in {"first", "second"}:
        chosen_gate_error = cross_summary_no_go_error(
            chosen,
            source_required=source_requires_no_go,
            current_evidence_manifest=evidence_manifest if _forensic else None,
        )
        if chosen_gate_error:
            return False, (
                f"judicial review cannot ratify invalid {side} audit: "
                f"{chosen_gate_error}"
            )
    no_go_error = no_go_discipline_gate.validate_no_go_discipline(
        gate_blob,
        source_required=source_requires_no_go,
        evidence_manifest=evidence_manifest if _forensic else None,
        prior_claim_scope=prior_claim_scope_for_row(row),
        structural_only=not _forensic,
        require_declaration=True,
    )
    if no_go_error:
        return False, no_go_error
    if isinstance(judgment.get("no_go_discipline"), dict) and _forensic:
        packet = dict(judgment["no_go_discipline"])
        packet.pop("evidence_snapshot", None)
        packet["evidence_snapshot"] = no_go_discipline_gate.build_evidence_snapshot(
            packet, evidence_manifest
        )
        judgment["no_go_discipline"] = packet

    # All fallible checks above are transactional: only now may the judicial
    # record mutate the live row.
    third = judicial_summary_from_blob(judgment)
    tuple_error = legacy_tuple_upgrade_error("third_audit", third)
    if tuple_error:
        return False, tuple_error
    row["cross_confirmation"]["third_audit"] = third
    row["cross_confirmation"]["mode"] = "judicial_third_pass"

    row["cross_confirmation"]["status"] = {
        "first": "third_confirmed_first",
        "second": "third_confirmed_second",
        "hybrid": "third_confirmed_hybrid",
    }[side]
    row["cross_confirmation"]["agreement_schema"] = AUDIT_TUPLE_AGREEMENT_SCHEMA
    row["audit_status"] = ratified_verdict
    row["auditor"] = judgment["third_auditor"]
    row["auditor_family"] = judgment["auditor_family"]
    row["auditor_model"] = judgment["auditor_model"]
    row["auditor_reasoning_effort"] = judgment["auditor_reasoning_effort"]
    row["independence"] = judgment["independence"]
    row["audit_date"] = third["audit_date"]
    row["claim_type"] = final_claim_type
    row["claim_scope"] = judgment.get("ratified_claim_scope") or chosen.get("claim_scope") or row.get("claim_scope")
    row["claim_type_provenance"] = "judicial_review"
    row["claim_type_last_reviewed"] = row["audit_date"]
    row["load_bearing_step"] = judgment.get("ratified_load_bearing_step") or row.get("load_bearing_step")
    row["load_bearing_step_class"] = ratified_class
    row["chain_closes"] = ratified_verdict == "audited_clean"
    row["chain_closure_explanation"] = judgment.get("judgment_rationale")
    row["verdict_rationale"] = judgment.get("judgment_rationale")
    if "notes_for_re_audit_if_any" in judgment:
        row["notes_for_re_audit_if_any"] = judgment.get("notes_for_re_audit_if_any")
    if "runner_check_breakdown" in judgment:
        row["runner_check_breakdown"] = judgment["runner_check_breakdown"]
    if "open_dependency_paths" in judgment:
        row["open_dependency_paths"] = judgment.get("open_dependency_paths") or []
    if ratified_verdict == "audited_clean":
        row["open_dependency_paths"] = []
        row["decoration_parent_claim_id"] = None
    elif ratified_verdict == "audited_decoration":
        row["decoration_parent_claim_id"] = ratified_decoration_parent
    else:
        row["decoration_parent_claim_id"] = judgment.get("decoration_parent_claim_id")
    row["auditor_confidence"] = judgment.get("auditor_confidence", "judicial")
    row["negative_assertion_classes"] = list(
        normalized_negative_assertion_classes(
            chosen if side in {"first", "second"} else judgment
        )
    )
    if judgment.get("no_go_discipline") is None:
        row.pop("no_go_discipline", None)
    else:
        row["no_go_discipline"] = judgment.get("no_go_discipline")
    row["blocker"] = None
    row["audit_state_snapshot"] = snapshot_audit_state(row, rows)
    consume_audit_invocation(row, invocation_id)
    rows[cid] = row
    ledger["rows"] = rows
    return True, f"judicial third auditor confirmed {side} verdict"


def apply_one(ledger: dict, audit: dict) -> tuple[bool, str]:
    audit = dict(audit)
    if "_no_go_evidence_manifest" in audit:
        return False, "_no_go_evidence_manifest is reserved for the orchestrator transport"
    if "sided_with" in audit or "third_auditor" in audit:
        return apply_judicial_review(ledger, audit)

    missing = REQUIRED_FIELDS - set(audit)
    if missing:
        return False, f"missing required fields: {sorted(missing)}"

    cid = audit["claim_id"]
    rows = ledger.get("rows", {})
    if cid not in rows:
        return False, f"unknown claim_id: {cid!r}"

    # Keep all pre-verdict mutations transactional. Only explicit accepted or
    # disagreement-recording paths assign this detached copy back to rows.
    row = copy.deepcopy(rows[cid])
    invocation_id = resolved_audit_invocation_id(audit)
    invocation_error = audit_invocation_error(audit)
    if invocation_error:
        return False, invocation_error
    if audit_invocation_seen(row, invocation_id):
        return False, "audit_invocation_id has already been consumed for this claim"
    prior_cross_confirmation = row.get("cross_confirmation")
    prior_cross_confirmation_status = (
        prior_cross_confirmation.get("status")
        if isinstance(prior_cross_confirmation, dict)
        else prior_cross_confirmation
    )
    if prior_cross_confirmation_status == "disagreement":
        return False, (
            "cross-confirmation disagreement cannot be resolved by an ordinary "
            "single-auditor pass; run the governed five-judge judicial panel"
        )

    def accept_row() -> None:
        """Commit the detached row and consume this invocation exactly once."""
        consume_audit_invocation(row, invocation_id)
        rows[cid] = row
        ledger["rows"] = rows

    verdict = audit["verdict"]
    if verdict not in ALLOWED_VERDICTS:
        return False, f"verdict {verdict!r} not in {sorted(ALLOWED_VERDICTS)}"

    claim_type = audit.get("claim_type")
    if claim_type not in ALLOWED_CLAIM_TYPES:
        return False, f"claim_type {claim_type!r} not in {sorted(ALLOWED_CLAIM_TYPES)}"
    claim_scope = audit.get("claim_scope")
    if not isinstance(claim_scope, str) or not claim_scope.strip():
        return False, "claim_scope must be a non-empty string"

    note_path = row.get("note_path") or ""
    note_body = ""
    if note_path:
        try:
            note_body = (REPO_ROOT / note_path).read_text(encoding="utf-8")
        except OSError:
            pass
    try:
        evidence_manifest = trusted_evidence_manifest(cid, invocation_id)
    except ValueError as exc:
        return False, str(exc)
    trusted_transport = evidence_manifest is not None
    _source_req_probe = no_go_discipline_gate.source_requires_no_go_discipline(
        note_path, note_body, claim_type
    )
    _forensic = bool(
        forensic_tier_for(claim_type, _source_req_probe)
        or (row.get("claim_type") or "") == "no_go"
    )
    if (
        evidence_manifest is None
        and _forensic
    ):
        if audit.get("no_go_discipline") is None:
            preliminary_error = no_go_discipline_gate.validate_no_go_discipline(
                audit,
                source_required=_source_req_probe,
                structural_only=True,
                require_declaration=True,
            )
            if preliminary_error:
                return False, preliminary_error
        return False, "No-Go Discipline apply requires trusted orchestrator evidence transport"
    if evidence_manifest is None:
        evidence_manifest = no_go_discipline_gate.build_evidence_manifest(
            row, rows, REPO_ROOT
        )
    if verdict == "audited_clean":
        clipped_error = clipped_clean_evidence_error(evidence_manifest)
        if clipped_error:
            return False, clipped_error
    if trusted_transport:
        manifest_error = trusted_manifest_current_error(
            audit.get("no_go_discipline") or {},
            evidence_manifest,
            row,
            rows,
            dynamic_index_drift_invalidates=_forensic,
        )
        if manifest_error:
            return False, f"trusted evidence manifest is stale: {manifest_error}"
    source_requires_no_go = (
        no_go_discipline_gate.source_requires_no_go_discipline(
            note_path,
            note_body,
            (
                ""
                if no_go_discipline_gate.manifest_has_blind_reaudit_control(
                    evidence_manifest
                )
                else claim_type
            ),
        )
    )
    _forensic = bool(
        forensic_tier_for(claim_type, source_requires_no_go)
        or (row.get("claim_type") or "") == "no_go"
    )
    no_go_error = no_go_discipline_gate.validate_no_go_discipline(
        audit,
        source_required=source_requires_no_go,
        evidence_manifest=evidence_manifest if _forensic else None,
        prior_claim_scope=prior_claim_scope_for_row(row),
        structural_only=not _forensic,
        require_declaration=True,
    )
    if no_go_error:
        return False, no_go_error
    if isinstance(audit.get("no_go_discipline"), dict) and _forensic:
        packet = dict(audit["no_go_discipline"])
        packet.pop("evidence_snapshot", None)
        packet["evidence_snapshot"] = no_go_discipline_gate.build_evidence_snapshot(
            packet, evidence_manifest
        )
        audit["no_go_discipline"] = packet

    if verdict == "audited_clean" and claim_type in {"decoration", "meta"}:
        return False, f"audited_clean cannot ratify claim_type={claim_type!r}"
    if verdict == "audited_decoration":
        if claim_type != "decoration":
            return False, "audited_decoration requires claim_type='decoration'"
        if not audit.get("decoration_parent_claim_id"):
            return False, "audited_decoration requires decoration_parent_claim_id"

    independence = audit["independence"]
    if independence not in ALLOWED_INDEPENDENCE:
        return False, f"independence {independence!r} not in {sorted(ALLOWED_INDEPENDENCE)}"

    provenance_error = validate_auditor_provenance(audit)
    if provenance_error:
        return False, provenance_error

    # Validate optional prose_status / prose_corrections fields on the blob.
    # Both are orthogonal to the physics verdict; vocabulary drift never
    # demotes audit_status. See docs/repo/VOCABULARY_HYGIENE_DESIGN.md.
    prose_error = validate_prose_fields(audit)
    if prose_error:
        return False, prose_error

    # Model-floor check: incoming Codex audits must come from a codex-gpt-*
    # family at or above MIN_NEW_AUDIT_FAMILY_RANK, or a non-codex family
    # (claude-*, legacy-confirmed-clean, judicial reviews, etc.). Existing
    # sub-floor rows are left for the re-audit queue; this rejects only newly
    # applied audit blobs.
    if not _family_meets_floor(audit["auditor_family"]):
        floor_str = ".".join(str(x) for x in MIN_NEW_AUDIT_FAMILY_RANK)
        return False, (
            f"auditor_family {audit['auditor_family']!r} is below the "
            f"incoming-audit codex-gpt-{floor_str}+ floor. Codex audit blobs "
            f"must be produced by codex-gpt-{floor_str} or newer; non-codex "
            f"families remain allowed for human / judicial reviews."
        )

    criticality = row.get("criticality") or "leaf"
    if verdict == "audited_clean":
        err = clean_independence_error(independence, criticality)
        if err:
            return False, err

    # If the audit chain ran vocab_lint --fix on the source note before
    # applying the verdict, the note's content (and therefore note_hash)
    # changed. The pre_audit_prose_fix envelope atomically refreshes
    # note_hash + writes prose_status / prose_corrections so the
    # downstream note_hash_drift_error check passes.
    prose_fix = audit.get("pre_audit_prose_fix")
    prose_fix_applied = False
    if prose_fix is not None:
        err = apply_pre_audit_prose_fix(row, prose_fix)
        if err:
            return False, err
        prose_fix_applied = True

    # Hash drift check.
    err = note_hash_drift_error(row)
    if err:
        return False, err

    terminal_second_pass_msg: str | None = None
    terminal_second_pass_error: str | None = None
    terminal_second_pass_blocker: str | None = None
    legacy_claim_type_reaudit = legacy_confirmed_clean_claim_type_reaudit(
        row, verdict, prior_cross_confirmation_status
    )
    legacy_verdict_reaudit = legacy_confirmed_clean_verdict_reaudit(
        row, verdict, prior_cross_confirmation_status
    )
    if legacy_verdict_reaudit:
        if criticality in {"critical", "high"} and independence == "weak":
            return False, "legacy clean verdict re-audit requires independence != 'weak'"

        first = legacy_clean_consensus_summary(row, audit, prior_cross_confirmation_status)
        second = audit_summary_from_blob(audit)
        row["cross_confirmation"] = {
            "first_audit": first,
            "second_audit": second,
            "status": "disagreement",
            "mode": "legacy_confirmed_clean_verdict_reaudit",
        }
        row["audit_status"] = "audit_in_progress"
        row["blocker"] = "cross_confirmation_disagreement"
        row["claim_type"] = claim_type
        row["claim_scope"] = claim_scope.strip()
        row["claim_type_provenance"] = "audited_pending_cross_confirmation"
        row["claim_type_last_reviewed"] = audit.get("audit_date") or datetime.now(timezone.utc).isoformat()
        accept_row()
        return True, (
            "legacy clean re-audit disagreement recorded "
            f"('audited_clean'/{first.get('claim_type')!r}/"
            f"{first.get('load_bearing_step_class')!r} vs "
            f"{second.get('verdict')!r}/{second.get('claim_type')!r}/"
            f"{second.get('load_bearing_step_class')!r}); "
            "promote to the governed five-judge judicial panel"
        )

    first_terminal_verdict = row.get("audit_status")
    explicit_second_seat = audit.get("cross_confirmation_role") == "second_seat"
    if explicit_second_seat:
        if first_terminal_verdict not in ALLOWED_VERDICTS:
            return False, (
                "explicit second-seat cross-confirmation requires an existing "
                f"terminal verdict, got {first_terminal_verdict!r}"
            )
        if prior_cross_confirmation_status not in {None, "none"}:
            return False, (
                "explicit second-seat cross-confirmation requires no existing "
                f"cross-confirmation status, got {prior_cross_confirmation_status!r}"
            )
        first = audit_summary_from_row(row)
        first_gate_error = cross_summary_no_go_error(
            first,
            source_required=source_requires_no_go,
            current_evidence_manifest=evidence_manifest,
        )
        if first_gate_error:
            return False, (
                "explicit second-seat cross-confirmation cannot ratify an invalid "
                f"first audit: {first_gate_error}"
            )
        err = cross_confirmation_error(first, audit)
        if err:
            return False, err
        if independence == "weak":
            return False, "explicit second-seat cross-confirmation requires independence != 'weak'"

        second = audit_summary_from_blob(audit)
        for label, summary in (("first_audit", first), ("second_audit", second)):
            tuple_error = legacy_tuple_upgrade_error(label, summary)
            if tuple_error:
                return False, tuple_error
        matches = audit_tuples_match(first, second)
        row["cross_confirmation"] = {
            "first_audit": first,
            "second_audit": second,
            "status": "confirmed" if matches else "disagreement",
            "mode": "explicit_second_seat",
        }
        if matches:
            row["cross_confirmation"]["agreement_schema"] = AUDIT_TUPLE_AGREEMENT_SCHEMA
        if not matches:
            row["audit_status"] = "audit_in_progress"
            row["blocker"] = "cross_confirmation_disagreement"
            accept_row()
            return True, (
                "explicit second-seat cross-confirmation disagreement recorded "
                f"({first.get('verdict')!r}/{first.get('claim_type')!r}/"
                f"{first.get('load_bearing_step_class')!r} vs "
                f"{second.get('verdict')!r}/{second.get('claim_type')!r}/"
                f"{second.get('load_bearing_step_class')!r}); "
                "promote to the governed five-judge judicial panel"
            )
        accept_row()
        return True, "explicit second-seat cross-confirmation recorded"

    terminal_second_pass = (
        first_terminal_verdict in TERMINAL_CROSS_CONFIRM_VERDICTS
        and criticality in {"critical", "high"}
        and prior_cross_confirmation_status in {None, "none"}
    )
    if terminal_second_pass:
        first = audit_summary_from_row(row)
        first_gate_error = cross_summary_no_go_error(
            first,
            source_required=source_requires_no_go,
            current_evidence_manifest=evidence_manifest,
        )
        if first_gate_error:
            return False, (
                "terminal cross-confirmation cannot ratify an invalid first audit: "
                f"{first_gate_error}"
            )
        err = cross_confirmation_error(first, audit)
        if err:
            return False, err
        if independence == "weak":
            return False, "terminal cross-confirmation requires independence != 'weak'"

        second = audit_summary_from_blob(audit)
        for label, summary in (("first_audit", first), ("second_audit", second)):
            tuple_error = legacy_tuple_upgrade_error(label, summary)
            if tuple_error:
                return False, tuple_error
        matches = audit_tuples_match(first, second)
        row["cross_confirmation"] = {
            "first_audit": first,
            "second_audit": second,
            "status": "confirmed" if matches else "disagreement",
            "mode": "terminal_second_pass",
        }
        if matches:
            row["cross_confirmation"]["agreement_schema"] = AUDIT_TUPLE_AGREEMENT_SCHEMA
            terminal_second_pass_msg = "terminal verdict cross-confirmed"
        else:
            terminal_second_pass_msg = (
                "first and second audits disagree "
                f"({first.get('verdict')!r}/{first.get('claim_type')!r}/"
                f"{first.get('load_bearing_step_class')!r} vs "
                f"{second.get('verdict')!r}/{second.get('claim_type')!r}/"
                f"{second.get('load_bearing_step_class')!r}); "
                "promote to the governed judicial/panel review path"
            )
            terminal_second_pass_blocker = "cross_confirmation_disagreement"
            row["audit_status"] = "audit_in_progress"
            row["blocker"] = terminal_second_pass_blocker
            accept_row()
            return True, terminal_second_pass_msg

    critical_second_pass = (
        criticality == "critical"
        and prior_cross_confirmation_status == "awaiting_second"
    )
    if critical_second_pass:
        first = (prior_cross_confirmation or {}).get("first_audit") or {}
        tuple_error = legacy_tuple_upgrade_error("first_audit", first)
        if tuple_error:
            return False, tuple_error
        first_gate_error = cross_summary_no_go_error(
            first,
            source_required=source_requires_no_go,
            current_evidence_manifest=evidence_manifest,
        )
        if first_gate_error:
            archive_invalid_first_and_require_fresh_packet(row, first)
            accept_row()
            return True, (
                "legacy packetless/invalid first audit archived; incoming packet "
                "not applied because cross-confirmation must restart from a fresh first seat"
            )
        err = cross_confirmation_error(first, audit)
        if err:
            return False, err

        second = audit_summary_from_blob(audit)
        tuple_error = legacy_tuple_upgrade_error("second_audit", second)
        if tuple_error:
            return False, tuple_error
        row["cross_confirmation"]["second_audit"] = second
        matches = audit_tuples_match(first, second)
        if matches:
            row["cross_confirmation"]["status"] = "confirmed"
            row["cross_confirmation"]["agreement_schema"] = AUDIT_TUPLE_AGREEMENT_SCHEMA
        else:
            row["cross_confirmation"]["status"] = "disagreement"
            row["audit_status"] = "audit_in_progress"
            row["blocker"] = "cross_confirmation_disagreement"
            accept_row()
            return True, (
                "cross-confirmation disagreement recorded "
                f"({first.get('verdict')!r}/{first.get('claim_type')!r}/"
                f"{first.get('load_bearing_step_class')!r} vs "
                f"{second.get('verdict')!r}/{second.get('claim_type')!r}/"
                f"{second.get('load_bearing_step_class')!r}); "
                "promote to the governed five-judge judicial panel"
            )

    # Cross-confirmation flow for critical claims.
    # First audit on a critical claim with audited_clean lands as
    # audit_in_progress and waits for a second independent auditor.
    # Second matching audit promotes to audited_clean.
    if (
        verdict == "audited_clean"
        and criticality == "critical"
        and not critical_second_pass
        and not legacy_claim_type_reaudit
    ):
        prior = row.get("cross_confirmation") or {}
        first = prior.get("first_audit")
        if first is None:
            first_summary = audit_summary_from_blob(audit)
            tuple_error = legacy_tuple_upgrade_error("first_audit", first_summary)
            if tuple_error:
                return False, tuple_error
            row["cross_confirmation"] = {
                "first_audit": first_summary,
                "second_audit": None,
                "status": "awaiting_second",
            }
            row["audit_status"] = "audit_in_progress"
            row["blocker"] = "awaiting_cross_confirmation"
            row["claim_type"] = claim_type
            row["claim_scope"] = claim_scope.strip()
            row["claim_type_provenance"] = "audited_pending_cross_confirmation"
            row["claim_type_last_reviewed"] = audit.get("audit_date") or datetime.now(timezone.utc).isoformat()
            accept_row()
            return True, "first audit recorded; awaiting independent second auditor"
        tuple_error = legacy_tuple_upgrade_error("first_audit", first)
        if tuple_error:
            return False, tuple_error
        first_gate_error = cross_summary_no_go_error(
            first,
            source_required=source_requires_no_go,
            current_evidence_manifest=evidence_manifest,
        )
        if first_gate_error:
            archive_invalid_first_and_require_fresh_packet(row, first)
            accept_row()
            return True, (
                "legacy packetless/invalid first audit archived; incoming packet "
                "not applied because N8 must be rebuilt against the updated history"
            )
        # We have a first audit on file; this is the second.
        err = cross_confirmation_error(first, audit)
        if err:
            return False, err
        second = audit_summary_from_blob(audit)
        tuple_error = legacy_tuple_upgrade_error("second_audit", second)
        if tuple_error:
            return False, tuple_error
        if not audit_tuples_match(first, second):
            row["cross_confirmation"]["second_audit"] = second
            row["cross_confirmation"]["status"] = "disagreement"
            row["audit_status"] = "audit_in_progress"
            row["blocker"] = "cross_confirmation_disagreement"
            accept_row()
            return True, (
                "first and second audits disagree on claim_type, "
                "claim_scope, load_bearing_step_class, or "
                "negative_assertion_classes "
                f"({first.get('claim_type')!r}/{first.get('load_bearing_step_class')!r} vs "
                f"{claim_type!r}/{audit.get('load_bearing_step_class')!r}); "
                "promote to the governed five-judge judicial panel"
            )
        # Concordant second audit: promote.
        row["cross_confirmation"]["second_audit"] = audit_summary_from_blob(audit)
        row["cross_confirmation"]["status"] = "confirmed"
        row["cross_confirmation"]["agreement_schema"] = AUDIT_TUPLE_AGREEMENT_SCHEMA

    # Apply the audit fields.
    row["audit_status"] = verdict
    row["auditor"] = audit["auditor"]
    row["auditor_family"] = audit["auditor_family"]
    row["auditor_model"] = audit["auditor_model"]
    row["auditor_reasoning_effort"] = audit["auditor_reasoning_effort"]
    row["independence"] = independence
    row["audit_date"] = audit.get("audit_date") or datetime.now(timezone.utc).isoformat()
    row["claim_type"] = claim_type
    row["claim_scope"] = claim_scope.strip()
    row["claim_type_provenance"] = "audited"
    row["claim_type_last_reviewed"] = row["audit_date"]
    row["notes_for_re_audit_if_any"] = audit.get("notes_for_re_audit_if_any")
    row["load_bearing_step"] = audit.get("load_bearing_step")
    row["load_bearing_step_class"] = audit.get("load_bearing_step_class")
    row["chain_closes"] = audit.get("chain_closes")
    row["chain_closure_explanation"] = audit.get("chain_closure_explanation")
    row["verdict_rationale"] = audit.get("verdict_rationale")
    row["open_dependency_paths"] = audit.get("open_dependency_paths", [])
    row["decoration_parent_claim_id"] = audit.get("decoration_parent_claim_id")
    row["auditor_confidence"] = audit.get("auditor_confidence")
    row["negative_assertion_classes"] = list(
        normalized_negative_assertion_classes(audit)
    )
    if audit.get("no_go_discipline") is None:
        row.pop("no_go_discipline", None)
    else:
        row["no_go_discipline"] = audit.get("no_go_discipline")
    if "runner_check_breakdown" in audit:
        row["runner_check_breakdown"] = audit["runner_check_breakdown"]
    row["blocker"] = terminal_second_pass_blocker
    if legacy_claim_type_reaudit:
        row.setdefault("cross_confirmation", {})["claim_type_reaudit"] = audit_summary_from_blob(audit)
        row["cross_confirmation"]["mode"] = "legacy_confirmed_clean_claim_type_reaudit"

    # Write prose_status / prose_corrections if the blob carried them
    # directly (without the pre_audit_prose_fix envelope). Validated above
    # by validate_prose_fields. If the envelope was applied, those fields
    # are already on the row; do not overwrite.
    if not prose_fix_applied:
        if "prose_status" in audit:
            row["prose_status"] = audit["prose_status"]
        if "prose_corrections" in audit:
            row["prose_corrections"] = audit["prose_corrections"]

    # Snapshot the state at audit time so invalidate_stale_audits.py can
    # detect changes that warrant re-audit (dep added/removed, dep status
    # changed, criticality bumped).
    row["audit_state_snapshot"] = snapshot_audit_state(row, rows)
    accept_row()
    if terminal_second_pass_error:
        return False, terminal_second_pass_error
    if terminal_second_pass_msg:
        return True, terminal_second_pass_msg
    return True, "applied"


PROPAGATION_STEPS = (
    # Steps that depend only on the ledger's audit verdicts. We skip the
    # graph rebuild (notes weren't edited) but recompute everything an
    # audit-verdict change could shift downstream.
    ("compute_effective_status.py",        "post-apply effective_status pass"),
    ("invalidate_stale_audits.py",         "invalidate audits whose deps shifted"),
    ("compute_effective_status.py",        "post-invalidation effective_status pass"),
    ("compute_lane_certification.py",      "refresh rolling lane certification"),
    ("compute_audit_queue.py",             "refresh audit queue"),
    ("compute_reaudit_candidates.py",      "refresh re-audit candidates"),
    ("render_audit_ledger.py",             "render AUDIT_LEDGER.md"),
    ("render_publication_effective_status.py", "render publication effective-status views"),
)


def run_propagation() -> int:
    """Run the propagation slice of the pipeline. Each step is a separate
    subprocess so a failure in one doesn't corrupt the others' state.
    """
    import subprocess

    scripts_dir = Path(__file__).resolve().parent
    print()
    print("Propagating audit verdicts through downstream pipeline steps...")
    for script, desc in PROPAGATION_STEPS:
        script_path = scripts_dir / script
        if not script_path.exists():
            print(f"  [skip] {script} not found")
            continue
        print(f"  -> {script:42s} ({desc})")
        result = subprocess.run(
            [sys.executable, str(script_path)],
            cwd=REPO_ROOT, capture_output=True, text=True,
        )
        if result.returncode != 0:
            print(f"     FAIL exit={result.returncode}", file=sys.stderr)
            if result.stderr:
                print(f"     stderr: {result.stderr.strip()[:400]}", file=sys.stderr)
            return 1
        if script == "invalidate_stale_audits.py":
            converged = False
            for attempt in range(1, 11):
                invalidated = len(
                    json.loads(LEDGER_PATH.read_text(encoding="utf-8")).get(
                        "last_invalidations", []
                    )
                )
                restore = subprocess.run(
                    [
                        sys.executable,
                        str(scripts_dir / "restore_overaggressively_invalidated_audits.py"),
                    ],
                    cwd=REPO_ROOT,
                    capture_output=True,
                    text=True,
                )
                if restore.returncode != 0:
                    print(
                        "     FAIL restore_overaggressively_invalidated_audits.py",
                        file=sys.stderr,
                    )
                    return 1
                restored_match = re.search(
                    r"^Restored (\d+) audits",
                    restore.stdout or "",
                    re.MULTILINE,
                )
                restored = int(restored_match.group(1)) if restored_match else 0
                if invalidated == 0 and restored == 0:
                    converged = True
                    break
                print(
                    f"     fixed-point pass {attempt}: {invalidated} invalidation(s), "
                    f"{restored} restoration(s); recomputing effective status"
                )
                compute = subprocess.run(
                    [sys.executable, str(scripts_dir / "compute_effective_status.py")],
                    cwd=REPO_ROOT, capture_output=True, text=True,
                )
                if compute.returncode != 0:
                    print("     FAIL compute_effective_status.py", file=sys.stderr)
                    return 1
                repeat = subprocess.run(
                    [sys.executable, str(script_path)],
                    cwd=REPO_ROOT, capture_output=True, text=True,
                )
                if repeat.returncode != 0:
                    print("     FAIL invalidate_stale_audits.py", file=sys.stderr)
                    return 1
            if not converged:
                print(
                    "     FAIL invalidation/restoration did not reach a fixed point "
                    "after 10 passes",
                    file=sys.stderr,
                )
                return 1
    print(f"Propagation: {len(PROPAGATION_STEPS)} steps OK")
    return 0


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--file", help="Path to a single audit JSON file.")
    p.add_argument("--batch", help="Directory of audit JSON files (one per claim).")
    p.add_argument(
        "--no-propagate",
        action="store_true",
        help="Skip the post-write propagation pipeline. Use when applying many "
             "audits in sequence (call run_pipeline.sh manually after the batch).",
    )
    args = p.parse_args()

    ledger_io.ensure_cache()
    if not LEDGER_PATH.exists():
        print(f"FAIL: ledger missing at {LEDGER_PATH}", file=sys.stderr)
        return 1

    ledger = json.loads(LEDGER_PATH.read_text(encoding="utf-8"))

    audits: list[dict] = []
    if args.file:
        audits.append(json.loads(Path(args.file).read_text(encoding="utf-8")))
    elif args.batch:
        for path in sorted(Path(args.batch).glob("*.json")):
            audits.append(json.loads(path.read_text(encoding="utf-8")))
    else:
        data = sys.stdin.read().strip()
        if not data:
            print("FAIL: no input on stdin and no --file/--batch given", file=sys.stderr)
            return 2
        parsed = json.loads(data)
        if isinstance(parsed, list):
            audits.extend(parsed)
        else:
            audits.append(parsed)

    applied = 0
    for a in audits:
        ok, msg = apply_one(ledger, a)
        cid = a.get("claim_id", "<unknown>")
        if ok:
            applied += 1
            print(f"OK  {cid}: {msg}")
        else:
            print(f"FAIL {cid}: {msg}", file=sys.stderr)

    ledger_io.save_ledger(ledger)
    print(f"Applied {applied}/{len(audits)} audit(s) to {LEDGER_PATH.relative_to(REPO_ROOT)}")

    propagation_rc = 0
    if applied > 0 and not args.no_propagate:
        propagation_rc = run_propagation()

    if propagation_rc != 0:
        return 4
    return 0 if applied == len(audits) else 3


if __name__ == "__main__":
    raise SystemExit(main())
