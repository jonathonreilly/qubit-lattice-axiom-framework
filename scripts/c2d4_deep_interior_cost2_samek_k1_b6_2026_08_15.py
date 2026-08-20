#!/usr/bin/env python3
"""Same-k reverse at k=1 under the named c2d4-plus-deep-interior hop-cost on B_6(0).

One Dijkstra from the origin on the finite nearest-neighbor graph. The
c2d4-plus-deep-interior hop-cost is displayed, not adopted, and is not
written into Admissibility. No cache or governance surface is written.
"""

from __future__ import annotations

import ast
import heapq
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "C2D4_DEEP_INTERIOR_COST2_SAMEK_K1_B6_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/C2D4_DEEP_INTERIOR_COST2_SAMEK_K1_B6_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

CLAIM_SCOPE = (
    "Same-k reverse at k=1 under the named c2d4-plus-deep-interior "
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
INTERIOR_SRC = (2, 2, 1)
INTERIOR_DST = (2, 2, 2)
INTERIOR_EXIT = (1, 2, 2)
DEEP_SRC = (2, 3, 3)
DEEP_DST = (3, 3, 3)
SHALLOW_DEEP_SRC = (3, 2, 2)
SHALLOW_DEEP_DST = (3, 3, 2)
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


def min_abs(site: Site) -> int:
    return min(abs(coordinate) for coordinate in site)


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


def interior_extra(source: Site, dest: Site) -> bool:
    return (
        support_size(source) == 3
        and support_size(dest) == 3
        and min_abs(dest) >= 2
    )


def deep_interior_extra(source: Site, dest: Site) -> bool:
    return (
        support_size(source) == 3
        and support_size(dest) == 3
        and min_abs(dest) >= 3
    )


def i2_cost(source: Site, dest: Site) -> int:
    if rho3_cost(source, dest) == 3:
        return 3
    if c2d4_cost(source, dest) == 2 or interior_extra(source, dest):
        return 2
    return 1


def j2_cost(source: Site, dest: Site) -> int:
    if rho3_cost(source, dest) == 3:
        return 3
    if c2d4_cost(source, dest) == 2 or deep_interior_extra(source, dest):
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
                candidate = cost + j2_cost(site, neighbor)
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
    t221 = dist[INTERIOR_SRC]
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
    print(f"t(2,2,1) = {t221}")
    print(f"t(2,2,2) = {t222}")
    print(f"dijkstra_calls {counter.calls}")
    print(
        f"j2_unit_out {j2_cost(FACE, UNIT_OUT)} "
        f"c2d4_unit_out {c2d4_cost(FACE, UNIT_OUT)} "
        f"rho3_unit_out {rho3_cost(FACE, UNIT_OUT)}"
    )
    print(
        f"j2_max4_out {j2_cost(MAX4_OUT_SRC, MAX4_OUT_DST)} "
        f"c2d4_max4_out {c2d4_cost(MAX4_OUT_SRC, MAX4_OUT_DST)} "
        f"rho3_max4_out {rho3_cost(MAX4_OUT_SRC, MAX4_OUT_DST)}"
    )
    print(
        f"j2_interior {j2_cost(INTERIOR_SRC, INTERIOR_DST)} "
        f"i2_interior {i2_cost(INTERIOR_SRC, INTERIOR_DST)} "
        f"c2d4_interior {c2d4_cost(INTERIOR_SRC, INTERIOR_DST)} "
        f"rho3_interior {rho3_cost(INTERIOR_SRC, INTERIOR_DST)} "
        f"interior_extra {int(interior_extra(INTERIOR_SRC, INTERIOR_DST))} "
        f"deep_interior_extra {int(deep_interior_extra(INTERIOR_SRC, INTERIOR_DST))}"
    )
    print(
        f"j2_deep {j2_cost(DEEP_SRC, DEEP_DST)} "
        f"i2_deep {i2_cost(DEEP_SRC, DEEP_DST)} "
        f"c2d4_deep {c2d4_cost(DEEP_SRC, DEEP_DST)} "
        f"rho3_deep {rho3_cost(DEEP_SRC, DEEP_DST)} "
        f"deep_interior_extra {int(deep_interior_extra(DEEP_SRC, DEEP_DST))}"
    )
    print(
        f"j2_shallow_deep {j2_cost(SHALLOW_DEEP_SRC, SHALLOW_DEEP_DST)} "
        f"i2_shallow_deep {i2_cost(SHALLOW_DEEP_SRC, SHALLOW_DEEP_DST)} "
        f"deep_interior_extra_shallow {int(deep_interior_extra(SHALLOW_DEEP_SRC, SHALLOW_DEEP_DST))}"
    )

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/C2D4_DEEP_INTERIOR_COST2_SAMEK_K1_B6_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
        j2_cost(origin, AXIS) == 3 and nu_cost(origin, AXIS) == 3,
    )
    checks.check(
        "hop-axis-axis",
        "a same-support axis hop has named cost 3",
        j2_cost(AXIS, (2, 0, 0)) == 3,
    )
    checks.check(
        "hop-support-rise",
        "the displayed body path keeps cost 1 on the 1-to-2 and 2-to-3 hops",
        j2_cost(AXIS, FACE) == 1 and j2_cost(FACE, BODY) == 1,
    )
    checks.check(
        "hop-deep-interior-clause",
        "the named 3-to-3 dest min-abs>=3 clause prices (2,3,3) to (3,3,3) at 2",
        deep_interior_extra(DEEP_SRC, DEEP_DST)
        and rho3_cost(DEEP_SRC, DEEP_DST) == 1
        and c2d4_cost(DEEP_SRC, DEEP_DST) == 1
        and i2_cost(DEEP_SRC, DEEP_DST) == 2
        and j2_cost(DEEP_SRC, DEEP_DST) == 2
        and min_abs(DEEP_DST) >= 3
        and DEEP_SRC not in sites
        and DEEP_DST not in sites,
    )
    checks.check(
        "hop-interior-skipped",
        "the named dest min-abs>=3 clause skips (2,2,1) to (2,2,2); dest min abs is 2",
        not deep_interior_extra(INTERIOR_SRC, INTERIOR_DST)
        and interior_extra(INTERIOR_SRC, INTERIOR_DST)
        and min_abs(INTERIOR_DST) == 2
        and rho3_cost(INTERIOR_SRC, INTERIOR_DST) == 1
        and c2d4_cost(INTERIOR_SRC, INTERIOR_DST) == 1
        and i2_cost(INTERIOR_SRC, INTERIOR_DST) == 2
        and j2_cost(INTERIOR_SRC, INTERIOR_DST) == 1
        and INTERIOR_SRC in sites
        and INTERIOR_DST in sites,
    )
    checks.check(
        "hop-interior-exit-idle",
        "the named deep-interior clause skips (2,2,2) to (1,2,2) because dest min abs is 1",
        not deep_interior_extra(INTERIOR_DST, INTERIOR_EXIT)
        and not interior_extra(INTERIOR_DST, INTERIOR_EXIT)
        and min_abs(INTERIOR_EXIT) == 1
        and rho3_cost(INTERIOR_DST, INTERIOR_EXIT) == 1
        and j2_cost(INTERIOR_DST, INTERIOR_EXIT) == 1
        and INTERIOR_EXIT in sites,
    )
    checks.check(
        "hop-max4-out-clause",
        "c2d4 still prices (4,2,0) to (5,2,0) at 2, so j2 does as well",
        d4_extra(MAX4_OUT_SRC, MAX4_OUT_DST)
        and rho3_cost(MAX4_OUT_SRC, MAX4_OUT_DST) == 1
        and c2d4_cost(MAX4_OUT_SRC, MAX4_OUT_DST) == 2
        and j2_cost(MAX4_OUT_SRC, MAX4_OUT_DST) == 2
        and not deep_interior_extra(MAX4_OUT_SRC, MAX4_OUT_DST)
        and MAX4_OUT_SRC in sites
        and MAX4_OUT_DST not in sites,
    )
    in_ball_deep = 0
    in_ball_interior = 0
    in_ball_cost2 = 0
    in_ball_c2d4_new = 0
    j2_equals_rho3_on_ball = True
    j2_equals_c2d4_on_ball = True
    for site in sites:
        for step in STEPS:
            neighbor = add(site, step)
            if neighbor not in sites:
                continue
            if j2_cost(site, neighbor) != rho3_cost(site, neighbor):
                j2_equals_rho3_on_ball = False
            if j2_cost(site, neighbor) != c2d4_cost(site, neighbor):
                j2_equals_c2d4_on_ball = False
            if j2_cost(site, neighbor) == 2:
                in_ball_cost2 += 1
            if deep_interior_extra(site, neighbor):
                in_ball_deep += 1
            if interior_extra(site, neighbor):
                in_ball_interior += 1
            if d4_extra(site, neighbor) and rho3_cost(site, neighbor) == 1:
                in_ball_c2d4_new += 1
    checks.check(
        "deep-interior-no-new-in-ball-tax",
        "no in-ball hop carries a j2 extra tax beyond rho3; dest min-abs>=3 3-to-3 hops miss this ball",
        in_ball_deep == 0
        and in_ball_cost2 == 0
        and in_ball_c2d4_new == 0
        and j2_equals_rho3_on_ball
        and j2_equals_c2d4_on_ball
        and in_ball_interior > 0,
    )
    checks.check(
        "j2-clauses",
        "seed-exit, axis, drop, corridor-slide, and ridge-slide cost 3; dest min-abs>=3 3-to-3 and max>=4 out-face cost 2; dest min-abs=2 interior stays 1",
        j2_cost((0, 0, 0), (1, 0, 0)) == 3
        and j2_cost((1, 0, 0), (2, 0, 0)) == 3
        and j2_cost((1, 1, 0), (1, 0, 0)) == 3
        and j2_cost((1, 1, 0), (2, 1, 0)) == 3
        and j2_cost((1, 1, 1), (2, 1, 1)) == 3
        and j2_cost((2, 3, 3), (3, 3, 3)) == 2
        and j2_cost((4, 2, 0), (5, 2, 0)) == 2
        and j2_cost((4, 1, 0), (5, 1, 0)) == 3
        and j2_cost((2, 2, 1), (2, 2, 2)) == 1
        and i2_cost((2, 2, 1), (2, 2, 2)) == 2
        and j2_cost((1, 0, 0), (1, 1, 0)) == 1
        and j2_cost((1, 1, 0), (1, 1, 1)) == 1
        and j2_cost((2, 2, 0), (3, 2, 0)) == 1
        and j2_cost((3, 2, 0), (4, 2, 0)) == 1
        and j2_cost((2, 2, 2), (1, 2, 2)) == 1
        and j2_cost((3, 2, 2), (3, 3, 2)) == 1
        and i2_cost((3, 2, 2), (3, 3, 2)) == 2
        and not deep_interior_extra((1, 1, 0), (1, 1, 1))
        and not deep_interior_extra((2, 2, 1), (2, 2, 2))
        and not deep_interior_extra((2, 2, 2), (1, 2, 2)),
    )
    axis_path_cost = j2_cost(origin, AXIS)
    body_path_cost = (
        j2_cost(origin, AXIS)
        + j2_cost(AXIS, FACE)
        + j2_cost(FACE, BODY)
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
        "the live Admissibility wording is unchanged and does not name j2",
        "There is one fixed nearest-neighbor admissibility rule" in axiom
        and "j2(v→w)" not in axiom
        and "Do not write j2 into Admissibility." in note,
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
        and "adds no new in-ball tax" in note
        and "j2` equals `ρ3`" in note,
    )
    checks.check(
        "no-axiom-edit",
        "note records hypothetical axiom status no edit",
        'hypothetical_axiom_status: "no edit"' in note,
    )
    checks.check(
        "skipped-interior-arrival",
        "the same Dijkstra records t(2,2,1)=9 and t(2,2,2)=10 matching the skipped dest min-abs=2 hop of cost 1",
        t221 == 9
        and t222 == 10
        and t221 + j2_cost(INTERIOR_SRC, INTERIOR_DST) == t222
        and "t(2,2,1) = 9" in note
        and "t(2,2,2) = 10" in note,
    )
    checks.check(
        "skipped-max3-arrival",
        "the same Dijkstra records t(3,2,0)=9 and t(4,2,0)=10 matching the skipped extra hop of cost 1",
        t320 == 9
        and t420 == 10
        and t320 + j2_cost(MAX3_OUT_SRC, MAX3_OUT_DST) == t420
        and "t(3,2,0) = 9" in note
        and "t(4,2,0) = 10" in note,
    )
    checks.check(
        "axiom-untouched",
        "the axiom memo is an input only and still names the four axioms",
        "### Admissibility / Local Constraint" in axiom
        and "j2(v→w)" not in axiom
        and "c2d4(v→w)" not in axiom
        and "ρ3(v→w)" not in axiom,
    )

    print("per_element: named hop-cost values are 1, 2, or 3 on nearest-neighbor hops.")
    print("per_site: arrival times are reported only at (1,0,0) and (1,1,1).")
    print("lattice_wide: checked and not executed — the search stays inside B_6(0).")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
