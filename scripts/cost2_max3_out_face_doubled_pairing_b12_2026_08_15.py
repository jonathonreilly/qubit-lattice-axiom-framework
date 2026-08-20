#!/usr/bin/env python3
"""Score doubled pairing reverse under c2d3 on B_12(0).

One origin Dijkstra. No cache write. No axiom edit.
"""

from __future__ import annotations

import ast
import heapq
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/COST2_MAX3_OUT_FACE_DOUBLED_PAIRING_B12_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/COST2_MAX3_OUT_FACE_DOUBLED_PAIRING_B12_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
CLAIM_SCOPE = (
    "Doubled-axis versus body-diagonal reverse under the named "
    "cost-2 max≥3 out-face hop-cost on B_12(0) is reported for available "
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
SCALES = (1, 2, 3, 4)
DIJKSTRA_CALLS = 0

WITNESS_AXIS = {
    1: ((0, 0, 0), (1, 0, 0), (2, 0, 0)),
    2: ((0, 0, 0), (1, 0, 0), (2, 0, 0), (3, 0, 0), (4, 0, 0)),
    3: (
        (0, 0, 0),
        (1, 0, 0),
        (2, 0, 0),
        (3, 0, 0),
        (4, 0, 0),
        (5, 0, 0),
        (6, 0, 0),
    ),
    4: (
        (0, 0, 0),
        (1, 0, 0),
        (2, 0, 0),
        (3, 0, 0),
        (4, 0, 0),
        (5, 0, 0),
        (6, 0, 0),
        (7, 0, 0),
        (8, 0, 0),
    ),
}
WITNESS_BODY = {
    1: ((0, 0, 0), (0, 0, 1), (0, 1, 1), (1, 1, 1)),
    2: (
        (0, 0, 0),
        (0, 0, 1),
        (0, 1, 1),
        (0, 1, 2),
        (0, 2, 2),
        (1, 2, 2),
        (2, 2, 2),
    ),
    3: (
        (0, 0, 0),
        (0, 0, 1),
        (0, 1, 1),
        (0, 1, 2),
        (0, 2, 2),
        (0, 2, 3),
        (0, 3, 3),
        (1, 3, 3),
        (2, 3, 3),
        (3, 3, 3),
    ),
    4: (
        (0, 0, 0),
        (0, 0, 1),
        (0, 1, 1),
        (0, 1, 2),
        (0, 2, 2),
        (0, 2, 3),
        (1, 2, 3),
        (1, 2, 4),
        (1, 3, 4),
        (1, 4, 4),
        (2, 4, 4),
        (3, 4, 4),
        (4, 4, 4),
    ),
}
WITNESS_SKIP = (
    (0, 0, 0),
    (0, 1, 0),
    (1, 1, 0),
    (1, 2, 0),
    (2, 2, 0),
    (3, 2, 0),
)
WITNESS_LATER = WITNESS_SKIP + ((4, 2, 0),)
WITNESS_FAR_AXIS = (
    (0, 0, 0),
    (0, -1, 0),
    (0, -1, -1),
    (1, -1, -1),
    (1, -2, -1),
    (2, -2, -1),
    (3, -2, -1),
    (4, -2, -1),
    (5, -2, -1),
    (6, -2, -1),
    (7, -2, -1),
    (8, -2, -1),
    (9, -2, -1),
    (9, -2, 0),
    (10, -2, 0),
    (10, -1, 0),
    (10, 0, 0),
    (11, 0, 0),
    (12, 0, 0),
)
WITNESS_RHO3_AXIS8 = (
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


def max_abs(v: tuple[int, int, int]) -> int:
    return max(abs(c) for c in v)


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


def omega_extra(v: tuple[int, int, int], w: tuple[int, int, int]) -> bool:
    return (
        support_size(v) == 2
        and support_size(w) == 2
        and max_abs(w) > max_abs(v)
    )


def df_extra(v: tuple[int, int, int], w: tuple[int, int, int]) -> bool:
    return omega_extra(v, w) and max_abs(v) >= 2


def d3_extra(v: tuple[int, int, int], w: tuple[int, int, int]) -> bool:
    return omega_extra(v, w) and max_abs(v) >= 3


def d3_cost(v: tuple[int, int, int], w: tuple[int, int, int]) -> int:
    if rho3_cost(v, w) == 3 or d3_extra(v, w):
        return 3
    return 1


def c2d3_cost(v: tuple[int, int, int], w: tuple[int, int, int]) -> int:
    if rho3_cost(v, w) == 3:
        return 3
    if d3_extra(v, w):
        return 2
    return 1


def path_cost(
    walk: tuple[tuple[int, int, int], ...],
    cost_fn,
) -> int:
    return sum(cost_fn(a, b) for a, b in zip(walk, walk[1:]))


def dijkstra_c2d3(
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
            nd = d + c2d3_cost(v, w)
            if nd < dist.get(w, 10**9):
                dist[w] = nd
                heapq.heappush(heap, (nd, w))
    return dist


def literal_audit_paths(source: str) -> tuple[str, ...] | None:
    module = ast.parse(source)
    for node in module.body:
        if not isinstance(node, ast.Assign):
            continue
        if not any(
            isinstance(target, ast.Name) and target.id == "AUDIT_INPUT_PATHS"
            for target in node.targets
        ):
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
        "c2d3 is not written into Admissibility",
        "Do not write c2d3 into Admissibility." in note
        and "Do not write `c2d3` into Admissibility." in note,
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
    dist = dijkstra_c2d3(sites)
    unit_out = ((1, 1, 0), (2, 1, 0))
    df_out = ((2, 2, 0), (3, 2, 0))
    max3_out = ((3, 2, 0), (4, 2, 0))
    body_last = ((1, 1, 0), (1, 1, 1))
    interior_hop = ((2, 2, 2), (3, 2, 2))
    ridge_slide = ((1, 1, 1), (2, 1, 1))
    later_out = ((7, 2, 0), (8, 2, 0))
    t1200 = dist[(12, 0, 0)]
    t320 = dist[(3, 2, 0)]
    t420 = dist[(4, 2, 0)]
    in_ball_new = 0
    for site in sites:
        sx, sy, sz = site
        for dx, dy, dz in NEIGH:
            neighbor = (sx + dx, sy + dy, sz + dz)
            if neighbor not in dist:
                continue
            if (
                d3_extra(site, neighbor)
                and rho3_cost(site, neighbor) == 1
                and c2d3_cost(site, neighbor) == 2
            ):
                in_ball_new += 1

    print(f"n_sites {len(sites)}")
    print(f"dijkstra_calls {DIJKSTRA_CALLS}")
    print(f"t(12,0,0) {t1200}")
    print(f"t(3,2,0) {t320}")
    print(f"t(4,2,0) {t420}")
    print(
        f"c2d3_max3_out {c2d3_cost(*max3_out)} "
        f"d3_max3_out {d3_cost(*max3_out)} "
        f"rho3_max3_out {rho3_cost(*max3_out)}"
    )
    print(
        f"c2d3_df_out {c2d3_cost(*df_out)} "
        f"d3_extra_df_out {int(d3_extra(*df_out))} "
        f"df_extra_df_out {int(df_extra(*df_out))}"
    )
    print(f"max3_out_live_hops {in_ball_new}")
    print(f"witness_skip_c2d3 {path_cost(WITNESS_SKIP, c2d3_cost)}")
    print(f"witness_later_c2d3 {path_cost(WITNESS_LATER, c2d3_cost)}")
    print(f"witness_far_axis_c2d3 {path_cost(WITNESS_FAR_AXIS, c2d3_cost)}")
    print(
        f"witness_rho3_axis8_c2d3 {path_cost(WITNESS_RHO3_AXIS8, c2d3_cost)} "
        f"rho3 {path_cost(WITNESS_RHO3_AXIS8, rho3_cost)}"
    )

    all_reverse = True
    available = True
    products: list[str] = []
    for k in SCALES:
        axis = (2 * k, 0, 0)
        body = (k, k, k)
        in_ball = l1(axis) <= 12 and l1(body) <= 12
        available = available and in_ball
        t_axis = dist[axis]
        t_body = dist[body]
        axis_path = path_cost(WITNESS_AXIS[k], c2d3_cost)
        body_path = path_cost(WITNESS_BODY[k], c2d3_cost)
        lhs = 3 * t_axis * t_axis
        rhs = 4 * t_body * t_body
        reverse = lhs > rhs
        all_reverse = all_reverse and reverse
        product = f"{lhs} > {rhs}"
        products.append(product)
        print(
            f"k {k} t({2 * k},0,0) {t_axis} t({k},{k},{k}) {t_body} "
            f"t_axis^2/(4k^2) {t_axis * t_axis}/{4 * k * k} "
            f"t_body^2/(3k^2) {t_body * t_body}/{3 * k * k} "
            f"3t_axis^2 {lhs} 4t_body^2 {rhs} reverse {reverse}"
        )
        checks.check(
            f"t-k{k}",
            f"t({2 * k},0,0) and t({k},{k},{k}) match Dijkstra and explicit walks",
            in_ball
            and t_axis == axis_path
            and t_body == body_path
            and t_axis > 0
            and t_body > 0,
        )
        checks.check(
            f"reverse-k{k}",
            f"t({2 * k},0,0)^2/(4k^2) > t({k},{k},{k})^2/(3k^2) holds",
            reverse and lhs > rhs and product in note,
        )

    checks.check(
        "one-dijkstra",
        "exactly one Dijkstra from the origin is executed",
        DIJKSTRA_CALLS == 1 and "dijkstra_c2d3" in source,
    )
    checks.check(
        "ball-b12",
        "B_12(0) has 2625 sites and 2624 nonzero sites",
        len(sites) == 2625
        and len(nonzero) == 2624
        and all(l1(v) <= 12 for v in sites),
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
        "reverse-holds-all",
        "doubled pairing reverse holds at every available k=1..4",
        all_reverse,
    )
    checks.check(
        "note-records-times",
        "note records the eight computed arrivals",
        all(
            f"`{path_cost(WITNESS_AXIS[k], c2d3_cost)}`" in note
            and f"`{path_cost(WITNESS_BODY[k], c2d3_cost)}`" in note
            for k in SCALES
        )
        and "`(2,0,0)`" in note
        and "`(6,0,0)`" in note
        and "`(8,0,0)`" in note
        and "`(4,4,4)`" in note,
    )
    checks.check(
        "note-records-reverse-products",
        "note records the four integer reverse products",
        all(product in note for product in products),
    )
    checks.check(
        "hop-unit-out-skipped",
        "the extra clause skips (1,1,0) to (2,1,0); rho3 already prices that hop",
        not d3_extra(*unit_out)
        and omega_extra(*unit_out)
        and max_abs((1, 1, 0)) == 1
        and rho3_cost(*unit_out) == 3
        and c2d3_cost(*unit_out) == 3
        and unit_out[0] in dist
        and unit_out[1] in dist,
    )
    checks.check(
        "hop-df-out-skipped",
        "the named 2-to-2 growing-max clause with source max at least 3 skips (2,2,0) to (3,2,0)",
        not d3_extra(*df_out)
        and df_extra(*df_out)
        and rho3_cost(*df_out) == 1
        and c2d3_cost(*df_out) == 1
        and max_abs((2, 2, 0)) == 2
        and df_out[0] in dist
        and df_out[1] in dist,
    )
    checks.check(
        "hop-max3-out-clause",
        "the named 2-to-2 growing-max clause with source max at least 3 prices (3,2,0) to (4,2,0) at 2",
        d3_extra(*max3_out)
        and rho3_cost(*max3_out) == 1
        and d3_cost(*max3_out) == 3
        and c2d3_cost(*max3_out) == 2
        and max_abs((3, 2, 0)) >= 3
        and max3_out[0] in dist
        and max3_out[1] in dist
        and "cannot price the max≥3 out-face hop" in note,
    )
    checks.check(
        "max3-out-live-on-ball",
        "nearest-neighbor hops inside B_12(0) trigger the extra cost-2 clause",
        in_ball_new > 0 and "new clause is live" in note,
    )
    checks.check(
        "hop-body-last-untaxed",
        "the 2-to-3 hop into (1,1,1) is not priced by the extra clause",
        c2d3_cost(*body_last) == 1
        and rho3_cost(*body_last) == 1
        and unit_coord_count((1, 1, 1)) == 3,
    )
    checks.check(
        "live-arrival-uses-cost-2",
        "the same Dijkstra records t(3,2,0)=9 and t(4,2,0)=11 matching the extra hop of cost 2",
        t320 == 9
        and t420 == 11
        and t320 == path_cost(WITNESS_SKIP, c2d3_cost)
        and t420 == path_cost(WITNESS_LATER, c2d3_cost)
        and t320 + c2d3_cost(*max3_out) == t420
        and "t(3,2,0) = 9" in note
        and "t(4,2,0) = 11" in note,
    )
    checks.check(
        "not-leftover-of-rho3",
        "c2d3 prices max>=3 out-face growth at 2 while rho3 prices it at 1",
        c2d3_cost(*max3_out) == 2
        and rho3_cost(*max3_out) == 1
        and dist[(8, 0, 0)] == 24
        and path_cost(WITNESS_RHO3_AXIS8, rho3_cost) == 20
        and path_cost(WITNESS_RHO3_AXIS8, c2d3_cost) == 25
        and "24` versus `20" in note,
    )
    checks.check(
        "not-leftover-of-b11",
        "(4,4,4) lies outside B_11(0) and the note says so",
        l1((4, 4, 4)) == 12
        and (4, 4, 4) in dist
        and t1200 == 33
        and t1200 == path_cost(WITNESS_FAR_AXIS, c2d3_cost)
        and "absent from `B_11(0)`" in note
        and "t(12,0,0) = 33" in note,
    )
    checks.check(
        "c2d3-clauses",
        "seed-exit, axis, drop, corridor-slide, and ridge-slide cost 3; max>=3 out-face costs 2; df-out extra is idle; 1-to-2 and small 2-to-3 cost 1",
        c2d3_cost((0, 0, 0), (1, 0, 0)) == 3
        and c2d3_cost((1, 0, 0), (2, 0, 0)) == 3
        and c2d3_cost((1, 1, 0), (1, 0, 0)) == 3
        and c2d3_cost((1, 1, 0), (2, 1, 0)) == 3
        and c2d3_cost(*ridge_slide) == 3
        and c2d3_cost(*max3_out) == 2
        and c2d3_cost(*later_out) == 2
        and c2d3_cost((1, 0, 0), (1, 1, 0)) == 1
        and c2d3_cost((1, 1, 0), (1, 1, 1)) == 1
        and c2d3_cost(*interior_hop) == 1
        and c2d3_cost(*df_out) == 1
        and not d3_extra(*df_out)
        and not d3_extra(*unit_out),
    )
    checks.check(
        "thm3-not-in-admissibility",
        "the live Admissibility wording is unchanged and does not name c2d3",
        "There is one fixed nearest-neighbor admissibility rule" in axiom
        and "c2d3(v→w)" not in axiom
        and "Do not write c2d3 into Admissibility." in note
        and "unit hop-cost" not in note.lower(),
    )
    checks.check(
        "scope-boundary",
        "the theorem stays on B_12(0) and proposes no axiom edit",
        "B_12(0)" in note
        and 'hypothetical_axiom_status: "no edit"' in note
        and "one Dijkstra" in note
        and "not leftover of a larger-ball table" in note,
    )
    checks.check(
        "axiom-untouched",
        "the axiom memo is an input only and still names the four axioms",
        "### Admissibility / Local Constraint" in axiom
        and "c2d3(v→w)" not in axiom
        and "ρ3(v→w)" not in axiom,
    )

    print("per_element: named hop-cost values are 1, 2, or 3 on nearest-neighbor hops.")
    print(
        "per_site: arrival times are reported at the doubled pairing sites "
        "and (12,0,0)."
    )
    print("lattice_wide: checked and not executed — the search stays inside B_12(0).")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
