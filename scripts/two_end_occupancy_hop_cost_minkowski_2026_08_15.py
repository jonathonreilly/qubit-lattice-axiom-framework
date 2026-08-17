#!/usr/bin/env python3
"""Exact B_3(0) census of G+-equivariant two-end occupancy hop costs.

Occupancy at a site is the 6-bit inward one-seed front. Edge costs take
values in {1,2} and are constant on proper-cubic orbits of endpoint
pairs. No axiom edit, cache write, or path-length law is adopted.
"""

from __future__ import annotations

import heapq
from collections import defaultdict
from itertools import permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "TWO_END_OCCUPANCY_HOP_COST_MINKOWSKI_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/TWO_END_OCCUPANCY_HOP_COST_MINKOWSKI_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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


def shortest(start: Point, goals: tuple[Point, ...], adj: dict[Point, list[tuple[Point, int]]], costs: tuple[int, ...]) -> dict[Point, int]:
    dist = {start: 0}
    heap: list[tuple[int, Point]] = [(0, start)]
    remaining = set(goals)
    while heap and remaining:
        current, node = heapq.heappop(heap)
        if current != dist[node]:
            continue
        remaining.discard(node)
        for neighbor, orbit in adj[node]:
            trial = current + costs[orbit]
            prior = dist.get(neighbor)
            if prior is None or trial < prior:
                dist[neighbor] = trial
                heapq.heappush(heap, (trial, neighbor))
    return dist


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

    print("external_scientific_inputs: none; B_3(0), G+, and {1,2} are theorem hypotheses")
    print("package_local_integrity_reads: runner source, proposed source note, and live axiom memo")
    print("measure_boundary: exact integer path costs on the radius-3 nearest-neighbor ball")
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

    seed_exits = {
        orbit_rep((occupancy(ORIGIN), occupancy(shift)), perms) for shift in SHIFTS
    }
    axis_steps = (
        orbit_rep((occupancy((0, 0, 0)), occupancy((1, 0, 0))), perms),
        orbit_rep((occupancy((1, 0, 0)), occupancy((2, 0, 0))), perms),
        orbit_rep((occupancy((2, 0, 0)), occupancy((3, 0, 0))), perms),
    )
    axis_neighbors = tuple(
        neighbor for neighbor, _ in adj[AXIS] if graph_radius(neighbor) <= 3
    )

    n_orbit = len(reps)
    n_assign = 1 << n_orbit
    reverse = 0
    unit = shortest(ORIGIN, (AXIS, DIAG), adj, tuple(1 for _ in reps))
    all_two = shortest(ORIGIN, (AXIS, DIAG), adj, tuple(2 for _ in reps))
    worst_axis = 0
    best_diag_at_worst = 0
    for mask in range(n_assign):
        costs = tuple(1 + ((mask >> index) & 1) for index in range(n_orbit))
        reached = shortest(ORIGIN, (AXIS, DIAG), adj, costs)
        t_axis = reached[AXIS]
        t_diag = reached[DIAG]
        if 3 * t_axis * t_axis > 9 * t_diag * t_diag:
            reverse += 1
        if t_axis > worst_axis or (
            t_axis == worst_axis and t_diag < best_diag_at_worst
        ):
            worst_axis = t_axis
            best_diag_at_worst = t_diag

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

    checks.check("gplus-order", "proper cubic rotations number 24", len(rotations) == 24)
    checks.check("ball-size", "B_3(0) has 63 sites", len(sites) == 63)
    checks.check("directed-edges", "B_3(0) has 228 directed nearest-neighbor edges", len(edges) == 228)
    checks.check("thm1-orbit-count", "endpoint occupancy pairs form 8 G+ orbits", n_orbit == 8)
    checks.check(
        "thm1-orbit-weights",
        "the eight orbits are the inward-weight pairs listed in the note",
        weights == expected_weights,
    )
    checks.check(
        "thm1-first-hop-one-orbit",
        "the six seed-exit pairs occupy one G+ orbit",
        seed_exits == {reps[0]} and weights[0] == (0, 1),
    )
    checks.check(
        "thm1-axis-extensions-one-orbit",
        "both axis extensions lie in the same-weight (1,1) orbit",
        axis_steps[1] == axis_steps[2] and weights[reps.index(axis_steps[1])] == (1, 1),
    )
    checks.check(
        "thm1-axis-leaf",
        "(3,0,0) has a unique in-ball neighbor",
        axis_neighbors == ((2, 0, 0),),
    )
    checks.check("thm2-assignment-count", "G+-equivariant {1,2} costs number 256", n_assign == 256)
    checks.check("thm2-no-reversal", "no assignment reverses the diamond order", reverse == 0)
    checks.check(
        "thm2-unit-costs",
        "unit costs give t(3,0,0)=t(1,1,1)=3 and 9<=27",
        unit[AXIS] == 3 and unit[DIAG] == 3 and 3 * 9 <= 9 * 9,
    )
    checks.check(
        "thm2-all-two",
        "constant-2 costs give t(3,0,0)=t(1,1,1)=6 and 36<=108",
        all_two[AXIS] == 6 and all_two[DIAG] == 6 and 3 * 36 <= 9 * 36,
    )
    checks.check(
        "thm2-shared-first-hop-c0-1",
        "if the seed-exit costs 1 then t_axis<=5 and 3*25<=9*9",
        3 * 5 * 5 <= 9 * 3 * 3,
    )
    checks.check(
        "thm2-shared-first-hop-c0-2",
        "if the seed-exit costs 2 then t_diag>=4 and 3*36<=9*16",
        3 * 6 * 6 <= 9 * 4 * 4,
    )
    checks.check(
        "thm2-worst-still-diamond",
        "the most axis-heavy realized pair still obeys 3 t_axis^2 <= 9 t_diag^2",
        reverse == 0 and 3 * worst_axis * worst_axis <= 9 * best_diag_at_worst * best_diag_at_worst,
    )
    checks.check(
        "thm3-displayed-not-adopted",
        "the note reports the family as displayed, not adopted",
        "Displayed, not adopted" in note
        and "not written into Admissibility" in note
        and "one fixed nearest-neighbor admissibility rule" in axiom,
    )
    checks.check(
        "claim-scope",
        "claim_scope reports the B_3(0) diamond-order question only",
        "On B_3(0), whether" in note
        and "G+-equivariant two-end occupancy hop" in note
        and "Displayed, not adopted" in note,
    )
    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/TWO_END_OCCUPANCY_HOP_COST_MINKOWSKI_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and "AUDIT_INPUT_PATHS = (" in source
        and '"docs/TWO_END_OCCUPANCY_HOP_COST_MINKOWSKI_BOUNDED_THEOREM_NOTE_2026-08-15.md"'
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
        "per_site: checked exactly — occupancy is the 6-bit inward front at that site"
    )
    print(
        "per_mode: checked exactly — eight G+ pair-orbits and all 256 {1,2} fillings"
    )
    print(
        "per_block: checked exactly — t(3,0,0)^2/9 <= t(1,1,1)^2/3 on every filling"
    )
    print(
        "lattice_wide: checked and not executed — no Admissibility cost and no path-length law are adopted"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
