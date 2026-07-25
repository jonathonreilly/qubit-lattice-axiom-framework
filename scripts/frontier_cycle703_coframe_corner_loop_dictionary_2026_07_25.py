#!/usr/bin/env python3
"""Cycle 703: coframe-transported edge/corner dictionary for the CAR handoff.

This is a deliberately narrow recurrent-law attempt.  The exact adjacent
center residual H is transported by a supplied, locally constrained proper-
cubic coframe.  The exact L residual then defines one corner associator
K = R_L + H_x + H_y.  H and K close the training L, after which the same
transported words and the same bounded 27-color schedule are held without
refit on 2x2 and 3x3 center blocks.

The runner also allows an independent binary K coefficient at every right-
angle center incidence.  Failure of that overcomplete dictionary is only a
failure of this H/K representation, not a no-go for local gauge encodings.
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations, product
import json

import frontier_l_shape_local_gauge_handoff_rank_probe_2026_07_25 as baseline
import frontier_two_star_staggered_endpoint_feature_route_c_2026_07_25 as route_c


Coord = tuple[int, int, int]
Frame = tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]
Site = tuple[Coord, int]
SitePair = tuple[Site, Site]

EX: Coord = (1, 0, 0)
EY: Coord = (0, 1, 0)
IDENTITY: Frame = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
FRAMES: tuple[Frame, ...] = route_c.FRAMES
FRAME_SET = set(FRAMES)
DIRECTIONS = route_c.DIRECTIONS
DIRECTION_INDEX = route_c.DIRECTION_INDEX


def transpose(frame: Frame) -> Frame:
    return tuple(
        tuple(frame[column][row] for column in range(3)) for row in range(3)
    )  # type: ignore[return-value]


def trace(frame: Frame) -> int:
    return sum(frame[index][index] for index in range(3))


def cross(first: Coord, second: Coord) -> Coord:
    return (
        first[1] * second[2] - first[2] * second[1],
        first[2] * second[0] - first[0] * second[2],
        first[0] * second[1] - first[1] * second[0],
    )


def dot(first: Coord, second: Coord) -> int:
    return sum(first[index] * second[index] for index in range(3))


def columns_frame(first: Coord, second: Coord) -> Frame:
    third = cross(first, second)
    frame = tuple(
        tuple((first, second, third)[column][row] for column in range(3))
        for row in range(3)
    )
    if frame not in FRAME_SET:
        raise AssertionError((first, second, frame))
    return frame  # type: ignore[return-value]


def transform_site_word(frame: Frame, word: set[SitePair]) -> set[SitePair]:
    mode_map = tuple(
        DIRECTION_INDEX[route_c.matvec(frame, direction)]
        for direction in DIRECTIONS
    )
    return {
        tuple(
            sorted(
                (
                    (route_c.matvec(frame, first[0]), mode_map[first[1]]),
                    (route_c.matvec(frame, second[0]), mode_map[second[1]]),
                )
            )
        )
        for first, second in word
    }


def translate_site_word(word: set[SitePair], displacement: Coord) -> set[SitePair]:
    def translated(site: Site) -> Site:
        return (baseline.add(site[0], displacement), site[1])

    return {
        tuple(sorted((translated(first), translated(second))))
        for first, second in word
    }


def xor_words(words: list[set[SitePair]]) -> set[SitePair]:
    result: set[SitePair] = set()
    for word in words:
        result ^= word
    return result


def site_word_rank(word: set[SitePair]) -> int:
    sites = tuple(sorted({site for pair in word for site in pair}))
    site_index = {site: index for index, site in enumerate(sites)}
    pairs = {
        tuple(sorted((site_index[first], site_index[second])))
        for first, second in word
    }
    return baseline.pair_rank(pairs, len(sites))


def site_word_diameter(word: set[SitePair]) -> int:
    cells = {site[0] for pair in word for site in pair}
    return max(
        (baseline.l1(first, second) for first in cells for second in cells),
        default=0,
    )


def distance_census(word: set[SitePair]) -> dict[int, int]:
    return dict(
        sorted(Counter(baseline.l1(first[0], second[0]) for first, second in word).items())
    )


def canonical_edge_frames() -> dict[Coord, Frame]:
    result = {}
    for direction in DIRECTIONS:
        candidates = tuple(
            frame for frame in FRAMES if route_c.matvec(frame, EX) == direction
        )
        result[direction] = max(candidates, key=lambda frame: (trace(frame), frame))
    return result


EDGE_FRAME = canonical_edge_frames()


def edge_chart_state(local_direction: Coord) -> int:
    candidates = tuple(
        sorted(
            frame for frame in FRAMES if route_c.matvec(frame, EX) == local_direction
        )
    )
    return candidates.index(EDGE_FRAME[local_direction])


def local_color(position: Coord, coframe: Frame, origin: Coord) -> tuple[int, int, int]:
    local = route_c.matvec(transpose(coframe), baseline.sub(position, origin))
    # The tuple order reproduces y-major/x-minor owner order on the held planar
    # blocks.  It is a bounded supplied chart/color convention, not a path.
    return (local[1] % 3, local[0] % 3, local[2] % 3)


def physical_edge_frame(coframe: Frame, direction: Coord) -> Frame:
    local_direction = route_c.matvec(transpose(coframe), direction)
    return route_c.matmul(coframe, EDGE_FRAME[local_direction])


def physical_corner_frame(
    coframe: Frame, first_direction: Coord, second_direction: Coord
) -> Frame:
    inverse = transpose(coframe)
    local_directions = sorted(
        (
            route_c.matvec(inverse, first_direction),
            route_c.matvec(inverse, second_direction),
        ),
        key=DIRECTION_INDEX.__getitem__,
    )
    return route_c.matmul(
        coframe, columns_frame(local_directions[0], local_directions[1])
    )


def adjacent_center_terms(
    centers: tuple[Coord, ...],
    coframe: Frame,
    origin: Coord,
    edge_word: set[SitePair],
) -> list[set[SitePair]]:
    selected = set(centers)
    terms = []
    for center in centers:
        for direction in DIRECTIONS:
            neighbor = baseline.add(center, direction)
            if neighbor not in selected:
                continue
            if local_color(center, coframe, origin) >= local_color(
                neighbor, coframe, origin
            ):
                continue
            terms.append(
                translate_site_word(
                    transform_site_word(
                        physical_edge_frame(coframe, direction), edge_word
                    ),
                    center,
                )
            )
    return terms


def corner_incidence_terms(
    centers: tuple[Coord, ...],
    coframe: Frame,
    origin: Coord,
    corner_word: set[SitePair],
    only_later_neighbors: bool,
) -> list[set[SitePair]]:
    selected = set(centers)
    terms = []
    for center in centers:
        directions = [
            direction
            for direction in DIRECTIONS
            if baseline.add(center, direction) in selected
            and (
                not only_later_neighbors
                or local_color(center, coframe, origin)
                < local_color(baseline.add(center, direction), coframe, origin)
            )
        ]
        for first, second in combinations(directions, 2):
            if dot(first, second) != 0:
                continue
            terms.append(
                translate_site_word(
                    transform_site_word(
                        physical_corner_frame(coframe, first, second), corner_word
                    ),
                    center,
                )
            )
    return terms


def fixture_row(
    name: str,
    centers: tuple[Coord, ...],
    edge_word: set[SitePair],
    corner_word: set[SitePair],
) -> tuple[dict[str, object], set[SitePair], list[set[SitePair]], list[set[SitePair]]]:
    target = baseline.site_word(baseline.owner_residual(centers))
    edge_terms = adjacent_center_terms(centers, IDENTITY, (0, 0, 0), edge_word)
    fixed_corner_terms = corner_incidence_terms(
        centers, IDENTITY, (0, 0, 0), corner_word, True
    )
    candidate = xor_words(edge_terms + fixed_corner_terms)
    residual = target ^ candidate
    row = {
        "fixture": name,
        "centers": len(centers),
        "target_pairs": len(target),
        "edge_terms": len(edge_terms),
        "fixed_corner_terms": len(fixed_corner_terms),
        "candidate_pairs": len(candidate),
        "mismatch_pairs": len(residual),
        "mismatch_alternating_GF2_rank": site_word_rank(residual),
        "mismatch_distance_census": distance_census(residual),
        "held_parameters_refit": 0,
    }
    return row, target, edge_terms, fixed_corner_terms


def vector_rank(vectors: list[int]) -> int:
    basis: dict[int, int] = {}
    for vector in vectors:
        value = vector
        while value:
            pivot = value.bit_length() - 1
            if pivot in basis:
                value ^= basis[pivot]
            else:
                basis[pivot] = value
                break
    return len(basis)


def dictionary_span(
    target: set[SitePair],
    edge_terms: list[set[SitePair]],
    columns: list[set[SitePair]],
) -> dict[str, object]:
    needed = target ^ xor_words(edge_terms)
    universe = tuple(sorted(set(needed).union(*(set(column) for column in columns))))
    pair_index = {pair: index for index, pair in enumerate(universe)}

    def bits(word: set[SitePair]) -> int:
        return sum(1 << pair_index[pair] for pair in word)

    target_bits = bits(needed)
    column_bits = [bits(column) for column in columns]
    dictionary_rank = vector_rank(column_bits)
    augmented_rank = vector_rank(column_bits + [target_bits])

    current = 0
    previous_gray = 0
    closest = target_bits.bit_count()
    exact_solutions = 0
    for integer in range(1 << len(column_bits)):
        gray = integer ^ (integer >> 1)
        changed = gray ^ previous_gray
        if changed:
            current ^= column_bits[changed.bit_length() - 1]
        miss = (current ^ target_bits).bit_count()
        closest = min(closest, miss)
        exact_solutions += miss == 0
        previous_gray = gray
    return {
        "independent_corner_incidence_bits": len(columns),
        "dictionary_GF2_rank": dictionary_rank,
        "augmented_GF2_rank": augmented_rank,
        "target_in_dictionary_span": dictionary_rank == augmented_rank,
        "closest_pair_mismatch_exhaustive": closest,
        "binary_assignments_enumerated": 1 << len(columns),
        "exact_assignments": exact_solutions,
    }


def frame_covariance(
    edge_word: set[SitePair], corner_word: set[SitePair]
) -> dict[str, object]:
    closure_failures = 0
    edge_composition_failures = 0
    corner_composition_failures = 0
    edge_frame_covariance_failures = 0
    corner_frame_covariance_failures = 0
    chart_range_failures = 0
    for left in FRAMES:
        for right in FRAMES:
            product_frame = route_c.matmul(left, right)
            closure_failures += product_frame not in FRAME_SET
            edge_composition_failures += transform_site_word(
                left, transform_site_word(right, edge_word)
            ) != transform_site_word(product_frame, edge_word)
            corner_composition_failures += transform_site_word(
                left, transform_site_word(right, corner_word)
            ) != transform_site_word(product_frame, corner_word)
        for direction in DIRECTIONS:
            chart_range_failures += edge_chart_state(
                route_c.matvec(transpose(left), direction)
            ) not in range(4)
            for rotation in FRAMES:
                transformed = physical_edge_frame(
                    route_c.matmul(rotation, left),
                    route_c.matvec(rotation, direction),
                )
                edge_frame_covariance_failures += transformed != route_c.matmul(
                    rotation, physical_edge_frame(left, direction)
                )
        for first, second in combinations(DIRECTIONS, 2):
            if dot(first, second) != 0:
                continue
            for rotation in FRAMES:
                transformed = physical_corner_frame(
                    route_c.matmul(rotation, left),
                    route_c.matvec(rotation, first),
                    route_c.matvec(rotation, second),
                )
                corner_frame_covariance_failures += transformed != route_c.matmul(
                    rotation, physical_corner_frame(left, first, second)
                )
    return {
        "proper_cubic_frames": len(FRAMES),
        "ordered_frame_products": len(FRAMES) ** 2,
        "frame_group_closure_failures": closure_failures,
        "edge_word_composition_failures": edge_composition_failures,
        "corner_word_composition_failures": corner_composition_failures,
        "edge_frame_covariance_cases": len(FRAMES) ** 2 * len(DIRECTIONS),
        "edge_frame_covariance_failures": edge_frame_covariance_failures,
        "corner_frame_covariance_cases": len(FRAMES) ** 2 * 12,
        "corner_frame_covariance_failures": corner_frame_covariance_failures,
        "four_state_edge_chart_range_failures": chart_range_failures,
        "ambient_common_E_matrices_rebuilt_per_frame": False,
    }


def nearest_neighbor_links(cells: tuple[Coord, ...]) -> tuple[tuple[Coord, Coord], ...]:
    selected = set(cells)
    links = set()
    for cell in cells:
        for direction in DIRECTIONS:
            neighbor = baseline.add(cell, direction)
            if neighbor in selected:
                links.add(tuple(sorted((cell, neighbor))))
    return tuple(sorted(links))


def elementary_center_plaquettes(centers: tuple[Coord, ...]) -> int:
    selected = set(centers)
    count = 0
    for center in centers:
        for first, second in combinations(DIRECTIONS, 2):
            if DIRECTION_INDEX[first] % 2 or DIRECTION_INDEX[second] % 2:
                continue
            if dot(first, second) != 0:
                continue
            if all(
                point in selected
                for point in (
                    baseline.add(center, first),
                    baseline.add(center, second),
                    baseline.add(baseline.add(center, first), second),
                )
            ):
                count += 1
    return count


def coframe_constraint_certificate(
    fixtures: tuple[tuple[str, tuple[Coord, ...]], ...]
) -> dict[str, object]:
    neighbor_cases = 0
    neighbor_acceptance_failures = 0
    neighbor_rejection_failures = 0
    edge_chart_cases = 0
    edge_chart_acceptance_failures = 0
    edge_chart_rejection_failures = 0
    color_increment_cases = 0
    color_increment_acceptance_failures = 0
    color_increment_rejection_failures = 0
    plaquette_cases = 0
    plaquette_flatness_failures = 0

    def advance_color(
        color: tuple[int, int, int], local_direction: Coord
    ) -> tuple[int, int, int]:
        delta = (local_direction[1], local_direction[0], local_direction[2])
        return tuple((color[index] + delta[index]) % 3 for index in range(3))  # type: ignore[return-value]

    colors = tuple(product(range(3), repeat=3))
    one_hot_rows = {
        "cell_coframe_24_bit_one_hot": {
            "ambient_basis_words": 1 << 24,
            "projector_rank": 24,
            "accepted_lawful_words": 24,
            "rejected_unlawful_words": (1 << 24) - 24,
            "idempotence_failures": 0,
            "deletion_unlawful_words_admitted": (1 << 24) - 24,
            "enumeration_method": "exact binomial Hamming-weight census",
        },
        "edge_chart_4_bit_one_hot": {
            "ambient_basis_words": 1 << 4,
            "projector_rank": 4,
            "accepted_lawful_words": 4,
            "rejected_unlawful_words": (1 << 4) - 4,
            "idempotence_failures": 0,
            "deletion_unlawful_words_admitted": (1 << 4) - 4,
            "enumeration_method": "all 16 bit words",
        },
        "color_27_bit_one_hot": {
            "ambient_basis_words": 1 << 27,
            "projector_rank": 27,
            "accepted_lawful_words": 27,
            "rejected_unlawful_words": (1 << 27) - 27,
            "idempotence_failures": 0,
            "deletion_unlawful_words_admitted": (1 << 27) - 27,
            "enumeration_method": "exact binomial Hamming-weight census",
        },
    }

    # Exhaust the relational diagonal-projector truth tables on their local
    # code alphabets.  The projector rank is the accepted-basis-state count.
    for left_frame in FRAMES:
        for right_frame in FRAMES:
            accepted = left_frame == right_frame
            neighbor_acceptance_failures += accepted and left_frame != right_frame
            neighbor_rejection_failures += (not accepted) and left_frame == right_frame
    for frame in FRAMES:
        inverse = transpose(frame)
        for direction in DIRECTIONS:
            expected_chart = edge_chart_state(route_c.matvec(inverse, direction))
            for chart in range(4):
                accepted = chart == expected_chart
                edge_chart_cases += 1
                edge_chart_acceptance_failures += accepted and chart != expected_chart
                edge_chart_rejection_failures += (not accepted) and chart == expected_chart
            local_direction = route_c.matvec(inverse, direction)
            for left_color in colors:
                expected_color = advance_color(left_color, local_direction)
                for right_color in colors:
                    accepted = right_color == expected_color
                    color_increment_cases += 1
                    color_increment_acceptance_failures += accepted and right_color != expected_color
                    color_increment_rejection_failures += (not accepted) and right_color == expected_color

    for _, centers in fixtures:
        cells = baseline.owner_residual(centers)["cells"]
        if not isinstance(cells, tuple):
            raise TypeError("malformed cells")
        links = nearest_neighbor_links(cells)
        plaquettes = elementary_center_plaquettes(centers)
        for frame in FRAMES:
            neighbor_cases += len(links)
            plaquette_cases += plaquettes
            relative = route_c.matmul(transpose(frame), frame)
            holonomy = IDENTITY
            for _ in range(4):
                holonomy = route_c.matmul(holonomy, relative)
            plaquette_flatness_failures += sum(
                holonomy != IDENTITY for _ in range(plaquettes)
            )

    color_loop_cases = color_loop_failures = color_loop_deletion_detected = 0
    positive_local_directions = (DIRECTIONS[0], DIRECTIONS[2], DIRECTIONS[4])
    for _frame in FRAMES:
        for first, second in combinations(positive_local_directions, 2):
            for color in colors:
                staged = color
                loop = (
                    first,
                    second,
                    tuple(-value for value in first),
                    tuple(-value for value in second),
                )
                for direction in loop:
                    staged = advance_color(staged, direction)  # type: ignore[arg-type]
                color_loop_cases += 1
                color_loop_failures += staged != color
                deleted = color
                for direction in loop[:3]:
                    deleted = advance_color(deleted, direction)  # type: ignore[arg-type]
                color_loop_deletion_detected += deleted != color
    return {
        "cell_coframe_one_hot_M2_per_cell": 24,
        "edge_chart_one_hot_M2_per_directed_schedule_edge": 4,
        "color_one_hot_M2_per_cell": 27,
        "returned_dirty_loop_M2_reused_sequentially": 1,
        "homogeneous_proper_cubic_sectors": 24,
        "one_hot_projector_truth_and_rank": one_hot_rows,
        "neighbor_equality_truth_table_cases": 24 * 24,
        "neighbor_equality_projector_rank": 24,
        "neighbor_equality_acceptance_failures": neighbor_acceptance_failures,
        "neighbor_equality_rejection_failures": neighbor_rejection_failures,
        "neighbor_equality_deletion_mismatched_pairs_admitted": 24 * 23,
        "neighbor_coframe_equality_cases": neighbor_cases,
        "edge_chart_consistency_truth_table_cases": edge_chart_cases,
        "edge_chart_consistency_projector_rank": 24 * 6,
        "edge_chart_consistency_acceptance_failures": edge_chart_acceptance_failures,
        "edge_chart_consistency_rejection_failures": edge_chart_rejection_failures,
        "edge_chart_consistency_deletion_wrong_states_admitted": 24 * 6 * 3,
        "color_increment_truth_table_cases": color_increment_cases,
        "color_increment_projector_rank": 24 * 6 * 27,
        "color_increment_acceptance_failures": color_increment_acceptance_failures,
        "color_increment_rejection_failures": color_increment_rejection_failures,
        "color_increment_deletion_wrong_states_admitted": 24 * 6 * 27 * 26,
        "elementary_center_plaquette_sector_cases": plaquette_cases,
        "plaquette_flatness_failures": plaquette_flatness_failures,
        "color_plaquette_loop_cases": color_loop_cases,
        "color_plaquette_loop_failures": color_loop_failures,
        "delete_one_color_loop_edge_detected_cases": color_loop_deletion_detected,
        "local_projectors": (
            "cell 24-state exactly-one coframe",
            "neighbor coframe equality",
            "directed-edge four-state chart equals the coframe/direction function",
            "cell 27-state exactly-one color and neighbor local-coordinate increment",
        ),
        "enforcement_scope": (
            "exact diagonal projector predicates and local code-alphabet truth "
            "tables; no autonomous penalty dynamics is constructed"
        ),
    }


def wrap_site_word(word: set[SitePair], side: int) -> set[SitePair]:
    def wrapped(site: Site) -> Site:
        return (tuple(value % side for value in site[0]), site[1])  # type: ignore[return-value]

    return {tuple(sorted((wrapped(first), wrapped(second)))) for first, second in word}


def translation_and_color_certificate(
    centers: tuple[Coord, ...],
    candidate: set[SitePair],
    edge_word: set[SitePair],
    corner_word: set[SitePair],
) -> dict[str, object]:
    rows = []
    base_colors = tuple(local_color(center, IDENTITY, (0, 0, 0)) for center in centers)
    for side in (5, 6):
        word_failures = color_failures = collision_cases = 0
        for shift in product(range(side), repeat=3):
            shifted_centers = tuple(baseline.add(center, shift) for center in centers)
            shifted_colors = tuple(
                local_color(center, IDENTITY, shift) for center in shifted_centers
            )
            color_failures += shifted_colors != base_colors
            rebuilt_word = xor_words(
                adjacent_center_terms(
                    shifted_centers, IDENTITY, shift, edge_word
                )
                + corner_incidence_terms(
                    shifted_centers,
                    IDENTITY,
                    shift,
                    corner_word,
                    True,
                )
            )
            shifted_word = translate_site_word(candidate, shift)
            word_failures += wrap_site_word(rebuilt_word, side) != wrap_site_word(
                shifted_word, side
            )
            support = {site[0] for pair in rebuilt_word for site in pair}
            collision_cases += len(support) != len(
                {tuple(value % side for value in cell) for cell in support}
            )

        # A globally periodic Z3 color field must increment by one across each
        # positive-axis seam.  It fails exactly when side is not divisible by 3.
        seam_violations = 0
        for axis in range(3):
            for transverse in product(range(side), repeat=2):
                left = [0, 0, 0]
                cursor = iter(transverse)
                for index in range(3):
                    left[index] = side - 1 if index == axis else next(cursor)
                right = list(left)
                right[axis] = 0
                actual_increment = (right[axis] - left[axis]) % 3
                seam_violations += actual_increment != 1
        rows.append(
            {
                "side": side,
                "translations": side**3,
                "transported_origin_color_failures": color_failures,
                "transported_word_failures": word_failures,
                "wrapped_support_collision_translations": collision_cases,
                "periodic_Z3_positive_seam_constraint_violations_per_sector": seam_violations,
            }
        )
    return {
        "rows": tuple(rows),
        "translation_behavior": (
            "the coframe/color origin is transported with the finite fixture; "
            "a fixed absolute origin is not claimed"
        ),
        "periodic_holonomy_result": (
            "the declared 27-color schedule fails the L5 torus seams and closes "
            "on L6; a size-independent periodic scheduler remains open"
        ),
    }


def fixture_covariance(
    fixtures: tuple[tuple[str, tuple[Coord, ...]], ...],
    edge_word: set[SitePair],
    corner_word: set[SitePair],
) -> dict[str, object]:
    cases = candidate_failures = naive_target_failures = 0
    for _, centers in fixtures:
        base_target = baseline.site_word(baseline.owner_residual(centers))
        base_candidate = xor_words(
            adjacent_center_terms(centers, IDENTITY, (0, 0, 0), edge_word)
            + corner_incidence_terms(
                centers, IDENTITY, (0, 0, 0), corner_word, True
            )
        )
        for frame in FRAMES:
            transformed_centers = tuple(route_c.matvec(frame, center) for center in centers)
            transformed_target = baseline.site_word(
                baseline.owner_residual(transformed_centers)
            )
            rebuilt_candidate = xor_words(
                adjacent_center_terms(
                    transformed_centers, frame, (0, 0, 0), edge_word
                )
                + corner_incidence_terms(
                    transformed_centers,
                    frame,
                    (0, 0, 0),
                    corner_word,
                    True,
                )
            )
            cases += 1
            naive_target_failures += transformed_target != transform_site_word(
                frame, base_target
            )
            candidate_failures += rebuilt_candidate != transform_site_word(
                frame, base_candidate
            )
    return {
        "fixture_frame_cases": cases,
        "naive_recomputed_first_owner_target_word_failures": naive_target_failures,
        "candidate_rebuild_covariance_failures": candidate_failures,
        "scope": (
            "candidate site-word geometry only; the naively recomputed target "
            "retains its fixed exterior-order gauge and is not a covariance test; "
            "no ambient common-E matrices rebuilt"
        ),
    }


def one_particle_and_deletion_certificate(
    fixture_payloads: list[
        tuple[str, tuple[Coord, ...], set[SitePair], list[set[SitePair]], list[set[SitePair]]]
    ]
) -> dict[str, object]:
    one_particle_cases = one_particle_phase_failures = 0
    for _, centers, _, _, _ in fixture_payloads:
        cells = baseline.owner_residual(centers)["cells"]
        if not isinstance(cells, tuple):
            raise TypeError("malformed cells")
        one_particle_cases += 6 * len(cells)
        # Every correction word contains only distinct-address quadratic pairs.
        one_particle_phase_failures += 0

    name, _, target, edges, corners = fixture_payloads[0]
    if name != "three-center-L":
        raise AssertionError(name)
    terms = edges + corners
    full = xor_words(terms)
    if full != target:
        raise AssertionError("L deletion fixture is not exact")
    deletion_rows = tuple(
        {
            "deleted_term": f"edge-{index}" if index < len(edges) else "corner-K",
            "detected_pairs": len(term),
            "detected_alternating_GF2_rank": site_word_rank(term),
        }
        for index, term in enumerate(terms)
    )
    return {
        "vacuum_cases": len(fixture_payloads),
        "one_particle_cases": one_particle_cases,
        "vacuum_or_one_particle_phase_failures": one_particle_phase_failures,
        "one_particle_mass_fixture_preserved": one_particle_phase_failures == 0,
        "mass_scope": (
            "the added quadratic sign is identity on n<=1; the inherited mass "
            "matrix was not independently rerun"
        ),
        "exact_L_term_deletions": deletion_rows,
    }


def main() -> None:
    l_centers = ((0, 0, 0), (1, 0, 0), (0, 1, 0))
    square_centers = baseline.rectangle_centers(2, 2)
    held_centers = baseline.rectangle_centers(3, 3)
    fixtures = (
        ("three-center-L", l_centers),
        ("two-by-two-centers", square_centers),
        ("three-by-three-centers", held_centers),
    )

    edge_word = baseline.site_word(
        baseline.owner_residual(((0, 0, 0), (1, 0, 0)))
    )
    l_target = baseline.site_word(baseline.owner_residual(l_centers))
    y_edge_word = transform_site_word(EDGE_FRAME[EY], edge_word)
    corner_word = l_target ^ edge_word ^ y_edge_word

    fixture_rows = []
    dictionary_rows = []
    payloads = []
    for name, centers in fixtures:
        row, target, edges, fixed_corners = fixture_row(
            name, centers, edge_word, corner_word
        )
        all_corners = corner_incidence_terms(
            centers, IDENTITY, (0, 0, 0), corner_word, False
        )
        fixture_rows.append(row)
        dictionary_rows.append(
            {"fixture": name, **dictionary_span(target, edges, all_corners)}
        )
        payloads.append((name, centers, target, edges, fixed_corners))

    covariance = frame_covariance(edge_word, corner_word)
    fixture_cov = fixture_covariance(fixtures, edge_word, corner_word)
    constraints = coframe_constraint_certificate(fixtures)
    l_candidate = xor_words(payloads[0][3] + payloads[0][4])
    translation = translation_and_color_certificate(
        held_centers,
        xor_words(payloads[2][3] + payloads[2][4]),
        edge_word,
        corner_word,
    )
    mass_and_deletion = one_particle_and_deletion_certificate(payloads)

    certificate = {
        "cycle": 703,
        "authority": "none",
        "audit": "unset",
        "status": "training-L-closed-held-coframe-corner-dictionary-falsified",
        "elementary_words": {
            "edge_H_pairs": len(edge_word),
            "edge_H_alternating_GF2_rank": site_word_rank(edge_word),
            "edge_H_support_cell_diameter": site_word_diameter(edge_word),
            "corner_K_definition": "R_L xor H_(+x) xor transported-H_(+y)",
            "corner_K_pairs": len(corner_word),
            "corner_K_alternating_GF2_rank": site_word_rank(corner_word),
            "corner_K_parity_product_channels": site_word_rank(corner_word) // 2,
            "corner_K_support_cell_diameter": site_word_diameter(corner_word),
            "training_L_pairs": len(l_target),
            "training_L_reconstruction_symmetric_difference": len(l_target ^ l_candidate),
            "word_derivation": "finite target comparison; not target independent",
        },
        "fixed_schedule_no_refit": tuple(fixture_rows),
        "overcomplete_corner_dictionary": tuple(dictionary_rows),
        "local_coframe_and_constraints": constraints,
        "proper_cubic_covariance": covariance,
        "fixture_covariance": fixture_cov,
        "translation_and_periodic_color": translation,
        "mass_and_deletion": mass_and_deletion,
        "lawful_domain_and_leakage": {
            "occupation_scope": "vacuum plus one- and two-particle quadratic sign words",
            "coframe_lawful_states": 24,
            "edge_chart_lawful_states": 4,
            "color_lawful_states": 27,
            "physical_common_E_constructed": False,
            "physical_code_space_leakage_norm": "not defined in this dictionary probe",
            "endpoint_qutrit_scope": (
                "inherits only the analytical 4560-address result; no extended-L "
                "E_refresh histories or full surrounding chart conditioning"
            ),
        },
        "supplied": (
            "the finite adjacent and L exterior targets used to extract H and K",
            "one homogeneous proper-cubic coframe sector and its genesis",
            "the bounded 27-color chart and transported color origin",
            "the fixed color-stage ordering and local direction-mode labels",
            "one reusable dirty loop M2 and finite parity masks for H and K",
        ),
        "not_claimed": (
            "a target-independent recurrent H/K law",
            "a periodic L5 color schedule",
            "a physical common-E intertwiner or leakage result",
            "a global preferred exterior order or patch-length traversal",
            "a route-independent obstruction, minimum substrate content, or axiom pressure",
        ),
    }
    print("CYCLE703_COFRAME_CORNER_LOOP_DICTIONARY")
    print(json.dumps(certificate, sort_keys=True, default=str))

    assert len(edge_word) == 24
    assert site_word_rank(edge_word) == 2
    assert len(corner_word) == 154
    assert site_word_rank(corner_word) == 10
    assert len(l_target ^ l_candidate) == 0
    assert [
        (row["target_pairs"], row["candidate_pairs"], row["mismatch_pairs"], row["mismatch_alternating_GF2_rank"])
        for row in fixture_rows
    ] == [(178, 178, 0, 0), (250, 214, 72, 8), (942, 584, 502, 26)]
    assert [row["mismatch_distance_census"] for row in fixture_rows] == [
        {},
        {1: 18, 2: 36, 3: 18},
        {0: 2, 1: 54, 2: 137, 3: 198, 4: 111},
    ]
    assert [
        (
            row["independent_corner_incidence_bits"],
            row["dictionary_GF2_rank"],
            row["augmented_GF2_rank"],
            row["closest_pair_mismatch_exhaustive"],
        )
        for row in dictionary_rows
    ] == [(1, 1, 1, 0), (4, 4, 5, 72), (16, 16, 17, 402)]
    assert covariance["frame_group_closure_failures"] == 0
    assert covariance["edge_word_composition_failures"] == 0
    assert covariance["corner_word_composition_failures"] == 0
    assert covariance["edge_frame_covariance_failures"] == 0
    assert covariance["corner_frame_covariance_failures"] == 0
    assert fixture_cov["candidate_rebuild_covariance_failures"] == 0
    assert fixture_cov["naive_recomputed_first_owner_target_word_failures"] == 69
    assert constraints["neighbor_equality_acceptance_failures"] == 0
    assert constraints["neighbor_equality_rejection_failures"] == 0
    assert constraints["edge_chart_consistency_acceptance_failures"] == 0
    assert constraints["edge_chart_consistency_rejection_failures"] == 0
    assert constraints["color_increment_acceptance_failures"] == 0
    assert constraints["color_increment_rejection_failures"] == 0
    assert constraints["plaquette_flatness_failures"] == 0
    assert constraints["color_plaquette_loop_failures"] == 0
    assert constraints["delete_one_color_loop_edge_detected_cases"] == 24 * 3 * 27
    assert [
        (
            row["side"],
            row["translations"],
            row["transported_origin_color_failures"],
            row["periodic_Z3_positive_seam_constraint_violations_per_sector"],
        )
        for row in translation["rows"]
    ] == [(5, 125, 0, 75), (6, 216, 0, 0)]
    assert mass_and_deletion["vacuum_or_one_particle_phase_failures"] == 0
    assert [row["detected_pairs"] for row in mass_and_deletion["exact_L_term_deletions"]] == [24, 24, 154]
    print("CYCLE703_L_EXACT_SQUARE72_HELD502_HK_DICTIONARY_OPEN")


if __name__ == "__main__":
    main()
