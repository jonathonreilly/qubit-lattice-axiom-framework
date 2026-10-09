"""E1 (3+1): validate the smeared 4D BD operator on sprinkled diamonds.
b = B/P, P=(4/sqrt6) rho_k^{1/2}; continuum: b1 -> 0, b(x^2) -> 2/P = 1.2247, b(t^2) -> -1.2247
(box = -dt^2 + grad^2), rho_k = 1. Targets: elements with t > T - 0.6 near the top vertex."""
import numpy as np, time, sys
from math import sqrt
from bd_core import sprinkle4d, bd4d_targets
rng = np.random.default_rng(4)
for eps, T, nreal in [(0.2, 5.0, 30), (0.1, 6.0, 20), (0.05, 7.0, 8)]:
    t0 = time.time(); vals = []; gains = []; ns = []
    for r in range(nreal):
        P = sprinkle4d(1/eps, T, rng)
        tg = np.nonzero(P[:, 0] > T - 0.6)[0]
        xc = P[tg]
        F = np.vstack([np.ones(len(P)), P[:, 1]**2, P[:, 0]**2])
        # shift quadratic fields to target origin: phi = (x - x_x)^2 handled by box const
        out, gain, nsh = bd4d_targets(P, tg, eps, F, F[:, tg])
        vals.append(out); gains.append(gain); ns.append(nsh)
    o = np.vstack(vals); R = np.array([v.mean(0) for v in vals])
    se = R.std(0, ddof=1)/sqrt(len(R))
    print(f"eps={eps} T={T} N~{len(P)} targets={o.shape[0]} <shell>={np.concatenate(ns).mean():.0f}"
          f"  b1={o[:,0].mean():+.4f}+-{se[0]:.4f} (sd/elem {o[:,0].std():.3f})"
          f"  b(x^2)={o[:,1].mean():+.3f}+-{se[1]:.3f}  b(t^2)={o[:,2].mean():+.3f}+-{se[2]:.3f}"
          f"  <A^2>={np.concatenate(gains).mean():.3f}  [{time.time()-t0:.0f}s]", flush=True)
