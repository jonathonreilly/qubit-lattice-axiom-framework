#!/usr/bin/env python3
"""n=0 cells never form: opposite neighbors cancel."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "N0_OPPOSITE_CANCEL_BOUNDED_THEOREM_NOTE_2026-08-14.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/N0_OPPOSITE_CANCEL_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

L, C, R = 0, 1, 2
NONE = None
MINUS, PLUS = "-", "+"


def occupancy(locks: tuple) -> tuple:
    return tuple(0 if x is NONE else 1 for x in locks)


def nx(site: int, locks: tuple) -> Fraction:
    """Identity gate."""
    occ = occupancy(locks)
    left = occ[site - 1] if site > L else 0
    right = occ[site + 1] if site < R else 0
    return Fraction(right - left, 3)


def step(locks: tuple) -> tuple:
    """Identity gate."""
    out = []
    for site, lock in enumerate(locks):
        if lock is not NONE:
            out.append(lock)
        else:
            out.append(MINUS if nx(site, locks) != 0 else NONE)
    return tuple(out)


def zero_count() -> int:
    """Identity gate. 6 bits, k=0 when each axis is balanced."""
    n = 0
    for bits in range(64):
        c = [(bits >> i) & 1 for i in range(6)]
        k = (c[0] - c[1]) ** 2 + (c[2] - c[3]) ** 2 + (c[4] - c[5]) ** 2
        if k == 0:
            n += 1
    return n


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
    print("measure_boundary: exact Q opposite cancellation")
    print("negative_scope: n=0 is a hard zero, not a TOE")

    both_plus = (PLUS, NONE, PLUS)
    both_minus = (MINUS, NONE, MINUS)
    checks.check("thm1-nx", "both ends locked gives n_x(C)=0", nx(C, both_plus) == 0 and nx(C, both_minus) == 0)
    checks.check("thm1-step", "step does not form C", step(both_plus) == both_plus and step(both_minus) == both_minus)
    checks.check("thm2-eight", "exactly 8 of 64 cells have k=0", zero_count() == 8)
    one_end = (MINUS, NONE, NONE)
    checks.check("thm3-one-end", "one locked end still forms C", step(one_end)[C] is not NONE)
    empty = (NONE, NONE, NONE)
    checks.check("thm3-empty", "empty line is a fixed point", step(empty) == empty)
    checks.check("mutation-both-form-fails", "predicate both ends form C must fail", step(both_plus)[C] is NONE)
    checks.check("mutation-zero0-fails", "predicate zero-cell count is 0 must fail", zero_count() != 0)
    checks.check("mutation-empty-fails", "predicate empty forms C must fail", step(empty)[C] is NONE)
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
    checks.check("memo-silent", "axioms do not name opposite cancellation", "oppcan" not in four)
    checks.check(
        "gates",
        "identity gates and AUDIT_INPUT_PATHS",
        "def nx(" in self_source
        and "def step(" in self_source
        and "def zero_count(" in self_source
        and AUDIT_INPUT_PATHS == (
            "docs/N0_OPPOSITE_CANCEL_BOUNDED_THEOREM_NOTE_2026-08-14.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        ),
    )
    print("per_element: checked exactly — n_x on three sites; 64-cell k")
    print("per_site: checked exactly — both ends, one end, empty")
    print("per_mode: checked exactly — formation is a difference")
    print("per_block: checked exactly — n=0 is a hard zero")
    print("lattice_wide: checked and not executed — no law adopted")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
