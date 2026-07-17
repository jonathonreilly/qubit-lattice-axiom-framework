#!/usr/bin/env python3
"""Independent exact check of the Cl(3) faithful direct-sum steelman.

This helper deliberately does not import the primary theorem runner.  It
reconstructs the two Pauli representations from exact SymPy matrices, checks
their separate and combined ranks, and exhibits a nontrivial commuting
projector for the faithful direct sum.
"""

from __future__ import annotations

import argparse
from collections.abc import Sequence

from sympy import I, Matrix, eye, zeros


BASIS_WORDS = ((), (0,), (1,), (2,), (0, 1), (0, 2), (1, 2), (0, 1, 2))


def product(word: tuple[int, ...], generators: Sequence[Matrix]) -> Matrix:
    result = eye(2)
    for index in word:
        result *= generators[index]
    return result


def coordinate_column(matrix: Matrix) -> Matrix:
    return Matrix([matrix[row, column] for row in range(2) for column in range(2)])


def representation_map(generators: Sequence[Matrix]) -> Matrix:
    return Matrix.hstack(
        *(coordinate_column(product(word, generators)) for word in BASIS_WORDS)
    )


def block_diagonal(left: Matrix, right: Matrix) -> Matrix:
    result = zeros(4)
    result[:2, :2] = left
    result[2:, 2:] = right
    return result


def check(condition: bool, label: str, failures: list[str]) -> None:
    status = "PASS" if condition else "FAIL"
    print(f"N7_INDEPENDENT_CHECK {label} status={status}")
    if not condition:
        failures.append(label)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--inject-failure",
        choices=("wrong-order", "false-reducibility"),
        help="apply one hostile evidence mutation",
    )
    args = parser.parse_args()

    sigma_1 = Matrix([[0, 1], [1, 0]])
    sigma_2 = Matrix([[0, -I], [I, 0]])
    sigma_3 = Matrix([[1, 0], [0, -1]])
    plus_generators = (sigma_1, sigma_2, sigma_3)
    minus_generators = (-sigma_1, -sigma_2, -sigma_3)
    if args.inject_failure == "wrong-order":
        # Oddly reorder the negative-sector generators.  This reverses its
        # central character and duplicates the positive simple-ideal action.
        minus_generators = (-sigma_1, -sigma_3, -sigma_2)

    plus_map = representation_map(plus_generators)
    minus_map = representation_map(minus_generators)
    combined_map = plus_map.col_join(minus_map)
    plus_volume = product((0, 1, 2), plus_generators)
    minus_volume = product((0, 1, 2), minus_generators)
    combined_generators = tuple(
        block_diagonal(plus_generators[index], minus_generators[index])
        for index in range(3)
    )

    sector_projector = block_diagonal(eye(2), zeros(2))
    if args.inject_failure == "false-reducibility":
        # This false witness still has rank two and is idempotent, but it is
        # not in the commutant and therefore cannot certify an invariant sum.
        sector_projector[0, 2] = 1

    failures: list[str] = []
    check(plus_map.rank() == 4, "rho_plus_complex_rank_4", failures)
    check(minus_map.rank() == 4, "rho_minus_complex_rank_4", failures)
    check(len(plus_map.nullspace()) == 4, "rho_plus_kernel_dim_complex_4", failures)
    check(len(minus_map.nullspace()) == 4, "rho_minus_kernel_dim_complex_4", failures)
    check(plus_volume == I * eye(2), "rho_plus_volume_character_plus_i", failures)
    check(minus_volume == -I * eye(2), "rho_minus_volume_character_minus_i", failures)
    check(combined_map.rank() == 8, "direct_sum_complex_rank_8_faithful", failures)
    check(sector_projector.rank() == 2, "proper_sector_projector_rank_2", failures)
    check(
        sector_projector * sector_projector == sector_projector,
        "proper_sector_projector_idempotent",
        failures,
    )
    check(
        all(
            sector_projector * generator == generator * sector_projector
            for generator in combined_generators
        ),
        "proper_sector_projector_commutes_with_action",
        failures,
    )

    if failures:
        print("N7_INDEPENDENT_RESULT status=FAIL failures=" + ",".join(failures))
        return 1

    print(
        "N7_STEELMAN_RESOLUTION "
        "wall=irreducible complexified A-module faithfulness boundary; "
        "steelman=rho_plus_direct_sum_rho_minus; "
        "individual_kernel_dim_complex=4; combined_complex_rank=8; "
        "faithful=true; reducible=true; invariant_summand_dims_complex=2,2; "
        "conclusion=faithfulness_does_not_recover_irreducibility"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
