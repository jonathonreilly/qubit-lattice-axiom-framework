#!/usr/bin/env python3
"""Exhibit lex-first shortest paths to the t=8 G+ representatives.

One Dijkstra on the induced six-neighbor graph of the closed taxicab ball
B_6(0). The named hop-cost nu is displayed, not adopted. No axiom edit,
L1 attachment, cache write, or citation manifest.
"""

from __future__ import annotations

import ast
from heapq import heappop, heappush
from itertools import permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/SUPPORT_DROP_T8_PATHS_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/SUPPORT_DROP_T8_PATHS_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Point = tuple[int, int, int]
Rotation = tuple[tuple[int, int, int], tuple[int, int, int]]
PathSites = tuple[Point, ...]

BALL_RADIUS = 6
TARGET_T = 8
ORIGIN: Point = (0, 0, 0)
SHIFTS: tuple[Point, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
FORBIDDEN_PHRASES = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE")
CLAIM_SCOPE = (
    "A shortest path under the named support-drop hop-cost is exhibited "
    "to each t=8 G+ representative on B_6(0). Displayed, not adopted."
)
EXPECTED_REPS: tuple[Point, ...] = (
    (2, 2, 2),
    (3, 1, 2),
    (3, 2, 1),
    (3, 3, 0),
    (4, 1, 1),
    (4, 2, 0),
    (5, 1, 0),
)
EXPECTED_PATHS: dict[Point, PathSites] = {
    (2, 2, 2): (
        (0, 0, 0),
        (0, 0, 1),
        (0, 1, 1),
        (0, 1, 2),
        (0, 2, 2),
        (1, 2, 2),
        (2, 2, 2),
    ),
    (3, 1, 2): (
        (0, 0, 0),
        (0, 0, 1),
        (0, 1, 1),
        (0, 1, 2),
        (1, 1, 2),
        (2, 1, 2),
        (3, 1, 2),
    ),
    (3, 2, 1): (
        (0, 0, 0),
        (0, 0, 1),
        (0, 1, 1),
        (0, 2, 1),
        (1, 2, 1),
        (2, 2, 1),
        (3, 2, 1),
    ),
    (3, 3, 0): (
        (0, 0, 0),
        (0, 1, 0),
        (1, 1, 0),
        (1, 2, 0),
        (1, 3, 0),
        (2, 3, 0),
        (3, 3, 0),
    ),
    (4, 1, 1): (
        (0, 0, 0),
        (0, 0, 1),
        (0, 1, 1),
        (1, 1, 1),
        (2, 1, 1),
        (3, 1, 1),
        (4, 1, 1),
    ),
    (4, 2, 0): (
        (0, 0, 0),
        (0, 1, 0),
        (1, 1, 0),
        (1, 2, 0),
        (2, 2, 0),
        (3, 2, 0),
        (4, 2, 0),
    ),
    (5, 1, 0): (
        (0, 0, 0),
        (0, 1, 0),
        (1, 1, 0),
        (2, 1, 0),
        (3, 1, 0),
        (4, 1, 0),
        (5, 1, 0),
    ),
}
DIJKSTRA_CALLS = 0


def permutation_sign(permutation: tuple[int, int, int]) -> int:
    inversions = sum(
        permutation[i] > permutation[j]
        for i in range(3)
        for j in range(i + 1, 3)
    )
    return -1 if inversions % 2 else 1


ROTATIONS: tuple[Rotation, ...] = tuple(
    (permutation, signs)
    for permutation in permutations((0, 1, 2))
    for signs in product((-1, 1), repeat=3)
    if permutation_sign(permutation) * signs[0] * signs[1] * signs[2] == 1
)


def rotate_vector(rotation: Rotation, vector: Point) -> Point:
    permutation, signs = rotation
    result = [0, 0, 0]
    for source_axis in range(3):
        result[permutation[source_axis]] = signs[source_axis] * vector[source_axis]
    return (result[0], result[1], result[2])


def taxicab(point: Point) -> int:
    return abs(point[0]) + abs(point[1]) + abs(point[2])


def support_weight(point: Point) -> int:
    return sum(coord != 0 for coord in point)


def in_ball(point: Point) -> bool:
    return taxicab(point) <= BALL_RADIUS


def ball_sites() -> tuple[Point, ...]:
    sites: list[Point] = []
    for x in range(-BALL_RADIUS, BALL_RADIUS + 1):
        for y in range(-BALL_RADIUS, BALL_RADIUS + 1):
            remain = BALL_RADIUS - abs(x) - abs(y)
            for z in range(-remain, remain + 1):
                sites.append((x, y, z))
    return tuple(sites)


def hop_cost(source: Point, target: Point) -> int:
    """Named support-drop hop-cost nu, as in the noshrt rule."""
    source_weight = support_weight(source)
    target_weight = support_weight(target)
    if source_weight == 0 or (source_weight == 1 and target_weight == 1) or target_weight < source_weight:
        return 3
    return 1


def hop_clause(source: Point, target: Point) -> str:
    source_weight = support_weight(source)
    target_weight = support_weight(target)
    if source_weight == 0:
        return "seed-exit"
    if source_weight == 1 and target_weight == 1:
        return "both-weights-1"
    if target_weight < source_weight:
        return "support-drop"
    return "neither"


def neighbors_in_ball(site: Point) -> tuple[Point, ...]:
    out: list[Point] = []
    for shift in SHIFTS:
        candidate = (site[0] + shift[0], site[1] + shift[1], site[2] + shift[2])
        if in_ball(candidate):
            out.append(candidate)
    return tuple(sorted(out))


def one_dijkstra(sites: tuple[Point, ...]) -> tuple[dict[Point, int], dict[Point, PathSites]]:
    """Single-source lex-first shortest paths from the origin. Called once."""
    global DIJKSTRA_CALLS
    DIJKSTRA_CALLS += 1
    dist: dict[Point, int] = {ORIGIN: 0}
    path: dict[Point, PathSites] = {ORIGIN: (ORIGIN,)}
    heap: list[tuple[int, PathSites, Point]] = [(0, (ORIGIN,), ORIGIN)]
    finalized: set[Point] = set()
    site_set = frozenset(sites)
    while heap:
        time, current_path, site = heappop(heap)
        if site in finalized:
            continue
        finalized.add(site)
        for nxt in neighbors_in_ball(site):
            if nxt not in site_set:
                continue
            arrival = time + hop_cost(site, nxt)
            new_path = current_path + (nxt,)
            better_cost = nxt not in dist or arrival < dist[nxt]
            better_path = nxt in dist and arrival == dist[nxt] and new_path < path[nxt]
            if better_cost or better_path:
                dist[nxt] = arrival
                path[nxt] = new_path
                heappush(heap, (arrival, new_path, nxt))
    return dist, path


def path_costs(walk: PathSites) -> tuple[int, ...]:
    return tuple(hop_cost(walk[index], walk[index + 1]) for index in range(len(walk) - 1))


def compact_point(point: Point) -> str:
    return f"({point[0]},{point[1]},{point[2]})"


def compact_path(walk: PathSites) -> str:
    return " → ".join(compact_point(site) for site in walk)


def gplus_orbit(point: Point) -> frozenset[Point]:
    return frozenset(rotate_vector(rotation, point) for rotation in ROTATIONS)


def representative(orbit: frozenset[Point]) -> Point:
    octant = tuple(point for point in orbit if point[0] >= 0 and point[1] >= 0 and point[2] >= 0)
    if not octant:
        raise ValueError("G+ orbit has no first-octant representative")
    return max(octant)


def literal_audit_paths(source: str) -> tuple[str, ...] | None:
    module = ast.parse(source)
    for node in module.body:
        if not isinstance(node, ast.Assign):
            continue
        if not any(isinstance(target, ast.Name) and target.id == "AUDIT_INPUT_PATHS" for target in node.targets):
            continue
        if not isinstance(node.value, ast.Tuple):
            return None
        out: list[str] = []
        for elt in node.value.elts:
            if not isinstance(elt, ast.Constant) or not isinstance(elt.value, str):
                return None
            out.append(elt.value)
        return tuple(out)
    return None


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool, residual: object | None = None) -> None:
        ok = bool(condition)
        self.passed += int(ok)
        self.failed += int(not ok)
        print(f"{'PASS' if ok else 'FAIL'}: {label} — {statement}")
        if not ok and residual is not None:
            print(f"  residual: {residual}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return 0 if self.failed == 0 else 1


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    source = Path(__file__).read_text(encoding="utf-8")
    for relative in AUDIT_INPUT_PATHS:
        (ROOT / relative).read_text(encoding="utf-8")

    print("construction: one Dijkstra for named support-drop hop-cost nu on B_6(0)")
    print("negative_scope: nu is displayed, not written into Admissibility; L1 is not attached")
    print(f"claim_scope: {CLAIM_SCOPE}")
    print("cache_write: false")

    checks.check(
        "audit-inputs",
        "AUDIT_INPUT_PATHS is the required string-literal pair and both files exist",
        AUDIT_INPUT_PATHS == (
            "docs/SUPPORT_DROP_T8_PATHS_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and AUDIT_TIMEOUT_SEC == 120
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file(),
    )
    checks.check(
        "audit-input-literal",
        "AUDIT_INPUT_PATHS is a static string-literal tuple",
        literal_audit_paths(source) == AUDIT_INPUT_PATHS,
    )

    sites = ball_sites()
    site_set = frozenset(sites)
    checks.check(
        "ball-census",
        "B_6(0) has 377 integer sites and 376 nonzero sites",
        len(sites) == 377 and ORIGIN in site_set and len(sites) - 1 == 376,
        residual=len(sites),
    )
    checks.check(
        "rotation-group",
        "the proper cubic group used for types has 24 elements",
        len(ROTATIONS) == 24 and len(set(ROTATIONS)) == 24,
    )

    arrivals, paths = one_dijkstra(sites)
    checks.check(
        "one-dijkstra-total",
        "exactly one Dijkstra ran and every site of B_6(0) receives a finite arrival",
        DIJKSTRA_CALLS == 1 and all(site in arrivals and arrivals[site] < 10**9 for site in sites),
    )
    checks.check(
        "named-nu-clauses",
        "nu is 3 on seed-exit, both-weight-1, and support drop, else 1",
        hop_cost(ORIGIN, (1, 0, 0)) == 3
        and hop_cost((1, 0, 0), (2, 0, 0)) == 3
        and hop_cost((1, 1, 0), (1, 0, 0)) == 3
        and hop_cost((1, 0, 0), (1, 1, 0)) == 1
        and hop_cost((1, 1, 0), (2, 1, 0)) == 1,
    )

    t8_sites = tuple(site for site in sites if site != ORIGIN and arrivals[site] == TARGET_T)
    consumed: set[Point] = set()
    reps: list[Point] = []
    for site in t8_sites:
        if site in consumed:
            continue
        orbit = gplus_orbit(site)
        orbit_in_ball = frozenset(point for point in orbit if point in site_set)
        consumed.update(orbit_in_ball)
        reps.append(representative(orbit_in_ball))
    reps_sorted = tuple(sorted(reps))
    checks.check(
        "seven-t8-reps",
        "the lex-sorted t=8 G+ representatives are the seven named types",
        reps_sorted == EXPECTED_REPS and len(t8_sites) == 140,
        residual=reps_sorted,
    )

    computed_rows: list[tuple[Point, PathSites, tuple[int, ...]]] = []
    for rep in EXPECTED_REPS:
        walk = paths[rep]
        costs = path_costs(walk)
        computed_rows.append((rep, walk, costs))
        print(f"path {compact_point(rep)}: {compact_path(walk)}")
        print(f"  hop_costs={costs} sum={sum(costs)} first_clause={hop_clause(walk[0], walk[1])}")

    checks.check(
        "thm1-lex-paths",
        "the computed lex-first shortest path matches the displayed walk at each representative",
        all(walk == EXPECTED_PATHS[rep] for rep, walk, _ in computed_rows)
        and all(arrivals[rep] == TARGET_T for rep in EXPECTED_REPS),
        residual=[(rep, walk) for rep, walk, _ in computed_rows],
    )
    checks.check(
        "thm1-hop-cost-lists",
        "each hop-cost list is 3,1,1,1,1,1 and sums to 8",
        all(costs == (3, 1, 1, 1, 1, 1) and sum(costs) == TARGET_T for _, _, costs in computed_rows),
    )
    checks.check(
        "thm1-sum-is-arrival",
        "each hop-cost sum equals the Dijkstra arrival t=8",
        all(sum(costs) == arrivals[rep] == TARGET_T for rep, _, costs in computed_rows),
    )
    checks.check(
        "thm1-note-table",
        "the note displays each representative, lex-first path, hop-cost list, and multiset",
        all(
            compact_point(rep) in note
            and compact_path(walk) in note
            and "3,1,1,1,1,1" in note
            and "{1,1,1,1,1,3}" in note
            for rep, walk, _ in computed_rows
        ),
    )
    checks.check(
        "thm1-not-leftover",
        "the note treats the path exhibition as not leftover of the type list",
        "not leftover of the type list" in note,
    )
    first_clauses = [hop_clause(walk[0], walk[1]) for _, walk, _ in computed_rows]
    first_costs = [costs[0] for _, _, costs in computed_rows]
    checks.check(
        "thm2-seed-exit",
        "every exhibited lex-first path starts with a cost-3 seed-exit",
        first_clauses == ["seed-exit"] * 7
        and first_costs == [3] * 7
        and all(walk[0] == ORIGIN for _, walk, _ in computed_rows)
        and all(hop_cost(ORIGIN, walk[1]) == 3 for _, walk, _ in computed_rows),
    )
    checks.check(
        "thm2-displayed",
        "the seed-exit statement is displayed, not adopted",
        "Displayed, not adopted." in note and "displayed, not adopted" in note.lower(),
    )

    lattice_lead = "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor"
    lattice_tail = "adjacency, standard translations, and proper cubic rotations about each site."
    admissibility_lead = "For each site, the probability distribution over the possibilities is"
    admissibility_tail = "determined by, and varies with, the nearest-neighbor conditions."
    record_lock = "When present, a record locks exactly one admissible local possibility."
    checks.check(
        "source-lattice",
        "current Lattice wording is pinned in the axiom memo and the note",
        lattice_lead in axiom and lattice_tail in axiom and lattice_lead in note and lattice_tail in note,
    )
    checks.check(
        "source-admissibility",
        "current Admissibility wording is pinned and nu is not written into it",
        admissibility_lead in axiom
        and admissibility_tail in axiom
        and admissibility_lead in note
        and admissibility_tail in note
        and "Do not write ν into Admissibility." in note
        and "hypothetical_axiom_status: no edit" in note,
    )
    checks.check(
        "thm3-no-l1",
        "the note refuses to attach L1 and treats the list as displayed, not adopted",
        "Do not attach L1." in note and "Displayed, not adopted." in note,
    )
    checks.check(
        "claim-scope",
        "front matter carries the declared claim_scope",
        CLAIM_SCOPE in note,
    )
    checks.check(
        "forbidden-phrases",
        "the note avoids the dispatch-forbidden phrases",
        all(phrase not in note for phrase in FORBIDDEN_PHRASES),
    )
    checks.check(
        "record-unused",
        "Record is quoted only as an unused boundary",
        record_lock in axiom and record_lock in note and "Record is not used" in note,
    )
    checks.check(
        "axiom-untouched",
        "the axiom memo is an input only and still names the four axioms",
        "### Admissibility / Local Constraint" in axiom and "ν(v→w)" not in axiom,
    )
    checks.check(
        "b6-only",
        "every executed hop and every named type stays inside B_6(0)",
        all(in_ball(site) for site in sites)
        and all(in_ball(rep) for rep in EXPECTED_REPS)
        and all(all(in_ball(site) for site in walk) for _, walk, _ in computed_rows)
        and BALL_RADIUS == 6
        and "B_6(0) only" in note,
    )

    print("per_element: checked exactly — each t=8 G+ representative and its lex-first path")
    print("per_site: checked exactly — first-arrival on the 377-site ball")
    print("per_mode: not used")
    print("per_block: checked exactly — seven hop-cost lists each summing to 8")
    print("lattice_wide: checked and not executed — no law outside B_6(0) is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
