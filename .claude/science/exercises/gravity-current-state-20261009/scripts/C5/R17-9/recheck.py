"""R17-9 recheck of archived runners (R16-13 copies of R16-3 zz.py, R16-13 dfam/content3/content4) against reported numbers."""
import numpy as np, time
from zz import ZLaw, xi_all, mu_E
from content3 import ferm, scal
from content4 import scalw
t0 = time.time()
# (1) R16-13 s3.1: G(1.4), m=0.01: mu_E=+4.338e-3, Xi_M,T2g=-1.689e-3, Xi_M,Eg=-8.49e-4
L = ZLaw([1.0, 0.0], [1.4 + (np.pi-1.4)/2], np.pi-1.4); g, f = L.samples(1 << 14)
x = xi_all(g, f, 0.01); print('G(1.4) m=0.01:', {k: '%.4e' % v for k, v in x.items()}, 'mu_E %.4e' % mu_E(g, f, 0.01), '[R16-13: M,T2g -1.689e-3 M,Eg -8.49e-4 mu_E +4.338e-3]')
# (2) R17-4 s3.1: NN m=1: U,T2g -2.289166113e-4, U,Eg -6.883236561e-5, M,T2g -1.903007307e-3, M,Eg -8.301856729e-4
n = 1 << 14; kk = 2*np.pi*(np.arange(n)+0.5)/n - np.pi
x = xi_all(4*np.sin(kk/2)**2, np.sin(kk), 1.0); print('NN m=1:', {k: '%.9e' % v for k, v in x.items()}, '[R17-4: U,T2g -2.289166113e-4 U,Eg -6.883236561e-5 M,T2g -1.903007307e-3 M,Eg -8.301856729e-4]')
# (3) R16-13 root6 totals at the reported knobs (expect ~1e-14 and mu_T2 -3.538e-5)
b1, b2, fr2, bf, r = 2.5647270310, 1.7406074658, 0.529124, 1.3133236385, 0.5731174634
fr2 = 0.7412942016/(np.pi - b2)
tot = 2*scalw(b1, 1.0, 0.01)[0] + 2*scalw(b2, fr2, 0.01)[0] + ferm(bf, r, 0.01)[0]
print('R16-13 root6 totals (Xi_T2g, Xi_Eg, mu_E, mu_T2):', tot, '[R16-13: -3.2e-15 -1.9e-15 +5.6e-14 | -3.538e-5]')
print('  fermion part:', ferm(bf, r, 0.01)[0], '[R16-13: +5.511e-3 +2.801e-3 -2.690e-2 -3.538e-5]')
# (4) D1(1.4, 0.3) m=0.01 [R16-13 grid N=192: +5.464e-3 +2.831e-3 mu_E -2.95e-2 mu_T2 -1.16e-6]
print('D1(1.4,0.3) m=0.01 (GL):', ferm(1.4, 0.3, 0.01)[0])
# (5) U-vertex values of the R16-13 root scalars (Lemma M: M non-local)
for nm, (b, fr) in (('G(b1)', (b1, 1.0)), ('G_w(b2,w2)', (b2, fr2))):
    print('  %s U-vertex:' % nm, scalw(b, fr, 0.01, vert='U')[0], ' M-vertex:', scalw(b, fr, 0.01, vert='M')[0])
print('elapsed %.1fs' % (time.time()-t0))
