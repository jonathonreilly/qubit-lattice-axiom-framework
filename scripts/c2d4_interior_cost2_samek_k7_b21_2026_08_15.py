#!/usr/bin/env python3
"""Same-k reverse at k=7 under the named c2d4-plus-interior hop-cost on B_21(0).

One Dijkstra from the origin on the finite nearest-neighbor graph. The
named hop-cost i2 is displayed, not adopted, and is not written into
Admissibility. No cache or governance surface is written.
"""

from __future__ import annotations

import ast
import heapq
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/C2D4_INTERIOR_COST2_SAMEK_K7_B21_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

AUDIT_INPUT_PATHS = (
    "docs/C2D4_INTERIOR_COST2_SAMEK_K7_B21_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

CLAIM_SCOPE = (
    "Same-k reverse at k=7 under the named c2d4-plus-interior "
    "hop-cost on B_21(0) is reported. Displayed, not adopted."
)

RADIUS = 21
AXIS = (7, 0, 0)
BODY = (7, 7, 7)
ORIGIN = (0, 0, 0)
FACE = (1, 1, 0)
UNIT_OUT = (2, 1, 0)
DF_OUT_SRC = (2, 2, 0)
DF_OUT_DST = (3, 2, 0)
MAX3_OUT_SRC = (3, 2, 0)
MAX3_OUT_DST = (4, 2, 0)
MAX4_OUT_SRC = (4, 2, 0)
MAX4_OUT_DST = (5, 2, 0)
MAX4_LIVE_SRC = (4, 1, 0)
MAX4_LIVE_DST = (5, 1, 0)
RIDGE_SRC = (1, 1, 1)
RIDGE_DST = (2, 1, 1)
INT_SRC = (2, 2, 2)
INT_DST = (3, 2, 2)
IOTA_INT_SRC = (2, 2, 1)
IOTA_INT_DST = (2, 2, 2)
HEIGHT_M_SRC = (3, 2, 2)
HEIGHT_M_DST = (4, 2, 2)
CUBE_SRC = (3, 3, 2)
CUBE_DST = (3, 3, 3)
STEPS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
Site = tuple[int, int, int]


def add(site: Site, step: Site) -> Site:
    return (site[0] + step[0], site[1] + step[1], site[2] + step[2])


def l1(site: Site) -> int:
    return abs(site[0]) + abs(site[1]) + abs(site[2])


def support_size(site: Site) -> int:
    return sum(1 for coordinate in site if coordinate != 0)


def unit_coord_count(site: Site) -> int:
    return sum(1 for coordinate in site if abs(coordinate) == 1)


def max_abs(site: Site) -> int:
    return max(abs(coordinate) for coordinate in site)


def min_abs(site: Site) -> int:
    return min(abs(coordinate) for coordinate in site)


def min_nonzero_abs(site: Site) -> int | None:
    nonzero = [abs(coordinate) for coordinate in site if coordinate != 0]
    if not nonzero:
        return None
    return min(nonzero)


def ball_sites(radius: int) -> list[Site]:
    sites: list[Site] = []
    for x in range(-radius, radius + 1):
        for y in range(-radius, radius + 1):
            rem = radius - abs(x) - abs(y)
            for z in range(-rem, rem + 1):
                sites.append((x, y, z))
    return sites


def nu_cost(source: Site, dest: Site) -> int:
    source_support = support_size(source)
    dest_support = support_size(dest)
    if (
        source_support == 0
        or (source_support == 1 and dest_support == 1)
        or dest_support < source_support
    ):
        return 3
    return 1


def mu_cost(source: Site, dest: Site) -> int:
    if nu_cost(source, dest) == 3:
        return 3
    if support_size(source) == 2 and support_size(dest) == 2:
        least = min_nonzero_abs(dest)
        if least == 1:
            return 3
    return 1


def rho3_cost(source: Site, dest: Site) -> int:
    if mu_cost(source, dest) == 3:
        return 3
    if support_size(source) == 3 and support_size(dest) == 3:
        if unit_coord_count(dest) == 2:
            return 3
    return 1


def d4_extra(source: Site, dest: Site) -> bool:
    return (
        support_size(source) == 2
        and support_size(dest) == 2
        and max_abs(dest) > max_abs(source)
        and max_abs(source) >= 4
    )


def d3_extra(source: Site, dest: Site) -> bool:
    return (
        support_size(source) == 2
        and support_size(dest) == 2
        and max_abs(dest) > max_abs(source)
        and max_abs(source) >= 3
    )


def c2d4_cost(source: Site, dest: Site) -> int:
    if rho3_cost(source, dest) == 3:
        return 3
    if d4_extra(source, dest):
        return 2
    return 1


def interior_extra(source: Site, dest: Site) -> bool:
    return (
        support_size(source) == 3
        and support_size(dest) == 3
        and min_abs(dest) >= 2
    )


def iota_extra(source: Site, dest: Site) -> bool:
    if support_size(source) != 3 or support_size(dest) != 3:
        return False
    least = min_abs(dest)
    if least < 2:
        return False
    equal_min = sum(1 for coordinate in dest if abs(coordinate) == least)
    return equal_min != 2


def iota_cost(source: Site, dest: Site) -> int:
    if rho3_cost(source, dest) == 3:
        return 3
    if iota_extra(source, dest):
        return 3
    return 1


def i2_cost(source: Site, dest: Site) -> int:
    if rho3_cost(source, dest) == 3:
        return 3
    if c2d4_cost(source, dest) == 2 or interior_extra(source, dest):
        return 2
    return 1


class DijkstraCounter:
    def __init__(self) -> None:
        self.calls = 0

    def distances(self, sites: list[Site], origin: Site) -> dict[Site, int]:
        self.calls += 1
        site_set = set(sites)
        dist: dict[Site, int] = {origin: 0}
        queue: list[tuple[int, Site]] = [(0, origin)]
        seen: set[Site] = set()
        while queue:
            cost, site = heapq.heappop(queue)
            if site in seen:
                continue
            seen.add(site)
            for step in STEPS:
                neighbor = add(site, step)
                if neighbor not in site_set:
                    continue
                candidate = cost + i2_cost(site, neighbor)
                if candidate < dist.get(neighbor, 10**9):
                    dist[neighbor] = candidate
                    heapq.heappush(queue, (candidate, neighbor))
        return dist


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool) -> None:
        if condition:
            self.passed += 1
        else:
            self.failed += 1
        print(f"{'PASS' if condition else 'FAIL'}: {label} {statement}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


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
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    self_source = Path(__file__).read_text(encoding="utf-8")

    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print("cache_write: false")
    print(f"claim_scope: {CLAIM_SCOPE}")
    print(
        "external_scientific_inputs: none; named hop-cost on the finite "
        "nearest-neighbor graph B_21(0) only"
    )
    print(
        "measure_boundary: integer hop-costs and one Dijkstra; no fit and "
        "no second graph search"
    )

    sites = ball_sites(RADIUS)
    site_set = set(sites)
    counter = DijkstraCounter()
    dist = counter.distances(sites, ORIGIN)
    t_axis = dist[AXIS]
    t_body = dist[BODY]
    t2100 = dist[(21, 0, 0)]
    t1800 = dist[(18, 0, 0)]
    t320 = dist[MAX3_OUT_SRC]
    t420 = dist[MAX3_OUT_DST]
    t520 = dist[MAX4_OUT_DST]
    t222 = dist[INT_SRC]
    t322 = dist[INT_DST]
    reverse = 3 * t_axis * t_axis > t_body * t_body
    axis_sq = t_axis * t_axis
    body_sq = t_body * t_body

    print(f"n_sites {len(sites)}")
    print(f"t(7,0,0) = {t_axis}")
    print(f"t(7,7,7) = {t_body}")
    print(
        f"same-k comparison: {t_axis}^2 / 49 = {axis_sq}/49 versus "
        f"{t_body}^2 / 147 = {body_sq}/147; reverse={reverse}"
    )
    print(f"3 t(7,0,0)^2 = {3 * axis_sq}")
    print(f"t(7,7,7)^2 = {body_sq}")
    print(f"t(21,0,0) = {t2100}")
    print(f"t(18,0,0) = {t1800}")
    print(f"t(3,2,0) = {t320}")
    print(f"t(4,2,0) = {t420}")
    print(f"t(5,2,0) = {t520}")
    print(f"t(2,2,2) = {t222}")
    print(f"t(3,2,2) = {t322}")
    print(f"dijkstra_calls {counter.calls}")

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required string-literal tuple",
        AUDIT_INPUT_PATHS == (NOTE_REL, AXIOM_REL)
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file(),
    )
    checks.check(
        "audit-input-literal",
        "AUDIT_INPUT_PATHS is a static string-literal tuple",
        literal_audit_paths(self_source) == AUDIT_INPUT_PATHS,
    )
    checks.check(
        "ball-cardinality",
        "B_21(0) is the 13287-site integer set with coordinate-sum at most 21",
        len(sites) == 13287
        and ORIGIN in site_set
        and AXIS in site_set
        and BODY in site_set
        and all(l1(site) <= RADIUS for site in sites),
    )
    checks.check(
        "one-dijkstra",
        "exactly one Dijkstra from the origin is executed",
        counter.calls == 1 and "DijkstraCounter" in self_source,
    )
    checks.check(
        "reachable",
        "every site of B_21(0) is reached",
        len(dist) == 13287 and all(dist[site] < 10**9 for site in sites),
    )
    checks.check(
        "hop-origin",
        "the unique origin hop has named cost 3",
        i2_cost(ORIGIN, (1, 0, 0)) == 3 and nu_cost(ORIGIN, (1, 0, 0)) == 3,
    )
    checks.check(
        "hop-max4-out-clause",
        "c2d4 would be 2 on (4,2,0) to (5,2,0), so i2 prices that hop at 2",
        d4_extra(MAX4_OUT_SRC, MAX4_OUT_DST)
        and rho3_cost(MAX4_OUT_SRC, MAX4_OUT_DST) == 1
        and c2d4_cost(MAX4_OUT_SRC, MAX4_OUT_DST) == 2
        and i2_cost(MAX4_OUT_SRC, MAX4_OUT_DST) == 2
        and MAX4_OUT_SRC in site_set
        and MAX4_OUT_DST in site_set,
    )
    checks.check(
        "hop-interior-clause",
        "a 3-to-3 hop whose dest min abs coord is at least 2 is priced at 2",
        interior_extra(INT_SRC, INT_DST)
        and rho3_cost(INT_SRC, INT_DST) == 1
        and c2d4_cost(INT_SRC, INT_DST) == 1
        and i2_cost(INT_SRC, INT_DST) == 2
        and min_abs(INT_DST) >= 2
        and INT_SRC in site_set
        and INT_DST in site_set,
    )
    checks.check(
        "hop-max3-out-skipped",
        "the max>=4 out-face clause skips (3,2,0) to (4,2,0)",
        not d4_extra(MAX3_OUT_SRC, MAX3_OUT_DST)
        and d3_extra(MAX3_OUT_SRC, MAX3_OUT_DST)
        and rho3_cost(MAX3_OUT_SRC, MAX3_OUT_DST) == 1
        and i2_cost(MAX3_OUT_SRC, MAX3_OUT_DST) == 1
        and MAX3_OUT_SRC in site_set
        and MAX3_OUT_DST in site_set,
    )
    checks.check(
        "i2-clauses",
        "seed-exit, axis, drop, corridor, and ridge cost 3; max>=4 out-face and interior 3-to-3 cost 2; other displayed hops cost 1",
        i2_cost((0, 0, 0), (1, 0, 0)) == 3
        and i2_cost((1, 0, 0), (2, 0, 0)) == 3
        and i2_cost((1, 1, 0), (1, 0, 0)) == 3
        and i2_cost(FACE, UNIT_OUT) == 3
        and i2_cost(RIDGE_SRC, RIDGE_DST) == 3
        and i2_cost(MAX4_OUT_SRC, MAX4_OUT_DST) == 2
        and i2_cost(INT_SRC, INT_DST) == 2
        and i2_cost(HEIGHT_M_SRC, HEIGHT_M_DST) == 2
        and i2_cost(CUBE_SRC, CUBE_DST) == 2
        and i2_cost((1, 0, 0), FACE) == 1
        and i2_cost(FACE, (1, 1, 1)) == 1
        and i2_cost(DF_OUT_SRC, DF_OUT_DST) == 1
        and i2_cost(MAX3_OUT_SRC, MAX3_OUT_DST) == 1
        and i2_cost((2, 1, 1), (2, 1, 2)) == 1,
    )
    in_ball_interior = 0
    in_ball_max4 = 0
    for site in sites:
        for step in STEPS:
            neighbor = add(site, step)
            if neighbor not in site_set:
                continue
            if interior_extra(site, neighbor) and rho3_cost(site, neighbor) == 1:
                in_ball_interior += 1
            if d4_extra(site, neighbor) and rho3_cost(site, neighbor) == 1:
                in_ball_max4 += 1
    checks.check(
        "extras-live-on-ball",
        "both extra i2 clauses fire on in-ball hops",
        in_ball_interior > 0 and in_ball_max4 > 0,
    )
    axis_path_cost = sum(
        i2_cost((k, 0, 0), (k + 1, 0, 0)) for k in range(7)
    )
    body_path = (
        (0, 0, 0),
        (0, 0, 1),
        (0, 1, 1),
        (0, 1, 2),
        (0, 2, 2),
        (0, 2, 3),
        (0, 2, 4),
        (1, 2, 4),
        (1, 2, 5),
        (1, 2, 6),
        (1, 2, 7),
        (1, 3, 7),
        (1, 4, 7),
        (1, 5, 7),
        (1, 6, 7),
        (1, 7, 7),
        (2, 7, 7),
        (3, 7, 7),
        (4, 7, 7),
        (5, 7, 7),
        (6, 7, 7),
        (7, 7, 7),
    )
    body_path_cost = sum(
        i2_cost(a, b) for a, b in zip(body_path, body_path[1:])
    )
    checks.check(
        "thm1-axis-time",
        "t(7,0,0) equals the computed origin-to-axis arrival time",
        t_axis == axis_path_cost and t_axis > 0,
    )
    checks.check(
        "thm1-body-time",
        "t(7,7,7) equals the computed origin-to-body arrival time",
        t_body == body_path_cost and t_body > 0,
    )
    checks.check(
        "thm2-reverse-holds",
        "t(7,0,0)^2 / 49 > t(7,7,7)^2 / 147 holds on the computed times",
        reverse and 3 * t_axis * t_axis > t_body * t_body,
    )
    checks.check(
        "thm1-note-reports-times",
        "the note reports the computed arrival times",
        f"t(7,0,0) = {t_axis}" in note and f"t(7,7,7) = {t_body}" in note,
    )
    checks.check(
        "thm2-note-reports-comparison",
        "the note reports the integer same-k comparison and does not adopt it",
        f"{3 * axis_sq} > {body_sq}" in note
        and "Displayed, not adopted" in note
        and "inequality holds" in note,
    )
    checks.check(
        "not-leftover-of-rho3-or-c2d4",
        "i2 disagrees with rho3 and with c2d4 on in-ball hops, and the arrivals are not the rho3 pair",
        i2_cost(INT_SRC, INT_DST) == 2
        and rho3_cost(INT_SRC, INT_DST) == 1
        and c2d4_cost(INT_SRC, INT_DST) == 1
        and i2_cost(MAX4_OUT_SRC, MAX4_OUT_DST) == 2
        and rho3_cost(MAX4_OUT_SRC, MAX4_OUT_DST) == 1
        and t_axis != 19
        and t_body != 25
        and "cannot price interior body hops" in note
        and "cannot price max≥4 out-face" in note,
    )
    checks.check(
        "not-leftover-of-iota",
        "i2 cheapens interior non-ridge 3-to-3 hops relative to iota and taxes height-m ridges that iota skips",
        iota_cost(IOTA_INT_SRC, IOTA_INT_DST) == 3
        and i2_cost(IOTA_INT_SRC, IOTA_INT_DST) == 2
        and iota_cost(HEIGHT_M_SRC, HEIGHT_M_DST) == 1
        and i2_cost(HEIGHT_M_SRC, HEIGHT_M_DST) == 2
        and iota_cost(CUBE_SRC, CUBE_DST) == 3
        and i2_cost(CUBE_SRC, CUBE_DST) == 2
        and "cannot price the cost-2 interior clause" in note,
    )
    checks.check(
        "not-leftover-of-b18",
        "(7,7,7) lies outside B_18(0) and the note says so",
        l1(BODY) == 21
        and BODY in dist
        and t2100 == 42
        and t1800 == 34
        and "absent from `B_18(0)`" in note
        and "not leftover of the `B_18(0)` times" in note,
    )
    checks.check(
        "thm3-not-in-admissibility",
        "the live Admissibility wording is unchanged and does not name i2",
        "There is one fixed nearest-neighbor admissibility rule" in axiom
        and "i2(v→w)" not in axiom
        and "Do not write i2 into Admissibility." in note,
    )
    checks.check(
        "thm3-no-l1-attachment",
        "the note refuses to attach L1",
        "Do not attach L1." in note and "Do not attach L1." not in axiom,
    )
    forbidden = (
        "G_" + "N",
        "1/" + "r",
        "1/" + "r^2",
        "Lattice-" + "named",
        "not a " + "TOE",
    )
    checks.check(
        "forbidden-tokens",
        "forbidden tokens are absent from the note",
        all(token not in note for token in forbidden),
    )
    checks.check(
        "claim-scope-contract",
        "the required claim_scope is source-visible",
        CLAIM_SCOPE in note.replace("\n", " ") and CLAIM_SCOPE in note,
    )
    checks.check(
        "uniqueness-not-claimed",
        "the note does not claim uniqueness of the named hop-cost",
        "Uniqueness is not claimed" in note and "unique hop-cost" not in note,
    )
    checks.check(
        "scope-boundary",
        "the theorem stays on B_21(0) and proposes no axiom edit",
        "B_21(0)" in note
        and 'hypothetical_axiom_status: "no edit"' in note
        and "one Dijkstra" in note
        and "not leftover of a larger-ball table" in note,
    )
    checks.check(
        "displayed-not-adopted",
        "the rule is displayed, not adopted",
        "Displayed, not adopted" in note,
    )
    checks.check(
        "no-axiom-edit",
        "note records hypothetical axiom status no edit",
        'hypothetical_axiom_status: "no edit"' in note,
    )
    checks.check(
        "axiom-untouched",
        "the axiom memo is an input only and still names the four axioms",
        "### Admissibility / Local Constraint" in axiom
        and "i2(v→w)" not in axiom
        and "c2d4(v→w)" not in axiom,
    )
    checks.check(
        "independent-sites",
        "the same Dijkstra records the skipped max>=3 hop and the live interior and max>=4 arrivals",
        t320 == 9
        and t420 == 10
        and t520 == 12
        and t222 == 11
        and t322 == 12
        and "t(3,2,0) = 9" in note
        and "t(4,2,0) = 10" in note
        and "t(5,2,0) = 12" in note
        and "t(3,2,2) = 12" in note,
    )

    print("per_element: named hop-cost values are 1, 2, or 3 on nearest-neighbor hops.")
    print("per_site: arrival times are reported at (7,0,0) and (7,7,7).")
    print("lattice_wide: checked and not executed — the search stays inside B_21(0).")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
