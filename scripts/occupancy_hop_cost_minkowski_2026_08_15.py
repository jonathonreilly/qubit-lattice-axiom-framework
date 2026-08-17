#!/usr/bin/env python3
"""Exact checks for G+-equivariant occupancy hop-costs on B_3(0)."""

from __future__ import annotations

from itertools import permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]

AUDIT_INPUT_PATHS = (
    "docs/OCCUPANCY_HOP_COST_MINKOWSKI_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / AUDIT_INPUT_PATHS[0]
AXIOM_PATH = ROOT / AUDIT_INPUT_PATHS[1]

Point = tuple[int, int, int]
Matrix = tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]

AXES: tuple[Point, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
AXIS_INDEX: dict[Point, int] = {axis: index for index, axis in enumerate(AXES)}
ORIGIN: Point = (0, 0, 0)
AXIS_TIP: Point = (3, 0, 0)
BODY_TIP: Point = (1, 1, 1)
RADIUS = 3


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


def add(left: Point, right: Point) -> Point:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


def l1_norm(vector: Point) -> int:
    return abs(vector[0]) + abs(vector[1]) + abs(vector[2])


def l2_sq(vector: Point) -> int:
    return vector[0] * vector[0] + vector[1] * vector[1] + vector[2] * vector[2]


def radius_ball(radius: int) -> tuple[Point, ...]:
    return tuple(
        (x, y, z)
        for x, y, z in product(range(-radius, radius + 1), repeat=3)
        if l1_norm((x, y, z)) <= radius
    )


def inverse_matrix(matrix: Matrix) -> Matrix:
    return tuple(tuple(matrix[j][i] for j in range(3)) for i in range(3))  # type: ignore[return-value]


def act_occupancy(matrix: Matrix, bits: int) -> int:
    inverse = inverse_matrix(matrix)
    out = 0
    for index, axis in enumerate(AXES):
        preimage = apply_linear(inverse, axis)
        out |= ((bits >> AXIS_INDEX[preimage]) & 1) << index
    return out


def occupancy_orbits(group: tuple[Matrix, ...]) -> tuple[tuple[int, ...], ...]:
    seen: set[int] = set()
    orbits: list[tuple[int, ...]] = []
    for bits in range(64):
        if bits in seen:
            continue
        orbit = {act_occupancy(matrix, bits) for matrix in group}
        seen |= orbit
        orbits.append(tuple(sorted(orbit)))
    return tuple(orbits)


def orbit_id_table(orbits: tuple[tuple[int, ...], ...]) -> tuple[int, ...]:
    table = [0] * 64
    for orbit_id, orbit in enumerate(orbits):
        for bits in orbit:
            table[bits] = orbit_id
    return tuple(table)


def occupancy_bits(site: Point, occupied: set[Point]) -> int:
    bits = 0
    for index, axis in enumerate(AXES):
        if add(site, axis) in occupied:
            bits |= 1 << index
    return bits


def front_arrival(
    ball: tuple[Point, ...],
    cost_of: object,
) -> dict[Point, int]:
    """One-seed front on the induced B_3 graph; layer-synchronous occupancy."""
    ball_set = set(ball)
    arrival: dict[Point, int] = {ORIGIN: 0}
    settled: set[Point] = set()
    while True:
        pending = [site for site in ball if site not in settled and site in arrival]
        if not pending:
            break
        time = min(arrival[site] for site in pending)
        layer = [site for site in pending if arrival[site] == time]
        settled.update(layer)
        for site in layer:
            for hop in AXES:
                neighbor = add(site, hop)
                if neighbor not in ball_set or neighbor in settled:
                    continue
                bits = occupancy_bits(neighbor, settled)
                next_time = time + cost_of(bits, hop)
                if next_time < arrival.get(neighbor, 10**9):
                    arrival[neighbor] = next_time
    return arrival


def weight_cost(table: tuple[int, ...]):
    def cost_of(bits: int, hop: Point) -> int:
        del hop
        return table[bin(bits).count("1")]

    return cost_of


def orbit_cost(orbit_table: tuple[int, ...], ids: tuple[int, ...]):
    def cost_of(bits: int, hop: Point) -> int:
        del hop
        return orbit_table[ids[bits]]

    return cost_of


def arrival_axis_cost(empty_cost: int, occupied_cost: int):
    """Cost depends on whether the far end of the arrival axis is occupied."""

    def cost_of(bits: int, hop: Point) -> int:
        opposite = (bits >> AXIS_INDEX[hop]) & 1
        return occupied_cost if opposite else empty_cost

    return cost_of


def axis_body_times(arrival: dict[Point, int], axes: tuple[Point, ...], bodies: tuple[Point, ...]) -> tuple[int, int]:
    axis_values = {arrival[site] for site in axes}
    body_values = {arrival[site] for site in bodies}
    if len(axis_values) != 1 or len(body_values) != 1:
        raise RuntimeError((axis_values, body_values))
    return next(iter(axis_values)), next(iter(body_values))


def diamond_order(axis_time: int, body_time: int) -> bool:
    """Axis sites arrive no later per Euclidean radius than body sites."""
    return axis_time * axis_time * l2_sq(BODY_TIP) <= body_time * body_time * l2_sq(AXIS_TIP)


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
    print("construction: one-seed front on B_3(0) with G+-equivariant occupancy hop-costs in {1,2}")
    print("negative_scope: occupancy-only hop-costs stay diamond on B_3(0); no axiom edit and no adopted cost")

    checks.check(
        "audit-inputs",
        "declared inputs are exactly the source note and the axiom memo",
        AUDIT_INPUT_PATHS
        == (
            "docs/OCCUPANCY_HOP_COST_MINKOWSKI_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
        "the axiom memo does not name Minkowski, a hop-cost, or a Wick map",
        all(token not in axiom for token in ("Minkowski", "hop-cost", "Wick")),
    )

    group = proper_cube_group()
    ball = radius_ball(RADIUS)
    axes = tuple(site for site in ball if l1_norm(site) == 3 and sorted(abs(coord) for coord in site) == [0, 0, 3])
    bodies = tuple(site for site in ball if l1_norm(site) == 3 and sorted(abs(coord) for coord in site) == [1, 1, 1])
    orbits = occupancy_orbits(group)
    ids = orbit_id_table(orbits)

    checks.check(
        "group-order",
        "the proper cube group has 24 matrices of determinant +1",
        len(group) == 24 and len(set(group)) == 24 and all(matrix_det(matrix) == 1 for matrix in group),
        residual=len(group),
    )
    checks.check(
        "ball-census",
        "B_3(0) has 63 integer sites; the ell^1=3 sphere has 6 axis and 8 body-diagonal sites",
        len(ball) == 63
        and len(axes) == 6
        and len(bodies) == 8
        and AXIS_TIP in axes
        and BODY_TIP in bodies
        and l2_sq(AXIS_TIP) == 9
        and l2_sq(BODY_TIP) == 3,
        residual=(len(ball), len(axes), len(bodies)),
    )
    checks.check(
        "occupancy-orbits",
        "G+ has ten orbits on {0,1}^6, so 1024 equivariant maps to {1,2}",
        len(orbits) == 10
        and sum(len(orbit) for orbit in orbits) == 64
        and all(act_occupancy(matrix, bits) in orbits[ids[bits]] for matrix in group for bits in range(64)),
        residual=len(orbits),
    )

    constant = front_arrival(ball, weight_cost((1, 1, 1, 1, 1, 1, 1)))
    axis_const, body_const = axis_body_times(constant, axes, bodies)
    sphere_ok = all(constant[site] == l1_norm(site) for site in ball)
    checks.check(
        "constant-isochrones",
        "constant c=1 gives first arrival equal to ell^1 on B_3(0)",
        sphere_ok and axis_const == 3 and body_const == 3 and constant[ORIGIN] == 0,
        residual=(axis_const, body_const),
    )
    checks.check(
        "ell1-euclidean-mismatch",
        "at ell^1=3 the 6 axis sites have |v|_2^2=9 and the 8 body sites have |v|_2^2=3",
        axis_const == body_const == 3
        and {l2_sq(site) for site in axes} == {9}
        and {l2_sq(site) for site in bodies} == {3}
        and (axis_const * axis_const) // 9 != (body_const * body_const) // 3,
        residual=((axis_const * axis_const) // 9, (body_const * body_const) // 3),
    )

    weight_pairs = set()
    weight_diamond = True
    for mask in range(128):
        table = tuple(1 + ((mask >> weight) & 1) for weight in range(7))
        arrival = front_arrival(ball, weight_cost(table))
        axis_time, body_time = axis_body_times(arrival, axes, bodies)
        weight_pairs.add((axis_time, body_time))
        weight_diamond = weight_diamond and diamond_order(axis_time, body_time)
    checks.check(
        "weight-family-diamond",
        "every weight-only cost in {1,2} keeps the axis/body Euclidean-radius order",
        weight_diamond and weight_pairs == {(3, 3), (3, 4), (3, 5), (6, 4), (6, 5), (6, 6)},
        residual=sorted(weight_pairs),
    )

    axis_pairs = set()
    axis_diamond = True
    for empty_cost, occupied_cost in product((1, 2), repeat=2):
        arrival = front_arrival(ball, arrival_axis_cost(empty_cost, occupied_cost))
        axis_time, body_time = axis_body_times(arrival, axes, bodies)
        axis_pairs.add((axis_time, body_time))
        axis_diamond = axis_diamond and diamond_order(axis_time, body_time)
    checks.check(
        "arrival-axis-family-diamond",
        "every arrival-axis occupancy cost in {1,2} keeps equal axis and body arrival",
        axis_diamond and axis_pairs == {(3, 3), (6, 6)},
        residual=sorted(axis_pairs),
    )

    first_reversal = None
    orbit_pairs = set()
    for mask in range(1 << len(orbits)):
        table = tuple(1 + ((mask >> orbit_id) & 1) for orbit_id in range(len(orbits)))
        arrival = front_arrival(ball, orbit_cost(table, ids))
        axis_time, body_time = axis_body_times(arrival, axes, bodies)
        orbit_pairs.add((axis_time, body_time))
        if not diamond_order(axis_time, body_time) and first_reversal is None:
            first_reversal = (table, axis_time, body_time)
    checks.check(
        "equivariant-census-diamond",
        "every G+-equivariant c:{0,1}^6->{1,2} keeps the Euclidean-radius diamond order",
        first_reversal is None
        and len(orbits) == 10
        and orbit_pairs == {(3, 3), (3, 4), (3, 5), (6, 4), (6, 5), (6, 6)},
        residual=first_reversal,
    )
    print(f"N_B3={len(ball)} N_orbits={len(orbits)} N_equivariant={1 << len(orbits)} first_reversal={first_reversal}")
    print(f"axis_body_pairs={sorted(orbit_pairs)}")

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
        "occupancy-only hop costs stay diamond",
        "|v|_2^2=9",
        "|v|_2^2=3",
        "Displayed, not adopted",
        "Do not write a cost into Admissibility",
        "authors no audit verdict",
        "FAIL / DO NOT SHIP",
        "one-seed front",
        "B_3(0)",
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

    print("per_element: six axis tips, eight body-diagonal tips, and every G+ occupancy orbit are executed")
    print("per_site: one-seed first arrival is scored on the induced B_3(0) graph")
    print("per_mode: checked and not executed — no spectral claim occurs")
    print("per_block: B_3(0) is the only comparison domain")
    print("lattice_wide: checked and not executed — no axiom edit and no adopted hop-cost")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
