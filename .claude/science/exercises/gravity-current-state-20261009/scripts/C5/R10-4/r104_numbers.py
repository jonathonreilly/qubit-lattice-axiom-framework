"""R10-4 numbers (natural units, GeV; comparator inputs labelled).

N1 rho_Lambda, Planck masses, phase-transition sizes (R5-3 inputs).
N2 mu-tuning size for a conserved chemical potential.
N3 stochastic (Poisson) record q-charge: potential noise dPhi ~ G chi^-1 / sqrt(q0), scale independent.
N4 Klinkhamer-Volovik electroweak remnant E_ew^8/E_P^4 (comparator 0905.1919).
N5 Brown-Teitelboim single-flux record steps: step size, thin-wall bounce, step counts, AdS crunch after EW.
N6 Thermostat on the stress trace: local residual rho_V = -(rho_m - 3 p_m)/4.
"""
import numpy as np
import sympy as sp

hbarc = 1.97327e-16      # GeV m
hbar = 6.58212e-25       # GeV s
c = 2.99792458e8
GeV4_to_m4 = (1 / hbarc)**4          # GeV^4 -> m^-4
MP = 1.22089e19          # unreduced Planck mass, GeV (G = 1/MP^2)
MPr = MP / np.sqrt(8 * np.pi)   # reduced
G = 1 / MP**2
lP = hbarc / MP          # m

print("=== N1 inputs ===")
H0 = 67.4 * 1e3 / 3.0857e22          # s^-1
H0_GeV = H0 * hbar
OmL = 0.6847
rho_crit = 3 * H0_GeV**2 / (8 * np.pi * G)
rhoL = OmL * rho_crit
print(f"H0 = {H0_GeV:.4e} GeV ; rho_crit = {rho_crit:.4e} GeV^4 ; rho_Lambda = {rhoL:.4e} GeV^4 = ({rhoL**0.25*1e12:.3f} meV)^4")
mH, v = 125.25, 246.22
dV_EW = mH**2 * v**2 / 8
dV_QCD = (4e-4, 3e-3)
print(f"Delta V_EW = m_H^2 v^2/8 = {dV_EW:.4e} GeV^4 = {dV_EW/rhoL:.3e} rho_Lambda  (R5-3: 4.721e54)")
print(f"Delta V_QCD = {dV_QCD[0]:.1e}-{dV_QCD[1]:.1e} GeV^4 = {dV_QCD[0]/rhoL:.2e}-{dV_QCD[1]/rhoL:.2e} rho_Lambda")
print(f"Planck tadpole MPr^4 = {MPr**4:.3e} GeV^4 = {MPr**4/rhoL:.3e} rho_Lambda")

print("\n=== N2 conserved mu: required precision ===")
print("Along eps'(q)=mu: d rho_V/d mu = -q0 (r104_variation.out S3). A later shift Delta needs delta mu = Delta/q0;")
print("so mu fixed before the EW transition must anticipate it: relative precision rho_Lambda/Delta_EW =", f"{rhoL/dV_EW:.3e}")

print("\n=== N3 Poisson record q-charge: noise vs compensation ===")
# region of 4-size l: N = q0 l^4, delta rho = chi^-1 / sqrt(N), delta Phi ~ G delta rho l^2 = G chi^-1 / sqrt(q0): l cancels
l, q0s, chi, Gs = sp.symbols('l q0 chi G', positive=True)
dPhi = Gs * (chi / sp.sqrt(q0s * l**4)) * l**2
print("dPhi(l) =", sp.simplify(dPhi), " (independent of l: white noise at every scale down to the record spacing)")
qP = MP**4  # one record per unprimed Planck 4-volume (GeV^4)
for chi_name, chi_v in [("chi^-1 = MPr^4 (compensate the Planck tadpole)", MPr**4),
                        ("chi^-1 = Delta V_EW (compensate EW only, Delta ln q ~ 1)", dV_EW),
                        ("chi^-1 = Delta V_QCD (QCD only)", dV_QCD[1])]:
    print(" ", chi_name)
    for target in (1e-5, 1e-18):
        q0_req = (G * chi_v / target)**2
        print(f"    dPhi <= {target:.0e}: q0 >= {q0_req:.3e} GeV^4 = {q0_req/qP:.3e} per Planck 4-volume"
              f" = {q0_req*GeV4_to_m4*c:.3e} m^-3 s^-1 ; spacing {(q0_req*GeV4_to_m4)**-0.25:.3e} m")
    dphi_planck = G * chi_v / np.sqrt(qP)
    print(f"    at one record per Planck 4-volume: dPhi = {dphi_planck:.3e}")
# matter-following flashes as q (R4-5 GRW scale): 1e-9 s^-1 per nucleon at ~1 nucleon/m^3 cosmic mean
q_flash = 1e-9 * 0.25 / c / GeV4_to_m4   # per m^3 s -> per m^4 -> GeV^4
print(f"  cosmic-mean matter-following flashes (1e-9 /s per baryon, 0.25 /m^3): q0 = {q_flash:.3e} GeV^4;"
      f" EW-only dPhi = {G*dV_EW/np.sqrt(q_flash):.3e}")

print("\n=== N4 KV electroweak remnant (comparator 0905.1919: E_ew ~ 1e3 GeV, reduced E_P) ===")
for Eew in (2.5e2, 5e2, 1e3, 2e3):
    r = Eew**8 / MPr**4
    print(f"  E_ew = {Eew:.0e} GeV: E_ew^8/E_P^4 = {r:.3e} GeV^4 = {r/rhoL:.3e} rho_Lambda  (=({r**0.25*1e12:.3f} meV)^4)")
print("  sensitivity: rho ~ E_ew^8, so a factor 2 in E_ew is a factor 256; prefactor not fixed by KV (verified summary).")

print("\n=== N5 Brown-Teitelboim single-flux record steps ===")
delta = rhoL     # step must be <~ rho_Lambda for the endpoint to land within the observed value
for B in (1e2, 1e3):
    # flat-space thin-wall: B = 27 pi^2 sigma^4 / (2 delta^3)
    sigma = (2 * B * delta**3 / (27 * np.pi**2))**0.25
    print(f"  bounce B <= {B:.0e} with step {delta:.2e} GeV^4 needs tension sigma <= {sigma:.3e} GeV^3 = ({sigma**(1/3)*1e12:.3f} meV)^3")
print(f"  steps to relax Delta V_EW: {dV_EW/delta:.2e}; Delta V_QCD: {dV_QCD[1]/delta:.2e}")
# EW: if the vacuum was relaxed to ~0 before EW, afterwards rho_V = -Delta V_EW (BT steps only go down)
g_star = 106.75
T_cross = (dV_EW / (np.pi**2 / 30 * g_star))**0.25
t_ads = np.sqrt(3 / (8 * np.pi * G * dV_EW)) * hbar
print(f"  rho_V = -Delta V_EW after EW: radiation falls below |rho_V| at T = {T_cross:.1f} GeV;"
      f" AdS time scale sqrt(3/(8 pi G |rho|)) = {t_ads:.2e} s  (crunch long before BBN at ~1 s)")
T_bbn = 1e-3
rho_bbn = np.pi**2 / 30 * 10.75 * T_bbn**4
print(f"  radiation density at T = 1 MeV: {rho_bbn:.2e} GeV^4 = {rho_bbn/rhoL:.2e} rho_Lambda; reheating by a final step of size"
      f" ~rho_Lambda gives T ~ {(rhoL/(np.pi**2/30*3.36))**0.25*1e12:.2f} meV")

print("\n=== N6 local thermostat on the total stress trace ===")
rV, rm, pm = sp.symbols('rho_V rho_m p_m', real=True)
trace = -4 * rV + (-rm + 3 * pm)      # T^mu_mu, signature (-+++): vacuum -4 rho_V, fluid -rho + 3p
print("T^mu_mu = 0  =>  rho_V =", sp.solve(sp.Eq(trace, 0), rV)[0],
      " ; for dust rho_V = -rho_m/4 (negative, tracks matter; KP's global residual is the 4-volume average of the same)")
for name, rho_m in [("cosmic mean today", 0.315 * rho_crit), ("Earth surface rock 5.5 g/cc", 5.5e3 * (hbarc**3) / 1.78266e-27 * 1.0)]:
    pass
rho_earth = 5.5e3 / 1.78266e-27 * hbarc**3   # kg/m^3 -> GeV/m^3 -> GeV^4
print(f"  dust today: rho_V = {-0.315*rho_crit/4:.3e} GeV^4 = {-0.315*rho_crit/4/rhoL:.3f} rho_Lambda (wrong sign for acceleration)")
print(f"  inside rock (5.5 g/cm^3): |rho_V| = {rho_earth/4:.3e} GeV^4 = {rho_earth/4/rhoL:.3e} rho_Lambda; its stress p_V = +rho_m/4"
      " acts on matter as a pressure of order rho_m/4 unless the relaxation is slower than local dynamics")
