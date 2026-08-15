#!/usr/bin/env python3
"""mixed3 among the 96 cube-covariant 1-site fillers on the two-cube.

Recompute the 24 proper cube rotations, the ten axis-type orbits, and the
96 maps with f(empty)=0 that fill the twelve-vertex two-cube from the
1-site seed with off-patch occupancy 0.  mixed3 is the G-orbit of axis
type (1,1,1): one unbalanced axis, one fully occupied, one empty.
f_L1 is the unbalanced-axis predicate (some n_mu != 0), never Hamming
|c|_1 mod 2.  N_mix3 counts fillers with f(mixed3)=1.
"""

from __future__ import annotations

from itertools import permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/ONE_SITE_FILLERS_MIXED3_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/ONE_SITE_FILLERS_MIXED3_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
TWO_CUBE: tuple[Site, ...] = tuple(
    (x, y, z) for x in range(3) for y in range(2) for z in range(2)
)
SEED: Site = (0, 0, 0)
MIXED3_REP: Config = (1, 0, 1, 1, 0, 0)

BIT_NAMES: tuple[str, ...] = ("wt1", "opp2", "adj2", "vertex3", "mixed3")
BIT_TYPES: dict[str, OrbitType] = {
    "wt1": (1, 0, 2),
    "opp2": (0, 1, 2),
    "adj2": (2, 0, 1),
    "vertex3": (3, 0, 0),
    "mixed3": (1, 1, 1),
}
L1_TUPLE: tuple[int, ...] = (1, 0, 1, 1, 1)
DIAMOND_TUPLE: tuple[int, ...] = (1, 0, 1, 0, 1)


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


def f_L1(config: Config) -> int:
    """1 iff some axis is unbalanced: n_mu != 0.  Not Hamming parity."""
    return int(any(config[2 * axis] != config[2 * axis + 1] for axis in range(3)))


def f_hamming(config: Config) -> int:
    return sum(config) % 2


def f_diamond(config: Config) -> int:
    """Displayed extra 1-site filler with f(mixed3)=1.  Not adopted."""
    orbit = axis_type(config)
    return int(orbit[0] >= 1 and orbit != (3, 0, 0))


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


def run_predicate(predicate) -> tuple[int, int, bool, tuple[int, ...]]:
    locked = {SEED}
    history = [len(locked)]
    first_wave_empty = False
    halt_tick = 0
    for tick in range(13):
        nxt = evolve(locked, predicate)
        if tick == 0:
            first_wave_empty = nxt == locked
        if nxt == locked:
            halt_tick = tick
            break
        locked = nxt
        history.append(len(locked))
    else:
        halt_tick = 13
    return len(locked), halt_tick, first_wave_empty, tuple(history)


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


def predicate_from_bits(
    bits: tuple[int, ...],
    orbit_types: tuple[OrbitType, ...],
    type_of: dict[Config, OrbitType],
):
    assignment = dict(zip(orbit_types, bits, strict=True))

    def predicate(config: Config) -> int:
        return assignment[type_of[config]]

    return predicate


def census_fillers(
    orbit_types: tuple[OrbitType, ...],
    orbits: dict[OrbitType, frozenset[Config]],
) -> list[tuple[int, ...]]:
    type_of = {config: orbit_type for orbit_type, members in orbits.items() for config in members}
    empty_index = orbit_types.index(axis_type(EMPTY))
    free = [index for index in range(len(orbit_types)) if index != empty_index]
    fillers: list[tuple[int, ...]] = []
    for mask in range(1 << len(free)):
        bits_list = [0] * len(orbit_types)
        for rank, index in enumerate(free):
            bits_list[index] = (mask >> rank) & 1
        bits = tuple(bits_list)
        n_locks, _halt, _first_empty, _history = run_predicate(
            predicate_from_bits(bits, orbit_types, type_of)
        )
        if n_locks == 12:
            fillers.append(bits)
    return fillers


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
    n_maps = 2 ** (len(orbit_types) - 1)
    mix_type = BIT_TYPES["mixed3"]
    mix_index = orbit_types.index(mix_type)

    l1_bits = bits_from_predicate(f_L1, orbit_types, orbits)
    diamond_bits = bits_from_predicate(f_diamond, orbit_types, orbits)
    ham_bits = bits_from_predicate(f_hamming, orbit_types, orbits)
    l1_assign = dict(zip(orbit_types, l1_bits, strict=True))
    diamond_assign = dict(zip(orbit_types, diamond_bits, strict=True))
    l1_named = named_tuple_from_assignment(l1_assign)
    diamond_named = named_tuple_from_assignment(diamond_assign)
    l1_locks, l1_halt, l1_first_empty, l1_history = run_predicate(f_L1)
    diamond_locks, diamond_halt, diamond_first_empty, diamond_history = run_predicate(
        f_diamond
    )
    ham_locks, _ham_halt, _ham_first, _ham_history = run_predicate(f_hamming)

    fillers = census_fillers(orbit_types, orbits)
    mixers = [bits for bits in fillers if bits[mix_index] == 1]
    n_mix3 = len(mixers)

    print(f"n_rotations={len(ROTATIONS)}")
    print(f"n_orbits={len(orbit_types)}")
    print(f"n_maps_empty0={n_maps}")
    print(f"N_fill={len(fillers)}")
    print(f"mixed3_type={mix_type} size={orbit_sizes[mix_type]} rep={MIXED3_REP}")
    print(f"L1_tuple={dict(zip(BIT_NAMES, l1_named))}")
    print(f"diamond_tuple={dict(zip(BIT_NAMES, diamond_named))}")
    print(f"N_mix3={n_mix3}")
    print(f"f_L1_locks={l1_locks} halt={l1_halt} history={l1_history}")
    print(f"f_diamond_locks={diamond_locks} halt={diamond_halt} history={diamond_history}")
    print(f"hamming_locks={ham_locks}")

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required note-plus-axiom string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/ONE_SITE_FILLERS_MIXED3_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and 'AUDIT_INPUT_PATHS = (\n'
        '    "docs/ONE_SITE_FILLERS_MIXED3_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
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
        "thm1-mixed3-orbit",
        "mixed3 is the size-12 G-orbit of axis type (1,1,1)",
        orbit_sizes == expected_sizes
        and BIT_TYPES["mixed3"] == (1, 1, 1)
        and axis_type(MIXED3_REP) == (1, 1, 1)
        and MIXED3_REP in orbits[mix_type]
        and len(orbits[mix_type]) == 12
        and BIT_TYPES["wt1"] == (1, 0, 2)
        and BIT_TYPES["opp2"] == (0, 1, 2)
        and BIT_TYPES["adj2"] == (2, 0, 1)
        and BIT_TYPES["vertex3"] == (3, 0, 0),
    )
    checks.check(
        "thm1-ninety-six-fillers",
        "exactly 96 cube-covariant maps with f(empty)=0 fill the two-cube",
        n_maps == 512
        and len(fillers) == 96
        and len(set(fillers)) == 96
        and axis_type(EMPTY) == (0, 0, 3)
        and l1_bits[orbit_types.index(axis_type(EMPTY))] == 0,
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
        "thm1-f-L1-in-96-and-mixed3",
        "f_L1 is one of the 96 fillers and f_L1(mixed3)=1",
        l1_bits in fillers
        and l1_named == L1_TUPLE
        and l1_assign[mix_type] == 1
        and f_L1(MIXED3_REP) == 1
        and l1_locks == 12
        and l1_halt == 4
        and not l1_first_empty
        and l1_history == (1, 4, 8, 11, 12),
    )
    checks.check(
        "thm1-two-cube-twelve",
        "the two-cube has twelve vertices and contains the seed",
        len(TWO_CUBE) == 12 and len(set(TWO_CUBE)) == 12 and SEED in TWO_CUBE,
    )
    checks.check(
        "thm2-n-mix3",
        f"N_mix3 = {n_mix3} is the number of the 96 fillers with f(mixed3)=1",
        n_mix3 == 48
        and n_mix3 == sum(1 for bits in fillers if bits[mix_index] == 1)
        and n_mix3 == len(fillers) // 2
        and f"N_mix3 = {n_mix3}" in note,
    )
    checks.check(
        "thm3-not-unique",
        "N_mix3>1 so mixed3=1 does not select f_L1 among the 96",
        n_mix3 > 1
        and l1_bits in mixers
        and diamond_bits in mixers
        and diamond_bits != l1_bits,
    )
    checks.check(
        "thm3-displayed-other",
        "displayed f_♦ fills, fires mixed3, and has tuple (1,0,1,0,1)",
        diamond_named == DIAMOND_TUPLE
        and diamond_assign[mix_type] == 1
        and f_diamond(MIXED3_REP) == 1
        and diamond_locks == 12
        and diamond_halt == 5
        and not diamond_first_empty
        and diamond_history == (1, 4, 8, 10, 11, 12)
        and diamond_bits in fillers
        and ham_bits not in fillers
        and ham_locks != 12,
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
        "bounded theorem, displayed-not-adopted mixed3 count, and machine status",
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
        "mixed3 is not written into Admissibility",
        "Do not write mixed3 into Admissibility" in note
        and "no axiom or approved primitive is added" in note
        and "hypothetical_axiom_status" in note,
    )
    checks.check(
        "not-leftover-6404",
        "the residual is N_mix3 on the 96, not leftover-character of the eight-filler bit splits",
        "Not leftover-character of #6404" in note
        and "Not leftover-character of #6402" in note
        and "Not leftover-character of #6403" in note
        and "Not leftover-character of #6405" in note
        and "independently motivated extra on the 96" in note,
    )
    checks.check(
        "off-patch-zero",
        "off-patch occupancy is the explicit 0 default, not a blank-block",
        "off-patch occupancy `0`" in note and "blank-block is a different rule" in note,
    )
    checks.check(
        "claim-scope-and-n-mix3",
        "claim_scope reports N_mix3 among the 96 and does not adopt mixed3",
        "Among the 96 cube-covariant 1-site fillers" in note
        and "N_mix3 = 48 have f(mixed3)=1" in note
        and "f_L1 is not unique in that subset" in note
        and "Displayed, not adopted" in note,
    )

    print("per_element: checked exactly — each of the 64 neighbor 6-tuples is assigned its axis-type orbit")
    print("per_site: checked exactly — each of the twelve two-cube vertices uses the same six-direction stencil")
    print("per_mode: checked exactly — every cube-covariant f with f(empty)=0 is classified as filler or not")
    print("per_block: checked exactly — N_mix3 is the mixed3=1 cardinality inside the 96-filler set")
    print("lattice_wide: checked and not executed — no Z^3-wide formation law or Admissibility rewrite is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
