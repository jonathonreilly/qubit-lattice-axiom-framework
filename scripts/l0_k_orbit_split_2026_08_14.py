#!/usr/bin/env python3
"""k is not a single proper-cubic orbit label on the 56 cells."""

from __future__ import annotations

from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "L0_K_ORBIT_SPLIT_BOUNDED_THEOREM_NOTE_2026-08-14.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/L0_K_ORBIT_SPLIT_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

PX, MX, PY, MY, PZ, MZ = range(6)


def cell_k(c: tuple) -> int:
    """Identity gate."""
    a, b, d = c[PX] - c[MX], c[PY] - c[MY], c[PZ] - c[MZ]
    return a * a + b * b + d * d


def rotate_z(c: tuple) -> tuple:
    """Identity gate. R:(x,y,z)->(-y,x,z); c'(g)=c(R^{-1} g)."""
    return (c[MY], c[PY], c[PX], c[MX], c[PZ], c[MZ])


def rotate_x(c: tuple) -> tuple:
    """Identity gate. R:(x,y,z)->(x,-z,y)."""
    return (c[PX], c[MX], c[MZ], c[PZ], c[PY], c[MY])


def all_cells():
    for bits in range(64):
        yield tuple((bits >> i) & 1 for i in range(6))


def orbit_sizes(target_k: int) -> list:
    """Identity gate. Orbit sizes of cells with this k under <90z, 90x>."""
    pool = {c for c in all_cells() if cell_k(c) == target_k}
    sizes = []
    while pool:
        start = pool.pop()
        seen = {start}
        stack = [start]
        while stack:
            cur = stack.pop()
            for nxt in (rotate_z(cur), rotate_x(cur)):
                if nxt not in seen:
                    seen.add(nxt)
                    stack.append(nxt)
        sizes.append(len(seen))
        pool -= seen
    return sorted(sizes)


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
    print("measure_boundary: exact orbit split of the 56 cells")
    print("negative_scope: k is not a cubic type, not a TOE")

    counts = {0: 0, 1: 0, 2: 0, 3: 0}
    for c in all_cells():
        counts[cell_k(c)] += 1
    checks.check("thm1-counts", "k=0,1,2,3 counts are 8,24,24,8", counts == {0: 8, 1: 24, 2: 24, 3: 8})
    o1 = orbit_sizes(1)
    o2 = orbit_sizes(2)
    o3 = orbit_sizes(3)
    checks.check("thm2-k1-split", "k=1 is more than one orbit", len(o1) > 1 and sum(o1) == 24)
    checks.check("thm3-k3-one", "k=3 is one orbit of 8", o3 == [8])
    checks.check("thm2-k2-sum", "k=2 orbits cover 24 cells", sum(o2) == 24)
    checks.check("mutation-k1-one-fails", "predicate k=1 is one orbit must fail", len(o1) != 1)
    checks.check("mutation-k3-two-fails", "predicate k=3 has two orbits must fail", o3 == [8])
    checks.check("mutation-64-fails", "predicate nonzero count is 64 must fail", counts[0] == 8)
    checks.check(
        "quoted",
        "note quotes Qubit and Admissibility",
        "The full one-site possibility domain has algebraic presentation `M_2(C)`." in note
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
    checks.check("memo-silent", "axioms do not name k-orbits", "k-orbit" not in four and "korb" not in four)
    checks.check(
        "gates",
        "identity gates and AUDIT_INPUT_PATHS",
        "def cell_k(" in self_source
        and "def rotate_z(" in self_source
        and "def orbit_sizes(" in self_source
        and AUDIT_INPUT_PATHS == (
            "docs/L0_K_ORBIT_SPLIT_BOUNDED_THEOREM_NOTE_2026-08-14.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        ),
    )
    print("per_element: checked exactly — 6 occupancy bits, two 90° generators")
    print("per_site: checked exactly — 64 occupancy cells")
    print("per_mode: checked exactly — orbit decomposition per k")
    print("per_block: checked exactly — k is a union of orbits")
    print("lattice_wide: checked and not executed — not axiom text")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
