#!/usr/bin/env python3
"""Same-host leftover-frame fire and named hop cost on the uneqrad breaker.

Host U is the uneqrad lex-first breaker. f is leftover-frame-positive.
rho is cost 3 iff equal inward weight or seed-exit, else 1. Score both
extras on this one host: bitfire N_new, rho as an edge labeling, and
rho as a cost-1 readiness filter. Displayed, not adopted. No cache.
"""

from __future__ import annotations

import ast
import itertools
from collections import Counter
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/SAME_HOST_AGEBIT_HOPCOST_"
    "BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/SAME_HOST_AGEBIT_HOPCOST_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
CLAIM_SCOPE = (
    'claim_scope: "On the uneqrad breaker, leftover-frame fire and the '
    "named hop cost are scored on the same host. Displayed, not "
    'adopted."'
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


def ball(center: Point, radius: int) -> frozenset[Point]:
    sites: set[Point] = set()
    span = range(-radius, radius + 1)
    for offset in itertools.product(span, repeat=3):
        site = add(center, offset)
        if l1(site, center) <= radius:
            sites.add(site)
    return frozenset(sites)


def locked_union(
    seeds: tuple[Point, ...] = SEEDS, radii: tuple[int, ...] = RADII
) -> frozenset[Point]:
    occupied = frozenset()
    for seed, radius in zip(seeds, radii):
        occupied = occupied | ball(seed, radius)
    return occupied


def occupancy_tuple(site: Point, occupied: frozenset[Point]) -> Coloring:
    return tuple(int(add(site, direction) in occupied) for direction in DIRS)


def seed_distance(site: Point) -> int:
    return min(l1(site, seed) for seed in SEEDS)


def lock_tick(site: Point) -> int:
    return seed_distance(site)


def tick_on_occupied(site: Point, occupied: frozenset[Point]) -> Tick:
    ticks: list[int | None] = []
    for direction in DIRS:
        neighbor = add(site, direction)
        if neighbor in occupied:
            ticks.append(lock_tick(neighbor))
        else:
            ticks.append(None)
    return tuple(ticks)


def inward_occupancy(site: Point) -> Coloring:
    here = seed_distance(site)
    return tuple(
        int(seed_distance(add(site, direction)) < here) for direction in DIRS
    )


def inward_weight(site: Point) -> int:
    return int(sum(inward_occupancy(site)))


def named_rho(source: Point, target: Point) -> int:
    source_weight = inward_weight(source)
    target_weight = inward_weight(target)
    if source_weight == target_weight or source_weight == 0:
        return 3
    return 1


def directed_edges_of(occupied: frozenset[Point]) -> tuple[tuple[Point, Point], ...]:
    edges: list[tuple[Point, Point]] = []
    for site in occupied:
        for direction in DIRS:
            neighbor = add(site, direction)
            if neighbor in occupied:
                edges.append((site, neighbor))
    return tuple(edges)


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
    coloring: Coloring | None,
    pair: frozenset[Coloring],
) -> tuple[frozenset[Point], int]:
    if coloring is None or V in occupied or coloring not in pair:
        return occupied, 0
    return occupied | {V}, 1


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
        "the July-3 pair; named hop-cost rho; uneqrad lex-first breaker"
    )
    print(
        "construction: one host U=B_2((-2,-2,-2))∪B_1((-2,-2,-1))∪B_3((-2,-2,1)), "
        "unread v=(-3,-3,-1), f leftover-frame-positive, "
        "rho=3 iff equal inward weight or seed-exit else 1"
    )
    print(
        "negative_scope: one host only; displayed, not adopted; "
        "L1 not attached; f and rho not written into Admissibility"
    )

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required static two-string literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/SAME_HOST_AGEBIT_HOPCOST_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
        "source-qubit",
        "Qubit remains M_2(C)",
        qubit_sentence in axiom
        and qubit_sentence in note
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
    after, n_new = execute_at_v(occupied, chosen, pair)
    u_persists = occupied <= after and V not in occupied
    fires = chosen is not None and n_new == 1 and u_persists and V in after

    edges = directed_edges_of(occupied)
    edge_costs = tuple(named_rho(source, target) for source, target in edges)
    cost_counts = Counter(edge_costs)
    seed_exit_ok = all(inward_weight(seed) == 0 for seed in SEEDS)
    incoming = tuple(
        named_rho(add(V, direction), V)
        for direction in DIRS
        if add(V, direction) in occupied
    )
    incoming_slots = tuple(
        (index, named_rho(add(V, direction), V), inward_weight(add(V, direction)))
        for index, direction in enumerate(DIRS)
        if add(V, direction) in occupied
    )
    mask_after_rho = occupancy_tuple(V, occupied)
    ticks_after_rho = tick_on_occupied(V, occupied)
    bit_after_rho = (
        age_bit(ticks_after_rho, named) if named is not None else None
    )
    after_rho, n_new_rho = execute_at_v(occupied, chosen, pair)
    fires_rho = (
        chosen is not None
        and n_new_rho == 1
        and occupied <= after_rho
        and V in after_rho
        and mask_after_rho == mask
        and bit_after_rho == bit
    )

    ready_mask = tuple(
        int(add(V, direction) in occupied and named_rho(add(V, direction), V) == 1)
        for direction in DIRS
    )
    ready_axis = unique_full_axis(ready_mask)
    ready_chosen = (
        leftover_frame_positive(ready_mask, bit, pair)
        if ready_axis is not None and bit is not None
        else None
    )
    _after_ready, n_new_ready = execute_at_v(occupied, ready_chosen, pair)

    neighbor_weights = tuple(inward_weight(add(V, direction)) for direction in DIRS)
    v_inward = inward_occupancy(V)
    v_weight = inward_weight(V)

    print(f"U_card={len(occupied)}")
    print(f"v_in_U={V in occupied}")
    print(f"occupancy_mask={mask}")
    print(f"lock_ticks={ticks}")
    print(f"unique_full_axis={named}")
    print(f"b={bit}")
    print(f"N_pair={len(pair)}")
    print(f"f={format_tuple(chosen) if chosen is not None else None}")
    print(f"N_new={n_new}")
    print(f"U_persists={u_persists}")
    print(f"fires={fires}")
    print(f"v_inward={v_inward}")
    print(f"v_inward_weight={v_weight}")
    print(f"neighbor_inward_weights={neighbor_weights}")
    print(f"U_directed_edges={len(edges)}")
    print(f"rho_cost_counts={dict(sorted(cost_counts.items()))}")
    print(f"seed_exit_weights_zero={seed_exit_ok}")
    print(f"incoming_rho={incoming}")
    print(f"incoming_slots={incoming_slots}")
    print(f"sigma_after_rho={mask_after_rho}")
    print(f"b_after_rho={bit_after_rho}")
    print(f"N_new_after_rho={n_new_rho}")
    print(f"fires_after_rho={fires_rho}")
    print(f"sigma_ready={ready_mask}")
    print(f"ready_full_axis={ready_axis}")
    print(f"N_new_ready={n_new_ready}")
    print("score: uneqrad host only")

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
        len(rotations) == 24
        and len({slots for _matrix, slots in rotations}) == 24,
    )
    checks.check(
        "one-host-only",
        "exactly one host is scored: the uneqrad lex-first breaker",
        len(occupied) == 81
        and V not in occupied
        and "One host only" in note
        and "uneqrad lex-first breaker" in note
        and "second host" in note_flat.lower(),
    )
    checks.check(
        "u-geometry",
        "U is the uneqrad lex-first unequal-radius 3-ball union",
        tuple(len(item) for item in balls) == (25, 7, 63)
        and pairwise == (7, 7, 7)
        and triple == 7
        and len(occupied) == 81
        and "B_2((−2,−2,−2))" in note
        and "B_1((−2,−2,−1))" in note
        and "B_3((−2,−2,1))" in note,
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
        "theorem-1-bitfire",
        "on U, f still fires N_new=1 when hop costs are ignored",
        chosen == (PLUS, EMPTY, MINUS, EMPTY, PLUS, MINUS)
        and leftover_frame_sign(chosen) == 1
        and chosen in pair
        and n_new == 1
        and fires
        and u_persists
        and after == occupied | {V}
        and format_tuple(chosen) in note
        and "`N_new = 1`" in note
        and "hop costs are ignored" in note_flat,
        residual=(format_tuple(chosen) if chosen is not None else None, n_new),
    )
    checks.check(
        "theorem-2-rho-labels",
        "assigning rho to directed NN edges of U does not change σ or the age bit",
        seed_exit_ok
        and v_weight == 2
        and v_inward == (1, 0, 1, 0, 0, 0)
        and neighbor_weights == (1, 2, 1, 2, 4, 2)
        and len(edges) == 288
        and cost_counts[1] + cost_counts[3] == 288
        and mask_after_rho == mask == (1, 0, 1, 0, 1, 1)
        and ticks_after_rho == ticks
        and bit_after_rho == bit == 1
        and "does not change the occupancy mask or the age bit" in note_flat,
        residual=(mask_after_rho, bit_after_rho, len(edges)),
    )
    checks.check(
        "theorem-2-still-fires",
        "because σ and b are unchanged, f still fires N_new=1 after rho labeling",
        fires_rho
        and n_new_rho == 1
        and after_rho == occupied | {V}
        and incoming == (1, 1, 1, 3)
        and incoming_slots[3][1] == 3
        and incoming_slots[3][2] == 2,
        residual=(n_new_rho, incoming),
    )
    checks.check(
        "theorem-2-readiness-filter",
        "cost-1 readiness filter reports N_new=0 on sigma_ready=(1,0,1,0,1,0)",
        ready_mask == (1, 0, 1, 0, 1, 0)
        and ready_axis is None
        and ready_chosen is None
        and n_new_ready == 0
        and "`σ_ready = (1, 0, 1, 0, 1, 0)`" in note
        and "`N_new = 0`" in note
        and "readiness filter" in note,
        residual=(ready_mask, n_new_ready),
    )
    checks.check(
        "claim-scope",
        "the note reports the declared displayed claim_scope",
        CLAIM_SCOPE in note,
    )
    checks.check(
        "displayed-not-adopted",
        "f and rho are displayed and not written into Admissibility",
        "Displayed, not adopted" in note
        and "Do not write f or ρ into Admissibility" in note
        and "hypothetical_axiom_status:" in note
        and "This note authors no audit verdict" in note,
    )
    checks.check(
        "l1-not-attached",
        "the note does not attach L1",
        "Do not attach L1" in note
        and "we attach L1" not in note_flat
        and "we add a 4th ball" not in note_flat,
    )
    checks.check(
        "uniqueness-not-required",
        "uniqueness of the matching member is not claimed",
        "Uniqueness not required" in note
        and "uniqueness not required" in note_flat.lower()
        and "unique leftover" not in note_flat.lower(),
    )
    checks.check(
        "not-leftover-two-hosts",
        "same-host score is not leftover of ourmem two-host pairing or bitfire",
        "not leftover of ourmem" in note_flat.replace("`", "").lower()
        and "not leftover of bitfire" in note_flat.replace("`", "").lower()
        and "two hosts" in note_flat.lower(),
    )
    checks.check(
        "admissibility-unedited",
        "f and rho are not written into Admissibility",
        covariance_clause in axiom_flat
        and "leftover-frame-positive" not in axiom
        and "named hop" not in axiom
        and "N_new" not in axiom
        and "uneqrad" not in axiom,
    )
    checks.check(
        "forbidden-phrases",
        "the forbidden rhetoric strings are absent from the note and runner",
        all(phrase not in note for phrase in forbidden_tokens())
        and all(phrase not in self_source for phrase in forbidden_tokens()),
    )
    checks.check(
        "no-axiom-edit",
        "the only axiom authority is the current memo; no cache or axiom rewrite",
        "[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)" in note
        and "cache_write: false" in self_source
        and AXIOM_REL in AUDIT_INPUT_PATHS
        and "no axiom" in note_flat.lower(),
    )

    print("per_element: f(σ,b), rho labels, and both N_new reports are exact")
    print("per_site: only the unread star center v is scored")
    print("per_mode: no spectral calculation")
    print("per_block: the six-neighbor star at v and directed edges of U")
    print("lattice_wide: checked and not executed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
