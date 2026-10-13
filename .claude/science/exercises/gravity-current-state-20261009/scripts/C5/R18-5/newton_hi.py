"""R18-5: convergence of the C96 root in the photon grid (N = 96, 128, 160) and Dirac quadrature (GL (4,10) vs (5,12));
one Newton step at N = 160 with the N = 96 Jacobian (cols b_g, a, fr_s), then re-evaluation at N = 160 and N = 192."""
import numpy as np, time
from smud_lib import dirac, phot, scal, NS, ND, NV
t0 = time.time(); z = np.load('smroot_C96.npy'); free = [0, 6, 5]
J = np.array([[1.86559085e-01, 2.06332419e+00, -2.54668636e-04], [2.88238625e-01, 4.09608970e+00, 2.23520972e-04], [1.99883800e-02, 0.0, 1.98958460e-02]])
F = ND*dirac(z[2], z[3], q=(4, 10)); F5 = ND*dirac(z[2], z[3], q=(5, 12))
print('Dirac GL(4,10):', F, ' GL(5,12)-GL(4,10):', F5 - F)
def tot(z, N):
    bg, fwg, bf, r, bs, frs, a = z
    return NS*scal(bs, frs*(np.pi - bs)) + F5 + NV*phot(bg, fwg*(np.pi - bg), N, 'VWa', a)
for N in (96, 128, 160):
    t = tot(z, N); print('C96 knobs, photon N=%d: TOTAL T2g %+.3e Eg %+.3e muE %+.3e  [%.0fs]' % (N, t[0], t[1], t[2], time.time()-t0), flush=True)
dx = -np.linalg.solve(J, t[:3]); z2 = z.copy(); z2[free] += dx
print('Newton step (b_g, a, fr_s):', dx)
for N in (160, 192):
    t = tot(z2, N); print('stepped knobs, photon N=%d: TOTAL T2g %+.3e Eg %+.3e muE %+.3e | mu_T2 %+.3e [%.0fs]' % (N, t[0], t[1], t[2], t[3], time.time()-t0), flush=True)
print('stepped raw z:', ','.join('%.12f' % v for v in z2)); np.save('smroot_C160.npy', z2)
