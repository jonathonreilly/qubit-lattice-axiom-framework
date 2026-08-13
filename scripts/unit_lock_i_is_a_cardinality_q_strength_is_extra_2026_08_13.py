#!/usr/bin/env python3
"""Exact checks: unit-lock I is a cardinality; Q-valued strength is extra.

Identity gates call I_card(n) and I_strength(n, q). The hostile predicate
that I_q(one lock) equals I_#(one lock) at q=3/2 must fail. Arithmetic uses
exact Fraction. No Newton coupling, no runner cache, no axiom edit.
"""

from __future__ import annotations

import inspect
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "UNIT_LOCK_I_IS_A_CARDINALITY_Q_STRENGTH_IS_EXTRA_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/UNIT_LOCK_I_IS_A_CARDINALITY_Q_STRENGTH_IS_EXTRA_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

MENU = ("plus", "minus")


def normalize(text: str) -> str:
    return " ".join(text.split())


def unit_lock_pattern(n: int, label: str = "plus") -> dict[int, str]:
    if n < 0:
        raise ValueError("lock count must be nonnegative")
    if label not in MENU:
        raise ValueError("label is not on the menu")
    return {site: label for site in range(n)}


def I_hash(pattern: dict[int, str]) -> int:
    return len(pattern)


def I_q_sum(pattern: dict[int, str], strengths: dict[int, Fraction]) -> Fraction:
    return sum((strengths[site] for site in pattern), start=Fraction(0))


def I_card(n: int) -> int:
    return I_hash(unit_lock_pattern(n))


def I_strength(n: int, q: Fraction) -> Fraction:
    q = Fraction(q)
    if q <= 0:
        raise ValueError("per-lock strength must be a positive rational")
    pattern = unit_lock_pattern(n)
    strengths = {site: q for site in pattern}
    return I_q_sum(pattern, strengths)


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


def identity_gates(checks: Checks) -> None:
    one = I_card(1)
    two = I_card(2)
    empty = I_card(0)
    q = Fraction(3, 2)
    one_strength = I_strength(1, q)
    two_strength = I_strength(2, q)
    recovered_one = I_strength(1, Fraction(1))
    recovered_two = I_strength(2, Fraction(1))

    checks.check(
        "theorem1-one-lock",
        "I_#(one lock)=1",
        one == 1,
    )
    checks.check(
        "theorem1-two-locks",
        "I_#(two disjoint locks)=2",
        two == 2,
    )
    checks.check(
        "theorem1-empty",
        "I_#(empty)=0",
        empty == 0,
    )
    checks.check(
        "theorem1-additivity",
        "I_# is additive on disjoint unit locks",
        one + one == two,
    )
    checks.check(
        "theorem2-unit-strength-recovers-card",
        "I_q with every q_x=1 recovers I_#",
        recovered_one == Fraction(one) and recovered_two == Fraction(two),
    )
    checks.check(
        "theorem2-three-halves-one",
        "I_q(one lock)=3/2 at q=3/2",
        one_strength == Fraction(3, 2),
    )
    checks.check(
        "theorem2-three-halves-two",
        "I_q(two locks)=3 at q=3/2",
        two_strength == Fraction(3),
    )
    checks.check(
        "theorem2-mismatch",
        "I_q differs from I_# at one lock when q=3/2",
        one_strength != Fraction(one),
    )


def mutation_strength_equals_card() -> bool:
    """Hostile predicate: I_q(one lock)=I_#(one lock) for q=3/2."""
    return I_strength(1, Fraction(3, 2)) == I_card(1)


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    note_norm = normalize(note)
    axiom_norm = normalize(axiom)

    print(
        "external_scientific_inputs: current Record wording is source-bound; "
        "no observational or fitted inputs are used"
    )
    print(
        "package_local_integrity_reads: the proposed source note is read for "
        "claim-surface consistency against the axiom memo"
    )

    checks.check(
        "source-record-lock",
        "the axiom names unit locking of one admissible local possibility",
        "a record locks exactly one admissible local possibility" in axiom_norm,
    )
    checks.check(
        "source-record-content",
        "the axiom determines readout by record content alone",
        "A readout value is determined by record content alone." in axiom_norm,
    )
    checks.check(
        "source-record-additivity",
        "the axiom names additive scalar I with I(empty)=0",
        "scalar readout `I` is additive, with `I(empty)=0`" in axiom_norm,
    )
    checks.check(
        "source-no-strength-dictionary",
        "the axiom memo does not name a Q-valued per-lock strength",
        all(
            needle not in axiom
            for needle in ("per-lock", "I_q", "q_x", "I_#", "lock strength")
        ),
    )

    one_lock = unit_lock_pattern(1)
    other_lock = {site + 10: label for site, label in unit_lock_pattern(1).items()}
    empty_lock: dict[int, str] = {}
    union_lock = {**one_lock, **other_lock}
    checks.check(
        "pattern-disjoint-union",
        "two singleton domains are disjoint and union to cardinality two",
        set(one_lock).isdisjoint(other_lock)
        and I_hash(union_lock) == I_hash(one_lock) + I_hash(other_lock)
        and I_hash(empty_lock) == 0,
    )

    identity_gates(checks)

    checks.check(
        "mutation-strength-equals-card",
        "the predicate I_q(one lock)=I_#(one lock) for q=3/2 fails",
        mutation_strength_equals_card() is False,
    )

    identity_source = inspect.getsource(identity_gates)
    checks.check(
        "identity-gates-call-card-and-strength",
        "identity gates call I_card(n) and I_strength(n, q)",
        "I_card(" in identity_source and "I_strength(" in identity_source,
    )

    checks.check(
        "note-cardinal-definition",
        "the note defines I_# as the domain cardinality",
        "`I_#(L) := |dom(L)|`" in note,
    )
    checks.check(
        "note-strength-definition",
        "the note defines I_q as a positive-rational domain sum",
        "`I_q(L) := sum_{x in dom(L)} q_x`" in note
        and "`q_x ∈ Q_{>0}`" in note,
    )
    checks.check(
        "note-display-not-adopt",
        "the note displays I_q and refuses adoption, Newton mass, and insufficiency rhetoric",
        all(
            phrase in note_norm
            for phrase in (
                "This note displays `I_q`.",
                "does not adopt `I_q`",
                "does not install it as Newton mass",
                "does not claim that `I_#` is insufficient for a later dictionary",
            )
        ),
    )
    checks.check(
        "note-theorem5-nonclaims",
        "the note refuses r=1/2 and L_phys",
        "does not force `r=1/2`" in note_norm and "does not adopt `L_phys`" in note_norm,
    )
    checks.check(
        "note-parent-is-axiom-memo",
        "the only named parent is the current axiom memo",
        "MINIMAL_AXIOMS_2026-06-29.md" in note
        and "That is the entire load-bearing parent." in note,
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
                "claim_type_reason:",
                "audit_required_before_effective_retained: true",
                "bare_retained_allowed: false",
            )
        ),
    )

    print("per_element: one lock, two disjoint locks, and the empty pattern are checked")
    print("per_site: each lock occupies one site and one menu entry")
    print("per_mode: two strength trials q=1 and q=3/2 are compared to I_#")
    print("per_block: the extra-dictionary block is I_q versus cardinal I_#")
    print("lattice_wide: checked and not executed — no lattice-wide dynamics is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
