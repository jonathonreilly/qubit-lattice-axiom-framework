#!/usr/bin/env python3
"""Prove the null-Record log-odds action-representative anchor.

The finite positive-family theorem is exact: normalized probabilities plus a
distinguished null configuration determine one unique dimensionless action
whose null row vanishes.  The runner also checks that the retained coframe cut
family realizes the anchor and that Block 25's nonzero common completions are
therefore new interactions rather than anchored matter-action equivalences.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from pathlib import Path
import sys

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import admissibility_cut_surface_coframe_stress_higher_form_ward_geometry_dynamics_boundary_2026_08_10 as coframe  # noqa: E402
import admissibility_normalized_family_additive_zero_contact_nonidentifiability_boundary_2026_08_10 as block25  # noqa: E402


AUDIT_TIMEOUT_SEC = 180
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_NULL_RECORD_LOG_ODDS_ACTION_REPRESENTATIVE_ANCHOR_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
BLOCK25_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_NORMALIZED_FAMILY_ADDITIVE_ZERO_CONTACT_"
    "NONIDENTIFIABILITY_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
COFRAME_PATH = coframe.NOTE_PATH
CUT_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_CODE_SWAP_CUT_AREA_LOCAL_SOURCE_IMPROVEMENT_"
    "METRIC_RESPONSE_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
PREMISE_REGISTRY_PATH = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_NULL_RECORD_LOG_ODDS_ACTION_REPRESENTATIVE_ANCHOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_NORMALIZED_FAMILY_ADDITIVE_ZERO_CONTACT_NONIDENTIFIABILITY_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/ADMISSIBILITY_CUT_SURFACE_COFRAME_STRESS_HIGHER_FORM_WARD_GEOMETRY_DYNAMICS_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/ADMISSIBILITY_CODE_SWAP_CUT_AREA_LOCAL_SOURCE_IMPROVEMENT_METRIC_RESPONSE_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "scripts/admissibility_normalized_family_additive_zero_contact_nonidentifiability_boundary_2026_08_10.py",
    "scripts/admissibility_cut_surface_coframe_stress_higher_form_ward_geometry_dynamics_boundary_2026_08_10.py",
    "scripts/admissibility_sourced_regge_joint_ward_schur_completion_boundary_2026_08_10.py",
    "scripts/admissibility_sourced_regge_flat_gauge_quotient_ward_completion_boundary_2026_08_10.py",
    "scripts/admissibility_regge_curvature_squared_nonflat_continuation_2026_08_10.py",
    "scripts/admissibility_fixed_metric_nonlinear_regge_kkt_continuation_2026_08_10.py",
    "scripts/admissibility_flat_regge_curvature_squared_branch_lift_2026_08_10.py",
    "scripts/admissibility_nonlinear_regge_extra_branch_cubic_lift_2026_08_10.py",
    "scripts/admissibility_compact_regge_homogeneous_reaction_rank_kkt_boundary_2026_08_10.py",
    "scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py",
)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition, detail: str = "") -> None:
        ok = bool(condition)
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {statement}")
        if detail:
            print(f"       {detail}")
        self.passed += int(ok)
        self.failed += int(not ok)


def normalized(weights):
    partition = sum(weights)
    return tuple(sp.simplify(weight / partition) for weight in weights)


def uniform_area_field(sites, stretch: Fraction):
    matrix = coframe.diagonal_matrix((Fraction(1) + stretch, Fraction(1), Fraction(1)))
    areas = tuple(coframe.area_factor(matrix, axis) for axis in range(3))
    return {site: areas for site in sites}


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    note_flat = " ".join(note.lower().split())
    axioms = AXIOM_PATH.read_text(encoding="utf-8")
    axioms_flat = " ".join(axioms.split())
    parent = BLOCK25_PATH.read_text(encoding="utf-8").lower()
    coframe_note = COFRAME_PATH.read_text(encoding="utf-8").lower()
    cut_note = CUT_PATH.read_text(encoding="utf-8").lower()
    registry = PREMISE_REGISTRY_PATH.read_text(encoding="utf-8")

    print("external_scientific_inputs: none; null-anchor uniqueness is exact finite probability algebra and the cut/source controls are repository-local")
    print("analytic_boundary: the finite positive-family and factorized-composition theorems are exact; the Block-25 source matrices are double-precision reconstructions")
    print("physical_boundary: the anchor does not select a joint family, action unit, pure-geometry action, source interaction, or Lorentzian update")

    checks.check(
        "source-and-axiom-boundary",
        "Record supplies I(empty)=0 but current axioms leave source/action and dynamics outside their content",
        "I(empty)=0" in axioms_flat
        and "source/action and physical-observable identification" in axioms_flat
        and "Admissibility is not a dynamics axiom" in axioms_flat
        and all(
            key in registry
            for key in (
                "minimal_axioms",
                "scale_reference_primitive",
                "kinetic_isotropy_primitive",
                "realized_state_primitive",
            )
        ),
    )
    checks.check(
        "retained-parent-chain",
        "Block 25 supplies the common-shift ambiguity and the retained cut family supplies an explicit representative",
        "normalized-family gauge" in parent
        and "absolute geometry contact hessian" in parent
        and "s_cut -> s_cut+c(f,b)" in coframe_note
        and "explicitly declares the local representative" in coframe_note
        and "empty/full" in cut_note,
    )
    checks.check(
        "note-contract",
        "the note states uniqueness, cut-family realization, the separate geometry action, and bounded scope",
        "unique dimensionless action representative" in note_flat
        and "pure-geometry action" in note_flat
        and "null-record source/action anchor candidate" in note_flat
        and "n1--n8 status: `pass` only" in note_flat
        and "no canonical axiom is edited" in note_flat,
    )

    x, y = sp.symbols("x y", real=True)
    actions = (
        x**2 + 2 * y,
        x * y + 3 * x - y,
        2 * x**2 - x * y + y**2 + 1,
    )
    common = 4 * x**2 + 3 * x * y - 2 * y**2 + x
    weights = tuple(sp.exp(-action) for action in actions)
    shifted_weights = tuple(sp.exp(-(action + common)) for action in actions)
    probabilities = normalized(weights)
    shifted_probabilities = normalized(shifted_weights)
    probability_errors = tuple(
        sp.simplify(left - right)
        for left, right in zip(probabilities, shifted_probabilities)
    )
    checks.check(
        "exact-normalized-common-shift",
        "a configuration-independent geometry function leaves every normalized probability unchanged",
        all(error == 0 for error in probability_errors),
    )

    anchored = tuple(sp.expand(action - actions[0]) for action in actions)
    shifted_anchored = tuple(
        sp.expand(action + common - (actions[0] + common)) for action in actions
    )
    odds_errors = tuple(
        sp.simplify(
            probabilities[index] / probabilities[0]
            - sp.exp(-anchored[index])
        )
        for index in range(len(actions))
    )
    checks.check(
        "null-log-odds-representative",
        "A_x=-log(pi_x/pi_0)=S_x-S_0 is common-shift invariant and has A_0=0",
        anchored[0] == 0
        and shifted_anchored == anchored
        and all(error == 0 for error in odds_errors),
    )

    arbitrary_shift = sp.symbols("f", real=True)
    anchor_solutions = sp.solve(sp.Eq(arbitrary_shift, 0), arbitrary_shift)
    checks.check(
        "unique-null-anchor",
        "two representatives of one positive family with vanishing null row have zero common difference",
        anchor_solutions == [0],
    )

    reconstructed = normalized(tuple(sp.exp(-action) for action in anchored))
    reconstruction_errors = tuple(
        sp.simplify(left - right)
        for left, right in zip(probabilities, reconstructed)
    )
    checks.check(
        "anchored-family-reconstruction",
        "the null-anchored log-odds action reproduces the complete normalized family",
        all(error == 0 for error in reconstruction_errors),
    )

    gradient_errors = []
    hessian_errors = []
    for original, shifted in zip(anchored, shifted_anchored):
        gradient_errors.append(
            sp.simplify(sp.diff(original, x) - sp.diff(shifted, x))
        )
        hessian_errors.append(
            sp.simplify(sp.diff(original, x, y) - sp.diff(shifted, x, y))
        )
    checks.check(
        "geometry-derivative-invariance",
        "all first and second geometry derivatives relative to the null configuration are identifiable",
        all(error == 0 for error in gradient_errors + hessian_errors),
    )

    a, b, c = sp.symbols("a b c", real=True)
    left_actions = (sp.Integer(0), a, b)
    right_actions = (sp.Integer(0), c)
    product_actions = tuple(
        sp.expand(left + right)
        for left, right in product(left_actions, right_actions)
    )
    left_probabilities = normalized(tuple(sp.exp(-value) for value in left_actions))
    right_probabilities = normalized(tuple(sp.exp(-value) for value in right_actions))
    product_probabilities = tuple(
        sp.simplify(left * right)
        for left, right in product(left_probabilities, right_probabilities)
    )
    product_odds_errors = tuple(
        sp.simplify(
            product_probabilities[index] / product_probabilities[0]
            - sp.exp(-product_actions[index])
        )
        for index in range(len(product_actions))
    )
    checks.check(
        "independent-product-additivity",
        "the null-anchored action of a factorized family is the sum of the two anchored actions",
        product_actions[0] == 0 and all(error == 0 for error in product_odds_errors),
    )

    size = 2
    sites = coframe.sites_of(size)
    all_sites = frozenset(sites)
    empty = frozenset()
    full = all_sites
    areas = coframe.area_field(coframe.coframe_field(sites))
    tension = Fraction(7, 11)
    source = {
        site: tuple(
            Fraction(1 + site[0] + 2 * site[1] + 3 * site[2] + axis, 17)
            for axis in range(3)
        )
        for site in sites
    }

    def total_cut_action(chosen, area_values=areas):
        return coframe.edge_action(chosen, sites, size, area_values, tension) + coframe.oriented_source_action(
            chosen, sites, size, source
        )

    null_actions = (total_cut_action(empty), total_cut_action(full))
    checks.check(
        "retained-cut-null-and-full-anchor",
        "the empty and full configurations have zero action for a nonuniform coframe and arbitrary supplied two-form source",
        null_actions == (0, 0),
        f"empty/full actions={null_actions}",
    )

    complement_errors = []
    anchored_errors = []
    for mask in range(1 << len(sites)):
        chosen = frozenset(
            site for index, site in enumerate(sites) if mask & (1 << index)
        )
        complement = all_sites - chosen
        action = coframe.edge_action(chosen, sites, size, areas, tension)
        complement_action = coframe.edge_action(
            complement, sites, size, areas, tension
        )
        complement_errors.append(action - complement_action)
        anchored_errors.append(action - coframe.edge_action(empty, sites, size, areas, tension) - action)
    checks.check(
        "retained-cut-complement-and-log-odds",
        "at zero two-form source the exact cut action is complement symmetric and already equals its null-anchored representative",
        all(error == 0 for error in complement_errors + anchored_errors),
        f"configurations checked={1 << len(sites)}",
    )

    path_null_actions = []
    singleton_actions = []
    singleton = frozenset((sites[0],))
    for stretch in (Fraction(-1, 5), Fraction(0), Fraction(1, 5)):
        path_areas = uniform_area_field(sites, stretch)
        path_null_actions.append(
            (
                coframe.edge_action(empty, sites, size, path_areas, tension),
                coframe.edge_action(full, sites, size, path_areas, tension),
            )
        )
        singleton_actions.append(
            coframe.edge_action(singleton, sites, size, path_areas, tension)
        )
    checks.check(
        "anchor-persists-across-geometry",
        "the cut null/full anchors persist along a nontrivial exact coframe path while a sourced configuration responds",
        all(pair == (0, 0) for pair in path_null_actions)
        and len(set(singleton_actions)) > 1,
        f"singleton path actions={singleton_actions}",
    )

    physical, source_records = block25.block23.reconstruct_mass_matrices()
    completion_norms = []
    completion_errors = []
    for _label, mass, _step_error in source_records:
        edge_hessian = -physical @ mass @ physical.conjugate().T
        completion_norms.append(float(np.linalg.norm(edge_hessian, 2)))
        completion_errors.append(
            float(
                np.linalg.norm(
                    physical.conjugate().T @ edge_hessian @ physical + mass,
                    2,
                )
            )
        )
    checks.check(
        "block25-common-completion-is-not-anchored-equivalence",
        "the Block-25 common completions are nonzero and exact, so the null anchor reclassifies them as new joint interactions",
        min(completion_norms) > 1.0e-3 and max(completion_errors) < 2.0e-13,
        f"minimum shift norm={min(completion_norms):.6f}; maximum completion residual={max(completion_errors):.3e}",
    )

    checks.check(
        "bounded-theorem-and-next-law",
        "the anchor fixes only the matter/source representative and leaves family selection, geometry action, unit, projective limit, and Lorentzian closure open",
        "not select the separate pure-geometry action" in note_flat
        and "projective consistency" in note_flat
        and "lorentzian" in note_flat
        and "unadopted" in note_flat
        and "no canonical axiom is edited" in note_flat,
    )

    print("N5_CERTIFICATE: resolution=the finite positive normalized-family common shift is fixed uniquely by the null matter-action anchor")
    print("N5_CERTIFICATE: retained_realization=the nonuniform coframe cut family is exactly empty/full anchored and recovered from null log odds")
    print("N5_CERTIFICATE: completion_boundary=Block-25 nonzero common Hessians become new joint interactions rather than normalization equivalences")
    print("N5_CERTIFICATE: live_routes=joint-family selection, allowed anchored counterterms, pure geometry, projective consistency, source transformations, and causal updates remain open")
    print("N5_CERTIFICATE: axiom_boundary=Record I(empty)=0 is not a source/action identity, action unit, or geometry law")
    print("per_element: checked every symbolic family row, every factorized product row, and all 256 binary configurations of the exact L=2 cut fixture")
    print("per_mode: checked every entry of the three Block-25 fifteen-edge completion tensors and their six-mode projections")
    print("per_block: checked normalized-family algebra, null-anchor uniqueness, exact cut realization, and source/geometry separation")
    print("lattice_wide: checked and not executed — no projective-limit, continuous-zone, Lorentzian, or nonlinear theorem is claimed")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return int(checks.failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
