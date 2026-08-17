#!/usr/bin/env python3
"""Exact shortest-path checks for the named support-drop hop-cost.

The runner computes a lexicographically first shortest path from one seed
to (2,2,2) on the six-neighbor ball of radius 6 and sums the hop costs.
It does not write a cache or edit the axiom memo.
"""

from __future__ import annotations

from collections import defaultdict
from heapq import heappop, heappush
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "NO_SHORTCUT_BODY_DIAGONAL_PATH_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/NO_SHORTCUT_BODY_DIAGONAL_PATH_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Site = tuple[int, int, int]
SEED: Site = (0, 0, 0)
TARGET: Site = (2, 2, 2)
STEPS: tuple[Site, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
RADIUS = 6
FORBIDDEN = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE")


def add(left: Site, right: Site) -> Site:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


def graph_radius(site: Site) -> int:
    return abs(site[0]) + abs(site[1]) + abs(site[2])


def inward_weight(site: Site) -> int:
    return int(site[0] != 0) + int(site[1] != 0) + int(site[2] != 0)


def hop_cost(source: Site, dest: Site) -> int:
    weight_source = inward_weight(source)
    weight_dest = inward_weight(dest)
    if (
        weight_source == 0
        or (weight_source == 1 and weight_dest == 1)
        or weight_dest < weight_source
    ):
        return 3
    return 1


def hop_cost_axis_skeleton(source: Site, dest: Site) -> int:
    weight_source = inward_weight(source)
    weight_dest = inward_weight(dest)
    if weight_source == 0 or (weight_source == 1 and weight_dest == 1):
        return 3
    return 1


def hop_clause(source: Site, dest: Site) -> str:
    weight_source = inward_weight(source)
    weight_dest = inward_weight(dest)
    if weight_source == 0:
        return "seed-exit"
    if weight_source == 1 and weight_dest == 1:
        return "both-weights-1"
    if weight_dest < weight_source:
        return "support-drop"
    return "neither"


def neighbors(site: Site) -> tuple[Site, ...]:
    out = []
    for step in STEPS:
        dest = add(site, step)
        if graph_radius(dest) <= RADIUS:
            out.append(dest)
    return tuple(sorted(out))


def ball_sites() -> tuple[Site, ...]:
    sites = []
    for x in range(-RADIUS, RADIUS + 1):
        for y in range(-RADIUS, RADIUS + 1):
            for z in range(-RADIUS, RADIUS + 1):
                site = (x, y, z)
                if graph_radius(site) <= RADIUS:
                    sites.append(site)
    return tuple(sites)


def dijkstra() -> tuple[dict[Site, int], dict[Site, tuple[Site, ...]]]:
    dist: dict[Site, int] = {SEED: 0}
    path: dict[Site, tuple[Site, ...]] = {SEED: (SEED,)}
    heap: list[tuple[int, tuple[Site, ...], Site]] = [(0, (SEED,), SEED)]
    finalized: set[Site] = set()
    while heap:
        cost, current_path, site = heappop(heap)
        if site in finalized:
            continue
        finalized.add(site)
        for dest in neighbors(site):
            new_cost = cost + hop_cost(site, dest)
            new_path = current_path + (dest,)
            better_cost = dest not in dist or new_cost < dist[dest]
            better_path = dest in dist and new_cost == dist[dest] and new_path < path[dest]
            if better_cost or better_path:
                dist[dest] = new_cost
                path[dest] = new_path
                heappush(heap, (new_cost, new_path, dest))
    return dist, path


def path_costs(path: tuple[Site, ...]) -> tuple[int, ...]:
    return tuple(hop_cost(path[index], path[index + 1]) for index in range(len(path) - 1))


def shortest_paths(dist: dict[Site, int]) -> list[tuple[Site, ...]]:
    predecessors: dict[Site, list[Site]] = defaultdict(list)
    for site, cost in dist.items():
        for dest in neighbors(site):
            if dest in dist and dist[dest] == cost + hop_cost(site, dest):
                predecessors[dest].append(site)
    found: list[tuple[Site, ...]] = []

    def walk(node: Site, acc: list[Site]) -> None:
        if node == SEED:
            found.append(tuple(reversed(acc + [node])))
            return
        for pred in predecessors[node]:
            walk(pred, acc + [node])

    walk(TARGET, [])
    return found


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


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    sites = ball_sites()
    dist, best_path = dijkstra()
    path = best_path[TARGET]
    costs = path_costs(path)
    all_short = shortest_paths(dist)
    multisets = {tuple(sorted(path_costs(item))) for item in all_short}
    clauses = [hop_clause(path[i], path[i + 1]) for i in range(len(path) - 1)]
    pairs = [
        (inward_weight(path[i]), inward_weight(path[i + 1]))
        for i in range(len(path) - 1)
    ]

    print("external_scientific_inputs: none; exact six-neighbor hop-cost algebra")
    print("package_local_integrity_reads: proposed source note and live axiom memo")
    print("claim_boundary: displayed named hop-cost; no admissibility edit")
    print("lex_first_path:", path)
    print("hop_pairs:", pairs)
    print("hop_clauses:", clauses)
    print("hop_costs:", costs)
    print("orbit_cost_sum:", sum(costs))
    print("shortest_path_count:", len(all_short))
    print("common_multiset:", next(iter(multisets)) if len(multisets) == 1 else multisets)

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/NO_SHORTCUT_BODY_DIAGONAL_PATH_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file(),
    )
    checks.check(
        "one-seed-b6-domain",
        "the search domain is the 377-site radius-6 ball about one seed",
        SEED in sites
        and TARGET in sites
        and len(sites) == 377
        and len(STEPS) == 6
        and all(graph_radius(step) == 1 for step in STEPS),
    )
    checks.check(
        "inward-weights",
        "seed weight is 0 and the body-diagonal weight is 3",
        inward_weight(SEED) == 0 and inward_weight(TARGET) == 3,
    )
    checks.check(
        "thm1-lex-path",
        "the lex-first shortest path is the displayed six-step site list",
        path
        == (
            (0, 0, 0),
            (0, 0, 1),
            (0, 1, 1),
            (0, 1, 2),
            (0, 2, 2),
            (1, 2, 2),
            (2, 2, 2),
        ),
    )
    hop_steps = tuple(
        (
            path[index + 1][0] - path[index][0],
            path[index + 1][1] - path[index][1],
            path[index + 1][2] - path[index][2],
        )
        for index in range(len(path) - 1)
    )
    checks.check(
        "thm1-six-hops",
        "that path has six nearest-neighbor hops",
        len(path) == 7
        and len(hop_steps) == 6
        and all(step in STEPS for step in hop_steps),
    )
    checks.check(
        "thm1-hop-costs",
        "the six computed hop costs are 3,1,1,1,1,1",
        costs == (3, 1, 1, 1, 1, 1),
    )
    checks.check(
        "thm1-orbit-cost-sum",
        "the orbit-cost sum equals the Dijkstra arrival and equals 8",
        sum(costs) == dist[TARGET] == 8,
    )
    checks.check(
        "thm1-seed-exit-only-expensive",
        "the path uses one seed-exit and five ordinary hops",
        clauses.count("seed-exit") == 1
        and clauses.count("both-weights-1") == 0
        and clauses.count("support-drop") == 0
        and clauses.count("neither") == 5
        and pairs == [(0, 1), (1, 2), (2, 2), (2, 2), (2, 3), (3, 3)],
    )
    checks.check(
        "thm2-common-multiset",
        "every shortest path has hop-cost multiset {1,1,1,1,1,3}",
        len(all_short) == 72
        and multisets == {(1, 1, 1, 1, 1, 3)}
        and all(len(item) == 7 for item in all_short),
    )
    checks.check(
        "thm2-lex-is-shortest",
        "the displayed path is among the enumerated shortest paths and is lex-first",
        path in all_short and path == min(all_short),
    )
    axis_stay_path = (
        (0, 0, 0),
        (0, 0, 1),
        (0, 0, 2),
        (0, 1, 2),
        (0, 2, 2),
        (1, 2, 2),
        (2, 2, 2),
    )
    axis_stay_costs = path_costs(axis_stay_path)
    mutation_unit = tuple(1 for _ in costs)
    drop_hop = ((0, 1, 1), (0, 1, 0))
    drop_path = (
        (0, 0, 0),
        (0, 0, 1),
        (0, 1, 1),
        (0, 1, 0),
        (0, 2, 0),
        (0, 2, 1),
        (0, 2, 2),
        (1, 2, 2),
        (2, 2, 2),
    )
    drop_costs = path_costs(drop_path)
    checks.check(
        "mutation-unit-costs-fail",
        "replacing every hop by cost 1 does not recover the orbit-cost sum 8",
        sum(mutation_unit) != 8 and sum(mutation_unit) == 6,
    )
    checks.check(
        "mutation-axis-stay-fails",
        "the axis-extension word costs 10 and is not shortest",
        axis_stay_costs == (3, 3, 1, 1, 1, 1)
        and sum(axis_stay_costs) == 10
        and sum(axis_stay_costs) != dist[TARGET]
        and axis_stay_path not in all_short,
    )
    checks.check(
        "mutation-support-drop-priced",
        "a support-drop hop costs 3 under the named rule and 1 without that clause",
        hop_cost(*drop_hop) == 3
        and hop_cost_axis_skeleton(*drop_hop) == 1
        and hop_clause(*drop_hop) == "support-drop",
    )
    checks.check(
        "mutation-support-drop-path-fails",
        "a word that uses a support-drop hop is not shortest",
        drop_costs[2] == 3
        and sum(drop_costs) == 14
        and sum(drop_costs) != dist[TARGET]
        and drop_path not in all_short,
    )
    checks.check(
        "axiom-unedited",
        "the live Admissibility sentences are present and the named rule is absent",
        "There is one fixed nearest-neighbor admissibility rule" in axiom
        and "the probability distribution over the possibilities is" in axiom
        and "named hop-cost" not in axiom
        and "seed-exit" not in axiom
        and "support-drop" not in axiom
        and "support drop" not in axiom,
    )
    checks.check(
        "thm3-not-written-into-admissibility",
        "the note refuses to write the named rule into Admissibility",
        "Do not write `ν` into Admissibility" in note
        and "Displayed, not adopted" in note
        and "displayed, not adopted" in note
        and "hypothetical_axiom_status: \"no edit" in note,
    )
    checks.check(
        "no-l1-attachment",
        "the note refuses to attach L1",
        "Do not attach L1" in note
        and "Do not identify the named hop-cost with six-neighbor graph distance" in note,
    )
    checks.check(
        "claim-scope-contract",
        "the declared claim_scope matches the exhibited-path statement",
        'claim_scope: "A shortest 0→(2,2,2) path under the named support-drop hop-cost is exhibited. Displayed, not adopted."'
        in note,
    )
    checks.check(
        "forbidden-phrases",
        "the note omits the dispatch-forbidden phrases",
        all(token not in note for token in FORBIDDEN),
    )
    checks.check(
        "note-contains-path-and-costs",
        "the note records the lex path, the six costs, the sum, and the common multiset",
        "(0,0,0) → (0,0,1) → (0,1,1) → (0,1,2) → (0,2,2) → (1,2,2) → (2,2,2)"
        in note
        and "3,1,1,1,1,1" in note
        and "{1,1,1,1,1,3}" in note
        and "orbit-cost sum is `8`" in note,
    )
    checks.check(
        "note-names-support-drop-clause",
        "the note names the third clause as support drop and as a different rule",
        "|σ_w| < |σ_v|" in note
        and "support drop" in note
        and "different rule" in note,
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
