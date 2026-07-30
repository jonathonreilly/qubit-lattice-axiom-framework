#!/usr/bin/env python3
"""Self-contained signed-Pauli and binary-tableau substrate for Cycle 727."""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product as cartesian_product


Coord = tuple[int, int, int]


@dataclass(frozen=True)
class Pauli:
    """Pauli word in the convention ``i**phase X**x Z**z``."""

    phase: int = 0
    x: int = 0
    z: int = 0

    def __matmul__(self, other: "Pauli") -> "Pauli":
        crossing = (self.z & other.x).bit_count() & 1
        return Pauli(
            (self.phase + other.phase + 2 * crossing) % 4,
            self.x ^ other.x,
            self.z ^ other.z,
        )

    def symplectic(self, qubits: int) -> int:
        return self.x | (self.z << qubits)


@dataclass(frozen=True)
class Coordinates:
    phase: int
    v_mask: int
    w_mask: int


def pauli_product(rows) -> Pauli:
    output = Pauli()
    for row in rows:
        output = output @ row
    return output


def gf2_rank(rows) -> int:
    pivots: dict[int, int] = {}
    for original in rows:
        row = int(original)
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                break
    return len(pivots)


def xor_rows(rows) -> int:
    output = 0
    for row in rows:
        output ^= row
    return output


def symplectic(left: int, right: int, qubits: int) -> int:
    mask = (1 << qubits) - 1
    left_x, left_z = left & mask, left >> qubits
    right_x, right_z = right & mask, right >> qubits
    return (
        (left_x & right_z).bit_count()
        + (left_z & right_x).bit_count()
    ) & 1


def anticommutes(left: Pauli, right: Pauli) -> int:
    return (
        (left.x & right.z).bit_count()
        + (left.z & right.x).bit_count()
    ) & 1


def gf2_solve(rows: list[tuple[int, int]]) -> tuple[int, int, int]:
    """Return one free-zero solution, coefficient rank, and contradictions."""
    pivots: dict[int, tuple[int, int]] = {}
    contradictions = 0
    for original_mask, original_rhs in rows:
        mask, rhs = original_mask, original_rhs
        while mask:
            pivot = mask.bit_length() - 1
            if pivot in pivots:
                old_mask, old_rhs = pivots[pivot]
                mask ^= old_mask
                rhs ^= old_rhs
            else:
                pivots[pivot] = (mask, rhs)
                break
        else:
            contradictions += rhs
    solution = 0
    for pivot in sorted(pivots):
        mask, rhs = pivots[pivot]
        if ((mask & solution).bit_count() & 1) != rhs:
            solution ^= 1 << pivot
    return solution, len(pivots), contradictions


def homogeneous_nullspace(
    equations: tuple[int, ...], variables: int
) -> tuple[int, ...]:
    pivots: dict[int, int] = {}
    for original in equations:
        row = original
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                break
    output = []
    for free in range(variables):
        if free in pivots:
            continue
        solution = 1 << free
        for pivot in sorted(pivots):
            if (pivots[pivot] & solution).bit_count() & 1:
                solution ^= 1 << pivot
        if any((row & solution).bit_count() & 1 for row in equations):
            raise AssertionError("nullspace replay failed")
        output.append(solution)
    return tuple(output)


def _dual_vectors(w_vectors: list[int], qubits: int) -> list[int]:
    pivots: dict[int, tuple[int, int]] = {}
    mask = (1 << qubits) - 1
    for index, vector in enumerate(w_vectors):
        equation = (vector >> qubits) | ((vector & mask) << qubits)
        combination = 1 << index
        while equation:
            pivot = equation.bit_length() - 1
            if pivot in pivots:
                old_equation, old_combination = pivots[pivot]
                equation ^= old_equation
                combination ^= old_combination
            else:
                pivots[pivot] = (equation, combination)
                break
        else:
            raise ValueError("W rows are not independent")
    for pivot in sorted(pivots):
        pivot_mask, pivot_combination = pivots[pivot]
        for other in tuple(pivots):
            if other != pivot and (pivots[other][0] >> pivot) & 1:
                old_mask, old_combination = pivots[other]
                pivots[other] = (
                    old_mask ^ pivot_mask,
                    old_combination ^ pivot_combination,
                )
    duals = [0] * qubits
    for pivot, (_equation, combination) in pivots.items():
        while combination:
            bit = combination & -combination
            duals[bit.bit_length() - 1] |= 1 << pivot
            combination ^= bit
    return duals


def complete_tableau(w_rows, explicit_v, qubits: int) -> tuple[Pauli, ...]:
    w_vectors = [row.symplectic(qubits) for row in w_rows]
    vectors = _dual_vectors(w_vectors, qubits)
    explicit_count = len(explicit_v)
    for index, row in enumerate(explicit_v):
        vector = row.symplectic(qubits)
        if any(
            symplectic(vector, w_vectors[column], qubits)
            != int(index == column)
            for column in range(qubits)
        ):
            raise ValueError(("explicit V row is not canonical", index))
        vectors[index] = vector
    for index in range(explicit_count, qubits):
        vector = vectors[index]
        for logical in range(explicit_count):
            if symplectic(
                vector, explicit_v[logical].symplectic(qubits), qubits
            ):
                vector ^= w_vectors[logical]
        vectors[index] = vector
    for left in range(explicit_count, qubits):
        for right in range(left + 1, qubits):
            if symplectic(vectors[left], vectors[right], qubits):
                vectors[left] ^= w_vectors[right]
    mask = (1 << qubits) - 1
    rows = list(explicit_v)
    for vector in vectors[explicit_count:]:
        x, z = vector & mask, vector >> qubits
        rows.append(Pauli((x & z).bit_count() & 1, x, z))
    return tuple(rows)


def decode(row, w_rows, v_rows, qubits: int) -> Coordinates:
    vector = row.symplectic(qubits)
    v_mask = sum(
        symplectic(vector, w.symplectic(qubits), qubits) << index
        for index, w in enumerate(w_rows)
    )
    w_mask = sum(
        symplectic(vector, v.symplectic(qubits), qubits) << index
        for index, v in enumerate(v_rows)
    )
    reconstructed = pauli_product(
        v_rows[index]
        for index in range(qubits)
        if (v_mask >> index) & 1
    ) @ pauli_product(
        w_rows[index]
        for index in range(qubits)
        if (w_mask >> index) & 1
    )
    if reconstructed.x != row.x or reconstructed.z != row.z:
        raise ValueError("tableau coordinate reconstruction failed")
    return Coordinates(
        (row.phase - reconstructed.phase) % 4,
        v_mask,
        w_mask,
    )


def apply_images(images, row: Pauli, qubits: int) -> Pauli:
    output = Pauli(row.phase)
    for offset, bits in ((0, row.x), (qubits, row.z)):
        while bits:
            bit = bits & -bits
            output = output @ images[offset + bit.bit_length() - 1]
            bits ^= bit
    return output


def box_cells(shape: tuple[int, int, int]) -> tuple[Coord, ...]:
    return tuple(cartesian_product(*(range(size) for size in shape)))


def target_cell(cell: Coord, axis: int) -> Coord:
    return tuple(
        value + int(index == axis) for index, value in enumerate(cell)
    )


def expected_logical_terms(
    cells: tuple[Coord, ...], owner: Coord, axis: int
) -> tuple[Pauli, ...]:
    left = 6 * cells.index(owner) + 2 * axis + 1
    right = 6 * cells.index(target_cell(owner, axis)) + 2 * axis
    left, right = sorted((left, right))
    endpoints = (1 << left) | (1 << right)
    between = ((1 << right) - 1) ^ ((1 << (left + 1)) - 1)
    return (
        Pauli(z=1 << left),
        Pauli(z=1 << right),
        Pauli(phase=2, x=endpoints, z=between | endpoints),
        Pauli(x=endpoints, z=between),
    )


def canonical_pauli(vector: int, qubits: int) -> Pauli:
    mask = (1 << qubits) - 1
    x, z = vector & mask, vector >> qubits
    return Pauli((x & z).bit_count() & 1, x, z)


def independent_paired_basis(
    physical: tuple[int, ...], target: tuple[int, ...]
) -> tuple[tuple[int, int, int], ...]:
    pivots: dict[int, tuple[int, int]] = {}
    output = []
    for index, original in enumerate(physical):
        row = original
        combination = 1 << index
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                previous, previous_combination = pivots[pivot]
                row ^= previous
                combination ^= previous_combination
            else:
                pivots[pivot] = (row, combination)
                target_row = xor_rows(
                    target[item]
                    for item in range(len(target))
                    if (combination >> item) & 1
                )
                output.append((row, target_row, combination))
                break
    return tuple(output)


def symplectic_split_paired(
    rows: tuple[tuple[int, int, int], ...], qubits: int
) -> tuple[
    tuple[tuple[int, int, int], ...],
    tuple[
        tuple[tuple[int, int, int], tuple[int, int, int]],
        ...,
    ],
]:
    remaining = list(rows)
    radicals = []
    pairs = []
    while remaining:
        left = remaining.pop()
        partner = next(
            (
                index
                for index, right in enumerate(remaining)
                if symplectic(left[0], right[0], qubits)
            ),
            None,
        )
        if partner is None:
            radicals.append(left)
            continue
        right = remaining.pop(partner)
        pairs.append((left, right))
        transformed = []
        for row in remaining:
            values = list(row)
            if symplectic(values[0], right[0], qubits):
                values = [
                    value ^ other for value, other in zip(values, left)
                ]
            if symplectic(values[0], left[0], qubits):
                values = [
                    value ^ other for value, other in zip(values, right)
                ]
            transformed.append(tuple(values))
        remaining = transformed
    return tuple(radicals), tuple(pairs)


def symplectic_split_vectors(
    rows: tuple[int, ...], qubits: int
) -> tuple[tuple[int, ...], tuple[tuple[int, int], ...]]:
    remaining = list(rows)
    radicals = []
    pairs = []
    while remaining:
        left = remaining.pop()
        partner = next(
            (
                index
                for index, right in enumerate(remaining)
                if symplectic(left, right, qubits)
            ),
            None,
        )
        if partner is None:
            radicals.append(left)
            continue
        right = remaining.pop(partner)
        pairs.append((left, right))
        transformed = []
        for row in remaining:
            if symplectic(row, right, qubits):
                row ^= left
            if symplectic(row, left, qubits):
                row ^= right
            transformed.append(row)
        remaining = transformed
    return tuple(radicals), tuple(pairs)
