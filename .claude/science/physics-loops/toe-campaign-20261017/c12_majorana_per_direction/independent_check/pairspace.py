"""Dressing-independent pair test: lambda over the ENTIRE affine space of
admissible (possibly flux-dressed) pair creators in an R-invariant window.

Admissible S (C8 rules): supported in window W (R-invariant);
  - anticommutes with B exactly at x, Rx;
  - commutes with every plaquette generator farther than distance 1 from x, Rx,
    and so does S^R;
  - S and S^R have the same syndrome on every generator.
Solutions form S0 * V0 (V0 = homogeneous solutions, a GF(2) space mod phase).
lambda(S0 N) = lambda(S0) F(N) with F(N1 N2) = F(N1) F(N2) c(N2, N1 N1^R)
(c = commutation sign).  Hence lambda is constant on the whole space iff
F(b_i) = +1 for a basis b_i and c(b_j, b_i b_i^R) = +1 for all i != j.
"""
import numpy as np
from mpd_core import mul, dag


def rref_solve(rows, rhs, nv):
    """rows: uint8 (m, nv); returns (particular or None, nullspace basis (k, nv))."""
    A = np.concatenate([rows, rhs[:, None]], 1).astype(np.uint8)
    m = A.shape[0]
    piv = []
    r = 0
    for c in range(nv):
        if r == m:
            break
        nz = np.flatnonzero(A[r:, c])
        if nz.size == 0:
            continue
        p = r + nz[0]
        if p != r:
            A[[r, p]] = A[[p, r]]
        rr = np.flatnonzero(A[:, c])
        rr = rr[rr != r]
        if rr.size:
            A[rr] ^= A[r]
        piv.append(c)
        r += 1
    if A[r:, -1].any():
        return None, None
    sol = np.zeros(nv, np.uint8)
    for i, c in enumerate(piv):
        sol[c] = A[i, -1]
    pivset = set(piv)
    free = [c for c in range(nv) if c not in pivset]
    basis = np.zeros((len(free), nv), np.uint8)
    P = A[:r, :nv]
    for j, f in enumerate(free):
        basis[j, f] = 1
        col = P[:, f]
        for i in np.flatnonzero(col):
            basis[j, piv[i]] = 1
    return sol, basis


def vec_to_pauli(vec, W):
    nw = len(W)
    x = z = 0
    for j in np.flatnonzero(vec[:nw]):
        x |= 1 << W[j]
    for j in np.flatnonzero(vec[nw:]):
        z |= 1 << W[j]
    k = (x & z).bit_count() % 4
    return (x, z, k)


def pauli_to_vec(P, W):
    nw = len(W)
    v = np.zeros(2 * nw, np.uint8)
    for j, q in enumerate(W):
        v[j] = (P[0] >> q) & 1
        v[nw + j] = (P[1] >> q) & 1
    return v


def comm_row(Q, W):
    """row r with r . s = commutation parity of S (window vector s) with Q."""
    nw = len(W)
    r = np.zeros(2 * nw, np.uint8)
    for j, q in enumerate(W):
        r[j] = (Q[1] >> q) & 1       # S_x * Q_z
        r[nw + j] = (Q[0] >> q) & 1  # S_z * Q_x
    return r


def analyse(W, gens, near, Bflip, rot, tab):
    """gens: list of (label, Pauli) touching W; near(label)->bool for plaquettes;
    Bflip(label)->0/1 for B rows; rot(P) = image of Pauli under R (exact);
    tab: signed-group tableau.  Returns dict."""
    nw = len(W)
    rows, rhs = [], []
    for lab, g in gens:
        rg = comm_row(g, W)
        if not rg.any() and not comm_row(rot(g), W).any():
            continue
        if lab[0] == "B":
            rows.append(rg); rhs.append(Bflip(lab))
            continue
        rRg = comm_row(rot(g), W)       # chi_S(R^-1 g) for an involution R
        if near(lab):
            rows.append(rg ^ rRg); rhs.append(0)
        else:
            rows.append(rg); rhs.append(0)
            rows.append(rRg); rhs.append(0)
    rows = np.array(rows, np.uint8)
    rhs = np.array(rhs, np.uint8)
    sol, basis = rref_solve(rows, rhs, 2 * nw)
    if sol is None:
        return {"status": "no solution"}
    S0 = vec_to_pauli(sol, W)
    lam0 = tab.sign_of(mul(dag(S0), rot(S0)))
    F = []
    for b in basis:
        N = vec_to_pauli(b, W)
        S = mul(S0, N)
        lam = tab.sign_of(mul(dag(S), rot(S)))
        F.append(lam * lam0 if lam in (1, -1) else 0)
    # bilinear form K_ij = c(b_j, b_i b_i^R)
    Wset = {q: j for j, q in enumerate(W)}
    Rb = np.array([pauli_to_vec(rot(vec_to_pauli(b, W)), W) for b in basis], np.uint8) if len(basis) else basis
    Wv = basis ^ Rb
    Ux, Uz = basis[:, :nw].astype(np.int64), basis[:, nw:].astype(np.int64)
    Wx, Wz = Wv[:, :nw].astype(np.int64), Wv[:, nw:].astype(np.int64)
    K = (Wz @ Ux.T + Wx @ Uz.T) % 2      # K[i, j] = c(b_j, w_i)
    np.fill_diagonal(K, 0)
    return {"status": "ok", "lam0": lam0, "dim": len(basis), "F": F,
            "Fbad": sum(1 for f in F if f != 1), "Kbad": int(K.sum()),
            "constant": all(f == 1 for f in F) and not K.any(), "S0": S0}
