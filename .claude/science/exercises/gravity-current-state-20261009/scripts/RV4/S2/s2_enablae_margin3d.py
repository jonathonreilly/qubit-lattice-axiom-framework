"""E∇E class trade-off in 3D (range<=3, L=32): does a common zero mu_E = mu_T2 = 0 (M=1) survive as the no-doubler margin
min_k Phi/Phi_NN >= m0 is raised?  Distance measured on the FULL coefficient vector b (incl. the nearest-neighbour orbit).
Also reports the quartic anisotropy (alpha, beta; NN: -1/24, 0) and the IR-log combinations (12 alpha - 2 beta, beta)."""
import numpy as np
from scipy.optimize import minimize
from s2_enablae_lib import Model, b_from_free
import sys
import sys
d, L, r = 3, 32, int(sys.argv[1]) if len(sys.argv) > 1 else 3
Mo = Model(d, L, r); qs = Mo.qs; j0 = qs.index((1, 0, 0))
bNN = np.zeros(len(qs)); bNN[j0] = d; xNN = np.delete(bNN, j0)
rng = np.random.default_rng(11)
for M in [1.0]:
    FM = Mo.mus(bNN, M)[0]
    for m0 in [0.2, 0.6]:
        cons = [{'type': 'eq', 'fun': lambda x: np.array(Mo.mus(b_from_free(x, Mo.norm, j0), M)[:2])/FM},
                {'type': 'ineq', 'fun': lambda x, m0=m0: Mo.costs(b_from_free(x, Mo.norm, j0))['min_ratio'] - m0}]
        best = None
        for s in range(3):
            x0 = xNN + 0.03*s*rng.standard_normal(len(xNN))
            rr = minimize(lambda x: np.sum((b_from_free(x, Mo.norm, j0) - bNN)**2), x0, constraints=cons, method='SLSQP',
                          options={'maxiter': 150, 'ftol': 1e-14})
            v = np.abs(cons[0]['fun'](rr.x)).max(); ok = cons[1]['fun'](rr.x) > -1e-8
            if v < 1e-9 and ok and (best is None or rr.fun < best.fun): best = rr
        if best is None:
            # report how close one gets: minimise residual subject to margin
            rr = minimize(lambda x: np.sum(cons[0]['fun'](x)**2), xNN, constraints=[cons[1]], method='SLSQP', options={'maxiter': 400, 'ftol': 1e-20})
            print(f"M={M} margin>={m0}: NO common zero found; min residual (mu/F_NN)^2 = {rr.fun:.3e}"); sys.stdout.flush(); continue
        b = b_from_free(best.x, Mo.norm, j0); cst = Mo.costs(b)
        print(f"M={M} margin>={m0}: common zero, |b-b_NN|={np.sqrt(best.fun):.3f}; alpha={cst['alpha']:+.3f} beta={cst['beta']:+.3f} "
              f"(12a-2b={12*cst['alpha']-2*cst['beta']:+.3f}); vmax={cst['vmax']:.3f}; mu at M=0.3: " +
              " ".join(f"{z/Mo.mus(bNN,0.3)[0]:+.3f}" for z in Mo.mus(b, 0.3)[:2]) + " (/F_NN)"); sys.stdout.flush()
