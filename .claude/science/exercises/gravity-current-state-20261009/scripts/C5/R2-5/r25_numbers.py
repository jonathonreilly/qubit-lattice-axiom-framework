"""R2-5 check 5: numbers for (c) induced Lorentz violation and the arrow's law-level parameters.
Inputs (standard constants; cosmology Planck-2018-like): hbar c = 197.327 MeV fm, t_P = 5.391e-44 s,
l_P = 1.616e-35 m, M_Pl = 1.2209e19 GeV (reduced 2.435e18 GeV), age 13.79 Gyr, H0 = 67.7 km/s/Mpc,
CMB T0 = 2.7255 K, m_e = 0.51100 MeV, alpha = 1/137.036.  F1 bounds from TESTS.md / C5_O1 (refereed
numbers): c_gamma - c_e < 2.66e-19; p-gamma 6e-20 (indicative); GW170817 3e-15 / 7e-16.
"""
import math
hbarc_eVm = 1.97327e-7
tP, lP = 5.391e-44, 1.616e-35
MPl, MPl_red = 1.2209e28, 2.435e27   # eV
yr = 3.15576e7
age = 13.79e9 * yr
Nsteps = age / tP
print(f"age in Planck times N_steps = {Nsteps:.3e}; 1/N_steps = {1/Nsteps:.3e}")
# critical density
G = 6.6743e-11; c = 2.99792458e8; Mpc = 3.0857e22
H0 = 67.7e3 / Mpc
rho_c = 3 * H0**2 / (8 * math.pi * G)           # kg/m^3
u_c = rho_c * c**2 / 1.602176634e-19              # eV/m^3
rho_c_eV4 = u_c * hbarc_eVm**3
kB = 8.617333e-5
T0 = 2.7255 * kB                                   # eV
rho_g_eV4 = math.pi**2 / 15 * T0**4
print(f"rho_crit = {rho_c_eV4:.3e} eV^4; rho_CMB = {rho_g_eV4:.3e} eV^4")
for name, M in (("M_Pl", MPl), ("reduced M_Pl", MPl_red)):
    print(f"  (iii) gravitational-strength state LV: rho_crit/{name}^4 = {rho_c_eV4/M**4:.2e}; rho_CMB/{name}^4 = {rho_g_eV4/M**4:.2e}")
alpha = 1/137.036; me = 0.51100e6
dv_photon = (44/135) * alpha**2 * rho_g_eV4 / me**4
print(f"  SM medium effect, photon in CMB (Euler-Heisenberg, RECALLED formula dv = -(44/135) a^2 rho/m_e^4): |dv| = {dv_photon:.2e}")
for E in (1e9, 1e12, 1.4e15):
    print(f"  SM medium effect, electron thermal-mass anisotropy ~ alpha T0^2/E^2 at E = {E:.1e} eV: {alpha*T0**2/E**2:.1e}")
F1 = 2.66e-19
print(f"F1 bound (c_gamma - c_e) = {F1:.2e}")
# natural-size LV from an O(1) lattice-scale vector condensate coupled at loop size (F2 instance)
nat = 8.55e-3
print(f"  O(1) record-sector condensate coupled at F2's natural size {nat:.2e}: miss factor {nat/F1:.2e} (needs coupling suppression <= {F1/nat:.1e})")
# route P2: label density with the F7 budget (refereed O4 number: <= 5.3e-11 /s per nucleon, 0.1 um Gaussian lock)
rate = 5.3e-11
cum = rate * age
print(f"route P2: cumulative records per nucleon over the age at the F7 budget = {cum:.2e}")
for name, n in (("Earth-density matter (3.3e30 nucleons/m^3)", 3.3e30), ("cosmic mean baryons (0.25 /m^3)", 0.25)):
    per_site = n * lP**3 * cum
    print(f"  records (= persistent worldlines) per lattice site, {name}: {per_site:.1e}  -> LV ~ g x {per_site:.1e} vs F1 {F1:.1e}")
# slow-gradient anisotropy of a gentle arrow
print(f"gentle arrow: a d_t ln n ~ 1/N_steps = {1/Nsteps:.1e}; quadratic {1/Nsteps**2:.1e}; "
      f"dimension-3 b-type ~ M_Pl/N_steps = {MPl/Nsteps:.1e} eV (electron b bounds ~1e-22 eV, RECALLED order)")
# route P1 (soft, column toy): permanence of every record in the observable universe with prob >= 1 - delta
Nb = 1e80
Nrec = Nb * cum
for delta in (1e-2, 1e-6):
    umax = delta / (Nrec * Nsteps)
    h = 1 / Nsteps
    eps = math.sqrt(umax * h)
    print(f"route P1 (column toy, K(1->0)=eps^2/h, arrow 1/h = age): delta={delta:.0e}: N_rec={Nrec:.1e}, "
          f"need K(1->0) <= {umax:.1e} per record per step; h = {h:.1e}; eps <= {eps:.1e} (cost -ln eps >= {-math.log(eps):.0f})")
# (iii) literal bar in Earth matter: rho_Earth / rho_Planck
rho_E = 5.5e3 * c**2                     # J/m^3
hbar = 1.054571817e-34
rho_P = c**7 / (hbar * G**2)             # J/m^3
print(f"(iii) literal bar in Earth matter: rho/M_Pl^4 = {rho_E/rho_P:.1e}; tagged-record LV at g=1e-2: {1e-2*3.2e-67:.1e}")
print(f"flash-law rarity estimate: Gamma/E for a 1 GeV nucleon at 5.3e-11/s = {5.3e-11*6.582e-16/1e9:.1e}")
