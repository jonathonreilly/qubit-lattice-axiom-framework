#!/usr/bin/env python3
"""Referee of J:derive:plane-memory-loss:a3 (author w-macbookpro90c72-j17cb, grok-4.6); referee
w-jonathonsmac4f50-j8129 (claude-opus-5). Independent machinery (exact rationals, sympy, mpmath), none of the author's code.

Walk of the plane: (P f)(x) = (f(x) + f(x - e1) + f(x - e2))/3; P_k = sum_y p_k(y)^2 (return sum).

M1  step 1: A(k) < k/3; the author's polynomial k^2 sinh^2 k - 3 sinh^2 k + 3k^2 >= 0 is the inequality A'(k) <= 1/3, not
    the monotonicity of A(k)/k; that monotonicity holds by k^2 + k sinh k cosh k - 2 sinh^2 k > 0 (coefficients
    2^(2m-2)(2m - 4)/(2m)! >= 0)
M2  step 2: KL(vMF(k u) || vMF(k u')) = k A(k)(1 - u.u') (quadrature at 30 digits), and a twist static in level time with
    gradient 1/L costs Theta(T), as the author says
M3  step 2's conclusion: for a space-time twist theta(x, t) with theta(., 0) = 0 and theta(x0, T) = 1, the minimum of the
    level-time Dirichlet cost sum_t ||theta_{t+1} - P theta_t||^2 is exactly 1/sum_{k<T} P_k (Cauchy-Schwarz, the
    optimum is attained), which tends to 0 like 1/(c0 log T), c0 = 3 sqrt3/(4 pi), by the recurrence of the walk:
    exact values up to T = 256; so the mechanism step 2 names is not forced; the order-one spread part of the relative
    entropy grows for that twist (numerical INFO), so whether route (i) works stays open
M4  step 3: the z-marginal W1 equals A(k) (stochastic order: difference of means) and the small-field W1 rate at k = 0 is
    exactly 1/3 (reflection coupling cost 1/3 = the test function s_1)
M5  step 5 and 6: P_1..P_4 = 1/3, 5/27, 31/243, 71/729; k P_k -> 3 sqrt3/(4 pi); mean-field A(3 beta m) <= beta m, and a
    positive fixed point for beta > 1
"""
from __future__ import annotations

import sys
from fractions import Fraction
from math import comb, factorial

import mpmath as mp
import sympy as sp

mp.mp.dps = 30
PASSES = 0
FAILS = 0


def check(tag, ok, msg):
    global PASSES, FAILS
    if ok:
        PASSES += 1
    else:
        FAILS += 1
    print(f"{'PASS' if ok else 'FAIL'}: {tag} {msg}")


def A(k):
    return mp.coth(k) - 1 / k


def m1():
    k = sp.symbols("k", positive=True)
    author = k ** 2 * sp.sinh(k) ** 2 - 3 * sp.sinh(k) ** 2 + 3 * k ** 2
    # author's polynomial >= 0  <=>  3k^2 >= (3 - k^2) sinh^2  <=>  (for k^2 < 3) 1/sinh^2 >= 1/k^2 - 1/3  <=>  A' <= 1/3
    grid = [mp.mpf(i) / 20 for i in range(1, 400)]
    apr = [1 / x ** 2 - 1 / mp.sinh(x) ** 2 for x in grid]
    auth = [x ** 2 * mp.sinh(x) ** 2 - 3 * mp.sinh(x) ** 2 + 3 * x ** 2 for x in grid]
    equiv = all((a >= 0) == (ap <= mp.mpf(1) / 3) for a, ap in zip(auth, apr))
    mono = k ** 2 + k * sp.sinh(k) * sp.cosh(k) - 2 * sp.sinh(k) ** 2
    ser = sp.series(mono, k, 0, 16).removeO()
    coeffs_ok = all(sp.simplify(ser.coeff(k, 2 * m) - (sp.Rational(2) ** (2 * m - 2) * (2 * m - 4) / sp.factorial(2 * m)
                                                          if m >= 2 else 0)) == 0 for m in range(1, 8))
    dec = all(A(grid[i + 1]) / grid[i + 1] < A(grid[i]) / grid[i] for i in range(len(grid) - 1))
    lt = all(A(x) < x / 3 for x in grid)
    ok = equiv and coeffs_ok and dec and lt
    check("M1", ok, "step 1: A(k) < k/3 on (0, 20); the author's polynomial is >= 0 exactly where A'(k) <= 1/3 (399 grid "
          "points), so it proves A' <= 1/3, not that A(k)/k decreases; A(k)/k does decrease, by k^2 + k sinh k cosh k - "
          "2 sinh^2 k whose k^(2m) coefficient is 2^(2m-2)(2m - 4)/(2m)! >= 0 (series to k^14) and on the grid; the "
          "monotonicity is not used later")


def m2():
    ok = True
    for kap, ang in ((mp.mpf(2), mp.mpf("0.7")), (mp.mpf(5), mp.mpf("0.3"))):
        # KL(vMF(k u)||vMF(k u')) with u = e_z, u' at angle ang: exponential family closed form vs quadrature
        # density on S^2 w.r.t. dsigma/(4 pi): k/sinh k * e^{k s.u}; E[s] = A(k) u
        def dens(mu):
            return kap / mp.sinh(kap) * mp.e ** (kap * mu)
        # KL = E_u[k s.u - k s.u'] = k (A(k) - A(k) cos ang) = k A(k)(1 - cos ang), check by 2D quadrature
        def integrand(th, ph):
            s = (mp.sin(th) * mp.cos(ph), mp.sin(th) * mp.sin(ph), mp.cos(th))
            su = s[2]
            sup = s[0] * mp.sin(ang) + s[2] * mp.cos(ang)
            return dens(su) * kap * (su - sup) * mp.sin(th) / (4 * mp.pi)
        kl = mp.quad(integrand, [0, mp.pi], [0, 2 * mp.pi])
        ok = ok and abs(kl - kap * A(kap) * (1 - mp.cos(ang))) < mp.mpf(10) ** -20
    check("M2", ok, "step 2: KL(vMF(k u)||vMF(k u')) = k A(k)(1 - u.u') by 2D quadrature at (k, angle) = (2, 0.7), (5, 0.3); "
          "a twist static in level time with gradient 1/L pays O(1) per level, Theta(T) in all, as the author says")


def return_sums(T):
    P = []
    for k in range(T):
        s = 0
        for a in range(k + 1):
            for b in range(k + 1 - a):
                c = factorial(k) // (factorial(a) * factorial(b) * factorial(k - a - b))
                s += c * c
        P.append(Fraction(s, 9 ** k))
    return P


def m3(P):
    ok = True
    rows = []
    c0 = 3 * mp.sqrt(3) / (4 * mp.pi)
    partial = Fraction(0)
    vals = {}
    for T in range(1, len(P) + 1):
        partial += P[T - 1]
        if T in (1, 2, 4, 16, 64, 256):
            vals[T] = 1 / partial
    seq = [vals[T] for T in sorted(vals)]
    ok = all(seq[i + 1] < seq[i] for i in range(len(seq) - 1)) and vals[1] == 1 and vals[2] == Fraction(3, 4)
    # growth of sum P_k against c0 log T
    dlt = 1 / vals[256] - 1 / vals[64]
    growth = (mp.mpf(dlt.numerator) / dlt.denominator) / mp.log(4)
    ok = ok and abs(growth - c0) < 0.01
    rows = ", ".join(f"T={T}: {vals[T]}" if T <= 4 else f"T={T}: {mp.nstr(mp.mpf(vals[T].numerator) / vals[T].denominator, 6)}"
                     for T in sorted(vals))
    # the spread term of the optimal twist, numerically (floats), on a finite window containing the backward cone
    spread_info = ""
    try:
        import numpy as np
        out = []
        for T in (8, 32, 64):
            n = T + 2
            # backward kernel images: w_k = (P^T)^k delta_{x0}; P^T f(y) = (f(y) + f(y + e1) + f(y + e2))/3
            x0 = (n - 1, n - 1)
            w = [np.zeros((n, n))]
            w[0][x0] = 1.0
            for k in range(1, T):
                f = w[-1]
                g = f.copy()
                g[:-1, :] += f[1:, :]
                g[:, :-1] += f[:, 1:]
                w.append(g / 3.0)
            Z = sum((wk ** 2).sum() for wk in w)
            # optimal u_s = w_{T-1-s}/Z, theta_t = sum_{s<t} P^{t-1-s} u_s
            def Pf(f):
                g = f.copy()
                g[1:, :] += f[:-1, :]
                g[:, 1:] += f[:, :-1]
                return g / 3.0
            theta = np.zeros((n, n))
            lin = 0.0
            spread = 0.0
            for t in range(T):
                u = w[T - 1 - t] / Z
                # spread term at level t: sum_x Var over the three predecessors of theta_t
                sh1 = np.zeros_like(theta)
                sh1[1:, :] = theta[:-1, :]
                sh2 = np.zeros_like(theta)
                sh2[:, 1:] = theta[:, :-1]
                m = (theta + sh1 + sh2) / 3.0
                spread += (((theta - m) ** 2 + (sh1 - m) ** 2 + (sh2 - m) ** 2) / 3.0).sum()
                lin += (u ** 2).sum()
                theta = Pf(theta) + u
            out.append(f"T={T}: theta_T(x0) = {theta[x0]:.6f}, linear cost {lin:.4f} (= 1/sum P_k), spread cost {spread:.2e}")
        spread_info = "; ".join(out)
    except Exception as exc:
        spread_info = f"; spread term skipped ({type(exc).__name__})"
    check("M3", ok,
          "step 2's conclusion: over space-time twists with theta(., 0) = 0 and theta(x0, T) = 1, the order-beta part of the "
          "path-space cost, sum_t ||theta_{t+1} - P theta_t||^2, has minimum exactly 1/sum_{k<T} P_k (Cauchy-Schwarz; "
          "attained by u_s proportional to (P^T)^(T-1-s) delta), decreasing to 0: " + rows + f"; sum P_k grows by "
          f"{mp.nstr(growth, 5)} per unit log T between T = 64 and 256 (c0 = {mp.nstr(c0, 5)}). So the mechanism step 2 "
          "names (a cost Theta(T) from the gradient) is not forced for space-time twists, and 'route (i) is closed as a "
          "no-go' does not follow from it")
    print("INFO: M3b (numerical, not a claim) for the same linear-optimal twist, the order-one spread part sum_t sum_x "
          "Var_(predecessors)(theta_t), which a second-order expansion of the vMF relative entropy also produces (rotating "
          "the three predecessors by different angles moves S at first order through the records' transverse "
          "fluctuations), grows with T: " + spread_info + ". Whether some space-time twist makes both parts small is open: "
          "the attempt neither proves nor refutes it")


def m4():
    ok = True
    for kap in (mp.mpf("0.5"), mp.mpf(2), mp.mpf(6)):
        # z under vMF(k e): density k e^{k z}/(2 sinh k) on [-1, 1]; uniform z has mean 0; the vMF law dominates
        mean = mp.quad(lambda z: z * kap * mp.e ** (kap * z) / (2 * mp.sinh(kap)), [-1, 1])
        # 1D W1 = integral |F_unif - F_vmf|; F_vmf <= F_unif pointwise, so W1 = difference of means
        Fv = lambda z: (mp.e ** (kap * z) - mp.e ** (-kap)) / (mp.e ** kap - mp.e ** (-kap))
        Fu = lambda z: (z + 1) / 2
        w1 = mp.quad(lambda z: abs(Fu(z) - Fv(z)), [-1, 1])
        ok = ok and abs(mean - A(kap)) < mp.mpf(10) ** -25 and abs(w1 - A(kap)) < mp.mpf(10) ** -20
    # reflection coupling at k = 0 in direction e1: move mass s1^+ to the mirror point, cost 2 s1 per unit mass
    cost = mp.quad(lambda th, ph: 2 * (mp.sin(th) * mp.cos(ph)) ** 2 * mp.sin(th) / (4 * mp.pi), [0, mp.pi], [-mp.pi / 2, mp.pi / 2])
    ok = ok and abs(cost - mp.mpf(1) / 3) < mp.mpf(10) ** -12
    check("M4", ok, "step 3: the z-marginal W1 between uniform and vMF(k e) equals the difference of means A(k) (k = 0.5, 2, 6), "
          f"and at k = 0 the reflection coupling transports the signed measure s_1 dsigma/(4 pi) at cost {mp.nstr(cost, 8)} = 1/3, "
          "matched by the test function s_1: the small-field W1 rate is exactly 1/3 (the upper half, which the attempt "
          "asserts via A(k)/k -> 1/3, needs this coupling)")


def m5(P):
    ok = P[1] == Fraction(1, 3) and P[2] == Fraction(5, 27) and P[3] == Fraction(31, 243) and P[4] == Fraction(71, 729)
    c0 = 3 * mp.sqrt(3) / (4 * mp.pi)
    kPk = [k * mp.mpf(P[k].numerator) / P[k].denominator for k in (64, 128, 255)]
    ok = ok and abs(kPk[-1] - c0) < 0.005 and abs(kPk[-1] - c0) < abs(kPk[0] - c0)
    mf = True
    for beta in (mp.mpf("0.5"), mp.mpf(1), mp.mpf("1.5"), mp.mpf(3)):
        for m in (mp.mpf("0.1"), mp.mpf("0.5"), mp.mpf("0.9")):
            mf = mf and A(3 * beta * m) <= beta * m
    fp = mp.findroot(lambda m: A(3 * mp.mpf(2) * m) - m, 0.8)
    ok = ok and mf and 0 < fp < 1
    check("M5", ok, f"steps 5-6: P_1..P_4 = {P[1]}, {P[2]}, {P[3]}, {P[4]}; k P_k at k = 64, 128, 255 = "
          + ", ".join(mp.nstr(v, 6) for v in kPk) + f" -> 3 sqrt3/(4 pi) = {mp.nstr(c0, 6)}; A(3 beta m) <= beta m on a grid; "
          f"at beta = 2 the mean-field map has the positive fixed point m = {mp.nstr(fp, 6)}")


def main():
    try:
        m1()
        m2()
        P = return_sums(256)
        m3(P)
        m4()
        m5(P)
    except Exception as exc:
        print(f"FAIL: X unexpected exception {type(exc).__name__}: {exc}")
        print("SUMMARY: referee check.py crashed")
        return 1
    print(f"TOTAL: PASS={PASSES} FAIL={FAILS}")
    if FAILS:
        print("SUMMARY: referee checks failed (see FAIL lines)")
        return 1
    print("SUMMARY: fails at step 2 - the identity KL = k A(k)(1 - u.u') and the Theta(T) cost of a twist that is static in "
          "level time are right, but they do not close route (i): the task's twist is a space-time field theta(x, t), and "
          "for it the order-beta part of the cost has minimum exactly 1/sum_{k<T} P_k -> 0 (recurrence of the walk), so "
          "the mechanism step 2 names is not forced; whether the order-one spread part (which grows for the "
          "linear-optimal twist, numerical) can also be made small is open, and 'route (i) is closed as a no-go' is not "
          "shown. The other identities hold, re-verified: KL, "
          "the z-marginal W1 = A(k), the small-field W1 rate 1/3 (with the coupling the attempt omits), P_1..P_4, "
          "k P_k -> 3 sqrt3/(4 pi), the mean-field threshold; step 1's monotonicity of A(k)/k is true but its stated "
          "polynomial proves A' <= 1/3 instead")
    return 0


if __name__ == "__main__":
    sys.exit(main())
