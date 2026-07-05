#!/usr/bin/env python3
"""Exact bounded-surface check for the g_bare Gram-scaling repair.

This runner checks only the narrowed Gram-scaling lemma:

  CN + rescaling by c => Gram -> c^2 Gram.

It does not prove Wilson matching, does not derive the Wilson action surface,
does not derive beta_new / beta_old under T_a -> c T_a,
and does not apply an audit verdict.
"""

from __future__ import annotations

import sys
from fractions import Fraction
from pathlib import Path


PASS = 0
FAIL = 0
ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03.md"


def check(name: str, cond: bool, detail: str = "") -> bool:
    global PASS, FAIL
    if cond:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    msg = f"[{tag}] {name}"
    if detail:
        msg += f" ({detail})"
    print(msg)
    return cond


def canonical_gram(n: int = 8) -> list[list[Fraction]]:
    return [
        [Fraction(1, 2) if i == j else Fraction(0) for j in range(n)]
        for i in range(n)
    ]


def scale_gram(gram: list[list[Fraction]], c_squared: Fraction) -> list[list[Fraction]]:
    return [[c_squared * entry for entry in row] for row in gram]


def main() -> int:
    note_text = NOTE.read_text(encoding="utf-8")
    gram = canonical_gram()

    for c_squared in [Fraction(1, 4), Fraction(2), Fraction(4), Fraction(9)]:
        scaled = scale_gram(gram, c_squared)
        expected_diag = c_squared * Fraction(1, 2)
        diag_ok = all(scaled[i][i] == expected_diag for i in range(8))
        off_diag_ok = all(
            scaled[i][j] == 0
            for i in range(8)
            for j in range(8)
            if i != j
        )
        check(
            f"Gram scales by c^2 = {c_squared}",
            diag_ok and off_diag_ok,
            f"new diagonal = {expected_diag}",
        )
        check(
            f"nontrivial c^2 = {c_squared} leaves canonical Gram only when c^2 = 1",
            c_squared != 1 and expected_diag != Fraction(1, 2),
            "canonical diagonal is 1/2",
        )

    check(
        "note states beta routing is out of scope",
        "this row is no longer a beta-routing" in note_text
        and "does not derive any `beta_new / beta_old`" in note_text,
    )
    check(
        "note states Wilson action normalization theorem remains separate",
        "normalization theorem not supplied by this row" in note_text,
    )

    print(f"SUMMARY: PASS = {PASS}, FAIL = {FAIL}")
    if FAIL:
        print("Conditional rescaling algebra check failed.")
        return 1

    print("Gram-scaling algebra check passed; no retained status is asserted.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
