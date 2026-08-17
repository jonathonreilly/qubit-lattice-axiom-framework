#!/usr/bin/env python3
"""Exact lex-first shortest paths under the named (0,1,1) clause-toggle.

The runner reconstructs the minimum-cost walks 0 → (4,0,0) and 0 → (2,2,2)
on the closed radius-six nearest-neighbor ball. Seed-exit is cheap; axis-one
and support-drop hops cost 3. The rule is displayed, not adopted.
"""

from __future__ import annotations

from heapq import heappop, heappush
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]

AUDIT_INPUT_PATHS = (
    "docs/CLAUSE_011_REVERSE_PATHS_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Point = tuple[int, int, int]
ORIGIN: Point = (0, 0, 0)
AXIS_SITE: Point = (4, 0, 0)
DIAG_SITE: Point = (2, 2, 2)
RADIUS = 6
SHIFTS: tuple[Point, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
CLAUSE_011 = (0, 1, 1)
EXPENSIVE_SEED = (1, 1, 1)


def normalize(text: str) -> str:
    return " ".join(text.split())


def add(left: Point, right: Point) -> Point:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


def l1_norm(site: Point) -> int:
    return abs(site[0]) + abs(site[1]) + abs(site[2])


def inward_weight(site: Point) -> int:
    return sum(1 for coordinate in site if coordinate != 0)


def ball_sites(radius: int = RADIUS) -> frozenset[Point]:
    return frozenset(
        (x, y, z)
        for x in range(-radius, radius + 1)
        for y in range(-radius, radius + 1)
        for z in range(-radius, radius + 1)
        if abs(x) + abs(y) + abs(z) <= radius
    )


BALL = ball_sites()


def neighbors(site: Point) -> tuple[Point, ...]:
    """Nearest-neighbor successors that remain inside B_6(0)."""
    return tuple(dest for shift in SHIFTS if (dest := add(site, shift)) in BALL)


def hop_clauses(src: Point, dest: Point) -> tuple[bool, bool, bool]:
    source_weight = inward_weight(src)
    dest_weight = inward_weight(dest)
    seed_exit = source_weight == 0
    both_weights_one = source_weight == 1 and dest_weight == 1
    support_drop = dest_weight < source_weight
    return seed_exit, both_weights_one, support_drop


def hop_cost(src: Point, dest: Point, clauses: tuple[int, int, int] = CLAUSE_011) -> int:
    """Named three-clause hop-cost. Identity-gate function."""
    seed_exit, both_weights_one, support_drop = hop_clauses(src, dest)
    seed_bit, axis_bit, drop_bit = clauses
    if (seed_bit and seed_exit) or (axis_bit and both_weights_one) or (drop_bit and support_drop):
        return 3
    return 1


def dijkstra_from(source: Point, clauses: tuple[int, int, int] = CLAUSE_011) -> dict[Point, int]:
    dist = {source: 0}
    heap: list[tuple[int, Point]] = [(0, source)]
    while heap:
        cost, site = heappop(heap)
        if cost != dist[site]:
            continue
        for dest in neighbors(site):
            candidate = cost + hop_cost(site, dest, clauses)
            if dest not in dist or candidate < dist[dest]:
                dist[dest] = candidate
                heappush(heap, (candidate, dest))
    return dist


def remaining_to(target: Point, clauses: tuple[int, int, int] = CLAUSE_011) -> dict[Point, int]:
    dist = {target: 0}
    heap: list[tuple[int, Point]] = [(0, target)]
    while heap:
        cost, dest = heappop(heap)
        if cost != dist[dest]:
            continue
        for src in neighbors(dest):
            candidate = cost + hop_cost(src, dest, clauses)
            if src not in dist or candidate < dist[src]:
                dist[src] = candidate
                heappush(heap, (candidate, src))
    return dist


def lex_first_shortest_path(
    target: Point,
    clauses: tuple[int, int, int] = CLAUSE_011,
) -> tuple[tuple[Point, ...], tuple[int, ...]]:
    arrivals = dijkstra_from(ORIGIN, clauses)
    leftover = remaining_to(target, clauses)
    if target not in arrivals or ORIGIN not in leftover:
        raise RuntimeError(f"target {target} is unreachable")
    if arrivals[target] != leftover[ORIGIN]:
        raise RuntimeError("forward and reverse arrivals disagree")
    path = [ORIGIN]
    costs: list[int] = []
    site = ORIGIN
    goal = arrivals[target]
    while site != target:
        candidates = []
        for dest in neighbors(site):
            step = hop_cost(site, dest, clauses)
            if arrivals[site] + step != arrivals[dest]:
                continue
            if arrivals[dest] + leftover[dest] != goal:
                continue
            candidates.append(dest)
        if not candidates:
            raise RuntimeError(f"lex reconstruction stuck at {site}")
        dest = min(candidates)
        costs.append(hop_cost(site, dest, clauses))
        path.append(dest)
        site = dest
    return tuple(path), tuple(costs)


def path_cost(path: tuple[Point, ...], clauses: tuple[int, int, int] = CLAUSE_011) -> int:
    return sum(hop_cost(path[index], path[index + 1], clauses) for index in range(len(path) - 1))


def format_path(path: tuple[Point, ...]) -> str:
    return " → ".join(str(site).replace(" ", "") for site in path)


def format_costs(costs: tuple[int, ...]) -> str:
    return "(" + ",".join(str(cost) for cost in costs) + ")"


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool, residual: object | None = None) -> None:
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
    note = (ROOT / AUDIT_INPUT_PATHS[0]).read_text(encoding="utf-8")
    axiom = (ROOT / AUDIT_INPUT_PATHS[1]).read_text(encoding="utf-8")
    normalized_note = normalize(note)
    normalized_axiom = normalize(axiom)

    print("external_scientific_inputs: current Lattice and Admissibility wording; no observations or fits")
    print("integrity_reads: this runner, its note, and the axiom memo; no other scientific inputs")
    print("construction: named (0,1,1) hop-cost on B_6(0) with lex-first Dijkstra reconstruction")
    print("negative_scope: displayed, not adopted; not written into Admissibility; uniform graph-length not attached")

    checks.check(
        "audit-inputs",
        "declared source-bound inputs exist as the required string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/CLAUSE_011_REVERSE_PATHS_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and AUDIT_TIMEOUT_SEC == 120
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    )

    lattice_sentence = "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor"
    admissibility_fixed = "There is one fixed nearest-neighbor admissibility rule, covariant under lattice"
    admissibility_sentence = "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions."
    record_lock = "When present, a record locks exactly one admissible local possibility."
    record_content = "A readout value is determined by record content alone."
    record_absence = "A site with no record cannot be read."
    formation_boundary = "does not supply the formation site, probability, or rate"

    checks.check("source-lattice", "current cubic nearest-neighbor wording is pinned", lattice_sentence in normalized_axiom and lattice_sentence in note)
    checks.check("source-admissibility", "current one-fixed-rule wording is pinned", admissibility_fixed in normalized_axiom and admissibility_sentence in normalized_axiom and admissibility_sentence in note)
    checks.check(
        "source-record-boundary",
        "current lock/content/unreadable-at-absence wording is pinned",
        all(phrase in normalized_axiom for phrase in (record_lock, record_content, record_absence))
        and all(phrase in note for phrase in (record_lock, record_content, record_absence)),
    )
    checks.check("source-formation-boundary", "formation site/probability/rate remains outside Admissibility", formation_boundary in normalized_axiom and formation_boundary in normalized_note)

    checks.check("ball-cardinality", "B_6(0) has exactly 377 integer sites", len(BALL) == 377)
    checks.check("targets-inside", "both reverse-diamond sites lie in B_6(0)", AXIS_SITE in BALL and DIAG_SITE in BALL)
    checks.check(
        "clause-identity",
        "seed-exit is cheap and axis-one and support-drop cost 3",
        hop_cost(ORIGIN, (1, 0, 0)) == 1
        and hop_cost((1, 0, 0), (2, 0, 0)) == 3
        and hop_cost((1, 1, 0), (1, 0, 0)) == 3
        and hop_cost((1, 0, 0), (1, 1, 0)) == 1,
    )

    arrivals = dijkstra_from(ORIGIN)
    axis_path, axis_costs = lex_first_shortest_path(AXIS_SITE)
    diag_path, diag_costs = lex_first_shortest_path(DIAG_SITE)
    axis_sum = sum(axis_costs)
    diag_sum = sum(diag_costs)

    print(f"lex_first_axis_path: {format_path(axis_path)}")
    print(f"lex_first_axis_costs: {format_costs(axis_costs)} sum={axis_sum}")
    print(f"lex_first_diag_path: {format_path(diag_path)}")
    print(f"lex_first_diag_costs: {format_costs(diag_costs)} sum={diag_sum}")

    checks.check("arrival-axis", "computed t(4,0,0) equals the reconstructed hop-cost sum", arrivals[AXIS_SITE] == axis_sum == path_cost(axis_path))
    checks.check("arrival-diag", "computed t(2,2,2) equals the reconstructed hop-cost sum", arrivals[DIAG_SITE] == diag_sum == path_cost(diag_path))
    checks.check("reverse-diamond", "the two-point comparison reverses on these sites", arrivals[AXIS_SITE] > arrivals[DIAG_SITE])
    checks.check(
        "axis-path-endpoints",
        "the axis reconstruction starts at the origin and ends at (4,0,0)",
        axis_path[0] == ORIGIN and axis_path[-1] == AXIS_SITE and all(site in BALL for site in axis_path),
    )
    checks.check(
        "diag-path-endpoints",
        "the body-diagonal reconstruction starts at the origin and ends at (2,2,2)",
        diag_path[0] == ORIGIN and diag_path[-1] == DIAG_SITE and all(site in BALL for site in diag_path),
    )
    checks.check(
        "note-axis-walk",
        "the note exhibits the computed axis walk and hop-cost list",
        format_path(axis_path) in note and format_costs(axis_costs) in note,
        residual=(format_path(axis_path), format_costs(axis_costs)),
    )
    checks.check(
        "note-diag-walk",
        "the note exhibits the computed body-diagonal walk and hop-cost list",
        format_path(diag_path) in note and format_costs(diag_costs) in note,
        residual=(format_path(diag_path), format_costs(diag_costs)),
    )
    checks.check(
        "not-leftover",
        "the hop-cost lists are longer than a two-point leftover",
        len(axis_costs) > 1 and len(diag_costs) > 1 and axis_costs != diag_costs,
    )

    first_axis = hop_clauses(axis_path[0], axis_path[1])
    first_diag = hop_clauses(diag_path[0], diag_path[1])
    checks.check(
        "cheap-seed-exit",
        "both lex-first walks open with a cost-1 seed-exit",
        axis_costs[0] == 1
        and diag_costs[0] == 1
        and first_axis == (True, False, False)
        and first_diag == (True, False, False),
    )

    axis_only = (ORIGIN, (1, 0, 0), (2, 0, 0), (3, 0, 0), AXIS_SITE)
    axis_only_costs = tuple(hop_cost(axis_only[index], axis_only[index + 1]) for index in range(len(axis_only) - 1))
    checks.check(
        "axis-only-not-shortest",
        "the axis-only competitor is strictly more expensive than t(4,0,0)",
        path_cost(axis_only) == sum(axis_only_costs) > arrivals[AXIS_SITE] and axis_only_costs[0] == 1 and set(axis_only_costs[1:]) == {3},
    )

    graph_length_axis = l1_norm(AXIS_SITE)
    graph_length_diag = l1_norm(DIAG_SITE)
    checks.check(
        "graph-length-contrast",
        "uniform graph-length does not reverse and is not the named toggle",
        graph_length_axis == 4
        and graph_length_diag == 6
        and graph_length_axis < graph_length_diag
        and (graph_length_axis, graph_length_diag) != (arrivals[AXIS_SITE], arrivals[DIAG_SITE]),
    )

    expensive = dijkstra_from(ORIGIN, EXPENSIVE_SEED)
    expensive_axis_path, expensive_axis_costs = lex_first_shortest_path(AXIS_SITE, EXPENSIVE_SEED)
    checks.check(
        "mutation-seed-exit",
        "charging seed-exit 3 changes the opening hop and the arrivals",
        expensive[AXIS_SITE] != arrivals[AXIS_SITE]
        and expensive[DIAG_SITE] != arrivals[DIAG_SITE]
        and expensive_axis_costs[0] == 3
        and hop_cost(ORIGIN, (1, 0, 0), EXPENSIVE_SEED) == 3,
    )
    checks.check(
        "mutation-graph-length",
        "replacing hop_cost by uniform ones would drop t(4,0,0) to graph-length 4",
        arrivals[AXIS_SITE] != graph_length_axis and hop_cost((4, -1, 0), AXIS_SITE) == 3,
    )

    allowed_retained = ("audit_required_before_effective_retained: true", "bare_retained_allowed: false")
    other_retained = note
    for line in allowed_retained:
        other_retained = other_retained.replace(line, "")
    required = (
        "actual_current_surface_status: bounded-support",
        "target_claim_type: bounded_theorem",
        "trace_class: frontier_discovery",
        "hypothetical_axiom_status: \"no edit\"",
        "Displayed, not adopted",
        "authors no audit verdict",
        "FAIL / DO NOT SHIP",
        "not leftover of the two-point times",
        "not written into Admissibility",
        "uniform graph-length",
    )
    forbidden = (
        "G_N",
        "1/r",
        "1/r^2",
        "Lattice-named",
        "not a TOE",
        "we adopt",
        "new axiom",
    )
    checks.check(
        "note-contract",
        "machine fields, exhibition wording, N1-N8, and forbidden-phrase hygiene hold",
        all(phrase in note for phrase in required)
        and all(line in note for line in allowed_retained)
        and all(f"### N{index}" in note for index in range(1, 9))
        and not any(phrase in note for phrase in forbidden)
        and "retained" not in other_retained
        and "promoted" not in note.lower()
        and "Codex" not in note
        and "toe-lphys" not in note,
        residual=[phrase for phrase in required if phrase not in note],
    )
    checks.check(
        "claim-scope",
        "front matter keeps the dispatch claim_scope",
        'Shortest paths under the named (0,1,1) clause-toggle that reverse diamond on B_6(0) are exhibited. Displayed, not adopted.'
        in note,
    )

    print("per_element: inward-weight clauses and hop-costs are evaluated on named directed nearest-neighbor edges")
    print("per_site: lex-first reconstructions are executed at (4,0,0) and (2,2,2) inside B_6(0)")
    print("per_mode: checked and not executed — no spectral or harmonic mode claim occurs in this finite graph theorem")
    print("per_block: one Dijkstra family, two lex-first walks, and two mutation controls are executed")
    print("lattice_wide: checked and not executed — no Admissibility edit and no attached uniform graph-length time")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
