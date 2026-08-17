#!/usr/bin/env python3
"""Score the B_3 variance-minimizing reversal on B_4(0) only.

The displayed 8-tuple c = (3,1,3,1,1,3,1,1) is the lex-first minimizer of
var(|v|_2 / t(v)) among the 405 diamond-reversing {1,2,3} fillings of the
eight G+ occupancy-pair orbits on B_3(0). This runner does not rescan those
6561 fillings. It assigns the same eight costs on the 129-site ball B_4(0)
and reports diamond order and the population variance of |v|_2 / t(v) versus
ell^1. The cost is displayed, not adopted. No axiom edit and no path-length
law.
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
    "COST3_BEST_REVERSAL_B4_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/COST3_BEST_REVERSAL_B4_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
AXIS3: Point = (3, 0, 0)
DIAG3: Point = (1, 1, 1)
AXIS4: Point = (4, 0, 0)
DIAG4: Point = (2, 2, 2)
FILLING: tuple[int, ...] = (3, 1, 3, 1, 1, 3, 1, 1)
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


def bit_permutation(matrix: tuple[tuple[int, ...], ...]) -> tuple[int, ...]:
    return tuple(SHIFT_INDEX[apply_matrix(matrix, shift)] for shift in SHIFTS)


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
        for shift in SHIFTS:
            neighbor = (site[0] + shift[0], site[1] + shift[1], site[2] + shift[2])
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

    print("external_scientific_inputs: none; B_4(0), G+, and the displayed 8-tuple are theorem hypotheses")
    print("package_local_integrity_reads: runner source, proposed source note, and live axiom memo")
    print("measure_boundary: exact integer path costs and |v|_2/t(v) on the radius-4 ball")
    print("negative_scope: displayed two-end costs are not written into Admissibility")

    rotations = proper_cubic_rotations()
    perms = tuple(bit_permutation(matrix) for matrix in rotations)
    sites3 = ball(3)
    sites4 = ball(4)
    edges3 = directed_edges(sites3)
    edges4 = directed_edges(sites4)
    reps3 = tuple(sorted({orbit_rep((occupancy(src), occupancy(dst)), perms) for src, dst in edges3}))
    reps4 = tuple(sorted({orbit_rep((occupancy(src), occupancy(dst)), perms) for src, dst in edges4}))
    extra4 = tuple(rep for rep in reps4 if rep not in set(reps3))
    rep_index = {rep: index for index, rep in enumerate(reps3)}
    weights3 = tuple((bin(rep[0]).count("1"), bin(rep[1]).count("1")) for rep in reps3)
    extra_weights = tuple((bin(rep[0]).count("1"), bin(rep[1]).count("1")) for rep in extra4)

    adj8: dict[Point, list[tuple[Point, int]]] = defaultdict(list)
    adj9: dict[Point, list[tuple[Point, int]]] = defaultdict(list)
    n_new = 0
    for src, dst in edges4:
        rep = orbit_rep((occupancy(src), occupancy(dst)), perms)
        if rep in rep_index:
            adj8[src].append((dst, rep_index[rep]))
            adj9[src].append((dst, rep_index[rep]))
        else:
            n_new += 1
            adj9[src].append((dst, 8))

    reached = shortest_all(ORIGIN, adj8, FILLING)
    l1_dist = {point: graph_radius(point) for point in sites4}
    var_fill = population_variance(ratio_list(reached, sites4))
    var_l1 = population_variance(ratio_list(l1_dist, sites4))
    type_times = tuple(reached[point] for point in ORBIT_TYPES)
    t_axis4 = reached[AXIS4]
    t_axis3 = reached[AXIS3]
    t_diag3 = reached[DIAG3]
    with_new = shortest_all(ORIGIN, adj9, FILLING + (3,))

    print(f"orbit_weights_b3: {weights3}")
    print(f"extra_b4_orbit_weights: {extra_weights}")
    print(f"n_b4_sites: {len(sites4)}")
    print(f"n_b4_edges: {len(edges4)}")
    print(f"n_new_orbit_edges: {n_new}")
    print(f"filling: {FILLING}")
    print(f"t(4,0,0): {t_axis4}")
    print(f"t(2,2,2)_in_ball: {DIAG4 in set(sites4)}")
    print(f"t(3,0,0): {t_axis3}")
    print(f"t(1,1,1): {t_diag3}")
    print(f"type_times: {type_times}")
    print(f"var_fill: {format(var_fill, 'f')}")
    print(f"var_l1: {format(var_l1, 'f')}")

    checks.check("gplus-order", "proper cubic rotations number 24", len(rotations) == 24)
    checks.check("ball-size", "B_4(0) has 129 sites", len(sites4) == 129)
    checks.check(
        "nonzero-sites",
        "the scored set B_4(0)\\{0} has 128 sites",
        sum(1 for point in sites4 if point != ORIGIN) == 128,
    )
    checks.check(
        "bfs-cap",
        "Dijkstra is capped at the 129-site ball",
        len(sites4) == 129 and len(reached) == 129 and DIAG4 not in reached,
    )
    checks.check(
        "thm1-orbit-count",
        "the B_3 endpoint occupancy pairs remain eight G+ orbits",
        len(reps3) == 8 and weights3 == EXPECTED_WEIGHTS,
    )
    checks.check(
        "thm1-new-orbit",
        "B_4 adds one unused (3,3) occupancy-pair orbit on 48 edges",
        extra_weights == ((3, 3),) and n_new == 48 and len(reps4) == 9,
    )
    checks.check(
        "thm1-t400",
        "the displayed filling realizes t(4,0,0)=12 on B_4(0)",
        t_axis4 == 12,
    )
    checks.check(
        "thm1-222-absent",
        "(2,2,2) is not a site of the 129-site ball",
        DIAG4 not in set(sites4) and graph_radius(DIAG4) == 6,
    )
    checks.check(
        "thm1-b3-pair",
        "the B_3 axis/diagonal pair still reverses: t(3,0,0)=9, t(1,1,1)=5",
        t_axis3 == 9
        and t_diag3 == 5
        and reverses_b3(9, 5)
        and 3 * 81 > 9 * 25,
    )
    checks.check(
        "thm1-new-orbit-unused",
        "assigning cost 3 to the new orbit does not change any B_4 arrival time",
        with_new == reached,
    )
    checks.check(
        "thm1-note-times",
        "the note exhibits t(4,0,0)=12 and the still-reversing B_3 pair",
        "t(4,0,0) = 12" in note
        and "t(3,0,0) = 9" in note
        and "t(1,1,1) = 5" in note
        and "(2,2,2)" in note
        and "not a site" in note,
    )
    checks.check(
        "thm2-type-times",
        "G+ type arrival times on B_4(0) are (3,4,5,6,7,8,10,9,10,12)",
        type_times == (3, 4, 5, 6, 7, 8, 10, 9, 10, 12),
    )
    checks.check(
        "thm2-vars-computed",
        "computed filling and ell^1 variances match the displayed digits",
        rounded(var_fill, 14) == "0.00035024862901"
        and rounded(var_l1, 14) == "0.01771035124177",
    )
    checks.check(
        "thm2-fill-below-l1",
        "var(|v|_2/t) on the filling is strictly below ell^1 on the same 128 sites",
        var_fill < var_l1,
    )
    checks.check(
        "thm2-note-vars",
        "the note reports both population variances and which is smaller",
        "0.00035024862901" in note
        and "0.01771035124177" in note
        and "strictly below" in note,
    )
    checks.check(
        "thm2-not-leftover-b3",
        "the note states the B_4 score is not a leftover of the B_3 minimum",
        "not a leftover" in note
        and "B_3" in note
        and "different ball" in note,
    )
    checks.check(
        "thm3-displayed-not-adopted",
        "the note reports the filling as displayed, not adopted",
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
        and "does not rescan" in note,
    )
    checks.check(
        "claim-scope",
        "claim_scope reports the B_4 score of the B_3 minimizer only",
        "On B_4(0), the B_3 variance-minimizing reversing filling"
        in note
        and "var(|v|_2/t)" in note
        and "Displayed, not adopted" in note,
    )
    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/COST3_BEST_REVERSAL_B4_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and "AUDIT_INPUT_PATHS = (" in source
        and '"docs/COST3_BEST_REVERSAL_B4_BOUNDED_THEOREM_NOTE_2026-08-15.md"'
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
        "per_element: checked exactly — each directed B_4(0) edge is an 8-orbit hop or the unused (3,3) orbit"
    )
    print(
        "per_site: checked exactly — |v|_2/t(v) is scored on each of the 128 nonzero sites"
    )
    print(
        "per_mode: checked exactly — the single displayed filling, with no 6561 rescan"
    )
    print(
        "per_block: checked exactly — diamond order and population variance on B_4(0)\\{0}"
    )
    print(
        "lattice_wide: checked and not executed — no Admissibility cost and no path-length law are adopted"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
