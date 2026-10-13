"""F3 (b)/(c) direct check: the full SF-strained law with the O(t^2) dressing V_t = exp(i t^2 a G1(k)) applied to D(Phi_t k)
(F1 branch B1: Dirac flow at m = 0.01, photon own flow, Psym, Feynman gauge, critical m = 0), Hessian by finite differences in t
exactly as f1_root.py (t = 0, d, 2d; evenness dm(-t) = dm(t)).  Compare with the reduction Hess(a) = Hess(0) + 2 a L_G1.
a = 0 must reproduce F1 (f1_root_conv.out:2 at 156 nodes: Rich +2.4238554e-02)."""
import numpy as np, time, sys
from f3_lib import *
t00 = time.time()
F = Ferm(*ROOT, mflow=0.01); G = Phot(CPH)
gi = int(sys.argv[1]) if len(sys.argv) > 1 else 0
nm = sys.argv[2] if len(sys.argv) > 2 else 'G1'
Lg = float(sys.argv[3]) if len(sys.argv) > 3 else -0.8585829730     # L_G at the same grid (f3_resp_main.out)
n, hm, mph = ((6, 0.25, 6), (8, 0.25, 10))[gi]
g = mkgrid(ROOT[0], n, hm, mph)
d = 0.003
def dm(t, a):
    dx, dy, dz = photon_syms(G, g.x, t, nrk=2)
    return dm_gen(make_cM(F, t, nm if a != 0 else None, a=a, nrk=2), dx, dy, dz, g.x, g.w)
f0 = dm(0.0, 0.0)
H0 = None
print('F1 branch B1 + dressing %s, grid n=%d hmax=%.2f mph=%d (%d nodes), d = %.4f; L_%s = %+.10e (t = 0 response, same grid)'
      % (nm, n, hm, mph, len(g.x), d, nm, Lg))
for a in (0.0, None, 'neg'):
    t0 = time.time()
    if a is None:
        a = -H0/(2*Lg)          # predicted zero
    elif a == 'neg':
        a = -0.05
    f1 = dm(d, a); f2 = dm(2*d, a)
    h1 = 2*(f1 - f0)/d**2; h2 = 2*(f2 - f0)/(2*d)**2; hr = (4*h1 - h2)/3
    if H0 is None:
        H0 = hr
        fm = dm(-d, a)
        print('   evenness at a = 0: dm(+d) - dm(-d) = %.1e' % (f1 - fm))
    pred = H0 + 2*a*Lg
    print('   a = %+.8f: Hess_t (d) %+.7e (2d) %+.7e Rich %+.7e ; predicted Hess(0) + 2 a L = %+.7e ; diff %.1e  (%.0fs)'
          % (a, h1, h2, hr, pred, hr - pred, time.time() - t0), flush=True)
print('time %.0f s' % (time.time() - t00))
