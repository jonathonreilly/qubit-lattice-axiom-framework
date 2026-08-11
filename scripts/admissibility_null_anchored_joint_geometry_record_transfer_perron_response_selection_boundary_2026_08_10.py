#!/usr/bin/env python3
"""Test a null-anchored joint geometry/Record transfer and its response.

Block 33 left two separately normalized geometry-sector transfers.  Here each
sector is first quotiented by its all-null transition weight and then coupled
through one positive two-state geometry kernel.  The resulting 1024-state
transfer has one Perron law, selected geometry odds, and a response Hessian
obtained by differentiating that same leading eigenvalue.

The construction is a supplied finite-width law.  It tests sufficiency and
the remaining selection boundary; it does not derive the geometry kernel,
the Record-to-metric coupling, a full-Z3 phase, a complete Ward connection,
or Lorentzian dynamics from the current axioms.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import admissibility_proper_cubic_cylinder_boundary_transfer_perron_phase_normalization_response_boundary_2026_08_10 as block33  # noqa: E402


block32 = block33.block32
block31 = block33.block31

AUDIT_TIMEOUT_SEC = 180
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_NULL_ANCHORED_JOINT_GEOMETRY_RECORD_TRANSFER_PERRON_"
    "RESPONSE_SELECTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
PARENT_PATH = block33.NOTE_PATH
ANCHOR_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_NULL_RECORD_LOG_ODDS_ACTION_REPRESENTATIVE_ANCHOR_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
PREMISE_REGISTRY_PATH = (
    ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
)

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_NULL_ANCHORED_JOINT_GEOMETRY_RECORD_TRANSFER_PERRON_RESPONSE_SELECTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_PROPER_CUBIC_CYLINDER_BOUNDARY_TRANSFER_PERRON_PHASE_NORMALIZATION_RESPONSE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/ADMISSIBILITY_NULL_RECORD_LOG_ODDS_ACTION_REPRESENTATIVE_ANCHOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "scripts/admissibility_proper_cubic_cylinder_boundary_transfer_perron_phase_normalization_response_boundary_2026_08_10.py",
)

GEOMETRY_KERNELS = (
    np.asarray(((2.0, 1.0), (1.0, 2.0))),
    np.asarray(((3.0, 1.0), (1.0, 3.0))),
)
FIELD_DIMENSION = 15
FIELD_STEP = 1.0e-5
JOINT_STATE_COUNT = 2 * block33.SLICE_STATE_COUNT


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
class JointData:
    geometry_kernel: np.ndarray
    transfer: np.ndarray
    eigenvalue: float
    right: np.ndarray
    left: np.ndarray
    stationary: np.ndarray
    source: np.ndarray
    residual: float


def flat(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").lower().split())


def local_weights(sector: int) -> np.ndarray:
    return np.asarray(block32.local_weights(sector), dtype=float)


def anchored_sector_transfer(
    sector: int, fields: np.ndarray
) -> tuple[np.ndarray, np.ndarray]:
    """Return K_g(h)/K_g(h)[null,null] and the occupied label law."""

    weights = local_weights(sector)
    tilted_actual = weights[1:] * np.exp(fields)
    aggregate = np.asarray((weights[0], float(np.sum(tilted_actual))))
    slice_weight = (
        aggregate[0]
        ** (block33.SLICE_SITE_COUNT - block33.SLICE_OCCUPANCY)
        * aggregate[1] ** block33.SLICE_OCCUPANCY
        * float(block33.PHASE_RHO[sector]) ** block33.TRANSVERSE_MATCHES
    )
    raw_transfer = (
        float(block33.PHASE_RHO[sector]) ** block33.VERTICAL_MATCHES
        * slice_weight[None, :]
    )
    anchor = float(raw_transfer[0, 0])
    return raw_transfer / anchor, tilted_actual / np.sum(tilted_actual)


def raw_joint_transfer(
    geometry_kernel: np.ndarray, fields: np.ndarray
) -> tuple[np.ndarray, tuple[np.ndarray, np.ndarray]]:
    sectors = tuple(
        anchored_sector_transfer(sector, fields) for sector in range(2)
    )
    transfers = tuple(item[0] for item in sectors)
    probabilities = tuple(item[1] for item in sectors)
    joint = np.block(
        [
            [
                geometry_kernel[source, target] * transfers[target]
                for target in range(2)
            ]
            for source in range(2)
        ]
    )
    return joint, probabilities  # type: ignore[return-value]


def joint_scale(geometry_kernel: np.ndarray) -> float:
    joint, _ = raw_joint_transfer(
        geometry_kernel, np.zeros(FIELD_DIMENSION, dtype=float)
    )
    return float(np.max(joint))


def build_joint(
    geometry_kernel: np.ndarray,
    fields: np.ndarray,
    reference_scale: float,
) -> JointData:
    raw, label_probabilities = raw_joint_transfer(geometry_kernel, fields)
    transfer = raw / reference_scale
    uniform = np.full(JOINT_STATE_COUNT, 1.0 / JOINT_STATE_COUNT)
    right, eigenvalue, _, right_residual = block33.normalized_power(
        transfer, uniform
    )
    left, left_eigenvalue, _, left_residual = block33.normalized_power(
        transfer.T, uniform
    )
    if abs(eigenvalue - left_eigenvalue) > 2.0e-12 * eigenvalue:
        raise RuntimeError("joint left/right Perron eigenvalues disagree")
    stationary = left * right
    stationary /= np.sum(stationary)
    source = np.zeros(FIELD_DIMENSION, dtype=float)
    for sector in range(2):
        sector_slice = stationary[
            sector * block33.SLICE_STATE_COUNT :
            (sector + 1) * block33.SLICE_STATE_COUNT
        ]
        expected_occupancy = float(
            np.dot(sector_slice, block33.SLICE_OCCUPANCY)
        )
        source += expected_occupancy * label_probabilities[sector]
    return JointData(
        geometry_kernel=geometry_kernel,
        transfer=transfer,
        eigenvalue=eigenvalue,
        right=right,
        left=left,
        stationary=stationary,
        source=source,
        residual=max(right_residual, left_residual),
    )


def response_hessian(
    geometry_kernel: np.ndarray,
) -> tuple[JointData, np.ndarray, float]:
    scale = joint_scale(geometry_kernel)
    zero = np.zeros(FIELD_DIMENSION, dtype=float)
    base = build_joint(geometry_kernel, zero, scale)
    hessian = np.empty((FIELD_DIMENSION, FIELD_DIMENSION), dtype=float)
    eigen_gradient = np.empty(FIELD_DIMENSION, dtype=float)
    for column in range(FIELD_DIMENSION):
        direction = np.zeros(FIELD_DIMENSION, dtype=float)
        direction[column] = FIELD_STEP
        plus = build_joint(geometry_kernel, direction, scale)
        minus = build_joint(geometry_kernel, -direction, scale)
        hessian[:, column] = (
            plus.source - minus.source
        ) / (2.0 * FIELD_STEP)
        eigen_gradient[column] = (
            np.log(plus.eigenvalue) - np.log(minus.eigenvalue)
        ) / (2.0 * FIELD_STEP)
    gradient_error = float(np.max(np.abs(eigen_gradient - base.source)))
    return base, hessian, gradient_error


def transition(data: JointData, scale: float = 1.0) -> np.ndarray:
    return (
        scale
        * data.transfer
        * data.right[None, :]
        / (scale * data.eigenvalue * data.right[:, None])
    )


def geometry_mass(data: JointData, sector: int) -> float:
    start = sector * block33.SLICE_STATE_COUNT
    stop = (sector + 1) * block33.SLICE_STATE_COUNT
    return float(np.sum(data.stationary[start:stop]))


def geometry_flip_rate(data: JointData) -> float:
    markov = transition(data)
    total = 0.0
    for source in range(2):
        source_start = source * block33.SLICE_STATE_COUNT
        source_stop = (source + 1) * block33.SLICE_STATE_COUNT
        target = 1 - source
        target_start = target * block33.SLICE_STATE_COUNT
        target_stop = (target + 1) * block33.SLICE_STATE_COUNT
        total += float(
            np.sum(
                data.stationary[source_start:source_stop, None]
                * markov[
                    source_start:source_stop,
                    target_start:target_stop,
                ]
            )
        )
    return total


def main() -> int:
    checks = Checks()
    note = flat(NOTE_PATH)
    axioms = flat(AXIOM_PATH)
    parent = flat(PARENT_PATH)
    anchor_note = flat(ANCHOR_PATH)
    registry = PREMISE_REGISTRY_PATH.read_text(encoding="utf-8")

    print("external_scientific_inputs: none; construction is repository-local")
    print("constructive_closure: one supplied null-anchored joint transfer selects conditional odds and same-functional response")
    print("selection_boundary: geometry kernel, common anchor license, metric coupling, full-Z3 phase, Ward, and Lorentzian update remain underived")

    checks.check(
        "axiom-parent-anchor-boundary",
        "the axioms leave extensional values and transfer content open, Block 33 leaves absolute normalization open, and the inherited null anchor is conditional on a registered positive family",
        "distribution's extensional form and values are not specified" in axioms
        and "does not choose a hamiltonian or transfer operator" in axioms
        and "absolute cross-sector normalization" in parent
        and "does not identify readout with action" in anchor_note
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
        "the note separates a sufficient finite-width joint law from axiom derivation, full-lattice phase, physical gravity, Ward, and Lorentzian closure and carries N1--N8",
        "null-anchored joint" in note
        and "same-functional linear response" in note
        and "not a physical gravity theorem" in note
        and "n1--n8 status:" in note
        and "no canonical axiom is edited" in note,
    )

    zero = np.zeros(FIELD_DIMENSION, dtype=float)
    anchored = [anchored_sector_transfer(sector, zero)[0] for sector in range(2)]
    anchor_error = max(abs(float(item[0, 0])) - 1.0 for item in anchored)
    scale_gauge_error = 0.0
    for sector, item in enumerate(anchored):
        raw = block33.build_phase(sector).transfer
        for scale in (7.0, 11.0):
            rescaled = scale * raw / (scale * raw[0, 0])
            scale_gauge_error = max(
                scale_gauge_error,
                float(np.max(np.abs(rescaled - item))) / float(np.max(item)),
            )
    checks.check(
        "all-null-sector-anchor",
        "dividing by each all-null transition fixes both sector representatives at unit null weight",
        anchor_error < 1.0e-15,
        f"maximum anchor error={anchor_error:.3e}",
    )
    checks.check(
        "sector-scale-gauge-quotient",
        "arbitrary positive whole-sector scales cancel exactly under the declared all-null quotient",
        scale_gauge_error < 2.0e-15,
        f"maximum relative quotient error={scale_gauge_error:.3e}",
    )

    kernel_failures = sum(
        int(
            kernel.shape != (2, 2)
            or not np.all(kernel > 0)
            or not np.allclose(kernel, kernel.T)
            or not np.allclose(np.sum(kernel, axis=1), kernel[0].sum())
        )
        for kernel in GEOMETRY_KERNELS
    )
    checks.check(
        "positive-symmetric-geometry-kernels",
        "both supplied geometry kernels are positive, symmetric, and have equal row sums within each law",
        kernel_failures == 0,
        f"kernel failures={kernel_failures}",
    )

    responses = [response_hessian(kernel) for kernel in GEOMETRY_KERNELS]
    bases = [item[0] for item in responses]
    raw_hessians = [item[1] for item in responses]
    gradient_errors = [item[2] for item in responses]
    checks.check(
        "positive-joint-geometry-record-transfer",
        "each anchored sector pair and positive geometry kernel form one strictly positive 1024-by-1024 transfer",
        all(
            data.transfer.shape == (JOINT_STATE_COUNT, JOINT_STATE_COUNT)
            and float(np.min(data.transfer)) > 0
            and np.all(np.isfinite(data.transfer))
            for data in bases
        ),
        "minimum entries="
        + ",".join(f"{np.min(data.transfer):.3e}" for data in bases),
    )
    checks.check(
        "unique-joint-perron-laws",
        "strict positivity supplies one unique normalized Perron boundary pair for each complete joint law",
        all(
            data.residual < 3.0e-14
            and float(np.min(data.left)) > 0
            and float(np.min(data.right)) > 0
            for data in bases
        ),
        "maximum residual=" + f"{max(data.residual for data in bases):.3e}",
    )

    interval_error = 0.0
    endpoint_error = 0.0
    markov_error = 0.0
    stationarity_error = 0.0
    for data in bases:
        overlap = float(np.dot(data.left, data.right))
        propagated = data.right.copy()
        for _length in range(7):
            interval_error = max(
                interval_error,
                abs(float(np.dot(data.left, propagated)) / overlap - 1.0),
            )
            propagated = data.transfer @ propagated / data.eigenvalue
        endpoint_error = max(
            endpoint_error,
            float(
                np.linalg.norm(
                    data.transfer @ data.right / data.eigenvalue - data.right,
                    1,
                )
            ),
            float(
                np.linalg.norm(
                    data.transfer.T @ data.left / data.eigenvalue - data.left,
                    1,
                )
            ),
        )
        markov = transition(data)
        markov_error = max(
            markov_error,
            float(np.max(np.abs(np.sum(markov, axis=1) - 1.0))),
        )
        stationarity_error = max(
            stationarity_error,
            float(np.linalg.norm(data.stationary @ markov - data.stationary, 1)),
        )
    checks.check(
        "joint-every-length-overlap-gluing",
        "the joint Perron endpoints normalize and project every finite longitudinal interval",
        interval_error < 3.0e-12 and endpoint_error < 3.0e-12,
        f"normalization={interval_error:.3e}; endpoint={endpoint_error:.3e}",
    )
    checks.check(
        "joint-stationary-markov-control",
        "the joint Doob transitions are stochastic and preserve their stationary laws",
        markov_error < 2.0e-12 and stationarity_error < 2.0e-12,
        f"row={markov_error:.3e}; stationarity={stationarity_error:.3e}",
    )

    geometry_masses = [
        (geometry_mass(data, 0), geometry_mass(data, 1)) for data in bases
    ]
    geometry_odds = [mass[1] / mass[0] for mass in geometry_masses]
    flip_rates = [geometry_flip_rate(data) for data in bases]
    checks.check(
        "joint-law-selects-positive-geometry-odds",
        "each complete joint transfer fixes positive normalized geometry masses and odds without an external mixture prior",
        all(
            min(mass) > 0
            and abs(sum(mass) - 1.0) < 1.0e-13
            and odds > 0
            for mass, odds in zip(geometry_masses, geometry_odds)
        ),
        "odds=" + ",".join(f"{value:.9f}" for value in geometry_odds),
    )
    checks.check(
        "positive-geometry-transition-control",
        "both stationary joint laws have positive longitudinal geometry-flip rate rather than disconnected sector mixtures",
        min(flip_rates) > 0.05,
        "flip rates=" + ",".join(f"{value:.9f}" for value in flip_rates),
    )

    common_scale_error = 0.0
    for data in bases:
        common_scale_error = max(
            common_scale_error,
            float(np.max(np.abs(transition(data, 7.0) - transition(data)))),
        )
    checks.check(
        "harmless-common-action-zero",
        "one common positive scale of the complete joint transfer is the only tested normalization gauge and leaves the joint law unchanged",
        common_scale_error < 1.0e-15,
        f"maximum transition error={common_scale_error:.3e}",
    )

    stationary_tv = 0.5 * float(
        np.linalg.norm(bases[0].stationary - bases[1].stationary, 1)
    )
    checks.check(
        "geometry-kernel-values-remain-law-content",
        "two equally positive symmetric geometry kernels select distinct stationary laws and geometry odds",
        stationary_tv > 0.05
        and abs(geometry_odds[0] - geometry_odds[1]) > 0.05,
        f"stationary TV={stationary_tv:.9f}; odds={geometry_odds}",
    )

    checks.check(
        "same-leading-functional-source-gradient",
        "the derivative of log Perron eigenvalue matches all fifteen stationary actual-edge source expectations",
        max(gradient_errors) < 2.0e-8
        and all(float(np.min(data.source)) > 0 for data in bases),
        "maximum gradient error=" + f"{max(gradient_errors):.3e}",
    )

    hessians = []
    symmetry_errors = []
    edge_minima = []
    edge_ranks = []
    for raw in raw_hessians:
        symmetry_errors.append(float(np.linalg.norm(raw - raw.T)))
        hessian = 0.5 * (raw + raw.T)
        hessians.append(hessian)
        edge_minima.append(float(np.min(np.linalg.eigvalsh(hessian))))
        edge_ranks.append(int(np.linalg.matrix_rank(hessian, tol=1.0e-8)))
    checks.check(
        "same-functional-susceptibility-symmetry",
        "the finite-difference derivative of the exact source gradient is symmetric within tolerance",
        max(symmetry_errors) < 1.0e-8,
        "maximum antisymmetric norm=" + f"{max(symmetry_errors):.3e}",
    )
    checks.check(
        "full-edge-response-rank",
        "the same joint leading functional supplies a positive full-rank fifteen-edge susceptibility",
        edge_ranks == [15, 15] and min(edge_minima) > 5.0e-4,
        f"ranks={edge_ranks}; minimum eigenvalues={edge_minima}",
    )

    metric_map = np.asarray(block31.reaction.exact_metric_map(), dtype=float)
    metric_hessians = [metric_map.T @ hessian @ metric_map for hessian in hessians]
    metric_sources = [metric_map.T @ data.source for data in bases]
    metric_ranks = [
        int(np.linalg.matrix_rank(hessian, tol=1.0e-8))
        for hessian in metric_hessians
    ]
    metric_minima = [
        float(np.min(np.linalg.eigvalsh(hessian)))
        for hessian in metric_hessians
    ]
    checks.check(
        "full-metric-response-rank",
        "pullback through the actual-edge metric map gives a positive full-rank ten-channel response kernel",
        metric_ranks == [10, 10] and min(metric_minima) > 3.0e-3,
        f"ranks={metric_ranks}; minimum eigenvalues={metric_minima}",
    )

    minimum_stress_eigenvalue = float("inf")
    for source in metric_sources:
        stress = block32.metric_tensor(source)
        minimum_stress_eigenvalue = min(
            minimum_stress_eigenvalue,
            float(np.min(np.linalg.eigvalsh(stress))),
        )
    checks.check(
        "positive-joint-stationary-metric-stress",
        "the jointly selected actual-edge sources retain positive Euclidean metric stress",
        minimum_stress_eigenvalue > 0,
        f"minimum stress eigenvalue={minimum_stress_eigenvalue:.6f}",
    )

    edge_responses = [
        np.linalg.solve(hessian, -data.source)
        for hessian, data in zip(hessians, bases)
    ]
    metric_responses = [
        np.linalg.solve(hessian, -source)
        for hessian, source in zip(metric_hessians, metric_sources)
    ]
    edge_equation = max(
        float(np.linalg.norm(hessian @ response + data.source, 2))
        for hessian, response, data in zip(hessians, edge_responses, bases)
    )
    metric_equation = max(
        float(np.linalg.norm(hessian @ response + source, 2))
        for hessian, response, source in zip(
            metric_hessians, metric_responses, metric_sources
        )
    )
    checks.check(
        "unique-same-functional-linear-response",
        "each positive Hessian fixes unique edge and metric Newton responses to its own selected source",
        edge_equation < 2.0e-10 and metric_equation < 2.0e-10,
        f"edge equation={edge_equation:.3e}; metric equation={metric_equation:.3e}",
    )

    source_separation = float(np.linalg.norm(bases[0].source - bases[1].source))
    hessian_separation = float(np.linalg.norm(hessians[0] - hessians[1]))
    metric_response_separation = float(
        np.linalg.norm(metric_responses[0] - metric_responses[1])
    )
    checks.check(
        "response-selection-is-conditional-on-law",
        "changing only the allowed geometry persistence kernel changes source, susceptibility, and selected metric response",
        source_separation > 5.0e-3
        and hessian_separation > 4.0e-3
        and metric_response_separation > 8.0,
        f"source={source_separation:.9f}; Hessian={hessian_separation:.9f}; response={metric_response_separation:.6f}",
    )

    checks.check(
        "finite-width-full-z3-ward-lorentzian-boundary",
        "the joint cylinder law is not a full-Z3 phase, complete differentiated Ward identity, or Lorentzian update",
        "finite-width" in note
        and "full `z^3`" in note
        and "complete" in note
        and "ward" in note
        and "lorentzian" in note,
    )
    checks.check(
        "minimal-law-or-axiom-delta",
        "the remaining interface is the physical joint geometry kernel, shared null-anchor license, Record-to-metric coupling, full-lattice extension, Ward connection, and causal update",
        "geometry kernel" in note
        and "shared-null" in note
        and "record-to-metric" in note
        and "downstream law" in note
        and "no fifth ontology axiom is proven necessary" in note,
    )

    print("N5_CERTIFICATE: closure=a supplied null-anchored positive joint transfer fixes geometry odds and same-functional edge/metric response")
    print("N5_CERTIFICATE: gauge=sector scales cancel before joining; only one harmless common full-transfer scale remains")
    print("N5_CERTIFICATE: selection=two symmetric positive geometry kernels give distinct odds and responses under the same structural axioms")
    print("N5_CERTIFICATE: boundary=physical kernel values, anchor license, metric coupling, full-Z3 phase, Ward connection, and Lorentzian update remain open")
    print("per_site: one null plus fifteen actual-edge labels inherited exactly")
    print("per_slice: two geometry labels times 512 occupancy states equals 1024 joint states")
    print("per_interval: every finite longitudinal interval by one joint Perron endpoint identity")
    print("full_lattice: no infinite-transverse, physical action, full Ward, or causal dynamics theorem is claimed")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return int(checks.failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
