#!/usr/bin/env python3
"""Cycle 843 v2: the honestly named pulse coincidence state.

The landed Cycle-719 controller core is the sole executable science
dependency.  Current-worktree Cycle-834/838 sources are SHA-pinned text/AST
controls only.  Cycle-832/833/835 sibling results are copied as small,
SHA-pinned provenance records and are never imported or executed.  V2 adopts
the independent identity ruling while retaining the exact phase and selector
results.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 200 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle834_k3_backbone_2026_07_28.py",
    "scripts/frontier_cycle834_backbone_independent_check_2026_07_28.py",
    "scripts/frontier_cycle838_k3_trio_forecast_2026_07_28.py",
    "scripts/frontier_cycle838_forecast_independent_check_2026_07_28.py",
)

import ast
from collections import Counter
from hashlib import sha1, sha256
import importlib.abc
from itertools import combinations
import json
from pathlib import Path
import subprocess
import sys
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

CORE_PATH = AUDIT_INPUT_PATHS[0]
TEXT_AST_ONLY_PATHS = AUDIT_INPUT_PATHS[1:]
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "8ed75c4e6f19fa5e8a9492225aae681ab85017dcfac00f8ab109b7c587aeddaa",
    AUDIT_INPUT_PATHS[2]:
        "4e8d50c7b0922628bb7c825657f84570a7575479e4ad7764a3808edfe67872d8",
    AUDIT_INPUT_PATHS[3]:
        "ea668b4d0be960622cd10d4e16b3cd1056d343db80ee6845407ca6ddb3e604c0",
    AUDIT_INPUT_PATHS[4]:
        "9052923ebfce6c365d2c9454ac9bb4858b782349009f65d552579846f5d1ebec",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    AUDIT_INPUT_PATHS[1]: "89d4506c6df9738bf0458027ab76cc9d2f9710ab",
    AUDIT_INPUT_PATHS[2]: "2cd06b93956a62a007e1f4984b4cf1ba98e607fe",
    AUDIT_INPUT_PATHS[3]: "2f89c8eb911375bed58b1126e9f5f7b860ead20a",
    AUDIT_INPUT_PATHS[4]: "7a215e0e7499a4e7b1af64f1f4045bd3d330b7cc",
}
COPIED_SIBLING_SOURCES = (
    {
        "package": "cycle832",
        "commit": "f3ec9213b4b02457bfc8bc092bf25510297e2813",
        "path":
            "scripts/frontier_cycle832_cohort_moment_law_2026_07_28.py",
        "sha256":
            "0db01e80084af4dbb52c74a0a055984edf8ab818f2c8ba8a99c1f6a3fc15bb3e",
        "git_blob": "d666f5c301ffe6b6508f3636b15814a662bfbe8e",
    },
    {
        "package": "cycle832_checker",
        "commit": "f3ec9213b4b02457bfc8bc092bf25510297e2813",
        "path":
            "scripts/frontier_cycle832_moment_law_independent_check_2026_07_28.py",
        "sha256":
            "80f898ece92e7bcb1728761746d52192809810eb84ccff98337609af90a59a28",
        "git_blob": "a421f7736e97b86b0fb5a1672ebccf43209ce9e2",
    },
    {
        "package": "cycle833",
        "commit": "dca1e252ec1981755f9e54837c1a9f0e2503ccc2",
        "path":
            "scripts/frontier_cycle833_funnel_family_2026_07_28.py",
        "sha256":
            "bd08f5f503e532c724e6ae28915ba2f0b4202360bbe01458924d689e27c79174",
        "git_blob": "b3512e0c3e8acdec7bc3f1cfb4e5bf1a236f8fda",
    },
    {
        "package": "cycle833_checker",
        "commit": "dca1e252ec1981755f9e54837c1a9f0e2503ccc2",
        "path":
            "scripts/frontier_cycle833_funnel_independent_check_2026_07_28.py",
        "sha256":
            "06fc7abc20dcbeba0ecd6234f366b838c45c91e1790599521e45b500192dde6b",
        "git_blob": "82af4734b13c50cb253c902b831734e7f6562fa1",
    },
    {
        "package": "cycle835",
        "commit": "1522d92ec66956621093273f75eb4e4e4d366f7e",
        "path":
            "scripts/frontier_cycle835_register_mechanism_2026_07_28.py",
        "sha256":
            "6b8c26ff77d99225aaa985c645aeee9fa1fb3db19517aec727ff38e0cbcc03f5",
        "git_blob": "a9bfc3d151a591b3d0a4ba06acaa30ed04ff7e67",
    },
)
COPIED_MODULES = tuple(
    Path(row["path"]).stem for row in COPIED_SIBLING_SOURCES
)
BLOCKLISTED_MODULES = (
    *(Path(path).stem for path in TEXT_AST_ONLY_PATHS),
    *COPIED_MODULES,
)


class _PrimaryFirewall(importlib.abc.MetaPathFinder):
    """Fail closed if a text/AST-only or copied primary is imported."""

    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(
        self,
        fullname: str,
        path: object = None,
        target: object = None,
    ) -> None:
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids import of {fullname}")
        return None


FIREWALL = _PrimaryFirewall()
sys.meta_path.insert(0, FIREWALL)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


State = tuple[int, ...]
Pair = tuple[int, int]
Key = tuple[int, Pair]

RING_STATIONS = 11
FIXTURE_BANKS = 2
STATE_BITS = 5815
SAMPLED_PERIODS = 12
EXPECTED_BRANCH = "physics-loop/toe-close-blockC25-20260729"
EXPECTED_BASE = "7a42ba01f4f549550b1dcfadbefb9aaedce1c0c3"
BACKBONE: tuple[Pair, ...] = (
    (1, 6), (1, 7), (2, 7), (2, 8), (3, 8),
    (3, 9), (4, 9), (4, 10), (5, 10),
)
EVENT3_KEYS: tuple[Key, ...] = tuple((3, pair) for pair in BACKBONE)
EXPECTED_PHASE_PARTITIONS = (
    (1, 3, 3, 2),
    (1, 3, 3, 2),
    (9,),
)
EXPECTED_COINCIDENCE_SHA256 = (
    "4a7ce9fd4e9ebfdbd8580c33122d9e87c3896b24ef196e34bec49e233d044375"
)
EXPECTED_CYCLE833_S0_PRIME_SHA256 = (
    "d874aeeb1d4e5ca29b806886314c796ac32e6658b21f888d8e2aa01044905c12"
)
V1_IDENTITY_RETRACTION = (
    "the v1 \"is exactly S0'\" claim RETRACTED as a naming collision"
)
REGISTER_FIELDS = (
    "source.LEFT_ENDPOINT",
    "source.RIGHT_ENDPOINT",
    "bank0.cell0.pred[0]",
    "bank0.cell0.pred[1]",
    "bank0.cell0.pred[2]",
    "bank0.cell0.pred[3]",
    "bank0.cell0.pred[4]",
    "bank0.cell0.pred[5]",
    "bank0.cell0.rotor_before[0]",
    "bank0.cell0.rotor_before[1]",
    "bank0.cell0.rotor_before[2]",
    "bank0.cell0.rotor_before[3]",
    "bank0.cell0.rotor_after[0]",
    "bank0.cell0.rotor_after[1]",
    "bank0.cell0.rotor_after[2]",
    "bank0.cell0.rotor_after[3]",
    "bank0.cell0.carry",
    "bank0.cell0.orientation",
    "bank0.cell1.pred[0]",
    "bank0.cell1.pred[1]",
    "bank0.cell1.pred[2]",
    "bank0.cell1.pred[3]",
    "bank0.cell1.pred[4]",
    "bank0.cell1.pred[5]",
    "bank0.cell1.rotor_before[1]",
    "bank0.cell1.rotor_before[2]",
    "bank0.cell1.rotor_before[3]",
    "bank0.cell1.rotor_after[1]",
    "bank0.cell1.rotor_after[2]",
    "bank0.cell1.carry",
    "bank0.cell1.orientation",
    "bank0.HEAD[0]",
    "bank0.HEAD[1]",
    "bank0.HEAD[2]",
    "bank0.HEAD[3]",
    "bank0.HEAD[4]",
    "bank0.HEAD[5]",
    "bank0.ROTOR[1]",
    "bank0.ROTOR[2]",
)


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def state_sha256(state: State) -> str:
    return sha256(bytes(state)).hexdigest()


def orbit_word(
    program: tuple[object, ...],
    pair: Pair,
) -> tuple[object, ...]:
    rows = []
    for movement_tick in range(len(program)):
        live = {
            (pair[0] + movement_tick) % len(program),
            (pair[1] + movement_tick) % len(program),
        }
        for station, macro in enumerate(program):
            if station in live:
                rows.extend(K.mapped_macro(macro))
    return tuple(rows)


def build_event3_family() -> dict[str, object]:
    program = K.interleaved_program(FIXTURE_BANKS)
    words = {pair: orbit_word(program, pair) for pair in BACKBONE}
    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    state = K.M.pack_state(banks, links)
    allocator = K.M.global_allocator_word(FIXTURE_BANKS)
    epochs = []
    for event in range(2 * FIXTURE_BANKS):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = K.M.prepare_endpoint(state, direction)
        epochs.append(before)
        state = K.A.apply_semantic(before, allocator)
    event3_states = {
        (3, pair): K.A.apply_semantic(epochs[3], words[pair])
        for pair in BACKBONE
    }
    rail_rows = []
    for pair in BACKBONE:
        after, rail_a, rail_b, trace = K.run_orbit(
            epochs[3], program, token_positions=pair
        )
        rail_rows.append({
            "key": (3, pair),
            "A_token_positions": tuple(
                station for station, bit in enumerate(rail_a) if bit
            ),
            "B_token_positions": tuple(
                station for station, bit in enumerate(rail_b) if bit
            ),
            "trace_ticks": len(trace),
            "composition_exact": after == event3_states[(3, pair)],
        })
    return {
        "program": program,
        "words": words,
        "epoch_states": tuple(epochs),
        "pulse_coincidence_state": epochs[3],
        "states": event3_states,
        "rail_rows": tuple(rail_rows),
        "summary": {
            "keys": len(event3_states),
            "state_bits": len(epochs[3]),
            "word_gate_counts": tuple(sorted({
                len(word) for word in words.values()
            })),
            "pulse_coincidence_state_weight": sum(epochs[3]),
            "all_rail_compositions_exact":
                all(row["composition_exact"] for row in rail_rows),
        },
    }


def _bank_wire_aliases() -> dict[int, tuple[str, ...]]:
    aliases: dict[int, list[str]] = {
        wire: [] for wire in range(K.A.N)
    }
    for cell, layout in enumerate(K.A.CELLS):
        for field, value in layout.items():
            if field == "payload":
                continue
            if isinstance(value, tuple):
                for index, wire in enumerate(value):
                    aliases[int(wire)].append(
                        f"cell{cell}.{field}[{index}]"
                    )
            else:
                aliases[int(value)].append(f"cell{cell}.{field}")
    for register in ("HEAD", "ROTOR", "TOKEN", "FRESH", "ZERO_WORK"):
        for index, wire in enumerate(getattr(K.A, register)):
            aliases[int(wire)].append(f"{register}[{index}]")
    for register in (
        "POINTER", "U_TO_V", "V_TO_U", "BINDER", "ACTUAL", "ADMISS",
        "LAW", "TOKEN_OK", "DIRECTION_OK", "ENABLE_TARGET",
    ):
        aliases[int(getattr(K.A, register))].append(register)
    return {wire: tuple(names) for wire, names in aliases.items()}


BANK_WIRE_ALIASES = _bank_wire_aliases()
SOURCE_NAMES = {
    K.R3.X.LEFT_ENDPOINT: "LEFT_ENDPOINT",
    K.R3.X.RIGHT_ENDPOINT: "RIGHT_ENDPOINT",
    K.R3.X.SOURCE_POINTER: "SOURCE_POINTER",
}


def wire_name(wire: int) -> str:
    if wire < K.M.R12.SOURCE_WIDTH:
        return f"source.{SOURCE_NAMES.get(wire, f'wire[{wire}]')}"
    for bank, base in enumerate(
        K.M.R12.BANK_BASES[:FIXTURE_BANKS]
    ):
        if base <= wire < base + K.A.N:
            local = wire - base
            aliases = BANK_WIRE_ALIASES[local]
            label = "|".join(aliases) if aliases else f"wire[{local}]"
            return f"bank{bank}.{label}"
    for link, base in enumerate(
        K.M.R12.LINK_BASES[:FIXTURE_BANKS - 1]
    ):
        if base <= wire < base + K.B.LINK_WIDTH:
            return f"link{link}.wire[{wire - base}]"
    return f"unused_padding.wire[{wire}]"


WIRE_NAMES = tuple(map(wire_name, range(STATE_BITS)))
WIRE_BY_NAME = {name: wire for wire, name in enumerate(WIRE_NAMES)}


def state_anatomy(state: State) -> dict[str, object]:
    banks, links = K.M.unpack_state(state, FIXTURE_BANKS)
    occupancy = tuple(
        tuple(bank[int(layout["valid"])] for layout in K.A.CELLS)
        for bank in banks
    )
    tokens = tuple(
        tuple(bank[wire] for wire in K.A.TOKEN)
        for bank in banks
    )
    return {
        "state_sha256": state_sha256(state),
        "hamming_weight": sum(state),
        "source_active_fields": tuple(
            wire_name(wire)
            for wire in range(K.M.R12.SOURCE_WIDTH)
            if state[wire]
        ),
        "source_weight": sum(state[:K.M.R12.SOURCE_WIDTH]),
        "bank_hamming_weights": tuple(map(sum, banks)),
        "occupancy": occupancy,
        "occupancy_weights": tuple(map(sum, occupancy)),
        "tokens": tokens,
        "token_weights": tuple(map(sum, tokens)),
        "link_active_fields": tuple(
            f"link{link}.wire[{wire}]"
            for link, row in enumerate(links)
            for wire, bit in enumerate(row) if bit
        ),
        "link_hamming_weights": tuple(map(sum, links)),
        "component_parities": {
            "full": sum(state) % 2,
            "source": sum(state[:K.M.R12.SOURCE_WIDTH]) % 2,
            **{
                f"bank{index}": sum(bank) % 2
                for index, bank in enumerate(banks)
            },
            **{
                f"link{index}": sum(link) % 2
                for index, link in enumerate(links)
            },
        },
    }


def state_partition(
    states: tuple[State, ...],
) -> tuple[tuple[int, ...], ...]:
    groups: dict[State, list[int]] = {}
    for lane, state in enumerate(states):
        groups.setdefault(state, []).append(lane)
    return tuple(tuple(group) for group in groups.values())


def exact_diff(left: State, right: State) -> dict[str, object]:
    wires = tuple(
        wire for wire, values in enumerate(zip(left, right))
        if values[0] != values[1]
    )
    component_xor_weights = Counter(
        WIRE_NAMES[wire].split(".", 1)[0] for wire in wires
    )
    return {
        "xor_weight": len(wires),
        "component_xor_weights": dict(sorted(component_xor_weights.items())),
        "bank_xor_weights": {
            f"bank{bank}": component_xor_weights.get(f"bank{bank}", 0)
            for bank in range(FIXTURE_BANKS)
        },
        "wire_indices": wires,
        "named_transitions": tuple(
            (WIRE_NAMES[wire], left[wire], right[wire])
            for wire in wires
        ),
        "left_weight": sum(left),
        "right_weight": sum(right),
    }


def meeting_geometry(pair: Pair) -> dict[str, object]:
    left, right = pair
    if (right - left) % RING_STATIONS == 5:
        short_direction = 1
    elif (left - right) % RING_STATIONS == 5:
        short_direction = -1
    else:
        raise AssertionError(("not separation five", pair))
    short_arc = tuple(
        (left + short_direction * offset) % RING_STATIONS
        for offset in range(6)
    )
    long_arc = tuple(
        (left - short_direction * offset) % RING_STATIONS
        for offset in range(7)
    )
    centers = tuple(sorted(set(short_arc[2:4] + long_arc[3:4])))
    a_positions = tuple(
        (station + 3) % RING_STATIONS for station in pair
    )
    return {
        "pair": pair,
        "meeting_times_short_long": (3, 3),
        "meeting_center_union": centers,
        "A_token_positions_at_meet": a_positions,
        "B_token_positions_at_meet": (),
        "both_A_tokens_on_center_union":
            all(station in centers for station in a_positions),
        "token_collision": len(set(a_positions)) != 2,
    }


def replay_phases(family: dict[str, object]) -> dict[str, object]:
    words = family["words"]
    states_by_key = family["states"]
    assert isinstance(words, dict)
    assert isinstance(states_by_key, dict)
    states = tuple(states_by_key[key] for key in EVENT3_KEYS)
    phases = [states]
    for _movement in range(3):
        states = tuple(
            K.A.apply_semantic(state, words[key[1]])
            for key, state in zip(EVENT3_KEYS, states)
        )
        phases.append(states)
    return {
        "phase_states": tuple(phases[:3]),
        "closure_states": phases[3],
        "all_close_at_movement_3": phases[3] == phases[0],
    }


def phase_state_certificate(
    family: dict[str, object],
    replay: dict[str, object],
    comparisons: dict[str, object],
) -> dict[str, object]:
    phases = replay["phase_states"]
    assert isinstance(phases, tuple)
    phase_rows = []
    for phase, states in enumerate(phases):
        partition = state_partition(states)
        phase_rows.append({
            "phase_mod_3": phase,
            "key_state_rows": tuple({
                "key": key,
                "anatomy": state_anatomy(state),
            } for key, state in zip(EVENT3_KEYS, states)),
            "partition_key_groups": tuple(
                tuple(EVENT3_KEYS[lane] for lane in group)
                for group in partition
            ),
            "component_sizes": tuple(map(len, partition)),
            "distinct_state_count": len(partition),
        })
    same_key_diffs = tuple({
        "key": EVENT3_KEYS[lane],
        "left_phase": left_phase,
        "right_phase": right_phase,
        "diff": exact_diff(
            phases[left_phase][lane],
            phases[right_phase][lane],
        ),
    } for lane in range(len(EVENT3_KEYS))
      for left_phase, right_phase in combinations(range(3), 2))
    coincidence = phases[2][0]
    coincidence_seed = family["pulse_coincidence_state"]
    comparison_states = comparisons["objects"]
    assert isinstance(coincidence_seed, tuple)
    assert isinstance(comparison_states, dict)
    cycle833_s0_prime = comparison_states["S0'"]
    identity_diff = exact_diff(coincidence, cycle833_s0_prime)
    exact = (
        tuple(row["component_sizes"] for row in phase_rows)
        == EXPECTED_PHASE_PARTITIONS
        and all(state == coincidence for state in phases[2])
        and coincidence == coincidence_seed
        and state_sha256(coincidence) == EXPECTED_COINCIDENCE_SHA256
        and sum(coincidence) == 59
        and coincidence != cycle833_s0_prime
        and state_sha256(cycle833_s0_prime)
        == EXPECTED_CYCLE833_S0_PRIME_SHA256
        and sum(cycle833_s0_prime) == 47
        and identity_diff["xor_weight"] == 32
        and identity_diff["component_xor_weights"]
        == {"bank0": 18, "bank1": 14}
        and replay["all_close_at_movement_3"]
        and len(same_key_diffs) == 27
        and all(row["diff"]["xor_weight"] > 0 for row in same_key_diffs)
    )
    return {
        "verdict": "PASS" if exact else "FAIL",
        "certificate": "A — rename and retraction",
        "retraction": V1_IDENTITY_RETRACTION,
        "identity_ruling":
            "DISTINCT: the pulse coincidence state is a new object, not "
            "the SHA-pinned Cycle-833 S0'.",
        "allowed_object_phrase": "pulse coincidence state",
        "definition":
            "all 27 full 5815-bit event-3 backbone boundary states",
        "phase_rows": tuple(phase_rows),
        "same_key_pairwise_diffs_across_phases": same_key_diffs,
        "meeting_geometry_by_key": tuple(
            meeting_geometry(key[1]) for key in EVENT3_KEYS
        ),
        "coincidence_phase_mod_3": 2,
        "coincidence_state_anatomy": state_anatomy(coincidence),
        "cycle833_S0_prime_anatomy": state_anatomy(cycle833_s0_prime),
        "coincidence_vs_cycle833_S0_prime": identity_diff,
        "coincidence_is_cycle833_S0_prime":
            coincidence == cycle833_s0_prime,
        "period_3_closure_exact": replay["all_close_at_movement_3"],
        "pass": exact,
    }


def pack_states(states: tuple[State, ...]) -> list[int]:
    return [
        sum(state[wire] << lane for lane, state in enumerate(states))
        for wire in range(len(states[0]))
    ]


def unpack_lane(columns: list[int], lane: int) -> State:
    return tuple((column >> lane) & 1 for column in columns)


def compiled_word(
    word: tuple[object, ...],
) -> tuple[tuple[int, int, int, int], ...]:
    rows = []
    for gate in word:
        if len(set(gate.wires)) != len(gate.wires):
            raise AssertionError(("repeated landed gate wire", gate))
        if gate.kind == "X":
            rows.append((0, gate.wires[0], 0, 0))
        elif gate.kind == "CNOT":
            rows.append((1, gate.wires[0], gate.wires[1], 0))
        elif gate.kind == "TOF":
            rows.append((2, gate.wires[0], gate.wires[1], gate.wires[2]))
        else:
            raise AssertionError(("non-reversible gate", gate))
    return tuple(rows)


def advance_packed(
    columns: list[int],
    schedule: tuple[tuple[int, int, int, int], ...],
    all_lanes: int,
) -> None:
    for kind, first, second, third in schedule:
        if kind == 0:
            columns[first] ^= all_lanes
        elif kind == 1:
            columns[second] ^= columns[first] & all_lanes
        else:
            columns[third] ^= (
                columns[first] & columns[second] & all_lanes
            )


def reconstruct_comparison_objects(
    family: dict[str, object],
) -> dict[str, object]:
    """Rebuild the three funnels and two named post-S* skeletons."""

    pulse_coincidence_state = family["pulse_coincidence_state"]
    assert isinstance(pulse_coincidence_state, tuple)
    events = (0, 2, 1)
    witness = BACKBONE[0]
    words = family["words"]
    epochs = family["epoch_states"]
    assert isinstance(words, dict)
    assert isinstance(epochs, tuple)
    initial_primary = tuple(
        K.A.apply_semantic(epochs[event], words[witness])
        for event in events
    )
    initial_states = initial_primary + initial_primary
    columns = pack_states(initial_states)
    schedule = compiled_word(words[witness])
    all_lanes = (1 << len(initial_states)) - 1
    capture_at = {
        14739: "FUNNEL_EVENT0_WEIGHT44",
        14744: "SSTAR_POST_5_WEIGHT51",
        14748: "SSTAR_POST_9_WEIGHT57",
        33190: "FUNNEL_EVENT2_WEIGHT45",
        51110: "FUNNEL_EVENT1_WEIGHT46",
    }
    captured: dict[str, State] = {}
    duplicate_rows = []
    for movement in range(1, max(capture_at) + 1):
        advance_packed(columns, schedule, all_lanes)
        if movement in capture_at:
            name = capture_at[movement]
            event_lane = (
                0 if movement < 20000
                else 1 if movement < 40000
                else 2
            )
            captured[name] = unpack_lane(columns, event_lane)
            duplicate_rows.append({
                "object": name,
                "movement": movement,
                "primary_sha256":
                    state_sha256(unpack_lane(columns, event_lane)),
                "duplicate_sha256":
                    state_sha256(unpack_lane(columns, event_lane + 3)),
                "exact":
                    unpack_lane(columns, event_lane)
                    == unpack_lane(columns, event_lane + 3),
            })
    expected_weights = {
        "FUNNEL_EVENT0_WEIGHT44": 44,
        "FUNNEL_EVENT2_WEIGHT45": 45,
        "FUNNEL_EVENT1_WEIGHT46": 46,
        "SSTAR_POST_5_WEIGHT51": 51,
        "SSTAR_POST_9_WEIGHT57": 57,
    }
    expected_funnel_hashes = {
        "FUNNEL_EVENT0_WEIGHT44":
            "cdf7e03092c6278b686c1f0edb9ebd716f4a285b1eabc8a7e2780695284a8f1a",
        "FUNNEL_EVENT2_WEIGHT45":
            "0015151ee4b751c35a5671fbb4f301d8569e78fc5a7ebe9f77372865b153c99b",
        "FUNNEL_EVENT1_WEIGHT46":
            "797fa122a629177c00c707aff4857d01bbad16b078983e3a6f1f5b632e094a41",
    }
    cycle833_s1 = captured["FUNNEL_EVENT1_WEIGHT46"]
    head1 = WIRE_BY_NAME["bank0.HEAD[1]"]
    cycle833_s0_prime_bits = list(cycle833_s1)
    cycle833_s0_prime_bits[head1] ^= 1
    cycle833_s0_prime = tuple(cycle833_s0_prime_bits)
    public_objects = {
        "S*": captured["FUNNEL_EVENT0_WEIGHT44"],
        "S2": captured["FUNNEL_EVENT2_WEIGHT45"],
        "S1": cycle833_s1,
        "S0'": cycle833_s0_prime,
        "station-0 funnel weight 57":
            captured["SSTAR_POST_9_WEIGHT57"],
        "station-0 funnel weight 51":
            captured["SSTAR_POST_5_WEIGHT51"],
    }
    rows = tuple({
        "object": public_name,
        "construction": (
            "Cycle-833 funnel boundary"
            if public_name in ("S*", "S2", "S1")
            else "Cycle-833 prediction S0' := map(S1)"
            if public_name == "S0'"
            else public_name
        ),
        "anatomy": state_anatomy(state),
    } for public_name, state in public_objects.items())
    iterates = []
    iterate = cycle833_s0_prime
    for power in range(1, 9):
        updated = list(iterate)
        updated[head1] ^= 1
        iterate = tuple(updated)
        iterates.append({
            "power": power,
            "sha256": state_sha256(iterate),
            "weight": sum(iterate),
            "is_S1": iterate == cycle833_s1,
            "is_S0_prime": iterate == cycle833_s0_prime,
            "is_pulse_coincidence_state":
                iterate == pulse_coincidence_state,
        })
    exact = (
        set(captured) == set(expected_weights)
        and all(
            sum(captured[name]) == weight
            for name, weight in expected_weights.items()
        )
        and all(
            state_sha256(captured[name]) == expected_hash
            for name, expected_hash in expected_funnel_hashes.items()
        )
        and all(row["exact"] for row in duplicate_rows)
        and sum(cycle833_s0_prime) == 47
        and state_sha256(cycle833_s0_prime)
        == EXPECTED_CYCLE833_S0_PRIME_SHA256
        and all(
            row["is_S1"] if row["power"] % 2 else row["is_S0_prime"]
            for row in iterates
        )
        and not any(
            row["is_pulse_coincidence_state"] for row in iterates
        )
    )
    return {
        "objects": public_objects,
        "public_rows": rows,
        "expected_weights": expected_weights,
        "expected_funnel_sha256": expected_funnel_hashes,
        "determinism_rows": tuple(duplicate_rows),
        "map_relationship": {
            "operation": "XOR bank0.HEAD[1]",
            "exact_orbit": "S1 <-> S0'",
            "positive_power_rows": tuple(iterates),
            "never_reaches_pulse_coincidence_state": not any(
                row["is_pulse_coincidence_state"] for row in iterates
            ),
        },
        "pass": exact,
    }


def projection(state: State, wires: tuple[int, ...]) -> int:
    return sum(state[wire] << index for index, wire in enumerate(wires))


def selector_certificate(
    family: dict[str, object],
    replay: dict[str, object],
    comparisons: dict[str, object],
) -> dict[str, object]:
    phases = replay["phase_states"]
    assert isinstance(phases, tuple)
    coincidence = phases[2][0]
    noncoincidence_states = tuple(dict.fromkeys(
        (*phases[0], *phases[1])
    ))
    diff_sets = tuple(
        frozenset(
            wire for wire, values in enumerate(zip(coincidence, state))
            if values[0] != values[1]
        )
        for state in noncoincidence_states
    )
    universal_difference = frozenset.intersection(*diff_sets)
    difference_union = frozenset.union(*diff_sets)
    register_wires = tuple(WIRE_BY_NAME[name] for name in REGISTER_FIELDS)
    register_set = frozenset(register_wires)
    complement_wires = tuple(
        wire for wire in range(STATE_BITS) if wire not in register_set
    )
    boundary_states = tuple(
        state for phase_states in phases for state in phase_states
    )
    register_values = tuple(
        projection(state, register_wires) for state in boundary_states
    )
    singleton_selectors = tuple(
        {
            "wire_index": wire,
            "field": WIRE_NAMES[wire],
            "coincidence_value": coincidence[wire],
            "noncoincidence_value": noncoincidence_states[0][wire],
        }
        for wire in complement_wires
        if all(
            state[wire] == coincidence[wire]
            for state in phases[2]
        )
        and all(
            state[wire] == 1 - coincidence[wire]
            for state in (*phases[0], *phases[1])
        )
    )
    anatomy_rows = tuple(
        state_anatomy(state) for state in boundary_states
    )
    occupancy_values = {
        compact(row["occupancy"]) for row in anatomy_rows
    }
    token_values = {compact(row["tokens"]) for row in anatomy_rows}
    geometry_rows = tuple(meeting_geometry(pair) for pair in BACKBONE)
    source_pointer = WIRE_BY_NAME["source.SOURCE_POINTER"]
    link_token = WIRE_BY_NAME["link0.wire[0]"]
    parity_rows = tuple({
        "phase_mod_3": phase,
        "key": key,
        "full_weight_parity": sum(state) % 2,
        "source_component_parity":
            sum(state[:K.M.R12.SOURCE_WIDTH]) % 2,
        "link0_component_parity": (
            sum(K.M.unpack_state(state, FIXTURE_BANKS)[1][0]) % 2
        ),
    } for phase, phase_states in enumerate(phases)
      for key, state in zip(EVENT3_KEYS, phase_states))
    full_parity_selects = all(
        row["full_weight_parity"] == sum(coincidence) % 2
        for row in parity_rows if row["phase_mod_3"] == 2
    ) and all(
        row["full_weight_parity"] != sum(coincidence) % 2
        for row in parity_rows if row["phase_mod_3"] != 2
    )
    component_parity_selects = {
        "source": all(
            (row["source_component_parity"] == 0)
            == (row["phase_mod_3"] == 2)
            for row in parity_rows
        ),
        "link0": all(
            (row["link0_component_parity"] == 0)
            == (row["phase_mod_3"] == 2)
            for row in parity_rows
        ),
    }
    comparison_states = comparisons["objects"]
    assert isinstance(comparison_states, dict)
    comparison_order = (
        "S*",
        "S2",
        "S1",
        "S0'",
        "station-0 funnel weight 57",
        "station-0 funnel weight 51",
    )
    comparison_rows = tuple({
        "object": name,
        "exact_match": coincidence == state,
        "exact_diff_from_coincidence": exact_diff(coincidence, state),
        "occupancy_equal":
            state_anatomy(coincidence)["occupancy"]
            == state_anatomy(state)["occupancy"],
        "tokens_equal":
            state_anatomy(coincidence)["tokens"]
            == state_anatomy(state)["tokens"],
    } for name in comparison_order
      for state in (comparison_states[name],))
    expected_census = {
        "S*": (
            44, 39, {"bank0": 23, "bank1": 14, "source": 2},
        ),
        "S2": (
            45, 40, {"bank0": 24, "bank1": 14, "source": 2},
        ),
        "S1": (
            46, 31, {"bank0": 17, "bank1": 14},
        ),
        "S0'": (
            47, 32, {"bank0": 18, "bank1": 14},
        ),
        "station-0 funnel weight 57": (
            57, 56,
            {"bank0": 28, "bank1": 24, "link0": 1, "source": 3},
        ),
        "station-0 funnel weight 51": (
            51, 50, {"bank0": 33, "bank1": 14, "source": 3},
        ),
    }
    census_exact = all(
        (
            row["exact_diff_from_coincidence"]["right_weight"],
            row["exact_diff_from_coincidence"]["xor_weight"],
            row["exact_diff_from_coincidence"]["component_xor_weights"],
        ) == expected_census[row["object"]]
        for row in comparison_rows
    )
    expected_singletons = (
        "source.SOURCE_POINTER",
        "link0.wire[0]",
    )
    exact = (
        comparisons["pass"]
        and len(noncoincidence_states) == 8
        and not register_set & difference_union
        and len(register_set) == len(REGISTER_FIELDS) == 39
        and len(set(register_values)) == 1
        and tuple(
            WIRE_NAMES[wire] for wire in sorted(universal_difference)
        ) == expected_singletons
        and tuple(row["field"] for row in singleton_selectors)
        == expected_singletons
        and len(occupancy_values) == len(token_values) == 1
        and all(
            row["both_A_tokens_on_center_union"]
            and not row["token_collision"]
            for row in geometry_rows
        )
        and not full_parity_selects
        and component_parity_selects == {
            "source": True, "link0": True
        }
        and all(
            state[source_pointer] + state[link_token] == 1
            for state in boundary_states
        )
        and census_exact
        and not any(row["exact_match"] for row in comparison_rows)
        and comparisons["map_relationship"][
            "never_reaches_pulse_coincidence_state"
        ]
    )
    return {
        "verdict": "PASS" if exact else "FAIL",
        "certificate": "B — relationship census",
        "coincidence_state_is":
            "DISTINCT_FROM_EVERY_CENSUSED_NAMED_STATE",
        "register_block": {
            "field_count": len(register_wires),
            "fields": REGISTER_FIELDS,
            "common_projection_hex":
                f"{register_values[0]:010x}",
            "common_projection_weight": register_values[0].bit_count(),
            "common_at_all_27_boundaries":
                len(set(register_values)) == 1,
            "difference_union_intersection": tuple(
                sorted(register_set & difference_union)
            ),
        },
        "complement": {
            "wire_count": len(complement_wires),
            "distinct_noncoincidence_state_count":
                len(noncoincidence_states),
            "diff_weight_by_distinct_state":
                tuple(map(len, diff_sets)),
            "exact_difference_union": tuple(
                (wire, WIRE_NAMES[wire])
                for wire in sorted(difference_union)
            ),
            "exact_universal_difference": tuple(
                (wire, WIRE_NAMES[wire])
                for wire in sorted(universal_difference)
            ),
            "minimal_single_wire_selectors": singleton_selectors,
            "selector_pair_is_redundant":
                len(singleton_selectors) == 2,
            "transfer_invariant":
                "source.SOURCE_POINTER + link0.wire[0] == 1",
        },
        "occupancy_geometry": {
            "boundary_occupancy_value_count": len(occupancy_values),
            "boundary_token_register_value_count": len(token_values),
            "selects_phase": False,
            "meet_rows": geometry_rows,
            "meet_geometry_phase_dependent": False,
        },
        "parity_structure": {
            "rows": parity_rows,
            "full_weight_parity_selects": full_parity_selects,
            "component_parity_selects": component_parity_selects,
            "reading":
                "source and link0 component parity are the same redundant "
                "logical transfer selector as the two physical wires",
        },
        "known_object_exact_comparisons": comparison_rows,
        "expected_weight_xor_and_component_splits": expected_census,
        "map_iterate_fact": comparisons["map_relationship"],
        "finding":
            "The pulse coincidence state is distinct from S*, S2, S1, "
            "S0', and both station-0 funnels. The Cycle-833 operation "
            "alternates S1 <-> S0' and never reaches it.",
        "pass": exact,
    }


def phase_law_certificate(
    family: dict[str, object],
) -> dict[str, object]:
    words = family["words"]
    family_states = family["states"]
    coincidence = family["pulse_coincidence_state"]
    assert isinstance(words, dict)
    assert isinstance(family_states, dict)
    assert isinstance(coincidence, tuple)
    source_pointer = WIRE_BY_NAME["source.SOURCE_POINTER"]
    link_token = WIRE_BY_NAME["link0.wire[0]"]
    states = tuple(family_states[key] for key in EVENT3_KEYS)
    initial_states = states
    phase_states = states
    boundary_rows = []
    for phase in range(3):
        boundary_rows.extend(
            (phase, key, state)
            for key, state in zip(EVENT3_KEYS, phase_states)
        )
        phase_states = tuple(
            K.A.apply_semantic(state, words[key[1]])
            for key, state in zip(EVENT3_KEYS, phase_states)
        )
    boundary_expected = tuple(
        phase == 2 for phase, _key, _state in boundary_rows
    )
    singleton_selectors = []
    for wire in range(STATE_BITS):
        for selected_value in (0, 1):
            observed = tuple(
                state[wire] == selected_value
                for _phase, _key, state in boundary_rows
            )
            if observed == boundary_expected:
                singleton_selectors.append({
                    "wire_index": wire,
                    "field": WIRE_NAMES[wire],
                    "selected_value": selected_value,
                })
    required_selectors = (
        (source_pointer, "source.SOURCE_POINTER", 1),
        (link_token, "link0.wire[0]", 0),
    )
    direction_rows = []
    for wire, name, selected_value in required_selectors:
        selected = tuple(
            state[wire] == selected_value
            for _phase, _key, state in boundary_rows
        )
        direction_rows.append({
            "selector": f"{name}={selected_value}",
            "coincidence_implies_selector": all(
                flag
                for flag, target in zip(selected, boundary_expected)
                if target
            ),
            "selector_implies_coincidence": all(
                target
                for flag, target in zip(selected, boundary_expected)
                if flag
            ),
            "true_positives": sum(
                flag and target
                for flag, target in zip(selected, boundary_expected)
            ),
            "false_positives": sum(
                flag and not target
                for flag, target in zip(selected, boundary_expected)
            ),
            "false_negatives": sum(
                not flag and target
                for flag, target in zip(selected, boundary_expected)
            ),
            "true_negatives": sum(
                not flag and not target
                for flag, target in zip(selected, boundary_expected)
            ),
        })
    rows = []
    period_closures = []
    for movement in range(3 * SAMPLED_PERIODS):
        expected = movement % 3 == 2
        for key, state in zip(EVENT3_KEYS, states):
            selector = (
                state[source_pointer] == 1
                and state[link_token] == 0
            )
            rows.append({
                "movement": movement,
                "period_index": movement // 3,
                "phase_mod_3": movement % 3,
                "key": key,
                "source.SOURCE_POINTER": state[source_pointer],
                "link0.wire[0]": state[link_token],
                "named_selector": selector,
                "is_pulse_coincidence_state": state == coincidence,
                "expected_coincidence_phase": expected,
                "biconditional_exact":
                    (state == coincidence)
                    == (state[source_pointer] == 1)
                    == (state[link_token] == 0)
                    == selector
                    == expected,
            })
        states = tuple(
            K.A.apply_semantic(state, words[key[1]])
            for key, state in zip(EVENT3_KEYS, states)
        )
        if (movement + 1) % 3 == 0:
            period_closures.append({
                "period_index": movement // 3,
                "all_nine_return_to_phase0":
                    states == initial_states,
                "phase0_state_stream_sha256": digest(tuple(
                    state_sha256(state) for state in states
                )),
            })
    exact = (
        len(rows) == 9 * 3 * SAMPLED_PERIODS
        and all(row["biconditional_exact"] for row in rows)
        and len(period_closures) == SAMPLED_PERIODS
        and all(
            row["all_nine_return_to_phase0"]
            for row in period_closures
        )
        and {
            row["phase_mod_3"]
            for row in rows if row["is_pulse_coincidence_state"]
        } == {2}
        and len(boundary_rows) == 27
        and sum(boundary_expected) == 9
        and tuple(
            (
                row["wire_index"],
                row["field"],
                row["selected_value"],
            )
            for row in singleton_selectors
        ) == required_selectors
        and all(
            row["coincidence_implies_selector"]
            and row["selector_implies_coincidence"]
            and row["true_positives"] == 9
            and row["false_positives"] == 0
            and row["false_negatives"] == 0
            and row["true_negatives"] == 18
            for row in direction_rows
        )
    )
    return {
        "verdict": "HOLDS_EXACTLY" if exact else "FAILS",
        "certificate": "C — kept selectors and phase law",
        "scope": "aligned completed orbit-word movement boundaries",
        "law":
            "For every event-3 backbone key and every integer movement m, "
            "state(m)=the pulse coincidence state iff "
            "source.SOURCE_POINTER=1 iff "
            "link0.wire[0]=0 iff m mod 3=2.",
        "sampled_period_count": SAMPLED_PERIODS,
        "sampled_boundary_rows": tuple(rows),
        "sampled_period_closures": tuple(period_closures),
        "forever_step": (
            "Each key returns exactly to its phase-0 full state after three "
            "applications of its fixed reversible word.  Determinism then "
            "repeats the verified three-boundary word for every integer "
            "period; this is finite-state induction, not extrapolation."
        ),
        "single_wire_corollaries": (
            "pulse coincidence state iff source.SOURCE_POINTER=1",
            "pulse coincidence state iff link0.wire[0]=0",
        ),
        "all_minimal_single_wire_selectors":
            tuple(singleton_selectors),
        "minimality":
            "The empty predicate cannot select exactly 9 of 27 rows; each "
            "listed one-wire biconditional has minimum cardinality.",
        "selector_directions_across_27_phase_states":
            tuple(direction_rows),
        "dense_gate_scope_warning":
            "No claim is made away from aligned movement boundaries.",
        "pass": exact,
    }


def git_blob(payload: bytes) -> str:
    return sha1(
        f"blob {len(payload)}\0".encode("ascii") + payload
    ).hexdigest()


def literal_assignment(tree: ast.Module, name: str) -> object | None:
    matches = []
    for node in tree.body:
        if (
            isinstance(node, ast.Assign)
            and any(
                isinstance(target, ast.Name) and target.id == name
                for target in node.targets
            )
        ):
            matches.append(node.value)
    if len(matches) != 1:
        return None
    try:
        return ast.literal_eval(matches[0])
    except (TypeError, ValueError):
        return None


def git_value(*arguments: str) -> str:
    completed = subprocess.run(
        ("git", *arguments),
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
        timeout=15,
    )
    return completed.stdout.strip()


def source_controls() -> dict[str, object]:
    payloads = {
        path: (ROOT / path).read_bytes()
        for path in AUDIT_INPUT_PATHS
        if (ROOT / path).is_file()
    }
    trees = {
        path: ast.parse(payload, filename=path)
        for path, payload in payloads.items()
    }
    self_payload = Path(__file__).read_bytes()
    self_tree = ast.parse(self_payload, filename=Path(__file__).name)
    source_rows = tuple({
        "path": path,
        "exists_worktree_relative":
            not Path(path).is_absolute() and (ROOT / path).is_file(),
        "sha256": sha256(payloads[path]).hexdigest(),
        "expected_sha256": EXPECTED_SHA256[path],
        "sha256_exact":
            sha256(payloads[path]).hexdigest() == EXPECTED_SHA256[path],
        "git_blob": git_blob(payloads[path]),
        "expected_git_blob": EXPECTED_GIT_BLOBS[path],
        "git_blob_exact":
            git_blob(payloads[path]) == EXPECTED_GIT_BLOBS[path],
        "access": (
            "DYNAMIC_IMPORT_CORE"
            if path == CORE_PATH else
            "TEXT_AST_ONLY_BLOCKLISTED"
        ),
        "AST_valid": isinstance(trees[path], ast.Module),
    } for path in AUDIT_INPUT_PATHS)
    direct_frontier_imports = tuple(
        alias.name
        for node in self_tree.body if isinstance(node, ast.Import)
        for alias in node.names
        if alias.name.startswith("frontier_cycle")
    )
    copied_rows = tuple({
        **row,
        "object_spec": f"{row['commit']}:{row['path']}",
        "object_git_blob":
            git_value("rev-parse", f"{row['commit']}:{row['path']}"),
        "object_git_blob_exact":
            git_value("rev-parse", f"{row['commit']}:{row['path']}")
            == row["git_blob"],
        "access": "COPIED_SHA_PIN_ONLY_NOT_READ_OR_EXECUTED",
    } for row in COPIED_SIBLING_SOURCES)
    branch = git_value("branch", "--show-current")
    head = git_value("rev-parse", "HEAD")
    base_is_ancestor = (
        git_value("merge-base", "HEAD", EXPECTED_BASE) == EXPECTED_BASE
    )
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_INPUT_PATHS_literal":
            literal_assignment(self_tree, "AUDIT_INPUT_PATHS")
            == AUDIT_INPUT_PATHS,
        "all_paths_existing_worktree_relative":
            len(payloads) == len(AUDIT_INPUT_PATHS)
            and all(row["exists_worktree_relative"] for row in source_rows),
        "plain_reading_named_files": len(AUDIT_INPUT_PATHS),
        "maximum_named_files": 6,
        "source_rows": source_rows,
        "text_AST_only_paths": TEXT_AST_ONLY_PATHS,
        "blocked_modules": BLOCKLISTED_MODULES,
        "blocked_modules_loaded": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits": tuple(FIREWALL.hits),
        "direct_frontier_imports": direct_frontier_imports,
        "copied_sibling_source_rows": copied_rows,
        "copied_sources_content_policy":
            "SHA-256 values are copied provenance pins; live object identity "
            "is checked by git blob without reading sibling source content.",
        "runner_sha256": sha256(self_payload).hexdigest(),
        "runner_git_blob": git_blob(self_payload),
        "git_branch": branch,
        "expected_git_branch": EXPECTED_BRANCH,
        "git_head": head,
        "expected_base": EXPECTED_BASE,
        "expected_base_is_ancestor": base_is_ancestor,
        "stdlib_only_runner":
            direct_frontier_imports
            == (
                "frontier_cycle719_two_rail_recurrent_controller_core_"
                "2026_07_26",
            ),
    }
    result["pass"] = (
        result["AUDIT_INPUT_PATHS_literal"]
        and result["all_paths_existing_worktree_relative"]
        and len(AUDIT_INPUT_PATHS) <= 6
        and all(
            row["sha256_exact"]
            and row["git_blob_exact"]
            and row["AST_valid"]
            for row in source_rows
        )
        and all(row["object_git_blob_exact"] for row in copied_rows)
        and not result["blocked_modules_loaded"]
        and not result["firewall_hits"]
        and result["stdlib_only_runner"]
        and branch == EXPECTED_BRANCH
        and base_is_ancestor
    )
    return result


def render(
    checks: dict[str, bool],
    certificates: dict[str, object],
    report: dict[str, object],
) -> str:
    lines = [
        f"CERTIFICATE {name} " + compact(value)
        for name, value in certificates.items()
    ]
    lines.extend(
        f"CHECK {name}={str(value).lower()}"
        for name, value in checks.items()
    )
    lines.append("SUMMARY_JSON " + compact(report))
    lines.append(str(report["terminal"]))
    return "\n".join(lines) + "\n"


def stable_render(
    checks: dict[str, bool],
    certificates: dict[str, object],
    report: dict[str, object],
) -> str:
    for _attempt in range(20):
        report["checks"] = dict(checks)
        report["pass"] = all(checks.values())
        report["terminal"] = (
            "CYCLE843_PULSE_PHASE_EXACT_PASS"
            if report["pass"]
            else "CYCLE843_PULSE_PHASE_HONEST_FAIL"
        )
        output = render(checks, certificates, report)
        size = len(output.encode("utf-8"))
        controls = certificates["D_CONTROLS"]
        if (
            report["stdout_bytes"] == size
            and controls["stdout_bytes"] == size
        ):
            return output
        report["stdout_bytes"] = size
        controls["stdout_bytes"] = size
    raise AssertionError("stdout byte fixed point did not converge")


def run() -> int:
    started = monotonic()
    sources = source_controls()
    family = build_event3_family()
    family_duplicate = build_event3_family()
    replay = replay_phases(family)
    replay_duplicate = replay_phases(family_duplicate)
    comparisons = reconstruct_comparison_objects(family)
    certificate_a = phase_state_certificate(family, replay, comparisons)
    certificate_b = selector_certificate(
        family, replay, comparisons
    )
    certificate_c = phase_law_certificate(family)
    law_duplicate = phase_law_certificate(family_duplicate)
    elapsed = monotonic() - started
    family_state_rows = tuple(
        (key, state_sha256(family["states"][key]))
        for key in EVENT3_KEYS
    )
    family_duplicate_state_rows = tuple(
        (key, state_sha256(family_duplicate["states"][key]))
        for key in EVENT3_KEYS
    )
    family_deterministic = (
        family_state_rows == family_duplicate_state_rows
        and state_sha256(family["pulse_coincidence_state"])
        == state_sha256(family_duplicate["pulse_coincidence_state"])
    )
    replay_deterministic = (
        digest(replay) == digest(replay_duplicate)
    )
    law_deterministic = (
        digest(certificate_c) == digest(law_duplicate)
    )
    deterministic = (
        family_deterministic
        and replay_deterministic
        and law_deterministic
        and all(
            row["exact"] for row in comparisons["determinism_rows"]
        )
    )
    controls_base = (
        sources["pass"]
        and family["summary"] == {
            "keys": 9,
            "state_bits": STATE_BITS,
            "word_gate_counts": (6212,),
            "pulse_coincidence_state_weight": 59,
            "all_rail_compositions_exact": True,
        }
        and deterministic
        and not any(
            name in sys.modules for name in BLOCKLISTED_MODULES
        )
        and not FIREWALL.hits
        and elapsed < AUDIT_TIMEOUT_SEC
    )
    controls = {
        **sources,
        "family_summary": family["summary"],
        "exact_arithmetic":
            "All state bits, Hamming weights, projections, parities, XOR "
            "diffs, movement indices, and equality tests use exact Python "
            "integers/tuples; only monotonic runtime is a float.",
        "determinism": {
            "family_duplicate_exact": family_deterministic,
            "phase_replay_duplicate_exact": replay_deterministic,
            "phase_law_duplicate_exact": law_deterministic,
            "funnel_duplicate_rows": comparisons["determinism_rows"],
            "deterministic": deterministic,
        },
        "blocked_modules_loaded_at_end": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits_at_end": tuple(FIREWALL.hits),
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "pass": controls_base,
    }
    checks = {
        "A_RENAME_AND_RETRACTION": bool(certificate_a["pass"]),
        "B_RELATIONSHIP_CENSUS": bool(certificate_b["pass"]),
        "C_KEPT_SELECTORS_AND_PHASE_LAW": bool(certificate_c["pass"]),
        "D_CONTROLS": controls_base,
    }
    certificates = {
        "A_RENAME_AND_RETRACTION": certificate_a,
        "B_RELATIONSHIP_CENSUS": certificate_b,
        "C_KEPT_RESULTS": certificate_c,
        "D_CONTROLS": controls,
    }
    report = {
        "cycle": 843,
        "target": "full-state pulse phase at the event-3 coincidence",
        "phase_partition_sequence": EXPECTED_PHASE_PARTITIONS,
        "coincidence_phase_mod_3": 2,
        "coincidence_object": "pulse coincidence state",
        "coincidence_sha256": EXPECTED_COINCIDENCE_SHA256,
        "coincidence_weight": 59,
        "cycle833_S0_prime_sha256":
            EXPECTED_CYCLE833_S0_PRIME_SHA256,
        "cycle833_S0_prime_weight": 47,
        "identity_retraction": V1_IDENTITY_RETRACTION,
        "minimal_single_wire_selectors": (
            "source.SOURCE_POINTER=1",
            "link0.wire[0]=0",
        ),
        "phase_law_outcome": certificate_c["verdict"],
        "phase_law_scope": certificate_c["scope"],
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "checks": {},
        "pass": False,
        "terminal": "CYCLE843_PULSE_PHASE_HONEST_FAIL",
    }
    output = stable_render(checks, certificates, report)
    stdout_ok = len(output.encode("utf-8")) < STDOUT_LIMIT_BYTES
    checks["D_CONTROLS"] = controls_base and stdout_ok
    controls["pass"] = checks["D_CONTROLS"]
    output = stable_render(checks, certificates, report)
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        sys.stdout.write(compact({
            "pass": False,
            "failure": "stdout limit exceeded",
            "stdout_bytes": len(output.encode("utf-8")),
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
            "terminal": "CYCLE843_PULSE_PHASE_HONEST_FAIL",
        }) + "\n")
        return 1
    sys.stdout.write(output)
    return 0 if report["pass"] else 1


def main() -> int:
    try:
        return run()
    except Exception as error:
        sys.stdout.write(compact({
            "pass": False,
            "exception_type": type(error).__name__,
            "exception": str(error),
            "terminal": "CYCLE843_PULSE_PHASE_HONEST_FAIL",
        }) + "\n")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
