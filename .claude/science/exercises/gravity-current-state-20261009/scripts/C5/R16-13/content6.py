"""R16-13: content n1 real scalars on G(b1) + n2 real scalars on G_w(b2, w2) + ND Dirac on D1(bf, r) [M vertex, V0].
Knobs (b1, b2, w2-frac, bf, r). Two scalar edge families (not SM-like: a Higgs doublet would share one edge)."""
import numpy as np, sys, time
from content3 import ferm
from content4 import scalw
from scipy.optimize import least_squares
n1, n2, ND, m = (float(v) for v in sys.argv[1:5])
x0 = np.array([float(v) for v in sys.argv[5].split(',')])
t0 = time.time()
def tot(z):
    b1, b2, fr2, bf, r = z
    return n1*scalw(b1, 1.0, m)[0] + n2*scalw(b2, fr2, m)[0] + ND*ferm(bf, r, m)[0]
res = least_squares(lambda z: tot(z)[:3]*1e3, x0, bounds=([0.3, 0.3, 0.02, 0.3, 0.02], [3.0, 3.0, 1.0, 1.55, 0.5773]),
                    xtol=1e-15, ftol=1e-15, gtol=1e-15, diff_step=1e-6, max_nfev=150)
b1, b2, fr2, bf, r = res.x; t = tot(res.x)
print('content %g G(b1) + %g G_w(b2,w2) real scalars + %g D1 Dirac, m=%g (nfev %d, %.1fs)' % (n1, n2, ND, m, res.nfev, time.time()-t0))
print('knobs b1=%.10f b2=%.10f w2=%.10f (frac %.6f) bf=%.10f r=%.10f' % (b1, b2, fr2*(np.pi-b2), fr2, bf, r))
print('s1:', scalw(b1, 1.0, m)[0][:3], ' s2:', scalw(b2, fr2, m)[0][:3], ' f:', ferm(bf, r, m)[0])
print('TOTAL: Xi_T2g %+.3e Xi_Eg %+.3e mu_E %+.3e | mu_T2 %+.3e' % tuple(t))
np.save('root6_%g_%g_%g.npy' % (n1, n2, ND), np.array([n1, n2, ND, m, *res.x]))
