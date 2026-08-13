#!/usr/bin/env python3
"""Exact checks for the C1 follow-on Born-extra dissolution note.

Reconstructs the displayed C1 retract and one-site Born arithmetic.
Does not adopt C1, write a Born axiom, import Gleason, force r=1/2,
adopt L_phys, or place a pairing on J.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / (
    "docs/"
    "BORN_EXTRA_UNDER_C1_IS_MENU_KERNEL_NOT_OCCUPANCY_HYPOTHETICAL_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/BORN_EXTRA_UNDER_C1_IS_MENU_KERNEL_NOT_OCCUPANCY_HYPOTHETICAL_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

ZERO = 0
A = "A"
B = "B"
J10A = (A, ZERO)
J01A = (ZERO, A)


Matrix = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]


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


def matrix_add(left: Matrix, right: Matrix) -> Matrix:
    return (
        (left[0][0] + right[0][0], left[0][1] + right[0][1]),
        (left[1][0] + right[1][0], left[1][1] + right[1][1]),
    )


def trace(matrix: Matrix) -> Fraction:
    return matrix[0][0] + matrix[1][1]


def o_from_J(history: tuple[object, object]) -> tuple[int, int]:
    """Definitional occupancy retract of displayed C1 readout J."""
    return tuple(0 if label == ZERO else 1 for label in history)  # type: ignore[return-value]


def born(rho: Matrix, projector: Matrix) -> Fraction:
    """Declared one-site kernel K(rho, P) = Tr(rho P)."""
    return trace(matrix_mul(rho, projector))


def I_J(history: tuple[object, object]) -> int:
    """Additive Record count of locked sites on the window."""
    return sum(0 if label == ZERO else 1 for label in history)


def normalize(text: str) -> str:
    return " ".join(text.split())


@dataclass(frozen=True)
class Checks:
    passed: int = 0
    failed: int = 0

    def check(self, label: str, statement: str, condition: bool) -> "Checks":
        result = bool(condition)
        if result:
            object.__setattr__(self, "passed", self.passed + 1)
        else:
            object.__setattr__(self, "failed", self.failed + 1)
        print(f"{'PASS' if result else 'FAIL'}: {label} {statement}")
        return self

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    normalized_note = normalize(note)
    normalized_axiom = normalize(axiom)

    identity = (
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(1)),
    )
    sigma_x = (
        (Fraction(0), Fraction(1)),
        (Fraction(1), Fraction(0)),
    )
    rho: Matrix = (
        (Fraction(3, 5), Fraction(0)),
        (Fraction(0), Fraction(2, 5)),
    )
    Pz: Matrix = (
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(0)),
    )
    Px: Matrix = (
        (
            (identity[0][0] + sigma_x[0][0]) / 2,
            (identity[0][1] + sigma_x[0][1]) / 2,
        ),
        (
            (identity[1][0] + sigma_x[1][0]) / 2,
            (identity[1][1] + sigma_x[1][1]) / 2,
        ),
    )
    I_minus_Pz = (
        (identity[0][0] - Pz[0][0], identity[0][1] - Pz[0][1]),
        (identity[1][0] - Pz[1][0], identity[1][1] - Pz[1][1]),
    )
    I_minus_Px = (
        (identity[0][0] - Px[0][0], identity[0][1] - Px[0][1]),
        (identity[1][0] - Px[1][0], identity[1][1] - Px[1][1]),
    )

    checks.check(
        "source-axioms",
        "the current axiom memo names Lattice, Qubit, Admissibility, and Record",
        all(
            name in axiom
            for name in (
                "### Lattice / Physical Locality",
                "### Qubit / Site Possibility",
                "### Admissibility / Local Constraint",
                "### Record / Fixed Reality",
            )
        ),
    )
    checks.check(
        "source-qubit-domain",
        "the one-site possibility domain is M_2(C)",
        "The full one-site possibility domain has algebraic presentation `M_2(C)`."
        in axiom,
    )
    checks.check(
        "source-record-count",
        "Record supplies additive scalar readout I with empty zero",
        "scalar readout `I` is additive, with `I(empty)=0`" in normalize(axiom),
    )
    checks.check(
        "canonical-nonmutation",
        "the axiom memo does not contain J, C1, a Born axiom, Gleason, L_phys, or a pairing",
        all(
            phrase not in normalized_axiom
            for phrase in (
                "site-indexed J",
                "Born axiom",
                "Gleason",
                "L_phys",
                "pairing on J",
                "o_from_J",
            )
        ),
    )
    checks.check(
        "menu-resolutions",
        "M_z and M_x are exact binary resolutions of I",
        matrix_add(Pz, I_minus_Pz) == identity
        and matrix_add(Px, I_minus_Px) == identity,
    )
    checks.check(
        "rho-normalization",
        "rho is a diagonal state with exact masses 3/5 and 2/5",
        trace(rho) == 1
        and rho[0][0] == Fraction(3, 5)
        and rho[1][1] == Fraction(2, 5)
        and rho[0][1] == 0
        and rho[1][0] == 0,
    )

    # Identity gates MUST call o_from_J, born(rho,Pz), born(rho,Px), I_J.
    occupancy_10 = o_from_J(J10A)
    occupancy_01 = o_from_J(J01A)
    kernel_z = born(rho,Pz)
    kernel_x = born(rho,Px)
    count_10 = I_J(J10A)
    count_01 = I_J(J01A)

    checks.check(
        "identity-o-J10A",
        "o_from_J on J10A is the occupancy (1, 0)",
        occupancy_10 == (1, 0),
    )
    checks.check(
        "identity-o-J01A",
        "o_from_J on J01A is the occupancy (0, 1)",
        occupancy_01 == (0, 1),
    )
    checks.check(
        "identity-born-Pz",
        "born(rho,Pz) equals the exact kernel 3/5",
        kernel_z == Fraction(3, 5),
    )
    checks.check(
        "identity-born-Px",
        "born(rho,Px) equals the exact kernel 1/2",
        kernel_x == Fraction(1, 2),
    )
    checks.check(
        "identity-I-J10A",
        "I_J on J10A is the unit-lock Record count 1",
        count_10 == 1,
    )
    checks.check(
        "identity-I-J01A",
        "I_J on J01A is the unit-lock Record count 1",
        count_01 == 1,
    )

    o_independent_of_J = occupancy_10 == occupancy_01
    menus_agree = kernel_z == kernel_x
    count_equals_kernel = count_10 == kernel_z
    checks.check(
        "mutation-occupancy-depends-on-J",
        "predicate 'o is independent of J' fails",
        o_independent_of_J is False,
    )
    checks.check(
        "mutation-menus-disagree",
        "predicate 'K(rho,P_z)=K(rho,P_x)' fails",
        menus_agree is False,
    )
    checks.check(
        "mutation-count-is-not-kernel",
        "predicate 'I_J equals K(rho,P_z)' fails",
        count_equals_kernel is False,
    )

    checks.check(
        "machine-status-contract",
        "the note uses the required bounded-support and C1 follow-on hypothetical fields",
        "actual_current_surface_status: bounded-support" in note
        and (
            'hypothetical_axiom_status: "C1 follow-on: under site-indexed J, '
            'Born extra is (M,K) not (o,M,K); not adopted"'
        )
        in note,
    )
    checks.check(
        "theorem-surface",
        "the five theorems and the (M,K) display are source-visible",
        all(
            phrase in normalized_note
            for phrase in (
                "Occupancy Dies Under C1",
                "Menu Survives",
                "Kernel Survives",
                "Smallest Complete Born Extra Under C1 Is `(M,K)`",
                "Forbidden Closures",
                "Display `(M, K)`",
                "not a new named extra",
                "Do not adopt C1",
                "Do not import Gleason",
                "Do not force `r = 1/2`",
                "Do not adopt `L_phys`",
                "Do not put a pairing on `J`",
            )
        ),
    )
    checks.check(
        "no-adoption",
        "C1 and a Born axiom remain unadopted on this surface",
        "not adopted" in note
        and "Do not adopt a Born axiom" in note
        and "C1 is reconstructed here only as a displayed counterfactual" in note,
    )
    checks.check(
        "audit-inputs",
        "declared audit inputs are the new note and the axiom memo only",
        AUDIT_INPUT_PATHS
        == (
            "docs/BORN_EXTRA_UNDER_C1_IS_MENU_KERNEL_NOT_OCCUPANCY_HYPOTHETICAL_BOUNDED_THEOREM_NOTE_2026-08-13.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file(),
    )

    print("per_element: two unit-lock histories, two menus, two kernel values")
    print("per_site: one M_2(C) law and a two-site window")
    print("per_mode: checked and not executed — no spectral claim")
    print("per_block: Born-cluster extras under displayed C1 only")
    print("lattice_wide: checked and not executed — no lattice-wide dynamics")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
