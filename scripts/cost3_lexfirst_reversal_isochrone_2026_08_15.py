#!/usr/bin/env python3
"""Isochrones of the lex-first diamond-reversing {1,2,3} two-end cost.

On B_3(0), arrival time is the minimum path cost from the seed under the
lex-first filling c = (1, 1, 3, 1, 1, 1, 1, 1): seed-exit 1, axis-extension
3, else 1. The note reports t(v) and compares var(|v|_2 / t(v)) with the
same ratio for graph radius. Displayed, not adopted. No axiom edit, cache
write, or path-length law.
"""

from __future__ import annotations

import heapq
from collections import defaultdict
from decimal import Decimal, ROUND_HALF_EVEN
from itertools import permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "COST3_LEXFIRST_REVERSAL_ISOCHRONE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/COST3_LEXFIRST_REVERSAL_ISOCHRONE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
EXPECTED_SITE_TIMES = {
    (0, 0, 0): 0,
    (0, 0, 1): 1,
    (0, 0, 2): 4,
    (0, 0, 3): 7,
    (0, 1, 1): 2,
    (0, 1, 2): 3,
    (1, 1, 1): 3,
}
VAR_PLACES = Decimal("1e-12")


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


def euclidean_sq(point: Point) -> int:
    return point[0] * point[0] + point[1] * point[1] + point[2] * point[2]


def site_type(point: Point) -> Point:
    return tuple(sorted(abs(coord) for coord in point))  # type: ignore[return-value]


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


def lex_first_costs(weights: tuple[tuple[int, int], ...]) -> tuple[int, ...]:
    """Seed-exit 1, axis-extension 3, every other orbit 1."""
    costs: list[int] = []
    for weight in weights:
        if weight == (0, 1):
            costs.append(1)
        elif weight == (1, 1):
            costs.append(3)
        else:
            costs.append(1)
    return tuple(costs)


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


def population_variance(values: list[Decimal]) -> Decimal:
    count = Decimal(len(values))
    mean = sum(values, start=Decimal(0)) / count
    return sum((value - mean) ** 2 for value in values) / count


def fmt_var(value: Decimal) -> str:
    return str(value.quantize(VAR_PLACES, rounding=ROUND_HALF_EVEN))


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

    print("external_scientific_inputs: none; B_3(0), G+, and the lex-first filling are theorem hypotheses")
    print("package_local_integrity_reads: runner source, proposed source note, and live axiom memo")
    print("measure_boundary: exact integer path costs and Decimal variance on the radius-3 ball")
    print("negative_scope: displayed lex-first isochrones are not written into Admissibility")

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
    filling = lex_first_costs(weights)
    adj: dict[Point, list[tuple[Point, int]]] = defaultdict(list)
    for src, dst in edges:
        adj[src].append(
            (dst, rep_index[orbit_rep((occupancy(src), occupancy(dst)), perms)])
        )

    times = min_path_costs(ORIGIN, adj, filling)
    unit_times = min_path_costs(ORIGIN, adj, tuple(1 for _ in reps))
    type_times: dict[Point, set[int]] = defaultdict(set)
    type_counts: dict[Point, int] = defaultdict(int)
    shells: dict[int, list[Point]] = defaultdict(list)
    for site in sites:
        kind = site_type(site)
        type_times[kind].add(times[site])
        type_counts[kind] += 1
        if site != ORIGIN:
            shells[times[site]].append(site)

    nonzero = tuple(site for site in sites if site != ORIGIN)
    cost_ratios: list[Decimal] = []
    radius_ratios: list[Decimal] = []
    for site in nonzero:
        radius = Decimal(euclidean_sq(site)).sqrt()
        cost_ratios.append(radius / Decimal(times[site]))
        radius_ratios.append(radius / Decimal(graph_radius(site)))
    var_cost = population_variance(cost_ratios)
    var_radius = population_variance(radius_ratios)
    var_cost_txt = fmt_var(var_cost)
    var_radius_txt = fmt_var(var_radius)
    smaller = "graph-radius" if var_radius < var_cost else "lex-first-cost"

    print(f"orbit_weights: {weights}")
    print(f"lex_first_c: {filling}")
    print(f"t_axis: {times[AXIS]}")
    print(f"t_diag: {times[DIAG]}")
    print(
        "site_orbit_times: "
        + ", ".join(
            f"{kind}->{sorted(type_times[kind])[0]}(n={type_counts[kind]})"
            for kind in sorted(type_times)
        )
    )
    print(
        "shells: "
        + ", ".join(
            f"t={level}:n={len(shells[level])}" for level in sorted(shells)
        )
    )
    print(f"var_lexfirst: {var_cost_txt}")
    print(f"var_graph_radius: {var_radius_txt}")
    print(f"smaller_variance: {smaller}")

    checks.check("gplus-order", "proper cubic rotations number 24", len(rotations) == 24)
    checks.check("ball-size", "B_3(0) has 63 sites", len(sites) == 63)
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
        "thm1-lex-first-c",
        "seed-exit 1 and axis-extension 3 with else 1 is (1,1,3,1,1,1,1,1)",
        filling == (1, 1, 3, 1, 1, 1, 1, 1),
    )
    checks.check(
        "thm1-axis-diag-times",
        "t(3,0,0)=7 and t(1,1,1)=3 under the lex-first filling",
        times[AXIS] == 7 and times[DIAG] == 3,
    )
    checks.check(
        "thm1-site-orbit-times",
        "each G+ site type on B_3(0) has one arrival time, matching the note table",
        all(len(type_times[kind]) == 1 for kind in type_times)
        and {kind: next(iter(vals)) for kind, vals in type_times.items()}
        == EXPECTED_SITE_TIMES
        and sum(type_counts.values()) == 63,
    )
    checks.check(
        "thm1-note-times",
        "the note records t(3,0,0)=7, t(1,1,1)=3, and the seven site-type times",
        "t(3,0,0) = 7" in note
        and "t(1,1,1) = 3" in note
        and "t(2,0,0) = 4" in note
        and "t(2,1,0) = 3" in note
        and "t(1,1,0) = 2" in note
        and "t(1,0,0) = 1" in note,
    )
    checks.check(
        "thm2-unit-is-graph-radius",
        "unit hop costs recover graph radius on every site of B_3(0)",
        all(unit_times[site] == graph_radius(site) for site in sites),
    )
    checks.check(
        "thm2-variance-comparison",
        "population variance of |v|_2 / graph-radius is smaller than for the lex-first times",
        var_radius < var_cost and smaller == "graph-radius",
    )
    checks.check(
        "thm2-variance-in-note",
        "the note reports both variances and that the graph-radius variance is smaller",
        var_cost_txt in note
        and var_radius_txt in note
        and "graph-radius variance is smaller" in note,
    )
    checks.check(
        "thm2-displayed-comparison",
        "the note displays the variance comparison and does not adopt a sphere law",
        "Displayed, not adopted" in note and "not a leftover" in note,
    )
    checks.check(
        "thm3-displayed-not-adopted",
        "the note reports the lex-first cost as displayed, not adopted",
        "Displayed, not adopted" in note
        and "not written into Admissibility" in note
        and "one fixed nearest-neighbor admissibility rule" in axiom,
    )
    checks.check(
        "thm3-no-path-length-law",
        "the note refuses to attach a path-length law",
        "No path-length law is attached" in note
        and "do not attach" in note.lower(),
    )
    checks.check(
        "claim-scope",
        "claim_scope reports the B_3(0) lex-first isochrones only",
        "On B_3(0), the isochrones" in note
        and "lex-first diamond-reversing" in note
        and "{1,2,3}" in note
        and "Displayed, not adopted" in note,
    )
    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/COST3_LEXFIRST_REVERSAL_ISOCHRONE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and "AUDIT_INPUT_PATHS = (" in source
        and '"docs/COST3_LEXFIRST_REVERSAL_ISOCHRONE_BOUNDED_THEOREM_NOTE_2026-08-15.md"'
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
        "not-mink3-leftover",
        "the note states the isochrone report is not a leftover of reversal existence",
        "not a leftover" in note and "existence" in note and "isochrone" in note.lower(),
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
        "per_site: checked exactly — t(v) is the min path cost at each of the 63 sites"
    )
    print(
        "per_mode: checked exactly — seven G+ site types and the eight pair-orbits of the filling"
    )
    print(
        "per_block: checked exactly — var(|v|_2 / t(v)) versus var(|v|_2 / graph-radius) on 62 sites"
    )
    print(
        "lattice_wide: checked and not executed — no Admissibility cost and no path-length law are adopted"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
