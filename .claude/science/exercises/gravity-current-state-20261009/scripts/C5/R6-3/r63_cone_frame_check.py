"""R6-3: single-frame check of the past-cone Fourier/Parseval step: Var_u N(P_T) (Monte Carlo over torus shifts)
vs rho^2 sum_{G != 0} |P_T^(Lambda G)|^2 (truncated reciprocal sum), for a fixed frame (eta along x1)."""
import numpy as np, sys, time
sys.path.insert(0, '.')
from r63_formfactor import P_abs2
exec(open('r63_mc_cone.py').read().split('t0 = time.time()')[0])
rng = np.random.default_rng(9)
T, eta = 13.0, 0.4; nhat = np.array([1.0, 0, 0])
t0 = time.time()
Ns = np.array([count(T, eta, nhat, rng.random(4)) for _ in range(20000)])
v = Ns.var(ddof=1)
print("MC over 20000 shifts: Var_u = %.2f +- %.2f  (Var/T^3 = %.4f)" % (v, v*np.sqrt(2/19999), v/T**3))
rho = 1/np.sqrt(7)
for R in (20, 40, 60):
    r = np.arange(-R, R+1)
    tot = 0.0
    for m0 in range(-R*3, R*3+1):     # q0 = 2pi m0/sqrt7 ; allow larger m0 range so |q0| ~ |q|
        M1, M2, M3 = np.meshgrid(r, r, r, indexing='ij')
        q0 = 2*np.pi*m0/np.sqrt(7); q1 = 2*np.pi*M1; q2 = 2*np.pi*M2; q3 = 2*np.pi*M3
        sel = (q0**2 + q1**2 + q2**2 + q3**2) <= (2*np.pi*R)**2
        if m0 == 0: sel &= ~((M1 == 0) & (M2 == 0) & (M3 == 0))
        if not sel.any(): continue
        q0s, q1s = np.full(sel.sum(), q0), q1[sel]
        # cone frame components: boost by -eta along x1 (lattice -> cone frame); P^ depends on (w, |k|)
        w = np.cosh(eta)*q0s - np.sinh(eta)*q1s
        k1 = -np.sinh(eta)*q0s + np.cosh(eta)*q1s
        kk = np.sqrt(k1**2 + q2[sel]**2 + q3[sel]**2)
        w = np.where(np.abs(w) < 1e-9, 1e-9, w); kk = np.maximum(kk, 1e-9)
        tot += np.sum(T**8*P_abs2(T*w, T*kk))
    print("R=%d  rho^2 sum |P_T^(G)|^2 = %.2f  (Var/T^3 = %.4f)   [%.0f s]" % (R, rho**2*tot, rho**2*tot/T**3, time.time()-t0), flush=True)
