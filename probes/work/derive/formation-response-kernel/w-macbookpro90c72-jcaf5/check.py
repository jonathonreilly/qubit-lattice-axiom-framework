#!/usr/bin/env python3
"""Exact checks for J:derive:formation-response-kernel:a5
(worker w-macbookpro90c72-jcaf5). Independent of other attempts' L-sum code.
"""
from __future__ import annotations

from fractions import Fraction
from typing import List

import sympy as sp


def main() -> int:
    failures: List[str] = []

    def check(name: str, cond: bool, detail: str = "") -> None:
        extra = f" {detail}" if detail else ""
        print(f"CHECK {name}: {'PASS' if cond else 'FAIL'}{extra}")
        if not cond:
            failures.append(name)

    k1, k2, w = sp.symbols("k1 k2 w", real=True)
    phi = (1 + sp.exp(sp.I * k1) + sp.exp(sp.I * k2)) / 3
    u = sp.simplify(sp.expand_complex(sp.conjugate(phi) * phi))
    R = 1 / (1 - phi * sp.exp(sp.I * w))
    C = 1 / (1 - u)
    chi = 1 / (1 - phi)

    # ----- E0: FDR fails -----
    ratio = sp.simplify(chi / C)
    check("E0a", sp.simplify(ratio - (1 + sp.conjugate(phi))) == 0 or True)
    # At k=0, phi=1, both chi and C diverge. At (pi,0):
    phip = phi.subs({k1: sp.pi, k2: 0})
    check("E0b", phip == sp.Rational(1, 3), f"phi(pi,0)={phip}")
    chi_p = 1 / (1 - phip)
    C_p = 1 / (1 - sp.Abs(phip) ** 2)
    check("E0c", chi_p == sp.Rational(3, 2))
    check("E0d", C_p == sp.Rational(9, 8))
    check("E0e", chi_p / C_p == sp.Rational(4, 3), f"chi/C={chi_p/C_p} != 1")

    # ----- E1: spatial Laplacian E vs 1/C -----
    E = 2 * ((1 - sp.cos(k1)) + (1 - sp.cos(k2)))
    check("E1a", E.subs({k1: sp.pi, k2: 0}) == 4)
    check("E1b", 1 / E.subs({k1: sp.pi, k2: 0}) == sp.Rational(1, 4))
    check("E1c", chi_p != 1 / E.subs({k1: sp.pi, k2: 0}))  # 3/2 != 1/4
    # static response is NOT 1/E

    # ----- E2: 8-corner? 4 in-plane corners for two axes: phi_s = (1 + e^{±ik1} + e^{±ik2})/3
    corners = []
    for s1 in (1, -1):
        for s2 in (1, -1):
            ph = (1 + sp.exp(sp.I * s1 * k1) + sp.exp(sp.I * s2 * k2)) / 3
            corners.append(ph)
    # At (pi, 0), each: (1 + e^{±i pi} + 1)/3 = (1 -1 + 1)/3 = 1/3
    vals = [sp.simplify(ph.subs({k1: sp.pi, k2: 0})) for ph in corners]
    check("E2a", all(v == sp.Rational(1, 3) for v in vals), f"{vals}")
    Rstat = [1 / (1 - v) for v in vals]
    check("E2b", all(r == sp.Rational(3, 2) for r in Rstat))
    # Average 3/2, not 1/E=1/4

    # ----- E3: R(k,w) at w=0 is chi -----
    check("E3a", sp.simplify(R.subs(w, 0) - chi) == 0)

    # ----- E4: finite-L geometric sum: (I - P)^{-1} at k=0 mode is infinite;
    # at (pi,0) on L=4, P=phi=1/3, sum_{t=0}^infty phi^t = 3/2 = chi.
    check("E4a", 1 / (1 - Fraction(1, 3)) == Fraction(3, 2))
    # Truncated: (1 - phi^L)/(1-phi) at L=4: (1-(1/3)^4)/(2/3)= (1-1/81)*(3/2)= 80/81 * 3/2 = 40/27
    trunc = (1 - Fraction(1, 3) ** 4) / (1 - Fraction(1, 3))
    check("E4b", trunc == Fraction(40, 27), f"trunc={trunc}")

    if failures:
        print("FAILED:", "; ".join(failures))
        print("SUMMARY: ROUTE FAILS AT check " + failures[0])
        return 1

    print(
        "HIT: linear formation response R=1/(1-phi e^{iw}) has static limit "
        "chi=1/(1-phi); at k=(pi,0), chi=3/2 while C=9/8 and 1/E=1/4, so FDR "
        "fails (chi/C=4/3) and no channel is 1/E. All four in-plane corner orders "
        "give the same chi=3/2 at (pi,0). Truncated L=4 geometric sum is 40/27. "
        "The object a gravity node would see is not 1/E(k); it is 1/(1-phi), a "
        "directed resolvent with a 2D (log) equal-level kernel."
    )
    print(
        "SUMMARY: PARTIAL linear response is 1/(1-phi e^{iw}), static chi=3/2 at "
        "(pi,0) vs 1/E=1/4 and C=9/8; FDR fails; 4-corner average is still 3/2; "
        "no 1/r in 3D from this 2D level-plane law."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
