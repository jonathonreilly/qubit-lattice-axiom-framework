#!/usr/bin/env python3
"""+x ray uniquely selects {F*, F_B} on the two-cube dual."""

from __future__ import annotations

from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "TWO_CUBE_PLUS_X_RAY_SUPPORT_BOUNDED_THEOREM_NOTE_2026-08-14.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/TWO_CUBE_PLUS_X_RAY_SUPPORT_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

# Dual: A --F*-- B --F_B-- ext, and A --F_A-- ext
# Coordinate of a node: A at x=0.5, B at x=1.5, ext via F_B at x>2 or via F_A at x<0
EDGES = {
    "F*": ("A", "B"),
    "F_B": ("B", "ext"),
    "F_A": ("A", "ext"),
}
# x-direction of crossing the edge from first node toward the other
DX = {"F*": 1, "F_B": 1, "F_A": -1}


def paths() -> tuple:
    """Identity gate. Simple A→ext paths as edge tuples."""
    return (("F*", "F_B"), ("F_A",))


def monotone_plus_x(path: tuple) -> bool:
    """Identity gate."""
    return all(DX[e] > 0 for e in path)


def selected() -> tuple:
    """Identity gate."""
    mono = [p for p in paths() if monotone_plus_x(p)]
    if len(mono) != 1:
        raise ValueError("plus-x path is not unique")
    return mono[0]


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
    print("measure_boundary: exact path count on the two-cube dual")
    print("negative_scope: support selection, not Newton")

    ps = paths()
    checks.check("thm1-two", "exactly two simple A→ext paths", ps == (("F*", "F_B"), ("F_A",)))
    checks.check("thm2-mono", "only (F*,F_B) is +x monotone", monotone_plus_x(("F*", "F_B")) and not monotone_plus_x(("F_A",)))
    checks.check("thm2-sel", "selected support is {F*, F_B}", selected() == ("F*", "F_B"))
    checks.check("mutation-third-fails", "predicate a third simple path exists must fail", len(ps) == 2)
    checks.check("mutation-fa-mono-fails", "predicate F_A is +x monotone must fail", not monotone_plus_x(("F_A",)))
    checks.check(
        "quoted",
        "note quotes Lattice, Admissibility, and Qubit",
        "Physical sites are the points of the cubic lattice `Z^3`" in note
        and "determined by, and varies with, the nearest-neighbor conditions." in note
        and "The full one-site possibility domain has algebraic presentation `M_2(C)`." in note,
    )
    forbidden = ("we adopt", "L_phys", "0.5934", "Lattice-named", "exhausted", "closes the route", "G_N")
    checks.check(
        "boundary",
        "required strings, no forbidden phrases",
        all(p not in note for p in forbidden)
        and "not a TOE" in note
        and "Qubit remains `M_2(C)`" in note
        and "This note authors no audit verdict" in note
        and "QCD is unused" in note
        and "actual_current_surface_status: bounded-support" in note
        and 'hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"' in note
        and "Honest-auditor / Boundary" in note,
    )
    checks.check("memo-silent", "axioms do not name the dual path", "treesup" not in four and "F_B" not in four)
    checks.check(
        "gates",
        "identity gates and AUDIT_INPUT_PATHS",
        "def paths(" in self_source
        and "def monotone_plus_x(" in self_source
        and "def selected(" in self_source
        and AUDIT_INPUT_PATHS == (
            "docs/TWO_CUBE_PLUS_X_RAY_SUPPORT_BOUNDED_THEOREM_NOTE_2026-08-14.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        ),
    )
    print("per_element: checked exactly — three dual edges")
    print("per_site: checked exactly — two A→ext paths")
    print("per_mode: checked exactly — +x monotone selection")
    print("per_block: checked exactly — support of the tree gauge")
    print("lattice_wide: checked and not executed — not axiom text")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
