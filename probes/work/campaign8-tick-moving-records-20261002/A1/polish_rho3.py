"""Continue LM / Gauss-Newton on the rho=3 near-solution and verify off-grid."""
import sys
import time
import numpy as np
from scipy.optimize import least_squares

sys.argv = ['covariant_walk_search.py', '3', '0', '12']
exec(open('covariant_walk_search.py').read().split("t0 = time.time()")[0])
t0 = time.time()
x = np.load('rho3_warm.npy')
for it in range(4):
    sol = least_squares(resid, x, jac=jac, args=(0.0, 0.0), method='lm', xtol=3e-16,
                        ftol=3e-16, gtol=3e-16, max_nfev=60)
    x = sol.x
    J = jac(x, 0.0, 0.0)[:-1]
    s = np.linalg.svd(J, compute_uv=False)
    print(f"LM pass {it}: |r|^2 = {np.sum(sol.fun[:-1]**2):.3e}, nfev {sol.nfev}, status {sol.status}, sv max {s[0]:.2e} min {s[-1]:.1e}, #sv<1e-6: {np.sum(s<1e-6)} t={time.time()-t0:.1f}s")
    if time.time() - t0 > 40:
        break
np.save('rho3_point.npy', x)
c = unpack(x)
wmov = np.real(c.conj() @ (gram * np.outer(mov, mov)) @ c)
print(f"moving weight {wmov:.6f}")
# off-grid unitarity check
rng2 = np.random.default_rng(99)
ks = rng2.uniform(-np.pi, np.pi, (300, 3))
Amats = []
off = 0
for v0, orb, inv in orbits:
    Av0 = sum(c[off + j] * B for j, B in enumerate(inv))
    off += len(inv)
    for w, U in orb.items():
        Amats.append((np.array(w), U @ Av0 @ U.conj().T))
vecs = np.array([a[0] for a in Amats])
mats = np.array([a[1] for a in Amats])
E = np.exp(-1j * ks @ vecs.T)
Wk = np.einsum('kv,vab->kab', E, mats)
dev = np.max(np.linalg.norm(np.einsum('kba,kbc->kac', Wk.conj(), Wk) - I2[None], axis=(1, 2)))
print(f"max ||W^dag W - 1|| on 300 random off-grid k: {dev:.3e}")
np.save('rho3_Amats.npy', mats)
np.save('rho3_vecs.npy', vecs)
