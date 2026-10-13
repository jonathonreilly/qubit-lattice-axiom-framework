"""R17-9 calibration: (i) continuum helicity-2 check of the photon pair amplitude; (ii) the grid-shift pipeline on a real U scalar
against zz.py's closed form (R16-3/R17-4 rechecked); (iii) photon Xi convergence on gammaG(1.4) and gammaNN."""
import numpy as np, time
from photon import *
from zz import ZLaw, xi_all
t0 = time.time()
print('(i) continuum q=0 photon pair weight vs helicity-2 formula, worst rel. dev: %.2e' % continuum_check())
L = ZLaw([1.0, 0.0], [1.4 + (np.pi-1.4)/2], np.pi-1.4); g, f = L.samples(1 << 14)
for m in (0.3, 0.1):
    x = xi_all(g, f, m)
    gfun = lambda k: (np.interp(np.abs(k), L.k, L.sig)**2, np.sign(k)*np.interp(np.abs(k), L.k, L.sig)*np.interp(np.abs(k), L.k, L.sp))
    for N in (64, 128, 256):
        r = [scalar_xi_grid(gfun, N, p, m) for p in ('T2g', 'Eg')]
        print('(ii) G(1.4) U scalar m=%.1f N=%d grid-shift Xi_T2g %+.5e Xi_Eg %+.5e | closed form %+.5e %+.5e' % (m, N, r[0][0], r[1][0], x['U,T2g'], x['U,Eg']))
for law in (photonG(1.4), photonNN()):
    for N in (32, 48, 64):
        t1 = time.time()
        r = [photon_xi(law, N, p) for p in ('T2g', 'Eg')]
        print('(iii) %s N=%d Xi_T2g %+.5e (a %+.4e b %+.4e)  Xi_Eg %+.5e (a %+.4e b %+.4e)  %.1fs' % (law.name, N, r[0][0], r[0][1], r[0][2], r[1][0], r[1][1], r[1][2], time.time()-t1))
print('elapsed %.1fs' % (time.time()-t0))
