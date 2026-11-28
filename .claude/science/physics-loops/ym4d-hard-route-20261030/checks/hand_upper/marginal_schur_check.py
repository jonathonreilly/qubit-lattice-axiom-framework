#!/usr/bin/env python3
"""Kill test of Lemma M, library/upper-chain-by-hand.md, section 2. Nothing rests on this run.

S(x, y) on a box (-1, 1) x (-1, 1), with a Schur complement that really moves with the point. V(y) := -log integral exp(-S(x, y)) dx by Gauss-Legendre.
Criteria, written before the run. For each test potential and random y, eta with y +- eta in the box:
M1. V(y + eta) + V(y - eta) - 2 V(y) >= eta^2 sigma, sigma := the minimum of S_yy - S_xy^2 / S_xx over a fine grid of the box, up to 1e-9 slack.
M2. Control: the same with sigma + 0.5 fails somewhere for at least one potential, so the test can fail.
"""
import numpy as np

nodes, wts = np.polynomial.legendre.leggauss(200)


def run(name, S, Sxx, Sxy, Syy):
    def V(y):
        return -np.log(np.sum(wts * np.exp(-S(nodes, y))))

    gx, gy = np.meshgrid(np.linspace(-1, 1, 401), np.linspace(-1, 1, 401), indexing="ij")
    sigma = float(np.min(Syy(gx, gy) - Sxy(gx, gy) ** 2 / Sxx(gx, gy)))
    rng = np.random.default_rng(1)
    margin, margin_ctl = np.inf, np.inf
    for _ in range(4000):
        y = rng.uniform(-1, 1)
        eta = rng.uniform(0, 1 - abs(y))
        if eta < 1e-3:
            continue
        d2 = V(y + eta) + V(y - eta) - 2 * V(y)
        margin = min(margin, (d2 - eta**2 * sigma) / eta**2)
        margin_ctl = min(margin_ctl, (d2 - eta**2 * (sigma + 0.5)) / eta**2)
    print(f"{name}: sigma = {sigma:.5f}, min (second difference / eta^2 - sigma) = {margin:.5f}, control margin = {margin_ctl:.5f}")
    return margin, margin_ctl


pots = [
    ("sin coupling", lambda x, y: (x**2 + y**2) / 2 + 0.6 * np.sin(x) * np.sin(y), lambda x, y: 1 - 0.6 * np.sin(x) * np.sin(y), lambda x, y: 0.6 * np.cos(x) * np.cos(y), lambda x, y: 1 - 0.6 * np.sin(x) * np.sin(y)),
    ("quartic", lambda x, y: x**2 + y**2 + 0.5 * x**2 * y**2 + 0.5 * x * y, lambda x, y: 2 + y**2, lambda x, y: 2 * x * y + 0.5, lambda x, y: 2 + x**2),
    ("exp tilt", lambda x, y: np.exp(x + y) + (x**2 + y**2) / 2, lambda x, y: 1 + np.exp(x + y), lambda x, y: np.exp(x + y), lambda x, y: 1 + np.exp(x + y)),
]
res = [run(*p) for p in pots]
print("M1", "PASS" if all(m >= -1e-9 for m, _ in res) else "FAIL")
print("M2", "PASS" if any(c < 0 for _, c in res) else "FAIL")
