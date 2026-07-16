#!/usr/bin/env python3
"""Cycle 165: verify whole-row payload taps beside both retained row readers."""

from __future__ import annotations

from pathlib import Path

import physical_row_reader_payload_tap_probe_2026_07_16 as p


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "PHYSICAL_ROW_READER_PAYLOAD_TAP_CYCLE165_NOTE_2026-07-16.md"
)
PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0

    print("AUTHORITY AND LAW")
    check("Cycle-165 review note exists", NOTE.is_file())
    check(
        "32 canonical tap rows add 768 disjoint cubic rows",
        len(p.TAP_TABLE) == 32
        and len(p.TAP_RAW) == 768
        and set(p.TAP_RAW).isdisjoint(p.prior.MERGED_RAW),
        (len(p.TAP_TABLE), len(p.TAP_RAW)),
    )
    check(
        "the 97,388-row candidate law is deterministic",
        len(p.prior.MERGED_RAW) == 96_620
        and len(p.MERGED_RAW) == 97_388
        and not p.RAW_CONFLICTS
        and all(len(outputs) == 1 for outputs in p.MERGED_RAW.values()),
        len(p.MERGED_RAW),
    )

    print("\nEXHAUSTIVE READER/TAP COMPOSITION")
    check("the complete reader/tap probe is green", p.main() == 0)

    print("\nSCOPE")
    note = (
        " ".join(NOTE.read_text(encoding="utf-8").lower().split())
        if NOTE.is_file()
        else ""
    )
    for phrase in (
        "one covariant whole-row tap",
        "4,375",
        "deleting the sole physical row source",
        "closes the last distinct interface mechanism",
        "one joint geometric placement",
        "does not claim that placement is already complete",
        "no axiom, primitive, registry, policy, or audit edit follows",
    ):
        check("note contains: " + phrase, phrase in note)

    print("\nTOTAL")
    print("PASS", PASS, "FAIL", FAIL)
    print("RESULT", "PHYSICAL_ROW_READER_PAYLOAD_TAP" if FAIL == 0 else "FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
