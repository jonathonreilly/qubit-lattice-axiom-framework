#!/usr/bin/env python3
"""J:attack-f:PR8027 — NORMALIZATION of Haar 1/18 and π in ρ_(r,s).

E J^2=(0+2+0)/36=1/18; ρ(r,s)=2 Σ_{k=1}^s cos(π k/(L+1)); path count
L!/(n1!n2!n3!). No 2π Fourier sum on a torus.
"""
from fractions import Fraction as Fr
from math import factorial

import sympy as sp


def npaths(n1, n2, n3):
    L = n1 + n2 + n3
    return factorial(L) // (factorial(n1) * factorial(n2) * factorial(n3))


def rho(r, s):
    L = r + s
    if r == 0 or s == 0:
        return sp.Integer(0)
    return sp.simplify(2 * sum(sp.cos(sp.pi * k / (L + 1)) for k in range(1, s + 1)))


def main() -> int:
    hits = []
    ej2 = (Fr(0) + Fr(2) + Fr(0)) / Fr(36)
    print(f"E J^2=(0+2+0)/36={ej2}")
    if ej2 != Fr(1, 18):
        hits.append(f"Haar {ej2} != 1/18")
    print(f"unique geodesic (3,0,0) npaths={npaths(3, 0, 0)}")
    if npaths(3, 0, 0) != 1:
        hits.append("npaths(3,0,0)!=1")
    if npaths(1, 1, 0) != 2:
        hits.append("npaths(1,1,0)!=2")
    got = rho(1, 1)
    print(f"ρ(1,1)={got} (stated 1); 2 cos(π/3)={sp.simplify(2 * sp.cos(sp.pi / 3))}")
    if got != 1:
        hits.append(f"ρ(1,1)={got} != 1")
    if rho(2, 1) != sp.sqrt(2):
        hits.append(f"ρ(2,1)={rho(2, 1)} != sqrt(2)")
    if hits:
        for h in hits:
            print("HIT:", h)
        print("SUMMARY: pattern (f) NORMALIZATION fired; " + "; ".join(hits))
        return 0
    print(
        "SUMMARY: pattern (f) NORMALIZATION — Haar E J^2=1/18, path "
        "L!/(n1!n2!n3!), and ρ(1,1)=2 cos(π/3)=1, ρ(2,1)=√2 all exact; "
        "no torus 2π Fourier; attack does not fire"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
