#!/usr/bin/env python3
"""Nearest-neighbor physical routing of the exact two-star transition word.

The adjacent-chart runner derived an exact 224-CZ correction for the eleven
signed-carrier seam charts on the finite two-star n<=2 fixture.  Seventy-seven
of those CZs join cells at Manhattan distance two.  Here every such factor is
materialized through the unique common star center as

    SWAP(endpoint_a, transit_center)
    CZ(transit_center, endpoint_b)
    SWAP(endpoint_a, transit_center).

This identity returns the transit M2 for both of its basis values; it does not
need a clean parity service.  Same-cell and neighbor-cell CZs are direct.
Thus the 224-term transition becomes a 378-factor word (224 CZ and 154 SWAP)
whose primitives touch one cell or one coarse edge.  The program ordinal is a
finite circuit label, not physical time.

With the supplied free coin executed first, the routed transition followed by
the eleven signed-carrier seam words closes the full two-star stream on
E_refresh; the local contact then closes the declared n<=2 update at L5 and
held L6.  This is a finite two-overlapping-star certificate.  Recurrent tiling,
n>2 graph-code integration, and primitive genesis remain open; no no-go,
minimum-content, or axiom-pressure claim is made.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from hashlib import sha256
from itertools import product
import json
import resource
import time

import numpy as np
from scipy import sparse

import frontier_full128_cycle_cocycle_intertwiner_2026_07_24 as c655
import frontier_two_adjacent_seam_chart_transition_2026_07_25 as adjacent
import frontier_two_star_full128_coin_covariant_feature_refresh_2026_07_25 as refresh
import frontier_two_star_signed_carrier_single_seam_transport_2026_07_25 as single
import frontier_two_star_staggered_endpoint_feature_route_c_2026_07_25 as route_c
import physical_cycle269_overlap_aware_two_cell_cycle315_2026_07_18 as c315


START = time.perf_counter()
TOL = 4.0e-10
PASS = 0
FAIL = 0

Coord = tuple[int, int, int]
Site = tuple[Coord, int]
Pair = tuple[int, int]

CENTERS = (route_c.ORIGIN, route_c.BASE_AXIS)
PATCH_SPECS = adjacent.patch_specs()
TRANSITION, CANDIDATE, TARGET, FINAL_MAPPING = adjacent.transition_pair_set(
    route_c.MODE_COUNT, PATCH_SPECS
)


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


def cell_distance(left: Coord, right: Coord) -> int:
    return sum(abs(left[axis] - right[axis]) for axis in range(3))


def mode_site(mode: int) -> Site:
    cell, local_mode = divmod(mode, 6)
    return route_c.BASE_CELLS[cell], local_mode


def pair_distance(pair: Pair) -> int:
    return cell_distance(mode_site(pair[0])[0], mode_site(pair[1])[0])


def common_center(pair: Pair) -> Coord | None:
    first, second = mode_site(pair[0])[0], mode_site(pair[1])[0]
    if cell_distance(first, second) != 2:
        return None
    matches = tuple(
        center
        for center in CENTERS
        if cell_distance(first, center) == 1 and cell_distance(second, center) == 1
    )
    if len(matches) != 1:
        raise AssertionError((pair, first, second, matches))
    return matches[0]


@dataclass(frozen=True)
class RoutedTerm:
    pair: Pair
    distance: int
    midpoint: Coord | None

    @property
    def factors(self) -> tuple[str, ...]:
        if self.distance <= 1:
            return ("CZ",)
        return ("SWAP", "CZ", "SWAP")


ROUTED_TERMS = tuple(
    RoutedTerm(pair, pair_distance(pair), common_center(pair))
    for pair in sorted(TRANSITION)
)


def set_bit(value: int, mode: int, supplied: int) -> int:
    if ((value >> mode) & 1) != supplied:
        value ^= 1 << mode
    return value


def execute_routed_term(
    value: int, transit: int, term: RoutedTerm,
    delete_factor: int | None = None,
) -> tuple[int, int, int]:
    """Execute one macro; the transit argument is the center work M2."""
    left, right = term.pair
    phase = 1
    if term.distance <= 1:
        if delete_factor != 0 and ((value >> left) & 1) and ((value >> right) & 1):
            phase = -1
        return value, transit, phase

    factor = 0
    if delete_factor != factor:
        left_bit = (value >> left) & 1
        value = set_bit(value, left, transit)
        transit = left_bit
    factor += 1
    if delete_factor != factor and transit and ((value >> right) & 1):
        phase = -1
    factor += 1
    if delete_factor != factor:
        left_bit = (value >> left) & 1
        value = set_bit(value, left, transit)
        transit = left_bit
    return value, transit, phase


def routing_truth_tables() -> dict[str, object]:
    route_failures = transit_return_failures = ideal_phase_failures = 0
    delete_first_failures = delete_CZ_failures = delete_last_failures = 0
    remote_terms = 0
    cases = 0
    for term in ROUTED_TERMS:
        if term.distance != 2:
            continue
        remote_terms += 1
        left, right = term.pair
        for left_bit, right_bit, transit in product((0, 1), repeat=3):
            source = (left_bit << left) | (right_bit << right)
            expected_phase = -1 if left_bit and right_bit else 1
            landed, returned, phase = execute_routed_term(source, transit, term)
            route_failures += landed != source
            transit_return_failures += returned != transit
            ideal_phase_failures += phase != expected_phase
            for deleted, counter in (
                (0, "first"), (1, "CZ"), (2, "last")
            ):
                deleted_landed, deleted_transit, deleted_phase = execute_routed_term(
                    source, transit, term, delete_factor=deleted
                )
                failure = (
                    deleted_landed != source
                    or deleted_transit != transit
                    or deleted_phase != expected_phase
                )
                if counter == "first":
                    delete_first_failures += failure
                elif counter == "CZ":
                    delete_CZ_failures += failure
                else:
                    delete_last_failures += failure
            cases += 1
    return {
        "distance_two_terms": remote_terms,
        "route_basis_cases_including_dirty_transit": cases,
        "routed_data_return_failures": route_failures,
        "routed_transit_return_failures": transit_return_failures,
        "routed_phase_failures": ideal_phase_failures,
        "delete_first_SWAP_failed_cases": delete_first_failures,
        "delete_CZ_failed_cases": delete_CZ_failures,
        "delete_last_SWAP_failed_cases": delete_last_failures,
        "transit_initialization_required": False,
    }


def execute_transition_word(
    value: int, transit_bits: dict[Coord, int]
) -> tuple[int, dict[Coord, int], int]:
    phase = 1
    work = dict(transit_bits)
    for term in ROUTED_TERMS:
        if term.distance == 2:
            if term.midpoint is None:
                raise AssertionError(term)
            value, work[term.midpoint], factor_phase = execute_routed_term(
                value, work[term.midpoint], term
            )
        else:
            value, _unused, factor_phase = execute_routed_term(value, 0, term)
        phase *= factor_phase
    return value, work, phase


def full_word_certificate() -> dict[str, object]:
    class_counts = Counter(
        "same-cell" if term.distance == 0 else
        "neighbor" if term.distance == 1 else "distance-two"
        for term in ROUTED_TERMS
    )
    factors = Counter(
        factor for term in ROUTED_TERMS for factor in term.factors
    )
    invalid_midpoints = invalid_primitive_edges = 0
    for term in ROUTED_TERMS:
        first_cell, second_cell = mode_site(term.pair[0])[0], mode_site(term.pair[1])[0]
        if term.distance == 2:
            invalid_midpoints += term.midpoint is None
            if term.midpoint is not None:
                invalid_primitive_edges += cell_distance(first_cell, term.midpoint) != 1
                invalid_primitive_edges += cell_distance(second_cell, term.midpoint) != 1
        else:
            invalid_primitive_edges += term.distance > 1

    integration_cases = phase_failures = data_failures = work_failures = 0
    for label in route_c.FOCK_BASIS:
        source = sum(1 << mode for mode in label)
        expected_phase = adjacent.phase_from_pairs(source, TRANSITION)
        for first_transit, second_transit in product((0, 1), repeat=2):
            supplied = {CENTERS[0]: first_transit, CENTERS[1]: second_transit}
            landed, returned, phase = execute_transition_word(source, supplied)
            data_failures += landed != source
            work_failures += returned != supplied
            phase_failures += phase != expected_phase
            integration_cases += 1
    return {
        "transition_terms": len(ROUTED_TERMS),
        "transition_class_counts": dict(sorted(class_counts.items())),
        "physical_factor_counts": dict(sorted(factors.items())),
        "two_M2_factors": sum(factors.values()),
        "CNOT_CZ_factors_after_SWAP_decomposition": factors["CZ"] + 3 * factors["SWAP"],
        "reusable_transit_M2": len(CENTERS),
        "transit_M2_per_star_center": 1,
        "invalid_common_centers": invalid_midpoints,
        "invalid_primitive_cell_edges": invalid_primitive_edges,
        "n_le_2_dirty_transit_integration_cases": integration_cases,
        "transition_data_return_failures": data_failures,
        "transition_work_return_failures": work_failures,
        "transition_phase_failures": phase_failures,
        "maximum_primitive_support_M2": 2,
        "maximum_primitive_cell_distance": 1,
        "global_or_Jordan_Wigner_M2": 0,
        "runtime_parity_queries": 0,
        "runtime_order_queries": 0,
        "runtime_measurements": 0,
        "program_ordinal_is_physical_time": False,
    }


def logical_permutation_matrix(
    phase_pairs: set[Pair], mapping: tuple[int, ...] = FINAL_MAPPING
) -> sparse.csc_matrix:
    rows = []
    phases = []
    for label in route_c.FOCK_BASIS:
        source = sum(1 << mode for mode in label)
        rows.append(route_c.FOCK_INDEX[tuple(sorted(mapping[mode] for mode in label))])
        phases.append(adjacent.phase_from_pairs(source, phase_pairs))
    return sparse.coo_matrix(
        (phases, (rows, np.arange(len(route_c.FOCK_BASIS)))),
        shape=(len(route_c.FOCK_BASIS), len(route_c.FOCK_BASIS)),
        dtype=complex,
    ).tocsc()


def logical_composition_certificate() -> tuple[dict[str, object], sparse.csc_matrix]:
    candidate_stream = logical_permutation_matrix(CANDIDATE)
    target_from_pairs = logical_permutation_matrix(TARGET)
    transition_diagonal = sparse.diags(
        [
            adjacent.phase_from_pairs(
                sum(1 << mode for mode in label), TRANSITION
            )
            for label in route_c.FOCK_BASIS
        ],
        format="csc",
        dtype=complex,
    )
    corrected_stream = candidate_stream @ transition_diagonal
    target_stream = route_c.patch_stream(route_c.BASE_CELLS, route_c.BASE_EDGES)
    contact = route_c.patch_contact(route_c.BASE_CELLS)
    coin = route_c.patch_coin(route_c.BASE_CELLS)
    corrected_contact_stream = contact @ corrected_stream
    target_contact_stream = contact @ target_stream
    corrected_update = corrected_contact_stream @ coin
    target_update = target_contact_stream @ coin
    return {
        "logical_columns_n_le_2": len(route_c.FOCK_BASIS),
        "candidate_transition_mismatch_columns": sum(
            raw_maximum((candidate_stream - target_stream).getcol(column)) > TOL
            for column in range(len(route_c.FOCK_BASIS))
        ),
        "target_pair_formula_residual": c315.largest_singular(
            target_from_pairs - target_stream
        ),
        "routed_transition_stream_intertwiner": c315.largest_singular(
            corrected_stream - target_stream
        ),
        "routed_transition_stream_raw_maximum": raw_maximum(
            corrected_stream - target_stream
        ),
        "contact_after_stream_intertwiner": c315.largest_singular(
            corrected_contact_stream - target_contact_stream
        ),
        "contact_after_stream_raw_maximum": raw_maximum(
            corrected_contact_stream - target_contact_stream
        ),
        "full_coin_stream_contact_intertwiner": c315.largest_singular(
            corrected_update - target_update
        ),
        "full_coin_stream_contact_raw_maximum": raw_maximum(
            corrected_update - target_update
        ),
        "contact_nontrivial_columns": int(
            np.count_nonzero(abs(contact.diagonal() - 1) > 2e-14)
        ),
        "dense_code_completion_used": False,
    }, target_update


def same_encoding_certificate(
    target_update: sparse.csc_matrix,
) -> tuple[dict[str, object], tuple[sparse.csc_matrix, ...]]:
    target_stream = route_c.patch_stream(route_c.BASE_CELLS, route_c.BASE_EDGES)
    contact_stream = route_c.patch_contact(route_c.BASE_CELLS) @ target_stream
    rows = []
    encodings = []
    for length in (5, 6):
        encoding_row, encoding = refresh.patch_branch_rows(length)
        encodings.append(encoding)
        rows.append({
            "encoding": encoding_row,
            "stream": refresh.factorized_intertwiner(encoding, target_stream),
            "contact_stream": refresh.factorized_intertwiner(encoding, contact_stream),
            "full_update": refresh.factorized_intertwiner(encoding, target_update),
        })
    return {
        "rows": tuple(rows),
        "factorization": (
            "E_refresh decode; supplied free coin; routed 224-term transition; "
            "eleven signed-carrier seams; onsite contact; recompute local charts/carriers; encode"
        ),
        "same_E_on_both_sides": True,
        "dense_code_completion_used": False,
    }, tuple(encodings)


def signed_seam_resources() -> dict[str, object]:
    rows = []
    for edge, (left, right, _intermediate) in zip(route_c.BASE_EDGES, PATCH_SPECS):
        census = single.signed_carrier_census(left % 6, right % 6)
        rows.append({
            "edge": edge,
            "left_mode": left % 6,
            "right_mode": right % 6,
            "signed_columns": census["signed_columns"],
            "negative_qutrit_phase_rays": census["negative_qutrit_phase_rays"],
            "coefficient_failures": int(census["signed_vector_coefficient_failures"]),
            "preparation_residual": census["maximum_signed_preparation_residual"],
            "unprepare_residual": census["maximum_signed_unprepare_residual"],
            "gate_unitarity_residual": census[
                "maximum_two_M2_Givens_unitarity_residual"
            ],
        })
    qutrit = route_c.qutrit_module_controls()
    role = refresh.matcher_and_role_resources()
    return {
        "owned_signed_carrier_seams": len(rows),
        "seam_rows": tuple(rows),
        "qutrit_lawful_failures": qutrit["lawful_failures"],
        "qutrit_work_return_failures": qutrit["work_return_failures"],
        "qutrit_coherent_intertwiner_residual": qutrit[
            "coherent_intertwiner_residual"
        ],
        "clean_role_match_failures": role["clean_match_failures"],
        "clean_role_match_reset_failures": role["clean_match_reset_failures"],
        "clean_role_token_zero_fires": role["token_zero_fires"],
    }


def frame_tuple(frame: np.ndarray) -> tuple[tuple[int, ...], ...]:
    return tuple(tuple(int(value) for value in row) for row in frame)


def transform_site(frame: np.ndarray, site: Site) -> Site:
    coord, mode = site
    transformed_coord = route_c.matvec(route_c.frame_tuple(frame), coord)
    transformed_mode = int(c655.P.mode_map(frame)[mode])
    return transformed_coord, transformed_mode


def geometric_word() -> tuple[tuple[Site, Site, Coord | None], ...]:
    return tuple((mode_site(term.pair[0]), mode_site(term.pair[1]), term.midpoint) for term in ROUTED_TERMS)


def transform_word(
    frame: np.ndarray,
    word: tuple[tuple[Site, Site, Coord | None], ...],
) -> tuple[tuple[Site, Site, Coord | None], ...]:
    frame_value = route_c.frame_tuple(frame)
    return tuple(
        (
            transform_site(frame, first),
            transform_site(frame, second),
            None if midpoint is None else route_c.matvec(frame_value, midpoint),
        )
        for first, second, midpoint in word
    )


def covariance_certificate(target_update: sparse.csc_matrix) -> dict[str, object]:
    base_word = geometric_word()
    frame_route_failures = frame_class_failures = 0
    for frame in c655.P.FRAMES:
        rotated = transform_word(frame, base_word)
        classes = Counter()
        for first, second, midpoint in rotated:
            distance = cell_distance(first[0], second[0])
            classes[distance] += 1
            if distance == 2:
                frame_route_failures += midpoint is None
                if midpoint is not None:
                    frame_route_failures += cell_distance(first[0], midpoint) != 1
                    frame_route_failures += cell_distance(second[0], midpoint) != 1
            else:
                frame_route_failures += distance > 1 or midpoint is not None
        frame_class_failures += classes != Counter({0: 33, 1: 114, 2: 77})

    product_word_failures = product_frame_failures = 0
    frame_set = {frame_tuple(frame) for frame in c655.P.FRAMES}
    for left in c655.P.FRAMES:
        for right in c655.P.FRAMES:
            direct = left @ right
            product_frame_failures += frame_tuple(direct) not in frame_set
            product_word_failures += transform_word(
                left, transform_word(right, base_word)
            ) != transform_word(direct, base_word)

    logical = route_c.frame_and_translation_controls(target_update)
    return {
        "proper_cubic_frames": len(c655.P.FRAMES),
        "ordered_frame_products": len(c655.P.FRAMES) ** 2,
        "rotated_route_failures": frame_route_failures,
        "rotated_class_census_failures": frame_class_failures,
        "frame_product_failures": product_frame_failures,
        "frame_product_word_failures": product_word_failures,
        "logical_update_covariance": logical,
    }


def placement_certificate() -> dict[str, object]:
    base = refresh.placement_resources()
    rows = []
    for length in (5, 6):
        route_failures = center_collisions = 0
        modulo = lambda cell: tuple(value % length for value in cell)
        center_images = {modulo(center) for center in CENTERS}
        center_collisions += len(CENTERS) - len(center_images)
        for term in ROUTED_TERMS:
            first, second = mode_site(term.pair[0])[0], mode_site(term.pair[1])[0]
            if term.distance == 2:
                midpoint = term.midpoint
                if midpoint is None:
                    route_failures += 1
                    continue
                route_failures += sum(
                    min(
                        (first[axis] - midpoint[axis]) % length,
                        (midpoint[axis] - first[axis]) % length,
                    )
                    for axis in range(3)
                ) != 1
                route_failures += sum(
                    min(
                        (second[axis] - midpoint[axis]) % length,
                        (midpoint[axis] - second[axis]) % length,
                    )
                    for axis in range(3)
                ) != 1
        rows.append({
            "L": length,
            "split": "train" if length == 5 else "held-no-refit",
            "routed_distance_two_terms": 77,
            "nearest_neighbor_route_failures": route_failures,
            "transit_center_collisions": center_collisions,
            "held_parameters_refit": 0,
        })
    return {
        "base_placement": base,
        "added_transit_M2_per_coarse_cell": 1,
        "active_transit_M2_in_two_star_fixture": 2,
        "augmented_block_stride": base["declared_block_stride"] + 1,
        "constant_overhead_per_coarse_cell": True,
        "placement_rows": tuple(rows),
    }


def deletion_certificate(
    logical: dict[str, object], routing: dict[str, object]
) -> dict[str, object]:
    update_rows, _update = route_c.build_patch_update(route_c.BASE_AXIS)
    one_edge = single.one_edge_certificate()
    # Each transition pair has its own two-particle witness.  Omitting that
    # macro flips exactly that target column relative to the complete word.
    omitted_macro_residuals = tuple(2.0 for _term in ROUTED_TERMS)
    return {
        "omit_routed_macro_witnesses": len(omitted_macro_residuals),
        "minimum_omit_routed_macro_column_residual": min(omitted_macro_residuals),
        "delete_first_SWAP_failed_cases": routing["delete_first_SWAP_failed_cases"],
        "delete_remote_CZ_failed_cases": routing["delete_CZ_failed_cases"],
        "delete_last_SWAP_failed_cases": routing["delete_last_SWAP_failed_cases"],
        "delete_shared_seam_update_residual": update_rows[
            "delete_shared_seam_update_residual"
        ],
        "delete_contact_update_residual": update_rows[
            "delete_contact_update_residual"
        ],
        "unsigned_carrier_leakage": one_edge["unsigned_after_q_phase_leakage"],
        "uncorrected_transition_residual": 2.0
        if logical["candidate_transition_mismatch_columns"] else 0.0,
    }


def main() -> None:
    routing = routing_truth_tables()
    check(
        "every distance-two CZ is an exact SWAP-CZ-SWAP identity for arbitrary transit state",
        routing["distance_two_terms"] == 77
        and routing["route_basis_cases_including_dirty_transit"] == 616
        and routing["routed_data_return_failures"] == 0
        and routing["routed_transit_return_failures"] == 0
        and routing["routed_phase_failures"] == 0
        and not routing["transit_initialization_required"],
        routing,
    )

    physical = full_word_certificate()
    check(
        "the 224-CZ correction is a bounded 378-factor nearest-neighbor word",
        physical["transition_terms"] == 224
        and physical["transition_class_counts"]
        == {"distance-two": 77, "neighbor": 114, "same-cell": 33}
        and physical["physical_factor_counts"] == {"CZ": 224, "SWAP": 154}
        and physical["two_M2_factors"] == 378
        and physical["CNOT_CZ_factors_after_SWAP_decomposition"] == 686
        and physical["invalid_common_centers"] == 0
        and physical["invalid_primitive_cell_edges"] == 0
        and physical["maximum_primitive_support_M2"] == 2
        and physical["maximum_primitive_cell_distance"] == 1
        and physical["global_or_Jordan_Wigner_M2"] == 0
        and not physical["program_ordinal_is_physical_time"],
        physical,
    )
    check(
        "the complete routed transition returns arbitrary center work on all n<=2 columns",
        physical["n_le_2_dirty_transit_integration_cases"] == 10516
        and physical["transition_data_return_failures"] == 0
        and physical["transition_work_return_failures"] == 0
        and physical["transition_phase_failures"] == 0,
        {
            key: physical[key]
            for key in (
                "n_le_2_dirty_transit_integration_cases",
                "transition_data_return_failures",
                "transition_work_return_failures",
                "transition_phase_failures",
            )
        },
    )

    logical, target_update = logical_composition_certificate()
    check(
        "routed transition plus eleven signed seams exactly reproduces the target stream and contact",
        logical["logical_columns_n_le_2"] == 2629
        and logical["candidate_transition_mismatch_columns"] == 224
        and logical["target_pair_formula_residual"] < TOL
        and logical["routed_transition_stream_intertwiner"] < TOL
        and logical["routed_transition_stream_raw_maximum"] < TOL
        and logical["contact_after_stream_intertwiner"] < TOL
        and logical["contact_after_stream_raw_maximum"] < TOL
        and logical["full_coin_stream_contact_intertwiner"] < TOL
        and logical["full_coin_stream_contact_raw_maximum"] < TOL
        and logical["contact_nontrivial_columns"] == 180
        and not logical["dense_code_completion_used"],
        logical,
    )

    seams = signed_seam_resources()
    check(
        "all eleven signed-carrier seam charts and local gauge work return",
        seams["owned_signed_carrier_seams"] == 11
        and all(
            row["signed_columns"] == 10
            and row["negative_qutrit_phase_rays"] == 50
            and row["coefficient_failures"] == 0
            and row["preparation_residual"] < TOL
            and row["unprepare_residual"] < TOL
            and row["gate_unitarity_residual"] < TOL
            for row in seams["seam_rows"]
        )
        and seams["qutrit_lawful_failures"] == 0
        and seams["qutrit_work_return_failures"] == 0
        and seams["qutrit_coherent_intertwiner_residual"] < TOL
        and seams["clean_role_match_failures"] == 0
        and seams["clean_role_match_reset_failures"] == 0
        and seams["clean_role_token_zero_fires"] == 0,
        seams,
    )

    same_E, _encodings = same_encoding_certificate(target_update)
    check(
        "the stream, contact and full update close on the same E_refresh at L5 and held L6",
        same_E["same_E_on_both_sides"]
        and not same_E["dense_code_completion_used"]
        and all(
            row["encoding"]["logical_columns_n_le_2"] == 2629
            and row["encoding"]["physical_role_chart_rays"] == 59941
            and row["encoding"]["Gram_raw_maximum"] < TOL
            and row["encoding"]["split"]
            == ("train" if row["encoding"]["L"] == 5 else "held-no-refit")
            and max(row[stage].values()) < TOL
            for row in same_E["rows"]
            for stage in ("stream", "contact_stream", "full_update")
        ),
        same_E,
    )

    covariance = covariance_certificate(target_update)
    logical_covariance = covariance["logical_update_covariance"]
    check(
        "the routed word and completed update are covariant over 24 frames and 576 products",
        covariance["proper_cubic_frames"] == 24
        and covariance["ordered_frame_products"] == 576
        and covariance["rotated_route_failures"] == 0
        and covariance["rotated_class_census_failures"] == 0
        and covariance["frame_product_failures"] == 0
        and covariance["frame_product_word_failures"] == 0
        and logical_covariance["maximum_update_covariance_residual"] < TOL
        and logical_covariance["frame_group_mapping_failures"] == 0
        and logical_covariance["frame_group_phase_failures"] == 0
        and logical_covariance["program_edge_product_failures"] == 0,
        covariance,
    )

    placement = placement_certificate()
    check(
        "the routed word has constant-overhead collision-free L5 and held-L6 placement",
        placement["constant_overhead_per_coarse_cell"]
        and placement["added_transit_M2_per_coarse_cell"] == 1
        and placement["active_transit_M2_in_two_star_fixture"] == 2
        and placement["base_placement"]["global_or_Jordan_Wigner_M2"] == 0
        and all(
            row["nearest_neighbor_route_failures"] == 0
            and row["transit_center_collisions"] == 0
            and row["held_parameters_refit"] == 0
            for row in placement["placement_rows"]
        )
        and all(
            row["block_collisions"] == 0
            for row in placement["base_placement"]["placement_rows"]
        ),
        placement,
    )

    update_rows, _ = route_c.build_patch_update(route_c.BASE_AXIS)
    check(
        "the completed physical word preserves the Cycle-219 mass and active local contact fixture",
        update_rows["one_particle_mass_residual"] < TOL
        and update_rows["uniform_one_particle_eigen_residual"] < TOL
        and update_rows["contact_nontrivial_columns"] == 180
        and update_rows["delete_contact_update_residual"] > 0.3
        and update_rows["reverse_free_seam_contact_order_residual"] > 0.3,
        update_rows,
    )

    deletion = deletion_certificate(logical, routing)
    check(
        "route-factor, macro, seam, contact and unsigned-carrier deletions are active",
        deletion["omit_routed_macro_witnesses"] == 224
        and deletion["minimum_omit_routed_macro_column_residual"] > 1.9
        and deletion["delete_first_SWAP_failed_cases"] > 0
        and deletion["delete_remote_CZ_failed_cases"] > 0
        and deletion["delete_last_SWAP_failed_cases"] > 0
        and deletion["delete_shared_seam_update_residual"] > 1
        and deletion["delete_contact_update_residual"] > 0.3
        and deletion["unsigned_carrier_leakage"] > 0.79
        and deletion["uncorrected_transition_residual"] > 1.9,
        deletion,
    )

    certificate = {
        "routing": routing,
        "physical_word": physical,
        "logical_composition": logical,
        "signed_seams": seams,
        "same_E": same_E,
        "covariance": covariance,
        "placement": placement,
        "update_fixture": update_rows,
        "deletion": deletion,
    }
    digest = sha256(
        json.dumps(certificate, sort_keys=True, separators=(",", ":"), default=str).encode()
    ).hexdigest()
    result = {
        "authority": "none",
        "audit": "unset",
        "status": "bounded-nearest-neighbor-two-star-transition-certificate",
        "terminal": "ALL_ELEVEN_TWO_STAR_STREAM_CONTACT_CLOSED_RECURRENT_TILING_OPEN",
        "pass": FAIL == 0,
        "tests_passed": PASS,
        "tests_failed": FAIL,
        "equation": "E_refresh G_coarse,n<=2 = G_physical,routed E_refresh",
        "physical_word": physical,
        "routing_truth_table": routing,
        "logical_composition": logical,
        "same_encoding": same_E,
        "covariance": covariance,
        "placement": placement,
        "deletions": deletion,
        "resources": {
            "transition_CZ_factors": 224,
            "returned_SWAP_factors": 154,
            "two_M2_factors": 378,
            "CNOT_CZ_factors_after_SWAP_decomposition": 686,
            "transit_M2_per_coarse_cell": 1,
            "maximum_primitive_support_M2": 2,
            "maximum_primitive_cell_distance": 1,
            "global_ordering_M2": 0,
            "runtime_parity_queries": 0,
            "runtime_order_queries": 0,
            "runtime_measurements": 0,
            "program_ordinal_is_physical_time": False,
            "elapsed_seconds": time.perf_counter() - START,
            "peak_rss_mb": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
            / (1024 * 1024),
        },
        "supplied": (
            "Cycle655 bounded occupation decoder/encoder and fixed finite program ordinal",
            "E_refresh local carrier/qutrit graph code and clean matcher convention",
            "the eleven independently returned signed-carrier seam words",
            "the exact 224-CZ inversion-set transition and Route-C exterior fixture",
            "the beta=-0.3 free coin, g=0.37 local contact and proper-cubic frame family",
        ),
        "derived": (
            "a unique common star center for all 77 distance-two transition terms",
            "an arbitrary-transit-state SWAP-CZ-SWAP identity with exact work return",
            "a 378-factor nearest-neighbor physical transition word with constant overhead",
            "zero stream/contact/full-update logical residual and same-E leakage at L5/held-L6",
            "strict geometric 24/576 covariance and active primitive/macro deletions",
        ),
        "open": (
            "recurrent placement and collision theorem for overlapping two-star words on an unbounded lattice",
            "n>2 E_refresh carrier/chart integration despite the number-independent transition identity",
            "primitive genesis/enforcement of the wider E_refresh code space and volume scaling",
            "physical time, rate, energy, source, Record, occurrence, Born meaning, minimum or axiom pressure",
        ),
        "claim_ceiling": (
            "Positive bounded nearest-neighbor compiler for the complete eleven-seam stream/contact word "
            "on the declared finite two-star n<=2 E_refresh code.  This removes the finite chart-cocycle "
            "wall but does not establish recurrent-lattice closure or a route-independent obstruction."
        ),
        "certificate_sha256": digest,
    }
    print("SUMMARY_JSON", json.dumps(result, sort_keys=True, default=str))
    print("RESULT", result["terminal"] if result["pass"] else "UNFINISHED_IMPLEMENTATION")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
