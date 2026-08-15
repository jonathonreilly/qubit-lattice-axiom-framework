#!/usr/bin/env python3
"""1-site halt of the k=4 F_cut map (1,1,1,0,1).

On the twelve-vertex two-cube with seed (0,0,0) and off-patch occupancy 0,
f is the F_cut remaining-bit tuple (wt1, opp2, adj2, vertex3, mixed3)=(1,1,1,0,1).
It fills the four long-axis 2-site seeds (k=4) and has cov1=8.  Report T,
lock history, and compare to the sibling (1,1,1,0,0) and to f_L1.  f_L1 is
the unbalanced-axis predicate (some n_mu != 0), never Hamming |c|_1 mod 2.
The history is displayed, not adopted, and is not leftover-character of
the #6445 sibling history.
"""

from __future__ import annotations

from itertools import combinations, permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
AUDIT_INPUT_PATHS = (
    "docs/F_CUT_K4_V31_ONE_SITE_HALT_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
NOTE_PATH = ROOT / AUDIT_INPUT_PATHS[0]
AXIOM_PATH = ROOT / AUDIT_INPUT_PATHS[1]

Direction = tuple[int, int, int]
Config = tuple[int, int, int, int, int, int]
Rotation = tuple[tuple[int, int, int], tuple[int, int, int]]
OrbitType = tuple[int, int, int]
Site = tuple[int, int, int]
BitTuple = tuple[int, int, int, int, int]

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
SEED: Site = (0, 0, 0)
TWO_SITE_SEEDS: tuple[frozenset[Site], ...] = tuple(
    frozenset(pair) for pair in combinations(TWO_CUBE, 2)
)
ONE_SITE_SEEDS: tuple[frozenset[Site], ...] = tuple(
    frozenset((site,)) for site in TWO_CUBE
)
LONG_AXIS_SEEDS: tuple[frozenset[Site], ...] = tuple(
    frozenset(((0, y, z), (2, y, z))) for y in (0, 1) for z in (0, 1)
)

WT1: OrbitType = (1, 0, 2)
OPP2: OrbitType = (0, 1, 2)
ADJ2: OrbitType = (2, 0, 1)
VERTEX3: OrbitType = (3, 0, 0)
MIXED3: OrbitType = (1, 1, 1)
DISPLAYED_BITS: BitTuple = (1, 1, 1, 0, 1)
SIBLING_BITS: BitTuple = (1, 1, 1, 0, 0)
L1_BITS: BitTuple = (1, 0, 1, 1, 1)
MAXIMIZER_BITS: tuple[BitTuple, ...] = ((1, 1, 1, 1, 0), (1, 1, 1, 1, 1))
K4_PREFIX: tuple[int, int, int] = (1, 1, 1)
ORBIT_PAIR_SIZE = {
    WT1: 12,
    OPP2: 6,
    ADJ2: 24,
    VERTEX3: 8,
    MIXED3: 12,
}


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
        orbit_kind = axis_type(config)
        if any(axis_type(member) != orbit_kind for member in orbit):
            raise RuntimeError("orbit mixed axis types")
        orbits[orbit_kind] = frozenset(orbit)
        seen.update(orbit)
    return orbits


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


def run_predicate(
    predicate, seed: frozenset[Site] | set[Site]
) -> tuple[int, int, tuple[int, ...]]:
    locked = set(seed)
    history = [len(locked)]
    halt_tick = 0
    for tick in range(13):
        nxt = evolve(locked, predicate)
        if nxt == locked:
            halt_tick = tick
            break
        locked = nxt
        history.append(len(locked))
    else:
        halt_tick = 13
    return len(locked), halt_tick, tuple(history)


def fills_from_seed(predicate, seed: frozenset[Site]) -> bool:
    n_locks, _halt, _history = run_predicate(predicate, seed)
    return n_locks == 12


def coverage(predicate) -> int:
    return sum(1 for seed in TWO_SITE_SEEDS if fills_from_seed(predicate, seed))


def one_site_coverage(predicate) -> int:
    return sum(1 for seed in ONE_SITE_SEEDS if fills_from_seed(predicate, seed))


def long_axis_k(predicate) -> int:
    return sum(1 for seed in LONG_AXIS_SEEDS if fills_from_seed(predicate, seed))


def run_lock_sets(
    predicate, seed: frozenset[Site] | set[Site]
) -> tuple[frozenset[Site], ...]:
    locked = set(seed)
    snapshots = [frozenset(locked)]
    for _tick in range(13):
        nxt = evolve(locked, predicate)
        if nxt == locked:
            break
        locked = nxt
        snapshots.append(frozenset(locked))
    return tuple(snapshots)


def bits_from_predicate(
    predicate,
    orbit_types: tuple[OrbitType, ...],
    orbits: dict[OrbitType, frozenset[Config]],
) -> BitTuple:
    assignment: dict[OrbitType, int] = {}
    for orbit_kind in orbit_types:
        sample = next(iter(orbits[orbit_kind]))
        value = int(predicate(sample))
        if any(int(predicate(member)) != value for member in orbits[orbit_kind]):
            raise RuntimeError("predicate is not cube-covariant")
        assignment[orbit_kind] = value
    return (
        assignment[WT1],
        assignment[OPP2],
        assignment[ADJ2],
        assignment[VERTEX3],
        assignment[MIXED3],
    )


def assignment_from_bits(bits: BitTuple) -> dict[OrbitType, int]:
    return {
        (0, 0, 3): 0,
        (0, 3, 0): 0,
        WT1: bits[0],
        (1, 2, 0): bits[0],
        OPP2: bits[1],
        (0, 2, 1): bits[1],
        ADJ2: bits[2],
        (2, 1, 0): bits[2],
        VERTEX3: bits[3],
        MIXED3: bits[4],
    }


def predicate_from_bits(bits: BitTuple, type_of: dict[Config, OrbitType]):
    assignment = assignment_from_bits(bits)

    def predicate(config: Config) -> int:
        return assignment[type_of[config]]

    return predicate


def complement_cell(config: Config) -> Config:
    return (
        1 - config[0],
        1 - config[1],
        1 - config[2],
        1 - config[3],
        1 - config[4],
        1 - config[5],
    )


def predicate_in_f_cut(predicate) -> bool:
    if int(predicate(EMPTY)) != 0 or int(predicate(FULL)) != 0:
        return False
    return all(
        int(predicate(config)) == int(predicate(complement_cell(config)))
        for config in product((0, 1), repeat=6)
    )


def in_f_cut(bits: BitTuple, type_of: dict[Config, OrbitType]) -> bool:
    return predicate_in_f_cut(predicate_from_bits(bits, type_of))


def support_of_bits(bits: BitTuple) -> int:
    return (
        ORBIT_PAIR_SIZE[WT1] * bits[0]
        + ORBIT_PAIR_SIZE[OPP2] * bits[1]
        + ORBIT_PAIR_SIZE[ADJ2] * bits[2]
        + ORBIT_PAIR_SIZE[VERTEX3] * bits[3]
        + ORBIT_PAIR_SIZE[MIXED3] * bits[4]
    )


def f_cut_free_data(
    orbit_types: tuple[OrbitType, ...],
) -> tuple[list[tuple[OrbitType, OrbitType]], list[OrbitType]]:
    used: set[OrbitType] = set()
    pairs: list[tuple[OrbitType, OrbitType]] = []
    fixed: list[OrbitType] = []
    empty_type = (0, 0, 3)
    full_type = (0, 3, 0)
    for orbit_kind in orbit_types:
        if orbit_kind in used:
            continue
        image = complement_type(orbit_kind)
        if image == orbit_kind:
            fixed.append(orbit_kind)
        else:
            pair = tuple(sorted((orbit_kind, image)))
            pairs.append((pair[0], pair[1]))
            used.add(orbit_kind)
            used.add(image)
    free_pairs = [pair for pair in pairs if empty_type not in pair and full_type not in pair]
    free_fixed = [orbit_kind for orbit_kind in fixed if orbit_kind not in (empty_type, full_type)]
    return free_pairs, free_fixed


def enumerate_remaining_bits() -> list[BitTuple]:
    members: list[BitTuple] = []
    for mask in range(32):
        bits: BitTuple = (
            (mask >> 0) & 1,
            (mask >> 1) & 1,
            (mask >> 2) & 1,
            (mask >> 3) & 1,
            (mask >> 4) & 1,
        )
        members.append(bits)
    return members


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
    orbit_sizes = {orbit_kind: len(orbits[orbit_kind]) for orbit_kind in orbit_types}
    type_of = {config: orbit_kind for orbit_kind, group in orbits.items() for config in group}
    free_pairs, free_fixed = f_cut_free_data(orbit_types)
    n_free = len(free_pairs) + len(free_fixed)
    n_cut = 1 << n_free

    displayed_pred = predicate_from_bits(DISPLAYED_BITS, type_of)
    sibling_pred = predicate_from_bits(SIBLING_BITS, type_of)
    displayed_locks, displayed_halt, displayed_history = run_predicate(
        displayed_pred, {SEED}
    )
    sibling_locks, sibling_halt, sibling_history = run_predicate(
        sibling_pred, {SEED}
    )
    displayed_sets = run_lock_sets(displayed_pred, {SEED})
    sibling_sets = run_lock_sets(sibling_pred, {SEED})
    displayed_k = long_axis_k(displayed_pred)
    displayed_cov1 = one_site_coverage(displayed_pred)
    displayed_support = support_of_bits(DISPLAYED_BITS)
    displayed_support_direct = sum(
        1 for cell in product((0, 1), repeat=6) if displayed_pred(cell)
    )

    l1_bits = bits_from_predicate(f_L1, orbit_types, orbits)
    ham_bits = bits_from_predicate(f_hamming, orbit_types, orbits)
    l1_locks, l1_halt, l1_history = run_predicate(f_L1, {SEED})
    ham_locks, _ham_halt, ham_history = run_predicate(f_hamming, {SEED})
    l1_support_direct = sum(1 for cell in product((0, 1), repeat=6) if f_L1(cell))
    matches_sibling = displayed_history == sibling_history and displayed_sets == sibling_sets
    matches_l1 = displayed_history == l1_history

    k4_members = [
        bits for bits in enumerate_remaining_bits() if bits[:3] == K4_PREFIX
    ]
    k4_k_values = {
        bits: long_axis_k(predicate_from_bits(bits, type_of)) for bits in k4_members
    }
    sibling_cov1 = one_site_coverage(sibling_pred)

    print(f"n_rotations={len(ROTATIONS)}")
    print(f"n_orbits={len(orbit_types)}")
    print(f"N_free={n_free}")
    print(f"|F_cut|={n_cut}")
    print(f"n_long_axis_seeds={len(LONG_AXIS_SEEDS)}")
    print(f"n_one_site_seeds={len(ONE_SITE_SEEDS)}")
    print(
        f"f_bits={DISPLAYED_BITS} supp={displayed_support} "
        f"k={displayed_k} cov1={displayed_cov1}"
    )
    print(f"f_locks={displayed_locks} halt={displayed_halt} history={displayed_history}")
    print(
        f"sibling_bits={SIBLING_BITS} locks={sibling_locks} "
        f"halt={sibling_halt} history={sibling_history} cov1={sibling_cov1}"
    )
    print(f"f_L1_bits={l1_bits} locks={l1_locks} history={l1_history}")
    print(f"matches_sibling={matches_sibling}")
    print(f"matches_l1={matches_l1}")
    print(f"f_hamming_bits={ham_bits} locks={ham_locks} history={ham_history}")
    print(f"k4_members={k4_members}")

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required note-plus-axiom string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/F_CUT_K4_V31_ONE_SITE_HALT_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and 'AUDIT_INPUT_PATHS = (\n'
        '    "docs/F_CUT_K4_V31_ONE_SITE_HALT_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ")" in self_source
        and AUDIT_TIMEOUT_SEC == 120,
    )
    checks.check(
        "thm1-twenty-four-rotations",
        "exactly 24 proper cube rotations",
        len(ROTATIONS) == 24 and len(set(ROTATIONS)) == 24,
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
        "thm1-ten-orbits",
        "exactly 10 orbits partition the 64 cells of {0,1}^6",
        len(orbit_types) == 10
        and sum(orbit_sizes.values()) == 64
        and orbit_sizes == expected_sizes,
    )
    checks.check(
        "thm1-f-cut-cardinality",
        "F_cut has five free bits and size 32",
        n_free == 5
        and n_cut == 32
        and len(free_pairs) == 3
        and len(free_fixed) == 2
        and in_f_cut(DISPLAYED_BITS, type_of),
    )
    checks.check(
        "thm1-two-cube-twelve",
        "the two-cube has twelve vertices and contains the seed",
        len(TWO_CUBE) == 12 and len(set(TWO_CUBE)) == 12 and SEED in TWO_CUBE,
    )
    checks.check(
        "thm1-four-long-axis-seeds",
        "exactly four long-axis 2-site seeds of the form ((0,y,z),(2,y,z))",
        len(LONG_AXIS_SEEDS) == 4
        and len(set(LONG_AXIS_SEEDS)) == 4
        and all(len(seed) == 2 and seed <= set(TWO_CUBE) for seed in LONG_AXIS_SEEDS)
        and LONG_AXIS_SEEDS
        == (
            frozenset(((0, 0, 0), (2, 0, 0))),
            frozenset(((0, 0, 1), (2, 0, 1))),
            frozenset(((0, 1, 0), (2, 1, 0))),
            frozenset(((0, 1, 1), (2, 1, 1))),
        ),
    )
    checks.check(
        "thm1-f-fills-long-axis",
        "f=(1,1,1,0,1) fills all four long-axis 2-site seeds",
        displayed_k == 4
        and DISPLAYED_BITS[:3] == K4_PREFIX
        and DISPLAYED_BITS == (1, 1, 1, 0, 1)
        and all(k4_k_values[bits] == 4 for bits in k4_members)
        and len(k4_members) == 4
        and "k(f)=4" in note_flat.replace(" ", ""),
    )
    checks.check(
        "thm1-cov1-eight",
        "f has cov1=8 on the twelve one-site seeds",
        displayed_cov1 == 8
        and sibling_cov1 == 8
        and DISPLAYED_BITS[3] == 0
        and displayed_support == 54
        and displayed_support_direct == 54
        and DISPLAYED_BITS not in MAXIMIZER_BITS
        and len(ONE_SITE_SEEDS) == 12
        and "cov1(f)=8" in note_flat.replace(" ", ""),
    )
    checks.check(
        "thm2-f-from-origin-fills",
        "f fills from (0,0,0): |locks_halt|=12 with reported T and history",
        displayed_locks == 12
        and displayed_halt == 5
        and displayed_history == (1, 4, 8, 10, 11, 12)
        and f"T = {displayed_halt}" in note
        and f"({', '.join(str(n) for n in displayed_history)})" in note,
    )
    checks.check(
        "thm2-f-L1-is-unbalanced-axis",
        "f_L1 is 1 iff some axis has c_+ != c_- (n != 0)",
        all(
            f_L1(config) == int(axis_type(config)[0] >= 1)
            for config in product((0, 1), repeat=6)
        )
        and l1_bits == L1_BITS
        and in_f_cut(l1_bits, type_of)
        and l1_support_direct == 56,
    )
    checks.check(
        "thm2-f-L1-not-hamming",
        "f_L1 is not Hamming |c|_1 mod 2",
        l1_bits != ham_bits
        and any(f_L1(config) != f_hamming(config) for config in product((0, 1), repeat=6))
        and "sum(config) % 2"
        not in self_source.split("def f_L1", 1)[1].split("def f_hamming", 1)[0]
        and ham_locks != 12,
    )
    checks.check(
        "thm2-f-L1-history",
        "f_L1 fills with history (1,4,8,11,12)",
        l1_locks == 12
        and l1_halt == 4
        and l1_history == (1, 4, 8, 11, 12),
    )
    checks.check(
        "thm3-matches-sibling-not-l1",
        "f history matches (1,1,1,0,0) and disagrees with L1",
        matches_sibling
        and not matches_l1
        and displayed_history == sibling_history == (1, 4, 8, 10, 11, 12)
        and displayed_sets == sibling_sets
        and displayed_history != l1_history
        and displayed_halt != l1_halt
        and DISPLAYED_BITS != SIBLING_BITS
        and DISPLAYED_BITS[:4] == SIBLING_BITS[:4]
        and DISPLAYED_BITS[4] == 1
        and SIBLING_BITS[4] == 0
        and "mixed3 is free" in note
        and "do not agree" in note,
    )
    checks.check(
        "thm3-displayed-not-adopted",
        "the named k=4 map and f_L1 are displayed, not adopted",
        "Displayed, not adopted" in note
        and 'hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"'
        in note
        and "Do not write f into Admissibility" in note,
    )
    checks.check(
        "lattice-and-admissibility-parents",
        "the live axiom memo supplies Z^3, proper cubic rotations, and a covariant nearest-neighbor rule",
        "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor"
        in axiom
        and "proper cubic rotations about each site." in axiom
        and "one fixed nearest-neighbor admissibility rule, covariant under lattice"
        in axiom
        and "A site with no record cannot be read." in axiom
        and "proper cubic rotations about each site" in note
        and "one fixed nearest-neighbor admissibility rule" in note,
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
        and "This is **not** Hamming parity" in note
        and "never Hamming" in note,
    )
    checks.check(
        "f-definition-in-note",
        "the note names f as the remaining-bit tuple (1, 1, 1, 0, 1)",
        "(1, 1, 1, 0, 1)" in note
        and "vertex3=0" in note
        and "mixed3=1" in note
        and "k=4" in note,
    )
    checks.check(
        "claim-type-and-gate",
        "bounded theorem type and a passing N1-N8 gate are source-visible",
        "**Type:** bounded_theorem" in note
        and all(f"### N{index}" in note for index in range(1, 9))
        and "No-Go Discipline disposition: **PASS**" in note
        and note.count("**ATTEMPTED**") == 6
        and "actual_current_surface_status: bounded-support" in note,
    )
    checks.check(
        "claim-scope-and-history",
        "claim_scope reports the lock history and does not adopt f",
        "F_cut map (1, 1, 1, 0, 1)" in note
        and "1-site lock history (1, 4, 8, 10, 11, 12)" in note
        and "Displayed, not adopted" in note
        and "off-patch o=0" in note,
    )
    checks.check(
        "not-leftover-6445",
        "the residual is the sibling comparison, not leftover-character of #6445",
        "Not leftover-character of #6445" in note
        and "did not report the 1-site lock history of" in note
        and "new comparison" in note,
    )
    checks.check(
        "off-patch-zero",
        "off-patch occupancy is the explicit 0 default, not a blank-block",
        "off-patch occupancy `0`" in note and "blank-block is a different rule" in note,
    )
    cache_probe = ROOT / "logs" / ("runner" + "-cache") / (
        "f_cut_k4_v31_one_site_halt_2026_08_15.txt"
    )
    checks.check(
        "no-cache-write",
        "this run did not emit a runner cache file",
        not cache_probe.is_file(),
    )

    print("per_element: checked exactly — each of the 64 neighbor 6-tuples is assigned its axis-type orbit")
    print("per_site: checked exactly — each of the 12 two-cube vertices is a lock site under o=0")
    print("per_mode: checked exactly — the named F_cut map is run from the 1-site seed and the long-axis four")
    print("per_block: checked exactly — named k=4 vertex3=0 sibling is run to a fixed point from the 1-site seed")
    print("lattice_wide: checked and not executed — no Z^3-wide formation law or Admissibility rewrite is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
