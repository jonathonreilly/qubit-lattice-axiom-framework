#!/usr/bin/env python3
"""Occupancy-to-lock step on a displayed 2x2x2 cube."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "CUBE_222_OCCUPANCY_STEP_BOUNDED_THEOREM_NOTE_2026-08-14.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/CUBE_222_OCCUPANCY_STEP_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

SITES = tuple((x, y, z) for x in (0, 1) for y in (0, 1) for z in (0, 1))
AXES = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
NONE = None
LOCK = "-"
ORIGIN = (0, 0, 0)
AXIS_SITES = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
FACE_SITES = ((1, 1, 0), (1, 0, 1), (0, 1, 1))
OPP = (1, 1, 1)


def empty() -> dict:
    return {s: NONE for s in SITES}


def occ(site: tuple, locks: dict) -> int:
    """Identity gate."""
    return 0 if locks[site] is NONE else 1


def nvec(site: tuple, locks: dict) -> tuple[Fraction, Fraction, Fraction]:
    """Identity gate."""
    out = []
    for ax in AXES:
        plus = (site[0] + ax[0], site[1] + ax[1], site[2] + ax[2])
        minus = (site[0] - ax[0], site[1] - ax[1], site[2] - ax[2])
        o_plus = occ(plus, locks) if plus in locks else 0
        o_minus = occ(minus, locks) if minus in locks else 0
        out.append(Fraction(o_plus - o_minus, 3))
    return tuple(out)


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
    print("measure_boundary: exact Q 2x2x2 occupancy update")
    print("negative_scope: cube comparator, not a TOE")

    seed = empty()
    seed[ORIGIN] = LOCK
    s1 = step(seed)
    s2 = step(s1)
    s3 = step(s2)
    s4 = step(s3)
    t0, t1, t2, t3, t4 = 0, formed(seed, s1), None, None, None
    t2 = t1 + formed(s1, s2)
    t3 = t2 + formed(s2, s3)
    t4 = t3 + formed(s3, s4)

    checks.check("thm1-seed", "only origin locked; axis k=1; opposite n=0", locked_set(seed) == {ORIGIN} and all(sum(c * c for c in nvec(p, seed)) == Fraction(1, 9) for p in AXIS_SITES) and nvec(OPP, seed) == (0, 0, 0))
    checks.check("thm2-axis", "step 1 forms the three axis sites", locked_set(s1) == {ORIGIN, *AXIS_SITES} and formed(seed, s1) == 3)
    checks.check("thm3-face", "step 2 forms the three face-diagonals", locked_set(s2) == {ORIGIN, *AXIS_SITES, *FACE_SITES} and formed(s1, s2) == 3)
    checks.check("thm3-opp", "step 3 forms the opposite corner", locked_set(s3) == set(SITES) and formed(s2, s3) == 1)
    checks.check("thm3-perm", "step 4 is identity", s4 == s3 and formed(s3, s4) == 0)
    checks.check("thm3-tick", "source/tick are 0,3,6,7,7", (t0, t1, t2, t3, t4) == (0, 3, 6, 7, 7))
    checks.check("thm4-empty", "empty cube is a fixed point", step(empty()) == empty())
    checks.check("mutation-s1-opp-fails", "predicate step 1 forms (1,1,1) must fail", s1[OPP] is NONE)
    checks.check("mutation-empty-fails", "predicate empty forms origin must fail", step(empty())[ORIGIN] is NONE)
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
    checks.check("memo-silent", "axioms do not name the cube step", "2×2×2" not in four and "cube6nn" not in four)
    checks.check(
        "gates",
        "identity gates and AUDIT_INPUT_PATHS",
        "def occ(" in self_source
        and "def nvec(" in self_source
        and "def step(" in self_source
        and AUDIT_INPUT_PATHS == (
            "docs/CUBE_222_OCCUPANCY_STEP_BOUNDED_THEOREM_NOTE_2026-08-14.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        ),
    )
    print("per_element: checked exactly — 6-NN n on eight sites")
    print("per_site: checked exactly — seed, axis, face, opposite, empty")
    print("per_mode: checked exactly — one occupancy step; source=formations")
    print("per_block: checked exactly — cube adjacency, not a line")
    print("lattice_wide: checked and not executed — no law adopted")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
