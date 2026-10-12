"""R11-1 (a): photon pairing does not imply TT pairing.  Bosons on the fermion's own curve v (photon coefficient then
cancels exactly, Theorem P) but with the minimal-metric TT vertex w = v (R9-9 member M) instead of the pairing vertex w = S^2."""
import numpy as np, sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from r111_necessity import fermion_band, C_photon, C_tt
from r101_pairing_copy import make_box_curve, wilson_curve
for name, cur in [('Wilson', wilson_curve()), ('box0.8', make_box_curve(0.8, 1.6))]:
    f = fermion_band(cur)
    bM = dict(u=f['u'], up=f['up'], A=f['A'], w=f['u'])          # TT vertex w = v (metric member M)
    for m in [1.0, 0.3, 0.05]:
        ph = 4 * C_photon(bM, m, 1 / 32) + C_photon(f, m, -1 / 8)
        tt = 4 * C_tt(bM, m, 2 * 4 / 32) + C_tt(f, m, -1.0)
        print('%-7s m=%.2f: photon C = %+.2e (paired curve) | TT T_2g with boson vertex w = v: C = %+.4e (x16pi^2 = %+.4f)' % (name, m, ph, tt, tt * 16 * np.pi ** 2))
