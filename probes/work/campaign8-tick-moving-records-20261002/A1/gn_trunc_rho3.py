"""Truncated-SVD Gauss-Newton on the rho=3 near-solution: steps only along
well-conditioned directions.  Quadratic decay of |r| to machine precision is
the signature of an exact solution."""
import sys
import time
import numpy as np

sys.argv = ['covariant_walk_search.py', '3', '0', '12']
exec(open('covariant_walk_search.py').read().split("t0 = time.time()")[0])
t0 = time.time()
x = np.load('rho3_point.npy')
for thr in [1e-6, 1e-7, 1e-8]:
    for it in range(4):
        r = resid(x, 0.0, 0.0)[:-1]
        J = jac(x, 0.0, 0.0)[:-1]
        u, s, vh = np.linalg.svd(J, full_matrices=False)
        keep = s > thr * s[0]
        xn = x - vh[keep].T @ ((u[:, keep].T @ r) / s[keep])
        rn = resid(xn, 0.0, 0.0)[:-1]
        print(f"thr {thr:.0e} it {it}: |r|^2 {r @ r:.3e} -> {rn @ rn:.3e} (kept {keep.sum()}/{len(s)})")
        if rn @ rn < r @ r:
            x = xn
        else:
            break
np.save('rho3_point_gn.npy', x)
print(f"time {time.time()-t0:.1f}s")
