#!/usr/bin/env python3
"""Exact Cl(3,0) ordered-volume identities and signed-permutation action."""

from __future__ import annotations

from itertools import permutations, product
from pathlib import Path
from typing import Callable


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
AUDIT_INPUT_PATHS = (
    "docs/CL3_ORDERED_VOLUME_ELEMENT_DETERMINANT_ACTION_NARROW_THEOREM_NOTE_2026-08-13.md",
)
NOTE_PATH = ROOT / AUDIT_INPUT_PATHS[0]


class Cl3:
    """Integer span of Cl(3,0) in mask order 1,e1,e2,e12,e3,e13,e23,e123."""

    __slots__ = ("c",)

    def __init__(self, coeffs: tuple[int, ...] | list[int]) -> None:
        values = tuple(int(value) for value in coeffs)
        if len(values) != 8:
            raise ValueError("Cl(3,0) vectors have eight integer coefficients")
        self.c = values

    def __add__(self, other: "Cl3") -> "Cl3":
        return Cl3(tuple(a + b for a, b in zip(self.c, other.c)))

    def __sub__(self, other: "Cl3") -> "Cl3":
        return Cl3(tuple(a - b for a, b in zip(self.c, other.c)))

    def __neg__(self) -> "Cl3":
        return Cl3(tuple(-value for value in self.c))

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Cl3) and self.c == other.c

    def __mul__(self, other: "Cl3") -> "Cl3":
        return multiply_with_rule(self, other, blade_mul)

    def grade_parity(self) -> int | None:
        parities = {
            mask.bit_count() % 2
            for mask, coefficient in enumerate(self.c)
            if coefficient
        }
        return next(iter(parities)) if len(parities) == 1 else None

    def is_scalar(self, value: int) -> bool:
        return self.c == (value, 0, 0, 0, 0, 0, 0, 0)


BladeRule = Callable[[int, int], tuple[int, int]]


def blade_mul(mask_a: int, mask_b: int) -> tuple[int, int]:
    """Euclidean Clifford product of two basis-blade masks."""
    sign = 1
    mask = mask_a
    for index in range(3):
        if ((mask_b >> index) & 1) == 0:
            continue
        higher = sum((mask >> other) & 1 for other in range(index + 1, 3))
        if higher % 2:
            sign = -sign
        mask ^= 1 << index
    return sign, mask


def mutant_blade_mul_without_swaps(mask_a: int, mask_b: int) -> tuple[int, int]:
    """One-fault copy: erase every anticommutation swap sign."""
    return 1, mask_a ^ mask_b


def multiply_with_rule(left: Cl3, right: Cl3, rule: BladeRule) -> Cl3:
    acc = [0] * 8
    for mask_a, coeff_a in enumerate(left.c):
        if coeff_a == 0:
            continue
        for mask_b, coeff_b in enumerate(right.c):
            if coeff_b == 0:
                continue
            sign, mask = rule(mask_a, mask_b)
            acc[mask] += sign * coeff_a * coeff_b
    return Cl3(tuple(acc))


def basis(mask: int) -> Cl3:
    coeffs = [0] * 8
    coeffs[mask] = 1
    return Cl3(tuple(coeffs))


ZERO = basis(0) - basis(0)
SCALAR = basis(0)
E1 = basis(1)
E2 = basis(2)
E3 = basis(4)
GENERATORS = (E1, E2, E3)


def volume() -> Cl3:
    return E1 * E2 * E3


def volume_reversed() -> Cl3:
    return E3 * E2 * E1


class Gauss:
    """Gaussian integer with exact arithmetic."""

    __slots__ = ("re", "im")

    def __init__(self, re: int, im: int = 0) -> None:
        self.re = int(re)
        self.im = int(im)

    def __add__(self, other: "Gauss") -> "Gauss":
        return Gauss(self.re + other.re, self.im + other.im)

    def __neg__(self) -> "Gauss":
        return Gauss(-self.re, -self.im)

    def __mul__(self, other: "Gauss") -> "Gauss":
        return Gauss(
            self.re * other.re - self.im * other.im,
            self.re * other.im + self.im * other.re,
        )

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Gauss) and (self.re, self.im) == (other.re, other.im)


class Mat2:
    """Two-by-two matrices over Gaussian integers."""

    __slots__ = ("a",)

    def __init__(self, entries: tuple[tuple[Gauss, Gauss], tuple[Gauss, Gauss]]) -> None:
        self.a = entries

    def __add__(self, other: "Mat2") -> "Mat2":
        return Mat2(
            tuple(
                tuple(self.a[row][col] + other.a[row][col] for col in range(2))
                for row in range(2)
            )  # type: ignore[arg-type]
        )

    def __neg__(self) -> "Mat2":
        return Mat2(
            tuple(tuple(-entry for entry in row) for row in self.a)  # type: ignore[arg-type]
        )

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Mat2) and self.a == other.a

    def __mul__(self, other: "Mat2") -> "Mat2":
        rows: list[tuple[Gauss, Gauss]] = []
        for row in range(2):
            values: list[Gauss] = []
            for col in range(2):
                value = Gauss(0)
                for mid in range(2):
                    value = value + self.a[row][mid] * other.a[mid][col]
                values.append(value)
            rows.append((values[0], values[1]))
        return Mat2((rows[0], rows[1]))


G0 = Gauss(0)
G1 = Gauss(1)
GI = Gauss(0, 1)
MAT_ZERO = Mat2(((G0, G0), (G0, G0)))
MAT_I = Mat2(((G1, G0), (G0, G1)))
I_TIMES_MAT_I = Mat2(((GI, G0), (G0, GI)))
SIGMA1 = Mat2(((G0, G1), (G1, G0)))
SIGMA2 = Mat2(((G0, Gauss(0, -1)), (GI, G0)))
SIGMA3 = Mat2(((G1, G0), (G0, Gauss(-1))))
PAULI_GENERATORS = (SIGMA1, SIGMA2, SIGMA3)


def pauli_volume() -> Mat2:
    return SIGMA1 * SIGMA2 * SIGMA3


def pauli_volume_reversed() -> Mat2:
    return SIGMA3 * SIGMA2 * SIGMA1


def mat_real_coordinates(matrix: Mat2) -> tuple[int, ...]:
    return tuple(
        coordinate
        for row in matrix.a
        for entry in row
        for coordinate in (entry.re, entry.im)
    )


def bareiss_determinant(values: list[list[int]]) -> int:
    """Exact fraction-free determinant for a square integer matrix."""
    matrix = [row[:] for row in values]
    size = len(matrix)
    if size == 1:
        return matrix[0][0]
    sign = 1
    previous = 1
    for pivot_index in range(size - 1):
        if matrix[pivot_index][pivot_index] == 0:
            swap = next(
                row
                for row in range(pivot_index + 1, size)
                if matrix[row][pivot_index] != 0
            )
            matrix[pivot_index], matrix[swap] = matrix[swap], matrix[pivot_index]
            sign = -sign
        pivot = matrix[pivot_index][pivot_index]
        for row in range(pivot_index + 1, size):
            for col in range(pivot_index + 1, size):
                numerator = (
                    matrix[row][col] * pivot
                    - matrix[row][pivot_index] * matrix[pivot_index][col]
                )
                matrix[row][col] = numerator // previous
            matrix[row][pivot_index] = 0
        previous = pivot
    return sign * matrix[-1][-1]


def pauli_basis_determinant() -> int:
    basis_images = (
        MAT_I,
        SIGMA1,
        SIGMA2,
        SIGMA3,
        SIGMA1 * SIGMA2,
        SIGMA1 * SIGMA3,
        SIGMA2 * SIGMA3,
        pauli_volume(),
    )
    columns = [mat_real_coordinates(matrix) for matrix in basis_images]
    coordinate_matrix = [
        [columns[col][row] for col in range(8)] for row in range(8)
    ]
    return bareiss_determinant(coordinate_matrix)


Matrix3 = tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]


def permutation_sign(perm: tuple[int, int, int]) -> int:
    inversions = sum(
        perm[i] > perm[j] for i in range(3) for j in range(i + 1, 3)
    )
    return -1 if inversions % 2 else 1


def determinant3(matrix: Matrix3) -> int:
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def signed_permutation_matrices() -> tuple[Matrix3, ...]:
    matrices: list[Matrix3] = []
    for perm_raw in permutations(range(3)):
        perm = (perm_raw[0], perm_raw[1], perm_raw[2])
        for signs in product((-1, 1), repeat=3):
            rows = tuple(
                tuple(signs[row] if perm[row] == col else 0 for col in range(3))
                for row in range(3)
            )
            matrices.append(rows)  # type: ignore[arg-type]
    return tuple(matrices)


def matrix_product(left: Matrix3, right: Matrix3) -> Matrix3:
    return tuple(
        tuple(sum(left[row][mid] * right[mid][col] for mid in range(3)) for col in range(3))
        for row in range(3)
    )  # type: ignore[return-value]


def apply_linear(matrix: Matrix3, generators: tuple[Cl3, Cl3, Cl3]) -> tuple[Cl3, Cl3, Cl3]:
    images: list[Cl3] = []
    for col in range(3):
        value = ZERO
        for row in range(3):
            coefficient = matrix[row][col]
            if coefficient == 1:
                value = value + generators[row]
            elif coefficient == -1:
                value = value - generators[row]
        images.append(value)
    return images[0], images[1], images[2]


def product3(first, second, third):
    return first * second * third


def mutant_no_swap_theorem_passes() -> bool:
    def mul(left: Cl3, right: Cl3) -> Cl3:
        return multiply_with_rule(left, right, mutant_blade_mul_without_swaps)

    car12 = mul(E1, E2) + mul(E2, E1) == ZERO
    forward = mul(mul(E1, E2), E3)
    reverse = mul(mul(E3, E2), E1)
    return car12 and reverse == -forward


def mutant_forward_word_passes() -> bool:
    mutated_reverse = E1 * E2 * E3
    return mutated_reverse == -volume()


def mutant_anticentral_passes() -> bool:
    return volume() * E1 == -(E1 * volume())


def mutant_positive_square_passes() -> bool:
    return volume() * volume() == SCALAR


def mutant_pauli_orientation_passes() -> bool:
    return (-SIGMA1) * SIGMA2 * SIGMA3 == I_TIMES_MAT_I


def mutant_group_census_passes(matrices: tuple[Matrix3, ...]) -> bool:
    return len(matrices) == 24


def mutant_all_preserve_passes(matrices: tuple[Matrix3, ...]) -> bool:
    omega = volume()
    return all(product3(*apply_linear(matrix, GENERATORS)) == omega for matrix in matrices)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool) -> None:
        result = bool(condition)
        self.passed += int(result)
        self.failed += int(not result)
        print(f"{'PASS' if result else 'FAIL'}: {label} {statement}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")

    print("external_scientific_inputs: none")
    print("package_local_integrity_reads: " + AUDIT_INPUT_PATHS[0])
    print("audit_input_paths: " + ", ".join(AUDIT_INPUT_PATHS))

    checks.check(
        "package-input",
        "the declared theorem note is readable",
        NOTE_PATH.is_file(),
    )
    required_note_fields = (
        "**Status:** proposed_retained",
        "target_claim_type: bounded_theorem",
        "actual_current_surface_status: candidate-retained-grade",
        "Direct scientific dependencies: none.",
        "bare_retained_allowed: false",
    )
    checks.check(
        "package-metadata",
        "the theorem surface carries the required proposal and trace fields",
        all(field in note for field in required_note_fields),
    )

    car_ok = all(
        left * right + right * left == (SCALAR + SCALAR if i == j else ZERO)
        for i, left in enumerate(GENERATORS)
        for j, right in enumerate(GENERATORS)
    )
    omega = volume()
    omega_rev = volume_reversed()
    checks.check("clifford-car", "all nine Euclidean CAR identities hold", car_ok)
    checks.check("reverse-order", "e3 e2 e1 equals minus e1 e2 e3", omega_rev == -omega)
    checks.check(
        "odd-grade",
        "both ordered volume words have odd grade",
        omega.grade_parity() == 1 and omega_rev.grade_parity() == 1,
    )
    checks.check(
        "centrality",
        "both volume words commute with all three generators",
        all(
            omega * generator == generator * omega
            and omega_rev * generator == generator * omega_rev
            for generator in GENERATORS
        ),
    )
    checks.check(
        "square-minus-one",
        "both volume words square to minus the identity",
        (omega * omega).is_scalar(-1) and (omega_rev * omega_rev).is_scalar(-1),
    )

    pauli_car_ok = all(
        left * right + right * left == (MAT_I + MAT_I if i == j else MAT_ZERO)
        for i, left in enumerate(PAULI_GENERATORS)
        for j, right in enumerate(PAULI_GENERATORS)
    )
    pauli_w = pauli_volume()
    pauli_rev = pauli_volume_reversed()
    checks.check("pauli-car", "the Pauli exhibit obeys all nine CAR identities", pauli_car_ok)
    checks.check(
        "pauli-volume",
        "the forward and reversed Pauli products are plus and minus iI",
        pauli_w == I_TIMES_MAT_I and pauli_rev == -I_TIMES_MAT_I,
    )
    checks.check(
        "pauli-squares",
        "both Pauli volume products square to minus the identity",
        pauli_w * pauli_w == -MAT_I and pauli_rev * pauli_rev == -MAT_I,
    )
    checks.check(
        "pauli-real-rank",
        "the eight real basis images have exact coordinate determinant minus sixteen",
        pauli_basis_determinant() == -16,
    )

    matrices = signed_permutation_matrices()
    matrix_set = set(matrices)
    determinants = tuple(determinant3(matrix) for matrix in matrices)
    checks.check(
        "signed-permutation-census",
        "the enumeration has 48 unique matrices",
        len(matrices) == 48 and len(matrix_set) == 48,
    )
    checks.check(
        "determinant-split",
        "the determinant classes contain 24 matrices each",
        determinants.count(1) == 24 and determinants.count(-1) == 24,
    )
    checks.check(
        "group-closure",
        "all signed-permutation products stay in the 48-element set",
        all(matrix_product(left, right) in matrix_set for left in matrices for right in matrices),
    )

    determinant_action = True
    proper_action = True
    improper_action = True
    for matrix, determinant in zip(matrices, determinants):
        image = product3(*apply_linear(matrix, GENERATORS))
        determinant_action &= image == (omega if determinant == 1 else -omega)
        if determinant == 1:
            proper_action &= image == omega and -image == -omega
        else:
            improper_action &= image == -omega and -image == omega
    checks.check(
        "determinant-action",
        "every signed permutation sends omega to determinant times omega",
        determinant_action,
    )
    checks.check(
        "proper-action",
        "all 24 determinant-plus-one elements fix both ordered signs",
        proper_action,
    )
    checks.check(
        "improper-action",
        "all 24 determinant-minus-one elements exchange the ordered signs",
        improper_action,
    )

    mutations = (
        ("mutation-clifford-swap", mutant_no_swap_theorem_passes()),
        ("mutation-reverse-word", mutant_forward_word_passes()),
        ("mutation-centrality-sign", mutant_anticentral_passes()),
        ("mutation-square-sign", mutant_positive_square_passes()),
        ("mutation-pauli-orientation", mutant_pauli_orientation_passes()),
        ("mutation-group-census", mutant_group_census_passes(matrices)),
        ("mutation-determinant-action", mutant_all_preserve_passes(matrices)),
    )
    for label, mutant_passes in mutations:
        checks.check(label, "the one-fault scientific mutant is rejected", not mutant_passes)
    checks.check(
        "mutation-aggregate",
        "all seven load-bearing one-fault mutants are rejected",
        all(not mutant_passes for _, mutant_passes in mutations),
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
