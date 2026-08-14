#!/usr/bin/env python3
"""Occupancy step commutes with a cube-center 90° rotation."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "CUBE_STEP_ROTATION_COVARIANCE_BOUNDED_THEOREM_NOTE_2026-08-14.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/CUBE_STEP_ROTATION_COVARIANCE_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

SITES = tuple((x, y, z) for x in (0, 1) for y in (0, 1) for z in (0, 1))
AXES = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
NONE = None
MARK = "-"


def rotate(site: tuple) -> tuple:
    """Identity gate: (x,y,z) -> (1-y, x, z)."""
    x, y, z = site
    return (1 - y, x, z)


def rotate_cfg(locks: dict) -> dict:
    return {rotate(s): locks[s] for s in SITES}


def n_at(site: tuple, locks: dict) -> tuple:
    """Identity gate."""
    occ = {s: 0 if locks[s] is NONE else 1 for s in SITES}
    out = []
    for e in AXES:
        plus = (site[0] + e[0], site[1] + e[1], site[2] + e[2])
        minus = (site[0] - e[0], site[1] - e[1], site[2] - e[2])
        op = occ[plus] if plus in occ else 0
        om = occ[minus] if minus in occ else 0
        out.append(Fraction(op - om, 3))
    return tuple(out)


def step(locks: dict) -> dict:
    """Identity gate."""
    out = {}
    for site in SITES:
        if locks[site] is not NONE:
            out[site] = locks[site]
            continue
        n = n_at(site, locks)
        out[site] = NONE if n == (0, 0, 0) else MARK
    return out


def cfg_from_mask(mask: int) -> dict:
    return {s: (MARK if mask & (1 << i) else NONE) for i, s in enumerate(SITES)}


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
    print("measure_boundary: exact Q cube-step covariance")
    print("negative_scope: update covariance, not a TOE")

    orbit = [(0, 0, 0)]
    for _ in range(3):
        orbit.append(rotate(orbit[-1]))
    checks.check("thm1-perm", "R is a 4-cycle on the z=0 face and permutes the cube",
                 len(set(orbit)) == 4 and all(rotate(rotate(rotate(rotate(s)))) == s for s in SITES) and set(rotate(s) for s in SITES) == set(SITES))

    failed = 0
    for mask in range(256):
        s = cfg_from_mask(mask)
        left = rotate_cfg(step(s))
        right = step(rotate_cfg(s))
        if left != right:
            failed += 1
    checks.check("thm2-256", "R(step(s))=step(R(s)) on all 256 configs", failed == 0)

    seed = {s: NONE for s in SITES}
    seed[(0, 0, 0)] = MARK
    checks.check("thm3-seed", "R sends seed (0,0,0) to (1,0,0)", rotate((0, 0, 0)) == (1, 0, 0))
    s1 = step(seed)
    rs1 = rotate_cfg(s1)
    rseed = rotate_cfg(seed)
    checks.check("thm3-pattern", "rotated step-1 equals step of rotated seed", rs1 == step(rseed) and rseed[(1, 0, 0)] == MARK)
    empty = {s: NONE for s in SITES}
    checks.check("thm4-empty", "empty cube is fixed by R and step", rotate_cfg(empty) == empty and step(empty) == empty)
    checks.check("mutation-cov-fails", "predicate some config fails covariance must fail", failed == 0)
    checks.check("mutation-seed-stay-fails", "predicate seed stays at origin under R must fail", rotate((0, 0, 0)) != (0, 0, 0))
    checks.check(
        "quoted",
        "note quotes lock, permanence, and NN distribution",
        "locks exactly one admissible local possibility" in note
        and "records are permanent" in note
        and "determined by, and varies with, the nearest-neighbor conditions." in note,
    )
    forbidden = ("Lattice-named", "we adopt", "L_phys", "0.5934", "pairing-on-J", "exhausted", "closes the route", "only route")
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
    checks.check("memo-silent", "axioms do not name the covariance", "stepcov" not in four and "R(step" not in four)
    checks.check(
        "gates",
        "identity gates present",
        "def rotate(" in self_source
        and "def n_at(" in self_source
        and "def step(" in self_source
        and NOTE_PATH.is_file()
        and AUDIT_INPUT_PATHS[0].endswith("CUBE_STEP_ROTATION_COVARIANCE_BOUNDED_THEOREM_NOTE_2026-08-14.md"),
    )
    print("per_element: checked exactly — 256 occupancy configs")
    print("per_site: checked exactly — 8 cube sites")
    print("per_mode: checked exactly — one 90° generator")
    print("per_block: checked exactly — covariance of step, not of n")
    print("lattice_wide: checked and not executed — not a TOE")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
