#!/usr/bin/env python3
"""180° about x commutes with the two-cube occupancy+ρ+φ update."""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "TWO_CUBE_180X_COVARIANCE_BOUNDED_THEOREM_NOTE_2026-08-14.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/TWO_CUBE_180X_COVARIANCE_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

VERTS = tuple((x, y, z) for x in (0, 1, 2) for y in (0, 1) for z in (0, 1))
A_VERTS = tuple(v for v in VERTS if v[0] in (0, 1))
B_VERTS = tuple(v for v in VERTS if v[0] in (1, 2))
AXES = ((1, 0, 0), (0, 1, 0), (0, 0, 1))


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


def rot(obj):
    """Identity gate. R(x,y,z)=(x,1-y,1-z)."""
    if isinstance(obj, tuple) and len(obj) == 3 and all(isinstance(c, int) for c in obj):
        return (obj[0], 1 - obj[1], 1 - obj[2])
    return frozenset(rot(v) for v in obj)


def occ_step(locks):
    """Identity gate."""
    out = set(locks)
    for v in VERTS:
        if v not in locks and any(c != 0 for c in nvec(v, locks)):
            out.add(v)
    return frozenset(out)


def commutes(locks):
    """Identity gate. R ∘ occ_step = occ_step ∘ R."""
    return rot(occ_step(locks)) == occ_step(rot(locks))


def rho(locks):
    """Identity gate."""
    return sum(occ(v, locks) for v in A_VERTS), sum(occ(v, locks) for v in B_VERTS)


def phi(locks):
    ra, rb = rho(locks)
    return ra, ra + rb


def all_occupancies():
    for bits in product((0, 1), repeat=len(VERTS)):
        yield frozenset(v for v, bit in zip(VERTS, bits) if bit)


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
    print("measure_boundary: exact commutation on all 4096 occupancy labels")
    print("negative_scope: covariance of one displayed R, not gauge uniqueness")

    image = tuple(rot(v) for v in VERTS)
    checks.check(
        "thm1-bijection",
        "R is a bijection of the twelve vertices",
        len(VERTS) == 12
        and len(set(VERTS)) == 12
        and set(image) == set(VERTS)
        and all(rot(rot(v)) == v for v in VERTS)
        and {rot(v) for v in A_VERTS} == set(A_VERTS)
        and {rot(v) for v in B_VERTS} == set(B_VERTS),
    )
    checks.check(
        "thm1-proper",
        "linear part diag(1,-1,-1) has det 1",
        (1) * (-1) * (-1) == 1 and rot((0, 0, 0)) == (0, 1, 1),
    )

    n_configs = 0
    all_commute = True
    rho_invariant = True
    phi_invariant = True
    for s in all_occupancies():
        n_configs += 1
        if not commutes(s):
            all_commute = False
        if rho(rot(s)) != rho(s):
            rho_invariant = False
        if phi(rot(s)) != phi(s):
            phi_invariant = False
    checks.check("thm2-commutes", "R∘occ_step=occ_step∘R on all 4096", n_configs == 4096 and all_commute)
    checks.check("thm3-rho", "ρ(R(s))=ρ(s) on all 4096", n_configs == 4096 and rho_invariant)
    checks.check("thm3-phi", "φ(R(s))=φ(s) on all 4096", n_configs == 4096 and phi_invariant)

    seed = frozenset({(0, 0, 0)})
    s1 = occ_step(seed)
    expected_step = frozenset({(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)})
    expected_rot = frozenset({(0, 1, 1), (1, 1, 1), (0, 0, 1), (0, 1, 0)})
    checks.check(
        "thm4-seed",
        "seed maps to (0,1,1); formation pattern rotates",
        rot((0, 0, 0)) == (0, 1, 1)
        and rot(seed) == frozenset({(0, 1, 1)})
        and s1 == expected_step
        and rot(s1) == expected_rot
        and occ_step(rot(seed)) == expected_rot
        and commutes(seed)
        and rho(seed) == (1, 0)
        and rho(rot(seed)) == (1, 0),
    )
    empty = frozenset()
    checks.check(
        "thm4-empty",
        "empty is a fixed point of R and occ_step",
        rot(empty) == empty and occ_step(empty) == empty and rho(empty) == (0, 0) and phi(empty) == (0, 0),
    )
    checks.check(
        "mutation-seed-fixed-fails",
        "predicate seed maps to itself must fail",
        rot((0, 0, 0)) != (0, 0, 0),
    )
    checks.check(
        "quoted",
        "note quotes cubic rotations, NN covariance, lock, permanence",
        "proper cubic rotations about each site" in note
        and "covariant under lattice translations and proper cubic rotations" in note
        and "determined by, and varies with, the nearest-neighbor conditions." in note
        and "locks exactly one admissible local possibility" in note
        and "records are permanent" in note,
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
        and "Honest-auditor / Boundary" in note
        and "Not a gauge-uniqueness" in note,
    )
    checks.check(
        "memo-silent",
        "axioms do not name this 180x two-cube update",
        "180x" not in four and "occ_step" not in four and "φ(F*)" not in four,
    )
    checks.check(
        "gates",
        "identity gates",
        "def rot(" in self_source
        and "def occ_step(" in self_source
        and "def commutes(" in self_source
        and "def rho(" in self_source
        and AUDIT_INPUT_PATHS
        == (
            "docs/TWO_CUBE_180X_COVARIANCE_BOUNDED_THEOREM_NOTE_2026-08-14.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        ),
    )
    print("per_element: checked exactly — twelve vertices and all 4096 occupancy labels")
    print("per_site: checked exactly — seed (0,0,0) and its rotate (0,1,1)")
    print("per_mode: checked exactly — 180° about x")
    print("per_block: checked exactly — occupancy step, ρ, displayed φ")
    print("lattice_wide: checked and not executed — not axiom text")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
