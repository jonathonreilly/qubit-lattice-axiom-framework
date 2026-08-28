#!/usr/bin/env python3
"""Independent exact checks for the finite-gap/strict-coupling packet.

This checker uses only :class:`fractions.Fraction` for the load-bearing
rational bounds.  It does not import SymPy or the primary runner.
"""

from __future__ import annotations

import itertools
from fractions import Fraction as F
from math import prod


AUDIT_TIMEOUT_SEC = 120


def shell_probability(inner: F, outer: F) -> F:
    """Normalized B^3 probability of one radial shell."""
    return outer**3 - inner**3


def shrunken_shell_fraction(inner: F, outer: F, m: int) -> F:
    delta = F(1, m)
    return ((outer - delta) ** 3 - (inner + delta) ** 3) / (
        outer**3 - inner**3
    )


def diagonal_lower(m: int) -> F:
    first = shrunken_shell_fraction(F(1, 4), F(1, 3), m)
    second = shrunken_shell_fraction(F(1, 2), F(2, 3), m)
    return min(first, second) * (1 - F(3, m * m))


def cross_upper(m: int) -> F:
    """Rational majorant after e^x >= x^4/4! and pi > 1."""
    factorial_four = prod(range(1, 5))
    prefactor = F(37 * factorial_four * 72**4, 1296)
    return prefactor / m**10


def radial_ratio_lower(m: int) -> F:
    return diagonal_lower(m) - cross_upper(m)


def normalized_gaussian_even_moment(order: int) -> F:
    """Standard-normal even moment from integration-by-parts recurrence."""
    if order == 0:
        return F(1)
    if order < 0 or order % 2:
        raise ValueError("order must be a nonnegative even integer")
    return (order - 1) * normalized_gaussian_even_moment(order - 2)


def two_by_two_det(matrix: tuple[tuple[F, F], tuple[F, F]]) -> F:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def matvec_three(matrix: tuple[tuple[F, F, F], ...],
                 vector: tuple[F, F, F]) -> tuple[F, F, F]:
    return tuple(sum((matrix[i][j] * vector[j] for j in range(3)), F(0))
                 for i in range(3))


def permutation_sign(permutation: tuple[int, ...]) -> int:
    inversions = sum(
        permutation[i] > permutation[j]
        for i in range(len(permutation))
        for j in range(i + 1, len(permutation))
    )
    return -1 if inversions % 2 else 1


def signed_permutation_image(
    permutation: tuple[int, int, int],
    signs: tuple[int, int, int],
    vector: tuple[F, F, F],
) -> tuple[F, F, F]:
    image = [F(0), F(0), F(0)]
    for column, row in enumerate(permutation):
        image[row] = signs[column] * vector[column]
    return tuple(image)


def independent_facts() -> dict[str, bool]:
    shell_one = shell_probability(F(1, 4), F(1, 3))
    shell_two = shell_probability(F(1, 2), F(2, 3))

    first_loss_formula = all(
        shrunken_shell_fraction(F(1, 4), F(1, 3), m)
        == 1 - F(900 * m * m - 432 * m + 3456, 37 * m**3)
        for m in (48, 96, 192)
    )
    second_is_larger = all(
        shrunken_shell_fraction(F(1, 2), F(2, 3), m)
        > shrunken_shell_fraction(F(1, 4), F(1, 3), m)
        for m in (48, 96, 192)
    )

    ratios = tuple(radial_ratio_lower(m) for m in (48, 96, 192, 384))

    gaussian_second_moment = sum(
        (normalized_gaussian_even_moment(2) for _ in range(3)), F(0)
    )
    cross_prefactor = cross_upper(1)
    cross_scale_squared_without_pi = F(2, 9) * shell_one * shell_two

    vector = (F(1, 4), F(1, 5), F(1, 6))
    vector_norm = sum((coordinate**2 for coordinate in vector), F(0))
    signed_images = []
    determinant_signs = []
    for permutation in itertools.permutations((0, 1, 2)):
        for signs in itertools.product((-1, 1), repeat=3):
            signed_images.append(
                signed_permutation_image(permutation, signs, vector)
            )
            determinant_signs.append(permutation_sign(permutation) * prod(signs))
    all_orthogonal = all(
        sum((coordinate**2 for coordinate in image), F(0)) == vector_norm
        for image in signed_images
    )

    parent_top, matter_top, matter_radial, sites = F(7), F(5), F(3), 3
    product_top = parent_top * matter_top**sites
    product_radial = parent_top * matter_radial * matter_top**(sites - 1)

    # Reconstruct the dyadic finite diagnostic from its atomic kernels.
    dyadic_t = F(1, 2)
    atoms = (0, 1, -1)
    matter_kernel = tuple(
        tuple(dyadic_t ** ((left - right) ** 2) / 3 for right in atoms)
        for left in atoms
    )
    matter_even_00 = matter_kernel[0][0]
    matter_even_11 = (
        matter_kernel[1][1] + matter_kernel[1][2]
        + matter_kernel[2][1] + matter_kernel[2][2]
    ) / 2
    matter_even_off_product = (
        (matter_kernel[0][1] + matter_kernel[0][2])
        * (matter_kernel[1][0] + matter_kernel[2][0]) / 2
    )
    matter_trace = matter_even_00 + matter_even_11
    matter_determinant = (
        matter_even_00 * matter_even_11 - matter_even_off_product
    )
    matter_discriminant = matter_trace**2 - 4 * matter_determinant
    odd_matter_eigenvalue = (
        matter_kernel[1][1] - matter_kernel[1][2]
    )

    dyadic_a = F(1, 2)
    gauge_kernel = (
        (F(1, 2), dyadic_a / 2),
        (dyadic_a / 2, F(1, 2)),
    )
    gauge_even = (
        gauge_kernel[0][0] + gauge_kernel[0][1]
        + gauge_kernel[1][0] + gauge_kernel[1][1]
    ) / 2
    gauge_odd = (
        gauge_kernel[0][0] - gauge_kernel[0][1]
        - gauge_kernel[1][0] + gauge_kernel[1][1]
    ) / 2

    reflection_diagonal = (-1, 1, 1)
    exterior_character = prod(1 + entry for entry in reflection_diagonal)
    reflection_defect = 16 - 2 * exterior_character

    # mu_+ / mu_- > 3 is equivalent to sqrt(57) > 11/2.  Therefore the
    # determinant gauge mode, not the lower even-matter mode, is second.
    gauge_mode_is_second = F(57) > F(121, 4)
    conjugation_trivial = all(
        h ^ u ^ h == u for h in (0, 1) for u in (0, 1)
    )
    matter_projector = (
        (F(1), F(0), F(0)),
        (F(0), F(1, 2), F(1, 2)),
        (F(0), F(1, 2), F(1, 2)),
    )
    matter_odd = (F(0), F(1), F(-1))
    matter_even = (F(0), F(1), F(1))

    return {
        "normalized radial shell masses are derived exactly": (
            shell_one == F(37, 1728) and shell_two == F(37, 216)
        ),
        "first-shell boundary loss matches the closed rational formula": (
            first_loss_formula
        ),
        "the thinner first shell supplies the minimum diagonal bound": (
            second_is_larger
        ),
        "the explicit radial ratio lower bound is positive and improves": (
            all(value > 0 for value in ratios)
            and all(left < right for left, right in zip(ratios, ratios[1:]))
        ),
        "the rational cross-shell majorant decays by ten powers": (
            cross_upper(96) == cross_upper(48) / 2**10
            and cross_prefactor == F(18_413_568)
        ),
        "the normalized cross-shell Gaussian prefactor is independently derived": (
            cross_scale_squared_without_pi == F(37, 1296) ** 2
        ),
        "the Gaussian tail loss derives from three coordinate moments": (
            gaussian_second_moment == 3
        ),
        "all signed cubic frames preserve radius including improper frames": (
            len(signed_images) == 48
            and determinant_signs.count(-1) == 24
            and all_orthogonal
        ),
        "the projected parent-times-matter radial eigenvalue ratio is exact": (
            product_radial / product_top == matter_radial / matter_top
        ),
        "dyadic even-matter trace and determinant are reconstructed": (
            matter_trace == F(11, 16)
            and matter_determinant == F(1, 16)
        ),
        "dyadic even-matter eigenvalue discriminant is exact": (
            matter_discriminant == F(57, 256)
        ),
        "the odd matter mode is explicit before projection": (
            odd_matter_eigenvalue == F(5, 16)
        ),
        "the two-point gauge convolution eigenvalues are derived": (
            gauge_even == F(3, 4) and gauge_odd == F(1, 4)
        ),
        "the improper diagnostic defect is derived from the exterior character": (
            reflection_defect == 16
        ),
        "periodic two-point holonomy survives abelian conjugation": (
            conjugation_trivial
        ),
        "the common Haar projector removes only the matter-odd vector": (
            matvec_three(matter_projector, matter_odd) == (F(0), F(0), F(0))
            and matvec_three(matter_projector, matter_even) == matter_even
        ),
        "the exact projected diagnostic gap is log three": (
            gauge_even / gauge_odd == 3 and gauge_mode_is_second
        ),
    }


def main() -> int:
    facts = independent_facts()
    passed = 0
    failed = 0
    for name, condition in facts.items():
        print(f"[{'PASS' if condition else 'FAIL'}] {name}")
        passed += int(condition)
        failed += int(not condition)
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return int(failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
