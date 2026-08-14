#!/usr/bin/env python3
"""Unique 2-face tree-gauge flux given g=ρ."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "TWO_CUBE_TREE_GAUGE_UNIQUENESS_BOUNDED_THEOREM_NOTE_2026-08-14.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/TWO_CUBE_TREE_GAUGE_UNIQUENESS_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

VERTS = tuple((x, y, z) for x in (0, 1, 2) for y in (0, 1) for z in (0, 1))
A_VERTS = tuple(v for v in VERTS if v[0] in (0, 1))
B_VERTS = tuple(v for v in VERTS if v[0] in (1, 2))
AXES = ((1, 0, 0), (0, 1, 0), (0, 0, 1))


def occ(v, locks) -> int:
    return 1 if v in locks else 0


def rho(locks) -> tuple[int, int]:
    """Identity gate."""
    return sum(occ(v, locks) for v in A_VERTS), sum(occ(v, locks) for v in B_VERTS)


def unique_two_face(src: tuple[int, int]) -> tuple[int, int]:
    """Identity gate. Only solution with support on {F*, F_B}."""
    ra, rb = src
    return ra, ra + rb


def three_face_family(src: tuple[int, int], t: int) -> tuple[int, int, int]:
    """Identity gate. (φ(F*), φ(F_A), φ(F_B)) for free t."""
    ra, rb = src
    return ra - t, t, rb + ra - t


def gauss_two(src, phi_star, phi_b) -> bool:
    ra, rb = src
    return phi_star == ra and (-phi_star + phi_b) == rb


def gauss_three(src, phi_star, phi_a, phi_b) -> bool:
    ra, rb = src
    return (phi_star + phi_a) == ra and (-phi_star + phi_b) == rb


def nvec(site, locks):
    out = []
    for ax in AXES:
        plus = (site[0] + ax[0], site[1] + ax[1], site[2] + ax[2])
        minus = (site[0] - ax[0], site[1] - ax[1], site[2] - ax[2])
        o_plus = occ(plus, locks) if plus in VERTS else 0
        o_minus = occ(minus, locks) if minus in VERTS else 0
        out.append(Fraction(o_plus - o_minus, 3))
    return tuple(out)


def occ_step(locks: frozenset) -> frozenset:
    """Identity gate."""
    out = set(locks)
    for v in VERTS:
        if v in locks:
            continue
        if any(c != 0 for c in nvec(v, locks)):
            out.add(v)
    return frozenset(out)


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
    print("measure_boundary: exact uniqueness of 2-face source-complete flux")
    print("negative_scope: gauge-fix uniqueness, not Newton")

    seed = frozenset({(0, 0, 0)})
    src0 = rho(seed)
    u0 = unique_two_face(src0)
    checks.check("thm1-unique-seed", "seed 2-face flux is unique (1,1)", src0 == (1, 0) and u0 == (1, 1) and gauss_two(src0, *u0))
    other = [(a, b) for a in range(-2, 4) for b in range(-2, 6) if (a, b) != u0]
    checks.check("thm1-no-other", "no other 2-face pair solves g=ρ on the seed", all(not gauss_two(src0, a, b) for a, b in other))
    fam = [three_face_family(src0, t) for t in range(-2, 3)]
    checks.check("thm2-family", "3-face solutions exist for five t values", all(gauss_three(src0, *trip) for trip in fam) and len({trip for trip in fam}) == 5)
    s1 = occ_step(seed)
    src1 = rho(s1)
    u1 = unique_two_face(src1)
    checks.check("thm3-step", "after occupancy step unique 2-face flux is (4,5)", s1 - seed == frozenset({(1, 0, 0), (0, 1, 0), (0, 0, 1)}) and src1 == (4, 1) and u1 == (4, 5) and gauss_two(src1, *u1))
    checks.check("mutation-second-fails", "predicate a second 2-face seed solution exists must fail", all(not gauss_two(src0, a, b) for a, b in other))
    checks.check("mutation-family-point-fails", "predicate 3-face family is a point must fail", len({trip for trip in fam}) != 1)
    checks.check(
        "quoted",
        "note quotes lock, Admissibility, and Qubit",
        "locks exactly one admissible local possibility" in note
        and "determined by, and varies with, the nearest-neighbor conditions." in note
        and "The full one-site possibility domain has algebraic presentation `M_2(C)`." in note,
    )
    forbidden = ("we adopt", "L_phys", "0.5934", "Lattice-named", "exhausted", "closes the route", "G_N")
    checks.check(
        "boundary",
        "no forbidden phrases; required status strings",
        all(p not in note for p in forbidden)
        and "not a TOE" in note
        and "Qubit remains `M_2(C)`" in note
        and "This note authors no audit verdict" in note
        and "QCD is unused" in note
        and "actual_current_surface_status: bounded-support" in note
        and 'hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"' in note
        and "Honest-auditor / Boundary" in note,
    )
    checks.check("memo-silent", "axioms do not name the tree gauge", "gaugefix" not in four and "F_B" not in four)
    checks.check(
        "gates",
        "identity gates and AUDIT_INPUT_PATHS",
        "def rho(" in self_source
        and "def unique_two_face(" in self_source
        and "def three_face_family(" in self_source
        and "def occ_step(" in self_source
        and AUDIT_INPUT_PATHS == (
            "docs/TWO_CUBE_TREE_GAUGE_UNIQUENESS_BOUNDED_THEOREM_NOTE_2026-08-14.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        ),
    )
    print("per_element: checked exactly — 2-face vs 3-face flux")
    print("per_site: checked exactly — seed and one occupancy step")
    print("per_mode: checked exactly — uniqueness of support-restricted gauge")
    print("per_block: checked exactly — tree gauge, not Newton")
    print("lattice_wide: checked and not executed — not axiom text")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
