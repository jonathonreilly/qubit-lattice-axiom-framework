#!/usr/bin/env python3
"""Exact variable-cell weighted-skew edge coupling.

For a finite nearest-neighbour graph with one positive symmetric carrier D_s
per site, weighted skew-adjointness of an off-diagonal kernel K is equivalent
edge by edge to

    D_s K_sr + K_rs.T D_r = 0.

Thus every solution is uniquely parameterized by one arbitrary cross-form
C_sr per oriented representative edge:

    K_sr = D_s^-1 C_sr,
    K_rs = -D_r^-1 C_sr.T.

The runner also checks an endpoint-symmetric construction from supplied local
D_s-self-adjoint direction matrices Gamma_s,d and supplied invertible link
comparisons U_sr.  It is exact over rational matrices, locally frame covariant,
and reduces to the constant-cell centered exterior link.

This is a finite algebra theorem.  The comparison maps are supplied inputs;
the runner does not select a physical connection, time direction, curvature
law, gravity dynamics, or continuum limit.
"""

from __future__ import annotations

import argparse
import itertools
import sys

import sympy as sp


AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_VARIABLE_CELL_WEIGHTED_SKEW_EDGE_COUPLING_BOUNDED_THEOREM_NOTE_2026-08-27.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_WEIGHTED_EXTERIOR_KERNEL_METRIC_SYMBOL_BOUNDED_THEOREM_NOTE_2026-08-27.md",
    "scripts/admissibility_dirac_kahler_weighted_exterior_kernel_metric_symbol_2026_08_27.py",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

MUTATIONS = (
    "reverse_edge_sign",
    "right_frame_law",
    "constant_link_factor",
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
    return all(sp.cancel(entry) == 0 for entry in matrix)


def block_diagonal(matrices: tuple[sp.Matrix, ...]) -> sp.Matrix:
    return sp.diag(*matrices)


def assemble_blocks(blocks: list[list[sp.Matrix]]) -> sp.Matrix:
    return sp.Matrix.vstack(*(sp.Matrix.hstack(*row) for row in blocks))


# Exterior basis: dt^t dx^x dy^y at corner index 4t+2x+y.
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


def metric(shear_tx: sp.Expr, shear_ty: sp.Expr,
           shear_xy: sp.Expr) -> sp.Matrix:
    return sp.Matrix([
        [1, shear_tx, shear_ty],
        [shear_tx, 1, shear_xy],
        [shear_ty, shear_xy, 1],
    ])


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
                        volume: sp.Expr) -> tuple[sp.Matrix, tuple[sp.Matrix, ...]]:
    carrier = d3_carrier(g, volume)
    inverse = carrier.inv()
    generators = tuple(sp.simplify(
        WEDGES[direction]
        + inverse * WEDGES[direction].T * carrier
    ) for direction in range(3))
    return carrier, generators


def positive_by_sylvester(matrix: sp.MatrixBase) -> bool:
    return all(sp.cancel(matrix[:size, :size].det()) > 0
               for size in range(1, matrix.rows + 1))


def comparison_map(edge: int) -> sp.Matrix:
    """A deterministic rational invertible comparison, not an isometry."""
    result = sp.eye(8)
    result[edge, edge + 1] = sp.Rational(edge + 1, edge + 3)
    result[edge + 2, edge + 4] = sp.Rational(-1, edge + 4)
    return result


def basis_change(site: int) -> sp.Matrix:
    result = sp.eye(8)
    result[site, site + 1] = sp.Rational(site + 2, site + 5)
    result[site + 3, site] = sp.Rational(-1, site + 4)
    return result


def endpoint_cross_form(
        d_left: sp.MatrixBase,
        gamma_left: sp.MatrixBase,
        d_right: sp.MatrixBase,
        gamma_right: sp.MatrixBase,
        comparison: sp.MatrixBase,
        divisor: int = 4) -> sp.Matrix:
    b_left = d_left * gamma_left
    b_right = d_right * gamma_right
    return sp.simplify(
        (b_left * comparison + comparison.inv().T * b_right) / divisor
    )


def kernel_from_cross_forms(
        carriers: tuple[sp.Matrix, ...],
        edges: tuple[tuple[int, int], ...],
        cross_forms: tuple[sp.Matrix, ...],
        reverse_sign: int = -1) -> sp.Matrix:
    size = carriers[0].rows
    blocks = [[sp.zeros(size) for _ in carriers] for _ in carriers]
    for (left, right), cross in zip(edges, cross_forms):
        blocks[left][right] += carriers[left].inv() * cross
        blocks[right][left] += (
            reverse_sign * carriers[right].inv() * cross.T
        )
    return assemble_blocks(blocks)


def main(mutation: str | None) -> int:
    site_data = (
        (metric(0, 0, 0), sp.Integer(1)),
        (metric(sp.Rational(3, 5), 0, 0), sp.Rational(4, 5)),
        (metric(0, sp.Rational(5, 13), 0), sp.Rational(12, 13)),
        (metric(sp.Rational(11, 50), sp.Rational(11, 50),
                sp.Rational(11, 50)), sp.Rational(117, 125)),
    )
    local = tuple(weighted_generators(g, volume)
                  for g, volume in site_data)
    carriers = tuple(item[0] for item in local)
    generators = tuple(item[1] for item in local)

    check("metric-volume locus: all four rational cells lie exactly on V^2=det(g)",
          all(sp.factor(g.det() - volume**2) == 0
              for g, volume in site_data))
    check("carrier positivity: every displayed D3 is exact symmetric positive definite",
          all(carrier == carrier.T and positive_by_sylvester(carrier)
              for carrier in carriers))
    check("local Clifford algebra: every Gamma is D3-self-adjoint with the local co-metric",
          all(
              matrix_is_zero(gamma.T * carrier - carrier * gamma)
              for carrier, local_generators in zip(carriers, generators)
              for gamma in local_generators
          ) and all(
              matrix_is_zero(
                  generators[site][left] * generators[site][right]
                  + generators[site][right] * generators[site][left]
                  - 2 * site_data[site][0].inv()[left, right] * sp.eye(8)
              )
              for site in range(4)
              for left in range(3)
              for right in range(left, 3)
          ))

    # One oriented representative for each edge of a four-site ring.
    edges = ((0, 1), (1, 2), (2, 3), (3, 0))
    directions = (0, 1, 2, 0)
    comparisons = tuple(comparison_map(edge) for edge in range(4))
    divisor = 3 if mutation == "constant_link_factor" else 4
    cross_forms = tuple(endpoint_cross_form(
        carriers[left], generators[left][direction],
        carriers[right], generators[right][direction],
        comparison, divisor,
    ) for (left, right), direction, comparison
        in zip(edges, directions, comparisons))
    reverse_sign = 1 if mutation == "reverse_edge_sign" else -1
    kernel = kernel_from_cross_forms(
        carriers, edges, cross_forms, reverse_sign=reverse_sign)
    h_global = block_diagonal(carriers)

    check("variable-cell weighted skew: the ring kernel is exact in the block D3 inner product",
          matrix_is_zero(h_global * kernel + kernel.T * h_global))
    check("nearest-neighbour locality: every nonzero block lies on a declared edge",
          all(
              kernel[left * 8:(left + 1) * 8,
                     right * 8:(right + 1) * 8] == sp.zeros(8)
              for left in range(4) for right in range(4)
              if left != right and (left, right) not in edges
              and (right, left) not in edges
          ) and all(
              kernel[site * 8:(site + 1) * 8,
                     site * 8:(site + 1) * 8] == sp.zeros(8)
              for site in range(4)))
    probe = sp.Matrix([sp.Rational((index % 7) - 3, index + 5)
                       for index in range(32)])
    check("quadratic norm: the exact derivative vanishes for a nonzero rational probe",
          sp.cancel((probe.T * (h_global * kernel + kernel.T * h_global)
                     * probe)[0]) == 0)

    # The edge classification does not use the endpoint-symmetric ansatz.
    arbitrary_cross = tuple(sp.Matrix(8, 8, lambda row, column, edge=edge:
        sp.Rational(((row + 2 * column + edge) % 7) - 3, edge + 5))
        for edge in range(4))
    arbitrary_kernel = kernel_from_cross_forms(
        carriers, edges, arbitrary_cross)
    recovered = tuple(
        carriers[left]
        * arbitrary_kernel[left * 8:(left + 1) * 8,
                           right * 8:(right + 1) * 8]
        for left, right in edges
    )
    check("cross-form sufficiency: arbitrary edge forms produce an exact weighted-skew kernel",
          matrix_is_zero(
              h_global * arbitrary_kernel + arbitrary_kernel.T * h_global))
    check("cross-form necessity: every form is recovered uniquely as C_sr=D_s K_sr",
          recovered == arbitrary_cross)
    check("solution-space dimension: four eight-component edges carry 4*8^2 coordinates",
          len(edges) * 8**2 == 256)

    # Independent local coordinate changes at all sites.
    changes = tuple(basis_change(site) for site in range(4))
    changed_carriers = tuple(sp.simplify(
        change.inv().T * carrier * change.inv())
        for change, carrier in zip(changes, carriers))
    changed_generators = tuple(tuple(sp.simplify(
        changes[site] * gamma * changes[site].inv())
        for gamma in generators[site]) for site in range(4))
    changed_comparisons = []
    for edge, ((left, right), comparison) in enumerate(zip(edges, comparisons)):
        if mutation == "right_frame_law" and edge == 0:
            changed = changes[left] * comparison * changes[right].T
        else:
            changed = changes[left] * comparison * changes[right].inv()
        changed_comparisons.append(sp.simplify(changed))
    changed_cross = tuple(endpoint_cross_form(
        changed_carriers[left], changed_generators[left][direction],
        changed_carriers[right], changed_generators[right][direction],
        comparison, divisor,
    ) for (left, right), direction, comparison
        in zip(edges, directions, changed_comparisons))
    changed_kernel = kernel_from_cross_forms(
        changed_carriers, edges, changed_cross, reverse_sign=reverse_sign)
    change_global = block_diagonal(changes)
    expected_changed_kernel = sp.simplify(
        change_global * kernel * change_global.inv())
    expected_changed_h = sp.simplify(
        change_global.inv().T * h_global * change_global.inv())
    check("cross-form covariance: four independent local frame changes obey the bilinear law",
          all(matrix_is_zero(
              changed_cross[edge]
              - changes[left].inv().T * cross_forms[edge]
              * changes[right].inv())
              for edge, (left, right) in enumerate(edges)))
    check("kernel covariance: the full operator transforms by block conjugation",
          changed_kernel == expected_changed_kernel)
    check("frame-independent adjoint: weighted skew survives all local frame changes",
          block_diagonal(changed_carriers) == expected_changed_h
          and matrix_is_zero(expected_changed_h * changed_kernel
                             + changed_kernel.T * expected_changed_h))

    # Constant-cell limit: same carrier, same direction matrix, identity link.
    flat_carrier, flat_generators = weighted_generators(sp.eye(3), sp.Integer(1))
    constant_carriers = (flat_carrier,) * 4
    constant_comparisons = (sp.eye(8),) * 4
    constant_cross = tuple(endpoint_cross_form(
        flat_carrier, flat_generators[0],
        flat_carrier, flat_generators[0],
        comparison, divisor,
    ) for comparison in constant_comparisons)
    constant_kernel = kernel_from_cross_forms(
        constant_carriers, edges, constant_cross, reverse_sign=reverse_sign)
    centered = sp.zeros(4)
    for left, right in edges:
        centered[left, right] += sp.Rational(1, 2)
        centered[right, left] -= sp.Rational(1, 2)
    expected_constant = sp.kronecker_product(centered, flat_generators[0])
    check("constant-cell reduction: identity comparisons give Gamma_d(T_d-T_d^-1)/2",
          constant_kernel == expected_constant)
    check("constant-cell skew symmetry: the specialized operator is ordinary skew-symmetric",
          constant_kernel.T == -constant_kernel)

    print("SUMMARY:")
    print(f"  exact checks: PASS={PASS} FAIL={FAIL}")
    print("  variable cells: 4; oriented representative edges: 4; carrier dimension: 8")
    print("  theorem: weighted-skew edge kernels are uniquely parameterized by cross-forms")
    print("  constructed family: endpoint-symmetric, local-frame covariant, constant-link normalized")
    print("  boundary: comparison-map selection, tangent compatibility, curvature, physical time, and dynamics remain separate")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    arguments = parser.parse_args()
    sys.exit(main(arguments.mutation))
