#!/usr/bin/env python3
"""First |S|<=3 seed that splits the four Max(11)\\Max(1) F_cut extras.

F_cut is the cube-covariant class with f(empty)=f(full)=0 and f(c)=f(1-c).
Dynamics are occupancy-to-lock on the twelve-vertex two-cube with off-patch
occupancy 0. Coverage cov_k(f) is the number of unordered k-site seeds from
which f fills. Max(k) is the set of F_cut maps attaining the maximum of
cov_k. The four remaining-bit extras in Max(11) minus Max(1) are named, not
adopted. f_L1 is the unbalanced-axis predicate (some n_mu != 0), never
Hamming |c|_1 mod 2.
"""

from __future__ import annotations

from itertools import combinations, permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/F_CUT_MAX11_EXTRA_FIRST_SPLIT_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/F_CUT_MAX11_EXTRA_FIRST_SPLIT_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Direction = tuple[int, int, int]
Config = tuple[int, int, int, int, int, int]
Rotation = tuple[tuple[int, int, int], tuple[int, int, int]]
OrbitType = tuple[int, int, int]
Site = tuple[int, int, int]
Remaining = tuple[int, int, int, int, int]

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
ONE_SITE_SEEDS: tuple[frozenset[Site], ...] = tuple(
    frozenset(single) for single in combinations(TWO_CUBE, 1)
)
ELEVEN_SITE_SEEDS: tuple[frozenset[Site], ...] = tuple(
    frozenset(combo) for combo in combinations(TWO_CUBE, 11)
)
BOUNDED_SEEDS: tuple[tuple[Site, ...], ...] = tuple(
    combo for size in range(0, 4) for combo in combinations(TWO_CUBE, size)
)
REMAINING_ORDER: tuple[OrbitType, ...] = (
    (1, 0, 2),
    (0, 1, 2),
    (2, 0, 1),
    (3, 0, 0),
    (1, 1, 1),
)
REMAINING_LABELS: tuple[str, ...] = ("wt1", "opp2", "adj2", "vertex3", "mixed3")
L1_REMAINING: Remaining = (1, 0, 1, 1, 1)
NAMED_EXTRAS: tuple[Remaining, ...] = (
    (0, 0, 1, 1, 0),
    (0, 0, 1, 1, 1),
    (0, 1, 1, 1, 0),
    (0, 1, 1, 1, 1),
)
DISPLAYED_SEED: tuple[Site, ...] = ((0, 0, 0), (0, 1, 1), (2, 0, 0))
DISPLAYED_FILL_BITS: tuple[int, ...] = (0, 0, 1, 1)
FULL_MASK = (1 << 12) - 1


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


def rotate_vector(rotation: Rotation, vector: Direction) -> Direction:
    permutation, signs = rotation
    result = [0, 0, 0]
    for source_axis in range(3):
        result[permutation[source_axis]] = signs[source_axis] * vector[source_axis]
    return (result[0], result[1], result[2])


def rotate_config(config: Config, rotation: Rotation) -> Config:
    occupancy = {direction: config[index] for index, direction in enumerate(DIRECTIONS)}
    forward = {direction: rotate_vector(rotation, direction) for direction in DIRECTIONS}
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


def bits_from_predicate(
    predicate, orbit_types: tuple[OrbitType, ...], orbits: dict[OrbitType, frozenset[Config]]
) -> tuple[int, ...]:
    bits = []
    for orbit_type in orbit_types:
        sample = next(iter(orbits[orbit_type]))
        value = int(predicate(sample))
        if any(int(predicate(member)) != value for member in orbits[orbit_type]):
            raise RuntimeError("predicate is not cube-covariant")
        bits.append(value)
    return tuple(bits)


def remaining_bits_from_assignment(assignment: dict[OrbitType, int]) -> Remaining:
    return tuple(assignment[orbit_type] for orbit_type in REMAINING_ORDER)  # type: ignore[return-value]


def remaining_bits_from_full(
    bits: tuple[int, ...], orbit_types: tuple[OrbitType, ...]
) -> Remaining:
    assignment = dict(zip(orbit_types, bits, strict=True))
    return remaining_bits_from_assignment(assignment)


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


def f_cut_free_data(
    orbit_types: tuple[OrbitType, ...],
    empty_type: OrbitType,
    full_type: OrbitType,
) -> tuple[list[tuple[OrbitType, OrbitType]], list[OrbitType]]:
    used: set[OrbitType] = set()
    pairs: list[tuple[OrbitType, OrbitType]] = []
    fixed: list[OrbitType] = []
    for orbit_type in orbit_types:
        if orbit_type in used:
            continue
        image = complement_type(orbit_type)
        if image == orbit_type:
            fixed.append(orbit_type)
        else:
            pair = tuple(sorted((orbit_type, image)))
            pairs.append((pair[0], pair[1]))
            used.add(orbit_type)
            used.add(image)
    free_pairs = [pair for pair in pairs if empty_type not in pair and full_type not in pair]
    free_fixed = [orbit_type for orbit_type in fixed if orbit_type not in (empty_type, full_type)]
    return free_pairs, free_fixed


def enumerate_f_cut(
    orbit_types: tuple[OrbitType, ...],
    empty_type: OrbitType,
    full_type: OrbitType,
) -> list[tuple[dict[OrbitType, int], Remaining]]:
    free_pairs, free_fixed = f_cut_free_data(orbit_types, empty_type, full_type)
    n_free = len(free_pairs) + len(free_fixed)
    members: list[tuple[dict[OrbitType, int], Remaining]] = []
    for mask in range(1 << n_free):
        assignment = {empty_type: 0, full_type: 0}
        for rank, pair in enumerate(free_pairs):
            value = (mask >> rank) & 1
            assignment[pair[0]] = value
            assignment[pair[1]] = value
        for rank, orbit_type in enumerate(free_fixed):
            assignment[orbit_type] = (mask >> (len(free_pairs) + rank)) & 1
        remaining = remaining_bits_from_assignment(assignment)
        members.append((assignment, remaining))
    return members


def neighbor_index_table() -> tuple[tuple[int, ...], ...]:
    site_index = {site: index for index, site in enumerate(TWO_CUBE)}
    rows = []
    for site in TWO_CUBE:
        row = []
        for direction in DIRECTIONS:
            neighbor = (
                site[0] + direction[0],
                site[1] + direction[1],
                site[2] + direction[2],
            )
            row.append(site_index.get(neighbor, -1))
        rows.append(tuple(row))
    return tuple(rows)


NEIGHBOR_INDEX: tuple[tuple[int, ...], ...] = neighbor_index_table()
SITE_INDEX: dict[Site, int] = {site: index for index, site in enumerate(TWO_CUBE)}


def seed_mask(seed: frozenset[Site] | tuple[Site, ...]) -> int:
    return sum(1 << SITE_INDEX[site] for site in seed)


def predicate_table(
    assignment: dict[OrbitType, int], type_of: dict[Config, OrbitType]
) -> tuple[int, ...]:
    table = [0] * 64
    for bits in range(64):
        config: Config = (
            bits & 1,
            (bits >> 1) & 1,
            (bits >> 2) & 1,
            (bits >> 3) & 1,
            (bits >> 4) & 1,
            (bits >> 5) & 1,
        )
        table[bits] = assignment[type_of[config]]
    return tuple(table)


def evolve(locked: int, table: tuple[int, ...]) -> int:
    nxt = locked
    for site in range(12):
        if (locked >> site) & 1:
            continue
        occupancy = 0
        for direction_index, neighbor in enumerate(NEIGHBOR_INDEX[site]):
            if neighbor >= 0 and (locked >> neighbor) & 1:
                occupancy |= 1 << direction_index
        if table[occupancy]:
            nxt |= 1 << site
    return nxt


def fills(seed: int, table: tuple[int, ...]) -> bool:
    locked = seed
    for _tick in range(13):
        nxt = evolve(locked, table)
        if nxt == locked:
            return locked == FULL_MASK
        locked = nxt
    return False


def coverage(table: tuple[int, ...], seeds: tuple[frozenset[Site], ...]) -> int:
    return sum(1 for seed in seeds if fills(seed_mask(seed), table))


def fill_bits_on_seed(
    seed: tuple[Site, ...], extra_tables: tuple[tuple[int, ...], ...]
) -> tuple[int, ...]:
    mask = seed_mask(seed)
    return tuple(int(fills(mask, table)) for table in extra_tables)


def first_split_seed(
    extra_tables: tuple[tuple[int, ...], ...]
) -> tuple[tuple[Site, ...], tuple[int, ...]]:
    for seed in BOUNDED_SEEDS:
        bits = fill_bits_on_seed(seed, extra_tables)
        if len(set(bits)) > 1:
            return seed, bits
    raise RuntimeError("no |S|<=3 seed splits the four extras")


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


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    self_source = Path(__file__).read_text(encoding="utf-8")
    note_flat = normalize(note)

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
    free_pairs, free_fixed = f_cut_free_data(orbit_types, empty_type, full_type)
    n_free = len(free_pairs) + len(free_fixed)
    n_cut = 1 << n_free
    type_of = {config: orbit_type for orbit_type, group in orbits.items() for config in group}

    members = enumerate_f_cut(orbit_types, empty_type, full_type)
    tables = {
        remaining: predicate_table(assignment, type_of) for assignment, remaining in members
    }
    cov1 = {remaining: coverage(table, ONE_SITE_SEEDS) for remaining, table in tables.items()}
    cov11 = {remaining: coverage(table, ELEVEN_SITE_SEEDS) for remaining, table in tables.items()}
    m1 = max(cov1.values())
    m11 = max(cov11.values())
    max1 = tuple(sorted(remaining for remaining, value in cov1.items() if value == m1))
    max11 = tuple(sorted(remaining for remaining, value in cov11.items() if value == m11))
    extras_computed = tuple(remaining for remaining in max11 if remaining not in max1)

    extra_tables = tuple(tables[remaining] for remaining in NAMED_EXTRAS)
    split_seed, split_bits = first_split_seed(extra_tables)
    n_split_bounded = sum(
        1 for seed in BOUNDED_SEEDS if len(set(fill_bits_on_seed(seed, extra_tables))) > 1
    )
    two_site_bits = [
        fill_bits_on_seed(seed, extra_tables)
        for seed in BOUNDED_SEEDS
        if len(seed) == 2
    ]

    l1_bits = bits_from_predicate(f_L1, orbit_types, orbits)
    ham_bits = bits_from_predicate(f_hamming, orbit_types, orbits)
    l1_remaining = remaining_bits_from_full(l1_bits, orbit_types)

    print(f"n_rotations={len(ROTATIONS)}")
    print(f"n_orbits={len(orbit_types)}")
    print("orbit_types_and_sizes=" + ",".join(f"{t}:{orbit_sizes[t]}" for t in orbit_types))
    print(f"remaining_labels={REMAINING_LABELS}")
    print(f"N_free={n_free}")
    print(f"|F_cut|={n_cut}")
    print(f"n_one_site_seeds={len(ONE_SITE_SEEDS)}")
    print(f"n_eleven_site_seeds={len(ELEVEN_SITE_SEEDS)}")
    print(f"n_bounded_seeds={len(BOUNDED_SEEDS)}")
    print(f"m1={m1}")
    print(f"N_max1={len(max1)}")
    print(f"Max1={list(max1)}")
    print(f"m11={m11}")
    print(f"N_max11={len(max11)}")
    print(f"Max11={list(max11)}")
    print(f"named_extras={list(NAMED_EXTRAS)}")
    print(f"extras_computed={list(extras_computed)}")
    print(f"extra_cov1={[cov1[remaining] for remaining in NAMED_EXTRAS]}")
    print(f"extra_cov11={[cov11[remaining] for remaining in NAMED_EXTRAS]}")
    print(f"split_seed={split_seed}")
    print(f"split_fill_bits={split_bits}")
    print(f"n_split_bounded={n_split_bounded}")
    print(f"f_L1_remaining={l1_remaining}")
    print(f"f_L1_bits={l1_bits}")
    print(f"f_hamming_bits={ham_bits}")

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required note-plus-axiom string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/F_CUT_MAX11_EXTRA_FIRST_SPLIT_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and "AUDIT_INPUT_PATHS = (\n"
        '    "docs/F_CUT_MAX11_EXTRA_FIRST_SPLIT_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ")" in self_source,
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
    expected_sizes = {
        (0, 0, 3): 1,
        (0, 1, 2): 3,
        (0, 2, 1): 3,
        (0, 3, 0): 1,
        (1, 0, 2): 6,
        (1, 1, 1): 12,
        (1, 2, 0): 6,
        (2, 0, 1): 12,
        (2, 1, 0): 12,
        (3, 0, 0): 8,
    }
    checks.check(
        "thm1-orbit-sizes",
        "orbit sizes are the axis-type class sizes",
        orbit_sizes == expected_sizes,
    )
    checks.check(
        "thm1-f-cut-cardinality",
        "F_cut has five free bits and size 32",
        n_free == 5
        and n_cut == 32
        and len(members) == 32
        and len(free_pairs) == 3
        and len(free_fixed) == 2
        and empty_type == (0, 0, 3)
        and full_type == (0, 3, 0)
        and REMAINING_ORDER == ((1, 0, 2), (0, 1, 2), (2, 0, 1), (3, 0, 0), (1, 1, 1)),
    )
    checks.check(
        "thm1-f-L1-is-unbalanced-axis",
        "f_L1 is 1 iff some axis has c_+ != c_-",
        all(
            f_L1(config) == int(axis_type(config)[0] >= 1)
            for config in product((0, 1), repeat=6)
        )
        and l1_remaining == L1_REMAINING,
    )
    checks.check(
        "thm1-f-L1-not-hamming",
        "f_L1 is not Hamming |c|_1 mod 2",
        l1_bits != ham_bits
        and any(f_L1(config) != f_hamming(config) for config in product((0, 1), repeat=6))
        and "sum(config) % 2"
        not in self_source.split("def f_L1", 1)[1].split("def f_hamming", 1)[0],
    )
    checks.check(
        "thm1-two-cube-and-seed-counts",
        "the two-cube has twelve vertices, C(12,1)=12 one-site seeds, C(12,11)=12 eleven-site seeds",
        len(TWO_CUBE) == 12
        and len(set(TWO_CUBE)) == 12
        and len(ONE_SITE_SEEDS) == 12
        and len(set(ONE_SITE_SEEDS)) == 12
        and len(ELEVEN_SITE_SEEDS) == 12
        and len(set(ELEVEN_SITE_SEEDS)) == 12
        and len(BOUNDED_SEEDS) == 1 + 12 + 66 + 220
        and all(seed <= set(TWO_CUBE) and len(seed) == 1 for seed in ONE_SITE_SEEDS)
        and all(seed <= set(TWO_CUBE) and len(seed) == 11 for seed in ELEVEN_SITE_SEEDS),
    )
    checks.check(
        "thm1-max11-contains-four-extras",
        "all four named extras lie in Max(11) and attain cov11=12",
        m11 == 12
        and len(max11) == 8
        and all(remaining in max11 for remaining in NAMED_EXTRAS)
        and all(cov11[remaining] == 12 for remaining in NAMED_EXTRAS)
        and extras_computed == NAMED_EXTRAS,
    )
    checks.check(
        "thm1-max1-excludes-four-extras",
        "none of the four named extras lie in Max(1); each has cov1=0",
        m1 == 12
        and len(max1) == 4
        and all(remaining not in max1 for remaining in NAMED_EXTRAS)
        and all(cov1[remaining] == 0 for remaining in NAMED_EXTRAS)
        and L1_REMAINING in max1
        and L1_REMAINING not in NAMED_EXTRAS,
    )
    checks.check(
        "thm2-first-split-seed",
        "lex-first |S|<=3 seed that splits the four extras is the displayed 3-site seed",
        split_seed == DISPLAYED_SEED
        and len(split_seed) == 3
        and len(set(split_bits)) > 1
        and all(
            len(set(fill_bits_on_seed(seed, extra_tables))) == 1
            for seed in BOUNDED_SEEDS
            if seed < DISPLAYED_SEED or len(seed) < 3
        ),
    )
    checks.check(
        "thm2-no-smaller-split",
        "no empty, 1-site, or 2-site seed splits the four extras",
        all(bits == (0, 0, 0, 0) for bits in two_site_bits)
        and len(two_site_bits) == 66
        and fill_bits_on_seed((), extra_tables) == (0, 0, 0, 0)
        and all(
            fill_bits_on_seed((site,), extra_tables) == (0, 0, 0, 0) for site in TWO_CUBE
        ),
    )
    checks.check(
        "thm3-displayed-fill-bits",
        "on the displayed seed the four fill-bits are (0, 0, 1, 1)",
        split_bits == DISPLAYED_FILL_BITS
        and split_bits == fill_bits_on_seed(DISPLAYED_SEED, extra_tables)
        and n_split_bounded == 20,
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
        "bounded theorem, displayed-not-adopted first split, and machine status",
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
        "note-reports-split",
        "the note reports Max(11), Max(1), the four extras, the first seed, and the fill-bits",
        "(wt1, opp2, adj2, vertex3, mixed3)" in note
        and "(0, 0, 1, 1, 0)" in note
        and "(0, 0, 1, 1, 1)" in note
        and "(0, 1, 1, 1, 0)" in note
        and "(0, 1, 1, 1, 1)" in note
        and "((0, 0, 0), (0, 1, 1), (2, 0, 0))" in note
        and "(0, 0, 1, 1)" in note
        and "m11 = 12" in note
        and "N_max11 = 8" in note
        and "m1 = 12" in note
        and "N_max1 = 4" in note,
    )
    checks.check(
        "no-axiom-edit",
        "the theorem proposes no axiom change",
        "no axiom or approved primitive is added" in note
        and "hypothetical_axiom_status" in note
        and "Do not write the seed into Admissibility" in note,
    )
    checks.check(
        "off-patch-zero",
        "off-patch occupancy is the explicit 0 default, not a blank-block",
        "off-patch occupancy `0`" in note and "blank-block is a different rule" in note,
    )
    checks.check(
        "not-leftover-6476",
        "the residual is the first split seed, not leftover-character of listing Max(11) minus Max(1)",
        "Not leftover-character of #6476" in note
        and "named the set" in note
        and "new uniqueness of the set" in note_flat,
    )
    checks.check(
        "claim-scope-split",
        "claim_scope reports the lex-first |S|<=3 split of the four extras",
        "On the two-cube with off-patch o=0" in note
        and "lex-first seed of size at most 3" in note
        and "Max(11) minus Max(1)" in note
        and "do not all fill or all miss" in note
        and "Displayed, not adopted" in note,
    )

    print("per_element: checked exactly — each of the 64 neighbor 6-tuples is assigned its axis-type orbit")
    print("per_site: checked exactly — each of the twelve two-cube vertices uses the same six-direction stencil")
    print("per_mode: checked exactly — every F_cut map is scored on all 1-site and 11-site seeds")
    print("per_block: checked exactly — the four extras and the lex-first |S|<=3 split seed are enumerated")
    print("lattice_wide: checked and not executed — no Z^3-wide formation law or physical Admissibility selector is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
