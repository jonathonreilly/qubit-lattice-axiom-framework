"""R16-1: small-m control of the selectron photon leg's q-extrapolation (P_M needs q << m): Nref = 256, 1024, 4096."""
import sys, time; sys.path.insert(0, '.')
import numpy as np
from r161_laws import D1Law
from r161_mscan import axis_nodes
from r161_partner_gl import selectron_gl
U = 16 * np.pi ** 2; t0 = time.time()
nx, wx = axis_nodes(1.4, 6); ny, wy = axis_nodes(1.4, 4)
for m in (0.005, 0.01, 0.02, 0.05, 0.1, 0.2):
    law = D1Law(1.4, 1 / np.sqrt(3), m)
    v = [2 * selectron_gl(law, nx, wx, ny, wy, Nref=Nr)[0] * U for Nr in (256, 1024, 4096)]
    print('m=%.3f  dcg_2sel*U  Nref=256: %+.5f  1024: %+.5f  4096: %+.5f   [%.0fs]' % (m, *v, time.time() - t0), flush=True)
