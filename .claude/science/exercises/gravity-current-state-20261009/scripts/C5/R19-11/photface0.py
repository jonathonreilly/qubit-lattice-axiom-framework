"""R19-11 (b): photon (VWa-geo, R18-13's archived vwface, unmodified) face rows at the root photon edge with stencil a (argv),
per vector, at own-direction data (0,0), (1,0), (0,1) -> values and the Lemma-O Jacobian. Massless photon: m-independent."""
import os, sys, time, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, '..', 'arch18_13')); sys.path.insert(1, os.path.join(HERE, '..', 'arch18'))
import vwface as V
from photon import photonGw
a = float(sys.argv[1]); N = int(sys.argv[2]); shifts = (1, 2)
law = photonGw(2.9435, np.pi - 2.9435); t0 = time.time()
sets = ((0.0, 0.0), (1.0, 0.0), (0.0, 1.0))
F1 = V.xi_geo(law, N, 'face1', a, sets, shifts); F2 = V.xi_geo(law, N, 'face2', a, sets, shifts)
print('a=%.10f N=%d per vector (wd,wo)=(0,0): face1 %+.10e face2 %+.10e | d/dwd %+.8e %+.8e | d/dwo %+.8e %+.8e [%.0fs]'
      % (a, N, F1[0], F2[0], F1[1]-F1[0], F2[1]-F2[0], F1[2]-F1[0], F2[2]-F2[0], time.time()-t0), flush=True)
np.save(os.path.join(HERE, 'photface0_N%d.npy' % N), np.r_[a, F1, F2])
