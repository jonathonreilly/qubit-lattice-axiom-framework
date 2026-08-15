#!/usr/bin/env python3
"""Exact checks for vertex3-orbit indicator dynamics on the two-cube.

Recomputes the ten cube-covariant occupation orbits on the six-ray star
and runs occupancy-lock ticks of the vertex3-orbit indicator (f_v3 = 1
exactly on that complement-fixed orbit) from a 1-site seed with off-patch
o=0. Writes no cache and no governance surface. Does not adopt a member.
"""

from __future__ import annotations

from itertools import permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
AUDIT_INPUT_PATHS = (
    "docs/VERTEX3_ORBIT_INDICATOR_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / AUDIT_INPUT_PATHS[0]
AXIOM_PATH = ROOT / AUDIT_INPUT_PATHS[1]

Vec = tuple[int, int, int]
RAYS: tuple[Vec, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
AXES: tuple[Vec, ...] = ((1, 0, 0), (0, 1, 0), (0, 0, 1))

CUBE_A = frozenset((x, y, z) for x in (0, 1) for y in (0, 1) for z in (0, 1))
CUBE_B = frozenset((x, y, z) for x in (1, 2) for y in (0, 1) for z in (0, 1))
PATCH = CUBE_A | CUBE_B
SEED: Vec = (0, 0, 0)
N_CELLS = 64

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


def occupancy(site: Vec, locks: frozenset[Vec]) -> int:
    return 1 if site in locks else 0


def permutation_sign(values: tuple[int, ...]) -> int:
    inversions = sum(
        values[i] > values[j]
        for i in range(len(values))
        for j in range(i + 1, len(values))
    )
    return -1 if inversions % 2 else 1


def apply_signed_permutation(
    ray: Vec,
    perm: tuple[int, ...],
    signs: tuple[int, ...],
) -> Vec:
    moved = [0, 0, 0]
    for row in range(3):
        moved[row] = signs[row] * ray[perm[row]]
    return (moved[0], moved[1], moved[2])


def proper_cube_ray_permutations() -> tuple[tuple[int, ...], ...]:
    index = {ray: i for i, ray in enumerate(RAYS)}
    rotations: list[tuple[int, ...]] = []
    for perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            if permutation_sign(perm) * signs[0] * signs[1] * signs[2] != 1:
                continue
            image = tuple(
                index[apply_signed_permutation(ray, perm, signs)] for ray in RAYS
            )
            rotations.append(image)
    return tuple(rotations)


def apply_perm(mask: int, perm: tuple[int, ...]) -> int:
    image = 0
    for src, dest in enumerate(perm):
        if mask >> src & 1:
            image |= 1 << dest
    return image


def complement(mask: int) -> int:
    return mask ^ (N_CELLS - 1)


def orbit_of(mask: int, rotations: tuple[tuple[int, ...], ...]) -> frozenset[int]:
    return frozenset(apply_perm(mask, rot) for rot in rotations)


def all_orbits(rotations: tuple[tuple[int, ...], ...]) -> tuple[frozenset[int], ...]:
    seen: set[int] = set()
    orbits: list[frozenset[int]] = []
    for mask in range(N_CELLS):
        if mask in seen:
            continue
        orbit = orbit_of(mask, rotations)
        seen.update(orbit)
        orbits.append(orbit)
    return tuple(sorted(orbits, key=lambda orb: (min(orb), len(orb))))


def plus_plus_plus_mask() -> int:
    # Occupied +x, +y, +z: bits 0, 2, 4.
    return (1 << 0) | (1 << 2) | (1 << 4)


def occupied_axes(mask: int) -> int:
    pairs = ((0, 1), (2, 3), (4, 5))
    return sum(1 for plus_bit, minus_bit in pairs if (mask >> plus_bit) & 1 or (mask >> minus_bit) & 1)


def is_one_per_axis_weight3(mask: int) -> bool:
    if mask.bit_count() != 3:
        return False
    pairs = ((0, 1), (2, 3), (4, 5))
    return all(((mask >> plus_bit) & 1) + ((mask >> minus_bit) & 1) == 1 for plus_bit, minus_bit in pairs)


def neighborhood_mask(site: Vec, locks: frozenset[Vec]) -> int:
    mask = 0
    for bit, ray in enumerate(RAYS):
        if occupancy(plus(site, ray), locks):
            mask |= 1 << bit
    return mask


def f_v3(mask: int, vertex3: frozenset[int]) -> int:
    return 1 if mask in vertex3 else 0


def f_l1(mask: int) -> int:
    # L1 form iff n≠0: at least one axis is unbalanced.
    for plus_bit, minus_bit in ((0, 1), (2, 3), (4, 5)):
        if ((mask >> plus_bit) & 1) != ((mask >> minus_bit) & 1):
            return 1
    return 0


def f_hamming(mask: int) -> int:
    return mask.bit_count() % 2


def ready_sites(locks: frozenset[Vec], predicate) -> frozenset[Vec]:
    return frozenset(
        site
        for site in PATCH
        if site not in locks and predicate(neighborhood_mask(site, locks)) == 1
    )


def step(locks: frozenset[Vec], predicate) -> frozenset[Vec]:
    return locks | ready_sites(locks, predicate)


def evolve_until_halt(
    seed: frozenset[Vec],
    predicate,
    max_ticks: int = 12,
) -> tuple[int, frozenset[Vec], list[frozenset[Vec]]]:
    hist = [seed]
    locks = seed
    for tick in range(1, max_ticks + 1):
        nxt = step(locks, predicate)
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


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    source = Path(__file__).read_text(encoding="utf-8")

    print("vertex3-orbit indicator dynamics on the two-cube")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print(
        "scope: twelve-vertex two-cube; 1-site seed; off-patch o=0; "
        "f_v3 = indicator of the complement-fixed vertex3 orbit"
    )
    print(
        "negative_scope: displayed, not adopted; not leftover-char static "
        "membership; not L1; f_L1 is n≠0, not Hamming parity"
    )

    expected_tuple = (
        "AUDIT_INPUT_PATHS = (\n"
        '    "docs/VERTEX3_ORBIT_INDICATOR_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ")"
    )
    checks.check(
        "audit-input-paths-static-literals",
        AUDIT_INPUT_PATHS
        == (
            "docs/VERTEX3_ORBIT_INDICATOR_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and expected_tuple in source
        and AUDIT_TIMEOUT_SEC == 120,
    )
    checks.check("audit-input-paths-exist", all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS))
    checks.check(
        "audit-input-paths-unique-relative",
        len(AUDIT_INPUT_PATHS) == len(set(AUDIT_INPUT_PATHS))
        and all(not Path(path).is_absolute() and ".." not in Path(path).parts for path in AUDIT_INPUT_PATHS),
    )
    checks.check("lattice-quote-present", "proper cubic rotations" in axiom)
    checks.check("record-form-quote-present", "Records form" in axiom)
    for token in FORBIDDEN_NOTE_SUBSTRINGS:
        checks.check(f"hygiene-avoids-{token!r}", token not in note)
    checks.check("note-has-no-runner-cache-path", "runner-cache" not in note)
    checks.check("note-has-no-citation-manifest", "citation_manifest" not in note)
    checks.check("patch-has-twelve-sites", len(PATCH) == 12)
    checks.check("seed-is-origin", SEED == (0, 0, 0) and SEED in PATCH)
    checks.check("off-patch-occupancy-is-zero", occupancy((3, 0, 0), frozenset({SEED})) == 0)

    rotations = proper_cube_ray_permutations()
    identity = tuple(range(6))
    checks.check(
        "rotation-group-order",
        len(rotations) == 24 and len(set(rotations)) == 24 and identity in rotations,
    )

    orbits = all_orbits(rotations)
    checks.check(
        "orbit-count",
        len(orbits) == 10 and sum(len(orbit) for orbit in orbits) == 64,
        f"N_orb={len(orbits)}",
    )

    vertex3 = orbit_of(plus_plus_plus_mask(), rotations)
    mixed3 = orbit_of((1 << 0) | (1 << 1) | (1 << 2), rotations)
    checks.check("vertex3-size-eight", len(vertex3) == 8)
    checks.check(
        "vertex3-is-one-per-axis",
        all(is_one_per_axis_weight3(mask) for mask in vertex3)
        and all(is_one_per_axis_weight3(mask) for mask in range(N_CELLS) if mask in vertex3)
        and occupied_axes(plus_plus_plus_mask()) == 3,
    )
    checks.check(
        "vertex3-complement-fixed",
        frozenset(complement(mask) for mask in vertex3) == vertex3,
    )
    checks.check("mixed3-is-distinct", mixed3 != vertex3 and len(mixed3) == 12)
    checks.check(
        "weight-1-not-in-vertex3",
        all(mask.bit_count() != 1 for mask in vertex3)
        and all(f_v3(1 << bit, vertex3) == 0 for bit in range(6)),
    )
    checks.check(
        "f-v3-exactly-the-orbit",
        all((f_v3(mask, vertex3) == 1) == (mask in vertex3) for mask in range(N_CELLS)),
    )

    def pred_v3(mask: int) -> int:
        return f_v3(mask, vertex3)

    seed_locks = frozenset({SEED})
    first_wave = ready_sites(seed_locks, pred_v3)
    halt_tick, locks, hist = evolve_until_halt(seed_locks, pred_v3, 12)
    post_halt = step(locks, pred_v3)
    one_tick = step(seed_locks, pred_v3)

    checks.check("theorem-1-first-wave-empty", first_wave == frozenset())
    checks.check("theorem-2-halt-is-zero-or-one", halt_tick in (0, 1), f"T={halt_tick}")
    checks.check("theorem-2-locks-are-seed-only", locks == seed_locks)
    checks.check("theorem-2-lock-count", len(locks) == 1, f"|locks|={len(locks)}")
    checks.check("theorem-2-halt-is-fixed-point", post_halt == locks)
    checks.check("theorem-2-one-tick-adds-nothing", one_tick == seed_locks)
    checks.check("theorem-3-does-not-fill", locks != PATCH and len(locks) != 12)
    checks.check("locks-monotone", all(hist[i] <= hist[i + 1] for i in range(len(hist) - 1)))

    hamming_wave = ready_sites(seed_locks, f_hamming)
    l1_wave = ready_sites(seed_locks, f_l1)
    l1_halt, l1_locks, _ = evolve_until_halt(seed_locks, f_l1, 12)
    axis_sites = frozenset({(1, 0, 0), (0, 1, 0), (0, 0, 1)})

    checks.check(
        "displayed-f-l1-is-unbalanced-axis-not-hamming",
        any(f_l1(mask) != f_hamming(mask) for mask in range(N_CELLS))
        and f_l1(1) == 1
        and f_hamming(1) == 1
        and f_l1(plus_plus_plus_mask()) == 1
        and f_hamming(plus_plus_plus_mask()) == 1
        and f_l1((1 << 0) | (1 << 1)) == 0
        and f_hamming((1 << 0) | (1 << 1)) == 0
        and f_l1((1 << 0) | (1 << 2)) == 1
        and f_hamming((1 << 0) | (1 << 2)) == 0,
    )
    checks.check(
        "hamming-first-wave-nonempty",
        hamming_wave == axis_sites and len(hamming_wave) == 3,
    )
    checks.check("l1-first-wave-nonempty", l1_wave == axis_sites)
    checks.check(
        "l1-displayed-fills-at-horizon-4",
        l1_halt == 4 and l1_locks == PATCH and len(l1_locks) == 12,
        f"L1 T={l1_halt} |locks|={len(l1_locks)}",
    )
    checks.check(
        "f-v3-distinct-from-l1-and-hamming",
        any(pred_v3(mask) != f_l1(mask) for mask in range(N_CELLS))
        and any(pred_v3(mask) != f_hamming(mask) for mask in range(N_CELLS))
        and pred_v3(1) == 0
        and f_l1(1) == 1
        and f_hamming(1) == 1,
    )

    claim_scope = (
        "The vertex3-orbit indicator has empty 1-site first wave on the "
        "twelve-vertex two-cube with off-patch o=0 and does not fill. "
        "Displayed, not adopted."
    )
    checks.check("claim-scope", claim_scope in note)
    checks.check("note-reports-empty-first-wave", "empty" in note and "first wave" in note)
    checks.check("note-reports-seed-only-locks", "|locks|" in note and "seed" in note)
    checks.check("note-reports-does-not-fill", "does not fill" in note)
    checks.check("note-displays-not-adopted", "Displayed, not adopted" in note)
    checks.check("note-not-leftover-char", "not leftover-char" in note)
    checks.check("note-authors-no-audit-verdict", "authors no audit verdict" in note)
    checks.check(
        "script-hygiene",
        "Does not adopt a member" in source and "cache_write: false" in source,
    )
    checks.check(
        "axiom-unedited",
        "### Lattice / Physical Locality" in axiom
        and "### Qubit / Site Possibility" in axiom
        and "### Admissibility / Local Constraint" in axiom
        and "### Record / Fixed Reality" in axiom
        and "f_v3" not in axiom
        and "vertex3" not in axiom,
    )

    print(f"halt_tick: {halt_tick}")
    print(f"lock_count: {len(locks)}")
    print(f"fills_patch: {locks == PATCH}")
    print(f"first_wave_size: {len(first_wave)}")
    print(f"hamming_first_wave_size: {len(hamming_wave)}")
    print(f"l1_halt_tick: {l1_halt}")
    print("per_element: 12 vertices")
    print("per_site: occupancy lock")
    print("per_mode: f_v3 vertex3-orbit indicator")
    print("per_block: first wave, halt, fill")
    print("lattice_wide: checked and not executed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
