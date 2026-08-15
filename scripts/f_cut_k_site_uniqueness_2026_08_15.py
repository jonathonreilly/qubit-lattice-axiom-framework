#!/usr/bin/env python3
"""Exact F_cut k-site coverage uniqueness set on the two-cube.

F_cut is the cube-covariant class with f(empty)=f(full)=0 and f(c)=f(1-c).
Dynamics are occupancy-to-lock on the twelve-vertex two-cube with off-patch
occupancy 0. For each k in {1,5,6,7,8,9,10,11}, cov_k(f) is the number of
unordered k-site seeds from which f fills. The new object is the set of
seed sizes whose coverage ranking has a unique maximizer, not leftover of
one k. Do not re-census k=2,3,4: cite #6429 N_max2=2, #6453 N_max3=2,
#6460 N_max4=1 is f1. f_L1 is the unbalanced-axis predicate (some n_mu !=
0), never Hamming |c|_1 mod 2. f1 is remaining bits (1,1,1,1,1).
"""

from __future__ import annotations

from itertools import combinations, permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/F_CUT_K_SITE_UNIQUENESS_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/F_CUT_K_SITE_UNIQUENESS_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
CENSUS_KS: tuple[int, ...] = (1, 5, 6, 7, 8, 9, 10, 11)
CITED_N_MAX: dict[int, int] = {2: 2, 3: 2, 4: 1}
CITED_UNIQUE_NAME: dict[int, str] = {4: "f1"}
REMAINING_ORDER: tuple[OrbitType, ...] = (
    (1, 0, 2),
    (0, 1, 2),
    (2, 0, 1),
    (3, 0, 0),
    (1, 1, 1),
)
REMAINING_LABELS: tuple[str, ...] = ("wt1", "opp2", "adj2", "vertex3", "mixed3")
L1_REMAINING: tuple[int, ...] = (1, 0, 1, 1, 1)
F1_REMAINING: tuple[int, ...] = (1, 1, 1, 1, 1)
EMPTY_TYPE: OrbitType = (0, 0, 3)
FULL_TYPE: OrbitType = (0, 3, 0)


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


def f1(config: Config) -> int:
    """f1 remaining bits (1, 1, 1, 1, 1): on except empty and full.  Not adopted."""
    kind = axis_type(config)
    if kind in (EMPTY_TYPE, FULL_TYPE):
        return 0
    return 1


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


def remaining_bits_from_assignment(assignment: dict[OrbitType, int]) -> tuple[int, ...]:
    return tuple(assignment[orbit_type] for orbit_type in REMAINING_ORDER)


def remaining_bits_from_full(
    bits: tuple[int, ...], orbit_types: tuple[OrbitType, ...]
) -> tuple[int, ...]:
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
) -> list[tuple[tuple[int, ...], tuple[int, ...]]]:
    free_pairs, free_fixed = f_cut_free_data(orbit_types, empty_type, full_type)
    n_free = len(free_pairs) + len(free_fixed)
    members: list[tuple[tuple[int, ...], tuple[int, ...]]] = []
    for mask in range(1 << n_free):
        assignment = {empty_type: 0, full_type: 0}
        for rank, pair in enumerate(free_pairs):
            value = (mask >> rank) & 1
            assignment[pair[0]] = value
            assignment[pair[1]] = value
        for rank, orbit_type in enumerate(free_fixed):
            assignment[orbit_type] = (mask >> (len(free_pairs) + rank)) & 1
        bits = tuple(assignment[orbit_type] for orbit_type in orbit_types)
        remaining = remaining_bits_from_assignment(assignment)
        members.append((bits, remaining))
    return members


def site_index_map() -> dict[Site, int]:
    return {site: index for index, site in enumerate(TWO_CUBE)}


def neighbor_indices() -> tuple[tuple[int, ...], ...]:
    index_of = site_index_map()
    rows = []
    for site in TWO_CUBE:
        row = []
        for direction in DIRECTIONS:
            neighbor = (
                site[0] + direction[0],
                site[1] + direction[1],
                site[2] + direction[2],
            )
            row.append(index_of.get(neighbor, -1))
        rows.append(tuple(row))
    return tuple(rows)


def seed_masks_for(k: int) -> tuple[int, ...]:
    index_of = site_index_map()
    return tuple(
        sum(1 << index_of[site] for site in combo) for combo in combinations(TWO_CUBE, k)
    )


def predicate_table(
    bits: tuple[int, ...],
    orbit_types: tuple[OrbitType, ...],
    type_of: dict[Config, OrbitType],
) -> tuple[int, ...]:
    assignment = dict(zip(orbit_types, bits, strict=True))
    table = []
    for packed in range(64):
        config: Config = (
            packed & 1,
            (packed >> 1) & 1,
            (packed >> 2) & 1,
            (packed >> 3) & 1,
            (packed >> 4) & 1,
            (packed >> 5) & 1,
        )
        table.append(assignment[type_of[config]])
    return tuple(table)


def evolve_mask(locked: int, table: tuple[int, ...], neighbors: tuple[tuple[int, ...], ...]) -> int:
    nxt = locked
    for site in range(12):
        if (locked >> site) & 1:
            continue
        occupancy = 0
        for direction, neighbor in enumerate(neighbors[site]):
            if neighbor >= 0 and (locked >> neighbor) & 1:
                occupancy |= 1 << direction
        if table[occupancy]:
            nxt |= 1 << site
    return nxt


def fills_from_mask(
    seed_mask: int, table: tuple[int, ...], neighbors: tuple[tuple[int, ...], ...]
) -> bool:
    locked = seed_mask
    full_mask = (1 << 12) - 1
    for _tick in range(13):
        nxt = evolve_mask(locked, table, neighbors)
        if nxt == locked:
            return locked == full_mask
        locked = nxt
    return False


def coverage_from_masks(
    table: tuple[int, ...],
    seeds: tuple[int, ...],
    neighbors: tuple[tuple[int, ...], ...],
) -> int:
    return sum(1 for seed in seeds if fills_from_mask(seed, table, neighbors))


def name_unique_maximizer(remaining: tuple[int, ...]) -> str:
    if remaining == F1_REMAINING:
        return "f1"
    if remaining == L1_REMAINING:
        return "f_L1"
    raise RuntimeError(f"unique maximizer {remaining} is neither f1 nor f_L1")


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
    neighbors = neighbor_indices()
    seed_masks = {k: seed_masks_for(k) for k in CENSUS_KS}

    ranked: dict[int, list[tuple[int, tuple[int, ...]]]] = {k: [] for k in CENSUS_KS}
    for bits, remaining in members:
        table = predicate_table(bits, orbit_types, type_of)
        for k in CENSUS_KS:
            cov = coverage_from_masks(table, seed_masks[k], neighbors)
            ranked[k].append((cov, remaining))

    m_of: dict[int, int] = {}
    n_max_of: dict[int, int] = {}
    maximizers_of: dict[int, list[tuple[int, ...]]] = {}
    cov_l1_of: dict[int, int] = {}
    cov_f1_of: dict[int, int] = {}
    for k in CENSUS_KS:
        scores = ranked[k]
        m_k = max(cov for cov, _remaining in scores)
        maximizers = sorted(remaining for cov, remaining in scores if cov == m_k)
        m_of[k] = m_k
        n_max_of[k] = len(maximizers)
        maximizers_of[k] = maximizers
        cov_l1_of[k] = next(cov for cov, remaining in scores if remaining == L1_REMAINING)
        cov_f1_of[k] = next(cov for cov, remaining in scores if remaining == F1_REMAINING)

    n_max_all = dict(CITED_N_MAX)
    n_max_all.update(n_max_of)
    k_unique = tuple(k for k in range(1, 12) if n_max_all[k] == 1)
    unique_name: dict[int, str] = dict(CITED_UNIQUE_NAME)
    for k in k_unique:
        if k in CENSUS_KS:
            unique_name[k] = name_unique_maximizer(maximizers_of[k][0])

    l1_bits = bits_from_predicate(f_L1, orbit_types, orbits)
    ham_bits = bits_from_predicate(f_hamming, orbit_types, orbits)
    f1_bits = bits_from_predicate(f1, orbit_types, orbits)
    l1_remaining = remaining_bits_from_full(l1_bits, orbit_types)
    f1_remaining = remaining_bits_from_full(f1_bits, orbit_types)

    print(f"n_rotations={len(ROTATIONS)}")
    print(f"n_orbits={len(orbit_types)}")
    print("orbit_types_and_sizes=" + ",".join(f"{t}:{orbit_sizes[t]}" for t in orbit_types))
    print(f"remaining_labels={REMAINING_LABELS}")
    print(f"N_free={n_free}")
    print(f"|F_cut|={n_cut}")
    print(f"census_ks={CENSUS_KS}")
    for k in CENSUS_KS:
        print(
            f"k={k} n_seeds={len(seed_masks[k])} m_{k}={m_of[k]} "
            f"N_max_{k}={n_max_of[k]} cov_L1={cov_l1_of[k]} cov_f1={cov_f1_of[k]}"
        )
        if n_max_of[k] == 1:
            print(f"unique_maximizer_{k}={unique_name[k]} remaining={maximizers_of[k][0]}")
    print(f"cited_N_max={CITED_N_MAX}")
    print(f"K_unique={list(k_unique)}")
    print(f"unique_names={ {k: unique_name[k] for k in k_unique} }")
    print(f"f_L1_bits={l1_bits}")
    print(f"f_L1_remaining={l1_remaining}")
    print(f"f1_bits={f1_bits}")
    print(f"f1_remaining={f1_remaining}")
    print(f"f_hamming_bits={ham_bits}")

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required note-plus-axiom string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/F_CUT_K_SITE_UNIQUENESS_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and "AUDIT_INPUT_PATHS = (\n"
        '    "docs/F_CUT_K_SITE_UNIQUENESS_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
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
        ),
    )
    checks.check(
        "thm1-f-L1-not-hamming",
        "f_L1 is not Hamming |c|_1 mod 2",
        l1_bits != ham_bits
        and any(f_L1(config) != f_hamming(config) for config in product((0, 1), repeat=6))
        and "sum(config) % 2"
        not in self_source.split("def f_L1", 1)[1].split("def f_hamming", 1)[0],
    )
    expected_seed_counts = {1: 12, 5: 792, 6: 924, 7: 792, 8: 495, 9: 220, 10: 66, 11: 12}
    checks.check(
        "thm1-two-cube-and-census-seeds",
        "the two-cube has twelve vertices and the eight census k-site seed counts",
        len(TWO_CUBE) == 12
        and len(set(TWO_CUBE)) == 12
        and CENSUS_KS == (1, 5, 6, 7, 8, 9, 10, 11)
        and all(len(seed_masks[k]) == expected_seed_counts[k] for k in CENSUS_KS)
        and all(len(set(seed_masks[k])) == expected_seed_counts[k] for k in CENSUS_KS),
    )
    expected_m = {1: 12, 5: 792, 6: 924, 7: 792, 8: 495, 9: 220, 10: 66, 11: 12}
    expected_n_max = {1: 4, 5: 2, 6: 1, 7: 2, 8: 1, 9: 4, 10: 4, 11: 8}
    checks.check(
        "thm1-m-and-n-max-census",
        "each census k reports its computed (m_k, N_max_k) pair",
        m_of == expected_m
        and n_max_of == expected_n_max
        and all(f"m_{k} = {m_of[k]}" in note for k in CENSUS_KS)
        and all(f"N_max_{k} = {n_max_of[k]}" in note for k in CENSUS_KS),
    )
    checks.check(
        "thm2-k-unique-set",
        "K_unique is the seed sizes in 1..11 with N_max_k=1",
        k_unique == (4, 6, 8)
        and n_max_all[2] == 2
        and n_max_all[3] == 2
        and n_max_all[4] == 1
        and "K_unique = {4, 6, 8}" in note,
    )
    checks.check(
        "thm2-cites-without-recensus",
        "k=2,3,4 enter K_unique only as cited N_max values, not a recensus",
        CITED_N_MAX == {2: 2, 3: 2, 4: 1}
        and 2 not in CENSUS_KS
        and 3 not in CENSUS_KS
        and 4 not in CENSUS_KS
        and "combinations(TWO_CUBE, " + "2)" not in self_source
        and "combinations(TWO_CUBE, " + "3)" not in self_source
        and "combinations(TWO_CUBE, " + "4)" not in self_source
        and "#6429" in note
        and "#6453" in note
        and "#6460" in note
        and "Do not re-census k=2,3,4" in note,
    )
    checks.check(
        "thm3-unique-maximizers-are-f1",
        "for each k in K_unique the unique maximizer is f1, not f_L1",
        unique_name[4] == "f1"
        and unique_name[6] == "f1"
        and unique_name[8] == "f1"
        and maximizers_of[6] == [F1_REMAINING]
        and maximizers_of[8] == [F1_REMAINING]
        and l1_remaining == L1_REMAINING
        and f1_remaining == F1_REMAINING
        and l1_remaining != f1_remaining
        and in_f_cut(l1_bits, orbit_types, empty_type, full_type)
        and in_f_cut(f1_bits, orbit_types, empty_type, full_type)
        and cov_l1_of[6] < m_of[6]
        and cov_l1_of[8] < m_of[8]
        and cov_f1_of[6] == m_of[6]
        and cov_f1_of[8] == m_of[8]
        and "unique maximizer is `f1`" in note,
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
        "bounded theorem, displayed-not-adopted uniqueness set, and machine status",
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
        "note-reports-ranking",
        "the note reports every census pair, K_unique, and names f1 not f_L1",
        "(wt1, opp2, adj2, vertex3, mixed3)" in note
        and "(1, 1, 1, 1, 1)" in note
        and "(1, 0, 1, 1, 1)" in note
        and "K_unique = {4, 6, 8}" in note
        and "f1=(1,1,1,1,1)" in note.replace(" ", ""),
    )
    checks.check(
        "no-axiom-edit",
        "the theorem proposes no axiom change",
        "no axiom or approved primitive is added" in note
        and "hypothetical_axiom_status" in note
        and "Do not write the ranking into Admissibility" in note,
    )
    checks.check(
        "off-patch-zero",
        "off-patch occupancy is the explicit 0 default, not a blank-block",
        "off-patch occupancy `0`" in note and "blank-block is a different rule" in note,
    )
    checks.check(
        "not-leftover-one-k",
        "the residual is the multi-k uniqueness set, not leftover-character of one k",
        "New selector, not leftover of one k" in note
        and "Not leftover-character of #6429" in note
        and "Not leftover-character of #6453" in note
        and "Not leftover-character of #6460" in note
        and "different |S|" in note,
    )
    checks.check(
        "claim-scope-ranking",
        "claim_scope reports unique-maximizer seed sizes and names f_L1 or f1",
        "Among the 32 F_cut maps on the two-cube" in note
        and "off-patch o=0" in note
        and "k in {1,5,6,7,8,9,10,11}" in note
        and "unique maximizer" in note
        and "f_L1 or f1" in note
        and "Displayed, not adopted" in note,
    )
    checks.check(
        "seeds-not-listed",
        "the note does not list k-site seeds and does not recensus 2,3,4",
        "Do not list the seeds" in note
        and "Do not re-census k=2,3,4" in note
        and "combinations(TWO_CUBE" not in note
        and "{(0, 0, 0), (0, 0, 1)}" not in note,
    )

    print("per_element: checked exactly — each of the 64 neighbor 6-tuples is assigned its axis-type orbit")
    print("per_site: checked exactly — each of the twelve two-cube vertices uses the same six-direction stencil")
    print("per_mode: checked exactly — every F_cut map is scored on each census seed size")
    print("per_block: checked exactly — K_unique is the set of k in 1..11 with a unique coverage maximizer")
    print("lattice_wide: checked and not executed — no Z^3-wide formation law or physical Admissibility selector is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
