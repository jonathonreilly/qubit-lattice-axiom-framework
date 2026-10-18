"""Fast driver for b5c_emitter: tolerance by linear response at x0, then one direct verification.
usage: python3 b5c_fast.py gam Tl  -> one JSON row"""
import sys, json, numpy as np
from b5c_emitter import errs, E
gam, Tl = float(sys.argv[1]), float(sys.argv[2]); g = 1.0
lam = gam**2 / g; T = Tl / lam; M = int(1.15 * 2 * g * 2 * T) + 60
cache = {}; row = dict(gam=gam, lam=lam, T=T, M=M)
for kind, x0 in (('SB', 1e-5), ('SO', 1e-7 * lam / 0.04), ('RB', 1e-7)):
    e0 = errs(gam, g, M, T, kind, x0, cache)
    for met in ('act', 'nom', 'pop'):
        if met == 'nom' and kind == 'RB': continue
        xs = x0 * E / e0[met]
        v = errs(gam, g, M, T, kind, xs, cache)[met]
        row[f'{kind}_{met}'] = xs; row[f'{kind}_{met}_verify'] = v
print(json.dumps({k: (float(f'{v:.4g}') if isinstance(v, float) else v) for k, v in row.items()}), flush=True)
