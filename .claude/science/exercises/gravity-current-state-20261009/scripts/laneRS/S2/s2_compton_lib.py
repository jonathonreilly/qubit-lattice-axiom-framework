"""Compton amplitude and sampler (extracted from s2_compton.py, parametrised by S and rng)."""
import numpy as np
from s2_core import *
def compton_T(S, k, p, kq, pq):
    m, d = S.m, S.d
    U, Uq = S.Uplus(k), S.Uplus(kq); E = eps(k, m)
    Ep, Eq = transverse(p, d), transverse(pq, d)
    ks, ku = wrapr(k + p), wrapr(k - pq)
    Rs = np.linalg.inv((E + omega(p))*np.eye(S.nn) - S.h(ks))
    Ru = np.linalg.inv((E - omega(pq))*np.eye(S.nn) - S.h(ku))
    npl = U.shape[1]; npol = Ep.shape[1]
    T = np.zeros((npl*npol, npl*npol), complex)
    for l in range(npol):
        Va_s = sum(Ep[i, l]*S.vert(k, p, ks, i) for i in range(d)); Va_u = sum(Ep[i, l]*S.vert(ku, p, kq, i) for i in range(d))
        for lq in range(npol):
            Ve_s = sum(Eq[j, lq]*S.vert(ks, -pq, kq, j) for j in range(d)); Ve_u = sum(Eq[j, lq]*S.vert(k, -pq, ku, j) for j in range(d))
            SG = -sum(Ep[i, l]*Eq[i, lq]*S.seag(k, p - pq, kq, i) for i in range(d))
            M = Uq.conj().T @ (Ve_s @ Rs @ Va_s + Va_u @ Ru @ Ve_u + SG) @ U
            for a in range(npl):
                for c in range(npl):
                    T[a*npol + lq, c*npol + l] = M[a, c]
    return T/np.sqrt(4*omega(p)*omega(pq))
def sample_compton(S, nsamp, mode, rng):
    m, d = S.m, S.d
    out = []; g = np.linspace(-np.pi, np.pi, 1601); tries = 0
    while len(out) < nsamp and tries < nsamp*300:
        tries += 1
        if mode == 'low':
            k = wrapr(rng.normal(0, 0.4, d)); p = wrapf(rng.normal(0, 0.6, d)); p0 = wrapf(rng.normal(0, 0.6, d))
        else:
            k = rng.uniform(-np.pi/2, np.pi/2, d); p = rng.uniform(-np.pi, np.pi, d); p0 = rng.uniform(-np.pi, np.pi, d)
        if omega(p) < 0.05: continue
        Etot = eps(k, m) + omega(p); ax = rng.integers(d)
        P = np.tile(p0, (len(g), 1)); P[:, ax] = g
        fv = eps(wrapr(k + p - P), m) + omega(P) - Etot
        idx = np.nonzero(np.sign(fv[:-1])*np.sign(fv[1:]) < 0)[0]
        for ii in idx:
            a, b = g[ii], g[ii+1]
            def F(t):
                x = p0.copy(); x[ax] = t; return eps(wrapr(k + p - x), m) + omega(x) - Etot
            fa = F(a)
            for _ in range(70):
                c = 0.5*(a+b); fc = F(c)
                if np.sign(fa)*np.sign(fc) <= 0: b = c
                else: a, fa = c, fc
            pq = p0.copy(); pq[ax] = 0.5*(a+b); pq = wrapf(pq)
            if np.max(np.abs(wrapf(pq - p))) < 1e-3 or omega(pq) < 0.05: continue
            kq = wrapr(k + p - pq)
            out.append((k, p, kq, pq))
            if len(out) >= nsamp: break
    return out
