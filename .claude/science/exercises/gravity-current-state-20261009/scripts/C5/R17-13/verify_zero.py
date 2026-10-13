"""R17-13 verify_zero: the explicit subluminal Wilson-Dirac law with mu_T2^F = 0 (ZEROED candidate).
Law: D1(b*, r) with r = 0.55962727 (R17-9 VM root's r, so only b_f moves) and r = 0.5; m = 0.01 and 0.001.
Checks: (i) lib13 form P at 3 GL resolutions, IBP form I; (ii) archived dfam.evaluate (R16-13 GL) at 2 resolutions;
(iii) archived dirac.strain_mu (uniform 3D midpoint grid, independent of GL) at N = 160, 240; (iv) Lemma V1 + sampled v_max;
(v) transversality d mu/db, d mu/dm; (vi) other Dirac rows (V0 + SF) and W_pi."""
import sys, time, numpy as np
sys.path.insert(0, sys.argv[1]); sys.path.insert(0, '.')
import lib13 as L
import dfam, dirac
from content3 import D1q
from scipy.optimize import brentq
t0 = time.time()
for r in (0.55962727, 0.5):
    for m in (0.01, 0.001):
        f = lambda b: L.muT2(L.D1law(b, r), m, 8, 16)
        bs = brentq(f, 0.6, 1.2, xtol=1e-15, rtol=1e-15)
        law = L.D1law(bs, r)
        P = [L.muT2(law, m, a, c) for a, c in ((4, 12), (8, 16), (12, 24))]
        I = L.muT2(law, m, 12, 24, form='I')
        parts = L.muT2_parts(law, m, 8, 16)
        lq = D1q(bs, r)
        A1 = dfam.evaluate(lq, m, 3, 8); A2 = dfam.evaluate(lq, m, 6, 12)
        U = [-4*dirac.strain_mu(lq, m, N)[1] for N in (160, 240)]
        h = 1e-4
        dmb = (L.muT2(L.D1law(bs+h, r), m, 8, 16) - L.muT2(L.D1law(bs-h, r), m, 8, 16))/(2*h)
        dmm = (L.muT2(law, m*1.1, 8, 16) - L.muT2(law, m*0.9, 8, 16))/(0.2*m)
        vm = dfam.vmax_sample(lq, m, 81)
        print('D1(b*=%.12f, r=%.8f), m=%g:' % (bs, r, m))
        print('   mu_T2^F form P (4x12, 8x16, 12x24): %+.3e %+.3e %+.3e ; IBP form I (12x24) %+.3e' % tuple(P + [I]))
        print('   parts KK %+.6e KM %+.6e MM %+.6e (scale of each part vs zero)' % tuple(parts))
        print('   archived dfam GL (3,8) %+.3e, (6,12) %+.3e ; archived uniform grid N=160 %+.3e, N=240 %+.3e' % (A1['muT2'], A2['muT2'], *U))
        print('   d mu_T2/d b = %+.6e ; d mu_T2/d m (fixed law) = %+.6e ; => b* drift db*/dm = %+.4f' % (dmb, dmm, -dmm/dmb))
        print('   other rows per Dirac field (V0+SF, dfam (6,12)): Xi_T2g %+.6e Xi_Eg %+.6e mu_E %+.6e' % (A2['T2g'], A2['Eg'], A2['muE']))
        print('   r < 1/sqrt3 = %.7f: %s -> Lemma V1: whole-zone v_max <= 1; sampled v_max (81^3) %.6f ; W_pi = %.6f (doubler rest energies m + n W_pi, n=1..3)' % (1/np.sqrt(3), r < 1/np.sqrt(3), vm, law.Wpi))
        print('   [%.0fs]' % (time.time()-t0), flush=True)
