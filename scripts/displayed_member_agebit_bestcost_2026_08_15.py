#!/usr/bin/env python3
"""Displayed member: leftover-frame-positive section plus best hop cost.

Member M = (f, c) pairs the bitsec leftover-frame-positive July-3 pair
section with the B_3 variance-minimizing hop cost
c = (3, 1, 3, 1, 1, 3, 1, 1). Both our-physics probes are scored on
their hosts: fire of f on the uneqrad lex-first breaker, and diamond
reversal plus variance of c on B_3(0). Displayed, not adopted.
Uniqueness of M is not claimed. No cache is written.
"""

from __future__ import annotations

import ast
import heapq
import itertools
import math
from collections import defaultdict
from decimal import Decimal, getcontext
from pathlib import Path


getcontext().prec = 80

AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/DISPLAYED_MEMBER_AGEBIT_BESTCOST_"
    "BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/DISPLAYED_MEMBER_AGEBIT_BESTCOST_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Point = tuple[int, int, int]
Coloring = tuple[int, ...]
Tick = tuple[int | None, ...]
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
EMPTY, PLUS, MINUS = 0, 1, 2
LETTER = {EMPTY: "0", PLUS: "+", MINUS: "−"}
V: Point = (-3, -3, -1)
SEEDS: tuple[Point, ...] = ((-2, -2, -2), (-2, -2, -1), (-2, -2, 1))
RADII: tuple[int, ...] = (2, 1, 3)
ORIGIN: Point = (0, 0, 0)
AXIS: Point = (3, 0, 0)
DIAG: Point = (1, 1, 1)
ORBIT_TYPES: tuple[Point, ...] = (
    (1, 0, 0),
    (2, 0, 0),
    (1, 1, 0),
    (3, 0, 0),
    (2, 1, 0),
    (1, 1, 1),
)
DISPLAYED_C: tuple[int, ...] = (3, 1, 3, 1, 1, 3, 1, 1)
EXPECTED_WEIGHTS = (
    (0, 1),
    (1, 0),
    (1, 1),
    (1, 2),
    (2, 1),
    (2, 2),
    (2, 3),
    (3, 2),
)
CLAIM_SCOPE = (
    'claim_scope: "One displayed member pairing the leftover-frame pair '
    "section with the B_3 variance-minimizing hop cost is scored on both "
    'our-physics hosts. Displayed, not adopted."'
)


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


def graph_radius(point: Point) -> int:
    return abs(point[0]) + abs(point[1]) + abs(point[2])


def euclid2(point: Point) -> int:
    return point[0] * point[0] + point[1] * point[1] + point[2] * point[2]


def ball(center: Point, radius: int) -> frozenset[Point]:
    sites: set[Point] = set()
    span = range(-radius, radius + 1)
    for offset in itertools.product(span, repeat=3):
        site = add(center, offset)
        if l1(site, center) <= radius:
            sites.add(site)
    return frozenset(sites)


def origin_ball(radius: int) -> tuple[Point, ...]:
    sites: list[Point] = []
    span = range(-radius, radius + 1)
    for coords in itertools.product(span, repeat=3):
        if graph_radius(coords) <= radius:
            sites.append(coords)
    return tuple(sites)


def locked_union(
    seeds: tuple[Point, ...] = SEEDS, radii: tuple[int, ...] = RADII
) -> frozenset[Point]:
    occupied: frozenset[Point] = frozenset()
    for seed, radius in zip(seeds, radii):
        occupied = occupied | ball(seed, radius)
    return occupied


def occupancy_tuple(site: Point, occupied: frozenset[Point]) -> Coloring:
    return tuple(int(add(site, direction) in occupied) for direction in DIRS)


def lock_tick(site: Point) -> int:
    return min(l1(site, seed) for seed in SEEDS)


def tick_on_occupied(site: Point, occupied: frozenset[Point]) -> Tick:
    ticks: list[int | None] = []
    for direction in DIRS:
        neighbor = add(site, direction)
        if neighbor in occupied:
            ticks.append(lock_tick(neighbor))
        else:
            ticks.append(None)
    return tuple(ticks)


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


def execute_at_v(
    occupied: frozenset[Point],
    coloring: Coloring,
    pair: frozenset[Coloring],
) -> tuple[frozenset[Point], int]:
    if V in occupied:
        return occupied, 0
    if coloring not in pair:
        return occupied, 0
    return occupied | {V}, 1


def occupancy_bits(point: Point) -> int:
    bits = 0
    for index, shift in enumerate(DIRS):
        neighbor = add(point, shift)
        if graph_radius(neighbor) < graph_radius(point):
            bits |= 1 << index
    return bits


def apply_bits(perm: tuple[int, ...], bits: int) -> int:
    out = 0
    for index in range(6):
        if bits >> index & 1:
            out |= 1 << perm[index]
    return out


def apply_pair(perm: tuple[int, ...], pair: tuple[int, int]) -> tuple[int, int]:
    return (apply_bits(perm, pair[0]), apply_bits(perm, pair[1]))


def orbit_rep(pair: tuple[int, int], perms: tuple[tuple[int, ...], ...]) -> tuple[int, int]:
    return min(apply_pair(perm, pair) for perm in perms)


def directed_edges(sites: tuple[Point, ...]) -> tuple[tuple[Point, Point], ...]:
    present = set(sites)
    edges: list[tuple[Point, Point]] = []
    for site in sites:
        for shift in DIRS:
            neighbor = add(site, shift)
            if neighbor in present:
                edges.append((site, neighbor))
    return tuple(edges)


def shortest_all(
    start: Point,
    adj: dict[Point, list[tuple[Point, int]]],
    costs: tuple[int, ...],
) -> dict[Point, int]:
    dist = {start: 0}
    heap: list[tuple[int, Point]] = [(0, start)]
    while heap:
        current, node = heapq.heappop(heap)
        if current != dist[node]:
            continue
        for neighbor, orbit in adj[node]:
            trial = current + costs[orbit]
            prior = dist.get(neighbor)
            if prior is None or trial < prior:
                dist[neighbor] = trial
                heapq.heappush(heap, (trial, neighbor))
    return dist


def reverses(t_axis: int, t_diag: int) -> bool:
    return 3 * t_axis * t_axis > 9 * t_diag * t_diag


def ratio_list(dist: dict[Point, int], sites: tuple[Point, ...]) -> list[Decimal]:
    values: list[Decimal] = []
    for point in sites:
        if point == ORIGIN:
            continue
        arrival = dist[point]
        values.append(Decimal(euclid2(point)).sqrt() / Decimal(arrival))
    return values


def population_variance(values: list[Decimal]) -> Decimal:
    count = Decimal(len(values))
    mean = sum(values) / count
    return sum((item - mean) ** 2 for item in values) / count


def rounded(value: Decimal, places: int) -> str:
    quantize = Decimal(10) ** -places
    return format(value.quantize(quantize), "f")


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

    def check(
        self,
        label: str,
        statement: str,
        condition: bool,
        residual: object | None = None,
    ) -> None:
        ok = bool(condition)
        self.passed += int(ok)
        self.failed += int(not ok)
        print(f"{'PASS' if ok else 'FAIL'}: {label} {statement}")
        if not ok and residual is not None:
            print(f"  residual: {residual}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


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

    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print(
        "external_scientific_inputs: current Lattice, Qubit, Admissibility, "
        "and Record sentences; leftover-frame-positive section rebuilt from "
        "the July-3 pair; uneqrad lex-first breaker; B_3(0) hop-cost host"
    )
    print(
        "construction: M=(f,c) with f leftover-frame-positive and "
        "c=(3,1,3,1,1,3,1,1); hosts are the uneqrad star and B_3(0)"
    )
    print(
        "negative_scope: displayed, not adopted; uniqueness of M is not "
        "claimed; L1 not attached; neither extra written into Admissibility"
    )

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required static two-string literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/DISPLAYED_MEMBER_AGEBIT_BESTCOST_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and literal_paths == AUDIT_INPUT_PATHS
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and AUDIT_TIMEOUT_SEC == 120,
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
        "current cubic nearest-neighbor wording is pinned",
        lattice_sentence in axiom and lattice_sentence in note,
    )
    checks.check(
        "source-admissibility",
        "current local-distribution wording is pinned",
        admissibility_sentence in axiom_flat and admissibility_sentence in note_flat,
    )
    checks.check(
        "source-covariance",
        "Admissibility still requires one proper-cubic covariant rule",
        covariance_clause in axiom_flat and covariance_clause in note_flat,
    )
    checks.check(
        "source-formation-boundary",
        "formation site/probability/rate remains outside Admissibility",
        formation_boundary in axiom and formation_boundary in note,
    )
    checks.check(
        "source-unread-qubit",
        "Qubit remains M_2(C) and unread sites cannot be read",
        qubit_sentence in axiom
        and qubit_sentence in note
        and record_absence in axiom
        and record_absence in note
        and "Qubit remains `M_2(C)`" in note,
    )
    checks.check(
        "source-record",
        "lock, permanence, content-only readout, and unreadability at absence are pinned",
        all(
            phrase in axiom_flat
            for phrase in (record_lock, record_perm, record_content, record_absence)
        )
        and all(
            phrase in note
            for phrase in (record_lock, record_perm, record_content, record_absence)
        ),
    )

    occupied = locked_union()
    mask = occupancy_tuple(V, occupied)
    ticks = tick_on_occupied(V, occupied)
    rotations = proper_rotations()
    pair = july3_k3_pair()
    named = unique_full_axis(mask)
    bit = age_bit(ticks, named) if named is not None else None
    found = completions(mask, bit, pair) if bit is not None else ()
    chosen = leftover_frame_positive(mask, bit, pair) if bit is not None else None
    after, n_new = (
        execute_at_v(occupied, chosen, pair)
        if chosen is not None
        else (occupied, 0)
    )
    u_persists = occupied <= after and V not in occupied
    fires = chosen is not None and n_new == 1 and u_persists and V in after

    perms = tuple(slots for _matrix, slots in rotations)
    sites = origin_ball(3)
    edges = directed_edges(sites)
    pairs = tuple((occupancy_bits(src), occupancy_bits(dst)) for src, dst in edges)
    reps = tuple(sorted({orbit_rep(pair_bits, perms) for pair_bits in pairs}))
    rep_index = {rep: index for index, rep in enumerate(reps)}
    adj: dict[Point, list[tuple[Point, int]]] = defaultdict(list)
    for src, dst in edges:
        adj[src].append(
            (dst, rep_index[orbit_rep((occupancy_bits(src), occupancy_bits(dst)), perms)])
        )
    weights = tuple((bin(rep[0]).count("1"), bin(rep[1]).count("1")) for rep in reps)
    l1_dist = {point: graph_radius(point) for point in sites}
    var_l1 = population_variance(ratio_list(l1_dist, sites))
    best_dist = shortest_all(ORIGIN, adj, DISPLAYED_C)
    var_best = population_variance(ratio_list(best_dist, sites))
    best_times = (best_dist[AXIS], best_dist[DIAG])
    type_times = tuple(best_dist[point] for point in ORBIT_TYPES)
    diamond = reverses(best_times[0], best_times[1])

    print(f"U_card={len(occupied)}")
    print(f"v={V}")
    print(f"occupancy_mask={mask}")
    print(f"lock_ticks={ticks}")
    print(f"unique_full_axis={named}")
    print(f"b={bit}")
    print(f"N_pair={len(pair)}")
    print(f"f={format_tuple(chosen) if chosen is not None else None}")
    print(
        f"leftover_frame_sign={leftover_frame_sign(chosen) if chosen is not None else None}"
    )
    print(f"N_new={n_new}")
    print(f"U_persists={u_persists}")
    print(f"fires={fires}")
    print(f"orbit_weights={weights}")
    print(f"c={DISPLAYED_C}")
    print(f"best_times={best_times}")
    print(f"best_type_times={type_times}")
    print(f"diamond_reverses={diamond}")
    print(f"var_best={format(var_best, 'f')}")
    print(f"var_l1={format(var_l1, 'f')}")
    print("score: uneqrad star and B_3(0) only")

    balls = tuple(ball(seed, radius) for seed, radius in zip(SEEDS, RADII))
    pairwise = (
        len(balls[0] & balls[1]),
        len(balls[0] & balls[2]),
        len(balls[1] & balls[2]),
    )
    triple = len(balls[0] & balls[1] & balls[2])

    checks.check(
        "g-plus-order",
        "finite G+ is exactly the 24 proper cube rotations",
        len(rotations) == 24 and len(set(perms)) == 24,
    )
    checks.check(
        "finite-hosts",
        "both our-physics hosts are finite and named in the note",
        len(occupied) == 81
        and len(sites) == 63
        and sum(1 for point in sites if point != ORIGIN) == 62
        and "Finite hosts only" in note
        and "B_3(0)" in note
        and "uneqrad lex-first breaker" in note,
    )
    checks.check(
        "u-geometry",
        "U is the uneqrad lex-first unequal-radius 3-ball union",
        tuple(len(item) for item in balls) == (25, 7, 63)
        and pairwise == (7, 7, 7)
        and triple == 7
        and V not in occupied
        and "B_2((−2,−2,−2))" in note
        and "B_1((−2,−2,−1))" in note
        and "B_3((−2,−2,1))" in note
        and "Same host as bitfire" in note,
    )
    checks.check(
        "occupancy-and-ticks",
        "σ, t, unique full axis, and b=[t(−z)<t(+z)] match the uneqrad star",
        mask == (1, 0, 1, 0, 1, 1)
        and ticks == (1, None, 1, None, 3, 2)
        and named == 2
        and bit == 1
        and ticks[5] is not None
        and ticks[4] is not None
        and ticks[5] < ticks[4]
        and "`σ = (1, 0, 1, 0, 1, 1)`" in note
        and "`t = (1, ·, 1, ·, 3, 2)`" in note
        and "`b = 1`" in note,
    )
    checks.check(
        "theorem-1-fire",
        "on the uneqrad lex-first breaker, f still fires N_new=1",
        chosen is not None
        and chosen == (PLUS, EMPTY, MINUS, EMPTY, PLUS, MINUS)
        and leftover_frame_sign(chosen) == 1
        and chosen in pair
        and len(found) == 2
        and len(pair) == 48
        and n_new == 1
        and u_persists
        and fires
        and after == occupied | {V}
        and format_tuple(chosen) in note
        and "`N_new = 1`" in note
        and "one unread site becomes occupied" in note
        and "Same host as bitfire" in note
        and "July-3 pair" in note,
        residual=(format_tuple(chosen) if chosen is not None else None, n_new),
    )
    checks.check(
        "theorem-2-hop-cost",
        "on B_3(0), c realizes t(3,0,0)=9, t(1,1,1)=5, diamond reverses, and variance beats ell^1",
        len(reps) == 8
        and weights == EXPECTED_WEIGHTS
        and best_times == (9, 5)
        and diamond
        and 3 * 81 > 9 * 25
        and type_times == (3, 6, 4, 9, 7, 5)
        and rounded(var_best, 14) == "0.00017588571746"
        and rounded(var_l1, 14) == "0.02073945514155"
        and var_best < var_l1
        and "(3, 1, 3, 1, 1, 3, 1, 1)" in note
        and "t(3,0,0) = 9" in note
        and "t(1,1,1) = 5" in note
        and "0.00017588571746" in note
        and "0.02073945514155" in note
        and "diamond reverses" in note
        and "ell^1" in note,
        residual=(best_times, rounded(var_best, 14), rounded(var_l1, 14)),
    )
    checks.check(
        "member-pairing",
        "the note displays M=(f,c) as one member scored on both hosts",
        "M = (f, c)" in note
        and "leftover-frame-positive" in note
        and "one displayed member" in note
        and "both our-physics hosts" in note,
    )
    checks.check(
        "claim-scope",
        "the note reports the declared displayed claim_scope",
        CLAIM_SCOPE in note,
    )
    checks.check(
        "displayed-not-adopted",
        "the pairing is displayed and neither extra is written into Admissibility",
        "Displayed, not adopted" in note
        and "Neither extra is written into Admissibility" in note
        and "Do not write f into Admissibility" in note
        and "hypothetical_axiom_status:" in note
        and "This note authors no audit verdict" in note,
    )
    checks.check(
        "uniqueness-not-claimed",
        "uniqueness of M is not claimed and is not required",
        "Uniqueness of `M` is not claimed" in note
        and "Uniqueness not required" in note,
    )
    checks.check(
        "l1-not-attached",
        "the note does not attach L1",
        "Do not attach L1" in note
        and "we attach L1" not in note_flat
        and "we add a 4th ball" not in note_flat
        and "no path-length law" in note_flat.lower(),
    )
    checks.check(
        "not-leftover-either-probe",
        "the pairing is not leftover of either probe alone",
        "not leftover of either probe alone" in note_flat
        and "bitfire" in note
        and "minkbest" in note,
    )
    checks.check(
        "admissibility-unedited",
        "neither extra is written into Admissibility",
        covariance_clause in axiom_flat
        and "leftover-frame-positive" not in axiom
        and "N_new" not in axiom
        and "two-end occupancy" not in axiom
        and "displayed member" not in axiom,
    )
    checks.check(
        "forbidden-phrases",
        "the forbidden rhetoric strings are absent from the note and runner",
        all(token not in note and token not in self_source for token in forbidden_tokens()),
    )
    checks.check(
        "no-axiom-edit",
        "the only axiom authority is the current memo; no cache or axiom rewrite",
        "[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)" in note
        and "cache_write: false" in self_source
        and AXIOM_REL in AUDIT_INPUT_PATHS
        and "no axiom" in note_flat.lower(),
    )
    checks.check(
        "claim-type-and-gate",
        "bounded theorem type and a passing N1-N8 gate are source-visible",
        "**Type:** bounded_theorem" in note
        and all(f"### N{index}" in note for index in range(1, 9))
        and "No-Go Discipline disposition: **PASS**" in note
        and note.count("**ATTEMPTED**") == 6,
    )

    print("per_element: f(σ,b), N_new, and each directed B_3(0) edge are exact")
    print("per_site: unread star center v and the 62 nonzero ball sites")
    print("per_mode: one leftover-frame section and one hop-cost 8-tuple")
    print("per_block: fire report plus population variance of |v|_2/t on B_3(0)")
    print("lattice_wide: checked and not executed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
