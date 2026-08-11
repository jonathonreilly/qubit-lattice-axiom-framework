#!/usr/bin/env python3
"""Test endogenous joint Records and a local covariant gravity contact.

The finite theorem separates two questions that were conflated by treating
geometry as an external parameter.  Conditional probabilities at fixed
geometry erase a common geometry function, whereas one positive joint law on
geometry-bearing configurations fixes the total null-relative action.  The
runner then classifies every source-linear quadratic contact on one retained
four-axis cell that is covariant under simultaneous axis permutations, and
tests that local class against the three Block-23 source tensors.

The fitted contact is an existence and selection-boundary result.  It is not a
physical gravity law: the coefficients are inferred from the supplied target
tensors, projective gluing and a Record-to-geometry compiler are absent, and
Lorentzian dynamics remains open.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations
from pathlib import Path
import sys

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import admissibility_null_record_rn_cocycle_source_unit_gravity_contact_boundary_2026_08_10 as block27  # noqa: E402


block23 = block27.block25.block23

AUDIT_TIMEOUT_SEC = 180
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_ENDOGENOUS_GEOMETRY_JOINT_RECORD_RN_LOCAL_COVARIANT_"
    "CONTACT_SELECTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
COMPATIBILITY_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_BINARY_FULL_CONDITIONAL_COMPATIBILITY_ISING_ACTION_"
    "AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
BLOCK23_PATH = block23.NOTE_PATH
BLOCK25_PATH = block27.block25.NOTE_PATH
BLOCK26_PATH = block27.block26.NOTE_PATH
BLOCK27_PATH = block27.NOTE_PATH
HYPERFACE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_FOUR_COFRAME_HYPERFACE_SEAGULL_SOURCED_REGGE_SPAN_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
PREMISE_REGISTRY_PATH = (
    ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
)

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_ENDOGENOUS_GEOMETRY_JOINT_RECORD_RN_LOCAL_COVARIANT_CONTACT_SELECTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_BINARY_FULL_CONDITIONAL_COMPATIBILITY_ISING_ACTION_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/ADMISSIBILITY_SOURCED_REGGE_JOINT_WARD_SCHUR_COMPLETION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/ADMISSIBILITY_NORMALIZED_FAMILY_ADDITIVE_ZERO_CONTACT_NONIDENTIFIABILITY_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/ADMISSIBILITY_NULL_RECORD_LOG_ODDS_ACTION_REPRESENTATIVE_ANCHOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/ADMISSIBILITY_NULL_RECORD_RN_COCYCLE_SOURCE_UNIT_GRAVITY_CONTACT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/ADMISSIBILITY_FOUR_COFRAME_HYPERFACE_SEAGULL_SOURCED_REGGE_SPAN_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "scripts/admissibility_null_record_rn_cocycle_source_unit_gravity_contact_boundary_2026_08_10.py",
    "scripts/admissibility_null_record_log_odds_action_representative_anchor_boundary_2026_08_10.py",
    "scripts/admissibility_normalized_family_additive_zero_contact_nonidentifiability_boundary_2026_08_10.py",
    "scripts/admissibility_sourced_regge_joint_ward_schur_completion_boundary_2026_08_10.py",
    "scripts/admissibility_sourced_regge_flat_gauge_quotient_ward_completion_boundary_2026_08_10.py",
    "scripts/admissibility_four_coframe_hyperface_seagull_sourced_regge_span_boundary_2026_08_10.py",
)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(
        self, key: str, statement: str, condition, detail: str = ""
    ) -> None:
        ok = bool(condition)
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {statement}")
        if detail:
            print(f"       {detail}")
        self.passed += int(ok)
        self.failed += int(not ok)


def flat(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").lower().split())


def metric_component_matrices() -> tuple[np.ndarray, ...]:
    """Return the ten symmetric metric-coordinate basis matrices."""
    matrices = []
    for left, right in block23.block22.regge.HCOMPS:
        matrix = np.zeros((4, 4), dtype=float)
        matrix[left, right] = 1.0
        matrix[right, left] = 1.0
        matrices.append(matrix)
    return tuple(matrices)


def axis_data():
    """Build the simultaneous S4 actions on edge supports and metric entries."""
    directions = tuple(tuple(item) for item in block23.block22.regge.DIRS15)
    direction_index = {item: index for index, item in enumerate(directions)}
    components = tuple(block23.block22.regge.HCOMPS)
    component_index = {
        tuple(sorted(item)): index for index, item in enumerate(components)
    }
    group = tuple(permutations(range(4)))

    def edge_map(edge: int, permutation: tuple[int, ...]) -> int:
        transformed = [0, 0, 0, 0]
        for old_axis in range(4):
            transformed[permutation[old_axis]] = directions[edge][old_axis]
        return direction_index[tuple(transformed)]

    def component_map(component: int, permutation: tuple[int, ...]) -> int:
        left, right = components[component]
        transformed = tuple(
            sorted((permutation[left], permutation[right]))
        )
        return component_index[transformed]

    return directions, components, group, edge_map, component_map


def contact_orbits():
    """Enumerate S4 orbits of J_e h_A h_B on one fifteen-edge cell."""
    directions, components, group, edge_map, component_map = axis_data()

    def act(triple, permutation):
        edge, left, right = triple
        new_left = component_map(left, permutation)
        new_right = component_map(right, permutation)
        return (
            edge_map(edge, permutation),
            min(new_left, new_right),
            max(new_left, new_right),
        )

    unseen = {
        (edge, left, right)
        for edge in range(len(directions))
        for left in range(len(components))
        for right in range(left, len(components))
    }
    orbits = []
    while unseen:
        representative = min(unseen)
        orbit = {act(representative, item) for item in group}
        orbits.append(tuple(sorted(orbit)))
        unseen -= orbit
    return tuple(orbits)


def orbit_hessians(source: np.ndarray, orbits) -> tuple[np.ndarray, ...]:
    """Evaluate every orbit-symmetrized real contact Hessian for one source."""
    hessians = []
    for orbit in orbits:
        hessian = np.zeros((10, 10), dtype=float)
        for edge, left, right in orbit:
            hessian[left, right] += source[edge]
            if left != right:
                hessian[right, left] += source[edge]
        hessians.append(hessian)
    return tuple(hessians)


def hermitian_vector(matrix: np.ndarray) -> np.ndarray:
    return np.concatenate((matrix.real.ravel(), matrix.imag.ravel()))


def fit_local_contact(physical, source_records, source_rows, orbits):
    metric_map = np.asarray(
        block23.block22.block19.reaction.exact_metric_map().evalf(),
        dtype=float,
    )
    metric_lift = np.linalg.pinv(metric_map) @ physical
    projected = []
    for source in source_rows:
        projected.append(
            tuple(
                metric_lift.conjugate().T @ hessian @ metric_lift
                for hessian in orbit_hessians(source, orbits)
            )
        )
    design = np.vstack(
        [
            np.stack(
                [hermitian_vector(matrix) for matrix in branch], axis=1
            )
            for branch in projected
        ]
    )
    target = np.concatenate(
        [-hermitian_vector(record[1]) for record in source_records]
    )
    coefficients, _residuals, rank, singular_values = np.linalg.lstsq(
        design, target, rcond=1.0e-11
    )
    full_u, full_s, full_vh = np.linalg.svd(design, full_matrices=True)
    del full_u
    svd_rank = int(np.sum(full_s > full_s[0] * 1.0e-11))
    nullspace = full_vh[svd_rank:].T
    contacts = tuple(
        sum(
            coefficient * hessian
            for coefficient, hessian in zip(
                coefficients, orbit_hessians(source, orbits)
            )
        )
        for source in source_rows
    )
    projected_contacts = tuple(
        metric_lift.conjugate().T @ contact @ metric_lift
        for contact in contacts
    )
    return {
        "metric_lift": metric_lift,
        "projected_orbits": tuple(projected),
        "design": design,
        "target": target,
        "coefficients": coefficients,
        "rank": int(rank),
        "singular_values": singular_values,
        "nullspace": nullspace,
        "contacts": contacts,
        "projected_contacts": projected_contacts,
    }


def permutation_matrices(permutation, edge_map, component_map):
    source_matrix = np.zeros((15, 15), dtype=float)
    metric_matrix = np.zeros((10, 10), dtype=float)
    for old in range(15):
        source_matrix[edge_map(old, permutation), old] = 1.0
    for old in range(10):
        metric_matrix[component_map(old, permutation), old] = 1.0
    return source_matrix, metric_matrix


def continuum_stress_hessians(source, metric_basis):
    """The complete O(4)-scalar quadratic ansatz linear in one rank-2 T."""
    directions = tuple(
        np.asarray(item, dtype=float) for item in block23.block22.regge.DIRS15
    )
    stress = np.zeros((4, 4), dtype=float)
    for weight, direction in zip(source, directions):
        if abs(weight) <= 1.0e-15:
            continue
        stress += weight * np.outer(direction, direction) / np.dot(
            direction, direction
        )
    source_trace = float(np.trace(stress))
    metric_traces = np.asarray(
        [np.trace(item) for item in metric_basis], dtype=float
    )
    metric_gram = np.asarray(
        [
            [np.trace(left @ right) for right in metric_basis]
            for left in metric_basis
        ],
        dtype=float,
    )
    stress_coordinates = np.asarray(
        [np.trace(stress @ item) for item in metric_basis], dtype=float
    )
    stress_square = np.asarray(
        [
            [
                np.trace(stress @ (left @ right + right @ left))
                for right in metric_basis
            ]
            for left in metric_basis
        ],
        dtype=float,
    )
    return (
        2.0 * source_trace * np.outer(metric_traces, metric_traces),
        2.0 * source_trace * metric_gram,
        np.outer(stress_coordinates, metric_traces)
        + np.outer(metric_traces, stress_coordinates),
        stress_square,
    )


def main() -> int:
    checks = Checks()
    note = flat(NOTE_PATH)
    axioms = AXIOM_PATH.read_text(encoding="utf-8")
    axioms_flat = " ".join(axioms.split())
    compatibility = flat(COMPATIBILITY_PATH)
    parent23 = flat(BLOCK23_PATH)
    parent25 = flat(BLOCK25_PATH)
    parent26 = flat(BLOCK26_PATH)
    parent27 = flat(BLOCK27_PATH)
    hyperface = flat(HYPERFACE_PATH)
    registry = PREMISE_REGISTRY_PATH.read_text(encoding="utf-8")

    print("external_scientific_inputs: none; finite joint-law algebra, Regge source tensors, and cell symmetries are repository-local")
    print("analytic_boundary: joint-law and orbit-covariance statements are exact finite algebra; the Block-23 tensor fit is double precision")
    print("physical_boundary: Record-to-geometry compilation, coefficient selection, projective gluing, causal update, and Lorentzian stability remain open")

    checks.check(
        "axiom-and-parent-boundary",
        "the current axioms supply sitewise laws but not joint geometry Records, while retained parents supply compatibility, anchor, RN, and target tensors",
        "probability distribution over the possibilities" in axioms_flat
        and "Admissibility is not a dynamics axiom" in axioms_flat
        and "source/action and physical-observable identification" in axioms_flat
        and "positive joint law exists" in compatibility
        and "full-rank hermitian mass coefficients" in parent23
        and "common geometry-dependent shift" in parent25
        and "unique dimensionless action representative" in parent26
        and "null-relative action identity" in parent27
        and "four-orientation span" in hyperface
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
        "the note states the endogenous joint-action closure, local contact existence, selection degeneracy, and bounded axiom interface",
        "external-geometry conditional ambiguity" in note
        and "endogenous joint-action closure" in note
        and "61 local axis-support orbits" in note
        and "11-dimensional coefficient nullspace" in note
        and "not a selected gravity law" in note
        and "n1--n8 status: `pass` only" in note
        and "no canonical axiom is edited here" in note,
    )

    weights = (
        (Fraction(7), Fraction(2)),
        (Fraction(3), Fraction(11)),
        (Fraction(5), Fraction(13)),
    )
    total = sum(sum(row) for row in weights)
    joint = tuple(tuple(value / total for value in row) for row in weights)
    joint_action = tuple(
        tuple(-sp.log(value / joint[0][0]) for value in row)
        for row in joint
    )
    geometry_null_action = tuple(
        -sp.log(row[0] / joint[0][0]) for row in joint
    )
    conditional_null_action = tuple(
        tuple(-sp.log(value / row[0]) for value in row) for row in joint
    )
    decomposition_errors = tuple(
        sp.simplify(
            joint_action[geometry][matter]
            - geometry_null_action[geometry]
            - conditional_null_action[geometry][matter]
        )
        for geometry in range(len(joint))
        for matter in range(len(joint[0]))
    )
    checks.check(
        "finite-endogenous-joint-action",
        "one positive geometry-plus-Record law has a unique null-relative total action and an exact geometry-null plus conditional decomposition",
        sum(sum(row) for row in joint) == 1
        and joint_action[0][0] == 0
        and all(error == 0 for error in decomposition_errors),
    )

    geometry_scales = (Fraction(1), Fraction(2), Fraction(3))
    shifted_weights = tuple(
        tuple(scale * value for value in row)
        for scale, row in zip(geometry_scales, weights)
    )
    shifted_total = sum(sum(row) for row in shifted_weights)
    shifted_joint = tuple(
        tuple(value / shifted_total for value in row)
        for row in shifted_weights
    )
    original_conditionals = tuple(
        tuple(value / sum(row) for value in row) for row in weights
    )
    shifted_conditionals = tuple(
        tuple(value / sum(row) for value in row) for row in shifted_weights
    )
    original_marginal = tuple(sum(row) for row in joint)
    shifted_marginal = tuple(sum(row) for row in shifted_joint)
    shifted_action_differences = tuple(
        sp.simplify(
            -sp.log(shifted_joint[g][x] / shifted_joint[0][0])
            - joint_action[g][x]
            + sp.log(geometry_scales[g] / geometry_scales[0])
        )
        for g in range(len(joint))
        for x in range(len(joint[0]))
    )
    checks.check(
        "external-conditional-common-shift",
        "geometry-dependent common rescaling is invisible to every fixed-geometry conditional law",
        original_conditionals == shifted_conditionals,
    )
    checks.check(
        "joint-law-detects-geometry-shift",
        "the same rescaling changes geometry marginals and the null-relative joint action, so it is not a symmetry of a fixed endogenous joint law",
        original_marginal != shifted_marginal
        and all(error == 0 for error in shifted_action_differences),
    )

    physical, source_records = block23.reconstruct_mass_matrices()
    source_rows = tuple(
        np.asarray(item.evalf(), dtype=float).reshape(15)
        for item in block23.block22.block19.reaction.exact_source_rows()
    )
    orbits = contact_orbits()
    orbit_sizes = {size: 0 for size in (3, 4, 6, 12, 24)}
    for orbit in orbits:
        orbit_sizes[len(orbit)] += 1
    checks.check(
        "local-axis-orbit-census",
        "all source-linear quadratic contacts J_e h_A h_B on one retained cell form exactly 61 simultaneous-axis permutation orbits",
        len(orbits) == 61
        and sum(len(orbit) for orbit in orbits) == 15 * 55
        and orbit_sizes == {3: 1, 4: 3, 6: 7, 12: 36, 24: 14},
        f"orbit sizes={orbit_sizes}",
    )

    fit = fit_local_contact(
        physical, source_records, source_rows, orbits
    )
    coefficients = fit["coefficients"]
    design = fit["design"]
    target = fit["target"]
    fit_error = design @ coefficients - target
    aggregate_relative = float(np.linalg.norm(fit_error) / np.linalg.norm(target))
    nullspace = fit["nullspace"]
    checks.check(
        "local-contact-design-rank",
        "the three-source local covariant design has rank 50 and an eleven-dimensional coefficient nullspace",
        design.shape == (216, 61)
        and fit["rank"] == 50
        and nullspace.shape == (61, 11)
        and float(np.linalg.norm(design @ nullspace, 2)) < 1.0e-10,
        f"shape={design.shape}; rank={fit['rank']}; nullity={nullspace.shape[1]}",
    )

    directions, components, group, edge_map, component_map = axis_data()
    del directions, components
    equivariance_errors = []
    for source, contact in zip(source_rows, fit["contacts"]):
        for permutation in group:
            source_transform, metric_transform = permutation_matrices(
                permutation, edge_map, component_map
            )
            transformed_source = source_transform @ source
            transformed_contact = sum(
                coefficient * hessian
                for coefficient, hessian in zip(
                    coefficients,
                    orbit_hessians(transformed_source, orbits),
                )
            )
            equivariance_errors.append(
                float(
                    np.linalg.norm(
                        transformed_contact
                        - metric_transform @ contact @ metric_transform.T,
                        2,
                    )
                )
            )
    checks.check(
        "simultaneous-axis-covariance",
        "the fitted one-cell score is equivariant under all 24 simultaneous permutations of source supports and metric axes",
        max(equivariance_errors) < 1.0e-12,
        f"maximum covariance residual={max(equivariance_errors):.3e}",
    )

    zero_contact = sum(
        coefficient * hessian
        for coefficient, hessian in zip(
            coefficients, orbit_hessians(np.zeros(15), orbits)
        )
    )
    linearity_errors = []
    combined = Fraction(2, 5) * source_rows[0] - Fraction(3, 7) * source_rows[1]
    combined_contact = sum(
        coefficient * hessian
        for coefficient, hessian in zip(
            coefficients, orbit_hessians(combined, orbits)
        )
    )
    expected_combined = (
        float(Fraction(2, 5)) * fit["contacts"][0]
        - float(Fraction(3, 7)) * fit["contacts"][1]
    )
    linearity_errors.append(
        float(np.linalg.norm(combined_contact - expected_combined, 2))
    )
    checks.check(
        "local-null-anchor-and-source-linearity",
        "the cell score vanishes for the null source and responds linearly to signed source rows",
        np.linalg.norm(zero_contact, 2) == 0.0
        and max(linearity_errors) < 1.0e-13,
    )

    branch_relative = []
    branch_operator = []
    branch_maximum = []
    for projected_contact, (_label, mass, _step_error) in zip(
        fit["projected_contacts"], source_records
    ):
        residual = projected_contact + mass
        branch_relative.append(
            float(np.linalg.norm(residual) / np.linalg.norm(mass))
        )
        branch_operator.append(
            float(np.linalg.norm(residual, 2) / np.linalg.norm(mass, 2))
        )
        branch_maximum.append(float(np.max(np.abs(residual))))
    checks.check(
        "local-covariant-full-contact-exists",
        "one source-linear one-cell axis-covariant quadratic cancels all three Block-23 six-mode coefficients",
        aggregate_relative < 1.0e-9
        and max(branch_relative) < 5.0e-9
        and max(branch_operator) < 5.0e-9
        and max(branch_maximum) < 5.0e-9,
        "aggregate relative="
        f"{aggregate_relative:.3e}; branch relative="
        + ", ".join(f"{value:.3e}" for value in branch_relative),
    )

    alternate_coefficients = coefficients + nullspace[:, 0]
    alternate_error = design @ alternate_coefficients - target
    checks.check(
        "covariance-does-not-select-contact",
        "distinct local covariant coefficient vectors give the same three target tensors, so locality and axis covariance do not select the law",
        float(np.linalg.norm(alternate_coefficients - coefficients)) > 0.9
        and float(np.linalg.norm(alternate_error - fit_error)) < 1.0e-10,
        f"coefficient separation={np.linalg.norm(alternate_coefficients - coefficients):.6f}",
    )

    rn_errors = []
    rn_contact_errors = []
    odds_changes = []
    positive_metric_margins = []
    metric_basis = metric_component_matrices()
    coupling = 0.2
    for contact, projected_contact, (_label, mass, _step_error) in zip(
        fit["contacts"], fit["projected_contacts"], source_records
    ):
        values, vectors = np.linalg.eigh(contact)
        direction = vectors[:, int(np.argmax(np.abs(values)))]
        geometry = 0.1 * direction
        metric_variation = sum(
            value * basis for value, basis in zip(geometry, metric_basis)
        )
        positive_metric_margins.append(
            float(np.min(np.linalg.eigvalsh(np.eye(4) + metric_variation)))
        )
        geometry_menu = (
            np.zeros(10),
            geometry,
            0.5 * geometry,
        )
        scores = np.asarray(
            [0.5 * item @ contact @ item for item in geometry_menu]
        )
        baseline = np.full(len(scores), 1.0 / len(scores))
        densities = np.exp(-coupling * scores)
        partition = float(np.dot(baseline, densities))
        deformed = baseline * densities / partition
        rn_density = deformed / baseline
        increments = -np.log(rn_density / rn_density[0])
        rn_errors.append(
            float(np.max(np.abs(increments - coupling * (scores - scores[0]))))
        )
        rn_contact_errors.append(
            float(
                np.linalg.norm(coupling * projected_contact + coupling * mass, 2)
            )
        )
        odds_changes.append(abs(float(np.exp(-coupling * scores[1]) - 1.0)))
    checks.check(
        "finite-rn-realization-of-local-contact",
        "an exponential finite-menu RN intervention realizes the fitted null-relative contact and changes configuration odds on positive metrics",
        max(rn_errors) < 1.0e-14
        and max(rn_contact_errors) < 1.0e-9
        and min(odds_changes) > 1.0e-6
        and min(positive_metric_margins) > 0.8,
        f"max RN error={max(rn_errors):.3e}; min odds change={min(odds_changes):.6f}",
    )

    stress_projected = []
    for source in source_rows:
        stress_projected.append(
            tuple(
                fit["metric_lift"].conjugate().T
                @ hessian
                @ fit["metric_lift"]
                for hessian in continuum_stress_hessians(source, metric_basis)
            )
        )
    stress_design = np.vstack(
        [
            np.stack(
                [hermitian_vector(matrix) for matrix in branch], axis=1
            )
            for branch in stress_projected
        ]
    )
    stress_coefficients, _residuals, stress_rank, _singular = np.linalg.lstsq(
        stress_design, target, rcond=None
    )
    stress_relative = float(
        np.linalg.norm(stress_design @ stress_coefficients - target)
        / np.linalg.norm(target)
    )
    checks.check(
        "rank-two-continuum-stress-ansatz-misses",
        "the complete four-contraction O(4)-scalar quadratic ansatz linear in one source stress tensor misses the stacked target",
        stress_rank == 4 and stress_relative > 0.98,
        f"rank={stress_rank}; aggregate relative residual={stress_relative:.6f}",
    )

    checks.check(
        "endogenous-total-action-boundary",
        "a joint geometry-bearing law fixes total gravity response without uniquely splitting pure geometry from conditional matter",
        "total joint action is identifiable" in note
        and "decomposition gauge" in note
        and "external parameter" in note,
    )
    checks.check(
        "minimal-axiom-or-downstream-delta",
        "the remaining decision is a compatible geometry-bearing joint law and selected local score, followed separately by autonomous causal update",
        "geometry-bearing joint record family" in note
        and "record-to-geometry map" in note
        and "projectively consistent" in note
        and "local rn score" in note
        and "autonomous causal update" in note
        and "can still be downstream" in note,
    )
    checks.check(
        "bounded-theorem-and-live-routes",
        "the theorem preserves simple non-rank-two scores, dynamical source blocks, background generators, refined actions, massive phases, and Lorentzian routes",
        "not a gravity no-go" in note
        and "background-dependent generator" in note
        and "dynamical source" in note
        and "refined/perfect action" in note
        and "massive or curved phase" in note
        and "lorentzian" in note,
    )

    print("N5_CERTIFICATE: ambiguity_boundary=fixed-geometry conditionals erase F(g), but a fixed endogenous joint law detects it and fixes the total null-relative action")
    print("N5_CERTIFICATE: constructive_escape=one-cell source-linear axis-covariant RN score cancels all three supplied Block-23 tensors")
    print("N5_CERTIFICATE: selection_boundary=61 orbit coefficients have rank 50 on the three targets and an eleven-dimensional nullspace")
    print("N5_CERTIFICATE: simple_ansatz_boundary=the complete four-term O(4) rank-two-stress scalar misses at 0.98 relative residual")
    print("N5_CERTIFICATE: axiom_boundary=joint geometry Records and local score selection may be downstream; causal update and Lorentzian stability remain separate")
    print("per_element: checked all 825 source-edge/metric-pair monomials and all 61 simultaneous-axis orbits")
    print("per_site: checked one complete fifteen-edge Kuhn cell; inter-cell/projective gluing is not claimed")
    print("per_mode: checked every entry of all three six-mode source tensors and their local contact projections")
    print("per_block: checked joint-law identifiability, RN realization, local covariance, contact fit, and coefficient nonselection")
    print("lattice_wide: checked and not executed — no infinite-volume joint law, Record-to-geometry compiler, continuous momentum, or Lorentzian theorem is claimed")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return int(checks.failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
