#!/usr/bin/env python3
"""Cycle 843: the full-state pulse phase and its exact selector.

The landed Cycle-719 controller core is the sole executable science
dependency.  Current-worktree Cycle-834/838 sources are SHA-pinned text/AST
controls only.  Cycle-832/833/835 sibling results are copied as small,
SHA-pinned provenance records and are never imported or executed.
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
        "S0_prime": epochs[3],
        "states": event3_states,
        "rail_rows": tuple(rail_rows),
        "summary": {
            "keys": len(event3_states),
            "state_bits": len(epochs[3]),
            "word_gate_counts": tuple(sorted(map(len, words.values()))),
            "S0_prime_weight": sum(epochs[3]),
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
    return {
        "xor_weight": len(wires),
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
    s0_prime = family["S0_prime"]
    assert isinstance(s0_prime, tuple)
    coincidence = phases[2][0]
    exact = (
        tuple(row["component_sizes"] for row in phase_rows)
        == EXPECTED_PHASE_PARTITIONS
        and all(state == coincidence for state in phases[2])
        and coincidence == s0_prime
        and replay["all_close_at_movement_3"]
        and len(same_key_diffs) == 27
        and all(row["diff"]["xor_weight"] > 0 for row in same_key_diffs)
    )
    return {
        "verdict": "PASS" if exact else "FAIL",
        "definition":
            "all 27 full 5815-bit event-3 backbone boundary states",
        "phase_rows": tuple(phase_rows),
        "same_key_pairwise_diffs_across_phases": same_key_diffs,
        "meeting_geometry_by_key": tuple(
            meeting_geometry(key[1]) for key in EVENT3_KEYS
        ),
        "coincidence_phase_mod_3": 2,
        "coincidence_state_anatomy": state_anatomy(coincidence),
        "S0_prime_anatomy": state_anatomy(s0_prime),
        "coincidence_is_exact_S0_prime": coincidence == s0_prime,
        "period_3_closure_exact": replay["all_close_at_movement_3"],
        "pass": exact,
    }
