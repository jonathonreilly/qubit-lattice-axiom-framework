"""R16-10 (b): the continuum constant K_s = lim of the speed shift of continuum QED (Feynman gauge) whose photon
loop momentum is integrated over a ball |q| < R (all q0), R -> infinity. Claim: K_s is independent of m, lam
(proved in the report; checked here for several m, lam), K_0 = -1/3 exactly (closed form), K_1/2 computed.
Units: dc x 16pi^2 (e^2/16pi^2)."""
import numpy as np, time, sys
from r1610_core import *
t0 = time.time()
u = lambda k: np.asarray(k, float)**2
d = lambda q: np.asarray(q, float)
S = lambda k: np.asarray(k, float)
Wz = lambda k: 0.0*np.asarray(k, float)
for (m, lam) in [(1.0, 1.0), (1.0, 0.1), (0.1, 1.0), (1.0, 0.0)]:
    for (R, nr, nmu) in [(2000.0, 12, 24), (20000.0, 16, 32)]:
        pts, wts, rr = sph_points(R*max(m, lam), nr, nmu)
        h = 0.01*min(m, lam) if lam > 0 else 0.01*m
        K0, _ = speed_scalar(pts, wts, m, lam, u, d, h)
        K12, _ = speed_dirac(pts, wts, m, lam, S, Wz, d, h)
        print('m=%.2f lam=%.2f R=%7.0f nr=%2d nmu=%2d | K_0 = %+.6f (exact -1/3 = %+.6f) | K_1/2 = %+.6f'
              % (m, lam, R, nr, nmu, K0, -1/3, K12), flush=True)
print('elapsed %.1fs' % (time.time() - t0))
