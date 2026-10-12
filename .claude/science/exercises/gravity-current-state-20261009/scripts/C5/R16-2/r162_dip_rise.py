"""R16-2: inside C but beyond the tested families: edges with S <= q on [b, pi] yet S' > 1 somewhere ("dip and rise"):
S = rho k + (1 - rho)(sin k - (beta/2) sin 2k), box (0.5, 1.5); naive photon. Lemma T' bounds the tadpole; does the
remainder stay small, i.e. is F_1/2 still < 0? Reports max S', max(S - k) on [0, pi], F at m = 0.2, 0.1 (literal edge:
F even in m), the tadpole and the Lemma T' bound. Subtractions: none."""
import numpy as np, sys, time
sys.path.insert(0, '.')
from r85_box_qed_copy import Law, plateau, deriv
from r162_dirac_scan import ce2, hstep
class DLaw(Law):
    def __init__(self, b1, b2, beta, m):
        super().__init__(b1, b2, 0.0, None, None, m, naive_photon=True); self.beta = beta
    def S(self, k):
        rho = plateau(k, self.b1, self.b2); return rho*k + (1 - rho)*(np.sin(k) - 0.5*self.beta*np.sin(2*k))
t0 = time.time(); lam = 0.02; kk = np.linspace(0, np.pi, 200001)
for N in (128, 192):
    for beta in (0.0, 0.5, 1.0, 1.5, 2.0, 3.0):
        L = DLaw(0.5, 1.5, beta, 0.1); Sp = deriv(L.S, kk); exc = np.max(L.S(kk) - kk)
        r = [ce2(DLaw(0.5, 1.5, beta, m), N, lam, hstep(m, lam)) for m in (0.2, 0.1)]
        print('dip-rise beta=%.1f N=%d | max S\' %.3f, min S\' %.3f, max(S-k) %+.3e (in C: %s) | F(0.2) %+8.4f F(0.1) %+8.4f [tad %+8.4f; bound -7.16 (lam 0.05)] rest %+7.3f'
              % (beta, N, Sp.max(), Sp.min(), exc, exc <= 1e-12, r[0][0], r[1][0], r[1][1], r[1][0] - r[1][1]), flush=True)
print('elapsed %.1fs' % (time.time() - t0))
