#!/usr/bin/env python3
"""J:attack-b:PR8171 — SAME TEST, BOTH SIDES: contraction threshold.

Identical test: n * (beta/sqrt(3)) < 1 with the T1 per-neighbour constant
beta/sqrt(3). Formation n=3 => beta < 1/sqrt(3). Static n=6 => beta < sqrt(3)/6.
HIT if the two thresholds agree or the algebra is wrong.
"""
from __future__ import annotations

import sympy as sp

beta = sp.symbols("beta", positive=True)
c = beta / sp.sqrt(3)
form = sp.simplify(sp.Lt(3 * c, 1))
stat = sp.simplify(sp.Lt(6 * c, 1))
thr_f = sp.simplify(1 / sp.sqrt(3))
thr_s = sp.simplify(sp.sqrt(3) / 6)
print(f"formation 3c<1 iff beta < {thr_f} = {sp.N(thr_f)}")
print(f"static    6c<1 iff beta < {thr_s} = {sp.N(thr_s)}")
print(f"thr_f/thr_s = {sp.simplify(thr_f / thr_s)}")
same = sp.simplify(thr_f - thr_s) == 0
if same:
    print("HIT: formation and static thresholds coincide; neighbor-count does not separate")
    print("SUMMARY: SAME TEST BOTH SIDES (PR #8171): 3c<1 and 6c<1 give the same beta threshold")
else:
    print(
        "SUMMARY: SAME TEST BOTH SIDES on n*(beta/sqrt(3))<1 (PR #8171): formation "
        "n=3 gives beta<1/sqrt(3) and static n=6 gives beta<sqrt(3)/6; the "
        "thresholds differ by 2 and the separation holds as written"
    )
