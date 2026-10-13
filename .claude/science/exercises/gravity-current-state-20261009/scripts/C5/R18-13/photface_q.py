"""R18-13: q-extrapolation check of the photon off-axis rows (VWa-geo, root edge, (wd, wo) = (0, 0)) at grid N, shift pair given."""
import os, sys, time, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', 'arch18'))
import vwface as V
from photon import photonGw
law = photonGw(2.9435, np.pi - 2.9435); a = -0.1760950036
N = int(sys.argv[1])
for sh in sys.argv[2].split(';'):
    shifts = tuple(int(v) for v in sh.split(',')); t0 = time.time()
    r = {row: V.xi_geo(law, N, row, a, ((0.0, 0.0),), shifts)[0] for row in ('face1', 'face2')}
    print('N=%d shifts=%s per vector: face1 %+.9e face2 %+.9e (%.0fs)' % (N, shifts, r['face1'], r['face2'], time.time() - t0), flush=True)
