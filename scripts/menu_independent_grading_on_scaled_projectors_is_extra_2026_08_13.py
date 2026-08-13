#!/usr/bin/env python3
"""Exact checks that a menu-independent scaled-projector grade is extra.

The runner compares two displayed trial grades at P_z, checks that the
current axiom memo does not name w_ρ, and checks that the source note
treats August 9 uniqueness as conditional on that extra matching. Exact
Fraction arithmetic only. No Gleason import.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "MENU_INDEPENDENT_GRADING_ON_SCALED_PROJECTORS_IS_EXTRA_BOUNDED_THEOREM_NOTE_2026-08-13.md"
PARENT_PATH = ROOT / "docs" / "BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/MENU_INDEPENDENT_GRADING_ON_SCALED_PROJECTORS_IS_EXTRA_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Matrix = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]

Pz: Matrix = ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(0)))
I2: Matrix = ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(1)))
ZERO: Matrix = ((Fraction(0), Fraction(0)), (Fraction(0), Fraction(0)))


def normalize(text: str) -> str:
    return " ".join(text.split())


def scale(coefficient: Fraction, matrix: Matrix) -> Matrix:
    return tuple(
        tuple(coefficient * matrix[row][column] for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def _entry_zero(matrix: Matrix, row: int, column: int) -> bool:
    return matrix[row][column] == 0


def _as_multiple(matrix: Matrix, basis: Matrix) -> Fraction | None:
    coefficient: Fraction | None = None
    for row in range(2):
        for column in range(2):
            basis_entry = basis[row][column]
            matrix_entry = matrix[row][column]
            if basis_entry == 0:
                if matrix_entry != 0:
                    return None
                continue
            candidate = matrix_entry / basis_entry
            if coefficient is None:
                coefficient = candidate
            elif candidate != coefficient:
                return None
    return Fraction(0) if coefficient is None else coefficient


def w_rho(effect: Matrix) -> Fraction:
    """Displayed grade from ρ=diag(3/5, 2/5) on {0, P_z, I}."""
    if effect == ZERO:
        return Fraction(0)
    identity_scale = _as_multiple(effect, I2)
    if identity_scale is not None:
        return identity_scale
    projector_scale = _as_multiple(effect, Pz)
    if projector_scale is not None:
        return projector_scale * Fraction(3, 5)
    raise ValueError("w_rho is defined only on scaled {0, P_z, I}")


def w_star(effect: Matrix) -> Fraction:
    """Displayed grade from I/2 on {0, P_z, I}."""
    if effect == ZERO:
        return Fraction(0)
    identity_scale = _as_multiple(effect, I2)
    if identity_scale is not None:
        return identity_scale
    projector_scale = _as_multiple(effect, Pz)
    if projector_scale is not None:
        return projector_scale * Fraction(1, 2)
    raise ValueError("w_star is defined only on scaled {0, P_z, I}")


def grades_equal_at_pz() -> bool:
    return w_rho(Pz) == w_star(Pz)


def axioms_name_w_rho(axiom_text: str) -> bool:
    needles = (
        "w_ρ",
        "w_rho",
        "menu-independent grading",
        "scaled projector",
        "scaled-projector",
        "Tr(ρ",
        "Tr(rho",
    )
    return any(needle in axiom_text for needle in needles)


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
    normalized_note = normalize(note).replace("> ", "")
    normalized_axiom = normalize(axiom)

    print(
        "external_scientific_inputs: current axiom wording and the parent "
        "low-arity uniqueness theorem are source-bound; no observational or "
        "fitted inputs are used"
    )
    print(
        "package_local_integrity_reads: the proposed source note is read for "
        "claim-surface consistency; Gleason is not imported"
    )
    print(
        "negative_scope: only the extra matching that a menu-independent "
        "scaled-projector grade exists and is the instrument is named; "
        "August 9 is not improved and Born is not denied"
    )

    checks.check(
        "pz-definition",
        "P_z is exactly diag(1, 0)",
        Pz == ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(0)))
        and _entry_zero(Pz, 0, 1)
        and _entry_zero(Pz, 1, 0)
        and _entry_zero(Pz, 1, 1),
    )
    checks.check(
        "identity-w-rho",
        "the identity gate w_rho(Pz) equals 3/5",
        w_rho(Pz) == Fraction(3, 5),
    )
    checks.check(
        "identity-w-star",
        "the identity gate w_star(Pz) equals 1/2",
        w_star(Pz) == Fraction(1, 2),
    )
    checks.check(
        "mutation-grades-unequal",
        "the predicate w_ρ=w_* fails at P_z",
        not grades_equal_at_pz() and w_rho(Pz) != w_star(Pz),
    )
    half = Fraction(1, 2)
    checks.check(
        "identity-ray-agreement",
        "both grades send c I to c and send 0 to 0",
        w_rho(I2) == 1
        and w_star(I2) == 1
        and w_rho(scale(half, I2)) == half
        and w_star(scale(half, I2)) == half
        and w_rho(ZERO) == 0
        and w_star(ZERO) == 0,
    )
    checks.check(
        "scaled-projector-split",
        "the grades remain unequal on a proper multiple of P_z",
        w_rho(scale(half, Pz)) == Fraction(3, 10)
        and w_star(scale(half, Pz)) == Fraction(1, 4)
        and w_rho(scale(half, Pz)) != w_star(scale(half, Pz)),
    )
    checks.check(
        "mutation-axioms-do-not-name-w-rho",
        "the predicate axioms-name-w_ρ fails on the current axiom memo",
        not axioms_name_w_rho(axiom),
    )
    checks.check(
        "source-admissibility",
        "the note quotes the nearest-neighbor distribution sentence",
        "the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions"
        in normalized_axiom
        and "the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions"
        in normalized_note,
    )
    checks.check(
        "source-record",
        "the note quotes the lock sentence and additive Record I",
        "a record locks exactly one admissible local possibility" in normalized_axiom
        and "a record locks exactly one admissible local possibility" in normalized_note
        and "scalar readout `I` is additive" in normalized_note
        and "I(empty)=0" in normalized_axiom
    )
    checks.check(
        "source-parent-uniqueness",
        "the parent uniqueness statement is conditional on a supplied menu-independent grade",
        all(
            phrase in parent
            for phrase in (
                "menu-independent grading",
                "Every two- or three-member menu is normalized",
                "There is a unique density matrix",
                "w(E)=Tr(rho E)",
            )
        ),
    )
    checks.check(
        "extra-matching-surface",
        "the note names the extra matching and displays w_ρ without adopting it",
        all(
            phrase in normalized_note
            for phrase in (
                "such a `w` exists and is the instrument",
                "Display `w_ρ`; do not adopt it",
                "Neither sentence names a grade `w` on scaled projectors",
                "w_ρ(P_z)=3/5 ≠ 1/2=w_*(P_z)",
            )
        ),
    )
    checks.check(
        "theorem-four-and-five-boundary",
        "the note refuses August 9 improvement, Gleason-as-physics, Born denial, forced r=1/2, and L_phys",
        all(
            phrase in note
            for phrase in (
                "This note does not claim that the August 9 theorem is improved.",
                "This note does not import Gleason as physics.",
                "This note does not say Born is false.",
                "This note does not force `r=1/2`.",
                "This note does not adopt `L_phys`.",
            )
        ),
    )

    print("per_element: identity gates evaluate w_rho(Pz) and w_star(Pz); scaled and identity-ray controls use exact Fraction")
    print("per_site: both trial grades and the axiom-text comparison are one-site statements")
    print("per_mode: no spectral-mode exhaustion is claimed")
    print("per_block: the extra matching that such a w exists and is the instrument is the only negative block tested")
    print("lattice_wide: checked and not executed — no lattice-wide Born no-go is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
