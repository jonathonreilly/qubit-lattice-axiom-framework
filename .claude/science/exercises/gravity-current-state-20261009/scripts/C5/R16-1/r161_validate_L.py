"""Validate Theorem W's closed form L against R13-7's on-shell runner at large m (BQ gapped S1, S3 with
R8-5's overlapping photon boxes; D1(1.4, 1/sqrt3) naive photon). Fit dc_e(m) = L m + c0 + c1/m on m = 25.6, 51.2, 102.4."""
import sys, time; sys.path.insert(0, '.')
import numpy as np
from r137_onshell import ce2_minus_1, U
from r161_laws import D1Law, BQLaw
from r161_heavy import L_photon_slot, L_p_difference
lam = 0.05
t0 = time.time()
laws = [('S1 gapped (BQ r=1, photon (1,2))', lambda m: BQLaw(1.0, 2.0, 1.0, m, (1.0, 2.0))),
        ('S3 gapped (BQ r=1, photon (2,3))', lambda m: BQLaw(2.0, 3.0, 1.0, m, (2.0, 3.0))),
        ('D1(b=1.4, r=1/sqrt3), naive photon', lambda m: D1Law(1.4, 1 / np.sqrt(3), m))]
for lab, mk in laws:
    for N in (48, 64):
        ms = (25.6, 51.2, 102.4); v = []
        for m in ms:
            ce, ct, _ = ce2_minus_1(mk(m), N, lam, h=0.02); v.append(ce / 2 * U)
        Amat = np.array([[m, 1, 1 / m] for m in ms]); L_fit, c0, c1 = np.linalg.solve(Amat, np.array(v))
        print('%-36s N=%2d on-shell dc_e*U at m=25.6/51.2/102.4: %+.4f %+.4f %+.4f | fit L*U=%+.5f c0=%+.3f c1=%+.2f'
              % (lab, N, *v, L_fit, c0, c1), flush=True)
    law = mk(1.0)
    Ls = L_photon_slot(law, lam, Np=64) * U
    Lp, a0 = L_p_difference(law, lam, Np=64)
    Ls96 = L_photon_slot(law, lam, Np=96, nx=800) * U
    print('%-36s closed form L*U: photon-slot %+.5f (Np=64), %+.5f (Np=96, nx=800); p-difference %+.5f (Np=64)'
          % (lab, Ls, Ls96, Lp * U), flush=True)
print('elapsed %.1fs' % (time.time() - t0))
