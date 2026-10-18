"""Universality test: is the Ward-violating part of the K^2 symbol in the non-universal (cutoff) part?
For each m: symbol M2 along generic n (Richardson), report |n.M2| (Ward violation), TT stiffness, and N-convergence."""
import time, sys, numpy as np
from indep_bubble import *
n = np.array([1.0, 0.37, 0.61, -0.23]); n /= np.linalg.norm(n)
e = tt_pol(0.01 * n)
plan = [(1.0, 12), (0.7, 12), (0.5, 16), (0.35, 20), (0.25, 28)]
if len(sys.argv) > 1: plan = [tuple(map(float, a.split(':'))) for a in sys.argv[1:]]
for m, N in plan:
    N = int(N); t = time.time()
    P0 = bubble(np.zeros(4), N, m)
    Ma = (bubble(0.1 * n, N, m) - P0) / 0.01
    Mb = (bubble(0.05 * n, N, m) - P0) / 0.0025
    M2 = (4 * Mb - Ma) / 3
    W = np.einsum('m,mnrs->nrs', n, M2)
    tt = np.einsum('ab,abcd,cd->', e, M2, e).real
    print("m=%.3f N=%d  |n.M2|max=%.5e  TT=%.5e  ratio=%.4f  maxM2=%.5e  (%.0fs)" %
          (m, N, np.abs(W).max(), tt, np.abs(W).max() / abs(tt), np.abs(M2).max(), time.time() - t), flush=True)
    np.save('M2_m%.3f_N%d.npy' % (m, N), M2)
