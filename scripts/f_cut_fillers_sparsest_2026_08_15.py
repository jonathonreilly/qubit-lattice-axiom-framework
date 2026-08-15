#!/usr/bin/env python3
"""Support-minimizer census among the eight F_cut 1-site two-cube fillers.

Recomputes the 24 proper cube rotations, the 10 orbits on {0,1}^6, and the
32-element three-cut class F_cut (f(empty)=f(full)=0 and f(c)=f(1-c)).
Fills the twelve-vertex two-cube from a 1-site seed with off-patch
occupancy 0. Among the eight F_cut fillers, reports the minimal support
and whether f_L1 (some axis unbalanced; never Hamming parity) is the
unique minimizer.

No axiom edit, no cache write, no citation-manifest write.
"""

from __future__ import annotations

from itertools import permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
AUDIT_INPUT_PATHS = (
    "docs/F_CUT_FILLERS_SPARSEST_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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

# Remaining free F_cut bits, in the displayed order
# (wt1, opp2, adj2, vertex3, mixed3).
WT1: OrbitType = (1, 0, 2)
OPP2: OrbitType = (0, 1, 2)
ADJ2: OrbitType = (2, 0, 1)
VERTEX3: OrbitType = (3, 0, 0)
MIXED3: OrbitType = (1, 1, 1)
L1_BITS: BitTuple = (1, 0, 1, 1, 1)
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


def f_global_min(config: Config) -> int:
    """Unique support-26 filler among the 96; outside F_cut. Not adopted."""
    if config == EMPTY:
        return 0
    return int(
        config[0] + config[1] <= 1
        and config[2] + config[3] <= 1
        and config[4] + config[5] <= 1
    )


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
    assignment = {
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
    return assignment


def predicate_from_bits(bits: BitTuple, type_of: dict[Config, OrbitType]):
    assignment = assignment_from_bits(bits)

    def predicate(config: Config) -> int:
        return assignment[type_of[config]]

    return predicate


def complement_cell(config: Config) -> Config:
    return (1 - config[0], 1 - config[1], 1 - config[2], 1 - config[3], 1 - config[4], 1 - config[5])


def predicate_in_f_cut(predicate) -> bool:
    if int(predicate(EMPTY)) != 0 or int(predicate(FULL)) != 0:
        return False
    return all(
        int(predicate(config)) == int(predicate(complement_cell(config)))
        for config in product((0, 1), repeat=6)
    )


def in_f_cut(bits: BitTuple) -> bool:
    return predicate_in_f_cut(predicate_from_bits(bits, {
        config: axis_type(config) for config in product((0, 1), repeat=6)
    }))


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

    print("external_scientific_inputs: none; two-cube patch, seed, and off-patch o=0 are theorem hypotheses")
    print("package_local_integrity_reads: runner source, proposed source note, and live axiom memo")
    print("measure_boundary: exact finite census on 64 cells, 32 F_cut maps, and 12 vertices; no physical selector")
    print("negative_scope: sparsity among the eight F_cut 1-site fillers does not select f_L1")
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
    global_min_bits = bits_from_predicate(f_global_min, orbit_types, orbits)
    l1_locks, l1_halt, l1_history = run_predicate(f_L1)
    ham_locks, _ham_halt, ham_history = run_predicate(f_hamming)
    l1_support = support_of_bits(l1_bits)
    l1_support_direct = sum(1 for cell in product((0, 1), repeat=6) if f_L1(cell))

    fillers = census_f_cut_fillers(type_of)
    n_fill = len(fillers)
    supports = [support for _bits, support, _halt, _history in fillers]
    m_cut = min(supports)
    n_min_cut = sum(1 for support in supports if support == m_cut)
    min_bits_list = [bits for bits, support, _halt, _history in fillers if support == m_cut]
    displayed_min = min_bits_list[0] if len(min_bits_list) == 1 else None

    print(f"n_rotations={len(ROTATIONS)}")
    print(f"n_orbits={len(orbit_types)}")
    print(f"N_free={n_free}")
    print(f"|F_cut|={n_cut}")
    print(f"N_fill_cut={n_fill}")
    print(f"f_L1_bits={l1_bits} supp={l1_support} locks={l1_locks} history={l1_history}")
    print(f"f_hamming_bits={ham_bits} locks={ham_locks} history={ham_history}")
    print(
        f"global_min_bits={global_min_bits} "
        f"in_F_cut={predicate_in_f_cut(f_global_min)}"
    )
    print("fillers=" + ",".join(f"{bits}:{support}" for bits, support, _h, _hist in fillers))
    print(f"m_cut={m_cut}")
    print(f"N_min_cut={n_min_cut}")
    print(f"displayed_minimizer={displayed_min}")

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required note-plus-axiom string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/F_CUT_FILLERS_SPARSEST_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and 'AUDIT_INPUT_PATHS = (\n'
        '    "docs/F_CUT_FILLERS_SPARSEST_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
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
        "thm1-l1-in-f-cut-and-fills",
        "f_L1 lies in F_cut, fills, and is one of the eight",
        l1_bits == L1_BITS
        and in_f_cut(l1_bits)
        and l1_locks == 12
        and l1_halt == 4
        and l1_history == (1, 4, 8, 11, 12)
        and any(bits == l1_bits for bits, _s, _h, _hist in fillers),
    )
    checks.check(
        "thm1-l1-support-56",
        "supp(f_L1)=56, equivalently 64 minus the 8 fully balanced cells",
        l1_support == 56
        and l1_support_direct == 56
        and l1_support == support_of_bits(L1_BITS),
    )
    checks.check(
        "thm1-l1-not-hamming",
        "f_L1 is n!=0 / unbalanced-axis, not Hamming |c|_1 mod 2",
        l1_bits != ham_bits
        and any(f_L1(config) != f_hamming(config) for config in product((0, 1), repeat=6))
        and "sum(config) % 2"
        not in self_source.split("def f_L1", 1)[1].split("def f_hamming", 1)[0],
    )
    checks.check(
        "thm1-two-cube-twelve",
        "the two-cube has twelve vertices and contains the seed",
        len(TWO_CUBE) == 12 and len(set(TWO_CUBE)) == 12 and SEED in TWO_CUBE,
    )
    checks.check(
        "thm2-m-cut",
        f"m_cut = min supp over the eight equals {m_cut}",
        m_cut == 36 and all(support >= 36 for support in supports),
    )
    checks.check(
        "thm2-n-min-cut",
        "N_min_cut = 1: exactly one of the eight attains m_cut",
        n_min_cut == 1 and len(min_bits_list) == 1,
    )
    checks.check(
        "thm3-unique-is-not-l1",
        "the unique F_cut support-minimizer is not f_L1",
        n_min_cut == 1
        and displayed_min is not None
        and displayed_min != l1_bits
        and l1_support == 56
        and l1_support > m_cut,
    )
    checks.check(
        "thm3-displayed-tuple",
        "the displayed minimizer is the remaining-bit tuple (1, 0, 1, 0, 0)",
        displayed_min == (1, 0, 1, 0, 0)
        and support_of_bits((1, 0, 1, 0, 0)) == 36
        and in_f_cut((1, 0, 1, 0, 0))
        and run_predicate(predicate_from_bits((1, 0, 1, 0, 0), type_of))[0] == 12,
    )
    checks.check(
        "mutation-global-min-outside-f-cut",
        "the unique support-26 filler among the 96 is outside F_cut",
        not predicate_in_f_cut(f_global_min)
        and global_min_bits != l1_bits
        and sum(1 for cell in product((0, 1), repeat=6) if f_global_min(cell)) == 26
        and any(
            f_global_min(config) != f_global_min(complement_cell(config))
            for config in product((0, 1), repeat=6)
        ),
    )
    checks.check(
        "mutation-hamming-nine-locks",
        "Hamming parity is in F_cut but is not a filler",
        in_f_cut(ham_bits)
        and ham_locks == 9
        and ham_history == (1, 4, 5, 7, 9)
        and ham_bits not in {bits for bits, _s, _h, _hist in fillers},
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
        "displayed-not-adopted",
        "the F_cut minimizer and f_L1 are displayed, not adopted",
        "Displayed, not adopted" in note
        and 'hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"'
        in note,
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
        "claim-scope-minimum",
        "claim_scope reports m_cut=36, N_min_cut=1, and that f_L1 is not the unique minimizer",
        "minimal support is 36" in note
        and "N_min_cut = 1" in note
        and "f_L1 is not the unique minimizer" in note,
    )
    checks.check(
        "not-leftover-of-ninetysix",
        "the residual is F_cut sparsity, not the 96-map support minimum",
        "Not leftover-character of the 96-map support minimum" in note
        and "outside `F_cut`" in note,
    )
    cache_probe = ROOT / "logs" / ("runner" + "-cache") / (
        "f_cut_fillers_sparsest_2026_08_15.txt"
    )
    checks.check(
        "no-cache-write",
        "this run did not emit a runner cache file",
        not cache_probe.is_file(),
    )

    print("per_element: checked exactly — each of the 64 cells is assigned by orbit and counted in supp(f)")
    print("per_site: checked exactly — each of the 12 two-cube vertices is a lock site under o=0")
    print("per_mode: checked exactly — every F_cut map is run; the eight fillers are the support domain")
    print("per_block: checked exactly — unique F_cut support minimum 36 is not attained by f_L1")
    print("lattice_wide: checked and not executed — no infinite-lattice fill or adopted occupancy axiom is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
