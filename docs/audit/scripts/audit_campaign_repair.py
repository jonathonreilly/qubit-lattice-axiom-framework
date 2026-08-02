#!/usr/bin/env python3
"""Explain how campaign-scoped audit exclusions and skips re-enter.

The audit supervisor records operational exclusions in
``campaign-row-exclusions.jsonl`` and non-suppressing selector dispositions in
``campaign-selector-skips.jsonl``. They are not scientific verdicts and must
not be copied into the ledger. This read-only helper joins those records to
current operational ledger metadata and emits the prerequisite repair route.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
REPO_ROOT = SCRIPTS.parents[2]
sys.path.insert(0, str(SCRIPTS))

import ledger_io  # noqa: E402
import orchestrate_audit_batch as batch  # noqa: E402


SCHEMA_QUARANTINE = batch.SCHEMA_QUARANTINE_RESULT
COMPUTE_QUARANTINE = batch.COMPUTE_QUARANTINE_RESULT
TRANSACTION_QUARANTINE = batch.CLAIM_TRANSACTION_QUARANTINE_RESULT
BLOCKED_REENTRY = batch.BLOCKED_ROW_QUARANTINE_RESULT
SELECTION_SKIP = "selection_skip"


def load_exclusions(path: Path) -> list[dict]:
    return batch.load_campaign_exclusion_records(path)


def load_campaign_records(campaign_workdir: Path) -> list[dict]:
    records = load_exclusions(
        campaign_workdir / "campaign-row-exclusions.jsonl"
    )
    records.extend(
        batch.load_campaign_selection_skip_records(
            campaign_workdir / "campaign-selector-skips.jsonl"
        )
    )
    return records


def repair_route(
    record: dict,
    row: dict | None,
    rows: dict[str, dict] | None = None,
) -> dict:
    claim_id = record["claim_id"]
    reason = record["reason"]
    current = {
        "audit_status": row.get("audit_status") if row else None,
        "effective_status": row.get("effective_status") if row else None,
        "note_path": row.get("note_path") if row else None,
        "runner_path": row.get("runner_path") if row else None,
    }
    result = {
        "claim_id": claim_id,
        "reason": reason,
        "current": current,
        "failures": record.get("failures") or [],
        "detail": record.get("detail"),
    }
    if row is None:
        return {
            **result,
            "route": "repair_ledger_registration",
            "ready_for_new_campaign": False,
            "action": (
                "Restore or register the missing canonical ledger row, run the "
                "full pipeline and strict lint, then start a new campaign."
            ),
        }
    if reason == SCHEMA_QUARANTINE:
        failure_classes = {
            failure.get("failure_class")
            for failure in result["failures"]
            if isinstance(failure, dict)
        }
        if failure_classes == {"packet_completion_exhausted"}:
            return {
                **result,
                "route": "repair_packet_completion_contract",
                "ready_for_new_campaign": False,
                "action": (
                    "Keep the preserved scientific judgment non-authoritative "
                    "but do not spend another full seat. Repair the typed "
                    "N1-N8 packet/prompt defect named in failures and retain "
                    "the forensic run log for fingerprint-bound packet-only "
                    "recovery."
                ),
            }
        return {
            **result,
            "route": "fresh_scientific_seat_required",
            "ready_for_new_campaign": True,
            "action": (
                "Keep the malformed output non-authoritative. Correct the "
                "top-level contract defect named in failures, then start a "
                "new campaign so a fresh restricted-context scientific seat "
                "is selected."
            ),
        }
    if reason == COMPUTE_QUARANTINE:
        runner = str(row.get("runner_path") or "").strip()
        command = (
            f"python3 scripts/cached_runner_output.py {runner}"
            if runner
            else None
        )
        return {
            **result,
            "route": "supply_compute_artifact",
            "ready_for_new_campaign": False,
            "command": command,
            "action": (
                "Produce a SHA-pinned runner cache, sliced deterministic "
                "certificate, or independent derivation; run the full pipeline "
                "and strict lint; then start a new campaign."
            ),
        }
    if reason == BLOCKED_REENTRY:
        resolved = row.get("audit_status") != "unaudited"
        return {
            **result,
            "route": (
                "already_moved_out_of_reentry"
                if resolved
                else "repair_invalidation_cause"
            ),
            "ready_for_new_campaign": resolved,
            "invalidation_reason": record.get("invalidation_reason"),
            "action": (
                "The current row no longer has the quarantined unaudited "
                "re-entry state; verify a full pipeline and strict lint before "
                "a new campaign."
                if resolved
                else
                "Repair the recorded classifier, dependency, source-hash, or "
                "status invalidation cause. Require a converged full pipeline "
                "and strict lint before starting a new campaign."
            ),
        }
    if reason == TRANSACTION_QUARANTINE:
        return {
            **result,
            "route": "repair_claim_transaction",
            "ready_for_new_campaign": False,
            "action": (
                "Repair the recorded apply, pipeline, or strict-lint defect and "
                "prove the full pipeline is converged. The failed delivery "
                "minted no verdict; retry with a fresh seat in a new campaign "
                "unless a separate preserved-delivery replay contract verifies "
                "the exact envelope and source fingerprint."
            ),
        }
    if reason in batch.SELECTION_SKIP_REASONS:
        if reason == "missing_ledger_row":
            return {
                **result,
                "route": "ledger_registration_resolved",
                "ready_for_new_campaign": True,
                "action": (
                    "The row now exists in the canonical ledger. Verify the "
                    "full pipeline before starting a new campaign."
                ),
            }
        if reason == "effective_status_not_actionable":
            return {
                **result,
                "route": "already_settled_or_governed",
                "ready_for_new_campaign": True,
                "action": (
                    "The row is retained-grade, meta, or a governed decoration. "
                    "Record the non-actionable disposition and continue."
                ),
            }
        if reason == "audit_status_not_unaudited":
            audit_status = str(row.get("audit_status") or "")
            if audit_status == "audit_in_progress":
                route = "resume_audit_seat"
                action = "Resume the missing independent audit seat."
            elif audit_status in {
                "audited_conditional",
                "audited_renaming",
                "audited_failed",
                "audited_numerical_match",
            }:
                route = "validated_science_handoff"
                action = (
                    "Use the canonical applied verdict and invocation-bound "
                    "science-fix handoff; never reconstruct it from skip prose."
                )
            else:
                route = "already_settled_or_governed"
                action = (
                    "The row's current canonical status needs no science-fix "
                    "worker; record the disposition and continue."
                )
            return {
                **result,
                "route": route,
                "ready_for_new_campaign": route == "already_settled_or_governed",
                "action": action,
            }
        if reason in {"forensic_no_go", "forensic_source_shape"}:
            return {
                **result,
                "route": "forensic_audit",
                "ready_for_new_campaign": False,
                "action": (
                    "Route the row through audit-loop forensic mode; ordinary "
                    "science-fix workers cannot settle this skip."
                ),
            }
        if reason == "non_batch_claim_type":
            return {
                **result,
                "route": "governed_non_batch_type",
                "ready_for_new_campaign": False,
                "action": (
                    "Keep the row out of the development batch and use the "
                    "governed owner lane for its canonical claim type."
                ),
            }
        if reason == "dependencies_not_retained":
            blockers = []
            for dep in row.get("deps") or []:
                if not isinstance(dep, str):
                    continue
                if batch.audit_runner.premise_nodes.is_non_evidence_context_dep(
                    dep
                ):
                    blockers.append(dep)
                    continue
                if batch.accepted(dep):
                    continue
                dep_status = (rows or {}).get(dep, {}).get("effective_status")
                if (
                    dep_status in batch.RETAINED
                    or str(dep_status or "").startswith("decoration_under_")
                ):
                    continue
                blockers.append(dep)
            return {
                **result,
                "route": "repair_or_audit_upstream_dependencies",
                "ready_for_new_campaign": False,
                "blocking_dependencies": blockers,
                "action": (
                    "Repair or audit the cheapest blocking upstream dependency; "
                    "do not edit the downstream row to hide the edge."
                ),
            }
        if reason == "note_hash_drift":
            return {
                **result,
                "route": "refresh_note_hash_pipeline",
                "ready_for_new_campaign": False,
                "action": (
                    "Run the seeder, full pipeline, and strict lint so the "
                    "ledger note hash matches the canonical source."
                ),
            }
        if reason == "awaiting_science_repair":
            return {
                **result,
                "route": "validated_science_handoff",
                "ready_for_new_campaign": False,
                "action": (
                    "Use the current applied non-clean verdict and its "
                    "invocation-bound handoff for a source-side repair PR."
                ),
            }
        return {
            **result,
            "route": "manual_selector_triage",
            "ready_for_new_campaign": False,
            "action": (
                "Add a typed selector route and regression before retrying; "
                "never infer a verdict from an unknown skip."
            ),
        }
    return {
        **result,
        "route": "manual_operational_triage",
        "ready_for_new_campaign": False,
        "action": (
            "Unknown exclusion reason: preserve it, diagnose the operational "
            "cause, and do not translate it into a scientific verdict."
        ),
    }


def build_plan(exclusions: list[dict], rows: dict[str, dict]) -> list[dict]:
    return [
        repair_route(record, rows.get(record["claim_id"]), rows)
        for record in exclusions
    ]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Render a read-only repair plan for audit campaign exclusions"
    )
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument(
        "--campaign-workdir",
        type=Path,
        help="directory containing campaign-row-exclusions.jsonl",
    )
    source.add_argument(
        "--exclusions",
        type=Path,
        help="campaign-row-exclusions.jsonl path",
    )
    parser.add_argument("--json", action="store_true", help="emit JSON only")
    args = parser.parse_args(argv)
    path = args.exclusions
    if path is not None and not path.exists():
        parser.error(f"exclusion file does not exist: {path}")
    if args.campaign_workdir is not None and not args.campaign_workdir.is_dir():
        parser.error(
            f"campaign workdir does not exist: {args.campaign_workdir}"
        )
    try:
        exclusions = (
            load_exclusions(path)
            if path is not None
            else load_campaign_records(args.campaign_workdir)
        )
        rows = ledger_io.load_ledger().get("rows", {})
    except (OSError, ValueError) as exc:
        parser.error(str(exc))
    plan = build_plan(exclusions, rows)
    if args.json:
        print(json.dumps({"exclusions": plan}, indent=2, sort_keys=True))
        return 0
    source_label = path or args.campaign_workdir
    print(f"audit campaign repair plan: {source_label}")
    if not plan:
        print("  no campaign exclusions")
        return 0
    for item in plan:
        print(
            f"  {item['claim_id']}: {item['reason']} -> {item['route']} "
            f"(new_campaign_ready={str(item['ready_for_new_campaign']).lower()})"
        )
        if item.get("command"):
            print(f"    command: {item['command']}")
        print(f"    {item['action']}")
    print(
        "Start repaired rows in a new campaign workdir; reusing the old "
        "workdir intentionally preserves its exclusions."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
