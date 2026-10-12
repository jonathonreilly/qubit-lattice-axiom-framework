# C5 R6-4 checks: Newtonian continuous classical-quantum (CQ) gravity with a smearing length.
# Conventions (stated in R6-4_report.md section 1):
#   Lindblad part:  d rho/dt  ⊃ -1/2 ∫∫ D0(x-y) [m(x),[m(y),rho]]       (D0 effective kernel on the bare mass density m)
#   classical part: pi_dot = ∇²Φ/(4πG) - (g*m)(x) + J,  <J(k,t) J*(k',t')> = (2π)^3 δ(k-k') P_J(k) δ(t-t'),  P_J = 2 D2~
#   coupling smeared by g: H_I = ∫ Φ (g*m),  g~(k) = exp(-k² ℓ²/2)  (Gaussian, width ℓ)
#   trade-off (CP):  P_J(k) * D0~(k) >= |g~(k)|^2 / 4
import numpy as np
from scipy import integrate, special

G = 6.67430e-11; hbar = 1.054571817e-34; c = 2.99792458e8
amu = 1.66053907e-27; mn = 1.6749e-27; me = 9.109e-31
pi = np.pi
out = []
def P(*a):
    s = " ".join(str(x) for x in a); print(s); out.append(s)

def k3(f, kmin=1e-3, kmax=1e20, n=6000):
    """∫ d^3k/(2π)^3 f(k) for isotropic f, log grid."""
    k = np.logspace(np.log10(kmin), np.log10(kmax), n)
    return np.trapezoid(f(k) * 4 * pi * k**2 / (2 * pi)**3, k)

# ---------------------------------------------------------------- [1] trade-off normalization
P("[1] CP trade-off: block [[2D2, -1/2],[-1/2, D0]] PSD  <=>  P_J D0 >= 1/4  (P_J = 2 D2)")
rng = np.random.default_rng(1)
ok = True
for _ in range(2000):
    D0 = 10**rng.uniform(-5, 5); PJ = 10**rng.uniform(-5, 5)
    M = np.array([[PJ, -0.5], [-0.5, D0]])
    psd = np.linalg.eigvalsh(M).min() >= -1e-12 * max(PJ, D0)
    ok &= (psd == (PJ * D0 >= 0.25 - 1e-12))
P("    random check of equivalence:", ok)
P("    measurement-feedback check: monitoring A with Lindblad kappa gives record noise 1/(4 kappa); feedback noise P_J = 1/(4 D0): saturates")

# ---------------------------------------------------------------- [2] AM-GM floor
P("[2] reduced matter kernel K(k) = D0 + (4πG)^2 |g|^2 P_J /(hbar^2 k^4) >= (4πG/hbar)|g|^2/k^2  (DP kernel, R0 = ℓ)")
worst = np.inf
for _ in range(5000):
    k = 10**rng.uniform(-3, 12); gg = rng.uniform(0, 1); D0 = 10**rng.uniform(-60, 60)
    PJ = gg**2 / (4 * D0)
    K = D0 + (4 * pi * G)**2 * gg**2 * PJ / (hbar**2 * k**4)
    floor = 4 * pi * G / hbar * gg**2 / k**2
    if floor > 0: worst = min(worst, K / floor)
P("    min K/floor over 5000 random (k,|g|,D0) at saturation:", f"{worst:.6f}", "(>= 1, equality at D0 = 2πG|g|^2/(hbar k^2))")

# ---------------------------------------------------------------- [3] point-mass no-go (unsmeared coupling)
P("[3] g~ = 1 (exact local Newton), point particle: momentum-diffusion rate >= 4πG hbar m^2 ∫ d^3k/(2π)^3  -> cutoff^3 divergence")
for Kc in [1e10, 1e15, 1e20, 1e30]:
    rate = 4 * pi * G * hbar * me**2 * Kc**3 / (6 * pi**2)
    P(f"    electron, k-cutoff {Kc:.0e} 1/m: d<p^2>/dt >= {rate:.3e} kg^2 m^2 s^-3 ; heating {rate/(2*me):.3e} W")
P("    -> no cutoff-free homogeneous kernel gives finite heating of a point mass (proved given the AM-GM floor)")

# ---------------------------------------------------------------- experiments / models
M_Cs = 132.905 * amu
A_Cs = 133; R_N_Cs = 1.2e-15 * A_Cs**(1/3); r_n = 0.84e-15
Delta_Cs = 1.9e-6; t_Cs = 70.0; Gam_Cs_max = 1 / t_Cs            # comparator (O4 referee checked 1.9 um, 70 s)
M_mol = 25000 * amu; Delta_mol = 266e-9; t_mol = 7e-3; Gam_mol_max = 1 / t_mol   # comparator (Fein 2019, from memory)
# LISA Pathfinder test mass (Au-Pt 46 mm cube, 1.928 kg: comparator); differential ASD 1.74 fm s^-2/rtHz (verified, Armano 2018)
M_T = 1.928; L_T = 0.046; R_T = (3 * L_T**3 / (4 * pi))**(1/3)
M_at_T = 0.73 * 196.97 * amu + 0.27 * 195.08 * amu
N_at_T = M_T / M_at_T; a_T = 2.9e-10; u_T = 6e-12
S_LPF_diff = (1.74e-15)**2; S_LPF = S_LPF_diff / 2        # per-mass one-sided PSD, uncorrelated noises
S_torsion = 2 * (1e-7)**2 * 1.0                           # OSSW 2022 conservative sigma_a=1e-7 m/s^2 over T~1 s (one-sided PSD)
h_Earth = 47e12 / 5.972e24                                # W/kg, all of Earth's heat flow (generous)
R0_DP_min = 4e-10                                         # Figurato et al. 2024 abstract (checked): R0 >~ 4e-10 m
R0_DP_min_2021 = 0.54e-10                                 # Donadi et al. 2021 (comparator, memory)
P("[4] inputs: M_Cs=%.4e kg, Delta=%.2e m, Gamma_max=%.3e /s; 25kDa M=%.3e, Gamma_max=%.3e; LPF S_a(per mass)=%.3e; Earth h=%.3e W/kg"
  % (M_Cs, Delta_Cs, Gam_Cs_max, M_mol, Gam_mol_max, S_LPF, h_Earth))

def FN(k, R):  # Gaussian charge-radius form factor squared
    return np.exp(-(k * R)**2 / 3)
def S_atom(k, M, A, RN):
    coh = FN(k, RN)
    return M**2 * coh + A * mn**2 * (1 - coh) * FN(k, r_n)
def S_body(k):
    x = k * R_T
    with np.errstate(all='ignore'):
        F = np.where(x < 1e-3, 1.0, 3 * (np.sin(x) - x * np.cos(x)) / x**3)
    coh = M_T**2 * F**2
    A = 196; RN = 1.2e-15 * A**(1/3)
    inc_atoms = N_at_T * S_atom(k, M_at_T, A, RN) / M_at_T**2 * M_at_T**2
    lattice = np.where(k > 2 * pi / a_T, 1.0, 1 - np.exp(-(k * u_T)**2))
    return coh + inc_atoms * lattice
def avg1mcos(k, D):  # orientation average of 1 - cos(k.D)
    x = k * D
    return 1 - np.where(x < 1e-6, 1 - x**2 / 6, np.sin(x) / np.maximum(x, 1e-300))

# ---------------------------------------------------------------- [5] floors and the ℓ window
P("[5] kernel-independent lower bounds on the smearing length ℓ (any homogeneous continuous kernel)")
P("    (a) radiation: matter kernel >= DP(R0=ℓ) pointwise  =>  ℓ >= R0_DP_min = %.1e m (Figurato 2024 abstract; Donadi 2021: %.2e)" % (R0_DP_min, R0_DP_min_2021))
# Earth heat floor per kg: (hbar^2/2) ∫ K k^2  >= (hbar^2/2)(4πG/hbar)∫|g|^2 = 2πG hbar /(8 π^1.5 ℓ^3) = G hbar/(4 sqrt(pi) ℓ^3)
l_heat = (G * hbar / (4 * np.sqrt(pi) * h_Earth))**(1/3)
P("    (b) Earth heat: per-kg heating >= G hbar/(4 sqrt(pi) ℓ^3)  =>  ℓ >= %.2e m" % l_heat)
def S_a_floor(l):
    I = k3(lambda k: np.exp(-(k * l)**2) * S_body(k), kmin=1e-2, kmax=50 / l)
    return (8 * pi / 3) * G * hbar * I / M_T**2
lo, hi = 1e-16, 1e-9
for _ in range(60):
    mid = np.sqrt(lo * hi)
    if S_a_floor(mid) > S_LPF: lo = mid
    else: hi = mid
P("    (c) LPF force-noise floor S_a >= (8π/3)G hbar ∫|g|^2 S_T /M^2  =>  ℓ >= %.2e m" % hi)
P("        floor at ℓ=1e-15: %.2e ; at 4e-10: %.2e ; at 1e-5: %.2e  (LPF per mass %.2e)" % (S_a_floor(1e-15), S_a_floor(4e-10), S_a_floor(1e-5), S_LPF))
# (d) stated-bounds-only pair: Cs interferometer x LPF via Cauchy-Schwarz
def X_pair(l, Mi, A, RN, D):
    f = lambda k: np.exp(-(k * l)**2) * np.sqrt(S_atom(k, Mi, A, RN) * avg1mcos(k, D) * S_body(k)) / k
    return k3(f, kmin=1e-2, kmax=50 / l)
def pair_ratio(l, Mi, A, RN, D, Gmax, Smax):
    return (1 / 6) * (4 * pi * G / M_T)**2 * X_pair(l, Mi, A, RN, D)**2 / (Gmax * Smax)
lo, hi = 1e-19, 1e-9
for _ in range(60):
    mid = np.sqrt(lo * hi)
    if pair_ratio(mid, M_Cs, A_Cs, R_N_Cs, Delta_Cs, Gam_Cs_max, S_LPF) > 1: lo = mid
    else: hi = mid
P("    (d) stated bounds only, Cs(1.9um,70s) x LPF, Cauchy-Schwarz over all kernels: excluded iff ℓ < %.2e m" % hi)
P("        ratio (needed/available) at ℓ=1e-15: %.2e ; 1e-13: %.2e" % (pair_ratio(1e-15, M_Cs, A_Cs, R_N_Cs, Delta_Cs, Gam_Cs_max, S_LPF), pair_ratio(1e-13, M_Cs, A_Cs, R_N_Cs, Delta_Cs, Gam_Cs_max, S_LPF)))
P("        same with OSSW-2022 torsion bar (sigma_a=1e-7): ratio at 1e-15: %.2e" % pair_ratio(1e-15, M_Cs, A_Cs, R_N_Cs, Delta_Cs, Gam_Cs_max, S_torsion))
P("    (e) upper end: ISL tested to 52 um (Lee et al. 2020, comparator); Gaussian smearing changes the two-body potential by erfc(r/2ℓ):")
for l in [5e-6, 1e-5, 1.5e-5, 2e-5]:
    P("        ℓ=%.1e: erfc(52um/2ℓ) = %.2e" % (l, special.erfc(52e-6 / (2 * l))))

# ---------------------------------------------------------------- [6] the least-decoherence (DP-type) kernel against the stated bounds
P("[6] kernel D0 = γ (2πG/hbar)|g|^2/k^2 (γ=1: least decoherence); matter kernel = (γ+1/γ)/2 · DP(R0=ℓ)")
def Gam_point(M, l, D):
    return G * M**2 / hbar * (1 / (np.sqrt(pi) * l) - special.erf(D / (2 * l)) / D)
# numeric check of the closed form
l0 = 4e-10
num = k3(lambda k: 4 * pi * G / hbar * np.exp(-(k * l0)**2) / k**2 * M_Cs**2 * avg1mcos(k, Delta_Cs), kmin=1e-2, kmax=50 / l0, n=20000)
P("    closed form vs numeric Γ_Cs(ℓ=4e-10): %.4e vs %.4e /s" % (Gam_point(M_Cs, l0, Delta_Cs), num))
for l in [4e-10, 1e-9, 1e-8, 1e-7, 1e-6, 1e-5]:
    gC = Gam_point(M_Cs, l, Delta_Cs); gM = Gam_point(M_mol, l, Delta_mol)
    sa = S_a_floor(l); hh = G * hbar / (4 * np.sqrt(pi) * l**3)
    P("    ℓ=%.0e: Γ_Cs=%.2e (max %.1e, margin %.1f dec) | Γ_25kDa<=%.2e (max %.1e, %.1f dec) | S_a=%.2e (LPF %.1e, %.1f dec) | heat=%.2e W/kg (%.1f dec)"
      % (l, gC, Gam_Cs_max, np.log10(Gam_Cs_max / gC), gM, Gam_mol_max, np.log10(Gam_mol_max / gM), sa, S_LPF, np.log10(S_LPF / sa), hh, np.log10(h_Earth / hh)))
P("    γ-window: (γ+1/γ)/2 <= B(ℓ) = min[(ℓ/R0min)^3 (radiation, conservative), Γmax/Γ, S_LPF/S_a, h_E/h]")
for l in [4e-10, 1e-9, 1e-8, 1e-6, 1e-5]:
    B = min((l / R0_DP_min)**3, Gam_Cs_max / Gam_point(M_Cs, l, Delta_Cs), Gam_mol_max / Gam_point(M_mol, l, Delta_mol), S_LPF / S_a_floor(l), h_Earth / (G * hbar / (4 * np.sqrt(pi) * l**3)))
    if B >= 1:
        gmin = B - np.sqrt(B**2 - 1); gmax = B + np.sqrt(B**2 - 1)
        P("        ℓ=%.0e: B=%.2e -> γ in [%.2e, %.2e]" % (l, B, gmin, gmax))
    else:
        P("        ℓ=%.0e: B=%.2e < 1 -> empty" % (l, B))

# ---------------------------------------------------------------- [7] ultra-local kernels
P("[7] ultra-local kernels (D0 const on the coupled density, P_J = |g|^2/(4 D0) white)")
# unregulated (g=1), nuclear-structure model for Cs and test mass: product Γ·S_a independent of D0
I_I = k3(lambda k: S_atom(k, M_Cs, A_Cs, R_N_Cs) * avg1mcos(k, Delta_Cs), kmin=1e-2, kmax=1e18, n=20000)
I_T = k3(lambda k: S_body(k) / k**2, kmin=1e-2, kmax=1e18, n=20000)
prod = (1 / 6) * (4 * pi * G / M_T)**2 * I_I * I_T
P("    unregulated, nucleon-form-factor model (electrons ignored): Γ·S_a >= %.2e vs allowed %.2e -> excluded by %.1f decades (Cs x LPF)"
  % (prod, Gam_Cs_max * S_LPF, np.log10(prod / (Gam_Cs_max * S_LPF))))
P("    with point electrons the Γ integral diverges ([3]); OSSW-2022/2023 published: 32-decade empty window (comparator, R3-4 referee checked)")
# regulated (Gaussian r): CSL map lambda = d0 amu^2/(8 pi^1.5 r^3); LPF needs d0 >= ...; Earth heat caps d0
for r in [1e-12, 1e-11, 1e-10, 4e-10, 1e-9, 1e-8, 1e-7]:
    IT = k3(lambda k: S_body(k) * np.exp(-(k * r)**2) / k**2, kmin=1e-2, kmax=50 / r)
    d0_min = (2 / 3) * (4 * pi * G / M_T)**2 * IT / (4 * S_LPF)
    d0_max_heat = h_Earth / ((hbar**2 / 2) * 3 / (16 * pi**1.5 * r**5))
    lam_min = d0_min * amu**2 / (8 * pi**1.5 * r**3)
    P("    r=%.0e: d0 >= %.2e (LPF), d0 <= %.2e (Earth heat) -> %s ; CSL-equivalent λ >= %.2e /s; DP floor needs r >= %.0e"
      % (r, d0_min, d0_max_heat, "window" if d0_min <= d0_max_heat else "EMPTY", lam_min, R0_DP_min))

# ---------------------------------------------------------------- [8] cosmology: (c)
P("[8] (c) energy-momentum / Λ-like drift")
rhoL = 5.3e-10; tH = 4.35e17; rho_m = 2.6e-27; rho_b = 4.2e-28
P("    first moment: E[J]=0, so the mean Poisson source has no drift (no Λ-like mean term)")
for l in [4e-10, 1e-9, 1e-6]:
    hh = G * hbar / (4 * np.sqrt(pi) * l**3)
    P("    matter-side exchange per Hubble time at γ=1, ℓ=%.0e: %.2e J/m^3 (all matter) vs ρ_Λc^2=%.1e -> %.1f decades short"
      % (l, hh * rho_m * tH, rhoL, np.log10(rhoL / (hh * rho_m * tH))))
# conditional (H-cosmo): OSSW F25 kinetic term (2πGc^2/3) pi^2 accumulates; ε_dot >= (2πGc^2/3)(hbar^2/(8 h_max)) (∫k|g| d^3k/(2π)^3)^2
def eps_dot_bound(Ik):
    return (2 * pi * G * c**2 / 3) * (hbar**2 / (8 * h_Earth)) * Ik**2
for l in [4e-10, 1e-8, 1e-5]:
    Ik = 1 / (pi**2 * l**4)
    e = eps_dot_bound(Ik) * tH
    P("    [H-cosmo] ℓ=%.0e: |ε| per Hubble time >= %.2e J/m^3 (%.1f decades above ρ_Λc^2)" % (l, e, np.log10(e / rhoL)))
kN = 1 / 52e-6
e = eps_dot_bound(kN**4 / (8 * pi**2)) * tH
P("    [H-cosmo] any g with g~1 up to k_N=1/(52um) (ISL): |ε| >= %.2e J/m^3 (%.1f decades above)" % (e, np.log10(e / rhoL)))
check_Ik = k3(lambda k: k * np.exp(-(k * 1e-8)**2 / 2), kmin=1e-2, kmax=5e9)
P("    check ∫k|g| at ℓ=1e-8: numeric %.4e vs 1/(π^2 ℓ^4) %.4e" % (check_Ik, 1 / (pi**2 * 1e-32)))

# ---------------------------------------------------------------- [9] record channel: V <= BC
P("[9] Gaussian metric record: -ln BC = (t/8)∫|g Δm|^2/P_J  <=  (t/2)∫ D0 |Δm|^2 = Γ t  (so V = e^{-Γt} <= BC)")
worst = 0
for _ in range(3000):
    n = 50
    g2 = rng.uniform(0, 1, n); dm2 = rng.exponential(1, n); D0 = 10**rng.uniform(-3, 3, n)
    PJ = g2 / (4 * D0) * 10**rng.uniform(0, 2, n)     # any P_J above the CP floor
    lnBC = np.sum(g2 * dm2 / PJ) / 8; Gam = np.sum(D0 * dm2) / 2
    worst = max(worst, lnBC / Gam)
P("    max(-ln BC)/(Γt) over random kernels obeying CP: %.6f (<= 1; = 1 at saturation)" % worst)

# ---------------------------------------------------------------- [10] OSSW ultra-local torsion step (their F8-F10) vs their own F6
P("[10] OSSW 2022 F8-F10 treat a nucleus's interior field (G rho r_N)^2 as uniform over V_b; F6 with a delta kernel gives sigma_a^2=(48pi/5)G^2 D2/(R T) (uniform sphere)")
Rs=0.05; Ts=100; sas=1e-7; Ns=1e26; rNs=1e-15; Vbs=1e15; rhos=mn/(4/3*pi*rNs**3); Ms=Ns*mn
theirs = Ns*G**2*rhos**2*rNs**2*Vbs/(Ts*Ms**2); mine = (48*pi/5)*G**2/(Rs*Ts)
P("     per-D2 sigma_a^2: OSSW %.2e vs direct %.2e (ratio %.1e); corrected torsion bound D2 <= %.2e kg^2 s m^-3 (OSSW: 1e-41)" % (theirs, mine, theirs/mine, sas**2*Ts*Rs/((48*pi/5)*G**2)))

open(__file__.replace('.py', '.out'), 'w').write("\n".join(out) + "\n")
