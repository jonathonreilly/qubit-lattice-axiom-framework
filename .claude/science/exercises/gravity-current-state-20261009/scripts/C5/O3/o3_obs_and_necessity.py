# O3 part 1: observational numbers and the "no tuning => exact pairing" necessity, illustrated
# with P1's exact free-species function F(M) (RN-L1 normalization, mu_E per site, lattice units).
import numpy as np
from numpy.polynomial.legendre import leggauss

# ---------- observational numbers ----------
hbar_c_GeV_m = 1.973269804e-16
H0 = 67.4  # km/s/Mpc
Mpc = 3.0856775814913673e22
H0_s = H0*1e3/Mpc
G = 6.67430e-11; c = 2.99792458e8; hbar = 1.054571817e-34
OmL = 0.685
rho_crit = 3*H0_s**2/(8*np.pi*G)          # kg/m^3
rho_L = OmL*rho_crit*c**2                  # J/m^3
# convert to GeV^4: J/m^3 -> GeV/m^3 -> * (hbar c)^3
GeV = 1.602176634e-10
rho_L_GeV4 = rho_L/GeV * hbar_c_GeV_m**3
MPl = 1.220890e19; MPl_red = 2.435323e18
print("rho_Lambda = %.3e GeV^4 = (%.3f meV)^4" % (rho_L_GeV4, rho_L_GeV4**0.25*1e12))
print("rho_Lambda / M_Pl^4      = %.3e" % (rho_L_GeV4/MPl**4))
print("rho_Lambda / Mbar_Pl^4   = %.3e" % (rho_L_GeV4/MPl_red**4))

# ---------- F(M) by Gauss-Legendre on the cube (integrand even in each k) ----------
n = 56
x, w = leggauss(n)
k = 0.5*np.pi*(x+1); wk = 0.5*np.pi*w/np.pi   # average over [0,pi] = average over BZ
cx = np.cos(k)
CX, CY, CZ = np.meshgrid(cx, cx, cx, indexing='ij')
W3 = wk[:,None,None]*wk[None,:,None]*wk[None,None,:]
S = (2-2*CX)+(2-2*CY)+(2-2*CZ)
num = (CX-CY)**2*(CX+CY)
def F(M):
    return 0.125*np.sum(W3*num/np.sqrt(M*M+S))
def Erho(M):  # vacuum energy per site of one real KG component, 1/2<omega>
    return 0.5*np.sum(W3*np.sqrt(M*M+S))
print("check F(1) = %.12e (V3 referee 1.970388642e-3)" % F(1.0))
print("check F(0.5) = %.12e" % F(0.5))
print("rho_vac per site of one KG component (M=0): 1/2<omega> = %.6f (lattice units)" % Erho(0.0))

# ---------- the necessity statement: a non-paired spectrum tuned to cancel at one mass drifts ----------
# species: 1 KG of mass c_b*t (weight +F), 2 staggered fields of mass c_f*t (weight -1/2 F(2 c_f t) each)
# exact pairing: c_b = 2 c_f.  Tuned alternative: 1 KG at c_b t  vs  2 staggered at different mass,
# with an extra KG at mass c_x t chosen so that the total cancels at t0 (R0 holds by count: 1+... no):
# simplest: R0-balanced non-paired content {KG(a t)} vs {2 stag(b t)}, b tuned so mu(t0)=0.
from scipy.optimize import brentq
def mu_content(t, cb, cf):
    return F(cb*t) - F(2*cf*t)   # 2 staggered fields: 2 * (-1/2) F(2 cf t)
t0 = 0.3
# tuned: KG mass a*t with a=1; staggered mass chosen to cancel at t0 -> forces 2 cf = cb (unique since F monotone)
print("\nF monotone on (0,3)? ", np.all(np.diff([F(m) for m in np.linspace(0.01,3,40)])<0))
# A genuinely non-paired tuned content needs >= 2 bosonic masses: KG(a1 t) + KG(a2 t) vs 4 stag(b t), choose a2 to cancel at t0
a1, b = 0.5, 0.4
def mu_np(t, a2): return F(a1*t)+F(a2*t) - 2*F(2*b*t)
a2 = brentq(lambda a: mu_np(t0, a), 0.81, 20.0) if mu_np(t0,0.81)*mu_np(t0,20.0)<0 else None
print("tuned non-paired content: KG(%.2f t)+KG(a2 t) vs 4 staggered(%.2f t); a2 = %s" % (a1, b, a2))
if a2 is not None:
    for t in [0.1, 0.2, 0.3, 0.4, 0.6, 1.0]:
        print("  t=%.2f  mu_E(non-paired) = %+.4e   mu_E(paired: 2 KG(2bt) vs 4 stag(bt)) = %+.1e" % (t, mu_np(t,a2), 2*F(2*b*t)-2*F(2*b*t)))
# moment proof illustration: the t^6 ln t coefficient sum_s w_s c_s^6 must vanish, etc. (proved in report)
