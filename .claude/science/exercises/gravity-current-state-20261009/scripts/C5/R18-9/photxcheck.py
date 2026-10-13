"""R18-9 (b): photon Xi at the root's photon edge and stencil, with different q-extrapolation shift pairs (R17-12's xi uses (1,2)),
at N (argv). Tests the q -> 0 extrapolation, independent of the grid-convergence check."""
import sys, time, numpy as np, lib9 as L
from r1712_lib import xi, photonGw
N = int(sys.argv[1]); bg, fw, a = 2.9435, 1.0, float(sys.argv[2]); law = photonGw(bg, fw*(np.pi - bg)); t0 = time.time()
for sh in ((1, 2), (1, 3), (2, 4)):
    T = xi(law, N, 'T2g', 'VWa', shifts=sh, lam=a)[0]; E = xi(law, N, 'Eg', 'VWa', shifts=sh, lam=a)[0]
    print('N=%d shifts %s: per vector Xi_T2g %+.6e Xi_Eg %+.6e ; x12: %+.4e %+.4e [%.0fs]' % (N, sh, T, E, 12*T, 12*E, time.time()-t0), flush=True)
