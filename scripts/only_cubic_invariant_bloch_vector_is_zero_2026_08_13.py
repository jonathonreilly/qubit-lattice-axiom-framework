#!/usr/bin/env python3
"""Exact checks for the proper-cubic fixed-space and Bloch-body theorem."""

from __future__ import annotations

import re
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    ROOT
    / "docs"
    / "ONLY_CUBIC_INVARIANT_BLOCH_VECTOR_IS_ZERO_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)

AUDIT_INPUT_PATHS = (
    "docs/ONLY_CUBIC_INVARIANT_BLOCH_VECTOR_IS_ZERO_BOUNDED_THEOREM_NOTE_2026-08-13.md",
)

Vec = tuple[Fraction, Fraction, Fraction]
Mat3 = tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]
C = tuple[Fraction, Fraction]
HMat = tuple[tuple[C, C], tuple[C, C]]

ZERO: Vec = (Fraction(0), Fraction(0), Fraction(0))
UNIT_X: Vec = (Fraction(1), Fraction(0), Fraction(0))
THREE_FIFTHS: Vec = (Fraction(3, 5), Fraction(0), Fraction(0))
SIX_FIFTHS: Vec = (Fraction(6, 5), Fraction(0), Fraction(0))

RZ: Mat3 = ((0, -1, 0), (1, 0, 0), (0, 0, 1))
RX: Mat3 = ((1, 0, 0), (0, 0, -1), (0, 1, 0))
I3: Mat3 = ((1, 0, 0), (0, 1, 0), (0, 0, 1))

CANONICAL_CLAIM_BLOCK = (
    "group_order: 24",
    "representation_dimension: 3",
    "irreducible_over: Q",
    "fixed_space_dimension: 0",
    "commutant_dimension: 1",
    "pauli_map_scalar_field: Q",
    "density_domain: x^2 + y^2 + z^2 <= 1",
    "unique_fixed_density: I/2",
)


def mat_mul(left: Mat3, right: Mat3) -> Mat3:
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(3)) for j in range(3))
        for i in range(3)
    )  # type: ignore[return-value]


def mat_vec(matrix: Mat3, vector: Vec) -> Vec:
    return tuple(
        sum(Fraction(matrix[i][j]) * vector[j] for j in range(3))
        for i in range(3)
    )  # type: ignore[return-value]


def det3(matrix: Mat3) -> int:
    a, b, c = matrix
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )


def is_signed_permutation(matrix: Mat3) -> bool:
    rows = all(sorted(abs(entry) for entry in row) == [0, 0, 1] for row in matrix)
    cols = all(
        sorted(abs(matrix[i][j]) for i in range(3)) == [0, 0, 1]
        for j in range(3)
    )
    return rows and cols


def generate_group() -> tuple[Mat3, ...]:
    seen: dict[Mat3, None] = {I3: None}
    queue = [I3]
    while queue:
        current = queue.pop()
        for generator in (RZ, RX):
            candidate = mat_mul(current, generator)
            if candidate not in seen:
                seen[candidate] = None
                queue.append(candidate)
    return tuple(seen)


def enumerate_proper_signed_permutations() -> tuple[Mat3, ...]:
    result: list[Mat3] = []
    for permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            matrix = tuple(
                tuple(signs[i] if j == permutation[i] else 0 for j in range(3))
                for i in range(3)
            )
            typed = matrix  # help the type checker retain the fixed 3 x 3 shape
            if det3(typed) == 1:  # type: ignore[arg-type]
                result.append(typed)  # type: ignore[arg-type]
    return tuple(result)


def matrix_rank(rows: list[list[Fraction]]) -> int:
    if not rows:
        return 0
    work = [row[:] for row in rows]
    width = len(work[0])
    rank = 0
    for column in range(width):
        pivot = next(
            (index for index in range(rank, len(work)) if work[index][column]),
            None,
        )
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        scale = work[rank][column]
        work[rank] = [entry / scale for entry in work[rank]]
        for index, row in enumerate(work):
            if index == rank or row[column] == 0:
                continue
            factor = row[column]
            work[index] = [
                row[j] - factor * work[rank][j] for j in range(width)
            ]
        rank += 1
        if rank == len(work):
            break
    return rank


def fixed_equation_rank() -> int:
    rows = [
        [Fraction(generator[i][j] - I3[i][j]) for j in range(3)]
        for generator in (RZ, RX)
        for i in range(3)
    ]
    return matrix_rank(rows)


def commutant_dimension() -> int:
    equations: list[list[Fraction]] = []
    for generator in (RZ, RX):
        for i in range(3):
            for j in range(3):
                row = [Fraction(0)] * 9
                for k in range(3):
                    row[i * 3 + k] += Fraction(generator[k][j])
                    row[k * 3 + j] -= Fraction(generator[i][k])
                equations.append(row)
    return 9 - matrix_rank(equations)


def trace3(matrix: Mat3) -> int:
    return sum(matrix[i][i] for i in range(3))


def character_inner_product(group: tuple[Mat3, ...]) -> Fraction:
    return Fraction(sum(trace3(matrix) ** 2 for matrix in group), len(group))


def reynolds_numerator(group: tuple[Mat3, ...]) -> Mat3:
    return tuple(
        tuple(sum(matrix[i][j] for matrix in group) for j in range(3))
        for i in range(3)
    )  # type: ignore[return-value]


def norm_squared(vector: Vec) -> Fraction:
    return sum((entry * entry for entry in vector), Fraction(0))


def c_add(left: C, right: C) -> C:
    return (left[0] + right[0], left[1] + right[1])


def c_sub(left: C, right: C) -> C:
    return (left[0] - right[0], left[1] - right[1])


def c_mul(left: C, right: C) -> C:
    return (
        left[0] * right[0] - left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def c_conjugate(value: C) -> C:
    return (value[0], -value[1])


def c_scale(scalar: Fraction, value: C) -> C:
    return (scalar * value[0], scalar * value[1])


def h_add(left: HMat, right: HMat) -> HMat:
    return tuple(
        tuple(c_add(left[i][j], right[i][j]) for j in range(2))
        for i in range(2)
    )  # type: ignore[return-value]


def h_scale(scalar: Fraction, matrix: HMat) -> HMat:
    return tuple(
        tuple(c_scale(scalar, matrix[i][j]) for j in range(2))
        for i in range(2)
    )  # type: ignore[return-value]


def h_complex_scale(scalar: C, matrix: HMat) -> HMat:
    return tuple(
        tuple(c_mul(scalar, matrix[i][j]) for j in range(2))
        for i in range(2)
    )  # type: ignore[return-value]


def h_mul(left: HMat, right: HMat) -> HMat:
    return tuple(
        tuple(
            c_add(c_mul(left[i][0], right[0][j]), c_mul(left[i][1], right[1][j]))
            for j in range(2)
        )
        for i in range(2)
    )  # type: ignore[return-value]


def h_dagger(matrix: HMat) -> HMat:
    return tuple(
        tuple(c_conjugate(matrix[j][i]) for j in range(2)) for i in range(2)
    )  # type: ignore[return-value]


def identity2() -> HMat:
    zero: C = (Fraction(0), Fraction(0))
    one: C = (Fraction(1), Fraction(0))
    return ((one, zero), (zero, one))


def zero2() -> HMat:
    zero: C = (Fraction(0), Fraction(0))
    return ((zero, zero), (zero, zero))


def pauli_dot(vector: Vec) -> HMat:
    x, y, z = vector
    return (
        ((z, Fraction(0)), (x, -y)),
        ((x, y), (-z, Fraction(0))),
    )


def density(vector: Vec) -> HMat:
    return h_scale(Fraction(1, 2), h_add(identity2(), pauli_dot(vector)))


def h_trace(matrix: HMat) -> C:
    return c_add(matrix[0][0], matrix[1][1])


def h_determinant(matrix: HMat) -> C:
    return c_sub(c_mul(matrix[0][0], matrix[1][1]), c_mul(matrix[0][1], matrix[1][0]))


def is_hermitian(matrix: HMat) -> bool:
    return h_dagger(matrix) == matrix


def is_bloch_body(vector: Vec) -> bool:
    return norm_squared(vector) <= 1


def is_density_matrix(matrix: HMat) -> bool:
    determinant = h_determinant(matrix)
    return (
        is_hermitian(matrix)
        and h_trace(matrix) == (Fraction(1), Fraction(0))
        and determinant[1] == 0
        and determinant[0] >= 0
    )


def quarter_turn_numerator(axis_pauli: HMat) -> HMat:
    return h_add(identity2(), h_complex_scale((Fraction(0), Fraction(-1)), axis_pauli))


def conjugate_quarter_turn(matrix: HMat, axis_pauli: HMat) -> HMat:
    numerator = quarter_turn_numerator(axis_pauli)
    return h_scale(
        Fraction(1, 2),
        h_mul(h_mul(numerator, matrix), h_dagger(numerator)),
    )


def section_text(document: str, heading: str) -> str:
    marker = heading + "\n"
    start = document.index(marker) + len(marker)
    next_heading = document.find("\n## ", start)
    return document[start:] if next_heading < 0 else document[start:next_heading]


def executable_claim_block(document: str) -> tuple[str, ...]:
    section = section_text(document, "## Executable claim block")
    blocks = re.findall(r"```text\n(.*?)\n```", section, flags=re.DOTALL)
    if len(blocks) != 1:
        return ()
    return tuple(blocks[0].splitlines())


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
    generated = generate_group()
    enumerated = enumerate_proper_signed_permutations()
    group_set = set(generated)

    print("external_scientific_inputs: none; all objects are declared in the source note")
    print("package_local_integrity_reads: the source note is a content-pinned runner input")
    print("proof_scope: exact finite-group, Q-linear Pauli, and rational Bloch-body algebra")

    checks.check(
        "audit-inputs",
        "the source note is the sole declared input",
        NOTE_PATH.is_file()
        and AUDIT_INPUT_PATHS
        == (
            "docs/ONLY_CUBIC_INVARIANT_BLOCH_VECTOR_IS_ZERO_BOUNDED_THEOREM_NOTE_2026-08-13.md",
        ),
    )
    checks.check(
        "group-generators",
        "the declared quarter turns have determinant +1 and order four",
        det3(RZ) == det3(RX) == 1
        and mat_mul(mat_mul(mat_mul(RZ, RZ), RZ), RZ) == I3
        and mat_mul(mat_mul(mat_mul(RX, RX), RX), RX) == I3,
    )
    checks.check(
        "group-enumeration",
        "generator closure equals the independent 24-element signed-permutation enumeration",
        len(generated) == len(group_set) == len(enumerated) == 24
        and group_set == set(enumerated),
    )
    checks.check(
        "group-closure",
        "every product stays in the determinant-+1 signed-permutation group",
        all(is_signed_permutation(matrix) and det3(matrix) == 1 for matrix in generated)
        and all(mat_mul(left, right) in group_set for left in generated for right in generated),
    )
    checks.check(
        "irreducible-character",
        "the exact character inner product is one",
        character_inner_product(generated) == 1,
    )
    checks.check(
        "irreducible-commutant",
        "the exact commutant dimension is one",
        commutant_dimension() == 1,
    )
    checks.check(
        "fixed-equations",
        "the stacked generator fixed equations have rank three",
        fixed_equation_rank() == 3,
    )
    checks.check(
        "reynolds-projector",
        "the exact Reynolds numerator is the zero matrix",
        reynolds_numerator(generated) == ((0, 0, 0), (0, 0, 0), (0, 0, 0)),
    )

    ex: Vec = (Fraction(1), Fraction(0), Fraction(0))
    ey: Vec = (Fraction(0), Fraction(1), Fraction(0))
    ez: Vec = (Fraction(0), Fraction(0), Fraction(1))
    sx, sy, sz = pauli_dot(ex), pauli_dot(ey), pauli_dot(ez)
    symbol: Vec = (Fraction(2), Fraction(-3), Fraction(5))
    other: Vec = (Fraction(-1), Fraction(4), Fraction(2))
    a, b = Fraction(3, 7), Fraction(-2, 5)
    combination = tuple(a * symbol[i] + b * other[i] for i in range(3))
    gram = tuple(
        tuple(h_trace(h_mul(left, right)) for right in (sx, sy, sz))
        for left in (sx, sy, sz)
    )
    expected_gram = tuple(
        tuple(
            (Fraction(2 if i == j else 0), Fraction(0)) for j in range(3)
        )
        for i in range(3)
    )
    checks.check(
        "pauli-q-linearity",
        "the Pauli-coordinate map is Q-linear with a nondegenerate basis Gram matrix",
        pauli_dot(combination)
        == h_add(h_scale(a, pauli_dot(symbol)), h_scale(b, pauli_dot(other)))
        and gram == expected_gram,
    )
    checks.check(
        "pauli-quarter-turn-normalization",
        "both conjugation numerators have N N-dagger = 2I",
        all(
            h_mul(quarter_turn_numerator(axis), h_dagger(quarter_turn_numerator(axis)))
            == h_scale(Fraction(2), identity2())
            for axis in (sz, sx)
        ),
    )
    checks.check(
        "pauli-quarter-turn-intertwining",
        "independent unitary conjugation implements both declared vector rotations",
        conjugate_quarter_turn(pauli_dot(symbol), sz)
        == pauli_dot(mat_vec(RZ, symbol))
        and conjugate_quarter_turn(pauli_dot(symbol), sx)
        == pauli_dot(mat_vec(RX, symbol)),
    )
    checks.check(
        "pauli-fixed-space",
        "zero is the unique coordinate compatible with the rank-three fixed equations",
        pauli_dot(ZERO) == zero2()
        and all(mat_vec(matrix, ZERO) == ZERO for matrix in generated)
        and fixed_equation_rank() == 3,
    )

    density_symbol = density(symbol)
    checks.check(
        "density-exact-formula",
        "rho(r) is Hermitian, trace one, and has the exact Bloch determinant",
        is_hermitian(density_symbol)
        and h_trace(density_symbol) == (Fraction(1), Fraction(0))
        and h_determinant(density_symbol)
        == ((Fraction(1) - norm_squared(symbol)) / 4, Fraction(0)),
    )
    checks.check(
        "density-determinant-scale",
        "det rho(r) equals (1-|r|^2)/4 on independent rational samples",
        all(
            h_determinant(density(vector))
            == ((Fraction(1) - norm_squared(vector)) / 4, Fraction(0))
            for vector in (ZERO, UNIT_X, THREE_FIFTHS, SIX_FIFTHS, symbol)
        ),
    )
    unit_density = density(UNIT_X)
    checks.check(
        "density-body-boundary",
        "the norm-one control is in the Bloch body and is a determinant-zero rank-one density",
        norm_squared(UNIT_X) == 1
        and is_bloch_body(UNIT_X)
        and is_density_matrix(unit_density)
        and h_determinant(unit_density) == (Fraction(0), Fraction(0))
        and unit_density != zero2()
        and h_mul(unit_density, unit_density) == unit_density,
    )
    checks.check(
        "density-body-interior",
        "the 3/5 control is inside the Bloch body and has determinant 4/25",
        is_bloch_body(THREE_FIFTHS)
        and is_density_matrix(density(THREE_FIFTHS))
        and h_determinant(density(THREE_FIFTHS)) == (Fraction(4, 25), Fraction(0)),
    )
    checks.check(
        "density-body-exterior",
        "the 6/5 mutation is outside the Bloch body and fails positive semidefiniteness",
        not is_bloch_body(SIX_FIFTHS)
        and not is_density_matrix(density(SIX_FIFTHS))
        and h_determinant(density(SIX_FIFTHS)) == (Fraction(-11, 100), Fraction(0)),
    )
    checks.check(
        "density-group-action",
        "all group elements preserve the exact Bloch norm",
        all(norm_squared(mat_vec(matrix, symbol)) == norm_squared(symbol) for matrix in generated),
    )
    checks.check(
        "density-unique-fixed",
        "the rank-three fixed equations select rho(0)=I/2",
        fixed_equation_rank() == 3
        and density(ZERO) == h_scale(Fraction(1, 2), identity2())
        and is_density_matrix(density(ZERO)),
    )

    theorem1 = section_text(note, "## Theorem 1 — the generated representation is irreducible")
    theorem2 = section_text(note, "## Theorem 2 — the fixed space is zero")
    theorem3 = section_text(note, "## Theorem 3 — the Pauli-coordinate fixed space is zero")
    theorem4 = section_text(note, "## Theorem 4 — the rational Bloch density body")
    checks.check(
        "section-bound-conclusions",
        "each displayed theorem section contains its exact canonical conclusion",
        "**Conclusion.** `G` has order `24`" in theorem1
        and "acts irreducibly on `Q^3`." in theorem1
        and "**Conclusion.** `Fix_G(Q^3) = {0}`." in theorem2
        and "**Conclusion.** The `G`-fixed subspace of the rational-Pauli traceless\nHermitian space is `{0}`." in theorem3
        and "**Conclusion.** `rho(r)` is a density matrix exactly when\n`r in B_Q`, and the unique `G`-fixed density in this body is `rho(0)=I/2`." in theorem4,
    )
    checks.check(
        "canonical-claim-block",
        "the executable claim block exactly matches all computed theorem outputs",
        executable_claim_block(note) == CANONICAL_CLAIM_BLOCK
        and len(generated) == 24
        and character_inner_product(generated) == 1
        and fixed_equation_rank() == 3
        and commutant_dimension() == 1,
    )
    imports = section_text(note, "## Imports and authority")
    checks.check(
        "self-contained-authority",
        "the note declares no upstream dependency or physical bridge",
        "upstream_dependencies: []" in note
        and "Imported scientific authority: none." in imports
        and "MINIMAL_AXIOMS" not in note
        and "Admissibility" not in note,
    )
    checks.check(
        "claim-surface-trim",
        "the superseded physical and negative-evidence sections are absent",
        "## Theorem 5" not in note
        and "### N5" not in note
        and "6-tuple" not in note
        and "Born" not in note
        and "vacuum" not in note,
    )
    proof_boundary = section_text(note, "## Proof boundary")
    review_record = section_text(note, "## Review record")
    checks.check(
        "proof-boundary",
        "the proof boundary states covered edge cases, excluded domains, and missing-lemma status",
        "`r=0`" in proof_boundary
        and "`0 < ||r||^2 < 1`" in proof_boundary
        and "`||r||^2 = 1`" in proof_boundary
        and "`||r||^2 > 1`" in proof_boundary
        and "outside `Q^3`" in proof_boundary
        and "physical\ncovariance interpretation" in proof_boundary
        and "No lemma in `P0`--`P6`\nremains open" in proof_boundary,
    )
    checks.check(
        "review-record",
        "the narrowing record distinguishes withdrawal from refutation and fixes the preserved scope",
        "withdraws rather\nthan refutes" in review_record
        and "minimal-axiom import" in review_record
        and "physical covariance corollary" in review_record
        and "six-component neighborhood tuple" in review_record
        and "scope ends at the self-contained finite-group" in review_record
        and "independent audit remains a separate lane" in review_record,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
