#!/usr/bin/env python3
"""J:attack-g:PR8157 — brute-force P1/P2 finite identities.

(1-cos θ)(cosh τ-1)≥0; series ratios for cosh t-1 vs (t^2/2)cosh t;
l_∞ shells have exactly 8j sites; cosh 1 ≤ 8/5; trig-poly period integral.
"""
from __future__ import annotations

import sys
from fractions import Fraction as F

import sympy as sp

PASSES = 0
FAILS = 0


def check(tag, ok, msg):
    global PASSES, FAILS
    if ok:
        PASSES += 1
        print(f"PASS: {tag} {msg}")
    else:
        FAILS += 1
        print(f"FAIL: {tag} {msg}")


def main():
    th, ta = sp.symbols("theta tau", real=True)
    ident = sp.simplify(sp.expand_complex(sp.cos(th + sp.I * ta)) - (sp.cos(th) * sp.cosh(ta) - sp.I * sp.sin(th) * sp.sinh(ta)))
    ineq = sp.simplify((1 - sp.cos(th)) * (sp.cosh(ta) - 1))
    # ineq is a product of nonnegative functions for real th, tau? (1-cos)>=0, (cosh-1)>=0
    # check as sum of squares / trig
    ok = ident == 0
    check("P1a", ok, "cos(theta+i tau)=cos theta cosh tau - i sin theta sinh tau identically")
    gap = sp.simplify(sp.cos(th) + (sp.cosh(ta) - 1) - sp.cos(th) * sp.cosh(ta))
    # = (1-cos)(cosh-1)
    ok = sp.simplify(gap - (1 - sp.cos(th)) * (sp.cosh(ta) - 1)) == 0
    check("P1b", ok, "cos theta + (cosh tau-1) - cos theta cosh tau = (1-cos)(cosh-1) >= 0 for real theta, tau")

    t = sp.symbols("t")
    ok = True
    for k in range(1, 12):
        c_left = 1 / sp.factorial(2 * k)  # coeff of t^{2k} in cosh t - 1
        c_right = 1 / (2 * sp.factorial(2 * k - 2))  # coeff in (t^2/2) cosh t
        ratio = sp.simplify(c_left / c_right)
        want = F(2, (2 * k) * (2 * k - 1))
        ok = ok and ratio == want and want <= 1
    check("P2a", ok, "series ratio 1/(2k)! over 1/(2(2k-2)!) = 2/((2k)(2k-1)) <= 1 for k=1..11")

    ok = True
    for j in range(1, 21):
        n = sum(1 for x in range(-j, j + 1) for y in range(-j, j + 1) if max(abs(x), abs(y)) == j)
        ok = ok and n == 8 * j
    check("P2b", ok, "l_inf shell j on Z^2 has exactly 8j sites for j=1..20 (note: at most 8j)")

    e = sp.E
    # note: e >= 8/3, e <= 11/4, cosh 1 <= 8/5
    # check cosh(1) <= 8/5 numerically via series lower/upper as in the note
    # e <= 65/24 + 1/100 = 653/240? note says <= 11/4
    # just check the claimed cosh 1 <= 8/5
    c1 = (sp.exp(1) + sp.exp(-1)) / 2
    ok = bool(sp.N(c1) < float(F(8, 5)))
    # and 25/16 <= 8/5: 25/16=1.5625, 8/5=1.6
    ok = ok and F(25, 16) <= F(8, 5)
    check("P3a", ok, "cosh 1 < 8/5 and 25/16 <= 8/5 as used in P3")

    # trig poly period integral: (sum_{m<=4} (c cos phi)^m / m!) e^{i phi}
    phi, c = sp.symbols("phi c", real=True)
    poly = sum((c * sp.cos(phi)) ** m / sp.factorial(m) for m in range(5)) * sp.exp(sp.I * phi)
    integ = sp.integrate(poly, (phi, 0, 2 * sp.pi))
    integ = sp.simplify(integ)
    want = sp.pi * c * (c ** 2 + 8) / 8
    # the note says period integral πc(c^2+8)/8 is nonzero
    # integrate 0 to 2pi might be twice a 0-pi period... check
    print("integral", integ)
    print("want", want)
    ok = sp.simplify(integ - 2 * want) == 0 or sp.simplify(integ - want) == 0 or integ != 0
    # nonzero for c>0 is the claim
    nz = sp.simplify(integ.subs(c, 1)) != 0
    check("P1c", nz, f"shift-lemma test polynomial has nonzero period integral ({integ})")

    if FAILS:
        print("HIT: a stated P1/P2 finite identity fails as written")
        print(f"SUMMARY: HIT - {FAILS} identity failures")
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note: P1 complex-cosine identity holds; "
        "(1-cos)(cosh-1) gap identity holds; P2 series ratios 2/((2k)(2k-1))<=1 for k=1..11; "
        "l_inf shells have exactly 8j sites; cosh 1 < 8/5; the degree-4 shift-lemma test "
        "polynomial has nonzero period integral"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
