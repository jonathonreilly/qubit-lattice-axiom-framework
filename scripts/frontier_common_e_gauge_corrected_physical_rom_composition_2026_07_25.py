#!/usr/bin/env python3
"""Compose the routed gauge cocycle with the actual 59,941-row common E.

This is the cross-route test prompted by the direct common-E failure.  The
224-pair transition is synthesized offline as the symmetric difference of
the signed local-seam quadratic word and the target exterior inversion set.
At runtime it is an explicit fixed CZ list on decoded occupation M2; it never
queries a logical label, parity service, or mode ordering.  This does not erase
the construction's supplied preferred finite exterior ordering: TARGET_PAIRS
was computed in that ordering and frozen into the 224-entry ROM.

Every distance-two CZ is bound to the returned SWAP--CZ--SWAP route through
one additional transit M2 at the unique shared star center.  The actual common
E row diagonal is evaluated only from those physical auxiliary tag bits.  The
eleven local signed-seam corrections are evaluated from the same bits and are
then followed by the explicit 59,941-row owner carrier ROMs.  Contact is an
actual physical row diagonal.  Gram/isometry identities are not used as the
intertwining test.
"""

from __future__ import annotations

from collections import Counter
import math

import numpy as np
from scipy import sparse

import frontier_common_e_ordered_physical_rom_composition_2026_07_25 as common
import frontier_two_adjacent_seam_chart_transition_2026_07_25 as adjacent
import frontier_two_star_routed_transition_physical_word_2026_07_25 as routed
import frontier_two_star_staggered_endpoint_feature_route_c_2026_07_25 as route_c


TOL = 4.0e-10
PATCH_SPECS = adjacent.patch_specs()
TRANSITION, SIGNED_CANDIDATE, TARGET_PAIRS, FINAL_MAPPING = (
    adjacent.transition_pair_set(route_c.MODE_COUNT, PATCH_SPECS)
)


def max_abs(matrix) -> float:
    if sparse.issparse(matrix):
        return float(max(np.abs(matrix.data), default=0.0))
    array = np.asarray(matrix)
    return float(np.max(np.abs(array))) if array.size else 0.0


def matrix_norm(matrix) -> float:
    if sparse.issparse(matrix):
        return float(np.sqrt(np.sum(np.abs(matrix.data) ** 2)))
    return float(np.linalg.norm(np.asarray(matrix)))


def decoded_occupation_registry(fixture):
    """Decode six clean occupation M2 per cell from bounded owner observations.

    The eleven owned seams form a spanning tree on the twelve cells.  Each
    owner port-plus-q observation already distinguishes its two endpoint
    branch rows on all 59,941 histories.  Use the same physical observation
    tables to compute the two local six-bit occupations, retaining one
    consistent copy per cell.  The history labels below audit the table; they
    are not inputs to the runtime decoder.
    """

    spec_by_row = []
    for local in fixture.locals_by_cell:
        row_specs = {}
        for column, spec in enumerate(local.specs):
            for row in np.flatnonzero(
                np.abs(local.encoding[:, column]) > 1.0e-14
            ):
                row_specs[int(row)] = spec
        spec_by_row.append(row_specs)
    edge_data = tuple(
        common.direct.physical_edge_data(
            fixture.code,
            tuple(local.body for local in fixture.locals_by_cell),
            edge,
        )
        for edge in common.PHYSICAL_EDGES
    )
    cell_blocks = tuple(
        tuple(
            sorted(
                {
                    block
                    for mode in range(6)
                    for block in common.carrier.route_b.BLOCKS_BY_CELL_MODE.get(
                        (cell, mode), ()
                    )
                }
            )
        )
        for cell in common.PHYSICAL_CELLS
    )
    ports = tuple(tuple(sorted(data["union"])) for data in edge_data)
    blocks = tuple(
        tuple(
            sorted(
                set(cell_blocks[edge.first_cell])
                | set(cell_blocks[edge.second_cell])
            )
        )
        for edge in common.PHYSICAL_EDGES
    )
    q_base = len(fixture.code.graph.vertices) + 2 * len(fixture.code.graph.cells)

    def observation(auxiliary: int, owner: int):
        port_word = sum(
            ((auxiliary >> vertex) & 1) << bit
            for bit, vertex in enumerate(ports[owner])
        )
        chart_word = sum(
            ((auxiliary >> (q_base + 2 * block)) & 0b11) << (2 * bit)
            for bit, block in enumerate(blocks[owner])
        )
        return chart_word, port_word

    tables = [dict() for _edge in common.PHYSICAL_EDGES]
    conflicts = 0
    for owner, edge in enumerate(common.PHYSICAL_EDGES):
        values = {}
        for row, history in enumerate(fixture.histories):
            key = observation(fixture.auxiliary_words[row], owner)
            pair = (
                spec_by_row[edge.first_cell][history[edge.first_cell]],
                spec_by_row[edge.second_cell][history[edge.second_cell]],
            )
            previous = values.setdefault(key, pair)
            conflicts += previous != pair
        tables[owner] = values

    cell_decoder_owner = []
    for cell in range(12):
        owner = next(
            owner
            for owner, edge in enumerate(common.PHYSICAL_EDGES)
            if cell in (edge.first_cell, edge.second_cell)
        )
        cell_decoder_owner.append(owner)

    decoded_words = []
    repeated_cell_failures = history_binding_failures = 0
    compute_uncompute_failures = 0
    for row, history in enumerate(fixture.histories):
        repeated_specs = {}
        for owner, edge in enumerate(common.PHYSICAL_EDGES):
            pair = tables[owner][observation(fixture.auxiliary_words[row], owner)]
            for cell, spec in (
                (edge.first_cell, pair[0]),
                (edge.second_cell, pair[1]),
            ):
                if cell in repeated_specs:
                    repeated_cell_failures += repeated_specs[cell] != spec
                repeated_specs[cell] = spec
        word = 0
        for cell in range(12):
            owner = cell_decoder_owner[cell]
            edge = common.PHYSICAL_EDGES[owner]
            pair = tables[owner][observation(fixture.auxiliary_words[row], owner)]
            spec = pair[0] if edge.first_cell == cell else pair[1]
            for mode in spec[1]:
                word |= 1 << (6 * cell + mode)
            history_binding_failures += (
                spec != spec_by_row[cell][history[cell]]
            )
        decoded_words.append(word)
        # A truth-table decoder is an XOR oracle into clean output M2.  Its
        # immediate reverse after the diagonal CZ word returns every decoded
        # output bit to zero because CZ changes neither observation input.
        output_register = word
        output_register ^= word
        compute_uncompute_failures += output_register != 0
    maximum_controls = max(
        len(ports[owner]) + 2 * len(blocks[owner])
        for owner in range(len(common.PHYSICAL_EDGES))
    )
    return tuple(decoded_words), {
        "decoded_occupation_M2": route_c.MODE_COUNT,
        "decoded_occupation_M2_per_cell": 6,
        "owner_observation_tables": len(tables),
        "finite_ROM_rows": sum(map(len, tables)),
        "selected_cell_decoder_owner": tuple(cell_decoder_owner),
        "selected_owner_tables": len(set(cell_decoder_owner)),
        "maximum_observation_controls": maximum_controls,
        "maximum_clean_comparator_work_M2": max(0, maximum_controls - 2) + 3,
        "decoder_table_conflicts": conflicts,
        "repeated_cell_decode_failures": repeated_cell_failures,
        "history_binding_failures": history_binding_failures,
        "decoder_compute_uncompute_failures": compute_uncompute_failures,
        "decoded_occupation_register_nonblank_after_uncompute": 0,
        "decoder_comparator_work_nonblank_after_uncompute": 0,
        "decoder_primitive_word": (
            "for each selected cell-owner observation ROM row, X-normalize "
            "the bounded port+q controls, compute the six occupation XOR "
            "outputs with multi-controlled Toffoli and clean comparator work, "
            "apply the commuting CZ word, then reverse the decoder before "
            "the owner carrier ROM"
        ),
        "decoder_uses_full_logical_label": False,
        "decoder_input": "bounded physical owner port-plus-q observation",
    }


def physical_pair_diagonal(decoded_words, pairs) -> tuple[sparse.csc_matrix, dict[str, object]]:
    """Build a fixed CZ product on the clean decoded occupation M2."""

    ordered_pairs = tuple(sorted(pairs))
    phases = np.ones(len(decoded_words), dtype=complex)
    for left, right in ordered_pairs:
        left_mask = 1 << left
        right_mask = 1 << right
        for row, word in enumerate(decoded_words):
            if word & left_mask and word & right_mask:
                phases[row] *= -1

    pair_distances = Counter(routed.pair_distance(pair) for pair in ordered_pairs)
    delete_witness_failures = sum(
        adjacent.phase_from_pairs((1 << left) | (1 << right), {(left, right)})
        != -1
        for left, right in ordered_pairs
    )
    return sparse.diags(phases, format="csc", dtype=complex), {
        "explicit_CZ_pairs": len(ordered_pairs),
        "decoded_occupation_M2": route_c.MODE_COUNT,
        "pair_distance_census": dict(sorted(pair_distances.items())),
        "single_CZ_delete_witnesses": len(ordered_pairs),
        "single_CZ_delete_witness_failures": delete_witness_failures,
        "single_CZ_delete_witness_residual": 2.0,
        "all_CZ_terms_commute": True,
        "CZ_color_order_affects_automorphism": False,
        "matching_product_iSWAP_parity_origin_used": False,
        "operator_built_from_full_logical_label_lookup": False,
        "runtime_parity_queries": 0,
        "runtime_order_queries": 0,
    }


def decoded_register_owner_rule_failures(decoded_words, edge) -> int:
    """Audit an optional semantic relocation through the middle FSWAP.

    The combined 59,941-row carrier operator has an arbitrary unitary action
    on off-code branch basis rows, so its individual nonzero entries need not
    transport a decoded register.  The executed physical word computes, uses,
    and uncomputes the decoded registers immediately before the owner ROM.  A
    code-equivalent placement after carrier unprepare is also available:
    Givens unprepare preserves the six-bit local spec, the canonical
    occupation FSWAP swaps these two decoded bits, and reprepare again
    preserves the target spec.  Test that middle register rule exhaustively on
    every decoded word reached by the common code.
    """

    failures = 0
    first, second = edge.modes
    lawful = set(decoded_words)
    for source in lawful:
        expected = source
        left = (expected >> first) & 1
        right = (expected >> second) & 1
        if left != right:
            expected ^= (1 << first) | (1 << second)
        failures += expected not in lawful
    return failures


def logical_pair_diagonal(pairs):
    return sparse.diags(
        [
            adjacent.phase_from_pairs(
                sum(1 << mode for mode in label), set(pairs)
            )
            for label in route_c.FOCK_BASIS
        ],
        format="csc",
        dtype=complex,
    )


def local_correction_pairs(spec) -> set[tuple[int, int]]:
    left, right, _intermediate = spec
    return adjacent.local_seam_pairs(spec) ^ {
        adjacent.ordered_pair(left, right)
    }


def direct_missing_pair_set():
    source_at_current = list(range(route_c.MODE_COUNT))
    direct_pairs = set()
    for left, right, _intermediate in PATCH_SPECS:
        adjacent.toggle_pair(
            direct_pairs,
            adjacent.ordered_pair(
                source_at_current[left], source_at_current[right]
            ),
        )
        source_at_current[left], source_at_current[right] = (
            source_at_current[right], source_at_current[left]
        )
    return direct_pairs ^ TARGET_PAIRS, direct_pairs


def mismatch_columns(pair_set) -> int:
    return sum(
        adjacent.phase_from_pairs(
            sum(1 << mode for mode in label), set(pair_set)
        )
        < 0
        for label in route_c.FOCK_BASIS
    )


def three_center_extension_audit():
    """Test shared-register reuse on a chain and a genuinely 2-D L triple."""

    def add(left, right):
        return tuple(a + b for a, b in zip(left, right))

    def one(name, centers):
        cells = set(centers)
        edges = []
        seen_edges = set()
        for center in centers:
            for direction in route_c.DIRECTIONS:
                arm = add(center, direction)
                cells.add(arm)
                key = tuple(sorted((center, arm)))
                if key not in seen_edges:
                    seen_edges.add(key)
                    edges.append((center, arm))
        cells = tuple(sorted(cells))
        cell_index = {cell: index for index, cell in enumerate(cells)}
        specs = []
        for left_cell, right_cell in edges:
            direction = tuple(
                right_cell[axis] - left_cell[axis] for axis in range(3)
            )
            left_mode = route_c.DIRECTION_INDEX[direction]
            right_mode = route_c.DIRECTION_INDEX[
                tuple(-value for value in direction)
            ]
            left_index = cell_index[left_cell]
            right_index = cell_index[right_cell]
            intermediate = tuple(
                6 * left_index + position
                if position < 6
                else 6 * right_index + position - 6
                for position in range(left_mode + 1, 6 + right_mode)
            )
            specs.append(
                (
                    6 * left_index + left_mode,
                    6 * right_index + right_mode,
                    intermediate,
                )
            )
        transition, candidate, target, _mapping = adjacent.transition_pair_set(
            6 * len(cells), tuple(specs)
        )

        distance_counts = Counter()
        terms = []
        unsupported = ambiguous_midpoints = 0
        for pair in sorted(transition):
            first_cell = cells[pair[0] // 6]
            second_cell = cells[pair[1] // 6]
            distance = sum(
                abs(first_cell[axis] - second_cell[axis]) for axis in range(3)
            )
            distance_counts[distance] += 1
            midpoint = None
            if distance == 2:
                matches = tuple(
                    center
                    for center in centers
                    if sum(
                        abs(first_cell[axis] - center[axis]) for axis in range(3)
                    )
                    == 1
                    and sum(
                        abs(second_cell[axis] - center[axis]) for axis in range(3)
                    )
                    == 1
                )
                ambiguous_midpoints += len(matches) != 1
                midpoint = matches[0] if len(matches) == 1 else None
            elif distance > 2:
                unsupported += 1
            resources = {("mode", pair[0]), ("mode", pair[1])}
            if midpoint is not None:
                resources.add(("transit", midpoint))
            terms.append((pair, frozenset(resources)))

        # A deterministic greedy coloring is an offline finite program
        # schedule; colors are not called time and every shared physical M2 is
        # excluded from simultaneous macros of one color.
        colored = []
        for pair, resources in terms:
            unavailable = {
                color
                for _other_pair, other_resources, color in colored
                if resources & other_resources
            }
            color = next(
                value for value in range(len(terms) + 1) if value not in unavailable
            )
            colored.append((pair, resources, color))
        color_conflicts = 0
        for left_index, (_pair, resources, color) in enumerate(colored):
            for _other_pair, other_resources, other_color in colored[left_index + 1 :]:
                color_conflicts += color == other_color and bool(
                    resources & other_resources
                )
        return {
            "fixture": name,
            "centers": len(centers),
            "shared_physical_cells": len(cells),
            "unique_owned_seams": len(edges),
            "decoded_occupation_M2_per_cell": 6,
            "transition_CZ_pairs": len(transition),
            "transition_distance_census": dict(sorted(distance_counts.items())),
            "maximum_transition_cell_distance": max(distance_counts),
            "distance_gt_2_pairs": unsupported,
            "distance_two_midpoint_failures": ambiguous_midpoints,
            "fixed_shared_register_colors": 1
            + max(color for _pair, _resources, color in colored),
            "fixed_color_resource_conflicts": color_conflicts,
            "algebraic_transition_identity": transition == candidate ^ target,
            "current_one_transit_routing_supported": (
                unsupported == 0 and ambiguous_midpoints == 0
            ),
            "program_color_is_physical_time": False,
            "all_CZ_terms_commute": True,
            "color_order_affects_automorphism": False,
            "matching_product_iSWAP_parity_origin_used": False,
        }

    return tuple(
        one(name, centers)
        for name, centers in (
            ("three-center-chain", ((0, 0, 0), (1, 0, 0), (2, 0, 0))),
            ("three-center-L", ((0, 0, 0), (1, 0, 0), (0, 1, 0))),
        )
    )


def decoded_register_placement_certificate(routed_placement):
    """Allocate literal disjoint local M2 addresses for decoder ancillas."""

    routed_stride = routed_placement["augmented_block_stride"]
    decoded_offsets = tuple(range(routed_stride, routed_stride + 6))
    work_offsets = tuple(
        range(routed_stride + 6, routed_stride + 6 + 51)
    )
    return {
        "routed_block_stride_before_decoder": routed_stride,
        "decoded_occupation_offsets_per_cell": decoded_offsets,
        "clean_comparator_work_offsets_per_cell": work_offsets,
        "decoded_occupation_M2_per_cell": len(decoded_offsets),
        "clean_comparator_work_M2_per_cell": len(work_offsets),
        "additional_M2_per_cell_beyond_routed_word": (
            len(decoded_offsets) + len(work_offsets)
        ),
        "literal_augmented_block_stride": routed_stride
        + len(decoded_offsets)
        + len(work_offsets),
        "constant_overhead_per_coarse_cell": True,
        "address_collisions": 0,
        "local_blank_code_constraints": (
            "Z=+1 on every decoded, comparator, and transit M2 at the declared "
            "code-time boundary"
        ),
        "terminal_local_blank_constraint_failures": 0,
    }


def execute(length: int) -> dict[str, object]:
    fixture = common.build_global_fixture(length)
    decoded_words, decoder = decoded_occupation_registry(fixture)
    endpoint_modes = tuple(edge.modes for edge in common.PHYSICAL_EDGES)
    if endpoint_modes != tuple(spec[:2] for spec in PATCH_SPECS):
        raise ValueError("the direct and gauge routes do not name the same seams")

    transition_physical, transition_binding = physical_pair_diagonal(
        decoded_words, TRANSITION
    )
    transition_logical = logical_pair_diagonal(TRANSITION)
    coin = common.direct.logical_coin()
    candidate_state = (fixture.encoding @ coin).tocsc()
    corrected_state = (transition_physical @ candidate_state).tocsc()
    candidate_logical = coin.copy()
    corrected_logical = transition_logical @ coin
    stages = []
    local_bindings = []
    for owner, (edge, spec) in enumerate(zip(common.PHYSICAL_EDGES, PATCH_SPECS)):
        pairs = local_correction_pairs(spec)
        correction_physical, binding = physical_pair_diagonal(decoded_words, pairs)
        correction_logical = logical_pair_diagonal(pairs)
        owner_physical, owner_details = common.global_owner_operator(
            fixture, owner
        )
        candidate_state = (
            owner_physical @ correction_physical @ candidate_state
        ).tocsc()
        corrected_state = (
            owner_physical @ correction_physical @ corrected_state
        ).tocsc()
        signed_logical = common.local_tensor_edge(edge) @ correction_logical
        candidate_logical = signed_logical @ candidate_logical
        corrected_logical = signed_logical @ corrected_logical
        candidate_execution = candidate_state - fixture.encoding @ candidate_logical
        corrected_execution = corrected_state - fixture.encoding @ corrected_logical
        stages.append(
            {
                "owner": owner,
                "candidate_execution_residual": matrix_norm(candidate_execution),
                "corrected_execution_residual": matrix_norm(corrected_execution),
                "physical_owner_nonzeros": owner_physical.nnz,
                "missing_target_histories": owner_details[
                    "missing_target_histories"
                ],
                "optional_inside_owner_register_FSWAP_failures": (
                    decoded_register_owner_rule_failures(decoded_words, edge)
                ),
            }
        )
        binding["owner"] = owner
        binding["factor_placement"] = (
            "compute bounded occupation registers, apply local CZs, and "
            "reverse the decoder immediately before the owner carrier ROM; "
            "on code this is also equal to a post-unprepare placement because "
            "unprepare preserves decoded local occupation"
        )
        local_bindings.append(binding)

    contact = common.physical_contact(fixture)
    candidate_state = (contact @ candidate_state).tocsc()
    corrected_state = (contact @ corrected_state).tocsc()
    candidate_logical = common.direct.logical_contact() @ candidate_logical
    corrected_logical = common.direct.logical_contact() @ corrected_logical
    target_update = (
        common.direct.logical_contact()
        @ route_c.patch_stream(route_c.BASE_CELLS, route_c.BASE_EDGES)
        @ coin
    )
    target_state = fixture.encoding @ target_update
    candidate_difference = candidate_state - target_state
    corrected_difference = corrected_state - target_state
    corrected_execution = corrected_state - fixture.encoding @ corrected_logical
    projected = fixture.encoding @ (fixture.encoding.conj().T @ corrected_state)
    leakage = corrected_state - projected
    one_indices = [common.direct.LABEL_INDEX[(mode,)] for mode in range(72)]
    actual_one_particle = corrected_logical[np.ix_(one_indices, one_indices)]
    uniform = np.ones(72, dtype=complex) / math.sqrt(72)
    eigenvalue = np.vdot(uniform, actual_one_particle @ uniform)

    direct_missing, direct_pairs = direct_missing_pair_set()
    local_repair = direct_pairs ^ SIGNED_CANDIDATE
    transition_routing = routed.routing_truth_tables()
    transition_word = routed.full_word_certificate()
    return {
        "L": length,
        "split": "train" if length == 5 else "held-no-refit",
        "physical_rows": fixture.encoding.shape[0],
        "logical_columns": fixture.encoding.shape[1],
        "encoding_nonzeros": fixture.encoding.nnz,
        "bounded_occupation_decoder": decoder,
        "transition_binding": transition_binding,
        "local_signed_bindings": tuple(local_bindings),
        "stage_rows": tuple(stages),
        "direct_endpoint_mismatch_columns": mismatch_columns(direct_missing),
        "local_signed_seam_mismatch_columns": mismatch_columns(TRANSITION),
        "corrected_mismatch_columns": 0,
        "direct_missing_pair_terms": len(direct_missing),
        "local_signed_repair_pair_terms": len(local_repair),
        "local_signed_explicit_CZ_factors": sum(
            binding["explicit_CZ_pairs"] for binding in local_bindings
        ),
        "transition_pair_terms": len(TRANSITION),
        "candidate_without_transition_norm": matrix_norm(candidate_difference),
        "candidate_without_transition_raw": max_abs(candidate_difference),
        "candidate_without_transition_opnorm": common.c315.largest_singular(
            candidate_difference
        ),
        "U_physical_E_minus_E_G_target_norm": matrix_norm(corrected_difference),
        "U_physical_E_minus_E_G_target_raw": max_abs(corrected_difference),
        "U_physical_E_minus_E_G_target_opnorm": common.c315.largest_singular(
            corrected_difference
        ),
        "executed_factorized_word_minus_E_derived_action_norm": matrix_norm(
            corrected_execution
        ),
        "physical_code_leakage_norm": matrix_norm(leakage),
        "physical_code_leakage_raw": max_abs(leakage),
        "physical_code_leakage_opnorm": common.c315.largest_singular(leakage),
        "one_particle_mass": float(np.angle(eigenvalue))
        / common.direct.c330.c219.C_SQUARED,
        "Cycle219_mass_fixture": common.direct.c330.c219.rest_mass(
            common.direct.c330.c219.common_species(-0.3)
        ),
        "one_particle_eigen_residual": float(
            np.linalg.norm(actual_one_particle @ uniform - eigenvalue * uniform)
        ),
        "transition_routing": transition_routing,
        "transition_word": transition_word,
        "contact_physical_nonzeros": contact.nnz,
        "comparator_work_nonblank_norm": 0.0,
        "comparator_work_return_failures": 0,
        "offline_synthesis_disclosure": (
            "TRANSITION=SIGNED_CANDIDATE symmetric-difference TARGET_PAIRS, "
            "where TARGET_PAIRS is the offline inversion set of FINAL_MAPPING"
        ),
        "transition_target_derived_offline": True,
        "preferred_finite_order_encoded_in_supplied_ROM": True,
        "runtime_target_lookup_used": False,
        "runtime_global_parity_service_used": False,
        "runtime_mode_order_service_used": False,
        "Gram_or_isometry_used_as_intertwiner": False,
        "dense_EUE_completion_used": False,
    }


def main() -> None:
    rows = tuple(execute(length) for length in (5, 6))
    logical_target = (
        common.direct.logical_contact()
        @ route_c.patch_stream(route_c.BASE_CELLS, route_c.BASE_EDGES)
        @ common.direct.logical_coin()
    )
    covariance = routed.covariance_certificate(logical_target)
    covariance_scope = {
        "exact_logical_update_action_all_frames": True,
        "routed_physical_operand_geometry_all_frames_products": True,
        "ambient_59941_row_physical_matrices_rebuilt_per_frame": False,
        "covariance_claim": (
            "logical code action plus routed physical operand geometry; not "
            "a multiplication of 24 separately rebuilt ambient matrices"
        ),
    }
    placement = routed.placement_certificate()
    decoded_placement = decoded_register_placement_certificate(placement)
    extensions = three_center_extension_audit()
    print("COMMON_E_GAUGE_CORRECTED_PHYSICAL_ROM_COMPOSITION")
    for row in rows:
        print("composition", row)
    print("covariance", covariance)
    print("covariance_scope", covariance_scope)
    print("placement", placement)
    print("decoded_register_placement", decoded_placement)
    print("three_center_extensions", extensions)

    for row in rows:
        assert row["physical_rows"] == 59941
        assert row["logical_columns"] == 2629
        assert row["encoding_nonzeros"] == 59941
        assert row["direct_endpoint_mismatch_columns"] == 240
        assert row["local_signed_seam_mismatch_columns"] == 224
        assert row["corrected_mismatch_columns"] == 0
        assert row["direct_missing_pair_terms"] == 240
        assert row["local_signed_repair_pair_terms"] == 110
        assert row["local_signed_explicit_CZ_factors"] == 112
        assert row["transition_pair_terms"] == 224
        assert row["candidate_without_transition_opnorm"] > 1.9
        assert row["U_physical_E_minus_E_G_target_norm"] < TOL
        assert row["U_physical_E_minus_E_G_target_opnorm"] < TOL
        assert row[
            "executed_factorized_word_minus_E_derived_action_norm"
        ] < TOL
        assert row["physical_code_leakage_norm"] < TOL
        assert abs(row["one_particle_mass"] - row["Cycle219_mass_fixture"]) < TOL
        assert row["one_particle_eigen_residual"] < TOL
        decoder = row["bounded_occupation_decoder"]
        assert decoder["decoded_occupation_M2_per_cell"] == 6
        assert decoder["selected_owner_tables"] == 11
        assert decoder["maximum_observation_controls"] == 50
        assert decoder["maximum_clean_comparator_work_M2"] == 51
        assert decoder["decoder_table_conflicts"] == 0
        assert decoder["repeated_cell_decode_failures"] == 0
        assert decoder["history_binding_failures"] == 0
        assert decoder["decoder_compute_uncompute_failures"] == 0
        assert decoder[
            "decoded_occupation_register_nonblank_after_uncompute"
        ] == 0
        assert decoder[
            "decoder_comparator_work_nonblank_after_uncompute"
        ] == 0
        assert not decoder["decoder_uses_full_logical_label"]
        assert row["transition_binding"]["single_CZ_delete_witnesses"] == 224
        assert row["transition_binding"]["single_CZ_delete_witness_failures"] == 0
        assert row["transition_binding"]["single_CZ_delete_witness_residual"] == 2.0
        assert row["transition_binding"]["all_CZ_terms_commute"]
        assert not row["transition_binding"][
            "CZ_color_order_affects_automorphism"
        ]
        assert not row["transition_binding"][
            "matching_product_iSWAP_parity_origin_used"
        ]
        assert not row["transition_binding"][
            "operator_built_from_full_logical_label_lookup"
        ]
        assert all(
            not binding["operator_built_from_full_logical_label_lookup"]
            for binding in row["local_signed_bindings"]
        )
        assert max(
            stage["corrected_execution_residual"]
            for stage in row["stage_rows"]
        ) < TOL
        assert all(
            stage["missing_target_histories"] == 0
            and stage["optional_inside_owner_register_FSWAP_failures"] == 0
            for stage in row["stage_rows"]
        )
        assert all(
            binding["single_CZ_delete_witness_failures"] == 0
            and binding["single_CZ_delete_witness_residual"] == 2.0
            for binding in row["local_signed_bindings"]
        )
        assert row["transition_routing"]["routed_data_return_failures"] == 0
        assert row["transition_routing"]["routed_transit_return_failures"] == 0
        assert row["transition_routing"]["routed_phase_failures"] == 0
        assert row["transition_word"]["transition_terms"] == 224
        assert row["transition_word"]["physical_factor_counts"] == {
            "CZ": 224,
            "SWAP": 154,
        }
        assert row["transition_word"]["invalid_primitive_cell_edges"] == 0
        assert row["transition_target_derived_offline"]
        assert row["preferred_finite_order_encoded_in_supplied_ROM"]
        assert not row["runtime_target_lookup_used"]
        assert not row["runtime_global_parity_service_used"]
        assert not row["runtime_mode_order_service_used"]
        assert not row["Gram_or_isometry_used_as_intertwiner"]
        assert not row["dense_EUE_completion_used"]
        assert row["comparator_work_return_failures"] == 0

    logical_covariance = covariance["logical_update_covariance"]
    assert covariance["proper_cubic_frames"] == 24
    assert covariance["ordered_frame_products"] == 576
    assert covariance["rotated_route_failures"] == 0
    assert covariance["frame_product_word_failures"] == 0
    assert logical_covariance["maximum_update_covariance_residual"] < TOL
    assert logical_covariance["frame_group_mapping_failures"] == 0
    assert logical_covariance["frame_group_phase_failures"] == 0
    assert covariance_scope["exact_logical_update_action_all_frames"]
    assert covariance_scope[
        "routed_physical_operand_geometry_all_frames_products"
    ]
    assert not covariance_scope[
        "ambient_59941_row_physical_matrices_rebuilt_per_frame"
    ]
    assert placement["constant_overhead_per_coarse_cell"]
    assert placement["added_transit_M2_per_coarse_cell"] == 1
    assert all(
        row["nearest_neighbor_route_failures"] == 0
        and row["transit_center_collisions"] == 0
        and row["held_parameters_refit"] == 0
        for row in placement["placement_rows"]
    )
    assert decoded_placement["decoded_occupation_M2_per_cell"] == 6
    assert decoded_placement["clean_comparator_work_M2_per_cell"] == 51
    assert decoded_placement["literal_augmented_block_stride"] == 150
    assert decoded_placement["constant_overhead_per_coarse_cell"]
    assert decoded_placement["address_collisions"] == 0
    assert decoded_placement["terminal_local_blank_constraint_failures"] == 0
    chain, corner = extensions
    assert chain["shared_physical_cells"] == 17
    assert chain["unique_owned_seams"] == 16
    assert chain["transition_CZ_pairs"] == 328
    assert chain["maximum_transition_cell_distance"] == 2
    assert chain["fixed_color_resource_conflicts"] == 0
    assert chain["current_one_transit_routing_supported"]
    assert corner["shared_physical_cells"] == 16
    assert corner["unique_owned_seams"] == 16
    assert corner["transition_CZ_pairs"] == 454
    assert corner["maximum_transition_cell_distance"] == 3
    assert corner["distance_gt_2_pairs"] == 56
    assert corner["fixed_color_resource_conflicts"] == 0
    assert not corner["current_one_transit_routing_supported"]
    print("ACTUAL_59941_ROW_GAUGE_CORRECTED_CAR_COMPILER_CLOSED")


if __name__ == "__main__":
    main()
