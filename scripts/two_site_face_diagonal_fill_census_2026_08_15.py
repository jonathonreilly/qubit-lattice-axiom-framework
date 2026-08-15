#!/usr/bin/env python3
"""Exact 2-site face-diagonal fill census of the 512 cube-covariant maps.

The class is cube-covariant f with f(empty)=0. Dynamics are occupancy-to-lock
on the twelve-vertex two-cube from seed {(0,0,0),(1,1,0)} with off-patch
occupancy 0. f_L1 is the unbalanced-axis predicate (some n_mu != 0), never
Hamming |c|_1 mod 2. f_two is u>=2, never f_L1.
"""

from __future__ import annotations

from itertools import permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/TWO_SITE_FACE_DIAGONAL_FILL_CENSUS_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/TWO_SITE_FACE_DIAGONAL_FILL_CENSUS_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
SEED: frozenset[Site] = frozenset(((0, 0, 0), (1, 1, 0)))
FORCED_FILL_TYPES: frozenset[OrbitType] = frozenset(
    ((1, 0, 2), (2, 0, 1), (3, 0, 0))
)


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


def f_two(config: Config) -> int:
    """1 iff at least two axes are unbalanced.  Not f_L1."""
    return int(axis_type(config)[0] >= 2)


def f_hamming(config: Config) -> int:
    return sum(config) % 2


def f_any(config: Config) -> int:
    """Displayed extra filler: 1 iff the 6-tuple is nonempty.  Not adopted."""
    return int(config != EMPTY)


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


def run_predicate(predicate) -> tuple[int, int, bool, tuple[int, ...], frozenset[Site]]:
    locked = set(SEED)
    history = [len(locked)]
    first_wave = evolve(locked, predicate)
    first_wave_empty = first_wave == locked
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
    return len(locked), halt_tick, first_wave_empty, tuple(history), frozenset(first_wave - SEED)


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
    empty_type: OrbitType,
) -> tuple[int, list[tuple[int, ...]]]:
    type_of = {config: orbit_type for orbit_type, members in orbits.items() for config in members}
    free_types = [orbit_type for orbit_type in orbit_types if orbit_type != empty_type]
    fillers: list[tuple[int, ...]] = []
    for mask in range(1 << len(free_types)):
        assignment = {empty_type: 0}
        for rank, orbit_type in enumerate(free_types):
            assignment[orbit_type] = (mask >> rank) & 1
        bits = tuple(assignment[orbit_type] for orbit_type in orbit_types)
        n_locks, _halt, _first_empty, _history, _wave = run_predicate(
            predicate_from_bits(bits, orbit_types, type_of)
        )
        if n_locks == 12:
            fillers.append(bits)
    return len(fillers), fillers


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
    n_maps = 1 << (len(orbit_types) - 1)

    l1_bits = bits_from_predicate(f_L1, orbit_types, orbits)
    two_bits = bits_from_predicate(f_two, orbit_types, orbits)
    ham_bits = bits_from_predicate(f_hamming, orbit_types, orbits)
    any_bits = bits_from_predicate(f_any, orbit_types, orbits)
    l1_locks, l1_halt, l1_first_empty, l1_history, l1_wave = run_predicate(f_L1)
    two_locks, two_halt, two_first_empty, two_history, two_wave = run_predicate(f_two)
    any_locks, any_halt, any_first_empty, any_history, _any_wave = run_predicate(f_any)
    n_fill, fillers = census_fillers(orbit_types, orbits, empty_type)
    free_unforced = [
        orbit_type
        for orbit_type in orbit_types
        if orbit_type != empty_type and orbit_type not in FORCED_FILL_TYPES
    ]
    forced_class: list[tuple[int, ...]] = []
    for mask in range(1 << len(free_unforced)):
        assignment = {empty_type: 0}
        for orbit_type in FORCED_FILL_TYPES:
            assignment[orbit_type] = 1
        for rank, orbit_type in enumerate(free_unforced):
            assignment[orbit_type] = (mask >> rank) & 1
        forced_class.append(tuple(assignment[orbit_type] for orbit_type in orbit_types))
    forced_ok = n_fill == 64 and set(fillers) == set(forced_class)

    print(f"n_rotations={len(ROTATIONS)}")
    print(f"n_orbits={len(orbit_types)}")
    print("orbit_types_and_sizes=" + ",".join(f"{t}:{orbit_sizes[t]}" for t in orbit_types))
    print(f"n_maps={n_maps}")
    print(f"N_fill_2={n_fill}")
    print(f"f_L1_bits={l1_bits}")
    print(f"f_L1_locks={l1_locks} halt={l1_halt} history={l1_history}")
    print(f"f_two_bits={two_bits}")
    print(f"f_two_locks={two_locks} halt={two_halt} history={two_history} wave={sorted(two_wave)}")
    print(f"f_any_locks={any_locks} halt={any_halt} history={any_history}")

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required note-plus-axiom string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/TWO_SITE_FACE_DIAGONAL_FILL_CENSUS_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and 'AUDIT_INPUT_PATHS = (\n'
        '    "docs/TWO_SITE_FACE_DIAGONAL_FILL_CENSUS_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
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
        "thm1-five-twelve-maps",
        "cube-covariant maps with f(empty)=0 number 512",
        n_maps == 512 and empty_type == (0, 0, 3) and full_type == (0, 3, 0),
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
        not in self_source.split("def f_L1", 1)[1].split("def f_two", 1)[0],
    )
    checks.check(
        "thm1-f-L1-fills",
        "f_L1 fills all twelve vertices from the face-diagonal 2-site seed",
        l1_locks == 12
        and l1_halt == 3
        and l1_history == (2, 7, 11, 12)
        and not l1_first_empty
        and l1_bits in fillers,
    )
    checks.check(
        "thm1-two-cube-and-seed",
        "the two-cube has twelve vertices and contains both seed sites",
        len(TWO_CUBE) == 12
        and len(set(TWO_CUBE)) == 12
        and SEED <= set(TWO_CUBE)
        and (1, 1, 0) in TWO_CUBE,
    )
    checks.check(
        "thm2-f-two-is-u-at-least-two",
        "f_two is 1 iff at least two axes are unbalanced",
        all(
            f_two(config) == int(axis_type(config)[0] >= 2)
            for config in product((0, 1), repeat=6)
        )
        and two_bits != l1_bits,
    )
    checks.check(
        "thm2-f-two-does-not-fill",
        "f_two halts with four locks and does not fill",
        two_locks == 4
        and two_halt == 1
        and two_history == (2, 4)
        and two_wave == frozenset(((1, 0, 0), (0, 1, 0)))
        and not two_first_empty
        and two_bits not in fillers,
    )
    checks.check(
        "thm3-n-fill-2",
        f"N_fill_2 = {n_fill} exactly",
        n_fill == 64 and n_fill == len(fillers) and f"N_fill_2 = {n_fill}" in note,
    )
    checks.check(
        "thm3-not-unique",
        "N_fill_2 > 1; f_L1 is not the unique 2-site filler",
        n_fill > 1 and l1_bits in fillers and any_bits in fillers and any_bits != l1_bits,
    )
    checks.check(
        "thm3-displayed-other-filler",
        "displayed f_any fills, vanishes on empty, and is distinct from f_L1",
        any_bits != l1_bits
        and any_bits[orbit_types.index(empty_type)] == 0
        and any_locks == 12
        and any_halt == 3
        and any_history == (2, 7, 11, 12)
        and not any_first_empty
        and forced_ok,
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
        "bounded theorem, displayed-not-adopted uniqueness failure, and machine status",
        "**Type:** bounded_theorem" in note
        and "actual_current_surface_status: bounded-support" in note
        and "f_L1 is not unique" in note
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
        "note-reports-census",
        "the note reports N_fill_2 = 64 and a second displayed filler",
        "N_fill_2 = 64" in note
        and "displayed second filler `f_any`" in note
        and "f_L1 is not unique" in note,
    )
    checks.check(
        "no-axiom-edit",
        "the theorem proposes no axiom change",
        "no axiom or approved primitive is added" in note
        and "hypothetical_axiom_status" in note,
    )
    checks.check(
        "off-patch-zero",
        "off-patch occupancy is the explicit 0 default, not a blank-block",
        "off-patch occupancy `0`" in note and "blank-block is a different rule" in note,
    )
    checks.check(
        "not-leftover-one-site-or-ftwo-run",
        "the residual is the 2-site fill count, not the 1-site census or an f_two halt run",
        "Not leftover-character of the 1-site fill census" in note
        and "Not a second f_two face-diagonal halt run" in note,
    )

    print(
        "per_element: checked exactly — each of the 64 neighbor 6-tuples is assigned its axis-type orbit"
    )
    print(
        "per_site: checked exactly — each of the twelve two-cube vertices uses the same six-direction stencil"
    )
    print(
        "per_mode: checked exactly — every cube-covariant f with f(empty)=0 is run to a fixed point"
    )
    print(
        "per_block: checked exactly — N_fill_2 is the 2-site fill cardinality on this patch"
    )
    print(
        "lattice_wide: checked and not executed — no Z^3-wide formation law or physical Admissibility selector is claimed"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
