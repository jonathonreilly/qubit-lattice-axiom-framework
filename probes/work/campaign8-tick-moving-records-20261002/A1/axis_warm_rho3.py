"""rho=3, branch m=1 (axis integrality imposed), warm start from the
quasi-local near-solution; reports the residual reached in limited time."""
import sys, time
import numpy as np
from scipy.optimize import least_squares
sys.argv = ['axis_branch_search.py', '3', '0', '31']
src = open("axis_branch_search.py").read().rsplit("t0 = time.time()", 1)[0]
exec(src)
x = np.load('rho3_point.npy')
c = unpack(x)
# normalise global phase so that W(0) = 1
W0 = np.einsum('i,itab->tab', c, axis_cols)[0][0, 0]
c = c / W0
x = np.concatenate([c.real, c.imag])
print(f"start: unitarity |r|^2 = {np.sum(resid(x,0.0,0.0)[:-1]**2):.3e}, with axis(m=1) total = {np.sum(resid2(x,1)**2):.3e}")
t0 = time.time()
sol = least_squares(resid2, x, jac=jac2, args=(1,), method='lm', xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=200)
print(f"after LM ({sol.nfev} nfev, {time.time()-t0:.0f}s): total residual^2 = {np.sum(sol.fun**2):.3e}; unitarity part = {np.sum(resid(sol.x,0.0,0.0)[:-1]**2):.3e}")
