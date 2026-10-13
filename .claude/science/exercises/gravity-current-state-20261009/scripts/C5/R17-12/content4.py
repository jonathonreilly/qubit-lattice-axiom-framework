"""R16-13: content Ns real scalars on G_w(bA, wA) [R14-3 family, M/U vertex] + ND Dirac on D1(bf, r). 4 knobs (bA, wA-frac, bf, r)."""
import numpy as np, sys, time
import dfam
from content3 import ferm
from zz import ZLaw, xi_all, mu_E
from scipy.optimize import least_squares
def scalw(bA, fr, m, vert='M', n=1 << 14, nu=1500):
    wA = fr*(np.pi - bA)
    L = ZLaw([1.0, 0.0], [bA + wA/2], wA); g, f = L.samples(n)
    x = xi_all(g, f, m, nu=nu)
    return np.array([x[vert+',T2g'], x[vert+',Eg'], mu_E(g, f, m, nu=nu), 0.0]), L
if __name__ == '__main__':
    Ns, ND, m = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])
    x0 = np.array([float(v) for v in sys.argv[4].split(',')]); vert = sys.argv[5] if len(sys.argv) > 5 else 'M'
    t0 = time.time()
    F = lambda z: (Ns*scalw(z[0], z[1], m, vert)[0] + ND*ferm(z[2], z[3], m)[0])[:3]*1e3
    res = least_squares(F, x0, bounds=([0.3, 0.02, 0.3, 0.02], [3.0, 1.0, 1.55, 0.5773]), xtol=1e-15, ftol=1e-15, gtol=1e-15, diff_step=1e-6, max_nfev=120)
    bA, fr, bf, r = res.x
    sv, L = scalw(bA, fr, m, vert); fv, law = ferm(bf, r, m); tot = Ns*sv + ND*fv
    print('content: Ns=%g real scalars on G_w(bA, wA) [%s] + ND=%g Dirac on D1(bf, r); m=%g (nfev %d, %.1fs)' % (Ns, vert, ND, m, res.nfev, time.time()-t0))
    print('knobs: bA=%.10f wA=%.10f (frac %.6f) bf=%.10f r=%.10f' % (bA, fr*(np.pi-bA), fr, bf, r))
    print('scalar per real: %+.6e %+.6e %+.6e | fermion per Dirac: %+.6e %+.6e %+.6e mu_T2 %+.3e' % (*sv[:3], *fv))
    print('TOTAL: Xi_T2g %+.3e Xi_Eg %+.3e mu_E %+.3e | mu_T2 %+.3e' % tuple(tot))
