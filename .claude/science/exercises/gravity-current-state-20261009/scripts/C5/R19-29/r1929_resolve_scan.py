"""R19-29 (c), lam_nn = 0 branch: scan the Schur-completed face1 total over w_d using the exactly-linear kappa(w_d), c4(w_d)
fitted in resolve_N128.out (photon Ng = 128; scalar+Dirac at N = 128); separates roots from the pole c4 + 8X = 0."""
import numpy as np
from scipy.optimize import brentq
wd0, J11 = -1.171554, 1.67645
pk = [-1.67837513e-06, 2.24653706e+00, 1.35124289e+00]; pc = [-3.35674389e-06, 2.28250037e+00, -2.52201334e-01]; X = 1.754162e-01
kap = lambda w: np.polyval(pk, w); den = lambda w: np.polyval(pc, w) + 8*X
f = lambda w: J11*(w - wd0) - kap(w)**2/den(w)
wp = brentq(den, -2, 1); wk = brentq(kap, -2, 1)
print('kappa = 0 at w_d = %+.5f ; c4 + 8X = 0 (gauge-block singular, leading-order Schur invalid) at w_d = %+.5f' % (wk, wp))
for w in np.r_[np.linspace(-3, wp - 1e-3, 8), np.linspace(wp + 1e-3, 1.0, 12)]:
    print('   w_d=%+.4f  kappa=%+.4f  c4+8X=%+.4f  Schur term=%+.4e  phys face1=%+.4e' % (w, kap(w), den(w), -kap(w)**2/den(w), f(w)))
g = np.linspace(wp + 1e-6, 3.0, 20001); fv = f(g)
roots = [brentq(f, g[i], g[i+1]) for i in range(len(g)-1) if fv[i]*fv[i+1] < 0]
g2 = np.linspace(-6, wp - 1e-6, 20001); fv2 = f(g2)
roots += [brentq(f, g2[i], g2[i+1]) for i in range(len(g2)-1) if fv2[i]*fv2[i+1] < 0]
for r in roots:
    h = 1e-6; d = (f(r + h) - f(r - h))/(2*h)
    print('root w_d = %+.5f (distance to the singular point %+.4f): d face1_phys/d w_d = %+.4f; det J (x w_o column 6.94286) = %+.4f' % (r, r - wp, d, d*6.94286))
