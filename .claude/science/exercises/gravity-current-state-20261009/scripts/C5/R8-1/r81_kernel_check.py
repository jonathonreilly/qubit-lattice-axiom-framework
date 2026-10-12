"""R8-1: check the exact Woodbury/Stieltjes BT kernel (r81_common) against Nystrom diagonalisation (d = 1)."""
import numpy as np
from r81_common import BTKernel, lam_for_mass
m, kap = 0.5, 0.4
lam = lam_for_mass(m, kap, 1, 0.85); K = BTKernel(m, kap, lam, 1)
out = ['lam = %.10f, bound mass = %.12f' % (lam, K.bound_mass())]
N = 801; q = np.linspace(-kap, kap, N); w = np.full(N, q[1]-q[0]); sw = np.sqrt(w)
for P in [0.0, 0.4, 1.0]:
    Wk = K.g1(q)[:, None]*K.g1(q)[None, :]*K.Omega(P*P, q, q)
    Mn = np.diag(K.M0(q)) + lam*np.outer(K.g1(q)*sw, K.g1(q)*sw)
    ev, U = np.linalg.eigh(Mn)
    Hs = (U*np.sqrt(ev**2 + P*P))@U.T - np.diag(np.sqrt(K.M0(q)**2 + P*P))
    out.append('P = %.1f: max|Nystrom - kernel| = %.1e (scale %.1e); min eig M = %.12f' % (P, np.abs(Hs - sw[:, None]*Wk*sw[None, :]).max(), np.abs(Hs).max(), ev.min()))
print('\n'.join(out)); open(__file__.replace('.py', '.out'), 'w').write('\n'.join(out) + '\n')
