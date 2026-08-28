#!/usr/bin/env python3
"""Exact exterior-character action, variation, and transfer checks.

The finite action family is built from the plaquette-holonomy parent's defect. This
runner checks the O(3) character classification, the ordered link variation,
the flat curl Hessian, coframe independence, topology controls, positive and
negative transfer signs, and an independently implemented reconstruction.
The finite transfer matrices below are exact controls; the all-O(3),
all-irrep reflection and spectral statements remain load-bearing proofs in the
paired source note.  No floating-point value is converted into exact data.
"""

from __future__ import annotations

import argparse
import itertools

import sympy as sp

from admissibility_dirac_kahler_exterior_character_action_transfer_independent_2026_08_28 import (
    independent_facts,
)


AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_EXTERIOR_CHARACTER_ACTION_TRANSFER_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_PLAQUETTE_HOLONOMY_CONNECTION_CURVATURE_BOUNDED_THEOREM_NOTE_2026-08-27.md",
    "scripts/admissibility_dirac_kahler_plaquette_holonomy_connection_curvature_2026_08_27.py",
    "scripts/admissibility_dirac_kahler_exterior_character_action_transfer_independent_2026_08_28.py",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
)

MUTATIONS = (
    "drop_top_exterior_degree",
    "reverse_staple_order",
    "extend_so3_formula_to_improper",
    "negative_temporal_sign",
    "zero_coupling_injective",
    "break_closed_density_cocycle",
    "break_nonlinear_flat_slope",
    "erase_torus_null_modes",
    "break_improper_zero_force",
    "erase_finite_curvature_nonselection",
)

PASS = 0
FAIL = 0


def check(name: str, condition: object) -> None:
    global PASS, FAIL
    ok = bool(condition)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    PASS += int(ok)
    FAIL += int(not ok)


def matrix_is_zero(matrix: sp.MatrixBase) -> bool:
    return all(sp.simplify(entry) == 0 for entry in matrix)


CORNERS = tuple(itertools.product((0, 1), repeat=3))
INDEX = {corner: 4 * corner[0] + 2 * corner[1] + corner[2]
         for corner in CORNERS}
ONE = (INDEX[(1, 0, 0)], INDEX[(0, 1, 0)], INDEX[(0, 0, 1)])
TWO = (INDEX[(0, 1, 1)], INDEX[(1, 0, 1)], INDEX[(1, 1, 0)])
WEDGE_SIGNATURE = sp.diag(1, -1, 1)


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
    return sp.Matrix(lift)


def d3_carrier(metric: sp.MatrixBase, volume: sp.Expr) -> sp.Matrix:
    inverse = sp.simplify(metric.inv())
    carrier = sp.zeros(8)
    carrier[0, 0] = volume
    carrier[7, 7] = 1 / volume
    for row in range(3):
        for column in range(3):
            carrier[ONE[row], ONE[column]] = volume * inverse[row, column]
            carrier[TWO[row], TWO[column]] = (
                WEDGE_SIGNATURE * metric * WEDGE_SIGNATURE / volume
            )[row, column]
    return sp.Matrix(carrier)


def plaquette_defect(holonomy: sp.MatrixBase,
                     carrier: sp.MatrixBase) -> sp.Expr:
    delta = holonomy - sp.eye(holonomy.rows)
    return sp.simplify(sp.trace(
        carrier.inv() * delta.T * carrier * delta
    ))


def rotation_x(cosine: sp.Expr, sine: sp.Expr) -> sp.Matrix:
    return sp.Matrix(((1, 0, 0),
                      (0, cosine, -sine),
                      (0, sine, cosine)))


def rotation_y(cosine: sp.Expr, sine: sp.Expr) -> sp.Matrix:
    return sp.Matrix(((cosine, 0, sine),
                      (0, 1, 0),
                      (-sine, 0, cosine)))


def rotation_z(cosine: sp.Expr, sine: sp.Expr) -> sp.Matrix:
    return sp.Matrix(((cosine, -sine, 0),
                      (sine, cosine, 0),
                      (0, 0, 1)))


def exterior_character(matrix: sp.MatrixBase,
                       mutation: str | None = None) -> sp.Expr:
    lift = exterior_lift(matrix)
    if mutation == "drop_top_exterior_degree":
        return sp.expand(sp.trace(lift) - matrix.det())
    return sp.expand(sp.trace(lift))


def q_defect(matrix: sp.MatrixBase) -> sp.Expr:
    return sp.simplify(
        16 - exterior_character(matrix) - exterior_character(matrix.inv())
    )


def main(mutation: str | None, mode: str) -> int:
    global PASS, FAIL
    PASS = 0
    FAIL = 0

    if mode == "independent":
        for name, condition in independent_facts().items():
            check(f"independent: {name}", condition)
        print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
        return int(FAIL != 0)

    symbols = sp.symbols("m00:03 m10:13 m20:23")
    generic = sp.Matrix(3, 3, symbols)
    check("exterior character: Tr Lambda(M)=det(I+M) as a generic polynomial",
          sp.expand(exterior_character(generic, mutation)
                    - (sp.eye(3) + generic).det()) == 0)

    proper = rotation_z(sp.Rational(3, 5), sp.Rational(4, 5))
    pi_rotation = sp.diag(-1, -1, 1)
    improper_one = sp.diag(1, 1, -1) * proper
    improper_two = sp.diag(-1, 1, 1)
    check("O(3) sectors: SO(3) is Wilson-type while every tested improper holonomy has Q=16",
          q_defect(proper) == 4 * (3 - sp.trace(proper))
          and q_defect(proper) == sp.Rational(16, 5)
          and q_defect(improper_one) == 16
          and q_defect(improper_two) == 16)

    improper_formula = (q_defect(improper_two) if
                        mutation != "extend_so3_formula_to_improper"
                        else 4 * (3 - sp.trace(improper_two)))
    check("improper boundary: the SO(3) trace formula is not extended across det(W)=-1",
          improper_formula == 16)
    tangent = sp.symbols("tangent", real=True)
    improper_path = (
        sp.diag(1, 1, -1)
        * rotation_z(sp.cos(tangent), sp.sin(tangent))
    )
    improper_path_q = q_defect(improper_path)
    if mutation == "break_improper_zero_force":
        improper_path_q = 4 * (3 - sp.trace(improper_path))
    check("improper force boundary: Q is constant with zero first and second tangent derivatives",
          sp.simplify(improper_path_q - 16) == 0
          and sp.diff(improper_path_q, tangent) == 0
          and sp.diff(improper_path_q, tangent, 2) == 0)
    check("maximum defect is not a determinant classifier: a proper pi rotation also has Q=16",
          pi_rotation.det() == 1 and q_defect(pi_rotation) == 16)
    check("orientation: Q(W^-1)=Q(W) on proper and improper representatives",
          q_defect(proper.inv()) == q_defect(proper)
          and q_defect(improper_one.inv()) == q_defect(improper_one))

    # Exact ordered first variation for left link variation R(t)=exp(tX)R.
    left = rotation_z(sp.Rational(5, 13), sp.Rational(12, 13))
    link = rotation_x(sp.Rational(7, 25), sp.Rational(24, 25))
    right = rotation_y(sp.Rational(3, 5), sp.Rational(4, 5))
    generator = sp.Matrix(((0, -1, 0), (1, 0, 0), (0, 0, 0)))
    direct_forward = sp.trace(left * generator * link * right)
    forward_staple = link * right * left
    direct_inverse = -sp.trace(left * link.inv() * generator * right)
    inverse_staple = right * left * link.inv()
    if mutation == "reverse_staple_order":
        forward_staple = left * right * link
    check("local variation: forward and inverse occurrences retain cyclic order and orientation sign",
          sp.simplify(direct_forward
                      - sp.trace(forward_staple * generator)) == 0
          and sp.simplify(direct_inverse
                          + sp.trace(inverse_staple * generator)) == 0)

    # Open-square curl complex: d1 d0=0 and positive Hessian kernel is gauge.
    d_zero = sp.Matrix(((-1, 1, 0, 0),
                        (0, -1, 1, 0),
                        (0, 0, 1, -1),
                        (-1, 0, 0, 1)))
    d_one = sp.Matrix(((1, 1, -1, -1),))
    hessian = 8 * d_one.T * d_one
    check("flat Hessian: H=8 d1^T K d1 and all linearized gauge gradients are null",
          d_one * d_zero == sp.zeros(1, 4)
          and hessian * d_zero == sp.zeros(4, 4)
          and hessian.rank() == 1)

    # Minimal cell structure for T^2: one vertex, two loop edges, one
    # commutator plaquette.  Its linearized boundary is exactly zero.
    torus_d_one = sp.zeros(1, 2)
    torus_hessian = 8 * torus_d_one.T * torus_d_one
    torus_nullity = (0 if mutation == "erase_torus_null_modes"
                     else 2 - torus_hessian.rank())
    check("topology: a torus cell has exact closed non-gauge flat Hessian directions",
          torus_nullity == 2)

    # Endpoint coframes telescope from the compatible parent defect.
    frames = (
        sp.eye(3),
        sp.Matrix(((sp.Rational(5, 4), sp.Rational(-3, 4), 0),
                   (0, 1, 0), (0, 0, 1))),
    )
    metric_defects = []
    for number, frame in enumerate(frames):
        metric = sp.simplify((frame.T * frame).inv())
        volume = sp.simplify(1 / frame.det())
        carrier = d3_carrier(metric, volume)
        holonomy = exterior_lift(sp.simplify(frame.inv() * proper * frame))
        if mutation == "break_closed_density_cocycle" and number == 1:
            holonomy = 2 * holonomy
        metric_defects.append(plaquette_defect(holonomy, carrier))
    frame_scale = sp.symbols("frame_scale", positive=True)
    varying_frame = sp.diag(frame_scale, 1, 1)
    varying_metric = sp.simplify((varying_frame.T * varying_frame).inv())
    varying_volume = sp.simplify(1 / varying_frame.det())
    varying_holonomy = exterior_lift(sp.simplify(
        varying_frame.inv() * proper * varying_frame
    ))
    varying_defect = sp.factor(plaquette_defect(
        varying_holonomy,
        d3_carrier(varying_metric, varying_volume),
    ))
    check("coframe response: fixed supplied R gives the same exact Q for unequal endpoint metrics",
          metric_defects == [sp.Rational(16, 5), sp.Rational(16, 5)]
          and varying_defect == sp.Rational(16, 5)
          and sp.diff(varying_defect, frame_scale) == 0
          and sp.diff(varying_defect, frame_scale, 2) == 0)

    # f_n(q)=2(8^n-(8-q/2)^n)/(n 8^(n-1)).  n=1 is Q and n=2 is nonlinear.
    q = sp.symbols("q", real=True)
    f_one = q
    f_two = q - q**2 / 32
    slope_two = sp.diff(f_two, q).subs(q, 0)
    if mutation == "break_nonlinear_flat_slope":
        f_two = 2 * f_two
        slope_two = sp.diff(f_two, q).subs(q, 0)
    check("nonselection witness: f1 and nonlinear f2 share f(0)=0 and unit flat slope",
          f_one.subs(q, 0) == f_two.subs(q, 0) == 0
          and slope_two == 1
          and sp.expand(f_two - f_one) != 0)
    check("nonlinear witness: f2 is nonnegative on Q in [0,16] with the same unique minimum",
          f_two.subs(q, 16) > 0
          and sp.diff(f_two, q).subs(q, 0) > 0
          and sp.solve(sp.diff(f_two, q), q) == [16])
    # Two same-axis plaquette gradients cancel for f1 but not for f2.  The
    # second angle is pi+theta, so its skew part has the opposite sign while
    # its Q value is different.
    stationary_one = rotation_z(sp.Rational(3, 5), sp.Rational(4, 5))
    stationary_two = rotation_z(sp.Rational(-3, 5), sp.Rational(-4, 5))
    skew = lambda matrix: sp.simplify((matrix - matrix.T) / 2)
    linear_stationarity = sp.simplify(
        skew(stationary_one) + skew(stationary_two)
    )
    stationary_q_one = q_defect(stationary_one)
    stationary_q_two = q_defect(stationary_two)
    if mutation == "erase_finite_curvature_nonselection":
        nonlinear_stationarity = linear_stationarity
    else:
        nonlinear_stationarity = sp.simplify(
            (1 - stationary_q_one / 16) * skew(stationary_one)
            + (1 - stationary_q_two / 16) * skew(stationary_two)
        )
    expected_nonlinear_residual = sp.Rational(12, 25) * generator
    check("finite-curvature nonselection: f1 stationarity can fail for f2 despite the shared flat Hessian",
          stationary_q_one == sp.Rational(16, 5)
          and stationary_q_two == sp.Rational(64, 5)
          and matrix_is_zero(linear_stationarity)
          and nonlinear_stationarity == expected_nonlinear_residual)

    # Positive-type mechanism: chi(g_i g_j^-1) is an exact Gram matrix for
    # vectorized exterior representation matrices; Schur powers remain Gram.
    samples = (sp.eye(3), proper,
               rotation_x(sp.Rational(5, 13), sp.Rational(12, 13)),
               improper_two)
    features = sp.Matrix([
        list(exterior_lift(sample)) for sample in samples
    ])
    character_gram = features * features.T
    expected_gram = sp.Matrix([
        [exterior_character(left_sample * right_sample.T)
         for right_sample in samples]
        for left_sample in samples
    ])
    squared_features = sp.Matrix([
        list(sp.kronecker_product(features[row, :], features[row, :]))
        for row in range(features.rows)
    ])
    check("positive character mechanism: character and its square are exact representation Grams",
          character_gram == expected_gram
          and character_gram.multiply_elementwise(character_gram)
          == squared_features * squared_features.T)

    # Exact Z2 restriction of the crossing kernel.  For kappa=log(2)/16,
    # exp(-16*kappa)=1/2.  The opposite sign produces the exact value 2.
    positive_transfer = sp.Matrix(((1, sp.Rational(1, 2)),
                                   (sp.Rational(1, 2), 1)))
    tested_transfer = (sp.Matrix(((1, 2), (2, 1)))
                       if mutation == "negative_temporal_sign"
                       else positive_transfer)
    check("OS sign: nonnegative temporal coupling gives a positive injective local seam kernel",
          tested_transfer.is_positive_definite and tested_transfer.det() > 0)

    negative_transfer = sp.Matrix(((1, 2), (2, 1)))
    check("negative-sign falsifier: the exact two-history Gram has eigenvalues 3 and -1",
          negative_transfer.eigenvals() == {sp.Integer(3): 1,
                                           sp.Integer(-1): 1})

    zero_transfer = sp.ones(2)
    zero_rank = (2 if mutation == "zero_coupling_injective"
                 else zero_transfer.rank())
    check("zero-coupling boundary: the nontrivial two-history transfer is rank one, not injective",
          zero_rank == 1 and zero_transfer.det() == 0)

    # Haar integration of temporal vertex links contributes a gauge projector.
    gauge_projector = sp.Rational(1, 2) * sp.ones(2)
    projected_transfer = gauge_projector * positive_transfer
    physical_vector = sp.Matrix((1, 1))
    check("gauge projection: full kinematic transfer has a projector kernel but is positive on its image",
          projected_transfer.rank() == 1
          and projected_transfer * sp.Matrix((1, -1)) == sp.zeros(2, 1)
          and (physical_vector.T * projected_transfer * physical_vector)[0] > 0)

    normalized_transfer = sp.Rational(2, 3) * positive_transfer
    check("transfer logarithm: normalized exact spectrum gives Hamiltonian levels 0 and log(3)",
          normalized_transfer.eigenvals() == {sp.Integer(1): 1,
                                              sp.Rational(1, 3): 1})

    independent = independent_facts()
    check("independent checker: separate principal-minor, derivative, and transfer paths all agree",
          all(independent.values()))

    print("per_element: exact O(3) character sectors, link occurrences, and two-history seam signs were checked.")
    print("per_site: endpoint coframe independence and local gauge-projector action were checked exactly.")
    print("per_mode: flat gauge and torus null modes plus transfer eigenmodes were checked exactly.")
    print("per_block: the supplied finite plaquette action, Hessian, OS kernel, and logarithm were checked.")
    print("lattice_wide: checked finite-cell topology boundaries; no continuum, Lorentz, or gravity claim was executed.")
    print("scope_note: finite matrices are hostile controls only; the all-O(3) reflected-Gram and spectral-domain proofs are source-load-bearing.")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return int(FAIL != 0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    parser.add_argument("--mode", choices=("normal", "independent"),
                        default="normal")
    arguments = parser.parse_args()
    raise SystemExit(main(arguments.mutation, arguments.mode))
