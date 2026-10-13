"""R19-11 (b): refine the m->0+ axial root at converged Dirac quadrature (GL q, argv), Jacobian from GL(4,10) (frozen),
then report rows at GL(5,12), (6,16) and the converged quadrature, as vR18-9 did for the m = 0.01 root."""
import sys, os, time, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, '..', 'arch9'))
import lib9 as L
z = np.load(os.path.join(HERE, 'root0_m0.npy')); x = z[:4].copy(); ms, mf = 1e-5, 0.0
q = tuple(int(v) for v in sys.argv[1].split(','))
P = np.load(os.path.join(HERE, 'phq_N224.npy')); T, E, Vmu = P[0:3], P[3:6], P[6]
def rows(x, q):
    bs, bf, r, a = x
    S = L.scal(bs, 1.0, ms); F = L.dirac(bf, r, m=mf, q=q)
    V = np.array([T[0] + T[1]*a + T[2]*a*a, E[0] + E[1]*a + E[2]*a*a, Vmu])
    t = L.NS*S[:3] + L.ND*F[:3] + L.NV*V
    return np.array([t[0], t[1], t[2], L.ND*F[3]])
t0 = time.time(); h = np.array([1e-5, 1e-6, 1e-6, 1e-6]); J = np.empty((4, 4))
for j in range(4):
    dx = np.zeros(4); dx[j] = h[j]; J[:, j] = (rows(x + dx, (4, 10)) - rows(x - dx, (4, 10)))/(2*h[j])
for it in range(3):
    f = rows(x, q); print('GL%s it %d x=(%.12f, %.12f, %.12f, %.12f) rows %s [%.0fs]' % (q, it, *x, f, time.time()-t0), flush=True)
    x = x - np.linalg.solve(J, f)
f = rows(x, q)
print('REFINED (GL%s) x = (%.12f, %.12f, %.12f, %.12f); rows %s; r < 1/sqrt3: %s ; sigma_min(J) %.4e' % (q, *x, f, x[2] < 1/np.sqrt(3), np.linalg.svd(J)[1][-1]))
for qq in ((4, 10), (5, 12)):
    print('  rows at GL%s: %s' % (qq, rows(x, qq)), flush=True)
np.save(os.path.join(HERE, 'root0_refined.npy'), np.r_[x, 1.0, 2.9435, 1.0, mf, ms])
print('[%.0fs]' % (time.time() - t0))
