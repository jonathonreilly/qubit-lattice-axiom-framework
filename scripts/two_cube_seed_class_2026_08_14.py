#!/usr/bin/env python3
"""Classify one-site seeds on the two-cube occupancy step."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "TWO_CUBE_SEED_CLASS_BOUNDED_THEOREM_NOTE_2026-08-14.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/TWO_CUBE_SEED_CLASS_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

VERTS = tuple((x, y, z) for x in (0, 1, 2) for y in (0, 1) for z in (0, 1))
A_ONLY = tuple(v for v in VERTS if v[0] == 0)
SHARED = tuple(v for v in VERTS if v[0] == 1)
B_ONLY = tuple(v for v in VERTS if v[0] == 2)
AXES = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
EXPECTED_CLASS_COUNTS = {
    "A-only": (4, 3),
    "shared": (4, 4),
    "B-only": (4, 3),
}


def occ(v, locks) -> int:
    return 1 if v in locks else 0


def nvec(site, locks):
    out = []
    for ax in AXES:
        plus = (site[0] + ax[0], site[1] + ax[1], site[2] + ax[2])
        minus = (site[0] - ax[0], site[1] - ax[1], site[2] - ax[2])
        o_plus = occ(plus, locks) if plus in VERTS else 0
        o_minus = occ(minus, locks) if minus in VERTS else 0
        out.append(Fraction(o_plus - o_minus, 3))
    return tuple(out)


def occ_step(locks):
    out = set(locks)
    for v in VERTS:
        if v not in locks and any(c != 0 for c in nvec(v, locks)):
            out.add(v)
    return frozenset(out)


def formed_from(seed) -> frozenset:
    """Identity gate."""
    before = frozenset({seed})
    return occ_step(before) - before


def seed_class(seed) -> str:
    if seed[0] == 0:
        return "A-only"
    if seed[0] == 1:
        return "shared"
    return "B-only"


def class_counts() -> dict[str, tuple[int, int]]:
    """Identity gate."""
    sizes: dict[str, list[int]] = {"A-only": [], "shared": [], "B-only": []}
    for seed in VERTS:
        sizes[seed_class(seed)].append(len(formed_from(seed)))
    out: dict[str, tuple[int, int]] = {}
    for name, values in sizes.items():
        common = values[0] if values and all(v == values[0] for v in values) else -1
        out[name] = (len(values), common)
    return out


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label, statement, condition) -> None:
        self.passed += int(bool(condition))
        self.failed += int(not condition)
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
    print("measure_boundary: exact integers on twelve single-site seeds")
    print("negative_scope: seed-class census, not Newton")
    counts = class_counts()
    a_forms = {len(formed_from(seed)) for seed in A_ONLY}
    s_forms = {len(formed_from(seed)) for seed in SHARED}
    b_forms = {len(formed_from(seed)) for seed in B_ONLY}
    seed000 = formed_from((0, 0, 0))
    seed100 = formed_from((1, 0, 0))
    seed200 = formed_from((2, 0, 0))
    checks.check(
        "thm1-twelve",
        "twelve single-site seeds partition as 4+4+4",
        len(VERTS) == 12 and len(A_ONLY) == 4 and len(SHARED) == 4 and len(B_ONLY) == 4,
    )
    checks.check(
        "thm2-a-only",
        "A-only x=0: 4 sites, each forms 3",
        a_forms == {3} and counts["A-only"] == (4, 3) and seed000 == frozenset({(1, 0, 0), (0, 1, 0), (0, 0, 1)}),
    )
    checks.check(
        "thm3-shared",
        "shared x=1: 4 sites, each forms 4",
        s_forms == {4} and counts["shared"] == (4, 4) and seed100 == frozenset({(0, 0, 0), (2, 0, 0), (1, 1, 0), (1, 0, 1)}),
    )
    checks.check(
        "thm4-b-only",
        "B-only x=2: 4 sites, each forms 3",
        b_forms == {3} and counts["B-only"] == (4, 3) and seed200 == frozenset({(1, 0, 0), (2, 1, 0), (2, 0, 1)}),
    )
    checks.check(
        "thm-class-counts",
        "class_counts is the 4/3, 4/4, 4/3 census",
        counts == EXPECTED_CLASS_COUNTS,
    )
    checks.check("mutation-a-only-forms-4-fails", "predicate A-only seed forms 4 must fail", a_forms != {4})
    checks.check("mutation-shared-forms-3-fails", "predicate shared seed forms 3 must fail", s_forms != {3})
    checks.check(
        "mutation-uniform-fails",
        "predicate all twelve seeds form the same number must fail",
        not (a_forms == s_forms == b_forms),
    )
    checks.check(
        "quoted",
        "note quotes lock, permanence, NN",
        "locks exactly one admissible local possibility" in note
        and "records are permanent" in note
        and "determined by, and varies with, the nearest-neighbor conditions." in note,
    )
    forbidden = ("we adopt", "L_phys", "0.5934", "Lattice-named", "exhausted", "closes the route", "G_N")
    checks.check(
        "boundary",
        "required strings",
        all(p not in note for p in forbidden)
        and "not a TOE" in note
        and "Qubit remains `M_2(C)`" in note
        and "This note authors no audit verdict" in note
        and "QCD is unused" in note
        and "actual_current_surface_status: bounded-support" in note
        and 'hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"' in note
        and "Honest-auditor / Boundary" in note,
    )
    checks.check("memo-silent", "axioms do not name the seed class", "seed class" not in four and "seedclass" not in four)
    checks.check(
        "gates",
        "identity gates",
        "def formed_from(" in self_source
        and "def class_counts(" in self_source
        and AUDIT_INPUT_PATHS
        == (
            "docs/TWO_CUBE_SEED_CLASS_BOUNDED_THEOREM_NOTE_2026-08-14.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        ),
    )
    print("per_element: checked exactly — formed-site set of each single-site seed")
    print("per_site: checked exactly — all twelve vertices as seeds")
    print("per_mode: checked exactly — A-only / shared / B-only classes")
    print("per_block: checked exactly — formation count vs seed x-class")
    print("lattice_wide: checked and not executed — not axiom text")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
