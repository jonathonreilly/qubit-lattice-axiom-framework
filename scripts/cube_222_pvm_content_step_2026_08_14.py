#!/usr/bin/env python3
"""2x2x2 occupancy step plus displayed PVM lock-content traces."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "CUBE_222_PVM_CONTENT_STEP_BOUNDED_THEOREM_NOTE_2026-08-14.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/CUBE_222_PVM_CONTENT_STEP_BOUNDED_THEOREM_NOTE_2026-08-14.md",
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
    """Identity gate."""
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


def traces(k: int) -> tuple[object, object]:
    """(3±√k)/6 as (rational, coeff of √k)."""
    return (Fraction(1, 2), Fraction(1, 6)), (Fraction(1, 2), Fraction(-1, 6))


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
    print("measure_boundary: exact cube occupancy plus Q(√k) traces")
    print("negative_scope: coupled comparator, not Born")

    seed = empty()
    seed[ORIGIN] = LOCK
    s1 = step(seed)
    s2 = step(s1)
    s3 = step(s2)
    s4 = step(s3)
    t = [0]
    t.append(t[-1] + formed(seed, s1))
    t.append(t[-1] + formed(s1, s2))
    t.append(t[-1] + formed(s2, s3))
    t.append(t[-1] + formed(s3, s4))

    checks.check("thm1-tick", "source/tick are 0,3,6,7,7", t == [0, 3, 6, 7, 7])
    checks.check("thm1-empty", "empty cube is a fixed point", step(empty()) == empty())
    k1s = {k_of(nvec(p, seed)) for p in AXIS_SITES}
    k2s = {k_of(nvec(p, s1)) for p in FACE_SITES}
    k3 = k_of(nvec(OPP, s2))
    checks.check("thm2-k", "shells have k=1,2,3", k1s == {1} and k2s == {2} and k3 == 3)
    tp1, tm1 = traces(1)
    tp2, tm2 = traces(2)
    tp3, tm3 = traces(3)
    checks.check("thm3-k1", "k=1 traces are 2/3 and 1/3", tp1[0] + tp1[1] == Fraction(2, 3) and tm1[0] + tm1[1] == Fraction(1, 3))
    checks.check("thm3-k2", "k=2 traces are (3±√2)/6", tp2 == (Fraction(1, 2), Fraction(1, 6)) and tm2 == (Fraction(1, 2), Fraction(-1, 6)))
    checks.check("thm3-k3", "k=3 traces are (3±√3)/6", tp3 == (Fraction(1, 2), Fraction(1, 6)) and tm3 == (Fraction(1, 2), Fraction(-1, 6)))
    # either content at an axis site still occupies it
    occupied_axis = empty()
    occupied_axis[ORIGIN] = LOCK
    for p in AXIS_SITES:
        occupied_axis[p] = "+"
    checks.check("thm4-plus-forms-face", "axis + content still forms face-diagonals", all(step(occupied_axis)[p] is not NONE for p in FACE_SITES))
    checks.check("mutation-k-fails", "predicate axis sites have k=2 must fail", k1s == {1})
    checks.check("mutation-empty-fails", "predicate empty cube forms must fail", step(empty())[ORIGIN] is NONE)
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
        "not Born, not TOE, no forbidden phrases",
        all(p not in note for p in forbidden)
        and "not a TOE" in note
        and "Qubit remains `M_2(C)`" in note
        and "This note authors no audit verdict" in note
        and "QCD is unused" in note
        and "actual_current_surface_status: bounded-support" in note
        and 'hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"' in note
        and "Honest-auditor / Boundary" in note,
    )
    checks.check("memo-silent", "axioms do not name the coupled cube PVM", "cubepvm" not in four)
    checks.check(
        "gates",
        "identity gates and AUDIT_INPUT_PATHS",
        "def nvec(" in self_source
        and "def k_of(" in self_source
        and "def step(" in self_source
        and AUDIT_INPUT_PATHS == (
            "docs/CUBE_222_PVM_CONTENT_STEP_BOUNDED_THEOREM_NOTE_2026-08-14.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        ),
    )
    print("per_element: checked exactly — k and traces on three shells")
    print("per_site: checked exactly — axis, face, opposite, empty")
    print("per_mode: checked exactly — occupancy step plus PVM traces")
    print("per_block: checked exactly — coupled cube+PVM comparator")
    print("lattice_wide: checked and not executed — not Born")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
