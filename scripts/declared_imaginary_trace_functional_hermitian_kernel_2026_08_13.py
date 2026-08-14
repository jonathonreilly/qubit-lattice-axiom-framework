#!/usr/bin/env python3
"""Exact checks for a declared imaginary-trace functional on M_2(C).

The runner verifies that J(C)=Im Tr(C)/2 vanishes on Hermitian matrices,
that A(u)=iu 1 is an exact non-Hermitian right inverse, and that the current
Record axiom supplies neither J nor the retired scalar/additivity semantics.
No cache is written by this runner.
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
    / "DECLARED_IMAGINARY_TRACE_FUNCTIONAL_HERMITIAN_KERNEL_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/DECLARED_IMAGINARY_TRACE_FUNCTIONAL_HERMITIAN_KERNEL_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)


def normalize(text: str) -> str:
    return " ".join(text.split())


def section(text: str, start: str, end: str) -> str:
    """Extract a current source section, excluding later historical prose."""
    start_at = text.index(start) + len(start)
    end_at = text.index(end, start_at)
    return text[start_at:end_at]


@dataclass(frozen=True)
class ExactComplex:
    re: Fraction = Fraction(0)
    im: Fraction = Fraction(0)

    def __add__(self, other: "ExactComplex") -> "ExactComplex":
        return ExactComplex(self.re + other.re, self.im + other.im)

    def __sub__(self, other: "ExactComplex") -> "ExactComplex":
        return ExactComplex(self.re - other.re, self.im - other.im)

    def __neg__(self) -> "ExactComplex":
        return ExactComplex(-self.re, -self.im)

    def __mul__(self, other: "ExactComplex") -> "ExactComplex":
        return ExactComplex(
            self.re * other.re - self.im * other.im,
            self.re * other.im + self.im * other.re,
        )

    def conj(self) -> "ExactComplex":
        return ExactComplex(self.re, -self.im)


Matrix = tuple[
    tuple[ExactComplex, ExactComplex],
    tuple[ExactComplex, ExactComplex],
]


def matrix_add(left: Matrix, right: Matrix) -> Matrix:
    return (
        (left[0][0] + right[0][0], left[0][1] + right[0][1]),
        (left[1][0] + right[1][0], left[1][1] + right[1][1]),
    )


def matrix_scale(value: ExactComplex, matrix: Matrix) -> Matrix:
    return (
        (value * matrix[0][0], value * matrix[0][1]),
        (value * matrix[1][0], value * matrix[1][1]),
    )


def matrix_real_scale(value: Fraction, matrix: Matrix) -> Matrix:
    return matrix_scale(ExactComplex(value), matrix)


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


def matrix_trace(matrix: Matrix) -> ExactComplex:
    return matrix[0][0] + matrix[1][1]


def matrix_dagger(matrix: Matrix) -> Matrix:
    return (
        (matrix[0][0].conj(), matrix[1][0].conj()),
        (matrix[0][1].conj(), matrix[1][1].conj()),
    )


def is_hermitian(matrix: Matrix) -> bool:
    return matrix == matrix_dagger(matrix)


def declared_j(matrix: Matrix) -> Fraction:
    return matrix_trace(matrix).im / 2


def real_trace_half(matrix: Matrix) -> Fraction:
    return matrix_trace(matrix).re / 2


def unnormalized_imaginary_trace(matrix: Matrix) -> Fraction:
    return matrix_trace(matrix).im


def pairing(state: Matrix, effect: Matrix) -> ExactComplex:
    return matrix_trace(matrix_mul(state, effect))


def hermitian(p: Fraction, q: Fraction, r: Fraction, s: Fraction) -> Matrix:
    """((p,q+ir),(q-ir,s)), the universal four-real-parameter form."""
    return (
        (ExactComplex(p), ExactComplex(q, r)),
        (ExactComplex(q, -r), ExactComplex(s)),
    )


def antihermitian_center(value: Fraction) -> Matrix:
    return matrix_scale(ExactComplex(Fraction(0), value), IDENTITY)


ZERO: Matrix = (
    (ExactComplex(), ExactComplex()),
    (ExactComplex(), ExactComplex()),
)
IDENTITY: Matrix = (
    (ExactComplex(Fraction(1)), ExactComplex()),
    (ExactComplex(), ExactComplex(Fraction(1))),
)
SIGMA_X = hermitian(Fraction(0), Fraction(1), Fraction(0), Fraction(0))
SIGMA_Y = hermitian(Fraction(0), Fraction(0), Fraction(-1), Fraction(0))
SIGMA_Z = hermitian(Fraction(1), Fraction(0), Fraction(0), Fraction(-1))
RHO_STAR = matrix_real_scale(Fraction(1, 2), IDENTITY)
RHO_35 = hermitian(Fraction(3, 5), Fraction(0), Fraction(0), Fraction(2, 5))
E0 = hermitian(Fraction(1, 2), Fraction(0), Fraction(0), Fraction(0))

PARAMETER_SAMPLE = (
    (Fraction(0), Fraction(0), Fraction(0), Fraction(0)),
    (Fraction(2), Fraction(1), Fraction(3), Fraction(-5)),
    (Fraction(-7, 3), Fraction(5, 4), Fraction(-9, 2), Fraction(11, 5)),
    (Fraction(1), Fraction(-2), Fraction(4), Fraction(6)),
)
U_SAMPLE = (
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

    def check(
        self,
        label: str,
        statement: str,
        condition: bool,
        residual: object | None = None,
    ) -> None:
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
    normalized_note = normalize(note)
    record = section(
        axiom,
        "### Record / Fixed Reality",
        "## Qualification",
    )
    qubit = section(
        axiom,
        "### Qubit / Site Possibility",
        "### Admissibility / Local Constraint",
    )
    normalized_record = normalize(record)

    print("external_scientific_inputs: none; J and the Hermitian restriction are declared mathematical conditions")
    print("framework_role: current Qubit supplies M_2(C); current Record supplies no scalar functional or additivity")
    print("negative_scope: only maps into the Hermitian subspace under fixed J are excluded; five formal or physical route families remain live")

    checks.check(
        "audit-input-paths",
        "declared inputs are exactly the new note and current minimal-axiom memo",
        AUDIT_INPUT_PATHS
        == (
            "docs/DECLARED_IMAGINARY_TRACE_FUNCTIONAL_HERMITIAN_KERNEL_BOUNDED_THEOREM_NOTE_2026-08-13.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    )
    checks.check(
        "current-qubit-domain",
        "the extracted current Qubit section supplies the full one-site M_2(C) presentation",
        "full one-site possibility domain has algebraic presentation `M_2(C)`" in qubit,
    )
    current_record_sentences = (
        "Records form.",
        "When present, a record locks exactly one admissible local possibility.",
        "A readout value is determined by record content alone.",
        "A site with no record cannot be read.",
    )
    checks.check(
        "current-record-section",
        "the current Record block is isolated rather than mixed with historical removal prose",
        all(sentence in normalized_record for sentence in current_record_sentences),
        residual=normalized_record,
    )
    retired_needles = (
        "I(empty)",
        "finite additivity",
        "pairwise-disjoint records",
        "scalar readout `I`",
    )
    checks.check(
        "retired-record-semantics-absent",
        "the current Record block supplies no named scalar, additivity, or value at absence",
        all(needle not in record for needle in retired_needles),
        residual=[needle for needle in retired_needles if needle in record],
    )

    hermitian_sample = tuple(hermitian(*params) for params in PARAMETER_SAMPLE)
    checks.check(
        "universal-hermitian-form",
        "the four-parameter constructor is Hermitian and has real trace p+s",
        all(is_hermitian(matrix) for matrix in hermitian_sample)
        and all(
            matrix_trace(matrix) == ExactComplex(params[0] + params[3])
            for matrix, params in zip(hermitian_sample, PARAMETER_SAMPLE)
        ),
    )
    basis = (IDENTITY, SIGMA_X, SIGMA_Y, SIGMA_Z)
    checks.check(
        "hermitian-basis-kernel",
        "J vanishes on the real Pauli basis spanning the Hermitian subspace",
        all(is_hermitian(matrix) and declared_j(matrix) == 0 for matrix in basis),
    )
    checks.check(
        "hermitian-sample-kernel",
        "J vanishes on every exact four-parameter Hermitian control",
        all(declared_j(matrix) == 0 for matrix in hermitian_sample),
        residual=tuple(declared_j(matrix) for matrix in hermitian_sample),
    )

    recovered = tuple(declared_j(antihermitian_center(value)) for value in U_SAMPLE)
    checks.check(
        "antihermitian-right-inverse",
        "J(iu 1)=u exactly on the rational discriminator sample",
        recovered == U_SAMPLE,
        residual=recovered,
    )
    checks.check(
        "antihermitian-domain-split",
        "iu 1 is Hermitian only at zero and anti-Hermitian for every sampled nonzero u",
        is_hermitian(antihermitian_center(Fraction(0)))
        and all(
            not is_hermitian(antihermitian_center(value))
            and matrix_dagger(antihermitian_center(value))
            == matrix_scale(ExactComplex(Fraction(-1)), antihermitian_center(value))
            for value in U_SAMPLE
            if value != 0
        ),
    )
    checks.check(
        "right-inverse-injective",
        "distinct sampled u values give distinct matrices and distinct J values",
        len({antihermitian_center(value) for value in U_SAMPLE}) == len(U_SAMPLE)
        and len(set(recovered)) == len(U_SAMPLE),
    )

    shifted = tuple(matrix_add(E0, antihermitian_center(value)) for value in U_SAMPLE)
    checks.check(
        "hermitian-shift",
        "for Hermitian E0, J(E0+iu 1)=u and every nonzero shift is non-Hermitian",
        tuple(declared_j(matrix) for matrix in shifted) == U_SAMPLE
        and all(
            not is_hermitian(matrix)
            for matrix, value in zip(shifted, U_SAMPLE)
            if value != 0
        ),
    )
    hermitian_encoding = tuple(matrix_real_scale(value, IDENTITY) for value in U_SAMPLE)
    checks.check(
        "fixed-J-hermitian-obstruction",
        "the natural Hermitian encoding u 1 remains invisible to fixed J",
        all(is_hermitian(matrix) for matrix in hermitian_encoding)
        and tuple(declared_j(matrix) for matrix in hermitian_encoding)
        == tuple(Fraction(0) for _ in U_SAMPLE),
    )
    checks.check(
        "alternative-functional-escape",
        "Re Tr/2 reads u from Hermitian u 1, proving the negative does not cover other functionals",
        tuple(real_trace_half(matrix) for matrix in hermitian_encoding) == U_SAMPLE,
    )
    checks.check(
        "normalization-mutation",
        "dropping the factor 1/2 changes the anti-Hermitian recovery from u to 2u",
        all(
            unnormalized_imaginary_trace(antihermitian_center(value)) == 2 * value
            for value in U_SAMPLE
        )
        and unnormalized_imaginary_trace(antihermitian_center(Fraction(1, 2)))
        != Fraction(1, 2),
    )
    traceless_antihermitian = matrix_scale(ExactComplex(Fraction(0), Fraction(1)), SIGMA_Z)
    checks.check(
        "nonhermitian-not-sufficient-mutation",
        "a traceless anti-Hermitian matrix has J=0, so non-Hermiticity alone is not claimed sufficient",
        not is_hermitian(traceless_antihermitian)
        and declared_j(traceless_antihermitian) == 0,
    )

    pair_star = pairing(RHO_STAR, E0)
    pair_biased = pairing(RHO_35, E0)
    checks.check(
        "pairing-discriminator",
        "the two-argument trace pairing gives 1/4 and 3/10 while J of both densities is zero",
        pair_star == ExactComplex(Fraction(1, 4))
        and pair_biased == ExactComplex(Fraction(3, 10))
        and declared_j(RHO_STAR) == 0
        and declared_j(RHO_35) == 0,
        residual=(pair_star, pair_biased),
    )
    checks.check(
        "real-linearity",
        "J is additive and real-homogeneous on exact matrix controls",
        declared_j(matrix_add(antihermitian_center(Fraction(1, 4)), antihermitian_center(Fraction(1, 2))))
        == Fraction(3, 4)
        and declared_j(matrix_real_scale(Fraction(3), antihermitian_center(Fraction(1, 4))))
        == Fraction(3, 4)
        and declared_j(ZERO) == 0,
    )

    checks.check(
        "note-current-record-boundary",
        "the note explicitly denies that current Record supplies J, additivity, or a value at absence",
        all(
            phrase in normalized_note
            for phrase in (
                "does **not** supply a named scalar functional",
                "it does not supply `J`",
                "neither restores the retired scalar premise",
            )
        ),
    )
    checks.check(
        "note-proof-contract",
        "the note states the universal kernel, fixed-J corollary, and explicit anti-Hermitian escape",
        all(
            phrase in note
            for phrase in (
                "`H_2` is contained in `ker J`",
                "no map",
                "`A(u)=iu 1`",
                "The proof-obligation graph is acyclic",
            )
        ),
    )
    checks.check(
        "note-no-go-packet",
        "the committed note carries complete N1 through N8 headings and a narrow PASS disposition",
        all(f"### N{index}" in note for index in range(1, 9))
        and note.count("| ATTEMPTED |") >= 6
        and "No-Go Discipline status:** PASS for the narrow algebraic corollary" in note,
    )
    checks.check(
        "note-machine-trace",
        "the source carries complete bounded machine status without an audit verdict",
        all(
            phrase in note
            for phrase in (
                "actual_current_surface_status: bounded-support",
                "target_claim_type: bounded_theorem",
                "trace_class: negative_route_pruning",
                "audit_required_before_effective_retained: true",
                "bare_retained_allowed: false",
            )
        )
        and "audited_clean" not in note,
    )
    checks.check(
        "note-dependency-contract",
        "the only external scientific authority is the current minimal-axiom memo",
        note.count("](MINIMAL_AXIOMS_2026-06-29.md)") == 1
        and "upstream_dependencies:\n  - minimal_axioms" in note,
    )
    checks.check(
        "note-nonclaims",
        "the note keeps physical readout, writing, formation, and framework-wide no-go outside scope",
        all(
            phrase in note
            for phrase in (
                "supplies no Record scalar",
                "no universal physical no-go claim",
                "physical readout, writing process, formation site/rate",
            )
        ),
    )

    print("N5_CERTIFICATE:")
    print("per_element: checked — the proof covers every Hermitian 2x2 matrix, with exact rational mutation controls")
    print("per_site: checked — the theorem is exactly one-site M_2(C) algebra and asserts no composite-site lift")
    print("per_mode: checked and not executed — no spectral-mode, eigenmode, or momentum decomposition is claimed")
    print("per_block: checked — the Hermitian subspace and central anti-Hermitian line are separated explicitly")
    print("lattice_wide: checked and not executed — no lattice history, writing process, or global no-go is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
