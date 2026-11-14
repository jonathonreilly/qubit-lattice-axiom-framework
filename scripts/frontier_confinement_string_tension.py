#!/usr/bin/env python3
"""
Confinement and String Tension in the Cl(3) / Z³ Framework
===========================================================

STATUS: bounded support note / qualitative confinement consistency check

SUPPORT CLAIM (bounded):
  The graph-first SU(3) gauge-sector context with g_bare = 1 gives the
  Wilson plaquette parameter beta = 6. Confinement itself is imported
  standard SU(3) Yang-Mills context; this runner does not show it. With
  imported Sommer-scale and EFT inputs it computes conditional string-tension
  estimates, and it runs a small finite Monte Carlo diagnostic.

INPUTS (imported or supplied, not derived here):
  1. Graph-first SU(3) at g_bare = 1 → Wilson plaquette at β = 2N_c/g² = 6
     (computed from the supplied normalization).
  2. Confinement of SU(3) Yang-Mills is imported literature context. It is
     printed as IMPORTED CONTEXT and is not a counted check.
  3. A bounded source value α_s(M_Z) = 0.1181 is consumed as an EFT input.
  4. Two-loop QCD running from M_Z with flavor thresholds → Λ_QCD.
  5. The lattice ratio √σ / Λ_MS̄, the Sommer-scale data at β = 6 and the
     0.96 screening factor are supplied, not derived here.

CONDITIONAL ESTIMATE (not a framework prediction):
  From α_s(M_Z) = 0.1181 → Λ_MS̄^(5) ≈ 210 MeV. With the supplied ratio
  and Sommer-scale data the two estimates are about 518 MeV (Method 1) and
  465 MeV (Method 2 with the supplied 0.96 factor); the comparator is 440 MeV.
  This is bounded: conditioned on the standard low-energy EFT bridge.

FINITE DIAGNOSTIC (not an area-law or string-tension extraction):
  Pure-gauge SU(3) Monte Carlo at β = 6.0 on a 4⁴ lattice reports <P> and
  the three small loops W(1,1), W(1,2), W(2,2).
  - Their decreasing order is consistent with an area law, but a perimeter
    law W = exp(-c(R+T)) satisfies the same order (analytic control below).
  - The Creutz ratio χ(2,2) is zero for a pure perimeter law, so χ(2,2) > 0
    beyond its blocked-jackknife error rules out a pure perimeter law for
    these loops. A short-distance term with no area term also gives
    χ(2,2) > 0 (second control), so the small-loop χ(2,2) does not
    establish an asymptotic string tension or confinement.

PStack experiment: frontier-confinement-string-tension
Self-contained: numpy only.
"""

from __future__ import annotations

import sys
from pathlib import Path
import numpy as np
from canonical_plaquette_surface import CANONICAL_ALPHA_BARE, CANONICAL_ALPHA_S_V, CANONICAL_PLAQUETTE, CANONICAL_U0

np.set_printoptions(precision=10, linewidth=120, suppress=True)

AUDIT_TIMEOUT_SEC = 600
AUDIT_INPUT_PATHS = ("docs/CONFINEMENT_STRING_TENSION_NOTE.md",)

PASS_COUNT = 0
FAIL_COUNT = 0
NOTE_PATH = Path(__file__).resolve().parents[1] / "docs" / "CONFINEMENT_STRING_TENSION_NOTE.md"


def check(name, condition, detail="", kind="EXACT"):
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    tag = f" [{kind}]" if kind != "EXACT" else ""
    msg = f"  [{status}]{tag} {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition


def imported(item, detail=""):
    """Print imported context. It is not a check and is not counted."""
    msg = f"  IMPORTED CONTEXT: {item}"
    if detail:
        msg += f"  ({detail})"
    print(msg)


def supplied(item, detail=""):
    """Print a supplied input value. It is not a check and is not counted."""
    msg = f"  SUPPLIED: {item}"
    if detail:
        msg += f"  ({detail})"
    print(msg)


def loop_ordering(w11, w12, w22):
    """The two ordering tests the runner applies to small Wilson loops."""
    return w12 < w11, w22 < w12


def creutz_chi22(w11, w12, w21, w22):
    """Creutz ratio chi(2,2) = -ln[W(2,2) W(1,1) / (W(1,2) W(2,1))].

    Perimeter and corner factors cancel. For W = exp(-V(R)T - c(R+T)) it
    equals V(2) - V(1); for a pure area law exp(-sigma R T - c(R+T)) it
    equals sigma.
    """
    return -np.log((w22 * w11) / (w12 * w21))


# =============================================================================
# Framework constants
# =============================================================================

P_PLAQ = CANONICAL_PLAQUETTE        # plaquette expectation on the Cl(3)/Z³ surface
U0 = CANONICAL_U0                   # tadpole factor
ALPHA_BARE = CANONICAL_ALPHA_BARE
G_BARE_SQ = 4 * np.pi * ALPHA_BARE  # = 1
N_C = 3
BETA_LATTICE = 2 * N_C / G_BARE_SQ  # = 6.0

ALPHA_S_V = CANONICAL_ALPHA_S_V
V_EW = 246.28281829012906  # GeV, hierarchy theorem
M_Z = 91.1876  # GeV
ALPHA_S_MZ = 0.1181  # bounded alpha_s source value consumed as EFT input

# Quark thresholds (PDG central values)
M_T = 172.69   # GeV
M_B = 4.18     # GeV
M_C = 1.27     # GeV

# Experimental comparison
SQRT_SIGMA_EXP = 0.440  # GeV, from Regge slope / heavy quarkonium


# =============================================================================
# Part 1: Beta=6 SU(3) support surface
# =============================================================================

def test_structural_confinement():
    """Verify the bounded support surface: beta=6 plus imported YM context."""
    print("\n=== Part 1: Beta=6 SU(3) support surface ===\n")

    check("g_bare² = 4π α_bare = 1",
          abs(G_BARE_SQ - 1.0) < 1e-12,
          f"g² = {G_BARE_SQ:.6f}")

    check("β = 2N_c/g² = 6.0",
          abs(BETA_LATTICE - 6.0) < 1e-12,
          f"β = {BETA_LATTICE:.1f}")

    supplied(f"N_c = {N_C} (from graph-first SU(3))",
             "graph-first commutant: gl(3) ⊕ gl(1), compact part su(3); used in β above")

    imported("Standard SU(3) YM confinement is imported, not derived here",
             "used as bounded Yang-Mills/lattice background")

    imported("β = 6.0 is on the standard low-temperature pure-gauge surface",
             "literature context; not a continuum confinement proof")

    # Plaquette consistency
    # At β = 6.0, standard lattice QCD: <P> ≈ 0.5934
    # This is a known result — the framework's <P> matches
    p_lattice_qcd = 0.5934  # standard MC result at β = 6.0
    check("Framework plaquette input matches the standard β=6 reuse value",
          abs(P_PLAQ - p_lattice_qcd) < 0.001,
          f"<P>_framework = {P_PLAQ}, <P>_lattice = {p_lattice_qcd}")

    return True


# =============================================================================
# Part 2: QCD coupling running and Λ_QCD
# =============================================================================

def beta0(nf):
    """One-loop β-function coefficient: β₀ = (33 - 2N_f)/(12π)."""
    return (33 - 2 * nf) / (12 * np.pi)


def beta1(nf):
    """Two-loop β-function coefficient: β₁ = (306 - 38N_f)/(48π²)."""
    return (306 - 38 * nf) / (48 * np.pi ** 2)


def lambda_msbar(mu, alpha_s, nf):
    """Compute Λ_MS̄^(N_f) from α_s at scale μ using two-loop formula.

    Λ = μ × exp[-1/(2β₀α)] × (β₀α)^{-β₁/(2β₀²)}
    """
    b0 = beta0(nf)
    b1 = beta1(nf)
    a = alpha_s
    return mu * np.exp(-1.0 / (2 * b0 * a)) * (b0 * a) ** (-b1 / (2 * b0 ** 2))


def run_alpha_s(alpha_s_0, mu0, mu1, nf):
    """Run α_s from scale μ₀ to μ₁ at two-loop accuracy.

    Uses iterative solution of the implicit two-loop equation.
    """
    b0 = beta0(nf)
    b1 = beta1(nf)
    L = np.log(mu1 ** 2 / mu0 ** 2)

    # One-loop seed
    a = alpha_s_0 / (1 + b0 * alpha_s_0 * L)

    # Newton iteration for two-loop
    for _ in range(20):
        lam = lambda_msbar(mu0, alpha_s_0, nf)
        t = np.log(mu1 ** 2 / lam ** 2)
        # Two-loop implicit: 1/α = β₀ t + (β₁/β₀) ln(t)
        rhs = b0 * t + (b1 / b0) * np.log(t)
        a = 1.0 / rhs

    return a


def test_coupling_running():
    """Compute Λ_QCD and α_s at various scales from the bounded source value."""
    print("\n=== Part 2: QCD coupling running and Λ_QCD ===\n")

    # Bounded source input.
    supplied(f"bounded α_s(M_Z) source value = {ALPHA_S_MZ} (consumed as EFT input)")

    # Compute Λ_MS̄^(5) from α_s(M_Z) = 0.1181 with N_f = 5
    lam5 = lambda_msbar(M_Z, ALPHA_S_MZ, 5)
    check("Λ_MS̄^(5) ≈ 210 MeV (from two-loop formula)",
          abs(lam5 - 0.210) < 0.015,
          f"Λ^(5) = {lam5 * 1000:.1f} MeV (PDG: 210 ± 14 MeV)",
          kind="BOUNDED")

    # Run α_s down to m_b threshold
    alpha_mb = run_alpha_s(ALPHA_S_MZ, M_Z, M_B, 5)
    check("α_s(m_b) ≈ 0.225 (run from M_Z with N_f = 5)",
          abs(alpha_mb - 0.225) < 0.015,
          f"α_s(m_b) = {alpha_mb:.4f} (PDG: 0.2268)",
          kind="BOUNDED")

    # Match to N_f = 4 at m_b (continuity)
    lam4 = lambda_msbar(M_B, alpha_mb, 4)
    check("Λ_MS̄^(4) ≈ 292 MeV",
          abs(lam4 - 0.292) < 0.030,
          f"Λ^(4) = {lam4 * 1000:.1f} MeV",
          kind="BOUNDED")

    # Run to m_c threshold
    alpha_mc = run_alpha_s(alpha_mb, M_B, M_C, 4)
    check("α_s(m_c) ≈ 0.39 (run from m_b with N_f = 4)",
          abs(alpha_mc - 0.39) < 0.04,
          f"α_s(m_c) = {alpha_mc:.4f}",
          kind="BOUNDED")

    # Match to N_f = 3 at m_c
    lam3 = lambda_msbar(M_C, alpha_mc, 3)
    check("Λ_MS̄^(3) in range 300–400 MeV (two-loop, no higher-order matching)",
          0.300 < lam3 < 0.400,
          f"Λ^(3) = {lam3 * 1000:.1f} MeV (PDG: 332 ± 17 MeV; two-loop matching only)",
          kind="BOUNDED")

    # α_s grows and becomes non-perturbative below ~ 1 GeV
    # This is where confinement sets in
    alpha_1gev = run_alpha_s(alpha_mc, M_C, 1.0, 3)
    check("α_s(1 GeV) > 0.4 (entering non-perturbative regime)",
          alpha_1gev > 0.4,
          f"α_s(1 GeV) ≈ {alpha_1gev:.3f} → perturbation theory breaks down",
          kind="BOUNDED")

    return lam5, lam4, lam3


# =============================================================================
# Part 3: String tension prediction
# =============================================================================

def test_string_tension(lam5, lam3):
    """Estimate sqrt(sigma) from imported low-energy QCD context."""
    print("\n=== Part 3: Conditional string-tension estimates (imported inputs) ===\n")

    # The ratio √σ / Λ_MS̄ is a universal QCD constant.
    # From lattice QCD determinations:
    #
    # Quenched (N_f = 0): σ / Λ_MS̄^(0)² ≈ 3.06 ± 0.18  (Bali 2000)
    #   → √σ / Λ^(0) ≈ 1.75
    #
    # N_f = 2+1 (physical): the string tension is reduced by quark screening.
    # The phenomenological value √σ ≈ 440 MeV combined with Λ^(3) ≈ 332 MeV
    # gives the ratio √σ / Λ^(3) ≈ 1.33.
    #
    # For this bounded support estimate, use:
    # sqrt(sigma)_support = (sqrt(sigma)/Lambda)_lattice * Lambda_source

    # Method 1: From Λ^(3) and lattice ratio
    ratio_nf3 = 1.33  # √σ / Λ_MS̄^(3), from lattice/phenomenology
    sqrt_sigma_1 = ratio_nf3 * lam3

    check("Method 1: √σ from Λ^(3) × supplied (√σ/Λ)_lattice = 1.33",
          abs(sqrt_sigma_1 - SQRT_SIGMA_EXP) / SQRT_SIGMA_EXP < 0.20,
          f"√σ = {ratio_nf3:.2f} × {lam3 * 1000:.0f} MeV = {sqrt_sigma_1 * 1000:.0f} MeV "
          f"(exp: {SQRT_SIGMA_EXP * 1000:.0f} MeV, "
          f"dev: {(sqrt_sigma_1 - SQRT_SIGMA_EXP) / SQRT_SIGMA_EXP * 100:+.1f}%)",
          kind="BOUNDED")

    # Method 2: Direct from Sommer scale
    # At beta = 6.0 (the support-surface coupling), standard lattice QCD gives:
    #   r₀/a = 5.37 ± 0.05   (Sommer parameter in lattice units)
    #   a = r₀ / 5.37 = 0.472 fm / 5.37 = 0.0879 fm
    #   σa² = 0.0465 ± 0.001  (Creutz ratio, large Wilson loops)
    #   √σ = √(0.0465) / 0.0879 fm = 2.453 fm⁻¹ = 484 MeV (quenched)
    #
    # With dynamical quarks (N_f = 2+1), the string tension is reduced
    # by ~10% due to quark-pair screening.

    r0_fm = 0.472  # Sommer parameter, fm
    r0_over_a = 5.37  # at β = 6.0 (quenched)
    a_fm = r0_fm / r0_over_a
    sigma_a2_quenched = 0.0465  # Creutz ratio at β = 6.0 (quenched)
    sqrt_sigma_quenched = np.sqrt(sigma_a2_quenched) / a_fm  # fm⁻¹
    hbarc = 0.197327  # GeV⋅fm
    sqrt_sigma_quenched_gev = sqrt_sigma_quenched * hbarc

    check("Method 2: quenched √σ at β = 6.0 from supplied Sommer-scale data",
          abs(sqrt_sigma_quenched_gev - 0.484) < 0.03,
          f"√σ_quenched = {sqrt_sigma_quenched_gev * 1000:.0f} MeV "
          f"(quenched value at beta=6)",
          kind="BOUNDED")

    # With dynamical quarks: ~10% reduction
    screening_factor = 0.96  # rough factor for N_f = 2+1
    sqrt_sigma_physical = sqrt_sigma_quenched_gev * screening_factor

    check("Method 2: √σ after the supplied 0.96 screening factor (not derived; see B2)",
          abs(sqrt_sigma_physical - SQRT_SIGMA_EXP) / SQRT_SIGMA_EXP < 0.08,
          f"√σ_phys ≈ {sqrt_sigma_physical * 1000:.0f} MeV "
          f"(exp: {SQRT_SIGMA_EXP * 1000:.0f} MeV, "
          f"dev: {(sqrt_sigma_physical - SQRT_SIGMA_EXP) / SQRT_SIGMA_EXP * 100:+.1f}%)",
          kind="BOUNDED")

    # Sensitivity analysis: how much does √σ change with α_s?
    # d(ln Λ)/d(α_s) = 1/(2β₀α_s²) at one loop
    b0_5 = beta0(5)
    sensitivity = 1.0 / (2 * b0_5 * ALPHA_S_MZ ** 2)
    delta_alpha = 0.1181 - 0.1179  # source value minus comparator
    delta_sqrt_sigma_pct = sensitivity * delta_alpha * 100

    check("Sensitivity: Δ(√σ)/√σ ≈ {:.1f}% from Δα_s = {:.4f}".format(
          abs(delta_sqrt_sigma_pct), abs(delta_alpha)),
          abs(delta_sqrt_sigma_pct) < 5.0,
          f"source α_s is 0.2% high vs comparator -> √σ shifts by ~{delta_sqrt_sigma_pct:+.1f}%",
          kind="BOUNDED")

    return True


# =============================================================================
# Part 4: Pure-gauge Monte Carlo at β = 6.0
# =============================================================================

def random_su3_near_identity(rng, epsilon=0.24):
    """SU(3) matrix near identity for Metropolis proposal."""
    H = rng.standard_normal((3, 3)) + 1j * rng.standard_normal((3, 3))
    H = (H + H.conj().T) / 2.0  # Hermitian
    H -= np.trace(H) / 3.0 * np.eye(3)  # traceless
    X = np.eye(3, dtype=complex) + 1j * epsilon * H
    # Project to SU(3) via QR
    Q, R = np.linalg.qr(X)
    d = np.diag(R)
    ph = d / np.abs(d)
    Q = Q @ np.diag(np.conj(ph))
    det = np.linalg.det(Q)
    Q *= np.exp(-1j * np.angle(det) / 3)
    return Q


def compute_staple(links, x, mu, L, ndim=4):
    """Compute the staple sum for link U_μ(x) in ndim dimensions.

    The staple is the sum over ν ≠ μ of:
      U_ν(x+μ̂) U_μ†(x+ν̂) U_ν†(x)  +  U_ν†(x+μ̂−ν̂) U_μ†(x−ν̂) U_ν(x−ν̂)
    """
    S = np.zeros((3, 3), dtype=complex)
    xp = list(x)
    xp[mu] = (xp[mu] + 1) % L

    for nu in range(ndim):
        if nu == mu:
            continue

        # Upper staple
        xpn = list(x)
        xpn[nu] = (xpn[nu] + 1) % L
        S += (links[tuple(xp)][nu]
              @ links[tuple(xpn)][mu].conj().T
              @ links[tuple(x)][nu].conj().T)

        # Lower staple
        xm = list(x)
        xm[nu] = (xm[nu] - 1) % L
        xpm = list(xp)
        xpm[nu] = (xpm[nu] - 1) % L
        S += (links[tuple(xpm)][nu].conj().T
              @ links[tuple(xm)][mu].conj().T
              @ links[tuple(xm)][nu])

    return S


def measure_plaquette(links, L, ndim=4):
    """Measure the average plaquette <P> = <Re Tr U_P> / N_c."""
    total = 0.0
    count = 0
    for coords in np.ndindex(*([L] * ndim)):
        x = list(coords)
        for mu in range(ndim):
            for nu in range(mu + 1, ndim):
                xm = list(x)
                xm[mu] = (xm[mu] + 1) % L
                xn = list(x)
                xn[nu] = (xn[nu] + 1) % L
                U_P = (links[tuple(x)][mu]
                       @ links[tuple(xm)][nu]
                       @ links[tuple(xn)][mu].conj().T
                       @ links[tuple(x)][nu].conj().T)
                total += np.trace(U_P).real / N_C
                count += 1
    return total / count


def measure_wilson_loop(links, x0, R, T, mu_dir, nu_dir, L):
    """Measure a single R×T Wilson loop in the (μ,ν) plane starting at x0."""
    W = np.eye(3, dtype=complex)
    x = list(x0)

    # Bottom edge: R steps in μ
    for _ in range(R):
        W = W @ links[tuple(x)][mu_dir]
        x[mu_dir] = (x[mu_dir] + 1) % L

    # Right edge: T steps in ν
    for _ in range(T):
        W = W @ links[tuple(x)][nu_dir]
        x[nu_dir] = (x[nu_dir] + 1) % L

    # Top edge: R steps in −μ
    for _ in range(R):
        x[mu_dir] = (x[mu_dir] - 1) % L
        W = W @ links[tuple(x)][mu_dir].conj().T

    # Left edge: T steps in −ν
    for _ in range(T):
        x[nu_dir] = (x[nu_dir] - 1) % L
        W = W @ links[tuple(x)][nu_dir].conj().T

    return np.trace(W).real / N_C


def test_monte_carlo():
    """Pure-gauge SU(3) Monte Carlo at β = 6.0 on a small lattice."""
    print("\n=== Part 4: Pure-gauge Monte Carlo at β = 6.0 ===\n")

    L = 4
    ndim = 4
    beta = 6.0
    n_therm = 300
    n_meas = 200
    n_skip = 3  # measurements every n_skip sweeps

    rng = np.random.default_rng(2026)

    # Initialize links to identity (cold start)
    links = {}
    for coords in np.ndindex(*([L] * ndim)):
        links[coords] = [np.eye(3, dtype=complex) for _ in range(ndim)]

    print(f"  Lattice: {L}⁴, β = {beta}, cold start")
    print(f"  Thermalizing ({n_therm} sweeps)...")

    accepted = 0
    total = 0

    def metropolis_sweep():
        nonlocal accepted, total
        for coords in np.ndindex(*([L] * ndim)):
            x = list(coords)
            for mu in range(ndim):
                U_old = links[tuple(x)][mu]
                staple = compute_staple(links, x, mu, L, ndim)

                # Propose
                X = random_su3_near_identity(rng)
                U_new = X @ U_old

                # ΔS = -(β/N_c) Re Tr[(U_new - U_old) × staple]
                dS = -(beta / N_C) * np.trace(
                    (U_new - U_old) @ staple
                ).real

                total += 1
                if dS < 0 or rng.random() < np.exp(-dS):
                    links[tuple(x)][mu] = U_new
                    accepted += 1

    # Thermalization
    for sweep in range(n_therm):
        metropolis_sweep()
        if (sweep + 1) % 100 == 0:
            p = measure_plaquette(links, L, ndim)
            acc_rate = accepted / total if total > 0 else 0
            print(f"    sweep {sweep + 1}: <P> = {p:.4f}, acc = {acc_rate:.2f}")

    acc_rate = accepted / total if total > 0 else 0
    print(f"  Acceptance rate: {acc_rate:.2f}")

    check("Acceptance rate in [0.3, 0.8]",
          0.3 < acc_rate < 0.8,
          f"rate = {acc_rate:.2f}",
          kind="BOUNDED")

    # Measurement phase
    print(f"  Measuring ({n_meas} configs, skip {n_skip})...")
    plaq_values = []
    wilson_1x1 = []
    wilson_1x2 = []
    wilson_2x2 = []

    for meas in range(n_meas):
        for _ in range(n_skip):
            metropolis_sweep()

        p = measure_plaquette(links, L, ndim)
        plaq_values.append(p)

        # Wilson loops (averaged over all orientations and positions)
        w11_sum, w12_sum, w22_sum = 0.0, 0.0, 0.0
        w_count = 0
        for coords in np.ndindex(*([L] * ndim)):
            for mu in range(ndim):
                for nu in range(mu + 1, ndim):
                    x0 = list(coords)
                    w11_sum += measure_wilson_loop(links, x0, 1, 1, mu, nu, L)
                    w12_sum += measure_wilson_loop(links, x0, 1, 2, mu, nu, L)
                    w22_sum += measure_wilson_loop(links, x0, 2, 2, mu, nu, L)
                    w_count += 1

        wilson_1x1.append(w11_sum / w_count)
        wilson_1x2.append(w12_sum / w_count)
        wilson_2x2.append(w22_sum / w_count)

    # Analysis
    plaq_mean = np.mean(plaq_values)
    plaq_std = np.std(plaq_values) / np.sqrt(len(plaq_values))

    print(f"\n  <P> = {plaq_mean:.4f} ± {plaq_std:.4f}")

    # At β = 6.0, standard result: <P> ≈ 0.5934
    # On a 4⁴ lattice, finite-size effects shift this; expect within ~5%
    check("MC plaquette consistent with framework <P> = 0.5934",
          abs(plaq_mean - P_PLAQ) / P_PLAQ < 0.08,
          f"<P>_MC = {plaq_mean:.4f} vs <P>_framework = {P_PLAQ}",
          kind="BOUNDED")

    # Wilson loop analysis
    w11_mean = np.mean(wilson_1x1)
    w12_mean = np.mean(wilson_1x2)
    w22_mean = np.mean(wilson_2x2)

    print(f"  W(1,1) = {w11_mean:.6f}")
    print(f"  W(1,2) = {w12_mean:.6f}")
    print(f"  W(2,2) = {w22_mean:.6f}")

    # Ordering of the three small loops. A perimeter law satisfies the same
    # ordering (see the analytic controls), so these are consistency checks.
    order_12_11, order_22_12 = loop_ordering(w11_mean, w12_mean, w22_mean)
    check("W(1,2) < W(1,1): ordering consistent with an area law (a perimeter law also satisfies it)",
          order_12_11,
          f"W(1,2)={w12_mean:.4f} < W(1,1)={w11_mean:.4f}",
          kind="BOUNDED")

    check("W(2,2) < W(1,2): ordering consistent with an area law (a perimeter law also satisfies it)",
          order_22_12,
          f"W(2,2)={w22_mean:.4f} < W(1,2)={w12_mean:.4f}",
          kind="BOUNDED")

    # Creutz ratio: χ(2,2) = −ln(W(2,2)·W(1,1) / (W(2,1)·W(1,2))).
    # W(2,1) = W(1,2) in expectation by the hypercubic symmetry of the L⁴
    # lattice; the runner measures one orientation in each of the six planes.
    # On a 4⁴ lattice χ includes short-distance contributions, so it is not
    # the asymptotic string tension.
    if w22_mean > 1e-10 and w11_mean > 1e-10 and w12_mean > 1e-10:
        chi_22 = creutz_chi22(w11_mean, w12_mean, w12_mean, w22_mean)
        # Blocked jackknife over 10 blocks of consecutive measurements.
        n_blocks = 10
        a11, a12, a22 = (np.array(v) for v in (wilson_1x1, wilson_1x2, wilson_2x2))
        blocks = np.array_split(np.arange(len(a11)), n_blocks)
        chi_jk = []
        for blk in blocks:
            keep = np.setdiff1d(np.arange(len(a11)), blk)
            m11, m12, m22 = a11[keep].mean(), a12[keep].mean(), a22[keep].mean()
            chi_jk.append(creutz_chi22(m11, m12, m12, m22))
        chi_jk = np.array(chi_jk)
        chi_err = float(np.sqrt((n_blocks - 1) / n_blocks
                                * np.sum((chi_jk - chi_jk.mean()) ** 2)))
        print(f"  χ(2,2) = {chi_22:.4f} ± {chi_err:.4f} (blocked jackknife, {n_blocks} blocks)")
        check("Creutz ratio χ(2,2) > 3 errors: rules out a pure perimeter law for these loops",
              chi_22 - 3.0 * chi_err > 0,
              f"χ(2,2) = {chi_22:.4f} ± {chi_err:.4f}; short-distance terms also give "
              f"χ > 0, so this is not an asymptotic string tension",
              kind="BOUNDED")
    else:
        check("Wilson loops have sufficient signal",
              False,
              "signal too noisy for Creutz ratio")

    # The supplied σa² = 0.0465 at β = 6.0 comes from large Wilson loops.
    # On a 4⁴ lattice, the Creutz ratio at small loops overestimates this.
    # We report it but don't require it to match the asymptotic value.

    return True


# =============================================================================
# Part 4b: Analytic controls for the Wilson-loop tests
# =============================================================================

def model_loops(log_w):
    """W(1,1), W(1,2), W(2,1), W(2,2) for a model ln W(R, T)."""
    return tuple(float(np.exp(log_w(r, t))) for r, t in ((1, 1), (1, 2), (2, 1), (2, 2)))


def test_wilson_loop_controls():
    """Show which Wilson-loop test discriminates, on exact model loops."""
    print("\n=== Part 4b: Analytic controls for the Wilson-loop tests ===\n")
    c, sigma, kappa = 0.5, 0.2, 0.15

    # Perimeter law: no area term.
    w11, w12, w21, w22 = model_loops(lambda r, t: -c * (r + t))
    o1, o2 = loop_ordering(w11, w12, w22)
    chi_p = creutz_chi22(w11, w12, w21, w22)
    check("Control: a perimeter law W = exp(-c(R+T)) satisfies both ordering tests",
          o1 and o2,
          f"c = {c}: W(1,1)={w11:.4f} > W(1,2)={w12:.4f} > W(2,2)={w22:.4f}")
    check("Control: the perimeter law has χ(2,2) = 0, so the χ(2,2) > 0 test rejects it",
          abs(chi_p) < 1e-12 and not chi_p > 1e-12,
          f"χ(2,2) = {chi_p:.2e}; the ordering does not discriminate, the Creutz ratio does")

    # Pure area law plus perimeter: chi(2,2) = sigma.
    w11, w12, w21, w22 = model_loops(lambda r, t: -sigma * r * t - c * (r + t))
    chi_a = creutz_chi22(w11, w12, w21, w22)
    check("Control: an area law W = exp(-σRT - c(R+T)) has χ(2,2) = σ",
          abs(chi_a - sigma) < 1e-12,
          f"σ = {sigma}, χ(2,2) = {chi_a:.12f}")

    # Short-distance toy with no area term: chi(2,2) = kappa > 0.
    w11, w12, w21, w22 = model_loops(lambda r, t: -c * (r + t) + kappa * (r / t + t / r))
    o1, o2 = loop_ordering(w11, w12, w22)
    chi_s = creutz_chi22(w11, w12, w21, w22)
    check("Control: a short-distance toy W = exp(-c(R+T) + κ(R/T+T/R)), no area term, has χ(2,2) = κ > 0",
          o1 and o2 and abs(chi_s - kappa) < 1e-12 and chi_s > 0,
          f"κ = {kappa}, χ(2,2) = {chi_s:.12f}; a positive small-loop χ alone "
          f"does not establish a string tension")


# =============================================================================
# Part 5: Imported context (printed, not counted)
# =============================================================================

def test_combined():
    """Print the imported context the note relies on. Nothing here is counted."""
    print("\n=== Part 5: Imported context (printed, not counted) ===\n")

    imported("Graph-first SU(3) at g_bare = 1 gives β = 6 (computed in Part 1)",
             "structural context + declared normalization")
    imported("Standard SU(3) YM confinement is imported context",
             "not a framework-native proof in this note")
    imported("α_s(M_Z) = 0.1181 is consumed as a bounded transfer input",
             "source boundary remains with alpha_s row")
    imported("√σ near 440 MeV is the supplied phenomenological comparator",
             "the Part 3 estimates are conditioned on the standard low-energy EFT bridge")
    imported("The note claims bounded support, not retained confinement closure",
             "beta=6 support + imported YM/lattice context")

    print("\n  --- Textbook consequences of the imported context (not shown by this runner) ---")
    imported("Regge slope α' = 1/(2πσ) at the 440 MeV comparator",
             f"α' = {1.0 / (2 * np.pi * SQRT_SIGMA_EXP ** 2):.2f} GeV⁻²; "
             f"phenomenological value ≈ 0.9 GeV⁻²")
    imported("Quenched deconfinement scale from the supplied ratio T_c/√σ ≈ 0.60",
             f"T_c ≈ {0.60 * SQRT_SIGMA_EXP * 1000:.0f} MeV at √σ = 440 MeV")
    imported("Area law ⇔ linear potential ⇔ chromoelectric flux tube",
             "textbook relation; this runner does not show an area law")

    return True


# =============================================================================
# Part 6: Source-status firewall
# =============================================================================

def test_source_status_firewall():
    """Ensure the companion note does not overstate this support result."""
    print("\n=== Part 6: Source-status firewall ===\n")
    text = NOTE_PATH.read_text(encoding="utf-8")
    flat = " ".join(text.split())

    check("source note declares bounded-support actual current status",
          "actual_current_surface_status: bounded-support" in text
          and "trace_class: upstream_support" in text)
    check("source note does not use proposed_retained wording",
          "proposed_retained" not in text)
    check("source note states confinement is not framework-derived here",
          "does not derive four-dimensional Yang-Mills confinement" in flat
          and "not a first-principles proof" in flat)
    check("source note identifies imported YM/lattice/EFT inputs",
          "imports standard Yang-Mills confinement" in flat
          and "Sommer-scale data" in flat
          and "EFT running" in flat)


# =============================================================================
# Main
# =============================================================================

def main():
    print("=" * 72)
    print("Confinement and String Tension in the Cl(3) / Z³ Framework")
    print("=" * 72)
    print()
    print("SUPPORT: beta=6 graph-first SU(3) context plus imported")
    print("         Yang-Mills/lattice/EFT inputs give conditional string-tension")
    print("         estimates; a finite 4⁴ Monte Carlo is a diagnostic only.")
    print("IMPORTED CONTEXT and SUPPLIED lines are printed, not counted.")
    print()

    test_structural_confinement()
    lam5, lam4, lam3 = test_coupling_running()
    test_string_tension(lam5, lam3)
    test_monte_carlo()
    test_wilson_loop_controls()
    test_combined()
    test_source_status_firewall()

    print()
    print("=" * 72)
    print(f"SUMMARY: PASS={PASS_COUNT}  FAIL={FAIL_COUNT}")
    print("=" * 72)

    if FAIL_COUNT > 0:
        print("\n*** FAILURES DETECTED ***")
        sys.exit(1)
    else:
        print("\nAll counted checks passed: β = 6 arithmetic, conditional")
        print("estimates on imported inputs, a finite 4⁴ Monte Carlo diagnostic")
        print("and analytic Wilson-loop controls. The small-loop ordering and")
        print("Creutz ratio do not establish an area law or a string tension;")
        print("confinement stays imported context, and no retained")
        print("framework-native confinement closure is claimed.")
        sys.exit(0)


if __name__ == "__main__":
    main()
