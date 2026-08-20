#!/usr/bin/env python3
"""Same-k reverse at k=13 under the named c2d4-plus-soft-ridge hop-cost on B_39(0).

One Dijkstra from the origin on the finite nearest-neighbor graph. The
hop-cost s2 is displayed, not adopted, and is not written into
Admissibility. No cache or governance surface is written.
"""

from __future__ import annotations

import ast
import heapq
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/C2D4_SOFT_RIDGE_COST2_SAMEK_K13_B39_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

AUDIT_INPUT_PATHS = (
    "docs/C2D4_SOFT_RIDGE_COST2_SAMEK_K13_B39_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

CLAIM_SCOPE = (
    "Same-k reverse at k=13 under the named c2d4-plus-soft-ridge "
    "hop-cost on B_39(0) is reported. Displayed, not adopted."
)

RADIUS = 39
ORIGIN = (0, 0, 0)
AXIS = (13, 0, 0)
BODY = (13, 13, 13)
FACE = (13, 13, 0)
AXIS_R2 = 169
BODY_R2 = 507
STEPS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
Site = tuple[int, int, int]
INF = 10**9
N_SITES = 82239
T_AXIS_REP = 27
T_BODY_REP = 42


def add(site: Site, step: Site) -> Site:
    return (site[0] + step[0], site[1] + step[1], site[2] + step[2])


def coord_sum(site: Site) -> int:
    return abs(site[0]) + abs(site[1]) + abs(site[2])


def in_ball(site: Site) -> bool:
    return coord_sum(site) <= RADIUS


def support_size(site: Site) -> int:
    return (site[0] != 0) + (site[1] != 0) + (site[2] != 0)


def unit_coord_count(site: Site) -> int:
    return (abs(site[0]) == 1) + (abs(site[1]) == 1) + (abs(site[2]) == 1)


def max_abs(site: Site) -> int:
    return max(abs(coordinate) for coordinate in site)


def min_abs(site: Site) -> int:
    return min(abs(coordinate) for coordinate in site)


def min_nonzero_abs(site: Site) -> int | None:
    nonzero = [abs(coordinate) for coordinate in site if coordinate != 0]
    if not nonzero:
        return None
    return min(nonzero)


def ridge_stay(source: Site, dest: Site) -> bool:
    return (
        support_size(source) == 3
        and support_size(dest) == 3
        and unit_coord_count(dest) == 2
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
    if ridge_stay(source, dest):
        return 3
    return 1


def omega_extra(source: Site, dest: Site) -> bool:
    return (
        support_size(source) == 2
        and support_size(dest) == 2
        and max_abs(dest) > max_abs(source)
    )


def d3_extra(source: Site, dest: Site) -> bool:
    return omega_extra(source, dest) and max_abs(source) >= 3


def d4_extra(source: Site, dest: Site) -> bool:
    return omega_extra(source, dest) and max_abs(source) >= 4


def c2d4_cost(source: Site, dest: Site) -> int:
    if rho3_cost(source, dest) == 3:
        return 3
    if d4_extra(source, dest):
        return 2
    return 1


def s2_cost(source: Site, dest: Site) -> int:
    if mu_cost(source, dest) == 3:
        return 3
    if ridge_stay(source, dest) or c2d4_cost(source, dest) == 2:
        return 2
    return 1


class DijkstraCounter:
    def __init__(self) -> None:
        self.calls = 0

    def distances(self) -> dict[Site, int]:
        self.calls += 1
        dist = {ORIGIN: 0}
        queue: list[tuple[int, Site]] = [(0, ORIGIN)]
        while queue:
            cost, site = heapq.heappop(queue)
            if cost != dist[site]:
                continue
            for step in STEPS:
                neighbor = add(site, step)
                if not in_ball(neighbor):
                    continue
                candidate = cost + s2_cost(site, neighbor)
                if candidate < dist.get(neighbor, INF):
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


def path_cost(walk: tuple[Site, ...], cost_fn=s2_cost) -> int:
    return sum(cost_fn(a, b) for a, b in zip(walk, walk[1:]))


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
        "nearest-neighbor graph B_39(0) only"
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
        "claim_boundary: same-k reverse at k=13 is displayed, not adopted"
    )

    hop_samples = (
        ((0, 0, 0), (1, 0, 0), 3),
        ((1, 0, 0), (2, 0, 0), 3),
        ((1, 0, 0), (1, 1, 0), 1),
        ((1, 1, 0), (1, 1, 1), 1),
        ((1, 1, 0), (2, 1, 0), 3),
        ((2, 2, 0), (3, 2, 0), 1),
        ((3, 2, 0), (4, 2, 0), 1),
        ((4, 2, 0), (5, 2, 0), 2),
        ((4, 1, 0), (5, 1, 0), 3),
        ((1, 1, 1), (2, 1, 1), 2),
        ((13, 2, 1), (13, 1, 1), 2),
        ((4, 1, 1), (5, 1, 1), 2),
        ((2, 2, 2), (3, 2, 2), 1),
        ((3, 3, 2), (3, 3, 3), 1),
        ((4, 2, 2), (5, 2, 2), 1),
        ((4, 3, 1), (5, 3, 1), 1),
        ((12, 13, 13), (13, 13, 13), 1),
        ((12, 0, 0), (13, 0, 0), 3),
        ((2, 1, 0), (2, 1, 1), 1),
    )

    counter = DijkstraCounter()
    dist = counter.distances()
    t_axis = dist[AXIS]
    t_body = dist[BODY]
    t320 = dist[(3, 2, 0)]
    t420 = dist[(4, 2, 0)]
    t520 = dist[(5, 2, 0)]
    t211 = dist[(2, 1, 1)]
    t221 = dist[(2, 2, 1)]
    t_face = dist[FACE]
    t13131 = dist[(13, 13, 1)]
    t3900 = dist[(39, 0, 0)]
    axis_sq = t_axis * t_axis
    body_sq = t_body * t_body
    reverse = axis_sq * BODY_R2 > body_sq * AXIS_R2

    witness_axis = (
        ORIGIN,
        (1, 0, 0),
        (1, 1, 0),
        (1, 1, 1),
        (2, 1, 1),
        (2, 2, 1),
        *[(x, 2, 1) for x in range(3, 14)],
        (13, 1, 1),
        (13, 1, 0),
        AXIS,
    )
    witness_body = (
        ORIGIN,
        (1, 0, 0),
        (1, 1, 0),
        (1, 1, 1),
        (2, 1, 1),
        (2, 2, 1),
        *[(x, 2, 1) for x in range(3, 14)],
        *[(13, y, 1) for y in range(3, 14)],
        *[(13, 13, z) for z in range(2, 14)],
    )
    ridge_hop = ((1, 1, 1), (2, 1, 1))
    later_ridge = ((13, 2, 1), (13, 1, 1))
    later_hop = ((4, 2, 0), (5, 2, 0))
    skip_hop = ((3, 2, 0), (4, 2, 0))

    print(f"n_sites {len(dist)}")
    print(f"t(13,0,0) = {t_axis}")
    print(f"t(13,13,13) = {t_body}")
    print(
        f"same-k comparison: {t_axis}^2 / {AXIS_R2} = {axis_sq}/{AXIS_R2} versus "
        f"{t_body}^2 / {BODY_R2} = {body_sq}/{BODY_R2}; reverse={reverse}"
    )
    print(f"3 t(13,0,0)^2 = {3 * axis_sq}")
    print(f"t(13,13,13)^2 = {body_sq}")
    print(f"cross {axis_sq * BODY_R2} vs {body_sq * AXIS_R2}")
    print(f"t(13,13,0) = {t_face}")
    print(f"t(13,13,1) = {t13131}")
    print(f"t(2,1,1) = {t211}")
    print(f"t(2,2,1) = {t221}")
    print(f"t(3,2,0) = {t320}")
    print(f"t(4,2,0) = {t420}")
    print(f"t(5,2,0) = {t520}")
    print(f"t(39,0,0) = {t3900}")
    print(f"dijkstra_calls {counter.calls}")
    print(f"witness_axis_sum {path_cost(witness_axis)}")
    print(f"witness_body_sum {path_cost(witness_body)}")
    print(
        f"s2_ridge {s2_cost(*ridge_hop)} "
        f"c2d4_ridge {c2d4_cost(*ridge_hop)} "
        f"rho3_ridge {rho3_cost(*ridge_hop)} "
        f"mu_ridge {mu_cost(*ridge_hop)}"
    )
    print(
        f"s2_max4_out {s2_cost(*later_hop)} "
        f"c2d4_max4_out {c2d4_cost(*later_hop)} "
        f"rho3_max4_out {rho3_cost(*later_hop)}"
    )
    print(
        f"s2_interior {s2_cost((2, 2, 2), (3, 2, 2))} "
        f"c2d4_interior {c2d4_cost((2, 2, 2), (3, 2, 2))}"
    )

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/C2D4_SOFT_RIDGE_COST2_SAMEK_K13_B39_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and AUDIT_TIMEOUT_SEC == 120,
    )
    checks.check(
        "audit-input-literal",
        "AUDIT_INPUT_PATHS is a static string-literal tuple",
        literal_audit_paths(self_source) == AUDIT_INPUT_PATHS,
    )
    checks.check(
        "ball-cardinality",
        "B_39(0) is the 82239-site integer set with coordinate-sum at most 39",
        len(dist) == N_SITES
        and ORIGIN in dist
        and AXIS in dist
        and BODY in dist
        and coord_sum(AXIS) == 13
        and coord_sum(BODY) == 39
        and not in_ball((14, 13, 13))
        and all(in_ball(site) for site in dist),
    )
    checks.check(
        "one-dijkstra",
        "exactly one Dijkstra from the origin is executed",
        counter.calls == 1
        and dist[ORIGIN] == 0
        and "DijkstraCounter" in self_source,
    )
    checks.check(
        "reachable",
        "every site of B_39(0) is reached",
        all(cost < INF for cost in dist.values()) and len(dist) == N_SITES,
    )
    checks.check(
        "s2-samples",
        "named c2d4-plus-soft-ridge hop-cost matches the displayed samples",
        all(s2_cost(src, dest) == cost for src, dest, cost in hop_samples),
    )
    checks.check(
        "s2-clauses",
        "mu-cost-3 hops stay 3; ridge-stay and max>=4 out-face cost 2; interior 3-to-3 stays 1",
        s2_cost((0, 0, 0), (1, 0, 0)) == 3
        and s2_cost((1, 0, 0), (2, 0, 0)) == 3
        and s2_cost((1, 1, 0), (1, 0, 0)) == 3
        and s2_cost((1, 1, 0), (2, 1, 0)) == 3
        and s2_cost(*ridge_hop) == 2
        and s2_cost(*later_ridge) == 2
        and s2_cost((4, 1, 1), (5, 1, 1)) == 2
        and s2_cost(*later_hop) == 2
        and s2_cost((2, 2, 2), (3, 2, 2)) == 1
        and s2_cost((3, 3, 2), (3, 3, 3)) == 1
        and s2_cost((4, 2, 2), (5, 2, 2)) == 1
        and s2_cost((4, 3, 1), (5, 3, 1)) == 1
        and s2_cost((12, 13, 13), (13, 13, 13)) == 1
        and s2_cost((1, 0, 0), (1, 1, 0)) == 1
        and s2_cost((1, 1, 0), (1, 1, 1)) == 1
        and s2_cost((2, 2, 0), (3, 2, 0)) == 1
        and s2_cost(*skip_hop) == 1
        and c2d4_cost(*ridge_hop) == 3
        and rho3_cost(*ridge_hop) == 3
        and mu_cost(*ridge_hop) == 1
        and c2d4_cost(*later_hop) == 2
        and rho3_cost(*later_hop) == 1
        and ridge_stay(*ridge_hop)
        and ridge_stay(*later_ridge)
        and not ridge_stay((2, 2, 2), (3, 2, 2))
        and not d4_extra(*skip_hop)
        and d3_extra(*skip_hop)
        and d4_extra(*later_hop),
    )
    checks.check(
        "thm1-axis-time",
        "t(13,0,0) equals the computed origin-to-axis arrival time 27",
        t_axis == T_AXIS_REP
        and t_axis == path_cost(witness_axis)
        and t_axis > 0,
    )
    checks.check(
        "thm1-body-time",
        "t(13,13,13) equals the computed origin-to-body arrival time 42",
        t_body == T_BODY_REP
        and t_body == path_cost(witness_body)
        and t_body > 0,
    )
    checks.check(
        "thm2-reverse-holds",
        "t(13,0,0)^2 / 169 > t(13,13,13)^2 / 507 holds on the computed times",
        reverse is True
        and 3 * t_axis * t_axis == 2187
        and t_body * t_body == 1764
        and 2187 > 1764,
    )
    checks.check(
        "thm2-exact-cross",
        "27^2 * 507 = 369603 > 298116 = 42^2 * 169",
        axis_sq * BODY_R2 == 369603
        and body_sq * AXIS_R2 == 298116
        and AXIS_R2 * 3 == BODY_R2
        and 729 * 3 == 2187,
    )
    checks.check(
        "live-arrivals",
        "the same Dijkstra records ridge-stay at cost 2, skipped max>=3 out at 1, and max>=4 out at 2",
        t211 == 7
        and t221 == 8
        and t320 == 9
        and t420 == 10
        and t520 == 12
        and t13131 == 30
        and t_face == 33
        and t3900 == 58
        and t320 + s2_cost(*skip_hop) == t420
        and t420 + s2_cost(*later_hop) == t520
        and t13131 + 12 == t_body
        and path_cost(witness_axis, c2d4_cost) == 29
        and path_cost(witness_body, c2d4_cost) == 43
        and path_cost(witness_axis, rho3_cost) == 29
        and path_cost(witness_body, rho3_cost) == 43,
    )
    checks.check(
        "thm1-note-reports-times",
        "the note reports the computed arrival times",
        f"t(13,0,0) = {t_axis}" in note and f"t(13,13,13) = {t_body}" in note,
    )
    checks.check(
        "thm2-note-reports-comparison",
        "the note reports the integer same-k comparison and does not adopt it",
        "729/169" in note
        and "1764/507" in note
        and "2187/507" in note
        and "2187 > 1764" in note
        and "369603" in note
        and "298116" in note
        and "The inequality holds" in note
        and "Displayed, not adopted" in note,
    )
    checks.check(
        "thm3-not-in-admissibility",
        "the live Admissibility wording is unchanged and does not name s2",
        "There is one fixed nearest-neighbor admissibility rule" in axiom
        and "s2(v→w)" not in axiom
        and "Do not write s2 into Admissibility." in note
        and "c2d4-plus-soft-ridge" in note,
    )
    checks.check(
        "thm3-no-l1-attachment",
        "the note refuses to attach L1 and does not score a unit hop-cost",
        "Do not attach L1." in note
        and "attach L1" in note
        and "unit hop-cost" not in note.lower()
        and "not attached as an arrival law" in note,
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
        "forbidden tokens are absent from the note and runner",
        all(token not in note and token not in self_source for token in forbidden)
        and ("runner-" + "cache") not in note,
    )
    checks.check(
        "claim-scope-contract",
        "the required claim_scope is source-visible",
        CLAIM_SCOPE in note.replace("\n", " ")
        and CLAIM_SCOPE in note
        and 'claim_scope: "Same-k reverse at k=13 under the named c2d4-plus-soft-ridge hop-cost on B_39(0) is reported. Displayed, not adopted."'
        in note,
    )
    checks.check(
        "uniqueness-not-claimed",
        "the note does not claim uniqueness of the named hop-cost",
        "Uniqueness is not claimed" in note and "unique hop-cost" not in note,
    )
    checks.check(
        "scope-boundary",
        "the theorem stays on B_39(0) and proposes no axiom edit",
        "B_39(0)" in note
        and 'hypothetical_axiom_status: "no edit"' in note
        and "one Dijkstra" in note
        and "not leftover of a larger-ball table" in note,
    )
    checks.check(
        "not-leftover-of-parents",
        "s2 prices ridge-stay at 2 while rho3 and c2d4 price it at 3; max>=4 out-face stays 2",
        s2_cost(*ridge_hop) == 2
        and rho3_cost(*ridge_hop) == 3
        and c2d4_cost(*ridge_hop) == 3
        and mu_cost(*ridge_hop) == 1
        and s2_cost(*later_hop) == 2
        and c2d4_cost(*later_hop) == 2
        and t211 == 7
        and t_axis == 27
        and t_body == 42
        and "cannot price the ridge-stay" in note
        and "`t(2,1,1) = 7`" in note
        and "not leftover of `ρ3`" in note
        and "not leftover of `c2d4`" in note,
    )
    checks.check(
        "live-quotes",
        "live Lattice, Admissibility, and Record sentences are quoted without rewrite",
        "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor"
        in axiom
        and "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor"
        in note
        and "There is one fixed nearest-neighbor admissibility rule, covariant under lattice"
        in axiom
        and "There is one fixed nearest-neighbor admissibility rule, covariant under lattice"
        in note
        and "A site with no record cannot be read." in axiom
        and "A site with no record cannot be read." in note
        and "When present, a record locks exactly one admissible local possibility."
        in axiom
        and "When present, a record locks exactly one admissible local possibility."
        in note,
    )
    checks.check(
        "axiom-untouched",
        "the axiom memo is an input only and still names the four axioms",
        "### Admissibility / Local Constraint" in axiom
        and "s2(v→w)" not in axiom
        and "c2d4(v→w)" not in axiom
        and "ρ3(v→w)" not in axiom,
    )
    checks.check(
        "displayed-not-adopted",
        "the rule is displayed, not adopted",
        "Displayed, not adopted" in note
        and "displayed, not adopted" in note.lower()
        and 'hypothetical_axiom_status: "no edit"' in note,
    )

    print("per_element: named hop-cost values are 1, 2, or 3 on nearest-neighbor hops.")
    print("per_site: arrival times are reported only at (13,0,0) and (13,13,13).")
    print("lattice_wide: checked and not executed — the search stays inside B_39(0).")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
