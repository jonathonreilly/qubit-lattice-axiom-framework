"""Theorem W closed form vs on-shell fits for two more members of Q_W^+: D1(1.0, 1/sqrt3) and BQ S3 r=1 with the naive photon;
and D1(1.4, 1/sqrt3) with photon box (0.7, 1.4)."""
import sys, time; sys.path.insert(0, '.')
import numpy as np
from r161_laws import D1Law, BQLaw
from r161_heavy import L_photon_slot, U
from r161_onshell_aniso import qx_nodes, dce_aniso
lam = 0.05; t0 = time.time()
for lab, mk in (('D1(1.0,1/sqrt3) naive', lambda m: D1Law(1.0, 1 / np.sqrt(3), m)),
                ('D1(1.4,1/sqrt3) photon (0.7,1.4)', lambda m: D1Law(1.4, 1 / np.sqrt(3), m, (0.7, 1.4))),
                ('BQ S3 r=1 naive', lambda m: BQLaw(2.0, 3.0, 1.0, m, 'naive'))):
    Lc = L_photon_slot(mk(1.0), lam, Np=64) * U
    for npan, Np in ((64, 64), (96, 96)):
        qxn, qxw = qx_nodes(npan, 8)
        ms = (25.6, 51.2, 102.4); v = [dce_aniso(mk(m), Np, lam, qxn, qxw) * U for m in ms]
        A = np.array([[m, 1, 1 / m] for m in ms]); Lf, c0, c1 = np.linalg.solve(A, np.array(v))
        print('%-34s qx %d panels Np=%d: on-shell fit L*U=%+.5f (c0=%+.3f c1=%+.2f) | closed form %+.5f   [%.0fs]' % (lab, npan, Np, Lf, c0, c1, Lc, time.time() - t0), flush=True)
