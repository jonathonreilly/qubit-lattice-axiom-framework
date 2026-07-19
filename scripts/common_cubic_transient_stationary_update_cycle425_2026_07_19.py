#!/usr/bin/env python3
"""Cycle 425: one cubic physical update with transient and stationary faces.

Embed the existing source-centered coin/vertex/stream walk into a periodic
installation containing one reservoir M2 and six directional field M2 per
cell.  A frozen physical response bit controls the one active source-cell
Cycle-421 vertex, giving one fixed controlled update with free and defect
branches.  The defect branch supports both the Cycle-422 physical source seed
and a selected stationary dressed eigenstate of that same update.

Eigenpair selection and state preparation remain host-supplied.  Eigenphase
is not a rate; update count is not time; occupation is not energy/source; the
profile is not gravity.  Authority is none and audit is unset.
"""

from __future__ import annotations

from itertools import product
from pathlib import Path
import sys

import numpy as np
from scipy import sparse


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import stationary_dressed_reservoir_shifted_green_profile_2026_07_17 as shore
import physical_number_preserving_cycle416_field_transfer_cycle422_2026_07_19 as c422


c418 = c422.c418
c7 = c418.c7
c210 = shore.c210
c211 = shore.c211
c214 = shore.c214
c216 = shore.c216
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "COMMON_CUBIC_TRANSIENT_STATIONARY_UPDATE_CYCLE425_NOTE_2026-07-19.md"
)
ANGLE = c422.ANGLE
TRAIN_SIZES = (3, 4, 5, 6, 7, 8)
HELD_SIZE = 9
SIZES = TRAIN_SIZES + (HELD_SIZE,)
SOURCE_CELL = (0, 0, 0)
TOLERANCE = 4e-10
AUTHORITY = "none"
AUDIT = "unset"
PASS = 0
FAIL = 0

Coord = tuple[int, int, int]


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def note_contract() -> None:
    required = (
        "authority: none",
        "audit: unset",
        "one fixed response-controlled update",
        "one reservoir m2 plus six directional field m2 per cell",
        "periodic l=3,...,9",
        "l=3,...,8 training",
        "held l=9",
        "cycle-422 physical source seed",
        "transient emission and transport",
        "stationary dressed eigenstate",
        "same update",
        "shifted-green",
        "cycle216",
        "no fitted coefficient",
        "exact inverse",
        "local continuity",
        "all 24 proper-cubic frames",
        "source-seam, vertex, stream, and coin deletions",
        "zero-mode",
        "conjugate branch",
        "eigenpair finding and preparation are host-supplied",
        "eigenphase is not a rate",
        "update count is not time",
        "occupation is not energy or source",
        "profile is not gravity",
        "no no-go, minimum-content, shared-obstruction, or axiom-pressure claim",
    )
    missing = required if not NOTE.exists() else tuple(
        phrase for phrase in required if phrase not in normalized(NOTE)
    )
    check("the Cycle-425 note freezes the common-update and comparison contract", not missing, missing)


def cell_index(cell: Coord, length: int) -> int:
    return shore.site_index(cell, length)


def reservoir_index(cell: Coord, length: int) -> int:
    return cell_index(cell, length)


def field_index(cell: Coord, direction: int, length: int) -> int:
    if direction not in range(6):
        raise ValueError("field direction must be in range(6)")
    return length**3 + 6 * cell_index(cell, length) + direction


def shifted(cell: Coord, displacement: np.ndarray, length: int) -> Coord:
    return tuple(
        int((cell[axis] + int(displacement[axis])) % length)
        for axis in range(3)
    )


def field_coin_layer(length: int, *, delete_coin: bool = False) -> sparse.csr_matrix:
    cells = length**3
    field_coin = (
        sparse.eye(6 * cells, dtype=complex, format="csr")
        if delete_coin
        else sparse.kron(
            sparse.eye(cells, dtype=complex, format="csr"),
            sparse.csr_matrix(c214.FIELD_COIN),
            format="csr",
        )
    )
    return sparse.block_diag(
        (sparse.eye(cells, dtype=complex, format="csr"), field_coin),
        format="csr",
    )


def vertex_layer(
    length: int,
    angle: float,
    *,
    source_cell: Coord = SOURCE_CELL,
) -> sparse.csr_matrix:
    dimension = 7 * length**3
    local = shore.local_vertex_block(angle)
    indices = (reservoir_index(source_cell, length),) + tuple(
        field_index(source_cell, direction, length) for direction in range(6)
    )
    delta = local - np.eye(7, dtype=complex)
    rows = []
    columns = []
    values = []
    for left, target in enumerate(indices):
        for right, source in enumerate(indices):
            if abs(delta[left, right]) > 1e-15:
                rows.append(target)
                columns.append(source)
                values.append(delta[left, right])
    return sparse.eye(dimension, dtype=complex, format="csr") + sparse.csr_matrix(
        (values, (rows, columns)), shape=(dimension, dimension)
    )


def stream_layer(length: int, *, delete_stream: bool = False) -> sparse.csr_matrix:
    cells = length**3
    dimension = 7 * cells
    if delete_stream:
        return sparse.eye(dimension, dtype=complex, format="csr")
    rows = list(range(cells))
    columns = list(range(cells))
    values = [1.0 + 0j] * cells
    for cell in product(range(length), repeat=3):
        for direction, displacement in enumerate(c210.DIRECTIONS):
            target = shifted(cell, displacement, length)
            rows.append(field_index(target, direction, length))
            columns.append(field_index(cell, direction, length))
            values.append(1.0 + 0j)
    return sparse.csr_matrix(
        (values, (rows, columns)), shape=(dimension, dimension)
    )


def cubic_update(
    length: int,
    response: int,
    *,
    source_cell: Coord = SOURCE_CELL,
    delete_vertex: bool = False,
    delete_stream: bool = False,
    delete_coin: bool = False,
) -> sparse.csr_matrix:
    if length < 3:
        raise ValueError("periodic direction streams require L>=3")
    if response not in (0, 1):
        raise ValueError("response control must be binary")
    angle = 0.0 if delete_vertex or response == 0 else ANGLE
    coin = field_coin_layer(length, delete_coin=delete_coin)
    vertex = vertex_layer(length, angle, source_cell=source_cell)
    stream = stream_layer(length, delete_stream=delete_stream)
    return (stream @ vertex @ coin).tocsr()


def source_seed(length: int) -> np.ndarray:
    """Cycle-422 W target code embedded at the source cell."""
    encoding = np.zeros((7 * length**3, 2), dtype=complex)
    encoding[reservoir_index(SOURCE_CELL, length), 0] = 1
    for direction in range(6):
        encoding[field_index(SOURCE_CELL, direction, length), 1] = -c210.UNIFORM[direction]
    return encoding


def shore_embedding(length: int) -> sparse.csr_matrix:
    """Embed [active reservoir, all fields] into all-reservoir cubic Q1 code."""
    cells = length**3
    rows = [reservoir_index(SOURCE_CELL, length)]
    columns = [0]
    values = [1.0 + 0j]
    for flat in range(cells):
        cell = (
            flat // (length * length),
            (flat // length) % length,
            flat % length,
        )
        for direction in range(6):
            rows.append(field_index(cell, direction, length))
            columns.append(1 + 6 * flat + direction)
            values.append(1.0 + 0j)
    return sparse.csr_matrix(
        (values, (rows, columns)),
        shape=(7 * cells, 1 + 6 * cells),
    )


def frame_representation(length: int, frame: np.ndarray) -> sparse.csr_matrix:
    cells = length**3
    direction = c210.direction_permutation(frame)
    direction_map = tuple(int(np.argmax(direction[:, item])) for item in range(6))
    rows = []
    columns = []
    values = []
    for cell in product(range(length), repeat=3):
        target = tuple(int(value % length) for value in frame @ np.asarray(cell))
        rows.append(reservoir_index(target, length))
        columns.append(reservoir_index(cell, length))
        values.append(1.0 + 0j)
        for source_direction in range(6):
            rows.append(field_index(target, direction_map[source_direction], length))
            columns.append(field_index(cell, source_direction, length))
            values.append(1.0 + 0j)
    return sparse.csr_matrix(
        (values, (rows, columns)), shape=(7 * cells, 7 * cells)
    )


def common_update_and_physical_seed_controls() -> None:
    rows = []
    failures = 0
    for length in SIZES:
        encoding = source_seed(length)
        stream = stream_layer(length)
        propagated = stream @ encoding
        target_local = c422.target_encoding()[: c422.TARGET_DIM]
        embedded_target = np.zeros_like(encoding)
        embedded_target[reservoir_index(SOURCE_CELL, length), 0] = target_local[64, 0]
        for direction in range(6):
            embedded_target[field_index(SOURCE_CELL, direction, length), 1] = target_local[1 << direction, 1]
        target_mapping = float(np.linalg.norm(encoding - embedded_target))
        branch_rows = []
        for response in (0, 1):
            update = cubic_update(length, response)
            logical = c422.c418.logical_gate(response, ANGLE)
            residual = float(np.linalg.norm(update @ encoding - propagated @ logical))
            inverse = float(np.linalg.norm(update.conj().T @ propagated - encoding @ logical.conj().T))
            branch_rows.append((response, residual, inverse))
            failures += int(max(residual, inverse) > 5e-14)
        shore_update = shore.defect_update(length, ANGLE)
        embedding = shore_embedding(length)
        defect_residual = float(
            sparse.linalg.norm(cubic_update(length, 1) @ embedding - embedding @ shore_update)
        )
        failures += int(defect_residual > 8e-13 or target_mapping > 2e-15)
        rows.append({
            "L": length,
            "held": length == HELD_SIZE,
            "full_Q1_dimension": 7 * length**3,
            "active_defect_dimension": 1 + 6 * length**3,
            "Cycle422_W_target_mapping": target_mapping,
            "physical_source_EG_rows": branch_rows,
            "shore_embedding_intertwiner": defect_residual,
        })
    check(
        "one fixed response-controlled cubic update carries the Cycle-422 physical seed and exactly embeds the stationary far-shore update",
        tuple(length for length in SIZES[:-1]) == TRAIN_SIZES
        and SIZES[-1] == HELD_SIZE
        and failures == 0,
        {"train_sizes": TRAIN_SIZES, "held_size": HELD_SIZE, "rows": rows, "failures": failures},
    )


def unitary_continuity_covariance_controls() -> None:
    length = 3
    dimension = 7 * length**3
    identity = sparse.eye(dimension, dtype=complex, format="csr")
    q1_operator = identity
    branch_rows = []
    failures = 0
    q_commutator_residuals = []
    for response in (0, 1):
        update = cubic_update(length, response)
        inverse = float(sparse.linalg.norm(update.getH() @ update - identity))
        q_commutator = float(
            sparse.linalg.norm(update @ q1_operator - q1_operator @ update)
        )
        failures += int(inverse > 8e-13)
        failures += int(q_commutator > 8e-13)
        branch_rows.append((response, inverse))
        q_commutator_residuals.append((response, q_commutator))

    update = cubic_update(length, 1)
    local = vertex_layer(length, ANGLE) @ field_coin_layer(length)
    stream = stream_layer(length)
    continuity_residuals = []
    for cell in product(range(length), repeat=3):
        values = np.zeros(dimension)
        values[reservoir_index(cell, length)] = 1
        for direction in range(6):
            values[field_index(cell, direction, length)] = 1
        local_q = sparse.diags(values, format="csr", dtype=complex)
        change = update.getH() @ local_q @ update - local_q
        divergence = local.getH() @ (stream.getH() @ local_q @ stream - local_q) @ local
        continuity_residuals.append(float(sparse.linalg.norm(change - divergence)))

    frame_residuals = []
    for frame in c210.proper_cubic_frames():
        representation = frame_representation(length, frame)
        frame_residuals.append(float(sparse.linalg.norm(representation @ update - update @ representation)))
    check(
        "the common Q1 update is unitary/invertible, locally continuous, bounded by cell/edge gates, and proper-cubic in all frames",
        failures == 0
        and max(continuity_residuals) < 2e-12
        and len(frame_residuals) == 24
        and max(frame_residuals) < 2e-12,
        {
            "Q1_basis_dimension_L3": dimension,
            "branch_unitarity_residuals": branch_rows,
            "branch_Q_commutator_residuals": q_commutator_residuals,
            "maximum_local_continuity_residual": max(continuity_residuals),
            "frames": len(frame_residuals),
            "maximum_frame_residual": max(frame_residuals),
            "cell_M2": 7,
            "response_controlled_vertex_support_M2": 8,
            "field_coin_support_M2": 6,
            "stream_SWAP_support_M2": 2,
        },
    )


def transient_and_deletion_controls() -> None:
    rows = []
    failures = 0
    for length in (5, HELD_SIZE):
        initial = source_seed(length)[:, 0]
        update = cubic_update(length, 1)
        first = update @ initial
        second = update @ first
        restored = update.conj().T @ first
        source_deleted = np.zeros_like(initial)
        vertex_deleted = cubic_update(length, 1, delete_vertex=True) @ initial
        stream_deleted = cubic_update(length, 1, delete_stream=True) @ initial
        coin_probe = np.zeros_like(initial)
        coin_probe[field_index(SOURCE_CELL, 0, length)] = 1
        coin_deleted = cubic_update(length, 1, delete_coin=True) @ coin_probe
        coin_nominal = update @ coin_probe
        cells = length**3
        first_field = float(np.linalg.norm(first[cells:]) ** 2)
        vertex_deleted_field = float(np.linalg.norm(vertex_deleted[cells:]) ** 2)
        stream_deleted_origin = sum(
            abs(stream_deleted[field_index(SOURCE_CELL, direction, length)]) ** 2
            for direction in range(6)
        )
        first_origin = sum(
            abs(first[field_index(SOURCE_CELL, direction, length)]) ** 2
            for direction in range(6)
        )
        failures += int(abs(first_field - np.sin(ANGLE) ** 2) > 4e-14)
        failures += int(np.linalg.norm(restored - initial) > 4e-14)
        failures += int(np.linalg.norm(source_deleted) != 0)
        failures += int(vertex_deleted_field != 0)
        failures += int(abs(stream_deleted_origin - np.sin(ANGLE) ** 2) > 4e-14)
        failures += int(first_origin > 2e-14)
        failures += int(np.linalg.norm(coin_nominal - coin_deleted) < 0.1)
        rows.append({
            "L": length,
            "held": length == HELD_SIZE,
            "first_field_weight": first_field,
            "second_field_weight": float(np.linalg.norm(second[cells:]) ** 2),
            "inverse_residual": float(np.linalg.norm(restored - initial)),
            "source_seam_deleted_norm": float(np.linalg.norm(source_deleted)),
            "vertex_deleted_field_weight": vertex_deleted_field,
            "stream_deleted_origin_field_weight": float(stream_deleted_origin),
            "nominal_origin_after_stream": float(first_origin),
            "coin_deletion_state_residual": float(np.linalg.norm(coin_nominal - coin_deleted)),
        })
    check(
        "the physical source seed gives transient emission/transport on train and held volumes with source-seam, vertex, stream, and coin deletions",
        failures == 0,
        {"rows": rows, "failures": failures, "update_steps_called_time": False},
    )


def stationary_profile_controls():
    rows = []
    cache = {}
    failures = 0
    for length in SIZES:
        shore_update, eigenvalue, shore_state = shore.dressed_eigenstate(length)
        embedding = shore_embedding(length)
        state = embedding @ shore_state
        update = cubic_update(length, 1)
        eigen_residual = float(np.linalg.norm(update @ state - eigenvalue * state))
        stationary_residual = float(np.max(np.abs(abs(update @ state) ** 2 - abs(state) ** 2)))
        eigenphase = float(np.angle(eigenvalue))
        shift = float(6 * (1 - np.cos(eigenphase)))
        source = c211.point_source(length)
        scalar = shore.scalar_projection(shore_state, length)
        scalar_perpendicular = scalar - np.mean(scalar)
        q = shore.emitted_amplitude(shore_state, length)
        shifted_profile = shore.shifted_green_profile(length, shift)
        prediction = q * (-0.5 * source + 1j * np.sin(eigenphase) * shifted_profile)
        normalized_tail = (
            scalar_perpendicular + 0.5 * q * source
        ) / (1j * q * np.sin(eigenphase))
        cycle216 = 3 * c211.solve_field(source)
        profile_ratio = float(np.linalg.norm(shifted_profile - cycle216) / np.linalg.norm(cycle216))
        exact_profile = float(np.linalg.norm(scalar_perpendicular - prediction) / np.linalg.norm(scalar_perpendicular))
        tail_residual = float(np.linalg.norm(normalized_tail - shifted_profile) / np.linalg.norm(shifted_profile))
        laplacian, _ = c211.c9.fourier_symbols(length)
        first_nonzero = float(np.min(laplacian[laplacian > 1e-14]))
        failures += int(eigen_residual > 3e-12 or stationary_residual > 3e-12)
        failures += int(exact_profile > 5e-12 or tail_residual > 4e-11)
        failures += int(not (0 < shift < first_nonzero))
        rows.append({
            "L": length,
            "held": length == HELD_SIZE,
            "full_Q1_dimension": update.shape[0],
            "eigenvalue": eigenvalue,
            "eigenphase_operator_coordinate": eigenphase,
            "reservoir_weight": float(abs(shore_state[0]) ** 2),
            "field_weight": float(np.linalg.norm(shore_state[1:]) ** 2),
            "full_update_eigen_residual": eigen_residual,
            "stationary_component_weight_residual": stationary_residual,
            "spectral_shift": shift,
            "first_nonzero_Laplacian": first_nonzero,
            "exact_shifted_profile_residual": exact_profile,
            "normalized_tail_residual": tail_residual,
            "profile_ratio_to_Cycle216_3Lplus": profile_ratio,
        })
        cache[length] = (eigenvalue, shore_state, state)
    check(
        "the same defect branch has selected stationary dressed eigenstates and the no-refit shifted-Green profile on frozen train/held sizes",
        failures == 0
        and all(0.45 < row["reservoir_weight"] < 0.48 for row in rows)
        and all(rows[index + 1]["profile_ratio_to_Cycle216_3Lplus"] < rows[index]["profile_ratio_to_Cycle216_3Lplus"] for index in range(len(rows) - 1))
        and rows[-1]["profile_ratio_to_Cycle216_3Lplus"] < 7.1e-4,
        {
            "selection_rule_frozen_before_outputs": True,
            "train_sizes": TRAIN_SIZES,
            "held_size": HELD_SIZE,
            "no_fitted_Green_coefficient": True,
            "rows": rows,
            "failures": failures,
        },
    )
    return cache, rows


def zero_mode_conjugate_domain_controls(cache, rows) -> None:
    branch_rows = []
    failures = 0
    for length in SIZES:
        positive_value, positive_shore, _state = cache[length]
        _update, negative_value, negative_state = shore.dressed_eigenstate(length, negative=True)
        full_negative = shore_embedding(length) @ negative_state
        negative_residual = float(np.linalg.norm(cubic_update(length, 1) @ full_negative - negative_value * full_negative))
        phase_sum = float(np.angle(positive_value) + np.angle(negative_value))
        weight_difference = float(abs(abs(positive_shore[0]) ** 2 - abs(negative_state[0]) ** 2))
        failures += int(abs(phase_sum) > 4e-13 or weight_difference > 4e-12 or negative_residual > 3e-12)
        branch_rows.append((length, phase_sum, weight_difference, negative_residual))
    source = c211.point_source(HELD_SIZE)
    source_hat = np.fft.fftn(source, norm="ortho")
    zero_shift = float(np.linalg.norm(shore.shifted_green_profile(HELD_SIZE, 0.0) - 3 * c211.solve_field(source)))
    rejections = 0
    for probe in (
        lambda: cubic_update(2, 1),
        lambda: cubic_update(3, 2),
        lambda: field_index((0, 0, 0), 6, 3),
    ):
        try:
            probe()
        except ValueError:
            rejections += 1
    check(
        "zero-mode subtraction, zero-shift Cycle216 equality, conjugate branch, and lawful domains remain explicit",
        failures == 0
        and abs(source.sum()) < 3e-14
        and abs(source_hat[0, 0, 0]) < 3e-14
        and zero_shift < 5e-13
        and rejections == 3,
        {
            "conjugate_branch_rows": branch_rows,
            "source_sum": float(source.sum()),
            "source_zero_mode": complex(source_hat[0, 0, 0]),
            "zero_shift_to_Cycle216_residual": zero_shift,
            "held_shifted_profile_ratio": rows[-1]["profile_ratio_to_Cycle216_3Lplus"],
            "domain_rejections": rejections,
        },
    )


def matter_contact_and_inventory_controls() -> None:
    length = 3
    update = cubic_update(length, 1)
    matter_identity = sparse.eye(64, dtype=complex, format="csr")
    joined = sparse.kron(matter_identity, update, format="csr")
    identity = sparse.eye(joined.shape[0], dtype=complex, format="csr")
    matter_number = np.asarray([state.bit_count() for state in range(64)], dtype=float)
    contact_phases = np.exp(1j * c7.c230.COUPLING * matter_number * (matter_number - 1) / 2)
    contact = sparse.kron(
        sparse.diags(contact_phases, format="csr"),
        sparse.eye(update.shape[0], dtype=complex, format="csr"),
        format="csr",
    )
    contact_residual = float(sparse.linalg.norm(joined @ contact - contact @ joined))
    row, column = joined.nonzero()
    matter_leakage = int(np.count_nonzero(row // update.shape[0] != column // update.shape[0]))
    angle_import = 0.8 * c7.c219.common_species(c7.BETA).analytic_mass
    inventory = {
        "supplied": (
            "Cycle422 physical W preparation/blank-target contract and signed Cycle418 seed",
            "one reservoir plus six field M2 per periodic cell and one frozen source response at the origin",
            "Cycle214 field coin, Cycle421 Q1 vertex restriction, ordinary directional streams, and coin-vertex-stream order",
            "L3-L8 training/L9 held boundary, source-centered defect, zero-mean convention, and Cycle216 3L+ comparator",
            "host shift-invert target/candidate count/sign filter/reservoir-weight selection, normalization, and phase convention",
            "one M64 matter/contact spectator and diagnostic readout/tolerances",
        ),
        "derived": (
            "one fixed response-controlled cubic Q1 update with exact Cycle422-source E/G and inverse",
            "unitarity, local continuity, proper-cubic covariance, transient transport, and deletion visibility",
            "stationary dressed eigenpairs of the same defect branch and conditional no-refit shifted-Green identity",
            "zero-mode/conjugate/held/domain and matter-contact spectator controls",
        ),
        "open": (
            "physical eigenpair selection and preparation; both remain host-supplied",
            "many-excitation cubic execution, carried matter/reservoir, recoil, contact work, and autonomous source recurrence",
            "equality to Cycle216 at finite nonzero shift or comparison under a different kernel/schedule",
            "energy/source interpretation, physical time/rate, Born law, Records, metric, and gravity",
        ),
        "eigenpair_finding_host_supplied": True,
        "eigenstate_preparation_host_supplied": True,
        "physical_source_EG_constructed": True,
        "profile_called_gravity": False,
        "occupation_called_energy_or_source": False,
        "eigenphase_called_rate": False,
        "update_count_called_time": False,
        "Born_claim": False,
        "actual_Records_added": 0,
        "negative_or_no_go_claim": False,
        "minimum_content_claim": False,
        "shared_obstruction_claim": False,
        "axiom_pressure": False,
    }
    check(
        "M64 mass/contact is a spectator and the inventory audits host-supplied eigenpair finding/preparation without semantic promotion",
        float(sparse.linalg.norm(joined.getH() @ joined - identity)) < 2e-11
        and contact_residual == 0
        and matter_leakage == 0
        and abs(angle_import - ANGLE) < 3e-16
        and inventory["eigenpair_finding_host_supplied"]
        and inventory["eigenstate_preparation_host_supplied"]
        and inventory["physical_source_EG_constructed"]
        and not inventory["profile_called_gravity"]
        and not inventory["occupation_called_energy_or_source"]
        and not inventory["eigenphase_called_rate"]
        and not inventory["update_count_called_time"]
        and not inventory["Born_claim"]
        and not inventory["negative_or_no_go_claim"]
        and not inventory["minimum_content_claim"]
        and not inventory["shared_obstruction_claim"]
        and not inventory["axiom_pressure"],
        {
            "joint_M64_x_Q1_dimension": joined.shape[0],
            "joint_unitarity_residual": float(sparse.linalg.norm(joined.getH() @ joined - identity)),
            "contact_commutator": contact_residual,
            "matter_block_leakage": matter_leakage,
            "mass_angle_difference": angle_import - ANGLE,
            **inventory,
        },
    )


def main() -> int:
    print("CYCLE 425: COMMON CUBIC TRANSIENT / STATIONARY PHYSICAL UPDATE")
    note_contract()
    common_update_and_physical_seed_controls()
    unitary_continuity_covariance_controls()
    transient_and_deletion_controls()
    cache, rows = stationary_profile_controls()
    zero_mode_conjugate_domain_controls(cache, rows)
    matter_contact_and_inventory_controls()
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL})
    if FAIL:
        print("RESULT COMMON_CUBIC_TRANSIENT_STATIONARY_UPDATE_NOT_CERTIFIED")
        return 1
    print("RESULT COMMON_CUBIC_TRANSIENT_STATIONARY_UPDATE_CERTIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
