"""Continuation scan of the moving weight tau for rho=2 covariant walks:
warm-start from neighbouring tau, plus a few fresh starts; record the minimal
unitarity residual as a function of tau.  Also a free-tau run (lam=0) from the
best near-solution to see whether it flows to an exact nontrivial solution."""
import sys
import time
import numpy as np
from scipy.optimize import least_squares

sys.argv = ['covariant_walk_search.py', '2', '0', '11']
exec(open('covariant_walk_search.py').read().split("t0 = time.time()")[0])

t0 = time.time()
x = np.load('polished_tau1.0.npy')
taus = np.round(np.concatenate([np.arange(1.0, 0.0, -0.1), np.arange(1.1, 2.01, 0.1)]), 2)
res = {}
xs = {1.0: x}
prev = x
for i, tau in enumerate(taus):
    if tau == 1.1:
        prev = xs[1.0]
    sol = least_squares(resid, prev, jac=jac, args=(tau,), method='lm', xtol=1e-15,
                        ftol=1e-15, gtol=1e-15, max_nfev=3000)
    res[tau] = float(np.sum(sol.fun ** 2))
    prev = sol.x
    xs[tau] = sol.x
print("tau -> min residual^2 (continuation):")
print("  " + ", ".join(f"{t:.1f}:{res[t]:.1e}" for t in sorted(res)))
# free tau: drop the constraint, start from the tau=1 near solution
sol = least_squares(resid, xs[1.0], jac=jac, args=(0.0, 0.0), method='lm', xtol=1e-15,
                    ftol=1e-15, gtol=1e-15, max_nfev=20000)
c = unpack(sol.x)
wmov = np.real(c.conj() @ (gram * np.outer(mov, mov)) @ c)
print(f"free run: residual^2 = {np.sum(sol.fun[:-1]**2):.3e}, moving weight = {wmov:.4f}")
print(f"time {time.time() - t0:.1f}s")
