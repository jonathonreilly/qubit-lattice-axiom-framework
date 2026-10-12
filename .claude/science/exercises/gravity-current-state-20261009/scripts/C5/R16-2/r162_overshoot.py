"""R16-2: outside the stated Dirac families. Literal-type edge with overshoot: S = rho k + (1 - rho) g sin k (g >= 1),
so S' > 1 in the transition (and v_max > 1). Does F_1/2(0+) change sign (a shape zero), and where? Also G_1/2 and v_max.
Same runner and conventions as r162_dirac_scan.py (R13-7 on-shell code). Subtractions: none."""
import numpy as np, sys, time
sys.path.insert(0, '.')
from r85_box_qed_copy import Law, plateau, deriv
from r162_dirac_scan import ce2, hstep
from r101_dirac_moment_copy import moment

class OLaw(Law):
    def __init__(self, b1, b2, g, c1, c2, m):
        super().__init__(b1, b2, 0.0, c1, c2, m, naive_photon=(c1 is None)); self.g = g
    def S(self, k):
        rho = plateau(k, self.b1, self.b2); return rho*k + (1 - rho)*self.g*np.sin(k)

if __name__ == '__main__':
    t0 = time.time(); N = int(sys.argv[1]); lam = 0.02
    kk = np.linspace(-np.pi, np.pi, 200001)
    for (b1, b2) in [(1.0, 2.0), (0.5, 1.5)]:
        for g in (1.0, 1.25, 1.5, 2.0, 2.5, 3.0):
            L0 = OLaw(b1, b2, g, None, None, 0.1)
            Sp = deriv(L0.S, kk); vmax1 = np.max(np.abs(Sp))   # 1D axis bound on |dE/dk_x| as m -> 0 along an axis
            row = []
            for m in (0.2, 0.1):
                L = OLaw(b1, b2, g, None, None, m); Fe, Ft = ce2(L, N, lam, hstep(m, lam)); row.append((Fe, Ft))
            G = moment(OLaw(b1, b2, g, None, None, 0.1), N)['tot']
            print('overshoot box=(%.1f,%.1f) g=%.2f N=%d | max S\' = %.3f (axis v_max ~ %.3f) | F12(0.2) %+8.4f F12(0.1) %+8.4f [tad %+8.4f] | G12(0.1) %+8.4f'
                  % (b1, b2, g, N, Sp.max(), vmax1, row[0][0], row[1][0], row[1][1], G), flush=True)
    print('elapsed %.1fs' % (time.time() - t0))
