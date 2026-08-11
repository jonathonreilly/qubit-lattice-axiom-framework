#!/usr/bin/env python3
"""Reclassify the homogeneous gravity-contact target before law selection.

Block 28 proves that a source-linear one-cell metric contact can cancel the
three Block-23 homogeneous six-mode matrices, but leaves eleven coefficient
directions unselected.  This runner asks two logically prior questions:

1. Are those six modes in the variational domain of the supplied Block-19
   compact ensemble at zero momentum?
2. Does a fitted one-cell contact extend to differentiated finite-momentum
   Ward data?

The first answer is exactly no: all six modes lie in the constant-metric image
fixed by the ten global constraints.  The second answer is negative only for
the tested one-cell classes.  A stronger direct-edge class improves the
infrared fit but fails held-out finite momenta.  A closed neutral history
supplies a constructive nonuniform escape on the unchanged flat carrier.

This is a phase/ensemble and contact-locality reclassification, not a gravity
no-go and not a selected geometry/history law.
"""

from __future__ import annotations

from itertools import permutations, product
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import admissibility_endogenous_geometry_joint_record_rn_local_covariant_contact_selection_boundary_2026_08_10 as block28  # noqa: E402
import admissibility_closed_helical_defect_history_ward_neutral_ir_regge_response_boundary_2026_08_10 as closed  # noqa: E402


block23 = block28.block23
block22 = block23.block22
regge = block22.regge

AUDIT_TIMEOUT_SEC = 240
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_GLOBAL_CONSTRAINT_PHASE_WARD_CONTACT_RECLASSIFICATION_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
BLOCK19_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_FIXED_METRIC_NONLINEAR_REGGE_KKT_CONTINUATION_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
BLOCK22_PATH = block22.NOTE_PATH
BLOCK28_PATH = block28.NOTE_PATH
CLOSED_PATH = closed.NOTE_PATH
PREMISE_REGISTRY_PATH = (
    ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
)

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_GLOBAL_CONSTRAINT_PHASE_WARD_CONTACT_RECLASSIFICATION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_FIXED_METRIC_NONLINEAR_REGGE_KKT_CONTINUATION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/ADMISSIBILITY_SOURCED_REGGE_FLAT_GAUGE_QUOTIENT_WARD_COMPLETION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/ADMISSIBILITY_ENDOGENOUS_GEOMETRY_JOINT_RECORD_RN_LOCAL_COVARIANT_CONTACT_SELECTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/ADMISSIBILITY_CLOSED_HELICAL_DEFECT_HISTORY_WARD_NEUTRAL_IR_REGGE_RESPONSE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "scripts/admissibility_endogenous_geometry_joint_record_rn_local_covariant_contact_selection_boundary_2026_08_10.py",
    "scripts/admissibility_null_record_rn_cocycle_source_unit_gravity_contact_boundary_2026_08_10.py",
    "scripts/admissibility_sourced_regge_joint_ward_schur_completion_boundary_2026_08_10.py",
    "scripts/admissibility_sourced_regge_flat_gauge_quotient_ward_completion_boundary_2026_08_10.py",
    "scripts/admissibility_regge_curvature_squared_nonflat_continuation_2026_08_10.py",
    "scripts/admissibility_fixed_metric_nonlinear_regge_kkt_continuation_2026_08_10.py",
    "scripts/admissibility_flat_regge_curvature_squared_branch_lift_2026_08_10.py",
    "scripts/admissibility_compact_regge_homogeneous_reaction_rank_kkt_boundary_2026_08_10.py",
    "scripts/admissibility_closed_helical_defect_history_ward_neutral_ir_regge_response_boundary_2026_08_10.py",
    "scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py",
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


def numerical_rank(matrix: np.ndarray, relative: float = 1.0e-10) -> int:
    singular = np.linalg.svd(matrix, compute_uv=False)
    if len(singular) == 0 or singular[0] == 0.0:
        return 0
    return int(np.sum(singular > singular[0] * relative))


def nullspace(matrix: np.ndarray, relative: float = 1.0e-10) -> np.ndarray:
    _left, singular, right = np.linalg.svd(matrix, full_matrices=True)
    rank = int(np.sum(singular > singular[0] * relative))
    return right[rank:].conjugate().T


def edge_contact_orbits():
    """S4 orbits of J_e u_f u_g for fifteen source/geometry edges."""
    directions = tuple(tuple(item) for item in regge.DIRS15)
    direction_index = {
        direction: index for index, direction in enumerate(directions)
    }
    group = tuple(permutations(range(4)))

    def edge_map(edge: int, permutation: tuple[int, ...]) -> int:
        transformed = [0, 0, 0, 0]
        for old_axis in range(4):
            transformed[permutation[old_axis]] = directions[edge][old_axis]
        return direction_index[tuple(transformed)]

    def act(triple, permutation):
        source, left, right = triple
        new_left = edge_map(left, permutation)
        new_right = edge_map(right, permutation)
        return (
            edge_map(source, permutation),
            min(new_left, new_right),
            max(new_left, new_right),
        )

    unseen = {
        (source, left, right)
        for source in range(15)
        for left in range(15)
        for right in range(left, 15)
    }
    orbits = []
    while unseen:
        representative = min(unseen)
        orbit = {act(representative, item) for item in group}
        orbits.append(tuple(sorted(orbit)))
        unseen -= orbit
    return tuple(orbits)


def edge_orbit_hessians(
    source: np.ndarray, orbits
) -> tuple[np.ndarray, ...]:
    hessians = []
    for orbit in orbits:
        hessian = np.zeros((15, 15), dtype=float)
        for source_edge, left, right in orbit:
            hessian[left, right] += source[source_edge]
            if left != right:
                hessian[right, left] += source[source_edge]
        hessians.append(hessian)
    return tuple(hessians)


def derivative_kernel_pairs():
    """Reconstruct the three Block-22 uniform-source tangent kernels."""
    block22.block21.mp.mp.dps = 40
    exact_basis = block22.block19.exact_normal_basis(block22.block21.mp)
    basis = np.asarray(exact_basis, dtype=float)
    flat_lengths = np.sqrt(
        np.asarray([sum(item) for item in regge.DIRS15], dtype=float)
    )
    flat_normal = block22.block21.normal_action(
        [block22.block21.mp.mpf(0) for _ in range(5)], exact_basis
    )
    flat_hessian = block22.block21.mp.matrix(flat_normal.hess)
    out = []
    for source in block22.block19.reaction.exact_source_rows():
        target = block22.block19.exact_source_target(
            source, block22.block21.sp.Rational(1, 1), block22.block21.mp
        )
        tangent = block22.block21.mp.lu_solve(flat_hessian, target)
        tangent_lengths = basis @ np.asarray(tangent, dtype=float).reshape(5)
        pairs = []
        for step in (1.0e-4, 5.0e-5):
            pairs.append(
                (
                    step,
                    block22.make_kernel(flat_lengths + step * tangent_lengths),
                    block22.make_kernel(flat_lengths - step * tangent_lengths),
                )
            )
        out.append(tuple(pairs))
    return tuple(out)


def derivative_at(pairs, momentum: np.ndarray) -> np.ndarray:
    derivatives = [
        (
            block22.block20.bloch(plus, momentum)
            - block22.block20.bloch(minus, momentum)
        )
        / (2.0 * step)
        for step, plus, minus in pairs
    ]
    return (4.0 * derivatives[1] - derivatives[0]) / 3.0


def metric_ward_system(momentum, sources, orbits, kernel_pairs):
    """Gauge-gauge differentiated-Ward system for metric-cell contacts."""
    momentum = np.asarray(momentum, dtype=float)
    metric_map = regge.metric_map(momentum)
    gauge = regge.gauge_map(momentum)
    metric_gauge = np.linalg.pinv(metric_map, rcond=1.0e-12) @ gauge
    map_residual = float(
        np.linalg.norm(metric_map @ metric_gauge - gauge, 2)
    )
    rows = []
    targets = []
    for source, pairs in zip(sources, kernel_pairs):
        rows.append(
            np.stack(
                [
                    block28.hermitian_vector(
                        metric_gauge.conjugate().T
                        @ hessian
                        @ metric_gauge
                    )
                    for hessian in block28.orbit_hessians(source, orbits)
                ],
                axis=1,
            )
        )
        derivative = derivative_at(pairs, momentum)
        targets.append(
            -block28.hermitian_vector(
                gauge.conjugate().T @ derivative @ gauge
            )
        )
    return np.vstack(rows), np.concatenate(targets), map_residual


def edge_ward_system(momentum, sources, orbits, kernel_pairs):
    """Gauge-gauge differentiated-Ward system for direct-edge contacts."""
    momentum = np.asarray(momentum, dtype=float)
    gauge = regge.gauge_map(momentum)
    rows = []
    targets = []
    for source, pairs in zip(sources, kernel_pairs):
        rows.append(
            np.stack(
                [
                    block28.hermitian_vector(
                        gauge.conjugate().T @ hessian @ gauge
                    )
                    for hessian in edge_orbit_hessians(source, orbits)
                ],
                axis=1,
            )
        )
        derivative = derivative_at(pairs, momentum)
        targets.append(
            -block28.hermitian_vector(
                gauge.conjugate().T @ derivative @ gauge
            )
        )
    return np.vstack(rows), np.concatenate(targets)


def stack_system(builder, momenta):
    records = [builder(momentum) for momentum in momenta]
    return (
        np.vstack([record[0] for record in records]),
        np.concatenate([record[1] for record in records]),
    )


def main() -> int:
    checks = Checks()
    note = flat(NOTE_PATH)
    axioms = flat(AXIOM_PATH)
    block19_note = flat(BLOCK19_PATH)
    block22_note = flat(BLOCK22_PATH)
    block28_note = flat(BLOCK28_PATH)
    closed_note = flat(CLOSED_PATH)
    registry = PREMISE_REGISTRY_PATH.read_text(encoding="utf-8")

    print("external_scientific_inputs: none; compact constraints, source tangents, Ward maps, and closed histories are repository-local")
    print("analytic_boundary: constraint-subspace and orbit statements are exact finite algebra; source-tangent and finite-momentum fits are double precision")
    print("physical_boundary: phase/ensemble selection, Record-to-geometry compilation, projective gluing, causal update, and Lorentzian nonlinear stability remain open")

    checks.check(
        "axiom-and-parent-boundary",
        "current axioms do not select a geometry action, source law, dynamics, or compact ensemble, while the parents expose each supplied choice",
        "admissibility is not a dynamics axiom" in axioms
        and "source/action and physical-observable identification" in axioms
        and "ten affine constraints" in block19_note
        and "inherited flat gauge map" in block22_note
        and "11-dimensional coefficient nullspace" in block28_note
        and "background-subtracted pair" in closed_note
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
        "the note reclassifies the homogeneous target, reports both one-cell tests, preserves constructive gravity routes, and states N1--N8",
        "phase/ensemble ordering correction" in note
        and "142 direct-edge orbits" in note
        and "held-out finite-momentum ward data" in note
        and "not a gravity no-go" in note
        and "n1--n8 status:" in note
        and "pass" in note
        and "no canonical axiom is edited here" in note,
    )

    physical, source_records = block23.reconstruct_mass_matrices()
    metric_map_zero = np.asarray(
        block22.block19.reaction.exact_metric_map().evalf(), dtype=float
    )
    metric_projection = (
        metric_map_zero @ np.linalg.pinv(metric_map_zero) @ physical
    )
    constraint_matrix = metric_map_zero.T @ physical
    constraint_singular = np.linalg.svd(
        constraint_matrix, compute_uv=False
    )
    checks.check(
        "six-modes-excluded-by-global-k0-constraints",
        "all six Block-23 modes lie in the constant-metric image and have zero intersection with the Block-19 allowed k0 tangent ker(M0^T)",
        physical.shape == (15, 6)
        and np.linalg.norm(metric_projection - physical, 2) < 1.0e-12
        and np.linalg.matrix_rank(constraint_matrix, tol=1.0e-10) == 6
        and float(np.min(constraint_singular)) > 0.45,
        "image residual="
        f"{np.linalg.norm(metric_projection - physical, 2):.3e}; "
        f"constraint singular values={np.array2string(constraint_singular, precision=6)}",
    )

    length = 5
    fourier_sums = []
    for index in product(range(length), repeat=4):
        if index == (0, 0, 0, 0):
            continue
        momentum = 2.0 * np.pi * np.asarray(index, dtype=float) / length
        total = sum(
            np.exp(1j * np.dot(momentum, np.asarray(site, dtype=float)))
            for site in product(range(length), repeat=4)
        )
        fourier_sums.append(abs(total))
    checks.check(
        "uniform-background-nonzero-mode-stationarity",
        "translation invariance makes a uniform first variation orthogonal to every nonzero Bloch mode; only the constrained compact mode needs reactions",
        len(fourier_sums) == length**4 - 1
        and max(fourier_sums) < 2.0e-12,
        f"L={length}; nonzero modes={len(fourier_sums)}; maximum structure sum={max(fourier_sums):.3e}",
    )

    sources = tuple(
        np.asarray(item.evalf(), dtype=float).reshape(15)
        for item in block22.block19.reaction.exact_source_rows()
    )
    metric_orbits = block28.contact_orbits()
    metric_fit = block28.fit_local_contact(
        physical, source_records, sources, metric_orbits
    )
    checks.check(
        "homogeneous-contact-target-is-conditional",
        "the Block-28 target is exactly recoverable on the six excluded k0 modes but remains an unselected massless-phase continuation condition",
        metric_fit["rank"] == 50
        and metric_fit["nullspace"].shape == (61, 11)
        and np.linalg.norm(
            metric_fit["design"] @ metric_fit["coefficients"]
            - metric_fit["target"]
        )
        / np.linalg.norm(metric_fit["target"])
        < 1.0e-9
        and "supplied affine compact ensemble" in block19_note
        and "massless phase" in block22_note,
    )

    kernel_pairs = derivative_kernel_pairs()
    held_out_momenta = (
        block22.LOWER_MOMENTUM,
        block22.UPPER_MOMENTUM,
        np.asarray((0.17, -0.11, 0.07, 0.03)),
        np.asarray((0.31, 0.19, -0.23, 0.13)),
        np.asarray((0.70, -0.40, 0.20, 0.50)),
        np.asarray((1.10, 0.80, -0.60, 0.30)),
    )
    metric_records = [
        metric_ward_system(
            momentum, sources, metric_orbits, kernel_pairs
        )
        for momentum in held_out_momenta
    ]
    metric_ward = np.vstack([record[0] for record in metric_records])
    metric_target = np.concatenate([record[1] for record in metric_records])
    metric_map_residual = max(record[2] for record in metric_records)
    metric_null_design = metric_ward @ metric_fit["nullspace"]
    metric_rhs = (
        metric_target - metric_ward @ metric_fit["coefficients"]
    )
    metric_adjustment, *_ = np.linalg.lstsq(
        metric_null_design, metric_rhs, rcond=1.0e-10
    )
    metric_residual = (
        metric_null_design @ metric_adjustment - metric_rhs
    )
    metric_relative = float(
        np.linalg.norm(metric_residual) / np.linalg.norm(metric_rhs)
    )
    checks.check(
        "metric-one-cell-ward-selection-misses",
        "held-out finite-momentum gauge-gauge Ward data see only four of the eleven homogeneous blind directions and are incompatible with the one-cell metric fit",
        numerical_rank(metric_null_design) == 4
        and metric_relative > 0.75
        and metric_map_residual < 1.0e-12,
        f"rank(WN)={numerical_rank(metric_null_design)}; relative residual={metric_relative:.6f}; metric-gauge map residual={metric_map_residual:.3e}",
    )

    edge_orbits = edge_contact_orbits()
    size_census = {
        size: sum(len(orbit) == size for orbit in edge_orbits)
        for size in (1, 3, 4, 6, 12, 24)
    }
    checks.check(
        "direct-edge-orbit-census",
        "all 1,800 source-edge/geometry-edge-pair one-cell monomials reduce to 142 simultaneous-axis orbits",
        len(edge_orbits) == 142
        and sum(len(orbit) for orbit in edge_orbits) == 15 * 120
        and size_census == {1: 1, 3: 1, 4: 17, 6: 14, 12: 81, 24: 28},
        f"orbit sizes={size_census}",
    )

    edge_projected = []
    for source in sources:
        edge_projected.append(
            tuple(
                physical.conjugate().T @ hessian @ physical
                for hessian in edge_orbit_hessians(source, edge_orbits)
            )
        )
    edge_design = np.vstack(
        [
            np.stack(
                [
                    block28.hermitian_vector(matrix)
                    for matrix in branch
                ],
                axis=1,
            )
            for branch in edge_projected
        ]
    )
    edge_target = np.concatenate(
        [-block28.hermitian_vector(record[1]) for record in source_records]
    )
    edge_coefficients, *_ = np.linalg.lstsq(
        edge_design, edge_target, rcond=1.0e-11
    )
    edge_null = nullspace(edge_design, 1.0e-11)
    edge_base_relative = float(
        np.linalg.norm(edge_design @ edge_coefficients - edge_target)
        / np.linalg.norm(edge_target)
    )
    checks.check(
        "stronger-edge-class-homogeneous-fit",
        "the complete one-cell direct-edge class also fits the conditional homogeneous target, with rank 50 and a 92-dimensional nullspace",
        numerical_rank(edge_design, 1.0e-11) == 50
        and edge_null.shape == (142, 92)
        and edge_base_relative < 1.0e-9,
        f"shape={edge_design.shape}; rank={numerical_rank(edge_design, 1.0e-11)}; nullity={edge_null.shape[1]}; relative residual={edge_base_relative:.3e}",
    )

    training_momenta = tuple(
        value * block22.GENERIC_DIRECTION
        for value in (0.02, 0.05, 0.10, 0.20)
    ) + tuple(
        value * np.eye(4)[axis]
        for value in (0.10, 0.30)
        for axis in range(4)
    )
    train_ward, train_target = stack_system(
        lambda momentum: edge_ward_system(
            momentum, sources, edge_orbits, kernel_pairs
        ),
        training_momenta,
    )
    held_ward, held_target = stack_system(
        lambda momentum: edge_ward_system(
            momentum, sources, edge_orbits, kernel_pairs
        ),
        held_out_momenta,
    )
    train_null = train_ward @ edge_null
    train_rhs = train_target - train_ward @ edge_coefficients
    train_adjustment, *_ = np.linalg.lstsq(
        train_null, train_rhs, rcond=1.0e-10
    )
    trained_coefficients = (
        edge_coefficients + edge_null @ train_adjustment
    )
    train_relative = float(
        np.linalg.norm(train_ward @ trained_coefficients - train_target)
        / np.linalg.norm(train_target)
    )
    held_relative = float(
        np.linalg.norm(held_ward @ trained_coefficients - held_target)
        / np.linalg.norm(held_target)
    )
    trained_base_relative = float(
        np.linalg.norm(edge_design @ trained_coefficients - edge_target)
        / np.linalg.norm(edge_target)
    )
    held_null = held_ward @ edge_null
    held_rhs = held_target - held_ward @ edge_coefficients
    held_adjustment, *_ = np.linalg.lstsq(
        held_null, held_rhs, rcond=1.0e-10
    )
    held_best_relative = float(
        np.linalg.norm(
            held_null @ held_adjustment - held_rhs
        )
        / np.linalg.norm(held_rhs)
    )
    combined_rank = numerical_rank(
        np.vstack((edge_design, held_ward))
    )
    checks.check(
        "direct-edge-ir-fit-held-out-failure",
        "the 142-orbit direct-edge class can learn the small/axis Ward inventory while preserving the homogeneous target, but fails the held-out generic/root-of-unity momenta",
        trained_base_relative < 1.0e-8
        and train_relative < 2.0e-3
        and held_relative > 0.10
        and held_best_relative > 0.20
        and combined_rank >= 120,
        f"training relative={train_relative:.6e}; held-out relative={held_relative:.6f}; held-out best within homogeneous null={held_best_relative:.6f}; combined rank={combined_rank}",
    )

    closed_length = 5
    closed_nonzero = 0
    closed_dynamic = 0
    worst_gauge = 0.0
    worst_full_null = 0.0
    worst_solve = 0.0
    for index in product(range(closed_length), repeat=4):
        momentum = 2.0 * np.pi * np.asarray(index, dtype=float) / closed_length
        momentum = (momentum + np.pi) % (2.0 * np.pi) - np.pi
        source = closed.neutral_pair_row(closed_length, momentum)
        worst_gauge = max(
            worst_gauge,
            float(np.linalg.norm(source @ regge.gauge_map(momentum))),
        )
        if np.linalg.norm(source) < 1.0e-10:
            continue
        closed_nonzero += 1
        closed_dynamic += int(abs(momentum[3]) > 1.0e-10)
        data = closed.source_data(source, momentum)
        worst_full_null = max(
            worst_full_null, float(data["null"])
        )
        worst_solve = max(worst_solve, float(data["solve"]))
    zero_source = closed.neutral_pair_row(
        closed_length, np.zeros(4)
    )
    checks.check(
        "closed-neutral-history-constructive-escape",
        "an unchanged flat Regge carrier accepts the complete L=5 neutral closed-history inventory with exact compact cancellation and unprojected Ward-compatible solves",
        closed_nonzero == 100
        and closed_dynamic == 80
        and np.linalg.norm(zero_source) == 0.0
        and worst_gauge < 1.0e-11
        and worst_full_null < 1.0e-10
        and worst_solve < 1.0e-10,
        f"nonzero/dynamic={closed_nonzero}/{closed_dynamic}; gauge={worst_gauge:.3e}; full-null={worst_full_null:.3e}; solve={worst_solve:.3e}",
    )

    checks.check(
        "phase-ensemble-ordering-correction",
        "massless-contact coefficient selection is downstream of selecting the compact/open ensemble and massless versus curved or massive sourced phase",
        "phase/ensemble selection precedes coefficient selection" in note
        and "excluded at k=0" in note
        and "global-only extension" in note
        and "curved or massive phase" in note,
    )
    checks.check(
        "minimal-axiom-or-downstream-delta",
        "the exact missing law is a compatible geometry-bearing joint Record/history family that selects its ensemble, source typing, full Ward connection, and causal update",
        "compatible geometry-bearing joint record/history family" in note
        and "record-to-geometry map" in note
        and "projective" in note
        and "full differentiated ward identity" in note
        and "autonomous causal update" in note
        and "can remain downstream" in note,
    )
    checks.check(
        "bounded-theorem-and-live-routes",
        "the scoped one-cell failure preserves inter-cell contacts, connection/tadpole terms, full stationary backgrounds, closed histories, refined actions, and Lorentzian routes",
        "not a gravity no-go" in note
        and "inter-cell" in note
        and "connection/tadpole" in note
        and "closed histories" in note
        and "refined/perfect action" in note
        and "lorentzian" in note,
    )

    print("N5_CERTIFICATE: reclassification=the six homogeneous contact targets are transverse curvatures of modes excluded by the supplied global k0 constraints, not on-domain k0 Hessian entries")
    print("N5_CERTIFICATE: one_cell_boundary=metric and stronger direct-edge axis-covariant one-cell contacts do not extend the homogeneous fit to the held-out finite-momentum differentiated-Ward inventory")
    print("N5_CERTIFICATE: constructive_escape=the L5 neutral closed history solves every sourced mode on the unchanged flat Regge carrier without source projection")
    print("N5_CERTIFICATE: priority_order=select the physical ensemble and massless-versus-curved phase before selecting homogeneous contact coefficients")
    print("N5_CERTIFICATE: axiom_boundary=a compatible geometry-bearing joint Record/history law, full Ward connection, and causal update may be derived downstream or explicitly registered; no fifth axiom is proven necessary")
    print("per_element: checked all 825 metric-contact and 1,800 direct-edge-contact monomials through their complete S4 orbit classes")
    print("per_site: checked one complete fifteen-edge cell plus every site of the L5 neutral closed-history torus")
    print("per_mode: checked the six homogeneous modes, 12 training momenta, six held-out momenta, and all 625 L5 torus momenta")
    print("per_block: checked compact constraint-domain typing, metric and edge contact classes, differentiated Ward data, and the closed-history escape")
    print("lattice_wide: checked one complete L5 finite torus; no arbitrary-volume, continuous-zone, projective, Lorentzian, or nonlinear theorem is claimed")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return int(checks.failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
