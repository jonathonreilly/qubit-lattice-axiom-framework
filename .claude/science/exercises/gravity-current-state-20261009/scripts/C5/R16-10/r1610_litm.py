"""R16-10 (d): small-m behaviour of F_1/2 on the literal edge (massless corner valleys at m -> 0), at the zero law
literal(2,3) + R85(1,2,G=2.8925) and at G = 1. Compare with D1 (gapped corners)."""
import numpy as np, time
from r1610_eval import *
from r1610_laws import *
t0 = time.time()
for lab, matter, G in [('lit(2,3)', dirac_lit(2.0, 3.0), 2.8925), ('lit(2,3)', dirac_lit(2.0, 3.0), 1.0), ('D1(1.4,1/sqrt3)', dirac_D1(1.4, 1/np.sqrt(3)), 3.1264)]:
    d = photon('R85', 1.0, 2.0, G)
    for N in (64, 128):
        row = []
        for m in (1e-6, 0.005, 0.01, 0.02, 0.04):
            row.append(K[0.5] + lattice_part(0.5, N, m, 0.0, matter, d, 0.25, 0.7, 0.02)[0])
        print('%-16s G=%.4f N=%3d  F(m = 0, .005, .01, .02, .04) = %s' % (lab, G, N, ' '.join('%+.5f' % x for x in row)), flush=True)
print('elapsed %.1fs' % (time.time() - t0))
