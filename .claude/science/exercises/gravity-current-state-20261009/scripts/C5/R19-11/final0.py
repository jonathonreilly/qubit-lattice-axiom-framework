"""R19-11 (b) final: the axial root with EVERY mass at 0+: Dirac m = 0, scalar m = 1e-5 (rows analytic in m^2, offset ~1e-14),
and the vector mu_E at m -> 0 (2 x mu_E at 1e-5) instead of the archived 1e-3 regulator (offset -3.6e-8 in the mu_E total).
Starts from refine0's GL(5,12) root; Jacobian at GL(4,10); Newton at GL(5,12); reports rows at GL(4,10), (5,12)."""
import sys, os, time, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, '..', 'arch9')); sys.path.insert(1, os.path.join(HERE, '..', 'arch18'))
import lib9 as L
from r1712_lib import photonGw
from zz import mu_E
z = np.load(os.path.join(HERE, 'root0_refined.npy')); x = z[:4].copy(); ms, mf = 1e-5, 0.0
P = np.load(os.path.join(HERE, 'phq_N224.npy')); T, E = P[0:3], P[3:6]
g, f = photonGw(2.9435, np.pi - 2.9435).samples(1 << 14); Vmu = 2*mu_E(g, f, 1e-5)
print('vector muE: archived regulator 1e-3 -> %.10e ; m -> 0 (1e-5) -> %.10e' % (P[6], Vmu))
def rows(x, q):
    bs, bf, r, a = x
    S = L.scal(bs, 1.0, ms); F = L.dirac(bf, r, m=mf, q=q)
    V = np.array([T[0] + T[1]*a + T[2]*a*a, E[0] + E[1]*a + E[2]*a*a, Vmu])
    t = L.NS*S[:3] + L.ND*F[:3] + L.NV*V
    return np.array([t[0], t[1], t[2], L.ND*F[3]])
t0 = time.time(); h = np.array([1e-5, 1e-6, 1e-6, 1e-6]); J = np.empty((4, 4))
for j in range(4):
    dx = np.zeros(4); dx[j] = h[j]; J[:, j] = (rows(x + dx, (4, 10)) - rows(x - dx, (4, 10)))/(2*h[j])
for it in range(2):
    fv = rows(x, (5, 12)); print('it %d x=(%.12f, %.12f, %.12f, %.12f) rows GL(5,12) %s' % (it, *x, fv), flush=True)
    x = x - np.linalg.solve(J, fv)
print('FINAL 0+ ROOT x = (%.12f, %.12f, %.12f, %.12f); r < 1/sqrt3 (margin %.6f); det J %.5e; sv %s' % (*x, 1/np.sqrt(3) - x[2], np.linalg.det(J), np.linalg.svd(J)[1]))
for qq in ((4, 10), (5, 12)): print('  rows at GL%s: %s' % (qq, rows(x, qq)), flush=True)
np.save(os.path.join(HERE, 'root0_final.npy'), np.r_[x, 1.0, 2.9435, 1.0, mf, ms]); print('[%.0fs]' % (time.time()-t0))
