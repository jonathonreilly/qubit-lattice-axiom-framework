#!/usr/bin/env python3
"""Exact integer checks for the I / bag / o / J Record-readout classification.

The runner reconstructs two-site occupancy/lock arithmetic and compares four
displayed readouts on five stipulated histories. None of the readouts is
adopted. No pairing, r=1/2, L_phys, or fifth extra is introduced.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "RECORD_READOUT_CLASSIFICATION_I_BAG_O_J_HYPOTHETICAL_BOUNDED_THEOREM_NOTE_2026-08-13.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/RECORD_READOUT_CLASSIFICATION_I_BAG_O_J_HYPOTHETICAL_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

EMPTY = 0
A = "A"
B = "B"
W = ("x", "y")
M = (A, B)


@dataclass(frozen=True)
class History:
    """Occupancy bits together with the unique lock at each occupied site."""

    occupancy: tuple[int, int]
    locks: tuple[object, object]

    def __post_init__(self) -> None:
        for bit, lock in zip(self.occupancy, self.locks):
            if bit not in (0, 1):
                raise ValueError("occupancy must be a {0,1}-bit")
            if bit == 0 and lock is not EMPTY:
                raise ValueError("empty site carries no lock")
            if bit == 1 and lock not in M:
                raise ValueError("occupied site must lock a menu entry")


H10A = History((1, 0), (A, EMPTY))
H10B = History((1, 0), (B, EMPTY))
H01A = History((0, 1), (EMPTY, A))
H11AB = History((1, 1), (A, B))
H11BA = History((1, 1), (B, A))
FIVE = (H10A, H10B, H01A, H11AB, H11BA)


def I_of(history: History) -> int:
    return history.occupancy[0] + history.occupancy[1]


def o_of(history: History) -> tuple[int, int]:
    return history.occupancy


def J_of(history: History) -> tuple[object, object]:
    return history.locks


def bag_of(history: History) -> tuple[int, tuple[object, ...]]:
    locks = tuple(sorted(lock for lock in J_of(history) if lock is not EMPTY))
    return (I_of(history), locks)


def lock_J(j_map: tuple[object, object], site_index: int) -> object | None:
    value = j_map[site_index]
    return None if value is EMPTY else value


def splits(left, right) -> bool:
    return left != right


def normalize(text: str) -> str:
    return " ".join(text.split())


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
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    normalized_axiom = normalize(axiom)
    normalized_note = normalize(note).replace("> ", "")

    print("external_scientific_inputs: current axiom wording is source-bound; occupancy/lock arithmetic is reconstructed; no observational or fitted inputs are used")
    print("package_local_integrity_reads: the proposed source note is read for claim-surface consistency")
    print("negative_scope: the four displayed readouts are compared on five histories; none is adopted")

    checks.check(
        "source-records-form",
        "the current Record section opens with Records form",
        "Records form." in axiom,
    )
    checks.check(
        "source-content-only",
        "readout is determined by record content alone and I is additive with I(empty)=0",
        "A readout value is determined by record content alone." in normalized_axiom
        and "scalar readout `I` is additive, with `I(empty)=0`." in normalize(axiom),
    )
    checks.check(
        "source-neither-o-nor-J",
        "current Record names scalar I and does not name occupancy o or site-indexed J",
        "scalar readout `I` is additive, with `I(empty)=0`." in normalized_axiom
        and "site-indexed J" not in axiom
        and "site-blind bag" not in axiom
        and "o:W" not in axiom,
    )

    # Identity gates MUST call I_of, bag_of, o_of, J_of on the five histories.
    i_h10A, bag_h10A, o_h10A, j_h10A = I_of(H10A), bag_of(H10A), o_of(H10A), J_of(H10A)
    i_h10B, bag_h10B, o_h10B, j_h10B = I_of(H10B), bag_of(H10B), o_of(H10B), J_of(H10B)
    i_h01A, bag_h01A, o_h01A, j_h01A = I_of(H01A), bag_of(H01A), o_of(H01A), J_of(H01A)
    i_h11AB, bag_h11AB, o_h11AB, j_h11AB = I_of(H11AB), bag_of(H11AB), o_of(H11AB), J_of(H11AB)
    i_h11BA, bag_h11BA, o_h11BA, j_h11BA = I_of(H11BA), bag_of(H11BA), o_of(H11BA), J_of(H11BA)

    checks.check(
        "identity-five-histories",
        "I_of, bag_of, o_of, J_of match the displayed table on all five histories",
        (
            (i_h10A, bag_h10A, o_h10A, j_h10A) == (1, (1, (A,)), (1, 0), (A, EMPTY))
            and (i_h10B, bag_h10B, o_h10B, j_h10B) == (1, (1, (B,)), (1, 0), (B, EMPTY))
            and (i_h01A, bag_h01A, o_h01A, j_h01A) == (1, (1, (A,)), (0, 1), (EMPTY, A))
            and (i_h11AB, bag_h11AB, o_h11AB, j_h11AB) == (2, (2, (A, B)), (1, 1), (A, B))
            and (i_h11BA, bag_h11BA, o_h11BA, j_h11BA) == (2, (2, (A, B)), (1, 1), (B, A))
        ),
    )

    checks.check(
        "theorem-1-site-column",
        "I and bag fail to split h10A from h01A; occupancy and J split them",
        i_h10A == i_h01A == 1
        and bag_h10A == bag_h01A == (1, (A,))
        and splits(o_h10A, o_h01A)
        and splits(j_h10A, j_h01A)
        and o_h10A == (1, 0)
        and o_h01A == (0, 1)
        and j_h10A == (A, EMPTY)
        and j_h01A == (EMPTY, A),
    )
    checks.check(
        "theorem-2-lock-column",
        "I and occupancy fail to split h10A from h10B; bag and J split them",
        i_h10A == i_h10B == 1
        and o_h10A == o_h10B == (1, 0)
        and splits(bag_h10A, bag_h10B)
        and splits(j_h10A, j_h10B)
        and bag_h10A == (1, (A,))
        and bag_h10B == (1, (B,))
        and j_h10A == (A, EMPTY)
        and j_h10B == (B, EMPTY),
    )
    checks.check(
        "theorem-3-ordered-locks",
        "I, bag, and occupancy fail to split h11AB from h11BA; only J splits them",
        i_h11AB == i_h11BA == 2
        and bag_h11AB == bag_h11BA == (2, (A, B))
        and o_h11AB == o_h11BA == (1, 1)
        and splits(j_h11AB, j_h11BA)
        and j_h11AB == (A, B)
        and j_h11BA == (B, A),
    )

    recovered = tuple(
        tuple(lock_J(J_of(history), index) for index in range(2))
        for history in FIVE
    )
    expected_locks = (
        (A, None),
        (B, None),
        (None, A),
        (A, B),
        (B, A),
    )
    named_site = 0
    lock_at_x = tuple(lock_J(J_of(history), named_site) for history in (H10A, H10B, H11AB, H11BA))
    checks.check(
        "theorem-4-lock-recovery",
        "lock_J recovers every lock; no map of o, I, or bag recovers the lock at x on the displayed set",
        recovered == expected_locks
        and lock_at_x == (A, B, A, B)
        and o_of(H10A) == o_of(H10B)
        and I_of(H10A) == I_of(H10B)
        and o_of(H11AB) == o_of(H11BA)
        and I_of(H11AB) == I_of(H11BA)
        and bag_of(H11AB) == bag_of(H11BA)
        and all(value in M for value in J_of(H11AB))
        and all(value in (0, 1) for value in o_of(H11AB)),
    )

    predicate_I_splits_h10A_h01A = splits(I_of(H10A), I_of(H01A))
    predicate_bag_splits_h11AB_h11BA = splits(bag_of(H11AB), bag_of(H11BA))
    predicate_o_splits_h10A_h10B = splits(o_of(H10A), o_of(H10B))
    predicate_J_h10A_eq_h01A = J_of(H10A) == J_of(H01A)
    predicate_J_h11AB_eq_h11BA = J_of(H11AB) == J_of(H11BA)
    checks.check(
        "mutation-predicates",
        "the five hostile predicates fail: I site-split, bag order-split, o lock-split, J site-equality, J order-equality",
        not predicate_I_splits_h10A_h01A
        and not predicate_bag_splits_h11AB_h11BA
        and not predicate_o_splits_h10A_h10B
        and not predicate_J_h10A_eq_h01A
        and not predicate_J_h11AB_eq_h11BA,
    )

    checks.check(
        "machine-status-contract",
        "the source uses the required hypothetical and bounded-support status fields",
        all(
            phrase in note
            for phrase in (
                'hypothetical_axiom_status: "C1 follow-on: classify Record readouts I / (I,bag) / o / J; none adopted"',
                "actual_current_surface_status: bounded-support",
                "target_claim_type: bounded_theorem",
                "trace_class: negative_route_pruning",
                "audit_required_before_effective_retained: true",
                "bare_retained_allowed: false",
            )
        ),
    )
    checks.check(
        "theorem-5-negatives",
        "the note refuses pairing on J, r=1/2, L_phys, a fifth extra, and adoption",
        all(
            phrase in normalized_note
            for phrase in (
                "does not put a pairing on `J`",
                "does not force `r=1/2`",
                "does not adopt `L_phys`",
                "does not name a fifth extra",
                "None is adopted",
            )
        ),
    )
    checks.check(
        "displayed-table",
        "the note displays the five-history readout table and the three-column split summary",
        "| `h10A` | `(1,0)` |" in note
        and "| `h11BA` | `(1,1)` |" in note
        and "| `h11AB` vs `h11BA` (order) | same | same | same | split |" in note,
    )
    checks.check(
        "no-go-gate",
        "all N1-N8 sections and the broad-claim rejection are source-visible",
        all(f"### N{index}" in note for index in range(1, 9))
        and "FAIL / DO NOT SHIP" in note
        and "an axiom update is necessary" in note,
    )
    checks.check(
        "canonical-nonmutation",
        "the hypothetical bag/J classification notation is absent from the canonical axiom file",
        all(phrase not in axiom for phrase in ("h10A", "h11BA", "site-blind bag", "lock_J")),
    )
    checks.check(
        "audit-input-paths",
        "declared inputs are exactly the new note and the axiom memo",
        AUDIT_INPUT_PATHS
        == (
            "docs/RECORD_READOUT_CLASSIFICATION_I_BAG_O_J_HYPOTHETICAL_BOUNDED_THEOREM_NOTE_2026-08-13.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file(),
    )

    print("per_element: five histories and four readouts are checked by I_of, bag_of, o_of, J_of")
    print("per_site: named sites x and y are compared; no lattice-wide formation rule is asserted")
    print("per_mode: site column, lock column, and ordered two-site column are the only modes tested")
    print("per_block: Record readout type is the only negative block tested")
    print("lattice_wide: checked and not executed — no lattice-wide dynamics or axiom necessity is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
