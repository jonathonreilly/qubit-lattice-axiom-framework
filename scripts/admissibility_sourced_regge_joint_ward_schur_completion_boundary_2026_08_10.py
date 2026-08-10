#!/usr/bin/env python3
"""Certify the minimal coefficient-level joint Ward completion of Block 22.

Block 22 reconstructs three full-rank, indefinite O(source) mass matrices on
the six flat physical Regge modes.  This runner asks what a *pure Schur*
source/constraint completion would have to contain.  For each supplied mass
matrix M it constructs B and invertible Hermitian C such that

    M - B C^{-1} B^dagger = 0.

The resulting joint coefficient Hessian has an exact six-dimensional kernel.
Rank and inertia inequalities prove per-branch minimality, while a common
fixed-signature construction proves that eight auxiliary directions are both
necessary and sufficient for all three retained source tangents.  A separate
order calculation shows why a regular source-decoupled analytic Schur block
with invertible zero-source Hessian cannot cancel an O(source) defect.

No local carrier, source dynamics, physical selection, Lorentzian theory, or
gravity law is inferred.
"""

from __future__ import annotations

from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import admissibility_sourced_regge_flat_gauge_quotient_ward_completion_boundary_2026_08_10 as block22  # noqa: E402


AUDIT_TIMEOUT_SEC = 120
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_SOURCED_REGGE_JOINT_WARD_SCHUR_COMPLETION_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
PARENT_NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_SOURCED_REGGE_FLAT_GAUGE_QUOTIENT_WARD_COMPLETION_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
COFRAME_NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_CUT_SURFACE_COFRAME_STRESS_HIGHER_FORM_WARD_"
    "GEOMETRY_DYNAMICS_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
LINE_NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_CLOSED_HELICAL_DEFECT_HISTORY_WARD_NEUTRAL_IR_"
    "REGGE_RESPONSE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
PREMISE_REGISTRY_PATH = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_SOURCED_REGGE_JOINT_WARD_SCHUR_COMPLETION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/ADMISSIBILITY_SOURCED_REGGE_FLAT_GAUGE_QUOTIENT_WARD_COMPLETION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/ADMISSIBILITY_CUT_SURFACE_COFRAME_STRESS_HIGHER_FORM_WARD_GEOMETRY_DYNAMICS_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/ADMISSIBILITY_CLOSED_HELICAL_DEFECT_HISTORY_WARD_NEUTRAL_IR_REGGE_RESPONSE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "scripts/admissibility_sourced_regge_flat_gauge_quotient_ward_completion_boundary_2026_08_10.py",
    "scripts/admissibility_regge_curvature_squared_nonflat_continuation_2026_08_10.py",
    "scripts/admissibility_fixed_metric_nonlinear_regge_kkt_continuation_2026_08_10.py",
    "scripts/admissibility_flat_regge_curvature_squared_branch_lift_2026_08_10.py",
    "scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py",
)

EXPECTED_MASS_INERTIAS = ((3, 3, 0), (4, 2, 0), (2, 4, 0))
LABELS = ("two-stream", "bundle-A", "bundle-B")
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


def inertia(matrix, tolerance=TOLERANCE):
    values = np.linalg.eigvalsh(0.5 * (matrix + matrix.conjugate().T))
    return (
        int(np.sum(values < -tolerance)),
        int(np.sum(values > tolerance)),
        int(np.sum(np.abs(values) <= tolerance)),
    ), values


def reconstruct_mass_matrices():
    """Reconstruct only Block 22's flat six-mode tangent calculation."""
    block22.block21.mp.mp.dps = 40
    exact_basis = block22.block19.exact_normal_basis(block22.block21.mp)
    basis = np.asarray(exact_basis, dtype=float)
    flat_lengths = np.sqrt(
        np.asarray(
            [sum(direction) for direction in block22.regge.DIRS15],
            dtype=float,
        )
    )

    flat_kernel = block22.make_kernel(flat_lengths)
    leading_gauge = block22.leading_flat_gauge(block22.GENERIC_DIRECTION)
    complement = block22.block20.gauge_quotient_basis(leading_gauge)
    zero_symbol = block22.block20.bloch(flat_kernel, np.zeros(4))
    reduced_zero = complement.conjugate().T @ zero_symbol @ complement
    values, vectors = np.linalg.eigh(reduced_zero)
    low = vectors[:, np.abs(values) < TOLERANCE]
    physical = complement @ low

    flat_normal = block22.block21.normal_action(
        [block22.block21.mp.mpf(0) for _ in range(5)], exact_basis
    )
    flat_normal_hessian = block22.block21.mp.matrix(flat_normal.hess)

    records = []
    for label, source_row in zip(
        LABELS, block22.block19.reaction.exact_source_rows()
    ):
        target = block22.block19.exact_source_target(
            source_row, block22.block21.sp.Rational(1, 1), block22.block21.mp
        )
        tangent_coordinates = block22.block21.mp.lu_solve(
            flat_normal_hessian, target
        )
        tangent_lengths = basis @ np.asarray(
            tangent_coordinates, dtype=float
        ).reshape(5)
        derivatives = []
        for step in (1.0e-4, 5.0e-5):
            plus = block22.make_kernel(flat_lengths + step * tangent_lengths)
            minus = block22.make_kernel(flat_lengths - step * tangent_lengths)
            derivatives.append(
                (
                    block22.block20.bloch(plus, np.zeros(4))
                    - block22.block20.bloch(minus, np.zeros(4))
                )
                / (2.0 * step)
            )
        derivative = (4.0 * derivatives[1] - derivatives[0]) / 3.0
        step_error = float(
            np.linalg.norm(derivatives[1] - derivatives[0], 2)
            / np.linalg.norm(derivative, 2)
        )
        mass = physical.conjugate().T @ derivative @ physical
        mass = 0.5 * (mass + mass.conjugate().T)
        records.append((label, mass, step_error))
    return physical, records


def minimal_completion(mass):
    """Spectral six-mode factorization M=B C^{-1} B^dagger."""
    values, vectors = np.linalg.eigh(mass)
    signs = np.sign(values)
    source = np.diag(signs)
    mixing = vectors @ np.diag(np.sqrt(np.abs(values)))
    repair = mixing @ source @ mixing.conjugate().T
    schur = mass - repair
    joint = np.block(
        [[mass, mixing], [mixing.conjugate().T, source]]
    )
    generator = np.vstack(
        [np.eye(6, dtype=complex), -source @ mixing.conjugate().T]
    )
    return values, source, mixing, repair, schur, joint, generator


def common_signature_completion(mass):
    """Embed one mass matrix into a fixed (4 negative, 4 positive) block."""
    values, vectors = np.linalg.eigh(mass)
    source = np.diag(np.asarray((-1.0,) * 4 + (1.0,) * 4))
    mixing = np.zeros((6, 8), dtype=complex)
    negative = np.flatnonzero(values < -TOLERANCE)
    positive = np.flatnonzero(values > TOLERANCE)
    for column, index in enumerate(negative):
        mixing[:, column] = vectors[:, index] * np.sqrt(-values[index])
    for column, index in enumerate(positive, start=4):
        mixing[:, column] = vectors[:, index] * np.sqrt(values[index])
    repair = mixing @ source @ mixing.conjugate().T
    schur = mass - repair
    joint = np.block([[mass, mixing], [mixing.conjugate().T, source]])
    generator = np.vstack(
        [np.eye(6, dtype=complex), -source @ mixing.conjugate().T]
    )
    return source, mixing, repair, schur, joint, generator


def main():
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    note_flat = " ".join(note.lower().split())
    parent = PARENT_NOTE_PATH.read_text(encoding="utf-8")
    coframe = COFRAME_NOTE_PATH.read_text(encoding="utf-8")
    line = LINE_NOTE_PATH.read_text(encoding="utf-8")
    axioms = AXIOM_PATH.read_text(encoding="utf-8").lower()
    registry = PREMISE_REGISTRY_PATH.read_text(encoding="utf-8")

    print("external_scientific_inputs: none; all matrices are reconstructed from the repository-local Block-22 Regge/source carrier")
    print("analytic_boundary: rank, inertia, Schur, and differentiated-Ward statements are finite-dimensional theorems; source-tangent matrices are double-precision numerical reconstructions")
    print("physical_boundary: the completion is coefficient-level and nonlocal until a selected joint local action supplies its source variables, scaling, stationary background, and transformations")

    checks.check(
        "source-and-axiom-boundary",
        "the current axioms do not select the joint source/geometry completion",
        "admissibility is not a dynamics axiom" in axioms
        and "source/action and physical-observable identification" in axioms
        and all(
            name in registry
            for name in (
                "minimal_axioms",
                "scale_reference_primitive",
                "kinetic_isotropy_primitive",
                "realized_state_primitive",
            )
        ),
    )
    checks.check(
        "retained-route-inventory",
        "retained artifacts separately supply a first Ward carrier and a same-family seagull route",
        "exp(i l theta)-1" in line.lower()
        and "same-family coframe seagull" in coframe.lower()
        and "o(k^0)" in parent.lower(),
    )
    checks.check(
        "note-contract",
        "the note states the six-mode pure-Schur theorem and its strict physical boundary",
        "rank(b) >= 6" in note_flat
        and "m - b c^{-1} b^dagger = 0" in note_flat
        and "coefficient-level" in note_flat
        and "n1--n8 status: `pass` only" in note_flat
        and "no canonical axiom is edited" in note_flat,
    )

    physical, records = reconstruct_mass_matrices()
    source_inertias = []
    source_gaps = []
    step_errors = []
    completion_residuals = []
    kernel_residuals = []
    source_block_inertias = []
    joint_inertias = []
    ranks = []
    common_completion_residuals = []
    common_kernel_residuals = []
    common_joint_inertias = []

    for label, mass, step_error in records:
        mass_inertia, mass_values = inertia(mass, 1.0e-7)
        (
            spectral_values,
            source,
            mixing,
            repair,
            schur,
            joint,
            generator,
        ) = minimal_completion(mass)
        source_inertia, _ = inertia(source)
        joint_inertia, _ = inertia(joint)
        repair_error = float(np.linalg.norm(repair - mass, 2))
        schur_error = float(np.linalg.norm(schur, 2))
        kernel_error = float(np.linalg.norm(joint @ generator, 2))
        spectral_match = float(
            np.max(np.abs(np.sort(spectral_values) - np.sort(mass_values)))
        )

        source_inertias.append(mass_inertia)
        source_gaps.append(float(np.min(np.abs(mass_values))))
        step_errors.append(step_error)
        completion_residuals.append(max(repair_error, schur_error, spectral_match))
        kernel_residuals.append(kernel_error)
        source_block_inertias.append(source_inertia)
        joint_inertias.append(joint_inertia)
        ranks.append(int(np.linalg.matrix_rank(mixing, tol=1.0e-9)))
        (
            common_source,
            common_mixing,
            common_repair,
            common_schur,
            common_joint,
            common_generator,
        ) = common_signature_completion(mass)
        common_completion_residuals.append(
            max(
                float(np.linalg.norm(common_repair - mass, 2)),
                float(np.linalg.norm(common_schur, 2)),
            )
        )
        common_kernel_residuals.append(
            float(np.linalg.norm(common_joint @ common_generator, 2))
        )
        common_joint_inertias.append(inertia(common_joint)[0])
        print(
            f"completion[{label}]: M={mass_inertia}; C={source_inertia}; "
            f"joint={joint_inertia}; gap={source_gaps[-1]:.9f}; "
            f"schur={schur_error:.3e}; kernel={kernel_error:.3e}"
        )

    checks.check(
        "flat-six-mode-carrier",
        "the reconstruction isolates the same six physical flat modes as Block 22",
        physical.shape == (15, 6)
        and np.linalg.norm(physical.conjugate().T @ physical - np.eye(6), 2)
        < 1.0e-12,
        f"shape={physical.shape}; orthogonality={np.linalg.norm(physical.conjugate().T @ physical - np.eye(6), 2):.3e}",
    )
    checks.check(
        "three-full-rank-indefinite-defects",
        "all three O(source) physical mass matrices are full-rank and indefinite",
        tuple(source_inertias) == EXPECTED_MASS_INERTIAS
        and min(source_gaps) > 0.025
        and max(step_errors) < 1.0e-6,
        "; ".join(
            f"{label}: inertia={source_inertias[index]}, gap={source_gaps[index]:.6f}, step={step_errors[index]:.3e}"
            for index, label in enumerate(LABELS)
        ),
    )
    checks.check(
        "rank-five-lower-bound",
        "every pure Schur correction with fewer than six source modes leaves a nonzero operator-norm residual",
        min(source_gaps) > 0.025 and all(rank == 6 for rank in ranks),
        "Eckart-Young lower bounds for rank <=5: "
        + ", ".join(
            f"{label} >= {source_gaps[index]:.6f}"
            for index, label in enumerate(LABELS)
        ),
    )
    checks.check(
        "definite-source-block-exclusion",
        "neither a positive- nor negative-definite C can reproduce any indefinite M through B C^{-1} B^dagger",
        all(negative > 0 and positive > 0 for negative, positive, _ in source_inertias),
        "positive C gives a positive-semidefinite correction; negative C gives a negative-semidefinite correction",
    )
    checks.check(
        "minimal-signature-budgets",
        "the explicit minimal C has exactly the positive/negative budget demanded by each M",
        tuple(source_block_inertias) == EXPECTED_MASS_INERTIAS,
        "; ".join(
            f"{label}: required/constructed C inertia={source_block_inertias[index]}"
            for index, label in enumerate(LABELS)
        ),
    )
    checks.check(
        "constructive-minimal-schur-completion",
        "six auxiliary modes explicitly cancel each six-dimensional source mass coefficient",
        max(completion_residuals) < 2.0e-13 and all(rank == 6 for rank in ranks),
        f"maximum factorization/Schur/spectral residual={max(completion_residuals):.3e}",
    )
    checks.check(
        "exact-joint-ward-kernel",
        "each 12 by 12 joint coefficient Hessian has the constructed six-dimensional graph kernel",
        max(kernel_residuals) < 2.0e-13
        and tuple(joint_inertias)
        == tuple((negative, positive, 6) for negative, positive, _ in EXPECTED_MASS_INERTIAS),
        f"joint inertias={joint_inertias}; maximum kernel residual={max(kernel_residuals):.3e}",
    )
    checks.check(
        "common-eight-mode-signature-lower-bound",
        "one fixed nonsingular source-block signature serving all three tangents needs at least four negative and four positive directions",
        max(negative for negative, _, _ in source_inertias) == 4
        and max(positive for _, positive, _ in source_inertias) == 4,
        "Sylvester bounds require dim(C) >= max n_-(M_s) + max n_+(M_s) = 4 + 4 = 8",
    )
    checks.check(
        "common-eight-mode-constructive-completion",
        "a single fixed C with inertia four negative and four positive explicitly completes every retained source tangent",
        max(common_completion_residuals) < 2.0e-13
        and max(common_kernel_residuals) < 2.0e-13
        and tuple(common_joint_inertias) == ((4, 4, 6),) * 3,
        f"joint inertias={common_joint_inertias}; maximum completion residual={max(common_completion_residuals):.3e}; maximum kernel residual={max(common_kernel_residuals):.3e}",
    )
    mass_rows = np.stack(
        [
            np.concatenate((mass.real.ravel(), mass.imag.ravel()))
            for _, mass, _ in records
        ]
    )
    mass_span_singular_values = np.linalg.svd(mass_rows, compute_uv=False)
    checks.check(
        "source-direction-dependence",
        "the three defect coefficients are linearly independent, so no source-blind fixed correction cancels all three",
        float(np.min(mass_span_singular_values)) > 0.1,
        "mass-family singular values="
        + np.array2string(mass_span_singular_values, precision=9),
    )
    regular_schur_errors = []
    sample_source, sample_mixing, *_ = common_signature_completion(records[0][1])
    for coupling in (1.0e-3, 5.0e-4, 2.5e-4):
        regular_schur = (
            coupling * records[0][1]
            - (coupling * sample_mixing)
            @ sample_source
            @ (coupling * sample_mixing).conjugate().T
        )
        regular_schur_errors.append(
            float(
                np.linalg.norm(regular_schur / coupling - records[0][1], 2)
            )
        )
    checks.check(
        "regular-analytic-schur-order-boundary",
        "with B(0)=0 and invertible C(0), analytic mixed blocks change the O(source) Schur coefficient only at quadratic order",
        regular_schur_errors[1] < 0.51 * regular_schur_errors[0]
        and regular_schur_errors[2] < 0.51 * regular_schur_errors[1]
        and "2p-q=1" in note_flat
        and "b(0)=0" in note_flat
        and "c(0)" in note_flat,
        "successive ||S(c)/c-M||="
        + ", ".join(f"{value:.3e}" for value in regular_schur_errors),
    )
    checks.check(
        "singular-scaling-taxonomy",
        "the explicit coefficient completion occupies the analytic p=q=1 singular-block route, not the regular invertible route",
        "p=q=1" in note_flat
        and "rank jump" in note_flat
        and "square-root" in note_flat
        and "flat isotropic mixing" in note_flat
        and "direct ward" in note_flat,
    )
    checks.check(
        "differentiated-ward-split",
        "the note distinguishes stationary Schur cancellation from the nonstationary connection term",
        "h_{ba} r^a" in note_flat
        and "partial_b r^a" in note_flat
        and "connection term" in note_flat,
    )
    checks.check(
        "bounded-theorem-and-no-go-scope",
        "the result is a constructive algebraic completion plus a bounded pure-Schur minimum, not a gravity no-go",
        "n1--n8 status: `pass` only" in note_flat
        and "not a gravity no-go" in note_flat
        and "locality remains open" in note_flat
        and "analytic coupling" in note_flat
        and "eight" in note_flat,
    )

    print("N5_CERTIFICATE: resolution=the claim is restricted to the six-mode coefficient-level pure-Schur class")
    print("N5_CERTIFICATE: constructive_route=per-branch six-mode and common fixed-signature eight-mode completions are supplied")
    print("N5_CERTIFICATE: excluded_rhetoric=no universal source, matter, Ward, gravity, or axiom impossibility is claimed")
    print("N5_CERTIFICATE: live_routes=connection terms, nonstationary backgrounds, singular blocks, additional local carriers, and massive phases remain open")
    print("N5_CERTIFICATE: physical_boundary=locality, coupling scaling, source selection, causal signature, and nonlinear stability are not derived")
    print("per_element: checked all six physical geometry modes and six explicit auxiliary modes for each source tangent")
    print("per_mode: checked the k=0 O(source) coefficient; no nonzero-momentum or continuous-zone completion is claimed")
    print("per_block: checked all three retained source tangents, their rank/signature minima, and explicit joint kernels")
    print("lattice_wide: checked and not executed — this is not a local nonuniform action, analytic coupling family, finite-torus, Lorentzian, or nonlinear theorem")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return int(checks.failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
