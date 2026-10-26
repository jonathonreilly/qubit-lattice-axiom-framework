#!/usr/bin/env python3
"""This runner reproduces supplied finite numerical fixtures and checks documentary
consistency. Its unchanged numerical predicates, grids and optimizer settings
are not a proof of global optimality, exact roots, physical selection or an
exhaustive remaining research burden. Text matches report text only. Historical
literal-True narrative is not counted as a mathematical PASS.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = ['archive_unlanded/dm-neutrino-stale-runners-2026-04-30/DM_NEUTRINO_WEAK_TRIPLET_COEFFICIENT_AXIOM_BOUNDARY_NOTE_2026-04-15.md', 'docs/DM_LEPTOGENESIS_PMNS_OBSERVABLE_RELATIVE_ACTION_LAW_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_BREAKING_TRIPLET_CP_THEOREM_NOTE_2026-04-15.md', 'docs/DM_NEUTRINO_EXACT_H_SOURCE_SURFACE_PREIMAGE_BUNDLE_THEOREM_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_EXACT_H_SOURCE_SURFACE_THEOREM_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_POSITIVE_POLAR_H_CP_THEOREM_NOTE_2026-04-15.md', 'docs/DM_NEUTRINO_POSTCANONICAL_POLAR_SECTION_NOTE_2026-04-15.md', 'docs/DM_NEUTRINO_SOURCE_AMPLITUDE_THEOREM_NOTE_2026-04-15.md', 'docs/DM_NEUTRINO_SOURCE_BANK_Z3_DOUBLET_BLOCK_SELECTION_OBSTRUCTION_THEOREM_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_SOURCE_SURFACE_ACTIVE_AFFINE_POINT_SELECTION_BOUNDARY_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_SOURCE_SURFACE_ACTIVE_HALF_PLANE_THEOREM_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_SOURCE_SURFACE_ATOMIC_WITNESS_VOLUME_SELECTOR_NONREALIZATION_NOTE_2026-04-18.md', 'docs/DM_NEUTRINO_SOURCE_SURFACE_CARRIER_NORMAL_FORM_THEOREM_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_SOURCE_SURFACE_INTRINSIC_SLOT_THEOREM_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_SOURCE_SURFACE_SHIFT_QUOTIENT_BUNDLE_THEOREM_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_SOURCE_SURFACE_Z3_DOUBLET_BLOCK_POINT_SELECTION_THEOREM_NOTE_2026-04-16.md', 'docs/DM_SELECTOR_FIRST_SHOULDER_EXIT_THRESHOLD_SUPPORT_NOTE_2026-04-21.md', 'docs/DM_SELECTOR_RELATIVE_ACTION_RECOVERED_BRANCH_SEPARATION_SUPPORT_THEOREM_NOTE_2026-04-21.md', 'docs/SCALAR_SELECTOR_REMAINING_OPEN_IMPORTS_2026-04-20.md', 'scripts/dm_leptogenesis_exact_common.py', 'scripts/dm_selector_branch_support.py', 'scripts/frontier_dm_leptogenesis_flavor_column_functional_theorem.py', 'scripts/frontier_dm_leptogenesis_ne_charged_source_response_reduction.py', 'scripts/frontier_dm_leptogenesis_pmns_active_projector_reduction.py', 'scripts/frontier_dm_leptogenesis_pmns_observable_relative_action_law.py', 'scripts/frontier_dm_leptogenesis_pmns_projector_interface.py', 'scripts/frontier_dm_neutrino_breaking_triplet_cp_theorem.py', 'scripts/frontier_dm_neutrino_exact_h_source_surface_preimage_bundle_theorem.py', 'scripts/frontier_dm_neutrino_hermitian_bridge_carrier.py', 'scripts/frontier_dm_neutrino_positive_polar_h_cp_theorem.py', 'scripts/frontier_dm_neutrino_postcanonical_polar_section.py', 'scripts/frontier_dm_neutrino_source_bank_z3_doublet_block_selection_obstruction_theorem.py', 'scripts/frontier_dm_neutrino_source_surface_active_affine_point_selection_boundary.py', 'scripts/frontier_dm_neutrino_source_surface_active_half_plane_theorem.py', 'scripts/frontier_dm_neutrino_source_surface_atomic_witness_volume_selector_nonrealization.py', 'scripts/frontier_dm_neutrino_source_surface_carrier_normal_form.py', 'scripts/frontier_dm_neutrino_source_surface_intrinsic_slot_theorem.py', 'scripts/frontier_dm_neutrino_source_surface_shift_quotient_bundle_theorem.py', 'scripts/frontier_dm_neutrino_source_surface_z3_doublet_block_point_selection_theorem.py']

import math
import sys
from pathlib import Path

import numpy as np
from scipy.optimize import brentq, differential_evolution, minimize

from dm_selector_branch_support import ANCHOR_OFFSET, common_shift, recovered_bank
from frontier_dm_leptogenesis_pmns_observable_relative_action_law import (
    XBAR_NE,
    YBAR_NE,
    best_eta_from_params,
    build_active_from_params,
    eta_columns_from_active,
    relative_action_from_params,
)
from frontier_dm_neutrino_source_bank_z3_doublet_block_selection_obstruction_theorem import (
    active_target_from_h,
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


def observable_relative_action_selection() -> tuple[int, np.ndarray, np.ndarray, float, np.ndarray, np.ndarray]:
    extremal = differential_evolution(
        lambda p: -best_eta_from_params(np.asarray(p, dtype=float)),
        bounds=[
            (-4.0, 4.0),
            (-4.0, 4.0),
            (-4.0, 4.0),
            (-4.0, 4.0),
            (-math.pi, math.pi),
        ],
        seed=0,
        maxiter=20,
        popsize=10,
        polish=False,
        disp=False,
    )
    x_opt, y_opt, delta_opt = build_active_from_params(extremal.x)
    _h_opt, _packet_opt, etas_opt = eta_columns_from_active(x_opt, y_opt, delta_opt)
    i_star = int(np.argmax(etas_opt))

    def eta_i(params: np.ndarray) -> float:
        x, y, delta = build_active_from_params(params)
        _h, _packet, etas = eta_columns_from_active(x, y, delta)
        return float(etas[i_star])

    def line_profile(t: float) -> np.ndarray:
        return np.asarray(extremal.x, dtype=float) * t

    t_root = brentq(lambda t: eta_i(line_profile(t)) - 1.0, 0.0, 1.0)
    start = line_profile(t_root)

    result = minimize(
        relative_action_from_params,
        start,
        method="SLSQP",
        bounds=[
            (-6.0, 6.0),
            (-6.0, 6.0),
            (-6.0, 6.0),
            (-6.0, 6.0),
            (-math.pi, math.pi),
        ],
        constraints=[{"type": "eq", "fun": lambda p: eta_i(np.asarray(p, dtype=float)) - 1.0}],
        options={"ftol": 1.0e-12, "maxiter": 500},
    )

    x_sel, y_sel, delta_sel = build_active_from_params(result.x)
    h_sel, _packet_sel, etas_sel = eta_columns_from_active(x_sel, y_sel, delta_sel)
    return i_star, x_sel, y_sel, float(delta_sel), np.asarray(h_sel, dtype=complex), np.asarray(etas_sel, dtype=float)


def main() -> int:
    print("=" * 88)
    print("DM SELECTOR RELATIVE-ACTION / RECOVERED-BRANCH SEPARATION FINITE NUMERICAL SUPPORT")
    print("=" * 88)

    rel_note = read("docs/DM_LEPTOGENESIS_PMNS_OBSERVABLE_RELATIVE_ACTION_LAW_NOTE_2026-04-16.md")
    thresh_note = read("docs/DM_SELECTOR_FIRST_SHOULDER_EXIT_THRESHOLD_SUPPORT_NOTE_2026-04-21.md")
    review = read("docs/SCALAR_SELECTOR_REMAINING_OPEN_IMPORTS_2026-04-20.md")

    i_star, x_sel, y_sel, delta_sel, h_sel, etas_sel = observable_relative_action_selection()
    _lifts, hs_bank, repairs_bank, targets = recovered_bank()
    mu_bank = common_shift(repairs_bank, ANCHOR_OFFSET)

    target_sel = np.asarray(active_target_from_h(h_sel), dtype=float)
    target_bank = [np.asarray(t, dtype=float) for t in targets]
    h_distances = np.array([np.linalg.norm(h_sel - np.asarray(h, dtype=complex)) for h in hs_bank], dtype=float)
    target_distances = np.array([np.linalg.norm(target_sel - t) for t in target_bank], dtype=float)

    params_bank = [inverse_eigenvalue_parameters(h, mu_bank) for h in hs_bank]
    params_sel = inverse_eigenvalue_parameters(h_sel, mu_bank)
    tau_b_bank = np.array([math.log1p(p[1]) for p in params_bank], dtype=float)
    tau_b_min = float(np.min(tau_b_bank))
    tau_b_sel = float(math.log1p(params_sel[1]))

    v_sel_low = float(witness_volume_from_atomic_field(params_sel, 0.13))
    v_sel_high = float(witness_volume_from_atomic_field(params_sel, 0.14))
    vals_bmin = np.array([witness_volume_from_atomic_field(p, tau_b_min) for p in params_bank], dtype=float)
    v_sel_bmin = float(witness_volume_from_atomic_field(params_sel, tau_b_min))
    vals_bsel = np.array([witness_volume_from_atomic_field(p, tau_b_sel) for p in params_bank], dtype=float)
    v_sel_bsel = float(witness_volume_from_atomic_field(params_sel, tau_b_sel))

    print("\n" + "=" * 88)
    print("PART 1: SUPPLIED NUMERICALLY CONSTRUCTED SOURCE")
    print("=" * 88)

    check("DOCUMENTARY: parent names an operational PMNS-assisted selector and disclaims branch-global analytic proof; no authority is inferred", "operational PMNS-assisted off-seed source selector" in rel_note and "branch-global analytic proof" in rel_note and "does **not** claim" in rel_note)
    check(
        'The reconstructed source stays on the computed fixed native seed surface',
        abs(np.mean(x_sel) - XBAR_NE) < 1.0e-12 and abs(np.mean(y_sel) - YBAR_NE) < 1.0e-12,
        f"(xbar,ybar)=({np.mean(x_sel):.6f},{np.mean(y_sel):.6f})",
    )
    check(
        'The reconstructed source still closes the favored transport column computedly',
        i_star == 0 and abs(etas_sel[0] - 1.0) < 1.0e-12,
        f"delta={delta_sel:.12e}, etas={np.round(etas_sel, 12)}",
    )

    print("\n" + "=" * 88)
    print("PART 2: THE RELATIVE-ACTION SOURCE STAYS OFF THE RECOVERED SELECTOR BRANCH")
    print("=" * 88)

    check(
        'No recovered-bank Hermitian source coincides with the relative-action source',
        float(np.min(h_distances)) > 1.0e-6,
        f"min Frobenius distance = {float(np.min(h_distances)):.12f}",
    )
    check(
        'No recovered active target coincides with the relative-action target',
        float(np.min(target_distances)) > 1.0e-6,
        f"min target distance = {float(np.min(target_distances)):.12f}",
    )
    check(
        'The nearest recovered point is the preferred lift, but the gap is still macroscopically nonzero on the audited scale',
        int(np.argmin(h_distances)) == 0 and float(np.min(h_distances)) > 1.0,
        f"nearest recovered index = {int(np.argmin(h_distances))}",
    )

    print("\n" + "=" * 88)
    print("PART 3: THE RELATIVE-ACTION SOURCE DOES NOT REALIZE THE RECOVERED THRESHOLD CANDIDATE")
    print("=" * 88)

    check("DOCUMENTARY only: first-shoulder note states conditional finite support and withdraws whole-window certification; text is not proof", "conditional finite numerical support; physical threshold selection open" in thresh_note and "exact-onset/whole-window certificate attribution is withdrawn" in thresh_note)
    check(
        'The relative-action source has its own later middle-branch breakpoint',
        tau_b_sel > tau_b_min,
        f"(tau_b_sel, tau_b_min)=({tau_b_sel:.15f}, {tau_b_min:.15f})",
    )
    check(
        'At tau = 0.13 and tau = 0.14 the relative-action source is still on the full-volume shoulder of the witness family',
        abs(v_sel_low - 1.0) < 1.0e-12 and abs(v_sel_high - 1.0) < 1.0e-12,
        f"(V_0.13, V_0.14)=({v_sel_low:.12f}, {v_sel_high:.12f})",
    )
    check(
        'At the recovered-bank canonical breakpoint tau_b,min, the preferred recovered lift still beats the relative-action source',
        vals_bmin[0] + 1.0e-12 < v_sel_bmin,
        f"(V_pref, V_rel)=({vals_bmin[0]:.12f}, {v_sel_bmin:.12f})",
    )
    check(
        'At its own breakpoint tau_b,rel, the relative-action source becomes strictly smaller than every recovered-bank competitor',
        v_sel_bsel + 1.0e-12 < float(np.min(vals_bsel)),
        f"(V_rel, min_bank)=({v_sel_bsel:.12f}, {float(np.min(vals_bsel)):.12f})",
    )

    print("\n" + "=" * 88)
    print("PART 4: DOCUMENTARY BOUNDARY AND FINITE COMPARISONS")
    print("=" * 88)

    check("DOCUMENTARY: summary reports physical selection obligations open and PMNS angles supplied", "selection obligations remain open" in " ".join(review.split()) and "PMNS angle triple is an input" in " ".join(review.split()))
    print("INFO: Historical selector-burden narration withdrawn; no mathematical check or exhaustive-route inference.")
    print("INFO: Historical selector-burden narration withdrawn; no mathematical check or exhaustive-route inference.")

    print("\n" + "=" * 88)
    print("RESULT: finite supplied computations and documentary observations only")
    print("No physical selector, exact optimizer/root certificate, exhaustive route or continuous-window theorem follows.")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")

    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
