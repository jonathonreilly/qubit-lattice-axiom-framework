"""R16-1 (d)+(c) for Q_W^P on D1(1.4, 1/sqrt3), naive photon, lam irrelevant for these legs (no photon line):
two matched selectrons' photon coefficient and the selectron-photino Yukawa loop, on the r161_mscan GL panels.
Combine with r161_mscan.out (electron photon loop dc_e and Dirac dc_gamma) for
  (P-a) selectrons only:      Delta^Pa = dc_e(photon loop) - dc_gamma(Dirac) - dc_gamma(2 sel)
  (P-b) R13-1 minimal SQED:   Delta^Pb = Delta^Pa + dc_e(partner loop)."""
import sys, time; sys.path.insert(0, '.')
import numpy as np
from r161_laws import D1Law
from r161_mscan import axis_nodes
from r161_partner_gl import selectron_gl, dc_partner_gl
U = 16 * np.pi ** 2
levels = [(6, 4), (8, 6)] if len(sys.argv) < 2 else [tuple(int(x) for x in sys.argv[1].split(','))]
ms = [0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.4, 0.8, 1.2, 1.6, 2.0, 2.5, 3.0, 6.4, 12.8, 25.6]
t0 = time.time()
print('D1(1.4,1/sqrt3) naive photon; m | level | dc_gamma(2 selectrons)*U | dc_e(partner loop, y^2=2e^2)*U')
for (lx, lp) in levels:
    nx, wx = axis_nodes(1.4, lx); ny, wy = axis_nodes(1.4, lp)
    for m in ms:
        law = D1Law(1.4, 1 / np.sqrt(3), m)
        dS, _ = selectron_gl(law, nx, wx, ny, wy, Nref=256)
        pa = 2.0 * dc_partner_gl(law, nx, wx, ny, wy)
        print('m=%7.3f | (%d,%d) | dcg_2sel=%+10.5f | dce_partner=%+10.5f   [%.0fs]' % (m, lx, lp, 2 * dS * U, pa * U, time.time() - t0), flush=True)
