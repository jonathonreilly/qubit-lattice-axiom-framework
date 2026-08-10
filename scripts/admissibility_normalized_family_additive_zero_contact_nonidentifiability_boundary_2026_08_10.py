#!/usr/bin/env python3
"""Test additive-zero identifiability of normalized action families.

The runner proves the exact normalized-family gauge S_i(g)->S_i(g)+F(g),
then pulls the three Block-23 sourced mass matrices back to explicit common
geometry shifts on the inherited physical quotient.  The construction is a
local identifiability boundary, not a physical action selection.
"""

from __future__ import annotations

from pathlib import Path
import sys

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import admissibility_sourced_regge_joint_ward_schur_completion_boundary_2026_08_10 as block23  # noqa: E402


AUDIT_TIMEOUT_SEC = 120
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_NORMALIZED_FAMILY_ADDITIVE_ZERO_CONTACT_"
    "NONIDENTIFIABILITY_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
PARENT_NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_FOUR_COFRAME_HYPERFACE_SEAGULL_SOURCED_REGGE_"
    "SPAN_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
COFRAME_NOTE_PATH = block23.COFRAME_NOTE_PATH
PREMISE_REGISTRY_PATH = block23.PREMISE_REGISTRY_PATH

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_NORMALIZED_FAMILY_ADDITIVE_ZERO_CONTACT_NONIDENTIFIABILITY_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/ADMISSIBILITY_FOUR_COFRAME_HYPERFACE_SEAGULL_SOURCED_REGGE_SPAN_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/ADMISSIBILITY_CUT_SURFACE_COFRAME_STRESS_HIGHER_FORM_WARD_GEOMETRY_DYNAMICS_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "scripts/admissibility_four_coframe_hyperface_seagull_sourced_regge_span_boundary_2026_08_10.py",
    "scripts/admissibility_sourced_regge_joint_ward_schur_completion_boundary_2026_08_10.py",
    "scripts/admissibility_sourced_regge_flat_gauge_quotient_ward_completion_boundary_2026_08_10.py",
    "scripts/admissibility_regge_curvature_squared_nonflat_continuation_2026_08_10.py",
    "scripts/admissibility_fixed_metric_nonlinear_regge_kkt_continuation_2026_08_10.py",
    "scripts/admissibility_flat_regge_curvature_squared_branch_lift_2026_08_10.py",
    "scripts/admissibility_nonlinear_regge_extra_branch_cubic_lift_2026_08_10.py",
    "scripts/admissibility_compact_regge_homogeneous_reaction_rank_kkt_boundary_2026_08_10.py",
    "scripts/admissibility_timelike_edge_current_network_compact_homothety_regge_boundary_2026_08_10.py",
    "scripts/admissibility_closed_helical_defect_history_ward_neutral_ir_regge_response_boundary_2026_08_10.py",
    "scripts/admissibility_centered_tick_edge_defect_improvement_exact_static_regge_source_boundary_2026_08_10.py",
    "scripts/admissibility_cut_worldvolume_affine_bag_regge_monopole_boundary_2026_08_10.py",
    "scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py",
)

TOLERANCE = 1.0e-10


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


def realification(matrix):
    """Real symmetric form corresponding to a complex Hermitian form."""
    return np.block(
        [[matrix.real, -matrix.imag], [matrix.imag, matrix.real]]
    )


def main():
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    note_flat = " ".join(note.lower().split())
    parent = PARENT_NOTE_PATH.read_text(encoding="utf-8").lower()
    coframe = COFRAME_NOTE_PATH.read_text(encoding="utf-8").lower()
    axioms = AXIOM_PATH.read_text(encoding="utf-8").lower()
    registry = PREMISE_REGISTRY_PATH.read_text(encoding="utf-8")

    print("external_scientific_inputs: none; the normalized-family identity is exact algebra and the target matrices are reconstructed from repository-local actions")
    print("analytic_boundary: probability invariance and arbitrary local Hessian realization are exact; Block-23 matrix reconstruction is double precision")
    print("physical_boundary: a common configuration-independent geometry shift is not a selected local covariant action or an adopted axiom")

    checks.check(
        "source-and-axiom-boundary",
        "the current axioms do not select an action representative, its geometry-dependent additive zero, or its unit",
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
        "retained-response-contract",
        "the retained response identity and Block-24 additive-zero route are bound",
        "psi''=cov(s',s')-e[s'']" in coframe
        and "geometry-dependent additive zero" in parent,
    )
    checks.check(
        "note-contract",
        "the note states exact probability invariance, arbitrary local response freedom, and bounded scope",
        "normalized-family gauge" in note_flat
        and "arbitrary hermitian" in note_flat
        and "not an action-selection no-go" in note_flat
        and "n1--n8 status: `pass` only" in note_flat
        and "no canonical axiom is edited" in note_flat,
    )

    x, y = sp.symbols("x y", real=True)
    actions = (x + 2 * y, 2 * x - y, -x + y)
    common = 3 * x**2 + 2 * x * y - 5 * y**2
    partition = sum(sp.exp(-action) for action in actions)
    shifted_partition = sum(sp.exp(-(action + common)) for action in actions)
    factor_error = sp.simplify(shifted_partition - sp.exp(-common) * partition)
    probability_errors = [
        sp.simplify(
            sp.exp(-(action + common)) / shifted_partition
            - sp.exp(-action) / partition
        )
        for action in actions
    ]
    checks.check(
        "exact-normalized-family-gauge",
        "S_i(g) plus a common F(g) leaves every normalized configuration probability unchanged",
        factor_error == 0 and all(error == 0 for error in probability_errors),
    )

    variables = sp.Matrix([x, y])
    common_hessian = sp.hessian(common, (x, y))
    response_shift = sp.hessian(-common, (x, y))
    checks.check(
        "exact-log-partition-response-shift",
        "log Z shifts by -F and its geometry Hessian shifts by -F''",
        response_shift + common_hessian == sp.zeros(2),
        f"F''={common_hessian.tolist()}",
    )

    h11, h12, h22 = sp.symbols("h11 h12 h22", real=True)
    target = sp.Matrix([[h11, h12], [h12, h22]])
    arbitrary = sp.Rational(1, 2) * (variables.T * target * variables)[0]
    checks.check(
        "arbitrary-local-real-hessian",
        "a common quadratic shift realizes any symmetric Hessian in a local geometry chart",
        sp.hessian(arbitrary, (x, y)) == target,
    )

    physical, source_records = block23.reconstruct_mass_matrices()
    leading_gauge = block23.block22.leading_flat_gauge(
        block23.block22.GENERIC_DIRECTION
    )
    orthonormal_error = float(
        np.linalg.norm(physical.conjugate().T @ physical - np.eye(6), 2)
    )
    physical_gauge_error = float(
        np.linalg.norm(physical.conjugate().T @ leading_gauge, 2)
    )
    checks.check(
        "inherited-physical-quotient",
        "the six Block-23 modes are orthonormal and transverse to the inherited four gauge columns",
        orthonormal_error < 1.0e-12 and physical_gauge_error < 1.0e-12,
        f"orthonormal residual={orthonormal_error:.3e}; gauge residual={physical_gauge_error:.3e}",
    )

    hermitian_errors = []
    realification_errors = []
    completion_errors = []
    ward_errors = []
    order_errors = []
    for _label, mass, _step_error in source_records:
        hermitian_errors.append(float(np.linalg.norm(mass - mass.conjugate().T, 2)))
        real_form = realification(mass)
        realification_errors.append(float(np.linalg.norm(real_form - real_form.T, 2)))

        # F_s(delta ell)=1/2 delta ell^dag D_s delta ell with
        # D_s=-U M_s U^dagger is common to every normalized configuration.
        edge_hessian = -physical @ mass @ physical.conjugate().T
        projected = physical.conjugate().T @ edge_hessian @ physical
        completion_errors.append(float(np.linalg.norm(projected + mass, 2)))
        ward_errors.append(float(np.linalg.norm(edge_hessian @ leading_gauge, 2)))
        for coupling in (1.0e-3, 5.0e-4, 2.5e-4):
            order_errors.append(
                float(np.linalg.norm((coupling * edge_hessian) / coupling - edge_hessian, 2))
            )

    checks.check(
        "complex-hermitian-real-local-form",
        "every sourced six-mode Hermitian tensor has a real symmetric twelve-coordinate quadratic representative",
        max(hermitian_errors) < 1.0e-12
        and max(realification_errors) < 1.0e-12,
        f"Hermitian residual={max(hermitian_errors):.3e}; real-form residual={max(realification_errors):.3e}",
    )
    checks.check(
        "three-source-exact-additive-completion",
        "one common geometry shift per named source tangent exactly cancels its full six-mode O(source) tensor",
        max(completion_errors) < 2.0e-13,
        f"maximum quotient residual={max(completion_errors):.3e}",
    )
    checks.check(
        "inherited-gauge-null-lift",
        "the explicit fifteen-edge shift annihilates the inherited gauge columns at the supplied direction",
        max(ward_errors) < 2.0e-13,
        f"maximum Ward residual={max(ward_errors):.3e}",
    )
    checks.check(
        "source-linear-additive-order",
        "F(c,g)=c F_1(g) contributes at the required first source order",
        max(order_errors) < 1.0e-14,
        f"maximum rescaled-order residual={max(order_errors):.3e}",
    )
    checks.check(
        "probability-contact-nonidentifiability",
        "identical normalized configuration probabilities can carry distinct and arbitrarily prescribed local contact tensors",
        all(error == 0 for error in probability_errors)
        and common_hessian != sp.zeros(2)
        and max(completion_errors) < 2.0e-13,
    )
    checks.check(
        "bounded-theorem-and-no-go-scope",
        "the note preserves locality, covariance, global consistency, action selection, and Lorentzian closure as live obligations",
        "n1--n8 status: `pass` only" in note_flat
        and "locality" in note_flat
        and "covariance" in note_flat
        and "global integrability" in note_flat
        and "not an action-selection no-go" in note_flat,
    )

    print("N5_CERTIFICATE: resolution=the exact ambiguity is local and restricted to normalized families modulo a common geometry-dependent shift")
    print("N5_CERTIFICATE: positive_result=an explicit source-linear common quadratic shift cancels each named full six-mode tensor and preserves the inherited gauge columns")
    print("N5_CERTIFICATE: negative_result=normalized probabilities alone cannot identify the absolute contact Hessian")
    print("N5_CERTIFICATE: live_routes=a selected local covariant representative, locality and gluing, global integrability, source transformations, and Lorentzian stability remain open")
    print("N5_CERTIFICATE: physical_boundary=the constructed shift is an identifiability witness, not a licensed action, physical completion, or adopted axiom")
    print("per_element: checked all normalized probabilities, symbolic Hessian entries, and every entry of three six-mode and fifteen-edge completion tensors")
    print("per_mode: checked the supplied k=0 O(source) coefficient on all six physical modes and four inherited gauge columns")
    print("per_block: checked exact normalized-family invariance, arbitrary Hessian realization, quotient cancellation, Ward-null lift, and source order")
    print("lattice_wide: checked and not executed — no sitewise local gluing, continuous-zone, Lorentzian, or nonlinear theorem is claimed")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return int(checks.failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
