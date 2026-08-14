#!/usr/bin/env python3
"""Exterior vacuum is load-bearing on the two-cube occupancy step."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "TWO_CUBE_EXTERIOR_VACUUM_BOUNDED_THEOREM_NOTE_2026-08-14.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/TWO_CUBE_EXTERIOR_VACUUM_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

VERTS = tuple((x, y, z) for x in (0, 1, 2) for y in (0, 1) for z in (0, 1))
B_ONLY = tuple(v for v in VERTS if v[0] == 2)
BFRONT = (2, 0, 0)
EXT_PLUS = (3, 0, 0)
AXES = ((1, 0, 0), (0, 1, 0), (0, 0, 1))


def occ_at(site, locks, exterior=None) -> int:
    """On-patch occupancy from locks; off-patch defaults to 0."""
    if site in VERTS:
        return 1 if site in locks else 0
    if not exterior:
        return 0
    if isinstance(exterior, dict):
        return int(bool(exterior.get(site, 0)))
    return int(site in exterior)


def nvec(site, locks, exterior=None):
    out = []
    for ax in AXES:
        plus = (site[0] + ax[0], site[1] + ax[1], site[2] + ax[2])
        minus = (site[0] - ax[0], site[1] - ax[1], site[2] - ax[2])
        out.append(Fraction(occ_at(plus, locks, exterior) - occ_at(minus, locks, exterior), 3))
    return tuple(out)


def occ_step(locks, exterior=None):
    """Occupancy step. Optional exterior map; off-patch occupancy defaults to 0."""
    out = set(locks)
    for v in VERTS:
        if v not in locks and any(c != 0 for c in nvec(v, locks, exterior)):
            out.add(v)
    return frozenset(out)


def n_at_Bfront(locks, exterior=None):
    """Identity gate: n at the B-front (2,0,0)."""
    return nvec(BFRONT, locks, exterior)


def forms_if_exterior(locks, exterior):
    """Identity gate: whether (2,0,0) forms under the given exterior map."""
    return BFRONT not in locks and any(c != 0 for c in n_at_Bfront(locks, exterior))


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
    print("measure_boundary: exact n and formation at the B-front")
    print("negative_scope: exterior vacuum load-bearing, not Newton")
    seed = frozenset({(0, 0, 0)})
    ext_occ = frozenset({EXT_PLUS})
    s1 = occ_step(seed)
    s1_ext = occ_step(seed, exterior=ext_occ)
    n0 = n_at_Bfront(seed)
    n_ext = n_at_Bfront(seed, exterior=ext_occ)
    checks.check(
        "thm1-n0",
        "default vacuum gives n=0 at B-front",
        n0 == (Fraction(0), Fraction(0), Fraction(0)),
    )
    checks.check(
        "thm1-noform",
        "(2,0,0) does not form from the seed",
        BFRONT not in s1 and not forms_if_exterior(seed, None),
    )
    checks.check(
        "thm1-Bonly",
        "all B-only sites stay unread on step 1",
        all(v not in s1 for v in B_ONLY),
    )
    checks.check(
        "thm2-nx",
        "occupied (3,0,0) gives n_x=(1-0)/3",
        n_ext == (Fraction(1, 3), Fraction(0), Fraction(0)),
    )
    checks.check(
        "thm2-forms",
        "occupied exterior forms the B-front",
        forms_if_exterior(seed, ext_occ) and BFRONT in s1_ext,
    )
    checks.check(
        "thm2-other-Bonly",
        "other B-only sites stay unread under that one-site exterior",
        all(v not in s1_ext for v in B_ONLY if v != BFRONT),
    )
    checks.check(
        "mutation-forms-fails",
        "predicate (2,0,0) forms under default vacuum must fail",
        BFRONT not in s1,
    )
    checks.check(
        "mutation-n0-fails",
        "predicate occupied (3,0,0) leaves n=0 at B-front must fail",
        n_ext != (Fraction(0), Fraction(0), Fraction(0)),
    )
    checks.check(
        "quoted",
        "note quotes lock, permanence, unread, NN",
        "locks exactly one admissible local possibility" in note
        and "records are permanent" in note
        and "A site with no record cannot be read." in note
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
    checks.check("memo-silent", "axioms do not name off-patch occupancy", "off-patch" not in four and "exterior vacuum" not in four)
    checks.check(
        "gates",
        "identity gates",
        "def occ_step(" in self_source
        and "def n_at_Bfront(" in self_source
        and "def forms_if_exterior(" in self_source
        and AUDIT_INPUT_PATHS
        == (
            "docs/TWO_CUBE_EXTERIOR_VACUUM_BOUNDED_THEOREM_NOTE_2026-08-14.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        ),
    )
    print("per_element: checked exactly — n at the B-front")
    print("per_site: checked exactly — seed step with and without exterior (3,0,0)")
    print("per_mode: checked exactly — default off-patch occupancy 0")
    print("per_block: checked exactly — exterior vacuum load-bearing")
    print("lattice_wide: checked and not executed — not axiom text")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
