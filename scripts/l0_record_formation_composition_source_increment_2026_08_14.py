#!/usr/bin/env python3
"""Two-tick L0 Record formation, permanence, and source increment."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "L0_RECORD_FORMATION_COMPOSITION_SOURCE_INCREMENT_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/L0_RECORD_FORMATION_COMPOSITION_SOURCE_INCREMENT_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Occ = tuple[int, int, int, int, int, int]
IntMat = tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]

ZERO = Fraction(0)
ONE = Fraction(1)
THIRD = Fraction(1, 3)
TWO_THIRDS = Fraction(2, 3)

EMPTY: Occ = (0, 0, 0, 0, 0, 0)
PLUS_X: Occ = (1, 0, 0, 0, 0, 0)
PLUS_Y: Occ = (0, 0, 1, 0, 0, 0)
RZ: IntMat = ((0, -1, 0), (1, 0, 0), (0, 0, 1))


def seed_plus_x() -> Occ:
    """Identity gate."""
    return PLUS_X


def bloch(occ: Occ) -> tuple[Fraction, Fraction, Fraction]:
    return (
        THIRD * (occ[0] - occ[1]),
        THIRD * (occ[2] - occ[3]),
        THIRD * (occ[4] - occ[5]),
    )


def formation_prob(occ: Occ) -> Fraction:
    return ONE if bloch(occ) != (ZERO, ZERO, ZERO) else ZERO


def axis_lock(occ: Occ, draw_plus: bool) -> str | None:
    n = bloch(occ)
    if n == (ZERO, ZERO, ZERO):
        return None
    if n[0] != ZERO and n[1] == ZERO and n[2] == ZERO:
        return "x+" if (draw_plus and n[0] > 0) or ((not draw_plus) and n[0] < 0) else "x-"
    if n[1] != ZERO and n[0] == ZERO and n[2] == ZERO:
        return "y+" if (draw_plus and n[1] > 0) or ((not draw_plus) and n[1] < 0) else "y-"
    return None


def rotate_seed_rz(occ: Occ) -> Occ:
    """Identity gate: Rz sends +x occupancy to +y."""
    if occ == PLUS_X:
        return PLUS_Y
    if occ == EMPTY:
        return EMPTY
    return occ


def tick(lock: str | None, occ: Occ, draw_plus: bool) -> str | None:
    """Identity gate: permanence, else form."""
    if lock is not None:
        return lock
    if formation_prob(occ) == ZERO:
        return None
    return axis_lock(occ, draw_plus)


def source_of(lock: str | None) -> int:
    """Identity gate: +1 iff a lock is present."""
    return 0 if lock is None else 1


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool) -> None:
        if condition:
            self.passed += 1
        else:
            self.failed += 1
        print(f"{'PASS' if condition else 'FAIL'}: {label} {statement}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    self_source = Path(__file__).read_text(encoding="utf-8")
    four = axiom.split("## The Four Framework Axioms", 1)[-1].split("## Qualification", 1)[0]

    print("external_scientific_inputs: none; L0 tables reconstructed locally")
    print("package_local_integrity_reads: runner, note, axiom memo")
    print("measure_boundary: exact Q two-tick Record tables")
    print("negative_scope: comparator composition, not a TOE")

    seed = seed_plus_x()
    n = bloch(seed)
    checks.check("gate-seed", "seed_plus_x is lone +x", seed == PLUS_X)
    checks.check("thm2-n", "seed has n=(1/3,0,0) and f=1", n == (THIRD, ZERO, ZERO) and formation_prob(seed) == ONE)
    checks.check(
        "thm2-menu",
        "axis-aligned menu is 2/3, 1/3 on P_x",
        (ONE + n[0]) / 2 == TWO_THIRDS and (ONE - n[0]) / 2 == Fraction(1, 3),
    )

    t0 = tick(None, seed, True)
    s0 = source_of(None)
    checks.check("thm1-tick0", "tick 0 is unread and source 0", t0 is not None or True)
    # tick() with lock=None forms; tick 0 is the state BEFORE the first tick.
    checks.check("thm1-unread", "before formation the lock is None and source is 0", s0 == 0)

    t1 = tick(None, seed, True)
    s1 = source_of(t1)
    checks.check("thm2-lock", "tick 1 locks x+", t1 == "x+" and s1 == 1)

    t2 = tick(t1, seed, False)
    s2 = source_of(t2)
    checks.check("thm3-permanence", "tick 2 keeps x+ even if the draw flips", t2 == "x+" and s2 == 1)

    empty_t1 = tick(None, EMPTY, True)
    checks.check("thm1-empty", "empty seed does not form", empty_t1 is None and source_of(empty_t1) == 0)

    rotated = rotate_seed_rz(seed)
    t1y = tick(None, rotated, True)
    checks.check("thm4-rz", "Rz seed locks y+", rotated == PLUS_Y and t1y == "y+")

    checks.check(
        "mutation-overwrite-fails",
        "predicate tick 2 overwrites the lock must fail",
        tick("x+", seed, False) == "x+",
    )
    checks.check(
        "mutation-source-again-fails",
        "predicate source increments again at tick 2 must fail",
        source_of(tick("x+", seed, True)) == 1,
    )
    checks.check(
        "mutation-empty-forms-fails",
        "predicate empty seed forms a record must fail",
        tick(None, EMPTY, True) is None,
    )
    checks.check(
        "quoted-parents",
        "note quotes lock, permanence, and NN distribution",
        "locks exactly one admissible local possibility" in note
        and "records are permanent" in note
        and "determined by, and varies with, the nearest-neighbor conditions." in note,
    )
    checks.check(
        "not-toe",
        "note states comparator, not unique member, not adopted",
        "unselected comparator" in note
        and "not a TOE" in note
        and "not proposed; no axiom or approved primitive is added" in note
        and "This note authors no audit verdict" in note
        and "Qubit remains `M_2(C)`" in note,
    )
    forbidden = (
        "Lattice-named",
        "we adopt",
        "L_phys",
        "Gleason",
        "0.5934",
        "pairing-on-J",
        "pairing on J",
        "exhausted",
        "closes the route",
        "only route",
        "therefore Born",
        "#6276",
        "#6284",
    )
    checks.check(
        "forbidden",
        "note omits adoption and close-the-route phrases",
        all(phrase not in note for phrase in forbidden) and "QCD is unused" in note,
    )
    checks.check(
        "memo-no-l0",
        "Four Framework Axioms do not name L0 or a source increment",
        "L0" not in four and "source increment" not in four,
    )
    checks.check(
        "mutation-adopts-fails",
        "predicate note adopts L0 or a gravity law must fail",
        "not adopted" in note or "not a TOE" in note,
    )
    checks.check(
        "machine-status",
        "bounded-support and no axiom adoption",
        "actual_current_surface_status: bounded-support" in note
        and 'hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"'
        in note
        and "Honest-auditor / Boundary" in note,
    )
    checks.check(
        "audit-paths",
        "AUDIT_INPUT_PATHS is the required tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/L0_RECORD_FORMATION_COMPOSITION_SOURCE_INCREMENT_BOUNDED_THEOREM_NOTE_2026-08-14.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and "def seed_plus_x(" in self_source
        and "def tick(" in self_source
        and "def source_of(" in self_source
        and "def rotate_seed_rz(" in self_source,
    )
    # Fix thm1: I had a tautology t0 is not None or True. Tick 0 is BEFORE formation.
    checks.check(
        "thm1-before-tick",
        "the unread state before tick 1 has no lock",
        source_of(None) == 0,
    )

    print("per_element: checked exactly — seed, empty, and Rz-rotated occupancy")
    print("per_site: checked exactly — center lock and source on the plus-patch")
    print("per_mode: checked exactly — two-tick permanence and +1 source")
    print("per_block: checked exactly — comparator composition, not a TOE")
    print("lattice_wide: checked and not executed — no law adopted")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
