"""F6 (a) loop 3 (top Yukawa) on the R18-9 root's D1 edge under F1's SF flow, plus the strain-dependent Higgs TADPOLE (outside the
pre-registered four loops; reported separately).  Per N_c y_t^2 (Sigma_Y) and per N_c y_t/sqrt2 (tadpole), SF units t.
Branches: Y-a/B1 (flow law datum at mflow = 0.01, F1's main), Y-a/B2 (mflow = 0), 0+ root B1; Y-b (flow tracks the actual mass);
F3's dressing responses (G1, G2) at t = 0, and the values at F3's a* (fermion additive-mass zero, f3_astar.out:1-2)."""
import numpy as np, time, sys
from f6_lib import *
t00 = time.time()
def grid(b, n, hm):
    return panels([b, np.pi - b], n, hm)
which = sys.argv[1] if len(sys.argv) > 1 else 'all'
if which in ('all', 'a'):
    F = Ferm(*ROOT, mflow=0.01)
    for (n, hm, d) in ((6, 0.25, 0.003), (8, 0.15, 0.003), (8, 0.15, 0.0015), (10, 0.10, 0.0015)):
        x, w = grid(ROOT[0], n, hm)
        y0, c0 = yuk(F, x, w, 0.0); y1, c1 = yuk(F, x, w, d); y2, c2 = yuk(F, x, w, 2*d)
        hy = (4*2*(y1 - y0)/d**2 - 2*(y2 - y0)/(2*d)**2)/3; hc = (4*2*(c1 - c0)/d**2 - 2*(c2 - c0)/(2*d)**2)/3
        print('Y-a B1 nodes %3d d %.4f: Y(0) %+.10f  d2_t Y Rich %+.8e (single-d %+.8e) | C(0) %+.10f  d2_t C Rich %+.8e  (%.0fs)'
              % (len(x), d, y0, hy, 2*(y1 - y0)/d**2, c0, hc, time.time() - t00), flush=True)
    for lab, F_, b in (('Y-a B2 (mflow 0)', Ferm(*ROOT, mflow=0.0), ROOT[0]), ('Y-a 0+ root B1', Ferm(*ROOT0, mflow=0.01), ROOT0[0])):
        x, w = grid(b, 8, 0.15); d = 0.0015
        y0, c0 = yuk(F_, x, w, 0.0); y1, c1 = yuk(F_, x, w, d); y2, c2 = yuk(F_, x, w, 2*d)
        hy = (4*2*(y1 - y0)/d**2 - 2*(y2 - y0)/(2*d)**2)/3; hc = (4*2*(c1 - c0)/d**2 - 2*(c2 - c0)/(2*d)**2)/3
        print('%-18s nodes %3d: Y(0) %+.10f  d2_t Y Rich %+.8e | C(0) %+.10f  d2_t C Rich %+.8e  (%.0fs)' % (lab, len(x), y0, hy, c0, hc, time.time() - t00), flush=True)
    x, w = grid(ROOT[0], 8, 0.15)
    for g, ast in (('G1', 1.411635e-02), ('G2', 8.068589e-03)):
        ry, rc = yuk(F, x, w, 0.0, dress=g)
        print('dressing %s: dY/deps %+.8e  dC/deps %+.8e ; at F3 a* = %.6e: Hessian shifts 2a*dY %+.6e, 2a*dC %+.6e  (%.0fs)'
              % (g, ry, rc, ast, 2*ast*ry, 2*ast*rc, time.time() - t00), flush=True)
if which in ('all', 'b'):
    x, w = grid(ROOT[0], 8, 0.15); d = 0.003; dm = 0.005
    tab = {}
    for m in (-dm, 0.0, dm):
        e0 = evac_track(*ROOT, x, w, 0.0, m); e1 = evac_track(*ROOT, x, w, d, m); e2 = evac_track(*ROOT, x, w, 2*d, m)
        tab[m] = (4*2*(e1 - e0)/d**2 - 2*(e2 - e0)/(2*d)**2)/3
        print('Y-b: mu_E(m = %+.4f) per Dirac field (own flow at m) %+.10e  (%.0fs)' % (m, tab[m], time.time() - t00), flush=True)
    d2 = (tab[dm] - 2*tab[0.0] + tab[-dm])/dm**2; d1 = (tab[dm] - tab[-dm])/(2*dm)
    print('Y-b: d mu_E/dm|0 = c1 %+.6e ; d2 mu_E/dm2|0 = 2 c2 %+.6e  -> Sigma_Y Hessian per N_c y^2 = (1/2) d2 mu = %+.6e ; tadpole Hessian per N_c y/sqrt2 = c1'
          % (d1, d2, d2/2), flush=True)
print('time %.0f s' % (time.time() - t00))
