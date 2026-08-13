#!/usr/bin/env python3
"""Exact checks: two kernels on one menu; K is not lock content.

Same menu, same density, same formed lock of content A. The trace kernel and
the half-threshold step kernel disagree. Live Record names the lock label A
from content alone, not a kernel number.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "TWO_KERNELS_ONE_MENU_K_IS_NOT_LOCK_CONTENT_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/TWO_KERNELS_ONE_MENU_K_IS_NOT_LOCK_CONTENT_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

CONTENT_ALONE = "A readout value is determined by record content alone."
LOCKS_ONE = "a record locks exactly one admissible local possibility"


Matrix = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]


def normalize(text: str) -> str:
    return " ".join(text.split())


def governing_record_section(note: str) -> str:
    """Live Record axiom only; exclude historical discussion."""
    try:
        section = note.split("### Record / Fixed Reality", 1)[1]
        section = section.split("## Qualification", 1)[0]
    except IndexError:
        return ""
    return normalize(section)


def mat_add(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(left[row][column] + right[row][column] for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def mat_sub(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(left[row][column] - right[row][column] for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def mat_mul(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            left[row][0] * right[0][column] + left[row][1] * right[1][column]
            for column in range(2)
        )
        for row in range(2)
    )  # type: ignore[return-value]


def tr(matrix: Matrix) -> Fraction:
    return matrix[0][0] + matrix[1][1]


def K_tr(rho: Matrix, projector: Matrix) -> Fraction:
    return tr(mat_mul(rho, projector))


def K_step(rho: Matrix, projector: Matrix) -> Fraction:
    return Fraction(1) if K_tr(rho, projector) >= Fraction(1, 2) else Fraction(0)


def kernels_agree_at_P_A(rho: Matrix, P_A: Matrix) -> bool:
    return K_tr(rho, P_A) == K_step(rho, P_A)


def live_memo_names_tr_rho_p(record_section: str) -> bool:
    compact = record_section.replace(" ", "")
    needles = (
        "Tr(ρP)",
        "Tr(ρ P)",
        "Tr(\\rho P)",
        "Tr(rhoP)",
        "Tr(rho P)",
    )
    return any(needle.replace(" ", "") in compact for needle in needles)


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
    record_section = governing_record_section(axiom)
    normalized_note = normalize(note)

    print(
        "external_scientific_inputs: current axiom wording is source-bound; "
        "no observational or fitted inputs are used"
    )
    print(
        "package_local_integrity_reads: the proposed source note is read for "
        "claim-surface consistency"
    )
    print(
        "arithmetic: exact Fraction matrix pairing; two kernels on one menu"
    )

    identity: Matrix = (
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(1)),
    )
    P_A: Matrix = (
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(0)),
    )
    P_B = mat_sub(identity, P_A)
    rho: Matrix = (
        (Fraction(3, 5), Fraction(0)),
        (Fraction(0), Fraction(2, 5)),
    )
    lock_label = "A"

    k_tr_a = K_tr(rho, P_A)
    k_tr_b = K_tr(rho, P_B)
    k_step_a = K_step(rho, P_A)
    k_step_b = K_step(rho, P_B)

    checks.check(
        "source-content-alone",
        "live Record determines readout value by record content alone",
        CONTENT_ALONE in record_section,
    )
    checks.check(
        "source-locks-one",
        "live Record locks exactly one admissible local possibility",
        LOCKS_ONE in record_section,
    )
    checks.check(
        "source-I-excluded",
        "memo states named I and I(empty)=0 are not Record axiom content",
        "named scalar collection functional `I`" in axiom
        and "I(empty)=0` are not Record axiom content" in axiom,
    )
    checks.check(
        "mutation-live-memo-tr",
        "predicate live memo names Tr(ρP) fails on governing Record",
        live_memo_names_tr_rho_p(record_section) is False,
    )
    checks.check(
        "menu-resolution",
        "P_A and P_B sum exactly to the identity",
        mat_add(P_A, P_B) == identity,
    )
    checks.check(
        "density-trace-one",
        "rho is a diagonal trace-one positive matrix",
        tr(rho) == Fraction(1)
        and rho[0][0] == Fraction(3, 5)
        and rho[1][1] == Fraction(2, 5)
        and rho[0][1] == 0
        and rho[1][0] == 0,
    )
    checks.check(
        "identity-K-tr-A",
        "K_tr(rho, P_A) computes the exact value 3/5",
        k_tr_a == Fraction(3, 5),
    )
    checks.check(
        "identity-K-tr-B",
        "K_tr(rho, P_B) computes the exact value 2/5",
        k_tr_b == Fraction(2, 5),
    )
    checks.check(
        "identity-K-step-A",
        "K_step(rho, P_A) computes the exact value 1",
        k_step_a == Fraction(1),
    )
    checks.check(
        "identity-K-step-B",
        "K_step(rho, P_B) computes the exact value 0",
        k_step_b == Fraction(0),
    )
    checks.check(
        "mutation-kernel-equality",
        "predicate K_tr(rho, P_A) == K_step(rho, P_A) fails",
        kernels_agree_at_P_A(rho, P_A) is False
        and k_tr_a != k_step_a,
    )
    checks.check(
        "t1-disagreement",
        "same menu, same rho, same lock label A, kernels 3/5 and 1 disagree",
        k_tr_a == Fraction(3, 5)
        and k_step_a == Fraction(1)
        and k_tr_a != k_step_a
        and lock_label == "A",
    )
    checks.check(
        "t2-lock-is-label",
        "the formed lock is the label A, not 3/5 and not 1",
        lock_label == "A"
        and lock_label != str(k_tr_a)
        and lock_label != str(k_step_a),
    )
    checks.check(
        "t2-no-I-A-axiom-step",
        "note does not write I(A)=1 as an axiom step",
        "does not write `I(A)=1` as an axiom step" in normalized_note,
    )
    checks.check(
        "t3-display-both",
        "note displays both kernels and adopts neither",
        "Display both kernels" in note
        and "Do not adopt" in note
        and "Do not adopt Born" in note,
    )
    checks.check(
        "note-theorems",
        "note states Theorems 1-3 and the two failed predicates",
        all(
            phrase in note
            for phrase in (
                "## Theorem 1",
                "## Theorem 2",
                "## Theorem 3",
                "`K_tr(ρ, P_A) == K_step(ρ, P_A)`",
                "live memo names `Tr(ρ P)`",
            )
        ),
    )
    checks.check(
        "note-quotes-content-alone",
        "note quotes the live content-alone sentence",
        CONTENT_ALONE in note,
    )
    checks.check(
        "hygiene-forbidden-phrases",
        "the source does not adopt Born, restore I, or import Gleason",
        "we adopt" not in note
        and "Born axiom" not in note
        and "GLEASON_ON_QUBIT_LATTICE" not in note
        and "I(A)=1` as an axiom step" in note,
    )
    checks.check(
        "claim-type-contract",
        "the author hint uses the exact bounded-theorem enum",
        "**Type:** bounded_theorem" in note,
    )
    checks.check(
        "note-status",
        "note machine status is bounded-support",
        "actual_current_surface_status: bounded-support" in note,
    )
    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the declared note and axiom memo",
        AUDIT_INPUT_PATHS
        == (
            "docs/TWO_KERNELS_ONE_MENU_K_IS_NOT_LOCK_CONTENT_BOUNDED_THEOREM_NOTE_2026-08-13.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        ),
    )

    print(
        "per_element: one binary menu, one density, two exact kernels, one lock label"
    )
    print(
        "per_site: one formed lock of content A; no composite carrier is asserted"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
