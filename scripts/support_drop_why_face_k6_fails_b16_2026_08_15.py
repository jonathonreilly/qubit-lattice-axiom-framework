#!/usr/bin/env python3
"""Exhibit lex-first shortest walks to (12,0,0) and (6,6,0) under ν.

One origin Dijkstra on B_16(0). No cache write. No axiom edit.
"""

from __future__ import annotations

import ast
import heapq
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/SUPPORT_DROP_WHY_FACE_K6_FAILS_B16_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/SUPPORT_DROP_WHY_FACE_K6_FAILS_B16_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
CLAIM_SCOPE = (
    "Lex-first shortest paths to (12,0,0) and (6,6,0) under "
    "the named support-drop hop-cost on B_16(0) are named. "
    "Displayed, not adopted."
)
TARGET_AXIS = (12, 0, 0)
TARGET_FACE = (6, 6, 0)
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


def running_costs(costs: list[int]) -> list[int]:
    out: list[int] = []
    acc = 0
    for c in costs:
        acc += c
        out.append(acc)
    return out


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


def in_ball_neighbors(
    v: tuple[int, int, int],
    sites: set[tuple[int, int, int]],
) -> set[tuple[int, int, int]]:
    vx, vy, vz = v
    return {
        (vx + dx, vy + dy, vz + dz)
        for dx, dy, dz in NEIGH
        if (vx + dx, vy + dy, vz + dz) in sites
    }


def dijkstra_lex_first(
    sites: set[tuple[int, int, int]],
    targets: frozenset[tuple[int, int, int]],
) -> dict[tuple[int, int, int], tuple[int, tuple[tuple[int, int, int], ...]]]:
    global DIJKSTRA_CALLS
    DIJKSTRA_CALLS += 1
    origin = (0, 0, 0)
    heap: list[tuple[int, tuple[tuple[int, int, int], ...]]] = [(0, (origin,))]
    seen: set[tuple[int, int, int]] = set()
    found: dict[tuple[int, int, int], tuple[int, tuple[tuple[int, int, int], ...]]] = {}
    while heap and len(found) < len(targets):
        dist, path = heapq.heappop(heap)
        v = path[-1]
        if v in seen:
            continue
        seen.add(v)
        if v in targets:
            found[v] = (dist, path)
        vx, vy, vz = v
        for dx, dy, dz in NEIGH:
            w = (vx + dx, vy + dy, vz + dz)
            if w not in sites or w in seen:
                continue
            heapq.heappush(heap, (dist + nu_cost(v, w), path + (w,)))
    missing = targets - found.keys()
    if missing:
        raise RuntimeError(f"targets unreachable: {sorted(missing)}")
    return found


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
        "note claim_scope matches the named-paths statement",
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
    arrivals = dijkstra_lex_first(sites, frozenset({TARGET_AXIS, TARGET_FACE}))
    t1200, path_axis = arrivals[TARGET_AXIS]
    t660, path_face = arrivals[TARGET_FACE]
    costs_axis = hop_costs(path_axis)
    costs_face = hop_costs(path_face)
    run_axis = running_costs(costs_axis)
    run_face = running_costs(costs_face)
    path_axis_text = format_path(path_axis)
    path_face_text = format_path(path_face)
    cost_axis_text = format_costs(costs_axis)
    cost_face_text = format_costs(costs_face)
    run_axis_text = format_costs(run_axis)
    run_face_text = format_costs(run_face)

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
        (8, -1, 0),
        (9, -1, 0),
        (10, -1, 0),
        (11, -1, 0),
        (12, -1, 0),
        (12, 0, 0),
    )
    expected_face = (
        (0, 0, 0),
        (0, 1, 0),
        (1, 1, 0),
        (1, 2, 0),
        (1, 3, 0),
        (1, 4, 0),
        (1, 5, 0),
        (1, 6, 0),
        (2, 6, 0),
        (3, 6, 0),
        (4, 6, 0),
        (5, 6, 0),
        (6, 6, 0),
    )
    expected_axis_costs = [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3]
    expected_face_costs = [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
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
        (8, 1, 0),
        (9, 1, 0),
        (10, 1, 0),
        (11, 1, 0),
        (12, 1, 0),
        (12, 0, 0),
    )
    later_face = (
        (0, 0, 0),
        (1, 0, 0),
        (1, 1, 0),
        (1, 2, 0),
        (1, 3, 0),
        (1, 4, 0),
        (1, 5, 0),
        (1, 6, 0),
        (2, 6, 0),
        (3, 6, 0),
        (4, 6, 0),
        (5, 6, 0),
        (6, 6, 0),
    )
    axis_nbrs = in_ball_neighbors(TARGET_AXIS, sites)
    face_nbrs = in_ball_neighbors(TARGET_FACE, sites)
    reverse = (t1200 * t1200) * 72 > (t660 * t660) * 144

    print(f"n_sites {len(sites)}")
    print(f"t(12,0,0) {t1200}")
    print(f"t(6,6,0) {t660}")
    print(f"lex_first_1200 {path_axis_text}")
    print(f"hop_costs_1200 {cost_axis_text}")
    print(f"running_1200 {run_axis}")
    print(f"last_hop_1200 {path_axis[-2]} -> {path_axis[-1]} cost {costs_axis[-1]}")
    print(f"lex_first_660 {path_face_text}")
    print(f"hop_costs_660 {cost_face_text}")
    print(f"running_660 {run_face}")
    print(f"last_hop_660 {path_face[-2]} -> {path_face[-1]} cost {costs_face[-1]}")
    print(f"k6_reverse {t1200 * t1200}/144 > {t660 * t660}/72 is {reverse}")
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
        "t-660",
        "t(6,6,0) on B_16(0) equals 14",
        t660 == 14,
    )
    checks.check(
        "valid-walk-1200",
        "the axis walk is a nearest-neighbor walk in B_16(0) from 0 to (12,0,0)",
        path_axis[0] == (0, 0, 0)
        and path_axis[-1] == TARGET_AXIS
        and is_walk(path_axis, sites),
    )
    checks.check(
        "valid-walk-660",
        "the face walk is a nearest-neighbor walk in B_16(0) from 0 to (6,6,0)",
        path_face[0] == (0, 0, 0)
        and path_face[-1] == TARGET_FACE
        and is_walk(path_face, sites),
    )
    checks.check(
        "lex-first-path-1200",
        "the Dijkstra reconstruction is the named lex-first walk to (12,0,0)",
        path_axis == expected_axis,
    )
    checks.check(
        "lex-first-path-660",
        "the Dijkstra reconstruction is the named lex-first walk to (6,6,0)",
        path_face == expected_face,
    )
    checks.check(
        "hop-costs-1200",
        "axis hop-costs equal ν on successive sites and sum to 18",
        costs_axis == expected_axis_costs and sum(costs_axis) == 18 == t1200,
    )
    checks.check(
        "hop-costs-660",
        "face hop-costs equal ν on successive sites and sum to 14",
        costs_face == expected_face_costs and sum(costs_face) == 14 == t660,
    )
    checks.check(
        "last-hops-make-t",
        "last hops are support-drop cost 3 versus face cost 1",
        path_axis[-2] == (12, -1, 0)
        and path_axis[-1] == TARGET_AXIS
        and costs_axis[-1] == 3
        and run_axis[-2] == 15
        and run_axis[-1] == 18
        and path_face[-2] == (5, 6, 0)
        and path_face[-1] == TARGET_FACE
        and costs_face[-1] == 1
        and run_face[-1] == 14
        and nu_cost((12, -1, 0), (12, 0, 0)) == 3
        and nu_cost((5, 6, 0), (6, 6, 0)) == 1
        and l1((12, -1, 0)) == 13
        and (12, -1, 0) in sites,
    )
    checks.check(
        "axis-interior-last-step",
        "(12,0,0) has six in-ball neighbors, each of cost 3",
        axis_nbrs
        == {(11, 0, 0), (13, 0, 0), (12, -1, 0), (12, 1, 0), (12, 0, -1), (12, 0, 1)}
        and all(nu_cost(nbr, TARGET_AXIS) == 3 for nbr in axis_nbrs),
    )
    checks.check(
        "face-interior-last-step",
        "(6,6,0) has six in-ball neighbors; face-plane in-hops cost 1",
        face_nbrs
        == {(5, 6, 0), (7, 6, 0), (6, 5, 0), (6, 7, 0), (6, 6, -1), (6, 6, 1)}
        and nu_cost((5, 6, 0), TARGET_FACE) == 1
        and nu_cost((7, 6, 0), TARGET_FACE) == 1
        and nu_cost((6, 5, 0), TARGET_FACE) == 1
        and nu_cost((6, 7, 0), TARGET_FACE) == 1
        and nu_cost((6, 6, -1), TARGET_FACE) == 3
        and nu_cost((6, 6, 1), TARGET_FACE) == 3,
    )
    checks.check(
        "k6-reverse-fails",
        "t(12,0,0)^2 / 144 > t(6,6,0)^2 / 72 fails as a displayed bit",
        (not reverse)
        and t1200 * t1200 == 324
        and t660 * t660 == 196
        and 72 * 324 == 23328
        and 144 * 196 == 28224
        and 23328 < 28224,
    )
    checks.check(
        "lex-first-beats-later-shortest",
        "later cost-matching walks exist and are strictly lex-later",
        is_walk(later_axis, sites)
        and sum(hop_costs(later_axis)) == 18
        and path_axis < later_axis
        and is_walk(later_face, sites)
        and sum(hop_costs(later_face)) == 14
        and path_face < later_face,
    )
    checks.check(
        "note-records-paths",
        "note records both lex-first sites, hop-costs, running costs, and last hops",
        path_axis_text in note
        and path_face_text in note
        and cost_axis_text in note
        and cost_face_text in note
        and run_axis_text in note
        and run_face_text in note
        and "(12,-1,0) → (12,0,0)" in note
        and "(5,6,0) → (6,6,0)" in note
        and "t(12,0,0) = 18" in note
        and "t(6,6,0) = 14" in note
        and "23328" in note
        and "28224" in note,
    )
    checks.check(
        "not-leftover-of-the-no-bit",
        "the walks are not leftover of the no bit",
        "not leftover of the no bit" in note and (not reverse),
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
