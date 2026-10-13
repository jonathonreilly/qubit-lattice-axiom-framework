"""R18-9 step 1 (model solve). Photon on gammaGw(b_g, pi - b_g) (fw = 1, R14-1's G(b) photon), VWa stencil a.
Photon Xi coefficients (T0,T1,T2,E0,E1,E2) interpolated in b_g (cubic through N=160 points); mu_E^gamma exact.
Dirac D1(b_f, r) with UD exact (GL(3,8)); scalar G_w(b_s, fr*(pi-b_s)) with U exact; m = 0.01.
Knobs (b_g, b_f, r, a) at fixed scalar (b_s, fr) from argv; rows (T2g, Eg, muE, muT2). Purpose: locate b_g*."""
import sys, glob, numpy as np, lib9 as L
from scipy.optimize import fsolve
from photon import photonGw
from zz import mu_E
D = np.vstack([np.load(f) for f in sorted(glob.glob('photres2_N160_parsed.npy'))]); D = D[D[:, 1] == 1.0]; D = D[np.argsort(D[:, 0])]
print('photon nodes b_g:', D[:, 0])
deg = min(3, len(D) - 1)
fits = [np.polyfit(D[:, 0], D[:, j], deg) for j in range(2, 8)]
def phot(bg, a):
    c = [np.polyval(f, bg) for f in fits]
    law = photonGw(bg, np.pi - bg); g, f = law.samples(1 << 14)
    return np.array([c[0] + c[1]*a + c[2]*a*a, c[3] + c[4]*a + c[5]*a*a, 2*mu_E(g, f, 1e-3)])
bs, fr = float(sys.argv[1]), float(sys.argv[2]); m = 0.01
S = L.scal(bs, fr, m)
def rows(x):
    bg, bf, r, a = x
    F = L.dirac(bf, r, m=m); V = phot(bg, a)
    t = L.NS*S[:3] + L.ND*F[:3] + L.NV*V
    return np.array([t[0], t[1], t[2], L.ND*F[3]])
x0 = np.array([float(v) for v in sys.argv[3].split(',')]) if len(sys.argv) > 3 else np.array([2.95, 0.92, 0.565, -0.173])
sol, info, ier, msg = fsolve(rows, x0, full_output=True, epsfcn=1e-10)
print('scalar G_w(%.4f, fr=%.3f) per real: T %+.4e E %+.4e muE %+.4e' % (bs, fr, *S[:3]))
print('start', x0, 'rows', rows(x0))
print('solution (b_g, b_f, r, a) =', sol, 'ier', ier, msg)
print('rows at solution', rows(sol), 'r <= 1/sqrt3:', sol[2] <= 1/np.sqrt(3))
np.save('model_root_%s_%s.npy' % (sys.argv[1], sys.argv[2]), sol)
