"""R16-2: locate the shape zero of F_1/2(0+) in the overshoot family (box (0.5,1.5), naive photon), N = 128/192,
m = 0.1 (literal edge: F is even in m, so F(0.1) - F(0+) = O(m^2)); bisection in g. Also v_max (axis, m -> 0) and
G_1/2 there (the photon side stays O(70) U, so kappa_gamma is still needed)."""
import numpy as np, sys, time
sys.path.insert(0, '.')
from r162_overshoot import OLaw
from r162_dirac_scan import ce2, hstep
from r101_dirac_moment_copy import moment
from r85_box_qed_copy import deriv
t0 = time.time(); lam = 0.02; m = 0.1
for N in (128, 192):
    f = lambda g: ce2(OLaw(0.5, 1.5, g, None, None, m), N, lam, hstep(m, lam))[0]
    lo, hi = 2.5, 3.0; flo, fhi = f(lo), f(hi)
    for _ in range(14):
        mid = 0.5*(lo + hi); fm = f(mid)
        if np.sign(fm) == np.sign(flo): lo, flo = mid, fm
        else: hi, fhi = mid, fm
    g0 = 0.5*(lo + hi); L = OLaw(0.5, 1.5, g0, None, None, m)
    kk = np.linspace(-np.pi, np.pi, 200001); vmax = np.max(np.abs(deriv(L.S, kk)))
    print('N=%d: F_1/2(m=0.1) = 0 at g* = %.5f (bracket F %+.2e .. %+.2e) | axis v_max(m->0) = %.3f | G_1/2(0.1) = %+.3f'
          % (N, g0, flo, fhi, vmax, moment(L, N)['tot']), flush=True)
print('elapsed %.1fs' % (time.time() - t0))
