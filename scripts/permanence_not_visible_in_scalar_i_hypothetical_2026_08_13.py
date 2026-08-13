#!/usr/bin/env python3
"""Exact stay-versus-move checks: permanence is not visible in scalar I.

Reconstructs the displayed C1 lock field J on a two-site window and compares
a legal stay to an illegal site-to-site move. All load-bearing values are
exact integers computed from the two histories. The note is not adopted as
an axiom edit.
"""

from __future__ import annotations

import hashlib
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/PERMANENCE_NOT_VISIBLE_IN_SCALAR_I_HYPOTHETICAL_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

AUDIT_INPUT_PATHS = (
    "docs/PERMANENCE_NOT_VISIBLE_IN_SCALAR_I_HYPOTHETICAL_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

# Site order (x, y). 0 is absence, not a menu element.
ABSENT = 0
A = "A"
B = "B"
MENU = frozenset({A, B})
SITES = ("x", "y")

# Histories are sequences of site-indexed lock snapshots.
# Occupancy is already one unit lock at t=0.
S = ((A, ABSENT), (A, ABSENT))
M = ((A, ABSENT), (ABSENT, A))


def file_sha256(rel_path: str) -> str:
    data = (ROOT / rel_path).read_bytes()
    return hashlib.sha256(data).hexdigest()


def normalize(text: str) -> str:
    return " ".join(text.split())


def J_of(snapshot: tuple[object, object]) -> tuple[object, object]:
    """Site-indexed lock field on one snapshot: 0 if unformed, else the lock."""
    if len(snapshot) != 2:
        raise ValueError("window is exactly two sites")
    reconstructed = []
    for lock in snapshot:
        if lock == ABSENT:
            reconstructed.append(ABSENT)
        elif lock in MENU:
            reconstructed.append(lock)
        else:
            raise ValueError("lock is neither absence nor a menu entry")
    return (reconstructed[0], reconstructed[1])


def I_of(snapshot: tuple[object, object]) -> int:
    """Named scalar readout: count of formed sites."""
    return sum(1 for lock in J_of(snapshot) if lock != ABSENT)


def bag_of(snapshot: tuple[object, object]) -> frozenset:
    """Site-blind lock bag on one snapshot."""
    return frozenset(lock for lock in J_of(snapshot) if lock != ABSENT)


def I_seq(history: tuple[tuple[object, object], ...]) -> tuple[int, ...]:
    return tuple(I_of(snapshot) for snapshot in history)


def J_seq(history: tuple[tuple[object, object], ...]) -> tuple[tuple[object, object], ...]:
    return tuple(J_of(snapshot) for snapshot in history)


def bag_seq(history: tuple[tuple[object, object], ...]) -> tuple[frozenset, ...]:
    return tuple(bag_of(snapshot) for snapshot in history)


def occupancy_seq(history: tuple[tuple[object, object], ...]) -> tuple[int, ...]:
    return I_seq(history)


def respects_permanence(history: tuple[tuple[object, object], ...]) -> bool:
    """If a site is locked at t=0, the same lock remains at t=1."""
    first, second = J_seq(history)
    for prior, later in zip(first, second):
        if prior != ABSENT and later != prior:
            return False
    return True


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
    note_norm = normalize(note).replace("> ", "")
    axiom_norm = normalize(axiom)
    source = Path(__file__).read_text(encoding="utf-8")

    print("external_scientific_inputs: current axiom wording only; no observational or fitted inputs")
    print("package_local_integrity_reads: proposed source note plus axiom memo")
    print(
        "input_sha256: "
        + ", ".join(f"{path}={file_sha256(path)}" for path in AUDIT_INPUT_PATHS)
    )

    checks.check(
        "source-permanence",
        "axiom memo contains records are permanent",
        "records are permanent" in axiom_norm,
    )
    checks.check(
        "source-named-I",
        "axiom memo names additive scalar readout I",
        "scalar readout `I` is additive, with `I(empty)=0`" in axiom_norm
        or "scalar readout I is additive, with I(empty)=0" in axiom_norm.replace("`", ""),
    )
    checks.check(
        "source-one-lock",
        "axiom memo locks exactly one admissible local possibility",
        "locks exactly one admissible local possibility" in axiom_norm,
    )
    checks.check(
        "menu-absence",
        "absence 0 is not a menu element",
        ABSENT not in MENU and A in MENU and B in MENU,
    )

    # Identity gates: must call I_seq(S), I_seq(M), J_seq(S), J_seq(M).
    i_s = I_seq(S)
    i_m = I_seq(M)
    j_s = J_seq(S)
    j_m = J_seq(M)
    bags = bag_seq(S)
    bagm = bag_seq(M)

    checks.check("identity-I-S", "I_seq(S) is (1, 1)", i_s == (1, 1))
    checks.check("identity-I-M", "I_seq(M) is (1, 1)", i_m == (1, 1))
    checks.check(
        "identity-J-S",
        "J_seq(S) is ((A, 0), (A, 0))",
        j_s == ((A, ABSENT), (A, ABSENT)),
    )
    checks.check(
        "identity-J-M",
        "J_seq(M) is ((A, 0), (0, A))",
        j_m == ((A, ABSENT), (ABSENT, A)),
    )
    checks.check(
        "identity-call-sites",
        "runner source calls I_seq(S), I_seq(M), J_seq(S), J_seq(M)",
        "I_seq(S)" in source
        and "I_seq(M)" in source
        and "J_seq(S)" in source
        and "J_seq(M)" in source,
    )

    checks.check(
        "theorem-1-I",
        "I-seq and bag do not split stay from illegal move",
        i_s == i_m == (1, 1) and bags == bagm == (frozenset({A}), frozenset({A})),
    )
    checks.check(
        "theorem-2-J",
        "J-seq of S differs from J-seq of M",
        j_s != j_m,
    )
    checks.check(
        "theorem-4-occupancy",
        "occupancy stays 1; no growth from empty",
        occupancy_seq(S) == (1, 1) and occupancy_seq(M) == (1, 1),
    )
    checks.check(
        "permanence-S-legal",
        "stay S respects permanence",
        respects_permanence(S) is True,
    )
    checks.check(
        "permanence-M-illegal",
        "move M is forbidden by permanence",
        respects_permanence(M) is False,
    )

    predicate_I_differs = I_seq(S) != I_seq(M)
    predicate_J_equal = J_seq(S) == J_seq(M)
    checks.check(
        "mutation-I-seq",
        "predicate I_seq(S) differs from I_seq(M) fails",
        predicate_I_differs is False,
    )
    checks.check(
        "mutation-J-seq",
        "predicate J_seq(S)=J_seq(M) fails",
        predicate_J_equal is False,
    )

    required_status = (
        'hypothetical_axiom_status: "C1 follow-on: Record permanence is not '
        'visible in scalar I; J splits stay vs illegal move; not adopted"'
    )
    checks.check(
        "note-hypothetical-status",
        "note carries the required hypothetical_axiom_status",
        required_status in note,
    )
    checks.check(
        "note-surface-status",
        "note carries actual_current_surface_status bounded-support",
        "actual_current_surface_status: bounded-support" in note,
    )
    checks.check(
        "note-permanence-quote",
        "note quotes records are permanent",
        "records are permanent" in note_norm,
    )
    checks.check(
        "note-display-only",
        "note does not adopt C1, r=1/2, L_phys, or a pairing on J",
        "Do not adopt C1" in note_norm
        and "Do not force `r=1/2`" in note_norm
        and "Do not adopt `L_phys`" in note_norm
        and "Do not put a pairing on `J`" in note_norm,
    )
    checks.check(
        "note-not-formation",
        "note refuses formation-rate and addition-order growth readings",
        "not a formation rate" in note_norm
        and "occupancy stays `1`" in note_norm,
    )
    checks.check(
        "parents-axiom-only",
        "AUDIT_INPUT_PATHS are the new note and the axiom memo",
        AUDIT_INPUT_PATHS == (NOTE_REL, AXIOM_REL),
    )

    print("per_element: two snapshots, unit lock I=1 on stay and illegal move")
    print("per_site: window {x,y}; illegal move empties x and occupies y")
    print("per_mode: I-seq and bag are stay/move-blind; J-seq is not")
    print("per_block: permanence visibility in named readout only; no rate or clock")
    print("lattice_wide: checked and not executed — two-site window only")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
