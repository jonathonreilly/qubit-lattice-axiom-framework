"""Channel B: (i) prove-by-check that mu1 = mu2 is an exactly flat (theta-blind) line; (ii) width of any D2h window near it."""
import numpy as np
from t3_landau import *
Ss, W = multiset_S(48)
rng = np.random.default_rng(3)
for mJ in (0.0, 0.1):
    M = massmat(0.2, mJ, 1.0, 1.0, 0.5 * np.ones(7), np.linspace(0, 2*np.pi, 7))
    ev = np.sort(np.linalg.eigvalsh(M), -1)
    print(f'mu1=mu2, mJ={mJ}: eigenvalue spread over theta {np.ptp(ev,0)}  (theta-blind spectrum => V flat)')
for ph in np.radians(np.arange(40, 50.01, 0.5)):
    pars = (0.2, 0.0, np.cos(ph), np.sin(ph))
    out = []
    for rho in (0.1, 0.3, 0.6, 1.0):
        V = V_B(pars, np.full(TH.size, rho), TH, Ss, W)
        t = ang_min(V); out.append(f'{rho}:{classify(t)}({np.degrees(t):.1f},dV={np.ptp(V):.1e})')
    print(f'phi={np.degrees(ph):5.1f}  ' + '  '.join(out))
