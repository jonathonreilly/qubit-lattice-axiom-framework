#!/usr/bin/env python3
"""J:attack-g:PR8177 — brute-force T3.1 up-factor identity.

Note T3.1: for n successor positions each empty, processed (weight x_P U) or
amplified (weight x_A U), the sum over configurations with at most one
processed child is (1 + x_A U)^n + n x_P U (1 + x_A U)^{n-1}.

Enumerate all 3^n assignments for n=1..6; compare the generating function
(exact integer monomials) to the closed form. HIT if they differ. Not the
known T2 predecessor-value HIT.
"""
from __future__ import annotations

from itertools import product

import sympy as sp

xP, xA, U = sp.symbols("x_P x_A U")
E, P, A = "E", "P", "A"


def enum_factor(n: int):
    acc = 0
    for cfg in product((E, P, A), repeat=n):
        nP = cfg.count(P)
        if nP > 1:
            continue
        nA = cfg.count(A)
        acc += (xP * U) ** nP * (xA * U) ** nA
    return sp.expand(acc)


def claimed(n: int):
    return sp.expand((1 + xA * U) ** n + n * xP * U * (1 + xA * U) ** (n - 1))


def main():
    bad = []
    for n in range(1, 7):
        a, b = enum_factor(n), claimed(n)
        ok = sp.simplify(a - b) == 0
        print(f"n={n}  3^{n}={3**n} configs  identity={ok}")
        if not ok:
            bad.append((n, a, b))
            print(f"  enum {a}")
            print(f"  claimed {b}")
    if bad:
        n, a, b = bad[0]
        print(f"HIT: T3.1 up-factor fails at n={n}: enum {a} != claimed {b}")
        print(
            "SUMMARY: PROOF STEP BY BRUTE FORCE on T3.1 up-factor (PR #8177): "
            f"enumeration of 3^n successor configs disagrees with the closed form at n={n}"
        )
    else:
        print(
            "SUMMARY: PROOF STEP BY BRUTE FORCE on T3.1 up-factor (PR #8177): "
            "enumerating all 3^n successor configs with at most one processed child "
            "matches (1+x_A U)^n + n x_P U (1+x_A U)^{n-1} for n=1..6; "
            "pattern has purchase and the step holds as written"
        )


if __name__ == "__main__":
    main()
