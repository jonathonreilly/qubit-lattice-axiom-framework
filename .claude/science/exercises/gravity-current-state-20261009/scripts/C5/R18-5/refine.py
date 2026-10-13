"""R18-5: high-resolution re-solve of an SM-count end point: free knobs (b_g, a, fr_s) [indices 0, 6, 5]; others frozen.
Photon grid N (argv), Dirac GL (4,10), scalar U as before.  m = 0.01."""
import numpy as np, sys, time
from scipy.optimize import least_squares
from smud_lib import dirac, phot, scal, NS, ND, NV
z0 = np.load(sys.argv[1]); N = int(sys.argv[2]); tag = sys.argv[3]; t0 = time.time()
free = [0, 6, 5]
bf, r = z0[2], z0[3]
F = ND*dirac(bf, r, q=(4, 10))
def full(x):
    z = z0.copy(); z[free] = x; return z
def tot(z, NN=N):
    bg, fwg, bf_, r_, bs, frs, a = z
    s = NS*scal(bs, frs*(np.pi - bs)); V = NV*phot(bg, fwg*(np.pi - bg), NN, 'VWa', a)
    return s, F, V
def resid(x):
    s, F_, V = tot(full(x)); return (s + F_ + V)[:3]*1e2
res = least_squares(resid, z0[free], xtol=1e-15, ftol=1e-15, gtol=1e-15, diff_step=1e-6, max_nfev=30)
z = full(res.x); s, F_, V = tot(z)
print('[%s] refine at photon N=%d, Dirac GL(4,10): status %d nfev %d %.0fs' % (tag, N, res.status, res.nfev, time.time()-t0))
print('knobs b_g=%.10f w_g=%.10f b_f=%.10f r=%.10f b_s=%.10f w_s=%.10f a=%.10f (lam=%.8f)' % (z[0], z[1]*(np.pi-z[0]), z[2], z[3], z[4], z[5]*(np.pi-z[4]), z[6], 0.25+2*z[6]))
print('raw z:', ','.join('%.12f' % v for v in z))
print('4 scalars:', s); print('22.5 Dirac (UD):', F_); print('12 vectors (VWa):', V)
t = s + F_ + V; print('TOTAL Xi_T2g %+.3e Xi_Eg %+.3e mu_E %+.3e | mu_T2 %+.3e' % tuple(t))
J = res.jac/1e2; print('Jacobian (rows T2g,Eg,muE; cols b_g,a,fr_s):\n', J, '\ndet %.3e' % np.linalg.det(J))
np.save('smroot_%s.npy' % tag, z)
