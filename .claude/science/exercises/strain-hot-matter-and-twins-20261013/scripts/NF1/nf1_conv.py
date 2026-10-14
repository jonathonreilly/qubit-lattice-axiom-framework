"""NF-1 (b), (c): converged numbers on F1's octant panel grids via the archived F1/F3 libraries (copies, imports repointed only),
applied to the staggered law through the exact dictionary Gamma_j <-> alpha_j x 1_2, Gamma_eps <-> beta x 1_2 (nf1_alg.py item 6;
the direct 8x8 evaluator agrees with F3's reduced formula to <= 1e-16 on a common grid, nf1_sigma8_*.out).
Parts (argv[1]):
  A  staggered additive mass and its SF E_g Hessian (FermC(0): r = 0, no Wilson term; F1 dm_sf, Psym, own flows, critical m = 0);
  B  control: F3's G1 (and G2) dressing linear response L = d dm/d eps at t = 0 (Hess_t = 2 a L), F3 lin_resp;
  C  control: eps-Wilson r_c sum sin^2 k_j Gamma_eps, additive mass and SF Hessian (critical mass fixed at t = 0);
  M  multiplicative channel: z(m) = [Sigma(m) - Sigma(0)]/m and z'' = [Hess(m) - Hess(0)]/m at P = 0 (F5's estimator, f5_mult.py).
argv: part n hmax mph d"""
import numpy as np, sys, os, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', 'flat'))
import f1_lib as L
from f3_lib import lin_resp
from sublum import SymS
t00 = time.time()
part = sys.argv[1]; n, hm, mph, d = int(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4]), float(sys.argv[5])
BF = L.ROOT[0]
A = SymS(BF); G = L.Phot(L.CPH)


class FermC:
    def __init__(self, rc, mflow=0.01):
        self.rc, self.mflow = rc, mflow
    def s(self, k): return A.s(k)
    def ds(self, k): return A.ds(k)
    def W(self, k): return self.rc*np.sin(k)**2
    def dW(self, k): return self.rc*np.sin(2*k)
    def p2(self, kx, ky, Wz):
        M = self.mflow + self.W(kx) + self.W(ky) + Wz
        return self.s(kx)*self.ds(kx) + M*self.dW(kx), self.s(ky)*self.ds(ky) + M*self.dW(ky)


br = [BF, np.pi - BF] + [L.CPH + i*(np.pi - L.CPH)/mph for i in range(mph)]
g = L.Grid(br, n, hm)
print('NF-1 part %s; grid n=%d hmax=%.2f mph=%d (%d nodes), d=%.4f; staggered edge s = SymS(%.9f), photon Gph(%.4f); per e^2, SF units'
      % (part, n, hm, mph, len(g.x), d, BF, L.CPH), flush=True)


def hessE(F, **kw):
    f0 = L.dm_sf(F, G, g, 0.0, nrk=2, **kw); f1 = L.dm_sf(F, G, g, d, nrk=2, **kw); f2 = L.dm_sf(F, G, g, 2*d, nrk=2, **kw)
    h1 = 2*(f1 - f0)/d**2; h2 = 2*(f2 - f0)/(2*d)**2
    return f0, h1, h2, (4*h1 - h2)/3


if part == 'A':
    F = FermC(0.0)
    for t in (0.0, d, 2*d, -d, 0.05, 0.2):
        tot, tad, loop = L.dm_sf(F, G, g, t, nrk=2, parts=True)
        print('  staggered t=%+.4f: dm %+.3e (tadpole %+.1e, exchange %+.1e)' % (t, tot, tad, loop), flush=True)
    f0, h1, h2, hr = hessE(F)
    print('  staggered Hess_t: (d) %+.3e (2d) %+.3e Rich %+.3e   [reference: F1 Wilson root +2.42401e-2]' % (h1, h2, hr))
    # same law with the root's Wilson term restored (F1 control, should reproduce F1 B1 on this grid)
    Fw = L.Ferm(*L.ROOT, mflow=0.01)
    f0, h1, h2, hr = hessE(Fw)
    print('  check: Wilson root D1(%.9f, %.9f) on this grid: dm %+.9f Hess_t Rich %+.7e (F1 B1: +0.041858390, +2.4240e-2)' % (*L.ROOT, f0, hr))
elif part == 'B':
    F = L.Ferm(BF, 0.0, mflow=0.01)                 # D1(b_f, r = 0) == staggered via the dictionary
    for nm in ('G1', 'G2'):
        L1, L2, Lr, f0 = lin_resp(F, G, g, nm, d=1e-3)
        print('  %s dressing on the staggered law: L (eps=1e-3) %+.7e (2e-3) %+.7e Rich %+.7e ; undressed dm %+.1e' % (nm, L1, L2, Lr, f0), flush=True)
        print('     -> Hess_t = 2 a L: a = 1 gives %+.4e ; a = 0.0141 (F3 a*) gives %+.4e ; |Hess| >= 1e-3 e^2 for |a| >= %.2e'
              % (2*Lr, 2*0.0141*Lr, 1e-3/(2*abs(Lr))))
elif part == 'C':
    for rc in (0.05, 0.1, 0.3):
        F = FermC(rc)
        f0, h1, h2, hr = hessE(F)
        print('  eps-Wilson r_c=%.2f: dm(t=0) %+.9f  Hess_t (d) %+.7e (2d) %+.7e Rich %+.7e  Hess/dm %+.4f' % (rc, f0, h1, h2, hr, hr/f0), flush=True)
elif part == 'M':
    F = FermC(0.0)
    res = {}
    for m in (0.0, 0.0025, 0.005, 0.01, 0.02):
        f0, h1, h2, hr = hessE(F, mprop=m)
        res[m] = (f0, hr)
        print('  m=%.4f  Sigma_eps(P=0) %+.10f  Hess_t %+.7e' % (m, f0, hr), flush=True)
    S0, H0 = res[0.0]
    for m in (0.0025, 0.005, 0.01, 0.02):
        print('  m=%.4f  z(m) = %+.6f   z\'\' = [Hess(m)-Hess(0)]/m = %+.6e' % (m, (res[m][0] - S0)/m, (res[m][1] - H0)/m))
print('time %.0f s' % (time.time() - t00))
