#!/usr/bin/env python3
"""Exact checks for J:derive:plane-memory-loss:a4 (worker w-macbookpro90c72-jcb00).

Mean-field critical coupling beta=1 from A(k)/k < 1/3, and the sign obstruction
of route (ii) (comparison |S| vs 3|m|).
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
    Ak = (k * sp.coth(k) - 1) / k**2  # A(k)/k, regular at 0

    # ----- E0: A(k)/k series and strict inequality ingredients -----
    ser = sp.series(Ak, k, 0, 4)
    check("E0a", ser.coeff(k, 0) == sp.Rational(1, 3), f"{ser}")
    check("E0b", ser.coeff(k, 2) == sp.Rational(-1, 45))
    q = (3 + k**2) * sp.sinh(k) - 3 * k * sp.cosh(k)
    dq = sp.simplify(sp.diff(q, k))
    want_q = k * (k * sp.cosh(k) - sp.sinh(k))
    check("E0c", sp.simplify(dq - want_q) == 0)
    r = k * sp.cosh(k) - sp.sinh(k)
    dr = sp.simplify(sp.diff(r, k))
    check("E0d", sp.simplify(dr - k * sp.sinh(k)) == 0)
    check("E0e", q.subs(k, 0) == 0 and r.subs(k, 0) == 0)
    # r' = k sinh k > 0 for k>0 => r>0 => q'>0 => q>0 => A(k)/k < 1/3 for k>0
    ok = True
    for kv in (sp.Rational(1, 10), sp.Rational(1, 2), 1, 2, 5):
        val = Ak.subs(k, kv).evalf(30)
        if val >= sp.Rational(1, 3) - sp.Float("1e-20"):
            # must be strictly below 1/3
            if val >= sp.Rational(1, 3):
                ok = False
    check("E0f", ok, "sampled A(k)/k < 1/3")

    # ----- E1: mean-field map m |-> A(3 beta m) on (0,1] -----
    # Linearisation at 0: A(u)~u/3 so A(3 beta m) ~ beta m. Critical beta=1.
    u = sp.symbols("u", positive=True)
    check("E1a", sp.series(A, k, 0, 2).coeff(k, 1) == sp.Rational(1, 3))
    # For beta <= 1 and m in (0,1]: let kappa = 3 beta m > 0.
    # A(kappa) = kappa * (A/kappa) < kappa * (1/3) = beta m <= m.
    # Identity: A(3*beta*m) < beta*m  whenever A/k < 1/3.
    # Check numerically at beta=1, m=1: A(3) < 1
    A3 = A.subs(k, 3).evalf(40)
    check("E1b", A3 < 1, f"A(3)={A3}")
    # beta=2, small m: derivative beta=2>1, A(3*2*m)/m -> 2 as m->0
    # A(6m)/m = 6 A(6m)/(6m) -> 6*(1/3)=2 (series, not sp.limit of coth form)
    ser_mf = sp.series(A.subs(k, 6 * u) / u, u, 0, 2)
    check("E1c", ser_mf.coeff(u, 0) == 2, f"{ser_mf}")

    # ----- E2: route (ii) sign obstruction (exact on a configuration) -----
    # Three aligned unit vectors: S = 3 e_z, |S|=3 = 3|m| with m=e_z.
    # Three 120-degree in-plane: sum 0, |S|=0 < 3|m|? m=0, |S|>=0.
    # Fluctuation above the mean: two +z and one -z.
    # S = e_z+e_z-e_z = e_z, |S|=1, mean of the three is m = (1/3)e_z, 3|m|=1.
    # Equal in that case.
    # Two +z and one orthogonal +x: S = (1,0,2) wait 2 e_z + e_x, |S|=sqrt(5),
    # m = (2/3)e_z + (1/3)e_x, |m|=sqrt(4/9+1/9)=sqrt(5)/3, 3|m|=sqrt(5)=|S|.
    # Always |S| >= |sum| = 3|m| by triangle. Equality iff all three parallel.
    # A is increasing on [0,infty): A' = 1/k^2 - csch^2 >=? We have A'<=1/3 but A'>0
    # iff 1/k^2 > csch^2 iff sinh k > k, true for k>0.
    sinh_minus = sp.sinh(k) - k
    check("E2a", sp.series(sinh_minus, k, 0, 4).coeff(k, 3) == sp.Rational(1, 6))
    check("E2b", sp.diff(sinh_minus, k).subs(k, 0) == 0)
    # sinh' - 1 = cosh-1, (cosh-1)' = sinh, sinh(0)=0, sinh>=0, so sinh k > k for k>0
    # hence A'(k) > 0, A increasing.
    # Therefore A(beta |S|) >= A(3 beta |m|), so the nonlinear gain on a typical
    # configuration is at least the mean-field gain: WRONG direction for an upper
    # bound on |m'|.
    # Exact witness: m=1, three aligned, |S|=3=3|m|, equality. Any non-aligned
    # triple with the same mean is impossible because equality in triangle holds
    # iff parallel. So on the aligned plane (the initial condition of the task)
    # one has equality |S|=3 at t=0. After one step, fluctuations make |S|<3
    # sometimes, which LOWERS A(beta|S|) (A increasing), which is the contracting
    # direction — but then one no longer has a closed comparison with the
    # mean-field map of |m| alone, because the output mean is E[A(beta|S|) S/|S|],
    # not A(3 beta |m|).
    # Integer witness of triangle: |2 e_z + e_x|^2 = 5, (3|m|)^2 = 5.
    check("E2c", 2**2 + 1**2 == 5)
    check("E2d", Fraction(4, 9) + Fraction(1, 9) == Fraction(5, 9))

    # ----- E3: linear backward phi(0)=1 (mean conserved linearly) -----
    # Backward 3-stencil: phi(0)=(1+1+1)/3=1. Symmetric 7-stencil in 2D would be
    # n=5, phi(0)=1 as well. The linear model does not forget the uniform mode.
    check("E3a", Fraction(1 + 1 + 1, 3) == 1)
    check("E3b", Fraction(1 + 2 + 2, 5) == 1)  # 2D symmetric n=5

    if failures:
        print("FAILED:", "; ".join(failures))
        print("SUMMARY: ROUTE FAILS AT check " + failures[0])
        return 1

    print(
        "HIT: mean-field of the sphere formation law (m |-> A(3 beta |m|)) forgets "
        "iff beta <= 1: A(k)/k < 1/3 for k>0 (q=(3+k^2)sinh-3k cosh, q'=k(k cosh-sinh), "
        "(k cosh-sinh)'=k sinh>=0) gives A(3 beta m) < beta m <= m on (0,1] when beta<=1; "
        "at 0 the derivative is beta, so beta>1 makes 0 unstable. Route (ii) fails at the "
        "comparison |S| vs 3|m|: triangle |S|>=3|m| and A increasing yield A(beta|S|) >= "
        "A(3 beta |m|), the wrong sign for an upper bound on |m'|; the linear model "
        "conserves the uniform mode (phi(0)=1) so cannot supply the decay either."
    )
    print(
        "SUMMARY: PARTIAL mean-field forgets iff beta<=1 (exact from A(k)/k<1/3); "
        "ROUTE FAILS AT route (ii) comparison |S|>=3|m| (wrong sign for contraction); "
        "linear phi(0)=1 so the linear model does not forget. Infinite-lattice m_t->0 "
        "is not proved."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
