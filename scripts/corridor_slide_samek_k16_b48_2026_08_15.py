#!/usr/bin/env python3
"""Score same-k reverse at k=16 under μ on B_48(0).

One origin Dijkstra. No cache write. No axiom edit.
"""

from __future__ import annotations

import ast
import heapq
from pathlib import Path


AUDIT_TIMEOUT_SEC = 180
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/CORRIDOR_SLIDE_SAMEK_K16_B48_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/CORRIDOR_SLIDE_SAMEK_K16_B48_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
CLAIM_SCOPE = (
    "Same-k reverse at k=16 under the named "
    "corridor-slide hop-cost on B_48(0) is reported. "
    "Displayed, not adopted."
)
NEIGH = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
FORBIDDEN_PARTS = (
    ("G_", "N"),
    ("1/", "r"),
    ("1/", "r^2"),
    ("Lattice-", "named"),
    ("not a ", "TOE"),
)
T_AXIS_REP = 26
T_BODY_REP = 50
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


def least_nonzero_abs(v: tuple[int, int, int]) -> int | None:
    nonzero = [abs(c) for c in v if c != 0]
    if not nonzero:
        return None
    return min(nonzero)


def ball(radius: int) -> list[tuple[int, int, int]]:
    sites: list[tuple[int, int, int]] = []
    for x in range(-radius, radius + 1):
        for y in range(-radius, radius + 1):
            rem = radius - abs(x) - abs(y)
            for z in range(-rem, rem + 1):
                sites.append((x, y, z))
    return sites


def nu_cost(v: tuple[int, int, int], w: tuple[int, int, int]) -> int:
    sigma_v = support_size(v)
    sigma_w = support_size(w)
    if sigma_v == 0 or (sigma_v == 1 and sigma_w == 1) or sigma_w < sigma_v:
        return 3
    return 1


def mu_cost(v: tuple[int, int, int], w: tuple[int, int, int]) -> int:
    if nu_cost(v, w) == 3:
        return 3
    if support_size(v) == 2 and support_size(w) == 2 and least_nonzero_abs(w) == 1:
        return 3
    return 1


def dijkstra_mu(sites: list[tuple[int, int, int]]) -> dict[tuple[int, int, int], int]:
    global DIJKSTRA_CALLS
    DIJKSTRA_CALLS += 1
    site_set = set(sites)
    dist: dict[tuple[int, int, int], int] = {(0, 0, 0): 0}
    heap: list[tuple[int, tuple[int, int, int]]] = [(0, (0, 0, 0))]
    seen: set[tuple[int, int, int]] = set()
    while heap:
        d, v = heapq.heappop(heap)
        if v in seen:
            continue
        seen.add(v)
        vx, vy, vz = v
        for dx, dy, dz in NEIGH:
            w = (vx + dx, vy + dy, vz + dz)
            if w not in site_set:
                continue
            nd = d + mu_cost(v, w)
            if nd < dist.get(w, 10**9):
                dist[w] = nd
                heapq.heappush(heap, (nd, w))
    return dist


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
        "μ is not written into Admissibility",
        "Do not write `μ` into Admissibility" in note,
    )
    checks.check(
        "not-attach-l1",
        "the displayed rule is not attached to L1",
        "Do not attach L1" in note and "Do not attach L1" not in axiom,
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

    sites = ball(48)
    nonzero = [v for v in sites if v != (0, 0, 0)]
    dist = dijkstra_mu(sites)
    t1600 = dist[(16, 0, 0)]
    t161616 = dist[(16, 16, 16)]
    t4800 = dist[(48, 0, 0)]
    t4500 = dist[(45, 0, 0)]
    reverse = 3 * t1600 * t1600 > t161616 * t161616
    witness_axis = (
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
        (8, 1, 1),
        (9, 1, 1),
        (10, 1, 1),
        (11, 1, 1),
        (12, 1, 1),
        (13, 1, 1),
        (14, 1, 1),
        (15, 1, 1),
        (16, 1, 1),
        (16, 1, 0),
        (16, 0, 0),
    )
    witness_mu_costs = [mu_cost(a, b) for a, b in zip(witness_axis, witness_axis[1:])]
    print(f"n_sites {len(sites)}")
    print(f"t(16,0,0) {t1600}")
    print(f"t(16,16,16) {t161616}")
    print(f"t(16,0,0)^2/256 {t1600 * t1600}/256")
    print(f"t(16,16,16)^2/768 {t161616 * t161616}/768")
    print(f"3t_axis^2 {3 * t1600 * t1600}")
    print(f"t_body^2 {t161616 * t161616}")
    print(f"reverse {reverse}")
    print(f"t(48,0,0) {t4800}")
    print(f"t(45,0,0) {t4500}")
    print(f"dijkstra_calls {DIJKSTRA_CALLS}")
    print(f"witness_mu_costs {witness_mu_costs}")
    print(f"witness_mu_sum {sum(witness_mu_costs)}")

    checks.check(
        "t-1600-161616",
        f"t(16,0,0)={T_AXIS_REP} and t(16,16,16)={T_BODY_REP}",
        t1600 == T_AXIS_REP and t161616 == T_BODY_REP,
    )
    checks.check(
        "reverse-k16",
        "t(16,0,0)^2/256 > t(16,16,16)^2/768 does not hold",
        (not reverse)
        and 3 * t1600 * t1600 == 2028
        and t161616 * t161616 == 2500
        and "2028 > 2500" in note
        and "inequality does not hold" in note,
    )
    checks.check(
        "one-dijkstra",
        "exactly one Dijkstra ran",
        DIJKSTRA_CALLS == 1,
    )
    checks.check(
        "ball-b48",
        "B_48(0) has 152193 sites and 152192 nonzero sites",
        len(sites) == 152193 and len(nonzero) == 152192 and all(l1(v) <= 48 for v in sites),
    )
    checks.check(
        "reachable",
        "every site of B_48(0) is reached",
        len(dist) == 152193,
    )
    checks.check(
        "note-records-times",
        "note records the two computed arrivals",
        "`26`" in note
        and "`50`" in note
        and "`(16,0,0)`" in note
        and "`(16,16,16)`" in note,
    )
    checks.check(
        "note-records-reverse-products",
        "note records the integer reverse products",
        "2028 > 2500" in note,
    )
    checks.check(
        "not-leftover-of-nu",
        "μ prices the corridor-slide hop at 3 while ν prices it at 1",
        mu_cost((1, 1, 0), (2, 1, 0)) == 3
        and nu_cost((1, 1, 0), (2, 1, 0)) == 1
        and sum(witness_mu_costs) == 26
        and t1600 == 26
        and t161616 == 50
        and t1600 != 22
        and "cannot price corridor slide" in note
        and "22` versus `50" in note,
    )
    checks.check(
        "not-leftover-of-b45",
        "(16,16,16) lies outside B_45(0) and the note says so",
        l1((16, 16, 16)) == 48
        and (16, 16, 16) in dist
        and t4800 == 62
        and t4500 == 55
        and t4500 != 51
        and t4500 != 59
        and "absent from `B_45(0)`" in note
        and "not leftover of the `B_45(0)` times" in note,
    )
    checks.check(
        "seed-and-corridor-clauses",
        "seed-exit, both-weights-1, support-drop, and corridor-slide cost 3; other hops cost 1",
        mu_cost((0, 0, 0), (1, 0, 0)) == 3
        and mu_cost((1, 0, 0), (2, 0, 0)) == 3
        and mu_cost((1, 1, 0), (1, 0, 0)) == 3
        and mu_cost((1, 1, 0), (2, 1, 0)) == 3
        and mu_cost((1, 0, 0), (1, 1, 0)) == 1
        and mu_cost((1, 1, 0), (1, 1, 1)) == 1
        and mu_cost((1, 1, 1), (2, 1, 1)) == 1
        and mu_cost((2, 2, 0), (3, 2, 0)) == 1,
    )
    checks.check(
        "axiom-untouched",
        "the axiom memo is an input only and still names the four axioms",
        "### Admissibility / Local Constraint" in axiom
        and "μ(v→w)" not in axiom,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
