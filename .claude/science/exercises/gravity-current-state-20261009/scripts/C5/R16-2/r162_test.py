import numpy as np, time, sys
sys.path.insert(0,'.')
from r162_laws import D1Law
from r137_onshell import ce2_minus_1, U
from r101_dirac_moment_copy import moment
L = D1Law(1.0, 1/np.sqrt(3), None, None, 0.1)
k = np.linspace(-1.0, 1.0, 11)
print('box check max|S-k|', np.abs(L.S(k)-k).max(), 'max|W|', np.abs(L.W(k)).max(), 'Wpi', L.Wpi, 'S(pi)', L.S(np.pi))
for N in (48, 64):
    t0 = time.time(); ce, ct, dE0 = ce2_minus_1(L, N, lam=0.05)
    mo = moment(L, N)
    print('N', N, 'dc_e*U', ce/2*U, 'tad', ct/2*U, 'dc_g*U', mo['tot'], 'time', time.time()-t0, flush=True)
