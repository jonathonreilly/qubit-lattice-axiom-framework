#!/usr/bin/env python3
"""AND of L1 remaining orbit bits among F_cut maps that fill from the line.

Reconstruct the 24 proper cube rotations, the ten axis-type orbits, and the
32-element three-cut class F_cut. Fill means halt locks = 12 on the
twelve-vertex two-cube with off-patch occupancy 0. The seed is the 3-site
long-axis line S = {(0,0,0),(1,0,0),(2,0,0)}, not a 1-site seed.
f_L1 is the unbalanced-axis predicate (some n_mu != 0), never Hamming
|c|_1 mod 2. N_fill_line counts F_cut fillers from S. N_and_line counts
those fillers matching L1 remaining bits (opp2=0, adj2=1, vertex3=1,
mixed3=1; wt1=1).
"""

from __future__ import annotations

from itertools import permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/F_CUT_LINE_SEED_L1_BIT_AND_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/F_CUT_LINE_SEED_L1_BIT_AND_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
SEED: frozenset[Site] = frozenset(((0, 0, 0), (1, 0, 0), (2, 0, 0)))

# Remaining L1 bits plus the first-wave bit. Complements are forced.
BIT_NAMES: tuple[str, ...] = ("wt1", "opp2", "adj2", "vertex3", "mixed3")
BIT_TYPES: dict[str, OrbitType] = {
    "wt1": (1, 0, 2),
    "opp2": (0, 1, 2),
    "adj2": (2, 0, 1),
    "vertex3": (3, 0, 0),
    "mixed3": (1, 1, 1),
}
COMPLEMENT_NAMES: dict[str, str] = {
    "wt1": "wt5",
    "opp2": "opp4",
    "adj2": "adj4",
}
L1_TUPLE: tuple[int, ...] = (1, 0, 1, 1, 1)


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


def run_predicate(predicate) -> tuple[int, int, bool, tuple[int, ...]]:
    locked = set(SEED)
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


def census_f_cut_line_fillers(
    orbit_types: tuple[OrbitType, ...],
    orbits: dict[OrbitType, frozenset[Config]],
    empty_type: OrbitType,
    full_type: OrbitType,
) -> list[tuple[int, ...]]:
    type_of = {config: orbit_type for orbit_type, members in orbits.items() for config in members}
    free_pairs, free_fixed = f_cut_free_data(orbit_types, empty_type, full_type)
    n_free = len(free_pairs) + len(free_fixed)
    fillers: list[tuple[int, ...]] = []
    for mask in range(1 << n_free):
        assignment = {empty_type: 0, full_type: 0}
        for rank, pair in enumerate(free_pairs):
            value = (mask >> rank) & 1
            assignment[pair[0]] = value
            assignment[pair[1]] = value
        for rank, orbit_type in enumerate(free_fixed):
            assignment[orbit_type] = (mask >> (len(free_pairs) + rank)) & 1
        bits = tuple(assignment[orbit_type] for orbit_type in orbit_types)
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
    empty_type = axis_type(EMPTY)
    full_type = axis_type(FULL)
    free_pairs, free_fixed = f_cut_free_data(orbit_types, empty_type, full_type)
    n_free = len(free_pairs) + len(free_fixed)
    n_cut = 1 << n_free

    l1_bits = bits_from_predicate(f_L1, orbit_types, orbits)
    ham_bits = bits_from_predicate(f_hamming, orbit_types, orbits)
    l1_assign = dict(zip(orbit_types, l1_bits, strict=True))
    l1_named = named_tuple_from_assignment(l1_assign)
    l1_locks, l1_halt, l1_first_empty, l1_history = run_predicate(f_L1)
    ham_locks, _ham_halt, _ham_first, _ham_history = run_predicate(f_hamming)

    fillers = census_f_cut_line_fillers(orbit_types, orbits, empty_type, full_type)
    filler_named = [
        named_tuple_from_assignment(dict(zip(orbit_types, bits, strict=True)))
        for bits in fillers
    ]
    n_fill_line = len(fillers)
    matches = [named for named in filler_named if named == L1_TUPLE]
    n_and_line = len(matches)

    print(f"n_rotations={len(ROTATIONS)}")
    print(f"n_orbits={len(orbit_types)}")
    print(f"|F_cut|={n_cut}")
    print(f"SEED={tuple(sorted(SEED))}")
    print(f"N_fill_line={n_fill_line}")
    print(f"L1_tuple={dict(zip(BIT_NAMES, l1_named))}")
    print(f"N_and_line={n_and_line}")
    print(f"f_L1_locks={l1_locks} halt={l1_halt} history={l1_history}")
    print(f"hamming_locks={ham_locks}")

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required note-plus-axiom string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/F_CUT_LINE_SEED_L1_BIT_AND_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and 'AUDIT_INPUT_PATHS = (\n'
        '    "docs/F_CUT_LINE_SEED_L1_BIT_AND_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
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
        "thm1-line-seed",
        "start locked is the 3-site long-axis line, not a 1-site seed",
        SEED == frozenset(((0, 0, 0), (1, 0, 0), (2, 0, 0)))
        and len(SEED) == 3
        and SEED.issubset(set(TWO_CUBE))
        and all(site[1] == 0 and site[2] == 0 for site in SEED)
        and {site[0] for site in SEED} == {0, 1, 2},
    )
    checks.check(
        "thm1-f-L1-in-f-cut-fills-from-S",
        "f_L1 is in F_cut and fills from S with lock history (3, 9, 12)",
        in_f_cut(l1_bits, orbit_types, empty_type, full_type)
        and l1_bits in fillers
        and l1_named == L1_TUPLE
        and l1_locks == 12
        and not l1_first_empty
        and l1_halt == 2
        and l1_history == (3, 9, 12),
    )
    checks.check(
        "thm2-n-fill-line",
        f"N_fill_line = {n_fill_line} F_cut maps fill from the 3-site line",
        n_fill_line == len(set(fillers))
        and n_fill_line == 8
        and n_cut == 32
        and f"N_fill_line = {n_fill_line}" in note,
    )
    checks.check(
        "thm2-n-and-line",
        f"N_and_line = {n_and_line} fillers match the L1 remaining-bit tuple",
        n_and_line == sum(1 for named in filler_named if named == L1_TUPLE)
        and n_and_line == 1
        and f"N_and_line = {n_and_line}" in note,
    )
    checks.check(
        "thm3-unique-no-second-match",
        "N_and_line=1; no second line-seed filler matches the tuple",
        n_and_line == 1
        and filler_named.count(L1_TUPLE) == 1
        and ham_bits not in fillers
        and ham_locks != 12,
    )
    checks.check(
        "thm1-complement-even-fixed",
        "wt5/adj4/opp4 equal wt1/adj2/opp2 by complement-even",
        all(
            dict(zip(orbit_types, bits, strict=True))[BIT_TYPES[name]]
            == dict(zip(orbit_types, bits, strict=True))[complement_type(BIT_TYPES[name])]
            for bits in fillers
            for name in ("wt1", "opp2", "adj2")
        )
        and COMPLEMENT_NAMES["wt1"] == "wt5"
        and COMPLEMENT_NAMES["adj2"] == "adj4"
        and COMPLEMENT_NAMES["opp2"] == "opp4",
    )
    checks.check(
        "thm1-two-cube-twelve",
        "the two-cube has twelve vertices and contains the line seed",
        len(TWO_CUBE) == 12
        and len(set(TWO_CUBE)) == 12
        and SEED.issubset(set(TWO_CUBE)),
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
        "bounded theorem, displayed-not-adopted line-seed AND, and machine status",
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
        "the bit tuple is not written into Admissibility",
        "Do not write the tuple into Admissibility" in note
        and "no axiom or approved primitive is added" in note
        and "hypothetical_axiom_status" in note,
    )
    checks.check(
        "not-leftover-6404",
        "the residual is the line-seed AND, not leftover-character of #6404",
        "Not leftover-character of #6404" in note
        and "different seed" in note
        and "Not leftover-character of the 1-site remaining-bit AND" in note,
    )
    checks.check(
        "not-occupancy-step-or-fill2site",
        "the census is not an occupancy-step clone and not the 2-site face-diagonal fill",
        "Not an occupancy-step clone" in note
        and "not a new 10" in note
        and "Not fill2site" in note
        and "face-diagonal" in note
        and "no AND" in note,
    )
    checks.check(
        "off-patch-zero",
        "off-patch occupancy is the explicit 0 default, not a blank-block",
        "off-patch occupancy `0`" in note and "blank-block is a different rule" in note,
    )
    checks.check(
        "claim-scope-and-n-and-line",
        "claim_scope reports N_and_line among line-seed F_cut fillers and does not adopt",
        "Among F_cut maps that fill the two-cube from the 3-site long-axis seed" in note
        and "N_and_line match L1 remaining orbit bits" in note
        and "Displayed, not adopted" in note,
    )

    print("per_element: checked exactly — each of the 64 neighbor 6-tuples is assigned its axis-type orbit")
    print("per_site: checked exactly — each of the twelve two-cube vertices uses the same six-direction stencil")
    print("per_mode: checked exactly — every F_cut map is classified as a line-seed filler or not, then filtered by the bit tuple")
    print("per_block: checked exactly — N_fill_line and N_and_line are the fill and AND cardinalities on this seed")
    print("lattice_wide: checked and not executed — no Z^3-wide formation law or Admissibility rewrite is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
