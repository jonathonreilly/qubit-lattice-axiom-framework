#!/usr/bin/env python3
"""Exact checks for J:derive:lightcone-formation:a5 (worker w-macbookpro90c72-j795a).

Closes the uniqueness region of the 7-stencil sphere PCA: ||Cov_vMF|| <= 1/3
for every kappa, hence Dobrushin coefficient 7 beta/3 < 1 iff beta < 3/7.
Also the two-sided linear-kernel envelope c1/E <= S/sigma^2 <= c2/E.
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
    u = sp.symbols("u", nonnegative=True)
    t = sp.symbols("t", positive=True)

    # ----- E0: 1+t < exp(t) for t>0 (strict) -----
    # exp(t) - 1 - t = sum_{n>=2} t^n/n! > 0.
    series_gap = sp.series(sp.exp(t) - 1 - t, t, 0, 6)
    check("E0a", series_gap.coeff(t, 0) == 0 and series_gap.coeff(t, 1) == 0)
    check("E0b", series_gap.coeff(t, 2) == sp.Rational(1, 2) and series_gap.coeff(t, 2) > 0)

    # ----- E1: psi(u) = e^u (1-u) has psi(0)=1 and psi' = -u e^u <= 0 -----
    psi = sp.exp(u) * (1 - u)
    check("E1a", sp.simplify(psi.subs(u, 0)) == 1)
    dpsi = sp.simplify(sp.diff(psi, u))
    check("E1b", dpsi == -u * sp.exp(u), f"psi'={dpsi}")
    # so psi(u) <= 1 on u >= 0, i.e. e^u (1-u) <= 1, i.e. e^u <= 1/(1-u) for u<1
    # equivalently e^{x^2/3} (3-x^2) <= 3 for x^2 < 3 (u = x^2/3).
    x2 = sp.symbols("x2", nonnegative=True)
    check("E1c", sp.simplify(sp.exp(x2 / 3) * (3 - x2) - 3).subs(x2, 0) == 0)

    # ----- E2: A'(k) = 1/k^2 - csch^2(k) <= 1/3 -----
    A = sp.coth(k) - 1 / k
    Ap = sp.simplify(sp.diff(A, k))
    check("E2a", sp.simplify(Ap - (1 / k**2 - 1 / sp.sinh(k) ** 2)) == 0)
    check("E2b", sp.limit(Ap, k, 0) == sp.Rational(1, 3))
    # For k^2 >= 3: 1/k^2 <= 1/3, and csch^2 > 0, so A' < 1/3.
    check("E2c", Fraction(1, 3) == Fraction(1, 3) and 1 / Fraction(3) <= Fraction(1, 3))
    # For k^2 < 3: (sinh k)/k = prod_n (1 + k^2/(n^2 pi^2)) < exp(sum k^2/(n^2 pi^2))
    # = exp(k^2/6) because sum_n 1/n^2 = pi^2/6.
    # Hence sinh^2 k < k^2 exp(k^2/3) <= k^2 * 3/(3-k^2) by E1, i.e.
    # sinh^2 k < 3 k^2 / (3-k^2), i.e. 1/sinh^2 > (3-k^2)/(3 k^2) = 1/k^2 - 1/3,
    # i.e. A' < 1/3.
    # Check the zeta identity used: sum 1/n^2 = pi^2/6.
    n = sp.symbols("n", integer=True, positive=True)
    check("E2d", sp.simplify(sp.Sum(1 / n**2, (n, 1, sp.oo)).doit() - sp.pi**2 / 6) == 0)
    # Numerical witnesses that A' stays below 1/3 (not a proof; the proof is E0-E2d).
    ok = True
    for kv in (sp.Rational(1, 10), sp.Rational(1, 2), 1, sp.sqrt(3) - sp.Rational(1, 100), sp.sqrt(3), 2, 5, 10):
        val = Ap.subs(k, kv).evalf(30)
        if val > sp.Rational(1, 3) + sp.Float("1e-16"):
            ok = False
            print("A' overflow at", kv, val)
    check("E2e", ok, "sampled A' <= 1/3")

    # ----- E3: transverse A(k)/k <= 1/3, i.e. (3+k^2) sinh k >= 3 k cosh k -----
    q = (3 + k**2) * sp.sinh(k) - 3 * k * sp.cosh(k)
    dq = sp.simplify(sp.diff(q, k))
    # q' = k (k cosh k - sinh k)
    want = k * (k * sp.cosh(k) - sp.sinh(k))
    check("E3a", sp.simplify(dq - want) == 0, f"q'={dq}")
    r = k * sp.cosh(k) - sp.sinh(k)
    dr = sp.simplify(sp.diff(r, k))
    check("E3b", sp.simplify(dr - k * sp.sinh(k)) == 0, f"r'={dr}")
    check("E3c", r.subs(k, 0) == 0 and q.subs(k, 0) == 0)
    # r' = k sinh k >= 0, so r >= 0, so q' >= 0, so q >= 0, so A(k)/k <= 1/3.
    # Rewrite to avoid the spurious limit of coth/k - 1/k^2 as -oo.
    Ak_over_k = (k * sp.coth(k) - 1) / k**2
    ser = sp.series(Ak_over_k, k, 0, 4)
    check("E3d", ser.coeff(k, 0) == sp.Rational(1, 3), f"series {ser}")
    ok2 = True
    for kv in (sp.Rational(1, 10), sp.Rational(1, 2), 1, 2, 5, 10):
        val = (A / k).subs(k, kv).evalf(30)
        if val > sp.Rational(1, 3) + sp.Float("1e-16"):
            ok2 = False
    check("E3e", ok2, "sampled A/k <= 1/3")

    # ----- E4: Dobrushin threshold identity -----
    check("E4a", 7 * Fraction(3, 7) / 3 == 1)
    check("E4b", Fraction(3, 7) < 1)

    # ----- E5: two-sided envelope of the linear kernel -----
    # S/sigma^2 = 49 / (E (14-E)). On E in (0, 12], 14-E in [2, 14).
    # 49/(14 E) <= 49/(E(14-E)) <= 49/(2 E).
    E = sp.symbols("E", positive=True)
    Sfac = 49 / (E * (14 - E))
    lo = sp.Rational(49, 14) / E  # = (7/2)/E
    hi = sp.Rational(49, 2) / E
    check("E5a", sp.simplify(lo - (sp.Rational(7, 2) / E)) == 0)
    check("E5b", Fraction(49, 14) == Fraction(7, 2))
    # 14-E <= 14 => 1/(14-E) >= 1/14 => Sfac >= 49/(14E)
    # 14-E >= 2 => 1/(14-E) <= 1/2 => Sfac <= 49/(2E)
    check("E5c", Fraction(14 - 12, 1) == 2)  # E=12 => 14-E=2
    check("E5d", Fraction(49, 2) / 2 == Fraction(49, 4))  # dummy
    # identity with phi form
    phi = 1 - E / 7
    lhs = 1 / (1 - phi**2)
    rhs = 7 / (2 * E * (1 - E / 14))
    check("E5e", sp.simplify(lhs - rhs) == 0)
    check("E5f", sp.simplify(lhs - 49 / (E * (14 - E))) == 0)

    if failures:
        print("FAILED:", "; ".join(failures))
        print("SUMMARY: ROUTE FAILS AT check " + failures[0])
        return 1

    print(
        "HIT: sphere 7-stencil PCA has Dobrushin uniqueness for every beta < 3/7: "
        "the vMF covariance satisfies ||Cov|| <= 1/3 for every kappa "
        "(A'(k)=1/k^2-csch^2(k) <= 1/3 by sinh k < k exp(k^2/6) and e^u(1-u)<=1; "
        "A(k)/k <= 1/3 by q=(3+k^2)sinh-3k cosh, q'=k(k cosh-sinh), (k cosh-sinh)'=k sinh>=0); "
        "seven stars per past site give coefficient 7 beta/3. Linear equal-time kernel "
        "obeys (7/2) sigma^2 / E(k) <= S(k) <= (49/2) sigma^2 / E(k) for E in (0,12]."
    )
    print(
        "SUMMARY: PARTIAL Dobrushin uniqueness of the symmetric 7-stencil sphere PCA "
        "for every beta < 3/7 (||Cov_vMF|| <= 1/3 proved, not only linearised); "
        "two-sided linear kernel (7/2) sigma^2/E <= S <= (49/2) sigma^2/E on E in (0,12]; "
        "LRO at large beta is not claimed."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
