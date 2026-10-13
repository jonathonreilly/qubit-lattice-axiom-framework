"""R17-12 (c): R17-9's SM-count solve (C5_R17-9 smsolve.py, content and knobs unchanged) with the vector vertex replaced by
the W1-forward-correct covariant VW0 (nearest symmetric placement).  4 real scalars G_w(b_s,w_s) [U, SF]; 22.5 Dirac
D1(b_f,r) [V0, SF]; 12 vectors gammaGw(b_g,w_g) [VW0; SF shear 2 x scalar formula].  m = 0.01.  Rows Xi_T2g, Xi_Eg, mu_E."""
import numpy as np, sys, time
from r1712_lib import xi, photonGw
from content3 import ferm
from content4 import scalw
from zz import mu_E
from scipy.optimize import least_squares
var = sys.argv[1]; Ng = int(sys.argv[2]); x0 = np.array([float(v) for v in sys.argv[3].split(',')]); m = 0.01
nfev = int(sys.argv[4]) if len(sys.argv) > 4 else 40
NS, ND, NV = 4.0, 22.5, 12.0
t0 = time.time()
def phot(bg, fwg, N=Ng):
    law = photonGw(bg, fwg*(np.pi - bg))
    T = xi(law, N, 'T2g', var)[0]; E = xi(law, N, 'Eg', var)[0]
    g, f = law.samples(1 << 14)
    return np.array([T, E, 2*mu_E(g, f, 1e-3), 0.0])
def parts(z, N=Ng):
    bg, fwg, bf, r, bs, frs = z
    return NS*scalw(bs, frs, m, vert='U')[0], ND*ferm(bf, r, m)[0], NV*phot(bg, fwg, N)
def tot(z, N=Ng):
    a, b, c = parts(z, N); return a + b + c
lo = [0.15, 0.05, 0.15, 0.02, 0.3, 0.02]; hi = [1.5, 1.0, 1.55, 0.5773, 3.0, 1.0]
res = least_squares(lambda z: tot(z)[:3]*1e2, x0, bounds=(lo, hi), xtol=1e-14, ftol=1e-14, gtol=1e-14, diff_step=1e-5, max_nfev=nfev)
z = res.x; s, F, V = parts(z)
print('vertex %s, photon grid N=%d, nfev %d, %.1fs, status %d, start %s' % (var, Ng, res.nfev, time.time()-t0, res.status, sys.argv[3]))
print('knobs b_g=%.8f w_g=%.8f b_f=%.8f r=%.8f b_s=%.8f w_s=%.8f' % (z[0], z[1]*(np.pi-z[0]), z[2], z[3], z[4], z[5]*(np.pi-z[4])))
print('raw z:', ','.join('%.10f' % v for v in z))
print('4 scalars (T2g,Eg,muE,muT2):', s); print('22.5 Dirac:', F); print('12 vectors:', V)
t = s + F + V; print('TOTAL Xi_T2g %+.3e Xi_Eg %+.3e mu_E %+.3e | mu_T2 %+.3e' % tuple(t))
at_bound = [i for i in range(6) if abs(z[i]-lo[i]) < 1e-6 or abs(z[i]-hi[i]) < 1e-6]; print('knobs at bounds:', at_bound)
