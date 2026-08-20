#!/usr/bin/env python3
"""Score same-k reverse at k=1 under δε on B_6(0).

One origin Dijkstra. No cache write. No axiom edit.
"""

from __future__ import annotations

import ast
import heapq
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/DEEP_ENTER_SAMEK_K1_B6_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/DEEP_ENTER_SAMEK_K1_B6_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
CLAIM_SCOPE = (
    "Same-k reverse at k=1 under the named "
    "deep-enter hop-cost on B_6(0) is reported. "
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
T_AXIS_REP = 3
T_BODY_REP = 5
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


def unit_coord_count(v: tuple[int, int, int]) -> int:
    return int(abs(v[0]) == 1) + int(abs(v[1]) == 1) + int(abs(v[2]) == 1)


def min_continuing_abs(
    v: tuple[int, int, int], w: tuple[int, int, int]
) -> int | None:
    continuing = [abs(w[i]) for i in range(3) if v[i] != 0]
    if not continuing:
        return None
    return min(continuing)


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


def rho3_cost(v: tuple[int, int, int], w: tuple[int, int, int]) -> int:
    if mu_cost(v, w) == 3:
        return 3
    if support_size(v) == 3 and support_size(w) == 3 and unit_coord_count(w) == 2:
        return 3
    return 1


def delta_eps_cost(v: tuple[int, int, int], w: tuple[int, int, int]) -> int:
    if rho3_cost(v, w) == 3:
        return 3
    if (
        support_size(v) == 2
        and support_size(w) == 3
        and min_continuing_abs(v, w) is not None
        and min_continuing_abs(v, w) >= 2
    ):
        return 3
    return 1


def dijkstra_delta_eps(
    sites: list[tuple[int, int, int]],
) -> dict[tuple[int, int, int], int]:
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
            nd = d + delta_eps_cost(v, w)
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
        "δε is not written into Admissibility",
        "Do not write `δε` into Admissibility" in note,
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

    sites = ball(6)
    nonzero = [v for v in sites if v != (0, 0, 0)]
    dist = dijkstra_delta_eps(sites)
    t100 = dist[(1, 0, 0)]
    t111 = dist[(1, 1, 1)]
    t600 = dist[(6, 0, 0)]
    reverse = 3 * t100 * t100 > t111 * t111
    deep_enter = ((2, 2, 0), (2, 2, 1))
    unit_cube = ((1, 1, 0), (1, 1, 1))
    unit_plane = ((2, 1, 0), (2, 1, 1))
    ridge_hop = ((1, 1, 1), (2, 1, 1))
    interior_hop = ((2, 2, 2), (3, 2, 2))
    print(f"n_sites {len(sites)}")
    print(f"t(1,0,0) {t100}")
    print(f"t(1,1,1) {t111}")
    print(f"t(1,0,0)^2/1 {t100 * t100}/1")
    print(f"t(1,1,1)^2/3 {t111 * t111}/3")
    print(f"3t_axis^2 {3 * t100 * t100}")
    print(f"t_body^2 {t111 * t111}")
    print(f"reverse {reverse}")
    print(f"t(6,0,0) {t600}")
    print(f"dijkstra_calls {DIJKSTRA_CALLS}")
    print(f"delta_eps_deep {delta_eps_cost(*deep_enter)}")
    print(f"rho3_deep {rho3_cost(*deep_enter)}")
    print(f"delta_eps_cube {delta_eps_cost(*unit_cube)}")
    print(f"delta_eps_plane {delta_eps_cost(*unit_plane)}")
    print(f"min_all_deep {min(abs(c) for c in deep_enter[1])}")
    print(f"min_cont_deep {min_continuing_abs(*deep_enter)}")

    checks.check(
        "t-100-111",
        f"t(1,0,0)={T_AXIS_REP} and t(1,1,1)={T_BODY_REP}",
        t100 == T_AXIS_REP and t111 == T_BODY_REP,
    )
    checks.check(
        "reverse-k1",
        "t(1,0,0)^2/1 > t(1,1,1)^2/3 holds",
        reverse
        and 3 * t100 * t100 == 27
        and t111 * t111 == 25
        and "27 > 25" in note
        and "inequality holds" in note,
    )
    checks.check(
        "one-dijkstra",
        "exactly one Dijkstra ran",
        DIJKSTRA_CALLS == 1,
    )
    checks.check(
        "ball-b6",
        "B_6(0) has 377 sites and 376 nonzero sites",
        len(sites) == 377 and len(nonzero) == 376 and all(l1(v) <= 6 for v in sites),
    )
    checks.check(
        "reachable",
        "every site of B_6(0) is reached",
        len(dist) == 377,
    )
    checks.check(
        "note-records-times",
        "note records the two computed arrivals",
        "`3`" in note
        and "`5`" in note
        and "`(1,0,0)`" in note
        and "`(1,1,1)`" in note,
    )
    checks.check(
        "note-records-reverse-products",
        "note records the integer reverse products",
        "27 > 25" in note,
    )
    checks.check(
        "independent-b6-dijkstra",
        "axis endpoint t(6,0,0)=18 and the note scores B_6 independently",
        t600 == 18
        and l1((1, 1, 1)) == 3
        and (1, 1, 1) in dist
        and "not leftover of a larger-ball table" in note,
    )
    checks.check(
        "k1-pair-kept",
        "the k=1 pair remains 3 versus 5 on this ball",
        t100 == 3
        and t111 == 5
        and "3` versus `5" in note,
    )
    checks.check(
        "deep-enter-clause",
        "δε prices (2,2,0)→(2,2,1) at 3 while ρ3 prices it at 1",
        delta_eps_cost(*deep_enter) == 3
        and rho3_cost(*deep_enter) == 1
        and mu_cost(*deep_enter) == 1
        and min_continuing_abs(*deep_enter) == 2
        and unit_coord_count(deep_enter[1]) == 1
        and min(abs(c) for c in deep_enter[1]) == 1
        and "cannot price the deep-enter hop" in note,
    )
    checks.check(
        "spare-unit-cube-and-plane",
        "δε leaves unit-cube and unit-plane 2→3 hops at cost 1",
        delta_eps_cost(*unit_cube) == 1
        and rho3_cost(*unit_cube) == 1
        and delta_eps_cost(*unit_plane) == 1
        and rho3_cost(*unit_plane) == 1
        and min_continuing_abs(*unit_cube) == 1
        and min_continuing_abs(*unit_plane) == 1
        and "unit cube" in note
        and "unit plane" in note,
    )
    checks.check(
        "seed-and-deep-enter-clauses",
        "ν clauses, corridor-slide, ridge 3→3, and deep 2→3 cost 3; 1→2, unit-cube 2→3, unit-plane 2→3, and non-ridge 3→3 cost 1",
        delta_eps_cost((0, 0, 0), (1, 0, 0)) == 3
        and delta_eps_cost((1, 0, 0), (2, 0, 0)) == 3
        and delta_eps_cost((1, 1, 0), (1, 0, 0)) == 3
        and delta_eps_cost((1, 1, 0), (2, 1, 0)) == 3
        and delta_eps_cost((1, 1, 1), (2, 1, 1)) == 3
        and delta_eps_cost(*deep_enter) == 3
        and delta_eps_cost((1, 0, 0), (1, 1, 0)) == 1
        and delta_eps_cost(*unit_cube) == 1
        and delta_eps_cost(*unit_plane) == 1
        and delta_eps_cost((2, 2, 0), (3, 2, 0)) == 1
        and delta_eps_cost(*interior_hop) == 1
        and rho3_cost(*ridge_hop) == 3,
    )
    checks.check(
        "axiom-untouched",
        "the axiom memo is an input only and still names the four axioms",
        "### Admissibility / Local Constraint" in axiom
        and "δε(v→w)" not in axiom,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
