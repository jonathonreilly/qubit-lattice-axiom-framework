#!/usr/bin/env python3
"""Pairwise occupied lock-tick order versus occupancy Stab.

U, v, σ, t are the uneqrad lex-first breaker. Order is the relation
i ≺ j on occupied slots with t_i < t_j. Report |Stab(σ)|, |Stab(σ,t)|,
|Stab(σ,≺)|, and N_ord_ok versus N_tick_ok=4. Displayed, not adopted.
No cache is written.
"""

from __future__ import annotations

import ast
import itertools
from array import array
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/UNEQUAL_RADIUS_TICK_ORDER_STAB_"
    "BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/UNEQUAL_RADIUS_TICK_ORDER_STAB_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Point = tuple[int, int, int]
Coloring = tuple[int, ...]
Tick = tuple[int | None, ...]
Matrix = tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]
Order = frozenset[tuple[int, int]]

DIRS: tuple[Point, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
DIR_INDEX = {direction: index for index, direction in enumerate(DIRS)}
SLOT_NAMES = ("+x", "-x", "+y", "-y", "+z", "-z")
EMPTY = 0
SHIFT = 5
STRIDE = 11
GRID = STRIDE * STRIDE * STRIDE
FORBIDDEN = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE")
CLAIM_SCOPE = (
    'claim_scope: "On the lex-first unequal-radius breaker, whether the '
    "pairwise older/newer order of occupied lock-ticks suffices to shrink "
    'Stab is reported. Displayed, not adopted."'
)
UNEQ_SEEDS: tuple[Point, Point, Point] = (
    (-2, -2, -2),
    (-2, -2, -1),
    (-2, -2, 1),
)
UNEQ_RADII = (2, 1, 3)
UNEQ_V: Point = (-3, -3, -1)
EXPECTED_SIGMA: Coloring = (1, 0, 1, 0, 1, 1)
EXPECTED_TICKS: Tick = (1, None, 1, None, 3, 2)
EXPECTED_ORDER: Order = frozenset(((0, 5), (0, 4), (2, 5), (2, 4), (5, 4)))
SWAPPER: Matrix = ((0, 1, 0), (1, 0, 0), (0, 0, -1))


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


def in_union(point: Point, seeds: tuple[Point, ...], radii: tuple[int, ...]) -> bool:
    return any(l1(point, seed) <= radius for seed, radius in zip(seeds, radii))


def sigma_ticks(
    site: Point, seeds: tuple[Point, ...], radii: tuple[int, ...]
) -> tuple[Coloring, Tick]:
    occupied = {
        add(seed, offset)
        for seed, radius in zip(seeds, radii)
        for offset in ball((0, 0, 0), radius)
    }
    sigma_bits: list[int] = []
    ticks_bits: list[int | None] = []
    for direction in DIRS:
        neighbor = add(site, direction)
        if neighbor in occupied:
            sigma_bits.append(1)
            ticks_bits.append(min(l1(neighbor, seed) for seed in seeds))
        else:
            sigma_bits.append(0)
            ticks_bits.append(None)
    return tuple(sigma_bits), tuple(ticks_bits)


def order_from_ticks(ticks: Tick) -> Order:
    pairs: list[tuple[int, int]] = []
    occupied = [index for index, tick in enumerate(ticks) if tick is not None]
    for left, right in itertools.permutations(occupied, 2):
        left_tick = ticks[left]
        right_tick = ticks[right]
        if left_tick is not None and right_tick is not None and left_tick < right_tick:
            pairs.append((left, right))
    return frozenset(pairs)


def format_order(order: Order) -> str:
    named = []
    for left, right in sorted(order):
        named.append(f"({SLOT_NAMES[left]},{SLOT_NAMES[right]})")
    return "{" + ", ".join(named) + "}"


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


def act_col(perm: tuple[int, ...], coloring: Coloring | Tick) -> tuple:
    out = [None] * len(coloring)
    for source, image in enumerate(perm):
        out[image] = coloring[source]
    return tuple(out)


def preserves_order(perm: tuple[int, ...], order: Order) -> bool:
    mapped = frozenset((perm[left], perm[right]) for left, right in order)
    return mapped == order


def stab_orders(
    sigma: Coloring, ticks: Tick, perms: list[tuple[int, ...]]
) -> tuple[int, int, int]:
    order = order_from_ticks(ticks)
    n_stab = 0
    n_stab_tick = 0
    n_stab_ord = 0
    for perm in perms:
        if act_col(perm, sigma) != sigma:
            continue
        n_stab += 1
        if act_col(perm, ticks) == ticks:
            n_stab_tick += 1
        if preserves_order(perm, order):
            n_stab_ord += 1
    return n_stab, n_stab_tick, n_stab_ord


def proper_rotations() -> tuple[Matrix, ...]:
    records: list[Matrix] = []
    seen: set[Matrix] = set()
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            rows = []
            for row, col in enumerate(perm):
                entry = [0, 0, 0]
                entry[col] = signs[row]
                rows.append(tuple(entry))
            matrix = (rows[0], rows[1], rows[2])
            if matrix not in seen and det3(matrix) == 1:
                seen.add(matrix)
                records.append(matrix)
    return tuple(records)


def july3_pair(perms: list[tuple[int, ...]]) -> frozenset[Coloring]:
    unseen = set(itertools.product(range(3), repeat=6))
    inversion = direction_perm(((-1, 0, 0), (0, -1, 0), (0, 0, -1)))
    pair: set[Coloring] = set()
    while unseen:
        seed = min(unseen)
        orbit = {act_col(perm, seed) for perm in perms}
        unseen -= orbit
        image = act_col(inversion, next(iter(orbit)))
        if image not in orbit:
            pair |= orbit
    return frozenset(pair)


def support(coloring: Coloring) -> Coloring:
    return tuple(int(letter != EMPTY) for letter in coloring)


def n_ok(
    sigma: Coloring,
    perms: list[tuple[int, ...]],
    pair: frozenset[Coloring],
    stab_filter,
) -> tuple[int, int, tuple[Coloring, ...]]:
    stab_perms = [perm for perm in perms if stab_filter(perm)]
    members = tuple(sorted(item for item in pair if support(item) == sigma))
    ok = tuple(
        item
        for item in members
        if all(act_col(perm, item) == item for perm in stab_perms)
    )
    return len(members), len(ok), members


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


def first_breaker(perms: list[tuple[int, ...]]) -> tuple | None:
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
    neighbor_pts = tuple(
        tuple(add(site, direction) for direction in DIRS) for site in v_box
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
                sigma_bits: list[int] = []
                ticks_bits: list[int | None] = []
                occupied_ticks: list[int] = []
                for slot, w_enc in enumerate(neighbor_enc[v_index]):
                    if mark[w_enc] == generation:
                        sigma_bits.append(1)
                        tick = min(
                            l1(neighbor_pts[v_index][slot], seed) for seed in seeds
                        )
                        ticks_bits.append(tick)
                        occupied_ticks.append(tick)
                    else:
                        sigma_bits.append(0)
                        ticks_bits.append(None)
                if len(occupied_ticks) != 4:
                    continue
                sigma = tuple(sigma_bits)
                ticks = tuple(ticks_bits)
                n_stab, n_stab_tick, _n_stab_ord = stab_orders(sigma, ticks, perms)
                if n_stab_tick < n_stab:
                    return (seeds, radii, site, sigma, ticks, n_stab, n_stab_tick)
    return None


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
    rotations = proper_rotations()
    perms = [direction_perm(matrix) for matrix in rotations]

    uneq_unread = not in_union(UNEQ_V, UNEQ_SEEDS, UNEQ_RADII)
    uneq_sigma, uneq_ticks = sigma_ticks(UNEQ_V, UNEQ_SEEDS, UNEQ_RADII)
    order = order_from_ticks(uneq_ticks)
    n_stab, n_stab_tick, n_stab_ord = stab_orders(uneq_sigma, uneq_ticks, perms)
    breaker = first_breaker(perms)
    pair = july3_pair(perms)
    n_pair_support, n_ord_ok, members = n_ok(
        uneq_sigma,
        perms,
        pair,
        lambda perm: act_col(perm, uneq_sigma) == uneq_sigma
        and preserves_order(perm, order),
    )
    _n_pair_tick, n_tick_ok, _tick_members = n_ok(
        uneq_sigma,
        perms,
        pair,
        lambda perm: act_col(perm, uneq_sigma) == uneq_sigma
        and act_col(perm, uneq_ticks) == uneq_ticks,
    )
    swap_perm = direction_perm(SWAPPER)

    print("unequal-radius pairwise lock-tick order occupancy Stab")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print(f"G_plus={len(rotations)}")
    print(f"uneq_unread={uneq_unread}")
    print(f"uneq_sigma={uneq_sigma}")
    print(f"uneq_ticks={uneq_ticks}")
    print(f"order={sorted(order)}")
    print(f"order_named={format_order(order)}")
    print(f"|Stab(sigma)|={n_stab}")
    print(f"|Stab(sigma,t)|={n_stab_tick}")
    print(f"|Stab(sigma,prec)|={n_stab_ord}")
    print(f"first_breaker={None if breaker is None else breaker[:3]}")
    print(f"N_pair={len(pair)}")
    print(f"N_pair_support={n_pair_support}")
    print(f"N_ord_ok={n_ord_ok}")
    print(f"N_tick_ok={n_tick_ok}")
    print("support_members=" + ",".join(str(item) for item in members))

    expected_paths = (
        "docs/UNEQUAL_RADIUS_TICK_ORDER_STAB_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
        "Physical sites are the points of the cubic lattice `Z^3`, with "
        "nearest-neighbor adjacency, standard translations, and proper cubic "
        "rotations about each site."
    )
    covariance_clause = (
        "There is one fixed nearest-neighbor admissibility rule, covariant "
        "under lattice translations and proper cubic rotations."
    )
    admissibility_sentence = (
        "For each site, the probability distribution over the possibilities is "
        "determined by, and varies with, the nearest-neighbor conditions."
    )
    unread_sentence = "A site with no record cannot be read."
    qubit_sentence = (
        "The full one-site possibility domain has algebraic presentation `M_2(C)`."
    )
    checks.check(
        "source-lattice",
        lattice_sentence in axiom_flat and lattice_sentence in note_flat,
    )
    checks.check(
        "source-admissibility",
        covariance_clause in axiom_flat
        and admissibility_sentence in axiom_flat
        and covariance_clause in note_flat
        and admissibility_sentence in note_flat,
    )
    checks.check(
        "source-unread-qubit",
        unread_sentence in axiom
        and unread_sentence in note
        and qubit_sentence in axiom
        and qubit_sentence in note,
    )
    checks.check(
        "g-plus-order",
        len(rotations) == 24
        and len(set(rotations)) == 24
        and det3(SWAPPER) == 1
        and SWAPPER in rotations,
        f"proper={len(rotations)}",
    )
    checks.check(
        "theorem-1-lex-first-breaker",
        uneq_unread
        and uneq_sigma == EXPECTED_SIGMA
        and uneq_ticks == EXPECTED_TICKS
        and breaker is not None
        and breaker[:3] == (UNEQ_SEEDS, UNEQ_RADII, UNEQ_V)
        and breaker[3:5] == (EXPECTED_SIGMA, EXPECTED_TICKS)
        and "`σ = (1, 0, 1, 0, 1, 1)`" in note
        and "`t = (1, ·, 1, ·, 3, 2)`" in note
        and "radii `(2, 1, 3)`" in note
        and "`v = (−3,−3,−1)`" in note,
        f"sigma={uneq_sigma} ticks={uneq_ticks}",
    )
    checks.check(
        "theorem-1-list-order",
        order == EXPECTED_ORDER
        and "`≺ = {(+x,−z), (+x,+z), (+y,−z), (+y,+z), (−z,+z)}`" in note
        and "+x" in format_order(order)
        and len(order) == 5,
        f"order={sorted(order)}",
    )
    checks.check(
        "theorem-1-stab-orders",
        n_stab == 2
        and n_stab_tick == 1
        and n_stab_ord == 1
        and "|Stab(σ)| = 2" in note
        and "|Stab(σ,t)| = 1" in note
        and "|Stab(σ,≺)| = 1" in note,
        f"stab={n_stab} tick={n_stab_tick} ord={n_stab_ord}",
    )
    checks.check(
        "theorem-1-swapper-breaks-order",
        act_col(swap_perm, EXPECTED_SIGMA) == EXPECTED_SIGMA
        and act_col(swap_perm, EXPECTED_TICKS) != EXPECTED_TICKS
        and not preserves_order(swap_perm, EXPECTED_ORDER)
        and swap_perm[0] == 2
        and swap_perm[4] == 5
        and "s : (x, y, z) ↦ (y, x, −z)" in note
        and "does not preserve order" in note,
    )
    checks.check(
        "theorem-2-ord-ok",
        n_ord_ok == 4
        and n_tick_ok == 4
        and n_pair_support == 4
        and members
        == (
            (1, 0, 2, 0, 1, 2),
            (1, 0, 2, 0, 2, 1),
            (2, 0, 1, 0, 1, 2),
            (2, 0, 1, 0, 2, 1),
        )
        and "N_ord_ok = 4" in note
        and "N_tick_ok = 4" in note
        and "N_pair_support = 4" in note,
        f"N_ord_ok={n_ord_ok} N_tick_ok={n_tick_ok}",
    )
    checks.check("claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "displayed-not-adopted",
        "Displayed, not adopted" in note
        and "Do not write ≺ into Admissibility" in note
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
        "not-leftover-uneqext",
        "not leftover of uneqext" in note_flat
        and "named the integer field" in note
        and "pairwise order" in note,
    )
    checks.check(
        "admissibility-unedited",
        covariance_clause in axiom_flat
        and "Stab(σ,≺)" not in axiom
        and "N_ord_ok" not in axiom
        and "lock-tick" not in axiom
        and "unequal-radius" not in axiom,
    )
    checks.check(
        "forbidden-phrases",
        all(phrase not in note for phrase in FORBIDDEN)
        and all(
            phrase not in self_source.split("FORBIDDEN = ", 1)[0]
            for phrase in FORBIDDEN
        ),
    )
    checks.check(
        "no-axiom-edit",
        "[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)" in note
        and "cache_write: false" in self_source
        and AXIOM_REL in AUDIT_INPUT_PATHS
        and "no axiom" in note_flat.lower(),
    )

    print("per_element: |Stab(σ)|, |Stab(σ,t)|, |Stab(σ,≺)|, N_ord_ok are exact integers")
    print("per_site: uneqrad lex-first unequal-radius breaker only")
    print("per_mode: no spectral calculation")
    print("per_block: 3-ball star only")
    print("lattice_wide: checked and not executed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
