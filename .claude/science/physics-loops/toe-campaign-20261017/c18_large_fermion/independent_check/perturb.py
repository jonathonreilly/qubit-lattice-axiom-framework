"""Helpers: O x T symmetrized second-neighbour hops (definitions only)."""
import numpy as np
from model import *
FD = dict(square=1, triangle=0, plaquette=1, tube=1)
u = solve_gauge(FD)
PS = [(R, *psg(u, R)) for R in ROTS]
PS = [(R, eta, s, (R @ s) % 2) for R, eta, s in PS]
Iv = -np.eye(3, dtype=int); etaI, sI = psg(u, Iv); WI = Wmat(Iv, etaI); SI = (Iv @ sI) % 2
KP = np.array([1, -1, 1]) * np.pi / 2
def paths2(c0):
    out = []
    for c1, sh1, k1 in neighbours(c0):
        for c2, sh2, k2 in neighbours(c1):
            sh = tuple(int(a + b) for a, b in zip(sh1, sh2))
            if c2 == c0 and sh == (0, 0, 0): continue
            g = (-1.0) ** (u[EKEY[(c0, c1, sh1)]] + u[EKEY[(c1, c2, sh2)]])
            out.append((c2, sh, g, (k1, k2)))
    return out
def Xbloch(hops, k):
    X = np.zeros((12, 12), complex)
    for c1, c2, sh, z in hops:
        X[c2, c1] += z * np.exp(-1j * np.asarray(k) @ np.array(sh))
    return X
def Xsym(hops, k):
    k = np.asarray(k, float); X = np.zeros((12, 12), complex)
    for R, eta, s, S in PS:
        W = Wmat(R, eta); kk = R.T @ (k - np.pi * S)
        X += W @ Xbloch(hops, kk) @ W.T
    return X + X.conj().T
def candidates(rng):
    cands = {}
    for c2, sh, g, kinds in paths2(0):
        cands.setdefault((kinds, c2, sh), []).append(g)
    res = []
    for (kinds, c2, sh), gs in sorted(cands.items(), key=lambda t: str(t[0])):
        for z, zn in ((1.0, '1'), (1j, 'i')):
            hops = [(0, c2, sh, z * gg) for gg in gs]
            ks = rng.uniform(-np.pi, np.pi, (4, 3))
            nrm = max(np.abs(Xsym(hops, k)).max() for k in ks)
            if nrm < 1e-9: continue
            ikb = max(np.abs(Xsym(hops, k + np.pi * SI) - WI @ Xsym(hops, k).conj() @ WI.T).max() for k in ks)
            res.append((kinds, c2, sh, zn, nrm, ikb, hops))
    return res
