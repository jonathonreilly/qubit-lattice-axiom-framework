"""F6 control branch: R19-31's NN scalar edge (eps^2 = m^2 + sum 4 sin^2(k/2)) with the NN photon (d = 2 sin(q/2)) under SF instead of H-cov.
Identical dispersions -> one common separable flow -> exact relabelling (F1's lemma): Sig_g(t) = 3 G_gam(t) at m = 0 and the Hessian is
pure Jacobian (Liouville) term.  Also the NN scalar with the ROOT photon Gph(2.9435) (mismatched flows)."""
import numpy as np
from f6_lib import *
class NN:
    def d(self, q): return 2*np.sin(np.asarray(q, float)/2)
    def p1(self, q): return np.sin(np.asarray(q, float))
S = NN(); G = Phot(CPH)
x, w = panels([2.2], 8, 0.15)
r = hess_even(lambda t: sig_gauge(S, S, x, w, t), 0.0015)
print('NN scalar + NN photon, SF, m=0: Sig(0) %.9f (R19-31 H-cov at m=0.1: 0.683593)  Hess_t %+.6e   [H-cov comparator -0.53181/4 = %+.5f per t^2]' % (r[0], r[3], -0.53181/4))
r2 = hess_even(lambda t: 3*g_scalar(S, x, w, t), 0.0015)
print('   3 G_gam Hessian (relabelling identity, must equal) %+.6e' % r2[3])
xg, wg = mkgrid(2.2, 8, 0.15, 16)
r3 = hess_even(lambda t: sig_gauge(S, G, xg, wg, t), 0.0015)
print('NN scalar + root photon Gph(2.9435), SF, m=0: Sig(0) %.9f Hess_t %+.6e' % (r3[0], r3[3]))
r4 = hess_even(lambda t: g_scalar(S, x, w, t), 0.0015)
print('NN scalar quartic loop: d2_t G_s %+.6e' % r4[3])
