"""Corollary F1 closed form: VU forward S_12 = (w/2) c_x c_y (1 - c_z^2) e(eps1, eps2) (T2g); and S_11 + S_22 trace check."""
import numpy as np
from r1712_lib import *
rng = np.random.default_rng(11); worst = 0.0
for law in (photonNN(), photonG(1.4), photonGw(0.25133, 1.01946)):
    for _ in range(300):
        kv = rng.uniform(-np.pi, np.pi, 3)
        S, Sreq = forward_S(law, kv, 'T2g', 'VU')
        sig = law.sig(kv); w = np.linalg.norm(sig); c = law.c(kv); sh, ep = pols(sig)
        pred = 0.5*w*c[0]*c[1]*(1 - c[2]**2)*(ep[0][0]*ep[1][1] + ep[0][1]*ep[1][0])
        worst = max(worst, abs(S[0, 1] - pred))
print('max |S_12(VU) - closed form| over 900 points: %.2e' % worst)
