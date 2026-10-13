"""R18-13: off-axis covariance control for VWa-geo: the face rows along (1,1,0), (0,1,1), (1,0,1) and (1,-1,0) must agree
(cubic images), at (wd, wo) = (0,0) and (1,0), (0,1). Root edge, a = -0.1760950036."""
import os, sys, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', 'arch18'))
import vwface as V
from photon import photonGw
law = photonGw(2.9435, np.pi - 2.9435); a = -0.1760950036; N = int(sys.argv[1])
r2 = np.sqrt(2.0)
cases = {'(1,1,0)': ((1, 1, 0), np.array([1, -1, 0])/r2, np.array([0, 0, 1.0])),
         '(0,1,1)': ((0, 1, 1), np.array([0, 1, -1])/r2, np.array([1.0, 0, 0])),
         '(1,0,1)': ((1, 0, 1), np.array([1, 0, -1])/r2, np.array([0, 1.0, 0])),
         '(1,-1,0)': ((1, -1, 0), np.array([1, 1, 0])/r2, np.array([0, 0, 1.0]))}
sets = ((0.0, 0.0), (1.0, 0.0), (0.0, 1.0))
for name, (d, av, bv) in cases.items():
    V.POL['f1'] = np.outer(av, av) - np.outer(bv, bv); V.POL['f2'] = np.outer(av, bv) + np.outer(bv, av)
    V.DIRS['f1'] = d; V.DIRS['f2'] = d
    f1 = V.xi_geo(law, N, 'f1', a, sets); f2 = V.xi_geo(law, N, 'f2', a, sets)
    print('N=%d dir %-9s face1 %+.10e face2 %+.10e | d/dwd %+.6e %+.6e | d/dwo %+.6e %+.6e' % (N, name, f1[0], f2[0], f1[1]-f1[0], f2[1]-f2[0], f1[2]-f1[0], f2[2]-f2[0]), flush=True)
