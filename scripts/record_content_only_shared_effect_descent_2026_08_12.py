#!/usr/bin/env python3
"""Exact checks for Record content-only descent versus Aug 10 restriction.

The runner recomputes the Aug 10 atomic masses, checks the narrow direct-value
obstruction for identical effect-only content, and exhibits context-bearing
content with one fixed readout that yields both restriction values. No cache
is written.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "RECORD_CONTENT_ONLY_SHARED_EFFECT_DESCENT_BOUNDED_THEOREM_NOTE_2026-08-12.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
PARENT_PATH = ROOT / "docs" / "ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-10.md"
BARYCENTER_PARENT_PATH = ROOT / "docs" / "ADMISSIBILITY_BARYCENTER_EVALUATION_MENU_KERNEL_BOUNDED_THEOREM_NOTE_2026-08-12.md"

AUDIT_INPUT_PATHS = (
    "docs/RECORD_CONTENT_ONLY_SHARED_EFFECT_DESCENT_BOUNDED_THEOREM_NOTE_2026-08-12.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/ADMISSIBILITY_BARYCENTER_EVALUATION_MENU_KERNEL_BOUNDED_THEOREM_NOTE_2026-08-12.md",
)


def normalize(text: str) -> str:
    return " ".join(text.split())


@dataclass(frozen=True)
class Qsqrt2:
    """Exact a + b sqrt(2) scalar sufficient for the Bloch witnesses."""

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
        sum((vector[index] for vector in vectors), ZERO)
        for index in range(3)
    )  # type: ignore[return-value]


def norm_squared(vector: Vector) -> Qsqrt2:
    return sum((component * component for component in vector), ZERO)


@dataclass(frozen=True)
class C:
    """Exact complex number with rational parts."""

    re: Fraction = Fraction(0)
    im: Fraction = Fraction(0)

    def __add__(self, other: "C") -> "C":
        return C(self.re + other.re, self.im + other.im)

    def __mul__(self, other: "C") -> "C":
        return C(
            self.re * other.re - self.im * other.im,
            self.re * other.im + self.im * other.re,
        )

    def scale(self, value: Fraction) -> "C":
        return C(value * self.re, value * self.im)


Matrix = tuple[tuple[C, C], tuple[C, C]]


def matrix_add(left: Matrix, right: Matrix) -> Matrix:
    return (
        (left[0][0] + right[0][0], left[0][1] + right[0][1]),
        (left[1][0] + right[1][0], left[1][1] + right[1][1]),
    )


def matrix_scale(value: C, matrix: Matrix) -> Matrix:
    return (
        (value * matrix[0][0], value * matrix[0][1]),
        (value * matrix[1][0], value * matrix[1][1]),
    )


def matrix_trace(matrix: Matrix) -> C:
    return matrix[0][0] + matrix[1][1]


def context_tag(matrix: Matrix) -> Fraction:
    return matrix_trace(matrix).im / 2


RESTRICTION_A = Fraction(25, 142)
RESTRICTION_B = Fraction(2, 11)


def context_readout(matrix: Matrix) -> Fraction:
    tag = context_tag(matrix)
    return (2 - tag) * RESTRICTION_A + (tag - 1) * RESTRICTION_B


IDENTITY: Matrix = (
    (C(Fraction(1)), C()),
    (C(), C(Fraction(1))),
)
E0_MATRIX: Matrix = (
    (C(Fraction(1, 2)), C()),
    (C(), C()),
)


def phi_eff(_menu_label: str, effect: Matrix) -> Matrix:
    return effect


def phi_ctx(menu_label: str, effect: Matrix) -> Matrix:
    alpha = {"A": Fraction(1), "B": Fraction(2)}[menu_label]
    shift = matrix_scale(C(Fraction(0), alpha), IDENTITY)
    return matrix_add(effect, shift)


@dataclass(frozen=True)
class Effect:
    coefficient: Fraction
    bloch: Vector


def menu_is_resolution(menu: tuple[Effect, ...]) -> bool:
    scalar_ok = sum(effect.coefficient for effect in menu) == 2
    vector = vector_sum(tuple(vector_scale(effect.coefficient, effect.bloch) for effect in menu))
    unit_vectors = all(norm_squared(effect.bloch) == ONE for effect in menu)
    scaled_domain = all(Fraction(0) < effect.coefficient <= Fraction(1) for effect in menu)
    return scalar_ok and vector == (ZERO, ZERO, ZERO) and unit_vectors and scaled_domain


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool, residual: object | None = None) -> None:
        result = bool(condition)
        if result:
            self.passed += 1
        else:
            self.failed += 1
        print(f"{'PASS' if result else 'FAIL'}: {label} {statement}")
        if not result and residual is not None:
            print(f"  residual: {residual}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    parent = PARENT_PATH.read_text(encoding="utf-8")
    barycenter_parent = BARYCENTER_PARENT_PATH.read_text(encoding="utf-8")
    normalized_note = normalize(note).replace("> ", "")
    normalized_axiom = normalize(axiom)
    normalized_parent = normalize(parent)
    normalized_barycenter_parent = normalize(barycenter_parent)

    print("external_scientific_inputs: current Record wording and the Aug 10 menus/atomic masses are source-bound; no observational or fitted inputs are used")
    print("package_local_integrity_reads: the proposed source note is read for claim-surface consistency; no runner cache is written")
    print("negative_scope: only direct identification of unequal restriction values with identical effect-only content is rejected; contextual content and formation-probability interpretations remain live")

    checks.check(
        "audit-input-paths",
        "declared audit inputs exist and match the note, axiom memo, Aug 10 parent, and Aug 12 barycenter parent",
        AUDIT_INPUT_PATHS == (
            "docs/RECORD_CONTENT_ONLY_SHARED_EFFECT_DESCENT_BOUNDED_THEOREM_NOTE_2026-08-12.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            "docs/ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-10.md",
            "docs/ADMISSIBILITY_BARYCENTER_EVALUATION_MENU_KERNEL_BOUNDED_THEOREM_NOTE_2026-08-12.md",
        )
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    )

    record_sentences = (
        "Only records are readable.",
        "A readout value is determined by record content alone.",
    )
    checks.check(
        "source-record-content-only",
        "the exact current content-only Record sentences are present",
        all(sentence in normalized_axiom for sentence in record_sentences),
    )
    record_section = axiom.split("### Record / Fixed Reality", 1)[1].split("## Qualification", 1)[0]
    checks.check(
        "record-premise-simplification",
        "the current Record section has the no-record sentence and no named scalar, additivity, or absence-value rule",
        "A site with no record cannot be read." in record_section
        and all(token not in record_section for token in ("I(", "I(empty)", "additiv", "scalar")),
    )
    checks.check(
        "source-aug10-restriction",
        "the Aug 10 parent states the shared-effect restriction witness and its masses",
        all(
            phrase in parent
            for phrase in (
                "Z=1/4+81/100+9/25+9/16+9/16=509/200",
                "K_nu(E_0|M_A)=(1/4)/(1/4+81/100+9/25)=25/142",
                "K_nu(E_0|M_B)=(1/4)/(1/4+9/16+9/16)=2/11",
            )
        ),
    )
    checks.check(
        "source-aug12-barycenter-scope",
        "the barycenter parent keeps an exact separate effect-functional grade live and distinguishes it from restriction",
        all(
            phrase in normalized_barycenter_parent
            for phrase in (
                "barycenter evaluation",
                "restriction is not this kernel",
                "The kernel is not a physical Record law.",
            )
        ),
    )

    z = (ZERO, ZERO, ONE)
    n1 = (rs2(Fraction(4, 9)), ZERO, q(Fraction(-7, 9)))
    n2 = (rs2(Fraction(-2, 3)), ZERO, q(Fraction(1, 3)))
    m1 = (rs2(Fraction(2, 3)), ZERO, q(Fraction(-1, 3)))
    m2 = (rs2(Fraction(-2, 3)), ZERO, q(Fraction(-1, 3)))

    e0 = Effect(Fraction(1, 2), z)
    a1 = Effect(Fraction(9, 10), n1)
    a2 = Effect(Fraction(3, 5), n2)
    b1 = Effect(Fraction(3, 4), m1)
    b2 = Effect(Fraction(3, 4), m2)
    menu_a = (e0, a1, a2)
    menu_b = (e0, b1, b2)

    checks.check(
        "ternary-menu-a",
        "the asymmetric shared-effect menu is an exact scaled-projector resolution",
        menu_is_resolution(menu_a),
    )
    checks.check(
        "ternary-menu-b",
        "the symmetric shared-effect menu is an exact scaled-projector resolution",
        menu_is_resolution(menu_b),
    )
    checks.check(
        "shared-effect-incidence",
        "the two menus share exactly E0 and otherwise contain distinct effects",
        set(menu_a).intersection(menu_b) == {e0} and len(set(menu_a).union(menu_b)) == 5,
    )

    coefficients = (e0.coefficient, a1.coefficient, a2.coefficient, b1.coefficient, b2.coefficient)
    atomic_masses = tuple(value * value for value in coefficients)
    atomic_normalization = sum(atomic_masses)
    checks.check(
        "atomic-global-normalization",
        "the five squared-trace atomic weights have exact normalization 509/200",
        atomic_normalization == Fraction(509, 200)
        and sum(mass / atomic_normalization for mass in atomic_masses) == 1,
        residual=atomic_normalization,
    )

    e0_square = e0.coefficient * e0.coefficient
    menu_a_square_sum = sum(effect.coefficient**2 for effect in menu_a)
    menu_b_square_sum = sum(effect.coefficient**2 for effect in menu_b)
    conditional_a = e0_square / menu_a_square_sum
    conditional_b = e0_square / menu_b_square_sum
    checks.check(
        "atomic-restriction-values",
        "normalized restriction recomputes to 25/142 on M_A and 2/11 on M_B",
        conditional_a == Fraction(25, 142) and conditional_b == Fraction(2, 11),
        residual=(conditional_a, conditional_b),
    )
    checks.check(
        "atomic-restriction-separation",
        "the same effect differs across the two menus by exactly -9/1562",
        conditional_a - conditional_b == Fraction(-9, 1562),
        residual=conditional_a - conditional_b,
    )

    content_eff_a = phi_eff("A", E0_MATRIX)
    content_eff_b = phi_eff("B", E0_MATRIX)
    checks.check(
        "effect-only-identical-content",
        "Phi_eff assigns the identical matrix E0 to both outcome pairs",
        content_eff_a == content_eff_b == E0_MATRIX,
        residual=(content_eff_a, content_eff_b),
    )
    checks.check(
        "restriction-not-direct-effect-only-readout",
        "two unequal restriction values cannot both be direct values of one function on identical Phi_eff content",
        conditional_a != conditional_b
        and content_eff_a == content_eff_b,
        residual=(conditional_a, conditional_b),
    )

    phi_a = phi_ctx("A", E0_MATRIX)
    phi_b = phi_ctx("B", E0_MATRIX)
    tag_a = context_tag(phi_a)
    tag_b = context_tag(phi_b)
    readout_a = context_readout(phi_a)
    readout_b = context_readout(phi_b)
    checks.check(
        "context-tags",
        "the two context-bearing matrices have exact tags 1 and 2",
        tag_a == Fraction(1) and tag_b == Fraction(2),
        residual=(tag_a, tag_b),
    )
    checks.check(
        "menu-context-distinct-content",
        "the menu-context records are distinct matrices in M_2(C)",
        phi_a != phi_b and phi_a != E0_MATRIX and phi_b != E0_MATRIX,
    )
    checks.check(
        "context-fixed-readout-values",
        "one fixed affine function of stored content returns exactly 25/142 and 2/11",
        readout_a == conditional_a == RESTRICTION_A
        and readout_b == conditional_b == RESTRICTION_B,
        residual=(readout_a, readout_b),
    )

    checks.check(
        "note-preserves-record-sentences",
        "the note quotes both current Record content-only sentences",
        all(sentence in normalized_note for sentence in record_sentences),
    )
    checks.check(
        "note-preserves-restriction-fractions",
        "the note records the recomputed restriction values 25/142 and 2/11",
        "25/142" in note and "2/11" in note and "509/200" in note,
    )
    checks.check(
        "note-links-parents",
        "the note links the axiom memo, Aug 10 type-separation note, and Aug 12 barycenter note",
        "MINIMAL_AXIOMS_2026-06-29.md" in note
        and "ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-10.md" in note
        and "ADMISSIBILITY_BARYCENTER_EVALUATION_MENU_KERNEL_BOUNDED_THEOREM_NOTE_2026-08-12.md" in note,
    )
    checks.check(
        "claim-type-contract",
        "the author hint uses the exact bounded-theorem enum",
        "**Type:** bounded_theorem" in note,
    )
    checks.check(
        "machine-status-contract",
        "the source uses the controlled bounded-support fields",
        all(
            phrase in note
            for phrase in (
                "actual_current_surface_status: bounded-support",
                "target_claim_type: bounded_theorem",
                "audit_required_before_effective_retained: true",
                "bare_retained_allowed: false",
                "hypothetical_axiom_status: \"no edit, adoption, minimality, or necessity claim\"",
                "next_trace_action:",
            )
        ),
    )
    checks.check(
        "post-simplification-note-contract",
        "the note disclaims removed Record premises and preserves the direct-value hypothesis",
        "It supplies no named scalar functional, no additivity rule, and no value for absence." in normalized_note
        and "direct readout values" in note
        and all(token not in note for token in ("I(empty)", "I ∘")),
    )
    checks.check(
        "no-go-discipline-contract",
        "the source carries N1 through N8 and the narrow gate disposition",
        all(f"### N{index}" in note for index in range(1, 9))
        and "PASS for Theorems 1–3 as narrowed" in note
        and "FAIL for the original" in note,
    )

    forbidden = ("new axiom", "we adopt", "promoted", "Codex")
    retained_hits = [
        line
        for line in note.splitlines()
        if "retained" in line
        and "audit_required_before_effective_retained" not in line
        and "bare_retained_allowed" not in line
    ]
    checks.check(
        "forbidden-rhetoric-absent",
        "the note avoids axiom-adoption, promotion, and executor-name rhetoric",
        all(phrase not in note for phrase in forbidden) and retained_hits == [],
        residual=retained_hits,
    )
    checks.check(
        "canonical-nonmutation",
        "the menu-context encoding is absent from the canonical axiom file",
        all(phrase not in axiom for phrase in ("Phi_ctx", "Φ_ctx", "alpha_M", "α_M")),
    )
    checks.check(
        "parent-objects-bound",
        "the Aug 10 parent still names the shared effect and both menus",
        all(
            phrase in normalized_parent
            for phrase in (
                "E_0=(1/2)P(z)",
                "M_A={E_0,(9/10)P(n_1),(3/5)P(n_2)}",
                "M_B={E_0,(3/4)P(m_1),(3/4)P(m_2)}",
            )
        ),
    )

    print("per_element: exact shared effect E0 is checked under identical Phi_eff content and distinct Phi_ctx content")
    print("per_site: one-site same-content substitution is checked; formation probabilities remain outside the direct-readout target")
    print("per_mode: checked and not executed — no spectral-mode or mode-exhaustion conclusion is part of the theorem")
    print("per_block: exactly two declared menus and the direct-readout identification are tested; other content maps remain live")
    print("lattice_wide: checked and not executed — no multi-site dynamics, formation law, or Born uniqueness is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
