#!/usr/bin/env python3
"""Supplied PMNS line: finite-difference search trace and point comparisons.
The grids locate numerical candidates only. No exhaustive roots, global
minimum, all-line exclusion or physical/nonlocal selection is established.
Historical no-go source and output are preserved in the PR9844 archive.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ('docs/DM_PMNS_SUPPLIED_LINE_FINITE_SEARCH_DIAGNOSTIC_NOTE_2026-04-20.md', 'scripts/dm_leptogenesis_exact_common.py', 'scripts/frontier_dm_leptogenesis_flavor_column_functional_theorem.py', 'scripts/frontier_dm_leptogenesis_pmns_active_projector_reduction.py', 'scripts/frontier_dm_leptogenesis_pmns_projector_interface.py', 'scripts/frontier_dm_neutrino_breaking_triplet_cp_theorem.py', 'scripts/frontier_dm_neutrino_exact_h_source_surface_preimage_bundle_theorem.py', 'scripts/frontier_dm_neutrino_hermitian_bridge_carrier.py', 'scripts/frontier_dm_neutrino_positive_polar_h_cp_theorem.py', 'scripts/frontier_dm_neutrino_postcanonical_polar_section.py', 'scripts/frontier_dm_neutrino_source_surface_active_affine_point_selection_boundary.py', 'scripts/frontier_dm_neutrino_source_surface_active_curvature_23_symmetric_baseline_boundary.py', 'scripts/frontier_dm_neutrino_source_surface_active_half_plane_theorem.py', 'scripts/frontier_dm_neutrino_source_surface_carrier_normal_form.py', 'scripts/frontier_dm_neutrino_source_surface_intrinsic_slot_theorem.py', 'scripts/frontier_dm_neutrino_source_surface_parity_compatible_observable_selector_theorem.py', 'scripts/frontier_dm_neutrino_source_surface_shift_quotient_bundle_theorem.py', 'scripts/frontier_dm_neutrino_source_surface_z3_doublet_block_point_selection_theorem.py', 'scripts/frontier_pmns_from_dm_neutrino_source_h_diagonalization_closure_theorem.py')

import math
from pathlib import Path

import numpy as np
from scipy.optimize import brentq

from frontier_dm_neutrino_source_surface_active_curvature_23_symmetric_baseline_boundary import (
    delta_star as curvature_delta_star,
    q_star as curvature_q_star,
)
from frontier_dm_neutrino_source_surface_parity_compatible_observable_selector_theorem import (
    delta_star as parity_delta_star,
    q_star as parity_q_star,
)
from frontier_pmns_from_dm_neutrino_source_h_diagonalization_closure_theorem import (
    TARGET_S12SQ,
    TARGET_S13SQ,
    TARGET_S23SQ,
    pmns_observables,
)


ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs/DM_PMNS_SUPPLIED_LINE_FINITE_SEARCH_DIAGNOSTIC_NOTE_2026-04-20.md"

PASS_COUNT = 0
FAIL_COUNT = 0

SCHUR_S = math.sqrt(6.0) / 3.0
TARGET = np.array([TARGET_S12SQ, TARGET_S13SQ, TARGET_S23SQ], dtype=float)

CANDIDATES = {
    "A Schur-Q": (0.5, SCHUR_S, SCHUR_S),
    "B det-crit": (0.613, 0.964, 1.552),
    "C Tr(H^2)-bdy": (0.385, 1.268, 0.365),
    "D K12 char": (0.0, 0.800, 1.000),
    "E par-mix F1": (
        4.0 * math.sqrt(2.0) / 9.0,
        math.sqrt(6.0) / 2.0 - math.sqrt(2.0) / 18.0,
        math.sqrt(6.0) / 6.0 + math.sqrt(2.0) / 18.0,
    ),
}


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


def read_note() -> str:
    return NOTE_PATH.read_text(encoding="utf-8")


def schur_obs(m: float) -> dict[str, float]:
    return pmns_observables(float(m), SCHUR_S, SCHUR_S)


def schur_vector(m: float) -> np.ndarray:
    obs = schur_obs(m)
    return np.array([obs["s12sq"], obs["s13sq"], obs["s23sq"]], dtype=float)


def s12_on_schur(m: float) -> float:
    return float(schur_obs(m)["s12sq"])


def chi2_on_schur(m: float) -> float:
    vec = schur_vector(m)
    return float(np.sum((vec - TARGET) ** 2))


def central_diff(fn, x: float, h: float) -> float:
    return float((fn(x + h) - fn(x - h)) / (2.0 * h))


def find_stationary_points(fn, lo: float, hi: float, *, h: float, num: int) -> list[float]:
    grid = np.linspace(lo, hi, num)
    deriv = [central_diff(fn, float(x), h) for x in grid]
    roots: list[float] = []
    for a, b, fa, fb in zip(grid[:-1], grid[1:], deriv[:-1], deriv[1:]):
        if fa == 0.0 or fb == 0.0 or fa * fb < 0.0:
            try:
                root = float(brentq(lambda x: central_diff(fn, x, h), float(a), float(b), maxiter=200))
            except ValueError:
                continue
            if all(abs(root - old) > 1.0e-3 for old in roots):
                roots.append(root)
    return roots


def part1_local_families_reduce_to_the_same_selected_line() -> None:
    print("\n" + "=" * 88)
    print("PART 1: IMPORTED FUNCTIONS RETURN THE SUPPLIED LINE CONSTANTS")
    print("=" * 88)

    note = read_note()
    d_parity = parity_delta_star()
    q_parity = parity_q_star()
    d_curv = curvature_delta_star()
    q_curv = curvature_q_star()

    check(
        "Imported parity functions return supplied sqrt(6)/3 coordinates",
        abs(d_parity - SCHUR_S) < 1.0e-12 and abs(q_parity - SCHUR_S) < 1.0e-12,
        f"(delta_*,q_+*)=({d_parity:.12f},{q_parity:.12f})",
    )
    check(
        "Imported curvature functions return the same supplied coordinates",
        abs(d_curv - SCHUR_S) < 1.0e-12 and abs(q_curv - SCHUR_S) < 1.0e-12,
        f"(delta_*,q_+*)=({d_curv:.12f},{q_curv:.12f})",
    )
    check(
        "The two imported function pairs numerically agree",
        abs(d_parity - d_curv) < 1.0e-12 and abs(q_parity - q_curv) < 1.0e-12,
    )
    check(
        "The note records the supplied line and finite search",
        "delta = q_+ = sqrt(6)/3" in note and "finite search trace" in note,
    )


def part2_schur_line_has_a_hard_solar_angle_floor() -> None:
    print("\n" + "=" * 88)
    print("PART 2: LOCATED SOLAR-COORDINATE CANDIDATES AND ENDPOINT VALUES")
    print("=" * 88)

    roots = find_stationary_points(s12_on_schur, -2000.0, 2000.0, h=1.0e-4, num=4001)
    values = [(root, s12_on_schur(root)) for root in roots]
    values.sort(key=lambda item: item[1])
    min_root, min_value = values[0]
    max_root, max_value = values[-1]
    left_value = s12_on_schur(-2000.0)
    right_value = s12_on_schur(2000.0)

    print(f" located finite-difference zeros of s12^2(m, S, S) on [-2000,2000]: {roots}")
    print(f" lowest located-candidate value: m = {min_root:.12f}, s12^2 = {min_value:.12f}")
    print(f" highest located-candidate value: m = {max_root:.12f}, s12^2 = {max_value:.12f}")
    print(f" endpoint values: s12^2(-2000) = {left_value:.12f}, s12^2(2000) = {right_value:.12f}")

    check(
        "This finite-difference bracketing procedure returns two candidates",
        len(roots) == 2,
        f"roots={roots}",
    )
    check(
        "Located candidate near m=4.365 has value below the two evaluated endpoints",
        abs(min_root - 4.365005345285525) < 1.0e-6
        and min_value < left_value
        and min_value < right_value,
        f"m_min={min_root:.12f}, s12^2_min={min_value:.12f}",
    )
    check(
        "Evaluated lower located-candidate solar value exceeds supplied target by 0.02",
        min_value > TARGET_S12SQ + 2.0e-2,
        f"s12^2_min - 0.307 = {min_value - TARGET_S12SQ:.12f}",
    )
    check(
        "Evaluated lower located-candidate solar value exceeds supplied target",
        min_value > TARGET_S12SQ,
        f"s12^2_min={min_value:.12f}",
    )


def part3_best_full_three_angle_fit_on_the_schur_line_still_misses() -> None:
    print("\n" + "=" * 88)
    print("PART 3: LOCATED UNWEIGHTED SQUARED-RESIDUAL CANDIDATE")
    print("=" * 88)

    roots = find_stationary_points(chi2_on_schur, -200.0, 200.0, h=1.0e-4, num=8001)
    best_root = roots[0]
    best_chi2 = chi2_on_schur(best_root)
    best_vec = schur_vector(best_root)
    left = chi2_on_schur(-200.0)
    right = chi2_on_schur(200.0)

    print(f" located finite-difference zeros of chi^2_line on [-200,200]: {roots}")
    print(f" located residual candidate: m = {best_root:.12f}")
    print(f" best chi^2 = {best_chi2:.12f}")
    print(
        " candidate triple = "
        f"({best_vec[0]:.12f}, {best_vec[1]:.12f}, {best_vec[2]:.12f})"
    )
    print(f" endpoint chi^2 values: chi^2(-200) = {left:.12f}, chi^2(200) = {right:.12f}")

    check(
        "This residual bracketing procedure returns one numerical candidate",
        len(roots) == 1,
        f"roots={roots}",
    )
    check(
        "The located residual candidate is near m ~= 1.27832212",
        abs(best_root - 1.278322119585464) < 1.0e-6,
        f"m_best={best_root:.12f}",
    )
    check(
        "Located residual exceeds 0.01 and is below evaluated endpoint residuals",
        best_chi2 > 1.0e-2 and best_chi2 < left and best_chi2 < right,
        f"chi^2_min={best_chi2:.12f}",
    )


def part4_all_current_explicit_candidate_points_miss() -> None:
    print("\n" + "=" * 88)
    print("PART 4: FIVE SUPPLIED POINT COMPARISONS")
    print("=" * 88)

    rows: list[tuple[str, float, float]] = []
    for label, point in CANDIDATES.items():
        obs = pmns_observables(*point)
        vec = np.array([obs["s12sq"], obs["s13sq"], obs["s23sq"]], dtype=float)
        diff = vec - TARGET
        chi2 = float(np.sum(diff**2))
        max_err = float(np.max(np.abs(diff)))
        rows.append((label, chi2, max_err))
        print(
            f" {label:15s} chi^2 = {chi2:.12f}  "
            f"max|angle error| = {max_err:.12f}"
        )

    check(
        "Each of the five supplied points has evaluated maximum angle error > 0.05",
        all(max_err > 5.0e-2 for _, _, max_err in rows),
        f"rows={rows}",
    )
    check(
        "Each of the five supplied points has evaluated squared residual > 0.03",
        all(chi2 > 3.0e-2 for _, chi2, _ in rows),
        f"rows={rows}",
    )


def part5_the_note_states_the_correct_i5_consequence() -> None:
    print("\n" + "=" * 88)
    print("PART 5: DOCUMENTARY EVIDENCE BOUNDARY")
    print("=" * 88)

    note = read_note()
    check(
        "The note records the evaluated solar coordinate and supplied target",
        "0.331582718643" in note and "0.307" in note,
    )
    check(
        "The note records finite-search scope and open positive status",
        "finite search trace" in note
        and "I5 is still open positively" in note,
    )


def part6_n5_execution_certificate() -> None:
    print("EXECUTION SCOPE: finite grid and numerical finite-difference brackets.")
    print("Per point: five supplied triples and the located candidates are printed.")
    print("Coordinates: three mixing-angle readouts, not a physical mode decomposition.")
    print("Imported constants do not certify the underlying selector premises.")
    print("No site, lattice, interval-bound or exact-root completeness certificate.")


def main() -> int:
    print("=" * 88)
    print("DM PMNS SUPPLIED-LINE FINITE SEARCH DIAGNOSTIC")
    print("=" * 88)
    print()
    print("Question:")
    print("  What numerical candidates and residuals are returned by the supplied")
    print("  finite grid/bracketing procedure and five supplied point evaluations?")

    part1_local_families_reduce_to_the_same_selected_line()
    part2_schur_line_has_a_hard_solar_angle_floor()
    part3_best_full_three_angle_fit_on_the_schur_line_still_misses()
    part4_all_current_explicit_candidate_points_miss()
    part5_the_note_states_the_correct_i5_consequence()
    part6_n5_execution_certificate()

    print("\n" + "=" * 88)
    print("RESULT")
    print("=" * 88)
    print("Finite numerical trace only; all reported values belong to evaluated points.")
    print("No global minimum, exhaustive root set, physical selector or necessity claim.")
    print()
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
