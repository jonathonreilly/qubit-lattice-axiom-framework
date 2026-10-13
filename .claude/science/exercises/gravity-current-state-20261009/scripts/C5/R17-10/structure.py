"""R17-10: per-level structure of stored relaxation optima (M/|bin|, mean slope^2 P/M, M P/|bin|^2)."""
import numpy as np, sys
L = 50; lev = np.linspace(0.15, np.pi, L); DL = lev[1]-lev[0]
for fn in sys.argv[1:]:
    x = np.load(fn); M, P, Q, R = x[:L], x[L:2*L], x[2*L:3*L], x[3*L:]
    print(fn); [print('  h=%.3f M/DL=%6.2f P/M=%.3f Q/M=%.3f R/M=%.3f MP/DL^2=%7.2f' % (lev[j], M[j]/DL, P[j]/M[j], Q[j]/M[j], R[j]/M[j], M[j]*P[j]/DL**2)) for j in range(L) if M[j] > 1e-6]
