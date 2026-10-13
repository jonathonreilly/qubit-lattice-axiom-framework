"""R17-10 §3.7: fast-slice shear form mu_E = (1/(12 Gamma(3/2))) int t^{-3/2} e^{-tm^2} Phi^3 x (5x - 1/2 + m^2 t) dt  vs the moment form. The fast form has a t^{-1/2} integrable singularity at t -> 0, so the log-t grid starts at e^{-44} (at e^{-16} the cut-off tail is ~1e-4)."""
import numpy as np
from math import gamma
L = 50; lev = np.linspace(0.15, np.pi, L); rng = np.random.default_rng(3)
for trial in range(4):
    M = rng.exponential(1.0, L)*(rng.uniform(size=L) < 0.3); b = rng.uniform(0.2, 1.0); M *= (np.pi-b)/M.sum(); m = [0.01, 0.1, 0.03, 0.01][trial]
    u = np.linspace(-44.0, np.log(80.0/(m*m)) + 2, 12000); t = np.exp(u); du = u[1]-u[0]
    xg, wg = np.polynomial.legendre.leggauss(400); kb = 0.5*b*(xg+1); wb = 0.5*b*wg
    mom = lambda p: (np.exp(-np.outer(t, kb*kb))@(wb*kb**p) + np.exp(-np.outer(t, lev**2))@(M*lev**p))/np.pi
    E0, F2, F4 = mom(0), mom(2), mom(4)
    mu_mom = np.sum(t*du*t**0.5*np.exp(-t*m*m)*E0*(3*F2**2 - F4*E0))/(12*gamma(1.5))
    X = t*F2/E0; mu_fast = np.sum(t*du*t**-1.5*np.exp(-t*m*m)*E0**3*X*(5*X - 0.5 + m*m*t))/(12*gamma(1.5))
    print('b=%.2f m=%.2f: mu_E moment %+.10e fast form %+.10e diff %.1e' % (b, m, mu_mom, mu_fast, abs(mu_mom-mu_fast)))
