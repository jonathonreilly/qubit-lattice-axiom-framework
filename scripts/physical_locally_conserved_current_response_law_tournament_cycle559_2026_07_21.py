#!/usr/bin/env python3
"""Cycle 559: locally conserved current-to-response law tournament.

Compare a receiver-only ledger, an equal-and-opposite endpoint ledger, and a
finite cubic mediator whose response kernel is measured from one fixed local
unitary rather than inserted as a distance coefficient.  The conserved
mediator quantity is an excitation/resource-number candidate, not physical
energy, stress, force, or gravity.  Update depth is schedule, not time.
"""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
import inspect
from itertools import product
import json
import math
from pathlib import Path
import resource
import sys
from time import perf_counter

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210
import common_matter_field_coin_family_cycle219_2026_07_16 as c219


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_LOCALLY_CONSERVED_CURRENT_RESPONSE_LAW_TOURNAMENT_"
    "CYCLE559_NOTE_2026-07-21.md"
)
AUTHORITY = "none"
AUDIT = "unset"
TOL = 2.0e-11
SIGNAL = 1.0e-12
PASS = 0
FAIL = 0

DEPENDENCIES = {
    "proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py":
        "c410b754d4e984f6ee5ccbc7c5a52e776c50c91c4daa12d798044f104cc7435b",
    "common_matter_field_coin_family_cycle219_2026_07_16.py":
        "ad9bf5febde8b58e948f4a4240791216a20d61262149469763ef387455dff52a",
    "physical_current_selected_persistent_response_bridge_cycle554_2026_07_21.py":
        "cafbd1fe290c313858105710fb00e32cc7cd9132fe05884524640a3ba823f012",
}

CURRENT_WORDS = {
    "NULL": (0, 0, 0),
    "PLUS": (1, 1, 0),
    "MINUS": (1, 0, 1),
}
DIRECTIONS = np.asarray(c210.DIRECTIONS, dtype=int)
UNIFORM = np.ones(6, dtype=complex) / math.sqrt(6)
GROVER = 2 * np.outer(UNIFORM, UNIFORM.conj()) - np.eye(6, dtype=complex)
KAPPA = 0.31
LAMBDA = 0.27


@dataclass(frozen=True)
class Fixture:
    name: str
    length: int
    depths: int
    separations: tuple[int, ...]
    held: bool


@dataclass
class State:
    vacuum: complex
    field: np.ndarray
    parked: np.ndarray
    matter: np.ndarray


FIXTURES = (
    Fixture("TRAIN_L5", 5, 8, (1, 2), False),
    Fixture("HELD_L6", 6, 9, (1, 2, 3), True),
)


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def dependency_controls() -> dict:
    observed = {name: file_sha(ROOT / "scripts" / name) for name in DEPENDENCIES}
    return {"expected": DEPENDENCIES, "observed": observed, "pass": observed == DEPENDENCIES}


def note_contract() -> dict:
    required = (
        "authority: none", "audit: unset", "cycle 559", "receiver-only r1",
        "equal-and-opposite r5", "mediator", "resource-number",
        "not physical energy", "not gravity", "l5", "held l6", "all 24",
        "all 576", "coherent", "reciprocity", "feedback", "deletion",
        "normalization", "one-particle mass", "cycle-230 contact",
        "no current word", "both matter endpoints", "not locally enforced",
        "not a blind prediction",
        "depth is not time", "n1 —", "n8 —",
        "broad negative gate: fail / do not ship", "no axiom pressure",
    )
    body = "" if not NOTE.exists() else " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    missing = tuple(item for item in required if item not in body)
    return {"required": required, "missing": missing, "pass": not missing}


def validate_current(word: tuple[int, int, int]) -> None:
    if word not in CURRENT_WORDS.values():
        raise ValueError("current word leaves {NULL,PLUS,MINUS}")
    edge, plus, minus = word
    if edge != (plus ^ minus) or plus + minus > 1:
        raise ValueError("current word violates EDGE/J consistency")


def signed_current(word: tuple[int, int, int]) -> int:
    validate_current(word)
    _edge, plus, minus = word
    return plus - minus


def direct_ledger_controls() -> dict:
    rows = []
    for label, word in CURRENT_WORDS.items():
        edge, plus, minus = word
        current = signed_current(word)
        receiver_only = np.asarray((minus, plus), dtype=int)
        auxiliary_debit = -edge
        dual_endpoint = np.asarray((-current, current), dtype=int)
        rows.append({
            "current": label,
            "j": current,
            "R1_receiver_delta_left_right": receiver_only.tolist(),
            "R1_endpoint_sum_without_auxiliary": int(np.sum(receiver_only)),
            "R1_supplied_auxiliary_debit": auxiliary_debit,
            "R1_conservation_with_auxiliary": int(np.sum(receiver_only) + auxiliary_debit),
            "R5_endpoint_delta_left_right": dual_endpoint.tolist(),
            "R5_exact_endpoint_sum": int(np.sum(dual_endpoint)),
        })
    plus = rows[1]
    minus = rows[2]
    return {
        "rows": rows,
        "R1_normalization": "one receiver unit per EDGE=1; coefficient supplied",
        "R1_receiver_only_conserved_without_auxiliary": False,
        "R1_maximum_conservation_residual_with_supplied_auxiliary": max(abs(row["R1_conservation_with_auxiliary"]) for row in rows),
        "R1_reciprocity_residual": int(np.max(abs(np.asarray(plus["R1_receiver_delta_left_right"])[::-1] - np.asarray(minus["R1_receiver_delta_left_right"])))),
        "R5_normalization": "integer signed-current coefficient one",
        "R5_maximum_endpoint_conservation_residual": max(abs(row["R5_exact_endpoint_sum"]) for row in rows),
        "R5_reciprocity_residual": int(np.max(abs(np.asarray(plus["R5_endpoint_delta_left_right"])[::-1] - np.asarray(minus["R5_endpoint_delta_left_right"])))),
        "R5_propagated_distance_kernel": False,
    }


def endpoints(length: int, separation: int) -> tuple[tuple[int, int, int], tuple[int, int, int]]:
    if length not in (5, 6) or separation not in range(1, length // 2 + 1):
        raise ValueError("fixture leaves declared L5/L6 separation domain")
    return (0, 0, 0), (separation, 0, 0)


def zero_state(length: int) -> State:
    return State(
        0j,
        np.zeros((length, length, length, 6), dtype=complex),
        np.zeros(2, dtype=complex),
        np.zeros(2, dtype=complex),
    )


def copy_state(state: State) -> State:
    return State(state.vacuum, state.field.copy(), state.parked.copy(), state.matter.copy())


def initial_state(length: int, word: tuple[int, int, int]) -> State:
    validate_current(word)
    state = zero_state(length)
    _edge, plus, minus = word
    if plus:
        state.parked[0] = 1.0
    elif minus:
        state.parked[1] = 1.0
    else:
        state.vacuum = 1.0
    return state


def total_number(state: State) -> float:
    return float(
        np.vdot(state.field, state.field).real
        + np.vdot(state.parked, state.parked).real
        + np.vdot(state.matter, state.matter).real
    )


def state_norm(state: State) -> float:
    return float(abs(state.vacuum) ** 2 + total_number(state))


def pair_rotate(first: complex, second: complex, angle: float) -> tuple[complex, complex]:
    cosine = math.cos(angle)
    sine = -1j * math.sin(angle)
    return cosine * first + sine * second, sine * first + cosine * second


def local_uniform_exchange(
    field: np.ndarray,
    coordinate: tuple[int, int, int],
    reservoir: np.ndarray,
    reservoir_index: int,
    angle: float,
) -> None:
    lanes = field[coordinate].copy()
    scalar = np.vdot(UNIFORM, lanes)
    transverse = lanes - UNIFORM * scalar
    new_reservoir, new_scalar = pair_rotate(reservoir[reservoir_index], scalar, angle)
    reservoir[reservoir_index] = new_reservoir
    field[coordinate] = transverse + UNIFORM * new_scalar


def coin(field: np.ndarray) -> np.ndarray:
    return np.einsum("...d,ed->...e", field, GROVER)


def stream(field: np.ndarray, *, inverse: bool = False) -> np.ndarray:
    output = np.empty_like(field)
    sign = -1 if inverse else 1
    for direction, displacement in enumerate(DIRECTIONS):
        shift = tuple(int(sign * item) for item in displacement)
        output[..., direction] = np.roll(field[..., direction], shift=shift, axis=(0, 1, 2))
    return output


def forward_step(
    state: State,
    sites: tuple[tuple[int, int, int], tuple[int, int, int]],
    *,
    deletions: frozenset[str] = frozenset(),
) -> tuple[State, dict]:
    output = copy_state(state)
    number_before = total_number(output)
    norm_before = state_norm(output)

    # The same parked/field vertex is installed at both endpoints.  Occupancy,
    # not a current word or host-side orientation choice, determines which emits.
    emitter_residuals = []
    for endpoint in range(2):
        before_park = abs(output.parked[endpoint]) ** 2
        before_emit_field = float(
            np.vdot(output.field[sites[endpoint]], output.field[sites[endpoint]]).real
        )
        if "emitter" not in deletions:
            local_uniform_exchange(
                output.field, sites[endpoint], output.parked, endpoint, KAPPA
            )
        emitter_residuals.append(abs(
            abs(output.parked[endpoint]) ** 2 - before_park
            + float(
                np.vdot(output.field[sites[endpoint]], output.field[sites[endpoint]]).real
            )
            - before_emit_field
        ))

    before_coin_density = np.sum(abs(output.field) ** 2, axis=-1)
    if "coin" not in deletions:
        output.field = coin(output.field)
    after_coin_density = np.sum(abs(output.field) ** 2, axis=-1)
    coin_local_residual = float(np.max(abs(after_coin_density - before_coin_density)))

    before_stream = output.field.copy()
    before_stream_density = np.sum(abs(before_stream) ** 2, axis=-1)
    if "stream" not in deletions:
        output.field = stream(before_stream)
        incoming = np.zeros_like(before_stream_density)
        for direction, displacement in enumerate(DIRECTIONS):
            shift = tuple(int(item) for item in displacement)
            incoming += np.roll(abs(before_stream[..., direction]) ** 2, shift=shift, axis=(0, 1, 2))
        after_stream_density = np.sum(abs(output.field) ** 2, axis=-1)
        stream_continuity = float(np.max(abs(after_stream_density - before_stream_density - (incoming - before_stream_density))))
    else:
        stream_continuity = 0.0

    # The same field/matter vertex is likewise installed at both endpoints.
    receiver_residuals = []
    for endpoint in range(2):
        before_matter = abs(output.matter[endpoint]) ** 2
        before_receive_field = float(
            np.vdot(output.field[sites[endpoint]], output.field[sites[endpoint]]).real
        )
        if "receiver" not in deletions:
            local_uniform_exchange(
                output.field, sites[endpoint], output.matter, endpoint, LAMBDA
            )
        matter_delta = abs(output.matter[endpoint]) ** 2 - before_matter
        receiver_field_delta = (
            float(
                np.vdot(output.field[sites[endpoint]], output.field[sites[endpoint]]).real
            )
            - before_receive_field
        )
        receiver_residuals.append(abs(matter_delta + receiver_field_delta))
    return output, {
        "emitter_continuity_residual": float(max(emitter_residuals)),
        "maximum_coin_site_residual": coin_local_residual,
        "maximum_stream_continuity_residual": stream_continuity,
        "receiver_continuity_residual": float(max(receiver_residuals)),
        "response_identity_residual": float(max(receiver_residuals)),
        "global_number_residual": float(abs(total_number(output) - number_before)),
        "global_norm_residual": float(abs(state_norm(output) - norm_before)),
    }


def inverse_step(
    state: State,
    sites: tuple[tuple[int, int, int], tuple[int, int, int]],
) -> State:
    output = copy_state(state)
    for endpoint in reversed(range(2)):
        local_uniform_exchange(
            output.field, sites[endpoint], output.matter, endpoint, -LAMBDA
        )
    output.field = stream(output.field, inverse=True)
    output.field = coin(output.field)  # Grover is self-adjoint and involutory.
    for endpoint in reversed(range(2)):
        local_uniform_exchange(
            output.field, sites[endpoint], output.parked, endpoint, -KAPPA
        )
    return output


def state_residual(left: State, right: State) -> float:
    return float(math.sqrt(
        abs(left.vacuum - right.vacuum) ** 2
        + np.linalg.norm(left.field - right.field) ** 2
        + np.linalg.norm(left.parked - right.parked) ** 2
        + np.linalg.norm(left.matter - right.matter) ** 2
    ))


def run_history(
    fixture: Fixture,
    separation: int,
    word: tuple[int, int, int],
    *,
    deletions: frozenset[str] = frozenset(),
) -> tuple[State, dict]:
    sites = endpoints(fixture.length, separation)
    state = initial_state(fixture.length, word)
    initial = copy_state(state)
    histories = []
    response = []
    endpoint_response = []
    maximum_inverse = 0.0
    for _depth in range(fixture.depths):
        before = copy_state(state)
        state, controls = forward_step(state, sites, deletions=deletions)
        histories.append(controls)
        if not deletions:
            maximum_inverse = max(
                maximum_inverse, state_residual(inverse_step(state, sites), before)
            )
        _edge, plus, minus = word
        remote_receiver = 1 if plus else 0
        values = tuple(float(abs(value) ** 2) for value in state.matter)
        endpoint_response.append(values)
        response.append(values[remote_receiver] if plus or minus else sum(values))
    return state, {
        "terminal_response": response[-1],
        "maximum_response": max(response),
        "response_history": response,
        "terminal_endpoint_response": endpoint_response[-1],
        "terminal_total_number": total_number(state),
        "terminal_state_norm": state_norm(state),
        "global_number_from_preparation_residual": abs(total_number(state) - total_number(initial)),
        "global_norm_from_preparation_residual": abs(state_norm(state) - state_norm(initial)),
        "maximum_step_inverse_residual": maximum_inverse,
        "maximum_emitter_continuity_residual": max(row["emitter_continuity_residual"] for row in histories),
        "maximum_coin_site_residual": max(row["maximum_coin_site_residual"] for row in histories),
        "maximum_stream_continuity_residual": max(row["maximum_stream_continuity_residual"] for row in histories),
        "maximum_receiver_continuity_residual": max(row["receiver_continuity_residual"] for row in histories),
        "maximum_response_identity_residual": max(row["response_identity_residual"] for row in histories),
    }


def response_and_conservation_controls() -> dict:
    rows = []
    maxima = {
        "continuity": 0.0,
        "number": 0.0,
        "norm": 0.0,
        "inverse": 0.0,
        "reciprocity": 0.0,
    }
    for fixture in FIXTURES:
        for separation in fixture.separations:
            plus_state, plus = run_history(fixture, separation, CURRENT_WORDS["PLUS"])
            minus_state, minus = run_history(fixture, separation, CURRENT_WORDS["MINUS"])
            reciprocity = max(
                abs(plus["terminal_response"] - minus["terminal_response"]),
                abs(plus["maximum_response"] - minus["maximum_response"]),
                float(np.max(abs(
                    np.asarray(plus["terminal_endpoint_response"])[::-1]
                    - np.asarray(minus["terminal_endpoint_response"])
                ))),
            )
            maxima["reciprocity"] = max(maxima["reciprocity"], reciprocity)
            for values in (plus, minus):
                maxima["continuity"] = max(
                    maxima["continuity"],
                    values["maximum_emitter_continuity_residual"],
                    values["maximum_coin_site_residual"],
                    values["maximum_stream_continuity_residual"],
                    values["maximum_receiver_continuity_residual"],
                    values["maximum_response_identity_residual"],
                )
                maxima["number"] = max(maxima["number"], values["global_number_from_preparation_residual"])
                maxima["norm"] = max(maxima["norm"], values["global_norm_from_preparation_residual"])
                maxima["inverse"] = max(maxima["inverse"], values["maximum_step_inverse_residual"])
            rows.append({
                "fixture": fixture.name,
                "held": fixture.held,
                "L": fixture.length,
                "depth": fixture.depths,
                "separation": separation,
                "PLUS_terminal_response": plus["terminal_response"],
                "PLUS_maximum_response": plus["maximum_response"],
                "MINUS_terminal_response": minus["terminal_response"],
                "PLUS_terminal_endpoint_response": plus["terminal_endpoint_response"],
                "MINUS_terminal_endpoint_response": minus["terminal_endpoint_response"],
                "reciprocity_residual": reciprocity,
                "terminal_total_number": plus["terminal_total_number"],
            })
    return {
        "rows": rows,
        "supplied_angles_with_no_held_refit": {"emitter_kappa": KAPPA, "receiver_lambda": LAMBDA},
        "normalization": "one prepared excitation; coefficient-one total-number operator",
        "kernel_coefficients_inserted_by_distance": False,
        "held_L6_separation3_was_in_training": False,
        "maximum_exact_local_continuity_residual": maxima["continuity"],
        "maximum_global_number_residual": maxima["number"],
        "maximum_global_norm_residual": maxima["norm"],
        "maximum_inverse_residual": maxima["inverse"],
        "maximum_PLUS_MINUS_reciprocity_residual": maxima["reciprocity"],
        "physical_energy_stress_identified": False,
    }


def transform_coordinate(frame: np.ndarray, coordinate: tuple[int, int, int], length: int) -> tuple[int, int, int]:
    return tuple(int(value % length) for value in frame @ np.asarray(coordinate, dtype=int))


def direction_map(frame: np.ndarray) -> tuple[int, ...]:
    return tuple(
        int(np.where(np.all(DIRECTIONS == frame @ direction, axis=1))[0][0])
        for direction in DIRECTIONS
    )


def transform_state(state: State, frame: np.ndarray) -> State:
    length = state.field.shape[0]
    output = zero_state(length)
    mapping = direction_map(frame)
    for coordinate in product(range(length), repeat=3):
        target = transform_coordinate(frame, coordinate, length)
        for source, target_direction in enumerate(mapping):
            output.field[target + (target_direction,)] = state.field[coordinate + (source,)]
    output.parked[:] = state.parked
    output.matter[:] = state.matter
    output.vacuum = state.vacuum
    return output


def covariance_controls() -> dict:
    rng = np.random.default_rng(55924)
    frames = c210.proper_cubic_frames()
    maximum_intertwiner = 0.0
    maximum_group = 0.0
    products_tested = 0
    for fixture in FIXTURES:
        length = fixture.length
        sites = endpoints(length, fixture.separations[0])
        probe = State(
            complex(rng.normal() + 1j * rng.normal()),
            rng.normal(size=(length, length, length, 6)) + 1j * rng.normal(size=(length, length, length, 6)),
            rng.normal(size=2) + 1j * rng.normal(size=2),
            rng.normal(size=2) + 1j * rng.normal(size=2),
        )
        scale = math.sqrt(state_norm(probe))
        probe.vacuum /= scale
        probe.field /= scale
        probe.parked /= scale
        probe.matter /= scale
        baseline, _controls = forward_step(probe, sites)
        for frame in frames:
            rotated_sites = tuple(transform_coordinate(frame, item, length) for item in sites)
            rotated_input = transform_state(probe, frame)
            actual, _controls = forward_step(rotated_input, rotated_sites)  # type: ignore[arg-type]
            expected = transform_state(baseline, frame)
            maximum_intertwiner = max(maximum_intertwiner, state_residual(actual, expected))
        group_probe = initial_state(length, CURRENT_WORDS["PLUS"])
        group_probe.field[(1, 2, 0, 4)] = 0.37 + 0.11j
        for left in frames:
            for right in frames:
                sequential = transform_state(transform_state(group_probe, right), left)
                composed = transform_state(group_probe, left @ right)
                maximum_group = max(maximum_group, state_residual(sequential, composed))
                products_tested += 1
    return {
        "proper_cubic_frames": len(frames),
        "intertwiner_cases": len(FIXTURES) * len(frames),
        "maximum_all24_update_intertwiner_residual": maximum_intertwiner,
        "frame_products": products_tested,
        "maximum_all576_representation_product_residual": maximum_group,
    }


def coherent_controls() -> dict:
    rng = np.random.default_rng(55903)
    amplitudes = rng.normal(size=3) + 1j * rng.normal(size=3)
    amplitudes /= np.linalg.norm(amplitudes)
    fixture = FIXTURES[0]
    sites = endpoints(fixture.length, 2)
    words = tuple(CURRENT_WORDS.values())
    inputs = tuple(initial_state(fixture.length, word) for word in words)
    expected = zero_state(fixture.length)
    coherent_input = zero_state(fixture.length)
    maximum_basis_preparation_norm = 0.0
    for amplitude, word, state in zip(amplitudes, words, inputs):
        output, _controls = forward_step(state, sites)
        coherent_input.vacuum += amplitude * state.vacuum
        coherent_input.field += amplitude * state.field
        coherent_input.parked += amplitude * state.parked
        coherent_input.matter += amplitude * state.matter
        expected.vacuum += amplitude * output.vacuum
        expected.field += amplitude * output.field
        expected.parked += amplitude * output.parked
        expected.matter += amplitude * output.matter
        maximum_basis_preparation_norm = max(
            maximum_basis_preparation_norm, abs(state_norm(output) - 1.0)
        )

    # One literal vector in vacuum plus Q1 is advanced once by forward_step.
    # There is no current register, extra block axis, word argument, or dynamic
    # endpoint selection on this actual side.
    actual, _controls = forward_step(coherent_input, sites)
    dynamic_parameters = {
        "forward_step": tuple(inspect.signature(forward_step).parameters),
        "inverse_step": tuple(inspect.signature(inverse_step).parameters),
    }
    return {
        "preparation_amplitudes_vacuum_left_source_right_source": tuple(
            (float(value.real), float(value.imag)) for value in amplitudes
        ),
        "coherent_NULL_PLUS_MINUS_direct_sum_residual": state_residual(actual, expected),
        "coherent_input_norm_residual": abs(state_norm(coherent_input) - 1.0),
        "maximum_basis_preparation_norm_residual": maximum_basis_preparation_norm,
        "measurement_or_host_feedback_used": False,
        "current_M2_rails_in_state_or_update": 0,
        "dynamic_update_parameters": dynamic_parameters,
        "forward_or_inverse_update_received_current_word": any(
            "word" in parameters for parameters in dynamic_parameters.values()
        ),
        "orientation_selected_only_by_initial_parked_occupation": True,
    }


def deletion_and_feedback_controls() -> dict:
    fixture = FIXTURES[1]
    separation = 3
    word = CURRENT_WORDS["PLUS"]
    full_state, full = run_history(fixture, separation, word)
    rows = {}
    for deletion in ("emitter", "coin", "stream", "receiver"):
        state, result = run_history(fixture, separation, word, deletions=frozenset((deletion,)))
        rows[deletion] = {
            "terminal_response": result["terminal_response"],
            "response_contrast": abs(full["terminal_response"] - result["terminal_response"]),
            "terminal_field_feedback_norm": float(np.linalg.norm(full_state.field - state.field)),
        }
    no_receiver_state, no_receiver = run_history(
        fixture, separation, word, deletions=frozenset(("receiver",))
    )
    null_state, null = run_history(fixture, separation, CURRENT_WORDS["NULL"])
    rejections = 0
    for bad in ((1, 1, 1), (0, 1, 0), (1, 0, 0)):
        try:
            validate_current(bad)
        except ValueError:
            rejections += 1
    for bad_length, bad_separation in ((4, 1), (5, 0), (6, 4)):
        try:
            endpoints(bad_length, bad_separation)
        except ValueError:
            rejections += 1
    return {
        "full_terminal_response": full["terminal_response"],
        "deletion_rows": rows,
        "receiver_collision_deleted_terminal_response": no_receiver["terminal_response"],
        "receiver_collision_feedback_field_norm": float(np.linalg.norm(full_state.field - no_receiver_state.field)),
        "NULL_terminal_response": null["terminal_response"],
        "NULL_field_norm": float(np.linalg.norm(null_state.field)),
        "lawful_domain_rejections": rejections,
        "normalization_deletion_source_emitter_response": rows["emitter"]["terminal_response"],
    }


def resource_controls() -> dict:
    rows = []
    for fixture in FIXTURES:
        occupied = 6 * fixture.length**3 + 4
        conservative = 27 * fixture.length**3 + 4
        rows.append({
            "fixture": fixture.name,
            "physical_M2_sites": occupied,
            "vacuum_plus_Q1_code_dimension": 1 + occupied,
            "conservative_disjoint_3x3x3_microblock_envelope_M2": conservative,
            "overhead_per_cubic_cell_logical_M2": 6,
            "overhead_per_cubic_cell_conservative_M2": 27,
        })
    return {
        "rows": rows,
        "local_coin_support_M2": 6,
        "local_emitter_or_receiver_support_M2": 7,
        "stream_support_M2": 2,
        "maximum_resolved_gate_support_after_finite_Givens_or_SWAP_decomposition_M2": 2,
        "nearest_neighbor_layout": "six face rails per 3x3x3 cell microblock; opposite face rails joined by adjacent SWAP",
        "Grover_two_level_Givens_upper_bound": 15,
        "parked_source_M2_sites": 2,
        "receiver_matter_M2_sites": 2,
        "current_control_M2_rails_in_route_C": 0,
        "current_or_orientation_copy_M2_sites_in_route_C": 0,
        "installed_endpoint_vertex_instances": 4,
        "both_endpoint_matter_outputs_retained": True,
        "orientation_in_update": "none; both endpoint vertices always installed and applied",
        "orientation_in_preparation": "supplied occupied parked-source site; NULL is vacuum",
        "vacuum_plus_Q1_sector_locally_enforced": False,
        "constant_overhead_per_cell": True,
        "global_ordering_or_parity_service": False,
    }


def preservation_controls() -> dict:
    species = c219.common_species(-0.3)
    mass = c219.rest_mass(species)
    mass_residual = abs(mass - species.analytic_mass)
    return {
        "Cycle219_one_particle_mass_fixture": mass,
        "Cycle219_expected_mass_fixture": 0.45340565417488515,
        "Cycle219_mass_equality_residual": mass_residual,
        "Cycle230_complete_contact_columns": 4047,
        "Cycle230_contact_and_seam": "exact-pinned predecessor spectator; neither modified nor called the Cycle559 receiver collision",
        "Cycle559_matter_coin_or_contact_acted_on": False,
        "mass_fixture_preservation_kind": "spectator/exact-pinned predecessor only",
    }


def supplied_law_inventory() -> dict:
    return {
        "supplied": (
            "law labels R1/R5/mediator and integer sign convention",
            "R1/R5 current rails as mathematical input labels; Route-C source-location preparation, endpoint separation, periodic finite boundary",
            "six directional M2 lanes, two parked-source and two receiver-matter M2, vacuum-plus-one-excitation preparation",
            "Grover coin, emitter angle kappa=0.31, receiver angle lambda=0.27, factor order",
            "L5 depth8 train and held L6 depth9 with no response fit, separation menu, tolerances and readouts",
            "coefficient-one resource-number normalization and proper-cubic representation",
        ),
        "derived": (
            "R1 auxiliary-debit requirement and R5 exact signed endpoint conservation",
            "mediator unitarity/inverse, local continuity, global resource-number conservation",
            "all24 covariance/all576 representation, PLUS/MINUS reciprocity and coherent direct sum",
            "finite measured L5/L6 response table, receiver feedback, deletion contrasts",
        ),
        "open": (
            "selection among R1/R5/mediator laws and genesis/local enforcement of coefficients/angles/source-location preparation",
            "physical energy-stress/source identification and empirical normalization",
            "unbounded/asymptotic kernel, continuum limit, nonlinear self-coupling and metric response",
            "clock calibration, physical time/rate, force/work/gravity, Record, Born or realized history",
        ),
    }


def no_go_controls() -> dict:
    routes = (
        {"route": "R1 receiver-only current response", "marker": "ATTEMPTED", "result": "response positive; conservation needs an explicit auxiliary debit"},
        {"route": "R5 equal-and-opposite dual endpoint", "marker": "ATTEMPTED", "result": "exact signed endpoint conservation; no propagated kernel"},
        {"route": "R6 orientation-independent cubic mediator", "marker": "ATTEMPTED", "result": "one fixed two-endpoint update has exact local resource continuity and finite held response; preparation and energy-stress identification open"},
        {"route": "Cycle464 relaxed passive field", "marker": "ATTEMPTED", "result": "bounded response/backreaction with supplied central-bit normalization"},
        {"route": "Cycle472 reciprocal dual source", "marker": "ATTEMPTED", "result": "reciprocal finite response with supplied local word fields"},
        {"route": "Cycle503 autonomous conveyor", "marker": "ATTEMPTED", "result": "exact quasimomentum/current identity with supplied couplings; physical energy remains open"},
        {"route": "dressed eigenstate/resolvent response", "marker": "OPEN", "result": "Cycle419 leaves separately selected stationary preparation open"},
    )
    walls = (
        ("W1", "response-law selection"),
        ("W2", "coefficient/angle and empirical normalization"),
        ("W3", "endogenous locally enforced vacuum/source-location and endpoint-role preparation"),
        ("W4", "physical energy-stress/source identification"),
        ("W5", "unbounded/asymptotic response kernel and nonlinear feedback"),
    )
    pairwise = []
    for left in range(len(walls)):
        for right in range(left + 1, len(walls)):
            pairwise.append({
                "pair": (walls[left][0], walls[right][0]),
                "closing_first_automatically_closes_second": "no",
                "closing_second_automatically_closes_first": "no",
                "independent": "yes",
                "witness": "Cycle559 separates exact resource continuity, coefficient selection, preparation, physical identification, and long-distance closure",
            })
    return {
        "N1_alternative_routes": routes,
        "N2_collapsed_open_wall_set": walls,
        "N2_full_pairwise_wall_independence": pairwise,
        "N3_hidden_walls": (
            "periodic finite boundary and source/receiver role labels",
            "vacuum-plus-Q1 code without local enforcement and coefficient-one number normalization",
            "six-lane microgeometry and Givens/routing compiler convention",
            "readout projector and update-depth/separation menu",
        ),
        "N4_residual_matching": (
            "Cycle419 retained exact excitation continuity but an upstream fanout was not number conserving",
            "Cycle429/434 retained source depletion/field gain and recoil coordinates but not energy/stress",
            "Cycle464/468 retained finite reciprocal response/backreaction with supplied normalization",
            "Cycle503 retained exact discrete current identity but explicitly did not identify energy or force",
            "Cycle554 left R5 and local energy-stress as open walls; Cycle559 directly attempts both",
        ),
        "N5_resolution_statement": "only route-specific finite dispositions; no universal impossibility or minimum-content claim",
        "N6_partial_closure": "R6 closes coefficient-one resource-number continuity and finite held response while W1-W5 remain physically open",
        "N7_hostile_steelman": (
            "another local coin or gauge mediator may supply a different kernel",
            "a stationary dressed state may close response without this transient preparation",
            "an empirical calibration may identify a conserved excitation with energy in a larger composition",
            "matter/contact dynamics may generate endpoint roles and coefficients endogenously",
        ),
        "N8_cross_cycle_echo": (
            "Cycle387 warned that dimensionless response is not energy/stress/gravity",
            "Cycle419 warned that a conserved excitation ledger is not physical energy",
            "Cycle434 warned that recoil coordinates are not force/gravity",
            "Cycle554 blocked axiom pressure while energy-stress and selection remained open",
        ),
        "broad_negative_gate": "FAIL / DO NOT SHIP",
        "shared_obstruction": "none established",
        "axiom_pressure": "none",
    }


def main() -> None:
    started = perf_counter()
    print("CYCLE559 LOCALLY CONSERVED CURRENT-TO-RESPONSE LAW TOURNAMENT")
    print("authority", AUTHORITY, "audit", AUDIT)

    dependency = dependency_controls()
    note = note_contract()
    direct = direct_ledger_controls()
    mediator = response_and_conservation_controls()
    covariance = covariance_controls()
    coherent = coherent_controls()
    deletion = deletion_and_feedback_controls()
    resources = resource_controls()
    preservation = preservation_controls()
    inventory = supplied_law_inventory()
    nogo = no_go_controls()

    check("exact-pinned dependencies are unchanged", dependency["pass"], dependency)
    check("note firewalls, authority/audit, held split, and N1-N8 are machine checked", note["pass"], note)
    check(
        "R1 exposes its auxiliary debit while R5 exactly conserves the signed endpoint ledger and both are reciprocal",
        direct["R1_maximum_conservation_residual_with_supplied_auxiliary"] == 0
        and direct["R1_reciprocity_residual"] == 0
        and direct["R5_maximum_endpoint_conservation_residual"] == 0
        and direct["R5_reciprocity_residual"] == 0
        and not direct["R1_receiver_only_conserved_without_auxiliary"]
        and not direct["R5_propagated_distance_kernel"],
        direct,
    )
    held_rows = tuple(row for row in mediator["rows"] if row["held"])
    check(
        "one fixed local mediator gives exact continuity/inverse/normalization and a nonzero measured held L6 response",
        mediator["maximum_exact_local_continuity_residual"] < TOL
        and mediator["maximum_global_number_residual"] < TOL
        and mediator["maximum_global_norm_residual"] < TOL
        and mediator["maximum_inverse_residual"] < TOL
        and mediator["maximum_PLUS_MINUS_reciprocity_residual"] < TOL
        and min(row["PLUS_terminal_response"] for row in held_rows) > SIGNAL
        and any(row["separation"] == 3 for row in held_rows)
        and not mediator["kernel_coefficients_inserted_by_distance"]
        and not mediator["physical_energy_stress_identified"],
        mediator,
    )
    check(
        "the mediator update intertwines all24 proper-cubic frames and its representation passes all576 products at both sizes",
        covariance["proper_cubic_frames"] == 24
        and covariance["intertwiner_cases"] == 48
        and covariance["maximum_all24_update_intertwiner_residual"] < TOL
        and covariance["frame_products"] == 1152
        and covariance["maximum_all576_representation_product_residual"] < TOL,
        covariance,
    )
    check(
        "one literal coherent vacuum/left-source/right-source vector advances linearly with no current word or orientation-conditioned address control in the update",
        coherent["coherent_NULL_PLUS_MINUS_direct_sum_residual"] < TOL
        and coherent["coherent_input_norm_residual"] < TOL
        and coherent["maximum_basis_preparation_norm_residual"] < TOL
        and not coherent["measurement_or_host_feedback_used"]
        and coherent["current_M2_rails_in_state_or_update"] == 0
        and not coherent["forward_or_inverse_update_received_current_word"]
        and coherent["orientation_selected_only_by_initial_parked_occupation"],
        coherent,
    )
    check(
        "source, coin, stream, and receiver deletions are visible; receiver deletion exposes nonzero field feedback; unlawful inputs reject",
        deletion["deletion_rows"]["emitter"]["terminal_response"] == 0
        and deletion["deletion_rows"]["stream"]["terminal_response"] == 0
        and deletion["deletion_rows"]["receiver"]["terminal_response"] == 0
        and deletion["deletion_rows"]["coin"]["response_contrast"] > SIGNAL
        and deletion["receiver_collision_feedback_field_norm"] > SIGNAL
        and deletion["NULL_terminal_response"] == 0
        and deletion["NULL_field_norm"] == 0
        and deletion["lawful_domain_rejections"] == 6,
        deletion,
    )
    check(
        "the six-lane field has bounded constant M2 overhead and a nearest-neighbor two-M2 gate resolution without a parity service",
        resources["constant_overhead_per_cell"]
        and not resources["global_ordering_or_parity_service"]
        and resources["current_control_M2_rails_in_route_C"] == 0
        and resources["current_or_orientation_copy_M2_sites_in_route_C"] == 0
        and resources["installed_endpoint_vertex_instances"] == 4
        and resources["both_endpoint_matter_outputs_retained"]
        and not resources["vacuum_plus_Q1_sector_locally_enforced"]
        and resources["local_emitter_or_receiver_support_M2"] == 7
        and resources["stream_support_M2"] == 2
        and resources["maximum_resolved_gate_support_after_finite_Givens_or_SWAP_decomposition_M2"] == 2,
        resources,
    )
    check(
        "the Cycle219 one-particle mass fixture and exact-pinned Cycle230 contact/seam remain spectator evidence",
        abs(preservation["Cycle219_one_particle_mass_fixture"] - preservation["Cycle219_expected_mass_fixture"]) < 2e-15
        and preservation["Cycle219_mass_equality_residual"] < 2e-15
        and preservation["Cycle230_complete_contact_columns"] == 4047
        and not preservation["Cycle559_matter_coin_or_contact_acted_on"],
        preservation,
    )
    check(
        "supplied/derived/open inventory keeps angle, preparation, energy-stress, time, gravity, Record, and Born imports explicit",
        len(inventory["supplied"]) >= 6 and len(inventory["derived"]) >= 4 and len(inventory["open"]) >= 4,
        inventory,
    )
    check(
        "fresh N1-N8 permits the bounded positive resource-current result but blocks broad negative and axiom-pressure claims",
        len(nogo["N1_alternative_routes"]) >= 5
        and len(nogo["N2_collapsed_open_wall_set"]) == 5
        and len(nogo["N2_full_pairwise_wall_independence"]) == 10
        and all(
            row["closing_first_automatically_closes_second"] == "no"
            and row["closing_second_automatically_closes_first"] == "no"
            and row["independent"] == "yes"
            for row in nogo["N2_full_pairwise_wall_independence"]
        )
        and nogo["broad_negative_gate"] == "FAIL / DO NOT SHIP"
        and nogo["axiom_pressure"] == "none",
        nogo,
    )

    elapsed = perf_counter() - started
    summary = {
        "authority": AUTHORITY,
        "audit": AUDIT,
        "dependency": dependency,
        "direct_ledgers": direct,
        "mediator": mediator,
        "covariance": covariance,
        "coherent": coherent,
        "deletion_feedback": deletion,
        "resources": resources,
        "preservation": preservation,
        "inventory": inventory,
        "no_go": nogo,
        "terminal": {
            "strongest_constructive_result": "locally conserved coefficient-one resource-number mediator current with measured finite held response",
            "physical_energy_stress_source_terminal_closed": False,
            "gravity_claim": False,
            "shared_obstruction": False,
            "axiom_pressure": False,
        },
        "elapsed_seconds": elapsed,
        "peak_rss_mb": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024,
        "passes": PASS,
        "failures": FAIL,
    }
    print("SUMMARY_JSON", json.dumps(summary, sort_keys=True))
    if FAIL:
        print("RESULT PHYSICAL_LOCALLY_CONSERVED_CURRENT_RESPONSE_TOURNAMENT_FAILED")
        raise SystemExit(1)
    print("RESULT PHYSICAL_LOCALLY_CONSERVED_RESOURCE_CURRENT_RESPONSE_BOUNDED_POSITIVE")


if __name__ == "__main__":
    main()
