#!/usr/bin/env python3
"""Restoration of audits over-aggressively invalidated by a since-refined
policy. Originally the one-shot PR #907 pass for `criticality_increased`;
now also the standing recovery lane for `no_go_discipline_packet_missing`
archives whose gating was narrowed by the trigger-precision repair, and
for `dep_weakened` archives whose dependency has recovered. Idempotent;
safe to run on every pipeline pass.

Restored categories:

  3. `no_go_discipline_packet_missing` invalidations whose archived audit
     is restorable under the CURRENT no-go trigger. The restoration guard
     re-runs the live source/output gate: retained clean/no-go authority that
     still requires a packet, or any archived packet that does not round-trip
     validation, stays invalidated for fresh audit. Development-tier non-clean
     repair verdicts follow their live optional-packet contract.

  4. `dep_weakened:dep_id:before->after` invalidations whose `dep_id`
     has already recovered on the live ledger — through a landed
     re-audit or an earlier restoration pass — to a tier at least as
     strong as the archived audit's recorded `before` tier, with every
     other still-live invalidation check clean. Chains recover one
     dependency hop per pass; the pipeline's joint invalidate/restore
     loop iterates passes to a fixed point within one run (ten-pass cap).

Original PR #907 categories, retained verbatim:

  1. `criticality_increased:before->after` invalidations where PR #907's
     `_categorize_criticality_bump` would have returned `noop` or
     `soft_reset`. Concretely:

       - `before -> medium` / `before -> leaf` are no-op (no new
         requirement). Restored back to the archived state.
       - `before -> high` is no-op when the archived audit had
         `independence != weak`. Restored.
       - `before -> critical` is no-op when cross-confirmation was
         already on file, OR soft-reset when the archived audit was
         `audited_clean` with non-weak independence and no
         cross-confirmation. Restored in both sub-cases; the next
         pipeline run will soft-reset where appropriate.

     Bumps where the audit fundamentally fails the new tier
     (`audited_clean` + `independence == weak` -> high/critical) are
     NOT restored — `_categorize_criticality_bump` would still return
     `invalidate`.

  2. `dep_weakened:dep_id:before->after` invalidations whose `dep_id` is
     in our category-1 restore set AND whose restored effective tier is
     at least as strong as the downstream audit's recorded `before`
     tier. This preserves downstream audits only when the dependency
     really returns to the state the downstream audit closed against.
     If the dependency restores to a still-weaker terminal verdict
     (for example `audited_numerical_match -> audited_conditional`),
     the downstream audit is left invalidated.

Other invalidation reasons (`note_hash` drift handled by
`seed_audit_ledger.py`, `runner_hash_changed`, `deps_changed`,
`dep_claim_type_changed`, `dep_claim_scope_changed`,
`runner_artifact_issue_resolved`) are NOT touched; those reflect real
state changes that genuinely invalidated the audit.

Every restoration category also requires the archived audit to satisfy
current audit-lane lint requirements (claim_type, claim_scope, repair
class prefix for audited_conditional rows, and current auditor-family
floor). Older archived audits that do not meet those requirements remain
invalidated for fresh audit.

Direct `criticality_increased:*` candidates are also checked for other
still-live invalidation reasons (dependency set drift, dependency status
weakening, dependency claim_type/scope drift). If any non-criticality
blocker would immediately re-fire, the audit remains invalidated.

Idempotent: only operates on currently-`unaudited` rows. Running twice
is a no-op on the second run.

Sequencing:

  This script now runs inside `run_pipeline.sh` step 7, interleaved with
  `invalidate_stale_audits.py` to a joint fixed point: invalidation
  settles the gate state, restoration recovers eligible archives, and
  `compute_effective_status.py` propagates between passes. Restoration
  can expose a masked lower-ranked dependency verdict; the next
  invalidation pass applies it with a fresh accurate reason, and the
  before-tier comparison prevents re-restoration, so the loop is
  monotone. Standalone invocation (with or without `--dry-run`) remains
  supported and idempotent.

  Historical PR #907 sequencing (one-shot): merge #907, run this script,
  then run the pipeline to propagate.

Usage:
  python3 docs/audit/scripts/restore_overaggressively_invalidated_audits.py [--dry-run] [--limit N]
"""
from __future__ import annotations

import argparse
import contextlib
import hashlib
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import no_go_discipline_gate

import ledger_io

REPO_ROOT = Path(__file__).resolve().parents[3]
DATA_DIR = REPO_ROOT / "docs" / "audit" / "data"
LEDGER_PATH = DATA_DIR / "audit_ledger.json"

# Mirror of `invalidate_stale_audits.ARCHIVED_FIELDS`. These are the
# audit-owned fields that `archive_and_reset` snapshots into
# previous_audits[-1] before zeroing the live row. Restoration copies
# them back. The two metadata fields `archived_at` and
# `invalidation_reason` are not restored — they describe the archive
# itself.
ARCHIVED_FIELDS = (
    "audit_status",
    "audit_date",
    "auditor",
    "auditor_family",
    "auditor_model",
    "auditor_reasoning_effort",
    "independence",
    "load_bearing_step",
    "load_bearing_step_class",
    "chain_closes",
    "chain_closure_explanation",
    "verdict_rationale",
    "open_dependency_paths",
    "decoration_parent_claim_id",
    "auditor_confidence",
    "runner_check_breakdown",
    "blocker",
    "audit_state_snapshot",
    "cross_confirmation",
    "claim_type",
    "claim_scope",
    "claim_type_provenance",
    "claim_type_last_reviewed",
    "notes_for_re_audit_if_any",
    "no_go_discipline",
    "negative_assertion_classes",
    "audit_invocation_id",
    "audit_invocation_history",
    "negative_assertion_classes",
)

RANK = {
    "retained": 100,
    "retained_no_go": 100,
    "retained_bounded": 95,
    "retained_pending_chain": 80,
    "open_gate": 40,
    "unaudited": 30,
    "audit_in_progress": 30,
    "meta": 25,
    "audited_decoration": 20,
    "audited_numerical_match": 15,
    "audited_renaming": 10,
    "audited_conditional": 10,
    "audited_failed": 0,
}

CLAIM_TYPE_TO_RETAINED = {
    "positive_theorem": "retained",
    "no_go": "retained_no_go",
    "bounded_theorem": "retained_bounded",
}

ALLOWED_CLAIM_TYPES = {
    "positive_theorem",
    "bounded_theorem",
    "no_go",
    "open_gate",
    "decoration",
    "meta",
}
ALLOWED_INDEPENDENCE = {"weak", "fresh_context", "cross_family", "strong", "external", "judicial_review", None}
ALLOWED_REPAIR_CLASSES = {
    "missing_dependency_edge",
    "dependency_not_retained",
    "missing_bridge_theorem",
    "scope_too_broad",
    "runner_artifact_issue",
    "compute_required",
    "other",
}
CANONICAL_AUDITOR_FAMILIES = {
    "codex-gpt-5",
    "codex-gpt-5.5",
    "codex-gpt-5.6",
    "codex-gpt-5.7",
    "codex-gpt-6",
    "claude-opus",
    "claude-sonnet",
    "human",
    "external",
    "legacy-confirmed-clean",
}
LEGACY_AUDITOR_FAMILIES = {
    "codex-current",
    "codex-fresh",
    "codex-fresh-agent",
    "codex-fresh-context",
}
TERMINAL_VERDICTS = {
    "audited_clean",
    "audited_renaming",
    "audited_conditional",
    "audited_decoration",
    "audited_failed",
    "audited_numerical_match",
}
_CODEX_FAMILY_RE = re.compile(r"^codex-gpt-(\d+(?:\.\d+)*)$")


def codex_family_meets_minimum(family: str, minimum: str = "gpt-5.5") -> bool:
    if not isinstance(family, str) or not family.startswith("codex-gpt-"):
        return True
    fam_match = _CODEX_FAMILY_RE.match(family)
    if not fam_match:
        return True
    min_match = re.match(r"gpt-(\d+(?:\.\d+)*)", minimum)
    if not min_match:
        return True
    fam_rank = tuple(int(part) for part in fam_match.group(1).split("."))
    min_rank = tuple(int(part) for part in min_match.group(1).split("."))
    width = max(len(fam_rank), len(min_rank))
    fam_padded = fam_rank + (0,) * (width - len(fam_rank))
    min_padded = min_rank + (0,) * (width - len(min_rank))
    return fam_padded >= min_padded


def repair_class_is_valid(notes: str | None) -> bool:
    if not notes:
        return False
    first_token = notes.strip().split(":", 1)[0].strip().split()[0].lower() if notes.strip() else ""
    return first_token in ALLOWED_REPAIR_CLASSES


def clean_audit_provenance_is_compatible(
    audit: dict, *, top_level: bool
) -> bool:
    """Apply the current capability policy without pinning one Codex release."""
    family = audit.get("auditor_family")
    independence = audit.get("independence")
    if isinstance(family, str) and family.startswith("codex-gpt-"):
        model = audit.get("auditor_model")
        match = (
            re.fullmatch(r"gpt-(\d+(?:\.\d+)*)-sol", model)
            if isinstance(model, str)
            else None
        )
        return bool(
            match
            and family == f"codex-gpt-{match.group(1)}"
            and codex_family_meets_minimum(family, minimum="gpt-5.6")
            and audit.get("auditor_reasoning_effort") == "xhigh"
            and independence != "weak"
        )
    model = audit.get("auditor_model")
    reasoning = audit.get("auditor_reasoning_effort")
    non_codex_provenance = bool(
        isinstance(family, str)
        and family
        and not family.startswith("codex-gpt-")
        and isinstance(model, str)
        and model
        and not model.startswith("gpt-")
        and isinstance(reasoning, str)
        and reasoning
    )
    if not non_codex_provenance:
        return False
    if top_level:
        return independence in {"strong", "external", "judicial_review"}
    return independence not in {None, "weak"}


def archived_audit_is_lint_compatible(archived: dict) -> bool:
    """True if restoring this archived audit will satisfy current audit lint.

    The restoration path should not turn old archived evidence into live
    authority when current lint would immediately queue or reject it. Rows
    that fail these checks remain invalidated and should be re-audited.
    """
    audit_status = archived.get("audit_status")
    if audit_status not in TERMINAL_VERDICTS:
        return False
    if archived.get("claim_type") not in ALLOWED_CLAIM_TYPES:
        return False
    if not archived.get("claim_scope"):
        return False
    if archived.get("independence") not in ALLOWED_INDEPENDENCE:
        return False
    if audit_status == "audited_conditional":
        if not repair_class_is_valid(archived.get("notes_for_re_audit_if_any")):
            return False

    fam = archived.get("auditor_family")
    if (
        archived.get("audit_status") == "audited_clean"
        and not clean_audit_provenance_is_compatible(archived, top_level=True)
    ):
        return False
    if fam is not None:
        if fam not in CANONICAL_AUDITOR_FAMILIES and fam not in LEGACY_AUDITOR_FAMILIES:
            if not (isinstance(fam, str) and fam.startswith("codex-gpt-")):
                return False
        if fam in LEGACY_AUDITOR_FAMILIES:
            return False
        if isinstance(fam, str) and fam.startswith("codex-gpt-"):
            if not codex_family_meets_minimum(fam):
                return False

    cross = archived.get("cross_confirmation") or {}
    if isinstance(cross, dict):
        for seat_name in ("first_audit", "second_audit", "third_audit"):
            seat = cross.get(seat_name)
            if not isinstance(seat, dict) or seat.get("verdict") != "audited_clean":
                continue
            if not clean_audit_provenance_is_compatible(seat, top_level=False):
                return False

    return True


def status_rank(status: str | None) -> int:
    if status and status.startswith("decoration_under_"):
        return 70
    return RANK.get(status or "unaudited", -1)


def estimate_restored_effective_status(archived: dict) -> str:
    """Conservative effective-status estimate for an archived audit once restored.

    This is used only to decide whether a downstream `dep_weakened:*`
    invalidation can also be restored. For clean theorem/no-go/bounded rows,
    use the retained grade implied by the archived claim_type. For terminal
    non-clean audits, the effective status is the terminal verdict itself.
    Decorations are intentionally conservative: if a downstream audit expected
    `decoration_under_*`, the full pipeline should decide whether that chain
    has really re-closed.
    """
    audit_status = archived.get("audit_status")
    if audit_status == "audited_clean":
        claim_type = archived.get("claim_type")
        if claim_type == "open_gate":
            return "open_gate"
        if claim_type == "meta":
            return "meta"
        if claim_type == "decoration":
            return "audited_decoration"
        return CLAIM_TYPE_TO_RETAINED.get(claim_type, "retained_pending_chain")
    return audit_status or "unaudited"


def is_archived_terminal_failed_dep(dep: str, rows: dict[str, dict]) -> bool:
    dep_row = rows.get(dep)
    if not dep_row:
        return False
    return (
        dep_row.get("audit_status") == "audited_failed"
        and (dep_row.get("note_path") or "").startswith("archive_unlanded/")
    )


def noncritical_invalidation_after_restore(row: dict, rows: dict[str, dict]) -> str | None:
    """Return a non-criticality invalidation reason that would still apply
    after restoration, or None if the archived audit is not stale for another
    reason.

    This intentionally mirrors the dependency/dependency-metadata checks from
    `invalidate_stale_audits.detect_invalidation`. The criticality bump itself
    is handled separately by PR #907's noop/soft-reset policy; if another
    blocker remains, restoration would only create churn and should be skipped.
    """
    restored = restore_audit_from_previous(row, rows)
    if restored is None:
        return "missing_previous_audit"

    snap = restored.get("audit_state_snapshot")
    if snap is None:
        return None

    current_deps = sorted(restored.get("deps", []))
    snap_deps = sorted(snap.get("deps", []))
    if current_deps != snap_deps:
        added = sorted(set(current_deps) - set(snap_deps))
        removed = sorted(
            dep
            for dep in set(snap_deps) - set(current_deps)
            if not is_archived_terminal_failed_dep(dep, rows)
        )
        parts = []
        if added:
            parts.append(f"dep_added:{','.join(added[:3])}")
        if removed:
            parts.append(f"dep_removed:{','.join(removed[:3])}")
        if parts:
            return "deps_changed:" + "|".join(parts)

    snap_dep_status = snap.get("dep_effective_status", {})
    for dep_id in current_deps:
        before = snap_dep_status.get(dep_id, "unknown")
        after = rows.get(dep_id, {}).get("effective_status") or "unaudited"
        if status_rank(after) < status_rank(before):
            return f"dep_weakened:{dep_id}:{before}->{after}"

    snap_dep_type = snap.get("dep_claim_type") or {}
    if snap_dep_type:
        for dep_id in current_deps:
            before = snap_dep_type.get(dep_id)
            after = rows.get(dep_id, {}).get("claim_type")
            if before is not None and after != before:
                return f"dep_claim_type_changed:{dep_id}:{before}->{after}"

    snap_dep_scope = snap.get("dep_claim_scope") or {}
    if snap_dep_scope:
        for dep_id in current_deps:
            before = snap_dep_scope.get(dep_id)
            after = rows.get(dep_id, {}).get("claim_scope")
            if before is not None and after != before:
                return f"dep_claim_scope_changed:{dep_id}"

    return None


def categorize_criticality_bump_for_archived(archived: dict, target_criticality: str) -> str:
    """Mirror `invalidate_stale_audits._categorize_criticality_bump` for an
    archived audit blob (in `previous_audits`).

    MUST STAY IN SYNC with the live policy in
    `docs/audit/scripts/invalidate_stale_audits.py`.

    Returns one of `"noop"`, `"soft_reset"`, `"invalidate"`.
    """
    if target_criticality in ("leaf", "medium"):
        return "noop"
    audit_status = archived.get("audit_status")
    indep = archived.get("independence")
    if audit_status != "audited_clean":
        return "noop"
    if indep is None or indep == "weak":
        return "invalidate"
    if target_criticality == "high":
        return "noop"
    cc = archived.get("cross_confirmation") or {}
    cc_status = cc.get("status") if isinstance(cc, dict) else None
    if cc_status in {"confirmed", "third_confirmed_first", "third_confirmed_second", "third_confirmed_hybrid"}:
        return "noop"
    return "soft_reset"


def parse_criticality_increased_target(reason: str) -> str | None:
    """Parse the `after` tier from `criticality_increased:before->after`."""
    if not reason.startswith("criticality_increased:"):
        return None
    payload = reason[len("criticality_increased:"):]
    if "->" not in payload:
        return None
    return payload.split("->", 1)[1].strip() or None


def parse_dep_weakened_dep_id(reason: str) -> str | None:
    """Parse `dep_id` from `dep_weakened:dep_id:before->after`."""
    parsed = parse_dep_weakened(reason)
    if parsed is None:
        return None
    return parsed[0]


def parse_dep_weakened(reason: str) -> tuple[str, str, str] | None:
    """Parse `dep_id`, `before`, and `after` from
    `dep_weakened:dep_id:before->after`.
    """
    if not reason.startswith("dep_weakened:"):
        return None
    parts = reason.split(":", 2)
    if len(parts) < 3:
        return None
    dep_id = parts[1] or None
    if dep_id is None or "->" not in parts[2]:
        return None
    before, after = parts[2].split("->", 1)
    before = before.strip()
    after = after.strip()
    if not before or not after:
        return None
    return dep_id, before, after


@contextlib.contextmanager
def _forensic_gate():
    prior = os.environ.get("AUDIT_FORENSIC_MODE")
    os.environ["AUDIT_FORENSIC_MODE"] = "1"
    try:
        yield
    finally:
        if prior is None:
            os.environ.pop("AUDIT_FORENSIC_MODE", None)
        else:
            os.environ["AUDIT_FORENSIC_MODE"] = prior


def restore_audit_from_previous(
    row: dict,
    rows: dict[str, dict] | None = None,
) -> dict | None:
    """Copy the most recent previous_audits entry back to the live row.

    The invalidation archive remains append-only. A separate restoration
    record identifies the exact archived payload and policy that authorized
    reversal, so restoration never erases the reason the audit was archived.
    """
    history = list(row.get("previous_audits") or [])
    if not history:
        return None
    archived = history[-1]
    # Axiom-premise pre-check (mirrors invalidate_stale_audits.py's
    # axiom_premise_changed trigger exactly, including its tolerance for
    # snapshots that predate the hash map): an audit performed under
    # different axiom-premise text is re-audit material, never restore
    # material. Without this, a restored stale-premise verdict is briefly
    # LIVE in the ledger until the next sweep re-invalidates it — a window
    # in which dispatch producers, lane certification, or a collaborator
    # can read a verdict audited under different axioms as current.
    if rows is not None:
        snap = archived.get("audit_state_snapshot") or {}
        snap_axiom_hash = snap.get("dep_axiom_premise_note_hash") or {}
        for dep, before in snap_axiom_hash.items():
            after = (rows.get(dep) or {}).get("note_hash")
            if before is not None and after is not None and before != after:
                return None
    new_row = dict(row)
    new_row["previous_audits"] = history
    archived_reference = hashlib.sha256(
        json.dumps(archived, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()
    restoration_history = list(row.get("restoration_history") or [])
    restoration_history.append({
        "restored_at": datetime.now(timezone.utc).isoformat(),
        "restoration_policy": "restore_overaggressive_invalidation.v2",
        "archived_audit_sha256": archived_reference,
        "archived_at": archived.get("archived_at"),
        "invalidation_reason": archived.get("invalidation_reason"),
    })
    new_row["restoration_history"] = restoration_history
    for field in ARCHIVED_FIELDS:
        if field in archived:
            new_row[field] = archived[field]
    invocation_history: list[str] = []
    for value in (
        *(archived.get("audit_invocation_history") or []),
        archived.get("audit_invocation_id"),
        *(row.get("audit_invocation_history") or []),
        row.get("audit_invocation_id"),
    ):
        if isinstance(value, str) and value and value not in invocation_history:
            invocation_history.append(value)
    if invocation_history:
        new_row["audit_invocation_history"] = invocation_history
    note_body = ""
    note_path = str(new_row.get("note_path") or "")
    try:
        note_body = (REPO_ROOT / note_path).read_text(encoding="utf-8", errors="replace")
    except OSError:
        pass
    # Restoring archived clean authority is a certification-like act and uses
    # the forensic tier. A non-clean development verdict is repair-queue
    # evidence, not retained authority, so it must use the same packet-binding
    # rule as live validation/invalidation instead of being promoted to a
    # stronger tier merely by the restoration transport.
    restoring_clean = new_row.get("audit_status") == "audited_clean"
    gate_context = _forensic_gate() if restoring_clean else contextlib.nullcontext()
    with gate_context:
        source_required = no_go_discipline_gate.source_requires_no_go_discipline(
            note_path, note_body, new_row.get("claim_type")
        )
    gate_blob = {
        "claim_type": new_row.get("claim_type"),
        "claim_scope": new_row.get("claim_scope"),
        "chain_closes": new_row.get("chain_closes"),
        "load_bearing_step": new_row.get("load_bearing_step"),
        "chain_closure_explanation": new_row.get("chain_closure_explanation"),
        "verdict": new_row.get("audit_status"),
        "verdict_rationale": new_row.get("verdict_rationale"),
        "notes_for_re_audit_if_any": new_row.get("notes_for_re_audit_if_any"),
        "no_go_discipline": new_row.get("no_go_discipline"),
        "negative_assertion_classes": new_row.get("negative_assertion_classes"),
    }
    gate_context = _forensic_gate() if restoring_clean else contextlib.nullcontext()
    with gate_context:
        output_required = no_go_discipline_gate.output_requires_no_go_discipline(
            gate_blob
        )
    # Honor a non-empty declaration present on EITHER storage surface:
    # the archived audit or the reset live row (legacy archives predate
    # the field, but a surviving live declaration is still the auditor's
    # semantic judgment). Absence of the key on genuinely old archives
    # remains accepted.
    declared_archived = archived.get("negative_assertion_classes")
    declared_live = row.get("negative_assertion_classes")
    declared_requires = any(
        isinstance(d, list) and bool(d)
        for d in (declared_archived, declared_live)
    )
    packet_binds = no_go_discipline_gate.packet_requirement_binds(
        gate_blob, source_required=source_required
    )
    if (
        (source_required or output_required or declared_requires)
        and packet_binds
        and new_row.get("no_go_discipline") is None
    ):
        return None
    cross = new_row.get("cross_confirmation") or {}
    cross_has_packet = isinstance(cross, dict) and any(
        isinstance(cross.get(audit_key), dict)
        and isinstance(cross[audit_key].get("no_go_discipline"), dict)
        for audit_key in ("first_audit", "second_audit", "third_audit")
    )
    current_manifest = None
    if new_row.get("no_go_discipline") is not None or cross_has_packet:
        ledger_rows = rows or {str(new_row.get("claim_id") or ""): new_row}
        validation_row = dict(new_row)
        validation_row["previous_audits"] = history[:-1]
        validation_rows = dict(ledger_rows)
        validation_rows[str(new_row.get("claim_id") or "")] = validation_row
        current_manifest = no_go_discipline_gate.build_evidence_manifest(
            validation_row, validation_rows, REPO_ROOT
        )
    if isinstance(cross, dict):
        for audit_key in ("first_audit", "second_audit", "third_audit"):
            summary = cross.get(audit_key)
            if not isinstance(summary, dict) or not summary:
                continue
            verdict = summary.get("verdict") or summary.get("audit_status")
            summary_requires_packet = (
                source_required
                or no_go_discipline_gate.output_requires_no_go_discipline(summary)
                or bool(summary.get("negative_assertion_classes"))
            )
            packet = summary.get("no_go_discipline")
            if packet is None:
                # A required clean seat without a packet is not restorable.
                if summary_requires_packet and verdict == "audited_clean":
                    return None
                continue
            # A PRESENT nested packet must round-trip validation even when
            # the seat would not independently require one, mirroring the
            # live invalidator's present-packet checks (restoration always
            # evaluates in the forensic tier).
            manifest = no_go_discipline_gate.evidence_manifest_from_snapshot(
                packet if isinstance(packet, dict) else {}
            )
            if verdict == "audited_clean":
                if manifest is None:
                    return None
                if no_go_discipline_gate.evidence_snapshot_current_error(
                    packet, current_manifest or {}
                ):
                    return None
            elif manifest is None:
                manifest = current_manifest
            if no_go_discipline_gate.validate_no_go_discipline(
                {
                    **summary,
                    "verdict": verdict,
                    "chain_closes": summary.get(
                        "chain_closes", verdict == "audited_clean"
                    ),
                },
                source_required=source_required,
                evidence_manifest=manifest,
            ):
                return None
    # Restoration is a certification-like act: a present packet must
    # round-trip through its authenticated snapshot and validate forensically.
    if new_row.get("no_go_discipline") is not None:
        evidence_manifest = no_go_discipline_gate.evidence_manifest_from_snapshot(
            new_row["no_go_discipline"]
        )
        if evidence_manifest is None:
            return None
        if no_go_discipline_gate.evidence_snapshot_current_error(
            new_row["no_go_discipline"], current_manifest or {}
        ):
            return None
        if no_go_discipline_gate.validate_no_go_discipline(
            gate_blob,
            source_required=source_required,
            evidence_manifest=evidence_manifest,
        ):
            return None
    return new_row


def select_restore_candidates(
    rows: dict[str, dict],
) -> tuple[dict[str, str], list[tuple[str, str, str]], dict[str, str], list[tuple[str, str, str]]]:
    """First pass: find rows that should be restored.

    Returns:
      - `crit_set`: dict mapping `cid` -> archived `audit_status`
        (e.g. `audited_clean`, `audited_conditional`, ...) for rows whose
        most recent invalidation was a `criticality_increased:*` that
        PR #907's rule would have noop'd or soft_reset'd.
      - `dep_weakened_set`: list of `(cid, dep_id, archived_status)`
        tuples for rows whose most recent invalidation was a
        `dep_weakened:*` whose dep is restored in this same pass (via
        `crit_set` or `packet_set`) and whose restored dep tier is no
        weaker than the archived audit's snapshot.
      - `packet_set`: dict mapping `cid` -> archived `audit_status` for
        rows whose most recent invalidation was
        `no_go_discipline_packet_missing` and whose archived audit is
        restorable under the CURRENT no-go trigger: the restoration
        guard in `restore_audit_from_previous` re-runs the live
        source/output gate, so a row that still asserts a gated negative
        boundary without a packet stays invalidated for fresh audit.
        Only the trigger-precision repair makes rows eligible here.
      - `recovered_dep_set`: list of `(cid, dep_id, archived_status)`
        tuples for rows whose most recent invalidation was a
        `dep_weakened:*` whose dep has ALREADY recovered on the live
        ledger (a landed re-audit or a prior restoration pass) to a tier
        no weaker than the one the archived audit closed against, and
        which pass every other still-live invalidation check.

    Rows further down a weakened chain become eligible on later passes as
    their dependencies recover; each nightly pipeline run advances the
    frontier by at least one dependency hop, so recovery converges without
    any ordering logic here.
    """
    crit_set: dict[str, str] = {}
    crit_archived: dict[str, dict] = {}
    packet_set: dict[str, str] = {}
    packet_archived: dict[str, dict] = {}
    recovered_dep_set: list[tuple[str, str, str]] = []
    dep_weakened_candidates: list[tuple[str, str, str, dict]] = []

    for cid, row in rows.items():
        if row.get("audit_status") != "unaudited":
            continue
        history = row.get("previous_audits") or []
        if not history:
            continue
        archived = history[-1]
        reason = archived.get("invalidation_reason") or ""

        target = parse_criticality_increased_target(reason)
        if target is not None:
            action = categorize_criticality_bump_for_archived(archived, target)
            if (
                action in ("noop", "soft_reset")
                and archived_audit_is_lint_compatible(archived)
                and restore_audit_from_previous(row, rows) is not None
                and noncritical_invalidation_after_restore(row, rows) is None
            ):
                crit_set[cid] = archived.get("audit_status") or "?"
                crit_archived[cid] = archived
            continue

        if reason == "no_go_discipline_packet_missing":
            if (
                archived_audit_is_lint_compatible(archived)
                and restore_audit_from_previous(row, rows) is not None
                and noncritical_invalidation_after_restore(row, rows) is None
            ):
                packet_set[cid] = archived.get("audit_status") or "?"
                packet_archived[cid] = archived
            continue

        dep = parse_dep_weakened(reason)
        if dep is not None:
            if not archived_audit_is_lint_compatible(archived):
                continue
            if restore_audit_from_previous(row, rows) is None:
                continue
            dep_id, before_status, _after_status = dep
            dep_row = rows.get(dep_id)
            if dep_row is None:
                # A vanished dependency is never a recovered dependency.
                dep_weakened_candidates.append(
                    (cid, dep_id, before_status, archived)
                )
                continue
            current_dep_status = dep_row.get("effective_status") or "unaudited"
            if (
                status_rank(current_dep_status) >= status_rank(before_status)
                and noncritical_invalidation_after_restore(row, rows) is None
            ):
                recovered_dep_set.append(
                    (cid, dep_id, archived.get("audit_status") or "?")
                )
                continue
            dep_weakened_candidates.append((cid, dep_id, before_status, archived))
            continue

    restored_this_pass = {**crit_archived, **packet_archived}
    dep_weakened_set: list[tuple[str, str, str]] = []
    for cid, dep_id, before_status, archived in dep_weakened_candidates:
        dep_archived = restored_this_pass.get(dep_id)
        if dep_archived is None:
            continue
        restored_dep_status = estimate_restored_effective_status(dep_archived)
        if status_rank(restored_dep_status) < status_rank(before_status):
            continue
        # Every other still-live invalidation check must also be clean;
        # evaluate the blockers with the paired dependency virtually at
        # its estimated restored tier so only the dependency being
        # restored this pass is exempt from the comparison.
        virtual_dep = dict(rows.get(dep_id) or {"claim_id": dep_id})
        virtual_dep["effective_status"] = restored_dep_status
        virtual_rows = dict(rows)
        virtual_rows[dep_id] = virtual_dep
        if noncritical_invalidation_after_restore(rows[cid], virtual_rows) is not None:
            continue
        dep_weakened_set.append((cid, dep_id, archived.get("audit_status") or "?"))

    return crit_set, dep_weakened_set, packet_set, recovered_dep_set


def select_false_positive_no_go_candidates(rows: dict[str, dict]) -> dict[str, str]:
    """Find clean audits invalidated only by a trigger that no longer fires.

    This is deliberately restricted to the packet-missing reason. Invalid
    packets and cross-confirmation failures still require fresh audit rather
    than schema-era restoration.
    """
    selected: dict[str, str] = {}
    for cid, row in rows.items():
        if row.get("audit_status") != "unaudited":
            continue
        history = row.get("previous_audits") or []
        if not history:
            continue
        archived = history[-1]
        if archived.get("invalidation_reason") != "no_go_discipline_packet_missing":
            continue
        if not archived_audit_is_lint_compatible(archived):
            continue
        if restore_audit_from_previous(row, rows) is None:
            continue
        if noncritical_invalidation_after_restore(row, rows) is not None:
            continue
        selected[cid] = archived.get("audit_status") or "?"
    return selected


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Restore audits over-aggressively invalidated before PR #907's "
            "criticality_increased / dep_weakened policy refinement."
        )
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Identify and report restore candidates without modifying the ledger.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Cap the number of rows restored (per category). For testing.",
    )
    parser.add_argument(
        "--false-positive-no-go-only",
        action="store_true",
        help=(
            "Skip the older criticality restoration scan and process only "
            "packet-missing rows whose current no-go trigger no longer fires."
        ),
    )
    args = parser.parse_args()

    ledger_io.ensure_cache()
    if not LEDGER_PATH.exists():
        print(f"FAIL: ledger missing at {LEDGER_PATH}", file=sys.stderr)
        return 1

    ledger = json.loads(LEDGER_PATH.read_text(encoding="utf-8"))
    rows: dict[str, dict] = ledger.get("rows", {})

    if args.false_positive_no_go_only:
        crit_set, dep_weakened_set = {}, []
        packet_set, recovered_dep_set = {}, []
    else:
        crit_set, dep_weakened_set, packet_set, recovered_dep_set = (
            select_restore_candidates(rows)
        )
    false_positive_set = select_false_positive_no_go_candidates(rows)

    if args.limit is not None:
        crit_set = dict(sorted(crit_set.items())[: args.limit])
        false_positive_set = dict(sorted(false_positive_set.items())[: args.limit])
        packet_set = dict(sorted(packet_set.items())[: args.limit])
        # Same-pass children whose parent was limited out must not restore
        # ahead of their dependency.
        surviving_parents = set(crit_set) | set(packet_set)
        dep_weakened_set = [
            entry for entry in dep_weakened_set if entry[1] in surviving_parents
        ][: args.limit]
        recovered_dep_set = recovered_dep_set[: args.limit]

    def report(label: str, counts_from) -> None:
        status_counts: dict[str, int] = {}
        for prev_status in counts_from:
            status_counts[prev_status] = status_counts.get(prev_status, 0) + 1
        for status, n in sorted(status_counts.items(), key=lambda x: -x[1]):
            print(f"    {n:5d}  was {status}")

    print(f"Identified {len(crit_set)} criticality_increased restore candidates:")
    report("crit", crit_set.values())

    print(f"Identified {len(dep_weakened_set)} dep_weakened restore candidates"
          f" (cascade from deps restored in this pass):")
    report("dep", [prev for _cid, _dep, prev in dep_weakened_set])

    false_positive_ids = set(false_positive_set)
    packet_set = {
        cid: status
        for cid, status in packet_set.items()
        if cid not in false_positive_ids
    }
    print(f"Identified {len(packet_set)} no_go_discipline_packet_missing restore"
          f" candidates (archived audit restorable under the current trigger,"
          f" excluding rows the false-positive lane already selects):")
    report("packet", packet_set.values())

    print(f"Identified {len(recovered_dep_set)} dep_weakened restore candidates"
          f" (dep already recovered on the live ledger):")
    report("recovered", [prev for _cid, _dep, prev in recovered_dep_set])

    print(
        f"Identified {len(false_positive_set)} false-positive no-go trigger "
        "restore candidates:"
    )
    false_positive_counts: dict[str, int] = {}
    for prev_status in false_positive_set.values():
        false_positive_counts[prev_status] = false_positive_counts.get(prev_status, 0) + 1
    for status, n in sorted(false_positive_counts.items(), key=lambda x: -x[1]):
        print(f"    {n:5d}  was {status}")

    if args.dry_run:
        print("\nDry run: no changes written.")
        return 0

    restored_count = 0
    restore_cids = list(crit_set)
    restore_cids += [cid for cid, _dep, _prev in dep_weakened_set]
    restore_cids += list(packet_set)
    restore_cids += [cid for cid, _dep, _prev in recovered_dep_set]
    seen: set[str] = set()
    for cid in restore_cids:
        if cid in seen:
            continue
        seen.add(cid)
        new_row = restore_audit_from_previous(rows[cid], rows)
        if new_row is None:
            continue
        rows[cid] = new_row
        restored_count += 1
    for cid in false_positive_set:
        if cid in seen:
            continue
        seen.add(cid)
        new_row = restore_audit_from_previous(rows[cid], rows)
        if new_row is None:
            continue
        rows[cid] = new_row
        restored_count += 1

    ledger["rows"] = rows
    ledger_io.save_ledger(ledger)

    print()
    print(f"Restored {restored_count} audits across {LEDGER_PATH.relative_to(REPO_ROOT)}")
    print()
    print("NEXT: run `bash docs/audit/scripts/run_pipeline.sh` to propagate. "
          "PR #907 must already be live on the running branch — otherwise the "
          "next nightly will re-invalidate under the old rule.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
