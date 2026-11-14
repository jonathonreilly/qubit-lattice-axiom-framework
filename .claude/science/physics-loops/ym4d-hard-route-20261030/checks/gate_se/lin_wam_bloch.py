#!/usr/bin/env python3
"""Second-order linear (WAM) coefficient in infinite volume, by Bloch sections. See CRITERIA.md."""
import argparse, itertools, json, math, time
import numpy as np
from scipy.optimize import minimize

PAIRS = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]

class Bloch:
    def __init__(s, B):
        s.B = B
        c = np.arange(B) - (B - 1) / 2
        s.n = np.array(list(itertools.product(c, repeat=4)))   # aliases, centred

    def Dk(s, k):
        B = s.B
        den = B * np.sin(k / 2)
        return np.where(np.abs(den) < 1e-14, 1.0, np.sin(B * k / 2) / np.where(np.abs(den) < 1e-14, 1, den))

    def blocks(s, p):
        B = s.B
        k = (p[None, :] + 2 * np.pi * s.n) / B
        e = np.exp(1j * k) - 1
        lap = (np.abs(e) ** 2).sum(1)
        D = s.Dk(k)
        pd = D.prod(1)
        q = B * pd[:, None] * D * np.exp(1j * k * (B - 1) / 2)
        na = len(k)
        d = np.zeros((na, 6, 4), complex)
        for i, (m, n) in enumerate(PAIRS):
            ph = np.exp(-0.5j * (k[:, m] + k[:, n]))      # plaquette centre
            d[:, i, n] = ph * e[:, m]
            d[:, i, m] = -ph * e[:, n]
        return d, lap, q

    def Phi(s, p):
        d, lap, q = s.blocks(p)
        ep = np.exp(1j * p) - 1
        v = ep / np.linalg.norm(ep)
        U = np.linalg.svd(v.conj()[None, :])[2].conj().T[:, 1:]    # basis orthogonal to e'(p)
        Psi = np.einsum('nij,nj,jk->nik', d, np.conj(q) / lap[:, None], U).reshape(-1, 3)
        G = Psi.conj().T @ Psi
        lam, V = np.linalg.eigh(G)
        return Psi @ (V / np.sqrt(lam)) @ V.conj().T, d, lap

    def value(s, p, dirn, eps=1e-4):
        F, d, lap = s.Phi(p)
        Fp = s.Phi(p + eps * dirn)[0]
        Fm = s.Phi(p - eps * dirn)[0]
        A = (Fp @ (Fp.conj().T @ F) - Fm @ (Fm.conj().T @ F)) / (2 * eps)
        na = len(lap)
        X = A.reshape(na, 6, 3)
        Y = np.einsum('nij,njk->nik', d.conj().transpose(0, 2, 1), X)
        Pb = np.einsum('nij,njk->nik', d, Y) / lap[:, None, None]
        Z = Pb.reshape(-1, 3) - F @ (F.conj().T @ Pb.reshape(-1, 3))
        return float(np.linalg.svd(Z, compute_uv=False)[0] ** 2)

def scan(bl, dirn, g, seed):
    pts = 2 * np.pi * (np.arange(g) + 0.5) / g - np.pi
    best, arg = -1, None
    starts = [np.array([np.pi, 4.04, 0.0, 0.0]), np.array([np.pi, np.pi, -np.pi, -np.pi])]
    for p in starts:
        v = bl.value(p + 1e-3, dirn)
        if v > best:
            best, arg = v, p + 1e-3
    for p in itertools.product(pts, repeat=4):
        p = np.array(p)
        if np.abs(np.exp(1j * p) - 1).max() < 1e-9:
            continue
        v = bl.value(p, dirn)
        if v > best:
            best, arg = v, p
    res = minimize(lambda x: -bl.value(x, dirn), arg, method='Nelder-Mead',
                   options=dict(xatol=1e-3, fatol=1e-6, maxiter=500))
    return (-res.fun, res.x.tolist()) if -res.fun > best else (best, arg.tolist())

def rays(bl, dirn, seed, nr=40):
    rng = np.random.default_rng(seed)
    out = {}
    dirs = [rng.standard_normal(4) for _ in range(nr)] + [np.eye(4)[0], np.eye(4)[1], np.ones(4)]
    for r in (1.0, 0.3, 0.1, 0.03, 0.01):
        v = 0.0
        for u in dirs:
            p = r * u / np.linalg.norm(u)
            v = max(v, bl.value(p, dirn, eps=1e-3 * r))
        out[str(r)] = v
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--Bs', default='3,5,9')
    ap.add_argument('--g', type=int, default=8)
    ap.add_argument('--out', default='bloch.json')
    a = ap.parse_args()
    rec = []
    for B in [int(x) for x in a.Bs.split(',')]:
        bl = Bloch(B)
        g = a.g if B <= 3 else (6 if B <= 5 else 3)
        for name, dirn in (('e0', np.eye(4)[0]), ('diag', np.ones(4))):
            t0 = time.time()
            ray = rays(bl, dirn, 11, nr=40 if B <= 5 else 6)
            top, arg = scan(bl, dirn, g, 5)
            r = dict(B=B, dir=name, D_oo=top, argmax=arg, rays=ray, grid=g, secs=round(time.time() - t0, 1))
            rec.append(r); print(r, flush=True)
            json.dump(rec, open(a.out, 'w'), indent=1)

if __name__ == '__main__':
    main()
