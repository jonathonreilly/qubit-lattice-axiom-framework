"""R4-5: everpresent-Lambda magnitudes per set, explicit factors.

Conventions (stated, not derived):
  unimodular term  S_L = -(Lambda/(8 pi G)) * V   (hbar = c = 1)
  => (V, Lambda/(8 pi G)) conjugate; heuristic  dLambda * dV ~ kappa_u * lbar_P^2 ,
     lbar_P^2 = 8 pi G hbar / c^3 ; kappa_u = 1 (ZAS/Sorkin heuristic) or 1/2 (minimal Gaussian).
  count-volume: N elements, density rho_e = l_e^-4 ; Var(N | region) = F * rho_e * V
     (F = 1 Poisson; F < 1 hyperuniform); dV = sqrt(Var N)/rho_e.
  => dLambda = kappa_u * lbar_P^2 * rho_e / sqrt(Var N)
            = kappa_u * (lbar_P/l_e)^2 / sqrt(F * V)     (volume-law case)
"""
import numpy as np
from scipy.integrate import quad

c = 2.99792458e8; G = 6.67430e-11; hbar = 1.054571817e-34
lP = np.sqrt(hbar*G/c**3); tP = lP/c
lbar = np.sqrt(8*np.pi)*lP
Mpc = 3.0856775814913673e22
H0 = 67.4e3/Mpc            # Planck 2018
OmL = 0.6847; Om = 0.3153; Orad = 9.2e-5
OmL = 1 - Om - Orad
Lam_obs = 3*OmL*H0**2/c**2
print("== constants")
print("l_P = %.4e m, lbar_P = %.4e m, t_P = %.4e s" % (lP, lbar, tP))
print("H0 = %.4e s^-1, c/H0 = %.4e m" % (H0, c/H0))
print("Lambda_obs = 3 Om_L H0^2/c^2 = %.4e m^-2 ; *l_P^2 = %.4e ; *lbar_P^2 = %.4e" % (Lam_obs, Lam_obs*lP**2, Lam_obs*lbar**2))

# --- FRW background
def Hz(a): return H0*np.sqrt(Orad/a**4 + Om/a**3 + OmL)
def t_of_a(a): return quad(lambda x: 1/(x*Hz(x)), 0, a, limit=400)[0]
t0 = t_of_a(1.0)
print("t0 = %.4e s = %.3f Gyr" % (t0, t0/3.15576e16))
# conformal time eta(a) = int da/(a^2 H)  (units s; comoving distance = c*eta)
def eta(a): return quad(lambda x: 1/(x*x*Hz(x)), 0, a, limit=400)[0]
eta0 = eta(1.0)
print("comoving particle horizon c*eta0 = %.4e m" % (c*eta0))
# 4-volume of past light cone of here-now:  V = int dt a^3 (4pi/3) (c (eta0-eta(t)))^3 * c
#  in terms of a: dt = da/(a H)
agrid = np.concatenate([np.logspace(-12, -4, 400, endpoint=False), np.linspace(1e-4, 1, 4000)])
etas = np.array([eta(a) for a in agrid[::20]])
from scipy.interpolate import interp1d
eta_i = interp1d(agrid[::20], etas, kind='cubic', fill_value='extrapolate')
def Vlc_integrand(a):
    return a**3*(4*np.pi/3)*(c*(eta0-eta_i(a)))**3*c/(a*Hz(a))
V_lc = quad(Vlc_integrand, 1e-12, 1.0, limit=800, points=[1e-4, 1e-2, 0.1])[0]
# "particle-horizon" variant quoted for ZAS Model 1: (4pi/3) int dt a^3 (c eta(t))^3 c
V_ph = quad(lambda a: a**3*(4*np.pi/3)*(c*eta_i(a))**3*c/(a*Hz(a)), 1e-12, 1.0, limit=800, points=[1e-4,1e-2,0.1])[0]
V_H = (c/H0)**4
V_t = (c*t0)**4
for name, V in [("V_lc (past light cone of here-now)", V_lc), ("V_ph (ZAS-quoted horizon form)", V_ph),
                ("V_H = (c/H0)^4", V_H), ("(c t0)^4", V_t)]:
    print("%-36s = %.4e m^4 = %.4e l_P^4 = %.4e lbar^4" % (name, V, V/lP**4, V/lbar**4))

print("\n== Sorkin magnitude with Planck-density Poisson count (F = 1)")
print("dLambda = kappa_u (lbar/l_e)^2 / sqrt(V)")
for le_name, le in [("l_e = lbar_P", lbar), ("l_e = l_P", lP)]:
    for ku in (1.0, 0.5):
        for name, V in [("V_lc", V_lc), ("V_H", V_H)]:
            dL = ku*(lbar/le)**2/np.sqrt(V)
            print("  %-12s kappa_u=%.1f %-5s : dLambda = %.3e m^-2 ; dLambda/Lambda_obs = %.3f" % (le_name, ku, name, dL, dL/Lam_obs))
beta_needed = Lam_obs*np.sqrt(V_lc)/1.0   # Lambda = beta / sqrt(V) in lbar=1 units: Lambda*lbar^2 = beta / sqrt(V/lbar^4)
beta_needed = Lam_obs*lbar**2*np.sqrt(V_lc/lbar**4)
print("beta needed so that Lambda_obs = beta/sqrt(V_lc) [8piG=hbar=c=1 units]: %.4f" % beta_needed)
print("  (ADGS/ZAS Model 1 viable range quoted 0.01 < beta < 0.02: that is an rms, the realized value today is one draw)")
print("  element spacing implied if kappa_u=1 and beta_rms=0.01-0.02: l_e = lbar/sqrt(beta) = %.1f-%.1f lbar_P = %.1f-%.1f l_P"
      % (1/np.sqrt(0.02), 1/np.sqrt(0.01), np.sqrt(8*np.pi)/np.sqrt(0.02), np.sqrt(8*np.pi)/np.sqrt(0.01)))
# epoch scaling check: Lambda_S(t) / H(t)^2 along history
print("\n== epoch scaling: Lambda_S = 1/sqrt(V_lc(t)) [lbar units] vs 3H^2/c^2")
for a in [1e-9, 1e-6, 1/1100., 0.1, 0.5, 1.0]:
    e0 = eta_i(a)
    Va = quad(lambda x: x**3*(4*np.pi/3)*(c*(e0-eta_i(x)))**3*c/(x*Hz(x)), 1e-12, a, limit=800)[0]
    LS = lbar**2/lbar**2/np.sqrt(Va)*1.0
    LS = 1.0/np.sqrt(Va/lbar**4)/lbar**2
    print("  a=%.3e: V_lc=%.3e m^4, Lambda_S=%.3e m^-2, Lambda_S/(3H^2/c^2)=%.4f" % (a, Va, LS, LS/(3*Hz(a)**2/c**2)))

print("\n== Set A: records only (rare flashes), forced identification V = N_rec / rho_rec")
nb = 0.2505  # cosmic mean baryon number density today, m^-3 (Omega_b h^2 = 0.0224)
ngam = 4.11e8; nnu = 3.36e8
P4 = lP**3*tP
cases = [("GRW lambda=1e-16/s, baryons", nb*1e-16),
         ("O4 Earth-heat max 5.3e-11/s per nucleon, baryons", nb*5.3e-11),
         ("IGM bound 1e-9/s, baryons", nb*1e-9),
         ("generous: every photon+nu+baryon at 1e-9/s", (nb+ngam+nnu)*1e-9)]
for name, rate in cases:
    rho_rec = rate/c  # events per m^4 (4-volume in m^4 = m^3 * c s)
    x = rho_rec*lP**4  # per Planck 4-volume
    fac = np.sqrt(rho_rec*lbar**4)  # dLambda/dLambda_S(l_e=lbar) = (lbar/l_e)^2 = sqrt(rho lbar^4)
    print("  %-50s rho_rec = %.3e /m^4 = %.3e per l_P^4 ; dLambda/Lambda_obs (kappa_u=1, V_lc) = %.3e"
          % (name, rho_rec, x, fac/np.sqrt(V_lc)/Lam_obs))

print("\n== Set C: Z^3 sites with ticks, one record per site, permanent")
# records in J^-(here-now) <= number of site worldlines meeting J^-(p) (comoving sites)
chi = c*eta0
for a0name, a0 in [("comoving spacing = l_P today", lP), ("comoving spacing = 1e-19 m today", 1e-19)]:
    Nsites = 4*np.pi/3*chi**3/a0**3
    N4 = V_lc/(lbar**4)
    fill = Nsites/(V_lc/lP**4)
    print("  %-34s N_sites(J^-) = %.3e ; V_lc/l_P^4 = %.3e ; max formation density = %.3e per l_P^4"
          % (a0name, Nsites, V_lc/lP**4, fill))
    # forced identification V = N_rec/rho_rec with rho_rec <= fill * l_P^-4
    fac = np.sqrt(fill*(lbar/lP)**4)
    print("     => dLambda/Lambda_obs <= %.3e (kappa_u=1)" % (fac/np.sqrt(V_lc/lbar**4)/(Lam_obs*lbar**2)))
print("  ratio t_P*H0 = %.3e ; sqrt = %.3e" % (tP*H0, np.sqrt(tP*H0)))

print("\n== lattice-site counts, using the MEASURED laws of r45_lattice_count/r45_checks2 (T <= 108 lattice units)")
print("   (A) aligned crystal (observer at rest, diamond): Var = F rho V, F = 0.60 (Z4), 7.76 (L7)  -> dLambda = Sorkin * F^-1/2")
for F in (0.60, 7.76):
    print("       F=%.2f: dLambda/dLambda_Sorkin = %.3f" % (F, F**-0.5))
print("   (B) LRL, Haar-ball-averaged: Var ~ c T^2.2, c T^2 with c ~ 0.5-0.9 (a=1, covolume sqrt7) at T<=108.")
print("       EXTRAPOLATION ONLY (TESTS.md:8: no verdict rests on it): if Var = 0.9 (T/a)^2 held at T = c t0, a = lbar:")
a = lbar; T = c*t0; rho = 1/(np.sqrt(7)*a**4)
dL = lbar**2*rho/np.sqrt(0.9*(T/a)**2)
print("       dLambda = %.3e m^-2 = %.3e Lambda_obs; epoch scaling dLambda ~ 1/T ~ H, not H^2" % (dL, dL/Lam_obs))
print("   (C) misaligned crystal: aligned time-row term suppressed by sinc^2(M d T/2), M = 2 pi/s, d = sinh(eta)")
d = 370e3/c
print("       Sun vs CMB d = %.2e; M d T/2 at T = c t0, s = lbar: %.3e  -> suppression ~ %.1e" % (d, 2*np.pi/lbar*d*c*t0/2, (2*np.pi/lbar*d*c*t0/2)**-2))
