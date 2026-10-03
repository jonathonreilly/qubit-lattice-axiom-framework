"""Gauss-Newton (min-norm pseudo-inverse steps) on the unitarity equations only
(no tau constraint), from the free-run near-solution.  Quadratic convergence to
zero residual would indicate an exact nontrivial covariant walk; stagnation at
a positive residual indicates a genuine local minimum (near miss)."""
import sys
import numpy as np
from scipy.optimize import least_squares

sys.argv = ['covariant_walk_search.py', '2', '0', '11']
exec(open('covariant_walk_search.py').read().split("t0 = time.time()")[0])

x = np.load('polished_tau1.0.npy')
sol = least_squares(resid, x, jac=jac, args=(0.0, 0.0), method='lm', xtol=1e-15,
                    ftol=1e-15, gtol=1e-15, max_nfev=20000)
x = sol.x
for it in range(25):
    r = resid(x, 0.0, 0.0)[:-1]
    J = jac(x, 0.0, 0.0)[:-1]
    u, s, vh = np.linalg.svd(J, full_matrices=False)
    c = unpack(x)
    wmov = np.real(c.conj() @ (gram * np.outer(mov, mov)) @ c)
    if it % 3 == 0 or it < 4:
        print(f"it {it}: |r|^2 = {r @ r:.3e}, moving weight {wmov:.5f}, "
              f"sing.vals: max {s[0]:.2e}, min {s[-1]:.2e}, #<1e-8: {np.sum(s < 1e-8)}")
    keep = s > 1e-10 * s[0]
    step = vh[keep].T @ ((u[:, keep].T @ r) / s[keep])
    x = x - step
np.save('gn_point.npy', x)
# gradient norm at the end (stationarity of |r|^2)
r = resid(x, 0.0, 0.0)[:-1]
J = jac(x, 0.0, 0.0)[:-1]
print(f"final |r|^2 = {r @ r:.3e}, |J^T r| = {np.linalg.norm(J.T @ r):.3e}")
