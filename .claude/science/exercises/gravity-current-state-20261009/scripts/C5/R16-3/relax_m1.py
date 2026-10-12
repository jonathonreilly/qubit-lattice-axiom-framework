"""Relaxed problem at m = 1: sup of Xi_T2g (= M = U in the zigzag limit) over H, one or two atoms; does it reach 0?"""
import numpy as np, sys, itertools; sys.path.insert(0, '.')
from zz import xi_all; from relax import relaxed_gf
best = None
for H in [0.05, 0.1, 0.2, 0.3, 0.4, 0.6, 1.0, 1.5, 2.0, 2.5, 3.0]:
    for x0 in [0.01, 0.02, 0.05, 0.1, 0.2, 0.4, 0.8, 1.2, 1.6, 2.0, 2.5, 3.0]:
        if x0 > H: continue
        g, f = relaxed_gf(H, [(x0, np.pi - H)], n=1 << 13)
        X = xi_all(g, f, 1.0, nu=600)
        if best is None or X['M,T2g'] > best[0]: best = (X['M,T2g'], X['M,Eg'], H, x0)
print('m=1 relaxed one-atom sup over grid: T2g %+.3e (Eg %+.3e) at H=%.2f x0=%.2f' % best)
best = None
for H in [0.2, 0.4, 1.0, 2.0, 3.0]:
    for x1, x2 in itertools.product([0.02, 0.1, 0.3, 0.8, 1.5, 2.5], repeat=2):
        if x2 <= x1 or x2 > H: continue
        for fr in [0.2, 0.5, 0.8]:
            g, f = relaxed_gf(H, [(x1, fr*(np.pi-H)), (x2, (1-fr)*(np.pi-H))], n=1 << 12)
            X = xi_all(g, f, 1.0, nu=500)
            if best is None or X['M,T2g'] > best[0]: best = (X['M,T2g'], X['M,Eg'], H, x1, x2, fr)
print('m=1 relaxed two-atom sup over grid: T2g %+.3e (Eg %+.3e) at H=%.2f x1=%.2f x2=%.2f fr=%.1f' % best)
