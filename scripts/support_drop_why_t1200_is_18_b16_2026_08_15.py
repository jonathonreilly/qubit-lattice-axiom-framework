#!/usr/bin/env python3
"""Exhibit the lex-first shortest 0→(12,0,0) walk under ν on B_16(0).

One origin Dijkstra. No cache write. No axiom edit.
"""

from __future__ import annotations

import ast
import heapq
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/SUPPORT_DROP_WHY_T1200_IS_18_B16_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/SUPPORT_DROP_WHY_T1200_IS_18_B16_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
CLAIM_SCOPE = (
    "A lex-first shortest path to (12,0,0) under the named support-drop "
    "hop-cost on B_16(0) is named. Displayed, not adopted."
)
TARGET = (12, 0, 0)
NEIGH = ((-1, 0, 0), (0, -1, 0), (0, 0, -1), (0, 0, 1), (0, 1, 0), (1, 0, 0))
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

    def check(self, label: str, statement: str, condition: bool) -> None:
        result = bool(condition)
        self.passed += int(result)
        self.failed += int(not result)
        print(f"{'PASS' if result else 'FAIL'}: {label} {statement}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def l1(v: tuple[int, int, int]) -> int:
    return abs(v[0]) + abs(v[1]) + abs(v[2])


def support_size(v: tuple[int, int, int]) -> int:
    return int(v[0] != 0) + int(v[1] != 0) + int(v[2] != 0)


def ball(radius: int) -> set[tuple[int, int, int]]:
    sites: set[tuple[int, int, int]] = set()
    for x in range(-radius, radius + 1):
        for y in range(-radius, radius + 1):
            rem = radius - abs(x) - abs(y)
            for z in range(-rem, rem + 1):
                sites.add((x, y, z))
    return sites


def nu_cost(v: tuple[int, int, int], w: tuple[int, int, int]) -> int:
    sigma_v = support_size(v)
    sigma_w = support_size(w)
    if sigma_v == 0 or (sigma_v == 1 and sigma_w == 1) or sigma_w < sigma_v:
        return 3
    return 1


def hop_costs(path: tuple[tuple[int, int, int], ...]) -> list[int]:
    return [nu_cost(a, b) for a, b in zip(path, path[1:])]


def format_path(path: tuple[tuple[int, int, int], ...]) -> str:
    return " → ".join(f"({v[0]},{v[1]},{v[2]})" for v in path)


def format_costs(costs: list[int]) -> str:
    return ", ".join(str(c) for c in costs)


def is_walk(path: tuple[tuple[int, int, int], ...], sites: set[tuple[int, int, int]]) -> bool:
    if not path:
        return False
    for a, b in zip(path, path[1:]):
        if a not in sites or b not in sites:
            return False
        if l1((a[0] - b[0], a[1] - b[1], a[2] - b[2])) != 1:
            return False
    return True


def first_site_outside_b12(
    path: tuple[tuple[int, int, int], ...],
) -> tuple[int, int, int] | None:
    for site in path:
        if l1(site) > 12:
            return site
    return None


def dijkstra_lex_first(
    sites: set[tuple[int, int, int]],
    target: tuple[int, int, int],
) -> tuple[int, tuple[tuple[int, int, int], ...]]:
    global DIJKSTRA_CALLS
    DIJKSTRA_CALLS += 1
    origin = (0, 0, 0)
    start_path = (origin,)
    heap: list[tuple[int, tuple[tuple[int, int, int], ...]]] = [(0, start_path)]
    seen: set[tuple[int, int, int]] = set()
    while heap:
        dist, path = heapq.heappop(heap)
        v = path[-1]
        if v in seen:
            continue
        seen.add(v)
        if v == target:
            return dist, path
        vx, vy, vz = v
        for dx, dy, dz in NEIGH:
            w = (vx + dx, vy + dy, vz + dz)
            if w not in sites or w in seen:
                continue
            heapq.heappush(heap, (dist + nu_cost(v, w), path + (w,)))
    raise RuntimeError(f"target {target} unreachable")


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

    sites = ball(16)
    t1200, path = dijkstra_lex_first(sites, TARGET)
    costs = hop_costs(path)
    path_text = format_path(path)
    cost_text = format_costs(costs)
    exit_site = first_site_outside_b12(path)
    later_shortest = (
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
        (9, 1, 0),
        (10, 1, 0),
        (11, 1, 0),
        (12, 1, 0),
        (12, 0, 0),
    )
    smaller_not_shortest = (
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
        (9, -1, 0),
        (10, -1, 0),
        (11, -1, 0),
        (12, -1, 0),
        (12, 0, 0),
    )
    expected_path = (
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
        (9, -1, 0),
        (10, -1, 0),
        (11, -1, 0),
        (12, -1, 0),
        (12, 0, 0),
    )
    expected_costs = [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3]
    running = []
    acc = 0
    for c in costs:
        acc += c
        running.append(acc)

    print(f"n_sites {len(sites)}")
    print(f"t(12,0,0) {t1200}")
    print(f"lex_first_path {path_text}")
    print(f"hop_costs {cost_text}")
    print(f"running_cost {running}")
    print(f"hop_sum {sum(costs)}")
    print(f"first_site_l1_gt_12 {exit_site}")
    print(f"first_exit_hop {(11, -1, 0)} -> {(12, -1, 0)}")
    print(f"dijkstra_calls {DIJKSTRA_CALLS}")

    checks.check(
        "one-dijkstra",
        "exactly one Dijkstra ran",
        DIJKSTRA_CALLS == 1,
    )
    checks.check(
        "ball-b16",
        "B_16(0) has 6017 sites",
        len(sites) == 6017 and all(l1(v) <= 16 for v in sites),
    )
    checks.check(
        "t-1200",
        "t(12,0,0) on B_16(0) equals 18",
        t1200 == 18,
    )
    checks.check(
        "valid-walk",
        "the exhibited walk is a nearest-neighbor walk in B_16(0) from 0 to (12,0,0)",
        path[0] == (0, 0, 0) and path[-1] == TARGET and is_walk(path, sites),
    )
    checks.check(
        "hop-costs-match",
        "recorded hop-costs equal ν on successive sites and sum to 18",
        costs == expected_costs and sum(costs) == 18,
    )
    checks.check(
        "shortest",
        "the walk cost equals the Dijkstra arrival, so the walk is shortest",
        sum(costs) == t1200,
    )
    checks.check(
        "lex-first-path",
        "the Dijkstra reconstruction is the named lex-first site sequence",
        path == expected_path,
    )
    checks.check(
        "first-site-outside-b12",
        "the first site with |v|_1 > 12 is (12,-1,0)",
        exit_site == (12, -1, 0)
        and l1((12, -1, 0)) == 13
        and all(l1(v) <= 12 for v in path[: path.index((12, -1, 0))]),
    )
    checks.check(
        "lex-first-beats-later-shortest",
        "a later cost-18 walk exists and is strictly lex-later",
        is_walk(later_shortest, sites)
        and sum(hop_costs(later_shortest)) == 18
        and path < later_shortest,
    )
    checks.check(
        "lex-smaller-is-not-shortest",
        "a lex-smaller walk that starts toward -x costs more than 18",
        is_walk(smaller_not_shortest, sites)
        and smaller_not_shortest < path
        and sum(hop_costs(smaller_not_shortest)) > 18,
    )
    checks.check(
        "note-records-path",
        "note records the lex-first sites and hop-costs",
        path_text in note and cost_text in note,
    )
    checks.check(
        "note-records-exit",
        "note records the first site outside B_12 and the leaving hop",
        "(12,-1,0)" in note
        and "|v|_1 = 13" in note
        and "(11,-1,0) → (12,-1,0)" in note,
    )
    checks.check(
        "not-leftover-of-the-two-times",
        "the walk is not leftover of the two times",
        "not leftover of the two times" in note and t1200 == 18,
    )
    checks.check(
        "seed-and-axis-clauses",
        "seed-exit and support-drop cost 3; support increase costs 1",
        nu_cost((0, 0, 0), (0, -1, 0)) == 3
        and nu_cost((0, -1, 0), (1, -1, 0)) == 1
        and nu_cost((1, -1, 0), (2, -1, 0)) == 1
        and nu_cost((12, -1, 0), (12, 0, 0)) == 3
        and nu_cost((11, 0, 0), (12, 0, 0)) == 3,
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
