import numpy as np, time
from r1913_lib import *
for R in (6, 10, 16):
    for M in (0.1, 0.01):
        W = window(M, R); t = time.time(); dU, S = symp_opt(W); print('R=%d M=%.3f dE=%.6e t=%.1fs' % (R, M, dU, time.time()-t), flush=True)
