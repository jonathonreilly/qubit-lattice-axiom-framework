"""Witness Z1: Laplace evaluator at two resolutions, 3D grid both forms N=120/160/240, v_max, I(B), A range."""
import numpy as np, sys, time; sys.path.insert(0, '.')
from zz import *; from laws import *; from grid3d import xi3d, samples_full
T0 = time.time()
law = Z1(0.06)
inf = law.info()
gA, fA, AA = samples_full(law, 1 << 16)
print('== %s : max|sigma\'| = %.12f ; sigma(pi) = %.6f ; sigma\'(pi) = %.2e ; A range [%.2f, %.2f]' % (law.name, inf['maxabs'], inf['sig_pi'], law.sp[-1], AA.min(), AA.max()))
print('   local minima of g (k, g):', inf['valleys'], '; min g on [1.0,pi] = %.4f' % (law.sig[law.k >= 1.0]**2).min())
for m in [1.0, 0.3, 0.1, 0.01]:
    g, f = law.samples(1 << 14); X1 = xi_all(g, f, m, nu=1500, umin=-16)
    g, f = law.samples(1 << 16); X2 = xi_all(g, f, m, nu=4000, umin=-22)
    print('  m=%.2f v_max(d=3)=%.6f | n=2^14: %s | n=2^16: %s' % (m, law.vmax(m), ' '.join('%s %+.5e' % kv for kv in X1.items()), ' '.join('%s %+.6e' % kv for kv in X2.items())), flush=True)
Bs = [1e-4, 1e-2, 0.1, 0.3, 0.5, 1, 2, 3, 5, 10]
g, f = law.samples(1 << 16)
print('  I(B):', ' '.join('B=%g:%+.4g' % (B, I) for B, I in zip(Bs, Icurve(g, f, Bs))))
for m in [0.3, 0.1]:
    for N in [120, 160, 240]:
        X = xi3d(law, m, N)
        print('  3D grid m=%.1f N=%d: ' % (m, N) + ' '.join('%s A %+.4e / IBP %+.4e' % (v, x[0], x[1]) for v, x in X.items()), flush=True)
print('runtime %.1fs' % (time.time()-T0))
