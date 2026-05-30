#!/usr/bin/env python3
"""Metadata-boundary checker for the unified-basin signed-source salvage row."""

from __future__ import annotations

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "UNIFIED_BASIN_SIGNED_SOURCE_CONTROL_SUPPORT_NOTE_2026-04-30.md"

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


def has_phrase(text: str, phrase: str) -> bool:
    return " ".join(phrase.split()) in " ".join(text.split())


def main() -> int:
    print("Unified basin signed-source metadata repair")
    print("=" * 72)

    note = NOTE.read_text(encoding="utf-8")

    print()
    print("A. Metadata boundary")
    print("-" * 72)
    check("note declares claim_type meta", "**Claim type:** meta" in note)
    check("note declares this metadata checker", "**Primary runner:** `scripts/unified_basin_signed_source_metadata_check.py`" in note)
    check("note no longer declares bounded_theorem", "**Claim type:** bounded_theorem" not in note)
    check("note does not carry branch-local status authority", "Status authority" not in note)
    check(
        "note says it carries no independent evidence",
        has_phrase(note, "carries no independent audit-grade evidence"),
    )
    check(
        "note says archive pointer is not load-bearing",
        has_phrase(note, "route-history provenance rather than a cited dependency")
        and has_phrase(note, "not load-bearing authority"),
    )
    check(
        "note keeps future runner as separate science",
        has_phrase(note, "future science repair may build a fresh retained-generator runner"),
    )
    check(
        "note explicitly says this metadata row is not numerical support",
        has_phrase(note, "not numerical support and not a theorem-like positive claim"),
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
