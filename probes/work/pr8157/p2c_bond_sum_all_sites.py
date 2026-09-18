#!/usr/bin/env python3
"""J:falsifier:PR8157 - block 23 (PR #8157), a stated theorem's finite check: P2(c),
    sum_b (cosh(a_y - a_z) - 1) <= 2 gamma^2 cosh(gamma) (1 + 8 H_R),   a_y = gamma max(0, log((1+R)/(1+d(y)))),  R = d(x),
with H_R = sum_{j<=R} 1/j, on every window of Z^2 containing {d < R} and on the torus.  The runner checks the ingredients (shell counts,
sum_{j<=R} 8j/(1+j)^2 <= 8 H_R for integer R <= 60); the proof's shell step ("only shells with j < R + 1, i.e. j <= R") is exact for
integer R, while R = d(x) is a Euclidean distance.  Here the inequality itself is evaluated directly, bond by bond, for every lattice
site x with 1 <= d(x) <= R_MAX on Z^2 (non-integer R included) and for every site of the tori (Z/2LZ)^2 with L in L_TORI, at the
couplings' shift heights gamma in GAMMAS (P3 uses gamma = min(1, 5/(256 beta))), in double precision (the bond sum only has bonds with
min(d(y), d(z)) < R).  HIT if the left side exceeds the right side at some (x, gamma) by more than a relative 1e-12.  INFO: the minimal
distance d* at which P3's final bound (3/2) e^{9/16} (1 + d)^{-kappa(beta)} drops below 1, for several beta.
"""
import math
import sys
import time

import numpy as np

R_MAX = 150
L_TORI = (8, 16, 32, 64)
GAMMAS = (0.01, 0.1, 0.5, 1.0, 2.0)


def H(R):
    n = int(math.floor(R + 1e-12))
    return sum(1.0 / j for j in range(1, n + 1))


def bond_sum_plane(x, gamma):
    R = math.hypot(*x)
    m = int(math.ceil(R)) + 2
    ys = np.arange(-m, m + 1)
    Y1, Y2 = np.meshgrid(ys, ys, indexing="ij")
    d = np.hypot(Y1, Y2)
    a = gamma * np.maximum(0.0, np.log((1 + R) / (1 + d)))
    s = 0.0
    for axis in (0, 1):
        da = np.diff(a, axis=axis)
        s += float(np.sum(np.cosh(da) - 1.0))
    return s, R


def bond_sum_torus(L, x, gamma):
    n = 2 * L
    ys = np.arange(n)
    dd = np.minimum(ys, n - ys)
    D1, D2 = np.meshgrid(dd, dd, indexing="ij")
    d = np.hypot(D1, D2)
    R = math.hypot(min(x[0], n - x[0]), min(x[1], n - x[1]))
    a = gamma * np.maximum(0.0, np.log((1 + R) / (1 + d)))
    s = 0.0
    for axis in (0, 1):
        s += float(np.sum(np.cosh(a - np.roll(a, 1, axis=axis)) - 1.0))
    return s, R


def main():
    t0 = time.time()
    worst = (0.0, None)
    n_checked = 0
    noninteger = 0
    viol = []
    for g in GAMMAS:
        bound_g = 2 * g * g * math.cosh(g)
        for x1 in range(0, R_MAX + 1):
            for x2 in range(0, x1 + 1):               # one octant suffices by the symmetry of d
                R = math.hypot(x1, x2)
                if R < 1 or R > R_MAX:
                    continue
                s, R = bond_sum_plane((x1, x2), g)
                b = bound_g * (1 + 8 * H(R))
                ratio = s / b
                n_checked += 1
                noninteger += abs(R - round(R)) > 1e-9
                if ratio > worst[0]:
                    worst = (ratio, ((x1, x2), g, R, s, b))
                if s > b * (1 + 1e-12):
                    viol.append(((x1, x2), g, R, s, b))
    print(f"[plane] {n_checked} (site, gamma) pairs with 1 <= d(x) <= {R_MAX} ({noninteger} with non-integer R), gamma in {GAMMAS}: "
          f"violations {len(viol)}; largest ratio left/right = {worst[0]:.6f} at x = {worst[1][0]}, gamma = {worst[1][1]}, R = {worst[1][2]:.4f} "
          f"(left {worst[1][3]:.6e}, right {worst[1][4]:.6e})")
    tworst = (0.0, None)
    tv = []
    tn = 0
    for L in L_TORI:
        for g in GAMMAS:
            bound_g = 2 * g * g * math.cosh(g)
            for x1 in range(0, L + 1):
                for x2 in range(0, x1 + 1):
                    if (x1, x2) == (0, 0):
                        continue
                    s, R = bond_sum_torus(L, (x1, x2), g)
                    if R < 1:
                        continue
                    b = bound_g * (1 + 8 * H(R))
                    tn += 1
                    if s / b > tworst[0]:
                        tworst = (s / b, (L, (x1, x2), g, R))
                    if s > b * (1 + 1e-12):
                        tv.append((L, (x1, x2), g, R, s, b))
    print(f"[torus] {tn} (L, site, gamma) triples on (Z/2LZ)^2, L in {L_TORI}: violations {len(tv)}; largest ratio {tworst[0]:.6f} at "
          f"L = {tworst[1][0]}, x = {tworst[1][1]}, gamma = {tworst[1][2]}, R = {tworst[1][3]:.4f}")
    # INFO: where P3's final bound becomes informative (below 1)
    rows = []
    for beta in (0.005, 5 / 256, 0.05, 0.1, 0.5, 1.0, 5.0):
        kappa = 5 / (512 * beta) if beta >= 5 / 256 else 1 - 128 * beta / 5
        c1 = 1.5 * math.exp(9 / 16)
        dstar_log10 = math.log10(c1) / kappa                      # (1 + d)^kappa > c1  <=>  log10(1 + d) > log10(c1)/kappa
        rows.append(f"beta={beta:g}: kappa={kappa:.5f}, bound < 1 from 1 + d > 10^{dstar_log10:.2f}")
    print("[INFO] P3's bound (3/2) e^(9/16) (1 + d)^(-kappa(beta)) is below 1 only from a distance: " + "; ".join(rows))
    print(f"[time] {time.time() - t0:.0f}s")
    if viol:
        print(f"HIT: P2(c) violated on Z^2 at {len(viol)} (site, gamma) pairs, e.g. {viol[0]}")
    if tv:
        print(f"HIT: P2(c) violated on the torus at {len(tv)} triples, e.g. {tv[0]}")
    print(f"SUMMARY: P2(c) evaluated bond by bond at {n_checked} plane pairs ({noninteger} non-integer R) and {tn} torus triples: "
          f"{len(viol) + len(tv)} violations; largest ratio of the bond sum to 2 gamma^2 cosh(gamma)(1 + 8 H_R) = {max(worst[0], tworst[0]):.4f}; "
          f"falsifier {'FIRES' if (viol or tv) else 'does not fire'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
