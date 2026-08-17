#!/usr/bin/env python3
"""Exact checks for the named support-drop hop-cost on B_4(0)."""

from __future__ import annotations

from heapq import heappop, heappush
from itertools import product
from math import sqrt
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]

AUDIT_INPUT_PATHS = (
    "docs/NO_SHORTCUT_SUPPORT_DROP_HOPCOST_B4_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / AUDIT_INPUT_PATHS[0]
AXIOM_PATH = ROOT / AUDIT_INPUT_PATHS[1]

Point = tuple[int, int, int]

AXES: tuple[Point, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
ORIGIN: Point = (0, 0, 0)
RADIUS = 4


def normalize(text: str) -> str:
    return " ".join(text.split())


def l1_norm(vector: Point) -> int:
    return abs(vector[0]) + abs(vector[1]) + abs(vector[2])


def l2_norm(vector: Point) -> float:
    return sqrt(vector[0] * vector[0] + vector[1] * vector[1] + vector[2] * vector[2])


def support_size(vector: Point) -> int:
    return int(vector[0] != 0) + int(vector[1] != 0) + int(vector[2] != 0)


def radius_ball(radius: int) -> tuple[Point, ...]:
    points = []
    for x, y, z in product(range(-radius, radius + 1), repeat=3):
        point = (x, y, z)
        if l1_norm(point) <= radius:
            points.append(point)
    return tuple(points)


def nu_cost(source: Point, target: Point) -> int:
    source_weight = support_size(source)
    target_weight = support_size(target)
    if source_weight == 0 or (source_weight == 1 and target_weight == 1) or target_weight < source_weight:
        return 3
    return 1


def first_arrivals(sites: tuple[Point, ...]) -> dict[Point, int]:
    site_set = set(sites)
    best = {ORIGIN: 0}
    queue: list[tuple[int, Point]] = [(0, ORIGIN)]
    while queue:
        cost, site = heappop(queue)
        if cost != best[site]:
            continue
        sx, sy, sz = site
        for dx, dy, dz in AXES:
            neighbor = (sx + dx, sy + dy, sz + dz)
            if neighbor not in site_set:
                continue
            next_cost = cost + nu_cost(site, neighbor)
            if next_cost < best.get(neighbor, next_cost + 1):
                best[neighbor] = next_cost
                heappush(queue, (next_cost, neighbor))
    return best


def population_variance(values: list[float]) -> float:
    count = len(values)
    mean = sum(values) / count
    return sum((value - mean) ** 2 for value in values) / count


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool, residual: object | None = None) -> None:
        ok = bool(condition)
        self.passed += int(ok)
        self.failed += int(not ok)
        print(f"{'PASS' if ok else 'FAIL'}: {label} {statement}")
        if not ok and residual is not None:
            print(f"  residual: {residual}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    for relative in AUDIT_INPUT_PATHS:
        (ROOT / relative).read_text(encoding="utf-8")
    normalized_note = normalize(note)
    normalized_axiom = normalize(axiom)

    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print("cache_write: false")
    print("external_scientific_inputs: current Lattice and Admissibility wording are source-bound; nu is a displayed hop-cost")
    print("construction: B_4(0) six-neighbor graph, named support-drop hop-cost, one Dijkstra first arrival")
    print("negative_scope: displayed comparison only; no axiom edit and no attached taxicab clock")

    checks.check(
        "audit-inputs",
        "declared inputs are exactly the source note and the axiom memo",
        AUDIT_INPUT_PATHS
        == (
            "docs/NO_SHORTCUT_SUPPORT_DROP_HOPCOST_B4_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and AUDIT_TIMEOUT_SEC == 120
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    )

    lattice_sentence = "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor"
    cubic_rotations = "proper cubic rotations about each site"
    admissibility_cov = "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations."
    admissibility_law = "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions."

    checks.check(
        "source-lattice",
        "current cubic nearest-neighbor and proper-cube wording is pinned",
        lattice_sentence in normalized_axiom
        and cubic_rotations in normalized_axiom
        and lattice_sentence in note
        and cubic_rotations in note,
    )
    checks.check(
        "source-admissibility",
        "current covariance and local-condition wording is pinned",
        admissibility_cov in normalized_axiom
        and admissibility_law in normalized_axiom
        and admissibility_cov in normalized_note
        and admissibility_law in normalized_note,
    )
    checks.check(
        "record-unused",
        "Record wording is quoted and the hop-cost does not use a record lock",
        "When present, a record locks exactly one admissible local possibility." in note
        and "A readout value is determined by record content alone." in note
        and "A site with no record cannot be read." in note
        and "Record is unused." in note,
    )

    ball = radius_ball(RADIUS)
    nonzero = tuple(point for point in ball if point != ORIGIN)
    site_set = set(ball)
    directed = []
    for site in ball:
        sx, sy, sz = site
        for dx, dy, dz in AXES:
            neighbor = (sx + dx, sy + dy, sz + dz)
            if neighbor in site_set:
                directed.append((site, neighbor, nu_cost(site, neighbor)))

    checks.check(
        "ball-cardinality",
        "B_4(0) has 129 sites and 128 nonzero sites; (2,2,2) is outside",
        len(ball) == 129
        and len(nonzero) == 128
        and (2, 2, 2) not in site_set
        and RADIUS == 4
        and all(l1_norm(point) <= 4 for point in ball),
        residual=(len(ball), len(nonzero)),
    )

    hop_ok = all(
        cost == (3 if support_size(source) == 0 or (support_size(source) == 1 and support_size(target) == 1) or support_size(target) < support_size(source) else 1)
        and cost in (1, 3)
        for source, target, cost in directed
    )
    seed_exit = all(cost == 3 for source, target, cost in directed if source == ORIGIN)
    checks.check(
        "named-hop-cost",
        "every in-ball 6-NN step uses the named support-drop rule with values in {1,3}",
        hop_ok and seed_exit and len(directed) == 528,
        residual=len(directed),
    )

    arrivals = first_arrivals(ball)
    t300 = arrivals[(3, 0, 0)]
    t111 = arrivals[(1, 1, 1)]
    t400 = arrivals[(4, 0, 0)]
    checks.check(
        "all-sites-reached",
        "one Dijkstra reaches every site of B_4(0)",
        len(arrivals) == 129 and arrivals[ORIGIN] == 0 and all(arrivals[point] > 0 for point in nonzero),
        residual=len(arrivals),
    )
    checks.check(
        "theorem-1-arrivals",
        "t(3,0,0)=9, t(1,1,1)=5, t(4,0,0)=12",
        t300 == 9 and t111 == 5 and t400 == 12,
        residual=(t300, t111, t400),
    )

    reverse_nu = 3 * t300 * t300 > 9 * t111 * t111
    reverse_l1 = 3 * 3 * 3 > 9 * 3 * 3
    checks.check(
        "small-ball-reverse",
        "3 t(3,0,0)^2 > 9 t(1,1,1)^2 holds for nu and fails for unit taxicab arrival",
        reverse_nu
        and not reverse_l1
        and 3 * t300 * t300 == 243
        and 9 * t111 * t111 == 225
        and 3 * l1_norm((3, 0, 0)) ** 2 == 27
        and 9 * l1_norm((1, 1, 1)) ** 2 == 81,
        residual=(3 * t300 * t300, 9 * t111 * t111),
    )

    ratios_nu = [l2_norm(point) / arrivals[point] for point in nonzero]
    ratios_l1 = [l2_norm(point) / l1_norm(point) for point in nonzero]
    var_nu = population_variance(ratios_nu)
    var_l1 = population_variance(ratios_l1)
    var_nu_text = f"{var_nu:.12f}"
    var_l1_text = f"{var_l1:.12f}"
    print(f"t300={t300} t111={t111} t400={t400}")
    print(f"reverse_left={3 * t300 * t300} reverse_right={9 * t111 * t111}")
    print(f"var_nu={var_nu_text} var_l1={var_l1_text}")
    checks.check(
        "theorem-2-variance",
        "population variance of |v|_2/t is smaller for nu than for unit taxicab arrival",
        var_nu < var_l1 and var_nu_text in note and var_l1_text in note,
        residual=(var_nu_text, var_l1_text),
    )

    allowed_retained = (
        "audit_required_before_effective_retained: true",
        "bare_retained_allowed: false",
    )
    other_retained = note
    for line in allowed_retained:
        other_retained = other_retained.replace(line, "")
    required = (
        "actual_current_surface_status: bounded-support",
        "target_claim_type: bounded_theorem",
        "trace_class: negative_route_pruning",
        "reachability_to_target: prunes",
        'hypothetical_axiom_status: "no edit"',
        "t(3,0,0)=9",
        "t(1,1,1)=5",
        "t(4,0,0)=12",
        "3 t(3,0,0)^2",
        "Displayed, not adopted",
        "Do not write",
        "into Admissibility",
        "Do not attach",
        "authors no audit verdict",
        "FAIL / DO NOT SHIP",
        "No occupancy is grown on a new patch",
        "On B_4(0), the named support-drop hop-cost is scored for small-ball reverse and for variance vs",
    )
    slash_r = "/" + "r"
    forbidden = (
        "G" + "_N",
        "1" + slash_r,
        "1" + slash_r + "^2",
        "Lattice" + "-named",
        "not a " + "TOE",
        "new axiom",
        "we adopt",
        "runner-cache",
        "trace_class: direct_blocker_closure",
        "reachability_to_target: partially_closes",
    )
    checks.check(
        "note-contract",
        "machine fields, displayed-not-adopted boundary, N1-N8, and forbidden-phrase hygiene hold",
        all(phrase in note for phrase in required)
        and all(line in note for line in allowed_retained)
        and all(f"### N{i}" in note for i in range(1, 9))
        and not any(phrase in note for phrase in forbidden)
        and "retained" not in other_retained
        and "promoted" not in note.lower()
        and "Block 12" not in note
        and "toe-lphys" not in note
        and "L1" not in note,
        residual=[phrase for phrase in required if phrase not in note],
    )
    checks.check(
        "displayed-not-adopted",
        "nu is not written into Admissibility and unit taxicab arrival is not attached",
        "Do not write `ν` into Admissibility" in note
        and "Do not attach ℓ¹" in note
        and "Displayed, not adopted" in note
        and 'hypothetical_axiom_status: "no edit"' in note
        and "ν" not in axiom,
    )

    print("per_element: named hops and the three reported arrival sites are executed")
    print("per_site: first arrival is shortest-path cost from the origin on B_4(0)")
    print("per_mode: checked and not executed — no spectral claim occurs")
    print("per_block: the radius-4 integer ball is the comparison domain")
    print("lattice_wide: checked and not executed — no occupancy step and no axiom edit")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
