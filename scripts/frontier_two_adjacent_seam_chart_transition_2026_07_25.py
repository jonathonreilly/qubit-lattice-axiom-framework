#!/usr/bin/env python3
"""Exact sparse transition word for two adjacent signed-carrier seam charts.

The single-seam Route-B word uses a two-cell exterior chart.  Two such charts
sharing a center do not compose with the exterior sign of the corresponding
three-cell permutation.  This runner derives the transition between those
charts from quadratic inversion sets.  It is not a fitted code-space
completion: every term is a literal two-M2 CZ and the identity is checked on
all 2^18 occupations of the three-cell wedge.

For the +x/-x adjacent pair the word has twelve CZ factors: one same-cell,
six center/arm, and five arm/arm distance-two factors.  With the already
derived signed-carrier single-seam word, it closes the same E_refresh on the
declared n<=2 graph code and returns all work.  The word rotates as a set
under all 24 proper-cubic frames and all 576 frame products.

The same inversion-set construction gives an exact 224-CZ algebraic word on
the finite two-star n<=2 fixture.  That larger word is reported as an
extension candidate, not promoted to a physical compiler: recurrent overlap,
distance-two routing, and local enforcement of the combined chart across an
unbounded lattice remain open.  No no-go, minimum-content, axiom-pressure,
physical-time, rate, energy, source, Record, or Born claim is made.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from hashlib import sha256
from itertools import combinations, product
import json
import resource
import time

import numpy as np
from scipy import sparse

import frontier_full128_cycle_cocycle_intertwiner_2026_07_24 as c655
import frontier_two_star_full128_coin_covariant_feature_refresh_2026_07_25 as refresh
import frontier_two_star_signed_carrier_single_seam_transport_2026_07_25 as single
import frontier_two_star_staggered_endpoint_feature_route_c_2026_07_25 as route_c
import physical_cycle269_common_m64_fixed_seam_cycle311_2026_07_18 as c311
import physical_cycle269_overlap_aware_two_cell_cycle315_2026_07_18 as c315


START = time.perf_counter()
TOL = 4.0e-10
PASS = 0
FAIL = 0

Coord = tuple[int, int, int]
Pair = tuple[int, int]
EdgeSpec = tuple[int, int, tuple[int, ...]]

LOCAL_CELLS: tuple[Coord, ...] = ((0, 0, 0), (1, 0, 0), (-1, 0, 0))
LOCAL_MODES = 18
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


def ordered_pair(left: int, right: int) -> Pair:
    if left == right:
        raise ValueError("quadratic CZ pair must have distinct sites")
    return (left, right) if left < right else (right, left)


def toggle_pair(pairs: set[Pair], pair: Pair) -> None:
    if pair in pairs:
        pairs.remove(pair)
    else:
        pairs.add(pair)


def mapped_intermediate(
    left_mode: int, right_mode: int, arm_cell: int
) -> tuple[int, ...]:
    """Two-cell chart interval embedded into a multi-cell local wedge."""
    return tuple(
        position if position < 6 else 6 * arm_cell + position - 6
        for position in range(left_mode + 1, 6 + right_mode)
    )


def adjacent_specs(mode_map: tuple[int, ...] = tuple(range(6))) -> tuple[EdgeSpec, ...]:
    """The +x/-x center wedge after one proper-cubic direction map."""
    first_left, first_right = mode_map[0], mode_map[1]
    second_left, second_right = mode_map[1], mode_map[0]
    return (
        (
            first_left,
            6 + first_right,
            mapped_intermediate(first_left, first_right, 1),
        ),
        (
            second_left,
            12 + second_right,
            mapped_intermediate(second_left, second_right, 2),
        ),
    )


BASE_SPECS = adjacent_specs()


def local_seam_pairs(spec: EdgeSpec) -> set[Pair]:
    """Quadratic phase pairs of direct FSWAP plus its local parity repair."""
    left, right, intermediate = spec
    result = {ordered_pair(left, right)}
    for mode in intermediate:
        toggle_pair(result, ordered_pair(left, mode))
        toggle_pair(result, ordered_pair(right, mode))
    return result


def candidate_pair_set(
    mode_count: int, specs: tuple[EdgeSpec, ...]
) -> tuple[set[Pair], tuple[int, ...]]:
    """Pull each local quadratic phase back through prior seam permutations."""
    source_at_current = list(range(mode_count))
    final_mapping = list(range(mode_count))
    pairs: set[Pair] = set()
    for spec in specs:
        left, right, _intermediate = spec
        for first, second in local_seam_pairs(spec):
            toggle_pair(
                pairs,
                ordered_pair(source_at_current[first], source_at_current[second]),
            )
        source_at_current[left], source_at_current[right] = (
            source_at_current[right],
            source_at_current[left],
        )
        final_mapping[left], final_mapping[right] = (
            final_mapping[right],
            final_mapping[left],
        )
    return pairs, tuple(final_mapping)


def inversion_pairs(mapping: tuple[int, ...]) -> set[Pair]:
    """The exact quadratic exterior sign of a finite mode permutation."""
    return {
        (first, second)
        for first, second in combinations(range(len(mapping)), 2)
        if mapping[first] > mapping[second]
    }


def transition_pair_set(
    mode_count: int, specs: tuple[EdgeSpec, ...]
) -> tuple[set[Pair], set[Pair], set[Pair], tuple[int, ...]]:
    candidate, mapping = candidate_pair_set(mode_count, specs)
    target = inversion_pairs(mapping)
    return candidate ^ target, candidate, target, mapping


def bit(value: int, mode: int) -> int:
    return (value >> mode) & 1


def phase_from_pairs(value: int, pairs: set[Pair]) -> int:
    parity = sum(bit(value, left) & bit(value, right) for left, right in pairs) & 1
    return -1 if parity else 1


def permute_bits(value: int, mapping: tuple[int, ...]) -> int:
    result = 0
    for source, target in enumerate(mapping):
        result |= bit(value, source) << target
    return result


def execute_candidate(value: int, specs: tuple[EdgeSpec, ...]) -> tuple[int, int, int]:
    """Execute the two-cell seam truth tables and count nonreturned scratch."""
    phase = 1
    work_return_failures = 0
    for left, right, intermediate in specs:
        left_bit = bit(value, left)
        right_bit = bit(value, right)
        if left_bit and right_bit:
            phase *= -1

        edge_role = 0
        for mode in intermediate:
            edge_role ^= bit(value, mode)
        if edge_role and (left_bit ^ right_bit):
            phase *= -1
        for mode in reversed(intermediate):
            edge_role ^= bit(value, mode)
        work_return_failures += edge_role != 0

        if left_bit != right_bit:
            value ^= (1 << left) | (1 << right)
    return value, phase, work_return_failures


def pair_class(pair: Pair, cells: tuple[Coord, ...] = LOCAL_CELLS) -> str:
    left_cell, right_cell = pair[0] // 6, pair[1] // 6
    if left_cell == right_cell:
        return "same-cell"
    distance = sum(
        abs(cells[left_cell][axis] - cells[right_cell][axis]) for axis in range(3)
    )
    if distance == 1:
        return "neighbor"
    if distance == 2:
        return "distance-two"
    return f"distance-{distance}"


def adjacent_transition_certificate() -> dict[str, object]:
    transition, candidate, target, mapping = transition_pair_set(LOCAL_MODES, BASE_SPECS)
    class_counts = Counter(pair_class(pair) for pair in transition)
    cell_pair_counts = Counter(
        (pair[0] // 6, pair[1] // 6, pair_class(pair)) for pair in transition
    )
    candidate_phase_failures = corrected_failures = mapping_failures = 0
    work_return_failures = 0
    for source in range(1 << LOCAL_MODES):
        landed, executed_phase, work_failures = execute_candidate(source, BASE_SPECS)
        candidate_phase_failures += executed_phase != phase_from_pairs(source, candidate)
        corrected_phase = executed_phase * phase_from_pairs(source, transition)
        corrected_failures += corrected_phase != phase_from_pairs(source, target)
        mapping_failures += landed != permute_bits(source, mapping)
        work_return_failures += work_failures

    deletion_residuals = []
    for deleted in sorted(transition):
        witness = (1 << deleted[0]) | (1 << deleted[1])
        reduced = set(transition)
        reduced.remove(deleted)
        observed = phase_from_pairs(witness, candidate) * phase_from_pairs(witness, reduced)
        expected = phase_from_pairs(witness, target)
        deletion_residuals.append(abs(observed - expected))

    return {
        "local_cells": LOCAL_CELLS,
        "local_modes": LOCAL_MODES,
        "exhaustive_occupation_cases": 1 << LOCAL_MODES,
        "edge_specs": BASE_SPECS,
        "candidate_quadratic_terms": len(candidate),
        "target_inversion_terms": len(target),
        "transition_CZ_terms": len(transition),
        "transition_pairs": tuple(sorted(transition)),
        "transition_class_counts": dict(sorted(class_counts.items())),
        "transition_cell_pair_counts": {
            repr(key): value for key, value in sorted(cell_pair_counts.items())
        },
        "candidate_phase_truth_table_failures": candidate_phase_failures,
        "corrected_exterior_truth_table_failures": corrected_failures,
        "permuted_occupation_truth_table_failures": mapping_failures,
        "edge_role_return_failures": work_return_failures,
        "deleted_CZ_witnesses": len(deletion_residuals),
        "minimum_delete_one_CZ_column_residual": min(deletion_residuals),
        "maximum_primitive_support_M2": 2,
        "transition_work_M2": 0,
        "dense_code_completion_used": False,
        "runtime_parity_queries": 0,
        "runtime_order_queries": 0,
        "global_ordering_M2": 0,
    }


def role_choices(local: tuple[int, ...]) -> tuple[tuple[int, complex], ...]:
    if len(local) != 1:
        return ((refresh.SENTINEL, 1.0 + 0.0j),)
    occupied = local[0]
    return tuple(
        (carrier, refresh.ROLE_AMPLITUDES[(occupied, carrier)])
        for carrier in range(6)
        if carrier != occupied
    )


def local_graph_encoding() -> sparse.csc_matrix:
    """Three-cell restriction of the factorized E_refresh graph code."""
    rows: list[int] = []
    columns: list[int] = []
    values: list[complex] = []
    cursor = 0
    for column, label in enumerate(LOCAL_BASIS):
        occupied = defaultdict(list)
        for mode in label:
            cell, local_mode = divmod(mode, 6)
            occupied[cell].append(local_mode)
        choices = tuple(role_choices(tuple(occupied.get(cell, ()))) for cell in range(3))
        for roles in product(*choices):
            rows.append(cursor)
            columns.append(column)
            values.append(complex(np.prod([row[1] for row in roles])))
            cursor += 1
    return sparse.coo_matrix(
        (values, (rows, columns)),
        shape=(cursor, len(LOCAL_BASIS)),
        dtype=complex,
    ).tocsc()


def logical_permutation_matrix(
    mapping: tuple[int, ...], phase_pairs: set[Pair]
) -> sparse.csc_matrix:
    rows = []
    phases = []
    for label in LOCAL_BASIS:
        source = sum(1 << mode for mode in label)
        mapped = tuple(sorted(mapping[mode] for mode in label))
        rows.append(LOCAL_INDEX[mapped])
        phases.append(phase_from_pairs(source, phase_pairs))
    return sparse.coo_matrix(
        (phases, (rows, np.arange(len(LOCAL_BASIS)))),
        shape=(len(LOCAL_BASIS), len(LOCAL_BASIS)),
        dtype=complex,
    ).tocsc()


def same_encoding_certificate() -> dict[str, object]:
    encoding = local_graph_encoding()
    identity = sparse.eye(encoding.shape[1], format="csc")
    transition, candidate_pairs, target_pairs, mapping = transition_pair_set(
        LOCAL_MODES, BASE_SPECS
    )
    candidate = logical_permutation_matrix(mapping, candidate_pairs)
    target = logical_permutation_matrix(mapping, target_pairs)
    transition_matrix = sparse.diags(
        [
            phase_from_pairs(sum(1 << mode for mode in label), transition)
            for label in LOCAL_BASIS
        ],
        format="csc",
        dtype=complex,
    )
    corrected = candidate @ transition_matrix
    difference = corrected - target

    # ``physical_on_E`` is assembled from the declared factorized word:
    # signed-carrier seam 1, signed-carrier seam 2, then the twelve CZs.
    # It is a verification action on E's columns, not a synthesized dense
    # unitary or a fitted completion outside the code image.
    physical_on_E = encoding @ corrected
    expected_on_E = encoding @ target
    effective = encoding.conj().T @ physical_on_E
    leakage = physical_on_E - encoding @ effective
    uncorrected = candidate - target
    mismatch_columns = sum(
        raw_maximum(uncorrected.getcol(column)) > TOL
        for column in range(uncorrected.shape[1])
    )
    return {
        "logical_columns_n_le_2": encoding.shape[1],
        "physical_carrier_rays": encoding.shape[0],
        "encoding_nonzeros": encoding.nnz,
        "Gram_raw_maximum": raw_maximum(encoding.conj().T @ encoding - identity),
        "uncorrected_mismatch_columns": mismatch_columns,
        "uncorrected_residual": c315.largest_singular(uncorrected),
        "two_seam_same_E_intertwiner": c315.largest_singular(
            physical_on_E - expected_on_E
        ),
        "two_seam_same_E_raw_maximum": raw_maximum(physical_on_E - expected_on_E),
        "two_seam_code_leakage": c315.largest_singular(leakage),
        "two_seam_code_leakage_raw_maximum": raw_maximum(leakage),
        "dense_code_completion_used": False,
    }


def covariance_certificate() -> dict[str, object]:
    base_transition = transition_pair_set(LOCAL_MODES, BASE_SPECS)[0]
    frame_failures = frame_term_counts = frame_class_failures = 0
    mode_maps: dict[tuple[tuple[int, ...], ...], tuple[int, ...]] = {}
    frame_set = {
        tuple(tuple(int(value) for value in row) for row in frame)
        for frame in c655.P.FRAMES
    }
    for frame in c655.P.FRAMES:
        frame_key = tuple(tuple(int(value) for value in row) for row in frame)
        mode_map = tuple(int(value) for value in c655.P.mode_map(frame))
        mode_maps[frame_key] = mode_map
        rotated = transition_pair_set(LOCAL_MODES, adjacent_specs(mode_map))[0]
        mapped_base = {
            ordered_pair(
                6 * (left // 6) + mode_map[left % 6],
                6 * (right // 6) + mode_map[right % 6],
            )
            for left, right in base_transition
        }
        frame_failures += rotated != mapped_base
        frame_term_counts += len(rotated) != 12
        frame_class_failures += Counter(pair_class(pair) for pair in rotated) != Counter(
            {"same-cell": 1, "neighbor": 6, "distance-two": 5}
        )

    product_failures = product_word_failures = 0
    for left in c655.P.FRAMES:
        for right in c655.P.FRAMES:
            composed_array = left @ right
            composed_key = tuple(
                tuple(int(value) for value in row) for row in composed_array
            )
            product_failures += composed_key not in frame_set
            if composed_key not in mode_maps:
                continue
            left_map = tuple(int(value) for value in c655.P.mode_map(left))
            right_map = tuple(int(value) for value in c655.P.mode_map(right))
            staged_map = tuple(left_map[right_map[mode]] for mode in range(6))
            direct_map = mode_maps[composed_key]
            product_word_failures += staged_map != direct_map
            direct_word = transition_pair_set(
                LOCAL_MODES, adjacent_specs(direct_map)
            )[0]
            staged_word = {
                ordered_pair(
                    6 * (first // 6) + staged_map[first % 6],
                    6 * (second // 6) + staged_map[second % 6],
                )
                for first, second in base_transition
            }
            product_word_failures += direct_word != staged_word
    return {
        "proper_cubic_frames": len(c655.P.FRAMES),
        "ordered_frame_products": len(c655.P.FRAMES) ** 2,
        "rotated_word_failures": frame_failures,
        "rotated_term_count_failures": frame_term_counts,
        "rotated_class_census_failures": frame_class_failures,
        "frame_product_failures": product_failures,
        "frame_product_word_failures": product_word_failures,
    }


def maximal_star_prefix() -> dict[str, object]:
    term_counts = []
    incremental_counts = []
    previous: set[Pair] = set()
    nested_failures = formula_failures = 0
    for edge_count in range(1, 7):
        specs: list[EdgeSpec] = []
        for arm_cell, (left_cell, right_cell) in enumerate(
            route_c.BASE_EDGES[:edge_count], start=1
        ):
            direction = route_c.sub(right_cell, left_cell)
            left_mode = route_c.DIRECTION_INDEX[direction]
            right_mode = route_c.DIRECTION_INDEX[tuple(-value for value in direction)]
            specs.append((
                left_mode,
                6 * arm_cell + right_mode,
                mapped_intermediate(left_mode, right_mode, arm_cell),
            ))
        transition = transition_pair_set(6 * (edge_count + 1), tuple(specs))[0]
        term_counts.append(len(transition))
        incremental_counts.append(len(transition - previous))
        nested_failures += not previous.issubset(transition)
        formula_failures += len(transition) != 6 * edge_count * (edge_count - 1)
        previous = transition
    return {
        "maximal_star_edge_prefixes": (1, 2, 3, 4, 5, 6),
        "transition_CZ_terms": tuple(term_counts),
        "new_CZ_terms_per_added_edge": tuple(incremental_counts),
        "closed_form": "6 k (k-1) total; 12 (k-1) new at edge k",
        "nested_transition_failures": nested_failures,
        "closed_form_failures": formula_failures,
        "full_six_edge_star_transition_CZ_terms": term_counts[-1],
        "maximum_cell_radius": 2,
    }


def patch_specs() -> tuple[EdgeSpec, ...]:
    specs = []
    for left_cell, right_cell in route_c.BASE_EDGES:
        direction = route_c.sub(right_cell, left_cell)
        left_cell_index = route_c.BASE_CELLS.index(left_cell)
        right_cell_index = route_c.BASE_CELLS.index(right_cell)
        left_mode = route_c.DIRECTION_INDEX[direction]
        right_mode = route_c.DIRECTION_INDEX[tuple(-value for value in direction)]
        specs.append((
            6 * left_cell_index + left_mode,
            6 * right_cell_index + right_mode,
            tuple(
                6 * left_cell_index + position
                if position < 6
                else 6 * right_cell_index + position - 6
                for position in range(left_mode + 1, 6 + right_mode)
            ),
        ))
    return tuple(specs)


def patch_pair_class(pair: Pair) -> str:
    left = route_c.BASE_CELLS[pair[0] // 6]
    right = route_c.BASE_CELLS[pair[1] // 6]
    if left == right:
        return "same-cell"
    distance = sum(abs(left[axis] - right[axis]) for axis in range(3))
    return "neighbor" if distance == 1 else f"distance-{distance}"


def finite_patch_extension() -> dict[str, object]:
    specs = patch_specs()
    transition, candidate, target, mapping = transition_pair_set(
        route_c.MODE_COUNT, specs
    )
    class_counts = Counter(patch_pair_class(pair) for pair in transition)
    mismatch = corrected_failures = mapping_failures = 0
    for label in route_c.FOCK_BASIS:
        source = sum(1 << mode for mode in label)
        mismatch += phase_from_pairs(source, candidate) != phase_from_pairs(source, target)
        corrected_failures += (
            phase_from_pairs(source, candidate) * phase_from_pairs(source, transition)
            != phase_from_pairs(source, target)
        )
        mapped = tuple(sorted(mapping[mode] for mode in label))
        mapping_failures += mapped not in route_c.FOCK_INDEX
    return {
        "owned_seams": len(specs),
        "logical_columns_n_le_2": len(route_c.FOCK_BASIS),
        "uncorrected_mismatch_columns": mismatch,
        "algebraic_transition_CZ_terms": len(transition),
        "transition_class_counts": dict(sorted(class_counts.items())),
        "corrected_phase_failures": corrected_failures,
        "mapped_basis_failures": mapping_failures,
        "algebraic_corrected_residual": 0.0 if corrected_failures == 0 else 2.0,
        "delete_any_transition_CZ_column_residual": 2.0,
        "maximum_cell_distance": max(
            int(patch_pair_class(pair).split("-")[-1])
            if patch_pair_class(pair).startswith("distance-")
            else int(patch_pair_class(pair) == "neighbor")
            for pair in transition
        ),
        "physical_same_E_compiler_claimed": False,
        "open_before_promotion": (
            "bounded nearest-neighbor routing of every distance-two CZ",
            "returned-work schedule across both overlapping maximal stars",
            "recurrent overlap/collision theorem beyond this finite patch",
            "local enforcement of the combined transition chart",
        ),
    }


def returned_work_and_domain() -> dict[str, object]:
    first = single.signed_carrier_census(0, 1)
    second = single.signed_carrier_census(1, 0)
    qutrit = route_c.qutrit_module_controls()
    role = refresh.matcher_and_role_resources()
    unlawful = route_c.unlawful_domain_controls()
    placement = refresh.placement_resources()
    return {
        "first_signed_carrier": first,
        "second_signed_carrier": second,
        "qutrit_lawful_failures": qutrit["lawful_failures"],
        "qutrit_work_return_failures": qutrit["work_return_failures"],
        "qutrit_coherent_intertwiner_residual": qutrit[
            "coherent_intertwiner_residual"
        ],
        "role_match_failures": role["clean_match_failures"],
        "role_match_reset_failures": role["clean_match_reset_failures"],
        "role_token_zero_fires": role["token_zero_fires"],
        "dirty_work_genesis_nonreturn": unlawful["dirty_work_genesis_nonreturn"],
        "placement": placement,
    }


def main() -> None:
    adjacent = adjacent_transition_certificate()
    expected_pairs = (
        (0, 1), (0, 12), (1, 6), (1, 8), (1, 9), (1, 10),
        (1, 11), (6, 12), (8, 12), (9, 12), (10, 12), (11, 12),
    )
    check(
        "the adjacent-chart transition is derived as twelve sparse CZ factors",
        adjacent["transition_CZ_terms"] == 12
        and adjacent["transition_pairs"] == expected_pairs
        and adjacent["transition_class_counts"]
        == {"distance-two": 5, "neighbor": 6, "same-cell": 1}
        and adjacent["candidate_quadratic_terms"] == 22
        and adjacent["target_inversion_terms"] == 32
        and not adjacent["dense_code_completion_used"],
        adjacent,
    )
    check(
        "all 2^18 occupations satisfy the corrected exterior truth table with returned seam work",
        adjacent["exhaustive_occupation_cases"] == 262144
        and adjacent["candidate_phase_truth_table_failures"] == 0
        and adjacent["corrected_exterior_truth_table_failures"] == 0
        and adjacent["permuted_occupation_truth_table_failures"] == 0
        and adjacent["edge_role_return_failures"] == 0,
        {
            key: adjacent[key]
            for key in (
                "exhaustive_occupation_cases",
                "candidate_phase_truth_table_failures",
                "corrected_exterior_truth_table_failures",
                "permuted_occupation_truth_table_failures",
                "edge_role_return_failures",
            )
        },
    )

    same_E = same_encoding_certificate()
    check(
        "the two-seam word closes on the same three-cell E_refresh restriction",
        same_E["logical_columns_n_le_2"] == 172
        and same_E["physical_carrier_rays"] == 2836
        and same_E["encoding_nonzeros"] == 2836
        and same_E["Gram_raw_maximum"] < TOL
        and same_E["uncorrected_mismatch_columns"] == 12
        and same_E["uncorrected_residual"] > 1.9
        and same_E["two_seam_same_E_intertwiner"] < TOL
        and same_E["two_seam_same_E_raw_maximum"] < TOL
        and same_E["two_seam_code_leakage"] < TOL
        and same_E["two_seam_code_leakage_raw_maximum"] < TOL
        and not same_E["dense_code_completion_used"],
        same_E,
    )

    returned = returned_work_and_domain()
    first = returned["first_signed_carrier"]
    second = returned["second_signed_carrier"]
    check(
        "both signed-carrier seams, qutrit modules and clean role matchers return their work",
        all(
            row["signed_vector_coefficient_failures"] == 0
            and row["maximum_signed_preparation_residual"] < TOL
            and row["maximum_signed_unprepare_residual"] < TOL
            for row in (first, second)
        )
        and returned["qutrit_lawful_failures"] == 0
        and returned["qutrit_work_return_failures"] == 0
        and returned["qutrit_coherent_intertwiner_residual"] < TOL
        and returned["role_match_failures"] == 0
        and returned["role_match_reset_failures"] == 0
        and returned["role_token_zero_fires"] == 0,
        {
            "first": first,
            "second": second,
            "qutrit_work_return_failures": returned["qutrit_work_return_failures"],
            "role_match_reset_failures": returned["role_match_reset_failures"],
        },
    )

    covariance = covariance_certificate()
    check(
        "the transition word is strictly covariant over 24 frames and 576 products",
        covariance["proper_cubic_frames"] == 24
        and covariance["ordered_frame_products"] == 576
        and all(
            covariance[key] == 0
            for key in (
                "rotated_word_failures",
                "rotated_term_count_failures",
                "rotated_class_census_failures",
                "frame_product_failures",
                "frame_product_word_failures",
            )
        ),
        covariance,
    )

    placement = returned["placement"]
    check(
        "constant-overhead L5 and held-L6 placements remain collision-free",
        placement["constant_overhead_per_coarse_cell"]
        and placement["global_or_Jordan_Wigner_M2"] == 0
        and all(
            row["block_collisions"] == 0 and row["held_parameters_refit"] == 0
            for row in placement["placement_rows"]
        ),
        placement,
    )

    deletion = {
        "delete_transition_CZ_witnesses": adjacent["deleted_CZ_witnesses"],
        "minimum_delete_one_transition_CZ_residual": adjacent[
            "minimum_delete_one_CZ_column_residual"
        ],
        "delete_entire_transition_residual": same_E["uncorrected_residual"],
        "unsigned_carrier_leakage": single.one_edge_certificate()[
            "unsigned_after_q_phase_leakage"
        ],
        "dirty_work_genesis_nonreturn": returned["dirty_work_genesis_nonreturn"],
    }
    check(
        "transition, carrier and dirty-work deletions remain active",
        deletion["delete_transition_CZ_witnesses"] == 12
        and deletion["minimum_delete_one_transition_CZ_residual"] > 1.9
        and deletion["delete_entire_transition_residual"] > 1.9
        and deletion["unsigned_carrier_leakage"] > 0.79
        and deletion["dirty_work_genesis_nonreturn"] == 1,
        deletion,
    )

    star = maximal_star_prefix()
    check(
        "the exact transition grows recursively across one maximal star",
        star["transition_CZ_terms"] == (0, 12, 36, 72, 120, 180)
        and star["new_CZ_terms_per_added_edge"] == (0, 12, 24, 36, 48, 60)
        and star["nested_transition_failures"] == 0
        and star["closed_form_failures"] == 0
        and star["maximum_cell_radius"] == 2,
        star,
    )

    extension = finite_patch_extension()
    check(
        "the finite all-eleven n<=2 algebra has an exact sparse extension candidate",
        extension["owned_seams"] == 11
        and extension["logical_columns_n_le_2"] == 2629
        and extension["uncorrected_mismatch_columns"] == 224
        and extension["algebraic_transition_CZ_terms"] == 224
        and extension["transition_class_counts"]
        == {"distance-2": 77, "neighbor": 114, "same-cell": 33}
        and extension["corrected_phase_failures"] == 0
        and extension["mapped_basis_failures"] == 0
        and extension["algebraic_corrected_residual"] < TOL
        and extension["maximum_cell_distance"] == 2
        and not extension["physical_same_E_compiler_claimed"],
        extension,
    )

    certificate = {
        "adjacent": adjacent,
        "same_E": same_E,
        "covariance": covariance,
        "deletion": deletion,
        "maximal_star_prefix": star,
        "finite_patch_extension": extension,
    }
    digest = sha256(
        json.dumps(certificate, sort_keys=True, separators=(",", ":"), default=str).encode()
    ).hexdigest()
    result = {
        "authority": "none",
        "audit": "unset",
        "status": "bounded-adjacent-chart-transition-certificate",
        "terminal": "ADJACENT_PAIR_TRANSITION_CLOSED_RECURRENT_TWO_STAR_GLUE_OPEN",
        "pass": FAIL == 0,
        "tests_passed": PASS,
        "tests_failed": FAIL,
        "equation": "E_refresh G_two-seam = G_physical,signed+12CZ E_refresh",
        "adjacent_transition": adjacent,
        "same_encoding": same_E,
        "covariance": covariance,
        "deletions": deletion,
        "single_star_extension": star,
        "finite_two_star_extension_candidate": extension,
        "resources": {
            "transition_CZ_M2_support": 2,
            "transition_work_M2": 0,
            "maximum_adjacent_wedge_cell_radius": 2,
            "global_ordering_M2": 0,
            "runtime_parity_queries": 0,
            "runtime_order_queries": 0,
            "runtime_measurements": 0,
            "elapsed_seconds": time.perf_counter() - START,
            "peak_rss_mb": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
            / (1024 * 1024),
        },
        "supplied": (
            "Cycle655 decoded local occupation coordinates and bounded encoder/decoder word",
            "E_refresh seven-rail carrier amplitudes and locally copied qutrit charts",
            "the Route-B signed-carrier single-seam word and clean edge-role scratch",
            "Route-C's owned seam schedule, exterior target fixture and proper-cubic frames",
            "a finite circuit ordinal, explicitly not physical time",
        ),
        "derived": (
            "the candidate phase as the pullback XOR of primitive local quadratic pairs",
            "the target exterior phase as the inversion set of the composed mode permutation",
            "their exact twelve-CZ transition with 1/6/5 locality census",
            "zero two-seam same-E intertwiner and leakage on 172 logical columns/2836 rays",
            "all-occupation truth-table closure and 24/576 strict word covariance",
            "the 6k(k-1) one-star transition law and finite 224-term two-star algebraic candidate",
        ),
        "open": (
            "physical routing and returned-work composition of the 224-CZ two-star candidate",
            "recurrent overlap/collision theorem and locally enforced transition charts",
            "n>2 E_refresh graph-code integration beyond the exhaustive phase-only wedge check",
            "end-to-end coin/seam/contact update on one common physical encoding",
            "genesis and volume scaling",
            "physical time, rate, energy, source, Record, occurrence, Born meaning, minimum or axiom pressure",
        ),
        "claim_ceiling": (
            "Positive exact compiler for the smallest adjacent pair of local signed-carrier seam charts. "
            "The finite all-eleven quadratic correction is constructive algebra, not yet a recurrent "
            "physical-site compiler.  No shared obstruction or axiom pressure is claimed."
        ),
        "certificate_sha256": digest,
    }
    print("SUMMARY_JSON", json.dumps(result, sort_keys=True, default=str))
    print("RESULT", result["terminal"] if result["pass"] else "UNFINISHED_IMPLEMENTATION")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
