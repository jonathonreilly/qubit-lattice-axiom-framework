#!/usr/bin/env python3
"""Halt dynamics of the unique support-36 F_cut 1-site filler.

On the twelve-vertex two-cube with seed (0,0,0) and off-patch occupancy 0,
f_cutmin is the unique F_cut 1-site filler with remaining-bit tuple
(wt1, opp2, adj2, vertex3, mixed3)=(1,0,1,0,0).  Reconfirm it is the
unique support-36 F_cut 1-site filler, then report its halt tick and lock
history.  f_L1 is the unbalanced-axis predicate (some n_mu != 0), never
Hamming |c|_1 mod 2.  The history is displayed, not adopted, and is not
leftover-character of the #6414 support identity or of #6411 (f_min).
"""

from __future__ import annotations

from itertools import permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
AUDIT_INPUT_PATHS = (
    "docs/F_CUT_SPARSEST_ONE_SITE_HALT_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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

WT1: OrbitType = (1, 0, 2)
OPP2: OrbitType = (0, 1, 2)
ADJ2: OrbitType = (2, 0, 1)
VERTEX3: OrbitType = (3, 0, 0)
MIXED3: OrbitType = (1, 1, 1)
CUTMIN_BITS: BitTuple = (1, 0, 1, 0, 0)
L1_BITS: BitTuple = (1, 0, 1, 1, 1)
F_MIN_BITS: BitTuple = (1, 0, 1, 1, 0)
ORBIT_PAIR_SIZE = {
    WT1: 12,  # (1,0,2) and (1,2,0)
    OPP2: 6,  # (0,1,2) and (0,2,1)
    ADJ2: 24,  # (2,0,1) and (2,1,0)
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


def f_min(config: Config) -> int:
    """Unique support-26 filler among the 96; outside F_cut. Not adopted."""
    n_unbalanced, n_both, _n_empty = axis_type(config)
    return int(n_both == 0 and n_unbalanced >= 1)


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


def run_predicate(predicate) -> tuple[int, int, tuple[int, ...]]:
    locked = {SEED}
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


def census_f_cut_fillers(
    type_of: dict[Config, OrbitType],
) -> list[tuple[BitTuple, int, int, tuple[int, ...]]]:
    fillers: list[tuple[BitTuple, int, int, tuple[int, ...]]] = []
    for mask in range(32):
        bits: BitTuple = (
            (mask >> 0) & 1,
            (mask >> 1) & 1,
            (mask >> 2) & 1,
            (mask >> 3) & 1,
            (mask >> 4) & 1,
        )
        n_locks, halt_tick, history = run_predicate(predicate_from_bits(bits, type_of))
        if n_locks == 12:
            fillers.append((bits, support_of_bits(bits), halt_tick, history))
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
    orbit_sizes = {orbit_kind: len(orbits[orbit_kind]) for orbit_kind in orbit_types}
    type_of = {
        config: orbit_kind for orbit_kind, members in orbits.items() for config in members
    }
    free_pairs, free_fixed = f_cut_free_data(orbit_types)
    n_free = len(free_pairs) + len(free_fixed)
    n_cut = 1 << n_free

    l1_bits = bits_from_predicate(f_L1, orbit_types, orbits)
    ham_bits = bits_from_predicate(f_hamming, orbit_types, orbits)
    min_bits = bits_from_predicate(f_min, orbit_types, orbits)
    cutmin_pred = predicate_from_bits(CUTMIN_BITS, type_of)
    cutmin_locks, cutmin_halt, cutmin_history = run_predicate(cutmin_pred)
    l1_locks, l1_halt, l1_history = run_predicate(f_L1)
    ham_locks, _ham_halt, ham_history = run_predicate(f_hamming)
    min_locks, _min_halt, _min_history = run_predicate(f_min)
    cutmin_support = support_of_bits(CUTMIN_BITS)
    l1_support = support_of_bits(l1_bits)
    l1_support_direct = sum(1 for cell in product((0, 1), repeat=6) if f_L1(cell))
    cutmin_support_direct = sum(
        1 for cell in product((0, 1), repeat=6) if cutmin_pred(cell)
    )
    histories_equal = cutmin_history == l1_history

    fillers = census_f_cut_fillers(type_of)
    n_fill = len(fillers)
    supports = [support for _bits, support, _halt, _history in fillers]
    m_cut = min(supports)
    n_min_cut = sum(1 for support in supports if support == m_cut)
    min_bits_list = [bits for bits, support, _halt, _history in fillers if support == m_cut]
    displayed_min = min_bits_list[0] if len(min_bits_list) == 1 else None
    cutmin_row = next(row for row in fillers if row[0] == CUTMIN_BITS)

    print(f"n_rotations={len(ROTATIONS)}")
    print(f"n_orbits={len(orbit_types)}")
    print(f"N_free={n_free}")
    print(f"|F_cut|={n_cut}")
    print(f"N_fill_cut={n_fill}")
    print(f"f_cutmin_bits={CUTMIN_BITS} supp={cutmin_support}")
    print(f"f_cutmin_locks={cutmin_locks} halt={cutmin_halt} history={cutmin_history}")
    print(f"f_L1_bits={l1_bits} supp={l1_support} locks={l1_locks} history={l1_history}")
    print(f"histories_equal={histories_equal}")
    print(f"f_hamming_bits={ham_bits} locks={ham_locks} history={ham_history}")
    print(
        f"f_min_bits={min_bits} in_F_cut={predicate_in_f_cut(f_min)} locks={min_locks}"
    )
    print(f"m_cut={m_cut} N_min_cut={n_min_cut} displayed_minimizer={displayed_min}")

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required note-plus-axiom string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/F_CUT_SPARSEST_ONE_SITE_HALT_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and 'AUDIT_INPUT_PATHS = (\n'
        '    "docs/F_CUT_SPARSEST_ONE_SITE_HALT_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
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
        and len(free_fixed) == 2,
    )
    checks.check(
        "thm1-eight-fillers",
        "exactly eight F_cut maps fill from the 1-site seed",
        n_fill == 8 and n_fill == len(set(bits for bits, _s, _h, _hist in fillers)),
    )
    checks.check(
        "thm1-two-cube-twelve",
        "the two-cube has twelve vertices and contains the seed",
        len(TWO_CUBE) == 12 and len(set(TWO_CUBE)) == 12 and SEED in TWO_CUBE,
    )
    checks.check(
        "thm1-unique-support-36",
        "f_cutmin is the unique support-36 F_cut 1-site filler",
        m_cut == 36
        and n_min_cut == 1
        and displayed_min == CUTMIN_BITS
        and cutmin_support == 36
        and cutmin_support_direct == 36
        and in_f_cut(CUTMIN_BITS, type_of)
        and any(bits == CUTMIN_BITS for bits, _s, _h, _hist in fillers)
        and cutmin_row[1] == 36,
    )
    checks.check(
        "thm1-f-cutmin-fills",
        "f_cutmin fills: |locks_halt|=12 with reported T and history",
        cutmin_locks == 12
        and cutmin_halt == cutmin_row[2]
        and cutmin_history == cutmin_row[3]
        and cutmin_locks == 12
        and f"T = {cutmin_halt}" in note
        and f"({', '.join(str(n) for n in cutmin_history)})" in note,
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
        and l1_support == 56
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
        and l1_history == (1, 4, 8, 11, 12)
        and any(bits == l1_bits for bits, _s, _h, _hist in fillers),
    )
    checks.check(
        "thm2-histories-unequal",
        "f_cutmin lock history does not equal the L1 history on this seed",
        not histories_equal
        and cutmin_history != l1_history
        and cutmin_halt != l1_halt
        and CUTMIN_BITS != l1_bits
        and "does not equal the L1 history" in note,
    )
    checks.check(
        "thm3-displayed-not-adopted",
        "the F_cut minimizer and f_L1 are displayed, not adopted",
        "Displayed, not adopted" in note
        and 'hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"'
        in note
        and "Do not write f_cutmin into Admissibility" in note,
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
        "f-cutmin-definition-in-note",
        "the note names f_cutmin as the remaining-bit tuple (1, 0, 1, 0, 0)",
        "(1, 0, 1, 0, 0)" in note
        and "support-36" in note
        and "f_cutmin" in note,
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
        "claim_scope reports T and the lock history and does not adopt f_cutmin",
        "unique support-36 F_cut 1-site filler" in note
        and f"halts at tick T = {cutmin_halt}" in note
        and f"lock history ({', '.join(str(n) for n in cutmin_history)})" in note
        and "Displayed, not adopted" in note,
    )
    checks.check(
        "not-leftover-6414-or-6411",
        "the residual is the halt history, not leftover-character of support or of f_min",
        "Not leftover-character of #6414" in note
        and "support only" in note
        and "Not leftover-character of #6411" in note
        and "f_min" in note
        and "not in `F_cut`" in note,
    )
    checks.check(
        "mutation-f-min-outside-f-cut",
        "the unique support-26 filler among the 96 is outside F_cut",
        not predicate_in_f_cut(f_min)
        and min_bits == F_MIN_BITS
        and min_bits != CUTMIN_BITS
        and min_locks == 12
        and sum(1 for cell in product((0, 1), repeat=6) if f_min(cell)) == 26,
    )
    checks.check(
        "off-patch-zero",
        "off-patch occupancy is the explicit 0 default, not a blank-block",
        "off-patch occupancy `0`" in note and "blank-block is a different rule" in note,
    )
    cache_probe = ROOT / "logs" / ("runner" + "-cache") / (
        "f_cut_sparsest_one_site_halt_2026_08_15.txt"
    )
    checks.check(
        "no-cache-write",
        "this run did not emit a runner cache file",
        not cache_probe.is_file(),
    )

    print("per_element: checked exactly — each of the 64 neighbor 6-tuples is assigned its axis-type orbit")
    print("per_site: checked exactly — each of the 12 two-cube vertices is a lock site under o=0")
    print("per_mode: checked exactly — every F_cut map is run; the eight fillers are the support domain")
    print("per_block: checked exactly — unique F_cut support-36 filler is run to a fixed point from the 1-site seed")
    print("lattice_wide: checked and not executed — no Z^3-wide formation law or Admissibility rewrite is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
