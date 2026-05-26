#!/usr/bin/env python3
"""Formal-ratio repair runner for the Koide Q-delta linking row.

This runner checks only the exact rational identity:

    Q_d = 2/d, Delta_d = 2/d^2  =>  Delta_d = Q_d/d.

It explicitly avoids the radian/Berry-holonomy bridge, equal-sector-norm
selector, PDG comparators, and any physical charged-lepton claim.
"""

from __future__ import annotations

import json
import sys
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NOTE_PATH = ROOT / "docs" / "KOIDE_Q_DELTA_LINKING_RELATION_THEOREM_NOTE_2026-04-20.md"
LEDGER_PATH = ROOT / "docs" / "audit" / "data" / "audit_ledger.json"
CLAIM_ID = "koide_q_delta_linking_relation_theorem_note_2026-04-20"
RUNNER_PATH = "scripts/frontier_koide_q_delta_formal_ratio_repair.py"

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    status = "PASS" if ok else "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"  [{status}] {label}{suffix}")


def section(title: str) -> None:
    print("\n" + "=" * 88)
    print(title)
    print("=" * 88)


def q_d(d: int) -> Fraction:
    return Fraction(2, d)


def delta_d(d: int) -> Fraction:
    return Fraction(2, d * d)


def q_alt(d: int) -> Fraction:
    return Fraction(d - 1, d)


def check_note_boundary() -> None:
    section("Source-note boundary")
    text = NOTE_PATH.read_text()
    required = [
        "bounded-support formal algebra",
        "No Berry-holonomy radian bridge",
        "That exact rational identity is the entire repaired theorem.",
        "This repair withdraws both from the binding claim.",
        "The bridge from this formal algebra to physical Koide/Brannen geometry remains a separate open science problem.",
    ]
    for needle in required:
        check(f"note contains required boundary: {needle!r}", needle in text)

    forbidden = [
        "uses PDG",
        "matches observed",
        "observed charged-lepton",
        "retained selected-line",
        "Berry holonomy in radians is derived",
        "equal-sector-norm input is retained",
    ]
    for needle in forbidden:
        check(f"note avoids overclaim/token: {needle!r}", needle not in text)


def check_exact_identity() -> None:
    section("Exact rational identity")
    for d in [1, 2, 3, 4, 5, 7, 11, 17, 32]:
        q = q_d(d)
        delta = delta_d(d)
        check(f"d={d}: Delta_d = Q_d/d", delta == q / d, f"Delta={delta}, Q/d={q/d}")
        check(f"d={d}: Delta_d/Q_d = 1/d", delta / q == Fraction(1, d), f"ratio={delta/q}")


def check_d3_values() -> None:
    section("d=3 exact values")
    check("Q_3 = 2/3", q_d(3) == Fraction(2, 3), str(q_d(3)))
    check("Delta_3 = 2/9", delta_d(3) == Fraction(2, 9), str(delta_d(3)))
    check("Delta_3 / Q_3 = 1/3", delta_d(3) / q_d(3) == Fraction(1, 3), str(delta_d(3) / q_d(3)))


def check_negative_control() -> None:
    section("Negative control: alternative Q'_d=(d-1)/d")
    for d in [2, 4, 5, 7, 11, 17]:
        check(
            f"d={d}: alternative Q'_d/d does not equal Delta_d",
            delta_d(d) != q_alt(d) / d,
            f"Delta={delta_d(d)}, Q_alt/d={q_alt(d)/d}",
        )
    check("d=3 is the unique tested coincidence for Q'_d=2/d", q_alt(3) == q_d(3), f"Q_alt(3)={q_alt(3)}")


def check_audit_metadata_after_pipeline() -> None:
    section("Audit metadata after pipeline regeneration")
    if not LEDGER_PATH.exists():
        check("audit ledger exists", False, str(LEDGER_PATH))
        return
    ledger = json.loads(LEDGER_PATH.read_text())
    row = ledger.get("rows", {}).get(CLAIM_ID)
    check(f"{CLAIM_ID} row exists", row is not None)
    if row is None:
        return
    check("claim_type is bounded_theorem", row.get("claim_type") == "bounded_theorem", str(row.get("claim_type")))
    check("audit_status reset to unaudited", row.get("audit_status") == "unaudited", str(row.get("audit_status")))
    check("effective_status reset to unaudited", row.get("effective_status") == "unaudited", str(row.get("effective_status")))
    check("runner path is formal-ratio repair runner", row.get("runner_path") == RUNNER_PATH, str(row.get("runner_path")))
    check("direct deps are empty for formal identity", row.get("deps") == [], str(row.get("deps")))
    check("open dependency paths are empty", row.get("open_dependency_paths") == [], str(row.get("open_dependency_paths")))


def main() -> int:
    print("Koide Q-delta formal ratio repair")
    check_note_boundary()
    check_exact_identity()
    check_d3_values()
    check_negative_control()
    check_audit_metadata_after_pipeline()
    print("\n" + "=" * 88)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
