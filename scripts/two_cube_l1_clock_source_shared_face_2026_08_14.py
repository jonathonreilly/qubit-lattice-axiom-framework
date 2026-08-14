#!/usr/bin/env python3
"""Exact checks for the L1 clock versus double-counted source increment.

On the supplied two-cube patch the occupancy kernel is reconstructed locally.
Each tick is compared to the shared-face identity

    Delta rho(A) + Delta rho(B) = F_tick + S,   S = |new locks intersect F*|.

No cache or governance surface is written.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "TWO_CUBE_L1_CLOCK_SOURCE_SHARED_FACE_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/TWO_CUBE_L1_CLOCK_SOURCE_SHARED_FACE_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Vec = tuple[int, int, int]
AXES: tuple[Vec, ...] = ((1, 0, 0), (0, 1, 0), (0, 0, 1))

CUBE_A = frozenset(
    (x, y, z) for x in (0, 1) for y in (0, 1) for z in (0, 1)
)
CUBE_B = frozenset(
    (x, y, z) for x in (1, 2) for y in (0, 1) for z in (0, 1)
)
PATCH = CUBE_A | CUBE_B
SHARED_FACE = frozenset(site for site in PATCH if site[0] == 1)
SEED: Vec = (0, 0, 0)

FORBIDDEN_NOTE_SUBSTRINGS = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE")


def plus(site: Vec, step: Vec) -> Vec:
    return (site[0] + step[0], site[1] + step[1], site[2] + step[2])


def minus(site: Vec, step: Vec) -> Vec:
    return (site[0] - step[0], site[1] - step[1], site[2] - step[2])


def occupancy(site: Vec, locks: frozenset[Vec]) -> int:
    return 1 if site in locks else 0


def n_vector(site: Vec, locks: frozenset[Vec]) -> tuple[Fraction, Fraction, Fraction]:
    return tuple(
        Fraction(occupancy(plus(site, axis), locks) - occupancy(minus(site, axis), locks), 3)
        for axis in AXES
    )


def rho(cube: frozenset[Vec], locks: frozenset[Vec]) -> int:
    return sum(occupancy(site, locks) for site in cube)


def unread_with_nonzero_n(locks: frozenset[Vec]) -> frozenset[Vec]:
    forming: set[Vec] = set()
    for site in PATCH:
        if site in locks:
            continue
        if any(component != 0 for component in n_vector(site, locks)):
            forming.add(site)
    return frozenset(forming)


def step(locks: frozenset[Vec]) -> tuple[frozenset[Vec], frozenset[Vec], int]:
    new_locks = unread_with_nonzero_n(locks)
    return locks | new_locks, new_locks, len(new_locks)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, condition: bool, detail: str = "") -> None:
        ok = bool(condition)
        self.passed += int(ok)
        self.failed += int(not ok)
        suffix = f"  ({detail})" if detail else ""
        print(f"{'PASS' if ok else 'FAIL'}: {label}{suffix}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")

    print("L1 clock versus double-counted two-cube source increment")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print("scope: supplied two-cube L1 patch; shared-face identity only")

    checks.check(
        "audit-input-paths-exist",
        all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    )
    checks.check(
        "audit-input-paths-unique-relative",
        len(AUDIT_INPUT_PATHS) == len(set(AUDIT_INPUT_PATHS))
        and all(
            not Path(path).is_absolute() and ".." not in Path(path).parts
            for path in AUDIT_INPUT_PATHS
        ),
    )
    checks.check("audit-timeout-declared", AUDIT_TIMEOUT_SEC == 120)
    checks.check(
        "shared-face-is-x-equals-one",
        SHARED_FACE == CUBE_A & CUBE_B,
        f"|F*|={len(SHARED_FACE)}",
    )
    checks.check("seed-in-A-not-B", SEED in CUBE_A and SEED not in CUBE_B)
    checks.check(
        "note-forbids-listed-substrings",
        all(token not in note for token in FORBIDDEN_NOTE_SUBSTRINGS),
    )
    checks.check("note-has-no-runner-cache-path", "runner-cache" not in note)
    checks.check("note-has-no-citation-manifest", "citation_manifest" not in note)

    locks0 = frozenset({SEED})
    rho_a0 = rho(CUBE_A, locks0)
    rho_b0 = rho(CUBE_B, locks0)
    checks.check("seed-rho", rho_a0 == 1 and rho_b0 == 0)

    locks1, new1, f1 = step(locks0)
    rho_a1 = rho(CUBE_A, locks1)
    rho_b1 = rho(CUBE_B, locks1)
    delta_a1 = rho_a1 - rho_a0
    delta_b1 = rho_b1 - rho_b0
    shared1 = new1 & SHARED_FACE
    s1 = len(shared1)

    checks.check(
        "tick1-new-locks",
        new1 == frozenset({(1, 0, 0), (0, 1, 0), (0, 0, 1)}),
        f"new1={sorted(new1)}",
    )
    checks.check("tick1-F", f1 == 3)
    checks.check("tick1-S-set", shared1 == frozenset({(1, 0, 0)}), f"S1={sorted(shared1)}")
    checks.check("tick1-S", s1 == 1)
    checks.check("tick1-delta-rho-A", delta_a1 == 3)
    checks.check("tick1-delta-rho-B", delta_b1 == 1)
    checks.check("tick1-identity", delta_a1 + delta_b1 == f1 + s1 == 4)
    checks.check("tick1-delta-A-is-new-locks-in-A", delta_a1 == len(new1 & CUBE_A))
    checks.check("tick1-delta-B-is-new-locks-in-B", delta_b1 == len(new1 & CUBE_B))
    checks.check("tick1-F-is-not-sum-delta-rho", f1 != delta_a1 + delta_b1)

    locks2, new2, f2 = step(locks1)
    rho_a2 = rho(CUBE_A, locks2)
    rho_b2 = rho(CUBE_B, locks2)
    delta_a2 = rho_a2 - rho_a1
    delta_b2 = rho_b2 - rho_b1
    shared2 = new2 & SHARED_FACE
    s2 = len(shared2)

    checks.check(
        "tick2-new-locks",
        new2 == frozenset({(1, 1, 0), (1, 0, 1), (0, 1, 1), (2, 0, 0)}),
        f"new2={sorted(new2)}",
    )
    checks.check("tick2-F", f2 == 4)
    checks.check(
        "tick2-S-set",
        shared2 == frozenset({(1, 1, 0), (1, 0, 1)}),
        f"S2={sorted(shared2)}",
    )
    checks.check("tick2-S", s2 == 2)
    checks.check("tick2-delta-rho-A", delta_a2 == 3)
    checks.check("tick2-delta-rho-B", delta_b2 == 3)
    checks.check("tick2-identity", delta_a2 + delta_b2 == f2 + s2 == 6)
    checks.check("tick2-delta-A-is-new-locks-in-A", delta_a2 == len(new2 & CUBE_A))
    checks.check("tick2-delta-B-is-new-locks-in-B", delta_b2 == len(new2 & CUBE_B))
    checks.check("tick2-F-is-not-sum-delta-rho", f2 != delta_a2 + delta_b2)

    locked_stay = all(site in locks2 for site in locks1)
    checks.check("locked-sites-stay-locked", locked_stay)

    unique_s1 = [s for s in range(len(SHARED_FACE) + 1) if delta_a1 + delta_b1 == f1 + s]
    unique_s2 = [s for s in range(len(SHARED_FACE) + 1) if delta_a2 + delta_b2 == f2 + s]
    checks.check("tick1-S-unique-in-0-to-4", unique_s1 == [s1])
    checks.check("tick2-S-unique-in-0-to-4", unique_s2 == [s2])

    union_delta_1 = rho(PATCH, locks1) - rho(PATCH, locks0)
    union_delta_2 = rho(PATCH, locks2) - rho(PATCH, locks1)
    checks.check("tick1-F-equals-union-occupancy-increment", f1 == union_delta_1)
    checks.check("tick2-F-equals-union-occupancy-increment", f2 == union_delta_2)
    checks.check(
        "sum-of-cube-increments-is-not-union-increment",
        delta_a1 + delta_b1 != union_delta_1 and delta_a2 + delta_b2 != union_delta_2,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
