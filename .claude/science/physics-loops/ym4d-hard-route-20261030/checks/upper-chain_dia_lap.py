#!/usr/bin/env python3
"""Criteria L0-L2: exact (DIA-B) at order 1/beta on a closed cube, by Laplace at the minimiser.

Links U_b = exp(i a.sigma/2) U_b; for a plaquette with holonomy h = h0 + i hv.sigma,
s_q(a) = s_q + (1/2) (sum c_k).hv + (h0/8) |sum c_k|^2 - (1/4) sum_{k<l} (c_k x c_l).hv + ...
with c_k = C_k a_k. Usage: upper-chain_dia_lap.py r seed
"""
import itertools
import os
import resource
import sys
import time

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import numpy as np

SIG = np.array([[[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]]], dtype=complex)
RSS_CAP = 2 * 1024**3


def check_rss():
    if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > RSS_CAP:
        sys.exit("RSS above cap")


def exp_su2(a):
    th = np.linalg.norm(a, axis=-1)
    c = np.cos(th / 2)
    s = 0.5 * np.sinc(th / (2 * np.pi))
    out = np.zeros(a.shape[:-1] + (2, 2), dtype=complex)
    out[..., 0, 0] = c + 1j * s * a[..., 2]
    out[..., 1, 1] = c - 1j * s * a[..., 2]
    out[..., 0, 1] = 1j * s * a[..., 0] + s * a[..., 1]
    out[..., 1, 0] = 1j * s * a[..., 0] - s * a[..., 1]
    return out


def dag(g):
    return np.conj(np.swapaxes(g, -1, -2))


def ad(g):
    """R with g (a.sigma) g^-1 = (R a).sigma."""
    gs = g[..., None, :, :] @ SIG
    return 0.5 * np.real(np.einsum("ikl,...jlm,...mk->...ij", SIG, gs, dag(g)))


def h_parts(h):
    h0 = 0.5 * np.real(h[..., 0, 0] + h[..., 1, 1])
    hv = np.stack([0.5 * np.imag(np.einsum("kl,...lk->...", SIG[i], h)) for i in range(3)], axis=-1)
    return h0, hv


def cross_mat(v):
    m = np.zeros(v.shape[:-1] + (3, 3))
    m[..., 0, 1] = -v[..., 2]
    m[..., 0, 2] = v[..., 1]
    m[..., 1, 0] = v[..., 2]
    m[..., 1, 2] = -v[..., 0]
    m[..., 2, 0] = -v[..., 1]
    m[..., 2, 1] = v[..., 0]
    return m


class Cube:
    def __init__(self, r):
        self.r = r
        coords = range(-r, r + 1)
        self.link = {}
        self.free_of = []
        nf = 0
        for x in itertools.product(coords, repeat=4):
            for mu in range(4):
                if x[mu] == r:
                    continue
                free = all(abs(x[n]) < r for n in range(4) if n != mu)
                self.link[(x, mu)] = len(self.free_of)
                self.free_of.append(nf if free else -1)
                nf += 1 if free else 0
        self.free_of = np.array(self.free_of)
        self.nf = nf
        self.nl = len(self.free_of)
        self.bdy = np.where(self.free_of < 0)[0]
        self.bdy_of = -np.ones(self.nl, dtype=int)
        self.bdy_of[self.bdy] = np.arange(len(self.bdy))
        plaq = []
        self.pindex = {}
        for x in itertools.product(coords, repeat=4):
            for mu, nu in itertools.combinations(range(4), 2):
                if x[mu] == r or x[nu] == r:
                    continue
                xm = list(x)
                xm[mu] += 1
                xn = list(x)
                xn[nu] += 1
                ls = (self.link[(x, mu)], self.link[(tuple(xm), nu)], self.link[(tuple(xn), mu)], self.link[(x, nu)])
                if any(self.free_of[l] >= 0 for l in ls):
                    self.pindex[(x, mu, nu)] = len(plaq)
                    plaq.append(ls)
        self.plaq = np.array(plaq)
        self.np = len(plaq)
        self.pf = self.free_of[self.plaq]

    def plaq_data(self, U):
        u = U[self.plaq]
        U1, U2, U3, U4 = u[:, 0], u[:, 1], u[:, 2], u[:, 3]
        P3 = U1 @ U2 @ dag(U3)
        h = P3 @ dag(U4)
        C = np.zeros((self.np, 4, 3, 3))
        C[:, 0] = np.eye(3)
        C[:, 1] = ad(U1)
        C[:, 2] = -ad(P3)
        C[:, 3] = -ad(h)
        h0, hv = h_parts(h)
        return h0, hv, C

    def gradient(self, U):
        h0, hv, C = self.plaq_data(U)
        g = np.zeros(3 * self.nf)
        gk = 0.5 * np.einsum("pkji,pj->pki", C, hv)
        for k in range(4):
            mask = self.pf[:, k] >= 0
            for i in range(3):
                np.add.at(g, 3 * self.pf[mask, k] + i, gk[mask, k, i])
        s = 1 - h0
        return g, s

    def q_blocks(self, U):
        """Q_q as blocks over (k, l), k, l in 0..3, with free links only used later."""
        h0, hv, C = self.plaq_data(U)
        X = cross_mat(hv)
        Q = np.zeros((self.np, 4, 4, 3, 3))
        for k in range(4):
            Q[:, k, k] = (h0[:, None, None] / 4) * np.eye(3)
            for l in range(k + 1, 4):
                b = (h0[:, None, None] / 4) * np.einsum("pji,pjm->pim", C[:, k], C[:, l])
                b += 0.25 * np.einsum("pji,pjn,pnm->pim", C[:, k], X, C[:, l])
                Q[:, k, l] = b
                Q[:, l, k] = np.swapaxes(b, 1, 2)
        return Q, h0, hv

    def hessian(self, Q):
        n = 3 * self.nf
        H = np.zeros((n, n))
        for k in range(4):
            for l in range(4):
                mask = (self.pf[:, k] >= 0) & (self.pf[:, l] >= 0)
                fk = 3 * self.pf[mask, k]
                fl = 3 * self.pf[mask, l]
                b = Q[mask, k, l]
                for i in range(3):
                    for j in range(3):
                        np.add.at(H, (fk + i, fl + j), b[:, i, j])
        return H

    def traces(self, Q, G):
        out = np.zeros(self.np)
        for k in range(4):
            for l in range(4):
                mask = (self.pf[:, k] >= 0) & (self.pf[:, l] >= 0)
                fk = 3 * self.pf[mask, k]
                fl = 3 * self.pf[mask, l]
                b = Q[mask, k, l]
                val = np.zeros(mask.sum())
                for i in range(3):
                    for j in range(3):
                        val += b[:, i, j] * G[fl + j, fk + i]
                out[mask] += val
        return out


def pinv_sym(H, tol=1e-9):
    w, v = np.linalg.eigh(H)
    keep = w > tol
    return (v[:, keep] / w[keep]) @ v[:, keep].T, w, int(keep.sum())


def apply_free(U, cube, a):
    a3 = a.reshape(-1, 3)
    idx = np.where(cube.free_of >= 0)[0]
    U = U.copy()
    U[idx] = exp_su2(a3[cube.free_of[idx]]) @ U[idx]
    return U


def minimise(cube, U, G0, tol=1e-11):
    for it in range(200):
        g, _ = cube.gradient(U)
        if np.linalg.norm(g) < tol:
            return U, it
        U = apply_free(U, cube, -G0 @ g)
    # finish with true Newton steps
    for it in range(10):
        g, _ = cube.gradient(U)
        if np.linalg.norm(g) < tol:
            return U, 200 + it
        Q, _, _ = cube.q_blocks(U)
        G, _, _ = pinv_sym(cube.hessian(Q))
        U = apply_free(U, cube, -G @ g)
    raise RuntimeError("no convergence")


class Problem:
    def __init__(self, r):
        self.cube = c = Cube(r)
        self.U0 = np.tile(np.eye(2, dtype=complex), (c.nl, 1, 1))
        Q0, _, _ = c.q_blocks(self.U0)
        H0 = c.hessian(Q0)
        self.G0, w0, self.rank = pinv_sym(H0)
        self.T0 = c.traces(Q0, self.G0)
        # scalar curvature map at cold: signs of the four links
        sg = np.array([1, 1, -1, -1])
        Df = np.zeros((c.np, c.nf))
        Db = np.zeros((c.np, len(c.bdy)))
        for k in range(4):
            mf = c.pf[:, k] >= 0
            Df[np.where(mf)[0], c.pf[mf, k]] += sg[k]
            mb = ~mf
            Db[np.where(mb)[0], c.bdy_of[c.plaq[mb, k]]] += sg[k]
        Gs = self.G0[::3, ::3]
        self.A_all = Db - 0.25 * Df @ (Gs @ (Df.T @ Db))
        self.nb = len(c.bdy)

    def boundary_config(self, eta3):
        """eta3 has shape (nb, 3)."""
        U = self.U0.copy()
        U[self.cube.bdy] = exp_su2(eta3)
        return U

    def evaluate(self, eta3, eps, weights):
        c = self.cube
        U, _ = minimise(c, self.boundary_config(eps * eta3), self.G0)
        Q, _, _ = c.q_blocks(U)
        G, w, rk = pinv_sym(c.hessian(Q))
        T = c.traces(Q, G)
        g, s = c.gradient(U)
        delta = 0.5 * (T - self.T0)
        return float(np.sum(weights * delta)), float(np.sum(delta)), float(np.sum(weights * s)), rk, w[0]


def nullspace_basis(A_all, target_rows, rng, m):
    """Random orthonormal directions in the boundary space, orthogonal to boundary gauge
    directions, with zero linear curvature on the target rows."""
    u, s, vt = np.linalg.svd(A_all, full_matrices=False)
    phys = vt[s > 1e-9].T  # boundary directions with non-zero curvature
    At = A_all[target_rows] @ phys
    uu, ss, vv = np.linalg.svd(At, full_matrices=True)
    rk = int((ss > 1e-9).sum())
    N = phys @ vv[rk:].T
    coef = rng.standard_normal((N.shape[1], m))
    B = N @ coef
    B, _ = np.linalg.qr(B)
    return B, N.shape[1], rk


def structured_basis(pr, target_rows, m):
    """Top right singular vectors, inside the null space of the target, of the linear
    curvature on plaquettes sharing a link with the target."""
    c = pr.cube
    tgt_links = set(c.plaq[target_rows].ravel().tolist())
    near = [q for q in range(c.np) if q not in set(target_rows) and tgt_links.intersection(c.plaq[q].tolist())]
    u, s, vt = np.linalg.svd(pr.A_all, full_matrices=False)
    phys = vt[s > 1e-9].T
    At = pr.A_all[target_rows] @ phys
    uu, ss, vv = np.linalg.svd(At, full_matrices=True)
    rk = int((ss > 1e-9).sum())
    N = phys @ vv[rk:].T
    An = pr.A_all[near] @ N
    uu2, ss2, vv2 = np.linalg.svd(An, full_matrices=False)
    print(f"structured basis: near plaquettes {len(near)}, null dim {N.shape[1]}, top singular values {ss2[:3]}, at {m}: {ss2[min(m, len(ss2)) - 1]:.3e}", flush=True)
    return N @ vv2[:m].T


def normalize(eta3, A_all):
    return eta3 / max(np.abs(A_all @ eta3).max(), 1e-12)


def rayleigh(pr, basis, weights, eps, colours, rng, label):
    """Quadratic form of D on the span of basis, with colour patterns as given."""
    m = basis.shape[1]
    vecs = []
    for j in range(m):
        if colours == 1:
            e = np.zeros((pr.nb, 3))
            e[:, 2] = basis[:, j]
        else:
            n = rng.standard_normal((3, 1))
            n /= np.linalg.norm(n)
            e = basis[:, j][:, None] @ n.T
            if j >= m // 2:
                e = np.column_stack([basis[:, j], basis[:, (j + 1) % m], basis[:, (j + 2) % m]]) / np.sqrt(3)
        vecs.append(normalize(e, pr.A_all))
    M = np.zeros((m, m))
    diag = np.zeros(m)
    maxsum = 0.0
    t0 = time.time()
    for i in range(m):
        d, tot, _, _, _ = pr.evaluate(vecs[i], eps, weights)
        maxsum = max(maxsum, abs(tot))
        diag[i] = d / eps**2
    for i in range(m):
        M[i, i] = diag[i]
        for j in range(i + 1, m):
            d, tot, _, _, _ = pr.evaluate((vecs[i] + vecs[j]) / np.sqrt(2), eps, weights)
            maxsum = max(maxsum, abs(tot))
            M[i, j] = M[j, i] = d / eps**2 - 0.5 * (diag[i] + diag[j])
        check_rss()
    # generalized problem: the vectors are not orthonormal, so use their Gram matrix
    V = np.array([v.ravel() for v in vecs]).T
    Gram = V.T @ V
    L = np.linalg.cholesky(Gram + 1e-12 * np.eye(m))
    Li = np.linalg.inv(L)
    w, x = np.linalg.eigh(Li @ M @ Li.T)
    best = Li.T @ x[:, 0]
    eta = sum(best[k] * vecs[k] for k in range(m))
    eta = normalize(eta, pr.A_all)
    d1 = pr.evaluate(eta, eps, weights)
    d2 = pr.evaluate(eta, eps / 2, weights)
    D1, D2 = d1[0] / eps**2, d2[0] / (eps / 2) ** 2
    print(f"{label}: lambda_min = {w[0]:.4e}, lambda_max = {w[-1]:.4e}, D(best dir, unit max curvature) = {D1:.5e} at eps, {D2:.5e} at eps/2, tol = {abs(D1-D2):.2e}, max |zero sum| = {maxsum:.2e}, s on target = {d1[2]:.2e}, min eig = {d1[4]:.2e}, time = {time.time()-t0:.0f}s", flush=True)
    return eta, D1, D2


def sanity(pr, rng):
    c = pr.cube
    U = pr.U0.copy()
    a = 0.05 * rng.standard_normal((c.nl, 3))
    U = exp_su2(a)
    Q, _, _ = c.q_blocks(U)
    H = c.hessian(Q)
    g0, _ = c.gradient(U)
    v = rng.standard_normal(3 * c.nf)
    v /= np.linalg.norm(v)
    e = 1e-5
    gp, _ = c.gradient(apply_free(U, c, e * v))
    gm, _ = c.gradient(apply_free(U, c, -e * v))
    # second difference of the total action along v is v.H.v
    W = lambda W_U: np.sum(c.gradient(W_U)[1])
    d2 = (W(apply_free(U, c, 1e-4 * v)) + W(apply_free(U, c, -1e-4 * v)) - 2 * W(U)) / 1e-8
    print(f"L0 v.H.v = {v @ H @ v:.8f}, finite difference {d2:.8f}", flush=True)
    return abs(v @ H @ v - d2) / abs(d2)


def main(r, seed):
    rng = np.random.default_rng(seed)
    pr = Problem(r)
    c = pr.cube
    print(f"r={r}: free links {c.nf}, boundary links {pr.nb}, plaquettes {c.np}, rank H {pr.rank}, expected {3*(c.nf-(2*r-1)**4)}", flush=True)
    rel = sanity(pr, rng)
    print(f"L0 relative Hessian error {rel:.2e}; sum Tr(Q G) at cold = {pr.T0.sum():.6f}", flush=True)
    x0 = (0, 0, 0, 0)
    # target T1
    p = pr.cube.pindex[(x0, 0, 1)]
    w1 = np.zeros(c.np)
    w1[p] = 1.0
    print(f"cold T1: (1/2) Tr(Q G) = {0.5*pr.T0[p]:.6f}", flush=True)
    # target T2: the 24 plaquettes with corner at the centre site
    rows = []
    for mu, nu in itertools.combinations(range(4), 2):
        for i in (0, 1):
            for j in (0, 1):
                x = [0, 0, 0, 0]
                x[mu] -= i
                x[nu] -= j
                rows.append(pr.cube.pindex[(tuple(x), mu, nu)])
    w2 = np.zeros(c.np)
    w2[rows] = 0.25
    print(f"cold T2: (1/2) Tr(Q G) weighted = {0.5*np.sum(w2*pr.T0):.6f}", flush=True)
    eps = 0.03
    if len(sys.argv) > 3 and sys.argv[3] == "structured":
        for label, tr, w in (("T1", [p], w1), ("T2", rows, w2)):
            B = structured_basis(pr, tr, 80)
            rayleigh(pr, B, w, eps, 1, rng, label + " structured one colour")
        print("RESULT structured done", flush=True)
        return
    for label, tr, w in (("T1", [p], w1), ("T2", rows, w2)):
        B, dim, rk = nullspace_basis(pr.A_all, tr, rng, 24)
        print(f"{label}: physical boundary directions with zero linear curvature on target: {dim}, constraints {rk}", flush=True)
        rayleigh(pr, B, w, eps, 1, rng, label + " one colour")
        B2, _, _ = nullspace_basis(pr.A_all, tr, rng, 12)
        rayleigh(pr, B2, w, eps, 3, rng, label + " three colours")
    print("RSS GB", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e9)
    print("RESULT done", flush=True)


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 2, int(sys.argv[2]) if len(sys.argv) > 2 else 7)
