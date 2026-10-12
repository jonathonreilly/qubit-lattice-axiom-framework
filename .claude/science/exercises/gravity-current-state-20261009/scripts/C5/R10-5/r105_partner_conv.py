"""C5 R10-5 script 4b: convergence of the partner-loop electron speed (grid N, p-step h, mass m). Imports r105_partner_loop."""
import numpy as np, time, sys
sys.path.insert(0, '.')
import r105_partner_loop as P
from r101_pairing import make_box_curve, wilson_curve
t0 = time.time()
U = 16 * np.pi ** 2
for lab, ce, cl in [('Wilson/Wilson', wilson_curve(), wilson_curve()), ('box0.8/box0.8', make_box_curve(0.8, 1.6), make_box_curve(0.8, 1.6))]:
    for m, N, h in [(0.1, 96, 0.01), (0.1, 128, 0.005), (0.1, 160, 0.005), (0.05, 128, 0.005), (0.05, 160, 0.0025), (0.05, 192, 0.0025), (0.025, 192, 0.00125)]:
        r, d0 = P.dc(ce, cl, m, N, [P.B0 @ P.PL, P.B0 @ P.PR], h=h)
        print('  %-14s m=%.3f N=%3d h=%.5f | dc_e(partner, chiral) x16pi^2/y^2 = %+8.4f' % (lab, m, N, h, r * U), flush=True)
print('elapsed %.1fs' % (time.time() - t0))
