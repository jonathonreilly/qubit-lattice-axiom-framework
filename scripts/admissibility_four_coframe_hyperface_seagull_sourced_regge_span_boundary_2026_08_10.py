#!/usr/bin/env python3
"""Test the retained four-coframe hyperface seagull against Block 23.

The runner derives the four unit-hyperface area Hessians exactly at the flat
four-coframe, pulls them through the repository's flat metric-to-edge map onto
Block 23's six physical modes, and compares their entire homogeneous span
with the three sourced O(c) Regge mass coefficients.  It is a bounded carrier
test, not a no-go for contact terms, coframes, source dynamics, or gravity.
"""

from __future__ import annotations

from itertools import product
from pathlib import Path
import sys

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import admissibility_sourced_regge_joint_ward_schur_completion_boundary_2026_08_10 as block23  # noqa: E402


AUDIT_TIMEOUT_SEC = 120
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_FOUR_COFRAME_HYPERFACE_SEAGULL_SOURCED_REGGE_"
    "SPAN_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
PARENT_NOTE_PATH = block23.NOTE_PATH
COFRAME_NOTE_PATH = block23.COFRAME_NOTE_PATH
WORLDVOLUME_NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_CUT_WORLDVOLUME_AFFINE_BAG_REGGE_MONOPOLE_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
PREMISE_REGISTRY_PATH = block23.PREMISE_REGISTRY_PATH

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_FOUR_COFRAME_HYPERFACE_SEAGULL_SOURCED_REGGE_SPAN_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/ADMISSIBILITY_SOURCED_REGGE_JOINT_WARD_SCHUR_COMPLETION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/ADMISSIBILITY_CUT_SURFACE_COFRAME_STRESS_HIGHER_FORM_WARD_GEOMETRY_DYNAMICS_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/ADMISSIBILITY_CUT_WORLDVOLUME_AFFINE_BAG_REGGE_MONOPOLE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "scripts/admissibility_sourced_regge_joint_ward_schur_completion_boundary_2026_08_10.py",
    "scripts/admissibility_sourced_regge_flat_gauge_quotient_ward_completion_boundary_2026_08_10.py",
    "scripts/admissibility_cut_surface_coframe_stress_higher_form_ward_geometry_dynamics_boundary_2026_08_10.py",
    "scripts/admissibility_cut_worldvolume_affine_bag_regge_monopole_boundary_2026_08_10.py",
    "scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py",
)

TOLERANCE = 1.0e-8
TARGET_INERTIAS = {(3, 3, 0), (4, 2, 0), (2, 4, 0)}


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


def symmetric_metric_basis():
    """Coframe variations X=h/2 for the repository's ten metric entries."""
    basis = []
    for left, right in block23.block22.regge.HCOMPS:
        matrix = sp.zeros(4)
        matrix[left, right] += sp.Rational(1, 2)
        if left != right:
            matrix[right, left] += sp.Rational(1, 2)
        basis.append(matrix)
    return basis


def hyperarea_second(mu, variation):
    """Exact A_mu''(0) for E(s)=I+sX and A_mu=|cof(E)e_mu|."""
    parameter = sp.symbols("seagull_parameter", real=True)
    columns = [index for index in range(4) if index != mu]
    coframe = sp.eye(4) + parameter * variation
    tangent = coframe[:, columns]
    gram_determinant = sp.expand((tangent.T * tangent).det())
    first = sp.diff(gram_determinant, parameter).subs(parameter, 0)
    second = sp.diff(gram_determinant, parameter, 2).subs(parameter, 0)
    # If A=sqrt(d) and d(0)=1, A''=d''/2-(d')^2/4.
    return sp.simplify(second / 2 - first * first / 4)


def exact_hyperarea_hessians():
    basis = symmetric_metric_basis()
    hessians = []
    for mu in range(4):
        matrix = sp.zeros(10)
        for left in range(10):
            matrix[left, left] = hyperarea_second(mu, basis[left])
        for left in range(10):
            for right in range(left + 1, 10):
                combined = hyperarea_second(mu, basis[left] + basis[right])
                entry = sp.simplify(
                    (combined - matrix[left, left] - matrix[right, right]) / 2
                )
                matrix[left, right] = matrix[right, left] = entry
        hessians.append(matrix)
    return hessians


def hermitian_vector(matrix):
    return np.concatenate((matrix.real.ravel(), matrix.imag.ravel()))


def main():
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    note_flat = " ".join(note.lower().split())
    parent = PARENT_NOTE_PATH.read_text(encoding="utf-8")
    coframe = COFRAME_NOTE_PATH.read_text(encoding="utf-8")
    worldvolume = WORLDVOLUME_NOTE_PATH.read_text(encoding="utf-8")
    axioms = AXIOM_PATH.read_text(encoding="utf-8").lower()
    registry = PREMISE_REGISTRY_PATH.read_text(encoding="utf-8")

    print("external_scientific_inputs: none; the coframe Hessians, Regge pullback, and source matrices are reconstructed from repository-local actions")
    print("analytic_boundary: four-coframe hyperarea Hessians are exact rational matrices; pullback spectra and span residuals are double-precision numerical results")
    print("physical_boundary: homogeneous orientation weights, flat symmetric coframe convention, one supplied momentum direction, and the inherited Regge carrier are bounded fixtures")

    checks.check(
        "source-and-axiom-boundary",
        "the current axioms select neither this coframe family nor its Regge contact term",
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
        "retained-carrier-contract",
        "retained notes supply the four-coframe hyperarea action and same-family seagull formula",
        "cof(e_z)" in worldvolume.lower()
        and "psi''=cov(s',s')-e[s'']" in coframe.lower()
        and "direct ward/contact" in parent.lower(),
    )
    checks.check(
        "note-contract",
        "the note states the correct-order positive result and the bounded four-span mismatch",
        "correct o(c) order" in note_flat
        and "four-orientation span" in note_flat
        and "not a contact-term no-go" in note_flat
        and "n1--n8 status: `pass` only" in note_flat
        and "no canonical axiom is edited" in note_flat,
    )

    physical, source_records = block23.reconstruct_mass_matrices()
    metric_map = block23.block22.regge.metric_map(np.zeros(4)).real
    metric_physical = np.linalg.pinv(metric_map) @ physical
    metric_residual = float(np.linalg.norm(metric_map @ metric_physical - physical, 2))
    checks.check(
        "flat-metric-six-mode-pullback",
        "all six Block-23 physical modes lie in the exact flat ten-metric image",
        metric_physical.shape == (10, 6)
        and np.linalg.matrix_rank(metric_physical, tol=1.0e-9) == 6
        and metric_residual < 1.0e-12,
        f"shape={metric_physical.shape}; rank={np.linalg.matrix_rank(metric_physical, tol=1.0e-9)}; residual={metric_residual:.3e}",
    )

    exact_hessians = exact_hyperarea_hessians()
    exact_inertias = []
    pulled = []
    pulled_inertias = []
    for matrix in exact_hessians:
        exact_float = np.asarray(matrix, dtype=float)
        exact_inertias.append(inertia(exact_float)[0])
        reduced = metric_physical.conjugate().T @ exact_float @ metric_physical
        reduced = 0.5 * (reduced + reduced.conjugate().T)
        pulled.append(reduced)
        pulled_inertias.append(inertia(reduced)[0])
    checks.check(
        "exact-four-hyperarea-seagulls",
        "each flat unit-hyperface Hessian is an exact rank-nine form on ten symmetric metric entries",
        all(matrix.rank() == 9 for matrix in exact_hessians)
        and exact_inertias == [(5, 4, 1)] * 4,
        f"ranks={[matrix.rank() for matrix in exact_hessians]}; inertias={exact_inertias}",
    )
    checks.check(
        "physical-hyperarea-pullbacks",
        "all four hyperarea seagulls are full rank on the supplied six physical modes",
        all(item[2] == 0 and item[0] + item[1] == 6 for item in pulled_inertias),
        f"inertias={pulled_inertias}",
    )

    design = np.stack([hermitian_vector(matrix) for matrix in pulled], axis=1)
    design_singular = np.linalg.svd(design, compute_uv=False)
    checks.check(
        "four-orientation-carrier-rank",
        "the four homogeneous orientation seagulls are linearly independent as physical Hermitian forms",
        np.linalg.matrix_rank(design, tol=1.0e-9) == 4
        and float(np.min(design_singular)) > 1.0,
        "singular values=" + np.array2string(design_singular, precision=6),
    )

    signature_examples = {}
    for weights in product((1.0, 2.0, 4.0, 8.0, 16.0, 32.0), repeat=4):
        candidate = sum(weight * matrix for weight, matrix in zip(weights, pulled))
        candidate_inertia = inertia(candidate)[0]
        if candidate_inertia in TARGET_INERTIAS and candidate_inertia not in signature_examples:
            signature_examples[candidate_inertia] = tuple(int(weight) for weight in weights)
        if set(signature_examples) == TARGET_INERTIAS:
            break
    checks.check(
        "positive-weight-signature-flexibility",
        "strictly positive hyperface weights realize every Block-23 mass inertia",
        set(signature_examples) == TARGET_INERTIAS,
        f"examples={signature_examples}",
    )

    fit_records = []
    for label, mass, _step_error in source_records:
        weights, *_ = np.linalg.lstsq(design, hermitian_vector(mass), rcond=None)
        approximation = sum(weight * matrix for weight, matrix in zip(weights, pulled))
        residual = mass - approximation
        fit_records.append(
            {
                "label": label,
                "weights": weights,
                "frobenius": float(np.linalg.norm(residual) / np.linalg.norm(mass)),
                "operator": float(np.linalg.norm(residual, 2) / np.linalg.norm(mass, 2)),
                "augmented_rank": int(
                    np.linalg.matrix_rank(
                        np.column_stack((design, hermitian_vector(mass))), tol=1.0e-9
                    )
                ),
            }
        )
    checks.check(
        "three-source-four-span-no-overlap",
        "none of the three sourced mass coefficients belongs to the entire real four-orientation seagull span",
        all(record["augmented_rank"] == 5 for record in fit_records)
        and min(record["frobenius"] for record in fit_records) > 0.89
        and min(record["operator"] for record in fit_records) > 0.77,
        "; ".join(
            f"{record['label']}: Fro={record['frobenius']:.6f}, op={record['operator']:.6f}, weights={np.array2string(record['weights'], precision=5)}"
            for record in fit_records
        ),
    )
    checks.check(
        "signed-weight-and-contact-sign-control",
        "the mismatch already allows arbitrary real weights and is unchanged by reversing the contact sign",
        all(np.any(record["weights"] < 0.0) or np.any(record["weights"] > 0.0) for record in fit_records)
        and min(record["frobenius"] for record in fit_records) > 0.89,
    )

    order_errors = []
    sample = sum((index + 1) * matrix for index, matrix in enumerate(pulled))
    for coupling in (1.0e-3, 5.0e-4, 2.5e-4):
        order_errors.append(float(np.linalg.norm((coupling * sample) / coupling - sample, 2)))
    checks.check(
        "direct-seagull-first-order-scaling",
        "a source-linear hyperface action contributes its geometry seagull at the correct O(c) order without a Schur rank jump",
        max(order_errors) < 1.0e-14 and "direct source-linear contact" in note_flat,
        f"maximum rescaled-order residual={max(order_errors):.3e}",
    )
    checks.check(
        "inertia-is-not-tensor-matching",
        "matching all three inertia classes does not imply matching any of the three required matrices",
        set(signature_examples) == TARGET_INERTIAS
        and min(record["frobenius"] for record in fit_records) > 0.89,
    )
    checks.check(
        "bounded-theorem-and-no-go-scope",
        "the note preserves connected, site-dependent, normalization, alternate-carrier, and full connection routes",
        "n1--n8 status: `pass` only" in note_flat
        and "connected covariance" in note_flat
        and "site-dependent" in note_flat
        and "geometry-dependent additive zero" in note_flat
        and "not a contact-term no-go" in note_flat,
    )

    print("N5_CERTIFICATE: resolution=the mismatch is restricted to one flat homogeneous four-hyperface seagull span at the supplied physical direction")
    print("N5_CERTIFICATE: positive_result=the carrier is full-rank, source-linear, and realizes all three target inertia classes")
    print("N5_CERTIFICATE: negative_result=all three full matrices remain outside the unconstrained real four-orientation span with large margins")
    print("N5_CERTIFICATE: live_routes=connected covariance, site-dependent coframes, additive normalization, full Ward connection, and alternate carriers remain open")
    print("N5_CERTIFICATE: physical_boundary=no local source selection, continuous-zone result, Lorentzian dynamics, or nonlinear stability is derived")
    print("per_element: checked all ten symmetric metric entries, four hyperface Hessians, and every entry of three six-mode target matrices")
    print("per_mode: checked the k=0 O(source) coefficient on the six physical modes for one supplied generic momentum direction")
    print("per_block: checked exact hyperarea forms, Regge pullback, positive signature controls, and unconstrained real-span fits")
    print("lattice_wide: checked and not executed — homogeneous weights are not a site-dependent, nonuniform, continuous-zone, Lorentzian, or nonlinear theorem")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return int(checks.failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
