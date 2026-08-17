#!/usr/bin/env python3
"""Score same-k reverse at k=2 under ε on B_8(0).

One origin Dijkstra. No cache write. No axiom edit.
"""

from __future__ import annotations

import ast
import heapq
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/ENTER_BODY_SAMEK_K2_B8_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/ENTER_BODY_SAMEK_K2_B8_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
CLAIM_SCOPE = (
    "Same-k reverse at k=2 under the named "
    "enter-body hop-cost on B_8(0) is reported. "
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
T_AXIS_REP = 6
T_BODY_REP = 10
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


def min_nonzero_abs(v: tuple[int, int, int]) -> int | None:
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
    if support_size(v) == 2 and support_size(w) == 2 and min_nonzero_abs(w) == 1:
        return 3
    return 1


def eps_cost(v: tuple[int, int, int], w: tuple[int, int, int]) -> int:
    if mu_cost(v, w) == 3 or (support_size(v) == 2 and support_size(w) == 3):
        return 3
    return 1


def dijkstra_eps(sites: list[tuple[int, int, int]]) -> dict[tuple[int, int, int], int]:
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
            nd = d + eps_cost(v, w)
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
        "ε is not written into Admissibility",
        "Do not write `ε` into Admissibility" in note,
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

    sites = ball(8)
    nonzero = [v for v in sites if v != (0, 0, 0)]
    dist = dijkstra_eps(sites)
    t200 = dist[(2, 0, 0)]
    t222 = dist[(2, 2, 2)]
    t800 = dist[(8, 0, 0)]
    reverse = 3 * t200 * t200 > t222 * t222
    enter_hop = ((1, 1, 0), (1, 1, 1))
    hug_hop = ((1, 1, 0), (2, 1, 0))
    witness_axis = ((0, 0, 0), (1, 0, 0), (2, 0, 0))
    witness_body = (
        (0, 0, 0),
        (1, 0, 0),
        (1, 1, 0),
        (1, 1, 1),
        (2, 1, 1),
        (2, 2, 1),
        (2, 2, 2),
    )
    witness_axis_costs = [eps_cost(a, b) for a, b in zip(witness_axis, witness_axis[1:])]
    witness_body_costs = [eps_cost(a, b) for a, b in zip(witness_body, witness_body[1:])]
    print(f"n_sites {len(sites)}")
    print(f"t(2,0,0) {t200}")
    print(f"t(2,2,2) {t222}")
    print(f"t(2,0,0)^2/4 {t200 * t200}/4")
    print(f"t(2,2,2)^2/12 {t222 * t222}/12")
    print(f"3t_axis^2 {3 * t200 * t200}")
    print(f"t_body^2 {t222 * t222}")
    print(f"reverse {reverse}")
    print(f"t(8,0,0) {t800}")
    print(f"dijkstra_calls {DIJKSTRA_CALLS}")
    print(f"eps_enter {eps_cost(*enter_hop)}")
    print(f"mu_enter {mu_cost(*enter_hop)}")
    print(f"eps_hug {eps_cost(*hug_hop)}")
    print(f"mu_hug {mu_cost(*hug_hop)}")
    print(f"witness_axis_costs {witness_axis_costs}")
    print(f"witness_body_costs {witness_body_costs}")

    checks.check(
        "t-200-222",
        f"t(2,0,0)={T_AXIS_REP} and t(2,2,2)={T_BODY_REP}",
        t200 == T_AXIS_REP and t222 == T_BODY_REP,
    )
    checks.check(
        "reverse-k2",
        "t(2,0,0)^2/4 > t(2,2,2)^2/12 holds",
        reverse
        and 3 * t200 * t200 == 108
        and t222 * t222 == 100
        and "108 > 100" in note
        and "inequality holds" in note,
    )
    checks.check(
        "recover-k2",
        "same-k reverse recovers at k=2",
        reverse and "recovers at `k=2`" in note,
    )
    checks.check(
        "one-dijkstra",
        "exactly one Dijkstra ran",
        DIJKSTRA_CALLS == 1,
    )
    checks.check(
        "ball-b8",
        "B_8(0) has 833 sites and 832 nonzero sites",
        len(sites) == 833 and len(nonzero) == 832 and all(l1(v) <= 8 for v in sites),
    )
    checks.check(
        "reachable",
        "every site of B_8(0) is reached",
        len(dist) == 833,
    )
    checks.check(
        "note-records-times",
        "note records the two computed arrivals",
        "`6`" in note
        and "`10`" in note
        and "`(2,0,0)`" in note
        and "`(2,2,2)`" in note,
    )
    checks.check(
        "note-records-reverse-products",
        "note records the integer reverse products",
        "108 > 100" in note,
    )
    checks.check(
        "independent-b8-dijkstra",
        "axis endpoint t(8,0,0)=24 and the note scores B_8 independently",
        t800 == 24
        and l1((2, 2, 2)) == 6
        and (2, 2, 2) in dist
        and "not leftover of a larger-ball table" in note
        and "not leftover of the `B_6(0)` times" in note,
    )
    checks.check(
        "not-leftover-of-mu",
        "μ prices the enter-body hop at 1 while ε prices it at 3",
        eps_cost(*enter_hop) == 3
        and mu_cost(*enter_hop) == 1
        and sum(witness_body_costs) == 10
        and sum(witness_axis_costs) == 6
        and t200 == 6
        and t222 == 10
        and t222 != 8
        and "cannot price the enter-body hop" in note
        and "`6` versus `8`" in note,
    )
    checks.check(
        "enter-body-clauses",
        "μ clauses and 2→3 cost 3; 1→2 and non-hugging 2→2 cost 1",
        eps_cost((0, 0, 0), (1, 0, 0)) == 3
        and eps_cost((1, 0, 0), (2, 0, 0)) == 3
        and eps_cost((1, 0, 0), (1, 1, 0)) == 1
        and eps_cost((1, 1, 0), (1, 0, 0)) == 3
        and eps_cost((1, 1, 0), (1, 1, 1)) == 3
        and eps_cost((1, 1, 0), (2, 1, 0)) == 3
        and eps_cost((2, 2, 0), (3, 2, 0)) == 1
        and eps_cost((1, 1, 1), (2, 1, 1)) == 1,
    )
    checks.check(
        "axiom-untouched",
        "the axiom memo is an input only and still names the four axioms",
        "### Admissibility / Local Constraint" in axiom
        and "ε(v→w)" not in axiom
        and "μ(v→w)" not in axiom,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
