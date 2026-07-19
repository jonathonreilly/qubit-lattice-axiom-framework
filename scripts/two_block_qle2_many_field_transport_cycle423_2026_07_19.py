#!/usr/bin/env python3
"""Cycle 423: two-block total-Q<=2 hard-core field transport.

Compose two Cycle-421 reservoir/field vertices with the existing full hard-core
field coin and an exact directed boundary-bit SWAP.  The executed code is the
complete vacuum plus total-Q one and two sector of fourteen M2, dimension 106.

The conserved coordinate is excitation number, not energy, source, work,
time, probability, or a Record.  Authority is none and audit is unset.
"""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path
import sys

import numpy as np
from scipy import sparse


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import proper_cubic_hard_core_many_field_vertex_cycle421_2026_07_19 as c421


c7 = c421.c7
c210 = c7.c210
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "TWO_BLOCK_QLE2_MANY_FIELD_TRANSPORT_CYCLE423_NOTE_2026-07-19.md"
)
ANGLE = c421.ANGLE
BLOCK_DIM = 128
BLOCKS = 2
EDGE_DIRECTION = 0
REVERSE = (1, 0, 3, 2, 5, 4)
MATTER_DIM = 64
PRIOR_TWO_FIELD_WEIGHT = c421.PRIOR_TWO_FIELD_WEIGHT
PRIOR_MISSING_SOURCE_COORDINATE = c421.PRIOR_MISSING_SOURCE_COORDINATE
TOLERANCE = 2e-11
AUTHORITY = "none"
AUDIT = "unset"
PASS = 0
FAIL = 0

Coord = tuple[int, int, int]
CENTERS: tuple[Coord, Coord] = ((0, 0, 0), (3, 0, 0))


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
        "complete total-q<=2 code",
        "dimension 106",
        "two reservoir m2 and twelve field m2",
        "cycle-421 many-field vertex",
        "full hard-core field coin",
        "directed field-bit swap",
        "exact inverse",
        "local continuity",
        "all 24 proper-cubic edge frames",
        "one-source history",
        "two-source history",
        "same-block two-field",
        "saturation and collision",
        "coupling and transport deletion",
        "0.002201473975253681",
        "-0.15248255286187232",
        "m64 matter/contact spectator",
        "not energy, source, work, time, probability, or a record",
        "no negative, no-go, shared-obstruction, or axiom-pressure claim",
    )
    missing = required if not NOTE.exists() else tuple(
        phrase for phrase in required if phrase not in normalized(NOTE)
    )
    check("the Cycle-423 note states the complete Q<=2 transport contract", not missing, missing)


def local_q(state: int) -> int:
    if state not in range(BLOCK_DIM):
        raise ValueError("local reservoir/field basis outside M2 x M64")
    return (state // 64) + (state % 64).bit_count()


def local_field_number(state: int) -> int:
    return (state % 64).bit_count()


def pair_basis() -> tuple[tuple[int, int], ...]:
    return tuple(
        (left, right)
        for total in range(3)
        for left in range(BLOCK_DIM)
        for right in range(BLOCK_DIM)
        if local_q(left) + local_q(right) == total
    )


BASIS = pair_basis()
INDEX = {state: index for index, state in enumerate(BASIS)}
DIMENSION = len(BASIS)


def local_coin() -> np.ndarray:
    return np.kron(np.eye(2), c7.full_field_coin())


@lru_cache(maxsize=None)
def onsite_matrix(delete_vertex: bool = False, delete_coin: bool = False) -> np.ndarray:
    coin = np.eye(BLOCK_DIM, dtype=complex) if delete_coin else local_coin()
    vertex = np.eye(BLOCK_DIM, dtype=complex) if delete_vertex else c421.vertex()
    local = vertex @ coin
    output = np.zeros((DIMENSION, DIMENSION), dtype=complex)
    for source_index, (source_left, source_right) in enumerate(BASIS):
        for target_index, (target_left, target_right) in enumerate(BASIS):
            output[target_index, source_index] = (
                local[target_left, source_left] * local[target_right, source_right]
            )
    return output


def swap_field_bits(left: int, right: int, direction: int) -> tuple[int, int]:
    if direction not in range(6):
        raise ValueError("edge direction must be in range(6)")
    left_reservoir, left_field = divmod(left, 64)
    right_reservoir, right_field = divmod(right, 64)
    left_bit = (left_field >> direction) & 1
    right_direction = REVERSE[direction]
    right_bit = (right_field >> right_direction) & 1
    if left_bit != right_bit:
        left_field ^= 1 << direction
        right_field ^= 1 << right_direction
    return left_reservoir * 64 + left_field, right_reservoir * 64 + right_field


@lru_cache(maxsize=None)
def stream_matrix(direction: int = EDGE_DIRECTION) -> np.ndarray:
    output = np.zeros((DIMENSION, DIMENSION), dtype=complex)
    for source_index, state in enumerate(BASIS):
        target = swap_field_bits(*state, direction)
        output[INDEX[target], source_index] = 1
    return output


@lru_cache(maxsize=None)
def update(
    direction: int = EDGE_DIRECTION,
    delete_vertex: bool = False,
    delete_transport: bool = False,
    delete_coin: bool = False,
) -> np.ndarray:
    stream = (
        np.eye(DIMENSION, dtype=complex)
        if delete_transport
        else stream_matrix(direction)
    )
    return stream @ onsite_matrix(delete_vertex, delete_coin)


def state(left: int, right: int) -> np.ndarray:
    if (left, right) not in INDEX:
        raise ValueError("state is outside the complete total-Q<=2 code")
    result = np.zeros(DIMENSION, dtype=complex)
    result[INDEX[(left, right)]] = 1
    return result


def diagonal(function) -> np.ndarray:
    return np.diag(np.asarray([function(*pair) for pair in BASIS], dtype=float)).astype(complex)


Q_TOTAL = diagonal(lambda left, right: local_q(left) + local_q(right))
Q_LEFT = diagonal(lambda left, _right: local_q(left))
F_TOTAL = diagonal(lambda left, right: local_field_number(left) + local_field_number(right))
F_LEFT = diagonal(lambda left, _right: local_field_number(left))
F_RIGHT = diagonal(lambda _left, right: local_field_number(right))


def expectation(vector: np.ndarray, observable: np.ndarray) -> float:
    return float(np.vdot(vector, observable @ vector).real)


def field_profile(vector: np.ndarray) -> tuple[float, float, float, float]:
    reservoir_left = diagonal(lambda left, _right: left // 64)
    reservoir_right = diagonal(lambda _left, right: right // 64)
    return (
        expectation(vector, reservoir_left),
        expectation(vector, F_LEFT),
        expectation(vector, reservoir_right),
        expectation(vector, F_RIGHT),
    )


def code_layout_controls() -> None:
    q_counts = {
        total: sum(local_q(left) + local_q(right) == total for left, right in BASIS)
        for total in range(3)
    }
    sites = []
    for center in CENTERS:
        sites.append(center)
        for direction in range(6):
            sites.append(tuple(int(center[axis] + c210.DIRECTIONS[direction, axis]) for axis in range(3)))
    edge_left = tuple(int(CENTERS[0][axis] + c210.DIRECTIONS[EDGE_DIRECTION, axis]) for axis in range(3))
    edge_right = tuple(int(CENTERS[1][axis] + c210.DIRECTIONS[REVERSE[EDGE_DIRECTION], axis]) for axis in range(3))
    frame_failures = 0
    for frame in c210.proper_cubic_frames():
        moved = tuple(tuple(int(value) for value in frame @ np.asarray(site)) for site in sites)
        moved_left = tuple(int(value) for value in frame @ np.asarray(edge_left))
        moved_right = tuple(int(value) for value in frame @ np.asarray(edge_right))
        frame_failures += int(len(set(moved)) != 14)
        frame_failures += int(sum(abs(moved_left[i] - moved_right[i]) for i in range(3)) != 1)
    check(
        "the explicit two-block basis is the complete total-Q<=2 sector and the fourteen-M2 edge layout remains local in every frame",
        DIMENSION == 106
        and q_counts == {0: 1, 1: 14, 2: 91}
        and len(BASIS) == len(INDEX)
        and len(set(sites)) == 14
        and frame_failures == 0,
        {
            "physical_M2": 14,
            "reservoir_M2": 2,
            "field_M2": 12,
            "full_Hilbert_dimension": 2**14,
            "executed_Q_le_2_dimension": DIMENSION,
            "sector_dimensions": q_counts,
            "basis_duplicates": len(BASIS) - len(INDEX),
            "edge_SWAP_support_M2": 2,
            "frame_layout_failures": frame_failures,
        },
    )


def operator_continuity_controls() -> np.ndarray:
    gate = update()
    identity = np.eye(DIMENSION, dtype=complex)
    inverse_error = gate.conj().T @ gate - identity
    number_commutator = gate @ Q_TOTAL - Q_TOTAL @ gate
    local = onsite_matrix()
    stream = stream_matrix()
    divergence = local.conj().T @ (stream.conj().T @ Q_LEFT @ stream - Q_LEFT) @ local
    continuity = gate.conj().T @ Q_LEFT @ gate - Q_LEFT
    check(
        "coin-vertex-directed-SWAP is unitary on all 106 states, conserves Q, and satisfies exact block continuity",
        np.linalg.norm(inverse_error) < TOLERANCE
        and np.max(np.linalg.norm(inverse_error, axis=0)) < 8e-13
        and np.linalg.norm(number_commutator) < TOLERANCE
        and np.linalg.norm(continuity - divergence) < TOLERANCE,
        {
            "unitarity_Frobenius_residual": float(np.linalg.norm(inverse_error)),
            "maximum_basis_inverse_residual": float(np.max(np.linalg.norm(inverse_error, axis=0))),
            "Q_commutator": float(np.linalg.norm(number_commutator)),
            "block_local_continuity_residual": float(np.linalg.norm(continuity - divergence)),
            "schedule": "full hard-core field coin; Cycle421 vertices; exact directed field-bit SWAP",
        },
    )
    return gate


def permute_field(field: int, direction_representation: np.ndarray) -> int:
    target = 0
    for source_direction in range(6):
        if (field >> source_direction) & 1:
            target_direction = int(np.argmax(direction_representation[:, source_direction]))
            target |= 1 << target_direction
    return target


def frame_representation(frame: np.ndarray) -> np.ndarray:
    direction = c210.direction_permutation(frame)
    output = np.zeros((DIMENSION, DIMENSION), dtype=complex)
    for source_index, (left, right) in enumerate(BASIS):
        left_r, left_f = divmod(left, 64)
        right_r, right_f = divmod(right, 64)
        target = (
            left_r * 64 + permute_field(left_f, direction),
            right_r * 64 + permute_field(right_f, direction),
        )
        output[INDEX[target], source_index] = 1
    return output


def covariance_controls(gate: np.ndarray) -> None:
    residuals = []
    for frame in c210.proper_cubic_frames():
        representation = frame_representation(frame)
        direction = c210.direction_permutation(frame)
        target_direction = int(np.argmax(direction[:, EDGE_DIRECTION]))
        target = update(target_direction)
        residuals.append(float(np.linalg.norm(representation @ gate @ representation.conj().T - target)))
    check(
        "the complete Q<=2 update intertwines all 24 proper-cubic directed-edge frames",
        len(residuals) == 24 and max(residuals) < TOLERANCE,
        {"frames": len(residuals), "maximum_edge_frame_residual": max(residuals)},
    )


def one_source_history_controls(gate: np.ndarray) -> None:
    initial = state(64, 0)
    first = gate @ initial
    second = gate @ first
    restored = gate.conj().T @ first
    deleted_vertex = update(delete_vertex=True) @ initial
    deleted_transport = update(delete_transport=True) @ initial
    neighbor_field = expectation(first, F_RIGHT)
    expected_neighbor = float(np.sin(ANGLE) ** 2 / 6)
    check(
        "one prepared reservoir produces a transported one-field history and the adjoint reabsorbs it exactly",
        abs(neighbor_field - expected_neighbor) < 5e-14
        and np.linalg.norm(restored - initial) < 3e-14
        and abs(expectation(first, Q_TOTAL) - 1) < 3e-14
        and abs(expectation(second, Q_TOTAL) - 1) < 3e-14
        and expectation(deleted_vertex, F_TOTAL) == 0
        and expectation(deleted_transport, F_RIGHT) == 0
        and expectation(deleted_transport, F_LEFT) > 0,
        {
            "initial_profile_Ra_Fa_Rb_Fb": field_profile(initial),
            "after_one_profile": field_profile(first),
            "after_two_profile": field_profile(second),
            "neighbor_field_weight": neighbor_field,
            "expected_sin2_over_6": expected_neighbor,
            "adjoint_return_reabsorption_residual": float(np.linalg.norm(restored - initial)),
            "vertex_deleted_total_field": expectation(deleted_vertex, F_TOTAL),
            "transport_deleted_neighbor_field": expectation(deleted_transport, F_RIGHT),
        },
    )


def two_source_collision_controls(gate: np.ndarray) -> None:
    initial = state(64, 64)
    first = gate @ initial
    second = gate @ first
    restored = gate.conj().T @ first
    deleted_transport = update(delete_transport=True) @ initial

    total_two_field = diagonal(
        lambda left, right: int(local_field_number(left) + local_field_number(right) == 2)
    )
    same_block_two_field = diagonal(
        lambda left, right: int(
            (local_field_number(left) == 2 and local_field_number(right) == 0)
            or (local_field_number(left) == 0 and local_field_number(right) == 2)
        )
    )
    edge_collision_pair = (
        1 << EDGE_DIRECTION,
        1 << REVERSE[EDGE_DIRECTION],
    )
    collision = state(*edge_collision_pair)
    collision_after = stream_matrix() @ collision
    saturated_local = c421.basis(1, 63)
    saturated_after = c421.vertex() @ saturated_local

    two_field_weight = expectation(first, total_two_field)
    same_block_weight = expectation(first, same_block_two_field)
    deleted_same_block = expectation(deleted_transport, same_block_two_field)
    second_two_field = expectation(second, total_two_field)
    expected = float(np.sin(ANGLE) ** 4)
    comparison = {
        "Cycle423_two_source_weight": two_field_weight,
        "Cycle421_two_independent_vertex_weight": expected,
        "older_two_tick_weight": PRIOR_TWO_FIELD_WEIGHT,
        "difference_from_older": two_field_weight - PRIOR_TWO_FIELD_WEIGHT,
        "ratio_to_older": two_field_weight / PRIOR_TWO_FIELD_WEIGHT,
        "older_missing_source_coordinate": PRIOR_MISSING_SOURCE_COORDINATE,
        "missing_source_coordinate_closed_here": False,
        "comparison_semantics": "different finite schedules; no forced match",
    }
    check(
        "two reservoirs produce and transport a genuine Q=2 two-field sector, including same-block arrivals and hard-core collision/saturation controls",
        abs(two_field_weight - expected) < 8e-14
        and same_block_weight > 0
        and deleted_same_block == 0
        and second_two_field > 0
        and np.linalg.norm(restored - initial) < 8e-14
        and np.linalg.norm(collision_after - collision) == 0
        and np.linalg.norm(saturated_after - saturated_local) == 0,
        {
            "two_field_weight_after_one": two_field_weight,
            "Cycle421_sin4_weight": expected,
            "same_block_two_field_after_transport": same_block_weight,
            "same_block_two_field_transport_deleted": deleted_same_block,
            "two_field_weight_after_two": second_two_field,
            "adjoint_return_reabsorption_residual": float(np.linalg.norm(restored - initial)),
            "occupied_edge_11_SWAP_collision_residual": float(np.linalg.norm(collision_after - collision)),
            "local_saturated_emission_residual": float(np.linalg.norm(saturated_after - saturated_local)),
            "prior_comparison": comparison,
        },
    )


def deletion_and_coin_controls() -> None:
    field_input = state(1 << 2, 0)
    nominal = update() @ field_input
    coin_deleted = update(delete_coin=True) @ field_input
    transport = stream_matrix()
    check(
        "coin, vertex, and transport layers are fixed reversible factors with visible independent deletions",
        np.linalg.norm(transport.conj().T @ transport - np.eye(DIMENSION)) == 0
        and np.linalg.norm(nominal - coin_deleted) > 0.1
        and np.linalg.norm(update(delete_vertex=True) - update()) > 0.1
        and np.linalg.norm(update(delete_transport=True) - update()) > 0.1,
        {
            "directed_SWAP_unitarity_residual": float(
                np.linalg.norm(transport.conj().T @ transport - np.eye(DIMENSION))
            ),
            "coin_deletion_state_residual": float(np.linalg.norm(nominal - coin_deleted)),
            "vertex_deletion_operator_residual": float(np.linalg.norm(update(delete_vertex=True) - update())),
            "transport_deletion_operator_residual": float(np.linalg.norm(update(delete_transport=True) - update())),
        },
    )


def matter_contact_spectator_controls(gate: np.ndarray) -> None:
    matter_identity = sparse.eye(MATTER_DIM, format="csr", dtype=complex)
    full = sparse.kron(matter_identity, sparse.csr_matrix(gate), format="csr")
    identity = sparse.eye(MATTER_DIM * DIMENSION, format="csr", dtype=complex)
    inverse = full.getH() @ full - identity
    matter_number = np.asarray([state.bit_count() for state in range(MATTER_DIM)], dtype=float)
    contact_phases = np.exp(
        1j * c7.c230.COUPLING * matter_number * (matter_number - 1) / 2
    )
    contact = sparse.kron(
        sparse.diags(contact_phases, format="csr"),
        sparse.eye(DIMENSION, format="csr", dtype=complex),
        format="csr",
    )
    contact_residual = float(sparse.linalg.norm(full @ contact - contact @ full))
    row, column = full.nonzero()
    matter_leakage = int(np.count_nonzero(row // DIMENSION != column // DIMENSION))
    angle_import = 0.8 * c7.c219.common_species(c7.BETA).analytic_mass
    check(
        "one M64 matter/contact block is an exact spectator of the complete Q<=2 transport update",
        full.shape == (MATTER_DIM * DIMENSION, MATTER_DIM * DIMENSION)
        and float(sparse.linalg.norm(inverse)) < 2e-10
        and contact_residual == 0
        and matter_leakage == 0
        and abs(angle_import - ANGLE) < 3e-16,
        {
            "joint_basis_dimension": MATTER_DIM * DIMENSION,
            "unitarity_Frobenius_residual": float(sparse.linalg.norm(inverse)),
            "contact_commutator": contact_residual,
            "matter_block_leakage": matter_leakage,
            "Cycle219_mass_angle_difference": angle_import - ANGLE,
            "matter_action": "identity spectator",
        },
    )


def domain_inventory_controls() -> None:
    rejections = 0
    for probe in (
        lambda: local_q(128),
        lambda: swap_field_bits(0, 0, 6),
        lambda: state(64 + 1, 64 + 1),
    ):
        try:
            probe()
        except ValueError:
            rejections += 1
    inventory = {
        "supplied": (
            "two seven-M2 star blocks, finite boundary, chosen directed edge, and total-Q<=2 preparation",
            "Cycle421 many-field vertex and fixed mass-normalized angle",
            "existing full hard-core field coin and coin-vertex-stream order",
            "ordinary two-M2 directional SWAP and proper-cubic direction action",
            "one M64 matter/contact spectator and diagnostic histories/readout",
        ),
        "derived": (
            "complete 106-state Q<=2 update with exact inverse, Q conservation, and local continuity",
            "all-24 directed-edge covariance and layer deletion visibility",
            "one-source transported history with adjoint return/reabsorption",
            "two-source same-block two-field transport and collision/saturation controls",
        ),
        "open": (
            "autonomous same-forward recurrence/return rather than scheduled adjoint recovery",
            "larger cubic lattice, carried reservoir/matter, recoil, contact work, and source calibration",
            "closure of the older missing source coordinate and comparison under a common frozen schedule",
            "energy/source interpretation, time, Born law, Records, metric, and gravity",
        ),
        "host_expectation_queries": 0,
        "global_field_blockade": False,
        "older_missing_source_coordinate_closed": False,
        "number_called_energy": False,
        "schedule_called_time": False,
        "Born_claim": False,
        "actual_Records_added": 0,
        "negative_or_no_go_claim": False,
        "shared_obstruction_claim": False,
        "axiom_pressure": False,
    }
    check(
        "domains and supplied/derived/open inventory preserve the bounded Q<=2 transport boundary",
        rejections == 3
        and not inventory["global_field_blockade"]
        and not inventory["older_missing_source_coordinate_closed"]
        and not inventory["number_called_energy"]
        and not inventory["schedule_called_time"]
        and not inventory["Born_claim"]
        and not inventory["negative_or_no_go_claim"]
        and not inventory["shared_obstruction_claim"]
        and not inventory["axiom_pressure"],
        {"domain_rejections": rejections, **inventory},
    )


def main() -> int:
    print("CYCLE 423: TWO-BLOCK COMPLETE Q<=2 MANY-FIELD TRANSPORT")
    note_contract()
    code_layout_controls()
    gate = operator_continuity_controls()
    covariance_controls(gate)
    one_source_history_controls(gate)
    two_source_collision_controls(gate)
    deletion_and_coin_controls()
    matter_contact_spectator_controls(gate)
    domain_inventory_controls()
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL})
    if FAIL:
        print("RESULT TWO_BLOCK_QLE2_MANY_FIELD_TRANSPORT_NOT_CERTIFIED")
        return 1
    print("RESULT TWO_BLOCK_QLE2_MANY_FIELD_TRANSPORT_CERTIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
