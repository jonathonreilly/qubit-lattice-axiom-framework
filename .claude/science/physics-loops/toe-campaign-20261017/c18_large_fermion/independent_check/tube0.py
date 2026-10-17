"""Item 7: C17 default flux (tube = 0): where is the band minimum?  (quartet.py does the t1=+1 sector.)"""
import itertools
import numpy as np
from scipy.optimize import minimize
import bands
from model import *
bands.U[2] = solve_gauge(dict(square=1, triangle=0, plaquette=1, tube=0))
bands.U[3] = solve_gauge(dict(square=1, triangle=1, plaquette=1, tube=0))
rng = np.random.default_rng(3)
for tri_key, t1 in ((2, -1.0), (3, 1.0)):
    for t2, lam in ((0.1, -0.5), (0.3, -0.5), (0.1, 0.5), (0.2, -0.3)):
        u = bands.U[tri_key]
        e0 = lambda k: np.linalg.eigvalsh(bloch(u, k, t1, t2, lam))[0]
        mins = []
        for k0 in rng.uniform(-np.pi, np.pi, (80, 3)):
            r = minimize(e0, k0, method='Nelder-Mead', options=dict(xatol=1e-10, fatol=1e-14, maxiter=20000))
            mins.append((r.fun, bands.wrap(r.x)))
        fmin = min(f for f, x in mins)
        glob = []
        for f, x in mins:
            if f - fmin < 1e-8 and all(np.linalg.norm(bands.wrap(x - y)) > 1e-3 for y in glob): glob.append(x)
        deg = int(np.sum(np.abs(np.linalg.eigvalsh(bloch(u, glob[0], t1, t2, lam)) - fmin) < 1e-7))
        print(f"tube=0 tri={tri_key-2} t1={t1:+} t2={t2} lam={lam}: Emin={fmin:.6f}, {len(glob)} degenerate minima at (units pi/2) "
              f"{[tuple(np.round(x/(np.pi/2), 4)) for x in glob]}, each {deg}-fold")
