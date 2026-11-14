#!/usr/bin/env python3
"""Rank of the contracted Wilson cubic form, against the bound forced by an isotropic slice.

The colour-contracted cubic form on single-colour link fields is, I claim (hand derivation, checked here as R1), the 3-form
    VV := sum_p phi_p ^ abar_mu^p ^ abar_nu^p,
with phi_p the curl on the plaquette and abar_mu^p the mean of the two mu links of p. If a linear subspace S of link fields, complementary to the gradients, has
VV(a, a', b) = 0 for all a, a', b in S, then for b in S the 2-form B[b] := VV(., ., b) vanishes on S x S, so rank B[b] <= 2 codim S = 2 (V - 1).
This holds with no symmetry of S at all.

PRE-REGISTERED CRITERIA (written before the first run).
 R1 FORMULA: 2 VV(a, a', a'') equals the sum of V_p of checks/witness_tree_coeff.py K_vert / 12, on random fields, relative 1e-12. FAIL stops everything.
 R2 GENERIC RANK: for random b on the torus, report rank B[b]. Expect rank > 2 (V - 1) in d = 3, 4. If not, the route is dead as stated.
 R3 FLUX IS NOT PURE GAUGE: for b = random field, report rank for b + d X with X random of amplitudes 0.1, 1, 10, and for X staggered (expect no change, the staggered part decouples).
 R4 ADVERSARY: for fixed flux, minimise over X the sum of squares of the singular values beyond the bound, in absolute size, against its value at X = 0. If it reaches below 1e-12 of that,
    a rank-deficient gauge exists and the route needs more than one b; report it. If the minimum stays above 1e-6 of it from all starts, that is numerical evidence (only) for a lower bound.
    Changed after the first run: that run normalised by the largest singular value, and the optimiser cheated with a huge localised X (|dX| ~ 1e6), which inflates the largest singular value and
    leaves the tail alone; rank(1e-8) stayed at 314 to 318 of 324. Absolute size removes the cheat. The first form is not evidence either way.
"""
from __future__ import annotations

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("VECLIB_MAXIMUM_THREADS", "1")

import resource
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))


def check_rss(limit_gb=2.0):
    r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024**3
    if r > limit_gb:
        raise MemoryError(f"rss {r:.2f} GB")
    return r


class Torus:
    def __init__(self, d, T):
        self.d, self.T = d, T
        self.V = T**d
        self.W = d * self.V
        self.shape = (T,) * d

    def s(self, x):
        out = 0
        for c in x:
            out = out * self.T + (c % self.T)
        return out

    def l(self, x, mu):
        return mu * self.V + self.s(x)

    def sites(self):
        return np.ndindex(*self.shape)

    def shift(self, x, mu, n=1):
        y = list(x)
        y[mu] += n
        return tuple(y)

    def plaquette_functionals(self):
        """List of (phi, abar_mu, abar_nu), each a list of (link, coefficient)."""
        out = []
        for x in self.sites():
            for mu in range(self.d):
                for nu in range(mu + 1, self.d):
                    a = self.l(x, mu)
                    b = self.l(self.shift(x, mu), nu)
                    c = self.l(self.shift(x, nu), mu)
                    e = self.l(x, nu)
                    out.append(([(a, 1.0), (b, 1.0), (c, -1.0), (e, -1.0)], [(a, 0.5), (c, 0.5)], [(b, 0.5), (e, 0.5)]))
        return out

    def grad(self, X):
        g = np.zeros(self.W)
        arr = X.reshape(self.shape)
        for mu in range(self.d):
            g[mu * self.V : (mu + 1) * self.V] = (np.roll(arr, -1, axis=mu) - arr).ravel()
        return g


def build_arrays(tor):
    """phi, m1, m2 as dense integer-indexed arrays: shape (np, 4) links and coefficients for phi; (np, 2) for the means."""
    pf = tor.plaquette_functionals()
    n = len(pf)
    L = np.zeros((n, 4), dtype=int)
    for i, (phi, m1, m2) in enumerate(pf):
        L[i] = [phi[0][0], phi[1][0], phi[2][0], phi[3][0]]
    return L  # order a, b, c, e: a, c are the mu links; b, e the nu links


def values(L, a):
    A, Bb, C, Ee = a[L[:, 0]], a[L[:, 1]], a[L[:, 2]], a[L[:, 3]]
    return A + Bb - C - Ee, 0.5 * (A + C), 0.5 * (Bb + Ee)


def VV(L, a1, a2, a3):
    p1, m1, n1 = values(L, a1)
    p2, m2, n2 = values(L, a2)
    p3, m3, n3 = values(L, a3)
    return float(np.sum(p1 * (m2 * n3 - n2 * m3) - m1 * (p2 * n3 - n2 * p3) + n1 * (p2 * m3 - m2 * p3)))


def Bmat(L, b, W):
    """Antisymmetric matrix of B[b](a, a') = VV(a, a', b)."""
    f, bm, bn = values(L, b)
    M = np.zeros((W, W))
    ph = np.array([1.0, 1.0, -1.0, -1.0])
    me = np.array([0.5, 0.0, 0.5, 0.0])
    ne = np.array([0.0, 0.5, 0.0, 0.5])
    # det(a, a', b) with rows (phi, m, n) = phi(b) (m ^ n)(a, a') + m(b) (n ^ phi)(a, a') + n(b) (phi ^ m)(a, a')
    for i in range(L.shape[0]):
        idx = L[i]
        wedge = f[i] * (np.outer(me, ne) - np.outer(ne, me)) + bm[i] * (np.outer(ne, ph) - np.outer(ph, ne)) + bn[i] * (np.outer(ph, me) - np.outer(me, ph))
        M[np.ix_(idx, idx)] += wedge
    return M


def K_vert_direct(tor, L, a1, a2, a3):
    # the sum in witness_tree_coeff.K_vert over a plaquette: sum_(i<j) det(P, inc_i, inc_j)
    tot = 0.0
    incs = []
    for a in (a1, a2, a3):
        A, Bb, C, Ee = a[L[:, 0]], a[L[:, 1]], a[L[:, 2]], a[L[:, 3]]
        incs.append([A, Bb, -C, -Ee, A + Bb - C - Ee])
    for i in range(4):
        for j in range(i + 1, 4):
            r0 = [incs[k][4] for k in range(3)]
            r1 = [incs[k][i] for k in range(3)]
            r2 = [incs[k][j] for k in range(3)]
            tot += np.sum(r0[0] * (r1[1] * r2[2] - r1[2] * r2[1]) - r0[1] * (r1[0] * r2[2] - r1[2] * r2[0]) + r0[2] * (r1[0] * r2[1] - r1[1] * r2[0]))
    return float(tot)


def rank_of(M, tol=1e-10):
    s = np.linalg.svd(M, compute_uv=False)
    return int(np.sum(s > tol * s[0])) if s[0] > 0 else 0, s


def adversary(tor, L, b0, bound, rng, steps, x0=None, lr=None):
    """Minimise sum_(i > bound) sigma_i^2 / sigma_1^2 over X with fixed flux, by L-BFGS on X."""
    from scipy.optimize import minimize

    V, W = tor.V, tor.W
    basis_cache = {}

    def gradB_entries(u, v):
        # d/dX_x of u^T B[b + dX] v, via VV(u, v, d delta_x), summed by adjoint: grad_b of VV(u, v, b) then d^T
        pu, mu, nu = values(L, u)
        pv, mv, nv = values(L, v)
        # VV(u, v, b) = sum_p [ f(b) (mu nv - nu mv) + bm (nu pv - pu nv) + bn (pu mv - mu pv) ]
        c_f = mu * nv - nu * mv
        c_m = nu * pv - pu * nv
        c_n = pu * mv - mu * pv
        g = np.zeros(W)
        np.add.at(g, L[:, 0], c_f + 0.5 * c_m)
        np.add.at(g, L[:, 1], c_f + 0.5 * c_n)
        np.add.at(g, L[:, 2], -c_f + 0.5 * c_m)
        np.add.at(g, L[:, 3], -c_f + 0.5 * c_n)
        return g

    def d_T(g):
        out = np.zeros(tor.shape)
        for mu in range(tor.d):
            arr = g[mu * V : (mu + 1) * V].reshape(tor.shape)
            out += np.roll(arr, 1, axis=mu) - arr
        return out.ravel()

    def fun(X):
        b = b0 + tor.grad(X)
        M = Bmat(L, b, W)
        U, s, Vt = np.linalg.svd(M)
        val = float(np.sum(s[bound:] ** 2))
        # gradient of sum_(i >= bound) s_i^2
        g = np.zeros(W)
        for i in range(bound, len(s)):
            if s[i] > 1e-14 * s[0]:
                g += 2 * s[i] * gradB_entries(U[:, i], Vt[i, :])
        return val, d_T(g)

    if x0 is None:
        x0 = rng.normal(size=V)
    res = minimize(fun, x0, jac=True, method="L-BFGS-B", options={"maxiter": steps, "maxfun": steps + 20, "ftol": 1e-22, "gtol": 1e-12})
    return res.fun, res.x, res.nit


def plane_wave_flux(tor, rng):
    """A smooth field with non-degenerate flux: two low plane waves in generic polarisations."""
    idx = np.indices(tor.shape).astype(float)
    b = np.zeros(tor.W)
    for mu in range(tor.d):
        ph = 0.0
        for q in range(2):
            k = rng.integers(-1, 2, size=tor.d) * 2 * np.pi / tor.T
            ph = ph + rng.normal() * np.cos(np.tensordot(k, idx, axes=1) + rng.uniform(0, 6.28))
        b[mu * tor.V : (mu + 1) * tor.V] = np.ravel(ph)
    return b


def main():
    rng = np.random.default_rng(5)
    mode = sys.argv[1] if len(sys.argv) > 1 else "basic"
    if mode == "basic":
        for d, T in ((2, 6), (3, 4), (4, 3), (4, 4)):
            t0 = time.time()
            tor = Torus(d, T)
            L = build_arrays(tor)
            a1, a2, a3 = rng.normal(size=(3, tor.W))
            lhs = 2 * VV(L, a1, a2, a3)
            rhs = K_vert_direct(tor, L, a1, a2, a3)
            print(f"R1 d={d} T={T}: 2 VV = {lhs:.8e}, sum_(i<j) det = {rhs:.8e}, rel diff {abs(lhs-rhs)/abs(rhs):.1e}", flush=True)
            M = Bmat(L, a3, tor.W)
            direct = float(a1 @ M @ a2)
            print(f"   B matrix check rel diff {abs(direct-VV(L,a1,a2,a3))/abs(direct):.1e}; antisym {np.abs(M+M.T).max():.1e}")
            bound = 2 * (tor.V - 1)
            r, s = rank_of(M)
            print(f"R2 d={d} T={T}: W={tor.W} bound 2(V-1)={bound} generic rank={r}", flush=True)
            pw = plane_wave_flux(tor, rng)
            r, s = rank_of(Bmat(L, pw, tor.W))
            print(f"   smooth b: rank={r}", flush=True)
            for amp in (0.1, 1.0, 10.0):
                X = amp * rng.normal(size=tor.V)
                r, s = rank_of(Bmat(L, pw + tor.grad(X), tor.W))
                print(f"R3 smooth b + d(random X), amp {amp}: rank={r}, smallest kept sv / largest {s[max(r-1,0)]/s[0]:.2e}", flush=True)
            if T % 2 == 0:
                st = np.indices(tor.shape).sum(axis=0) % 2 * 2.0 - 1.0
                g = tor.grad(st.ravel())
                r, s = rank_of(Bmat(L, g, tor.W))
                print(f"   staggered gradient alone: largest sv {s[0]:.1e}, rank {r}")
                r2, s2 = rank_of(Bmat(L, pw + 3 * g, tor.W))
                r3, s3 = rank_of(Bmat(L, pw, tor.W))
                print(f"   smooth + staggered: rank {r2}, difference of singular values from smooth {np.abs(s2-s3).max():.1e}")
            print(f"   time {time.time()-t0:.1f}s rss {check_rss():.2f}GB", flush=True)
    elif mode == "adv":
        d, T = int(sys.argv[2]), int(sys.argv[3])
        steps = int(sys.argv[4]) if len(sys.argv) > 4 else 300
        tor = Torus(d, T)
        L = build_arrays(tor)
        bound = 2 * (tor.V - 1)
        for label, b0 in (("random flux", rng.normal(size=tor.W)), ("smooth flux", plane_wave_flux(tor, rng))):
            f0 = np.linalg.svd(Bmat(L, b0, tor.W), compute_uv=False)
            tail0 = np.sum(f0[bound:] ** 2)
            print(f"R4 d={d} T={T} {label}: bound={bound}, tail sum at X = 0: {tail0:.3e}", flush=True)
            for st in range(3):
                t0 = time.time()
                val, X, nit = adversary(tor, L, b0, bound, rng, steps)
                s = np.linalg.svd(Bmat(L, b0 + tor.grad(X), tor.W), compute_uv=False)
                print(f"   start {st}: min tail / tail at 0 = {val/tail0:.3e} in {nit} its, rank(1e-8)={int(np.sum(s>1e-8*s[0]))}, smallest kept sv {s[-3]:.3e}, sigma[bound]={s[bound]:.3e}, |dX|max={np.abs(tor.grad(X)).max():.2e}, time={time.time()-t0:.0f}s, rss={check_rss():.2f}GB", flush=True)


if __name__ == "__main__":
    main()
