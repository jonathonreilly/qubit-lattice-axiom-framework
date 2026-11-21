#!/usr/bin/env python3
"""GUIDE (row 918, family 4): Delta(1) = rho (<N>_0 - <N>_v)/(1 - rho) from twist.py logs, per spin class.
Classes: all half-integer spins, spin 3/2 only, half-integer >= 5/2 (N_hi). Error: N errors and rho error
(Monte Carlo resampling of log rho, N's Gaussian)."""
import json, sys
import numpy as np
rng = np.random.default_rng(0)
print("run | rho | Delta_half | Delta_3/2 | Delta_hi(>=5/2) | <N_hi>_0 per step")
for f in sys.argv[1:]:
    r = json.loads([l for l in open(f) if l.startswith('{') and 'logrho' in l][-1])
    if 'spin_plus_half' not in r: continue
    lr = rng.normal(min(r['logrho_bar'], -1e-3), r['err_bar'], 20000); lr = np.minimum(lr, -1e-4)
    rho = np.exp(lr)
    out = []
    for key in ('half', '3h', 'hi'):
        n0 = rng.normal(r[f'spin_plus_{key}'], r[f'spin_plus_{key}_err'], 20000)
        nv = rng.normal(r[f'spin_minus_{key}'], r[f'spin_minus_{key}_err'], 20000)
        D = rho*(n0 - nv)/(1 - rho)
        out.append(f"{np.median(D):+.3g} [{np.percentile(D,16):+.2g}, {np.percentile(D,84):+.2g}]")
    print(f"{f.split('/')[-1][:-4]} | {np.exp(r['logrho_bar']):.2f} | " + " | ".join(out) + f" | {r['spin_plus_hi']:.1e}({r['spin_plus_hi_err']:.0e})")
