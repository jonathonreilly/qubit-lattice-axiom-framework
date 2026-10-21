"""C4d-04: range 1, G = T: numerical search for general (quantum) T-covariant pair walks W obeying
unitarity + the 3-magnon spectator isometries (U and U^dagger), with a prescribed weight mu on
COM-moving amplitudes.  Evidence only (local optimisation); the exact statement is c4d_05."""
import sys, time, json
import numpy as np
from scipy.optimize import least_squares
from c4d_common import check, total, T
from c4d_quantum import PairWalkSpace, build_constraints
from c4d_solver import compile_system, moving_mask, make_fun, bloch

t0 = time.time()
S = PairWalkSpace(T, 1)
unit, spec = build_constraints(S)
sysd = compile_system(S, unit, spec)
print(f"nvar={S.nvar} residual rows={sysd['nr']} build {time.time()-t0:.1f}s", flush=True)
mv, mult = moving_mask(S)
n = S.nvar
rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv) > 1 else 1)

# baseline: identity solves everything
fun0, jac0 = make_fun(sysd)
from c4d_common import pair
xid = np.zeros(n, complex)
for k, (rho0, s, m) in enumerate(S.var_info):
    if s == pair((0, 0, 0), rho0):
        xid[k] = 1
check("identity W solves the system exactly", np.max(np.abs(fun0(np.concatenate([xid.real, xid.imag])))) < 1e-14)

results = {}
for mu in (0.0, 0.02, 0.1, 0.3):
    def g(x, mu=mu):
        return 10.0 * (np.sum(mult[mv] * np.abs(x[mv]) ** 2) - mu)

    def dg(x):
        ga = 10.0 * 2 * mult * mv * x.real
        gb = 10.0 * 2 * mult * mv * x.imag
        return np.concatenate([ga, gb])
    fun, jac = make_fun(sysd, extra=(g, dg))
    best = []
    for trial in range(6):
        z0 = rng.normal(size=2 * n) * 0.4
        sol = least_squares(fun, z0, jac=jac, method="trf", x_scale="jac", max_nfev=400, xtol=1e-14, ftol=1e-14, gtol=1e-14)
        x = sol.x[:n] + 1j * sol.x[n:]
        cost = float(np.sum(sol.fun ** 2))
        mvw = float(np.sum(mult[mv] * np.abs(x[mv]) ** 2))
        best.append((cost, mvw))
        print(f"mu={mu} trial={trial} cost={cost:.3e} moving_weight={mvw:.3e}", flush=True)
    results[mu] = min(best)
check("mu=0: optimiser reaches an exact solution (sanity)", results[0.0][0] < 1e-12, str(results[0.0]))
for mu in (0.02, 0.1, 0.3):
    print(f"mu={mu}: best cost {results[mu][0]:.3e}")
check("mu>0: no near-solution with moving weight found (best cost >= 1e-4 for all mu>0)",
      all(results[mu][0] > 1e-4 for mu in (0.02, 0.1, 0.3)), str({k: v[0] for k, v in results.items()}))
total()
