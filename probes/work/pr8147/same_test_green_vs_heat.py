#!/usr/bin/env python3
"""J:attack-b:PR8147 — pattern (b) SAME TEST, BOTH SIDES.

Same test: does the two-point diagonal series converge like a 3d Green
function? Static p_{2n}=C(2n,n)/4^n P_n; formation uses P_n. At n=1,
P_1=1/3 while p_2=C(2,1)/4 * 1/3 wait C(2,1)=2 so 1/6. They differ.
Do not re-find T3(ii) u^2.
"""
from __future__ import annotations

from fractions import Fraction as F
from math import comb

HITS = []


def P1():
    # two independent 1-steps agree: 3/9=1/3
    return F(1, 3)


def main():
    pn = P1()
    p2 = F(comb(2, 1), 4) * pn  # note uses C(2n,n); n=1 C(2,1)=2
    # actually C(2n,n)=C(2,1)=2 is WRONG for central binomial: C(2,1)=2 but C(2n,n)=C(2,1)? n=1, 2n=2, C(2,1)=2 vs C(2,1). Wait C(2,1)=2, C(2,0)=1, C(2,2)=1. CENTRAL is C(2,1)=2. Yes.
    # Standard C(2,1)=2. p_2 = 2/4 * 1/3 = 1/6.
    print(f"P_1={pn}  p_2=C(2,1)/4 P_1={p2}")
    # formation series term P_n; static term p_{2n}
    form_term = pn
    stat_term = p2
    print(f"same n=1 diagonal term: formation {form_term} static {stat_term}")
    if form_term == stat_term:
        HITS.append("n=1 terms do not separate")
    if HITS:
        print("HIT: " + "; ".join(HITS))
        print("SUMMARY: attack pattern (b) SAME TEST BOTH SIDES - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - the same n=1 diagonal "
        "term is P_1=1/3 for formation and p_2=1/6 for the static walk; they "
        "separate. Not a re-find of T3(ii) u^2"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
