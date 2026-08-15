#!/usr/bin/env python3
"""Halt dynamics of the unique support-26 1-site filler f_min.

On the twelve-vertex two-cube with seed (0,0,0) and off-patch occupancy 0,
f_min(c)=1 iff n_both(c)=0 and some axis is unbalanced.  Reconfirm it is
the unique support-26 cube-covariant 1-site filler, then report its halt
tick and lock history.  f_L1 is the unbalanced-axis predicate (some
n_mu != 0), never Hamming |c|_1 mod 2.  The history is displayed, not
adopted, and is not leftover-character of the #6407 identity.
"""

from __future__ import annotations

from itertools import permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/F_MIN_ONE_SITE_HALT_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/F_MIN_ONE_SITE_HALT_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
F_MIN_TUPLE: tuple[int, ...] = (1, 0, 1, 1, 0)
L1_TUPLE: tuple[int, ...] = (1, 0, 1, 1, 1)
L1_HISTORY: tuple[int, ...] = (1, 4, 8, 11, 12)


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


def f_min(config: Config) -> int:
    """1 iff n_both=0 and some axis is unbalanced.  Not f_L1."""
    n_unbalanced, n_both, _n_empty = axis_type(config)
    return int(n_both == 0 and n_unbalanced >= 1)


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


def predicate_from_assignment(assignment: dict[OrbitType, int], type_of: dict[Config, OrbitType]):
    def predicate(config: Config) -> int:
        return assignment[type_of[config]]

    return predicate


def in_f_cut_pred(predicate) -> bool:
    if int(predicate(EMPTY)) != 0 or int(predicate(FULL)) != 0:
        return False
    return all(
        int(predicate(config)) == int(predicate(tuple(1 - bit for bit in config)))  # type: ignore[arg-type]
        for config in product((0, 1), repeat=6)
    )


def support_of(predicate) -> int:
    return sum(int(predicate(config)) for config in product((0, 1), repeat=6))


def census_one_site_fillers(
    orbit_types: tuple[OrbitType, ...],
    orbits: dict[OrbitType, frozenset[Config]],
    empty_type: OrbitType,
) -> list[tuple[tuple[int, ...], int, tuple[int, ...], int]]:
    type_of = {config: orbit_type for orbit_type, members in orbits.items() for config in members}
    free_types = [orbit_type for orbit_type in orbit_types if orbit_type != empty_type]
    fillers: list[tuple[tuple[int, ...], int, tuple[int, ...], int]] = []
    for mask in range(1 << len(free_types)):
        assignment = {empty_type: 0}
        for rank, orbit_type in enumerate(free_types):
            assignment[orbit_type] = (mask >> rank) & 1
        n_locks, halt, _first_empty, history = run_predicate(
            predicate_from_assignment(assignment, type_of)
        )
        if n_locks == 12:
            bits = tuple(assignment[orbit_type] for orbit_type in orbit_types)
            supp = sum(assignment[orbit_type] * len(orbits[orbit_type]) for orbit_type in orbit_types)
            fillers.append((bits, supp, history, halt))
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
    empty_type = axis_type(EMPTY)
    full_type = axis_type(FULL)

    min_bits = bits_from_predicate(f_min, orbit_types, orbits)
    l1_bits = bits_from_predicate(f_L1, orbit_types, orbits)
    ham_bits = bits_from_predicate(f_hamming, orbit_types, orbits)
    min_assign = dict(zip(orbit_types, min_bits, strict=True))
    l1_assign = dict(zip(orbit_types, l1_bits, strict=True))
    min_named = named_tuple_from_assignment(min_assign)
    l1_named = named_tuple_from_assignment(l1_assign)
    min_supp = support_of(f_min)
    l1_supp = support_of(f_L1)
    min_locks, min_halt, min_first_empty, min_history = run_predicate(f_min)
    l1_locks, l1_halt, l1_first_empty, l1_history = run_predicate(f_L1)
    ham_locks, _ham_halt, _ham_first, _ham_history = run_predicate(f_hamming)
    histories_equal = min_history == l1_history

    fillers = census_one_site_fillers(orbit_types, orbits, empty_type)
    supports = [supp for _bits, supp, _hist, _halt in fillers]
    min_support = min(supports)
    sparse = [row for row in fillers if row[1] == min_support]

    print(f"n_rotations={len(ROTATIONS)}")
    print(f"n_orbits={len(orbit_types)}")
    print(f"N_fill={len(fillers)}")
    print(f"m_supp={min_support} N_min={len(sparse)}")
    print(f"f_min_tuple={dict(zip(BIT_NAMES, min_named))}")
    print(f"f_min_supp={min_supp} in_F_cut={in_f_cut_pred(f_min)}")
    print(f"f_min_locks={min_locks} halt={min_halt} history={min_history}")
    print(f"f_L1_locks={l1_locks} halt={l1_halt} history={l1_history}")
    print(f"histories_equal={histories_equal}")

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required note-plus-axiom string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/F_MIN_ONE_SITE_HALT_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and 'AUDIT_INPUT_PATHS = (\n'
        '    "docs/F_MIN_ONE_SITE_HALT_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
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
        "thm1-two-cube-twelve",
        "the two-cube has twelve vertices and contains the seed",
        len(TWO_CUBE) == 12 and len(set(TWO_CUBE)) == 12 and SEED in TWO_CUBE,
    )
    checks.check(
        "thm1-f-min-definition",
        "f_min is 1 iff n_both=0 and n_unbalanced>=1",
        all(
            f_min(config) == int(axis_type(config)[1] == 0 and axis_type(config)[0] >= 1)
            for config in product((0, 1), repeat=6)
        ),
    )
    checks.check(
        "thm1-unique-support-26",
        "f_min is the unique support-26 1-site filler",
        len(fillers) == 96
        and min_support == 26
        and len(sparse) == 1
        and min_supp == 26
        and min_named == F_MIN_TUPLE
        and min_bits == sparse[0][0]
        and min_named != l1_named
        and l1_supp == 56,
    )
    checks.check(
        "thm1-not-in-f-cut",
        "f_min is not in F_cut (fails complement-even)",
        not in_f_cut_pred(f_min)
        and min_assign[empty_type] == 0
        and min_assign[full_type] == 0
        and min_assign[(1, 0, 2)] != min_assign[complement_type((1, 0, 2))],
    )
    checks.check(
        "thm1-f-min-fills",
        "f_min fills: |locks_halt|=12 with reported T and history",
        min_locks == 12
        and min_halt == 4
        and min_history == (1, 4, 8, 11, 12)
        and not min_first_empty
        and f"T = {min_halt}" in note
        and f"({', '.join(str(n) for n in min_history)})" in note,
    )
    checks.check(
        "thm2-f-L1-is-unbalanced-axis",
        "f_L1 is 1 iff some axis has c_+ != c_- (n != 0)",
        all(
            f_L1(config) == int(axis_type(config)[0] >= 1)
            for config in product((0, 1), repeat=6)
        ),
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
        and l1_history == L1_HISTORY
        and l1_named == L1_TUPLE
        and not l1_first_empty,
    )
    checks.check(
        "thm2-histories-equal",
        "f_min lock history equals the L1 history on this seed",
        histories_equal
        and min_history == l1_history
        and min_halt == l1_halt
        and min_named != l1_named
        and "equals the L1 history" in note,
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
        "bounded theorem, displayed-not-adopted halt history, and machine status",
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
        "f-min-definition-in-note",
        "the note defines f_min as nonempty n_both=0",
        "`f_min(c)=1` if and only if `n_both(c)=0` and some axis is unbalanced" in note_flat
        and "(1, 0, 1, 1, 0)" in note
        and "support 26" in note,
    )
    checks.check(
        "no-axiom-edit",
        "the history is not written into Admissibility",
        "Do not write f_min into Admissibility" in note
        and "no axiom or approved primitive is added" in note
        and "hypothetical_axiom_status" in note,
    )
    checks.check(
        "not-leftover-6407",
        "the residual is the halt history, not leftover-character of the identity",
        "Not leftover-character of #6407" in note
        and "identity only" in note,
    )
    checks.check(
        "not-other-member-dynamics",
        "the residual is not Hamming, vertex3, or f_two 2-site dynamics",
        "Not Hamming-parity formation dynamics" in note
        and "Not vertex3-orbit indicator dynamics" in note
        and "Not f_two face-diagonal 2-site fill" in note,
    )
    checks.check(
        "off-patch-zero",
        "off-patch occupancy is the explicit 0 default, not a blank-block",
        "off-patch occupancy `0`" in note and "blank-block is a different rule" in note,
    )
    checks.check(
        "claim-scope-and-history",
        "claim_scope reports T and the lock history and does not adopt f_min",
        "unique support-26 1-site filler f_min" in note
        and "halts at tick T = 4" in note
        and "lock history (1, 4, 8, 11, 12)" in note
        and "Displayed, not adopted" in note,
    )

    print("per_element: checked exactly — each of the 64 neighbor 6-tuples is assigned its axis-type orbit")
    print("per_site: checked exactly — each of the twelve two-cube vertices uses the same six-direction stencil")
    print("per_mode: checked exactly — every cube-covariant empty-silent map is classified as filler or not")
    print("per_block: checked exactly — the unique support-26 filler is run to a fixed point from the 1-site seed")
    print("lattice_wide: checked and not executed — no Z^3-wide formation law or Admissibility rewrite is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
