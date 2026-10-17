"""Survey of extra band-0/1 touchings (t1=-1, lowest level at k* a doublet) incl. larger delta, plus the
off-grid overshoot of band 0 above / band 1 below E_d.  If no extra touching and no overshoot: clean."""
import numpy as np
from scipy.optimize import minimize
from core import *
from bases import get
rng = np.random.default_rng(31)
fm = fixed_momenta(); KS = np.array(fm[0]) * np.pi / 4
Xb = get('X_r1')
def build(t1, t2, dl, c):
    X = addm(*Xb, coeffs=list(c / np.linalg.norm(c))); nrm = max(np.abs(M).max() for M in X.values())
    return addm(hop(t1, t2), X, coeffs=[1, dl / nrm])
N = 24; g = (np.arange(N) + 0.37) * 2 * np.pi / N
KG = np.array(np.meshgrid(g, g, g, indexing='ij')).reshape(3, -1).T
def dist(k, k0): return np.linalg.norm((k - k0 + np.pi) % (2 * np.pi) - np.pi)
cnt = dict(n=0, touch=0, clean=0)
for trial in range(40):
    t2 = rng.uniform(-1, 1); dl = 10 ** rng.uniform(-1.3, 0); H = build(-1.0, t2, dl, rng.normal(size=9))
    e = np.linalg.eigvalsh(bloch(H, KS))
    if abs(e[0] - e[1]) > 1e-8 or abs(e[1] - e[2]) < 1e-8: continue
    Ed = e[0]; cnt['n'] += 1
    E = np.linalg.eigvalsh(bloch_batch(H, KG)); gap = E[:, 1] - E[:, 0]; tch = []
    for i in np.argsort(gap)[:40]:
        r = minimize(lambda k: np.diff(np.linalg.eigvalsh(bloch(H, k))[0:2])[0], KG[i], method='Nelder-Mead', options=dict(xatol=1e-10, fatol=1e-14, maxiter=6000))
        if r.fun < 1e-6 and min(dist(r.x, KS), dist(r.x, -KS)) > 1e-2: tch.append(np.linalg.eigvalsh(bloch(H, r.x))[0] - Ed)
    mx = E[:, 0].max() - Ed; mn = Ed - E[:, 1].min()
    for i in np.argsort(-E[:, 0])[:8]:
        r = minimize(lambda k: -np.linalg.eigvalsh(bloch(H, k))[0], KG[i], method='Nelder-Mead', options=dict(xatol=1e-10, fatol=1e-14)); mx = max(mx, -r.fun - Ed)
    for i in np.argsort(E[:, 1])[:8]:
        r = minimize(lambda k: np.linalg.eigvalsh(bloch(H, k))[1], KG[i], method='Nelder-Mead', options=dict(xatol=1e-10, fatol=1e-14)); mn = max(mn, Ed - r.fun)
    cnt['touch'] += bool(tch); cnt['clean'] += (not tch) and mx < 1e-8 and mn < 1e-8
    print(f"  t2={t2:+.3f} delta={dl:.3f}: extra touchings {len(tch):2d} at E-E_d {np.round(sorted(set(np.round(tch, 5))), 4)}; band0 overshoot {mx:+.2e}, band1 undershoot {mn:+.2e}")
print(cnt)
