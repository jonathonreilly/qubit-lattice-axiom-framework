"""R16-2: steep photon boxes (R13-7's sign-flip shapes for the heavy constant) on the stated Dirac edges and the scalar:
does F_s(0+) keep its sign? m = 0.1 (Dirac D1: + slope ~ 1-2 U per unit m, i.e. F(0+) ~ F(0.1) - 0.1..0.2), lam = 0.02.
Subtractions: none."""
import numpy as np, sys, time
sys.path.insert(0, '.')
from r162_laws import D1Law, GScal
from r85_box_qed_copy import Law
from r162_dirac_scan import ce2, hstep
from r162_scalar import dc_scalar
t0 = time.time(); lam = 0.02; m = 0.1
for N in (128, 192):
    for (c1, c2) in [(2.5, 3.1), (2.8, 3.1), (0.5, 1.5), (1.4, 1.6)]:
        a = ce2(D1Law(1.4, 1/np.sqrt(3), c1, c2, m), N, lam, hstep(m, lam))
        b = ce2(D1Law(1.0, 0.2, c1, c2, m), N, lam, hstep(m, lam))
        c = ce2(Law(1.0, 2.0, 0.0, c1, c2, m), N, lam, hstep(m, lam))
        d = ce2(Law(2.5, 3.1, 0.0, c1, c2, m), N, lam, hstep(m, lam))
        e = dc_scalar(GScal(1.4, c1, c2, m), N, lam, hstep(m, lam))
        f = dc_scalar(GScal(0.6, c1, c2, m), N, lam, hstep(m, lam))
        print('photon box (%.1f,%.1f) N=%d | D1(1.4,.577) %+8.4f [tad %+8.4f] | D1(1.0,0.2) %+8.4f | LIT(1,2) %+8.4f | LIT(2.5,3.1) %+8.4f | G(1.4) %+8.4f [sea %+8.4f] | G(0.6) %+8.4f'
              % (c1, c2, N, a[0], a[1], b[0], c[0], d[0], e[0], e[1], f[0]), flush=True)
print('elapsed %.1fs' % (time.time() - t0))
