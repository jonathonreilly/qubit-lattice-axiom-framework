#!/usr/bin/env python3
"""A Gaussian potential does not have <T> = 0 when holonomies are path ordered.

Samples A_b^a independent in colour and direction with covariance (4/beta) G, G = (-Delta)^{-1}
without zero mode (Feynman gauge, T^4), U_b = exp(i A_b . sigma / 2), and measures the corner
cluster T as in checks/witness_mc_corner.py. Also measures the flux class value, where W_i is
replaced by exp(i Phi_i . sigma / 2), Phi_i the linear flux.

PRE-REGISTERED CRITERIA (written before the first run).
 G1 NONZERO: a fit beta^2 <T> = K + K2 / beta has |K| > 10 sigma.
 G2 VALUE: |K - K_comp(T)| < max(3 sigma, 0.01), with K_comp(T) from witness_tree_coeff at this T.
 G3 FLUX: the flux class value is within 3 sigma of 0 at each beta (exact zero by oddness).
 G4 FINITE-T for the Wilson run: prints K_total(T = 8) to compare with the Monte Carlo fit.
"""
from __future__ import annotations

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("VECLIB_MAXIMUM_THREADS", "1")

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from witness_mc_corner import binned_err, check_rss, qconj, qmul  # noqa: E402
from witness_tree_coeff import Lat, evaluate, plaq  # noqa: E402


def expq(A):
    """A[..., 3] -> quaternion exp(i A . sigma / 2) = (cos, sin * n)."""
    n = np.sqrt(np.sum(A * A, axis=-1, keepdims=True))
    s = np.sinc(n / (2 * np.pi)) / 2  # sin(n/2)/n
    return np.concatenate([np.cos(n / 2), s * A], axis=-1)


def sample(T, beta, nsamples, seed):
    rng = np.random.default_rng(seed)
    lat = Lat(4, T)
    sq = np.sqrt(lat.inv * 4.0 / beta)
    res, resf = [], []
    triples = ((0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3))
    for _ in range(nsamples):
        noise = rng.normal(size=(4, 3, T, T, T, T))
        A = np.fft.ifftn(np.fft.fftn(noise, axes=(2, 3, 4, 5)) * sq, axes=(2, 3, 4, 5)).real
        A = np.moveaxis(A, 1, -1)  # (mu, x, colour)
        U = expq(A)

        def pl(m, n):
            return qmul(qmul(qmul(U[m], np.roll(U[n], -1, axis=m)), qconj(np.roll(U[m], -1, axis=n))), qconj(U[n]))

        def fl(m, n):
            return A[m] + np.roll(A[n], -1, axis=m) - np.roll(A[m], -1, axis=n) - A[n]

        vals, valsf = [], []
        for (m, n, r) in triples:
            sgn = {(m, n): 1, (n, r): 1, (m, r): -1}
            p1, p2, p3 = pl(m, n)[..., 1:], pl(n, r)[..., 1:], -pl(m, r)[..., 1:]
            vals.append(2 * np.mean(np.sum(p1 * np.cross(p2, p3), axis=-1)))
            f1, f2, f3 = fl(m, n), fl(n, r), -fl(m, r)
            q1, q2, q3 = expq(f1)[..., 1:], expq(f2)[..., 1:], expq(f3)[..., 1:]
            valsf.append(2 * np.mean(np.sum(q1 * np.cross(q2, q3), axis=-1)))
        res.append(np.mean(vals))
        resf.append(np.mean(valsf))
    check_rss()
    return np.array(res), np.array(resf)


def main():
    T = 8
    lat = Lat(4, T)
    r = evaluate(lat, (0, 0, 0, 0), plaq(1, 2), plaq(2, 3), plaq(3, 1))
    print(f"T={T} formula: K_comp={r['K_comp']:.5f} K_vert={r['K_vert']:.5f} K_total={r['K_total']:.5f}")
    rows = []
    for beta, n in ((16.0, 1500), (32.0, 1500), (64.0, 3000), (128.0, 6000)):
        t, tf = sample(T, beta, n, seed=int(beta) + 11)
        tm, te = binned_err(t)
        fm, fe = binned_err(tf)
        rows.append((beta, beta**2 * tm, beta**2 * te))
        print(f"beta={beta:g} n={n}: beta^2<T>_G={beta**2*tm:.4f}+-{beta**2*te:.4f} beta^2<T>_flux={beta**2*fm:.4f}+-{beta**2*fe:.4f} G3 {'PASS' if abs(fm) < 3*fe else 'CHECK'} rss={check_rss():.2f}GB", flush=True)
    b = np.array(rows)
    A = np.stack([np.ones(len(b)), 1.0 / b[:, 0]], axis=1)
    w = 1.0 / b[:, 2]
    cov = np.linalg.inv((A * w[:, None]).T @ (A * w[:, None]))
    par = cov @ ((A * w[:, None]).T @ (b[:, 1] * w))
    K, dK = par[0], np.sqrt(cov[0, 0])
    print(f"fit K={K:.4f}+-{dK:.4f} K2={par[1]:.3f}")
    print(f"G1 {'PASS' if abs(K) > 10*dK else 'FAIL'} G2 {'PASS' if abs(K-r['K_comp']) < max(3*dK, 0.01) else 'FAIL'}")


if __name__ == "__main__":
    main()
