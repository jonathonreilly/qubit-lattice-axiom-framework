#!/usr/bin/env python3
"""Independent freeze-out re-check (own code): log-Y ODE with LSODA, Yeq from scipy.special.kv (not kve).
Claude Sonnet 5.5 (same family as attacker)."""
import math, numpy as np
from scipy.integrate import solve_ivp
from scipy.special import kv
import mpmath as mp
mp.mp.dps = 20

MPL, GS = 1.2209e19, 106.75
LAM = math.sqrt(math.pi/45)*math.sqrt(GS)*MPL     # dY/dx = -(LAM m <sv> / x^2)(Y^2-Yeq^2)

def yeq(x, g):
    return 45/(4*math.pi**4)*g/GS*x*x*kv(2, x)

def omega(m, sv_of_x, g, dirac, x0=5.0, x1=1500.0):
    # own solver: Y directly, Radau, tight tolerances (different from attacker's: kv not kve, own lambda)
    def rhs(x, y):
        Y = y[0]; Ye = yeq(x, g)
        return [-(LAM*m*sv_of_x(x)/x**2)*(Y*Y - Ye*Ye)]
    sol = solve_ivp(rhs, [x0, x1], [yeq(x0, g)], method='Radau', rtol=1e-10, atol=1e-32)
    Yinf = sol.y[0][-1]
    return 2.742e8*m*Yinf*(2 if dirac else 1)

def avgS(c, a, attractive):     # <S> with S argument 2 pi * c / v, c = alpha_eff, weight v^2 exp(-a v^2), a = x/4
    sgn = 1 if attractive else -1
    def S(z):
        z = sgn*z
        return mp.mpf(1) if abs(z) < 1e-30 else z/(1-mp.e**(-z))
    num = mp.quad(lambda v: S(2*mp.pi*c/v)*v*v*mp.e**(-a*v*v), [0, 1, 5, mp.inf])
    den = mp.quad(lambda v: v*v*mp.e**(-a*v*v), [0, 1, 5, mp.inf])
    return float(num/den)

m = 3940.53
a_lm = 0.09067
a_s_m = 0.07851
print("lane formula (kappa=1, alpha_LM, S=1, self-conj g=2):       Omega h^2 =", round(omega(m, lambda x: math.pi*a_lm**2/m**2, 2, False), 4))
print("dark U(1) Dirac, alpha_LM, S=1:                              Omega h^2 =", round(omega(m, lambda x: math.pi*a_lm**2/m**2, 2, True), 4))
# C1 no Sommerfeld
sv0 = (43/27)*math.pi*a_s_m**2/m**2
print("coloured Dirac triplet, alpha_s(m)=0.0785, no S, g=6 Dirac: Omega h^2 =", round(omega(m, lambda x: sv0, 6, True), 4), " (attack: 0.2230)")
# C1 with Sommerfeld (2pi kernel): tabulate S1,S8 on an x grid
xs = np.geomspace(4, 2000, 45)
S1 = np.array([avgS(4/3*a_s_m, x/4, True) for x in xs]); S8 = np.array([avgS(a_s_m/6, x/4, False) for x in xs])
lS1 = lambda x: float(np.interp(math.log(x), np.log(xs), S1)); lS8 = lambda x: float(np.interp(math.log(x), np.log(xs), S8))
sv1 = lambda x: math.pi*a_s_m**2/m**2*((2/27)*lS1(x) + (5/27 + 12/9)*lS8(x))
print("coloured Dirac triplet with colour-resolved Sommerfeld:      Omega h^2 =", round(omega(m, sv1, 6, True), 4), " (attack: 0.2348)")
print("   same, self-conj counting (not available to a complex rep): Omega h^2 =", round(omega(m, sv1, 6, False), 4), " (attack: 0.1174)")
# Colourless SU(2) doublet (the f_dark = C2(2)*3 reading of R_BASE): pure-Higgsino thermal mass is ~1.1 TeV (literature);
# Omega ~ m^2 at fixed coupling => Omega(3.94 TeV) ~ 0.12*(3.94/1.1)^2
print("colourless SU(2)-doublet (Higgsino-like), scaling estimate Omega(3.94 TeV) ~", round(0.12*(3.9405/1.1)**2,2), "(suggested, not solved)")
