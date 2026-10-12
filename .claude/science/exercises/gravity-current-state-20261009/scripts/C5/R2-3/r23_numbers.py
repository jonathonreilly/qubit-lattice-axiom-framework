"""R2-3 arithmetic: per-particle (rGRWf-type, mass-proportional) flashes on a
continuum, against heat, Lambda drift, TT channel, GW strain, definiteness.
SI units unless stated. Every input is printed with its source label.
"""
import math
from scipy.integrate import quad

hbar = 1.054571817e-34; c = 2.99792458e8; G = 6.67430e-11; kB = 1.380649e-23
mN = 1.67262192e-27; eV = 1.602176634e-19; sigmaSB = 5.670374419e-8
lP = math.sqrt(hbar * G / c**3); tP = lP / c
MPl_eV = math.sqrt(hbar * c / G) * c**2 / eV          # non-reduced, eV
# unit conversions to natural units (eV)
m_to_inv_eV = 1 / (hbar * c / eV)                     # 1 m = this many eV^-1
s_to_inv_eV = eV / hbar                               # 1 s = this many eV^-1
J_per_m3_to_eV4 = (1 / eV) / m_to_inv_eV**3
print(f"lP={lP:.4e} m tP={tP:.4e} s  M_Pl={MPl_eV:.4e} eV;  1 J/m^3 = {J_per_m3_to_eV4:.4e} eV^4")

# ---------------- flash law parameters
rC = 1e-7
lam_GRW = 1e-16
dE_flash = 3 * hbar**2 / (4 * mN * rC**2)             # GRW/CSL per-flash heating, r_C = 0.1 um
P_GRW = lam_GRW * dE_flash
print(f"\n[a] per-flash heating 3hbar^2/(4 m rC^2) = {dE_flash:.4e} J = {dE_flash/eV:.4e} eV;"
      f" kick variance per axis hbar^2/(2rC^2) -> rms {hbar/(math.sqrt(2)*rC):.3e} kg m/s")
print(f"    GRW (lam=1e-16) heating per nucleon P = {P_GRW:.4e} W")

# heat budgets (per nucleon)
P_earth = 47e12 / 5.97e24 * mN                        # O4 H4 (refereed allowance), W per nucleon
print(f"\n[d] Earth-heat allowance (O4 H4): {P_earth:.3e} W/nucleon -> lam_max(rC=0.1um) = {P_earth/dE_flash:.3e} s^-1"
      f"  (O4 quotes 2.6e-11 in CSL convention)")
# neutron star: T_inf < 42,000 K (Guillot et al. 2019 HST, checked by web search), R = 12 km, 1.4 Msun
R_ns = 12e3; M_ns = 1.4 * 1.989e30; N_ns = M_ns / mN; T_ns = 4.2e4
L_max = 4 * math.pi * R_ns**2 * sigmaSB * T_ns**4
P_ns = L_max / N_ns
print(f"    NS (T<42kK, R=12km, 1.4Msun; redshift ignored): L_max={L_max:.3e} W, P_max={P_ns:.3e} W/nucleon"
      f" -> lam_max={P_ns/dE_flash:.3e} s^-1")
T_eq_GRW = (N_ns * P_GRW / (4 * math.pi * R_ns**2 * sigmaSB))**0.25
print(f"    NS equilibrium surface T at GRW rate: {T_eq_GRW:.1f} K (state-independent heating; Tilloy-Stace form)")
t_H = 13.8e9 * 3.156e7
dT_igm = (2 / 3) * P_GRW * t_H / kB
P_igm = 1e4 * kB * 1.5 / t_H                          # allow <~1e4 K over a Hubble time
print(f"    IGM: GRW heating over t_H gives dT = {dT_igm:.3e} K per baryon; allowance ~1e4 K -> P_max ~{P_igm:.2e} W,"
      f" lam_max ~{P_igm/dE_flash:.1e}")
lam_xray = 5e-15
print(f"    X-ray (as quoted in repo DECISION_MATRIX.md:82 for mass-proportional CSL at rC=1e-7; exact Majorana number not re-verified): lam <~ {lam_xray:.0e}")

# ---------------- (g) definiteness vs heat: trade-off bound
print("\n[g] registered pointer: N=1e10 nucleons, d=1 um, localize within 1 ms (needs Gamma >= 1e3 s^-1)")
N_ptr = 1e10; d = 1e-6; Gam_need = 1e3
print(f"    independent per-particle flashes, d >> rC: needs lam >= {Gam_need/N_ptr:.1e} s^-1")
for name, Pm in (("Earth heat (O4 H4)", P_earth), ("NS 42kK", P_ns), ("IGM ~1e4K", P_igm),
                 ("X-ray-quoted lam*dE", lam_xray * dE_flash)):
    G_iso = N_ptr * mN * d**2 * Pm / (3 * hbar**2)
    G_any = 3 * G_iso
    print(f"    {name:22s}: P_max={Pm:.3e} W -> Gamma_max(isotropic envelope) = {G_iso:.3e} s^-1,"
          f" (any envelope) = {G_any:.3e} s^-1;  shortfall vs 1e3: x{Gam_need/G_any:.2e}")
# minimal pointer for 1 ms at Earth-heat budget, any envelope
N_min = Gam_need * hbar**2 / (mN * d**2 * P_earth)
print(f"    minimal isolated pointer (d=1um, 1ms, Earth heat, any envelope): N >= {N_min:.3e} nucleons")
# environmental amplification: 1 um sphere in air
n_air = 2.45e25; v_air = 470.0; sig = math.pi * (0.5e-6)**2
R_coll = n_air * v_air * sig
R_nuc = R_coll * 29
lam_env = 2 / (R_nuc * (1e-3)**2)
print(f"    in air: collisions {R_coll:.3e} s^-1 -> {R_nuc:.3e} recording nucleons/s;"
      f" int lam N_eff dt >= 1 in 1 ms needs lam >= {lam_env:.2e} s^-1"
      f" (Earth-heat lam_max {P_earth/dE_flash:.2e}; X-ray-quoted {lam_xray:.0e}; GRW {lam_GRW:.0e})")
for lam in (lam_GRW, lam_xray, P_earth / dE_flash):
    tdef = math.sqrt(2 / (lam * R_nuc))
    print(f"      lam={lam:.1e}: definiteness time for the pointer in air ~ {tdef*1e3:.3g} ms")

# ---------------- (f) flash densities
pl_density = 1 / (lP**3 * tP)
print(f"\n[f] Planck event density = {pl_density:.3e} m^-3 s^-1")
for name, n in (("water 6e29", 6e29), ("Earth mean 3.3e30", 5514 / mN), ("cosmic baryons 0.25", 0.2515)):
    for lname, lam in (("GRW", lam_GRW), ("X-ray-quoted", lam_xray), ("Earth-heat max", P_earth / dE_flash)):
        rate = n * lam
        print(f"    {name:20s} {lname:15s}: {rate:.3e} flashes m^-3 s^-1 = {rate/pl_density:.3e} of Planck density")

# ---------------- (b) Lambda drift from the homogeneous mean heating (UG, JPS form)
H0 = 67.4e3 / 3.0857e22; Om = 0.315; Orad = 9.1e-5; OL = 1 - Om - Orad
rho_crit = 3 * H0**2 / (8 * math.pi * G)
rhoL = OL * rho_crit * c**2
n_b0 = 0.0224 / 0.674**2 * rho_crit / mN
print(f"\n[b] H0={H0:.4e} s^-1, rho_Lambda={rhoL:.4e} J/m^3, n_b0={n_b0:.4f} m^-3")
Hz = lambda z: H0 * math.sqrt(Om * (1 + z)**3 + Orad * (1 + z)**4 + OL)
def inj(zmax, zmin=0.0):
    # int J_0 dt = P * int n_b(t) dt ; dt = dz/((1+z)H)
    g = lambda u: n_b0 * math.exp(3 * u) / Hz(math.expm1(u)) # u = ln(1+z), dt = du/H
    val, _ = quad(g, math.log1p(zmin), math.log1p(zmax), limit=400)
    return val
for zmax in (1.0, 1e3, 1e9, 1e12):
    I = inj(zmax)
    for lname, lam in (("GRW", lam_GRW), ("X-ray-quoted", lam_xray), ("Earth-heat max", P_earth / dE_flash)):
        dr = lam * dE_flash * I
        print(f"    z_max={zmax:8.0e} {lname:15s}: Delta rho_Lambda = {dr:.3e} J/m^3 = {dr/rhoL:.3e} rho_Lambda")
for lname, lam in (("GRW", lam_GRW), ("X-ray-quoted", lam_xray), ("Earth-heat max", P_earth / dE_flash)):
    rate = n_b0 * lam * dE_flash / (H0 * rhoL)
    print(f"    today d ln rho_Lambda / d ln a = J0/(H0 rho_L) [{lname}] = {rate:.3e}  (w+1 ~ -{rate/3:.1e})")

# ---------------- (c) TT channel
mu_P0 = 2.39e8                                         # eV^4, PRICE_NOTE P0 (B referee c1)
print(f"\n[c] P0 mu = {mu_P0:.3e} eV^4")
def heat_density_eV5(n, lam):
    return n * lam * dE_flash * J_per_m3_to_eV4 / s_to_inv_eV   # (J/m^3/s) -> eV^5
omegas = {"Hubble": H0, "PTA 1/yr": 2 * math.pi / 3.156e7, "LIGO 100Hz": 2 * math.pi * 100}
for name, n in (("cosmic baryons", n_b0), ("Earth", 5514 / mN), ("NS core 0.5 fm^-3", 0.5e45)):
    for lname, lam in (("GRW", lam_GRW), ("Earth-heat max", P_earth / dE_flash)):
        q = heat_density_eV5(n, lam)
        s = "  ".join(f"{k}: {q/(w/s_to_inv_eV):.2e}" for k, w in omegas.items())
        print(f"    covariant-law secular response bound rho_dot/omega [{name}, {lname}] (eV^4): {s}")
# additive stress noise S_TT(0) (white below 1/tau_r): S ~ n lam <dtau^2> tau_r^2
J2sm3_to_eV4 = (1 / eV)**2 * s_to_inv_eV / m_to_inv_eV**3
print(f"    1 J^2 s m^-3 = {J2sm3_to_eV4:.3e} eV^4")
for name, n, T, tau in (("IGM (T=1e4K, tau_r=2e12 s Spitzer ion)", n_b0, 1e4, 2e12),
                        ("IGM, tau_r capped at t_H", n_b0, 1e4, t_H),
                        ("Earth solid (300K, tau_r=1e-12 s)", 5514 / mN, 300, 1e-12)):
    for lname, lam in (("GRW", lam_GRW), ("Earth-heat max", P_earth / dE_flash)):
        dtau2 = kB * T * hbar**2 / (mN * rC**2)
        S = n * lam * dtau2 * tau**2 * J2sm3_to_eV4
        print(f"    additive S_TT(0) [{name}, {lname}] = {S:.3e} eV^4  (vs mu {mu_P0:.2e}: not a mass, see report)")
# stochastic GW background from flash stress steps, PTA and LIGO bands
G_nat = 1 / MPl_eV**2
rho_crit_eV4 = rho_crit * c**2 * J_per_m3_to_eV4
for bname, w in (("PTA", 2 * math.pi / 3.156e7), ("LIGO", 2 * math.pi * 100)):
    for lname, lam in (("GRW", lam_GRW), ("Earth-heat max", P_earth / dE_flash)):
        dtau2 = kB * 1e4 * hbar**2 / (mN * rC**2)
        S_w = n_b0 * lam * dtau2 / w**2 * J2sm3_to_eV4     # omega*tau_r >> 1
        w_eV = w / s_to_inv_eV
        rho_gw = G_nat * w_eV**4 * S_w * (t_H * s_to_inv_eV)  # O(1) factor omitted
        print(f"    Omega_gw({bname}, {lname}) ~ {rho_gw/rho_crit_eV4:.2e}  (PTA signal ~1e-9; O(1) prefactor omitted)")
# direct force noise on test masses (per-particle independent kicks), one-sided S_F = N lam hbar^2/rC^2
for name, M, f0, Sx_ref in (("LIGO 40 kg mirror, 100 Hz, L=4 km", 40.0, 100.0, 4e-24),):
    for lname, lam in (("GRW", lam_GRW), ("Earth-heat max", P_earth / dE_flash)):
        SF = (M / mN) * lam * hbar**2 / rC**2
        x = math.sqrt(SF) / (M * (2 * math.pi * f0)**2)
        print(f"    {name} [{lname}]: sqrt S_F={math.sqrt(SF):.2e} N/rtHz, strain {x/4e3:.2e}/rtHz vs LIGO ~{Sx_ref:.0e}")
for lname, lam in (("GRW", lam_GRW), ("Earth-heat max", P_earth / dE_flash)):
    M = 1.928
    SF = (M / mN) * lam * hbar**2 / rC**2
    print(f"    LISA Pathfinder 1.93 kg [{lname}]: sqrt S_a = {math.sqrt(SF)/M:.2e} m s^-2/rtHz vs ~1.7e-15 measured")

# ---------------- size of the per-flash Ward/constraint defect (Setting Q), estimate
for r in (1e-7, 1e-6):
    print(f"\n[b'] (l_P/r_C)^2 = (Delta p/(M_Pl c))^2 with Delta p = hbar/r_C, r_C={r:.0e}: {(lP/r)**2:.3e} per flash per nucleon"
          f" (dimensionless gauge-defect strength; estimate)")
