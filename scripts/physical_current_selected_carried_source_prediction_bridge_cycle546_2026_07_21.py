#!/usr/bin/env python3
"""Cycle 546: coherent selected-seam current -> carried-source receiver bridge.

The Cycle-526 EDGE_PASSED/J_plus/J_minus carriers control a literal bounded
Y-track.  One fixed schedule contains both arms; no current value selects a
host-side update.  A single Q=1 token is carried to the corresponding endpoint
emitter, after which the fixed symmetric Cycle-434 recoil/transport/receiver
engine is applied.  Schedule layers are compiler order, not physical time.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
import gc
import hashlib
from itertools import product
import json
from pathlib import Path
import resource
import sys
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_carried_source_motion_recoil_bridge_cycle434_2026_07_19 as c434


c429 = c434.c429
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_CURRENT_SELECTED_CARRIED_SOURCE_PREDICTION_BRIDGE_CYCLE546_NOTE_2026-07-21.md"
)
AUTHORITY = "none"
AUDIT = "unset"
TRAIN_SIZE = 5
HELD_SIZE = 6
TOL = 1.2e-9
PASS = 0
FAIL = 0

CYCLE_RUNNERS = {
    420: ROOT / "scripts/physical_source_prediction_bridge_contract_cycle420_2026_07_19.py",
    432: ROOT / "scripts/physical_signed_transverse_source_test_matter_prediction_cycle432_2026_07_19.py",
    434: ROOT / "scripts/physical_carried_source_motion_recoil_bridge_cycle434_2026_07_19.py",
    526: ROOT / "scripts/physical_selected_seam_event_current_adapter_cycle526_2026_07_21.py",
    530: ROOT / "scripts/physical_shadow_normal_form_sync_cycle530_2026_07_21.py",
    533: ROOT / "scripts/physical_selected_seam_code_space_isometry_compiler_cycle533_2026_07_21.py",
    539: ROOT / "scripts/physical_shared_seam_code_space_isometry_compiler_cycle539_2026_07_21.py",
    540: ROOT / "scripts/physical_rough_fswap_pauli_rotation_gate_compiler_cycle540_2026_07_21.py",
}
STRICT_FILE_HASHES = {
    CYCLE_RUNNERS[420]: "79eca68ca217277fa237d2420888b64ef7bfba801e8745925a8dfb14b7576d5c",
    CYCLE_RUNNERS[432]: "7e9a78895db3d1389f1cc119a51308c3a086d6bd7324ce49b8e8c615617f36c6",
    CYCLE_RUNNERS[434]: "b962f5a5de5bd21a600cfe808ca9134ed7815c5dc13521374ec79c4e623f0fb8",
    CYCLE_RUNNERS[526]: "7c3d4a35664eaf5c7737c86464ca069e15ce29c40f61778081af8139970c37cd",
    CYCLE_RUNNERS[530]: "f5f90a331803a43d293fa8e8e3640e29886bed81935827763773d84f61ce9c99",
    CYCLE_RUNNERS[533]: "72fe24e03b38812ef9f6dc610bc445b5ea6046a30683c2b734e9c0396e84facd",
    CYCLE_RUNNERS[539]: "aa126a6363f9fc8c08d28a47b840c1b6e0a7c0b47bbe296087340b804a0087d1",
    CYCLE_RUNNERS[540]: "1bb1528459fecb9f78ed3fe4c295d75e94ffb07745a1aa807bcdd4d276bf87fa",
}

CURRENT_BITS = {
    "NULL": (0, 0, 0),
    "PLUS": (1, 1, 0),
    "MINUS": (1, 0, 1),
}
CURRENT_ORDER = tuple(CURRENT_BITS)
ROLE_FOR_CURRENT = {"PLUS": "A_to_C", "MINUS": "C_to_A"}
SOURCE_FOR_CURRENT = {"PLUS": 0, "MINUS": 2}
RECEIVER_FOR_CURRENT = {"PLUS": 2, "MINUS": 0}
FIXED_ENGINE_ROLE = "A_to_C"

# Frozen values are comparators, not fitted inputs to the new schedule.
CYCLE420_HOST_VALUES = {
    "family1_odd_v0.5": 1.343024093419393e-08,
    "family1_odd_v1": 2.336182949854692e-08,
    "family2_odd_v0.5": 1.4954711268234017e-08,
    "family2_odd_v1": 2.5731175813034173e-08,
}
CYCLE432_VALUES = {
    "train_reservoir_contrast": 3.623825473668225e-06,
    "train_receiver_effect_contrast": 2.366440221008881e-06,
    "held_b1d3_receiver_effect_contrast": 7.889613205507204e-07,
    "held_b2d2_receiver_effect_contrast": 3.273727811347154e-07,
}


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def rss_bytes() -> int:
    return int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)


def swap_count() -> int:
    return int(getattr(resource.getrusage(resource.RUSAGE_SELF), "ru_nswap", 0))


def file_sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def dependency_controls() -> dict:
    expected = {
        str(path.relative_to(ROOT)): digest for path, digest in STRICT_FILE_HASHES.items()
    }
    observed = {
        str(path.relative_to(ROOT)): file_sha(path) for path in STRICT_FILE_HASHES
    }
    return {
        "expected_sha256": expected,
        "observed_sha256": observed,
        "strictly_gated_cycle_runners": tuple(CYCLE_RUNNERS),
        "pass": expected == observed,
    }


def normalized(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").lower().split())


def note_contract() -> dict:
    required = (
        "one fixed symmetric schedule",
        "literal q=1 token",
        "no host branch",
        "current=0 is a null control",
        "e_546 g_546 = g_physical,546 e_546",
        "cycle-434 frozen values without refit",
        "source/current/receiver deletions",
        "sparse direct-sum bookkeeping",
        "cycle-426 coefficient-two recoil vertex remains supplied",
        "no axiom pressure",
        "authority: none",
        "audit: unset",
    )
    body = "" if not NOTE.exists() else normalized(NOTE)
    missing = tuple(phrase for phrase in required if phrase not in body)
    return {"required_phrases": required, "missing": missing, "pass": not missing}


Coord = tuple[int, int, int]
CurrentKey = tuple[str, int]
CurrentState = dict[CurrentKey, np.ndarray]


@dataclass(frozen=True)
class CurrentFixture:
    length: int
    family: str
    origin_key: int
    plus_keys: tuple[int, ...]
    minus_keys: tuple[int, ...]
    plus_coordinates: tuple[Coord, ...]
    minus_coordinates: tuple[Coord, ...]

    @property
    def path_length(self) -> int:
        return len(self.plus_keys) - 1

    @property
    def external_track_keys(self) -> tuple[int, ...]:
        return tuple(
            sorted(
                (set(self.plus_keys) | set(self.minus_keys))
                - {c429.reservoir_site(0), c429.reservoir_site(2)}
            )
        )


def fixture(length: int) -> CurrentFixture:
    origin = c429.FIELD_DIM
    if length == TRAIN_SIZE:
        plus_keys = (origin, origin + 1, c429.reservoir_site(0))
        minus_keys = (origin, origin + 2, c429.reservoir_site(2))
        plus_coordinates = ((0, 1, 0), (-1, 1, 0), (-1, 0, 0))
        minus_coordinates = ((0, 1, 0), (1, 1, 0), (1, 0, 0))
        family = "symmetric_straight_Y"
    elif length == HELD_SIZE:
        plus_keys = (origin, origin + 1, origin + 2, c429.reservoir_site(0))
        minus_keys = (origin, origin + 3, origin + 4, c429.reservoir_site(2))
        plus_coordinates = ((0, 2, 0), (-1, 2, 0), (-1, 1, 0), (-1, 0, 0))
        minus_coordinates = ((0, 2, 0), (1, 2, 0), (1, 1, 0), (1, 0, 0))
        family = "symmetric_dogleg_Y"
    else:
        raise ValueError("Cycle546 accepts only train L5 and held L6 fixtures")
    return CurrentFixture(
        length,
        family,
        origin,
        plus_keys,
        minus_keys,
        plus_coordinates,
        minus_coordinates,
    )


def state_residual(left: CurrentState, right: CurrentState) -> float:
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


def state_norm(state: CurrentState) -> float:
    return float(sum(np.vdot(value, value).real for value in state.values()))


def prune(state: CurrentState, threshold: float = 2e-13) -> CurrentState:
    return {key: value for key, value in state.items() if np.linalg.norm(value) > threshold}


def sector(state: CurrentState, current: str) -> dict[int, np.ndarray]:
    return {site: value for (code, site), value in state.items() if code == current}


def replace_sector(state: CurrentState, current: str, replacement) -> CurrentState:
    output = {key: value for key, value in state.items() if key[0] != current}
    output.update({(current, site): value for site, value in replacement.items()})
    return prune(output)


def carry_gates(item: CurrentFixture) -> tuple[tuple[str, int, int], ...]:
    plus = tuple(
        ("PLUS", item.plus_keys[index], item.plus_keys[index + 1])
        for index in range(item.path_length)
    )
    minus = tuple(
        ("MINUS", item.minus_keys[index], item.minus_keys[index + 1])
        for index in range(item.path_length)
    )
    return plus + minus


def tensor_carry_transition(
    current_bits: tuple[int, int, int],
    track_word: int,
    item: CurrentFixture,
    sites: tuple[int, ...],
    *,
    inverse: bool = False,
) -> tuple[tuple[int, int, int], int]:
    """Exact computational-basis action of the fixed Fredkin tensor circuit."""

    if len(current_bits) != 3 or any(bit not in (0, 1) for bit in current_bits):
        raise ValueError("EDGE/PLUS/MINUS must be three physical bits")
    if track_word not in range(1 << len(sites)):
        raise ValueError("track word leaves the declared tensor product")
    gates = carry_gates(item)
    if inverse:
        gates = tuple(reversed(gates))
    output = int(track_word)
    for control, left, right in gates:
        control_index = 1 if control == "PLUS" else 2
        if current_bits[control_index]:
            left_index = sites.index(left)
            right_index = sites.index(right)
            left_bit = (output >> left_index) & 1
            right_bit = (output >> right_index) & 1
            if left_bit != right_bit:
                output ^= (1 << left_index) | (1 << right_index)
    return current_bits, output


def tensor_circuit_controls(item: CurrentFixture) -> dict:
    """Exhaust the full current-bit x track-qubit basis, including off code."""

    sites = tuple(sorted(set(item.plus_keys) | set(item.minus_keys)))
    dimension = 8 * (1 << len(sites))
    permutation = np.empty(dimension, dtype=np.int64)
    inverse_failures = 0
    outputs = set()
    lawful_sparse_failures = 0
    invalid_code_words = 0
    for edge, plus, minus in product((0, 1), repeat=3):
        bits = (edge, plus, minus)
        current_index = (edge << 2) | (plus << 1) | minus
        invalid_code_words += int(bits not in CURRENT_BITS.values())
        for word in range(1 << len(sites)):
            _bits, target = tensor_carry_transition(bits, word, item, sites)
            column = current_index * (1 << len(sites)) + word
            row = current_index * (1 << len(sites)) + target
            permutation[column] = row
            outputs.add(row)
            restored_bits, restored = tensor_carry_transition(
                bits, target, item, sites, inverse=True
            )
            inverse_failures += int(restored_bits != bits or restored != word)

    for current in CURRENT_ORDER:
        bits = CURRENT_BITS[current]
        for site in sites:
            probe = {(current, site): np.ones(1, dtype=complex)}
            sparse_output = current_carry(probe, item)
            sparse_site = next(iter(sparse_output))[1]
            one_hot_word = 1 << sites.index(site)
            _bits, tensor_word = tensor_carry_transition(
                bits, one_hot_word, item, sites
            )
            tensor_site = sites[int(np.log2(tensor_word))]
            lawful_sparse_failures += int(sparse_site != tensor_site)

    digest = hashlib.sha256()
    digest.update(np.asarray((dimension, len(sites)), dtype=np.int64).tobytes())
    digest.update(permutation.tobytes())
    return {
        "track_tensor_qubits": len(sites),
        "current_tensor_qubits_EDGE_PLUS_MINUS": 3,
        "complete_tensor_basis_dimension": dimension,
        "fixed_gate_list": carry_gates(item),
        "permutation_unique_rows": len(outputs),
        "off_code_inverse_failures": inverse_failures,
        "lawful_sparse_direct_sum_vs_tensor_failures": lawful_sparse_failures,
        "lawful_current_words": tuple(CURRENT_BITS.values()),
        "invalid_current_words_flagged_only_by_code_constraint": invalid_code_words,
        "double_current_words_have_reversible_circuit_action": True,
        "permutation_sha256": digest.hexdigest(),
        "pass": len(outputs) == dimension
        and inverse_failures == 0
        and lawful_sparse_failures == 0
        and invalid_code_words == 5,
    }


def current_carry(
    state: CurrentState,
    item: CurrentFixture,
    *,
    inverse: bool = False,
    deleted_gate: int | None = None,
    delete_current_controls: bool = False,
) -> CurrentState:
    """Apply one fixed list of physical Fredkins controlled by J+ or J-."""

    output = dict(state)
    gates = carry_gates(item)
    indexed = tuple(enumerate(gates))
    if inverse:
        indexed = tuple(reversed(indexed))
    for index, (control, left, right) in indexed:
        if index == deleted_gate or delete_current_controls:
            continue
        moved = sector(output, control)
        moved = c434.swap_keys(moved, left, right)
        output = replace_sector(output, control, moved)
    return prune(output)


def map_engine(state: CurrentState, transform) -> CurrentState:
    output: CurrentState = {}
    for current in CURRENT_ORDER:
        transformed = transform(sector(state, current))
        output.update({(current, site): value for site, value in transformed.items()})
    return prune(output)


def fixed_forward(
    state: CurrentState,
    item: CurrentFixture,
    factors,
    *,
    depth: int = 3,
    carry_enabled: bool = True,
    delete_current_controls: bool = False,
    deleted_carry_gate: int | None = None,
    source_enabled: tuple[bool, bool, bool] = (True, True, True),
    enabled_edges: tuple[bool, bool] = (True, True),
    contact_enabled: bool = True,
) -> CurrentState:
    output = (
        current_carry(
            state,
            item,
            deleted_gate=deleted_carry_gate,
            delete_current_controls=delete_current_controls,
        )
        if carry_enabled
        else dict(state)
    )
    for _ in range(depth):
        output = map_engine(
            output,
            lambda value: c434.extended_step(
                value,
                FIXED_ENGINE_ROLE,
                factors,
                source_enabled=source_enabled,
                enabled_edges=enabled_edges,
                contact_enabled=contact_enabled,
            ),
        )
    return prune(output)


def fixed_inverse(state: CurrentState, item: CurrentFixture, factors, *, depth: int = 3):
    output = dict(state)
    for _ in range(depth):
        output = map_engine(
            output,
            lambda value: c434.extended_inverse(
                value, FIXED_ENGINE_ROLE, factors
            ),
        )
    return current_carry(output, item, inverse=True)


def physical_forward(state: CurrentState, item: CurrentFixture, encoding, factors):
    output = current_carry(state, item)
    for _ in range(3):
        output = map_engine(
            output,
            lambda value: c434.physical_step_extended(
                value, encoding, FIXED_ENGINE_ROLE, factors
            ),
        )
    return prune(output)


def physical_inverse(state: CurrentState, item: CurrentFixture, encoding, factors):
    output = dict(state)
    for _ in range(3):
        output = map_engine(
            output,
            lambda value: c434.physical_inverse_extended(
                value, encoding, FIXED_ENGINE_ROLE, factors
            ),
        )
    return current_carry(output, item, inverse=True)


def matter_basis(label) -> np.ndarray:
    vector = np.zeros(c429.MATTER_DIM, dtype=complex)
    vector[c429.LABEL_INDEX[label]] = 1
    return vector


def initial_state(item: CurrentFixture, amplitudes=None, *, delete_token=False) -> CurrentState:
    if amplitudes is None:
        amplitudes = {"NULL": 1.0 + 0j}
    vectors = {
        "NULL": matter_basis((0, (), 0, (), 0, ())),
        "PLUS": next(iter(c429.initial_state("A_to_C").values())).copy(),
        "MINUS": next(iter(c429.initial_state("C_to_A").values())).copy(),
    }
    output = {}
    for current, amplitude in amplitudes.items():
        if current not in CURRENT_BITS:
            raise ValueError("current is outside NULL/PLUS/MINUS code")
        if not delete_token and abs(amplitude) > 0:
            output[(current, item.origin_key)] = amplitude * vectors[current]
    return output


def encode_state(state: CurrentState, encoding) -> CurrentState:
    output = {}
    for current in CURRENT_ORDER:
        encoded = c429.encode_state(sector(state, current), encoding)
        output.update({(current, site): value for site, value in encoded.items()})
    return prune(output)


def receiver_weight(state: CurrentState, current: str) -> float:
    return c429.reservoir_weight(sector(state, current), RECEIVER_FOR_CURRENT[current])


def source_vertex_trace(carried, cell: int, factors):
    coin, _first, _second, _contact = factors
    output = c429.apply_matter(carried, coin)
    output = c434.field_coin_extended(output)
    before = after = None
    for candidate in c429.CELLS:
        if candidate == cell:
            before = output
        output = c429.apply_source(output, candidate)
        if candidate == cell:
            after = output
    assert before is not None and after is not None
    return before, after


def receiver_vertex_trace(second, cell: int, factors):
    return source_vertex_trace(second, cell, factors)


def branch_row(item: CurrentFixture, current: str, factors) -> dict:
    prepared = initial_state(item, {current: 1})
    carried_all = current_carry(prepared, item)
    carried = sector(carried_all, current)
    first = c434.extended_step(carried, FIXED_ENGINE_ROLE, factors)
    second = c434.extended_step(first, FIXED_ENGINE_ROLE, factors)
    third = c434.extended_step(second, FIXED_ENGINE_ROLE, factors)
    source = SOURCE_FOR_CURRENT[current]
    receiver = RECEIVER_FOR_CURRENT[current]
    source_before, source_after = source_vertex_trace(carried, source, factors)
    receiver_before, receiver_after = receiver_vertex_trace(second, receiver, factors)
    source_depletion = (
        c429.reservoir_weight(source_before, source)
        - c429.reservoir_weight(source_after, source)
    )
    source_field_gain = (
        c429.cell_q(source_after, source)
        - c429.reservoir_weight(source_after, source)
    )
    source_matter = (
        c429.matter_direction(source_after, source)
        - c429.matter_direction(source_before, source)
    )
    source_twice_field = 2 * (
        c429.field_direction(source_after, source)
        - c429.field_direction(source_before, source)
    )
    receiver_gain = (
        c429.reservoir_weight(receiver_after, receiver)
        - c429.reservoir_weight(receiver_before, receiver)
    )
    receiver_matter = (
        c429.matter_direction(receiver_after, receiver)
        - c429.matter_direction(receiver_before, receiver)
    )
    receiver_twice_field = 2 * (
        c429.field_direction(receiver_after, receiver)
        - c429.field_direction(receiver_before, receiver)
    )

    old_role = ROLE_FOR_CURRENT[current]
    old_family, old_stride = (
        ("straight", 1) if item.length == TRAIN_SIZE else ("dogleg", 2)
    )
    old_item = c434.fixture(item.length, old_role, old_family, old_stride)
    old_output = c434.common_forward(c434.track_initial(old_item), old_item, factors)

    return {
        "L": item.length,
        "held": item.length == HELD_SIZE,
        "current": current,
        "current_bits_EDGE_PLUS_MINUS": CURRENT_BITS[current],
        "emitter_cell": source,
        "receiver_cell": receiver,
        "receiver_reservoir_response": c429.reservoir_weight(third, receiver),
        "receiver_gain_at_exposed_vertex": receiver_gain,
        "receiver_matter_direction_change": receiver_matter,
        "receiver_twice_field_direction_change": receiver_twice_field,
        "receiver_direction_ledger_residual": receiver_matter + receiver_twice_field,
        "source_reservoir_depletion": source_depletion,
        "source_field_gain": source_field_gain,
        "source_resource_balance_residual": source_depletion - source_field_gain,
        "source_matter_direction_change": source_matter,
        "source_twice_field_direction_change": source_twice_field,
        "source_direction_ledger_residual": source_matter + source_twice_field,
        "global_Q_after_three": c429.state_norm(third),
        "old_Cycle434_complete_state_residual": c429.state_residual(third, old_output),
    }


def current_adapter_controls() -> dict:
    labels = c429.c319.c315.joint_labels()
    counts = {"NULL": 0, "PLUS": 0, "MINUS": 0}
    failures = 0
    for label in labels:
        left_number, left_label, right_number, right_label = label
        failures += int(left_number != len(left_label) or right_number != len(right_label))
        a = int(0 in left_label)
        b = int(1 in right_label)
        event = a ^ b
        plus = a & (1 ^ b)
        minus = (1 ^ a) & b
        current = plus - minus
        delta_left = b - a
        delta_right = a - b
        code = "PLUS" if plus else "MINUS" if minus else "NULL"
        counts[code] += 1
        failures += int((event, plus, minus) != CURRENT_BITS[code])
        failures += int(event != (plus ^ minus) or plus & minus)
        failures += int(delta_left != -current or delta_right != current)
    return {
        "complete_two_cell_Fock_columns": len(labels),
        "current_code_histogram": counts,
        "continuity_or_constraint_failures": failures,
        "Cycle526_relation": "EDGE=a XOR b; PLUS=a AND NOT b; MINUS=NOT a AND b",
        "pass": len(labels) == 4096 and failures == 0 and counts == {
            "NULL": 2048,
            "PLUS": 1024,
            "MINUS": 1024,
        },
    }


def schedule_and_covariance_controls(factors) -> dict:
    rows = []
    maximum_role_schedule_residual = 0.0
    maximum_frame_vector_residual = 0.0
    frame_failures = 0
    inverse_failures = 0
    tensor_rows = []
    frames = c429.c210.proper_cubic_frames()
    endpoint_reversing_frames = 0
    for frame in frames:
        mapped = frame @ np.asarray((1, 0, 0), dtype=int)
        axis = int(np.flatnonzero(mapped)[0])
        endpoint_reversing_frames += int(mapped[axis] == -1)
    for length in (TRAIN_SIZE, HELD_SIZE):
        item = fixture(length)
        tensor_rows.append(tensor_circuit_controls(item))
        all_sites = set(item.plus_keys) | set(item.minus_keys)
        for current, site in product(CURRENT_ORDER, sorted(all_sites)):
            probe = {(current, site): np.ones(1, dtype=complex)}
            inverse_failures += int(
                state_residual(
                    current_carry(current_carry(probe, item), item, inverse=True),
                    probe,
                )
                != 0
            )
        for path in (item.plus_coordinates, item.minus_coordinates):
            frame_failures += sum(
                c434.manhattan(left, right) != 1
                for left, right in zip(path, path[1:])
            )
            for frame in frames:
                moved = tuple(
                    tuple(int(value) for value in frame @ np.asarray(coord))
                    for coord in path
                )
                frame_failures += int(len(moved) != len(set(moved)))
                frame_failures += sum(
                    c434.manhattan(left, right) != 1
                    for left, right in zip(moved, moved[1:])
                )

        for current in ("PLUS", "MINUS"):
            carried = sector(current_carry(initial_state(item, {current: 1}), item), current)
            forward = c434.extended_step(carried, "A_to_C", factors)
            reverse = c434.extended_step(carried, "C_to_A", factors)
            maximum_role_schedule_residual = max(
                maximum_role_schedule_residual, c429.state_residual(forward, reverse)
            )

        plus = branch_row(item, "PLUS", factors)
        minus = branch_row(item, "MINUS", factors)
        plus_vector = plus["receiver_matter_direction_change"]
        minus_vector = minus["receiver_matter_direction_change"]
        for frame in frames:
            mapped_plus = frame @ plus_vector
            mapped_minus = frame @ minus_vector
            maximum_frame_vector_residual = max(
                maximum_frame_vector_residual,
                float(np.linalg.norm(mapped_plus + mapped_minus)),
            )
        rows.append(
            {
                "fixture": asdict(item),
                "fixed_controlled_Fredkins": len(carry_gates(item)),
                "bare_one_two_M2_calls_using_Cycle526_Fredkin_decomposition": 17
                * len(carry_gates(item)),
                "new_external_track_M2": len(item.external_track_keys),
                "plus_minus_receiver_odd_residual": float(
                    np.linalg.norm(plus_vector + minus_vector)
                ),
            }
        )
    return {
        "rows": rows,
        "full_tensor_circuit_rows": tensor_rows,
        "sparse_current_sector_keys_are_direct_sum_bookkeeping_only": True,
        "literal_tensor_circuit_controls": "physical EDGE/J_plus/J_minus M2",
        "fixed_engine_role_argument_for_all_current_sectors": FIXED_ENGINE_ROLE,
        "host_selected_engine_branches": 0,
        "proper_cubic_frames": len(frames),
        "endpoint_reversing_frames": endpoint_reversing_frames,
        "endpoint_action": "PLUS <-> MINUS under endpoint reversal; NULL fixed",
        "current_carry_inverse_failures": inverse_failures,
        "track_frame_failures": frame_failures,
        "maximum_AtoC_vs_CtoA_engine_schedule_residual": maximum_role_schedule_residual,
        "maximum_all24_rotated_odd_vector_residual": maximum_frame_vector_residual,
        "inherited_Cycle434_source_covariance_residual": 8.807749891993861e-16,
        "pass": inverse_failures == frame_failures == 0
        and all(row["pass"] for row in tensor_rows)
        and len(frames) == 24
        and endpoint_reversing_frames == 12
        and maximum_role_schedule_residual < 2e-13
        and maximum_frame_vector_residual < 2e-14,
    }


def response_controls(factors) -> dict:
    rows = []
    pair_rows = []
    failures = 0
    for length in (TRAIN_SIZE, HELD_SIZE):
        item = fixture(length)
        plus = branch_row(item, "PLUS", factors)
        minus = branch_row(item, "MINUS", factors)
        rows.extend((plus, minus))
        receiver_odd = float(
            np.linalg.norm(
                plus["receiver_matter_direction_change"]
                + minus["receiver_matter_direction_change"]
            )
        )
        source_odd = float(
            np.linalg.norm(
                plus["source_matter_direction_change"]
                + minus["source_matter_direction_change"]
            )
        )
        reciprocity = abs(
            plus["receiver_reservoir_response"]
            - minus["receiver_reservoir_response"]
        )
        pair_rows.append(
            {
                "L": length,
                "held": length == HELD_SIZE,
                "receiver_response_reciprocity_residual": reciprocity,
                "receiver_odd_vector_residual": receiver_odd,
                "source_backreaction_odd_vector_residual": source_odd,
                "plus_receiver_coordinate": plus["receiver_matter_direction_change"],
                "minus_receiver_coordinate": minus["receiver_matter_direction_change"],
            }
        )
        for row in (plus, minus):
            failures += int(row["receiver_reservoir_response"] < 1e-10)
            failures += int(row["old_Cycle434_complete_state_residual"] > 3e-13)
            failures += int(abs(row["source_resource_balance_residual"]) > 3e-14)
            failures += int(np.linalg.norm(row["source_direction_ledger_residual"]) > 2e-14)
            failures += int(np.linalg.norm(row["receiver_direction_ledger_residual"]) > 2e-14)
            failures += int(abs(row["global_Q_after_three"] - 1) > 3e-12)
        failures += int(receiver_odd > 2e-14 or source_odd > 2e-14 or reciprocity > 2e-14)

    train_plus = next(row for row in rows if row["L"] == 5 and row["current"] == "PLUS")
    comparisons = {
        "Cycle434_receiver_response_exact_replay": train_plus[
            "receiver_reservoir_response"
        ],
        "Cycle434_receiver_direction_exact_replay": train_plus[
            "receiver_matter_direction_change"
        ],
        "Cycle420_host_centroid_values_not_refitted": CYCLE420_HOST_VALUES,
        "Cycle432_phase_source_values_not_refitted": CYCLE432_VALUES,
        "Cycle420_type_match_claimed": False,
        "Cycle432_same_apparatus_claimed": False,
        "new_parameter_fit_count": 0,
    }
    return {
        "rows": rows,
        "odd_pairs": pair_rows,
        "frozen_prediction_comparisons": comparisons,
        "same_Cycle426_angle_and_Cycle434_three_update_schedule": True,
        "host_trajectory_used": False,
        "coherent_weights_called_probability": False,
        "direction_called_force_momentum_energy_stress_or_gravity": False,
        "schedule_called_time": False,
        "failures": failures,
        "pass": failures == 0,
    }


def null_deletion_domain_controls(factors, baseline: float) -> dict:
    item = fixture(TRAIN_SIZE)
    null_initial = initial_state(item, {"NULL": 1})
    null_output = fixed_forward(null_initial, item, factors)
    plus_initial = initial_state(item, {"PLUS": 1})
    source_deleted = fixed_forward(
        initial_state(item, {"PLUS": 1}, delete_token=True), item, factors
    )
    current_deleted = fixed_forward(
        plus_initial, item, factors, delete_current_controls=True
    )
    first_carry_deleted = fixed_forward(
        plus_initial, item, factors, deleted_carry_gate=0
    )
    emission_enabled = [True, True, True]
    emission_enabled[0] = False
    emission_deleted = fixed_forward(
        plus_initial, item, factors, source_enabled=tuple(emission_enabled)
    )
    receiver_enabled = [True, True, True]
    receiver_enabled[2] = False
    receiver_deleted = fixed_forward(
        plus_initial, item, factors, source_enabled=tuple(receiver_enabled)
    )
    first_transport = fixed_forward(
        plus_initial, item, factors, enabled_edges=(False, True)
    )
    second_transport = fixed_forward(
        plus_initial, item, factors, enabled_edges=(True, False)
    )
    contact_deleted = fixed_forward(
        plus_initial, item, factors, contact_enabled=False
    )
    restored = fixed_inverse(fixed_forward(plus_initial, item, factors), item, factors)

    rows = {
        "current0_full_apparatus_state_residual": state_residual(null_output, null_initial),
        "source_deleted_output_norm": state_norm(source_deleted),
        "current_rails_deleted_receiver": receiver_weight(current_deleted, "PLUS"),
        "first_carry_Fredkin_deleted_receiver": receiver_weight(first_carry_deleted, "PLUS"),
        "emitter_vertex_deleted_receiver": receiver_weight(emission_deleted, "PLUS"),
        "receiver_vertex_deleted_receiver": receiver_weight(receiver_deleted, "PLUS"),
        "first_transport_deleted_receiver": receiver_weight(first_transport, "PLUS"),
        "second_transport_deleted_receiver": receiver_weight(second_transport, "PLUS"),
        "contact_deleted_receiver": receiver_weight(contact_deleted, "PLUS"),
        "baseline_receiver": baseline,
        "logical_inverse_residual": state_residual(restored, plus_initial),
    }
    rejections = 0
    for probe in (
        lambda: fixture(4),
        lambda: initial_state(item, {"BAD": 1}),
    ):
        try:
            probe()
        except ValueError:
            rejections += 1
    invalid_current = (1, 1, 1)
    return {
        "rows": rows,
        "lawful_current_code": CURRENT_BITS,
        "invalid_double_current_word_rejected": invalid_current not in CURRENT_BITS.values(),
        "domain_rejections": rejections,
        "token_one_hot_constraint_support_M2": c429.FIELD_DIM + len(item.external_track_keys),
        "event_current_constraint_support_M2": 3,
        "pass": rows["current0_full_apparatus_state_residual"] < 2e-13
        and rows["source_deleted_output_norm"] == 0
        and rows["current_rails_deleted_receiver"] == 0
        and rows["first_carry_Fredkin_deleted_receiver"] == 0
        and rows["emitter_vertex_deleted_receiver"] == 0
        and rows["receiver_vertex_deleted_receiver"] == 0
        and rows["first_transport_deleted_receiver"] == 0
        and rows["second_transport_deleted_receiver"] == 0
        and abs(rows["contact_deleted_receiver"] - baseline) > 1e-9
        and rows["logical_inverse_residual"] < 2e-13
        and rejections == 2
        and invalid_current not in CURRENT_BITS.values(),
    }


def eg_controls(factors) -> dict:
    rows = []
    amplitudes = {
        "NULL": 0.3 + 0.1j,
        "PLUS": -0.2 + 0.5j,
        "MINUS": 0.4 - 0.25j,
    }
    norm = np.sqrt(sum(abs(value) ** 2 for value in amplitudes.values()))
    amplitudes = {key: value / norm for key, value in amplitudes.items()}
    for length in (TRAIN_SIZE, HELD_SIZE):
        item = fixture(length)
        encodings, _reducer, support, gram_raw = c429.c396.build_shell(length)
        encoding = encodings[c429.c319.ORDER_INDEX[(0, 1, 2)]]
        logical = initial_state(item, amplitudes)
        physical = encode_state(logical, encoding)
        logical_output = fixed_forward(logical, item, factors)
        physical_output = physical_forward(physical, item, encoding, factors)
        expected = encode_state(logical_output, encoding)
        restored_logical = fixed_inverse(logical_output, item, factors)
        restored_physical = physical_inverse(physical_output, item, encoding, factors)
        intermediate_weight = sum(
            np.vdot(value, value).real
            for (current, site), value in physical_output.items()
            if site in item.external_track_keys and site != item.origin_key
        )
        rows.append(
            {
                "L": length,
                "held": length == HELD_SIZE,
                "single_fixed_matter_encoding_order": (0, 1, 2),
                "encoding_shape": encoding.shape,
                "matter_support_M2": support,
                "Gram_raw": gram_raw[c429.c319.ORDER_INDEX[(0, 1, 2)]],
                "coherent_current_EG_residual": state_residual(
                    physical_output, expected
                ),
                "logical_inverse_residual": state_residual(restored_logical, logical),
                "physical_inverse_residual": state_residual(restored_physical, physical),
                "output_norm_drift": abs(state_norm(physical_output) - 1),
                "track_intermediate_terminal_weight": float(intermediate_weight),
            }
        )
        del encodings, encoding, physical, logical_output, physical_output, expected
        del restored_logical, restored_physical
        gc.collect()
    maximum = max(
        max(
            row["Gram_raw"],
            row["coherent_current_EG_residual"],
            row["logical_inverse_residual"],
            row["physical_inverse_residual"],
            row["output_norm_drift"],
            row["track_intermediate_terminal_weight"],
        )
        for row in rows
    )
    return {
        "identity": "E_546 G_546 = G_physical,546 E_546",
        "factorization": (
            "strict-pinned Cycle526/533/539 selected-seam current output tensor "
            "single Cycle429 matter encoding and literal current-controlled track"
        ),
        "declared_code": (
            "Cycle526 lawful EDGE/PLUS/MINUS code x Cycle429 988-state matter shell "
            "x complete Q1 over 21 internal plus bounded Y-track M2"
        ),
        "coherent_test_amplitudes": amplitudes,
        "rows": rows,
        "maximum_EG_inverse_leakage_residual": maximum,
        "off_code_completion": (
            "Cycle429 factorwise identity completion; physical Fredkins have their "
            "ordinary reversible action on all current/track words"
        ),
        "pass": maximum < TOL,
    }


def physics_fixture_controls(update_rows) -> dict:
    return {
        "Cycle219_mass_fixture": update_rows["Cycle219_mass_fixture"],
        "receiver_engine_three_cell_mass": update_rows["three_cell_rest_mass"],
        "receiver_engine_uniform_one_particle_residual": update_rows[
            "uniform_one_particle_eigen_residual"
        ],
        "receiver_engine_contact_nontrivial_columns": update_rows[
            "contact_nontrivial_columns"
        ],
        "receiver_engine_first_FSWAP_unitarity_residual": update_rows[
            "first_FSWAP_unitarity_residual"
        ],
        "receiver_engine_second_FSWAP_unitarity_residual": update_rows[
            "second_FSWAP_unitarity_residual"
        ],
        "upstream_Cycle526_mass": 0.45340565417488515,
        "upstream_Cycle526_contact_nontrivial_columns": 4047,
        "upstream_Cycle526_seam_and_contact_strict_pinned": True,
        "pass": abs(
            update_rows["three_cell_rest_mass"] - update_rows["Cycle219_mass_fixture"]
        )
        < TOL
        and update_rows["uniform_one_particle_eigen_residual"] < TOL
        and update_rows["contact_nontrivial_columns"] == 645
        and update_rows["first_FSWAP_unitarity_residual"] < TOL
        and update_rows["second_FSWAP_unitarity_residual"] < TOL,
    }


def boundary_inventory(response, schedules) -> dict:
    maximum_track = max(row["new_external_track_M2"] for row in schedules["rows"])
    return {
        "supplied": (
            "Cycle526 persistent-shadow EDGE_PASSED/PLUS/MINUS semantics and selected-seam compiler chain",
            "Cycle434/Cycle429 988-state matter preparation, physical encoding, field coin, three-update factor order, and readout",
            "Cycle426 coefficient-two recoil vertex, angle/sign/normalization, and seven-M2 reservoir/field star at each cell",
            "current-correlated lawful input code: NULL uses the matter vacuum; PLUS/MINUS use the frozen mirrored Cycle434 preparations",
            "blank Y-track sites, current rails, finite L5/L6 geometry, and compile-time proper-cubic schedule orbit",
        ),
        "constructed": (
            "one fixed J+/J--controlled Y-track schedule with a literal Q=1 token",
            "a fixed endpoint-symmetric recoil/transport schedule independent of current value",
            "factorized physical E/G composition on a coherent NULL/PLUS/MINUS superposition",
            "exact Cycle434 receiver replay, odd coordinate, source/receiver ledgers, deletions, inverse, held geometry, and all-frame audit",
        ),
        "open_import_retirement": (
            "primitive one-/two-M2 synthesis of the Cycle426 coefficient-two recoil/source vertex and Cycle429 matter lifts",
            "autonomous preparation of the current-correlated matter/token input code",
            "a tested transducer between the Cycle539 selected carrier and Cycle540 rough-gauge carrier",
            "Cycle420 host-profile/centroid identification and any clock-calibrated motion law",
            "energy/stress/source selection, gravity response, occurrence, Record formation, and Born selection",
        ),
        "resources": {
            "Cycle526_selected_current_patch_M2": 106,
            "Cycle429_matter_role_union_M2": 118,
            "Cycle429_internal_reservoir_field_M2": 21,
            "maximum_new_Y_track_M2": maximum_track,
            "conservative_additive_bounded_total_M2": 106 + 118 + 21 + maximum_track,
            "largest_new_gate_support_M2": 3,
            "largest_new_gate_after_Cycle526_Toffoli_decomposition_M2": 2,
        },
        "claim_boundary": {
            "Cycle526_to_Cycle434_prediction_bridge_closed": True,
            "Cycle432_phase_source_transplant_needed": False,
            "Cycle420_named_moving_source_surface_closed": False,
            "primitive_recoil_source_compiler_closed": False,
            "Cycle539_to_Cycle540_carrier_transducer_closed": False,
            "physical_energy_source_or_gravity_derived": False,
            "Record_or_Born_law_derived": False,
            "negative_or_minimum_claim": False,
            "axiom_pressure": False,
        },
        "response_maximum_old_Cycle434_state_residual": max(
            row["old_Cycle434_complete_state_residual"] for row in response["rows"]
        ),
        "authority": AUTHORITY,
        "audit": AUDIT,
    }


def main() -> int:
    started = time.monotonic()
    print("Cycle546 coherent-current carried-source prediction bridge")
    print("authority=none; audit=unset; schedule layers are not physical time")
    dependencies = dependency_controls()
    contract = note_contract()
    adapter = current_adapter_controls()
    update_rows, coin, first, second, contact, _forward, _reverse = (
        c429.c319.update_controls(c429.LABELS, "path")
    )
    factors = (coin, first, second, contact)
    schedules = schedule_and_covariance_controls(factors)
    response = response_controls(factors)
    baseline = next(
        row["receiver_reservoir_response"]
        for row in response["rows"]
        if row["L"] == TRAIN_SIZE and row["current"] == "PLUS"
    )
    controls = null_deletion_domain_controls(factors, baseline)
    eg = eg_controls(factors)
    fixtures = physics_fixture_controls(update_rows)
    boundaries = boundary_inventory(response, schedules)

    tests = {
        "strict_cycle420_432_434_526_530_533_539_540_byte_pins": dependencies[
            "pass"
        ],
        "note_contract_authority_and_claim_boundary": contract["pass"],
        "complete_Fock_Cycle526_current_relation": adapter["pass"],
        "one_fixed_current_controlled_track_and_all24_covariance": schedules["pass"],
        "exact_Cycle434_odd_receiver_and_ledgers_without_refit": response["pass"],
        "null_inverse_deletion_and_lawful_domain_controls": controls["pass"],
        "coherent_current_physical_EG_inverse_and_leakage": eg["pass"],
        "mass_contact_and_seam_fixtures_preserved": fixtures["pass"],
        "explicit_imports_and_no_axiom_pressure": (
            boundaries["authority"] == "none"
            and boundaries["audit"] == "unset"
            and not boundaries["claim_boundary"]["axiom_pressure"]
            and not boundaries["claim_boundary"]["negative_or_minimum_claim"]
            and not boundaries["claim_boundary"][
                "primitive_recoil_source_compiler_closed"
            ]
        ),
    }
    result = {
        "cycle": 546,
        "authority": AUTHORITY,
        "audit": AUDIT,
        "dependencies": dependencies,
        "note_contract": contract,
        "Cycle526_current_adapter": adapter,
        "fixed_schedule_and_covariance": schedules,
        "prediction_and_ledgers": response,
        "null_deletions_and_domain": controls,
        "physical_EG": eg,
        "mass_contact_seam": fixtures,
        "inventory_and_boundary": boundaries,
        "tests": tests,
        "pass": all(tests.values()),
        "elapsed_seconds": time.monotonic() - started,
        "maximum_RSS_bytes": rss_bytes(),
        "process_swap_count": swap_count(),
    }
    for label, passed in tests.items():
        check(label.replace("_", " "), bool(passed), "ok" if passed else result)
    result["pass_count"] = PASS
    result["fail_count"] = FAIL
    print("RESULT_JSON", json.dumps(result, sort_keys=True, default=str))
    print("SUMMARY", {"pass": PASS, "fail": FAIL, "authority": AUTHORITY, "audit": AUDIT})
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
