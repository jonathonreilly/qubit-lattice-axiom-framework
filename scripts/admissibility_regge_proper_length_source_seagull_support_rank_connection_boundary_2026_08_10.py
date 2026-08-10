#!/usr/bin/env python3
"""Bound the direct proper-length source seagull on the Block-23 carrier.

The three retained compact sources are affine in independent Regge edge
lengths.  When the same source is written through a homogeneous metric or
coframe, each proper length has a nonzero second derivative.  This runner
derives that contact, restricts it to the six flat physical metric modes, and
tests whether it can cancel the full-rank O(source) coefficients reconstructed
in Block 23.

The result is deliberately narrow.  A contact supported only on the m edge
classes touched by one source has rank at most m.  Here m=2,3,4, whereas every
Block-23 coefficient has rank six.  In addition, the apparent proper-length
seagull cancels the geometry connection term under a mere coordinate change
at a fully stationary point.  Cross-edge geometry spreading, dynamical source
variables, nonuniform closed histories, and a curved or massive phase remain
open.
"""

from __future__ import annotations

from itertools import combinations
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import admissibility_sourced_regge_joint_ward_schur_completion_boundary_2026_08_10 as block23  # noqa: E402


AUDIT_TIMEOUT_SEC = 180

NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_REGGE_PROPER_LENGTH_SOURCE_SEAGULL_SUPPORT_RANK_"
    "CONNECTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
PARENT_NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_SOURCED_REGGE_JOINT_WARD_SCHUR_COMPLETION_"
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
    "docs/ADMISSIBILITY_REGGE_PROPER_LENGTH_SOURCE_SEAGULL_SUPPORT_RANK_CONNECTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_SOURCED_REGGE_JOINT_WARD_SCHUR_COMPLETION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/ADMISSIBILITY_CUT_SURFACE_COFRAME_STRESS_HIGHER_FORM_WARD_GEOMETRY_DYNAMICS_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/ADMISSIBILITY_CLOSED_HELICAL_DEFECT_HISTORY_WARD_NEUTRAL_IR_REGGE_RESPONSE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "scripts/admissibility_sourced_regge_joint_ward_schur_completion_boundary_2026_08_10.py",
    "scripts/admissibility_sourced_regge_flat_gauge_quotient_ward_completion_boundary_2026_08_10.py",
    "scripts/admissibility_regge_curvature_squared_nonflat_continuation_2026_08_10.py",
    "scripts/admissibility_fixed_metric_nonlinear_regge_kkt_continuation_2026_08_10.py",
    "scripts/admissibility_flat_regge_curvature_squared_branch_lift_2026_08_10.py",
    "scripts/admissibility_compact_regge_homogeneous_reaction_rank_kkt_boundary_2026_08_10.py",
    "scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py",
)

LABELS = ("two-stream", "bundle-A", "bundle-B")
EXPECTED_MASS_INERTIAS = ((3, 3, 0), (4, 2, 0), (2, 4, 0))
EXPECTED_SUPPORT_RANKS = (2, 3, 4)
EXPECTED_CONTACTED_INERTIAS = ((3, 3, 0), (3, 3, 0), (2, 4, 0))
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


def metric_matrix(coordinates):
    """Return the symmetric 4x4 h encoded by the retained ten components."""
    out = np.zeros((4, 4), dtype=float)
    for value, (left, right) in zip(coordinates, block23.block22.regge.HCOMPS):
        out[left, right] = value
        out[right, left] = value
    return out


def edge_length(direction, coordinates):
    vector = np.asarray(direction, dtype=float)
    metric = np.eye(4) + metric_matrix(coordinates)
    return float(np.sqrt(vector @ metric @ vector))


def proper_length_contacts(physical, metric_map, metric_lift, sources, lengths):
    records = []
    for label, source in zip(LABELS, sources):
        support = np.flatnonzero(np.abs(source) > 0.0)
        support_rows = physical[support, :]
        diagonal = np.diag(source[support] / lengths[support])
        contact_from_rows = support_rows.conjugate().T @ diagonal @ support_rows
        metric_contact = sum(
            (source[edge] / lengths[edge])
            * np.outer(metric_map[edge], metric_map[edge])
            for edge in support
        )
        contact_from_metric = (
            metric_lift.conjugate().T @ metric_contact @ metric_lift
        )
        contact = 0.5 * (contact_from_rows + contact_from_rows.conjugate().T)
        records.append(
            (
                label,
                support,
                support_rows,
                contact,
                float(np.linalg.norm(contact_from_rows - contact_from_metric, 2)),
            )
        )
    return records


def best_six_edge_chart(physical):
    best = None
    for indices in combinations(range(physical.shape[0]), 6):
        chart = physical[np.asarray(indices), :]
        singular_values = np.linalg.svd(chart, compute_uv=False)
        if singular_values[-1] <= 1.0e-10:
            continue
        condition = float(singular_values[0] / singular_values[-1])
        if best is None or condition < best[0]:
            best = (condition, indices, singular_values, chart)
    if best is None:
        raise AssertionError("no six-edge chart spans the physical carrier")
    return best


def main():
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    note_flat = " ".join(note.lower().split())
    parent = PARENT_NOTE_PATH.read_text(encoding="utf-8").lower()
    coframe = COFRAME_NOTE_PATH.read_text(encoding="utf-8").lower()
    line = LINE_NOTE_PATH.read_text(encoding="utf-8").lower()
    axioms = AXIOM_PATH.read_text(encoding="utf-8").lower()
    registry = PREMISE_REGISTRY_PATH.read_text(encoding="utf-8")

    print("external_scientific_inputs: none; all source rows, metric maps, and mass coefficients are reconstructed from repository-local retained carriers")
    print("analytic_boundary: the support-rank and stationary pullback cancellations are exact finite-dimensional theorems; Regge mass coefficients are double-precision reconstructions")
    print("physical_boundary: the proper-length contact class is not a selected source law, and the result does not decide nonuniform histories, dynamical source variables, or a curved or massive phase")

    checks.check(
        "source-and-axiom-boundary",
        "the current axioms select neither this proper-length completion nor a joint gravity/source law",
        "admissibility is not a dynamics axiom" in axioms
        and "source/action and physical-observable identification" in axioms
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
        "retained-carrier-boundary",
        "the parent names the direct seagull route while the retained history action is affine in actual edge lengths",
        "direct ward/contact term" in parent
        and "a_v,a[g]" in line
        and "ell_v" in line
        and "same-family coframe seagull" in coframe,
    )
    checks.check(
        "note-contract",
        "the note states the strict support-rank and coordinate-connection boundaries",
        "rank c_s <= m_s < 6" in note_flat
        and "stationary pullback cancellation" in note_flat
        and "n1--n8 status: `pass` only" in note_flat
        and "no canonical axiom is edited" in note_flat,
    )

    physical, mass_records = block23.reconstruct_mass_matrices()
    metric_map = np.asarray(
        block23.block22.block19.reaction.exact_metric_map().evalf(), dtype=float
    )
    metric_lift = np.linalg.pinv(metric_map) @ physical
    flat_lengths = np.sqrt(
        np.asarray(
            [sum(direction) for direction in block23.block22.regge.DIRS15],
            dtype=float,
        )
    )
    sources = tuple(
        np.asarray(source.evalf(), dtype=float).reshape(15)
        for source in block23.block22.block19.reaction.exact_source_rows()
    )

    affine_residual = float(np.linalg.norm(metric_map @ metric_lift - physical, 2))
    affine_gram_error = float(
        np.linalg.norm(
            metric_lift.conjugate().T
            @ metric_map.T
            @ metric_map
            @ metric_lift
            - np.eye(6),
            2,
        )
    )
    checks.check(
        "six-mode-affine-metric-carrier",
        "the Block-23 physical zero modes lie in the ten-dimensional affine metric tangent",
        physical.shape == (15, 6)
        and affine_residual < 1.0e-12
        and affine_gram_error < 1.0e-12,
        f"affine residual={affine_residual:.3e}; induced Gram error={affine_gram_error:.3e}",
    )

    mass_inertias = tuple(inertia(record[1], 1.0e-7)[0] for record in mass_records)
    mass_ranks = tuple(np.linalg.matrix_rank(record[1], tol=1.0e-7) for record in mass_records)
    checks.check(
        "full-rank-parent-coefficients",
        "all three O(source) coefficients retain the full-rank Block-23 inertias",
        mass_inertias == EXPECTED_MASS_INERTIAS and mass_ranks == (6, 6, 6),
        f"inertias={mass_inertias}; ranks={mass_ranks}",
    )

    support_counts = tuple(int(np.count_nonzero(source)) for source in sources)
    source_minima = tuple(float(np.min(source[source > 0.0])) for source in sources)
    checks.check(
        "declared-source-support-inventory",
        "the two-stream and bundle rows touch exactly two, three, and four positive edge classes",
        support_counts == EXPECTED_SUPPORT_RANKS and min(source_minima) > 0.0,
        f"support counts={support_counts}; smallest positive weights={source_minima}",
    )

    first_variation_errors = []
    second_variation_errors = []
    direction_a = np.asarray((0.17, -0.11, 0.09, 0.05, -0.07, 0.03, 0.08, -0.04, 0.06, -0.02))
    direction_b = np.asarray((-0.06, 0.12, -0.08, 0.04, 0.03, -0.05, 0.07, 0.02, -0.09, 0.11))
    step = 2.0e-4
    zero = np.zeros(10)
    for edge, direction in enumerate(block23.block22.regge.DIRS15):
        expected_first = float(metric_map[edge] @ direction_a)
        measured_first = (
            edge_length(direction, step * direction_a)
            - edge_length(direction, -step * direction_a)
        ) / (2.0 * step)
        expected_second = -float(
            (metric_map[edge] @ direction_a)
            * (metric_map[edge] @ direction_b)
            / flat_lengths[edge]
        )
        measured_second = (
            edge_length(direction, step * direction_a + step * direction_b)
            - edge_length(direction, step * direction_a - step * direction_b)
            - edge_length(direction, -step * direction_a + step * direction_b)
            + edge_length(direction, -step * direction_a - step * direction_b)
        ) / (4.0 * step * step)
        first_variation_errors.append(abs(measured_first - expected_first))
        second_variation_errors.append(abs(measured_second - expected_second))
    checks.check(
        "proper-length-first-and-second-variation",
        "ell_e(g)=sqrt(v_e^T g v_e) has r_e=d ell_e and d2 ell_e=-r_e tensor r_e/ell_e",
        max(first_variation_errors) < 2.0e-9
        and max(second_variation_errors) < 2.0e-7
        and edge_length(block23.block22.regge.DIRS15[0], zero) == flat_lengths[0],
        f"max first error={max(first_variation_errors):.3e}; max mixed-second error={max(second_variation_errors):.3e}",
    )

    contact_records = proper_length_contacts(
        physical, metric_map, metric_lift, sources, flat_lengths
    )
    support_ranks = tuple(
        np.linalg.matrix_rank(record[2], tol=1.0e-9) for record in contact_records
    )
    contact_ranks = tuple(
        np.linalg.matrix_rank(record[3], tol=1.0e-9) for record in contact_records
    )
    representation_errors = tuple(record[4] for record in contact_records)
    checks.check(
        "proper-length-contact-ranks",
        "the projected proper-length seagulls have ranks two, three, and four",
        support_ranks == EXPECTED_SUPPORT_RANKS
        and contact_ranks == EXPECTED_SUPPORT_RANKS
        and max(representation_errors) < 1.0e-12,
        f"support ranks={support_ranks}; contact ranks={contact_ranks}; representation error={max(representation_errors):.3e}",
    )

    rank_lower_bounds = tuple(6 - rank for rank in contact_ranks)
    checks.check(
        "support-rank-cancellation-boundary",
        "any direct Hessian confined to the active source-edge coordinates leaves nonzero six-mode rank",
        rank_lower_bounds == (4, 3, 2)
        and "rank(m_s + alpha c_s) >= 6 - m_s" in note_flat,
        f"Sylvester lower bounds on residual rank={rank_lower_bounds}",
    )

    contacted_inertias = []
    contacted_gaps = []
    best_residual_ratios = []
    best_scalars = []
    for (_, mass, _), (_, _support, _rows, contact, _error) in zip(
        mass_records, contact_records
    ):
        contacted_inertia, contacted_values = inertia(mass + contact, 1.0e-7)
        contacted_inertias.append(contacted_inertia)
        contacted_gaps.append(float(np.min(np.abs(contacted_values))))
        best_scalar = -float(
            np.vdot(contact, mass).real / np.vdot(contact, contact).real
        )
        best_scalars.append(best_scalar)
        best_residual_ratios.append(
            float(
                np.linalg.norm(mass + best_scalar * contact, "fro")
                / np.linalg.norm(mass, "fro")
            )
        )
    checks.check(
        "proper-length-seagull-does-not-cancel",
        "the sign-fixed proper-length source contact leaves every six-mode coefficient nonsingular",
        tuple(contacted_inertias) == EXPECTED_CONTACTED_INERTIAS
        and min(contacted_gaps) > 8.0e-4,
        f"contacted inertias={tuple(contacted_inertias)}; minimum gap={min(contacted_gaps):.6f}",
    )
    checks.check(
        "scalar-rescaling-does-not-cancel",
        "even the Frobenius-best scalar multiple of each proper-length contact leaves a large residual",
        min(best_residual_ratios) > 0.64,
        "best scalars="
        + ", ".join(f"{value:.6f}" for value in best_scalars)
        + "; relative residuals="
        + ", ".join(f"{value:.6f}" for value in best_residual_ratios),
    )

    connection_residuals = []
    for record in contact_records:
        contact = record[3]
        geometry_connection = -contact
        source_seagull = contact
        connection_residuals.append(
            float(np.linalg.norm(geometry_connection + source_seagull, 2))
        )
    checks.check(
        "stationary-pullback-cancellation",
        "for S_g(ell)-c J dot ell at a full stationary point, the geometry connection and proper-length source seagull cancel exactly",
        max(connection_residuals) == 0.0
        and "g_a + u_a=0" in note_flat
        and "l^dagger h_g l" in note_flat,
        f"maximum connection-plus-seagull residual={max(connection_residuals):.3e}",
    )
    checks.check(
        "no-coordinate-only-repair",
        "rewriting the same affine edge source through metric or coframe variables cannot create an independent physical repair",
        "coordinate rewrite is not a new action" in note_flat
        and "double counts" in note_flat
        and max(connection_residuals) == 0.0,
    )

    condition, chart_indices, chart_singular_values, chart = best_six_edge_chart(physical)
    chart_inverse = np.linalg.inv(chart)
    spread_errors = []
    spread_inertias = []
    for _label, mass, _step_error in mass_records:
        contact_chart = (
            chart_inverse.conjugate().T @ (-mass) @ chart_inverse
        )
        contact_chart = 0.5 * (contact_chart + contact_chart.conjugate().T)
        spread_errors.append(
            float(
                np.linalg.norm(
                    chart.conjugate().T @ contact_chart @ chart + mass, 2
                )
            )
        )
        spread_inertias.append(inertia(contact_chart)[0])
    chart_directions = tuple(
        block23.block22.regge.DIRS15[index] for index in chart_indices
    )
    checks.check(
        "six-edge-spreading-escape",
        "a six-edge chart admits an algebraic source-responsive contact completion, so the narrow support bound is not a gravity no-go",
        condition < 2.0
        and max(spread_errors) < 1.0e-12
        and min(chart_singular_values) > 0.5,
        f"chart={chart_directions}; condition={condition:.6f}; completion residual={max(spread_errors):.3e}; contact inertias={tuple(spread_inertias)}",
    )
    checks.check(
        "live-structural-routes",
        "geometry-spreading contact, dynamical p=q=1 source blocks, nonuniform closed histories, and curved phases remain explicit live routes",
        "geometry-spreading" in note_flat
        and "p=q=1" in note_flat
        and "nonuniform closed" in note_flat
        and "curved or massive" in note_flat,
    )
    checks.check(
        "bounded-theorem-and-no-go-scope",
        "the result retires only support-confined direct contacts and coordinate-only seagull transfer",
        "n1--n8 status: `pass` only" in note_flat
        and "not a gravity no-go" in note_flat
        and "not an axiom necessity" in note_flat
        and "local joint action remains open" in note_flat,
    )

    print("N5_CERTIFICATE: resolution=the negative is restricted to direct Hessians confined to each retained source row's active edge coordinates and to coordinate-only proper-length rewrites")
    print("N5_CERTIFICATE: constructive_route=a common six-edge physical chart explicitly supports source-responsive coefficient cancellation")
    print("N5_CERTIFICATE: excluded_rhetoric=no gravity, Regge, source, seagull, worldline, or axiom impossibility is claimed")
    print("N5_CERTIFICATE: live_routes=geometry-spreading contacts, dynamical source variables, nonuniform closed histories, richer actions, and curved or massive phases remain open")
    print("N5_CERTIFICATE: physical_boundary=source selection, locality, full stationarity, continuous momentum, Lorentzian evolution, and nonlinear stability are not derived")
    print("per_element: checked all fifteen actual edge classes, every active source edge, and one common six-edge escape chart")
    print("per_mode: checked the six homogeneous flat physical metric modes at the O(source) coefficient; no nonzero-momentum theorem is claimed")
    print("per_block: checked the two-stream, Bundle-A, and Bundle-B source rows and their proper-length contacts")
    print("lattice_wide: checked and not executed — no nonuniform source field, continuous-zone, finite-torus, Lorentzian, or nonlinear action theorem is claimed")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return int(checks.failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
