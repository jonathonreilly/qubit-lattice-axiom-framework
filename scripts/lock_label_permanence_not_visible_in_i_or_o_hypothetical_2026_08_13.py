#!/usr/bin/env python3
"""Exact integer checks: lock-label permanence is not visible in I or o.

A legal stay and an illegal same-site relock share I-seq and o-seq.
The site-blind bag and site-indexed J split them. Values are computed
from the displayed J field. Unit-count I=1 is a convention.
"""

from __future__ import annotations

from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    ROOT
    / "docs"
    / "LOCK_LABEL_PERMANENCE_NOT_VISIBLE_IN_I_OR_O_HYPOTHETICAL_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/LOCK_LABEL_PERMANENCE_NOT_VISIBLE_IN_I_OR_O_HYPOTHETICAL_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

EMPTY = 0
A = "A"
B = "B"

# Histories are pairs of J snapshots (J(x), J(y)).
S = ((A, EMPTY), (A, EMPTY))
R = ((A, EMPTY), (B, EMPTY))
MOVE = ((A, EMPTY), (EMPTY, A))


def occupancy(snapshot: tuple) -> tuple[int, int]:
    return tuple(0 if value == EMPTY else 1 for value in snapshot)


def I_of(snapshot: tuple) -> int:
    """Unit-count convention: each occupied site contributes 1."""
    return sum(occupancy(snapshot))


def bag_of(snapshot: tuple) -> frozenset:
    return frozenset(value for value in snapshot if value != EMPTY)


def I_seq(history: tuple) -> tuple:
    return tuple(I_of(snapshot) for snapshot in history)


def o_seq(history: tuple) -> tuple:
    return tuple(occupancy(snapshot) for snapshot in history)


def bag_seq(history: tuple) -> tuple:
    return tuple(bag_of(snapshot) for snapshot in history)


def J_seq(history: tuple) -> tuple:
    return tuple(history)


def i_seq_differs(left: tuple, right: tuple) -> bool:
    return I_seq(left) != I_seq(right)


def o_seq_differs(left: tuple, right: tuple) -> bool:
    return o_seq(left) != o_seq(right)


def j_seq_equal(left: tuple, right: tuple) -> bool:
    return J_seq(left) == J_seq(right)


def I_scaled(snapshot: tuple, unit: int) -> int:
    return unit * I_of(snapshot)


def additive_on_sites(unit: int) -> bool:
    lock_x = (A, EMPTY)
    lock_y = (EMPTY, B)
    both = (A, B)
    empty = (EMPTY, EMPTY)
    return (
        I_scaled(empty, unit) == 0
        and I_scaled(lock_x, unit) + I_scaled(lock_y, unit)
        == I_scaled(both, unit) + I_scaled(empty, unit)
    )


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


def normalize(text: str) -> str:
    return " ".join(text.split())


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    runner_source = Path(__file__).read_text(encoding="utf-8")
    norm_note = normalize(note)
    norm_axiom = normalize(axiom)

    print(
        "external_scientific_inputs: current axiom wording only; "
        "J arithmetic is reconstructed in this runner"
    )
    print(
        "package_local_integrity_reads: the proposed source note is read "
        "for claim-surface consistency"
    )

    checks.check(
        "source-permanence",
        "Record states that records are permanent",
        "records are permanent" in norm_axiom,
    )
    checks.check(
        "source-locks-exactly-one",
        "Record states that a record locks exactly one admissible local possibility",
        "locks exactly one admissible local possibility" in norm_axiom,
    )
    checks.check(
        "source-additivity",
        "Record names additive scalar I with I(empty)=0",
        "scalar readout `I` is additive, with `I(empty)=0`" in axiom
        or "I(empty)=0" in axiom,
    )
    checks.check(
        "note-hypothetical-status",
        "note carries the required hypothetical axiom status",
        'hypothetical_axiom_status: "C1 follow-on: lock-label permanence not visible in I or o; J and bag split relock; not adopted"'
        in note,
    )
    checks.check(
        "note-surface-status",
        "note is bounded-support and not adopted",
        "actual_current_surface_status: bounded-support" in note
        and "not adopted" in note,
    )

    # Identity gates: must call I_seq, o_seq, bag_seq, J_seq on S and R.
    i_s = I_seq(S)
    i_r = I_seq(R)
    o_s = o_seq(S)
    o_r = o_seq(R)
    bag_s = bag_seq(S)
    bag_r = bag_seq(R)
    j_s = J_seq(S)
    j_r = J_seq(R)

    print(f"identity_gate I_seq(S)={i_s}")
    print(f"identity_gate I_seq(R)={i_r}")
    print(f"identity_gate o_seq(S)={o_s}")
    print(f"identity_gate o_seq(R)={o_r}")
    print(f"identity_gate bag_seq(S)={tuple(sorted(item) for item in bag_s)}")
    print(f"identity_gate bag_seq(R)={tuple(sorted(item) for item in bag_r)}")
    print(f"identity_gate J_seq(S)={j_s}")
    print(f"identity_gate J_seq(R)={j_r}")

    checks.check(
        "identity-gate-calls",
        "runner source calls I_seq, o_seq, bag_seq, J_seq on S and R",
        all(
            f"{name}(S)" in runner_source and f"{name}(R)" in runner_source
            for name in ("I_seq", "o_seq", "bag_seq", "J_seq")
        ),
    )
    checks.check(
        "occupancy-stays-at-x",
        "both histories keep one unit lock at x",
        o_s == ((1, 0), (1, 0)) and o_r == ((1, 0), (1, 0)),
    )
    checks.check(
        "I-seq-both",
        "I-seq of stay and relock is (1,1) by unit count",
        i_s == (1, 1) and i_r == (1, 1),
    )
    checks.check(
        "mutation-I-seq-differs",
        "predicate I_seq(S) differs from I_seq(R) fails",
        i_seq_differs(S, R) is False,
    )
    checks.check(
        "mutation-o-seq-differs",
        "predicate o_seq(S) differs from o_seq(R) fails",
        o_seq_differs(S, R) is False,
    )
    checks.check(
        "bag-stay",
        "site-blind bag of stay is ({A},{A})",
        bag_s == (frozenset({A}), frozenset({A})),
    )
    checks.check(
        "bag-relock",
        "site-blind bag of relock is ({A},{B})",
        bag_r == (frozenset({A}), frozenset({B})),
    )
    checks.check(
        "bag-splits",
        "bag_seq splits stay from relock",
        bag_s != bag_r,
    )
    checks.check(
        "J-seq-values",
        "J-seq is ((A,0),(A,0)) on stay and ((A,0),(B,0)) on relock",
        j_s == ((A, EMPTY), (A, EMPTY)) and j_r == ((A, EMPTY), (B, EMPTY)),
    )
    checks.check(
        "mutation-J-seq-equal",
        "predicate J_seq(S)=J_seq(R) fails",
        j_seq_equal(S, R) is False,
    )

    i_move = I_seq(MOVE)
    o_move = o_seq(MOVE)
    bag_move = bag_seq(MOVE)
    j_move = J_seq(MOVE)
    checks.check(
        "site-move-contrast",
        "reconstructed site-move shares I and bag with stay, not o or J",
        i_move == i_s
        and bag_move == bag_s
        and o_move != o_s
        and j_move != j_s
        and o_move == ((1, 0), (0, 1))
        and j_move == ((A, EMPTY), (EMPTY, A)),
    )
    checks.check(
        "visibility-split",
        "J sees move and relock; o sees only the move; bag sees only the relock",
        j_move != j_s
        and j_r != j_s
        and o_move != o_s
        and o_r == o_s
        and bag_move == bag_s
        and bag_r != bag_s,
    )
    checks.check(
        "unit-count-convention",
        "I=1 is a unit convention; additivity also holds for unit 2",
        I_of((A, EMPTY)) == 1
        and additive_on_sites(1)
        and additive_on_sites(2)
        and I_scaled((A, EMPTY), 2) == 2,
    )
    checks.check(
        "not-formation",
        "occupancy count stays 1; this is not a formation-rate history",
        i_s == (1, 1) and i_r == (1, 1) and I_of(S[0]) == I_of(S[1]),
    )
    checks.check(
        "not-site-change",
        "relock keeps the occupied site; it is not a site move",
        occupancy(R[0]) == occupancy(R[1]) == (1, 0)
        and occupancy(MOVE[0]) != occupancy(MOVE[1]),
    )
    checks.check(
        "note-forbids-relock-quotes",
        "note quotes permanence and locks-exactly-one as jointly forbidding relock",
        "records are permanent" in norm_note
        and "locks exactly one" in norm_note
        and "forbid relock" in norm_note,
    )
    checks.check(
        "display-only",
        "note does not force r=1/2, adopt L_phys, or put a pairing on J",
        "Do not force `r=1/2`" in note
        and "Do not adopt" in note
        and "`L_phys`" in note
        and "Do not put a pairing on `J`" in note,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
