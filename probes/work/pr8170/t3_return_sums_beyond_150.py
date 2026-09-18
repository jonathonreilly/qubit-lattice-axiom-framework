#!/usr/bin/env python3
"""J:falsifier:PR8170 - block 26 (PR #8170), falsifier bullet D: "a P_k outside the stated two-sided bounds ... or
sum_{k<=t} P_k < (3 sqrt3/(4 pi)) H_t - 6/25 at some t <= 150", run far beyond the note's k, t <= 150.

Objects (the note's).  The three-predecessor level walk: one step moves by (0,0), (-1,0) or (0,-1), each with probability 1/3; p_k its law
after k steps; P_k = sum_y p_k(y)^2 (the return sums).  Stated (T3), for every k >= 1:
    3 sqrt3/(4 pi k) - 1/k^2 - (5/(2k)) e^{-k/4}  <=  P_k  <=  3 sqrt3/(4 pi k) + 27/k^2 + e^{-sqrt(k)/7},
and sum_{k<=t} P_k >= (3 sqrt3/(4 pi)) H_t - 1/4 for every t >= 1 (with - 6/25 for t <= 150, from the exact sums).
Machinery disjoint from the runner (which enumerates the trinomial form for k <= 150):
  (1) exact rationals for k <= K_EXACT from the one-dimensional identity sum_{a+b+c=k} (k!/(a! b! c!))^2 = sum_j C(k,j)^2 C(2j,j)
      (Vandermonde on the inner sum), so P_k = 9^{-k} sum_j C(k,j)^2 C(2j,j); the bounds compared exactly with rational enclosures of
      sqrt3, pi and the exponentials; the partial sums S_t = sum_{k=1..t} P_k compared exactly with c0 H_t - 6/25 and c0 H_t - 1/4;
  (2) for k up to 10^6, P_k = (2 pi)^{-2} int u(theta)^k (u = |phi|^2, the difference walk's characteristic function) by the periodic
      trapezoid rule on an M x M grid, M = min(k + 1, 60 sqrt(k) + 64): the rule is exact for M > k, and for smaller M the aliasing error
      is the difference walk's mass at distance >= M, below 4 exp(-M^2/(8k)) by Hoeffding (steps bounded by 1 per coordinate, variance
      proxy 2k), plus a floating-point allowance (k 1e-15 + 1e-13) P_k; the bounds are compared with this error included.
HIT if a bound fails (exactly in (1), beyond the error bars in (2)).  INFO: k^2 (P_k - c0/k), the coefficient the bounds confine to
[-1, 27] as k grows.
"""
import sys
import time
from fractions import Fraction as Fr
from math import comb, exp, pi, sqrt

import numpy as np

K_EXACT = 2000
K_FLOAT = [2000, 3000, 5000, 10 ** 4, 2 * 10 ** 4, 5 * 10 ** 4, 10 ** 5, 2 * 10 ** 5, 5 * 10 ** 5, 10 ** 6]


def enclosures():
    # sqrt3 and pi by rational bounds; c0 = 3 sqrt3/(4 pi)
    s3_lo, s3_hi = Fr(17320508075688772, 10 ** 16), Fr(17320508075688773, 10 ** 16)
    assert s3_lo ** 2 < 3 < s3_hi ** 2
    pi_lo, pi_hi = Fr(31415926535897932, 10 ** 16), Fr(31415926535897933, 10 ** 16)
    return 3 * s3_lo / (4 * pi_hi), 3 * s3_hi / (4 * pi_lo)


def exp_neg_bounds(x):
    """rational enclosure of e^{-x}, x >= 0 rational: 1/e^{x} with e^{x} enclosed by its series."""
    n = int(3 * float(x)) + 40
    s, term = Fr(0), Fr(1)
    for k in range(n + 1):
        s += term
        term = term * x / (k + 1)
    hi_e = s + term / (1 - x / (n + 2))
    return 1 / hi_e, 1 / s


def sqrt_bounds(q):
    lo = Fr(int(sqrt(float(q)) * 10 ** 9), 10 ** 9)
    while lo * lo > q:
        lo -= Fr(1, 10 ** 9)
    hi = lo + Fr(1, 10 ** 9)
    while hi * hi < q:
        hi += Fr(1, 10 ** 9)
    return lo, hi


def part_exact():
    c0_lo, c0_hi = enclosures()
    print(f"== (1) exact P_k for k = 1..{K_EXACT} (P_k = 9^-k sum_j C(k,j)^2 C(2j,j)); c0 = 3 sqrt3/(4 pi) in [{float(c0_lo):.15f}, {float(c0_hi):.15f}]")
    t0 = time.time()
    fails_lo, fails_hi, fails_h, fails_h150 = [], [], [], []
    S = Fr(0)
    H = Fr(0)
    coef = []
    minmarg_h = None
    cnj = [comb(2 * j, j) for j in range(K_EXACT + 1)]
    e50_lo, e50_hi = exp_neg_bounds(Fr(50))
    ambiguous = []
    for k in range(1, K_EXACT + 1):
        num = sum(comb(k, j) ** 2 * cnj[j] for j in range(k + 1))
        P = Fr(num, 9 ** k)
        S += P
        H += Fr(1, k)
        # a bound is certified when it holds with the stringent enclosures and violated only when it fails with the lenient ones
        if k < 200:
            em_lo, em_hi = exp_neg_bounds(Fr(k, 4))
        else:
            em_lo, em_hi = Fr(0), e50_hi                     # e^{-k/4} <= e^{-50} for k >= 200
        low_strict = c0_hi / k - Fr(1, k * k) - Fr(5, 2 * k) * em_lo
        low_lenient = c0_lo / k - Fr(1, k * k) - Fr(5, 2 * k) * em_hi
        sq_lo, sq_hi = sqrt_bounds(Fr(k))
        e2_lo, _ = exp_neg_bounds(sq_hi / 7)
        _, e2_hi = exp_neg_bounds(sq_lo / 7)
        up_strict = c0_lo / k + Fr(27, k * k) + e2_lo
        up_lenient = c0_hi / k + Fr(27, k * k) + e2_hi
        if P < low_lenient:
            fails_lo.append(k)
        elif P < low_strict:
            ambiguous.append(("lower", k))
        if P > up_lenient:
            fails_hi.append(k)
        elif P > up_strict:
            ambiguous.append(("upper", k))
        if S < c0_hi * H - Fr(1, 4):
            if S < c0_lo * H - Fr(1, 4):
                fails_h.append(k)
            else:
                ambiguous.append(("harmonic", k))
        if k <= 150 and S < c0_hi * H - Fr(6, 25):
            if S < c0_lo * H - Fr(6, 25):
                fails_h150.append(k)
            else:
                ambiguous.append(("harmonic150", k))
        m = S - c0_hi * H
        minmarg_h = m if minmarg_h is None or m < minmarg_h else minmarg_h
        if k in (1, 2, 10, 150, 500, 1000, K_EXACT):
            coef.append((k, float(k * k * (P - (c0_lo + c0_hi) / 2 / k)), float(S - (c0_lo + c0_hi) / 2 * H)))
    print(f"[1] lower bound violated at {len(fails_lo)} k; upper bound violated at {len(fails_hi)} k; S_t < c0 H_t - 1/4 at {len(fails_h)} t; "
          f"S_t < c0 H_t - 6/25 at {len(fails_h150)} t <= 150; undecided by the enclosures: {len(ambiguous)} {ambiguous[:5]}   ({time.time() - t0:.0f}s)")
    print(f"[1] min over t <= {K_EXACT} of S_t - c0 H_t = {float(minmarg_h):.6f} (bounds: -6/25 = -0.24 for t <= 150, -1/4 beyond)")
    for k, c, s in coef:
        print(f"[1]   k = {k:5d}: k^2 (P_k - c0/k) = {c:+.6f}; S_k - c0 H_k = {s:+.6f}")
    return fails_lo, fails_hi, fails_h, fails_h150


def part_float():
    c0 = 3 * sqrt(3) / (4 * pi)
    print(f"== (2) P_k by the periodic trapezoid rule for k up to {K_FLOAT[-1]} (aliasing bounded by Hoeffding)")
    fails = []
    for k in K_FLOAT:
        t0 = time.time()
        M = min(k + 1, int(60 * sqrt(k)) + 64)
        alias = 0.0 if M > k else 4 * exp(-M * M / (8 * k))
        th = 2 * np.pi * np.arange(M) / M
        tot = 0.0
        for i0 in range(0, M, 512):
            t1 = th[i0:i0 + 512][:, None]
            u = (3 + 2 * np.cos(t1) + 2 * np.cos(th[None, :]) + 2 * np.cos(t1 - th[None, :])) / 9
            tot += np.sum(u ** k)
        P = tot / (M * M)
        rnd = (k * 1e-15 + 1e-13) * P + 1e-300              # u^k amplifies the rounding of u (about 4e-16) by k; summation adds ~1e-13
        err = alias + rnd
        lower = c0 / k - 1 / k ** 2 - 2.5 / k * exp(-k / 4)
        upper = c0 / k + 27 / k ** 2 + exp(-sqrt(k) / 7)
        ok = (P + err >= lower) and (P - err <= upper)
        if not ok:
            fails.append(k)
        print(f"[2] k = {k:8d}: M = {M:6d}, P_k = {P:.12e} (error <= {err:.1e}); k^2 (P_k - c0/k) = {k * k * (P - c0 / k):+.6f}; "
              f"margins in units of 1/k^2: lower {k * k * (P - lower):+.4f}, upper {k * k * (upper - P):+.4f}  ({time.time() - t0:.0f}s)")
    return fails


def main():
    t0 = time.time()
    lo, hi, h, h150 = part_exact()
    fl = part_float()
    print(f"[time] {time.time() - t0:.0f}s")
    if lo:
        print(f"HIT: T3 lower bound violated (exact) at k = {lo[:10]}")
    if hi:
        print(f"HIT: T3 upper bound violated (exact) at k = {hi[:10]}")
    if h:
        print(f"HIT: T3 harmonic bound S_t >= c0 H_t - 1/4 violated (exact) at t = {h[:10]}")
    if h150:
        print(f"HIT: T3 exact-range bound S_t >= c0 H_t - 6/25 violated at t = {h150[:10]}")
    if fl:
        print(f"HIT: T3 bounds violated beyond the error bars at k = {fl}")
    print(f"SUMMARY: T3 return sums: exact k <= {K_EXACT}: {len(lo)} lower and {len(hi)} upper violations, harmonic bound violated at "
          f"{len(h)} t (6/25 version at {len(h150)} t <= 150); trapezoid k up to {K_FLOAT[-1]}: {len(fl)} violations; k^2 (P_k - c0/k) tends to "
          f"about -0.1034 (the bounds allow [-1, 27]); falsifier {'FIRES' if (lo or hi or h or h150 or fl) else 'does not fire'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
