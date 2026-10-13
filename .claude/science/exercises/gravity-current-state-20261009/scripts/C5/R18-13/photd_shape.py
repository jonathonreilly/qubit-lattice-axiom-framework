"""R18-13 (suggested-level probe of shape payment): photon d1, d2 per vector (VWa-geo, a = root value) across photon edges
gammaGw(b, fw*(pi-b)) at grid N."""
import os, sys, time, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', 'arch18'))
import vwface as V
from photon import photonGw
N = int(sys.argv[1]); a = -0.1760950036
for spec in sys.argv[2].split(';'):
    b, fw = (float(v) for v in spec.split(',')); law = photonGw(b, fw*(np.pi - b)); t0 = time.time()
    r = {row: V.xi_geo(law, N, row, a, ((0.0, 0.0),))[0] for row in ('T2g', 'Eg', 'face1', 'face2')}
    print('N=%d gammaGw(%.3f, fw=%.2f) a=%+.6f per vector: T2g %+.4e Eg %+.4e | d1 %+.5e d2 %+.5e (%.0fs)'
          % (N, b, fw, a, r['T2g'], r['Eg'], r['face1'] - (3*r['Eg'] + r['T2g'])/4, r['face2'] - r['T2g'], time.time() - t0), flush=True)
