"""R19-11 (b): DIRECT re-evaluation of the photon (VWa-geo, archived vwface) face rows at the m->0+ root's a and solved (w_d, w_o),
N = 224, and the face totals with the scalar (m = 1e-5) and Dirac (m = 0, GL(4,10)) values of fsolve0.out."""
import os, sys, time, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, '..', 'arch18_13')); sys.path.insert(1, os.path.join(HERE, '..', 'arch18'))
import vwface as V
from photon import photonGw
a, wd, wo, N = -0.1761772299, -1.17171474, -0.19556642, 224
s1, s2, d1, d2 = -4.646720e-04, -6.368017e-04, +1.190214e-03, +2.195877e-03
law = photonGw(2.9435, np.pi - 2.9435); t0 = time.time()
G1 = V.xi_geo(law, N, 'face1', a, ((wd, wo),), (1, 2))[0]; G2 = V.xi_geo(law, N, 'face2', a, ((wd, wo),), (1, 2))[0]
print('per vector at solved data: face1 %+.10e face2 %+.10e | TOTALS face1 %+.3e face2 %+.3e [%.0fs]' % (G1, G2, 4*s1 + 22.5*d1 + 12*G1, 4*s2 + 22.5*d2 + 12*G2, time.time()-t0))
