#!/usr/bin/env python3
"""Exhibit lex-first shortest 0→(8,0,0) and 0→(4,4,4) walks under ν.

One origin Dijkstra on B_12(0). No cache write. No axiom edit.
"""

from __future__ import annotations

import ast
import heapq
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/SUPPORT_DROP_WHY_T800_EQ_T444_B12_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/SUPPORT_DROP_WHY_T800_EQ_T444_B12_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
CLAIM_SCOPE = (
    "Lex-first shortest paths to (8,0,0) and (4,4,4) under "
    "the named support-drop hop-cost on B_12(0) are named. "
    "Displayed, not adopted."
)
TARGET_800 = (8, 0, 0)
TARGET_444 = (4, 4, 4)
NEIGH = ((-1, 0, 0), (0, -1, 0), (0, 0, -1), (0, 0, 1), (0, 1, 0), (1, 0, 0))
FORBIDDEN_PARTS = (
    ("G_", "N"),
    ("1/", "r"),
    ("1/", "r^2"),
    ("Lattice-", "named"),
    ("not a ", "TOE"),
)
DIJKSTRA_CALLS = 0
Point = tuple[int, int, int]
PathT = tuple[Point, ...]


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


def l1(v: Point) -> int:
    return abs(v[0]) + abs(v[1]) + abs(v[2])


def support_size(v: Point) -> int:
    return int(v[0] != 0) + int(v[1] != 0) + int(v[2] != 0)


def ball(radius: int) -> set[Point]:
    sites: set[Point] = set()
    for x in range(-radius, radius + 1):
        for y in range(-radius, radius + 1):
            rem = radius - abs(x) - abs(y)
            for z in range(-rem, rem + 1):
                sites.add((x, y, z))
    return sites


def nu_cost(v: Point, w: Point) -> int:
    sigma_v = support_size(v)
    sigma_w = support_size(w)
    if sigma_v == 0 or (sigma_v == 1 and sigma_w == 1) or sigma_w < sigma_v:
        return 3
    return 1


def hop_costs(path: PathT) -> list[int]:
    return [nu_cost(a, b) for a, b in zip(path, path[1:])]


def running_costs(costs: list[int]) -> list[int]:
    running: list[int] = []
    acc = 0
    for cost in costs:
        acc += cost
        running.append(acc)
    return running


def format_path(path: PathT) -> str:
    return " → ".join(f"({v[0]},{v[1]},{v[2]})" for v in path)


def format_costs(costs: list[int]) -> str:
    return ", ".join(str(c) for c in costs)


def is_walk(path: PathT, sites: set[Point]) -> bool:
    if not path:
        return False
    for a, b in zip(path, path[1:]):
        if a not in sites or b not in sites:
            return False
        if l1((a[0] - b[0], a[1] - b[1], a[2] - b[2])) != 1:
            return False
    return True


def dijkstra_lex_first(
    sites: set[Point],
    targets: set[Point],
) -> dict[Point, tuple[int, PathT]]:
    global DIJKSTRA_CALLS
    DIJKSTRA_CALLS += 1
    origin = (0, 0, 0)
    heap: list[tuple[int, PathT]] = [(0, (origin,))]
    seen: set[Point] = set()
    found: dict[Point, tuple[int, PathT]] = {}
    while heap:
        dist, path = heapq.heappop(heap)
        v = path[-1]
        if v in seen:
            continue
        seen.add(v)
        if v in targets:
            found[v] = (dist, path)
            if len(found) == len(targets):
                return found
        vx, vy, vz = v
        for dx, dy, dz in NEIGH:
            w = (vx + dx, vy + dy, vz + dz)
            if w not in sites or w in seen:
                continue
            heapq.heappush(heap, (dist + nu_cost(v, w), path + (w,)))
    raise RuntimeError(f"targets {targets} not all reached")


def literal_audit_paths(source: str) -> tuple[str, ...] | None:
    module = ast.parse(source)
    for node in module.body:
        if not isinstance(node, ast.Assign):
            continue
        if not any(isinstance(t, ast.Name) and t.id == "AUDIT_INPUT_PATHS" for t in node.targets):
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
    note_path = ROOT / NOTE_REL
    axiom_path = ROOT / AXIOM_REL
    note = note_path.read_text(encoding="utf-8")
    axiom = axiom_path.read_text(encoding="utf-8")
    source = Path(__file__).read_text(encoding="utf-8")

    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print("cache_write: false")
    print(f"claim_scope: {CLAIM_SCOPE}")

    checks.check(
        "audit-input-paths",
        "declared inputs are the source note and the current axiom memo",
        AUDIT_INPUT_PATHS == (NOTE_REL, AXIOM_REL)
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    )
    checks.check(
        "audit-input-literal",
        "AUDIT_INPUT_PATHS is a static string-literal tuple",
        literal_audit_paths(source) == AUDIT_INPUT_PATHS,
    )
    checks.check(
        "claim-scope",
        "note claim_scope matches the named-path statement",
        CLAIM_SCOPE in note.replace("\n", " "),
    )
    checks.check(
        "displayed-not-adopted",
        "the rule is displayed, not adopted",
        "Displayed, not adopted" in note or "displayed, not adopted" in note,
    )
    checks.check(
        "not-in-admissibility",
        "ν is not written into Admissibility",
        "Do not write `ν` into Admissibility" in note,
    )
    checks.check(
        "not-attach-l1",
        "the displayed rule is not attached to L1",
        "Do not attach L1" in note,
    )
    checks.check(
        "uniqueness-not-claimed",
        "uniqueness among hop-costs is not claimed",
        "Uniqueness is not claimed" in note,
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
    )

    sites = ball(12)
    found = dijkstra_lex_first(sites, {TARGET_800, TARGET_444})
    t800, path800 = found[TARGET_800]
    t444, path444 = found[TARGET_444]
    costs800 = hop_costs(path800)
    costs444 = hop_costs(path444)
    run800 = running_costs(costs800)
    run444 = running_costs(costs444)
    path800_text = format_path(path800)
    path444_text = format_path(path444)
    cost800_text = format_costs(costs800)
    cost444_text = format_costs(costs444)
    run800_text = format_costs(run800)
    run444_text = format_costs(run444)
    equalizing_hop = (path800[-2], path800[-1])
    later_800 = (
        (0, 0, 0),
        (1, 0, 0),
        (1, 1, 0),
        (2, 1, 0),
        (3, 1, 0),
        (4, 1, 0),
        (5, 1, 0),
        (6, 1, 0),
        (7, 1, 0),
        (8, 1, 0),
        (8, 0, 0),
    )
    later_444 = (
        (0, 0, 0),
        (1, 0, 0),
        (1, 1, 0),
        (1, 1, 1),
        (2, 1, 1),
        (2, 2, 1),
        (2, 2, 2),
        (3, 2, 2),
        (3, 3, 2),
        (3, 3, 3),
        (4, 3, 3),
        (4, 4, 3),
        (4, 4, 4),
    )
    smaller_not_800 = (
        (0, 0, 0),
        (-1, 0, 0),
        (-1, -1, 0),
        (0, -1, 0),
        (1, -1, 0),
        (2, -1, 0),
        (3, -1, 0),
        (4, -1, 0),
        (5, -1, 0),
        (6, -1, 0),
        (7, -1, 0),
        (8, -1, 0),
        (8, 0, 0),
    )
    smaller_not_444 = (
        (0, 0, 0),
        (0, 0, -1),
        (0, 1, -1),
        (0, 1, 0),
        (0, 1, 1),
        (0, 1, 2),
        (0, 1, 3),
        (0, 1, 4),
        (0, 2, 4),
        (0, 3, 4),
        (0, 4, 4),
        (1, 4, 4),
        (2, 4, 4),
        (3, 4, 4),
        (4, 4, 4),
    )
    expected_800 = (
        (0, 0, 0),
        (0, -1, 0),
        (1, -1, 0),
        (2, -1, 0),
        (3, -1, 0),
        (4, -1, 0),
        (5, -1, 0),
        (6, -1, 0),
        (7, -1, 0),
        (8, -1, 0),
        (8, 0, 0),
    )
    expected_444 = (
        (0, 0, 0),
        (0, 0, 1),
        (0, 1, 1),
        (0, 1, 2),
        (0, 1, 3),
        (0, 1, 4),
        (0, 2, 4),
        (0, 3, 4),
        (0, 4, 4),
        (1, 4, 4),
        (2, 4, 4),
        (3, 4, 4),
        (4, 4, 4),
    )
    expected_costs_800 = [3, 1, 1, 1, 1, 1, 1, 1, 1, 3]
    expected_costs_444 = [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    expected_run_800 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 14]
    expected_run_444 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

    print(f"n_sites {len(sites)}")
    print(f"t(8,0,0) {t800}")
    print(f"t(4,4,4) {t444}")
    print(f"lex_first_path_800 {path800_text}")
    print(f"lex_first_path_444 {path444_text}")
    print(f"hop_costs_800 {cost800_text}")
    print(f"hop_costs_444 {cost444_text}")
    print(f"running_cost_800 {run800_text}")
    print(f"running_cost_444 {run444_text}")
    print(f"both_equal_14 {run800[-1] == 14 and run444[-1] == 14}")
    print(f"equalizing_hop {equalizing_hop[0]} -> {equalizing_hop[1]}")
    print(f"dijkstra_calls {DIJKSTRA_CALLS}")

    checks.check(
        "one-dijkstra",
        "exactly one Dijkstra ran",
        DIJKSTRA_CALLS == 1,
    )
    checks.check(
        "ball-b12",
        "B_12(0) has 2625 sites",
        len(sites) == 2625 and all(l1(v) <= 12 for v in sites),
    )
    checks.check(
        "t-800",
        "t(8,0,0) on B_12(0) equals 14",
        t800 == 14,
    )
    checks.check(
        "t-444",
        "t(4,4,4) on B_12(0) equals 14",
        t444 == 14,
    )
    checks.check(
        "both-equal-14",
        "both running-cost sequences terminate at 14",
        run800 == expected_run_800
        and run444 == expected_run_444
        and run800[-1] == 14
        and run444[-1] == 14,
    )
    checks.check(
        "valid-walk-800",
        "the axis walk is a nearest-neighbor walk in B_12(0) from 0 to (8,0,0)",
        path800[0] == (0, 0, 0) and path800[-1] == TARGET_800 and is_walk(path800, sites),
    )
    checks.check(
        "valid-walk-444",
        "the body-diagonal walk is a nearest-neighbor walk in B_12(0) from 0 to (4,4,4)",
        path444[0] == (0, 0, 0) and path444[-1] == TARGET_444 and is_walk(path444, sites),
    )
    checks.check(
        "hop-costs-800",
        "axis hop-costs equal ν on successive sites and sum to 14",
        costs800 == expected_costs_800 and sum(costs800) == 14,
    )
    checks.check(
        "hop-costs-444",
        "body-diagonal hop-costs equal ν on successive sites and sum to 14",
        costs444 == expected_costs_444 and sum(costs444) == 14,
    )
    checks.check(
        "shortest-both",
        "each walk cost equals the Dijkstra arrival, so both walks are shortest",
        sum(costs800) == t800 and sum(costs444) == t444,
    )
    checks.check(
        "lex-first-800",
        "the Dijkstra reconstruction is the named lex-first axis site sequence",
        path800 == expected_800,
    )
    checks.check(
        "lex-first-444",
        "the Dijkstra reconstruction is the named lex-first body-diagonal site sequence",
        path444 == expected_444,
    )
    checks.check(
        "equalizing-hop",
        "the hop that equalizes the arrivals is (8,-1,0) -> (8,0,0)",
        equalizing_hop == ((8, -1, 0), (8, 0, 0))
        and nu_cost((8, -1, 0), (8, 0, 0)) == 3
        and run800[8] == 11
        and run444[8] == 11
        and run800[-1] == run444[-1] == 14,
    )
    checks.check(
        "lex-first-beats-later-800",
        "a later cost-14 axis walk exists and is strictly lex-later",
        is_walk(later_800, sites)
        and sum(hop_costs(later_800)) == 14
        and path800 < later_800,
    )
    checks.check(
        "lex-first-beats-later-444",
        "a later cost-14 body-diagonal walk exists and is strictly lex-later",
        is_walk(later_444, sites)
        and sum(hop_costs(later_444)) == 14
        and path444 < later_444,
    )
    checks.check(
        "lex-smaller-is-not-shortest-800",
        "a lex-smaller axis walk that starts toward -x costs more than 14",
        is_walk(smaller_not_800, sites)
        and smaller_not_800 < path800
        and sum(hop_costs(smaller_not_800)) > 14,
    )
    checks.check(
        "lex-smaller-is-not-shortest-444",
        "a lex-smaller body-diagonal walk that starts toward -z costs more than 14",
        is_walk(smaller_not_444, sites)
        and smaller_not_444 < path444
        and sum(hop_costs(smaller_not_444)) > 14,
    )
    checks.check(
        "note-records-paths",
        "note records both lex-first sites and hop-costs",
        path800_text in note
        and path444_text in note
        and cost800_text in note
        and cost444_text in note,
    )
    checks.check(
        "note-records-running",
        "note records both running-cost sequences",
        run800_text in note and run444_text in note,
    )
    checks.check(
        "note-records-equalizing-hop",
        "note records the hop that equalizes the arrivals",
        "(8,-1,0) → (8,0,0)" in note
        and "hop that equalizes the arrivals" in note
        and "(3,4,4) → (4,4,4)" in note,
    )
    checks.check(
        "not-leftover-of-shared-shell",
        "the walks are not leftover of the shared-shell bit",
        "not leftover of the shared-shell bit" in note and t800 == t444 == 14,
    )
    checks.check(
        "seed-and-drop-clauses",
        "seed-exit and support-drop cost 3; support increase costs 1",
        nu_cost((0, 0, 0), (0, -1, 0)) == 3
        and nu_cost((0, 0, 0), (0, 0, 1)) == 3
        and nu_cost((0, -1, 0), (1, -1, 0)) == 1
        and nu_cost((0, 0, 1), (0, 1, 1)) == 1
        and nu_cost((8, -1, 0), (8, 0, 0)) == 3
        and nu_cost((3, 4, 4), (4, 4, 4)) == 1,
    )
    checks.check(
        "axiom-untouched",
        "the axiom memo is an input only and still names the four axioms",
        "### Admissibility / Local Constraint" in axiom
        and "ν(v→w)" not in axiom,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
