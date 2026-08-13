#!/usr/bin/env python3
"""Exact checks: I(empty)=0 is a count identity, not a vacuum energy.

Identity gates are I_empty() and trial_E0(). Every identity or trial-constant
check calls those functions. The predicates “I(empty)=1” and “I(empty)
selects E0=1/2” are required to fail.
"""

from __future__ import annotations

import ast
from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "I_EMPTY_ZERO_IS_NOT_A_VACUUM_ENERGY_BOUNDED_THEOREM_NOTE_2026-08-13.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
PRIMITIVE_PATH = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"

AUDIT_INPUT_PATHS = (
    "docs/I_EMPTY_ZERO_IS_NOT_A_VACUUM_ENERGY_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
)

Collection = frozenset[object]


def normalize(text: str) -> str:
    return " ".join(text.split())


def I(collection: Collection) -> Fraction:
    """Scalar readout: number of locks in a finite record collection."""
    return Fraction(len(collection))


def I_empty() -> Fraction:
    """Additive identity of the Record readout.

    empty ∪ empty = empty, so additivity forces I(empty) = I(empty)+I(empty).
    The readout itself is the lock count of the empty collection.
    """
    empty: Collection = frozenset()
    unioned = empty.union(empty)
    if unioned != empty:
        raise RuntimeError("empty ∪ empty is not empty")
    value = I(empty)
    if I(unioned) != value + value:
        raise RuntimeError("additivity failed on empty ∪ empty")
    # Unique solution of x = x + x in Q is 0: (2-1)x = 0.
    if (Fraction(2) - Fraction(1)) * value != Fraction(0):
        raise RuntimeError("additive identity is not 0")
    return value


def trial_E0(value: Fraction | int = 1) -> Fraction:
    """Law-level constant attached to the empty history; not a lock count."""
    return Fraction(value)


def predicate_I_empty_equals_one() -> bool:
    return I_empty() == Fraction(1)


def predicate_I_empty_selects_half() -> bool:
    return I_empty() == trial_E0(Fraction(1, 2))


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


def _identity_gate_calls(source: str) -> tuple[bool, bool]:
    tree = ast.parse(source)
    defined = {
        node.name
        for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef)
    }
    called: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            called.add(node.func.id)
    return "I_empty" in defined and "I_empty" in called, (
        "trial_E0" in defined and "trial_E0" in called
    )


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    primitive = PRIMITIVE_PATH.read_text(encoding="utf-8")
    runner_source = Path(__file__).read_text(encoding="utf-8")
    normalized_note = normalize(note)
    normalized_axiom = normalize(axiom)
    normalized_primitive = normalize(primitive)

    print(
        "external_scientific_inputs: axiom wording and the realized-state "
        "primitive are source-bound; no observational or fitted inputs are used"
    )
    print(
        "package_local_integrity_reads: the proposed source note is read for "
        "claim-surface consistency"
    )

    empty: Collection = frozenset()
    empty_value = I_empty()
    extra_one = trial_E0(1)
    extra_half = trial_E0(Fraction(1, 2))
    extra_zero = trial_E0(0)

    checks.check(
        "i-empty-zero",
        "I_empty() equals 0 as the lock count of the empty collection",
        empty_value == Fraction(0) and I(empty) == I_empty(),
    )
    checks.check(
        "additivity-empty-union",
        "I(empty ∪ empty) equals I_empty() + I_empty()",
        I(empty.union(empty)) == I_empty() + I_empty(),
    )
    checks.check(
        "additive-identity-unique",
        "I_empty() = I_empty() + I_empty() forces the unique rational 0",
        I_empty() == I_empty() + I_empty()
        and (Fraction(2) - Fraction(1)) * I_empty() == Fraction(0),
    )
    checks.check(
        "trial-e0-one",
        "trial_E0(1) is the well-defined rational 1 and is not I_empty()",
        extra_one == Fraction(1) and extra_one != I_empty(),
    )
    checks.check(
        "trial-e0-half",
        "trial_E0(1/2) is the well-defined rational 1/2 and is not 0",
        extra_half == Fraction(1, 2)
        and extra_half != I_empty()
        and extra_half != Fraction(0),
    )
    checks.check(
        "trial-e0-zero-is-still-extra",
        "trial_E0(0) equals I_empty() as a rational and remains an extra object",
        extra_zero == I_empty() and extra_zero == Fraction(0),
    )
    checks.check(
        "mutation-equals-one",
        "the predicate I(empty)=1 fails",
        predicate_I_empty_equals_one() is False,
    )
    checks.check(
        "mutation-selects-half",
        "the predicate I(empty) selects E0=1/2 fails",
        predicate_I_empty_selects_half() is False,
    )
    checks.check(
        "identity-gates-present",
        "identity gates I_empty() and trial_E0() are defined and called",
        all(_identity_gate_calls(runner_source)),
    )

    record_sentence = "`I` is additive, with `I(empty)=0`"
    checks.check(
        "source-record",
        "the axiom memo states finite additivity with I(empty)=0",
        record_sentence in axiom
        and "pairwise-disjoint records" in axiom
        and "A readout value is determined by record content" in axiom,
    )
    checks.check(
        "source-realized-state",
        "the realized-state primitive states pointwise evaluation and no averaging",
        "evaluate at the realized state, pointwise" in primitive
        and "no averaging over alternatives" in primitive
        and "pointwise" in normalized_primitive,
    )
    checks.check(
        "note-theorem-1",
        "the note recomputes I(empty ∪ empty)=I(empty)+I(empty) ⇒ I(empty)=0",
        "I(empty ∪ empty) = I(empty) + I(empty)" in note
        and "empty ∪ empty = empty" in note
        and "`I(empty) = 0`" in note,
    )
    checks.check(
        "note-theorem-2",
        "the note states E0=1 and E0=1/2 are unequal to I(empty)",
        "E0 = 1 ≠ I(empty) = 0" in normalized_note
        and "E0 = 1/2 ≠ I(empty) = 0" in normalized_note,
    )
    checks.check(
        "note-theorem-3",
        "the note quotes pointwise evaluation and refuses a selectable vacuum readout",
        "evaluate at the realized state, pointwise" in note
        and "no averaging over alternatives" in note
        and "count identity, not a selectable energy" in normalized_note,
    )
    checks.check(
        "note-theorem-4",
        "the note displays E0=1 as extra, does not adopt it, and claims no cosmology",
        "Display `E0=1` as extra" in note
        and "Do not adopt it" in note
        and "does not install a cosmological constant" in normalized_note
        and "does not claim cosmology" in normalized_note,
    )
    checks.check(
        "note-theorem-5",
        "the note does not identify E0 with r, w, or G_N and does not force r=1/2",
        "Do not identify `E0` with `r`, `w`, or `G_N`" in note
        and "does not force `r=1/2`" in note,
    )
    checks.check(
        "note-mutation",
        "the note requires I(empty)=1 and I(empty) selects E0=1/2 to fail",
        "I(empty)=1" in note
        and "I(empty)` selects `E0=1/2" in note
        and "P1` fails" in note
        and "P½` fails" in note,
    )
    checks.check(
        "note-forbidden-surface",
        "the note has no adoption phrasing and cites no unmerged pull request",
        "we adopt" not in note.lower()
        and "new axiom" not in note.lower()
        and "codex" not in note.lower()
        and "energy dictionary" not in note.lower()
        and "clockscale" not in note.lower()
        and "PR #" not in note
        and "github.com" not in note.lower(),
    )
    checks.check(
        "canonical-nonmutation",
        "the displayed trial constant E0 is absent from the canonical axiom file",
        all(phrase not in axiom for phrase in ("E0=1", "trial_E0", "emptyvac")),
    )
    checks.check(
        "claim-type-contract",
        "the author hint uses the exact bounded-theorem enum",
        "**Type:** bounded_theorem" in note,
    )
    checks.check(
        "parents-unmutated",
        "the axiom identity and the realized-state pointwise sentence remain",
        "`I` is additive, with `I(empty)=0`" in axiom
        and "Derivations may evaluate at the realized state, pointwise."
        in primitive,
    )
    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the new note, axiom memo, and realized-state primitive",
        AUDIT_INPUT_PATHS
        == (
            "docs/I_EMPTY_ZERO_IS_NOT_A_VACUUM_ENERGY_BOUNDED_THEOREM_NOTE_2026-08-13.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
        )
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    )

    print("per_element: I_empty() and trial_E0() are the only identity gates")
    print("per_site: the empty collection is the only record collection used")
    print("per_mode: trial values are 1 and 1/2; r=1/2 is not forced")
    print("per_block: rejected blocks are I(empty)=1 and I(empty) selects E0=1/2")
    print("lattice_wide: checked and not executed — no lattice-wide claim is made")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
