#!/usr/bin/env python3
"""Test a local geometry/Record bond law and its response boundaries.

Block 34 coupled one geometry label to an entire nine-site transverse slice.
This runner replaces that plane label by a four-state local code at every
site: a geometry bit and a Record-occupancy bit.  One positive symmetric bond
factor is used on every one of the six proper-cubic nearest-neighbour
incidences.  On C3 x C3 x Z the 4^9-state transfer is applied as a tensor
product, never materialized as a dense matrix.

The supplied bond is a positive-definite Gram matrix.  Its cylinder transfer
is therefore entrywise positive, symmetric, and positive definite.  The
Perron law has local geometry domain walls, is reversible in the transfer
direction, and supplies signed-cubic Record-ray response from the same leading
functional.  Geometry fugacity, domain-wall tension, the physical
Record-to-geometry decoder, full-Z3 phase, Ward generator, and Lorentzian
dynamics remain unselected.  A nonlinear decoder test keeps the mandatory
source-times-second-derivative connection term explicit.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import permutations, product
from pathlib import Path
import sys

import numpy as np
from scipy.sparse.linalg import LinearOperator, eigsh
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import admissibility_null_anchored_joint_geometry_record_transfer_perron_response_selection_boundary_2026_08_10 as block34  # noqa: E402


AUDIT_TIMEOUT_SEC = 240
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_LOCAL_GEOMETRY_RECORD_BOND_TRANSFER_REFLECTION_RESPONSE_"
    "CONNECTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
PARENT_PATH = block34.NOTE_PATH
ENDOGENOUS_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_ENDOGENOUS_GEOMETRY_JOINT_RECORD_RN_LOCAL_COVARIANT_"
    "CONTACT_SELECTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
KINETIC_PATH = ROOT / "docs" / (
    "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
)
PREMISE_REGISTRY_PATH = (
    ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
)

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_LOCAL_GEOMETRY_RECORD_BOND_TRANSFER_REFLECTION_RESPONSE_CONNECTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_NULL_ANCHORED_JOINT_GEOMETRY_RECORD_TRANSFER_PERRON_RESPONSE_SELECTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/ADMISSIBILITY_ENDOGENOUS_GEOMETRY_JOINT_RECORD_RN_LOCAL_COVARIANT_CONTACT_SELECTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "scripts/admissibility_null_anchored_joint_geometry_record_transfer_perron_response_selection_boundary_2026_08_10.py",
)

WIDTH = 3
SLICE_SITE_COUNT = WIDTH * WIDTH
LOCAL_STATE_COUNT = 4
SLICE_STATE_COUNT = LOCAL_STATE_COUNT ** SLICE_SITE_COUNT
FIELD_DIMENSION = 10
ACTIVITY_DENOMINATOR = 12.0
FIELD_STEP = 2.0e-4
METRIC_STEP = 3.0e-4
NONLINEAR_KAPPA = -1.0 / 4.0

GEOMETRY_OF_STATE = np.asarray((0, 0, 1, 1), dtype=np.uint8)
OCCUPANCY_OF_STATE = np.asarray((0, 1, 0, 1), dtype=np.uint8)

HCOMPS = (
    (0, 0),
    (1, 1),
    (2, 2),
    (3, 3),
    (0, 1),
    (0, 2),
    (0, 3),
    (1, 2),
    (1, 3),
    (2, 3),
)

# Four spatial body-diagonal rays modulo overall sign, followed by the six
# spatial-axis-plus-tick rays.  These two orbits are closed under all 24
# signed proper-cubic spatial rotations.
CUBIC_RAYS = (
    (1, 1, 1, 0),
    (1, 1, -1, 0),
    (1, -1, 1, 0),
    (1, -1, -1, 0),
    (1, 0, 0, 1),
    (-1, 0, 0, 1),
    (0, 1, 0, 1),
    (0, -1, 0, 1),
    (0, 0, 1, 1),
    (0, 0, -1, 1),
)


def exact_metric_map() -> sp.Matrix:
    return sp.Matrix(
        [
            [
                direction[left]
                * direction[right]
                * (1 if left == right else 2)
                for left, right in HCOMPS
            ]
            for direction in CUBIC_RAYS
        ]
    )


EXACT_METRIC_MAP = exact_metric_map()

# A rational Walsh-character Gram kernel.  Each factor
# 1+c f(s)f(t), with |c|<1, is positive semidefinite and entrywise positive.
# The three characters distinguish all four local states, so their Schur
# product is positive definite.  Geometry exchange remains an exact symmetry.
GEOMETRY_SPIN = np.asarray((-1.0, -1.0, 1.0, 1.0))
OCCUPANCY_SPIN = np.asarray((-1.0, 1.0, -1.0, 1.0))
MIXED_SPIN = GEOMETRY_SPIN * OCCUPANCY_SPIN
BASE_BOND = (
    1.0 + (1.0 / 10.0) * np.outer(GEOMETRY_SPIN, GEOMETRY_SPIN)
) * (
    1.0 + (1.0 / 12.0) * np.outer(OCCUPANCY_SPIN, OCCUPANCY_SPIN)
) * (
    1.0 + (1.0 / 14.0) * np.outer(MIXED_SPIN, MIXED_SPIN)
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


@dataclass
class LawData:
    fields: np.ndarray
    eta: np.ndarray
    tension: float
    bond: np.ndarray
    label_probabilities: np.ndarray
    site_factors: np.ndarray
    log_slice_weight: np.ndarray
    sqrt_slice_weight: np.ndarray
    eigenvalue: float
    free_energy: float
    perron: np.ndarray
    stationary: np.ndarray
    source: np.ndarray
    residual: float


def flat(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").lower().split())


def slice_digits() -> np.ndarray:
    digits = np.empty((SLICE_SITE_COUNT, SLICE_STATE_COUNT), dtype=np.uint8)
    values = np.arange(SLICE_STATE_COUNT, dtype=np.int64)
    for site in range(SLICE_SITE_COUNT):
        digits[site] = values % LOCAL_STATE_COUNT
        values //= LOCAL_STATE_COUNT
    return digits


SLICE_DIGITS = slice_digits()
SLICE_GEOMETRY = GEOMETRY_OF_STATE[SLICE_DIGITS]
SLICE_OCCUPANCY = OCCUPANCY_OF_STATE[SLICE_DIGITS]


def transverse_edges() -> tuple[tuple[int, int], ...]:
    edges: list[tuple[int, int]] = []
    for left in range(WIDTH):
        for right in range(WIDTH):
            site = WIDTH * left + right
            edges.append((site, WIDTH * ((left + 1) % WIDTH) + right))
            edges.append((site, WIDTH * left + (right + 1) % WIDTH))
    return tuple(edges)


TRANSVERSE_EDGES = transverse_edges()


def actual_weights() -> np.ndarray:
    """One null plus ten orbit-constant actual-Record weights per geometry."""

    return np.asarray(
        (
            (5.0, 3.0, 3.0, 3.0, 3.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0),
            (5.0, 6.0, 6.0, 6.0, 6.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0),
        )
    )


RAW_RECORD_WEIGHTS = actual_weights()


def tension_bond(tension: float) -> np.ndarray:
    geometry = GEOMETRY_OF_STATE
    geometry_factor = np.where(
        geometry[:, None] == geometry[None, :], tension, 1.0
    )
    return BASE_BOND * geometry_factor


def local_data(
    fields: np.ndarray,
    eta: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    tilted = RAW_RECORD_WEIGHTS[:, 1:] * np.exp(fields)[None, :]
    label_probabilities = tilted / np.sum(tilted, axis=1)[:, None]
    factors = np.empty(LOCAL_STATE_COUNT, dtype=float)
    for state in range(LOCAL_STATE_COUNT):
        geometry = int(GEOMETRY_OF_STATE[state])
        if OCCUPANCY_OF_STATE[state] == 0:
            relative = 1.0
        else:
            relative = (
                float(np.sum(tilted[geometry]))
                / (ACTIVITY_DENOMINATOR * RAW_RECORD_WEIGHTS[geometry, 0])
            )
        factors[state] = eta[geometry] * relative
    return factors, label_probabilities


def apply_tensor_bond(
    vector: np.ndarray,
    bond: np.ndarray,
    replacement_site: int | None = None,
    replacement_bond: np.ndarray | None = None,
) -> np.ndarray:
    tensor = vector.reshape((LOCAL_STATE_COUNT,) * SLICE_SITE_COUNT)
    for axis in range(SLICE_SITE_COUNT):
        factor = (
            replacement_bond
            if axis == replacement_site and replacement_bond is not None
            else bond
        )
        tensor = np.tensordot(factor, tensor, axes=(1, axis))
        tensor = np.moveaxis(tensor, 0, axis)
    return tensor.reshape(-1)


def solve_law(
    fields: np.ndarray,
    eta: tuple[float, float] = (1.0, 1.0),
    tension: float = 1.0,
    initial: np.ndarray | None = None,
) -> LawData:
    eta_array = np.asarray(eta, dtype=float)
    site_factors, label_probabilities = local_data(fields, eta_array)
    bond = tension_bond(tension)
    log_slice_weight = np.sum(np.log(site_factors[SLICE_DIGITS]), axis=0)
    log_bond = np.log(bond)
    for left, right in TRANSVERSE_EDGES:
        log_slice_weight += log_bond[SLICE_DIGITS[left], SLICE_DIGITS[right]]
    shift = float(np.max(log_slice_weight))
    sqrt_slice_weight = np.exp(0.5 * (log_slice_weight - shift))

    def multiply(vector: np.ndarray) -> np.ndarray:
        return sqrt_slice_weight * apply_tensor_bond(
            sqrt_slice_weight * vector, bond
        )

    operator = LinearOperator(
        (SLICE_STATE_COUNT, SLICE_STATE_COUNT),
        matvec=multiply,
        rmatvec=multiply,
        dtype=float,
    )
    eigenvalues, eigenvectors = eigsh(
        operator,
        k=1,
        which="LA",
        tol=5.0e-12,
        maxiter=250,
        v0=initial,
    )
    perron = np.abs(eigenvectors[:, 0])
    perron /= np.linalg.norm(perron)
    eigenvalue = float(eigenvalues[0])
    residual = float(np.linalg.norm(multiply(perron) - eigenvalue * perron) / eigenvalue)
    stationary = perron * perron

    source = np.zeros(FIELD_DIMENSION, dtype=float)
    for geometry in range(2):
        occupied_mass = 0.0
        for site in range(SLICE_SITE_COUNT):
            occupied_mass += float(
                np.dot(
                    stationary,
                    (SLICE_GEOMETRY[site] == geometry)
                    & (SLICE_OCCUPANCY[site] == 1),
                )
            )
        source += occupied_mass * label_probabilities[geometry]

    return LawData(
        fields=np.asarray(fields, dtype=float),
        eta=eta_array,
        tension=tension,
        bond=bond,
        label_probabilities=label_probabilities,
        site_factors=site_factors,
        log_slice_weight=log_slice_weight,
        sqrt_slice_weight=sqrt_slice_weight,
        eigenvalue=eigenvalue,
        free_energy=float(np.log(eigenvalue) + shift),
        perron=perron,
        stationary=stationary,
        source=source,
        residual=residual,
    )


def transfer_multiply(data: LawData, vector: np.ndarray) -> np.ndarray:
    return data.sqrt_slice_weight * apply_tensor_bond(
        data.sqrt_slice_weight * vector, data.bond
    )


def transfer_entry(data: LawData, source: int, target: int) -> float:
    local_product = 1.0
    for site in range(SLICE_SITE_COUNT):
        local_product *= data.bond[
            SLICE_DIGITS[site, source], SLICE_DIGITS[site, target]
        ]
    return float(
        data.sqrt_slice_weight[source]
        * local_product
        * data.sqrt_slice_weight[target]
    )


def pair_expectation(
    data: LawData,
    local_mask: np.ndarray,
    site: int = 0,
) -> float:
    endpoint = data.sqrt_slice_weight * data.perron
    marked_bond = data.bond * local_mask
    propagated = apply_tensor_bond(
        endpoint,
        data.bond,
        replacement_site=site,
        replacement_bond=marked_bond,
    )
    return float(np.dot(endpoint, propagated) / data.eigenvalue)


def response_hessian(base: LawData) -> tuple[np.ndarray, float]:
    hessian = np.empty((FIELD_DIMENSION, FIELD_DIMENSION), dtype=float)
    eigen_gradient = np.empty(FIELD_DIMENSION, dtype=float)
    for column in range(FIELD_DIMENSION):
        direction = np.zeros(FIELD_DIMENSION, dtype=float)
        direction[column] = FIELD_STEP
        plus = solve_law(direction, initial=base.perron)
        minus = solve_law(-direction, initial=base.perron)
        hessian[:, column] = (plus.source - minus.source) / (2.0 * FIELD_STEP)
        eigen_gradient[column] = (
            plus.free_energy - minus.free_energy
        ) / (2.0 * FIELD_STEP)
    return hessian, float(np.max(np.abs(eigen_gradient - base.source)))


def spatial_rotation_matrices() -> tuple[np.ndarray, ...]:
    rotations: list[np.ndarray] = []
    for permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            matrix = np.zeros((3, 3), dtype=int)
            for old_axis, new_axis in enumerate(permutation):
                matrix[new_axis, old_axis] = signs[old_axis]
            if round(float(np.linalg.det(matrix))) == 1:
                rotations.append(matrix)
    rotations.sort(key=lambda item: tuple(item.reshape(-1)))
    return tuple(rotations)


SPATIAL_ROTATIONS = spatial_rotation_matrices()


def proper_rotations() -> tuple[tuple[int, ...], ...]:
    directions = (
        (1, 0, 0),
        (-1, 0, 0),
        (0, 1, 0),
        (0, -1, 0),
        (0, 0, 1),
        (0, 0, -1),
    )
    index = {direction: position for position, direction in enumerate(directions)}
    return tuple(
        tuple(index[tuple(matrix @ np.asarray(direction))] for direction in directions)
        for matrix in SPATIAL_ROTATIONS
    )


def canonical_ray(direction: tuple[int, ...] | np.ndarray) -> tuple[int, ...]:
    values = np.asarray(direction, dtype=int)
    first = next(int(value) for value in values if value != 0)
    if first < 0:
        values = -values
    return tuple(int(value) for value in values)


def four_rotation(spatial: np.ndarray) -> np.ndarray:
    result = np.eye(4, dtype=int)
    result[:3, :3] = spatial
    return result


def ray_permutation(spatial: np.ndarray) -> np.ndarray:
    index = {canonical_ray(direction): position for position, direction in enumerate(CUBIC_RAYS)}
    matrix = np.zeros((FIELD_DIMENSION, FIELD_DIMENSION), dtype=float)
    rotation = four_rotation(spatial)
    for column, direction in enumerate(CUBIC_RAYS):
        transformed = canonical_ray(rotation @ np.asarray(direction))
        matrix[index[transformed], column] = 1.0
    return matrix


def metric_rotation(spatial: np.ndarray) -> np.ndarray:
    rotation = four_rotation(spatial)
    action = np.zeros((len(HCOMPS), len(HCOMPS)), dtype=float)
    for column, (left, right) in enumerate(HCOMPS):
        basis = np.zeros((4, 4), dtype=float)
        basis[left, right] = 1.0
        basis[right, left] = 1.0
        transformed = rotation @ basis @ rotation.T
        for row, (target_left, target_right) in enumerate(HCOMPS):
            action[row, column] = transformed[target_left, target_right]
    return action


def inherited_signed_ray_closure() -> set[tuple[int, ...]]:
    inherited = tuple(tuple(item) for item in block34.block31.regge.DIRS15)
    return {
        canonical_ray(four_rotation(rotation) @ np.asarray(direction))
        for rotation in SPATIAL_ROTATIONS
        for direction in inherited
    }


def neighborhoods() -> np.ndarray:
    count = LOCAL_STATE_COUNT ** 6
    values = np.arange(count, dtype=np.int64)
    result = np.empty((6, count), dtype=np.uint8)
    for incidence in range(6):
        result[incidence] = values % LOCAL_STATE_COUNT
        values //= LOCAL_STATE_COUNT
    return result


def local_conditionals(
    neighbor_states: np.ndarray,
    site_factors: np.ndarray,
    bond: np.ndarray,
) -> np.ndarray:
    unnormalized = local_unnormalized_weights(neighbor_states, site_factors, bond)
    return unnormalized / np.sum(unnormalized, axis=0, keepdims=True)


def local_unnormalized_weights(
    neighbor_states: np.ndarray,
    site_factors: np.ndarray,
    bond: np.ndarray,
) -> np.ndarray:
    unnormalized = np.repeat(site_factors[:, None], neighbor_states.shape[1], axis=1)
    for incidence in range(6):
        unnormalized *= bond[:, neighbor_states[incidence]]
    return unnormalized


def grouped_record_conditionals(data: LawData) -> np.ndarray:
    geometry_codes = np.sum(
        SLICE_GEOMETRY.astype(np.int64)
        * (2 ** np.arange(SLICE_SITE_COUNT, dtype=np.int64))[:, None],
        axis=0,
    )
    scaled = np.exp(data.log_slice_weight - np.max(data.log_slice_weight))
    totals = np.bincount(geometry_codes, weights=scaled, minlength=2 ** SLICE_SITE_COUNT)
    return scaled / totals[geometry_codes]


def nonlinear_metric_hessian(
    base: LawData,
    edge_hessian: np.ndarray,
    metric_map: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, float]:
    analytic = (
        metric_map.T @ edge_hessian @ metric_map
        + NONLINEAR_KAPPA * float(np.sum(base.source)) * np.eye(metric_map.shape[1])
    )
    numerical = np.empty_like(analytic)
    for column in range(metric_map.shape[1]):
        direction = np.zeros(metric_map.shape[1], dtype=float)
        direction[column] = METRIC_STEP
        gradients = []
        for sign in (1.0, -1.0):
            q = sign * direction
            fields = metric_map @ q + 0.5 * NONLINEAR_KAPPA * np.dot(q, q)
            law = solve_law(fields, initial=base.perron)
            jacobian = metric_map + NONLINEAR_KAPPA * np.ones(
                (FIELD_DIMENSION, 1)
            ) * q[None, :]
            gradients.append(jacobian.T @ law.source)
        numerical[:, column] = (gradients[0] - gradients[1]) / (2.0 * METRIC_STEP)
    error = float(np.linalg.norm(numerical - analytic, 2))
    return analytic, numerical, error


def main() -> int:
    checks = Checks()
    note = flat(NOTE_PATH)
    axioms = flat(AXIOM_PATH)
    parent = flat(PARENT_PATH)
    endogenous = flat(ENDOGENOUS_PATH)
    kinetic = flat(KINETIC_PATH)
    registry = PREMISE_REGISTRY_PATH.read_text(encoding="utf-8")

    print("external_scientific_inputs: none; all state factors, bonds, parent weights, and response maps are repository-local")
    print("constructive_gain: a matrix-free local geometry/Record bond law removes the slice-plane label and supplies a symmetric positive transfer")
    print("boundary: the local geometry code, fugacity, wall tension, full-Z3 phase, Ward generator, and Lorentzian Record dynamics remain underived")

    checks.check(
        "axiom-parent-interface",
        "the axioms supply a covariant nearest-neighbour distribution but not its values or dynamics, while the parents require a physical local geometry map",
        "distribution's extensional form and values are not specified" in axioms
        and "admissibility is not a dynamics axiom" in axioms
        and "one slice-level geometry label" in parent
        and "record configurations -> local coframe/metric/history data" in endogenous
        and "does not supply" in kinetic
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
        "note-and-no-go-contract",
        "the source note states the finite-width Euclidean scope, lands the current N1--N8 gate, and does not claim a physical geometry decoder, full-Z3 phase, Ward identity, or Lorentzian dynamics",
        "local geometry/record bond" in note
        and "no-go discipline gate" in note
        and "not a physical geometry theorem" in note
        and "full-`z^3`" in note
        and "lorentzian" in note,
    )

    neighborhoods_all = neighborhoods()
    rotations = proper_rotations()
    base_factors, _ = local_data(np.zeros(FIELD_DIMENSION), np.ones(2))
    base_conditionals = local_conditionals(neighborhoods_all, base_factors, BASE_BOND)
    covariance_error = 0.0
    for action in rotations:
        rotated = local_conditionals(
            neighborhoods_all[np.asarray(action)], base_factors, BASE_BOND
        )
        covariance_error = max(
            covariance_error, float(np.max(np.abs(rotated - base_conditionals)))
        )
    sensitivity = []
    reference_neighbors = np.zeros((6, 1), dtype=np.uint8)
    reference_conditional = local_conditionals(
        reference_neighbors, base_factors, BASE_BOND
    )
    for incidence in range(6):
        changed = reference_neighbors.copy()
        changed[incidence, 0] = 3
        sensitivity.append(
            float(
                np.max(
                    np.abs(
                        local_conditionals(changed, base_factors, BASE_BOND)
                        - reference_conditional
                    )
                )
            )
        )
    checks.check(
        "six-incidence-proper-cubic-local-rule",
        "one normalized positive coarse geometry/occupancy conditional is invariant under all 24 proper-cubic rotations and varies with each of the six neighbour incidences",
        len(rotations) == 24
        and covariance_error < 1.0e-15
        and min(sensitivity) > 1.0e-3
        and float(np.min(base_conditionals)) > 0.0
        and float(np.max(np.abs(np.sum(base_conditionals, axis=0) - 1.0))) < 1.0e-14,
        f"environments={neighborhoods_all.shape[1]}; rotations={len(rotations)}; covariance={covariance_error:.3e}; minimum sensitivity={min(sensitivity):.6f}",
    )

    metric_map = np.asarray(EXACT_METRIC_MAP, dtype=float)
    ray_covariance_error = 0.0
    weight_covariance_error = 0.0
    for rotation in SPATIAL_ROTATIONS:
        edge_action = ray_permutation(rotation)
        metric_action = metric_rotation(rotation)
        ray_covariance_error = max(
            ray_covariance_error,
            float(np.linalg.norm(metric_map @ metric_action - edge_action @ metric_map)),
        )
        for geometry in range(2):
            weight_covariance_error = max(
                weight_covariance_error,
                float(
                    np.max(
                        np.abs(
                            edge_action @ RAW_RECORD_WEIGHTS[geometry, 1:]
                            - RAW_RECORD_WEIGHTS[geometry, 1:]
                        )
                    )
                ),
            )
    inherited_closure = inherited_signed_ray_closure()
    exact_determinant = abs(int(EXACT_METRIC_MAP.det()))
    exact_gram_determinant = int((EXACT_METRIC_MAP.T * EXACT_METRIC_MAP).det())
    checks.check(
        "minimal-signed-cubic-record-ray-repair",
        "the inherited fifteen positive-support rays expand to forty under signed cubic rotations, while the ten replacement rays are closed and attain the rank-ten metric lower bound",
        len(inherited_closure) == 40
        and len(CUBIC_RAYS) == len(HCOMPS) == 10
        and EXACT_METRIC_MAP.rank() == 10
        and exact_determinant == 24576
        and exact_gram_determinant == 603979776
        and ray_covariance_error == 0.0
        and weight_covariance_error == 0.0,
        f"inherited closure={len(inherited_closure)}; determinant={exact_determinant}; Gram determinant={exact_gram_determinant}; covariance={ray_covariance_error:.1e}",
    )

    unnormalized = local_unnormalized_weights(
        neighborhoods_all, base_factors, BASE_BOND
    )
    heat_balance_error = 0.0
    for left in range(LOCAL_STATE_COUNT):
        for right in range(LOCAL_STATE_COUNT):
            heat_balance_error = max(
                heat_balance_error,
                float(
                    np.max(
                        np.abs(
                            unnormalized[left] * base_conditionals[right]
                            - unnormalized[right] * base_conditionals[left]
                        )
                    )
                ),
            )
    checks.check(
        "local-heat-bath-euclidean-control",
        "the displayed local conditional defines a reversible single-site heat-bath sampler, while the note keeps its scheduler and Record-erasing moves outside physical dynamics",
        heat_balance_error < 1.0e-15
        and "record-erasing" in note
        and "euclidean sampler" in note,
        f"maximum local balance residual={heat_balance_error:.3e}",
    )

    base = solve_law(np.zeros(FIELD_DIMENSION))
    local_eigenvalues = np.linalg.eigvalsh(base.bond)
    checks.check(
        "matrix-free-positive-definite-transfer",
        "the 262144-state transfer is applied by nine four-state contractions; the positive Gram bond makes the unmaterialized symmetric transfer positive definite",
        SLICE_STATE_COUNT == 262144
        and float(np.min(base.bond)) > 0.0
        and float(np.min(local_eigenvalues)) > 0.3
        and base.residual < 2.0e-12
        and float(np.min(base.perron)) > 0.0,
        f"local bond minimum eigenvalue={np.min(local_eigenvalues):.9f}; Perron residual={base.residual:.3e}; minimum message={np.min(base.perron):.3e}",
    )

    interval_error = 0.0
    propagated = base.perron.copy()
    for _length in range(7):
        interval_error = max(interval_error, abs(float(np.dot(base.perron, propagated)) - 1.0))
        propagated = transfer_multiply(base, propagated) / base.eigenvalue
    checks.check(
        "every-length-local-cylinder-projectivity",
        "the one local tensor transfer and its Perron endpoint normalize and project every finite longitudinal interval",
        interval_error < 3.0e-12,
        f"executed interval error={interval_error:.3e}; analytic identity holds for every length",
    )

    geometry_masses = [
        float(np.dot(base.stationary, SLICE_GEOMETRY[site]))
        for site in range(SLICE_SITE_COUNT)
    ]
    occupancy_masses = [
        float(np.dot(base.stationary, SLICE_OCCUPANCY[site]))
        for site in range(SLICE_SITE_COUNT)
    ]
    all_zero = np.all(SLICE_GEOMETRY == 0, axis=0)
    all_one = np.all(SLICE_GEOMETRY == 1, axis=0)
    mixed_geometry_mass = 1.0 - float(np.sum(base.stationary[all_zero])) - float(
        np.sum(base.stationary[all_one])
    )
    transverse_disagreements = [
        float(
            np.dot(
                base.stationary,
                SLICE_GEOMETRY[left] != SLICE_GEOMETRY[right],
            )
        )
        for left, right in TRANSVERSE_EDGES
    ]
    flip_mask = (
        GEOMETRY_OF_STATE[:, None] != GEOMETRY_OF_STATE[None, :]
    ).astype(float)
    vertical_flip = pair_expectation(base, flip_mask)
    checks.check(
        "local-geometry-domain-wall-law",
        "geometry is sitewise rather than one plane label: mixed slices, transverse domain walls, and longitudinal local flips all have positive stationary mass",
        mixed_geometry_mass > 0.4
        and min(transverse_disagreements) > 0.1
        and vertical_flip > 0.1
        and max(geometry_masses) - min(geometry_masses) < 1.0e-12
        and max(occupancy_masses) - min(occupancy_masses) < 1.0e-12,
        f"mixed={mixed_geometry_mass:.9f}; transverse disagreement={np.mean(transverse_disagreements):.9f}; vertical flip={vertical_flip:.9f}",
    )

    all_state = lambda state: state * (LOCAL_STATE_COUNT ** SLICE_SITE_COUNT - 1) // (LOCAL_STATE_COUNT - 1)
    new_cycle = (all_state(0), all_state(2), all_state(1))
    forward = np.prod(
        [
            transfer_entry(base, new_cycle[0], new_cycle[1]),
            transfer_entry(base, new_cycle[1], new_cycle[2]),
            transfer_entry(base, new_cycle[2], new_cycle[0]),
        ]
    )
    reverse = np.prod(
        [
            transfer_entry(base, new_cycle[0], new_cycle[2]),
            transfer_entry(base, new_cycle[2], new_cycle[1]),
            transfer_entry(base, new_cycle[1], new_cycle[0]),
        ]
    )
    parent_joint, _ = block34.raw_joint_transfer(
        block34.GEOMETRY_KERNELS[0], np.zeros(block34.FIELD_DIMENSION)
    )
    parent_cycle = (0, block34.JOINT_STATE_COUNT // 2, block34.block33.SLICE_STATE_COUNT - 1)
    parent_forward = (
        parent_joint[parent_cycle[0], parent_cycle[1]]
        * parent_joint[parent_cycle[1], parent_cycle[2]]
        * parent_joint[parent_cycle[2], parent_cycle[0]]
    )
    parent_reverse = (
        parent_joint[parent_cycle[0], parent_cycle[2]]
        * parent_joint[parent_cycle[2], parent_cycle[1]]
        * parent_joint[parent_cycle[1], parent_cycle[0]]
    )
    parent_cycle_ratio = float(parent_forward / parent_reverse)
    checks.check(
        "symmetric-transfer-reversibility-repair",
        "the local Gram-bond transfer has unit forward/reverse cycle ratio and reversible Perron flux, unlike the target-sector Block-34 transfer control",
        abs(float(forward / reverse) - 1.0) < 1.0e-13
        and abs(parent_cycle_ratio - (3.0 / 2.0) ** 9) < 1.0e-11,
        f"local ratio={forward / reverse:.12f}; parent control={parent_cycle_ratio:.12f}",
    )

    edge_hessian_raw, gradient_error = response_hessian(base)
    symmetry_error = float(np.linalg.norm(edge_hessian_raw - edge_hessian_raw.T, 2))
    edge_hessian = 0.5 * (edge_hessian_raw + edge_hessian_raw.T)
    edge_eigenvalues = np.linalg.eigvalsh(edge_hessian)
    affine_metric_hessian = metric_map.T @ edge_hessian @ metric_map
    affine_metric_eigenvalues = np.linalg.eigvalsh(affine_metric_hessian)
    checks.check(
        "same-functional-local-source-and-response",
        "the log-Perron gradient reproduces all ten signed-cubic Record-ray sources, whose symmetric susceptibility and metric pullback are positive and full rank",
        gradient_error < 2.0e-7
        and symmetry_error < 2.0e-7
        and np.linalg.matrix_rank(edge_hessian, tol=1.0e-7) == 10
        and np.linalg.matrix_rank(affine_metric_hessian, tol=1.0e-7) == 10
        and float(np.min(edge_eigenvalues)) > 0.1
        and float(np.min(affine_metric_eigenvalues)) > 0.05,
        f"gradient={gradient_error:.3e}; symmetry={symmetry_error:.3e}; minima={np.min(edge_eigenvalues):.6f}/{np.min(affine_metric_eigenvalues):.6f}",
    )

    nonlinear_analytic, nonlinear_numerical, connection_error = nonlinear_metric_hessian(
        base, edge_hessian, metric_map
    )
    nonlinear_minimum = float(np.min(np.linalg.eigvalsh(nonlinear_analytic)))
    omitted_connection_error = float(
        np.linalg.norm(nonlinear_numerical - affine_metric_hessian, 2)
    )
    checks.check(
        "nonlinear-decoder-connection-chain-rule",
        "the composed metric Hessian matches M^T H M plus source times decoder curvature; omitting that connection term fails and can reverse the affine positivity conclusion",
        connection_error < 3.0e-6
        and omitted_connection_error > 0.1
        and nonlinear_minimum < -0.01,
        f"included error={connection_error:.3e}; omitted error={omitted_connection_error:.6f}; nonlinear minimum={nonlinear_minimum:.6f}",
    )

    nonlinear_covariance_error = 0.0
    probe = np.linspace(-0.07, 0.11, metric_map.shape[1])
    nonlinear_probe = metric_map @ probe + 0.5 * NONLINEAR_KAPPA * np.dot(probe, probe)
    for rotation in SPATIAL_ROTATIONS:
        edge_action = ray_permutation(rotation)
        metric_action = metric_rotation(rotation)
        rotated_probe = metric_action @ probe
        rotated_nonlinear = metric_map @ rotated_probe + 0.5 * NONLINEAR_KAPPA * np.dot(
            rotated_probe, rotated_probe
        )
        nonlinear_covariance_error = max(
            nonlinear_covariance_error,
            float(np.linalg.norm(rotated_nonlinear - edge_action @ nonlinear_probe)),
        )
    checks.check(
        "nonlinear-decoder-covariant-control",
        "the connection mutation is not symmetry breaking: its all-edge quadratic curvature commutes with all 24 signed proper-cubic spatial rotations",
        nonlinear_covariance_error < 1.0e-13,
        f"maximum covariance error={nonlinear_covariance_error:.3e}",
    )

    low_eta = solve_law(np.zeros(FIELD_DIMENSION), eta=(1.0, 0.5), initial=base.perron)
    high_eta = solve_law(np.zeros(FIELD_DIMENSION), eta=(1.0, 2.0), initial=base.perron)
    eta_geometry_masses = (
        float(np.dot(low_eta.stationary, SLICE_GEOMETRY[0])),
        float(np.dot(high_eta.stationary, SLICE_GEOMETRY[0])),
    )
    low_conditionals = grouped_record_conditionals(low_eta)
    high_conditionals = grouped_record_conditionals(high_eta)
    fixed_geometry_error = float(np.max(np.abs(low_conditionals - high_conditionals)))
    checks.check(
        "local-geometry-fugacity-selection-boundary",
        "a geometry-only fugacity leaves every tested fixed-slice-geometry Record conditional unchanged while moving the joint geometry marginal",
        fixed_geometry_error < 2.0e-14
        and abs(eta_geometry_masses[1] - eta_geometry_masses[0]) > 0.5,
        f"conditional error={fixed_geometry_error:.3e}; geometry masses={eta_geometry_masses[0]:.9f}/{eta_geometry_masses[1]:.9f}",
    )

    tension_law = solve_law(
        np.zeros(FIELD_DIMENSION), tension=6.0 / 5.0, initial=base.perron
    )
    tension_eigenvalues = np.linalg.eigvalsh(tension_law.bond)
    tension_disagreement = float(
        np.dot(
            tension_law.stationary,
            SLICE_GEOMETRY[TRANSVERSE_EDGES[0][0]]
            != SLICE_GEOMETRY[TRANSVERSE_EDGES[0][1]],
        )
    )
    uniform_geometry_ratio_error = 0.0
    for left in range(LOCAL_STATE_COUNT):
        for right in range(LOCAL_STATE_COUNT):
            if GEOMETRY_OF_STATE[left] == GEOMETRY_OF_STATE[right]:
                uniform_geometry_ratio_error = max(
                    uniform_geometry_ratio_error,
                    abs(tension_law.bond[left, right] / base.bond[left, right] - 6.0 / 5.0),
                )
    checks.check(
        "domain-wall-tension-selection-boundary",
        "a second positive-definite proper-cubic bond is a constant on uniform-geometry sectors yet changes local domain-wall statistics",
        float(np.min(tension_eigenvalues)) > 0.3
        and uniform_geometry_ratio_error < 1.0e-14
        and abs(tension_disagreement - transverse_disagreements[0]) > 0.1,
        f"uniform-sector ratio error={uniform_geometry_ratio_error:.3e}; disagreements={transverse_disagreements[0]:.9f}/{tension_disagreement:.9f}",
    )

    checks.check(
        "four-obligation-boundary",
        "the finite local Euclidean law closes neither the physical geometry carrier, full-lattice phase, exact Ward generator, nor autonomous Lorentzian Record update",
        "four independent obligations" in note
        and "geometry carrier" in note
        and "full-`z^3` phase" in note
        and "ward" in note
        and "lorentzian" in note
        and "no fifth ontology axiom" in note,
    )

    print("N5_CERTIFICATE: local geometry replaces the plane label; the transfer is symmetric positive and reversible")
    print("N5_CERTIFICATE: source response includes ten cubic Record-ray fields, ten metric fields, and nonlinear decoder curvature")
    print("N5_CERTIFICATE: fugacity and domain-wall controls preserve fixed-sector information while changing the joint local law")
    print("per_element: checked all four local geometry/occupancy states and all ten signed-cubic Record rays in the supplied bond law")
    print("per_site: checked all 4096 six-neighbour environments, all 24 proper-cubic rotations, and each incidence separately")
    print("per_mode: checked ten affine and nonlinear metric-coordinate response directions; nonzero Fourier Ward modes were not executed")
    print("per_block: checked all 262144 width-three slice states through a matrix-free nine-factor transfer and mixed-domain observables")
    print("lattice_wide: checked and not executed — finite width does not certify a selected full-Z3 phase or Lorentzian causal dynamics")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return int(checks.failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
