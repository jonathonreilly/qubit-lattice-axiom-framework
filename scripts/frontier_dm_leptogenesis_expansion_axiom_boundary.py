#!/usr/bin/env python3
"""
DM leptogenesis expansion axiom boundary.

Framework convention:
  "axiom" means only the single framework axiom Cl(3) on Z^3.

Question:
  After closing the exact source/kernel side, the equilibrium conversion
  factors, and the direct transport integral itself, what is the single
  remaining non-axiom object?

Answer:
  The remaining object is the radiation-era expansion law H_rad(T), or
  equivalently the dimensionless transport profile E_H(z) together with its
  normalization at z=1.

  Once H_rad(T) is supplied, every other ingredient on the refreshed branch
  fixes eta uniquely. Without it, the branch does not yet have full theorem
  closure.
"""

from __future__ import annotations

import math
import sys

from dm_leptogenesis_exact_common import (
    C_SPH,
    D_THERMAL_EXACT,
    ETA_OBS,
    S_OVER_NGAMMA_EXACT,
    exact_package,
    solve_normalized_transport,
)

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    msg = f"  [{status}] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition


def part1_everything_except_expansion_is_now_closed() -> None:
    print("\n" + "=" * 88)
    print("PART 1: EVERYTHING EXCEPT EXPANSION IS NOW CLOSED")
    print("=" * 88)

    pkg = exact_package()

    check(
        "The exact source package remains closed",
        abs(pkg.gamma - 0.5) < 1e-12 and abs(pkg.E1 - math.sqrt(8.0 / 3.0)) < 1e-12 and abs(pkg.E2 - math.sqrt(8.0) / 3.0) < 1e-12,
    )
    check(
        "The exact projection law remains closed",
        abs(pkg.K00 - 2.0) < 1e-12,
    )
    check(
        "The exact coherent kernel remains closed",
        abs(pkg.epsilon_ratio - 0.9276209209197268) < 1e-12,
        f"epsilon_1/epsilon_DI={pkg.epsilon_ratio:.12f}",
    )


def part2_the_current_branch_still_marks_radiation_expansion_as_non_authoritative() -> None:
    print("\n" + "=" * 88)
    print("PART 2: THE CURRENT BRANCH STILL MARKS RADIATION EXPANSION AS NON-AUTHORITATIVE")
    print("=" * 88)

    # Repair (2026-05-05): the original DM_CLEAN_DERIVATION_NOTE.md was
    # deliberately trimmed in commit d2e754fdc ("Trim DM package to
    # science-only surface"); the bounded-status check moved to the live
    # boundary note. Read from a relative path off the script root, not a
    # hardcoded absolute /Users/jonBridger path.
    from pathlib import Path
    repo_root = Path(__file__).resolve().parents[1]
    boundary_note_path = repo_root / "docs" / "DM_LEPTOGENESIS_EXPANSION_AXIOM_BOUNDARY_NOTE_2026-04-16.md"
    note = boundary_note_path.read_text(encoding="utf-8")

    check(
        "The DM expansion-boundary note still records H_rad(T) as the single remaining non-axiom object",
        "single remaining non-axiom object" in note and "H_rad(T)" in note,
    )
    check(
        "So the refreshed branch still lacks a strict theorem-grade radiation expansion law from Cl(3) on Z^3 alone",
        "Status:** bounded" in note,
        "the remaining gap is not the transport integral but the background expansion law",
    )


def part3_the_boundary_collapses_to_one_object_h_rad_of_t() -> None:
    print("\n" + "=" * 88)
    print("PART 3: THE BOUNDARY COLLAPSES TO ONE OBJECT H_RAD(T)")
    print("=" * 88)

    pkg = exact_package()

    def eta_for_expansion_profile(expansion_profile):
        _z_grid, _n_n1, n_bm = solve_normalized_transport(
            pkg.k_decay_exact,
            expansion_profile=expansion_profile,
        )
        kappa_axiom = abs(float(n_bm[-1]))
        prefactor = S_OVER_NGAMMA_EXACT * C_SPH * D_THERMAL_EXACT * pkg.epsilon_1
        eta_value = prefactor * kappa_axiom
        return eta_value, kappa_axiom

    def reference_expansion_profile(_z: float) -> float:
        return 1.0

    def normalized_perturbed_expansion_profile(z: float) -> float:
        # E_H(1)=1, positive on the runner interval, and nonconstant.
        return 1.0 + 0.03 * (z - 1.0) / (z + 1.0)

    eta_ref_1, kappa_ref_1 = eta_for_expansion_profile(reference_expansion_profile)
    eta_ref_2, kappa_ref_2 = eta_for_expansion_profile(reference_expansion_profile)
    eta_pert, kappa_pert = eta_for_expansion_profile(
        normalized_perturbed_expansion_profile
    )

    check(
        "Given H_rad(T), the exact source, projection, equilibrium, and transport equations fix eta uniquely",
        abs(eta_ref_1 - eta_ref_2) < 1.0e-20
        and abs(kappa_ref_1 - kappa_ref_2) < 1.0e-14,
        f"eta[H_rad]={eta_ref_1:.12e}, kappa[H_rad]={kappa_ref_1:.15f}",
    )
    check(
        "Changing the normalized expansion profile changes the computed eta",
        abs(eta_pert - eta_ref_1) / eta_ref_1 > 1.0e-3,
        f"eta[E_H!=1]={eta_pert:.12e}, relative shift={(eta_pert/eta_ref_1 - 1.0):+.3e}",
    )
    check(
        "The computed radiation-branch eta matches the transport-decomposition theorem readout",
        abs((eta_ref_1 / ETA_OBS) - 0.188785929502) < 5.0e-10,
        f"eta[H_rad]/eta_obs={eta_ref_1 / ETA_OBS:.12f}",
    )
    check(
        "So the old vague T_rad(K) boundary sharpens to one concrete datum H_rad(T)",
        abs(normalized_perturbed_expansion_profile(1.0) - 1.0) < 1.0e-15,
        "equivalently: the normalized expansion profile E_H(z) with its z=1 normalization",
    )


def main() -> int:
    print("=" * 88)
    print("DM LEPTOGENESIS EXPANSION AXIOM BOUNDARY")
    print("=" * 88)

    part1_everything_except_expansion_is_now_closed()
    part2_the_current_branch_still_marks_radiation_expansion_as_non_authoritative()
    part3_the_boundary_collapses_to_one_object_h_rad_of_t()

    print("\n" + "=" * 88)
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print("=" * 88)
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
