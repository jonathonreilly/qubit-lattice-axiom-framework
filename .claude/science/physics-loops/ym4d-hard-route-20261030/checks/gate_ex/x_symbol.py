#!/usr/bin/env python3
"""X6 of CRITERIA.md: min over all P, polarisation, of (g(P) - 1)/|P-hat|^2, by optimiser, not a grid."""
import importlib.util, os, sys
import numpy as np
from scipy.optimize import minimize
spec = importlib.util.spec_from_file_location("exc", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "hard-core--mapped_excess.py"))
sys.argv = ["x"]
exc = importlib.util.module_from_spec(spec); spec.loader.exec_module(exc)
def obj(P, L):
    P = np.asarray(P)
    Min = exc.forms(P, L, 1, 4)[0]
    Min = (Min + Min.T) / 2
    Ph = 2 * np.sin(P / 2)
    return (np.linalg.eigvalsh(Min)[0] - 1) / np.sum(Ph**2)
rng = np.random.default_rng(0)
for L in [3, 5, 7]:
    best = (1e9, None)
    starts = [rng.uniform(1e-3, np.pi, 4) for _ in range(60)]
    starts += [rng.uniform(1e-3, 0.3, 4) for _ in range(30)]
    starts += [np.array(s) * x for x in [0.05, 0.5, 1.0, 2.0, 3.0] for s in [(1, 1, 1, 0.0), (1, 1, 1, 1), (1, 1, 0, 0), (1, 0, 0, 0)]]
    for s in starts:
        s = np.where(s == 0, 1e-4, s)
        r = minimize(obj, s, args=(L,), method="Nelder-Mead", options=dict(xatol=1e-5, fatol=1e-9, maxiter=1500))
        if r.fun < best[0]:
            best = (r.fun, r.x)
    print(f"L={L} min (g-1)/|Phat|^2 = {best[0]:.6f} at P={np.round(best[1],4)}; (1/9)(1-L^-2)={(1-L**-2)/9:.6f}; ratio={best[0]/((1-L**-2)/9):.4f}", flush=True)
