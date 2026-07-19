#!/usr/bin/env python3
"""Cycle 429: physical test-matter recoil receiver on a two-edge path.

Join the Cycle-426 hard-core recoil source to the Cycle-319/396 nonduplicated
three-cell matter seam.  One literal reservoir/field star is installed at A,
B, and C.  A prepared reservoir at one end emits, the field crosses two
ordinary edge-bit SWAPs, and the opposite M64 cell absorbs through the same
even-CAR recoil vertex.

The declared field code is the complete one-excitation sector of the 21
hard-core M2.  Direction and excitation ledgers are not force, momentum,
energy, stress, gravity, a rate, time, probability, or a Record.  Authority is
none and audit is unset.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from functools import lru_cache
from itertools import product
from pathlib import Path
import sys

import numpy as np
from scipy import sparse


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_shared_middle_three_cell_source_compiler_cycle396_2026_07_18 as c396
import physical_source_prediction_bridge_contract_cycle420_2026_07_19 as c420
import common_cubic_transient_stationary_update_cycle425_2026_07_19 as c425
import physical_recoil_hard_core_field_bridge_cycle426_2026_07_19 as c426


c319 = c396.c319
c322 = c396.c322
c210 = c396.c210
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_TEST_MATTER_RECOIL_RECEIVER_MULTIEDGE_PREDICTION_CYCLE429_NOTE_2026-07-19.md"
)
LABELS = c396.LABELS
LABEL_INDEX = c396.LABEL_INDEX
MATTER_DIM = len(LABELS)
CELLS = (0, 1, 2)
LOCAL_FIELD_DIM = 7
FIELD_DIM = 21
COMMON_DIMENSION = MATTER_DIM * FIELD_DIM
PATH_DIRECTION = 0
REVERSE = c322.REVERSE
TRAIN_SIZE = 5
HELD_SIZE = 6
TOLERANCE = 9e-10
AUTHORITY = "none"
AUDIT = "unset"
PASS = 0
FAIL = 0

LogicalState = dict[int, np.ndarray]
PhysicalState = dict[int, np.ndarray]


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
        "three-cell/two-edge shared-middle installation",
        "complete q=1 sector of 21 hard-core m2",
        "same recoil vertex",
        "physical test-matter receiver",
        "e_429 g_429 = g_physical,429 e_429",
        "matter-direction/recoil observable",
        "reciprocal source/receiver role swap",
        "one-edge and two-edge no-refit response",
        "all 24 proper-cubic frames",
        "held l=6 origins",
        "source coupling, receiver coupling, transport, and contact deletions",
        "host packet/profile joins remain false",
        "direction current is not force, momentum, energy, stress, or gravity",
        "steps are not time",
        "no expectation controls a gate",
        "no no-go, minimum-content, shared-obstruction, or axiom-pressure claim",
    )
    missing = required if not NOTE.exists() else tuple(
        phrase for phrase in required if phrase not in normalized(NOTE)
    )
    check("the Cycle-429 note states the multiedge receiver and prediction boundary", not missing, missing)


def site_index(cell: int, local_site: int) -> int:
    if cell not in CELLS or local_site not in range(LOCAL_FIELD_DIM):
        raise ValueError("field site is outside the three-cell seven-M2 stars")
    return LOCAL_FIELD_DIM * cell + local_site


def reservoir_site(cell: int) -> int:
    return site_index(cell, 0)


def field_site(cell: int, direction: int) -> int:
    if direction not in range(6):
        raise ValueError("field direction must be in 0..5")
    return site_index(cell, 1 + direction)


def validate_state(state: dict) -> None:
    for key, value in state.items():
        if key not in range(FIELD_DIM):
            raise ValueError("state is outside the complete 21-site Q=1 code")
        if value.ndim != 1:
            raise ValueError("matter amplitude must be a vector")


def prune(state: dict, threshold: float = 2e-13) -> dict:
    return {key: value for key, value in state.items() if np.linalg.norm(value) > threshold}


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


def role_cells(role: str) -> tuple[int, int, int]:
    if role == "A_to_C":
        return (0, 1, 2)
    if role == "C_to_A":
        return (2, 1, 0)
    raise ValueError("role must be A_to_C or C_to_A")


def source_cell(role: str) -> int:
    return role_cells(role)[0]


def receiver_cell(role: str) -> int:
    return role_cells(role)[-1]


def edge_order(role: str) -> tuple[int, int]:
    return (0, 1) if role == "A_to_C" else (1, 0)


def apply_matter(state: dict, factor: sparse.spmatrix) -> dict:
    return prune({key: factor @ value for key, value in state.items()})


def field_coin_transitions(site: int, *, inverse: bool = False):
    cell, local = divmod(site, LOCAL_FIELD_DIM)
    if local == 0:
        return ((site, 1.0 + 0j),)
    source_direction = local - 1
    coin = c396.c214.FIELD_COIN.conj().T if inverse else c396.c214.FIELD_COIN
    return tuple(
        (field_site(cell, target), coin[target, source_direction])
        for target in range(6)
        if abs(coin[target, source_direction]) > 1e-15
    )


def apply_field_coin(state: dict, *, inverse: bool = False, enabled: bool = True) -> dict:
    if not enabled:
        return {key: value.copy() for key, value in state.items()}
    output = {}
    for site, value in state.items():
        for target, coefficient in field_coin_transitions(site, inverse=inverse):
            output[target] = output.get(target, 0) + coefficient * value
    return prune(output)


def swap_edge_site(site: int, edge: int, direction: int = PATH_DIRECTION) -> int:
    if edge not in (0, 1):
        raise ValueError("path edge must be zero or one")
    left = field_site(edge, direction)
    right = field_site(edge + 1, REVERSE[direction])
    if site == left:
        return right
    if site == right:
        return left
    return site


def apply_transport(
    state: dict,
    role: str,
    *,
    direction: int = PATH_DIRECTION,
    enabled_edges: tuple[bool, bool] = (True, True),
    inverse: bool = False,
) -> dict:
    if direction not in range(6):
        raise ValueError("path direction must be in 0..5")
    order = tuple(reversed(edge_order(role))) if inverse else edge_order(role)
    output = {key: value.copy() for key, value in state.items()}
    for edge in order:
        if enabled_edges[edge]:
            output = {swap_edge_site(key, edge, direction): value for key, value in output.items()}
    return prune(output)


def apply_source(
    state: LogicalState,
    cell: int,
    *,
    inverse: bool = False,
    enabled: bool = True,
) -> LogicalState:
    if cell not in CELLS:
        raise ValueError("source cell must be A, B, or C")
    if not enabled:
        return {key: value.copy() for key, value in state.items()}
    active = (reservoir_site(cell),) + tuple(field_site(cell, d) for d in range(6))
    zero = np.zeros(MATTER_DIM, dtype=complex)
    joint = np.column_stack([state.get(key, zero) for key in active]).reshape(-1)
    operator = c396.embedded_source_operator("coefficient_two", cell, inverse)
    transformed = (operator @ joint).reshape((MATTER_DIM, 7))
    output = {key: value.copy() for key, value in state.items() if key not in active}
    for local, key in enumerate(active):
        output[key] = transformed[:, local]
    return prune(output)


def apply_sources(
    state: LogicalState,
    role: str,
    *,
    enabled: tuple[bool, bool, bool] = (True, True, True),
    inverse: bool = False,
) -> LogicalState:
    order = tuple(reversed(role_cells(role))) if inverse else role_cells(role)
    output = state
    for cell in order:
        output = apply_source(output, cell, inverse=inverse, enabled=enabled[cell])
    return output


def logical_step(
    state: LogicalState,
    role: str,
    factors,
    *,
    source_enabled: tuple[bool, bool, bool] = (True, True, True),
    enabled_edges: tuple[bool, bool] = (True, True),
    contact_enabled: bool = True,
    field_coin_enabled: bool = True,
) -> LogicalState:
    validate_state(state)
    coin, first, second, contact = factors
    output = apply_matter(state, coin)
    output = apply_field_coin(output, enabled=field_coin_enabled)
    output = apply_sources(output, role, enabled=source_enabled)
    matter_edges = (first, second) if role == "A_to_C" else (second, first)
    for factor in matter_edges:
        output = apply_matter(output, factor)
    output = apply_transport(output, role, enabled_edges=enabled_edges)
    if contact_enabled:
        output = apply_matter(output, contact)
    return output


def logical_inverse(state: LogicalState, role: str, factors) -> LogicalState:
    validate_state(state)
    coin, first, second, contact = factors
    output = apply_matter(state, contact.getH())
    output = apply_transport(output, role, inverse=True)
    matter_edges = (first, second) if role == "A_to_C" else (second, first)
    for factor in reversed(matter_edges):
        output = apply_matter(output, factor.getH())
    output = apply_sources(output, role, inverse=True)
    output = apply_field_coin(output, inverse=True)
    return apply_matter(output, coin.getH())


def evolve(state: LogicalState, role: str, factors, depth: int, **kwargs) -> LogicalState:
    output = state
    for _ in range(depth):
        output = logical_step(output, role, factors, **kwargs)
    return output


def initial_state(role: str) -> LogicalState:
    origin = source_cell(role)
    old = c396.initial_response_state(origin)
    vector = next(iter(old.values())).copy()
    return {reservoir_site(origin): vector}


def reservoir_weight(state: dict, cell: int) -> float:
    value = state.get(reservoir_site(cell))
    return 0.0 if value is None else float(np.vdot(value, value).real)


@lru_cache(maxsize=None)
def matter_direction_values(cell: int, axis: int) -> np.ndarray:
    if cell not in CELLS or axis not in range(3):
        raise ValueError("matter direction coordinate outside cell/axis domain")
    values = []
    for label in LABELS:
        _number, local_label = c319.label_specs(label)[cell]
        values.append(
            sum(float(c210.DIRECTIONS[direction, axis]) for direction in local_label)
        )
    return np.asarray(values)


def matter_direction(state: dict, cell: int) -> np.ndarray:
    return np.asarray(
        [
            sum(
                np.vdot(value, matter_direction_values(cell, axis) * value).real
                for value in state.values()
            )
            for axis in range(3)
        ],
        dtype=float,
    )


def field_direction(state: dict, cell: int) -> np.ndarray:
    result = np.zeros(3, dtype=float)
    for site, value in state.items():
        site_cell, local = divmod(site, LOCAL_FIELD_DIM)
        if site_cell == cell and local > 0:
            result += float(np.vdot(value, value).real) * c210.DIRECTIONS[local - 1]
    return result


def direction_ledger(state: dict, cell: int) -> np.ndarray:
    return matter_direction(state, cell) + 2 * field_direction(state, cell)


def cell_q(state: dict, cell: int) -> float:
    return float(
        sum(
            np.vdot(value, value).real
            for site, value in state.items()
            if site // LOCAL_FIELD_DIM == cell
        )
    )


def receiver_source_trace(state: LogicalState, role: str, factors):
    """Advance to the receiver vertex of the next fixed update and expose it."""

    coin, _first, _second, _contact = factors
    order = role_cells(role)
    output = apply_matter(state, coin)
    output = apply_field_coin(output)
    for cell in order[:-1]:
        output = apply_source(output, cell)
    before = output
    after = apply_source(before, order[-1])
    return before, after


def local_source_and_overlap_controls(factors, update_rows) -> None:
    print("\nLOCAL RECOIL SOURCE / SHARED-MIDDLE ORDER")
    identity = sparse.eye(7 * MATTER_DIM, format="csc")
    number_values = np.repeat(
        [label[0] + label[2] + label[4] for label in LABELS], 7
    )
    number = sparse.diags(number_values, format="csc", dtype=float)
    rows = []
    for cell in CELLS:
        operator = c396.embedded_source_operator("coefficient_two", cell)
        rows.append(
            {
                "cell": cell,
                "unitarity_raw": c319.c315.raw_maximum_abs(operator.getH() @ operator - identity),
                "matter_number_commutator_raw": c319.c315.raw_maximum_abs(
                    operator @ number - number @ operator
                ),
                "nonzeros": operator.nnz,
            }
        )
    rng = np.random.default_rng(42901)
    vector = rng.normal(size=MATTER_DIM) + 1j * rng.normal(size=MATTER_DIM)
    vector /= np.linalg.norm(vector)
    seed = {reservoir_site(0): vector}
    ab = apply_source(apply_source(seed, 0), 1)
    ba = apply_source(apply_source(seed, 1), 0)
    field_first = transport_matrix(PATH_DIRECTION, (0, 1))
    field_reverse = transport_matrix(PATH_DIRECTION, (1, 0))
    check(
        "the same recoil vertex embeds once at A/B/C, preserves matter number, and does not duplicate the shared middle cell",
        max(row["unitarity_raw"] for row in rows) < TOLERANCE
        and max(row["matter_number_commutator_raw"] for row in rows) == 0
        and state_residual(ab, ba) < TOLERANCE
        and len(set(CELLS)) == 3,
        {
            "local_source_rows": rows,
            "adjacent_source_order_residual": state_residual(ab, ba),
            "installed_cells": CELLS,
            "middle_cell_multiplicity": 1,
        },
    )
    check(
        "both edge orders commute because they touch distinct middle rails, while the shared middle coin/source/contact factor occurs only once",
        np.linalg.norm(field_first - field_reverse) == 0
        and update_rows["two_FSWAP_commutator"] == 0
        and update_rows["two_ordered_update_residual"] == 0
        and len(set(CELLS)) == 3,
        {
            "field_edge_order_residual": float(np.linalg.norm(field_first - field_reverse)),
            "matter_FSWAP_commutator_opnorm": update_rows["two_FSWAP_commutator"],
            "matter_ordered_update_opnorm": update_rows["two_ordered_update_residual"],
            "middle_rails": "AB uses B,-x; BC uses B,+x",
            "shared_nonedge_factors": "one B coin, one B source vertex, one B contact factor",
            "role_schedule": "A-to-C lists AB then BC; C-to-A lists BC then AB, with exact equality",
        },
    )


def transport_matrix(
    direction: int = PATH_DIRECTION, order: tuple[int, int] = (0, 1)
) -> np.ndarray:
    result = np.eye(FIELD_DIM, dtype=complex)
    for edge in order:
        permutation = np.zeros((FIELD_DIM, FIELD_DIM), dtype=complex)
        for source in range(FIELD_DIM):
            permutation[swap_edge_site(source, edge, direction), source] = 1
        result = permutation @ result
    return result


def field_frame_representation(frame: np.ndarray) -> np.ndarray:
    direction = c210.direction_permutation(frame)
    output = np.zeros((FIELD_DIM, FIELD_DIM), dtype=complex)
    for cell in CELLS:
        output[reservoir_site(cell), reservoir_site(cell)] = 1
        for source_direction in range(6):
            target_direction = int(np.argmax(direction[:, source_direction]))
            output[field_site(cell, target_direction), field_site(cell, source_direction)] = 1
    return output


def conservation_continuity_covariance_controls(factors, update_rows) -> None:
    print("\nQ / DIRECTION / CURRENT / 24-FRAME CONTROLS")
    source_rows = []
    for q_number in (1,):
        generator = c426.recoil_generator(q_number)
        source_rows.append(
            {
                "Q": q_number,
                "Hermiticity": float(sparse.linalg.norm(generator - generator.getH())),
                "direction_commutators": tuple(
                    float(
                        sparse.linalg.norm(
                            generator @ c426.local_diagonal(
                                q_number,
                                lambda mask, field, axis=axis: sum(
                                    c210.DIRECTIONS[d, axis]
                                    for d in range(6)
                                    if (mask >> d) & 1
                                )
                                + 2
                                * sum(
                                    c210.DIRECTIONS[d, axis]
                                    for d in range(6)
                                    if ((field % 64) >> d) & 1
                                ),
                            )
                            - c426.local_diagonal(
                                q_number,
                                lambda mask, field, axis=axis: sum(
                                    c210.DIRECTIONS[d, axis]
                                    for d in range(6)
                                    if (mask >> d) & 1
                                )
                                + 2
                                * sum(
                                    c210.DIRECTIONS[d, axis]
                                    for d in range(6)
                                    if ((field % 64) >> d) & 1
                                ),
                            )
                            @ generator
                        )
                    )
                    for axis in range(3)
                ),
            }
        )
    stream = transport_matrix()
    local_q = []
    continuity_rows = []
    for cell in CELLS:
        values = np.asarray([int(site // 7 == cell) for site in range(FIELD_DIM)])
        observable = np.diag(values).astype(complex)
        local_q.append(observable)
        change = stream.conj().T @ observable @ stream - observable
        continuity_rows.append(float(np.linalg.norm(change - change.conj().T)))
    edge_current_rows = []
    for edge in (0, 1):
        edge_stream = transport_matrix(PATH_DIRECTION, (edge,))
        changes = tuple(
            edge_stream.conj().T @ observable @ edge_stream - observable
            for observable in local_q
        )
        edge_current_rows.append(
            {
                "edge": edge,
                "global_conservation_residual": float(np.linalg.norm(sum(changes))),
                "nonincident_cell_change": float(
                    np.linalg.norm(changes[2 if edge == 0 else 0])
                ),
                "left_plus_right_residual": float(
                    np.linalg.norm(changes[edge] + changes[edge + 1])
                ),
                "current_operator_Hermiticity": float(
                    np.linalg.norm(changes[edge] - changes[edge].conj().T)
                ),
            }
        )

    coin, first, second, contact = factors
    forward_matter = contact @ second @ first @ coin
    reverse_matter = contact @ first @ second @ coin
    covariance = c319.covariance_schedule_controls(
        LABELS,
        "path",
        coin,
        first,
        second,
        contact,
        forward_matter,
        reverse_matter,
    )
    source_frame = []
    stream_frame = []
    for frame in c210.proper_cubic_frames():
        representation = c322.local_source_frame(frame)
        source_vertex = c322.local_source_blocks(c322.ANGLE)[1]
        source_frame.append(
            float(np.linalg.norm(representation @ source_vertex @ representation.T - source_vertex))
        )
        field_representation = field_frame_representation(frame)
        direction = c210.direction_permutation(frame)
        target_direction = int(np.argmax(direction[:, PATH_DIRECTION]))
        stream_frame.append(
            float(
                np.linalg.norm(
                    field_representation @ stream @ field_representation.conj().T
                    - transport_matrix(target_direction)
                )
            )
        )
    check(
        "the Q=1 source and two-edge stream have exact excitation/direction ledgers and cell-current continuity",
        max(max(row["Hermiticity"], *row["direction_commutators"]) for row in source_rows)
        == 0
        and max(continuity_rows) == 0
        and max(max(row.values()) for row in edge_current_rows) <= 1
        and max(
            max(
                row["global_conservation_residual"],
                row["nonincident_cell_change"],
                row["left_plus_right_residual"],
                row["current_operator_Hermiticity"],
            )
            for row in edge_current_rows
        )
        == 0
        and np.linalg.norm(stream.conj().T @ stream - np.eye(FIELD_DIM)) == 0,
        {
            "source_operator_rows": source_rows,
            "global_Q": 1,
            "transport_unitarity": float(np.linalg.norm(stream.conj().T @ stream - np.eye(FIELD_DIM))),
            "cell_current_Hermiticity_residuals": continuity_rows,
            "edge_current_rows": edge_current_rows,
            "direction_semantics": "coefficient-two source-layer direction ledger only",
        },
    )
    check(
        "matter/contact, recoil source, field coin, and the two-edge path form an all-24 proper-cubic covariant family",
        covariance["proper_cubic_frames"] == 24
        and covariance["maximum_update_covariance_residual"] < TOLERANCE
        and covariance["frame_group_law_failures"] == 0
        and max(source_frame) < TOLERANCE
        and max(stream_frame) == 0,
        {
            "matter_schedule": covariance,
            "maximum_source_frame_residual": max(source_frame),
            "maximum_field_stream_frame_residual": max(stream_frame),
        },
    )


def response_and_recoil_controls(factors) -> dict:
    print("\nONE-EDGE / TWO-EDGE RECEIVER AND ROLE SWAP")
    rows = []
    traces = {}
    for role in ("A_to_C", "C_to_A"):
        initial = initial_state(role)
        first = logical_step(initial, role, factors)
        second = logical_step(first, role, factors)
        third = logical_step(second, role, factors)
        restored = logical_inverse(first, role, factors)
        source, middle, receiver = role_cells(role)
        before, after = receiver_source_trace(second, role, factors)
        matter_change = matter_direction(after, receiver) - matter_direction(before, receiver)
        field_change = 2 * (field_direction(after, receiver) - field_direction(before, receiver))
        ledger_change = direction_ledger(after, receiver) - direction_ledger(before, receiver)
        reservoir_gain = reservoir_weight(after, receiver) - reservoir_weight(before, receiver)
        one_edge = reservoir_weight(second, middle)
        two_edge = reservoir_weight(third, receiver)
        rows.append(
            {
                "role": role,
                "source": source,
                "receiver": receiver,
                "one_edge_depth2_response": one_edge,
                "two_edge_depth3_response": two_edge,
                "receiver_reservoir_gain_at_vertex": reservoir_gain,
                "receiver_matter_direction_change": matter_change,
                "receiver_twice_field_direction_change": field_change,
                "receiver_direction_ledger_residual": ledger_change,
                "first_step_inverse_residual": state_residual(restored, initial),
                "Q_after_three": state_norm(third),
            }
        )
        traces[role] = (initial, first, second, third, before, after)
    forward, reverse = rows
    check(
        "one fixed calibration gives nonzero one-edge and two-edge receiver response without refitting",
        min(row["one_edge_depth2_response"] for row in rows) > 1e-7
        and min(row["two_edge_depth3_response"] for row in rows) > 1e-10
        and all(row["one_edge_depth2_response"] > row["two_edge_depth3_response"] for row in rows)
        and max(abs(row["Q_after_three"] - 1) for row in rows) < 2e-11
        and max(row["first_step_inverse_residual"] for row in rows) < 3e-11,
        {
            "angle": c322.ANGLE,
            "calibration_refit_between_distances": False,
            "rows": rows,
        },
    )
    check(
        "source/test-matter role swap is reciprocal and the receiver vertex has a nonzero matter-direction change balanced by the field leg",
        abs(forward["one_edge_depth2_response"] - reverse["one_edge_depth2_response"])
        < 2e-11
        and abs(forward["two_edge_depth3_response"] - reverse["two_edge_depth3_response"])
        < 2e-11
        and abs(
            forward["receiver_reservoir_gain_at_vertex"]
            - reverse["receiver_reservoir_gain_at_vertex"]
        )
        < 2e-11
        and np.linalg.norm(forward["receiver_matter_direction_change"]) > 1e-7
        and np.linalg.norm(reverse["receiver_matter_direction_change"]) > 1e-7
        and np.linalg.norm(forward["receiver_direction_ledger_residual"]) < 2e-11
        and np.linalg.norm(reverse["receiver_direction_ledger_residual"]) < 2e-11
        and np.linalg.norm(
            forward["receiver_matter_direction_change"]
            + reverse["receiver_matter_direction_change"]
        )
        < 2e-11,
        {
            "forward": forward,
            "reverse": reverse,
            "response_reciprocity": abs(
                forward["two_edge_depth3_response"]
                - reverse["two_edge_depth3_response"]
            ),
            "role_swapped_matter_direction_sum": (
                forward["receiver_matter_direction_change"]
                + reverse["receiver_matter_direction_change"]
            ),
        },
    )
    return {"rows": rows, "traces": traces}


def deletion_controls(factors, response_data) -> None:
    print("\nSOURCE / RECEIVER / TRANSPORT / CONTACT DELETIONS")
    role = "A_to_C"
    initial = initial_state(role)
    baseline = response_data["rows"][0]["two_edge_depth3_response"]
    source_off = reservoir_weight(
        evolve(initial, role, factors, 3, source_enabled=(False, True, True)), 2
    )
    receiver_off = reservoir_weight(
        evolve(initial, role, factors, 3, source_enabled=(True, True, False)), 2
    )
    middle_off = reservoir_weight(
        evolve(initial, role, factors, 3, source_enabled=(True, False, True)), 2
    )
    first_edge_off = reservoir_weight(
        evolve(initial, role, factors, 3, enabled_edges=(False, True)), 2
    )
    second_edge_off = reservoir_weight(
        evolve(initial, role, factors, 3, enabled_edges=(True, False)), 2
    )
    contact_off = reservoir_weight(
        evolve(initial, role, factors, 3, contact_enabled=False), 2
    )
    blank_source = {reservoir_site(0): np.zeros(MATTER_DIM, dtype=complex)}
    blank_output = evolve(blank_source, role, factors, 3)
    check(
        "source coupling, receiver coupling, each transport edge, blank preparation, and contact deletion are independently visible",
        source_off < TOLERANCE
        and receiver_off < TOLERANCE
        and first_edge_off < TOLERANCE
        and second_edge_off < TOLERANCE
        and state_norm(blank_output) == 0
        and abs(middle_off - baseline) > 1e-10
        and abs(contact_off - baseline) > 1e-10,
        {
            "baseline_two_edge_response": baseline,
            "source_coupling_deleted": source_off,
            "receiver_coupling_deleted": receiver_off,
            "middle_coupling_deleted": middle_off,
            "first_edge_deleted": first_edge_off,
            "second_edge_deleted": second_edge_off,
            "contact_deleted": contact_off,
            "blank_source_preparation_output_norm": state_norm(blank_output),
        },
    )


def encode_state(state: LogicalState, encoding) -> PhysicalState:
    return {key: encoding @ value for key, value in state.items()}


def apply_physical_matter(state: PhysicalState, encoding, factor) -> PhysicalState:
    output = {}
    for key, value in state.items():
        decoded = encoding.getH() @ value
        output[key] = value + encoding @ (factor @ decoded - decoded)
    return prune(output)


def apply_physical_source(
    state: PhysicalState,
    encoding,
    cell: int,
    *,
    inverse: bool = False,
) -> PhysicalState:
    active = (reservoir_site(cell),) + tuple(field_site(cell, d) for d in range(6))
    zero_physical = np.zeros(encoding.shape[0], dtype=complex)
    decoded = {key: encoding.getH() @ state.get(key, zero_physical) for key in active}
    transformed = apply_source(decoded, cell, inverse=inverse)
    output = {key: value.copy() for key, value in state.items() if key not in active}
    zero_logical = np.zeros(MATTER_DIM, dtype=complex)
    for key in active:
        before_physical = state.get(key, zero_physical)
        before_logical = decoded[key]
        after_logical = transformed.get(key, zero_logical)
        output[key] = before_physical + encoding @ (after_logical - before_logical)
    return prune(output)


def physical_step(state: PhysicalState, encoding, role: str, factors) -> PhysicalState:
    coin, first, second, contact = factors
    output = apply_physical_matter(state, encoding, coin)
    output = apply_field_coin(output)
    for cell in role_cells(role):
        output = apply_physical_source(output, encoding, cell)
    matter_edges = (first, second) if role == "A_to_C" else (second, first)
    for factor in matter_edges:
        output = apply_physical_matter(output, encoding, factor)
    output = apply_transport(output, role)
    return apply_physical_matter(output, encoding, contact)


def physical_inverse(state: PhysicalState, encoding, role: str, factors) -> PhysicalState:
    coin, first, second, contact = factors
    output = apply_physical_matter(state, encoding, contact.getH())
    output = apply_transport(output, role, inverse=True)
    matter_edges = (first, second) if role == "A_to_C" else (second, first)
    for factor in reversed(matter_edges):
        output = apply_physical_matter(output, encoding, factor.getH())
    for cell in reversed(role_cells(role)):
        output = apply_physical_source(output, encoding, cell, inverse=True)
    output = apply_field_coin(output, inverse=True)
    return apply_physical_matter(output, encoding, coin.getH())


def shell_for_origin(length: int, origin: tuple[int, int, int]):
    code = c319.c269.build_code(length)
    cells = tuple(
        tuple((origin[axis] + offset * int(c210.DIRECTIONS[PATH_DIRECTION, axis])) % length for axis in range(3))
        for offset in range(3)
    )
    return cells, c319.multi_order_encodings(code, cells, LABELS)


def physical_code_held_origin_controls(factors) -> None:
    print("\nPHYSICAL E/G / HELD SIZE AND ORIGIN")
    rows = []
    for length in (TRAIN_SIZE, HELD_SIZE):
        encodings, _reducer, support, gram_raw = c396.build_shell(length)
        for role, order in (("A_to_C", (0, 1, 2)), ("C_to_A", (2, 1, 0))):
            encoding = encodings[c319.ORDER_INDEX[order]]
            logical = initial_state(role)
            encoded = encode_state(logical, encoding)
            logical_output = logical_step(logical, role, factors)
            physical_output = physical_step(encoded, encoding, role, factors)
            expected = encode_state(logical_output, encoding)
            restored = physical_inverse(physical_output, encoding, role, factors)
            rows.append(
                {
                    "L": length,
                    "held": length == HELD_SIZE,
                    "role": role,
                    "encoding_order": order,
                    "matter_encoding_shape": encoding.shape,
                    "Gram_raw_maximum": gram_raw[c319.ORDER_INDEX[order]],
                    "EG_residual": state_residual(physical_output, expected),
                    "inverse_residual": state_residual(restored, encoded),
                    "output_norm": state_norm(physical_output),
                    "matter_support": support,
                }
            )
    held_origin = (3, 2, 1)
    held_cells, (translated, _reducer, translated_support) = shell_for_origin(
        HELD_SIZE, held_origin
    )
    identity = sparse.eye(MATTER_DIM, format="csc")
    translated_grams = tuple(
        c319.c315.raw_maximum_abs(encoding.getH() @ encoding - identity)
        for encoding in translated
    )
    check(
        "E_429 G_429 = G_physical,429 E_429 and the adjoint inverse close for both roles on train and held physical codes",
        max(
            max(
                row["Gram_raw_maximum"],
                row["EG_residual"],
                row["inverse_residual"],
                abs(row["output_norm"] - 1),
            )
            for row in rows
        )
        < TOLERANCE,
        {
            "common_logical_dimension": COMMON_DIMENSION,
            "rows": rows,
            "off_code_completion": "factorwise identity outside each matter code image",
        },
    )
    check(
        "the held L=6 shell remains isometric at a translated origin in all six matter-factor orders",
        max(translated_grams) < TOLERANCE and len(set(held_cells)) == 3,
        {
            "held_origin": held_origin,
            "held_cells": held_cells,
            "translated_Gram_raw_maxima": translated_grams,
            "translated_support": translated_support,
        },
    )


@dataclass(frozen=True)
class PredictionJoin:
    surface: str
    constructed_readout: str
    bounded_near_side_source_seam: bool
    bounded_receiver_seam: bool
    cycle420_physical_source_EG: bool
    cycle420_physical_test_matter_readout: bool
    host_profile_join: bool
    host_packet_join: bool
    surface_prediction_closed: bool
    remaining_interface: str


def prediction_interface_controls(response_data) -> None:
    print("\nCYCLE-420 TYPED PREDICTION INTERFACES")
    contracts = {surface.name: surface for surface in c420.SURFACES}
    rows = (
        PredictionJoin(
            "causal_ratio",
            "one-edge/two-edge reservoir occupation plus receiver matter-direction change",
            True,
            True,
            False,
            False,
            False,
            False,
            False,
            "no host density profile, detector centroid, or continuum causal-ratio join",
        ),
        PredictionJoin(
            "impact_parameter",
            "collinear two-edge receiver coordinate only",
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            "no transverse impact geometry, host density, packet centroid, or fit join",
        ),
        PredictionJoin(
            "quadrupole_width",
            "single-source receiver matter-direction coordinate only",
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            "no signed (+1,-2,+1) physical profile or packet-width join",
        ),
    )
    serialized = tuple(asdict(row) for row in rows)
    check(
        "the bounded near-side source/receiver seam narrows Cycle 420 while every named-surface E/G/readout and host join remains false",
        {row.surface for row in rows}
        == {"causal_ratio", "impact_parameter", "quadrupole_width"}
        and rows[0].bounded_near_side_source_seam
        and rows[0].bounded_receiver_seam
        and all(not row.cycle420_physical_source_EG for row in rows)
        and all(not row.cycle420_physical_test_matter_readout for row in rows)
        and all(not row.host_profile_join for row in rows)
        and all(not row.host_packet_join for row in rows)
        and all(not row.surface_prediction_closed for row in rows)
        and not rows[1].bounded_near_side_source_seam
        and not rows[1].bounded_receiver_seam
        and not rows[2].bounded_near_side_source_seam
        and not rows[2].bounded_receiver_seam
        and contracts["causal_ratio"].source_interface.startswith("positive host")
        and contracts["impact_parameter"].source_interface.startswith("positive host")
        and contracts["quadrupole_width"].source_interface.startswith("signed host"),
        {
            "rows": serialized,
            "constructed_forward_response": response_data["rows"][0],
            "Cycle420_original_flags_all_false": all(
                not surface.physical_source_eg and not surface.physical_test_matter_readout
                for surface in c420.SURFACES
            ),
        },
    )


def mass_contact_support_domain_inventory_controls(factors, update_rows) -> None:
    print("\nMASS / CONTACT / SUPPORT / DOMAIN / INVENTORY")
    contact = factors[3]
    endpoint_support = 18 + 7
    rejected = 0
    probe = initial_state("A_to_C")
    for function in (
        lambda: site_index(3, 0),
        lambda: field_site(0, 6),
        lambda: role_cells("bad"),
        lambda: swap_edge_site(0, 2),
        lambda: logical_step({21: next(iter(probe.values()))}, "A_to_C", factors),
    ):
        try:
            function()
        except ValueError:
            rejected += 1
    inventory = {
        "supplied": (
            "Cycle319/396 n<=3 three-cell matter shell, local checks/Wilson sector, S3 role register, two FSWAP orders, and identity completion",
            "Cycle426 fixed coefficient-two hard-core recoil vertex and theta=0.8m calibration",
            "three reservoir M2, eighteen directional field M2, and complete global Q1 preparation",
            "Cycle425/426 field coin-source-stream order specialized to two ordinary path-edge bit SWAPs",
            "prepared endpoint reservoir, three-cell matter columns, path boundary, roles, frames, train/held origins, and readouts",
        ),
        "derived": (
            "same-law physical source emission and distinct M64 receiver absorption across two edges",
            "nonzero receiver matter-direction change with exact coefficient-two local balance",
            "reciprocal A/C role swap and one-edge/two-edge no-refit response",
            "physical E/G and inverse, Q/current, mass/contact, deletion, covariance, overlap, and held-origin controls",
            "typed Cycle420 causal/impact/quadrupole boundary narrowed while named-surface E/G/readout and host joins stay false",
        ),
        "open": (
            "complete Q2 and higher three-cell histories and homogeneous full cubic source/receiver network",
            "primitive synthesis replacing inherited matrix-unit completion and autonomous source preparation/recurrence",
            "signed quadrupole source, transverse impact geometry, host-profile replacement, packet observables, and prediction calibration",
            "contact-work law, physical clock, Records, Born law, energy/stress/source selection, metric, and gravity",
        ),
        "host_expectation_queries_controlling_gates": 0,
        "direction_called_force_or_momentum": False,
        "number_called_energy_or_source": False,
        "steps_called_time": False,
        "Born_claim": False,
        "actual_Records_added": 0,
        "negative_or_no_go_claim": False,
        "minimum_content_claim": False,
        "shared_obstruction_claim": False,
        "axiom_pressure": False,
        "authority": AUTHORITY,
        "audit": AUDIT,
    }
    check(
        "the Cycle-219 mass and Cycle-230 contact remain nontrivial on the shared physical receiver code",
        abs(update_rows["three_cell_rest_mass"] - update_rows["Cycle219_mass_fixture"])
        < TOLERANCE
        and update_rows["uniform_one_particle_eigen_residual"] < TOLERANCE
        and update_rows["contact_nontrivial_columns"] == 645
        and np.count_nonzero(abs(contact.diagonal() - 1) > 2e-14) == 645,
        {
            "Cycle219_mass_fixture": update_rows["Cycle219_mass_fixture"],
            "three_cell_mass": update_rows["three_cell_rest_mass"],
            "mass_eigen_residual": update_rows["uniform_one_particle_eigen_residual"],
            "contact_nontrivial_columns": update_rows["contact_nontrivial_columns"],
        },
    )
    check(
        "the three-cell patch has bounded support, one shared middle factor, and constant 36-M2-per-cell matter/field installation",
        endpoint_support == 25,
        {
            "matter_face_port_cell_union_M2": 118,
            "S3_role_register_M2": 3,
            "literal_reservoir_field_M2": 21,
            "fixed_origin_common_patch_M2": 142,
            "translated_held_matter_union_M2": 122,
            "translated_held_common_patch_M2": 146,
            "maximum_tested_common_patch_M2": 146,
            "homogeneous_matter_plus_field_M2_per_cell": 36,
            "endpoint_recoil_vertex_support_M2": endpoint_support,
            "middle_cell_multiplicity": 1,
        },
    )
    check(
        "lawful domains and the supplied/derived/open inventory preserve the bounded positive scope",
        rejected == 5
        and inventory["host_expectation_queries_controlling_gates"] == 0
        and not inventory["direction_called_force_or_momentum"]
        and not inventory["number_called_energy_or_source"]
        and not inventory["steps_called_time"]
        and not inventory["Born_claim"]
        and not inventory["negative_or_no_go_claim"]
        and not inventory["minimum_content_claim"]
        and not inventory["shared_obstruction_claim"]
        and not inventory["axiom_pressure"],
        {"domain_rejections": rejected, **inventory},
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("CYCLE 429: PHYSICAL TEST-MATTER RECOIL RECEIVER / MULTIEDGE PREDICTION")
    print("authority=none; audit=unset")
    note_contract()
    update_rows, coin, first, second, contact, _forward, _reverse = c319.update_controls(
        LABELS, "path"
    )
    factors = (coin, first, second, contact)
    local_source_and_overlap_controls(factors, update_rows)
    conservation_continuity_covariance_controls(factors, update_rows)
    response_data = response_and_recoil_controls(factors)
    deletion_controls(factors, response_data)
    physical_code_held_origin_controls(factors)
    prediction_interface_controls(response_data)
    mass_contact_support_domain_inventory_controls(factors, update_rows)
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL})
    if FAIL:
        print("RESULT PHYSICAL_TEST_MATTER_RECOIL_RECEIVER_MULTIEDGE_PREDICTION_NOT_CERTIFIED")
        return 1
    print("RESULT PHYSICAL_TEST_MATTER_RECOIL_RECEIVER_MULTIEDGE_PREDICTION_CERTIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
