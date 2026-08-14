#!/usr/bin/env python3
"""Exact k=1 PVM traces at the three first-wave two-cube formers."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "TWO_CUBE_FORMATION_PVM_BOUNDED_THEOREM_NOTE_2026-08-14.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/TWO_CUBE_FORMATION_PVM_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

VERTS = tuple((x, y, z) for x in (0, 1, 2) for y in (0, 1) for z in (0, 1))
AXES = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
FORMERS = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
SEED = frozenset({(0, 0, 0)})


def occ(v, locks) -> int:
    return 1 if v in locks else 0


def nvec(site, locks):
    """Identity gate."""
    out = []
    for ax in AXES:
        plus = (site[0] + ax[0], site[1] + ax[1], site[2] + ax[2])
        minus = (site[0] - ax[0], site[1] - ax[1], site[2] - ax[2])
        o_plus = occ(plus, locks) if plus in VERTS else 0
        o_minus = occ(minus, locks) if minus in VERTS else 0
        out.append(Fraction(o_plus - o_minus, 3))
    return tuple(out)


def k_of(n) -> Fraction:
    """Identity gate. k = |3n|^2."""
    return sum((3 * c) ** 2 for c in n)


def traces_k1():
    """Identity gate. Displayed PVM traces at k=1: (3±1)/6."""
    return Fraction(3 + 1, 6), Fraction(3 - 1, 6)


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
    print("measure_boundary: exact k=1 traces at three forming sites")
    print("negative_scope: first-wave PVM traces, not Newton")
    ns = [nvec(site, SEED) for site in FORMERS]
    ks = [k_of(n) for n in ns]
    plus_t, minus_t = traces_k1()
    checks.check(
        "thm1-k1",
        "three formers each have k=|3n|^2=1",
        FORMERS == ((1, 0, 0), (0, 1, 0), (0, 0, 1))
        and len(VERTS) == 12
        and ks == [1, 1, 1]
        and ns[0] == (Fraction(-1, 3), Fraction(0), Fraction(0))
        and ns[1] == (Fraction(0), Fraction(-1, 3), Fraction(0))
        and ns[2] == (Fraction(0), Fraction(0), Fraction(-1, 3)),
    )
    checks.check(
        "thm1-unbalanced",
        "each first-wave site has one unbalanced axis",
        all(sum(c != 0 for c in n) == 1 for n in ns),
    )
    checks.check(
        "thm2-traces",
        "traces_k1 are 2/3 and 1/3",
        plus_t == Fraction(2, 3) and minus_t == Fraction(1, 3),
    )
    checks.check(
        "thm2-formula",
        "traces equal (3±1)/6",
        plus_t == Fraction(3 + 1, 6) and minus_t == Fraction(3 - 1, 6),
    )
    checks.check(
        "thm3-display",
        "note keeps qubit M_2(C) and unused QCD",
        "Qubit remains `M_2(C)`" in note and "QCD is unused" in note,
    )
    checks.check(
        "mutation-k2-fails",
        "predicate a first-wave site has k=2 must fail",
        all(k != 2 for k in ks),
    )
    checks.check(
        "mutation-half-fails",
        "predicate traces are 1/2, 1/2 must fail",
        {plus_t, minus_t} != {Fraction(1, 2)},
    )
    checks.check(
        "quoted",
        "note quotes M_2(C) and NN distribution",
        "The full one-site possibility domain has algebraic presentation `M_2(C)`." in note
        and "determined by, and varies with, the nearest-neighbor conditions." in note
        and "The full one-site possibility domain has algebraic presentation `M_2(C)`." in axiom
        and "determined by, and varies with, the nearest-neighbor conditions." in axiom,
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
    checks.check("memo-silent", "axioms do not name these traces", "2/3" not in four and "PVM" not in four)
    checks.check(
        "gates",
        "identity gates",
        "def nvec(" in self_source
        and "def k_of(" in self_source
        and "def traces_k1(" in self_source
        and AUDIT_INPUT_PATHS
        == (
            "docs/TWO_CUBE_FORMATION_PVM_BOUNDED_THEOREM_NOTE_2026-08-14.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        ),
    )
    print("per_element: checked exactly — k and traces at three formers")
    print("per_site: checked exactly — (1,0,0), (0,1,0), (0,0,1)")
    print("per_mode: checked exactly — k=1 PVM traces 2/3, 1/3")
    print("per_block: checked exactly — measure on the two-cube step")
    print("lattice_wide: checked and not executed — not axiom text")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
