"""R16-10 (a): locate the Dirac zero F_1/2(0+) = 0 in the stiffened-photon family
photon R85(c1, c2, G): d = rho_g q + (1 - rho_g) G 2 sin(q/2)  (nondecreasing for G >= pi/2, proved: report 3.4),
matter D1(1.4, 1/sqrt3) (R14-1, subluminal, S <= q).  Checks: N, (r0, r1), h, m, lam."""
import numpy as np, sys, time
from r1610_eval import *
from r1610_laws import *
t0 = time.time()
mode = sys.argv[1]
def F12(G, N=48, r0=0.25, r1=0.7, h=0.02, m=1e-6, lam=0.0, mat=('D1', 1.4, 1/np.sqrt(3)), c=(1.0, 2.0)):
    d = photon('R85', c[0], c[1], G)
    matter = dirac_D1(mat[1], mat[2]) if mat[0] == 'D1' else dirac_lit(mat[1], mat[2])
    lp, tp = lattice_part(0.5, N, m, lam, matter, d, r0, r1, h)
    return K[0.5] + lp, tp
if mode == 'bisect':
    for mat in [('D1', 1.4, 1/np.sqrt(3)), ('D1', 1.0, 1/np.sqrt(3))]:
        a, b = 2.0, 4.0
        Fa, _ = F12(a, mat=mat); Fb, _ = F12(b, mat=mat)
        print(mat, 'F(G=2) %+.5f  F(G=4) %+.5f' % (Fa, Fb), flush=True)
        for it in range(16):
            c = 0.5*(a + b); Fc, _ = F12(c, mat=mat)
            if np.sign(Fc) == np.sign(Fa): a, Fa = c, Fc
            else: b, Fb = c, Fc
        Gs = 0.5*(a + b)
        print(mat, 'zero at G* = %.5f (N=48)' % Gs, flush=True)
if mode == 'checks':
    Gs = float(sys.argv[2]); mat = ('D1', float(sys.argv[3]), 1/np.sqrt(3))
    for kw in [dict(N=48), dict(N=64), dict(N=96), dict(N=64, r0=0.15, r1=0.5), dict(N=64, r0=0.3, r1=0.9),
               dict(N=64, h=0.01), dict(N=64, m=1e-3), dict(N=64, m=1e-3, lam=1e-3), dict(N=64, m=0.01, lam=0.0)]:
        for G in (Gs - 0.05, Gs, Gs + 0.05):
            F, tp = F12(G, mat=mat, **kw)
            print('%s G=%.5f %-40s F(0+) %+.5f [tadpole %+.5f]' % (str(mat), G, str(kw), F, tp), flush=True)
print('elapsed %.1fs' % (time.time() - t0))
