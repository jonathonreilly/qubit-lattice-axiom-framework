"""Warm-start the rho=3 covariant search from the rho=2 near-miss (free tau),
plus random starts while time remains (< 50 s total)."""
import sys
import time
import numpy as np
from scipy.optimize import least_squares

# rho=2 point -> orbit matrices
sys.argv = ['covariant_walk_search.py', '2', '0', '11']
ns2 = {}
exec(open('covariant_walk_search.py').read().split("t0 = time.time()")[0], ns2)
x2 = np.load('gn_point.npy')
c2 = ns2['unpack'](x2)
A0 = {}
off = 0
for v0, orb, inv in ns2['orbits']:
    A0[v0] = sum(c2[off + j] * B for j, B in enumerate(inv))
    off += len(inv)

sys.argv = ['covariant_walk_search.py', '3', '0', '12']
ns3 = {}
exec(open('covariant_walk_search.py').read().split("t0 = time.time()")[0], ns3)
t0 = time.time()
c3 = []
for v0, orb, inv in ns3['orbits']:
    if v0 in A0:
        Mb = np.array([B.reshape(-1) for B in inv]).T
        coef, *_ = np.linalg.lstsq(Mb, A0[v0].reshape(-1), rcond=None)
        c3.extend(coef)
    else:
        c3.extend([0.0] * len(inv))
c3 = np.array(c3, complex)
x3 = np.concatenate([c3.real, c3.imag])
resid, jac, unpack, gram, mov = ns3['resid'], ns3['jac'], ns3['unpack'], ns3['gram'], ns3['mov']
print(f"embedded rho=2 point: |r|^2 = {np.sum(resid(x3, 0.0, 0.0)[:-1]**2):.3e}")
sol = least_squares(resid, x3, jac=jac, args=(0.0, 0.0), method='lm', xtol=1e-15,
                    ftol=1e-15, gtol=1e-15, max_nfev=150)
c = unpack(sol.x)
wmov = np.real(c.conj() @ (gram * np.outer(mov, mov)) @ c)
print(f"rho=3 warm LM: |r|^2 = {np.sum(sol.fun[:-1]**2):.3e}, moving weight {wmov:.4f}, nfev {sol.nfev}, t={time.time()-t0:.1f}s")
np.save('rho3_warm.npy', sol.x)
