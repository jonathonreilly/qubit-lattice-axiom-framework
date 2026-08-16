#!/usr/bin/env python3
"""First remaining-bit refuse of the lex-first Q_* cov2=62 map.

F_cut is the cube-covariant class with f(empty)=f(full)=0 and f(c)=f(1-c).
Q_* is the eight-member subclass with remaining bits wt1=1 and adj2=1.
Dynamics are occupancy-to-lock on the twelve-vertex two-cube with off-patch
occupancy 0. f_L1 is the unbalanced-axis predicate (some n_mu != 0), never
Hamming |c|_1 mod 2. f_g is the remaining-bit tuple (1, 0, 1, 1, 0). f0 is
(1, 1, 1, 1, 0). The new object is the first remaining-bit refuse of f_g on
the lex-first 2-site seed f0 fills and f_g misses. Displayed, not adopted.
"""

from __future__ import annotations

from itertools import combinations, permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/F_CUT_QSTAR_COV2_GAP62_FIRST_REFUSE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/F_CUT_QSTAR_COV2_GAP62_FIRST_REFUSE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Direction = tuple[int, int, int]
Config = tuple[int, int, int, int, int, int]
Rotation = tuple[tuple[int, int, int], tuple[int, int, int]]
OrbitType = tuple[int, int, int]
Site = tuple[int, int, int]
Remaining = tuple[int, int, int, int, int]

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
REMAINING_ORDER: tuple[OrbitType, ...] = (
    (1, 0, 2),
    (0, 1, 2),
    (2, 0, 1),
    (3, 0, 0),
    (1, 1, 1),
)
REMAINING_LABELS: tuple[str, ...] = ("wt1", "opp2", "adj2", "vertex3", "mixed3")
L1_REMAINING: Remaining = (1, 0, 1, 1, 1)
G_REMAINING: Remaining = (1, 0, 1, 1, 0)
F0_REMAINING: Remaining = (1, 1, 1, 1, 0)
F1_REMAINING: Remaining = (1, 1, 1, 1, 1)
EMPTY_TYPE: OrbitType = (0, 0, 3)
FULL_TYPE: OrbitType = (0, 3, 0)
EXPECTED_MISS_SEEDS: tuple[frozenset[Site], ...] = (
    frozenset([(0, 0, 0), (2, 0, 0)]),
    frozenset([(0, 0, 1), (2, 0, 1)]),
    frozenset([(0, 1, 0), (2, 1, 0)]),
    frozenset([(0, 1, 1), (2, 1, 1)]),
)
EXPECTED_HALT: frozenset[Site] = frozenset(
    {
        (0, 0, 0),
        (0, 0, 1),
        (0, 1, 0),
        (0, 1, 1),
        (2, 0, 0),
        (2, 0, 1),
        (2, 1, 0),
        (2, 1, 1),
    }
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


def complement_type(orbit_type: OrbitType) -> OrbitType:
    unbalanced, both, empty = orbit_type
    return (unbalanced, empty, both)


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


def f_g(config: Config) -> int:
    return remaining_value(config, G_REMAINING)


def f0(config: Config) -> int:
    return remaining_value(config, F0_REMAINING)


def remaining_label(kind: OrbitType) -> str | None:
    if kind in REMAINING_ORDER:
        return REMAINING_LABELS[REMAINING_ORDER.index(kind)]
    partner = complement_type(kind)
    if partner in REMAINING_ORDER:
        return REMAINING_LABELS[REMAINING_ORDER.index(partner)]
    return None


def is_remaining_bit_type(kind: OrbitType) -> bool:
    return remaining_label(kind) is not None


def in_qstar(remaining: tuple[int, ...]) -> bool:
    """Q_* is the F_cut subclass with wt1=1 and adj2=1."""
    return remaining[0] == 1 and remaining[2] == 1


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


def fills_from_seed(predicate, seed: frozenset[Site]) -> bool:
    locked = set(seed)
    for _tick in range(13):
        nxt = evolve(locked, predicate)
        if nxt == locked:
            return len(locked) == 12
        locked = nxt
    return False


def halt_set(predicate, seed: frozenset[Site]) -> frozenset[Site]:
    locked = set(seed)
    for _tick in range(13):
        nxt = evolve(locked, predicate)
        if nxt == locked:
            return frozenset(locked)
        locked = nxt
    return frozenset(locked)


def lock_count_history(predicate, seed: frozenset[Site]) -> tuple[int, ...]:
    locked = set(seed)
    history = [len(locked)]
    for _tick in range(13):
        nxt = evolve(locked, predicate)
        if nxt == locked:
            return tuple(history)
        locked = nxt
        history.append(len(locked))
    return tuple(history)


def remaining_bit_events(
    predicate, locked: set[Site]
) -> list[tuple[Site, Config, OrbitType, str | None, int]]:
    events: list[tuple[Site, Config, OrbitType, str | None, int]] = []
    for site in TWO_CUBE:
        if site in locked:
            continue
        config = neighborhood(site, locked)
        kind = axis_type(config)
        value = int(predicate(config))
        events.append((site, config, kind, remaining_label(kind), value))
    return events


def remaining_bit_refuses(
    events: list[tuple[Site, Config, OrbitType, str | None, int]],
) -> list[tuple[Site, Config, OrbitType, str]]:
    refuses: list[tuple[Site, Config, OrbitType, str]] = []
    for site, config, kind, label, value in events:
        if value == 0 and label is not None:
            refuses.append((site, config, kind, label))
    return refuses


def first_remaining_bit_refuse(
    predicate, seed: frozenset[Site]
) -> tuple[int, Site, Config, OrbitType, str, int] | None:
    locked = set(seed)
    for tick in range(1, 14):
        events = remaining_bit_events(predicate, locked)
        refuses = remaining_bit_refuses(events)
        nxt = set(locked)
        for site, _config, _kind, _label, value in events:
            if value:
                nxt.add(site)
        if refuses:
            site, config, kind, label = refuses[0]
            return (tick, site, config, kind, label, len(refuses))
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


def enumerate_f_cut(
    orbit_types: tuple[OrbitType, ...],
    empty_type: OrbitType,
    full_type: OrbitType,
) -> list[tuple[tuple[int, ...], tuple[int, ...]]]:
    free_pairs, free_fixed = f_cut_free_data(orbit_types, empty_type, full_type)
    n_free = len(free_pairs) + len(free_fixed)
    members: list[tuple[tuple[int, ...], tuple[int, ...]]] = []
    for mask in range(1 << n_free):
        assignment = {empty_type: 0, full_type: 0}
        for rank, pair in enumerate(free_pairs):
            value = (mask >> rank) & 1
            assignment[pair[0]] = value
            assignment[pair[1]] = value
        for rank, orbit_type in enumerate(free_fixed):
            assignment[orbit_type] = (mask >> (len(free_pairs) + rank)) & 1
        bits = tuple(assignment[orbit_type] for orbit_type in orbit_types)
        remaining = remaining_bits_from_assignment(assignment)
        members.append((bits, remaining))
    return members


def two_site_seeds() -> tuple[frozenset[Site], ...]:
    return tuple(frozenset(pair) for pair in combinations(TWO_CUBE, 2))


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
        (ROOT / path).read_text(encoding="utf-8")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print(
        "external_scientific_inputs: current Lattice/Admissibility/Record "
        "boundary only; no observation or fit"
    )
    print(
        "negative_scope: displayed first remaining-bit refuse of f_g; "
        "does not adopt a bit"
    )

    orbits = build_orbits()
    orbit_types = tuple(sorted(orbits))
    orbit_sizes = {orbit_type: len(orbits[orbit_type]) for orbit_type in orbit_types}
    empty_type = axis_type(EMPTY)
    full_type = axis_type(FULL)
    free_pairs, free_fixed = f_cut_free_data(orbit_types, empty_type, full_type)
    n_free = len(free_pairs) + len(free_fixed)
    n_cut = 1 << n_free
    members = enumerate_f_cut(orbit_types, empty_type, full_type)
    type_of = {config: orbit_type for orbit_type, group in orbits.items() for config in group}
    seeds = two_site_seeds()

    g_bits = bits_from_predicate(f_g, orbit_types, orbits)
    g_remaining = remaining_bits_from_full(g_bits, orbit_types)
    f0_bits = bits_from_predicate(f0, orbit_types, orbits)
    f0_remaining = remaining_bits_from_full(f0_bits, orbit_types)
    l1_bits = bits_from_predicate(f_L1, orbit_types, orbits)
    ham_bits = bits_from_predicate(f_hamming, orbit_types, orbits)
    l1_remaining = remaining_bits_from_full(l1_bits, orbit_types)
    pred_g = predicate_from_bits(g_bits, orbit_types, type_of)
    pred_f0 = predicate_from_bits(f0_bits, orbit_types, type_of)

    qstar = [(bits, remaining) for bits, remaining in members if in_qstar(remaining)]
    cov_g = sum(1 for seed in seeds if fills_from_seed(f_g, seed))
    cov_f0 = sum(1 for seed in seeds if fills_from_seed(f0, seed))
    miss = tuple(seed for seed in seeds if fills_from_seed(f0, seed) and not fills_from_seed(f_g, seed))
    lex_seed = miss[0]
    seed_halt = halt_set(f_g, lex_seed)
    seed_hist = lock_count_history(f_g, lex_seed)
    refuse = first_remaining_bit_refuse(f_g, lex_seed)

    print(f"n_rotations={len(ROTATIONS)}")
    print(f"n_orbits={len(orbit_types)}")
    print(f"remaining_labels={REMAINING_LABELS}")
    print(f"N_free={n_free}")
    print(f"|F_cut|={n_cut}")
    print(f"n_two_site_seeds={len(seeds)}")
    print(f"|Q_*|={len(qstar)}")
    print(f"f_L1_remaining={l1_remaining}")
    print(f"f_g_remaining={g_remaining}")
    print(f"f0_remaining={f0_remaining}")
    print(f"cov2(f_g)={cov_g}")
    print(f"cov2(f0)={cov_f0}")
    print(f"n_miss={len(miss)}")
    print(f"lex_seed={tuple(sorted(lex_seed))}")
    print(f"f_g_halt_size={len(seed_halt)}")
    print(f"f_g_history={seed_hist}")
    print(f"first_refuse={refuse}")
    print(f"f_hamming_bits_neq_L1={ham_bits != l1_bits}")

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required note-plus-axiom string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/F_CUT_QSTAR_COV2_GAP62_FIRST_REFUSE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and AUDIT_TIMEOUT_SEC == 120
        and "AUDIT_INPUT_PATHS = (\n"
        '    "docs/F_CUT_QSTAR_COV2_GAP62_FIRST_REFUSE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ")" in self_source,
    )
    checks.check(
        "thm1-host",
        "24 rotations, 10 orbits, 32 F_cut maps, 66 two-site seeds, 8 Q_* maps",
        len(ROTATIONS) == 24
        and len(set(ROTATIONS)) == 24
        and len(orbit_types) == 10
        and sum(orbit_sizes.values()) == 64
        and n_free == 5
        and n_cut == 32
        and len(members) == 32
        and len(seeds) == 66
        and len(TWO_CUBE) == 12
        and len(qstar) == 8
        and empty_type == EMPTY_TYPE
        and full_type == FULL_TYPE
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
        "f_L1 is n!=0, not Hamming |c|_1 mod 2",
        l1_bits != ham_bits
        and any(f_L1(config) != f_hamming(config) for config in product((0, 1), repeat=6))
        and "sum(config) % 2"
        not in self_source.split("def f_L1", 1)[1].split("def f_hamming", 1)[0]
        and "n ≠ 0" in note
        and "This is **not** Hamming parity" in note,
    )
    checks.check(
        "thm1-f-g-and-f0",
        "f_g is (1,0,1,1,0) in Q_* with vertex3=1; f0 is Max(2)",
        g_remaining == G_REMAINING
        and g_remaining == (1, 0, 1, 1, 0)
        and g_remaining[3] == 1
        and g_remaining[1] == 0
        and in_qstar(g_remaining)
        and in_f_cut(g_bits, orbit_types, empty_type, full_type)
        and f0_remaining == F0_REMAINING
        and f0_remaining == (1, 1, 1, 1, 0)
        and in_qstar(f0_remaining)
        and in_f_cut(f0_bits, orbit_types, empty_type, full_type)
        and F1_REMAINING == (1, 1, 1, 1, 1)
        and "`f_g`" in note
        and "(1, 0, 1, 1, 0)" in note
        and "(1, 1, 1, 1, 0)" in note,
    )
    checks.check(
        "thm1-lex-first-miss-seed",
        "lex-first 2-site seed f0 fills and f_g misses is {(0,0,0),(2,0,0)}",
        cov_g == 62
        and cov_f0 == 66
        and len(miss) == 4
        and miss == EXPECTED_MISS_SEEDS
        and lex_seed == frozenset([(0, 0, 0), (2, 0, 0)])
        and fills_from_seed(f0, lex_seed) is True
        and fills_from_seed(f_g, lex_seed) is False
        and fills_from_seed(pred_f0, lex_seed) is True
        and fills_from_seed(pred_g, lex_seed) is False
        and seed_halt == EXPECTED_HALT
        and seed_hist == (2, 6, 8)
        and "{(0,0,0), (2,0,0)}" in note,
    )
    assert refuse is not None
    refuse_tick, refuse_site, refuse_config, refuse_kind, refuse_label, n_refuse = refuse
    checks.check(
        "thm1-first-remaining-bit-refuse-opp2",
        "first remaining-bit refuse of f_g from S is opp2 at tick 1",
        refuse_tick == 1
        and refuse_label == "opp2"
        and refuse_kind == (0, 1, 2)
        and is_remaining_bit_type(refuse_kind)
        and f_g(refuse_config) == 0
        and f0(refuse_config) == 1
        and remaining_value(refuse_config, G_REMAINING) == 0
        and remaining_value(refuse_config, F0_REMAINING) == 1,
    )
    checks.check(
        "thm1-first-refused-neighborhood",
        "lex-first refused remaining-bit neighborhood is (1,1,0,0,0,0) at (1,0,0)",
        refuse_site == (1, 0, 0)
        and refuse_config == (1, 1, 0, 0, 0, 0)
        and axis_type(refuse_config) == (0, 1, 2)
        and "(1, 1, 0, 0, 0, 0)" in note
        and "`(1,0,0)`" in note
        and "tick 1" in note,
    )
    checks.check(
        "thm2-n-refuse-on-first-tick",
        "N_refuse on the first refuse tick is 1",
        n_refuse == 1
        and "N_refuse = 1" in note
        and refuse_tick == 1,
    )
    seed_events = remaining_bit_events(f_g, set(lex_seed))
    seed_refuses = remaining_bit_refuses(seed_events)
    empty_refuses = [
        event
        for event in seed_events
        if event[4] == 0 and event[2] in (EMPTY_TYPE, FULL_TYPE)
    ]
    checks.check(
        "thm2-single-opp2-and-empty-not-remaining",
        "the first refuse tick has one opp2 site; empty refuses are not remaining bits",
        seed_refuses == [((1, 0, 0), (1, 1, 0, 0, 0, 0), (0, 1, 2), "opp2")]
        and len(empty_refuses) >= 1
        and remaining_label(EMPTY_TYPE) is None
        and remaining_label(FULL_TYPE) is None
        and all(label == "opp2" for _s, _c, _k, label in seed_refuses),
    )
    checks.check(
        "thm3-displayed-not-adopted",
        "the opp2 refuse is displayed and no bit is adopted",
        g_remaining[1] == 0
        and f0_remaining[1] == 1
        and G_REMAINING != L1_REMAINING
        and "Do not adopt `opp2`" in note
        and "Do not adopt a bit" in note
        and "Displayed, not adopted" in note
        and "does not adopt a bit" in self_source,
    )

    lattice_sites = (
        "Physical sites are the points of the cubic lattice `Z^3`, with "
        "nearest-neighbor adjacency, standard translations, and proper cubic "
        "rotations about each site."
    )
    admissibility = (
        "There is one fixed nearest-neighbor admissibility rule, covariant "
        "under lattice translations and proper cubic rotations."
    )
    formation_residual = "it does not supply the formation site, probability, or rate."
    record_lock = "When present, a record locks exactly one admissible local possibility."
    record_content = "A readout value is determined by record content alone."
    record_absence = "A site with no record cannot be read."
    records_form = "Records form."

    checks.check(
        "source-lattice-admissibility",
        "Lattice rotations and Admissibility covariance are pinned",
        lattice_sites in axiom_flat
        and admissibility in axiom_flat
        and lattice_sites in note_flat
        and admissibility in note_flat,
    )
    checks.check(
        "source-record-boundary",
        "Record lock, content-only readout, unreadable absence, and formation residual are pinned",
        all(
            phrase in axiom_flat
            for phrase in (
                records_form,
                record_lock,
                record_content,
                record_absence,
                formation_residual,
            )
        )
        and all(
            phrase in note_flat
            for phrase in (
                records_form,
                record_lock,
                record_content,
                record_absence,
                formation_residual,
            )
        ),
    )

    claim_scope = (
        "On the two-cube with off-patch o=0, the first remaining-bit refuse "
        "of F_cut (1,0,1,1,0) on the lex-first 2-site seed f0 fills and "
        "(1,0,1,1,0) misses is reported. Displayed, not adopted."
    )
    checks.check(
        "claim-scope",
        "claim_scope reports the first remaining-bit refuse and does not adopt a bit",
        claim_scope in note and "Displayed, not adopted" in note,
    )

    allowed_retained = (
        "audit_required_before_effective_retained: true",
        "bare_retained_allowed: false",
    )
    other_retained = note
    for line in allowed_retained:
        other_retained = other_retained.replace(line, "")
    required = (
        "actual_current_surface_status: bounded-support",
        "target_claim_type: bounded_theorem",
        "trace_class: frontier_discovery",
        "reachability_to_target: advances",
        'hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"',
        "authors no audit verdict",
        "FAIL / DO NOT SHIP",
        "Theorem 1",
        "Theorem 2",
        "Theorem 3",
        "|F_cut| = 32",
        "No-Go Discipline disposition: **PASS**",
    )
    forbidden = ("G_" + "N", "1/" + "r", "1/" + "r^2", "Lattice-" + "named", "not a " + "TOE")
    checks.check(
        "note-contract",
        "machine fields, three theorems, and forbidden-phrase hygiene hold",
        all(phrase in note for phrase in required)
        and all(line in note for line in allowed_retained)
        and all(f"### N{index}" in note for index in range(1, 9))
        and note.count("**ATTEMPTED**") == 6
        and not any(phrase in note or phrase in self_source for phrase in forbidden)
        and "retained" not in other_retained
        and "promoted" not in note.lower()
        and "toe-lphys" not in note
        and "runner-cache" not in note
        and "citation" not in note.lower(),
    )
    checks.check(
        "no-axiom-edit",
        "the axiom memo is unedited and the theorem proposes no axiom change",
        "### Lattice / Physical Locality" in axiom
        and "### Qubit / Site Possibility" in axiom
        and "### Admissibility / Local Constraint" in axiom
        and "### Record / Fixed Reality" in axiom
        and "F_cut" not in axiom
        and "f_L1" not in axiom
        and "no axiom or approved primitive is added" in note
        and "Do not write `opp2` into Admissibility" in note,
    )
    checks.check(
        "off-patch-zero",
        "off-patch occupancy is the explicit 0 default, not a blank-block",
        "off-patch occupancy `0`" in note
        and "off-patch o=0" in note
        and "blank-block is a different rule" in note,
    )
    checks.check(
        "l1-definition-in-note",
        "the note defines f_L1 as unbalanced-axis / n != 0 and rejects Hamming",
        "`f_L1(c)=1` if and only if some axis is unbalanced" in note_flat
        and "`n_μ = c_{+μ} − c_{-μ}` is nonzero" in note
        and "This is **not** Hamming parity" in note,
    )
    checks.check(
        "not-leftover-tot2q",
        "the residual is the 62-gap refuse, not leftover-character of tot2q",
        "Not leftover-character of tot2q" in note
        and "Mechanism of the 62-gap" in note
        and "Not leftover-character of the `f_L1` two-site miss mechanism" in note,
    )

    print("per_element: checked exactly — each of the 64 neighbor 6-tuples is assigned its axis-type orbit")
    print("per_site: checked exactly — each of the twelve two-cube vertices uses the same six-direction stencil")
    print("per_mode: checked exactly — f_g is evolved from the lex-first f0-fill / f_g-miss seed")
    print("per_block: checked exactly — first remaining-bit refuse and N_refuse are exact on this patch")
    print("lattice_wide: checked and not executed — no Z^3-wide formation law or physical Admissibility selector is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
