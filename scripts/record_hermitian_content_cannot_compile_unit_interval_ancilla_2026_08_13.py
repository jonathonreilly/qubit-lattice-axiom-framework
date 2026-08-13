#!/usr/bin/env python3
"""Exact checks: Hermitian content-only I cannot compile u in [0,1].

I = Im Tr/2 vanishes on every 2x2 Hermitian matrix and recovers u from
C_u = i u I. No cache is written.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    ROOT
    / "docs"
    / "RECORD_HERMITIAN_CONTENT_CANNOT_COMPILE_UNIT_INTERVAL_ANCILLA_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/RECORD_HERMITIAN_CONTENT_CANNOT_COMPILE_UNIT_INTERVAL_ANCILLA_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)


def normalize(text: str) -> str:
    return " ".join(text.split())


@dataclass(frozen=True)
class C:
    """Exact complex number with rational parts."""

    re: Fraction = Fraction(0)
    im: Fraction = Fraction(0)

    def __add__(self, other: "C") -> "C":
        return C(self.re + other.re, self.im + other.im)

    def __sub__(self, other: "C") -> "C":
        return C(self.re - other.re, self.im - other.im)

    def __neg__(self) -> "C":
        return C(-self.re, -self.im)

    def __mul__(self, other: "C") -> "C":
        return C(
            self.re * other.re - self.im * other.im,
            self.re * other.im + self.im * other.re,
        )

    def scale(self, value: Fraction) -> "C":
        return C(value * self.re, value * self.im)

    def conj(self) -> "C":
        return C(self.re, -self.im)


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


def matrix_real_scale(value: Fraction, matrix: Matrix) -> Matrix:
    return matrix_scale(C(value), matrix)


def matrix_mul(left: Matrix, right: Matrix) -> Matrix:
    return (
        (
            left[0][0] * right[0][0] + left[0][1] * right[1][0],
            left[0][0] * right[0][1] + left[0][1] * right[1][1],
        ),
        (
            left[1][0] * right[0][0] + left[1][1] * right[1][0],
            left[1][0] * right[0][1] + left[1][1] * right[1][1],
        ),
    )


def matrix_trace(matrix: Matrix) -> C:
    return matrix[0][0] + matrix[1][1]


def matrix_dagger(matrix: Matrix) -> Matrix:
    return (
        (matrix[0][0].conj(), matrix[1][0].conj()),
        (matrix[0][1].conj(), matrix[1][1].conj()),
    )


def is_hermitian(matrix: Matrix) -> bool:
    return matrix == matrix_dagger(matrix)


def content_readout(matrix: Matrix) -> Fraction:
    return matrix_trace(matrix).im / 2


def pairing(state: Matrix, effect: Matrix) -> C:
    return matrix_trace(matrix_mul(state, effect))


def hermitian_params(matrix: Matrix) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    """Four real parameters of a Hermitian matrix ((p, q+ir), (q-ir, s))."""
    return (
        matrix[0][0].re,
        matrix[0][1].re,
        matrix[0][1].im,
        matrix[1][1].re,
    )


def ancilla_content(value: Fraction) -> Matrix:
    """C_u = i u I."""
    return matrix_scale(C(Fraction(0), value), IDENTITY)


def labeled(effect: Matrix, value: Fraction) -> Matrix:
    """E + i u I."""
    return matrix_add(effect, ancilla_content(value))


ZERO: Matrix = (
    (C(), C()),
    (C(), C()),
)
IDENTITY: Matrix = (
    (C(Fraction(1)), C()),
    (C(), C(Fraction(1))),
)
SIGMA_X: Matrix = (
    (C(), C(Fraction(1))),
    (C(Fraction(1)), C()),
)
SIGMA_Y: Matrix = (
    (C(), C(Fraction(0), Fraction(-1))),
    (C(Fraction(0), Fraction(1)), C()),
)
SIGMA_Z: Matrix = (
    (C(Fraction(1)), C()),
    (C(), C(Fraction(-1))),
)
MIXED: Matrix = matrix_real_scale(Fraction(1, 2), IDENTITY)
RHO_35: Matrix = (
    (C(Fraction(3, 5)), C()),
    (C(), C(Fraction(2, 5))),
)
E0: Matrix = (
    (C(Fraction(1, 2)), C()),
    (C(), C()),
)
GENERIC_HERMITIAN: Matrix = (
    (C(Fraction(2)), C(Fraction(1), Fraction(3))),
    (C(Fraction(1), Fraction(-3)), C(Fraction(-5))),
)

HERMITIAN_SAMPLE: tuple[Matrix, ...] = (
    ZERO,
    IDENTITY,
    SIGMA_X,
    SIGMA_Y,
    SIGMA_Z,
    MIXED,
    RHO_35,
    E0,
    GENERIC_HERMITIAN,
    matrix_add(matrix_real_scale(Fraction(2), SIGMA_X), matrix_real_scale(Fraction(-3), SIGMA_Z)),
)

ANCILLA_SAMPLE: tuple[Fraction, ...] = (
    Fraction(0),
    Fraction(1, 5),
    Fraction(1, 4),
    Fraction(1, 2),
    Fraction(3, 5),
    Fraction(1),
)


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
    normalized_note = normalize(note).replace("> ", "")
    normalized_axiom = normalize(axiom)

    print("external_scientific_inputs: current Record wording is source-bound; no observational or fitted inputs are used")
    print("package_local_integrity_reads: the proposed source note is read for claim-surface consistency; no runner cache is written")
    print("negative_scope: only Hermitian content under I=Im Tr/2 is silent for u; non-Hermitian C_u remains a live formal escape")

    checks.check(
        "audit-input-paths",
        "declared audit inputs exist and match the note and axiom memo",
        AUDIT_INPUT_PATHS
        == (
            "docs/RECORD_HERMITIAN_CONTENT_CANNOT_COMPILE_UNIT_INTERVAL_ANCILLA_BOUNDED_THEOREM_NOTE_2026-08-13.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    )

    record_sentences = (
        "Records form.",
        "A readout value is determined by record content alone.",
        "I(empty)=0",
    )
    checks.check(
        "source-record-sentences",
        "the axiom memo pins Records form, content alone, and I(empty)=0",
        all(sentence in normalized_axiom for sentence in record_sentences)
        and "content alone" in normalized_axiom,
    )

    hermitian_ok = all(is_hermitian(matrix) for matrix in HERMITIAN_SAMPLE)
    i_on_hermitian = tuple(content_readout(matrix) for matrix in HERMITIAN_SAMPLE)
    checks.check(
        "hermitian-sample-closed",
        "the declared sample matrices are Hermitian, including the Pauli basis and a generic four-parameter matrix",
        hermitian_ok
        and is_hermitian(GENERIC_HERMITIAN)
        and hermitian_params(GENERIC_HERMITIAN) == (Fraction(2), Fraction(1), Fraction(3), Fraction(-5)),
        residual=hermitian_params(GENERIC_HERMITIAN),
    )
    checks.check(
        "hermitian-I-vanishes",
        "I=Im Tr/2 is identically 0 on the Hermitian sample",
        i_on_hermitian == tuple(Fraction(0) for _ in HERMITIAN_SAMPLE),
        residual=i_on_hermitian,
    )

    combo = matrix_add(
        matrix_add(matrix_real_scale(Fraction(3), IDENTITY), matrix_real_scale(Fraction(-1), SIGMA_X)),
        matrix_add(matrix_real_scale(Fraction(2), SIGMA_Y), matrix_real_scale(Fraction(4), SIGMA_Z)),
    )
    checks.check(
        "four-parameter-span",
        "a real combination of I, sigma_x, sigma_y, sigma_z is Hermitian with I=0 and four independent parameters",
        is_hermitian(combo)
        and content_readout(combo) == 0
        and hermitian_params(combo) == (Fraction(7), Fraction(-1), Fraction(-2), Fraction(-1))
        and len(set(hermitian_params(GENERIC_HERMITIAN))) == 4,
        residual=hermitian_params(combo),
    )

    density_readouts = (
        content_readout(MIXED),
        content_readout(RHO_35),
        content_readout(matrix_real_scale(Fraction(1), ((C(Fraction(1)), C()), (C(), C())))),
    )
    checks.check(
        "density-I-independent",
        "I(rho)=0 for I/2, diag(3/5,2/5), and P(z), independently of rho",
        density_readouts == (Fraction(0), Fraction(0), Fraction(0))
        and matrix_trace(MIXED) == C(Fraction(1))
        and matrix_trace(RHO_35) == C(Fraction(1)),
        residual=density_readouts,
    )

    pair_mixed = pairing(MIXED, E0)
    pair_biased = pairing(RHO_35, E0)
    checks.check(
        "pairing-not-record-I",
        "Newton/Born pairing Tr(rho E0) is 1/4 and 3/10, not the Record I of those densities",
        pair_mixed == C(Fraction(1, 4))
        and pair_biased == C(Fraction(3, 10))
        and pair_mixed.im == 0
        and pair_biased.im == 0
        and pair_mixed.re != content_readout(MIXED)
        and pair_biased.re != content_readout(RHO_35),
        residual=(pair_mixed, pair_biased),
    )

    i_times_identity = ancilla_content(Fraction(1))
    i_times_generic = matrix_scale(C(Fraction(0), Fraction(1)), GENERIC_HERMITIAN)
    checks.check(
        "I-sees-i-hermitian",
        "I does not vanish on i times Hermitian: I(i I)=1 and I(i H)=Tr(H)/2",
        content_readout(i_times_identity) == 1
        and content_readout(i_times_generic) == matrix_trace(GENERIC_HERMITIAN).re / 2
        and not is_hermitian(i_times_identity)
        and not is_hermitian(i_times_generic),
        residual=(
            content_readout(i_times_identity),
            content_readout(i_times_generic),
            matrix_trace(GENERIC_HERMITIAN),
        ),
    )

    recovered = tuple(content_readout(ancilla_content(value)) for value in ANCILLA_SAMPLE)
    hermitian_labels = tuple(content_readout(matrix_real_scale(value, IDENTITY)) for value in ANCILLA_SAMPLE)
    nonhermitian = tuple(
        not is_hermitian(ancilla_content(value)) for value in ANCILLA_SAMPLE if value != 0
    )
    checks.check(
        "ancilla-Cu-recovers-u",
        "I(i u I)=u on the exact sample u in {0,1/5,1/4,1/2,3/5,1}",
        recovered == ANCILLA_SAMPLE,
        residual=recovered,
    )
    checks.check(
        "ancilla-Cu-nonhermitian",
        "C_u is non-Hermitian for every sampled u in (0,1] and Hermitian only at u=0",
        all(nonhermitian)
        and is_hermitian(ancilla_content(Fraction(0)))
        and ancilla_content(Fraction(1, 2)) == matrix_dagger(ancilla_content(Fraction(-1, 2))),
    )
    checks.check(
        "hermitian-label-silent",
        "the Hermitian competitor u I has I=0 for every sampled u, so it does not store the ancilla",
        hermitian_labels == tuple(Fraction(0) for _ in ANCILLA_SAMPLE)
        and all(is_hermitian(matrix_real_scale(value, IDENTITY)) for value in ANCILLA_SAMPLE),
        residual=hermitian_labels,
    )

    labeled_recovered = tuple(content_readout(labeled(E0, value)) for value in ANCILLA_SAMPLE)
    labeled_nonhermitian = tuple(
        not is_hermitian(labeled(E0, value)) for value in ANCILLA_SAMPLE if value != 0
    )
    checks.check(
        "label-E-plus-iuI",
        "I(E0 + i u I)=u while I(E0)=0, so the non-Hermitian label stores u",
        labeled_recovered == ANCILLA_SAMPLE
        and content_readout(E0) == 0
        and all(labeled_nonhermitian)
        and is_hermitian(labeled(E0, Fraction(0))),
        residual=labeled_recovered,
    )

    u_left = Fraction(1, 4)
    u_right = Fraction(1, 2)
    checks.check(
        "readout-additivity",
        "I is additive, real-homogeneous, and vanishes on the zero matrix",
        content_readout(matrix_add(ancilla_content(u_left), ancilla_content(u_right)))
        == u_left + u_right
        and content_readout(matrix_real_scale(Fraction(3), ancilla_content(u_left))) == 3 * u_left
        and content_readout(ZERO) == 0
        and content_readout(matrix_add(GENERIC_HERMITIAN, ancilla_content(u_right))) == u_right,
        residual=(
            content_readout(matrix_add(ancilla_content(u_left), ancilla_content(u_right))),
            content_readout(ZERO),
        ),
    )

    checks.check(
        "hermitian-cannot-separate-u",
        "I is constant on Hermitian content, so it cannot inject [0,1]",
        len(set(i_on_hermitian)) == 1
        and i_on_hermitian[0] == 0
        and len(set(recovered)) == len(ANCILLA_SAMPLE),
    )

    fiber_mixed = pair_mixed.re
    fiber_biased = pair_biased.re
    checks.check(
        "fiber-length-is-pairing",
        "reconstructed [0,1] fiber lengths are Tr(rho E0), not I(rho)",
        fiber_mixed == Fraction(1, 4)
        and fiber_biased == Fraction(3, 10)
        and fiber_mixed != content_readout(MIXED)
        and fiber_biased != content_readout(RHO_35),
        residual=(fiber_mixed, fiber_biased),
    )

    checks.check(
        "note-preserves-record-sentences",
        "the note quotes Records form, content alone, and I(empty)=0",
        all(sentence in normalized_note for sentence in record_sentences)
        and "content alone" in normalized_note
        and "Records form" in note,
    )
    checks.check(
        "note-links-axioms",
        "the note links the current axiom memo",
        "MINIMAL_AXIOMS_2026-06-29.md" in note,
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
                'hypothetical_axiom_status: "no edit"',
            )
        ),
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
        "the C_u encoding is absent from the canonical axiom file",
        all(
            phrase not in axiom
            for phrase in ("C_u", "i u I", "unit-interval ancilla", "Im Tr(C)/2")
        ),
    )

    print("per_element: Hermitian sample, C_u, and E0+i u I are evaluated under I=Im Tr/2")
    print("per_site: the identities are one-site 2x2 statements; no composite carrier is asserted")
    print("per_mode: no spectral-mode exhaustion is claimed")
    print("per_block: only Hermitian silence versus non-Hermitian storage of u is tested")
    print("lattice_wide: checked and not executed — no lattice-wide dynamics or Born uniqueness is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
