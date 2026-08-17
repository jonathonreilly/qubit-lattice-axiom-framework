#!/usr/bin/env python3
"""Named (0,1,1) lex-first shortest path to (5,0,0) on B_16(0).

One Dijkstra from the origin. Displayed, not adopted. No axiom edit,
no cache write, no L1 hop-cost attachment.
"""

from __future__ import annotations

import ast
import heapq
from collections import defaultdict, deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_NAME = "CLAUSE_011_WHY_T500_IS_9_B16_BOUNDED_THEOREM_NOTE_2026-08-15.md"
NOTE_PATH = ROOT / "docs" / NOTE_NAME
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/CLAUSE_011_WHY_T500_IS_9_B16_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

BALL_RADIUS = 16
TARGET = (5, 0, 0)
NEIGHBOR_STEPS = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
FORBIDDEN_PARTS = (
    ("G_", "N"),
    ("1/", "r"),
    ("1/", "r^2"),
    ("Lattice-", "named"),
    ("not a ", "TOE"),
)
DIJKSTRA_CALLS = 0

Site = tuple[int, int, int]


def nn_radius(site: Site) -> int:
    return abs(site[0]) + abs(site[1]) + abs(site[2])


def in_ball(site: Site) -> bool:
    return nn_radius(site) <= BALL_RADIUS


def support_size(site: Site) -> int:
    return int(site[0] != 0) + int(site[1] != 0) + int(site[2] != 0)


def on_axis_1_skeleton(site: Site) -> bool:
    return support_size(site) <= 1


def hop_cost(src: Site, dst: Site) -> int:
    """Rule (0,1,1): cost 3 iff both weights 1 or support drop, else 1."""
    src_support = support_size(src)
    dst_support = support_size(dst)
    both_weights_one = src_support == 1 and dst_support == 1
    support_drop = dst_support < src_support
    if both_weights_one or support_drop:
        return 3
    return 1


def ball_sites() -> list[Site]:
    sites: list[Site] = []
    for x in range(-BALL_RADIUS, BALL_RADIUS + 1):
        for y in range(-BALL_RADIUS, BALL_RADIUS + 1):
            remain = BALL_RADIUS - abs(x) - abs(y)
            if remain < 0:
                continue
            for z in range(-remain, remain + 1):
                sites.append((x, y, z))
    return sites


def neighbors(site: Site) -> list[Site]:
    x, y, z = site
    out: list[Site] = []
    for dx, dy, dz in NEIGHBOR_STEPS:
        nxt = (x + dx, y + dy, z + dz)
        if in_ball(nxt):
            out.append(nxt)
    return out


def compact(site: Site) -> str:
    return f"({site[0]},{site[1]},{site[2]})"


def dijkstra_from_origin(sites: list[Site]) -> dict[Site, int]:
    global DIJKSTRA_CALLS
    DIJKSTRA_CALLS += 1
    origin = (0, 0, 0)
    dist = {origin: 0}
    heap = [(0, origin)]
    while heap:
        cost_here, site = heapq.heappop(heap)
        if cost_here != dist[site]:
            continue
        for nxt in neighbors(site):
            cand = cost_here + hop_cost(site, nxt)
            if cand < dist.get(nxt, 10**9):
                dist[nxt] = cand
                heapq.heappush(heap, (cand, nxt))
    if len(dist) != len(sites):
        raise RuntimeError("Dijkstra did not reach every site of B_16(0)")
    return dist


def shortest_path_predecessors(dist: dict[Site, int]) -> dict[Site, list[Site]]:
    preds: dict[Site, list[Site]] = defaultdict(list)
    for site in dist:
        for nxt in neighbors(site):
            if dist[site] + hop_cost(site, nxt) == dist[nxt]:
                preds[nxt].append(site)
    return preds


def nodes_on_shortest_paths(
    target: Site, preds: dict[Site, list[Site]]
) -> set[Site]:
    reach = {target}
    queue: deque[Site] = deque([target])
    while queue:
        site = queue.popleft()
        for pred in preds[site]:
            if pred not in reach:
                reach.add(pred)
                queue.append(pred)
    return reach


def lex_first_shortest_path(
    dist: dict[Site, int], target: Site
) -> tuple[list[Site], list[int], list[int]]:
    preds = shortest_path_predecessors(dist)
    reach = nodes_on_shortest_paths(target, preds)
    origin = (0, 0, 0)
    if origin not in reach:
        raise RuntimeError("origin is not on a shortest path to the target")
    path = [origin]
    current = origin
    while current != target:
        candidates = [
            nxt
            for nxt in neighbors(current)
            if nxt in reach and dist[current] + hop_cost(current, nxt) == dist[nxt]
        ]
        if not candidates:
            raise RuntimeError("lex-first walk left the shortest-path DAG")
        nxt = min(candidates)
        path.append(nxt)
        current = nxt
    hop_costs = [hop_cost(src, dst) for src, dst in zip(path, path[1:])]
    running = [0]
    for cost in hop_costs:
        running.append(running[-1] + cost)
    return path, hop_costs, running


def format_hop_sequence(path: list[Site], hop_costs: list[int]) -> str:
    parts = [compact(path[0])]
    for dst, cost in zip(path[1:], hop_costs):
        parts.append(f"--{cost}-->")
        parts.append(compact(dst))
    return " ".join(parts)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool) -> None:
        result = bool(condition)
        self.passed += int(result)
        self.failed += int(not result)
        print(f"{'PASS' if result else 'FAIL'}: {label} {statement}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def audit_paths_are_static_literals() -> bool:
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source)
    for node in tree.body:
        if isinstance(node, ast.Assign):
            names = [t.id for t in node.targets if isinstance(t, ast.Name)]
            if "AUDIT_INPUT_PATHS" in names:
                value = node.value
                if not isinstance(value, ast.Tuple):
                    return False
                return all(
                    isinstance(elt, ast.Constant) and isinstance(elt.value, str)
                    for elt in value.elts
                )
    return False


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")

    print(
        "external_scientific_inputs: none; hop-costs are the named (0,1,1) "
        "rule on the finite 16-hop neighborhood B_16(0)"
    )
    print(
        "package_local_integrity_reads: the note and current minimal axiom "
        "are read; no cache or governance surface is written"
    )
    print(
        "negative_scope: the named rule is displayed, not adopted; it is "
        "not written into Admissibility and is not attached as an L1 hop-cost"
    )
    print("cache_write: false")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required static literal pair and both files exist",
        AUDIT_INPUT_PATHS
        == (
            "docs/CLAUSE_011_WHY_T500_IS_9_B16_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and audit_paths_are_static_literals()
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    )

    sites = ball_sites()
    checks.check(
        "ball-b16-only",
        "B_16(0) is the 16-hop neighborhood of the origin and contains (5,0,0)",
        len(sites) == 6017
        and in_ball(TARGET)
        and TARGET in sites
        and (16, 0, 0) in set(sites)
        and (17, 0, 0) not in set(sites)
        and nn_radius(TARGET) == 5,
    )

    checks.check(
        "clause-011-local",
        "seed-exit costs 1; axis 1-skeleton and support-drop cost 3; else 1",
        hop_cost((0, 0, 0), (1, 0, 0)) == 1
        and hop_cost((0, 0, 0), (0, -1, 0)) == 1
        and hop_cost((1, 0, 0), (2, 0, 0)) == 3
        and hop_cost((1, 1, 0), (1, 0, 0)) == 3
        and hop_cost((5, -1, 0), (5, 0, 0)) == 3
        and hop_cost((1, -1, 0), (2, -1, 0)) == 1
        and hop_cost((1, 0, 0), (1, 1, 0)) == 1,
    )

    distances = dijkstra_from_origin(sites)
    path, hop_costs, running = lex_first_shortest_path(distances, TARGET)
    hop_sequence = format_hop_sequence(path, hop_costs)
    first_hop_cost = hop_costs[0]
    leaves_axis = any(not on_axis_1_skeleton(site) for site in path)
    first_off_axis = next(site for site in path if not on_axis_1_skeleton(site))
    axis_skeleton_sum = 1 + 3 * 4

    print(f"n_sites {len(sites)}")
    print(f"dijkstra_calls {DIJKSTRA_CALLS}")
    print("dijkstra_count=1")
    print(f"t(5,0,0)={distances[TARGET]}")
    print(f"lex_first_path {hop_sequence}")
    print(f"running_cost {','.join(str(value) for value in running)}")
    print(f"first_hop_cost {first_hop_cost}")
    print(f"leaves_axis_1_skeleton {leaves_axis}")
    print(f"first_off_axis {compact(first_off_axis)}")
    print(f"axis_skeleton_sum {axis_skeleton_sum}")

    checks.check(
        "theorem-1-time",
        "one Dijkstra gives t(5,0,0)=9",
        distances[TARGET] == 9 and running[-1] == 9,
    )
    checks.check(
        "theorem-1-path",
        "the lex-first hop sequence stays in B_16(0) and its costs sum to t(5,0,0)",
        path[0] == (0, 0, 0)
        and path[-1] == TARGET
        and all(in_ball(site) for site in path)
        and all(
            hop_cost(src, dst) == cost
            for (src, dst), cost in zip(zip(path, path[1:]), hop_costs)
        )
        and sum(hop_costs) == distances[TARGET]
        and running == [0, 1, 2, 3, 4, 5, 6, 9],
    )
    checks.check(
        "theorem-1-lex-first",
        "each hop is the lex-least shortest-path-DAG successor",
        path
        == lex_first_shortest_path(distances, TARGET)[0]
        and path
        == [
            (0, 0, 0),
            (0, -1, 0),
            (1, -1, 0),
            (2, -1, 0),
            (3, -1, 0),
            (4, -1, 0),
            (5, -1, 0),
            (5, 0, 0),
        ]
        and hop_costs == [1, 1, 1, 1, 1, 1, 3],
    )
    checks.check(
        "theorem-2-first-hop",
        "the first hop is a cost-1 seed-exit and the path leaves the axis 1-skeleton",
        first_hop_cost == 1
        and path[1] == (0, -1, 0)
        and on_axis_1_skeleton(path[0])
        and on_axis_1_skeleton(path[1])
        and leaves_axis
        and first_off_axis == (1, -1, 0)
        and hop_cost((0, 0, 0), (0, -1, 0)) == 1,
    )
    checks.check(
        "one-dijkstra",
        "exactly one origin Dijkstra assigned a finite time to every ball site",
        DIJKSTRA_CALLS == 1
        and len(distances) == len(sites)
        and all(distances[site] >= 0 for site in sites),
    )
    checks.check(
        "note-reports-path",
        "the note reports t(5,0,0)=9 and the computed hop sequence with running cost",
        "t(5,0,0)=9" in note
        and hop_sequence in note
        and "0,1,2,3,4,5,6,9" in note
        and "(0,-1,0)" in note
        and "(5,-1,0)" in note,
    )
    checks.check(
        "note-reports-first-hop",
        "the note displays the first-hop cost and the axis-skeleton exit",
        "first-hop cost is 1" in note
        and "leaves the axis 1-skeleton" in note
        and "seed-exit" in note
        and compact(first_off_axis) in note,
    )
    checks.check(
        "displayed-not-adopted",
        "the note displays the (0,1,1) scores and does not adopt them",
        "Displayed, not adopted" in note
        and "do not write (0,1,1) into Admissibility" in note
        and "Do not attach L1" in note,
    )
    checks.check(
        "admissibility-unedited",
        "the current axiom memo still names Admissibility and does not contain the hop-cost rule",
        "Admissibility" in axiom
        and "Lattice" in axiom
        and "Qubit" in axiom
        and "Record" in axiom
        and "both weights 1 or support drop" not in axiom
        and "(0,1,1)" not in axiom,
    )
    checks.check(
        "no-axiom-edit",
        "note records hypothetical axiom status no edit",
        'hypothetical_axiom_status: "no edit"' in note,
    )
    checks.check(
        "claim-scope",
        "the note states the required claim_scope",
        "A lex-first shortest path to (5,0,0) under the named (0,1,1) hop-cost on B_16(0) is named"
        in note,
    )
    forbidden = tuple("".join(parts) for parts in FORBIDDEN_PARTS)
    forbidden_hits = [token for token in forbidden if token in note]
    checks.check(
        "forbidden-tokens",
        "the note avoids the forbidden tokens",
        forbidden_hits == [],
    )
    checks.check(
        "uniqueness-not-required",
        "the note does not claim uniqueness of the named path or rule",
        "Uniqueness is not required" in note
        and "unique hop-cost" not in note
        and "unique shortest path" not in note,
    )
    checks.check(
        "not-attach-l1",
        "the displayed rule is not attached to L1",
        "Do not attach L1" in note and "Do not attach L1" not in axiom,
    )
    checks.check(
        "cheaper-than-axis-skeleton",
        "the named path is cheaper than the axis 1-skeleton sum 13",
        distances[TARGET] == 9
        and axis_skeleton_sum == 13
        and distances[TARGET] < axis_skeleton_sum
        and "1+3+3+3+3=13" in note,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
