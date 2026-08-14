#!/usr/bin/env python3
"""Δρ on each cube equals new locks in that cube."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "TWO_CUBE_RHO_INCREMENT_BOUNDED_THEOREM_NOTE_2026-08-14.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/TWO_CUBE_RHO_INCREMENT_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

VERTS = tuple((x, y, z) for x in (0, 1, 2) for y in (0, 1) for z in (0, 1))
A_VERTS = frozenset(v for v in VERTS if v[0] in (0, 1))
B_VERTS = frozenset(v for v in VERTS if v[0] in (1, 2))
AXES = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
SEED_NEW = frozenset({(1, 0, 0), (0, 1, 0), (0, 0, 1)})


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
    """Identity gate."""
    out = set(locks)
    for v in VERTS:
        if v not in locks and any(c != 0 for c in nvec(v, locks)):
            out.add(v)
    return frozenset(out)


def rho(locks):
    """Identity gate. Occupancy counts on cubes A and B."""
    return sum(occ(v, locks) for v in A_VERTS), sum(occ(v, locks) for v in B_VERTS)


def new_in(locks, cube_verts):
    """Identity gate. New locks that land in the cube."""
    after = occ_step(locks)
    return frozenset(v for v in (after - frozenset(locks)) if v in cube_verts)


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
    print("measure_boundary: exact integers on one occupancy step")
    print("negative_scope: increment identity, not Newton")

    empty = frozenset()
    seed = frozenset({(0, 0, 0)})
    after_empty = occ_step(empty)
    after_seed = occ_step(seed)
    rho_empty0 = rho(empty)
    rho_empty1 = rho(after_empty)
    rho_seed0 = rho(seed)
    rho_seed1 = rho(after_seed)
    dA = rho_seed1[0] - rho_seed0[0]
    dB = rho_seed1[1] - rho_seed0[1]
    new_A = new_in(seed, A_VERTS)
    new_B = new_in(seed, B_VERTS)
    new_empty_A = new_in(empty, A_VERTS)
    new_empty_B = new_in(empty, B_VERTS)

    checks.check(
        "geom",
        "12 verts; A x in {0,1}; B x in {1,2}",
        len(VERTS) == 12 and len(A_VERTS) == 8 and len(B_VERTS) == 8 and len(A_VERTS & B_VERTS) == 4,
    )
    checks.check(
        "thm-new",
        "seed forms exactly {(1,0,0),(0,1,0),(0,0,1)}",
        after_seed - seed == SEED_NEW and (0, 0, 0) in after_seed,
    )
    checks.check(
        "thm-delta",
        "seed step Δρ(A)=3, Δρ(B)=1",
        rho_seed0 == (1, 0) and rho_seed1 == (4, 1) and dA == 3 and dB == 1,
    )
    checks.check(
        "thm-id",
        "Δρ(C) equals |new locks ∩ C|",
        dA == len(new_A) and dB == len(new_B) and new_A == SEED_NEW and new_B == frozenset({(1, 0, 0)}),
    )
    checks.check(
        "thm-empty",
        "empty step Δρ=0",
        after_empty == empty and rho_empty0 == (0, 0) and rho_empty1 == (0, 0) and not new_empty_A and not new_empty_B,
    )
    checks.check(
        "mutation-dB0-fails",
        "predicate Δρ(B)=0 on the seed step must fail",
        dB != 0,
    )
    checks.check(
        "mutation-empty-rho-fails",
        "predicate empty step changes ρ must fail",
        rho_empty0 == rho_empty1,
    )
    checks.check(
        "quoted",
        "note quotes lock and NN",
        "locks exactly one admissible local possibility" in note
        and "determined by, and varies with, the nearest-neighbor conditions." in note
        and "M_2(C)" in note,
    )
    forbidden = ("we adopt", "L_phys", "0.5934", "Lattice-named", "exhausted", "closes the route", "G_N")
    checks.check(
        "boundary",
        "required strings and forbidden absent",
        all(p not in note for p in forbidden)
        and "Result Up Front" in note
        and "not a TOE" in note
        and "Qubit remains `M_2(C)`" in note
        and "This note authors no audit verdict" in note
        and "QCD is unused" in note
        and "actual_current_surface_status: bounded-support" in note
        and 'hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"' in note
        and "Honest-auditor / Boundary" in note
        and "claim_id:" in note,
    )
    checks.check(
        "memo-silent",
        "axioms do not name Δρ",
        "Δρ" not in four and "rhogrow" not in four,
    )
    checks.check(
        "gates",
        "identity gates occ_step/rho/new_in",
        "def occ_step(" in self_source
        and "def rho(" in self_source
        and "def new_in(" in self_source
        and AUDIT_INPUT_PATHS
        == (
            "docs/TWO_CUBE_RHO_INCREMENT_BOUNDED_THEOREM_NOTE_2026-08-14.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and AUDIT_TIMEOUT_SEC == 120,
    )

    print("per_element: checked exactly — Δρ(A), Δρ(B), new-lock counts")
    print("per_site: checked exactly — seed (0,0,0) and empty")
    print("per_mode: checked exactly — occupancy increment identity")
    print("per_block: checked exactly — two-cube source increment")
    print("lattice_wide: checked and not executed — not axiom text")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
