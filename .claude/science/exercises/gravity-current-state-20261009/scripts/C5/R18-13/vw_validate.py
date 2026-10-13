"""R18-13: check vwface's geometric extension against R17-12's archived r1712_lib (VWa) on the axis, term by term in Xi."""
import os, sys, numpy as np, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, '..', 'arch18'))
from r1712_lib import xi, photonGw
import vwface as V
bg, fw, a = 2.9435, 1.0, -0.1760950036
law = photonGw(bg, fw*(np.pi - bg))
for N in (32, 48):
    for pol in ('T2g', 'Eg'):
        t0 = time.time(); ref = xi(law, N, pol, 'VWa', lam=a)[0]; mine = V.xi_geo(law, N, pol, a)[0]
        print('N=%d %s: r1712_lib %+.12e  vwface-geo %+.12e  diff %+.2e (%.1fs)' % (N, pol, ref, mine, mine - ref, time.time() - t0), flush=True)
