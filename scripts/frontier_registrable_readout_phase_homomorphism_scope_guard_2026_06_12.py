#!/usr/bin/env python3
"""Scope guard for the registrable-readout phase theorem."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_"
    "2026-06-10.md"
)

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS: {name}")
    else:
        FAIL += 1
        print(f"FAIL: {name}")
    if detail:
        print(f"      {detail}")


def main() -> int:
    text = NOTE.read_text(encoding="utf-8")

    check(
        "status is scoped to determinant-character / log-character homomorphism class",
        "Record-registrable determinant-character / log-character\nhomomorphism readout class" in text,
    )
    check(
        "homomorphism boundary is explicit and not derived from Record",
        "determinant-character / log-character homomorphism boundary" in text
        and "as part of the supplied readout context and **not** as\na consequence of Record" in text,
    )
    check(
        "non-homomorphic K-even counterexample is preserved",
        "sum_j cos(theta_j)" in text
        and "finite additivity alone still admits K-even phase-dependent functions" in text
        and "excluded only by" in text
        and "determinant-character / log-character homomorphism boundary" in text,
    )
    check(
        "theorem statement requires the homomorphism boundary",
        "Suppose in addition that its determinant phase-bearing component is a\n> determinant-character / log-character homomorphism" in text
        and "that homomorphic per-sector **phase** contribution is identically zero" in text,
    )
    check(
        "Conditional Implication A does not discharge the bridge",
        "This is a conditional algebraic implication, not a bridge discharge" in text
        and "a separate retained theorem still has to\nidentify the physical mass-orientation readout" in text,
    )
    check(
        "Conditional Implication B is restricted to supplied unordered-multiset orbit data",
        "inside the supplied Record-registrable unordered-multiset context" in text
        and "does not by itself reduce the physical\nAC_phi_lambda admission to the magnitude-only atom `|delta|`" in text,
    )
    check(
        "boundary excludes Record-alone phase-group additivity",
        "It does **not** derive phase-group additivity from\nRecord finite additivity" in text
        and "Record finite additivity alone" in text,
    )
    forbidden = [
        "uses only (Additivity) and (Orbit); it adds nothing",
        "no separately-registrable non-multiplicative\nphase datum survives",
        "A non-additive\nreadout is simply not Record-registrable",
        "discharges only the determinant-character phase content",
        "inside the symmetric-function / H_char readout subclass",
    ]
    check(
        "old broad Record-alone language is absent",
        not any(s in text for s in forbidden),
    )

    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
