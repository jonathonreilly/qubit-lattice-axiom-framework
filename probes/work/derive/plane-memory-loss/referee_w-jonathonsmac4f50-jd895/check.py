#!/usr/bin/env python3
"""Referee of J:derive:plane-memory-loss:a1 (author w-macbookpro90c72-j8231, grok-4.6); referee w-jonathonsmac4f50-jd895
(claude-opus-5). Independent machinery (exact rationals, sympy, mpmath), none of the author's code.

P1  step 1: phi(0) = 1 for the three-predecessor plane stencil and the 7-stencil; the zero mode of the linear AR is a random
    walk (its mean is conserved)
P2  step 2's premise: on the plane the linear law's transverse site variance from the aligned start is
    v_t = sigma^2 sum_{k<t} P_k (per component; P_k the exact return sums of the walk with steps 0, e1, e2), which grows like
    c0 log t (c0 = 3 sqrt3/(4 pi)): exact sums to t = 256; so the linear magnetization proxy exp(-v_t) (block 26 T5) tends to 0:
    the linear law on the plane DOES forget its initial direction - through the random walk of its zero mode. (For contrast,
    the 7-stencil's 3D return sums are summable, so the 3D linear law keeps a positive proxy; the plane is the task's object.)
P3  step 3: A(k) = k/3 - k^3/45 + 2k^5/945 + O(k^7); 3k cosh k - 3 sinh k - k^2 sinh k = -k^5/15 - k^7/210 + O(k^9); at beta = 1
    A(3m) = m - (3/5) m^3 + O(m^5); A(k) < k/3 on a grid of (0, 50]
P4  step 3-4: the mean-field map m -> A(3 beta m) contracts for beta < 1 (A(3 beta m) <= beta m) and has a positive fixed point for
    beta > 1; 1/sqrt3 < 1
"""
from __future__ import annotations

import sys
from fractions import Fraction
from math import factorial

import mpmath as mp
import sympy as sp

mp.mp.dps = 30


def main():
    fails = 0

    def check(tag, ok, msg):
        nonlocal fails
        fails += (not ok)
        print(("PASS: " if ok else "FAIL: ") + tag + " " + msg)

    # P1
    k1, k2, k3 = sp.symbols("k1 k2 k3", real=True)
    phi3 = (1 + sp.exp(sp.I * k1) + sp.exp(sp.I * k2)) / 3
    phi7 = (1 + 2 * (sp.cos(k1) + sp.cos(k2) + sp.cos(k3))) / 7
    ok = phi3.subs({k1: 0, k2: 0}) == 1 and phi7.subs({k1: 0, k2: 0, k3: 0}) == 1
    check("P1", ok, "phi(0) = 1 for both stencils: the zero mode theta_{t+1}(0) = theta_t(0) + xi is a random walk with conserved mean")

    # P2: return sums of the plane walk
    T = 256
    P = []
    for k in range(T):
        s = 0
        for a in range(k + 1):
            for b in range(k + 1 - a):
                c = factorial(k) // (factorial(a) * factorial(b) * factorial(k - a - b))
                s += c * c
        P.append(Fraction(s, 9 ** k))
    partial = {}
    acc = Fraction(0)
    for t in range(1, T + 1):
        acc += P[t - 1]
        if t in (4, 16, 64, 256):
            partial[t] = acc
    c0 = 3 * mp.sqrt(3) / (4 * mp.pi)
    vals = {t: mp.mpf(v.numerator) / v.denominator for t, v in partial.items()}
    slope = (vals[256] - vals[64]) / mp.log(4)
    ok = all(vals[a] < vals[b] for a, b in ((4, 16), (16, 64), (64, 256))) and abs(slope - c0) < 0.01
    # 3D contrast: return sums of the 7-stencil lazy walk (steps 0, +-e_j with weight 1/7) - summable
    # compute sum_{k<K} Q_k with Q_k = sum_y q_k(y)^2 by convolution on a finite box (exact rationals, small K)
    K = 24
    import itertools
    dist = {(0, 0, 0): Fraction(1)}
    steps = [(0, 0, 0), (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    Q = []
    for k in range(K):
        Q.append(sum(v * v for v in dist.values()))
        new = {}
        for x, v in dist.items():
            for e in steps:
                y = (x[0] + e[0], x[1] + e[1], x[2] + e[2])
                new[y] = new.get(y, 0) + v / 7
        dist = new
    q_tail = [float(Q[k]) * k ** 1.5 for k in (8, 16, 23)]
    check("P2", ok,
          "step 2's premise: on the plane v_t/sigma^2 = sum_{k<t} P_k = " + ", ".join(f"{mp.nstr(vals[t], 6)} (t = {t})" for t in sorted(vals))
          + f", growing by {mp.nstr(slope, 5)} per unit log t (c0 = {mp.nstr(c0, 5)}): v_t -> infinity, so the linear magnetization proxy "
          "exp(-v_t) -> 0 and the linear law on the plane forgets its initial direction, through the random walk of the zero mode whose "
          "MEAN is conserved; the stated no-go ('the linear model does not forget') does not hold on the plane. In 3D the 7-stencil "
          "return sums decay like k^(-3/2) (k^1.5 Q_k = " + ", ".join(f"{v:.4f}" for v in q_tail) + " at k = 8, 16, 23), summable, so "
          "there the linear proxy stays positive")

    # P3
    k = sp.symbols("k", positive=True)
    A = sp.coth(k) - 1 / k
    serA = sp.series((k * sp.cosh(k) - sp.sinh(k)) / (k * sp.sinh(k)), k, 0, 7).removeO()
    okA = sp.simplify(serA - (k / 3 - k ** 3 / 45 + 2 * k ** 5 / 945)) == 0
    sgn = sp.series(3 * k * sp.cosh(k) - 3 * sp.sinh(k) - k ** 2 * sp.sinh(k), k, 0, 9).removeO()
    okS = sp.simplify(sgn - (-k ** 5 / 15 - k ** 7 / 210)) == 0
    m = sp.symbols("m", positive=True)
    ser3 = sp.series(((3 * m) * sp.cosh(3 * m) - sp.sinh(3 * m)) / ((3 * m) * sp.sinh(3 * m)), m, 0, 5).removeO()
    ok3 = sp.simplify(ser3 - (m - sp.Rational(3, 5) * m ** 3)) == 0
    grid = all(mp.coth(x) - 1 / x < x / 3 for x in [mp.mpf(i) / 10 for i in range(1, 501)])
    check("P3", okA and okS and ok3 and grid, "A(k) = k/3 - k^3/45 + 2k^5/945 + O(k^7); 3k cosh k - 3 sinh k - k^2 sinh k = -k^5/15 - k^7/210 + O(k^9); "
          "A(3m) = m - (3/5)m^3 + O(m^5); A(k) < k/3 at 500 points of (0, 50]")

    # P4
    ok = True
    for beta in (mp.mpf("0.5"), mp.mpf("0.9"), mp.mpf("0.99")):
        for mm in (mp.mpf("0.01"), mp.mpf("0.3"), mp.mpf("0.9")):
            ok = ok and (mp.coth(3 * beta * mm) - 1 / (3 * beta * mm)) <= beta * mm
    fp = mp.findroot(lambda x: mp.coth(3 * mp.mpf("1.5") * x) - 1 / (3 * mp.mpf("1.5") * x) - x, 0.6)
    ok = ok and 0 < fp < 1 and 1 / mp.sqrt(3) < 1
    check("P4", ok, f"A(3 beta m) <= beta m for beta < 1 (grid), a positive mean-field fixed point at beta = 1.5 (m = {mp.nstr(fp, 6)}), 1/sqrt3 < 1")

    if fails:
        print("SUMMARY: fails at a checked step (see FAIL lines)")
        return 1
    print("SUMMARY: fails at step 2 - 'the linear model does not forget, so a comparison with it cannot prove m_t -> 0' confuses the "
          "conserved mean of the zero mode with the magnetization: on the plane the linear transverse variance v_t = sigma^2 sum_{k<t} P_k "
          "grows like (3 sqrt3/(4 pi)) log t (exact return sums to t = 256), so the linear magnetization proxy exp(-v_t) tends to 0; the "
          "zero mode's random walk is the forgetting mechanism, not an obstruction, and the stated no-go for route (ii) does not follow. "
          "Steps 1, 3, 4 hold (phi(0) = 1, the Langevin jet and the sign identity, the mean-field threshold beta = 1)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
