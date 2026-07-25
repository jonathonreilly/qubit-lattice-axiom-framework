#!/usr/bin/env python3
"""Rank and local-loop baseline for the recurrent L-shaped CAR handoff.

This runner independently reconstructs the fixed-register owner's L-shaped
residual, rather than trusting the earlier reported census.  It then treats
that residual as a quadratic form over GF(2), derives an exact symplectic
factorization, and executes every factor through one reusable dirty Z2 loop
M2.  The factorization closes the finite L residual but is not promoted to a
recurrent law: its masks were extracted from the finite target comparison.

The decisive recurrent controls are therefore negative but narrow.  The same
unrefitted local-owner construction has increasing ranks on 2x2 and 3x3
center blocks, and the isolated axial handoff has four distinct words under
the four proper rotations fixing its edge.  A scalar unoriented edge flag
cannot carry that transported chart.  A covariant transported four-state
chart or a different plaquette law remains live.
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations, permutations, product
import json

import frontier_full128_cycle_cocycle_intertwiner_2026_07_24 as c655
import frontier_two_adjacent_seam_chart_transition_2026_07_25 as adjacent
import frontier_two_star_fixed_register_local_executor_2026_07_25 as fixed
import frontier_two_star_staggered_endpoint_feature_route_c_2026_07_25 as route_c


Coord = tuple[int, int, int]
Pair = tuple[int, int]
Site = tuple[Coord, int]
SitePair = tuple[Site, Site]


def add(left: Coord, right: Coord) -> Coord:
    return tuple(left[axis] + right[axis] for axis in range(3))  # type: ignore[return-value]


def sub(left: Coord, right: Coord) -> Coord:
    return tuple(left[axis] - right[axis] for axis in range(3))  # type: ignore[return-value]


def l1(left: Coord, right: Coord) -> int:
    return sum(abs(left[axis] - right[axis]) for axis in range(3))


def independent_geometry(
    centers: tuple[Coord, ...],
) -> tuple[tuple[Coord, ...], tuple[tuple[Coord, Coord], ...], tuple[int, ...]]:
    """Rebuild the first-owner finite geometry without calling fixed.geometry."""

    cells = set(centers)
    edges: list[tuple[Coord, Coord]] = []
    owners: list[int] = []
    seen: set[tuple[Coord, Coord]] = set()
    for owner, center in enumerate(centers):
        for direction in route_c.DIRECTIONS:
            arm = add(center, direction)
            cells.add(arm)
            key = tuple(sorted((center, arm)))
            if key in seen:
                continue
            seen.add(key)
            edges.append((center, arm))
            owners.append(owner)
    return tuple(sorted(cells)), tuple(edges), tuple(owners)


def independent_specs(
    cells: tuple[Coord, ...], edges: tuple[tuple[Coord, Coord], ...]
) -> tuple[adjacent.EdgeSpec, ...]:
    rows = []
    for left_cell, right_cell in edges:
        direction = sub(right_cell, left_cell)
        left_index = cells.index(left_cell)
        right_index = cells.index(right_cell)
        left_mode = route_c.DIRECTION_INDEX[direction]
        right_mode = route_c.DIRECTION_INDEX[
            tuple(-value for value in direction)
        ]
        rows.append(
            (
                6 * left_index + left_mode,
                6 * right_index + right_mode,
                tuple(
                    6 * left_index + position
                    if position < 6
                    else 6 * right_index + position - 6
                    for position in range(left_mode + 1, 6 + right_mode)
                ),
            )
        )
    return tuple(rows)


def toggle(pairs: set[Pair], pair: Pair) -> None:
    ordered = tuple(sorted(pair))
    if ordered in pairs:
        pairs.remove(ordered)
    else:
        pairs.add(ordered)


def independent_local_owned_target(
    global_cells: tuple[Coord, ...], owned_edges: tuple[tuple[Coord, Coord], ...]
) -> set[Pair]:
    local_cells = tuple(sorted({cell for edge in owned_edges for cell in edge}))
    local_specs = independent_specs(local_cells, owned_edges)
    target = adjacent.transition_pair_set(6 * len(local_cells), local_specs)[2]
    local_to_global = tuple(
        6 * global_cells.index(cell) + mode
        for cell in local_cells
        for mode in range(6)
    )
    return {
        tuple(sorted((local_to_global[left], local_to_global[right])))
        for left, right in target
    }


def owner_residual(
    centers: tuple[Coord, ...], order: tuple[int, ...] | None = None
) -> dict[str, object]:
    cells, edges, owners = independent_geometry(centers)
    specs = independent_specs(cells, edges)
    target = adjacent.transition_pair_set(6 * len(cells), specs)[2]
    if order is None:
        order = tuple(range(len(centers)))
    source_at_current = list(range(6 * len(cells)))
    local_word: set[Pair] = set()
    for owner in order:
        owned = tuple(
            edge for edge, edge_owner in zip(edges, owners) if edge_owner == owner
        )
        for left, right in independent_local_owned_target(cells, owned):
            toggle(
                local_word,
                (source_at_current[left], source_at_current[right]),
            )
        for spec, edge_owner in zip(specs, owners):
            if edge_owner != owner:
                continue
            left, right = spec[:2]
            source_at_current[left], source_at_current[right] = (
                source_at_current[right],
                source_at_current[left],
            )
    residual = local_word ^ target
    distances = Counter(
        l1(cells[left // 6], cells[right // 6]) for left, right in residual
    )
    return {
        "centers": centers,
        "cells": cells,
        "edges": edges,
        "owners": owners,
        "specs": specs,
        "owner_order": order,
        "local_word": local_word,
        "target": target,
        "residual": residual,
        "residual_pairs": len(residual),
        "residual_distance_census": dict(sorted(distances.items())),
        "maximum_residual_cell_distance": max(distances, default=0),
    }


def adjacency_rows(pairs: set[Pair], mode_count: int) -> list[int]:
    rows = [0] * mode_count
    for left, right in pairs:
        rows[left] ^= 1 << right
        rows[right] ^= 1 << left
    return rows


def gf2_rank_rows(rows: list[int], width: int) -> int:
    work = list(rows)
    rank = 0
    for column in range(width):
        pivot = next(
            (
                row
                for row in range(rank, len(work))
                if (work[row] >> column) & 1
            ),
            None,
        )
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        for row in range(len(work)):
            if row != rank and ((work[row] >> column) & 1):
                work[row] ^= work[rank]
        rank += 1
    return rank


def pair_rank(pairs: set[Pair], mode_count: int) -> int:
    return gf2_rank_rows(adjacency_rows(pairs, mode_count), mode_count)


def pair_word_from_channel(first: int, second: int, mode_count: int) -> set[Pair]:
    return {
        (left, right)
        for left, right in combinations(range(mode_count), 2)
        if (((first >> left) & 1) & ((second >> right) & 1))
        ^ (((second >> left) & 1) & ((first >> right) & 1))
    }


def symplectic_channels(
    pairs: set[Pair], mode_count: int
) -> tuple[tuple[int, int], ...]:
    """Factor an alternating matrix as sum a b^T + b a^T over GF(2)."""

    rows = adjacency_rows(pairs, mode_count)
    channels = []
    while any(rows):
        first_pivot = next(index for index, row in enumerate(rows) if row)
        second_pivot = (rows[first_pivot] & -rows[first_pivot]).bit_length() - 1
        first = sum(
            ((rows[row] >> second_pivot) & 1) << row
            for row in range(mode_count)
        )
        second = sum(
            ((rows[row] >> first_pivot) & 1) << row
            for row in range(mode_count)
        )
        channels.append((first, second))
        for row in range(mode_count):
            if (first >> row) & 1:
                rows[row] ^= second
            if (second >> row) & 1:
                rows[row] ^= first
    return tuple(channels)


def channel_support_diameter(
    channel: tuple[int, int], cells: tuple[Coord, ...]
) -> int:
    support_cells = {
        cells[mode // 6]
        for mode in range(6 * len(cells))
        if ((channel[0] | channel[1]) >> mode) & 1
    }
    return max(
        (l1(left, right) for left in support_cells for right in support_cells),
        default=0,
    )


def channel_certificate(row: dict[str, object]) -> dict[str, object]:
    cells = row["cells"]
    pairs = row["residual"]
    if not isinstance(cells, tuple) or not isinstance(pairs, set):
        raise TypeError("malformed residual row")
    mode_count = 6 * len(cells)
    channels = symplectic_channels(pairs, mode_count)
    reconstructed: set[Pair] = set()
    for first, second in channels:
        reconstructed ^= pair_word_from_channel(first, second, mode_count)

    labels = ((),) + tuple((mode,) for mode in range(mode_count)) + tuple(
        combinations(range(mode_count), 2)
    )
    truth_failures = work_return_failures = 0
    delete_echo_failures = delete_use_failures = 0
    delete_compute_failures = delete_uncompute_failures = 0
    for first, second in channels:
        channel_pairs = pair_word_from_channel(first, second, mode_count)
        overlap = first & second
        for label in labels:
            value = sum(1 << mode for mode in label)
            first_parity = (value & first).bit_count() & 1
            second_parity = (value & second).bit_count() & 1
            overlap_parity = (value & overlap).bit_count() & 1
            expected = sum(
                ((value >> left) & 1) & ((value >> right) & 1)
                for left, right in channel_pairs
            ) & 1
            for scratch in (0, 1):
                # Dirty-tolerant echo:
                # CZ(s,b); s ^= a; CZ(s,b); s ^= a; Z_(a intersect b).
                observed = (
                    scratch * second_parity
                    + (scratch ^ first_parity) * second_parity
                    + overlap_parity
                ) & 1
                truth_failures += observed != expected
                returned = scratch ^ first_parity ^ first_parity
                work_return_failures += returned != scratch
                delete_echo = (
                    (scratch ^ first_parity) * second_parity + overlap_parity
                ) & 1
                delete_use = scratch * second_parity + overlap_parity
                delete_compute = overlap_parity
                delete_uncompute = observed
                delete_echo_failures += delete_echo != expected
                delete_use_failures += delete_use != expected
                delete_compute_failures += delete_compute != expected
                delete_uncompute_failures += (
                    delete_uncompute != expected
                    or (scratch ^ first_parity) != scratch
                )
    return {
        "alternating_GF2_rank": pair_rank(pairs, mode_count),
        "minimum_parity_product_channels_for_this_quadratic_form": len(channels),
        "channel_weights": tuple(
            (first.bit_count(), second.bit_count(), (first & second).bit_count())
            for first, second in channels
        ),
        "maximum_channel_cell_diameter": max(
            (channel_support_diameter(channel, cells) for channel in channels),
            default=0,
        ),
        "reconstructed_pair_symmetric_difference": len(reconstructed ^ pairs),
        "n_le_2_channel_truth_cases_including_dirty_loop": (
            len(channels) * len(labels) * 2
        ),
        "dirty_loop_phase_failures": truth_failures,
        "dirty_loop_return_failures": work_return_failures,
        "delete_first_echo_detected_cases": delete_echo_failures,
        "delete_second_use_detected_cases": delete_use_failures,
        "delete_compute_detected_cases": delete_compute_failures,
        "delete_uncompute_detected_cases": delete_uncompute_failures,
        "reusable_loop_M2": 1,
        "loop_initialization_required": False,
        "macro": (
            "CZ(loop,b); compute parity a into loop; CZ(loop,b); uncompute a; "
            "apply Z on a-intersect-b to cancel Boolean diagonal terms"
        ),
        "finite_target_extracted_masks": True,
        "recurrent_rule_claimed": False,
    }


def incidence_certificate(row: dict[str, object]) -> dict[str, object]:
    centers = row["centers"]
    cells = row["cells"]
    pairs = row["residual"]
    if not isinstance(centers, tuple) or not isinstance(cells, tuple) or not isinstance(pairs, set):
        raise TypeError("malformed incidence row")
    signatures = Counter()
    incidence_phase_classes: dict[tuple[int, int, int], set[int]] = {}
    outside_corner_support = 0
    qutrit_state_phase_classes: dict[tuple[int, int], set[int]] = {}
    occupied_endpoint_outer_tag_one_rows = 0
    pair_addresses = 0
    for left, right in combinations(range(6 * len(cells)), 2):
        first_cell, second_cell = cells[left // 6], cells[right // 6]
        first_incidence = sum(
            (l1(first_cell, center) <= 1) << index
            for index, center in enumerate(centers)
        )
        second_incidence = sum(
            (l1(second_cell, center) <= 1) << index
            for index, center in enumerate(centers)
        )
        signature = (
            min(first_incidence, second_incidence),
            max(first_incidence, second_incidence),
            l1(first_cell, second_cell),
        )
        required_phase = int((left, right) in pairs)
        incidence_phase_classes.setdefault(signature, set()).add(required_phase)
        qutrit_state_phase_classes.setdefault((1, 1), set()).add(required_phase)
        pair_addresses += 1

        # Under the declared feature-word/role rule, an occupied endpoint's
        # qutrit word is 01.  If the particles share a cell the carrier is the
        # sentinel; otherwise every allowed carrier excludes the occupied
        # mode.  This is an analytic address classification, not construction
        # of the extended L-patch qutrit histories.
        if left // 6 == right // 6:
            occupied_endpoint_outer_tag_one_rows += 0
        else:
            for occupied in (left % 6, right % 6):
                occupied_endpoint_outer_tag_one_rows += sum(
                    carrier == occupied
                    for carrier in range(6)
                    if carrier != occupied
                )

        if required_phase:
            signatures[signature] += 1
            outside_corner_support += first_incidence == 0 or second_incidence == 0
    lawful_qutrits = tuple(sorted(fixed.refresh.qcore.LAWFUL_QUTRIT_WORDS))
    return {
        "corner_incidence_classes": {
            repr(key): value for key, value in sorted(signatures.items())
        },
        "corner_incidence_class_count": len(signatures),
        "residual_pairs_outside_three_star_corner_support": outside_corner_support,
        "lawful_endpoint_qutrit_words": lawful_qutrits,
        "two_particle_mode_address_rows": pair_addresses,
        "qutrit_state_only_required_negative_addresses": len(pairs),
        "qutrit_state_only_required_positive_addresses": pair_addresses - len(pairs),
        "qutrit_state_only_sign_conflicts": sum(
            len(phases) > 1 for phases in qutrit_state_phase_classes.values()
        ),
        "incidence_conditioned_sign_conflicts": sum(
            len(phases) > 1 for phases in incidence_phase_classes.values()
        ),
        "declared_rule_occupied_endpoint_outer_tag_one_rows": (
            occupied_endpoint_outer_tag_one_rows
        ),
        "declared_rule_occupied_endpoint_qutrit_word": 1,
        "extended_L_qutrit_histories_constructed": False,
        "full_qutrit_chart_conditioning_closed": False,
        "load_bearing_qutrit_result": (
            "under the declared endpoint rule, state 01 occurs at both required "
            "signs; endpoint state alone is insufficient, while full qutrit-chart "
            "conditioning remains open"
        ),
    }


def site_word(row: dict[str, object]) -> set[SitePair]:
    cells = row["cells"]
    pairs = row["residual"]
    if not isinstance(cells, tuple) or not isinstance(pairs, set):
        raise TypeError("malformed site word")
    return {
        tuple(
            sorted(
                (
                    (cells[left // 6], left % 6),
                    (cells[right // 6], right % 6),
                )
            )
        )
        for left, right in pairs
    }


def transform_site_word(frame, word: set[SitePair]) -> set[SitePair]:
    frame_tuple = route_c.frame_tuple(frame)
    mode_map = c655.P.mode_map(frame)
    return {
        tuple(
            sorted(
                (
                    (route_c.matvec(frame_tuple, first[0]), int(mode_map[first[1]])),
                    (route_c.matvec(frame_tuple, second[0]), int(mode_map[second[1]])),
                )
            )
        )
        for first, second in word
    }


def axial_covariance_certificate(edge_row: dict[str, object]) -> dict[str, object]:
    word = site_word(edge_row)
    stabilizer = tuple(
        frame
        for frame in c655.P.FRAMES
        if route_c.matvec(route_c.frame_tuple(frame), (1, 0, 0)) == (1, 0, 0)
    )
    stabilizer_words = tuple(transform_site_word(frame, word) for frame in stabilizer)
    orbit = tuple(transform_site_word(frame, word) for frame in c655.P.FRAMES)
    frame_set = {
        route_c.frame_tuple(frame) for frame in c655.P.FRAMES
    }
    closure_failures = 0
    composition_failures = 0
    for left in c655.P.FRAMES:
        for right in c655.P.FRAMES:
            closure_failures += route_c.frame_tuple(left @ right) not in frame_set
            staged = transform_site_word(left, transform_site_word(right, word))
            direct = transform_site_word(left @ right, word)
            composition_failures += staged != direct
    return {
        "proper_cubic_frames": len(c655.P.FRAMES),
        "ordered_frame_products": len(c655.P.FRAMES) ** 2,
        "axial_stabilizer_frames": len(stabilizer),
        "distinct_axial_stabilizer_words": len(
            {frozenset(row) for row in stabilizer_words}
        ),
        "axial_stabilizer_symmetric_differences_from_base": tuple(
            sorted(len(row ^ word) for row in stabilizer_words)
        ),
        "full_transported_edge_word_orbit": len({frozenset(row) for row in orbit}),
        "frame_group_closure_failures": closure_failures,
        "transported_word_composition_failures": composition_failures,
        "scalar_unoriented_edge_rule_covariant": len(
            {frozenset(row) for row in stabilizer_words}
        ) == 1,
        "transported_chart_family_covariant": composition_failures == 0,
        "ambient_common_E_matrices_rebuilt_per_frame": False,
    }


def rectangle_centers(width: int, height: int) -> tuple[Coord, ...]:
    return tuple(
        (x, y, 0) for y in range(height) for x in range(width)
    )


def main() -> None:
    l_centers = ((0, 0, 0), (1, 0, 0), (0, 1, 0))
    independent = tuple(
        owner_residual(l_centers, order)
        for order in permutations(range(3))
    )
    source = fixed.l_shape_coloring_probe()
    independent_summary = tuple(
        {
            "owner_order": row["owner_order"],
            "residual_pairs": row["residual_pairs"],
            "distance_census": row["residual_distance_census"],
            "alternating_GF2_rank": pair_rank(row["residual"], 96),
        }
        for row in independent
    )
    independent_crosscheck = {
        "source_minimum_pairs": source["minimum_naive_coloring_mismatch_pairs"],
        "source_maximum_pairs": source["maximum_naive_coloring_mismatch_pairs"],
        "independent_minimum_pairs": min(row["residual_pairs"] for row in independent),
        "independent_maximum_pairs": max(row["residual_pairs"] for row in independent),
        "all_six_source_orders_reproduced": tuple(
            row["owner_order"] for row in independent_summary
        ) == tuple(row["owner_order"] for row in source["owner_order_rows"]),
        "independent_rows": independent_summary,
    }

    base_l = independent[0]
    transition = adjacent.transition_pair_set(
        96, base_l["specs"]
    )[0]
    transition_distance = Counter(
        l1(base_l["cells"][left // 6], base_l["cells"][right // 6])
        for left, right in transition
    )
    distance_three = {
        pair
        for pair in base_l["residual"]
        if l1(base_l["cells"][pair[0] // 6], base_l["cells"][pair[1] // 6])
        == 3
    }
    base_channels = channel_certificate(base_l)
    distance_three_channels = {
        "pairs": len(distance_three),
        "alternating_GF2_rank": pair_rank(distance_three, 96),
        "minimum_parity_product_channels_for_this_quadratic_subword": (
            pair_rank(distance_three, 96) // 2
        ),
    }

    edge = owner_residual(((0, 0, 0), (1, 0, 0)))
    chain = owner_residual(((0, 0, 0), (1, 0, 0), (2, 0, 0)))
    square = owner_residual(rectangle_centers(2, 2))
    held = owner_residual(rectangle_centers(3, 3))
    scaling = tuple(
        {
            "fixture": name,
            "centers": len(row["centers"]),
            "cells": len(row["cells"]),
            "owned_edges": len(row["edges"]),
            "residual_pairs": row["residual_pairs"],
            "alternating_GF2_rank": pair_rank(
                row["residual"], 6 * len(row["cells"])
            ),
            "parity_product_channels": pair_rank(
                row["residual"], 6 * len(row["cells"])
            )
            // 2,
            "maximum_residual_cell_distance": row[
                "maximum_residual_cell_distance"
            ],
            "held_parameters_refit": 0,
        }
        for name, row in (
            ("adjacent-two-center", edge),
            ("three-center-chain", chain),
            ("three-center-L", base_l),
            ("two-by-two-centers", square),
            ("three-by-three-centers", held),
        )
    )

    order_delta = independent[0]["residual"] ^ independent[1]["residual"]
    local_order_handoff = {
        "orders": (
            independent[0]["owner_order"],
            independent[1]["owner_order"],
        ),
        "same_color_owner_swap_pair_delta": len(order_delta),
        "same_color_owner_swap_alternating_rank": pair_rank(order_delta, 96),
        "same_color_owner_swap_parity_channels": pair_rank(order_delta, 96) // 2,
        "one_local_Z2_order_handoff_bit_suffices_for_this_swap": (
            pair_rank(order_delta, 96) == 2
        ),
    }

    incidence = incidence_certificate(base_l)
    covariance = axial_covariance_certificate(edge)
    certificate = {
        "authority": "none",
        "audit": "unset",
        "status": "finite-L-loop-rank-and-declared-endpoint-class-closed-full-chart-and-recurrence-open",
        "source_crosscheck": independent_crosscheck,
        "whole_patch_transition": {
            "pairs": len(transition),
            "distance_census": dict(sorted(transition_distance.items())),
            "distance_gt_2_pairs": sum(
                count for distance, count in transition_distance.items() if distance > 2
            ),
        },
        "finite_L_loop_factorization": base_channels,
        "distance_three_subword": distance_three_channels,
        "endpoint_and_corner_incidence": incidence,
        "local_order_handoff": local_order_handoff,
        "held_scaling_no_refit": scaling,
        "edge_chart_covariance": covariance,
        "supplied": (
            "the finite exterior target used only as a comparison oracle",
            "first-owner finite patch order in the diagnostic scaling rows",
            "the local star chart and direction-mode labels",
            "one reusable loop scratch M2 and a bounded factor program",
        ),
        "not_claimed": (
            "a target-independent recurrent plaquette law",
            "a scalar unoriented proper-cubic edge handoff",
            "a physical common-E intertwiner on the held center blocks",
            "conditioning on constructed extended L-patch qutrit histories",
            "a route-independent obstruction, minimum substrate content, or axiom pressure",
        ),
    }
    print("L_SHAPE_LOCAL_GAUGE_HANDOFF_RANK_PROBE")
    print(json.dumps(certificate, sort_keys=True, default=str))

    assert independent_crosscheck["source_minimum_pairs"] == 178
    assert independent_crosscheck["source_maximum_pairs"] == 178
    assert independent_crosscheck["independent_minimum_pairs"] == 178
    assert independent_crosscheck["independent_maximum_pairs"] == 178
    assert independent_crosscheck["all_six_source_orders_reproduced"]
    assert all(row["alternating_GF2_rank"] == 10 for row in independent_summary)
    assert len(transition) == 454
    assert dict(sorted(transition_distance.items())) == {0: 48, 1: 174, 2: 176, 3: 56}
    assert sum(count for distance, count in transition_distance.items() if distance > 2) == 56
    assert base_channels["alternating_GF2_rank"] == 10
    assert base_channels[
        "minimum_parity_product_channels_for_this_quadratic_form"
    ] == 5
    assert base_channels["reconstructed_pair_symmetric_difference"] == 0
    assert base_channels["dirty_loop_phase_failures"] == 0
    assert base_channels["dirty_loop_return_failures"] == 0
    assert base_channels["delete_first_echo_detected_cases"] > 0
    assert base_channels["delete_second_use_detected_cases"] > 0
    assert base_channels["delete_compute_detected_cases"] > 0
    assert base_channels["delete_uncompute_detected_cases"] > 0
    assert distance_three_channels == {
        "pairs": 56,
        "alternating_GF2_rank": 6,
        "minimum_parity_product_channels_for_this_quadratic_subword": 3,
    }
    assert incidence["residual_pairs_outside_three_star_corner_support"] == 0
    assert incidence["two_particle_mode_address_rows"] == 4560
    assert incidence["qutrit_state_only_required_negative_addresses"] == 178
    assert incidence["qutrit_state_only_required_positive_addresses"] == 4382
    assert incidence["qutrit_state_only_sign_conflicts"] == 1
    assert incidence["incidence_conditioned_sign_conflicts"] > 0
    assert incidence["declared_rule_occupied_endpoint_outer_tag_one_rows"] == 0
    assert not incidence["extended_L_qutrit_histories_constructed"]
    assert not incidence["full_qutrit_chart_conditioning_closed"]
    assert local_order_handoff["same_color_owner_swap_pair_delta"] == 8
    assert local_order_handoff["same_color_owner_swap_alternating_rank"] == 2
    assert [
        (row["residual_pairs"], row["alternating_GF2_rank"], row["maximum_residual_cell_distance"])
        for row in scaling
    ] == [(24, 2, 2), (48, 4, 2), (178, 10, 3), (250, 16, 3), (942, 36, 4)]
    assert covariance["proper_cubic_frames"] == 24
    assert covariance["ordered_frame_products"] == 576
    assert covariance["axial_stabilizer_frames"] == 4
    assert covariance["distinct_axial_stabilizer_words"] == 4
    assert covariance["axial_stabilizer_symmetric_differences_from_base"] == (0, 24, 24, 48)
    assert covariance["frame_group_closure_failures"] == 0
    assert covariance["transported_word_composition_failures"] == 0
    assert not covariance["scalar_unoriented_edge_rule_covariant"]
    assert covariance["transported_chart_family_covariant"]
    print("L_SHAPE_RANK10_FIVE_LOOP_CHANNELS_CLOSED_RECURRENT_HANDOFF_OPEN")


if __name__ == "__main__":
    main()
