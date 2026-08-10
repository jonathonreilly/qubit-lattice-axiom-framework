#!/usr/bin/env python3
"""Check sourced continuation and constraint localization of the Regge repair.

The parent block establishes a flat linear repair for

    S_alpha = sum_h A_h (epsilon_h + alpha epsilon_h**2).

This runner differentiates that actual action away from flatness.  It tracks
the old unsourced nonflat branch to its fold, continues the three retained
compact source covectors from flat at alpha=1/1024, reconstructs the complete
Bloch Hessian on the largest sourced branch, and tests two named constraint
localizations.  It also gives two fixed-momentum witnesses proving that no
single alpha in this one-parameter family keeps the inherited five-normal
inertia under the constant pointwise-affine localization.

Nothing here selects the action, coefficient, source, constraints, Euclidean
signature, or realized history.
"""

from __future__ import annotations

from collections import defaultdict
from pathlib import Path
import sys

import mpmath as mp
from mpmath import iv
import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import admissibility_fixed_metric_nonlinear_regge_kkt_continuation_2026_08_10 as block19  # noqa: E402
import admissibility_flat_regge_curvature_squared_branch_lift_2026_08_10 as block20  # noqa: E402
import frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09 as regge  # noqa: E402


AUDIT_TIMEOUT_SEC = 240

NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_REGGE_CURVATURE_SQUARED_SOURCED_CONTINUATION_"
    "CONSTRAINT_LOCALIZATION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
PARENT_NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_FIXED_METRIC_NONLINEAR_REGGE_KKT_CONTINUATION_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
REPAIR_NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_FLAT_REGGE_CURVATURE_SQUARED_BRANCH_LIFT_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
REACTION_NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_COMPACT_REGGE_HOMOGENEOUS_REACTION_RANK_KKT_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
REGGE_NOTE_PATH = ROOT / "docs" / (
    "CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_"
    "NARROW_THEOREM_NOTE_2026-06-09.md"
)
PREMISE_REGISTRY_PATH = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
PRIMITIVE_PATHS = (
    ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md",
    ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
)

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_REGGE_CURVATURE_SQUARED_SOURCED_CONTINUATION_CONSTRAINT_LOCALIZATION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_FIXED_METRIC_NONLINEAR_REGGE_KKT_CONTINUATION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/ADMISSIBILITY_FLAT_REGGE_CURVATURE_SQUARED_BRANCH_LIFT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/ADMISSIBILITY_COMPACT_REGGE_HOMOGENEOUS_REACTION_RANK_KKT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_NARROW_THEOREM_NOTE_2026-06-09.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
    "scripts/admissibility_fixed_metric_nonlinear_regge_kkt_continuation_2026_08_10.py",
    "scripts/admissibility_flat_regge_curvature_squared_branch_lift_2026_08_10.py",
    "scripts/admissibility_compact_regge_homogeneous_reaction_rank_kkt_boundary_2026_08_10.py",
    "scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py",
)

ALPHA = mp.mpf(1) / 1024
LOWER_WITNESS_ALPHA = 21.0 / 4096.0
UPPER_WITNESS_ALPHA = 20.0 / 4096.0
TOLERANCE = 1.0e-8


class Checks:
    def __init__(self):
        self.passed = 0
        self.failed = 0

    def check(self, key, statement, condition, detail=""):
        ok = bool(condition)
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {statement}")
        if detail:
            print(f"       {detail}")
        self.passed += int(ok)
        self.failed += int(not ok)


def context_scalar(value, ctx):
    if ctx is mp:
        return mp.mpf(value)
    return ctx.mpf(mp.nstr(value, 70))


def geometry_action_jet(lengths, alpha, curvature_only=False):
    """Jet of sum_h A_h (epsilon_h + alpha epsilon_h^2)."""
    n = lengths[0].n
    ctx = lengths[0].ctx
    squared = tuple(length * length for length in lengths)
    area_cache = {}
    angle_cache = {}

    def area(classes):
        if classes not in area_cache:
            qa, qb, qc = (squared[index] for index in classes)
            area_cache[classes] = block19.jet_sqrt(
                (
                    2 * qa * qb
                    + 2 * qa * qc
                    + 2 * qb * qc
                    - qa * qa
                    - qb * qb
                    - qc * qc
                )
                / 16
            )
        return area_cache[classes]

    def angle(missing, classes):
        key = (missing, classes)
        if key in angle_cache:
            return angle_cache[key]
        q = {
            pair: squared[classes[index]]
            for index, pair in enumerate(regge.PAIRS5)
        }

        def qq(left, right):
            return q[(min(left, right), max(left, right))]

        def dot(left, right, base):
            if left == right:
                return qq(base, left)
            return (qq(base, left) + qq(base, right) - qq(left, right)) / 2

        left, right = missing
        base, first, second = [
            index for index in range(5) if index not in missing
        ]
        g11 = dot(first, first, base)
        g12 = dot(first, second, base)
        g22 = dot(second, second, base)
        determinant = g11 * g22 - g12 * g12

        def projected_pair(i, j):
            i1, i2 = dot(first, i, base), dot(second, i, base)
            j1, j2 = dot(first, j, base), dot(second, j, base)
            projection = (
                g22 * i1 * j1
                - g12 * (i1 * j2 + i2 * j1)
                + g11 * i2 * j2
            ) / determinant
            return dot(i, j, base) - projection

        cosine = projected_pair(left, right) / block19.jet_sqrt(
            projected_pair(left, left) * projected_pair(right, right)
        )
        angle_cache[key] = block19.jet_acos(cosine)
        return angle_cache[key]

    total = block19.Jet2.constant(0, n, ctx)
    alpha_ctx = context_scalar(alpha, ctx)
    for area_classes, stars in block19.TRIANGLE_DATA:
        deficit = block19.Jet2.constant(2 * ctx.pi, n, ctx)
        for missing, simplex_classes in stars:
            deficit -= angle(missing, simplex_classes)
        if curvature_only:
            total += area(area_classes) * deficit * deficit
        else:
            total += area(area_classes) * (
                deficit + deficit * deficit * alpha_ctx
            )
    return total


def normal_action(
    coordinates, basis, alpha=ALPHA, curvature_only=False, ctx=mp
):
    variables = [
        block19.Jet2.variable(value, index, 5, ctx)
        for index, value in enumerate(coordinates)
    ]
    lengths = []
    for edge, direction in enumerate(regge.DIRS15):
        value = block19.Jet2.constant(ctx.sqrt(sum(direction)), 5, ctx)
        for column in range(5):
            value += variables[column] * basis[edge][column]
        lengths.append(value)
    return geometry_action_jet(lengths, alpha, curvature_only)


def symmetric_action(a, u, alpha=ALPHA, ctx=mp):
    range_vector, extra_vector = block19.exact_symmetric_vectors(ctx)
    a_jet = block19.Jet2.variable(a, 0, 2, ctx)
    u_jet = block19.Jet2.variable(u, 1, 2, ctx)
    lengths = [
        block19.Jet2.constant(ctx.sqrt(sum(direction)), 2, ctx)
        + a_jet * range_vector[index]
        + u_jet * extra_vector[index]
        for index, direction in enumerate(regge.DIRS15)
    ]
    return geometry_action_jet(lengths, alpha)


def theta_length_hessian(missing, simplex_edges):
    """Complex-step Hessian of one dihedral angle in edge-length variables."""
    lengths = np.asarray([entry[2] for entry in simplex_edges], dtype=float)
    squared = lengths * lengths
    out = regge.THETA[missing](*squared)
    gradient_q = np.asarray(out[1:], dtype=float)
    hessian_q = np.zeros((10, 10), dtype=float)
    for column in range(10):
        probe = squared.astype(complex)
        probe[column] += 1j * 1.0e-20
        shifted = regge.THETA[missing](*probe)
        hessian_q[:, column] = (
            np.imag(np.asarray(shifted[1:], dtype=complex)) / 1.0e-20
        )
    hessian_length = 4.0 * np.outer(lengths, lengths) * hessian_q
    hessian_length += np.diag(2.0 * gradient_q)
    return 0.5 * (hessian_length + hessian_length.T)


def add_pair(kernel, left, right, value):
    row, row_anchor, _ = left
    column, column_anchor, _ = right
    shift = tuple(
        column_anchor[axis] - row_anchor[axis] for axis in range(4)
    )
    kernel[shift][row, column] += float(value)


def curvature_squared_kernel(lengths):
    """Full Hessian of sum_h A_h epsilon_h^2 at uniform lengths."""
    kernel = defaultdict(lambda: np.zeros((15, 15), dtype=float))
    for triangle in regge.TRI_CLASSES:
        area, area_edges, area_terms, deficit, deficit_terms = (
            block20.triangle_geometry(triangle, lengths)
        )

        area_lengths = np.asarray([entry[2] for entry in area_edges])
        area_hessian_q = np.asarray(
            block20.AREA_HESSIAN(*(area_lengths * area_lengths)), dtype=float
        )
        area_out = regge.AREA(*(area_lengths * area_lengths))
        for row_slot, left in enumerate(area_edges):
            for column_slot, right in enumerate(area_edges):
                value = (
                    4.0
                    * left[2]
                    * right[2]
                    * area_hessian_q[row_slot, column_slot]
                )
                if row_slot == column_slot:
                    value += 2.0 * float(area_out[1 + row_slot])
                add_pair(kernel, left, right, deficit * deficit * value)

        for left in area_terms:
            for right in deficit_terms:
                add_pair(kernel, left, right, 2.0 * deficit * left[2] * right[2])
        for left in deficit_terms:
            for right in area_terms:
                add_pair(kernel, left, right, 2.0 * deficit * left[2] * right[2])
        for left in deficit_terms:
            for right in deficit_terms:
                add_pair(kernel, left, right, 2.0 * area * left[2] * right[2])

        for simplex in regge.STARS[triangle]:
            local = {vertex: index for index, vertex in enumerate(simplex)}
            hinge = sorted(local[vertex] for vertex in triangle)
            missing = tuple(
                sorted(index for index in range(5) if index not in hinge)
            )
            simplex_edges = [
                block20.edge_data(simplex[left], simplex[right], lengths)
                for left, right in regge.PAIRS5
            ]
            hessian = theta_length_hessian(missing, simplex_edges)
            for row_slot, left in enumerate(simplex_edges):
                for column_slot, right in enumerate(simplex_edges):
                    add_pair(
                        kernel,
                        left,
                        right,
                        -2.0 * area * deficit * hessian[row_slot, column_slot],
                    )
    return dict(kernel)


def combine_kernels(left, right, alpha=ALPHA):
    return {
        shift: left.get(shift, 0.0) + float(alpha) * right.get(shift, 0.0)
        for shift in set(left) | set(right)
    }


def solve_fold():
    calls = 0

    def equations(a, u, alpha):
        nonlocal calls
        calls += 1
        value = symmetric_action(a, u, alpha)
        determinant = (
            value.hess[0][0] * value.hess[1][1]
            - value.hess[0][1] * value.hess[1][0]
        )
        return value.grad[0], value.grad[1], determinant

    a, u, alpha = mp.findroot(
        equations,
        (mp.mpf("0.0033"), mp.mpf("0.0654"), mp.mpf("0.000394")),
        solver="mdnewton",
        tol=mp.mpf("1e-26"),
        maxsteps=30,
    )
    value = symmetric_action(a, u, alpha)
    determinant = (
        value.hess[0][0] * value.hess[1][1]
        - value.hess[0][1] * value.hess[1][0]
    )
    return a, u, alpha, value, determinant, calls


def trace_parent_branch():
    """Numerically continue the Block-19 symmetric root toward the fold."""
    a, u, _ = block19.symmetric_root()
    records = []
    for alpha in (
        mp.mpf(0),
        mp.mpf("0.0002"),
        mp.mpf("0.00036"),
        mp.mpf("0.00039"),
        mp.mpf("0.000394"),
    ):
        if alpha:
            def equations(next_a, next_u):
                value = symmetric_action(next_a, next_u, alpha)
                return value.grad[0], value.grad[1]

            root = mp.findroot(
                equations,
                (a, u),
                solver="mdnewton",
                tol=mp.mpf("1e-26"),
                maxsteps=30,
            )
            a, u = root[0], root[1]
        value = symmetric_action(a, u, alpha)
        eigenvalues = mp.eigsy(mp.matrix(value.hess), eigvals_only=True)
        records.append(
            (alpha, a, u, mp.norm(mp.matrix(value.grad)), eigenvalues)
        )
    return records


def fold_nondegeneracy(a, u, alpha, value):
    """Return numerical saddle-node transversality diagnostics."""
    eigenvalues, eigenvectors = mp.eigsy(mp.matrix(value.hess))
    null_index = min(range(2), key=lambda index: abs(eigenvalues[index]))
    null_vector = mp.matrix(
        [eigenvectors[row, null_index] for row in range(2)]
    )

    alpha_step = mp.mpf("1e-8")
    alpha_plus = symmetric_action(a, u, alpha + alpha_step)
    alpha_minus = symmetric_action(a, u, alpha - alpha_step)
    parameter_derivative = mp.matrix(
        [
            (alpha_plus.grad[index] - alpha_minus.grad[index])
            / (2 * alpha_step)
            for index in range(2)
        ]
    )
    transversality = (null_vector.T * parameter_derivative)[0]

    coordinate_step = mp.mpf("1e-6")
    coordinate_plus = symmetric_action(
        a + coordinate_step * null_vector[0],
        u + coordinate_step * null_vector[1],
        alpha,
    )
    coordinate_minus = symmetric_action(
        a - coordinate_step * null_vector[0],
        u - coordinate_step * null_vector[1],
        alpha,
    )
    directional_hessian_derivative = mp.matrix(2)
    for row in range(2):
        for column in range(2):
            directional_hessian_derivative[row, column] = (
                coordinate_plus.hess[row][column]
                - coordinate_minus.hess[row][column]
            ) / (2 * coordinate_step)
    null_quadratic = (
        null_vector.T * directional_hessian_derivative * null_vector
    )[0]
    return eigenvalues, transversality, null_quadratic


def solve_source(source, coupling, basis):
    target = block19.exact_source_target(source, coupling, mp)
    coordinates = [mp.mpf(0) for _ in range(5)]
    for iteration in range(12):
        value = normal_action(coordinates, basis)
        residual = mp.matrix(
            [value.grad[index] - target[index] for index in range(5)]
        )
        if mp.norm(residual) < mp.mpf("1e-28"):
            break
        correction = mp.lu_solve(mp.matrix(value.hess), -residual)
        coordinates = [
            coordinates[index] + correction[index] for index in range(5)
        ]
    value = normal_action(coordinates, basis)
    residual = mp.matrix(
        [value.grad[index] - target[index] for index in range(5)]
    )
    return coordinates, value, mp.norm(residual), iteration


def source_krawczyk(coordinates, center_jet, source, coupling):
    radius = mp.mpf("2e-9")
    boxes = [
        iv.mpf(
            [
                mp.nstr(value - radius, 70),
                mp.nstr(value + radius, 70),
            ]
        )
        for value in coordinates
    ]
    interval_basis = block19.exact_normal_basis(iv)
    box_jet = normal_action(boxes, interval_basis, ctx=iv)
    inverse = mp.matrix(center_jet.hess) ** -1
    center_intervals = [iv.mpf(mp.nstr(value, 70)) for value in coordinates]
    point_jet = normal_action(center_intervals, interval_basis, ctx=iv)
    inverse_intervals = [
        [iv.mpf(mp.nstr(inverse[row, column], 70)) for column in range(5)]
        for row in range(5)
    ]
    targets = block19.exact_source_target(source, coupling, iv)
    newton_center = []
    for row in range(5):
        value = center_intervals[row]
        for column in range(5):
            value -= inverse_intervals[row][column] * (
                point_jet.grad[column] - targets[column]
            )
        newton_center.append(value)
    delta_box = iv.mpf([mp.nstr(-radius, 70), mp.nstr(radius, 70)])
    image = []
    for row in range(5):
        value = newton_center[row]
        for column in range(5):
            coefficient = iv.mpf(int(row == column))
            for inner in range(5):
                coefficient -= (
                    inverse_intervals[row][inner]
                    * box_jet.hess[inner][column]
                )
            value += coefficient * delta_box
        image.append(value)
    inside = all(
        float(value.a) > float(coordinates[index] - radius)
        and float(value.b) < float(coordinates[index] + radius)
        for index, value in enumerate(image)
    )
    contraction = max(
        (float(value.b) - float(value.a)) / (2 * float(radius))
        for value in image
    )
    return inside, contraction, radius


def determinant_root(kernel, direction, left, right, basis=None):
    def matrix(value):
        result = block20.bloch(kernel, value * direction)
        if basis is not None:
            result = basis.T @ result @ basis
        return result

    left_value = float(np.linalg.det(matrix(left)).real)
    right_value = float(np.linalg.det(matrix(right)).real)
    initial = (left_value, right_value)
    if left_value * right_value >= 0:
        raise AssertionError("determinant bracket does not change sign")
    left_inertia = block20.inertia(np.linalg.eigvalsh(matrix(left)))
    right_inertia = block20.inertia(np.linalg.eigvalsh(matrix(right)))
    for _ in range(70):
        midpoint = 0.5 * (left + right)
        middle_value = float(np.linalg.det(matrix(midpoint)).real)
        if left_value * middle_value <= 0:
            right = midpoint
            right_value = middle_value
        else:
            left = midpoint
            left_value = middle_value
    root = 0.5 * (left + right)
    return (
        root,
        initial,
        left_inertia,
        right_inertia,
        np.linalg.eigvalsh(matrix(root)),
    )


def main():
    mp.mp.dps = 40
    iv.dps = 35
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    parent_note = PARENT_NOTE_PATH.read_text(encoding="utf-8")
    repair_note = REPAIR_NOTE_PATH.read_text(encoding="utf-8")
    reaction_note = REACTION_NOTE_PATH.read_text(encoding="utf-8")
    regge_note = REGGE_NOTE_PATH.read_text(encoding="utf-8")
    registry = PREMISE_REGISTRY_PATH.read_text(encoding="utf-8")
    primitives = "\n".join(
        path.read_text(encoding="utf-8") for path in PRIMITIVE_PATHS
    )
    note_flat = " ".join(note.split())
    axiom_flat = " ".join(axiom.split())
    parent_flat = " ".join(parent_note.split())
    repair_flat = " ".join(repair_note.split())

    print("external_scientific_inputs: none; all actions, sources, roots, and Hessians are reconstructed from repository-local Regge data")
    print("package_local_integrity_reads: current axioms, approved primitives, Blocks 17/19/20, and the retained Regge carrier are source-bound")
    print("analytic_boundary: source roots have interval Krawczyk certificates; the fold and momentum roots are high-precision numerical brackets, not interval root theorems")
    print("physical_boundary: Euclidean signature, alpha=1/1024, compact sources, affine constraints, and both localization extensions remain supplied fixtures")

    checks.check(
        "source-and-axiom-boundary",
        "the current foundation selects neither the gravity action nor source and constraint localization",
        "Admissibility is not a dynamics axiom" in axiom_flat
        and "source/action and physical-observable identification" in axiom_flat
        and "ten affine constraints" in parent_flat
        and "fix the constant-metric tangent coordinates" in parent_flat
        and "does not select" in parent_flat
        and "constraint" in repair_flat
        and '"kinetic_isotropy_primitive"' in registry
        and "It carries no dimensionless dynamical content" in primitives,
    )
    checks.check(
        "source-note-contract",
        "the note states the bounded two-witness result, live alternatives, N1-N8 gate, and candidate law wording",
        "21/4096" in note
        and "20/4096" in note
        and "No-Go Discipline Gate" in note
        and "Candidate Geometry-Law Wording" in note
        and "generalized-pencil intersection" in note
        and "| `W1,W2` | no | no | yes |" in note
        and "N1--N8 status: `PASS` only" in note
        and "`kinetic_isotropy_primitive`" in note
        and "covariant sourced second variation" in note_flat
        and "not a gravity no-go" in note_flat,
    )
    checks.check(
        "source-parent-carriers",
        "the retained sources, Regge action, nonflat continuation, and flat repair are all explicit upstream carriers",
        "three" in reaction_note
        and "four massive branches" in regge_note
        and "interval-certified" in parent_note
        and "curvature-square" in repair_note,
    )

    exact_basis = block19.exact_normal_basis(mp)
    basis = np.asarray(exact_basis, dtype=float)
    flat_lengths = np.sqrt(
        np.asarray([sum(direction) for direction in regge.DIRS15], dtype=float)
    )
    flat_q, flat_deficits = block20.uniform_regge_kernel(flat_lengths)
    flat_r2 = curvature_squared_kernel(flat_lengths)
    parent_flat_r2 = block20.curvature_squared_kernel(flat_lengths)
    flat_r2_error = max(
        float(np.max(np.abs(flat_r2[shift] - parent_flat_r2.get(shift, 0.0))))
        for shift in set(flat_r2) | set(parent_flat_r2)
    )
    checks.check(
        "full-curvature-hessian-flat-reduction",
        "the off-flat Hessian formula reduces to the parent's exact flat Gram form",
        flat_r2_error < 2.0e-10
        and np.max(np.abs(flat_deficits)) < 2.0e-13,
        f"kernel error={flat_r2_error:.3e}; deficit max={np.max(np.abs(flat_deficits)):.3e}",
    )

    parent_coordinates = [
        mp.mpf("0.0176289114528026416711"),
        mp.mpf(0),
        mp.mpf(0),
        mp.mpf(0),
        mp.mpf("0.1522365512153477903341"),
    ]
    parent_lengths = flat_lengths + basis @ np.asarray(
        parent_coordinates, dtype=float
    )
    parent_q, _ = block20.uniform_regge_kernel(parent_lengths)
    parent_r2 = curvature_squared_kernel(parent_lengths)
    parent_combined = combine_kernels(parent_q, parent_r2)
    parent_jet = normal_action(parent_coordinates, exact_basis)
    parent_projected = (
        basis.T
        @ block20.bloch(parent_combined, np.zeros(4)).real
        @ basis
    )
    parent_error = float(
        np.max(np.abs(parent_projected - np.asarray(parent_jet.hess, dtype=float)))
    )
    checks.check(
        "off-flat-k0-action-reconstruction",
        "the complete real-space extended Hessian matches independent automatic differentiation off flatness",
        parent_error < 2.0e-10,
        f"five-normal Hessian error={parent_error:.3e}",
    )

    branch_trace = trace_parent_branch()
    fold_a, fold_u, fold_alpha, fold_jet, fold_det, fold_calls = solve_fold()
    fold_eigenvalues, fold_transversality, fold_null_quadratic = (
        fold_nondegeneracy(
            fold_a, fold_u, fold_alpha, fold_jet
        )
    )
    fold_residual = mp.norm(mp.matrix(fold_jet.grad))
    branch_positive_eigenvalues = [record[4][1] for record in branch_trace]
    branch_residual = max(record[3] for record in branch_trace)
    branch_endpoint_distance = mp.sqrt(
        (branch_trace[-1][1] - fold_a) ** 2
        + (branch_trace[-1][2] - fold_u) ** 2
    )
    checks.check(
        "tracked-unsourced-branch-fold",
        "the numerically continued Block-19 unsourced branch reaches a stationary Hessian singularity before alpha=1/1024",
        fold_residual < mp.mpf("1e-24")
        and abs(fold_det) < mp.mpf("1e-22")
        and mp.mpf("0.00039418") < fold_alpha < mp.mpf("0.00039420")
        and fold_alpha < ALPHA,
        f"a={mp.nstr(fold_a, 13)}; u={mp.nstr(fold_u, 13)}; alpha_fold={mp.nstr(fold_alpha, 14)}; residual={mp.nstr(fold_residual, 3)}; calls={fold_calls}",
    )
    checks.check(
        "tracked-unsourced-saddle-node-nondegeneracy",
        "continuation from the Block-19 root and both saddle-node transversality coefficients are numerically nonzero",
        branch_residual < mp.mpf("1e-24")
        and all(value > 0 for value in branch_positive_eigenvalues)
        and all(
            branch_positive_eigenvalues[index + 1]
            < branch_positive_eigenvalues[index]
            for index in range(len(branch_positive_eigenvalues) - 1)
        )
        and branch_endpoint_distance < mp.mpf("0.002")
        and abs(fold_eigenvalues[0]) > mp.mpf("40")
        and abs(fold_eigenvalues[1]) < mp.mpf("1e-20")
        and abs(fold_transversality) > mp.mpf("100")
        and abs(fold_null_quadratic) > mp.mpf("15"),
        "positive eigenvalue path="
        + ",".join(mp.nstr(value, 6) for value in branch_positive_eigenvalues)
        + f"; endpoint distance={mp.nstr(branch_endpoint_distance, 4)}"
        + f"; parameter transversality={mp.nstr(fold_transversality, 8)}"
        + f"; null quadratic={mp.nstr(fold_null_quadratic, 8)}",
    )

    sources = block19.reaction.exact_source_rows()
    coupling = sp.Rational(1, 100)
    names = ("two-stream", "bundle-A", "bundle-B")
    source_records = []
    for name, source in zip(names, sources):
        coordinates, value, residual, iterations = solve_source(
            source, coupling, exact_basis
        )
        inside, contraction, radius = source_krawczyk(
            coordinates, value, source, coupling
        )
        eigenvalues = np.linalg.eigvalsh(np.asarray(value.hess, dtype=float))
        source_records.append(
            (
                name,
                coordinates,
                value,
                residual,
                iterations,
                inside,
                contraction,
                radius,
                eigenvalues,
            )
        )
    checks.check(
        "three-sourced-stationary-continuations",
        "all three retained compact source covectors have nondegenerate alpha=1/1024 continuations from flat",
        all(
            record[3] < mp.mpf("1e-25")
            and block20.inertia(record[8]) == (4, 1, 0)
            for record in source_records
        ),
        "; ".join(
            f"{record[0]}: residual={mp.nstr(record[3], 2)}, iterations={record[4]}, u={mp.nstr(record[1][4], 9)}"
            for record in source_records
        ),
    )
    checks.check(
        "three-sourced-interval-certificates",
        "each sourced continuation is unique in its declared five-normal interval box",
        all(record[5] and record[6] < 2.0e-2 for record in source_records),
        "; ".join(
            f"{record[0]}: radius={mp.nstr(record[7], 2)}, contraction={record[6]:.3e}"
            for record in source_records
        ),
    )

    bundle_coordinates = source_records[-1][1]
    bundle_jet = source_records[-1][2]
    bundle_lengths = flat_lengths + basis @ np.asarray(
        bundle_coordinates, dtype=float
    )
    bundle_q, bundle_deficits = block20.uniform_regge_kernel(bundle_lengths)
    bundle_r2 = curvature_squared_kernel(bundle_lengths)
    bundle_kernel = combine_kernels(bundle_q, bundle_r2)
    bundle_projected = (
        basis.T @ block20.bloch(bundle_kernel, np.zeros(4)).real @ basis
    )
    bundle_k0_error = float(
        np.max(
            np.abs(bundle_projected - np.asarray(bundle_jet.hess, dtype=float))
        )
    )
    checks.check(
        "sourced-off-flat-k0-reconstruction",
        "the complete sourced Bundle-B Hessian reduces to its independently certified five-normal Hessian",
        bundle_k0_error < 2.0e-10
        and np.max(np.abs(bundle_deficits)) > 0.05,
        f"Hessian error={bundle_k0_error:.3e}; deficit max={np.max(np.abs(bundle_deficits)):.6f}",
    )

    rng = np.random.default_rng(21082026)
    box_vector = rng.normal(size=15)
    box_vector /= np.linalg.norm(box_vector)
    box_momentum = np.asarray((2.0 * np.pi / 3.0, 2.0 * np.pi / 3.0, 0.0, 0.0))
    background_delta = bundle_lengths - flat_lengths

    def sourced_eps(scale):
        def evaluate(edge_class, anchor):
            return background_delta[edge_class] + scale * box_vector[
                edge_class
            ] * np.cos(np.dot(box_momentum, anchor))

        return evaluate

    def sourced_box_action(scale):
        eps = sourced_eps(scale)
        return regge.box_action(3, eps) + float(ALPHA) * block20.box_curvature_square(
            3, eps
        )

    step = 4.0e-4
    box_second = (
        sourced_box_action(step)
        - 2.0 * sourced_box_action(0.0)
        + sourced_box_action(-step)
    ) / (step * step)
    box_prediction = (
        3**4
        / 2.0
        * float(
            box_vector
            @ block20.bloch(bundle_kernel, box_momentum).real
            @ box_vector
        )
    )
    box_relative = abs(box_second - box_prediction) / abs(box_prediction)
    checks.check(
        "sourced-periodic-action-validation",
        "an independent periodic extended-action second difference reproduces the nonzero-momentum sourced Hessian",
        box_relative < 2.0e-6,
        f"finite difference={box_second:.7f}; prediction={box_prediction:.7f}; relative={box_relative:.3e}",
    )

    generic_direction = np.asarray((1.0, 0.7, -0.4, 0.2))
    global_root = determinant_root(
        bundle_kernel, generic_direction, 0.02, 0.03
    )
    pointwise_root = determinant_root(
        bundle_kernel, generic_direction, 1.9, 2.1, basis=basis
    )
    checks.check(
        "sourced-global-soft-mode",
        "the globally constrained sourced extension numerically brackets a generic-momentum inertia crossing",
        global_root[1][0] * global_root[1][1] < 0
        and global_root[2] == (7, 8, 0)
        and global_root[3] == (8, 7, 0)
        and np.min(np.abs(global_root[4])) < 2.0e-10
        and abs(global_root[0] - 0.0240357490) < 2.0e-8,
        f"x={global_root[0]:.12f}; bracket=({global_root[1][0]:.3e},{global_root[1][1]:.3e}); inertias={global_root[2]}/{global_root[3]}",
    )
    checks.check(
        "sourced-pointwise-soft-mode",
        "the constant pointwise five-normal sourced extension brackets a distinct high-momentum crossing",
        pointwise_root[1][0] * pointwise_root[1][1] < 0
        and pointwise_root[2] == (4, 1, 0)
        and pointwise_root[3] == (5, 0, 0)
        and np.min(np.abs(pointwise_root[4])) < 2.0e-10
        and abs(pointwise_root[0] - 1.9834291011) < 2.0e-8,
        f"x={pointwise_root[0]:.12f}; bracket=({pointwise_root[1][0]:.3e},{pointwise_root[1][1]:.3e}); inertias={pointwise_root[2]}/{pointwise_root[3]}",
    )

    lower_momentum = np.asarray(
        (2.0 * np.pi / 3.0, -np.pi / 2.0, 2.0 * np.pi / 3.0, -np.pi / 2.0)
    )
    upper_momentum = np.asarray(
        (0.0, 3.0 * np.pi / 4.0, 3.0 * np.pi / 4.0, 3.0 * np.pi / 4.0)
    )

    def normal_pair(momentum):
        q = basis.T @ block20.bloch(flat_q, momentum) @ basis
        correction = basis.T @ block20.bloch(flat_r2, momentum) @ basis
        return q, correction

    def generalized_crossings(q, correction):
        correction_values, correction_vectors = np.linalg.eigh(correction)
        inverse_square_root = (
            correction_vectors * (1.0 / np.sqrt(correction_values))
        ) @ correction_vectors.T.conj()
        return np.linalg.eigvalsh(
            -inverse_square_root @ q @ inverse_square_root
        )

    lower_q, lower_r2 = normal_pair(lower_momentum)
    upper_q, upper_r2 = normal_pair(upper_momentum)
    lower_values = np.linalg.eigvalsh(
        lower_q + LOWER_WITNESS_ALPHA * lower_r2
    )
    upper_values = np.linalg.eigvalsh(
        upper_q + UPPER_WITNESS_ALPHA * upper_r2
    )
    correction_gap = min(
        float(np.min(np.linalg.eigvalsh(lower_r2))),
        float(np.min(np.linalg.eigvalsh(upper_r2))),
    )
    lower_crossings = generalized_crossings(lower_q, lower_r2)
    upper_crossings = generalized_crossings(upper_q, upper_r2)
    checks.check(
        "pointwise-coefficient-two-witness-no-overlap",
        "positive-semidefinite monotonicity makes the two pointwise-affine coefficient requirements disjoint",
        correction_gap > 40.0
        and block20.inertia(lower_values) == (5, 0, 0)
        and np.max(lower_values) < -0.2
        and block20.inertia(upper_values) == (3, 2, 0)
        and upper_values[-2] > 0.3
        and LOWER_WITNESS_ALPHA > UPPER_WITNESS_ALPHA,
        f"lower alpha=21/4096 requires alpha greater, max eigenvalue={np.max(lower_values):.6f}; upper alpha=20/4096 requires alpha smaller, second-positive={upper_values[-2]:.6f}; correction gap={correction_gap:.6f}",
    )
    checks.check(
        "pointwise-generalized-crossing-intervals",
        "an independent whitened-pencil calculation gives disjoint coefficient intervals for four-negative/one-positive inertia",
        lower_crossings[0] > LOWER_WITNESS_ALPHA
        and upper_crossings[1] < UPPER_WITNESS_ALPHA
        and lower_crossings[0] > upper_crossings[1]
        and lower_crossings[1] > lower_crossings[0]
        and upper_crossings[1] > upper_crossings[0],
        "lower target interval="
        + f"({lower_crossings[0]:.12f},{lower_crossings[1]:.12f}); "
        + "upper target interval="
        + f"({upper_crossings[0]:.12f},{upper_crossings[1]:.12f})",
    )

    flat_repaired = combine_kernels(flat_q, flat_r2)
    full_witness_inertias = [
        block20.inertia(
            np.linalg.eigvalsh(block20.bloch(flat_repaired, momentum))
        )
        for momentum in (lower_momentum, upper_momentum)
    ]
    checks.check(
        "full-gauge-quotient-alternative-remains-live",
        "the same two momenta retain the parent's repaired full-symbol inertia and exact four-gauge kernel",
        full_witness_inertias == [(9, 2, 4), (9, 2, 4)],
        f"full inertias={full_witness_inertias}",
    )

    print("per_element: checked all fifteen edge classes in the full off-flat Einstein-plus-curvature-square Hessian")
    print("per_site: checked all fifty hinge classes and every local area, deficit, and deficit-Hessian contribution")
    print("per_mode: checked two root-of-unity coefficient witnesses, one generic sourced path, and one independent periodic Bloch mode")
    print("per_block: checked the Block-19-connected fold, three sourced continuations, and the largest sourced background")
    print("lattice_wide: checked and not executed — no continuous-zone or full source-field theorem; only the two fixed witnesses and one sourced path are resolved")

    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return int(checks.failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
