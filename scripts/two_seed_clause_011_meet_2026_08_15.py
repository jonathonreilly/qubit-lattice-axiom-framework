#!/usr/bin/env python3
"""Score two-seed meetings under the named (0,1,1) hop-cost.

One pair of Dijkstras on B_4(0)∪B_4((2,0,0)). No cache write. No axiom edit.
"""

from __future__ import annotations

import ast
import heapq
import math
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/TWO_SEED_CLAUSE_011_MEET_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/TWO_SEED_CLAUSE_011_MEET_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
CLAIM_SCOPE = (
    "Two-seed meetings under the named (0,1,1) hop-cost are "
    "scored vs ℓ¹. Displayed, not adopted."
)
NEIGH = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
S0 = (0, 0, 0)
S1 = (2, 0, 0)
FORBIDDEN_PARTS = (
    ("G_", "N"),
    ("1/", "r"),
    ("1/", "r^2"),
    ("Lattice-", "named"),
    ("not a ", "TOE"),
)
VAR_011_REPORTED = 0.01142337008814
VAR_L1_REPORTED = 0.00995038158264
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


def l1(v: tuple[int, int, int], seed: tuple[int, int, int] = S0) -> int:
    return abs(v[0] - seed[0]) + abs(v[1] - seed[1]) + abs(v[2] - seed[2])


def support_size(v: tuple[int, int, int], seed: tuple[int, int, int]) -> int:
    return int(v[0] != seed[0]) + int(v[1] != seed[1]) + int(v[2] != seed[2])


def l2(v: tuple[int, int, int], seed: tuple[int, int, int] = S0) -> float:
    dx = v[0] - seed[0]
    dy = v[1] - seed[1]
    dz = v[2] - seed[2]
    return math.sqrt(dx * dx + dy * dy + dz * dz)


def ball(center: tuple[int, int, int], radius: int) -> list[tuple[int, int, int]]:
    cx, cy, cz = center
    sites: list[tuple[int, int, int]] = []
    for x in range(cx - radius, cx + radius + 1):
        for y in range(cy - radius, cy + radius + 1):
            rem = radius - abs(x - cx) - abs(y - cy)
            for z in range(cz - rem, cz + rem + 1):
                sites.append((x, y, z))
    return sites


def clause_011_cost(
    v: tuple[int, int, int],
    w: tuple[int, int, int],
    seed: tuple[int, int, int],
) -> int:
    sigma_v = support_size(v, seed)
    sigma_w = support_size(w, seed)
    if (sigma_v == 1 and sigma_w == 1) or sigma_w < sigma_v:
        return 3
    return 1


def dijkstra_011(
    sites: set[tuple[int, int, int]],
    seed: tuple[int, int, int],
) -> dict[tuple[int, int, int], int]:
    global DIJKSTRA_CALLS
    DIJKSTRA_CALLS += 1
    dist: dict[tuple[int, int, int], int] = {seed: 0}
    heap: list[tuple[int, tuple[int, int, int]]] = [(0, seed)]
    seen: set[tuple[int, int, int]] = set()
    while heap:
        d, v = heapq.heappop(heap)
        if v in seen:
            continue
        seen.add(v)
        vx, vy, vz = v
        for dx, dy, dz in NEIGH:
            w = (vx + dx, vy + dy, vz + dz)
            if w not in sites:
                continue
            nd = d + clause_011_cost(v, w, seed)
            if nd < dist.get(w, 10**9):
                dist[w] = nd
                heapq.heappush(heap, (nd, w))
    return dist


def first_meetings(
    sites: list[tuple[int, int, int]],
    site_set: set[tuple[int, int, int]],
    t0: dict[tuple[int, int, int], int],
    t1: dict[tuple[int, int, int], int],
) -> list[tuple[int, int, int]]:
    meetings: list[tuple[int, int, int]] = []
    for v in sites:
        if t0[v] != t1[v]:
            continue
        vx, vy, vz = v
        earlier_both = False
        for dx, dy, dz in NEIGH:
            w = (vx + dx, vy + dy, vz + dz)
            if w not in site_set:
                continue
            if t0[w] < t0[v] and t1[w] < t1[v]:
                earlier_both = True
                break
        if not earlier_both:
            meetings.append(v)
    return meetings


def population_variance(values: list[float]) -> float:
    n = len(values)
    mean = math.fsum(values) / n
    return math.fsum((x - mean) ** 2 for x in values) / n


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
        "note claim_scope matches the displayed scoring statement",
        CLAIM_SCOPE in note.replace("\n", " "),
    )
    checks.check(
        "displayed-not-adopted",
        "the rule is displayed, not adopted",
        "Displayed, not adopted" in note or "displayed, not adopted" in note,
    )
    checks.check(
        "not-in-admissibility",
        "(0,1,1) is not written into Admissibility",
        "not written into Admissibility" in note,
    )
    checks.check(
        "not-attach-l1",
        "the displayed rule is not attached to L1",
        "not attached to L1" in note and "Do not attach L1" not in axiom,
    )
    checks.check(
        "uniqueness-not-claimed",
        "uniqueness among hop-costs is not claimed",
        "Uniqueness is not claimed" in note or "no uniqueness" in note.lower(),
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

    sites = sorted(set(ball(S0, 4)) | set(ball(S1, 4)))
    site_set = set(sites)
    t0 = dijkstra_011(site_set, S0)
    t1 = dijkstra_011(site_set, S1)
    mid_011 = [v for v in sites if t0[v] == t1[v]]
    meetings = first_meetings(sites, site_set, t0, t1)
    lex_first = min(meetings)
    meet_t = t0[lex_first]
    var_011 = population_variance([l2(v, S0) / t0[v] for v in mid_011])

    mid_l1 = [v for v in sites if l1(v, S0) == l1(v, S1)]
    var_l1 = population_variance([l2(v, S0) / l1(v, S0) for v in mid_l1])

    print(f"n_sites {len(sites)}")
    print(f"lex_first {lex_first}")
    print(f"meet_t {meet_t}")
    print(f"|M| {len(meetings)}")
    print(f"n_mid_011 {len(mid_011)}")
    print(f"n_mid_l1 {len(mid_l1)}")
    print(f"var_011 {var_011:.14f}")
    print(f"var_l1 {var_l1:.14f}")
    print(f"dijkstra_calls {DIJKSTRA_CALLS}")

    checks.check(
        "one-pair-dijkstra",
        "exactly one pair of Dijkstras ran",
        DIJKSTRA_CALLS == 2,
    )
    checks.check(
        "union-b4",
        "the union B_4(0)∪B_4((2,0,0)) has 195 sites",
        len(sites) == 195
        and all(l1(v, S0) <= 4 or l1(v, S1) <= 4 for v in sites),
    )
    checks.check(
        "reachable",
        "every site of the union is reached from both seeds",
        len(t0) == 195 and len(t1) == 195,
    )
    checks.check(
        "lex-first-meeting",
        "lex-first meeting site is (1,0,0) at t=1",
        lex_first == (1, 0, 0) and meet_t == 1 and t1[lex_first] == 1,
    )
    checks.check(
        "meeting-cardinality",
        "|M| = 1",
        meetings == [(1, 0, 0)],
    )
    checks.check(
        "matching-member-front",
        "first meeting stays the matching-member front (1,0,0)",
        meetings == [(1, 0, 0)] and "matching-member front" in note,
    )
    checks.check(
        "note-records-meeting",
        "note records the lex-first meeting site, time, and |M|",
        "(1,0,0)" in note and "t=1" in note and "|M|=1" in note,
    )
    checks.check(
        "var-011",
        "midplane population variance under (0,1,1) matches the reported value",
        abs(var_011 - VAR_011_REPORTED) < 5e-14,
    )
    checks.check(
        "var-l1",
        "midplane population variance under ℓ¹ matches the reported value",
        abs(var_l1 - VAR_L1_REPORTED) < 5e-14,
    )
    checks.check(
        "var-l1-smaller",
        "var(|v-s0|_2/t0) is strictly smaller under ℓ¹ than under (0,1,1)",
        var_l1 < var_011,
    )
    checks.check(
        "note-records-variances",
        "note records both midplane variances and the comparison",
        "0.01142337008814" in note
        and "0.00995038158264" in note
        and "var_ℓ¹ < var_(0,1,1)" in note,
    )
    checks.check(
        "seed-relative-clauses",
        "seed-exit is cheap; both-weights-1 and support drop cost 3",
        clause_011_cost(S0, (1, 0, 0), S0) == 1
        and clause_011_cost(S1, (1, 0, 0), S1) == 1
        and clause_011_cost((1, 1, 0), (1, 0, 0), S0) == 3
        and clause_011_cost((3, 1, 0), (3, 0, 0), S1) == 3
        and clause_011_cost((1, 0, 0), (1, 1, 0), S0) == 1
        and clause_011_cost((1, 0, 0), (2, 0, 0), S0) == 3,
    )
    checks.check(
        "axiom-untouched",
        "the axiom memo is an input only and still names the four axioms",
        "### Admissibility / Local Constraint" in axiom
        and "(0,1,1)_s(v→w)" not in axiom
        and "clause_011_cost" not in axiom,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
