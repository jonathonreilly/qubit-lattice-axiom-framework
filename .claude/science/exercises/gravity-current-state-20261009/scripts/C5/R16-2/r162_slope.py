"""R16-2 (d): mass slope dF/dm of the on-shell speed at resolved masses (m >= 0.2, N = 192/256, lam = 0.05),
for the residual after tuning. D1(1.4, 1/sqrt3) and D1(1.0, 1/sqrt3) Dirac; G(1.4), G(1.0) scalars; naive photon.
Subtractions: none. The quoted slope is a finite difference, F(0.4) - F(0.2) over 0.2 (and 0.2 -> 0.1 at N = 256)."""
import numpy as np, sys, time
sys.path.insert(0, '.')
from r162_laws import D1Law, GScal
from r162_dirac_scan import ce2
from r162_scalar import dc_scalar
t0 = time.time(); lam = 0.05
for b in (1.4, 1.0):
    for N in (192, 256):
        vals = {}
        for m in (0.8, 0.4, 0.2, 0.1):
            if N == 192 and m == 0.1: continue
            vals[m] = ce2(D1Law(b, 1/np.sqrt(3), None, None, m), N, lam, 0.02)[0]
        s = ' '.join('F(%.1f)=%+8.4f' % (m, v) for m, v in vals.items())
        print('Dirac D1(b=%.1f, r=1/sqrt3) N=%d: %s | slope(0.2..0.4) %+7.3f' % (b, N, s, (vals[0.4]-vals[0.2])/0.2)
              + (' slope(0.1..0.2) %+7.3f' % ((vals[0.2]-vals[0.1])/0.1) if 0.1 in vals else ''), flush=True)
    for N in (192, 256):
        vals = {}
        for m in (0.8, 0.4, 0.2, 0.1):
            if N == 192 and m == 0.1: continue
            vals[m] = dc_scalar(GScal(b, None, None, m), N, lam, 0.02)[0]
        s = ' '.join('F(%.1f)=%+8.4f' % (m, v) for m, v in vals.items())
        print('Scalar G(b=%.1f) N=%d: %s | slope(0.2..0.4) %+7.3f' % (b, N, s, (vals[0.4]-vals[0.2])/0.2)
              + (' slope(0.1..0.2) %+7.3f' % ((vals[0.2]-vals[0.1])/0.1) if 0.1 in vals else ''), flush=True)
print('elapsed %.1fs' % (time.time() - t0))
