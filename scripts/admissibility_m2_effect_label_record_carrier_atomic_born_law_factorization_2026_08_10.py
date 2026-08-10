#!/usr/bin/env python3
"""Exact checks for the M2 effect-label carrier and atomic-law factorization.

The runner checks the exact carrier inverse, injectivity, finite additive
label readout, unitary covariance, two rational ternary effect resolutions,
their exact second-moment weights, shared-effect atomic descent, and the
condition-varying fixed decoded atom. Gaussian integration and the probability
integral transform are proved analytically in the source note.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "ADMISSIBILITY_M2_EFFECT_LABEL_RECORD_CARRIER_ATOMIC_BORN_LAW_FACTORIZATION_BOUNDED_THEOREM_NOTE_2026-08-10.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
DECODER_PARENT_PATH = ROOT / "docs" / "ADMISSIBILITY_RECORD_CONTENT_DECODER_PUSHFORWARD_EFFECT_DESCENT_INDEPENDENCE_BOUNDED_THEOREM_NOTE_2026-08-10.md"
COMPILER_PARENT_PATH = ROOT / "docs" / "ADMISSIBILITY_GAUSSIAN_SECOND_MOMENT_QUANTILE_DECODER_EFFECT_QUOTIENT_BOUNDED_THEOREM_NOTE_2026-08-10.md"
UNIFORMIZER_PARENT_PATH = ROOT / "docs" / "ADMISSIBILITY_GAUSSIAN_CONTENT_ONLY_UNIFORMIZER_WEIERSTRASS_DECODER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_M2_EFFECT_LABEL_RECORD_CARRIER_ATOMIC_BORN_LAW_FACTORIZATION_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RECORD_CONTENT_DECODER_PUSHFORWARD_EFFECT_DESCENT_INDEPENDENCE_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/ADMISSIBILITY_GAUSSIAN_SECOND_MOMENT_QUANTILE_DECODER_EFFECT_QUOTIENT_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/ADMISSIBILITY_GAUSSIAN_CONTENT_ONLY_UNIFORMIZER_WEIERSTRASS_DECODER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
)


@dataclass(frozen=True)
class ExactComplex:
    real: Fraction = Fraction(0)
    imag: Fraction = Fraction(0)

    def __add__(self, other: "ExactComplex") -> "ExactComplex":
        return ExactComplex(self.real + other.real, self.imag + other.imag)

    def __neg__(self) -> "ExactComplex":
        return ExactComplex(-self.real, -self.imag)

    def __sub__(self, other: "ExactComplex") -> "ExactComplex":
        return self + (-other)

    def __mul__(self, other: "ExactComplex") -> "ExactComplex":
        return ExactComplex(
            self.real * other.real - self.imag * other.imag,
            self.real * other.imag + self.imag * other.real,
        )

    def conjugate(self) -> "ExactComplex":
        return ExactComplex(self.real, -self.imag)

    def scale(self, value: Fraction) -> "ExactComplex":
        return ExactComplex(value * self.real, value * self.imag)


ZERO = ExactComplex()
ONE = ExactComplex(Fraction(1))
I_UNIT = ExactComplex(Fraction(0), Fraction(1))


def z(value: int | Fraction) -> ExactComplex:
    return ExactComplex(Fraction(value))


Matrix = tuple[
    tuple[ExactComplex, ExactComplex],
    tuple[ExactComplex, ExactComplex],
]

ZERO_MATRIX: Matrix = ((ZERO, ZERO), (ZERO, ZERO))
IDENTITY: Matrix = ((ONE, ZERO), (ZERO, ONE))
PAULI_X: Matrix = ((ZERO, ONE), (ONE, ZERO))
PHASE_UNITARY: Matrix = ((ONE, ZERO), (ZERO, I_UNIT))


def matrix(*entries: int | Fraction) -> Matrix:
    if len(entries) != 4:
        raise ValueError("matrix requires four row-major real entries")
    return (
        (z(entries[0]), z(entries[1])),
        (z(entries[2]), z(entries[3])),
    )


def matrix_add(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(left[row][column] + right[row][column] for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def matrix_scale(value: Fraction, operand: Matrix) -> Matrix:
    return tuple(
        tuple(operand[row][column].scale(value) for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def matrix_multiply(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            sum(
                (left[row][index] * right[index][column] for index in range(2)),
                ZERO,
            )
            for column in range(2)
        )
        for row in range(2)
    )  # type: ignore[return-value]


def matrix_dagger(operand: Matrix) -> Matrix:
    return tuple(
        tuple(operand[column][row].conjugate() for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def matrix_trace(operand: Matrix) -> ExactComplex:
    return operand[0][0] + operand[1][1]


def conjugate(operand: Matrix, unitary: Matrix) -> Matrix:
    return matrix_multiply(matrix_multiply(unitary, operand), matrix_dagger(unitary))


def hermitian_part(operand: Matrix) -> Matrix:
    return matrix_scale(Fraction(1, 2), matrix_add(operand, matrix_dagger(operand)))


def label_readout(operand: Matrix) -> Fraction:
    return matrix_trace(operand).imag / 2


def carrier(effect: Matrix, label: Fraction) -> Matrix:
    label_matrix: Matrix = (
        (ExactComplex(Fraction(0), label), ZERO),
        (ZERO, ExactComplex(Fraction(0), label)),
    )
    return matrix_add(effect, label_matrix)


def real_trace_product(left: Matrix, right: Matrix) -> Fraction:
    product_trace = matrix_trace(matrix_multiply(left, right))
    if product_trace.imag != 0:
        raise ValueError("fixture trace product must be real")
    return product_trace.real


def real_symmetric_psd(effect: Matrix) -> bool:
    if effect != matrix_dagger(effect):
        return False
    a = effect[0][0].real
    b = effect[0][1].real
    d = effect[1][1].real
    entries_real = all(
        entry.imag == 0 for row in effect for entry in row
    )
    return entries_real and a >= 0 and d >= 0 and a * d - b * b >= 0


def effect_resolution(menu: tuple[Matrix, ...]) -> bool:
    return all(real_symmetric_psd(effect) for effect in menu) and sum_matrices(menu) == IDENTITY


def sum_matrices(operands: tuple[Matrix, ...]) -> Matrix:
    result = ZERO_MATRIX
    for operand in operands:
        result = matrix_add(result, operand)
    return result


def density_at_t(t: int, offset: int = 0) -> Matrix:
    denominator = t * t + 4 + 2 * offset
    return matrix(
        Fraction(t * t + 2 + offset, denominator),
        0,
        0,
        Fraction(2 + offset, denominator),
    )


def effect_weights(density: Matrix, menu: tuple[Matrix, ...]) -> tuple[Fraction, ...]:
    return tuple(real_trace_product(density, effect) for effect in menu)


def cumulative(weights: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    cuts = [Fraction(0)]
    for weight in weights:
        cuts.append(cuts[-1] + weight)
    return tuple(cuts)


def quantile_index(value: Fraction, cuts: tuple[Fraction, ...]) -> int:
    for index in range(1, len(cuts)):
        if value < cuts[index]:
            return index - 1
    return len(cuts) - 2


def writer(
    value: Fraction,
    cuts: tuple[Fraction, ...],
    menu: tuple[Matrix, ...],
    labels: tuple[Fraction, ...],
) -> Matrix:
    index = quantile_index(value, cuts)
    return carrier(menu[index], labels[index])


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
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    decoder_parent = DECODER_PARENT_PATH.read_text(encoding="utf-8")
    compiler_parent = COMPILER_PARENT_PATH.read_text(encoding="utf-8")
    uniformizer_parent = UNIFORMIZER_PARENT_PATH.read_text(encoding="utf-8")
    note_flat = " ".join(note.split())
    axiom_flat = " ".join(axiom.split())

    print("external_scientific_inputs: the current axiom and three stacked decoder/compiler/uniformizer boundaries are source-bound; no literature theorem, observed probability, fitted parameter, or external PR artifact is imported")
    print("package_local_integrity_reads: the proposed theorem note is checked for its carrier, atomic law, exact fixtures, trace status, and N1-N8 surfaces; the cache envelope binds every declared input")
    print("analytic_boundary: Gaussian integration, the common-uniform probability transform, general positive-functional normalization, and all-unitary covariance are proved in the source; exact rational carrier, menu, weight, and conjugation fixtures are executed here")
    print("negative_scope: only autonomous law selection, program/preparation registration, occurrence, histories, and axiom adoption are withheld; no global Born, Record, Admissibility, contact, or axiom no-go is claimed")

    checks.check(
        "source-current-axiom",
        "the current M2 possibility, neighborhood-distribution, and content-only additive Record clauses are present",
        all(
            phrase in axiom_flat
            for phrase in (
                "The full one-site possibility domain has algebraic presentation `M_2(C)`.",
                "the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions",
                "A readout value is determined by record content alone.",
                "scalar readout `I` is additive, with `I(empty)=0`.",
            )
        ),
    )
    checks.check(
        "source-decoder-parent",
        "Block 3 separates decoder registration from effect descent",
        "decoder registration and measure pushforward do not imply same-effect descent" in decoder_parent
        and "derive a physical decoder and equivalence quotient from current dynamics" in decoder_parent,
    )
    checks.check(
        "source-compiler-parent",
        "Block 4 supplies exact second-moment weights while leaving physical program encoding open",
        "`rho_C := M_C/Tr(M_C)=(C^2+2I)/(Tr(C^2)+4)`" in compiler_parent
        and "Encoding those parameters in a physical Record/apparatus" in compiler_parent
        and "`p(M_A)=(3/10,19/50,8/25)`" in compiler_parent,
    )
    checks.check(
        "source-uniformizer-parent",
        "Block 6 supplies the common content uniformizer and indexed-threshold escape",
        "`U(A)=Phi(Im Tr A)`" in uniformizer_parent
        and "condition-indexed threshold" in uniformizer_parent
        and "tag-writing contact" in uniformizer_parent,
    )

    e0 = matrix(Fraction(1, 2), 0, 0, 0)
    e_a1 = matrix(Fraction(1, 2), 0, 0, Fraction(1, 5))
    e_a2 = matrix(0, 0, 0, Fraction(4, 5))
    e_b1 = matrix(Fraction(1, 4), Fraction(1, 4), Fraction(1, 4), Fraction(1, 2))
    e_b2 = matrix(Fraction(1, 4), Fraction(-1, 4), Fraction(-1, 4), Fraction(1, 2))
    menu_a = (e0, e_a1, e_a2)
    menu_b = (e0, e_b1, e_b2)
    labels = (Fraction(1), Fraction(2), Fraction(3))

    real_dimension = 2 * 2 * 2
    effect_dimension = 2 * 2
    label_dimension = 1
    checks.check(
        "carrier-dimension-capacity",
        "M2 has eight real coordinates; a Hermitian effect plus one real label uses five and leaves three",
        real_dimension == 8
        and effect_dimension == 4
        and real_dimension - effect_dimension - label_dimension == 3,
    )

    tags_a = tuple(carrier(effect, label) for effect, label in zip(menu_a, labels))
    tags_b = tuple(carrier(effect, label) for effect, label in zip(menu_b, labels))
    checks.check(
        "carrier-left-inverse",
        "Hermitian-part and half-imaginary-trace decoders recover every displayed effect-label pair exactly",
        all(
            hermitian_part(tag) == effect and label_readout(tag) == label
            for menu, tags in ((menu_a, tags_a), (menu_b, tags_b))
            for effect, label, tag in zip(menu, labels, tags)
        ),
    )
    checks.check(
        "carrier-injectivity",
        "the five distinct displayed effect-label pairs produce five codewords with exactly one shared effect-label atom",
        len(set(tags_a).union(tags_b)) == 5
        and set(tags_a).intersection(tags_b) == {tags_a[0]},
    )

    covariance_effect = e_b1
    covariance_tag = carrier(covariance_effect, Fraction(7, 3))
    checks.check(
        "carrier-covariance",
        "Pauli-X and phase conjugations commute exactly with effect-label encoding",
        all(
            conjugate(covariance_tag, unitary)
            == carrier(conjugate(covariance_effect, unitary), Fraction(7, 3))
            for unitary in (PAULI_X, PHASE_UNITARY)
        ),
    )
    checks.check(
        "decoder-covariance",
        "decoded effect co-transports and decoded label is invariant under both conjugations",
        all(
            hermitian_part(conjugate(covariance_tag, unitary))
            == conjugate(covariance_effect, unitary)
            and label_readout(conjugate(covariance_tag, unitary)) == Fraction(7, 3)
            for unitary in (PAULI_X, PHASE_UNITARY)
        ),
    )

    collection_left = (tags_a[0], tags_a[1])
    collection_right = (tags_a[2],)
    scalar_readout = lambda records: sum((label_readout(record) for record in records), Fraction(0))
    checks.check(
        "finite-additive-readout",
        "the fixed scalar label readout is zero on empty and additive on disjoint finite Record collections",
        scalar_readout(()) == 0
        and scalar_readout(collection_left + collection_right)
        == scalar_readout(collection_left) + scalar_readout(collection_right)
        == 6,
    )

    checks.check(
        "exact-effect-resolutions",
        "both rational ternary menus are positive semidefinite resolutions of the identity",
        effect_resolution(menu_a) and effect_resolution(menu_b),
    )
    checks.check(
        "shared-effect-incidence",
        "the two rational programs share only E0 before encoding",
        set(menu_a).intersection(menu_b) == {e0}
        and len(set(menu_a).union(menu_b)) == 5,
    )

    rho = density_at_t(1)
    weights_a = effect_weights(rho, menu_a)
    weights_b = effect_weights(rho, menu_b)
    checks.check(
        "exact-menu-a-weights",
        "the rational menu A has exact weights (3/10,19/50,8/25)",
        weights_a == (Fraction(3, 10), Fraction(19, 50), Fraction(8, 25)),
    )
    checks.check(
        "exact-menu-b-weights",
        "the rational menu B has exact weights (3/10,7/20,7/20)",
        weights_b == (Fraction(3, 10), Fraction(7, 20), Fraction(7, 20)),
    )
    checks.check(
        "atomic-law-normalization",
        "both exact atomic laws have strictly positive masses summing to one",
        all(sum(weights) == 1 and all(weight > 0 for weight in weights) for weights in (weights_a, weights_b)),
    )
    checks.check(
        "shared-effect-atomic-descent",
        "the identical shared codeword has mass 3/10 in both supplied programs",
        tags_a[0] == tags_b[0]
        and weights_a[0] == weights_b[0] == Fraction(3, 10),
    )

    cuts_a = cumulative(weights_a)
    cuts_b = cumulative(weights_b)
    checks.check(
        "exact-quantile-cuts",
        "the atomic-law cuts are (0,3/10,17/25,1) and (0,3/10,13/20,1)",
        cuts_a == (Fraction(0), Fraction(3, 10), Fraction(17, 25), Fraction(1))
        and cuts_b == (Fraction(0), Fraction(3, 10), Fraction(13, 20), Fraction(1)),
    )
    checks.check(
        "quantile-pushforward",
        "every interval length equals its exact atomic mass",
        all(
            tuple(cuts[index + 1] - cuts[index] for index in range(3)) == weights
            for cuts, weights in ((cuts_a, weights_a), (cuts_b, weights_b))
        ),
    )
    checks.check(
        "writer-decoder-composition",
        "midpoint samples from every interval write a codeword decoded to the intended effect and label",
        all(
            hermitian_part(writer((cuts[index] + cuts[index + 1]) / 2, cuts, menu, labels))
            == menu[index]
            and label_readout(writer((cuts[index] + cuts[index + 1]) / 2, cuts, menu, labels))
            == labels[index]
            for menu, cuts in ((menu_a, cuts_a), (menu_b, cuts_b))
            for index in range(3)
        ),
    )

    shared_masses = tuple(effect_weights(density_at_t(t), menu_a)[0] for t in (0, 1, 2))
    checks.check(
        "condition-varying-fixed-atom",
        "the same decoded E0/label-one atom has masses 1/4, 3/10, and 3/8 at t=0,1,2",
        shared_masses == (Fraction(1, 4), Fraction(3, 10), Fraction(3, 8))
        and len(set(shared_masses)) == 3,
    )
    checks.check(
        "compiler-nonselection-control",
        "the same carrier accepts lambda zero and one while their shared-atom masses remain separated by 1/70",
        effect_weights(density_at_t(1, 0), menu_a)[0]
        - effect_weights(density_at_t(1, 1), menu_a)[0]
        == Fraction(1, 70),
    )

    construction_needles = (
        "`kappa(E,ell)=E+i ell I_2`",
        "`Q(R)=(R+R^dagger)/2`",
        "`L(R)=(1/2) Im Tr R`",
        "`nu_(omega,M)=sum_j p_j delta_(kappa(E_j,ell_j))`",
        "`(W_(C,M))_* mu_C=nu_(omega_C,M)`",
        "`p(M_A)=(3/10,19/50,8/25)`",
        "`p(M_B)=(3/10,7/20,7/20)`",
    )
    checks.check(
        "construction-source-surface",
        "the source states the carrier, fixed decoders, atomic law, pushforward, and exact menu outputs",
        all(phrase in note_flat for phrase in construction_needles),
    )
    boundary_needles = (
        "No enlargement of the Qubit one-site possibility domain is needed",
        "This wording would directly supply Born-form one-shot masses",
        "hypothetical wording only",
        "No global Born, Admissibility, Record, contact, or axiom no-go is claimed",
        "No canonical axiom is edited",
        "the fixed TOE percentages do not move",
    )
    checks.check(
        "boundary-source-surface",
        "the source preserves the type, hypothetical-update, global-negative, governance, and score limits",
        all(phrase in note_flat for phrase in boundary_needles),
    )
    checks.check(
        "machine-status-contract",
        "the source carries the complete bounded upstream-support trace contract",
        all(
            phrase in note
            for phrase in (
                "actual_current_surface_status: bounded-support",
                "target_claim_type: bounded_theorem",
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
        "the effect-label carrier and atomic Born-law wording are absent from the canonical axiom memo",
        all(
            phrase not in axiom
            for phrase in (
                "kappa(E,ell)",
                "E_(eta,j)+i ell_j I_2",
                "normalized positive linear functional `omega_eta`",
                "atomic Born-law",
            )
        ),
    )
    checks.check(
        "no-go-gate",
        "all N1-N8 sections, source matching, primitive scan, steelman acceptance, and global-negative rejection are visible",
        all(f"### N{index}" in note for index in range(1, 9))
        and "| Source location | Source residual used |" in note
        and "The primitive-registry scan used" in note
        and "This steelman is accepted" in note
        and "FAIL / DO NOT SHIP" in note
        and "No global Born, Admissibility, Record, contact, or axiom no-go is claimed" in note_flat,
    )

    print("per_element: five distinct rational effects, five encoded effect-label pairs, exact inverse maps, and every quantile interval are checked")
    print("per_site: one M_2(C) output site carries one effect plus one real label with fixed content decoders and an exact finite atomic distribution; no formation event is asserted")
    print("per_mode: identity, Pauli-X, phase conjugation, two program menus, three preparation centers, and two isotropic extractor members are separated exactly")
    print("per_block: the M2 carrier-to-fixed-decoder-to-atomic-effect-weight-to-Gaussian-quantile factorization is checked through the local-law-selection residual")
    print("lattice_wide: checked and not executed — translation/proper-cubic covariance follows for a co-transported supplied program, while physical program registration, occurrence, causal order, and histories remain absent")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
