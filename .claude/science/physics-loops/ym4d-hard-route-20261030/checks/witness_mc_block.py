#!/usr/bin/env python3
"""Monte Carlo of the rectangle sum on blocked links: the actual Wilson law at level 1, against a Gaussian potential at level 1.

Blocking: L = 3, V(x, mu) = normalise( w_0 U_straight + w_1 sum of the 6 staples of height 1 ), as in checks/witness_block_tree.py.
Wilson: heat bath on T_f^4, block, measure the rectangle functions T^(k) on the coarse links, averaged over all fine translations of the coarse grid and
over axis permutations. Gaussian potential at level 1: fine Feynman Gaussian A with covariance (4 / beta) G, coarse link variable exp(i A_coarse) with A_coarse the
LINEAR block sum_pi w_pi Phi_pi. That is a Gaussian potential on the level-1 lattice, whose flux covariance is the blocked one, invariant under the lattice symmetries.

Predictions, in the same torus: Wilson, beta^2 Stk -> Stk_total^(1) of witness_block_tree. Gaussian, beta^2 Stk -> Stk_G1, which is -24 Flux^(1) plus the far Levy term of (3.1):
the blocked covariance is not diagonal in direction on coarse links, because of the staples, so that term is not exactly zero at small R. It is computed exactly and printed.

PRE-REGISTERED CRITERIA (written before the first run).
 L1 FORMULA: |beta^2 Stk_W - Stk_total^(1)| < max(3 sigma, 0.3 |Stk_total^(1)|) at the largest beta run. FAIL means Lemma 5.2 or the form A~ fails in the actual law.
 L2 SEPARATION: Wilson and Gaussian values differ by more than 3 sigma at the largest beta, when the predictions differ by more than 6 sigma of the run. Otherwise UNRESOLVED,
    and nothing is concluded.
 L3 GAUSS: |beta^2 Stk_G - Stk_G1| < max(3 sigma, 0.3 |Stk_G1|).
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
from witness_block_tree import Block, CoarsePath, coarse_steps_between, lasso, run_rect  # noqa: E402
from witness_gauss_sample import expq  # noqa: E402
from witness_mc_corner import Field, binned_err, check_rss, qconj, qmul  # noqa: E402
from witness_tree_coeff import Lat, field_E, plaq  # noqa: E402


def fine_path_product(U, steps):
    pos = np.zeros(4, dtype=int)
    W = None
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


def block_links(U, L, w0, w1):
    V = np.zeros_like(U)
    for mu in range(1, 5):
        straight = [mu] * L
        acc = w0 * fine_path_product(U, straight)
        for nu in range(1, 5):
            if nu == mu:
                continue
            for sgn in (1, -1):
                acc = acc + w1 * fine_path_product(U, [sgn * nu] + straight + [-sgn * nu])
        V[mu - 1] = acc / np.sqrt(np.sum(acc * acc, axis=-1, keepdims=True))
    return V


def coarse_path_product(V, L, steps):
    pos = np.zeros(4, dtype=int)
    W = None
    for s in steps:
        mu = abs(s) - 1
        if s > 0:
            link = np.roll(V[mu], tuple(-pos), axis=(0, 1, 2, 3))
            pos[mu] += L
        else:
            pos[mu] -= L
            link = qconj(np.roll(V[mu], tuple(-pos), axis=(0, 1, 2, 3)))
        W = link if W is None else qmul(W, link)
    return W


def edge_paths(D, R):
    c = (D - 1) // 2
    far = (R, 0, c, c)
    corners = [(0, 0, 0, 0), (0, 0, D, 0), (0, 0, D, D), (0, 0, 0, D)]
    out = []
    for k, y in enumerate(corners):
        z = corners[(k + 1) % 4]
        out.append((plaq(1, 2), lasso(coarse_steps_between(y, z), plaq(1, 2)), lasso(coarse_steps_between(y, far), plaq(3, 4))))
    return out


def permute(steps, perm):
    return [(1 if s > 0 else -1) * (perm[abs(s) - 1] + 1) for s in steps]


def measure(V, L, paths, perms):
    vals = np.zeros(4)
    for perm in perms:
        for k, (s1, s2, s3) in enumerate(paths):
            v1 = coarse_path_product(V, L, permute(s1, perm))[..., 1:]
            v2 = coarse_path_product(V, L, permute(s2, perm))[..., 1:]
            v3 = coarse_path_product(V, L, permute(s3, perm))[..., 1:]
            vals[k] += 2 * np.mean(np.sum(v1 * np.cross(v2, v3), axis=-1))
    return vals / len(perms)


def gauss_coarse(lat, L, w0, w1, beta, rng):
    T = lat.T
    sq = np.sqrt(lat.inv * 4.0 / beta)
    noise = rng.normal(size=(4, 3, T, T, T, T))
    A = np.fft.ifftn(np.fft.fftn(noise, axes=(2, 3, 4, 5)) * sq, axes=(2, 3, 4, 5)).real
    A = np.moveaxis(A, 1, -1)  # (mu, x, colour)

    def line(mu, shift):
        tot = 0.0
        pos = np.array(shift)
        for _ in range(L):
            tot = tot + np.roll(A[mu], tuple(-pos), axis=(0, 1, 2, 3))
            pos[mu] += 1
        return tot

    Ac = np.zeros_like(A)
    for mu in range(4):
        acc = w0 * line(mu, [0, 0, 0, 0])
        for nu in range(4):
            if nu == mu:
                continue
            for sgn in (1, -1):
                sh = [0, 0, 0, 0]
                sh[nu] = sgn
                up = A[nu] if sgn > 0 else -np.roll(A[nu], tuple(1 if i == nu else 0 for i in range(4)), axis=(0, 1, 2, 3))
                e = [0, 0, 0, 0]
                e[mu] = L
                acc = acc + w1 * (up + line(mu, sh) - np.roll(up, tuple(-v for v in e), axis=(0, 1, 2, 3)))
        Ac[mu] = acc
    return expq(Ac)


def main():
    Tc = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    D = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    R = int(sys.argv[3]) if len(sys.argv) > 3 else 2
    beta = float(sys.argv[4]) if len(sys.argv) > 4 else 16.0
    nmeas = int(sys.argv[5]) if len(sys.argv) > 5 else 100
    nperm = int(sys.argv[6]) if len(sys.argv) > 6 else 6
    seed = int(sys.argv[7]) if len(sys.argv) > 7 else 0
    L, w0 = 3, 0.4
    T = L * Tc
    lat = Lat(4, T)
    block = Block(lat, L, w0)
    w1 = block.w1
    sc, st, flux, Pk = run_rect(block, D, R)
    # exact tree value for the Gaussian potential on the level-1 lattice, with the blocked covariance: Levy area of the blocked values on coarse paths
    fine = lambda y: tuple(L * v for v in y)
    c0 = (D - 1) // 2
    far_c = (R, 0, c0, c0)
    corners = [(0, 0, 0, 0), (0, 0, D, 0), (0, 0, D, D), (0, 0, 0, D)]
    Es = {y: field_E(lat, CoarsePath(block, fine(y), plaq(1, 2)).current()) for y in corners}
    E3 = field_E(lat, CoarsePath(block, fine(far_c), plaq(3, 4)).current())
    st_g = 0.0
    for k, y in enumerate(corners):
        z = corners[(k + 1) % 4]
        G1 = CoarsePath(block, fine(y), plaq(1, 2))
        G2 = CoarsePath(block, fine(y), lasso(coarse_steps_between(y, z), plaq(1, 2)))
        G3 = CoarsePath(block, fine(y), lasso(coarse_steps_between(y, far_c), plaq(3, 4)))
        st_g += -12.0 * (G1.form_coarse(Es[z], E3) + G2.form_coarse(E3, Es[y]) + G3.form_coarse(Es[y], Es[z])) / Pk
    print(f"T_c={Tc} T_f={T} D={D} R={R} w0={w0}: tree Stk_total={st:.5e} -24Flux={-24*flux:.5e} Stk_G1 exact={st_g:.5e} Stk_comp(fine form)={sc:.5e} P_k={Pk:.5e} rss={check_rss():.2f}GB", flush=True)
    rng = np.random.default_rng(int(beta) + 7 * R + 1000 * D + 100000 * seed)
    perms = list(itertools.permutations(range(4)))
    rng.shuffle(perms)
    perms = perms[:nperm]
    paths = edge_paths(D, R)
    f = Field(T, rng)
    t0 = time.time()
    for _ in range(100):
        f.sweep(beta)
    print(f"thermalised {time.time()-t0:.0f}s", flush=True)
    ws, gs = [], []
    for i in range(nmeas):
        for _ in range(2):
            f.sweep(beta)
        V = block_links(f.U, L, w0, w1)
        ws.append(np.sum(measure(V, L, paths, perms)) / Pk)
        G = gauss_coarse(lat, L, w0, w1, beta, rng)
        gs.append(np.sum(measure(G, L, paths, perms)) / Pk)
        if (i + 1) % 100 == 0:
            print(f"  {i+1} measured, {time.time()-t0:.0f}s", flush=True)
    w, we = binned_err(np.array(ws), nbins=10)
    g, ge = binned_err(np.array(gs), nbins=10)
    print(f"beta={beta:g} nmeas={nmeas} time={time.time()-t0:.0f}s rss={check_rss():.2f}GB")
    print(f"Wilson blocked beta^2 Stk = {beta**2*w:.4e} +- {beta**2*we:.4e}   Gaussian level 1 beta^2 Stk = {beta**2*g:.4e} +- {beta**2*ge:.4e}")
    print(f"difference of predictions in units of the Wilson sigma: {abs(st+24*flux)/(beta**2*we):.1f}")


if __name__ == "__main__":
    main()
