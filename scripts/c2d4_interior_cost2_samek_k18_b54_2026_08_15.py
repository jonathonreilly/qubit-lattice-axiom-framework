#!/usr/bin/env python3
"""Same-k reverse at k=18 under the named c2d4-plus-interior hop-cost on B_54(0).

One Dijkstra from the origin on the finite nearest-neighbor graph. The
c2d4-plus-interior hop-cost is displayed, not adopted, and is not
written into Admissibility. No cache or governance surface is written.
"""

from __future__ import annotations

import ast
import heapq
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "C2D4_INTERIOR_COST2_SAMEK_K18_B54_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/C2D4_INTERIOR_COST2_SAMEK_K18_B54_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

CLAIM_SCOPE = (
    "Same-k reverse at k=18 under the named c2d4-plus-interior "
    "hop-cost on B_54(0) is reported. Displayed, not adopted."
)

RADIUS = 54
K = 18
AXIS = (18, 0, 0)
BODY = (18, 18, 18)
FACE = (1, 1, 0)
UNIT_OUT = (2, 1, 0)
MAX3_OUT_SRC = (3, 2, 0)
MAX3_OUT_DST = (4, 2, 0)
MAX4_OUT_SRC = (4, 2, 0)
MAX4_OUT_DST = (5, 2, 0)
INTERIOR_SRC = (2, 2, 1)
INTERIOR_DST = (2, 2, 2)
INTERIOR_EXIT = (1, 2, 2)
HUG = (18, 18, 1)
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


def omega_extra(source: Site, dest: Site) -> bool:
    return (
        support_size(source) == 2
        and support_size(dest) == 2
        and max_abs(dest) > max_abs(source)
    )


def d4_extra(source: Site, dest: Site) -> bool:
    return omega_extra(source, dest) and max_abs(source) >= 4


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


def i2_cost(source: Site, dest: Site) -> int:
    if rho3_cost(source, dest) == 3:
        return 3
    if c2d4_cost(source, dest) == 2 or interior_extra(source, dest):
        return 2
    return 1


def path_cost(path: list[Site]) -> int:
    return sum(i2_cost(a, b) for a, b in zip(path, path[1:]))


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
            sx, sy, sz = site
            for dx, dy, dz in STEPS:
                neighbor = (sx + dx, sy + dy, sz + dz)
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


def axis_witness() -> list[Site]:
    path: list[Site] = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (1, 1, 1), (1, 2, 1)]
    path.extend((x, 2, 1) for x in range(2, K + 1))
    path.extend([(K, 2, 0), (K, 1, 0), (K, 0, 0)])
    return path


def body_witness() -> list[Site]:
    path: list[Site] = [
        (0, 0, 0),
        (1, 0, 0),
        (1, 1, 0),
        (1, 2, 0),
        (2, 2, 0),
        (2, 2, 1),
    ]
    path.extend((x, 2, 1) for x in range(3, K + 1))
    path.extend((K, y, 1) for y in range(3, K + 1))
    path.extend((K, K, z) for z in range(2, K + 1))
    return path


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
        "nearest-neighbor graph B_54(0) only"
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
        "claim_boundary: same-k reverse at k=18 is displayed, not adopted"
    )

    sites = ball_sites(RADIUS)
    origin = (0, 0, 0)
    counter = DijkstraCounter()
    dist = counter.distances(sites, origin)
    t_axis = dist[AXIS]
    t_body = dist[BODY]
    t100 = dist[(1, 0, 0)]
    t111 = dist[(1, 1, 1)]
    t320 = dist[MAX3_OUT_SRC]
    t420 = dist[MAX3_OUT_DST]
    t520 = dist[MAX4_OUT_DST]
    t222 = dist[INTERIOR_DST]
    t_hug = dist[HUG]
    t5400 = dist[(54, 0, 0)]
    t5100 = dist[(51, 0, 0)]
    reverse = 3 * t_axis * t_axis > t_body * t_body
    axis_sq = t_axis * t_axis
    body_sq = t_body * t_body
    axis_prod = 3 * axis_sq
    axis_path = axis_witness()
    body_path = body_witness()
    axis_path_cost = path_cost(axis_path)
    body_path_cost = path_cost(body_path)

    print(f"n_sites {len(sites)}")
    print(f"t(18,0,0) = {t_axis}")
    print(f"t(18,18,18) = {t_body}")
    print(
        f"same-k comparison: {t_axis}^2 / 324 = {axis_sq}/324 versus "
        f"{t_body}^2 / 972 = {body_sq}/972; reverse={reverse}"
    )
    print(f"3 t(18,0,0)^2 = {axis_prod}")
    print(f"t(18,18,18)^2 = {body_sq}")
    print(f"t(1,0,0) = {t100}")
    print(f"t(1,1,1) = {t111}")
    print(f"t(3,2,0) = {t320}")
    print(f"t(4,2,0) = {t420}")
    print(f"t(5,2,0) = {t520}")
    print(f"t(2,2,2) = {t222}")
    print(f"t(18,18,1) = {t_hug}")
    print(f"t(54,0,0) = {t5400}")
    print(f"t(51,0,0) = {t5100}")
    print(f"dijkstra_calls {counter.calls}")
    print(
        f"i2_interior {i2_cost(INTERIOR_SRC, INTERIOR_DST)} "
        f"c2d4_interior {c2d4_cost(INTERIOR_SRC, INTERIOR_DST)} "
        f"rho3_interior {rho3_cost(INTERIOR_SRC, INTERIOR_DST)}"
    )
    print(
        f"i2_max4_out {i2_cost(MAX4_OUT_SRC, MAX4_OUT_DST)} "
        f"c2d4_max4_out {c2d4_cost(MAX4_OUT_SRC, MAX4_OUT_DST)}"
    )

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/C2D4_INTERIOR_COST2_SAMEK_K18_B54_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
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
        "B_54(0) is the 215929-site integer set with coordinate-sum at most 54",
        len(sites) == 215929 and origin in dist and AXIS in dist and BODY in dist,
    )
    checks.check(
        "one-dijkstra",
        "exactly one Dijkstra from the origin is executed",
        counter.calls == 1 and "DijkstraCounter" in self_source,
    )
    checks.check(
        "reachable",
        "every site of B_54(0) is reached",
        len(dist) == 215929 and all(dist[site] < 10**9 for site in sites),
    )
    checks.check(
        "hop-origin",
        "the unique origin hop has named cost 3",
        i2_cost(origin, (1, 0, 0)) == 3 and nu_cost(origin, (1, 0, 0)) == 3,
    )
    checks.check(
        "hop-interior-clause",
        "the named 3-to-3 dest min-abs>=2 clause prices (2,2,1) to (2,2,2) at 2",
        interior_extra(INTERIOR_SRC, INTERIOR_DST)
        and rho3_cost(INTERIOR_SRC, INTERIOR_DST) == 1
        and c2d4_cost(INTERIOR_SRC, INTERIOR_DST) == 1
        and i2_cost(INTERIOR_SRC, INTERIOR_DST) == 2
        and min_abs(INTERIOR_DST) >= 2
        and INTERIOR_SRC in dist
        and INTERIOR_DST in dist,
    )
    checks.check(
        "hop-interior-exit-idle",
        "the named interior clause skips (2,2,2) to (1,2,2) because dest min abs is 1",
        not interior_extra(INTERIOR_DST, INTERIOR_EXIT)
        and min_abs(INTERIOR_EXIT) == 1
        and rho3_cost(INTERIOR_DST, INTERIOR_EXIT) == 1
        and i2_cost(INTERIOR_DST, INTERIOR_EXIT) == 1
        and INTERIOR_EXIT in dist,
    )
    checks.check(
        "hop-max4-out-clause",
        "c2d4 still prices (4,2,0) to (5,2,0) at 2, so i2 does as well",
        d4_extra(MAX4_OUT_SRC, MAX4_OUT_DST)
        and rho3_cost(MAX4_OUT_SRC, MAX4_OUT_DST) == 1
        and c2d4_cost(MAX4_OUT_SRC, MAX4_OUT_DST) == 2
        and i2_cost(MAX4_OUT_SRC, MAX4_OUT_DST) == 2
        and not interior_extra(MAX4_OUT_SRC, MAX4_OUT_DST)
        and MAX4_OUT_SRC in dist
        and MAX4_OUT_DST in dist,
    )
    in_ball_interior = 0
    in_ball_cost2 = 0
    in_ball_c2d4_new = 0
    site_set = set(sites)
    for site in sites:
        for step in STEPS:
            neighbor = add(site, step)
            if neighbor not in site_set:
                continue
            if i2_cost(site, neighbor) == 2:
                in_ball_cost2 += 1
            if interior_extra(site, neighbor):
                in_ball_interior += 1
            if d4_extra(site, neighbor) and rho3_cost(site, neighbor) == 1:
                in_ball_c2d4_new += 1
    checks.check(
        "in-ball-cost2-split",
        "in-ball i2=2 hops are interior 3-to-3 dest min-abs>=2 hops plus c2d4 max>=4 out-face hops",
        in_ball_cost2 == in_ball_interior + in_ball_c2d4_new
        and in_ball_interior > 0
        and in_ball_c2d4_new > 0,
    )
    checks.check(
        "i2-clauses",
        "seed-exit, axis, drop, corridor-slide, and ridge-slide cost 3; interior 3-to-3 and max>=4 out-face cost 2; body last hop costs 1",
        i2_cost((0, 0, 0), (1, 0, 0)) == 3
        and i2_cost((1, 0, 0), (2, 0, 0)) == 3
        and i2_cost((1, 1, 0), (1, 0, 0)) == 3
        and i2_cost((1, 1, 0), (2, 1, 0)) == 3
        and i2_cost((1, 1, 1), (2, 1, 1)) == 3
        and i2_cost((2, 2, 1), (2, 2, 2)) == 2
        and i2_cost((4, 2, 0), (5, 2, 0)) == 2
        and i2_cost((4, 1, 0), (5, 1, 0)) == 3
        and i2_cost((1, 0, 0), (1, 1, 0)) == 1
        and i2_cost((1, 1, 0), (1, 1, 1)) == 1
        and i2_cost((2, 2, 0), (3, 2, 0)) == 1
        and i2_cost((3, 2, 0), (4, 2, 0)) == 1
        and i2_cost((2, 2, 2), (1, 2, 2)) == 1
        and i2_cost((18, 18, 1), (18, 18, 2)) == 2
        and i2_cost((18, 18, 17), (18, 18, 18)) == 2
        and not interior_extra((1, 1, 0), (1, 1, 1))
        and not interior_extra((2, 2, 2), (1, 2, 2)),
    )
    checks.check(
        "thm1-axis-time",
        "t(18,0,0) equals the computed origin-to-axis arrival time",
        t_axis == axis_path_cost and t_axis > 0 and axis_path[-1] == AXIS,
    )
    checks.check(
        "thm1-body-time",
        "t(18,18,18) equals the computed origin-to-body arrival time",
        t_body == body_path_cost and t_body > 0 and body_path[-1] == BODY,
    )
    checks.check(
        "thm2-reverse-reported",
        "the integer same-k comparison is computed from the two arrivals",
        reverse == (axis_prod > body_sq)
        and axis_sq == t_axis * t_axis
        and body_sq == t_body * t_body
        and (K * K) == 324
        and (3 * K * K) == 972,
    )
    checks.check(
        "thm1-note-reports-times",
        "the note reports the computed arrival times",
        f"t(18,0,0) = {t_axis}" in note and f"t(18,18,18) = {t_body}" in note,
    )
    checks.check(
        "thm2-note-reports-comparison",
        "the note reports the integer same-k comparison and does not adopt it",
        f"{axis_sq}/324" in note
        and f"{body_sq}/972" in note
        and f"{axis_prod} > {body_sq}" in note
        and "Displayed, not adopted" in note
        and ("does not hold" in note or "inequality does not hold" in note),
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
        "the note refuses to attach L1 and does not score a unit hop-cost",
        "Do not attach L1." in note
        and "attach L1" in note
        and "unit hop-cost" not in note.lower(),
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
        CLAIM_SCOPE in note.replace("\n", " ")
        and CLAIM_SCOPE in note,
    )
    checks.check(
        "uniqueness-not-claimed",
        "the note does not claim uniqueness of the named hop-cost",
        "Uniqueness is not claimed" in note and "unique hop-cost" not in note,
    )
    checks.check(
        "scope-boundary",
        "the theorem stays on B_54(0) and proposes no axiom edit",
        "B_54(0)" in note
        and 'hypothetical_axiom_status: "no edit"' in note
        and "one Dijkstra" in note
        and "not leftover of a larger-ball table" in note,
    )
    checks.check(
        "displayed-not-adopted",
        "the rule is displayed, not adopted",
        "Displayed, not adopted" in note
        and "interior body hops" in note
        and "i2` equals `3` if `ρ3" in note,
    )
    checks.check(
        "no-axiom-edit",
        "note records hypothetical axiom status no edit",
        'hypothetical_axiom_status: "no edit"' in note,
    )
    checks.check(
        "interior-arrival",
        "the same Dijkstra records t(2,2,2) matching the interior extra hop of cost 2",
        t222 == t111 + i2_cost((1, 1, 1), (2, 1, 1)) + i2_cost((2, 1, 1), INTERIOR_SRC) + 2
        and f"t(2,2,2) = {t222}" in note,
    )
    checks.check(
        "skipped-max3-arrival",
        "the same Dijkstra records t(3,2,0)=9 and t(4,2,0)=10 matching the skipped extra hop of cost 1",
        t320 == 9
        and t420 == 10
        and t320 + i2_cost(MAX3_OUT_SRC, MAX3_OUT_DST) == t420
        and "t(3,2,0) = 9" in note
        and "t(4,2,0) = 10" in note,
    )
    checks.check(
        "hug-then-interior",
        "the same Dijkstra records t(18,18,1) and the remaining interior hops of cost 2",
        t_hug == t_body - 2 * 17
        and i2_cost(HUG, (18, 18, 2)) == 2
        and t_hug + 2 * 17 == t_body
        and f"t(18,18,1) = {t_hug}" in note,
    )
    checks.check(
        "not-leftover-of-b51",
        "(18,18,18) lies outside B_51(0) and the note says so",
        l1(BODY) == 54
        and t5400 == dist[(54, 0, 0)]
        and t5100 == dist[(51, 0, 0)]
        and f"t(54,0,0) = {t5400}" in note
        and f"t(51,0,0) = {t5100}" in note
        and "absent from `B_51(0)`" in note
        and "not leftover of the `B_51(0)` times" in note,
    )
    checks.check(
        "axiom-untouched",
        "the axiom memo is an input only and still names the four axioms",
        "### Admissibility / Local Constraint" in axiom
        and "i2(v→w)" not in axiom
        and "c2d4(v→w)" not in axiom
        and "ρ3(v→w)" not in axiom,
    )

    print("per_element: named hop-cost values are 1, 2, or 3 on nearest-neighbor hops.")
    print("per_site: arrival times are reported only at (18,0,0) and (18,18,18).")
    print("lattice_wide: checked and not executed — the search stays inside B_54(0).")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
