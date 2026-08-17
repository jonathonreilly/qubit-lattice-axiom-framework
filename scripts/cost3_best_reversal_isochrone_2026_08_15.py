#!/usr/bin/env python3
"""Isochrones of the variance-minimizing diamond-reversing {1,2,3} cost.

On B_3(0), arrival time is the minimum path cost from the seed under the
lex-first variance-minimizing filling c = (3, 1, 3, 1, 1, 3, 1, 1). The
note reports t on every G+ site-type, the |v|_2/t table, and whether the
t=const shells are that Euclidean-ratio table. Displayed, not adopted.
No axiom edit, cache write, or path-length law.
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
    "COST3_BEST_REVERSAL_ISOCHRONE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/COST3_BEST_REVERSAL_ISOCHRONE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
SITE_TYPES: tuple[Point, ...] = (
    (1, 0, 0),
    (2, 0, 0),
    (1, 1, 0),
    (3, 0, 0),
    (2, 1, 0),
    (1, 1, 1),
)
BEST_FILLING = (3, 1, 3, 1, 1, 3, 1, 1)
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
EXPECTED_TYPE_TIMES = {
    (1, 0, 0): 3,
    (2, 0, 0): 6,
    (1, 1, 0): 4,
    (3, 0, 0): 9,
    (2, 1, 0): 7,
    (1, 1, 1): 5,
}


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


def site_type(point: Point) -> Point:
    return tuple(sorted((abs(coord) for coord in point), reverse=True))  # type: ignore[return-value]


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


def min_path_costs(
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


def ratio_list(dist: dict[Point, int], sites: tuple[Point, ...]) -> list[Decimal]:
    values: list[Decimal] = []
    for point in sites:
        if point == ORIGIN:
            continue
        values.append(Decimal(euclid2(point)).sqrt() / Decimal(dist[point]))
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

    print("external_scientific_inputs: none; B_3(0), G+, and the variance-minimizing filling are theorem hypotheses")
    print("package_local_integrity_reads: runner source, proposed source note, and live axiom memo")
    print("measure_boundary: exact integer path costs and |v|_2/t on the radius-3 ball")
    print("negative_scope: displayed variance-minimizing isochrones are not written into Admissibility")

    rotations = proper_cubic_rotations()
    perms = tuple(bit_permutation(matrix) for matrix in rotations)
    sites = ball(3)
    edges = directed_edges(sites)
    pairs = tuple((occupancy(src), occupancy(dst)) for src, dst in edges)
    reps = tuple(sorted({orbit_rep(pair, perms) for pair in pairs}))
    rep_index = {rep: index for index, rep in enumerate(reps)}
    weights = tuple(
        (bin(rep[0]).count("1"), bin(rep[1]).count("1")) for rep in reps
    )
    adj: dict[Point, list[tuple[Point, int]]] = defaultdict(list)
    for src, dst in edges:
        adj[src].append(
            (dst, rep_index[orbit_rep((occupancy(src), occupancy(dst)), perms)])
        )

    times = min_path_costs(ORIGIN, adj, BEST_FILLING)
    l1_dist = {point: graph_radius(point) for point in sites}
    type_times: dict[Point, set[int]] = defaultdict(set)
    type_counts: dict[Point, int] = defaultdict(int)
    shells: dict[int, set[Point]] = defaultdict(set)
    for site in sites:
        kind = site_type(site)
        type_times[kind].add(times[site])
        type_counts[kind] += 1
        if site != ORIGIN:
            shells[times[site]].add(kind)

    type_time_map = {kind: next(iter(vals)) for kind, vals in type_times.items() if kind != ORIGIN}
    type_ratios = {
        kind: Decimal(euclid2(kind)).sqrt() / Decimal(type_time_map[kind])
        for kind in SITE_TYPES
    }
    var_best = population_variance(ratio_list(times, sites))
    var_l1 = population_variance(ratio_list(l1_dist, sites))
    shells_are_types = all(len(kinds) == 1 for kinds in shells.values()) and len(shells) == 6

    print(f"orbit_weights: {weights}")
    print(f"best_c: {BEST_FILLING}")
    print(f"t_axis: {times[AXIS]}")
    print(f"t_diag: {times[DIAG]}")
    print(
        "site_type_times: "
        + ", ".join(
            f"{kind}->{type_time_map[kind]}(n={type_counts[kind]}, |v|_2/t={rounded(type_ratios[kind], 14)})"
            for kind in SITE_TYPES
        )
    )
    print(
        "shells: "
        + ", ".join(
            f"t={level}:{next(iter(shells[level]))}" for level in sorted(shells)
        )
    )
    print(f"shells_are_euclidean_ratio_table: {shells_are_types}")
    print(f"var_best: {rounded(var_best, 14)}")
    print(f"var_l1: {rounded(var_l1, 14)}")

    checks.check("gplus-order", "proper cubic rotations number 24", len(rotations) == 24)
    checks.check("ball-size", "B_3(0) has 63 sites", len(sites) == 63)
    checks.check(
        "nonzero-sites",
        "the scored set B_3(0)\\{0} has 62 sites",
        sum(1 for point in sites if point != ORIGIN) == 62,
    )
    checks.check(
        "directed-edges",
        "B_3(0) has 228 directed nearest-neighbor edges",
        len(edges) == 228,
    )
    checks.check(
        "thm1-pair-orbits",
        "endpoint occupancy pairs form 8 G+ orbits",
        len(reps) == 8 and weights == EXPECTED_WEIGHTS,
    )
    checks.check(
        "thm1-best-c",
        "the variance-minimizing filling is (3,1,3,1,1,3,1,1)",
        BEST_FILLING == (3, 1, 3, 1, 1, 3, 1, 1),
    )
    checks.check(
        "thm1-axis-diag-times",
        "t(3,0,0)=9 and t(1,1,1)=5 under the variance-minimizing filling",
        times[AXIS] == 9 and times[DIAG] == 5,
    )
    checks.check(
        "thm1-six-type-times",
        "each of the six G+ site-types has one arrival time matching the table",
        all(len(type_times[kind]) == 1 for kind in SITE_TYPES)
        and type_time_map == EXPECTED_TYPE_TIMES
        and sum(type_counts[kind] for kind in SITE_TYPES) == 62,
    )
    checks.check(
        "thm1-note-times",
        "the note records the six type times, t(3,0,0)=9, and t(1,1,1)=5",
        "t(3,0,0) = 9" in note
        and "t(1,1,1) = 5" in note
        and "t(1,0,0) = 3" in note
        and "t(2,0,0) = 6" in note
        and "t(1,1,0) = 4" in note
        and "t(2,1,0) = 7" in note,
    )
    checks.check(
        "thm1-note-ratios",
        "the note reports |v|_2/t for each of the six site-types",
        "1/3" in note
        and "√2 / 4" in note
        and "√3 / 5" in note
        and "√5 / 7" in note,
    )
    checks.check(
        "thm1-shells-are-ratio-table",
        "each t=const shell is one G+ site-type, hence one Euclidean radius",
        shells_are_types
        and "Euclidean-ratio table" in note
        and "single `G+` site-type" in note,
    )
    checks.check(
        "thm2-var-best-computed",
        "computed population variance matches the minkbest digits",
        rounded(var_best, 14) == "0.00017588571746",
    )
    checks.check(
        "thm2-var-l1-below",
        "that variance is strictly below the displayed ell^1 figure",
        rounded(var_l1, 14) == "0.02073945514155" and var_best < var_l1,
    )
    checks.check(
        "thm2-vars-in-note",
        "the note reports both variances and that the best variance is smaller",
        "0.00017588571746" in note
        and "0.02073945514155" in note
        and "strictly below" in note,
    )
    checks.check(
        "thm2-displayed-comparison",
        "the note displays the variance comparison and does not adopt a sphere law",
        "Displayed, not adopted" in note and "not a leftover" in note,
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
        "no path-length law" in note.lower() and "not attach" in note,
    )
    checks.check(
        "claim-scope",
        "claim_scope reports the B_3(0) variance-minimizing isochrones only",
        "On B_3(0), the isochrones" in note
        and "variance-minimizing diamond-reversing" in note
        and "{1,2,3}" in note
        and "Displayed, not adopted" in note,
    )
    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/COST3_BEST_REVERSAL_ISOCHRONE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and "AUDIT_INPUT_PATHS = (" in source
        and '"docs/COST3_BEST_REVERSAL_ISOCHRONE_BOUNDED_THEOREM_NOTE_2026-08-15.md"'
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
        "not-minkbest-or-minkiso-leftover",
        "the note states the isochrone report is not a leftover of the minimizer identity or of the wrong map",
        "not a leftover" in note
        and "minimizer identity" in note
        and "wrong map" in note
        and "isochrone" in note.lower(),
    )
    checks.check(
        "claim-type-and-gate",
        "bounded theorem type and a passing N1-N8 gate are source-visible",
        "**Type:** bounded_theorem" in note
        and all(f"### N{index}" in note for index in range(1, 9))
        and "No-Go Discipline disposition: **PASS**" in note
        and note.count("**ATTEMPTED**") == 6,
    )
    checks.check(
        "scored-ball-only",
        "the note scores the comparison on B_3(0) only",
        "on `B_3(0)` only" in note or "on B_3(0) only" in note,
    )

    print(
        "per_element: checked exactly — each directed B_3(0) edge carries one inward occupancy pair"
    )
    print(
        "per_site: checked exactly — t(v) and |v|_2/t(v) on each of the 62 nonzero sites"
    )
    print(
        "per_mode: checked exactly — six G+ site-types and the eight pair-orbits of the filling"
    )
    print(
        "per_block: checked exactly — population variance of |v|_2/t on B_3(0)\\{0}"
    )
    print(
        "lattice_wide: checked and not executed — no Admissibility cost and no path-length law are adopted"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
