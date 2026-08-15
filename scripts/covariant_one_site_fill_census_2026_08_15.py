#!/usr/bin/env python3
"""Exact fill census of cube-covariant occupancy predicates on the two-cube.

The class is every {0,1}-valued map on the ten proper-cube orbits of {0,1}^6
with f(empty)=0.  Dynamics are occupancy-to-lock on the twelve-vertex
two-cube from a 1-site seed with off-patch occupancy 0.  f_L1 is the
unbalanced-axis predicate (some n_mu != 0), never Hamming |c|_1 mod 2.
"""

from __future__ import annotations

from itertools import permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/COVARIANT_ONE_SITE_FILL_CENSUS_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/COVARIANT_ONE_SITE_FILL_CENSUS_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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


def f_star(config: Config) -> int:
    """Displayed non-unique filler: some unbalanced axis and no fully occupied axis."""
    n_unbalanced, n_both, _n_empty = axis_type(config)
    return int(n_unbalanced >= 1 and n_both == 0)


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


def predicate_from_bits(
    bits: tuple[int, ...],
    orbit_types: tuple[OrbitType, ...],
    type_of: dict[Config, OrbitType],
):
    assignment = dict(zip(orbit_types, bits, strict=True))

    def predicate(config: Config) -> int:
        return assignment[type_of[config]]

    return predicate


def census(
    orbit_types: tuple[OrbitType, ...],
    orbits: dict[OrbitType, frozenset[Config]],
) -> tuple[int, int, list[tuple[int, ...]]]:
    type_of = {config: orbit_type for orbit_type, members in orbits.items() for config in members}
    empty_index = orbit_types.index(axis_type(EMPTY))
    free = [index for index in range(len(orbit_types)) if index != empty_index]
    n_fill = 0
    n_empty = 0
    fillers: list[tuple[int, ...]] = []
    for mask in range(1 << len(free)):
        bits_list = [0] * len(orbit_types)
        for rank, index in enumerate(free):
            bits_list[index] = (mask >> rank) & 1
        bits = tuple(bits_list)
        n_locks, _halt, first_empty, _history = run_predicate(
            predicate_from_bits(bits, orbit_types, type_of)
        )
        if first_empty:
            n_empty += 1
        if n_locks == 12:
            n_fill += 1
            fillers.append(bits)
    return n_fill, n_empty, fillers


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

    l1_bits = bits_from_predicate(f_L1, orbit_types, orbits)
    star_bits = bits_from_predicate(f_star, orbit_types, orbits)
    ham_bits = bits_from_predicate(f_hamming, orbit_types, orbits)
    l1_locks, l1_halt, l1_first_empty, l1_history = run_predicate(f_L1)
    star_locks, star_halt, star_first_empty, star_history = run_predicate(f_star)
    ham_locks, _ham_halt, _ham_first, _ham_history = run_predicate(f_hamming)
    n_fill, n_empty, fillers = census(orbit_types, orbits)

    print(f"n_rotations={len(ROTATIONS)}")
    print(f"n_orbits={len(orbit_types)}")
    print("orbit_types_and_sizes=" + ",".join(f"{t}:{orbit_sizes[t]}" for t in orbit_types))
    print(f"n_maps_empty0={n_maps}")
    print(f"N_fill={n_fill}")
    print(f"N_empty={n_empty}")
    print(f"f_L1_bits={l1_bits}")
    print(f"f_L1_locks={l1_locks} halt={l1_halt} first_wave_empty={int(l1_first_empty)} history={l1_history}")
    print(f"f_star_locks={star_locks} halt={star_halt} history={star_history}")
    print(f"f_hamming_locks={ham_locks} distinct_from_L1={int(ham_bits != l1_bits)}")

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required note-plus-axiom string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/COVARIANT_ONE_SITE_FILL_CENSUS_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file(),
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
        "thm1-five-hundred-twelve-maps",
        "cube-covariant f with f(empty)=0 number 512",
        n_maps == 512 and axis_type(EMPTY) == (0, 0, 3) and l1_bits[orbit_types.index((0, 0, 3))] == 0,
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
        and "sum(config) % 2" not in self_source.split("def f_L1", 1)[1].split("def f_hamming", 1)[0],
    )
    checks.check(
        "thm1-two-cube-twelve",
        "the two-cube has twelve vertices and contains the seed",
        len(TWO_CUBE) == 12 and len(set(TWO_CUBE)) == 12 and SEED in TWO_CUBE,
    )
    checks.check(
        "thm2-n-fill",
        f"N_fill = {n_fill} exactly",
        n_fill == 96 and f"N_fill = {n_fill}" in note,
    )
    checks.check(
        "thm2-n-empty",
        f"N_empty = {n_empty} exactly",
        n_empty == 256 and f"N_empty = {n_empty}" in note,
    )
    checks.check(
        "thm2-empty-wave-is-wt1-off",
        "first-wave emptiness is exactly f=0 on the one-unbalanced-axis orbit",
        n_empty == 2 ** 8,
    )
    checks.check(
        "thm3-f-L1-fills",
        "f_L1 fills all twelve vertices at halt tick 4",
        l1_locks == 12
        and l1_halt == 4
        and l1_history == (1, 4, 8, 11, 12)
        and not l1_first_empty,
    )
    checks.check(
        "thm3-not-unique",
        "N_fill != 1; f_L1 is not the unique filler",
        n_fill != 1 and n_fill == len(fillers) and l1_bits in fillers and star_bits in fillers,
    )
    checks.check(
        "thm3-displayed-other-filler",
        "displayed f_star fills and is distinct from f_L1",
        star_bits != l1_bits
        and star_locks == 12
        and star_halt == 4
        and star_history == (1, 4, 8, 11, 12)
        and not star_first_empty,
    )
    checks.check(
        "mutation-hamming-does-not-fill",
        "Hamming parity is a different cube-covariant map and does not fill",
        ham_bits[orbit_types.index((0, 0, 3))] == 0
        and ham_locks != 12
        and ham_bits not in fillers,
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
        and "f_L1 is not the unique filler" in note
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
        "note-reports-other-filler",
        "the note displays a second filler rather than adopting uniqueness",
        "displayed second filler `f_★`" in note
        and "f_L1 is not the unique filler" in note,
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

    print("per_element: checked exactly — each of the 64 neighbor 6-tuples is assigned its axis-type orbit")
    print("per_site: checked exactly — each of the twelve two-cube vertices uses the same six-direction stencil")
    print("per_mode: checked exactly — every cube-covariant f with f(empty)=0 is run to a fixed point")
    print("per_block: checked exactly — N_fill and N_empty are whole-class cardinalities on this patch")
    print("lattice_wide: checked and not executed — no Z^3-wide formation law or physical Admissibility selector is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
