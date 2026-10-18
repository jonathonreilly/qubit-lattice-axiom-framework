import numpy as np, time, cProfile, pstats
from nt1_lib import *
from lat2d import Geom, nodes
G = Geom(2, 6, False, -1); LK = Links(G)
z = np.load('pool_K2c_wsearch_hard_O_open_Lt12_seed1401.npz'); U = [{'x': z['ux'][i], 't': z['ut'][i]} for i in range(len(z['ux']))]
ph, w = nodes(G, U[0], U[1], 0.6, 16, 'hard'); A = LK.joined(U[0], U[1], ph); print(A.shape)
CH = Chiral(LK, '11112', Ns=32, sk=-1)
t=time.time(); CH.logrho(A); print('logrho 16 nodes Ns32', time.time()-t)
cProfile.run('CH.logrho(A)', 'p.out'); pstats.Stats('p.out').sort_stats('cumtime').print_stats(8)
print('fast vs einsum D:', np.abs(LK.D(A) - LK.D_einsum(A)).max())
for Ns in (8, 16):
    t=time.time(); CH = Chiral(LK, '11112', Ns=Ns, sk=-1); CH.logrho(A); print('logrho Ns', Ns, time.time()-t)
