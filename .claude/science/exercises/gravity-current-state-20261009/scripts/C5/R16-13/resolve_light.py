"""R16-13: re-solve the content-6 root at m = 0.001 with the same 3 knobs (b2, bf, r); b1, w2frac frozen."""
import numpy as np
from content3 import ferm
from content4 import scalw
from scipy.optimize import fsolve
n1, n2, ND, m0, b1, b2, fr2, bf, r = np.load('root6_2_2_1.npy')
for m in (0.001,):
    g = lambda y: (n1*scalw(b1, 1.0, m)[0] + n2*scalw(y[0], fr2, m)[0] + ND*ferm(y[1], y[2], m)[0])[:3]*1e3
    y = fsolve(g, [b2, bf, r], xtol=1e-13)
    f = ferm(y[1], y[2], m)[0]
    print('m=%.3f: b2=%.10f bf=%.10f r=%.10f residual %s  mu_T2 total %+.3e' % (m, *y, g(y)/1e3, ND*f[3]))
