"""Are bands lev and lev+1 forced to touch away from +-k*?  Minimum direct gap over the BZ (grid + local
minimization) for the runner's H and the best search candidates; where the touchings are and at what energy."""
import glob, pickle
import numpy as np
from scipy.optimize import minimize
from core import *
from bases import get
rng = np.random.default_rng(1)
fm = fixed_momenta(); KS = np.array(fm[0]) * np.pi / 4
Xb = get('X_r1')
def build(t1, t2, dl, c):
    X = addm(*Xb, coeffs=list(c / np.linalg.norm(c))); nrm = max(np.abs(M).max() for M in X.values())
    return addm(hop(t1, t2), X, coeffs=[1, dl / nrm])
R = pickle.load(open('runner_blocks.pkl', 'rb'))
Hrun = {tuple(-x for x in sh): M for sh, M in R['bl'].items()}
cands = [('runner', Hrun, 0)]
for f in sorted(glob.glob('global_search_*.pkl')):
    for fun, t1, x in pickle.load(open(f, 'rb')):
        if fun < 1e-3 and 10 ** x[1] > 1e-3 and abs(x[0]) > 1e-3 and t1 < 0:
            cands.append((f't1={t1:+.0f} t2={x[0]:+.4f} d={10**x[1]:.4f}', build(t1, x[0], 10 ** x[1], x[2:]), 0))
N = 24; g = (np.arange(N) + 0.37) * 2 * np.pi / N
KG = np.array(np.meshgrid(g, g, g, indexing='ij')).reshape(3, -1).T
def dist(k, k0): return np.linalg.norm((k - k0 + np.pi) % (2 * np.pi) - np.pi)
for name, H, lev in cands:
    E = np.linalg.eigvalsh(bloch_batch(H, KG)); gap = E[:, lev + 1] - E[:, lev]
    found = []
    for i in np.argsort(gap)[:40]:
        f = lambda k: np.diff(np.linalg.eigvalsh(bloch(H, k))[lev:lev + 2])[0]
        r = minimize(f, KG[i], method='Nelder-Mead', options=dict(xatol=1e-10, fatol=1e-14, maxiter=6000))
        if r.fun < 1e-6:
            kk = r.x % (2 * np.pi)
            if all(dist(kk, q) > 1e-3 for q, _ in found): found.append((kk, np.linalg.eigvalsh(bloch(H, kk))[lev]))
    Ed = np.linalg.eigvalsh(bloch(H, KS))[lev]
    print(f"{name}: touchings of bands {lev},{lev+1} (E_d = {Ed:.5f}):")
    for kk, e in sorted(found, key=lambda x: x[1]):
        print(f"    k/(pi/2) = {np.round(kk / (np.pi / 2), 4)}   E - E_d = {e - Ed:+.5f}")
