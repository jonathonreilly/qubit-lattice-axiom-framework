#!/usr/bin/env python3
"""Excess kurtosis of a truncated plaquette holonomy: psi = u + xi x xi', with (u, xi, xi') colour vectors, jointly Gaussian, colour isotropic, any correlation among the three.

Hand derivation (Text 3.13, closing notes): E|psi|^4 - (5/3) (E|psi|^2)^2 = (5/3) delta^4, delta^2 := E|xi x xi'|^2 = 6 (v v' - c^2), for any correlation of u with xi, xi'.

PRE-REGISTERED CRITERION. K1: on ten random covariances, |measured excess - (5/3) delta^4| below 5 standard errors of the Monte Carlo, or below 1 percent of (5/3) delta^4. FAIL means the identity is wrong.
"""
from __future__ import annotations

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("VECLIB_MAXIMUM_THREADS", "1")

import numpy as np


def main():
    rng = np.random.default_rng(2)
    n = 4_000_000
    ok = True
    for trial in range(10):
        R = rng.normal(size=(3, 3))
        C = R @ R.T
        L = np.linalg.cholesky(C)
        z = rng.normal(size=(n, 3, 3))  # sample, field, colour
        f = np.einsum("ij,njc->nic", L, z)
        u, xi, xp = f[:, 0], f[:, 1], f[:, 2]
        q = np.cross(xi, xp)
        psi = u + q
        s2 = np.sum(psi * psi, axis=1)
        m2 = s2.mean()
        m4 = (s2 * s2).mean()
        d2 = 6 * (C[1, 1] * C[2, 2] - C[1, 2] ** 2)
        pred = (5.0 / 3.0) * d2 * d2
        # jackknife-free error: split in 20 batches
        ex = []
        for b in np.array_split(s2, 20):
            ex.append((b * b).mean() - (5.0 / 3.0) * b.mean() ** 2)
        ex = np.array(ex)
        err = ex.std(ddof=1) / np.sqrt(20)
        val = m4 - (5.0 / 3.0) * m2 * m2
        passed = abs(val - pred) < max(5 * err, 0.01 * pred)
        ok &= bool(passed)
        print(f"trial {trial}: excess {val:.4f} +- {err:.4f}, (5/3) delta^4 = {pred:.4f}, E|u|^2 = {3*C[0,0]:.3f}, corr(u, xi) = {C[0,1]/np.sqrt(C[0,0]*C[1,1]):.2f}, corr(u, xi') = {C[0,2]/np.sqrt(C[0,0]*C[2,2]):.2f}, {'pass' if passed else 'FAIL'}", flush=True)
    print("K1", "PASS" if ok else "FAIL")


if __name__ == "__main__":
    main()
