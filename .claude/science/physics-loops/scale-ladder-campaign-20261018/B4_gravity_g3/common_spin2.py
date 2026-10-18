"""Shared helpers for block B4 (graviton birefringence / g3 extraction).

Conventions
-----------
* A two-derivative quadratic form for a symmetric tensor h in d dimensions is stored
  as a rank-6 tensor T[a,b,c,d,e,f] with   S(k,h) = sum h_ab h_cd T_abcd,ef k_e k_f
  (full index sums, T symmetric in (ab), (cd), (ab)<->(cd), (ef)).
* Component vectors use HCOMP ordering (a<=b) with the ACTUAL metric components h_ab;
  matrix entries S_IJ = w_I w_J T_IJ with w = 2 for off-diagonal pairs.
* Group machinery: invariant tensors under a finite matrix group (generators), and the
  gauge-invariant subspace under delta h_ab = k_a xi_b + k_b xi_a.
"""
from __future__ import annotations

import itertools
import numpy as np


def hcomps(d):
    return [(a, a) for a in range(d)] + [(a, b) for a in range(d) for b in range(a + 1, d)]


def act_slots(X, n, d, mats):
    m = X.shape[1]
    T = X.reshape((d,) * n + (m,))
    for s in range(n):
        T = np.moveaxis(np.tensordot(mats[s], T, axes=([1], [s])), 0, s)
    return T.reshape(d ** n, m)


def permute_axes(X, n, d, perm):
    m = X.shape[1]
    T = X.reshape((d,) * n + (m,))
    return np.transpose(T, tuple(perm) + (n,)).reshape(d ** n, m)


def nullspace(A, rtol=1e-10):
    """Right null space of A (columns). Uses the small side only (no huge U matrix)."""
    A = np.asarray(A)
    if A.shape[0] >= A.shape[1]:
        _, s, vt = np.linalg.svd(A, full_matrices=False)
    else:
        _, s, vt = np.linalg.svd(A, full_matrices=True)
        s = np.concatenate([s, np.zeros(vt.shape[0] - s.size)])
    top = s[0] if s.size and s[0] > 0 else 1.0
    return vt[s <= rtol * top].conj().T


def index_sym_basis(d):
    """Orthonormal basis of rank-6 tensors with the symmetries of a quadratic 2-derivative form."""
    n = 6
    swaps = [(1, 0, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5), (2, 3, 0, 1, 4, 5), (0, 1, 2, 3, 5, 4)]
    # orbit closure
    grp = {tuple(range(n))}
    frontier = [tuple(range(n))]
    while frontier:
        new = []
        for g in frontier:
            for h in swaps:
                x = tuple(g[h[i]] for i in range(n))
                if x not in grp:
                    grp.add(x)
                    new.append(x)
        frontier = new
    seen, cols = set(), []
    for flat in range(d ** n):
        idx = np.unravel_index(flat, (d,) * n)
        orbit = sorted({tuple(idx[p[i]] for i in range(n)) for p in grp})
        if orbit[0] in seen:
            continue
        seen.add(orbit[0])
        v = np.zeros(d ** n)
        for o in orbit:
            v[np.ravel_multi_index(o, (d,) * n)] = 1.0
        cols.append(v / np.linalg.norm(v))
    return np.array(cols).T


def perm_matrices(d, signed):
    gens = []
    for i in range(d - 1):
        R = np.eye(d)
        R[[i, i + 1]] = R[[i + 1, i]]
        gens.append(R)
    if signed:
        F = np.eye(d)
        F[0, 0] = -1.0
        gens.append(F)
    return gens


def invariant_forms(d, gens, extra_rows=None):
    S = index_sym_basis(d)
    rows = [act_slots(S, 6, d, [R] * 6) - S for R in gens]
    if extra_rows:
        rows += [f(S) for f in extra_rows]
    Ginv = nullspace(np.vstack(rows))
    B = S @ Ginv
    q, _ = np.linalg.qr(B)
    return q


def gauge_variation_operator(d):
    """Linear map T -> its gauge variation tensor V[a,b,c,e,f,g] (coefficient of
    h_ab xi_c k_e k_f k_g after symmetrisation over (e,f,g)); T gauge-invariant iff V = 0.
    delta S = 2 sum h_ab T_ab,cd,ef k_e k_f (k_c xi_d + k_d xi_c) = 4 sum h_ab T_ab,cd,ef k_c k_e k_f xi_d."""
    def op(B):
        n = 6
        m = B.shape[1]
        T = B.reshape((d,) * n + (m,))
        # V[a,b,d,c,e,f] = T[a,b,c,d,e,f]; symmetrise over (c,e,f)
        V = np.transpose(T, (0, 1, 3, 2, 4, 5, 6))
        acc = np.zeros_like(V)
        for p in itertools.permutations((3, 4, 5)):
            perm = [0, 1, 2] + list(p) + [6]
            acc += np.transpose(V, perm)
        return acc.reshape(d ** n, m)
    return op


def gauge_invariant_subspace(B, d):
    op = gauge_variation_operator(d)
    V = op(B)
    K = nullspace(V)
    G = B @ K
    if G.shape[1]:
        G, _ = np.linalg.qr(G)
    return G


def tensor_to_matrix(Tflat, k, d):
    T = Tflat.reshape((d,) * 6)
    Kt = np.einsum("abcdef,e,f->abcd", T, k, k)
    hc = hcomps(d)
    w = [1.0 if a == b else 2.0 for a, b in hc]
    return np.array([[w[I] * w[J] * Kt[a, b, c, dd] for J, (c, dd) in enumerate(hc)]
                     for I, (a, b) in enumerate(hc)])


def matrix_symbol_to_tensor(Sfun, d):
    """Sfun(k) -> (nc x nc) symmetric matrix exactly quadratic in k. Returns flat rank-6 tensor."""
    hc = hcomps(d)
    w = [1.0 if a == b else 2.0 for a, b in hc]
    E = np.eye(d)
    C = {}
    for e in range(d):
        C[(e, e)] = Sfun(E[e])
    for e in range(d):
        for f in range(e + 1, d):
            C[(e, f)] = 0.5 * (Sfun(E[e] + E[f]) - C[(e, e)] - C[(f, f)])
    T = np.zeros((d,) * 6, dtype=complex)
    for (e, f), Cm in C.items():
        for I, (a, b) in enumerate(hc):
            for J, (c, dd) in enumerate(hc):
                val = Cm[I, J] / (w[I] * w[J])
                for (aa, bb) in {(a, b), (b, a)}:
                    for (cc, ddd) in {(c, dd), (dd, c)}:
                        T[aa, bb, cc, ddd, e, f] = val
                        T[aa, bb, cc, ddd, f, e] = val
    return T.reshape(-1)


def eh_tensor(d, g0=None):
    """Linearised Einstein-Hilbert form  S = h_ab G^{(1)ab}[h]-type pairing in Fourier space
    for flat background metric g0 (default identity), as a rank-6 tensor (real).
    Uses   L = -(1/2) h^{ab} E_ab[h]  with the linearised Einstein operator
      E_ab = -(1/2)[ k^2 h_ab - k_a k^c h_cb - k_b k^c h_ca + k_a k_b h - g_ab (k^2 h - k^c k^d h_cd) ]
    Overall normalisation is irrelevant here; only the ray/form is used."""
    if g0 is None:
        g0 = np.eye(d)
    gi = np.linalg.inv(g0)
    hc = hcomps(d)

    def Smat(k):
        k_up = gi @ k
        k2 = k @ k_up
        out = np.zeros((len(hc), len(hc)))
        for J, (c, dd) in enumerate(hc):
            h = np.zeros((d, d))
            h[c, dd] = h[dd, c] = 1.0
            h_up = gi @ h @ gi                    # h^{ab}
            tr = np.trace(gi @ h)
            khk = k_up @ h @ k_up
            Eab = (k2 * h - np.outer(k, h @ k_up) - np.outer(h @ k_up, k) + np.outer(k, k) * tr
                   - g0 * (k2 * tr - khk))
            for I, (a, b) in enumerate(hc):
                hI = np.zeros((d, d))
                hI[a, b] = hI[b, a] = 1.0
                out[I, J] = 0.5 * np.sum((gi @ hI @ gi) * Eab)
        return 0.5 * (out + out.T)
    return matrix_symbol_to_tensor(Smat, d).real


def tt_dispersion(Tflat, d, nhat, tau=None, w2max=3.0, ngrid=1500):
    """omega^2/|k|^2 roots of the d-dim symbol continued to k_tau = i*omega (tau = last axis
    by default), using the 'all equations x spatial components' (temporal-gauge) matrix.
    Returns list of (omega^2/k^2, sign of omega, multiplicity, rel sigma_min)."""
    if tau is None:
        tau = d - 1
    T = Tflat.reshape((d,) * 6)
    hc = hcomps(d)
    sp_cols = [J for J, (a, b) in enumerate(hc) if a != tau and b != tau]
    w = [1.0 if a == b else 2.0 for a, b in hc]
    nh = np.asarray(nhat, float)
    nh = nh / np.linalg.norm(nh)
    spatial_axes = [i for i in range(d) if i != tau]

    def Mat(om):
        k = np.zeros(d, complex)
        for i, ax in enumerate(spatial_axes):
            k[ax] = nh[i]
        k[tau] = 1j * om
        Kt = np.einsum("abcdef,e,f->abcd", T, k, k)
        return np.array([[w[I] * w[J] * Kt[hc[I][0], hc[I][1], hc[J][0], hc[J][1]] for J in sp_cols]
                         for I in range(len(hc))])

    def f(om):
        s = np.linalg.svd(Mat(om), compute_uv=False)
        return s[-1] / s[0]

    roots = []
    for sgn in (+1, -1):
        grid = sgn * np.sqrt(np.linspace(0.02, w2max, ngrid))
        vals = np.array([f(x) for x in grid])
        for i in range(1, len(grid) - 1):
            if vals[i] <= vals[i - 1] and vals[i] <= vals[i + 1] and vals[i] < 5e-2:
                lo, hi = sorted((grid[i - 1], grid[i + 1]))
                gr = (np.sqrt(5) - 1) / 2
                for _ in range(120):
                    c1, c2 = hi - gr * (hi - lo), lo + gr * (hi - lo)
                    if f(c1) < f(c2):
                        hi = c2
                    else:
                        lo = c1
                om = 0.5 * (lo + hi)
                s = np.linalg.svd(Mat(om), compute_uv=False)
                mult = int((s / s[0] < 1e-7).sum())
                roots.append((om * om, sgn, mult, s[-1] / s[0]))
    return roots


def check_factory():
    state = {"PASS": 0, "FAIL": 0}

    def check(name, cond, detail=""):
        print(f"[{'PASS' if cond else 'FAIL'}] {name}")
        if detail:
            print(f"       {detail}")
        state["PASS" if cond else "FAIL"] += 1
        return bool(cond)
    return check, state
