#!/usr/bin/env python3
"""J:attack:PR8156 - block 22 (PR #8156), attack pattern (f) NORMALIZATION: every factor between block 19's torus constant and the
note's return sum, recomputed by brute force, and the certificate recomputed along a separate code path.
  * the torus constant g_L = N^{-1} sum_{k != 0} 1/E(k), E(k) = sum_i 2(1 - cos k_i), on L^3 tori, L = 4..256, extrapolated in odd
    powers of 1/L (two Richardson steps), against G(0) = int_0^inf (e^{-2t} I_0(2t))^3 dt by 40-digit quadrature (the Gamma-value
    closed form as a cross-check of that quadrature only); the finite-L thresholds 3 g_L;
  * the return probabilities: closed walks of length 2n <= 24 counted by dynamic programming on a 25^3 torus (no wrap is possible),
    against the note's closed form C(2n,n) sum_a C(n,a)^2 C(2(n-a),n-a) and against (2 pi)^{-3} int phi^{2n} by grid quadrature (exact
    for trigonometric polynomials of degree below the grid size); the paired series (2 pi)^{-3} int (1 + phi) phi^{2m} = P_{2m} and the
    vanishing odd integrals; E = 6(1 - phi); hence G(0) = (1/6) sum P and 3G(0) = (1/2) sum P;
  * the certificate: S_1000 as one exact rational from my own sum (checked against the three-term recurrence
    n^2 a(n) = (10n^2 - 10n + 3) a(n-1) - 9(n-1)^2 a(n-2) at every n <= 1000), floor(10^6 S_1000), floor(10^6 S_250), the reduced
    denominator's digits, the majorants T_1^2 <= (36/11)^3/(108 N) and T_2 <= (225/14)(197/225)^(N+1) against the true T_1 and T_2
    (40 digits), e^{-2/15} <= 197/225, T_1 < 181/10^4, and the two rational comparisons;
  * the tail bound V2 against the exact P_2n for n = 1..1000, through the intermediate 2(2 pi)^{-3} int_Q e^{-2n g(k)} dk (erf form);
    1 - phi >= g on a 161^3 grid and the one-dimensional inequality 1 - cos u >= 11u^2/24 on [-1, 1]; the true tail
    sum_{n > 1000} P_2n (the recurrence in floating point to n = 10^6 plus c zeta(3/2, 10^6 + 1)) against T_1 + T_2, and
    (S_1000 + true tail)/2 against 3G(0);
  * the stated numbers: 3G(0) in (75/100, 76/100), the window width 76/100 - sqrt3/6 < 1/2, the band's factor seven, 3 sqrt3 pi/8.
HIT if a stated identity, bound or number fails.
"""
import math
import sys
import time
from fractions import Fraction

import mpmath as mp
import numpy as np


def torus_constant(L):
    e1 = 2 * (1 - np.cos(2 * np.pi * np.arange(L) / L))
    tot = 0.0
    for i in range(L):
        E = e1[i] + e1[:, None] + e1[None, :]
        if i == 0:
            E = E.copy()
            E[0, 0] = np.inf
        tot += np.sum(1.0 / E)
    return tot / L ** 3


def main():
    t0 = time.time()
    hits = []
    mp.mp.dps = 40
    # ---- G(0) by quadrature, and the Gamma-value closed form as a cross-check of the quadrature
    G_quad = mp.quad(lambda t: (mp.besseli(0, 2 * t) * mp.exp(-2 * t)) ** 3, [0, 1, 4, 16, 64, 256, 1024, mp.inf])
    W_gz = mp.sqrt(6) / (32 * mp.pi ** 3) * mp.gamma(mp.mpf(1) / 24) * mp.gamma(mp.mpf(5) / 24) * mp.gamma(mp.mpf(7) / 24) * mp.gamma(mp.mpf(11) / 24)
    G_gz = W_gz / 6  # the Gamma-value form is (2 pi)^-3 int dk/(1 - phi) = sum P = 6 G(0)
    assert abs(G_quad - G_gz) < mp.mpf(10) ** -12, (G_quad, G_gz)
    G0 = G_gz
    print(f"[G(0)] quadrature of (e^-2t I_0(2t))^3: {mp.nstr(G_quad, 20)}; Gamma-value form / 6: {mp.nstr(G_gz, 20)}; "
          f"3G(0) = {mp.nstr(3 * G0, 15)}; sum P = 6G(0) = {mp.nstr(6 * G0, 15)}")
    # ---- torus normalization
    Ls = [4, 6, 8, 16, 32, 64, 128, 256]
    g = {L: torus_constant(L) for L in Ls}
    R1 = {L: 2 * g[2 * L] - g[L] for L in (16, 32, 64, 128)}
    R2 = {L: (8 * R1[2 * L] - R1[L]) / 7 for L in (16, 32, 64)}
    G_torus = R2[64]
    print("[torus] N^-1 sum_{k != 0} 1/E(k): " + ", ".join(f"L={L}: {g[L]:.10f}" for L in Ls)
          + f"; Richardson (1/L then 1/L^3): {', '.join(f'{R2[L]:.12f}' for L in (16, 32, 64))}; G(0) = {mp.nstr(G0, 13)}; "
          f"|extrapolated - G(0)| = {abs(G_torus - float(G0)):.1e}; finite-L thresholds 3 g_L: "
          + ", ".join(f"L={L}: {3 * g[L]:.6f}" for L in (4, 8, 16, 64, 256)) + f"  ({time.time() - t0:.0f}s)")
    if abs(G_torus - float(G0)) > 1e-7 or not all(g[L] < g[2 * L] for L in (4, 8, 16, 32, 64, 128)):
        hits.append(f"torus constant does not tend to G(0): extrapolated {G_torus}, G(0) {G0}")
    # ---- walk counts by DP, closed form, Fourier normalization, paired series
    Nmax = 1000
    cb = [1] * (Nmax + 1)
    for k in range(1, Nmax + 1):
        cb[k] = cb[k - 1] * (2 * k) * (2 * k - 1) // (k * k)
    a = []
    for n in range(Nmax + 1):
        s, c = 0, 1
        for k in range(n + 1):
            s += c * c * cb[k]
            c = c * (n - k) // (k + 1)
        a.append(s)
    rec_ok = all(n * n * a[n] == (10 * n * n - 10 * n + 3) * a[n - 1] - 9 * (n - 1) ** 2 * a[n - 2] for n in range(2, Nmax + 1))
    Z3 = [cb[n] * a[n] for n in range(Nmax + 1)]
    cnt = np.zeros((25, 25, 25), dtype=np.int64)
    cnt[0, 0, 0] = 1
    dp = [1]
    for step in range(1, 25):
        cnt = sum(np.roll(cnt, s, axis=ax) for ax in range(3) for s in (1, -1))
        if step % 2 == 0:
            dp.append(int(cnt[0, 0, 0]))
    dp_ok = dp == Z3[:13]
    fourier_err, paired_err, odd_max = 0.0, 0.0, 0.0
    for n in range(0, 9):
        M = 2 * n + 3
        u = 2 * np.pi * np.arange(M) / M
        ph = (np.cos(u)[:, None, None] + np.cos(u)[None, :, None] + np.cos(u)[None, None, :]) / 3
        P = Z3[n] / 36 ** n
        fourier_err = max(fourier_err, abs(np.mean(ph ** (2 * n)) - P) / P)
        paired_err = max(paired_err, abs(np.mean((1 + ph) * ph ** (2 * n)) - P) / P)
        odd_max = max(odd_max, abs(np.mean(ph ** (2 * n + 1))))
    kk = np.random.default_rng(8156).uniform(-np.pi, np.pi, (1000, 3))
    six = np.max(np.abs(np.sum(2 * (1 - np.cos(kk)), axis=1) - 6 * (1 - np.mean(np.cos(kk), axis=1))))
    print(f"[walks] DP closed-walk counts for 2n <= 24: {dp[:5]}...{dp[-1]}; equal to the closed form: {dp_ok}; the three-term recurrence "
          f"holds at every n <= {Nmax}: {rec_ok}; grid quadrature (2 pi)^-3 int phi^2n vs P_2n (n <= 8): max relative error {fourier_err:.1e}; "
          f"paired series (1 + phi) phi^2m vs P_2m: {paired_err:.1e}; odd integrals max {odd_max:.1e}; |E - 6(1 - phi)| max {six:.1e}")
    if not (dp_ok and rec_ok) or max(fourier_err, paired_err) > 1e-12 or odd_max > 1e-14 or six > 1e-12:
        hits.append(f"walk normalization: dp {dp_ok}, recurrence {rec_ok}, fourier {fourier_err}, paired {paired_err}, odd {odd_max}")
    # ---- the certificate, exactly
    N = 1000
    num = sum(Z3[n] * 36 ** (N - n) for n in range(N + 1))
    S = Fraction(num, 36 ** N)
    fl6 = (10 ** 6 * S.numerator) // S.denominator
    S250 = Fraction(sum(Z3[n] * 36 ** (250 - n) for n in range(251)), 36 ** 250)
    fl250 = (10 ** 6 * S250.numerator) // S250.denominator
    den_digits = len(str(S.denominator))
    T1sq_maj = Fraction(36, 11) ** 3 / (108 * N)
    T2_maj = Fraction(225, 14) * Fraction(197, 225) ** (N + 1)
    X = Fraction(152, 100) - S - T2_maj
    cmp1, cmp2 = X > 0, X * X > T1sq_maj
    T1_true = (mp.mpf(36) / 11) ** 1.5 / (2 * mp.pi ** 1.5 * mp.sqrt(N))
    T2_true = 2 * mp.exp(-4 * mp.mpf(N + 1) / (3 * mp.pi ** 2)) / (1 - mp.exp(-4 / (3 * mp.pi ** 2)))
    maj1 = T1_true ** 2 <= mp.mpf(T1sq_maj.numerator) / T1sq_maj.denominator
    maj2 = T2_true <= mp.mpf(T2_maj.numerator) / T2_maj.denominator
    e215 = mp.exp(-mp.mpf(2) / 15) <= mp.mpf(197) / 225
    t1_181 = T1sq_maj < Fraction(181, 10 ** 4) ** 2
    fl12 = (10 ** 12 * T1sq_maj.numerator) // T1sq_maj.denominator
    lower = S > Fraction(150, 100)
    print(f"[certificate] floor(10^6 S_1000) = {fl6} (note 1501637), floor(10^6 S_250) = {fl250} (runner 1486921), reduced denominator "
          f"{den_digits} digits (note 1553); floor(10^12 (36/11)^3/(108N)) = {fl12} (runner 324567993); T_1 true {mp.nstr(T1_true, 8)} (majorant "
          f"{mp.nstr(mp.sqrt(mp.mpf(T1sq_maj.numerator) / T1sq_maj.denominator), 8)}, holds {maj1}; < 181/10^4: {t1_181}); T_2 true "
          f"{mp.nstr(T2_true, 5)} <= majorant {mp.nstr(mp.mpf(T2_maj.numerator) / T2_maj.denominator, 5)}: {maj2}; e^-2/15 <= 197/225: {e215}; "
          f"152/100 - S - T_2 = {float(X):.6f} > 0: {cmp1}; its square > T_1 majorant^2: {cmp2}; S_1000/2 > 75/100: {lower}  ({time.time() - t0:.0f}s)")
    if (fl6, fl250, den_digits, fl12) != (1501637, 1486921, 1553, 324567993) or not all((cmp1, cmp2, maj1, maj2, e215, t1_181, lower)):
        hits.append(f"certificate: floors {fl6}/{fl250}, digits {den_digits}, {fl12}, comparisons {cmp1}/{cmp2}, majorants {maj1}/{maj2}/{e215}/{t1_181}, lower {lower}")
    # ---- V2 against the exact P_2n, through the erf intermediate
    worst_ratio, worst_mid, n_worst, mid_above, mid_resolved = mp.mpf(0), mp.mpf(0), 0, 0, 0
    for n in range(1, N + 1):
        P = mp.mpf(Z3[n]) / mp.mpf(36) ** n
        aa = mp.mpf(11) * n / 36
        mid = 2 / (2 * mp.pi) ** 3 * ((mp.sqrt(mp.pi / aa) * mp.erf(mp.sqrt(aa))) ** 3 + ((2 * mp.pi) ** 3 - 8) * mp.exp(-4 * mp.mpf(n) / (3 * mp.pi ** 2)))
        bound = (mp.mpf(36) / 11) ** 1.5 / (4 * mp.pi ** 1.5 * mp.mpf(n) ** 1.5) + 2 * mp.exp(-4 * mp.mpf(n) / (3 * mp.pi ** 2))
        r = P / bound
        if r > worst_ratio:
            worst_ratio, n_worst = r, n
        worst_mid = max(worst_mid, P / mid)
        gap = (bound - mid) / bound  # analytically positive; below 40-digit resolution once erf(sqrt a) and e^{-4n/(3 pi^2)} are negligible
        if abs(gap) > mp.mpf(10) ** -35:
            mid_resolved += 1
            mid_above += gap < 0
    ratio1000 = (mp.mpf(36) / 11) ** 1.5 / (4 * mp.pi ** 1.5 * mp.mpf(N) ** 1.5) / (mp.mpf(Z3[N]) / mp.mpf(36) ** N)
    u = np.linspace(-1, 1, 2000001)
    u = u[u != 0]
    one_d = np.min((1 - np.cos(u)) / (11 * u * u / 24))
    grid = np.linspace(-np.pi, np.pi, 161)
    worst_g, worst_diff = np.inf, np.inf
    for k1 in grid:
        K2, K3 = np.meshgrid(grid, grid, indexing="ij")
        phi = (np.cos(k1) + np.cos(K2) + np.cos(K3)) / 3
        linf = np.maximum(abs(k1), np.maximum(np.abs(K2), np.abs(K3)))
        gk = np.where(linf <= 1, 11 / 72 * (k1 * k1 + K2 * K2 + K3 * K3), 2 / (3 * np.pi ** 2))
        diff = (1 - phi) - gk
        worst_diff = min(worst_diff, np.min(diff))
        nz = (k1 * k1 + K2 * K2 + K3 * K3) > 0
        worst_g = min(worst_g, np.min((1 - phi)[nz] / gk[nz]))
    print(f"[V2] P_2n / bound over n = 1..1000: max {mp.nstr(worst_ratio, 6)} (at n = {n_worst}); max P / (2(2 pi)^-3 int_Q e^(-2n g)) = "
          f"{mp.nstr(worst_mid, 6)}; intermediate <= bound resolved at {mid_resolved} of 1000 n (40 digits), violated at {mid_above}; bound's "
          f"first term / P at n = 1000: {mp.nstr(ratio1000, 5)}; min (1 - cos u)/(11u^2/24) on [-1,1] without 0 = {one_d:.6f} (1 - cos 1 = "
          f"{1 - math.cos(1):.6f} vs 11/24 = {11 / 24:.6f}); on the 161^3 grid min (1 - phi) - g = {worst_diff:.1e} (at k = 0), min (1 - phi)/g "
          f"over k != 0 = {worst_g:.6f}")
    if worst_ratio > 1 or worst_mid > 1 or mid_above or one_d < 1 or worst_g < 1 or worst_diff < -1e-15:
        hits.append(f"V2 fails: max P/bound {worst_ratio} at n {n_worst}, chain {worst_mid}/{mid_above}, 1D {one_d}, grid {worst_g}/{worst_diff}")
    # ---- the true tail
    Mbig = 10 ** 6
    q_prev2, q_prev1 = float(Fraction(a[N - 1], 9 ** (N - 1))), float(Fraction(a[N], 9 ** N))
    bnorm = float(Fraction(cb[N], 4 ** N))
    rel_check = abs(bnorm * q_prev1 - float(Fraction(Z3[N], 36 ** N))) / float(Fraction(Z3[N], 36 ** N))
    tail = 0.0
    for n in range(N + 1, Mbig + 1):
        q = ((10 * n * n - 10 * n + 3) * q_prev1 / 9 - (n - 1) ** 2 * q_prev2 / 9) / (n * n)
        bnorm *= (2 * n - 1) / (2 * n)
        tail += bnorm * q
        q_prev2, q_prev1 = q_prev1, q
    cconst = 2 * (mp.mpf(3) / (4 * mp.pi)) ** 1.5
    tail_true = tail + float(cconst * mp.zeta(1.5, Mbig + 1))
    three_g_from_sum = (float(S) + tail_true) / 2
    print(f"[tail] true sum_{{n > 1000}} P_2n = {tail_true:.8f} (recurrence in floating point to n = 10^6, start error {rel_check:.1e}, plus "
          f"c zeta(3/2, 10^6+1), c = 2(3/(4 pi))^3/2 = {mp.nstr(cconst, 8)}) vs T_1 + T_2 = {mp.nstr(T1_true + T2_true, 8)}; "
          f"(S_1000 + true tail)/2 = {three_g_from_sum:.10f} vs 3G(0) = {mp.nstr(3 * G0, 11)} (difference {abs(three_g_from_sum - float(3 * G0)):.1e})")
    if tail_true > float(T1_true + T2_true) or abs(three_g_from_sum - float(3 * G0)) > 1e-7:
        hits.append(f"tail or normalization: true tail {tail_true}, T1+T2 {T1_true + T2_true}, (S+tail)/2 {three_g_from_sum}, 3G(0) {3 * G0}")
    # ---- the stated numbers
    tg = 3 * G0
    in_band = mp.mpf(75) / 100 < tg < mp.mpf(76) / 100
    width = mp.mpf(76) / 100 - mp.sqrt(3) / 6
    crude = 3 * mp.sqrt(3) * mp.pi / 8
    factor = crude / (mp.sqrt(3) / 6)
    print(f"[numbers] 3G(0) = {mp.nstr(tg, 10)} in (75/100, 76/100): {in_band} (margins {mp.nstr(tg - mp.mpf(75) / 100, 4)} and "
          f"{mp.nstr(mp.mpf(76) / 100 - tg, 4)}); window width 76/100 - sqrt3/6 = {mp.nstr(width, 6)} < 1/2: {width < 0.5}; 3 sqrt3 pi/8 = "
          f"{mp.nstr(crude, 6)} < 21/10: {crude < 2.1}; the old band's factor (3 sqrt3 pi/8)/(sqrt3/6) = {mp.nstr(factor, 5)}; tail bound "
          f"T_1 + T_2 < 0.019: {T1_true + T2_true < 0.019}")
    if not (in_band and width < 0.5 and crude < 2.1 and 6.5 < factor < 7.5 and T1_true + T2_true < 0.019):
        hits.append(f"stated numbers: 3G(0) {tg}, width {width}, crude {crude}, factor {factor}")
    print(f"[time] {time.time() - t0:.0f}s")
    for h in hits:
        print("HIT: " + h)
    print(f"SUMMARY: attack pattern (f) NORMALIZATION - block 19's torus constant N^-1 sum 1/E(k) on L = 4..256 extrapolates to G(0) = "
          f"{mp.nstr(G0, 12)} (difference {abs(G_torus - float(G0)):.0e}); DP closed-walk counts to 2n = 24 equal the closed form; the grid "
          f"quadratures give P_2n and the paired series; E = 6(1 - phi); S_1000 recomputed exactly (floor 10^6 S = {fl6}, denominator {den_digits} "
          f"digits); both majorants hold at the true pi; both rational comparisons hold; V2 holds at every n <= 1000 (max P/bound "
          f"{mp.nstr(worst_ratio, 4)}); the true tail {tail_true:.6f} < T_1 + T_2 = {mp.nstr(T1_true + T2_true, 6)} and (S_1000 + tail)/2 "
          f"matches 3G(0) = {mp.nstr(tg, 8)} to {abs(three_g_from_sum - float(3 * G0)):.0e}; {len(hits)} failures; attack "
          f"{'FIRES' if hits else 'does not fire'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
