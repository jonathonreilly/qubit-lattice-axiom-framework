"""R3-4 checks: set A's gravity escapes E1-E5.

[1] Lemma P inputs: localization branches on a ground state all raise energy;
    mean heating equals Lemma H's c-number (nonrelativistic check).
[2] E1 signalling toy: field at Charlie under conditional-<T> sourcing vs linear sourcing.
[3] E4 sizes: acausal ADM / dipole updates per flash and for a species-conversion signal.
[4] E5 reservoir: stored energy density a static reservoir would need inside the Earth.
[5] CQ windows (Oppenheim et al. 2023 Table 1 numbers, comparator): widths in decades.
All SI units. numpy only.
"""
import numpy as np

hbar = 1.054571817e-34
G = 6.67430e-11
c = 2.99792458e8
mN = 1.67262192e-27
mE = 5.972e24

print("[1] Lemma P inputs: localization on a ground state (1D harmonic oscillator, m = 1, hbar = 1, omega = 1)")
x = np.linspace(-30, 30, 24001)
dx = x[1] - x[0]
m, w = 1.0, 1.0
psi0 = np.exp(-x**2 / 2); psi0 /= np.sqrt(np.sum(psi0**2) * dx)


def energy(psi):
    dpsi = np.gradient(psi, dx)
    kin = 0.5 * np.sum(dpsi**2) * dx / m
    pot = 0.5 * m * w**2 * np.sum(x**2 * psi**2) * dx
    return kin + pot


E0 = energy(psi0)
for rC in [0.3, 1.0, 3.0]:
    # amplitude multiplier f(x-X) with int f^2 dX = 1 (normalized Gaussian density of width rC)
    Xs = np.linspace(-(8 + 5 * rC), 8 + 5 * rC, 1601)
    dX = Xs[1] - Xs[0]
    probs, dEs = [], []
    for X in Xs:
        f = (2 * np.pi * rC**2) ** (-0.25) * np.exp(-(x - X) ** 2 / (4 * rC**2))
        phi = f * psi0
        p = np.sum(phi**2) * dx
        phin = phi / np.sqrt(p)
        probs.append(p); dEs.append(energy(phin) - E0)
    probs = np.array(probs); dEs = np.array(dEs)
    mean_dE = np.sum(probs * dEs) * dX
    lemmaH = 1.0 / (2 * m) * (1.0 / (4 * rC**2))  # hbar^2/(2m) int |f'|^2 = 1/(8 m rC^2) per axis
    print(f"  r_C = {rC}: total prob = {np.sum(probs)*dX:.6f}; min branch dE = {dEs.min():.6e} (all > 0: {bool((dEs > 0).all())}); "
          f"mean dE = {mean_dE:.6f}; Lemma H = {lemmaH:.6f}")

# a hot state: some branches can LOSE energy, but the mean still rises by the same c-number
psi_hot = np.exp(-(x - 4) ** 2 / 2) + np.exp(-(x + 4) ** 2 / 2)
psi_hot = psi_hot / np.sqrt(np.sum(psi_hot**2) * dx)
Eh = energy(psi_hot)
rC = 1.0
Xs = np.linspace(-10, 10, 1001); dX = Xs[1] - Xs[0]
probs, dEs = [], []
for X in Xs:
    f = (2 * np.pi * rC**2) ** (-0.25) * np.exp(-(x - X) ** 2 / (4 * rC**2))
    phi = f * psi_hot; p = np.sum(phi**2) * dx
    probs.append(p); dEs.append(energy(phi / np.sqrt(p)) - Eh)
probs = np.array(probs); dEs = np.array(dEs)
print(f"  two-packet state (|x|=4), r_C = 1: min branch dE = {dEs.min():.4f}, max = {dEs.max():.4f}, "
      f"mean = {np.sum(probs*dEs)*dX:.6f} (Lemma H 0.125)")

print("\n[2] E1 signalling toy (conditional-<T> sourcing) vs linear sourcing")
m_A = 1e-14       # kg, Alice's mesoscopic mass
d = 1e-6          # m, superposition separation
r = 10e-6         # m, Charlie's distance along the axis
gL = G * m_A / (r - d / 2) ** 2
gR = G * m_A / (r + d / 2) ** 2
gavg = 0.5 * (gL + gR)
print(f"  g_L = {gL:.4e}, g_R = {gR:.4e}, mean-field g = {gavg:.4e} m/s^2; |g_L - g_mean| = {abs(gL-gavg):.3e}")
print("  Bob measures Z -> Charlie's classical field is g_L or g_R (p = 1/2 each).")
print("  Bob measures X -> Alice's mass stays superposed -> field is g_mean with certainty.")
print("  Single-shot distinguishable (total-variation distance 1 for a resolving field reading): signal.")
print("  Linear (E3/E4): Charlie's reduced state is the same 50/50 mixture of L/R fields for both choices: no signal.")
N_A = m_A / mN
for lam in [1e-16, 1e-11]:
    print(f"  GRW self-collapse time of Alice's mass at lambda = {lam:g}: 1/(N lambda) = {1/(N_A*lam):.3e} s (N = {N_A:.2e})")

print("\n[3] E4 sizes: acausal monopole and dipole updates")
rCg = 1e-7
dE_flash = 3 * hbar**2 / (4 * mN * rCg**2)   # R2-3 convention (O4 used half)
print(f"  per-nucleon flash energy (R2-3 convention) = {dE_flash:.4e} J; delta M = {dE_flash/c**2:.4e} kg")
NE = mE / mN
for lam, lab in [(1e-16, "GRW"), (2.64e-11, "Earth-heat max (R2-3 convention)")]:
    P = NE * lam * dE_flash
    print(f"  Earth ({lab}): flash heating {P:.3e} W; ADM mass growth {P/c**2:.3e} kg/s")
# species-conversion signal: per-particle mass-proportional heating power is mass independent
Pp = 1e-16 * dE_flash
Nb, T = 1e27, 1.0
dM = Nb * Pp * T / c**2
print(f"  Bob converts 1e27 flashing particles into non-flashing quanta for 1 s: delta E = {Nb*Pp*T:.3e} J, "
      f"delta M = {dM:.3e} kg, delta g at 1 m = {G*dM:.3e} m/s^2 (instantaneous on the dressing slice)")
mp = 1e10 * mN; dp = 1e-6
print(f"  pointer (1e10 nucleons, 1 um) localization: dipole change m d = {mp*dp:.3e} kg m; "
      f"far-field change at 1 m ~ G m d / r^3 = {G*mp*dp:.3e} m/s^2 per outcome, zero on average")

print("\n[4] E5 reservoir: static energy store needed inside the Earth over its age")
VE = 4 / 3 * np.pi * 6.371e6**3
age = 4.5e9 * 3.156e7
for lam, lab in [(1e-16, "GRW"), (2.64e-11, "Earth-heat max")]:
    P = NE * lam * dE_flash
    u = P * age / VE
    print(f"  {lab}: drain {P/VE:.3e} W/m^3; stored need {u:.3e} J/m^3 = {u/c**2:.3e} kg/m^3 mass-equivalent;"
          f" surface influx if replenished {P/(4*np.pi*6.371e6**2):.3e} W/m^2")
nb = 0.25  # baryons per m^3 today
H0age = 4.35e17
rho_L = 0.69 * 3 * (67.7e3 / 3.0857e22) ** 2 / (8 * np.pi * G) * c**2
print(f"  cosmic: GRW heating of all baryons over 4.35e17 s = {nb*1e-16*dE_flash*H0age:.3e} J/m^3 vs rho_Lambda c^2 = {rho_L:.3e} J/m^3")

print("\n[5] CQ windows (Oppenheim et al. 2023, Table 1 as fetched; comparator)")
rows = [("ultra-local continuous D2 [kg^2 s m^-3]", 1e-41, 1e-9),
        ("non-local (DP-type) lP^2 D2 [kg^2 s m^-1]", 1e-9, 1e-35),
        ("ultra-local discrete lP^2 D2/mP [kg]", 1e-1, 1e-25)]
for name, up, low in rows:
    width = np.log10(up / low)
    print(f"  {name}: upper {up:g}, lower {low:g} -> window {width:+.0f} decades ({'EMPTY' if width < 0 else 'open'})")

print("\n[6] E5' emission-type flashes funded by an internal store (Lemma P: matter must lose >= |dp| c per flash)")
for rCe in [1e-7, 1e-6]:
    dp = np.sqrt(3.0 / 2.0) * hbar / rCe          # rms |dp| for the R2-3 Gaussian envelope (variance hbar^2/(2 rC^2) per axis)
    Emin = dp * c
    for lam in [1e-16, 1e-11]:
        P_E = NE * lam * Emin
        frac = Emin / (mN * c**2)
        print(f"  r_C = {rCe:g}, lambda = {lam:g}: emitted energy per flash >= {Emin:.3e} J ({Emin/1.602e-19:.3f} eV); "
              f"Earth emission {P_E:.3e} W (Earth heat flow 4.7e13 W); per-flash rest-mass loss {frac:.3e}; "
              f"drift {lam*frac*3.156e7:.3e} per yr")

print("\n[7] E5 ambient reservoir: can a gravitating medium fund the flashes causally?")
u_gamma = 4.17e-14                     # J/m^3, CMB photons today (RECALLED)
u_dr = 0.3 * (7 / 8) * (4 / 11) ** (4 / 3) * u_gamma   # Delta N_eff <= 0.3 (RECALLED Planck-era bound)
F_dr = u_dr * c / 4
RE = 6.371e6
for lam, lab in [(1e-16, "GRW"), (2.64e-11, "Earth-heat max")]:
    need = NE * lam * dE_flash / (4 * np.pi * RE**2)
    print(f"  {lab}: needed influx {need:.3e} W/m^2; dark-radiation max one-sided flux (Delta N_eff 0.3) {F_dr:.3e} W/m^2 "
          f"-> ratio need/available {need/F_dr:.2f}")
rho_dm = 0.4 * 1.602e-10 / 1e-6        # J/m^3 rest energy, local dark matter 0.4 GeV/cm^3 (RECALLED)
v_dm = 2.3e5
print(f"  cold clustered medium at local DM density: rest-energy flux {rho_dm*v_dm/4:.3e} W/m^2 (ample)")
