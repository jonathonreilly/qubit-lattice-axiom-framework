# random-restart check of the explicit-isometry optimiser (identity start vs random symplectic starts)
import numpy as np
from scipy.linalg import expm
from r1913_lib import window, symp_opt, J_of
rng = np.random.default_rng(7)
for M, R in ((0.1, 6), (0.03, 10), (1.0, 3)):
    W = window(M, R); n = W['n']; J = J_of(n)
    d0, _ = symp_opt(W)
    outs = []
    for s in range(3):
        K = rng.normal(size=(2*n, 2*n)); K = (K + K.T)/2
        S0 = expm(0.3*J @ K)
        outs.append(symp_opt(W, S_init=S0)[0])
    print('M=%.2f R=%d identity start %.10e ; random starts %s' % (M, R, d0, ' '.join('%.10e' % v for v in outs)), flush=True)
