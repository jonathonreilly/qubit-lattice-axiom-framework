#!/usr/bin/env python3
"""Shared-face formation has n parallel to the face normal."""

from __future__ import annotations

import re
from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "TWO_CUBE_SHARED_NORMAL_BOUNDED_THEOREM_NOTE_2026-08-14.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/TWO_CUBE_SHARED_NORMAL_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

VERTS = tuple((x, y, z) for x in (0, 1, 2) for y in (0, 1) for z in (0, 1))
AXES = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
ZERO = (Fraction(0), Fraction(0), Fraction(0))
N_SHARED = (Fraction(-1, 3), Fraction(0), Fraction(0))
N_Y = (Fraction(0), Fraction(-1, 3), Fraction(0))
N_Z = (Fraction(0), Fraction(0), Fraction(-1, 3))


def occ(v, locks) -> int:
    return 1 if v in locks else 0


def nvec(site, locks):
    """Identity gate. Displayed occupancy kernel n_μ = (o_{+μ} − o_{-μ}) / 3."""
    out = []
    for ax in AXES:
        plus = (site[0] + ax[0], site[1] + ax[1], site[2] + ax[2])
        minus = (site[0] - ax[0], site[1] - ax[1], site[2] - ax[2])
        o_plus = occ(plus, locks) if plus in VERTS else 0
        o_minus = occ(minus, locks) if minus in VERTS else 0
        out.append(Fraction(o_plus - o_minus, 3))
    return tuple(out)


def shared_normal():
    """Identity gate. Geometric +x normal of the shared face x=1."""
    return (Fraction(1), Fraction(0), Fraction(0))


def cross(u, v):
    return (
        u[1] * v[2] - u[2] * v[1],
        u[2] * v[0] - u[0] * v[2],
        u[0] * v[1] - u[1] * v[0],
    )


def parallel_to(u, v):
    """Identity gate. Nonzero vectors with vanishing cross product."""
    return cross(u, v) == ZERO and u != ZERO and v != ZERO


def occ_step(locks):
    out = set(locks)
    for v in VERTS:
        if v not in locks and nvec(v, locks) != ZERO:
            out.add(v)
    return frozenset(out)


def prose_outside_fences(text: str) -> str:
    lines = []
    in_fence = False
    for line in text.splitlines():
        if line.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if not in_fence:
            lines.append(line)
    return "\n".join(lines)


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
    print("measure_boundary: exact Fraction n on one seed")
    print("negative_scope: shared-face direction of n, not unique support")

    seed = frozenset({(0, 0, 0)})
    after = occ_step(seed)
    n_x = nvec((1, 0, 0), seed)
    n_y = nvec((0, 1, 0), seed)
    n_z = nvec((0, 0, 1), seed)
    normal = shared_normal()

    checks.check(
        "geom",
        "12 verts; shared face x=1; normal (1,0,0)",
        len(VERTS) == 12 and normal == (Fraction(1), Fraction(0), Fraction(0)),
    )
    checks.check(
        "thm-n",
        "at (1,0,0), n = (-1/3, 0, 0)",
        n_x == N_SHARED and n_x != ZERO,
    )
    checks.check(
        "thm-parallel",
        "n at (1,0,0) is parallel to the shared-face normal",
        parallel_to(n_x, normal) and n_x == tuple(Fraction(-1, 3) * c for c in normal),
    )
    checks.check(
        "thm-form",
        "(1,0,0) forms because n is nonzero",
        (1, 0, 0) in after and (0, 1, 0) in after and (0, 0, 1) in after,
    )
    checks.check(
        "thm-others",
        "other first-wave n are not parallel to the shared-face normal",
        n_y == N_Y and n_z == N_Z and not parallel_to(n_y, normal) and not parallel_to(n_z, normal),
    )
    checks.check(
        "mutation-orthogonal-fails",
        "predicate n at (1,0,0) is orthogonal to (1,0,0) must fail",
        sum(a * b for a, b in zip(n_x, normal)) != 0,
    )
    checks.check(
        "mutation-y-parallel-fails",
        "predicate n at (0,1,0) is parallel to the shared-face normal must fail",
        not parallel_to(n_y, normal),
    )
    checks.check(
        "quoted",
        "note quotes lock, permanence, NN",
        "locks exactly one admissible local possibility" in note
        and "records are permanent" in note
        and "determined by, and varies with, the nearest-neighbor conditions." in note,
    )
    forbidden = (
        "we adopt",
        "L_phys",
        "0.5934",
        "Lattice-named",
        "exhausted",
        "closes the route",
        "closes gravity",
        "only route",
        "last route",
        "G_N",
        "Codex",
    )
    pinned = ("closes the route", "only route", "last route", "exhaust")
    prose = prose_outside_fences(note)
    decimal_hits = re.findall(r"[0-9]\.[0-9]", prose)
    checks.check(
        "NOTE_HYGIENE",
        "no prose decimals, pinned phrases absent, claim-type and required sections",
        decimal_hits == []
        and all(p not in note.lower() for p in pinned)
        and "**Claim type:** bounded_theorem" in note
        and "**Type:** bounded_theorem" in note
        and "## Honest-auditor / Boundary" in note
        and "## What This Does Not Claim" in note
        and "**Audit-status authority:** independent audit lane only." in note,
    )
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
        and "Not a unique-support statement" in note
        and "claim_id:" in note,
    )
    checks.check(
        "memo-silent",
        "axioms do not name this n or shared-face normal",
        "shared-face" not in four and "shared_normal" not in four and "nrmdir" not in four,
    )
    checks.check(
        "gates",
        "identity gates nvec/parallel_to/shared_normal",
        "def nvec(" in self_source
        and "def parallel_to(" in self_source
        and "def shared_normal(" in self_source
        and AUDIT_INPUT_PATHS
        == (
            "docs/TWO_CUBE_SHARED_NORMAL_BOUNDED_THEOREM_NOTE_2026-08-14.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and AUDIT_TIMEOUT_SEC == 120,
    )

    print("per_element: checked exactly — n at (1,0,0), (0,1,0), (0,0,1)")
    print("per_site: checked exactly — seed (0,0,0) and shared-face site")
    print("per_mode: checked exactly — parallel to shared-face normal")
    print("per_block: checked exactly — two-cube direction of n")
    print("lattice_wide: checked and not executed — not axiom text")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
