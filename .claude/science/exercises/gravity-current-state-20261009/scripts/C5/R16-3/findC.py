"""Smooth laws with Xi_Eg < 0 < Xi_T2g (vertex M and U) — the third corner for the simultaneous-zero triangle."""
import numpy as np, sys; sys.path.insert(0, '.')
from zz import *; from floor_scan import Zz
res = []
for b in [1.0, 1.2, 1.4]:
    for V in [0.35, 0.45, 0.55]:
        for amp in [0.08, 0.12, 0.16, 0.2]:
            for wt in [0.03, 0.05]:
                if amp < 1.6*wt: continue
                L = Zz(b, V, V + amp, wt)
                if L is None: continue
                g, f = L.samples(1 << 14)
                for m in [0.3, 0.1]:
                    X = xi_all(g, f, m, nu=800)
                    res.append((m, X['M,T2g'] - 3*max(X['M,Eg'], 0), L.name, X))
for m in [0.3, 0.1]:
    rr = sorted([r for r in res if r[0] == m], key=lambda r: -r[1])[:6]
    for r in rr: print('m=%.1f %s :: %s' % (m, r[2], ' '.join('%s %+.3e' % kv for kv in r[3].items())))
