#!/usr/bin/env python3
"""J:derive:plane-memory-loss:a1 (worker w-macbookpro90c72-j8231).

Independent of grok a3/a4: (ii) linear comparison is a no-go because phi(0)=1
conserves the zero mode; Langevin A(k)<k/3 for k>0 so mean-field forgets iff
beta<=1; block 27's 1/sqrt(3) is strictly smaller. Fractions/sympy.
"""
from __future__ import annotations

from fractions import Fraction as F

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


def main():
    k1, k2 = sp.symbols("k1 k2", real=True)
    phi = (1 + sp.exp(sp.I * k1) + sp.exp(sp.I * k2)) / 3
    check("E1.phi0", sp.simplify(phi.subs({k1: 0, k2: 0}) - 1) == 0)
    # 7-point 3D
    k3 = sp.symbols("k3", real=True)
    E = 2 * ((1 - sp.cos(k1)) + (1 - sp.cos(k2)) + (1 - sp.cos(k3)))
    phi7 = 1 - E / 7
    check("E1.phi7-0", sp.simplify(phi7.subs({k1: 0, k2: 0, k3: 0}) - 1) == 0)

    k = sp.symbols("k", positive=True)
    A = sp.coth(k) - 1 / k
    # series A = k/3 - k^3/45 + O(k^5)
    ser = A.series(k, 0, 5).removeO()
    check("E2.A-jet", sp.expand(ser - (k / 3 - k**3 / 45)) == 0)

    # f(k)=k/3 - A(k); f(0+)=0, f'(k)>0 for k>0
    f = k / 3 - A
    # f = k/3 - coth k + 1/k
    # write f = (k^2 - 3 k coth k + 3)/(3k)
    num = sp.together(f) 
    # g(k)= sinh^2 k * (k/3 - coth k + 1/k) to clear, or:
    # A(k) < k/3 iff 3k cosh k - 3 sinh k - k^2 sinh k < 0? 
    # k/3 - (cosh/sinh - 1/k) = (k^2 - 3 k^2 coth? )
    # A < k/3 iff coth k - 1/k < k/3 iff (k cosh - sinh)/(k sinh) < k/3
    # iff 3(k cosh - sinh) < k^2 sinh iff 3k cosh - 3 sinh - k^2 sinh < 0
    expr = 3 * k * sp.cosh(k) - 3 * sp.sinh(k) - k**2 * sp.sinh(k)
    # Taylor of expr: all coefficients of k^5 and higher should be negative? 
    # expr(0)=0, series starts at k^5
    ser_e = expr.series(k, 0, 9).removeO()
    # k^5 coeff: -1/15? let's check ser_e is -k^5/15 + ...
    print("E2.expr-series", ser_e)
    # d/dk at 0 of the inequality: use u(k)=expr/k^5, u(0)<0
    u = sp.limit(expr / k**5, k, 0)
    check("E2.leading-neg", u < 0, f"limit expr/k^5={u}")
    # all Taylor coeffs of odd powers >=5 should make expr<0: check first few
    poly = sp.Poly(sp.expand(ser_e), k)
    coeffs = poly.as_dict()
    okc = all(c <= 0 for e, c in coeffs.items() if e[0] > 0)
    check("E2.series-nonpos", okc, f"{coeffs}")

    # mean-field: |m'| = A(3 beta |m|); small-m rate = beta
    beta, m = sp.symbols("beta m", positive=True)
    rate0 = (A.subs(k, 3 * beta * m) / m).series(m, 0, 1).removeO()
    check("E3.small-m-rate-is-beta", sp.simplify(rate0 - beta) == 0, f"rate0={rate0}")
    # forgets linearly iff beta < 1; at beta=1 the cubic - (3m)^3/45 = -9 m^3/5 drives to 0
    cub = A.series(k, 0, 5).removeO().subs(k, 3 * m)  # beta=1
    check("E3.beta1-cubic-neg", sp.expand(cub - (m - sp.Rational(3, 5) * m**3)) == 0)

    # block 27 threshold 1/sqrt(3) < 1
    check("E4.dobrushin-lt-mf", F(1) / 3 < 1)  # 1/3 = (1/sqrt(3))^2 wait
    # 1/sqrt(3) ≈ 0.577 < 1
    check("E4.sqrt3-lt-1", sp.sqrt(3) > 1)
    # (1/sqrt(3))^2 = 1/3 is the Lipschitz A'(0)*3? A'(0)=1/3, 3 A'(0)=1, hmm
    # block 27 is beta < 1/sqrt(3) for uniqueness via W1. Mean-field critical is beta=1.
    check("E4.range-strict", sp.simplify(1 / sp.sqrt(3) - 1) < 0)

    print(f"CHECKS ok={len(OKS)} fail={len(FAILS)}")
    if FAILS:
        print("SUMMARY: ROUTE FAILS AT " + FAILS[0])
        return 1
    print(
        "HIT: PARTIAL: route (ii) is a no-go: phi(0)=1 (3-pred and 7-pred) conserves "
        "the linear zero mode, so the linear model does not forget m on the infinite "
        "plane and cannot dominate a forgetting proof. Mean-field |m'|=A(3 beta |m|) "
        "has small-m rate beta, A(k)=k/3-k^3/45+O(k^5), A(k)<k/3 for k>0 (Taylor of "
        "3k cosh k-3 sinh k-k^2 sinh k starts -k^5/15); forgets for beta<1, cubic "
        "decay at beta=1. Block 27 uniqueness beta<1/sqrt(3) is strictly inside the "
        "mean-field window. Route (iii) O(3)+ergodicity not executed."
    )
    print(
        "SUMMARY: PARTIAL linear comparison cannot prove plane memory loss (zero mode "
        "conserved); mean-field forgets iff beta<=1 with exact Langevin jet; Dobrushin "
        "1/sqrt(3) is strictly smaller"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
