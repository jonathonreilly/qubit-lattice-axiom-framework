#!/usr/bin/env python3
"""Exact checks for cube-covariant 6-NN hop-cost versus displayed light tests."""

from __future__ import annotations

from heapq import heappop, heappush
from itertools import permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]

AUDIT_INPUT_PATHS = (
    "docs/CUBE_COVARIANT_NN_HOP_COST_MINKOWSKI_MISMATCH_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / AUDIT_INPUT_PATHS[0]
AXIOM_PATH = ROOT / AUDIT_INPUT_PATHS[1]

Point = tuple[int, int, int]
Matrix = tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]
HopCost = dict[Point, int]

AXES: tuple[Point, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
ORIGIN: Point = (0, 0, 0)
AXIS_WITNESS: Point = (1, 0, 0)
FACE_WITNESS: Point = (1, 1, 0)
RADIUS = 4


def normalize(text: str) -> str:
    return " ".join(text.split())


def matrix_det(matrix: Matrix) -> int:
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def apply_linear(matrix: Matrix, vector: Point) -> Point:
    return tuple(sum(matrix[i][j] * vector[j] for j in range(3)) for i in range(3))  # type: ignore[return-value]


def proper_cube_group() -> tuple[Matrix, ...]:
    """Signed permutation matrices with determinant +1."""
    group: list[Matrix] = []
    for perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            rows = []
            for i in range(3):
                row = [0, 0, 0]
                row[perm[i]] = signs[i]
                rows.append(tuple(row))
            matrix = (rows[0], rows[1], rows[2])
            if matrix_det(matrix) == 1:
                group.append(matrix)
    return tuple(group)


def hop_orbit(seed: Point, group: tuple[Matrix, ...]) -> frozenset[Point]:
    return frozenset(apply_linear(matrix, seed) for matrix in group)


def l1_norm(vector: Point) -> int:
    return abs(vector[0]) + abs(vector[1]) + abs(vector[2])


def l2_sq(vector: Point) -> int:
    return vector[0] * vector[0] + vector[1] * vector[1] + vector[2] * vector[2]


def radius_ball(radius: int) -> tuple[Point, ...]:
    points = []
    for x, y, z in product(range(-radius, radius + 1), repeat=3):
        point = (x, y, z)
        if l1_norm(point) <= radius:
            points.append(point)
    return tuple(points)


def constant_hop_cost(weight: int) -> HopCost:
    if weight < 1:
        raise ValueError("hop costs must be positive integers")
    return {axis: weight for axis in AXES}


def is_cube_covariant(weights: HopCost, group: tuple[Matrix, ...]) -> bool:
    if set(weights) != set(AXES):
        return False
    if any(value < 1 for value in weights.values()):
        return False
    return all(
        weights[apply_linear(matrix, axis)] == weights[axis]
        for matrix in group
        for axis in AXES
    )


def first_arrival(target: Point, weights: HopCost) -> int:
    """Shortest-path cost from the origin on the six-direction graph."""
    if target == ORIGIN:
        return 0
    bound = max(weights.values()) * (l1_norm(target) + 2)
    best = {ORIGIN: 0}
    queue: list[tuple[int, Point]] = [(0, ORIGIN)]
    while queue:
        cost, site = heappop(queue)
        if cost != best[site]:
            continue
        if site == target:
            return cost
        for hop, hop_weight in weights.items():
            neighbor = (site[0] + hop[0], site[1] + hop[1], site[2] + hop[2])
            next_cost = cost + hop_weight
            if next_cost > bound:
                continue
            if next_cost < best.get(neighbor, bound + 1):
                best[neighbor] = next_cost
                heappush(queue, (next_cost, neighbor))
    raise RuntimeError(f"no path found to {target}")


def arrival_ratio(vector: Point, weights: HopCost) -> int:
    """Return t(v)^2 / |v|_2^2 when that quotient is an integer."""
    if vector == ORIGIN:
        raise ValueError("ratio is undefined at the origin")
    arrival = first_arrival(vector, weights)
    spatial = l2_sq(vector)
    if arrival * arrival % spatial != 0:
        raise ValueError("displayed ratio is not an integer on this site")
    return (arrival * arrival) // spatial


def is_discrete_null(vector: Point, weights: HopCost) -> bool:
    return first_arrival(vector, weights) ** 2 == l2_sq(vector)


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
    print("external_scientific_inputs: current Lattice and Admissibility wording are source-bound; Minkowski light is a displayed comparator")
    print("construction: G+ orbit of the six NN directions, cube-covariant hop-costs, shortest-path first arrival")
    print("negative_scope: displayed t proportional to ell^1 fails isotropic c and the discrete ell^2 null cone; no axiom edit")

    checks.check(
        "audit-inputs",
        "declared inputs are exactly the source note and the axiom memo",
        AUDIT_INPUT_PATHS
        == (
            "docs/CUBE_COVARIANT_NN_HOP_COST_MINKOWSKI_MISMATCH_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
        "source-no-minkowski-in-axioms",
        "the axiom memo does not name Minkowski, a boost, or a Wick map",
        all(token not in axiom for token in ("Minkowski", "boost", "Wick")),
    )

    group = proper_cube_group()
    orbit = hop_orbit(AXIS_WITNESS, group)
    checks.check(
        "group-order",
        "the proper cube group has 24 matrices of determinant +1",
        len(group) == 24 and len(set(group)) == 24 and all(matrix_det(matrix) == 1 for matrix in group),
        residual=len(group),
    )
    checks.check(
        "single-orbit",
        "the six axis directions are one G+ orbit of e_1",
        orbit == frozenset(AXES) and len(orbit) == 6,
        residual=sorted(orbit),
    )

    weights_one = constant_hop_cost(1)
    weights_two = constant_hop_cost(2)
    weights_three = constant_hop_cost(3)
    unequal = dict(weights_one)
    unequal[(0, 1, 0)] = 2
    checks.check(
        "covariant-constant",
        "every constant hop-cost is cube-covariant and the unequal mutation is not",
        is_cube_covariant(weights_one, group)
        and is_cube_covariant(weights_two, group)
        and is_cube_covariant(weights_three, group)
        and not is_cube_covariant(unequal, group),
    )

    ball = radius_ball(RADIUS)
    nonzero = tuple(point for point in ball if point != ORIGIN)
    arrival_ok = all(
        first_arrival(point, weights_one) == l1_norm(point)
        and first_arrival(point, weights_two) == 2 * l1_norm(point)
        and first_arrival(point, weights_three) == 3 * l1_norm(point)
        for point in nonzero
    )
    checks.check(
        "first-arrival-form",
        "shortest-path arrival equals w_0 |v|_1 on the radius-4 ball",
        arrival_ok and first_arrival(ORIGIN, weights_one) == 0,
    )

    ratio_pairs = []
    for weight in (1, 2, 3, 5):
        costs = constant_hop_cost(weight)
        axis_ratio = arrival_ratio(AXIS_WITNESS, costs)
        face_ratio = arrival_ratio(FACE_WITNESS, costs)
        ratio_pairs.append((weight, axis_ratio, face_ratio))
        if axis_ratio != weight * weight or face_ratio != 2 * weight * weight:
            break
    checks.check(
        "ratio-witnesses",
        "(1,0,0) gives w_0^2 and (1,1,0) gives 2 w_0^2 for every tested w_0",
        all(axis == weight * weight and face == 2 * weight * weight for weight, axis, face in ratio_pairs)
        and len(ratio_pairs) == 4,
        residual=ratio_pairs,
    )
    checks.check(
        "ratio-not-constant",
        "t^2 / |v|_2^2 is not constant on the nonzero radius-4 ball",
        arrival_ratio(AXIS_WITNESS, weights_one) != arrival_ratio(FACE_WITNESS, weights_one)
        and arrival_ratio(AXIS_WITNESS, weights_two) != arrival_ratio(FACE_WITNESS, weights_two),
    )

    null_one = tuple(point for point in nonzero if is_discrete_null(point, weights_one))
    null_two = tuple(point for point in nonzero if is_discrete_null(point, weights_two))
    checks.check(
        "discrete-null-subset",
        "discrete null t^2 = |v|_2^2 is a proper subset; (1,1,0) is the witness",
        FACE_WITNESS in nonzero
        and FACE_WITNESS not in null_one
        and not is_discrete_null(FACE_WITNESS, weights_two)
        and len(null_one) < len(nonzero)
        and len(null_two) < len(nonzero)
        and AXIS_WITNESS in null_one,
        residual=(len(nonzero), len(null_one), len(null_two)),
    )
    print(f"N_ball={len(nonzero)} N_null_w1={len(null_one)} N_null_w2={len(null_two)}")

    no_match = all(
        arrival_ratio(AXIS_WITNESS, constant_hop_cost(weight))
        != arrival_ratio(FACE_WITNESS, constant_hop_cost(weight))
        and not is_discrete_null(FACE_WITNESS, constant_hop_cost(weight))
        for weight in (1, 2, 3, 5)
    )
    checks.check(
        "no-minkowski-match",
        "no cube-covariant 6-NN unit-orbit member matches both displayed light tests",
        no_match and is_cube_covariant(weights_one, group),
    )

    rot_z: Matrix = ((0, -1, 0), (1, 0, 0), (0, 0, 1))
    rot_y: Matrix = ((0, 0, 1), (0, 1, 0), (-1, 0, 0))
    checks.check(
        "identity-rotations",
        "the named 90-degree generators sit in G+ and move e_1 onto the other axes",
        rot_z in group
        and rot_y in group
        and apply_linear(rot_z, AXIS_WITNESS) == (0, 1, 0)
        and apply_linear(rot_y, AXIS_WITNESS) == (0, 0, -1),
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
        "t(v) = w_0 |v|_1",
        "(1,0,0)` gives `w_0^2",
        "(1,1,0)` gives",
        "2 w_0^2",
        "Displayed, not adopted",
        "Do not adopt a Wick map",
        "Do not write Minkowski into Admissibility",
        "authors no audit verdict",
        "FAIL / DO NOT SHIP",
        "No occupancy is grown on a new patch",
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

    print("per_element: six axis directions, G+ orbit, and the two named witnesses are executed")
    print("per_site: first arrival is shortest-path cost from the origin on Z^3")
    print("per_mode: checked and not executed — no spectral claim occurs")
    print("per_block: the radius-4 integer ball is the comparison domain")
    print("lattice_wide: checked and not executed — no occupancy step and no axiom edit")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
