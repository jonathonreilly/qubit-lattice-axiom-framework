#!/usr/bin/env python3
"""J:attack-g:PR8171 - block 27 (PR #8171), pattern (g) PROOF STEP BY BRUTE FORCE, on T1(c) - the step that makes A(kappa)/kappa
decreasing and so fixes the constant 1/(2 sqrt3) of T1(d), T2's contraction rate sqrt3 beta and the region beta < 1/sqrt3.

The step as written: "1 - 3A/kappa - A^2 = (kappa A' - A)/kappa ... Multiplying kappa A' <= A by kappa sinh^2 kappa:
sinh^2 kappa - kappa^2 <= kappa sinh kappa cosh kappa - sinh^2 kappa, i.e. 2 sinh^2 kappa <= (kappa/2) sinh 2kappa + kappa^2. Both sides
are power series with 2 sinh^2 kappa = cosh 2kappa - 1 = sum_{m>=1} (2 kappa)^{2m}/(2m)! and (kappa/2) sinh 2kappa =
sum_{m>=1} (2 kappa)^{2m} (m/2)/(2m)!; the difference is kappa^2 - kappa^2 + sum_{m>=2} (2^{2m}/(2m)!)(m/2 - 1) kappa^{2m} >= 0
(B3: the coefficients 0, 0, 2/45, 2/315, ...)".

Verified literally, with machinery disjoint from the runner's sympy series:
  * the Taylor coefficients of 2 sinh^2 k, (k/2) sinh 2k and k^2 built exactly (fractions) from the exponential series e^{+-2k}, term by
    term to k^80, against each displayed series, the displayed difference formula, and the listed coefficients 0, 0, 2/45, 2/315;
  * each equality and equivalence of the chain evaluated at 50 digits at 400 points of (0, 60] (A = coth k - 1/k, A' = 1/k^2 - 1/sinh^2 k),
    the sign of 1 - 3A/k - A^2 and the monotonicity of A/k on that grid, and A/k <= 1/3;
  * the consequence the step feeds, TV(K_V, K_V') <= |V - V'|/(2 sqrt3), by quadrature on the sphere (Gauss-Legendre in the cosine x
    uniform azimuth) at kappa = 0 ... 20 and small shifts in the parallel, perpendicular and oblique directions.
HIT if a coefficient, a link of the chain, or the bound fails.
"""
import math
import sys
from fractions import Fraction

import mpmath as mp
import numpy as np

mp.mp.dps = 50


def exp_series(a, n):
    """coefficients of e^{a k} up to k^n, exact"""
    return [Fraction(a) ** j / math.factorial(j) for j in range(n + 1)]


def main():
    n = 80
    ep, em = exp_series(2, n), exp_series(-2, n)
    sinh2 = [(x - y) / 2 for x, y in zip(ep, em)]                   # sinh 2k
    cosh2 = [(x + y) / 2 for x, y in zip(ep, em)]                   # cosh 2k
    two_sinh_sq = [c - (1 if j == 0 else 0) for j, c in enumerate(cosh2)]   # 2 sinh^2 k = cosh 2k - 1
    half_k_sinh2 = [Fraction(0)] + [c / 2 for c in sinh2[:-1]]      # (k/2) sinh 2k
    ksq = [Fraction(1) if j == 2 else Fraction(0) for j in range(n + 1)]
    diff = [h + q - t for h, q, t in zip(half_k_sinh2, ksq, two_sinh_sq)]
    ok_series = True
    for m in range(1, n // 2 + 1):
        j = 2 * m
        ok_series &= two_sinh_sq[j] == Fraction(2 ** j, math.factorial(j))
        ok_series &= half_k_sinh2[j] == Fraction(2 ** j, math.factorial(j)) * Fraction(m, 2)
        if m >= 2:
            ok_series &= diff[j] == Fraction(2 ** j, math.factorial(j)) * (Fraction(m, 2) - 1)
    odd_zero = all(two_sinh_sq[j] == 0 and half_k_sinh2[j] == 0 and diff[j] == 0 for j in range(1, n + 1, 2))
    listed = [diff[2], diff[4], diff[6], diff[8]]
    listed_ok = listed == [0, 0, Fraction(2, 45), Fraction(2, 315)]
    nonneg = all(c >= 0 for c in diff)
    print(f"[series] exact coefficients from e^(+-2k) to k^{n}: 2 sinh^2 k = sum (2k)^(2m)/(2m)!, (k/2) sinh 2k = sum (2k)^(2m)(m/2)/(2m)!, "
          f"difference = sum_(m>=2) (2^(2m)/(2m)!)(m/2 - 1) k^(2m): {ok_series}; odd coefficients vanish: {odd_zero}; coefficients of k^2, k^4, "
          f"k^6, k^8 = {[str(x) for x in listed]} (listed 0, 0, 2/45, 2/315: {listed_ok}); every coefficient >= 0: {nonneg}")
    # ---- the chain at 50 digits
    ks = [mp.mpf(i) / 400 * 60 for i in range(1, 401)] + [mp.mpf(1) / 10 ** 3, mp.mpf(1) / 10 ** 2]
    worst = {"id1": 0, "mult_left": 0, "mult_right": 0, "sign": -mp.inf, "series_vs_closed": 0}
    prev = None
    mono = True
    le_third = True
    for k in sorted(ks):
        A = mp.coth(k) - 1 / k
        Ad = 1 / k ** 2 - 1 / mp.sinh(k) ** 2
        lhs = 1 - 3 * A / k - A ** 2
        rhs = (k * Ad - A) / k
        worst["id1"] = max(worst["id1"], abs(lhs - rhs))
        a1, b1 = k * mp.sinh(k) ** 2 * k * Ad, mp.sinh(k) ** 2 - k ** 2
        a2, b2 = k * mp.sinh(k) ** 2 * A, k * mp.sinh(k) * mp.cosh(k) - mp.sinh(k) ** 2
        worst["mult_left"] = max(worst["mult_left"], abs(a1 - b1) / max(1, abs(b1)))
        worst["mult_right"] = max(worst["mult_right"], abs(a2 - b2) / max(1, abs(b2)))
        worst["sign"] = max(worst["sign"], lhs)
        closed = (k / 2) * mp.sinh(2 * k) + k ** 2 - 2 * mp.sinh(k) ** 2
        ser = mp.fsum(mp.mpf(diff[j].numerator) / diff[j].denominator * k ** j for j in range(0, n + 1)) if k < 8 else closed
        worst["series_vs_closed"] = max(worst["series_vs_closed"], abs(ser - closed) / max(1, abs(closed)))
        r = A / k
        if prev is not None and r > prev:
            mono = False
        prev = r
        le_third &= r <= mp.mpf(1) / 3
    print(f"[chain] at {len(ks)} points of (0, 60], 50 digits: max |(1 - 3A/k - A^2) - (kA' - A)/k| = {mp.nstr(worst['id1'], 3)}; "
          f"k sinh^2 k * kA' vs sinh^2 k - k^2: {mp.nstr(worst['mult_left'], 3)} (relative); k sinh^2 k * A vs k sinh k cosh k "
          f"- sinh^2 k: {mp.nstr(worst['mult_right'], 3)} (relative); truncated series (k < 8) vs closed form: {mp.nstr(worst['series_vs_closed'], 3)} relative; "
          f"max of 1 - 3A/k - A^2: {mp.nstr(worst['sign'], 5)} (must be <= 0); A/k decreasing on the grid: {mono}; A/k <= 1/3: {le_third}")
    # ---- the consequence, TV <= |dV|/(2 sqrt3), by quadrature
    xg, wg = np.polynomial.legendre.leggauss(400)
    ph = np.linspace(0, 2 * np.pi, 800, endpoint=False)
    X, P = np.meshgrid(xg, ph, indexing="ij")
    W = np.outer(wg, np.full(len(ph), 2 * np.pi / len(ph)))
    S = np.stack([np.sqrt(1 - X ** 2) * np.cos(P), np.sqrt(1 - X ** 2) * np.sin(P), X], axis=-1)

    def dens(V):
        k = np.linalg.norm(V)
        if k == 0:
            return np.full(X.shape, 1 / (4 * np.pi))
        return k / (4 * np.pi * np.sinh(k)) * np.exp(S @ V) if k < 30 else k / (2 * np.pi) * np.exp(S @ V - k) / (1 - np.exp(-2 * k))

    worst_ratio, where = 0.0, None
    for k in (0.0, 0.1, 0.5, 1.0, 2.0, 5.0, 10.0, 20.0):
        V = np.array([0.0, 0.0, k])
        for dirn in (np.array([0, 0, 1.0]), np.array([1.0, 0, 0]), np.array([1.0, 0, 1.0]) / math.sqrt(2)):
            for h in (1e-3, 0.05):
                tv = 0.5 * np.sum(W * np.abs(dens(V) - dens(V + h * dirn)))
                ratio = tv / h
                if ratio > worst_ratio:
                    worst_ratio, where = ratio, (k, tuple(np.round(dirn, 3)), h)
    bound = 1 / (2 * math.sqrt(3))
    print(f"[consequence] TV(K_V, K_V+h d)/h by quadrature (400 x 800 nodes) at kappa = 0 ... 20, three directions, h = 1e-3, 0.05: max "
          f"{worst_ratio:.6f} at (kappa, d, h) = {where}; the bound 1/(2 sqrt3) = {bound:.6f}; the Reading's 1/4 at V = 0")
    hits = []
    if not (ok_series and odd_zero and listed_ok and nonneg):
        hits.append(f"the series step: formula {ok_series}, listed coefficients {[str(x) for x in listed]}, non-negative {nonneg}")
    if not (worst["id1"] < mp.mpf(10) ** -40 and worst["mult_left"] < mp.mpf(10) ** -40 and worst["mult_right"] < mp.mpf(10) ** -40
            and worst["sign"] <= 0 and mono and le_third):
        hits.append(f"the chain: identity {mp.nstr(worst['id1'], 3)}, sign {mp.nstr(worst['sign'], 5)}, monotone {mono}, <= 1/3 {le_third}")
    if worst_ratio > bound:
        hits.append(f"TV/|dV| = {worst_ratio} exceeds 1/(2 sqrt3) at {where}")
    for h in hits:
        print("HIT: " + h)
    print(f"SUMMARY: pattern (g) PROOF STEP BY BRUTE FORCE on T1(c) - the three displayed power series and the difference formula hold "
          f"coefficient by coefficient to k^{n} from the exponential series, the listed coefficients are 0, 0, 2/45, 2/315, every coefficient is "
          f">= 0, each link of the chain holds at 402 points to 50 digits, 1 - 3A/k - A^2 <= 0 and A/k decreases and stays <= 1/3 on (0, 60], "
          f"and the consequence TV/|dV| peaks at {worst_ratio:.4f} (<= 1/(2 sqrt3) = {bound:.4f}); {len(hits)} failures; the step "
          f"{'fails' if hits else 'holds as written'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
