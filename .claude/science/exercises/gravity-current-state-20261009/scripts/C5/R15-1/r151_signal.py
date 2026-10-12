"""R15-1 (a): instantaneous response of the dust comoving density to a local impulse, R14-5 model, linear order.
Equations (R14-5 Sec. 4.5, re-derived in the report): sync-comoving dust gauge, CMC time T = t + xi,
  Dk xi = deltadot,  Dk = k^2/a^2 - 3 Hdot                         (CMC condition)
  deltaddot + 2H deltadot = (kappa/2) rho delta + (1/2)[(3 gdot + 2 g theta) xi + 3 g xidot] + F(x) delta_Dirac(t)
Jump across the impulse (proved in report): Delta deltadot_k = F_k * Dk/(Dk - 1.5 g) = F_k [1 + 1.5 g/(k^2/a^2 + Qbar)],
  Qbar = 1.5 kappa (rho+p)_nc  (uses Hdot = -(kappa(rho+p)_nc + g)/2).
Check 1: integrate the (delta, xi) system through a narrow Gaussian pulse for one k and compare with the jump formula.
Check 2: real-space response at distance r from a unit-monopole source: Delta deltadot(r) = 1.5 g exp(-sqrt(Qbar) a r)/(4 pi r) a^2 (r > 0),
  i.e. nonzero at every r at the instant of the impulse (outside the light cone). GR (g = 0): exactly zero for r > source size.
"""
import numpy as np
from scipy.integrate import solve_ivp
a, H, rho_p = 1.0, 1.0, 1.0           # units H = 1; kappa (rho+p)_nc = 1
for g in [-50.0, -1.0, 2e-6, 1.0]:
    Qbar = 1.5*rho_p
    Hdot = -(rho_p + g)/2
    for k in [0.3, 1.0, 5.0]:
        Dk = k**2/a**2 - 3*Hdot
        s = 1e-4
        F = lambda t: np.exp(-t**2/(2*s**2))/np.sqrt(2*np.pi)/s
        # frozen background (gdot = 0, H, rho const over the pulse); state y = [delta, deltadot]; xi = deltadot/Dk, xidot = deltaddot/Dk
        def rhs(t, y):
            d, dd = y
            xi = dd/Dk
            # deltaddot (1 - 1.5 g/Dk) = -2H dd + 0.5*rho*d + 0.5*(2 g 3H) xi + F
            ddd = (-2*H*dd + 0.5*1.0*d + 0.5*(2*g*3*H)*xi + F(t))/(1 - 1.5*g/Dk)
            return [dd, ddd]
        sol = solve_ivp(rhs, (-10*s, 10*s), [0.0, 0.0], rtol=1e-11, atol=1e-14, max_step=s/20)
        jump = sol.y[1, -1]
        pred = Dk/(Dk - 1.5*g)
        print(f"g/H^2 = {g:+.1e}, k = {k}: numerical jump = {jump:.8f}, formula 1 + 1.5g/(k^2+Qbar) = {1 + 1.5*g/(k**2 + Qbar):.8f}, Dk/(Dk-1.5g) = {pred:.8f}")
print("\nReal-space instantaneous response to a unit monopole impulse (units c = H = 1, Qbar = 1.35 H0^2 today):")
for g_over_H2, label in [(3e-6, "today, backreaction-sized g (suggested magnitude)"), (1.0, "transition, g ~ H^2"), (100.0, "transition with reader excursion (R14-5 runs reach |g| ~ 1e2-1e3 H^2)")]:
    Qb = 1.35
    vals = [1.5*g_over_H2*np.exp(-np.sqrt(Qb)*r)/(4*np.pi*r) for r in (0.01, 0.1, 0.5, 1.0)]
    print(f"  g/H^2 = {g_over_H2:g} ({label}): Delta deltadot at r = 0.01, 0.1, 0.5, 1 c/H: " + ", ".join(f"{v:.2e}" for v in vals))
