"""R16-1 (d): third resolution (12,8) of the Q_W^P legs on a mass subset; selectron with Nref = 4096 (q << m)."""
import sys, time; sys.path.insert(0, '.')
import numpy as np
from r161_laws import D1Law
from r161_mscan import axis_nodes
from r161_partner_gl import selectron_gl, dc_partner_gl
U = 16 * np.pi ** 2; t0 = time.time()
for (lx, lp) in ((12, 8),):
    nx, wx = axis_nodes(1.4, lx); ny, wy = axis_nodes(1.4, lp)
    for m in (0.01, 0.1, 0.8, 3.0, 25.6):
        law = D1Law(1.4, 1 / np.sqrt(3), m)
        dS, _ = selectron_gl(law, nx, wx, ny, wy, Nref=4096)
        pa = 2.0 * dc_partner_gl(law, nx, wx, ny, wy)
        print('m=%7.3f | (%d,%d) | dcg_2sel(Nref=4096)=%+10.5f | dce_partner=%+10.5f   [%.0fs]' % (m, lx, lp, 2 * dS * U, pa * U, time.time() - t0), flush=True)
