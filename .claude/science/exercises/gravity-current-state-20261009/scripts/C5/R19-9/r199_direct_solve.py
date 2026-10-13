"""R19-9 (c): one Newton step in (w_d, w_o) on the DIRECT N = 224 face rows at the r = 0.1 exact-vertex root (removes the
w-quadratic finite-q artefact that the linear-in-w model does not carry; R18-13 sec. 3.4), then a direct re-evaluation.
Axial rows do not depend on (w_d, w_o) (Lemma O(iii)); the corner shift changes by 12 dC/dw r^4 dw ~ 1e-13 (included)."""
import os, sys, time, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, 'arch17_4')); sys.path.insert(0, os.path.join(HERE, 'arch18_13')); sys.path.insert(0, os.path.join(HERE, 'arch18'))
import offaxis as O
from zz import ZLaw
import dface as DF, vwface as V
from content3 import D1q
import r199_corner_rows as CR
t0 = time.time(); r = float(sys.argv[1]); N = 224
z = np.load(os.path.join(HERE, 'arch18_13', 'root_refR18-9.npy')); fr, bg, fw, m = z[4], z[5], z[6], z[7]
S = np.load('resolve_sols.npy'); x = S[np.argmin(np.abs(S[:, 0] - r))][1:7].copy(); bs, bf, rD, a, wd, wo = x
wA = fr*(np.pi - bs); Xs, _ = O.xi_off(ZLaw([1.0, 0.0], [bs + wA/2], wA), m, 'U')
Xd = DF.xi_dirac(D1q(bf, rD), m, rows=('face1', 'face2'), npan=4, ngl=10)
law = V.photonGw(bg, fw*(np.pi - bg))
def tot(wd_, wo_):
    C = CR.corner_coeffs(a, wd_, wo_)
    ph = {rw: V.xi_geo(law, N, rw, a, settings=((wd_, wo_),))[0] for rw in ('face1', 'face2')}
    return np.array([4*Xs[rw] + 22.5*Xd[rw] + 12*ph[rw] + 12*C[rw]*r**4 for rw in ('face1', 'face2')])
f0 = np.array([-1.847e-06, -4.437e-07]) if len(sys.argv) < 3 else tot(wd, wo)
Jw = 12*np.array([[1.397040e-01, 2.892797e-01], [0.0, 5.785714e-01]])
dw = -np.linalg.solve(Jw, f0); wd1, wo1 = wd + dw[0], wo + dw[1]
f1 = tot(wd1, wo1)
print(f'r = {r}: start (w_d, w_o) = ({wd:.10f}, {wo:.10f}) direct face totals {f0} (r199_direct_r{r}.out)')
print(f'  step dw = {dw}; new (w_d, w_o) = ({wd1:.10f}, {wo1:.10f}); DIRECT N=224 face totals {f1} [{time.time()-t0:.0f}s]')
