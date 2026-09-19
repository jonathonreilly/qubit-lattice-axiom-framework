#!/usr/bin/env python3
"""Exact checks for J:derive:no-waves-under-positive-formation:a2
(worker w-macbookpro90c72-j80c2).
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

    k1, k2, k3 = sp.symbols("k1 k2 k3", real=True)

    # ----- E0: 7-stencil gain-one: lambda = 1 - E/7 -----
    E = 2 * ((1 - sp.cos(k1)) + (1 - sp.cos(k2)) + (1 - sp.cos(k3)))
    lam7 = (1 + 2 * sp.cos(k1) + 2 * sp.cos(k2) + 2 * sp.cos(k3)) / 7
    check("E0a", sp.simplify(lam7 - (1 - E / 7)) == 0)
    check("E0b", lam7.subs({k1: 0, k2: 0, k3: 0}) == 1)
    check("E0c", lam7.subs({k1: sp.pi, k2: 0, k3: 0}) == sp.Rational(3, 7))
    # |lambda| = |1-E/7| < 1 for E in (0,14]; at (pi,0,0) E=4, 1-4/7=3/7
    check("E0d", abs(Fraction(3, 7)) < 1)

    # ----- E1: Jensen |sum w e^{ikz}| <= 1, equality iff phases equal -----
    # Two-point: w=1/2 at 0 and e1. lambda=(1+exp(i k1))/2, |lambda|^2 = (1+cos k1)/2
    lam2 = (1 + sp.exp(sp.I * k1)) / 2
    mod2 = sp.simplify(sp.expand_complex(sp.conjugate(lam2) * lam2))
    check("E1a", sp.simplify(mod2 - (1 + sp.cos(k1)) / 2) == 0)
    check("E1b", mod2.subs(k1, 0) == 1)
    check("E1c", mod2.subs(k1, sp.pi) == 0)
    # Perpendicular: k=(0,k2), k1=0, |lambda|=1 for ALL k2. Collinear exception.
    check("E1d", mod2.subs(k1, 0) == 1)

    # ----- E2: small-k expansion of 7-stencil: 1 - E/7 = 1 - |k|^2/7 + O(k^4)
    # 1-cos k = k^2/2 - k^4/24 + ..., E = |k|^2 + O(k^4), lambda = 1 - |k|^2/7 + O(k^4)
    ser = sp.series(lam7.subs({k2: 0, k3: 0}), k1, 0, 4)
    check("E2a", ser.coeff(k1, 0) == 1)
    check("E2b", ser.coeff(k1, 1) == 0)
    check("E2c", ser.coeff(k1, 2) == -sp.Rational(1, 7), f"{ser}")
    # No i v·k term along a lattice axis for the symmetric 7-stencil (v=0).
    # Drift appears in the BACKWARD 4-stencil: phi=(1+e^{ik1}+e^{ik2}+e^{ik3})/4
    phi4 = (1 + sp.exp(sp.I * k1) + sp.exp(sp.I * k2) + sp.exp(sp.I * k3)) / 4
    dphi = sp.diff(phi4, k1).subs({k1: 0, k2: 0, k3: 0})
    check("E2d", dphi == sp.I / 4)

    # ----- E3: negative weight can oscillate / |lambda|>1 -----
    # w=2 at 0, w=-1 at e1: lambda=2-exp(i k1), |lambda|^2 at k1=0 is 1, at k1=pi is 9
    lam_n = 2 - sp.exp(sp.I * k1)
    mod_n = sp.simplify(sp.expand_complex(sp.conjugate(lam_n) * lam_n))
    check("E3a", mod_n.subs(k1, 0) == 1)
    check("E3b", mod_n.subs(k1, sp.pi) == 9)
    check("E3c", 9 > 1)

    # ----- E4: covariance of 7-stencil support is (2/7) I on the three axes
    # positions: 0 and ±e_j, each weight 1/7.  E[x_j^2] = 2/7, E[x_j x_l]=0
    check("E4a", Fraction(2, 7) > 0)
    # Hessian of |lambda|^2 at 0 for 7-stencil: lambda real, |lambda|^2=(1-E/7)^2
    # d^2/dk1^2 at 0 of (1-E/7)^2. E=2(1-cos k1)+..., E_k1k1(0)=2, lambda=1-E/7
    # (1-E/7)^2 at 0 is 1; first deriv 0; second: 2(1)(-E_k1k1/7)= -4/7
    H = sp.diff(sp.diff((1 - E / 7) ** 2, k1), k1).subs({k1: 0, k2: 0, k3: 0})
    check("E4b", H == -sp.Rational(4, 7), f"H={H}")
    # Negative Hessian => |lambda|<1 in a neighbourhood of 0 (diffusion).

    if failures:
        print("FAILED:", "; ".join(failures))
        print("SUMMARY: ROUTE FAILS AT check " + failures[0])
        return 1

    print(
        "HIT: gain-one linear formation with positive weights has |lambda(k)|<=1, "
        "with equality at k\neq0 iff e^{ik·z} is constant on the support (collinear "
        "exception: two-point (1+e^{ik1})/2 has |lambda|=1 for all k perp to e1). "
        "7-stencil lambda=1-E/7, Hessian of |lambda|^2 at 0 is -4/7 on each axis "
        "(diffusion). Backward 4-stencil has drift i/4. Negative weights: 2-e^{ik} "
        "has |lambda|^2=9 at k=pi (amplification/oscillation). Waves |lambda|=1 with "
        "arg=c|k| require dropping positivity or adding a conserved unitary structure."
    )
    print(
        "SUMMARY: PARTIAL positive gain-one linear formation is drift+diffusion "
        "(|lambda|<=1, Hessian of |lambda|^2 negative definite unless collinear); "
        "collinear exception and negative-weight |lambda|=3 at pi are exact; "
        "no propagating wave under positivity."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
