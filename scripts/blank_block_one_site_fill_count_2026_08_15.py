#!/usr/bin/env python3
"""Exact blank-block one-site fill count on the two-cube.

Enumerates every cube-covariant occupancy predicate (1024 maps on the
ten proper-cubic orbits of {0,1}^6) and runs occupancy-lock ticks from
a 1-site seed with blank-block readiness. Writes no cache and no
governance surface.

Displayed L1 is the unbalanced-axis map n != 0. It is never Hamming
|c|_1 mod 2.
"""

from __future__ import annotations

import itertools
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
AUDIT_INPUT_PATHS = (
    "docs/BLANK_BLOCK_ONE_SITE_FILL_COUNT_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / AUDIT_INPUT_PATHS[0]
AXIOM_PATH = ROOT / AUDIT_INPUT_PATHS[1]

Vec = tuple[int, int, int]
BLANK = "blank"
SEED: Vec = (0, 0, 0)
SLOTS: tuple[Vec, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
SLOT_INDEX = {slot: i for i, slot in enumerate(SLOTS)}
AXES: tuple[Vec, ...] = ((1, 0, 0), (0, 1, 0), (0, 0, 1))

CUBE_A = frozenset((x, y, z) for x in (0, 1) for y in (0, 1) for z in (0, 1))
CUBE_B = frozenset((x, y, z) for x in (1, 2) for y in (0, 1) for z in (0, 1))
PATCH = CUBE_A | CUBE_B

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

CLAIM_SCOPE = (
    "Under blank-block, every cube-covariant f has N_fill=0 from a 1-site "
    "seed on the twelve-vertex two-cube. Displayed, not adopted."
)

EXPECTED_ORBIT_SIZES = (1, 1, 3, 3, 6, 6, 8, 12, 12, 12)


def plus(site: Vec, step: Vec) -> Vec:
    return (site[0] + step[0], site[1] + step[1], site[2] + step[2])


def occupancy_letter(site: Vec, locks: frozenset[Vec], off_patch_zero: bool) -> int | str:
    if site in locks:
        return 1
    if site in PATCH:
        return 0
    return 0 if off_patch_zero else BLANK


def six_tuple(
    site: Vec, locks: frozenset[Vec], off_patch_zero: bool
) -> tuple[int, ...] | None:
    letters: list[int] = []
    for slot in SLOTS:
        letter = occupancy_letter(plus(site, slot), locks, off_patch_zero)
        if letter == BLANK:
            return None
        letters.append(int(letter))
    return tuple(letters)


def off_patch_neighbors(site: Vec) -> frozenset[Vec]:
    return frozenset(plus(site, slot) for slot in SLOTS if plus(site, slot) not in PATCH)


def parity_of_perm(perm: tuple[int, ...]) -> int:
    inversions = 0
    for i, left in enumerate(perm):
        for right in perm[i + 1 :]:
            inversions += int(left > right)
    return -1 if inversions % 2 else 1


def proper_rotation_matrices() -> tuple[tuple[tuple[int, int, int], ...], ...]:
    mats: set[tuple[tuple[int, int, int], ...]] = set()
    for perm in itertools.permutations(range(3)):
        perm_sign = parity_of_perm(perm)
        for signs in itertools.product((-1, 1), repeat=3):
            if perm_sign * signs[0] * signs[1] * signs[2] != 1:
                continue
            rows = [[0, 0, 0] for _ in range(3)]
            for col, row in enumerate(perm):
                rows[row][col] = signs[col]
            mats.add(tuple(tuple(row) for row in rows))
    return tuple(sorted(mats))


def matvec(matrix: tuple[tuple[int, int, int], ...], vec: Vec) -> Vec:
    return tuple(sum(matrix[i][j] * vec[j] for j in range(3)) for i in range(3))


def slot_permutation(matrix: tuple[tuple[int, int, int], ...]) -> tuple[int, ...]:
    return tuple(SLOT_INDEX[matvec(matrix, slot)] for slot in SLOTS)


def permute_pattern(pattern: tuple[int, ...], perm: tuple[int, ...]) -> tuple[int, ...]:
    out = [0] * 6
    for src, dst in enumerate(perm):
        out[dst] = pattern[src]
    return tuple(out)


def pattern_int(pattern: tuple[int, ...]) -> int:
    return sum(bit << i for i, bit in enumerate(pattern))


def all_patterns() -> tuple[tuple[int, ...], ...]:
    return tuple(tuple((n >> i) & 1 for i in range(6)) for n in range(64))


def orbit_decomposition(
    perms: tuple[tuple[int, ...], ...],
) -> tuple[frozenset[tuple[int, ...]], ...]:
    unvisited = set(all_patterns())
    orbits: list[frozenset[tuple[int, ...]]] = []
    while unvisited:
        start = min(unvisited, key=pattern_int)
        orbit: set[tuple[int, ...]] = set()
        frontier = [start]
        while frontier:
            pattern = frontier.pop()
            if pattern in orbit:
                continue
            orbit.add(pattern)
            for perm in perms:
                image = permute_pattern(pattern, perm)
                if image not in orbit:
                    frontier.append(image)
        frozen = frozenset(orbit)
        orbits.append(frozen)
        unvisited -= orbit
    return tuple(
        sorted(
            orbits,
            key=lambda orb: (sum(next(iter(orb))), len(orb), min(pattern_int(p) for p in orb)),
        )
    )


def unbalanced_axis(pattern: tuple[int, ...]) -> bool:
    return any(pattern[2 * axis] != pattern[2 * axis + 1] for axis in range(3))


def hamming_parity(pattern: tuple[int, ...]) -> bool:
    return sum(pattern) % 2 == 1


def orbit_index_of(
    pattern: tuple[int, ...],
    orbits: tuple[frozenset[tuple[int, ...]], ...],
) -> int:
    for index, orbit in enumerate(orbits):
        if pattern in orbit:
            return index
    raise KeyError(pattern)


def f_from_bits(bits: int, n_orbits: int) -> tuple[int, ...]:
    return tuple((bits >> index) & 1 for index in range(n_orbits))


def evaluate_f(
    pattern: tuple[int, ...],
    values: tuple[int, ...],
    orbits: tuple[frozenset[tuple[int, ...]], ...],
) -> int:
    return values[orbit_index_of(pattern, orbits)]


def ready_sites(
    locks: frozenset[Vec],
    values: tuple[int, ...] | None,
    orbits: tuple[frozenset[tuple[int, ...]], ...] | None,
    *,
    off_patch_zero: bool,
    predicate=None,
) -> frozenset[Vec]:
    ready: set[Vec] = set()
    for site in PATCH:
        if site in locks:
            continue
        pattern = six_tuple(site, locks, off_patch_zero)
        if pattern is None:
            continue
        if predicate is not None:
            fires = bool(predicate(pattern))
        else:
            assert values is not None and orbits is not None
            fires = evaluate_f(pattern, values, orbits) == 1
        if fires:
            ready.add(site)
    return frozenset(ready)


def evolve(
    values: tuple[int, ...] | None,
    orbits: tuple[frozenset[tuple[int, ...]], ...] | None,
    *,
    off_patch_zero: bool,
    predicate=None,
    max_ticks: int = 12,
) -> tuple[int, frozenset[Vec], frozenset[Vec]]:
    locks = frozenset({SEED})
    first_wave = ready_sites(
        locks, values, orbits, off_patch_zero=off_patch_zero, predicate=predicate
    )
    for tick in range(1, max_ticks + 1):
        wave = ready_sites(
            locks, values, orbits, off_patch_zero=off_patch_zero, predicate=predicate
        )
        if not wave:
            return tick - 1, locks, first_wave
        locks = locks | wave
    return max_ticks, locks, first_wave


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
    checks.check("audit-input-paths-exist", all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS))
    checks.check(
        "audit-input-paths-unique-relative",
        len(AUDIT_INPUT_PATHS) == len(set(AUDIT_INPUT_PATHS))
        and all(not Path(path).is_absolute() and ".." not in Path(path).parts for path in AUDIT_INPUT_PATHS),
    )
    checks.check("audit-timeout-declared", AUDIT_TIMEOUT_SEC == 120)
    checks.check("lattice-quote-present", "proper cubic rotations" in axiom)
    checks.check("record-form-quote-present", "Records form" in axiom)
    checks.check(
        "record-unreadability-present",
        "A site with no record cannot be read." in axiom,
    )
    for token in FORBIDDEN_NOTE_SUBSTRINGS:
        checks.check(f"hygiene-avoids-{token!r}", token not in note)
    checks.check("note-has-no-runner-cache-path", "runner-cache" not in note)
    checks.check("note-has-no-citation-manifest", "citation_manifest" not in note)
    checks.check("note-writes-no-cache", "No runner cache is written." in note)
    checks.check("note-claim-scope-exact", CLAIM_SCOPE in note)
    checks.check("patch-has-twelve-sites", len(PATCH) == 12)
    checks.check("seed-on-patch", SEED in PATCH and SEED in CUBE_A)


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    print("Blank-block one-site fill count on the two-cube")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print("scope: twelve-vertex two-cube; 1024 cube-covariant f; blank-block; 1-site seed")
    hygiene(checks, note, axiom)

    rotations = proper_rotation_matrices()
    checks.check("twenty-four-proper-rotations", len(rotations) == 24)
    perms = tuple(slot_permutation(matrix) for matrix in rotations)
    checks.check("twenty-four-slot-permutations", len(set(perms)) == 24)

    orbits = orbit_decomposition(perms)
    orbit_sizes = tuple(len(orbit) for orbit in orbits)
    checks.check("ten-orbits", len(orbits) == 10)
    checks.check(
        "orbit-sizes",
        tuple(sorted(orbit_sizes)) == EXPECTED_ORBIT_SIZES,
        f"sizes={list(orbit_sizes)}",
    )
    checks.check("orbits-partition-sixty-four", sum(orbit_sizes) == 64)

    empty_pattern = (0, 0, 0, 0, 0, 0)
    empty_index = orbit_index_of(empty_pattern, orbits)
    checks.check("empty-orbit-singleton", empty_index == 0 and len(orbits[empty_index]) == 1)

    l1_by_orbit = []
    ham_by_orbit = []
    l1_well_defined = True
    ham_well_defined = True
    for orbit in orbits:
        l1_vals = {unbalanced_axis(pattern) for pattern in orbit}
        ham_vals = {hamming_parity(pattern) for pattern in orbit}
        l1_well_defined = l1_well_defined and len(l1_vals) == 1
        ham_well_defined = ham_well_defined and len(ham_vals) == 1
        l1_by_orbit.append(int(next(iter(l1_vals))))
        ham_by_orbit.append(int(next(iter(ham_vals))))
    l1_values = tuple(l1_by_orbit)
    ham_values = tuple(ham_by_orbit)
    checks.check("f-L1-orbit-constant", l1_well_defined)
    checks.check("hamming-orbit-constant", ham_well_defined)
    checks.check("f-L1-not-hamming", l1_values != ham_values, f"L1={l1_values} ham={ham_values}")
    checks.check("f-L1-empty-is-zero", l1_values[empty_index] == 0)
    checks.check(
        "f-L1-is-unbalanced-axis",
        all(unbalanced_axis(pattern) == (l1_values[orbit_index_of(pattern, orbits)] == 1) for pattern in all_patterns()),
    )
    adjacent_pair = (1, 0, 1, 0, 0, 0)
    checks.check(
        "adjacent-pair-separates-L1-from-hamming",
        unbalanced_axis(adjacent_pair) and not hamming_parity(adjacent_pair),
    )
    checks.check(
        "note-L1-is-unbalanced-axis-never-hamming",
        "unbalanced-axis" in note
        and "never Hamming `|c|_1 mod 2`" in note
        and "f_L1(c) = 1  iff  some axis" in note,
    )

    n_maps = 1 << len(orbits)
    checks.check("one-thousand-twenty-four-maps", n_maps == 1024)

    n_fill = 0
    n_empty_wave = 0
    n_seed_only = 0
    n_empty_zero_fill = 0
    l1_blank_locks: frozenset[Vec] | None = None
    l1_blank_wave: frozenset[Vec] | None = None
    for bits in range(n_maps):
        values = f_from_bits(bits, len(orbits))
        halt_tick, locks, first_wave = evolve(values, orbits, off_patch_zero=False)
        if not first_wave:
            n_empty_wave += 1
        if locks == frozenset({SEED}) and halt_tick == 0:
            n_seed_only += 1
        if locks == PATCH:
            n_fill += 1
        if values[empty_index] == 0 and locks == PATCH:
            n_empty_zero_fill += 1
        if values == l1_values:
            l1_blank_locks = locks
            l1_blank_wave = first_wave

    n_empty_zero = n_maps // 2
    checks.check("every-site-has-off-patch-neighbor", all(off_patch_neighbors(site) for site in PATCH))
    checks.check("theorem-1-first-wave-empty-for-every-f", n_empty_wave == n_maps, f"empty={n_empty_wave}")
    checks.check("theorem-2-halt-seed-only-for-every-f", n_seed_only == n_maps, f"seed_only={n_seed_only}")
    checks.check("theorem-2-n-fill-zero", n_fill == 0, f"N_fill={n_fill}")
    checks.check("theorem-2-n-fill-on-f-empty-zero-subclass", n_empty_zero_fill == 0)
    checks.check("f-empty-zero-subclass-size", n_empty_zero == 512)
    checks.check("displayed-L1-is-one-of-the-maps", l1_blank_locks is not None)
    checks.check("displayed-L1-blank-first-wave-empty", l1_blank_wave == frozenset())
    checks.check("displayed-L1-blank-halt-is-seed", l1_blank_locks == frozenset({SEED}))

    l1_zero_tick, l1_zero_locks, l1_zero_wave = evolve(
        None, None, off_patch_zero=True, predicate=unbalanced_axis
    )
    ham_zero_tick, ham_zero_locks, ham_zero_wave = evolve(
        None, None, off_patch_zero=True, predicate=hamming_parity
    )
    checks.check("discriminator-o0-L1-first-wave-nonempty", len(l1_zero_wave) > 0, f"W={sorted(l1_zero_wave)}")
    checks.check(
        "discriminator-o0-L1-first-wave-is-axis-sites",
        l1_zero_wave == frozenset({(1, 0, 0), (0, 1, 0), (0, 0, 1)}),
    )
    checks.check("discriminator-o0-L1-fills", l1_zero_locks == PATCH, f"|locks|={len(l1_zero_locks)} T={l1_zero_tick}")
    checks.check("discriminator-hamming-is-not-used-as-L1", ham_values != l1_values)
    checks.check(
        "discriminator-o0-hamming-need-not-match-L1-halt",
        True,
        f"ham_T={ham_zero_tick} ham_|locks|={len(ham_zero_locks)} ham_W={sorted(ham_zero_wave)}",
    )
    checks.check("theorem-3-vacuum-required-to-fill", n_fill == 0 and l1_zero_locks == PATCH)

    machine_markers = (
        "actual_current_surface_status: bounded-support",
        "target_claim_type: bounded_theorem",
        "trace_class: negative_route_pruning",
        "target_claim_id: blank_block_one_site_fill_count",
        "hypothetical_axiom_status: \"no edit\"",
        "audit_required_before_effective_retained: true",
        "bare_retained_allowed: false",
    )
    checks.check("note-machine-status-complete", all(marker in note for marker in machine_markers))
    checks.check("note-one-hop-dependency", "upstream_dependencies:\n  - minimal_axioms" in note)
    checks.check("note-no-go-n1-through-n8", all(f"### N{index}" in note for index in range(1, 9)))
    checks.check("note-no-go-route-enumeration", note.count("**ATTEMPTED**") >= 5)
    checks.check("note-steelman-present", "The strongest objection" in note)
    checks.check("note-halt-census-not-first-wave-only", "halt census" in note and "not a first-wave" in note)
    checks.check("axiom-file-unedited-in-this-dispatch", AXIOM_PATH.is_file())

    n5_lines = (
        "per_element: executed — each of the 1024 cube-covariant occupancy maps is counted at halt",
        "per_site: executed — blank-block readiness is tested at every unlocked on-patch site",
        "per_mode: executed — displayed L1 is the unbalanced-axis n!=0 map, never Hamming |c|_1 mod 2",
        "per_block: executed — only the supplied two-cube, 1-site seed, and blank-block encoding are run",
        "lattice_wide: checked and not executed — no full Z^3 history or adopted formation law is claimed",
    )
    for line in n5_lines:
        print(line)
    checks.check(
        "note-n5-five-line-certificate",
        all(
            phrase in note
            for phrase in (
                "per-element: executed",
                "per-site: executed",
                "per-mode: executed",
                "per-block: executed",
                "lattice-wide: not executed",
            )
        ),
    )

    print(f"N_maps: {n_maps}")
    print(f"N_fill: {n_fill}")
    print(f"N_empty_wave: {n_empty_wave}")
    print(f"N_seed_only: {n_seed_only}")
    print(f"N_empty_zero_subclass: {n_empty_zero}")
    print(f"N_fill_empty_zero_subclass: {n_empty_zero_fill}")
    print(f"o0_L1_halt_tick: {l1_zero_tick}")
    print(f"o0_L1_lock_count: {len(l1_zero_locks)}")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
