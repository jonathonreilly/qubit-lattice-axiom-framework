#!/usr/bin/env python3
"""J:attack-f:PR8176 — NORMALIZATION.

No Fourier / 2π / conjugation. The 1/2 and generating-function factors
that are present: max_t t(4/27-t)=4/729 at t=2/27; affine min at c=3/4
is 3/2 given 6 at c=0 and 0 at c=1; d3 crosses 4/729 between 367 and 368.
"""
from fractions import Fraction as Fr

import sympy as sp


def d3(p):
    return Fr(2 * p + 11, p * p + 2 * p + 11)


def main() -> int:
    hits = []
    t = sp.symbols("t", positive=True)
    f = t * (sp.Rational(4, 27) - t)
    crit = sp.solve(sp.diff(f, t), t)
    print(f"critical points of t(4/27-t): {crit}")
    if sp.Rational(2, 27) not in crit:
        hits.append(f"critical point {crit} != 2/27")
    val = sp.simplify(f.subs(t, sp.Rational(2, 27)))
    print(f"max t(4/27-t)={val} (stated 4/729)")
    if val != sp.Rational(4, 729):
        hits.append(f"max={val} != 4/729")

    # affine interpolation of T2.1 min: 6 at c=0, 0 at c=1 => at 3/4 is 3/2
    m = 6 * (1 - Fr(3, 4))
    print(f"affine min at c=3/4: {m} (stated 3/2)")
    if m != Fr(3, 2):
        hits.append(f"3/2 interpolation {m}")

    thresh = Fr(4, 729)
    print(f"d3(367)={d3(367)} >4/729? {d3(367) > thresh}")
    print(f"d3(368)={d3(368)} >4/729? {d3(368) > thresh}")
    if not (d3(367) > thresh):
        hits.append("d3(367) is not > 4/729")
    if not (d3(368) <= thresh):
        hits.append("d3(368) is not <= 4/729")

    # recursion domain x<4/27: (1+xU)^2 factor is a square, not a 1/2
    print("recursion (1+xU)^2 is a square, not a Fourier 1/2")

    if hits:
        for h in hits:
            print("HIT:", h)
        print("SUMMARY: pattern (f) NORMALIZATION fired; " + "; ".join(hits))
        return 0
    print(
        "SUMMARY: pattern (f) NORMALIZATION — no Fourier/2π/conjugation; "
        "max t(4/27-t)=4/729 at t=2/27, affine 3/2 at c=3/4, and d3 crosses "
        "4/729 between 367 and 368, all exact; attack does not fire"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
