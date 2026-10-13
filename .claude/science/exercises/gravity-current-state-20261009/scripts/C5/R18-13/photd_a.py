"""R18-13: photon (VWa-geo) anisotropy rows d1 = face1 - (3Eg + T2g)/4 and d2 = face2 - T2g per vector as a function of the
stencil weight a (root edge). Under an identically conserved (superpotential) off-axis extension of the stencil, Lemma S says
d1, d2 would NOT depend on a; under the geometric extension they may."""
import os, sys, time, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', 'arch18'))
import vwface as V
from photon import photonGw
law = photonGw(2.9435, np.pi - 2.9435)
N = int(sys.argv[1])
for a in [float(v) for v in sys.argv[2].split(',')]:
    t0 = time.time()
    r = {row: V.xi_geo(law, N, row, a, ((0.0, 0.0),))[0] for row in ('T2g', 'Eg', 'face1', 'face2')}
    print('N=%d a=%+.6f per vector: T2g %+.6e Eg %+.6e face1 %+.6e face2 %+.6e | d1 %+.6e d2 %+.6e (%.0fs)'
          % (N, a, r['T2g'], r['Eg'], r['face1'], r['face2'], r['face1'] - (3*r['Eg'] + r['T2g'])/4, r['face2'] - r['T2g'], time.time() - t0), flush=True)
