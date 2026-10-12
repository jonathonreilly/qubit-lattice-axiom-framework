"""Relaxed problem with two atoms: look for Eg < 0 < T2g (vertex M = U in the zigzag limit). Also endpoint values of Zz(V=0.2)."""
import numpy as np, sys, itertools; sys.path.insert(0, '.')
from zz import *; from relax import relaxed_gf; from floor_scan import Zz
for m in [0.3, 0.1]:
    best = None; cnt = 0
    for H in [0.6, 0.8, 1.0, 1.4, 1.8, 2.2]:
        for x1, x2 in itertools.product([0.1, 0.2, 0.3, 0.5, 0.7, 1.0, 1.4, 2.0], repeat=2):
            if x1 > H or x2 > H or x2 <= x1: continue
            for fr in [0.1, 0.3, 0.5, 0.7, 0.9]:
                c = np.pi - H
                g, f = relaxed_gf(H, [(x1, fr*c), (x2, (1-fr)*c)], n=1 << 12)
                X = xi_all(g, f, m, nu=500); cnt += 1
                if X['M,Eg'] < 0 and (best is None or X['M,T2g'] > best[0]): best = (X['M,T2g'], X['M,Eg'], H, x1, x2, fr)
    print('relaxed m=%.1f (%d configs): max T2g subject to Eg<0: %s' % (m, cnt, best), flush=True)
for (b, V) in [(0.6, 0.2), (0.8, 0.2), (0.8, 0.3), (1.0, 0.4)]:
    L = Zz(b, V, b, 0.06); g, f = L.samples(1 << 14)
    print('Zz(b=%.1f,V=%.1f,P=b) ' % (b, V) + ' '.join('m=%.1f: %s' % (m, ' '.join('%s %+.2e' % kv for kv in xi_all(g, f, m).items())) for m in [0.3, 0.1]))
