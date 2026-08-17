#!/usr/bin/env python3
"""Lex-first shortest 0 → (4,0,0) path under the named support-drop hop-cost.

Finite Dijkstra on B_6(0). No cache write, no axiom edit, no citation
manifest, and no identification of the displayed hop-cost with Admissibility.
"""

from __future__ import annotations

from heapq import heappop, heappush
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "SUPPORT_DROP_AXIS_PATH_B6_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/SUPPORT_DROP_AXIS_PATH_B6_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Point = tuple[int, int, int]
ORIGIN: Point = (0, 0, 0)
TARGET: Point = (4, 0, 0)
RADIUS = 6
SHIFTS: tuple[Point, ...] = (
    (-1, 0, 0),
    (1, 0, 0),
    (0, -1, 0),
    (0, 1, 0),
    (0, 0, -1),
    (0, 0, 1),
)
INF = 10**9


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool) -> None:
        ok = bool(condition)
        self.passed += int(ok)
        self.failed += int(not ok)
        print(f"{'PASS' if ok else 'FAIL'}: {label} {statement}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def l1_norm(site: Point) -> int:
    return abs(site[0]) + abs(site[1]) + abs(site[2])


def in_ball(site: Point) -> bool:
    return l1_norm(site) <= RADIUS


def ball_sites() -> tuple[Point, ...]:
    return tuple(
        (x, y, z)
        for x in range(-RADIUS, RADIUS + 1)
        for y in range(-RADIUS, RADIUS + 1)
        for z in range(-RADIUS, RADIUS + 1)
        if in_ball((x, y, z))
    )


def weight(site: Point) -> int:
    return sum(1 for coord in site if coord != 0)


def hop_cost(src: Point, dst: Point) -> int:
    src_w = weight(src)
    dst_w = weight(dst)
    if src_w == 0 or (src_w == 1 and dst_w == 1) or dst_w < src_w:
        return 3
    return 1


def neighbors(site: Point) -> tuple[Point, ...]:
    out: list[Point] = []
    for shift in SHIFTS:
        nxt = (site[0] + shift[0], site[1] + shift[1], site[2] + shift[2])
        if in_ball(nxt):
            out.append(nxt)
    return tuple(sorted(out))


def dijkstra(source: Point) -> dict[Point, int]:
    sites = ball_sites()
    dist = {site: INF for site in sites}
    dist[source] = 0
    heap: list[tuple[int, Point]] = [(0, source)]
    while heap:
        cost, site = heappop(heap)
        if cost != dist[site]:
            continue
        for nxt in neighbors(site):
            cand = cost + hop_cost(site, nxt)
            if cand < dist[nxt]:
                dist[nxt] = cand
                heappush(heap, (cand, nxt))
    return dist


def reverse_dist(target: Point) -> dict[Point, int]:
    sites = ball_sites()
    dist = {site: INF for site in sites}
    dist[target] = 0
    heap: list[tuple[int, Point]] = [(0, target)]
    while heap:
        cost, site = heappop(heap)
        if cost != dist[site]:
            continue
        for prev in neighbors(site):
            cand = cost + hop_cost(prev, site)
            if cand < dist[prev]:
                dist[prev] = cand
                heappush(heap, (cand, prev))
    return dist


def lex_first_shortest(source: Point, target: Point) -> tuple[tuple[Point, ...], tuple[int, ...]]:
    forward = dijkstra(source)
    backward = reverse_dist(target)
    total = forward[target]
    if total >= INF:
        raise RuntimeError("target unreachable in B_6(0)")
    path = [source]
    while path[-1] != target:
        site = path[-1]
        candidates = [
            nxt
            for nxt in neighbors(site)
            if forward[site] + hop_cost(site, nxt) + backward[nxt] == total
            and forward[nxt] == forward[site] + hop_cost(site, nxt)
        ]
        if not candidates:
            raise RuntimeError(f"lex reconstruction stuck at {site}")
        path.append(min(candidates))
    costs = tuple(hop_cost(path[i], path[i + 1]) for i in range(len(path) - 1))
    return tuple(path), costs


def enumerate_shortest(source: Point, target: Point) -> tuple[tuple[Point, ...], ...]:
    forward = dijkstra(source)
    backward = reverse_dist(target)
    total = forward[target]
    found: list[tuple[Point, ...]] = []
    stack: list[list[Point]] = [[source]]
    while stack:
        walk = stack.pop()
        site = walk[-1]
        if site == target:
            found.append(tuple(walk))
            continue
        for nxt in neighbors(site):
            if (
                forward[site] + hop_cost(site, nxt) + backward[nxt] == total
                and forward[nxt] == forward[site] + hop_cost(site, nxt)
            ):
                stack.append(walk + [nxt])
    return tuple(sorted(found))


def axis_only_path() -> tuple[tuple[Point, ...], tuple[int, ...]]:
    path = tuple((k, 0, 0) for k in range(5))
    costs = tuple(hop_cost(path[i], path[i + 1]) for i in range(len(path) - 1))
    return path, costs


def site_text(site: Point) -> str:
    return f"({site[0]},{site[1]},{site[2]})"


def path_text(path: tuple[Point, ...]) -> str:
    return " → ".join(site_text(site) for site in path)


def cost_text(costs: tuple[int, ...]) -> str:
    return ", ".join(str(cost) for cost in costs)


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    self_source = Path(__file__).read_text(encoding="utf-8")
    for relative in AUDIT_INPUT_PATHS:
        (ROOT / relative).read_text(encoding="utf-8")

    print("external_scientific_inputs: live Lattice / Admissibility / Record sentences only")
    print("integrity_reads: this runner, its note, and the axiom memo; no cache")
    print("construction: named support-drop hop-cost on the six-neighbor graph of B_6(0)")
    print("negative_scope: displayed path is not an Admissibility rule and is not a coordinate-sum law")

    sites = ball_sites()
    path, costs = lex_first_shortest(ORIGIN, TARGET)
    shortest = enumerate_shortest(ORIGIN, TARGET)
    axis_path, axis_costs = axis_only_path()
    arrival = sum(costs)
    axis_arrival = sum(axis_costs)
    lex_min = min(shortest)

    print(f"ball_size: {len(sites)}")
    print(f"lex_path: {path_text(path)}")
    print(f"lex_costs: {cost_text(costs)}")
    print(f"lex_sum: {arrival}")
    print(f"axis_path: {path_text(axis_path)}")
    print(f"axis_costs: {cost_text(axis_costs)}")
    print(f"axis_sum: {axis_arrival}")
    print(f"n_shortest: {len(shortest)}")

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/SUPPORT_DROP_AXIS_PATH_B6_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and AUDIT_TIMEOUT_SEC == 120,
    )
    checks.check(
        "ball-is-b6",
        "B_6(0) has 377 sites",
        len(sites) == 377 and all(in_ball(site) for site in path + axis_path),
    )
    checks.check(
        "named-rule-seed-exit",
        "seed-exit from the origin costs 3",
        hop_cost(ORIGIN, (1, 0, 0)) == 3 and hop_cost(ORIGIN, (0, -1, 0)) == 3,
    )
    checks.check(
        "named-rule-axis-axis",
        "both-weight-1 axis continuation costs 3",
        hop_cost((1, 0, 0), (2, 0, 0)) == 3 and hop_cost((3, 0, 0), (4, 0, 0)) == 3,
    )
    checks.check(
        "named-rule-support-drop",
        "a coordinate-support drop costs 3",
        hop_cost((4, -1, 0), (4, 0, 0)) == 3 and hop_cost((1, 1, 0), (1, 0, 0)) == 3,
    )
    checks.check(
        "named-rule-face-walk",
        "a support-raising or equal-face hop costs 1",
        hop_cost((0, -1, 0), (1, -1, 0)) == 1 and hop_cost((1, -1, 0), (2, -1, 0)) == 1,
    )
    checks.check(
        "thm1-lex-path",
        "lex-first shortest path is the computed site list",
        path == lex_min == (
            (0, 0, 0),
            (0, -1, 0),
            (1, -1, 0),
            (2, -1, 0),
            (3, -1, 0),
            (4, -1, 0),
            (4, 0, 0),
        )
        and path[-1] == TARGET
        and path[0] == ORIGIN,
    )
    checks.check(
        "thm1-hop-costs-sum-10",
        "lex-first hop costs are 3,1,1,1,1,3 and sum to 10",
        costs == (3, 1, 1, 1, 1, 3) and arrival == 10 and arrival == dijkstra(ORIGIN)[TARGET],
    )
    checks.check(
        "thm1-note-exhibits-path",
        "note exhibits the computed sites and hop costs",
        path_text(path) in note
        and cost_text(costs) in note
        and "sum to 10" in note,
    )
    checks.check(
        "thm2-axis-costs-12",
        "on-axis-only path costs 12 and is strictly longer",
        axis_path == ((0, 0, 0), (1, 0, 0), (2, 0, 0), (3, 0, 0), (4, 0, 0))
        and axis_costs == (3, 3, 3, 3)
        and axis_arrival == 12
        and axis_arrival > arrival,
    )
    checks.check(
        "thm2-axis-displayed-not-adopted",
        "note displays the axis path and does not adopt it",
        path_text(axis_path) in note
        and cost_text(axis_costs) in note
        and "Displayed, not adopted." in note
        and "on-axis-only path costs 12" in note,
    )
    checks.check(
        "thm3-not-written-into-admissibility",
        "ν is not written into Admissibility",
        "Do not write ν into Admissibility." in note
        and "ν(" not in axiom
        and "support-drop" not in axiom
        and "There is one fixed nearest-neighbor admissibility rule" in axiom,
    )
    checks.check(
        "thm3-do-not-attach-l1",
        "note refuses to attach L1",
        "Do not attach L1." in note
        and "not leftover of the arrival number" in note,
    )
    checks.check(
        "shortest-family-size",
        "exactly eight shortest paths, all of cost 10",
        len(shortest) == 8
        and all(
            sum(hop_cost(walk[i], walk[i + 1]) for i in range(len(walk) - 1)) == 10
            for walk in shortest
        ),
    )
    checks.check(
        "mutation-axis-as-shortest-fails",
        "predicate that the axis path is shortest fails",
        axis_arrival != arrival,
    )
    forbidden = (
        "G" + "_N",
        "1/" + "r",
        "1/" + "r^2",
        "Lattice" + "-named",
        "not a " + "TOE",
    )
    checks.check(
        "forbidden-tokens",
        "forbidden tokens are absent from note and runner",
        all(token not in note and token not in self_source for token in forbidden),
    )
    checks.check(
        "claim-scope-and-type",
        "front matter and type match the exhibited path claim",
        'claim_type: bounded_theorem' in note
        and "**Type:** bounded_theorem" in note
        and "A shortest 0→(4,0,0) path under the named support-drop hop-cost is exhibited and sums to 10."
        in note
        and "Displayed, not adopted." in note,
    )
    checks.check(
        "machine-status-contract",
        "note carries bounded-support status and no hypothetical axiom",
        'hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"'
        in note
        and "actual_current_surface_status: bounded-support" in note
        and "next_trace_action:" in note,
    )
    checks.check(
        "n1-n8-gate",
        "N1-N8 headings and a passing no-go disposition are present",
        all(f"### N{index}" in note for index in range(1, 9))
        and "No-Go Discipline disposition: **PASS**" in note
        and note.count("**ATTEMPTED**") == 6,
    )
    checks.check(
        "axiom-quotes",
        "Lattice nearest-neighbor and Record lock sentences are quoted",
        "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor"
        in note
        and "When present, a record locks exactly one admissible local possibility."
        in note
        and "A site with no record cannot be read." in axiom,
    )

    print("per_element: checked exactly — each displayed hop cost is the named support-drop rule")
    print("per_site: checked exactly — every site of the exhibited walks lies in B_6(0)")
    print("per_mode: checked exactly — lex-first among the eight cost-10 walks is selected")
    print("per_block: checked exactly — axis-only cost 12 is displayed and not adopted")
    print("lattice_wide: checked and not executed — no Admissibility rewrite or whole-lattice law")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
