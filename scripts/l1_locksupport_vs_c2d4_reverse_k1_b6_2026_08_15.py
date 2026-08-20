#!/usr/bin/env python3
"""Same-k reverse bits at k=1: unit ℓ¹ lock-support versus named c2d4 on B_6(0).

Two Dijkstras from the origin on the finite nearest-neighbor graph: first
unit ℓ¹ cost on every 6-NN hop, then named c2d4. Reverse bits are
displayed, not adopted. Hop-costs are not written into Admissibility.
L1 is not attached. No cache or governance surface is written.
"""

from __future__ import annotations

import ast
import heapq
from pathlib import Path
from typing import Callable


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "L1_LOCKSUPPORT_VS_C2D4_REVERSE_K1_B6_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/L1_LOCKSUPPORT_VS_C2D4_REVERSE_K1_B6_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

CLAIM_SCOPE = (
    "Same-k reverse at k=1 under unit ℓ¹ versus named c2d4 "
    "on B_6(0) is compared. Displayed, not adopted."
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
STEPS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
Site = tuple[int, int, int]
CostFn = Callable[[Site, Site], int]


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


def l1_cost(_source: Site, _dest: Site) -> int:
    return 1


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


def reverse_bit(t_axis: int, t_body: int) -> bool:
    return 3 * t_axis * t_axis > t_body * t_body


class DijkstraCounter:
    def __init__(self) -> None:
        self.calls = 0

    def distances(
        self,
        sites: frozenset[Site],
        origin: Site,
        cost_fn: CostFn,
    ) -> dict[Site, int]:
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
                candidate = cost + cost_fn(site, neighbor)
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
        "external_scientific_inputs: none; unit ℓ¹ lock-support versus named "
        "c2d4 on the finite nearest-neighbor graph B_6(0) only"
    )
    print(
        "package_local_integrity_reads: proposed source note and live axiom "
        "memo only; no cache or governance surface is written"
    )
    print(
        "measure_boundary: integer hop-costs and two Dijkstras; no fit and "
        "no leftover larger-ball table"
    )
    print(
        "claim_boundary: same-k reverse bits at k=1 are displayed, not adopted"
    )

    sites = ball_sites(RADIUS)
    origin = (0, 0, 0)
    counter = DijkstraCounter()
    dist_l1 = counter.distances(sites, origin, l1_cost)
    dist_c2 = counter.distances(sites, origin, c2d4_cost)
    t_l1_axis = dist_l1[AXIS]
    t_l1_body = dist_l1[BODY]
    t_c2_axis = dist_c2[AXIS]
    t_c2_body = dist_c2[BODY]
    reverse_l1 = reverse_bit(t_l1_axis, t_l1_body)
    reverse_c2 = reverse_bit(t_c2_axis, t_c2_body)
    bits_agree = reverse_l1 == reverse_c2

    print(f"n_sites {len(sites)}")
    print(f"l1 t(1,0,0) = {t_l1_axis}")
    print(f"l1 t(1,1,1) = {t_l1_body}")
    print(
        f"l1 same-k comparison: {t_l1_axis}^2 / 1 = {t_l1_axis * t_l1_axis} versus "
        f"{t_l1_body}^2 / 3 = {t_l1_body * t_l1_body}/3; reverse={reverse_l1}"
    )
    print(f"l1 3 t(1,0,0)^2 = {3 * t_l1_axis * t_l1_axis}")
    print(f"l1 t(1,1,1)^2 = {t_l1_body * t_l1_body}")
    print(f"c2d4 t(1,0,0) = {t_c2_axis}")
    print(f"c2d4 t(1,1,1) = {t_c2_body}")
    print(
        f"c2d4 same-k comparison: {t_c2_axis}^2 / 1 = {t_c2_axis * t_c2_axis} versus "
        f"{t_c2_body}^2 / 3 = {t_c2_body * t_c2_body}/3; reverse={reverse_c2}"
    )
    print(f"c2d4 3 t(1,0,0)^2 = {3 * t_c2_axis * t_c2_axis}")
    print(f"c2d4 t(1,1,1)^2 = {t_c2_body * t_c2_body}")
    print(f"reverse_bits_agree {bits_agree}")
    print(f"dijkstra_calls {counter.calls}")

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/L1_LOCKSUPPORT_VS_C2D4_REVERSE_K1_B6_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
        "two-dijkstras",
        "exactly two Dijkstras from the origin are executed, unit ℓ¹ then c2d4",
        counter.calls == 2
        and "dist_l1 = counter.distances(sites, origin, l1_cost)" in self_source
        and "dist_c2 = counter.distances(sites, origin, c2d4_cost)" in self_source
        and self_source.index("l1_cost") < self_source.index("c2d4_cost"),
    )
    checks.check(
        "reachable",
        "every site of B_6(0) is reached under both costs",
        all(dist_l1[site] < 10**9 for site in sites)
        and all(dist_c2[site] < 10**9 for site in sites),
    )
    checks.check(
        "l1-unit-hops",
        "ℓ¹ prices every 6-NN hop at cost 1",
        l1_cost(origin, AXIS) == 1
        and l1_cost(AXIS, (2, 0, 0)) == 1
        and l1_cost(AXIS, FACE) == 1
        and l1_cost(FACE, BODY) == 1
        and l1_cost(MAX4_OUT_SRC, MAX4_OUT_DST) == 1,
    )
    checks.check(
        "c2d4-clauses",
        "seed-exit, axis, drop, corridor-slide, and ridge-slide cost 3; max>=4 out-face costs 2; 1-to-2 and small 2-to-3 cost 1",
        c2d4_cost((0, 0, 0), (1, 0, 0)) == 3
        and c2d4_cost((1, 0, 0), (2, 0, 0)) == 3
        and c2d4_cost((1, 1, 0), (1, 0, 0)) == 3
        and c2d4_cost((1, 1, 0), (2, 1, 0)) == 3
        and c2d4_cost((1, 1, 1), (2, 1, 1)) == 3
        and c2d4_cost((4, 2, 0), (5, 2, 0)) == 2
        and c2d4_cost((4, 1, 0), (5, 1, 0)) == 3
        and c2d4_cost((1, 0, 0), (1, 1, 0)) == 1
        and c2d4_cost((1, 1, 0), (1, 1, 1)) == 1
        and c2d4_cost((2, 2, 2), (3, 2, 2)) == 1
        and c2d4_cost((2, 2, 0), (3, 2, 0)) == 1
        and c2d4_cost((3, 2, 0), (4, 2, 0)) == 1
        and not d4_extra((3, 2, 0), (4, 2, 0))
        and not d4_extra((1, 1, 0), (2, 1, 0)),
    )
    l1_axis_path = l1_cost(origin, AXIS)
    l1_body_path = (
        l1_cost(origin, AXIS) + l1_cost(AXIS, FACE) + l1_cost(FACE, BODY)
    )
    c2_axis_path = c2d4_cost(origin, AXIS)
    c2_body_path = (
        c2d4_cost(origin, AXIS) + c2d4_cost(AXIS, FACE) + c2d4_cost(FACE, BODY)
    )
    checks.check(
        "thm1-l1-times",
        "under ℓ¹, t(1,0,0)=1 and t(1,1,1)=3 match the unit-cost arrivals",
        t_l1_axis == 1
        and t_l1_body == 3
        and t_l1_axis == l1_axis_path
        and t_l1_body == l1_body_path,
    )
    checks.check(
        "thm1-l1-reverse",
        "under ℓ¹, t(1,0,0)^2 > t(1,1,1)^2 / 3 fails",
        not reverse_l1
        and 3 * t_l1_axis * t_l1_axis == 3
        and t_l1_body * t_l1_body == 9,
    )
    checks.check(
        "thm2-c2d4-times",
        "under c2d4, t(1,0,0)=3 and t(1,1,1)=5 match the named-cost arrivals",
        t_c2_axis == 3
        and t_c2_body == 5
        and t_c2_axis == c2_axis_path
        and t_c2_body == c2_body_path,
    )
    checks.check(
        "thm2-c2d4-reverse",
        "under c2d4, t(1,0,0)^2 > t(1,1,1)^2 / 3 holds",
        reverse_c2
        and 3 * t_c2_axis * t_c2_axis == 27
        and t_c2_body * t_c2_body == 25,
    )
    checks.check(
        "thm3-bits-disagree",
        "the two reverse bits disagree, so occupancy t is not the Record-side cone",
        not bits_agree
        and reverse_l1 is False
        and reverse_c2 is True,
    )
    checks.check(
        "thm1-note-reports-l1",
        "the note reports the ℓ¹ times and failed reverse",
        "t(1,0,0) = 1" in note
        and "t(1,1,1) = 3" in note
        and "1 > 9/3" in note
        and "3 > 9" in note,
    )
    checks.check(
        "thm2-note-reports-c2d4",
        "the note reports the c2d4 times and holding reverse",
        "t(1,0,0) = 3" in note
        and "t(1,1,1) = 5" in note
        and "9 > 25/3" in note
        and "27 > 25" in note,
    )
    checks.check(
        "thm3-note-reports-disagreement",
        "the note reports disagreement and the occupancy reading",
        "The two reverse bits disagree" in note
        and "occupancy t is not the Record-side cone" in note
        and "Displayed, not adopted" in note,
    )
    checks.check(
        "thm3-not-in-admissibility",
        "the live Admissibility wording is unchanged and does not name these hop-costs",
        "There is one fixed nearest-neighbor admissibility rule" in axiom
        and "c2d4(v→w)" not in axiom
        and "ℓ¹" not in axiom
        and "Do not write hop-costs into Admissibility." in note,
    )
    checks.check(
        "thm3-no-l1-attachment",
        "the note refuses to attach L1",
        "Do not attach L1." in note and "attach L1" in note,
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
        "uniqueness-not-required",
        "the note does not require uniqueness",
        "Uniqueness is not required" in note and "unique hop-cost" not in note,
    )
    checks.check(
        "scope-boundary",
        "the theorem stays on B_6(0), uses two Dijkstras, and proposes no axiom edit",
        "B_6(0)" in note
        and 'hypothetical_axiom_status: "no edit"' in note
        and "Two Dijkstras" in note
        and "not leftover of a larger-ball table" in note
        and "B_" + "57" not in note
        and "B_" + "57" not in self_source,
    )
    checks.check(
        "displayed-not-adopted",
        "the comparison is displayed, not adopted",
        "Displayed, not adopted" in note
        and "lock-support cone" in note,
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
        and "c2d4(v→w)" not in axiom
        and "ρ3(v→w)" not in axiom,
    )
    checks.check(
        "no-path-dump",
        "the runner stores arrival costs only",
        ("pre" + "decessor") not in self_source.lower()
        and ("path " + "dump") not in self_source.lower()
        and ("path " + "dump") not in note.lower(),
    )

    print("per_element: named hop-costs are integers on nearest-neighbor hops.")
    print("per_site: arrival times are reported only at (1,0,0) and (1,1,1).")
    print("lattice_wide: checked and not executed — the search stays inside B_6(0).")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
