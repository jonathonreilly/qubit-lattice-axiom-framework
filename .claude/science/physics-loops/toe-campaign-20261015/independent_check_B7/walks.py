"""Shared walk machinery: class sign data, covariant subspaces, symbols."""
import itertools, json, numpy as np
from common import *

cl = json.load(open("classes.json"))
OFFS = [np.array(n) for n in itertools.product([-1, 0, 1], repeat=3)]
OIDX = {tuple(n): i for i, n in enumerate(OFFS)}
INV = np.zeros((8, 8))
for v in corners: INV[idx(1 - v), idx(v)] = 1

def class_D(ci):
    """dict rotkey -> D(R) (8x8 int), one lift per rotation"""
    sa, sb = np.array(cl[ci]["sa"]), np.array(cl[ci]["sb"])
    Da = Pmat(A_q).astype(int) @ np.diag(sa); Db = Pmat(B_t).astype(int) @ np.diag(sb)
    G = gen_group([Da, Db], 48)
    pk = {Pmat(R).astype(np.int8).tobytes(): rkey(R) for R in ROTS}
    D = {}
    for g in G:
        k = pk[perm_part(g).astype(np.int8).tobytes()]
        D.setdefault(k, g)
    return D

def commutant_basis(Dlist):
    """basis of 8x8 complex matrices commuting with all D in Dlist"""
    rows = []
    I = np.eye(8)
    for D in Dlist:
        rows.append(np.kron(D, I) - np.kron(I, D.T))  # vec(D X - X D) row-major
    Mx = np.vstack(rows)
    u, s, vh = np.linalg.svd(Mx)
    null = vh[np.sum(s > 1e-9):]
    return [x.reshape(8, 8) for x in null]

def covariant_basis(D, support=None):
    """orthonormal basis (real coefficient space suffices: constraints are real) of tuples
    (A_n) with A_{Rn} = D(R) A_n D(R)^T, via the Reynolds projector. support: optional
    boolean mask (27,8,8), assumed symmetry-invariant (checked)."""
    N = 27 * 64
    P = np.zeros((N, N))
    for R in ROTS:
        DR = D[rkey(R)].astype(float)
        K = np.kron(DR, DR)
        for n in OFFS:
            i, j = OIDX[tuple(n)], OIDX[tuple(R @ n)]
            P[j * 64:(j + 1) * 64, i * 64:(i + 1) * 64] += K
    P /= 24
    assert np.allclose(P @ P, P)
    if support is not None:
        m = support.reshape(-1)
        assert np.allclose(P[~m][:, m], 0) and np.allclose(P[m][:, ~m], 0)
        P = P * np.outer(m, m)
    w, V = np.linalg.eigh((P + P.T) / 2)
    return V[:, w > 0.5].T.reshape(-1, 27, 8, 8)

def symbol(A, k):
    W = np.zeros((8, 8), complex)
    for i, n in enumerate(OFFS):
        W += A[i] * np.exp(1j * np.dot(k, n))
    return W

def unitarity_defect(A):
    """max_d || sum_n A_n^dag A_{n+d} - delta_{d0} I ||, and same for A A^dag"""
    err = 0
    for d in itertools.product(range(-2, 3), repeat=3):
        d = np.array(d)
        S1 = np.zeros((8, 8), complex); S2 = np.zeros((8, 8), complex)
        for i, n in enumerate(OFFS):
            j = OIDX.get(tuple(n + d))
            if j is not None:
                S1 += A[i].conj().T @ A[j]
                S2 += A[j] @ A[i].conj().T
        if not d.any():
            S1 -= np.eye(8); S2 -= np.eye(8)
        err = max(err, np.abs(S1).max(), np.abs(S2).max())
    return err

def covariance_defect(A, D):
    err = 0
    for R in ROTS:
        DR = D[rkey(R)]
        for i, n in enumerate(OFFS):
            err = max(err, np.abs(A[OIDX[tuple(R @ n)]] - DR @ A[i] @ DR.T).max())
    return err

def two_layer(uA, uBt):
    """W(k) = G(k) uBt G(k)^dag uA with G = diag(e^{ik.v}); returns offsets A_n.
    uBt = INV uB INV is the shifted-block unitary written in original corner labels."""
    A = np.zeros((27, 8, 8), complex)
    for vo in corners:
        for vi in corners:
            n = vo - vi
            A[OIDX[tuple(n)], idx(vo), :] += uBt[idx(vo), idx(vi)] * uA[idx(vi), :]
    return A

def nn_support():
    """mask of entries allowed by nearest-site hops"""
    S = np.zeros((27, 8, 8), bool)
    for i, n in enumerate(OFFS):
        for vo in corners:
            for vi in corners:
                d = vo - vi - 2 * n
                S[i, idx(vo), idx(vi)] = np.all(np.abs(d) <= 1)
    return S

def site_disp_max(A, tol=1e-10):
    m = 0
    for i, n in enumerate(OFFS):
        for vo in corners:
            for vi in corners:
                if abs(A[i, idx(vo), idx(vi)]) > tol:
                    m = max(m, np.abs(vo - vi - 2 * n).max())
    return m
