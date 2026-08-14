#!/usr/bin/env python3
"""Occupancy-to-lock step on a displayed 3x3x3 cube with interior seed."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "CUBE_333_INTERIOR_STEP_BOUNDED_THEOREM_NOTE_2026-08-14.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/CUBE_333_INTERIOR_STEP_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

SITES = tuple((x, y, z) for x in (0, 1, 2) for y in (0, 1, 2) for z in (0, 1, 2))
AXES = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
NONE = None
LOCK = "-"
CENTER = (1, 1, 1)


def is_face(p: tuple) -> bool:
    return sum(c in (0, 2) for c in p) == 1 and sum(c == 1 for c in p) == 2


def is_edge(p: tuple) -> bool:
    return sum(c in (0, 2) for c in p) == 2 and sum(c == 1 for c in p) == 1


def is_corner(p: tuple) -> bool:
    return all(c in (0, 2) for c in p)


FACE = tuple(p for p in SITES if is_face(p))
EDGE = tuple(p for p in SITES if is_edge(p))
CORN = tuple(p for p in SITES if is_corner(p))


def empty() -> dict:
    return {s: NONE for s in SITES}


def occ(site: tuple, locks: dict) -> int:
    """Identity gate."""
    return 0 if locks[site] is NONE else 1


def nvec(site: tuple, locks: dict) -> tuple:
    """Identity gate."""
    out = []
    for ax in AXES:
        plus = (site[0] + ax[0], site[1] + ax[1], site[2] + ax[2])
        minus = (site[0] - ax[0], site[1] - ax[1], site[2] - ax[2])
        o_plus = occ(plus, locks) if plus in locks else 0
        o_minus = occ(minus, locks) if minus in locks else 0
        out.append(Fraction(o_plus - o_minus, 3))
    return tuple(out)


def k_of(n: tuple) -> int:
    return int(sum((3 * c) * (3 * c) for c in n))


def step(locks: dict) -> dict:
    """Identity gate."""
    out = {}
    for site, lock in locks.items():
        if lock is not NONE:
            out[site] = lock
            continue
        n = nvec(site, locks)
        out[site] = LOCK if any(c != 0 for c in n) else NONE
    return out


def formed(before: dict, after: dict) -> int:
    return sum(1 for s in SITES if before[s] is NONE and after[s] is not NONE)


def locked_set(locks: dict) -> set:
    return {s for s, v in locks.items() if v is not NONE}


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
    print("measure_boundary: exact Q 3x3x3 interior occupancy update")
    print("negative_scope: cube comparator, not a TOE")

    checks.check("shell-counts", "6 faces, 12 edges, 8 corners, 27 sites", len(FACE) == 6 and len(EDGE) == 12 and len(CORN) == 8 and len(SITES) == 27)
    seed = empty()
    seed[CENTER] = LOCK
    s1 = step(seed)
    s2 = step(s1)
    s3 = step(s2)
    s4 = step(s3)
    t = [0]
    t.append(t[-1] + formed(seed, s1))
    t.append(t[-1] + formed(s1, s2))
    t.append(t[-1] + formed(s2, s3))
    t.append(t[-1] + formed(s3, s4))

    checks.check("thm1-seed", "only center locked; faces k=1; corners n=0", locked_set(seed) == {CENTER} and all(k_of(nvec(p, seed)) == 1 for p in FACE) and all(nvec(p, seed) == (0, 0, 0) for p in CORN))
    checks.check("thm2-face", "step 1 forms the six face-centers", locked_set(s1) == {CENTER, *FACE} and formed(seed, s1) == 6)
    checks.check("thm2-edge", "step 2 forms the twelve edge-centers", locked_set(s2) == {CENTER, *FACE, *EDGE} and formed(s1, s2) == 12)
    checks.check("thm2-corn", "step 3 forms the eight corners", locked_set(s3) == set(SITES) and formed(s2, s3) == 8)
    checks.check("thm2-perm", "step 4 is identity", s4 == s3 and formed(s3, s4) == 0)
    checks.check("thm2-tick", "source/tick are 0,6,18,26,26", t == [0, 6, 18, 26, 26])
    checks.check("thm3-empty", "empty cube is a fixed point", step(empty()) == empty())
    checks.check("mutation-s1-corn-fails", "predicate step 1 forms a corner must fail", all(s1[p] is NONE for p in CORN))
    checks.check("mutation-empty-fails", "predicate empty forms center must fail", step(empty())[CENTER] is NONE)
    checks.check("mutation-s4-source-fails", "predicate step 4 increments source must fail", formed(s3, s4) == 0)
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
        "comparator not TOE, no forbidden phrases",
        all(p not in note for p in forbidden)
        and "not a TOE" in note
        and "Qubit remains `M_2(C)`" in note
        and "This note authors no audit verdict" in note
        and "QCD is unused" in note
        and "actual_current_surface_status: bounded-support" in note
        and 'hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"' in note
        and "Honest-auditor / Boundary" in note,
    )
    checks.check("memo-silent", "axioms do not name the 3x3x3 step", "3×3×3" not in four and "cube333" not in four)
    checks.check(
        "gates",
        "identity gates and AUDIT_INPUT_PATHS",
        "def occ(" in self_source
        and "def nvec(" in self_source
        and "def step(" in self_source
        and AUDIT_INPUT_PATHS == (
            "docs/CUBE_333_INTERIOR_STEP_BOUNDED_THEOREM_NOTE_2026-08-14.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        ),
    )
    print("per_element: checked exactly — 6-NN n on 27 sites")
    print("per_site: checked exactly — center, faces, edges, corners, empty")
    print("per_mode: checked exactly — one occupancy step; source=formations")
    print("per_block: checked exactly — interior 6-NN, not a 2x2x2 corner cube")
    print("lattice_wide: checked and not executed — no law adopted")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
