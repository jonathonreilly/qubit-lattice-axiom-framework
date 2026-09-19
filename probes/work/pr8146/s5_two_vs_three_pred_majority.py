#!/usr/bin/env python3
"""J:attack-b:PR8146 — SAME TEST, BOTH SIDES on S5's 2D-vs-3D majority.

S5: 2D two-predecessor kernel r(s|a,b) for a!=b gives equal weight to s=a
and s=b (no majority). S2/S6: 3D three-predecessor majority. Identical test:
is the mode of r(·| recorded set) the majority value of the recorded set?

Not the known HIT (2:1 most likely iff p>max(q,r) fails at (5,2,4) antipodal).
"""
from __future__ import annotations

from fractions import Fraction as F

VALS = ("+x", "-x", "+y", "-y", "+z", "-z")
OPP = {"+x": "-x", "-x": "+x", "+y": "-y", "-y": "+y", "+z": "-z", "-z": "+z"}


def K(p, q, r, s, t):
    if s == t:
        return p
    if OPP[s] == t:
        return q
    return r


def rcond(p, q, r, rec, s):
    num = 1
    for a in rec:
        num *= K(p, q, r, s, a)
    den = 0
    for t in VALS:
        pr = 1
        for a in rec:
            pr *= K(p, q, r, t, a)
        den += pr
    return F(num, den)


def main():
    p, q, r = 3, 1, 2  # not the known (5,2,4) witness
    a, b = "+x", "+y"  # orthogonal 2-pred disagreement
    w2_a = rcond(p, q, r, (a, b), a)
    w2_b = rcond(p, q, r, (a, b), b)
    print(f"2D r(+x|+x,+y)={w2_a} r(+y|+x,+y)={w2_b} equal={w2_a==w2_b}")

    # 3D 2:1 orthogonal (a,a,b)
    w3_a = rcond(p, q, r, (a, a, b), a)
    w3_b = rcond(p, q, r, (a, a, b), b)
    print(f"3D r(+x|+x,+x,+y)={w3_a} r(+y|...)={w3_b} majority_a={w3_a>w3_b}")

    # 3D 2:1 antipodal at (3,1,2) — not the known (5,2,4) failure
    am = "-x"
    w3p = rcond(p, q, r, (a, a, am), a)
    w3m = rcond(p, q, r, (a, a, am), am)
    print(f"3D r(+x|+x,+x,-x)={w3p} r(-x|...)={w3m} majority_a={w3p>w3m}")

    # The test separates 2D (tie) from 3D (majority) at (3,1,2)
    if w2_a == w2_b and w3_a > w3_b and w3p > w3m:
        print(
            "SUMMARY: SAME TEST BOTH SIDES on 2-pred vs 3-pred majority (PR #8146): "
            "at (3,1,2) the identical mode-of-r test finds a 2D a!=b tie and a 3D "
            "2:1 majority (orthogonal and antipodal); the known (5,2,4) antipodal "
            "counterexample is not re-found; the separation holds as written"
        )
    else:
        print(
            "HIT: at (3,1,2) the mode-of-r test does not separate 2D ties from 3D majority "
            f"2D equal={w2_a==w2_b} 3D orth={w3_a>w3_b} 3D anti={w3p>w3m}"
        )
        print(
            "SUMMARY: SAME TEST BOTH SIDES (PR #8146): 2-pred vs 3-pred majority test "
            "failed to separate at (3,1,2)"
        )


if __name__ == "__main__":
    main()
