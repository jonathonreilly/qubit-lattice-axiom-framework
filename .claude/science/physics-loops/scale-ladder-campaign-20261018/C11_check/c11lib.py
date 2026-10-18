"""Checker letters, analytic derivatives, path bookkeeping by subspace tracking, direct diagonalisation, Berry flux."""
import itertools
import numpy as np
from scipy.linalg import schur, expm
from c11model import *

TAU = {}
_t = np.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tau_frames.npy'))
TAU[1], TAU[-1] = _t[0], _t[1]

class Letter:
    """f(k) -> 12x12 unitary; df(k) -> list of 3 analytic derivatives; chi = +-1 declared."""
    def __init__(self, name, chi, f, df): self.name, self.chi, self.f, self.df = name, chi, f, df

def expiH_and_d(Hk, dHk):
    w, V = np.linalg.eigh(Hk); e = np.exp(1j * w)
    dw = w[:, None] - w[None, :]
    with np.errstate(divide='ignore', invalid='ignore'):
        G = np.where(np.abs(dw) > 1e-10, (e[:, None] - e[None, :]) / np.where(np.abs(dw) > 1e-10, dw, 1), 1j * e[:, None] * np.ones_like(dw))
    U = (V * e) @ V.conj().T
    return U, [V @ ((V.conj().T @ dH @ V) * G) @ V.conj().T for dH in dHk]

def L_S(p): return Letter(f"S^{p}", 1, lambda k, p=p: Sk(k, p), lambda k, p=p: dSk(k, p))
def L_AS(p): return Letter(f"A0S^{p}", -1, lambda k, p=p: A0 @ Sk(k, p), lambda k, p=p: [A0 @ d for d in dSk(k, p)])
def L_block(name, X): return Letter(name, 1, lambda k, X=X: bl(X, k), lambda k, X=X: bl_d(X, k))
def L_expX(name, X, theta=1.0, chi=1, pre=None):
    def f(k):
        U, _ = expiH_and_d(theta * bl(X, k), [np.zeros((12, 12))] * 3); return U if pre is None else pre @ U
    def df(k):
        _, d = expiH_and_d(theta * bl(X, k), [theta * D for D in bl_d(X, k)]); return d if pre is None else [pre @ x for x in d]
    return Letter(name, chi, f, df)
def L_const(name, M, chi=1): return Letter(name, chi, lambda k, M=M: M, lambda k: [np.zeros((12, 12), complex)] * 3)
L_RL = L_block("R_L", RLX); L_RT = L_block("Rt", RTX)
def L_onsite(rng):
    H = sym_onsite(rng); H = (H + H.conj().T) / 2; H = H / np.linalg.norm(H, 2) * rng.uniform(0.5, 3)
    return L_const("onsite", expm(1j * H))
def rand_H(rng, rmax=2):
    X = {}
    for a in itertools.product(range(-rmax, rmax + 1), repeat=3):
        if sum(map(abs, a)) <= rmax and rng.random() < 0.6:
            X[a] = rng.normal(size=(12, 12)) + 1j * rng.normal(size=(12, 12))
    X = avg(X); Xd = dagx(X); H = {}
    for a in set(X) | set(Xd): H[a] = (X.get(a, 0) + Xd.get(a, 0)) / 2
    nrm = max(np.linalg.norm(bl(H, rng.uniform(-np.pi, np.pi, 3)), 2) for _ in range(3))
    return {a: B / nrm for a, B in H.items()}
def L_gen(rng, a2=False, scale=None):
    H = rand_H(rng); s = rng.uniform(0.3, 3.0) if scale is None else scale
    return L_expX("A0exp(iH)" if a2 else "exp(iH)", H, s, chi=-1 if a2 else 1, pre=A0 if a2 else None), H, s

def covariant(L, rng, nk=2):
    for _ in range(nk):
        k = rng.uniform(-np.pi, np.pi, 3); U = L.f(k)
        for g in GRP:
            c = g['chi'] if L.chi == -1 else 1
            if not np.allclose(g['U'] @ L.f(g['M'].T @ k + np.pi * g['lam']) @ g['U'].T, c * U, atol=1e-9): return False
    return True

def label_of(B):
    """which doublet the 2-dim isometry B spans (by projector weight), or None"""
    wp = np.linalg.norm(DP.conj().T @ B) ** 2 / 2; wm = np.linalg.norm(DM.conj().T @ B) ** 2 / 2
    if abs(wp - 1) < 1e-8: return +1
    if abs(wm - 1) < 1e-8: return -1
    return None

def fit_v(M, b):
    """M = list of three 2x2 matrices in D_b's basis; fit M_i = i v tau^(b)_i by least squares; return v (complex), residual"""
    A = np.concatenate([(1j * TAU[b][i]).flatten() for i in range(3)]); y = np.concatenate([M[i].flatten() for i in range(3)])
    v = np.vdot(A, y) / np.vdot(A, A)
    return v, np.abs(y - v * A).max()

def letter_v(L, k0, b):
    D = DOUB[b]; U = L.f(k0); dU = L.df(k0)
    M = [D.conj().T @ U.conj().T @ dU[i] @ D for i in range(3)]
    return fit_v(M, b)

def word_eval(w, k):
    X = np.eye(12, dtype=complex)
    for L in w: X = X @ L.f(k)
    return X

def path_terms(w, k0, a):
    """track the input doublet D_a from the right through the word; returns list of (label_in, B_j^dag U_j^dag dU_j B_j)"""
    B = DOUB[a].copy(); out = []
    for L in reversed(w):
        lab = label_of(B)
        U = L.f(k0); dU = L.df(k0)
        T = [B.conj().T @ U.conj().T @ dU[i] @ B for i in range(3)]
        out.append((lab, L, T, B.copy()))
        B = U @ B
    return out[::-1], label_of(B)

def eig_unitary(W):
    T, Z = schur(W, output='complex'); return np.diag(T), Z

def direct_speed(w, k0, w0, q, delta=1e-4):
    """half splitting of the two eigenphases nearest w0 of W(k0 + delta q), Richardson (delta, delta/2); also mean shift/delta
    (the mean shift contains an O(delta) scalar second-order term; the caller antisymmetrises in q to get the tilt)"""
    res = []
    for dl in (delta, delta / 2):
        ev = np.linalg.eigvals(word_eval(w, k0 + dl * q)); ph = np.angle(ev / w0); idx = np.argsort(np.abs(ph))[:2]
        p = np.sort(ph[idx]); res.append(((p[1] - p[0]) / 2 / dl, (p[1] + p[0]) / 2 / dl))
    return (4 * res[1][0] - res[0][0]) / 3, (4 * res[1][1] - res[0][1]) / 3

def sphere_chern(Wfun, k0, w0, nb_sel, r, nth=20, nph=40):
    """Berry flux through a sphere of radius r about k0 for groups of bands among the n eigenvalues nearest w0,
    ordered by phase relative to w0.  nb_sel: list of tuples of band indices (0 = lowest phase).  Returns list of Chern numbers.
    Outward orientation: (theta, phi) with e_theta x e_phi = e_r."""
    nsel = max(max(s) for s in nb_sel) + 1
    th = np.linspace(0, np.pi, nth + 1); ph = np.linspace(0, 2 * np.pi, nph + 1)[:-1]
    vecs = {}
    def at(i, j):
        if i == 0: j = 0
        if i == nth: j = 0
        if (i, j) in vecs: return vecs[(i, j)]
        n = np.array([np.sin(th[i]) * np.cos(ph[j]), np.sin(th[i]) * np.sin(ph[j]), np.cos(th[i])])
        ev, Z = eig_unitary(Wfun(k0 + r * n)); rel = np.angle(ev / w0)
        idx = np.argsort(np.abs(rel))[:nsel]; idx = idx[np.argsort(rel[idx])]
        vecs[(i, j)] = (Z[:, idx], rel[idx]); return vecs[(i, j)]
    out = []
    gapmin = np.inf
    for sel in nb_sel:
        F = 0.0
        for i in range(nth):
            for j in range(nph):
                corners = [at(i, j), at(i + 1, j), at(i + 1, (j + 1) % nph), at(i, (j + 1) % nph)]
                V = [c[0][:, list(sel)] for c in corners]
                prod = 1.0 + 0j
                for m in range(4):
                    prod *= np.linalg.det(V[m].conj().T @ V[(m + 1) % 4])
                F += np.angle(prod)
        out.append(F / (2 * np.pi))
    for c in vecs.values():
        gapmin = min(gapmin, np.min(np.diff(c[1])))
    return out, gapmin
