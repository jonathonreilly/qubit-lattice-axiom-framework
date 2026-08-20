#!/usr/bin/env python3
"""Score same-k reverse at k=7 under κλ on B_21(0).

One origin Dijkstra. No cache write. No axiom edit.
"""

from __future__ import annotations

import ast
import heapq
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/KAPPA_LATE_LEAVE_SAMEK_K7_B21_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/KAPPA_LATE_LEAVE_SAMEK_K7_B21_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
CLAIM_SCOPE = (
    "Same-k reverse at k=7 under the named "
    "kappa-plus-late-leave hop-cost on B_21(0) is reported. "
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


def unit_coord_count(v: tuple[int, int, int]) -> int:
    return int(abs(v[0]) == 1) + int(abs(v[1]) == 1) + int(abs(v[2]) == 1)


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


def rho3_cost(v: tuple[int, int, int], w: tuple[int, int, int]) -> int:
    if mu_cost(v, w) == 3:
        return 3
    if support_size(v) == 3 and support_size(w) == 3 and unit_coord_count(w) == 2:
        return 3
    return 1


def kappa_cost(v: tuple[int, int, int], w: tuple[int, int, int]) -> int:
    if rho3_cost(v, w) == 3:
        return 3
    if support_size(v) == 2 and support_size(w) == 3 and unit_coord_count(w) == 2:
        return 3
    return 1


def lambda2_cost(v: tuple[int, int, int], w: tuple[int, int, int]) -> int:
    if rho3_cost(v, w) == 3:
        return 3
    if support_size(v) == 1 and support_size(w) == 2 and max(abs(c) for c in w) >= 2:
        return 3
    return 1


def kappa_lambda_cost(v: tuple[int, int, int], w: tuple[int, int, int]) -> int:
    if rho3_cost(v, w) == 3:
        return 3
    if support_size(v) == 2 and support_size(w) == 3 and unit_coord_count(w) == 2:
        return 3
    if support_size(v) == 1 and support_size(w) == 2 and max(abs(c) for c in w) >= 2:
        return 3
    return 1


def dijkstra_kappa_lambda(
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
            nd = d + kappa_lambda_cost(v, w)
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


def path_cost(
    walk: tuple[tuple[int, int, int], ...],
    cost_fn,
) -> int:
    return sum(cost_fn(a, b) for a, b in zip(walk, walk[1:]))


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
        "κλ is not written into Admissibility",
        "Do not write κλ into Admissibility" in note
        and "Do not write `κλ` into Admissibility" in note,
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

    sites = ball(21)
    nonzero = [v for v in sites if v != (0, 0, 0)]
    dist = dijkstra_kappa_lambda(sites)
    t700 = dist[(7, 0, 0)]
    t777 = dist[(7, 7, 7)]
    t2100 = dist[(21, 0, 0)]
    t1800 = dist[(18, 0, 0)]
    t1911 = dist[(19, 1, 1)]
    reverse = 3 * t700 * t700 > t777 * t777
    witness_axis = (
        (0, 0, 0),
        (0, -1, 0),
        (1, -1, 0),
        (1, -2, 0),
        (2, -2, 0),
        (3, -2, 0),
        (4, -2, 0),
        (5, -2, 0),
        (6, -2, 0),
        (7, -2, 0),
        (7, -1, 0),
        (7, 0, 0),
    )
    witness_body = (
        (0, 0, 0),
        (0, 0, 1),
        (0, 1, 1),
        (0, 1, 2),
        (0, 2, 2),
        (0, 3, 2),
        (0, 4, 2),
        (0, 5, 2),
        (0, 6, 2),
        (0, 7, 2),
        (0, 7, 3),
        (0, 7, 4),
        (0, 7, 5),
        (0, 7, 6),
        (0, 7, 7),
        (1, 7, 7),
        (2, 7, 7),
        (3, 7, 7),
        (4, 7, 7),
        (5, 7, 7),
        (6, 7, 7),
        (7, 7, 7),
    )
    witness_ridge = (
        (0, 0, 0),
        (0, 1, 0),
        (1, 1, 0),
        (1, 2, 0),
        *[(n, 2, 0) for n in range(2, 20)],
        (19, 1, 0),
        (19, 1, 1),
    )
    witness_axis_costs = [
        kappa_lambda_cost(a, b) for a, b in zip(witness_axis, witness_axis[1:])
    ]
    witness_body_costs = [
        kappa_lambda_cost(a, b) for a, b in zip(witness_body, witness_body[1:])
    ]
    late_leave_hop = ((2, 0, 0), (2, 1, 0))
    unit_cube_hop = ((1, 0, 0), (1, 1, 0))
    ridge_enter_hop = ((2, 1, 0), (2, 1, 1))
    every_enter_hop = ((1, 1, 0), (1, 1, 1))
    generic_body_enter = ((0, 7, 7), (1, 7, 7))
    print(f"n_sites {len(sites)}")
    print(f"t(7,0,0) {t700}")
    print(f"t(7,7,7) {t777}")
    print(f"t(7,0,0)^2/49 {t700 * t700}/49")
    print(f"t(7,7,7)^2/147 {t777 * t777}/147")
    print(f"3t_axis^2 {3 * t700 * t700}")
    print(f"t_body^2 {t777 * t777}")
    print(f"reverse {reverse}")
    print(f"t(21,0,0) {t2100}")
    print(f"t(18,0,0) {t1800}")
    print(f"t(19,1,1) {t1911}")
    print(f"dijkstra_calls {DIJKSTRA_CALLS}")
    print(f"witness_axis_sum {sum(witness_axis_costs)}")
    print(f"witness_body_sum {sum(witness_body_costs)}")
    print(f"klam_late_leave {kappa_lambda_cost(*late_leave_hop)}")
    print(f"kappa_late_leave {kappa_cost(*late_leave_hop)}")
    print(f"lambda2_late_leave {lambda2_cost(*late_leave_hop)}")
    print(f"rho3_late_leave {rho3_cost(*late_leave_hop)}")
    print(f"klam_ridge_enter {kappa_lambda_cost(*ridge_enter_hop)}")
    print(f"kappa_ridge_enter {kappa_cost(*ridge_enter_hop)}")
    print(f"lambda2_ridge_enter {lambda2_cost(*ridge_enter_hop)}")
    print(f"rho3_ridge_enter {rho3_cost(*ridge_enter_hop)}")
    print(f"klam_unit_cube {kappa_lambda_cost(*unit_cube_hop)}")
    print(f"witness_ridge_klam {path_cost(witness_ridge, kappa_lambda_cost)}")
    print(f"witness_ridge_rho3 {path_cost(witness_ridge, rho3_cost)}")

    checks.check(
        "t-700-777",
        "t(7,0,0)=19 and t(7,7,7)=25",
        t700 == 19
        and t777 == 25
        and t700 == sum(witness_axis_costs)
        and t777 == sum(witness_body_costs),
    )
    checks.check(
        "reverse-k7",
        "t(7,0,0)^2/49 > t(7,7,7)^2/147 holds",
        reverse
        and 3 * t700 * t700 == 1083
        and t777 * t777 == 625
        and "1083 > 625" in note
        and "inequality holds" in note,
    )
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
        "reachable",
        "every site of B_21(0) is reached",
        len(dist) == 13287,
    )
    checks.check(
        "note-records-times",
        "note records the two computed arrivals",
        "`19`" in note
        and "`25`" in note
        and "`(7,0,0)`" in note
        and "`(7,7,7)`" in note,
    )
    checks.check(
        "note-records-reverse-products",
        "note records the integer reverse products",
        "1083 > 625" in note,
    )
    checks.check(
        "not-leftover-of-rho3",
        "κλ prices late-leave and ridge-enter at 3 while ρ3 prices both at 1",
        kappa_lambda_cost(*late_leave_hop) == 3
        and rho3_cost(*late_leave_hop) == 1
        and kappa_lambda_cost(*ridge_enter_hop) == 3
        and rho3_cost(*ridge_enter_hop) == 1
        and kappa_lambda_cost(*unit_cube_hop) == 1
        and t1911 == 31
        and path_cost(witness_ridge, kappa_lambda_cost) == 31
        and path_cost(witness_ridge, rho3_cost) == 29
        and t700 == 19
        and t777 == 25
        and "cannot price late leave" in note
        and "cannot price ridge-enter" in note
        and "new clause is live" in note
        and "spares the unit-cube" in note,
    )
    checks.check(
        "not-leftover-of-kappa",
        "κλ prices the late-leave hop at 3 while κ prices it at 1",
        kappa_lambda_cost(*late_leave_hop) == 3
        and kappa_cost(*late_leave_hop) == 1
        and lambda2_cost(*late_leave_hop) == 3
        and "cannot price late leave" in note
        and "stacked" in note,
    )
    checks.check(
        "not-leftover-of-lambda2",
        "κλ prices the ridge-enter hop at 3 while λ2 prices it at 1",
        kappa_lambda_cost(*ridge_enter_hop) == 3
        and lambda2_cost(*ridge_enter_hop) == 1
        and kappa_cost(*ridge_enter_hop) == 3
        and "cannot price ridge-enter" in note,
    )
    checks.check(
        "not-leftover-of-b18",
        "(7,7,7) lies outside B_18(0) and the note says so",
        l1((7, 7, 7)) == 21
        and (7, 7, 7) in dist
        and t2100 == 37
        and t1800 == 30
        and "absent from `B_18(0)`" in note
        and "not leftover of the `B_18(0)` times" in note,
    )
    checks.check(
        "seed-and-stacked-clauses",
        "seed-exit, both-weights-1, support-drop, corridor-slide, ridge-slide, ridge-enter, and late-leave cost 3; unit-cube 1→2 and generic rises cost 1",
        kappa_lambda_cost((0, 0, 0), (1, 0, 0)) == 3
        and kappa_lambda_cost((1, 0, 0), (2, 0, 0)) == 3
        and kappa_lambda_cost((1, 1, 0), (1, 0, 0)) == 3
        and kappa_lambda_cost((1, 1, 0), (2, 1, 0)) == 3
        and kappa_lambda_cost((1, 1, 1), (2, 1, 1)) == 3
        and kappa_lambda_cost((2, 1, 0), (2, 1, 1)) == 3
        and kappa_lambda_cost((2, 0, 0), (2, 1, 0)) == 3
        and kappa_lambda_cost((3, 0, 0), (3, 1, 0)) == 3
        and kappa_lambda_cost((1, 0, 0), (1, 1, 0)) == 1
        and kappa_lambda_cost((1, 1, 0), (1, 1, 1)) == 1
        and kappa_lambda_cost(*every_enter_hop) == 1
        and kappa_lambda_cost(*generic_body_enter) == 1
        and kappa_lambda_cost((2, 2, 0), (3, 2, 0)) == 1
        and kappa_lambda_cost((2, 2, 2), (3, 2, 2)) == 1
        and kappa_lambda_cost((2, 7, 7), (3, 7, 7)) == 1
        and kappa_lambda_cost((6, 7, 7), (7, 7, 7)) == 1,
    )
    checks.check(
        "axiom-untouched",
        "the axiom memo is an input only and still names the four axioms",
        "### Admissibility / Local Constraint" in axiom
        and "κλ(v→w)" not in axiom
        and "κ(v→w)" not in axiom
        and "λ2(v→w)" not in axiom
        and "ρ3(v→w)" not in axiom,
    )
    checks.check(
        "one-dijkstra-in-note",
        "the theorem stays on B_21(0) and uses one Dijkstra",
        "B_21(0)" in note and "one Dijkstra" in note,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
