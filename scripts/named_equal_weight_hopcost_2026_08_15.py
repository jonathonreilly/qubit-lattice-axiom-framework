#!/usr/bin/env python3
"""Named equal-weight hop-cost versus the minkbest 8-tuple on B_4(0).

The local-in-weights rule rho assigns cost 3 when the inward occupancies of
the two ends have equal Hamming weight or the source is the seed (weight 0),
and cost 1 otherwise. This runner checks that rho reproduces the displayed
eight-orbit filling (3,1,3,1,1,3,1,1) and names the new B_4 orbit (3,3) by
rho(3,3)=3. On B_4(0) the resulting arrival table equals the table obtained
by omitting that new orbit or by assigning it any cost at least 3. The rule
is displayed, not adopted. Uniqueness of rho is not claimed. No axiom edit
and no path-length law.
"""

from __future__ import annotations

import heapq
from collections import defaultdict
from itertools import permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "NAMED_EQUAL_WEIGHT_HOPCOST_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/NAMED_EQUAL_WEIGHT_HOPCOST_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Point = tuple[int, int, int]
SHIFTS: tuple[Point, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
SHIFT_INDEX = {shift: index for index, shift in enumerate(SHIFTS)}
ORIGIN: Point = (0, 0, 0)
AXIS3: Point = (3, 0, 0)
DIAG3: Point = (1, 1, 1)
AXIS4: Point = (4, 0, 0)
MINKBEST: tuple[int, ...] = (3, 1, 3, 1, 1, 3, 1, 1)
EXPECTED_WEIGHTS: tuple[Point, ...] = (
    (0, 1),
    (1, 0),
    (1, 1),
    (1, 2),
    (2, 1),
    (2, 2),
    (2, 3),
    (3, 2),
)


def forbidden_tokens() -> tuple[str, ...]:
    return (
        "G" + "_N",
        "1/" + "r",
        "1/" + "r^2",
        "Lattice-" + "named",
        "not a " + "TOE",
    )


def graph_radius(point: Point) -> int:
    return abs(point[0]) + abs(point[1]) + abs(point[2])


def ball(radius: int) -> tuple[Point, ...]:
    sites: list[Point] = []
    span = range(-radius, radius + 1)
    for coords in product(span, repeat=3):
        if graph_radius(coords) <= radius:
            sites.append(coords)
    return tuple(sites)


def occupancy(point: Point) -> int:
    """6-bit inward occupation of the one-seed front at ``point``."""
    bits = 0
    for index, shift in enumerate(SHIFTS):
        neighbor = (
            point[0] + shift[0],
            point[1] + shift[1],
            point[2] + shift[2],
        )
        if graph_radius(neighbor) < graph_radius(point):
            bits |= 1 << index
    return bits


def weight(bits: int) -> int:
    return bin(bits).count("1")


def rho(weight_v: int, weight_w: int) -> int:
    """Named rule: cost 3 iff equal inward weight or seed-exit, else 1."""
    if weight_v == weight_w or weight_v == 0:
        return 3
    return 1


def apply_matrix(matrix: tuple[tuple[int, ...], ...], point: Point) -> Point:
    return (
        matrix[0][0] * point[0] + matrix[0][1] * point[1] + matrix[0][2] * point[2],
        matrix[1][0] * point[0] + matrix[1][1] * point[1] + matrix[1][2] * point[2],
        matrix[2][0] * point[0] + matrix[2][1] * point[1] + matrix[2][2] * point[2],
    )


def determinant(matrix: tuple[tuple[int, ...], ...]) -> int:
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def proper_cubic_rotations() -> tuple[tuple[tuple[int, ...], ...], ...]:
    rotations: list[tuple[tuple[int, ...], ...]] = []
    for perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            rows = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            for src, dest in enumerate(perm):
                rows[src][dest] = signs[src]
            matrix = tuple(tuple(row) for row in rows)
            if determinant(matrix) == 1:
                rotations.append(matrix)
    return tuple(rotations)


def bit_permutation(matrix: tuple[tuple[int, ...], ...]) -> tuple[int, ...]:
    return tuple(SHIFT_INDEX[apply_matrix(matrix, shift)] for shift in SHIFTS)


def apply_bits(perm: tuple[int, ...], bits: int) -> int:
    out = 0
    for index in range(6):
        if bits >> index & 1:
            out |= 1 << perm[index]
    return out


def apply_pair(perm: tuple[int, ...], pair: tuple[int, int]) -> tuple[int, int]:
    return (apply_bits(perm, pair[0]), apply_bits(perm, pair[1]))


def orbit_rep(pair: tuple[int, int], perms: tuple[tuple[int, ...], ...]) -> tuple[int, int]:
    return min(apply_pair(perm, pair) for perm in perms)


def directed_edges(sites: tuple[Point, ...]) -> tuple[tuple[Point, Point], ...]:
    present = set(sites)
    edges: list[tuple[Point, Point]] = []
    for site in sites:
        for shift in SHIFTS:
            neighbor = (site[0] + shift[0], site[1] + shift[1], site[2] + shift[2])
            if neighbor in present:
                edges.append((site, neighbor))
    return tuple(edges)


def shortest_all(
    start: Point,
    adj: dict[Point, list[tuple[Point, int]]],
    costs: tuple[int, ...],
) -> dict[Point, int]:
    dist = {start: 0}
    heap: list[tuple[int, Point]] = [(0, start)]
    while heap:
        current, node = heapq.heappop(heap)
        if current != dist[node]:
            continue
        for neighbor, orbit in adj[node]:
            trial = current + costs[orbit]
            prior = dist.get(neighbor)
            if prior is None or trial < prior:
                dist[neighbor] = trial
                heapq.heappush(heap, (trial, neighbor))
    return dist


def reverses_b3(t_axis: int, t_diag: int) -> bool:
    return 3 * t_axis * t_axis > 9 * t_diag * t_diag


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


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    source = Path(__file__).read_text(encoding="utf-8")

    print("external_scientific_inputs: none; B_4(0), G+, and the named weight rule are theorem hypotheses")
    print("package_local_integrity_reads: runner source, proposed source note, and live axiom memo")
    print("measure_boundary: exact integer path costs on the radius-4 nearest-neighbor ball")
    print("negative_scope: the named rule is displayed, not written into Admissibility")

    rotations = proper_cubic_rotations()
    perms = tuple(bit_permutation(matrix) for matrix in rotations)
    sites3 = ball(3)
    sites4 = ball(4)
    edges3 = directed_edges(sites3)
    edges4 = directed_edges(sites4)
    reps3 = tuple(
        sorted(
            {
                orbit_rep((occupancy(src), occupancy(dst)), perms)
                for src, dst in edges3
            }
        )
    )
    reps4 = tuple(
        sorted(
            {
                orbit_rep((occupancy(src), occupancy(dst)), perms)
                for src, dst in edges4
            }
        )
    )
    extra4 = tuple(rep for rep in reps4 if rep not in set(reps3))
    weights3 = tuple((weight(rep[0]), weight(rep[1])) for rep in reps3)
    extra_weights = tuple((weight(rep[0]), weight(rep[1])) for rep in extra4)
    named8 = tuple(rho(weight_v, weight_w) for weight_v, weight_w in weights3)
    named33 = rho(3, 3)

    rep_index = {rep: index for index, rep in enumerate(reps3)}
    adj8: dict[Point, list[tuple[Point, int]]] = defaultdict(list)
    adj9: dict[Point, list[tuple[Point, int]]] = defaultdict(list)
    n_new = 0
    for src, dst in edges4:
        rep = orbit_rep((occupancy(src), occupancy(dst)), perms)
        if rep in rep_index:
            adj8[src].append((dst, rep_index[rep]))
            adj9[src].append((dst, rep_index[rep]))
        else:
            n_new += 1
            adj9[src].append((dst, 8))

    omit = shortest_all(ORIGIN, adj8, named8)
    with_rho = shortest_all(ORIGIN, adj9, named8 + (named33,))
    ge3_same = all(
        shortest_all(ORIGIN, adj9, named8 + (cost,)) == omit for cost in (3, 4, 5, 6, 7)
    )
    cheap_differs = all(
        shortest_all(ORIGIN, adj9, named8 + (cost,)) != omit for cost in (1, 2)
    )
    t_axis4 = omit[AXIS4]
    t_axis3 = omit[AXIS3]
    t_diag3 = omit[DIAG3]

    print(f"orbit_weights_b3: {weights3}")
    print(f"named8: {named8}")
    print(f"rho(3,3): {named33}")
    print(f"extra_b4_orbit_weights: {extra_weights}")
    print(f"n_b4_sites: {len(sites4)}")
    print(f"n_new_orbit_edges: {n_new}")
    print(f"t(4,0,0): {t_axis4}")
    print(f"t(3,0,0): {t_axis3}")
    print(f"t(1,1,1): {t_diag3}")
    print(f"diamond_reverses: {reverses_b3(t_axis3, t_diag3)}")

    checks.check("gplus-order", "proper cubic rotations number 24", len(rotations) == 24)
    checks.check("ball-size", "B_4(0) has 129 sites", len(sites4) == 129)
    checks.check(
        "thm1-eight-orbits",
        "B_3 endpoint occupancy pairs form the eight inward-weight orbits",
        len(reps3) == 8 and weights3 == EXPECTED_WEIGHTS,
    )
    checks.check(
        "thm1-reproduces-minkbest",
        "rho reproduces the minkbest 8-tuple (3,1,3,1,1,3,1,1)",
        named8 == MINKBEST,
    )
    checks.check(
        "thm1-rho-33",
        "rho names the new B_4 orbit by rho(3,3)=3",
        named33 == 3 and extra_weights == ((3, 3),),
    )
    checks.check(
        "thm1-new-orbit-edges",
        "B_4 realizes the (3,3) orbit on 48 directed edges and nine orbits total",
        n_new == 48 and len(reps4) == 9,
    )
    checks.check(
        "thm1-note-tuple",
        "the note exhibits the named rule, the 8-tuple, and rho(3,3)=3",
        "cost 3 if" in note
        and "(3, 1, 3, 1, 1, 3, 1, 1)" in note
        and "rho(3,3) = 3" in note,
    )
    checks.check(
        "thm2-t400",
        "the named filling realizes t(4,0,0)=12 on B_4(0)",
        t_axis4 == 12,
    )
    checks.check(
        "thm2-diamond",
        "diamond still reverses on (3,0,0) versus (1,1,1): times 9 and 5",
        t_axis3 == 9
        and t_diag3 == 5
        and reverses_b3(9, 5)
        and 3 * 81 > 9 * 25,
    )
    checks.check(
        "thm2-omit-equals-rho",
        "filling (3,3) by rho(3,3)=3 matches omitting that orbit",
        with_rho == omit and len(omit) == 129,
    )
    checks.check(
        "thm2-any-cost-ge-3",
        "any (3,3) cost at least 3 yields the same B_4 arrival table",
        ge3_same,
    )
    checks.check(
        "thm2-ge3-sharp",
        "costs 1 and 2 on (3,3) change the arrival table, so the bound 3 is sharp",
        cheap_differs,
    )
    checks.check(
        "thm2-note-times",
        "the note reports t(4,0,0)=12 and the still-reversing diamond pair",
        "t(4,0,0) = 12" in note
        and "t(3,0,0) = 9" in note
        and "t(1,1,1) = 5" in note
        and "still reverses" in note,
    )
    checks.check(
        "thm2-note-same-table",
        "the note states omit and any cost >=3 share the arrival table",
        "same arrival table" in note and "any cost" in note and "at least `3`" in note,
    )
    checks.check(
        "thm2-not-leftover",
        "the named rule is a member clause, not a per-radius leftover",
        "member clause" in note and "not a per-radius leftover" in note,
    )
    checks.check(
        "thm3-displayed-not-adopted",
        "the note reports the named rule as displayed, not adopted",
        "Displayed, not adopted" in note
        and "not written into Admissibility" in note
        and "one fixed nearest-neighbor admissibility rule" in axiom,
    )
    checks.check(
        "thm3-no-uniqueness",
        "uniqueness of rho is not claimed",
        "Uniqueness of" in note and "is not claimed" in note,
    )
    checks.check(
        "thm3-no-l1-law",
        "the note does not attach an ell^1 path-length law",
        "no path-length law" in note and "not attach" in note,
    )
    checks.check(
        "claim-scope",
        "claim_scope reports the named equal-weight rule versus the 8-tuple",
        "The named rule cost=3 iff equal inward weight or seed-exit"
        in note
        and "reproduces the minkbest 8-tuple" in note
        and "names the B_4 (3,3) orbit" in note
        and "Displayed, not adopted" in note,
    )
    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/NAMED_EQUAL_WEIGHT_HOPCOST_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and "AUDIT_INPUT_PATHS = (" in source
        and '"docs/NAMED_EQUAL_WEIGHT_HOPCOST_BOUNDED_THEOREM_NOTE_2026-08-15.md"'
        in source,
    )
    checks.check(
        "forbidden-strings",
        "note, runner, and axiom avoid the dispatch-forbidden phrases",
        all(token not in note and token not in source for token in forbidden_tokens()),
    )
    checks.check(
        "no-axiom-cost",
        "the live axiom memo does not host a two-end occupancy hop cost",
        "two-end occupancy" not in axiom and "c(σ_v, σ_w)" not in axiom,
    )
    checks.check(
        "claim-type-and-gate",
        "bounded theorem type and a passing N1-N8 gate are source-visible",
        "**Type:** bounded_theorem" in note
        and all(f"### N{index}" in note for index in range(1, 9))
        and "No-Go Discipline disposition: **PASS**" in note
        and note.count("**ATTEMPTED**") == 6,
    )

    print(
        "per_element: checked exactly — each directed B_4(0) edge is an 8-orbit hop or the named (3,3) orbit"
    )
    print(
        "per_site: checked exactly — occupancy is the 6-bit inward front at that site"
    )
    print(
        "per_mode: checked exactly — the named weight rule on the eight orbits and the new (3,3) orbit"
    )
    print(
        "per_block: checked exactly — t(4,0,0) and diamond order on (3,0,0) versus (1,1,1)"
    )
    print(
        "lattice_wide: checked and not executed — no Admissibility cost and no path-length law are adopted"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
