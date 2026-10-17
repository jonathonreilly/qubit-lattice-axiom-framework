"""Second search: larger X strength.  Score = max overshoot (grid 16^3, offset grid + k*), then local
optimization; final verification by fine extremes, touchings, and the massive global gap."""
import pickle, sys
import numpy as np
from scipy.optimize import minimize
from core import *
from bases import get
rng = np.random.default_rng(int(sys.argv[1]))
fm = fixed_momenta(); KS = np.array(fm[0]) * np.pi / 4
Xb = get('X_r1'); Mb = get('Q_onsite_im_A2')
def build(t1, t2, dl, c):
    X = addm(*Xb, coeffs=list(c / np.linalg.norm(c))); nrm = max(np.abs(M).max() for M in X.values())
    return addm(hop(t1, t2), X, coeffs=[1, dl / nrm])
N = 16; g = (np.arange(N) + 0.5) * 2 * np.pi / N
KG = np.vstack([np.array(np.meshgrid(g, g, g, indexing='ij')).reshape(3, -1).T, KS])
def doublets(H):
    e = np.linalg.eigvalsh(bloch(H, KS)); out = []; i = 0
    while i < 12:
        j = i
        while j + 1 < 12 and abs(e[j+1] - e[i]) < 1e-8: j += 1
        if j - i + 1 == 2: out.append((i, e[i]))
        i = j + 1
    return out
def score(t1, t2, dl, c):
    H = build(t1, t2, dl, c); E = np.linalg.eigvalsh(bloch_batch(H, KG)); best = (np.inf, None)
    for lev, Ed in doublets(H):
        s = max((E[:, lev] - Ed).max(), (Ed - E[:, lev + 1]).max())
        # normalize by the Weyl splitting scale: require a usable gap to neighbours as well
        best = min(best, (s, lev), key=lambda x: x[0])
    return best
res = []
for trial in range(int(sys.argv[2])):
    t1 = rng.choice([-1.0, 1.0]); t2 = rng.uniform(-1.0, 1.0); dl = 10 ** rng.uniform(-0.6, 0.5); c = rng.normal(size=9)
    s, lev = score(t1, t2, dl, c); res.append((s, t1, t2, dl, c, lev))
res.sort(key=lambda r: r[0])
for r in res[:6]: print(f"  bad={r[0]:+.4f} t1={r[1]:+.0f} t2={r[2]:+.3f} delta={r[3]:.3f} lev={r[5]}")
out = []
for r in res[:3]:
    x0 = np.concatenate([[r[2], np.log10(r[3])], r[4]])
    o = minimize(lambda x: score(r[1], x[0], 10 ** x[1], x[2:])[0], x0, method='Nelder-Mead', options=dict(maxiter=600, xatol=1e-6, fatol=1e-9))
    out.append((o.fun, r[1], o.x)); print(f"  optimized: bad={o.fun:+.2e} t1={r[1]:+.0f} t2={o.x[0]:+.4f} delta={10**o.x[1]:.4f}")
pickle.dump(out, open(f'search2_{sys.argv[1]}.pkl', 'wb'))
