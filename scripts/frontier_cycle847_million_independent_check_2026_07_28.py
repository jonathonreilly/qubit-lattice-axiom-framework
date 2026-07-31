#!/usr/bin/env python3
"""Independent adversarial check of the Cycle-847 million-tick null."""
from __future__ import annotations

AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle847_trio_to_a_million_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle838_k3_trio_forecast_2026_07_28.py",
    "scripts/frontier_cycle844_standing_bets_2026_07_28.py",
)

import ast
from hashlib import sha1, sha256
import importlib.abc
from itertools import combinations
import json
from pathlib import Path
import sys
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
PRIMARY_PATH = AUDIT_INPUT_PATHS[0]
CORE_PATH = AUDIT_INPUT_PATHS[1]
SOURCE_ONLY_PATHS = (
    AUDIT_INPUT_PATHS[0],
    AUDIT_INPUT_PATHS[2],
    AUDIT_INPUT_PATHS[3],
)
BLOCKLISTED_MODULES = tuple(Path(path).stem for path in SOURCE_ONLY_PATHS)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "dab7567b80c9f70488581a9387e654d9bf5e053afcade822576e5a3bd47bba95",
    AUDIT_INPUT_PATHS[1]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[2]:
        "ea668b4d0be960622cd10d4e16b3cd1056d343db80ee6845407ca6ddb3e604c0",
    AUDIT_INPUT_PATHS[3]:
        "6c52e0d8db9b4b7ecf91b3c5b17436036c89ff18def2f951fb2ee0db8e2a19f9",
}
EXPECTED_GIT_BLOB = {
    AUDIT_INPUT_PATHS[0]: "c18478b434b962a42df0b9a46ebc50e50fb30f81",
    AUDIT_INPUT_PATHS[1]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    AUDIT_INPUT_PATHS[2]: "2f89c8eb911375bed58b1126e9f5f7b860ead20a",
    AUDIT_INPUT_PATHS[3]: "a12245720a7e866134978c25629e19ba57596929",
}


class PrimaryFirewall(importlib.abc.MetaPathFinder):
    """Make accidental execution of a source primary a hard failure."""

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


FIREWALL = PrimaryFirewall()
sys.meta_path.insert(0, FIREWALL)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


Key = tuple[int, tuple[int, ...], int]
State = bytes
Partition = tuple[tuple[int, ...], ...]
MaskedGate = tuple[int, int, int, int, int]
TARGET_T = 1_048_576
RING_STATIONS = 11
FIXTURE_BANKS = 2
STATE_BITS = 5815
WATCHED_COORDINATES = 477
BRAID_DEPTH = 64
FUNNEL_T = 14_739
EXPECTED_FUNNEL_SHA256 = (
    "cdf7e03092c6278b686c1f0edb9ebd716f4a285b1eabc8a7e2780695284a8f1a"
)
EXPECTED_BRAID_SHA256 = (
    "3a145e4ad78f9440d58a781c123b7915fe5e83993f288b16562ea91e37ccbbc4"
)
RUNTIME_LIMIT_SECONDS = 1500
STDOUT_LIMIT_BYTES = 150_000

ALL_K3_KEYS: tuple[Key, ...] = (
    (3, (0, 2, 6), 2),
    (3, (0, 2, 6), 3),
    (3, (0, 2, 7), 2),
    (3, (0, 2, 7), 3),
    (3, (0, 2, 8), 2),
    (3, (0, 2, 8), 3),
    (3, (0, 3, 6), 2),
    (3, (0, 3, 6), 3),
    (3, (0, 3, 7), 2),
    (3, (0, 3, 7), 3),
)
SPOT_KEYS: tuple[Key, ...] = (
    (3, (0, 2, 6), 2),
    (3, (0, 2, 6), 3),
    (3, (0, 3, 6), 2),
)
DETERMINISM_KEY = SPOT_KEYS[0]
BACKBONE = (
    (1, 6), (1, 7), (2, 7), (2, 8), (3, 8),
    (3, 9), (4, 9), (4, 10), (5, 10),
)


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def state_sha256(state: State | tuple[int, ...]) -> str:
    return sha256(bytes(state)).hexdigest()


def git_blob(payload: bytes) -> str:
    header = f"blob {len(payload)}\0".encode("ascii")
    return sha1(header + payload).hexdigest()


def literal_assignment(tree: ast.Module, name: str) -> object | None:
    values: list[ast.expr] = []
    for node in tree.body:
        if isinstance(node, ast.Assign):
            if any(
                isinstance(target, ast.Name) and target.id == name
                for target in node.targets
            ):
                values.append(node.value)
        elif (
            isinstance(node, ast.AnnAssign)
            and isinstance(node.target, ast.Name)
            and node.target.id == name
            and node.value is not None
        ):
            values.append(node.value)
    if len(values) != 1:
        return None
    try:
        return ast.literal_eval(values[0])
    except (TypeError, ValueError):
        return None


def source_controls() -> dict[str, object]:
    """Read exactly four named inputs as bytes/AST; execute only the core."""
    payloads = {path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS}
    trees = {
        path: ast.parse(payload, filename=path)
        for path, payload in payloads.items()
    }
    self_tree = ast.parse(
        Path(__file__).read_bytes(), filename=Path(__file__).name
    )
    rows = tuple({
        "path": path,
        "worktree_relative": not Path(path).is_absolute(),
        "exists": (ROOT / path).is_file(),
        "sha256": sha256(payloads[path]).hexdigest(),
        "expected_sha256": EXPECTED_SHA256[path],
        "sha256_exact":
            sha256(payloads[path]).hexdigest() == EXPECTED_SHA256[path],
        "git_blob": git_blob(payloads[path]),
        "expected_git_blob": EXPECTED_GIT_BLOB[path],
        "git_blob_exact":
            git_blob(payloads[path]) == EXPECTED_GIT_BLOB[path],
        "AST_valid": isinstance(trees[path], ast.Module),
        "access": (
            "EXECUTABLE_LANDED_CORE"
            if path == CORE_PATH else "TEXT_AST_ONLY_BLOCKLISTED"
        ),
    } for path in AUDIT_INPUT_PATHS)
    direct_frontier_imports = tuple(
        alias.name
        for node in self_tree.body if isinstance(node, ast.Import)
        for alias in node.names
        if alias.name.startswith("frontier_cycle")
    )
    primary_tree = trees[PRIMARY_PATH]
    forecast_keys = literal_assignment(
        trees[AUDIT_INPUT_PATHS[2]], "K3_OPEN_THROUGH_T65536"
    )
    standing_keys = literal_assignment(
        trees[AUDIT_INPUT_PATHS[3]], "K3_KEYS"
    )
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "input_count": len(AUDIT_INPUT_PATHS),
        "read_limit": 5,
        "self_plus_named_files_read": len(AUDIT_INPUT_PATHS) + 1,
        "AUDIT_INPUT_PATHS_literal":
            literal_assignment(self_tree, "AUDIT_INPUT_PATHS")
            == AUDIT_INPUT_PATHS,
        "all_existing_worktree_relative": all(
            row["exists"] and row["worktree_relative"] for row in rows
        ),
        "source_rows": rows,
        "source_only_paths": SOURCE_ONLY_PATHS,
        "blocked_modules": BLOCKLISTED_MODULES,
        "direct_frontier_imports": direct_frontier_imports,
        "primary_literal_target":
            literal_assignment(primary_tree, "TARGET_HORIZON"),
        "primary_literal_k3_keys":
            literal_assignment(primary_tree, "K3_KEYS"),
        "primary_literal_braid_sha256":
            literal_assignment(
                primary_tree, "EXPECTED_UNIVERSAL_BRAID_SHA256"
            ),
        "forecast_literal_k3_keys": forecast_keys,
        "standing_literal_k3_keys": standing_keys,
    }
    result["literal_claim_surface_exact"] = (
        result["primary_literal_target"] == TARGET_T
        and result["primary_literal_k3_keys"] == ALL_K3_KEYS
        and result["primary_literal_braid_sha256"]
        == EXPECTED_BRAID_SHA256
        and forecast_keys == ALL_K3_KEYS
        and standing_keys == ALL_K3_KEYS
    )
    result["pass"] = (
        result["AUDIT_INPUT_PATHS_literal"]
        and result["self_plus_named_files_read"] <= result["read_limit"]
        and result["all_existing_worktree_relative"]
        and all(
            row["sha256_exact"]
            and row["git_blob_exact"]
            and row["AST_valid"]
            for row in rows
        )
        and direct_frontier_imports
        == (
            "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26",
        )
        and result["literal_claim_surface_exact"]
        and not any(name in sys.modules for name in BLOCKLISTED_MODULES)
        and not FIREWALL.hits
    )
    return result


def make_context() -> dict[str, object]:
    """Reconstruct the four landed event fixtures without primary code."""
    program = K.interleaved_program(FIXTURE_BANKS)
    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    state = K.M.pack_state(banks, links)
    allocator = K.M.global_allocator_word(FIXTURE_BANKS)
    fixtures: dict[int, State] = {}
    for event in range(2 * FIXTURE_BANKS):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = K.M.prepare_endpoint(state, direction)
        fixtures[event] = bytes(before)
        state = K.A.apply_semantic(before, allocator)
    if (
        len(program) != RING_STATIONS
        or tuple(fixtures) != (0, 1, 2, 3)
        or len(allocator) != 3106
    ):
        raise AssertionError("landed fixture construction changed")
    return {"program": program, "fixtures": fixtures}


def orbit_word(
    program: tuple[object, ...],
    positions: tuple[int, ...],
) -> tuple[object, ...]:
    """Independently concatenate the macros seen in one synchronous orbit."""
    word: list[object] = []
    for step in range(len(program)):
        live = {(position + step) % len(program) for position in positions}
        for station, row in enumerate(program):
            if station in live:
                word.extend(K.mapped_macro(row))
    return tuple(word)


def compile_gates(
    word: tuple[object, ...],
) -> tuple[tuple[int, int, int, int], ...]:
    compiled = []
    for gate in word:
        wires = tuple(map(int, gate.wires))
        if len(wires) != len(set(wires)):
            raise AssertionError(("repeated landed gate wire", gate))
        if gate.kind == "X" and len(wires) == 1:
            compiled.append((0, wires[0], 0, 0))
        elif gate.kind == "CNOT" and len(wires) == 2:
            compiled.append((1, wires[0], wires[1], 0))
        elif gate.kind == "TOF" and len(wires) == 3:
            compiled.append((2, wires[0], wires[1], wires[2]))
        else:
            raise AssertionError(("unsupported landed gate", gate))
    return tuple(compiled)


def scalar_forward(
    state: list[int],
    compiled: tuple[tuple[int, int, int, int], ...],
) -> None:
    for kind, first, second, third in compiled:
        if kind == 0:
            state[first] ^= 1
        elif kind == 1:
            state[second] ^= state[first]
        else:
            state[third] ^= state[first] & state[second]


def scalar_reverse(
    state: list[int],
    compiled: tuple[tuple[int, int, int, int], ...],
) -> None:
    for kind, first, second, third in reversed(compiled):
        if kind == 0:
            state[first] ^= 1
        elif kind == 1:
            state[second] ^= state[first]
        else:
            state[third] ^= state[first] & state[second]


def bit_slice(states: tuple[tuple[int, ...], ...]) -> list[int]:
    return [
        sum(int(state[wire]) << lane for lane, state in enumerate(states))
        for wire in range(len(states[0]))
    ]


def lane_state(columns: list[int] | tuple[int, ...], lane: int) -> State:
    return bytes((column >> lane) & 1 for column in columns)


def masked_orbit_schedule(
    program: tuple[object, ...],
    keys: tuple[Key, ...],
) -> tuple[MaskedGate, ...]:
    """Compile a fresh bit-sliced schedule; no Cycle-847 function is used."""
    rows: list[MaskedGate] = []
    for step in range(len(program)):
        live_by_lane = tuple(
            {(position + step) % len(program) for position in key[1]}
            for key in keys
        )
        for station, program_row in enumerate(program):
            mask = sum(
                1 << lane
                for lane, live in enumerate(live_by_lane)
                if station in live
            )
            if not mask:
                continue
            for gate in K.mapped_macro(program_row):
                wires = tuple(map(int, gate.wires))
                if len(wires) != len(set(wires)):
                    raise AssertionError(("repeated landed gate wire", gate))
                if gate.kind == "X" and len(wires) == 1:
                    rows.append((0, wires[0], 0, 0, mask))
                elif gate.kind == "CNOT" and len(wires) == 2:
                    rows.append((1, wires[0], wires[1], 0, mask))
                elif gate.kind == "TOF" and len(wires) == 3:
                    rows.append((2, wires[0], wires[1], wires[2], mask))
                else:
                    raise AssertionError(("unsupported landed gate", gate))
    return tuple(rows)


def advance_columns(
    columns: list[int],
    schedule: tuple[MaskedGate, ...],
) -> None:
    for kind, first, second, third, mask in schedule:
        if kind == 0:
            columns[first] ^= mask
        elif kind == 1:
            columns[second] ^= columns[first] & mask
        else:
            columns[third] ^= columns[first] & columns[second] & mask


def residual_coordinates() -> tuple[tuple[str, int], ...]:
    bank_fields = (
        ("POINTER", K.A.POINTER),
        ("U_TO_V", K.A.U_TO_V),
        ("V_TO_U", K.A.V_TO_U),
        ("DIRECTION_OK", K.A.DIRECTION_OK),
        *((f"FRESH_{index}", wire)
          for index, wire in enumerate(K.A.FRESH)),
        *((f"ZERO_WORK_{index}", wire)
          for index, wire in enumerate(K.A.ZERO_WORK)),
        ("TOKEN_OK", K.A.TOKEN_OK),
    )
    rows = [("source.SOURCE_POINTER", int(K.R3.X.SOURCE_POINTER))]
    for bank_index, base in enumerate(
        K.M.R12.BANK_BASES[:FIXTURE_BANKS]
    ):
        rows.extend(
            (f"bank{bank_index}.{name}", int(base + wire))
            for name, wire in bank_fields
        )
    for link_index, base in enumerate(
        K.M.R12.LINK_BASES[:FIXTURE_BANKS - 1]
    ):
        rows.extend(
            (f"link{link_index}.WIRE_{wire}", int(base + wire))
            for wire in range(K.B.LINK_WIDTH)
        )
    result = tuple(rows)
    indices = tuple(wire for _name, wire in result)
    if (
        len(indices) != WATCHED_COORDINATES
        or len(set(indices)) != WATCHED_COORDINATES
        or min(indices) < 0
        or max(indices) >= STATE_BITS
    ):
        raise AssertionError("landed residual coordinate basis changed")
    return result


def direct_clean(state: State | tuple[int, ...]) -> bool:
    banks, links = K.M.unpack_state(state, FIXTURE_BANKS)
    return not any((
        state[K.R3.X.SOURCE_POINTER],
        any(
            bank[wire]
            for bank in banks
            for wire in (
                K.A.POINTER,
                K.A.U_TO_V,
                K.A.V_TO_U,
                K.A.DIRECTION_OK,
                *K.A.FRESH,
                *K.A.ZERO_WORK,
                K.A.TOKEN_OK,
            )
        ),
        any(any(link) for link in links),
    ))


def dirty_lane_mask(
    columns: list[int] | tuple[int, ...],
    residual_indices: tuple[int, ...],
) -> int:
    dirty = 0
    for wire in residual_indices:
        dirty |= columns[wire]
    return dirty


def equality_lane_mask(
    columns: list[int] | tuple[int, ...],
    target_columns: list[int] | tuple[int, ...],
    candidates: int,
) -> int:
    matches = candidates
    for current, target in zip(columns, target_columns):
        matches &= ~(current ^ target)
        if not matches:
            break
    return matches


def set_lanes(mask: int) -> tuple[int, ...]:
    lanes = []
    while mask:
        bit = mask & -mask
        lanes.append(bit.bit_length() - 1)
        mask ^= bit
    return tuple(lanes)


def initial_lane(
    key: Key,
    context: dict[str, object],
    word: tuple[object, ...],
) -> tuple[State, dict[str, object]]:
    program = context["program"]
    fixture = context["fixtures"][key[2]]
    initial, rail_a, rail_b, _trace = K.run_orbit(
        fixture, program, token_positions=key[1]
    )
    state = bytes(initial)
    semantic = bytes(K.A.apply_semantic(fixture, word))
    expected_rail = tuple(
        int(station in key[1]) for station in range(RING_STATIONS)
    )
    row = {
        "key": key,
        "state_bits": len(state),
        "initial_sha256": state_sha256(state),
        "composition_exact": state == semantic,
        "rail_A_exact": rail_a == expected_rail,
        "rail_B_zero": not any(rail_b),
        "initial_landed_nonclean": not direct_clean(state),
    }
    row["pass"] = (
        len(state) == STATE_BITS
        and row["composition_exact"]
        and row["rail_A_exact"]
        and row["rail_B_zero"]
        and row["initial_landed_nonclean"]
    )
    return state, row


def checkpoint_row(
    moment: int,
    columns: list[int],
    initial_states: tuple[State, ...],
    lane_keys: tuple[Key, ...],
    residual_indices: tuple[int, ...],
) -> dict[str, object]:
    dirty = dirty_lane_mask(columns, residual_indices)
    initial_columns = bit_slice(initial_states)
    returns = equality_lane_mask(
        columns, initial_columns, (1 << len(lane_keys)) - 1
    )
    rows = []
    for lane, key in enumerate(lane_keys):
        state = lane_state(columns, lane)
        compiled_nonclean = bool(dirty & (1 << lane))
        direct_nonclean = not direct_clean(state)
        compiled_return = bool(returns & (1 << lane))
        direct_return = state == initial_states[lane]
        rows.append({
            "lane": lane,
            "key": key,
            "sha256": state_sha256(state),
            "landed_support_weight":
                sum(state[wire] for wire in residual_indices),
            "compiled_nonclean": compiled_nonclean,
            "direct_nonclean": direct_nonclean,
            "compiled_return_to_t0": compiled_return,
            "direct_return_to_t0": direct_return,
            "tests_agree":
                compiled_nonclean == direct_nonclean
                and compiled_return == direct_return,
        })
    return {
        "t": moment,
        "rows": tuple(rows),
        "tests_agree": all(row["tests_agree"] for row in rows),
        "duplicate_exact":
            rows[0]["sha256"] == rows[-1]["sha256"]
            and lane_state(columns, 0) == lane_state(columns, len(rows) - 1),
    }


def independent_spot_sweep(
    context: dict[str, object],
    residual_rows: tuple[tuple[str, int], ...],
) -> tuple[dict[str, object], dict[str, object]]:
    """Run three claimed-null keys with an independently written evolution."""
    started = monotonic()
    lane_keys = SPOT_KEYS + (DETERMINISM_KEY,)
    program = context["program"]
    positions = tuple(sorted({key[1] for key in lane_keys}))
    words = {position: orbit_word(program, position) for position in positions}
    compiled = {
        position: compile_gates(word) for position, word in words.items()
    }
    initial_pairs = tuple(
        initial_lane(key, context, words[key[1]]) for key in lane_keys
    )
    initial_states = tuple(pair[0] for pair in initial_pairs)
    construction_rows = tuple(pair[1] for pair in initial_pairs)
    columns = bit_slice(initial_states)
    initial_columns = tuple(columns)
    schedule = masked_orbit_schedule(program, lane_keys)
    one_step_columns = columns.copy()
    advance_columns(one_step_columns, schedule)
    one_step_rows = tuple({
        "lane": lane,
        "key": key,
        "exact": lane_state(one_step_columns, lane)
        == bytes(K.A.apply_semantic(
            initial_states[lane], words[key[1]]
        )),
    } for lane, key in enumerate(lane_keys))
    duplicate_schedule_lockstep = all(
        bool(mask & 1) == bool(mask & (1 << (len(lane_keys) - 1)))
        for _kind, _first, _second, _third, mask in schedule
    )
    residual_indices = tuple(wire for _name, wire in residual_rows)
    initial_dirty = dirty_lane_mask(columns, residual_indices)
    all_lanes = (1 << len(lane_keys)) - 1
    construction_pass = (
        all(row["pass"] for row in construction_rows)
        and all(row["exact"] for row in one_step_rows)
        and initial_dirty == all_lanes
        and initial_states[0] == initial_states[-1]
        and duplicate_schedule_lockstep
        and len(columns) == STATE_BITS
        and bool(schedule)
    )
    checkpoints = [
        checkpoint_row(
            0, columns, initial_states, lane_keys, residual_indices
        )
    ]
    checkpoint_times = {1, 65_536, 524_288, TARGET_T}
    events = []
    reached = 0
    for moment in range(1, TARGET_T + 1):
        advance_columns(columns, schedule)
        reached = moment
        dirty = dirty_lane_mask(columns, residual_indices)
        clean_hits = all_lanes & ~dirty
        return_hits = equality_lane_mask(
            columns, initial_columns, all_lanes & ~clean_hits
        )
        if clean_hits or return_hits:
            for lane in set_lanes(clean_hits | return_hits):
                events.append({
                    "t": moment,
                    "lane": lane,
                    "key": lane_keys[lane],
                    "role": (
                        "determinism_duplicate"
                        if lane == len(lane_keys) - 1 else "spot_primary"
                    ),
                    "event": (
                        "CLEAN_POSTIMAGE"
                        if clean_hits & (1 << lane) else "EXACT_RETURN_TO_T0"
                    ),
                    "state_sha256": state_sha256(lane_state(columns, lane)),
                })
            break
        if moment in checkpoint_times:
            checkpoints.append(checkpoint_row(
                moment, columns, initial_states, lane_keys, residual_indices
            ))
    terminal_rows = tuple({
        "key": key,
        "lane": lane,
        "state_sha256": state_sha256(lane_state(columns, lane)),
        "landed_support_weight": sum(
            lane_state(columns, lane)[wire] for wire in residual_indices
        ),
        "transitions_executed": reached,
    } for lane, key in enumerate(lane_keys))
    primary_events = tuple(
        row for row in events if row["role"] == "spot_primary"
    )
    complete_null = reached == TARGET_T and not primary_events
    coverage = {
        "finding": (
            "NO CLEAN POSTIMAGE OR EXACT T0 RETURN FOUND AT ANY INTEGER "
            "t=1..1048576 FOR ALL DECLARED SPOT KEYS"
            if complete_null else
            "MISSED RESOLUTION EVENT FOUND; PRIMARY REFUTED"
        ),
        "target_horizon": TARGET_T,
        "reached_horizon": reached,
        "selected_keys": SPOT_KEYS,
        "selected_key_count": len(SPOT_KEYS),
        "selected_trio_keys": tuple(
            key for key in SPOT_KEYS
            if key[1] in ((0, 2, 6), (0, 2, 7), (0, 2, 8))
        ),
        "selected_trio_key_count": sum(
            key[1] in ((0, 2, 6), (0, 2, 7), (0, 2, 8))
            for key in SPOT_KEYS
        ),
        "coverage":
            "t=0 initial landed nonclean; exact landed cleanliness and "
            "exact full-state return to t0 after every integer movement "
            "t=1..1048576",
        "tested_key_moments": len(SPOT_KEYS) * reached,
        "expected_key_moments": len(SPOT_KEYS) * TARGET_T,
        "events": tuple(events),
        "primary_event_count": len(primary_events),
        "construction_rows": construction_rows,
        "one_step_rows": one_step_rows,
        "checkpoints": tuple(checkpoints),
        "terminal_rows": terminal_rows[:len(SPOT_KEYS)],
        "seconds": round(monotonic() - started, 6),
    }
    coverage["pass"] = (
        construction_pass
        and len(SPOT_KEYS) >= 3
        and coverage["selected_trio_key_count"] >= 2
        and complete_null
        and coverage["tested_key_moments"]
        == coverage["expected_key_moments"]
        and not events
        and all(row["tests_agree"] for row in checkpoints)
    )
    physical_lane_word_gates = sum(
        len(compiled[key[1]]) for key in lane_keys
    )
    schedule_mask_gate_ops = sum(
        mask.bit_count()
        for _kind, _first, _second, _third, mask in schedule
    )
    accounting = {
        "finding": (
            "TRANSITION ARITHMETIC EXACT FOR THE COMPLETE DECLARED SWEEP"
            if complete_null else
            "TRANSITION ARITHMETIC REPORTED ONLY TO THE REFUTING EVENT"
        ),
        "physical_global_updates": reached,
        "expected_physical_global_updates": TARGET_T,
        "selected_primary_transition_rows": tuple({
            "key": key,
            "executed": reached,
            "expected": TARGET_T,
            "exact": reached == TARGET_T,
        } for key in SPOT_KEYS),
        "selected_primary_transitions": len(SPOT_KEYS) * reached,
        "expected_selected_primary_transitions":
            len(SPOT_KEYS) * TARGET_T,
        "claimed_ten_key_upper_if_no_terminals":
            len(ALL_K3_KEYS) * TARGET_T,
        "claimed_ten_key_arithmetic":
            f"{len(ALL_K3_KEYS)} * {TARGET_T} = "
            f"{len(ALL_K3_KEYS) * TARGET_T}",
        "schedule_instructions_per_tick": len(schedule),
        "logical_gate_applications_per_tick": schedule_mask_gate_ops,
        "sum_physical_lane_word_lengths": physical_lane_word_gates,
        "gate_accounting_exact":
            schedule_mask_gate_ops == physical_lane_word_gates,
        "physical_schedule_instructions_executed": len(schedule) * reached,
        "logical_gate_applications_executed":
            schedule_mask_gate_ops * reached,
        "no_terminal_savings_on_spot_keys": not primary_events,
    }
    accounting["pass"] = (
        reached == TARGET_T
        and accounting["selected_primary_transitions"]
        == accounting["expected_selected_primary_transitions"]
        and all(
            row["exact"]
            for row in accounting["selected_primary_transition_rows"]
        )
        and accounting["claimed_ten_key_upper_if_no_terminals"]
        == 10_485_760
        and accounting["gate_accounting_exact"]
        and accounting["no_terminal_savings_on_spot_keys"]
    )
    determinism = {
        "declared_slice": (DETERMINISM_KEY,),
        "scope": "duplicate lanes from t=0 through complete T=1048576",
        "primary_lane": 0,
        "duplicate_lane": len(lane_keys) - 1,
        "initial_exact": initial_states[0] == initial_states[-1],
        "schedule_masks_lockstep": duplicate_schedule_lockstep,
        "checkpoint_exact": all(
            row["duplicate_exact"] for row in checkpoints
        ),
        "terminal_exact":
            lane_state(columns, 0)
            == lane_state(columns, len(lane_keys) - 1),
        "terminal_primary_sha256": terminal_rows[0]["state_sha256"],
        "terminal_duplicate_sha256": terminal_rows[-1]["state_sha256"],
    }
    determinism["pass"] = all((
        determinism["initial_exact"],
        determinism["schedule_masks_lockstep"],
        determinism["checkpoint_exact"],
        determinism["terminal_exact"],
        reached == TARGET_T,
    ))
    coverage["determinism"] = determinism
    return coverage, accounting


def equality_partition(states: tuple[State, ...]) -> Partition:
    groups: dict[State, list[int]] = {}
    for lane, state in enumerate(states):
        groups.setdefault(state, []).append(lane)
    return tuple(
        tuple(group)
        for group in sorted(groups.values(), key=lambda group: group[0])
    )


def restrict_partition_direct(
    partition: Partition,
    subset: tuple[int, int, int],
) -> Partition:
    relabel = {old: new for new, old in enumerate(subset)}
    blocks = []
    for block in partition:
        reduced = tuple(relabel[lane] for lane in block if lane in relabel)
        if reduced:
            blocks.append(reduced)
    return tuple(sorted(blocks, key=lambda block: block[0]))


def restriction_chain(
    rows: tuple[tuple[tuple[int, int, int], tuple[Partition, ...]], ...],
) -> str:
    chain = sha256(b"CYCLE847-84-RESTRICTIONS-v1").digest()
    for ordinal, (subset, sequence) in enumerate(rows):
        payload = compact((ordinal, subset, sequence)).encode("utf-8")
        chain = sha256(chain + payload).digest()
    return chain.hex()


def independent_braid_arming(
    context: dict[str, object],
) -> dict[str, object]:
    """Build the nine-braid and verify all 84 restrictions by two routes."""
    started = monotonic()
    program = context["program"]
    fixture = context["fixtures"][0]
    keys = tuple((2, pair, 0) for pair in BACKBONE)
    words = {pair: orbit_word(program, pair) for pair in BACKBONE}
    compiled = {
        pair: compile_gates(words[pair]) for pair in BACKBONE
    }
    initial_states = []
    construction_rows = []
    for key in keys:
        pair = key[1]
        initial, rail_a, rail_b, _trace = K.run_orbit(
            fixture, program, token_positions=pair
        )
        state = bytes(initial)
        expected_rail = tuple(
            int(station in pair) for station in range(RING_STATIONS)
        )
        construction_rows.append({
            "key": key,
            "composition_exact":
                state == bytes(K.A.apply_semantic(fixture, words[pair])),
            "rail_A_exact": rail_a == expected_rail,
            "rail_B_zero": not any(rail_b),
        })
        initial_states.append(state)
    columns = bit_slice(tuple(initial_states))
    schedule = masked_orbit_schedule(program, keys)
    for _moment in range(FUNNEL_T):
        advance_columns(columns, schedule)
    funnel_states = tuple(
        lane_state(columns, lane) for lane in range(len(keys))
    )
    depth_states = [funnel_states]
    roundtrip_exact = True
    current = funnel_states
    for _depth in range(1, BRAID_DEPTH + 1):
        predecessors = []
        for pair, state in zip(BACKBONE, current):
            predecessor = list(state)
            scalar_reverse(predecessor, compiled[pair])
            replay = predecessor.copy()
            scalar_forward(replay, compiled[pair])
            roundtrip_exact &= bytes(replay) == state
            predecessors.append(bytes(predecessor))
        current = tuple(predecessors)
        depth_states.append(current)
    depth_states_tuple = tuple(depth_states)
    nine_braid = tuple(
        equality_partition(states) for states in depth_states_tuple
    )
    subsets = tuple(combinations(range(len(BACKBONE)), 3))
    route_a = tuple(
        (
            subset,
            tuple(
                restrict_partition_direct(partition, subset)
                for partition in nine_braid
            ),
        )
        for subset in subsets
    )
    route_b = tuple(
        (
            subset,
            tuple(
                equality_partition(tuple(states[lane] for lane in subset))
                for states in depth_states_tuple
            ),
        )
        for subset in subsets
    )
    route_a_map = dict(route_a)
    route_b_map = dict(route_b)
    per_restriction_rows = tuple({
        "ordinal": ordinal,
        "subset": subset,
        "backbone_subset": tuple(BACKBONE[lane] for lane in subset),
        "sha256": digest(route_a_map[subset]),
        "direct_state_sha256": digest(route_b_map[subset]),
        "routes_exact": route_a_map[subset] == route_b_map[subset],
    } for ordinal, subset in enumerate(subsets))
    nine_braid_sha = digest(tuple(enumerate(nine_braid)))
    aggregate_sha = digest(route_a)
    route_a_chain = restriction_chain(route_a)
    route_b_chain = restriction_chain(route_b)
    funnel = funnel_states[0]
    all_nine_equal = len(set(funnel_states)) == 1
    result = {
        "finding":
            "84/84 DIRECT THREE-KEY RESTRICTIONS RECONSTRUCTED; "
            "SHA CHAINS AGREE; BRAID CLAUSE WAS ARMED",
        "lineage":
            "event-0 nine-braid rebuilt only from the landed Cycle-719 "
            "core; Cycle-847/838/844 remained text/AST-only",
        "event": 0,
        "funnel_t": FUNNEL_T,
        "keys": keys,
        "depth_bounds": (0, BRAID_DEPTH),
        "construction_exact": all(
            row["composition_exact"]
            and row["rail_A_exact"]
            and row["rail_B_zero"]
            for row in construction_rows
        ),
        "funnel_all_nine_equal": all_nine_equal,
        "funnel_state_sha256": state_sha256(funnel),
        "expected_funnel_state_sha256": EXPECTED_FUNNEL_SHA256,
        "funnel_weight": sum(funnel),
        "expected_funnel_weight": 44,
        "nine_braid_sha256": nine_braid_sha,
        "expected_nine_braid_sha256": EXPECTED_BRAID_SHA256,
        "restriction_count": len(subsets),
        "expected_restriction_count": 84,
        "restriction_combinatorics":
            "C(9,3) = 9*8*7/(3*2*1) = 84",
        "restriction_aggregate_sha256": aggregate_sha,
        "restriction_rolling_sha256": route_a_chain,
        "direct_state_rolling_sha256": route_b_chain,
        "restriction_sha_chain_exact": route_a_chain == route_b_chain,
        "all_restriction_routes_exact": all(
            row["routes_exact"] for row in per_restriction_rows
        ),
        "unique_restricted_braid_count": len({
            row["sha256"] for row in per_restriction_rows
        }),
        "per_restriction_sha256": tuple(
            (row["ordinal"], row["subset"], row["sha256"])
            for row in per_restriction_rows
        ),
        "reverse_forward_roundtrip_exact": roundtrip_exact,
        "seconds": round(monotonic() - started, 6),
    }
    result["pass"] = (
        result["construction_exact"]
        and all_nine_equal
        and result["funnel_state_sha256"] == EXPECTED_FUNNEL_SHA256
        and result["funnel_weight"] == result["expected_funnel_weight"]
        and nine_braid_sha == EXPECTED_BRAID_SHA256
        and len(subsets) == 84
        and result["restriction_sha_chain_exact"]
        and result["all_restriction_routes_exact"]
        and all(
            row["sha256"] == row["direct_state_sha256"]
            for row in per_restriction_rows
        )
        and roundtrip_exact
    )
    return result


def render(
    certificates: tuple[tuple[str, dict[str, object]], ...],
    summary: dict[str, object],
) -> str:
    lines = tuple(
        f"CERTIFICATE {name} "
        f"{'PASS' if certificate['pass'] else 'FAIL'} "
        f"{compact(certificate)}"
        for name, certificate in certificates
    )
    return "\n".join((
        *lines,
        "SUMMARY_JSON " + compact(summary),
        str(summary["terminal"]),
        "",
    ))


def stable_output(
    certificates: tuple[tuple[str, dict[str, object]], ...],
    summary: dict[str, object],
    controls: dict[str, object],
) -> str:
    for _attempt in range(20):
        output = render(certificates, summary)
        size = len(output.encode("utf-8"))
        if (
            controls["stdout_bytes"] == size
            and summary["stdout_bytes"] == size
        ):
            return output
        controls["stdout_bytes"] = size
        summary["stdout_bytes"] = size
    raise AssertionError("stdout byte-count fixed point did not converge")


def run() -> int:
    script_started = monotonic()
    sources = source_controls()
    context = make_context()
    residual_rows = residual_coordinates()
    braid = independent_braid_arming(context)
    coverage, accounting = independent_spot_sweep(context, residual_rows)
    spot_trio_events = tuple(
        event for event in coverage["events"]
        if event["key"] in coverage["selected_trio_keys"]
    )
    braid["spot_trio_resolution_events"] = spot_trio_events
    braid["braid_clause_disposition"] = (
        "NOT_TRIGGERED_ON_COMPLETE_SPOT_SWEEP"
        if not spot_trio_events else
        "SPOT_RESOLUTION_FOUND; PRIMARY NULL REFUTED"
    )
    braid["pass"] = (
        braid["pass"]
        and (
            not spot_trio_events
            or coverage["finding"]
            == "MISSED RESOLUTION EVENT FOUND; PRIMARY REFUTED"
        )
    )
    elapsed = monotonic() - script_started
    controls = {
        "finding":
            "SHAS EXACT; SOURCE PRIMARIES BLOCKLISTED TEXT/AST-ONLY; "
            "DECLARED DETERMINISM SLICE EXACT; PATH/RUNTIME/STDOUT "
            "CONTROLS SATISFIED",
        "sources": sources,
        "residual_basis": {
            "state_bits": STATE_BITS,
            "coordinate_count": len(residual_rows),
            "unique_coordinate_count":
                len({wire for _name, wire in residual_rows}),
            "basis_sha256": digest(residual_rows),
            "zero_state_clean": direct_clean(bytes(STATE_BITS)),
        },
        "determinism": coverage["determinism"],
        "blocked_modules_loaded_at_end": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits_at_end": tuple(FIREWALL.hits),
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": RUNTIME_LIMIT_SECONDS,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
    }
    controls_base = (
        sources["pass"]
        and controls["residual_basis"]["coordinate_count"]
        == WATCHED_COORDINATES
        and controls["residual_basis"]["unique_coordinate_count"]
        == WATCHED_COORDINATES
        and controls["residual_basis"]["zero_state_clean"]
        and controls["determinism"]["pass"]
        and not controls["blocked_modules_loaded_at_end"]
        and not controls["firewall_hits_at_end"]
        and elapsed < RUNTIME_LIMIT_SECONDS
    )
    controls["pass"] = controls_base
    certificates = (
        ("NULL_SPOT_COVERAGE", coverage),
        ("THE_ACCOUNTING", accounting),
        ("THE_BRAID_CLAUSE_ARMING", braid),
        ("CONTROLS", controls),
    )
    all_pass = all(certificate["pass"] for _name, certificate in certificates)
    refuted = bool(coverage["events"])
    summary = {
        "cycle": 847,
        "checker": Path(__file__).name,
        "spot_key_count": len(SPOT_KEYS),
        "spot_trio_key_count": coverage["selected_trio_key_count"],
        "complete_horizon": coverage["reached_horizon"],
        "missed_event_count": len(coverage["events"]),
        "primary_refuted": refuted,
        "universal_braid_sha256": braid["nine_braid_sha256"],
        "restriction_count": braid["restriction_count"],
        "restriction_rolling_sha256":
            braid["restriction_rolling_sha256"],
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": RUNTIME_LIMIT_SECONDS,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "pass": all_pass,
        "terminal": (
            "CYCLE847_MILLION_PRIMARY_REFUTED"
            if refuted else (
                "CYCLE847_MILLION_INDEPENDENT_CHECK_PASS"
                if all_pass else
                "CYCLE847_MILLION_INDEPENDENT_CHECK_FAIL"
            )
        ),
    }
    output = stable_output(certificates, summary, controls)
    stdout_ok = len(output.encode("utf-8")) < STDOUT_LIMIT_BYTES
    controls["pass"] = controls_base and stdout_ok
    all_pass = all(certificate["pass"] for _name, certificate in certificates)
    summary["pass"] = all_pass
    summary["terminal"] = (
        "CYCLE847_MILLION_PRIMARY_REFUTED"
        if refuted else (
            "CYCLE847_MILLION_INDEPENDENT_CHECK_PASS"
            if all_pass else "CYCLE847_MILLION_INDEPENDENT_CHECK_FAIL"
        )
    )
    output = stable_output(certificates, summary, controls)
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        sys.stdout.write(compact({
            "pass": False,
            "failure": "stdout limit exceeded",
            "stdout_bytes": len(output.encode("utf-8")),
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
            "terminal": "CYCLE847_MILLION_INDEPENDENT_CHECK_FAIL",
        }) + "\n")
        return 1
    sys.stdout.write(output)
    return 0 if all_pass else 1


def main() -> int:
    try:
        return run()
    except Exception as error:
        sys.stdout.write(compact({
            "pass": False,
            "exception_type": type(error).__name__,
            "exception": str(error),
            "terminal": "CYCLE847_MILLION_INDEPENDENT_CHECK_FAIL",
        }) + "\n")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
