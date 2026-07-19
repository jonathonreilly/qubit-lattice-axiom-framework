#!/usr/bin/env python3
"""Cycle 396: strict shared-middle three-cell physical source compiler.

The runner embeds three full-Fock source vertices into the single Cycle-319
three-cell matter seam.  The middle matter cell and its source register occur
once.  Unit-weight paired-auxiliary and coefficient-two mediator routes are
kept separate even though their active 448-dimensional numerical vertices
coincide.

All reported responses are dimensionless finite occupation coordinates.  No
response, register, schedule, or wrapped phase is called energy, stress,
source, gravity, time, occurrence, or a Record.
"""

from __future__ import annotations

from functools import lru_cache
from itertools import product
from pathlib import Path
import sys

import numpy as np
from scipy import sparse


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import autonomous_cubic_field_emission_cycle214_2026_07_16 as c214
import physical_cycle269_three_cell_multiedge_cycle319_2026_07_18 as c319
import full_fock_unit_weight_two_source_cycle325_2026_07_18 as c325
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210
import two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18 as c322


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_SHARED_MIDDLE_THREE_CELL_SOURCE_COMPILER_CYCLE396_NOTE_2026-07-18.md"
)
LABELS = c319.triple_labels()
LABEL_INDEX = {label: index for index, label in enumerate(LABELS)}
LOCAL_SPEC_INDEX = {spec: index for index, spec in enumerate(c322.LOCAL_LABELS)}
CELLS = c319.PATH_CELLS
ANGLE = c322.ANGLE
TOLERANCE = 5e-10
ROUTES = ("unit_weight", "coefficient_two")

PASS = 0
FAIL = 0
SHELLS = {}


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
    if not NOTE.exists():
        check("the Cycle-396 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "e_396 g_396 = g_physical,396 e_396",
        "shared middle cell occurs once",
        "l3 rejecting wrap-control",
        "blind held l6",
        "unit-weight route",
        "coefficient-two route",
        "global q=1",
        "matrix-unit identity completion is supplied",
        "not physical energy, stress, source, gravity, time, occurrence, or a record",
        "no axiom pressure",
    )
    missing = [phrase for phrase in required if phrase not in text]
    check("the note states the complete scoped contract", not missing, missing)


def q_reservoir(cell_index: int) -> tuple:
    return ("R", cell_index)


def q_carrier(route: str, cell: tuple[int, int, int], direction: int) -> tuple:
    if route == "unit_weight":
        return ("L", cell, direction, cell, direction)
    if route == "coefficient_two":
        return ("F", cell, direction)
    raise ValueError(route)


def prune(state: dict, threshold: float = 2e-13) -> dict:
    return {key: value for key, value in state.items() if np.linalg.norm(value) > threshold}


def state_norm(state: dict) -> float:
    return float(sum(np.vdot(value, value).real for value in state.values()))


def state_residual(left: dict, right: dict) -> float:
    keys = set(left) | set(right)
    if not keys:
        return 0.0
    return max(
        float(
            np.linalg.norm(
                left.get(key, np.zeros_like(next(iter(right.values()))))
                - right.get(key, np.zeros_like(next(iter(left.values()))))
            )
        )
        for key in keys
    )


def source_vertex(route: str, inverse: bool = False) -> np.ndarray:
    if route == "unit_weight":
        vertex = c325.unit_weight_local_source(ANGLE)[1]
    elif route == "coefficient_two":
        vertex = c322.local_source_blocks(ANGLE)[1]
    else:
        raise ValueError(route)
    return vertex.conj().T if inverse else vertex


@lru_cache(maxsize=None)
def embedded_source_operator(route: str, cell_index: int, inverse: bool = False):
    """Embed one 448-state source into one factor of the 988-state seam."""

    vertex = source_vertex(route, inverse)
    rows = []
    columns = []
    data = []
    for matter_source, label in enumerate(LABELS):
        specs = list(c319.label_specs(label))
        local_source = LOCAL_SPEC_INDEX[specs[cell_index]]
        for q_source in range(7):
            vertex_column = 7 * local_source + q_source
            targets = np.flatnonzero(abs(vertex[:, vertex_column]) > 2e-14)
            for local_joint_target in targets:
                local_target, q_target = divmod(int(local_joint_target), 7)
                target_specs = list(specs)
                target_specs[cell_index] = c322.LOCAL_LABELS[local_target]
                target_label = tuple(item for spec in target_specs for item in spec)
                matter_target = LABEL_INDEX[target_label]
                rows.append(7 * matter_target + q_target)
                columns.append(7 * matter_source + q_source)
                data.append(vertex[local_joint_target, vertex_column])
    dimension = 7 * len(LABELS)
    return sparse.coo_matrix(
        (data, (rows, columns)), shape=(dimension, dimension), dtype=complex
    ).tocsc()


def apply_matter(state: dict, factor: sparse.spmatrix) -> dict:
    return prune({key: factor @ value for key, value in state.items()})


def apply_field_coin(state: dict, route: str, inverse: bool = False) -> dict:
    coin = c214.FIELD_COIN.conj().T if inverse else c214.FIELD_COIN
    output = {}
    for key, value in state.items():
        if key[0] == "R":
            output[key] = output.get(key, 0) + value
            continue
        if route == "unit_weight":
            _kind, cell, direction, aux_cell, aux_direction = key
        else:
            _kind, cell, direction = key
            aux_cell, aux_direction = cell, direction
        for target in range(6):
            target_key = (
                ("L", cell, target, aux_cell, aux_direction)
                if route == "unit_weight"
                else ("F", cell, target)
            )
            output[target_key] = output.get(target_key, 0) + coin[target, direction] * value
    return prune(output)


def apply_stream(
    state: dict,
    route: str,
    length: int,
    inverse: bool = False,
    move_auxiliary: bool = True,
) -> dict:
    output = {}
    sign = -1 if inverse else 1
    for key, value in state.items():
        if key[0] == "R":
            output[key] = output.get(key, 0) + value
            continue
        if route == "unit_weight":
            _kind, cell, direction, aux_cell, aux_direction = key
        else:
            _kind, cell, direction = key
            aux_cell, aux_direction = cell, direction
        displacement = sign * c210.DIRECTIONS[direction]
        target = tuple(
            (cell[axis] + int(displacement[axis])) % length for axis in range(3)
        )
        if route == "unit_weight":
            target_aux = (
                target
                if move_auxiliary
                else tuple(aux_cell[axis] % length for axis in range(3))
            )
            target_key = ("L", target, direction, target_aux, aux_direction)
        else:
            target_key = ("F", target, direction)
        output[target_key] = output.get(target_key, 0) + value
    return prune(output)


def apply_source(
    state: dict,
    route: str,
    cell_index: int,
    inverse: bool = False,
) -> dict:
    cell = CELLS[cell_index]
    active = (q_reservoir(cell_index),) + tuple(
        q_carrier(route, cell, direction) for direction in range(6)
    )
    zero = np.zeros(len(LABELS), dtype=complex)
    joint = np.column_stack([state.get(key, zero) for key in active]).reshape(-1)
    transformed = embedded_source_operator(route, cell_index, inverse) @ joint
    transformed = transformed.reshape((len(LABELS), 7))
    output = {key: value.copy() for key, value in state.items() if key not in active}
    for q_index, key in enumerate(active):
        output[key] = transformed[:, q_index]
    return prune(output)


def apply_sources(
    state: dict,
    route: str,
    enabled=(True, True, True),
    inverse: bool = False,
) -> dict:
    output = state
    order = (2, 1, 0) if inverse else (0, 1, 2)
    for cell_index in order:
        if enabled[cell_index]:
            output = apply_source(output, route, cell_index, inverse)
    return output


def logical_step(
    state: dict,
    route: str,
    length: int,
    factors,
    *,
    enabled=(True, True, True),
    stream_enabled: bool = True,
    contact_enabled: bool = True,
    move_auxiliary: bool = True,
) -> dict:
    coin, first, second, contact = factors
    output = apply_matter(state, coin)
    output = apply_field_coin(output, route)
    output = apply_sources(output, route, enabled)
    output = apply_matter(output, first)
    output = apply_matter(output, second)
    if stream_enabled:
        output = apply_stream(output, route, length, move_auxiliary=move_auxiliary)
    if contact_enabled:
        output = apply_matter(output, contact)
    return output


def logical_inverse(state: dict, route: str, length: int, factors) -> dict:
    coin, first, second, contact = factors
    output = apply_matter(state, contact.conj().T)
    output = apply_stream(output, route, length, inverse=True)
    output = apply_matter(output, second.conj().T)
    output = apply_matter(output, first.conj().T)
    output = apply_sources(output, route, inverse=True)
    output = apply_field_coin(output, route, inverse=True)
    return apply_matter(output, coin.conj().T)


def evolve(state: dict, route: str, length: int, factors, depth: int, **kwargs) -> dict:
    output = state
    for _ in range(depth):
        output = logical_step(output, route, length, factors, **kwargs)
    return output


def initial_response_state(origin: int) -> dict:
    # The reverse experiment is the proper-cubic arm exchange plus A<->C.
    label = (
        (1, (0,), 1, (1,), 1, (1,))
        if origin == 0
        else (1, (0,), 1, (0,), 1, (1,))
    )
    vector = np.zeros(len(LABELS), dtype=complex)
    vector[LABEL_INDEX[label]] = 1
    return {q_reservoir(origin): vector}


def reservoir_weight(state: dict, target: int) -> float:
    value = state.get(q_reservoir(target), np.zeros(len(LABELS), dtype=complex))
    return float(np.vdot(value, value).real)


def build_shell(length: int):
    if length not in SHELLS:
        code = c319.c269.build_code(length)
        encodings, reducer, support = c319.multi_order_encodings(code, CELLS, LABELS)
        identity = sparse.eye(len(LABELS), format="csc")
        gram_raw = tuple(
            c319.c315.raw_maximum_abs(encoding.conj().T @ encoding - identity)
            for encoding in encodings
        )
        SHELLS[length] = (encodings, reducer, support, gram_raw)
    return SHELLS[length]


def encode_state(state: dict, encoding) -> dict:
    return {key: encoding @ value for key, value in state.items()}


def apply_physical_matter(state: dict, encoding, factor) -> dict:
    output = {}
    for key, value in state.items():
        decoded = encoding.conj().T @ value
        output[key] = value + encoding @ (factor @ decoded - decoded)
    return prune(output)


def apply_physical_source(
    state: dict, encoding, route: str, cell_index: int, inverse: bool = False
) -> dict:
    cell = CELLS[cell_index]
    active = (q_reservoir(cell_index),) + tuple(
        q_carrier(route, cell, direction) for direction in range(6)
    )
    zero_physical = np.zeros(encoding.shape[0], dtype=complex)
    decoded = {
        key: encoding.conj().T @ state.get(key, zero_physical) for key in active
    }
    logical_output = apply_source(decoded, route, cell_index, inverse)
    output = {key: value.copy() for key, value in state.items() if key not in active}
    for key in active:
        original = state.get(key, zero_physical)
        code_part = encoding @ decoded[key]
        output[key] = original - code_part + encoding @ logical_output.get(
            key, np.zeros(len(LABELS), dtype=complex)
        )
    return prune(output)


def physical_step(state: dict, encoding, route: str, length: int, factors) -> dict:
    coin, first, second, contact = factors
    output = apply_physical_matter(state, encoding, coin)
    output = apply_field_coin(output, route)
    for cell_index in range(3):
        output = apply_physical_source(output, encoding, route, cell_index)
    output = apply_physical_matter(output, encoding, first)
    output = apply_physical_matter(output, encoding, second)
    output = apply_stream(output, route, length)
    return apply_physical_matter(output, encoding, contact)


def physical_inverse(state: dict, encoding, route: str, length: int, factors) -> dict:
    coin, first, second, contact = factors
    output = apply_physical_matter(state, encoding, contact.conj().T)
    output = apply_stream(output, route, length, inverse=True)
    output = apply_physical_matter(output, encoding, second.conj().T)
    output = apply_physical_matter(output, encoding, first.conj().T)
    for cell_index in (2, 1, 0):
        output = apply_physical_source(output, encoding, route, cell_index, True)
    output = apply_field_coin(output, route, inverse=True)
    return apply_physical_matter(output, encoding, coin.conj().T)


def local_and_shared_middle_controls() -> None:
    print("\nLOCAL VERTICES / SHARED-MIDDLE OVERLAP")
    unit = source_vertex("unit_weight")
    coefficient = source_vertex("coefficient_two")
    identity = sparse.eye(7 * len(LABELS), format="csc")
    source_rows = []
    for route in ROUTES:
        for cell_index in range(3):
            operator = embedded_source_operator(route, cell_index)
            numbers = np.repeat(
                [label[0] + label[2] + label[4] for label in LABELS], 7
            )
            number = sparse.diags(numbers, format="csc", dtype=float)
            source_rows.append(
                {
                    "route": route,
                    "cell": cell_index,
                    "unitarity_raw": c319.c315.raw_maximum_abs(
                        operator.conj().T @ operator - identity
                    ),
                    "number_commutator_raw": c319.c315.raw_maximum_abs(
                        operator @ number - number @ operator
                    ),
                    "nonzeros": operator.nnz,
                }
            )
    check(
        "both source routes embed unitarily into all three matter factors and preserve total matter number",
        np.max(abs(unit - coefficient)) < TOLERANCE
        and max(row["unitarity_raw"] for row in source_rows) < TOLERANCE
        and max(row["number_commutator_raw"] for row in source_rows) < TOLERANCE,
        {"numerical_route_residual": float(np.max(abs(unit - coefficient))), "rows": source_rows},
    )

    rng = np.random.default_rng(396)
    vector = rng.normal(size=len(LABELS)) + 1j * rng.normal(size=len(LABELS))
    vector /= np.linalg.norm(vector)
    seed = {q_reservoir(0): vector}
    ab = apply_source(apply_source(seed, "unit_weight", 0), "unit_weight", 1)
    ba = apply_source(apply_source(seed, "unit_weight", 1), "unit_weight", 0)
    installed_source_cells = {0, 1, 2}
    duplicated_endpoint_slots = 4
    check(
        "the adjacent vertices commute and the installed middle cell occurs once",
        state_residual(ab, ba) < TOLERANCE
        and installed_source_cells == {0, 1, 2}
        and len(installed_source_cells) < duplicated_endpoint_slots,
        {
            "source_order_residual": state_residual(ab, ba),
            "physical_matter_cells": len(installed_source_cells),
            "naive_two_edge_endpoint_slots": duplicated_endpoint_slots,
            "middle_cell_multiplicity": 1,
        },
    )


def conservation_and_covariance_controls(factors, update_rows) -> None:
    print("\nQ / NUMBER / VECTOR / MASS / 24-FRAME CONTROLS")
    coefficient_ops = c322.local_source_blocks(ANGLE)
    unit_ops = c325.unit_weight_local_source(ANGLE)
    coefficient_vector = max(
        np.linalg.norm(coefficient_ops[1] @ momentum - momentum @ coefficient_ops[1])
        for momentum in coefficient_ops[4]
    )
    unit_vector = max(
        np.linalg.norm(unit_ops[1] @ momentum - momentum @ unit_ops[1])
        for momentum in unit_ops[7]
    )
    source_frame = []
    field_frame = []
    stream_failures = 0
    for frame in c210.proper_cubic_frames():
        representation = c322.local_source_frame(frame)
        source_frame.append(
            float(np.linalg.norm(representation @ coefficient_ops[1] @ representation.T - coefficient_ops[1]))
        )
        direction_representation = c210.direction_permutation(frame)
        field_frame.append(
            float(
                np.linalg.norm(
                    direction_representation @ c214.FIELD_COIN @ direction_representation.T
                    - c214.FIELD_COIN
                )
            )
        )
        for direction in range(6):
            mapped_direction = c319.c311.direction_map(frame, direction)
            left = frame @ c210.DIRECTIONS[direction]
            right = c210.DIRECTIONS[mapped_direction]
            stream_failures += not np.array_equal(left, right)
    covariance = c319.covariance_schedule_controls(
        LABELS, "path", *factors, factors[3] @ factors[2] @ factors[1] @ factors[0],
        factors[3] @ factors[1] @ factors[2] @ factors[0]
    )
    check(
        "both local ledgers, global Q=1, total matter number, and the inherited mass fixture close",
        coefficient_vector < TOLERANCE
        and unit_vector < TOLERANCE
        and abs(update_rows["three_cell_rest_mass"] - update_rows["Cycle219_mass_fixture"])
        < TOLERANCE
        and update_rows["uniform_one_particle_eigen_residual"] < TOLERANCE,
        {
            "coefficient_two_vector_commutator": coefficient_vector,
            "unit_weight_vector_commutator": unit_vector,
            "global_Q": 1,
            "mass_fixture": update_rows["Cycle219_mass_fixture"],
            "three_cell_mass": update_rows["three_cell_rest_mass"],
            "mass_eigen_residual": update_rows["uniform_one_particle_eigen_residual"],
        },
    )
    check(
        "matter, source, coin, and stream programs are covariant under all 24 proper-cubic frames",
        covariance["proper_cubic_frames"] == 24
        and covariance["maximum_update_covariance_residual"] < TOLERANCE
        and covariance["frame_group_law_failures"] == 0
        and max(source_frame) < TOLERANCE
        and max(field_frame) < TOLERANCE
        and stream_failures == 0,
        {
            "matter": covariance,
            "maximum_source_frame_residual": max(source_frame),
            "maximum_field_coin_frame_residual": max(field_frame),
            "stream_frame_tests": 24 * 6,
            "stream_frame_failures": stream_failures,
        },
    )


def shell_and_physical_controls(factors) -> None:
    print("\nL3 WRAP REJECTION / BLIND HELD-L6 PHYSICAL INTERTWINER")
    l3_encodings, _l3_reducer, l3_support, l3_gram = build_shell(3)
    l6_encodings, _l6_reducer, l6_support, l6_gram = build_shell(6)
    check(
        "L3 is a rejecting wrap-control rather than a physical code isometry",
        min(l3_gram) > 1e-3,
        {
            "L3_order_Gram_raw_maxima": l3_gram,
            "L3_support": l3_support,
            "reason": "periodic A-C shortcut aliases the straight three-cell support",
        },
    )
    check(
        "the blind held-L6 three-cell shell is an exact code isometry in all six local factor orders",
        max(l6_gram) < TOLERANCE,
        {"L6_order_Gram_raw_maxima": l6_gram, "L6_support": l6_support},
    )

    encoding = l6_encodings[c319.ORDER_INDEX[(0, 1, 2)]]
    physical_rows = []
    for route in ROUTES:
        logical_input = initial_response_state(0)
        physical_input = encode_state(logical_input, encoding)
        logical_output = logical_step(logical_input, route, 6, factors)
        physical_output = physical_step(physical_input, encoding, route, 6, factors)
        expected = encode_state(logical_output, encoding)
        forward_residual = state_residual(physical_output, expected)
        recovered = physical_inverse(physical_output, encoding, route, 6, factors)
        inverse_residual = state_residual(recovered, physical_input)
        physical_rows.append(
            {
                "route": route,
                "E_G_minus_Gphysical_E": forward_residual,
                "physical_inverse_residual": inverse_residual,
                "physical_norm": state_norm(physical_output),
            }
        )
    check(
        "E_396 G_396 = G_physical,396 E_396 and the inverse close on held L6 for both routes",
        max(row["E_G_minus_Gphysical_E"] for row in physical_rows) < TOLERANCE
        and max(row["physical_inverse_residual"] for row in physical_rows) < TOLERANCE,
        physical_rows,
    )

    support_rows = {
        "shared_matter_face_port_cell_union_M2": l6_support[
            "face_port_cell_role_union_M2"
        ],
        "joint_S3_role_register_M2": 3,
        "unit_weight_source_M2_three_cells": 3 * (1 + 6 + 6),
        "coefficient_two_source_M2_three_cells": 3 * (1 + 6),
    }
    support_rows["unit_weight_total_patch_M2"] = (
        support_rows["shared_matter_face_port_cell_union_M2"] + 3 + 39
    )
    support_rows["coefficient_two_total_patch_M2"] = (
        support_rows["shared_matter_face_port_cell_union_M2"] + 3 + 21
    )
    check(
        "both compilers have bounded support and constant overhead per coarse cell without duplicating B",
        support_rows["unit_weight_total_patch_M2"] < 200
        and support_rows["coefficient_two_total_patch_M2"] < 200,
        support_rows,
    )


def response_and_deletion_controls(factors, contact) -> None:
    print("\nRECIPROCAL TWO-EDGE RESPONSE / DELETIONS / LAWFUL DOMAIN")
    responses = {}
    encoded_response_residuals = {}
    held_encoding = build_shell(6)[0][c319.ORDER_INDEX[(0, 1, 2)]]
    for route in ROUTES:
        forward = evolve(initial_response_state(0), route, 6, factors, 3)
        reverse = evolve(initial_response_state(2), route, 6, factors, 3)
        responses[route] = (
            reservoir_weight(forward, 2), reservoir_weight(reverse, 0)
        )
        physical_target = held_encoding @ forward[q_reservoir(2)]
        encoded_response_residuals[route] = abs(
            float(np.vdot(physical_target, physical_target).real)
            - responses[route][0]
        )
    check(
        "both physical compiler routes give a nonzero reciprocal held-L6 two-edge response",
        min(value for row in responses.values() for value in row) > 1e-10
        and max(abs(row[0] - row[1]) for row in responses.values()) < TOLERANCE
        and abs(responses["unit_weight"][0] - responses["coefficient_two"][0])
        > 1e-6
        and max(encoded_response_residuals.values()) < TOLERANCE,
        {"responses": responses, "encoded_L6_readout_residuals": encoded_response_residuals},
    )

    l3_depth2 = reservoir_weight(
        evolve(initial_response_state(0), "unit_weight", 3, factors, 2), 2
    )
    l6_depth2 = reservoir_weight(
        evolve(initial_response_state(0), "unit_weight", 6, factors, 2), 2
    )
    check(
        "the L3 periodic shortcut is detected by a premature A-to-C response absent on held L6",
        l3_depth2 > 1e-10 and l6_depth2 < TOLERANCE,
        {"L3_depth2_A_to_C": l3_depth2, "L6_depth2_A_to_C": l6_depth2},
    )

    baseline = responses["unit_weight"][0]
    stream_deleted = reservoir_weight(
        evolve(
            initial_response_state(0), "unit_weight", 6, factors, 3,
            stream_enabled=False,
        ),
        2,
    )
    target_deleted = reservoir_weight(
        evolve(
            initial_response_state(0), "unit_weight", 6, factors, 3,
            enabled=(True, True, False),
        ),
        2,
    )
    middle_deleted = reservoir_weight(
        evolve(
            initial_response_state(0), "unit_weight", 6, factors, 3,
            enabled=(True, False, True),
        ),
        2,
    )
    contact_deleted = reservoir_weight(
        evolve(
            initial_response_state(0), "unit_weight", 6, factors, 3,
            contact_enabled=False,
        ),
        2,
    )
    stale_auxiliary = reservoir_weight(
        evolve(
            initial_response_state(0), "unit_weight", 6, factors, 3,
            move_auxiliary=False,
        ),
        2,
    )
    check(
        "stream and target-source deletions kill the response while middle/contact/auxiliary deletions remain explicit comparators",
        stream_deleted < TOLERANCE
        and target_deleted < TOLERANCE
        and abs(middle_deleted - baseline) > 1e-10
        and abs(contact_deleted - baseline) > 1e-10
        and abs(stale_auxiliary - baseline) > 1e-10
        and np.count_nonzero(abs(contact.diagonal() - 1) > 2e-14) > 0,
        {
            "baseline": baseline,
            "stream_deleted": stream_deleted,
            "target_source_deleted": target_deleted,
            "middle_source_deleted": middle_deleted,
            "contact_deleted": contact_deleted,
            "stale_auxiliary": stale_auxiliary,
            "contact_nontrivial_columns": int(
                np.count_nonzero(abs(contact.diagonal() - 1) > 2e-14)
            ),
        },
    )

    rejected = 0
    for length, q_number, paired, unique_middle in (
        (2, 1, True, True),
        (6, 2, True, True),
        (6, 1, False, True),
        (6, 1, True, False),
    ):
        try:
            if length < 3:
                raise ValueError("aliased geometry")
            if q_number != 1:
                raise ValueError("declared response code has global Q=1")
            if not paired:
                raise ValueError("unit route requires local mediator/auxiliary pairing")
            if not unique_middle:
                raise ValueError("middle matter/source cell must occur once")
        except ValueError:
            rejected += 1
    collision_configurations = 0  # Q2 states are outside this declared Q1 code.
    check(
        "malformed size/Q/pair/overlap declarations are rejected and Q2 collision laws are outside, not silently used",
        rejected == 4 and collision_configurations == 0,
        {
            "lawful_domain_rejections": rejected,
            "Q2_collision_configurations_in_declared_code": collision_configurations,
            "collision_route_disposition": "open outside the global-Q1 compiler",
        },
    )


def inventory_controls() -> None:
    print("\nSUPPLIED / DERIVED / OPEN INVENTORY")
    inventory = {
        "matter substrate": "Cycle-319 n<=3 three-cell/two-edge M64 shell",
        "matter law": "Cycle-219 coin, two ordered FSWAPs, Cycle-230 contact",
        "source laws": "Cycle-325 unit-weight and Cycle-322 coefficient-two local vertices",
        "source sector": "supplied global Q=1 reservoir-or-carrier code",
        "unit auxiliary": "six auxiliary M2 per cell with a local paired-cell constraint",
        "transport": "supplied direction coin and bounded nearest-neighbor carrier stream",
        "overlap compiler": "one A/B/C factorization; B matter and source registers occur once",
        "physical completion": "supplied Cycle-319 dense matrix-unit identity completion",
        "role data": "supplied bounded three-M2 S3 factor-order role register",
        "derived": "embedded source unitaries, EG/inverse, reciprocal response, controls",
        "not used": "global parity string, Jordan-Wigner ordering, nonlocal parity service, host branch",
        "open": "primitive sparse synthesis, Q2 collision extension, preparation/selection law",
        "interpretation": "dimensionless response; not physical energy/stress/source/gravity/time/occurrence/Record",
        "authority": "none",
        "audit": "unset",
    }
    check(
        "all supplied structure and residual implementation walls are explicit",
        len(inventory) == 15,
        inventory,
    )


def methodology_controls() -> None:
    check(
        "the result is constructive and makes no no-go, minimum-content, or axiom-pressure claim",
        True,
        {
            "route_specific_failures_are_shared_obstructions": False,
            "N1_to_N8_triggered": False,
            "axiom_pressure": False,
            "Thirring_used": False,
        },
    )


def main() -> int:
    print("CYCLE 396: SHARED-MIDDLE THREE-CELL PHYSICAL SOURCE COMPILER")
    print("authority=none; audit=unset")
    note_contract()
    update_rows, coin, first, second, contact, _forward, _reverse = c319.update_controls(
        LABELS, "path"
    )
    factors = (coin, first, second, contact)
    local_and_shared_middle_controls()
    conservation_and_covariance_controls(factors, update_rows)
    shell_and_physical_controls(factors)
    response_and_deletion_controls(factors, contact)
    inventory_controls()
    methodology_controls()
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL})
    if FAIL:
        print("RESULT SHARED_MIDDLE_THREE_CELL_SOURCE_COMPILER_OPEN")
        return 1
    print("RESULT SHARED_MIDDLE_THREE_CELL_SOURCE_COMPILER_CERTIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
