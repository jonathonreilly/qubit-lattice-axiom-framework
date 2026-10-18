#!/usr/bin/env python3
"""HIER-2: best fits when symmetry allows only two orders {1, 3} (class L1 result of A3).
m = Lam * eps^n, n in {1, 3}, unit coefficients; Lam, eps fitted (2 parameters).
Reports the minimal worst-case deviation factor (one sector alone; all nine sector-blind)."""
import itertools
import numpy as np
from fit_control import SETS, SECT

def best_dev(logm, ords):
    # minimise max |log m_i - logLam - n_i log eps| over logLam, log eps<0 (grid + refine)
    best = np.inf; arg = None
    for le in np.linspace(np.log(1e-4), np.log(0.9), 3000):
        r = logm - np.array(ords) * le
        lam = (r.max() + r.min()) / 2           # minimax offset
        d = (r.max() - r.min()) / 2
        if d < best: best, arg = d, (np.exp(le), np.exp(lam))
    return np.exp(best), arg

for nm, m in SETS.items():
    print(f"=== set {nm}")
    for sec, ks in SECT.items():
        lm = np.log(np.array([m[k] for k in ks]))      # light, middle, heavy
        res = []
        for ords in itertools.product((1, 3), repeat=3):
            if not (ords[0] >= ords[1] >= ords[2]): continue
            dev, arg = best_dev(lm, ords)
            res.append((dev, ords, arg))
        res.sort()
        print(f"  {sec:<5} two-level best: x{res[0][0]:.2f} with orders(light,mid,heavy)={res[0][1]} eps={res[0][2][0]:.3g}")
    # all nine, sector-blind two-level patterns
    lm9 = np.log(np.array([[m['u'], m['c'], m['t']], [m['d'], m['s'], m['b']], [m['e'], m['mu'], m['tau']]]))
    res = []
    for ords in itertools.product((1, 3), repeat=3):
        dev, arg = best_dev(lm9.ravel(), list(ords) * 3)
        res.append((dev, ords, arg))
    res.sort()
    print(f"  all nine, sector-blind two-level best: x{res[0][0]:.1f} with orders={res[0][1]} eps={res[0][2][0]:.3g}")
    # all nine, sector-dependent assignment of {1,3} (still only two orders)
    best = (np.inf,)
    for o in itertools.product((1, 3), repeat=9):
        dev, arg = best_dev(lm9.ravel(), list(o))
        if dev < best[0]: best = (dev, o, arg)
    print(f"  all nine, any assignment of orders {{1,3}}: x{best[0]:.1f} with orders={best[1]} eps={best[2][0]:.3g}")
