#!/usr/bin/env python3
"""First remaining-bit refuse of f_nt from the q1split seed.

F_cut is the cube-covariant class with f(empty)=f(full)=0 and f(c)=f(1-c).
Q_* is the eight-member subclass with remaining bits wt1=1 and adj2=1.
Dynamics are occupancy-to-lock on the twelve-vertex two-cube with off-patch
occupancy 0. f_L1 is the unbalanced-axis predicate (some n_mu != 0), never
Hamming |c|_1 mod 2. f_nt is the lex-first Q_* map with vertex3=0, remaining
bits (1, 0, 1, 0, 0). The new object is the first remaining-bit refuse of
f_nt from S={(1, 0, 0)}. Displayed, not adopted.
"""

from __future__ import annotations

from itertools import permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/F_CUT_QSTAR_NONTOT_FIRST_REFUSE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/F_CUT_QSTAR_NONTOT_FIRST_REFUSE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
NT_REMAINING: Remaining = (1, 0, 1, 0, 0)
CONTRAST_REMAINING: Remaining = (1, 0, 1, 1, 0)
SPLIT_SEED: frozenset[Site] = frozenset([(1, 0, 0)])
EMPTY_TYPE: OrbitType = (0, 0, 3)
FULL_TYPE: OrbitType = (0, 3, 0)
EXPECTED_HALT: frozenset[Site] = frozenset(
    {
        (0, 0, 0),
        (0, 0, 1),
        (0, 1, 0),
        (1, 0, 0),
        (1, 0, 1),
        (1, 1, 0),
        (1, 1, 1),
        (2, 0, 0),
        (2, 0, 1),
        (2, 1, 0),
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


def f_nt(config: Config) -> int:
    return remaining_value(config, NT_REMAINING)


def f_contrast(config: Config) -> int:
    """Displayed vertex3-flipped contrast (1, 0, 1, 1, 0).  Not adopted."""
    return remaining_value(config, CONTRAST_REMAINING)


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
    members = enumerate_f_cut(orbit_types, empty_type, full_type)
    type_of = {config: orbit_type for orbit_type, group in orbits.items() for config in group}

    nt_bits = bits_from_predicate(f_nt, orbit_types, orbits)
    nt_remaining = remaining_bits_from_full(nt_bits, orbit_types)
    l1_bits = bits_from_predicate(f_L1, orbit_types, orbits)
    ham_bits = bits_from_predicate(f_hamming, orbit_types, orbits)
    l1_remaining = remaining_bits_from_full(l1_bits, orbit_types)
    contrast_bits = bits_from_predicate(f_contrast, orbit_types, orbits)
    contrast_remaining = remaining_bits_from_full(contrast_bits, orbit_types)

    qstar = [(bits, remaining) for bits, remaining in members if in_qstar(remaining)]
    nontot = sorted(
        [(bits, remaining) for bits, remaining in qstar if remaining[3] == 0],
        key=lambda item: item[1],
    )

    seed_halt = halt_set(f_nt, SPLIT_SEED)
    seed_fills = fills_from_seed(f_nt, SPLIT_SEED)
    l1_fills = fills_from_seed(f_L1, SPLIT_SEED)
    refuse = first_remaining_bit_refuse(f_nt, SPLIT_SEED)
    contrast_fills = fills_from_seed(f_contrast, SPLIT_SEED)
    pred_nt = predicate_from_bits(nt_bits, orbit_types, type_of)

    print(f"n_rotations={len(ROTATIONS)}")
    print(f"n_orbits={len(orbit_types)}")
    print("orbit_types_and_sizes=" + ",".join(f"{t}:{orbit_sizes[t]}" for t in orbit_types))
    print(f"remaining_labels={REMAINING_LABELS}")
    print(f"N_free={n_free}")
    print(f"|F_cut|={n_cut}")
    print(f"|Q_*|={len(qstar)}")
    print(f"f_L1_remaining={l1_remaining}")
    print(f"f_nt_remaining={nt_remaining}")
    print(f"f_L1_in_Qstar={in_qstar(l1_remaining)}")
    print(f"f_nt_in_Qstar={in_qstar(nt_remaining)}")
    print(f"seed_halt_size={len(seed_halt)}")
    print(f"f_nt_fills_S={seed_fills}")
    print(f"f_L1_fills_S={l1_fills}")
    print(f"first_refuse={refuse}")
    print(f"contrast_remaining={contrast_remaining}")
    print(f"contrast_fills_S={contrast_fills}")
    print(f"f_hamming_bits_neq_L1={ham_bits != l1_bits}")

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required note-plus-axiom string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/F_CUT_QSTAR_NONTOT_FIRST_REFUSE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and "AUDIT_INPUT_PATHS = (\n"
        '    "docs/F_CUT_QSTAR_NONTOT_FIRST_REFUSE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
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
        and n_cut == 32
        and len(members) == 32
        and len(free_pairs) == 3
        and len(free_fixed) == 2
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
        "f_L1 is not Hamming |c|_1 mod 2",
        l1_bits != ham_bits
        and any(f_L1(config) != f_hamming(config) for config in product((0, 1), repeat=6))
        and "sum(config) % 2"
        not in self_source.split("def f_L1", 1)[1].split("def f_hamming", 1)[0],
    )
    checks.check(
        "thm1-qstar-and-f-nt",
        "f_nt is the lex-first Q_* remaining-bit tuple with vertex3=0",
        nt_remaining == NT_REMAINING
        and nt_remaining == (1, 0, 1, 0, 0)
        and nt_remaining[3] == 0
        and in_qstar(nt_remaining)
        and in_qstar(l1_remaining)
        and in_f_cut(nt_bits, orbit_types, empty_type, full_type)
        and len(qstar) == 8
        and nontot[0][1] == min(remaining for _bits, remaining in nontot)
        and nontot[0][1] == NT_REMAINING
        and SPLIT_SEED == frozenset([(1, 0, 0)])
        and "`f_nt`" in note
        and "(1, 0, 1, 0, 0)" in note,
    )
    checks.check(
        "thm1-f-nt-does-not-fill-S",
        "f_nt does not fill S; f_L1 does; halt size is 10",
        seed_fills is False
        and l1_fills is True
        and len(seed_halt) == 10
        and seed_halt == EXPECTED_HALT
        and not fills_from_seed(pred_nt, SPLIT_SEED)
        and fills_from_seed(f_L1, SPLIT_SEED),
    )
    assert refuse is not None
    refuse_tick, refuse_site, refuse_config, refuse_kind, refuse_label, n_refuse = refuse
    checks.check(
        "thm1-first-remaining-bit-refuse-vertex3",
        "first remaining-bit refuse of f_nt from S is vertex3 at tick 3",
        refuse_tick == 3
        and refuse_label == "vertex3"
        and refuse_kind == (3, 0, 0)
        and is_remaining_bit_type(refuse_kind)
        and f_nt(refuse_config) == 0
        and remaining_value(refuse_config, NT_REMAINING) == 0,
    )
    checks.check(
        "thm1-first-refused-neighborhood",
        "lex-first refused remaining-bit neighborhood is (1,0,0,1,0,1) at (0,1,1)",
        refuse_site == (0, 1, 1)
        and refuse_config == (1, 0, 0, 1, 0, 1)
        and axis_type(refuse_config) == (3, 0, 0)
        and "(1, 0, 0, 1, 0, 1)" in note
        and "`(0,1,1)`" in note
        and "tick 3" in note,
    )
    checks.check(
        "thm2-n-refuse-on-first-tick",
        "N_refuse on the first refuse tick is 2",
        n_refuse == 2
        and "N_refuse = 2" in note
        and refuse_tick == 3,
    )
    locked_before = set(SPLIT_SEED)
    earlier_remaining_refuses = 0
    first_tick_refuses: list[tuple[Site, Config, OrbitType, str]] = []
    for tick in range(1, refuse_tick + 1):
        events = remaining_bit_events(f_nt, locked_before)
        refuses = remaining_bit_refuses(events)
        if tick < refuse_tick:
            earlier_remaining_refuses += len(refuses)
        else:
            first_tick_refuses = refuses
        nxt = set(locked_before)
        for site, _config, _kind, _label, value in events:
            if value:
                nxt.add(site)
        locked_before = nxt
    checks.check(
        "thm2-two-vertex3-refuses-and-no-earlier",
        "the first refuse tick has two vertex3 sites and no earlier remaining-bit refuse",
        earlier_remaining_refuses == 0
        and len(first_tick_refuses) == 2
        and first_tick_refuses[0] == ((0, 1, 1), (1, 0, 0, 1, 0, 1), (3, 0, 0), "vertex3")
        and first_tick_refuses[1] == ((2, 1, 1), (0, 1, 0, 1, 0, 1), (3, 0, 0), "vertex3")
        and all(label == "vertex3" for _s, _c, _k, label in first_tick_refuses)
        and "(2,1,1)" in note.replace(" ", ""),
    )
    checks.check(
        "thm3-displayed-not-adopted",
        "the vertex3 refuse and vertex3-flipped contrast are displayed, not adopted",
        contrast_remaining == CONTRAST_REMAINING
        and contrast_remaining != nt_remaining
        and contrast_remaining[3] == 1
        and contrast_fills is True
        and NT_REMAINING != L1_REMAINING
        and "Do not adopt `vertex3`" in note
        and "Do not adopt a bit" in note
        and "Displayed, not adopted" in note
        and "do not adopt" in note_flat.lower(),
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
        "bounded theorem, displayed-not-adopted refuse, and machine status",
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
        "note-reports-refuse",
        "the note names f_nt, the seed, the refuse, and N_refuse",
        "(wt1, opp2, adj2, vertex3, mixed3)" in note
        and "(1, 0, 1, 0, 0)" in note
        and "{(1, 0, 0)}" in note
        and "vertex3" in note
        and "N_refuse = 2" in note
        and "Mechanism of `Q_*` non-totality" in note,
    )
    checks.check(
        "no-axiom-edit",
        "the theorem proposes no axiom change and does not adopt a bit",
        "no axiom or approved primitive is added" in note
        and "hypothetical_axiom_status" in note
        and "Do not adopt a bit" in note
        and "Do not write the ranking into Admissibility" in note
        and "Do not write `Q_*` or `vertex3=1` into" in note,
    )
    checks.check(
        "off-patch-zero",
        "off-patch occupancy is the explicit 0 default, not a blank-block",
        "off-patch occupancy `0`" in note and "blank-block is a different rule" in note,
    )
    checks.check(
        "not-leftover-q1split",
        "the residual is the refuse mechanism, not leftover-character of the q1split census",
        "Not leftover-character of the `q1split` seed census" in note
        and "Mechanism of `Q_*` non-totality" in note
        and "Not leftover-character of #6473" in note,
    )
    checks.check(
        "claim-scope-refuse",
        "claim_scope reports the first remaining-bit refuse of F_cut (1,0,1,0,0) from S",
        "On the two-cube with off-patch o=0" in note
        and "first remaining-bit refuse of F_cut (1,0,1,0,0)" in note
        and "S={(1,0,0)}" in note
        and "Displayed, not adopted" in note,
    )

    print("per_element: checked exactly — each of the 64 neighbor 6-tuples is assigned its axis-type orbit")
    print("per_site: checked exactly — each of the twelve two-cube vertices uses the same six-direction stencil")
    print("per_mode: checked exactly — f_nt is evolved from S={(1, 0, 0)} and compared with f_L1 and the vertex3 contrast")
    print("per_block: checked exactly — first remaining-bit refuse, N_refuse, and halt size are exact on this patch")
    print("lattice_wide: checked and not executed — no Z^3-wide formation law or physical Admissibility selector is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
