"""R18-5 (c'): SM-count solve with the Dirac pair block opened: Gamma_u = (1-u) V0* + u UD (every u has Lemma-F forward values;
u is a pair-block law datum, P-R18-5b).  Xi is exactly quadratic in u (t is quadratic in G), so Xi(u) is built from u = 0, 1/2, 1.
knobs z = (b_g, fw_g, b_f, r, b_s, fr_s, u); photon VW0.  argv: tag start(7 csv) Nphot [tmax]."""
import numpy as np, sys, time
from scipy.optimize import least_squares
import dfam
from content3 import D1q
from xiud import pointwise
from smud_lib import phot, scal, NS, ND, NV
tag = sys.argv[1]; x0 = np.array([float(v) for v in sys.argv[2].split(',')]); Ng = int(sys.argv[3])
tmax = float(sys.argv[4]) if len(sys.argv) > 4 else 520.0
t0 = time.time(); best = [np.inf, None]
class Stop(Exception): pass
def dirac_mix(bf, r, u, m=0.01, q=(3, 8)):
    law = D1q(bf, r); ref = dfam.evaluate(law, m, *q); out = []
    for pol in ('T2g', 'Eg'):
        pw = pointwise(law, m, ['V0', 'mix0.0', 'mix0.5', 'mix1.0'], pol, *q)
        y0, yh, y1 = (ref[pol] + pw[n] - pw['V0'] for n in ('mix0.0', 'mix0.5', 'mix1.0'))
        # quadratic through (0,y0),(1/2,yh),(1,y1)
        out.append(y0*(1-u)*(1-2*u) + 4*yh*u*(1-u) + y1*u*(2*u-1))
    return np.array([out[0], out[1], ref['muE'], ref['muT2']])
def parts(z):
    bg, fwg, bf, r, bs, frs, u = z
    return NS*scal(bs, frs*(np.pi - bs)), ND*dirac_mix(bf, r, u), NV*phot(bg, fwg*(np.pi - bg), Ng)
def resid(z):
    if time.time() - t0 > tmax: raise Stop()
    s, F, V = parts(z); t = (s + F + V)[:3]; n = float(np.linalg.norm(t))
    if n < best[0]: best[0], best[1] = n, z.copy()
    return t*1e2
lo = [0.15, 0.10, 0.10, 0.02, 0.3, 0.006, 0.0]; hi = [1.5, 0.95, 1.55, 0.5773, 3.0, 1.0, 1.0]
try:
    res = least_squares(resid, x0, bounds=(lo, hi), xtol=1e-14, ftol=1e-14, gtol=1e-14, diff_step=1e-5, max_nfev=200); status = 'status %d' % res.status
except Stop:
    status = 'stopped at wall-clock guard %.0fs' % tmax
z = best[1]; s, F, V = parts(z)
print('[%s] mix vertex (1-u)V0*+u UD, photon VW0 N=%d, %s, %.0fs, start %s' % (tag, Ng, status, time.time()-t0, sys.argv[2]))
print('knobs b_g=%.8f w_g=%.8f b_f=%.8f r=%.8f b_s=%.8f w_s=%.8f u=%.6f' % (z[0], z[1]*(np.pi-z[0]), z[2], z[3], z[4], z[5]*(np.pi-z[4]), z[6]))
print('raw z:', ','.join('%.10f' % v for v in z))
print('4 scalars:', s); print('22.5 Dirac:', F); print('12 vectors:', V)
t = s + F + V; print('TOTAL Xi_T2g %+.3e Xi_Eg %+.3e mu_E %+.3e | mu_T2 %+.3e' % tuple(t))
print('knobs at bounds:', [i for i in range(7) if abs(z[i]-lo[i]) < 1e-6 or abs(z[i]-hi[i]) < 1e-6])
np.save('smroot_%s.npy' % tag, z)
