#!/usr/bin/env python3
"""Exact signed-axis projector decomposition and integer-monomial theorem.

The historical filename is preserved for claim-graph continuity.  The theorem
is finite rational algebra on an explicitly defined six-element carrier.  It
does not select a physical exponent, normalization, source, readout, or
endpoint.

Modes:
  default                              exact construction and proof checks
  --independent                        independently coded exact oracles
  --hostile                            reject every hostile mutation
  --mode intentional-failure --fixture NAME|all
                                       install mutations and exit nonzero
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path
import re
import sys
from typing import Callable, TypeAlias


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs/QUARK_ROUTE2_DOUBLE_LOCAL_PROJECTOR_NORMALIZATION_BRIDGE_CONDITIONAL_NOTE_2026-06-21.md"

IntVector3: TypeAlias = tuple[int, int, int]
IntMatrix3: TypeAlias = tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]
QVector: TypeAlias = tuple[Fraction, ...]
QMatrix: TypeAlias = tuple[tuple[Fraction, ...], ...]
ExponentCertificate: TypeAlias = tuple[int, int, int, int]

PASS = 0
FAIL = 0

ARMS: tuple[IntVector3, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
ARM_INDEX = {arm: index for index, arm in enumerate(ARMS)}


class FractionSubclass(Fraction):
    """Hostile fixture: exact-looking subclasses are outside the contract."""


class IntSubclass(int):
    """Hostile fixture: integer subclasses are outside the contract."""


def report(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" :: {detail}" if detail else ""
    print(f"{tag} {label}{suffix}")


def section(title: str) -> None:
    print(f"\n{'-' * 78}\n{title}\n{'-' * 78}")


def exact_fraction(value: object, context: str, *, positive: bool = False) -> Fraction:
    if type(value) is not Fraction:
        raise TypeError(f"{context} must have exact runtime type Fraction")
    if positive and value <= 0:
        raise ValueError(f"{context} must be positive")
    return value


def exact_integer(value: object, context: str) -> int:
    if type(value) is not int:
        raise TypeError(f"{context} must have exact runtime type int")
    return value


def strict_qmatrix(value: object, dimension: int = 6) -> QMatrix:
    if type(value) is not tuple or len(value) != dimension:
        raise TypeError(f"matrix must be a {dimension}-row tuple")
    rows: list[tuple[Fraction, ...]] = []
    for row in value:
        if type(row) is not tuple or len(row) != dimension:
            raise TypeError(f"matrix rows must be {dimension}-entry tuples")
        checked = tuple(exact_fraction(entry, "matrix entry") for entry in row)
        rows.append(checked)
    return tuple(rows)


def strict_qvector(value: object, dimension: int = 6) -> QVector:
    if type(value) is not tuple or len(value) != dimension:
        raise TypeError(f"vector must be a {dimension}-entry tuple")
    return tuple(exact_fraction(entry, "vector entry") for entry in value)


def qzero(dimension: int) -> QMatrix:
    return tuple(
        tuple(Fraction(0) for _ in range(dimension)) for _ in range(dimension)
    )


def qidentity(dimension: int) -> QMatrix:
    return tuple(
        tuple(Fraction(int(row == column)) for column in range(dimension))
        for row in range(dimension)
    )


def qadd(left: QMatrix, right: QMatrix) -> QMatrix:
    left = strict_qmatrix(left, len(left))
    right = strict_qmatrix(right, len(left))
    return tuple(
        tuple(left[i][j] + right[i][j] for j in range(len(left)))
        for i in range(len(left))
    )


def qsub(left: QMatrix, right: QMatrix) -> QMatrix:
    left = strict_qmatrix(left, len(left))
    right = strict_qmatrix(right, len(left))
    return tuple(
        tuple(left[i][j] - right[i][j] for j in range(len(left)))
        for i in range(len(left))
    )


def qmul(left: QMatrix, right: QMatrix) -> QMatrix:
    left = strict_qmatrix(left, len(left))
    right = strict_qmatrix(right, len(left))
    dimension = len(left)
    return tuple(
        tuple(
            sum((left[i][k] * right[k][j] for k in range(dimension)), Fraction(0))
            for j in range(dimension)
        )
        for i in range(dimension)
    )


def qtranspose(matrix: QMatrix) -> QMatrix:
    matrix = strict_qmatrix(matrix, len(matrix))
    return tuple(tuple(matrix[j][i] for j in range(len(matrix))) for i in range(len(matrix)))


def qmatvec(matrix: QMatrix, vector: QVector) -> QVector:
    matrix = strict_qmatrix(matrix, len(matrix))
    vector = strict_qvector(vector, len(matrix))
    return tuple(
        sum((matrix[i][j] * vector[j] for j in range(len(matrix))), Fraction(0))
        for i in range(len(matrix))
    )


def qrank(matrix: QMatrix) -> int:
    checked = strict_qmatrix(matrix, len(matrix))
    work = [list(row) for row in checked]
    rows = len(work)
    columns = len(work[0])
    pivot_row = 0
    for column in range(columns):
        pivot = next((row for row in range(pivot_row, rows) if work[row][column] != 0), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        scale = work[pivot_row][column]
        work[pivot_row] = [entry / scale for entry in work[pivot_row]]
        for row in range(rows):
            if row == pivot_row:
                continue
            factor = work[row][column]
            if factor:
                work[row] = [
                    work[row][j] - factor * work[pivot_row][j] for j in range(columns)
                ]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def qtrace(matrix: QMatrix) -> Fraction:
    matrix = strict_qmatrix(matrix, len(matrix))
    return sum((matrix[i][i] for i in range(len(matrix))), Fraction(0))


def replace_entry(matrix: QMatrix, row: int, column: int, value: Fraction) -> QMatrix:
    matrix = strict_qmatrix(matrix, len(matrix))
    exact_fraction(value, "replacement")
    return tuple(
        tuple(value if (i, j) == (row, column) else matrix[i][j] for j in range(len(matrix)))
        for i in range(len(matrix))
    )


def int3_identity() -> IntMatrix3:
    return ((1, 0, 0), (0, 1, 0), (0, 0, 1))


def strict_int3_matrix(value: object) -> IntMatrix3:
    if type(value) is not tuple or len(value) != 3:
        raise TypeError("group matrix must be a three-row tuple")
    rows: list[tuple[int, int, int]] = []
    for row in value:
        if type(row) is not tuple or len(row) != 3:
            raise TypeError("group matrix rows must be three-entry tuples")
        checked = tuple(exact_integer(entry, "group matrix entry") for entry in row)
        rows.append(checked)  # type: ignore[arg-type]
    return tuple(rows)  # type: ignore[return-value]


def int3_mul(left: IntMatrix3, right: IntMatrix3) -> IntMatrix3:
    left = strict_int3_matrix(left)
    right = strict_int3_matrix(right)
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(3)) for j in range(3))
        for i in range(3)
    )  # type: ignore[return-value]


def int3_transpose(matrix: IntMatrix3) -> IntMatrix3:
    matrix = strict_int3_matrix(matrix)
    return tuple(tuple(matrix[j][i] for j in range(3)) for i in range(3))  # type: ignore[return-value]


def int3_det(matrix: IntMatrix3) -> int:
    m = strict_int3_matrix(matrix)
    return (
        m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
        - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
        + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
    )


def int3_matvec(matrix: IntMatrix3, vector: IntVector3) -> IntVector3:
    matrix = strict_int3_matrix(matrix)
    if type(vector) is not tuple or len(vector) != 3 or any(type(x) is not int for x in vector):
        raise TypeError("axis vector must be a strict three-integer tuple")
    return tuple(sum(matrix[i][j] * vector[j] for j in range(3)) for i in range(3))  # type: ignore[return-value]


def signed_axis_group() -> tuple[IntMatrix3, ...]:
    matrices: list[IntMatrix3] = []
    for permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            rows: list[tuple[int, int, int]] = []
            for row in range(3):
                rows.append(
                    tuple(signs[row] if column == permutation[row] else 0 for column in range(3))
                )
            matrices.append(tuple(rows))  # type: ignore[arg-type]
    return tuple(matrices)


def is_signed_permutation_matrix(matrix: IntMatrix3) -> bool:
    try:
        matrix = strict_int3_matrix(matrix)
    except (TypeError, ValueError):
        return False
    if any(entry not in (-1, 0, 1) for row in matrix for entry in row):
        return False
    row_counts = [sum(entry != 0 for entry in row) for row in matrix]
    column_counts = [sum(matrix[row][column] != 0 for row in range(3)) for column in range(3)]
    return row_counts == [1, 1, 1] and column_counts == [1, 1, 1]


def group_contract(group: object) -> bool:
    try:
        if type(group) is not tuple or len(group) != 48:
            return False
        checked = tuple(strict_int3_matrix(element) for element in group)
    except (TypeError, ValueError):
        return False
    elements = set(checked)
    if len(elements) != 48 or any(not is_signed_permutation_matrix(element) for element in checked):
        return False
    if int3_identity() not in elements:
        return False
    if sum(int3_det(element) == 1 for element in checked) != 24:
        return False
    if sum(int3_det(element) == -1 for element in checked) != 24:
        return False
    for left in checked:
        if int3_transpose(left) not in elements or int3_mul(left, int3_transpose(left)) != int3_identity():
            return False
        images = tuple(int3_matvec(left, arm) for arm in ARMS)
        if set(images) != set(ARMS) or len(set(images)) != 6:
            return False
        for right in checked:
            if int3_mul(left, right) not in elements:
                return False
    return True


def arm_permutation(matrix: IntMatrix3) -> tuple[int, ...]:
    matrix = strict_int3_matrix(matrix)
    images: list[int] = []
    for arm in ARMS:
        image = int3_matvec(matrix, arm)
        if image not in ARM_INDEX:
            raise ValueError("matrix does not preserve the signed-axis carrier")
        images.append(ARM_INDEX[image])
    if len(set(images)) != 6:
        raise ValueError("axis action is not bijective")
    return tuple(images)


def permutation_representation(matrix: IntMatrix3) -> QMatrix:
    permutation = arm_permutation(matrix)
    return tuple(
        tuple(Fraction(int(row == permutation[column])) for column in range(6))
        for row in range(6)
    )


def representation_homomorphism(group: tuple[IntMatrix3, ...]) -> bool:
    if not group_contract(group):
        return False
    representations = {element: permutation_representation(element) for element in group}
    return all(
        representations[int3_mul(left, right)] == qmul(representations[left], representations[right])
        for left in group
        for right in group
    )


def direct_projectors() -> tuple[QMatrix, QMatrix, QMatrix, QMatrix]:
    identity = qidentity(6)
    constant = tuple(tuple(Fraction(1, 6) for _ in range(6)) for _ in range(6))
    pair_even = tuple(
        tuple(Fraction(1, 2) if row // 2 == column // 2 else Fraction(0) for column in range(6))
        for row in range(6)
    )
    even_zero_sum = qsub(pair_even, constant)
    pair_odd = qsub(identity, pair_even)
    return constant, even_zero_sum, pair_odd, pair_even


def qvector_from_ints(entries: tuple[int, ...]) -> QVector:
    if type(entries) is not tuple or len(entries) != 6 or any(type(x) is not int for x in entries):
        raise TypeError("basis vector must be a strict six-integer tuple")
    return tuple(Fraction(entry) for entry in entries)


A1_BASIS = (qvector_from_ints((1, 1, 1, 1, 1, 1)),)
E_BASIS = (
    qvector_from_ints((1, 1, -1, -1, 0, 0)),
    qvector_from_ints((1, 1, 1, 1, -2, -2)),
)
T1_BASIS = (
    qvector_from_ints((1, -1, 0, 0, 0, 0)),
    qvector_from_ints((0, 0, 1, -1, 0, 0)),
    qvector_from_ints((0, 0, 0, 0, 1, -1)),
)


def basis_matrix_rank(bases: tuple[tuple[QVector, ...], ...]) -> int:
    vectors = tuple(vector for basis in bases for vector in basis)
    matrix = tuple(tuple(vectors[column][row] for column in range(6)) for row in range(6))
    return qrank(matrix)


def projector_action_contract(projectors: tuple[QMatrix, QMatrix, QMatrix]) -> bool:
    if type(projectors) is not tuple or len(projectors) != 3:
        return False
    bases = (A1_BASIS, E_BASIS, T1_BASIS)
    zero = tuple(Fraction(0) for _ in range(6))
    for projector_index, projector in enumerate(projectors):
        for basis_index, basis in enumerate(bases):
            for vector in basis:
                expected = vector if projector_index == basis_index else zero
                if qmatvec(projector, vector) != expected:
                    return False
    return basis_matrix_rank(bases) == 6


def projector_decomposition_valid(
    p_a1: object, p_e: object, p_t1: object, group: object
) -> bool:
    try:
        p_a1 = strict_qmatrix(p_a1)
        p_e = strict_qmatrix(p_e)
        p_t1 = strict_qmatrix(p_t1)
        if not group_contract(group):
            return False
        checked_group = tuple(strict_int3_matrix(element) for element in group)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return False
    identity = qidentity(6)
    zero = qzero(6)
    projectors = (p_a1, p_e, p_t1)
    expected_ranks = (1, 2, 3)
    expected_diagonals = (Fraction(1, 6), Fraction(1, 3), Fraction(1, 2))
    if qadd(qadd(p_a1, p_e), p_t1) != identity:
        return False
    for index, projector in enumerate(projectors):
        if qtranspose(projector) != projector or qmul(projector, projector) != projector:
            return False
        if qrank(projector) != expected_ranks[index] or qtrace(projector) != expected_ranks[index]:
            return False
        if tuple(projector[i][i] for i in range(6)) != (expected_diagonals[index],) * 6:
            return False
        for representation in map(permutation_representation, checked_group):
            if qmul(representation, projector) != qmul(projector, representation):
                return False
    if any(qmul(projectors[i], projectors[j]) != zero for i in range(3) for j in range(3) if i != j):
        return False
    return projector_action_contract(projectors)


def dot(left: QVector, right: QVector) -> Fraction:
    left = strict_qvector(left)
    right = strict_qvector(right)
    return sum((a * b for a, b in zip(left, right)), Fraction(0))


def independent_basis_projector(basis: tuple[QVector, ...]) -> QMatrix:
    if type(basis) is not tuple or not basis:
        raise TypeError("oracle basis must be a nonempty tuple")
    checked = tuple(strict_qvector(vector) for vector in basis)
    if any(dot(left, right) != 0 for i, left in enumerate(checked) for right in checked[i + 1 :]):
        raise ValueError("oracle basis must be orthogonal")
    if any(dot(vector, vector) == 0 for vector in checked):
        raise ValueError("oracle basis contains zero")
    return tuple(
        tuple(
            sum(
                (vector[row] * vector[column] / dot(vector, vector) for vector in checked),
                Fraction(0),
            )
            for column in range(6)
        )
        for row in range(6)
    )


def independent_axis_permutations() -> tuple[tuple[int, ...], ...]:
    actions: list[tuple[int, ...]] = []
    for pair_permutation in permutations(range(3)):
        for flips in product((0, 1), repeat=3):
            action: list[int] = []
            for source in range(6):
                source_pair, source_sign = divmod(source, 2)
                destination_pair = pair_permutation[source_pair]
                destination_sign = source_sign ^ flips[source_pair]
                action.append(2 * destination_pair + destination_sign)
            actions.append(tuple(action))
    return tuple(actions)


def monomial_lambda(u: object, v: object, exponent: object) -> Fraction:
    u = exact_fraction(u, "u", positive=True)
    v = exact_fraction(v, "v", positive=True)
    exponent = exact_integer(exponent, "exponent")
    return (u / v) ** exponent


def independent_monomial_lambda(u: object, v: object, exponent: object) -> Fraction:
    if type(u) is not Fraction or type(v) is not Fraction:
        raise TypeError("oracle u and v must be strict Fractions")
    if u <= 0 or v <= 0:
        raise ValueError("oracle u and v must be positive")
    if type(exponent) is not int:
        raise TypeError("oracle exponent must be a strict int")
    numerator = u.numerator * v.denominator
    denominator = u.denominator * v.numerator
    power = exponent
    if power < 0:
        numerator, denominator = denominator, numerator
        power = -power
    result_numerator = 1
    result_denominator = 1
    for _ in range(power):
        result_numerator *= numerator
        result_denominator *= denominator
    return Fraction(result_numerator, result_denominator)


def is_prime(value: object) -> bool:
    try:
        value = exact_integer(value, "prime")
    except TypeError:
        return False
    if value < 2:
        return False
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 1
    return True


def integer_valuation(value: int, prime: int) -> int:
    value = exact_integer(value, "valuation integer")
    prime = exact_integer(prime, "valuation prime")
    if value <= 0 or not is_prime(prime):
        raise ValueError("valuation requires a positive integer and a prime")
    order = 0
    while value % prime == 0:
        value //= prime
        order += 1
    return order


def rational_valuation(value: object, prime: object) -> int:
    value = exact_fraction(value, "valuation rational", positive=True)
    prime = exact_integer(prime, "valuation prime")
    if not is_prime(prime):
        raise ValueError("valuation base must be prime")
    return integer_valuation(value.numerator, prime) - integer_valuation(value.denominator, prime)


def make_exponent_certificate(base: object, target: object, prime: object) -> ExponentCertificate:
    base = exact_fraction(base, "certificate base", positive=True)
    target = exact_fraction(target, "certificate target", positive=True)
    prime = exact_integer(prime, "certificate prime")
    base_order = rational_valuation(base, prime)
    target_order = rational_valuation(target, prime)
    if base_order == 0:
        raise ValueError("chosen valuation cannot certify exponent uniqueness")
    if target_order % base_order != 0:
        raise ValueError("target valuation is incompatible with an integer exponent")
    candidate = target_order // base_order
    if base**candidate != target:
        raise ValueError("valuation candidate does not satisfy the exact equation")
    return prime, base_order, target_order, candidate


def verify_exponent_certificate(
    base: object, target: object, certificate: object
) -> bool:
    try:
        base = exact_fraction(base, "verified base", positive=True)
        target = exact_fraction(target, "verified target", positive=True)
        if type(certificate) is not tuple or len(certificate) != 4:
            return False
        prime, base_order, target_order, candidate = (
            exact_integer(entry, "certificate entry") for entry in certificate
        )
        expected = make_exponent_certificate(base, target, prime)
    except (TypeError, ValueError):
        return False
    return certificate == expected and base_order * candidate == target_order and base**candidate == target


def certified_integer_equivalence(
    base: object, target: object, exponent: object, certificate: object
) -> bool:
    base = exact_fraction(base, "equivalence base", positive=True)
    target = exact_fraction(target, "equivalence target", positive=True)
    exponent = exact_integer(exponent, "equivalence exponent")
    if not verify_exponent_certificate(base, target, certificate):
        raise ValueError("invalid global uniqueness certificate")
    prime, base_order, target_order, candidate = certificate  # type: ignore[misc]
    equality = base**exponent == target
    if equality and exponent * base_order != target_order:
        return False
    return equality == (exponent == candidate)


def affine_endpoint(lambda_value: object, q: object, d: object) -> tuple[Fraction, Fraction]:
    lambda_value = exact_fraction(lambda_value, "lambda")
    q = exact_fraction(q, "q")
    d = exact_fraction(d, "d")
    q_prime = lambda_value * q
    rho = d * (q_prime - 1)
    return q_prime, rho


def verify_affine_endpoint(
    lambda_value: object, q: object, d: object, candidate: object
) -> bool:
    try:
        expected = affine_endpoint(lambda_value, q, d)
        if type(candidate) is not tuple or len(candidate) != 2:
            return False
        checked = tuple(exact_fraction(entry, "endpoint candidate") for entry in candidate)
    except (TypeError, ValueError):
        return False
    return checked == expected


def independent_affine_endpoint(
    lambda_value: object, q: object, d: object
) -> tuple[Fraction, Fraction]:
    if any(type(value) is not Fraction for value in (lambda_value, q, d)):
        raise TypeError("oracle affine inputs must be strict Fractions")
    product_numerator = lambda_value.numerator * q.numerator
    product_denominator = lambda_value.denominator * q.denominator
    q_prime = Fraction(product_numerator, product_denominator)
    difference = Fraction(q_prime.numerator - q_prime.denominator, q_prime.denominator)
    rho = Fraction(d.numerator * difference.numerator, d.denominator * difference.denominator)
    return q_prime, rho


FORBIDDEN_AFFIRMATIVE_SOURCE_PHRASES = (
    "the theorem selects the physical exponent",
    "the theorem supplies the physical normalization",
    "the theorem derives the physical source",
    "the theorem predicts the physical endpoint",
)


def source_boundary_clean_text(text: object) -> bool:
    if type(text) is not str:
        raise TypeError("source text must be a strict string")
    lowered = text.lower()
    return not any(phrase in lowered for phrase in FORBIDDEN_AFFIRMATIVE_SOURCE_PHRASES)


def source_scope_checks() -> None:
    section("Source and implementation boundary")
    note_text = NOTE.read_text()
    normalized_note = " ".join(note_text.split())
    runner_text = Path(__file__).read_text()
    report(
        "source note declares a dependency-free positive theorem",
        "**Claim type:** positive_theorem" in note_text
        and "**Dependencies:** none." in note_text,
    )
    report(
        "source note denies exponent, normalization, source, and endpoint selection",
        all(
            marker in normalized_note
            for marker in (
                "does not select an exponent",
                "does not select a normalization",
                "does not identify a physical source or readout",
                "does not predict a physical endpoint",
            )
        )
        and source_boundary_clean_text(note_text),
    )
    report(
        "implementation uses no numerical-array or float-recovery path",
        re.search(r"^\s*(?:from|import)\s+numpy\b", runner_text, re.MULTILINE) is None
        and ("limit_" + "denominator") not in runner_text
        and ("d" + "type=float") not in runner_text,
    )
    report(
        "formal APIs expose no physical selection inputs",
        not call_succeeds(
            lambda: monomial_lambda(
                Fraction(1, 3),
                Fraction(1, 2),
                -2,
                physical_source="selected",  # type: ignore[call-arg]
            )
        )
        and not call_succeeds(
            lambda: direct_projectors(
                physical_normalization="selected"  # type: ignore[call-arg]
            )
        ),
    )


def normal_checks() -> None:
    group = signed_axis_group()
    p_a1, p_e, p_t1, pair_even = direct_projectors()

    section("Exact signed-axis group and representation")
    report(
        "the full signed-axis group has 48 unique elements, closure, and 24+24 determinant split",
        group_contract(group),
    )
    report(
        "the induced six-arm permutation matrices form an exact representation",
        representation_homomorphism(group),
    )
    report(
        "the antipodal-pair action is transitive on all six arms",
        {arm_permutation(element)[0] for element in group} == set(range(6)),
    )

    section("Exact orthogonal projector decomposition")
    report(
        "A1, E, and T1 are mutually orthogonal projectors summing to identity",
        projector_decomposition_valid(p_a1, p_e, p_t1, group),
    )
    report(
        "projector ranks and traces are exactly 1, 2, and 3",
        tuple(qrank(projector) for projector in (p_a1, p_e, p_t1)) == (1, 2, 3)
        and tuple(qtrace(projector) for projector in (p_a1, p_e, p_t1))
        == (Fraction(1), Fraction(2), Fraction(3)),
    )
    report(
        "all diagonal weights are exactly 1/6, 1/3, and 1/2",
        tuple(tuple(projector[i][i] for i in range(6)) for projector in (p_a1, p_e, p_t1))
        == (
            (Fraction(1, 6),) * 6,
            (Fraction(1, 3),) * 6,
            (Fraction(1, 2),) * 6,
        ),
    )
    report(
        "pair parity gives P_even=P_A1+P_E and P_T1=I-P_even",
        pair_even == qadd(p_a1, p_e) and p_t1 == qsub(qidentity(6), pair_even),
    )
    report(
        "the six displayed orthogonal basis vectors determine the projectors uniquely",
        projector_action_contract((p_a1, p_e, p_t1))
        and basis_matrix_rank((A1_BASIS, E_BASIS, T1_BASIS)) == 6,
    )

    section("Integer monomial and affine arithmetic")
    base = Fraction(2, 3)
    target = Fraction(9, 4)
    certificate_two = make_exponent_certificate(base, target, 2)
    certificate_three = make_exponent_certificate(base, target, 3)
    report(
        "for u=1/3 and v=1/2, lambda_p=(u/v)^p is exact for negative powers",
        monomial_lambda(Fraction(1, 3), Fraction(1, 2), -2) == target,
    )
    report(
        "the 2-adic certificate proves lambda_p=9/4 iff p=-2 over every integer",
        certificate_two == (2, 1, -2, -2)
        and verify_exponent_certificate(base, target, certificate_two)
        and all(
            certified_integer_equivalence(base, target, exponent, certificate_two)
            for exponent in (-10**6, -3, -2, -1, 0, 1, 10**6)
        ),
    )
    report(
        "the independent 3-adic certificate gives the same unique exponent",
        certificate_three == (3, -1, 2, -2)
        and verify_exponent_certificate(base, target, certificate_three),
    )
    report(
        "the supplied affine example gives q'=15/8 and rho=21/4 exactly",
        affine_endpoint(Fraction(9, 4), Fraction(5, 6), Fraction(6))
        == (Fraction(15, 8), Fraction(21, 4)),
    )


def independent_checks() -> None:
    section("Independent exact construction and arithmetic oracles")
    group = signed_axis_group()
    direct_actions = {arm_permutation(element) for element in group}
    oracle_actions = independent_axis_permutations()
    report(
        "pair-permutation/flip enumeration independently recovers all 48 group actions",
        len(oracle_actions) == 48
        and len(set(oracle_actions)) == 48
        and set(oracle_actions) == direct_actions,
    )

    p_a1, p_e, p_t1, _ = direct_projectors()
    oracle_projectors = (
        independent_basis_projector(A1_BASIS),
        independent_basis_projector(E_BASIS),
        independent_basis_projector(T1_BASIS),
    )
    report(
        "orthogonal-basis outer products independently recover every projector entry",
        oracle_projectors == (p_a1, p_e, p_t1),
    )
    report(
        "the independent projectors pass the full group/decomposition contract",
        projector_decomposition_valid(*oracle_projectors, group),
    )

    rational_cases = (
        (Fraction(1, 3), Fraction(1, 2)),
        (Fraction(2, 5), Fraction(7, 11)),
        (Fraction(9, 4), Fraction(5, 6)),
        (Fraction(13, 7), Fraction(3, 8)),
        (Fraction(1, 97), Fraction(89, 101)),
        (Fraction(144, 35), Fraction(55, 21)),
    )
    exponents = (-17, -8, -3, -1, 0, 1, 2, 5, 13)
    monomial_agreement = all(
        monomial_lambda(u, v, exponent) == independent_monomial_lambda(u, v, exponent)
        for u, v in rational_cases
        for exponent in exponents
    )
    report(
        "independent numerator/denominator powers agree on 54 varied rational cases",
        monomial_agreement,
    )

    affine_cases = (
        (Fraction(9, 4), Fraction(5, 6), Fraction(6)),
        (Fraction(-7, 11), Fraction(13, 5), Fraction(3, 8)),
        (Fraction(0), Fraction(4, 9), Fraction(-5, 2)),
        (Fraction(17, 19), Fraction(-23, 29), Fraction(31, 37)),
        (Fraction(101, 7), Fraction(1, 103), Fraction(107, 109)),
    )
    report(
        "independent common-denominator affine arithmetic agrees on varied signed inputs",
        all(
            affine_endpoint(lambda_value, q, d)
            == independent_affine_endpoint(lambda_value, q, d)
            for lambda_value, q, d in affine_cases
        ),
    )

    base = Fraction(2, 3)
    target = Fraction(9, 4)
    cert_two = make_exponent_certificate(base, target, 2)
    cert_three = make_exponent_certificate(base, target, 3)
    report(
        "two independent prime valuations force the same global exponent without a scan",
        cert_two[-1] == cert_three[-1] == -2
        and cert_two[1] * cert_two[-1] == cert_two[2]
        and cert_three[1] * cert_three[-1] == cert_three[2]
        and independent_monomial_lambda(Fraction(1, 3), Fraction(1, 2), -2) == target,
    )


def call_succeeds(function: Callable[[], object]) -> bool:
    try:
        function()
    except (TypeError, ValueError, ZeroDivisionError):
        return False
    return True


HOSTILE_FIXTURES = (
    "projector-diagonal-perturbation",
    "non-idempotent-projector",
    "nonorthogonal-projectors",
    "wrong-projector-ranks-weights",
    "malformed-matrix-container",
    "duplicate-group-element",
    "incomplete-group",
    "bool-exponent",
    "float-exponent",
    "int-subclass-exponent",
    "float-weight",
    "fraction-subclass-weight",
    "zero-weight",
    "malformed-valuation-certificate",
    "scan-only-global-uniqueness",
    "wrong-global-exponent",
    "ambiguous-global-uniqueness",
    "wrong-affine-endpoint",
    "integer-affine-coercion",
    "physical-source-selects-exponent",
    "physical-source-selects-normalization",
    "affirmative-physical-source-mutation",
)


def hostile_mutation_acceptance(name: str) -> bool:
    group = signed_axis_group()
    p_a1, p_e, p_t1, pair_even = direct_projectors()
    base = Fraction(2, 3)
    target = Fraction(9, 4)
    certificate = make_exponent_certificate(base, target, 2)

    if name == "projector-diagonal-perturbation":
        mutant = replace_entry(p_a1, 0, 0, p_a1[0][0] + Fraction(1, 6))
        return projector_decomposition_valid(mutant, p_e, p_t1, group)
    if name == "non-idempotent-projector":
        mutant = replace_entry(p_e, 0, 1, p_e[0][1] + Fraction(1, 7))
        return projector_decomposition_valid(p_a1, mutant, p_t1, group)
    if name == "nonorthogonal-projectors":
        return projector_decomposition_valid(p_a1, p_e, qadd(p_t1, p_a1), group)
    if name == "wrong-projector-ranks-weights":
        return projector_decomposition_valid(p_a1, pair_even, p_t1, group)
    if name == "malformed-matrix-container":
        return projector_decomposition_valid([list(row) for row in p_a1], p_e, p_t1, group)
    if name == "duplicate-group-element":
        return group_contract(group[:-1] + (group[0],))
    if name == "incomplete-group":
        return group_contract(group[:-1])
    if name == "bool-exponent":
        return call_succeeds(lambda: monomial_lambda(Fraction(1, 3), Fraction(1, 2), True))
    if name == "float-exponent":
        return call_succeeds(lambda: monomial_lambda(Fraction(1, 3), Fraction(1, 2), -2.0))
    if name == "int-subclass-exponent":
        return call_succeeds(
            lambda: monomial_lambda(Fraction(1, 3), Fraction(1, 2), IntSubclass(-2))
        )
    if name == "float-weight":
        return call_succeeds(lambda: monomial_lambda(1 / 3, Fraction(1, 2), -2))
    if name == "fraction-subclass-weight":
        return call_succeeds(
            lambda: monomial_lambda(FractionSubclass(1, 3), Fraction(1, 2), -2)
        )
    if name == "zero-weight":
        return call_succeeds(lambda: monomial_lambda(Fraction(0), Fraction(1, 2), -2))
    if name == "malformed-valuation-certificate":
        return verify_exponent_certificate(base, target, [2, 1, -2, -2])
    if name == "scan-only-global-uniqueness":
        return verify_exponent_certificate(base, target, (-2, -6, 6))
    if name == "wrong-global-exponent":
        return verify_exponent_certificate(base, target, (2, 1, -2, -1))
    if name == "ambiguous-global-uniqueness":
        return call_succeeds(lambda: make_exponent_certificate(Fraction(1), Fraction(1), 2))
    if name == "wrong-affine-endpoint":
        return verify_affine_endpoint(
            Fraction(9, 4),
            Fraction(5, 6),
            Fraction(6),
            (Fraction(15, 8), Fraction(5)),
        )
    if name == "integer-affine-coercion":
        return call_succeeds(lambda: affine_endpoint(Fraction(9, 4), Fraction(5, 6), 6))
    if name == "physical-source-selects-exponent":
        return call_succeeds(
            lambda: monomial_lambda(
                Fraction(1, 3),
                Fraction(1, 2),
                -2,
                physical_source="selected",  # type: ignore[call-arg]
            )
        )
    if name == "physical-source-selects-normalization":
        return call_succeeds(
            lambda: direct_projectors(
                physical_normalization="selected"  # type: ignore[call-arg]
            )
        )
    if name == "affirmative-physical-source-mutation":
        mutant = NOTE.read_text() + "\nThe theorem derives the physical source.\n"
        return source_boundary_clean_text(mutant)
    if name not in HOSTILE_FIXTURES:
        raise ValueError(f"unknown hostile fixture: {name}")
    return verify_exponent_certificate(base, target, certificate)


def hostile_checks() -> None:
    section("Hostile mutation rejection")
    for name in HOSTILE_FIXTURES:
        report(f"hostile mutation rejected: {name}", not hostile_mutation_acceptance(name))


def intentional_failure_checks(fixture: str) -> None:
    section("Intentional hostile failure controls")
    selected = HOSTILE_FIXTURES if fixture == "all" else (fixture,)
    for name in selected:
        report(
            f"intentional false acceptance must fail: {name}",
            hostile_mutation_acceptance(name),
            "mutation did not satisfy the exact theorem contract",
        )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--mode",
        choices=("normal", "independent", "hostile", "intentional-failure"),
        default="normal",
    )
    aliases = parser.add_mutually_exclusive_group()
    aliases.add_argument("--independent", action="store_true", help="alias for --mode independent")
    aliases.add_argument("--hostile", action="store_true", help="alias for --mode hostile")
    parser.add_argument("--fixture", choices=("all",) + HOSTILE_FIXTURES, default="all")
    args = parser.parse_args()
    if args.independent:
        if args.mode != "normal":
            parser.error("--independent cannot combine with explicit non-normal --mode")
        args.mode = "independent"
    if args.hostile:
        if args.mode != "normal":
            parser.error("--hostile cannot combine with explicit non-normal --mode")
        args.mode = "hostile"
    if args.fixture != "all" and args.mode != "intentional-failure":
        parser.error("--fixture requires --mode intentional-failure")
    return args


def main() -> int:
    args = parse_args()
    print("Exact signed-axis projector decomposition and integer-monomial theorem")
    print(f"MODE={args.mode}")
    source_scope_checks()
    if args.mode == "normal":
        normal_checks()
    elif args.mode == "independent":
        independent_checks()
    elif args.mode == "hostile":
        hostile_checks()
    else:
        intentional_failure_checks(args.fixture)
    print(f"\nSUMMARY: MODE={args.mode} PASS={PASS} FAIL={FAIL}")
    print("THEOREM_SCOPE=DEFINED_SIX_ARM_PROJECTORS_INTEGER_MONOMIAL_AND_AFFINE_ARITHMETIC")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
