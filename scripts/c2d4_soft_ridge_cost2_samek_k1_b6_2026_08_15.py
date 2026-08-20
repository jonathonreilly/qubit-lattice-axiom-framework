#!/usr/bin/env python3
"""Same-k reverse at k=1 under the named c2d4-plus-soft-ridge hop-cost on B_6(0).

One Dijkstra from the origin on the finite nearest-neighbor graph. The
c2d4-plus-soft-ridge hop-cost is displayed, not adopted, and is not
written into Admissibility. No cache or governance surface is written.
"""

from __future__ import annotations

import ast
import heapq
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "C2D4_SOFT_RIDGE_COST2_SAMEK_K1_B6_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/C2D4_SOFT_RIDGE_COST2_SAMEK_K1_B6_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

CLAIM_SCOPE = (
    "Same-k reverse at k=1 under the named c2d4-plus-soft-ridge "
    "hop-cost on B_6(0) is reported. Displayed, not adopted."
)

RADIUS = 6
AXIS = (1, 0, 0)
BODY = (1, 1, 1)
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
INTERIOR_SRC = (2, 2, 1)
INTERIOR_DST = (2, 2, 2)
STEPS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
Site = tuple[int, int, int]


def add(site: Site, step: Site) -> Site:
    return (site[0] + step[0], site[1] + step[1], site[2] + step[2])


def support_size(site: Site) -> int:
    return sum(1 for coordinate in site if coordinate != 0)


def unit_coord_count(site: Site) -> int:
    return sum(1 for coordinate in site if abs(coordinate) == 1)


def max_abs(site: Site) -> int:
    return max(abs(coordinate) for coordinate in site)


def min_nonzero_abs(site: Site) -> int | None:
    nonzero = [abs(coordinate) for coordinate in site if coordinate != 0]
    if not nonzero:
        return None
    return min(nonzero)


def ball_sites(radius: int) -> frozenset[Site]:
    return frozenset(
        (x, y, z)
        for x in range(-radius, radius + 1)
        for y in range(-radius, radius + 1)
        for z in range(-radius, radius + 1)
        if abs(x) + abs(y) + abs(z) <= radius
    )


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


def ridge_stay_extra(source: Site, dest: Site) -> bool:
    return (
        support_size(source) == 3
        and support_size(dest) == 3
        and unit_coord_count(dest) == 2
    )


def s2_cost(source: Site, dest: Site) -> int:
    if mu_cost(source, dest) == 3:
        return 3
    if ridge_stay_extra(source, dest) or c2d4_cost(source, dest) == 2:
        return 2
    return 1


class DijkstraCounter:
    def __init__(self) -> None:
        self.calls = 0

    def distances(self, sites: frozenset[Site], origin: Site) -> dict[Site, int]:
        self.calls += 1
        infinity = 10**9
        dist = {site: infinity for site in sites}
        dist[origin] = 0
        queue: list[tuple[int, Site]] = [(0, origin)]
        while queue:
            cost, site = heapq.heappop(queue)
            if cost != dist[site]:
                continue
            for step in STEPS:
                neighbor = add(site, step)
                if neighbor not in dist:
                    continue
                candidate = cost + s2_cost(site, neighbor)
                if candidate < dist[neighbor]:
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
        "nearest-neighbor graph B_6(0) only"
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
        "claim_boundary: same-k reverse at k=1 is displayed, not adopted"
    )

    sites = ball_sites(RADIUS)
    origin = (0, 0, 0)
    counter = DijkstraCounter()
    dist = counter.distances(sites, origin)
    t_axis = dist[AXIS]
    t_body = dist[BODY]
    t320 = dist[MAX3_OUT_SRC]
    t420 = dist[MAX3_OUT_DST]
    t211 = dist[RIDGE_DST]
    t222 = dist[INTERIOR_DST]
    reverse = 3 * t_axis * t_axis > t_body * t_body
    axis_sq = t_axis * t_axis
    body_sq = t_body * t_body

    print(f"n_sites {len(sites)}")
    print(f"t(1,0,0) = {t_axis}")
    print(f"t(1,1,1) = {t_body}")
    print(
        f"same-k comparison: {t_axis}^2 / 1 = {axis_sq} versus "
        f"{t_body}^2 / 3 = {body_sq}/3; reverse={reverse}"
    )
    print(f"3 t(1,0,0)^2 = {3 * axis_sq}")
    print(f"t(1,1,1)^2 = {body_sq}")
    print(f"t(3,2,0) = {t320}")
    print(f"t(4,2,0) = {t420}")
    print(f"t(2,1,1) = {t211}")
    print(f"t(2,2,2) = {t222}")
    print(f"dijkstra_calls {counter.calls}")
    print(
        f"s2_unit_out {s2_cost(FACE, UNIT_OUT)} "
        f"c2d4_unit_out {c2d4_cost(FACE, UNIT_OUT)} "
        f"rho3_unit_out {rho3_cost(FACE, UNIT_OUT)} "
        f"mu_unit_out {mu_cost(FACE, UNIT_OUT)}"
    )
    print(
        f"s2_max4_out {s2_cost(MAX4_OUT_SRC, MAX4_OUT_DST)} "
        f"c2d4_max4_out {c2d4_cost(MAX4_OUT_SRC, MAX4_OUT_DST)} "
        f"rho3_max4_out {rho3_cost(MAX4_OUT_SRC, MAX4_OUT_DST)}"
    )
    print(
        f"s2_ridge {s2_cost(RIDGE_SRC, RIDGE_DST)} "
        f"c2d4_ridge {c2d4_cost(RIDGE_SRC, RIDGE_DST)} "
        f"rho3_ridge {rho3_cost(RIDGE_SRC, RIDGE_DST)} "
        f"mu_ridge {mu_cost(RIDGE_SRC, RIDGE_DST)} "
        f"ridge_stay_extra {int(ridge_stay_extra(RIDGE_SRC, RIDGE_DST))}"
    )
    print(
        f"s2_interior {s2_cost(INTERIOR_SRC, INTERIOR_DST)} "
        f"c2d4_interior {c2d4_cost(INTERIOR_SRC, INTERIOR_DST)} "
        f"rho3_interior {rho3_cost(INTERIOR_SRC, INTERIOR_DST)} "
        f"ridge_stay_interior {int(ridge_stay_extra(INTERIOR_SRC, INTERIOR_DST))}"
    )

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/C2D4_SOFT_RIDGE_COST2_SAMEK_K1_B6_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
        "B_6(0) is the 377-site integer set with coordinate-sum at most 6",
        len(sites) == 377 and origin in sites and AXIS in sites and BODY in sites,
    )
    checks.check(
        "one-dijkstra",
        "exactly one Dijkstra from the origin is executed",
        counter.calls == 1 and "DijkstraCounter" in self_source,
    )
    checks.check(
        "reachable",
        "every site of B_6(0) is reached",
        all(dist[site] < 10**9 for site in sites),
    )
    checks.check(
        "hop-origin",
        "the unique origin hop has named cost 3",
        s2_cost(origin, AXIS) == 3 and nu_cost(origin, AXIS) == 3,
    )
    checks.check(
        "hop-axis-axis",
        "a same-support axis hop has named cost 3",
        s2_cost(AXIS, (2, 0, 0)) == 3,
    )
    checks.check(
        "hop-support-rise",
        "the displayed body path keeps cost 1 on the 1-to-2 and 2-to-3 hops",
        s2_cost(AXIS, FACE) == 1 and s2_cost(FACE, BODY) == 1,
    )
    checks.check(
        "hop-ridge-stay-clause",
        "the named 3-to-3 dest two-unit clause prices (1,1,1) to (2,1,1) at 2",
        ridge_stay_extra(RIDGE_SRC, RIDGE_DST)
        and mu_cost(RIDGE_SRC, RIDGE_DST) == 1
        and rho3_cost(RIDGE_SRC, RIDGE_DST) == 3
        and c2d4_cost(RIDGE_SRC, RIDGE_DST) == 3
        and s2_cost(RIDGE_SRC, RIDGE_DST) == 2
        and unit_coord_count(RIDGE_DST) == 2
        and RIDGE_SRC in sites
        and RIDGE_DST in sites,
    )
    checks.check(
        "hop-interior-idle",
        "the named ridge-stay clause skips (2,2,1) to (2,2,2) because dest has no unit coordinate",
        not ridge_stay_extra(INTERIOR_SRC, INTERIOR_DST)
        and unit_coord_count(INTERIOR_DST) == 0
        and rho3_cost(INTERIOR_SRC, INTERIOR_DST) == 1
        and c2d4_cost(INTERIOR_SRC, INTERIOR_DST) == 1
        and s2_cost(INTERIOR_SRC, INTERIOR_DST) == 1
        and INTERIOR_SRC in sites
        and INTERIOR_DST in sites,
    )
    checks.check(
        "hop-max4-out-clause",
        "c2d4 still prices (4,2,0) to (5,2,0) at 2, so s2 does as well",
        d4_extra(MAX4_OUT_SRC, MAX4_OUT_DST)
        and rho3_cost(MAX4_OUT_SRC, MAX4_OUT_DST) == 1
        and c2d4_cost(MAX4_OUT_SRC, MAX4_OUT_DST) == 2
        and s2_cost(MAX4_OUT_SRC, MAX4_OUT_DST) == 2
        and not ridge_stay_extra(MAX4_OUT_SRC, MAX4_OUT_DST)
        and MAX4_OUT_SRC in sites
        and MAX4_OUT_DST not in sites,
    )
    in_ball_ridge = 0
    in_ball_cost2 = 0
    in_ball_c2d4_new = 0
    for site in sites:
        for step in STEPS:
            neighbor = add(site, step)
            if neighbor not in sites:
                continue
            if s2_cost(site, neighbor) == 2:
                in_ball_cost2 += 1
            if ridge_stay_extra(site, neighbor) and mu_cost(site, neighbor) != 3:
                in_ball_ridge += 1
            if d4_extra(site, neighbor) and rho3_cost(site, neighbor) == 1:
                in_ball_c2d4_new += 1
    checks.check(
        "ridge-in-ball-tax",
        "in-ball s2=2 hops are exactly the 3-to-3 dest two-unit ridge-stay hops; c2d4 adds none",
        in_ball_cost2 == in_ball_ridge
        and in_ball_ridge > 0
        and in_ball_c2d4_new == 0,
    )
    checks.check(
        "s2-clauses",
        "seed-exit, axis, drop, and corridor-slide cost 3; ridge-stay and max>=4 out-face cost 2; body last hop costs 1",
        s2_cost((0, 0, 0), (1, 0, 0)) == 3
        and s2_cost((1, 0, 0), (2, 0, 0)) == 3
        and s2_cost((1, 1, 0), (1, 0, 0)) == 3
        and s2_cost((1, 1, 0), (2, 1, 0)) == 3
        and s2_cost((1, 1, 1), (2, 1, 1)) == 2
        and s2_cost((2, 2, 1), (2, 2, 2)) == 1
        and s2_cost((4, 2, 0), (5, 2, 0)) == 2
        and s2_cost((4, 1, 0), (5, 1, 0)) == 3
        and s2_cost((1, 0, 0), (1, 1, 0)) == 1
        and s2_cost((1, 1, 0), (1, 1, 1)) == 1
        and s2_cost((2, 2, 0), (3, 2, 0)) == 1
        and s2_cost((3, 2, 0), (4, 2, 0)) == 1
        and s2_cost((2, 2, 2), (1, 2, 2)) == 1
        and ridge_stay_extra((1, 1, 1), (2, 1, 1))
        and not ridge_stay_extra((2, 2, 1), (2, 2, 2)),
    )
    axis_path_cost = s2_cost(origin, AXIS)
    body_path_cost = (
        s2_cost(origin, AXIS)
        + s2_cost(AXIS, FACE)
        + s2_cost(FACE, BODY)
    )
    ridge_path_cost = body_path_cost + s2_cost(BODY, RIDGE_DST)
    interior_path_cost = (
        ridge_path_cost
        + s2_cost(RIDGE_DST, INTERIOR_SRC)
        + s2_cost(INTERIOR_SRC, INTERIOR_DST)
    )
    checks.check(
        "thm1-axis-time",
        "t(1,0,0) equals the computed origin-to-axis arrival time",
        t_axis == axis_path_cost and t_axis > 0,
    )
    checks.check(
        "thm1-body-time",
        "t(1,1,1) equals the computed origin-to-body arrival time",
        t_body == body_path_cost and t_body > 0,
    )
    checks.check(
        "thm2-reverse-holds",
        "t(1,0,0)^2 / 1 > t(1,1,1)^2 / 3 holds on the computed times",
        reverse and 3 * t_axis * t_axis > t_body * t_body,
    )
    checks.check(
        "thm1-note-reports-times",
        "the note reports the computed arrival times",
        f"t(1,0,0) = {t_axis}" in note and f"t(1,1,1) = {t_body}" in note,
    )
    checks.check(
        "thm2-note-reports-comparison",
        "the note reports the integer same-k comparison and does not adopt it",
        f"{axis_sq} > {body_sq}/3" in note
        and f"{3 * axis_sq} > {body_sq}" in note
        and "Displayed, not adopted" in note,
    )
    checks.check(
        "thm3-not-in-admissibility",
        "the live Admissibility wording is unchanged and does not name s2",
        "There is one fixed nearest-neighbor admissibility rule" in axiom
        and "s2(v→w)" not in axiom
        and "Do not write s2 into Admissibility." in note,
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
        "the theorem stays on B_6(0) and proposes no axiom edit",
        "B_6(0)" in note
        and 'hypothetical_axiom_status: "no edit"' in note
        and "one Dijkstra" in note
        and "not leftover of a larger-ball table" in note,
    )
    checks.check(
        "displayed-not-adopted",
        "the rule is displayed, not adopted",
        "Displayed, not adopted" in note
        and "cheapens body" in note
        and "s2` equals `3` if `μ" in note,
    )
    checks.check(
        "no-axiom-edit",
        "note records hypothetical axiom status no edit",
        'hypothetical_axiom_status: "no edit"' in note,
    )
    checks.check(
        "ridge-arrival",
        "the same Dijkstra records t(2,1,1) matching the ridge-stay extra hop of cost 2",
        t211 == ridge_path_cost
        and t211 == t_body + 2
        and f"t(2,1,1) = {t211}" in note,
    )
    checks.check(
        "interior-arrival",
        "the same Dijkstra records t(2,2,2) matching the idle interior hop of cost 1",
        t222 == interior_path_cost
        and t222 == t211 + s2_cost(RIDGE_DST, INTERIOR_SRC) + 1
        and f"t(2,2,2) = {t222}" in note,
    )
    checks.check(
        "skipped-max3-arrival",
        "the same Dijkstra records t(3,2,0)=9 and t(4,2,0)=10 matching the skipped extra hop of cost 1",
        t320 == 9
        and t420 == 10
        and t320 + s2_cost(MAX3_OUT_SRC, MAX3_OUT_DST) == t420
        and "t(3,2,0) = 9" in note
        and "t(4,2,0) = 10" in note,
    )
    checks.check(
        "axiom-untouched",
        "the axiom memo is an input only and still names the four axioms",
        "### Admissibility / Local Constraint" in axiom
        and "s2(v→w)" not in axiom
        and "c2d4(v→w)" not in axiom
        and "ρ3(v→w)" not in axiom,
    )

    print("per_element: named hop-cost values are 1, 2, or 3 on nearest-neighbor hops.")
    print("per_site: arrival times are reported only at (1,0,0) and (1,1,1).")
    print("lattice_wide: checked and not executed — the search stays inside B_6(0).")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
