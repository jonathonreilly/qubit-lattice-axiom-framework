#!/usr/bin/env python3
"""J:attack-g:PR8153 — brute-force G3 cosine/Laplacian bounds.

Note: 1-cos θ ≥ 2θ²/π² on (0,π], hence E(k) ≥ (4/π²)|k|².
"""
from __future__ import annotations

import sys
from fractions import Fraction as F
from itertools import product

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
    th = sp.symbols("theta", positive=True)
    f = (1 - sp.cos(th)) / th ** 2
    # min on (0,pi] is at pi: 2/pi^2; limit at 0 is 1/2
    lim0 = sp.limit(f, th, 0)
    fpi = sp.simplify(f.subs(th, sp.pi))
    ok = lim0 == sp.Rational(1, 2) and fpi == 2 / sp.pi ** 2
    # derivative: critical points
    df = sp.simplify(sp.diff(1 - sp.cos(th) - 2 * th ** 2 / sp.pi ** 2, th))
    # check the inequality at a dense grid
    gap_ok = True
    for n in range(1, 201):
        t = n * sp.pi / 200
        val = sp.N((1 - sp.cos(t)) - 2 * t ** 2 / sp.pi ** 2)
        if val < -1e-12:
            gap_ok = False
            break
    check("G3a", ok and gap_ok,
          "1-cos theta >= 2 theta^2/pi^2 on (0,pi]: equality at pi, limit 1/2 at 0, nonnegative on 200-grid")

    # E(k)=sum_i 2(1-cos k_i) >= (4/pi^2)|k|^2 when each |k_i|<=pi
    ok = True
    pi = sp.pi
    for n in product(range(-2, 3), repeat=3):
        if n == (0, 0, 0):
            continue
        k = [sp.Integer(n[i]) * pi / 2 for i in range(3)]  # in [-pi,pi]
        # clamp: n=±2 -> ±pi
        E = sum(2 * (1 - sp.cos(k[i])) for i in range(3))
        r2 = sum(k[i] ** 2 for i in range(3))
        gap = sp.N(E - (4 / pi ** 2) * r2)
        if gap < -1e-10:
            ok = False
            print("fail", n, gap)
    check("G3b", ok, "E(k) >= (4/pi^2)|k|^2 on the (pi/2)Z^3 grid in [-pi,pi]^3, k!=0")

    if FAILS:
        print("HIT: G3 cosine/Laplacian bound fails at a checked point")
        print(f"SUMMARY: HIT - {FAILS} failures")
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note: G3's 1-cos theta >= 2 theta^2/pi^2 "
        "holds (equality at pi; 200-point grid nonnegative) and E(k) >= (4/pi^2)|k|^2 on "
        "the (pi/2)-grid in the Brillouin zone"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
