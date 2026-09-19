#!/usr/bin/env python3
"""Referee of J:derive:formation-in-3plus1:a6 (author w-macbookpro90c72-j30e1, grok-4.6); referee w-jonathonsmac4f50-j223e
(claude-opus-5). Independent code (sympy with exponential rewrites, mpmath); nothing from the author's check.py. Provenance: this
referee's model family refereed attempts a2 and a3 of this problem (grok), whose mean-field threshold and Hessian this attempt
shares; the checks below are written afresh.

Setting: backward 3+1 with four predecessors, phi(k) = (1 + sum_j e^{-i k_j})/4, A(k) = coth k - 1/k, mean-field map
f(m) = A(4 beta m) on [0, 1].

Q1  step 1: A(k) < k/3 for k > 0: with u(k) = (k^2 + 3) sinh k - 3k cosh k, A < k/3 <=> u > 0 (multiply by 3k sinh k > 0);
    u(0) = 0, u' = k(k cosh k - sinh k), (k cosh k - sinh k)' = k sinh k > 0 (sympy)
Q2  step 2: f(m) < (4 beta/3) m, so for beta <= 3/4 every orbit decreases to 0; f'(0) = 4 beta/3 > 1 for beta > 3/4 and
    f(1) = A(4 beta) < 1, so a positive fixed point exists and orbits from m_0 = 1 stay above it. Numerics (mpmath): orbits from
    m_0 = 1 at beta = 0.70, 0.75 decrease towards 0; at beta = 0.80, 1.00 they converge to the positive fixed point; 2+1 (three
    predecessors) has threshold beta = 1
Q3  step 3: the Hessian of 1 - |phi|^2 at 0 has eigenvalues 1/8 (along (1,1,1)) and 1/2 (twice) (sympy), so to leading order
    |k|^2/16 <= 1 - |phi|^2 <= |k|^2/4 and 4 sigma^2/|k|^2 <= S(k) = sigma^2/(1 - |phi|^2) <= 16 sigma^2/|k|^2; along (1,1,1)
    and (1,-1,0) at |k| = 1e-4, |k|^2 S/sigma^2 = 16 and 4 to 7 digits (mpmath)
"""
from __future__ import annotations

import sys

import mpmath as mp
import sympy as sp

fails = []


def check(name, ok, msg):
    print(("PASS " if ok else "FAIL ") + name + ": " + msg)
    if not ok:
        fails.append(name)


def main():
    k = sp.symbols("k", positive=True)
    A = sp.coth(k) - 1 / k
    u = (k ** 2 + 3) * sp.sinh(k) - 3 * k * sp.cosh(k)
    equiv = sp.simplify(((k / 3 - A) * 3 * k * sp.sinh(k) - u).rewrite(sp.exp)) == 0
    du = sp.simplify((sp.diff(u, k) - k * (k * sp.cosh(k) - sp.sinh(k))).rewrite(sp.exp)) == 0
    dv = sp.simplify(sp.diff(k * sp.cosh(k) - sp.sinh(k), k) - k * sp.sinh(k)) == 0
    check("Q1", equiv and du and dv and u.subs(k, 0) == 0,
          f"(k/3 - A) 3k sinh k = u ({equiv}); u' = k(k cosh k - sinh k) ({du}); (k cosh k - sinh k)' = k sinh k ({dv}); u(0) = 0")

    mp.mp.dps = 30
    Af = lambda x: mp.coth(x) - 1 / x if x != 0 else mp.mpf(0)
    rows = []
    ok = True
    for beta, expect_zero in ((mp.mpf("0.70"), True), (mp.mpf("0.75"), True), (mp.mpf("0.80"), False), (mp.mpf(1), False)):
        m = mp.mpf(1)
        orbit = [m]
        for _ in range(4000):
            m = Af(4 * beta * m)
            orbit.append(m)
        mono = all(a >= b for a, b in zip(orbit, orbit[1:]))
        if expect_zero:
            ok &= mono and orbit[-1] < orbit[100] < mp.mpf("0.5")
            rows.append(f"beta {float(beta)}: m_100 = {float(orbit[100]):.4f}, m_4000 = {float(orbit[-1]):.4f} (decreasing)")
        else:
            mstar = mp.findroot(lambda x: Af(4 * beta * x) - x, 0.9)
            ok &= mstar > 0 and abs(orbit[-1] - mstar) < mp.mpf("1e-20") and 4 * beta / 3 > 1
            rows.append(f"beta {float(beta)}: fixed point {float(mstar):.6f}, orbit limit {float(orbit[-1]):.6f}")
    ok &= mp.mpf(4) * mp.mpf("0.75") / 3 == 1 and Af(mp.mpf(3)) < 1
    check("Q2", ok, "mean-field orbits from m_0 = 1: " + "; ".join(rows) + f"; A(3) = {float(Af(mp.mpf(3))):.6f} < 1; the 2+1 "
          "map A(3 beta m) has slope beta at 0 (threshold 1)")

    k1, k2, k3 = sp.symbols("k1 k2 k3", real=True)
    ks = (k1, k2, k3)
    phi = (1 + sum(sp.exp(-sp.I * kk) for kk in ks)) / 4
    om = sp.simplify(sp.expand_complex(1 - phi * sp.conjugate(phi)))
    H = sp.Matrix(3, 3, lambda a, b: sp.simplify(sp.diff(om, ks[a], ks[b]).subs({k1: 0, k2: 0, k3: 0})))
    ev = H.eigenvals()
    omf = sp.lambdify(ks, om, "mpmath")
    eps = mp.mpf("1e-4")
    d111 = [eps / mp.sqrt(3)] * 3
    d110 = [eps / mp.sqrt(2), -eps / mp.sqrt(2), mp.mpf(0)]
    s111 = eps ** 2 / omf(*d111)
    s110 = eps ** 2 / omf(*d110)
    check("Q3", ev == {sp.Rational(1, 8): 1, sp.Rational(1, 2): 2} and abs(s111 - 16) < 1e-6 and abs(s110 - 4) < 1e-6,
          f"Hessian eigenvalues {ev}; |k|^2 S/sigma^2 at |k| = 1e-4: {float(s111):.7f} along (1,1,1), {float(s110):.7f} along "
          "(1,-1,0): the envelope [4, 16] is attained at both ends")

    if fails:
        print("SUMMARY: fails at a checked step (see FAIL lines)")
        return 1
    print("HIT: confirmed - formation-in-3plus1 a6: A(k) < k/3 for k > 0 (u(k) = (k^2+3) sinh k - 3k cosh k > 0 via u' = k(k cosh k "
          "- sinh k)), so the four-predecessor mean-field map A(4 beta m) sends every orbit to 0 iff beta <= 3/4 (slope 4 beta/3 at "
          "0; positive fixed point for beta > 3/4), against beta = 1 for three predecessors; Hessian eigenvalues 1/8, 1/2, 1/2 give "
          "4 sigma^2/|k|^2 <= S(k) <= 16 sigma^2/|k|^2 to leading order, both ends attained; recomputed independently. The "
          "attempt correctly leaves nonlinear LRO open")
    print("SUMMARY: confirmed - no failing step in the claimed partial (mean-field threshold and linear envelope); it overlaps "
          "attempt a2's threshold and Hessian")
    return 0


if __name__ == "__main__":
    sys.exit(main())
