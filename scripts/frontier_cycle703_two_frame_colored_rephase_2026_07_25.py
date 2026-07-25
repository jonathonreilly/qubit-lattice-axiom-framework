#!/usr/bin/env python3
"""Cycle 703: bounded two-frame colored rephase and held prediction audit.

Replace the obstructed same-register equation by

    r(n) = f_in(n) xor f_out(S n).

Both phases use the same target-independent colored geometric basis but have
independent coefficients.  Training uses adjacent/L/2x2; the canonical
free-zero solution is frozen on 3x3 and a 2x2x2 cube.  Row-space membership
also determines which held bits are forced by every training solution.
"""

from __future__ import annotations

from itertools import combinations, product
import hashlib
import json

import frontier_cycle703_local_encoding_rephase_cohomology_2026_07_25 as rephase


baseline = rephase.baseline
cycle703 = rephase.cycle703
route_c = rephase.route_c
Coord = rephase.Coord
Frame = rephase.Frame
Site = rephase.Site

ORIGIN: Coord = (0, 0, 0)


def advance_color(
    color: tuple[int, int, int], displacement: Coord
) -> tuple[int, int, int]:
    delta = (displacement[1], displacement[0], displacement[2])
    return tuple((color[index] + delta[index]) % 3 for index in range(3))  # type: ignore[return-value]


def canonical_colored_key(
    color: tuple[int, int, int],
    displacement: Coord,
    first_mode: int,
    second_mode: int,
) -> tuple[tuple[int, int, int], Coord, int, int]:
    forward = (color, displacement, first_mode, second_mode)
    reverse = (
        advance_color(color, displacement),
        tuple(-value for value in displacement),
        second_mode,
        first_mode,
    )
    return min(forward, reverse)


def universal_colored_keys(
    basis_name: str,
) -> tuple[tuple[tuple[int, int, int], Coord, int, int], ...]:
    keys = set()
    for color in product(range(3), repeat=3):
        for displacement in product(range(-2, 3), repeat=3):
            if not rephase.allowed_displacement(displacement, basis_name):
                continue
            for first_mode in range(6):
                for second_mode in range(6):
                    if displacement == ORIGIN and first_mode == second_mode:
                        continue
                    keys.add(
                        canonical_colored_key(
                            color, displacement, first_mode, second_mode
                        )
                    )
    return tuple(sorted(keys))


def row_colored_key(
    row: dict[str, object], first: int, second: int
) -> tuple[tuple[int, int, int], Coord, int, int]:
    cells = row["cells"]
    if not isinstance(cells, tuple):
        raise TypeError("malformed cells")
    first_cell = cells[first // 6]
    second_cell = cells[second // 6]
    color = (first_cell[1] % 3, first_cell[0] % 3, first_cell[2] % 3)
    return canonical_colored_key(
        color,
        baseline.sub(second_cell, first_cell),
        first % 6,
        second % 6,
    )


def equation_vector(
    row: dict[str, object],
    first: int,
    second: int,
    permutation: tuple[int, ...],
    key_index: dict[tuple[tuple[int, int, int], Coord, int, int], int],
    width: int,
) -> int:
    result = 0
    input_key = row_colored_key(row, first, second)
    output_key = row_colored_key(
        row, permutation[first], permutation[second]
    )
    if input_key in key_index:
        result ^= 1 << key_index[input_key]
    if output_key in key_index:
        result ^= 1 << (width + key_index[output_key])
    return result


def equations(
    row: dict[str, object],
    key_index: dict[tuple[tuple[int, int, int], Coord, int, int], int],
    width: int,
) -> list[tuple[int, int]]:
    permutation = rephase.stream_permutation(row)
    residual = row["residual"]
    if not isinstance(residual, set):
        raise TypeError("malformed residual")
    return [
        (
            equation_vector(
                row, first, second, permutation, key_index, width
            ),
            int((first, second) in residual),
        )
        for first, second in combinations(range(len(permutation)), 2)
    ]


def elimination(
    rows: list[tuple[int, int]], variable_count: int
) -> tuple[dict[int, tuple[int, int]], int, int]:
    coefficient_basis: dict[int, int] = {}
    augmented_basis: dict[int, int] = {}
    solution_basis: dict[int, tuple[int, int]] = {}
    for coefficient, rhs in rows:
        reduced = coefficient
        reduced_rhs = rhs
        while reduced:
            pivot = reduced.bit_length() - 1
            if pivot in solution_basis:
                basis_row, basis_rhs = solution_basis[pivot]
                reduced ^= basis_row
                reduced_rhs ^= basis_rhs
            else:
                solution_basis[pivot] = (reduced, reduced_rhs)
                break

        coefficient_row = coefficient
        while coefficient_row:
            pivot = coefficient_row.bit_length() - 1
            if pivot in coefficient_basis:
                coefficient_row ^= coefficient_basis[pivot]
            else:
                coefficient_basis[pivot] = coefficient_row
                break

        augmented_row = coefficient | (rhs << variable_count)
        while augmented_row:
            pivot = augmented_row.bit_length() - 1
            if pivot in augmented_basis:
                augmented_row ^= augmented_basis[pivot]
            else:
                augmented_basis[pivot] = augmented_row
                break
    return solution_basis, len(coefficient_basis), len(augmented_basis)


def canonical_free_zero_solution(
    basis: dict[int, tuple[int, int]]
) -> int:
    solution = 0
    for pivot in sorted(basis):
        row, rhs = basis[pivot]
        lower = row ^ (1 << pivot)
        value = rhs ^ ((lower & solution).bit_count() & 1)
        if value:
            solution |= 1 << pivot
    return solution


def basis_training_rows(
    basis_name: str,
    training: tuple[dict[str, object], ...],
) -> dict[str, object]:
    keys = universal_colored_keys(basis_name)
    key_index = {key: index for index, key in enumerate(keys)}
    rows = sum((equations(row, key_index, len(keys)) for row in training), [])
    _, coefficient_rank, augmented_rank = elimination(rows, 2 * len(keys))
    return {
        "basis": basis_name,
        "colored_geometric_keys_per_frame_phase": len(keys),
        "two_frame_coefficients": 2 * len(keys),
        "training_equations": len(rows),
        "coefficient_GF2_rank": coefficient_rank,
        "augmented_GF2_rank": augmented_rank,
        "consistent": coefficient_rank == augmented_rank,
        "target_independent_basis": True,
    }


def predict_fixture(
    name: str,
    row: dict[str, object],
    key_index: dict[tuple[tuple[int, int, int], Coord, int, int], int],
    width: int,
    solution: int,
    training_basis: dict[int, tuple[int, int]],
) -> dict[str, object]:
    permutation = rephase.stream_permutation(row)
    residual = row["residual"]
    if not isinstance(residual, set):
        raise TypeError("malformed residual")
    predicted = set()
    determined = underdetermined = determined_target_conflicts = 0
    for first, second in combinations(range(len(permutation)), 2):
        coefficient = equation_vector(
            row, first, second, permutation, key_index, width
        )
        if (coefficient & solution).bit_count() & 1:
            predicted.add((first, second))

        reduced = coefficient
        required = int((first, second) in residual)
        while reduced:
            pivot = reduced.bit_length() - 1
            if pivot not in training_basis:
                break
            basis_row, basis_rhs = training_basis[pivot]
            reduced ^= basis_row
            required ^= basis_rhs
        if reduced:
            underdetermined += 1
        else:
            determined += 1
            determined_target_conflicts += required
    mismatch = predicted ^ residual
    return {
        "fixture": name,
        "target_pairs": len(residual),
        "canonical_predicted_pairs": len(predicted),
        "canonical_mismatch_pairs": len(mismatch),
        "canonical_mismatch_alternating_GF2_rank": baseline.pair_rank(
            mismatch, len(permutation)
        ),
        "held_equations_forced_by_training_row_space": determined,
        "held_equations_underdetermined_by_training": underdetermined,
        "forced_target_conflicts_for_every_training_solution": (
            determined_target_conflicts
        ),
    }


def combined_rank_row(
    name: str,
    rows: list[tuple[int, int]],
    variable_count: int,
) -> dict[str, object]:
    _, coefficient_rank, augmented_rank = elimination(rows, variable_count)
    return {
        "system": name,
        "equations": len(rows),
        "coefficient_GF2_rank": coefficient_rank,
        "augmented_GF2_rank": augmented_rank,
        "consistent": coefficient_rank == augmented_rank,
    }


def colored_coframe_key(
    first: Site, second: Site, coframe: Frame, origin: Coord
) -> tuple[tuple[int, int, int], Coord, int, int]:
    inverse = cycle703.transpose(coframe)
    first_local = route_c.matvec(inverse, baseline.sub(first[0], origin))
    displacement = route_c.matvec(
        inverse, baseline.sub(second[0], first[0])
    )
    first_direction = route_c.matvec(
        inverse, route_c.DIRECTIONS[first[1]]
    )
    second_direction = route_c.matvec(
        inverse, route_c.DIRECTIONS[second[1]]
    )
    color = (first_local[1] % 3, first_local[0] % 3, first_local[2] % 3)
    return canonical_colored_key(
        color,
        displacement,
        route_c.DIRECTION_INDEX[first_direction],
        route_c.DIRECTION_INDEX[second_direction],
    )


def active_covariance_certificate(
    keys: tuple[tuple[tuple[int, int, int], Coord, int, int], ...],
    solution: int,
) -> dict[str, object]:
    width = len(keys)
    active_indices = tuple(
        index for index in range(2 * width) if (solution >> index) & 1
    )
    active_keys = tuple(sorted({keys[index % width] for index in active_indices}))
    frame_failures = composition_failures = translation_failures = 0
    for color, displacement, first_mode, second_mode in active_keys:
        first_cell = (color[1], color[0], color[2])
        base_first: Site = (first_cell, first_mode)
        base_second: Site = (
            baseline.add(first_cell, displacement), second_mode
        )
        base_key = colored_coframe_key(
            base_first, base_second, cycle703.IDENTITY, ORIGIN
        )
        for frame in cycle703.FRAMES:
            first = rephase.transform_site(frame, base_first)
            second = rephase.transform_site(frame, base_second)
            frame_failures += colored_coframe_key(
                first, second, frame, ORIGIN
            ) != base_key
        for left in cycle703.FRAMES:
            for right in cycle703.FRAMES:
                staged_first = rephase.transform_site(
                    left, rephase.transform_site(right, base_first)
                )
                staged_second = rephase.transform_site(
                    left, rephase.transform_site(right, base_second)
                )
                product_frame = route_c.matmul(left, right)
                composition_failures += colored_coframe_key(
                    staged_first, staged_second, product_frame, ORIGIN
                ) != base_key
        for side in (5, 6):
            for shift in product(range(side), repeat=3):
                shifted_first: Site = (
                    baseline.add(base_first[0], shift), base_first[1]
                )
                shifted_second: Site = (
                    baseline.add(base_second[0], shift), base_second[1]
                )
                translation_failures += colored_coframe_key(
                    shifted_first,
                    shifted_second,
                    cycle703.IDENTITY,
                    shift,
                ) != base_key
    return {
        "active_coefficient_indices": len(active_indices),
        "distinct_active_geometric_keys": len(active_keys),
        "proper_cubic_frames": len(cycle703.FRAMES),
        "ordered_frame_products": len(cycle703.FRAMES) ** 2,
        "active_key_frame_cases": len(active_keys) * len(cycle703.FRAMES),
        "active_key_frame_failures": frame_failures,
        "active_key_composition_cases": len(active_keys)
        * len(cycle703.FRAMES) ** 2,
        "active_key_composition_failures": composition_failures,
        "active_key_L5_L6_translations": len(active_keys) * (5**3 + 6**3),
        "active_key_translation_failures": translation_failures,
        "periodic_color_scope": (
            "transported lifted origin only; inherited L5 Z3 seam failure remains"
        ),
    }


def deletion_certificate(
    training_rows: list[tuple[int, int]], solution: int
) -> dict[str, object]:
    active = tuple(index for index in range(solution.bit_length()) if (solution >> index) & 1)
    detected = []
    for index in active:
        detected.append(
            sum((coefficient >> index) & 1 for coefficient, _ in training_rows)
        )
    return {
        "active_coefficients_deleted_individually": len(active),
        "deletions_detected": sum(count > 0 for count in detected),
        "minimum_training_pair_failures_after_one_deletion": min(detected),
        "maximum_training_pair_failures_after_one_deletion": max(detected),
    }


def main() -> None:
    pair = baseline.owner_residual(((0, 0, 0), (1, 0, 0)))
    l_shape = baseline.owner_residual(
        ((0, 0, 0), (1, 0, 0), (0, 1, 0))
    )
    square = baseline.owner_residual(baseline.rectangle_centers(2, 2))
    held = baseline.owner_residual(baseline.rectangle_centers(3, 3))
    cube_centers = tuple(
        sorted(
            product(range(2), repeat=3),
            key=lambda center: cycle703.local_color(
                center, cycle703.IDENTITY, ORIGIN
            ),
        )
    )
    cube = baseline.owner_residual(cube_centers)
    training = (pair, l_shape, square)

    basis_rows = tuple(
        basis_training_rows(name, training)
        for name in (
            "onsite-edge",
            "onsite-edge-face",
            "onsite-edge-two-step",
            "elementary-cube",
        )
    )

    chosen_basis = "onsite-edge-two-step"
    keys = universal_colored_keys(chosen_basis)
    key_index = {key: index for index, key in enumerate(keys)}
    width = len(keys)
    training_rows = sum(
        (equations(row, key_index, width) for row in training), []
    )
    training_basis, training_rank, training_augmented_rank = elimination(
        training_rows, 2 * width
    )
    solution = canonical_free_zero_solution(training_basis)
    training_predictions = tuple(
        predict_fixture(
            name,
            row,
            key_index,
            width,
            solution,
            training_basis,
        )
        for name, row in (
            ("adjacent-centers", pair),
            ("three-center-L", l_shape),
            ("two-by-two-centers", square),
        )
    )
    held_predictions = tuple(
        predict_fixture(
            name,
            row,
            key_index,
            width,
            solution,
            training_basis,
        )
        for name, row in (
            ("three-by-three-centers", held),
            ("two-by-two-by-two-cube", cube),
        )
    )
    held_rows = equations(held, key_index, width)
    cube_rows = equations(cube, key_index, width)
    combined_rows = (
        combined_rank_row("training", training_rows, 2 * width),
        combined_rank_row(
            "training-plus-three-by-three",
            training_rows + held_rows,
            2 * width,
        ),
        combined_rank_row(
            "training-plus-cube", training_rows + cube_rows, 2 * width
        ),
        combined_rank_row(
            "training-plus-both-held",
            training_rows + held_rows + cube_rows,
            2 * width,
        ),
    )
    covariance = active_covariance_certificate(keys, solution)
    deletion = deletion_certificate(training_rows, solution)
    active_input = (solution & ((1 << width) - 1)).bit_count()
    active_output = (solution >> width).bit_count()
    active_digest = hashlib.sha256(
        repr(
            tuple(
                index
                for index in range(2 * width)
                if (solution >> index) & 1
            )
        ).encode()
    ).hexdigest()

    certificate = {
        "cycle": 703,
        "authority": "none",
        "audit": "unset",
        "status": "two-frame-colored-training-fit-held-prediction-falsified",
        "equation": "r(n) = f_in(n) xor f_out(S n)",
        "basis_tournament": basis_rows,
        "canonical_training_solution": {
            "basis": chosen_basis,
            "colored_keys_per_phase": width,
            "two_frame_coefficients": 2 * width,
            "training_equations": len(training_rows),
            "training_coefficient_rank": training_rank,
            "training_augmented_rank": training_augmented_rank,
            "free_coefficients": 2 * width - training_rank,
            "selection_rule": "lexicographic columns, highest-pivot elimination, all free coefficients zero",
            "active_f_in_coefficients": active_input,
            "active_f_out_coefficients": active_output,
            "active_index_sha256": active_digest,
            "training_predictions": training_predictions,
        },
        "held_no_refit": held_predictions,
        "held_compatibility_ranks": combined_rows,
        "active_basis_covariance_and_translation": covariance,
        "bounded_CZ_and_returned_routing": {
            **rephase.routing_certificate(),
            "chosen_basis_maximum_taxi_length": 2,
            "chosen_basis_maximum_SWAPS_out_and_back": 2,
            "scope": (
                "every chosen active two-step monomial is bounded and returned; "
                "the coefficient law fits training but fails held fixtures"
            ),
        },
        "deletion": deletion,
        "mass_and_domain": {
            "quadratic_phases_identity_on_vacuum_and_one_particle": True,
            "one_particle_mass_fixture_preserved": True,
            "occupation_scope": "vacuum plus one- and two-particle sign words",
            "physical_common_E_constructed": False,
            "physical_code_space_leakage_norm": "not defined",
            "autonomous_two_frame_clock_constructed": False,
        },
        "supplied": (
            "the bounded 27-color chart, coframe, and transported origin",
            "separate input/output phase slots",
            "the adjacent/L/square residuals used as training right-hand sides",
            "the lexicographic free-zero solution selector",
        ),
        "not_claimed": (
            "a target-independent derivation of the 280 active coefficients",
            "a held-predictive two-frame law",
            "an L5-periodic color schedule or autonomous clock",
            "a physical common-E intertwiner or leakage result",
            "a route-independent obstruction, minimum content, or axiom pressure",
        ),
    }
    print("CYCLE703_TWO_FRAME_COLORED_REPHASE")
    print(json.dumps(certificate, sort_keys=True, default=str))

    assert [
        (
            row["colored_geometric_keys_per_frame_phase"],
            row["coefficient_GF2_rank"],
            row["augmented_GF2_rank"],
        )
        for row in basis_rows
    ] == [
        (3321, 2069, 2070),
        (9153, 4135, 4136),
        (12069, 4701, 4701),
        (13041, 4935, 4936),
    ]
    assert all(row["canonical_mismatch_pairs"] == 0 for row in training_predictions)
    assert (active_input, active_output) == (110, 170)
    assert [
        (
            row["canonical_predicted_pairs"],
            row["canonical_mismatch_pairs"],
            row["canonical_mismatch_alternating_GF2_rank"],
            row["held_equations_forced_by_training_row_space"],
            row["held_equations_underdetermined_by_training"],
            row["forced_target_conflicts_for_every_training_solution"],
        )
        for row in held_predictions
    ] == [
        (288, 714, 42, 20020, 7241, 251),
        (250, 906, 54, 13041, 5295, 224),
    ]
    assert [
        (row["coefficient_GF2_rank"], row["augmented_GF2_rank"])
        for row in combined_rows
    ] == [(4701, 4701), (11188, 11189), (9210, 9211), (14442, 14443)]
    assert covariance["active_key_frame_failures"] == 0
    assert covariance["active_key_composition_failures"] == 0
    assert covariance["active_key_translation_failures"] == 0
    assert deletion["active_coefficients_deleted_individually"] == 280
    assert deletion["deletions_detected"] == 280
    print("CYCLE703_TWO_FRAME_TRAIN_EXACT_HELD_714_906_FORCED_CONFLICTS_251_224")


if __name__ == "__main__":
    main()
