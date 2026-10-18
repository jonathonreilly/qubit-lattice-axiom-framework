import sys, itertools, numpy as np
sys.path.insert(0, '.')
import regge_generic as RG
from d4m import C, HC, eidx
pairs = list(itertools.combinations(range(4), 2))
OFFS = C.OFF
def hole_type(pos2):        # pos = integer + (e_m+e_n)/2 ; returns (b, type)
    p = np.asarray(pos2, float)
    for h, (m, n) in enumerate(pairs):
        q = p - OFFS[2+h]
        if np.allclose(q, np.round(q)): return (tuple(int(x) for x in np.round(q)), 2+h)
    raise ValueError
def Lsym(k):
    k = np.asarray(k, complex); Lm = np.zeros((10, C.E), complex); E = np.eye(4, dtype=int)
    def add(row, v1, v2, coef):
        c, anc = eidx(v1, v2); Lm[row, c] += coef*np.exp(1j*k @ anc)
    for mu in range(4): add(HC.index((mu, mu)), ((0,0,0,0), 0), (tuple(E[mu]), 0), 2.0)
    for (m, n) in pairs:
        row = HC.index((m, n))
        # + diagonal: 0 -> e_m+e_n through hole (e_m+e_n)/2 : 2 h_mn = 2 sqrt2 dl - h_mm - h_nn
        hp = hole_type(0.5*(E[m]+E[n]))
        add(row, ((0,0,0,0), 0), hp, np.sqrt(2)/2); add(row, hp, (tuple(E[m]+E[n]), 0), np.sqrt(2)/2)
        add(row, ((0,0,0,0), 0), (tuple(E[m]), 0), -0.5); add(row, ((0,0,0,0), 0), (tuple(E[n]), 0), -0.5)
        # - diagonal: e_n -> e_m through hole (e_m+e_n)/2 : -2 h_mn = 2 sqrt2 dl - h_mm - h_nn
        add(row, (tuple(E[n]), 0), hp, -np.sqrt(2)/2); add(row, hp, (tuple(E[m]), 0), -np.sqrt(2)/2)
        add(row, ((0,0,0,0), 0), (tuple(E[m]), 0), +0.5); add(row, ((0,0,0,0), 0), (tuple(E[n]), 0), +0.5)
    return Lm
G = C.gauge(np.array([0.3, -0.2, 0.1, 0.25])); print("|Lsym G_nonsite| =", np.abs(Lsym(np.array([0.3, -0.2, 0.1, 0.25])) @ np.hstack([G[:, 4*t:4*t+4] for t in range(1, 8)])).max(), " |Lsym M(0) - 1| =", np.abs(Lsym(np.zeros(4)) @ C.line_map(np.zeros(4)) - np.eye(10)).max())
itt = HC.index((3, 3))
for kk in [np.array([0.012, -0.009, 0.013, 0.0]), np.array([0.02, 0, 0, 0.0]), np.array([0.01, 0.01, 0.01, 0.0])]:
    Q = C.Q(kk); w, V = np.linalg.eigh(0.5*(Q + Q.conj().T)); V = V[:, np.argsort(np.abs(w))]
    M = C.line_map(kk); Gk = C.gauge(kk); A = np.hstack([M, Gk]); P = np.eye(C.E) - A @ np.linalg.pinv(A, rcond=1e-10)
    partners = np.linalg.svd(P @ V[:, 32:40])[0][:, :2]
    Lk = Lsym(kk); T = np.zeros(10); T[itt] = 1.0; J = Lk.conj().T @ T
    x = np.linalg.pinv(Q, rcond=1e-11) @ J; xp = partners @ (partners.conj().T @ x); k2 = np.dot(kk, kk)
    print(f"k={kk}: h_tt k^2 total {np.real((Lk@x)[itt])*k2:+.4f}; partner {np.real((Lk@xp)[itt])*k2:+.4f}; |Lsym partners| {np.round(np.linalg.norm(Lk@partners, axis=0),4)}")
