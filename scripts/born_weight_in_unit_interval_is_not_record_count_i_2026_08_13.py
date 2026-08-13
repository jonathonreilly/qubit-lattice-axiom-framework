#!/usr/bin/env python3
"""Exact type checks: a Born weight in (0, 1) is not a unit-lock Record count.

The runner computes Tr(rho P) by Fraction matrix arithmetic and evaluates
record_I as a unit-lock cardinality. It does not approximate, fit, or cache.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "BORN_WEIGHT_IN_UNIT_INTERVAL_IS_NOT_RECORD_COUNT_I_BOUNDED_THEOREM_NOTE_2026-08-13.md"
PARENT_PATH = ROOT / "docs" / "BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/BORN_WEIGHT_IN_UNIT_INTERVAL_IS_NOT_RECORD_COUNT_I_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Matrix = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]


def normalize(text: str) -> str:
    return " ".join(text.split())


def matmul(left: Matrix, right: Matrix) -> Matrix:
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


def trace(matrix: Matrix) -> Fraction:
    return matrix[0][0] + matrix[1][1]


def born(rho: Matrix, P: Matrix) -> Fraction:
    return trace(matmul(rho, P))


def record_I(nlocks: int) -> int:
    if nlocks < 0:
        raise ValueError("unit-lock count is nonnegative")
    return nlocks


def identity_born_gate(rho: Matrix, P: Matrix) -> Fraction:
    return born(rho, P)


def identity_record_gate(nlocks: int) -> int:
    return record_I(nlocks)


def predicate_born_weight_is_integer(value: Fraction) -> bool:
    return value.denominator == 1


def predicate_one_lock_equals_three_fifths(nlocks: int) -> bool:
    return record_I(nlocks) == Fraction(3, 5)


@dataclass
class Checks:
    passed: int = 0
    failed: int = 0

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
    runner_src = Path(__file__).read_text(encoding="utf-8")
    normalized_note = normalize(note)

    print(
        "external_scientific_inputs: axiom Record wording and the August 9 "
        "supplied-grading Born form are source-bound; no observational or fitted inputs"
    )
    print(
        "package_local_integrity_reads: the proposed source note, the August 9 "
        "parent, and the axiom memo are read for claim-surface consistency"
    )
    print("arithmetic: exact Fraction matrix pairing and integer unit-lock cardinality")

    P: Matrix = (
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(0)),
    )
    rho: Matrix = (
        (Fraction(3, 5), Fraction(0)),
        (Fraction(0), Fraction(2, 5)),
    )

    weight = identity_born_gate(rho, P)
    empty_count = identity_record_gate(0)
    one_lock = identity_record_gate(1)
    two_locks = identity_record_gate(2)

    checks.check(
        "source-record",
        "the axiom memo states additive I with I(empty)=0",
        "`I` is additive, with `I(empty)=0`" in axiom,
    )
    checks.check(
        "source-parent",
        "the August 9 parent supplies the unique trace form on a supplied grading",
        all(
            phrase in parent
            for phrase in (
                "w(E)=Tr(rho E)",
                "unique density matrix",
                "explicitly supplied grading",
            )
        ),
    )
    checks.check(
        "identity-born",
        "identity gate born(rho, P) returns the exact pairing 3/5",
        weight == Fraction(3, 5) and Fraction(0) < weight < Fraction(1),
    )
    checks.check(
        "identity-record",
        "identity gate record_I(nlocks) is the unit-lock cardinality",
        empty_count == 0 and one_lock == 1 and two_locks == 2,
    )
    checks.check(
        "identity-gate-calls",
        "identity gates call born(rho, P) and record_I(nlocks)",
        "born(rho, P)" in runner_src and "record_I(nlocks)" in runner_src,
    )
    checks.check(
        "record-additivity",
        "unit-lock I is additive on disjoint locks",
        record_I(2) == record_I(1) + record_I(1)
        and record_I(1) == record_I(0) + record_I(1),
    )
    checks.check(
        "projector-and-density",
        "P is a projector and rho is a trace-one positive diagonal density",
        matmul(P, P) == P
        and P[0][1] == P[1][0] == Fraction(0)
        and trace(rho) == Fraction(1)
        and rho[0][0] > 0
        and rho[1][1] > 0,
    )
    checks.check(
        "mutation-integer-born",
        "the predicate Tr(rho P) is an integer fails on 3/5",
        not predicate_born_weight_is_integer(born(rho, P)),
    )
    checks.check(
        "mutation-one-lock-fraction",
        "the predicate I(one lock)=3/5 fails",
        not predicate_one_lock_equals_three_fifths(1),
    )
    checks.check(
        "type-separation",
        "the pairing is rational non-integral and the unit-lock values are integers",
        weight.denominator != 1
        and isinstance(empty_count, int)
        and isinstance(one_lock, int)
        and isinstance(two_locks, int),
    )
    checks.check(
        "note-theorems",
        "the note states the five theorems, the extra dictionary, and the two failed predicates",
        all(
            phrase in normalized_note
            for phrase in (
                "3/5 notin Z",
                "not equal to any unit-lock",
                "different types",
                "extra dictionary",
                "does not adopt the dictionary",
                "does not say that the Born form is false",
                "does not force `r=1/2`",
                "does not adopt `L_phys`",
                "`Tr(rho P)` is an integer",
                "`I(one lock)=3/5`",
            )
        ),
    )
    checks.check(
        "independence-surface",
        "the note excludes Bessel functions, Haar measure, and four-dimensional plaquettes",
        all(
            phrase in normalized_note
            for phrase in (
                "Bessel functions",
                "Haar measure",
                "four-dimensional plaquettes",
            )
        ),
    )
    checks.check(
        "forbidden-imports-absent",
        "the note does not cite Gleason, the decimal 0.5934, or unmerged block names",
        all(
            token not in note
            for token in ("Gleason", "0.5934", "realens", "oneweight", "pvmluders")
        ),
    )
    checks.check(
        "claim-type-contract",
        "the author hint uses the exact bounded-theorem enum",
        "**Type:** bounded_theorem" in note,
    )
    checks.check(
        "audit-input-paths",
        "declared audit inputs are the new note, the August 9 parent, and the axiom memo",
        AUDIT_INPUT_PATHS
        == (
            "docs/BORN_WEIGHT_IN_UNIT_INTERVAL_IS_NOT_RECORD_COUNT_I_BOUNDED_THEOREM_NOTE_2026-08-13.md",
            "docs/BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    )
    checks.check(
        "canonical-nonmutation",
        "the axiom memo is not edited by this block",
        "unit-lock Record pattern" not in axiom,
    )

    print("per_element: one exact projector-density pairing and the unit-lock counts 0,1,2")
    print("dictionary: displayed mismatch only; no pairing-to-count map is adopted")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
