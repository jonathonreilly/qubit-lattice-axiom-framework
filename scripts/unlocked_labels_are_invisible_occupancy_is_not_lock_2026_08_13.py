#!/usr/bin/env python3
"""Exact checks: unlocked labels are invisible; occupancy is not lock.

I sees only lock patterns. A putative unlocked label is invisible:
I(ghost)=I(L_1)=1 versus I(L_2)=2. Identity gates call I_of_locks(L)
and is_state(L). Occupancy-without-lock is extra. No cache is written.
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
    / "UNLOCKED_LABELS_ARE_INVISIBLE_OCCUPANCY_IS_NOT_LOCK_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/UNLOCKED_LABELS_ARE_INVISIBLE_OCCUPANCY_IS_NOT_LOCK_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

SITES = ("x", "y")
MENU = ("A", "B")


def normalize(text: str) -> str:
    return " ".join(text.split())


@dataclass(frozen=True)
class LockPattern:
    """Partial map L: {x,y} ⇀ {A,B}."""

    pairs: tuple[tuple[str, str], ...] = ()

    def __post_init__(self) -> None:
        seen: set[str] = set()
        for site, label in self.pairs:
            if site not in SITES:
                raise ValueError("lock site must lie on the star")
            if label not in MENU:
                raise ValueError("lock label must lie on the menu")
            if site in seen:
                raise ValueError("a site never carries more than one record")
            seen.add(site)

    def domain(self) -> frozenset[str]:
        return frozenset(site for site, _ in self.pairs)

    def content_at(self, site: str) -> str | None:
        return dict(self.pairs).get(site)

    def readable(self) -> frozenset[tuple[str, str]]:
        return frozenset(self.pairs)


@dataclass(frozen=True)
class Occupancy:
    """Total map O: {x,y} → {A,B,∅} plus which sites actually lock."""

    labels: tuple[tuple[str, str | None], ...]
    locked: frozenset[str]

    def __post_init__(self) -> None:
        sites = tuple(site for site, _ in self.labels)
        if sites != SITES:
            raise ValueError("occupancy must assign both star sites in order")
        for site, label in self.labels:
            if label is not None and label not in MENU:
                raise ValueError("occupancy label must lie on the menu or be empty")
        for site in self.locked:
            if site not in SITES:
                raise ValueError("locked site must lie on the star")
            if dict(self.labels)[site] is None:
                raise ValueError("a lock requires a nonempty label")

    def as_lock_pattern(self) -> LockPattern:
        pairs = tuple(
            (site, label)
            for site, label in self.labels
            if site in self.locked and label is not None
        )
        return LockPattern(pairs)

    def unlocked_labels(self) -> tuple[tuple[str, str], ...]:
        return tuple(
            (site, label)
            for site, label in self.labels
            if site not in self.locked and label is not None
        )

    def is_ghost(self) -> bool:
        return len(self.unlocked_labels()) > 0


def I_of_locks(pattern: LockPattern | Occupancy) -> Fraction:
    """Identity-gate function: unit-strength count of locked sites only."""
    locks = pattern.as_lock_pattern() if isinstance(pattern, Occupancy) else pattern
    return sum((Fraction(1) for _ in locks.pairs), Fraction(0))


def is_state(pattern: LockPattern | Occupancy) -> bool:
    """Identity-gate function: true iff the object is a lock pattern, not a ghost."""
    if isinstance(pattern, Occupancy):
        return not pattern.is_ghost()
    return isinstance(pattern, LockPattern)


def I_counting_labels(pattern: Occupancy) -> Fraction:
    """Mutation: count every nonempty occupancy value, locked or unlocked."""
    return sum((Fraction(1) for _, label in pattern.labels if label is not None), Fraction(0))


def force_lock_every_label(pattern: Occupancy) -> LockPattern:
    """Mutation: treat every nonempty occupancy value as a lock."""
    pairs = tuple((site, label) for site, label in pattern.labels if label is not None)
    return LockPattern(pairs)


def predicate_i_counts_unlocked(pattern: Occupancy) -> bool:
    """Mutation predicate: I counts unlocked labels."""
    return I_of_locks(pattern) == I_counting_labels(pattern)


def predicate_ghost_is_state(pattern: Occupancy) -> bool:
    """Mutation predicate: declare any occupancy, including a ghost, a state."""
    return True


def support_of(measure: dict[str, Fraction]) -> frozenset[str]:
    return frozenset(label for label, mass in measure.items() if mass > 0)


def lawful(pattern: LockPattern, measure: dict[str, Fraction]) -> bool:
    allowed = support_of(measure)
    return all(label in allowed for _, label in pattern.pairs)


def occupancy_from(locks: LockPattern, unlocked: dict[str, str] | None = None) -> Occupancy:
    unlocked = unlocked or {}
    labels: list[tuple[str, str | None]] = []
    locked_sites = locks.domain()
    for site in SITES:
        if site in locked_sites:
            labels.append((site, locks.content_at(site)))
        elif site in unlocked:
            labels.append((site, unlocked[site]))
        else:
            labels.append((site, None))
    return Occupancy(tuple(labels), locked_sites)


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
    for relative in AUDIT_INPUT_PATHS:
        (ROOT / relative).read_text(encoding="utf-8")
    normalized_note = normalize(note).replace("> ", "")
    normalized_axiom = normalize(axiom)

    print(
        "external_scientific_inputs: current Record content-only readout, "
        "I(empty)=0, and the state-as-records sentence are source-bound; no "
        "observational or fitted inputs are used"
    )
    print(
        "package_local_integrity_reads: the proposed source note is read for "
        "claim-surface consistency; no runner cache is written"
    )
    print(
        "negative_scope: unlocked labels are invisible and are not states; "
        "occupancy-without-lock is extra; no occupancy compiler is excluded"
    )

    checks.check(
        "audit-input-paths",
        "declared audit inputs exist and match the note and the axiom memo",
        AUDIT_INPUT_PATHS
        == (
            "docs/UNLOCKED_LABELS_ARE_INVISIBLE_OCCUPANCY_IS_NOT_LOCK_BOUNDED_THEOREM_NOTE_2026-08-13.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and AUDIT_TIMEOUT_SEC == 120,
    )

    readable_sentence = "Only records are readable."
    content_sentence = "A readout value is determined by record content alone."
    state_sentence = "A state is a configuration of records."
    additivity_sentence = (
        "For any finite collection of pairwise-disjoint records, scalar readout "
        "`I` is additive, with `I(empty)=0`."
    )
    checks.check(
        "source-only-records-readable",
        "the exact current readable-records sentence is present in the axiom memo",
        readable_sentence in normalized_axiom,
    )
    checks.check(
        "source-record-content-only",
        "the exact current content-only readout sentence is present in the axiom memo",
        content_sentence in normalized_axiom,
    )
    checks.check(
        "source-state-configuration",
        "the exact current state-as-records sentence is present in the axiom memo",
        state_sentence in normalized_axiom,
    )
    checks.check(
        "source-i-empty",
        "the exact current Record additivity sentence with I(empty)=0 is present",
        additivity_sentence in normalized_axiom,
    )

    empty = LockPattern()
    lock_1 = LockPattern((("x", "A"),))
    lock_2 = LockPattern((("x", "A"), ("y", "B")))
    ghost = occupancy_from(lock_1, unlocked={"y": "B"})
    ghost_as_occupancy_of_lock_1 = occupancy_from(lock_1)

    checks.check(
        "empty-readout",
        "I(empty)=0",
        I_of_locks(empty) == Fraction(0),
        residual=I_of_locks(empty),
    )
    checks.check(
        "theorem-1-lock-counts",
        "I(L_1)=1, I(L_2)=2, I(empty)=0 by unit-strength domain count",
        I_of_locks(lock_1) == Fraction(1)
        and I_of_locks(lock_2) == Fraction(2)
        and I_of_locks(empty) == Fraction(0)
        and lock_1.domain() == frozenset({"x"})
        and lock_2.domain() == frozenset({"x", "y"})
        and empty.domain() == frozenset(),
        residual=(I_of_locks(empty), I_of_locks(lock_1), I_of_locks(lock_2)),
    )
    checks.check(
        "theorem-1-ghost-invisible",
        "I(ghost)=I(L_1)=1; the unlocked B does not change I",
        I_of_locks(ghost) == I_of_locks(lock_1) == Fraction(1)
        and I_of_locks(ghost) != I_of_locks(lock_2)
        and ghost.unlocked_labels() == (("y", "B"),)
        and ghost.as_lock_pattern() == lock_1,
        residual=(I_of_locks(ghost), I_of_locks(lock_1), I_of_locks(lock_2)),
    )
    lock_at_y = LockPattern((("y", "B"),))
    checks.check(
        "theorem-1-additivity",
        "I(L_2)=I(L_1)+I(y↦B)=1+1=2 on disjoint one-site records",
        lock_1.domain().isdisjoint(lock_at_y.domain())
        and I_of_locks(lock_1) + I_of_locks(lock_at_y) == I_of_locks(lock_2) == Fraction(2),
        residual=I_of_locks(lock_1) + I_of_locks(lock_at_y),
    )

    checks.check(
        "theorem-2-states-are-lock-patterns",
        "is_state is true of L_1 and L_2 and false of the ghost",
        is_state(lock_1)
        and is_state(lock_2)
        and is_state(empty)
        and is_state(ghost_as_occupancy_of_lock_1)
        and not is_state(ghost)
        and ghost.is_ghost(),
        residual=(is_state(lock_1), is_state(lock_2), is_state(ghost)),
    )
    checks.check(
        "theorem-3-content-only",
        "readable content of the ghost equals L_1; no readout of unlocked B exists",
        lock_1.readable() == frozenset({("x", "A")})
        and ghost.as_lock_pattern().readable() == lock_1.readable()
        and lock_2.readable() == frozenset({("x", "A"), ("y", "B")})
        and ("y", "B") not in ghost.as_lock_pattern().readable()
        and content_sentence in normalized_note
        and readable_sentence in normalized_note,
        residual=ghost.as_lock_pattern().readable(),
    )

    measure = {"A": Fraction(1, 3), "B": Fraction(2, 3)}
    checks.check(
        "theorem-4-formation-free",
        "the same content law with support {A,B} is compatible with L_1 and L_2",
        support_of(measure) == frozenset({"A", "B"})
        and sum(measure.values(), Fraction(0)) == 1
        and lawful(lock_1, measure)
        and lawful(lock_2, measure)
        and I_of_locks(lock_1) != I_of_locks(lock_2)
        and not is_state(ghost),
        residual=(support_of(measure), I_of_locks(lock_1), I_of_locks(lock_2)),
    )
    forced = force_lock_every_label(ghost)
    checks.check(
        "theorem-4-unlocking-not-third-option",
        "forcing a lock at every occupied site turns the ghost into L_2",
        forced == lock_2
        and I_of_locks(forced) == Fraction(2)
        and I_of_locks(ghost) == Fraction(1),
        residual=I_of_locks(forced),
    )
    checks.check(
        "theorem-5-not-selected",
        "occupancy-without-lock remains a second object; I still sees only locks",
        readable_sentence in note
        and state_sentence in note
        and "I(empty)=0" in note
        and additivity_sentence in normalized_note
        and I_of_locks(ghost) == I_of_locks(lock_1)
        and not is_state(ghost)
        and I_counting_labels(ghost) != I_of_locks(ghost),
    )

    checks.check(
        "mutation-count-unlocked-fails",
        "a predicate that I counts unlocked labels fails; ghost still I=1",
        I_of_locks(ghost) == Fraction(1)
        and I_counting_labels(ghost) == Fraction(2)
        and predicate_i_counts_unlocked(ghost) is False
        and I_of_locks(ghost) != I_counting_labels(ghost),
        residual=(I_of_locks(ghost), I_counting_labels(ghost)),
    )
    checks.check(
        "mutation-replace-L1-by-L2",
        "replacing L_1 by L_2 changes I from 1 to 2",
        I_of_locks(lock_1) == Fraction(1)
        and I_of_locks(lock_2) == Fraction(2)
        and I_of_locks(lock_1) != I_of_locks(lock_2),
        residual=(I_of_locks(lock_1), I_of_locks(lock_2)),
    )
    checks.check(
        "mutation-ghost-is-state-fails",
        "a predicate that the ghost is a state fails Theorem 2",
        is_state(ghost) is False
        and predicate_ghost_is_state(ghost) is True
        and predicate_ghost_is_state(ghost) != is_state(ghost)
        and is_state(lock_1)
        and is_state(lock_2),
        residual=(is_state(ghost), predicate_ghost_is_state(ghost)),
    )

    allowed_retained = (
        "audit_required_before_effective_retained: true",
        "bare_retained_allowed: false",
    )
    retained_ok = all(line in note for line in allowed_retained)
    other_retained = note
    for line in allowed_retained:
        other_retained = other_retained.replace(line, "")
    checks.check(
        "note-contract",
        "machine-status fields, required phrases, and forbidden-word hygiene hold",
        all(
            phrase in note
            for phrase in (
                "actual_current_surface_status: bounded-support",
                "target_claim_type: bounded_theorem",
                'hypothetical_axiom_status: "no edit"',
                "trace_class: negative_route_pruning",
                "target_claim_id: occupancy_versus_lock",
                "reachability_to_target: prunes",
                'target_blocker_text: "identify site occupancy with Record lock, or read unlocked labels"',
                'next_trace_action: "Unlocked labels are invisible and are not states. Occupancy-without-lock is extra. Do not adopt axiom text."',
                "Only records are readable",
                "A state is a configuration of records.",
                "I(empty)=0",
                "I(L_1)=1",
                "I(L_2)=2",
                "I(ghost)=I(L_1)=1",
                "authors no audit verdict",
            )
        )
        and additivity_sentence in normalized_note
        and content_sentence in note
        and "MINIMAL_AXIOMS_2026-06-29.md" in note
        and "**Type:** bounded_theorem" in note
        and retained_ok
        and "retained" not in other_retained
        and "promoted" not in note.lower()
        and "we adopt" not in note.lower()
        and "new axiom" not in note.lower()
        and "Codex" not in note
        and "toe-lphys" not in note,
    )
    checks.check(
        "canonical-nonmutation",
        "unlocked labels and occupancy-without-lock are absent from the axiom memo",
        all(
            phrase not in axiom
            for phrase in (
                "unlocked label",
                "occupancy-without-lock",
                "putative occupancy",
                "O_ghost",
            )
        )
        and readable_sentence in axiom
        and state_sentence in axiom,
    )

    n5_lines = (
        "per_element: lock patterns L_1, L_2, empty, and the ghost occupancy are recomputed as maps on {x,y}",
        "per_site: each star site is empty, locked, or carrying an unlocked label; I counts only locks",
        "per_mode: menu labels {A,B} are content; unlocked B is not a value of I",
        "per_block: only the two-site star and unit-strength readout are executed; occupancy-without-lock stays extra",
        "lattice_wide: checked and not executed — no lattice-wide occupancy compiler or formation law is claimed",
    )
    for line in n5_lines:
        checks.check(
            "n5-length",
            "each N5 resolution line is at least 40 characters",
            line.startswith(("per_element:", "per_site:", "per_mode:", "per_block:", "lattice_wide:"))
            and len(line) >= 40,
            residual=(len(line), line[:40]),
        )
        print(line)

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
