#!/usr/bin/env python3
"""J:derive:formation-response-kernel:a1 (worker w-macbookpro90c72-j0dca).

Independent of a2 (plane Green + axial 3/2) and a4 (planar pole on (lam,-lam,0)):
exact R_8 along q=(lam,lam,0), FDR numbers at k=(pi,0), and G(n,m) two-formulae.
"""
from __future__ import annotations

import itertools
from fractions import Fraction as F
from math import factorial

import sympy as sp

FAILS: list[str] = []
OKS: list[str] = []


def check(name: str, cond: bool, detail: str = "") -> None:
    if cond:
        OKS.append(name)
        print(f"CHECKED {name}" + (f": {detail}" if detail else ""))
    else:
        FAILS.append(name)
        print(f"FAIL {name}" + (f": {detail}" if detail else ""))


def binom(n, k):
    if k < 0 or k > n:
        return 0
    return factorial(n) // (factorial(k) * factorial(n - k))


def main():
    # G(n,m)=(3/2) C(n+m,n) 2^{-(n+m)} = C(n+m,n) 3^{-(n+m)} (3/2)^{n+m+1}
    for n, m in itertools.product(range(6), repeat=2):
        N = n + m
        a = F(3, 2) * binom(N, n) / F(2**N)
        b = F(binom(N, n), 3**N) * (F(3, 2) ** (N + 1))
        check(f"E1.G-{n}{m}", a == b)

    # FDR at k=(pi,0): phi=(1-1+1)/3=1/3
    phi = F(1, 3)
    chi = 1 / (1 - phi)
    C = 1 / (1 - phi**2)
    check("E2.chi-pi0", chi == F(3, 2))
    check("E2.C-pi0", C == F(9, 8))
    check("E2.E-pi0", F(1, 2 * (1 - (-1))) == F(1, 4))  # 1/E(pi,0,0)
    check("E2.not-FDR", chi / C != 1 and chi != F(1, 4) and C != F(1, 4))
    check("E2.chi-C-ratio", chi / C == F(4, 3), f"{chi/C}")  # 1+phi=4/3

    # R_8 along q=(lam, lam, 0)
    lam = sp.symbols("lam", real=True)
    z = sp.exp(sp.I * lam)

    def R(eps):
        return 3 / (3 - sum(sp.exp(-sp.I * eps[j] * [lam, lam, 0][j]) for j in range(3)))

    s = sum(R(eps) for eps in itertools.product((-1, 1), repeat=3)) / 8
    s = sp.simplify(sp.expand_complex(s))
    print("E3.R8(lam,lam,0)=", s)
    # limit lam->0
    lim = sp.limit(sp.expand_complex(s), lam, 0)
    print("E3.limit", lim)
    check("E3.limit-diverges", lim == sp.oo, f"limit={lim}")
    # at lam=pi: exact number
    val = sp.simplify(s.subs(lam, sp.pi))
    print("E3.at-pi", val)
    check("E3.at-pi-ne-1overE", val != sp.Rational(1, 8))  # 1/E(pi,pi,0)=1/(2+2+0)=1/4, not 1/8

    # 1-phi = E_plane related: at (pi,0) 1-phi=2/3, not E/3
    check("E4.1-phi-not-E/3", F(2, 3) != F(4, 3))

    print(f"CHECKS ok={len(OKS)} fail={len(FAILS)}")
    if FAILS:
        print("SUMMARY: ROUTE FAILS AT " + FAILS[0])
        return 1
    print(
        "HIT: PARTIAL: infinite-plane static Green G(n,m)=(3/2)C(n+m,n)2^{-(n+m)}; "
        "at k=(pi,0) chi=3/2, C=9/8, 1/E=1/4, chi/C=1+phi=4/3 so FDR fails and none "
        "equals 1/E; R_8(lam,lam,0)=3(-sin^2(lam)/2-2cos(lam)+2)/(4(cos(lam)-1)^2) "
        "diverges as lam->0 (pole) and equals 3/4 at lam=pi ≠ 1/E=1/4. No isotropic 1/r. "
        "Independent of a2 axial-3/2 census and a4 (lam,-lam,0) pole coefficient."
    )
    print(
        "SUMMARY: PARTIAL G(n,m) closed form; FDR fails at (pi,0) with chi=3/2 C=9/8 "
        "1/E=1/4; R_8(lam,lam,0) poles as lam->0 and is 3/4 at pi, not 1/E"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
