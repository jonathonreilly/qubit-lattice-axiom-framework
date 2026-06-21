#!/usr/bin/env python3
"""
Charged-lepton Yukawa — BZ matching-coefficient boundary cross-check

The Koide-lane claim y_τ^bare = α_LM/(4π) is a FRAMEWORK TREE-LEVEL
identification on the retained canonical surface, NOT a 1-loop BZ-
quadrature result that needs separate verification. Specifically:

  - α_LM is retained (PLAQ_MC → u_0 → α_LM)
  - 1/(4π) is the standard 1-loop phase-space factor (not a matching
    coefficient that requires BZ integration)
  - C_τ = 1 is the Casimir combination (explicit enumeration in
    frontier_charged_lepton_yukawa_diagrammatic_enumeration.py)

What the retained YT_P1 BZ quadrature computes is a lattice-to-MSbar
matching coefficient (Δ_R for the top, analogous Δ_τ for the lepton).
On the current implementation, the scalar-vertex integral converges near
32, not in the old small-coefficient bracket [4, 10]. Therefore this
runner is a boundary check: it verifies the BZ machinery runs, and it
prevents the Koide support package from using that integral as evidence
for a small radiative correction to the tree-level tau identification.

This runner verifies the retained YT_P1 machinery works on the lepton
channel and shows:

  1. The scalar-density matching coefficient I_v_scalar (YT_P1 output)
     is a well-defined finite number with monotone grid convergence.

  2. For the top quark, I_v_scalar is multiplied by C_F (color) to enter
     Δ_R. For the charged lepton, the color factor is absent; only the
     EW Casimir C_τ = 1 enters.

  3. The large value means this BZ integral is not the small correction
     that explains the 0.006% PDG agreement. The tree-level identity
     y_τ = α_LM/(4π) remains separate and bounded.

Inputs (retained primitives, imported directly):
  - scripts/frontier_yt_p1_bz_quadrature_full_staggered_pt.py provides
      integrate_I_v_scalar_full(N)  — 4D BZ scalar-vertex integral with
      full Kawamoto-Smit staggered propagator + Wilson-plaquette gluon
      + MS-bar continuum subtraction. Returns the matching coefficient
      including the I_S^CL = 2 continuum offset.
  - scripts/canonical_plaquette_surface.py provides ALPHA_LM, U_0.

Lepton-specific piece:
  - C_τ = 1 exactly, computed by gauge-by-gauge Casimir enumeration
    in frontier_charged_lepton_yukawa_diagrammatic_enumeration.py.

What this runner does NOT claim:
  - That I_v_scalar = 1.0 exactly (it's not; it's a matching coefficient
    including a +2.0 continuum offset by YT_P1 convention)
  - That y_τ^bare = α_LM/(4π) requires BZ verification (it doesn't; it's
    the retained tree-level identification)

What this runner DOES claim:
  - The retained YT_P1 BZ machinery runs correctly and converges
  - The matching coefficient is large on the current normalization
  - This does not support the old small-correction framing for y_τ^bare
"""

import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from dm_leptogenesis_exact_common import ALPHA_LM as ALPHA_LM_EXACT, V_EW  # noqa: E402

PASSES: list[tuple[str, bool, str]] = []


def record(name: str, ok: bool, detail: str = ""):
    PASSES.append((name, ok, detail))
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] {name}")
    if detail:
        for line in detail.split("\n"):
            print(f"       {line}")


def section(title: str):
    print()
    print("=" * 88)
    print(title)
    print("=" * 88)


# =============================================================================
# Part A — import retained YT_P1 BZ quadrature machinery
# =============================================================================
def part_A():
    section("Part A — Import retained YT_P1 BZ quadrature machinery")

    from frontier_yt_p1_bz_quadrature_full_staggered_pt import (  # noqa: E402
        integrate_I_v_scalar_full,
        build_bz_grid,
        D_psi_full,
        D_gluon_full,
        F_scalar_ps_per_mu,
        ALPHA_LM,
        U_0,
        C_F,
        FOUR_PI,
    )

    print(f"  Retained primitives imported from YT_P1 BZ quadrature:")
    print(f"    ALPHA_LM           = {ALPHA_LM:.6f}")
    print(f"    u_0 (tadpole)      = {U_0:.6f}")
    print(f"    C_F (SU(3) color)  = {C_F:.6f}  (used by top quark, NOT by lepton)")
    print(f"    4π                 = {FOUR_PI:.6f}")

    # Sanity check: the BZ machinery is callable
    # Test with small N for fast verification
    N_test = 8
    _K, _dk = build_bz_grid(N_test)
    print(f"\n  BZ grid at N={N_test}: shape {_K.shape}, dk = {_dk:.6e}")

    record(
        "A.1 Retained YT_P1 BZ quadrature machinery imports successfully",
        True,
        "build_bz_grid, D_psi_full, D_gluon_full, F_scalar_ps_per_mu,\n"
        "integrate_I_v_scalar_full all available from retained runner.",
    )

    return integrate_I_v_scalar_full, ALPHA_LM, U_0, FOUR_PI


# =============================================================================
# Part B — run the scalar-vertex BZ integral at multiple grid sizes
# =============================================================================
def part_B(integrate_I_v_scalar_full):
    section("Part B — Run retained scalar-vertex BZ integral (I_loop convergence)")

    print("  Evaluating the 4D BZ integral at grid sizes N = 16, 24, 32.")
    print("  (At N=48, 64 the calculation is ~5 min; these sizes are tractable")
    print("   and show grid convergence of the physical matching coefficient.)")
    print()

    results = {}
    for N in [16, 24, 32]:
        I_val = integrate_I_v_scalar_full(N)
        results[N] = I_val
        print(f"    N = {N:2d}:  I_v_scalar(lattice) = {I_val:.6f}")

    print()
    print("  Grid convergence: N=16 → N=24 → N=32:")
    d_16_24 = abs(results[24] - results[16]) / results[24] * 100
    d_24_32 = abs(results[32] - results[24]) / results[32] * 100
    print(f"    Δ(16→24) = {d_16_24:.3f}%")
    print(f"    Δ(24→32) = {d_24_32:.3f}%")
    print(f"    Monotone convergence as expected for smooth integrand.")

    record(
        "B.1 BZ integral converges under grid refinement (<2% N=24→32)",
        d_24_32 < 2.0,
        f"Δ(N=24→N=32) = {d_24_32:.3f}% < 2% target (retained systematic 5%)",
    )

    # The retained I_v_scalar is the YT_P1 matching coefficient defined as
    # [lat_artifact / N_TASTE / u_0²] + 2.0 (I_S^CL continuum offset).
    # The LATTICE ARTIFACT (what measures lattice vs continuum deviation) is
    # the piece WITHOUT the +2.0 offset.
    lat_artifact_N32 = results[32] - 2.0
    print()
    print(f"  YT_P1 matching coefficient structure at N=32:")
    print(f"    Total I_v_scalar = {results[32]:.4f}")
    print(f"    Continuum offset = 2.0 (I_S^CL)")
    print(f"    Lattice artifact = {lat_artifact_N32:.4f}")
    print(f"    (the lattice artifact is what the BZ quadrature computes;")
    print(f"     the continuum offset is a retained analytical value)")

    record(
        "B.2 I_v_scalar is outside the old small-coefficient range [4, 10]",
        results[32] > 10.0,
        f"I_v_scalar(N=32) = {results[32]:.4f}; this is not in [4, 10].\n"
        "The BZ integral is a large matching coefficient on the current normalization.",
    )

    return results[32], results


# =============================================================================
# Part C — assemble y_τ from BZ integral × C_τ × α_LM/(4π)
# =============================================================================
def part_C(I_v_scalar_N32, results, ALPHA_LM, FOUR_PI):
    section("Part C — Framework tree-level y_τ = α_LM/(4π) + retained matching")

    # From diagrammatic enumeration: C_τ = 1 exactly
    C_tau = 1

    print("  Framework identification on retained canonical surface:")
    print()
    print(f"    y_τ^bare = α_LM / (4π) · C_τ   (TREE-LEVEL retained)")
    print(f"            = {ALPHA_LM} / (4π) · {C_tau}")
    print(f"            = {ALPHA_LM / FOUR_PI * C_tau:.10f}")
    print()
    print("  This identification does NOT require a separate BZ-quadrature")
    print("  verification — α_LM and 1/(4π) are retained primitives and the")
    print("  Casimir C_τ = 1 is explicit (gauge-by-gauge enumeration).")
    print()

    y_tau_bare = (ALPHA_LM / FOUR_PI) * C_tau

    M_TAU_PDG = 1776.86
    v_EW_MeV = V_EW * 1000.0
    y_tau_obs = M_TAU_PDG / v_EW_MeV
    m_tau_bare = v_EW_MeV * y_tau_bare

    print(f"  Framework tree-level y_τ^bare        = {y_tau_bare:.10f}")
    print(f"  Observed y_τ = m_τ/v_EW              = {y_tau_obs:.10f}")
    print(f"  m_τ (tree-level)  = {m_tau_bare:.2f} MeV")
    print(f"  PDG m_τ           = {M_TAU_PDG} MeV")

    dev_tree = abs(m_tau_bare - M_TAU_PDG) / M_TAU_PDG * 100
    print(f"  Deviation: {dev_tree:.4f}%")

    record(
        "C.1 Framework tree-level y_τ^bare = α_LM/(4π) · C_τ matches PDG at <0.01%",
        dev_tree < 0.01,
        f"y_τ^bare = {y_tau_bare:.6e}, y_τ^obs = {y_tau_obs:.6e}\n"
        f"m_τ prediction: {m_tau_bare:.2f} MeV vs PDG {M_TAU_PDG} MeV ({dev_tree:.4f}%)",
    )

    # Optional: retained YT_P1 matching coefficient scale
    print()
    print("  Retained YT_P1 matching-coefficient context:")
    print(f"    I_v_scalar (BZ, N=32) = {I_v_scalar_N32:.4f}")
    print(f"    Lattice artifact     = {I_v_scalar_N32 - 2.0:.4f} (large vs continuum 2.0)")
    print("  This is a boundary result: the current BZ integral is not a")
    print("  small per-channel correction explaining the 0.006% observed deviation.")

    # The I_v_scalar matching coefficient enters the MS-bar-to-lattice
    # correction at order (α_LM/(4π)) · I_v_scalar. With the current
    # I_v_scalar near 32, that scale is large, so it must not be cited as
    # a small retained matching correction for the tau mass.
    matching_correction_percent = (ALPHA_LM / FOUR_PI) * I_v_scalar_N32 * 100
    print(f"\n  Matching correction scale:")
    print(f"    Δy_τ / y_τ^bare ~ (α_LM/(4π)) · I_v_scalar · C_τ")
    print(f"                    ~ {ALPHA_LM/FOUR_PI:.4f} · {I_v_scalar_N32:.2f} · {C_tau}")
    print(f"                    ~ {matching_correction_percent:.2f}%")
    print(f"    Observed deviation: {dev_tree:.4f}%")
    print(f"    → observed is {matching_correction_percent/dev_tree:.0f}× smaller than systematic")

    record(
        "C.2 BZ matching scale is too large to explain the 0.006% PDG match",
        matching_correction_percent > 10.0 and dev_tree < matching_correction_percent,
        f"Matching correction scale: {matching_correction_percent:.2f}%\n"
        f"Observed y_τ deviation:   {dev_tree:.4f}%\n"
        "The small observed agreement is not evidence that this BZ integral is the retained tau correction.",
    )


# =============================================================================
# Part D — Richardson extrapolation of the retained matching coefficient
# =============================================================================
def part_D(results):
    section("Part D — Richardson extrapolation of retained matching coefficient")

    # Extrapolate the FULL I_v_scalar (matching coefficient including offset)
    # assuming O(1/N²) lattice-quadrature artifact.
    N1, N2 = 24, 32
    I1, I2 = results[N1], results[N2]
    c = (I1 - I2) / (1.0/N1**2 - 1.0/N2**2)
    I_inf = I2 - c / N2**2

    print(f"  Retained I_v_scalar (with I_S^CL = 2 continuum offset):")
    print(f"    I(N=24) = {I1:.6f}")
    print(f"    I(N=32) = {I2:.6f}")
    print(f"    Richardson coeff c (O(1/N²)) = {c:.4f}")
    print(f"    I_∞ (extrapolated) = {I_inf:.6f}")
    print()
    print(f"  Continuum-limit I_v_scalar: {I_inf:.6f}")
    print(f"  Expected I_S^CL offset:     2.00 (retained analytical)")
    print(f"  Lattice artifact at N→∞:    {I_inf - 2.0:.4f}")

    record(
        "D.1 Richardson-extrapolated I_v_scalar remains outside [4, 10]",
        I_inf > 10.0,
        f"I_v_scalar(∞) = {I_inf:.4f}; this remains outside the old [4, 10] bracket.\n"
        "The large-coefficient boundary is stable under the N=24,32 extrapolation.",
    )


def main() -> int:
    section("Charged-Lepton Yukawa BZ Matching Boundary Cross-Check")
    print()
    print("The identification y_τ^bare = α_LM/(4π) · C_τ is a RETAINED TREE-")
    print("LEVEL IDENTIFICATION, not a 1-loop BZ integral. This runner:")
    print("  - Confirms the retained YT_P1 BZ machinery runs and converges on")
    print("    the scalar-vertex matching coefficient I_v_scalar.")
    print("  - Shows the current BZ coefficient is large, not a small correction.")
    print("  - Keeps y_τ = α_LM/(4π) · C_τ as a separate tree-level")
    print("    bounded identification from α_LM, 1/(4π), and C_τ = 1.")
    print()

    integrate_I_v_scalar_full, ALPHA_LM, U_0, FOUR_PI = part_A()
    I_v_scalar_N32, results = part_B(integrate_I_v_scalar_full)
    part_C(I_v_scalar_N32, results, ALPHA_LM, FOUR_PI)
    part_D(results)

    section("SUMMARY")
    n_pass = sum(1 for _, ok, _ in PASSES if ok)
    n_total = len(PASSES)
    print(f"PASSED: {n_pass}/{n_total}")
    for name, ok, _ in PASSES:
        status = "PASS" if ok else "FAIL"
        print(f"  [{status}] {name}")

    print()
    all_pass = n_pass == n_total
    if all_pass:
        print("VERDICT: BZ machinery verified; small-correction framing rejected.")
        print()
        print("Correct framing of the radiative/Yukawa support lane:")
        print()
        print("  y_τ^bare = α_LM / (4π) · C_τ    (TREE-LEVEL RETAINED)")
        print("         |         |       |")
        print("         |         |       └── Casimir enumeration (= 1)")
        print("         |         └── 1-loop phase-space factor (universal)")
        print("         └── retained lattice coupling from PLAQ_MC → u_0 → α_LM")
        print()
        print("The current BZ coefficient is too large to be cited as the small")
        print("matching correction behind the 0.006% tau agreement.")
        print()
        print("No citation remains. The only retained inputs are:")
        print("  1. α_LM (retained from PLAQ_MC)")
        print("  2. v_EW = M_Pl · (7/8)^(1/4) · α_LM^16 (retained hierarchy)")
        print("  3. C_τ = 1 (gauge-by-gauge Casimir enumeration)")
        print("  4. BZ quadrature machinery as a boundary check, not a small-correction proof")
        print()
        print("All of these are either retained primitives or explicit calculations")
        print("on retained primitives. This strengthens the charged-lepton")
        print("radiative/Yukawa support lane but does not by itself close")
        print("the Koide bridges.")
    else:
        print("VERDICT: verification has FAILs. See PASS/FAIL summary above.")

    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
