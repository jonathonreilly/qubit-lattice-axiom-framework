"""E1 translation of the measured noise laws into observational bounds on l_k.

Measured/derived (rho_k = l_k^-4, eps = (l/l_k)^4, rho = l^-4; b = B/P, P=(4/sqrt6)/l_k^2):
  element variance  Var b1 = kappa * eps * S(tau),  S(tau) -> 1.674 (tau/l_k)^2,  kappa ~ 3
  white strength of delta m^2 :  Q = P^2 Var(b)/rho = (8/3)*1.674*kappa * eps^2 (tau/l_k)^2
  instability (renewal, CHECKED at eps=.05-.2): gamma_rms = 0.5*sqrt(3.35*kappa*eps)/l_k
Criteria (each ARGUED; see report):
  C1 coarse-grained GW phase noise      : <dPhi^2> ~ Q/(16 pi^2) < 0.01
  C2 incoherent loss, elastic-only kin. : Q*w*D/(16 pi^2) < 1
  C3 incoherent loss, E_max = 1/l_k     : Q*D/(16 pi^2 w l_k^2) < 1
  C4 realization stability (all fields) : gamma_rms * L_prop < 1
  C4' isolated GW wavetrain (support du): gamma_GW = 1.674 kappa eps du / l_k^2 ; gamma_GW*D < 1
  SW1 CMB photon swerve, lenient (E_max=E0): k1 = Q E0^2/(64 pi^2) < 1.04e-40 eV^2
  SW2 CMB photon swerve, E_max = 1/l_k     : k1 = Q E_max^4/(64 pi^2 E0^2)
  SW3 relic nu (m=0.05 eV) lenient          : k = Q m^3/(480 pi^2) < 1e-34 eV^3
"""
import numpy as np
from scipy.optimize import brentq

hbarc = 1.97327e-7           # eV m
lP = 1.616e-35               # m (discreteness scale l = l_P; scale_reference_primitive)
L_H = 1.31e26                # m, c * 13.8 Gyr (IR extent of the past)
D = 3.086e25                 # m, 1 Gpc
f = 100.0; w = 2*np.pi*f/2.998e8   # GW wavenumber, m^-1
du = 3.0e7                   # m, GW wavetrain length (~0.1 s)
E0_cmb = 6.3e-4/hbarc        # m^-1 (2.7 T)
k1_bound = 7e-97 * (1.2209e28)**2   # eV^2  (Philpott-Dowker-Sorkin 2009, Planck units -> eV^2)
k_nu_bound = 1e-61 * 1e27    # eV^3  (Kaloper-Mattingly 2006: 1e-61 GeV^3)
m_nu = 0.05/hbarc            # m^-1
kappa = 3.0
BAR = 1e-19


def eps(lk, l=lP): return (l/lk)**4
def Q(lk, L, l=lP): return (8/3)*1.674*kappa*eps(lk, l)**2*(L/lk)**2


crit = {
 "C1 coarse phase noise (L=L_H)":      lambda lk: Q(lk, L_H)/(16*np.pi**2)/0.01,
 "C1 coarse phase noise (L^2=du*D)":   lambda lk: Q(lk, np.sqrt(du*D))/(16*np.pi**2)/0.01,
 "C2 elastic-only loss (L=L_H)":       lambda lk: Q(lk, L_H)*w*D/(16*np.pi**2),
 "C3 loss, E_max=1/l_k (L^2=du*D)":    lambda lk: Q(lk, np.sqrt(du*D))*D/(16*np.pi**2*w*lk**2),
 "C3 loss, E_max=1/l_k (L=L_H)":       lambda lk: Q(lk, L_H)*D/(16*np.pi**2*w*lk**2),
 "C4 stability, all fields, over D":   lambda lk: 0.5*np.sqrt(3.35*kappa*eps(lk))/lk*D,
 "C4 stability, all fields, over ct0": lambda lk: 0.5*np.sqrt(3.35*kappa*eps(lk))/lk*L_H,
 "C4' isolated GW over D (ARGUED)":    lambda lk: 1.674*kappa*eps(lk)*du/lk**2*D,
 "SW1 CMB swerve, lenient":            lambda lk: Q(lk, L_H)*(E0_cmb*hbarc)**2/(64*np.pi**2)/k1_bound,
 "SW2 CMB swerve, E_max=1/l_k":        lambda lk: Q(lk, L_H)*(hbarc/lk)**4/(64*np.pi**2*(E0_cmb*hbarc)**2)/k1_bound,
 "SW3 relic nu swerve, lenient":       lambda lk: Q(lk, L_H)*(m_nu*hbarc)**3/(480*np.pi**2)/k_nu_bound,
}
print(f"inputs: l={lP:.3e} m, L_H={L_H:.2e} m, D={D:.3e} m, GW k={w:.2e} 1/m, du={du:.0e} m,"
      f" k1_bound={k1_bound:.2e} eV^2, k_nu_bound={k_nu_bound:.1e} eV^3, kappa={kappa}")
print(f"at l_k = 1e-19 m: eps = {eps(1e-19):.2e}, A^2(L_H) = {1.674*eps(1e-19)*(L_H/1e-19)**2:.2e},"
      f" Q(L_H) = {Q(1e-19, L_H):.2e}, 1/gamma_rms = {1/(0.5*np.sqrt(3.35*kappa*eps(1e-19))/1e-19):.2e} m")
print(f"{'criterion':40s} {'value at 1e-19 m':>18s} {'required l_k (m)':>18s}  vs bar 1e-19")
for name, fn in crit.items():
    v = fn(BAR)
    # every criterion decreases monotonically with l_k: solve fn(lk)=1
    lk_req = np.exp(brentq(lambda x: np.log(fn(np.exp(x))), np.log(1e-35), np.log(1e-3)))
    print(f"{name:40s} {v:18.2e} {lk_req:18.2e}  {'PASS' if lk_req <= BAR else 'FAIL'}")
# sensitivity of the stability bound to the discreteness scale and kappa
for l in [lP, 8.1e-35]:
    for kap in [2.6, 3.0, 4.0]:
        lk = (0.5*np.sqrt(3.35*kap)*l**2*L_H)**(1/3)
        print(f"   stability over ct0: l={l:.2e} kappa={kap}: l_k >= {lk:.2e} m")
# Sorkin 2007 element-wise estimate for comparison: lambda0^3 >> l^2 R
print(f"   Sorkin 2007 (l^2 R)^(1/3) with R = L_H: {(lP**2*L_H)**(1/3):.2e} m")
# TT analogue of everpresent Lambda (crude, ARGUED): m_g^2/H^2 ~ 1.3 (l/l_k)^6 (L_H/l_k)
H = hbarc/L_H
for lk in [lP, 1e-30, 1e-25, 1e-19]:
    r = 1.3*(lP/lk)**6*(L_H/lk)
    print(f"   TT 'everpresent' estimate l_k={lk:.0e}: m_g ~ {np.sqrt(r)*H:.2e} eV (H={H:.2e} eV; GWTC-3 1.27e-23 eV)")
