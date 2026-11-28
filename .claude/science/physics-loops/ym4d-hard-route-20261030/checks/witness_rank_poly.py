#!/usr/bin/env python3
"""The moment map in polynomial gauges, in the continuum form: a pair of linear potentials.

For A = M x + c, A' = M' x + c', with F_mu_nu = M_nu_mu - M_mu_nu, the current of the two fields is (hand derivation, Text 7 item 27)
    J2(A', A) = R(M) A' - R(M') A,      R(M) := tr(M) 1 - 2 M + M^T.
So J2 = 0 for all x exactly when R(M) M' = R(M') M and R(M) c' = R(M') c. The fluxes F' reached by solutions M' of the first equation form a subspace of Lambda^2, of dimension d(M).
The moment map on the kernel of the site densities has rank r(M) = 6 - d(M) in the polynomial gauge M, if rough gauges do not do better.

Known by hand: M = e_1 e_0^T (A_1 = x_0, flux F_01): solutions give fluxes F_01, F_02, F_03, F_23: d = 4, r = 2, which agrees with the lattice run of checks/witness_rank_moment.py (rank 2, F = F_01, t = 0).

PRE-REGISTERED CRITERIA (written before the first run).
 P0: the formula for J2 against the direct continuum expression, on random M, M', c, c', x: relative 1e-12.
 P1: M = e_1 e_0^T: d = 4.
 P2: random M: d = 1 (only M' = M).  Fock M = antisymmetric generic: d = 2.  Fock simple: report.
 P3 SEARCH: minimise r(M) over M with F != 0. Method: M of the structured forms (rank one, rank two, block, nilpotent, random symmetric part added to antisymmetric), plus optimisation of the sum of the smallest singular values of the map.
    If r(M) = 0 is found with F != 0, the statement "the moment map is not zero" is false in a polynomial gauge: report M. If min r(M) >= 1 in all forms: numerical evidence (only).
"""
from __future__ import annotations

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("VECLIB_MAXIMUM_THREADS", "1")

import itertools

import numpy as np
from scipy.optimize import minimize

PLANES = list(itertools.combinations(range(4), 2))


def R(M):
    return np.trace(M) * np.eye(4) - 2 * M + M.T


def J2_direct(M, c, Mp, cp, x):
    A = M @ x + c
    Ap = Mp @ x + cp
    F = M.T - M  # F_mu_nu = d_mu A_nu - d_nu A_mu = M_nu_mu - M_mu_nu
    Fp = Mp.T - Mp
    out = np.zeros(4)
    for nu in range(4):
        v = -np.trace(Mp) * A[nu] + np.trace(M) * Ap[nu]
        for mu in range(4):
            # - A'_mu d_nu A_mu + A_mu d_nu A'_mu + 2 F'_mu_nu A_mu - 2 F_mu_nu A'_mu
            v += -Ap[mu] * M[mu, nu] + A[mu] * Mp[mu, nu] + 2 * Fp[mu, nu] * A[mu] - 2 * F[mu, nu] * Ap[mu]
        out[nu] = v
    return out


def linmap(M):
    """Matrix of M' -> R(M) M' - R(M') M on 16 dimensions."""
    L = np.zeros((16, 16))
    for i in range(16):
        E = np.zeros(16)
        E[i] = 1
        Mp = E.reshape(4, 4)
        L[:, i] = (R(M) @ Mp - R(Mp) @ M).ravel()
    return L


def flux_map():
    Fl = np.zeros((6, 16))
    for k, (mu, nu) in enumerate(PLANES):
        E = np.zeros((4, 4))
        E[nu, mu] += 1
        E[mu, nu] -= 1
        Fl[k] = E.ravel()
    return Fl


FL = flux_map()


def d_of(M, tol=1e-9):
    L = linmap(M)
    U, s, Vt = np.linalg.svd(L)
    ker = Vt[s < tol * max(s[0], 1e-300)]
    if ker.shape[0] == 0:
        return 0, s
    return int(np.linalg.matrix_rank(FL @ ker.T, tol=1e-8)), s


def main():
    rng = np.random.default_rng(1)
    worst = 0.0
    for _ in range(50):
        M, Mp = rng.normal(size=(2, 4, 4))
        c, cp, x = rng.normal(size=(3, 4))
        d = J2_direct(M, c, Mp, cp, x)
        f = R(M) @ (Mp @ x + cp) - R(Mp) @ (M @ x + c)
        worst = max(worst, np.abs(d - f).max() / np.abs(d).max())
    print(f"P0 formula worst relative difference {worst:.1e}")
    M = np.zeros((4, 4))
    M[1, 0] = 1
    print(f"P1 M = e_1 e_0^T: d = {d_of(M)[0]}, r = {6 - d_of(M)[0]}")
    M = rng.normal(size=(4, 4))
    print(f"P2 random M: d = {d_of(M)[0]}")
    Af = rng.normal(size=(4, 4))
    Af = Af - Af.T
    print(f"P2 Fock generic: d = {d_of(Af)[0]}")
    Fs = np.zeros((4, 4))
    Fs[0, 1] = 1
    Fs[1, 0] = -1
    print(f"P2 Fock simple: d = {d_of(Fs)[0]}")
    # structured forms
    best = {}
    def record(label, M):
        F = M.T - M
        if np.linalg.norm(F) < 1e-6 * max(np.linalg.norm(M), 1e-300):
            return
        d = d_of(M)[0]
        if label not in best or d > best[label][0]:
            best[label] = (d, M.copy())
    for trial in range(4000):
        u, v, w, z = rng.normal(size=(4, 4))
        record("rank one", np.outer(u, v))
        vv = v - (v @ u) / (u @ u) * u
        record("rank one, u.v = 0", np.outer(u, vv))
        record("rank two", np.outer(u, v) + np.outer(w, z))
        ww = w - (w @ vv) / (vv @ vv) * vv
        record("u v^T + w v^T, v perp", np.outer(u - (u @ vv) / (vv @ vv) * vv, vv) + np.outer(ww, vv))
        record("x_0 times polarisations", np.array([[0, 0, 0, 0], [rng.normal(), 0, 0, 0], [rng.normal(), 0, 0, 0], [rng.normal(), 0, 0, 0]]))
        G = rng.normal(size=(4, 4))
        record("random", G)
        record("block 2 + 2", np.block([[rng.normal(size=(2, 2)), np.zeros((2, 2))], [np.zeros((2, 2)), rng.normal(size=(2, 2))]]))
        N = np.triu(rng.normal(size=(4, 4)), 1)
        record("strictly triangular", N)
        Q, _ = np.linalg.qr(rng.normal(size=(4, 4)))
        record("rotated triangular", Q @ N @ Q.T)
        record("x_0 e_i + x_i e_j type", np.array([[0, 0, 0, 0], [rng.normal(), 0, 0, 0], [rng.normal(), rng.normal(), 0, 0], [rng.normal(), rng.normal(), rng.normal(), 0]]))
        ii = rng.integers(0, 4, size=3)
        E = np.zeros((4, 4))
        for a in range(3):
            E[rng.integers(0, 4), rng.integers(0, 4)] = rng.choice([-1.0, 1.0, 2.0, 0.5])
        record("sparse", E)
    for k, (d, M) in sorted(best.items(), key=lambda kv: -kv[1][0]):
        print(f"P3 {k}: largest d = {d}, r = {6 - d}")
    # optimisation: want a large kernel with all fluxes: minimise the sum of the 6 smallest singular values, keeping F normalised
    def obj(m):
        M = m.reshape(4, 4)
        n = np.linalg.norm(M.T - M)
        if n < 1e-8:
            return 1e3
        M = M / n
        s = np.linalg.svd(linmap(M), compute_uv=False)
        return float(np.sum(s[-6:] ** 2))
    bestv = (1e9, None)
    for st in range(30):
        m0 = rng.normal(size=16)
        res = minimize(obj, m0, method="Nelder-Mead", options={"maxiter": 6000, "maxfev": 6000, "xatol": 1e-7, "fatol": 1e-12})
        res = minimize(obj, res.x, method="BFGS", options={"maxiter": 400})
        if res.fun < bestv[0]:
            bestv = (res.fun, res.x.copy())
    M = bestv[1].reshape(4, 4)
    M = M / np.linalg.norm(M.T - M)
    d, s = d_of(M, tol=1e-6)
    print(f"P3 optimisation: smallest sum of squares of six smallest sv {bestv[0]:.3e}; there d = {d}, sv {np.array2string(s, precision=2)}")
    print(np.array2string(M, precision=3, suppress_small=True))


if __name__ == "__main__":
    main()
