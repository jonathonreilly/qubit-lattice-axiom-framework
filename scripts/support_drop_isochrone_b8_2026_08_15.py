#!/usr/bin/env python3
"""Isochrones of the named support-drop hop-cost on B_8(0).

One Dijkstra on the six-neighbor graph of the closed ℓ¹ ball of radius 8.
The named cost and the ℓ¹ comparator are displayed, not adopted. No cache
is written and Admissibility is not edited.
"""

from __future__ import annotations

from collections import defaultdict
from decimal import Decimal, getcontext
from fractions import Fraction
from heapq import heappop, heappush
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/SUPPORT_DROP_ISOCHRONE_B8_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/SUPPORT_DROP_ISOCHRONE_B8_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

RADIUS = 8
NEIGHBORS = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
getcontext().prec = 50


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(
        self,
        label: str,
        statement: str,
        condition: bool,
        residual: object | None = None,
    ) -> None:
        result = bool(condition)
        self.passed += int(result)
        self.failed += int(not result)
        print(f"{'PASS' if result else 'FAIL'}: {label} {statement}")
        if not result and residual is not None:
            print(f"  residual: {residual}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def l1_norm(site: tuple[int, int, int]) -> int:
    return abs(site[0]) + abs(site[1]) + abs(site[2])


def radius2(site: tuple[int, int, int]) -> int:
    return site[0] * site[0] + site[1] * site[1] + site[2] * site[2]


def support_weight(site: tuple[int, int, int]) -> int:
    return sum(coord != 0 for coord in site)


def support_drop_cost(
    source: tuple[int, int, int],
    target: tuple[int, int, int],
) -> int:
    source_weight = support_weight(source)
    target_weight = support_weight(target)
    if source_weight == 0 or (source_weight == 1 and target_weight == 1) or target_weight < source_weight:
        return 3
    return 1


def ball_sites(radius: int) -> list[tuple[int, int, int]]:
    sites: list[tuple[int, int, int]] = []
    for x in range(-radius, radius + 1):
        for y in range(-radius, radius + 1):
            for z in range(-radius, radius + 1):
                if abs(x) + abs(y) + abs(z) <= radius:
                    sites.append((x, y, z))
    return sites


def rotate_x(site: tuple[int, int, int]) -> tuple[int, int, int]:
    return (site[0], -site[2], site[1])


def rotate_y(site: tuple[int, int, int]) -> tuple[int, int, int]:
    return (site[2], site[1], -site[0])


def rotate_z(site: tuple[int, int, int]) -> tuple[int, int, int]:
    return (-site[1], site[0], site[2])


def generate_proper_cubic() -> tuple[tuple[tuple[int, int, int], ...], ...]:
    identity = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    seen = {identity}
    stack = [identity]
    rotations = (rotate_x, rotate_y, rotate_z)
    while stack:
        current = stack.pop()
        for rotate in rotations:
            columns = tuple(rotate(current[index]) for index in range(3))
            if columns not in seen:
                seen.add(columns)
                stack.append(columns)
    return tuple(sorted(seen))


def apply_linear(
    matrix: tuple[tuple[int, int, int], ...],
    site: tuple[int, int, int],
) -> tuple[int, int, int]:
    return (
        matrix[0][0] * site[0] + matrix[1][0] * site[1] + matrix[2][0] * site[2],
        matrix[0][1] * site[0] + matrix[1][1] * site[1] + matrix[2][1] * site[2],
        matrix[0][2] * site[0] + matrix[1][2] * site[1] + matrix[2][2] * site[2],
    )


def orbit_of(
    site: tuple[int, int, int],
    group: tuple[tuple[tuple[int, int, int], ...], ...],
) -> frozenset[tuple[int, int, int]]:
    return frozenset(apply_linear(matrix, site) for matrix in group)


def type_representative(orbit: frozenset[tuple[int, int, int]]) -> tuple[int, int, int]:
    nonnegative = [site for site in orbit if site[0] >= 0 and site[1] >= 0 and site[2] >= 0]
    return max(nonnegative)


def dijkstra_times(
    sites: list[tuple[int, int, int]],
) -> dict[tuple[int, int, int], int]:
    allowed = set(sites)
    infinity = 10**9
    arrival = {site: infinity for site in sites}
    origin = (0, 0, 0)
    arrival[origin] = 0
    queue: list[tuple[int, tuple[int, int, int]]] = [(0, origin)]
    while queue:
        time, site = heappop(queue)
        if time != arrival[site]:
            continue
        for step in NEIGHBORS:
            neighbor = (site[0] + step[0], site[1] + step[1], site[2] + step[2])
            if neighbor not in allowed:
                continue
            candidate = time + support_drop_cost(site, neighbor)
            if candidate < arrival[neighbor]:
                arrival[neighbor] = candidate
                heappush(queue, (candidate, neighbor))
    return arrival


def population_second_moment(
    sites: list[tuple[int, int, int]],
    time_of: dict[tuple[int, int, int], int],
) -> Fraction:
    total = Fraction(0)
    count = 0
    for site in sites:
        if site == (0, 0, 0):
            continue
        total += Fraction(radius2(site), time_of[site] ** 2)
        count += 1
    return total / count


def population_mean_speed(
    sites: list[tuple[int, int, int]],
    time_of: dict[tuple[int, int, int], int],
) -> Decimal:
    total = Decimal(0)
    count = 0
    for site in sites:
        if site == (0, 0, 0):
            continue
        total += Decimal(radius2(site)).sqrt() / Decimal(time_of[site])
        count += 1
    return total / count


def population_variance(second_moment: Fraction, mean: Decimal) -> Decimal:
    exact_second = Decimal(second_moment.numerator) / Decimal(second_moment.denominator)
    return exact_second - mean * mean


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")

    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print("cache_write: false")
    print("dijkstra_count: 1")
    print(
        "external_scientific_inputs: none; the named support-drop hop-cost is a "
        "declared displayed rule on B_8(0)"
    )
    print(
        "claim_scope: On B_8(0), the isochrones of the named support-drop "
        "hop-cost are reported. Displayed, not adopted."
    )

    checks.check(
        "audit-input-paths",
        "declared inputs are exactly the source note and current axiom memo",
        AUDIT_INPUT_PATHS == (NOTE_REL, AXIOM_REL)
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    )

    sites = ball_sites(RADIUS)
    checks.check(
        "ball-cardinality",
        "B_8(0) is the closed ℓ¹ ball of radius 8 and has 833 sites",
        len(sites) == 833,
        residual=len(sites),
    )

    arrival = dijkstra_times(sites)
    checks.check(
        "one-dijkstra-complete",
        "the single Dijkstra reaches every site of B_8(0)",
        all(arrival[site] < 10**9 for site in sites),
    )

    named = {
        (4, 0, 0): 10,
        (6, 0, 0): 12,
        (8, 0, 0): 16,
        (2, 2, 2): 8,
    }
    for site, expected in named.items():
        checks.check(
            f"arrival-{site[0]}-{site[1]}-{site[2]}",
            f"t{site} = {expected}",
            arrival[site] == expected,
            residual=arrival[site],
        )

    group = generate_proper_cubic()
    checks.check(
        "proper-cubic-order",
        "the proper cubic group generated by 90-degree axis rotations has order 24",
        len(group) == 24,
        residual=len(group),
    )

    seen_orbits: set[frozenset[tuple[int, int, int]]] = set()
    types: list[tuple[tuple[int, int, int], int, int, int]] = []
    type_time_constant = True
    type_radius_constant = True
    for site in sites:
        if site == (0, 0, 0):
            continue
        orbit = orbit_of(site, group)
        if orbit in seen_orbits:
            continue
        seen_orbits.add(orbit)
        times = {arrival[point] for point in orbit}
        radii = {radius2(point) for point in orbit}
        type_time_constant = type_time_constant and len(times) == 1
        type_radius_constant = type_radius_constant and len(radii) == 1
        representative = type_representative(orbit)
        types.append(
            (
                representative,
                len(orbit),
                arrival[representative],
                radius2(representative),
            )
        )
    types.sort(key=lambda row: (row[2], -row[3], row[0]))

    checks.check(
        "gplus-type-count",
        "B_8(0)\\{0} splits into 44 proper-cubic site-types covering 832 sites",
        len(types) == 44 and sum(row[1] for row in types) == 832,
        residual=(len(types), sum(row[1] for row in types)),
    )
    checks.check(
        "type-arrival-constant",
        "arrival time is constant on every proper-cubic site-type",
        type_time_constant,
    )
    checks.check(
        "type-radius-constant",
        "Euclidean radius is constant on every proper-cubic site-type",
        type_radius_constant,
    )

    extra_axis = arrival[(1, 0, 0)] == 3 and arrival[(5, 0, 0)] == 11 and arrival[(7, 0, 0)] == 13
    extra_off = arrival[(1, 1, 0)] == 4 and arrival[(3, 3, 0)] == 8 and arrival[(4, 4, 0)] == 10
    checks.check(
        "full-ball-not-four-point",
        "arrivals on further site-types are computed with the same Dijkstra, not copied from four points",
        extra_axis and extra_off,
        residual=(arrival[(1, 0, 0)], arrival[(5, 0, 0)], arrival[(3, 3, 0)]),
    )

    shells: dict[int, set[int]] = defaultdict(set)
    shell_count: dict[int, int] = defaultdict(int)
    for site in sites:
        if site == (0, 0, 0):
            continue
        shells[arrival[site]].add(radius2(site))
        shell_count[arrival[site]] += 1
    single_shells = [time for time, radii in shells.items() if len(radii) == 1]
    multi_shells = [time for time, radii in shells.items() if len(radii) > 1]
    checks.check(
        "isochrones-not-single-radius",
        "not every t-constant shell is a single Euclidean radius",
        len(multi_shells) > 0,
        residual=sorted(multi_shells),
    )
    checks.check(
        "single-radius-shells",
        "exactly the six shells t in {3,4,11,12,13,16} are single Euclidean radii",
        sorted(single_shells) == [3, 4, 11, 12, 13, 16],
        residual=sorted(single_shells),
    )
    checks.check(
        "multi-radius-shells",
        "exactly the six shells t in {5,6,7,8,9,10} mix Euclidean radii",
        sorted(multi_shells) == [5, 6, 7, 8, 9, 10],
        residual=sorted(multi_shells),
    )

    l1_times = {site: l1_norm(site) for site in sites}
    l1_times[(0, 0, 0)] = 0
    second_nu = population_second_moment(sites, arrival)
    second_l1 = population_second_moment(sites, l1_times)
    mean_nu = population_mean_speed(sites, arrival)
    mean_l1 = population_mean_speed(sites, l1_times)
    var_nu = population_variance(second_nu, mean_nu)
    var_l1 = population_variance(second_l1, mean_l1)
    print(f"var_nu={var_nu:.12f}")
    print(f"var_l1={var_l1:.12f}")
    print(f"E[r^2]_nu={second_nu.numerator}/{second_nu.denominator}")
    print(f"E[r^2]_l1={second_l1.numerator}/{second_l1.denominator}")
    print(f"single_shells={sorted(single_shells)}")
    print(f"multi_shells={sorted(multi_shells)}")
    print(f"n_types={len(types)}")

    checks.check(
        "variance-below-l1",
        "population var(|v|_2/t) on B_8(0)\\{0} is strictly smaller for the named cost than for ℓ¹",
        var_nu < var_l1,
        residual=(str(var_nu), str(var_l1)),
    )
    checks.check(
        "second-moments",
        "the displayed second moments are 1255910253469/4501790092800 and 55/104",
        second_nu == Fraction(1255910253469, 4501790092800) and second_l1 == Fraction(55, 104),
        residual=(str(second_nu), str(second_l1)),
    )

    seed_exit = support_drop_cost((0, 0, 0), (1, 0, 0)) == 3
    axis_skeleton = support_drop_cost((1, 0, 0), (2, 0, 0)) == 3
    drop_clause = support_drop_cost((1, 1, 0), (1, 0, 0)) == 3
    cheap_raise = support_drop_cost((1, 1, 0), (1, 1, 1)) == 1
    checks.check(
        "named-cost-clauses",
        "ν is 3 on seed-exit, both-weights-1, and support-drop, else 1",
        seed_exit and axis_skeleton and drop_clause and cheap_raise,
    )

    forbidden = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE")
    checks.check(
        "forbidden-tokens",
        "the note avoids the forbidden tokens",
        all(token not in note for token in forbidden),
    )
    checks.check(
        "displayed-not-adopted",
        "the note reports the isochrones as displayed, not adopted",
        "Displayed, not adopted" in note and "not adopted" in note,
    )
    checks.check(
        "nu-not-admissibility",
        "the note refuses to write ν into Admissibility, and the axiom memo is untouched by this claim",
        "Do not write" in note
        and "Admissibility" in note
        and "named support-drop hop-cost" in note
        and "ν" not in axiom
        and "support-drop" not in axiom,
    )
    checks.check(
        "l1-not-attached",
        "ℓ¹ is a displayed comparator only and is not attached as a hop-cost",
        "not attached" in note and "displayed comparator" in note and "attach L1" not in note,
    )
    checks.check(
        "claim-scope-text",
        "the note states the declared B_8(0) isochrone claim_scope",
        "On B_8(0), the isochrones of the named support-drop hop-cost are reported."
        in note,
    )
    checks.check(
        "note-records-named-times",
        "the note records the four named arrivals and the 44 site-types",
        "t(4,0,0)=10" in note
        and "t(6,0,0)=12" in note
        and "t(8,0,0)=16" in note
        and "t(2,2,2)=8" in note
        and "44" in note,
    )
    checks.check(
        "note-records-shells",
        "the note records the mixed-radius shells and the variance comparison",
        "not a single Euclidean radius" in note
        and "0.006349675165" in note
        and "0.011339404957" in note,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
