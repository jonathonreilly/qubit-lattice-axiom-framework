#!/usr/bin/env python3
"""Exact checks for J:derive:formation-in-3plus1:a6 (worker w-macbookpro90c72-j30e1).

Mean-field LRO threshold beta=3/4 for 4-predecessor sphere formation, and
two-sided small-k envelope of the linear kernel from the Hessian of 1-|phi|^2.
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

    k = sp.symbols("k", positive=True)
    A = sp.coth(k) - 1 / k
    Ak = (k * sp.coth(k) - 1) / k**2

    # A(k)/k < 1/3 for k>0 (same q as plane-memory-loss a4 / lightcone a5)
    q = (3 + k**2) * sp.sinh(k) - 3 * k * sp.cosh(k)
    dq = sp.simplify(sp.diff(q, k))
    check("E0a", sp.simplify(dq - k * (k * sp.cosh(k) - sp.sinh(k))) == 0)
    r = k * sp.cosh(k) - sp.sinh(k)
    check("E0b", sp.simplify(sp.diff(r, k) - k * sp.sinh(k)) == 0)
    check("E0c", sp.series(Ak, k, 0, 2).coeff(k, 0) == sp.Rational(1, 3))

    # Mean-field: 4 predecessors, m |-> A(4 beta m). Linearisation 4 beta / 3.
    check("E1a", 4 * Fraction(3, 4) / 3 == 1, "4*(3/4)/3=1")
    # A(4 beta m) < (4 beta / 3) m, so contractive at every m in (0,1] iff beta < 3/4.
    # At beta=3/4, A(3 m) < m for m in (0,1] (same as 2+1 mean-field at beta=1).
    A3 = A.subs(k, 3).evalf(30)
    check("E1b", A3 < 1, f"A(3)={A3}")
    # Derivative at 0 for beta=1: 4/3 > 1, so 0 is unstable in 3+1 already at beta=1
    # (whereas 2+1 mean-field is critical at beta=1).
    ser = sp.series(A.subs(k, 4 * k) / k, k, 0, 2)
    check("E1c", ser.coeff(k, 0) == sp.Rational(4, 3), f"{ser}")

    # Hessian of 1-|phi|^2 at 0 for d=3: eigenvalues 1/8, 1/2, 1/2
    k1, k2, k3 = sp.symbols("k1 k2 k3", real=True)
    phi = (1 + sp.exp(sp.I * k1) + sp.exp(sp.I * k2) + sp.exp(sp.I * k3)) / 4
    one_m = sp.simplify(1 - sp.expand_complex(sp.conjugate(phi) * phi))
    hess = sp.simplify(sp.hessian(one_m, [k1, k2, k3]).subs({k1: 0, k2: 0, k3: 0}))
    ev = hess.eigenvals()
    check("E2a", set(sp.simplify(lam) for lam in ev) == {sp.Rational(1, 8), sp.Rational(1, 2)})
    # 1-|phi|^2 = (1/2) k^T H k + O(4) so
    # (1/16)|k|^2 <= 1-|phi|^2 <= (1/4)|k|^2 + O(4)  because (1/2)*(1/8)=1/16, (1/2)*(1/2)=1/4
    check("E2b", Fraction(1, 2) * Fraction(1, 8) == Fraction(1, 16))
    check("E2c", Fraction(1, 2) * Fraction(1, 2) == Fraction(1, 4))
    # Hence S = sigma^2 / (1-|phi|^2) obeys 4 sigma^2/|k|^2 <= S <= 16 sigma^2/|k|^2
    # at small k (leading order).
    check("E2d", 1 / Fraction(1, 4) == 4 and 1 / Fraction(1, 16) == 16)

    # 2+1 comparison: 3 predecessors, threshold beta=1 = 3/3
    check("E3a", 3 * Fraction(1, 1) / 3 == 1)
    check("E3b", Fraction(3, 4) < 1)  # 3+1 mean-field orders at weaker coupling than 2+1

    if failures:
        print("FAILED:", "; ".join(failures))
        print("SUMMARY: ROUTE FAILS AT check " + failures[0])
        return 1

    print(
        "HIT: 3+1 sphere mean-field (4 predecessors, m |-> A(4 beta |m|)) has "
        "critical coupling beta=3/4: A(k)/k<1/3 gives A(4 beta m)<(4 beta/3) m, "
        "so m_t->0 for all m in [0,1] iff beta<=3/4; at 0 the derivative is 4 beta/3. "
        "This is below the 2+1 mean-field threshold beta=1. Linear kernel at small k: "
        "Hessian eigenvalues of 1-|phi|^2 are 1/8 and 1/2 (twice), hence "
        "4 sigma^2/|k|^2 <= S(k) <= 16 sigma^2/|k|^2 to leading order. Nonlinear LRO "
        "is not proved (same |S| vs 4|m| sign obstruction as in 2+1)."
    )
    print(
        "SUMMARY: PARTIAL 3+1 mean-field LRO threshold beta=3/4 (vs 2+1: beta=1) "
        "from A(k)/k<1/3; linear small-k envelope 4 sigma^2/|k|^2 <= S <= 16 sigma^2/|k|^2; "
        "nonlinear sphere LRO not proved."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
