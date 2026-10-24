#!/usr/bin/env python3
"""Finite seeded center-law search on the supplied five-coordinate seed chart.
Numerical residuals, distinct representatives and finite-difference ranks are
sampled diagnostics. They do not certify exact roots, neighborhood rank,
a local manifold dimension, global solution counts or a physical no-go.
The PMNS target and positive source sign are supplied conditions.
No approval or numerical premise is imported from held PR9844."""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = ('docs/DM_LEPTOGENESIS_NE_PROJECTED_SOURCE_TRIPLET_SIGN_THEOREM_NOTE_2026-04-16.md', 'docs/DM_LEPTOGENESIS_PMNS_ACTIVE_PROJECTOR_REDUCTION_NOTE_2026-04-16.md', 'docs/DM_LEPTOGENESIS_PMNS_CONSTRUCTIVE_CONTINUITY_CLOSURE_THEOREM_NOTE_2026-04-17.md', 'docs/DM_LEPTOGENESIS_PMNS_CONSTRUCTIVE_PROJECTED_SOURCE_SELECTOR_THEOREM_NOTE_2026-04-16.md', 'docs/DM_LEPTOGENESIS_PMNS_CP_BRIDGE_BOUNDARY_NOTE_2026-04-16.md', 'docs/DM_LEPTOGENESIS_PMNS_OBSERVABLE_RELATIVE_ACTION_LAW_NOTE_2026-04-16.md', 'docs/DM_LEPTOGENESIS_PMNS_PROJECTOR_INTERFACE_NOTE_2026-04-16.md', 'docs/DM_LEPTOGENESIS_PMNS_REDUCED_SURFACE_SELECTOR_SUPPORT_NOTE_2026-04-16.md', 'docs/DM_LEPTOGENESIS_PMNS_RELATIVE_ACTION_STATIONARITY_THEOREM_NOTE_2026-04-16.md', 'docs/DM_LEPTOGENESIS_PMNS_TRANSPORT_EXTREMAL_SOURCE_CANDIDATE_NOTE_2026-04-16.md', 'docs/DM_LEPTOGENESIS_PMNS_TRANSPORT_SELECTOR_FIREWALL_NOTE_2026-06-17.md', 'docs/DM_NEUTRINO_BREAKING_TRIPLET_CP_THEOREM_NOTE_2026-04-15.md', 'docs/DM_NEUTRINO_EXACT_H_SOURCE_SURFACE_PREIMAGE_BUNDLE_THEOREM_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_EXACT_H_SOURCE_SURFACE_THEOREM_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_POSITIVE_POLAR_H_CP_THEOREM_NOTE_2026-04-15.md', 'docs/DM_NEUTRINO_POSTCANONICAL_POLAR_SECTION_NOTE_2026-04-15.md', 'docs/DM_NEUTRINO_SOURCE_AMPLITUDE_THEOREM_NOTE_2026-04-15.md', 'docs/DM_NEUTRINO_SOURCE_BANK_Z3_DOUBLET_BLOCK_SELECTION_OBSTRUCTION_THEOREM_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_SOURCE_SURFACE_ACTIVE_AFFINE_POINT_SELECTION_BOUNDARY_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_SOURCE_SURFACE_ACTIVE_HALF_PLANE_THEOREM_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_SOURCE_SURFACE_CARRIER_NORMAL_FORM_THEOREM_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_SOURCE_SURFACE_INTRINSIC_SLOT_THEOREM_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_SOURCE_SURFACE_SHIFT_QUOTIENT_BUNDLE_THEOREM_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_SOURCE_SURFACE_Z3_DOUBLET_BLOCK_POINT_SELECTION_THEOREM_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_WEAK_TRIPLET_COEFFICIENT_AXIOM_BOUNDARY_NOTE_2026-04-15.md', 'docs/DM_PMNS_NE_SEED_SURFACE_EXACT_SOURCE_MANIFOLD_THEOREM_NOTE_2026-04-20.md', 'docs/DM_PMNS_Z3_DOUBLET_BLOCK_CENTER_POSITIVE_SHEET_NO_GO_THEOREM_NOTE_2026-04-20.md', 'scripts/dm_leptogenesis_exact_common.py', 'scripts/frontier_dm_leptogenesis_flavor_column_functional_theorem.py', 'scripts/frontier_dm_leptogenesis_full_microscopic_reduction.py', 'scripts/frontier_dm_leptogenesis_ne_projected_source_law_derivation.py', 'scripts/frontier_dm_leptogenesis_ne_projected_source_triplet_sign_theorem.py', 'scripts/frontier_dm_leptogenesis_pmns_active_projector_reduction.py', 'scripts/frontier_dm_leptogenesis_pmns_constructive_continuity_closure_theorem.py', 'scripts/frontier_dm_leptogenesis_pmns_constructive_projected_source_selector_theorem.py', 'scripts/frontier_dm_leptogenesis_pmns_cp_bridge_boundary.py', 'scripts/frontier_dm_leptogenesis_pmns_observable_relative_action_law.py', 'scripts/frontier_dm_leptogenesis_pmns_projector_interface.py', 'scripts/frontier_dm_leptogenesis_pmns_reduced_surface_selector_support.py', 'scripts/frontier_dm_leptogenesis_pmns_relative_action_stationarity_theorem.py', 'scripts/frontier_dm_leptogenesis_pmns_transport_extremal_source_candidate.py', 'scripts/frontier_dm_neutrino_breaking_triplet_cp_theorem.py', 'scripts/frontier_dm_neutrino_exact_h_source_surface_preimage_bundle_theorem.py', 'scripts/frontier_dm_neutrino_hermitian_bridge_carrier.py', 'scripts/frontier_dm_neutrino_positive_polar_h_cp_theorem.py', 'scripts/frontier_dm_neutrino_postcanonical_polar_section.py', 'scripts/frontier_dm_neutrino_source_bank_z3_doublet_block_selection_obstruction_theorem.py', 'scripts/frontier_dm_neutrino_source_surface_active_affine_point_selection_boundary.py', 'scripts/frontier_dm_neutrino_source_surface_active_half_plane_theorem.py', 'scripts/frontier_dm_neutrino_source_surface_carrier_normal_form.py', 'scripts/frontier_dm_neutrino_source_surface_intrinsic_slot_theorem.py', 'scripts/frontier_dm_neutrino_source_surface_shift_quotient_bundle_theorem.py', 'scripts/frontier_dm_neutrino_source_surface_z3_doublet_block_point_selection_theorem.py', 'scripts/frontier_dm_pmns_ne_seed_surface_exact_source_manifold_theorem_2026_04_20.py')


import math
import sys
from pathlib import Path

import numpy as np
from scipy.optimize import least_squares

from frontier_dm_pmns_ne_seed_surface_exact_source_manifold_theorem_2026_04_20 import (
    CHART_HI,
    CHART_LO,
    SEED_CHART_STARTS,
    TARGET,
    chart_to_obs,
)
from frontier_dm_neutrino_source_bank_z3_doublet_block_selection_obstruction_theorem import (
    active_target_from_h,
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


def center_features(chart: np.ndarray) -> tuple[np.ndarray, float, float, float]:
    obs, _x, _y, _delta_src, h = chart_to_obs(np.asarray(chart, dtype=float))
    delta_db, q_plus = active_target_from_h(h)
    source_cubic = float(np.imag(h[0, 1] * h[1, 2] * h[2, 0]))
    return obs, float(delta_db), float(q_plus), source_cubic


def center_residual(chart: np.ndarray) -> np.ndarray:
    _obs, delta_db, q_plus, _cubic = center_features(chart)
    return np.array([delta_db - 1.0, q_plus], dtype=float)


def center_target_residual(chart: np.ndarray) -> np.ndarray:
    obs, delta_db, q_plus, _cubic = center_features(chart)
    return np.concatenate([obs - TARGET, np.array([delta_db - 1.0, q_plus], dtype=float)])


def finite_jacobian(fun, chart: np.ndarray, eps: float = 1.0e-6) -> np.ndarray:
    chart = np.asarray(chart, dtype=float)
    f0 = np.asarray(fun(chart), dtype=float)
    jac = np.zeros((len(f0), len(chart)), dtype=float)
    for idx in range(len(chart)):
        step = np.zeros_like(chart)
        step[idx] = eps
        jac[:, idx] = (fun(chart + step) - fun(chart - step)) / (2.0 * eps)
    return jac


def collect_positive_center_points() -> list[dict[str, np.ndarray | float | int]]:
    rng = np.random.default_rng(7)
    starts = list(SEED_CHART_STARTS)
    for _ in range(18):
        starts.append(CHART_LO + (CHART_HI - CHART_LO) * rng.random(5))

    reps: list[dict[str, np.ndarray | float | int]] = []
    for start in starts:
        result = least_squares(
            center_residual,
            np.asarray(start, dtype=float),
            bounds=(CHART_LO, CHART_HI),
            xtol=1.0e-12,
            ftol=1.0e-12,
            gtol=1.0e-12,
            max_nfev=3000,
        )
        obs, delta_db, q_plus, source_cubic = center_features(result.x)
        if np.linalg.norm([delta_db - 1.0, q_plus]) > 1.0e-8 or source_cubic <= 0.0:
            continue
        chart = np.asarray(result.x, dtype=float)
        if all(np.linalg.norm(chart - rep["chart"]) > 1.0e-3 for rep in reps):
            jac = finite_jacobian(center_residual, chart)
            reps.append(
                {
                    "chart": chart,
                    "obs": obs,
                    "delta_db": delta_db,
                    "q_plus": q_plus,
                    "source_cubic": source_cubic,
                    "rank": int(np.linalg.matrix_rank(jac, tol=1.0e-5)),
                }
            )
    return reps


def collect_conditional_center_pairs() -> list[dict[str, np.ndarray | float]]:
    rng = np.random.default_rng(5)
    starts = list(SEED_CHART_STARTS)
    for _ in range(10):
        starts.append(CHART_LO + (CHART_HI - CHART_LO) * rng.random(5))

    reps: list[dict[str, np.ndarray | float]] = []
    for start in starts:
        result = least_squares(
            center_target_residual,
            np.asarray(start, dtype=float),
            bounds=(CHART_LO, CHART_HI),
            xtol=1.0e-11,
            ftol=1.0e-11,
            gtol=1.0e-11,
            max_nfev=4000,
        )
        if float(np.linalg.norm(center_target_residual(result.x))) > 1.0e-8:
            continue
        obs, _delta_db, _q_plus, source_cubic = center_features(result.x)
        _obs2, x, y, delta_src, _h = chart_to_obs(result.x)
        item = np.concatenate([x, y, [delta_src]])
        if all(np.linalg.norm(item - rep["item"]) > 1.0e-4 for rep in reps):
            reps.append(
                {
                    "item": item,
                    "obs": obs,
                    "x": x,
                    "y": y,
                    "delta_src": float(delta_src),
                    "source_cubic": source_cubic,
                }
            )
    return reps


def part1_positive_sheet_center_locus_is_not_a_point_selector() -> list[dict[str, np.ndarray | float | int]]:
    print("\n" + "=" * 88)
    print("PART 1: FINITE POSITIVE-SHEET CENTER SEARCH")
    print("=" * 88)

    reps = collect_positive_center_points()
    obs = np.array([rep["obs"] for rep in reps], dtype=float)

    check(
        "The seeded search finds at least eight separated numerical representatives",
        len(reps) >= 8,
        f"count={len(reps)}",
    )
    check(
        "Every sampled representative has componentwise center residual below 1e-10",
        all(abs(float(rep["delta_db"]) - 1.0) < 1.0e-10 and abs(float(rep["q_plus"])) < 1.0e-10 for rep in reps),
    )
    check(
        "Every sampled representative has computed I_src > 0",
        all(float(rep["source_cubic"]) > 0.0 for rep in reps),
        f"cubic values={[round(float(rep['source_cubic']), 9) for rep in reps[:6]]}",
    )
    check(
        "Sampled angle ranges exceed the stated finite spread thresholds",
        float(obs[:, 0].max() - obs[:, 0].min()) > 0.5
        and float(obs[:, 1].max() - obs[:, 1].min()) > 0.4
        and float(obs[:, 2].max() - obs[:, 2].min()) > 0.8,
        (
            f"ranges="
            f"({obs[:,0].min():.6f},{obs[:,0].max():.6f}) × "
            f"({obs[:,1].min():.6f},{obs[:,1].max():.6f}) × "
            f"({obs[:,2].min():.6f},{obs[:,2].max():.6f})"
        ),
    )

    for idx, rep in enumerate(reps[:4], start=1):
        print(f"  rep {idx}: obs={np.round(rep['obs'], 6)}, I_src={float(rep['source_cubic']):.9f}")

    return reps


def part2_center_constraints_have_rank_two_on_the_verified_patch(
    reps: list[dict[str, np.ndarray | float | int]]
) -> None:
    print("\n" + "=" * 88)
    print("PART 2: FINITE-DIFFERENCE RANK DIAGNOSTICS AT SAMPLED POINTS")
    print("=" * 88)

    ranks = [int(rep["rank"]) for rep in reps[:8]]
    check(
        "The first eight finite-difference Jacobians have numerical rank 2 at tolerance 1e-5",
        all(rank == 2 for rank in ranks),
        f"ranks={ranks}",
    )
    check(
        "Repeated sampled-rank check; no neighborhood or manifold certificate",
        all(rank == 2 for rank in ranks),
        "five supplied chart coordinates, two constraints; neighborhood rank unproved",
    )


def part3_conditional_intersection_with_the_exact_pmns_target_is_discrete() -> None:
    print("\n" + "=" * 88)
    print("PART 3: FINITE SEARCH WITH THE SUPPLIED TARGET IMPOSED")
    print("=" * 88)

    reps = collect_conditional_center_pairs()
    reps = sorted(reps, key=lambda rep: float(rep["delta_src"]))

    check(
        "This seeded target-constrained search returns two separated numerical representatives",
        len(reps) == 2,
        f"count={len(reps)}",
    )
    check(
        "The two sampled target-constrained representatives agree in x and y within 1e-10",
        len(reps) == 2
        and np.linalg.norm(np.asarray(reps[0]["x"]) - np.asarray(reps[1]["x"])) < 1.0e-10
        and np.linalg.norm(np.asarray(reps[0]["y"]) - np.asarray(reps[1]["y"])) < 1.0e-10,
    )
    check(
        "The sampled pair has opposite delta_src and I_src within 1e-10",
        len(reps) == 2
        and abs(float(reps[0]["delta_src"]) + float(reps[1]["delta_src"])) < 1.0e-10
        and abs(float(reps[0]["source_cubic"]) + float(reps[1]["source_cubic"])) < 1.0e-10,
        (
            f"delta_src=({float(reps[0]['delta_src']):.12f},"
            f"{float(reps[1]['delta_src']):.12f})"
        ) if len(reps) == 2 else "",
    )


def part4_note_records_the_correct_status() -> None:
    note = read('docs/DM_PMNS_Z3_DOUBLET_BLOCK_CENTER_POSITIVE_SHEET_NO_GO_THEOREM_NOTE_2026-04-20.md')
    print("DOCUMENTARY SCOPE (unscored):", "finite numerical diagnostics" in note)
    print("PR9844 remains held; its local-selector note is not consumed.")


def part5_n5_execution_certificate() -> None:
    print("EXECUTION SCOPE: finite seeded least-squares search only.")
    print("Per candidate: norm acceptance 1e-8, separate component checks 1e-10.")
    print("Per observable: original spread thresholds 0.5, 0.4, 0.8 retained.")
    print("Per block: finite-difference step 1e-6 and rank threshold 1e-5.")
    print("No site, mode completeness, global root exhaustion or limit certificate.")
    print("Exact roots, neighborhood rank and physical selection remain open.")


def main() -> int:
    print("=" * 88)
    print("DM PMNS Z3 FINITE CENTER-SEARCH DIAGNOSTIC")
    print("=" * 88)
    print()
    print("Question:")
    print("  Does the coefficient-free center law delta_db = 1, q_+ = 0, together")
    print("  with supplied sign condition I_src > 0, sample the remaining")
    print("  PMNS angle-pin I5 on the fixed native N_e seed surface?")

    reps = part1_positive_sheet_center_locus_is_not_a_point_selector()
    part2_center_constraints_have_rank_two_on_the_verified_patch(reps)
    part3_conditional_intersection_with_the_exact_pmns_target_is_discrete()
    part4_note_records_the_correct_status()
    part5_n5_execution_certificate()

    print("\n" + "=" * 88)
    print("RESULT")
    print("=" * 88)
    print("Finite residual, range and sampled-rank findings only.")
    print("The search does not establish exact roots, global two-solution exhaustion,")
    print("a local three-real manifold, a physical sheet, or an I5/I12 no-go.")
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 1 if FAIL_COUNT else 0


if __name__ == "__main__":
    sys.exit(main())
