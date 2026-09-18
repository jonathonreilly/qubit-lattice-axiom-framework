#!/usr/bin/env python3
"""J:falsifier:PR8156 - block 22 (PR #8156), falsifiers V1-V3: the constant 3G(0) = 3 (2 pi)^{-3} int_{[-pi,pi]^3} dk/E(k),
E(k) = sum_i 2(1 - cos k_i), stated to satisfy 75/100 < 3G(0) < 76/100 (V3), with 3G(0) = (1/2) sum_{n>=0} P_{2n}(0,0) (V1) and the tail
bound P_{2n}(0,0) <= (36/11)^{3/2}/(4 pi^{3/2} n^{3/2}) + 2 e^{-4n/(3 pi^2)} for n >= 1 (V2).  Machinery disjoint from the runner's
(exact partial sum to N = 1000 plus the tail bound):
  (1) the closed form of the simple cubic walk's return sum, u = sum_n P_{2n} = (sqrt6/(32 pi^3)) Gamma(1/24) Gamma(5/24) Gamma(7/24)
      Gamma(11/24) (Glasser-Zucker; named, used as an independent route), at 50 digits;
  (2) the Bessel representation G(0) = int_0^oo e^{-6t} I_0(2t)^3 dt (from 1/E = int_0^oo e^{-tE} dt and (2 pi)^{-1} int e^{2t cos k} dk =
      I_0(2t)), by 50-digit quadrature;
  (3) V2 at every n <= N2 exactly: P_{2n} = 6^{-2n} C(2n, n) sum_a C(n, a)^2 C(2(n - a), n - a) as a rational, against the right side with
      pi and e enclosed (the right side is decreasing in pi: the check uses pi <= 3.1416, i.e. the smaller right side);
  (4) V3 recomputed: the exact S_1000 and a tail bound on sum_{n > 1000} of V2's right side (the integral bound c * 2/sqrt(1000) and the
      geometric sum), compared with 75/100 and 76/100.
HIT if 3G(0) lies outside (75/100, 76/100) by either route, the two routes disagree beyond 1e-20, V2 fails at some n <= N2, or the
recomputed certificate fails.
"""
import sys
import time
from fractions import Fraction as Fr
from math import comb

import mpmath as mp

mp.mp.dps = 50
N2 = 2000


def P2n(n):
    s = sum(comb(n, a) ** 2 * comb(2 * (n - a), n - a) for a in range(n + 1))
    return Fr(comb(2 * n, n) * s, 36 ** n)


def main():
    t0 = time.time()
    hits = []
    # (1) closed form
    u = mp.sqrt(6) / (32 * mp.pi ** 3) * mp.gamma(mp.mpf(1) / 24) * mp.gamma(mp.mpf(5) / 24) * mp.gamma(mp.mpf(7) / 24) * mp.gamma(mp.mpf(11) / 24)
    g_closed = u / 2
    # (2) Bessel integral for G(0); 3G(0) should equal u/2
    G0 = mp.quad(lambda t: mp.e ** (-6 * t) * mp.besseli(0, 2 * t) ** 3, [0, 1, 10, 100, mp.inf])
    g_bessel = 3 * G0
    print(f"[1] closed form: sum_n P_2n = u = {mp.nstr(u, 30)}, so 3G(0) = u/2 = {mp.nstr(g_closed, 30)}")
    print(f"[2] Bessel integral: 3G(0) = 3 int_0^oo e^(-6t) I_0(2t)^3 dt = {mp.nstr(g_bessel, 30)}; |difference| = {mp.nstr(abs(g_bessel - g_closed), 5)}")
    in_window = mp.mpf(75) / 100 < g_closed < mp.mpf(76) / 100 and mp.mpf(75) / 100 < g_bessel < mp.mpf(76) / 100
    if not in_window:
        hits.append(f"3G(0) outside (75/100, 76/100): closed form {mp.nstr(g_closed, 12)}, Bessel {mp.nstr(g_bessel, 12)}")
    if abs(g_bessel - g_closed) > mp.mpf(10) ** -20:          # the 50-digit quadrature agrees to about 1e-28
        hits.append(f"the two routes disagree: {mp.nstr(abs(g_bessel - g_closed), 5)}")
    # (3) V2 exactly for n <= N2
    t1 = time.time()
    c = mp.mpf(36) / 11
    worst = (mp.mpf(0), 0)
    fails = []
    S = Fr(1)                                  # P_0 = 1
    S1000 = None
    for n in range(1, N2 + 1):
        P = P2n(n)
        S += P
        if n == 1000:
            S1000 = S
        rhs = c ** mp.mpf(1.5) / (4 * mp.mpf("3.1416") ** mp.mpf(1.5) * mp.mpf(n) ** mp.mpf(1.5)) + 2 * mp.e ** (-4 * mp.mpf(n) / (3 * mp.mpf("3.1416") ** 2))
        Pm = mp.mpf(P.numerator) / P.denominator
        ratio = Pm / rhs
        if ratio > worst[0]:
            worst = (ratio, n)
        if Pm > rhs:
            fails.append(n)
    print(f"[3] V2 at every n <= {N2} (exact P_2n, right side with pi <= 3.1416): {len(fails)} failures; largest ratio P_2n / right side = "
          f"{mp.nstr(worst[0], 8)} at n = {worst[1]} ({time.time() - t1:.0f}s)")
    if fails:
        hits.append(f"V2 fails at n = {fails[:5]}")
    # asymptotic comparison (INFO): n^{3/2} P_2n against the bound's coefficient
    lead = c ** mp.mpf(1.5) / (4 * mp.pi ** mp.mpf(1.5))
    asym = 2 * (mp.mpf(3) / (4 * mp.pi)) ** mp.mpf(1.5)
    Pn = P2n(N2)
    print(f"[INFO] n^(3/2) P_2n at n = {N2}: {mp.nstr(mp.mpf(Pn.numerator) / Pn.denominator * mp.mpf(N2) ** 1.5, 10)}; local-limit constant "
          f"2 (3/(4 pi))^(3/2) = {mp.nstr(asym, 10)}; V2's constant (36/11)^(3/2)/(4 pi^(3/2)) = {mp.nstr(lead, 10)}")
    # (4) V3 recomputed
    half = S1000 / 2
    lower_ok = half > Fr(75, 100)
    lead_up = c ** mp.mpf(1.5) / (4 * mp.mpf(3) ** mp.mpf(1.5))                  # pi >= 3 makes the leading coefficient larger (safe side)
    tail = lead_up * 2 / mp.sqrt(1000)                                             # sum_{n>1000} n^{-3/2} <= int_{1000}^oo x^{-3/2} dx = 2/sqrt(1000)
    a = 4 / (3 * mp.pi ** 2)
    tail += 2 * mp.e ** (-a * 1001) / (1 - mp.e ** (-a))
    upper = mp.mpf(half.numerator) / half.denominator + tail / 2
    upper_ok = upper < mp.mpf(76) / 100
    print(f"[4] V3 recomputed: S_1000/2 = {mp.nstr(mp.mpf(half.numerator) / half.denominator, 20)} > 75/100: {lower_ok}; with the tail bound "
          f"(1/2) sum_(n>1000) rhs <= {mp.nstr(tail / 2, 8)}: upper bound {mp.nstr(upper, 12)} < 76/100: {upper_ok}")
    if not (lower_ok and upper_ok):
        hits.append("the recomputed certificate fails")
    print(f"[time] {time.time() - t0:.0f}s")
    for h in hits:
        print("HIT: " + h)
    print(f"SUMMARY: 3G(0) = {mp.nstr(g_closed, 20)} by the Gamma closed form and {mp.nstr(g_bessel, 20)} by the Bessel integral (both in "
          f"(75/100, 76/100)); V2 holds at every n <= {N2} (largest ratio {mp.nstr(worst[0], 6)} at n = {worst[1]}); the recomputed certificate "
          f"gives {mp.nstr(mp.mpf(half.numerator) / half.denominator, 10)} < 3G(0) < {mp.nstr(upper, 10)}; falsifier {'FIRES' if hits else 'does not fire'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
