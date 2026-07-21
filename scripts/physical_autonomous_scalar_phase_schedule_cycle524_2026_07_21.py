#!/usr/bin/env python3
"""Cycle 524: autonomous scalar phase-marker schedule.

This runner does not interpret the schedule count as physical time.  It tests
a three-state scalar marker, encoded in two M2 with one locally excluded
computational state, which autonomously sequences coin, the commuting FSWAP
layer, and contact.  The code-space identity is

    E_schedule G_coarse = F_physical**3 E_schedule.

The two-cell fixture uses the complete 4096-dimensional Fock space.  The
degree-three star recurrence uses the declared n=0,...,2 301-dimensional
fixture.  Physical encodings are regenerated at L=5 and held L=6.
"""

from __future__ import annotations

from itertools import product
from pathlib import Path
import json
import re
import subprocess
import sys

import numpy as np
from scipy import sparse


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import exact_3d_higher_form_bosonization_cycle235_2026_07_17 as c235
import physical_cycle269_overlap_aware_two_cell_cycle315_2026_07_18 as c315
import physical_cycle269_four_cell_star_cycle324_2026_07_18 as c324
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230
import wilson_subsystem_sector_free_compiler_cycle269_2026_07_17 as c269


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_AUTONOMOUS_SCALAR_PHASE_SCHEDULE_CYCLE524_NOTE_2026-07-21.md"
)
FRESH_MAIN = "8e1adb5bc486b3236f3988214ce49946e9bccd65"
TOLERANCE = 8e-10
PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def opnorm(matrix) -> float:
    return c315.largest_singular(matrix)


def raw(matrix) -> float:
    return c315.raw_maximum_abs(matrix)


def note_contract() -> None:
    if not NOTE.exists():
        check("the Cycle-524 note exists", False, NOTE)
        return
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "authority: none",
        "audit: unset",
        "state count, not time",
        "three marker states",
        "two m2 per coarse cell",
        "one locally excluded computational state",
        "neighbor equality",
        "e_schedule g_coarse = f_physical^3 e_schedule",
        "complete two-cell all-fock",
        "degree-three star",
        "all 24 proper-cubic frames",
        "held l=6",
        "host queries = 0",
        "no global jordan–wigner",
        "no axiom pressure",
        "n1",
        "n2",
        "n3",
        "n4",
        "n5",
        "n6",
        "n7",
        "n8",
    )
    missing = tuple(fragment for fragment in required if fragment not in text)
    check("the note pins the schedule and N1-N8 boundary", not missing, missing)


def methodology_controls() -> dict:
    completed = subprocess.run(
        ["git", "merge-base", "--is-ancestor", FRESH_MAIN, "origin/main"],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    check(
        "the no-go-discipline methodology commit remains on origin/main",
        completed.returncode == 0,
        {"recorded": FRESH_MAIN, "returncode": completed.returncode},
    )
    note = NOTE.read_text(encoding="utf-8")
    route_markers = re.findall(
        r"^\|\s*[^|]+\|\s*\*\*(ATTEMPTED|RULED OUT BY PRIOR RESULT|OPEN / UNTESTED)\*\*\s*\|",
        note,
        re.MULTILINE,
    )
    check(
        "N1 uses explicit route-status markers",
        len(route_markers) >= 7 and "OPEN / UNTESTED" in route_markers,
        route_markers,
    )
    wall_rows = re.findall(
        r"^\|\s*W_[^|]+\|\s*W_[^|]+\|\s*(yes|no)\s*\|\s*(yes|no)\s*\|\s*(yes|no)\s*\|",
        note,
        re.MULTILINE | re.IGNORECASE,
    )
    check(
        "N2 records bidirectional wall-independence evidence",
        len(wall_rows) >= 6,
        {"rows": len(wall_rows)},
    )
    return {
        "fresh_main_ancestor": completed.returncode == 0,
        "N1_explicit_route_rows": len(route_markers),
        "N2_wall_pair_rows": len(wall_rows),
    }


def phase_shift() -> sparse.csc_matrix:
    """0->1->2->0, while the unused computational state 3 is fixed."""
    return sparse.coo_matrix(
        (np.ones(4), ((1, 2, 0, 3), (0, 1, 2, 3))),
        shape=(4, 4),
        dtype=complex,
    ).tocsc()


def phase_schedule(coin, stream, contact) -> sparse.csc_matrix:
    """One autonomous marker count on the synchronized marker subspace."""
    dimension = coin.shape[0]
    zero = sparse.csc_matrix((dimension, dimension), dtype=complex)
    identity = sparse.eye(dimension, format="csc")
    return sparse.bmat(
        (
            (zero, zero, contact, zero),
            (coin, zero, zero, zero),
            (zero, stream, zero, zero),
            (zero, zero, zero, identity),
        ),
        format="csc",
    )


def phase_embedding(dimension: int, phase: int = 0) -> sparse.csc_matrix:
    marker = sparse.coo_matrix(
        ([1.0], ([phase], [0])), shape=(4, 1), dtype=complex
    ).tocsc()
    return sparse.kron(marker, sparse.eye(dimension, format="csc"), format="csc")


def schedule_controls(coin, stream, contact) -> dict:
    dimension = coin.shape[0]
    identity = sparse.eye(dimension, format="csc")
    schedule_identity = sparse.eye(4 * dimension, format="csc")
    schedule = phase_schedule(coin, stream, contact)
    embedding = phase_embedding(dimension)
    macro = contact @ stream @ coin
    cube = schedule @ schedule @ schedule
    intertwining = cube @ embedding - embedding @ macro

    deleted = schedule.tolil(copy=True)
    deleted[dimension : 2 * dimension, :dimension] = 0
    deleted = deleted.tocsc()

    two_phase = sparse.bmat(
        (
            (sparse.csc_matrix(identity.shape), contact @ stream),
            (coin, sparse.csc_matrix(identity.shape)),
        ),
        format="csc",
    )
    two_embedding = sparse.vstack((identity, sparse.csc_matrix(identity.shape)), format="csc")
    two_macro_residual = opnorm(
        two_phase @ two_phase @ two_embedding - two_embedding @ macro
    )
    return {
        "phase_states_used": 3,
        "physical_marker_dimension": 4,
        "marker_M2_per_cell": 2,
        "excluded_marker_states_per_cell": 1,
        "schedule_unitarity": opnorm(schedule.conj().T @ schedule - schedule_identity),
        "schedule_unitarity_raw_maximum": raw(
            schedule.conj().T @ schedule - schedule_identity
        ),
        "inverse_residual": opnorm(schedule.conj().T @ schedule - schedule_identity),
        "three_count_intertwining": opnorm(intertwining),
        "three_count_intertwining_raw_maximum": raw(intertwining),
        "marker_free_packaged_macro_residual": opnorm(macro - contact @ stream @ coin),
        "two_phase_packaged_contact_stream_residual": two_macro_residual,
        "two_phase_packs_two_atomic_stages": True,
        "deleted_coin_transition_unitarity_residual": opnorm(
            deleted.conj().T @ deleted - schedule_identity
        ),
        "unused_state_fixed_residual": opnorm(
            schedule @ phase_embedding(dimension, 3) - phase_embedding(dimension, 3)
        ),
    }


def marker_constraints(cells: int, edges: tuple[tuple[int, int], ...]) -> dict:
    marker_dimension = 4**cells
    states = tuple(product(range(4), repeat=cells))
    state_index = {state: index for index, state in enumerate(states)}
    shift = phase_shift()
    shift_all = sparse.csc_matrix([[1.0]])
    for _ in range(cells):
        shift_all = sparse.kron(shift_all, shift, format="csc")

    use_constraints = []
    for cell in range(cells):
        diagonal = [1 if state[cell] != 3 else -1 for state in states]
        use_constraints.append(sparse.diags(diagonal, format="csc", dtype=complex))
    equality_constraints = []
    for first, second in edges:
        diagonal = [1 if state[first] == state[second] else -1 for state in states]
        equality_constraints.append(
            sparse.diags(diagonal, format="csc", dtype=complex)
        )

    constraints = tuple(use_constraints + equality_constraints)
    identity = sparse.eye(marker_dimension, format="csc")
    valid = [
        state
        for state in states
        if all(value != 3 for value in state)
        and all(state[first] == state[second] for first, second in edges)
    ]
    use_only_rank = 3**cells
    equality_only_rank = sum(
        all(state[first] == state[second] for first, second in edges)
        for state in states
    )
    desynchronized = tuple(0 if cell == 0 else 1 for cell in range(cells))
    vector = np.zeros(marker_dimension, dtype=complex)
    vector[state_index[desynchronized]] = 1
    after_three = shift_all @ shift_all @ shift_all @ vector
    synchronized_zero = np.zeros(marker_dimension, dtype=complex)
    synchronized_zero[state_index[(0,) * cells]] = 1
    return {
        "cells": cells,
        "marker_shell_dimension": marker_dimension,
        "locally_constrained_schedule_rank": len(valid),
        "expected_rank": 3,
        "use_only_rank_if_neighbor_equality_deleted": use_only_rank,
        "rank_surplus_if_neighbor_equality_deleted": use_only_rank - len(valid),
        "equality_only_rank_if_unused_state_constraint_deleted": equality_only_rank,
        "rank_surplus_if_unused_state_constraint_deleted": equality_only_rank - len(valid),
        "maximum_constraint_involution_residual": max(
            opnorm(constraint @ constraint - identity) for constraint in constraints
        ),
        "maximum_constraint_commutator": max(
            [
                opnorm(left @ right - right @ left)
                for left in constraints
                for right in constraints
            ]
            or [0.0]
        ),
        "maximum_shift_constraint_commutator": max(
            opnorm(shift_all @ constraint - constraint @ shift_all)
            for constraint in constraints
        ),
        "desynchronized_three_count_return_residual": float(
            np.linalg.norm(after_three - vector)
        ),
        "desynchronized_to_code_overlap_after_three_counts": float(
            abs(np.vdot(synchronized_zero, after_three))
        ),
        "neighbor_equality_constraint_support_M2": 4,
        "unused_state_constraint_support_M2": 2,
    }


def completion_controls(encoding, layers: tuple, macro) -> dict:
    columns = encoding.shape[1]
    identity = sparse.eye(columns, format="csc")
    gram = (encoding.conj().T @ encoding).tocsc()
    gram_difference = gram - identity
    stage_residuals = []
    reduced_completions = []
    for layer in layers:
        residual = encoding @ ((layer - identity) @ gram_difference)
        stage_residuals.append(opnorm(residual))
        reduced_completions.append(identity + (layer - identity) @ gram)
    reduced_macro = (
        reduced_completions[2]
        @ reduced_completions[1]
        @ reduced_completions[0]
    )
    macro_residual = encoding @ (reduced_macro - macro)
    return {
        "physical_completion_formula": "A_E(L)=E L E^dagger + I-E E^dagger",
        "Gram_residual": opnorm(gram_difference),
        "Gram_raw_maximum": raw(gram_difference),
        "maximum_stage_intertwining_residual": max(stage_residuals),
        "macro_EG_minus_GphysicalE_residual": opnorm(macro_residual),
        "macro_EG_minus_GphysicalE_raw_maximum": raw(macro_residual),
        "off_code_identity_completion_supplied": True,
    }


def joint_role_completion_controls(encodings: tuple, layers: tuple, macro) -> dict:
    """Test E_4=(1/sqrt(24)) sum_pi |pi> tensor E_pi without stacking it."""
    columns = encodings[0].shape[1]
    identity = sparse.eye(columns, format="csc")
    grams = tuple((encoding.conj().T @ encoding).tocsc() for encoding in encodings)
    joint_gram = sum(
        grams, start=sparse.csc_matrix(identity.shape, dtype=complex)
    ) / len(encodings)

    stage_residuals = []
    stage_raw = []
    for layer in layers:
        residual_norm_square = sparse.csc_matrix(identity.shape, dtype=complex)
        maximum_raw = 0.0
        for encoding, gram in zip(encodings, grams):
            residual = encoding @ ((layer - identity) @ (gram - identity))
            residual_norm_square += residual.conj().T @ residual / len(encodings)
            maximum_raw = max(maximum_raw, raw(residual) / np.sqrt(len(encodings)))
        stage_residuals.append(np.sqrt(max(0.0, opnorm(residual_norm_square))))
        stage_raw.append(maximum_raw)

    macro_norm_square = sparse.csc_matrix(identity.shape, dtype=complex)
    macro_raw = 0.0
    for encoding, gram in zip(encodings, grams):
        reduced = tuple(identity + (layer - identity) @ gram for layer in layers)
        residual = encoding @ (reduced[2] @ reduced[1] @ reduced[0] - macro)
        macro_norm_square += residual.conj().T @ residual / len(encodings)
        macro_raw = max(macro_raw, raw(residual) / np.sqrt(len(encodings)))
    return {
        "physical_completion_formula": (
            "E_4=(1/sqrt(24)) sum_pi |pi> tensor E_pi; "
            "A_pi(L)=E_pi L E_pi^dagger + I-E_pi E_pi^dagger"
        ),
        "Gram_residual": opnorm(joint_gram - identity),
        "Gram_raw_maximum": raw(joint_gram - identity),
        "maximum_stage_intertwining_residual": max(stage_residuals),
        "maximum_stage_intertwining_raw_maximum": max(stage_raw),
        "macro_EG_minus_GphysicalE_residual": np.sqrt(
            max(0.0, opnorm(macro_norm_square))
        ),
        "macro_EG_minus_GphysicalE_raw_maximum": macro_raw,
        "off_code_identity_completion_supplied": True,
        "joint_S4_role_states": len(encodings),
        "joint_S4_unused_computational_states_excluded": 8,
    }


def two_cell_physical_fixture(length: int, labels, layers: tuple, macro) -> dict:
    code = c269.build_code(length)
    reducer = c315.RayReducer(code)
    encoding = c315.joint_encoding(code, labels, reducer, False)
    if encoding.shape[0] < len(reducer.row_by_aux):
        encoding.resize((len(reducer.row_by_aux), encoding.shape[1]))
    support = c315.physical_support_and_constraint_controls(code, labels)
    completion = completion_controls(encoding, layers, macro)
    return {
        "L": length,
        "held": length == 6,
        "logical_columns_complete_all_Fock": len(labels),
        "physical_rays": encoding.shape[0],
        "matrix_nonzeros": encoding.nnz,
        "native_patch_with_edge_role_M2": support[
            "total_patch_union_with_edge_role_gauge"
        ],
        "phase_marker_M2": 4,
        "total_bounded_patch_M2": support[
            "total_patch_union_with_edge_role_gauge"
        ]
        + 4,
        "port_constraint_commutator_failures": support[
            "port_constraint_commutator_failures"
        ],
        "fixed_sector_commutator_failures": support[
            "fixed_sector_commutator_failures"
        ],
        **completion,
    }


def star_physical_fixture(length: int, labels, layers: tuple, macro) -> dict:
    code = c269.build_code(length)
    geometry = c324.GEOMETRIES["star"]
    encodings, reducer, support = c324.multi_order_encodings(
        code, geometry["cells"], labels
    )
    identity = sparse.eye(len(labels), format="csc")
    gram_residuals = [
        opnorm(encoding.conj().T @ encoding - identity) for encoding in encodings
    ]
    completion = joint_role_completion_controls(encodings, layers, macro)
    constraints = c324.inherited_constraint_controls(code, geometry["cells"])
    return {
        "L": length,
        "held": length == 6,
        "logical_columns_n0_to_n2": len(labels),
        "shared_physical_rays": len(reducer.row_by_aux),
        "twenty_four_order_total_nonzeros": sum(E.nnz for E in encodings),
        "maximum_twenty_four_order_Gram_residual": max(gram_residuals),
        "native_patch_with_joint_S4_role_M2": support[
            "face_port_cell_role_union_M2"
        ]
        + 5,
        "phase_marker_M2": 8,
        "total_bounded_patch_M2": support["face_port_cell_role_union_M2"] + 5 + 8,
        "port_constraint_commutator_failures": constraints[
            "port_constraint_commutator_failures"
        ],
        "fixed_sector_commutator_failures": constraints[
            "fixed_sector_commutator_failures"
        ],
        **completion,
    }


def two_cell_covariance(labels, coin, contact) -> dict:
    frames = c235.proper_cubic_frames()
    identity = sparse.eye(len(labels), format="csc")
    base_stream = c315.edge_fswap_matrix(labels, 0)
    base_schedule = phase_schedule(coin, base_stream, contact)
    residuals = []
    unitarities = []
    for frame in frames:
        mapped_direction = frame @ np.asarray((1, 0, 0), dtype=int)
        axis = int(np.flatnonzero(mapped_direction)[0])
        reversed_endpoints = int(mapped_direction[axis]) == -1
        representation = c315.pair_frame_representation(
            labels, frame, reversed_endpoints
        )
        target = phase_schedule(
            coin, c315.edge_fswap_matrix(labels, axis), contact
        )
        lifted = sparse.kron(sparse.eye(4, format="csc"), representation, format="csc")
        residuals.append(opnorm(lifted @ base_schedule - target @ lifted))
        unitarities.append(
            opnorm(representation.conj().T @ representation - identity)
        )
    inherited = c315.covariance_translation_controls(
        labels, coin, contact, contact @ base_stream @ coin
    )
    return {
        "proper_cubic_frames": len(frames),
        "maximum_schedule_covariance_residual": max(residuals),
        "maximum_frame_representation_unitarity": max(unitarities),
        "edge_role_group_law_tests": inherited["edge_role_group_law_tests"],
        "edge_role_group_law_failures": inherited["edge_role_group_law_failures"],
        "marker_frame_action": "scalar identity",
    }


def star_covariance(labels, coin, streams, contact) -> dict:
    frames = c235.proper_cubic_frames()
    base_stream = streams[2] @ streams[1] @ streams[0]
    base_schedule = phase_schedule(coin, base_stream, contact)
    representations = {}
    residuals = []
    for frame in frames:
        representation = c324.frame_representation(labels, frame)
        representations[tuple(frame.reshape(-1))] = representation
        target_streams = tuple(
            c324.edge_fswap(labels, c324.mapped_edge(edge, frame))
            for edge in c324.GEOMETRIES["star"]["edges"]
        )
        target_schedule = phase_schedule(
            coin, target_streams[2] @ target_streams[1] @ target_streams[0], contact
        )
        lifted = sparse.kron(
            sparse.eye(4, format="csc"), representation, format="csc"
        )
        residuals.append(opnorm(lifted @ base_schedule - target_schedule @ lifted))

    group_failures = 0
    maximum_group_residual = 0.0
    for left in frames:
        for right in frames:
            difference = (
                representations[tuple(left.reshape(-1))]
                @ representations[tuple(right.reshape(-1))]
                - representations[tuple((left @ right).reshape(-1))]
            )
            maximum_group_residual = max(maximum_group_residual, opnorm(difference))
            group_failures += difference.nnz != 0
    return {
        "proper_cubic_frames": len(frames),
        "schedule_frame_tests": len(frames),
        "maximum_schedule_covariance_residual": max(residuals),
        "schedule_group_product_tests": len(frames) ** 2,
        "schedule_group_product_failures": group_failures,
        "maximum_schedule_group_product_residual": maximum_group_residual,
        "marker_frame_action": "scalar identity",
        "axis_or_chirality_phase_marker_supplied": False,
    }


def lawful_domain_controls() -> dict:
    rejects = 0
    for operation in (
        lambda: c315.joint_labels(13),
        lambda: c324.four_cell_labels(3),
        lambda: marker_constraints(1, ((0, 1),)),
    ):
        try:
            operation()
        except (ValueError, IndexError):
            rejects += 1
    return {
        "declared_two_cell_domain": "complete n=0,...,12 Fock space",
        "declared_star_domain": "four cells with total n=0,...,2",
        "lawful_domain_rejections": rejects,
        "expected_rejections": 3,
    }


def main() -> int:
    print("CYCLE 524: AUTONOMOUS SCALAR PHASE-MARKER SCHEDULE")
    print("authority=none; audit=unset; schedule state count is not physical time")
    note_contract()
    methodology = methodology_controls()

    two_labels = c315.joint_labels()
    two_coin, two_stream, two_contact, two_update, two_update_rows = (
        c315.logical_update_controls(two_labels)
    )
    two_schedule = schedule_controls(two_coin, two_stream, two_contact)
    two_markers = marker_constraints(2, ((0, 1),))
    two_covariance = two_cell_covariance(two_labels, two_coin, two_contact)
    two_physical = tuple(
        two_cell_physical_fixture(
            length,
            two_labels,
            (two_coin, two_stream, two_contact),
            two_update,
        )
        for length in (5, 6)
    )

    star_labels = c324.four_cell_labels()
    star_update_rows, star_coin, star_streams, star_contact, star_orders = (
        c324.update_controls(star_labels, "star")
    )
    star_stream = star_streams[2] @ star_streams[1] @ star_streams[0]
    star_update = star_contact @ star_stream @ star_coin
    star_schedule = schedule_controls(star_coin, star_stream, star_contact)
    star_edges = tuple(
        (first[0], second[0])
        for first, second in c324.GEOMETRIES["star"]["edges"]
    )
    star_markers = marker_constraints(4, star_edges)
    star_covariance_rows = star_covariance(
        star_labels, star_coin, star_streams, star_contact
    )
    star_physical = tuple(
        star_physical_fixture(
            length,
            star_labels,
            (star_coin, star_stream, star_contact),
            star_update,
        )
        for length in (5, 6)
    )

    commutators = {
        "two_cell_stream_coin": opnorm(two_stream @ two_coin - two_coin @ two_stream),
        "two_cell_contact_stream": opnorm(
            two_contact @ two_stream - two_stream @ two_contact
        ),
        "star_maximum_stream_stream": max(
            opnorm(star_streams[first] @ star_streams[second] - star_streams[second] @ star_streams[first])
            for first, second in ((0, 1), (0, 2), (1, 2))
        ),
        "star_maximum_six_order_update_residual": max(
            opnorm(update - star_orders[0][1]) for _order, update in star_orders
        ),
    }
    mass = {
        "Cycle219_mass_fixture": c219.rest_mass(c219.common_species(-0.3)),
        "two_cell_mass": two_update_rows["two_cell_rest_mass"],
        "two_cell_uniform_one_particle_residual": two_update_rows[
            "two_cell_uniform_one_particle_residual"
        ],
        "star_mass": star_update_rows["four_cell_rest_mass"],
        "star_uniform_one_particle_residual": star_update_rows[
            "uniform_one_particle_eigen_residual"
        ],
    }
    domains = lawful_domain_controls()

    result = {
        "authority": "none",
        "audit": "unset",
        "identity": "E_schedule G_coarse = F_physical^3 E_schedule",
        "schedule_count_is_physical_time": False,
        "host_queries": 0,
        "global_Jordan_Wigner_ordering": False,
        "nonlocal_parity_service": False,
        "two_cell_schedule": two_schedule,
        "two_cell_marker_constraints": two_markers,
        "two_cell_covariance": two_covariance,
        "two_cell_physical": two_physical,
        "star_schedule": star_schedule,
        "star_marker_constraints": star_markers,
        "star_covariance": star_covariance_rows,
        "star_physical": star_physical,
        "commutators_and_alternatives": commutators,
        "mass_fixture": mass,
        "domains": domains,
        "methodology": methodology,
        "supplied_structure": (
            "Cycle-219 coin and mass fixture; Cycle-230 contact coupling; "
            "Cycle-315 full two-cell M64 physical encoder and edge-role gauge; "
            "Cycle-324 n<=2 degree-three-star/S4-order physical shell; "
            "Cycle-235 proper-cubic frames; sparse off-code completion formula"
        ),
        "new_in_cycle_524": (
            "three-state scalar marker in two M2 per cell; local unused-state "
            "and neighbor-equality constraints; autonomous three-count recurrence; "
            "schedule-level covariance and deletion/desynchronization audit"
        ),
    }

    check(
        "the three-state schedule is unitary and exactly recurs to D S K",
        two_schedule["schedule_unitarity"] < TOLERANCE
        and two_schedule["three_count_intertwining"] < TOLERANCE
        and star_schedule["schedule_unitarity"] < TOLERANCE
        and star_schedule["three_count_intertwining"] < TOLERANCE,
        {
            "two": two_schedule,
            "star": star_schedule,
        },
    )
    check(
        "local marker constraints have rank three and are preserved",
        two_markers["locally_constrained_schedule_rank"] == 3
        and star_markers["locally_constrained_schedule_rank"] == 3
        and two_markers["maximum_shift_constraint_commutator"] < TOLERANCE
        and star_markers["maximum_shift_constraint_commutator"] < TOLERANCE,
        {"two": two_markers, "star": star_markers},
    )
    check(
        "deletion and desynchronization controls are discriminating",
        two_schedule["deleted_coin_transition_unitarity_residual"] > 0.9
        and star_schedule["deleted_coin_transition_unitarity_residual"] > 0.9
        and two_markers["rank_surplus_if_neighbor_equality_deleted"] > 0
        and star_markers["rank_surplus_if_neighbor_equality_deleted"] > 0
        and two_markers["desynchronized_to_code_overlap_after_three_counts"] == 0,
        {
            "two_deleted": two_schedule["deleted_coin_transition_unitarity_residual"],
            "star_deleted": star_schedule["deleted_coin_transition_unitarity_residual"],
            "two_desync": two_markers,
            "star_desync": star_markers,
        },
    )
    check(
        "L5 and held L6 physical completions satisfy E G = Gphysical E",
        all(
            row["Gram_residual"] < TOLERANCE
            and row["macro_EG_minus_GphysicalE_residual"] < TOLERANCE
            and row["port_constraint_commutator_failures"] == 0
            and row["fixed_sector_commutator_failures"] == 0
            for row in two_physical + star_physical
        ),
        {"two": two_physical, "star": star_physical},
    )
    check(
        "all 24 proper-cubic frames and schedule group products pass",
        two_covariance["maximum_schedule_covariance_residual"] < TOLERANCE
        and two_covariance["edge_role_group_law_failures"] == 0
        and star_covariance_rows["maximum_schedule_covariance_residual"] < TOLERANCE
        and star_covariance_rows["schedule_group_product_failures"] == 0,
        {"two": two_covariance, "star": star_covariance_rows},
    )
    check(
        "the degree-three seam layer is marker-free and order-independent",
        commutators["star_maximum_stream_stream"] < TOLERANCE
        and commutators["star_maximum_six_order_update_residual"] < TOLERANCE,
        commutators,
    )
    check(
        "the one-particle mass fixture is preserved",
        abs(mass["two_cell_mass"] - mass["Cycle219_mass_fixture"]) < TOLERANCE
        and abs(mass["star_mass"] - mass["Cycle219_mass_fixture"]) < TOLERANCE
        and mass["two_cell_uniform_one_particle_residual"] < TOLERANCE
        and mass["star_uniform_one_particle_residual"] < TOLERANCE,
        mass,
    )
    check(
        "lawful domains reject all out-of-contract probes",
        domains["lawful_domain_rejections"] == domains["expected_rejections"],
        domains,
    )

    print("RESULT_JSON", json.dumps(result, sort_keys=True, default=str))
    print(f"SUMMARY {PASS} passed / {FAIL} failed")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
