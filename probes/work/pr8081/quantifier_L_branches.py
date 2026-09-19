#!/usr/bin/env python3
"""J:attack-d:PR8081 — QUANTIFIER SCOPE on L(E,F) for all E,F>=0.

Note: L(E,F)=-3E²-3EF (F<=2E); -6E²-3F²/4 (2E<=F<=4E); 6E²-6EF (F>=4E),
from min_{m∈[-3,6], a∈[0,E]} a²m - a F sqrt(3m+18). Check the claimed
formula against that min on a grid of (E,F) inside the three regimes.
HIT if a grid point in the stated range misses the min.
"""
from __future__ import annotations

import sys
from fractions import Fraction as Fr
from math import sqrt

import sympy as sp


def hits(msg: str) -> int:
    print(f"HIT: {msg}")
    print(f"SUMMARY: HIT - {msg}")
    return 0


def L_note(E, F):
    if F <= 2 * E:
        return -3 * E * E - 3 * E * F
    if F <= 4 * E:
        return -6 * E * E - 3 * F * F / 4
    return 6 * E * E - 6 * E * F


def f(a, m, F):
    return a * a * m - a * F * sqrt(3 * m + 18)


def min_num(E, F, n_a=40, n_m=80):
    best = None
    for i in range(n_a + 1):
        a = E * i / n_a
        for j in range(n_m + 1):
            m = -3 + 9 * j / n_m
            val = f(a, m, F)
            if best is None or val < best:
                best = val
    return best


def main() -> int:
    E = Fr(1)
    # endpoints
    for F in (Fr(0), Fr(2), Fr(4), Fr(6), Fr(1), Fr(3), Fr(8)):
        Ln = L_note(E, F)
        mn = min_num(float(E), float(F))
        print(f"E=1 F={F} L_note={float(Ln):.6f} gridmin={mn:.6f} diff={mn-float(Ln):.6f}")
        if mn < float(Ln) - 1e-4:
            return hits(f"grid min {mn} < L_note {Ln} at F={F} (formula not a lower bound)")
        # formula should be the exact min; grid is slightly above
        if float(Ln) < mn - 0.05:
            return hits(f"L_note {Ln} much below grid min {mn} at F={F}")

    # T^2 <= 3T+18I on the actual 15x15 T
    from itertools import combinations
    edges = list(combinations(range(6), 2))
    T = sp.zeros(15)
    for i, a in enumerate(edges):
        for j, b in enumerate(edges):
            if i != j and set(a).isdisjoint(b):
                T[i, j] = 1
    M = T ** 2 - 3 * T - 18 * sp.eye(15)
    ev = M.eigenvals()
    if any(sp.N(lam) > 1e-10 for lam in ev):
        return hits(f"T^2-3T-18I has positive eigenvalue {ev}")
    print("T^2 <= 3T+18I on K6 disjoint-pair T: True")

    # lambda scales {0,1/2,1,3/2,2} all in the dual clamp [0,4]
    for lam in (Fr(0), Fr(1, 2), Fr(1), Fr(3, 2), Fr(2)):
        if lam < 0 or lam > 4:
            return hits(f"lambda={lam} outside stated clamp [0,4]")
    print("five lambda scales lie in [0,4]: True")

    print(
        "SUMMARY: pattern has no purchase on this note: L(E,F) matches the "
        "enumerated min on all three F/E regimes, T^2<=3T+18I holds, and the "
        "lambda grid sits inside the stated clamp"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
