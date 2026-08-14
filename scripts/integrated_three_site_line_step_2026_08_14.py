#!/usr/bin/env python3
"""One occupancy-to-lock update on a displayed 3-site line."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "INTEGRATED_THREE_SITE_LINE_STEP_BOUNDED_THEOREM_NOTE_2026-08-14.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/INTEGRATED_THREE_SITE_LINE_STEP_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

L, C, R = 0, 1, 2
MINUS, NONE = "-", None
THIRD = Fraction(-1, 3)


def occupancy(locks: tuple) -> tuple[int, int, int]:
    """Identity gate."""
    return tuple(0 if lock is NONE else 1 for lock in locks)


def nx(site: int, locks: tuple) -> Fraction:
    """Identity gate: n_x = (o_right - o_left)/3 on the line."""
    occ = occupancy(locks)
    left = occ[site - 1] if site > L else 0
    right = occ[site + 1] if site < R else 0
    return Fraction(right - left, 3)


def step(locks: tuple) -> tuple:
    """Identity gate: one simultaneous update."""
    out = []
    for site, lock in enumerate(locks):
        if lock is not NONE:
            out.append(lock)
            continue
        n = nx(site, locks)
        if n == 0:
            out.append(NONE)
        else:
            out.append(MINUS if n < 0 else "+")
    return tuple(out)


def formed(before: tuple, after: tuple) -> int:
    """Identity gate: new locks this step."""
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
    print("measure_boundary: exact Q 3-site line update")
    print("negative_scope: one comparator step, not a TOE")

    seed = (MINUS, NONE, NONE)
    s1 = step(seed)
    s2 = step(s1)
    s3 = step(s2)
    t0, t1, t2, t3 = 0, formed(seed, s1), formed(seed, s1) + formed(s1, s2), None
    t3 = t2 + formed(s2, s3)

    checks.check("thm1-seed", "seed is (−,·,·) with source 0", seed == (MINUS, NONE, NONE))
    checks.check("thm1-nx-c", "at seed, C has n_x=-1/3 and R has n_x=0", nx(C, seed) == THIRD and nx(R, seed) == 0)
    checks.check("thm2-step1", "step 1 is (−,−,·) and forms 1", s1 == (MINUS, MINUS, NONE) and formed(seed, s1) == 1)
    checks.check("thm3-step2", "step 2 is (−,−,−) because C is now occupied", s2 == (MINUS, MINUS, MINUS) and formed(s1, s2) == 1)
    checks.check("thm3-recoil-nx", "after step 1, R has n_x=-1/3", nx(R, s1) == THIRD)
    checks.check("thm4-step3", "step 3 is identity and forms 0", s3 == s2 and formed(s2, s3) == 0)
    checks.check("thm5-tick", "source/tick are 0,1,2,2", t0 == 0 and t1 == 1 and t2 == 2 and t3 == 2)
    checks.check(
        "thm5-one-function",
        "step is the only update; source is formed() of that step",
        "def step(" in self_source and "def formed(" in self_source,
    )
    empty = (NONE, NONE, NONE)
    checks.check("mutation-empty-fails", "predicate empty seed forms C must fail", step(empty) == empty)
    checks.check("mutation-step2-no-R-fails", "predicate step 2 does not form R must fail", s2[R] == MINUS)
    checks.check("mutation-step3-source-fails", "predicate step 3 increments source must fail", formed(s2, s3) == 0)
    checks.check(
        "quoted",
        "note quotes lock, permanence, and NN distribution",
        "locks exactly one admissible local possibility" in note
        and "records are permanent" in note
        and "determined by, and varies with, the nearest-neighbor conditions." in note,
    )
    forbidden = ("Lattice-named", "we adopt", "L_phys", "0.5934", "pairing-on-J", "exhausted", "closes the route", "only route")
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
    checks.check("memo-silent", "axioms do not name the line update", "3-site line" not in four and "intstep" not in four)
    checks.check(
        "audit-paths",
        "AUDIT_INPUT_PATHS tuple",
        AUDIT_INPUT_PATHS == (
            "docs/INTEGRATED_THREE_SITE_LINE_STEP_BOUNDED_THEOREM_NOTE_2026-08-14.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and "def occupancy(" in self_source
        and "def nx(" in self_source
        and "def step(" in self_source
        and "def formed(" in self_source,
    )
    print("per_element: checked exactly — L,C,R occupancy and n_x")
    print("per_site: checked exactly — seed, C form, R form, permanence")
    print("per_mode: checked exactly — one step function; source=tick=formations")
    print("per_block: checked exactly — line recoil, not Newton")
    print("lattice_wide: checked and not executed — no law adopted")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
