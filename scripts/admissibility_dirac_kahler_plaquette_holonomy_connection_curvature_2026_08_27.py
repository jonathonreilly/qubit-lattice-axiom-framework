#!/usr/bin/env python3
"""Exact plaquette holonomy of metric-compatible D3 exterior links.

For A_sr=E_s^-1 R_sr E_r and
U_sr=sqrt(V_r/V_s) Lambda(A_sr), a closed ordered product telescopes to

    H_A = E_0^-1 (product R) E_0,
    H_U = Lambda(H_A).

The endpoint-only section R=I is therefore exactly flat, while nonidentity
orthogonal product supplies nontrivial compatible holonomy. A positive
D3-based plaquette defect is also checked. Connection selection and a
gravitational action remain open follow-on obligations.
"""

from __future__ import annotations

import argparse
import itertools
import sys

import sympy as sp


AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_PLAQUETTE_HOLONOMY_CONNECTION_CURVATURE_BOUNDED_THEOREM_NOTE_2026-08-27.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_METRIC_COMPATIBLE_EXTERIOR_TRANSPORT_BOUNDED_THEOREM_NOTE_2026-08-27.md",
    "scripts/admissibility_dirac_kahler_metric_compatible_exterior_transport_2026_08_27.py",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

MUTATIONS = (
    "drop_closing_link",
    "reverse_connection_order",
    "break_density_cocycle",
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


def product(matrices: tuple[sp.Matrix, ...], size: int) -> sp.Matrix:
    result = sp.eye(size)
    for matrix in matrices:
        result = sp.simplify(result * matrix)
    return result


def block_diagonal(matrices: tuple[sp.Matrix, ...]) -> sp.Matrix:
    return sp.diag(*matrices)


def assemble_blocks(blocks: list[list[sp.Matrix]]) -> sp.Matrix:
    return sp.Matrix.vstack(*(sp.Matrix.hstack(*row) for row in blocks))


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


def exterior_lift(matrix: sp.MatrixBase) -> sp.Matrix:
    lift = sp.zeros(8)
    for input_corner in CORNERS:
        input_axes = [axis for axis, bit in enumerate(input_corner) if bit]
        degree = len(input_axes)
        for output_corner in CORNERS:
            output_axes = [axis for axis, bit in enumerate(output_corner) if bit]
            if len(output_axes) != degree:
                continue
            coefficient = (sp.Integer(1) if degree == 0 else
                           matrix.extract(output_axes, input_axes).det())
            lift[INDEX[output_corner], INDEX[input_corner]] = coefficient
    return lift


def rotation_z(cosine: sp.Expr, sine: sp.Expr) -> sp.Matrix:
    return sp.Matrix([[cosine, -sine, 0], [sine, cosine, 0], [0, 0, 1]])


def rotation_x(cosine: sp.Expr, sine: sp.Expr) -> sp.Matrix:
    return sp.Matrix([[1, 0, 0], [0, cosine, -sine], [0, sine, cosine]])


def rotation_y(cosine: sp.Expr, sine: sp.Expr) -> sp.Matrix:
    return sp.Matrix([[cosine, 0, sine], [0, 1, 0], [-sine, 0, cosine]])


def gamma_in_direction(generators: tuple[sp.Matrix, ...],
                       direction: sp.MatrixBase) -> sp.Matrix:
    return sp.simplify(sum(
        (direction[axis] * generators[axis] for axis in range(3)),
        sp.zeros(8),
    ))


def positive_by_sylvester(matrix: sp.MatrixBase) -> bool:
    return all(sp.simplify(matrix[:size, :size].det()) > 0
               for size in range(1, matrix.rows + 1))


def plaquette_defect(holonomy: sp.MatrixBase,
                     carrier: sp.MatrixBase) -> sp.Expr:
    delta = holonomy - sp.eye(holonomy.rows)
    return sp.simplify(sp.trace(
        carrier.inv() * delta.T * carrier * delta
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
    edges = ((0, 1), (1, 2), (2, 3), (3, 0))

    check("positive variable cells: every D3 is exact positive symmetric on V^2=det(g)",
          all(sp.simplify(volume**2 - g.det()) == 0
              for g, volume in zip(metrics, volumes))
          and all(carrier == carrier.T and positive_by_sylvester(carrier)
                  for carrier in carriers))

    rotations = (
        rotation_z(sp.Rational(3, 5), sp.Rational(4, 5)),
        rotation_x(sp.Rational(5, 13), sp.Rational(12, 13)),
        rotation_y(sp.Rational(7, 25), sp.Rational(24, 25)),
        sp.eye(3),
    )
    endpoint_rotations = (sp.eye(3),) * 4

    tangent_maps = tuple(sp.simplify(
        coframes[left].inv() * rotations[edge] * coframes[right])
        for edge, (left, right) in enumerate(edges))
    endpoint_maps = tuple(sp.simplify(
        coframes[left].inv() * coframes[right])
        for left, right in edges)
    densities = [sp.sqrt(volumes[right] / volumes[left])
                 for left, right in edges]
    if mutation == "break_density_cocycle":
        densities[0] *= 2
    links = tuple(sp.simplify(densities[edge]
                             * exterior_lift(tangent_maps[edge]))
                  for edge in range(4))
    endpoint_links = tuple(sp.simplify(
        sp.sqrt(volumes[right] / volumes[left])
        * exterior_lift(endpoint_maps[edge]))
        for edge, (left, right) in enumerate(edges))

    check("edge compatibility: all tangent maps and exterior links preserve endpoint metrics",
          all(matrix_is_zero(
              tangent_maps[edge].T * inverse_metrics[left]
              * tangent_maps[edge] - inverse_metrics[right])
              for edge, (left, right) in enumerate(edges))
          and all(matrix_is_zero(
              links[edge].T * carriers[left] * links[edge]
              - carriers[right])
              for edge, (left, right) in enumerate(edges)))

    loop_tangent_maps = (tangent_maps[:3]
                         if mutation == "drop_closing_link" else tangent_maps)
    loop_links = (links[:3] if mutation == "drop_closing_link" else links)
    loop_endpoint_maps = (endpoint_maps[:3]
                          if mutation == "drop_closing_link" else endpoint_maps)
    loop_endpoint_links = (endpoint_links[:3]
                           if mutation == "drop_closing_link" else endpoint_links)
    tangent_holonomy = product(tuple(loop_tangent_maps), 3)
    exterior_holonomy = product(tuple(loop_links), 8)
    endpoint_tangent_holonomy = product(tuple(loop_endpoint_maps), 3)
    endpoint_exterior_holonomy = product(tuple(loop_endpoint_links), 8)
    connection_sequence = (tuple(reversed(rotations))
                           if mutation == "reverse_connection_order"
                           else rotations)
    connection_holonomy = product(connection_sequence, 3)
    density_holonomy = sp.simplify(product(tuple(
        sp.Matrix([[density]]) for density in densities), 1)[0, 0])

    check("closed-loop density cocycle: product sqrt(V_next/V_current)=1",
          density_holonomy == 1)
    check("tangent telescoping: H_A=E_0^-1(product R)E_0",
          matrix_is_zero(
              tangent_holonomy
              - coframes[0].inv() * connection_holonomy * coframes[0]))
    check("exterior functoriality: H_U=Lambda(H_A) after density cancellation",
          matrix_is_zero(exterior_holonomy
                         - exterior_lift(tangent_holonomy)))
    check("loop carrier isometry: the full holonomy preserves the base D3 carrier",
          matrix_is_zero(exterior_holonomy.T * carriers[0]
                         * exterior_holonomy - carriers[0]))

    check("endpoint-only flat section: varying coframes with every R=I give identity holonomy",
          product(endpoint_rotations, 3) == sp.eye(3)
          and endpoint_tangent_holonomy == sp.eye(3)
          and endpoint_exterior_holonomy == sp.eye(8))
    check("connection curvature carrier: nonidentity product R gives nonidentity compatible holonomy",
          connection_holonomy != sp.eye(3)
          and tangent_holonomy != sp.eye(3)
          and exterior_holonomy != sp.eye(8))
    check("exterior faithfulness: the degree-one block recovers the tangent holonomy exactly",
          exterior_holonomy.extract(ONE, ONE) == tangent_holonomy)

    defect = plaquette_defect(exterior_holonomy, carriers[0])
    trace_defect = sp.simplify(
        16 - sp.trace(exterior_holonomy) - sp.trace(exterior_holonomy.inv()))
    check("positive plaquette defect: ||H_U-I||_D^2 is positive and equals the isometry trace form",
          defect > 0 and sp.simplify(defect - trace_defect) == 0)
    check("flat plaquette defect: endpoint-only identity holonomy has exactly zero defect",
          plaquette_defect(endpoint_exterior_holonomy, carriers[0]) == 0)

    # A flat-carrier one-rotation control gives a readable exact invariant.
    simple_rotation = rotations[0]
    simple_holonomy = exterior_lift(simple_rotation)
    flat_carrier = d3_carrier(sp.eye(3), sp.Integer(1))
    check("single-angle control: trace Lambda(R)=32/5 and the positive defect is 16/5",
          sp.trace(simple_holonomy) == sp.Rational(32, 5)
          and plaquette_defect(simple_holonomy, flat_carrier)
          == sp.Rational(16, 5))

    # A change of coframe representatives leaves A and U invariant while the
    # orthogonal product changes only by conjugation at the base site.
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
    changed_maps = tuple(sp.simplify(
        changed_frames[left].inv() * changed_rotations[edge]
        * changed_frames[right])
        for edge, (left, right) in enumerate(edges))
    changed_connection_holonomy = product(changed_rotations, 3)
    check("coframe gauge law: edge maps stay fixed and product R conjugates at the base",
          changed_maps == tangent_maps
          and matrix_is_zero(
              changed_connection_holonomy
              - gauges[0] * product(rotations, 3) * gauges[0].T))

    # Moving the base point cyclically conjugates both holonomies and leaves
    # the scalar defect unchanged.
    tangent_at_one = product((tangent_maps[1], tangent_maps[2],
                              tangent_maps[3], tangent_maps[0]), 3)
    exterior_at_one = product((links[1], links[2], links[3], links[0]), 8)
    check("base-point covariance: cyclic holonomy is conjugate by the first edge map",
          matrix_is_zero(tangent_at_one
                         - tangent_maps[0].inv() * tangent_holonomy
                         * tangent_maps[0])
          and matrix_is_zero(exterior_at_one
                             - links[0].inv() * exterior_holonomy * links[0]))
    check("base-point invariant defect: the D3 plaquette scalar is unchanged",
          sp.simplify(plaquette_defect(exterior_at_one, carriers[1])
                      - defect) == 0)

    reverse_tangent = product(tuple(matrix.inv()
                                    for matrix in reversed(tangent_maps)), 3)
    reverse_exterior = product(tuple(matrix.inv()
                                     for matrix in reversed(links)), 8)
    check("orientation reversal: the reverse plaquette holonomies are exact inverses",
          matrix_is_zero(reverse_tangent - tangent_holonomy.inv())
          and matrix_is_zero(reverse_exterior - exterior_holonomy.inv()))

    # The nontrivial connection holonomy remains compatible with the global
    # Block 215 weighted-skew operator.
    directions = (sp.eye(3)[:, 0], sp.eye(3)[:, 1],
                  sp.eye(3)[:, 2], sp.Matrix([1, 1, 0]))
    blocks = [[sp.zeros(8) for _ in range(4)] for _ in range(4)]
    endpoint_equalities = []
    for edge, ((left, right), direction) in enumerate(zip(edges, directions)):
        gamma_right = gamma_in_direction(generators[right], direction)
        gamma_left = gamma_in_direction(
            generators[left], tangent_maps[edge] * direction)
        left_form = carriers[left] * gamma_left * links[edge]
        right_form = links[edge].inv().T * carriers[right] * gamma_right
        endpoint_equalities.append(matrix_is_zero(left_form - right_form))
        cross = sp.simplify(left_form / 2)
        blocks[left][right] += carriers[left].inv() * cross
        blocks[right][left] -= carriers[right].inv() * cross.T
    kernel = assemble_blocks(blocks)
    global_carrier = block_diagonal(carriers)
    check("compatible edge collapse: both endpoint forms agree around the plaquette",
          all(endpoint_equalities))
    check("operator coexistence: nontrivial holonomy preserves global weighted skew-adjointness",
          matrix_is_zero(global_carrier * kernel
                         + kernel.T * global_carrier))

    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("RESULT:")
    print("  plaquette theorem: endpoint coframes and density factors telescope exactly")
    print("  curvature carrier: full exterior holonomy is faithful to the ordered orthogonal edge product")
    print("  scalar diagnostic: the D3 plaquette defect is positive, base-point invariant, and zero exactly at identity holonomy")
    print("  follow-on obligations: R selection, plaquette action, time interpretation, gravity dynamics, and continuum limit")
    return int(FAIL != 0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    arguments = parser.parse_args()
    sys.exit(main(arguments.mutation))
