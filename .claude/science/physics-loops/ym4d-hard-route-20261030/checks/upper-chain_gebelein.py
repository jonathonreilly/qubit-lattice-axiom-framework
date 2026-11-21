#!/usr/bin/env python3
"""Maximal correlation of a uniformly log-concave law, Lemma 21.5 of parts/upper-chain.md.

Claim. For a density exp(-S(x, y)) on a product of intervals, with S_xx >= k_x, S_yy >= k_y, |S_xy| <= b and
b^2 < k_x k_y, the maximal correlation satisfies rho <= r := b / (k_x k_y)^(1/2).

Criteria, written before the run.
G1: on 300 random convex S with quartic and mixed terms, on a grid of 161 x 161 points, rho <= r (1 + 1e-3), the
    margin being for the grid. rho is the second singular value of p_ij / (p_i p_j)^(1/2).
G2: for Gaussian S with no cut, where the claim is an equality, rho / r lies in [0.98, 1.02] on 20 random cases,
    on a domain of 8 standard deviations.
G3: the bound does not depend on an overall scale: rho / r is unchanged within 2 percent when S is multiplied
    by 100, on 20 Gaussian cases, as the x-free form claims.

First run: G1 FAILED as registered, on its floor of 100 admissible cases: only 56 of 300 draws were convex on the box,
with max rho/r = 0.54, so the bound was not violated. G2, G3 passed.
G1', registered after that run: 2000 draws, the same claim rho <= r (1 + 1e-3), at least 300 admissible cases.
"""
import resource

import numpy as np

RSS_LIMIT_GB = 2.0


def rss_guard():
    if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e9 > RSS_LIMIT_GB:
        raise SystemExit("RSS above limit")


def rho_of(S, xs, ys):
    P = np.exp(-(S - S.min()))
    P /= P.sum()
    px, py = P.sum(axis=1), P.sum(axis=0)
    K = P / np.sqrt(np.outer(px, py))
    sv = np.linalg.svd(K, compute_uv=False)
    return float(sv[1])


def main():
    rng = np.random.default_rng(20261031)
    worst = 0.0
    n_done = 0
    for _ in range(2000):
        a, c = rng.uniform(0.5, 3, size=2)
        q1, q2, q3 = rng.uniform(0, 0.5, size=3)
        b0 = rng.uniform(-0.6, 0.6) * (a * c) ** 0.5
        R = rng.uniform(1, 3)
        xs = np.linspace(-R, R, 161)
        ys = np.linspace(-R, R, 161)
        X, Y = np.meshgrid(xs, ys, indexing="ij")
        S = a * X**2 / 2 + c * Y**2 / 2 + b0 * X * Y + q1 * X**4 + q2 * Y**4 + q3 * X**2 * Y**2
        Sxx = a + 12 * q1 * X**2 + 2 * q3 * Y**2
        Syy = c + 12 * q2 * Y**2 + 2 * q3 * X**2
        Sxy = b0 + 4 * q3 * X * Y
        # convexity on the box, in the blocks
        kx, ky, b = Sxx.min(), Syy.min(), np.abs(Sxy).max()
        if b**2 >= kx * ky or np.any(Sxx * Syy - Sxy**2 <= 0):
            continue
        r = b / (kx * ky) ** 0.5
        worst = max(worst, rho_of(S, xs, ys) / r)
        n_done += 1
    print(f"G1': {n_done} convex cases, max rho/r = {worst:.4f} (claim <= 1)")
    ok1 = worst <= 1 + 1e-3 and n_done >= 300

    lo, hi = 9.0, 0.0
    drift = 0.0
    for _ in range(20):
        a, c = rng.uniform(0.5, 3, size=2)
        b0 = rng.uniform(-0.8, 0.8) * (a * c) ** 0.5
        r = abs(b0) / (a * c) ** 0.5
        if r < 0.1:
            continue
        cov = np.linalg.inv(np.array([[a, b0], [b0, c]]))
        vals = []
        for scale in (1.0, 100.0):
            sx, sy = (cov[0, 0] / scale) ** 0.5, (cov[1, 1] / scale) ** 0.5
            xs = np.linspace(-8 * sx, 8 * sx, 321)
            ys = np.linspace(-8 * sy, 8 * sy, 321)
            X, Y = np.meshgrid(xs, ys, indexing="ij")
            S = scale * (a * X**2 / 2 + c * Y**2 / 2 + b0 * X * Y)
            vals.append(rho_of(S, xs, ys) / r)
        lo, hi = min(lo, vals[0]), max(hi, vals[0])
        drift = max(drift, abs(vals[1] / vals[0] - 1))
    print(f"G2: Gaussian rho/r in [{lo:.4f}, {hi:.4f}] (claim [0.98, 1.02])")
    print(f"G3: largest change of rho/r under scale 100 = {drift:.2e} (claim <= 0.02)")
    rss_guard()
    print("G1'", "PASS" if ok1 else "FAIL")
    print("G2", "PASS" if 0.98 <= lo and hi <= 1.02 else "FAIL")
    print("G3", "PASS" if drift <= 0.02 else "FAIL")


if __name__ == "__main__":
    main()
