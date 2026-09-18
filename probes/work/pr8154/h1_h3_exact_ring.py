#!/usr/bin/env python3
"""J:falsifier:PR8154 - block 20 (PR #8154), a stated theorem's finite check: H1 (the zero-field lower bound, stated for every k != 0
in every dimension d <= 3) and H3's line bound, on the exactly solvable ring; with B1 and B3 (H2's counts) extended far beyond the note.

The ring Z/NZ (N = 2L, the note's line torus) with weight prod_x exp(beta s_x.s_{x+1}) and the uniform law on the sphere is solved by its
transfer operator: by the Funk-Hecke formula its eigenvalues on the degree-l spherical harmonics (multiplicity 2l + 1) are the modified
spherical Bessel functions lam_l = i_l(beta) (normalized surface measure), and the vector s couples degree l to l + 1 and l - 1 with total
squared matrix elements l + 1 and l (summed over the 2l + 1 states), so with rho_l = lam_(l+1)/lam_l and Z = sum_l (2l+1) lam_l^N:
    C(x) = <s_0 . s_x> = Z^{-1} sum_l (l+1) [lam_l^(N-x) lam_(l+1)^x + lam_(l+1)^(N-x) lam_l^x],
    u(k) = <|s^1(k)|^2> = (1/3) sum_x e^{ikx} C(x) = (3Z)^{-1} sum_l (l+1) lam_l^N (1 - rho_l^N)(1 - rho_l^2)/(1 - 2 rho_l cos k + rho_l^2),
and M_N^2 = N^{-2} <|sum_x s_x|^2> = 3 u(0)/N; all at 40 digits with degrees l <= 80.  The closed form (a geometric sum over x) is
cross-checked against the direct sum over x for L <= 30, and the chain's nearest-neighbour correlation against coth(beta) - 1/beta.
Checks (d = 1, E(k) = 2(1 - cos k), k = pi n/L, n in {-L+1, ..., L}):
  H1: u(k) >= (2M^2/3)^2 / [(beta E)^{1/2} + (beta E + 4M^2/(3N))^{1/2}]^2 >= (M^2/3)^2/(beta E + 4/(3N)) for every k != 0;
  H3 (line): M_N^4 <= 3(beta pi^2 + 2/3)/floor(sqrt L) <= (6 pi^2 beta + 4)/sqrt(L) for L >= 2; the sum rule sum_k u(k) = N/3.
at 7 couplings beta in [1/10, 30] and 14 sides L in [2, 5000] (the note executes the identities symbolically and the counts to L = 12/400).
  B1 extended: on {-L+1..L}^2 the sup-norm shells have 8j points (j < L) and 4L - 1 (j = L), |n|^2 <= 2j^2 on shell j, and
      sum_{n != 0} |n|^-2 >= 4 H_(L-1), for every L <= 400 (the sums in double precision; the margin is printed);
  B2 extended: H_(2^m) >= 1 + m/2 for m <= 60 (40-digit harmonic numbers);
  B3 extended: 4 floor(sqrt L)^2 >= L and the count of n in {-L+1..L} with 1 <= |n| <= floor(sqrt L) equals 2 floor(sqrt L), 2 <= L <= 10^6.
HIT if an inequality fails beyond 1e-25 (relative) or a count differs.  Deterministic.
"""
import math
import sys
import time

import mpmath as mp
import numpy as np

mp.mp.dps = 40
LMAX = 80
BETAS = (0.1, 0.5, 1, 2, 5, 10, 30)
SIDES = (2, 3, 4, 5, 8, 10, 30, 100, 300, 600, 1000, 2000, 3000, 5000)


def lams(beta):
    b = mp.mpf(beta)
    return [mp.sqrt(mp.pi / (2 * b)) * mp.besseli(l + mp.mpf(1) / 2, b) for l in range(LMAX + 2)]


def ring(lam, L):
    N = 2 * L
    Z = mp.fsum((2 * l + 1) * lam[l] ** N for l in range(LMAX + 1))
    terms = []
    for l in range(LMAX + 1):
        rho = lam[l + 1] / lam[l]
        terms.append(((l + 1) * lam[l] ** N * (1 - rho ** N) * (1 - rho ** 2) / (3 * Z), rho))

    def u(k):
        c = mp.cos(k)
        return mp.fsum(w / (1 - 2 * rho * c + rho ** 2) for w, rho in terms)

    return N, Z, u


def direct_C(lam, N, Z, x):
    return mp.fsum((l + 1) * (lam[l] ** (N - x) * lam[l + 1] ** x + lam[l + 1] ** (N - x) * lam[l] ** x) for l in range(LMAX + 1)) / Z


def main():
    t0 = time.time()
    hits = []
    tol = mp.mpf(10) ** -25
    worst1 = (mp.mpf(0), None)
    worst3 = (mp.mpf(0), None)
    worst_simpl = mp.mpf(0)
    sumrule = mp.mpf(0)
    crossdiff = mp.mpf(0)
    n_checks = 0
    n_rings = 0
    for beta in BETAS:
        lam = lams(beta)
        langevin = mp.coth(beta) - 1 / mp.mpf(beta)
        for L in SIDES:
            N, Z, u = ring(lam, L)
            n_rings += 1
            us = [(n, mp.pi * n / L, u(mp.pi * n / L)) for n in range(-L + 1, L + 1)]
            M2 = 3 * u(mp.mpf(0)) / N
            sr = abs(mp.fsum(v for _, _, v in us) - mp.mpf(N) / 3) / (mp.mpf(N) / 3)
            sumrule = max(sumrule, sr)
            if sr > tol:
                hits.append(f"sum rule at beta={beta}, L={L}: relative error {mp.nstr(sr, 5)}")
            if L <= 30:                                     # cross-check the closed form against the direct sum over x
                C = [direct_C(lam, N, Z, x) for x in range(N)]
                M2d = mp.fsum(C) / N
                crossdiff = max(crossdiff, abs(M2d - M2))
                for n, k, v in us[:: max(1, L // 5)]:
                    vd = mp.fsum(mp.cos(k * x) * C[x] for x in range(N)) / 3
                    crossdiff = max(crossdiff, abs(vd - v) / v)
            for n, k, v in us:
                if n == 0:
                    continue
                a = beta * 2 * (1 - mp.cos(k))
                b1 = (2 * M2 / 3) ** 2 / (mp.sqrt(a) + mp.sqrt(a + 4 * M2 / (3 * N))) ** 2
                b2 = (M2 / 3) ** 2 / (a + mp.mpf(4) / (3 * N))
                n_checks += 1
                r = b1 / v
                if r > worst1[0]:
                    worst1 = (r, (beta, L, n, v, b1))
                worst_simpl = max(worst_simpl, b2 / b1)
                if v < b1 * (1 - tol):
                    hits.append(f"H1 first inequality at beta={beta}, L={L}, n={n}: u = {mp.nstr(v, 12)} < {mp.nstr(b1, 12)}")
                if b1 < b2 * (1 - tol):
                    hits.append(f"H1 second inequality at beta={beta}, L={L}, n={n}: {mp.nstr(b1, 12)} < {mp.nstr(b2, 12)}")
            m = math.isqrt(L)
            mid = 3 * (beta * mp.pi ** 2 + mp.mpf(2) / 3) / m
            b3 = (6 * mp.pi ** 2 * beta + 4) / mp.sqrt(L)
            r3 = M2 ** 2 / b3
            if r3 > worst3[0]:
                worst3 = (r3, (beta, L, M2, M2 ** 2 / mid))
            if M2 ** 2 > mid * (1 + tol) or mid > b3 * (1 + tol):
                hits.append(f"H3 line at beta={beta}, L={L}: M^4 = {mp.nstr(M2 ** 2, 12)}, 3(beta pi^2+2/3)/m = {mp.nstr(mid, 12)}, "
                            f"(6 pi^2 beta+4)/sqrt L = {mp.nstr(b3, 12)}")
        # nearest-neighbour correlation of the long ring against the infinite chain's value coth(beta) - 1/beta
        N, Z, _ = ring(lam, SIDES[-1])
        c1 = direct_C(lam, N, Z, 1)
        print(f"[ring] beta = {beta}: {len(SIDES)} sides L = 2..{SIDES[-1]}; M_N^2 at L = {SIDES[-1]}: {mp.nstr(M2, 10)}; <s_0.s_1> = {mp.nstr(c1, 15)} "
              f"vs coth(beta) - 1/beta = {mp.nstr(langevin, 15)}  ({time.time() - t0:.0f}s)")
    print(f"[cross] closed form vs direct sum over x (L <= 30): largest relative difference {mp.nstr(crossdiff, 3)}; sum rule sum_k u(k) = N/3 to {mp.nstr(sumrule, 3)}")
    print(f"[H1] {n_checks} (beta, L, k != 0) cases on {n_rings} rings: largest ratio of H1's first bound to u(k) = {mp.nstr(worst1[0], 10)} at beta = "
          f"{worst1[1][0]}, L = {worst1[1][1]}, n = {worst1[1][2]} (u = {mp.nstr(worst1[1][3], 8)}); largest ratio second/first bound = {mp.nstr(worst_simpl, 10)}")
    print(f"[H3] line: largest ratio M_N^4 / ((6 pi^2 beta + 4)/sqrt L) = {mp.nstr(worst3[0], 8)} at beta = {worst3[1][0]}, L = {worst3[1][1]} "
          f"(M_N^2 = {mp.nstr(worst3[1][2], 8)}; ratio to the proof's 3(beta pi^2 + 2/3)/floor(sqrt L): {mp.nstr(worst3[1][3], 8)})")
    # B1 extended
    t1 = time.time()
    b1_bad = []
    b1_margin = math.inf
    for L in range(2, 401):
        r = np.arange(-L + 1, L + 1)
        X, Y = np.meshgrid(r, r, indexing="ij")
        J = np.maximum(np.abs(X), np.abs(Y))
        cnt = np.bincount(J.ravel(), minlength=L + 1)
        if any(cnt[j] != 8 * j for j in range(1, L)) or cnt[L] != 4 * L - 1:
            b1_bad.append(("count", L))
        R2 = X * X + Y * Y
        if np.any(R2 > 2 * J * J):
            b1_bad.append(("norm", L))
        mask = R2 > 0
        s = float(np.sum(1.0 / R2[mask]))
        HL = sum(1.0 / j for j in range(1, L))
        b1_margin = min(b1_margin, s / (4 * HL))
        if s < 4 * HL * (1 + 1e-12):
            b1_bad.append(("sum", L))
    print(f"[B1] L = 2..400: shells 8j / 4L-1, |n|^2 <= 2j^2 and sum |n|^-2 >= 4 H_(L-1): {len(b1_bad)} failures; smallest ratio "
          f"sum/(4 H_(L-1)) = {b1_margin:.6f}  ({time.time() - t1:.0f}s)")
    if b1_bad:
        hits.append(f"B1 fails: {b1_bad[:5]}")
    # B2 extended
    b2_bad = [mm for mm in range(0, 61) if mp.harmonic(2 ** mm) < 1 + mp.mpf(mm) / 2]
    print(f"[B2] H_(2^m) >= 1 + m/2 for m = 0..60: {len(b2_bad)} failures; H_(2^60) = {mp.nstr(mp.harmonic(2 ** 60), 12)} vs 31")
    if b2_bad:
        hits.append(f"B2 fails at m = {b2_bad[:5]}")
    # B3 extended
    t1 = time.time()
    b3_bad = []
    for L in range(2, 10 ** 6 + 1):
        m = math.isqrt(L)
        if 4 * m * m < L:
            b3_bad.append(("4m^2", L))
        # n in {-L+1..L} with 1 <= |n| <= m: n = 1..min(m, L) and n = -1..-min(m, L-1)
        cnt = min(m, L) + min(m, L - 1)
        if cnt != 2 * m:
            b3_bad.append(("count", L))
    print(f"[B3] L = 2..10^6: 4 floor(sqrt L)^2 >= L and the block count 2 floor(sqrt L): {len(b3_bad)} failures  ({time.time() - t1:.0f}s)")
    if b3_bad:
        hits.append(f"B3 fails: {b3_bad[:5]}")
    print(f"[time] {time.time() - t0:.0f}s")
    for h in hits[:10]:
        print("HIT: " + h)
    print(f"SUMMARY: exact ring (transfer operator, 40 digits, {n_rings} rings, L up to {SIDES[-1]}, beta 0.1..30): H1's two inequalities at "
          f"{n_checks} (beta, L, k) cases, largest ratio bound/u = {mp.nstr(worst1[0], 6)}; H3's line bound largest ratio {mp.nstr(worst3[0], 6)}; "
          f"sum rule to {mp.nstr(sumrule, 2)}; B1 to L = 400, B2 to m = 60, B3 to L = 10^6: {len(b1_bad) + len(b2_bad) + len(b3_bad)} failures; "
          f"falsifier {'FIRES' if hits else 'does not fire'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
