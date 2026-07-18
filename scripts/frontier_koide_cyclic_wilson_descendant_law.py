#!/usr/bin/env python3
"""Exact certificate for the adjacent-chain cyclic-response Riesz lemma.

The historical runner path is retained for ledger continuity. All theorem
checks use symbolic integer or rational algebra. Mutation checks exercise the
normalization, orientation, dimension, Hermiticity, linearity, response, and
cone-factor contracts.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "KOIDE_CYCLIC_WILSON_DESCENDANT_LAW_NOTE_2026-04-18.md"
KINDS = ("EXACT", "SUPPORT", "MUTATION")


class Evidence:
    def __init__(self) -> None:
        self.passes = {kind: 0 for kind in KINDS}
        self.failures = {kind: 0 for kind in KINDS}

    def check(self, kind: str, name: str, condition: object, detail: str = "") -> None:
        if kind not in KINDS:
            raise ValueError(f"unknown evidence kind: {kind}")
        status = "PASS" if condition else "FAIL"
        bucket = self.passes if condition else self.failures
        bucket[kind] += 1
        message = f"  [{status}][{kind}] {name}"
        if detail:
            message += f"  ({detail})"
        print(message)

    def failed(self) -> int:
        return sum(self.failures.values())

    def summary(self) -> str:
        fields = []
        for kind in KINDS:
            fields.append(f"{kind}={self.passes[kind]}/{self.failures[kind]}")
        fields.append(f"TOTAL_FAIL={self.failed()}")
        return " ".join(fields)


EVIDENCE = Evidence()


def matrix_unit(i: int, j: int) -> sp.Matrix:
    matrix = sp.zeros(3)
    matrix[i - 1, j - 1] = sp.Integer(1)
    return matrix


def canonical_cycle() -> sp.Matrix:
    return sp.Matrix(((0, 0, 1), (1, 0, 0), (0, 1, 0)))


def canonical_basis() -> tuple[sp.Matrix, sp.Matrix, sp.Matrix]:
    cycle = canonical_cycle()
    cycle2 = cycle**2
    return sp.eye(3), cycle + cycle2, sp.I * (cycle - cycle2)


def matrix_is_zero(matrix: sp.Matrix) -> object:
    return all(sp.simplify(entry) == 0 for entry in matrix)


def matrices_equal(left: sp.Matrix, right: sp.Matrix) -> object:
    return matrix_is_zero(left - right)


def is_hermitian(matrix: sp.Matrix) -> object:
    return matrices_equal(matrix, matrix.conjugate().T)


def real_trace_pair(left: sp.Matrix, right: sp.Matrix) -> sp.Expr:
    return sp.simplify(sp.re(sp.trace(left * right)))


def hermitian_coordinate_basis() -> tuple[sp.Matrix, ...]:
    e11, e22, e33 = matrix_unit(1, 1), matrix_unit(2, 2), matrix_unit(3, 3)

    def x(i: int, j: int) -> sp.Matrix:
        return matrix_unit(i, j) + matrix_unit(j, i)

    def y(i: int, j: int) -> sp.Matrix:
        return sp.I * (matrix_unit(j, i) - matrix_unit(i, j))

    return (
        e11,
        e22,
        e33,
        x(1, 2),
        x(1, 3),
        x(2, 3),
        y(1, 2),
        y(1, 3),
        y(2, 3),
    )


def hermitian_coordinates(matrix: sp.Matrix) -> sp.Matrix:
    basis = hermitian_coordinate_basis()
    norms = tuple(real_trace_pair(item, item) for item in basis)
    return sp.Matrix(tuple(sp.simplify(real_trace_pair(item, matrix) / norm) for item, norm in zip(basis, norms)))


def real_imag_vector(matrix: sp.Matrix) -> sp.Matrix:
    entries = []
    for entry in matrix:
        entries.extend((sp.simplify(sp.re(entry)), sp.simplify(sp.im(entry))))
    return sp.Matrix(entries)


def commutator_map(cycle: sp.Matrix) -> sp.Matrix:
    columns = [real_imag_vector(item * cycle - cycle * item) for item in hermitian_coordinate_basis()]
    return sp.Matrix.hstack(*columns)


def cyclic_projector(matrix: sp.Matrix, cycle: sp.Matrix, denominator: int) -> sp.Matrix:
    return sp.simplify(
        (matrix + cycle * matrix * cycle.inv() + cycle**2 * matrix * cycle.inv() ** 2)
        / sp.Integer(denominator)
    )


def gram_matrix(basis: tuple[sp.Matrix, ...]) -> sp.Matrix:
    return sp.Matrix(tuple(tuple(real_trace_pair(left, right) for right in basis) for left in basis))


def generic_hermitian() -> tuple[sp.Matrix, tuple[sp.Symbol, ...]]:
    names = "d0 d1 d2 x12 x13 x23 y12 y13 y23"
    variables = sp.symbols(names, real=sp.S.true)
    matrix = sum(
        (coefficient * basis for coefficient, basis in zip(variables, hermitian_coordinate_basis())),
        sp.zeros(3),
    )
    return matrix, variables


def section(title: str) -> None:
    print()
    print("=" * 92)
    print(title)
    print("=" * 92)


def exact_adjacent_chain_and_commutant() -> None:
    section("EXACT 1: adjacent-chain certificates and the full Hermitian commutant")
    units = {(i, j): matrix_unit(i, j) for i in range(1, 4) for j in range(1, 4)}
    cycle = canonical_cycle()
    cycle2 = cycle**2
    b0, b1, b2 = canonical_basis()

    EVIDENCE.check("EXACT", "E12 E23 is the long corner E13", matrices_equal(units[1, 2] * units[2, 3], units[1, 3]))
    EVIDENCE.check("EXACT", "E32 E21 is the long corner E31", matrices_equal(units[3, 2] * units[2, 1], units[3, 1]))
    diagonal_words = (
        units[1, 2] * units[2, 1],
        units[2, 1] * units[1, 2],
        units[3, 2] * units[2, 3],
    )
    EVIDENCE.check(
        "EXACT",
        "adjacent generators and words contain all three diagonal units",
        all(matrices_equal(actual, expected) for actual, expected in zip(diagonal_words, (units[1, 1], units[2, 2], units[3, 3]))),
    )
    EVIDENCE.check(
        "EXACT",
        "the displayed orientation is C=E21+E32+E13",
        matrices_equal(cycle, units[2, 1] + units[3, 2] + units[1, 2] * units[2, 3]),
    )
    EVIDENCE.check(
        "EXACT",
        "the inverse orientation is C^2=E12+E23+E31",
        matrices_equal(cycle2, units[1, 2] + units[2, 3] + units[3, 2] * units[2, 1]),
    )
    EVIDENCE.check(
        "EXACT",
        "C has order three and C^2=C^dagger",
        matrices_equal(cycle**3, sp.eye(3)) and matrices_equal(cycle2, cycle.conjugate().T),
    )
    EVIDENCE.check(
        "EXACT",
        "B0,B1,B2 are Hermitian adjacent-chain combinations",
        all(is_hermitian(item) for item in (b0, b1, b2)),
    )
    y12 = sp.I * (units[2, 1] - units[1, 2])
    y13 = sp.I * (units[3, 1] - units[1, 3])
    y23 = sp.I * (units[3, 2] - units[2, 3])
    EVIDENCE.check("EXACT", "the fixed B2 orientation is Y12+Y23-Y13", matrices_equal(b2, y12 + y23 - y13))

    comm_map = commutator_map(cycle)
    kernel = comm_map.nullspace()
    expected_kernel = sp.Matrix.hstack(*(hermitian_coordinates(item) for item in (b0, b1, b2)))
    solved_kernel = sp.Matrix.hstack(*kernel)
    EVIDENCE.check(
        "EXACT",
        "the full 18-by-9 real commutator system has rank six",
        comm_map.shape == (18, 9) and comm_map.rank() == 6,
        detail=f"shape={comm_map.shape} rank={comm_map.rank()}",
    )
    EVIDENCE.check(
        "EXACT",
        "the solved Hermitian commutant has nullity exactly three",
        len(kernel) == 3,
        detail=f"nullity={len(kernel)}",
    )
    EVIDENCE.check(
        "EXACT",
        "the complete commutant kernel equals span_R{B0,B1,B2}",
        expected_kernel.rank() == 3
        and solved_kernel.rank() == 3
        and sp.Matrix.hstack(expected_kernel, solved_kernel).rank() == 3,
    )

    h, variables = generic_hermitian()
    a, x, y = sp.symbols("a x y", real=sp.S.true)
    commutant_substitution = {
        variables[0]: a,
        variables[1]: a,
        variables[2]: a,
        variables[3]: x,
        variables[4]: x,
        variables[5]: x,
        variables[6]: y,
        variables[7]: -y,
        variables[8]: y,
    }
    solved_form = sp.simplify(h.subs(commutant_substitution))
    EVIDENCE.check(
        "EXACT",
        "the explicit nine-coordinate commutant solution is aB0+xB1+yB2",
        matrices_equal(solved_form, a * b0 + x * b1 + y * b2),
        detail="d0=d1=d2; x12=x13=x23; y12=y23=-y13",
    )


def exact_projector_and_gram() -> None:
    section("EXACT 2: orthogonal C3 conjugation projector and exact Gram data")
    cycle = canonical_cycle()
    b0, b1, b2 = canonical_basis()
    h_basis = hermitian_coordinate_basis()
    projected = tuple(cyclic_projector(item, cycle, 3) for item in h_basis)
    projector_coordinates = sp.Matrix.hstack(*(hermitian_coordinates(item) for item in projected))

    EVIDENCE.check(
        "EXACT",
        "the average preserves Hermiticity on a full real basis of Herm(3)",
        all(is_hermitian(item) for item in projected),
    )
    EVIDENCE.check(
        "EXACT",
        "every averaged basis element commutes with C",
        all(matrix_is_zero(item * cycle - cycle * item) for item in projected),
    )
    EVIDENCE.check(
        "EXACT",
        "the average fixes B0,B1,B2",
        all(matrices_equal(cyclic_projector(item, cycle, 3), item) for item in (b0, b1, b2)),
    )
    EVIDENCE.check(
        "EXACT",
        "the average is idempotent on all nine Hermitian coordinates",
        all(matrices_equal(cyclic_projector(item, cycle, 3), item) for item in projected),
    )
    EVIDENCE.check(
        "EXACT",
        "the group average is self-adjoint for Re Tr on all 81 basis pairs",
        all(
            sp.simplify(real_trace_pair(cyclic_projector(left, cycle, 3), right) - real_trace_pair(left, cyclic_projector(right, cycle, 3))) == 0
            for left in h_basis
            for right in h_basis
        ),
    )
    EVIDENCE.check(
        "EXACT",
        "the projector image has exact real rank three",
        projector_coordinates.rank() == 3,
        detail=f"rank={projector_coordinates.rank()}",
    )
    gram = gram_matrix((b0, b1, b2))
    EVIDENCE.check(
        "EXACT",
        "the ordered trace Gram matrix is diag(3,6,6)",
        gram == sp.diag(3, 6, 6),
        detail=f"gram={gram.tolist()}",
    )


def exact_riesz_reconstruction_and_cone() -> None:
    section("EXACT 3: arbitrary supplied functional, unique Riesz representative, and cone")
    cycle = canonical_cycle()
    b0, b1, b2 = canonical_basis()
    cyclic_basis = (b0, b1, b2)
    q = sp.symbols("q0:9", real=sp.S.true)

    def functional(matrix: sp.Matrix) -> sp.Expr:
        coords = hermitian_coordinates(matrix)
        return sp.simplify(sum(coefficient * coordinate for coefficient, coordinate in zip(q, coords)))

    responses = tuple(functional(item) for item in cyclic_basis)
    h_ell = sp.simplify(responses[0] * b0 / 3 + responses[1] * b1 / 6 + responses[2] * b2 / 6)
    u0, u1, u2 = sp.symbols("u0 u1 u2", real=sp.S.true)
    test_vector = u0 * b0 + u1 * b1 + u2 * b2
    EVIDENCE.check("EXACT", "the Riesz formula is Hermitian for arbitrary real functional data", is_hermitian(h_ell))
    EVIDENCE.check(
        "EXACT",
        "the Riesz representative agrees with an arbitrary real-linear functional on all cyclic coordinates",
        sp.simplify(functional(test_vector) - real_trace_pair(h_ell, test_vector)) == 0,
    )
    gram = gram_matrix(cyclic_basis)
    response_vector = sp.Matrix(sp.symbols("r0:3", real=sp.S.true))
    unique_coefficients = sp.simplify(gram.inv() * response_vector)
    EVIDENCE.check(
        "EXACT",
        "the nonsingular Gram system gives the unique coefficients (r0/3,r1/6,r2/6)",
        gram.det() == 108
        and unique_coefficients == sp.Matrix((response_vector[0] / 3, response_vector[1] / 6, response_vector[2] / 6)),
        detail=f"det(G)={gram.det()}",
    )

    a, x, y = sp.symbols("a x y", real=sp.S.true)
    generic_cyclic = a * b0 + x * b1 + y * b2
    trace_responses = tuple(real_trace_pair(item, generic_cyclic) for item in cyclic_basis)
    recovered = sp.simplify(trace_responses[0] * b0 / 3 + trace_responses[1] * b1 / 6 + trace_responses[2] * b2 / 6)
    EVIDENCE.check(
        "EXACT",
        "every cyclic Hermitian H has responses (3a,6x,6y)",
        trace_responses == (3 * a, 6 * x, 6 * y),
    )
    EVIDENCE.check("EXACT", "the three trace responses recover every cyclic Hermitian H", matrices_equal(recovered, generic_cyclic))

    generic_h, _ = generic_hermitian()
    projected = cyclic_projector(generic_h, cycle, 3)
    projected_responses = tuple(real_trace_pair(item, generic_h) for item in cyclic_basis)
    projected_reconstruction = sp.simplify(
        projected_responses[0] * b0 / 3 + projected_responses[1] * b1 / 6 + projected_responses[2] * b2 / 6
    )
    EVIDENCE.check(
        "EXACT",
        "for a generic nine-coordinate Hermitian matrix the same responses reconstruct its cyclic projection",
        matrices_equal(projected, projected_reconstruction),
    )

    r0, r1, r2 = sp.symbols("r0 r1 r2", real=sp.S.true)
    cone_in_responses = sp.expand(18 * ((r0 / 3) ** 2 - 2 * ((r1 / 6) ** 2 + (r2 / 6) ** 2)))
    cone_polynomial = sp.Poly(cone_in_responses, r0, r1, r2)
    EVIDENCE.check(
        "EXACT",
        "independent coefficient extraction gives 2r0^2-r1^2-r2^2",
        cone_polynomial.coeff_monomial(r0**2) == 2
        and cone_polynomial.coeff_monomial(r1**2) == -1
        and cone_polynomial.coeff_monomial(r2**2) == -1
        and len(cone_polynomial.terms()) == 3,
        detail=f"18*residual={cone_in_responses}",
    )


def source_support_checks() -> None:
    section("SUPPORT: source scope, wiring, and evidence hygiene")
    note = NOTE_PATH.read_text(encoding="utf-8")
    source = Path(__file__).read_text(encoding="utf-8")
    required_note = (
        "# Adjacent-Chain Cyclic-Response Compression and Riesz-Reconstruction Lemma",
        "**Type:** positive_theorem",
        "ell : V -> R",
        "H_ell = (r0/3) B0 + (r1/6) B1 + (r2/6) B2",
        "No microscopic source functional, physical carrier or readout, mass",
    )
    forbidden_note = (
        "actual local " + "Wilson descendant",
        "Wilson first-" + "variation",
        "charged-" + "lepton target",
        "physical mass " + "spectrum",
        "selected physical " + "Koide law",
        "future Wilson " + "obligation",
        "what this buys",
        "sharp next move",
    )
    EVIDENCE.check(
        "SUPPORT",
        "the note carries every required abstract supplied-functional marker",
        all(marker in note for marker in required_note),
    )
    EVIDENCE.check(
        "SUPPORT",
        "the note carries none of the removed physical or promotional claims",
        all(marker.lower() not in note.lower() for marker in forbidden_note),
    )
    markdown_doc_links = re.findall(r"\[[^\]]+\]\(([^)]+\.md(?:#[^)]+)?)\)", note)
    EVIDENCE.check(
        "SUPPORT",
        "the self-contained proof has no hidden source-note dependency link",
        len(markdown_doc_links) == 0,
        detail=f"links={markdown_doc_links}",
    )
    forbidden_runner_tokens = (
        "num" + "py",
        "ran" + "dom",
        "all" + "close",
        "PD" + "G",
        "masses" + " =",
        "cls=" + '"D"',
    )
    EVIDENCE.check(
        "SUPPORT",
        "the runner contains no floating, stochastic, observed-comparator, or D-check evidence path",
        all(token not in source for token in forbidden_runner_tokens),
    )


def theorem_contract_errors(
    cycle: sp.Matrix,
    claimed_dimension: int,
    gram_denominators: tuple[int, int, int],
    projector_denominator: int,
    response_basis: tuple[sp.Matrix, sp.Matrix, sp.Matrix],
    reconstruction_basis: tuple[sp.Matrix, sp.Matrix, sp.Matrix],
    koide_factor: int,
) -> set[str]:
    errors: set[str] = set()
    canonical = canonical_cycle()
    canonical_responses = canonical_basis()
    if not matrices_equal(cycle, canonical):
        errors.add("cycle_orientation")

    actual_dimension = 9 - commutator_map(cycle).rank()
    if claimed_dimension != actual_dimension:
        errors.add("commutant_dimension")

    actual_gram = gram_matrix(canonical_responses)
    claimed_gram = sp.diag(*gram_denominators)
    if actual_gram != claimed_gram:
        errors.add("gram_denominator")

    projected_basis = tuple(cyclic_projector(item, cycle, projector_denominator) for item in hermitian_coordinate_basis())
    projector_ok = all(
        matrices_equal(cyclic_projector(item, cycle, projector_denominator), item)
        for item in projected_basis
    ) and all(
        matrices_equal(cyclic_projector(item, cycle, projector_denominator), item)
        for item in canonical_responses
    )
    if not projector_ok:
        errors.add("projector_normalization")

    a, x, y = sp.symbols("ma mx my", real=sp.S.true)
    target = a * canonical_responses[0] + x * canonical_responses[1] + y * canonical_responses[2]
    responses = tuple(real_trace_pair(item, target) for item in response_basis)
    reconstructed = sum(
        (
            response * basis / sp.Integer(denominator)
            for response, basis, denominator in zip(responses, reconstruction_basis, gram_denominators)
        ),
        sp.zeros(3),
    )
    if not matrices_equal(reconstructed, target):
        errors.add("response_reconstruction")
    reconstruction_columns = sp.Matrix.hstack(*(hermitian_coordinates(item) for item in reconstruction_basis))
    if reconstruction_columns.rank() != 3:
        errors.add("reconstruction_uniqueness")

    r0, r1, r2 = sp.symbols("mr0 mr1 mr2", real=sp.S.true)
    scaled_cone = sp.expand(18 * ((r0 / 3) ** 2 - koide_factor * ((r1 / 6) ** 2 + (r2 / 6) ** 2)))
    expected_cone = 2 * r0**2 - r1**2 - r2**2
    if sp.simplify(scaled_cone - expected_cone) != 0:
        errors.add("koide_factor")
    return errors


def functional_contract_errors(functional: object) -> set[str]:
    errors: set[str] = set()
    b0, b1, b2 = canonical_basis()
    u = b0 + b1
    v = 2 * b0 - b1 + b2
    values = tuple(sp.simplify(functional(item)) for item in (u, v, u + v, 3 * u))
    if sp.simplify(values[2] - values[0] - values[1]) != 0 or sp.simplify(values[3] - 3 * values[0]) != 0:
        errors.add("functional_linearity")
    if any(sp.simplify(sp.im(value)) != 0 for value in values):
        errors.add("functional_reality")
    return errors


def mutation_checks() -> None:
    section("MUTATION: hostile theorem-contract variants must be rejected")
    cycle = canonical_cycle()
    basis = canonical_basis()
    base = {
        "cycle": cycle,
        "claimed_dimension": 3,
        "gram_denominators": (3, 6, 6),
        "projector_denominator": 3,
        "response_basis": basis,
        "reconstruction_basis": basis,
        "koide_factor": 2,
    }
    baseline_errors = theorem_contract_errors(**base)
    EVIDENCE.check("MUTATION", "canonical theorem contract is accepted before mutation", len(baseline_errors) == 0, detail=str(sorted(baseline_errors)))

    mutations = (
        ("wrong cycle orientation", "cycle_orientation", {"cycle": cycle.T}),
        ("missing commutant dimension", "commutant_dimension", {"claimed_dimension": 2}),
        ("extra commutant dimension", "commutant_dimension", {"claimed_dimension": 4}),
        ("wrong Gram denominator", "gram_denominator", {"gram_denominators": (3, 5, 6)}),
        ("wrong projector normalization", "projector_normalization", {"projector_denominator": 2}),
        ("wrong response index", "response_reconstruction", {"response_basis": (basis[0], basis[2], basis[1])}),
        ("wrong response sign", "response_reconstruction", {"response_basis": (basis[0], basis[1], -basis[2])}),
        ("nonunique reconstruction basis", "reconstruction_uniqueness", {"reconstruction_basis": (basis[0], basis[1], basis[1])}),
        ("wrong Koide factor", "koide_factor", {"koide_factor": 1}),
    )
    for name, expected_error, override in mutations:
        candidate = dict(base)
        candidate.update(override)
        errors = theorem_contract_errors(**candidate)
        EVIDENCE.check(
            "MUTATION",
            f"validator kills {name}",
            expected_error in errors,
            detail=f"errors={sorted(errors)}",
        )

    valid_target = 2 * basis[0] - 3 * basis[1] + basis[2]
    invalid_target = valid_target + matrix_unit(1, 2)
    EVIDENCE.check("MUTATION", "Hermitian target validator accepts the exact control", is_hermitian(valid_target))
    EVIDENCE.check("MUTATION", "Hermitian target validator kills a non-Hermitian supplied target", not is_hermitian(invalid_target))

    linear_functional = lambda matrix: real_trace_pair(2 * basis[0] - basis[1] + 3 * basis[2], matrix)
    nonlinear_functional = lambda matrix: sp.trace(matrix) ** 2 + real_trace_pair(basis[1], matrix)
    linear_errors = functional_contract_errors(linear_functional)
    nonlinear_errors = functional_contract_errors(nonlinear_functional)
    EVIDENCE.check("MUTATION", "real-linear functional validator accepts the exact control", len(linear_errors) == 0, detail=str(sorted(linear_errors)))
    EVIDENCE.check(
        "MUTATION",
        "real-linear functional validator kills nonlinear functional misuse",
        "functional_linearity" in nonlinear_errors,
        detail=str(sorted(nonlinear_errors)),
    )


def main() -> int:
    print("ADJACENT-CHAIN CYCLIC-RESPONSE COMPRESSION / RIESZ CERTIFICATE")
    exact_adjacent_chain_and_commutant()
    exact_projector_and_gram()
    exact_riesz_reconstruction_and_cone()
    source_support_checks()
    mutation_checks()
    print()
    print("SUMMARY " + EVIDENCE.summary())
    return int(EVIDENCE.failed() != 0)


if __name__ == "__main__":
    sys.exit(main())
