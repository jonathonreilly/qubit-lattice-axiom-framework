#!/usr/bin/env python3
"""This runner reproduces supplied finite numerical fixtures and checks documentary
consistency. Its unchanged numerical predicates, grids and optimizer settings
are not a proof of global optimality, exact roots, physical selection or an
exhaustive remaining research burden. Text matches report text only. Historical
literal-True narrative is not counted as a mathematical PASS.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = ['archive_unlanded/dm-neutrino-stale-runners-2026-04-30/DM_NEUTRINO_WEAK_TRIPLET_COEFFICIENT_AXIOM_BOUNDARY_NOTE_2026-04-15.md', 'docs/DM_NEUTRINO_BREAKING_TRIPLET_CP_THEOREM_NOTE_2026-04-15.md', 'docs/DM_NEUTRINO_EXACT_H_SOURCE_SURFACE_PREIMAGE_BUNDLE_THEOREM_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_EXACT_H_SOURCE_SURFACE_THEOREM_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_POSITIVE_POLAR_H_CP_THEOREM_NOTE_2026-04-15.md', 'docs/DM_NEUTRINO_POSTCANONICAL_POLAR_SECTION_NOTE_2026-04-15.md', 'docs/DM_NEUTRINO_SOURCE_AMPLITUDE_THEOREM_NOTE_2026-04-15.md', 'docs/DM_NEUTRINO_SOURCE_BANK_Z3_DOUBLET_BLOCK_SELECTION_OBSTRUCTION_THEOREM_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_SOURCE_SURFACE_ACTIVE_AFFINE_POINT_SELECTION_BOUNDARY_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_SOURCE_SURFACE_ACTIVE_HALF_PLANE_THEOREM_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_SOURCE_SURFACE_ATOMIC_WITNESS_VOLUME_SELECTOR_NONREALIZATION_NOTE_2026-04-18.md', 'docs/DM_NEUTRINO_SOURCE_SURFACE_CARRIER_NORMAL_FORM_THEOREM_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_SOURCE_SURFACE_INTRINSIC_SLOT_THEOREM_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_SOURCE_SURFACE_SHIFT_QUOTIENT_BUNDLE_THEOREM_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_SOURCE_SURFACE_Z3_DOUBLET_BLOCK_POINT_SELECTION_THEOREM_NOTE_2026-04-16.md', 'docs/DM_SELECTOR_THRESHOLD_STABILIZATION_SUPPORT_THEOREM_NOTE_2026-04-21.md', 'docs/SCALAR_SELECTOR_REMAINING_OPEN_IMPORTS_2026-04-20.md', 'scripts/dm_leptogenesis_exact_common.py', 'scripts/dm_selector_branch_support.py', 'scripts/frontier_dm_leptogenesis_flavor_column_functional_theorem.py', 'scripts/frontier_dm_leptogenesis_ne_charged_source_response_reduction.py', 'scripts/frontier_dm_leptogenesis_pmns_projector_interface.py', 'scripts/frontier_dm_neutrino_breaking_triplet_cp_theorem.py', 'scripts/frontier_dm_neutrino_exact_h_source_surface_preimage_bundle_theorem.py', 'scripts/frontier_dm_neutrino_hermitian_bridge_carrier.py', 'scripts/frontier_dm_neutrino_positive_polar_h_cp_theorem.py', 'scripts/frontier_dm_neutrino_postcanonical_polar_section.py', 'scripts/frontier_dm_neutrino_source_bank_z3_doublet_block_selection_obstruction_theorem.py', 'scripts/frontier_dm_neutrino_source_surface_active_affine_point_selection_boundary.py', 'scripts/frontier_dm_neutrino_source_surface_active_half_plane_theorem.py', 'scripts/frontier_dm_neutrino_source_surface_atomic_witness_volume_selector_nonrealization.py', 'scripts/frontier_dm_neutrino_source_surface_carrier_normal_form.py', 'scripts/frontier_dm_neutrino_source_surface_intrinsic_slot_theorem.py', 'scripts/frontier_dm_neutrino_source_surface_shift_quotient_bundle_theorem.py', 'scripts/frontier_dm_neutrino_source_surface_z3_doublet_block_point_selection_theorem.py']

import math
import sys
from pathlib import Path

import numpy as np
from scipy.optimize import brentq

from dm_selector_branch_support import (
    ANCHOR_OFFSET,
    PREFERRED_RECOVERED_LIFT,
    common_shift,
    recovered_bank,
)
from frontier_dm_neutrino_source_surface_atomic_witness_volume_selector_nonrealization import (
    inverse_eigenvalue_parameters,
    witness_volume_from_atomic_field,
)

ROOT = Path(__file__).resolve().parents[1]

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


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def threshold_volume(params: tuple[float, float, float], tau: float) -> float:
    return witness_volume_from_atomic_field(params, float(tau))


def pairwise_diff(
    params_bank: list[tuple[float, float, float]], tau: float, idx: int, jdx: int
) -> float:
    return threshold_volume(params_bank[idx], tau) - threshold_volume(params_bank[jdx], tau)


def bisection_root(
    params_bank: list[tuple[float, float, float]],
    idx: int,
    jdx: int,
    lo: float,
    hi: float,
) -> float:
    def f(tau: float) -> float:
        return pairwise_diff(params_bank, tau, idx, jdx)

    flo = f(lo)
    fhi = f(hi)
    if flo == 0.0:
        return lo
    if fhi == 0.0:
        return hi
    if flo * fhi > 0.0:
        raise RuntimeError(f"failed to bracket root for pair ({idx},{jdx}) on [{lo},{hi}]")
    return float(brentq(f, lo, hi))


def part1_intrinsic_threshold_volume_data_are_exact() -> tuple[list[tuple[float, float, float]], float]:
    print("\n" + "=" * 88)
    print("PART 1: SUPPLIED THRESHOLD-VOLUME DATA")
    print("=" * 88)

    lifts, hs_bank, repairs_bank, _targets = recovered_bank()
    mu_bank = common_shift(repairs_bank, ANCHOR_OFFSET)
    params_bank = [inverse_eigenvalue_parameters(h, mu_bank) for h in hs_bank]

    note = read("docs/DM_NEUTRINO_SOURCE_SURFACE_ATOMIC_WITNESS_VOLUME_SELECTOR_NONREALIZATION_NOTE_2026-04-18.md")

    check(
        'The preferred recovered lift is the first recovered-bank point used throughout the selector packet',
        np.linalg.norm(np.asarray(lifts[0], dtype=float) - PREFERRED_RECOVERED_LIFT) < 1.0e-12,
        f"preferred lift = {np.round(lifts[0], 12)}",
    )
    check(
        'One common positive comparison window still exists on the full recovered bank',
        float(mu_bank) > float(np.max(repairs_bank)),
        f"mu_bank = {mu_bank:.12f}",
    )
    check('DOCUMENTARY text observation only: The nonrealization note already records the exact intrinsic threshold-volume family V_tau(H)', "V_tau(H)" in note and "piecewise-quadratic" in note and "intrinsic threshold law" in note)
    check(
        'The preferred recovered lift has the smallest terminal inverse eigenvalue a among the recovered bank',
        params_bank[0][0] == min(p[0] for p in params_bank),
        f"a values = {np.round([p[0] for p in params_bank], 12)}",
    )

    return params_bank, float(mu_bank)


def part2_pairwise_crossovers_isolate_one_last_stabilization_threshold(
    params_bank: list[tuple[float, float, float]]
) -> tuple[float, float]:
    print("\n" + "=" * 88)
    print("PART 2: PAIRWISE CROSSOVERS ISOLATE THE LAST STABILIZATION THRESHOLD")
    print("=" * 88)

    # Supplied brackets locate numerical crossover candidates only;
    # no exhaustive root isolation or uniqueness certificate is inferred.
    tau_roots = {
        4: bisection_root(params_bank, 0, 4, 0.12, 0.125),
        3: bisection_root(params_bank, 0, 3, 0.125, 0.13),
        2: bisection_root(params_bank, 0, 2, 0.13, 0.135),
        1: bisection_root(params_bank, 0, 1, 0.13, 0.135),
    }
    tau_star = max(tau_roots.values())
    tau_zero_0 = math.log1p(params_bank[0][0])
    tau_zero_next = min(math.log1p(params_bank[j][0]) for j in range(1, len(params_bank)))

    check(
        'The preferred lift crosses below lift 4 first, then lift 3, then lift 2, and last lift 1',
        tau_roots[4] < tau_roots[3] < tau_roots[2] < tau_roots[1],
        f"roots = {tau_roots}",
    )
    check(
        'The last pairwise crossover defines the high-threshold stabilization onset tau_star',
        abs(tau_star - tau_roots[1]) < 1.0e-14,
        f"tau_star = {tau_star:.15f}",
    )
    check(
        'The preferred lift reaches zero witness volume before every competing lift',
        tau_zero_0 < tau_zero_next,
        f"(tau_zero_0, tau_zero_next)=({tau_zero_0:.15f},{tau_zero_next:.15f})",
    )
    check(
        'So there is a nonempty open threshold window after tau_star and before the next zero-volume tie',
        tau_star < tau_zero_next,
        f"window = ({tau_star:.15f}, {tau_zero_next:.15f})",
    )

    print()
    print("  Pairwise high-threshold crossover values:")
    for jdx in (4, 3, 2, 1):
        print(f"    tau_0{jdx} = {tau_roots[jdx]:.15f}")
    print(f"  tau_star      = {tau_star:.15f}")
    print(f"  tau_zero(0)   = {tau_zero_0:.15f}")
    print(f"  tau_zero(next)= {tau_zero_next:.15f}")

    return tau_star, tau_zero_next


def part3_the_preferred_lift_is_unique_on_the_whole_stabilization_window(
    params_bank: list[tuple[float, float, float]], tau_star: float, tau_zero_next: float
) -> None:
    print("\n" + "=" * 88)
    print("PART 3: REPRESENTATIVE AND PIECEWISE-MIDPOINT COMPARISONS")
    print("=" * 88)

    tau_zero_0 = math.log1p(params_bank[0][0])
    tau_samples = [
        0.5 * (tau_star + tau_zero_0),
        0.5 * (tau_zero_0 + tau_zero_next),
    ]
    # Include a representative support threshold already in the packet.
    tau_samples.insert(0, 0.14)

    sample_ok = True
    details: list[str] = []
    for tau in tau_samples:
        vals = np.array([threshold_volume(p, tau) for p in params_bank], dtype=float)
        winner = int(np.argmin(vals))
        sample_ok &= winner == 0 and np.all(vals[0] + 1.0e-12 < vals[1:])
        details.append(f"tau={tau:.6f}: winner={winner}, vals={np.round(vals, 6)}")

    check(
        'Representative points from the stabilization window all choose the preferred recovered lift uniquely',
        sample_ok,
        " ; ".join(details),
    )

    post_zero_vals = np.array([threshold_volume(p, 0.5 * (tau_zero_0 + tau_zero_next)) for p in params_bank], dtype=float)
    check(
        'Finite supplied diagnostic: post-zero sampled comparison',
        abs(post_zero_vals[0]) < 1.0e-12 and np.all(post_zero_vals[1:] > 1.0e-6),
        f"post-zero volumes = {np.round(post_zero_vals, 12)}",
    )

    # Piecewise-break analysis on the open interval (tau_star, tau_zero_0):
    # the only formula changes come from the b-thresholds of the recovered lifts
    # and from tau_zero_0 itself.
    breakpoints = sorted(
        {
            tau_star,
            math.log1p(params_bank[0][1]),
            math.log1p(params_bank[4][1]),
            math.log1p(params_bank[3][1]),
            math.log1p(params_bank[1][1]),
            math.log1p(params_bank[2][1]),
            tau_zero_0,
        }
    )
    interval_checks = True
    interval_details: list[str] = []
    for left, right in zip(breakpoints[:-1], breakpoints[1:]):
        if right <= tau_star + 1.0e-12:
            continue
        mid = 0.5 * (left + right)
        vals = np.array([threshold_volume(p, mid) for p in params_bank], dtype=float)
        interval_checks &= np.all(vals[0] + 1.0e-12 < vals[1:])
        interval_details.append(f"({left:.6f},{right:.6f})->{np.round(vals, 6)}")

    check(
        'Finite supplied diagnostic: piecewise midpoint comparisons',
        interval_checks,
        " ; ".join(interval_details),
    )


def part4_the_remaining_selector_target_is_now_narrower() -> None:
    print("\n" + "=" * 88)
    print("PART 4: DOCUMENTARY BOUNDARY AND FINITE COMPARISONS")
    print("=" * 88)

    obstruction = read("docs/DM_NEUTRINO_SOURCE_SURFACE_ATOMIC_WITNESS_VOLUME_SELECTOR_NONREALIZATION_NOTE_2026-04-18.md")
    review = read("docs/SCALAR_SELECTOR_REMAINING_OPEN_IMPORTS_2026-04-20.md")

    check('DOCUMENTARY text observation only: The prior selector-side note already said the missing datum is an intrinsic threshold law', "intrinsic threshold law" in obstruction)
    check("DOCUMENTARY: summary reports physical selection obligations open and PMNS angles supplied", "selection obligations remain open" in " ".join(review.split()) and "PMNS angle triple is an input" in " ".join(review.split()))
    print("INFO: Historical selector-burden narration withdrawn; no mathematical check or exhaustive-route inference.")


def main() -> int:
    print("=" * 88)
    print("DM SELECTOR THRESHOLD STABILIZATION FINITE NUMERICAL SUPPORT")
    print("=" * 88)

    params_bank, _mu_bank = part1_intrinsic_threshold_volume_data_are_exact()
    tau_star, tau_zero_next = part2_pairwise_crossovers_isolate_one_last_stabilization_threshold(params_bank)
    part3_the_preferred_lift_is_unique_on_the_whole_stabilization_window(params_bank, tau_star, tau_zero_next)
    part4_the_remaining_selector_target_is_now_narrower()

    print("\n" + "=" * 88)
    print("RESULT: finite supplied computations and documentary observations only")
    print("No physical selector, exact optimizer/root certificate, exhaustive route or continuous-window theorem follows.")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")

    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
