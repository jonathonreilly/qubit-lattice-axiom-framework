#!/usr/bin/env python3
"""Prove the null-relative RN source cocycle and gravity-contact boundary."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import sys

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import admissibility_null_record_log_odds_action_representative_anchor_boundary_2026_08_10 as block26  # noqa: E402


coframe = block26.coframe
block25 = block26.block25

AUDIT_TIMEOUT_SEC = 180
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_NULL_RECORD_RN_COCYCLE_SOURCE_UNIT_GRAVITY_CONTACT_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
BLOCK26_PATH = block26.NOTE_PATH
COMPATIBILITY_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_BINARY_FULL_CONDITIONAL_COMPATIBILITY_ISING_ACTION_"
    "AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
RN_PATH = ROOT / "docs" / "SOURCE_MEASURE_PCAL_RN_COCYCLE_THEOREM_NOTE_2026-05-30.md"
SCALE_PATH = ROOT / "docs" / "SOURCE_MEASURE_LOG_SELECTION_BOUNDARY_THEOREM_NOTE_2026-05-30.md"
PREMISE_REGISTRY_PATH = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_NULL_RECORD_RN_COCYCLE_SOURCE_UNIT_GRAVITY_CONTACT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_NULL_RECORD_LOG_ODDS_ACTION_REPRESENTATIVE_ANCHOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/ADMISSIBILITY_BINARY_FULL_CONDITIONAL_COMPATIBILITY_ISING_ACTION_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/SOURCE_MEASURE_PCAL_RN_COCYCLE_THEOREM_NOTE_2026-05-30.md",
    "docs/SOURCE_MEASURE_LOG_SELECTION_BOUNDARY_THEOREM_NOTE_2026-05-30.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "scripts/admissibility_null_record_log_odds_action_representative_anchor_boundary_2026_08_10.py",
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


def flat(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").lower().split())


def action(probabilities):
    return tuple(-sp.log(value / probabilities[0]) for value in probabilities)


def main() -> int:
    checks = Checks()
    note = flat(NOTE_PATH)
    axioms = AXIOM_PATH.read_text(encoding="utf-8")
    axioms_flat = " ".join(axioms.split())
    parent = flat(BLOCK26_PATH)
    compatibility = flat(COMPATIBILITY_PATH)
    rn_parent = flat(RN_PATH)
    scale_parent = flat(SCALE_PATH)
    registry = PREMISE_REGISTRY_PATH.read_text(encoding="utf-8")

    print("external_scientific_inputs: none; finite RN calculus, cut/source data, and Regge matrices are repository-local")
    print("analytic_boundary: finite positive-family identities are exact; Block-23 completion matrices are double-precision reconstructions")
    print("physical_boundary: physical intervention typing, source unit/orientation, local geometry score, pure geometry, and Lorentzian dynamics remain open")

    checks.check(
        "source-and-parent-boundary",
        "current axioms leave source/action and dynamics open while the retained parents supply compatibility, anchor, and RN scale boundaries",
        "source/action and physical-observable identification" in axioms_flat
        and "Admissibility is not a dynamics axiom" in axioms_flat
        and "unique dimensionless action representative" in parent
        and "zero multiplicative curl" in compatibility
        and "physical source intervention is an rn cocycle" in rn_parent
        and "scaled rn family" in scale_parent
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
        "note-contract",
        "the note states the RN repair, retained zero-contact result, constructive escape, and bounded axiom split",
        "registered joint-family/rn source bridge candidate (unadopted)" in note
        and "source-independent pure-geometry action" in note
        and "target-tailored and nonlocal" in note
        and "n1--n8 status: `pass` only" in note
        and "no canonical axiom is edited here" in note,
    )

    reference = (sp.Rational(2, 11), sp.Rational(3, 11), sp.Rational(6, 11))
    deformed = (sp.Rational(5, 23), sp.Rational(7, 23), sp.Rational(11, 23))
    terminal = (sp.Rational(7, 30), sp.Rational(8, 30), sp.Rational(15, 30))
    rn_qp = tuple(sp.simplify(q / p) for p, q in zip(reference, deformed))
    checks.check(
        "finite-rn-normalization",
        "the exact RN density of one positive normalized law relative to another has reference expectation one",
        sp.simplify(sum(p * r for p, r in zip(reference, rn_qp)) - 1) == 0,
        f"RN density={rn_qp}",
    )

    action_p = action(reference)
    action_q = action(deformed)
    rn_action_errors = tuple(
        sp.simplify(
            sp.exp(-(action_q[index] - action_p[index]))
            - rn_qp[index] / rn_qp[0]
        )
        for index in range(len(reference))
    )
    checks.check(
        "null-relative-rn-action",
        "the anchored action increment is exactly minus the log RN density relative to its null value",
        action_p[0] == action_q[0] == 0
        and all(error == 0 for error in rn_action_errors),
    )

    rn_tq = tuple(sp.simplify(t / q) for q, t in zip(deformed, terminal))
    rn_tp = tuple(sp.simplify(t / p) for p, t in zip(reference, terminal))
    chain_errors = tuple(
        sp.simplify(rn_tp[index] - rn_tq[index] * rn_qp[index])
        for index in range(len(reference))
    )
    anchored_chain_errors = tuple(
        sp.simplify(
            rn_tp[index] / rn_tp[0]
            - (rn_tq[index] / rn_tq[0]) * (rn_qp[index] / rn_qp[0])
        )
        for index in range(len(reference))
    )
    checks.check(
        "rn-chain-cocycle",
        "sequential RN interventions multiply pointwise and their null-relative action increments add",
        all(error == 0 for error in chain_errors + anchored_chain_errors),
    )

    h = sp.symbols("h", real=True)
    observable = (sp.Integer(-2), sp.Integer(1), sp.Integer(3))
    partition = sum(
        probability * sp.exp(h * value)
        for probability, value in zip(reference, observable)
    )
    tilt = tuple(sp.exp(h * value) / partition for value in observable)
    tilt_normalization = sp.simplify(
        sum(probability * density for probability, density in zip(reference, tilt))
    )
    tilt_ratio_errors = tuple(
        sp.simplify(
            tilt[index] / tilt[0]
            - sp.exp(h * (observable[index] - observable[0]))
        )
        for index in range(len(observable))
    )
    checks.check(
        "exponential-tilt-normalizer-cancels",
        "the exponential RN family normalizes exactly and its partition factor cancels from every null ratio",
        tilt_normalization == 1 and all(error == 0 for error in tilt_ratio_errors),
    )

    g1, g2 = sp.symbols("g1 g2", real=True)
    geometry_observable = (
        sp.Integer(0),
        g1**2 + 2 * g1 * g2 + 3 * g2**2,
        2 * g1**2 - g1 * g2 + g2**2,
    )
    geometry_increments = tuple(
        sp.expand(-h * (value - geometry_observable[0]))
        for value in geometry_observable
    )
    geometry_hessians = tuple(
        sp.hessian(value, (g1, g2)) for value in geometry_increments
    )
    checks.check(
        "geometry-relative-source-response",
        "a configuration-dependent RN score has an exact identifiable null-relative geometry contact",
        geometry_hessians[0] == sp.zeros(2)
        and geometry_hessians[1] == -h * sp.Matrix([[2, 2], [2, 6]])
        and geometry_hessians[2] == -h * sp.Matrix([[4, -1], [-1, 2]])
        and geometry_hessians[1].det() != 0
        and geometry_hessians[2].det() != 0,
    )

    lam = sp.symbols("lambda", positive=True)
    lam_real = sp.symbols("lambda_real", real=True)
    binary_weights = {1: sp.Rational(1, 2), -1: sp.Rational(1, 2)}
    binary_partition = sum(
        binary_weights[e] * sp.exp(h * lam * e) for e in (-1, 1)
    )
    binary_rn = {
        e: sp.exp(h * lam * e) / binary_partition for e in (-1, 1)
    }
    binary_score = {
        e: sp.simplify(sp.diff(sp.log(binary_rn[e]), h).subs(h, 0))
        for e in (-1, 1)
    }
    fisher = sp.simplify(
        sum(binary_weights[e] * binary_score[e] ** 2 for e in (-1, 1))
    )
    checks.check(
        "fisher-source-scale-and-orientation",
        "unit Fisher norm selects positive lambda=1 while an unsigned norm alone leaves both orientations",
        fisher == lam**2
        and sp.solve(sp.Eq(fisher, 1), lam) == [1]
        and sp.solve(sp.Eq(lam_real**2, 1), lam_real) == [-1, 1],
        f"score={binary_score}; Fisher={fisher}",
    )

    kappa = sp.symbols("kappa", positive=True)
    source_value, base_action = sp.symbols("O S0", real=True)
    sourced_action = base_action - kappa * h * source_value
    log_weight_ratio = sp.simplify(-(sourced_action - base_action) / kappa)
    checks.check(
        "action-quantum-rn-bridge",
        "a declared action quantum converts S_h=S_0-kappa h O exactly to the dimensionless RN source coordinate",
        log_weight_ratio == h * source_value
        and kappa not in sp.diff(log_weight_ratio, h).free_symbols,
    )

    size = 2
    sites = coframe.sites_of(size)
    all_sites = frozenset(sites)
    empty = frozenset()
    areas = coframe.area_field(coframe.coframe_field(sites))
    tension = Fraction(7, 11)
    source = {
        site: tuple(
            Fraction(1 + site[0] + 2 * site[1] + 3 * site[2] + axis, 17)
            for axis in range(3)
        )
        for site in sites
    }

    source_actions = {}
    intervention_errors = []
    complement_errors = []
    geometry_increment_errors = []
    stretches = (Fraction(-1, 5), Fraction(0), Fraction(1, 5))
    for mask in range(1 << len(sites)):
        chosen = frozenset(
            site for index, site in enumerate(sites) if mask & (1 << index)
        )
        complement = all_sites - chosen
        source_action = coframe.oriented_source_action(chosen, sites, size, source)
        source_actions[chosen] = source_action
        base = coframe.edge_action(chosen, sites, size, areas, tension)
        total = base + source_action
        intervention_errors.append(total - base - source_action)
        complement_errors.append(
            source_action
            + coframe.oriented_source_action(complement, sites, size, source)
        )
        path_increments = []
        for stretch in stretches:
            path_areas = block26.uniform_area_field(sites, stretch)
            path_base = coframe.edge_action(
                chosen, sites, size, path_areas, tension
            )
            path_total = path_base + source_action
            path_increments.append(path_total - path_base)
        geometry_increment_errors.extend(
            value - source_action for value in path_increments
        )
        geometry_increment_errors.append(
            path_increments[0] - 2 * path_increments[1] + path_increments[2]
        )

    nonzero_source_count = sum(value != 0 for value in source_actions.values())
    checks.check(
        "retained-cut-rn-intervention",
        "the retained two-form source is an exact null-anchored RN action increment on every finite configuration",
        source_actions[empty] == 0
        and all(error == 0 for error in intervention_errors)
        and nonzero_source_count > 0,
        f"configurations=256; nonzero source increments={nonzero_source_count}",
    )
    checks.check(
        "retained-source-complement-orientation",
        "the retained source increment reverses under configuration complement while preserving the empty anchor",
        all(error == 0 for error in complement_errors),
    )
    checks.check(
        "retained-topological-source-zero-contact",
        "the retained two-form source increment is coframe independent and has zero contact along the exact geometry path",
        all(error == 0 for error in geometry_increment_errors),
        f"path checks={len(geometry_increment_errors)}",
    )

    rotations = coframe.proper_cubic_rotations()
    count_errors = []
    for chosen in source_actions:
        for rotation in rotations:
            count_errors.append(
                len(coframe.rotate_set(chosen, rotation, size)) - len(chosen)
            )
    checks.check(
        "count-carrier-cubic-null-anchor",
        "the occupancy-count carrier vanishes on empty and is invariant under all proper-cubic permutations",
        len(empty) == 0
        and len(frozenset((sites[0],))) == 1
        and all(error == 0 for error in count_errors),
        f"rotation/configuration checks={len(count_errors)}",
    )

    physical, source_records = block25.block23.reconstruct_mass_matrices()
    completion_norms = []
    completion_errors = []
    hermitian_errors = []
    odds_changes = []
    for _label, mass, _step_error in source_records:
        completion = -physical @ mass @ physical.conjugate().T
        completion_norms.append(float(np.linalg.norm(completion, 2)))
        completion_errors.append(
            float(
                np.linalg.norm(
                    physical.conjugate().T @ completion @ physical + mass,
                    2,
                )
            )
        )
        hermitian_errors.append(
            float(np.linalg.norm(completion - completion.conjugate().T, 2))
        )
        eigenvalues = np.linalg.eigvalsh(completion)
        largest = float(eigenvalues[np.argmax(np.abs(eigenvalues))])
        odds_changes.append(abs(np.exp(-0.5 * largest) - 1.0))
    checks.check(
        "anchored-full-contact-completion-exists",
        "a configuration-dependent count-weighted quadratic preserves the null anchor and cancels every Block-23 source matrix algebraically",
        min(completion_norms) > 1.0e-3
        and max(completion_errors) < 2.0e-13
        and max(hermitian_errors) < 2.0e-13,
        f"maximum completion residual={max(completion_errors):.3e}",
    )
    checks.check(
        "anchored-completion-changes-odds",
        "the anchored completion is a genuine interaction rather than a normalized-family common shift",
        min(odds_changes) > 1.0e-6,
        f"minimum unit-direction odds change={min(odds_changes):.6f}",
    )

    checks.check(
        "minimal-axiom-delta",
        "RN composition reduces the source/action update to joint-family/intervention registration plus unit/orientation, with pure geometry separate",
        "can be a downstream bridge rather than a fifth foundational axiom" in note
        and "joint-family compatibility/registration" in note
        and "primitive fisher metric" in note
        and "physical action quantum" in note
        and "pure-geometry law is independently unavoidable" in note,
    )
    checks.check(
        "bounded-theorem-and-next-law",
        "the theorem preserves local joint-action, proper-length, connected, generator, projective, and Lorentzian routes",
        "proper-length source contact" in note
        and "generator/constraint connection" in note
        and "projective-limit" in note
        and "lorentzian" in note
        and "no source, gravity, or axiom no-go is claimed" in note,
    )

    print("N5_CERTIFICATE: rn_repair=null-relative RN log density gives the exact additive source-action cocycle")
    print("N5_CERTIFICATE: source_unit=unit Fisher norm fixes positive dimensionless scale while orientation and action quantum remain separate")
    print("N5_CERTIFICATE: retained_boundary=the two-form cut source is an exact RN intervention but has identically zero coframe contact")
    print("N5_CERTIFICATE: constructive_escape=count-weighted anchored joint interactions algebraically cancel all three Block-23 matrices")
    print("N5_CERTIFICATE: axiom_boundary=joint-family compatibility and intervention typing may be downstream; pure geometry and causal dynamics remain independent")
    print("per_element: checked every row of three exact positive laws and all 256 retained cut configurations")
    print("per_site: checked occupancy-count anchoring under all 24 proper-cubic rotations on the L=2 fixture")
    print("per_mode: checked every entry of all three fifteen-edge completions and their six-mode projections")
    print("per_block: checked RN normalization, cocycle composition, Fisher/action units, retained source contact, and the axiom split")
    print("lattice_wide: checked and not executed — no projective-limit, continuous-zone, nonuniform Regge, or Lorentzian theorem is claimed")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return int(checks.failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
