"""R17-13 scan1: sign map of mu_T2^F on D1(b, r) at m = 0.01, 0.001 (form P, 4x12 and 6x16 GL), parts KK/KM/MM, and the zero b*(r)."""
import sys, time, numpy as np
sys.path.insert(0, '.')
import lib13 as L
from scipy.optimize import brentq
t0 = time.time()
bs = [0.15, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5]
rs = [0.05, 0.1, 0.3, 0.5, 0.56, 1/np.sqrt(3)]
for m in (0.01, 0.001):
    print('m = %g: mu_T2^F per Dirac field (rows b, cols r = %s)' % (m, ' '.join('%.4f' % r for r in rs)))
    for b in bs:
        vals = [L.muT2(L.D1law(b, r), m, 4, 12) for r in rs]
        print('  b=%.2f ' % b + ' '.join('%+.3e' % v for v in vals), flush=True)
print('parts (KK, KM, MM) at m=0.01, r=0.56:')
for b in (0.3, 0.6, 0.9, 1.2, 1.4):
    p = L.muT2_parts(L.D1law(b, 0.56), 0.01, 4, 12); print('  b=%.2f KK %+.3e KM %+.3e MM %+.3e sum %+.3e' % (b, *p, p.sum()))
print('zero b*(r) (brentq on b, 4x12; then value at 6x16):')
for m in (0.01, 0.001):
    for r in rs:
        f = lambda b: L.muT2(L.D1law(b, r), m, 4, 12)
        grid = np.linspace(0.15, 1.5, 28); v = [f(b) for b in grid]
        roots = []
        for i in range(len(grid)-1):
            if v[i]*v[i+1] < 0:
                bb = brentq(f, grid[i], grid[i+1], xtol=1e-13); roots.append((bb, L.muT2(L.D1law(bb, r), m, 6, 16)))
        print('  m=%g r=%.6f roots: %s' % (m, r, '; '.join('b*=%.10f (6x16 value %+.2e)' % x for x in roots)), flush=True)
print('elapsed %.0fs' % (time.time()-t0))
