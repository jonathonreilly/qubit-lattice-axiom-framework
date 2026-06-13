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
        "status is scoped to determinant-character / group-homomorphic subclass",
        "determinant-character / group-homomorphic phase-readout\nsubclass" in text,
    )
    check(
        "H_char is explicit and not derived from Record additivity",
        "**(H_char)**" in text
        and "Record\nfinite additivity over disjoint record collections does **not** by itself imply\nH_char"
        in text,
    )
    check(
        "non-homomorphic K-even counterexample is preserved",
        "sum_{j in S} cos(theta_j)" in text
        and "finite-additive over disjoint record collections" in text
        and "phase-dependent" in text,
    )
    check(
        "theorem statement requires H_char",
        "Suppose in addition that the phase part is restricted to H_char" in text
        and "inside this restricted\n> subclass" in text,
    )
    check(
        "Consequence A is restricted to determinant-character content",
        "discharges only the determinant-character phase content" in text
        and "does not address\naction-level data outside H_char" in text,
    )
    check(
        "Consequence B is restricted to symmetric-function / H_char content",
        "inside the symmetric-function / H_char readout subclass" in text
        and "magnitude-only atom `|delta|` only on that restricted\nsurface" in text,
    )
    check(
        "non-claim bullet excludes Record-alone restriction",
        "does **not** prove Record finite additivity alone restricts phase readouts" in text
        and "does **not**\n  exclude non-homomorphic per-sector `K`-even phase data" in text,
    )
    forbidden = [
        "uses only (Additivity) and (Orbit); it adds nothing",
        "no separately-registrable non-multiplicative\nphase datum survives",
        "A non-additive\nreadout is simply not Record-registrable",
        "theorem removes phase freedom *within* that class",
    ]
    check(
        "old broad Record-alone language is absent",
        not any(s in text for s in forbidden),
    )

    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
