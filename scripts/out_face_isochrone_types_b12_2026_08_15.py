#!/usr/bin/env python3
"""Count G+ types on the t(2,2,2) and t(4,4,4) shells of the out-face hop-cost.

One origin Dijkstra on B_12(0). No cache write. No axiom edit.
"""

from __future__ import annotations

import ast
import heapq
from itertools import permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/OUT_FACE_ISOCHRONE_TYPES_B12_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/OUT_FACE_ISOCHRONE_TYPES_B12_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
CLAIM_SCOPE = (
    "Isochrone type counts of the t(2,2,2) and t(4,4,4) shells under "
    "the named out-face hop-cost on B_12(0) are reported. "
    "Displayed, not adopted."
)
NEIGH = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
FORBIDDEN_PARTS = (
    ("G_", "N"),
    ("1/", "r"),
    ("1/", "r^2"),
    ("Lattice-", "named"),
    ("not a ", "TOE"),
)
T10_EXPECTED = (
    ((2, 2, 2), 12, 8),
    ((3, 1, 0), 10, 24),
    ((3, 1, 2), 14, 24),
    ((3, 2, 1), 14, 24),
)
T16_EXPECTED = (
    ((4, 4, 0), 32, 12),
    ((4, 4, 4), 48, 8),
    ((5, 1, 0), 26, 24),
    ((5, 3, 0), 34, 24),
    ((5, 3, 4), 50, 24),
    ((5, 4, 3), 50, 24),
    ((5, 5, 2), 54, 24),
    ((6, 1, 1), 38, 24),
    ((6, 1, 5), 62, 24),
    ((6, 2, 0), 40, 24),
    ((6, 2, 4), 56, 24),
    ((6, 3, 3), 54, 24),
    ((6, 4, 2), 56, 24),
    ((6, 5, 1), 62, 24),
    ((7, 1, 4), 66, 24),
    ((7, 2, 3), 62, 24),
    ((7, 3, 2), 62, 24),
    ((7, 4, 1), 66, 24),
    ((8, 1, 3), 74, 24),
    ((8, 2, 2), 72, 24),
    ((8, 3, 1), 74, 24),
    ((9, 1, 2), 86, 24),
    ((9, 2, 1), 86, 24),
)
KAPPA_T10 = (6, 5)
KAPPA_T16 = (25, 13)
DIJKSTRA_CALLS = 0
Point = tuple[int, int, int]
Rotation = tuple[tuple[int, int, int], tuple[int, int, int]]


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


def rotate_vector(rotation: Rotation, vector: Point) -> Point:
    permutation, signs = rotation
    result = [0, 0, 0]
    for source_axis in range(3):
        result[permutation[source_axis]] = signs[source_axis] * vector[source_axis]
    return (result[0], result[1], result[2])


def l1(v: Point) -> int:
    return abs(v[0]) + abs(v[1]) + abs(v[2])


def support_size(v: Point) -> int:
    return int(v[0] != 0) + int(v[1] != 0) + int(v[2] != 0)


def least_nonzero_abs(v: Point) -> int | None:
    nonzero = [abs(c) for c in v if c != 0]
    if not nonzero:
        return None
    return min(nonzero)


def unit_coord_count(v: Point) -> int:
    return int(abs(v[0]) == 1) + int(abs(v[1]) == 1) + int(abs(v[2]) == 1)


def r2(v: Point) -> int:
    return v[0] * v[0] + v[1] * v[1] + v[2] * v[2]


def is_body_diagonal(v: Point) -> bool:
    return v != (0, 0, 0) and abs(v[0]) == abs(v[1]) == abs(v[2])


def ball(radius: int) -> list[Point]:
    sites: list[Point] = []
    for x in range(-radius, radius + 1):
        for y in range(-radius, radius + 1):
            rem = radius - abs(x) - abs(y)
            for z in range(-rem, rem + 1):
                sites.append((x, y, z))
    return sites


def nu_cost(v: Point, w: Point) -> int:
    sigma_v = support_size(v)
    sigma_w = support_size(w)
    if sigma_v == 0 or (sigma_v == 1 and sigma_w == 1) or sigma_w < sigma_v:
        return 3
    return 1


def mu_cost(v: Point, w: Point) -> int:
    if nu_cost(v, w) == 3:
        return 3
    if support_size(v) == 2 and support_size(w) == 2 and least_nonzero_abs(w) == 1:
        return 3
    return 1


def rho3_cost(v: Point, w: Point) -> int:
    if mu_cost(v, w) == 3:
        return 3
    if support_size(v) == 3 and support_size(w) == 3 and unit_coord_count(w) == 2:
        return 3
    return 1


def kappa_cost(v: Point, w: Point) -> int:
    if rho3_cost(v, w) == 3:
        return 3
    if support_size(v) == 2 and support_size(w) == 3 and unit_coord_count(w) == 2:
        return 3
    return 1


def omega_cost(v: Point, w: Point) -> int:
    if rho3_cost(v, w) == 3:
        return 3
    if support_size(v) == 2 and support_size(w) == 2:
        if max(abs(coord) for coord in w) > max(abs(coord) for coord in v):
            return 3
    return 1


def dijkstra_omega(sites: list[Point]) -> dict[Point, int]:
    global DIJKSTRA_CALLS
    DIJKSTRA_CALLS += 1
    site_set = set(sites)
    dist: dict[Point, int] = {(0, 0, 0): 0}
    heap: list[tuple[int, Point]] = [(0, (0, 0, 0))]
    seen: set[Point] = set()
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
            nd = d + omega_cost(v, w)
            if nd < dist.get(w, 10**9):
                dist[w] = nd
                heapq.heappush(heap, (nd, w))
    return dist


def gplus_orbit(point: Point) -> frozenset[Point]:
    return frozenset(rotate_vector(rotation, point) for rotation in ROTATIONS)


def representative(orbit: frozenset[Point]) -> Point:
    octant = tuple(point for point in orbit if point[0] >= 0 and point[1] >= 0 and point[2] >= 0)
    if not octant:
        raise ValueError("G+ orbit has no first-octant representative")
    return max(octant)


def shell_types(
    dist: dict[Point, int],
    site_set: set[Point],
    arrival: int,
) -> tuple[list[Point], list[tuple[Point, int, int]], tuple[int, ...]]:
    pts = [v for v, t in dist.items() if t == arrival and v != (0, 0, 0)]
    consumed: set[Point] = set()
    rows: list[tuple[Point, int, int]] = []
    for site in pts:
        if site in consumed:
            continue
        orbit = gplus_orbit(site)
        if not orbit.issubset(site_set):
            raise AssertionError(f"orbit of {site} leaves B_12(0)")
        times = {dist[point] for point in orbit}
        if times != {arrival}:
            raise AssertionError(f"arrival not constant on orbit of {site}: {times}")
        consumed.update(orbit)
        rep = representative(orbit)
        rows.append((rep, r2(rep), len(orbit)))
    rows.sort()
    if consumed != set(pts):
        raise AssertionError("G+ orbits do not partition the shell")
    radii = tuple(sorted({radius for _, radius, _ in rows}))
    return pts, rows, radii


def literal_audit_paths(source: str) -> tuple[str, ...] | None:
    module = ast.parse(source)
    for node in module.body:
        if not isinstance(node, ast.Assign):
            continue
        if not any(isinstance(t, ast.Name) and t.id == "AUDIT_INPUT_PATHS" for t in node.targets):
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
        "note claim_scope matches the isochrone type-count statement",
        CLAIM_SCOPE in note.replace("\n", " "),
    )
    checks.check(
        "displayed-not-adopted",
        "the census is displayed, not adopted",
        "Displayed, not adopted" in note or "displayed, not adopted" in note,
    )
    checks.check(
        "not-in-admissibility",
        "ω is not written into Admissibility",
        "Do not write `ω` into Admissibility" in note,
    )
    checks.check(
        "not-attach-l1",
        "the displayed rule is not attached to L1",
        "Do not attach L1" in note and "Do not attach L1" not in axiom,
    )
    checks.check(
        "uniqueness-not-claimed",
        "uniqueness among hop-costs is not claimed",
        "Uniqueness is not claimed" in note,
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
    checks.check(
        "cache-false",
        "the note records cache_write false",
        "cache_write: false" in note,
    )

    sites = ball(12)
    site_set = set(sites)
    nonzero = [v for v in sites if v != (0, 0, 0)]
    dist = dijkstra_omega(sites)
    t2 = dist[(2, 2, 2)]
    t4 = dist[(4, 4, 4)]
    t111 = dist[(1, 1, 1)]
    t333 = dist[(3, 3, 3)]
    t10_sites, t10_rows, t10_radii = shell_types(dist, site_set, t2)
    t16_sites, t16_rows, t16_radii = shell_types(dist, site_set, t4)
    t10_reps = {rep for rep, _, _ in t10_rows}
    t16_reps = {rep for rep, _, _ in t16_rows}
    out_face_hop = ((1, 1, 0), (2, 1, 0))
    face_growth = ((2, 2, 0), (3, 2, 0))
    ridge_enter = ((2, 1, 0), (2, 1, 1))
    interior_hop = ((2, 2, 2), (3, 2, 2))
    body_t10 = [v for v in t10_sites if is_body_diagonal(v)]
    body_types_t10 = {tuple(sorted(abs(c) for c in v)) for v in body_t10}
    t10_mixed = len(t10_radii) > 1
    t16_mixed = len(t16_radii) > 1

    print(f"n_sites {len(sites)}")
    print(f"t2 {t2} t4 {t4}")
    print(f"t10_sites {len(t10_sites)} t10_types {len(t10_rows)} t10_n_r2 {len(t10_radii)}")
    print(f"t16_sites {len(t16_sites)} t16_types {len(t16_rows)} t16_n_r2 {len(t16_radii)}")
    print(f"t10_radii {list(t10_radii)}")
    print(f"t16_radii {list(t16_radii)}")
    print(f"t(2,2,2) {t2}")
    print(f"t(4,4,4) {t4}")
    print(f"t(1,1,1) {t111}")
    print(f"t(3,3,3) {t333}")
    print(f"has_222_in_t10 {(2, 2, 2) in t10_reps}")
    print(f"has_444_in_t16 {(4, 4, 4) in t16_reps}")
    print(f"body_t10 {len(body_t10)} body_types_t10 {sorted(body_types_t10)}")
    print(f"t10_mixed {t10_mixed}")
    print(f"t16_mixed {t16_mixed}")
    print(f"versus_kappa_t10 {KAPPA_T10} versus_kappa_t16 {KAPPA_T16}")
    print(f"dijkstra_calls {DIJKSTRA_CALLS}")
    print(f"omega_out_face {omega_cost(*out_face_hop)}")
    print(f"omega_face_growth {omega_cost(*face_growth)}")
    print(f"rho3_face_growth {rho3_cost(*face_growth)}")
    print(f"kappa_face_growth {kappa_cost(*face_growth)}")
    print(f"omega_ridge_enter {omega_cost(*ridge_enter)}")
    print(f"kappa_ridge_enter {kappa_cost(*ridge_enter)}")
    print(f"omega_interior {omega_cost(*interior_hop)}")

    checks.check(
        "one-dijkstra",
        "exactly one Dijkstra ran",
        DIJKSTRA_CALLS == 1,
    )
    checks.check(
        "ball-b12",
        "B_12(0) has 2625 sites and 2624 nonzero sites",
        len(sites) == 2625 and len(nonzero) == 2624 and all(l1(v) <= 12 for v in sites),
    )
    checks.check(
        "reachable",
        "every site of B_12(0) is reached",
        len(dist) == 2625,
    )
    checks.check(
        "rotation-group",
        "the proper cubic group used for types has 24 elements",
        len(ROTATIONS) == 24 and len(set(ROTATIONS)) == 24,
    )
    checks.check(
        "t10-counts",
        "t=10 has 80 sites, 4 G+ types, and 3 distinct |v|_2^2",
        t2 == 10
        and len(t10_sites) == 80
        and len(t10_rows) == 4
        and len(t10_radii) == 3
        and tuple(t10_rows) == T10_EXPECTED
        and t10_radii == (10, 12, 14),
    )
    checks.check(
        "t16-counts",
        "t=16 has 524 sites, 23 G+ types, and 14 distinct |v|_2^2",
        t4 == 16
        and len(t16_sites) == 524
        and len(t16_rows) == 23
        and len(t16_radii) == 14
        and tuple(t16_rows) == T16_EXPECTED
        and t16_radii == (26, 32, 34, 38, 40, 48, 50, 54, 56, 62, 66, 72, 74, 86),
    )
    checks.check(
        "counts-do-not-stay",
        "type counts under ω are not the κ pair 6/5 and 25/13",
        (len(t10_rows), len(t10_radii)) != KAPPA_T10
        and (len(t16_rows), len(t16_radii)) != KAPPA_T16
        and (len(t10_rows), len(t10_radii)) == (4, 3)
        and (len(t16_rows), len(t16_radii)) == (23, 14)
        and "do not stay" in note
        and "6/5" in note
        and "25/13" in note
        and "4/3" in note
        and "23/14" in note,
    )
    checks.check(
        "t-222-in-t10",
        "(2,2,2) sits in the t=10 shell",
        t2 == 10 and (2, 2, 2) in t10_reps and r2((2, 2, 2)) == 12,
    )
    checks.check(
        "t-444-in-t16",
        "(4,4,4) sits in the t=16 shell",
        t4 == 16 and (4, 4, 4) in t16_reps and r2((4, 4, 4)) == 48,
    )
    checks.check(
        "unique-body-diagonal",
        "(2,2,2) is the unique body-diagonal type in its shell",
        len(body_t10) == 8
        and body_types_t10 == {(2, 2, 2)}
        and (2, 2, 2) in t10_reps
        and (1, 1, 1) not in t10_reps
        and (3, 3, 3) not in t10_reps
        and t111 == 5
        and t333 == 13
        and "unique body-diagonal" in note,
    )
    checks.check(
        "shells-mixed",
        "the t(2,2,2) and t(4,4,4) shells remain mixed",
        t10_mixed and t16_mixed and "remain mixed" in note,
    )
    checks.check(
        "not-leftover-of-kappa",
        "ω prices face-growth 2→2 at 3 while κ and ρ3 price it at 1",
        omega_cost(*face_growth) == 3
        and rho3_cost(*face_growth) == 1
        and kappa_cost(*face_growth) == 1
        and omega_cost(*out_face_hop) == 3
        and omega_cost(*ridge_enter) == 1
        and kappa_cost(*ridge_enter) == 3
        and omega_cost(*interior_hop) == 1
        and "cannot price out-face" in note
        and "(2,2,0) → (3,2,0)" in note,
    )
    checks.check(
        "note-records-counts",
        "note records site, type, and radius counts for both shells",
        "| `10` | `80` | `4` | `3` |" in note
        and "| `16` | `524` | `23` | `14` |" in note,
    )
    checks.check(
        "note-records-memberships",
        "note records (2,2,2) in t=10 and (4,4,4) in t=16",
        "t(2,2,2) = 10" in note
        and "t(4,4,4) = 16" in note
        and "(2,2,2)` is in" in note
        and "(4,4,4)` is in" in note,
    )
    checks.check(
        "chiral-pairs-split",
        "abs-sorted first-octant form still splits G+ chiral pairs",
        gplus_orbit((3, 1, 2)).isdisjoint(gplus_orbit((3, 2, 1)))
        and gplus_orbit((5, 3, 4)).isdisjoint(gplus_orbit((5, 4, 3)))
        and ((3, 1, 2), 14, 24) in t10_rows
        and ((3, 2, 1), 14, 24) in t10_rows
        and ((5, 3, 4), 50, 24) in t16_rows
        and ((5, 4, 3), 50, 24) in t16_rows,
    )
    checks.check(
        "seed-and-out-face-clauses",
        "ν clauses, corridor-slide, ridge 3→3, and out-face 2→2 cost 3; 1→2, ridge-enter, and non-ridge 3→3 cost 1",
        omega_cost((0, 0, 0), (1, 0, 0)) == 3
        and omega_cost((1, 0, 0), (2, 0, 0)) == 3
        and omega_cost((1, 1, 0), (1, 0, 0)) == 3
        and omega_cost((1, 1, 0), (2, 1, 0)) == 3
        and omega_cost((2, 2, 0), (3, 2, 0)) == 3
        and omega_cost((1, 1, 1), (2, 1, 1)) == 3
        and omega_cost((1, 0, 0), (1, 1, 0)) == 1
        and omega_cost((1, 1, 0), (1, 1, 1)) == 1
        and omega_cost((2, 1, 0), (2, 1, 1)) == 1
        and omega_cost((2, 2, 2), (3, 2, 2)) == 1,
    )
    checks.check(
        "axiom-untouched",
        "the axiom memo is an input only and still names the four axioms",
        "### Admissibility / Local Constraint" in axiom
        and "ω(v→w)" not in axiom
        and "κ(v→w)" not in axiom
        and "ρ3(v→w)" not in axiom,
    )
    checks.check(
        "b12-only",
        "every named type stays inside B_12(0)",
        all(l1(rep) <= 12 for rep, _, _ in t10_rows)
        and all(l1(rep) <= 12 for rep, _, _ in t16_rows)
        and l1((4, 4, 4)) == 12
        and "B_12(0) only" in note,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
