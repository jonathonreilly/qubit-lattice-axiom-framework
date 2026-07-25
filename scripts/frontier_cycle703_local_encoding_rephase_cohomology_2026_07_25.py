#!/usr/bin/env python3
"""Cycle 703: local encoding-rephase coboundary test.

Seek a diagonal occupation rephase f such that the fixed-register residual
quadratic word r is the stream coboundary delta_S f = f + f composed with S.
The tested local bases are geometric onsite/edge/face/cube neighborhoods in a
transported coframe.  An unrestricted per-patch quadratic calculation then
separates local-basis failure from a stronger same-register orbit obstruction.
"""

from __future__ import annotations

from itertools import combinations, permutations, product
import json

import frontier_cycle703_coframe_corner_loop_dictionary_2026_07_25 as cycle703


baseline = cycle703.baseline
route_c = cycle703.route_c
Coord = cycle703.Coord
Frame = cycle703.Frame
Site = cycle703.Site

ORIGIN: Coord = (0, 0, 0)


def stream_permutation(row: dict[str, object]) -> tuple[int, ...]:
    cells = row["cells"]
    specs = row["specs"]
    owners = row["owners"]
    order = row["owner_order"]
    if not all(isinstance(value, tuple) for value in (cells, specs, owners, order)):
        raise TypeError("malformed owner row")
    source_at_current = list(range(6 * len(cells)))
    for owner in order:
        for spec, edge_owner in zip(specs, owners):
            if edge_owner != owner:
                continue
            left, right = spec[:2]
            source_at_current[left], source_at_current[right] = (
                source_at_current[right],
                source_at_current[left],
            )
    current_of_source = [0] * len(source_at_current)
    for current, source in enumerate(source_at_current):
        current_of_source[source] = current
    return tuple(current_of_source)


def pair_orbit_certificate(
    name: str, row: dict[str, object]
) -> dict[str, object]:
    permutation = stream_permutation(row)
    residual = row["residual"]
    if not isinstance(residual, set):
        raise TypeError("malformed residual")
    mode_count = len(permutation)
    involution_failures = sum(
        permutation[permutation[index]] != index for index in range(mode_count)
    )
    visited = set()
    fixed_orbits = two_orbits = odd_orbits = 0
    representative_rows = []
    for pair in combinations(range(mode_count), 2):
        if pair in visited:
            continue
        image = tuple(sorted((permutation[pair[0]], permutation[pair[1]])))
        if image == pair:
            visited.add(pair)
            fixed_orbits += 1
            if pair in residual:
                odd_orbits += 1
                if len(representative_rows) < 8:
                    representative_rows.append((pair, image, 1, 1))
            continue
        visited.update((pair, image))
        two_orbits += 1
        first = int(pair in residual)
        second = int(image in residual)
        if first ^ second:
            odd_orbits += 1
            if len(representative_rows) < 8:
                representative_rows.append((pair, image, first, second))
    pair_dimension = mode_count * (mode_count - 1) // 2
    return {
        "fixture": name,
        "cells": len(row["cells"]),
        "modes": mode_count,
        "residual_pairs": len(residual),
        "stream_involution_failures": involution_failures,
        "quadratic_pair_dimension": pair_dimension,
        "fixed_pair_orbits": fixed_orbits,
        "two_pair_orbits": two_orbits,
        "delta_S_unrestricted_quadratic_rank": two_orbits,
        "delta_S_augmented_rank": two_orbits + int(odd_orbits > 0),
        "odd_residual_pair_orbits": odd_orbits,
        "minimum_pair_mismatch_in_unrestricted_quadratic_image": odd_orbits,
        "two_particle_configuration_symmetry_failures": 2 * odd_orbits,
        "representative_odd_orbits": tuple(representative_rows),
        "exact_same_register_diagonal_rephase_exists": odd_orbits == 0,
    }


def independent_cycle330_adjacent_witness() -> dict[str, object]:
    """Rebuild one odd orbit from direction/seam grammar, not owner_residual."""

    centers = ((0, 0, 0), (1, 0, 0))
    cells_set = set(centers)
    edges = []
    owners = []
    seen = set()
    for owner, center in enumerate(centers):
        for direction in route_c.DIRECTIONS:
            arm = baseline.add(center, direction)
            cells_set.add(arm)
            edge = tuple(sorted((center, arm)))
            if edge in seen:
                continue
            seen.add(edge)
            edges.append((center, arm))
            owners.append(owner)
    cells = tuple(sorted(cells_set))

    def specs_for(
        local_cells: tuple[Coord, ...], local_edges: tuple[tuple[Coord, Coord], ...]
    ) -> tuple[tuple[int, int, tuple[int, ...]], ...]:
        specs = []
        for left_cell, right_cell in local_edges:
            direction = baseline.sub(right_cell, left_cell)
            left_index = local_cells.index(left_cell)
            right_index = local_cells.index(right_cell)
            left_mode = route_c.DIRECTION_INDEX[direction]
            right_mode = route_c.DIRECTION_INDEX[
                tuple(-value for value in direction)
            ]
            specs.append(
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
        return tuple(specs)

    global_specs = specs_for(cells, tuple(edges))
    global_target = baseline.adjacent.transition_pair_set(
        6 * len(cells), global_specs
    )[2]
    source_at_current = list(range(6 * len(cells)))
    local_word = set()
    for owner in range(len(centers)):
        owned_edges = tuple(
            edge for edge, edge_owner in zip(edges, owners) if edge_owner == owner
        )
        local_cells = tuple(sorted({cell for edge in owned_edges for cell in edge}))
        local_specs = specs_for(local_cells, owned_edges)
        local_target = baseline.adjacent.transition_pair_set(
            6 * len(local_cells), local_specs
        )[2]
        local_to_global = tuple(
            6 * cells.index(cell) + mode
            for cell in local_cells
            for mode in range(6)
        )
        for first, second in local_target:
            pair = tuple(
                sorted(
                    (
                        source_at_current[local_to_global[first]],
                        source_at_current[local_to_global[second]],
                    )
                )
            )
            if pair in local_word:
                local_word.remove(pair)
            else:
                local_word.add(pair)
        for spec, edge_owner in zip(global_specs, owners):
            if edge_owner != owner:
                continue
            left, right = spec[:2]
            source_at_current[left], source_at_current[right] = (
                source_at_current[right],
                source_at_current[left],
            )
    residual = local_word ^ global_target
    current_of_source = [0] * len(source_at_current)
    for current, source in enumerate(source_at_current):
        current_of_source[source] = current

    first_pair = (18, 38)
    image_pair = tuple(
        sorted(
            (
                current_of_source[first_pair[0]],
                current_of_source[first_pair[1]],
            )
        )
    )

    def site_label(index: int) -> dict[str, object]:
        return {
            "address": index,
            "cell": cells[index // 6],
            "mode": index % 6,
            "cycle330_direction": route_c.DIRECTIONS[index % 6],
        }

    return {
        "cycle330_module": route_c.c330.__name__,
        "cycle330_direction_modes": route_c.DIRECTIONS,
        "cycle330_pair_labels": len(route_c.c330.PAIR_LABELS),
        "reconstruction_used_owner_residual_helper": False,
        "reconstructed_cells": len(cells),
        "reconstructed_edges": len(edges),
        "reconstructed_residual_pairs": len(residual),
        "pair": tuple(site_label(index) for index in first_pair),
        "stream_image_pair": tuple(site_label(index) for index in image_pair),
        "residual_bits_pair_and_image": (
            int(first_pair in residual),
            int(image_pair in residual),
        ),
        "stream_returns_pair_after_two_steps": tuple(
            sorted(
                (
                    current_of_source[image_pair[0]],
                    current_of_source[image_pair[1]],
                )
            )
        )
        == first_pair,
        "delta_f_necessary_equality_violated": (
            int(first_pair in residual) != int(image_pair in residual)
        ),
    }


def canonical_feature_key(
    displacement: Coord, first_mode: int, second_mode: int
) -> tuple[Coord, int, int]:
    forward = (displacement, first_mode, second_mode)
    reverse = (
        tuple(-value for value in displacement),
        second_mode,
        first_mode,
    )
    return min(forward, reverse)


def allowed_displacement(displacement: Coord, basis: str) -> bool:
    taxi = sum(abs(value) for value in displacement)
    maximum = max(abs(value) for value in displacement)
    if basis == "onsite-edge":
        return taxi <= 1
    if basis == "onsite-edge-face":
        return maximum <= 1 and taxi <= 2
    if basis == "onsite-edge-two-step":
        return taxi <= 2
    if basis == "elementary-cube":
        return maximum <= 1
    raise ValueError(basis)


def feature_keys(basis: str) -> tuple[tuple[Coord, int, int], ...]:
    keys = set()
    for displacement in product(range(-2, 3), repeat=3):
        if not allowed_displacement(displacement, basis):
            continue
        for first_mode in range(6):
            for second_mode in range(6):
                if displacement == ORIGIN and first_mode == second_mode:
                    continue
                keys.add(
                    canonical_feature_key(
                        displacement, first_mode, second_mode
                    )
                )
    return tuple(sorted(keys))


def row_feature_key(
    row: dict[str, object], first: int, second: int
) -> tuple[Coord, int, int]:
    cells = row["cells"]
    if not isinstance(cells, tuple):
        raise TypeError("malformed cells")
    first_cell = cells[first // 6]
    second_cell = cells[second // 6]
    displacement = baseline.sub(second_cell, first_cell)
    return canonical_feature_key(displacement, first % 6, second % 6)


def gf2_vector_rank(rows: list[int]) -> int:
    basis: dict[int, int] = {}
    for source in rows:
        row = source
        while row:
            pivot = row.bit_length() - 1
            if pivot in basis:
                row ^= basis[pivot]
            else:
                basis[pivot] = row
                break
    return len(basis)


def local_basis_system(
    basis_name: str, training_rows: tuple[dict[str, object], ...]
) -> dict[str, object]:
    keys = feature_keys(basis_name)
    key_index = {key: index for index, key in enumerate(keys)}
    width = len(keys)
    coefficient_rows = []
    augmented_rows = []
    nonzero_rhs = 0
    for row in training_rows:
        permutation = stream_permutation(row)
        residual = row["residual"]
        if not isinstance(residual, set):
            raise TypeError("malformed residual")
        for first, second in combinations(range(len(permutation)), 2):
            coefficient = 0
            input_key = row_feature_key(row, first, second)
            output_key = row_feature_key(
                row, permutation[first], permutation[second]
            )
            if input_key in key_index:
                coefficient ^= 1 << key_index[input_key]
            if output_key in key_index:
                coefficient ^= 1 << key_index[output_key]
            rhs = int((first, second) in residual)
            nonzero_rhs += rhs
            coefficient_rows.append(coefficient)
            augmented_rows.append(coefficient | (rhs << width))
    coefficient_rank = gf2_vector_rank(coefficient_rows)
    augmented_rank = gf2_vector_rank(augmented_rows)
    return {
        "basis": basis_name,
        "geometric_coefficients": width,
        "training_pair_equations": len(coefficient_rows),
        "training_nonzero_rhs": nonzero_rhs,
        "coefficient_GF2_rank": coefficient_rank,
        "augmented_GF2_rank": augmented_rank,
        "consistent": coefficient_rank == augmented_rank,
        "solution_frozen_for_held_test": False,
        "maximum_cell_taxi_support": max(
            sum(abs(value) for value in key[0]) for key in keys
        ),
        "target_independent_basis": True,
        "target_used_only_as_equation_rhs": True,
    }


def transform_site(frame: Frame, site: Site) -> Site:
    mode_direction = route_c.DIRECTIONS[site[1]]
    transformed_direction = route_c.matvec(frame, mode_direction)
    return (
        route_c.matvec(frame, site[0]),
        route_c.DIRECTION_INDEX[transformed_direction],
    )


def coframe_feature_key(
    first: Site, second: Site, coframe: Frame
) -> tuple[Coord, int, int]:
    inverse = cycle703.transpose(coframe)
    displacement = route_c.matvec(
        inverse, baseline.sub(second[0], first[0])
    )
    first_local_direction = route_c.matvec(
        inverse, route_c.DIRECTIONS[first[1]]
    )
    second_local_direction = route_c.matvec(
        inverse, route_c.DIRECTIONS[second[1]]
    )
    return canonical_feature_key(
        displacement,
        route_c.DIRECTION_INDEX[first_local_direction],
        route_c.DIRECTION_INDEX[second_local_direction],
    )


def basis_covariance_certificate() -> dict[str, object]:
    keys = feature_keys("elementary-cube")
    frame_failures = composition_failures = 0
    for displacement, first_mode, second_mode in keys:
        base_first: Site = (ORIGIN, first_mode)
        base_second: Site = (displacement, second_mode)
        base_key = coframe_feature_key(
            base_first, base_second, cycle703.IDENTITY
        )
        for frame in cycle703.FRAMES:
            transformed_first = transform_site(frame, base_first)
            transformed_second = transform_site(frame, base_second)
            frame_failures += coframe_feature_key(
                transformed_first, transformed_second, frame
            ) != base_key
        for left in cycle703.FRAMES:
            for right in cycle703.FRAMES:
                staged_first = transform_site(
                    left, transform_site(right, base_first)
                )
                staged_second = transform_site(
                    left, transform_site(right, base_second)
                )
                product_frame = route_c.matmul(left, right)
                direct_first = transform_site(product_frame, base_first)
                direct_second = transform_site(product_frame, base_second)
                composition_failures += (
                    staged_first != direct_first
                    or staged_second != direct_second
                    or coframe_feature_key(
                        staged_first, staged_second, product_frame
                    )
                    != base_key
                )
    return {
        "largest_basis_keys": len(keys),
        "proper_cubic_frames": len(cycle703.FRAMES),
        "ordered_frame_products": len(cycle703.FRAMES) ** 2,
        "coframe_key_frame_cases": len(keys) * len(cycle703.FRAMES),
        "coframe_key_frame_failures": frame_failures,
        "coframe_key_composition_cases": len(keys) * len(cycle703.FRAMES) ** 2,
        "coframe_key_composition_failures": composition_failures,
    }


def routing_certificate() -> dict[str, object]:
    displacements = tuple(
        sorted(
            {
                key[0]
                for key in feature_keys("elementary-cube")
                if key[0] != ORIGIN
            }
        )
    )
    return_failures = adjacency_failures = 0
    rows = []
    for displacement in displacements:
        steps = []
        for axis in range(3):
            sign = 1 if displacement[axis] > 0 else -1
            for _ in range(abs(displacement[axis])):
                step = [0, 0, 0]
                step[axis] = sign
                steps.append(tuple(step))
        labels = list(range(len(steps) + 1))
        for index in range(max(0, len(steps) - 1)):
            labels[index], labels[index + 1] = labels[index + 1], labels[index]
        adjacency_failures += labels[-2:] != [0, len(steps)]
        for index in reversed(range(max(0, len(steps) - 1))):
            labels[index], labels[index + 1] = labels[index + 1], labels[index]
        return_failures += labels != list(range(len(steps) + 1))
        rows.append(
            {
                "displacement": displacement,
                "taxi_length": len(steps),
                "routing_SWAPS_out_and_back": 2 * max(0, len(steps) - 1),
            }
        )
    return {
        "non_onsite_displacement_programs": len(displacements),
        "maximum_taxi_length": max(row["taxi_length"] for row in rows),
        "maximum_SWAPS_out_and_back": max(
            row["routing_SWAPS_out_and_back"] for row in rows
        ),
        "pre_CZ_adjacency_failures": adjacency_failures,
        "returned_routing_failures": return_failures,
        "onsite_realization": "bounded intra-cell CZ",
        "offsite_realization": (
            "coframe-axis SWAP path to adjacency, CZ, reverse SWAP path"
        ),
        "scope": (
            "realization of every candidate basis monomial; no consistent "
            "coefficient vector exists for the training residual"
        ),
    }


def main() -> None:
    pair_centers = ((0, 0, 0), (1, 0, 0))
    l_centers = ((0, 0, 0), (1, 0, 0), (0, 1, 0))
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
    fixtures = (
        ("adjacent-centers", pair_centers),
        ("three-center-L", l_centers),
        ("two-by-two-centers", square_centers),
        ("three-by-three-centers", held_centers),
        ("two-by-two-by-two-cube", cube_centers),
    )
    rows = tuple(
        (name, baseline.owner_residual(centers)) for name, centers in fixtures
    )
    orbit_rows = tuple(pair_orbit_certificate(name, row) for name, row in rows)
    training = tuple(row for _, row in rows[:3])
    local_systems = tuple(
        local_basis_system(name, training)
        for name in (
            "onsite-edge",
            "onsite-edge-face",
            "onsite-edge-two-step",
            "elementary-cube",
        )
    )

    l_order_rows = tuple(
        pair_orbit_certificate(
            f"L-order-{''.join(map(str, order))}",
            baseline.owner_residual(l_centers, order),
        )
        for order in permutations(range(3))
    )
    covariance = basis_covariance_certificate()
    routing = routing_certificate()
    independent_witness = independent_cycle330_adjacent_witness()
    certificate = {
        "cycle": 703,
        "authority": "none",
        "audit": "unset",
        "status": "same-register-diagonal-rephase-orbit-obstructed",
        "equation": "r(n) = f(n) xor f(S n)",
        "target_independent_local_basis_systems": local_systems,
        "unrestricted_quadratic_pair_orbits": orbit_rows,
        "all_six_L_owner_orders": tuple(
            {
                "fixture": row["fixture"],
                "residual_pairs": row["residual_pairs"],
                "odd_residual_pair_orbits": row[
                    "odd_residual_pair_orbits"
                ],
                "exact_same_register_diagonal_rephase_exists": row[
                    "exact_same_register_diagonal_rephase_exists"
                ],
            }
            for row in l_order_rows
        ),
        "general_diagonal_involution_test": {
            "identity": (
                "for S^2=I, delta_S f(Sn)=f(Sn) xor f(S^2n)="
                "f(Sn) xor f(n)=delta_S f(n)"
            ),
            "tested_sector": "vacuum plus one- and two-particle configurations",
            "training_two_particle_symmetry_failures": tuple(
                row["two_particle_configuration_symmetry_failures"]
                for row in orbit_rows[:3]
            ),
            "held_two_particle_symmetry_failures": tuple(
                row["two_particle_configuration_symmetry_failures"]
                for row in orbit_rows[3:]
            ),
            "conclusion_scope": (
                "no diagonal f on the same occupation register, even nonlocal "
                "or nonquadratic, can match the listed residual on every n<=2 "
                "configuration"
            ),
        },
        "independent_cycle330_orbit_witness": independent_witness,
        "basis_covariance": covariance,
        "bounded_CZ_and_returned_routing": routing,
        "mass_and_domain": {
            "residual_zero_on_vacuum_and_one_particle": True,
            "one_particle_mass_fixture_preserved_by_the_question": True,
            "physical_common_E_constructed": False,
            "physical_code_space_leakage_norm": "not defined",
        },
        "supplied": (
            "the fixed-register owner residuals used as equation right-hand sides",
            "the coarse stream permutation S from the declared seam swaps",
            "a homogeneous local coframe and direction-mode labels",
            "the geometric neighborhood class for f",
        ),
        "not_claimed": (
            "failure of an auxiliary-state, time-dependent, or non-diagonal rephase",
            "failure of the local gauge compiler route",
            "minimum physical substrate content",
            "a route-independent obstruction or axiom pressure",
        ),
    }
    print("CYCLE703_LOCAL_ENCODING_REPHASE_COHOMOLOGY")
    print(json.dumps(certificate, sort_keys=True, default=str))

    assert [
        (
            row["modes"],
            row["residual_pairs"],
            row["fixed_pair_orbits"],
            row["two_pair_orbits"],
            row["odd_residual_pair_orbits"],
        )
        for row in orbit_rows
    ] == [
        (72, 24, 1236, 660, 4),
        (96, 178, 2032, 1264, 22),
        (120, 250, 3180, 1980, 34),
        (234, 942, 11217, 8022, 100),
        (192, 1136, 7176, 5580, 156),
    ]
    assert all(row["stream_involution_failures"] == 0 for row in orbit_rows)
    assert all(
        not row["exact_same_register_diagonal_rephase_exists"]
        for row in orbit_rows
    )
    assert [
        (
            row["geometric_coefficients"],
            row["coefficient_GF2_rank"],
            row["augmented_GF2_rank"],
        )
        for row in local_systems
    ] == [(123, 120, 121), (339, 318, 319), (447, 397, 398), (483, 432, 433)]
    assert all(not row["consistent"] for row in local_systems)
    assert all(row["odd_residual_pair_orbits"] == 22 for row in l_order_rows)
    assert independent_witness["reconstructed_residual_pairs"] == 24
    assert independent_witness["residual_bits_pair_and_image"] == (1, 0)
    assert independent_witness["stream_returns_pair_after_two_steps"]
    assert independent_witness["delta_f_necessary_equality_violated"]
    assert covariance["coframe_key_frame_failures"] == 0
    assert covariance["coframe_key_composition_failures"] == 0
    assert routing["pre_CZ_adjacency_failures"] == 0
    assert routing["returned_routing_failures"] == 0
    print("CYCLE703_REPHASE_ODD_ORBITS_4_22_34_HELD_100_156")


if __name__ == "__main__":
    main()
