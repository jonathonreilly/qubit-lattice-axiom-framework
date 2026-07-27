from __future__ import annotations

import argparse
import collections
import dataclasses
import itertools
import sys
from typing import Iterable

import numpy as np


I2 = np.eye(2, dtype=complex)
X2 = np.array([[0, 1], [1, 0]], dtype=complex)
Z2 = np.array([[1, 0], [0, -1]], dtype=complex)

OUTCOME_ORDER = ((0, 0), (1, 0), (0, 1), (1, 1))
OUTCOME_LABELS = {
    (0, 0): "Phi+",
    (1, 0): "Phi-",
    (0, 1): "Psi+",
    (1, 1): "Psi-",
}


@dataclasses.dataclass(frozen=True)
class Geometry:
    dim: int
    side: int

    @property
    def n_sites(self) -> int:
        return self.side**self.dim

    @property
    def n_cells(self) -> int:
        return (self.side // 2) ** self.dim


@dataclasses.dataclass
class Encoding:
    geometry: Geometry
    cell: tuple[int, ...]
    logical_axis: int
    spectators: tuple[int, ...]
    indices: tuple[int, int]
    eta_pair: tuple[tuple[int, ...], tuple[int, ...]]
    z_logical: np.ndarray
    adapted_x_logical: np.ndarray
    fixed_x_logical: np.ndarray
    z_sign: int
    adapted_x_sign: int
    fixed_x_sign: int | None
    fixed_x_signed_pauli: bool
    fixed_x_leakage: float
    fixed_x_square_error: float
    fixed_x_anticommutator_norm: float
    fixed_x_restriction_zero: bool
    fixed_x_usable: bool

    @property
    def canonical_z_logical(self) -> np.ndarray:
        return self.z_sign * self.z_logical

    @property
    def canonical_adapted_x_logical(self) -> np.ndarray:
        return self.adapted_x_sign * self.adapted_x_logical


@dataclasses.dataclass(frozen=True)
class BellProjectorMetrics:
    resolution_error: float
    idempotence_error: float
    orthogonality_error: float


@dataclasses.dataclass(frozen=True)
class LogicalTeleportationCertificate:
    bell_projector_rank_one_count: int
    bell_projector_resolution_error: float
    bell_projector_idempotence_error: float
    bell_projector_orthogonality_error: float
    bell_projector_outer_product_error: float
    branch_map_error: float
    branch_channel_basis_error: float
    corrected_branch_map_error: float
    corrected_channel_basis_error: float
    pauli_twirl_basis_error: float


@dataclasses.dataclass(frozen=True)
class StructuralCertificate:
    total_encodings: int
    expected_encodings: int
    unique_encoding_count: int
    implied_ordered_triples: int
    expected_ordered_triples: int
    certified_ordered_triples: int
    isometry_pass_count: int
    canonical_pauli_pass_count: int
    max_isometry_error: float
    max_projector_error: float
    max_canonical_z_error: float
    max_canonical_x_error: float
    max_pauli_square_error: float
    max_pauli_anticommutator_error: float
    logical: LogicalTeleportationCertificate


@dataclasses.dataclass(frozen=True)
class TeleportationMetrics:
    n_trials: int
    projector_resolution_error: float
    projector_idempotence_error: float
    projector_orthogonality_error: float
    min_fidelity: float
    max_infidelity: float
    max_branch_probability_error: float
    max_total_probability_error: float
    max_pre_measurement_trace_distance: float
    max_post_measurement_trace_distance: float
    max_pairwise_pre_message_distance: float
    max_corrected_trace_error: float
    outcomes_seen: tuple[tuple[int, int], ...]


@dataclasses.dataclass
class MapSummary:
    label: str
    total_cases: int = 0
    expected_pass_cases: int = 0
    teleportation_run: int = 0
    teleportation_pass: int = 0
    skipped_before_teleportation: int = 0
    unexpected_results: int = 0
    failure_causes: collections.Counter[str] = dataclasses.field(
        default_factory=collections.Counter
    )
    by_geometry: dict[tuple[int, int], list[int]] = dataclasses.field(default_factory=dict)
    max_projector_resolution_error: float = 0.0
    max_projector_idempotence_error: float = 0.0
    max_projector_orthogonality_error: float = 0.0
    min_fidelity: float = 1.0
    max_infidelity: float = 0.0
    max_branch_probability_error: float = 0.0
    max_total_probability_error: float = 0.0
    max_pre_measurement_trace_distance: float = 0.0
    max_post_measurement_trace_distance: float = 0.0
    max_pairwise_pre_message_distance: float = 0.0
    max_corrected_trace_error: float = 0.0
    outcomes_seen: set[tuple[int, int]] = dataclasses.field(default_factory=set)

    def _record_case(self, geometry: Geometry, expected_pass: bool, result_pass: bool) -> None:
        self.total_cases += 1
        self.expected_pass_cases += int(expected_pass)
        key = (geometry.dim, geometry.side)
        if key not in self.by_geometry:
            self.by_geometry[key] = [0, 0, 0]
        self.by_geometry[key][0] += 1
        self.by_geometry[key][1] += int(result_pass)
        self.by_geometry[key][2] += int(expected_pass)
        if result_pass != expected_pass:
            self.unexpected_results += 1

    def update_skip(self, geometry: Geometry, expected_pass: bool, cause: str) -> None:
        self.skipped_before_teleportation += 1
        self.failure_causes[cause] += 1
        self._record_case(geometry, expected_pass=expected_pass, result_pass=False)

    def update_metrics(
        self,
        geometry: Geometry,
        metrics: TeleportationMetrics,
        expected_pass: bool,
        tolerance: float,
        failure_cause: str | None = None,
    ) -> None:
        result_pass = teleportation_metrics_pass(metrics, tolerance)
        if failure_cause is not None and not result_pass:
            self.failure_causes[failure_cause] += 1
        self._record_case(geometry, expected_pass=expected_pass, result_pass=result_pass)

        self.teleportation_run += 1
        self.teleportation_pass += int(result_pass)
        self.max_projector_resolution_error = max(
            self.max_projector_resolution_error,
            metrics.projector_resolution_error,
        )
        self.max_projector_idempotence_error = max(
            self.max_projector_idempotence_error,
            metrics.projector_idempotence_error,
        )
        self.max_projector_orthogonality_error = max(
            self.max_projector_orthogonality_error,
            metrics.projector_orthogonality_error,
        )
        self.min_fidelity = min(self.min_fidelity, metrics.min_fidelity)
        self.max_infidelity = max(self.max_infidelity, metrics.max_infidelity)
        self.max_branch_probability_error = max(
            self.max_branch_probability_error,
            metrics.max_branch_probability_error,
        )
        self.max_total_probability_error = max(
            self.max_total_probability_error,
            metrics.max_total_probability_error,
        )
        self.max_pre_measurement_trace_distance = max(
            self.max_pre_measurement_trace_distance,
            metrics.max_pre_measurement_trace_distance,
        )
        self.max_post_measurement_trace_distance = max(
            self.max_post_measurement_trace_distance,
            metrics.max_post_measurement_trace_distance,
        )
        self.max_pairwise_pre_message_distance = max(
            self.max_pairwise_pre_message_distance,
            metrics.max_pairwise_pre_message_distance,
        )
        self.max_corrected_trace_error = max(
            self.max_corrected_trace_error,
            metrics.max_corrected_trace_error,
        )
        self.outcomes_seen.update(metrics.outcomes_seen)


@dataclasses.dataclass
class RequirementSummary:
    total_possible_triples: int = 0
    surveyed_triples: int = 0
    by_geometry: dict[tuple[int, int], list[int]] = dataclasses.field(default_factory=dict)
    a_to_r_same_support: int = 0
    explicit_a_to_r_maps: int = 0
    r_to_b_same_support: int = 0
    explicit_r_to_b_maps: int = 0
    no_site_maps_needed: int = 0
    both_site_maps_needed: int = 0
    cross_register_bell_pairing_required: int = 0
    axis_adapted_bell_x_required: int = 0
    adapted_bell_measurement_required: int = 0
    fixed_last_axis_bell_x_sufficient: int = 0
    a_to_r_pair_kinds: collections.Counter[str] = dataclasses.field(
        default_factory=collections.Counter
    )
    r_to_b_pair_kinds: collections.Counter[str] = dataclasses.field(
        default_factory=collections.Counter
    )
    max_partial_isometry_error: float = 0.0

    def add_geometry(self, geometry: Geometry, possible: int, surveyed: int) -> None:
        self.total_possible_triples += possible
        key = (geometry.dim, geometry.side)
        if key not in self.by_geometry:
            self.by_geometry[key] = [0, 0]
        self.by_geometry[key][0] += possible
        self.by_geometry[key][1] += surveyed

    def update(self, a_encoding: Encoding, r_encoding: Encoding, b_encoding: Encoding) -> None:
        self.surveyed_triples += 1

        a_to_r_kind = pair_requirement_kind(a_encoding, r_encoding)
        r_to_b_kind = pair_requirement_kind(r_encoding, b_encoding)
        self.a_to_r_pair_kinds[a_to_r_kind] += 1
        self.r_to_b_pair_kinds[r_to_b_kind] += 1

        a_to_r_same = a_to_r_kind == "same_support"
        r_to_b_same = r_to_b_kind == "same_support"
        self.a_to_r_same_support += int(a_to_r_same)
        self.explicit_a_to_r_maps += int(not a_to_r_same)
        self.r_to_b_same_support += int(r_to_b_same)
        self.explicit_r_to_b_maps += int(not r_to_b_same)
        self.no_site_maps_needed += int(a_to_r_same and r_to_b_same)
        self.both_site_maps_needed += int((not a_to_r_same) and (not r_to_b_same))

        fixed_bell_x_sufficient = a_encoding.fixed_x_usable and r_encoding.fixed_x_usable
        cross_pairing_required = not a_to_r_same
        axis_adapted_required = not fixed_bell_x_sufficient
        adapted_bell_required = cross_pairing_required or axis_adapted_required

        self.cross_register_bell_pairing_required += int(cross_pairing_required)
        self.axis_adapted_bell_x_required += int(axis_adapted_required)
        self.adapted_bell_measurement_required += int(adapted_bell_required)
        self.fixed_last_axis_bell_x_sufficient += int(fixed_bell_x_sufficient)

        self.max_partial_isometry_error = max(
            self.max_partial_isometry_error,
            partial_isometry_error(a_encoding, r_encoding),
            partial_isometry_error(r_encoding, b_encoding),
        )


def parse_csv_ints(raw: str) -> tuple[int, ...]:
    values = tuple(int(part.strip()) for part in raw.split(",") if part.strip())
    if not values:
        raise ValueError("expected at least one integer")
    return values


def coordinate_index(coords: tuple[int, ...], side: int) -> int:
    index = 0
    for coord in coords:
        index = index * side + coord
    return index


def build_cell_taste_operator(
    dim: int, side: int, taste_paulis: Iterable[np.ndarray]
) -> np.ndarray:
    taste_paulis = list(taste_paulis)
    if side % 2 != 0:
        raise ValueError("KS taste decomposition requires even side length")
    if len(taste_paulis) != dim:
        raise ValueError("Need one Pauli factor per taste axis")

    n_sites = side**dim
    op = np.zeros((n_sites, n_sites), dtype=complex)
    coords_list = list(itertools.product(range(side), repeat=dim))

    for i, coords_i in enumerate(coords_list):
        cell_i = tuple(coord // 2 for coord in coords_i)
        eta_i = tuple(coord % 2 for coord in coords_i)
        for j, coords_j in enumerate(coords_list):
            cell_j = tuple(coord // 2 for coord in coords_j)
            if cell_i != cell_j:
                continue
            eta_j = tuple(coord % 2 for coord in coords_j)
            element = 1.0 + 0.0j
            for axis in range(dim):
                element *= taste_paulis[axis][eta_i[axis], eta_j[axis]]
            op[i, j] = element
    return op


def build_sublattice_z(dim: int, side: int) -> np.ndarray:
    coords_list = list(itertools.product(range(side), repeat=dim))
    parity = [(-1) ** sum(coords) for coords in coords_list]
    return np.diag([float(value) for value in parity]).astype(complex)


def build_pair_hop_x(dim: int, side: int) -> np.ndarray:
    n_sites = side**dim
    if n_sites % 2 != 0:
        raise ValueError("pair-hop X requires an even number of sites")
    op = np.zeros((n_sites, n_sites), dtype=complex)
    for pair in range(n_sites // 2):
        i, j = 2 * pair, 2 * pair + 1
        op[i, j] = 1.0
        op[j, i] = 1.0
    return op


def encoded_indices_and_etas(
    dim: int,
    side: int,
    cell: tuple[int, ...],
    logical_axis: int,
    spectators: tuple[int, ...],
) -> tuple[tuple[int, int], tuple[tuple[int, ...], tuple[int, ...]]]:
    spectator_axes = tuple(axis for axis in range(dim) if axis != logical_axis)
    if len(spectators) != len(spectator_axes):
        raise ValueError("wrong number of spectator taste bits")

    spectator_by_axis = dict(zip(spectator_axes, spectators))
    indices: list[int] = []
    etas: list[tuple[int, ...]] = []
    for logical_bit in (0, 1):
        eta = [0] * dim
        eta[logical_axis] = logical_bit
        for axis in spectator_axes:
            eta[axis] = spectator_by_axis[axis]
        eta_tuple = tuple(eta)
        coords = tuple(2 * cell[axis] + eta_tuple[axis] for axis in range(dim))
        indices.append(coordinate_index(coords, side))
        etas.append(eta_tuple)
    return (indices[0], indices[1]), (etas[0], etas[1])


def restrict_to_encoded_qubit(op: np.ndarray, indices: tuple[int, int]) -> np.ndarray:
    return op[np.ix_(indices, indices)]


def leakage_norm(op: np.ndarray, indices: tuple[int, int]) -> float:
    columns = op[:, list(indices)].copy()
    columns[list(indices), :] = 0.0
    return float(np.linalg.norm(columns))


def max_abs(op: np.ndarray) -> float:
    return float(np.max(np.abs(op)))


def encoding_isometry(encoding: Encoding) -> np.ndarray:
    """Return V_E with the ordered encoded site states as its columns."""

    isometry = np.zeros((encoding.geometry.n_sites, 2), dtype=complex)
    for logical_bit, site_index in enumerate(encoding.indices):
        isometry[site_index, logical_bit] = 1.0
    return isometry


def signed_pauli_match(
    restricted: np.ndarray, target: np.ndarray, tolerance: float
) -> tuple[bool, int | None]:
    if np.allclose(restricted, target, atol=tolerance):
        return True, 1
    if np.allclose(restricted, -target, atol=tolerance):
        return True, -1
    return False, None


def axis_taste_x(dim: int, side: int, axis: int) -> np.ndarray:
    paulis = [I2] * dim
    paulis[axis] = X2
    return build_cell_taste_operator(dim, side, paulis)


def enumerate_encodings(geometry: Geometry, tolerance: float) -> list[Encoding]:
    z_site = build_sublattice_z(geometry.dim, geometry.side)
    fixed_x_site = build_pair_hop_x(geometry.dim, geometry.side)
    adapted_x_by_axis = {
        axis: axis_taste_x(geometry.dim, geometry.side, axis)
        for axis in range(geometry.dim)
    }

    encodings: list[Encoding] = []
    for cell in itertools.product(range(geometry.side // 2), repeat=geometry.dim):
        for logical_axis in range(geometry.dim):
            spectator_axes = tuple(axis for axis in range(geometry.dim) if axis != logical_axis)
            for spectators in itertools.product((0, 1), repeat=len(spectator_axes)):
                indices, eta_pair = encoded_indices_and_etas(
                    geometry.dim,
                    geometry.side,
                    cell,
                    logical_axis,
                    spectators,
                )
                z_logical = restrict_to_encoded_qubit(z_site, indices)
                adapted_x_logical = restrict_to_encoded_qubit(
                    adapted_x_by_axis[logical_axis],
                    indices,
                )
                fixed_x_logical = restrict_to_encoded_qubit(fixed_x_site, indices)

                z_signed, z_sign = signed_pauli_match(z_logical, Z2, tolerance)
                adapted_x_signed, adapted_x_sign = signed_pauli_match(
                    adapted_x_logical,
                    X2,
                    tolerance,
                )
                fixed_x_signed, fixed_x_sign = signed_pauli_match(
                    fixed_x_logical,
                    X2,
                    tolerance,
                )
                if not z_signed or z_sign is None:
                    raise ValueError(f"Z is not a signed Pauli on indices {indices}")
                if not adapted_x_signed or adapted_x_sign is None:
                    raise ValueError(f"adapted X is not a signed Pauli on indices {indices}")

                fixed_x_square_error = max_abs(fixed_x_logical @ fixed_x_logical - I2)
                fixed_x_anticommutator_norm = float(
                    np.linalg.norm(z_logical @ fixed_x_logical + fixed_x_logical @ z_logical)
                )
                fixed_x_leakage = leakage_norm(fixed_x_site, indices)
                fixed_x_usable = bool(
                    fixed_x_signed
                    and fixed_x_leakage < tolerance
                    and fixed_x_square_error < tolerance
                    and fixed_x_anticommutator_norm < tolerance
                )

                encodings.append(
                    Encoding(
                        geometry=geometry,
                        cell=cell,
                        logical_axis=logical_axis,
                        spectators=spectators,
                        indices=indices,
                        eta_pair=eta_pair,
                        z_logical=z_logical,
                        adapted_x_logical=adapted_x_logical,
                        fixed_x_logical=fixed_x_logical,
                        z_sign=z_sign,
                        adapted_x_sign=adapted_x_sign,
                        fixed_x_sign=fixed_x_sign,
                        fixed_x_signed_pauli=fixed_x_signed,
                        fixed_x_leakage=fixed_x_leakage,
                        fixed_x_square_error=fixed_x_square_error,
                        fixed_x_anticommutator_norm=fixed_x_anticommutator_norm,
                        fixed_x_restriction_zero=bool(
                            np.allclose(fixed_x_logical, np.zeros((2, 2)), atol=tolerance)
                        ),
                        fixed_x_usable=fixed_x_usable,
                    )
                )
    return encodings


def bell_projector(
    z_a: np.ndarray,
    x_a: np.ndarray,
    z_r: np.ndarray,
    x_r: np.ndarray,
    z_bit: int,
    x_bit: int,
) -> np.ndarray:
    zz = np.kron(z_a, z_r)
    xx = np.kron(x_a, x_r)
    identity = np.eye(4, dtype=complex)
    return 0.25 * (identity + ((-1) ** x_bit) * zz) @ (
        identity + ((-1) ** z_bit) * xx
    )


def bell_projector_metrics(
    z_a: np.ndarray,
    x_a: np.ndarray,
    z_r: np.ndarray,
    x_r: np.ndarray,
) -> BellProjectorMetrics:
    identity = np.eye(4, dtype=complex)
    projectors = [
        bell_projector(z_a, x_a, z_r, x_r, z_bit, x_bit)
        for z_bit, x_bit in OUTCOME_ORDER
    ]
    resolution_error = max_abs(sum(projectors) - identity)
    idempotence_error = max(max_abs(projector @ projector - projector) for projector in projectors)

    orthogonality_error = 0.0
    for i, first in enumerate(projectors):
        for j, second in enumerate(projectors):
            if i == j:
                continue
            orthogonality_error = max(orthogonality_error, max_abs(first @ second))

    return BellProjectorMetrics(
        resolution_error=resolution_error,
        idempotence_error=idempotence_error,
        orthogonality_error=orthogonality_error,
    )


def normalize(state: np.ndarray) -> np.ndarray:
    norm = np.linalg.norm(state)
    if norm <= 1e-15:
        raise ValueError("cannot normalize a zero vector")
    return state / norm


def random_qubit(rng: np.random.Generator) -> np.ndarray:
    state = rng.standard_normal(2) + 1j * rng.standard_normal(2)
    return normalize(state)


def conversion_bell_state(conversion_map: np.ndarray) -> np.ndarray:
    state = np.zeros(4, dtype=complex)
    for logical_bit in range(2):
        resource_basis = np.zeros(2, dtype=complex)
        resource_basis[logical_bit] = 1.0
        state += np.kron(resource_basis, conversion_map[:, logical_bit])
    return normalize(state)


def prepare_three_register_state(input_state: np.ndarray, resource_conversion_map: np.ndarray) -> np.ndarray:
    return np.kron(input_state, conversion_bell_state(resource_conversion_map))


def bob_reduced_from_three_register_state(state: np.ndarray) -> np.ndarray:
    amplitudes = state.reshape(4, 2)
    return amplitudes.T @ amplitudes.conj()


def trace_distance(first: np.ndarray, second: np.ndarray) -> float:
    diff = 0.5 * (first - second + (first - second).conj().T)
    eigvals = np.linalg.eigvalsh(diff)
    return float(0.5 * np.sum(np.abs(eigvals)))


def branch_bob_rho(state: np.ndarray, measurement_operator: np.ndarray) -> tuple[float, np.ndarray]:
    projected = np.kron(measurement_operator, I2) @ state
    probability = float(np.real(np.vdot(projected, projected)))
    if probability <= 1e-15:
        raise ValueError("Bell branch has zero probability")
    amplitudes = projected.reshape(4, 2)
    bob_rho = amplitudes.T @ amplitudes.conj() / probability
    return probability, bob_rho


def correction_operator(z_op: np.ndarray, x_op: np.ndarray, z_bit: int, x_bit: int) -> np.ndarray:
    z_power = z_op if z_bit else I2
    x_power = x_op if x_bit else I2
    return z_power @ x_power


def fidelity_with_pure_state(state: np.ndarray, rho: np.ndarray) -> float:
    state = normalize(state)
    return float(np.real(np.vdot(state, rho @ state)))


def run_teleportation_trials(
    measure_z_a: np.ndarray,
    measure_x_a: np.ndarray,
    measure_z_r: np.ndarray,
    measure_x_r: np.ndarray,
    bob_z_op: np.ndarray,
    bob_x_op: np.ndarray,
    resource_conversion_map: np.ndarray,
    target_conversion_map: np.ndarray,
    n_trials: int,
    rng: np.random.Generator,
) -> TeleportationMetrics:
    half_identity = 0.5 * I2
    min_fidelity = 1.0
    max_infidelity = 0.0
    max_branch_probability_error = 0.0
    max_total_probability_error = 0.0
    max_pre_measurement_trace_distance = 0.0
    max_post_measurement_trace_distance = 0.0
    max_pairwise_pre_message_distance = 0.0
    max_corrected_trace_error = 0.0
    outcomes_seen: set[tuple[int, int]] = set()
    reference_pre_message_rho: np.ndarray | None = None

    projector_metrics = bell_projector_metrics(
        measure_z_a,
        measure_x_a,
        measure_z_r,
        measure_x_r,
    )
    measurement_operators = {
        (z_bit, x_bit): bell_projector(
            measure_z_a,
            measure_x_a,
            measure_z_r,
            measure_x_r,
            z_bit,
            x_bit,
        )
        for z_bit, x_bit in OUTCOME_ORDER
    }

    for _ in range(n_trials):
        input_state = random_qubit(rng)
        target_state = normalize(target_conversion_map @ input_state)
        three_register_state = prepare_three_register_state(
            input_state,
            resource_conversion_map,
        )

        rho_before = bob_reduced_from_three_register_state(three_register_state)
        max_pre_measurement_trace_distance = max(
            max_pre_measurement_trace_distance,
            trace_distance(rho_before, half_identity),
        )

        total_probability = 0.0
        pre_message_rho = np.zeros((2, 2), dtype=complex)
        for z_bit, x_bit in OUTCOME_ORDER:
            probability, bob_rho = branch_bob_rho(
                three_register_state,
                measurement_operators[(z_bit, x_bit)],
            )
            outcomes_seen.add((z_bit, x_bit))
            total_probability += probability
            max_branch_probability_error = max(
                max_branch_probability_error,
                abs(probability - 0.25),
            )
            pre_message_rho += probability * bob_rho

            correction = correction_operator(bob_z_op, bob_x_op, z_bit, x_bit)
            corrected_rho = correction @ bob_rho @ correction.conj().T
            max_corrected_trace_error = max(
                max_corrected_trace_error,
                float(abs(np.trace(corrected_rho) - 1.0)),
            )
            fidelity = fidelity_with_pure_state(target_state, corrected_rho)
            min_fidelity = min(min_fidelity, fidelity)
            max_infidelity = max(max_infidelity, abs(1.0 - fidelity))

        max_total_probability_error = max(
            max_total_probability_error,
            abs(total_probability - 1.0),
        )
        max_post_measurement_trace_distance = max(
            max_post_measurement_trace_distance,
            trace_distance(pre_message_rho, half_identity),
        )
        if reference_pre_message_rho is None:
            reference_pre_message_rho = pre_message_rho
        else:
            max_pairwise_pre_message_distance = max(
                max_pairwise_pre_message_distance,
                trace_distance(pre_message_rho, reference_pre_message_rho),
            )

    return TeleportationMetrics(
        n_trials=n_trials,
        projector_resolution_error=projector_metrics.resolution_error,
        projector_idempotence_error=projector_metrics.idempotence_error,
        projector_orthogonality_error=projector_metrics.orthogonality_error,
        min_fidelity=min_fidelity,
        max_infidelity=max_infidelity,
        max_branch_probability_error=max_branch_probability_error,
        max_total_probability_error=max_total_probability_error,
        max_pre_measurement_trace_distance=max_pre_measurement_trace_distance,
        max_post_measurement_trace_distance=max_post_measurement_trace_distance,
        max_pairwise_pre_message_distance=max_pairwise_pre_message_distance,
        max_corrected_trace_error=max_corrected_trace_error,
        outcomes_seen=tuple(sorted(outcomes_seen)),
    )


def teleportation_metrics_pass(metrics: TeleportationMetrics, tolerance: float) -> bool:
    return bool(
        metrics.projector_resolution_error < tolerance
        and metrics.projector_idempotence_error < tolerance
        and metrics.projector_orthogonality_error < tolerance
        and metrics.max_infidelity < tolerance
        and metrics.max_branch_probability_error < tolerance
        and metrics.max_total_probability_error < tolerance
        and metrics.max_pre_measurement_trace_distance < tolerance
        and metrics.max_post_measurement_trace_distance < tolerance
        and metrics.max_pairwise_pre_message_distance < tolerance
        and metrics.max_corrected_trace_error < tolerance
        and set(metrics.outcomes_seen) == set(OUTCOME_ORDER)
    )


def logical_teleportation_certificate(
    tolerance: float,
) -> LogicalTeleportationCertificate:
    """Check the two-dimensional theorem independently of the encodings.

    Bell-projector algebra is checked directly in the logical basis.  Branch
    Kraus maps, corrected channels, and the Pauli twirl are checked on the four
    matrix units spanning the full 2x2 operator space, so no random-state
    completeness assumption enters the factorized certificate.
    """

    phi = np.array([1.0, 0.0, 0.0, 1.0], dtype=complex) / np.sqrt(2.0)
    phi_matrix = phi.reshape(2, 2)
    projectors: list[np.ndarray] = []
    rank_one_count = 0
    max_outer_product_error = 0.0
    max_branch_map_error = 0.0
    max_branch_channel_basis_error = 0.0
    max_corrected_branch_map_error = 0.0
    max_corrected_channel_basis_error = 0.0

    matrix_units: list[np.ndarray] = []
    for row in range(2):
        for column in range(2):
            matrix_unit = np.zeros((2, 2), dtype=complex)
            matrix_unit[row, column] = 1.0
            matrix_units.append(matrix_unit)

    branch_paulis: list[np.ndarray] = []
    for z_bit, x_bit in OUTCOME_ORDER:
        z_power = Z2 if z_bit else I2
        x_power = X2 if x_bit else I2
        branch_pauli = x_power @ z_power
        correction = z_power @ x_power
        bell_state = np.kron(I2, branch_pauli) @ phi
        projector = bell_projector(Z2, X2, Z2, X2, z_bit, x_bit)
        projectors.append(projector)
        branch_paulis.append(branch_pauli)

        rank_one_count += int(np.linalg.matrix_rank(projector, tol=tolerance) == 1)
        max_outer_product_error = max(
            max_outer_product_error,
            max_abs(projector - np.outer(bell_state, bell_state.conj())),
        )

        branch_map = np.einsum(
            "ar,rb->ba",
            bell_state.reshape(2, 2).conj(),
            phi_matrix,
        )
        max_branch_map_error = max(
            max_branch_map_error,
            max_abs(branch_map - 0.5 * branch_pauli),
        )
        max_corrected_branch_map_error = max(
            max_corrected_branch_map_error,
            max_abs(correction @ branch_map - 0.5 * I2),
        )

        for matrix_unit in matrix_units:
            branch_channel = branch_map @ matrix_unit @ branch_map.conj().T
            expected_branch_channel = (
                0.25 * branch_pauli @ matrix_unit @ branch_pauli.conj().T
            )
            max_branch_channel_basis_error = max(
                max_branch_channel_basis_error,
                max_abs(branch_channel - expected_branch_channel),
            )
            corrected_channel = (
                correction @ branch_channel @ correction.conj().T
            )
            max_corrected_channel_basis_error = max(
                max_corrected_channel_basis_error,
                max_abs(corrected_channel - 0.25 * matrix_unit),
            )

    projector_metrics = bell_projector_metrics(Z2, X2, Z2, X2)
    max_pauli_twirl_basis_error = 0.0
    for matrix_unit in matrix_units:
        twirled = sum(
            (
                0.25
                * pauli
                @ matrix_unit
                @ pauli.conj().T
            )
            for pauli in branch_paulis
        )
        expected = 0.5 * np.trace(matrix_unit) * I2
        max_pauli_twirl_basis_error = max(
            max_pauli_twirl_basis_error,
            max_abs(twirled - expected),
        )

    return LogicalTeleportationCertificate(
        bell_projector_rank_one_count=rank_one_count,
        bell_projector_resolution_error=projector_metrics.resolution_error,
        bell_projector_idempotence_error=projector_metrics.idempotence_error,
        bell_projector_orthogonality_error=projector_metrics.orthogonality_error,
        bell_projector_outer_product_error=max_outer_product_error,
        branch_map_error=max_branch_map_error,
        branch_channel_basis_error=max_branch_channel_basis_error,
        corrected_branch_map_error=max_corrected_branch_map_error,
        corrected_channel_basis_error=max_corrected_channel_basis_error,
        pauli_twirl_basis_error=max_pauli_twirl_basis_error,
    )


def build_structural_certificate(
    encodings_by_geometry: dict[Geometry, list[Encoding]],
    tolerance: float,
) -> StructuralCertificate:
    """Exhaust the local premises whose Cartesian product defines triples."""

    total_encodings = 0
    expected_encodings = 0
    encoding_keys: set[tuple[int, int, tuple[int, int]]] = set()
    implied_ordered_triples = 0
    expected_ordered_triples = 0
    isometry_pass_count = 0
    canonical_pauli_pass_count = 0
    max_isometry_error = 0.0
    max_projector_error = 0.0
    max_canonical_z_error = 0.0
    max_canonical_x_error = 0.0
    max_pauli_square_error = 0.0
    max_pauli_anticommutator_error = 0.0

    for geometry, encodings in encodings_by_geometry.items():
        expected_geometry_encodings = (
            geometry.n_cells * geometry.dim * (2 ** (geometry.dim - 1))
        )
        expected_encodings += expected_geometry_encodings
        expected_ordered_triples += expected_geometry_encodings**3
        implied_ordered_triples += len(encodings) ** 3
        for encoding in encodings:
            total_encodings += 1
            encoding_keys.add(
                (geometry.dim, geometry.side, encoding.indices)
            )
            isometry = encoding_isometry(encoding)
            projector = isometry @ isometry.conj().T
            isometry_error = max_abs(isometry.conj().T @ isometry - I2)
            projector_error = max_abs(projector @ projector - projector)
            max_isometry_error = max(max_isometry_error, isometry_error)
            max_projector_error = max(max_projector_error, projector_error)
            if isometry_error < tolerance and projector_error < tolerance:
                isometry_pass_count += 1

            canonical_z = encoding.canonical_z_logical
            canonical_x = encoding.canonical_adapted_x_logical
            z_error = max_abs(canonical_z - Z2)
            x_error = max_abs(canonical_x - X2)
            square_error = max(
                max_abs(canonical_z @ canonical_z - I2),
                max_abs(canonical_x @ canonical_x - I2),
            )
            anticommutator_error = max_abs(
                canonical_z @ canonical_x + canonical_x @ canonical_z
            )
            max_canonical_z_error = max(max_canonical_z_error, z_error)
            max_canonical_x_error = max(max_canonical_x_error, x_error)
            max_pauli_square_error = max(max_pauli_square_error, square_error)
            max_pauli_anticommutator_error = max(
                max_pauli_anticommutator_error,
                anticommutator_error,
            )
            if max(z_error, x_error, square_error, anticommutator_error) < tolerance:
                canonical_pauli_pass_count += 1

    logical = logical_teleportation_certificate(tolerance)
    logical_pass = bool(
        logical.bell_projector_rank_one_count == len(OUTCOME_ORDER)
        and logical.bell_projector_resolution_error < tolerance
        and logical.bell_projector_idempotence_error < tolerance
        and logical.bell_projector_orthogonality_error < tolerance
        and logical.bell_projector_outer_product_error < tolerance
        and logical.branch_map_error < tolerance
        and logical.branch_channel_basis_error < tolerance
        and logical.corrected_branch_map_error < tolerance
        and logical.corrected_channel_basis_error < tolerance
        and logical.pauli_twirl_basis_error < tolerance
    )
    local_premises_pass = bool(
        total_encodings == expected_encodings
        and len(encoding_keys) == total_encodings
        and implied_ordered_triples == expected_ordered_triples
        and isometry_pass_count == total_encodings
        and canonical_pauli_pass_count == total_encodings
        and logical_pass
    )
    certified_ordered_triples = (
        expected_ordered_triples if local_premises_pass else 0
    )

    return StructuralCertificate(
        total_encodings=total_encodings,
        expected_encodings=expected_encodings,
        unique_encoding_count=len(encoding_keys),
        implied_ordered_triples=implied_ordered_triples,
        expected_ordered_triples=expected_ordered_triples,
        certified_ordered_triples=certified_ordered_triples,
        isometry_pass_count=isometry_pass_count,
        canonical_pauli_pass_count=canonical_pauli_pass_count,
        max_isometry_error=max_isometry_error,
        max_projector_error=max_projector_error,
        max_canonical_z_error=max_canonical_z_error,
        max_canonical_x_error=max_canonical_x_error,
        max_pauli_square_error=max_pauli_square_error,
        max_pauli_anticommutator_error=max_pauli_anticommutator_error,
        logical=logical,
    )


def partial_isometry_error(source: Encoding, target: Encoding) -> float:
    n_sites = source.geometry.n_sites
    conversion = np.zeros((n_sites, n_sites), dtype=complex)
    source_projector = np.zeros((n_sites, n_sites), dtype=complex)
    target_projector = np.zeros((n_sites, n_sites), dtype=complex)
    for source_index, target_index in zip(source.indices, target.indices):
        conversion[target_index, source_index] = 1.0
        source_projector[source_index, source_index] = 1.0
        target_projector[target_index, target_index] = 1.0
    return max(
        max_abs(conversion.conj().T @ conversion - source_projector),
        max_abs(conversion @ conversion.conj().T - target_projector),
    )


def pair_requirement_kind(source: Encoding, target: Encoding) -> str:
    same_support = source.indices == target.indices
    same_cell = source.cell == target.cell
    same_taste = source.eta_pair == target.eta_pair

    if same_support:
        return "same_support"
    if same_taste and not same_cell:
        return "relocation_same_taste"
    if same_cell and not same_taste:
        return "in_cell_retaste"
    return "relocation_and_retaste"


def valid_geometries(dims: Iterable[int], sides: Iterable[int]) -> tuple[list[Geometry], list[tuple[int, int, str]]]:
    geometries: list[Geometry] = []
    skipped: list[tuple[int, int, str]] = []
    for dim in dims:
        for side in sides:
            if dim not in (1, 2, 3):
                skipped.append((dim, side, "dimension outside audited 1D/2D/3D context"))
                continue
            if side <= 0:
                skipped.append((dim, side, "side length must be positive"))
                continue
            if side % 2 != 0:
                skipped.append((dim, side, "KS cell/taste decomposition requires even side"))
                continue
            geometries.append(Geometry(dim=dim, side=side))
    return geometries, skipped


def encode_triple_index(a_index: int, r_index: int, b_index: int, n_encodings: int) -> int:
    return (a_index * n_encodings + r_index) * n_encodings + b_index


def decode_triple_index(index: int, n_encodings: int) -> tuple[int, int, int]:
    b_index = index % n_encodings
    quotient = index // n_encodings
    r_index = quotient % n_encodings
    a_index = quotient // n_encodings
    return a_index, r_index, b_index


def select_triple_indices(
    n_encodings: int,
    max_triples: int,
    rng: np.random.Generator,
) -> list[int]:
    total = n_encodings**3
    if max_triples <= 0 or total <= max_triples:
        return list(range(total))

    selected: set[int] = set()

    def add(a_index: int, r_index: int, b_index: int) -> None:
        if len(selected) < max_triples:
            selected.add(encode_triple_index(a_index, r_index, b_index, n_encodings))

    for i in range(n_encodings):
        add(i, i, i)
    for i in range(n_encodings):
        add(i, (i + 1) % n_encodings, (i + 1) % n_encodings)
    for i in range(n_encodings):
        add(i, i, (i + 1) % n_encodings)
    for i in range(n_encodings):
        add(i, (i + 1) % n_encodings, (i + 2) % n_encodings)

    while len(selected) < max_triples:
        selected.add(int(rng.integers(0, total)))

    return sorted(selected)


def classify_fixed_bell_failure(a_encoding: Encoding, r_encoding: Encoding) -> str:
    a_bad = not a_encoding.fixed_x_usable
    r_bad = not r_encoding.fixed_x_usable
    if a_bad and r_bad:
        return "a_and_r_bell_x_not_axis_adapted"
    if a_bad:
        return "a_bell_x_not_axis_adapted"
    if r_bad:
        return "r_bell_x_not_axis_adapted"
    return "unexpected_fixed_bell_failure"


def classify_bob_fixed_failure(b_encoding: Encoding) -> str:
    if b_encoding.fixed_x_restriction_zero:
        return "bob_fixed_pairhop_x_zero_on_encoding"
    if not b_encoding.fixed_x_signed_pauli:
        return "bob_fixed_pairhop_x_not_logical_x"
    if b_encoding.fixed_x_leakage > 0.0:
        return "bob_fixed_pairhop_x_leaks_out_of_encoding"
    return "bob_fixed_pairhop_x_not_usable"


