#!/usr/bin/env python3
"""J:attack-d:PR8171 — QUANTIFIER SCOPE.

T1(c) claims 1-3A/κ-A²≤0 and A/κ≤1/3 for every κ>0 (series executed at
low m). Check (m/2-1)≥0 in the difference series for m=2..60, A/κ≤1/3 on
a grid of κ, and √3 β<1 iff β²<1/3 at the note's 5773/10^4 vs 5774/10^4.
"""
from __future__ import annotations

import math
from fractions import Fraction

import mpmath as mp

HITS = []
mp.mp.dps = 40


def main():
    for m in range(2, 61):
        coef = Fraction(m, 2) - 1
        if coef < 0:
            HITS.append(f"series coef m={m} {coef} < 0")
            break
        # 2^{2m}/(2m)! * coef
        term = (Fraction(2) ** (2 * m) / math.factorial(2 * m)) * coef
        if term < 0:
            HITS.append(f"term m={m} {term} < 0")
            break
    print("series (m/2-1)≥0 for m=2..60: True" if not HITS else "series failed")

    third = mp.mpf(1) / 3
    ks = [mp.mpf(n) / 20 for n in range(1, 201)] + [mp.mpf(n) for n in range(11, 41)]
    for k in ks:
        A = mp.coth(k) - 1 / k
        if A / k > third + mp.mpf("1e-20"):
            HITS.append(f"A/κ={A/k} > 1/3 at κ={k}")
            break
        sign = 1 - 3 * A / k - A * A
        if sign > mp.mpf("1e-20"):
            HITS.append(f"1-3A/κ-A²={sign} > 0 at κ={k}")
            break
    else:
        print(f"A/κ≤1/3 and sign lemma on {len(ks)} points: True")

    lo, hi = Fraction(5773, 10000), Fraction(5774, 10000)
    thresh2 = Fraction(1, 3)
    print(f"β=5773/10^4: β²={lo*lo} vs 1/3={thresh2}  β²<1/3 {lo*lo < thresh2}")
    print(f"β=5774/10^4: β²={hi*hi} vs 1/3={thresh2}  β²<1/3 {hi*hi < thresh2}")
    if not (lo * lo < thresh2):
        HITS.append("5773/10^4 not below 1/√3")
    if hi * hi < thresh2:
        HITS.append("5774/10^4 still below 1/√3")

    if HITS:
        print("HIT: " + "; ".join(HITS))
        print("SUMMARY: attack pattern (d) QUANTIFIER SCOPE - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - series coefficients "
        "(m/2-1) stay ≥0 through m=60; A/κ≤1/3 and the sign lemma hold on a "
        "grid of κ∈(0,40]; 5773/10^4 sits below 1/√3 and 5774/10^4 above"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
