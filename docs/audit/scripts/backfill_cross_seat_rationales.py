#!/usr/bin/env python3
"""Backfill pre-contract cross-confirmation seat summaries from envelopes.

The rationale-preserving apply contract (2026-07-13) records each seat's
``verdict_rationale`` and ``notes_for_re_audit_if_any`` inside its
``cross_confirmation`` summary, and the judicial panel refuses to seat a
disagreement whose recorded positions lack an invocation-bound full
rationale. Disagreements recorded BEFORE the contract carry tuple-only
summaries, so their panels are blocked even though the seats' full audits
still exist as orchestrator delivery envelopes on disk.

This tool completes exactly that gap and nothing else. For each targeted
disagreement row it scans the supplied delivery directories for envelopes
whose ``audit.claim_id`` matches the row and whose
``audit.audit_invocation_id`` EQUALS the invocation id already recorded in
the seat summary, then copies the envelope's ``verdict_rationale`` and
``notes_for_re_audit_if_any`` into that summary. Every recorded seat field
other than those two backfill fields is cross-checked against the envelope
first (with the same whitespace normalization for ``claim_scope`` and set
normalization for ``negative_assertion_classes`` used by ``apply_audit.py``).
ANY mismatch refuses that seat: an envelope that disagrees with the recorded
seat is not evidence, whatever its invocation id says. Rows whose summaries
already carry rationales are left untouched. Nothing is deleted and no
verdict, status, or tuple field is modified.

Run from a dedicated clean ``main`` checkout; commit the ledger change
through the standard pipeline gates like any audit-data repair.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
import orchestrate_audit_batch as batch  # noqa: E402

import ledger_io

LEDGER = batch.DATA / "audit_ledger.json"

REQUIRED_BINDING_FIELDS = (
    "verdict",
    "claim_type",
    "claim_scope",
    "load_bearing_step_class",
    "negative_assertion_classes",
    "auditor",
    "auditor_family",
    "auditor_model",
    "auditor_reasoning_effort",
    "independence",
    "audit_date",
    "audit_invocation_id",
)
BACKFILL_FIELDS = {"verdict_rationale", "notes_for_re_audit_if_any"}


def norm(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip())


def normalized_classes(value: object) -> tuple[str, ...] | None:
    if not isinstance(value, list) or not all(
        isinstance(item, str) for item in value
    ):
        return None
    return tuple(sorted(set(value)))


def envelope_index(delivery_dirs: list[Path]) -> dict[tuple[str, str], dict]:
    index: dict[tuple[str, str], dict] = {}
    sources: dict[tuple[str, str], Path] = {}
    for directory in delivery_dirs:
        for path in sorted(directory.glob("delivery-*.json")):
            try:
                envelope = json.loads(path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError):
                continue
            audit = envelope.get("audit")
            if not isinstance(audit, dict):
                continue
            cid = str(audit.get("claim_id") or "")
            invocation = str(audit.get("audit_invocation_id") or "")
            if cid and invocation:
                key = (cid, invocation)
                if key in index:
                    if index[key] != audit:
                        raise ValueError(
                            "conflicting delivery envelopes for "
                            f"claim {cid!r}, invocation {invocation}: "
                            f"{sources[key]} and {path}"
                        )
                    continue
                index[key] = audit
                sources[key] = path
    return index


def seat_mismatch(
    summary: dict,
    audit: dict,
    expected_claim_id: str,
    expected_invocation_id: str,
) -> str | None:
    if audit.get("claim_id") != expected_claim_id:
        return (
            f"claim_id mismatch: row={expected_claim_id!r} "
            f"envelope={audit.get('claim_id')!r}"
        )
    if audit.get("audit_invocation_id") != expected_invocation_id:
        return (
            "audit_invocation_id mismatch: "
            f"summary={expected_invocation_id!r} "
            f"envelope={audit.get('audit_invocation_id')!r}"
        )
    missing = [field for field in REQUIRED_BINDING_FIELDS if field not in summary]
    if missing:
        return f"summary missing recorded binding fields: {missing}"

    summary_scope = summary.get("claim_scope")
    audit_scope = audit.get("claim_scope")
    if not isinstance(summary_scope, str) or not isinstance(audit_scope, str):
        return "claim_scope mismatch: both values must be strings"
    if norm(summary_scope) != norm(audit_scope):
        return "claim_scope mismatch after whitespace normalization"

    summary_classes = normalized_classes(summary.get("negative_assertion_classes"))
    audit_classes = normalized_classes(audit.get("negative_assertion_classes"))
    if summary_classes is None or audit_classes is None:
        return (
            "negative_assertion_classes mismatch: both values must be "
            "lists of strings"
        )
    if summary_classes != audit_classes:
        return (
            f"negative_assertion_classes mismatch: summary={summary_classes} "
            f"envelope={audit_classes}"
        )

    special_fields = {"claim_scope", "negative_assertion_classes"}
    for field in sorted(set(summary) - BACKFILL_FIELDS - special_fields):
        if summary.get(field) != audit.get(field):
            return (
                f"{field} mismatch: summary={summary.get(field)!r} "
                f"envelope={audit.get(field)!r}"
            )
    return None


def backfill_row(row: dict, index: dict[tuple[str, str], dict]) -> tuple[int, list[str]]:
    cid = str(row.get("claim_id") or "")
    cross = row.get("cross_confirmation") or {}
    filled = 0
    problems: list[str] = []
    for label in ("first_audit", "second_audit"):
        summary = cross.get(label)
        if not isinstance(summary, dict) or not summary:
            problems.append(f"{label}: summary missing")
            continue
        if str(summary.get("verdict_rationale") or "").strip():
            continue
        invocation = str(summary.get("audit_invocation_id") or "")
        if not invocation:
            problems.append(
                f"{label}: summary has no invocation id; fresh seat rerun required"
            )
            continue
        audit = index.get((cid, invocation))
        if audit is None:
            problems.append(
                f"{label}: no envelope bound to invocation {invocation[:12]}; "
                "fresh seat rerun required if the original envelope is unavailable"
            )
            continue
        mismatch = seat_mismatch(summary, audit, cid, invocation)
        if mismatch:
            problems.append(f"{label}: {mismatch}")
            continue
        rationale = audit.get("verdict_rationale")
        if not isinstance(rationale, str) or not rationale.strip():
            problems.append(
                f"{label}: bound envelope rationale must be a non-empty string"
            )
            continue
        summary["verdict_rationale"] = rationale
        notes = audit.get("notes_for_re_audit_if_any")
        if isinstance(notes, str) and notes.strip():
            summary["notes_for_re_audit_if_any"] = notes
        filled += 1
    return filled, problems


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Backfill pre-contract disagreement seat rationales from "
            "invocation-bound orchestrator delivery envelopes"
        )
    )
    parser.add_argument(
        "--deliveries",
        action="append",
        required=True,
        help="directory of delivery-*.json envelopes (repeatable)",
    )
    parser.add_argument(
        "--claims",
        help="comma-separated claim ids (default: every disagreement row)",
    )
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if not args.dry_run:
        error = batch.clean_main_error()
        if error:
            print(f"refusing to run: {error}. Use a dedicated clean main checkout.")
            return 2

    delivery_dirs = [Path(entry) for entry in args.deliveries]
    for directory in delivery_dirs:
        if not directory.is_dir():
            print(f"refusing to run: {directory} is not a directory")
            return 2
    try:
        index = envelope_index(delivery_dirs)
    except ValueError as exc:
        print(f"refusing to run: {exc}")
        return 2
    print(f"indexed {len(index)} invocation-bound envelopes")

    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    rows = ledger.get("rows", {})
    if args.claims:
        scope = [cid.strip() for cid in args.claims.split(",") if cid.strip()]
    else:
        scope = sorted(
            cid
            for cid, row in rows.items()
            if (row.get("cross_confirmation") or {}).get("status") == "disagreement"
        )

    total_filled = 0
    for cid in scope:
        row = rows.get(cid)
        if not row:
            print(f"   skip: {cid}: missing ledger row")
            continue
        if (row.get("cross_confirmation") or {}).get("status") != "disagreement":
            print(f"   skip: {cid}: not a disagreement")
            continue
        filled, problems = backfill_row(row, index)
        total_filled += filled
        state = f"filled {filled} seat rationale(s)"
        if problems:
            state += "; unresolved: " + " | ".join(problems)
        print(f"   {cid}: {state}")

    if total_filled == 0:
        print("nothing to backfill")
        return 0
    if args.dry_run:
        print(f"dry run: would fill {total_filled} seat rationale(s)")
        return 0
    # Match apply_audit.py's canonical ledger serialization exactly.
    ledger_io.save_ledger(ledger)
    print(f"wrote {LEDGER} with {total_filled} backfilled seat rationale(s)")
    print(
        "NEXT: bash docs/audit/scripts/run_pipeline.sh && "
        "python3 docs/audit/scripts/audit_lint.py --strict, then commit the "
        "generated audit surfaces per the standard audit-data flow."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
