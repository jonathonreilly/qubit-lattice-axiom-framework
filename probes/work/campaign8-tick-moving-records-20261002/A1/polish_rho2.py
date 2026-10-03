"""Polish the best rho=2 near-solutions and inspect their structure."""
import sys
import numpy as np
from scipy.optimize import least_squares

sys.argv = ['covariant_walk_search.py', '2', '0', '2']
exec(open('covariant_walk_search.py').read().split("t0 = time.time()")[0])

data = np.load('best_rho2_seed2.npy')
for row in data:
    tau, x = row[0], row[1:]
    print(f"--- tau = {tau}: start residual^2 = {np.sum(resid(x, tau)**2):.3e}")
    for it in range(6):
        sol = least_squares(resid, x, jac=jac, args=(tau,), method='lm', xtol=1e-15,
                            ftol=1e-15, gtol=1e-15, max_nfev=20000)
        x = sol.x
        print(f"   pass {it}: residual^2 = {np.sum(sol.fun**2):.3e}")
    c = unpack(x)
    # weight per orbit
    off = 0
    for v0, orb, inv in orbits:
        cc = c[off:off + len(inv)]
        wt = np.real(cc.conj() @ gram[off:off + len(inv), off:off + len(inv)] @ cc)
        off += len(inv)
        if wt > 1e-6:
            print(f"   orbit {v0}: weight {wt:.4f}")
    # unitarity defect on a fine random k sample (independent of the grid)
    rng2 = np.random.default_rng(5)
    ks = rng2.uniform(-np.pi, np.pi, (400, 3))
    def Wk(k):
        M = np.zeros((2, 2), complex)
        off = 0
        for v0, orb, inv in orbits:
            for j, B in enumerate(inv):
                for w, U in orb.items():
                    M += c[off + j] * np.exp(-1j * np.dot(k, w)) * (U @ B @ U.conj().T)
            off += len(inv)
        return M
    dmax = max(np.linalg.norm(Wk(k).conj().T @ Wk(k) - I2) for k in ks)
    print(f"   max ||W^dag W - 1|| on 400 random k: {dmax:.3e}")
    np.save(f"polished_tau{tau}.npy", x)
