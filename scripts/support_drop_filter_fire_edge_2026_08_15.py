#!/usr/bin/env python3
"""Support-drop cost of leftover-frame fire edges on the uneqrad host.

Host U is the uneqrad lex-first breaker. f is leftover-frame-positive.
nu is the noshrt support-drop hop-cost: cost 3 iff seed-exit or both
coordinate supports 1 or support drop, else 1. Report which leftover-
frame fire edges have nu-cost 1 and confirm the fire slot is among
them. Also report N_filt_fire on the 12 lex-first perp-mask hosts.
Displayed, not adopted. No cache.
"""

from __future__ import annotations

import ast
import itertools
from array import array
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/SUPPORT_DROP_FILTER_FIRE_EDGE_"
    "BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/SUPPORT_DROP_FILTER_FIRE_EDGE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Point = tuple[int, int, int]
Coloring = tuple[int, ...]
Tick = tuple[int | None, ...]
Host = tuple[tuple[Point, Point, Point], tuple[int, int, int], Point]
Matrix = tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]

DIRS: tuple[Point, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
DIR_INDEX = {direction: index for index, direction in enumerate(DIRS)}
AXES: tuple[tuple[int, int], ...] = ((0, 1), (2, 3), (4, 5))
AXIS_NAME = ("x", "y", "z")
SLOT_NAME = ("+x", "−x", "+y", "−y", "+z", "−z")
EMPTY, PLUS, MINUS = 0, 1, 2
LETTER = {EMPTY: "0", PLUS: "+", MINUS: "−"}
SHIFT = 5
STRIDE = 11
GRID = STRIDE * STRIDE * STRIDE
V: Point = (-3, -3, -1)
SEEDS: tuple[Point, ...] = ((-2, -2, -2), (-2, -2, -1), (-2, -2, 1))
RADII: tuple[int, ...] = (2, 1, 3)
CLAIM_SCOPE = (
    'claim_scope: "The leftover-frame fire edge on the uneqrad host '
    "has support-drop cost 1, so a cost-1 filter does not kill fire. "
    'Displayed, not adopted."'
)
BITREAL_HOSTS: dict[Coloring, Host] = {
    (0, 1, 0, 1, 1, 1): (
        ((-2, -2, -2), (-2, -2, -1), (-2, -2, 0)),
        (2, 1, 2),
        (-1, -1, -1),
    ),
    (0, 1, 1, 0, 1, 1): (
        ((-2, -2, -2), (-2, -2, -1), (-2, -2, 0)),
        (2, 1, 2),
        (-1, -3, -1),
    ),
    (0, 1, 1, 1, 0, 1): (
        ((-2, -2, -2), (-2, -2, -1), (-2, 0, -2)),
        (1, 1, 2),
        (-1, -1, -1),
    ),
    (0, 1, 1, 1, 1, 0): (
        ((-2, -2, -2), (-2, -2, -1), (-2, 0, -2)),
        (1, 2, 1),
        (-1, -1, -2),
    ),
    (1, 0, 0, 1, 1, 1): (
        ((-2, -2, -2), (-2, -2, -1), (-2, -2, 0)),
        (2, 1, 2),
        (-3, -1, -1),
    ),
    (1, 0, 1, 0, 1, 1): (
        ((-2, -2, -2), (-2, -2, -1), (-2, -2, 0)),
        (2, 1, 2),
        (-3, -3, -1),
    ),
    (1, 0, 1, 1, 0, 1): (
        ((-2, -2, -2), (-2, -2, -1), (-2, 0, -2)),
        (1, 1, 2),
        (-3, -1, -1),
    ),
    (1, 0, 1, 1, 1, 0): (
        ((-2, -2, -2), (-2, -2, -1), (-2, 0, -2)),
        (1, 2, 1),
        (-3, -1, -2),
    ),
    (1, 1, 0, 1, 0, 1): (
        ((-2, -2, -2), (-2, -2, -1), (0, -2, -2)),
        (1, 1, 2),
        (-1, -1, -1),
    ),
    (1, 1, 0, 1, 1, 0): (
        ((-2, -2, -2), (-2, -2, -1), (0, -2, -2)),
        (1, 2, 1),
        (-1, -1, -2),
    ),
    (1, 1, 1, 0, 0, 1): (
        ((-2, -2, -2), (-2, -2, -1), (0, -2, -2)),
        (1, 1, 2),
        (-1, -3, -1),
    ),
    (1, 1, 1, 0, 1, 0): (
        ((-2, -2, -2), (-2, -2, -1), (0, -2, -2)),
        (1, 2, 1),
        (-1, -3, -2),
    ),
}


def forbidden_tokens() -> tuple[str, ...]:
    return (
        "G" + "_N",
        "1/" + "r",
        "1/" + "r^2",
        "Lattice-" + "named",
        "not a " + "TOE",
    )


def normalize(text: str) -> str:
    return " ".join(text.split())


def add(left: Point, right: Point) -> Point:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


def l1(left: Point, right: Point) -> int:
    return abs(left[0] - right[0]) + abs(left[1] - right[1]) + abs(left[2] - right[2])


def ball(center: Point, radius: int) -> tuple[Point, ...]:
    sites: list[Point] = []
    span = range(-radius, radius + 1)
    for offset in itertools.product(span, repeat=3):
        if abs(offset[0]) + abs(offset[1]) + abs(offset[2]) <= radius:
            sites.append(add(center, offset))
    return tuple(sites)


def enc(point: Point) -> int:
    return (point[0] + SHIFT) + STRIDE * (
        (point[1] + SHIFT) + STRIDE * (point[2] + SHIFT)
    )


def perp_masks() -> tuple[Coloring, ...]:
    records: list[Coloring] = []
    for mask in itertools.product((0, 1), repeat=len(DIRS)):
        if sum(mask) != 4:
            continue
        empty = [index for index, bit in enumerate(mask) if bit == 0]
        axes = {index // 2 for index in empty}
        if len(axes) == 2:
            records.append(mask)
    return tuple(records)


def locked_union(seeds: tuple[Point, ...], radii: tuple[int, ...]) -> frozenset[Point]:
    occupied: set[Point] = set()
    for seed, radius in zip(seeds, radii):
        occupied.update(ball(seed, radius))
    return frozenset(occupied)


def occupancy_tuple(site: Point, occupied: frozenset[Point]) -> Coloring:
    return tuple(int(add(site, direction) in occupied) for direction in DIRS)


def lock_tick(site: Point, seeds: tuple[Point, ...]) -> int:
    return min(l1(site, seed) for seed in seeds)


def tick_on_occupied(
    site: Point,
    occupied: frozenset[Point],
    seeds: tuple[Point, ...],
) -> Tick:
    ticks: list[int | None] = []
    for direction in DIRS:
        neighbor = add(site, direction)
        if neighbor in occupied:
            ticks.append(lock_tick(neighbor, seeds))
        else:
            ticks.append(None)
    return tuple(ticks)


def support_size(point: Point) -> int:
    return int(sum(1 for coord in point if coord != 0))


def named_nu(source: Point, target: Point) -> int:
    source_support = support_size(source)
    target_support = support_size(target)
    if (
        source_support == 0
        or (source_support == 1 and target_support == 1)
        or target_support < source_support
    ):
        return 3
    return 1


def support(coloring: Coloring) -> Coloring:
    return tuple(int(slot != EMPTY) for slot in coloring)


def det3(matrix: Matrix) -> int:
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def mat_vec(matrix: Matrix, vector: Point) -> Point:
    return (
        matrix[0][0] * vector[0] + matrix[0][1] * vector[1] + matrix[0][2] * vector[2],
        matrix[1][0] * vector[0] + matrix[1][1] * vector[1] + matrix[1][2] * vector[2],
        matrix[2][0] * vector[0] + matrix[2][1] * vector[1] + matrix[2][2] * vector[2],
    )


def direction_perm(matrix: Matrix) -> tuple[int, ...]:
    return tuple(DIR_INDEX[mat_vec(matrix, direction)] for direction in DIRS)


def act_col(perm: tuple[int, ...], coloring: Coloring | tuple) -> tuple:
    out = [None] * len(coloring)
    for source, image in enumerate(perm):
        out[image] = coloring[source]
    return tuple(out)


def proper_rotations() -> tuple[tuple[Matrix, tuple[int, ...]], ...]:
    records: list[tuple[Matrix, tuple[int, ...]]] = []
    seen: set[tuple[int, ...]] = set()
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            rows = []
            for row, col in enumerate(perm):
                entry = [0, 0, 0]
                entry[col] = signs[row]
                rows.append(tuple(entry))
            matrix = (rows[0], rows[1], rows[2])
            if det3(matrix) != 1:
                continue
            slots = direction_perm(matrix)
            if slots not in seen:
                seen.add(slots)
                records.append((matrix, slots))
    return tuple(records)


def inversion_perm() -> tuple[int, ...]:
    return direction_perm(((-1, 0, 0), (0, -1, 0), (0, 0, -1)))


def july3_k3_pair() -> frozenset[Coloring]:
    proper = [slots for _matrix, slots in proper_rotations()]
    inversion = inversion_perm()
    unseen = set(itertools.product(range(3), repeat=6))
    pair: set[Coloring] = set()
    while unseen:
        seed = min(unseen)
        orbit = {act_col(perm, seed) for perm in proper}
        unseen -= orbit
        image = act_col(inversion, next(iter(orbit)))
        if image not in orbit:
            pair |= orbit
    return frozenset(pair)


def unique_full_axis(sigma: Coloring) -> int | None:
    named = tuple(
        axis_index
        for axis_index, (plus, minus) in enumerate(AXES)
        if sigma[plus] == 1 and sigma[minus] == 1
    )
    if len(named) == 1:
        return named[0]
    return None


def age_bit(ticks: Tick, axis_index: int) -> int:
    plus, minus = AXES[axis_index]
    minus_tick = ticks[minus]
    plus_tick = ticks[plus]
    if minus_tick is not None and plus_tick is not None and minus_tick < plus_tick:
        return 1
    return 0


def axis_letters(bit: int) -> tuple[int, int]:
    if bit == 1:
        return (PLUS, MINUS)
    return (MINUS, PLUS)


def completions(
    sigma: Coloring,
    bit: int,
    pair: frozenset[Coloring],
) -> tuple[Coloring, ...]:
    named = unique_full_axis(sigma)
    if named is None:
        return ()
    plus, minus = AXES[named]
    plus_letter, minus_letter = axis_letters(bit)
    matches = [
        item
        for item in pair
        if support(item) == sigma
        and item[plus] == plus_letter
        and item[minus] == minus_letter
    ]
    return tuple(sorted(matches))


def leftover_frame_sign(coloring: Coloring) -> int:
    named = unique_full_axis(support(coloring))
    if named is None:
        raise AssertionError("completion has no unique full axis")
    leftover = [
        index
        for index in range(6)
        if support(coloring)[index] == 1 and index not in AXES[named]
    ]
    plus_left = next(index for index in leftover if coloring[index] == PLUS)
    minus_left = next(index for index in leftover if coloring[index] == MINUS)
    plus_full = next(index for index in AXES[named] if coloring[index] == PLUS)
    return det3((DIRS[plus_left], DIRS[minus_left], DIRS[plus_full]))


def leftover_slots(sigma: Coloring) -> tuple[int, ...]:
    named = unique_full_axis(sigma)
    if named is None:
        return ()
    return tuple(
        index
        for index in range(6)
        if sigma[index] == 1 and index not in AXES[named]
    )


def leftover_frame_positive(
    sigma: Coloring,
    bit: int,
    pair: frozenset[Coloring],
) -> Coloring | None:
    found = completions(sigma, bit, pair)
    positive = [item for item in found if leftover_frame_sign(item) == 1]
    if len(positive) != 1:
        return None
    return positive[0]


def format_tuple(coloring: Coloring) -> str:
    return "(" + ", ".join(LETTER[slot] for slot in coloring) + ")"


def format_mask(mask: Coloring) -> str:
    return "(" + ", ".join(str(slot) for slot in mask) + ")"


def format_ticks(ticks: Tick) -> str:
    parts = ["·" if tick is None else str(tick) for tick in ticks]
    return "(" + ", ".join(parts) + ")"


def format_point(point: Point) -> str:
    return "(" + ", ".join(str(coord) for coord in point) + ")"


def execute_at_v(
    occupied: frozenset[Point],
    site: Point,
    coloring: Coloring | None,
    pair: frozenset[Coloring],
) -> tuple[frozenset[Point], int]:
    if coloring is None or site in occupied or coloring not in pair:
        return occupied, 0
    return occupied | {site}, 1


def realize_hosts() -> dict[Coloring, Host]:
    masks = perp_masks()
    remaining = set(masks)
    hosts: dict[Coloring, Host] = {}
    seed_box = tuple(itertools.product(range(-2, 3), repeat=3))
    v_box = tuple(itertools.product(range(-4, 5), repeat=3))
    radii_opts = tuple(
        radii
        for radii in itertools.product((1, 2, 3), repeat=3)
        if not (radii[0] == radii[1] == radii[2])
    )
    ball_enc = {
        (seed, radius): tuple(enc(site) for site in ball(seed, radius))
        for seed in seed_box
        for radius in (1, 2, 3)
    }
    v_enc = tuple(enc(site) for site in v_box)
    neighbor_enc = tuple(
        tuple(enc(add(site, direction)) for direction in DIRS) for site in v_box
    )
    mark = array("I", [0]) * GRID
    generation = 0
    for s1, s2, s3 in itertools.combinations(seed_box, 3):
        seeds = (s1, s2, s3)
        for radii in radii_opts:
            generation += 1
            for seed, radius in zip(seeds, radii):
                for index in ball_enc[(seed, radius)]:
                    mark[index] = generation
            for v_index, site in enumerate(v_box):
                if mark[v_enc[v_index]] == generation:
                    continue
                sigma = tuple(
                    1 if mark[w_enc] == generation else 0
                    for w_enc in neighbor_enc[v_index]
                )
                if sum(sigma) != 4:
                    continue
                if sigma in remaining:
                    remaining.remove(sigma)
                    hosts[sigma] = (seeds, radii, site)
            if not remaining:
                return hosts
    return hosts


def parse_audit_input_paths(source: str) -> object:
    tree = ast.parse(source)
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id == "AUDIT_INPUT_PATHS":
                return ast.literal_eval(node.value)
    raise AssertionError("AUDIT_INPUT_PATHS assignment is missing")


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, condition: bool, detail: str = "") -> None:
        ok = bool(condition)
        self.passed += int(ok)
        self.failed += int(not ok)
        suffix = f" | {detail}" if detail else ""
        print(f"{'PASS' if ok else 'FAIL'}: {label}{suffix}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def score_filt_host(
    sigma: Coloring,
    host: Host,
    pair: frozenset[Coloring],
) -> dict:
    seeds, radii, site = host
    occupied = locked_union(seeds, radii)
    mask = occupancy_tuple(site, occupied)
    ticks = tick_on_occupied(site, occupied, seeds)
    named = unique_full_axis(mask)
    bit = age_bit(ticks, named) if named is not None else None
    ready_mask = tuple(
        int(
            add(site, direction) in occupied
            and named_nu(add(site, direction), site) == 1
        )
        for direction in DIRS
    )
    ready_axis = unique_full_axis(ready_mask)
    ready_chosen = (
        leftover_frame_positive(ready_mask, bit, pair)
        if ready_axis is not None and bit is not None
        else None
    )
    _after_ready, n_new_ready = execute_at_v(occupied, site, ready_chosen, pair)
    incoming_nu = tuple(
        named_nu(add(site, direction), site)
        for direction in DIRS
        if add(site, direction) in occupied
    )
    fires_filt = ready_chosen is not None and n_new_ready == 1 and ready_chosen in pair
    rebuild = mask == sigma and site not in occupied and host == BITREAL_HOSTS[sigma]
    return {
        "sigma": sigma,
        "rebuild": rebuild,
        "incoming_nu": incoming_nu,
        "ready_mask": ready_mask,
        "n_new_filt": n_new_ready,
        "fires_filt": fires_filt,
    }


def main() -> int:
    checks = Checks()
    note_path = ROOT / NOTE_REL
    axiom_path = ROOT / AXIOM_REL
    note = note_path.read_text(encoding="utf-8")
    axiom = axiom_path.read_text(encoding="utf-8")
    note_flat = normalize(note)
    axiom_flat = normalize(axiom)
    self_source = Path(__file__).read_text(encoding="utf-8")
    literal_paths = parse_audit_input_paths(self_source)
    masks = perp_masks()
    hosts = realize_hosts()
    pair = july3_k3_pair()
    rotations = proper_rotations()

    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print(
        "external_scientific_inputs: current Lattice, Qubit, Admissibility, "
        "and Record sentences; leftover-frame-positive section rebuilt from "
        "the July-3 pair; named support-drop hop-cost nu; uneqrad lex-first "
        "breaker; nuclk 12 lex-first perp-mask hosts"
    )
    print(
        "construction: one uneqrad host; leftover-frame fire edges of f; "
        "nu=3 iff seed-exit or both supports 1 or support drop else 1; "
        "plus N_filt_fire on the 12 lex-first perp-mask hosts"
    )
    print(
        "negative_scope: one host plus the 12-count check; displayed, not "
        "adopted; L1 not attached; f and nu not written into Admissibility"
    )

    occupied = locked_union(SEEDS, RADII)
    mask = occupancy_tuple(V, occupied)
    ticks = tick_on_occupied(V, occupied, SEEDS)
    named = unique_full_axis(mask)
    bit = age_bit(ticks, named) if named is not None else None
    chosen = leftover_frame_positive(mask, bit, pair) if bit is not None else None
    after, n_new = execute_at_v(occupied, V, chosen, pair)
    u_persists = occupied <= after and V not in occupied
    leftover = leftover_slots(mask)
    fire_slot = None
    if chosen is not None:
        fire_slot = next(index for index in leftover if chosen[index] == PLUS)
    leftover_edges = []
    for index in leftover:
        source = add(V, DIRS[index])
        cost = named_nu(source, V)
        leftover_edges.append((index, source, V, support_size(source), support_size(V), cost))
    cost1_slots = tuple(index for index, _s, _t, _a, _b, cost in leftover_edges if cost == 1)
    fire_edge_cost = None
    fire_source = None
    if fire_slot is not None:
        fire_source = add(V, DIRS[fire_slot])
        fire_edge_cost = named_nu(fire_source, V)
    incoming_all = tuple(
        (
            index,
            add(V, DIRS[index]),
            named_nu(add(V, DIRS[index]), V),
            support_size(add(V, DIRS[index])),
        )
        for index, direction in enumerate(DIRS)
        if add(V, direction) in occupied
    )

    print(f"U_card={len(occupied)}")
    print(f"v={format_point(V)} v_in_U={V in occupied}")
    print(f"occupancy_mask={mask}")
    print(f"lock_ticks={ticks}")
    print(f"unique_full_axis={AXIS_NAME[named] if named is not None else None}")
    print(f"b={bit}")
    print(f"f={format_tuple(chosen) if chosen is not None else None}")
    print(f"N_new={n_new} U_persists={u_persists}")
    print(
        "leftover_frame_slots="
        + ",".join(SLOT_NAME[index] for index in leftover)
    )
    print(f"fire_slot={SLOT_NAME[fire_slot] if fire_slot is not None else None}")
    for index, source, target, src_w, tgt_w, cost in leftover_edges:
        print(
            f"leftover_edge slot={SLOT_NAME[index]} "
            f"{format_point(source)}->{format_point(target)} "
            f"|s|={src_w} |t|={tgt_w} nu={cost}"
        )
    print(
        "cost1_leftover_slots="
        + ",".join(SLOT_NAME[index] for index in cost1_slots)
    )
    print(
        f"directed_fire_edge={format_point(fire_source) if fire_source is not None else None}"
        f"->{format_point(V)} nu={fire_edge_cost}"
    )
    print(
        "incoming_occupied="
        + ",".join(
            f"{SLOT_NAME[index]}:{cost}"
            for index, _source, cost, _weight in incoming_all
        )
    )

    filt_rows = [score_filt_host(sigma, hosts[sigma], pair) for sigma in masks]
    n_filt_fire = sum(1 for row in filt_rows if row["fires_filt"])
    print(f"N_filt_fire={n_filt_fire}")
    print("score: one host plus the 12-count check")

    expected_paths = (
        "docs/SUPPORT_DROP_FILTER_FIRE_EDGE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
        "docs/MINIMAL_AXIOMS_2026-06-29.md",
    )
    checks.check(
        "audit-input-paths",
        AUDIT_INPUT_PATHS == expected_paths
        and literal_paths == AUDIT_INPUT_PATHS
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and AUDIT_TIMEOUT_SEC == 120,
        "AUDIT_INPUT_PATHS is the required static two-string literal tuple",
    )

    lattice_sentence = (
        "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor"
    )
    admissibility_sentence = (
        "For each site, the probability distribution over the possibilities is "
        "determined by, and varies with, the nearest-neighbor conditions."
    )
    covariance_clause = (
        "one fixed nearest-neighbor admissibility rule, covariant under "
        "lattice translations and proper cubic rotations"
    )
    formation_boundary = "it does not supply the formation site, probability,"
    qubit_sentence = (
        "The full one-site possibility domain has algebraic presentation `M_2(C)`."
    )
    record_lock = "When present, a record locks exactly one admissible local possibility."
    record_perm = "A site never carries more than one record; records are permanent."
    record_content = "A readout value is determined by record content alone."
    record_absence = "A site with no record cannot be read."

    checks.check(
        "source-lattice",
        lattice_sentence in axiom and lattice_sentence in note,
    )
    checks.check(
        "source-admissibility",
        admissibility_sentence in axiom_flat and admissibility_sentence in note_flat,
    )
    checks.check(
        "source-covariance",
        covariance_clause in axiom_flat and covariance_clause in note_flat,
    )
    checks.check(
        "source-formation-boundary",
        formation_boundary in axiom and formation_boundary in note,
    )
    checks.check(
        "source-qubit",
        qubit_sentence in axiom
        and qubit_sentence in note
        and "Qubit remains `M_2(C)`" in note,
    )
    checks.check(
        "source-record",
        all(
            phrase in axiom_flat
            for phrase in (record_lock, record_perm, record_content, record_absence)
        )
        and all(
            phrase in note
            for phrase in (record_lock, record_perm, record_content, record_absence)
        ),
    )
    checks.check(
        "g-plus-order",
        len(rotations) == 24
        and len({slots for _matrix, slots in rotations}) == 24
        and len(pair) == 48,
        f"N_G+={len(rotations)} N_pair={len(pair)}",
    )
    checks.check(
        "uneqrad-host",
        V not in occupied
        and mask == (1, 0, 1, 0, 1, 1)
        and ticks == (1, None, 1, None, 3, 2)
        and named == 2
        and bit == 1
        and chosen == (PLUS, EMPTY, MINUS, EMPTY, PLUS, MINUS)
        and leftover_frame_sign(chosen) == 1
        and chosen in pair
        and n_new == 1
        and u_persists
        and leftover == (0, 2)
        and "`σ = (1, 0, 1, 0, 1, 1)`" in note
        and "`t = (1, ·, 1, ·, 3, 2)`" in note
        and "`b = [t(−z) < t(+z)] = 1`" in note
        and "`f = (+, 0, −, 0, +, −)`" in note
        and "B_2((−2,−2,−2))" in note
        and "B_1((−2,−2,−1))" in note
        and "B_3((−2,−2,1))" in note
        and "`v = (−3,−3,−1)`" in note,
        f"mask={mask} t={ticks} f={format_tuple(chosen) if chosen else None}",
    )
    checks.check(
        "theorem-1-fire-edge-cost-1",
        fire_slot == 0
        and fire_edge_cost == 1
        and fire_source == (-2, -3, -1)
        and cost1_slots == (0, 2)
        and leftover == (0, 2)
        and fire_slot in cost1_slots
        and all(cost == 1 for _i, _s, _t, _a, _b, cost in leftover_edges)
        and "`ν`-cost 1" in note
        and "fire slot" in note
        and "`+x`" in note
        and "`(−2,−3,−1) → (−3,−3,−1)`" in note
        and "`(−3,−2,−1) → (−3,−3,−1)`" in note
        and "The directed fire edge of `f` on `U` has `ν`-cost 1" in note,
        (
            f"fire_slot={SLOT_NAME[fire_slot] if fire_slot is not None else None} "
            f"cost1={tuple(SLOT_NAME[i] for i in cost1_slots)} "
            f"fire_nu={fire_edge_cost}"
        ),
    )
    checks.check(
        "theorem-2-n-filt-fire",
        n_filt_fire == 12
        and len(filt_rows) == 12
        and all(row["rebuild"] for row in filt_rows)
        and all(row["fires_filt"] and row["n_new_filt"] == 1 for row in filt_rows)
        and all(row["incoming_nu"] == (1, 1, 1, 1) for row in filt_rows)
        and hosts == BITREAL_HOSTS
        and "`N_filt_fire = 12`" in note
        and "12 lex-first perp-mask hosts" in note
        and "Displayed, not adopted" in note,
        f"N_filt_fire={n_filt_fire}",
    )
    checks.check("claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "displayed-not-adopted",
        "Displayed, not adopted" in note
        and "Do not write f or ν into Admissibility" in note
        and "hypothetical_axiom_status:" in note
        and "This note authors no audit verdict" in note,
    )
    checks.check(
        "l1-not-attached",
        "Do not attach L1" in note
        and "we attach L1" not in note_flat
        and "we add a 4th ball" not in note_flat,
    )
    checks.check(
        "not-leftover-12-count",
        "not leftover of the 12/12 count" in note_flat.replace("`", "").lower()
        and "one host plus the 12-count check" in note_flat.lower(),
    )
    checks.check(
        "admissibility-unedited",
        covariance_clause in axiom_flat
        and "leftover-frame-positive" not in axiom
        and "N_filt_fire" not in axiom
        and "uneqrad" not in axiom
        and "hop-cost" not in axiom,
    )
    checks.check(
        "forbidden-phrases",
        all(phrase not in note for phrase in forbidden_tokens())
        and all(phrase not in self_source for phrase in forbidden_tokens()),
    )
    checks.check(
        "no-axiom-edit",
        "[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)" in note
        and "cache_write: false" in self_source
        and AXIOM_REL in AUDIT_INPUT_PATHS
        and "no axiom" in note_flat.lower(),
    )

    print("per_element: leftover-frame fire-edge nu costs and N_filt_fire are exact")
    print("per_site: uneqrad unread center plus the 12 lex-first realizing hosts")
    print("per_mode: no spectral calculation")
    print("per_block: one host plus the 12-count check")
    print("lattice_wide: checked and not executed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
