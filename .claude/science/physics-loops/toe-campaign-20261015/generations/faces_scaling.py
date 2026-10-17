import numpy as np, itertools
from scipy.optimize import least_squares
import coinfast as CF, coinrep as CR
rep = 'E12+H'
d, N, J, K, pairs, nz = CF.build(rep)
rng = np.random.default_rng(5)
for delta in (0.02, 0.05, 0.1, 0.2, 0.4):
    fun, jac, unpack = CF.make(d, N, J, K, pairs, nz, delta)
    best = 1e9
    for t in range(6):
        r = least_squares(fun, rng.normal(size=2 * J) * rng.choice([0.3, 1.0]), jac=jac, xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=8000)
        best = min(best, np.linalg.norm(r.fun))
    print(f'delta {delta}: best residual {best:.3e}', flush=True)
