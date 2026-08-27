#!/usr/bin/env python3
"""Exact metric-compatible exterior transport for variable D3 cells.

For inverse metrics h_s=g_s^-1 with positive coframes h_s=E_s.T E_s,
every tangent isometry A from the r one-form coordinates to the s one-form
coordinates has the form

    A = E_s^-1 R E_r,             R.T R = I.

If L(A) is the exterior lift and V_s^2=det(g_s), then

    U_sr = sqrt(V_r/V_s) L(A)

obeys U_sr.T D_s U_sr=D_r and intertwines the complete weighted exterior
Clifford systems.  The checks are exact SymPy algebra.  The orthogonal edge
factor R is supplied connection data; no physical rule for selecting it is
assumed here.
"""

from __future__ import annotations

import argparse
import itertools
import sys

import sympy as sp


AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_METRIC_COMPATIBLE_EXTERIOR_TRANSPORT_BOUNDED_THEOREM_NOTE_2026-08-27.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_VARIABLE_CELL_WEIGHTED_SKEW_EDGE_COUPLING_BOUNDED_THEOREM_NOTE_2026-08-27.md",
    "scripts/admissibility_dirac_kahler_variable_cell_weighted_skew_edge_coupling_2026_08_27.py",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

MUTATIONS = (
    "omit_density_factor",
    "transpose_target_coframe",
    "transpose_exterior_minors",
)

PASS = 0
FAIL = 0


def check(name: str, condition: object) -> None:
    global PASS, FAIL
    ok = bool(condition)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}", flush=True)
    PASS += int(ok)
    FAIL += int(not ok)


def matrix_is_zero(matrix: sp.MatrixBase) -> bool:
    return all(sp.simplify(entry) == 0 for entry in matrix)


# Exterior basis dt^t dx^x dy^y at corner index 4t+2x+y.
CORNERS = tuple(itertools.product((0, 1), repeat=3))
INDEX = {corner: 4 * corner[0] + 2 * corner[1] + corner[2]
         for corner in CORNERS}
ONE = (INDEX[(1, 0, 0)], INDEX[(0, 1, 0)], INDEX[(0, 0, 1)])
TWO = (INDEX[(0, 1, 1)], INDEX[(1, 0, 1)], INDEX[(1, 1, 0)])
WEDGE_SIGNATURE = sp.diag(1, -1, 1)


def wedge(direction: int) -> sp.Matrix:
    operator = sp.zeros(8)
    for corner in CORNERS:
        if corner[direction]:
            continue
        target = list(corner)
        target[direction] = 1
        sign = sp.Integer(-1) ** sum(corner[:direction])
        operator[INDEX[tuple(target)], INDEX[corner]] = sign
    return operator


WEDGES = tuple(wedge(direction) for direction in range(3))


def d3_carrier(g: sp.MatrixBase, volume: sp.Expr) -> sp.Matrix:
    inverse = sp.simplify(g.inv())
    carrier = sp.zeros(8)
    carrier[0, 0] = volume
    carrier[7, 7] = 1 / volume
    for row in range(3):
        for column in range(3):
            carrier[ONE[row], ONE[column]] = volume * inverse[row, column]
            carrier[TWO[row], TWO[column]] = (
                WEDGE_SIGNATURE * g * WEDGE_SIGNATURE / volume
            )[row, column]
    return sp.Matrix(carrier)


def weighted_generators(g: sp.MatrixBase,
                        volume: sp.Expr) -> tuple[sp.Matrix, ...]:
    carrier = d3_carrier(g, volume)
    inverse = carrier.inv()
    return tuple(sp.simplify(
        WEDGES[direction]
        + inverse * WEDGES[direction].T * carrier
    ) for direction in range(3))


def exterior_lift(matrix: sp.MatrixBase,
                  transpose_minors: bool = False) -> sp.Matrix:
    """Induced action on the ordered exterior basis via exact minors."""
    source = matrix.T if transpose_minors else matrix
    lift = sp.zeros(8)
    for input_corner in CORNERS:
        input_axes = [axis for axis, bit in enumerate(input_corner) if bit]
        degree = len(input_axes)
        for output_corner in CORNERS:
            output_axes = [axis for axis, bit in enumerate(output_corner) if bit]
            if len(output_axes) != degree:
                continue
            if degree == 0:
                coefficient = sp.Integer(1)
            else:
                coefficient = source.extract(output_axes, input_axes).det()
            lift[INDEX[output_corner], INDEX[input_corner]] = coefficient
    return lift


def rotation_z(cosine: sp.Expr, sine: sp.Expr) -> sp.Matrix:
    return sp.Matrix([
        [cosine, -sine, 0],
        [sine, cosine, 0],
        [0, 0, 1],
    ])


def rotation_x(cosine: sp.Expr, sine: sp.Expr) -> sp.Matrix:
    return sp.Matrix([
        [1, 0, 0],
        [0, cosine, -sine],
        [0, sine, cosine],
    ])


def rotation_y(cosine: sp.Expr, sine: sp.Expr) -> sp.Matrix:
    return sp.Matrix([
        [cosine, 0, sine],
        [0, 1, 0],
        [-sine, 0, cosine],
    ])


def gamma_in_direction(generators: tuple[sp.Matrix, ...],
                       direction: sp.MatrixBase) -> sp.Matrix:
    return sp.simplify(sum(
        (direction[axis] * generators[axis] for axis in range(3)),
        sp.zeros(8),
    ))


def main(mutation: str | None) -> int:
    coframes = (
        sp.eye(3),
        sp.Matrix([[sp.Rational(5, 4), sp.Rational(-3, 4), 0],
                   [0, 1, 0], [0, 0, 1]]),
        sp.Matrix([[1, 0, 0],
                   [0, sp.Rational(13, 12), sp.Rational(-5, 12)],
                   [0, 0, 1]]),
        sp.Matrix([[sp.Rational(6, 5), sp.Rational(1, 5), 0],
                   [0, 1, sp.Rational(1, 4)], [0, 0, 1]]),
    )
    inverse_metrics = tuple(sp.simplify(frame.T * frame)
                            for frame in coframes)
    metrics = tuple(sp.simplify(metric.inv()) for metric in inverse_metrics)
    volumes = tuple(sp.simplify(1 / frame.det()) for frame in coframes)
    carriers = tuple(d3_carrier(g, volume)
                     for g, volume in zip(metrics, volumes))
    generators = tuple(weighted_generators(g, volume)
                       for g, volume in zip(metrics, volumes))

    check("metric-volume locus: every coframe cell obeys V^2=det(g) exactly",
          all(sp.simplify(volume**2 - g.det()) == 0
              for g, volume in zip(metrics, volumes)))
    check("local Clifford carriers: every D3 is symmetric and every Gamma is D3-self-adjoint",
          all(carrier == carrier.T for carrier in carriers)
          and all(matrix_is_zero(gamma.T * carriers[site]
                                 - carriers[site] * gamma)
                  for site in range(4) for gamma in generators[site]))

    edges = ((0, 1), (1, 2), (2, 3), (3, 0))
    rotations = (
        rotation_z(sp.Rational(3, 5), sp.Rational(4, 5)),
        rotation_x(sp.Rational(5, 13), sp.Rational(12, 13)),
        rotation_y(sp.Rational(7, 25), sp.Rational(24, 25)),
        sp.diag(-1, 1, 1),
    )
    tangent_maps = []
    links = []
    lifts = []
    for edge, ((left, right), rotation) in enumerate(zip(edges, rotations)):
        right_frame = (coframes[right].T
                       if mutation == "transpose_target_coframe" and edge == 0
                       else coframes[right])
        tangent = sp.simplify(
            coframes[left].inv() * rotation * right_frame)
        lift = exterior_lift(
            tangent,
            transpose_minors=(mutation == "transpose_exterior_minors"
                              and edge == 0),
        )
        density = (sp.Integer(1) if mutation == "omit_density_factor"
                   and edge == 0 else sp.sqrt(volumes[right] / volumes[left]))
        tangent_maps.append(tangent)
        lifts.append(lift)
        links.append(sp.simplify(density * lift))

    check("tangent compatibility: every A satisfies A^T g_s^-1 A=g_r^-1",
          all(matrix_is_zero(
              tangent_maps[edge].T * inverse_metrics[left]
              * tangent_maps[edge] - inverse_metrics[right])
              for edge, (left, right) in enumerate(edges)))
    check("coframe classification: recovered R=E_s A E_r^-1 is exactly orthogonal",
          all(matrix_is_zero(
              (coframes[left] * tangent_maps[edge]
               * coframes[right].inv()).T
              * (coframes[left] * tangent_maps[edge]
                 * coframes[right].inv()) - sp.eye(3))
              for edge, (left, right) in enumerate(edges)))
    check("determinant-volume law: |det(A)|=V_s/V_r on every compatible edge",
          all(sp.simplify(abs(tangent_maps[edge].det())
                          - volumes[left] / volumes[right]) == 0
              for edge, (left, right) in enumerate(edges)))
    check("exterior functor: lifted products agree with products of lifted maps",
          matrix_is_zero(
              exterior_lift(tangent_maps[0] * tangent_maps[1])
              - exterior_lift(tangent_maps[0])
              * exterior_lift(tangent_maps[1])))
    check("wedge naturality: Lambda(A) epsilon(q)=epsilon(Aq) Lambda(A)",
          all(matrix_is_zero(
              lifts[edge] * WEDGES[direction]
              - sum((tangent_maps[edge][axis, direction] * WEDGES[axis]
                     for axis in range(3)), sp.zeros(8)) * lifts[edge])
              for edge in range(4) for direction in range(3)))
    check("full carrier isometry: U^T D_s U=D_r requires the positive volume normalization",
          all(matrix_is_zero(
              links[edge].T * carriers[left] * links[edge]
              - carriers[right])
              for edge, (left, right) in enumerate(edges)))

    check("Clifford intertwining: Gamma_s(Aq) U=U Gamma_r(q) in all basis directions",
          all(matrix_is_zero(
              gamma_in_direction(generators[left],
                                 tangent_maps[edge][:, direction])
              * links[edge] - links[edge] * generators[right][direction])
              for edge, (left, right) in enumerate(edges)
              for direction in range(3)))
    check("reverse-link law: the compatible reverse transport is exactly U^-1",
          all(matrix_is_zero(
              sp.sqrt(volumes[left] / volumes[right])
              * exterior_lift(tangent_maps[edge].inv()) - links[edge].inv())
              for edge, (left, right) in enumerate(edges)))

    # Under compatibility, the two endpoint contributions of Block 215 agree.
    directions = (sp.eye(3)[:, 0], sp.eye(3)[:, 1],
                  sp.eye(3)[:, 2], sp.Matrix([1, 1, 0]))
    cross_forms = []
    collapsed = []
    for edge, ((left, right), direction) in enumerate(zip(edges, directions)):
        gamma_right = gamma_in_direction(generators[right], direction)
        gamma_left = gamma_in_direction(
            generators[left], tangent_maps[edge] * direction)
        left_form = carriers[left] * gamma_left * links[edge]
        right_form = links[edge].inv().T * carriers[right] * gamma_right
        cross_forms.append(sp.simplify((left_form + right_form) / 4))
        collapsed.append(sp.simplify(left_form / 2))
    check("endpoint collapse: compatible transport makes the two cross-form contributions identical",
          all(matrix_is_zero(cross_forms[edge] - collapsed[edge])
              for edge in range(4)))
    check("covariant centered hop: K_sr=Gamma_s(Aq)U/2=U Gamma_r(q)/2",
          all(matrix_is_zero(
              carriers[left].inv() * cross_forms[edge]
              - links[edge] * gamma_in_direction(
                  generators[right], directions[edge]) / 2)
              for edge, (left, right) in enumerate(edges)))

    # The endpoint metrics do not choose the orthogonal edge factor.
    flat_rotation = rotations[0]
    flat_link = exterior_lift(flat_rotation)
    check("connection freedom: equal endpoint metrics admit a nonidentity compatible orthogonal link",
          flat_rotation.T * flat_rotation == sp.eye(3)
          and flat_rotation != sp.eye(3)
          and flat_link.T * d3_carrier(sp.eye(3), 1) * flat_link
          == d3_carrier(sp.eye(3), 1))

    # Coframe representatives may rotate without changing h or A.
    gauges = (
        rotation_z(sp.Rational(5, 13), sp.Rational(12, 13)),
        rotation_x(sp.Rational(7, 25), sp.Rational(24, 25)),
        rotation_y(sp.Rational(3, 5), sp.Rational(4, 5)),
        sp.diag(1, -1, 1),
    )
    changed_frames = tuple(gauges[site] * coframes[site]
                           for site in range(4))
    changed_rotations = tuple(sp.simplify(
        gauges[left] * rotations[edge] * gauges[right].T)
        for edge, (left, right) in enumerate(edges))
    check("coframe gauge covariance: E->QE and R->Q_s R Q_r^T leave every A unchanged",
          all(matrix_is_zero(
              changed_frames[left].inv() * changed_rotations[edge]
              * changed_frames[right] - tangent_maps[edge])
              for edge, (left, right) in enumerate(edges)))

    flat_carrier = d3_carrier(sp.eye(3), sp.Integer(1))
    flat_generators = weighted_generators(sp.eye(3), sp.Integer(1))
    identity_link = exterior_lift(sp.eye(3))
    check("constant-cell normalization: E_s=E_r and R=I give U=I and the parent half-hop",
          identity_link == sp.eye(8)
          and matrix_is_zero(
              flat_carrier.inv()
              * (flat_carrier * flat_generators[0] * identity_link / 2)
              - flat_generators[0] / 2))

    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("RESULT:")
    print("  tangent theorem: A=E_s^-1 R E_r with R orthogonal")
    print("  exterior link: U=sqrt(V_r/V_s) Lambda(A) is a D3 isometry and Clifford intertwiner")
    print("  bridge: the Block 215 cross-form collapses to the covariant centered half-hop")
    print("  boundary: R is independent connection data; its physical selection, curvature dynamics, time, and continuum remain open")
    return int(FAIL != 0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    arguments = parser.parse_args()
    sys.exit(main(arguments.mutation))
