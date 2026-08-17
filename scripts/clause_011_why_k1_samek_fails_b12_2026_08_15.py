#!/usr/bin/env python3
"""Exact checks for the named (0,1,1) hop-cost on B_12(0).

One Dijkstra from the origin names t(1,0,0), t(1,1,1), and the lex-first
shortest paths. The same-k reverse comparison is displayed, not adopted.
No cache or axiom surface is written.
"""

from __future__ import annotations

from collections import deque
from heapq import heappop, heappush
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/CLAUSE_011_WHY_K1_SAMEK_FAILS_B12_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/CLAUSE_011_WHY_K1_SAMEK_FAILS_B12_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Point = tuple[int, int, int]
ORIGIN: Point = (0, 0, 0)
AXIS: Point = (1, 0, 0)
DIAG: Point = (1, 1, 1)
RADIUS = 12
SHIFTS: tuple[Point, ...] = (
    (-1, 0, 0),
    (0, -1, 0),
    (0, 0, -1),
    (0, 0, 1),
    (0, 1, 0),
    (1, 0, 0),
)
CLAIM_SCOPE = (
    "Lex-first shortest paths to (1,0,0) and (1,1,1) under the named "
    "(0,1,1) hop-cost on B_12(0) are named. Displayed, not adopted."
)
FORBIDDEN = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE")


def normalize(text: str) -> str:
    return " ".join(text.split())


def in_ball(point: Point) -> bool:
    return max(abs(point[0]), abs(point[1]), abs(point[2])) <= RADIUS


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


class DijkstraOnce:
    def __init__(self) -> None:
        self.calls = 0

    def distances(self, source: Point) -> dict[Point, int]:
        self.calls += 1
        dist = {source: 0}
        heap: list[tuple[int, Point]] = [(0, source)]
        seen: set[Point] = set()
        while heap:
            cost, site = heappop(heap)
            if site in seen:
                continue
            seen.add(site)
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


def shortest_path_count(dist: dict[Point, int], target: Point) -> int:
    allowed = on_shortest_paths(dist, target)

    def walk(site: Point) -> int:
        if site == target:
            return 1
        return sum(
            walk(nxt)
            for nxt in neighbors(site)
            if nxt in allowed and dist[nxt] == dist[site] + hop_cost(site, nxt)
        )

    return walk(ORIGIN)


def reverse_left_right(axis_t: int, diag_t: int) -> tuple[int, int, bool]:
    left = axis_t * axis_t
    right = (diag_t * diag_t) // 3
    return left, right, left > right


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


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
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

    ball_ok = (
        in_ball(ORIGIN)
        and in_ball(AXIS)
        and in_ball(DIAG)
        and in_ball((4, 4, 4))
        and in_ball((12, 0, 0))
        and in_ball((-12, -12, -12))
        and not in_ball((13, 0, 0))
        and not in_ball((0, 0, -13))
    )
    checks.check(
        "b12-domain",
        "named sites lie in the closed max-norm ball B_12(0) and radius 13 is excluded",
        ball_ok,
    )

    cost_table = (
        (ORIGIN, AXIS, 1),
        (AXIS, (2, 0, 0), 3),
        (AXIS, (1, 1, 0), 1),
        ((1, 1, 0), AXIS, 3),
        ((1, 1, 0), DIAG, 1),
        (AXIS, ORIGIN, 3),
    )
    checks.check(
        "hop-cost-rule",
        "cost is 3 iff both support weights are 1 or the hop drops support, else 1",
        all(hop_cost(src, dst) == value for src, dst, value in cost_table),
        [(src, dst, hop_cost(src, dst), value) for src, dst, value in cost_table],
    )

    seed_costs = tuple(hop_cost(ORIGIN, nxt) for nxt in neighbors(ORIGIN))
    checks.check(
        "cheap-seed-exit",
        "every origin-adjacent hop has cost 1",
        seed_costs == (1, 1, 1, 1, 1, 1) and len(neighbors(ORIGIN)) == 6,
        seed_costs,
    )

    search = DijkstraOnce()
    dist = search.distances(ORIGIN)
    checks.check(
        "one-dijkstra",
        "a single Dijkstra from the origin is executed",
        search.calls == 1 and ORIGIN in dist and AXIS in dist and DIAG in dist,
        search.calls,
    )

    t100 = dist[AXIS]
    t111 = dist[DIAG]
    checks.check("t-100", "t(1,0,0)=1", t100 == 1, t100)
    checks.check("t-111", "t(1,1,1)=3", t111 == 3, t111)

    path100 = lex_first_path(dist, AXIS)
    path111 = lex_first_path(dist, DIAG)
    checks.check(
        "lex-path-100",
        "the lex-first shortest path to (1,0,0) is the single seed-exit hop",
        path100 == (ORIGIN, AXIS),
        path100,
    )
    checks.check(
        "lex-path-111",
        "the lex-first shortest path to (1,1,1) is (0,0,0)->(0,0,1)->(0,1,1)->(1,1,1)",
        path111 == (ORIGIN, (0, 0, 1), (0, 1, 1), DIAG),
        path111,
    )

    n111 = shortest_path_count(dist, DIAG)
    checks.check(
        "uniqueness-not-required",
        "six shortest paths reach (1,1,1); the residual names the lex-first one only",
        n111 == 6 and shortest_path_count(dist, AXIS) == 1,
        n111,
    )

    left1, right1, holds1 = reverse_left_right(t100, t111)
    checks.check(
        "k1-reverse-fails",
        "t(1,0,0)^2 / 1 > t(1,1,1)^2 / 3 fails because 1 > 3 is false",
        left1 == 1 and right1 == 3 and holds1 is False,
        (left1, right1, holds1),
    )

    later = []
    for k in (2, 3, 4):
        later.append(reverse_left_right(dist[(k, 0, 0)], dist[(k, k, k)]))
    checks.check(
        "k234-reverse-holds",
        "the same displayed comparison holds at k=2,3,4",
        later == [(16, 12, True), (49, 27, True), (64, 48, True)],
        later,
    )

    hop100 = hop_cost(path100[0], path100[1])
    hop111 = hop_cost(path111[0], path111[1])
    checks.check(
        "first-hop-costs",
        "both lex-first first hops have cost 1",
        hop100 == 1 and hop111 == 1 and path111[1] == (0, 0, 1),
        (hop100, hop111, path100[1], path111[1]),
    )

    t400 = dist[(4, 0, 0)]
    checks.check(
        "l1-not-attached",
        "t(4,0,0)=8 is not the taxicab length 4, so L1 is not attached",
        t400 == 8 and t400 != 4 and dist[(4, 4, 4)] == 12,
        t400,
    )

    required = (
        CLAIM_SCOPE,
        "t(1,0,0)=1",
        "t(1,1,1)=3",
        "(0,0,0)->(1,0,0)",
        "(0,0,0)->(0,0,1)->(0,1,1)->(1,1,1)",
        "t(1,0,0)^2 / 1 > t(1,1,1)^2 / 3",
        "Displayed, not adopted",
        "Do not write (0,1,1) into Admissibility",
        "Do not attach L1",
        "cheap seed-exit",
        "actual_current_surface_status: bounded-support",
        "target_claim_type: bounded_theorem",
        'hypothetical_axiom_status: "no edit"',
        "audit_required_before_effective_retained: true",
        "bare_retained_allowed: false",
        "authors no audit verdict",
        "FAIL / DO NOT SHIP",
        "**Type:** bounded_theorem",
    )
    checks.check(
        "note-contract",
        "the note names the lex-first residual, displays the reverse, and keeps the axiom unedited",
        all(phrase in note for phrase in required),
        [phrase for phrase in required if phrase not in note],
    )
    checks.check(
        "claim-scope-field",
        "YAML claim_scope matches the dispatch sentence",
        f'claim_scope: "{CLAIM_SCOPE}"' in note,
    )
    checks.check(
        "not-in-admissibility",
        "the current Admissibility wording does not contain the (0,1,1) hop-cost",
        "both weights 1 or support drop" not in axiom
        and "named (0,1,1) hop-cost" not in axiom
        and "There is one fixed nearest-neighbor admissibility rule" in axiom_n,
    )
    checks.check(
        "displayed-not-adopted",
        "the note refuses adoption into Admissibility and refuses an L1 attachment",
        "Do not write (0,1,1) into Admissibility" in note
        and "Do not attach L1" in note
        and "displayed, not adopted" in note.lower()
        and "new axiom" not in note.lower(),
    )

    checks.check(
        "forbidden-tokens",
        "the note omits the dispatch-forbidden tokens",
        all(token not in note for token in FORBIDDEN),
        [token for token in FORBIDDEN if token in note],
    )
    checks.check(
        "no-cache-surface",
        "the runner declares no cache write and the note names no cache artifact",
        "cache_write: false" not in note
        and "runner-cache" not in note
        and "citation" not in note.lower(),
    )

    print("per_element: named hops, support weights, and first-hop costs are exact")
    print("per_site: t values and lex-first paths are read from one origin Dijkstra on B_12(0)")
    print("per_mode: checked and not executed — no spectral claim")
    print("per_block: k=1 reverse is displayed; k=2,3,4 are the comparison block")
    print("lattice_wide: checked and not executed — B_12(0) only; no axiom edit")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
