"""Exact finite-region tensor extension for the Cl(3,0) exclusion runner.

The audit packet includes imported ``scripts/*.py`` helpers as complete source
artifacts.  Keeping this finite-lattice calculation separate leaves the
primary runner's load-bearing E2--E4 classification and faithfulness code
untruncated without dropping any of the original 62 computed checks.
"""

from __future__ import annotations

import itertools
from typing import Callable, Sequence

import sympy as sp
from sympy import I, Matrix, eye, simplify, symbols, zeros


def run_lattice_extension(
    *,
    check: Callable[[str, object, str], bool],
    section: Callable[[str], None],
    dimension: int,
    representation_images: Callable[[int, Sequence[Matrix]], list[Matrix]],
    pauli: Sequence[Matrix],
    matrix_equal: Callable[[Matrix, Matrix], bool],
    real_coordinates_of_matrix: Callable[[Matrix], Matrix],
    same_subspace: Callable[[Sequence[Matrix], Sequence[Matrix]], bool],
) -> tuple[bool, bool]:
    """Compute the scalar-character and two-site module certificates."""
    section("EL: finite-region lattice tensor extension")

    lattice_scalar_ok = True
    for n_sites in (2, 3):
        site_unknowns = [
            [symbols(f"z{site}_{index}") for index in range(1, 4)]
            for site in range(n_sites)
        ]
        joint_system = []
        for site_vars in site_unknowns:
            for i in range(3):
                for j in range(3):
                    lhs = (
                        site_vars[i] * site_vars[j]
                        + site_vars[j] * site_vars[i]
                    )
                    rhs = 2 if i == j else 0
                    joint_system.append(sp.expand(lhs - rhs))
        flat_unknowns = [value for site in site_unknowns for value in site]
        joint_solutions = sp.solve(joint_system, flat_unknowns, dict=True)
        lattice_scalar_ok = lattice_scalar_ok and joint_solutions == []
        check(
            f"EL.scalar N={n_sites}: joint scalar Clifford system is empty",
            joint_solutions == [],
            f"unknowns={3 * n_sites}, equations={len(joint_system)}, "
            f"solutions={len(joint_solutions)}",
        )
    el1_certificate = lattice_scalar_ok

    two_site_modules_ok = True
    site_irreps = {
        1: representation_images(1, pauli),
        -1: representation_images(-1, pauli),
    }
    generator_blade_indices = (1, 2, 4)
    shuffle = eye(4)[:, [0, 2, 1, 3]]
    central_character_pairs = set()
    total_square = 0
    for sign_a in (1, -1):
        for sign_b in (1, -1):
            images_a = site_irreps[sign_a]
            images_b = site_irreps[sign_b]
            site_a_generators = [
                sp.kronecker_product(images_a[index], eye(2))
                for index in generator_blade_indices
            ]
            site_b_generators = [
                sp.kronecker_product(eye(2), images_b[index])
                for index in generator_blade_indices
            ]
            joint_generators = site_a_generators + site_b_generators
            commutant_entries = [
                [symbols(f"c{sign_a}{sign_b}_{row}{col}") for col in range(4)]
                for row in range(4)
            ]
            commutant = Matrix(commutant_entries)
            equations = []
            for generator in joint_generators:
                equations.extend(sp.expand(commutant * generator - generator * commutant))
            unknowns = [entry for row in commutant_entries for entry in row]
            constraint, rhs = sp.linear_eq_to_matrix(equations, unknowns)
            nullspace = constraint.nullspace()
            identity_coordinates = Matrix(
                [
                    sp.Integer(1) if row == col else sp.Integer(0)
                    for row in range(4)
                    for col in range(4)
                ]
            )
            scalar_commutant = (
                rhs == zeros(rhs.rows, 1)
                and len(nullspace) == 1
                and same_subspace(nullspace, [identity_coordinates])
            )

            site_a_restriction_ok = all(
                matrix_equal(
                    shuffle.T * generator * shuffle,
                    sp.diag(images_a[index], images_a[index]),
                )
                for generator, index in zip(
                    site_a_generators, generator_blade_indices
                )
            )
            site_b_restriction_ok = all(
                matrix_equal(
                    generator,
                    sp.diag(images_b[index], images_b[index]),
                )
                for generator, index in zip(
                    site_b_generators, generator_blade_indices
                )
            )

            omega_a = sp.kronecker_product(images_a[7], eye(2))
            omega_b = sp.kronecker_product(eye(2), images_b[7])
            central_characters_ok = (
                matrix_equal(omega_a, sign_a * I * eye(4))
                and matrix_equal(omega_b, sign_b * I * eye(4))
            )
            if central_characters_ok:
                central_character_pairs.add((sign_a, sign_b))

            real_images = [
                sp.kronecker_product(
                    images_a[left_mask], images_b[right_mask]
                )
                for left_mask, right_mask in itertools.product(
                    range(dimension), repeat=2
                )
            ]
            real_map = Matrix.hstack(
                *[real_coordinates_of_matrix(image) for image in real_images]
            )
            real_rank = real_map.rank()
            real_kernel_dim = len(real_map.nullspace())
            real_restriction_nonfaithful = (
                real_rank == 32 and real_kernel_dim == 32
            )

            module_ok = (
                scalar_commutant
                and site_a_restriction_ok
                and site_b_restriction_ok
                and central_characters_ok
                and real_restriction_nonfaithful
            )
            two_site_modules_ok = two_site_modules_ok and module_ok
            total_square += 16
            signs = f"{'+' if sign_a == 1 else '-'},{'+' if sign_b == 1 else '-'}"
            check(
                f"EL.module ({signs}): irreducible module and real kernel",
                module_ok,
                f"commutant rank={constraint.rank()}, nullity={len(nullspace)}; "
                f"real rank={real_rank}, kernel dim={real_kernel_dim}",
            )

    expected_character_pairs = {(1, 1), (1, -1), (-1, 1), (-1, -1)}
    finite_n = symbols("finite_N", integer=True, positive=True)
    finite_region_dimension_identity = (
        simplify(
            (2**finite_n) * (2**finite_n) ** 2 - dimension**finite_n
        )
        == 0
    )
    finite_n_ge_two_offset = symbols(
        "finite_N_minus_one", integer=True, positive=True
    )
    finite_region_nonfaithfulness_ratio = (
        simplify(
            dimension ** (finite_n_ge_two_offset + 1)
            / (2 * (2 ** (finite_n_ge_two_offset + 1)) ** 2)
            - 2**finite_n_ge_two_offset
        )
        == 0
    )
    dimension_exhausts = (
        two_site_modules_ok
        and central_character_pairs == expected_character_pairs
        and total_square == dimension**2
        and finite_region_dimension_identity
        and finite_region_nonfaithfulness_ratio
    )
    check(
        "EL.exhaustion: four modules exhaust the 64-dimensional algebra",
        dimension_exhausts,
        f"central characters={sorted(central_character_pairs)}; "
        f"sum squared dimensions={total_square}",
    )
    el2_certificate = two_site_modules_ok and dimension_exhausts
    check(
        "EL.TOTAL finite-region certificates for both exclusions execute",
        el1_certificate and el2_certificate,
        "no finite-region scalar character; simple dimensions 2^N; "
        "N>=2 real restrictions are nonfaithful",
    )
    return el1_certificate, el2_certificate
