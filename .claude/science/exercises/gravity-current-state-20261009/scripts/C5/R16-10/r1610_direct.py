"""R16-10: the zero law checked with the refereed R13-7 on-shell runner itself (direct BZ sum, no split), at finite
(m, lam), against the split evaluator at the same (m, lam); and the photon's whole-zone v_max."""
import numpy as np, sys, os, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, 'arch', 'R16-2'))
import r137_onshell, r162_laws
from r1610_eval import *
from r1610_laws import *
t0 = time.time()
G = float(sys.argv[1])
class ZLaw(r162_laws.D1Law):
    def __init__(self, b, r, m, G):
        r162_laws.D1Law.__init__(self, b, r, 1.0, 2.0, m); self._d = photon('R85', 1.0, 2.0, G)
q = np.linspace(0, np.pi, 200001); d = photon('R85', 1.0, 2.0, G); dd = np.gradient(d(q), q)
print('photon R85(1,2,G=%.5f): min d\' = %+.4f, max d\' = %.4f at q = %.3f, d(pi) = %.4f' % (G, dd.min(), dd.max(), q[dd.argmax()], d(np.array(np.pi))))
for (m, lam) in [(0.1, 0.05), (0.05, 0.02)]:
    L = ZLaw(1.4, 1/np.sqrt(3), m, G)
    lp, tp = lattice_part(0.5, 64, m, lam, (L.S, L.W), L.d, 0.25, 0.7, 0.02)
    cp = cont_part(0.5, m, lam, 0.25, 0.7, h=0.004)
    print('m=%.2f lam=%.2f split (N=64): %+.5f' % (m, lam, lp + cp), flush=True)
    for N in (96, 128, 160):
        c2, ct, dE0 = r137_onshell.ce2_minus_1(L, N, lam, min(0.02, 0.3*np.sqrt(2*m*lam)))
        print('m=%.2f lam=%.2f direct R13-7 runner N=%3d: %+.5f  [tadpole %+.5f]' % (m, lam, N, c2/2*U, ct/2*U), flush=True)
print('elapsed %.1fs' % (time.time() - t0))
