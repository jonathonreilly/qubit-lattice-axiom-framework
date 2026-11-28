#!/usr/bin/env python3
"""GUIDE (row 918, family 3): cut response on the joined free-wall box B|B, for (J-INT) of row 910.
Usage: fw.py tlen b c d beta nsgrid nth nmeas seed
Lattice tlen x (2b) x c x d, periodic time, free spatial walls. Cut = (1, nu) plaquettes with base x_1 = b-1
(they contain the crossing links between the two halves). Cut coefficient s on a Gauss-Legendre grid of [0, 1].
Prints per s the mean and binned error of X_cut = sum of x_p over the cut, and the Gauss-Legendre weights.
E(a; B) = beta int_0^1 [<X>_(a; s) - (a/T) <X>_(T; s)] ds (two runs, tlen = a and tlen = T).
"""
import sys, json, time
import numpy as np
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from su2lat import Lattice, binned_err, pl_index

tl, b, c, d = (int(x) for x in sys.argv[1:5]); beta = float(sys.argv[5])
ns, nth, nme, seed = (int(x) for x in sys.argv[6:10])
lat = Lattice((tl, 2*b, c, d), beta, seed, free=(False, True, True, True))
cut = []
for nu in (0, 2, 3):
    k = pl_index(1, nu)
    sites = np.nonzero((lat.coords[1] == b-1) & (lat.C[k] != 0))[0]
    cut.append((k, sites))
ncut = sum(s.size for _, s in cut)
xg, wg = np.polynomial.legendre.leggauss(ns); sg = 0.5*(xg + 1); wg = 0.5*wg
T0 = time.time()
for si, s in enumerate(sg):
    for k, sites in cut: lat.C[k, sites] = s
    lat.refresh()
    for _ in range(nth if si > 0 else 3*nth): lat.sweep(3)
    xs = []
    for _ in range(nme):
        lat.sweep(3); x = lat.plaquettes()
        xs.append(sum(x[k, sites].sum() for k, sites in cut))
    print(json.dumps(dict(tlen=tl, b=b, c=c, d=d, beta=beta, s=float(s), w=float(wg[si]), ncut=int(ncut),
                          X=float(np.mean(xs)), dX=float(binned_err(xs)), nmeas=nme, sec=round(time.time()-T0, 1))), flush=True)
