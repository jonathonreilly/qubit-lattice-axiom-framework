#!/usr/bin/env python3
"""GUIDE (row 918): plaquette means on a torus t x B along a beta grid, for thermodynamic integration.
Usage: ti.py t b1 b2 b3 betas(comma) nth nmeas seed [free(0/1)] [n_or]
  free=1 makes all three spatial directions free walls (periodic time).
Per beta prints one JSON line: mean and binned error of Pw = sum_p c_p x_p / N_c (the beta-derivative of log Z
divided by N_c = sum_p c_p), of the temporal (planes 0i) and spatial (planes ij) parts, and N_c.
Annealed: each beta starts from the last configuration of the previous one, then nth sweeps of thermalization.
"""
import sys, json, time
import numpy as np
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from su2lat import Lattice, binned_err

t, b1, b2, b3 = (int(x) for x in sys.argv[1:5])
betas = [float(x) for x in sys.argv[5].split(',')]
nth, nme, seed = int(sys.argv[6]), int(sys.argv[7]), int(sys.argv[8])
free = len(sys.argv) > 9 and sys.argv[9] == '1'
n_or = int(sys.argv[10]) if len(sys.argv) > 10 else 3
lat = Lattice((t, b1, b2, b3), betas[0], seed, free=(False, free, free, free))
C = lat.C
tmask = np.zeros(6, bool); tmask[:3] = True
Nc = C.sum(); Nt = C[tmask].sum(); Ns = C[~tmask].sum()
T0 = time.time()
for beta in betas:
    lat.beta = beta
    for _ in range(nth): lat.sweep(n_or)
    W, Wt, Ws = [], [], []
    for _ in range(nme):
        lat.sweep(n_or)
        x = lat.plaquettes() * C
        st = x[tmask].sum(); ss = x[~tmask].sum()
        W.append((st + ss)/Nc); Wt.append(st/Nt); Ws.append(ss/Ns)
    out = dict(t=t, B=[b1, b2, b3], free=free, beta=beta, nth=nth, nmeas=nme, seed=seed, Nc=float(Nc), Nt=float(Nt), Ns=float(Ns),
               P=float(np.mean(W)), dP=float(binned_err(W)), Pt=float(np.mean(Wt)), dPt=float(binned_err(Wt)),
               Ps=float(np.mean(Ws)), dPs=float(binned_err(Ws)), sec=round(time.time()-T0, 1))
    print(json.dumps(out), flush=True)
