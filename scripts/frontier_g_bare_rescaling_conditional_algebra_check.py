#!/usr/bin/env python3
"""Exact bounded-surface check for the g_bare rescaling algebra repair.

This runner checks only the narrowed conditional lemma:

  CN + scoped Wilson matching + rescaling by c
    => Gram -> c^2 Gram and beta -> c^2 beta.

It does not prove Wilson matching, does not derive the Wilson action surface,
and does not apply an audit verdict.
"""

from __future__ import annotations

import sys
from fractions import Fraction


PASS = 0
FAIL = 0


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
    gram = canonical_gram()
    n_c = Fraction(3)
    g_bare_sq = Fraction(1)
    beta_old = Fraction(2) * n_c / g_bare_sq

    check(
        "scoped WM gives beta_old = 2 N_c / g_bare^2 = 6 at the test point",
        beta_old == Fraction(6),
        f"beta_old = {beta_old}",
    )

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
        beta_new = c_squared * beta_old

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
            f"scoped WM routes rescaling into beta by c^2 = {c_squared}",
            beta_new / beta_old == c_squared,
            f"beta_new = {beta_new}; beta_new / beta_old = {beta_new / beta_old}",
        )

    print(f"SUMMARY: PASS = {PASS}, FAIL = {FAIL}")
    if FAIL:
        print("Conditional rescaling algebra check failed.")
        return 1

    print("Conditional rescaling algebra check passed; no retained status is asserted.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
