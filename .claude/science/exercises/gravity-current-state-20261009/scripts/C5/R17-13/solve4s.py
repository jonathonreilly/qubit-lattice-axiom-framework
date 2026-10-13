"""R17-13 (c), r-slaved: same content/rows as solve4.py, but the Dirac edge is held ON the nontrivial mu_T2^F = 0 branch:
r = r*(b_f, w_f) solved by brentq on (0.02, 1/sqrt3) (lib13 DG mu_T2, GL 3x10), excluding the trivial r -> 0 corner (naive-fermion doublers).
Knobs y = (b_g, fw_g, b_f, w_f, b_s, fr_s); rows Xi_T2g, Xi_Eg, mu_E (totals)."""
import sys, time, numpy as np
sys.path.insert(0, sys.argv[1]); sys.path.insert(0, '.')
import solve4 as S4, lib13 as L
from scipy.optimize import brentq, least_squares
m = 0.01
def rstar(bf, wf):
    wf = min(wf, np.pi/2 - bf); f = lambda r: L.muT2(L.DGlaw(bf, wf, r), m, 3, 10)
    a, c = 0.02, 1/np.sqrt(3)
    if f(a)*f(c) > 0: return None
    return brentq(f, a, c, xtol=1e-12)
def F(y):
    r = rstar(y[2], y[3])
    if r is None: return np.ones(3)*10
    z = np.array([y[0], y[1], y[2], y[3], r, y[4], y[5]]); return S4.tot(z)[:3]*1e2
x0 = np.array([float(v) for v in sys.argv[2].split(',')]); t0 = time.time()
res = least_squares(F, x0, bounds=([0.15, 0.05, 0.1, 0.02, 0.3, 0.02], [2.4, 1.0, 1.3, 0.6, 3.1, 1.0]), xtol=1e-12, ftol=1e-12, gtol=1e-12, diff_step=1e-5, x_scale='jac', max_nfev=int(sys.argv[4]))
y = res.x; r = rstar(y[2], y[3]); z = np.array([y[0], y[1], y[2], y[3], r, y[4], y[5]])
s, Fd, V = S4.parts(z)
print('start', x0, 'nfev %d %.0fs status %d cost %.3e' % (res.nfev, time.time()-t0, res.status, res.cost))
print('raw z:', ','.join('%.10f' % v for v in z))
print('4 scalars:', s); print('22.5 Dirac:', Fd); print('12 vectors:', V)
print('TOTAL Xi_T2g %+.3e Xi_Eg %+.3e mu_E %+.3e mu_T2 %+.3e' % tuple(s + Fd + V))
np.save('root4s_%s.npy' % sys.argv[3], z)
