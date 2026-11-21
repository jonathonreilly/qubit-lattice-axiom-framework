#!/usr/bin/env python3
"""GUIDE spectroscopy (row 918): lowest even (0++ glueball) and odd (torelon) levels of the box b^3.
Usage: spec.py T b beta nth nmeas seed nsmear [free(0/1) b2 b3]
free=1: free spatial walls (box b x b2 x b3); smearing staples and plaquettes weighted by the coefficient field
(0 across a wall); no torelon channel.
Periodic T x b^3 torus. APE smearing of spatial links within each time slice (alpha = 0.5, nsmear steps, exact
SU(2) projection by quaternion normalization). Zero-momentum slice operators:
  O_g(tau) = sum over x and spatial planes of x_p (smeared), vacuum-subtracted  (centre-even; glueball channel)
  O_i(tau) = sum over the transverse plane of tr/2 of the smeared spatial Polyakov loop in direction i  (odd under C_i)
Prints correlators C(d) = <O(tau) O(tau+d)> averaged over tau (and over i for the torelon), d = 0..T/2, with binned
errors, and effective energies log C(d)/C(d+1) (jackknife).
"""
import sys, json, time
import numpy as np
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from su2lat import Lattice, qmul, qconj, binned_err

T, b = int(sys.argv[1]), int(sys.argv[2]); beta = float(sys.argv[3])
nth, nme, seed, nsm = (int(x) for x in sys.argv[4:8])
free = len(sys.argv) > 8 and sys.argv[8] == '1'
bb = (b, int(sys.argv[9]), int(sys.argv[10])) if free else (b, b, b)
lat = Lattice((T,) + bb, beta, seed, free=(False, free, free, free))
from su2lat import pl_index
Cw = lat.C
fwd, bwd = lat.fwd, lat.bwd

def smear(U):
    S = U.copy()
    for _ in range(nsm):
        new = S.copy()
        for i in (1, 2, 3):
            st = np.zeros_like(S[i])
            for j in (1, 2, 3):
                if j == i: continue
                kk = pl_index(i, j); bj = bwd[j]
                st += Cw[kk][:, None] * qmul(qmul(S[j], S[i][fwd[j]]), qconj(S[j][fwd[i]]))
                st += Cw[kk][bj][:, None] * qmul(qmul(qconj(S[j][bj]), S[i][bj]), S[j][fwd[i][bj]])
            v = 0.5*S[i] + 0.5/4*st
            new[i] = v/np.sqrt((v*v).sum(axis=1))[:, None]
        S = new
    return S

tau = lat.coords[0]
for _ in range(nth): lat.sweep(3)
Og, Ot = [], []
T0 = time.time()
for m in range(nme):
    lat.sweep(3); lat.sweep(3)
    S = smear(lat.U)
    g = np.zeros(T)
    for (i, j) in ((1, 2), (1, 3), (2, 3)):
        p = qmul(qmul(S[i], S[j][fwd[i]]), qmul(qconj(S[i][fwd[j]]), qconj(S[j])))[:, 0]
        g += np.bincount(tau, weights=p*Cw[pl_index(i, j)], minlength=T)
    Og.append(g)
    if free:
        Ot.append(np.zeros((3, T))); continue
    tor = []
    for i in (1, 2, 3):
        start = np.nonzero(lat.coords[i] == 0)[0]
        P = S[i][start].copy(); cur = fwd[i][start]
        for _ in range(b - 1):
            P = qmul(P, S[i][cur]); cur = fwd[i][cur]
        tor.append(np.bincount(tau[start], weights=P[:, 0], minlength=T))
    Ot.append(np.array(tor))
Og = np.array(Og); Ot = np.array(Ot)   # (n, T), (n, 3, T)

def corr(O, sub):
    # O: (n, T) per configuration; returns per-config correlator estimates (n, T//2+1)
    X = O - sub
    return np.array([[np.mean(x*np.roll(x, -d)) for d in range(T//2+1)] for x in X])

def jk_eff(Cs):
    n = len(Cs); nb = 20; m = n//nb
    blocks = [np.delete(Cs, np.s_[k*m:(k+1)*m], axis=0).mean(axis=0) for k in range(nb)]
    full = Cs.mean(axis=0)
    def eff(c):
        with np.errstate(all='ignore'): return np.log(c[:-1]/c[1:])
    e = eff(full); eb = np.array([eff(c) for c in blocks])
    err = np.sqrt((nb-1)*np.nanvar(eb, axis=0))
    return e, err

Cg = corr(Og, Og.mean())
Ct = np.mean([corr(Ot[:, i, :], 0.0) for i in range(3)], axis=0)
eg, egerr = jk_eff(Cg); et, eterr = jk_eff(Ct)
print(json.dumps(dict(T=T, b=b, beta=beta, nmeas=nme, nsmear=nsm, sec=round(time.time()-T0, 1),
                      Cg=[float(x) for x in Cg.mean(0)], Cg_err=[float(x) for x in binned_err(Cg, 20)],
                      Ct=[float(x) for x in Ct.mean(0)], Ct_err=[float(x) for x in binned_err(Ct, 20)],
                      Eg_eff=[float(x) for x in eg], Eg_err=[float(x) for x in egerr],
                      Et_eff=[float(x) for x in et], Et_err=[float(x) for x in eterr])))
