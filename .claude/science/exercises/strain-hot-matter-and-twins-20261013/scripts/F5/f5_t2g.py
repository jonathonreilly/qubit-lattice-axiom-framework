"""F5 (a)/(c): the T2g Hessian of the one-loop additive mass on F1's SF law (branch B1, Psym), i.e. the second coefficient
the rule's counterterm m_c(h) carries at O(h^2) (cubic symmetry: one E_g and one T2g quadratic invariant for traceless h).
Unit T2g strain h = e_x e_y + e_y e_x (same Frobenius norm as F1's diag(1,-1,0)); SF units t.  dm(-t) = dm(t) (C4 about z maps
h_xy -> -h_xy), so Hess = 2[dm(d) - dm(0)]/d^2 with Richardson over d, 2d.  Domain x in [-pi, pi], y, z in [0, pi]
(validated in f5_validate.out (3)).  argv: n hmax mph d [root0]"""
import numpy as np, time, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from f5_lib import *
t00 = time.time()
n, hm, mph, d = int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4])
which = sys.argv[5] if len(sys.argv) > 5 else 'root'
rt = ROOT0 if which == 'root0' else ROOT
mflow = 0.0 if which == 'B2' else 0.01
F = Ferm(*rt, mflow=mflow); G = Phot(CPH)
br = mkbreaks(rt[0], CPH, mph)
xo = panels(br, n, hm); xs = panels_sym(br, n, hm)
print('T2g Hessian, %s D1%s mflow=%.2f, Gph(%.4f); grid n=%d hmax=%.2f mph=%d (%d nodes/half-axis), d=%.4f'
      % (which, str(rt), mflow, CPH, n, hm, mph, len(xo[0]), d), flush=True)
f0 = dm_gen(F, G, H_T2, xs, xo, xo, 0.0)
f1 = dm_gen(F, G, H_T2, xs, xo, xo, d); f2 = dm_gen(F, G, H_T2, xs, xo, xo, 2*d)
h1 = 2*(f1 - f0)/d**2; h2 = 2*(f2 - f0)/(2*d)**2
print('  dm0 %+.10f  dm(d) %+.13e dm(2d) %+.13e' % (f0, f1, f2))
print('  Hess_T2g (d) %+.7e (2d) %+.7e  Rich %+.7e   [%.0f s]' % (h1, h2, (4*h1 - h2)/3, time.time() - t00), flush=True)
if len(sys.argv) > 6 and sys.argv[6] == 'parts':
    _, ta0, lo0 = dm_gen(F, G, H_T2, xs, xo, xo, 0.0, parts=True)
    _, ta1, lo1 = dm_gen(F, G, H_T2, xs, xo, xo, d, parts=True)
    _, ta2, lo2 = dm_gen(F, G, H_T2, xs, xo, xo, 2*d, parts=True)
    R = lambda a0, a1, a2: (4*2*(a1 - a0)/d**2 - 2*(a2 - a0)/(2*d)**2)/3
    print('  parts: tadpole Hess %+.6e  exchange Hess %+.6e' % (R(ta0, ta1, ta2), R(lo0, lo1, lo2)))
    for lab, kw in (('photon unstrained', dict(phot_on=False)), ('fermion unstrained', dict(ferm_on=False))):
        g0 = dm_gen(F, G, H_T2, xs, xo, xo, 0.0, **kw); g1 = dm_gen(F, G, H_T2, xs, xo, xo, d, **kw)
        g2 = dm_gen(F, G, H_T2, xs, xo, xo, 2*d, **kw)
        print('  control %-20s Hess %+.6e' % (lab, R(g0, g1, g2)), flush=True)
print('time %.0f s' % (time.time() - t00))
