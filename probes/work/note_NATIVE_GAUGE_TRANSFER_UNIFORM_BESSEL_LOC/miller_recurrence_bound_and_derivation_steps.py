#!/usr/bin/env python3
"""Probe: NATIVE_GAUGE_TRANSFER_UNIFORM_BESSEL_LOCAL_CLT_RUNG_TEN_BOUNDED_NOTE_2026-06-12.

The note's claim: for integer k >= 0, t >= 1, a = k/sqrt(t),
  |exp(-t) I_k(t) - (2 pi t)^(-1/2) exp(-a^2/2) (1 + P_1(a)/t)| <= C_0 / (sqrt(2 pi t) t^2),
  P_1(a) = (a^4 - 6a^2 + 3)/24,
  C_0 = 105 sqrt2/36864 (24/11)^(9/2) + 1/48 + 29/8 + sqrt(2 pi) (60/(11 e))^(5/2).

Machinery disjoint from the runner (scipy.special.ive on 12 t-values <= 400):
exp(-t) I_k(t) for ALL k at once by Miller backward recurrence
  I_{k-1} = (2k/t) I_k + I_{k+1},   normalised by  e^t = I_0 + 2 sum_{k>=1} I_k,
in mpmath at 50 digits (stability checked by two start indices; values
cross-checked against mpmath.besseli and against quadrature of the note's
integral representation).  Beyond the runner's sizes: t on a fine grid in
[1, 3] (non-integer), every integer t <= 200, and t = 10^(m/4) up to 10^6,
each with EVERY k <= 15 sqrt(t) + 10.

Also checked literally: each pointwise inequality of the derivation (cosine
series bounds, core integrand bound, cos 1 <= 13/24, the t-tail constant,
the Gaussian-tail and theta-tail integral bounds), the Gaussian-moment
evaluation sqrt(2/pi) B_abs = C_0 by quadrature, P_1 through the limit
t^2 R_2 -> P_2(a) = He_8(a)/1152 + He_6(a)/720 along exact a = k/sqrt(t),
and the falsifier numbers.

Prints SUMMARY: lines; HIT: only when a stated bound or step fails.
"""
import math
import sys
import time

import mpmath as mp

mp.mp.dps = 50
HITS = []


def hit(msg):
    HITS.append(msg)
    print("HIT: " + msg)


def summary(msg):
    print("SUMMARY: " + msg)


C0 = (105 * mp.sqrt(2) / 36864 * (mp.mpf(24) / 11) ** mp.mpf(4.5) + mp.mpf(1) / 48 + mp.mpf(29) / 8
      + mp.sqrt(2 * mp.pi) * (60 / (11 * mp.e)) ** mp.mpf(2.5))


def P1(a):
    return (a ** 4 - 6 * a ** 2 + 3) / 24


def miller(t, kmax, extra=None):
    """exp(-t) I_k(t) for k = 0..kmax by backward recurrence (list of mpf)."""
    t = mp.mpf(t)
    st = mp.sqrt(t)
    N = int(kmax + (extra if extra is not None else 20 * st + 100))
    y_next = mp.mpf(0)
    y = mp.mpf(10) ** -200
    ys = [mp.mpf(0)] * (N + 1)
    ys[N] = y
    for k in range(N, 0, -1):
        y_prev = (2 * k / t) * y + y_next
        y_next, y = y, y_prev
        ys[k - 1] = y                          # mpf exponents are unbounded: no rescaling needed
    norm = ys[0] + 2 * mp.fsum(ys[1:])
    return [ys[k] / norm for k in range(kmax + 1)]


def run_values_check():
    print("=" * 78)
    print("V  recurrence values: stability and cross-checks")
    worst_stab = mp.mpf(0)
    worst_bes = mp.mpf(0)
    worst_quad = mp.mpf(0)
    for t in (1, 2.5, 17, 400, 10 ** 4):
        kmax = int(15 * math.sqrt(t)) + 10
        v1 = miller(t, kmax)
        v2 = miller(t, kmax, extra=30 * math.sqrt(t) + 200)
        worst_stab = max(worst_stab, max(abs(a - b) / b for a, b in zip(v1, v2) if b > mp.mpf(10) ** -45))
        for k in sorted({0, 1, 2, kmax // 4, kmax // 2}):
            try:
                ref = mp.besseli(k, t) * mp.e ** (-mp.mpf(t))
                worst_bes = max(worst_bes, abs(v1[k] - ref) / ref)
            except mp.libmp.libhyper.NoConvergence:
                pass
        for k in (0, int(2 * math.sqrt(t))):
            tt = mp.mpf(t)
            f = lambda th: mp.e ** (-tt * (1 - mp.cos(th))) * mp.cos(k * th)
            pts = [0, 1 / mp.sqrt(tt), 4 / mp.sqrt(tt), 12 / mp.sqrt(tt)]
            pts = sorted(set(p for p in pts if p < 1)) + [1, mp.pi]
            q = mp.quad(f, pts) / mp.pi
            worst_quad = max(worst_quad, abs(v1[k] - q) / q)
    print(f"  relative change under a larger start index: {mp.nstr(worst_stab, 3)}; vs mpmath.besseli: "
          f"{mp.nstr(worst_bes, 3)}; vs quadrature of the integral representation: {mp.nstr(worst_quad, 3)}")
    if worst_stab > mp.mpf(10) ** -30 or worst_bes > mp.mpf(10) ** -30 or worst_quad > mp.mpf(10) ** -20:
        raise RuntimeError("Bessel values not reliable")
    return worst_stab, worst_bes, worst_quad


def run_bound():
    print("=" * 78)
    print("B  the absolute (all-a) and relative bounds on the grid")
    tgrid = [mp.mpf(1) + mp.mpf(j) / 100 for j in range(0, 201)]
    tgrid += [mp.mpf(n) for n in range(4, 201)]
    tgrid += [mp.mpf(10) ** (mp.mpf(m) / 4) for m in range(10, 25)]
    worst = (mp.mpf(0), None)
    worst_rel = (mp.mpf(0), None)
    npairs = 0
    for t in tgrid:
        st = mp.sqrt(t)
        kmax = int(15 * st) + 10
        vals = miller(t, kmax)
        pref = 1 / mp.sqrt(2 * mp.pi * t)
        bound = C0 * pref / t ** 2
        for k in range(kmax + 1):
            a = k / st
            g = pref * mp.e ** (-a * a / 2)
            approx = g * (1 + P1(a) / t)
            err = abs(vals[k] - approx)
            r = err / bound
            npairs += 1
            if r > worst[0]:
                worst = (r, (t, k, a))
            if g > mp.mpf(10) ** -40:
                rel = abs(vals[k] / g - 1 - P1(a) / t) / (C0 * mp.e ** (a * a / 2) / t ** 2)
                if rel > worst_rel[0]:
                    worst_rel = (rel, (t, k, a))
    t, k, a = worst[1]
    print(f"  {len(tgrid)} t-values in [1, 1e6], {npairs} (k,t) pairs: max |error| / (C_0/(sqrt(2 pi t) t^2)) = "
          f"{mp.nstr(worst[0], 6)} at t={mp.nstr(t, 6)}, k={k}; empirical C_0 needed = {mp.nstr(worst[0] * C0, 6)} "
          f"(C_0 = {mp.nstr(C0, 12)})")
    print(f"  max |R_2| / (C_0 e^(a^2/2)/t^2) = {mp.nstr(worst_rel[0], 6)} at t={mp.nstr(worst_rel[1][0], 6)}, "
          f"k={worst_rel[1][1]}")
    if worst[0] >= 1 or worst_rel[0] >= 1:
        hit(f"derived bound violated: absolute usage {mp.nstr(worst[0], 6)}, relative usage {mp.nstr(worst_rel[0], 6)}")
    return len(tgrid), npairs, worst, worst_rel


def hermite_e(n, a):
    h0, h1 = mp.mpf(1), a
    if n == 0:
        return h0
    for m in range(1, n):
        h0, h1 = h1, a * h1 - m * h0
    return h1


def run_P2_limit():
    print("=" * 78)
    print("P  t^2 R_2 -> P_2(a) = He_8/1152 + He_6/720 along exact a = k/sqrt(t)")
    rows = []
    worst_rate = mp.mpf(0)
    for a_num, a_den in ((0, 1), (1, 1), (2, 1), (3, 1), (1, 2)):
        a = mp.mpf(a_num) / a_den
        P2 = hermite_e(8, a) / 1152 + hermite_e(6, a) / 720
        seq = []
        for kk in (40, 80, 160, 320, 640):
            k = kk * a_num
            t = (mp.mpf(kk * a_den)) ** 2 if a_num else mp.mpf(kk) ** 2
            vals = miller(t, max(k, 1))
            g = mp.e ** (-a * a / 2) / mp.sqrt(2 * mp.pi * t)
            R2 = vals[k] / g - 1 - P1(a) / t
            seq.append((t, t ** 2 * R2))
        diffs = [abs(s - P2) for _, s in seq]
        # O(1/t) approach: diff * t roughly constant
        rate = [d * t for (t, _), d in zip(seq, diffs)]
        rows.append((a, P2, seq[-1][1], diffs[-1], rate[-2], rate[-1]))
        print(f"  a={mp.nstr(a, 3)}: P_2 = {mp.nstr(P2, 12)}; t^2 R_2 at t={mp.nstr(seq[-1][0], 8)}: "
              f"{mp.nstr(seq[-1][1], 12)}; |diff|*t over the last two t: {mp.nstr(rate[-2], 6)}, {mp.nstr(rate[-1], 6)}")
        if diffs[-1] > mp.mpf("1e-3"):
            hit(f"t^2 R_2 does not approach He_8/1152 + He_6/720 at a={a} (P_1 structure)")
    return rows


def run_steps():
    print("=" * 78)
    print("S  pointwise steps of the derivation")
    # (i) cosine series bounds on [0,1] (in theta; u/t)
    bad_i = 0
    for j in range(0, 2001):
        th = mp.mpf(j) / 2000
        w = mp.cos(th) - 1 + th ** 2 / 2
        if not (w >= 0 and w <= th ** 4 / 24 and th ** 4 / 24 - w <= th ** 6 / 720 and th ** 4 / 24 - w >= 0):
            bad_i += 1
    # (ii) core integrand bound, dense s-grid for several t
    worst_ii = mp.mpf(0)
    for t in (1, 1.5, 2, 3, 5, 10, 30, 100, 1000, 10 ** 4, 10 ** 5):
        t = mp.mpf(t)
        st = mp.sqrt(t)
        for j in range(1, 801):
            s = st * j / 800
            lhs = abs(mp.e ** (-t * (1 - mp.cos(s / st))) - mp.e ** (-s * s / 2) * (1 + s ** 4 / (24 * t)))
            rhs = (s ** 8 * mp.e ** (-11 * s * s / 24) / 1152 + s ** 6 * mp.e ** (-s * s / 2) / 720) / t ** 2
            if rhs > 0:
                worst_ii = max(worst_ii, lhs / rhs)
    # (iii) cos 1 <= 13/24
    c1 = mp.cos(1)
    # (iv) sup_{t>=1} t^(5/2) exp(-11t/24) = (60/(11e))^(5/2) at t = 60/11
    K = (60 / (11 * mp.e)) ** mp.mpf(2.5)
    sup_iv = max(mp.mpf(t) ** mp.mpf(2.5) * mp.e ** (-11 * mp.mpf(t) / 24) for t in
                 [1 + mp.mpf(j) / 200 for j in range(0, 4001)])
    # (v) Gaussian tail and (vi) theta tail
    worst_v = mp.mpf(0)
    worst_vi = mp.mpf(0)
    for t in (1, 1.5, 2, 3, 5, 10, 30, 100, 1000):
        t = mp.mpf(t)
        st = mp.sqrt(t)
        gt = mp.quad(lambda s: mp.e ** (-s * s / 2) * (1 + s ** 4 / (24 * t)), [st, st + 5, mp.inf])
        gb = (mp.quad(lambda s: s ** 4 * mp.e ** (-s * s / 2), [0, mp.inf])
              + mp.quad(lambda s: s ** 6 * mp.e ** (-s * s / 2), [0, mp.inf]) / 24) / t ** 2
        worst_v = max(worst_v, gt / gb)
        tt = mp.quad(lambda s: mp.e ** (-t * (1 - mp.cos(s / st))), [st, 2 * st, mp.pi * st])
        tb1 = mp.pi * st * mp.e ** (-11 * t / 24)
        tb2 = mp.pi * K / t ** 2
        worst_vi = max(worst_vi, tt / tb1, tb1 / tb2)
    print(f"  (i) cosine-series bounds on 2001 theta in [0,1]: failures {bad_i}")
    print(f"  (ii) core integrand |exact - Gaussian(1 + s^4/24t)| / bound: max {mp.nstr(worst_ii, 9)} "
          f"(11 t-values, 800 s-points each)")
    print(f"  (iii) cos 1 = {mp.nstr(c1, 12)} <= 13/24 = {mp.nstr(mp.mpf(13) / 24, 12)}: {c1 <= mp.mpf(13) / 24}")
    print(f"  (iv) max t^(5/2) e^(-11t/24) on [1,21] = {mp.nstr(sup_iv, 12)} vs (60/(11e))^(5/2) = {mp.nstr(K, 12)}")
    print(f"  (v) Gaussian tail / t^-2 (3 + 5/8) sqrt(pi/2): max {mp.nstr(worst_v, 6)}; (vi) theta tail ratios max "
          f"{mp.nstr(worst_vi, 6)}")
    if bad_i or worst_ii > 1 or c1 > mp.mpf(13) / 24 or sup_iv > K * (1 + mp.mpf(10) ** -30) or worst_v > 1 \
            or worst_vi > 1:
        hit("a pointwise step of the derivation fails")
    # (vii) moments: sqrt(2/pi) B_abs = C_0
    m8 = mp.quad(lambda s: s ** 8 * mp.e ** (-11 * s * s / 24), [0, mp.inf]) / 1152
    m6 = mp.quad(lambda s: s ** 6 * mp.e ** (-s * s / 2), [0, mp.inf]) / 720
    m4 = mp.quad(lambda s: s ** 4 * mp.e ** (-s * s / 2), [0, mp.inf])
    m6b = mp.quad(lambda s: s ** 6 * mp.e ** (-s * s / 2), [0, mp.inf]) / 24
    Babs = m8 + m6 + m4 + m6b + mp.pi * K
    dev = abs(mp.sqrt(2 / mp.pi) * Babs - C0)
    parts = [mp.sqrt(2 / mp.pi) * x for x in (m8, m6, m4 + m6b, mp.pi * K)]
    print(f"  (vii) sqrt(2/pi) B_abs by quadrature = {mp.nstr(mp.sqrt(2 / mp.pi) * Babs, 20)}; closed-form C_0 = "
          f"{mp.nstr(C0, 20)}; |diff| = {mp.nstr(dev, 3)}; pieces {[mp.nstr(p, 10) for p in parts]}")
    if dev > mp.mpf(10) ** -25:
        hit("C_0 closed form differs from the Gaussian-moment evaluation")
    return bad_i, worst_ii, c1, sup_iv, K, worst_v, worst_vi, dev, parts


def run_falsifier_numbers():
    print("=" * 78)
    print("F  falsifier numbers")
    wrong = mp.e ** (-mp.mpf(1) ** 2 * 64 / 2)
    right = mp.e ** (-mp.mpf(1) / 2)
    p0, p2 = P1(mp.mpf(0)), P1(mp.mpf(2))
    fixed = [(-1 + 1 / (8 * mp.mpf(t))) for t in (1, 4, 64)]
    # the fixed-index factor 1 - (4k^2-1)/(8t) at k = 2 sqrt(t)
    fixed_direct = [1 - (4 * (2 * mp.sqrt(mp.mpf(t))) ** 2 - 1) / (8 * mp.mpf(t)) for t in (1, 4, 64)]
    print(f"  wrong scaling a=1,t=64: exp(-32) = {mp.nstr(wrong, 8)} vs exp(-1/2) = {mp.nstr(right, 8)}")
    print(f"  P_1(0) = {mp.nstr(p0, 10)} (1/8), P_1(2) = {mp.nstr(p2, 10)} (-5/24); reversed-sign value +5/24")
    print(f"  fixed-index factor at k = 2 sqrt t, t = 1, 4, 64: {[mp.nstr(f, 8) for f in fixed_direct]} "
          f"(= -1 + 1/(8t): {[mp.nstr(f, 8) for f in fixed]}); local-CLT factor exp(-2) = {mp.nstr(mp.e ** -2, 8)}")
    ok = (abs(p0 - mp.mpf(1) / 8) < mp.mpf(10) ** -40 and abs(p2 + mp.mpf(5) / 24) < mp.mpf(10) ** -40
          and all(abs(a - b) < mp.mpf(10) ** -40 for a, b in zip(fixed, fixed_direct)) and all(f < 0 for f in fixed))
    if not ok:
        hit("falsifier numbers differ from the note")
    return p0, p2


def main():
    t0 = time.time()
    ws, wb, wq = run_values_check()
    summary(f"V Miller-recurrence e^-t I_k(t) (50 digits): stability {mp.nstr(ws, 2)}, vs mpmath.besseli "
            f"{mp.nstr(wb, 2)}, vs quadrature of the integral representation {mp.nstr(wq, 2)}")
    nt, npairs, worst, worst_rel = run_bound()
    summary(f"B {nt} t-values in [1,1e6] (fine grid on [1,3], integers <= 200, 10^(m/4) to 1e6), every k <= "
            f"15 sqrt t + 10 ({npairs} pairs): max absolute-bound usage {mp.nstr(worst[0], 6)} at t="
            f"{mp.nstr(worst[1][0], 5)}, k={worst[1][1]} (empirical C_0 need {mp.nstr(worst[0] * C0, 5)} vs C_0 = "
            f"{mp.nstr(C0, 10)}); max relative-bound usage {mp.nstr(worst_rel[0], 6)}")
    rows = run_P2_limit()
    summary("P t^2 R_2 -> He_8/1152 + He_6/720: " + "; ".join(
        f"a={mp.nstr(a, 3)}: limit {mp.nstr(P2, 8)}, value at the largest t {mp.nstr(v, 8)}"
        for a, P2, v, d, r1, r2 in rows))
    bad_i, wii, c1, sup_iv, K, wv, wvi, dev, parts = run_steps()
    summary(f"S derivation steps: cosine bounds failures {bad_i}; core integrand bound usage max {mp.nstr(wii, 9)} "
            f"(< 1; tight only as s -> 0 where both sides ~ s^6/(720 t^2)); "
            f"cos1 = {mp.nstr(c1, 8)} <= 13/24; t-tail sup {mp.nstr(sup_iv, 10)} = (60/(11e))^(5/2) "
            f"{mp.nstr(K, 10)}; Gaussian-tail usage {mp.nstr(wv, 4)}; theta-tail usage {mp.nstr(wvi, 4)}; "
            f"moments give C_0 to {mp.nstr(dev, 2)} with pieces {[mp.nstr(p, 8) for p in parts]}")
    p0, p2 = run_falsifier_numbers()
    summary(f"F P_1(0) = {mp.nstr(p0, 6)}, P_1(2) = {mp.nstr(p2, 6)}, wrong-scaling exp(-32) vs exp(-1/2), "
            f"fixed-index factor -1 + 1/(8t) < 0")
    print("=" * 78)
    summary(f"hits={len(HITS)}; runtime {time.time() - t0:.0f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
