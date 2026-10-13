"""R19-11 (c) demonstration of the IFT 'one law at a spectrum' statement on a SCALED SM-like spectrum (not the physical one):
masses scaled so the top has m a = s_top (argv); Dirac species t, b, c, tau with SM counts and ratios (lighter ones set to 0:
they carry 0.3% of sum n m); scalar edge H, W, W, Z; vector mu_E with W, W, Z (vector Xi massless, as archived).
(i) residual of the 0+ law at this spectrum vs the linear prediction; (ii) Newton (frozen 0+ Jacobian) to the spectrum root;
(iii) compare the knob shift with -J^-1 R(x0)."""
import sys, os, time, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, '..', 'arch9')); sys.path.insert(1, os.path.join(HERE, '..', 'arch18'))
import lib9 as L
from r1712_lib import photonGw
from zz import mu_E
st = float(sys.argv[1]); mt = 172.69; sc = st/mt
dirac_sp = [(3, 172.69), (3, 4.18), (3, 1.27), (1, 1.77686), (12.5, 0.0)]      # 22.5 total
scal_sp = [(1, 125.25), (2, 80.377), (1, 91.1876)]; vec_sp = [(2, 80.377), (1, 91.1876), (9, 0.0)]
P = np.load(os.path.join(HERE, 'phq_N224.npy')); T, E = P[0:3], P[3:6]
g, f = photonGw(2.9435, np.pi - 2.9435).samples(1 << 14)
Vmu = sum(n*2*mu_E(g, f, max(m*sc, 1e-5)) for n, m in vec_sp)/12.0
def rows(x, spec=True, q=(4, 10)):
    bs, bf, r, a = x
    if spec:
        Ssum = sum(n*L.scal(bs, 1.0, max(m*sc, 1e-5)) for n, m in scal_sp); Fsum = sum(n*L.dirac(bf, r, m=m*sc, q=q) for n, m in dirac_sp); vmu = Vmu
    else:
        Ssum = 4*L.scal(bs, 1.0, 1e-5); Fsum = 22.5*L.dirac(bf, r, m=0.0, q=q); vmu = 2*mu_E(g, f, 1e-5)
    V = np.array([T[0] + T[1]*a + T[2]*a*a, E[0] + E[1]*a + E[2]*a*a, vmu])
    t = Ssum[:3] + Fsum[:3] + 12*V
    return np.array([t[0], t[1], t[2], Fsum[3]])
z = np.load(os.path.join(HERE, 'root0_final.npy')); x0 = z[:4].copy(); t0 = time.time()
h = np.array([1e-5, 1e-6, 1e-6, 1e-6]); J = np.empty((4, 4))
for j in range(4):
    dx = np.zeros(4); dx[j] = h[j]; J[:, j] = (rows(x0 + dx, False) - rows(x0 - dx, False))/(2*h[j])
R0 = rows(x0, False); Rs = rows(x0, True)
c1 = np.array([-1.44595e-3, -1.67037e-4, 1.06932e-2, 2.73929e-3]); S1 = sum(n*m*sc for n, m in dirac_sp)
print('scaled spectrum: top m a = %g; Dirac sum n m a = %.4e' % (st, S1))
print('0+ law at m=0+ (GL(4,10)): %s' % R0)
print('0+ law at the scaled spectrum: R = %s ; linear Dirac prediction c1*sum = %s' % (Rs - R0, c1*S1))
pred = x0 - np.linalg.solve(J, Rs - R0)
x = x0.copy()
for it in range(3):
    fv = rows(x, True) - R0; print('it %d x=(%.12f, %.12f, %.12f, %.12f) rows-R0 %s [%.0fs]' % (it, *x, fv, time.time()-t0), flush=True)
    x = x - np.linalg.solve(J, fv)
print('SPECTRUM ROOT x = (%.12f, %.12f, %.12f, %.12f); shift %s ; linear IFT prediction shift %s ; r < 1/sqrt3: %s' % (*x, x - x0, pred - x0, x[2] < 1/np.sqrt(3)))
print('[%.0fs]' % (time.time() - t0))
