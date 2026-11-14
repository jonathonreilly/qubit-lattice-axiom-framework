#!/usr/bin/env python3
"""tw1b -- display-only re-run of tw1-G, which aborted in tw1_feas.py.

tw1_feas.py line 202 raised TypeError building Fraction(1, 3**(-e)) for a
non-integer exponent e. That is a DISPLAY defect in the last block only: gates
tw1-A, tw1-B, tw1-B', tw1-C, tw1-D, tw1-D', tw1-E and tw1-F had all completed
and printed before it (see tw1_out.txt, kept unaltered, and tw1_err.txt).
No criterion is changed; tw1_criteria.md is untouched. This file re-prints
tw1-G only, with exact rationals where the exponent is an integer and the
exponent itself otherwise. No new verdict is defined here.
"""
from fractions import Fraction as F

def A_exponent(d, tr, tA):
    return d - tr - 2 * tA

print("[tw1-G, re-run] A = L^{d - theta_w^r - 2 theta_A} at d = 4, L = 3")
rows = [("data-only            tr = 3", F(3)),
        ("nonlinear  theta=1/2 tr = 5/2", F(5, 2)),
        ("nonlinear  theta=1/4 tr = 9/4", F(9, 4)),
        ("nonlinear  theta=1/12 tr=25/12", F(25, 12)),
        ("boundary             tr = 2", F(2))]
for name, tr in rows:
    e = A_exponent(4, tr, F(1))
    if e.denominator == 1:
        val = F(3) ** int(e)
        print(f"  {name:>30}: exponent {e},  A = 3^({e}) = {val}  "
              f"[{'contraction' if val < 1 else 'NOT a contraction'}]")
    else:
        # exact statement without evaluating an irrational: bracket by integers
        lo, hi = -(-e.numerator // e.denominator), e.numerator // e.denominator
        print(f"  {name:>30}: exponent {e},  A = 3^({e}),  "
              f"3^{min(0, hi)} > A > 3^{e - 1} ; "
              f"{'contraction' if e < 0 else 'NOT a contraction'}")
print("  Reading: with the nonlinear-source cap theta_w^r = 2 + theta and "
      "theta_A = 1,")
print("           A = L^{4 - (2+theta) - 2} = L^{-theta}.  "
      "A < 1 <=> theta > 0; A = 1/L only at theta = 1, which is excluded.")
