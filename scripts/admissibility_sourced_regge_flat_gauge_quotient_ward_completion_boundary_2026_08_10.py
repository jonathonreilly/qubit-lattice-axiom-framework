#!/usr/bin/env python3
"""Test the inherited flat-gauge quotient on the sourced Regge background.

Block 21 proves that a constant five-normal localization cannot be repaired by
retuning the one curvature-square coefficient.  This runner tests a distinct,
momentum-covariant alternative: the orthogonal complement of the inherited
flat vertex-displacement map.  It also constructs the unique Frobenius-nearest
Hermitian Ward completion (I-P)Q(I-P).

The construction escapes Block 21's two high-momentum witnesses but develops
four numerical inertia crossings on one sourced infrared path.  It is not a
background-dependent gauge law, a local source connection, a continuous-zone
theorem, or a gravity no-go.
"""

from __future__ import annotations

from collections import Counter
from itertools import product
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import admissibility_fixed_metric_nonlinear_regge_kkt_continuation_2026_08_10 as block19  # noqa: E402
import admissibility_flat_regge_curvature_squared_branch_lift_2026_08_10 as block20  # noqa: E402
import admissibility_regge_curvature_squared_nonflat_continuation_2026_08_10 as block21  # noqa: E402
import frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09 as regge  # noqa: E402


AUDIT_TIMEOUT_SEC = 240
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_SOURCED_REGGE_FLAT_GAUGE_QUOTIENT_WARD_COMPLETION_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
PARENT_NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_REGGE_CURVATURE_SQUARED_SOURCED_CONTINUATION_"
    "CONSTRAINT_LOCALIZATION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
PREMISE_REGISTRY_PATH = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
PRIMITIVE_PATHS = (
    ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md",
    ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
)

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_SOURCED_REGGE_FLAT_GAUGE_QUOTIENT_WARD_COMPLETION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_REGGE_CURVATURE_SQUARED_SOURCED_CONTINUATION_CONSTRAINT_LOCALIZATION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
    "scripts/admissibility_regge_curvature_squared_nonflat_continuation_2026_08_10.py",
    "scripts/admissibility_fixed_metric_nonlinear_regge_kkt_continuation_2026_08_10.py",
    "scripts/admissibility_flat_regge_curvature_squared_branch_lift_2026_08_10.py",
    "scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py",
)

TOLERANCE = 1.0e-8
GENERIC_DIRECTION = np.asarray((1.0, 0.7, -0.4, 0.2))
LOWER_MOMENTUM = np.asarray(
    (2.0 * np.pi / 3.0, -np.pi / 2.0, 2.0 * np.pi / 3.0, -np.pi / 2.0)
)
UPPER_MOMENTUM = np.asarray(
    (0.0, 3.0 * np.pi / 4.0, 3.0 * np.pi / 4.0, 3.0 * np.pi / 4.0)
)
EXPECTED_ROOTS = np.asarray(
    (0.0512802589684685, 0.0698870072573606, 0.0887158958882546, 0.204407087874502)
)
EXPECTED_PATH_INERTIAS = (
    (7, 4, 0),
    (8, 3, 0),
    (9, 2, 0),
    (10, 1, 0),
    (9, 2, 0),
)
EXPECTED_STRESS_COUNTS = Counter(
    {
        (6, 5, 0): 6,
        (7, 4, 0): 35,
        (8, 3, 0): 19,
        (9, 2, 0): 11150,
        (10, 1, 0): 69,
    }
)


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


def projector(gauge):
    gram = gauge.conjugate().T @ gauge
    out = gauge @ np.linalg.solve(gram, gauge.conjugate().T)
    return 0.5 * (out + out.conjugate().T)


def reduced_record(kernel, momentum):
    q = block20.bloch(kernel, np.asarray(momentum, dtype=float))
    gauge = regge.gauge_map(np.asarray(momentum, dtype=float))
    quotient = block20.gauge_quotient_basis(gauge)
    reduced = quotient.conjugate().T @ q @ quotient
    values = np.linalg.eigvalsh(reduced)
    return q, gauge, quotient, reduced, values


def make_kernel(lengths):
    """Complete Einstein-plus-curvature-square kernel at uniform lengths."""
    regge_kernel, _ = block20.uniform_regge_kernel(lengths)
    curvature_kernel = block21.curvature_squared_kernel(lengths)
    return block21.combine_kernels(regge_kernel, curvature_kernel)


def leading_flat_gauge(direction):
    """Coefficient of x in the exact flat gauge map G_0(x direction)."""
    out = np.zeros((15, 4), dtype=complex)
    for index, vector in enumerate(regge.DIRS15):
        vector = np.asarray(vector, dtype=float)
        out[index, :] = (
            1j
            * np.dot(direction, vector)
            * vector
            / np.linalg.norm(vector)
        )
    return out


def matrix_inertia(matrix, tolerance=1.0e-8):
    values = np.linalg.eigvalsh(matrix)
    return (
        int(np.sum(values < -tolerance)),
        int(np.sum(values > tolerance)),
        int(np.sum(np.abs(values) <= tolerance)),
    ), values


def even_low_schur(kernel, complement, low, high, value):
    """Even path Schur complement divided by x^2 on the six flat zero modes."""
    records = []
    for sign in (-1.0, 1.0):
        reduced = complement.conjugate().T @ block20.bloch(
            kernel, sign * value * GENERIC_DIRECTION
        ) @ complement
        low_low = low.conjugate().T @ reduced @ low
        low_high = low.conjugate().T @ reduced @ high
        high_high = high.conjugate().T @ reduced @ high
        records.append(
            low_low
            - low_high
            @ np.linalg.solve(high_high, low_high.conjugate().T)
        )
    return 0.5 * (records[0] + records[1]) / (value * value)


def positive_pencil_ratios(mass, kinetic):
    """Positive real rho from det(M + rho^2 K)=0."""
    roots = np.linalg.eigvals(-np.linalg.solve(kinetic, mass))
    positive = np.sort(
        roots.real[
            (np.abs(roots.imag) < 1.0e-7)
            & (roots.real > 0.0)
        ]
    )
    return np.sqrt(positive)


def strict_inertia(values, tolerance=1.0e-11):
    return (
        int(np.sum(values < -tolerance)),
        int(np.sum(values > tolerance)),
        int(np.sum(np.abs(values) <= tolerance)),
    )


def path_determinant(kernel, value):
    *_, reduced, _values = reduced_record(kernel, value * GENERIC_DIRECTION)
    return float(np.linalg.det(reduced).real)


def bisect_root(kernel, left, right):
    left_value = path_determinant(kernel, left)
    right_value = path_determinant(kernel, right)
    if left_value * right_value >= 0:
        raise AssertionError("determinant bracket does not change sign")
    initial = (left, right)
    for _ in range(70):
        middle = 0.5 * (left + right)
        middle_value = path_determinant(kernel, middle)
        if left_value * middle_value <= 0:
            right = middle
            right_value = middle_value
        else:
            left = middle
            left_value = middle_value
    return 0.5 * (left + right), initial, (left_value, right_value)


def scan_path_roots(kernel, points):
    """Find simple determinant sign changes on an ordered positive path grid."""
    records = []
    left = float(points[0])
    left_det = path_determinant(kernel, left)
    for raw_right in points[1:]:
        right = float(raw_right)
        right_det = path_determinant(kernel, right)
        if left_det * right_det < 0.0:
            root, bracket, signs = bisect_root(kernel, left, right)
            delta = max(1.0e-10, root * 1.0e-4)
            before = strict_inertia(
                reduced_record(kernel, (root - delta) * GENERIC_DIRECTION)[-1]
            )
            after = strict_inertia(
                reduced_record(kernel, (root + delta) * GENERIC_DIRECTION)[-1]
            )
            records.append((root, before, after, bracket, signs))
        left = right
        left_det = right_det
    return records


def main():
    block21.mp.mp.dps = 40
    block21.iv.dps = 35
    checks = Checks()

    note = NOTE_PATH.read_text(encoding="utf-8")
    note_flat = " ".join(note.lower().split())
    axiom_flat = AXIOM_PATH.read_text(encoding="utf-8").lower()
    parent_note = PARENT_NOTE_PATH.read_text(encoding="utf-8")
    registry = PREMISE_REGISTRY_PATH.read_text(encoding="utf-8")
    primitives = [path.read_text(encoding="utf-8") for path in PRIMITIVE_PATHS]

    print("external_scientific_inputs: none; the quotient, Ward completion, roots, and stress inventory are reconstructed from repository-local Regge data")
    print("package_local_integrity_reads: current axioms, approved primitives, Block 21, and the retained Regge carrier are source-bound")
    print("analytic_boundary: the projector identity is algebraic; tangent spectra, weak-source scaling, and finite-source path roots are double-precision numerical results")
    print("physical_boundary: the inherited flat gauge map, Euclidean signature, homogeneous external-source branches, action, and coefficient remain supplied fixtures")

    checks.check(
        "source-and-axiom-boundary",
        "the current foundation does not select the sourced gauge/constraint connection",
        "admissibility is not a dynamics axiom" in axiom_flat
        and "source/action and physical-observable identification" in axiom_flat
        and "not a covariant-gravity no-go" in note_flat,
    )
    checks.check(
        "source-note-contract",
        "the note states both the witness escape and the four-crossing inherited-gauge boundary",
        "0.051280258968" in note
        and "0.204407087875" in note
        and "O(k^0)" in note
        and "square-root crossover law" in note
        and "8,749" in note
        and "(i-p) q (i-p)" in note_flat
        and "n1--n8 status: `pass` only" in note_flat
        and "`kinetic_isotropy_primitive`" in note,
    )
    checks.check(
        "source-parent-carrier",
        "Block 21 supplies the interval-certified source and the fixed-N no-overlap being tested",
        "radius-`2e-9`" in parent_note
        and "alpha>21/4096" in parent_note
        and all(name in registry for name in ("minimal_axioms", "scale_reference_primitive", "kinetic_isotropy_primitive", "realized_state_primitive"))
        and all(text.strip() for text in primitives),
    )

    exact_basis = block19.exact_normal_basis(block21.mp)
    basis = np.asarray(exact_basis, dtype=float)
    source = block19.reaction.exact_source_rows()[-1]
    coordinates, source_jet, source_residual, source_iterations = block21.solve_source(
        source, block21.sp.Rational(1, 100), exact_basis
    )
    flat_lengths = np.sqrt(
        np.asarray([sum(direction) for direction in regge.DIRS15], dtype=float)
    )
    lengths = flat_lengths + basis @ np.asarray(coordinates, dtype=float)
    regge_kernel, deficits = block20.uniform_regge_kernel(lengths)
    curvature_kernel = block21.curvature_squared_kernel(lengths)
    kernel = block21.combine_kernels(regge_kernel, curvature_kernel)
    source_coordinates = np.asarray(coordinates, dtype=float)
    expected_coordinates = np.asarray(
        (-0.0002118903455527, 0.0012366779546983, 0.0012366779546975, 0.0012366779546977, 0.0093762842804963)
    )
    checks.check(
        "bundle-b-source-reconstruction",
        "the Block-21 Bundle-B stationary point is independently reconstructed before quotienting",
        source_residual < block21.mp.mpf("1e-25")
        and np.max(np.abs(source_coordinates - expected_coordinates)) < 2.0e-14
        and block20.inertia(np.linalg.eigvalsh(np.asarray(source_jet.hess, dtype=float))) == (4, 1, 0)
        and np.max(np.abs(deficits)) > 0.05,
        f"residual={block21.mp.nstr(source_residual, 4)}; iterations={source_iterations}; deficit max={np.max(np.abs(deficits)):.6f}",
    )

    # The x -> 0 quotient has five massive directions and six flat physical
    # zero modes.  Its Schur complement supplies the O(x^2) kinetic matrix.
    flat_kernel = make_kernel(flat_lengths)
    leading_gauge = leading_flat_gauge(GENERIC_DIRECTION)
    leading_gauge_basis = block20.orthonormal_columns(leading_gauge)
    leading_complement = block20.gauge_quotient_basis(leading_gauge)
    flat_zero_symbol = block20.bloch(flat_kernel, np.zeros(4))
    flat_reduced_zero = (
        leading_complement.conjugate().T
        @ flat_zero_symbol
        @ leading_complement
    )
    flat_values, flat_vectors = np.linalg.eigh(flat_reduced_zero)
    zero_mask = np.abs(flat_values) < 1.0e-8
    low = flat_vectors[:, zero_mask]
    high = flat_vectors[:, ~zero_mask]
    physical = leading_complement @ low
    kinetic_coarse = even_low_schur(
        flat_kernel, leading_complement, low, high, 2.0e-3
    )
    kinetic_fine = even_low_schur(
        flat_kernel, leading_complement, low, high, 1.0e-3
    )
    kinetic = (4.0 * kinetic_fine - kinetic_coarse) / 3.0
    kinetic_inertia, kinetic_values = matrix_inertia(kinetic, 1.0e-7)
    kinetic_relative_step = float(
        np.linalg.norm(kinetic_fine - kinetic_coarse, 2)
        / np.linalg.norm(kinetic, 2)
    )
    flat_ward_residual = float(
        np.linalg.norm(flat_zero_symbol @ leading_gauge, 2)
    )
    checks.check(
        "flat-connected-six-mode-kinetic-limit",
        "the inherited flat quotient has six massless physical directions with the intended five-negative/one-positive O(k^2) kinetic form",
        leading_gauge_basis.shape[1] == 4
        and leading_complement.shape[1] == 11
        and low.shape[1] == 6
        and high.shape[1] == 5
        and kinetic_inertia == (5, 1, 0)
        and np.min(np.abs(kinetic_values)) > 0.65
        and kinetic_relative_step < 2.0e-6
        and flat_ward_residual < 1.0e-10,
        f"rank={leading_gauge_basis.shape[1]}; low/massive={low.shape[1]}/{high.shape[1]}; kinetic={kinetic_inertia}; minimum |eigenvalue|={np.min(np.abs(kinetic_values)):.6f}; step ratio={kinetic_relative_step:.3e}",
    )

    # Differentiate each stationary source branch at zero coupling.  If z is
    # the five-normal coordinate and t the retained source target, then
    # z'(0)=H_N(0)^(-1)t.  Centered length perturbations reconstruct the
    # induced O(coupling) Hessian coefficient without fitting a prefactor.
    flat_normal = block21.normal_action(
        [block21.mp.mpf(0) for _ in range(5)], exact_basis
    )
    flat_normal_hessian = block21.mp.matrix(flat_normal.hess)
    labels = ("two-stream", "bundle-A", "bundle-B")
    expected_mass_inertias = ((3, 3, 0), (4, 2, 0), (2, 4, 0))
    expected_ir_inertias = ((7, 4, 0), (8, 3, 0), (6, 5, 0))
    expected_root_counts = (2, 1, 3)
    small_coupling = block21.sp.Rational(1, 100000)
    small_coupling_float = float(small_coupling)
    small_root_grid = np.geomspace(1.0e-7, 1.0e-2, 1200)
    source_records = []
    for label, source_row in zip(labels, block19.reaction.exact_source_rows()):
        target = block19.exact_source_target(
            source_row, block21.sp.Rational(1, 1), block21.mp
        )
        tangent_coordinates = block21.mp.lu_solve(
            flat_normal_hessian, target
        )
        tangent_lengths = basis @ np.asarray(
            tangent_coordinates, dtype=float
        ).reshape(5)
        derivatives = []
        for step in (1.0e-4, 5.0e-5):
            plus = make_kernel(flat_lengths + step * tangent_lengths)
            minus = make_kernel(flat_lengths - step * tangent_lengths)
            derivatives.append(
                (
                    block20.bloch(plus, np.zeros(4))
                    - block20.bloch(minus, np.zeros(4))
                )
                / (2.0 * step)
            )
        derivative = (4.0 * derivatives[1] - derivatives[0]) / 3.0
        derivative_relative_step = float(
            np.linalg.norm(derivatives[1] - derivatives[0], 2)
            / np.linalg.norm(derivative, 2)
        )
        mass = physical.conjugate().T @ derivative @ physical
        mass_inertia, mass_values = matrix_inertia(mass, 1.0e-7)
        predicted_ratios = positive_pencil_ratios(mass, kinetic)

        small_coordinates, _small_jet, small_residual, _small_iterations = (
            block21.solve_source(source_row, small_coupling, exact_basis)
        )
        small_lengths = flat_lengths + basis @ np.asarray(
            small_coordinates, dtype=float
        )
        small_kernel = make_kernel(small_lengths)
        small_roots = scan_path_roots(small_kernel, small_root_grid)
        actual_ratios = np.asarray(
            [record[0] for record in small_roots]
        ) / np.sqrt(small_coupling_float)
        small_difference = (
            block20.bloch(small_kernel, np.zeros(4)) - flat_zero_symbol
        ) / small_coupling_float
        actual_mass = physical.conjugate().T @ small_difference @ physical
        actual_mass_relative = float(
            np.linalg.norm(actual_mass - mass, 2)
            / np.linalg.norm(mass, 2)
        )
        ward_derivative = float(np.linalg.norm(derivative @ leading_gauge, 2))
        ward_actual = float(np.linalg.norm(small_difference @ leading_gauge, 2))
        ward_relative = abs(ward_actual - ward_derivative) / ward_derivative
        ir_inertia = strict_inertia(
            reduced_record(
                small_kernel, 1.0e-6 * GENERIC_DIRECTION
            )[-1]
        )
        source_records.append(
            {
                "label": label,
                "mass_inertia": mass_inertia,
                "mass_gap": float(np.min(np.abs(mass_values))),
                "derivative_relative_step": derivative_relative_step,
                "ward_derivative": ward_derivative,
                "ward_relative": ward_relative,
                "actual_mass_relative": actual_mass_relative,
                "predicted_ratios": predicted_ratios,
                "actual_ratios": actual_ratios,
                "small_roots": small_roots,
                "small_residual": small_residual,
                "ir_inertia": ir_inertia,
            }
        )

    checks.check(
        "three-source-O-k0-mass-splitting",
        "the three retained sourced branch tangents generate nonzero O(k^0) physical mass matrices with source-dependent wrong infrared inertias",
        tuple(record["mass_inertia"] for record in source_records)
        == expected_mass_inertias
        and min(record["mass_gap"] for record in source_records) > 0.025
        and max(record["derivative_relative_step"] for record in source_records)
        < 1.0e-6
        and min(record["ward_derivative"] for record in source_records) > 5.0,
        "; ".join(
            f"{record['label']}: mass={record['mass_inertia']}, gap={record['mass_gap']:.6f}, Ward slope={record['ward_derivative']:.6f}"
            for record in source_records
        ),
    )
    checks.check(
        "weak-source-square-root-crossovers",
        "the generalized pencils predict every positive-coupling infrared crossing and direct coupling-1e-5 roots follow k proportional to sqrt(coupling)",
        tuple(len(record["small_roots"]) for record in source_records)
        == expected_root_counts
        and all(
            len(record["predicted_ratios"]) == expected_root_counts[index]
            and np.max(
                np.abs(
                    record["actual_ratios"]
                    - record["predicted_ratios"]
                )
            )
            < 2.0e-3
            for index, record in enumerate(source_records)
        ),
        "; ".join(
            f"{record['label']}: predicted={np.round(record['predicted_ratios'], 6).tolist()}, actual={np.round(record['actual_ratios'], 6).tolist()}"
            for record in source_records
        ),
    )
    checks.check(
        "weak-source-direct-Ward-scaling",
        "direct nonlinear source branches reproduce the tangent mass matrices, Ward defects, and three non-target infrared chambers",
        tuple(record["ir_inertia"] for record in source_records)
        == expected_ir_inertias
        and max(record["actual_mass_relative"] for record in source_records)
        < 5.0e-4
        and max(record["ward_relative"] for record in source_records) < 5.0e-4
        and all(
            record["small_residual"] < block21.mp.mpf("1e-24")
            for record in source_records
        ),
        "; ".join(
            f"{record['label']}: IR={record['ir_inertia']}, mass error={record['actual_mass_relative']:.3e}, Ward error={record['ward_relative']:.3e}"
            for record in source_records
        ),
    )

    witness_records = [reduced_record(kernel, momentum) for momentum in (LOWER_MOMENTUM, UPPER_MOMENTUM)]
    witness_inertias = [block20.inertia(record[-1]) for record in witness_records]
    witness_gaps = [float(np.min(np.abs(record[-1]))) for record in witness_records]
    witness_ward = [float(np.linalg.norm(record[0] @ record[1], ord=2)) for record in witness_records]
    checks.check(
        "flat-gauge-quotient-witness-escape",
        "the momentum-covariant inherited-gauge quotient escapes both fixed-N high-momentum witnesses",
        witness_inertias == [(9, 2, 0), (9, 2, 0)]
        and min(witness_gaps) > 0.12,
        f"inertias={witness_inertias}; gaps={[f'{value:.9f}' for value in witness_gaps]}",
    )
    checks.check(
        "inherited-flat-gauge-ward-defect",
        "the sourced geometry Hessian does not annihilate the inherited flat vertex-displacement map",
        min(witness_ward) > 0.4,
        f"witness spectral defects={[f'{value:.9f}' for value in witness_ward]}",
    )

    completion_errors = []
    completion_inertias = []
    for momentum in (LOWER_MOMENTUM, UPPER_MOMENTUM, 0.02 * GENERIC_DIRECTION):
        q, gauge, quotient, _reduced, values = reduced_record(kernel, momentum)
        p = projector(gauge)
        complement = np.eye(15) - p
        completed = complement @ q @ complement
        completed = 0.5 * (completed + completed.conjugate().T)
        completed_values = np.linalg.eigvalsh(completed)
        completed_nonzero = completed_values[np.abs(completed_values) > TOLERANCE]
        errors = (
            np.max(np.abs(p @ p - p)),
            np.max(np.abs(completed @ gauge)),
            np.max(np.abs(completed_nonzero - values)),
            np.max(np.abs(completed - completed.conjugate().T)),
        )
        completion_errors.append(max(float(value) for value in errors))
        completion_inertias.append(block20.inertia(completed_values))
    checks.check(
        "frobenius-nearest-hermitian-ward-completion",
        "(I-P)Q(I-P) has the inherited gauge kernel and exactly the quotient nonzero spectrum",
        max(completion_errors) < 2.0e-10
        and completion_inertias[:2] == [(9, 2, 4), (9, 2, 4)]
        and completion_inertias[2] == (7, 4, 4),
        f"maximum algebra/spectrum error={max(completion_errors):.3e}; inertias={completion_inertias}",
    )

    path_points = np.concatenate(
        (np.geomspace(1.0e-5, 0.1, 512), np.linspace(0.1, np.pi, 2048)[1:])
    )
    transitions = []
    brackets = []
    prior_inertia = None
    prior_x = None
    path_minimum_gap = np.inf
    path_maximum_ward = 0.0
    for value in path_points:
        q, gauge, _quotient, _reduced, values = reduced_record(
            kernel, value * GENERIC_DIRECTION
        )
        inertia = block20.inertia(values)
        if np.linalg.matrix_rank(gauge, tol=1.0e-9) != 4:
            raise AssertionError("inherited gauge rank changed on declared path")
        path_minimum_gap = min(path_minimum_gap, float(np.min(np.abs(values))))
        path_maximum_ward = max(path_maximum_ward, float(np.linalg.norm(q @ gauge, ord=2)))
        if inertia != prior_inertia:
            transitions.append(inertia)
            if prior_inertia is not None:
                brackets.append(bisect_root(kernel, float(prior_x), float(value)))
            prior_inertia = inertia
        prior_x = value
    roots = np.asarray([record[0] for record in brackets])
    root_signs = [record[2][0] * record[2][1] <= 0 for record in brackets]
    checks.check(
        "generic-path-four-crossing-sequence",
        "the inherited-gauge quotient has four simple numerical inertia crossings on the named sourced path",
        tuple(transitions) == EXPECTED_PATH_INERTIAS
        and len(roots) == 4
        and np.max(np.abs(roots - EXPECTED_ROOTS)) < 2.0e-10
        and all(root_signs),
        "roots=" + ",".join(f"{value:.12f}" for value in roots) + f"; inertias={transitions}",
    )

    stress_points = []
    for template in (
        (1.0, 0.0, 0.0, 0.0),
        (1.0, 1.0, 0.0, 0.0),
        (1.0, -1.0, 0.0, 0.0),
        (1.0, 1.0, 1.0, 0.0),
        (1.0, 1.0, -1.0, 0.0),
        (1.0, 1.0, 1.0, 1.0),
    ):
        stress_points.extend(
            np.asarray(template) * value for value in np.linspace(0.005, np.pi, 512)
        )
    stress_points.extend(
        np.asarray(point, dtype=float)
        for point in product((0.0, np.pi), repeat=4)
        if any(point)
    )
    rng = np.random.default_rng(22082026)
    stress_points.extend(rng.uniform(-np.pi, np.pi, size=(8192, 4)))
    stress_counts = Counter()
    stress_minimum_gap = np.inf
    for momentum in stress_points:
        _q, gauge, _quotient, _reduced, values = reduced_record(kernel, momentum)
        if np.linalg.matrix_rank(gauge, tol=1.0e-9) != 4:
            raise AssertionError("inherited gauge rank changed on stress inventory")
        stress_counts[block20.inertia(values)] += 1
        stress_minimum_gap = min(stress_minimum_gap, float(np.min(np.abs(values))))
    checks.check(
        "bounded-stress-inertia-inventory",
        "the deterministic sourced quotient inventory contains five inertia chambers rather than a uniform target chamber",
        len(stress_points) == 11279
        and stress_counts == EXPECTED_STRESS_COUNTS
        and stress_minimum_gap > 6.0e-6
        and path_maximum_ward > 0.54,
        f"points={len(stress_points)}; counts={dict(stress_counts)}; minimum gap={stress_minimum_gap:.3e}; maximum Ward defect={path_maximum_ward:.6f}",
    )
    torus_modes = 0
    torus_failures = 0
    torus_minimum_gap = np.inf
    for length in range(3, 9):
        for index in product(range(length), repeat=4):
            if not any(index):
                continue
            momentum = 2.0 * np.pi * np.asarray(index, dtype=float) / length
            momentum = (momentum + np.pi) % (2.0 * np.pi) - np.pi
            values = reduced_record(kernel, momentum)[-1]
            inertia = block20.inertia(values)
            torus_modes += 1
            torus_failures += int(inertia != (9, 2, 0))
            torus_minimum_gap = min(
                torus_minimum_gap, float(np.min(np.abs(values)))
            )
    checks.check(
        "finite-torus-infrared-aliasing",
        "all L=3 through L=8 quotient modes miss the narrow sourced infrared chambers found by the continuum-path probe",
        torus_modes == 8749
        and torus_failures == 0
        and torus_minimum_gap > 0.08,
        f"modes={torus_modes}; target failures={torus_failures}; minimum gap={torus_minimum_gap:.6f}",
    )
    checks.check(
        "bounded-theorem-and-no-go-scope",
        "the source licenses only the inherited-flat-gauge bounded diagnosis and preserves the covariant completion route",
        "N1--N8 status: `PASS` only" in note
        and "background-dependent gauge/source connection" in note_flat
        and "not a continuous-zone theorem" in note_flat
        and "not a covariant-gravity no-go" in note_flat,
    )

    print("per_element: checked all fifteen edge classes in the sourced action Hessian and the fifteen-dimensional Ward completion")
    print("per_site: checked all fifty hinge classes inherited by the independently reconstructed Bundle-B kernel")
    print("per_mode: checked weak-source roots, two high-momentum witnesses, four finite-source path roots, 11,279 stress points, and 8,749 torus modes")
    print("per_block: checked all three retained weak-source branches plus the interval-backed Bundle-B quotient and algebraic Ward completion")
    print("lattice_wide: checked and not executed — finite tori and sampled paths are not a continuous-zone, local source-connection, nonuniform-field, or Lorentzian theorem")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return int(checks.failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
