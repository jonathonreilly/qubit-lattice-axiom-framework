"""Calibration: reproduce R14-1's mu_E for G(1.4), S(1.4) (r141_shear_extra.out) and v_max; Xi signs."""
import numpy as np, time, sys
sys.path.insert(0, '.')
from prof import *
T0 = time.time()
for law in [G_law(1.4), S_law(1.4)]:
    for m in [1.0, 0.3]:
        for N in [160, 320]:
            a, b = mu_E(law, m, N)
            print('%s m=%.1f N=%d  mu_E (A-form) = %+.6e  (IBP form) = %+.6e' % (law.name, m, N, a, b), flush=True)
        print('   v_max(d=3) = %.6f   A range [%.3f, %.3f]' % ((law.vmax(m),) + law.Amax()[::-1]), flush=True)
        X = Xi(law, m, 160)
        print('   Xi (A-form / IBP form): ' + '  '.join('%s %+.4e/%+.4e' % (v, x[0], x[1]) for v, x in X.items()), flush=True)
print('ref R14-1 (r141_shear_extra.out): G14 m=1 +3.525432e-03, m=0.3 +4.252013e-03; S14 m=1 +5.063092e-03 (N=480), m=0.3 +7.056032e-03; v_max G(1.4) d=3 0.9938 (m=0.3)')
print('runtime %.1fs' % (time.time()-T0))
