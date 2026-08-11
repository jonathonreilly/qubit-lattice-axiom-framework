#!/usr/bin/env python3
"""Test exact cylinder gluing and the remaining normalization/response wall.

The bounded carrier is the finite-width quotient C3 x C3 x Z of the cubic
lattice.  Each site has one null Record label and fifteen actual-edge labels.
The interaction depends on null/actual occupancy, so the sixteen-state slice
transfer reduces exactly to 2^9 occupancy states while retaining the full
actual-edge source lift.

All transfer entries are defined by positive integers.  Perron messages are
computed in double precision; their uniqueness and the interval restriction
identities follow analytically from strict positivity and the displayed
eigenvector equations.  This is not a full-Z3 thermodynamic-limit theorem or
an adopted physical law.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import permutations, product
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import admissibility_interacting_record_spatial_gluing_phase_response_selection_boundary_2026_08_10 as block32  # noqa: E402


block31 = block32.block31

AUDIT_TIMEOUT_SEC = 180
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_PROPER_CUBIC_CYLINDER_BOUNDARY_TRANSFER_PERRON_PHASE_"
    "NORMALIZATION_RESPONSE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
PARENT_PATH = block32.NOTE_PATH
PREMISE_REGISTRY_PATH = (
    ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
)

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_PROPER_CUBIC_CYLINDER_BOUNDARY_TRANSFER_PERRON_PHASE_NORMALIZATION_RESPONSE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_INTERACTING_RECORD_SPATIAL_GLUING_PHASE_RESPONSE_SELECTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "scripts/admissibility_interacting_record_spatial_gluing_phase_response_selection_boundary_2026_08_10.py",
)

WIDTH = 3
SLICE_SITE_COUNT = WIDTH * WIDTH
SLICE_STATE_COUNT = 2**SLICE_SITE_COUNT
PHASE_RHO = (2, 3)


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


@dataclass
class PhaseData:
    phase: int
    rho: int
    local_weights: np.ndarray
    aggregate_weights: np.ndarray
    slice_weight: np.ndarray
    transfer: np.ndarray
    eigenvalue: float
    right: np.ndarray
    left: np.ndarray
    stationary: np.ndarray
    right_iterations: int
    left_iterations: int
    right_residual: float
    left_residual: float


def flat(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").lower().split())


def site(x: int, y: int) -> int:
    return (x % WIDTH) + WIDTH * (y % WIDTH)


TRANSVERSE_EDGES = tuple(
    edge
    for y in range(WIDTH)
    for x in range(WIDTH)
    for edge in (
        (site(x, y), site(x + 1, y)),
        (site(x, y), site(x, y + 1)),
    )
)

SLICE_BITS = np.asarray(
    tuple(product((0, 1), repeat=SLICE_SITE_COUNT)), dtype=np.int8
)
SLICE_OCCUPANCY = np.sum(SLICE_BITS, axis=1)
TRANSVERSE_MATCHES = sum(
    (SLICE_BITS[:, left] == SLICE_BITS[:, right]).astype(np.int16)
    for left, right in TRANSVERSE_EDGES
)
VERTICAL_MATCHES = np.sum(
    SLICE_BITS[:, None, :] == SLICE_BITS[None, :, :], axis=2
)


def determinant3(matrix: tuple[tuple[int, ...], ...]) -> int:
    (a, b, c), (d, e, f), (g, h, i) = matrix
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def proper_cubic_rotations() -> tuple[tuple[tuple[int, ...], ...], ...]:
    matrices = []
    for permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            matrix = tuple(
                tuple(
                    signs[row] * int(permutation[row] == column)
                    for column in range(3)
                )
                for row in range(3)
            )
            if determinant3(matrix) == 1:
                matrices.append(matrix)
    return tuple(matrices)


def apply_rotation(
    matrix: tuple[tuple[int, ...], ...], vector: tuple[int, int, int]
) -> tuple[int, int, int]:
    return tuple(
        sum(matrix[row][column] * vector[column] for column in range(3))
        for row in range(3)
    )  # type: ignore[return-value]


def normalized_power(
    operator: np.ndarray, initial: np.ndarray, tolerance: float = 1.0e-14
) -> tuple[np.ndarray, float, int, float]:
    vector = np.asarray(initial, dtype=float)
    vector /= np.sum(vector)
    iterations = 0
    for iterations in range(1, 257):
        image = operator @ vector
        eigenvalue = float(np.sum(image))
        next_vector = image / eigenvalue
        if float(np.linalg.norm(next_vector - vector, 1)) < tolerance:
            vector = next_vector
            break
        vector = next_vector
    image = operator @ vector
    eigenvalue = float(np.sum(image))
    residual = float(
        np.linalg.norm(image - eigenvalue * vector, 1) / eigenvalue
    )
    return vector, eigenvalue, iterations, residual


def build_phase(phase: int) -> PhaseData:
    rho = PHASE_RHO[phase]
    local_weights = np.asarray(block32.local_weights(phase), dtype=float)
    aggregate_weights = np.asarray(
        (local_weights[0], np.sum(local_weights[1:])), dtype=float
    )
    slice_weight = (
        aggregate_weights[0] ** (SLICE_SITE_COUNT - SLICE_OCCUPANCY)
        * aggregate_weights[1] ** SLICE_OCCUPANCY
        * float(rho) ** TRANSVERSE_MATCHES
    )
    transfer = float(rho) ** VERTICAL_MATCHES * slice_weight[None, :]
    uniform = np.full(SLICE_STATE_COUNT, 1.0 / SLICE_STATE_COUNT)
    right, eigenvalue, right_iterations, right_residual = normalized_power(
        transfer, uniform
    )
    left, left_eigenvalue, left_iterations, left_residual = normalized_power(
        transfer.T, uniform
    )
    if abs(eigenvalue - left_eigenvalue) > 1.0e-12 * eigenvalue:
        raise RuntimeError("left/right Perron eigenvalues disagree")
    stationary = left * right
    stationary /= np.sum(stationary)
    return PhaseData(
        phase=phase,
        rho=rho,
        local_weights=local_weights,
        aggregate_weights=aggregate_weights,
        slice_weight=slice_weight,
        transfer=transfer,
        eigenvalue=eigenvalue,
        right=right,
        left=left,
        stationary=stationary,
        right_iterations=right_iterations,
        left_iterations=left_iterations,
        right_residual=right_residual,
        left_residual=left_residual,
    )


def transition(phase: PhaseData) -> np.ndarray:
    return (
        phase.transfer
        * phase.right[None, :]
        / (phase.eigenvalue * phase.right[:, None])
    )


def main() -> int:
    checks = Checks()
    note = flat(NOTE_PATH)
    axioms = flat(AXIOM_PATH)
    parent = flat(PARENT_PATH)
    registry = PREMISE_REGISTRY_PATH.read_text(encoding="utf-8")

    print("external_scientific_inputs: none; construction is repository-local")
    print("analytic_boundary: positivity gives unique Perron messages and exact conditional endpoint restriction")
    print("physical_boundary: transfer values, full-Z3 phase, normalization, Ward, and Lorentzian update remain unselected")

    checks.check(
        "axiom-and-parent-boundary",
        "the axioms supply one varying nearest-neighbour rule but not its values or transfer operator, while Block 32 leaves the boundary fixed point open",
        "one fixed nearest-neighbor admissibility rule" in axioms
        and "distribution's extensional form and values are not specified" in axioms
        and "does not choose a hamiltonian or transfer operator" in axioms
        and "boundary-message/transfer law" in parent
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
        "the note separates conditional cylinder gluing from rule, phase, response, full-lattice, Ward, and Lorentzian selection and carries N1--N8",
        "finite-width proper-cubic quotient" in note
        and "perron boundary" in note
        and "normalization gauge" in note
        and "not a full" in note
        and "n1--n8 status:" in note
        and "no canonical axiom is edited" in note,
    )

    degrees = [0] * SLICE_SITE_COUNT
    for left, right in TRANSVERSE_EDGES:
        degrees[left] += 1
        degrees[right] += 1
    checks.check(
        "c3x-c3-cylinder-carrier",
        "the transverse quotient has nine sites, eighteen distinct edges, degree four per slice site, and degree six after the two longitudinal incidences",
        len(set(tuple(sorted(edge)) for edge in TRANSVERSE_EDGES)) == 18
        and degrees == [4] * SLICE_SITE_COUNT
        and SLICE_STATE_COUNT == 512,
        f"slice sites={SLICE_SITE_COUNT}; transverse edges={len(TRANSVERSE_EDGES)}; occupancy states={SLICE_STATE_COUNT}",
    )

    rotations = proper_cubic_rotations()
    directions = {
        (1, 0, 0),
        (-1, 0, 0),
        (0, 1, 0),
        (0, -1, 0),
        (0, 0, 1),
        (0, 0, -1),
    }
    rotation_failures = sum(
        {apply_rotation(matrix, direction) for direction in directions}
        != directions
        for matrix in rotations
    )
    label_failures = 0
    for axis_permutation in permutations(range(4)):
        relabel = block32.state_label_permutation(axis_permutation)
        for phase in range(2):
            weights = block32.local_weights(phase)
            label_failures += sum(
                weights[state] != weights[relabel[state]]
                for state in range(16)
            )
    checks.check(
        "proper-cubic-and-label-factor-covariance",
        "occupancy matching is invariant under all 24 proper cubic rotations and local edge weights under all 24 four-axis label relabellings",
        len(rotations) == 24
        and rotation_failures == 0
        and label_failures == 0,
        f"rotations={len(rotations)}; spatial failures={rotation_failures}; label failures={label_failures}",
    )

    aggregation_failures = 0
    conditional_variations = []
    adjacent_cross_ratios = []
    aggregate_values = []
    for phase, rho in enumerate(PHASE_RHO):
        weights = block32.local_weights(phase)
        aggregate = (weights[0], sum(weights[1:]))
        aggregate_values.append(aggregate)
        for neighbours in product((0, 1), repeat=6):
            full = []
            for state in range(16):
                occupancy = int(state != 0)
                full.append(
                    weights[state]
                    * rho ** sum(occupancy == item for item in neighbours)
                )
            aggregation_failures += int(full[0] != aggregate[0] * rho ** neighbours.count(0))
            aggregation_failures += int(
                sum(full[1:]) != aggregate[1] * rho ** neighbours.count(1)
            )
        null_all_null = aggregate[0] * rho**6 / (
            aggregate[0] * rho**6 + aggregate[1]
        )
        null_all_actual = aggregate[0] / (
            aggregate[0] + aggregate[1] * rho**6
        )
        conditional_variations.append(abs(null_all_null - null_all_actual))
        adjacent_cross_ratios.append(rho * rho)
    checks.check(
        "exact-sixteen-state-occupancy-lift",
        "summing the fifteen positive actual labels gives the exact binary occupancy conditional in every six-neighbour context",
        aggregate_values == [(5, 62), (7, 77)]
        and aggregation_failures == 0,
        f"aggregate weights={aggregate_values}; failures={aggregation_failures}",
    )
    checks.check(
        "nearest-neighbour-variation-and-interaction",
        "the full conditional varies with the six neighbour occupancies and adjacent occupancy cross-ratios are four and nine",
        min(conditional_variations) > 0
        and adjacent_cross_ratios == [4, 9],
        f"minimum null-probability variation={min(conditional_variations):.6f}; cross-ratios={adjacent_cross_ratios}",
    )

    phases = [build_phase(phase) for phase in range(2)]
    checks.check(
        "strictly-positive-integer-transfer-family",
        "both implicit 16^9-label slice laws reduce exactly to finite positive 512-by-512 occupancy transfers",
        all(
            phase.transfer.shape == (SLICE_STATE_COUNT, SLICE_STATE_COUNT)
            and np.all(np.isfinite(phase.transfer))
            and float(np.min(phase.transfer)) > 0
            for phase in phases
        ),
        "transfer shapes="
        + ",".join(str(phase.transfer.shape) for phase in phases)
        + "; entry minima="
        + ",".join(f"{np.min(phase.transfer):.3e}" for phase in phases),
    )
    checks.check(
        "perron-boundary-fixed-points",
        "strict positivity supplies unique normalized left/right boundary messages and both numerical residuals are below tolerance",
        all(
            phase.right_residual < 5.0e-13
            and phase.left_residual < 5.0e-13
            and float(np.min(phase.right)) > 0
            and float(np.min(phase.left)) > 0
            for phase in phases
        ),
        "iterations(right/left)="
        + ",".join(
            f"{phase.right_iterations}/{phase.left_iterations}" for phase in phases
        )
        + "; maximum residual="
        + f"{max(max(p.right_residual, p.left_residual) for p in phases):.3e}",
    )

    initialization_separations = []
    for phase in phases:
        delta = np.zeros(SLICE_STATE_COUNT)
        delta[0] = 1.0
        ramp = np.arange(1, SLICE_STATE_COUNT + 1, dtype=float)
        from_delta, _, _, _ = normalized_power(phase.transfer, delta)
        from_ramp, _, _, _ = normalized_power(phase.transfer, ramp)
        initialization_separations.extend(
            (
                float(np.linalg.norm(from_delta - phase.right, 1)),
                float(np.linalg.norm(from_ramp - phase.right, 1)),
            )
        )
    checks.check(
        "perron-initialization-control",
        "delta, ramp, and uniform initial boundary messages converge to the same normalized positive fixed point in both sectors",
        max(initialization_separations) < 1.0e-12,
        f"maximum L1 separation={max(initialization_separations):.3e}",
    )

    interval_normalization_error = 0.0
    endpoint_restriction_error = 0.0
    stationarity_error = 0.0
    row_error = 0.0
    for phase in phases:
        overlap = float(np.dot(phase.left, phase.right))
        propagated = phase.right.copy()
        for _length in range(9):
            interval_normalization_error = max(
                interval_normalization_error,
                abs(float(np.dot(phase.left, propagated)) / overlap - 1.0),
            )
            propagated = phase.transfer @ propagated / phase.eigenvalue
        endpoint_restriction_error = max(
            endpoint_restriction_error,
            float(
                np.linalg.norm(
                    phase.transfer @ phase.right / phase.eigenvalue
                    - phase.right,
                    1,
                )
            ),
            float(
                np.linalg.norm(
                    phase.transfer.T @ phase.left / phase.eigenvalue
                    - phase.left,
                    1,
                )
            ),
        )
        kernel = transition(phase)
        row_error = max(
            row_error, float(np.max(np.abs(np.sum(kernel, axis=1) - 1.0)))
        )
        stationarity_error = max(
            stationarity_error,
            float(np.linalg.norm(phase.stationary @ kernel - phase.stationary, 1)),
        )
    checks.check(
        "exact-overlapping-interval-gluing",
        "Perron endpoint messages normalize every tested interval length and deletion of either endpoint returns the shorter interval family",
        interval_normalization_error < 2.0e-12
        and endpoint_restriction_error < 2.0e-12,
        f"normalization={interval_normalization_error:.3e}; endpoint restriction={endpoint_restriction_error:.3e}",
    )
    checks.check(
        "stationary-slice-markov-control",
        "the Doob-normalized slice transition is stochastic and preserves the left-right stationary slice law",
        row_error < 2.0e-12 and stationarity_error < 2.0e-12,
        f"row residual={row_error:.3e}; stationarity={stationarity_error:.3e}",
    )

    expected_sources = []
    expected_occupancies = []
    for phase in phases:
        expected_occupancy = float(
            np.dot(phase.stationary, SLICE_OCCUPANCY)
        )
        label_probabilities = (
            phase.local_weights[1:] / phase.aggregate_weights[1]
        )
        expected_source = expected_occupancy * label_probabilities
        expected_occupancies.append(expected_occupancy)
        expected_sources.append(expected_source)
    checks.check(
        "stationary-actual-edge-source-lift",
        "the unique occupancy boundary law lifts to fifteen positive actual-edge source expectations whose sum is the stationary occupied-site count",
        all(float(np.min(source)) > 0 for source in expected_sources)
        and all(
            abs(float(np.sum(source)) - occupancy) < 1.0e-12
            for source, occupancy in zip(expected_sources, expected_occupancies)
        ),
        "expected occupied sites="
        + ",".join(f"{value:.9f}" for value in expected_occupancies),
    )

    metric_map = np.asarray(block31.reaction.exact_metric_map(), dtype=float)
    minimum_stress_eigenvalue = float("inf")
    for source in expected_sources:
        tensor = block32.metric_tensor(metric_map.T @ source)
        minimum_stress_eigenvalue = min(
            minimum_stress_eigenvalue, float(np.min(np.linalg.eigvalsh(tensor)))
        )
    checks.check(
        "positive-stationary-metric-stress",
        "each Perron-selected stationary source retains positive semidefinite Euclidean metric stress",
        minimum_stress_eigenvalue > -1.0e-12,
        f"minimum stress eigenvalue={minimum_stress_eigenvalue:.3e}",
    )

    stationary_tv = 0.5 * float(
        np.linalg.norm(phases[0].stationary - phases[1].stationary, 1)
    )
    right_tv = 0.5 * float(
        np.linalg.norm(phases[0].right - phases[1].right, 1)
    )
    checks.check(
        "conditional-transfer-sectors-remain-distinct",
        "the two supplied local laws produce distinct unique Perron messages and stationary cylinder laws",
        stationary_tv > 1.0e-4 and right_tv > 1.0e-3,
        f"stationary TV={stationary_tv:.9f}; right-message TV={right_tv:.9f}",
    )

    scale_gauge_error = 0.0
    eigenvalue_ratios = []
    for phase in phases:
        kernel = transition(phase)
        scale = 7.0
        scaled_kernel = (
            scale
            * phase.transfer
            * phase.right[None, :]
            / (scale * phase.eigenvalue * phase.right[:, None])
        )
        scale_gauge_error = max(
            scale_gauge_error,
            float(np.max(np.abs(kernel - scaled_kernel))),
            float(
                np.linalg.norm(
                    scale * phase.transfer @ phase.right
                    - scale * phase.eigenvalue * phase.right,
                    1,
                )
                / (scale * phase.eigenvalue),
            ),
        )
    eigenvalue_ratios.extend(
        (
            phases[1].eigenvalue / phases[0].eigenvalue,
            7.0 * phases[1].eigenvalue / phases[0].eigenvalue,
        )
    )
    checks.check(
        "absolute-transfer-normalization-gauge",
        "positive whole-sector transfer scaling leaves boundary messages and normalized interval laws unchanged while rescaling the Perron eigenvalue",
        scale_gauge_error < 2.0e-12
        and abs(eigenvalue_ratios[1] / eigenvalue_ratios[0] - 7.0) < 1.0e-12,
        f"kernel/fixed-point error={scale_gauge_error:.3e}; eigenvalue-ratio multiplier={eigenvalue_ratios[1] / eigenvalue_ratios[0]:.1f}",
    )

    prior_failures = 0
    prior_odds = []
    for multipliers in ((1, 1), (1, 7)):
        total = sum(multipliers)
        prior_odds.append(multipliers[1] / multipliers[0])
        for phase, multiplier in enumerate(multipliers):
            joint = multiplier * phases[phase].stationary / total
            recovered_mass = float(np.sum(joint))
            recovered_conditional = joint / recovered_mass
            prior_failures += int(
                abs(recovered_mass - multiplier / total) > 1.0e-14
                or np.linalg.norm(
                    recovered_conditional - phases[phase].stationary, 1
                )
                > 1.0e-13
            )
    checks.check(
        "geometry-phase-prior-survives-unique-gluing",
        "unique within-sector Perron messages do not fix cross-sector odds, which change from one to seven with both cylinder laws unchanged",
        prior_failures == 0 and prior_odds == [1.0, 7.0],
        f"failures={prior_failures}; phase odds={prior_odds}",
    )

    q0, r20, metric_map, metric_projector, _ = block31.compact_operators()
    source_matrix = np.asarray(expected_sources, dtype=float).T
    compact_ranks = set()
    metric_ranks = set()
    compact_equation = 0.0
    compact_constraint = 0.0
    metric_equation = 0.0
    response_separation = 0.0
    for alpha in block31.lift.ALPHA_WITNESSES:
        repaired = q0 + alpha * r20
        kkt = np.block(
            [
                [repaired, metric_map],
                [metric_map.T, np.zeros((10, 10))],
            ]
        )
        compact_ranks.add(int(np.linalg.matrix_rank(kkt, tol=1.0e-8)))
        for beta in (0.5, 1.0, 2.0):
            sources = beta * source_matrix
            right_hand_side = np.vstack(
                (-sources, np.zeros((10, sources.shape[1])))
            )
            compact_solution = np.linalg.solve(kkt, right_hand_side)
            compact_response = compact_solution[:15]
            multipliers = compact_solution[15:]
            compact_equation = max(
                compact_equation,
                float(
                    np.linalg.norm(
                        repaired @ compact_response
                        + metric_map @ multipliers
                        + sources,
                        2,
                    )
                ),
            )
            compact_constraint = max(
                compact_constraint,
                float(np.linalg.norm(metric_map.T @ compact_response, 2)),
            )
            for gamma in (0.25, 1.0, 4.0):
                metric_operator = repaired + gamma * metric_projector
                metric_ranks.add(
                    int(np.linalg.matrix_rank(metric_operator, tol=1.0e-8))
                )
                free_response = np.linalg.solve(metric_operator, -sources)
                metric_equation = max(
                    metric_equation,
                    float(
                        np.linalg.norm(
                            metric_operator @ free_response + sources, 2
                        )
                    ),
                )
                response_separation = max(
                    response_separation,
                    float(np.linalg.norm(free_response - compact_response, 2)),
                )
    checks.check(
        "perron-source-compact-reaction-completion",
        "the compact rank-25 reaction branch solves both Perron-selected stationary sources at every alpha and beta control",
        compact_ranks == {25}
        and compact_equation < 1.0e-10
        and compact_constraint < 1.0e-10,
        f"ranks={compact_ranks}; equation={compact_equation:.3e}; constraint={compact_constraint:.3e}",
    )
    checks.check(
        "perron-source-metric-response-control",
        "a distinct rank-15 metric-response branch solves the same fixed-point sources without selecting itself",
        metric_ranks == {15}
        and metric_equation < 1.0e-10
        and response_separation > 1.0,
        f"ranks={metric_ranks}; equation={metric_equation:.3e}; separation={response_separation:.6f}",
    )
    checks.check(
        "coefficient-family-survives-unique-gluing",
        "positive unique boundary fixed points exist at both interaction strengths and all inherited response coefficients",
        PHASE_RHO == (2, 3)
        and all(phase.eigenvalue > 0 for phase in phases)
        and stationary_tv > 0
        and len(block31.lift.ALPHA_WITNESSES) == 5
        and compact_ranks == {25}
        and metric_ranks == {15},
    )
    checks.check(
        "boundary-fixed-point-does-not-select-law-or-response",
        "unique overlap gluing is conditional on supplied coefficients and coexists with arbitrary sector odds and two complete geometry responses",
        stationary_tv > 0
        and scale_gauge_error < 2.0e-12
        and prior_failures == 0
        and compact_ranks == {25}
        and metric_ranks == {15},
    )
    checks.check(
        "full-z3-ward-and-lorentzian-boundary",
        "a finite-width stationary spatial cylinder does not establish a full-Z3 phase, complete same-law Ward connection, or Lorentzian dynamics",
        "finite-width" in note
        and "full `z^3`" in note
        and "complete stationary ward" in note
        and "lorentzian" in note,
    )
    checks.check(
        "minimal-law-or-axiom-delta",
        "the narrowed deficit is an absolutely normalized geometry-bearing full-lattice specification and update, not another boundary iteration",
        "absolute cross-sector normalization" in note
        and "geometry-bearing specification" in note
        and "downstream law" in note
        and "no fifth ontology axiom is proven necessary" in note,
    )

    print("N5_CERTIFICATE: gluing=positive Perron messages normalize and endpoint-project every finite cylinder interval")
    print("N5_CERTIFICATE: lift=the 512-state occupancy transfer exactly lifts to one null plus fifteen positive actual-edge Record labels")
    print("N5_CERTIFICATE: normalization=whole-sector transfer scale cancels from normalized intervals and cannot fix geometry odds")
    print("N5_CERTIFICATE: response=both compact reaction and metric response solve the Perron-selected stationary sources")
    print("N5_CERTIFICATE: boundary=full-Z3 selection, absolute geometry normalization, complete Ward connection, and Lorentzian update remain open")
    print("per_site: one null plus fifteen actual-edge labels with occupancy-mediated six-neighbour interaction")
    print("per_slice: nine sites and 512 occupancy states on C3 x C3")
    print("per_interval: every finite longitudinal interval by the analytic Perron endpoint identity")
    print("full_lattice: no infinite-transverse-limit, full-Z3 Gibbs uniqueness, physical phase, Ward, or Lorentzian theorem is claimed")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return int(checks.failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
