"""R17-12 (c): SM-count solve with the covariant W1-forward-correct family VWa (one common stencil a for every
half-integer-height product, weights (1-a) at z +- 1/2 and a at z +- 3/2; a in [0, 1] keeps both weights >= 0).
7 knobs: (b_g, fw_g, b_f, r, b_s, fr_s, a).  Content and matter vertices as R17-9."""
import numpy as np, sys, time
from r1712_lib import xi, photonGw
from content3 import ferm
from content4 import scalw
from zz import mu_E
from scipy.optimize import least_squares
Ng = int(sys.argv[1]); x0 = np.array([float(v) for v in sys.argv[2].split(',')]); m = float(sys.argv[4]) if len(sys.argv) > 4 else 0.01
nfev = int(sys.argv[3]) if len(sys.argv) > 3 else 40
NS, ND, NV = 4.0, 22.5, 12.0
t0 = time.time()
def phot(bg, fwg, a, N=Ng):
    law = photonGw(bg, fwg*(np.pi - bg))
    T = xi(law, N, 'T2g', 'VWa', lam=a)[0]; E = xi(law, N, 'Eg', 'VWa', lam=a)[0]
    g, f = law.samples(1 << 14)
    return np.array([T, E, 2*mu_E(g, f, 1e-3), 0.0])
def parts(z, N=Ng):
    bg, fwg, bf, r, bs, frs, a = z
    return NS*scalw(bs, frs, m, vert='U')[0], ND*ferm(bf, r, m)[0], NV*phot(bg, fwg, a, N)
def tot(z, N=Ng):
    s, f, v = parts(z, N); return s + f + v
lo = [0.15, 0.05, 0.15, 0.02, 0.3, 0.02, 0.0]; hi = [1.5, 1.0, 1.55, 0.5773, 3.0, 1.0, 1.0]
res = least_squares(lambda z: tot(z)[:3]*1e2, x0, bounds=(lo, hi), xtol=1e-14, ftol=1e-14, gtol=1e-14, diff_step=1e-5, max_nfev=nfev)
z = res.x; s, F, V = parts(z)
print('VWa solve, photon grid N=%d, m=%g, nfev %d, %.1fs, status %d, start %s' % (Ng, m, res.nfev, time.time()-t0, res.status, sys.argv[2]))
print('knobs b_g=%.8f w_g=%.8f b_f=%.8f r=%.8f b_s=%.8f w_s=%.8f a=%.8f (lam=%.6f)' % (z[0], z[1]*(np.pi-z[0]), z[2], z[3], z[4], z[5]*(np.pi-z[4]), z[6], 0.25 + 2*z[6]))
print('raw z:', ','.join('%.10f' % v for v in z))
print('4 scalars (T2g,Eg,muE,muT2):', s); print('22.5 Dirac:', F); print('12 vectors:', V)
t = s + F + V; print('TOTAL Xi_T2g %+.3e Xi_Eg %+.3e mu_E %+.3e | mu_T2 %+.3e' % tuple(t))
at_bound = [i for i in range(7) if abs(z[i]-lo[i]) < 1e-6 or abs(z[i]-hi[i]) < 1e-6]; print('knobs at bounds:', at_bound)
np.save('smroot_VWa1_N%d.npy' % Ng, z)
