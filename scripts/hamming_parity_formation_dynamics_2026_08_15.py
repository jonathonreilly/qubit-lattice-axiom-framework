#!/usr/bin/env python3
"""Exact checks for Hamming-parity occupancy-lock dynamics on the two-cube.

Reconstructs f_H(c) = |c|_1 mod 2 on six-neighbor occupancy tuples, with
off-patch occupancy 0, from the 1-site seed (0,0,0). Distinct from f_L1,
which is n!=0 / unbalanced-axis. Writes no cache and no governance surface.
"""

from __future__ import annotations

from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
AUDIT_INPUT_PATHS = (
    "docs/HAMMING_PARITY_FORMATION_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / AUDIT_INPUT_PATHS[0]
AXIOM_PATH = ROOT / AUDIT_INPUT_PATHS[1]

Vec = tuple[int, int, int]
Cell = tuple[int, int, int, int, int, int]
AXES: tuple[Vec, ...] = ((1, 0, 0), (0, 1, 0), (0, 0, 1))

CUBE_A = frozenset((x, y, z) for x in (0, 1) for y in (0, 1) for z in (0, 1))
CUBE_B = frozenset((x, y, z) for x in (1, 2) for y in (0, 1) for z in (0, 1))
PATCH = CUBE_A | CUBE_B
SEED: frozenset[Vec] = frozenset({(0, 0, 0)})
AXIS_SITES: frozenset[Vec] = frozenset({(1, 0, 0), (0, 1, 0), (0, 0, 1)})

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
)


def plus(site: Vec, step: Vec) -> Vec:
    return (site[0] + step[0], site[1] + step[1], site[2] + step[2])


def minus(site: Vec, step: Vec) -> Vec:
    return (site[0] - step[0], site[1] - step[1], site[2] - step[2])


def occupancy(site: Vec, locks: frozenset[Vec]) -> int:
    return 1 if site in locks else 0


def six_tuple(site: Vec, locks: frozenset[Vec]) -> Cell:
    bits: list[int] = []
    for axis in AXES:
        bits.append(occupancy(plus(site, axis), locks))
        bits.append(occupancy(minus(site, axis), locks))
    return (bits[0], bits[1], bits[2], bits[3], bits[4], bits[5])


def f_H(cell: Cell) -> int:
    """Hamming parity of the six-neighbor occupancy tuple."""
    return sum(cell) % 2


def f_L1(cell: Cell) -> int:
    """Displayed contrast only: n!=0 / at least one unbalanced axis."""
    return int(any(cell[2 * i] != cell[2 * i + 1] for i in range(3)))


def ready_sites(locks: frozenset[Vec]) -> frozenset[Vec]:
    return frozenset(
        site for site in PATCH if site not in locks and f_H(six_tuple(site, locks)) == 1
    )


def ready_sites_l1(locks: frozenset[Vec]) -> frozenset[Vec]:
    return frozenset(
        site for site in PATCH if site not in locks and f_L1(six_tuple(site, locks)) == 1
    )


def step(locks: frozenset[Vec]) -> frozenset[Vec]:
    return locks | ready_sites(locks)


def step_l1(locks: frozenset[Vec]) -> frozenset[Vec]:
    return locks | ready_sites_l1(locks)


def evolve_until_halt(
    seed: frozenset[Vec], stepper, max_ticks: int = 12
) -> tuple[int, frozenset[Vec], list[frozenset[Vec]]]:
    hist = [seed]
    locks = seed
    for tick in range(1, max_ticks + 1):
        nxt = stepper(locks)
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
    checks.check("lattice-quote-present", "proper cubic rotations" in axiom)
    checks.check("record-form-quote-present", "Records form" in axiom)
    for token in FORBIDDEN_NOTE_SUBSTRINGS:
        checks.check(f"hygiene-avoids-{token!r}", token not in note)
    checks.check("note-has-no-runner-cache-path", "runner-cache" not in note)
    checks.check("note-has-no-citation-manifest", "citation_manifest" not in note)
    checks.check("note-does-not-call-hamming-f-L1", "f_H" in note and "Hamming f_L1" not in note)
    checks.check("note-does-not-identify-hamming-with-L1", "Hamming-as-L1" not in note)
    checks.check("patch-has-twelve-sites", len(PATCH) == 12)
    checks.check("seed-is-origin", SEED == frozenset({(0, 0, 0)}))
    checks.check("seed-on-patch", SEED <= PATCH)
    checks.check("off-patch-occupancy-is-zero", occupancy((3, 0, 0), SEED) == 0)


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    print("Hamming-parity formation dynamics on the two-cube")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print("scope: supplied two-cube Hamming-parity patch; 1-site seed halt census")
    hygiene(checks, note, axiom)

    weight1 = six_tuple((1, 0, 0), SEED)
    checks.check("identity-f-H-on-weight-1", f_H(weight1) == 1, f"c={weight1}")
    checks.check("weight-1-tuple-is-odd", sum(weight1) == 1)
    two_axis = (1, 0, 1, 0, 0, 0)
    checks.check("identity-f-H-on-weight-2-even", f_H(two_axis) == 0)
    checks.check("displayed-f-L1-on-weight-2-unbalanced", f_L1(two_axis) == 1)
    checks.check("f-H-is-not-f-L1", f_H(two_axis) != f_L1(two_axis))
    empty = (0, 0, 0, 0, 0, 0)
    checks.check("identity-f-H-empty-zero", f_H(empty) == 0)
    checks.check("identity-f-H-full-zero", f_H((1, 1, 1, 1, 1, 1)) == 0)

    first_wave = ready_sites(SEED)
    halt_tick, locks, hist = evolve_until_halt(SEED, step, 12)
    post_halt = step(locks)
    unlocked = PATCH - locks
    l1_halt, l1_locks, _ = evolve_until_halt(SEED, step_l1, 12)

    checks.check("theorem-1-first-wave-three-axis-sites", first_wave == AXIS_SITES)
    checks.check(
        "theorem-1-first-wave-weight-1-odd",
        all(sum(six_tuple(site, SEED)) == 1 and f_H(six_tuple(site, SEED)) == 1 for site in first_wave),
    )
    checks.check("theorem-2-halt-within-twelve", halt_tick <= 12)
    checks.check("theorem-2-halt-is-fixed-point", post_halt == locks)
    checks.check("seed-permanent-in-halt", SEED <= locks)
    checks.check(
        "locks-monotone",
        all(hist[i] <= hist[i + 1] for i in range(len(hist) - 1)),
    )
    if halt_tick > 0:
        checks.check(
            "halt-tick-is-last-growth",
            step(hist[halt_tick - 1]) != hist[halt_tick - 1],
        )
    checks.check("theorem-3-halt-tick", halt_tick == 4, f"T={halt_tick}")
    checks.check("theorem-3-lock-count", len(locks) == 9, f"|locks|={len(locks)}")
    checks.check("theorem-3-patch-does-not-fill", locks != PATCH and len(locks) != 12)
    checks.check(
        "unlocked-sites-have-even-hamming",
        all(f_H(six_tuple(site, locks)) == 0 for site in unlocked),
    )
    checks.check(
        "displayed-L1-fills-horizon-4",
        l1_halt == 4 and len(l1_locks) == 12 and l1_locks == PATCH,
    )
    checks.check("hamming-and-L1-same-first-wave", first_wave == ready_sites_l1(SEED))
    checks.check("hamming-and-L1-different-halt-locks", locks != l1_locks)
    checks.check("note-reports-halt-tick-four", "T = 4" in note)
    checks.check("note-reports-nine-locks", "|locks_4| = 9" in note)
    checks.check("note-reports-does-not-fill", "does not fill" in note)
    checks.check("note-displays-L1-horizon-four", "horizon 4" in note)
    checks.check("note-displayed-not-adopted", "not adopted" in note)

    print(f"first_wave: {sorted(first_wave)}")
    print(f"halt_tick: {halt_tick}")
    print(f"lock_count: {len(locks)}")
    print(f"fills_patch: {locks == PATCH}")
    print(f"displayed_L1_halt: {l1_halt}")
    print(f"displayed_L1_locks: {len(l1_locks)}")
    print("per_element: 12 vertices")
    print("per_site: occupancy lock")
    print("per_mode: f_H Hamming parity")
    print("per_block: halt census")
    print("lattice_wide: checked and not executed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
