#!/usr/bin/env python3
"""B23 bookkeeping: multiplicities of all k* levels (n_S != 0 words) in the screened families, to state what the
Dirac-level screen (m = 4, D+ (+) D-) leaves out."""
import sys, os, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from b23lib import *
from multiprocessing import Pool
def f(job):
    w = build(*job)
    if nS(w) == 0: return []
    W0 = Wb(w, kst[None])[0]; e, V = np.linalg.eig(W0); out = []
    for E, m in levels(W0):
        tag = m
        if m >= 4:
            Vd = V[:, np.abs(wrap(np.angle(e) - E)) < 1e-6]; Q, _ = np.linalg.qr(Vd)
            tag = (m, round(float(np.linalg.norm(Q.conj().T @ Dpm) ** 2)))     # (multiplicity, dim of overlap with D+ (+) D-)
        out.append(tag)
    return out
if __name__ == '__main__':
    tot = collections.Counter()
    for T in ['cliff2:0,1,2,3,4,5,6,7,8,9,10', 'pi6', 'taste_pi6']:
        with Pool(4) as p: R = p.map(f, list(jobs(T)), chunksize=64)
        c = collections.Counter(x for r in R for x in r); print(T, dict(sorted(c.items(), key=str)), flush=True); tot.update(c)
    print("all:", dict(sorted(tot.items(), key=str)))
    print("TOTAL: PASS=0 FAIL=0  (bookkeeping only)")
