#!/usr/bin/env python3
"""Lex-first shortest paths to (10,0,0) and (5,5,0) under named (0,1,1).

One origin Dijkstra on B_12(0). Seed-exit is cheap; both-weights-one and
support-drop cost 3. The rule is displayed, not adopted. No cache write.
No axiom edit.
"""

from __future__ import annotations

from collections import defaultdict
from heapq import heappop, heappush
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/CLAUSE_011_WHY_FACE_K5_FAILS_B12_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/CLAUSE_011_WHY_FACE_K5_FAILS_B12_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
CLAIM_SCOPE = (
    "Lex-first shortest paths to (10,0,0) and (5,5,0) under "
    "the named (0,1,1) hop-cost on B_12(0) are named. "
    "Displayed, not adopted."
)
RADIUS = 12
ORIGIN = (0, 0, 0)
AXIS_SITE = (10, 0, 0)
FACE_SITE = (5, 5, 0)
CLAUSE_011 = (0, 1, 1)
EXPENSIVE_SEED = (1, 1, 1)
SHIFTS: tuple[tuple[int, int, int], ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
FORBIDDEN = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE")
DIJKSTRA_CALLS = 0


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


Point = tuple[int, int, int]


def normalize(text: str) -> str:
    return " ".join(text.split())


def add(left: Point, right: Point) -> Point:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


def l1_norm(site: Point) -> int:
    return abs(site[0]) + abs(site[1]) + abs(site[2])


def l2sq(site: Point) -> int:
    return site[0] * site[0] + site[1] * site[1] + site[2] * site[2]


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
    return tuple(dest for shift in SHIFTS if (dest := add(site, shift)) in BALL)


def hop_clauses(src: Point, dest: Point) -> tuple[bool, bool, bool]:
    source_weight = inward_weight(src)
    dest_weight = inward_weight(dest)
    seed_exit = source_weight == 0
    both_weights_one = source_weight == 1 and dest_weight == 1
    support_drop = dest_weight < source_weight
    return seed_exit, both_weights_one, support_drop


def hop_cost(src: Point, dest: Point, clauses: tuple[int, int, int] = CLAUSE_011) -> int:
    seed_exit, both_weights_one, support_drop = hop_clauses(src, dest)
    seed_bit, axis_bit, drop_bit = clauses
    if (seed_bit and seed_exit) or (axis_bit and both_weights_one) or (drop_bit and support_drop):
        return 3
    return 1


def dijkstra_from(source: Point, clauses: tuple[int, int, int] = CLAUSE_011) -> dict[Point, int]:
    global DIJKSTRA_CALLS
    DIJKSTRA_CALLS += 1
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


def shortest_path_pred(
    arrivals: dict[Point, int],
    clauses: tuple[int, int, int] = CLAUSE_011,
) -> dict[Point, list[Point]]:
    pred: dict[Point, list[Point]] = defaultdict(list)
    for site in BALL:
        if site not in arrivals:
            continue
        for dest in neighbors(site):
            if dest not in arrivals:
                continue
            if arrivals[site] + hop_cost(site, dest, clauses) == arrivals[dest]:
                pred[dest].append(site)
    return pred


def lex_first_shortest_path(
    target: Point,
    arrivals: dict[Point, int],
    pred: dict[Point, list[Point]],
    clauses: tuple[int, int, int] = CLAUSE_011,
) -> tuple[tuple[Point, ...], tuple[int, ...]]:
    can_reach: set[Point] = set()
    stack = [target]
    while stack:
        site = stack.pop()
        if site in can_reach:
            continue
        can_reach.add(site)
        stack.extend(pred[site])
    if ORIGIN not in can_reach:
        raise RuntimeError(f"target {target} is unreachable")
    path = [ORIGIN]
    costs: list[int] = []
    site = ORIGIN
    while site != target:
        candidates = [
            dest
            for dest in neighbors(site)
            if dest in can_reach
            and arrivals[site] + hop_cost(site, dest, clauses) == arrivals[dest]
        ]
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


def main() -> int:
    checks = Checks()
    note = (ROOT / AUDIT_INPUT_PATHS[0]).read_text(encoding="utf-8")
    axiom = (ROOT / AUDIT_INPUT_PATHS[1]).read_text(encoding="utf-8")
    source = Path(__file__).read_text(encoding="utf-8")
    normalized_note = normalize(note)
    normalized_axiom = normalize(axiom)

    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print("cache_write: false")
    print("dijkstra_count_budget: 1")
    print(f"claim_scope: {CLAIM_SCOPE}")
    print("external_scientific_inputs: current Lattice and Admissibility wording; no observations or fits")
    print("integrity_reads: this runner, its note, and the axiom memo; no other scientific inputs")
    print("construction: named (0,1,1) hop-cost on B_12(0) with one origin Dijkstra")
    print("negative_scope: displayed, not adopted; not written into Admissibility; L1 not attached")

    checks.check(
        "audit-inputs",
        "declared source-bound inputs exist as the required string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/CLAUSE_011_WHY_FACE_K5_FAILS_B12_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and AUDIT_TIMEOUT_SEC == 120
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and NOTE_REL in source
        and AXIOM_REL in source,
    )
    checks.check(
        "audit-input-literals",
        "AUDIT_INPUT_PATHS is a static two-string literal in this runner",
        'AUDIT_INPUT_PATHS = (\n    "docs/CLAUSE_011_WHY_FACE_K5_FAILS_B12_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n)'
        in source,
    )

    lattice_sentence = "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor"
    admissibility_fixed = "There is one fixed nearest-neighbor admissibility rule, covariant under lattice"
    admissibility_sentence = "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions."
    record_lock = "When present, a record locks exactly one admissible local possibility."
    record_content = "A readout value is determined by record content alone."
    record_absence = "A site with no record cannot be read."
    formation_boundary = "does not supply the formation site, probability, or rate"

    checks.check("source-lattice", "current cubic nearest-neighbor wording is pinned", lattice_sentence in normalized_axiom and lattice_sentence in note)
    checks.check(
        "source-admissibility",
        "current one-fixed-rule wording is pinned",
        admissibility_fixed in normalized_axiom
        and admissibility_sentence in normalized_axiom
        and admissibility_sentence in note,
    )
    checks.check(
        "source-record-boundary",
        "current lock/content/unreadable-at-absence wording is pinned",
        all(phrase in normalized_axiom for phrase in (record_lock, record_content, record_absence))
        and all(phrase in note for phrase in (record_lock, record_content, record_absence)),
    )
    checks.check(
        "source-formation-boundary",
        "formation site/probability/rate remains outside Admissibility",
        formation_boundary in normalized_axiom and formation_boundary in normalized_note,
    )

    checks.check("ball-cardinality", "B_12(0) has exactly 2625 integer sites", len(BALL) == 2625)
    checks.check(
        "targets-inside",
        "both scored sites lie in B_12(0) and (12,1,0) does not",
        AXIS_SITE in BALL
        and FACE_SITE in BALL
        and (12, 1, 0) not in BALL
        and (10, -1, 0) in BALL
        and (1, 5, 0) in BALL
        and l1_norm(AXIS_SITE) == 10
        and l1_norm(FACE_SITE) == 10,
    )
    checks.check(
        "clause-identity",
        "seed-exit is cheap and axis-one and support-drop cost 3",
        hop_cost(ORIGIN, (1, 0, 0)) == 1
        and hop_cost((1, 0, 0), (2, 0, 0)) == 3
        and hop_cost((1, 1, 0), (1, 0, 0)) == 3
        and hop_cost((1, 0, 0), (1, 1, 0)) == 1,
    )

    arrivals = dijkstra_from(ORIGIN)
    pred = shortest_path_pred(arrivals)
    checks.check("one-dijkstra", "exactly one Dijkstra computation is used", DIJKSTRA_CALLS == 1)
    checks.check(
        "finite-times",
        "both in-ball targets are reached by a finite path",
        AXIS_SITE in arrivals and FACE_SITE in arrivals,
    )

    axis_path, axis_costs = lex_first_shortest_path(AXIS_SITE, arrivals, pred)
    face_path, face_costs = lex_first_shortest_path(FACE_SITE, arrivals, pred)
    axis_sum = sum(axis_costs)
    face_sum = sum(face_costs)
    print(f"lex_first_axis_path: {format_path(axis_path)}")
    print(f"lex_first_axis_costs: {format_costs(axis_costs)} sum={axis_sum}")
    print(f"lex_first_face_path: {format_path(face_path)}")
    print(f"lex_first_face_costs: {format_costs(face_costs)} sum={face_sum}")
    print(f"t{AXIS_SITE}={arrivals[AXIS_SITE]}  t^2/|v|_2^2={arrivals[AXIS_SITE] ** 2}/{l2sq(AXIS_SITE)}")
    print(f"t{FACE_SITE}={arrivals[FACE_SITE]}  t^2/|v|_2^2={arrivals[FACE_SITE] ** 2}/{l2sq(FACE_SITE)}")

    checks.check(
        "arrival-axis",
        "computed t(10,0,0) equals 14 and the reconstructed hop-cost sum",
        arrivals[AXIS_SITE] == axis_sum == path_cost(axis_path) == 14
        and "t(10,0,0)=14" in note,
    )
    checks.check(
        "arrival-face",
        "computed t(5,5,0) equals 10 and the reconstructed hop-cost sum",
        arrivals[FACE_SITE] == face_sum == path_cost(face_path) == 10
        and "t(5,5,0)=10" in note,
    )
    checks.check(
        "axis-path-endpoints",
        "the axis reconstruction starts at the origin and ends at (10,0,0)",
        axis_path[0] == ORIGIN and axis_path[-1] == AXIS_SITE and all(site in BALL for site in axis_path),
    )
    checks.check(
        "face-path-endpoints",
        "the face reconstruction starts at the origin and ends at (5,5,0)",
        face_path[0] == ORIGIN and face_path[-1] == FACE_SITE and all(site in BALL for site in face_path),
    )
    checks.check(
        "note-axis-walk",
        "the note exhibits the computed axis walk and hop-cost list",
        format_path(axis_path) in note and format_costs(axis_costs) in note,
        residual=(format_path(axis_path), format_costs(axis_costs)),
    )
    checks.check(
        "note-face-walk",
        "the note exhibits the computed face walk and hop-cost list",
        format_path(face_path) in note and format_costs(face_costs) in note,
        residual=(format_path(face_path), format_costs(face_costs)),
    )
    checks.check(
        "not-leftover",
        "the hop-cost lists are longer than a two-point leftover of the no bit",
        len(axis_costs) > 1
        and len(face_costs) > 1
        and axis_costs != face_costs
        and "not leftover of the no bit" in note,
    )

    reverse_holds = arrivals[AXIS_SITE] ** 2 * l2sq(FACE_SITE) > arrivals[FACE_SITE] ** 2 * l2sq(AXIS_SITE)
    dens_ok = arrivals[AXIS_SITE] ** 2 * 50 > arrivals[FACE_SITE] ** 2 * 100
    checks.check(
        "reverse-fails",
        "t(10,0,0)^2/100 > t(5,5,0)^2/50 fails and is written",
        reverse_holds is False
        and dens_ok is False
        and arrivals[AXIS_SITE] ** 2 * 50 == 9800
        and arrivals[FACE_SITE] ** 2 * 100 == 10000
        and "50 t(10,0,0)^2 = 9800 < 10000 = 100 t(5,5,0)^2" in note,
    )

    first_axis = hop_clauses(axis_path[0], axis_path[1])
    first_face = hop_clauses(face_path[0], face_path[1])
    checks.check(
        "cheap-seed-exit",
        "both lex-first walks open with a cost-1 seed-exit",
        axis_costs[0] == 1
        and face_costs[0] == 1
        and first_axis == (True, False, False)
        and first_face == (True, False, False),
    )

    axis_only = tuple((index, 0, 0) for index in range(11))
    axis_only_costs = tuple(hop_cost(axis_only[index], axis_only[index + 1]) for index in range(len(axis_only) - 1))
    checks.check(
        "axis-only-not-shortest",
        "the axis-only competitor is strictly more expensive than t(10,0,0)",
        path_cost(axis_only) == sum(axis_only_costs) > arrivals[AXIS_SITE]
        and axis_only_costs[0] == 1
        and set(axis_only_costs[1:]) == {3},
    )

    other_axis = (
        ORIGIN,
        (1, 0, 0),
        (1, 1, 0),
        (2, 1, 0),
        (3, 1, 0),
        (4, 1, 0),
        (5, 1, 0),
        (6, 1, 0),
        (7, 1, 0),
        (8, 1, 0),
        (9, 1, 0),
        (10, 1, 0),
        AXIS_SITE,
    )
    other_face = (
        ORIGIN,
        (1, 0, 0),
        (1, 1, 0),
        (2, 1, 0),
        (3, 1, 0),
        (4, 1, 0),
        (5, 1, 0),
        (5, 2, 0),
        (5, 3, 0),
        (5, 4, 0),
        FACE_SITE,
    )
    checks.check(
        "uniqueness-not-required",
        "other shortest walks exist and uniqueness is not claimed",
        path_cost(other_axis) == arrivals[AXIS_SITE]
        and path_cost(other_face) == arrivals[FACE_SITE]
        and other_axis != axis_path
        and other_face != face_path
        and "Uniqueness is not claimed" in note,
    )

    graph_length_axis = l1_norm(AXIS_SITE)
    graph_length_face = l1_norm(FACE_SITE)
    graph_reverse = graph_length_axis ** 2 * 50 > graph_length_face ** 2 * 100
    checks.check(
        "graph-length-contrast",
        "uniform graph-length is a different pair of arrivals and is not attached",
        graph_length_axis == 10
        and graph_length_face == 10
        and (graph_length_axis, graph_length_face) != (arrivals[AXIS_SITE], arrivals[FACE_SITE])
        and graph_reverse is False
        and "Do not attach L1" in note,
    )
    checks.check(
        "mutation-seed-exit",
        "charging seed-exit 3 changes the opening hop of both named walks",
        hop_cost(ORIGIN, (0, -1, 0), EXPENSIVE_SEED) == 3
        and hop_cost(ORIGIN, (0, 1, 0), EXPENSIVE_SEED) == 3
        and path_cost(axis_path, EXPENSIVE_SEED) != arrivals[AXIS_SITE]
        and path_cost(face_path, EXPENSIVE_SEED) != arrivals[FACE_SITE],
    )

    allowed_retained = ("audit_required_before_effective_retained: true", "bare_retained_allowed: false")
    other_retained = note
    for line in allowed_retained:
        other_retained = other_retained.replace(line, "")
    required = (
        "actual_current_surface_status: bounded-support",
        "target_claim_type: bounded_theorem",
        "trace_class: frontier_discovery",
        'hypothetical_axiom_status: "no edit"',
        "Displayed, not adopted",
        "authors no audit verdict",
        "FAIL / DO NOT SHIP",
        "not leftover of the no bit",
        "not written into Admissibility",
        "Do not attach L1",
        "Uniqueness is not claimed",
    )
    checks.check(
        "note-contract",
        "machine fields, exhibition wording, N1-N8, and forbidden-phrase hygiene hold",
        all(phrase in note for phrase in required)
        and all(line in note for line in allowed_retained)
        and all(f"### N{index}" in note for index in range(1, 9))
        and not any(phrase in note for phrase in FORBIDDEN)
        and "retained" not in other_retained
        and "promoted" not in note.lower()
        and "Codex" not in note
        and "toe-lphys" not in note,
        residual=[phrase for phrase in required if phrase not in note],
    )
    checks.check(
        "claim-scope",
        "front matter keeps the dispatch claim_scope",
        CLAIM_SCOPE in note,
    )
    checks.check(
        "not-in-admissibility",
        "(0,1,1) is not written into Admissibility",
        "Do not write (0,1,1) into Admissibility" in note
        and "not written into Admissibility" in note
        and "There is one fixed nearest-neighbor admissibility rule" in axiom,
    )
    forbidden_hits = [phrase for phrase in FORBIDDEN if phrase in note or phrase in source.split("FORBIDDEN =", 1)[0]]
    checks.check(
        "forbidden-phrases",
        "forbidden phrases are absent from the note and from runner prose",
        forbidden_hits == [],
        residual=forbidden_hits,
    )
    checks.check(
        "axiom-untouched",
        "the axiom memo is an input only",
        "### Admissibility / Local Constraint" in axiom
        and "(0,1,1)" not in axiom,
    )

    print("per_element: inward-weight clauses and hop-costs are evaluated on named directed nearest-neighbor edges")
    print("per_site: lex-first reconstructions are executed at (10,0,0) and (5,5,0) inside B_12(0)")
    print("per_mode: reverse is the exact integer comparison t(10,0,0)^2/100 > t(5,5,0)^2/50")
    print("per_block: one Dijkstra on B_12(0) and the named (0,1,1) hop-cost")
    print("lattice_wide: checked and not executed — no Admissibility edit and L1 is not attached")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
