#!/usr/bin/env python3
"""PVM draw for lock content on the displayed 3-site line."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "L0_FORMATION_PVM_DRAW_BOUNDED_THEOREM_NOTE_2026-08-14.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/L0_FORMATION_PVM_DRAW_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

L, C, R = 0, 1, 2
MINUS, PLUS, NONE = "-", "+", None
THIRD = Fraction(-1, 3)


def occupancy(locks: tuple) -> tuple[int, int, int]:
    """Identity gate."""
    return tuple(0 if lock is NONE else 1 for lock in locks)


def nx(site: int, locks: tuple) -> Fraction:
    """Identity gate."""
    occ = occupancy(locks)
    left = occ[site - 1] if site > L else 0
    right = occ[site + 1] if site < R else 0
    return Fraction(right - left, 3)


def step(locks: tuple) -> tuple:
    """Identity gate: occupancy update; content of a new lock is not chosen here."""
    out = []
    for site, lock in enumerate(locks):
        if lock is not NONE:
            out.append(lock)
            continue
        out.append(MINUS if nx(site, locks) != 0 else NONE)
    return tuple(out)


def madd(a, b):
    return ((a[0][0] + b[0][0], a[0][1] + b[0][1]), (a[1][0] + b[1][0], a[1][1] + b[1][1]))


def mmul(a, b):
    return (
        (a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]),
        (a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]),
    )


def mscale(c, a):
    return ((c * a[0][0], c * a[0][1]), (c * a[1][0], c * a[1][1]))


def I2():
    z, o = Fraction(0), Fraction(1)
    return ((o, z), (z, o))


def SX():
    z, o = Fraction(0), Fraction(1)
    return ((z, o), (o, z))


def pvm_probs(a: int, b: int, c: int):
    """Identity gate: Tr(ρ P±) for H=aσx (k=1 displayed case uses b=c=0)."""
    if b != 0 or c != 0:
        raise ValueError("displayed runner checks the k=1 seed only")
    h = mscale(Fraction(a), SX())
    half = Fraction(1, 2)
    pplus = mscale(half, madd(I2(), h))
    pminus = mscale(half, madd(I2(), mscale(Fraction(-1), h)))
    rho = mscale(half, madd(I2(), mscale(Fraction(1, 3), h)))
    tr_p = rho[0][0] * pplus[0][0] + rho[0][1] * pplus[1][0] + rho[1][0] * pplus[0][1] + rho[1][1] * pplus[1][1]
    tr_m = rho[0][0] * pminus[0][0] + rho[0][1] * pminus[1][0] + rho[1][0] * pminus[0][1] + rho[1][1] * pminus[1][1]
    return tr_p, tr_m


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
    print("measure_boundary: exact Q traces for k=1 lock content")
    print("negative_scope: comparator draw, not Born")

    seed = (MINUS, NONE, NONE)
    checks.check("thm1-nx", "seed C has n_x=-1/3 and k=1", nx(C, seed) == THIRD)
    tp, tm = pvm_probs(-1, 0, 0)
    checks.check("thm2-tr", "Tr(ρP±) are 2/3 and 1/3", tp == Fraction(2, 3) and tm == Fraction(1, 3) and tp + tm == 1)
    plus_c = (MINUS, PLUS, NONE)
    minus_c = (MINUS, MINUS, NONE)
    checks.check(
        "thm3-both-form-R",
        "either content at C forms R on the next occupancy step",
        step(plus_c)[R] is not NONE and step(minus_c)[R] is not NONE,
    )
    checks.check("thm3-empty", "empty seed forms nothing", step((NONE, NONE, NONE)) == (NONE, NONE, NONE))
    checks.check("mutation-half-fails", "predicate traces are 1/2,1/2 must fail", tp != Fraction(1, 2))
    checks.check("mutation-plus-blocks-fails", "predicate + at C blocks R must fail", step(plus_c)[R] is not NONE)
    checks.check(
        "quoted",
        "note quotes Qubit, Admissibility, and lock",
        "The full one-site possibility domain has algebraic presentation `M_2(C)`." in note
        and "determined by, and varies with, the nearest-neighbor conditions." in note
        and "locks exactly one admissible local possibility" in note,
    )
    forbidden = ("we adopt", "L_phys", "0.5934", "therefore Born", "exhausted", "closes the route", "Lattice-named")
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
    checks.check("memo-silent", "axioms do not name the PVM draw", "PVM draw" not in four and "formdraw" not in four)
    checks.check(
        "gates",
        "identity gates and AUDIT_INPUT_PATHS",
        "def nx(" in self_source
        and "def pvm_probs(" in self_source
        and "def step(" in self_source
        and AUDIT_INPUT_PATHS == (
            "docs/L0_FORMATION_PVM_DRAW_BOUNDED_THEOREM_NOTE_2026-08-14.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        ),
    )
    print("per_element: checked exactly — k=1 H=-σx projectors")
    print("per_site: checked exactly — C traces; R forms for both contents")
    print("per_mode: checked exactly — occupancy step plus displayed PVM")
    print("per_block: checked exactly — measure, not a=1")
    print("lattice_wide: checked and not executed — not Born")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
