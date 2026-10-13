import numpy as np, time
from r1913_lib import *
for M in (0.3, 1.0, 0.05):
    W = window(M, 0)
    print('M=%.2f R=0 product dE = %.6f' % (M, dE_of_S(W, np.eye(2))), flush=True)
for M in (1.0, 0.3):
    for R in (1, 2, 3, 4):
        W = window(M, R)
        t = time.time(); dU, S = symp_opt(W); t1 = time.time() - t
        t = time.time(); dL, st = sdp_lower(W); t2 = time.time() - t
        print('M=%.2f R=%d  upper(isometry)=%.10e  lower(SDP)=%.10e  [%s]  t=%.1f,%.1f s' % (M, R, dU, dL, st, t1, t2), flush=True)
