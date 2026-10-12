"""R14-5 (c): linear dust growth in the zero-mode-lapse (CMC) model, synchronous-comoving gauge.
Derivation (report Sec. 4c): E-fluid rho_E = lam(t) on CMC slices, p_E = g/N - lam; CMC time T = t + xi,
   xi = deltadot / (k^2/a^2 - 3 Hdot)                (CMC condition, delta theta_T = 0)
   delta rho_E(sync) = -g theta xi ;  delta p_E(sync) = (gdot + g theta) xi + g xidot
   deltaddot + 2 H deltadot = (kappa/2) rho_m delta + (1/2)[(3 gdot + 2 g theta) xi + 3 g xidot]
Background with curvature-like memory X (optional F-law memory): H^2 = Om a^-3 + OX a^-2, g = 2X, X ~ a^-2.
g = 0 (OX = 0, exact reader, no transition) => equation is GR's exactly (Lt = 0).
Comparator 'GRsameH': same H(a), xi-terms dropped (GR open-FRW sub-horizon form).
Units H0 = c = 1; k in H0/c. Initial growing mode delta ~ a at a = 1e-3.
"""
import numpy as np
from scipy.integrate import solve_ivp
def growth(OX, k, xi_terms=True):
    Om = 1 - OX
    def rhs(N, y):
        a = np.exp(N); d, dp = y
        H = np.sqrt(Om*a**-3 + OX*a**-2)
        Hd = -1.5*Om*a**-3 - OX*a**-2                 # dH/dt
        Hdd = H*(4.5*Om*a**-3 + 2*OX*a**-2)            # d2H/dt2
        X = OX*a**-2; g = 2*X; gd = -2*H*g; th = 3*H
        S = 1.5*Om*a**-3
        ddot_d = H*dp                                  # deltadot
        if xi_terms and g != 0:
            Dk = k**2/a**2 - 3*Hd; Dkd = -2*H*k**2/a**2 - 3*Hdd
            c = 1.5*g/Dk; B = (3*gd + 2*g*th)/(2*Dk)
            dd = (-2*H*ddot_d + S*d + B*ddot_d - c*ddot_d*Dkd/Dk)/(1 - c)
        else:
            dd = -2*H*ddot_d + S*d
        # deltaddot = H^2 d'' + H Hdot/H d'... in N: deltaddot = H^2 d'' + Hd d'
        dpp = (dd - Hd*dp)/H**2
        return [dp, dpp]
    a0 = 1e-3
    sol = solve_ivp(rhs, (np.log(a0), 0.0), [a0, a0], rtol=1e-10, atol=1e-14, method='DOP853')
    return sol.y[0, -1]
print("g = 0 (OX = 0): model == GR exactly; D(1) =", growth(0.0, 10.0), "(EdS expectation ~ 1 - small init transient)")
for OX in [3e-3, 0.3]:
    print(f"OX = {OX}  (g = 2X):")
    Dref = growth(OX, 1.0, xi_terms=False)
    for k in [0.3, 1.0, 3.0, 10.0, 100.0]:
        Dk = growth(OX, k)
        print(f"   k = {k:6.1f} H0/c: D(1) = {Dk:.8f}; GRsameH = {Dref:.8f}; rel diff = {(Dk/Dref - 1):+.3e};  OX*(H0/k)^2 = {OX/k**2:.1e}")
    print(f"   GRsameH vs flat-EdS D(1)=0.99910...: rel = {Dref/growth(0.0, 10.0) - 1:+.3e}  (background effect of the w=-1/3 memory fluid)")
