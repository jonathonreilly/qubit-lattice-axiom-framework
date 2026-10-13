"""R18-9 (b): photon mu_E^gamma regulator and quadrature dependence at the root's photon edge (convention: 2 x scalar mu_E at regulator 1e-3)."""
import numpy as np, lib9 as L
from photon import photonGw
from zz import mu_E
law = photonGw(2.9435, np.pi - 2.9435)
for n in (1 << 14, 1 << 16):
    g, f = law.samples(n)
    print('n=2^%d: ' % int(np.log2(n)) + '  '.join('reg %.0e: %+.8e' % (mreg, 2*mu_E(g, f, mreg)) for mreg in (1e-2, 3e-3, 1e-3, 3e-4, 1e-4)))
g, f = law.samples(1 << 14); print('nu=3000 at reg 1e-3: %+.8e' % (2*mu_E(g, f, 1e-3, nu=3000)))
