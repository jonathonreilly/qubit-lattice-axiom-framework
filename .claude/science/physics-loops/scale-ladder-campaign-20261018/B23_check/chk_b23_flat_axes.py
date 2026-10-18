#!/usr/bin/env python3
"""Follow-up to chk_b23.py: the three sampled stored-'flat' nodes read 'aniso' with 60 random directions.
Re-test them with the coordinate axes and face/body diagonals added (independent build, core_build.py), and
measure the slope scaling along the slowest direction (flat = some direction with zero branch slope; either O(q^2) or identically at E)."""
import os, sys, itertools
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import numpy as np
import core_build as B
def wrap(x): return np.angle(np.exp(1j * np.asarray(x)))
kmap = lambda k: -np.asarray(k, float) + np.pi * np.ones(3)      # dictionary fixed in chk_b23.log (s=-1, lam=(1,1,1), S-sign +1)
cases = [(('S', 'o', 'S', 'o'), ('L002', 'L222'), (0.0, 0.0, 0.5), 4), (('S2', 'o', 'S2', 'o'), ('L220', 'L310'), (-0.5, -0.25, -0.25), 2),
         (('S', 'o', 'S', 'o'), ('L100', 'L030'), (-1.0, -1.0, 0.25), 2)]
import pickle, glob
E_of = {}
for fn in glob.glob(os.path.join(HERE, '..', 'B23_dirac_level_screen', 'screen_cliff2*.pkl')):
    for r in pickle.load(open(fn, 'rb'))['recs']:
        if not r['fermi']: E_of[(r['sk'], r['names'])] = r['E']
dirs = [np.array(d, float) for d in itertools.product((-1, 0, 1), repeat=3) if any(d)]
dirs = [d / np.linalg.norm(d) for d in dirs]
P = F = 0
for sk, nm, kb, m in cases:
    w = B.word(sk, nm); E = E_of[(sk, nm)]; k0 = kmap(np.array(kb) * np.pi)
    e0 = wrap(np.angle(np.linalg.eigvals(B.Wk(w, k0))) - E); mult = int(np.sum(np.abs(e0) < 1e-8))
    def sl(d, q):
        e = wrap(np.angle(np.linalg.eigvals(B.Wk(w, k0 + q * d))) - E); e = np.sort(e[np.argsort(np.abs(e))[:m]]); return np.abs(e) / q
    smin = [(float(sl(d, 1e-4).min()), float(sl(d, 1e-3).min()), tuple(np.round(d, 3))) for d in dirs]
    smin.sort()
    ok = mult == m and smin[0][0] < 1e-3          # zero branch slope along some direction (flat)
    kind = 'exactly zero along it (branch stays at E: nodal line)' if smin[0][1] < 1e-9 else 'quadratic along it'
    P += ok; F += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {sk} {nm} k/pi={kb} m={m}: mult {mult}; slowest direction {smin[0][2]}: min |e|/q = {smin[0][0]:.2e} (q=1e-4), {smin[0][1]:.2e} (q=1e-3) -> flat, {kind}")
print(f"TOTAL: PASS={P} FAIL={F}")
