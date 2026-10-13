"""R16-13: content Ns real scalars on R16-3's simplex mix (A = G(1.0), C2 = Zz(1.0,.35,.47,.03), C = Zz(1.0,.35,.43,.03)),
sigma' = (1-u-v) A + u C2 + v C  [M vertex] + ND Dirac on DG(bf, wf, r). Knobs (u, v, bf, wf-frac, r)."""
import numpy as np, sys, time
import dfam
from zz import ZLaw, Mix, xi_all, mu_E
from floor_scan import Zz
from scipy.optimize import least_squares
A = ZLaw([1.0, 0.0], [1.0 + (np.pi-1.0)/2], np.pi-1.0, nf=1 << 16)
C2 = Zz(1.0, 0.35, 0.47, 0.03); C = Zz(1.0, 0.35, 0.43, 0.03)
def scal(u, v, m, vert='M'):
    L = Mix([A, C2, C], [1-u-v, u, v]); g, f = L.samples(1 << 14)
    x = xi_all(g, f, m, nu=1500)
    return np.array([x[vert+',T2g'], x[vert+',Eg'], mu_E(g, f, m, nu=1500), 0.0]), L
def ferm(bf, fr, r, m, q=(3, 8)):
    law = dfam.DG(bf, fr*(np.pi/2 - bf), r, nf=100001)
    o = dfam.evaluate(law, m, *q)
    return np.array([o['T2g'], o['Eg'], o['muE'], o['muT2']]), law
if __name__ == '__main__':
    Ns, ND, m = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])
    x0 = np.array([float(v) for v in sys.argv[4].split(',')])
    t0 = time.time()
    def F(z):
        u, v, bf, fr, r = z
        pen = max(0.0, u + v - 1.0)*1e2
        return (Ns*scal(u, v, m)[0] + ND*ferm(bf, fr, r, m)[0])[:3]*1e3 + pen
    res = least_squares(F, x0, bounds=([0, 0, 0.3, 0.05, 0.02], [1, 1, 1.5, 1.0, 0.5773]), xtol=1e-15, ftol=1e-15, gtol=1e-15, diff_step=1e-6, max_nfev=150)
    u, v, bf, fr, r = res.x
    sv, L = scal(u, v, m); fv, law = ferm(bf, fr, r, m); tot = Ns*sv + ND*fv
    print('content Ns=%g (R16-3 simplex, M) + ND=%g DG; m=%g (nfev %d, %.1fs)' % (Ns, ND, m, res.nfev, time.time()-t0))
    print('knobs u=%.10f v=%.10f (1-u-v %.6f) bf=%.10f wf=%.10f r=%.10f' % (u, v, 1-u-v, bf, fr*(np.pi/2-bf), r))
    print('scalar per real: %+.6e %+.6e %+.6e | fermion per Dirac: %+.6e %+.6e %+.6e mu_T2 %+.3e' % (*sv[:3], *fv))
    print('TOTAL: Xi_T2g %+.3e Xi_Eg %+.3e mu_E %+.3e | mu_T2 %+.3e' % tuple(tot))
    np.save('root5_%g_%g.npy' % (Ns, ND), np.array([Ns, ND, m, u, v, bf, fr, r]))
