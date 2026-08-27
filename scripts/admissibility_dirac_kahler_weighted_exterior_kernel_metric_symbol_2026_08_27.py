#!/usr/bin/env python3
"""Block 214: a metric-weighted exterior kernel and its exact symbol.

This runner asks the next constructive question after the finite D3 geometry:
does the canonical exterior differential, paired with its adjoint under

    D3(g,V) = diag(V, V g^-1, E g E / V, 1/V),

produce a nearest-neighbour kernel whose square is the co-metric quadratic
form?  It does exactly on the metric-volume locus V^2 = det(g).  Off that
locus the middle-degree adjoint carries the exact mismatch det(g)/V^2.

All identities are exact over rational functions or exact rational witnesses.
The result is a conditional finite Kähler-Dirac construction.  It does not
select D3 from the framework axioms, identify physical time, perform a Wick
rotation, supply dynamics or gravity, or take a continuum limit.
"""

from __future__ import annotations

import itertools
import sys
from collections import Counter

import sympy as sp


AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_WEIGHTED_EXTERIOR_KERNEL_METRIC_SYMBOL_BOUNDED_THEOREM_NOTE_2026-08-27.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_THREE_DIRECTION_RULE_GEOMETRY_BOUNDED_THEOREM_NOTE_2026-08-26.md",
    "scripts/admissibility_dirac_kahler_three_direction_rule_geometry_2026_08_26.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_COVARIANT_RULE_IDENTIFICATION_BOUNDED_THEOREM_NOTE_2026-08-26.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    ".claude/science/physics-loops/CAMPAIGN_20260824_GRAVITY_MAINLINE.md",
)

STACK_PARENT = "4e9931a970ded94f769553da9e6d77770d612f64"
SCIENTIFIC_PARENT = "Block 209 three-direction rule geometry"
CURRENT_MAIN_AT_START = "66e478505e055faf4a5b9e6f4883211e44304718"

PASS = 0
FAIL = 0


def check(name: str, condition: object) -> None:
    global PASS, FAIL
    ok = bool(condition)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}", flush=True)
    PASS += int(ok)
    FAIL += int(not ok)


def kron(left: sp.MatrixBase, right: sp.MatrixBase) -> sp.Matrix:
    return sp.Matrix(sp.kronecker_product(left, right))


# Exterior basis: dt^t dx^x dy^y at corner index 4t+2x+y.
CORNERS = tuple(itertools.product((0, 1), repeat=3))
INDEX = {corner: 4 * corner[0] + 2 * corner[1] + corner[2]
         for corner in CORNERS}
DEGREE = tuple(sum(corner) for corner in CORNERS)
ONE = (INDEX[(1, 0, 0)], INDEX[(0, 1, 0)], INDEX[(0, 0, 1)])
TWO = (INDEX[(0, 1, 1)], INDEX[(1, 0, 1)], INDEX[(1, 1, 0)])
WEDGE_SIGNATURE = sp.diag(1, -1, 1)


def wedge(direction: int) -> sp.Matrix:
    """Left exterior multiplication by dt, dx, or dy."""
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
CONTRACTIONS = tuple(operator.T for operator in WEDGES)


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


def weighted_generators(g: sp.MatrixBase, volume: sp.Expr) -> tuple:
    """Gamma_d = epsilon_d + epsilon_d^dagger in the D3 inner product."""
    carrier = d3_carrier(g, volume)
    carrier_inverse = sp.simplify(carrier.inv())
    adjoints = tuple(sp.simplify(
        carrier_inverse * operator.T * carrier) for operator in WEDGES)
    generators = tuple(sp.simplify(WEDGES[d] + adjoints[d])
                       for d in range(3))
    return carrier, adjoints, generators


def matrix_is_zero(matrix: sp.MatrixBase) -> bool:
    return all(sp.cancel(entry) == 0 for entry in matrix)


def vanishes_mod_volume(matrix: sp.MatrixBase, volume: sp.Symbol,
                        determinant: sp.Expr) -> bool:
    """Test a rational matrix on the algebraic locus volume^2=determinant."""
    modulus = sp.Poly(volume**2 - determinant, volume)
    for entry in matrix:
        numerator = sp.together(entry).as_numer_denom()[0]
        if numerator == 0:
            continue
        remainder = sp.rem(sp.Poly(numerator, volume), modulus)
        if sp.expand(remainder.as_expr()) != 0:
            return False
    return True


def degree_block(matrix: sp.MatrixBase, target_degree: int,
                 source_degree: int) -> sp.Matrix:
    rows = [i for i, degree in enumerate(DEGREE) if degree == target_degree]
    columns = [i for i, degree in enumerate(DEGREE) if degree == source_degree]
    return matrix.extract(rows, columns)


def symbol(generators: tuple, q: tuple) -> sp.Matrix:
    return sum((q[d] * generators[d] for d in range(3)), sp.zeros(8))


def momentum_histogram(extents: tuple, inverse: sp.MatrixBase) -> Counter:
    values = Counter()
    for mode in itertools.product(*(range(extent) for extent in extents)):
        q = sp.Matrix([
            sp.sin(2 * sp.pi * n / extent)
            for n, extent in zip(mode, extents)
        ])
        if len(extents) == 2:
            q = sp.Matrix([q[0], q[1], 0])
        value = sp.cancel((q.T * inverse * q)[0])
        values[value] += 1
    return values


def omega4(site: tuple, generators: tuple) -> sp.Matrix:
    result = sp.eye(4)
    for direction, coordinate in enumerate(site):
        if coordinate % 2:
            result = result * generators[direction]
    return sp.Matrix(result)


def main() -> int:
    shear_tx, shear_ty, shear_xy = sp.symbols("c_tx c_ty c_xy")
    volume = sp.Symbol("V", positive=True)
    g = metric(shear_tx, shear_ty, shear_xy)
    determinant = sp.factor(g.det())
    inverse = sp.simplify(g.inv())
    carrier, adjoints, generators = weighted_generators(g, volume)

    # A. Exterior algebra and the declared D3 carrier.
    nilpotent = all(matrix_is_zero(operator * operator)
                    for operator in WEDGES)
    exterior_anticommutation = all(matrix_is_zero(
        WEDGES[left] * WEDGES[right]
        + WEDGES[right] * WEDGES[left])
        for left in range(3) for right in range(left + 1, 3))
    check("A1 exterior creation operators are nilpotent and anticommute",
          nilpotent and exterior_anticommutation)
    expected_two = WEDGE_SIGNATURE * g * WEDGE_SIGNATURE / volume
    check("A2 D3 has blocks (V, V g^-1, E g E/V, 1/V) in the declared basis",
          carrier[0, 0] == volume
          and carrier[7, 7] == 1 / volume
          and carrier.extract(ONE, ONE) == volume * inverse
          and carrier.extract(TWO, TWO) == expected_two
          and carrier == carrier.T)

    # B. Locate exactly where the volume enters the exterior adjoint.
    rho = sp.cancel(determinant / volume**2)
    adjoint_pattern = True
    for direction in range(3):
        canonical = sum(
            (inverse[direction, other] * CONTRACTIONS[other]
             for other in range(3)), sp.zeros(8))
        adjoint_pattern = adjoint_pattern and matrix_is_zero(
            degree_block(adjoints[direction] - canonical, 0, 1))
        adjoint_pattern = adjoint_pattern and matrix_is_zero(
            degree_block(adjoints[direction] - rho * canonical, 1, 2))
        adjoint_pattern = adjoint_pattern and matrix_is_zero(
            degree_block(adjoints[direction] - canonical, 2, 3))
    check("B1 D3-adjoint equals metric contraction except for det(g)/V^2 on degree 2->1",
          adjoint_pattern)
    check("B2 every weighted Gamma_d is exactly self-adjoint in the D3 inner product",
          all(matrix_is_zero(generator.T * carrier - carrier * generator)
              for generator in generators))

    # C. Generalized Clifford closure and the volume selector.
    clifford_residuals = []
    for left in range(3):
        for right in range(left, 3):
            anticommutator = (
                generators[left] * generators[right]
                + generators[right] * generators[left]
            )
            clifford_residuals.append(sp.simplify(
                anticommutator - 2 * inverse[left, right] * sp.eye(8)))
    check("C1 all six generalized-Clifford residuals vanish on V^2=det(g)",
          all(vanishes_mod_volume(residual, volume, determinant)
              for residual in clifford_residuals))
    diagonal_trace_formula = all(sp.cancel(
        sp.trace(generators[direction] * generators[direction]
                 - inverse[direction, direction] * sp.eye(8))
        - 4 * (rho - 1) * inverse[direction, direction]) == 0
        for direction in range(3))
    check("C2 the exact closure defect trace is 4(det(g)/V^2-1)(g^-1)_dd",
          diagonal_trace_formula)
    # For a positive-definite g, every diagonal of g^-1 is positive.  Thus C2
    # makes V^2=det(g) necessary, while C1 makes it sufficient.
    check("C3 positive-metric full-carrier closure selects V^2=det(g), not an arbitrary V",
          diagonal_trace_formula
          and sp.factor(determinant - volume**2) != 0)

    q_t, q_x, q_y = sp.symbols("q_t q_x q_y")
    q = (q_t, q_x, q_y)
    weighted_symbol = symbol(generators, q)
    quadratic = sp.cancel((sp.Matrix(q).T * inverse * sp.Matrix(q))[0])
    symbol_residual = sp.simplify(weighted_symbol * weighted_symbol
                                  - quadratic * sp.eye(8))
    check("C4 Gamma(q)^2 = q^T g^-1 q on the selected metric-volume locus",
          vanishes_mod_volume(symbol_residual, volume, determinant))

    # D. The flat carrier is exactly two copies of Block 209's Cl(3,0) rule.
    sigma_x = sp.Matrix([[0, 1], [1, 0]])
    sigma_z = sp.diag(1, -1)
    identity_2 = sp.eye(2)
    rule_generators = (
        kron(sigma_x, identity_2),
        kron(sigma_z, sigma_x),
        kron(sigma_z, sigma_z),
    )
    doubled_rule = tuple(sp.diag(generator, generator)
                         for generator in rule_generators)
    flat_carrier, _, flat_generators = weighted_generators(sp.eye(3), sp.Integer(1))
    intertwiner = sp.Matrix([
        [-1,  1, -1,  1,  1, -1, -1,  1],
        [-1, -1,  1,  1,  1,  1,  1,  1],
        [ 1, -1, -1,  1, -1,  1, -1,  1],
        [-1, -1, -1, -1,  1,  1, -1, -1],
        [-1,  1, -1,  1, -1,  1,  1, -1],
        [ 1,  1, -1, -1,  1,  1,  1,  1],
        [-1,  1,  1, -1, -1,  1, -1,  1],
        [-1, -1, -1, -1, -1, -1,  1,  1],
    ])
    check("D1 at g=I,V=1 the carrier is I8 and the exact intertwiner is orthogonal up to 8",
          flat_carrier == sp.eye(8)
          and intertwiner.T * intertwiner == 8 * sp.eye(8)
          and intertwiner.det() == 4096)
    check("D2 the flat exterior generators intertwine with two copies of Block 209's generators",
          all(flat_generators[d] * intertwiner
              == intertwiner * doubled_rule[d] for d in range(3)))
    scalarization = True
    for site in CORNERS:
        omega_left = (intertwiner
                      * sp.diag(omega4(site, rule_generators),
                                omega4(site, rule_generators))
                      * intertwiner.T / 8)
        for direction in range(3):
            neighbour = list(site)
            neighbour[direction] += 1
            neighbour = tuple(neighbour)
            omega_right = (intertwiner
                           * sp.diag(omega4(neighbour, rule_generators),
                                     omega4(neighbour, rule_generators))
                           * intertwiner.T / 8)
            eta = sp.Integer(-1) ** sum(site[:direction])
            link = sp.simplify(
                omega_left.T * (flat_generators[direction] / 2) * omega_right)
            scalarization = scalarization and link == eta * sp.eye(8) / 2
    check("D3 the transported flat staggering scalarizes every corner link to eta_d I8/2",
          scalarization)

    # E. Exact finite-momentum checks, including the landed two-dimensional window.
    flat_2d = momentum_histogram((4, 4), sp.eye(3))
    flat_3d = momentum_histogram((4, 4, 4), sp.eye(3))
    check("E1 flat exact momentum histograms reproduce sum sin^2(k_d)",
          flat_2d == Counter({0: 4, 1: 8, 2: 4})
          and flat_3d == Counter({0: 8, 1: 24, 2: 24, 3: 8}))

    shear_2d = sp.Rational(3, 5)
    volume_2d = sp.Rational(4, 5)
    g_2d_window = metric(shear_2d, 0, 0)
    carrier_2d, _, generators_2d = weighted_generators(g_2d_window, volume_2d)
    plane_indices = (INDEX[(0, 0, 0)], INDEX[(0, 1, 0)],
                     INDEX[(1, 0, 0)], INDEX[(1, 1, 0)])
    g2 = sp.Matrix([[1, shear_2d], [shear_2d, 1]])
    landed_2d = sp.diag(volume_2d, volume_2d * g2.inv(), 1 / volume_2d)
    q2 = (q_t, q_x, sp.Integer(0))
    quadratic_2d = sp.cancel(
        (sp.Matrix(q2).T * g_2d_window.inv() * sp.Matrix(q2))[0])
    check("E2 c=3/5,V=4/5 is an exact metric-volume point and D3 restricts to the landed 2D Hodge form",
          sp.factor(g_2d_window.det() - volume_2d**2) == 0
          and carrier_2d.extract(plane_indices, plane_indices) == landed_2d)
    plane_symbol = symbol(generators_2d, q2)
    check("E3 the landed 2D window squares to (q_t^2-2c q_t q_x+q_x^2)/(1-c^2)",
          matrix_is_zero(plane_symbol * plane_symbol
                         - quadratic_2d * sp.eye(8))
          and sp.cancel(quadratic_2d
                        - (q_t**2 - 2 * shear_2d * q_t * q_x + q_x**2)
                        / (1 - shear_2d**2)) == 0)

    # F. A genuinely three-direction rational witness with exact volume.
    witness_shear = sp.Rational(11, 50)
    witness_volume = sp.Rational(117, 125)
    witness_metric = metric(witness_shear, witness_shear, witness_shear)
    witness_inverse = witness_metric.inv()
    witness_carrier, _, witness_generators = weighted_generators(
        witness_metric, witness_volume)
    witness_minors = tuple(sp.factor(
        witness_carrier[:size, :size].det()) for size in range(1, 9))
    check("F1 the all-shear rational witness has det(g)=V^2 and positive D3",
          sp.factor(witness_metric.det() - witness_volume**2) == 0
          and all(minor > 0 for minor in witness_minors))
    expected_inverse = sp.Matrix([
        [sp.Rational(1525, 1404), sp.Rational(-275, 1404), sp.Rational(-275, 1404)],
        [sp.Rational(-275, 1404), sp.Rational(1525, 1404), sp.Rational(-275, 1404)],
        [sp.Rational(-275, 1404), sp.Rational(-275, 1404), sp.Rational(1525, 1404)],
    ])
    witness_clifford = all(matrix_is_zero(
        witness_generators[left] * witness_generators[right]
        + witness_generators[right] * witness_generators[left]
        - 2 * witness_inverse[left, right] * sp.eye(8))
        for left in range(3) for right in range(left, 3))
    check("F2 the rational witness has exact off-diagonal co-metric mixing and closes the generalized Clifford algebra",
          witness_inverse == expected_inverse
          and all(witness_inverse[i, j] != 0
                  for i in range(3) for j in range(3) if i != j)
          and witness_clifford)
    witness_histogram = momentum_histogram((4, 4, 4), witness_inverse)
    expected_histogram = Counter({
        sp.Integer(0): 8,
        sp.Rational(1525, 1404): 24,
        sp.Rational(625, 351): 12,
        sp.Rational(25, 12): 2,
        sp.Rational(100, 39): 12,
        sp.Rational(5125, 1404): 6,
    })
    check("F3 all 64 exact 4^3 momenta give the six predicted mixed-metric values",
          witness_histogram == expected_histogram)

    # G. Design boundary: scalar eta weights alone cannot carry shear.
    diagonal_weights = sp.symbols("w_t w_x w_y")
    scalar_eta_quadratic = sum(
        diagonal_weights[d]**2 * q[d]**2 for d in range(3))
    mixed_metric_quadratic = sp.cancel(
        (sp.Matrix(q).T * witness_inverse * sp.Matrix(q))[0])
    mixed_scalar = sp.diff(scalar_eta_quadratic, q_t, q_x)
    mixed_metric = sp.diff(mixed_metric_quadratic, q_t, q_x)
    check("G1 scalar axis-weighted eta links have zero mixed coefficient, while the sheared metric requires one",
          mixed_scalar == 0
          and mixed_metric == 2 * witness_inverse[0, 1]
          and mixed_metric != 0)

    print("MEASURED", flush=True)
    print(f"  stack parent: {STACK_PARENT}", flush=True)
    print(f"  scientific parent: {SCIENTIFIC_PARENT}", flush=True)
    print(f"  main at campaign start: {CURRENT_MAIN_AT_START}", flush=True)
    print(f"  det(g): {determinant}", flush=True)
    print("  selected normalization: V^2 = det(g)", flush=True)
    print("  weighted symbol: Gamma(q)^2 = q^T g^-1 q I8", flush=True)
    print(f"  rational 3D witness: c=11/50, V=117/125, histogram={dict(witness_histogram)}",
          flush=True)
    print("  scope: finite exact conditional D3/exterior construction; no physical time, Lorentzian cone, dynamics, gravity, or continuum limit", flush=True)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}", flush=True)
    return 1 if FAIL else 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except SystemExit:
        raise
    except Exception as error:
        print(f"[FAIL] INTERNAL-EXCEPTION: {type(error).__name__}: {error}",
              flush=True)
        print("TOTAL: PASS=0 FAIL=1", flush=True)
        raise
