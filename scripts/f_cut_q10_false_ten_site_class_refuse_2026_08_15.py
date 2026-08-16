#!/usr/bin/env python3
"""Whether all four Q10-false maps first-refuse the same remaining-bit type.

F_cut is the cube-covariant class with f(empty)=f(full)=0 and f(c)=f(1-c).
Dynamics are occupancy-to-lock on the twelve-vertex two-cube with off-patch
occupancy 0. The four zeros are the maps with adj2=vertex3=mixed3=0. S is
the lex-first 10-site seed that f1 fills. For each of the four maps the first
remaining-bit refuse type from S is reported, or N_refuse=0. Whether all four
such first refuses have the same type is displayed; it does not adopt a bit.
f_L1 is the unbalanced-axis predicate (some n_mu != 0), never Hamming
|c|_1 mod 2. New object: not leftover of the single-map first refuse of
f_z0=(0,0,0,0,0). Class fact of the Q10 zeros.
"""

from __future__ import annotations

from itertools import combinations, permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/F_CUT_Q10_FALSE_TEN_SITE_CLASS_REFUSE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/F_CUT_Q10_FALSE_TEN_SITE_CLASS_REFUSE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Direction = tuple[int, int, int]
Config = tuple[int, int, int, int, int, int]
Rotation = tuple[tuple[int, int, int], tuple[int, int, int]]
OrbitType = tuple[int, int, int]
Site = tuple[int, int, int]
Seed = tuple[Site, Site, Site, Site, Site, Site, Site, Site, Site, Site]
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
TEN_SITE_SEEDS: tuple[frozenset[Site], ...] = tuple(
    frozenset(combo) for combo in combinations(TWO_CUBE, 10)
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
L1_REMAINING: Remaining = (1, 0, 1, 1, 1)
F1_REMAINING: Remaining = (1, 1, 1, 1, 1)
FZ0_REMAINING: Remaining = (0, 0, 0, 0, 0)
SEED_S_SITES: Seed = (
    (0, 0, 0),
    (0, 0, 1),
    (0, 1, 0),
    (0, 1, 1),
    (1, 0, 0),
    (1, 0, 1),
    (1, 1, 0),
    (1, 1, 1),
    (2, 0, 0),
    (2, 0, 1),
)
Q10_FALSE_CLASS: tuple[Remaining, ...] = (
    (0, 0, 0, 0, 0),
    (0, 1, 0, 0, 0),
    (1, 0, 0, 0, 0),
    (1, 1, 0, 0, 0),
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


def make_predicate(remaining: tuple[int, ...]):
    def predicate(config: Config) -> int:
        return remaining_value(config, remaining)

    return predicate


def f1(config: Config) -> int:
    """F_cut remaining bits (1, 1, 1, 1, 1).  Displayed.  Not adopted."""
    return remaining_value(config, F1_REMAINING)


def f_z0(config: Config) -> int:
    """Lex-first Q10-false remaining-bit map."""
    return remaining_value(config, FZ0_REMAINING)


def q10(remaining: tuple[int, ...]) -> int:
    return int(remaining[2] == 1 or remaining[3] == 1 or remaining[4] == 1)


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


def seed_key(seed: frozenset[Site]) -> Seed:
    ordered = tuple(sorted(seed))
    if len(ordered) != 10:
        raise ValueError("expected 10-site seed")
    return (
        ordered[0],
        ordered[1],
        ordered[2],
        ordered[3],
        ordered[4],
        ordered[5],
        ordered[6],
        ordered[7],
        ordered[8],
        ordered[9],
    )


def seed_display(seed: frozenset[Site] | Seed) -> str:
    sites = seed_key(frozenset(seed))
    inner = ",".join(f"({a[0]},{a[1]},{a[2]})" for a in sites)
    return "{" + inner + "}"


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
                "f_map": int(predicate(config)),
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


def class_first_refuses(seed: frozenset[Site], members: tuple[Remaining, ...]) -> list[dict]:
    rows: list[dict] = []
    for remaining in members:
        predicate = make_predicate(remaining)
        first = first_remaining_refuse(seed, predicate)
        if first is None:
            rows.append(
                {
                    "remaining": remaining,
                    "n_refuse": 0,
                    "tick": None,
                    "site": None,
                    "remaining_name": None,
                    "remaining_type": None,
                    "config": None,
                    "fills": fills_from_seed(predicate, seed),
                    "history": run_from_seed(predicate, seed)["history"],
                }
            )
            continue
        rows.append(
            {
                "remaining": remaining,
                "n_refuse": first["n_events"],
                "tick": first["tick"],
                "site": first["site"],
                "remaining_name": first["remaining_name"],
                "remaining_type": first["remaining_type"],
                "config": first["config"],
                "fills": fills_from_seed(predicate, seed),
                "history": run_from_seed(predicate, seed)["history"],
            }
        )
    return rows


def coverage_ten(predicate) -> int:
    return sum(1 for seed in TEN_SITE_SEEDS if fills_from_seed(predicate, seed))


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


def remaining_bits_from_assignment(assignment: dict[OrbitType, int]) -> Remaining:
    values = tuple(assignment[orbit_type] for orbit_type in REMAINING_ORDER)
    return (values[0], values[1], values[2], values[3], values[4])


def remaining_bits_from_full(
    bits: tuple[int, ...], orbit_types: tuple[OrbitType, ...]
) -> Remaining:
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
        if complement_type(orbit_type) != orbit_type
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
) -> list[Remaining]:
    free_pairs, free_fixed = f_cut_free_data(orbit_types, empty_type, full_type)
    n_free = len(free_pairs) + len(free_fixed)
    members: list[Remaining] = []
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


def remaining_display(remaining: tuple[int, ...]) -> str:
    return "(" + ", ".join(str(bit) for bit in remaining) + ")"


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
    print("construction: first remaining-bit refuse of each Q10-false map from S")
    print("negative_scope: adj2 is displayed, not adopted or written into Admissibility")

    orbits = build_orbits()
    orbit_types = tuple(sorted(orbits))
    orbit_sizes = {orbit_type: len(orbits[orbit_type]) for orbit_type in orbit_types}
    empty_type = axis_type(EMPTY)
    full_type = axis_type(FULL)
    free_pairs, free_fixed = f_cut_free_data(orbit_types, empty_type, full_type)
    n_free = len(free_pairs) + len(free_fixed)
    remaining_members = enumerate_f_cut_remaining(orbit_types, empty_type, full_type)

    cov10_by_remaining = {
        remaining: coverage_ten(make_predicate(remaining)) for remaining in remaining_members
    }
    zeros = tuple(
        sorted(
            remaining
            for remaining in remaining_members
            if remaining[2] == 0 and remaining[3] == 0 and remaining[4] == 0
        )
    )
    zeros_by_cov = tuple(
        sorted(remaining for remaining in remaining_members if cov10_by_remaining[remaining] == 0)
    )
    lex_first_zero = zeros[0]

    l1_bits = bits_from_predicate(f_L1, orbit_types, orbits)
    f1_bits = bits_from_predicate(f1, orbit_types, orbits)
    fz0_bits = bits_from_predicate(f_z0, orbit_types, orbits)
    ham_bits = bits_from_predicate(f_hamming, orbit_types, orbits)
    l1_remaining = remaining_bits_from_full(l1_bits, orbit_types)
    f1_remaining = remaining_bits_from_full(f1_bits, orbit_types)
    fz0_remaining = remaining_bits_from_full(fz0_bits, orbit_types)

    seed_s = frozenset(SEED_S_SITES)
    lex_first_filled_by_f1 = next(seed for seed in TEN_SITE_SEEDS if fills_from_seed(f1, seed))
    run_f1 = run_from_seed(f1, seed_s)
    run_fz0 = run_from_seed(f_z0, seed_s)
    class_rows = class_first_refuses(seed_s, zeros)
    types = [row["remaining_name"] for row in class_rows]
    same_type = (
        len(class_rows) == 4
        and all(row["n_refuse"] != 0 for row in class_rows)
        and len(set(types)) == 1
    )
    counterexamples = [
        row
        for row in class_rows
        if row["n_refuse"] == 0
        or row["remaining_name"] != class_rows[0]["remaining_name"]
    ]
    lex_first_counterexample = None
    if not same_type:
        lex_first_counterexample = counterexamples[0] if counterexamples else class_rows[0]

    print(f"n_rotations={len(ROTATIONS)}")
    print(f"n_orbits={len(orbit_types)}")
    print("orbit_types_and_sizes=" + ",".join(f"{t}:{orbit_sizes[t]}" for t in orbit_types))
    print(f"remaining_labels={REMAINING_LABELS}")
    print(f"N_free={n_free}")
    print(f"|F_cut|={len(remaining_members)}")
    print(f"N_Q10={sum(1 for member in remaining_members if q10(member) == 1)}")
    print(f"N_cov10={sum(1 for count in cov10_by_remaining.values() if count > 0)}")
    print(f"N_zeros={len(zeros)}")
    print(f"zeros_class={list(zeros)}")
    print(f"f_z0_remaining={fz0_remaining}")
    print(f"f1_remaining={f1_remaining}")
    print(f"f_L1_remaining={l1_remaining}")
    print(f"S={seed_display(seed_s)}")
    print(f"f1_fills_S={run_f1['fill']}")
    print(f"f1_history={run_f1['history']}")
    for row in class_rows:
        print(
            "zero "
            + remaining_display(row["remaining"])
            + f" tick={row['tick']} site={row['site']} "
            + f"type={row['remaining_name']} N_refuse={row['n_refuse']} "
            + f"fills_S={row['fills']} history={row['history']}"
        )
    print(f"same_first_refuse_type={same_type}")
    print(f"shared_type={types[0] if same_type else None}")
    if not same_type:
        print(f"named_types={types}")

    checks.check(
        "audit-inputs",
        "AUDIT_INPUT_PATHS are the required static literals and both files exist",
        AUDIT_INPUT_PATHS
        == (
            "docs/F_CUT_Q10_FALSE_TEN_SITE_CLASS_REFUSE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and AUDIT_TIMEOUT_SEC == 120,
    )
    checks.check(
        "thm1-rotations-orbits-fcut",
        "24 rotations, 10 orbits, and |F_cut|=32",
        len(ROTATIONS) == 24
        and len(orbit_types) == 10
        and len(remaining_members) == 32
        and n_free == 5
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
        "f_L1 is n!=0, not Hamming |c|_1 mod 2",
        l1_bits != ham_bits
        and any(f_L1(config) != f_hamming(config) for config in product((0, 1), repeat=6))
        and "sum(config) % 2"
        not in self_source.split("def f_L1", 1)[1].split("def f_hamming", 1)[0]
        and "n ≠ 0" in note
        and "This is **not** Hamming parity" in note,
    )
    checks.check(
        "thm1-two-cube-and-s-filled-by-f1",
        "the two-cube has twelve vertices and f1 fills the lex-first 10-site seed S",
        len(TWO_CUBE) == 12
        and len(set(TWO_CUBE)) == 12
        and len(TEN_SITE_SEEDS) == 66
        and seed_key(seed_s) == SEED_S_SITES
        and seed_key(lex_first_filled_by_f1) == SEED_S_SITES
        and f1_remaining == F1_REMAINING
        and in_f_cut(f1_bits, orbit_types, empty_type, full_type)
        and run_f1["fill"]
        and run_f1["history"] == (10, 12)
        and not run_fz0["fill"]
        and run_fz0["history"] == (10,),
    )
    checks.check(
        "thm1-q10-false-four-zeros",
        "the four Q10-false remaining-bit tuples are adj2=vertex3=mixed3=0",
        zeros == Q10_FALSE_CLASS
        and zeros == zeros_by_cov
        and lex_first_zero == FZ0_REMAINING
        and fz0_remaining == FZ0_REMAINING
        and all(q10(member) == 0 for member in zeros)
        and all(cov10_by_remaining[member] == 0 for member in zeros)
        and all(member[2] == 0 and member[3] == 0 and member[4] == 0 for member in zeros)
        and all((cov10_by_remaining[member] > 0) == (q10(member) == 1) for member in remaining_members)
        and in_f_cut(fz0_bits, orbit_types, empty_type, full_type),
    )
    checks.check(
        "thm1-class-first-refuse-types",
        "each of the four zeros has a first remaining-bit refuse from S",
        len(class_rows) == 4
        and all(row["n_refuse"] != 0 for row in class_rows)
        and all(row["tick"] == 1 for row in class_rows)
        and all(row["site"] == (2, 1, 0) for row in class_rows)
        and all(row["remaining_name"] == "adj2" for row in class_rows)
        and all(row["remaining_type"] == (2, 0, 1) for row in class_rows)
        and all(row["config"] == (0, 1, 0, 1, 0, 0) for row in class_rows)
        and all(row["n_refuse"] == 2 for row in class_rows)
        and all(not row["fills"] for row in class_rows)
        and all(row["history"] == (10,) for row in class_rows),
    )
    checks.check(
        "thm2-all-four-first-refuse-same-type",
        "all four first refuses have the same type adj2; the four types do not differ",
        same_type
        and lex_first_counterexample is None
        and types == ["adj2", "adj2", "adj2", "adj2"]
        and class_rows[0]["remaining"] == (0, 0, 0, 0, 0)
        and class_rows[1]["remaining"] == (0, 1, 0, 0, 0)
        and class_rows[2]["remaining"] == (1, 0, 0, 0, 0)
        and class_rows[3]["remaining"] == (1, 1, 0, 0, 0)
        and f1((0, 1, 0, 1, 0, 0)) == 1
        and f_z0((0, 1, 0, 1, 0, 0)) == 0,
    )
    checks.check(
        "thm3-display-not-adopt",
        "the Q10-false class first-refuse type is displayed and is not adopted",
        same_type
        and "Displayed, not adopted" in note
        and "Do not adopt a bit" in note
        and "Do not write `adj2` into Admissibility" in note
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
        "On the two-cube with off-patch o=0, whether all four Q10-false maps "
        "first refuse the same remaining-bit type from the lex-first 10-site f1 "
        "fill is reported. Displayed, not adopted."
    )
    checks.check(
        "claim-scope",
        "claim_scope reports whether all four Q10-false maps first refuse the same type from S",
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
        and "Do not write `adj2` into Admissibility" in note,
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
        "note-reports-class-refuse",
        "the note reports the four zeros, S, and first-refuse type adj2",
        "(0, 0, 0, 0, 0)" in note
        and "(0, 1, 0, 0, 0)" in note
        and "(1, 0, 0, 0, 0)" in note
        and "(1, 1, 0, 0, 0)" in note
        and "`S = {(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1), (2, 0, 0), (2, 0, 1)}`"
        in note
        and "N_refuse = 2" in note
        and "`adj2`" in note
        and "(2, 0, 1)" in note
        and "tick `1`" in note
        and "site `(2, 1, 0)`" in note
        and "same type" in note,
    )
    checks.check(
        "not-leftover-c10zero",
        "the residual is Q10 zeros class sameness, not leftover of the single-map refuse",
        "Not leftover-character of the single-map first refuse" in note
        and "f_z0=(0,0,0,0,0)" in note.replace(" ", "")
        and ("New object" in note or "new object" in note)
        and "Class fact of the Q10 zeros" in note_flat,
    )

    print("per_element: checked exactly — each of the 64 neighbor 6-tuples is assigned its axis-type orbit")
    print("per_site: checked exactly — each of the twelve two-cube vertices uses the same six-direction stencil")
    print("per_mode: checked exactly — all four Q10-false zeros are scored from S")
    print("per_block: checked exactly — each first remaining-bit refuse type is named, or N_refuse=0")
    print("lattice_wide: checked and not executed — no Z^3-wide formation law or physical Admissibility selector is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
