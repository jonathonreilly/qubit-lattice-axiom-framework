"""NT-1 descriptive: |rho_11112| = |det D(1)|^2 |det D(2)|^(1/2) (massless vector overlaps, up to a constant) on joined configs."""
import numpy as np
from nt1_lib import *
from lat2d import Geom, nodes
G = Geom(2, 6, False, -1); LK = Links(G)
z = np.load('pool_K2c_wsearch_hard_O_open_Lt12_seed1401.npz'); U = [{'x': z['ux'][i], 't': z['ut'][i]} for i in range(len(z['ux']))]
A = np.concatenate([LK.joined(U[a], U[b], nodes(G, U[a], U[b], 0.6, 16, 'hard')[0][3:6]) for (a, b) in [(0, 1), (4, 9), (13, 17)]])
W = Chiral(LK, '11112', Ns=8, sk=-1).logrho(A)[0].real
v1, _ = vec_logdet(LK, A, 0.0, 1); v2, _ = vec_logdet(LK, A, 0.0, 2)
r = W - (2 * v1.real + 0.5 * v2.real)
print(f"ln|rho_chi| - [2 ln det D(1) + 0.5 ln det D(2)]: spread over 9 configs {r.max() - r.min():.2e} (constant = {r.mean():+.6f}; expected -(4*N/2 + N/2) ln 2 = {-(2.5*G.N)*np.log(2):+.6f})")
