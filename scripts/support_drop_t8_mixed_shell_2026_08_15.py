#!/usr/bin/env python3
"""Name the G+ types that share arrival t=8 under the support-drop hop-cost.

One Dijkstra on the induced six-neighbor graph of the closed taxicab ball
B_6(0). The named hop-cost nu is displayed, not adopted. No axiom edit,
L1 attachment, cache write, or citation manifest.
"""

from __future__ import annotations

from heapq import heappop, heappush
from itertools import permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/SUPPORT_DROP_T8_MIXED_SHELL_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/SUPPORT_DROP_T8_MIXED_SHELL_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Point = tuple[int, int, int]
Rotation = tuple[tuple[int, int, int], tuple[int, int, int]]

BALL_RADIUS = 6
TARGET_T = 8
ORIGIN: Point = (0, 0, 0)
SHIFTS: tuple[Point, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
FORBIDDEN_PHRASES = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE")


def permutation_sign(permutation: tuple[int, int, int]) -> int:
    inversions = sum(
        permutation[i] > permutation[j]
        for i in range(3)
        for j in range(i + 1, 3)
    )
    return -1 if inversions % 2 else 1


ROTATIONS: tuple[Rotation, ...] = tuple(
    (permutation, signs)
    for permutation in permutations((0, 1, 2))
    for signs in product((-1, 1), repeat=3)
    if permutation_sign(permutation) * signs[0] * signs[1] * signs[2] == 1
)


def rotate_vector(rotation: Rotation, vector: Point) -> Point:
    permutation, signs = rotation
    result = [0, 0, 0]
    for source_axis in range(3):
        result[permutation[source_axis]] = signs[source_axis] * vector[source_axis]
    return (result[0], result[1], result[2])


def taxicab(point: Point) -> int:
    return abs(point[0]) + abs(point[1]) + abs(point[2])


def euclidean_sq(point: Point) -> int:
    return point[0] * point[0] + point[1] * point[1] + point[2] * point[2]


def support_weight(point: Point) -> int:
    return sum(coord != 0 for coord in point)


def in_ball(point: Point) -> bool:
    return taxicab(point) <= BALL_RADIUS


def ball_sites() -> tuple[Point, ...]:
    sites: list[Point] = []
    for x in range(-BALL_RADIUS, BALL_RADIUS + 1):
        for y in range(-BALL_RADIUS, BALL_RADIUS + 1):
            remain = BALL_RADIUS - abs(x) - abs(y)
            for z in range(-remain, remain + 1):
                sites.append((x, y, z))
    return tuple(sites)


def hop_cost(source: Point, target: Point) -> int:
    """Named support-drop hop-cost nu, as in the noshrt rule."""
    source_weight = support_weight(source)
    target_weight = support_weight(target)
    if source_weight == 0 or (source_weight == 1 and target_weight == 1) or target_weight < source_weight:
        return 3
    return 1


def neighbors_in_ball(site: Point) -> tuple[Point, ...]:
    out: list[Point] = []
    for shift in SHIFTS:
        candidate = (site[0] + shift[0], site[1] + shift[1], site[2] + shift[2])
        if in_ball(candidate):
            out.append(candidate)
    return tuple(out)


def one_dijkstra(sites: tuple[Point, ...]) -> dict[Point, int]:
    """Single-source first-arrival times from the origin. Called once."""
    infinity = 10**9
    dist = {site: infinity for site in sites}
    dist[ORIGIN] = 0
    heap: list[tuple[int, Point]] = [(0, ORIGIN)]
    while heap:
        time, site = heappop(heap)
        if time != dist[site]:
            continue
        for nxt in neighbors_in_ball(site):
            arrival = time + hop_cost(site, nxt)
            if arrival < dist[nxt]:
                dist[nxt] = arrival
                heappush(heap, (arrival, nxt))
    return dist


def gplus_orbit(point: Point) -> frozenset[Point]:
    return frozenset(rotate_vector(rotation, point) for rotation in ROTATIONS)


def representative(orbit: frozenset[Point]) -> Point:
    """Lexicographically maximal first-octant member of a G+ orbit."""
    octant = tuple(point for point in orbit if point[0] >= 0 and point[1] >= 0 and point[2] >= 0)
    if not octant:
        raise ValueError("G+ orbit has no first-octant representative")
    return max(octant)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool, residual: object | None = None) -> None:
        ok = bool(condition)
        self.passed += int(ok)
        self.failed += int(not ok)
        print(f"{'PASS' if ok else 'FAIL'}: {label} — {statement}")
        if not ok and residual is not None:
            print(f"  residual: {residual}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return 0 if self.failed == 0 else 1


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    for relative in AUDIT_INPUT_PATHS:
        (ROOT / relative).read_text(encoding="utf-8")

    print("construction: one Dijkstra for named support-drop hop-cost nu on B_6(0)")
    print("negative_scope: nu is displayed, not written into Admissibility; L1 is not attached")

    checks.check(
        "audit-inputs",
        "AUDIT_INPUT_PATHS is the required string-literal pair and both files exist",
        AUDIT_INPUT_PATHS == (
            "docs/SUPPORT_DROP_T8_MIXED_SHELL_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and AUDIT_TIMEOUT_SEC == 120
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file(),
    )

    sites = ball_sites()
    site_set = frozenset(sites)
    checks.check(
        "ball-census",
        "B_6(0) has 377 integer sites and 376 nonzero sites",
        len(sites) == 377 and ORIGIN in site_set and len(sites) - 1 == 376,
        residual=len(sites),
    )
    checks.check(
        "rotation-group",
        "the proper cubic group used for types has 24 elements",
        len(ROTATIONS) == 24 and len(set(ROTATIONS)) == 24,
    )

    arrivals = one_dijkstra(sites)
    checks.check(
        "one-dijkstra-total",
        "every site of B_6(0) receives a finite arrival time",
        all(arrivals[site] < 10**9 for site in sites),
    )
    checks.check(
        "reverse-critical-shell",
        "t(2,2,2)=8 and t(4,0,0)=10, so t=8 is the reverse-critical shell",
        arrivals[(2, 2, 2)] == TARGET_T and arrivals[(4, 0, 0)] == 10,
        residual=(arrivals[(2, 2, 2)], arrivals[(4, 0, 0)]),
    )
    checks.check(
        "l1-not-identified",
        "arrival t is not the taxicab length: t(1,0,0)=3 and t(2,2,2)=8 != 6",
        arrivals[(1, 0, 0)] == 3 and arrivals[(2, 2, 2)] != taxicab((2, 2, 2)),
    )

    seed_exit = hop_cost(ORIGIN, (1, 0, 0))
    axis_step = hop_cost((1, 0, 0), (2, 0, 0))
    support_drop = hop_cost((1, 1, 0), (1, 0, 0))
    support_gain = hop_cost((1, 0, 0), (1, 1, 0))
    equal_off_axis = hop_cost((1, 1, 0), (2, 1, 0))
    checks.check(
        "named-nu-clauses",
        "nu is 3 on seed-exit, both-weight-1, and support drop, else 1",
        seed_exit == 3
        and axis_step == 3
        and support_drop == 3
        and support_gain == 1
        and equal_off_axis == 1,
    )

    t8_sites = tuple(site for site in sites if site != ORIGIN and arrivals[site] == TARGET_T)
    consumed: set[Point] = set()
    rows: list[tuple[Point, int, int]] = []
    for site in t8_sites:
        if site in consumed:
            continue
        orbit = gplus_orbit(site)
        orbit_in_ball = frozenset(point for point in orbit if point in site_set)
        checks.check(
            "orbit-inside-ball",
            f"the G+ orbit of {representative(orbit)} lies in B_6(0)",
            orbit == orbit_in_ball,
            residual=(len(orbit), len(orbit_in_ball)),
        )
        times = {arrivals[point] for point in orbit_in_ball}
        checks.check(
            "orbit-constant-t",
            f"arrival is constant on the G+ orbit of {representative(orbit)}",
            times == {TARGET_T},
            residual=times,
        )
        consumed.update(orbit_in_ball)
        rep = representative(orbit_in_ball)
        rows.append((rep, euclidean_sq(rep), len(orbit_in_ball)))
    rows.sort()

    radii = sorted({radius_sq for _, radius_sq, _ in rows})
    print("t8_gplus_types:")
    for rep, radius_sq, orbit_size in rows:
        print(f"  {rep}  |v|_2^2={radius_sq}  orbit={orbit_size}")
    print(f"t8_radius_squares: {radii}")

    expected_rows = (
        ((2, 2, 2), 12, 8),
        ((3, 1, 2), 14, 24),
        ((3, 2, 1), 14, 24),
        ((3, 3, 0), 18, 12),
        ((4, 1, 1), 18, 24),
        ((4, 2, 0), 20, 24),
        ((5, 1, 0), 26, 24),
    )
    checks.check(
        "thm1-lex-list",
        "the lex-sorted G+ representatives at t=8 are the seven computed types",
        tuple(rows) == expected_rows,
        residual=rows,
    )
    checks.check(
        "thm1-contains-222",
        "the reverse-critical body-diagonal type (2,2,2) is on the t=8 list",
        rows[0] == ((2, 2, 2), 12, 8),
    )
    checks.check(
        "thm1-note-table",
        "the note displays each representative with |v|_2^2 and orbit size",
        all(
            f"| `{rep[0]},{rep[1]},{rep[2]}` | {radius_sq} | {orbit_size} |"
            in note
            or f"| `({rep[0]},{rep[1]},{rep[2]})` | {radius_sq} | {orbit_size} |"
            in note
            for rep, radius_sq, orbit_size in rows
        ),
    )
    checks.check(
        "thm2-mixed-radii",
        "the t=8 list uses more than one Euclidean radius",
        len(radii) > 1 and radii == [12, 14, 18, 20, 26],
        residual=radii,
    )
    checks.check(
        "thm2-shared-radius-not-same-type",
        "(3,3,0) and (4,1,1) share |v|_2^2=18 but are distinct G+ types",
        ((3, 3, 0), 18, 12) in rows and ((4, 1, 1), 18, 24) in rows,
    )
    checks.check(
        "thm2-chiral-pair",
        "(3,1,2) and (3,2,1) are distinct 24-point G+ orbits of the same radius",
        gplus_orbit((3, 1, 2)).isdisjoint(gplus_orbit((3, 2, 1)))
        and len(gplus_orbit((3, 1, 2))) == 24
        and len(gplus_orbit((3, 2, 1))) == 24
        and euclidean_sq((3, 1, 2)) == euclidean_sq((3, 2, 1)) == 14,
    )
    checks.check(
        "coverage",
        "the seven orbits partition every t=8 site and omit every other site",
        len(t8_sites) == sum(orbit_size for _, _, orbit_size in rows) == 140
        and consumed == set(t8_sites),
        residual=len(t8_sites),
    )

    lattice_lead = "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor"
    lattice_tail = "adjacency, standard translations, and proper cubic rotations about each site."
    admissibility_lead = "For each site, the probability distribution over the possibilities is"
    admissibility_tail = "determined by, and varies with, the nearest-neighbor conditions."
    record_lock = "When present, a record locks exactly one admissible local possibility."
    checks.check(
        "source-lattice",
        "current Lattice wording is pinned in the axiom memo and the note",
        lattice_lead in axiom and lattice_tail in axiom and lattice_lead in note and lattice_tail in note,
    )
    checks.check(
        "source-admissibility",
        "current Admissibility wording is pinned and nu is not written into it",
        admissibility_lead in axiom
        and admissibility_tail in axiom
        and admissibility_lead in note
        and admissibility_tail in note
        and "Do not write ν into Admissibility." in note
        and "hypothetical_axiom_status: no edit" in note,
    )
    checks.check(
        "thm3-no-l1",
        "the note refuses to attach L1 and treats the list as displayed, not adopted",
        "Do not attach L1." in note
        and "Displayed, not adopted." in note
        and "displayed, not adopted" in note.lower(),
    )
    checks.check(
        "claim-scope",
        "front matter carries the declared claim_scope",
        "The G+ site-types that share arrival t=8 under the named support-drop hop-cost on B_6(0) are named. Displayed, not adopted."
        in note,
    )
    checks.check(
        "forbidden-phrases",
        "the note avoids the dispatch-forbidden phrases",
        all(phrase not in note for phrase in FORBIDDEN_PHRASES),
    )
    checks.check(
        "record-unused",
        "Record is quoted only as an unused boundary",
        record_lock in axiom and record_lock in note and "Record is not used" in note,
    )
    checks.check(
        "b6-only",
        "every executed hop and every named type stays inside B_6(0)",
        all(in_ball(site) for site in sites)
        and all(in_ball(rep) for rep, _, _ in rows)
        and BALL_RADIUS == 6
        and "B_6(0) only" in note,
    )

    print("per_element: checked exactly — each t=8 G+ representative, |v|_2^2, and orbit size")
    print("per_site: checked exactly — first-arrival on the 377-site ball")
    print("per_mode: not used")
    print("per_block: checked exactly — the seven-orbit partition of the t=8 shell")
    print("lattice_wide: checked and not executed — no law outside B_6(0) is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
