#!/usr/bin/env python3
"""Name G+ types on the t=14 shell of the support-drop hop-cost.

One origin Dijkstra on B_12(0). No cache write. No axiom edit.
"""

from __future__ import annotations

import ast
import heapq
from itertools import permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/SUPPORT_DROP_T14_SHELL_TYPES_B12_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/SUPPORT_DROP_T14_SHELL_TYPES_B12_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
CLAIM_SCOPE = (
    "G+ types of the t=14 shell under "
    "the named support-drop hop-cost on B_12(0) are named. "
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
T14_EXPECTED = (
    ((4, 4, 4), 8),
    ((5, 3, 4), 24),
    ((5, 4, 3), 24),
    ((5, 5, 2), 24),
    ((6, 1, 5), 24),
    ((6, 2, 4), 24),
    ((6, 3, 3), 24),
    ((6, 4, 2), 24),
    ((6, 5, 1), 24),
    ((6, 6, 0), 12),
    ((7, 1, 4), 24),
    ((7, 2, 3), 24),
    ((7, 3, 2), 24),
    ((7, 4, 1), 24),
    ((7, 5, 0), 24),
    ((8, 0, 0), 6),
    ((8, 1, 3), 24),
    ((8, 2, 2), 24),
    ((8, 3, 1), 24),
    ((8, 4, 0), 24),
    ((9, 1, 2), 24),
    ((9, 2, 1), 24),
    ((9, 3, 0), 24),
    ((10, 1, 1), 24),
    ((10, 2, 0), 24),
    ((11, 1, 0), 24),
)
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


def dijkstra_nu(sites: list[Point]) -> dict[Point, int]:
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
            nd = d + nu_cost(v, w)
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
) -> tuple[list[Point], list[tuple[Point, int]]]:
    pts = [v for v, t in dist.items() if t == arrival and v != (0, 0, 0)]
    consumed: set[Point] = set()
    rows: list[tuple[Point, int]] = []
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
        rows.append((representative(orbit), len(orbit)))
    rows.sort()
    if consumed != set(pts):
        raise AssertionError("G+ orbits do not partition the shell")
    return pts, rows


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
        "note claim_scope matches the t=14 type-naming statement",
        CLAIM_SCOPE in note.replace("\n", " "),
    )
    checks.check(
        "displayed-not-adopted",
        "the census is displayed, not adopted",
        "Displayed, not adopted" in note or "displayed, not adopted" in note,
    )
    checks.check(
        "not-in-admissibility",
        "ν is not written into Admissibility",
        "Do not write `ν` into Admissibility" in note,
    )
    checks.check(
        "not-attach-l1",
        "the displayed rule is not attached to L1",
        "Do not attach L1" in note,
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

    sites = ball(12)
    site_set = set(sites)
    nonzero = [v for v in sites if v != (0, 0, 0)]
    dist = dijkstra_nu(sites)
    t14_sites, t14_rows = shell_types(dist, site_set, 14)
    t800 = dist[(8, 0, 0)]
    t444 = dist[(4, 4, 4)]
    t14_reps = {rep for rep, _ in t14_rows}

    print(f"n_sites {len(sites)}")
    print(f"t14_sites {len(t14_sites)} t14_types {len(t14_rows)}")
    print(f"t(8,0,0) {t800}")
    print(f"t(4,4,4) {t444}")
    print(f"same_shell {t800 == 14 and t444 == 14}")
    print("t14_types_named")
    for rep, count in t14_rows:
        print(f"  {rep} {count}")
    print(f"dijkstra_calls {DIJKSTRA_CALLS}")

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
        "t14-named-types",
        "t=14 has 578 sites in 26 named G+ types with the computed site counts",
        len(t14_sites) == 578
        and len(t14_rows) == 26
        and tuple(t14_rows) == T14_EXPECTED
        and sum(count for _, count in t14_rows) == 578,
    )
    checks.check(
        "t-800-and-444",
        "(8,0,0) and (4,4,4) both have t=14",
        t800 == 14
        and t444 == 14
        and (8, 0, 0) in t14_reps
        and (4, 4, 4) in t14_reps,
    )
    checks.check(
        "not-leftover-of-counts",
        "named types are not leftover of the 26/15 counts",
        "not leftover of the 26/15 counts" in note
        and "does not name the representatives" in note,
    )
    checks.check(
        "note-records-types",
        "note records every lex-sorted representative with its site count",
        all(
            f"| `({rep[0]},{rep[1]},{rep[2]})` | {count} |" in note
            for rep, count in t14_rows
        ),
    )
    checks.check(
        "note-records-shared-shell",
        "note records that (8,0,0) and (4,4,4) both have t=14",
        "t(8,0,0) = 14" in note
        and "t(4,4,4) = 14" in note
        and "(8,0,0)` and `(4,4,4)` both have `t=14" in note,
    )
    checks.check(
        "chiral-pairs-split",
        "abs-sorted first-octant form still splits G+ chiral pairs",
        gplus_orbit((5, 3, 4)).isdisjoint(gplus_orbit((5, 4, 3)))
        and ((5, 3, 4), 24) in t14_rows
        and ((5, 4, 3), 24) in t14_rows,
    )
    checks.check(
        "seed-and-axis-clauses",
        "seed-exit and both-weights-1 cost 3; support increase costs 1",
        nu_cost((0, 0, 0), (1, 0, 0)) == 3
        and nu_cost((1, 0, 0), (2, 0, 0)) == 3
        and nu_cost((1, 0, 0), (1, 1, 0)) == 1
        and nu_cost((1, 1, 0), (1, 1, 1)) == 1
        and nu_cost((1, 1, 0), (1, 0, 0)) == 3,
    )
    checks.check(
        "axiom-untouched",
        "the axiom memo is an input only and still names the four axioms",
        "### Admissibility / Local Constraint" in axiom
        and "ν(v→w)" not in axiom,
    )
    checks.check(
        "b12-only",
        "every named type stays inside B_12(0)",
        all(l1(rep) <= 12 for rep, _ in t14_rows)
        and "B_12(0) only" in note,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
