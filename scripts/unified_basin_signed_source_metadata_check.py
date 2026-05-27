#!/usr/bin/env python3
"""Metadata-boundary checker for the unified-basin signed-source salvage row."""

from __future__ import annotations

import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"
NOTE = DOCS / "UNIFIED_BASIN_SIGNED_SOURCE_CONTROL_SUPPORT_NOTE_2026-04-30.md"
CLAIM_ID = "unified_basin_signed_source_control_support_note_2026-04-30"

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        status = "PASS"
    else:
        FAIL_COUNT += 1
        status = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"{status}: {name}{suffix}")


def main() -> int:
    print("Unified basin signed-source metadata repair")
    print("=" * 72)

    note = NOTE.read_text(encoding="utf-8")
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    row = ledger["rows"][CLAIM_ID]

    print()
    print("A. Metadata boundary")
    print("-" * 72)
    check("note declares claim_type meta", "**Claim type:** meta" in note)
    check("note no longer declares bounded_theorem", "**Claim type:** bounded_theorem" not in note)
    check(
        "note says it carries no independent evidence",
        "carries no independent\naudit-grade numerical evidence" in note,
    )
    check(
        "note says archive pointer is not load-bearing",
        "route-history\nprovenance rather than a cited dependency" in note
        and "not load-bearing\nauthority" in note,
    )
    check(
        "note keeps future runner as separate science",
        "future science repair may\nbuild a fresh retained-generator runner" in note,
    )

    print()
    print("B. Archive link hygiene")
    print("-" * 72)
    check(
        "archive path is plain provenance text, not markdown authority link",
        "](../archive_unlanded/" not in note,
    )
    check(
        "archive path remains recorded",
        "archive_unlanded/unified-basin-signed-source-salvage-2026-04-30/UNIFIED_BASIN_FREEZE_NOTE.md" in note,
    )

    print()
    print("C. Current ledger row before pipeline")
    print("-" * 72)
    check("row is audited_conditional before repair pipeline", row.get("audit_status") == "audited_conditional", str(row.get("audit_status")))
    check("auditor already classified row as meta", row.get("claim_type") == "meta", str(row.get("claim_type")))
    check(
        "row records missing recomputation blocker",
        "live retained-generator" in (row.get("notes_for_re_audit_if_any") or "")
        or "live retained-generator" in (row.get("chain_closure_explanation") or ""),
    )

    print()
    print("Summary")
    print("-" * 72)
    print(f"TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    if FAIL_COUNT == 0:
        print("VERDICT: row is ready to leave the conditional backlog as metadata.")
        return 0
    print("VERDICT: unified-basin metadata repair checks failed.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
