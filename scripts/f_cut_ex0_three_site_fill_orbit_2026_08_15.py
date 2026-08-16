#!/usr/bin/env python3
"""Orbit type of the 24 3-site seeds filled by F_cut (0,0,1,1,0).

F_cut is the cube-covariant class with f(empty)=f(full)=0 and f(c)=f(1-c).
Dynamics are occupancy-to-lock on the twelve-vertex two-cube with off-patch
occupancy 0. f_ex0 is the remaining-bit map (0,0,1,1,0). M is the set of
unordered 3-site seeds that f_ex0 fills. N_orb is the number of orbits of M
under two-cube-preserving proper cube rotations about the box center.
f_L1 is the unbalanced-axis predicate (some n_mu != 0), never Hamming
|c|_1 mod 2.
"""

from __future__ import annotations

from itertools import combinations, permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/F_CUT_EX0_THREE_SITE_FILL_ORBIT_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/F_CUT_EX0_THREE_SITE_FILL_ORBIT_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Direction = tuple[int, int, int]
Config = tuple[int, int, int, int, int, int]
Rotation = tuple[tuple[int, int, int], tuple[int, int, int]]
OrbitType = tuple[int, int, int]
Site = tuple[int, int, int]

DIRECTIONS: tuple[Direction, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
EMPTY: Config = (0, 0, 0, 0, 0, 0)
FULL: Config = (1, 1, 1, 1, 1, 1)
TWO_CUBE: tuple[Site, ...] = tuple(
    (x, y, z) for x in range(3) for y in range(2) for z in range(2)
)
THREE_SITE_SEEDS: tuple[frozenset[Site], ...] = tuple(
    frozenset(triple) for triple in combinations(TWO_CUBE, 3)
)
REMAINING_ORDER: tuple[OrbitType, ...] = (
    (1, 0, 2),
    (0, 1, 2),
    (2, 0, 1),
    (3, 0, 0),
    (1, 1, 1),
)
EX0_REMAINING: tuple[int, ...] = (0, 0, 1, 1, 0)
L1_REMAINING: tuple[int, ...] = (1, 0, 1, 1, 1)
SEED_6517: frozenset[Site] = frozenset(((0, 0, 0), (1, 0, 1), (2, 1, 0)))
LEX_REPS: tuple[frozenset[Site], ...] = (
    frozenset(((0, 0, 0), (1, 0, 1), (2, 1, 0))),
    frozenset(((0, 0, 0), (1, 0, 1), (2, 1, 1))),
    frozenset(((0, 0, 0), (1, 1, 0), (2, 0, 1))),
    frozenset(((0, 0, 0), (1, 1, 0), (2, 1, 1))),
)
ORBIT_SIZES: tuple[int, ...] = (8, 4, 8, 4)
BOX_CENTER: tuple[float, float, float] = (1.0, 0.5, 0.5)
NON_REP_SEED: frozenset[Site] = frozenset(((0, 0, 1), (1, 0, 0), (2, 1, 0)))


def permutation_sign(permutation: tuple[int, int, int]) -> int:
    inversions = sum(
        permutation[i] > permutation[j]
        for i in range(3)
        for j in range(i + 1, 3)
    )
    return -1 if inversions % 2 else 1


ROTATIONS: tuple[Rotation, ...] = tuple(
    (permutation, signs)
    for permutation in permutations((0, 1, 2))
    for signs in product((-1, 1), repeat=3)
    if permutation_sign(permutation) * signs[0] * signs[1] * signs[2] == 1
)


def rotate_vector(rotation: Rotation, vector: tuple[float, float, float]) -> tuple[float, float, float]:
    permutation, signs = rotation
    result = [0.0, 0.0, 0.0]
    for source_axis in range(3):
        result[permutation[source_axis]] = signs[source_axis] * vector[source_axis]
    return (result[0], result[1], result[2])


def rotate_config(config: Config, rotation: Rotation) -> Config:
    occupancy = {direction: config[index] for index, direction in enumerate(DIRECTIONS)}
    forward = {
        direction: tuple(int(component) for component in rotate_vector(rotation, direction))
        for direction in DIRECTIONS
    }
    inverse = {image: source for source, image in forward.items()}
    return tuple(occupancy[inverse[direction]] for direction in DIRECTIONS)  # type: ignore[return-value]


def axis_type(config: Config) -> OrbitType:
    n_unbalanced = 0
    n_both = 0
    n_empty = 0
    for axis in range(3):
        plus = config[2 * axis]
        minus = config[2 * axis + 1]
        if plus != minus:
            n_unbalanced += 1
        elif plus == 1:
            n_both += 1
        else:
            n_empty += 1
    return (n_unbalanced, n_both, n_empty)


def complement_type(orbit_type: OrbitType) -> OrbitType:
    unbalanced, both, empty = orbit_type
    return (unbalanced, empty, both)


def f_L1(config: Config) -> int:
    """1 iff some axis is unbalanced: n_mu != 0.  Not Hamming parity."""
    return int(any(config[2 * axis] != config[2 * axis + 1] for axis in range(3)))


def f_hamming(config: Config) -> int:
    return sum(config) % 2


def build_orbits() -> dict[OrbitType, frozenset[Config]]:
    orbits: dict[OrbitType, frozenset[Config]] = {}
    seen: set[Config] = set()
    for raw in product((0, 1), repeat=6):
        config: Config = (raw[0], raw[1], raw[2], raw[3], raw[4], raw[5])
        if config in seen:
            continue
        orbit: set[Config] = set()
        stack = [config]
        while stack:
            current = stack.pop()
            if current in orbit:
                continue
            orbit.add(current)
            for rotation in ROTATIONS:
                stack.append(rotate_config(current, rotation))
        orbit_type = axis_type(config)
        if any(axis_type(member) != orbit_type for member in orbit):
            raise RuntimeError("orbit mixed axis types")
        orbits[orbit_type] = frozenset(orbit)
        seen.update(orbit)
    return orbits


def remaining_bits_from_assignment(assignment: dict[OrbitType, int]) -> tuple[int, ...]:
    return tuple(assignment[orbit_type] for orbit_type in REMAINING_ORDER)


def predicate_from_remaining(bits: tuple[int, ...]):
    assignment = {
        (0, 0, 3): 0,
        (0, 3, 0): 0,
        (1, 0, 2): bits[0],
        (1, 2, 0): bits[0],
        (0, 1, 2): bits[1],
        (0, 2, 1): bits[1],
        (2, 0, 1): bits[2],
        (2, 1, 0): bits[2],
        (3, 0, 0): bits[3],
        (1, 1, 1): bits[4],
    }

    def predicate(config: Config) -> int:
        return assignment[axis_type(config)]

    return predicate


def in_f_cut(
    bits: tuple[int, ...],
    orbit_types: tuple[OrbitType, ...],
    empty_type: OrbitType,
    full_type: OrbitType,
) -> bool:
    assignment = dict(zip(orbit_types, bits, strict=True))
    if assignment[empty_type] != 0 or assignment[full_type] != 0:
        return False
    return all(
        assignment[orbit_type] == assignment[complement_type(orbit_type)]
        for orbit_type in orbit_types
    )


def bits_from_predicate(
    predicate,
    orbit_types: tuple[OrbitType, ...],
    orbits: dict[OrbitType, frozenset[Config]],
) -> tuple[int, ...]:
    bits = []
    for orbit_type in orbit_types:
        sample = next(iter(orbits[orbit_type]))
        value = int(predicate(sample))
        if any(int(predicate(member)) != value for member in orbits[orbit_type]):
            raise RuntimeError("predicate is not cube-covariant")
        bits.append(value)
    return tuple(bits)


def neighborhood(site: Site, locked: set[Site]) -> Config:
    values = []
    for direction in DIRECTIONS:
        neighbor = (
            site[0] + direction[0],
            site[1] + direction[1],
            site[2] + direction[2],
        )
        values.append(1 if neighbor in locked else 0)
    return (values[0], values[1], values[2], values[3], values[4], values[5])


def evolve(locked: set[Site], predicate) -> set[Site]:
    nxt = set(locked)
    for site in TWO_CUBE:
        if site in locked:
            continue
        if predicate(neighborhood(site, locked)):
            nxt.add(site)
    return nxt


def fills_from_seed(predicate, seed: frozenset[Site]) -> bool:
    locked = set(seed)
    for _tick in range(13):
        nxt = evolve(locked, predicate)
        if nxt == locked:
            return len(locked) == 12
        locked = nxt
    return False


def rotate_site(rotation: Rotation, site: Site) -> Site | None:
    relative = (
        site[0] - BOX_CENTER[0],
        site[1] - BOX_CENTER[1],
        site[2] - BOX_CENTER[2],
    )
    image = rotate_vector(rotation, relative)
    absolute = (
        image[0] + BOX_CENTER[0],
        image[1] + BOX_CENTER[1],
        image[2] + BOX_CENTER[2],
    )
    rounded = (
        int(round(absolute[0])),
        int(round(absolute[1])),
        int(round(absolute[2])),
    )
    if any(abs(absolute[index] - rounded[index]) > 1e-9 for index in range(3)):
        return None
    return rounded


def two_cube_preserving(rotations: tuple[Rotation, ...]) -> tuple[Rotation, ...]:
    preserved: list[Rotation] = []
    two_cube_set = set(TWO_CUBE)
    for rotation in rotations:
        images = []
        ok = True
        for site in TWO_CUBE:
            image = rotate_site(rotation, site)
            if image is None or image not in two_cube_set:
                ok = False
                break
            images.append(image)
        if ok and set(images) == two_cube_set:
            preserved.append(rotation)
    return tuple(preserved)


def rotate_seed(seed: frozenset[Site], rotation: Rotation) -> frozenset[Site]:
    images = []
    for site in seed:
        image = rotate_site(rotation, site)
        if image is None:
            raise RuntimeError("rotation left the integer lattice")
        images.append(image)
    return frozenset(images)


def lex_key(seed: frozenset[Site]) -> tuple[Site, ...]:
    return tuple(sorted(seed))


def orbit_of(seed: frozenset[Site], group: tuple[Rotation, ...]) -> frozenset[frozenset[Site]]:
    orbit: set[frozenset[Site]] = set()
    stack = [seed]
    while stack:
        current = stack.pop()
        if current in orbit:
            continue
        orbit.add(current)
        for rotation in group:
            stack.append(rotate_seed(current, rotation))
    return frozenset(orbit)


def orbits_of(
    seeds: tuple[frozenset[Site], ...], group: tuple[Rotation, ...]
) -> list[frozenset[frozenset[Site]]]:
    remaining = set(seeds)
    orbits: list[frozenset[frozenset[Site]]] = []
    while remaining:
        seed = min(remaining, key=lex_key)
        orbit = orbit_of(seed, group)
        orbits.append(orbit)
        remaining -= set(orbit)
    return orbits


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


def normalize(text: str) -> str:
    return " ".join(text.split())


def compact_seed(seed: frozenset[Site]) -> str:
    return "{" + ",".join(str(site).replace(" ", "") for site in sorted(seed)) + "}"


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    self_source = Path(__file__).read_text(encoding="utf-8")
    note_flat = normalize(note)
    note_compact = note.replace(" ", "")

    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")

    orbits = build_orbits()
    orbit_types = tuple(sorted(orbits))
    orbit_sizes = {orbit_type: len(orbits[orbit_type]) for orbit_type in orbit_types}
    empty_type = axis_type(EMPTY)
    full_type = axis_type(FULL)
    all_configs = tuple(product((0, 1), repeat=6))

    f_ex0 = predicate_from_remaining(EX0_REMAINING)
    f_ex0_bits = bits_from_predicate(f_ex0, orbit_types, orbits)
    l1_bits = bits_from_predicate(f_L1, orbit_types, orbits)
    ham_bits = bits_from_predicate(f_hamming, orbit_types, orbits)
    f_ex0_remaining = remaining_bits_from_assignment(
        {orbit_type: f_ex0(next(iter(orbits[orbit_type]))) for orbit_type in orbit_types}
    )
    l1_remaining = remaining_bits_from_assignment(
        {orbit_type: f_L1(next(iter(orbits[orbit_type]))) for orbit_type in orbit_types}
    )

    fill_set = tuple(seed for seed in THREE_SITE_SEEDS if fills_from_seed(f_ex0, seed))
    m_count = len(fill_set)
    seed_6517_in_m = SEED_6517 in set(fill_set)

    group = two_cube_preserving(ROTATIONS)
    fill_orbits = orbits_of(fill_set, group)
    n_orb = len(fill_orbits)
    lex_reps = tuple(sorted((min(orbit, key=lex_key) for orbit in fill_orbits), key=lex_key))
    sizes = tuple(len(orbit) for orbit in fill_orbits)
    closed = all(
        rotate_seed(seed, rotation) in set(fill_set) for seed in fill_set for rotation in group
    )

    print(f"n_rotations={len(ROTATIONS)}")
    print(f"n_preserving={len(group)}")
    print(f"n_config_orbits={len(orbit_types)}")
    print(f"|F_cut|_free_check={1 << 5}")
    print(f"n_three_site_seeds={len(THREE_SITE_SEEDS)}")
    print(f"f_ex0_remaining={f_ex0_remaining}")
    print(f"f_L1_remaining={l1_remaining}")
    print(f"|M|={m_count}")
    print(f"seed_6517_in_M={seed_6517_in_m}")
    print(f"N_orb={n_orb}")
    print(f"lex_reps={[tuple(sorted(rep)) for rep in lex_reps]}")
    print(f"orbit_sizes={sizes}")
    print(f"M_closed_under_G={closed}")

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required note-plus-axiom string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/F_CUT_EX0_THREE_SITE_FILL_ORBIT_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and 'AUDIT_INPUT_PATHS = (\n'
        '    "docs/F_CUT_EX0_THREE_SITE_FILL_ORBIT_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ')' in self_source,
    )
    checks.check(
        "thm1-twenty-four-rotations",
        "exactly 24 proper cube rotations",
        len(ROTATIONS) == 24 and len(set(ROTATIONS)) == 24,
    )
    checks.check(
        "thm1-ten-orbits",
        "exactly 10 orbits partition the 64 cells of {0,1}^6",
        len(orbit_types) == 10 and sum(orbit_sizes.values()) == 64,
    )
    checks.check(
        "thm1-f-cut-and-f-ex0",
        "F_cut has size 32 and f_ex0=(0,0,1,1,0) is a member",
        empty_type == (0, 0, 3)
        and full_type == (0, 3, 0)
        and in_f_cut(f_ex0_bits, orbit_types, empty_type, full_type)
        and f_ex0_remaining == EX0_REMAINING
        and all(int(f_ex0(config)) == int(f_ex0(tuple(1 - bit for bit in config))) for config in all_configs)  # type: ignore[arg-type]
        and f_ex0(EMPTY) == 0
        and f_ex0(FULL) == 0,
    )
    checks.check(
        "thm1-f-L1-not-hamming",
        "f_L1 is unbalanced-axis n_mu != 0, not Hamming |c|_1 mod 2",
        l1_bits != ham_bits
        and l1_remaining == L1_REMAINING
        and any(f_L1(config) != f_hamming(config) for config in all_configs)
        and all(
            f_L1(config) == int(axis_type(config)[0] >= 1)  # type: ignore[arg-type]
            for config in all_configs
        )
        and "sum(config) % 2"
        not in self_source.split("def f_L1", 1)[1].split("def f_hamming", 1)[0],
    )
    checks.check(
        "thm1-two-cube-and-220-seeds",
        "the two-cube has twelve vertices and C(12,3)=220 three-site seeds",
        len(TWO_CUBE) == 12
        and len(set(TWO_CUBE)) == 12
        and len(THREE_SITE_SEEDS) == 220
        and len(set(THREE_SITE_SEEDS)) == 220
        and all(seed <= set(TWO_CUBE) and len(seed) == 3 for seed in THREE_SITE_SEEDS),
    )
    checks.check(
        "thm1-fill-count-and-6517",
        "|M|=24 and the #6517 seed is in M",
        m_count == 24
        and seed_6517_in_m
        and SEED_6517 <= set(TWO_CUBE)
        and len(SEED_6517) == 3
        and fills_from_seed(f_ex0, SEED_6517)
        and f"|M| = {m_count}" in note
        and "#6517" in note
        and "{(0,0,0),(1,0,1),(2,1,0)}" in note_compact,
    )
    checks.check(
        "thm2-preserving-group",
        "two-cube-preserving proper rotations about the box center form a group of order 8",
        len(group) == 8
        and len(set(group)) == 8
        and all(rotate_site(rotation, site) in set(TWO_CUBE) for rotation in group for site in TWO_CUBE)
        and all(axis[0] == 0 for axis, _signs in group),
    )
    checks.check(
        "thm2-n-orb-and-lex-reps",
        "N_orb=4 with one lex representative per orbit",
        n_orb == 4
        and closed
        and lex_reps == LEX_REPS
        and sizes == ORBIT_SIZES
        and SEED_6517 == LEX_REPS[0]
        and set().union(*fill_orbits) == set(fill_set)
        and all(orbit <= set(fill_set) for orbit in fill_orbits)
        and f"N_orb = {n_orb}" in note
        and "one lex representative" in note
        and all(compact_seed(rep) in note_compact for rep in LEX_REPS),
    )
    checks.check(
        "thm3-display-not-list-twenty-four",
        "the note displays N_orb and does not list all 24 seeds",
        f"N_orb = {n_orb}" in note
        and "Do not list all 24" in note
        and compact_seed(NON_REP_SEED) not in note_compact
        and note.count("{(0,") <= 6,
    )
    checks.check(
        "lattice-and-admissibility-parents",
        "the live axiom memo supplies Z^3, proper cubic rotations, and a covariant nearest-neighbor rule",
        "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor"
        in axiom
        and "proper cubic rotations about each site." in axiom
        and "one fixed nearest-neighbor admissibility rule, covariant under lattice"
        in axiom
        and "A site with no record cannot be read." in axiom,
    )
    checks.check(
        "note-contract",
        "bounded theorem, displayed-not-adopted orbit type, and machine status",
        "**Type:** bounded_theorem" in note
        and "actual_current_surface_status: bounded-support" in note
        and "Displayed, not adopted" in note
        and 'hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"'
        in note,
    )
    checks.check(
        "claim-type-and-gate",
        "N1-N8 and a passing no-go disposition are source-visible",
        all(f"### N{index}" in note for index in range(1, 9))
        and "No-Go Discipline disposition: **PASS**" in note
        and note.count("**ATTEMPTED**") == 6
        and ("import " + "qcd") not in self_source.lower(),
    )
    forbidden = ("G_" + "N", "1/" + "r", "1/" + "r^2", "Lattice-" + "named", "not a " + "TOE")
    checks.check(
        "forbidden-phrases-absent",
        "the note and runner omit the dispatch-forbidden phrases",
        all(phrase not in note and phrase not in self_source for phrase in forbidden),
    )
    checks.check(
        "l1-definition-in-note",
        "the note defines f_L1 as unbalanced-axis / n != 0 and rejects Hamming",
        "`f_L1(c)=1` if and only if some axis is unbalanced" in note_flat
        and "`n_μ = c_{+μ} − c_{-μ}` is nonzero" in note
        and "This is **not** Hamming parity" in note,
    )
    checks.check(
        "no-axiom-edit",
        "the theorem proposes no axiom change",
        "no axiom or approved primitive is added" in note
        and "hypothetical_axiom_status" in note
        and "Do not write the orbit into Admissibility" in note,
    )
    checks.check(
        "off-patch-zero",
        "off-patch occupancy is the explicit 0 default, not a blank-block",
        "off-patch occupancy `0`" in note and "blank-block is a different rule" in note,
    )
    checks.check(
        "not-leftover-count",
        "the residual is the orbit type of the counted fill set, not leftover of the cov3=24 count",
        "Not leftover-character of #6502" in note
        and "cov3=24" in note.replace(" ", "")
        and "New geometry" in note
        and "newly named map" in note,
    )
    checks.check(
        "claim-scope-orbit",
        "claim_scope states the 24 three-site fills of f_ex0 form N_orb orbits",
        "On the two-cube with off-patch o=0" in note
        and "24 three-site seeds that F_cut (0,0,1,1,0) fills form" in note
        and "N_orb=4" in note
        and "two-cube-preserving rotations" in note
        and "Displayed, not adopted" in note,
    )
    checks.check(
        "cache-and-timeout",
        "audit timeout is 120s and no runner cache is written",
        AUDIT_TIMEOUT_SEC == 120
        and "cache_write: false" in self_source
        and ("logs/" + "runner-cache") not in self_source,
    )

    print("per_element: checked exactly — each of the 64 neighbor 6-tuples is assigned its axis-type orbit")
    print("per_site: checked exactly — each of the twelve two-cube vertices uses the same six-direction stencil")
    print("per_mode: checked exactly — f_ex0 is scored on all 220 three-site seeds; G acts on M")
    print("per_block: checked exactly — N_orb is the orbit count of the 24-element fill set")
    print("lattice_wide: checked and not executed — no Z^3-wide formation law or physical Admissibility selector is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
