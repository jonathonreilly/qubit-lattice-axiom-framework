"""R16-1 (b), outside the subclass: L can vanish when the photon plateau transition sits on the Wilson edge (outside H2').
Family BQ(b1, b1+1, r=1) with photon box (b1, b1+1) (R8-5's S2 at b1=1.5: L>0; S3 at b1=2: L<0). Bisect the closed-form L,
then fit the on-shell dc_e(m) = L m + c0 + c1/m at m = 25.6, 51.2, 102.4 (anisotropic GL runner) for the next coefficient c0."""
import sys, time; sys.path.insert(0, '.')
import numpy as np
from r161_laws import BQLaw
from r161_heavy import L_photon_slot, U
from r161_onshell_aniso import qx_nodes, dce_aniso
lam = 0.05; t0 = time.time()
mk = lambda b1, m: BQLaw(b1, b1 + 1.0, 1.0, m, (b1, b1 + 1.0))
f = lambda b1: L_photon_slot(mk(b1, 1.0), lam, Np=96, nx=800) * U
lo, hi = 1.5, 2.0; flo, fhi = f(lo), f(hi)
print('L*U at b1 = 1.5: %+.5f, 2.0: %+.5f' % (flo, fhi))
for it in range(40):
    mid = 0.5 * (lo + hi); fm = f(mid)
    if np.sign(fm) == np.sign(flo): lo, flo = mid, fm
    else: hi, fhi = mid, fm
b1s = 0.5 * (lo + hi)
print('root b1* = %.10f, L*U(b1*) = %+.2e (Np=96, nx=800); Np=64: %+.2e' % (b1s, f(b1s), L_photon_slot(mk(b1s, 1.0), lam, Np=64) * U), flush=True)
for npan, Np in ((64, 64), (96, 96)):
    qxn, qxw = qx_nodes(npan, 8)
    ms = (25.6, 51.2, 102.4); v = [dce_aniso(mk(b1s, m), Np, lam, qxn, qxw) * U for m in ms]
    A = np.array([[m, 1, 1 / m] for m in ms]); Lf, c0, c1 = np.linalg.solve(A, np.array(v))
    A2 = np.array([[1, 1 / m] for m in ms[1:]]); c0b, c1b = np.linalg.solve(A2, np.array(v[1:]))
    print('tuned law, qx %d panels, Np=%d: dc_e*U = %+.4f %+.4f %+.4f | 3-pt fit L*U=%+.4f c0=%+.4f c1=%+.2f | with L=0: c0=%+.4f c1=%+.2f  [%.0fs]'
          % (npan, Np, *v, Lf, c0, c1, c0b, c1b, time.time() - t0), flush=True)
