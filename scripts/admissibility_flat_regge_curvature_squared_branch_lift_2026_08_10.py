#!/usr/bin/env python3
"""Check a finite-momentum Regge boundary and an action-native flat repair.

The paired note separates two questions that the homogeneous nonlinear KKT
certificate cannot answer by itself:

* the complete inhomogeneous Hessian of its named nonflat background; and
* whether the flat weak-field carrier's fifth, nonmetric zero branch can be
  lifted by a local geometry action rather than an inserted projector.

The repair studied here is the supplied fixture

    S_alpha = sum_h A_h (epsilon_h + alpha epsilon_h**2), alpha = 1/1024.

At a flat background its exact second variation is

    Q_alpha(k) = Q_R(k) + 2 alpha sum_h A_h d_h(k)^dag d_h(k).

No coefficient selection, Lorentzian continuation, or realized geometry law
is inferred from the finite fixture.
"""

from __future__ import annotations

from collections import defaultdict
from functools import lru_cache
from itertools import product
from pathlib import Path
import sys

import numpy as np
import sympy as sp


AUDIT_TIMEOUT_SEC = 240

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_FLAT_REGGE_CURVATURE_SQUARED_BRANCH_LIFT_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
PARENT_NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_FIXED_METRIC_NONLINEAR_REGGE_KKT_CONTINUATION_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
REGGE_NOTE_PATH = ROOT / "docs" / (
    "CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_"
    "NARROW_THEOREM_NOTE_2026-06-09.md"
)
HISTORY_NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_CLOSED_HELICAL_DEFECT_HISTORY_WARD_NEUTRAL_IR_"
    "REGGE_RESPONSE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
ACTION_SELECTION_NOTE_PATH = ROOT / "docs" / (
    "CUBIC_COXETER_REGGE_LINEARIZED_ACTION_SELECTION_EH_CLASS_"
    "NARROW_THEOREM_NOTE_2026-06-10.md"
)
PREMISE_REGISTRY_PATH = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
PRIMITIVE_PATHS = (
    ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md",
    ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
)

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_FLAT_REGGE_CURVATURE_SQUARED_BRANCH_LIFT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_FIXED_METRIC_NONLINEAR_REGGE_KKT_CONTINUATION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_NARROW_THEOREM_NOTE_2026-06-09.md",
    "docs/ADMISSIBILITY_CLOSED_HELICAL_DEFECT_HISTORY_WARD_NEUTRAL_IR_REGGE_RESPONSE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/CUBIC_COXETER_REGGE_LINEARIZED_ACTION_SELECTION_EH_CLASS_NARROW_THEOREM_NOTE_2026-06-10.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
    "scripts/admissibility_fixed_metric_nonlinear_regge_kkt_continuation_2026_08_10.py",
    "scripts/admissibility_nonlinear_regge_extra_branch_cubic_lift_2026_08_10.py",
    "scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py",
    "scripts/frontier_cubic_coxeter_regge_linearized_action_selection_2026_06_10.py",
)

sys.path.insert(0, str(ROOT / "scripts"))
import admissibility_fixed_metric_nonlinear_regge_kkt_continuation_2026_08_10 as block19  # noqa: E402
import admissibility_nonlinear_regge_extra_branch_cubic_lift_2026_08_10 as block18  # noqa: E402
import frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09 as regge  # noqa: E402


ALPHA = 1.0 / 1024.0
TOLERANCE = 1.0e-8
BODY = np.asarray((1, 1, 1, 1), dtype=int)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition: bool, detail: str = "") -> None:
        ok = bool(condition)
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {statement}")
        if detail:
            print(f"       {detail}")
        self.passed += int(ok)
        self.failed += int(not ok)


AREA_HESSIAN = sp.lambdify(
    regge.AREA_SYMS,
    [
        [sp.diff(regge._A, left, right) for right in regge.AREA_SYMS]
        for left in regge.AREA_SYMS
    ],
    "numpy",
)


def edge_data(left, right, lengths):
    edge_class, anchor = regge.edge_class(tuple(left), tuple(right))
    return (
        edge_class,
        tuple(int(value) for value in anchor),
        float(lengths[edge_class]),
    )


def triangle_geometry(triangle, lengths):
    vertices = [np.asarray(vertex) for vertex in triangle]
    area_edges = [
        edge_data(vertices[left], vertices[right], lengths)
        for left, right in ((0, 1), (0, 2), (1, 2))
    ]
    area_lengths = np.asarray([entry[2] for entry in area_edges])
    area_out = regge.AREA(*(area_lengths * area_lengths))
    area = float(area_out[0])
    area_terms = [
        (edge_class, anchor, 2.0 * length * float(area_out[1 + slot]))
        for slot, (edge_class, anchor, length) in enumerate(area_edges)
    ]

    deficit = 2.0 * np.pi
    deficit_terms_raw = []
    for simplex in regge.STARS[triangle]:
        local = {vertex: index for index, vertex in enumerate(simplex)}
        hinge = sorted(local[vertex] for vertex in triangle)
        missing = tuple(sorted(index for index in range(5) if index not in hinge))
        simplex_edges = [
            edge_data(simplex[left], simplex[right], lengths)
            for left, right in regge.PAIRS5
        ]
        simplex_lengths = np.asarray([entry[2] for entry in simplex_edges])
        theta = regge.THETA[missing](*(simplex_lengths * simplex_lengths))
        deficit -= float(theta[0])
        for slot, (edge_class, anchor, length) in enumerate(simplex_edges):
            deficit_terms_raw.append(
                (edge_class, anchor, -2.0 * length * float(theta[1 + slot]))
            )

    deficit_map = defaultdict(float)
    for edge_class, anchor, value in deficit_terms_raw:
        deficit_map[(edge_class, anchor)] += value
    deficit_terms = [
        (key[0], key[1], value) for key, value in deficit_map.items()
    ]
    return area, area_edges, area_terms, deficit, deficit_terms


def add_kernel(kernel, shift, row, column, value):
    kernel[shift][row, column] += float(value)


def uniform_regge_kernel(lengths):
    """Real-space Hessian of the actual Regge action at uniform lengths."""
    kernel = defaultdict(lambda: np.zeros((15, 15), dtype=float))
    deficits = []
    for triangle in regge.TRI_CLASSES:
        area, area_edges, area_terms, deficit, deficit_terms = triangle_geometry(
            triangle, lengths
        )
        del area
        deficits.append(deficit)
        for row, row_anchor, row_value in area_terms:
            for column, column_anchor, column_value in deficit_terms:
                shift = tuple(
                    column_anchor[axis] - row_anchor[axis] for axis in range(4)
                )
                add_kernel(
                    kernel,
                    shift,
                    row,
                    column,
                    0.5 * row_value * column_value,
                )
        for row, row_anchor, row_value in deficit_terms:
            for column, column_anchor, column_value in area_terms:
                shift = tuple(
                    column_anchor[axis] - row_anchor[axis] for axis in range(4)
                )
                add_kernel(
                    kernel,
                    shift,
                    row,
                    column,
                    0.5 * row_value * column_value,
                )

        area_lengths = np.asarray([entry[2] for entry in area_edges])
        area_hessian_q = np.asarray(
            AREA_HESSIAN(*(area_lengths * area_lengths)), dtype=float
        )
        area_out = regge.AREA(*(area_lengths * area_lengths))
        for row_slot, (row, row_anchor, row_length) in enumerate(area_edges):
            for column_slot, (
                column,
                column_anchor,
                column_length,
            ) in enumerate(area_edges):
                value = (
                    4.0
                    * row_length
                    * column_length
                    * area_hessian_q[row_slot, column_slot]
                )
                if row_slot == column_slot:
                    value += 2.0 * float(area_out[1 + row_slot])
                shift = tuple(
                    column_anchor[axis] - row_anchor[axis] for axis in range(4)
                )
                add_kernel(kernel, shift, row, column, deficit * value)
    return dict(kernel), np.asarray(deficits)


def curvature_squared_kernel(flat_lengths):
    """Exact flat-background Hessian of sum_h A_h epsilon_h**2."""
    kernel = defaultdict(lambda: np.zeros((15, 15), dtype=float))
    for triangle in regge.TRI_CLASSES:
        area, _, _, deficit, deficit_terms = triangle_geometry(
            triangle, flat_lengths
        )
        if abs(deficit) >= 1.0e-12:
            raise AssertionError("curvature-square Hessian requires the flat anchor")
        for row, row_anchor, row_value in deficit_terms:
            for column, column_anchor, column_value in deficit_terms:
                shift = tuple(
                    column_anchor[axis] - row_anchor[axis] for axis in range(4)
                )
                add_kernel(
                    kernel,
                    shift,
                    row,
                    column,
                    2.0 * area * row_value * column_value,
                )
    return dict(kernel)


def exact_extra_curvature_square_hessian():
    """Compute the flat S_2 Hessian along Block 18's exact extra branch.

    Block 18's truncated-series algebra works over
    Q(sqrt(2),sqrt(3)).  Here every triangle deficit is expanded from the
    actual simplex angles before the coefficient is collected, so the value
    is derived rather than embedded as a comparator.
    """
    jet = block18.Jet
    lengths = tuple(
        jet.constant(sp.sqrt(sum(direction)))
        + jet.monomial((1, 0), block18.EXTRA[index])
        for index, direction in enumerate(regge.DIRS15)
    )
    squared = tuple(length * length for length in lengths)

    @lru_cache(maxsize=None)
    def area(classes):
        qa, qb, qc = (squared[index] for index in classes)
        return block18.jet_sqrt(
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

    @lru_cache(maxsize=None)
    def angle_delta(missing, classes):
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

        cosine = projected_pair(left, right) / block18.jet_sqrt(
            projected_pair(left, left) * projected_pair(right, right)
        )
        return block18.jet_acos_delta(cosine)

    total = jet.constant(0)
    for triangle in regge.TRI_CLASSES:
        deficit = jet.constant(0)
        for simplex in regge.STARS[triangle]:
            local = {vertex: index for index, vertex in enumerate(simplex)}
            hinge = sorted(local[vertex] for vertex in triangle)
            missing = tuple(
                sorted(index for index in range(5) if index not in hinge)
            )
            deficit -= angle_delta(
                missing, block18.simplex_edge_classes(simplex)
            )
        total += (
            area(block18.triangle_edge_classes(triangle))
            * deficit
            * deficit
        )
    coefficient = total.coefficient((2, 0))
    return sp.simplify(2 * block18.K.to_sympy(coefficient))


def bloch(kernel, momentum):
    out = np.zeros((15, 15), dtype=complex)
    for shift, matrix in kernel.items():
        out += matrix * np.exp(1j * np.dot(momentum, shift))
    return 0.5 * (out + out.conjugate().T)


def inertia(values, tolerance=TOLERANCE):
    return (
        int(np.sum(values < -tolerance)),
        int(np.sum(values > tolerance)),
        int(np.sum(np.abs(values) <= tolerance)),
    )


def orthonormal_columns(matrix, tolerance=1.0e-9):
    left, singular, _ = np.linalg.svd(matrix, full_matrices=False)
    return left[:, singular > tolerance]


def extra_direction(q, gauge):
    values, vectors = np.linalg.eigh(q)
    null = vectors[:, np.abs(values) < TOLERANCE]
    gauge_basis = orthonormal_columns(gauge)
    residual = null - gauge_basis @ (gauge_basis.conjugate().T @ null)
    extra = orthonormal_columns(residual)
    if null.shape[1] != 5 or gauge_basis.shape[1] != 4 or extra.shape[1] != 1:
        raise AssertionError("expected four gauge modes and one extra branch")
    return extra[:, 0]


def determinant_root(kernel, left, right, basis=None):
    def determinant(value):
        q = bloch(kernel, np.asarray((value, value, 0.0, 0.0)))
        if basis is not None:
            q = basis.conjugate().T @ q @ basis
        return float(np.linalg.det(q).real)

    left_value = determinant(left)
    right_value = determinant(right)
    if left_value * right_value >= 0:
        raise AssertionError("determinant bracket does not change sign")
    initial = (left_value, right_value)
    for _ in range(70):
        midpoint = 0.5 * (left + right)
        middle_value = determinant(midpoint)
        if left_value * middle_value <= 0:
            right = midpoint
            right_value = middle_value
        else:
            left = midpoint
            left_value = middle_value
    root = 0.5 * (left + right)
    q = bloch(kernel, np.asarray((root, root, 0.0, 0.0)))
    if basis is not None:
        q = basis.conjugate().T @ q @ basis
    return root, initial, np.linalg.eigvalsh(q)


def box_curvature_square(length, eps_fun):
    """Independent periodic action sum_h A_h epsilon_h**2."""
    triangle_deficits = {}
    triangle_areas = {}
    for base in product(range(length), repeat=4):
        for simplex in regge.cell_simplices(base):
            simplex_mod = [tuple(np.mod(vertex, length)) for vertex in simplex]
            squared = []
            for left, right in regge.PAIRS5:
                edge_class, anchor = regge.edge_class(
                    simplex[left], simplex[right]
                )
                flat = np.sqrt(float(sum(regge.DIRS15[edge_class])))
                edge_length = flat + eps_fun(
                    edge_class, np.mod(anchor, length)
                )
                squared.append(edge_length * edge_length)
            for missing in regge.PAIRS5:
                hinge = [
                    vertex
                    for slot, vertex in enumerate(simplex_mod)
                    if slot not in missing
                ]
                key = tuple(sorted(hinge))
                theta = regge.THETA[missing](*squared)
                triangle_deficits.setdefault(key, 2.0 * np.pi)
                triangle_deficits[key] -= float(theta[0])
                if key not in triangle_areas:
                    vertices = [
                        np.asarray(simplex[slot])
                        for slot in range(5)
                        if slot not in missing
                    ]

                    def perturbed_edge(left_vertex, right_vertex):
                        edge_class, anchor = regge.edge_class(
                            tuple(left_vertex), tuple(right_vertex)
                        )
                        flat = np.sqrt(float(sum(regge.DIRS15[edge_class])))
                        return flat + eps_fun(
                            edge_class, np.mod(anchor, length)
                        )

                    edge_lengths = (
                        perturbed_edge(vertices[0], vertices[1]),
                        perturbed_edge(vertices[0], vertices[2]),
                        perturbed_edge(vertices[1], vertices[2]),
                    )
                    triangle_areas[key] = float(
                        regge.AREA(*(value * value for value in edge_lengths))[0]
                    )
    return sum(
        triangle_areas[key] * triangle_deficits[key] ** 2
        for key in triangle_deficits
    )


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    parent = PARENT_NOTE_PATH.read_text(encoding="utf-8")
    regge_note = REGGE_NOTE_PATH.read_text(encoding="utf-8")
    history_note = HISTORY_NOTE_PATH.read_text(encoding="utf-8")
    action_selection_note = ACTION_SELECTION_NOTE_PATH.read_text(encoding="utf-8")
    registry = PREMISE_REGISTRY_PATH.read_text(encoding="utf-8")
    primitives = "\n".join(path.read_text(encoding="utf-8") for path in PRIMITIVE_PATHS)
    note_flat = " ".join(note.split())
    axiom_flat = " ".join(axiom.split())
    parent_flat = " ".join(parent.split())
    regge_flat = " ".join(regge_note.split())
    history_flat = " ".join(history_note.split())
    action_selection_flat = (
        " ".join(action_selection_note.split()).replace("`", "").replace("**", "")
    )

    print("external_scientific_inputs: none; all geometry, spectra, and finite inventories are computed from repository-local edge action data")
    print("package_local_integrity_reads: current axioms, all approved primitives, Block 19, the actual Regge carrier, and the prior fifth-branch source control are source-bound")
    print("analytic_boundary: the curvature-square second variation and exact gauge kernel are algebraic; the continuous Brillouin claim is a deterministic finite scan, not an interval theorem")
    print("physical_boundary: alpha=1/1024, the flat background, Euclidean signature, and the geometry action remain supplied fixtures rather than a selected realized gravity law")

    checks.check(
        "source-and-premise-boundary",
        "the current foundation supplies neither a geometry action nor its dimensionless correction coefficient",
        "source/action and physical-observable identification" in axiom_flat
        and "Admissibility is not a dynamics axiom" in axiom_flat
        and '"kinetic_isotropy_primitive"' in registry
        and "It carries no dimensionless dynamical content" in primitives
        and "pointwise evaluation, not a state-selection rule" in primitives,
    )
    checks.check(
        "source-parent-boundary",
        "Block 19 certifies only the five-normal homogeneous constrained system and expressly leaves inhomogeneous stability open",
        "five-normal Hessian" in parent_flat
        and "inhomogeneous" in parent_flat
        and "does not select" in parent_flat,
    )
    checks.check(
        "source-regge-and-fifth-branch",
        "the retained flat carrier supplies four gauge zeros, one extra branch, and a prior projector-only repair control",
        "four massive branches" in regge_flat
        and "one exactly flat branch" in regge_flat
        and "rank-one projector onto the isolated fifth null direction" in history_flat,
    )
    checks.check(
        "source-prior-curvature-square-boundary",
        "the closest prior result establishes the local gauge-exact O(k^4) freedom but not the present branch and source repair",
        "Higher-order freedom witness" in action_selection_flat
        and "deficit-squared form" in action_selection_flat
        and "higher-curvature lattice terms exist" in action_selection_flat
        and "does not select the action at the nonlinear level" in action_selection_flat,
    )
    checks.check(
        "source-note-contract",
        "the source note lands the N1-N8 packet, candidate law wording, curved boundary, and flat repair scope",
        "No-Go Discipline Gate" in note
        and "Candidate geometry-law wording" in note
        and "1.169" in note
        and "A_h epsilon_h^2" in note_flat,
    )

    flat_lengths = np.sqrt(
        np.asarray([sum(direction) for direction in regge.DIRS15], dtype=float)
    )
    flat_kernel, flat_deficits = uniform_regge_kernel(flat_lengths)
    r2_kernel = curvature_squared_kernel(flat_lengths)
    reconstruction_error = 0.0
    for momentum in (
        np.asarray((0.0, 0.0, 0.0, 0.0)),
        np.asarray((0.31, -0.27, 0.19, 0.41)),
        np.asarray((1.1, -0.7, 0.5, 0.9)),
    ):
        reconstruction_error = max(
            reconstruction_error,
            float(np.max(np.abs(bloch(flat_kernel, momentum) - regge.bloch_Q(momentum)))),
        )
    checks.check(
        "flat-kernel-reconstruction",
        "the real-space construction reproduces the retained Regge Bloch Hessian and all fifty flat deficits vanish",
        reconstruction_error < 8.0e-13 and np.max(np.abs(flat_deficits)) < 2.0e-13,
        f"Bloch error={reconstruction_error:.3e}; max flat deficit={np.max(np.abs(flat_deficits)):.3e}",
    )

    basis = np.asarray(block19.exact_normal_basis(block19.mp), dtype=float)
    coordinates = np.asarray(
        (0.0176289114528026416711, 0.0, 0.0, 0.0, 0.1522365512153477903341)
    )
    curved_lengths = flat_lengths + basis @ coordinates
    curved_kernel, curved_deficits = uniform_regge_kernel(curved_lengths)
    curved_zero = bloch(curved_kernel, np.zeros(4))
    parent_jet = block19.normal_action(
        [block19.mp.mpf(str(value)) for value in coordinates],
        block19.exact_normal_basis(block19.mp),
    )
    parent_hessian = np.asarray(
        [[float(value) for value in row] for row in parent_jet.hess]
    )
    parent_error = float(
        np.max(np.abs(basis.T @ curved_zero.real @ basis - parent_hessian))
    )
    checks.check(
        "curved-k0-parent-reconstruction",
        "the inhomogeneous kernel reduces at k=0 to the independent Block-19 five-normal Hessian",
        parent_error < 2.0e-10
        and curved_deficits.min() < -0.70
        and curved_deficits.max() > 1.20,
        f"Hessian error={parent_error:.3e}; deficits=[{curved_deficits.min():.9f},{curved_deficits.max():.9f}]",
    )

    rng = np.random.default_rng(22082026)
    box_vector = rng.normal(size=15)
    box_vector /= np.linalg.norm(box_vector)
    box_length = 3
    box_momentum = np.asarray((2.0 * np.pi / 3.0, 2.0 * np.pi / 3.0, 0.0, 0.0))
    background_delta = curved_lengths - flat_lengths

    def curved_eps(scale):
        def evaluate(edge_class, anchor):
            return background_delta[edge_class] + scale * box_vector[edge_class] * np.cos(
                np.dot(box_momentum, anchor)
            )

        return evaluate

    step = 2.0e-4
    box_plus = regge.box_action(box_length, curved_eps(step))
    box_center = regge.box_action(box_length, curved_eps(0.0))
    box_minus = regge.box_action(box_length, curved_eps(-step))
    box_second = (box_plus - 2.0 * box_center + box_minus) / (step * step)
    box_prediction = (
        box_length**4
        / 2.0
        * float(box_vector @ bloch(curved_kernel, box_momentum).real @ box_vector)
    )
    box_relative = abs(box_second - box_prediction) / max(abs(box_prediction), 1.0e-12)
    checks.check(
        "curved-periodic-action-validation",
        "an independent periodic L=3 action second difference reproduces the finite-momentum curved Hessian",
        box_relative < 7.0e-5,
        f"finite difference={box_second:.9f}; prediction={box_prediction:.9f}; relative={box_relative:.3e}",
    )

    full_root, full_bracket, full_root_values = determinant_root(
        curved_kernel, 1.16, 1.18
    )
    full_left_values = np.linalg.eigvalsh(
        bloch(curved_kernel, np.asarray((1.16, 1.16, 0.0, 0.0)))
    )
    full_right_values = np.linalg.eigvalsh(
        bloch(curved_kernel, np.asarray((1.18, 1.18, 0.0, 0.0)))
    )
    checks.check(
        "curved-global-constraint-soft-mode",
        "the globally constrained interpretation numerically brackets a full-Hessian spatial soft-mode crossing on the named background",
        full_bracket[0] * full_bracket[1] < 0.0
        and inertia(full_left_values) != inertia(full_right_values)
        and np.min(np.abs(full_root_values)) < 2.0e-11
        and abs(full_root - 1.1694470624) < 2.0e-9,
        f"root={full_root:.12f}; determinant bracket=({full_bracket[0]:.6e},{full_bracket[1]:.6e}); endpoint inertias={inertia(full_left_values)}/{inertia(full_right_values)}",
    )

    normal_root, normal_bracket, normal_root_values = determinant_root(
        curved_kernel, 2.42, 2.43, basis=basis
    )
    normal_left = np.linalg.eigvalsh(
        basis.T
        @ bloch(curved_kernel, np.asarray((2.42, 2.42, 0.0, 0.0)))
        @ basis
    )
    normal_right = np.linalg.eigvalsh(
        basis.T
        @ bloch(curved_kernel, np.asarray((2.43, 2.43, 0.0, 0.0)))
        @ basis
    )
    checks.check(
        "curved-pointwise-affine-soft-mode",
        "the pointwise extension of the five-normal affine surface numerically brackets a distinct spatial soft-mode crossing",
        normal_bracket[0] * normal_bracket[1] < 0.0
        and inertia(normal_left) != inertia(normal_right)
        and np.min(np.abs(normal_root_values)) < 2.0e-11
        and abs(normal_root - 2.4250409952) < 2.0e-9,
        f"root={normal_root:.12f}; determinant bracket=({normal_bracket[0]:.6e},{normal_bracket[1]:.6e}); endpoint inertias={inertia(normal_left)}/{inertia(normal_right)}",
    )

    q0 = bloch(flat_kernel, np.zeros(4))
    r20 = bloch(r2_kernel, np.zeros(4))
    exact_extra_lift = exact_extra_curvature_square_hessian()
    repaired_zero = q0 + ALPHA * r20
    metric_zero = regge.metric_map(np.zeros(4))
    extra_zero = np.asarray(
        [float(value) for value in block19.exact_symmetric_vectors(block19.mp)[1]]
    )
    extra_zero /= np.linalg.norm(extra_zero)
    extra_lift_zero = float(extra_zero @ r20.real @ extra_zero)
    metric_r2_residual = float(np.max(np.abs(r20 @ metric_zero)))
    checks.check(
        "flat-curvature-square-k0-lift",
        "the local curvature-square action lifts only the extra k=0 branch while retaining all ten constant-metric zeros",
        inertia(np.linalg.eigvalsh(q0)) == (4, 0, 11)
        and inertia(np.linalg.eigvalsh(repaired_zero)) == (4, 1, 10)
        and exact_extra_lift == 768 + 384 * sp.sqrt(2)
        and extra_lift_zero > 1300.0
        and metric_r2_residual < 1.0e-10,
        f"exact extra lift={exact_extra_lift}; numeric={extra_lift_zero:.9f}; metric residual={metric_r2_residual:.3e}; repaired inertia={inertia(np.linalg.eigvalsh(repaired_zero))}",
    )

    action_vector = rng.normal(size=15)
    action_vector /= np.linalg.norm(action_vector)
    action_momentum = np.asarray((2.0 * np.pi / 3.0, 0.0, 0.0, 0.0))

    def flat_eps(scale):
        def evaluate(edge_class, anchor):
            return scale * action_vector[edge_class] * np.cos(
                np.dot(action_momentum, anchor)
            )

        return evaluate

    action_step = 1.0e-4
    total_values = []
    for scale in (action_step, 0.0, -action_step):
        eps = flat_eps(scale)
        total_values.append(
            regge.box_action(3, eps) + ALPHA * box_curvature_square(3, eps)
        )
    action_second = (
        total_values[0] - 2.0 * total_values[1] + total_values[2]
    ) / action_step**2
    action_prediction = (
        3**4
        / 2.0
        * float(
            action_vector
            @ (
                bloch(flat_kernel, action_momentum)
                + ALPHA * bloch(r2_kernel, action_momentum)
            ).real
            @ action_vector
        )
    )
    action_relative = abs(action_second - action_prediction) / max(
        abs(action_prediction), 1.0e-12
    )
    checks.check(
        "extended-periodic-action-validation",
        "the actual periodic Regge-plus-curvature-square action reproduces the repaired Bloch Hessian",
        action_relative < 1.5e-4,
        f"finite difference={action_second:.9f}; prediction={action_prediction:.9f}; relative={action_relative:.3e}",
    )

    body_momentum = np.asarray((0.3, 0.2, -0.1, -0.4))
    body_source = np.zeros(15, dtype=complex)
    body_source[regge.DIR_IDX[tuple(BODY)]] = 2.0
    body_q = bloch(flat_kernel, body_momentum)
    body_r2 = bloch(r2_kernel, body_momentum)
    body_repaired = body_q + ALPHA * body_r2
    body_gauge = regge.gauge_map(body_momentum)
    body_ward = float(np.linalg.norm(body_gauge.conjugate().T @ body_source.conjugate()))
    bare_solution = -np.linalg.pinv(body_q, rcond=1.0e-10) @ body_source.conjugate()
    repaired_solution = -np.linalg.pinv(body_repaired, rcond=1.0e-10) @ body_source.conjugate()
    bare_residual = float(np.linalg.norm(body_q @ bare_solution + body_source.conjugate()))
    repaired_residual = float(
        np.linalg.norm(body_repaired @ repaired_solution + body_source.conjugate())
    )
    repaired_gauge = float(np.max(np.abs(body_repaired @ body_gauge)))
    checks.check(
        "body-source-action-native-repair",
        "the same gauge-compatible body source rejected by the fifth branch becomes solvable without an inserted projector",
        body_ward < 1.0e-14
        and bare_residual > 1.9
        and repaired_residual < 2.0e-12
        and repaired_gauge < 1.0e-12
        and inertia(np.linalg.eigvalsh(body_repaired)) == (9, 2, 4),
        f"Ward={body_ward:.3e}; bare={bare_residual:.9f}; repaired={repaired_residual:.3e}; gauge={repaired_gauge:.3e}",
    )

    finite_modes = 0
    finite_failures = 0
    finite_minimum_gap = np.inf
    finite_worst_gauge = 0.0
    for length in range(3, 11):
        for indices in product(range(length), repeat=4):
            if not any(indices):
                continue
            momentum = 2.0 * np.pi * np.asarray(indices, dtype=float) / length
            repaired = bloch(flat_kernel, momentum) + ALPHA * bloch(
                r2_kernel, momentum
            )
            values = np.linalg.eigvalsh(repaired)
            finite_modes += 1
            finite_failures += int(inertia(values) != (9, 2, 4))
            nonzero = np.abs(values)[np.abs(values) > TOLERANCE]
            finite_minimum_gap = min(finite_minimum_gap, float(np.min(nonzero)))
            finite_worst_gauge = max(
                finite_worst_gauge,
                float(np.max(np.abs(repaired @ regge.gauge_map(momentum)))),
            )
    checks.check(
        "finite-torus-mode-inventory",
        "all 25,308 nonzero modes on L=3 through L=10 tori have exactly four gauge zeros and no fifth branch",
        finite_modes == 25308
        and finite_failures == 0
        and finite_minimum_gap > 0.14
        and finite_worst_gauge < 2.0e-12,
        f"modes={finite_modes}; failures={finite_failures}; minimum nonzero gap={finite_minimum_gap:.9f}; gauge={finite_worst_gauge:.3e}",
    )

    scan_points = list(rng.uniform(-np.pi, np.pi, size=(4096, 4)))
    scan_points.extend(
        np.asarray(point, dtype=float)
        for point in product((0.0, np.pi), repeat=4)
        if any(point)
    )
    for template in (
        (1.0, 0.0, 0.0, 0.0),
        (1.0, 1.0, 0.0, 0.0),
        (1.0, -1.0, 0.0, 0.0),
        (1.0, 1.0, 1.0, 0.0),
        (1.0, 1.0, -1.0, 0.0),
        (1.0, 1.0, 1.0, 1.0),
    ):
        scan_points.extend(
            np.asarray(template) * value
            for value in np.linspace(0.005, np.pi, 512)
        )
    scan_failures = 0
    scan_worst_gauge = 0.0
    scan_minimum_lift = np.inf
    for momentum in scan_points:
        q = bloch(flat_kernel, momentum)
        r2 = bloch(r2_kernel, momentum)
        repaired = q + ALPHA * r2
        scan_failures += int(inertia(np.linalg.eigvalsh(repaired)) != (9, 2, 4))
        gauge = regge.gauge_map(momentum)
        scan_worst_gauge = max(
            scan_worst_gauge, float(np.max(np.abs(repaired @ gauge)))
        )
        extra = extra_direction(q, gauge)
        scan_minimum_lift = min(
            scan_minimum_lift,
            float(np.real(extra.conjugate() @ r2 @ extra)),
        )
    checks.check(
        "bounded-brillouin-stress-scan",
        "the repair retains four gauge zeros and lifts the extra branch across every declared random, corner, and high-symmetry sample",
        len(scan_points) == 7183
        and scan_failures == 0
        and scan_worst_gauge < 2.0e-12
        and scan_minimum_lift > 500.0,
        f"samples={len(scan_points)}; failures={scan_failures}; minimum extra lift={scan_minimum_lift:.9f}; gauge={scan_worst_gauge:.3e}",
    )

    infrared_direction = np.asarray((0.37, -0.21, 0.43, 0.19))
    infrared_direction /= np.linalg.norm(infrared_direction)
    metric_components = np.asarray(
        (0.3, -0.2, 0.1, 0.4, -0.1, 0.2, 0.3, -0.4, 0.15, 0.25)
    )
    infrared_ratios = []
    for scale in (1.0e-2, 5.0e-3, 2.5e-3):
        momentum = scale * infrared_direction
        metric = regge.metric_map(momentum)
        vector = metric @ metric_components
        leading = float(abs(vector.conjugate() @ bloch(flat_kernel, momentum) @ vector))
        correction = float(
            abs(ALPHA * vector.conjugate() @ bloch(r2_kernel, momentum) @ vector)
        )
        infrared_ratios.append(correction / leading)
    checks.check(
        "infrared-einstein-order-preservation",
        "the curvature-square correction is O(k^4) on metric perturbations and leaves the leading O(k^2) Einstein pole unchanged",
        infrared_ratios[0] < 5.0e-7
        and 0.23 < infrared_ratios[1] / infrared_ratios[0] < 0.27
        and 0.23 < infrared_ratios[2] / infrared_ratios[1] < 0.27,
        "ratios=" + ",".join(f"{value:.3e}" for value in infrared_ratios),
    )

    print("per_element: checked all fifteen actual edge classes in both local action Hessians and the repaired body-edge source")
    print("per_site: checked every one of fifty hinge classes and all two-hundred-forty dihedral incidences per translation cell")
    print("per_mode: checked two curved spatial soft-mode brackets plus 25,308 exhaustive torus modes and 7,183 stress samples")
    print("per_block: checked the Block-19 nonflat background, the flat repaired background, and their distinct constraint interpretations")
    print("lattice_wide: checked complete L=3 through L=10 periodic spectra and independent L=3 action reconstructions without source projection")

    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return int(checks.failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
