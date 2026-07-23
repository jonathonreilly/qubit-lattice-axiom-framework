#!/usr/bin/env python3
"""Explain how campaign-scoped audit exclusions re-enter the drainer.

The audit supervisor records operational exclusions in
``campaign-row-exclusions.jsonl``.  They are not scientific verdicts and must
not be copied into the ledger.  This read-only helper joins those records to
current operational ledger metadata and emits the prerequisite repair route
for a fresh campaign.
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


def load_exclusions(path: Path) -> list[dict]:
    return batch.load_campaign_exclusion_records(path)


def repair_route(record: dict, row: dict | None) -> dict:
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
        return {
            **result,
            "route": "fresh_schema_valid_seat",
            "ready_for_new_campaign": True,
            "action": (
                "Keep the malformed output non-authoritative. Correct the "
                "transport/prompt defect named in failures, then start a new "
                "campaign so a fresh restricted-context seat is selected."
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
        repair_route(record, rows.get(record["claim_id"]))
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
    path = (
        args.exclusions
        if args.exclusions is not None
        else args.campaign_workdir / "campaign-row-exclusions.jsonl"
    )
    if not path.exists():
        parser.error(f"exclusion file does not exist: {path}")
    try:
        exclusions = load_exclusions(path)
        rows = ledger_io.load_ledger().get("rows", {})
    except (OSError, ValueError) as exc:
        parser.error(str(exc))
    plan = build_plan(exclusions, rows)
    if args.json:
        print(json.dumps({"exclusions": plan}, indent=2, sort_keys=True))
        return 0
    print(f"audit campaign repair plan: {path}")
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
