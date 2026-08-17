#!/usr/bin/env python3
"""Score the named axis-skeleton hop-cost on B_4(0) only.

The named rule alpha assigns cost 3 iff the source is the seed or both
inward weights equal 1, else cost 1. This is the same alpha scored on
B_6(0). On the same B_4(0) sites the runner also scores rho (cost 3 iff
equal inward weight or seed-exit) and ell^1. The residual is whether the
B_3 pair (3,0,0) vs (1,1,1) still reverses, and the order of
var(|v|_2 / t) for alpha, rho, and ell^1. Displayed, not adopted. No
axiom edit and no path-length law. B_4(0) only; not leftover of B_6 times.
"""

from __future__ import annotations

import heapq
from collections import defaultdict
from decimal import Decimal, getcontext
from itertools import permutations, product
from pathlib import Path


getcontext().prec = 80

AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "AXIS_SKELETON_HOPCOST_B4_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/AXIS_SKELETON_HOPCOST_B4_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Point = tuple[int, int, int]
SHIFTS: tuple[Point, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
ORIGIN: Point = (0, 0, 0)
AXIS3: Point = (3, 0, 0)
DIAG3: Point = (1, 1, 1)
AXIS4: Point = (4, 0, 0)
OFF_AXIS_B6: Point = (4, 1, 0)
EXPECTED_WEIGHTS = (
    (0, 1),
    (1, 0),
    (1, 1),
    (1, 2),
    (2, 1),
    (2, 2),
    (2, 3),
    (3, 2),
    (3, 3),
)
ORBIT_TYPES: tuple[Point, ...] = (
    (1, 0, 0),
    (1, 1, 0),
    (1, 1, 1),
    (2, 0, 0),
    (2, 1, 0),
    (2, 1, 1),
    (2, 2, 0),
    (3, 0, 0),
    (3, 1, 0),
    (4, 0, 0),
)


def forbidden_tokens() -> tuple[str, ...]:
    return (
        "G" + "_N",
        "1/" + "r",
        "1/" + "r^2",
        "Lattice-" + "named",
        "not a " + "TOE",
    )


def graph_radius(point: Point) -> int:
    return abs(point[0]) + abs(point[1]) + abs(point[2])


def euclid2(point: Point) -> int:
    return point[0] * point[0] + point[1] * point[1] + point[2] * point[2]


def ball(radius: int) -> tuple[Point, ...]:
    sites: list[Point] = []
    span = range(-radius, radius + 1)
    for coords in product(span, repeat=3):
        if graph_radius(coords) <= radius:
            sites.append(coords)
    return tuple(sites)


def occupancy(point: Point) -> int:
    """6-bit inward occupation of the one-seed front at ``point``."""
    bits = 0
    for index, shift in enumerate(SHIFTS):
        neighbor = (
            point[0] + shift[0],
            point[1] + shift[1],
            point[2] + shift[2],
        )
        if graph_radius(neighbor) < graph_radius(point):
            bits |= 1 << index
    return bits


def inward_weight(point: Point) -> int:
    return bin(occupancy(point)).count("1")


def axis_skeleton_cost(src: Point, dst: Point) -> int:
    """Cost 3 iff seed-exit or both inward weights equal 1, else 1."""
    weight_src = inward_weight(src)
    weight_dst = inward_weight(dst)
    if weight_src == 0 or (weight_src == 1 and weight_dst == 1):
        return 3
    return 1


def equal_weight_cost(src: Point, dst: Point) -> int:
    """Cost 3 iff equal inward weight or seed-exit, else 1."""
    weight_src = inward_weight(src)
    weight_dst = inward_weight(dst)
    if weight_src == weight_dst or weight_src == 0:
        return 3
    return 1


def apply_matrix(matrix: tuple[tuple[int, ...], ...], point: Point) -> Point:
    return (
        matrix[0][0] * point[0] + matrix[0][1] * point[1] + matrix[0][2] * point[2],
        matrix[1][0] * point[0] + matrix[1][1] * point[1] + matrix[1][2] * point[2],
        matrix[2][0] * point[0] + matrix[2][1] * point[1] + matrix[2][2] * point[2],
    )


def determinant(matrix: tuple[tuple[int, ...], ...]) -> int:
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def proper_cubic_rotations() -> tuple[tuple[tuple[int, ...], ...], ...]:
    rotations: list[tuple[tuple[int, ...], ...]] = []
    for perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            rows = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            for src, dest in enumerate(perm):
                rows[src][dest] = signs[src]
            matrix = tuple(tuple(row) for row in rows)
            if determinant(matrix) == 1:
                rotations.append(matrix)
    return tuple(rotations)


def directed_edges(sites: tuple[Point, ...]) -> tuple[tuple[Point, Point], ...]:
    present = set(sites)
    edges: list[tuple[Point, Point]] = []
    for site in sites:
        for shift in SHIFTS:
            neighbor = (site[0] + shift[0], site[1] + shift[1], site[2] + shift[2])
            if neighbor in present:
                edges.append((site, neighbor))
    return tuple(edges)


def shortest_named(
    start: Point,
    adj: dict[Point, list[tuple[Point, int]]],
) -> dict[Point, int]:
    dist = {start: 0}
    heap: list[tuple[int, Point]] = [(0, start)]
    while heap:
        current, node = heapq.heappop(heap)
        if current != dist[node]:
            continue
        for neighbor, cost in adj[node]:
            trial = current + cost
            prior = dist.get(neighbor)
            if prior is None or trial < prior:
                dist[neighbor] = trial
                heapq.heappush(heap, (trial, neighbor))
    return dist


def reverses_b3(t_axis: int, t_diag: int) -> bool:
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


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    source = Path(__file__).read_text(encoding="utf-8")

    print(
        "external_scientific_inputs: none; B_4(0), G+, and the named axis-skeleton hop-cost are theorem hypotheses"
    )
    print("package_local_integrity_reads: runner source, proposed source note, and live axiom memo")
    print("measure_boundary: exact integer path costs and |v|_2/t(v) on the radius-4 ball")
    print("negative_scope: displayed two-end costs are not written into Admissibility")

    rotations = proper_cubic_rotations()
    sites = ball(4)
    edges = directed_edges(sites)
    adj_alpha: dict[Point, list[tuple[Point, int]]] = defaultdict(list)
    adj_rho: dict[Point, list[tuple[Point, int]]] = defaultdict(list)
    weight_pairs: set[tuple[int, int]] = set()
    alpha_on_equal: set[int] = set()
    rho_on_equal: set[int] = set()
    for src, dst in edges:
        pair = (inward_weight(src), inward_weight(dst))
        weight_pairs.add(pair)
        cost_alpha = axis_skeleton_cost(src, dst)
        cost_rho = equal_weight_cost(src, dst)
        adj_alpha[src].append((dst, cost_alpha))
        adj_rho[src].append((dst, cost_rho))
        if pair[0] == pair[1] and pair[0] > 1:
            alpha_on_equal.add(cost_alpha)
            rho_on_equal.add(cost_rho)
    weights = tuple(sorted(weight_pairs))

    reached_alpha = shortest_named(ORIGIN, adj_alpha)
    reached_rho = shortest_named(ORIGIN, adj_rho)
    l1_dist = {point: graph_radius(point) for point in sites}
    var_alpha = population_variance(ratio_list(reached_alpha, sites))
    var_rho = population_variance(ratio_list(reached_rho, sites))
    var_l1 = population_variance(ratio_list(l1_dist, sites))
    type_times_alpha = tuple(reached_alpha[point] for point in ORBIT_TYPES)
    type_times_rho = tuple(reached_rho[point] for point in ORBIT_TYPES)
    t_axis3 = reached_alpha[AXIS3]
    t_diag3 = reached_alpha[DIAG3]
    t_axis4 = reached_alpha[AXIS4]
    still_reverses = reverses_b3(t_axis3, t_diag3)

    print(f"orbit_weights_b4: {weights}")
    print(f"n_b4_sites: {len(sites)}")
    print(f"n_b4_edges: {len(edges)}")
    print(f"t_alpha(3,0,0): {t_axis3}")
    print(f"t_alpha(1,1,1): {t_diag3}")
    print(f"t_alpha(4,0,0): {t_axis4}")
    print(f"t_rho(3,0,0): {reached_rho[AXIS3]}")
    print(f"t_rho(1,1,1): {reached_rho[DIAG3]}")
    print(f"t_rho(4,0,0): {reached_rho[AXIS4]}")
    print(f"type_times_alpha: {type_times_alpha}")
    print(f"type_times_rho: {type_times_rho}")
    print(f"b3_pair_reverses: {still_reverses}")
    print(f"var_alpha: {format(var_alpha, 'f')}")
    print(f"var_rho: {format(var_rho, 'f')}")
    print(f"var_l1: {format(var_l1, 'f')}")
    print(f"(4,1,0)_in_b4: {OFF_AXIS_B6 in set(sites)}")

    checks.check("gplus-order", "proper cubic rotations number 24", len(rotations) == 24)
    checks.check("ball-size", "B_4(0) has 129 sites", len(sites) == 129)
    checks.check(
        "nonzero-sites",
        "the scored set B_4(0)\\{0} has 128 sites",
        sum(1 for point in sites if point != ORIGIN) == 128,
    )
    checks.check(
        "dijkstra-cap",
        "both named Dijkstras are capped at the 129-site ball",
        len(sites) == 129
        and len(reached_alpha) == 129
        and len(reached_rho) == 129
        and graph_radius(OFF_AXIS_B6) == 5,
    )
    checks.check(
        "thm1-weight-pairs",
        "B_4 inward occupancy pairs realize the nine weight pairs including (3,3)",
        weights == EXPECTED_WEIGHTS,
    )
    checks.check(
        "thm1-alpha-vs-rho-pairs",
        "alpha cheapens equal-weight pairs of weight greater than 1 that rho costs 3",
        alpha_on_equal == {1} and rho_on_equal == {3},
    )
    checks.check(
        "thm1-times",
        "alpha realizes t(3,0,0)=7, t(1,1,1)=5, t(4,0,0)=10",
        t_axis3 == 7 and t_diag3 == 5 and t_axis4 == 10,
    )
    checks.check(
        "thm1-b3-pair",
        "the B_3 pair does not reverse under alpha: 3*49=147 is not greater than 9*25=225",
        not still_reverses and 3 * 49 == 147 and 9 * 25 == 225 and 147 < 225,
    )
    checks.check(
        "thm1-note-times",
        "the note exhibits t_alpha of (3,0,0), (1,1,1), (4,0,0) and reports no reverse",
        "t(3,0,0) = 7" in note
        and "t(1,1,1) = 5" in note
        and "t(4,0,0) = 10" in note
        and "does not reverse" in note,
    )
    checks.check(
        "thm2-type-times",
        "G+ type arrival times under alpha are (3,4,5,6,5,6,6,7,6,10)",
        type_times_alpha == (3, 4, 5, 6, 5, 6, 6, 7, 6, 10),
    )
    checks.check(
        "thm2-vars-computed",
        "computed alpha, rho, and ell^1 variances match the displayed digits",
        rounded(var_alpha, 14) == "0.00397088249988"
        and rounded(var_rho, 14) == "0.00035024862901"
        and rounded(var_l1, 14) == "0.01771035124177",
    )
    checks.check(
        "thm2-order",
        "var_rho < var_alpha < var_l1 on the same 128 sites",
        var_rho < var_alpha < var_l1,
    )
    checks.check(
        "thm2-note-vars",
        "the note reports all three population variances and the order",
        "0.00397088249988" in note
        and "0.00035024862901" in note
        and "0.01771035124177" in note
        and "var_rho < var_alpha < var_ell1" in note,
    )
    checks.check(
        "thm2-not-leftover-b6",
        "the note states the B_4 score is not a leftover of B_6 times",
        "not a leftover" in note
        and "B_6" in note
        and "different ball" in note
        and "(4,1,0)" in note
        and "t(4,0,0) = 10" in note,
    )
    checks.check(
        "thm3-displayed-not-adopted",
        "the note reports the named rule as displayed, not adopted",
        "Displayed, not adopted" in note
        and "not written into Admissibility" in note
        and "one fixed nearest-neighbor admissibility rule" in axiom,
    )
    checks.check(
        "thm3-no-l1-law",
        "the note does not attach an ell^1 path-length law",
        "no path-length law" in note and "not attach" in note,
    )
    checks.check(
        "claim-scope",
        "claim_scope reports the B_4 axis-skeleton score only",
        "On B_4(0), the named axis-skeleton hop-cost is scored"
        in note
        and "small-ball reverse" in note
        and "variance vs" in note
        and "Displayed, not adopted" in note,
    )
    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/AXIS_SKELETON_HOPCOST_B4_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and "AUDIT_INPUT_PATHS = (" in source
        and '"docs/AXIS_SKELETON_HOPCOST_B4_BOUNDED_THEOREM_NOTE_2026-08-15.md"'
        in source,
    )
    checks.check(
        "forbidden-strings",
        "note, runner, and axiom avoid the dispatch-forbidden phrases",
        all(token not in note and token not in source for token in forbidden_tokens()),
    )
    checks.check(
        "no-axiom-cost",
        "the live axiom memo does not host a two-end occupancy hop cost",
        "two-end occupancy" not in axiom and "c(σ_v, σ_w)" not in axiom,
    )
    checks.check(
        "claim-type-and-gate",
        "bounded theorem type and a passing N1-N8 gate are source-visible",
        "**Type:** bounded_theorem" in note
        and all(f"### N{index}" in note for index in range(1, 9))
        and "No-Go Discipline disposition: **PASS**" in note
        and note.count("**ATTEMPTED**") == 6,
    )

    print(
        "per_element: checked exactly — each directed B_4(0) edge carries alpha and, separately, rho"
    )
    print(
        "per_site: checked exactly — |v|_2/t(v) is scored on each of the 128 nonzero sites"
    )
    print(
        "per_mode: checked exactly — the named axis-skeleton rule, rho, and ell^1 on the same ball"
    )
    print(
        "per_block: checked exactly — B_3 pair order and population variance on B_4(0)\\{0}"
    )
    print(
        "lattice_wide: checked and not executed — no Admissibility cost and no path-length law are adopted"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
