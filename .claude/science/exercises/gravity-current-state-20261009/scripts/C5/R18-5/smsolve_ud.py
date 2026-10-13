"""R18-5 (c): SM-count solve under (U, UD, VW).  argv: tag start(6 or 7 csv) photon_var(VW0|VWa) Nphot vtx(UD|mixU) [tmax]
knobs z = (b_g, fw_g, b_f, r, b_s, fr_s[, a]) with w_g = fw_g (pi - b_g), w_s = fr_s (pi - b_s); a = VWa stencil weight (lam = 1/4 + 2a).
Wall-clock guard: stops at tmax seconds and reports the best point seen."""
import numpy as np, sys, time
from scipy.optimize import least_squares
from smud_lib import dirac, phot, scal, NS, ND, NV
tag = sys.argv[1]; x0 = np.array([float(v) for v in sys.argv[2].split(',')]); pv = sys.argv[3]; Ng = int(sys.argv[4]); vtx = sys.argv[5]
tmax = float(sys.argv[6]) if len(sys.argv) > 6 else 520.0
t0 = time.time(); best = [np.inf, None, None]
class Stop(Exception): pass
def parts(z, N=Ng):
    bg, fwg, bf, r, bs, frs = z[:6]
    a = z[6] if len(z) > 6 else None
    s = NS*scal(bs, frs*(np.pi - bs)); F = ND*dirac(bf, r, vtx=vtx); V = NV*phot(bg, fwg*(np.pi - bg), N, pv, a)
    return s, F, V
def resid(z):
    if time.time() - t0 > tmax: raise Stop()
    s, F, V = parts(z); t = (s + F + V)[:3]
    n = float(np.linalg.norm(t))
    if n < best[0]: best[0], best[1], best[2] = n, z.copy(), t.copy()
    return t*1e2
lo = [0.15, 0.10, 0.10, 0.02, 0.3, 0.006]; hi = [1.5, 0.95, 1.55, 0.5773, 3.0, 1.0]
if len(x0) > 6: lo.append(-0.6); hi.append(1.0)   # signed stencils allowed (lam = 1/4 + 2a may be < 1/4)
try:
    res = least_squares(resid, x0, bounds=(lo, hi), xtol=1e-14, ftol=1e-14, gtol=1e-14, diff_step=1e-5, max_nfev=200)
    status = 'converged/stopped status %d' % res.status
except Stop:
    status = 'stopped at wall-clock guard %.0fs' % tmax
z = best[1]; s, F, V = parts(z)
print('[%s] vtx %s, photon %s N=%d, %s, %.0fs, start %s' % (tag, vtx, pv, Ng, status, time.time()-t0, sys.argv[2]))
print('knobs b_g=%.8f w_g=%.8f b_f=%.8f r=%.8f b_s=%.8f w_s=%.8f' % (z[0], z[1]*(np.pi-z[0]), z[2], z[3], z[4], z[5]*(np.pi-z[4])) + (' a=%.6f (lam=%.6f)' % (z[6], 0.25+2*z[6]) if len(z) > 6 else ''))
print('raw z:', ','.join('%.10f' % v for v in z))
print('4 scalars (T2g,Eg,muE,muT2):', s); print('22.5 Dirac:', F); print('12 vectors:', V)
t = s + F + V; print('TOTAL Xi_T2g %+.3e Xi_Eg %+.3e mu_E %+.3e | mu_T2 %+.3e' % tuple(t))
print('knobs at bounds:', [i for i in range(len(z)) if abs(z[i]-lo[i]) < 1e-6 or abs(z[i]-hi[i]) < 1e-6])
np.save('smroot_%s.npy' % tag, z)
