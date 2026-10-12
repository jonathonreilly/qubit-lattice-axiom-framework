"""Convention checks: (1) O(e) Ward identity sum_i s_i(Q) V^i(Q) = c*(h(kout) D - D h(kin)); (2) seagull Ward identity
sum_i s_i(p) eps'_i SG^i(p,p') vs commutator of the O(e) emission vertex with the density.  Prints the fitted constants and residuals."""
import numpy as np
from s2_core import *
rng = np.random.default_rng(1)
for d in (2, 3):
    S = Stag(d, 0.37)
    for t in range(3):
        k = wrapr(rng.uniform(-2, 2, d)); Q = wrapf(rng.uniform(-3, 3, d)); ko = wrapr(k + Q)
        s = 2*np.sin(Q/2)
        L = sum(s[i]*S.vert(k, Q, ko, i) for i in range(d))
        R = S.h(ko) @ S.dens(k, Q, ko) - S.dens(k, Q, ko) @ S.h(k)
        c = np.vdot(R.ravel(), L.ravel())/np.vdot(R.ravel(), R.ravel())
        print(f"d={d} O(e) Ward: L = c*[h,rho], c={c:.6f}, residual {np.linalg.norm(L - c*R):.2e}")
    # seagull: gauge variation of the photon field by grad chi (momentum p): delta(O(e) emission vertex for p') = O(e^2) seagull
    for t in range(3):
        k = wrapr(rng.uniform(-2, 2, d)); p = wrapf(rng.uniform(-3, 3, d)); pp = wrapf(rng.uniform(-3, 3, d))
        ep = rng.normal(size=d)
        ko = wrapr(k + p - pp)
        s = 2*np.sin(p/2)
        # LHS: seagull with absorbed field longitudinal (eps=s), emitted eps'
        L = -sum(s[i]*ep[i]*S.seag(k, p - pp, ko, i) for i in range(d))
        # RHS: commutator of density(p) with emission vertex (absorb -pp) : both orderings
        km1 = wrapr(k - pp); kp1 = wrapr(k + p)
        Ve1 = sum(ep[i]*S.vert(k, -pp, km1, i) for i in range(d)); D1 = S.dens(km1, p, ko)
        D2 = S.dens(k, p, kp1); Ve2 = sum(ep[i]*S.vert(kp1, -pp, ko, i) for i in range(d))
        R = D1 @ Ve1 - Ve2 @ D2
        c = np.vdot(R.ravel(), L.ravel())/np.vdot(R.ravel(), R.ravel())
        print(f"d={d} seagull Ward: L = c*[rho,V], c={c:.6f}, residual {np.linalg.norm(L - c*R):.2e}")
