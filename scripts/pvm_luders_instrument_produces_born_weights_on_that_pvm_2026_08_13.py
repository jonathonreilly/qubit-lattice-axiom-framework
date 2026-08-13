#!/usr/bin/env python3
"""Exact checks for the declared PVM Lüders matching note.

Identity gates call born_pvm(sigma, P) and luders(sigma, P). The runner
does not write a cache and does not edit axiom text.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "PVM_LUDERS_INSTRUMENT_PRODUCES_BORN_WEIGHTS_ON_THAT_PVM_"
    "BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
PARENT_PATH = ROOT / "docs" / (
    "BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_"
    "BOUNDED_THEOREM_NOTE_2026-08-09.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/PVM_LUDERS_INSTRUMENT_PRODUCES_BORN_WEIGHTS_ON_THAT_PVM_"
    "BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_"
    "BOUNDED_THEOREM_NOTE_2026-08-09.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Matrix = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]


def normalize(text: str) -> str:
    return " ".join(text.split())


def entry(value: int | Fraction) -> Fraction:
    return Fraction(value)


def mat(
    a00: int | Fraction,
    a01: int | Fraction,
    a10: int | Fraction,
    a11: int | Fraction,
) -> Matrix:
    return ((entry(a00), entry(a01)), (entry(a10), entry(a11)))


def mat_add(left: Matrix, right: Matrix) -> Matrix:
    return mat(
        left[0][0] + right[0][0],
        left[0][1] + right[0][1],
        left[1][0] + right[1][0],
        left[1][1] + right[1][1],
    )


def mat_scale(scalar: Fraction, value: Matrix) -> Matrix:
    return mat(
        scalar * value[0][0],
        scalar * value[0][1],
        scalar * value[1][0],
        scalar * value[1][1],
    )


def mat_mul(left: Matrix, right: Matrix) -> Matrix:
    return mat(
        left[0][0] * right[0][0] + left[0][1] * right[1][0],
        left[0][0] * right[0][1] + left[0][1] * right[1][1],
        left[1][0] * right[0][0] + left[1][1] * right[1][0],
        left[1][0] * right[0][1] + left[1][1] * right[1][1],
    )


def mat_trace(value: Matrix) -> Fraction:
    return value[0][0] + value[1][1]


def born_pvm(sigma: Matrix, projector: Matrix) -> Fraction:
    return mat_trace(mat_mul(sigma, projector))


def luders(sigma: Matrix, projector: Matrix) -> Matrix:
    weight = born_pvm(sigma, projector)
    if weight <= 0:
        raise ValueError("Lüders update is defined only for positive Born weight")
    return mat_scale(Fraction(1, 1) / weight, mat_mul(mat_mul(projector, sigma), projector))


def four_axioms_name_luders(axiom_text: str) -> bool:
    compact = normalize(axiom_text).casefold()
    return "lüders" in compact or "luders" in compact


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
    parent = PARENT_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")

    print(
        "external_scientific_inputs: current axiom wording and the 2026-08-09 "
        "frame-lift uniqueness note are source-bound; no observational or fitted inputs are used"
    )
    print(
        "package_local_integrity_reads: the proposed source note is read for "
        "claim-surface consistency; this dispatch writes no runner cache"
    )
    print(
        "identity_gate_contract: Born and repeatability identities call "
        "born_pvm(sigma, P) and luders(sigma, P)"
    )

    identity = mat(1, 0, 0, 1)
    projector_p = mat(1, 0, 0, 0)
    projector_q = mat(0, 0, 0, 1)
    rho_star = mat(Fraction(1, 2), 0, 0, Fraction(1, 2))
    rho = mat(Fraction(3, 5), 0, 0, Fraction(2, 5))
    sigma_mix = mat_scale(Fraction(1, 2), mat_add(rho, rho_star))

    admissibility_sentence = (
        "For each site, the probability distribution over the possibilities is "
        "determined by, and varies with, the nearest-neighbor conditions."
    )
    record_lock_sentence = (
        "When present, a record locks exactly one admissible local possibility."
    )
    record_additivity_sentence = (
        "For any finite collection of pairwise-disjoint records, scalar readout "
        "`I` is additive, with `I(empty)=0`."
    )

    checks.check(
        "source-admissibility",
        "the canonical memo states the nearest-neighbor determined distribution",
        admissibility_sentence in normalize(axiom),
    )
    checks.check(
        "source-record-lock",
        "the canonical memo states that a record locks one admissible possibility",
        record_lock_sentence in normalize(axiom),
    )
    checks.check(
        "source-record-additivity",
        "the canonical memo states finite additive scalar readout I",
        record_additivity_sentence in normalize(axiom),
    )
    checks.check(
        "source-parent",
        "the 2026-08-09 parent still states unique density-matrix trace form",
        all(
            phrase in parent
            for phrase in (
                "menu-independent grading",
                "There is a unique density matrix",
                "w(E)=Tr(rho E)",
            )
        ),
    )
    checks.check(
        "surface-status",
        "the note keeps conditional support, hypothetical axiom wording, and independent audit explicit",
        all(
            phrase in note
            for phrase in (
                "actual_current_surface_status: conditional-support",
                "hypothetical_axiom_status:",
                "Independent audit remains required",
                "no canonical axiom edit",
            )
        ),
    )
    checks.check(
        "quoted-axiom-sentences",
        "the note quotes the Admissibility and Record sentences used in Theorem 4",
        all(
            phrase in normalize(note).replace("> ", "")
            for phrase in (
                admissibility_sentence,
                record_lock_sentence,
                record_additivity_sentence,
            )
        ),
    )
    checks.check(
        "extra-matching-sentence",
        "the note states the extra matching that the instrument is a PVM Lüders readout",
        "the instrument is a PVM Lüders readout" in note,
    )
    checks.check(
        "pvm-resolution",
        "Q equals I-P and the declared pair sums to the identity",
        projector_q == mat_add(identity, mat_scale(Fraction(-1), projector_p))
        and mat_add(projector_p, projector_q) == identity,
    )
    checks.check(
        "mix-entries",
        "the midpoint mix is exactly diag(11/20, 9/20)",
        sigma_mix == mat(Fraction(11, 20), 0, 0, Fraction(9, 20)),
    )

    weight_star_p = born_pvm(rho_star, projector_p)
    weight_star_q = born_pvm(rho_star, projector_q)
    weight_rho_p = born_pvm(rho, projector_p)
    weight_rho_q = born_pvm(rho, projector_q)
    weight_mix_p = born_pvm(sigma_mix, projector_p)
    updated = luders(rho, projector_p)
    repeated = born_pvm(updated, projector_p)

    checks.check(
        "identity-born-star",
        "born_pvm(rho_*, P) equals 1/2 and the complementary weight completes to one",
        weight_star_p == Fraction(1, 2)
        and weight_star_q == Fraction(1, 2)
        and weight_star_p + weight_star_q == 1,
    )
    checks.check(
        "identity-born-rho",
        "born_pvm(rho, P) equals 3/5 and born_pvm(rho, Q) equals 2/5",
        weight_rho_p == Fraction(3, 5)
        and weight_rho_q == Fraction(2, 5)
        and weight_rho_p + weight_rho_q == 1,
    )
    checks.check(
        "identity-born-mix",
        "born_pvm(sigma_mix, P) equals 11/20 and matches the midpoint of the named weights",
        weight_mix_p == Fraction(11, 20)
        and weight_mix_p == (weight_rho_p + weight_star_p) / 2,
    )
    checks.check(
        "identity-luders-repeatability",
        "luders(rho, P) returns P and born_pvm of that update on P is 1",
        updated == projector_p and repeated == 1,
    )
    checks.check(
        "mutation-axioms-name-luders",
        "the predicate that the four axioms name Lüders fails",
        four_axioms_name_luders(axiom) is False,
    )
    checks.check(
        "mutation-constant-half",
        "replacing born_pvm(rho, P) by 1/2 disagrees with the live 3/5 identity",
        Fraction(1, 2) != born_pvm(rho, projector_p)
        and born_pvm(rho, projector_p) == Fraction(3, 5),
    )
    checks.check(
        "nonclaim-no-adoption",
        "the note refuses axiom adoption, parent replacement, Born-false, and every-kernel claims",
        all(
            phrase in note
            for phrase in (
                "does not adopt Lüders as an axiom",
                "does not claim that the 2026-08-09 frame-lift uniqueness",
                "does not claim that Born is false",
                "does not claim that every kernel is Born",
            )
        )
        and "we adopt" not in note.casefold()
        and "new axiom" not in note.casefold()
        and "l_phys" not in note.casefold()
        and "codex" not in note.casefold()
        and "purity-weighted" not in note.casefold(),
    )

    print(
        "per_element: exact Fraction traces and the Lüders product are checked "
        "on P, Q, and the named densities"
    )
    print(
        "per_site: one complete M_2(C) site and one declared two-outcome PVM "
        "are checked; no multi-site carrier is asserted"
    )
    print(
        "per_mode: only the declared computational-basis PVM is checked; "
        "no dimension-two frame reconstruction is launched"
    )
    print(
        "per_block: this matching block checks Born numbers, midpoint affinity, "
        "Lüders repeatability, and the extra-matching boundary together"
    )
    print(
        "lattice_wide: checked and not executed — the theorem is one-site "
        "matching algebra and makes no lattice-wide registration claim"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
