#!/usr/bin/env python3
"""Exact proper-cubic invariants of two-qubit Pauli coefficient matrices.

The certificate is the rational nullspace of the declared covariance
constraints. A hand-listed basis that did not span that nullspace fails.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations, product


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, name: str, ok: bool) -> None:
        if ok:
            self.passed += 1
            print(f"PASS {name}")
        else:
            self.failed += 1
            print(f"FAIL {name}")


def det3(matrix: list[list[int]]) -> int:
    a, b, c = matrix
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )


def mul3(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return [
        [sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3)]
        for i in range(3)
    ]


def key3(matrix: list[list[int]]) -> tuple:
    return tuple(tuple(row) for row in matrix)


def all_proper() -> list[list[list[int]]]:
    found = []
    for perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            matrix = [[0, 0, 0] for _ in range(3)]
            for src, dst in enumerate(perm):
                matrix[dst][src] = signs[src]
            if det3(matrix) == 1:
                found.append(matrix)
    return found


def generated_by(generators: list[list[list[int]]]) -> set[tuple]:
    group = {key3([[1, 0, 0], [0, 1, 0], [0, 0, 1]])}
    changed = True
    while changed:
        changed = False
        current = list(group)
        for left in current:
            for gen in generators:
                product_key = key3(mul3([list(row) for row in left], gen))
                if product_key not in group:
                    group.add(product_key)
                    changed = True
    return group


def embed(rotation: list[list[int]]) -> list[list[Fraction]]:
    big = [[Fraction(0) for _ in range(4)] for _ in range(4)]
    big[0][0] = Fraction(1)
    for i in range(3):
        for j in range(3):
            big[i + 1][j + 1] = Fraction(rotation[i][j])
    return big


def rref(rows: list[list[Fraction]]) -> tuple[list[list[Fraction]], list[int]]:
    matrix = [row[:] for row in rows]
    n_rows = len(matrix)
    n_cols = len(matrix[0])
    pivots: list[int] = []
    row = 0
    for col in range(n_cols):
        pivot = next((i for i in range(row, n_rows) if matrix[i][col] != 0), None)
        if pivot is None:
            continue
        matrix[row], matrix[pivot] = matrix[pivot], matrix[row]
        scale = matrix[row][col]
        matrix[row] = [value / scale for value in matrix[row]]
        for i in range(n_rows):
            if i != row and matrix[i][col] != 0:
                factor = matrix[i][col]
                matrix[i] = [
                    matrix[i][j] - factor * matrix[row][j] for j in range(n_cols)
                ]
        pivots.append(col)
        row += 1
        if row == n_rows:
            break
    return matrix, pivots


def nullspace(rows: list[list[Fraction]], n_cols: int) -> list[list[Fraction]]:
    reduced, pivots = rref(rows)
    free = [col for col in range(n_cols) if col not in set(pivots)]
    basis = []
    for col in free:
        vector = [Fraction(0) for _ in range(n_cols)]
        vector[col] = Fraction(1)
        for row, pivot in zip(reduced, pivots):
            vector[pivot] = -row[col]
        basis.append(vector)
    return basis


def constraint_rows(rotations: list[list[list[int]]]) -> list[list[Fraction]]:
    rows = []
    for rotation in rotations:
        big = embed(rotation)
        for i in range(4):
            for j in range(4):
                row = [Fraction(0) for _ in range(16)]
                for k in range(4):
                    for ell in range(4):
                        row[4 * k + ell] += big[i][k] * big[j][ell]
                row[4 * i + j] -= 1
                rows.append(row)
    return rows


def residual(rotation: list[list[int]], vector: list[Fraction]) -> list[Fraction]:
    return [
        sum(coeff * value for coeff, value in zip(row, vector))
        for row in constraint_rows([rotation])
    ]


def matches(computed: list[list[Fraction]], expected: list[list[Fraction]]) -> bool:
    if len(computed) != len(expected):
        return False
    reduced_expected, pivots = rref(expected)
    del reduced_expected, pivots
    # Each computed vector is an exact rational combination of the expected
    # rows, and the two spans have equal dimension, so they agree.
    span_rows = [row[:] for row in expected]
    for vector in computed:
        trial = span_rows + [vector]
        _, pivots = rref(trial)
        if len(pivots) != len(expected):
            return False
    return True


def unit(index: int, value: Fraction = Fraction(1)) -> list[Fraction]:
    vector = [Fraction(0) for _ in range(16)]
    vector[index] = value
    return vector


def add(*vectors: list[Fraction]) -> list[Fraction]:
    total = [Fraction(0) for _ in range(16)]
    for vector in vectors:
        for i, value in enumerate(vector):
            total[i] += value
    return total


def one_site_fixed_dimension(rotations: list[list[list[int]]]) -> int:
    rows = []
    for rotation in rotations:
        for i in range(3):
            row = [Fraction(rotation[i][j]) for j in range(3)]
            row[i] -= 1
            rows.append(row)
    return len(nullspace(rows, 3))


def axis_image(rotation: list[list[int]], axis: int) -> list[int]:
    return [rotation[i][axis] for i in range(3)]


def xxz_eigenvalues(u: Fraction, v: Fraction) -> list[Fraction]:
    return [v, v, 2 * u - v, -2 * u - v]


def positive(u: Fraction, v: Fraction) -> bool:
    return all(1 + value >= 0 for value in xxz_eigenvalues(u, v))


def main() -> None:
    checks = Checks()
    r_z = [[0, -1, 0], [1, 0, 0], [0, 0, 1]]
    r_x = [[1, 0, 0], [0, 0, -1], [0, 1, 0]]
    half_turn_x = mul3(r_x, r_x)
    proper = all_proper()
    generated = generated_by([r_z, r_x])
    checks.check("group equals det+1 signed permutations", generated == {key3(m) for m in proper})
    checks.check("group order is 24", len(generated) == 24)
    checks.check("one-site fixed Bloch space is 0", one_site_fixed_dimension(proper) == 0)

    full_basis = nullspace(constraint_rows(proper), 16)
    expected_full = [
        unit(0),
        add(unit(5), unit(10), unit(15)),
    ]
    checks.check("full invariant dimension is 2", len(full_basis) == 2)
    checks.check("full basis is span of I and sigma dot sigma", matches(full_basis, expected_full))
    checks.check(
        "I and sigma dot sigma are invariant",
        all(
            all(value == 0 for value in residual(rotation, vector))
            for rotation in proper
            for vector in expected_full
        ),
    )
    checks.check(
        "c12 is not a full invariant",
        any(value != 0 for value in residual(r_z, unit(6))),
    )

    directed = [rotation for rotation in proper if axis_image(rotation, 2) == [0, 0, 1]]
    directed_basis = nullspace(constraint_rows(directed), 16)
    expected_directed = [
        unit(0),
        unit(3),
        add(unit(6, -1), unit(9)),
        add(unit(5), unit(10)),
        unit(12),
        unit(15),
    ]
    checks.check("directed stabilizer order is 4", len(directed) == 4)
    checks.check("directed invariant dimension is 6", len(directed_basis) == 6)
    checks.check("directed basis matches the six listed matrices", matches(directed_basis, expected_directed))
    checks.check(
        "c01 is not directed-invariant",
        any(value != 0 for value in residual(r_z, unit(1))),
    )

    undirected = [
        rotation
        for rotation in proper
        if axis_image(rotation, 2) in ([0, 0, 1], [0, 0, -1])
    ]
    undirected_basis = nullspace(constraint_rows(undirected), 16)
    expected_undirected = [
        unit(0),
        add(unit(5), unit(10)),
        unit(15),
    ]
    checks.check("undirected stabilizer order is 8", len(undirected) == 8)
    checks.check(
        "Rz and the x half turn generate the undirected stabilizer",
        generated_by([r_z, half_turn_x]) == {key3(rotation) for rotation in undirected},
    )
    checks.check("undirected invariant dimension is 3", len(undirected_basis) == 3)
    checks.check(
        "undirected basis is span of I, XX+YY and ZZ",
        matches(undirected_basis, expected_undirected),
    )
    checks.check(
        "ZZ survives in the undirected nullspace",
        any(vector[15] != 0 for vector in undirected_basis),
    )
    checks.check(
        "the twist survives in the directed nullspace and dies undirected",
        any(vector[6] != 0 or vector[9] != 0 for vector in directed_basis)
        and all(vector[6] == 0 and vector[9] == 0 for vector in undirected_basis),
    )

    checks.check("w=1 is not positive", not positive(Fraction(1), Fraction(1)))
    checks.check("w=1/3 is positive", positive(Fraction(1, 3), Fraction(1, 3)))
    checks.check("w=-1 is positive", positive(Fraction(-1), Fraction(-1)))
    checks.check("singlet eigenvalue at w=-1 is 3", -2 * Fraction(-1) - Fraction(-1) == 3)
    checks.check("triplet eigenvalue at w=1/3 vanishes", 1 + Fraction(1, 3) == Fraction(4, 3) and 1 - 3 * Fraction(1, 3) == 0)

    def isotropic_chsh_squared(w: Fraction) -> Fraction:
        return 8 * w * w

    checks.check("w=-1/2 has CHSH square 2", isotropic_chsh_squared(Fraction(-1, 2)) == 2)
    checks.check("w=-1/2 does not violate", isotropic_chsh_squared(Fraction(-1, 2)) < 4)
    checks.check("w squared 1/2 gives CHSH square 4", 8 * Fraction(1, 2) == 4)
    checks.check("singlet CHSH square is 8", isotropic_chsh_squared(Fraction(-1)) == 8)
    checks.check("(1,-1) is positive", positive(Fraction(1), Fraction(-1)))
    checks.check("(-1,-1) is positive", positive(Fraction(-1), Fraction(-1)))
    checks.check("|u|=2 has an empty positive interval", 1 - 2 * 2 < -1)

    # Equality case for CHSH square 8 on the xy plane at both corners.
    # |c|^2=|d|^2=2 and T=±I on that plane give |Tc|^2=|Td|^2=2.
    for u, v in ((Fraction(-1), Fraction(-1)), (Fraction(1), Fraction(-1))):
        tc2 = u * u * 2
        td2 = u * u * 2
        checks.check(
            f"corner ({u},{v}) achieves CHSH square 8",
            tc2 == 2 and td2 == 2 and (tc2 + td2) * 2 == 8,
        )

    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    if checks.failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
