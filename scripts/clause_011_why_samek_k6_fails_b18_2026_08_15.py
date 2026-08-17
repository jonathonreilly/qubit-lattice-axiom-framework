#!/usr/bin/env python3
"""Exact lex-first shortest paths under the named (0,1,1) hop-cost on B_18(0).

One origin Dijkstra names t(6,0,0), t(6,6,6), and the lex-first shortest
paths. The same-k reverse comparison is displayed, not adopted. No cache
write. No axiom edit.
"""

from __future__ import annotations

import ast
from collections import deque
from heapq import heappop, heappush
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/CLAUSE_011_WHY_SAMEK_K6_FAILS_B18_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/CLAUSE_011_WHY_SAMEK_K6_FAILS_B18_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Point = tuple[int, int, int]
ORIGIN: Point = (0, 0, 0)
AXIS: Point = (6, 0, 0)
BODY: Point = (6, 6, 6)
RADIUS = 18
SHIFTS: tuple[Point, ...] = (
    (-1, 0, 0),
    (0, -1, 0),
    (0, 0, -1),
    (0, 0, 1),
    (0, 1, 0),
    (1, 0, 0),
)
CLAIM_SCOPE = (
    "Lex-first shortest paths to (6,0,0) and (6,6,6) under the named "
    "(0,1,1) hop-cost on B_18(0) are named. Displayed, not adopted."
)
FORBIDDEN_PARTS = (
    ("G_", "N"),
    ("1/", "r"),
    ("1/", "r^2"),
    ("Lattice-", "named"),
    ("not a ", "TOE"),
)
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


def normalize(text: str) -> str:
    return " ".join(text.split())


def l1(point: Point) -> int:
    return abs(point[0]) + abs(point[1]) + abs(point[2])


def in_ball(point: Point) -> bool:
    return l1(point) <= RADIUS


def add(left: Point, right: Point) -> Point:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


def neighbors(point: Point) -> tuple[Point, ...]:
    return tuple(cand for shift in SHIFTS if in_ball(cand := add(point, shift)))


def support_size(point: Point) -> int:
    return sum(coord != 0 for coord in point)


def hop_cost(src: Point, dst: Point) -> int:
    """Named (0,1,1) rule: cost 3 iff both weights 1 or support drop, else 1."""

    src_w = support_size(src)
    dst_w = support_size(dst)
    if (src_w == 1 and dst_w == 1) or dst_w < src_w:
        return 3
    return 1


def ball_sites() -> list[Point]:
    sites: list[Point] = []
    for x in range(-RADIUS, RADIUS + 1):
        for y in range(-RADIUS, RADIUS + 1):
            remain = RADIUS - abs(x) - abs(y)
            if remain < 0:
                continue
            for z in range(-remain, remain + 1):
                sites.append((x, y, z))
    return sites


def dijkstra_from_origin() -> dict[Point, int]:
    global DIJKSTRA_CALLS
    DIJKSTRA_CALLS += 1
    dist = {ORIGIN: 0}
    heap: list[tuple[int, Point]] = [(0, ORIGIN)]
    while heap:
        cost, site = heappop(heap)
        if cost != dist[site]:
            continue
        for nxt in neighbors(site):
            trial = cost + hop_cost(site, nxt)
            prior = dist.get(nxt)
            if prior is None or trial < prior:
                dist[nxt] = trial
                heappush(heap, (trial, nxt))
    return dist


def on_shortest_paths(dist: dict[Point, int], target: Point) -> set[Point]:
    marked = {target}
    queue = deque([target])
    while queue:
        site = queue.popleft()
        for prev in neighbors(site):
            if prev not in dist:
                continue
            if dist[site] == dist[prev] + hop_cost(prev, site) and prev not in marked:
                marked.add(prev)
                queue.append(prev)
    return marked


def lex_first_path(dist: dict[Point, int], target: Point) -> tuple[Point, ...]:
    allowed = on_shortest_paths(dist, target)
    path = [ORIGIN]
    site = ORIGIN
    while site != target:
        choices = [
            nxt
            for nxt in neighbors(site)
            if nxt in allowed and dist[nxt] == dist[site] + hop_cost(site, nxt)
        ]
        if not choices:
            raise RuntimeError(f"no lex successor from {site} toward {target}")
        site = min(choices)
        path.append(site)
    return tuple(path)


def path_costs(path: tuple[Point, ...]) -> tuple[int, ...]:
    return tuple(hop_cost(path[index], path[index + 1]) for index in range(len(path) - 1))


def format_path(path: tuple[Point, ...]) -> str:
    return "->".join(str(site).replace(" ", "") for site in path)


def format_costs(costs: tuple[int, ...]) -> str:
    return "(" + ",".join(str(cost) for cost in costs) + ")"


def shortest_path_count(dist: dict[Point, int], target: Point) -> int:
    allowed = on_shortest_paths(dist, target)
    memo: dict[Point, int] = {}

    def walk(site: Point) -> int:
        cached = memo.get(site)
        if cached is not None:
            return cached
        if site == target:
            memo[site] = 1
            return 1
        total = sum(
            walk(nxt)
            for nxt in neighbors(site)
            if nxt in allowed and dist[nxt] == dist[site] + hop_cost(site, nxt)
        )
        memo[site] = total
        return total

    return walk(ORIGIN)


def literal_audit_paths(source: str) -> tuple[str, ...] | None:
    module = ast.parse(source)
    for node in module.body:
        if not isinstance(node, ast.Assign):
            continue
        if not any(isinstance(tgt, ast.Name) and tgt.id == "AUDIT_INPUT_PATHS" for tgt in node.targets):
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


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    source = Path(__file__).read_text(encoding="utf-8")
    note_n = normalize(note)
    axiom_n = normalize(axiom)

    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print("cache_write: false")
    print("dijkstra_count_budget: 1")
    print(f"claim_scope: {CLAIM_SCOPE}")

    checks.check(
        "audit-input-paths",
        "declared inputs are exactly the source note and current axiom memo",
        AUDIT_INPUT_PATHS == (NOTE_REL, AXIOM_REL)
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
        AUDIT_INPUT_PATHS,
    )
    checks.check(
        "audit-input-literal",
        "AUDIT_INPUT_PATHS is a static string-literal tuple",
        literal_audit_paths(source) == AUDIT_INPUT_PATHS,
    )
    checks.check(
        "claim-scope",
        "note claim_scope matches the displayed scoring statement",
        CLAIM_SCOPE in note_n,
    )
    checks.check(
        "displayed-not-adopted",
        "the rule is displayed, not adopted",
        "Displayed, not adopted" in note or "displayed, not adopted" in note,
    )
    checks.check(
        "not-in-admissibility",
        "(0,1,1) is not written into Admissibility",
        "Do not write (0,1,1) into Admissibility" in note
        and "both weights 1 or support drop" not in axiom
        and "(0,1,1)" not in axiom,
    )
    checks.check(
        "not-attach-l1",
        "the displayed rule is not attached to L1",
        "Do not attach L1" in note and "Do not attach L1" not in axiom,
    )
    checks.check(
        "uniqueness-not-claimed",
        "uniqueness among hop-costs or shortest paths is not claimed",
        "Uniqueness is not required" in note or "no uniqueness" in note.lower(),
    )
    checks.check(
        "no-axiom-edit",
        "note records hypothetical axiom status no edit",
        'hypothetical_axiom_status: "no edit"' in note,
    )
    forbidden = tuple("".join(parts) for parts in FORBIDDEN_PARTS)
    forbidden_hits = [token for token in forbidden if token in note]
    checks.check(
        "forbidden-absent",
        "forbidden phrases are absent from the source note",
        forbidden_hits == [],
        forbidden_hits,
    )

    lattice_sentence = "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor"
    admissibility_fixed = "There is one fixed nearest-neighbor admissibility rule, covariant under lattice"
    admissibility_sentence = (
        "For each site, the probability distribution over the possibilities is "
        "determined by, and varies with, the nearest-neighbor conditions."
    )
    checks.check(
        "source-lattice",
        "current cubic nearest-neighbor wording is pinned",
        lattice_sentence in axiom_n and lattice_sentence in note,
    )
    checks.check(
        "source-admissibility",
        "current one-fixed-rule wording is pinned",
        admissibility_fixed in axiom_n
        and admissibility_sentence in axiom_n
        and admissibility_sentence in note_n,
    )

    sites = ball_sites()
    nonzero = [site for site in sites if site != ORIGIN]
    checks.check(
        "ball-b18",
        "B_18(0) has 8473 sites and contains both named targets",
        len(sites) == 8473
        and len(nonzero) == 8472
        and AXIS in set(sites)
        and BODY in set(sites)
        and (18, 0, 0) in set(sites)
        and (19, 0, 0) not in set(sites)
        and l1(BODY) == 18
        and l1(AXIS) == 6
        and all(l1(site) <= 18 for site in sites),
    )

    cost_table = (
        (ORIGIN, (1, 0, 0), 1),
        ((1, 0, 0), (2, 0, 0), 3),
        ((1, 0, 0), (1, 1, 0), 1),
        ((1, 1, 0), (1, 0, 0), 3),
        ((1, 1, 0), (1, 1, 1), 1),
        ((1, 0, 0), ORIGIN, 3),
    )
    checks.check(
        "hop-cost-rule",
        "cost is 3 iff both support weights are 1 or the hop drops support, else 1",
        all(hop_cost(src, dst) == value for src, dst, value in cost_table),
        [(src, dst, hop_cost(src, dst), value) for src, dst, value in cost_table],
    )

    dist = dijkstra_from_origin()
    t600 = dist[AXIS]
    t666 = dist[BODY]
    reverse = 3 * t600 * t600 > t666 * t666
    path600 = lex_first_path(dist, AXIS)
    path666 = lex_first_path(dist, BODY)
    costs600 = path_costs(path600)
    costs666 = path_costs(path666)
    n600 = shortest_path_count(dist, AXIS)
    axis_only = (ORIGIN, (1, 0, 0), (2, 0, 0), (3, 0, 0), (4, 0, 0), (5, 0, 0), AXIS)
    axis_only_cost = sum(path_costs(axis_only))

    print(f"n_sites {len(sites)}")
    print(f"t(6,0,0) {t600}")
    print(f"t(6,6,6) {t666}")
    print(f"t(6,0,0)^2/36 {t600 * t600}/36")
    print(f"t(6,6,6)^2/108 {t666 * t666}/108")
    print(f"3t_axis^2 {3 * t600 * t600}")
    print(f"t_body^2 {t666 * t666}")
    print(f"reverse {reverse}")
    print(f"lex_first_axis_path: {format_path(path600)}")
    print(f"lex_first_axis_costs: {format_costs(costs600)} sum={sum(costs600)}")
    print(f"lex_first_body_path: {format_path(path666)}")
    print(f"lex_first_body_costs: {format_costs(costs666)} sum={sum(costs666)}")
    print(f"n_shortest_axis {n600}")
    print(f"axis_only_cost {axis_only_cost}")
    print(f"dijkstra_calls {DIJKSTRA_CALLS}")

    checks.check(
        "one-dijkstra",
        "exactly one Dijkstra ran",
        DIJKSTRA_CALLS == 1 and len(dist) == 8473,
        DIJKSTRA_CALLS,
    )
    checks.check(
        "t-600-666",
        "t(6,0,0)=10 and t(6,6,6)=18",
        t600 == 10 and t666 == 18,
        (t600, t666),
    )
    checks.check(
        "reverse-k6-fails",
        "t(6,0,0)^2/36 > t(6,6,6)^2/108 fails",
        reverse is False
        and t600 * t600 == 100
        and t666 * t666 == 324
        and 3 * t600 * t600 == 300,
        (t600 * t600, t666 * t666, reverse),
    )
    checks.check(
        "lex-path-600",
        "lex-first shortest path to (6,0,0) is the named face detour",
        path600
        == (
            ORIGIN,
            (0, -1, 0),
            (1, -1, 0),
            (2, -1, 0),
            (3, -1, 0),
            (4, -1, 0),
            (5, -1, 0),
            (6, -1, 0),
            AXIS,
        )
        and costs600 == (1, 1, 1, 1, 1, 1, 1, 3)
        and sum(costs600) == 10,
        path600,
    )
    checks.check(
        "lex-path-666",
        "lex-first shortest path to (6,6,6) is the named support-nondecreasing walk",
        path666
        == (
            ORIGIN,
            (0, 0, 1),
            (0, 1, 1),
            (0, 1, 2),
            (0, 1, 3),
            (0, 1, 4),
            (0, 1, 5),
            (0, 1, 6),
            (0, 2, 6),
            (0, 3, 6),
            (0, 4, 6),
            (0, 5, 6),
            (0, 6, 6),
            (1, 6, 6),
            (2, 6, 6),
            (3, 6, 6),
            (4, 6, 6),
            (5, 6, 6),
            BODY,
        )
        and costs666 == (1,) * 18
        and sum(costs666) == 18,
        path666,
    )
    checks.check(
        "note-records-times",
        "note records the two computed arrivals",
        "`10`" in note
        and "`18`" in note
        and "`(6,0,0)`" in note
        and "`(6,6,6)`" in note
        and "t(6,0,0)=10" in note
        and "t(6,6,6)=18" in note,
    )
    checks.check(
        "note-records-paths",
        "note exhibits both lex-first walks and hop-cost lists",
        format_path(path600) in note
        and format_path(path666) in note
        and format_costs(costs600) in note
        and format_costs(costs666) in note,
        (format_path(path600), format_costs(costs600)),
    )
    checks.check(
        "note-records-reverse-products",
        "note records the integer reverse products",
        "100/36" in note and "324/108" in note and "300 > 324" in note,
    )
    checks.check(
        "not-leftover-of-no-bit",
        "the walks are longer than a leftover of the no bit",
        len(costs600) == 8
        and len(costs666) == 18
        and n600 == 8
        and axis_only_cost == 16
        and axis_only_cost > t600
        and t600 != l1(AXIS)
        and "not leftover of the no bit" in note,
    )
    checks.check(
        "first-hop-costs",
        "both lex-first first hops have cost 1",
        costs600[0] == 1 and costs666[0] == 1 and hop_cost(ORIGIN, (1, 0, 0)) == 1,
    )
    checks.check(
        "l1-not-attached",
        "t(6,0,0)=10 is not the taxicab length 6",
        t600 == 10 and t600 != 6 and t666 == l1(BODY) and "Do not attach L1" in note,
    )
    checks.check(
        "k6-needs-b18",
        "(6,6,6) lies outside B_16(0) and the note says so",
        l1(BODY) == 18
        and BODY in dist
        and "absent from `B_16(0)`" in note
        and "B_18(0)" in note,
    )
    checks.check(
        "note-contract",
        "machine fields, exhibition wording, N1-N8, and hygiene hold",
        all(
            phrase in note
            for phrase in (
                CLAIM_SCOPE,
                "actual_current_surface_status: bounded-support",
                "target_claim_type: bounded_theorem",
                'hypothetical_axiom_status: "no edit"',
                "audit_required_before_effective_retained: true",
                "bare_retained_allowed: false",
                "authors no audit verdict",
                "FAIL / DO NOT SHIP",
                "**Type:** bounded_theorem",
            )
        )
        and all(f"### N{index}" in note for index in range(1, 9)),
    )
    checks.check(
        "axiom-untouched",
        "the axiom memo is an input only and still names the four axioms",
        "### Admissibility / Local Constraint" in axiom
        and "### Lattice / Physical Locality" in axiom
        and "### Qubit / Site Possibility" in axiom
        and "### Record / Fixed Reality" in axiom,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
