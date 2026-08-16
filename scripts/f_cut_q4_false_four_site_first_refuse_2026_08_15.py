#!/usr/bin/env python3
"""First remaining-bit refuse of a Q4-false F_cut map on a 4-site seed.

F_cut is the cube-covariant class with f(empty)=f(full)=0 and f(c)=f(1-c).
Dynamics are occupancy-to-lock on the twelve-vertex two-cube with off-patch
occupancy 0. Q4(f) is (wt1=1) or (adj2=1). f_q0 is the lex-first remaining-
bit map with wt1=0 and adj2=0. S is the lex-first 4-site seed that f1
fills. The first remaining-bit neighborhood f_q0 refuses from S is
displayed, not adopted. f_L1 is the unbalanced-axis predicate (some n_mu
!= 0), never Hamming |c|_1 mod 2. New object: not leftover of #6518
(that was cov4>0 iff Q4).
"""

from __future__ import annotations

from itertools import combinations, permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/F_CUT_Q4_FALSE_FOUR_SITE_FIRST_REFUSE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/F_CUT_Q4_FALSE_FOUR_SITE_FIRST_REFUSE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Direction = tuple[int, int, int]
Config = tuple[int, int, int, int, int, int]
Rotation = tuple[tuple[int, int, int], tuple[int, int, int]]
OrbitType = tuple[int, int, int]
Site = tuple[int, int, int]
Seed = tuple[Site, Site, Site, Site]

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
FOUR_SITE_SEEDS: tuple[frozenset[Site], ...] = tuple(
    frozenset(quad) for quad in combinations(TWO_CUBE, 4)
)
REMAINING_ORDER: tuple[OrbitType, ...] = (
    (1, 0, 2),
    (0, 1, 2),
    (2, 0, 1),
    (3, 0, 0),
    (1, 1, 1),
)
REMAINING_LABELS: tuple[str, ...] = ("wt1", "opp2", "adj2", "vertex3", "mixed3")
AXIS_TYPE_NAME: dict[OrbitType, str] = {
    (0, 0, 3): "empty",
    (0, 3, 0): "full",
    (1, 0, 2): "wt1",
    (1, 2, 0): "wt1_comp",
    (0, 1, 2): "opp2",
    (0, 2, 1): "opp2_comp",
    (2, 0, 1): "adj2",
    (2, 1, 0): "adj2_comp",
    (3, 0, 0): "vertex3",
    (1, 1, 1): "mixed3",
}
L1_REMAINING: tuple[int, ...] = (1, 0, 1, 1, 1)
F1_REMAINING: tuple[int, ...] = (1, 1, 1, 1, 1)
FQ0_REMAINING: tuple[int, ...] = (0, 0, 0, 0, 0)
SEED_S_SITES: Seed = ((0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1))


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


def remaining_representative(kind: OrbitType) -> OrbitType | None:
    if kind in REMAINING_ORDER:
        return kind
    image = complement_type(kind)
    if image in REMAINING_ORDER:
        return image
    return None


def remaining_label(kind: OrbitType) -> str:
    representative = remaining_representative(kind)
    if representative is None:
        return AXIS_TYPE_NAME[kind]
    return REMAINING_LABELS[REMAINING_ORDER.index(representative)]


def f_L1(config: Config) -> int:
    """1 iff some axis is unbalanced: n_mu != 0.  Not Hamming parity."""
    return int(any(config[2 * axis] != config[2 * axis + 1] for axis in range(3)))


def f_hamming(config: Config) -> int:
    return sum(config) % 2


def remaining_value(config: Config, remaining: tuple[int, ...]) -> int:
    kind = axis_type(config)
    if kind in (axis_type(EMPTY), axis_type(FULL)):
        return 0
    assignment = dict(zip(REMAINING_ORDER, remaining, strict=True))
    if kind in assignment:
        return assignment[kind]
    return assignment[complement_type(kind)]


def f1(config: Config) -> int:
    """F_cut remaining bits (1, 1, 1, 1, 1).  Displayed.  Not adopted."""
    return remaining_value(config, F1_REMAINING)


def f_q0(config: Config) -> int:
    """Lex-first remaining-bit map with wt1=0 and adj2=0."""
    return remaining_value(config, FQ0_REMAINING)


def q4(remaining: tuple[int, ...]) -> int:
    return int(remaining[0] == 1 or remaining[2] == 1)


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


def run_from_seed(predicate, seed: frozenset[Site], halt_bound: int = 13) -> dict:
    locked = set(seed)
    history = [len(locked)]
    for _tick in range(halt_bound):
        nxt = evolve(locked, predicate)
        if nxt == locked:
            break
        locked = nxt
        history.append(len(locked))
    return {
        "fill": len(locked) == 12,
        "history": tuple(history),
        "locks": frozenset(locked),
        "halt_tick": len(history) - 1,
    }


def fills_from_seed(predicate, seed: frozenset[Site]) -> bool:
    return bool(run_from_seed(predicate, seed)["fill"])


def coverage4(predicate) -> int:
    return sum(1 for seed in FOUR_SITE_SEEDS if fills_from_seed(predicate, seed))


def seed_key(seed: frozenset[Site]) -> Seed:
    ordered = tuple(sorted(seed))
    return (ordered[0], ordered[1], ordered[2], ordered[3])


def seed_display(seed: frozenset[Site] | Seed) -> str:
    a, b, c, d = seed_key(frozenset(seed))
    return (
        f"{{({a[0]},{a[1]},{a[2]}),"
        f"({b[0]},{b[1]},{b[2]}),"
        f"({c[0]},{c[1]},{c[2]}),"
        f"({d[0]},{d[1]},{d[2]})}}"
    )


def remaining_refuse_events(locked: set[Site], predicate) -> list[dict]:
    rows: list[dict] = []
    for site in TWO_CUBE:
        if site in locked:
            continue
        config = neighborhood(site, locked)
        kind = axis_type(config)
        representative = remaining_representative(kind)
        if representative is None:
            continue
        if int(predicate(config)) != 0:
            continue
        rows.append(
            {
                "site": site,
                "config": config,
                "axis_type": kind,
                "remaining_type": representative,
                "remaining_name": remaining_label(kind),
                "f_q0": int(predicate(config)),
                "f1": int(f1(config)),
            }
        )
    return rows


def first_remaining_refuse(seed: frozenset[Site], predicate, halt_bound: int = 13) -> dict | None:
    locked = set(seed)
    for tick in range(1, halt_bound + 1):
        events = remaining_refuse_events(locked, predicate)
        if events:
            first = events[0]
            return {
                "tick": tick,
                "site": first["site"],
                "config": first["config"],
                "axis_type": first["axis_type"],
                "remaining_type": first["remaining_type"],
                "remaining_name": first["remaining_name"],
                "n_events": len(events),
                "events": tuple(events),
            }
        nxt = evolve(locked, predicate)
        if nxt == locked:
            return None
        locked = nxt
    return None


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


def remaining_bits_from_assignment(assignment: dict[OrbitType, int]) -> tuple[int, ...]:
    return tuple(assignment[orbit_type] for orbit_type in REMAINING_ORDER)


def remaining_bits_from_full(
    bits: tuple[int, ...], orbit_types: tuple[OrbitType, ...]
) -> tuple[int, ...]:
    assignment = dict(zip(orbit_types, bits, strict=True))
    return remaining_bits_from_assignment(assignment)


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


def enumerate_f_cut_remaining(
    orbit_types: tuple[OrbitType, ...],
    empty_type: OrbitType,
    full_type: OrbitType,
) -> list[tuple[int, ...]]:
    free_pairs, free_fixed = f_cut_free_data(orbit_types, empty_type, full_type)
    n_free = len(free_pairs) + len(free_fixed)
    members: list[tuple[int, ...]] = []
    for mask in range(1 << n_free):
        assignment = {empty_type: 0, full_type: 0}
        for rank, pair in enumerate(free_pairs):
            value = (mask >> rank) & 1
            assignment[pair[0]] = value
            assignment[pair[1]] = value
        for rank, orbit_type in enumerate(free_fixed):
            assignment[orbit_type] = (mask >> (len(free_pairs) + rank)) & 1
        members.append(remaining_bits_from_assignment(assignment))
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
    axiom_flat = normalize(axiom)

    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print("construction: occupancy-to-lock from lex-first 4-site seed f1 fills")
    print("negative_scope: Q4 is displayed, not adopted or written into Admissibility")

    orbits = build_orbits()
    orbit_types = tuple(sorted(orbits))
    orbit_sizes = {orbit_type: len(orbits[orbit_type]) for orbit_type in orbit_types}
    empty_type = axis_type(EMPTY)
    full_type = axis_type(FULL)
    free_pairs, free_fixed = f_cut_free_data(orbit_types, empty_type, full_type)
    n_free = len(free_pairs) + len(free_fixed)
    remaining_members = enumerate_f_cut_remaining(orbit_types, empty_type, full_type)
    q4_false = sorted(member for member in remaining_members if q4(member) == 0)
    lex_first_q4_false = q4_false[0]

    l1_bits = bits_from_predicate(f_L1, orbit_types, orbits)
    f1_bits = bits_from_predicate(f1, orbit_types, orbits)
    q0_bits = bits_from_predicate(f_q0, orbit_types, orbits)
    ham_bits = bits_from_predicate(f_hamming, orbit_types, orbits)
    l1_remaining = remaining_bits_from_full(l1_bits, orbit_types)
    f1_remaining = remaining_bits_from_full(f1_bits, orbit_types)
    q0_remaining = remaining_bits_from_full(q0_bits, orbit_types)

    seed_s = frozenset(SEED_S_SITES)
    lex_first_filled_by_f1 = next(seed for seed in FOUR_SITE_SEEDS if fills_from_seed(f1, seed))
    run_q0 = run_from_seed(f_q0, seed_s)
    run_f1 = run_from_seed(f1, seed_s)
    run_l1 = run_from_seed(f_L1, seed_s)
    cov4_q0 = coverage4(f_q0)
    first = first_remaining_refuse(seed_s, f_q0)
    n_refuse = 0 if first is None else first["n_events"]

    print(f"n_rotations={len(ROTATIONS)}")
    print(f"n_orbits={len(orbit_types)}")
    print("orbit_types_and_sizes=" + ",".join(f"{t}:{orbit_sizes[t]}" for t in orbit_types))
    print(f"remaining_labels={REMAINING_LABELS}")
    print(f"N_free={n_free}")
    print(f"|F_cut|={len(remaining_members)}")
    print(f"n_four_site_seeds={len(FOUR_SITE_SEEDS)}")
    print(f"f_q0_remaining={q0_remaining}")
    print(f"Q4_f_q0={q4(q0_remaining)}")
    print(f"cov4_f_q0={cov4_q0}")
    print(f"f1_remaining={f1_remaining}")
    print(f"f_L1_remaining={l1_remaining}")
    print(f"S={seed_display(seed_s)}")
    print(f"f1_fills_S={run_f1['fill']} hist_f1={run_f1['history']}")
    print(f"f_q0_fills_S={run_q0['fill']} hist_q0={run_q0['history']}")
    print(f"f_L1_fills_S={run_l1['fill']} hist_L1={run_l1['history']}")
    if first is None:
        print("first_remaining_refuse=None")
        print("N_refuse=0")
    else:
        print(
            "first_remaining_refuse="
            f"t={first['tick']} x={first['site']} "
            f"type={first['remaining_name']}{first['remaining_type']} "
            f"cfg={first['config']}"
        )
        print(f"N_refuse={n_refuse}")

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required note-plus-axiom string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/F_CUT_Q4_FALSE_FOUR_SITE_FIRST_REFUSE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and 'AUDIT_INPUT_PATHS = (\n'
        '    "docs/F_CUT_Q4_FALSE_FOUR_SITE_FIRST_REFUSE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
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
        "thm1-f-cut-cardinality",
        "F_cut has five free bits and size 32",
        n_free == 5
        and len(remaining_members) == 32
        and len(free_pairs) == 3
        and len(free_fixed) == 2
        and empty_type == (0, 0, 3)
        and full_type == (0, 3, 0)
        and REMAINING_ORDER == ((1, 0, 2), (0, 1, 2), (2, 0, 1), (3, 0, 0), (1, 1, 1)),
    )
    checks.check(
        "thm1-f-L1-is-unbalanced-axis",
        "f_L1 is 1 iff some axis has c_+ != c_-",
        all(
            f_L1(config) == int(axis_type(config)[0] >= 1)
            for config in product((0, 1), repeat=6)
        )
        and l1_remaining == L1_REMAINING
        and in_f_cut(l1_bits, orbit_types, empty_type, full_type),
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
        "thm1-two-cube-and-four-ninety-five-seeds",
        "the two-cube has twelve vertices and C(12,4)=495 four-site seeds",
        len(TWO_CUBE) == 12
        and len(set(TWO_CUBE)) == 12
        and len(FOUR_SITE_SEEDS) == 495
        and len(set(FOUR_SITE_SEEDS)) == 495
        and all(seed <= set(TWO_CUBE) and len(seed) == 4 for seed in FOUR_SITE_SEEDS),
    )
    checks.check(
        "thm1-name-fq0-q4-false-cov4-zero",
        "f_q0 is the lex-first Q4-false map and has Q4=0 and cov4=0",
        q0_remaining == FQ0_REMAINING
        and lex_first_q4_false == FQ0_REMAINING
        and q4(q0_remaining) == 0
        and q0_remaining[0] == 0
        and q0_remaining[2] == 0
        and cov4_q0 == 0
        and in_f_cut(q0_bits, orbit_types, empty_type, full_type)
        and all(q4(member) == 0 for member in q4_false)
        and len(q4_false) == 8,
    )
    checks.check(
        "thm1-f1-fills-S",
        "f1 fills the lex-first 4-site seed S",
        f1_remaining == F1_REMAINING
        and in_f_cut(f1_bits, orbit_types, empty_type, full_type)
        and seed_key(seed_s) == SEED_S_SITES
        and seed_key(lex_first_filled_by_f1) == SEED_S_SITES
        and run_f1["fill"]
        and run_f1["history"] == (4, 8, 12)
        and run_l1["fill"]
        and run_l1["history"] == (4, 8, 12)
        and not run_q0["fill"]
        and run_q0["history"] == (4,),
    )
    checks.check(
        "thm2-first-remaining-bit-refuse",
        "first remaining-bit refuse is t=1, site (1,0,0), type wt1; N_refuse=4",
        first is not None
        and first["tick"] == 1
        and first["site"] == (1, 0, 0)
        and first["remaining_type"] == (1, 0, 2)
        and first["remaining_name"] == "wt1"
        and first["config"] == (0, 1, 0, 0, 0, 0)
        and first["axis_type"] == (1, 0, 2)
        and n_refuse == 4
        and n_refuse != 0
        and all(event["remaining_name"] == "wt1" for event in first["events"])
        and f1(first["config"]) == 1
        and f_q0(first["config"]) == 0,
    )
    checks.check(
        "thm3-display-not-adopt-q4",
        "the first remaining-bit refuse is displayed and Q4 is not adopted",
        first is not None
        and first["remaining_name"] == "wt1"
        and "Do not adopt Q4" in note
        and "Do not write it into Admissibility" in note
        and "Displayed, not adopted" in note,
    )
    lattice_sentence = "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor"
    admissibility_sentence = (
        "There is one fixed nearest-neighbor admissibility rule, covariant under lattice"
    )
    record_lock = "When present, a record locks exactly one admissible local possibility."
    record_absence = "A site with no record cannot be read."
    checks.check(
        "lattice-and-admissibility-parents",
        "the live axiom memo supplies Z^3, proper cubic rotations, and a covariant nearest-neighbor rule",
        lattice_sentence in axiom
        and "proper cubic rotations about each site." in axiom
        and admissibility_sentence in axiom
        and record_lock in axiom
        and record_absence in axiom
        and lattice_sentence in note
        and record_absence in note,
    )
    checks.check(
        "note-contract",
        "bounded theorem, displayed-not-adopted first refuse, and machine status",
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
        "note-reports-first-refuse",
        "the note reports f_q0, S, the first remaining-bit refuse, and N_refuse",
        "(0, 0, 0, 0, 0)" in note
        and "(1, 1, 1, 1, 1)" in note
        and "{(0,0,0),(0,0,1),(0,1,0),(0,1,1)}" in note.replace(" ", "")
        and "t = 1" in note
        and "(1, 0, 0)" in note
        and "`wt1`" in note
        and "(1, 0, 2)" in note
        and "N_refuse = 4" in note
        and "Q4(f_q0)=0" in note
        and "cov4(f_q0)=0" in note,
    )
    checks.check(
        "no-axiom-edit",
        "the theorem proposes no axiom change",
        "no axiom or approved primitive is added" in note
        and "hypothetical_axiom_status" in note
        and "Do not write it into Admissibility" in note,
    )
    checks.check(
        "off-patch-zero",
        "off-patch occupancy is the explicit 0 default, not a blank-block",
        "off-patch occupancy `0`" in note and "blank-block is a different rule" in note,
    )
    checks.check(
        "not-leftover-6518",
        "the residual is the first remaining-bit refuse, not leftover-character of #6518",
        "Not leftover-character of #6518" in note
        and "cov4>0` iff Q4" in note
        and ("New object" in note or "new object" in note),
    )
    checks.check(
        "claim-scope",
        "claim_scope reports the first refused neighborhood of the lex-first Q4-false map",
        "On the two-cube with off-patch o=0, the first refused neighborhood of the lex-first Q4-false F_cut map on the lex-first 4-site seed f1 fills is reported."
        in note
        and "Displayed, not adopted" in note,
    )
    checks.check(
        "source-formation-boundary",
        "formation site/probability/rate remains outside Admissibility",
        "does not supply the formation site, probability, or rate" in axiom_flat
        and "does not supply the formation site, probability, or rate" in note_flat,
    )

    print("per_element: checked exactly — each of the 64 neighbor 6-tuples is assigned its axis-type orbit")
    print("per_site: checked exactly — each of the twelve two-cube vertices uses the same six-direction stencil")
    print("per_mode: checked exactly — f_q0 is scored on all 495 four-site seeds and from S against f1")
    print("per_block: checked exactly — the first remaining-bit refuse is named by tick, site, and type")
    print("lattice_wide: checked and not executed — no Z^3-wide formation law or physical Admissibility selector is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
