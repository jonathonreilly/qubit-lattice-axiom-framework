"""F4 validation: (i) M = 1 W-average reproduces F1's dm_sf (Psym) at t = 0 and t = 0.05; (ii) Ward identity for every family
at t = 0.3; (iii) at t = 0 every family gives the same dm (separable law: all families agree on axis hops)."""
import numpy as np, time, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from f4_lib import *
F = Ferm(*ROOT, mflow=0.01); G = Phot(CPH)
g = mkgrid(ROOT[0], 4, 0.5, 2)
print('grid nodes', len(g.x))
for t in (0.0, 0.05):
    t0 = time.time()
    P = pieces(F, G, g, t, Ms=(1, 2, 3), nrk=2)
    f1 = dm_sf(F, G, g, t, nrk=2)
    print('t=%.3f  F1 dm_sf %+.15f | F4 M=1 %+.15f diff %.1e | M=2 %+.15f | M=3 %+.15f | J %+.15f  (%.0fs)' % (
        t, f1, fam_dm(P, 1, ('M', 1)), fam_dm(P, 1, ('M', 1)) - f1, fam_dm(P, 2, ('M', 2)), fam_dm(P, 3, ('M', 3)),
        fam_dm(P, 1, 'J'), time.time() - t0), flush=True)
    print('   Tad', {str(k): '%+.12f' % v for k, v in P['Tad'].items()})
    print('   E  ', {str(k): '%+.12f' % v for k, v in P['E'].items()})
g2 = Grid([ROOT[0]], 2, 1.0)
P = pieces(F, G, g2, 0.3, Ms=(1, 2, 3, 4), nrk=4, check_ward=True)
print('Ward residual max |sum_j d_j V_j - (D_t(q) - D_t(0))| at t = 0.3, all M in (1,2,3,4), %d^3 pts: %.2e' % (len(g2.x), P['ward']))
