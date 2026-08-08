#!/usr/bin/env python3
"""Compute the consolidated science-fix backlog surface.

Writes ``docs/audit/data/science_fix_backlog.json``: a generated, read-only
summary of every surface the science-fix-loop can drain, so the repair lane
survives ledger-wide invalidations and the nightly workflow can show the true
repair backlog even when zero applied verdicts exist.

Surfaces summarized:

1. ``applied_non_clean`` — live applied non-clean verdicts (the fix-loop's
   primary lane; empty immediately after any mass invalidation).
2. ``archived_advisory`` — rows whose LAST archived audit in
   ``previous_audits[]`` carries a non-clean scientific verdict while the live
   row is ``unaudited``.  These are ADVISORY: the archived verdict is void and
   authorizes nothing; the count exists so recorded defect-finding stays
   visible across resets.  ``unmapped_category_records`` counts complete
   archived non-clean records whose repair instruction cannot be routed
   automatically; ``incomplete_records`` counts records without the minimum
   rationale/path metadata needed to create an advisory candidate.
3. ``evidence_repair`` — rows the audit queue marks ``evidence_repair_required``,
   grouped by gate family (e.g. the forensic N5 execution certificate).

This script writes a generated data surface only.  It mints no verdict, edits
no ledger row, and carries no audit authority.
"""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
LEDGER_DIR = REPO_ROOT / "docs" / "audit" / "data" / "ledger"
QUEUE_PATH = REPO_ROOT / "docs" / "audit" / "data" / "audit_queue.json"
OUT_PATH = REPO_ROOT / "docs" / "audit" / "data" / "science_fix_backlog.json"

APPLIED_NON_CLEAN = (
    "audited_conditional",
    "audited_failed",
    "audited_renaming",
    "audited_numerical_match",
)

CONDITIONAL_PREFIXES = (
    "runner_artifact_issue",
    "scope_too_broad",
    "missing_dependency_edge",
    "missing_bridge_theorem",
)


def _mapped_category(verdict: str, repair_target: str) -> bool:
    """Mirror of scripts/science_fix_loop.py:audit_repair_category coverage."""
    if verdict in ("audited_renaming", "audited_failed", "audited_numerical_match"):
        return True
    if verdict == "audited_conditional":
        prefix = repair_target.split("—", 1)[0].split(":", 1)[0].strip().lower()
        return prefix in CONDITIONAL_PREFIXES
    return False


def _archived_repair_target(archived: dict) -> str:
    """Mirror science_fix_loop.archived_repair_target without importing it."""
    return str(
        archived.get("notes_for_re_audit_if_any")
        or archived.get("repair_target")
        or ""
    ).strip()


def _gate_family(issue: str) -> str:
    """Collapse a readiness-issue string to its stable gate-family prefix."""
    return issue.split(":", 1)[0].strip() or "unknown"


def main() -> int:
    applied = Counter()
    applied_rows: list[str] = []
    advisory = Counter()
    advisory_rows: list[str] = []
    advisory_unmapped = 0
    advisory_incomplete = 0

    for shard in sorted(LEDGER_DIR.glob("*/*.json")):
        try:
            row = json.loads(shard.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        if not isinstance(row, dict):
            continue
        raw_claim_id = row.get("claim_id")
        claim_id = str(raw_claim_id or shard.stem)
        status = row.get("audit_status")
        if status in APPLIED_NON_CLEAN:
            applied[status] += 1
            applied_rows.append(claim_id)
            continue
        if status != "unaudited":
            continue
        archived = row.get("previous_audits") or []
        if not isinstance(archived, list) or not archived:
            continue
        last = archived[-1]
        if not isinstance(last, dict):
            continue
        verdict = last.get("audit_status")
        if verdict not in APPLIED_NON_CLEAN:
            continue
        rationale = str(last.get("verdict_rationale") or "").strip()
        if not rationale:
            advisory_incomplete += 1
            continue
        repair_target = _archived_repair_target(last)
        if _mapped_category(str(verdict), repair_target):
            if not raw_claim_id or not row.get("note_path"):
                advisory_incomplete += 1
                continue
            advisory[str(verdict)] += 1
            advisory_rows.append(claim_id)
        else:
            advisory_unmapped += 1

    evidence = Counter()
    evidence_total = 0
    queue_available = QUEUE_PATH.exists()
    if queue_available:
        try:
            queue = json.loads(QUEUE_PATH.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            queue = {}
            queue_available = False
        rows = (
            queue.get("queue") if isinstance(queue, dict) else None
        ) or (queue.get("rows") if isinstance(queue, dict) else None)
        for entry in rows if isinstance(rows, list) else []:
            if not isinstance(entry, dict):
                continue
            issue = entry.get("forensic_evidence_readiness_issue")
            if entry.get("audit_work_kind") != "evidence_repair_required" and not issue:
                continue
            issue = issue or entry.get("audit_work_reason") or "unknown"
            evidence[_gate_family(str(issue))] += 1
            evidence_total += 1

    payload = {
        "schema": "science_fix_backlog_v1",
        "authority": (
            "generated summary only; no verdict, no premise, no audit "
            "authority; archived_advisory entries are VOID verdicts whose "
            "defect reports must be re-verified on current main before any "
            "edit"
        ),
        "applied_non_clean": {
            "total": sum(applied.values()),
            "by_verdict": dict(sorted(applied.items())),
        },
        "archived_advisory": {
            "total": sum(advisory.values()),
            "by_verdict": dict(sorted(advisory.items())),
            "unmapped_category_records": advisory_unmapped,
            "incomplete_records": advisory_incomplete,
        },
        "evidence_repair": {
            "queue_available": queue_available,
            "total": evidence_total if queue_available else None,
            "by_gate_family": dict(evidence.most_common()),
            "note": (
                "" if queue_available else
                "audit_queue.json absent (generated per pipeline run); run "
                "docs/audit/scripts/run_pipeline.sh first"
            ),
        },
        "drain_commands": {
            "applied_non_clean": "python3 scripts/science_fix_loop.py --dry-run",
            "archived_advisory": (
                "python3 scripts/science_fix_loop.py --from-archived --dry-run"
            ),
            "evidence_repair": (
                "see docs/audit/data/audit_queue.json rows with "
                "audit_work_kind=evidence_repair_required"
            ),
        },
    }
    OUT_PATH.write_text(
        json.dumps(payload, indent=1, sort_keys=False) + "\n", encoding="utf-8"
    )
    print(
        f"science_fix_backlog: applied={payload['applied_non_clean']['total']} "
        f"archived_advisory={payload['archived_advisory']['total']} "
        f"(+{advisory_unmapped} unmapped, "
        f"+{advisory_incomplete} incomplete) "
        f"evidence_repair={evidence_total if queue_available else 'unavailable'} "
        f"-> {OUT_PATH.relative_to(REPO_ROOT)}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
