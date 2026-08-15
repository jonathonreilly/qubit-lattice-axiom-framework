#!/usr/bin/env python3
"""Identify the unique support-26 cube-covariant 1-site filler.

Reconstruct the 24 proper cube rotations, the ten axis-type orbits of
{0,1}^6, and the 512 cube-covariant maps with f(empty)=0.  Fill the
twelve-vertex two-cube from the 1-site seed with off-patch occupancy 0.
Among the 96 fillers, compute min supp(f), prove N_min=1, and name that
unique minimizer by its orbit bits and F_cut membership.  f_L1 is the
unbalanced-axis predicate (some n_mu != 0), never Hamming |c|_1 mod 2.
"""

from __future__ import annotations

from itertools import permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/SPARSEST_FILLER_IDENTITY_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/SPARSEST_FILLER_IDENTITY_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
SEED: Site = (0, 0, 0)

BIT_NAMES: tuple[str, ...] = ("wt1", "opp2", "adj2", "vertex3", "mixed3")
BIT_TYPES: dict[str, OrbitType] = {
    "wt1": (1, 0, 2),
    "opp2": (0, 1, 2),
    "adj2": (2, 0, 1),
    "vertex3": (3, 0, 0),
    "mixed3": (1, 1, 1),
}
ALL_ORBIT_NAMES: tuple[str, ...] = (
    "empty",
    "wt1",
    "opp2",
    "adj2",
    "vertex3",
    "mixed3",
    "wt5",
    "opp4",
    "adj4",
    "full",
)
ALL_ORBIT_TYPES: dict[str, OrbitType] = {
    "empty": (0, 0, 3),
    "wt1": (1, 0, 2),
    "opp2": (0, 1, 2),
    "adj2": (2, 0, 1),
    "vertex3": (3, 0, 0),
    "mixed3": (1, 1, 1),
    "wt5": (1, 2, 0),
    "opp4": (0, 2, 1),
    "adj4": (2, 1, 0),
    "full": (0, 3, 0),
}
# Unique support-26 filler: fire iff n_both=0 and c != empty.
MIN_NAMED: tuple[int, ...] = (1, 0, 1, 1, 0)
MIN_ALL: tuple[int, ...] = (0, 1, 0, 1, 1, 0, 0, 0, 0, 0)
L1_NAMED: tuple[int, ...] = (1, 0, 1, 1, 1)


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


def f_min_closed(config: Config) -> int:
    """Closed form of the unique support-26 filler: n_both=0 and c != empty."""
    n_unbalanced, n_both, _n_empty = axis_type(config)
    return int(n_both == 0 and n_unbalanced >= 1)


def support_size(predicate) -> int:
    return sum(int(predicate(raw)) for raw in product((0, 1), repeat=6))


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


def named_tuple_from_assignment(assignment: dict[OrbitType, int]) -> tuple[int, ...]:
    return tuple(assignment[BIT_TYPES[name]] for name in BIT_NAMES)


def all_tuple_from_assignment(assignment: dict[OrbitType, int]) -> tuple[int, ...]:
    return tuple(assignment[ALL_ORBIT_TYPES[name]] for name in ALL_ORBIT_NAMES)


def predicate_from_bits(
    bits: tuple[int, ...],
    orbit_types: tuple[OrbitType, ...],
    type_of: dict[Config, OrbitType],
):
    assignment = dict(zip(orbit_types, bits, strict=True))

    def predicate(config: Config) -> int:
        return assignment[type_of[config]]

    return predicate


def support_from_bits(
    bits: tuple[int, ...],
    orbit_types: tuple[OrbitType, ...],
    orbit_sizes: dict[OrbitType, int],
) -> int:
    return sum(
        orbit_sizes[orbit_type]
        for orbit_type, bit in zip(orbit_types, bits, strict=True)
        if bit == 1
    )


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
    print("external_scientific_inputs: none; exact two-cube occupancy census only")
    print("package_local_integrity_reads: proposed source note and live axiom memo only")

    orbits = build_orbits()
    orbit_types = tuple(sorted(orbits))
    orbit_sizes = {orbit_type: len(orbits[orbit_type]) for orbit_type in orbit_types}
    empty_type = axis_type(EMPTY)
    full_type = axis_type(FULL)
    n_maps = 2 ** (len(orbit_types) - 1)

    l1_bits = bits_from_predicate(f_L1, orbit_types, orbits)
    min_closed_bits = bits_from_predicate(f_min_closed, orbit_types, orbits)
    ham_bits = bits_from_predicate(f_hamming, orbit_types, orbits)
    l1_assign = dict(zip(orbit_types, l1_bits, strict=True))
    min_closed_assign = dict(zip(orbit_types, min_closed_bits, strict=True))
    l1_named = named_tuple_from_assignment(l1_assign)
    min_closed_named = named_tuple_from_assignment(min_closed_assign)
    min_closed_all = all_tuple_from_assignment(min_closed_assign)
    l1_locks, l1_halt, l1_first_empty, l1_history = run_predicate(f_L1)
    min_locks, min_halt, min_first_empty, min_history = run_predicate(f_min_closed)
    ham_locks, _ham_halt, _ham_first, _ham_history = run_predicate(f_hamming)
    supp_l1 = support_from_bits(l1_bits, orbit_types, orbit_sizes)
    supp_min_closed = support_from_bits(min_closed_bits, orbit_types, orbit_sizes)
    supp_l1_cells = support_size(f_L1)
    supp_min_cells = support_size(f_min_closed)

    fillers = census_fillers(orbit_types, orbits)
    n_fill = len(fillers)
    filler_supps = [support_from_bits(bits, orbit_types, orbit_sizes) for bits in fillers]
    m_supp = min(filler_supps)
    n_min = sum(1 for size in filler_supps if size == m_supp)
    min_bits_list = [bits for bits, size in zip(fillers, filler_supps) if size == m_supp]
    min_bits = min_bits_list[0] if len(min_bits_list) == 1 else None
    min_assign = dict(zip(orbit_types, min_bits, strict=True)) if min_bits is not None else {}
    min_named = named_tuple_from_assignment(min_assign) if min_assign else ()
    min_all = all_tuple_from_assignment(min_assign) if min_assign else ()
    min_in_cut = (
        in_f_cut(min_bits, orbit_types, empty_type, full_type)
        if min_bits is not None
        else False
    )
    l1_in_cut = in_f_cut(l1_bits, orbit_types, empty_type, full_type)

    print(f"n_rotations={len(ROTATIONS)}")
    print(f"n_orbits={len(orbit_types)}")
    print(f"n_maps_empty0={n_maps}")
    print(f"N_fill={n_fill}")
    print(f"m={m_supp}")
    print(f"N_min={n_min}")
    print(f"supp_f_L1={supp_l1}")
    print(f"f_min_named={dict(zip(BIT_NAMES, min_named)) if min_named else None}")
    print(f"f_min_all={dict(zip(ALL_ORBIT_NAMES, min_all)) if min_all else None}")
    print(f"f_min_in_F_cut={int(min_in_cut)}")
    print(f"f_L1_named={dict(zip(BIT_NAMES, l1_named))}")
    print(f"f_L1_locks={l1_locks} halt={l1_halt} history={l1_history}")
    print(f"f_min_locks={min_locks} halt={min_halt} history={min_history}")
    print(f"hamming_locks={ham_locks}")

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required note-plus-axiom string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/SPARSEST_FILLER_IDENTITY_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and "AUDIT_INPUT_PATHS = (\n"
        '    "docs/SPARSEST_FILLER_IDENTITY_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
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
        "thm1-five-hundred-twelve-maps",
        "cube-covariant maps with f(empty)=0 number 512",
        n_maps == 512 and empty_type == (0, 0, 3) and l1_bits[orbit_types.index(empty_type)] == 0,
    )
    checks.check(
        "thm1-two-cube-twelve",
        "the two-cube has twelve vertices and contains the seed",
        len(TWO_CUBE) == 12 and len(set(TWO_CUBE)) == 12 and SEED in TWO_CUBE,
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
        "thm1-n-fill-and-l1-fills",
        "N_fill=96 and f_L1 is one of the 96 fillers",
        n_fill == 96
        and len(set(fillers)) == 96
        and l1_bits in fillers
        and l1_locks == 12
        and not l1_first_empty
        and l1_history == (1, 4, 8, 11, 12)
        and f"N_fill = {n_fill}" in note,
    )
    checks.check(
        "thm1-supp-l1",
        f"supp(f_L1) = {supp_l1}",
        supp_l1 == 56
        and supp_l1 == supp_l1_cells
        and supp_l1 == sum(orbit_sizes[t] for t in orbit_types if l1_assign[t] == 1)
        and f"supp(f_L1) = {supp_l1}" in note_flat,
    )
    checks.check(
        "thm1-unique-min-not-l1",
        f"min supp is m={m_supp} with N_min={n_min}, and that filler is not f_L1",
        m_supp == 26
        and n_min == 1
        and min_bits is not None
        and min_bits != l1_bits
        and supp_l1 != m_supp
        and f"m = {m_supp}" in note_flat
        and f"N_min = {n_min}" in note_flat,
    )
    checks.check(
        "thm2-f-min-named-tuple",
        "f_min on (wt1,opp2,adj2,vertex3,mixed3) is (1,0,1,1,0)",
        min_named == MIN_NAMED
        and min_closed_named == MIN_NAMED
        and min_named != L1_NAMED
        and l1_named == L1_NAMED
        and "(1, 0, 1, 1, 0)" in note,
    )
    checks.check(
        "thm2-f-min-all-orbits",
        "f_min bits on every axis-type orbit are the nonempty n_both=0 assignment",
        min_all == MIN_ALL
        and min_closed_all == MIN_ALL
        and min_bits == min_closed_bits
        and all(
            min_assign[ALL_ORBIT_TYPES[name]] == bit
            for name, bit in zip(ALL_ORBIT_NAMES, MIN_ALL, strict=True)
        ),
    )
    checks.check(
        "thm2-f-min-closed-form",
        "f_min(c)=1 iff n_both=0 and some axis is unbalanced",
        all(
            f_min_closed(config) == int(min_assign[axis_type(config)])
            for config in product((0, 1), repeat=6)
        )
        and supp_min_closed == 26
        and supp_min_closed == supp_min_cells
        and min_locks == 12
        and not min_first_empty,
    )
    checks.check(
        "thm2-f-min-not-in-f-cut",
        "f_min is not in F_cut: complement-even fails on wt1 vs wt5",
        min_in_cut is False
        and min_assign[ALL_ORBIT_TYPES["empty"]] == 0
        and min_assign[ALL_ORBIT_TYPES["full"]] == 0
        and min_assign[ALL_ORBIT_TYPES["wt1"]] != min_assign[ALL_ORBIT_TYPES["wt5"]]
        and l1_in_cut is True
        and "f_min is not a member of `F_cut`" in note_flat,
    )
    checks.check(
        "thm3-displayed-rival",
        "the unique support-26 map is displayed as a named rival and is not adopted",
        "Displayed, not adopted" in note
        and "Do not write `f_min` into Admissibility" in note
        and "named rival member" in note
        and min_bits != l1_bits
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
        and "A site with no record cannot be read." in axiom
        and "A site with no record cannot be read." in note,
    )
    checks.check(
        "note-contract",
        "bounded theorem, displayed-not-adopted identity, and machine status",
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
        "the identified map is not written into Admissibility",
        "Do not write `f_min` into Admissibility" in note
        and "no axiom or approved primitive is added" in note
        and "hypothetical_axiom_status" in note,
    )
    checks.check(
        "not-leftover-6400",
        "the residual is the identity of the unique minimizer, not leftover-character of #6400",
        "Not leftover-character of #6400" in note
        and "that census reported only `m` and `N_min`" in note,
    )
    checks.check(
        "off-patch-zero",
        "off-patch occupancy is the explicit 0 default, not a blank-block",
        "off-patch occupancy `0`" in note and "blank-block is a different rule" in note,
    )
    checks.check(
        "claim-scope-identity",
        "claim_scope identifies the unique support-26 map by orbit bits and F_cut membership",
        "Among the 96 cube-covariant 1-site fillers" in note
        and "unique support-26 map is identified by its orbit bits and F_cut membership"
        in note
        and "It is not f_L1" in note
        and "Displayed, not adopted" in note,
    )
    checks.check(
        "mutation-l1-and-hamming",
        "f_L1 and Hamming are rejected as the unique support-26 filler",
        supp_l1 == 56
        and support_from_bits(ham_bits, orbit_types, orbit_sizes) == 32
        and min_named != L1_NAMED
        and min_all != all_tuple_from_assignment(l1_assign),
    )

    print(
        "per_element: checked exactly — each of the 64 neighbor 6-tuples is assigned its axis-type orbit"
    )
    print(
        "per_site: checked exactly — each of the twelve two-cube vertices uses the same six-direction stencil"
    )
    print(
        "per_mode: checked exactly — every cube-covariant f(empty)=0 map is classified as filler or not"
    )
    print(
        "per_block: checked exactly — the unique support-26 filler is named by orbit bits and F_cut membership"
    )
    print(
        "lattice_wide: checked and not executed — no Z^3-wide formation law or Admissibility rewrite is claimed"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
