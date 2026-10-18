"""B20 checker library.  Builds everything from B18_check/chk_model.py (a copy of the scale-ladder runner's
construction code: gauge, PSG lifts, H0, Bloch blocks, diagonal shift S, Lambda).  Does NOT use b20lib,
b18lib or walklib.  Adds: Bloch representations of the PSG operators (momentum action derived from the
operators themselves), the full on-site symmetric algebra (solved from real-space invariance), words,
finite-difference/Berry-flux node diagnostics."""
import os, sys, itertools
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'B18_check'))
from chk_model import *          # noqa
import numpy as np

GRIDK = [np.array(t) * np.pi / 2 for t in itertools.product(range(4), repeat=3)]   # L=4 momenta
def kred(k): return tuple(int(round(x)) % 4 for x in np.asarray(k) / (np.pi / 2))

_BL = {kred(k): Bloch(k) for k in GRIDK}
def op_bloch(P, s, k):
    """Return (k', U) with Op Bloch(k) = Bloch(k') U, for the signed permutation (P, s)."""
    O = opmat_from(P, s); X = O @ _BL[kred(k)]
    for kk in GRIDK:
        U = _BL[kred(kk)].conj().T @ X
        if abs(np.linalg.norm(U) ** 2 - 12) < 1e-8: return kk, U
    raise RuntimeError('no definite momentum')

# ---- on-site symmetric algebra: 12x12 blocks B with  O_r(B) invariant under every rotation and translation
def onsite_real(B):
    O = np.zeros((nV, nV), complex)
    for a, (v, c) in enumerate(VERTS):
        for b2, c2 in enumerate(CORN):
            j = C['VID'][(v, c2)]; O[a, j] = B[CI[c], b2]
    return O
def _onsite_constraints():
    rowsC = []
    site_idx = {}
    for a, (v, c) in enumerate(VERTS): site_idx.setdefault(v, {})[CI[c]] = a
    for P, s in rots + trans:
        sg = (-1.0) ** s
        # Y[P(a),P(b)] = O[a,b] sg_a sg_b must equal O[P(a),P(b)]  for a,b on one site
        for v, d in list(site_idx.items())[:8]:      # 8 sites suffice for the linear span; checked below on all
            for ci, a in d.items():
                for cj, b in d.items():
                    pa, pb = P[a], P[b]
                    va, ca = VERTS[pa]; vb, cb = VERTS[pb]
                    assert va == vb
                    r = np.zeros(144); r[CI[ca] * 12 + CI[cb]] += 1; r[ci * 12 + cj] -= sg[a] * sg[b]
                    rowsC.append(r)
    A = np.array(rowsC); G = A.T @ A
    w_, V_ = np.linalg.eigh(G)
    null = V_[:, w_ < 1e-9].T
    return [n.reshape(12, 12) for n in null]
    _, sv, Vh = np.linalg.svd(A)
    null = Vh[np.sum(sv > 1e-9):]
    return [n.reshape(12, 12) for n in null]
ONSITE_BASIS = _onsite_constraints()
def onsite_check(B):
    O = onsite_real(B)
    return all(np.allclose(conj(O, P, s), O) for P, s in rots + trans)

def rand_onsite_unitary(rng):
    H = sum(rng.normal() * (Bm + Bm.conj().T) / 2 + rng.normal() * 1j * (Bm - Bm.conj().T) / 2 for Bm in ONSITE_BASIS)
    H = (H + H.conj().T) / 2; w, V = np.linalg.eigh(H)
    return V @ np.diag(np.exp(1j * w * 3.0)) @ V.conj().T

# ---- letters
def Sk(k, p=1):
    d = np.diag(SKc(k)); return np.diag(d ** p) if p > 0 else np.diag(np.conj(d) ** (-p))
def letter(L, k):
    if isinstance(L, str):
        if L == 'R': return RLk(k)
        return Sk(k, {'S': 1, 'Si': -1, 'S2': 2, 'S2i': -2}[L])
    return L
def Wword(w, k):
    M = np.eye(12, dtype=complex)
    for L in w: M = M @ letter(L, np.asarray(k, float))
    return M
NSP = {'S': 1, 'Si': -1, 'S2': 2, 'S2i': -2, 'R': 0}
def nS(w): return sum(NSP[L] for L in w if isinstance(L, str))
def nR(w): return sum(1 for L in w if isinstance(L, str) and L == 'R')

def eigph(W): return np.angle(np.linalg.eigvals(W))
def levels(W, tol=1e-7):
    e = np.sort(np.mod(eigph(W), 2 * np.pi)); out = []; i = 0
    while i < 12:
        j = i
        while j < 12 and abs(e[j] - e[i]) < tol: j += 1
        out.append((float(np.angle(np.exp(1j * e[i]))), j - i)); i = j
    # merge wrap-around
    if len(out) > 1 and abs(wrap(out[0][0] - out[-1][0])) < tol:
        out[0] = (out[0][0], out[0][1] + out[-1][1]); out.pop()
    return out
def closest(W, E, m):
    e = eigph(W); return np.sort(wrap(e[np.argsort(np.abs(wrap(e - E)))[:m]] - E))

# ---- independent node diagnostics: finite-difference speeds along directions; Berry flux (own FHS)
def fd_speeds(w, k0, E, m=2, h=1e-5, ndir=26, rng=None):
    rng = rng or np.random.default_rng(1)
    dirs = [np.eye(3)[i] for i in range(3)] + [d / np.linalg.norm(d) for d in rng.normal(size=(ndir, 3))]
    out = []
    for d in dirs:
        a = closest(Wword(w, k0 + h * d), E, m); b = closest(Wword(w, k0 - h * d), E, m)
        out.append((a, b))
    return dirs, out
def berry_flux(w, k0, E, r=1e-3, n=20, band='below'):
    th = np.linspace(0, np.pi, n + 1); ph = np.linspace(0, 2 * np.pi, 2 * n, endpoint=False)
    U = np.zeros((n + 1, 2 * n, 12), complex)
    for i, t in enumerate(th):
        for j, p in enumerate(ph):
            k = k0 + r * np.array([np.sin(t) * np.cos(p), np.sin(t) * np.sin(p), np.cos(t)])
            e, v = np.linalg.eig(Wword(w, k)); a = wrap(np.angle(e) - E)
            idx = np.where(a < 0, a, -9).argmax() if band == 'below' else np.where(a > 0, a, 9).argmin()
            x = v[:, idx]; U[i, j] = x / np.linalg.norm(x)
    tot = 0.0
    for i in range(n):
        for j in range(2 * n):
            a, b, c, d = U[i, j], U[i + 1, j], U[i + 1, (j + 1) % (2 * n)], U[i, (j + 1) % (2 * n)]
            tot += np.angle(np.vdot(a, b) * np.vdot(b, c) * np.vdot(c, d) * np.vdot(d, a))
    return tot / (2 * np.pi)
