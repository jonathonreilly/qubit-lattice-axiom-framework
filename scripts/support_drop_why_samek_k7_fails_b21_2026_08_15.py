#!/usr/bin/env python3
"""Exhibit lex-first shortest walks to (7,0,0) and (7,7,7) under ν on B_21(0).

One origin Dijkstra. No cache write. No axiom edit.
"""

from __future__ import annotations

import ast
import heapq
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/SUPPORT_DROP_WHY_SAMEK_K7_FAILS_B21_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/SUPPORT_DROP_WHY_SAMEK_K7_FAILS_B21_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
CLAIM_SCOPE = (
    "Lex-first shortest paths to (7,0,0) and (7,7,7) under "
    "the named support-drop hop-cost on B_21(0) are named. "
    "Displayed, not adopted."
)
AXIS = (7, 0, 0)
BODY = (7, 7, 7)
NEIGH = ((-1, 0, 0), (0, -1, 0), (0, 0, -1), (0, 0, 1), (0, 1, 0), (1, 0, 0))
FORBIDDEN_PARTS = (
    ("G_", "N"),
    ("1/", "r"),
    ("1/", "r^2"),
    ("Lattice-", "named"),
    ("not a ", "TOE"),
)
T_AXIS_REP = 13
T_BODY_REP = 23
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


def alpha_cost(v: tuple[int, int, int], w: tuple[int, int, int]) -> int:
    sigma_v = support_size(v)
    sigma_w = support_size(w)
    if sigma_v == 0 or (sigma_v == 1 and sigma_w == 1):
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


def running_costs(costs: list[int]) -> list[int]:
    running: list[int] = []
    acc = 0
    for c in costs:
        acc += c
        running.append(acc)
    return running


def dijkstra_lex_first(
    sites: set[tuple[int, int, int]],
    targets: set[tuple[int, int, int]],
) -> dict[tuple[int, int, int], tuple[int, tuple[tuple[int, int, int], ...]]]:
    global DIJKSTRA_CALLS
    DIJKSTRA_CALLS += 1
    origin = (0, 0, 0)
    heap: list[tuple[int, tuple[tuple[int, int, int], ...]]] = [(0, (origin,))]
    seen: set[tuple[int, int, int]] = set()
    found: dict[tuple[int, int, int], tuple[int, tuple[tuple[int, int, int], ...]]] = {}
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
    missing = targets - set(found)
    raise RuntimeError(f"targets unreachable: {missing}")


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
        "Do not attach L1" in note and "Do not attach L1" not in axiom,
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

    sites = ball(21)
    nonzero = [v for v in sites if v != (0, 0, 0)]
    found = dijkstra_lex_first(sites, {AXIS, BODY})
    t700, path_axis = found[AXIS]
    t777, path_body = found[BODY]
    costs_axis = hop_costs(path_axis)
    costs_body = hop_costs(path_body)
    running_axis = running_costs(costs_axis)
    running_body = running_costs(costs_body)
    path_axis_text = format_path(path_axis)
    path_body_text = format_path(path_body)
    cost_axis_text = format_costs(costs_axis)
    cost_body_text = format_costs(costs_body)
    running_axis_text = format_costs(running_axis)
    running_body_text = format_costs(running_body)
    reverse = 3 * t700 * t700 > t777 * t777

    later_axis = (
        (0, 0, 0),
        (1, 0, 0),
        (1, 1, 0),
        (2, 1, 0),
        (3, 1, 0),
        (4, 1, 0),
        (5, 1, 0),
        (6, 1, 0),
        (7, 1, 0),
        (7, 0, 0),
    )
    later_body = (
        (0, 0, 0),
        (1, 0, 0),
        (1, 1, 0),
        (1, 1, 1),
        (2, 1, 1),
        (3, 1, 1),
        (4, 1, 1),
        (5, 1, 1),
        (6, 1, 1),
        (7, 1, 1),
        (7, 2, 1),
        (7, 3, 1),
        (7, 4, 1),
        (7, 5, 1),
        (7, 6, 1),
        (7, 7, 1),
        (7, 7, 2),
        (7, 7, 3),
        (7, 7, 4),
        (7, 7, 5),
        (7, 7, 6),
        (7, 7, 7),
    )
    smaller_not_shortest_axis = (
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
        (7, 0, 0),
    )
    expected_axis = (
        (0, 0, 0),
        (0, -1, 0),
        (1, -1, 0),
        (2, -1, 0),
        (3, -1, 0),
        (4, -1, 0),
        (5, -1, 0),
        (6, -1, 0),
        (7, -1, 0),
        (7, 0, 0),
    )
    expected_body = (
        (0, 0, 0),
        (0, 0, 1),
        (0, 1, 1),
        (0, 1, 2),
        (0, 1, 3),
        (0, 1, 4),
        (0, 1, 5),
        (0, 1, 6),
        (0, 1, 7),
        (0, 2, 7),
        (0, 3, 7),
        (0, 4, 7),
        (0, 5, 7),
        (0, 6, 7),
        (0, 7, 7),
        (1, 7, 7),
        (2, 7, 7),
        (3, 7, 7),
        (4, 7, 7),
        (5, 7, 7),
        (6, 7, 7),
        (7, 7, 7),
    )
    expected_axis_costs = [3] + [1] * 7 + [3]
    expected_body_costs = [3] + [1] * 20
    expected_axis_running = [3, 4, 5, 6, 7, 8, 9, 10, 13]
    expected_body_running = list(range(3, 24))

    print(f"n_sites {len(sites)}")
    print(f"t(7,0,0) {t700}")
    print(f"t(7,7,7) {t777}")
    print(f"lex_first_axis {path_axis_text}")
    print(f"lex_first_body {path_body_text}")
    print(f"hop_costs_axis {cost_axis_text}")
    print(f"hop_costs_body {cost_body_text}")
    print(f"running_cost_axis {running_axis}")
    print(f"running_cost_body {running_body}")
    print(f"t(7,0,0)^2/49 {t700 * t700}/49")
    print(f"t(7,7,7)^2/147 {t777 * t777}/147")
    print(f"3t_axis^2 {3 * t700 * t700}")
    print(f"t_body^2 {t777 * t777}")
    print(f"reverse {reverse}")
    print(f"dijkstra_calls {DIJKSTRA_CALLS}")

    checks.check(
        "one-dijkstra",
        "exactly one Dijkstra ran",
        DIJKSTRA_CALLS == 1,
    )
    checks.check(
        "ball-b21",
        "B_21(0) has 13287 sites and 13286 nonzero sites",
        len(sites) == 13287 and len(nonzero) == 13286 and all(l1(v) <= 21 for v in sites),
    )
    checks.check(
        "t-700-777",
        f"t(7,0,0)={T_AXIS_REP} and t(7,7,7)={T_BODY_REP}",
        t700 == T_AXIS_REP and t777 == T_BODY_REP,
    )
    checks.check(
        "valid-walks",
        "the exhibited walks are nearest-neighbor walks in B_21(0) from 0 to the two sites",
        path_axis[0] == (0, 0, 0)
        and path_axis[-1] == AXIS
        and path_body[0] == (0, 0, 0)
        and path_body[-1] == BODY
        and is_walk(path_axis, sites)
        and is_walk(path_body, sites),
    )
    checks.check(
        "hop-costs-match",
        "recorded hop-costs equal ν on successive sites and sum to the arrivals",
        costs_axis == expected_axis_costs
        and costs_body == expected_body_costs
        and sum(costs_axis) == 13
        and sum(costs_body) == 23,
    )
    checks.check(
        "running-cost",
        "running costs are the partial sums of the hop-costs",
        running_axis == expected_axis_running and running_body == expected_body_running,
    )
    checks.check(
        "shortest",
        "each walk cost equals the Dijkstra arrival, so each walk is shortest",
        sum(costs_axis) == t700 and sum(costs_body) == t777,
    )
    checks.check(
        "lex-first-paths",
        "the Dijkstra reconstructions are the named lex-first site sequences",
        path_axis == expected_axis and path_body == expected_body,
    )
    checks.check(
        "lex-first-beats-later-shortest",
        "later cost-matching walks exist and are strictly lex-later",
        is_walk(later_axis, sites)
        and is_walk(later_body, sites)
        and sum(hop_costs(later_axis)) == 13
        and sum(hop_costs(later_body)) == 23
        and path_axis < later_axis
        and path_body < later_body,
    )
    checks.check(
        "lex-smaller-is-not-shortest",
        "a lex-smaller axis walk that starts toward -x costs more than 13",
        is_walk(smaller_not_shortest_axis, sites)
        and smaller_not_shortest_axis < path_axis
        and sum(hop_costs(smaller_not_shortest_axis)) > 13,
    )
    checks.check(
        "reverse-k7",
        "t(7,0,0)^2/49 > t(7,7,7)^2/147 is false",
        (not reverse)
        and 3 * t700 * t700 == 507
        and t777 * t777 == 529
        and "507 > 529" in note
        and "does not hold" in note,
    )
    checks.check(
        "note-records-paths",
        "note records the lex-first sites, hop-costs, and running costs",
        path_axis_text in note
        and path_body_text in note
        and cost_axis_text in note
        and cost_body_text in note
        and running_axis_text in note
        and running_body_text in note,
    )
    checks.check(
        "note-records-times",
        "note records the two computed arrivals",
        "`13`" in note
        and "`23`" in note
        and "`(7,0,0)`" in note
        and "`(7,7,7)`" in note,
    )
    checks.check(
        "not-leftover-of-the-no-bit",
        "the walks are not leftover of the no bit",
        "not leftover of the no bit" in note
        and (not reverse)
        and path_axis != path_body,
    )
    checks.check(
        "not-leftover-of-alpha",
        "α cannot price the support-drop hop (7,-1,0)→(7,0,0)",
        nu_cost((7, -1, 0), (7, 0, 0)) == 3
        and alpha_cost((7, -1, 0), (7, 0, 0)) == 1
        and "cannot price support drop" in note,
    )
    checks.check(
        "seed-and-axis-clauses",
        "seed-exit and support-drop cost 3; support increase costs 1",
        nu_cost((0, 0, 0), (0, -1, 0)) == 3
        and nu_cost((0, -1, 0), (1, -1, 0)) == 1
        and nu_cost((6, -1, 0), (7, -1, 0)) == 1
        and nu_cost((7, -1, 0), (7, 0, 0)) == 3
        and nu_cost((0, 0, 0), (0, 0, 1)) == 3
        and nu_cost((0, 0, 1), (0, 1, 1)) == 1
        and nu_cost((0, 7, 7), (1, 7, 7)) == 1
        and all(c == 1 for c in costs_body[1:]),
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
