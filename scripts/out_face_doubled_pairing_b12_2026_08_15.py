#!/usr/bin/env python3
"""Score doubled pairing reverse under ω on B_12(0).

One origin Dijkstra. No cache write. No axiom edit.
"""

from __future__ import annotations

import ast
import heapq
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/OUT_FACE_DOUBLED_PAIRING_B12_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/OUT_FACE_DOUBLED_PAIRING_B12_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
CLAIM_SCOPE = (
    "Doubled-axis versus body-diagonal reverse under the named "
    "out-face hop-cost on B_12(0) is reported for available "
    "k=1..4. Displayed, not adopted."
)
NEIGH = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
FORBIDDEN_PARTS = (
    ("G_", "N"),
    ("1/", "r"),
    ("1/", "r^2"),
    ("Lattice-", "named"),
    ("not a ", "TOE"),
)
# (k, t(2k,0,0), t(k,k,k), reverse)
REPORTED = ((1, 6, 5, True), (2, 12, 10, True), (3, 18, 13, True), (4, 24, 16, True))
REVERSE_PRODUCTS = ("108 > 100", "432 > 400", "972 > 676", "1728 > 1024")
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


def omega_cost(v: tuple[int, int, int], w: tuple[int, int, int]) -> int:
    if rho3_cost(v, w) == 3:
        return 3
    if (
        support_size(v) == 2
        and support_size(w) == 2
        and max(abs(c) for c in w) > max(abs(c) for c in v)
    ):
        return 3
    return 1


def dijkstra_omega(
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
            nd = d + omega_cost(v, w)
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
    print(
        "external_scientific_inputs: none; named hop-cost on the finite "
        "nearest-neighbor graph B_12(0) only"
    )
    print(
        "package_local_integrity_reads: proposed source note and live axiom "
        "memo only; no cache or governance surface is written"
    )
    print(
        "measure_boundary: integer hop-costs and one Dijkstra; no fit and "
        "no second graph search"
    )
    print(
        "claim_boundary: doubled pairing reverse at k=1..4 is displayed, "
        "not adopted"
    )

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
        "Displayed, not adopted" in note,
    )
    checks.check(
        "not-in-admissibility",
        "ω is not written into Admissibility",
        "Do not write ω into Admissibility." in note
        and "Do not write `ω` into Admissibility." in note,
    )
    checks.check(
        "not-attach-l1",
        "the displayed rule is not attached to L1",
        "Do not attach L1." in note and "Do not attach L1." not in axiom,
    )
    checks.check(
        "uniqueness-not-claimed",
        "uniqueness among hop-costs is not claimed",
        "Uniqueness is not claimed" in note and "unique hop-cost" not in note,
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
    nonzero = [v for v in sites if v != (0, 0, 0)]
    dist = dijkstra_omega(sites)
    unit_face_grow = ((1, 1, 0), (2, 1, 0))
    out_face_hop = ((2, 2, 0), (3, 2, 0))
    body_last = ((1, 1, 0), (1, 1, 1))
    interior_hop = ((2, 2, 2), (3, 2, 2))
    ridge_slide = ((1, 1, 1), (2, 1, 1))
    height2_nongrow = ((1, -2, 0), (2, -2, 0))
    later_out_face = ((7, 2, 0), (8, 2, 0))
    t1200 = dist[(12, 0, 0)]
    t320 = dist[(3, 2, 0)]
    witness_rho3_axis8 = (
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
        (8, -2, 0),
        (8, -1, 0),
        (8, 0, 0),
    )
    witness_out_face = (
        (0, 0, 0),
        (1, 0, 0),
        (1, 1, 0),
        (1, 2, 0),
        (2, 2, 0),
        (3, 2, 0),
    )
    in_ball_new = 0
    for site in sites:
        sx, sy, sz = site
        for dx, dy, dz in NEIGH:
            neighbor = (sx + dx, sy + dy, sz + dz)
            if neighbor not in dist:
                continue
            if omega_cost(site, neighbor) == 3 and rho3_cost(site, neighbor) == 1:
                in_ball_new += 1
    print(f"n_sites {len(sites)}")
    print(f"dijkstra_calls {DIJKSTRA_CALLS}")
    print(f"t(12,0,0) {t1200}")
    print(f"t(3,2,0) {t320}")
    print(
        f"omega_out_face {omega_cost(*out_face_hop)} "
        f"rho3_out_face {rho3_cost(*out_face_hop)} "
        f"mu_out_face {mu_cost(*out_face_hop)}"
    )
    print(f"omega_unit_face_grow {omega_cost(*unit_face_grow)}")
    print(f"omega_body_last {omega_cost(*body_last)}")
    print(f"out_face_live_hops {in_ball_new}")
    print(f"witness_rho3_axis8_omega {path_cost(witness_rho3_axis8, omega_cost)}")
    print(f"witness_rho3_axis8_rho3 {path_cost(witness_rho3_axis8, rho3_cost)}")
    print(f"witness_out_face_omega {path_cost(witness_out_face, omega_cost)}")
    print(f"witness_out_face_rho3 {path_cost(witness_out_face, rho3_cost)}")

    all_match = True
    available = True
    for k, t_axis_rep, t_body_rep, reverse_rep in REPORTED:
        axis = (2 * k, 0, 0)
        body = (k, k, k)
        in_ball = l1(axis) <= 12 and l1(body) <= 12
        available = available and in_ball
        t_axis = dist[axis]
        t_body = dist[body]
        lhs = 3 * t_axis * t_axis
        rhs = 4 * t_body * t_body
        reverse = lhs > rhs
        all_match = all_match and reverse == reverse_rep
        print(
            f"k {k} t({2 * k},0,0) {t_axis} t({k},{k},{k}) {t_body} "
            f"t_axis^2/(4k^2) {t_axis * t_axis}/{4 * k * k} "
            f"t_body^2/(3k^2) {t_body * t_body}/{3 * k * k} "
            f"3t_axis^2 {lhs} 4t_body^2 {rhs} reverse {reverse}"
        )
        checks.check(
            f"t-k{k}",
            f"t({2 * k},0,0)={t_axis_rep} and t({k},{k},{k})={t_body_rep}",
            in_ball and t_axis == t_axis_rep and t_body == t_body_rep,
        )
        checks.check(
            f"reverse-k{k}",
            f"t({2 * k},0,0)^2/(4k^2) > t({k},{k},{k})^2/(3k^2) is {reverse_rep}",
            reverse == reverse_rep and (lhs > rhs) == reverse,
        )

    checks.check(
        "one-dijkstra",
        "exactly one Dijkstra from the origin is executed",
        DIJKSTRA_CALLS == 1 and "dijkstra_omega" in source,
    )
    checks.check(
        "ball-b12",
        "B_12(0) has 2625 sites and 2624 nonzero sites",
        len(sites) == 2625 and len(nonzero) == 2624 and all(l1(v) <= 12 for v in sites),
    )
    checks.check(
        "reachable",
        "every site of B_12(0) is reached",
        len(dist) == 2625 and all(dist[site] < 10**9 for site in sites),
    )
    checks.check(
        "pairs-available",
        "both sites of each k=1..4 pair lie in B_12(0)",
        available
        and l1((8, 0, 0)) == 8
        and l1((4, 4, 4)) == 12
        and "no pair is omitted" in note,
    )
    checks.check(
        "reverse-bits-match",
        "computed reverse bits match the four-scale census",
        all_match,
    )
    checks.check(
        "note-records-times",
        "note records the eight computed arrivals",
        all(
            f"`{t_axis}`" in note and f"`{t_body}`" in note
            for _k, t_axis, t_body, _rev in REPORTED
        )
        and "`(2,0,0)`" in note
        and "`(6,0,0)`" in note
        and "`(8,0,0)`" in note
        and "`(4,4,4)`" in note,
    )
    checks.check(
        "note-records-reverse-products",
        "note records the four integer reverse products",
        all(product in note for product in REVERSE_PRODUCTS),
    )
    checks.check(
        "out-face-clause",
        "the named 2-to-2 growing-max clause prices (2,2,0) to (3,2,0) at 3",
        omega_cost(*out_face_hop) == 3
        and rho3_cost(*out_face_hop) == 1
        and mu_cost(*out_face_hop) == 1
        and omega_cost(*later_out_face) == 3
        and rho3_cost(*later_out_face) == 1
        and omega_cost(*height2_nongrow) == 1
        and out_face_hop[0] in dist
        and out_face_hop[1] in dist
        and "cannot price out-face" in note,
    )
    checks.check(
        "out-face-live-on-ball",
        "nearest-neighbor hops inside B_12(0) trigger the extra out-face clause",
        in_ball_new > 0 and "new clause is live" in note,
    )
    checks.check(
        "hop-body-last-untaxed",
        "the 2-to-3 hop into (1,1,1) is not priced by the extra clause",
        omega_cost(*body_last) == 1
        and rho3_cost(*body_last) == 1
        and unit_coord_count((1, 1, 1)) == 3,
    )
    checks.check(
        "not-leftover-of-rho3",
        "ω prices height-2 out-face growth at 3 while ρ3 prices it at 1, and t(8,0,0) differs",
        omega_cost(*out_face_hop) == 3
        and rho3_cost(*out_face_hop) == 1
        and dist[(8, 0, 0)] == 24
        and path_cost(witness_rho3_axis8, rho3_cost) == 20
        and path_cost(witness_rho3_axis8, omega_cost) == 32
        and t320 == 11
        and path_cost(witness_out_face, omega_cost) == 11
        and path_cost(witness_out_face, rho3_cost) == 9
        and "24` versus `20" in note
        and "cannot price out-face" in note,
    )
    checks.check(
        "not-leftover-of-b11",
        "(4,4,4) lies outside B_11(0) and the note says so",
        l1((4, 4, 4)) == 12
        and (4, 4, 4) in dist
        and t1200 == 34
        and "absent from `B_11(0)`" in note,
    )
    checks.check(
        "omega-clauses",
        "seed-exit, axis, drop, corridor-slide, ridge-slide, and out-face growth cost 3; 1-to-2, small 2-to-3, non-growing height-2, and interior 3-to-3 cost 1",
        omega_cost((0, 0, 0), (1, 0, 0)) == 3
        and omega_cost((1, 0, 0), (2, 0, 0)) == 3
        and omega_cost((1, 1, 0), (1, 0, 0)) == 3
        and omega_cost((1, 1, 0), (2, 1, 0)) == 3
        and omega_cost(*ridge_slide) == 3
        and omega_cost(*out_face_hop) == 3
        and omega_cost((2, 2, 0), (2, 3, 0)) == 3
        and omega_cost((1, 0, 0), (1, 1, 0)) == 1
        and omega_cost((1, 1, 0), (1, 1, 1)) == 1
        and omega_cost((2, 1, 0), (2, 1, 1)) == 1
        and omega_cost(*height2_nongrow) == 1
        and omega_cost((2, 2, 0), (2, 2, 1)) == 1
        and omega_cost(*interior_hop) == 1,
    )
    checks.check(
        "thm3-not-in-admissibility",
        "the live Admissibility wording is unchanged and does not name ω",
        "There is one fixed nearest-neighbor admissibility rule" in axiom
        and "ω(v→w)" not in axiom
        and "Do not write ω into Admissibility." in note,
    )
    checks.check(
        "axiom-untouched",
        "the axiom memo is an input only and still names the four axioms",
        "### Admissibility / Local Constraint" in axiom
        and "ω(v→w)" not in axiom
        and "ρ3(v→w)" not in axiom,
    )

    print("per_element: named hop-cost values are 1 or 3 on nearest-neighbor hops.")
    print("per_site: arrival times are reported at the doubled pairing sites and (12,0,0).")
    print("lattice_wide: checked and not executed — the search stays inside B_12(0).")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
