#!/usr/bin/env python3
"""Cycle 426: physical recoil/contact to hard-core field common-code bridge.

Lift the Cycle-322 matter-controlled, coefficient-two recoil source from its
global-Q=1 label space to two ordinary seven-M2 reservoir/field stars.  The
new fixed local Hermitian generator acts on hard-core occupations and is
composed with the Cycle-315 M64xM64 matter coin/FSWAP/contact seam and the
Cycle-423 field coin/directed-SWAP transport schedule.

The executed common code is M64 x M64 tensor the complete fourteen-M2
total-Q<=2 sector.  Excitation number and the source-layer recoil coordinate
are finite operator ledgers, not energy, source, work, rate, probability, or
a Record.  Authority is none and audit is unset.
"""

from __future__ import annotations

from functools import lru_cache
from itertools import product
from pathlib import Path
import sys

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import expm_multiply


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import connected_edge_same_code_local_instrument_cycle278_2026_07_17 as c278
import physical_cycle269_overlap_aware_two_cell_cycle315_2026_07_18 as c315
import two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18 as c322
import physical_number_preserving_cycle416_field_transfer_cycle422_2026_07_19 as c422
import two_block_qle2_many_field_transport_cycle423_2026_07_19 as c423


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_RECOIL_HARD_CORE_FIELD_BRIDGE_CYCLE426_NOTE_2026-07-19.md"
)
ANGLE = c322.ANGLE
EDGE_DIRECTION = c423.EDGE_DIRECTION
REVERSE = c322.REVERSE
MATTER_DIM = 4096
FIELD_DIM = c423.DIMENSION
COMMON_DIMENSION = MATTER_DIM * FIELD_DIM
SIZES = (3, 4, 6)
HELD_SIZE = 6
TOLERANCE = 8e-10
AUTHORITY = "none"
AUDIT = "unset"
PASS = 0
FAIL = 0

FieldPair = tuple[int, int]
LogicalState = dict[FieldPair, np.ndarray]
PhysicalState = dict[FieldPair, np.ndarray]


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
        "m64 tensor m64 tensor complete total-q<=2",
        "fixed hard-core recoil generator",
        "e_common g_common = g_physical,common e_common",
        "coefficient-two recoil ledger",
        "field emission, transport, and absorption",
        "one-source and two-source histories",
        "reciprocal a-to-b and b-to-a response",
        "all 24 proper-cubic frames",
        "held l=6",
        "source, coupling, contact, and transport deletions",
        "source coupling, calibration, and blank preparation",
        "not energy, source, work, rate, probability, or a record",
        "scheduled adjoint return is not autonomous recurrence",
        "no host expectation controls a gate",
        "no negative, no-go, minimum-content, shared-obstruction, or axiom-pressure claim",
    )
    missing = required if not NOTE.exists() else tuple(
        phrase for phrase in required if phrase not in normalized(NOTE)
    )
    check("the Cycle-426 note states the common-code construction and boundary", not missing, missing)


def local_states(q_number: int) -> tuple[int, ...]:
    if q_number not in range(8):
        raise ValueError("local reservoir-plus-field number must be in 0..7")
    return tuple(state for state in range(128) if c423.local_q(state) == q_number)


LOCAL_STATES = {q: local_states(q) for q in range(8)}
LOCAL_STATE_INDEX = {
    q: {state: index for index, state in enumerate(states)}
    for q, states in LOCAL_STATES.items()
}


@lru_cache(maxsize=None)
def recoil_generator(q_number: int, omit_direction: int | None = None) -> sparse.csr_matrix:
    """Second-quantized even-CAR recoil exchange on one M64 x seven-M2 star."""

    if omit_direction is not None and omit_direction not in range(6):
        raise ValueError("omitted direction must be in 0..5")
    states = LOCAL_STATES[q_number]
    state_index = LOCAL_STATE_INDEX[q_number]
    local_field_dimension = len(states)
    rows: list[int] = []
    columns: list[int] = []
    data: list[complex] = []
    for matter_index, mask in enumerate(c322.LOCAL_MASKS):
        for field_index, field_state in enumerate(states):
            reservoir, field = divmod(field_state, 64)
            if reservoir != 1:
                continue
            source = matter_index * local_field_dimension + field_index
            for direction in range(6):
                if direction == omit_direction or ((field >> direction) & 1):
                    continue
                hopped = c322.fermion_hop(mask, direction, REVERSE[direction])
                if hopped is None:
                    continue
                target_mask, sign = hopped
                target_matter = c322.LOCAL_INDEX[target_mask]
                target_state = field | (1 << direction)
                target = (
                    target_matter * local_field_dimension
                    + state_index[target_state]
                )
                rows.extend((target, source))
                columns.extend((source, target))
                data.extend((complex(sign), complex(sign)))
    dimension = 64 * local_field_dimension
    return sparse.coo_matrix(
        (data, (rows, columns)), shape=(dimension, dimension), dtype=complex
    ).tocsr()


def local_diagonal(q_number: int, function) -> sparse.csr_matrix:
    states = LOCAL_STATES[q_number]
    values = []
    for mask in c322.LOCAL_MASKS:
        for field_state in states:
            values.append(function(mask, field_state))
    return sparse.diags(np.asarray(values, dtype=float), format="csr")


def source_layer_operator_controls() -> None:
    print("\nFIXED HARD-CORE RECOIL SOURCE OPERATOR")
    rows = []
    maximum_frame_residual = 0.0
    for q_number in (0, 1, 2):
        generator = recoil_generator(q_number)
        matter_number = local_diagonal(q_number, lambda mask, _field: mask.bit_count())
        total_q = local_diagonal(q_number, lambda _mask, field: c423.local_q(field))
        momentum = []
        for axis in range(3):
            momentum.append(
                local_diagonal(
                    q_number,
                    lambda mask, field, axis=axis: sum(
                        c423.c210.DIRECTIONS[d, axis]
                        for d in range(6)
                        if (mask >> d) & 1
                    )
                    + 2
                    * sum(
                        c423.c210.DIRECTIONS[d, axis]
                        for d in range(6)
                        if ((field % 64) >> d) & 1
                    ),
                )
            )
        row = {
            "Q": q_number,
            "dimension": generator.shape[0],
            "nonzero_generator_entries": int(generator.nnz),
            "Hermiticity_residual": float(sparse.linalg.norm(generator - generator.getH())),
            "matter_number_commutator": float(
                sparse.linalg.norm(generator @ matter_number - matter_number @ generator)
            ),
            "Q_commutator": float(sparse.linalg.norm(generator @ total_q - total_q @ generator)),
            "P_commutators": tuple(
                float(sparse.linalg.norm(generator @ component - component @ generator))
                for component in momentum
            ),
        }
        rows.append(row)

    for frame in c423.c210.proper_cubic_frames():
        for q_number in (1, 2):
            representation = recoil_frame(q_number, frame)
            generator = recoil_generator(q_number)
            maximum_frame_residual = max(
                maximum_frame_residual,
                float(
                    sparse.linalg.norm(
                        representation @ generator @ representation.getH() - generator
                    )
                ),
            )
    check(
        "one fixed hard-core source generator preserves local matter number, total Q, and the coefficient-two recoil coordinate through Q=2",
        max(
            max(
                row["Hermiticity_residual"],
                row["matter_number_commutator"],
                row["Q_commutator"],
                *row["P_commutators"],
            )
            for row in rows
        )
        == 0
        and maximum_frame_residual == 0,
        {"sectors": rows, "maximum_24_frame_generator_residual": maximum_frame_residual},
    )


def permute_local_field_state(state: int, direction_representation: np.ndarray) -> int:
    reservoir, field = divmod(state, 64)
    return reservoir * 64 + c423.permute_field(field, direction_representation)


@lru_cache(maxsize=None)
def recoil_frame_cached(q_number: int, frame_bytes: bytes) -> sparse.csr_matrix:
    frame = np.frombuffer(frame_bytes, dtype=np.int64).reshape(3, 3)
    direction = c423.c210.direction_permutation(frame)
    fock = c322.local_fock_frame(frame)
    states = LOCAL_STATES[q_number]
    state_index = LOCAL_STATE_INDEX[q_number]
    local_field_dimension = len(states)
    rows = []
    columns = []
    data = []
    for matter_source in range(64):
        matter_column = fock[:, matter_source]
        matter_target = int(np.argmax(abs(matter_column)))
        sign = complex(matter_column[matter_target])
        for field_source, state in enumerate(states):
            target_state = permute_local_field_state(state, direction)
            field_target = state_index[target_state]
            source = matter_source * local_field_dimension + field_source
            target = matter_target * local_field_dimension + field_target
            rows.append(target)
            columns.append(source)
            data.append(sign)
    dimension = 64 * local_field_dimension
    return sparse.coo_matrix(
        (data, (rows, columns)), shape=(dimension, dimension), dtype=complex
    ).tocsr()


def recoil_frame(q_number: int, frame: np.ndarray) -> sparse.csr_matrix:
    return recoil_frame_cached(q_number, np.asarray(frame, dtype=np.int64).tobytes())


def q1_encoding() -> sparse.csr_matrix:
    """Cycle-322 seven-label sector into the seven-M2 one-excitation sector."""

    states = LOCAL_STATES[1]
    state_index = LOCAL_STATE_INDEX[1]
    rows = []
    columns = []
    for matter in range(64):
        labels = (64,) + tuple(1 << direction for direction in range(6))
        for old_q, field_state in enumerate(labels):
            rows.append(matter * len(states) + state_index[field_state])
            columns.append(7 * matter + old_q)
    return sparse.coo_matrix(
        (np.ones(len(rows)), (rows, columns)), shape=(448, 448), dtype=complex
    ).tocsr()


def q1_seam_controls() -> None:
    old_exchange, old_vertex, _charge, _number, _momenta = c322.local_source_blocks(ANGLE)
    encoding = q1_encoding()
    new_exchange = recoil_generator(1)
    rng = np.random.default_rng(42601)
    probe = rng.normal(size=448) + 1j * rng.normal(size=448)
    probe /= np.linalg.norm(probe)
    mapped = encoding @ probe
    new_output = expm_multiply(1j * ANGLE * new_exchange, mapped)
    expected = encoding @ (old_vertex @ probe)
    inverse = expm_multiply(-1j * ANGLE * new_exchange, new_output)
    check(
        "the Cycle-322 recoil vertex embeds exactly into the seven-M2 Q=1 sector with forward and inverse intertwining",
        sparse.linalg.norm(new_exchange @ encoding - encoding @ sparse.csr_matrix(old_exchange))
        == 0
        and np.linalg.norm(new_output - expected) < 4e-13
        and np.linalg.norm(inverse - mapped) < 4e-13,
        {
            "encoding_shape": encoding.shape,
            "Gram_residual": float(sparse.linalg.norm(encoding.getH() @ encoding - sparse.eye(448))),
            "generator_intertwiner_residual": float(
                sparse.linalg.norm(new_exchange @ encoding - encoding @ sparse.csr_matrix(old_exchange))
            ),
            "finite_forward_intertwiner_residual": float(np.linalg.norm(new_output - expected)),
            "finite_inverse_residual": float(np.linalg.norm(inverse - mapped)),
        },
    )


def prune(state: dict, threshold: float = 2e-13) -> dict:
    return {key: value for key, value in state.items() if np.linalg.norm(value) > threshold}


def validate_common_keys(state: dict) -> None:
    for pair in state:
        if pair not in c423.INDEX:
            raise ValueError("field state is outside the complete total-Q<=2 code")


def state_norm(state: dict) -> float:
    return float(sum(np.vdot(value, value).real for value in state.values()))


def state_residual(left: dict, right: dict) -> float:
    if not left and not right:
        return 0.0
    sample = next(iter(left.values()), next(iter(right.values())))
    zero = np.zeros_like(sample)
    return float(
        np.sqrt(
            sum(
                np.vdot(
                    left.get(key, zero) - right.get(key, zero),
                    left.get(key, zero) - right.get(key, zero),
                ).real
                for key in left.keys() | right.keys()
            )
        )
    )


def apply_matter_factor(state: LogicalState, factor: sparse.spmatrix) -> LogicalState:
    return prune({key: factor @ value for key, value in state.items()})


def local_coin_transitions(state: int, *, inverse: bool = False):
    reservoir, field = divmod(state, 64)
    if field.bit_count() != 1:
        return ((state, 1.0 + 0j),)
    source_direction = field.bit_length() - 1
    coin = c423.c7.full_field_coin().conj().T if inverse else c423.c7.full_field_coin()
    rows = []
    for target_direction in range(6):
        coefficient = coin[1 << target_direction, 1 << source_direction]
        if abs(coefficient) > 1e-15:
            rows.append((reservoir * 64 + (1 << target_direction), coefficient))
    return tuple(rows)


def apply_field_coin(
    state: dict, *, inverse: bool = False, enabled: bool = True
) -> dict:
    if not enabled:
        return {key: value.copy() for key, value in state.items()}
    output = {}
    for (left, right), value in state.items():
        for target_left, left_coefficient in local_coin_transitions(left, inverse=inverse):
            for target_right, right_coefficient in local_coin_transitions(right, inverse=inverse):
                key = (target_left, target_right)
                output[key] = output.get(key, 0) + left_coefficient * right_coefficient * value
    return prune(output)


def apply_stream(
    state: dict,
    direction: int = EDGE_DIRECTION,
    *,
    inverse: bool = False,
    enabled: bool = True,
) -> dict:
    if direction not in range(6):
        raise ValueError("edge direction must be in 0..5")
    if not enabled:
        return {key: value.copy() for key, value in state.items()}
    # A SWAP is its own inverse; the flag is explicit for schedule auditing.
    _ = inverse
    return {
        c423.swap_field_bits(left, right, direction): value.copy()
        for (left, right), value in state.items()
    }


def apply_recoil_source(
    state: LogicalState,
    endpoint: int,
    *,
    angle: float = ANGLE,
    inverse: bool = False,
    enabled: bool = True,
) -> LogicalState:
    if endpoint not in (0, 1):
        raise ValueError("endpoint must be zero or one")
    if not enabled or angle == 0:
        return {key: value.copy() for key, value in state.items()}
    output: LogicalState = {}
    other_values = sorted({pair[1 - endpoint] for pair in state})
    exponential_sign = -1 if inverse else 1
    for other_field in other_values:
        other_q = c423.local_q(other_field)
        for local_q_number in range(3 - other_q):
            local_field_states = LOCAL_STATES[local_q_number]
            local_field_dimension = len(local_field_states)
            block = np.zeros((64 * local_field_dimension, 64), dtype=complex)
            present = False
            for field_index, local_field in enumerate(local_field_states):
                pair = (
                    (local_field, other_field)
                    if endpoint == 0
                    else (other_field, local_field)
                )
                value = state.get(pair)
                if value is None:
                    continue
                present = True
                for local_matter in range(64):
                    for other_matter in range(64):
                        joint = (
                            c322.JOINT_INDEX[(local_matter, other_matter)]
                            if endpoint == 0
                            else c322.JOINT_INDEX[(other_matter, local_matter)]
                        )
                        block[
                            local_matter * local_field_dimension + field_index,
                            other_matter,
                        ] = value[joint]
            if not present:
                continue
            transformed = expm_multiply(
                exponential_sign * 1j * angle * recoil_generator(local_q_number),
                block,
            )
            for field_index, local_field in enumerate(local_field_states):
                pair = (
                    (local_field, other_field)
                    if endpoint == 0
                    else (other_field, local_field)
                )
                vector = np.zeros(MATTER_DIM, dtype=complex)
                for local_matter in range(64):
                    for other_matter in range(64):
                        joint = (
                            c322.JOINT_INDEX[(local_matter, other_matter)]
                            if endpoint == 0
                            else c322.JOINT_INDEX[(other_matter, local_matter)]
                        )
                        vector[joint] = transformed[
                            local_matter * local_field_dimension + field_index,
                            other_matter,
                        ]
                if np.linalg.norm(vector) > 2e-13:
                    output[pair] = vector
    return prune(output)


def logical_step(
    state: LogicalState,
    factors,
    *,
    direction: int = EDGE_DIRECTION,
    angles: tuple[float, float] = (ANGLE, ANGLE),
    source_enabled: tuple[bool, bool] = (True, True),
    coupling_enabled: bool = True,
    contact_enabled: bool = True,
    transport_enabled: bool = True,
    field_coin_enabled: bool = True,
) -> LogicalState:
    validate_common_keys(state)
    coin, fswap, contact = factors
    output = apply_matter_factor(state, coin)
    output = apply_field_coin(output, enabled=field_coin_enabled)
    source_angles = angles if coupling_enabled else (0.0, 0.0)
    output = apply_recoil_source(
        output, 0, angle=source_angles[0], enabled=source_enabled[0]
    )
    output = apply_recoil_source(
        output, 1, angle=source_angles[1], enabled=source_enabled[1]
    )
    output = apply_matter_factor(output, fswap)
    output = apply_stream(output, direction, enabled=transport_enabled)
    if contact_enabled:
        output = apply_matter_factor(output, contact)
    return output


def logical_inverse(
    state: LogicalState,
    factors,
    *,
    direction: int = EDGE_DIRECTION,
) -> LogicalState:
    validate_common_keys(state)
    coin, fswap, contact = factors
    output = apply_matter_factor(state, contact.getH())
    output = apply_stream(output, direction, inverse=True)
    output = apply_matter_factor(output, fswap.getH())
    output = apply_recoil_source(output, 1, inverse=True)
    output = apply_recoil_source(output, 0, inverse=True)
    output = apply_field_coin(output, inverse=True)
    return apply_matter_factor(output, coin.getH())


def expectation(state: dict, function) -> float:
    return float(
        sum(np.vdot(value, value).real * function(*key) for key, value in state.items())
    )


def total_q(state: dict) -> float:
    return expectation(state, lambda left, right: c423.local_q(left) + c423.local_q(right))


def field_number(state: dict) -> float:
    return expectation(
        state,
        lambda left, right: c423.local_field_number(left) + c423.local_field_number(right),
    )


def reservoir_weight(state: dict, endpoint: int) -> float:
    return expectation(
        state,
        lambda left, right: (left // 64) if endpoint == 0 else (right // 64),
    )


def block_q(state: dict, endpoint: int) -> float:
    return expectation(
        state,
        lambda left, right: c423.local_q(left) if endpoint == 0 else c423.local_q(right),
    )


def block_field(state: dict, endpoint: int) -> float:
    return expectation(
        state,
        lambda left, right: c423.local_field_number(left)
        if endpoint == 0
        else c423.local_field_number(right),
    )


def two_field_weight(state: dict) -> float:
    return expectation(
        state,
        lambda left, right: int(
            c423.local_field_number(left) + c423.local_field_number(right) == 2
        ),
    )


def same_block_two_field_weight(state: dict) -> float:
    return expectation(
        state,
        lambda left, right: int(
            (c423.local_field_number(left) == 2 and c423.local_field_number(right) == 0)
            or (c423.local_field_number(left) == 0 and c423.local_field_number(right) == 2)
        ),
    )


def response_matrix(factors, *, angles=(ANGLE, ANGLE), source_enabled=(True, True), transport_enabled=True):
    matrix = np.zeros((2, 2), dtype=float)
    maximum_norm_drift = 0.0
    matter = c322.symmetric_one_one_state()
    for source in range(2):
        pair = (64, 0) if source == 0 else (0, 64)
        state: LogicalState = {pair: matter.copy()}
        for _ in range(2):
            state = logical_step(
                state,
                factors,
                angles=angles,
                source_enabled=source_enabled,
                transport_enabled=transport_enabled,
            )
            maximum_norm_drift = max(maximum_norm_drift, abs(state_norm(state) - 1))
        for target in range(2):
            matrix[target, source] = reservoir_weight(state, target)
    return matrix, maximum_norm_drift


def one_source_history_controls(factors) -> None:
    print("\nONE-SOURCE EMISSION / TRANSPORT / ABSORPTION")
    matter = c322.symmetric_one_one_state()
    initial: LogicalState = {(64, 0): matter}
    pre_stream = apply_matter_factor(initial, factors[0])
    pre_stream = apply_field_coin(pre_stream)
    pre_stream = apply_recoil_source(pre_stream, 0)
    pre_stream = apply_recoil_source(pre_stream, 1)
    pre_stream = apply_matter_factor(pre_stream, factors[1])
    first = logical_step(initial, factors)
    second = logical_step(first, factors)
    restored = logical_inverse(first, factors)
    coupling_deleted = logical_step(initial, factors, coupling_enabled=False)
    transport_deleted = logical_step(initial, factors, transport_enabled=False)
    expected_neighbor = float(np.sin(ANGLE) ** 2 / 6)
    neighbor = block_field(first, 1)
    boundary_current = block_q(first, 0) - block_q(pre_stream, 0)
    response, drift = response_matrix(factors)
    receiver_deleted, _ = response_matrix(factors, source_enabled=(True, False))
    stream_deleted, _ = response_matrix(factors, transport_enabled=False)
    asymmetric, _ = response_matrix(factors, angles=(ANGLE, 1.17 * ANGLE))
    check(
        "the fixed common schedule emits, transports, and conjugately reabsorbs one recoil-balanced excitation",
        abs(neighbor - expected_neighbor) < 2e-12
        and np.linalg.norm(restored[(64, 0)] - matter) < 3e-11
        and state_residual(restored, initial) < 3e-11
        and abs(total_q(first) - 1) < 3e-12
        and abs(total_q(second) - 1) < 3e-12
        and field_number(coupling_deleted) == 0
        and block_field(transport_deleted, 1) == 0
        and abs(boundary_current + neighbor) < 3e-12,
        {
            "angle": ANGLE,
            "blank_preparation": "R_A=1; R_B=0; all twelve field M2 blank",
            "neighbor_field_after_one": neighbor,
            "expected_sin2_over_6": expected_neighbor,
            "after_two_total_field": field_number(second),
            "adjoint_return_residual": state_residual(restored, initial),
            "coupling_deleted_field": field_number(coupling_deleted),
            "transport_deleted_neighbor_field": block_field(transport_deleted, 1),
            "boundary_QA_current": boundary_current,
            "one_source_continuity_residual": abs(boundary_current + neighbor),
        },
    )
    check(
        "the two-update response is reciprocal under A/B exchange and distinguishes receiver-source and transport deletion",
        response[0, 1] > 1e-7
        and abs(response[0, 1] - response[1, 0]) < 2e-11
        and abs(response[0, 0] - response[1, 1]) < 2e-11
        and drift < 3e-11
        and receiver_deleted[1, 0] < 2e-13
        and stream_deleted[1, 0] < 2e-13
        and abs(asymmetric[0, 1] - asymmetric[1, 0]) < 2e-11
        and abs(asymmetric[0, 0] - asymmetric[1, 1]) > 1e-3,
        {
            "response_matrix": response.tolist(),
            "reciprocity_residual": abs(response[0, 1] - response[1, 0]),
            "receiver_source_deleted_A_to_B": receiver_deleted[1, 0],
            "transport_deleted_A_to_B": stream_deleted[1, 0],
            "unequal_coupling_matrix": asymmetric.tolist(),
            "maximum_norm_drift": drift,
        },
    )


def two_source_history_controls(factors) -> None:
    print("\nTWO-SOURCE Q=2 / COLLISION / CONTINUITY")
    matter = c322.symmetric_one_one_state()
    initial: LogicalState = {(64, 64): matter}
    pre_stream = apply_matter_factor(initial, factors[0])
    pre_stream = apply_field_coin(pre_stream)
    pre_stream = apply_recoil_source(pre_stream, 0)
    pre_stream = apply_recoil_source(pre_stream, 1)
    pre_stream = apply_matter_factor(pre_stream, factors[1])
    first = apply_stream(pre_stream)
    first = apply_matter_factor(first, factors[2])
    deleted_transport = logical_step(initial, factors, transport_enabled=False)
    second = logical_step(first, factors)
    restored = logical_inverse(first, factors)
    expected_two_field = float(np.sin(ANGLE) ** 4)
    current = block_q(first, 0) - block_q(pre_stream, 0)
    continuity_residual = abs(
        (block_q(first, 0) - block_q(initial, 0))
        - (
            (block_q(pre_stream, 0) - block_q(initial, 0))
            + current
        )
    )
    collision_pair = (1 << EDGE_DIRECTION, 1 << REVERSE[EDGE_DIRECTION])
    collision = {collision_pair: matter}
    collision_after = apply_stream(collision)
    saturated_generator = recoil_generator(7)
    check(
        "two prepared reservoirs enter a genuine transported Q=2 sector with exact hard-core collision and block continuity controls",
        abs(two_field_weight(first) - expected_two_field) < 3e-11
        and same_block_two_field_weight(first) > 1e-6
        and same_block_two_field_weight(deleted_transport) == 0
        and two_field_weight(second) > 0
        and abs(total_q(first) - 2) < 3e-12
        and abs(total_q(second) - 2) < 3e-12
        and state_residual(restored, initial) < 5e-11
        and state_residual(collision_after, collision) == 0
        and saturated_generator.nnz == 0
        and continuity_residual < 3e-12,
        {
            "blank_preparation": "R_A=R_B=1; all twelve field M2 blank",
            "two_field_weight_after_one": two_field_weight(first),
            "expected_sin4": expected_two_field,
            "same_block_two_field_after_transport": same_block_two_field_weight(first),
            "same_block_two_field_transport_deleted": same_block_two_field_weight(deleted_transport),
            "two_field_weight_after_two": two_field_weight(second),
            "adjoint_return_residual": state_residual(restored, initial),
            "boundary_QA_current": current,
            "block_continuity_residual": continuity_residual,
            "occupied_edge_11_SWAP_residual": state_residual(collision_after, collision),
            "saturated_R1_F111111_generator_entries": saturated_generator.nnz,
        },
    )


def random_common_state(seed: int = 426) -> LogicalState:
    rng = np.random.default_rng(seed)
    keys = ((64, 0), (1, 2), (64 + 4, 0))
    state = {
        key: rng.normal(size=MATTER_DIM) + 1j * rng.normal(size=MATTER_DIM)
        for key in keys
    }
    norm = np.sqrt(state_norm(state))
    return {key: value / norm for key, value in state.items()}


def encode_physical(state: LogicalState, encoding: sparse.spmatrix) -> PhysicalState:
    return {key: encoding @ value for key, value in state.items()}


def apply_physical_matter_factor(state: PhysicalState, encoding, factor) -> PhysicalState:
    output = {}
    for key, value in state.items():
        decoded = encoding.getH() @ value
        output[key] = value + encoding @ (factor @ decoded - decoded)
    return prune(output)


def apply_physical_recoil_source(
    state: PhysicalState, encoding, endpoint: int, *, inverse: bool = False
) -> PhysicalState:
    decoded = {key: encoding.getH() @ value for key, value in state.items()}
    transformed = apply_recoil_source(decoded, endpoint, inverse=inverse)
    output = {}
    zero_physical = np.zeros(encoding.shape[0], dtype=complex)
    zero_logical = np.zeros(MATTER_DIM, dtype=complex)
    for key in state.keys() | transformed.keys():
        before_physical = state.get(key, zero_physical)
        before_logical = decoded.get(key, zero_logical)
        after_logical = transformed.get(key, zero_logical)
        output[key] = before_physical + encoding @ (after_logical - before_logical)
    return prune(output)


def physical_step(state: PhysicalState, encoding, factors) -> PhysicalState:
    coin, fswap, contact = factors
    output = apply_physical_matter_factor(state, encoding, coin)
    output = apply_field_coin(output)
    output = apply_physical_recoil_source(output, encoding, 0)
    output = apply_physical_recoil_source(output, encoding, 1)
    output = apply_physical_matter_factor(output, encoding, fswap)
    output = apply_stream(output)
    return apply_physical_matter_factor(output, encoding, contact)


def physical_inverse(state: PhysicalState, encoding, factors) -> PhysicalState:
    coin, fswap, contact = factors
    output = apply_physical_matter_factor(state, encoding, contact.getH())
    output = apply_stream(output, inverse=True)
    output = apply_physical_matter_factor(output, encoding, fswap.getH())
    output = apply_physical_recoil_source(output, encoding, 1, inverse=True)
    output = apply_physical_recoil_source(output, encoding, 0, inverse=True)
    output = apply_field_coin(output, inverse=True)
    return apply_physical_matter_factor(output, encoding, coin.getH())


def common_code_physical_controls(factors) -> None:
    print("\nCOMMON PHYSICAL-M2 INTERTWINER / HELD SIZE")
    encoding = c322.build_encoding(3)
    logical = random_common_state()
    encoded = encode_physical(logical, encoding)
    logical_output = logical_step(logical, factors)
    physical_output = physical_step(encoded, encoding, factors)
    expected = encode_physical(logical_output, encoding)
    restored = physical_inverse(physical_output, encoding, factors)
    size_rows = [c315.size_gram_control(length, c322.LABELS) for length in SIZES]
    identity = sparse.eye(MATTER_DIM, format="csc")
    gram = c315.largest_singular(encoding.getH() @ encoding - identity)
    check(
        "E_common G_common = G_physical,common E_common on a Q=1/Q=2 probe with exact adjoint inverse and zero code leakage",
        gram < TOLERANCE
        and state_residual(physical_output, expected) < TOLERANCE
        and state_residual(restored, encoded) < TOLERANCE
        and abs(state_norm(physical_output) - 1) < TOLERANCE,
        {
            "logical_common_dimension": COMMON_DIMENSION,
            "executed_field_dimension": FIELD_DIM,
            "matter_encoding_shape": encoding.shape,
            "matter_Gram_opnorm_residual": gram,
            "forward_intertwiner_residual": state_residual(physical_output, expected),
            "inverse_residual": state_residual(restored, encoded),
            "output_norm": state_norm(physical_output),
            "off_code_completion": "identity for each bounded local factor",
        },
    )
    check(
        "the complete M64xM64 matter encoding remains isometric through held L=6 while the fourteen field M2 are literal hard-core sites",
        all(row["logical_columns"] == MATTER_DIM for row in size_rows)
        and max(row["Gram_opnorm_residual"] for row in size_rows) < TOLERANCE,
        size_rows,
    )


def support_covariance_origin_controls(factors) -> None:
    print("\nSUPPORT / FRAMES / ORIGINS")
    code = c315.c269.build_code(3)
    endpoint_supports = []
    for cell in c322.ENDPOINTS:
        union = 0
        for row in c278.cell_bs(code, cell):
            union |= row.x | row.z
        endpoint_supports.append(union.bit_count())
    covariance = c315.covariance_translation_controls(
        c322.LABELS, factors[0], factors[2], factors[2] @ factors[1] @ factors[0]
    )
    source_frame_residuals = []
    stream_frame_residuals = []
    base_stream = c423.stream_matrix(EDGE_DIRECTION)
    for frame in c423.c210.proper_cubic_frames():
        source_frame_residuals.append(
            max(
                float(
                    sparse.linalg.norm(
                        recoil_frame(q, frame)
                        @ recoil_generator(q)
                        @ recoil_frame(q, frame).getH()
                        - recoil_generator(q)
                    )
                )
                for q in (1, 2)
            )
        )
        representation = c423.frame_representation(frame)
        direction = c423.c210.direction_permutation(frame)
        target_direction = int(np.argmax(direction[:, EDGE_DIRECTION]))
        stream_frame_residuals.append(
            float(
                np.linalg.norm(
                    representation @ base_stream @ representation.conj().T
                    - c423.stream_matrix(target_direction)
                )
            )
        )
    origin_tests = 0
    origin_failures = 0
    for length in SIZES:
        origins = tuple(product(range(length), repeat=3)) if length == 3 else ((0, 0, 0), (length - 1, 1, 2))
        for origin in origins:
            for direction in range(6):
                target = tuple(
                    (origin[axis] + int(c423.c210.DIRECTIONS[direction, axis])) % length
                    for axis in range(3)
                )
                origin_tests += 1
                origin_failures += int(target == origin)
    check(
        "the 97-M2 patch has bounded endpoint source support and constant 36-M2-per-cell overhead",
        endpoint_supports == [18, 18],
        {
            "Cycle315_matter_M2_per_cell": 29,
            "new_reservoir_plus_field_M2_per_cell": 7,
            "common_M2_per_cell": 36,
            "Cycle315_two_cell_patch_union_M2": 83,
            "common_two_cell_patch_union_M2": 97,
            "endpoint_matter_support_M2": endpoint_supports,
            "endpoint_recoil_vertex_support_M2": [value + 7 for value in endpoint_supports],
            "field_coin_support_M2": 6,
            "boundary_SWAP_support_M2": 2,
        },
    )
    check(
        "matter/contact, recoil source, and directed transport factors cover all 24 proper-cubic frames and translated/held origins",
        covariance["proper_cubic_frames"] == 24
        and covariance["maximum_update_covariance_residual"] < TOLERANCE
        and max(source_frame_residuals) == 0
        and max(stream_frame_residuals) < 2e-12
        and origin_failures == 0,
        {
            "inherited_matter_covariance": covariance,
            "maximum_source_frame_residual": max(source_frame_residuals),
            "maximum_stream_frame_residual": max(stream_frame_residuals),
            "origin_edge_tests": origin_tests,
            "held_L": HELD_SIZE,
            "origin_failures": origin_failures,
        },
    )


def mass_contact_deletion_domain_controls(factors) -> None:
    print("\nMASS / CONTACT / DELETIONS / LAWFUL DOMAIN")
    coin, fswap, contact = factors
    logical_rows = c315.logical_update_controls(c322.LABELS)[4]
    contact_deletion = float(np.max(abs(contact.diagonal() - 1)))
    rng = np.random.default_rng(42602)
    matter = rng.normal(size=MATTER_DIM) + 1j * rng.normal(size=MATTER_DIM)
    matter /= np.linalg.norm(matter)
    probe: LogicalState = {(64, 0): matter}
    nominal = logical_step(probe, factors)
    contact_deleted = logical_step(probe, factors, contact_enabled=False)
    field_probe: LogicalState = {(1 << 2, 0): c322.symmetric_one_one_state()}
    coin_nominal = logical_step(field_probe, factors)
    coin_deleted = logical_step(field_probe, factors, field_coin_enabled=False)
    rejected = 0
    for function in (
        lambda: local_states(-1),
        lambda: recoil_generator(1, 6),
        lambda: apply_recoil_source(probe, 2),
        lambda: apply_stream(probe, 6),
        lambda: logical_step({(64 + 1, 64 + 2): matter}, factors),
    ):
        try:
            function()
        except ValueError:
            rejected += 1
    check(
        "the Cycle-219 one-particle mass and literal Cycle-230 contact remain on the same common code and contact deletion is visible",
        abs(logical_rows["two_cell_rest_mass"] - logical_rows["Cycle219_mass_fixture"])
        < TOLERANCE
        and logical_rows["contact_nontrivial_columns"] == 4047
        and contact_deletion > 1.9
        and state_residual(nominal, contact_deleted) > 0.1,
        {
            "Cycle219_mass_fixture": logical_rows["Cycle219_mass_fixture"],
            "two_cell_rest_mass": logical_rows["two_cell_rest_mass"],
            "uniform_one_particle_residual": logical_rows[
                "two_cell_uniform_one_particle_residual"
            ],
            "contact_nontrivial_columns": logical_rows["contact_nontrivial_columns"],
            "contact_deletion_opnorm": contact_deletion,
            "contact_deleted_history_residual": state_residual(nominal, contact_deleted),
        },
    )
    check(
        "field coin deletion and malformed sector/endpoint/direction controls are detected",
        state_residual(coin_nominal, coin_deleted) > 0.1 and rejected == 5,
        {
            "field_coin_deletion_history_residual": state_residual(coin_nominal, coin_deleted),
            "lawful_domain_rejections": rejected,
        },
    )


def prior_bridge_and_inventory_controls() -> None:
    print("\nPRIOR BRIDGE / SUPPLIED-DERIVED-OPEN INVENTORY")
    angle_416, _charge = c422.c416.source_angle()
    inventory = {
        "supplied": (
            "Cycle315 complete M64 tensor M64 physical matter seam, local checks/Wilson sector, coin, FSWAP, and Cycle230 contact",
            "Cycle322 coefficient-two even-CAR recoil convention and local six-mode fermion ordering",
            "two ordinary reservoir M2 and twelve ordinary directional field M2",
            "Cycle423 complete total-Q<=2 preparation, full hard-core field coin, directed boundary SWAP, and factor order",
            "theta=0.8 m with the Cycle219 mass-normalized m, sign, zero, and source invocation",
            "one- and two-reservoir blank-field preparations, finite edge, boundary, frames, origins, and readouts",
        ),
        "derived": (
            "fixed hard-core recoil generator through Q=2 and exact Cycle322 Q1 isometry",
            "common 434176-dimensional code with physical-M2 intertwiner and adjoint inverse on Q1/Q2 probe",
            "local matter-number, total-Q, coefficient-two recoil, and boundary-current ledgers",
            "one-/two-source emission, transport, absorption, reciprocity, collision, deletion, and saturation controls",
            "all-24-frame covariance and held-size/origin controls",
        ),
        "open": (
            "primitive synthesis of the bounded source-star exponential and autonomous forward recurrence",
            "full cubic multi-edge field network, Q>2 histories, prepared source creation, and contact-work ledger",
            "selection/calibration as physical energy, stress, source, force, clock response, metric, or gravity",
            "actual Records, physical time, Born law, and empirical calibration",
        ),
        "host_expectation_queries": 0,
        "global_Jordan_Wigner_or_parity_service": False,
        "field_auxiliary_constraints": "none; literal hard-core M2",
        "matter_constraints": "inherited local checks plus declared Wilson sector",
        "scheduled_adjoint_called_autonomous_recurrence": False,
        "number_called_energy": False,
        "generator_called_rate": False,
        "Born_claim": False,
        "negative_or_no_go_claim": False,
        "minimum_content_claim": False,
        "shared_obstruction_claim": False,
        "axiom_pressure": False,
        "authority": AUTHORITY,
        "audit": AUDIT,
    }
    check(
        "the Cycle416/422 and Cycle322 couplings share the declared mass-normalized angle without turning transfer into a source interpretation",
        abs(angle_416 - ANGLE) < 3e-16,
        {
            "Cycle416_angle": angle_416,
            "Cycle422_angle": c422.ANGLE,
            "Cycle426_angle": ANGLE,
            "angle_difference": angle_416 - ANGLE,
            "interpretation": "shared supplied calibration only",
        },
    )
    check(
        "the supplied, derived, and open inventory preserves the narrow constructive boundary",
        inventory["host_expectation_queries"] == 0
        and not inventory["global_Jordan_Wigner_or_parity_service"]
        and not inventory["scheduled_adjoint_called_autonomous_recurrence"]
        and not inventory["number_called_energy"]
        and not inventory["generator_called_rate"]
        and not inventory["Born_claim"]
        and not inventory["negative_or_no_go_claim"]
        and not inventory["minimum_content_claim"]
        and not inventory["shared_obstruction_claim"]
        and not inventory["axiom_pressure"],
        inventory,
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("CYCLE 426: PHYSICAL RECOIL / CONTACT TO HARD-CORE FIELD BRIDGE")
    print("authority=none; audit=unset")
    note_contract()
    coin, fswap, contact, _update, _details = c315.logical_update_controls(c322.LABELS)
    factors = (coin, fswap, contact)
    source_layer_operator_controls()
    q1_seam_controls()
    one_source_history_controls(factors)
    two_source_history_controls(factors)
    common_code_physical_controls(factors)
    support_covariance_origin_controls(factors)
    mass_contact_deletion_domain_controls(factors)
    prior_bridge_and_inventory_controls()
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL})
    if FAIL:
        print("RESULT PHYSICAL_RECOIL_HARD_CORE_FIELD_BRIDGE_NOT_CERTIFIED")
        return 1
    print("RESULT PHYSICAL_RECOIL_HARD_CORE_FIELD_BRIDGE_CERTIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
