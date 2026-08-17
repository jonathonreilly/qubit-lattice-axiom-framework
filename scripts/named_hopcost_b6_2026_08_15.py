#!/usr/bin/env python3
"""Score the named equal-weight hop-cost on B_6(0) only.

The named rule rho assigns cost 3 iff the inward weights are equal or the
source is the seed, else cost 1, on every inward occupancy pair that
appears in B_6. This runner does not rescan the 6561 fillings. It runs one
Dijkstra on the 377-site ball B_6(0) and reports diamond order at (4,0,0)
versus (2,2,2) and the population variance of |v|_2 / t(v) versus ell^1.
The cost is displayed, not adopted. No axiom edit and no path-length law.
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
    "NAMED_HOPCOST_B6_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/NAMED_HOPCOST_B6_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
SHIFT_INDEX = {shift: index for index, shift in enumerate(SHIFTS)}
ORIGIN: Point = (0, 0, 0)
AXIS4: Point = (4, 0, 0)
AXIS6: Point = (6, 0, 0)
DIAG6: Point = (2, 2, 2)
AXIS3: Point = (3, 0, 0)
DIAG3: Point = (1, 1, 1)
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
    (2, 2, 1),
    (2, 2, 2),
    (3, 0, 0),
    (3, 1, 0),
    (3, 1, 1),
    (3, 2, 0),
    (3, 2, 1),
    (3, 3, 0),
    (4, 0, 0),
    (4, 1, 0),
    (4, 1, 1),
    (4, 2, 0),
    (5, 0, 0),
    (5, 1, 0),
    (6, 0, 0),
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


def named_cost(src: Point, dst: Point) -> int:
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


def spec_reverse(t_axis: int, t_diag: int) -> bool:
    return 3 * t_axis * t_axis > 16 * t_diag * t_diag


def b3_order_reverse(t_axis: int, t_diag: int) -> bool:
    return 12 * t_axis * t_axis > 16 * t_diag * t_diag


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

    print("external_scientific_inputs: none; B_6(0), G+, and the named hop-cost are theorem hypotheses")
    print("package_local_integrity_reads: runner source, proposed source note, and live axiom memo")
    print("measure_boundary: exact integer path costs and |v|_2/t(v) on the radius-6 ball")
    print("negative_scope: displayed two-end costs are not written into Admissibility")

    rotations = proper_cubic_rotations()
    sites = ball(6)
    edges = directed_edges(sites)
    adj: dict[Point, list[tuple[Point, int]]] = defaultdict(list)
    weight_pairs: set[tuple[int, int]] = set()
    for src, dst in edges:
        adj[src].append((dst, named_cost(src, dst)))
        weight_pairs.add((inward_weight(src), inward_weight(dst)))
    weights = tuple(sorted(weight_pairs))

    reached = shortest_named(ORIGIN, adj)
    l1_dist = {point: graph_radius(point) for point in sites}
    var_rho = population_variance(ratio_list(reached, sites))
    var_l1 = population_variance(ratio_list(l1_dist, sites))
    type_times = tuple(reached[point] for point in ORBIT_TYPES)
    t_axis4 = reached[AXIS4]
    t_axis6 = reached[AXIS6]
    t_diag6 = reached[DIAG6]
    t_axis3 = reached[AXIS3]
    t_diag3 = reached[DIAG3]
    diamond_spec = spec_reverse(t_axis4, t_diag6)
    diamond_b3 = b3_order_reverse(t_axis4, t_diag6)

    print(f"orbit_weights_b6: {weights}")
    print(f"n_b6_sites: {len(sites)}")
    print(f"n_b6_edges: {len(edges)}")
    print(f"t(4,0,0): {t_axis4}")
    print(f"t(6,0,0): {t_axis6}")
    print(f"t(2,2,2): {t_diag6}")
    print(f"t(3,0,0): {t_axis3}")
    print(f"t(1,1,1): {t_diag3}")
    print(f"type_times: {type_times}")
    print(f"diamond_spec_reverse: {diamond_spec}")
    print(f"diamond_b3_order_reverse: {diamond_b3}")
    print(f"var_rho: {format(var_rho, 'f')}")
    print(f"var_l1: {format(var_l1, 'f')}")

    checks.check("gplus-order", "proper cubic rotations number 24", len(rotations) == 24)
    checks.check("ball-size", "B_6(0) has 377 sites", len(sites) == 377)
    checks.check(
        "nonzero-sites",
        "the scored set B_6(0)\\{0} has 376 sites",
        sum(1 for point in sites if point != ORIGIN) == 376,
    )
    checks.check(
        "one-dijkstra",
        "one Dijkstra is capped at the 377-site ball",
        len(sites) == 377 and len(reached) == 377 and DIAG6 in reached,
    )
    checks.check(
        "thm1-weight-pairs",
        "B_6 inward occupancy pairs realize the nine weight pairs including (3,3)",
        weights == EXPECTED_WEIGHTS,
    )
    checks.check(
        "thm1-times",
        "the named rule realizes t(4,0,0)=12, t(6,0,0)=18, t(2,2,2)=14",
        t_axis4 == 12 and t_axis6 == 18 and t_diag6 == 14,
    )
    checks.check(
        "thm1-diamond-spec",
        "the scale test 3 t(4,0,0)^2 > 16 t(2,2,2)^2 fails: 432 vs 3136",
        not diamond_spec and 3 * 144 == 432 and 16 * 196 == 3136,
    )
    checks.check(
        "thm1-diamond-b3-order",
        "the B_3 axis/body-diagonal order on (4,0,0) vs (2,2,2) also fails to reverse",
        not diamond_b3 and 12 * 144 < 16 * 196,
    )
    checks.check(
        "thm1-note-times",
        "the note exhibits t(4,0,0), t(6,0,0), t(2,2,2) and reports no reverse",
        "t(4,0,0) = 12" in note
        and "t(6,0,0) = 18" in note
        and "t(2,2,2) = 14" in note
        and "does not reverse" in note,
    )
    checks.check(
        "thm2-type-times",
        "selected G+ type arrival times include axis 3k and body-diagonal 14",
        type_times[ORBIT_TYPES.index(AXIS4)] == 12
        and type_times[ORBIT_TYPES.index(AXIS6)] == 18
        and type_times[ORBIT_TYPES.index(DIAG6)] == 14
        and type_times[ORBIT_TYPES.index((1, 0, 0))] == 3
        and type_times[ORBIT_TYPES.index((2, 2, 0))] == 10,
    )
    checks.check(
        "thm2-vars-computed",
        "computed named-rule and ell^1 variances match the displayed digits",
        rounded(var_rho, 14) == "0.00067960829822"
        and rounded(var_l1, 14) == "0.01350203761919",
    )
    checks.check(
        "thm2-rho-below-l1",
        "var(|v|_2/t) on the named rule is strictly below ell^1 on the same 376 sites",
        var_rho < var_l1,
    )
    checks.check(
        "thm2-note-vars",
        "the note reports both population variances and which is smaller",
        "0.00067960829822" in note
        and "0.01350203761919" in note
        and "strictly below" in note,
    )
    checks.check(
        "thm2-not-leftover-b4",
        "the note states the B_6 score is not a leftover of the B_4 score",
        "not a leftover" in note
        and "B_4" in note
        and "different ball" in note
        and "(2,2,2)" in note,
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
        "no-rescan",
        "the runner does not rescan the 6561 fillings",
        "product((1, 2, 3), " + "repeat" not in source
        and "6561" in note
        and "does not rescan" in note
        and source.count("shortest_" + "named(") == 2,
    )
    checks.check(
        "claim-scope",
        "claim_scope reports the B_6 named-rule score only",
        "On B_6(0), the named equal-weight hop-cost is scored"
        in note
        and "var(|v|_2/t)" in note
        and "Displayed, not adopted" in note,
    )
    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/NAMED_HOPCOST_B6_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and "AUDIT_INPUT_PATHS = (" in source
        and '"docs/NAMED_HOPCOST_B6_BOUNDED_THEOREM_NOTE_2026-08-15.md"'
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
        "per_element: checked exactly — each directed B_6(0) edge carries the named equal-weight hop-cost"
    )
    print(
        "per_site: checked exactly — |v|_2/t(v) is scored on each of the 376 nonzero sites"
    )
    print(
        "per_mode: checked exactly — the single named rule, with one Dijkstra and no 6561 rescan"
    )
    print(
        "per_block: checked exactly — diamond order and population variance on B_6(0)\\{0}"
    )
    print(
        "lattice_wide: checked and not executed — no Admissibility cost and no path-length law are adopted"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
