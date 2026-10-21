#!/usr/bin/env python3
"""Reviewer re-run of the author's (unkept) scratch test NOTE §3.3 'conditional detailed balance at fixed vertex
positions': with all vertex (F+P) positions frozen (sweep(..., nfix>=0), no loops, no cube moves), the cluster
phase (+ global reversal) must sample (s0, F/P labelling) with weight exp(-g beta Ibar[F-path]), because
n_F + n_P is fixed.  Ibar is computed here by own code.  Occupancies vs exact weights normalised on the visited
set; errors by 20 batch means.  usage: rs5_cluster_conditional_db.py SEED BETA NSWEEPS [L]"""
import os, sys, itertools
os.environ.setdefault("NUMBA_CACHE_DIR", os.path.join(os.path.dirname(os.path.abspath(__file__)), "__pycache__", "numba"))
sys.dont_write_bytecode = True
import numpy as np
from scipy import stats
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "scripts"))
import ctqmc
from sim import PT
seed, beta, NSW = int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3])
L = int(sys.argv[4]) if len(sys.argv) > 4 else 2
# get a typical configuration from the block's own PT at this beta (single replica)
pt = PT(L, [beta], seed=seed)
for _ in range(500): pt.sweep_all()
r = pt.reps[0]; A = pt.A
pl = A[0]
s0 = r.s0.copy(); ft = r.ft[:r.nF].copy(); fp = r.fp[:r.nF].copy(); nF = r.nF
# draw one marker set via one ordinary sweep, then freeze all vertices
ctqmc.nb_seed(seed + 5)
ftn, fpn, nF, st, _, mt, mp, nM = ctqmc.sweep(s0, ft, fp, nF, beta, 1.0, 0.0, pl, A[2], A[3], A[4], A[5], A[6], 0, 0.5)
ft, fp, mt, mp = ftn[:nF].copy(), fpn[:nF].copy(), mt[:nM].copy(), mp[:nM].copy()
allt = np.concatenate([ft, mt]); allp = np.concatenate([fp, mp])
print(f"[INFO] L={L} beta={beta} seed={seed}: frozen vertices nF+nP = {nF}+{nM} = {nF+nM}")

def own_ibar(s0, ft, fp):
    """own: integral over u of the number of circulating plaquettes along the F-path."""
    o = np.argsort(ft); ts = np.concatenate([[0.0], ft[o], [1.0]])
    s = s0.copy(); I = 0.0
    for i in range(len(ts) - 1):
        a = s[pl]
        nc = np.sum(np.abs(a[:, 0] + a[:, 1] - a[:, 2] - a[:, 3]) == 4)
        I += nc * (ts[i+1] - ts[i])
        if i < len(o):
            q = fp[o[i]]
            assert abs(s[pl[q, 0]] + s[pl[q, 1]] - s[pl[q, 2]] - s[pl[q, 3]]) == 4
            s[pl[q]] *= -1
    assert np.array_equal(s, s0)
    return I

keys = {}; Ib = []; seq = []
ctqmc.nb_seed(seed + 77)
for it in range(NSW):
    ftn, fpn, nF2, st, _, mt2, mp2, nM2 = ctqmc.sweep(s0, ft, fp, nF, beta, 1.0, 0.0, pl, A[2], A[3], A[4], A[5], A[6],
                                                    0, 0.5, True, mt, mp, nM)
    assert nF2 + nM2 == len(allt)
    ft, fp, nF = ftn[:nF2].copy(), fpn[:nF2].copy(), nF2
    mt, mp, nM = mt2[:nM2].copy(), mp2[:nM2].copy(), nM2
    o = np.argsort(ft)
    k = (tuple(s0.tolist()), tuple(np.round(ft[o], 12).tolist()), tuple(fp[o].tolist()))
    if k not in keys:
        keys[k] = len(keys); Ib.append(own_ibar(s0, ft, fp))
    seq.append(keys[k])
seq = np.array(seq); Ib = np.array(Ib); n = len(keys)
w = np.exp(-beta * (Ib - Ib.min())); pi = w / w.sum()
NB = 20; m = len(seq) // NB
occ = np.array([np.bincount(seq[b*m:(b+1)*m], minlength=n) / m for b in range(NB)])
f = occ.mean(0); se = occ.std(0, ddof=1) / np.sqrt(NB)
use = (pi * len(seq) > 200) & (se > 0)
z = (f[use] - pi[use]) / se[use]
chi2 = float((z**2).sum()); dof = int(use.sum()) - 1
# chi^2 of batch-mean z's: Hotelling-free approximation; compare also with the max |z|
p = 1 - stats.chi2.cdf(chi2, dof)
npass = int(p > 1e-3); nfail = 1 - npass
print(f"[INFO] visited configurations: {n}; tested (expected count > 200): {use.sum()}; distinct Ibar values: {len(np.unique(np.round(Ib, 9)))}")
print(f"[{'PASS' if npass else 'FAIL'}] occupancy vs exp(-g beta Ibar) on the visited set: chi2={chi2:.1f} dof={dof} p={p:.3f} max|z|={np.abs(z).max():.2f}")
# control: the same occupancies against the uniform distribution (should be rejected if Ibar varies)
pu = np.ones(n) / n
zu = (f[use] - pu[use]) / se[use]
print(f"[INFO] control vs uniform: chi2={float((zu**2).sum()):.1f} dof={dof}")
print(f"TOTAL: PASS={npass} FAIL={nfail}")
