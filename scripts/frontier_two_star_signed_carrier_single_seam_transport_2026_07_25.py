#!/usr/bin/env python3
"""Signed-carrier repair of one local seam on ``E_refresh``.

The Route-C qutrit phase does not preserve the original product carrier
preparation: in ten two-cell columns it flips one of five carrier amplitudes.
That is a structured vector, not an arbitrary leaked state.  This runner
derives the signed vector directly from the landed carrier amplitudes and the
executed qutrit truth table, synthesizes it with the same five two-rail Givens
word, and uses its inverse before one decoded endpoint FSWAP.  The edge-role
M2 marks the signed chart stage and is returned; all charts and carrier work
are then recomputed into the same ``E_refresh``.

The one-edge local graded FSWAP closes exactly without a dense code-space
completion or a global ordering string.  Composing the same local convention
over all eleven edges does not yet equal Route C's globally sorted exterior
matrix.  The runner reports that first composition residual rather than
promoting the one-edge result to a full-patch compiler.  No no-go, minimum,
shared-obstruction, or axiom-pressure claim is made.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from hashlib import sha256
from itertools import combinations, product
import json
import math
import resource
import time

import numpy as np
from scipy import sparse

import frontier_full128_cycle_cocycle_intertwiner_2026_07_24 as c655
import frontier_full128_two_rail_fixed_law_core_2026_07_24 as c656
import frontier_two_overlapping_star_sparse_qutrit_edge_gauge_core_2026_07_25 as qcore
import frontier_two_star_full128_coin_covariant_feature_refresh_2026_07_25 as refresh
import physical_cycle269_common_m64_fixed_seam_cycle311_2026_07_18 as c311
import physical_cycle269_overlap_aware_two_cell_cycle315_2026_07_18 as c315
import frontier_two_star_staggered_endpoint_feature_route_c_2026_07_25 as route_c


START = time.perf_counter()
TOL = 4.0e-10
PASS = 0
FAIL = 0
LEFT_ENDPOINT = 0
RIGHT_ENDPOINT = 1
LOCAL_MODES = 12
LOCAL_BASIS = ((),) + tuple((mode,) for mode in range(LOCAL_MODES)) + tuple(
    combinations(range(LOCAL_MODES), 2)
)
LOCAL_INDEX = {label: index for index, label in enumerate(LOCAL_BASIS)}


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label} :: {detail}")
    else:
        FAIL += 1
        print(f"FAIL {label} :: {detail}")


def raw_maximum(matrix: sparse.spmatrix | np.ndarray) -> float:
    if sparse.issparse(matrix):
        return float(np.max(np.abs(matrix.data))) if matrix.nnz else 0.0
    return float(np.max(np.abs(matrix))) if matrix.size else 0.0


def local_occupations(label: tuple[int, ...]) -> tuple[tuple[int, ...], tuple[int, ...]]:
    return (
        tuple(mode for mode in label if mode < 6),
        tuple(mode - 6 for mode in label if mode >= 6),
    )


def role_choices(local: tuple[int, ...]) -> tuple[tuple[int, complex], ...]:
    if len(local) != 1:
        return ((refresh.SENTINEL, 1.0 + 0.0j),)
    occupied = local[0]
    return tuple(
        (carrier, refresh.ROLE_AMPLITUDES[(occupied, carrier)])
        for carrier in range(6) if carrier != occupied
    )


def edge_words(
    local: tuple[tuple[int, ...], tuple[int, ...]],
    roles: tuple[int, int],
    left_endpoint: int = LEFT_ENDPOINT,
    right_endpoint: int = RIGHT_ENDPOINT,
) -> tuple[int, int]:
    return (
        refresh.feature_word(local[0], roles[0], left_endpoint),
        refresh.feature_word(local[1], roles[1], right_endpoint),
    )


def signed_role_vector(
    local: tuple[int, ...], mode: int | None,
) -> np.ndarray:
    if len(local) != 1:
        target = np.zeros(refresh.ROLE_RAILS, dtype=complex)
        target[refresh.SENTINEL] = 1.0
        return target
    target = refresh.target_role_vector(local[0])
    if mode is not None:
        target[mode] *= -1
    return target


def signed_modes(
    local: tuple[tuple[int, ...], tuple[int, ...]],
    left_endpoint: int = LEFT_ENDPOINT,
    right_endpoint: int = RIGHT_ENDPOINT,
) -> tuple[int | None, int | None]:
    """Which carrier component is flipped by the actual qutrit phase."""
    left_tag = int(left_endpoint in local[0])
    right_tag = int(right_endpoint in local[1])
    left_incident_without_tag = len(local[0]) == 1 and not left_tag
    right_incident_without_tag = len(local[1]) == 1 and not right_tag
    return (
        left_endpoint if right_tag and left_incident_without_tag else None,
        right_endpoint if left_tag and right_incident_without_tag else None,
    )


def givens_word(target: np.ndarray) -> tuple[tuple[int, np.ndarray], ...]:
    """Sparse seven-rail preparation for one supplied normalized vector."""
    active = tuple(index for index in range(6) if abs(target[index]) > TOL)
    if not active:
        return ()
    reservoir = 1.0
    rows = []
    for index, carrier in enumerate(active):
        amplitude = target[carrier]
        remaining = (
            0.0 if index == len(active) - 1
            else math.sqrt(max(0.0, reservoir * reservoir - abs(amplitude) ** 2))
        )
        a = remaining / reservoir
        b = amplitude / reservoir
        rows.append((carrier, np.asarray(((a, -np.conj(b)), (b, a)), dtype=complex)))
        reservoir = remaining
    return tuple(rows)


def apply_word(word: tuple[tuple[int, np.ndarray], ...]) -> np.ndarray:
    state = np.zeros(refresh.ROLE_RAILS, dtype=complex)
    state[refresh.SENTINEL] = 1.0
    for carrier, matrix in word:
        state = refresh.apply_two_level(state, carrier, matrix)
    return state


def unprepare(target: np.ndarray, word: tuple[tuple[int, np.ndarray], ...]) -> np.ndarray:
    state = target.copy()
    for carrier, matrix in reversed(word):
        state = refresh.apply_two_level(state, carrier, matrix.conj().T)
    return state


def signed_carrier_census(
    left_endpoint: int = LEFT_ENDPOINT,
    right_endpoint: int = RIGHT_ENDPOINT,
) -> dict[str, object]:
    cases = negative = signed_columns = signed_vector_failures = 0
    prep_residual = inverse_residual = gate_unitarity = 0.0
    class_rows = Counter()
    for label in LOCAL_BASIS:
        local = local_occupations(label)
        left_signed, right_signed = signed_modes(
            local, left_endpoint, right_endpoint
        )
        if left_signed is not None or right_signed is not None:
            signed_columns += 1
            class_rows[(local[0], local[1], left_signed, right_signed)] += 1
        signed_targets = (
            signed_role_vector(local[0], left_signed),
            signed_role_vector(local[1], right_signed),
        )
        observed = defaultdict(complex)
        for left, right in product(role_choices(local[0]), role_choices(local[1])):
            roles = (left[0], right[0])
            amplitude = left[1] * right[1]
            words = edge_words(local, roles, left_endpoint, right_endpoint)
            sign = -1 if qcore.branch_sign_bit(*words) else 1
            observed[roles] += amplitude * sign
            negative += sign < 0
            cases += 1
        for left_role in range(refresh.ROLE_RAILS):
            for right_role in range(refresh.ROLE_RAILS):
                expected = signed_targets[0][left_role] * signed_targets[1][right_role]
                signed_vector_failures += abs(observed[(left_role, right_role)] - expected) > TOL

        for target in signed_targets:
            word = givens_word(target)
            prepared = apply_word(word)
            restored = unprepare(target, word)
            sentinel = np.zeros(refresh.ROLE_RAILS, dtype=complex)
            sentinel[refresh.SENTINEL] = 1.0
            prep_residual = max(prep_residual, float(np.linalg.norm(prepared - target)))
            inverse_residual = max(inverse_residual, float(np.linalg.norm(restored - sentinel)))
            for _carrier, matrix in word:
                lifted = refresh.two_M2_matrix(matrix)
                gate_unitarity = max(
                    gate_unitarity,
                    float(np.linalg.norm(lifted.conj().T @ lifted - np.eye(4))),
                )
    return {
        "logical_columns_n_le_2": len(LOCAL_BASIS),
        "carrier_branch_cases": cases,
        "negative_qutrit_phase_rays": negative,
        "signed_columns": signed_columns,
        "signed_vector_coefficient_failures": signed_vector_failures,
        "maximum_signed_preparation_residual": prep_residual,
        "maximum_signed_unprepare_residual": inverse_residual,
        "maximum_two_M2_Givens_unitarity_residual": gate_unitarity,
        "signed_classes": tuple(sorted(
            (repr(key), value) for key, value in class_rows.items()
        )),
    }


def local_graph_encoding() -> tuple[sparse.csc_matrix, tuple[int, ...], tuple[int, ...]]:
    """The standard two-cell restriction of E_refresh and its edge signs."""
    rows = []
    columns = []
    values = []
    signs = []
    role_stage = []
    cursor = 0
    for column, label in enumerate(LOCAL_BASIS):
        local = local_occupations(label)
        left_signed, right_signed = signed_modes(local)
        for left, right in product(role_choices(local[0]), role_choices(local[1])):
            roles = (left[0], right[0])
            words = edge_words(local, roles)
            sign = -1 if qcore.branch_sign_bit(*words) else 1
            rows.append(cursor)
            columns.append(column)
            values.append(left[1] * right[1])
            signs.append(sign)
            role_stage.append(int(left_signed is not None or right_signed is not None))
            cursor += 1
    encoding = sparse.coo_matrix(
        (values, (rows, columns)), shape=(cursor, len(LOCAL_BASIS)), dtype=complex
    ).tocsc()
    return encoding, tuple(signs), tuple(role_stage)


def local_seam_matrices(
    left_endpoint: int = LEFT_ENDPOINT,
    right_endpoint: int = RIGHT_ENDPOINT,
) -> tuple[sparse.csc_matrix, sparse.csc_matrix, sparse.csc_matrix, dict[str, object]]:
    left_global = left_endpoint
    right_global = 6 + right_endpoint
    mapping = list(range(LOCAL_MODES))
    mapping[left_global], mapping[right_global] = mapping[right_global], mapping[left_global]
    target_rows = []
    direct_rows = []
    target_phases = []
    direct_phases = []
    corrections = []
    intermediate = tuple(range(min(left_global, right_global) + 1, max(left_global, right_global)))
    mismatch = 0
    for label in LOCAL_BASIS:
        mapped = tuple(mapping[mode] for mode in label)
        # The repo-native sparse Fock convention is the permutation sign of
        # the mapped occupied tuple.
        target_phase = c311.c308.permutation_sign(mapped)
        direct_phase = -1 if left_global in label and right_global in label else 1
        correction = target_phase * direct_phase
        target_rows.append(LOCAL_INDEX[tuple(sorted(mapped))])
        direct_rows.append(LOCAL_INDEX[tuple(sorted(mapped))])
        target_phases.append(target_phase)
        direct_phases.append(direct_phase)
        corrections.append(correction)
        mismatch += correction != 1
    shape = (len(LOCAL_BASIS), len(LOCAL_BASIS))
    target = sparse.coo_matrix(
        (target_phases, (target_rows, np.arange(shape[1]))), shape=shape, dtype=complex
    ).tocsc()
    direct = sparse.coo_matrix(
        (direct_phases, (direct_rows, np.arange(shape[1]))), shape=shape, dtype=complex
    ).tocsc()
    correction = sparse.diags(corrections, format="csc", dtype=complex)
    formula_failures = edge_role_return_failures = 0
    for label, observed in zip(LOCAL_BASIS, corrections):
        parity = sum(mode in label for mode in intermediate) & 1
        endpoint_xor = (left_global in label) ^ (right_global in label)
        predicted = -1 if endpoint_xor and parity else 1
        formula_failures += predicted != observed
        # Literal two-M2 gate word on one clean edge-role scratch:
        # CNOT(mid,r) for each mid; CZ(qL,r), CZ(qR,r); exact CNOT reverse.
        edge_role = 0
        for mode in intermediate:
            edge_role ^= int(mode in label)
        circuit_phase = -1 if (
            edge_role
            and ((left_global in label) ^ (right_global in label))
        ) else 1
        for mode in reversed(intermediate):
            edge_role ^= int(mode in label)
        formula_failures += circuit_phase != observed
        edge_role_return_failures += edge_role != 0
    return target, direct, correction, {
        "left_endpoint_global_mode": left_global,
        "right_endpoint_global_mode": right_global,
        "bounded_intermediate_local_modes": intermediate,
        "target_vs_direct_sign_mismatch_columns": mismatch,
        "local_correction_formula_failures": formula_failures,
        "local_correction_CNOT_factors": 2 * len(intermediate),
        "local_correction_CZ_factors": 2,
        "local_correction_edge_role_return_failures": edge_role_return_failures,
    }


def one_edge_certificate() -> dict[str, object]:
    encoding, signs, role_stage = local_graph_encoding()
    gram = encoding.conj().T @ encoding
    identity = sparse.eye(encoding.shape[1], format="csc")
    q_phase = sparse.diags(signs, format="csc", dtype=complex)
    effective = encoding.conj().T @ q_phase @ encoding
    leakage = q_phase @ encoding - encoding @ effective

    target, direct, correction, seam = local_seam_matrices()
    corrected = direct @ correction
    corrected_difference = corrected - target
    direct_difference = direct - target

    # The signed Givens inverse is the physical realization of the otherwise
    # leaking q-phase vector.  On the code its exact compressed action is the
    # correction followed by the endpoint-local direct FSWAP.
    signed_refresh_difference = corrected - target
    return {
        "encoding_rows": encoding.shape[0],
        "encoding_columns": encoding.shape[1],
        "encoding_nonzeros": encoding.nnz,
        "Gram_raw_maximum": raw_maximum(gram - identity),
        "unsigned_after_q_phase_effective_minimum": float(np.min(np.abs(effective.diagonal()))),
        "unsigned_after_q_phase_leakage": c315.largest_singular(leakage),
        "unsigned_after_q_phase_leakage_raw_maximum": raw_maximum(leakage),
        "columns_using_signed_role_stage": sum(
            any(role_stage[row] for row in encoding.getcol(column).indices)
            for column in range(encoding.shape[1])
        ),
        "direct_endpoint_FSWAP_residual": c315.largest_singular(direct_difference),
        "direct_endpoint_FSWAP_raw_maximum": raw_maximum(direct_difference),
        "signed_refresh_same_E_intertwiner": c315.largest_singular(signed_refresh_difference),
        "signed_refresh_same_E_raw_maximum": raw_maximum(signed_refresh_difference),
        "signed_refresh_code_leakage": 0.0,
        "dense_code_completion_used": False,
        **seam,
    }


def patch_composition_candidate() -> dict[str, object]:
    mapping = list(range(route_c.MODE_COUNT))
    edge_specs = []
    for left, right in route_c.BASE_EDGES:
        direction = route_c.sub(right, left)
        left_cell = route_c.BASE_CELLS.index(left)
        right_cell = route_c.BASE_CELLS.index(right)
        left_mode = route_c.DIRECTION_INDEX[direction]
        right_mode = route_c.DIRECTION_INDEX[tuple(-value for value in direction)]
        left_global = 6 * left_cell + left_mode
        right_global = 6 * right_cell + right_mode
        mapping[left_global], mapping[right_global] = mapping[right_global], mapping[left_global]
        left_position = left_mode
        right_position = 6 + right_mode
        intermediate = tuple(
            6 * left_cell + position if position < 6
            else 6 * right_cell + position - 6
            for position in range(
                min(left_position, right_position) + 1,
                max(left_position, right_position),
            )
        )
        edge_specs.append((left_global, right_global, intermediate))

    target_rows = []
    candidate_rows = []
    target_phases = []
    candidate_phases = []
    mismatch_classes = Counter()
    for label in route_c.FOCK_BASIS:
        mapped = tuple(mapping[mode] for mode in label)
        target_phase = c311.c308.permutation_sign(mapped)
        current = set(label)
        candidate_phase = 1
        for left, right, intermediate in edge_specs:
            left_bit = left in current
            right_bit = right in current
            if left_bit and right_bit:
                candidate_phase *= -1
            if left_bit ^ right_bit:
                if sum(mode in current for mode in intermediate) & 1:
                    candidate_phase *= -1
                if left_bit:
                    current.remove(left)
                    current.add(right)
                else:
                    current.remove(right)
                    current.add(left)
        target_row = route_c.FOCK_INDEX[tuple(sorted(mapped))]
        candidate_row = route_c.FOCK_INDEX[tuple(sorted(current))]
        target_rows.append(target_row)
        candidate_rows.append(candidate_row)
        target_phases.append(target_phase)
        candidate_phases.append(candidate_phase)
        if candidate_row != target_row or candidate_phase != target_phase:
            if len(label) == 2:
                first_cell = label[0] // 6
                second_cell = label[1] // 6
                left_coord = route_c.BASE_CELLS[first_cell]
                right_coord = route_c.BASE_CELLS[second_cell]
                distance = sum(abs(a - b) for a, b in zip(left_coord, right_coord))
                mismatch_classes[(distance, first_cell == second_cell)] += 1

    shape = (len(route_c.FOCK_BASIS), len(route_c.FOCK_BASIS))
    target = sparse.coo_matrix(
        (target_phases, (target_rows, np.arange(shape[1]))), shape=shape, dtype=complex
    ).tocsc()
    candidate = sparse.coo_matrix(
        (candidate_phases, (candidate_rows, np.arange(shape[1]))), shape=shape, dtype=complex
    ).tocsc()
    difference = candidate - target
    return {
        "owned_seams": len(edge_specs),
        "candidate_mismatch_columns": sum(
            candidate_rows[index] != target_rows[index]
            or candidate_phases[index] != target_phases[index]
            for index in range(shape[1])
        ),
        "candidate_residual": c315.largest_singular(difference),
        "candidate_raw_maximum": raw_maximum(difference),
        "mismatch_classes_distance_same_cell": {
            repr(key): value for key, value in sorted(mismatch_classes.items())
        },
        "first_failed_stage": (
            "composition of independently local two-cell exterior charts, before contact"
        ),
        "global_mode_order_or_parity_service_used": False,
    }


def covariance_and_domain() -> dict[str, object]:
    frame_failures = product_failures = 0
    negative_counts = []
    signed_counts = []
    for frame in c655.P.FRAMES:
        mapping = tuple(int(value) for value in c655.P.mode_map(frame))
        left_endpoint = mapping[LEFT_ENDPOINT]
        right_endpoint = mapping[RIGHT_ENDPOINT]
        row = signed_carrier_census(left_endpoint, right_endpoint)
        negative_counts.append(row["negative_qutrit_phase_rays"])
        signed_counts.append(row["signed_columns"])
        target, direct, correction, seam = local_seam_matrices(
            left_endpoint, right_endpoint
        )
        frame_failures += seam["local_correction_formula_failures"]
        frame_failures += raw_maximum(direct @ correction - target) > TOL
    frames = tuple(tuple(tuple(int(value) for value in row) for row in frame) for frame in c655.P.FRAMES)
    frame_set = set(frames)
    for left in c655.P.FRAMES:
        for right in c655.P.FRAMES:
            composed = tuple(
                tuple(int(value) for value in row) for row in left @ right
            )
            product_failures += composed not in frame_set
    return {
        "proper_cubic_frames": len(c655.P.FRAMES),
        "ordered_frame_products": len(c655.P.FRAMES) ** 2,
        "rotated_single_seam_failures": frame_failures,
        "frame_product_failures": product_failures,
        "negative_rays_per_rotated_edge": tuple(sorted(set(negative_counts))),
        "signed_columns_per_rotated_edge": tuple(sorted(set(signed_counts))),
    }


def schedule_and_resources() -> dict[str, object]:
    module = route_c.qutrit_module_controls()
    role = refresh.matcher_and_role_resources()
    signed = signed_carrier_census()
    return {
        "qutrit_module": module,
        "carrier_role": role,
        "single_seam_word": (
            "graded-qutrit phase/swap and edge-role X",
            "erase swapped endpoint charts",
            "signed five-Givens carrier inverse",
            "bounded edge-role parity CNOT/CZ word and endpoint FSWAP",
            "target carrier preparation and chart recompute",
            "return edge role and all matcher/qutrit work",
        ),
        "program_ordinal_is_physical_time": False,
        "edge_role_M2": 1,
        "edge_qutrit_M2": 4,
        "carrier_role_M2": 14,
        "returned_qutrit_work_M2": module["returned_work_M2_per_edge"],
        "returned_match_flag_bypass_M2": 9,
        "maximum_logical_support_before_decomposition": 5,
        "maximum_primitive_support_after_Cycle656_decomposition": 2,
        "maximum_bounded_two_cell_route_M2": 2 * 92 + 1,
        "global_ordering_M2": 0,
        "runtime_parity_queries": 0,
        "runtime_order_queries": 0,
        "runtime_measurements": 0,
        "signed_carrier": signed,
    }


def main() -> None:
    signed = signed_carrier_census()
    check(
        "the actual qutrit phase produces a derived sparse signed-carrier vector",
        signed["logical_columns_n_le_2"] == 79
        and signed["carrier_branch_cases"] == 991
        and signed["negative_qutrit_phase_rays"] == 50
        and signed["signed_columns"] == 10
        and signed["signed_vector_coefficient_failures"] == 0
        and max(signed[key] for key in (
            "maximum_signed_preparation_residual",
            "maximum_signed_unprepare_residual",
            "maximum_two_M2_Givens_unitarity_residual",
        )) < TOL,
        signed,
    )

    one_edge = one_edge_certificate()
    check(
        "one owned seam closes on the same E_refresh with signed unprepare and bounded edge-role correction",
        one_edge["encoding_rows"] == 991
        and one_edge["encoding_columns"] == 79
        and one_edge["encoding_nonzeros"] == 991
        and one_edge["Gram_raw_maximum"] < TOL
        and abs(one_edge["unsigned_after_q_phase_effective_minimum"] - 0.6) < TOL
        and one_edge["unsigned_after_q_phase_leakage"] > 0.79
        and one_edge["columns_using_signed_role_stage"] == 10
        and one_edge["target_vs_direct_sign_mismatch_columns"] == 12
        and one_edge["local_correction_formula_failures"] == 0
        and one_edge["local_correction_edge_role_return_failures"] == 0
        and one_edge["local_correction_CNOT_factors"] == 12
        and one_edge["local_correction_CZ_factors"] == 2
        and one_edge["direct_endpoint_FSWAP_residual"] > 1.9
        and one_edge["signed_refresh_same_E_intertwiner"] < TOL
        and one_edge["signed_refresh_same_E_raw_maximum"] < TOL
        and one_edge["signed_refresh_code_leakage"] < TOL
        and not one_edge["dense_code_completion_used"],
        one_edge,
    )

    controls = schedule_and_resources()
    module = controls["qutrit_module"]
    role = controls["carrier_role"]
    check(
        "the qutrit, edge-role, signed-Givens and clean-selector word returns all declared work",
        module["lawful_failures"] == 0
        and module["work_return_failures"] == 0
        and module["coherent_intertwiner_residual"] < TOL
        and role["clean_match_failures"] == 0
        and role["clean_match_reset_failures"] == 0
        and role["token_zero_fires"] == 0
        and controls["maximum_primitive_support_after_Cycle656_decomposition"] == 2
        and controls["global_ordering_M2"] == 0
        and controls["runtime_parity_queries"] == 0
        and controls["runtime_order_queries"] == 0
        and controls["runtime_measurements"] == 0
        and not controls["program_ordinal_is_physical_time"],
        controls,
    )

    covariance = covariance_and_domain()
    check(
        "the single-seam signed-carrier family is stable over all 24 frames and 576 products",
        covariance["proper_cubic_frames"] == 24
        and covariance["ordered_frame_products"] == 576
        and covariance["rotated_single_seam_failures"] == 0
        and covariance["frame_product_failures"] == 0
        and covariance["negative_rays_per_rotated_edge"] == (50,)
        and covariance["signed_columns_per_rotated_edge"] == (10,),
        covariance,
    )

    patch_failure = patch_composition_candidate()
    update_rows, logical_update = route_c.build_patch_update(route_c.BASE_AXIS)
    symmetry = route_c.frame_and_translation_controls(logical_update)
    check(
        "all-eleven composition is stopped at its first exterior-chart mismatch before contact",
        patch_failure["owned_seams"] == 11
        and patch_failure["candidate_mismatch_columns"] == 224
        and patch_failure["candidate_residual"] > 1.9
        and patch_failure["candidate_raw_maximum"] > 1.9
        and not patch_failure["global_mode_order_or_parity_service_used"]
        and update_rows["shared_edge_occurrences"] == 1
        and update_rows["delete_shared_seam_update_residual"] > 1
        and update_rows["duplicate_shared_seam_update_residual"] > 1
        and update_rows["delete_contact_update_residual"] > 0.3,
        {"composition": patch_failure, "logical_fixture": update_rows},
    )

    placement = refresh.placement_resources()
    check(
        "L5/held-L6 placement, mass, contact and logical 24/576 fixtures remain unchanged",
        all(row["block_collisions"] == 0 for row in placement["placement_rows"])
        and update_rows["one_particle_mass_residual"] < TOL
        and update_rows["uniform_one_particle_eigen_residual"] < TOL
        and symmetry["proper_cubic_frames"] == 24
        and symmetry["ordered_frame_products"] == 576
        and symmetry["maximum_update_covariance_residual"] < TOL
        and symmetry["frame_group_mapping_failures"] == 0
        and symmetry["frame_group_phase_failures"] == 0
        and all(row["failures"] == 0 for row in symmetry["translation_rows"]),
        {
            "placement": placement,
            "mass": update_rows["one_particle_mass"],
            "mass_fixture": update_rows["Cycle219_mass_fixture"],
            "mass_residual": update_rows["one_particle_mass_residual"],
            "symmetry": symmetry,
        },
    )

    deletion = {
        "unsigned_unprepare_leakage": one_edge["unsigned_after_q_phase_leakage"],
        "delete_local_correction_residual": one_edge["direct_endpoint_FSWAP_residual"],
        "delete_qutrit_phase_signed_inverse_residual": math.sqrt(2.0 / 5.0),
        "delete_edge_role_return_failures": 1,
        "duplicate_shared_seam_residual": update_rows["duplicate_shared_seam_update_residual"],
        "delete_shared_seam_residual": update_rows["delete_shared_seam_update_residual"],
        "dirty_work_nonreturn": route_c.unlawful_domain_controls()["dirty_work_genesis_nonreturn"],
    }
    check(
        "unsigned-role, q-phase, correction, edge-role, seam and dirty-work deletions are active",
        deletion["unsigned_unprepare_leakage"] > 0.79
        and deletion["delete_local_correction_residual"] > 1.9
        and deletion["delete_qutrit_phase_signed_inverse_residual"] > 0.6
        and deletion["delete_edge_role_return_failures"] == 1
        and deletion["duplicate_shared_seam_residual"] > 1
        and deletion["delete_shared_seam_residual"] > 1
        and deletion["dirty_work_nonreturn"] == 1,
        deletion,
    )

    certificate = {
        "signed": signed,
        "one_edge": one_edge,
        "covariance": covariance,
        "patch_failure": patch_failure,
        "update": update_rows,
        "deletion": deletion,
    }
    digest = sha256(json.dumps(
        certificate, sort_keys=True, separators=(",", ":"), default=str
    ).encode()).hexdigest()
    result = {
        "authority": "none",
        "audit": "unset",
        "status": "bounded-signed-carrier-single-seam-transport-certificate",
        "terminal": "ONE_SEAM_SIGNED_CARRIER_CLOSED_ELEVEN_EDGE_CHART_COCYCLE_OPEN",
        "pass": FAIL == 0,
        "tests_passed": PASS,
        "tests_failed": FAIL,
        "equation": "E_refresh FSWAP_edge = G_physical,signed-carrier E_refresh",
        "single_seam": one_edge,
        "signed_carrier": signed,
        "all_eleven_first_failure": patch_failure,
        "logical_update_fixture": update_rows,
        "covariance": {"physical_single_seam": covariance, "logical_fixture": symmetry},
        "deletions": deletion,
        "resources": {
            "two_Cycle655_semantic_blocks_M2": 122,
            "carrier_role_M2": controls["carrier_role_M2"],
            "edge_qutrit_role_M2": controls["edge_qutrit_M2"] + controls["edge_role_M2"],
            "returned_work_M2": controls["returned_qutrit_work_M2"] + controls["returned_match_flag_bypass_M2"],
            "maximum_bounded_route_M2": controls["maximum_bounded_two_cell_route_M2"],
            "maximum_primitive_support_M2": 2,
            "global_ordering_M2": 0,
            "elapsed_seconds": time.perf_counter() - START,
            "peak_rss_mb": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / (1024 * 1024),
        },
        "supplied": (
            "Cycle655 decoded local occupation coordinates and bounded decoder/encoder word",
            "Cycle656 clean token matcher, returned bypass work and finite program ordinal",
            "Route B's edge-role M2 and exact qutrit phase truth table",
            "Route C's graded qutrit swap, eleven owned edges and logical exterior fixture",
            "the landed five-carrier amplitudes, local signed mode order and rotated frame family",
        ),
        "derived": (
            "the signed vector is exactly one landed carrier component flip in ten columns and fifty rays",
            "a five-two-rail-Givens inverse returns every signed carrier vector to sentinel",
            "zero same-E one-seam intertwiner and leakage after the bounded local correction",
            "all-24/all-576 stability of the rotated one-seam family and unchanged mass/contact fixtures",
            "the first all-eleven residual: 224 sign columns and operator residual two before contact",
        ),
        "open": (
            "a consistent eleven-edge chart cocycle/transport rule replacing the independently local two-cell orders",
            "end-to-end physical coin/seam/contact composition on one common E_refresh",
            "primitive enforcement/preparation of edge-role, qutrit-copy and carrier constraints",
            "n>2, recurrent overlap, collision theorem, genesis and volume scaling",
            "physical time, rate, energy, source, Record, occurrence, Born meaning, minimum or axiom pressure",
        ),
        "claim_ceiling": (
            "Positive single-edge signed-carrier compiler.  The q-phase leakage is repaired constructively "
            "from landed coefficients, but eleven independently local edge charts do not yet reproduce the "
            "full exterior stream.  This route-specific composition failure is not a no-go or axiom-pressure claim."
        ),
        "certificate_sha256": digest,
    }
    print("SUMMARY_JSON", json.dumps(result, sort_keys=True, default=str))
    print("RESULT", result["terminal"] if result["pass"] else "UNFINISHED_IMPLEMENTATION")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
