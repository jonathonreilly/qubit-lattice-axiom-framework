#!/usr/bin/env python3
"""List the four two-site seeds the F_cut rival f_mix0 does not fill.

Reconstruct the 24 proper cube rotations, the ten axis-type orbits, the
32-element three-cut class F_cut, and the remaining-bit map f_mix0 with
tuple (wt1, opp2, adj2, vertex3, mixed3) = (1, 0, 1, 1, 0). Enumerate
all 66 two-site seeds on the twelve-vertex two-cube with off-patch
occupancy 0. Report coverage, the four miss seeds in lex order with
halt histories, and whether that four-set equals the four seeds f_L1
misses. f_L1 is the unbalanced-axis predicate (some n_mu != 0), never
Hamming |c|_1 mod 2.
"""

from __future__ import annotations

from itertools import combinations, permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/F_MIX0_TWO_SITE_MISS_SEEDS_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/F_MIX0_TWO_SITE_MISS_SEEDS_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
SEED_ONE: Site = (0, 0, 0)
SEED_FACE: frozenset[Site] = frozenset({(0, 0, 0), (1, 1, 0)})
SEED_SSTAR: frozenset[Site] = frozenset({(0, 0, 0), (2, 1, 1)})

BIT_NAMES: tuple[str, ...] = ("wt1", "opp2", "adj2", "vertex3", "mixed3")
BIT_TYPES: dict[str, OrbitType] = {
    "wt1": (1, 0, 2),
    "opp2": (0, 1, 2),
    "adj2": (2, 0, 1),
    "vertex3": (3, 0, 0),
    "mixed3": (1, 1, 1),
}
L1_TUPLE: tuple[int, ...] = (1, 0, 1, 1, 1)
MIX0_TUPLE: tuple[int, ...] = (1, 0, 1, 1, 0)


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
    for _tick in range(13):
        nxt = evolve(locked, predicate)
        if nxt == locked:
            halt_tick = _tick
            break
        locked = nxt
        history.append(len(locked))
    else:
        halt_tick = 13
    return len(locked), halt_tick, tuple(history)


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


def named_tuple_from_assignment(assignment: dict[OrbitType, int]) -> tuple[int, ...]:
    return tuple(assignment[BIT_TYPES[name]] for name in BIT_NAMES)


def assignment_from_named(named: tuple[int, ...]) -> dict[OrbitType, int]:
    assignment = {
        BIT_TYPES["wt1"]: named[0],
        complement_type(BIT_TYPES["wt1"]): named[0],
        BIT_TYPES["opp2"]: named[1],
        complement_type(BIT_TYPES["opp2"]): named[1],
        BIT_TYPES["adj2"]: named[2],
        complement_type(BIT_TYPES["adj2"]): named[2],
        BIT_TYPES["vertex3"]: named[3],
        BIT_TYPES["mixed3"]: named[4],
        axis_type(EMPTY): 0,
        axis_type(FULL): 0,
    }
    return assignment


def predicate_from_assignment(assignment: dict[OrbitType, int], type_of: dict[Config, OrbitType]):
    def predicate(config: Config) -> int:
        return assignment[type_of[config]]

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


def support_of_assignment(
    assignment: dict[OrbitType, int],
    orbit_sizes: dict[OrbitType, int],
) -> int:
    return sum(orbit_sizes[orbit_type] for orbit_type, value in assignment.items() if value == 1)


def two_site_seeds() -> tuple[frozenset[Site], ...]:
    pairs = [frozenset(pair) for pair in combinations(TWO_CUBE, 2)]
    return tuple(sorted(pairs, key=lambda seed: tuple(sorted(seed))))


def seed_key(seed: frozenset[Site]) -> tuple[Site, ...]:
    return tuple(sorted(seed))


def miss_census(
    predicate, seeds: tuple[frozenset[Site], ...]
) -> tuple[int, tuple[tuple[tuple[Site, ...], int, int, tuple[int, ...]], ...]]:
    misses = []
    n_fill = 0
    for seed in seeds:
        n_locks, halt_tick, history = run_predicate(predicate, seed)
        if n_locks == 12:
            n_fill += 1
        else:
            misses.append((seed_key(seed), n_locks, halt_tick, history))
    return n_fill, tuple(misses)


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
    type_of = {config: orbit_type for orbit_type, members in orbits.items() for config in members}
    free_pairs, free_fixed = f_cut_free_data(orbit_types, empty_type, full_type)
    n_cut = 1 << (len(free_pairs) + len(free_fixed))

    l1_bits = bits_from_predicate(f_L1, orbit_types, orbits)
    ham_bits = bits_from_predicate(f_hamming, orbit_types, orbits)
    l1_assign = dict(zip(orbit_types, l1_bits, strict=True))
    l1_named = named_tuple_from_assignment(l1_assign)

    mix0_assign = assignment_from_named(MIX0_TUPLE)
    mix0_bits = tuple(mix0_assign[orbit_type] for orbit_type in orbit_types)
    f_mix0 = predicate_from_assignment(mix0_assign, type_of)
    mix0_named = named_tuple_from_assignment(mix0_assign)
    mix0_support = support_of_assignment(mix0_assign, orbit_sizes)

    seeds = two_site_seeds()
    mix0_cov, mix0_misses = miss_census(f_mix0, seeds)
    l1_cov, l1_misses = miss_census(f_L1, seeds)
    mix0_miss_keys = tuple(item[0] for item in mix0_misses)
    l1_miss_keys = tuple(item[0] for item in l1_misses)
    same_miss_set = set(mix0_miss_keys) == set(l1_miss_keys)

    mix0_face = run_predicate(f_mix0, SEED_FACE)
    mix0_sstar = run_predicate(f_mix0, SEED_SSTAR)
    l1_face = run_predicate(f_L1, SEED_FACE)
    l1_sstar = run_predicate(f_L1, SEED_SSTAR)
    mix0_one = run_predicate(f_mix0, frozenset({SEED_ONE}))
    ham_face = run_predicate(f_hamming, SEED_FACE)

    print(f"n_rotations={len(ROTATIONS)}")
    print(f"n_orbits={len(orbit_types)}")
    print(f"|F_cut|={n_cut}")
    print(f"n_two_site_seeds={len(seeds)}")
    print(f"L1_tuple={dict(zip(BIT_NAMES, l1_named))}")
    print(f"MIX0_tuple={dict(zip(BIT_NAMES, mix0_named))}")
    print(f"mix0_support={mix0_support}")
    print(f"cov(f_mix0)={mix0_cov}")
    print(f"cov(f_L1)={l1_cov}")
    print(f"f_mix0_face locks={mix0_face[0]} halt={mix0_face[1]} history={mix0_face[2]}")
    print(f"f_mix0_Sstar locks={mix0_sstar[0]} halt={mix0_sstar[1]} history={mix0_sstar[2]}")
    print("f_mix0_misses:")
    for key, n_locks, halt_tick, history in mix0_misses:
        print(f"  seed={key} locks={n_locks} halt={halt_tick} history={history}")
    print("f_L1_misses:")
    for key, n_locks, halt_tick, history in l1_misses:
        print(f"  seed={key} locks={n_locks} halt={halt_tick} history={history}")
    print(f"same_four={same_miss_set}")

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required note-plus-axiom string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/F_MIX0_TWO_SITE_MISS_SEEDS_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and "AUDIT_INPUT_PATHS = (\n"
        '    "docs/F_MIX0_TWO_SITE_MISS_SEEDS_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
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
        "exactly 10 axis-type orbits partition the 64 cells",
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
        "thm1-named-orbit-types",
        "wt1/opp2/adj2/vertex3/mixed3 are the listed axis-type orbits",
        orbit_sizes == expected_sizes
        and BIT_TYPES["wt1"] == (1, 0, 2)
        and BIT_TYPES["opp2"] == (0, 1, 2)
        and BIT_TYPES["adj2"] == (2, 0, 1)
        and BIT_TYPES["vertex3"] == (3, 0, 0)
        and BIT_TYPES["mixed3"] == (1, 1, 1),
    )
    checks.check(
        "thm1-f-L1-is-unbalanced-axis",
        "f_L1 is 1 iff some axis has c_+ != c_- (n != 0)",
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
    checks.check(
        "thm1-two-cube-sixty-six-seeds",
        "the two-cube has twelve vertices and C(12,2)=66 two-site seeds",
        len(TWO_CUBE) == 12
        and len(set(TWO_CUBE)) == 12
        and len(seeds) == 66
        and SEED_FACE.issubset(TWO_CUBE)
        and SEED_SSTAR.issubset(TWO_CUBE)
        and mix0_miss_keys == tuple(sorted(mix0_miss_keys)),
    )
    checks.check(
        "thm1-mix0-in-f-cut-cov-62",
        "f_mix0 is the F_cut map (1,0,1,1,0) with cov=62",
        in_f_cut(mix0_bits, orbit_types, empty_type, full_type)
        and mix0_named == MIX0_TUPLE == (1, 0, 1, 1, 0)
        and mix0_named != L1_TUPLE
        and l1_named == L1_TUPLE
        and n_cut == 32
        and mix0_support == 44
        and mix0_cov == 62
        and mix0_one[0] == 12
        and mix0_one[2] == (1, 4, 8, 11, 12),
    )
    checks.check(
        "thm1-face-diagonal-and-sstar-fill",
        "f_mix0 fills the face-diagonal seed and opposite-corner S*",
        mix0_face[0] == 12
        and mix0_face[2] == (2, 7, 11, 12)
        and mix0_sstar[0] == 12
        and mix0_sstar[2] == (2, 8, 12)
        and l1_face[0] == 12
        and l1_sstar[0] == 12
        and SEED_FACE not in {frozenset(key) for key in mix0_miss_keys}
        and SEED_SSTAR not in {frozenset(key) for key in mix0_miss_keys},
    )
    expected_miss_keys = (
        ((0, 0, 0), (2, 0, 0)),
        ((0, 0, 1), (2, 0, 1)),
        ((0, 1, 0), (2, 1, 0)),
        ((0, 1, 1), (2, 1, 1)),
    )
    checks.check(
        "thm2-four-miss-seeds-lex",
        "f_mix0 misses exactly four two-site seeds, listed in lex order",
        len(mix0_misses) == 4
        and mix0_miss_keys == expected_miss_keys
        and mix0_cov + len(mix0_misses) == 66,
    )
    checks.check(
        "thm2-halt-histories",
        "each miss seed halts at 8 locks with history (2, 6, 8)",
        all(item[1] == 8 and item[2] == 2 and item[3] == (2, 6, 8) for item in mix0_misses),
    )
    checks.check(
        "thm3-same-four-as-l1",
        "the four f_mix0 miss seeds equal the four f_L1 miss seeds",
        l1_cov == 62
        and len(l1_misses) == 4
        and l1_miss_keys == mix0_miss_keys
        and same_miss_set
        and all(item[3] == (2, 6, 8) for item in l1_misses)
        and ham_face[0] != 12,
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
        "bounded theorem, displayed-not-adopted miss-set comparison, and machine status",
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
        "f_mix0 is not written into Admissibility",
        "Do not write f_mix0 into Admissibility" in note
        and "no axiom or approved primitive is added" in note
        and "hypothetical_axiom_status" in note,
    )
    checks.check(
        "not-leftover-6434",
        "the residual is the four miss seeds, not leftover-character of #6434 or l1miss2",
        "Not leftover-character of #6434" in note
        and "l1miss2" in note
        and "same four" in note,
    )
    checks.check(
        "off-patch-zero",
        "off-patch occupancy is the explicit 0 default, not a blank-block",
        "off-patch occupancy `0`" in note and "blank-block is a different rule" in note,
    )
    checks.check(
        "claim-scope-and-same-set",
        "claim_scope lists the four misses and states they equal f_L1's four",
        "they are the same four that f_L1 misses" in note
        and "Displayed, not adopted" in note
        and "((0, 0, 0), (2, 0, 0))" in note
        and "(2, 6, 8)" in note,
    )

    print("per_element: checked exactly — each of the 64 neighbor 6-tuples is assigned its axis-type orbit")
    print("per_site: checked exactly — each of the twelve two-cube vertices uses the same six-direction stencil")
    print("per_mode: checked exactly — f_mix0 and f_L1 are each run from every two-site seed to a fixed point")
    print("per_block: checked exactly — the four miss seeds and halt histories are compared as sets")
    print("lattice_wide: checked and not executed — no Z^3-wide formation law or Admissibility rewrite is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
