#!/usr/bin/env python3
"""Isochrones of the named support-drop hop-cost on B_6(0).

One origin Dijkstra under ν as in noshrt. The note reports t on every
G+ site-type, the |v|_2/t table, and whether the t=const shells are
single Euclidean radii. Displayed, not adopted. No axiom edit, cache
write, or L1 attachment.
"""

from __future__ import annotations

import ast
import heapq
from collections import defaultdict
from decimal import Decimal, getcontext
from itertools import permutations, product
from pathlib import Path


getcontext().prec = 80

AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/SUPPORT_DROP_ISOCHRONE_B6_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/SUPPORT_DROP_ISOCHRONE_B6_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
CLAIM_SCOPE = (
    "On B_6(0), the isochrones of the named support-drop hop-cost "
    "are reported. Displayed, not adopted."
)

Point = tuple[int, int, int]
NEIGH: tuple[Point, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
ORIGIN: Point = (0, 0, 0)
AXIS: Point = (4, 0, 0)
DIAG: Point = (2, 2, 2)
SITE_TYPES: tuple[Point, ...] = (
    (1, 0, 0),
    (1, 1, 0),
    (2, 0, 0),
    (1, 1, 1),
    (2, 1, 0),
    (3, 0, 0),
    (2, 1, 1),
    (2, 2, 0),
    (3, 1, 0),
    (4, 0, 0),
    (2, 2, 1),
    (3, 1, 1),
    (3, 2, 0),
    (4, 1, 0),
    (5, 0, 0),
    (2, 2, 2),
    (3, 2, 1),
    (3, 3, 0),
    (4, 1, 1),
    (4, 2, 0),
    (5, 1, 0),
    (6, 0, 0),
)
EXPECTED_TYPE_TIMES = {
    (1, 0, 0): 3,
    (1, 1, 0): 4,
    (2, 0, 0): 6,
    (1, 1, 1): 5,
    (2, 1, 0): 5,
    (3, 0, 0): 9,
    (2, 1, 1): 6,
    (2, 2, 0): 6,
    (3, 1, 0): 6,
    (4, 0, 0): 10,
    (2, 2, 1): 7,
    (3, 1, 1): 7,
    (3, 2, 0): 7,
    (4, 1, 0): 7,
    (5, 0, 0): 11,
    (2, 2, 2): 8,
    (3, 2, 1): 8,
    (3, 3, 0): 8,
    (4, 1, 1): 8,
    (4, 2, 0): 8,
    (5, 1, 0): 8,
    (6, 0, 0): 14,
}
EXPECTED_ORBIT_SIZES = {
    (1, 0, 0): 6,
    (1, 1, 0): 12,
    (2, 0, 0): 6,
    (1, 1, 1): 8,
    (2, 1, 0): 24,
    (3, 0, 0): 6,
    (2, 1, 1): 24,
    (2, 2, 0): 12,
    (3, 1, 0): 24,
    (4, 0, 0): 6,
    (2, 2, 1): 24,
    (3, 1, 1): 24,
    (3, 2, 0): 24,
    (4, 1, 0): 24,
    (5, 0, 0): 6,
    (2, 2, 2): 8,
    (3, 2, 1): 48,
    (3, 3, 0): 12,
    (4, 1, 1): 24,
    (4, 2, 0): 24,
    (5, 1, 0): 24,
    (6, 0, 0): 6,
}
VAR_NU_REPORTED = "0.00590563902870"
VAR_L1_REPORTED = "0.01350203761919"
DIJKSTRA_CALLS = 0


def forbidden_tokens() -> tuple[str, ...]:
    return (
        "G" + "_N",
        "1/" + "r",
        "1/" + "r^2",
        "Lattice-" + "named",
        "not a " + "TOE",
    )


def l1(point: Point) -> int:
    return abs(point[0]) + abs(point[1]) + abs(point[2])


def euclid2(point: Point) -> int:
    return point[0] * point[0] + point[1] * point[1] + point[2] * point[2]


def support_size(point: Point) -> int:
    return int(point[0] != 0) + int(point[1] != 0) + int(point[2] != 0)


def site_type(point: Point) -> Point:
    return tuple(sorted((abs(coord) for coord in point), reverse=True))  # type: ignore[return-value]


def ball(radius: int) -> tuple[Point, ...]:
    sites: list[Point] = []
    span = range(-radius, radius + 1)
    for coords in product(span, repeat=3):
        if l1(coords) <= radius:
            sites.append(coords)
    return tuple(sites)


def nu_cost(src: Point, dst: Point) -> int:
    sigma_v = support_size(src)
    sigma_w = support_size(dst)
    if sigma_v == 0 or (sigma_v == 1 and sigma_w == 1) or sigma_w < sigma_v:
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


def dijkstra_nu(sites: tuple[Point, ...]) -> dict[Point, int]:
    global DIJKSTRA_CALLS
    DIJKSTRA_CALLS += 1
    present = set(sites)
    dist: dict[Point, int] = {ORIGIN: 0}
    heap: list[tuple[int, Point]] = [(0, ORIGIN)]
    seen: set[Point] = set()
    while heap:
        current, node = heapq.heappop(heap)
        if node in seen:
            continue
        seen.add(node)
        for shift in NEIGH:
            neighbor = (node[0] + shift[0], node[1] + shift[1], node[2] + shift[2])
            if neighbor not in present:
                continue
            trial = current + nu_cost(node, neighbor)
            prior = dist.get(neighbor)
            if prior is None or trial < prior:
                dist[neighbor] = trial
                heapq.heappush(heap, (trial, neighbor))
    return dist


def ratio_list(dist: dict[Point, int], sites: tuple[Point, ...]) -> list[Decimal]:
    values: list[Decimal] = []
    for point in sites:
        if point == ORIGIN:
            continue
        values.append(Decimal(euclid2(point)).sqrt() / Decimal(dist[point]))
    return values


def population_variance(values: list[Decimal]) -> Decimal:
    count = Decimal(len(values))
    mean = sum(values) / count
    return sum((item - mean) ** 2 for item in values) / count


def rounded(value: Decimal, places: int) -> str:
    quantize = Decimal(10) ** -places
    return format(value.quantize(quantize), "f")


def literal_audit_paths(source: str) -> tuple[str, ...] | None:
    module = ast.parse(source)
    for node in module.body:
        if not isinstance(node, ast.Assign):
            continue
        if not any(isinstance(target, ast.Name) and target.id == "AUDIT_INPUT_PATHS" for target in node.targets):
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
    print("external_scientific_inputs: none; B_6(0), G+, and the named support-drop hop-cost are theorem hypotheses")
    print("package_local_integrity_reads: runner source, proposed source note, and live axiom memo")
    print("measure_boundary: exact integer path costs and |v|_2/t on the radius-6 ball")
    print("negative_scope: displayed support-drop isochrones are not written into Admissibility")

    rotations = proper_cubic_rotations()
    sites = ball(6)
    nonzero = tuple(site for site in sites if site != ORIGIN)
    times = dijkstra_nu(sites)

    type_times: dict[Point, set[int]] = defaultdict(set)
    type_counts: dict[Point, int] = defaultdict(int)
    type_radii: dict[Point, set[int]] = defaultdict(set)
    shells: dict[int, set[Point]] = defaultdict(set)
    shell_radii: dict[int, set[int]] = defaultdict(set)
    for site in nonzero:
        kind = site_type(site)
        type_times[kind].add(times[site])
        type_counts[kind] += 1
        type_radii[kind].add(euclid2(site))
        shells[times[site]].add(kind)
        shell_radii[times[site]].add(euclid2(site))

    type_time_map = {kind: next(iter(vals)) for kind, vals in type_times.items()}
    type_ratios = {
        kind: Decimal(euclid2(kind)).sqrt() / Decimal(type_time_map[kind])
        for kind in SITE_TYPES
    }
    var_nu = population_variance(ratio_list(times, sites))
    var_l1 = population_variance(
        [Decimal(euclid2(site)).sqrt() / Decimal(l1(site)) for site in nonzero]
    )
    single_radius_shells = {
        level: len(radii) == 1 for level, radii in shell_radii.items()
    }
    n_single = sum(1 for flag in single_radius_shells.values() if flag)
    n_mixed = len(single_radius_shells) - n_single

    print(f"n_sites {len(sites)}")
    print(f"n_nonzero {len(nonzero)}")
    print(f"n_types {len(SITE_TYPES)}")
    print(f"t(4,0,0) {times[AXIS]}")
    print(f"t(2,2,2) {times[DIAG]}")
    print(
        "site_type_times: "
        + ", ".join(
            f"{kind}->{type_time_map[kind]}(n={type_counts[kind]}, |v|_2/t={rounded(type_ratios[kind], 12)})"
            for kind in SITE_TYPES
        )
    )
    print(
        "shells: "
        + ", ".join(
            f"t={level}:types={sorted(shells[level])}:r2={sorted(shell_radii[level])}:single={single_radius_shells[level]}"
            for level in sorted(shells)
        )
    )
    print(f"n_t_values {len(shells)}")
    print(f"n_single_radius_shells {n_single}")
    print(f"n_mixed_radius_shells {n_mixed}")
    print(f"var_nu {rounded(var_nu, 14)}")
    print(f"var_l1 {rounded(var_l1, 14)}")
    print(f"dijkstra_calls {DIJKSTRA_CALLS}")

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
        "note claim_scope matches the displayed isochrone statement",
        CLAIM_SCOPE in note.replace("\n", " "),
    )
    checks.check(
        "gplus-order",
        "proper cubic rotations number 24",
        len(rotations) == 24,
    )
    checks.check(
        "one-dijkstra",
        "exactly one Dijkstra ran",
        DIJKSTRA_CALLS == 1,
    )
    checks.check(
        "ball-b6",
        "B_6(0) has 377 sites and 376 nonzero sites",
        len(sites) == 377 and len(nonzero) == 376 and all(l1(site) <= 6 for site in sites),
    )
    checks.check(
        "reachable",
        "every site of B_6(0) is reached",
        len(times) == 377,
    )
    checks.check(
        "thm1-type-count",
        "B_6(0)\\{0} has 22 G+ site-types",
        len(type_times) == 22
        and set(type_times) == set(SITE_TYPES)
        and sum(type_counts[kind] for kind in SITE_TYPES) == 376,
    )
    checks.check(
        "thm1-orbit-sizes",
        "each G+ site-type has the expected orbit size",
        all(type_counts[kind] == EXPECTED_ORBIT_SIZES[kind] for kind in SITE_TYPES),
    )
    checks.check(
        "thm1-type-constant",
        "arrival time is constant on each G+ site-type",
        all(len(type_times[kind]) == 1 for kind in SITE_TYPES)
        and all(len(type_radii[kind]) == 1 for kind in SITE_TYPES),
    )
    checks.check(
        "thm1-axis-diag-times",
        "t(4,0,0)=10 and t(2,2,2)=8",
        times[AXIS] == 10 and times[DIAG] == 8,
    )
    checks.check(
        "thm1-all-type-times",
        "each of the 22 G+ site-types has the reported arrival time",
        type_time_map == EXPECTED_TYPE_TIMES,
    )
    checks.check(
        "thm1-note-times",
        "the note records t(4,0,0)=10, t(2,2,2)=8, and every type time",
        "t(4,0,0) = 10" in note
        and "t(2,2,2) = 8" in note
        and all(f"`{kind[0]},{kind[1]},{kind[2]}`" in note.replace(" ", "") or f"({kind[0]},{kind[1]},{kind[2]})" in note.replace(" ", "") for kind in SITE_TYPES)
        and all(
            f"`{EXPECTED_TYPE_TIMES[kind]}`" in note
            or f"| `{EXPECTED_TYPE_TIMES[kind]}` |" in note
            for kind in SITE_TYPES
        ),
    )
    checks.check(
        "thm1-note-ratios",
        "the note reports |v|_2/t for each of the 22 site-types",
        "1/3" in note
        and "√2 / 4" in note
        and "√3 / 5" in note
        and "√5 / 5" in note
        and "2/5" in note
        and "√3 / 4" in note
        and "3/7" in note,
    )
    checks.check(
        "thm1-gplus-action",
        "G+ acts and preserves both type and arrival time",
        all(
            site_type(apply_matrix(matrix, kind)) == kind
            and times[apply_matrix(matrix, kind)] == times[kind]
            for matrix in rotations
            for kind in SITE_TYPES
        ),
    )
    checks.check(
        "thm1-shells-not-all-single",
        "t=const shells are not all single Euclidean radii",
        n_single == 6
        and n_mixed == 4
        and len(shells) == 10
        and single_radius_shells[3]
        and single_radius_shells[4]
        and not single_radius_shells[5]
        and not single_radius_shells[6]
        and not single_radius_shells[7]
        and not single_radius_shells[8]
        and single_radius_shells[9]
        and single_radius_shells[10]
        and single_radius_shells[11]
        and single_radius_shells[14],
    )
    checks.check(
        "thm1-note-shells",
        "the note reports the mixed t=5,6,7,8 shells and the six single-radius shells",
        "not all single Euclidean radii" in note
        and "t = 5" in note
        and "t = 8" in note
        and "six single-radius" in note
        and "four mixed" in note,
    )
    checks.check(
        "thm2-var-nu",
        "population variance under ν equals the noshrt figure",
        rounded(var_nu, 14) == VAR_NU_REPORTED,
    )
    checks.check(
        "thm2-var-l1",
        "population variance under ℓ¹ matches the noshrt comparator",
        rounded(var_l1, 14) == VAR_L1_REPORTED,
    )
    checks.check(
        "thm2-var-below",
        "var(|v|_2/t) is strictly below ℓ¹",
        var_nu < var_l1,
    )
    checks.check(
        "thm2-vars-in-note",
        "the note records both variances and the comparison",
        VAR_NU_REPORTED in note
        and VAR_L1_REPORTED in note
        and "strictly below" in note
        and "var_ν < var_ℓ¹" in note,
    )
    checks.check(
        "thm3-displayed-not-adopted",
        "the rule is displayed, not adopted",
        "Displayed, not adopted" in note
        and "not written into Admissibility" in note,
    )
    checks.check(
        "thm3-not-attach-l1",
        "the displayed rule is not attached to L1",
        "not attached to L1" in note and "Do not attach L1" not in axiom,
    )
    checks.check(
        "no-axiom-edit",
        "note records hypothetical axiom status no edit",
        'hypothetical_axiom_status: "no edit"' in note,
    )
    checks.check(
        "not-two-point-leftover",
        "the isochrone report is not leftover of the two-point 10 and 8 times",
        "not a leftover" in note
        and "two-point" in note
        and "isochrone" in note.lower(),
    )
    forbidden = forbidden_tokens()
    forbidden_hits = [
        token
        for token in forbidden
        if token in note or token in source
    ]
    checks.check(
        "forbidden-absent",
        "forbidden phrases are absent from the source note and runner",
        forbidden_hits == [],
    )
    checks.check(
        "axiom-untouched",
        "the axiom memo is an input only and still names the four axioms",
        "### Admissibility / Local Constraint" in axiom
        and "ν(v→w)" not in axiom
        and "support-drop hop-cost" not in axiom,
    )
    checks.check(
        "claim-type-and-gate",
        "bounded theorem type and a passing N1-N8 gate are source-visible",
        "**Type:** bounded_theorem" in note
        and all(f"### N{index}" in note for index in range(1, 9))
        and "No-Go Discipline disposition: **PASS**" in note
        and note.count("**ATTEMPTED**") >= 5,
    )
    checks.check(
        "scored-ball-only",
        "the note scores the comparison on B_6(0) only",
        "on `B_6(0)` only" in note or "On B_6(0)" in note,
    )

    print("per_element: checked exactly — each directed B_6(0) edge carries one support-drop hop cost")
    print("per_site: checked exactly — t(v) and |v|_2/t(v) on each of the 376 nonzero sites")
    print("per_mode: checked exactly — 22 G+ site-types and the 10 arrival shells")
    print("per_block: checked exactly — population variance of |v|_2/t on B_6(0)\\{0}")
    print("lattice_wide: checked and not executed — no Admissibility cost and no L1 attachment are adopted")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
