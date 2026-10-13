"""R16-13: content Ns real scalars on R14-1's G(bA) [M or U vertex, zz.py Laplace] + ND 4-comp Dirac on R14-1's D1(bf, r)
[vielbein vertex V0, dfam GL quadrature]. Knobs (bA, bf, r): root of Xi_T2g = Xi_Eg = mu_E = 0 (totals) at m."""
import numpy as np, sys, time
import dfam
from dirac import D1
from zz import ZLaw, xi_all, mu_E
from scipy.optimize import least_squares
class D1q(D1):
    def breaks(self): return [0.0, self.b, np.pi - self.b, np.pi]
    def tables(self, k):
        return self.S(k), self.dS(k), self.d2S(k), self.W(k), self.dW(k), self.d2W(k)
def scal(bA, m, vert='M', n=1 << 14, nu=1500):
    L = ZLaw([1.0, 0.0], [bA + (np.pi-bA)/2], np.pi-bA); g, f = L.samples(n)
    x = xi_all(g, f, m, nu=nu)
    return np.array([x[vert+',T2g'], x[vert+',Eg'], mu_E(g, f, m, nu=nu), 0.0]), L
def ferm(bf, r, m, q=(3, 8)):
    law = D1q(bf, r)
    o = dfam.evaluate(law, m, *q)
    return np.array([o['T2g'], o['Eg'], o['muE'], o['muT2']]), law
if __name__ == '__main__':
    Ns, ND, m = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])
    x0 = np.array([float(v) for v in sys.argv[4].split(',')]); vert = sys.argv[5] if len(sys.argv) > 5 else 'M'
    t0 = time.time()
    F = lambda z: (Ns*scal(z[0], m, vert)[0] + ND*ferm(z[1], z[2], m)[0])[:3]*1e3
    res = least_squares(F, x0, bounds=([0.3, 0.3, 0.02], [3.0, 1.55, 0.5773]), xtol=1e-15, ftol=1e-15, gtol=1e-15, diff_step=1e-6, max_nfev=80)
    bA, bf, r = res.x
    sv, L = scal(bA, m, vert); fv, law = ferm(bf, r, m); tot = Ns*sv + ND*fv
    print('content: Ns=%g real scalars on G(bA) [%s vertex] + ND=%g Dirac on D1(bf, r); m=%g  (nfev %d, %.1fs)' % (Ns, vert, ND, m, res.nfev, time.time()-t0))
    print('knobs: bA=%.10f  bf=%.10f  r=%.10f   (r_max=1/sqrt3=0.5773503)' % (bA, bf, r))
    print('scalar per real: Xi_T2g %+.6e Xi_Eg %+.6e mu_E %+.6e' % tuple(sv[:3]))
    print('fermion per Dirac: Xi_T2g %+.6e Xi_Eg %+.6e mu_E %+.6e mu_T2 %+.6e  W_pi %.4f' % (*fv, law.Wpi))
    print('TOTAL: Xi_T2g %+.3e Xi_Eg %+.3e mu_E %+.3e | mu_T2 %+.3e' % tuple(tot))
    np.save('root3_%g_%g_%s.npy' % (Ns, ND, vert), np.array([Ns, ND, m, bA, bf, r]))
