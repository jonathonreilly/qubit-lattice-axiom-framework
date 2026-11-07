#!/usr/bin/env python3
"""Monte Carlo check of the rectangle sum at the smallest size: Wilson against Gaussian potential.

Geometry of parts/witness.md, Text 3, at D = 1 and small R, averaged over translations and the 24
axis permutations, all of which are symmetries of the law. Stk = sum_k <T^(k)> / P_k with P_k the
lattice values on this torus; beta^2 Stk -> Stk_total on the Wilson weight, and -> Stk_comp on the
Gaussian potential in Feynman gauge.

PRE-REGISTERED CRITERIA (written before the first run).
 R1 FORMULA: |beta^2 Stk - Stk_total(T)| < max(3 sigma, 0.3 |Stk_total(T)|) at the largest beta run,
    where the corrections of order 1 / beta are allowed by the second term.
 R2 VERTEX: beta^2 Stk differs from Stk_comp(T) by more than 3 sigma at the largest beta, when
    the formula predicts them to differ by more than 6 sigma of the run. If the run cannot resolve
    this, the result is reported as UNRESOLVED and nothing is concluded.
 R3 GAUSS: the Gaussian potential sampled at the same beta gives beta^2 Stk within
    max(3 sigma, 0.3 |Stk_comp(T)|) of Stk_comp(T).
"""
from __future__ import annotations

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("VECLIB_MAXIMUM_THREADS", "1")

import itertools
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from witness_gauss_sample import expq  # noqa: E402
from witness_mc_corner import Field, binned_err, check_rss, qconj, qmul  # noqa: E402
from witness_stokes import lasso_steps, run as formula_run, steps_between  # noqa: E402
from witness_tree_coeff import Lat, plaq  # noqa: E402


def path_product(U, steps):
    """Ordered product along signed steps, base at every site. U[mu][x..., 4]."""
    T = U.shape[1]
    W = None
    pos = np.zeros(4, dtype=int)
    for s in steps:
        mu = abs(s) - 1
        if s > 0:
            link = np.roll(U[mu], tuple(-pos), axis=(0, 1, 2, 3))
            pos[mu] += 1
        else:
            pos[mu] -= 1
            link = qconj(np.roll(U[mu], tuple(-pos), axis=(0, 1, 2, 3)))
        W = link if W is None else qmul(W, link)
    return W


def edge_paths(D, R):
    c = (D - 1) // 2
    far = (R, 0, c, c)
    corners = [(0, 0, 0, 0), (0, 0, D, 0), (0, 0, D, D), (0, 0, 0, D)]
    out = []
    for k, y in enumerate(corners):
        z = corners[(k + 1) % 4]
        s1 = plaq(1, 2)
        s2 = lasso_steps(steps_between(y, z), plaq(1, 2))
        s3 = lasso_steps(steps_between(y, far), plaq(3, 4))
        out.append((y, s1, s2, s3))
    return out


def permute(steps, perm):
    return [(1 if s > 0 else -1) * (perm[abs(s) - 1] + 1) for s in steps]


def measure_T(U, paths, perms):
    vals = np.zeros(4)
    for perm in perms:
        for k, (y, s1, s2, s3) in enumerate(paths):
            w1 = path_product(U, permute(s1, perm))[..., 1:]
            w2 = path_product(U, permute(s2, perm))[..., 1:]
            w3 = path_product(U, permute(s3, perm))[..., 1:]
            vals[k] += 2 * np.mean(np.sum(w1 * np.cross(w2, w3), axis=-1))
    return vals / len(perms)


def gauss_field(lat, beta, rng):
    T = lat.T
    sq = np.sqrt(lat.inv * 4.0 / beta)
    noise = rng.normal(size=(4, 3, T, T, T, T))
    A = np.fft.ifftn(np.fft.fftn(noise, axes=(2, 3, 4, 5)) * sq, axes=(2, 3, 4, 5)).real
    return expq(np.moveaxis(A, 1, -1))


def main():
    T = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    D = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    R = int(sys.argv[3]) if len(sys.argv) > 3 else 2
    beta = float(sys.argv[4]) if len(sys.argv) > 4 else 16.0
    nmeas = int(sys.argv[5]) if len(sys.argv) > 5 else 200
    nperm = int(sys.argv[6]) if len(sys.argv) > 6 else 24
    lat = Lat(4, T)
    rows, sc, st, salt, flux = formula_run(T, D, R)
    Pk = np.array([r[4] for r in rows])
    print(f"T={T} D={D} R={R}: formula Stk_comp={sc:.5e} Stk_total={st:.5e} -24Flux={-24*flux:.5e} P_k={Pk[0]:.5e}", flush=True)
    paths = edge_paths(D, R)
    perms = list(itertools.permutations(range(4)))[:nperm]
    rng = np.random.default_rng(int(beta) + 100 * R + 7)
    f = Field(T, rng)
    t0 = time.time()
    for _ in range(200):
        f.sweep(beta)
    ws, gs = [], []
    for i in range(nmeas):
        f.sweep(beta)
        ws.append(np.sum(measure_T(f.U, paths, perms) / Pk))
        gs.append(np.sum(measure_T(gauss_field(lat, beta, rng), paths, perms) / Pk))
    w, we = binned_err(np.array(ws))
    g, ge = binned_err(np.array(gs))
    print(f"beta={beta:g} nmeas={nmeas} time={time.time()-t0:.0f}s rss={check_rss():.2f}GB")
    print(f"Wilson beta^2 Stk = {beta**2*w:.4e} +- {beta**2*we:.4e}   Gaussian beta^2 Stk = {beta**2*g:.4e} +- {beta**2*ge:.4e}")
    print(f"formula difference in units of the Wilson sigma: {abs(st-sc)/(beta**2*we):.1f}")


if __name__ == "__main__":
    main()
