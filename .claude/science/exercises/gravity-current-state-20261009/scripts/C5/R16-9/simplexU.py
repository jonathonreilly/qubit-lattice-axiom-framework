"""R16-9: explicit-law search for the U-vertex triple zero (U,Eg = U,T2g = mu_E = 0) in convex mixes (sigma' mixes keep |sigma'|<=1)
of R16-3's corners A = G(1.0), C2 = Zz(1.0,0.35,0.47,0.03), C = Zz(1.0,0.35,0.43,0.03), Z1, and shear corners D (terraces).
Reports, per D, the best sign-feasible point (U,Eg>=0, U,T2g>=0) with smallest mu_E on a simplex grid. m = 0.1."""
import numpy as np, sys, time, itertools; sys.path.insert(0, '.')
from zz import *; from floor_scan import Zz
T0 = time.time(); NF = 1 << 16; m = float(sys.argv[1]) if len(sys.argv) > 1 else 0.1; VTX = sys.argv[2] if len(sys.argv) > 2 else 'U'
A = ZLaw([1.0, 0.0], [1.0 + (np.pi-1.0)/2], np.pi-1.0, 'G(1.0)', nf=NF)
C = Zz(1.0, 0.35, 0.43, 0.03); C2 = Zz(1.0, 0.35, 0.47, 0.03)
Z1 = ZLaw([1, -1, 1, -1, 1, -1, 0], [1.0, 1.4, 1.8, 2.2, 2.6, 3.0], 0.06, 'Z1', nf=NF)
Ds = [ZLaw([1.0, 0.0], [1.0 + 0.025], 0.05, 'Gw(1.0,0.05)', nf=NF),
      ZLaw([1.0, 0.0, 1.0, 0.0], [0.5, 1.2, 1.5], 0.03, 'T(0.5,1.2,1.5)', nf=NF),
      ZLaw([1.0, 0.0, 1.0, 0.0], [0.3, 1.6, 2.2], 0.03, 'T(0.3,1.6,2.2)', nf=NF),
      ZLaw([1.0, 0.0], [0.4 + 0.015], 0.03, 'Gw(0.4,0.03)', nf=NF),
      ZLaw([1.0, -1.0, 0.0], [0.4, 0.6], 0.03, 'drop(0.4->0.2)flat', nf=NF)]
def ev(L, nn=1 << 12, nu=500):
    g, f = L.samples(nn); X = xi_all(g, f, m, nu=nu); return np.array([X[VTX+',Eg'], X[VTX+',T2g'], mu_E(g, f, m, nu=nu)])
for D in Ds:
    print('corner %s: %s,Eg %+.2e %s,T2g %+.2e mu_E %+.2e' % (D.name, VTX, *ev(D)[:1], VTX, *ev(D)[1:]), flush=True)
best_all = None
for D in Ds:
    corners = [A, C2, C, D]; best = None; cnt = 0
    step = 0.05
    for w1 in np.arange(0, 1.0001, step):
        for w2 in np.arange(0, 1.0001 - w1, step):
            for w3 in np.arange(0, 1.0001 - w1 - w2, step):
                w0 = 1 - w1 - w2 - w3
                if w0 < -1e-12: continue
                L = Mix(corners, [w0, w1, w2, w3]); r = ev(L); cnt += 1
                if r[0] >= 0 and r[1] >= 0 and (best is None or r[2] < best[0]): best = (r[2], r[0], r[1], (w0, w1, w2, w3))
    print('D=%s: %d mixes; min mu_E with %s,Eg>=0 & %s,T2g>=0: %s (%.0fs)' % (D.name, cnt, VTX, VTX, 'none' if best is None else '%+.3e (Eg %+.1e T2g %+.1e) w=%s' % (best[0], best[1], best[2], np.round(best[3], 3)), time.time()-T0), flush=True)
