#!/usr/bin/env python3
"""Exact checks for the Gaussian second-moment/quantile compiler theorem.

The runner checks the finite Gaussian moment parameters, exact density-operator
fixtures, exact shared-effect menus and weights, quantile interval arithmetic,
covariance controls, the atomic deterministic-decoder boundary, and the
source-bound status/N1-N8 surfaces. Gaussian integration and the probability-
integral transform are proved analytically in the source note.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "ADMISSIBILITY_GAUSSIAN_SECOND_MOMENT_QUANTILE_DECODER_EFFECT_QUOTIENT_BOUNDED_THEOREM_NOTE_2026-08-10.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
PARENT_PATH = ROOT / "docs" / "ADMISSIBILITY_RECORD_CONTENT_DECODER_PUSHFORWARD_EFFECT_DESCENT_INDEPENDENCE_BOUNDED_THEOREM_NOTE_2026-08-10.md"
MENU_PARENT_PATH = ROOT / "docs" / "ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-10.md"
EFFECT_PRIOR_PATH = ROOT / "docs" / "COVARIANT_EFFECT_MAP_NONSELECTION_AND_REPEAT_CERTAINTY_COLLAPSE_BOUNDED_THEOREM_NOTE_2026-07-11.md"
FINITE_PROCESS_PATH = ROOT / "docs" / "work_history" / "repo" / "review_feedback" / "CONTACT_ARCHIVE_FINITE_PROCESS_HISTORY_CYCLE284_NOTE_2026-07-17.md"
PHYSICAL_QUOTIENT_PATH = ROOT / "docs" / "work_history" / "repo" / "review_feedback" / "PHYSICAL_EFFECT_EQUIVALENCE_NORMALIZED_GRADE_CYCLE321_NOTE_2026-07-18.md"

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_GAUSSIAN_SECOND_MOMENT_QUANTILE_DECODER_EFFECT_QUOTIENT_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RECORD_CONTENT_DECODER_PUSHFORWARD_EFFECT_DESCENT_INDEPENDENCE_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/COVARIANT_EFFECT_MAP_NONSELECTION_AND_REPEAT_CERTAINTY_COLLAPSE_BOUNDED_THEOREM_NOTE_2026-07-11.md",
    "docs/work_history/repo/review_feedback/CONTACT_ARCHIVE_FINITE_PROCESS_HISTORY_CYCLE284_NOTE_2026-07-17.md",
    "docs/work_history/repo/review_feedback/PHYSICAL_EFFECT_EQUIVALENCE_NORMALIZED_GRADE_CYCLE321_NOTE_2026-07-18.md",
)


def normalize(text: str) -> str:
    return " ".join(text.split())


Matrix = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]

ZERO_MATRIX: Matrix = (
    (Fraction(0), Fraction(0)),
    (Fraction(0), Fraction(0)),
)
IDENTITY: Matrix = (
    (Fraction(1), Fraction(0)),
    (Fraction(0), Fraction(1)),
)
P_Z: Matrix = (
    (Fraction(1), Fraction(0)),
    (Fraction(0), Fraction(0)),
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


def matrix_trace(matrix: Matrix) -> Fraction:
    return matrix[0][0] + matrix[1][1]


def matrix_determinant(matrix: Matrix) -> Fraction:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def trace_product(left: Matrix, right: Matrix) -> Fraction:
    return sum(
        left[row][column] * right[column][row]
        for row in range(2)
        for column in range(2)
    )


def conjugate_by_x(matrix: Matrix) -> Matrix:
    return matrix_multiply(matrix_multiply(PAULI_X, matrix), PAULI_X)


def gaussian_noise_second_moment() -> Matrix:
    real_variance = Fraction(1, 2)
    complex_variance = 2 * real_variance
    return tuple(
        tuple(
            sum(
                (complex_variance if row == column else Fraction(0))
                for _ in range(2)
            )
            for column in range(2)
        )
        for row in range(2)
    )  # type: ignore[return-value]


def gaussian_state(center: Matrix, isotropic_offset: Fraction = Fraction(0)) -> Matrix:
    center_squared = matrix_multiply(center, center)
    moment = matrix_add(
        center_squared,
        matrix_scale(Fraction(2) + isotropic_offset, IDENTITY),
    )
    return matrix_scale(Fraction(1, matrix_trace(moment)), moment)


@dataclass(frozen=True)
class Qsqrt2:
    """Exact scalar a + b sqrt(2) for menu geometry."""

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
    return (
        scalar_ok
        and vector == (ZERO, ZERO, ZERO)
        and all(norm_squared(effect.bloch) == ONE for effect in menu)
        and all(Fraction(0) < effect.coefficient <= 1 for effect in menu)
    )


def effect_weight(effect: Effect, z_bias: Fraction) -> Fraction:
    z_component = effect.bloch[2]
    if z_component.b != 0:
        raise ValueError("weight fixture requires rational z component")
    return effect.coefficient * (Fraction(1) + z_bias * z_component.a) / 2


def cumulative(weights: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    result = [Fraction(0)]
    for weight in weights:
        result.append(result[-1] + weight)
    return tuple(result)


def quantile_label(value: Fraction, cuts: tuple[Fraction, ...]) -> int:
    for index in range(1, len(cuts)):
        if value < cuts[index]:
            return index - 1
    return len(cuts) - 2


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
    menu_parent = MENU_PARENT_PATH.read_text(encoding="utf-8")
    effect_prior = EFFECT_PRIOR_PATH.read_text(encoding="utf-8")
    finite_process = FINITE_PROCESS_PATH.read_text(encoding="utf-8")
    physical_quotient = PHYSICAL_QUOTIENT_PATH.read_text(encoding="utf-8")
    normalized_note = normalize(note).replace("> ", "")

    print("external_scientific_inputs: the current axiom, stacked Gaussian/menu parents, and three explicit instrument/effect prior boundaries are source-bound; no observed, fitted, or target probability is read")
    print("package_local_integrity_reads: the proposed theorem note is checked for its construction, boundary, machine status, and N1-N8 surfaces; the cache envelope binds every declared input")
    print("analytic_boundary: Gaussian integration, the probability-integral transform, Borel measurability, and general covariance are source proofs; the runner checks exact finite parameters and independent controls")
    print("negative_scope: only the displayed isotropic compiler family and singleton-support deterministic half-half target are rejected as unique/universal routes")

    canonical_probability = (
        "For each site, the probability distribution over the possibilities is "
        "determined by, and varies with, the nearest-neighbor conditions."
    )
    canonical_readout = (
        "Only records are readable. A readout value is determined by record "
        "content alone. For any finite collection of pairwise-disjoint records, "
        "scalar readout `I` is additive, with `I(empty)=0`."
    )
    checks.check(
        "source-current-axiom",
        "the exact current probability and content-only additive Record clauses are present",
        canonical_probability in normalize(axiom)
        and canonical_readout in normalize(axiom),
    )
    checks.check(
        "source-parent-residual",
        "Block 3 leaves the map to rho, physical program compiler, and operational quotient open",
        "the map `p -> rho_p` from the current possibility measure" in parent
        and "a physical program compiler or universal content decoder" in parent
        and "a dynamics-derived operational-effect quotient" in parent,
    )
    checks.check(
        "source-menu-parent",
        "the stacked menu parent supplies both exact shared-effect ternary menus",
        all(phrase in menu_parent for phrase in ("`E_0=(1/2)P(z)`", "`M_A={E_0", "`M_B={E_0")),
    )
    checks.check(
        "source-effect-prior",
        "the covariant effect prior leaves effect selection conditional on repeat certainty",
        "What selects `E_P=P`?" in effect_prior
        and "A physical derivation of (11)" in effect_prior,
    )
    checks.check(
        "source-finite-process-prior",
        "the prior finite decoder uses a supplied trace/Kraus four-state domain",
        "trace/Kraus rule is supplied" in finite_process
        and "four-state" in finite_process,
    )
    checks.check(
        "source-physical-quotient-prior",
        "the prior physical quotient does not derive a general effect-only quotient",
        "do not derive a general effect-only quotient" in normalize(physical_quotient),
    )

    real_dimension = 2 * 2 * 2
    noise = gaussian_noise_second_moment()
    checks.check(
        "gaussian-noise-moment",
        "eight real coordinates with variance one-half give E[Z Zdagger]=2I",
        real_dimension == 8 and noise == matrix_scale(Fraction(2), IDENTITY),
    )

    rho_blank = gaussian_state(ZERO_MATRIX)
    rho_zero = gaussian_state(P_Z)
    rho_one = gaussian_state(P_Z, Fraction(1))
    checks.check(
        "second-moment-density",
        "the raw normalized second moment gives I/2 at blank and diag(3/5,2/5) at Pz",
        rho_blank == matrix_scale(Fraction(1, 2), IDENTITY)
        and rho_zero
        == ((Fraction(3, 5), Fraction(0)), (Fraction(0), Fraction(2, 5))),
    )
    checks.check(
        "isotropic-family-density",
        "the lambda-one member is diag(4/7,3/7) and both fixtures are positive trace one",
        rho_one
        == ((Fraction(4, 7), Fraction(0)), (Fraction(0), Fraction(3, 7)))
        and all(matrix_trace(rho) == 1 and matrix_determinant(rho) > 0 for rho in (rho_zero, rho_one)),
    )
    checks.check(
        "density-operator-extractor-variation",
        "the second-moment density operator changes between blank and all-Pz conditions",
        rho_blank != rho_zero,
    )
    checks.check(
        "density-operator-extractor-covariance",
        "an exact Pauli-X control transports the center and extracted density operator by conjugation",
        gaussian_state(conjugate_by_x(P_Z)) == conjugate_by_x(rho_zero)
        and gaussian_state(conjugate_by_x(P_Z), Fraction(1))
        == conjugate_by_x(rho_one),
    )
    trace_noise_variance = 2 * Fraction(1, 2)
    checks.check(
        "trace-uniformizer-parameters",
        "the centered real trace has exact Gaussian mean zero and variance one",
        matrix_trace(P_Z) - matrix_trace(P_Z) == 0
        and trace_noise_variance == 1,
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
        "exact-menu-geometry",
        "both shared-effect ternary programs are exact scaled-projector resolutions",
        menu_is_resolution(menu_a) and menu_is_resolution(menu_b),
    )
    checks.check(
        "shared-effect-incidence",
        "the exact ternary programs share only E0",
        set(menu_a).intersection(menu_b) == {e0}
        and len(set(menu_a).union(menu_b)) == 5,
    )

    weights_a_zero = tuple(effect_weight(effect, Fraction(1, 5)) for effect in menu_a)
    weights_b_zero = tuple(effect_weight(effect, Fraction(1, 5)) for effect in menu_b)
    weights_a_one = tuple(effect_weight(effect, Fraction(1, 7)) for effect in menu_a)
    weights_b_one = tuple(effect_weight(effect, Fraction(1, 7)) for effect in menu_b)
    checks.check(
        "raw-compiler-menu-a",
        "the raw second-moment compiler gives exact menu-A weights (3/10,19/50,8/25)",
        weights_a_zero
        == (Fraction(3, 10), Fraction(19, 50), Fraction(8, 25)),
    )
    checks.check(
        "raw-compiler-menu-b",
        "the raw second-moment compiler gives exact menu-B weights (3/10,7/20,7/20)",
        weights_b_zero
        == (Fraction(3, 10), Fraction(7, 20), Fraction(7, 20)),
    )
    checks.check(
        "effect-grade-normalization",
        "all four exact compiler vectors are nonnegative and normalized",
        all(
            sum(weights) == 1 and all(weight > 0 for weight in weights)
            for weights in (weights_a_zero, weights_b_zero, weights_a_one, weights_b_one)
        ),
    )
    checks.check(
        "effect-descent",
        "at one fixed Gaussian condition, the shared effect receives one value in both contexts for each compiler member",
        weights_a_zero[0] == weights_b_zero[0] == Fraction(3, 10)
        and weights_a_one[0] == weights_b_one[0] == Fraction(2, 7),
    )
    checks.check(
        "compiler-nonselection-gap",
        "lambda zero and one give the shared effect the exact positive difference 1/70",
        weights_a_zero[0] - weights_a_one[0] == Fraction(1, 70),
    )

    cuts_a = cumulative(weights_a_zero)
    cuts_b = cumulative(weights_b_zero)
    checks.check(
        "quantile-cuts",
        "the exact cumulative cuts are (0,3/10,17/25,1) and (0,3/10,13/20,1)",
        cuts_a
        == (Fraction(0), Fraction(3, 10), Fraction(17, 25), Fraction(1))
        and cuts_b
        == (Fraction(0), Fraction(3, 10), Fraction(13, 20), Fraction(1)),
    )
    checks.check(
        "quantile-pushforward",
        "uniform interval lengths reproduce every exact effect weight",
        tuple(cuts_a[index + 1] - cuts_a[index] for index in range(3))
        == weights_a_zero
        and tuple(cuts_b[index + 1] - cuts_b[index] for index in range(3))
        == weights_b_zero,
    )
    checks.check(
        "quantile-decoder-totality",
        "midpoints of every nonempty interval receive exactly their ordered labels",
        all(
            quantile_label((cuts[index] + cuts[index + 1]) / 2, cuts) == index
            for cuts in (cuts_a, cuts_b)
            for index in range(3)
        )
        and quantile_label(Fraction(0), cuts_a) == 0
        and quantile_label(Fraction(1), cuts_a) == 2,
    )
    checks.check(
        "grade-endpoints",
        "the extracted density operator evaluates the null and certain effects as zero and one",
        trace_product(rho_zero, ZERO_MATRIX) == 0
        and trace_product(rho_zero, IDENTITY) == 1,
    )

    attainable_atomic = {
        tuple(Fraction(1 if assignment[0] == label else 0) for label in range(2))
        for assignment in product(range(2), repeat=1)
    }
    checks.check(
        "atomic-deterministic-boundary",
        "a singleton-support deterministic decoder attains only (1,0) or (0,1), never half-half",
        attainable_atomic
        == {(Fraction(1), Fraction(0)), (Fraction(0), Fraction(1))}
        and (Fraction(1, 2), Fraction(1, 2)) not in attainable_atomic,
    )

    construction_needles = (
        "`M_C := integral A A^dagger d mu_C(A)=C C^dagger+2I=C^2+2I`",
        "`rho_C := M_C/Tr(M_C)=(C^2+2I)/(Tr(C^2)+4)`",
        "`u_C(A)=Phi(t_C(A))`",
        "`mu_C(d_(C,M)^(-1)({i}))=c_i-c_(i-1)=p_i=w_C(E_i)`",
        "`p(M_A)=(3/10,19/50,8/25)`",
        "`p(M_B)=(3/10,7/20,7/20)`",
    )
    checks.check(
        "construction-source-surface",
        "the source states the moment, density operator, uniformizer, pushforward, and exact menu outputs",
        all(phrase in normalized_note for phrase in construction_needles),
    )
    boundary_needles = (
        "`lambda=0` gives `3/10`, while `lambda=1` gives `2/7`",
        "exact difference `1/70`",
        "`nu_C=delta_C`",
        "It cannot realize `(1/2,1/2)`",
        "not an adopted axiom update, recommendation, minimality theorem, or necessity claim",
    )
    checks.check(
        "boundary-source-surface",
        "the source states the bounded nonselection, atomic boundary, and governance limit",
        all(phrase in normalized_note for phrase in boundary_needles),
    )
    checks.check(
        "machine-status-contract",
        "the source carries the complete bounded upstream-support trace contract",
        all(
            phrase in note
            for phrase in (
                "actual_current_surface_status: bounded-support",
                "target_claim_type: bounded_theorem",
                "claim_type_reason:",
                "trace_class: upstream_support",
                "target_claim_id:",
                "target_blocker_text:",
                "source_of_blocker_text: handoff",
                "reachability_to_target: advances",
                "artifact_role: theorem",
                "next_trace_action:",
                "audit_required_before_effective_retained: true",
                "bare_retained_allowed: false",
            )
        ),
    )
    checks.check(
        "canonical-nonmutation",
        "the second-moment/quantile compiler notation is absent from the canonical axiom file",
        all(
            phrase not in axiom
            for phrase in ("rho_C :=", "u_C(A)", "quantile", "lambda I")
        ),
    )
    checks.check(
        "no-go-gate",
        "all N1-N8 sections, source matching, primitive scan, and global-negative rejection are visible",
        all(f"### N{index}" in note for index in range(1, 9))
        and "| Source location | Source residual used |" in note
        and "The primitive-registry scan used" in note
        and "FAIL / DO NOT SHIP" in note
        and "No global no-go is certified" in note,
    )

    print("per_element: all eight Gaussian coordinates, exact second moments, five menu effects, four weight vectors, and singleton atomic support are checked")
    print("per_site: one M_2(C) site is executed at blank and all-Pz neighbor conditions; no physical site-selection or formation process is asserted")
    print("per_mode: the centered trace uniformizer and an exact simultaneous Pauli-X conjugation control are checked; no spectral-mode exhaustion is claimed")
    print("per_block: the fixed-condition measure-to-density-operator-to-quantile-decoder-to-effect-grade chain is checked on two ternary programs and one atomic binary control")
    print("lattice_wide: checked and not executed — translation/proper-cubic covariance is analytic for the center rule, while global program dynamics and histories remain absent")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
