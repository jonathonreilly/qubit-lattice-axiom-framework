"""R16-6 (c): DESI-like CPL dark energy + matter + radiation, homogeneous, kappa = 1, u = ln a, a = 1 today.
(w0, wa) = (-0.75, -0.86) (the values R15-6 used; DESI DR2-like, RECALLED).  Omega_m = 0.31, Omega_r = 9e-5.
Plus any constant true vacuum V_t (never enters an h-only reader).
Readers: IE (EoS-initialized at a = 1e-4, then R' = -3h) and LIN (two-register linear, G(0)=0, G(3)=G(4)=1;
my design, R15-4 class).  Report g/H^2 = (-3h - R')/R and Lam_late = R/rho_nc - 1 over 0.1 < a < 1.
"""
import numpy as np
from scipy.integrate import solve_ivp
w0, wa, Om, Or = -0.75, -0.86, 0.31, 9e-5
Ode = 1 - Om - Or
rho_de = lambda a: Ode*a**(-3*(1+w0+wa))*np.exp(-3*wa*(1-a))
w = lambda a: w0 + wa*(1-a)
rho_nc = lambda a: Om*a**-3 + Or*a**-4 + rho_de(a)
h_of = lambda a: Om*a**-3 + 4/3*Or*a**-4 + (1+w(a))*rho_de(a)
beta = np.array([5.0, 10.0]); kk = np.array([-1/3, 3.5])
u0, u1 = np.log(1e-4), 0.0
def rhs(u, y):
    a = np.exp(u); h = h_of(a)
    return [-3*h] + list(3*h - beta*y[1:3])
# LIN registers start at the radiation-era steady state y_j = E/(beta_j - x) with x = 4 (exact on radiation)
a0 = np.exp(u0); x = 4.0
E0 = 3*h_of(a0)
y0 = [rho_nc(a0)] + list(E0/(beta - x))
us = np.linspace(u0, u1, 20001)
s = solve_ivp(rhs, (u0, u1), y0, t_eval=us, rtol=1e-12, atol=1e-30, method='DOP853')
a = np.exp(us); h = h_of(a); rn = rho_nc(a)
R_IE = s.y[0]; R_LIN = kk[0]*s.y[1] + kk[1]*s.y[2]
sel = a > 0.1
for name, R in [('IE', R_IE), ('LIN', R_LIN)]:
    dR = np.gradient(R, us) if name == 'LIN' else -3*h
    gH2 = (-3*h - dR)/R
    Lam = R/rn - 1
    print("%-3s 0.1<a<1: g/H^2 in [%+.3e, %+.3e], today %+.3e | Lam_late=R/rho_nc-1 in [%+.3e, %+.3e], today %+.3e"
          % (name, gH2[sel].min(), gH2[sel].max(), gH2[-1], Lam[sel].min(), Lam[sel].max(), Lam[-1]))
print("w(a) crosses -1 at a = %.3f (z = %.3f); IE is not in R15-4's class R+ (integrator kernel, start-dependent)." % ((1+w0+wa)/wa, wa/(1+w0+wa)-1))
