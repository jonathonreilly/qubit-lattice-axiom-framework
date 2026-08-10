#!/usr/bin/env python3
"""Exact checks for the Admissibility/Record content-decoder boundary.

The runner checks the explicit Gaussian marginal data, covariance fixtures,
content-only additive readouts, exact shared-effect menus, and the source-bound
decoder/effect-descent interfaces. Atomlessness, Borel measurability, and the
Gaussian integral inequality are proved analytically in the source note.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import permutations, product
from math import erf, sqrt
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "ADMISSIBILITY_RECORD_CONTENT_DECODER_PUSHFORWARD_EFFECT_DESCENT_INDEPENDENCE_BOUNDED_THEOREM_NOTE_2026-08-10.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
PARENT_PATH = ROOT / "docs" / "ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-10.md"
FINITE_PRIOR_PATH = ROOT / "docs" / "PROBABILITY_READOUT_UNDERDETERMINATION_CYCLE912_BOUNDED_THEOREM_NOTE_2026-07-28.md"
PHYSICAL_PRIOR_PATH = ROOT / "docs" / "work_history" / "repo" / "review_feedback" / "PHYSICAL_EFFECT_EQUIVALENCE_NORMALIZED_GRADE_CYCLE321_NOTE_2026-07-18.md"
OUTCOME_OPERATION_PATH = ROOT / "docs" / "RECORD_OBSERVABLE_QUOTIENT_AND_RANK_ONE_FORMATION_OUTCOME_OPERATION_NORMAL_FORM_BOUNDED_THEOREM_NOTE_2026-07-11.md"

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RECORD_CONTENT_DECODER_PUSHFORWARD_EFFECT_DESCENT_INDEPENDENCE_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/PROBABILITY_READOUT_UNDERDETERMINATION_CYCLE912_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "docs/work_history/repo/review_feedback/PHYSICAL_EFFECT_EQUIVALENCE_NORMALIZED_GRADE_CYCLE321_NOTE_2026-07-18.md",
    "docs/RECORD_OBSERVABLE_QUOTIENT_AND_RANK_ONE_FORMATION_OUTCOME_OPERATION_NORMAL_FORM_BOUNDED_THEOREM_NOTE_2026-07-11.md",
)


def normalize(text: str) -> str:
    return " ".join(text.split())


Matrix = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]

ZERO_MATRIX: Matrix = (
    (Fraction(0), Fraction(0)),
    (Fraction(0), Fraction(0)),
)
P_Z: Matrix = (
    (Fraction(1), Fraction(0)),
    (Fraction(0), Fraction(0)),
)
IDENTITY: Matrix = (
    (Fraction(1), Fraction(0)),
    (Fraction(0), Fraction(1)),
)
PAULI_X: Matrix = (
    (Fraction(0), Fraction(1)),
    (Fraction(1), Fraction(0)),
)


def matrix_add(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(left[row][column] + right[row][column] for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def matrix_scale(value: Fraction, matrix: Matrix) -> Matrix:
    return tuple(
        tuple(value * matrix[row][column] for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def matrix_multiply(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            sum(left[row][index] * right[index][column] for index in range(2))
            for column in range(2)
        )
        for row in range(2)
    )  # type: ignore[return-value]


def trace_product(left: Matrix, right: Matrix) -> Fraction:
    return sum(
        left[row][column] * right[column][row]
        for row in range(2)
        for column in range(2)
    )


def conjugate_by_x(matrix: Matrix) -> Matrix:
    return matrix_multiply(matrix_multiply(PAULI_X, matrix), PAULI_X)


def matrix_average(matrices: tuple[Matrix, ...]) -> Matrix:
    total = ZERO_MATRIX
    for matrix in matrices:
        total = matrix_add(total, matrix)
    return matrix_scale(Fraction(1, len(matrices)), total)


def permutation_parity(values: tuple[int, int, int]) -> int:
    inversions = sum(
        values[left] > values[right]
        for left in range(3)
        for right in range(left + 1, 3)
    )
    return -1 if inversions % 2 else 1


Direction = tuple[int, int, int]


def proper_cubic_direction_permutations() -> tuple[tuple[int, ...], ...]:
    directions: tuple[Direction, ...] = (
        (1, 0, 0),
        (-1, 0, 0),
        (0, 1, 0),
        (0, -1, 0),
        (0, 0, 1),
        (0, 0, -1),
    )
    direction_index = {direction: index for index, direction in enumerate(directions)}
    induced: set[tuple[int, ...]] = set()
    for axes_raw in permutations(range(3)):
        axes = tuple(axes_raw)
        for signs_raw in product((-1, 1), repeat=3):
            signs = tuple(signs_raw)
            if permutation_parity(axes) * signs[0] * signs[1] * signs[2] != 1:
                continue
            image = []
            for direction in directions:
                transformed = tuple(
                    signs[row] * direction[axes[row]] for row in range(3)
                )
                image.append(direction_index[transformed])
            induced.add(tuple(image))
    return tuple(sorted(induced))


def content_score(matrix: Matrix) -> Fraction:
    return trace_product(IDENTITY, matrix)


def decoder_up(matrix: Matrix) -> str:
    return "+" if content_score(matrix) >= 0 else "-"


def decoder_down(matrix: Matrix) -> str:
    return "+" if content_score(matrix) < 0 else "-"


def positive_count(contents: tuple[Matrix, ...], decoder) -> int:
    return sum(decoder(content) == "+" for content in contents)


@dataclass(frozen=True)
class RecordFixture:
    identifier: str
    content: Matrix


@dataclass(frozen=True)
class Qsqrt2:
    """Exact scalar a + b sqrt(2) for the shared-effect menu checks."""

    a: Fraction = Fraction(0)
    b: Fraction = Fraction(0)

    def __add__(self, other: "Qsqrt2") -> "Qsqrt2":
        return Qsqrt2(self.a + other.a, self.b + other.b)

    def __neg__(self) -> "Qsqrt2":
        return Qsqrt2(-self.a, -self.b)

    def __sub__(self, other: "Qsqrt2") -> "Qsqrt2":
        return self + (-other)

    def __mul__(self, other: "Qsqrt2") -> "Qsqrt2":
        return Qsqrt2(
            self.a * other.a + 2 * self.b * other.b,
            self.a * other.b + self.b * other.a,
        )

    def scale(self, value: Fraction) -> "Qsqrt2":
        return Qsqrt2(value * self.a, value * self.b)


ZERO = Qsqrt2()
ONE = Qsqrt2(Fraction(1))


def q(value: int | Fraction) -> Qsqrt2:
    return Qsqrt2(Fraction(value))


def rs2(value: int | Fraction) -> Qsqrt2:
    return Qsqrt2(Fraction(0), Fraction(value))


Vector = tuple[Qsqrt2, Qsqrt2, Qsqrt2]


def vector_scale(value: Fraction, vector: Vector) -> Vector:
    return tuple(component.scale(value) for component in vector)  # type: ignore[return-value]


def vector_sum(vectors: tuple[Vector, ...]) -> Vector:
    return tuple(
        sum((vector[index] for vector in vectors), ZERO) for index in range(3)
    )  # type: ignore[return-value]


def norm_squared(vector: Vector) -> Qsqrt2:
    return sum((component * component for component in vector), ZERO)


@dataclass(frozen=True)
class Effect:
    coefficient: Fraction
    bloch: Vector


def menu_is_resolution(menu: tuple[Effect, ...]) -> bool:
    scalar_ok = sum(effect.coefficient for effect in menu) == 2
    vector = vector_sum(
        tuple(vector_scale(effect.coefficient, effect.bloch) for effect in menu)
    )
    unit_vectors = all(norm_squared(effect.bloch) == ONE for effect in menu)
    scaled_domain = all(Fraction(0) < effect.coefficient <= 1 for effect in menu)
    return scalar_ok and vector == (ZERO, ZERO, ZERO) and unit_vectors and scaled_domain


def contextual_label(epsilon: int, score: Fraction, residual: Fraction) -> int:
    if epsilon * score >= 0:
        return 0
    return 1 if residual >= 0 else 2


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool) -> None:
        result = bool(condition)
        if result:
            self.passed += 1
        else:
            self.failed += 1
        print(f"{'PASS' if result else 'FAIL'}: {label} {statement}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    parent = PARENT_PATH.read_text(encoding="utf-8")
    finite_prior = FINITE_PRIOR_PATH.read_text(encoding="utf-8")
    physical_prior = PHYSICAL_PRIOR_PATH.read_text(encoding="utf-8")
    outcome_operation = OUTCOME_OPERATION_PATH.read_text(encoding="utf-8")
    normalized_note = normalize(note).replace("> ", "")

    print("external_scientific_inputs: current axiom wording and four explicit prior boundary sources are source-bound; no observational, fitted, or target-value input is used")
    print("package_local_integrity_reads: the proposed source note is checked for its decoder, candidate, status, and N1-N8 surfaces; the cache envelope binds every declared input")
    print("analytic_boundary: Borel measurability, atomlessness, and strict Gaussian half-space inequality are source proofs; the runner checks their exact finite parameters and independent controls")
    print("negative_scope: only decoder nonselection on the displayed Gaussian completion and automatic effect descent for the displayed two-menu family are rejected")

    canonical_readout = (
        "Only records are readable. A readout value is determined by record "
        "content alone. For any finite collection of pairwise-disjoint records, "
        "scalar readout `I` is additive, with `I(empty)=0`."
    )
    checks.check(
        "source-current-record",
        "the exact current content-only additive Record clause is present",
        canonical_readout in normalize(axiom),
    )
    checks.check(
        "source-parent-interface",
        "Block 2 names registered measurable outcome partitions and same-effect descent separately",
        "registered measurable outcome partitions" in parent
        and "same-effect descent" in parent,
    )
    checks.check(
        "source-finite-prior",
        "the finite prior exposes an affine simplex of content-determined weights",
        "The normalized non-negative content-determined weights form an affine simplex"
        in normalize(finite_prior),
    )
    checks.check(
        "source-physical-prior",
        "the physical prior does not derive a general effect-only quotient",
        "do not derive a general effect-only quotient" in normalize(physical_prior),
    )
    checks.check(
        "source-outcome-operation",
        "the supplied locked-output normal form makes the effect unique without selecting it",
        "The effect is unique" in outcome_operation
        and "does not derive `E_P=P`" in outcome_operation,
    )

    real_dimension = 2 * 2 * 2
    density_power = Fraction(-4)
    integral_power = Fraction(real_dimension, 2)
    checks.check(
        "gaussian-normalization",
        "the pi^-4 density normalizes on the eight-real-dimensional matrix domain",
        real_dimension == 8 and density_power + integral_power == 0,
    )

    rotations = proper_cubic_direction_permutations()
    neighbor_contents = tuple(
        (
            (Fraction(index + 1), Fraction(index, 7)),
            (Fraction(index, 11), Fraction(6 - index, 5)),
        )
        for index in range(6)
    )
    center = matrix_average(neighbor_contents)
    rotation_centers = {
        matrix_average(tuple(neighbor_contents[index] for index in permutation))
        for permutation in rotations
    }
    checks.check(
        "proper-cubic-neighbor-covariance",
        "all 24 proper-cubic shell permutations preserve the neighbor-average center",
        len(rotations) == 24 and rotation_centers == {center},
    )
    checks.check(
        "neighbor-condition-variation",
        "the fixed center rule changes between all-zero and all-Pz neighbor conditions",
        matrix_average((ZERO_MATRIX,) * 6) == ZERO_MATRIX
        and matrix_average((P_Z,) * 6) == P_Z
        and ZERO_MATRIX != P_Z,
    )

    sample_matrix: Matrix = (
        (Fraction(2), Fraction(1)),
        (Fraction(3), Fraction(-1)),
    )
    transformed_score = trace_product(
        conjugate_by_x(IDENTITY), conjugate_by_x(sample_matrix)
    )
    checks.check(
        "simultaneous-unitary-covariance",
        "an exact Pauli-X control preserves the content statistic under simultaneous conjugation",
        conjugate_by_x(P_Z)
        == ((Fraction(0), Fraction(0)), (Fraction(0), Fraction(1)))
        and transformed_score == content_score(sample_matrix),
    )

    gaussian_mean = trace_product(IDENTITY, P_Z)
    gaussian_variance = trace_product(IDENTITY, IDENTITY) / 2
    checks.check(
        "gaussian-marginal-parameters",
        "the declared content statistic has exact Gaussian mean one and variance one",
        gaussian_mean == 1 and gaussian_variance == 1,
    )

    negative: Matrix = (
        (Fraction(-2), Fraction(0)),
        (Fraction(0), Fraction(0)),
    )
    boundary = ZERO_MATRIX
    positive: Matrix = (
        (Fraction(3), Fraction(0)),
        (Fraction(0), Fraction(0)),
    )
    samples = (negative, boundary, positive)
    checks.check(
        "binary-decoder-partitions",
        "both opposite decoders assign exactly one label to negative, boundary, and positive controls",
        tuple(decoder_up(matrix) for matrix in samples) == ("-", "+", "+")
        and tuple(decoder_down(matrix) for matrix in samples) == ("+", "-", "-"),
    )
    left_record = RecordFixture("left", positive)
    right_record = RecordFixture("right", positive)
    checks.check(
        "decoder-content-only",
        "duplicated record contents receive the same label independent of record identity",
        left_record.identifier != right_record.identifier
        and left_record.content == right_record.content
        and decoder_up(left_record.content) == decoder_up(right_record.content)
        and decoder_down(left_record.content) == decoder_down(right_record.content),
    )
    left_records = (negative, boundary)
    right_records = (positive, negative)
    checks.check(
        "record-readout-additivity",
        "recordwise indicator sums are exactly additive on disjoint finite collections",
        all(
            positive_count(left_records + right_records, decoder)
            == positive_count(left_records, decoder)
            + positive_count(right_records, decoder)
            for decoder in (decoder_up, decoder_down)
        )
        and positive_count((), decoder_up) == 0,
    )

    p_up = Fraction(1, 2) + erf(1 / sqrt(2)) / 2
    p_down = Fraction(1, 2) - erf(1 / sqrt(2)) / 2
    checks.check(
        "gaussian-pushforward-normalization",
        "the opposite half-space probabilities sum to one",
        abs(float(p_up + p_down) - 1.0) < 1e-15,
    )
    checks.check(
        "gaussian-decoder-selection",
        "the same measure gives the two positive labels strictly different probabilities Phi(1) and Phi(-1)",
        float(p_up) > 0.5 > float(p_down)
        and float(p_up - p_down) > 0,
    )

    z = (ZERO, ZERO, ONE)
    n1 = (rs2(Fraction(4, 9)), ZERO, q(Fraction(-7, 9)))
    n2 = (rs2(Fraction(-2, 3)), ZERO, q(Fraction(1, 3)))
    m1 = (rs2(Fraction(2, 3)), ZERO, q(Fraction(-1, 3)))
    m2 = (rs2(Fraction(-2, 3)), ZERO, q(Fraction(-1, 3)))
    e0 = Effect(Fraction(1, 2), z)
    menu_a = (
        e0,
        Effect(Fraction(9, 10), n1),
        Effect(Fraction(3, 5), n2),
    )
    menu_b = (
        e0,
        Effect(Fraction(3, 4), m1),
        Effect(Fraction(3, 4), m2),
    )
    checks.check(
        "ternary-menu-a",
        "the asymmetric decoder program is an exact scaled-projector resolution",
        menu_is_resolution(menu_a),
    )
    checks.check(
        "ternary-menu-b",
        "the symmetric decoder program is an exact scaled-projector resolution",
        menu_is_resolution(menu_b),
    )
    checks.check(
        "shared-effect-incidence",
        "the two decoder programs share exactly E0 and otherwise contain distinct effects",
        set(menu_a).intersection(menu_b) == {e0}
        and len(set(menu_a).union(menu_b)) == 5,
    )
    epsilon_a = 1 if max(effect.coefficient for effect in menu_a[1:]) > Fraction(3, 4) else -1
    epsilon_b = 1 if max(effect.coefficient for effect in menu_b[1:]) > Fraction(3, 4) else -1
    checks.check(
        "invariant-context-sign",
        "the trace-coefficient rule assigns opposite exact signs to the two menu contexts",
        epsilon_a == 1 and epsilon_b == -1,
    )
    checks.check(
        "context-decoder-totality",
        "each contextual decoder assigns exactly one of three labels on all sign controls",
        all(
            contextual_label(epsilon, score, residual) in (0, 1, 2)
            for epsilon in (epsilon_a, epsilon_b)
            for score in (Fraction(-1), Fraction(0), Fraction(1))
            for residual in (Fraction(-1), Fraction(0), Fraction(1))
        ),
    )
    shared_a = p_up if epsilon_a == 1 else p_down
    shared_b = p_up if epsilon_b == 1 else p_down
    checks.check(
        "effect-descent-separation",
        "normalized content decoders assign the shared effect Phi(1) and Phi(-1)",
        shared_a == p_up and shared_b == p_down and shared_a != shared_b,
    )

    decoder_needles = (
        "finite-label measurable decoders and labeled measurable partitions are the same data",
        "`K(i)=mu_eta(A(i))=mu_eta(d^{-1}({i}))`",
        "This readout is determined by record content, is additive on disjoint finite collections",
        "decoder registration and measure pushforward do not imply same-effect descent",
    )
    checks.check(
        "decoder-equivalence-surface",
        "the source states the decoder/partition equivalence, pushforward, Record link, and descent boundary",
        all(phrase in normalized_note for phrase in decoder_needles),
    )

    candidate_needles = (
        "For each fixed preparation class `p` and each registered local program `a`",
        "`d_{p,a}:X->{1,...,|M_a|}`",
        "`K_{p,a}(i)=mu_{p,a}(d_{p,a}^{-1}({i}))`",
        "`q(a,i)=E_{a,i}` descends at fixed `p`",
        "with `w_p(0)=0` and `w_p(I)=1`",
        "Every binary and ternary nonzero resolution of `I` by members of the full scaled domain `S`",
        "not a canonical edit, primitive, recommendation",
    )
    checks.check(
        "candidate-sufficiency-surface",
        "the refined candidate separates preparation, program, decoder, effect quotient, endpoints, and coverage",
        all(phrase in normalized_note for phrase in candidate_needles),
    )
    checks.check(
        "machine-status-contract",
        "the source uses controlled bounded-support and negative-route-pruning fields",
        all(
            phrase in note
            for phrase in (
                "actual_current_surface_status: bounded-support",
                "target_claim_type: bounded_theorem",
                "claim_type_reason:",
                "trace_class: negative_route_pruning",
                "source_of_blocker_text: handoff",
                "artifact_role: theorem",
                "next_trace_action:",
                "audit_required_before_effective_retained: true",
                "bare_retained_allowed: false",
            )
        ),
    )
    checks.check(
        "canonical-nonmutation",
        "the hypothetical decoder/program/effect-quotient notation is absent from the canonical axiom file",
        all(
            phrase not in axiom
            for phrase in ("content decoder", "d_{p,a}", "K_{p,a}", "q(a,i)")
        ),
    )
    checks.check(
        "no-go-gate",
        "all N1-N8 sections and the global-negative rejection are source-visible",
        all(f"### N{index}" in note for index in range(1, 9))
        and "FAIL / DO NOT SHIP" in note
        and "an axiom update is necessary" in note
        and "| Source location | Source residual used |" in note
        and "The primitive-registry scan used" in note,
    )

    print("per_element: exact Gaussian center/statistic data, two binary decoders, and the shared ternary effect E0 are checked")
    print("per_site: one M_2(C) site at a declared six-neighbor condition is executed; no global formation process is asserted")
    print("per_mode: all 24 proper-cubic shell permutations and an exact simultaneous-conjugation control are checked; no spectral exhaustion is claimed")
    print("per_block: decoder/partition pushforward, decoder selection, and same-effect descent are separated; endpoints and coverage remain explicit walls")
    print("lattice_wide: checked and not executed — covariance of the neighbor-average rule is analytic/local; no lattice-wide dynamics or decoder no-go is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
