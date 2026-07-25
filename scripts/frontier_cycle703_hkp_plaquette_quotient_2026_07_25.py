#!/usr/bin/env python3
"""Cycle 703: freeze the target-derived H/K/P cell-complex dictionary.

H is the adjacent-center residual, K is the right-angle L associator, and P is
the remaining 2x2 square residual after H/K.  The runner applies one
coframe-transported P per elementary center plaquette without refit, then
tests 3x3, an out-of-plane corner, and a 2x2x2 cube.
"""

from __future__ import annotations

from itertools import combinations, product
import json

import frontier_cycle703_coframe_corner_loop_dictionary_2026_07_25 as cycle703


baseline = cycle703.baseline
route_c = cycle703.route_c
Coord = cycle703.Coord
Frame = cycle703.Frame
SitePair = cycle703.SitePair

ORIGIN: Coord = (0, 0, 0)
EX: Coord = (1, 0, 0)
EY: Coord = (0, 1, 0)
EZ: Coord = (0, 0, 1)
POSITIVE_LOCAL_AXES = (EX, EY, EZ)


def plaquette_terms(
    centers: tuple[Coord, ...],
    coframe: Frame,
    plaquette_word: set[SitePair],
) -> list[set[SitePair]]:
    selected = set(centers)
    terms = []
    for anchor in centers:
        for first, second in combinations(POSITIVE_LOCAL_AXES, 2):
            physical_first = route_c.matvec(coframe, first)
            physical_second = route_c.matvec(coframe, second)
            if not all(
                point in selected
                for point in (
                    baseline.add(anchor, physical_first),
                    baseline.add(anchor, physical_second),
                    baseline.add(
                        baseline.add(anchor, physical_first), physical_second
                    ),
                )
            ):
                continue
            frame = route_c.matmul(
                coframe, cycle703.columns_frame(first, second)
            )
            terms.append(
                cycle703.translate_site_word(
                    cycle703.transform_site_word(frame, plaquette_word), anchor
                )
            )
    return terms


def hkp_terms(
    centers: tuple[Coord, ...],
    coframe: Frame,
    origin: Coord,
    edge_word: set[SitePair],
    corner_word: set[SitePair],
    plaquette_word: set[SitePair],
) -> tuple[list[set[SitePair]], list[set[SitePair]], list[set[SitePair]]]:
    return (
        cycle703.adjacent_center_terms(
            centers, coframe, origin, edge_word
        ),
        cycle703.corner_incidence_terms(
            centers, coframe, origin, corner_word, True
        ),
        plaquette_terms(centers, coframe, plaquette_word),
    )


def channel_certificate(word: set[SitePair]) -> dict[str, object]:
    sites = tuple(sorted({site for pair in word for site in pair}))
    site_index = {site: index for index, site in enumerate(sites)}
    pairs = {
        tuple(sorted((site_index[first], site_index[second])))
        for first, second in word
    }
    channels = baseline.symplectic_channels(pairs, len(sites))
    reconstructed = set()
    for first, second in channels:
        reconstructed ^= baseline.pair_word_from_channel(first, second, len(sites))

    labels = ((),) + tuple((mode,) for mode in range(len(sites))) + tuple(
        combinations(range(len(sites)), 2)
    )
    phase_failures = return_failures = 0
    for first, second in channels:
        channel_pairs = baseline.pair_word_from_channel(
            first, second, len(sites)
        )
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
                observed = (
                    scratch * second_parity
                    + (scratch ^ first_parity) * second_parity
                    + overlap_parity
                ) & 1
                phase_failures += observed != expected
                returned = scratch ^ first_parity ^ first_parity
                return_failures += returned != scratch
    return {
        "support_sites": len(sites),
        "alternating_GF2_rank": cycle703.site_word_rank(word),
        "parity_product_channels": len(channels),
        "reconstruction_symmetric_difference": len(reconstructed ^ pairs),
        "n_le_2_dirty_loop_truth_cases": len(channels) * len(labels) * 2,
        "dirty_loop_phase_failures": phase_failures,
        "dirty_loop_return_failures": return_failures,
        "returned_dirty_loop_M2_reused_sequentially": 1,
    }


def renamed_plaquette_span(
    target: set[SitePair],
    edge_and_corner_terms: list[set[SitePair]],
    columns: list[set[SitePair]],
) -> dict[str, object]:
    source = cycle703.dictionary_span(target, edge_and_corner_terms, columns)
    return {
        "independent_plaquette_bits": source[
            "independent_corner_incidence_bits"
        ],
        "plaquette_dictionary_GF2_rank": source["dictionary_GF2_rank"],
        "augmented_GF2_rank": source["augmented_GF2_rank"],
        "target_in_plaquette_span": source["target_in_dictionary_span"],
        "closest_pair_mismatch_exhaustive": source[
            "closest_pair_mismatch_exhaustive"
        ],
        "binary_assignments_enumerated": source[
            "binary_assignments_enumerated"
        ],
        "exact_assignments": source["exact_assignments"],
    }


def fixture_row(
    name: str,
    centers: tuple[Coord, ...],
    edge_word: set[SitePair],
    corner_word: set[SitePair],
    plaquette_word: set[SitePair],
) -> tuple[dict[str, object], set[SitePair], tuple[list[set[SitePair]], ...]]:
    target = baseline.site_word(baseline.owner_residual(centers))
    term_groups = hkp_terms(
        centers,
        cycle703.IDENTITY,
        ORIGIN,
        edge_word,
        corner_word,
        plaquette_word,
    )
    candidate = cycle703.xor_words(sum((list(group) for group in term_groups), []))
    residual = target ^ candidate
    row = {
        "fixture": name,
        "centers": len(centers),
        "target_pairs": len(target),
        "H_terms": len(term_groups[0]),
        "K_terms": len(term_groups[1]),
        "P_terms": len(term_groups[2]),
        "candidate_pairs": len(candidate),
        "mismatch_pairs": len(residual),
        "mismatch_alternating_GF2_rank": cycle703.site_word_rank(residual),
        "mismatch_support_cell_diameter": cycle703.site_word_diameter(residual),
        "mismatch_distance_census": cycle703.distance_census(residual),
        "held_parameters_refit": 0,
        "P_span": renamed_plaquette_span(
            target, list(term_groups[0]) + list(term_groups[1]), list(term_groups[2])
        ) if term_groups[2] else None,
    }
    return row, target, term_groups


def covariance_certificate(
    fixtures: tuple[tuple[str, tuple[Coord, ...]], ...],
    edge_word: set[SitePair],
    corner_word: set[SitePair],
    plaquette_word: set[SitePair],
) -> dict[str, object]:
    composition_failures = frame_failures = candidate_failures = 0
    for left in cycle703.FRAMES:
        for right in cycle703.FRAMES:
            product_frame = route_c.matmul(left, right)
            composition_failures += cycle703.transform_site_word(
                left, cycle703.transform_site_word(right, plaquette_word)
            ) != cycle703.transform_site_word(product_frame, plaquette_word)
        for first, second in combinations(POSITIVE_LOCAL_AXES, 2):
            for physical_rotation in cycle703.FRAMES:
                base_frame = route_c.matmul(
                    left, cycle703.columns_frame(first, second)
                )
                transformed_frame = route_c.matmul(
                    route_c.matmul(physical_rotation, left),
                    cycle703.columns_frame(first, second),
                )
                frame_failures += transformed_frame != route_c.matmul(
                    physical_rotation, base_frame
                )

    for _, centers in fixtures:
        base_groups = hkp_terms(
            centers,
            cycle703.IDENTITY,
            ORIGIN,
            edge_word,
            corner_word,
            plaquette_word,
        )
        base_candidate = cycle703.xor_words(
            sum((list(group) for group in base_groups), [])
        )
        for frame in cycle703.FRAMES:
            transformed_centers = tuple(
                route_c.matvec(frame, center) for center in centers
            )
            rebuilt_groups = hkp_terms(
                transformed_centers,
                frame,
                ORIGIN,
                edge_word,
                corner_word,
                plaquette_word,
            )
            rebuilt = cycle703.xor_words(
                sum((list(group) for group in rebuilt_groups), [])
            )
            candidate_failures += rebuilt != cycle703.transform_site_word(
                frame, base_candidate
            )
    return {
        "proper_cubic_frames": len(cycle703.FRAMES),
        "ordered_frame_products": len(cycle703.FRAMES) ** 2,
        "P_word_composition_failures": composition_failures,
        "plaquette_frame_covariance_cases": len(cycle703.FRAMES) ** 2 * 3,
        "plaquette_frame_covariance_failures": frame_failures,
        "fixture_candidate_frame_cases": len(fixtures) * len(cycle703.FRAMES),
        "fixture_candidate_rebuild_failures": candidate_failures,
        "scope": "site-word geometry; no physical common-E matrices rebuilt",
    }


def out_of_plane_corner_certificate(
    l_centers: tuple[Coord, ...],
    l_target: set[SitePair],
    edge_word: set[SitePair],
    corner_word: set[SitePair],
    plaquette_word: set[SitePair],
) -> dict[str, object]:
    frame = cycle703.columns_frame(EX, EZ)
    centers = tuple(route_c.matvec(frame, center) for center in l_centers)
    groups = hkp_terms(
        centers, frame, ORIGIN, edge_word, corner_word, plaquette_word
    )
    candidate = cycle703.xor_words(sum((list(group) for group in groups), []))
    covariant_target = cycle703.transform_site_word(frame, l_target)
    recomputed_target = baseline.site_word(baseline.owner_residual(centers))
    covariant_residual = covariant_target ^ candidate
    exterior_residual = recomputed_target ^ candidate

    wrong_groups = hkp_terms(
        centers,
        cycle703.IDENTITY,
        ORIGIN,
        edge_word,
        corner_word,
        plaquette_word,
    )
    wrong_candidate = cycle703.xor_words(
        sum((list(group) for group in wrong_groups), [])
    )
    wrong_residual = recomputed_target ^ wrong_candidate
    return {
        "centers": centers,
        "P_terms": len(groups[2]),
        "transported_target_pairs": len(covariant_target),
        "transported_target_mismatch_pairs": len(covariant_residual),
        "transported_target_mismatch_rank": cycle703.site_word_rank(
            covariant_residual
        ),
        "recomputed_fixed_exterior_target_pairs": len(recomputed_target),
        "recomputed_target_mismatch_pairs": len(exterior_residual),
        "recomputed_target_mismatch_rank": cycle703.site_word_rank(
            exterior_residual
        ),
        "wrong_identity_coframe_recomputed_target_mismatch_pairs": len(
            wrong_residual
        ),
        "wrong_identity_coframe_recomputed_target_mismatch_rank": (
            cycle703.site_word_rank(wrong_residual)
        ),
        "interpretation": (
            "geometric H/K/P transport closes the transported target; the "
            "separately recomputed target retains the preferred exterior-order "
            "gauge, whose physical frame action is not compiled"
        ),
    }


def deletion_certificate(
    rows: dict[str, tuple[set[SitePair], tuple[list[set[SitePair]], ...]]]
) -> dict[str, object]:
    square_target, square_groups = rows["two-by-two-centers"]
    square_candidate = cycle703.xor_words(
        sum((list(group) for group in square_groups), [])
    )
    square_deleted = square_target ^ (
        square_candidate ^ square_groups[2][0]
    )

    held_rows = []
    for name in ("three-by-three-centers", "two-by-two-by-two-cube"):
        target, groups = rows[name]
        candidate = cycle703.xor_words(sum((list(group) for group in groups), []))
        held_rows.append(
            {
                "fixture": name,
                "single_P_deletion_rows": tuple(
                    {
                        "P_index": index,
                        "mismatch_pairs": len(target ^ (candidate ^ term)),
                        "mismatch_rank": cycle703.site_word_rank(
                            target ^ (candidate ^ term)
                        ),
                    }
                    for index, term in enumerate(groups[2])
                ),
            }
        )
    return {
        "square_delete_only_P_detected_pairs": len(square_deleted),
        "square_delete_only_P_detected_rank": cycle703.site_word_rank(
            square_deleted
        ),
        "held_single_P_deletions": tuple(held_rows),
    }


def main() -> None:
    l_centers = (ORIGIN, EX, EY)
    pair_centers = (ORIGIN, EX)
    square_centers = baseline.rectangle_centers(2, 2)
    held_centers = baseline.rectangle_centers(3, 3)
    cube_centers = tuple(
        sorted(
            product(range(2), repeat=3),
            key=lambda center: cycle703.local_color(
                center, cycle703.IDENTITY, ORIGIN
            ),
        )
    )

    edge_word = baseline.site_word(baseline.owner_residual(pair_centers))
    l_target = baseline.site_word(baseline.owner_residual(l_centers))
    y_edge_word = cycle703.transform_site_word(
        cycle703.EDGE_FRAME[EY], edge_word
    )
    corner_word = l_target ^ edge_word ^ y_edge_word

    square_target = baseline.site_word(baseline.owner_residual(square_centers))
    square_hk = cycle703.xor_words(
        cycle703.adjacent_center_terms(
            square_centers, cycle703.IDENTITY, ORIGIN, edge_word
        )
        + cycle703.corner_incidence_terms(
            square_centers,
            cycle703.IDENTITY,
            ORIGIN,
            corner_word,
            True,
        )
    )
    plaquette_word = square_target ^ square_hk

    fixtures = (
        ("adjacent-centers", pair_centers),
        ("three-center-L", l_centers),
        ("two-by-two-centers", square_centers),
        ("three-by-three-centers", held_centers),
        ("two-by-two-by-two-cube", cube_centers),
    )
    fixture_rows = []
    deletion_payload: dict[
        str, tuple[set[SitePair], tuple[list[set[SitePair]], ...]]
    ] = {}
    for name, centers in fixtures:
        row, target, groups = fixture_row(
            name, centers, edge_word, corner_word, plaquette_word
        )
        fixture_rows.append(row)
        deletion_payload[name] = (target, groups)

    covariance = covariance_certificate(
        (
            ("two-by-two-centers", square_centers),
            ("three-by-three-centers", held_centers),
            ("two-by-two-by-two-cube", cube_centers),
        ),
        edge_word,
        corner_word,
        plaquette_word,
    )
    out_of_plane = out_of_plane_corner_certificate(
        l_centers,
        l_target,
        edge_word,
        corner_word,
        plaquette_word,
    )
    deletion = deletion_certificate(deletion_payload)
    p_channels = channel_certificate(plaquette_word)

    certificate = {
        "cycle": 703,
        "authority": "none",
        "audit": "unset",
        "status": "H-K-P-training-square-closed-held-quotient-open",
        "P_extraction": {
            "definition": "2x2 target xor frozen H/K candidate",
            "pairs": len(plaquette_word),
            "alternating_GF2_rank": cycle703.site_word_rank(plaquette_word),
            "support_cell_diameter": cycle703.site_word_diameter(
                plaquette_word
            ),
            "distance_census": cycle703.distance_census(plaquette_word),
            "finite_target_extracted": True,
            "target_independent": False,
        },
        "P_loop_factorization": p_channels,
        "fixed_H_K_P_no_refit": tuple(fixture_rows),
        "out_of_plane_corner": out_of_plane,
        "proper_cubic_covariance": covariance,
        "deletion": deletion,
        "mass_and_domain": {
            "quadratic_correction_identity_on_vacuum_and_one_particle": True,
            "one_particle_mass_fixture_preserved": True,
            "occupation_scope": "vacuum plus one- and two-particle sign words",
            "physical_common_E_constructed": False,
            "physical_code_space_leakage_norm": "not defined",
        },
        "inherited_local_constraints": (
            "Cycle703 H/K exact diagonal coframe/chart/color projector truth tables",
            "the P executor reuses one returned dirty loop M2 sequentially",
        ),
        "supplied": (
            "the adjacent, L, and square finite exterior target oracles",
            "the H/K/P masks extracted from those targets",
            "the homogeneous coframe sector and bounded 27-color chart/origin",
            "the fixed color stages and local direction-mode labels",
        ),
        "not_claimed": (
            "a target-independent H/K/P recurrence",
            "proper-cubic covariance of the preferred exterior target gauge",
            "a physical common-E intertwiner, leakage bound, or autonomous clock",
            "a route-independent obstruction, minimum content, or axiom pressure",
        ),
    }
    print("CYCLE703_HKP_PLAQUETTE_QUOTIENT")
    print(json.dumps(certificate, sort_keys=True, default=str))

    assert len(plaquette_word) == 72
    assert cycle703.site_word_rank(plaquette_word) == 8
    assert cycle703.site_word_diameter(plaquette_word) == 3
    assert p_channels["parity_product_channels"] == 4
    assert p_channels["reconstruction_symmetric_difference"] == 0
    assert p_channels["dirty_loop_phase_failures"] == 0
    assert p_channels["dirty_loop_return_failures"] == 0
    assert [
        (
            row["target_pairs"],
            row["P_terms"],
            row["mismatch_pairs"],
            row["mismatch_alternating_GF2_rank"],
        )
        for row in fixture_rows
    ] == [
        (24, 0, 0, 0),
        (178, 0, 0, 0),
        (250, 1, 0, 0),
        (942, 4, 482, 24),
        (1136, 6, 680, 48),
    ]
    assert fixture_rows[3]["P_span"] == {
        "independent_plaquette_bits": 4,
        "plaquette_dictionary_GF2_rank": 4,
        "augmented_GF2_rank": 5,
        "target_in_plaquette_span": False,
        "closest_pair_mismatch_exhaustive": 364,
        "binary_assignments_enumerated": 16,
        "exact_assignments": 0,
    }
    assert fixture_rows[4]["P_span"] == {
        "independent_plaquette_bits": 6,
        "plaquette_dictionary_GF2_rank": 6,
        "augmented_GF2_rank": 7,
        "target_in_plaquette_span": False,
        "closest_pair_mismatch_exhaustive": 668,
        "binary_assignments_enumerated": 64,
        "exact_assignments": 0,
    }
    assert out_of_plane["transported_target_mismatch_pairs"] == 0
    assert out_of_plane["recomputed_target_mismatch_pairs"] == 150
    assert out_of_plane["recomputed_target_mismatch_rank"] == 14
    assert covariance["P_word_composition_failures"] == 0
    assert covariance["plaquette_frame_covariance_failures"] == 0
    assert covariance["fixture_candidate_rebuild_failures"] == 0
    assert deletion["square_delete_only_P_detected_pairs"] == 72
    assert deletion["square_delete_only_P_detected_rank"] == 8
    print("CYCLE703_HKP_CLOSES_SQUARE_HELD_3X3_482_CUBE_680")


if __name__ == "__main__":
    main()
