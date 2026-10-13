"""R17-13 (c): 4-row SM-count solve. Content (R17-9): 4 real scalars on ONE edge G_w(b_s, fr_s(pi-b_s)) [U vertex, SF; archived content4.scalw],
22.5 four-comp Dirac on ONE Wilson edge DG(b_f, w_f, r) [V0+SF; lib13.dirac_rows, independent of dfam], 12 massless vectors on ONE photon
edge gammaGw(b_g, fw_g(pi-b_g)) [VM vertex; SF; archived R17-9 photon.py via smsolve_lib.phot]. Common matter mass m.
Rows: Xi_T2g, Xi_Eg, mu_E, mu_T2 (totals). Knobs z = (b_g, fw_g, b_f, w_f, r, b_s, fr_s).
DG(b, w, r) is R16-13's family (C5_R16-13_report.md:79); Lemma V1 needs r <= 1/sqrt3; b + w <= pi/2."""
import sys, time, numpy as np
sys.path.insert(0, sys.argv[1]); sys.path.insert(0, '.')
import smsolve_lib as SL
import lib13 as L
from content4 import scalw
from scipy.optimize import least_squares
SL.vert = 'VM'
NS, ND, NV = 4.0, 22.5, 12.0
def parts(z, N=48, m=0.01, q=(3, 8)):
    bg, fwg, bf, wf, r, bs, frs = z
    s = scalw(bs, frs, m, vert='U')[0]; f = L.dirac_rows(L.DGlaw(bf, min(wf, np.pi/2 - bf), r), m, *q); p = SL.phot(bg, fwg, N)[0]
    return NS*s, ND*f, NV*p
def tot(z, **kw):
    a, b, c = parts(z, **kw); return a + b + c
W = np.array([1e2, 1e2, 1e2, 1e3])
import os
lo = [0.15, 0.05, 0.1, 0.02, float(os.environ.get("RLO", "0.01")), 0.3, 0.02]; hi = [2.4, 1.0, 1.3, 0.6, 0.5773, 3.1, 1.0]
if __name__ == '__main__':
    x0 = np.array([float(v) for v in sys.argv[2].split(',')]); tag = sys.argv[3]; nfev = int(sys.argv[4]) if len(sys.argv) > 4 else 30
    t0 = time.time()
    res = least_squares(lambda z: tot(z)*W, x0, bounds=(lo, hi), xtol=1e-13, ftol=1e-13, gtol=1e-13, diff_step=1e-5, x_scale='jac', max_nfev=nfev)
    z = res.x; s, F, V = parts(z)
    print('start', x0); print('nfev %d, %.0fs, status %d, cost %.3e' % (res.nfev, time.time()-t0, res.status, res.cost))
    print('raw z:', ','.join('%.10f' % v for v in z))
    print('4 scalars:', s); print('22.5 Dirac:', F); print('12 vectors:', V)
    print('TOTAL Xi_T2g %+.3e Xi_Eg %+.3e mu_E %+.3e mu_T2 %+.3e' % tuple(s + F + V))
    print('knobs at bounds:', [i for i in range(7) if abs(z[i]-lo[i]) < 1e-6 or abs(z[i]-hi[i]) < 1e-6])
    np.save('root4_%s.npy' % tag, z)
