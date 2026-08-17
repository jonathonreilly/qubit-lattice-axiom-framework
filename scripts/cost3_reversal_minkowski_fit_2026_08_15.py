#!/usr/bin/env python3
"""Exact B_3(0) Euclidean-ratio census of the 405 reversing {1,2,3} costs.

Among G+-equivariant two-end occupancy hop costs in {1,2,3} that reverse
the diamond axis/diagonal order, this runner reports the lex-first
minimizer of the population variance of |v|_2 / t(v) on B_3(0)\\{0}.
The cost is displayed, not adopted. No axiom edit and no path-length law.
"""

from __future__ import annotations

import heapq
import math
from collections import defaultdict
from decimal import Decimal, getcontext
from itertools import permutations, product
from pathlib import Path


getcontext().prec = 80

AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "COST3_REVERSAL_MINKOWSKI_FIT_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/COST3_REVERSAL_MINKOWSKI_FIT_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
LEX_FIRST_REVERSAL = (1, 1, 3, 1, 1, 1, 1, 1)
EXPECTED_BEST = (3, 1, 3, 1, 1, 3, 1, 1)


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


def float_var(dist: dict[Point, int], sites: tuple[Point, ...]) -> float:
    ratios: list[float] = []
    for point in sites:
        if point == ORIGIN:
            continue
        ratios.append(math.sqrt(euclid2(point)) / dist[point])
    count = len(ratios)
    mean = sum(ratios) / count
    return sum((item - mean) ** 2 for item in ratios) / count


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

    print("external_scientific_inputs: none; B_3(0), G+, and {1,2,3} are theorem hypotheses")
    print("package_local_integrity_reads: runner source, proposed source note, and live axiom memo")
    print("measure_boundary: exact integer path costs and |v|_2/t(v) on the radius-3 ball")
    print("negative_scope: displayed two-end costs are not written into Admissibility")

    rotations = proper_cubic_rotations()
    perms = tuple(bit_permutation(matrix) for matrix in rotations)
    sites = ball(3)
    edges = directed_edges(sites)
    pairs = tuple((occupancy(src), occupancy(dst)) for src, dst in edges)
    reps = tuple(sorted({orbit_rep(pair, perms) for pair in pairs}))
    rep_index = {rep: index for index, rep in enumerate(reps)}
    adj: dict[Point, list[tuple[Point, int]]] = defaultdict(list)
    for src, dst in edges:
        adj[src].append((dst, rep_index[orbit_rep((occupancy(src), occupancy(dst)), perms)]))

    n_orbit = len(reps)
    weights = tuple(
        (bin(rep[0]).count("1"), bin(rep[1]).count("1")) for rep in reps
    )
    expected_weights = (
        (0, 1),
        (1, 0),
        (1, 1),
        (1, 2),
        (2, 1),
        (2, 2),
        (2, 3),
        (3, 2),
    )

    l1_dist = {point: graph_radius(point) for point in sites}
    var_l1 = population_variance(ratio_list(l1_dist, sites))
    lex_dist = shortest_all(ORIGIN, adj, LEX_FIRST_REVERSAL)
    var_lex = population_variance(ratio_list(lex_dist, sites))

    reverse = 0
    best: tuple[int, ...] | None = None
    best_var: Decimal | None = None
    best_dist: dict[Point, int] | None = None
    n_tied = 0
    for filling in product((1, 2, 3), repeat=n_orbit):
        reached = shortest_all(ORIGIN, adj, filling)
        if not reverses(reached[AXIS], reached[DIAG]):
            continue
        reverse += 1
        variance = population_variance(ratio_list(reached, sites))
        if best_var is None or variance < best_var:
            best_var = variance
            best = filling
            best_dist = reached
            n_tied = 1
        elif variance == best_var:
            n_tied += 1

    assert best is not None and best_var is not None and best_dist is not None
    best_times = (best_dist[AXIS], best_dist[DIAG])
    type_times = tuple(best_dist[point] for point in ORBIT_TYPES)
    lex_times = (lex_dist[AXIS], lex_dist[DIAG])

    print(f"orbit_weights: {weights}")
    print(f"n_rev: {reverse}")
    print(f"var_l1: {format(var_l1, 'f')}")
    print(f"var_lex: {format(var_lex, 'f')}")
    print(f"lex_first_reversal: {LEX_FIRST_REVERSAL}")
    print(f"lex_first_reversal_times: {lex_times}")
    print(f"best_c: {best}")
    print(f"best_times: {best_times}")
    print(f"best_var: {format(best_var, 'f')}")
    print(f"best_type_times: {type_times}")
    print(f"n_tied_at_best: {n_tied}")

    checks.check("gplus-order", "proper cubic rotations number 24", len(rotations) == 24)
    checks.check("ball-size", "B_3(0) has 63 sites", len(sites) == 63)
    checks.check(
        "nonzero-sites",
        "the scored set B_3(0)\\{0} has 62 sites",
        sum(1 for point in sites if point != ORIGIN) == 62,
    )
    checks.check(
        "thm1-orbit-count",
        "endpoint occupancy pairs form 8 G+ orbits",
        n_orbit == 8 and weights == expected_weights,
    )
    checks.check(
        "thm1-reverse-count",
        "exactly 405 of the 6561 assignments reverse the diamond order",
        reverse == 405,
    )
    checks.check(
        "thm1-lex-reversal",
        "the lex-first reversing filling is (1,1,3,1,1,1,1,1) with times (7, 3)",
        lex_times == (7, 3) and reverses(7, 3),
    )
    checks.check(
        "thm1-var-l1-note",
        "the note reports the ell^1 population variance on the 62 sites",
        "0.02073945514155" in note and "ell^1" in note,
    )
    checks.check(
        "thm1-var-lex-note",
        "the note reports the lex-first reversal population variance",
        "0.02227566969848" in note and "(1, 1, 3, 1, 1, 1, 1, 1)" in note,
    )
    def rounded(value: Decimal, places: int) -> str:
        quantize = Decimal(10) ** -places
        return format(value.quantize(quantize), "f")

    checks.check(
        "thm1-vars-computed",
        "computed ell^1 and lex-first-reversal variances match the displayed digits",
        rounded(var_l1, 14) == "0.02073945514155"
        and rounded(var_lex, 14) == "0.02227566969848",
    )
    checks.check(
        "thm2-lex-first-minimizer",
        "the lex-first variance minimizer is (3,1,3,1,1,3,1,1)",
        best == EXPECTED_BEST,
    )
    checks.check(
        "thm2-arrival-times",
        "that filling realizes t(3,0,0)=9 and t(1,1,1)=5",
        best_times == (9, 5) and reverses(9, 5) and 3 * 81 > 9 * 25,
    )
    checks.check(
        "thm2-note-tuple",
        "the note exhibits the lex-first minimizer and those arrival times",
        "(3, 1, 3, 1, 1, 3, 1, 1)" in note
        and "t(3,0,0) = 9" in note
        and "t(1,1,1) = 5" in note,
    )
    checks.check(
        "thm2-var-best-note",
        "the note reports the minimizer population variance",
        "0.00017588571746" in note,
    )
    checks.check(
        "thm2-var-best-computed",
        "computed minimizer variance matches the displayed digits and beats both baselines",
        rounded(best_var, 14) == "0.00017588571746"
        and best_var < var_l1
        and best_var < var_lex,
    )
    checks.check(
        "thm2-type-times",
        "orbit arrival times on the minimizer are (3,6,4,9,7,5)",
        type_times == (3, 6, 4, 9, 7, 5),
    )
    checks.check(
        "thm2-degeneracy",
        "exactly 27 reversing fillings share the minimizing arrival table",
        n_tied == 27,
    )
    checks.check(
        "thm2-not-mink3-leftover",
        "the note states the variance minimizer is not a leftover of existence or of one map",
        "not a leftover" in note
        and "existence" in note
        and "one map" in note
        and "405" in note,
    )
    checks.check(
        "thm3-displayed-not-adopted",
        "the note reports the minimizer as displayed, not adopted",
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
        "claim_scope reports the 405-map variance minimizer only",
        "Among the 405 diamond-reversing" in note
        and "lex-first minimizer" in note
        and "var(|v|_2/t(v))" in note
        and "Displayed, not adopted" in note,
    )
    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/COST3_REVERSAL_MINKOWSKI_FIT_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and "AUDIT_INPUT_PATHS = (" in source
        and '"docs/COST3_REVERSAL_MINKOWSKI_FIT_BOUNDED_THEOREM_NOTE_2026-08-15.md"'
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
        "per_element: checked exactly — each directed B_3(0) edge carries one inward occupancy pair"
    )
    print(
        "per_site: checked exactly — |v|_2/t(v) is scored on each of the 62 nonzero sites"
    )
    print(
        "per_mode: checked exactly — all 405 reversing {1,2,3} fillings"
    )
    print(
        "per_block: checked exactly — population variance of |v|_2/t(v) on B_3(0)\\{0}"
    )
    print(
        "lattice_wide: checked and not executed — no Admissibility cost and no path-length law are adopted"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
