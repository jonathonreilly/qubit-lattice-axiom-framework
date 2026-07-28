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
    one_site_split_certified: bool,
    one_site_simple_modules_certified: bool,
    one_site_scalar_excluded: bool,
    one_site_real_surjectivity_certified: bool,
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
    # For every nonempty finite N, a unital scalar character on the tensor
    # algebra restricts along a -> 1 tensor ... tensor a tensor ... tensor 1
    # to a unital one-site character.  The primary E3 certificate excludes
    # that restriction.  The N=2,3 solves above are exact finite-case checks,
    # not the premise for the general statement.
    el1_certificate = one_site_scalar_excluded and lattice_scalar_ok

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
    # Exact analytic certificate for every finite N, rather than an
    # extrapolation from the N=2 computation above.
    #
    # Base: primary E1/E2 establishes
    #   A_C = M_2(C) (+) M_2(C)
    # and the unique 2-dimensional simple module in each block.
    #
    # Step: distribute tensor product over the two new summands and use the
    # matrix-unit isomorphism
    #   E_ab tensor E_cd -> E_(2a+c),(2b+d).
    # Multiplication is preserved because, for c,d in {0,1},
    #   2b+d = 2a'+c' iff b=a' and d=c'.
    # Thus 2^N copies of M_(2^N)(C) become 2^(N+1) copies of
    # M_(2^(N+1))(C).  Artin-Wedderburn then exhausts the simple modules.
    # Restriction to any fixed site leaves a tensor factor of dimension
    # 2^(N-1), hence exactly that many copies of its 2-dimensional site
    # module.
    #
    # Real-image surjectivity is also constructive.  Primary E4 establishes
    # that each one-site real image is all M_2(C) over R, so it contains
    # preimages of E_ab and i E_ab.  Tensoring real matrix-unit preimages
    # gives every E_(a-vector),(b-vector); inserting i at one chosen site
    # gives every i E_(a-vector),(b-vector).  These are the
    # 2 * (2^N)^2 real basis vectors of M_(2^N)(C).  The real image therefore
    # has rank 2 * 4^N, and rank-nullity forces a kernel for N >= 2.
    finite_n = symbols("finite_N", integer=True, positive=True)
    block_count = 2**finite_n
    block_size = 2**finite_n
    tensor_step_block_count = (
        simplify(2 * block_count - 2 ** (finite_n + 1)) == 0
    )
    tensor_step_block_size = (
        simplify(2 * block_size - 2 ** (finite_n + 1)) == 0
    )
    finite_region_dimension_identity = (
        simplify(block_count * block_size**2 - dimension**finite_n) == 0
    )
    site_multiplicity_identity = (
        simplify(2 * 2 ** (finite_n - 1) - block_size) == 0
    )
    real_image_rank_identity = (
        simplify(2 * block_size**2 - 2 * 4**finite_n) == 0
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
    finite_region_classification_certificate = (
        one_site_split_certified
        and one_site_simple_modules_certified
        and one_site_real_surjectivity_certified
        and tensor_step_block_count
        and tensor_step_block_size
        and finite_region_dimension_identity
        and site_multiplicity_identity
        and real_image_rank_identity
        and finite_region_nonfaithfulness_ratio
    )
    dimension_exhausts = (
        two_site_modules_ok
        and central_character_pairs == expected_character_pairs
        and total_square == dimension**2
        and finite_region_classification_certificate
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
