import sys, time; sys.path.insert(0, '.')
import numpy as np
from r161_onshell_aniso import qx_nodes, dce_aniso, U
from r137_onshell import ce2_minus_1
from r161_laws import D1Law, BQLaw
lam = 0.05; t0 = time.time()
# consistency: aniso runner == R13-7 runner on a uniform midpoint q_x grid (S3 gapped, m = 1, N = 48)
law = BQLaw(2.0, 3.0, 1.0, 1.0, (2.0, 3.0))
N = 48; qmid = (np.arange(N) + 0.5) * 2 * np.pi / N - np.pi
a = dce_aniso(law, N, lam, qmid, np.full(N, 2 * np.pi / N)) * U
ce, _, _ = ce2_minus_1(law, N, lam, h=0.02)
print('consistency (S3 gapped, m=1, N=48 midpoint): aniso %+.8f  R13-7 runner %+.8f' % (a, ce / 2 * U), flush=True)
for npan in (64, 128):
    qxn, qxw = qx_nodes(npan, 8)
    for Np in (48, 64, 96):
        ms = (25.6, 51.2, 102.4); v = [dce_aniso(D1Law(1.4, 1 / np.sqrt(3), m), Np, lam, qxn, qxw) * U for m in ms]
        A = np.array([[m, 1, 1 / m] for m in ms]); Lf, c0, c1 = np.linalg.solve(A, np.array(v))
        print('D1(1.4,1/sqrt3) naive  qx: %d GL panels x8, Np=%d: dc_e*U at 25.6/51.2/102.4 = %+.4f %+.4f %+.4f | fit L*U=%+.5f c0=%+.3f c1=%+.2f  [%.0fs]'
              % (npan, Np, *v, Lf, c0, c1, time.time() - t0), flush=True)
