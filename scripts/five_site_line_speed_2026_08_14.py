#!/usr/bin/env python3
"""Five-site occupancy wave with speed 1."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "FIVE_SITE_LINE_SPEED_BOUNDED_THEOREM_NOTE_2026-08-14.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/FIVE_SITE_LINE_SPEED_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

N = 5
NONE = None
LOCK = "-"


def occupancy(locks: tuple) -> tuple:
    return tuple(0 if x is NONE else 1 for x in locks)


def nx(site: int, locks: tuple) -> Fraction:
    """Identity gate."""
    occ = occupancy(locks)
    left = occ[site - 1] if site > 0 else 0
    right = occ[site + 1] if site < N - 1 else 0
    return Fraction(right - left, 3)


def step(locks: tuple) -> tuple:
    """Identity gate."""
    out = []
    for site, lock in enumerate(locks):
        if lock is not NONE:
            out.append(lock)
        else:
            out.append(LOCK if nx(site, locks) != 0 else NONE)
    return tuple(out)


def locked_prefix(locks: tuple) -> int:
    """Identity gate: number of leading locks, or -1 if a hole exists."""
    count = 0
    seen_unread = False
    for lock in locks:
        if lock is not NONE:
            if seen_unread:
                return -1
            count += 1
        else:
            seen_unread = True
    return count


def formed(before: tuple, after: tuple) -> int:
    return sum(1 for b, a in zip(before, after) if b is NONE and a is not NONE)


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

    print("external_scientific_inputs: none")
    print("package_local_integrity_reads: runner, note, axiom memo")
    print("measure_boundary: exact Q 5-site speed-1 wave")
    print("negative_scope: line comparator, not a TOE")

    state = (LOCK,) + (NONE,) * 4
    snapshots = [state]
    source = [0]
    for _ in range(5):
        nxt = step(state)
        source.append(source[-1] + formed(state, nxt))
        state = nxt
        snapshots.append(state)

    cone_ok = all(locked_prefix(snapshots[t]) == t + 1 for t in range(5))
    checks.check("thm1-cone", "after t steps, prefix t+1 is locked", cone_ok)
    checks.check("thm2-site3-t1", "at t=1 site 3 has n_x=0 and is unread", snapshots[1][3] is NONE and nx(3, snapshots[1]) == 0)
    checks.check("thm2-site3-t2", "at t=2 site 3 is unread with n_x≠0", snapshots[2][3] is NONE and nx(3, snapshots[2]) != 0)
    checks.check("thm2-site3-t3", "site 3 forms at step 3", snapshots[3][3] is not NONE)
    checks.check("thm3-step5", "step 5 is identity", snapshots[5] == snapshots[4] and source[5] == 4)
    checks.check("thm3-source", "source/tick are 0,1,2,3,4,4", source == [0, 1, 2, 3, 4, 4])
    empty = (NONE,) * 5
    checks.check("thm3-empty", "empty line is a fixed point", step(empty) == empty)
    checks.check("mutation-early-fails", "predicate site 3 forms at step 2 must fail", snapshots[2][3] is NONE)
    checks.check("mutation-step5-fails", "predicate step 5 increments source must fail", source[5] == source[4])
    checks.check("mutation-empty-fails", "predicate empty forms site 0 must fail", step(empty)[0] is NONE)
    checks.check(
        "quoted",
        "note quotes lock, permanence, and NN distribution",
        "locks exactly one admissible local possibility" in note
        and "records are permanent" in note
        and "determined by, and varies with, the nearest-neighbor conditions." in note,
    )
    forbidden = ("we adopt", "L_phys", "0.5934", "Lattice-named", "exhausted", "closes the route")
    checks.check(
        "boundary",
        "not TOE, no forbidden phrases",
        all(p not in note for p in forbidden)
        and "not a TOE" in note
        and "Qubit remains `M_2(C)`" in note
        and "This note authors no audit verdict" in note
        and "QCD is unused" in note
        and "actual_current_surface_status: bounded-support" in note
        and 'hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"' in note
        and "Honest-auditor / Boundary" in note,
    )
    checks.check("memo-silent", "axioms do not name the 5-site wave", "5-site" not in four and "linespd" not in four)
    checks.check(
        "gates",
        "identity gates and AUDIT_INPUT_PATHS",
        "def nx(" in self_source
        and "def step(" in self_source
        and "def locked_prefix(" in self_source
        and AUDIT_INPUT_PATHS == (
            "docs/FIVE_SITE_LINE_SPEED_BOUNDED_THEOREM_NOTE_2026-08-14.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        ),
    )
    print("per_element: checked exactly — five sites, n_x")
    print("per_site: checked exactly — cone, site 3 delay, empty")
    print("per_mode: checked exactly — speed-1 composition")
    print("per_block: checked exactly — light-cone, not recoil-as-menu")
    print("lattice_wide: checked and not executed — no law adopted")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
