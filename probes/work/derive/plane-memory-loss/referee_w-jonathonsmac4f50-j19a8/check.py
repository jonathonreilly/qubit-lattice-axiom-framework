#!/usr/bin/env python3
"""Referee of J:derive:plane-memory-loss:a4 (author w-macbookpro90c72-jcb00, grok-4.6); referee w-jonathonsmac4f50-j19a8
(claude-opus-5). Independent code (sympy with exponential rewrites, exact integers, mpmath); nothing from the author's check.py.
Disclosure: this referee's model family refereed attempts a1, a2 and a3 of this problem (grok); the linear-model point below is
the one recorded against a1 (referee_w-jonathonsmac4f50-j8129).

Block 26's sphere formation law in level time: three recorded predecessors x, x - e1, x - e2, weight exp(beta s.S), S their sum;
A(k) = coth k - 1/k; the linear (spin-wave) model theta_{t+1} = P theta_t + noise, P the three-point average.

M1  step 1: A(k) < k/3 for k > 0 (q = (3 + k^2) sinh k - 3k cosh k > 0 via q' = k(k cosh k - sinh k), (k cosh k - sinh k)' =
    k sinh k), A(k)/k = 1/3 - k^2/45 + O(k^4)
M2  step 2: A' = 1/k^2 - csch^2 k > 0 (sinh k > k)
M3  step 3: the mean-field map A(3 beta m): orbits from m = 1 go to 0 at beta = 0.9, 1.0 and to positive fixed points at 1.2, 2.0;
    slope beta at 0
M4  step 4 does not follow: with m the plane magnetization (the mean of a record), '|S| >= 3|m|' fails pointwise - on the second
    level of the aligned start, records (+z, +z, -z), which lie in the support of the vMF law, give |S| = 1 < 3 A(3 beta) at
    beta = 1 (3 A(3) = 2.0149); with m the average of the three realized records it is the identity |S| = 3|m| (the attempt's
    witness 2e_z + e_x is of this kind) and carries no sign; either way the stated no-go is not established
M5  step 5 is false: the linear model forgets. Its per-site variance after t levels is sigma^2 sum_{s<t} q_s with q_s the return
    probability of the difference of two three-point walks, q_s = sum_{a+b+c=s} (s!/(a!b!c!))^2 / 9^s (exact); s q_s -> 3 sqrt3/(4 pi)
    = 0.41350, so the variance grows like 0.4135 sigma^2 log t and the projection on the initial direction decays; phi(0) = 1 conserves
    the mean of the uniform mode, not the magnetization
"""
from __future__ import annotations

import math
import sys
from math import factorial

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
    q = (3 + k ** 2) * sp.sinh(k) - 3 * k * sp.cosh(k)
    eq = sp.simplify(((k / 3 - A) * 3 * k * sp.sinh(k) - q).rewrite(sp.exp)) == 0
    dq = sp.simplify((sp.diff(q, k) - k * (k * sp.cosh(k) - sp.sinh(k))).rewrite(sp.exp)) == 0
    dr = sp.simplify(sp.diff(k * sp.cosh(k) - sp.sinh(k), k) - k * sp.sinh(k)) == 0
    ser = sp.series((A / k).rewrite(sp.exp), k, 0, 4).removeO()
    check("M1", eq and dq and dr and sp.simplify(ser - (sp.Rational(1, 3) - k ** 2 / 45)) == 0,
          f"(k/3 - A) 3k sinh k = q ({eq}); q' = k(k cosh k - sinh k) ({dq}); (k cosh k - sinh k)' = k sinh k ({dr}); A/k = {ser} + O(k^4)")

    dA = sp.simplify((sp.diff(A, k) - (1 / k ** 2 - 1 / sp.sinh(k) ** 2)).rewrite(sp.exp)) == 0
    check("M2", dA, "A' = 1/k^2 - csch^2 k, positive since sinh k > k")

    mp.mp.dps = 30
    Af = lambda x: mp.coth(x) - 1 / x if x != 0 else mp.mpf(0)
    rows, ok = [], True
    for beta, to_zero in ((mp.mpf("0.9"), True), (mp.mpf(1), True), (mp.mpf("1.2"), False), (mp.mpf(2), False)):
        m = mp.mpf(1)
        for _ in range(3000):
            m = Af(3 * beta * m)
        if to_zero:
            ok &= m < mp.mpf("0.05")
            rows.append(f"beta {float(beta)}: m_3000 = {float(m):.4f}")
        else:
            fp = mp.findroot(lambda x: Af(3 * beta * x) - x, 0.8)
            ok &= fp > 0 and abs(m - fp) < mp.mpf("1e-15")
            rows.append(f"beta {float(beta)}: fixed point {float(fp):.5f}")
    check("M3", ok, "; ".join(rows))

    threeA3 = 3 * Af(mp.mpf(3))
    S = abs(1 + 1 - 1)
    check("M4", S < threeA3, f"records (+z, +z, -z) give |S| = {S} < 3 A(3) = {float(threeA3):.4f} at beta = 1: '|S| >= 3|m|' is false "
          "pointwise for the magnetization; for the realized average it is an identity with no sign")

    rows, vals = [], {}
    for s in (25, 50, 100, 200, 400):
        tot = 0
        for a in range(s + 1):
            for b in range(s + 1 - a):
                c = s - a - b
                tot += (factorial(s) // (factorial(a) * factorial(b) * factorial(c))) ** 2
        qs = mp.mpf(tot) / mp.mpf(9) ** s
        vals[s] = s * qs
        rows.append(f"s = {s}: s q_s = {float(s * qs):.5f}")
    const = 3 * math.sqrt(3) / (4 * math.pi)
    ok = abs(float(vals[400]) - const) < 2e-3 and abs(float(vals[400]) - const) < abs(float(vals[25]) - const)
    check("M5", ok, "; ".join(rows) + f" -> 3 sqrt3/(4 pi) = {const:.5f}: the per-site variance grows like {const:.4f} sigma^2 log t, so the "
          "linear model's projection on the initial direction decays")

    if fails:
        print("SUMMARY: fails at a checked step (see FAIL lines)")
        return 1
    print("SUMMARY: fails at step 4 - steps 1-3 hold (A(k)/k < 1/3 via q = (3+k^2) sinh k - 3k cosh k, A increasing, the mean-field map "
          "A(3 beta m) forgets iff beta <= 1), but step 4's 'triangle |S| >= |ES| = 3|m|' is false pointwise when m is the magnetization "
          "(records (+z,+z,-z) give |S| = 1 < 3A(3) = 2.01) and an identity with no sign when m is the realized average, so the route-(ii) "
          "no-go is not established; and step 5's 'the linear model conserves the uniform mode, so cannot supply the decay' is false: "
          "phi(0) = 1 conserves the mode's mean while its variance grows (per-site 0.4135 sigma^2 log t, s q_s -> 3 sqrt3/(4 pi)), so the "
          "linear model does forget (the point recorded against a1)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
