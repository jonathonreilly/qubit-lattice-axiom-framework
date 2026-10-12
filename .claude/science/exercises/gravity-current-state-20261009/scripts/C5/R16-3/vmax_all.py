"""Whole-zone v_max (d=3, exact for separable laws by bisection) for every law named in the report; corner values."""
import numpy as np, sys; sys.path.insert(0, '.')
from zz import *; from floor_scan import Zz; from simul2 import A, B, C, law
C2 = Zz(1.0, 0.35, 0.47, 0.03)
Lg = ZLaw([1.0, -0.44, 0.44, -0.44, 0.0], [1.0, 1.8, 2.4, 2.8], 0.06, 'gentle', nf=1 << 16)
for nm, L in [('G(1.0)', A), ('Z1(0.06)', B), ('C=Zz(1.0,0.35,0.43,0.03)', C), ('C2=Zz(1.0,0.35,0.47,0.03)', C2), ('gentle', Lg)]:
    g, f = L.samples(1 << 15)
    print('%s: max|s\'|=%.9f, edge valleys(k,g)=%s | ' % (nm, np.abs(L.sp).max(), L.info()['valleys']) + ' '.join('m=%.2f v_max %.6f' % (m, L.vmax(m)) for m in [1.0, 0.3, 0.1, 0.01]))
    for m in [0.3, 0.1]:
        X = xi_all(g, f, m); print('     m=%.1f %s mu_E %+.3e' % (m, ' '.join('%s %+.3e' % kv for kv in X.items()), mu_E(g, f, m)))
