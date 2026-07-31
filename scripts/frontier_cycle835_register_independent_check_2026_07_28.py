#!/usr/bin/env python3
"""Cycle 835 independent adversarial check of the dwell correction.

The Cycle-835/833/832 primaries are SHA-pinned text/AST evidence only.  This
checker imports only the landed Cycle-719 controller core, reconstructs one
register trajectory per event, and separately replays the pulse boundaries.
"""
from __future__ import annotations

AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle835_register_mechanism_2026_07_28.py",
    "scripts/frontier_cycle832_cohort_moment_law_2026_07_28.py",
    "scripts/frontier_cycle833_funnel_family_2026_07_28.py",
)

import ast
from fractions import Fraction
from hashlib import sha1, sha256
import importlib.abc
from itertools import combinations
import json
from math import lcm
from pathlib import Path
import sys
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

CORE_PATH = AUDIT_INPUT_PATHS[0]
PRIMARY_835_PATH = AUDIT_INPUT_PATHS[1]
PRIMARY_832_PATH = AUDIT_INPUT_PATHS[2]
PRIMARY_833_PATH = AUDIT_INPUT_PATHS[3]
TEXT_AST_ONLY_PATHS = (
    PRIMARY_835_PATH,
    PRIMARY_832_PATH,
    PRIMARY_833_PATH,
)
BLOCKLISTED_MODULES = tuple(Path(path).stem for path in TEXT_AST_ONLY_PATHS)
EXPECTED_SHA256 = {
    CORE_PATH:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    PRIMARY_835_PATH:
        "6b8c26ff77d99225aaa985c645aeee9fa1fb3db19517aec727ff38e0cbcc03f5",
    PRIMARY_832_PATH:
        "0db01e80084af4dbb52c74a0a055984edf8ab818f2c8ba8a99c1f6a3fc15bb3e",
    PRIMARY_833_PATH:
        "bd08f5f503e532c724e6ae28915ba2f0b4202360bbe01458924d689e27c79174",
}
EXPECTED_GIT_BLOBS = {
    CORE_PATH: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    PRIMARY_835_PATH: "a9bfc3d151a591b3d0a4ba06acaa30ed04ff7e67",
    PRIMARY_832_PATH: "d666f5c301ffe6b6508f3636b15814a662bfbe8e",
    PRIMARY_833_PATH: "b3512e0c3e8acdec7bc3f1cfb4e5bf1a236f8fda",
}
AUDIT_TIMEOUT_SECONDS = 1400
STDOUT_LIMIT_BYTES = 150 * 1024
MAX_FILES_READ = 6


class _PrimaryFirewall(importlib.abc.MetaPathFinder):
    """Reject any attempt to import the three source primaries."""

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
            raise ImportError(f"BLOCKLIST rejects {fullname}")
        return None


FIREWALL = _PrimaryFirewall()
sys.meta_path.insert(0, FIREWALL)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


State = tuple[int, ...]
Pair = tuple[int, int]
CompiledGate = tuple[int, int, int, int]

RING_STATIONS = 11
FIXTURE_BANKS = 2
STATE_BITS = 5815
EVENT_ORDER = (0, 2, 1)
FUNNEL_MOMENTS = {0: 14739, 2: 33190, 1: 51110}
WITNESS_PAIR = (1, 6)
BACKBONE = (
    (1, 6), (1, 7), (2, 7), (2, 8), (3, 8),
    (3, 9), (4, 9), (4, 10), (5, 10),
)
TRANSITIONS = (
    {"source_event": 0, "target_event": 2, "residual": 595},
    {"source_event": 2, "target_event": 1, "residual": 64},
)
LCM_FACTORS = (4464, 5952)
LCM_SKELETON = lcm(*LCM_FACTORS)
EXPECTED_FUNNEL_SHA256 = {
    0: "cdf7e03092c6278b686c1f0edb9ebd716f4a285b1eabc8a7e2780695284a8f1a",
    2: "0015151ee4b751c35a5671fbb4f301d8569e78fc5a7ebe9f77372865b153c99b",
    1: "797fa122a629177c00c707aff4857d01bbad16b078983e3a6f1f5b632e094a41",
}
EXPECTED_FUNNEL_WEIGHTS = {0: 44, 2: 45, 1: 46}
EXPECTED_UNIQUE_SEQUENCES = 74
EXPECTED_RAW_BYTES = 203926
EXPECTED_RAW_SHA256 = (
    "3d588a959c0f461859b41931a104237adcd2df5e33bd29aa7457811cca0d702d"
)


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def state_sha256(state: State) -> str:
    return sha256(bytes(state)).hexdigest()


def git_blob(payload: bytes) -> str:
    header = f"blob {len(payload)}\0".encode("ascii")
    return sha1(header + payload).hexdigest()


def literal_assignment(tree: ast.Module, name: str) -> object:
    matches = []
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
        ):
            matches.append(node.value)
        elif (
            isinstance(node, ast.AnnAssign)
            and isinstance(node.target, ast.Name)
            and node.target.id == name
            and node.value is not None
        ):
            matches.append(node.value)
    if len(matches) != 1:
        raise AssertionError((name, len(matches)))
    return ast.literal_eval(matches[0])


def function_node(tree: ast.Module, name: str) -> ast.FunctionDef:
    matches = [
        node for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    if len(matches) != 1:
        raise AssertionError((name, len(matches)))
    return matches[0]


def assigned_expression(
    function: ast.FunctionDef,
    name: str,
) -> ast.expr:
    matches = [
        node.value
        for node in ast.walk(function)
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
        )
    ]
    if len(matches) != 1:
        raise AssertionError((name, len(matches)))
    return matches[0]


def expression_equal(actual: ast.expr, expected: str) -> bool:
    parsed = ast.parse(expected, mode="eval").body
    return ast.dump(actual, include_attributes=False) == ast.dump(
        parsed, include_attributes=False
    )


def dict_value_expression(
    function: ast.FunctionDef,
    key: str,
) -> ast.expr:
    matches: list[ast.expr] = []
    for node in ast.walk(function):
        if not isinstance(node, ast.Dict):
            continue
        for item_key, value in zip(node.keys, node.values):
            if (
                isinstance(item_key, ast.Constant)
                and item_key.value == key
            ):
                matches.append(value)
    if len(matches) != 1:
        raise AssertionError((key, len(matches)))
    return matches[0]


def lcm_call_factors(tree: ast.Module) -> tuple[int, ...]:
    matches = [
        node.value
        for node in tree.body
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name)
            and target.id == "LCM_SKELETON"
            for target in node.targets
        )
    ]
    if len(matches) != 1 or not isinstance(matches[0], ast.Call):
        raise AssertionError("LCM_SKELETON is not one call")
    call = matches[0]
    if not isinstance(call.func, ast.Name) or call.func.id != "lcm":
        raise AssertionError("LCM_SKELETON does not call lcm")
    return tuple(ast.literal_eval(argument) for argument in call.args)


def top_level_functions(tree: ast.Module) -> set[str]:
    return {
        node.name for node in tree.body
        if isinstance(node, ast.FunctionDef)
    }


def source_audit() -> tuple[dict[str, object], ast.Module]:
    payloads = {
        path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS
    }
    trees = {
        path: ast.parse(payload, filename=path)
        for path, payload in payloads.items()
    }
    self_tree = ast.parse(
        Path(__file__).read_text(encoding="utf-8"),
        filename=Path(__file__).name,
    )
    marker_sets = {
        PRIMARY_835_PATH: {
            "track_register_trajectories", "residual_certificate",
            "pulse_phase_certificate", "run",
        },
        PRIMARY_832_PATH: {
            "build_seed_family", "cycle_cohort_certificate", "run",
        },
        PRIMARY_833_PATH: {
            "build_family", "rank_edge_field_map_certificate", "run",
        },
    }
    direct_imports = tuple(sorted(
        alias.name
        for node in self_tree.body
        if isinstance(node, ast.Import)
        for alias in node.names
        if alias.name.startswith("frontier_cycle")
    ))
    sha_rows = {
        path: sha256(payload).hexdigest()
        for path, payload in payloads.items()
    }
    blob_rows = {
        path: git_blob(payload) for path, payload in payloads.items()
    }
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_INPUT_PATHS_literal":
            literal_assignment(self_tree, "AUDIT_INPUT_PATHS")
            == AUDIT_INPUT_PATHS,
        "existing_worktree_relative": all(
            not Path(path).is_absolute() and (ROOT / path).is_file()
            for path in AUDIT_INPUT_PATHS
        ),
        "unique_files_plain_read": len(AUDIT_INPUT_PATHS) + 1,
        "unique_files_plain_read_includes_self": True,
        "maximum_files": MAX_FILES_READ,
        "sha256": sha_rows,
        "expected_sha256": EXPECTED_SHA256,
        "git_blobs": blob_rows,
        "expected_git_blobs": EXPECTED_GIT_BLOBS,
        "text_AST_only_paths": TEXT_AST_ONLY_PATHS,
        "blocked_modules": BLOCKLISTED_MODULES,
        "blocked_markers_present": all(
            required <= top_level_functions(trees[path])
            for path, required in marker_sets.items()
        ),
        "blocked_modules_loaded": tuple(
            module for module in BLOCKLISTED_MODULES
            if module in sys.modules
        ),
        "firewall_hits": tuple(FIREWALL.hits),
        "direct_frontier_imports": direct_imports,
    }
    result["pass"] = (
        result["AUDIT_INPUT_PATHS_literal"]
        and result["existing_worktree_relative"]
        and result["unique_files_plain_read"] <= MAX_FILES_READ
        and sha_rows == EXPECTED_SHA256
        and blob_rows == EXPECTED_GIT_BLOBS
        and result["blocked_markers_present"]
        and direct_imports == (
            "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26",
        )
        and not result["blocked_modules_loaded"]
        and not result["firewall_hits"]
    )
    return result, trees[PRIMARY_835_PATH]


def orbit_word(
    program: tuple[object, ...],
    pair: Pair,
) -> tuple[object, ...]:
    """Independently expand one moving two-token orbit."""
    gates: list[object] = []
    width = len(program)
    for step in range(width):
        live_stations = {
            (pair[0] + step) % width,
            (pair[1] + step) % width,
        }
        for station, macro in enumerate(program):
            if station in live_stations:
                gates.extend(K.mapped_macro(macro))
    return tuple(gates)


def compile_word(word: tuple[object, ...]) -> tuple[CompiledGate, ...]:
    rows: list[CompiledGate] = []
    for gate in word:
        if len(set(gate.wires)) != len(gate.wires):
            raise AssertionError(("repeated wire", gate))
        if gate.kind == "X":
            rows.append((0, gate.wires[0], 0, 0))
        elif gate.kind == "CNOT":
            rows.append((1, gate.wires[0], gate.wires[1], 0))
        elif gate.kind == "TOF":
            rows.append(
                (2, gate.wires[0], gate.wires[1], gate.wires[2])
            )
        else:
            raise AssertionError(("non-reversible gate", gate))
    return tuple(rows)


def build_epochs(
    program: tuple[object, ...],
) -> tuple[dict[int, State], dict[str, object]]:
    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    state = K.M.pack_state(banks, links)
    allocator = K.M.global_allocator_word(FIXTURE_BANKS)
    epochs: dict[int, State] = {}
    semantic_failures = 0
    rail_failures = 0
    trace_failures = 0
    for event in range(2 * FIXTURE_BANKS):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = K.M.prepare_endpoint(state, direction)
        after, rail_a, rail_b, trace = K.run_orbit(before, program)
        semantic_failures += (
            after != K.A.apply_semantic(before, allocator)
        )
        rail_failures += rail_a != (1,) + (0,) * (len(program) - 1)
        rail_failures += any(rail_b)
        trace_failures += len(trace) != len(program)
        epochs[event] = before
        state = after
    result = {
        "event_count": len(epochs),
        "state_bits": len(state),
        "allocator_gates": len(allocator),
        "semantic_failures": semantic_failures,
        "rail_failures": rail_failures,
        "trace_failures": trace_failures,
    }
    result["pass"] = (
        result["event_count"] == 4
        and result["state_bits"] == STATE_BITS
        and result["allocator_gates"] == 3106
        and semantic_failures == rail_failures == trace_failures == 0
    )
    return epochs, result


def trajectory_seed(
    before: State,
    program: tuple[object, ...],
    pair: Pair,
    word: tuple[object, ...],
) -> tuple[State, bool]:
    after, rail_a, rail_b, _trace = K.run_orbit(
        before, program, token_positions=pair
    )
    expected_rail = tuple(
        int(station in pair) for station in range(len(program))
    )
    exact = (
        after == K.A.apply_semantic(before, word)
        and rail_a == expected_rail
        and not any(rail_b)
    )
    return after, exact


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
    return {
        wire: tuple(names) for wire, names in aliases.items()
    }


BANK_WIRE_ALIASES = _bank_wire_aliases()
SOURCE_NAMES = {
    K.R3.X.LEFT_ENDPOINT: "LEFT_ENDPOINT",
    K.R3.X.RIGHT_ENDPOINT: "RIGHT_ENDPOINT",
    K.R3.X.SOURCE_POINTER: "SOURCE_POINTER",
}


def wire_name(wire: int) -> str:
    if wire < K.M.R12.SOURCE_WIDTH:
        local_name = SOURCE_NAMES.get(wire, f"wire[{wire}]")
        return f"source.{local_name}"
    for bank, base in enumerate(K.M.R12.BANK_BASES[:FIXTURE_BANKS]):
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


def register_wires(field_names: tuple[str, ...]) -> tuple[int, ...]:
    names = {wire_name(wire): wire for wire in range(STATE_BITS)}
    if len(names) != STATE_BITS:
        raise AssertionError("wire naming is not injective")
    return tuple(names[field] for field in field_names)


def pack_states(states: tuple[State, ...]) -> list[int]:
    return [
        sum(state[wire] << lane for lane, state in enumerate(states))
        for wire in range(len(states[0]))
    ]


def unpack_lane(columns: list[int], lane: int) -> State:
    return tuple((column >> lane) & 1 for column in columns)


def projected_int(
    columns: list[int],
    lane: int,
    wires: tuple[int, ...],
) -> int:
    return sum(
        ((columns[wire] >> lane) & 1) << index
        for index, wire in enumerate(wires)
    )


def state_projection(state: State, wires: tuple[int, ...]) -> int:
    return sum(state[wire] << index for index, wire in enumerate(wires))


def advance_packed(
    columns: list[int],
    word: tuple[CompiledGate, ...],
    active_mask: int,
) -> None:
    for kind, first, second, third in word:
        if kind == 0:
            columns[first] ^= active_mask
        elif kind == 1:
            columns[second] ^= columns[first] & active_mask
        else:
            columns[third] ^= (
                columns[first] & columns[second] & active_mask
            )


def track_trajectories(
    epochs: dict[int, State],
    program: tuple[object, ...],
    wires: tuple[int, ...],
) -> dict[str, object]:
    """Fresh packed replay; no Cycle-835 function or output is consumed."""
    landed_word = orbit_word(program, WITNESS_PAIR)
    compiled = compile_word(landed_word)
    seeds: dict[int, State] = {}
    seed_checks = {}
    for event in EVENT_ORDER:
        seeds[event], seed_checks[event] = trajectory_seed(
            epochs[event], program, WITNESS_PAIR, landed_word
        )

    lane_rows = tuple(
        (event, role)
        for event in EVENT_ORDER
        for role in ("primary", "duplicate")
    )
    primary_lane = {
        event: lane
        for lane, (event, role) in enumerate(lane_rows)
        if role == "primary"
    }
    duplicate_lane = {
        event: lane
        for lane, (event, role) in enumerate(lane_rows)
        if role == "duplicate"
    }
    initial = tuple(seeds[event] for event, _role in lane_rows)
    columns = pack_states(initial)
    changes = {
        event: [[] for _wire in wires] for event in EVENT_ORDER
    }
    histories = {
        event: [projected_int(columns, primary_lane[event], wires)]
        for event in EVENT_ORDER
    }
    previous = {
        event: histories[event][0] for event in EVENT_ORDER
    }
    duplicate_exact = True
    for cohort_time in range(1, max(FUNNEL_MOMENTS.values()) + 1):
        active_mask = sum(
            1 << lane
            for lane, (event, _role) in enumerate(lane_rows)
            if cohort_time <= FUNNEL_MOMENTS[event]
        )
        advance_packed(columns, compiled, active_mask)
        for event in EVENT_ORDER:
            if cohort_time > FUNNEL_MOMENTS[event]:
                continue
            primary_value = projected_int(
                columns, primary_lane[event], wires
            )
            duplicate_value = projected_int(
                columns, duplicate_lane[event], wires
            )
            duplicate_exact &= primary_value == duplicate_value
            flipped = primary_value ^ previous[event]
            while flipped:
                low_bit = flipped & -flipped
                field_index = low_bit.bit_length() - 1
                changes[event][field_index].append(cohort_time)
                flipped ^= low_bit
            histories[event].append(primary_value)
            previous[event] = primary_value

    funnels = {
        event: unpack_lane(columns, primary_lane[event])
        for event in EVENT_ORDER
    }
    duplicate_funnels = {
        event: unpack_lane(columns, duplicate_lane[event])
        for event in EVENT_ORDER
    }
    stats = {}
    for event in EVENT_ORDER:
        history = histories[event]
        endpoint = FUNNEL_MOMENTS[event]
        final_value = history[-1]
        entry = endpoint
        while entry and history[entry - 1] == final_value:
            entry -= 1
        all_times = {
            time for sequence in changes[event] for time in sequence
        }
        stats[event] = {
            "endpoint": endpoint,
            "last_change_time": max(all_times),
            "final_entry_time": entry,
            "terminal_dwell": endpoint - entry,
            "total_field_flips": sum(
                len(sequence) for sequence in changes[event]
            ),
            "distinct_change_ticks": len(all_times),
            "final_projection": final_value,
        }

    xor_union = tuple(
        wire for wire in range(STATE_BITS)
        if any(
            funnels[left][wire] != funnels[right][wire]
            for left, right in ((0, 2), (2, 1), (0, 1))
        )
    )
    result = {
        "word_gates": len(compiled),
        "seeds": seeds,
        "changes": changes,
        "histories": histories,
        "funnels": funnels,
        "stats": stats,
        "xor_union": xor_union,
        "seed_semantics_exact": all(seed_checks.values()),
        "duplicate_projection_exact_at_every_tick": duplicate_exact,
        "duplicate_full_funnels_exact": all(
            funnels[event] == duplicate_funnels[event]
            for event in EVENT_ORDER
        ),
    }
    result["pass"] = (
        len(compiled) == 6212
        and result["seed_semantics_exact"]
        and result["duplicate_projection_exact_at_every_tick"]
        and result["duplicate_full_funnels_exact"]
        and xor_union == tuple(sorted(wires))
        and all(
            state_sha256(funnels[event])
            == EXPECTED_FUNNEL_SHA256[event]
            and sum(funnels[event]) == EXPECTED_FUNNEL_WEIGHTS[event]
            for event in EVENT_ORDER
        )
    )
    return result


def uleb128(value: int) -> bytes:
    if value < 0:
        raise ValueError(value)
    output = bytearray()
    while True:
        byte = value & 0x7F
        value >>= 7
        if value:
            output.append(byte | 0x80)
        else:
            output.append(byte)
            return bytes(output)


def sequence_encoding(
    changes: dict[int, list[list[int]]],
) -> dict[str, object]:
    sequences: list[tuple[int, ...]] = []
    seen: dict[tuple[int, ...], int] = {}
    for event in EVENT_ORDER:
        for times in changes[event]:
            sequence = tuple(times)
            if sequence not in seen:
                seen[sequence] = len(sequences)
                sequences.append(sequence)
    raw = bytearray()
    for sequence in sequences:
        previous = 0
        for change_time in sequence:
            raw.extend(uleb128(change_time - previous))
            previous = change_time
    result = {
        "unique_sequence_count": len(sequences),
        "raw_bytes": len(raw),
        "raw_sha256": sha256(raw).hexdigest(),
        "sequence_set_sha256": digest(tuple(sequences)),
    }
    result["pass"] = (
        result["unique_sequence_count"] == EXPECTED_UNIQUE_SEQUENCES
        and result["raw_bytes"] == EXPECTED_RAW_BYTES
        and result["raw_sha256"] == EXPECTED_RAW_SHA256
    )
    return result


def state_as_int(state: State) -> int:
    return sum(bit << wire for wire, bit in enumerate(state))


def apply_word_to_int(
    state: int,
    word: tuple[CompiledGate, ...],
) -> int:
    for kind, first, second, third in word:
        if kind == 0:
            state ^= 1 << first
        elif kind == 1:
            if (state >> first) & 1:
                state ^= 1 << second
        elif (
            (state >> first) & 1
            and (state >> second) & 1
        ):
            state ^= 1 << third
    return state


def pulse_boundaries(
    epochs: dict[int, State],
    program: tuple[object, ...],
    wires: tuple[int, ...],
) -> dict[str, object]:
    initial_states = []
    schedules = []
    semantic_checks = []
    for pair in BACKBONE:
        word = orbit_word(program, pair)
        seed, exact = trajectory_seed(epochs[3], program, pair, word)
        initial_states.append(state_as_int(seed))
        schedules.append(compile_word(word))
        semantic_checks.append(exact)

    def replay() -> tuple[tuple[tuple[int, ...], tuple[int, ...]], ...]:
        states = list(initial_states)
        rows = []
        for movement in range(4):
            projections = tuple(
                sum(
                    ((state >> wire) & 1) << field
                    for field, wire in enumerate(wires)
                )
                for state in states
            )
            rows.append((tuple(states), projections))
            if movement < 3:
                states = [
                    apply_word_to_int(state, schedule)
                    for state, schedule in zip(states, schedules)
                ]
        return tuple(rows)

    first = replay()
    second = replay()
    full_common_phases = tuple(
        phase for phase, (states, _projections) in enumerate(first[:3])
        if len(set(states)) == 1
    )
    register_common_phases = tuple(
        phase for phase, (_states, projections) in enumerate(first[:3])
        if len(set(projections)) == 1
    )
    common_values = tuple(
        f"{first[phase][1][0]:010x}"
        for phase in register_common_phases
    )
    result = {
        "keys": tuple((3, pair) for pair in BACKBONE),
        "gates_per_movement": tuple(map(len, schedules)),
        "full_common_phases_mod_3": full_common_phases,
        "register_common_phases_mod_3": register_common_phases,
        "register_common_values_hex": common_values,
        "movement_3_closes": first[3][0] == first[0][0],
        "duplicate_replay_exact": first == second,
        "seed_semantics_exact": all(semantic_checks),
    }
    result["pass"] = (
        result["gates_per_movement"] == (6212,) * len(BACKBONE)
        and result["seed_semantics_exact"]
        and result["duplicate_replay_exact"]
        and result["movement_3_closes"]
        and full_common_phases == (2,)
        and register_common_phases == (0, 1, 2)
        and len(set(common_values)) == 1
    )
    return result


def definition_audit(
    primary_tree: ast.Module,
    stats: dict[int, dict[str, object]],
) -> dict[str, object]:
    residual_function = function_node(
        primary_tree, "residual_certificate"
    )
    track_function = function_node(
        primary_tree, "track_register_trajectories"
    )
    entry_expression = assigned_expression(
        residual_function, "entry_gap"
    )
    dwell_expression = assigned_expression(
        residual_function, "dwell_correction"
    )
    corrected_expression = assigned_expression(
        residual_function, "corrected"
    )
    final_entry_expression = assigned_expression(
        track_function, "final_entry"
    )
    terminal_dwell_expression = dict_value_expression(
        track_function, "terminal_dwell_ticks"
    )
    ast_exact = (
        expression_equal(
            entry_expression,
            "stats[target]['final_projection_entry_time']"
            " - stats[source]['final_projection_entry_time']",
        )
        and expression_equal(
            dwell_expression,
            "stats[target]['terminal_dwell_ticks']"
            " - stats[source]['terminal_dwell_ticks']",
        )
        and expression_equal(
            corrected_expression,
            "entry_gap - LCM_SKELETON + dwell_correction",
        )
        and expression_equal(
            final_entry_expression, "FUNNEL_MOMENTS[event]"
        )
        and expression_equal(
            terminal_dwell_expression,
            "FUNNEL_MOMENTS[event] - final_entry",
        )
    )

    rows = []
    fitted_coefficients = []
    for transition in TRANSITIONS:
        source = transition["source_event"]
        target = transition["target_event"]
        expected = transition["residual"]
        source_stats = stats[source]
        target_stats = stats[target]
        entry_gap = (
            target_stats["final_entry_time"]
            - source_stats["final_entry_time"]
        )
        dwell_delta = (
            target_stats["terminal_dwell"]
            - source_stats["terminal_dwell"]
        )
        raw = entry_gap - LCM_SKELETON
        corrected = raw + dwell_delta
        endpoint_baseline = (
            target_stats["endpoint"]
            - source_stats["endpoint"]
            - LCM_SKELETON
        )
        alpha = Fraction(expected - raw, dwell_delta)
        fitted_coefficients.append(alpha)
        rows.append({
            "source_event": source,
            "target_event": target,
            "source_entry": source_stats["final_entry_time"],
            "target_entry": target_stats["final_entry_time"],
            "source_dwell": source_stats["terminal_dwell"],
            "target_dwell": target_stats["terminal_dwell"],
            "raw": raw,
            "dwell_delta": dwell_delta,
            "recomputed_without_target": corrected,
            "withheld_target_for_check_only": expected,
            "endpoint_baseline": endpoint_baseline,
            "identity_exact": corrected == endpoint_baseline,
            "target_exact": corrected == expected,
            "alpha_fitted_afterward": str(alpha),
        })

    expression_constants = {
        node.value
        for expression in (
            entry_expression, dwell_expression, corrected_expression
        )
        for node in ast.walk(expression)
        if isinstance(node, ast.Constant)
        and isinstance(node.value, (int, float))
    }
    no_residual_literal = not ({595, 64} & expression_constants)
    identical_change_sequence_counterexample = {
        "event": 0,
        "original_endpoint": stats[0]["endpoint"],
        "extended_endpoint_with_no_new_change":
            stats[0]["endpoint"] + 1,
        "change_sequences_identical": True,
        "original_dwell": stats[0]["terminal_dwell"],
        "extended_dwell": stats[0]["terminal_dwell"] + 1,
        "corrected_coordinate_changes_by": 1,
    }
    rows_exact = all(
        row["target_exact"] and row["identity_exact"] for row in rows
    )
    coefficient_fit = tuple(fitted_coefficients) == (
        Fraction(1), Fraction(1)
    )
    result = {
        "ruling": "FITTED",
        "primary_definition_AST": {
            "entry_gap": ast.unparse(entry_expression),
            "dwell_correction": ast.unparse(dwell_expression),
            "corrected": ast.unparse(corrected_expression),
            "terminal_dwell": ast.unparse(terminal_dwell_expression),
            "exact_source_shape": ast_exact,
        },
        "formal_definition": (
            "h_e=cohort endpoint; tau_e=entry into the final register "
            "value; d_e=h_e-tau_e; C(s,t)="
            "(tau_t-tau_s-L)+(d_t-d_s)=h_t-h_s-L"
        ),
        "direct_595_or_64_literal_in_formula": not no_residual_literal,
        "computable_from_unbounded_change_sequences_alone": False,
        "forbidden_dependency": (
            "d_e requires FUNNEL_MOMENTS[e], the cohort endpoint; an "
            "unchanged extension preserves every register change sequence "
            "but changes d_e and C"
        ),
        "same_sequences_counterexample":
            identical_change_sequence_counterexample,
        "degrees_of_freedom": (
            "In C_alpha=raw+alpha*(target dwell-source dwell), no "
            "independent dynamics in the primary fixes alpha.  The chosen "
            "alpha=+1 (including the signed target-minus-source transfer) "
            "is exactly the value selected by both retained targets."
        ),
        "two_point_fit": {
            "family": "C_alpha=raw+alpha*Delta_dwell",
            "fitted_alpha_by_transition":
                tuple(str(value) for value in fitted_coefficients),
            "shared_alpha": "1" if coefficient_fit else "NONE",
        },
        "recomputation": tuple(rows),
        "accounting_identity_not_register_prediction": all(
            row["recomputed_without_target"] == row["endpoint_baseline"]
            for row in rows
        ),
        "finding": (
            "FITTED: the +1 signed dwell transfer is not defined by the "
            "register sequences alone; because dwell is measured to each "
            "cohort moment, it algebraically restores the cohort-moment "
            "baseline and turns {594,65} into {595,64}."
        ),
    }
    result["pass"] = (
        ast_exact
        and no_residual_literal
        and rows_exact
        and coefficient_fit
        and result["accounting_identity_not_register_prediction"]
        and not result["computable_from_unbounded_change_sequences_alone"]
        and result["ruling"] == "FITTED"
    )
    return result


def sequence_certificate(
    primary_tree: ast.Module,
    fields: tuple[str, ...],
    wires: tuple[int, ...],
    trajectory: dict[str, object],
    encoding: dict[str, object],
) -> dict[str, object]:
    rows = tuple({
        "event": event,
        "trajectory_key": (event, WITNESS_PAIR),
        "endpoint": trajectory["stats"][event]["endpoint"],
        "final_entry": trajectory["stats"][event]["final_entry_time"],
        "terminal_dwell": trajectory["stats"][event]["terminal_dwell"],
        "last_change": trajectory["stats"][event]["last_change_time"],
        "total_field_flips":
            trajectory["stats"][event]["total_field_flips"],
        "distinct_change_ticks":
            trajectory["stats"][event]["distinct_change_ticks"],
        "funnel_sha256":
            state_sha256(trajectory["funnels"][event]),
    } for event in EVENT_ORDER)
    primary_constants_exact = (
        literal_assignment(primary_tree, "EVENT_ORDER") == EVENT_ORDER
        and literal_assignment(primary_tree, "FUNNEL_MOMENTS")
        == FUNNEL_MOMENTS
        and literal_assignment(primary_tree, "BACKBONE") == BACKBONE
        and literal_assignment(primary_tree, "REGISTER_FIELDS") == fields
        and lcm_call_factors(primary_tree) == LCM_FACTORS
    )
    result = {
        "definition": (
            "one fresh (event,(1,6)) landed cohort replay per event; "
            "the core orbit word is expanded locally and applied once per "
            "integer cohort tick"
        ),
        "register_field_count": len(fields),
        "register_wire_count": len(wires),
        "derived_funnel_xor_union_exact":
            trajectory["xor_union"] == tuple(sorted(wires)),
        "trajectory_rows": rows,
        "encoding": encoding,
        "primary_fixture_constants_AST_exact": primary_constants_exact,
        "finding": (
            "independent replay re-derives 39 field sequences with 74 "
            "unique sequences; final entries are 14739/33189/51110 and "
            "terminal dwells are 0/1/0"
        ),
    }
    result["pass"] = (
        trajectory["pass"]
        and encoding["pass"]
        and len(fields) == len(wires) == 39
        and result["derived_funnel_xor_union_exact"]
        and primary_constants_exact
        and tuple(
            trajectory["stats"][event]["final_entry_time"]
            for event in EVENT_ORDER
        ) == (14739, 33189, 51110)
        and tuple(
            trajectory["stats"][event]["terminal_dwell"]
            for event in EVENT_ORDER
        ) == (0, 1, 0)
    )
    return result


def failed_candidate_certificate(
    trajectory: dict[str, object],
) -> dict[str, object]:
    stats = trajectory["stats"]
    changes = trajectory["changes"]
    rows = []
    expected_observations = {
        "C1_LAST_ANY_REGISTER_CHANGE_CATCHUP": (594, 65),
        "C2_FINAL_REGISTER_VALUE_ENTRY_CATCHUP": (594, 65),
        "C3_RANK_EDGE_FIELDS_LAST_CHANGE_CATCHUP": (594, 65),
        "C4_TOTAL_REGISTER_FLIP_DIFFERENCE": (60849, 46058),
        "C5_DISTINCT_REGISTER_CHANGE_TICK_DIFFERENCE": (8104, 8037),
    }
    definitions = {
        "C1_LAST_ANY_REGISTER_CHANGE_CATCHUP":
            "target last 39-field change minus source last change minus LCM",
        "C2_FINAL_REGISTER_VALUE_ENTRY_CATCHUP":
            "target final-projection entry minus source entry minus LCM",
        "C3_RANK_EDGE_FIELDS_LAST_CHANGE_CATCHUP":
            "last-change gap restricted to the transition's funnel XOR "
            "mask minus LCM",
        "C4_TOTAL_REGISTER_FLIP_DIFFERENCE":
            "target total 39-field flips minus source total flips",
        "C5_DISTINCT_REGISTER_CHANGE_TICK_DIFFERENCE":
            "target distinct 39-field change ticks minus source count",
    }
    observations: dict[str, list[int]] = {
        candidate: [] for candidate in expected_observations
    }
    for transition in TRANSITIONS:
        source = transition["source_event"]
        target = transition["target_event"]
        source_stats = stats[source]
        target_stats = stats[target]
        edge_mask = (
            source_stats["final_projection"]
            ^ target_stats["final_projection"]
        )

        def edge_last(event: int) -> int:
            return max(
                change_time
                for field, times in enumerate(changes[event])
                if (edge_mask >> field) & 1
                for change_time in times
            )

        observations[
            "C1_LAST_ANY_REGISTER_CHANGE_CATCHUP"
        ].append(
            target_stats["last_change_time"]
            - source_stats["last_change_time"]
            - LCM_SKELETON
        )
        observations[
            "C2_FINAL_REGISTER_VALUE_ENTRY_CATCHUP"
        ].append(
            target_stats["final_entry_time"]
            - source_stats["final_entry_time"]
            - LCM_SKELETON
        )
        observations[
            "C3_RANK_EDGE_FIELDS_LAST_CHANGE_CATCHUP"
        ].append(edge_last(target) - edge_last(source) - LCM_SKELETON)
        observations[
            "C4_TOTAL_REGISTER_FLIP_DIFFERENCE"
        ].append(
            target_stats["total_field_flips"]
            - source_stats["total_field_flips"]
        )
        observations[
            "C5_DISTINCT_REGISTER_CHANGE_TICK_DIFFERENCE"
        ].append(
            target_stats["distinct_change_ticks"]
            - source_stats["distinct_change_ticks"]
        )

    targets = tuple(row["residual"] for row in TRANSITIONS)
    for candidate, expected_values in expected_observations.items():
        observed = tuple(observations[candidate])
        rows.append({
            "candidate_id": candidate,
            "definition": definitions[candidate],
            "observed": observed,
            "targets": targets,
            "printed_reason_reproduced": observed == expected_values,
            "outcome": "FAILS" if observed != targets else "HOLDS_EXACTLY",
        })
    result = {
        "candidate_rows": tuple(rows),
        "finding": (
            "all five mechanistic candidates fail for the printed numeric "
            "reasons: C1/C2/C3 give {594,65}, C4 gives "
            "{60849,46058}, and C5 gives {8104,8037}, not {595,64}"
        ),
    }
    result["pass"] = all(
        row["printed_reason_reproduced"] and row["outcome"] == "FAILS"
        for row in rows
    )
    return result


def pulse_certificate(pulse: dict[str, object]) -> dict[str, object]:
    result = {
        **pulse,
        "phase_selection_outcome": "FAILS",
        "finding": (
            "the full states coincide only at phase 2, but the 39-field "
            "register block is common at phases 0, 1, and 2"
        ),
    }
    result["pass"] = (
        pulse["pass"]
        and pulse["full_common_phases_mod_3"] == (2,)
        and pulse["register_common_phases_mod_3"] == (0, 1, 2)
        and result["phase_selection_outcome"] == "FAILS"
    )
    return result


def render(
    checks: dict[str, bool],
    certificates: dict[str, object],
    summary: dict[str, object],
) -> str:
    lines = [
        f"{'PASS' if passed else 'FAIL'} {name} "
        f"{compact(certificates[name])}"
        for name, passed in checks.items()
    ]
    lines.append("SUMMARY_JSON " + compact(summary))
    lines.append(summary["terminal"])
    return "\n".join(lines) + "\n"


def stable_render(
    checks: dict[str, bool],
    certificates: dict[str, object],
    summary: dict[str, object],
) -> str:
    for _attempt in range(20):
        summary["checks"] = checks
        summary["pass"] = all(checks.values())
        summary["terminal"] = (
            "CYCLE835_REGISTER_INDEPENDENT_REFUTATION_PASS"
            if summary["pass"]
            else "CYCLE835_REGISTER_INDEPENDENT_HONEST_FAIL"
        )
        output = render(checks, certificates, summary)
        size = len(output.encode("utf-8"))
        controls = certificates["CONTROLS"]
        if (
            controls["stdout_bytes"] == size
            and summary["stdout_bytes"] == size
        ):
            return output
        controls["stdout_bytes"] = size
        summary["stdout_bytes"] = size
    raise AssertionError("stdout size failed to converge")


def run() -> int:
    started = monotonic()
    sources, primary_tree = source_audit()
    fields = tuple(literal_assignment(primary_tree, "REGISTER_FIELDS"))
    wires = register_wires(fields)
    program = K.interleaved_program(FIXTURE_BANKS)
    epochs, epoch_checks = build_epochs(program)
    trajectory = track_trajectories(epochs, program, wires)
    encoding = sequence_encoding(trajectory["changes"])
    definition = definition_audit(primary_tree, trajectory["stats"])
    sequences = sequence_certificate(
        primary_tree, fields, wires, trajectory, encoding
    )
    failed_candidates = failed_candidate_certificate(trajectory)
    pulse = pulse_certificate(
        pulse_boundaries(epochs, program, wires)
    )
    elapsed = monotonic() - started

    determinism = {
        "cohort_duplicate_projection_exact_at_every_tick":
            trajectory["duplicate_projection_exact_at_every_tick"],
        "cohort_duplicate_full_funnels_exact":
            trajectory["duplicate_full_funnels_exact"],
        "pulse_duplicate_replay_exact": pulse["duplicate_replay_exact"],
    }
    controls_base = (
        sources["pass"]
        and epoch_checks["pass"]
        and all(determinism.values())
        and elapsed < AUDIT_TIMEOUT_SECONDS
        and not FIREWALL.hits
        and not any(
            module in sys.modules for module in BLOCKLISTED_MODULES
        )
    )
    controls = {
        **sources,
        "epoch_reconstruction": epoch_checks,
        "determinism": determinism,
        "blocked_modules_loaded_at_end": tuple(
            module for module in BLOCKLISTED_MODULES
            if module in sys.modules
        ),
        "firewall_hits_at_end": tuple(FIREWALL.hits),
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SECONDS,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "finding": (
            "all four SHA-pinned inputs exist worktree-relative; the "
            "Cycle-835/833/832 primaries were parsed as text/AST only"
        ),
        "pass": controls_base,
    }
    certificates = {
        "THE_DEFINITION_AUDIT": definition,
        "THE_SEQUENCES": sequences,
        "THE_FAILED_CANDIDATES": failed_candidates,
        "THE_PULSE_NEGATIVE": pulse,
        "CONTROLS": controls,
    }
    checks = {
        "THE_DEFINITION_AUDIT": bool(definition["pass"]),
        "THE_SEQUENCES": bool(sequences["pass"]),
        "THE_FAILED_CANDIDATES": bool(failed_candidates["pass"]),
        "THE_PULSE_NEGATIVE": bool(pulse["pass"]),
        "CONTROLS": controls_base,
    }
    summary = {
        "cycle": 835,
        "definition_audit_ruling": definition["ruling"],
        "recomputed_corrected_residuals": tuple(
            row["recomputed_without_target"]
            for row in definition["recomputation"]
        ),
        "raw_residuals": tuple(
            row["raw"] for row in definition["recomputation"]
        ),
        "register_final_entries": tuple(
            trajectory["stats"][event]["final_entry_time"]
            for event in EVENT_ORDER
        ),
        "terminal_dwells": tuple(
            trajectory["stats"][event]["terminal_dwell"]
            for event in EVENT_ORDER
        ),
        "pulse_full_common_phases":
            pulse["full_common_phases_mod_3"],
        "pulse_register_common_phases":
            pulse["register_common_phases_mod_3"],
        "overall": (
            "REFUTES_DWELL_CORRECTION_AS_A_PRINCIPLED_REGISTER_MECHANISM"
        ),
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SECONDS,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "checks": {},
        "pass": False,
        "terminal": "CYCLE835_REGISTER_INDEPENDENT_HONEST_FAIL",
    }
    output = stable_render(checks, certificates, summary)
    stdout_ok = len(output.encode("utf-8")) < STDOUT_LIMIT_BYTES
    checks["CONTROLS"] = controls_base and stdout_ok
    controls["pass"] = checks["CONTROLS"]
    output = stable_render(checks, certificates, summary)
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        sys.stdout.write(compact({
            "pass": False,
            "failure": "stdout limit exceeded",
            "stdout_bytes": len(output.encode("utf-8")),
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
            "terminal": "CYCLE835_REGISTER_INDEPENDENT_HONEST_FAIL",
        }) + "\n")
        return 1
    sys.stdout.write(output)
    return 0 if summary["pass"] else 1


def main() -> int:
    return run()


if __name__ == "__main__":
    raise SystemExit(main())
