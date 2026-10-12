"""Z1: transition-width dependence (Laplace) and high-N 3D grid at m = 0.3 (both forms)."""
import numpy as np, sys, time; sys.path.insert(0, '.')
from zz import *; from laws import *; from grid3d import xi3d, samples_full
T0 = time.time()
for wt in [0.03, 0.06, 0.1, 0.15, 0.2, 0.25, 0.3]:
    law = Z1(wt); g, f = law.samples(1 << 15); _, _, A = samples_full(law, 1 << 15)
    r = []
    for m in [1.0, 0.3, 0.1, 0.01]:
        X = xi_all(g, f, m, nu=2000)
        r.append('m=%.2f T2g M %+.3e U %+.3e Eg M %+.3e U %+.3e' % (m, X['M,T2g'], X['U,T2g'], X['M,Eg'], X['U,Eg']))
    print('wt=%.2f max|s\'|=%.6f A in [%.1f,%.1f] min edge g=%.4f :: %s' % (wt, np.abs(law.sp).max(), A.min(), A.max(), (law.sig[law.k >= 1.0]**2).min(), ' | '.join(r)), flush=True)
for wt in [0.06, 0.15]:
    law = Z1(wt)
    for N in [360, 480, 720]:
        X = xi3d(law, 0.3, N)
        print('  Z1(wt=%.2f) 3D grid m=0.3 N=%d: ' % (wt, N) + ' '.join('%s A %+.5e / IBP %+.5e' % (v, x[0], x[1]) for v, x in X.items()), flush=True)
print('runtime %.1fs' % (time.time()-T0))
