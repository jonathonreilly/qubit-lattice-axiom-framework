#!/usr/bin/env python3
"""Exact checks for f_two three-site seed fill on the two-cube.

Reconstructs the displayed f_two occupancy-lock ticks (form iff u>=2)
on the twelve-site two-cube patch from the axis-triple seed. Writes no
cache and no governance surface.
"""

from __future__ import annotations

from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
AUDIT_INPUT_PATHS = (
    "docs/F_TWO_THREE_SITE_SEED_FILL_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / AUDIT_INPUT_PATHS[0]
AXIOM_PATH = ROOT / AUDIT_INPUT_PATHS[1]

Vec = tuple[int, int, int]
AXES: tuple[Vec, ...] = ((1, 0, 0), (0, 1, 0), (0, 0, 1))

CUBE_A = frozenset((x, y, z) for x in (0, 1) for y in (0, 1) for z in (0, 1))
CUBE_B = frozenset((x, y, z) for x in (1, 2) for y in (0, 1) for z in (0, 1))
PATCH = CUBE_A | CUBE_B
SEED: frozenset[Vec] = frozenset({(1, 0, 0), (0, 1, 0), (0, 0, 1)})

FORBIDDEN_NOTE_SUBSTRINGS = (
    "G_N",
    "1/r",
    "1/r^2",
    "Lattice-named",
    "not a TOE",
    "exhausted",
    "only route",
    "we adopt",
    "Codex",
    "L_phys",
    "PVM",
)


def plus(site: Vec, step: Vec) -> Vec:
    return (site[0] + step[0], site[1] + step[1], site[2] + step[2])


def minus(site: Vec, step: Vec) -> Vec:
    return (site[0] - step[0], site[1] - step[1], site[2] - step[2])


def occupancy(site: Vec, locks: frozenset[Vec]) -> int:
    return 1 if site in locks else 0


def unbalanced_axes(site: Vec, locks: frozenset[Vec]) -> int:
    return sum(
        occupancy(plus(site, axis), locks) != occupancy(minus(site, axis), locks)
        for axis in AXES
    )


def ready_sites(locks: frozenset[Vec]) -> frozenset[Vec]:
    return frozenset(
        site
        for site in PATCH
        if site not in locks and unbalanced_axes(site, locks) >= 2
    )


def step(locks: frozenset[Vec]) -> frozenset[Vec]:
    return locks | ready_sites(locks)


def evolve_until_halt(max_ticks: int = 12) -> tuple[int, frozenset[Vec], list[frozenset[Vec]]]:
    hist = [SEED]
    locks = SEED
    for tick in range(1, max_ticks + 1):
        nxt = step(locks)
        if nxt == locks:
            return tick - 1, locks, hist
        locks = nxt
        hist.append(locks)
    return max_ticks, locks, hist


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


def hygiene(checks: Checks, note: str, axiom: str) -> None:
    checks.check("audit-input-paths-exist", all((ROOT / p).is_file() for p in AUDIT_INPUT_PATHS))
    checks.check(
        "audit-input-paths-unique-relative",
        len(AUDIT_INPUT_PATHS) == len(set(AUDIT_INPUT_PATHS))
        and all(not Path(p).is_absolute() and ".." not in Path(p).parts for p in AUDIT_INPUT_PATHS),
    )
    checks.check("audit-timeout-declared", AUDIT_TIMEOUT_SEC == 120)
    checks.check("lattice-quote-present", "proper cubic rotations" in axiom)
    checks.check("record-form-quote-present", "Records form" in axiom)
    for token in FORBIDDEN_NOTE_SUBSTRINGS:
        checks.check(f"hygiene-avoids-{token!r}", token not in note)
    checks.check("note-has-no-runner-cache-path", "runner-cache" not in note)
    checks.check("note-has-no-citation-manifest", "citation_manifest" not in note)
    checks.check("patch-has-twelve-sites", len(PATCH) == 12)
    checks.check("seed-is-axis-triple", SEED == frozenset({(1, 0, 0), (0, 1, 0), (0, 0, 1)}))
    checks.check("seed-sites-on-patch", SEED <= PATCH)
    checks.check("off-patch-occupancy-is-zero", occupancy((3, 0, 0), SEED) == 0)


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    print("f_two three-site seed fill on the two-cube")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print("scope: supplied two-cube f_two patch; 3-site seed halt census")
    hygiene(checks, note, axiom)

    first_wave = ready_sites(SEED)
    halt_tick, locks, hist = evolve_until_halt(12)
    post_halt = step(locks)
    unlocked = PATCH - locks

    checks.check("theorem-1-first-wave-nonempty", len(first_wave) > 0)
    checks.check("origin-ready-at-seed", (0, 0, 0) in first_wave)
    checks.check(
        "first-wave-computed-set",
        first_wave == frozenset({(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0)}),
    )
    checks.check("theorem-2-halt-within-twelve", halt_tick <= 12)
    checks.check("theorem-2-halt-is-fixed-point", post_halt == locks)
    checks.check("seed-permanent-in-halt", SEED <= locks)
    checks.check("locks-monotone", all(hist[i] <= hist[i + 1] for i in range(len(hist) - 1)))
    if halt_tick > 0:
        checks.check("halt-tick-is-first-fixed-point", step(hist[halt_tick - 1]) != hist[halt_tick - 1])
    checks.check("theorem-3-halt-tick", halt_tick == 2, f"T={halt_tick}")
    checks.check("theorem-3-lock-count", len(locks) == 8, f"|locks|={len(locks)}")
    checks.check("theorem-3-patch-does-not-fill", locks != PATCH and len(locks) != 12)
    checks.check("halt-locks-equal-cube-a", locks == CUBE_A)
    checks.check(
        "x-equals-two-sites-unlocked",
        unlocked == frozenset({(2, 0, 0), (2, 0, 1), (2, 1, 0), (2, 1, 1)}),
    )
    checks.check(
        "unlocked-sites-have-u-less-than-two",
        all(unbalanced_axes(site, locks) < 2 for site in unlocked),
    )
    checks.check("note-reports-halt-tick-two", "T = 2" in note)
    checks.check("note-reports-eight-locks", "|locks_2| = 8" in note)
    checks.check("note-reports-does-not-fill", "does not fill" in note)

    print(f"halt_tick: {halt_tick}")
    print(f"lock_count: {len(locks)}")
    print(f"fills_patch: {locks == PATCH}")
    print("per_element: 12 vertices")
    print("per_site: occupancy lock")
    print("per_mode: f_two u>=2")
    print("per_block: halt census")
    print("lattice_wide: checked and not executed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
