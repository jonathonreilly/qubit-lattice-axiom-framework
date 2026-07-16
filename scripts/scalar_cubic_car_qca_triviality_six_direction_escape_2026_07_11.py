#!/usr/bin/env python3
"""Exact checks for the scalar cubic CAR-QCA classification and carrier escape."""

import itertools
from pathlib import Path

import numpy as np
import sympy as sp


PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str) -> None:
    global PASS, FAIL
    if bool(condition):
        PASS += 1
        print(f"PASS {name}: {detail}")
    else:
        FAIL += 1
        print(f"FAIL {name}: {detail}")


def permutation_sign(permutation: tuple[int, ...]) -> int:
    inversions = sum(
        permutation[i] > permutation[j]
        for i in range(len(permutation))
        for j in range(i + 1, len(permutation))
    )
    return -1 if inversions % 2 else 1


def proper_cubic_rotations() -> list[tuple[tuple[int, ...], ...]]:
    rotations = []
    for permutation in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            if permutation_sign(permutation) * np.prod(signs) != 1:
                continue
            rotations.append(
                tuple(
                    tuple(signs[row] if column == permutation[row] else 0 for column in range(3))
                    for row in range(3)
                )
            )
    return rotations


def act(rotation: tuple[tuple[int, ...], ...], vector: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sum(rotation[i][j] * vector[j] for j in range(3)) for i in range(3))


def compose(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    """Permutation left after right, stored as source -> target."""
    return tuple(left[right[index]] for index in range(len(left)))


def inverse(permutation: tuple[int, ...]) -> tuple[int, ...]:
    result = [0] * len(permutation)
    for source, target in enumerate(permutation):
        result[target] = source
    return tuple(result)


def vertices(side: int) -> list[tuple[int, ...]]:
    return list(itertools.product(range(side), repeat=3))


def direction_shift_permutation(
    side: int,
    directions: tuple[tuple[int, ...], ...],
) -> tuple[int, ...]:
    verts = vertices(side)
    vertex_index = {vertex: index for index, vertex in enumerate(verts)}
    result = [0] * (len(verts) * len(directions))
    for vertex in verts:
        for direction_index, direction in enumerate(directions):
            target = tuple((vertex[axis] + direction[axis]) % side for axis in range(3))
            source_index = len(directions) * vertex_index[vertex] + direction_index
            target_index = len(directions) * vertex_index[target] + direction_index
            result[source_index] = target_index
    return tuple(result)


def spatial_rotation_permutation(
    side: int,
    directions: tuple[tuple[int, ...], ...],
    rotation: tuple[tuple[int, ...], ...],
) -> tuple[int, ...]:
    verts = vertices(side)
    vertex_index = {vertex: index for index, vertex in enumerate(verts)}
    direction_index = {direction: index for index, direction in enumerate(directions)}
    result = [0] * (len(verts) * len(directions))
    for vertex in verts:
        rotated_vertex = tuple(value % side for value in act(rotation, vertex))
        for old_direction_index, direction in enumerate(directions):
            rotated_direction_index = direction_index[act(rotation, direction)]
            source = len(directions) * vertex_index[vertex] + old_direction_index
            target = len(directions) * vertex_index[rotated_vertex] + rotated_direction_index
            result[source] = target
    return tuple(result)


def translation_permutation(
    side: int,
    directions: tuple[tuple[int, ...], ...],
    translation: tuple[int, ...],
) -> tuple[int, ...]:
    verts = vertices(side)
    vertex_index = {vertex: index for index, vertex in enumerate(verts)}
    result = [0] * (len(verts) * len(directions))
    for vertex in verts:
        target_vertex = tuple((vertex[axis] + translation[axis]) % side for axis in range(3))
        for direction_index in range(len(directions)):
            source = len(directions) * vertex_index[vertex] + direction_index
            target = len(directions) * vertex_index[target_vertex] + direction_index
            result[source] = target
    return tuple(result)


def cubic_group_checks() -> tuple[list[tuple[tuple[int, ...], ...]], tuple[tuple[int, ...], ...]]:
    rotations = proper_cubic_rotations()
    check("G01", len(rotations) == 24 and len(set(rotations)) == 24, "the proper cubic rotation group has 24 exact signed-permutation matrices")
    check("G02", all(round(np.linalg.det(np.array(rotation))) == 1 for rotation in rotations), "every generated cubic matrix has determinant +1")

    stacked = sp.Matrix.vstack(*[sp.Matrix(rotation) - sp.eye(3) for rotation in rotations])
    check("G03", stacked.rank() == 3 and len(stacked.nullspace()) == 0, "the only vector fixed by every proper cubic rotation is zero")

    direction_seed = (1, 0, 0)
    direction_orbit = tuple(sorted({act(rotation, direction_seed) for rotation in rotations}))
    expected = tuple(sorted(((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))))
    check("G04", direction_orbit == expected, "the nearest-neighbor direction orbit has exactly six elements")

    orbit_sizes = {
        len({act(rotation, vector) for rotation in rotations})
        for vector in itertools.product(range(-2, 3), repeat=3)
        if vector != (0, 0, 0)
    }
    check("G05", min(orbit_sizes) == 6 and orbit_sizes == {6, 8, 12, 24}, "nonzero cubic displacement orbits in the exhaustive radius-two box have sizes 6, 8, 12, or 24")
    return rotations, direction_orbit


def scalar_laurent_checks(rotations: list[tuple[tuple[int, ...], ...]]) -> None:
    # General support-collapse certificate.  For any finite Laurent support,
    # choose an integer linear functional with unique extrema.  The extreme
    # autocorrelation coefficient of u*conjugate(u) then contains exactly the
    # product a_max conjugate(a_min), so constant modulus forbids two endpoints.
    def extreme_coefficient(support: tuple[tuple[int, ...], ...]) -> tuple[sp.Expr, sp.Expr, int]:
        bound = max(abs(value) for point in support for value in point)
        base = 2 * bound + 2
        weights = tuple(base**axis for axis in range(len(support[0])))
        score = lambda point: sum(weights[axis] * point[axis] for axis in range(len(point)))
        low = min(support, key=score)
        high = max(support, key=score)
        delta = tuple(high[axis] - low[axis] for axis in range(len(low)))
        coefficients = {point: sp.Symbol("a_" + "_".join(map(str, point)), complex=True) for point in support}
        pairs = [
            (left, right)
            for left in support
            for right in support
            if tuple(left[axis] - right[axis] for axis in range(len(left))) == delta
        ]
        coefficient = sp.simplify(sum(coefficients[left] * sp.conjugate(coefficients[right]) for left, right in pairs))
        expected = coefficients[high] * sp.conjugate(coefficients[low])
        return coefficient, expected, len(pairs)

    support_1d = tuple((value,) for value in range(-3, 4))
    coefficient, expected, pair_count = extreme_coefficient(support_1d)
    check("S01A", pair_count == 1 and sp.simplify(coefficient - expected) == 0, "the general one-variable extreme autocorrelation coefficient is the unique endpoint product")

    support_3d = tuple(itertools.product((-1, 0, 1), repeat=3))
    coefficient, expected, pair_count = extreme_coefficient(support_3d)
    check("S01B", pair_count == 1 and sp.simplify(coefficient - expected) == 0, "the full radius-one three-variable support has the same unique extreme-pair certificate")

    sparse_3d = ((-2, 1, 0), (-1, -2, 2), (0, 0, 0), (1, 2, -1), (2, -1, 1))
    coefficient, expected, pair_count = extreme_coefficient(sparse_3d)
    check("S01C", pair_count == 1 and sp.simplify(coefficient - expected) == 0, "a nonsymmetric sparse three-variable support is also collapsed by the generic-extrema proof")

    z1, z2, z3 = sp.symbols("z1 z2 z3")
    blend = (z1 + z2) / sp.sqrt(2)
    samples = ((0.2, 0.7, 1.1), (0.9, 0.9, 2.0), (1.4, 2.2, 0.3))
    blend_moduli = [
        abs(complex(blend.subs({z1: np.exp(1j * k1), z2: np.exp(1j * k2), z3: np.exp(1j * k3)})))
        for k1, k2, k3 in samples
    ]
    check("S01", any(abs(value - 1) > 1e-6 for value in blend_moduli), "a two-direction scalar Laurent blend fails torus unitarity")

    winding = (1, -2, 1)
    monomial = z1**winding[0] * z2**winding[1] * z3**winding[2]
    monomial_ok = all(
        abs(abs(complex(monomial.subs({z1: np.exp(1j * k1), z2: np.exp(1j * k2), z3: np.exp(1j * k3)}))) - 1) < 1e-12
        for k1, k2, k3 in samples
    )
    check("S02", monomial_ok, "scalar Laurent monomials are exactly unimodular on the torus")

    rotated = {act(rotation, winding) for rotation in rotations}
    check("S03", len(rotated) > 1, "a nonzero scalar monomial winding is moved by proper cubic rotations")
    check("S04", all(act(rotation, (0, 0, 0)) == (0, 0, 0) for rotation in rotations), "zero winding is proper-cubic invariant")

    axis_shift = (1, 0, 0)
    axis_orbit = {act(rotation, axis_shift) for rotation in rotations}
    check("S05", len(axis_orbit) == 6, "dropping cubic invariance admits six symmetry-related scalar nearest-neighbor shifts")


def general_car_bridge_checks() -> None:
    root_two = sp.sqrt(2)
    hadamard = sp.Matrix([[1, 1], [1, -1]]) / root_two
    plus = sp.diag(1, 0)
    minus = sp.diag(0, 1)
    coefficients = {
        1: sp.simplify(hadamard * plus * hadamard),
        -1: sp.simplify(hadamard * minus * hadamard),
    }

    def isometry_coefficient(delta: int) -> sp.Matrix:
        return sp.simplify(sum(
            (coefficients[h].H * coefficients[h + delta] for h in coefficients if h + delta in coefficients),
            sp.zeros(2),
        ))

    def coisometry_coefficient(delta: int) -> sp.Matrix:
        return sp.simplify(sum(
            (coefficients[h + delta] * coefficients[h].H for h in coefficients if h + delta in coefficients),
            sp.zeros(2),
        ))

    expected = lambda delta: sp.eye(2) if delta == 0 else sp.zeros(2)
    check("L01", all(isometry_coefficient(delta) == expected(delta) for delta in range(-2, 3)), "a non-diagonal 2x2 Laurent family satisfies every U-dagger-U Fourier coefficient identity")
    check("L02", all(coisometry_coefficient(delta) == expected(delta) for delta in range(-2, 3)), "the same family satisfies every U-U-dagger coisometry identity")

    inverse_coefficients = {-h: matrix.H for h, matrix in coefficients.items()}

    def convolution(left: dict[int, sp.Matrix], right: dict[int, sp.Matrix], delta: int) -> sp.Matrix:
        return sp.simplify(sum(
            (left[h] * right[delta - h] for h in left if delta - h in right),
            sp.zeros(2),
        ))

    check("L03", all(convolution(inverse_coefficients, coefficients, delta) == expected(delta) for delta in range(-2, 3)), "the coefficient formula V_h=U_(-h)^dagger is an exact left inverse")
    check("L04", all(convolution(coefficients, inverse_coefficients, delta) == expected(delta) for delta in range(-2, 3)), "the same finite coefficient family is an exact right inverse")
    check("L05", max(map(abs, coefficients)) == max(map(abs, inverse_coefficients)) == 1, "the nontrivial Laurent tick and its inverse have equal finite range")

    z = sp.symbols("z", nonzero=True)
    symbol = sp.simplify(coefficients[1] * z + coefficients[-1] / z)
    inverse_symbol = sp.simplify(inverse_coefficients[1] * z + inverse_coefficients[-1] / z)
    check("L06", sp.simplify(inverse_symbol * symbol) == sp.eye(2), "the matrix-valued Laurent symbols multiply to identity exactly")


def car_lift_and_escape_checks(
    rotations: list[tuple[tuple[int, ...], ...]],
    directions: tuple[tuple[int, ...], ...],
) -> None:
    side = 4
    tick = direction_shift_permutation(side, directions)
    tick_inverse = inverse(tick)
    identity = tuple(range(len(tick)))
    check("C01", sorted(tick) == list(identity), "the six-direction one-particle update is a unitary permutation")
    check("C02", compose(tick_inverse, tick) == identity and compose(tick, tick_inverse) == identity, "the inverse update is exact and finite-range")

    for translation in ((1, 0, 0), (0, 1, 0), (0, 0, 1)):
        shift = translation_permutation(side, directions, translation)
        if compose(shift, tick) != compose(tick, shift):
            check("C03", False, "the direction update commutes with all unit translations")
            break
    else:
        check("C03", True, "the direction update commutes with all unit translations")

    cubic_covariant = True
    for rotation in rotations:
        spatial = spatial_rotation_permutation(side, directions, rotation)
        if compose(spatial, compose(tick, inverse(spatial))) != tick:
            cubic_covariant = False
            break
    check("C04", cubic_covariant, "the six-direction update is covariant under all 24 proper cubic rotations")

    verts = vertices(side)
    vertex_index = {vertex: index for index, vertex in enumerate(verts)}
    max_forward = 0
    max_inverse = 0
    for vertex in verts:
        for direction_index, direction in enumerate(directions):
            source = len(directions) * vertex_index[vertex] + direction_index
            forward_target = tick[source] // len(directions)
            inverse_target = tick_inverse[source] // len(directions)
            for target, accumulator in ((forward_target, "forward"), (inverse_target, "inverse")):
                target_vertex = verts[target]
                wrapped = [min((target_vertex[i] - vertex[i]) % side, (vertex[i] - target_vertex[i]) % side) for i in range(3)]
                distance = sum(wrapped)
                if accumulator == "forward":
                    max_forward = max(max_forward, distance)
                else:
                    max_inverse = max(max_inverse, distance)
    check("C05", max_forward == 1 and max_inverse == 1, "both the tick and inverse have exact graph radius one")

    total_winding = tuple(sum(direction[axis] for direction in directions) for axis in range(3))
    check("C06", total_winding == (0, 0, 0), "the six dispersive direction bands have zero total determinant winding")
    check("C07", all(any(component != 0 for component in direction) for direction in directions), "every direction band transports despite zero total determinant winding")
    check("C08", 2 ** len(directions) == 64, "six fermionic modes require local Fock dimension 64 in this explicit escape")

    # CAR preservation for a number-preserving linear lift is the coefficient
    # identity U U^dag=I.  The permutation supplies that identity exactly.
    permutation_matrix = sp.zeros(len(tick), len(tick))
    for source, target in enumerate(tick):
        permutation_matrix[target, source] = 1
    check("C09", permutation_matrix.T * permutation_matrix == sp.eye(len(tick)), "the finite-torus coefficient matrix preserves the CAR anticommutator exactly")

    # Zero total winding alone is not a no-transport condition.
    k = sp.symbols("k", real=True)
    paired = sp.diag(sp.exp(sp.I * k), sp.exp(-sp.I * k))
    check("C10", sp.simplify(paired.det()) == 1 and paired != sp.eye(2), "opposite-moving bands have determinant one while remaining dispersive")


def source_checks() -> None:
    path = Path("docs/SCALAR_CUBIC_CAR_QCA_TRIVIALITY_AND_SIX_DIRECTION_ESCAPE_BOUNDED_THEOREM_NOTE_2026-07-11.md")
    check("N01", path.exists(), "source note exists")
    text = path.read_text() if path.exists() else ""
    markers = (
        "supplied CAR realization",
        "does not classify all qubit QCAs",
        "does not derive the physical tick",
        "does not establish that an axiom update is necessary",
    )
    for index, marker in enumerate(markers, 2):
        check(f"N{index:02d}", marker in text, f"source contains boundary marker: {marker}")


def main() -> int:
    rotations, directions = cubic_group_checks()
    scalar_laurent_checks(rotations)
    general_car_bridge_checks()
    car_lift_and_escape_checks(rotations, directions)
    source_checks()
    print("BOUNDARY: the CAR algebra, linear number-preserving update, finite Laurent range, and cubic action are explicit conditional inputs.")
    print("BOUNDARY: the one-mode theorem is exhaustive only for scalar Gaussian/CAR ticks; interacting and general qubit QCAs remain open.")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
