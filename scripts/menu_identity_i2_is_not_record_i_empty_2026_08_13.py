#!/usr/bin/env python3
"""Exact checks that the menu identity I_2 is not Record I(empty)=0.

Identity-gate comparisons call tr_I2() and I_empty(). The hostile predicate
Tr(I_2)=I(empty) must fail because 2 != 0 in Q. No dictionary, Born negation,
r=1/2 forcing, or L_phys adoption is accepted.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "MENU_IDENTITY_I2_IS_NOT_RECORD_I_EMPTY_BOUNDED_THEOREM_NOTE_2026-08-13.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
PARENT_PATH = ROOT / "docs" / "BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md"

AUDIT_INPUT_PATHS = (
    "docs/MENU_IDENTITY_I2_IS_NOT_RECORD_I_EMPTY_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Matrix = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]


def normalize(text: str) -> str:
    return " ".join(text.split())


def I2() -> Matrix:
    return ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(1)))


def tr_I2() -> Fraction:
    matrix = I2()
    return matrix[0][0] + matrix[1][1]


def I_empty() -> Fraction:
    return Fraction(0)


def matrix_add(left: Matrix, right: Matrix) -> Matrix:
    return (
        (left[0][0] + right[0][0], left[0][1] + right[0][1]),
        (left[1][0] + right[1][0], left[1][1] + right[1][1]),
    )


def matrix_sub(left: Matrix, right: Matrix) -> Matrix:
    return (
        (left[0][0] - right[0][0], left[0][1] - right[0][1]),
        (left[1][0] - right[1][0], left[1][1] - right[1][1]),
    )


def identity_equal_predicate() -> bool:
    """Hostile predicate Tr(I_2)=I(empty). Identity gates must call both maps."""
    return tr_I2() == I_empty()


@dataclass(frozen=True)
class Checks:
    passed: int = 0
    failed: int = 0

    def check(self, label: str, statement: str, condition: bool) -> "Checks":
        result = bool(condition)
        if result:
            self = Checks(self.passed + 1, self.failed)
        else:
            self = Checks(self.passed, self.failed + 1)
        print(f"{'PASS' if result else 'FAIL'}: {label} {statement}")
        return self

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    parent = PARENT_PATH.read_text(encoding="utf-8")
    normalized_note = normalize(note).replace("> ", "")
    normalized_axiom = normalize(axiom)
    normalized_parent = normalize(parent)

    print("external_scientific_inputs: current axiom wording and the parent menu-sum convention are source-bound; no observational or fitted inputs are used")
    print("package_local_integrity_reads: the proposed source note is read for claim-surface consistency")
    print("identity_boundary: identity gates call tr_I2() and I_empty(); the hostile equality predicate must fail")
    print("negative_scope: only the I_2 / I(empty) homonym is rejected; Born form, weights, and lengths remain unforced")

    checks = checks.check(
        "source-record",
        "Record supplies a scalar readout I with I(empty)=0",
        "scalar readout `I` is additive, with `I(empty)=0`" in normalized_axiom,
    )
    checks = checks.check(
        "source-parent-menu-identity",
        "the August 9 parent uses I_2 as the operator menus sum to",
        all(
            phrase in parent
            for phrase in (
                "scaled rank-one qubit effects summing to `I_2`",
                "A menu is a finite family of nonzero members of `S` summing to `I`.",
            )
        ),
    )

    identity = I2()
    checks = checks.check(
        "i2-matrix-type",
        "I_2 is a 2x2 matrix over Q",
        len(identity) == 2
        and all(len(row) == 2 for row in identity)
        and all(isinstance(identity[i][j], Fraction) for i in range(2) for j in range(2)),
    )
    checks = checks.check(
        "i-empty-scalar-type",
        "I(empty) is a scalar rational count",
        isinstance(I_empty(), Fraction) and not isinstance(I_empty(), tuple),
    )
    checks = checks.check(
        "type-separation",
        "the menu identity and the empty readout have different types",
        type(identity) is not type(I_empty()),
    )

    checks = checks.check(
        "tr-i2-value",
        "tr_I2() returns the exact rational 2",
        tr_I2() == Fraction(2),
    )
    checks = checks.check(
        "i-empty-value",
        "I_empty() returns the exact rational 0",
        I_empty() == Fraction(0),
    )
    checks = checks.check(
        "identity-gate-rational-unequal",
        "Tr(I_2)=2 is not I(empty)=0 even as rationals",
        tr_I2() != I_empty() and tr_I2() - I_empty() == Fraction(2),
    )
    checks = checks.check(
        "mutation-predicate",
        "the hostile predicate Tr(I_2)=I(empty) fails",
        identity_equal_predicate() is False,
    )

    projector = (
        (Fraction(1, 2), Fraction(1, 2)),
        (Fraction(1, 2), Fraction(1, 2)),
    )
    complement = matrix_sub(I2(), projector)
    menu_sum = matrix_add(projector, complement)
    checks = checks.check(
        "binary-menu-resolution",
        "the binary menu {P, I_2-P} sums exactly to I_2",
        menu_sum == I2() and projector[0][0] + projector[1][1] == Fraction(1),
    )

    theorem_needles = (
        "Tr(I_2)=2` and `I(empty)=0` are both elements of `Q`",
        "`I_2` is a `2 times 2` matrix. `I(empty)` is a scalar count.",
        "Identifying the menu identity with Record `I` is extra.",
        "It does not claim that the Born trace form is false.",
        "Nothing in Theorems 1--4 selects a Koide or Born weight `r=1/2`.",
        "Nothing in Theorems 1--4 introduces or adopts a physical length `L_phys`.",
    )
    checks = checks.check(
        "theorem-surface",
        "the note states Theorems 1 through 5 on the declared objects",
        all(phrase in normalized_note for phrase in theorem_needles),
    )
    checks = checks.check(
        "no-dictionary-adoption",
        "the note displays the mismatch and refuses a dictionary",
        "This note displays that table. It does not adopt a dictionary" in normalized_note
        and "`I_2 := I(empty)`" in note,
    )
    checks = checks.check(
        "no-born-false-claim",
        "the note does not claim Born is false",
        "does not claim that the Born trace form is false" in normalized_note
        and "Born is false" in note,
    )
    checks = checks.check(
        "no-r-half-force",
        "the note does not force r=1/2",
        "does not force a weight `r=1/2`" in normalized_note
        and "force `r=1/2`" in note,
    )
    checks = checks.check(
        "no-lphys-adoption",
        "the note does not adopt L_phys",
        "does not adopt a physical length `L_phys`" in normalized_note
        and "adopt `L_phys`" in note,
    )
    checks = checks.check(
        "claim-type-contract",
        "the author hint uses the exact bounded-theorem enum",
        "**Type:** bounded_theorem" in note,
    )
    checks = checks.check(
        "machine-status-contract",
        "the source uses the controlled bounded-support and negative-route-pruning trace fields",
        all(
            phrase in note
            for phrase in (
                "actual_current_surface_status: bounded-support",
                "target_claim_type: bounded_theorem",
                "claim_type_reason:",
                "trace_class: negative_route_pruning",
                "source_of_blocker_text: handoff",
                "audit_required_before_effective_retained: true",
                "bare_retained_allowed: false",
            )
        ),
    )
    checks = checks.check(
        "canonical-nonmutation",
        "the canonical axiom memo is not edited and still has only the Record scalar I(empty)=0",
        "scalar readout `I` is additive, with `I(empty)=0`." in normalized_axiom
        and "I_2 := I(empty)" not in axiom
        and "menu identity" not in axiom,
    )
    checks = checks.check(
        "no-unmerged-pr-citation",
        "the note does not cite unmerged PR labels",
        all(
            token not in note.lower()
            for token in ("trvsi", "emptyvac", "#6215", "#6212", "unmerged pr")
        ),
    )
    checks = checks.check(
        "no-go-gate",
        "all N1-N8 sections and the broad-claim rejection are source-visible",
        all(f"### N{index}" in note for index in range(1, 9))
        and "FAIL / DO NOT SHIP" in note
        and "an axiom update is necessary" in note,
    )

    print("per_element: I_2 diagonal entries, empty-collection readout, and one rank-one binary menu are checked")
    print("per_site: the mismatch is a one-site statement in M_2(C); no composite carrier is asserted")
    print("per_mode: only the identity-versus-empty-readout pair is tested")
    print("per_block: the two-symbol homonym is the only negative block tested")
    print("lattice_wide: checked and not executed — no lattice-wide dynamics or Born no-go is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
