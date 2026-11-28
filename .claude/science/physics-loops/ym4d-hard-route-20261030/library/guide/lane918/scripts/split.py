#!/usr/bin/env python3
"""GUIDE (row 918): Delta(a; B) = 2 g(a; B) - g(2a; B) by interpolating the time gluing (cut and reglue).
Usage: split.py a b1 b2 b3 beta free(0/1) ns nth nmeas seed
Lattice of 2a time slices (a even). Geometry L ('long'): one torus of period 2a. Geometry P ('pair'): the links
U_0 of slices a-1 and 2a-1 point to slices 0 and a, which makes two tori of period a. The temporal plaquettes with
base slice a-1 or 2a-1 (the gluing plaquettes) carry weight s in geometry L and 1-s in geometry P; all other
plaquettes are those of L (identical in P). Weight exp(beta [sum_L c x^L + sum_P c' x^P]); both staples add.
d log Z_s/ds = beta <X>_s, X = sum over gluing plaquettes of (x^L - x^P). Z_1 = Z(2a; B), Z_0 = Z(a; B)^2, so
  g(2a) - 2 g(a) = beta int_0^1 <X>_s ds,  Delta(a) = -beta int_0^1 <X>_s ds   (lambda_0 factors cancel exactly).
Gauss-Legendre in s. Updates: the heat bath and overrelaxation of su2lat with the summed staple; classes of the
2a-periodic lattice are proper for both geometries when a is even (time parity is preserved by both maps).
"""
import sys, json, time
import numpy as np
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from su2lat import Lattice, binned_err, pl_index, qmul, qconj

a, b1, b2, b3 = (int(x) for x in sys.argv[1:5]); beta = float(sys.argv[5]); free = sys.argv[6] == '1'
ns, nth, nme, seed = (int(x) for x in sys.argv[7:11])
assert a % 2 == 0
fr = (False, free, free, free)
L = Lattice((2*a, b1, b2, b3), beta, seed, free=fr)
P = Lattice((2*a, b1, b2, b3), beta, seed + 1, free=fr)
P.U = L.U   # shared links
t0 = L.coords[0]
lin = np.arange(L.V)
f0 = L.fwd[0].copy(); b0 = L.bwd[0].copy()
up = (t0 == a-1) | (t0 == 2*a-1)
f0[up] = lin[up] - (a-1) * np.prod((b1, b2, b3))  # slice a-1 -> 0, slice 2a-1 -> a (row-major, time is axis 0)
dn = (t0 == 0) | (t0 == a)
b0[dn] = lin[dn] + (a-1) * np.prod((b1, b2, b3))
P.fwd[0] = f0; P.bwd[0] = b0
assert np.all(L.coords[0][f0[up]] == np.where(t0[up] == a-1, 0, a))
glue = []   # (plane index, base sites) of gluing plaquettes
Cfree = L.C.copy()
for i in (1, 2, 3):
    k = pl_index(0, i)
    sites = np.nonzero(up & (Cfree[k] != 0))[0]
    glue.append((k, sites))
P.C[:] = 0.0

def set_s(s):
    for k, sites in glue:
        L.C[k, sites] = s * Cfree[k, sites]
        P.C[k, sites] = (1 - s) * Cfree[k, sites]
    L.refresh(); P.refresh()

def staple(mu, ci):
    idx, tL = L.plan[mu][ci]; idx2, tP = P.plan[mu][ci]
    return idx, L.staple(mu, idx, tL) + P.staple(mu, idx, tP)

def sweep():
    for mu in range(4):
        for ci in range(len(L.plan[mu])):
            idx, A = staple(mu, ci)
            k = np.sqrt((A*A).sum(axis=1))
            h = L._h1(beta*k)
            v = L.rng.normal(size=(idx.size, 3)); v /= np.sqrt((v*v).sum(axis=1))[:, None]
            w = np.empty((idx.size, 4)); w[:, 0] = h; w[:, 1:] = np.sqrt(np.clip(1-h*h, 0, 1))[:, None]*v
            new = qmul(w, qconj(A)/np.maximum(k, 1e-300)[:, None])
            z = k < 1e-12
            if np.any(z):
                g = L.rng.normal(size=(int(z.sum()), 4)); g /= np.sqrt((g*g).sum(axis=1))[:, None]; new[z] = g
            L.U[mu][idx] = new
    for _ in range(3):
        for mu in range(4):
            for ci in range(len(L.plan[mu])):
                idx, A = staple(mu, ci)
                k = np.sqrt((A*A).sum(axis=1)); ok = k > 1e-12
                Vd = qconj(A[ok]/k[ok][:, None])
                L.U[mu][idx[ok]] = qmul(qmul(Vd, qconj(L.U[mu][idx[ok]])), Vd)
    for mu in range(4):
        n = np.sqrt((L.U[mu]**2).sum(axis=1)); L.U[mu] /= n[:, None]

def X():
    xL = L.plaquettes(); xP = P.plaquettes()
    return sum((xL[k, s] - xP[k, s]).sum() for k, s in glue)

xg, wg = np.polynomial.legendre.leggauss(ns); sg = 0.5*(xg + 1); wg = 0.5*wg
T0 = time.time(); means = []; errs = []
for si, s in enumerate(sg[::-1]):
    set_s(s)
    for _ in range(nth if si > 0 else 3*nth): sweep()
    xs = []
    for _ in range(nme):
        sweep(); xs.append(X())
    means.append(np.mean(xs)); errs.append(binned_err(xs))
    print(json.dumps(dict(s=float(s), X=float(means[-1]), dX=float(errs[-1]), sec=round(time.time()-T0, 1))), flush=True)
means = np.array(means[::-1]); errs = np.array(errs[::-1])
D = -beta*(wg*means).sum(); dD = beta*np.sqrt(((wg*errs)**2).sum())
print(json.dumps(dict(a=a, B=[b1, b2, b3], beta=beta, free=free, ns=ns, nmeas=nme, nglue=int(sum(s.size for _, s in glue)),
                      Delta=float(D), dDelta=float(dD), sec=round(time.time()-T0, 1))), flush=True)
