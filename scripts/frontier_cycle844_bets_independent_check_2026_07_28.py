#!/usr/bin/env python3
"""Cycle 844 independent adversarial check: the pair and the bets.

Only the landed Cycle-719 controller core is executable.  The Cycle-831,
834, 843, and 844 science primaries are SHA-pinned, parsed as text/AST, and
blocked from import.  Dynamics, resolution bookkeeping, the million-tick
funnel, null spots, and target-state visits are recomputed here.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
STDOUT_LIMIT_BYTES = 150_000
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle831_deep_k2_forecast_tests_2026_07_28.py",
    "scripts/frontier_cycle834_k3_backbone_2026_07_28.py",
    "scripts/frontier_cycle843_pulse_phase_2026_07_28.py",
    "scripts/frontier_cycle844_standing_bets_2026_07_28.py",
)

import ast
from collections import Counter, deque
from hashlib import sha1, sha256
import importlib.abc
import json
from pathlib import Path
import sys
from time import monotonic
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
CORE_PATH = AUDIT_INPUT_PATHS[0]
TEXT_AST_ONLY_PATHS = AUDIT_INPUT_PATHS[1:]
BLOCKLISTED_MODULES = tuple(Path(path).stem for path in TEXT_AST_ONLY_PATHS)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "624dad4d841e10e24891810dbc500cc4d6ebe871d6f09dd96f89e3189e52e2ff",
    AUDIT_INPUT_PATHS[2]:
        "8ed75c4e6f19fa5e8a9492225aae681ab85017dcfac00f8ab109b7c587aeddaa",
    AUDIT_INPUT_PATHS[3]:
        "68116221b3451aefd294d939b788cd3dbf518a190eaebd996b43fba5e8a54de9",
    AUDIT_INPUT_PATHS[4]:
        "6c52e0d8db9b4b7ecf91b3c5b17436036c89ff18def2f951fb2ee0db8e2a19f9",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    AUDIT_INPUT_PATHS[1]: "ef24edda08118c4e14439b899790fff6c6f94175",
    AUDIT_INPUT_PATHS[2]: "89d4506c6df9738bf0458027ab76cc9d2f9710ab",
    AUDIT_INPUT_PATHS[3]: "cd500d58847c3c1046c500b73b25911920db0ce0",
    AUDIT_INPUT_PATHS[4]: "a12245720a7e866134978c25629e19ba57596929",
}


class _SourcePrimaryFirewall(importlib.abc.MetaPathFinder):
    """Fail closed if a text/AST-only science primary is imported."""

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


FIREWALL = _SourcePrimaryFirewall()
sys.meta_path.insert(0, FIREWALL)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


State = bytes
Key = tuple[int, tuple[int, ...], int]
Lane = tuple[Key, str]
CompiledGate = tuple[int, int, int, int]
MaskedGate = tuple[int, int, int, int, int]
RING_STATIONS = 11
FIXTURE_BANKS = 2
STATE_BITS = 5815
PAIR_RESOLUTION = 1_142_432
PAIR_STOP = PAIR_RESOLUTION + 6
NULL_HORIZON = 524_288
CHECKPOINT_STRIDE = 4096
PAIR_KEYS: tuple[Key, ...] = (
    (2, (0, 5), 0),
    (2, (0, 6), 0),
)
STATION_ZERO_KEYS: tuple[Key, ...] = tuple(
    (2, pair, event)
    for event in range(4)
    for pair in ((0, 5), (0, 6))
)
NULL_KEYS: tuple[Key, ...] = (
    (3, (0, 2, 6), 2),
    (3, (0, 2, 6), 3),
)
EXPECTED_NAMED = {
    "S_star": (
        44,
        "cdf7e03092c6278b686c1f0edb9ebd716f4a285b1eabc8a7e2780695284a8f1a",
    ),
    "S2": (
        45,
        "0015151ee4b751c35a5671fbb4f301d8569e78fc5a7ebe9f77372865b153c99b",
    ),
    "S1": (
        46,
        "797fa122a629177c00c707aff4857d01bbad16b078983e3a6f1f5b632e094a41",
    ),
    "S0_prime": (
        47,
        "d874aeeb1d4e5ca29b806886314c796ac32e6658b21f888d8e2aa01044905c12",
    ),
    "funnel_weight_51": (51, None),
    "funnel_weight_57": (57, None),
    "pulse_coincidence_state": (
        59,
        "4a7ce9fd4e9ebfdbd8580c33122d9e87c3896b24ef196e34bec49e233d044375",
    ),
}


def compact(value: object) -> str:
    def json_ready(item: object) -> object:
        if isinstance(item, dict):
            return {
                (
                    key
                    if isinstance(key, (str, int, float, bool))
                    or key is None
                    else repr(key)
                ): json_ready(entry)
                for key, entry in item.items()
            }
        if isinstance(item, (tuple, list)):
            return [json_ready(entry) for entry in item]
        return item

    return json.dumps(
        json_ready(value),
        sort_keys=True,
        separators=(",", ":"),
        default=str,
    )


def state_sha256(state: State | Iterable[int]) -> str:
    return sha256(bytes(state)).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(
        f"blob {len(payload)}\0".encode("ascii") + payload
    ).hexdigest()


def literal_assignment(tree: ast.Module, name: str) -> object | None:
    values: list[ast.expr] = []
    for node in tree.body:
        if (
            isinstance(node, ast.Assign)
            and any(
                isinstance(target, ast.Name) and target.id == name
                for target in node.targets
            )
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
    payloads = {
        path: (ROOT / path).read_bytes()
        for path in AUDIT_INPUT_PATHS
        if not Path(path).is_absolute() and (ROOT / path).is_file()
    }
    trees = {
        path: ast.parse(payload, filename=path)
        for path, payload in payloads.items()
    }
    self_tree = ast.parse(
        Path(__file__).read_bytes(), filename=Path(__file__).name
    )
    source_rows = tuple({
        "path": path,
        "exists_worktree_relative":
            not Path(path).is_absolute() and (ROOT / path).is_file(),
        "sha256": sha256(payloads[path]).hexdigest(),
        "sha256_exact":
            sha256(payloads[path]).hexdigest() == EXPECTED_SHA256[path],
        "git_blob": git_blob(payloads[path]),
        "git_blob_exact":
            git_blob(payloads[path]) == EXPECTED_GIT_BLOBS[path],
        "mode": (
            "EXECUTABLE_LANDED_CORE"
            if path == CORE_PATH else "TEXT_AST_ONLY_BLOCKLISTED"
        ),
        "AST_valid": isinstance(trees[path], ast.Module),
    } for path in AUDIT_INPUT_PATHS)
    direct_frontier_imports = tuple(
        alias.name
        for node in self_tree.body if isinstance(node, ast.Import)
        for alias in node.names
        if alias.name.startswith("frontier_cycle")
    )
    controls = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_INPUT_PATHS_literal":
            literal_assignment(self_tree, "AUDIT_INPUT_PATHS")
            == AUDIT_INPUT_PATHS,
        "all_paths_existing_worktree_relative":
            len(payloads) == len(AUDIT_INPUT_PATHS)
            and all(row["exists_worktree_relative"] for row in source_rows),
        "source_rows": source_rows,
        "text_AST_only_paths": TEXT_AST_ONLY_PATHS,
        "blocked_modules": BLOCKLISTED_MODULES,
        "direct_frontier_imports": direct_frontier_imports,
        "trees": trees,
    }
    controls["pass"] = (
        controls["AUDIT_INPUT_PATHS_literal"]
        and controls["all_paths_existing_worktree_relative"]
        and all(
            row["sha256_exact"]
            and row["git_blob_exact"]
            and row["AST_valid"]
            for row in source_rows
        )
        and direct_frontier_imports
        == (
            "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26",
        )
        and not any(name in sys.modules for name in BLOCKLISTED_MODULES)
        and not FIREWALL.hits
    )
    return controls


def build_context() -> dict[str, object]:
    """Rebuild the four prepared epochs directly from the landed core."""

    program = K.interleaved_program(FIXTURE_BANKS)
    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    state = K.M.pack_state(banks, links)
    allocator = K.M.global_allocator_word(FIXTURE_BANKS)
    fixtures = []
    for event in range(2 * FIXTURE_BANKS):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = K.M.prepare_endpoint(state, direction)
        fixtures.append((event, direction, before))
        state = K.A.apply_semantic(before, allocator)
    return {
        "program": program,
        "fixtures": tuple(fixtures),
        "pass": (
            len(program) == RING_STATIONS
            and tuple(row[0] for row in fixtures) == (0, 1, 2, 3)
            and len(allocator) == 3106
        ),
    }


def orbit_word(
    program: tuple[object, ...],
    positions0: tuple[int, ...],
) -> tuple[object, ...]:
    positions = tuple(positions0)
    word = []
    for _movement in range(len(program)):
        live = set(positions)
        for station, row in enumerate(program):
            if station in live:
                word.extend(K.mapped_macro(row))
        positions = tuple(
            (position + 1) % len(program) for position in positions
        )
    return tuple(word)


def compile_word(word: tuple[object, ...]) -> tuple[CompiledGate, ...]:
    rows = []
    for gate in word:
        wires = tuple(int(wire) for wire in gate.wires)
        if len(set(wires)) != len(wires):
            raise AssertionError(("repeated landed gate wire", gate))
        if gate.kind == "X" and len(wires) == 1:
            rows.append((0, wires[0], 0, 0))
        elif gate.kind == "CNOT" and len(wires) == 2:
            rows.append((1, wires[0], wires[1], 0))
        elif gate.kind == "TOF" and len(wires) == 3:
            rows.append((2, wires[0], wires[1], wires[2]))
        else:
            raise AssertionError(("unsupported landed gate", gate))
    return tuple(rows)


def advance_scalar(
    state: list[int],
    compiled: tuple[CompiledGate, ...],
) -> None:
    for kind, first, second, third in compiled:
        if kind == 0:
            state[first] ^= 1
        elif kind == 1:
            state[second] ^= state[first]
        else:
            state[third] ^= state[first] & state[second]


def pack_states(states: tuple[State, ...]) -> list[int]:
    return [
        sum(state[wire] << lane for lane, state in enumerate(states))
        for wire in range(len(states[0]))
    ]


def unpack_lane(columns: list[int], lane: int) -> State:
    return bytes((column >> lane) & 1 for column in columns)


def lane_mask_rows(mask: int) -> tuple[int, ...]:
    rows = []
    while mask:
        bit = mask & -mask
        rows.append(bit.bit_length() - 1)
        mask ^= bit
    return tuple(rows)


def compile_masked_schedule(
    program: tuple[object, ...],
    lanes: tuple[Lane, ...],
) -> tuple[MaskedGate, ...]:
    """Compile the synchronous program without calling any primary helper."""

    rows: list[MaskedGate] = []
    for movement in range(len(program)):
        for station, program_row in enumerate(program):
            mask = 0
            for lane, (key, _role) in enumerate(lanes):
                if station in {
                    (position + movement) % len(program)
                    for position in key[1]
                }:
                    mask |= 1 << lane
            if not mask:
                continue
            for gate in K.mapped_macro(program_row):
                wires = tuple(int(wire) for wire in gate.wires)
                if gate.kind == "X" and len(wires) == 1:
                    rows.append((0, wires[0], 0, 0, mask))
                elif gate.kind == "CNOT" and len(wires) == 2:
                    rows.append((1, wires[0], wires[1], 0, mask))
                elif gate.kind == "TOF" and len(wires) == 3:
                    rows.append(
                        (2, wires[0], wires[1], wires[2], mask)
                    )
                else:
                    raise AssertionError(("unsupported landed gate", gate))
    return tuple(rows)


def advance_packed(
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


def equality_mask(
    columns: list[int],
    targets: tuple[State, ...],
    candidates: int,
) -> int:
    """Exact per-lane equality against that lane's own target state."""

    matches = candidates
    for wire, values in enumerate(zip(*targets)):
        want_one = sum(
            int(value) << lane for lane, value in enumerate(values)
        )
        matches &= ~(columns[wire] ^ want_one)
        if not matches:
            return 0
    return matches


def residual_indices() -> tuple[int, ...]:
    bank_wires = (
        K.A.POINTER,
        K.A.U_TO_V,
        K.A.V_TO_U,
        K.A.DIRECTION_OK,
        *K.A.FRESH,
        *K.A.ZERO_WORK,
        K.A.TOKEN_OK,
    )
    indices = [int(K.R3.X.SOURCE_POINTER)]
    for base in K.M.R12.BANK_BASES[:FIXTURE_BANKS]:
        indices.extend(int(base + wire) for wire in bank_wires)
    for base in K.M.R12.LINK_BASES[:FIXTURE_BANKS - 1]:
        indices.extend(
            int(base + wire) for wire in range(K.B.LINK_WIDTH)
        )
    return tuple(indices)


def nonclean_mask(
    columns: list[int],
    indices: tuple[int, ...],
) -> int:
    mask = 0
    for wire in indices:
        mask |= columns[wire]
    return mask


def is_clean(state: State, indices: tuple[int, ...]) -> bool:
    return not any(state[wire] for wire in indices)


def component_weights(state: State) -> dict[str, object]:
    source_width = K.M.R12.SOURCE_WIDTH
    bank0 = K.M.R12.BANK_BASES[0]
    bank1 = K.M.R12.BANK_BASES[1]
    link0 = K.M.R12.LINK_BASES[0]
    return {
        "full": sum(state),
        "source": sum(state[:source_width]),
        "bank0": sum(state[bank0:bank0 + K.A.N]),
        "bank1": sum(state[bank1:bank1 + K.A.N]),
        "link0": sum(state[link0:link0 + K.B.LINK_WIDTH]),
    }


def diff_summary(left: State, right: State) -> dict[str, object]:
    source_width = K.M.R12.SOURCE_WIDTH
    bank0 = K.M.R12.BANK_BASES[0]
    bank1 = K.M.R12.BANK_BASES[1]
    link0 = K.M.R12.LINK_BASES[0]
    counts: Counter[str] = Counter()
    for wire, (left_bit, right_bit) in enumerate(zip(left, right)):
        if left_bit == right_bit:
            continue
        if wire < source_width:
            counts["source"] += 1
        elif bank0 <= wire < bank0 + K.A.N:
            counts["bank0"] += 1
        elif bank1 <= wire < bank1 + K.A.N:
            counts["bank1"] += 1
        elif link0 <= wire < link0 + K.B.LINK_WIDTH:
            counts["link0"] += 1
        else:
            counts["padding"] += 1
    return {
        "left_weight": sum(left),
        "right_weight": sum(right),
        "xor_weight": sum(counts.values()),
        "component_xor_weights": dict(sorted(counts.items())),
    }


def watch_window(target: State) -> tuple[int, ...]:
    active = tuple(wire for wire, bit in enumerate(target) if bit)
    inactive = tuple(wire for wire, bit in enumerate(target) if not bit)
    return tuple(sorted((*active[:8], *inactive[::193][:8])))


def watch_matches(
    columns: list[int],
    lane: int,
    target: State,
    window: tuple[int, ...],
) -> tuple[bool, bool]:
    candidate = all(
        ((columns[wire] >> lane) & 1) == target[wire]
        for wire in window
    )
    return candidate, candidate and unpack_lane(columns, lane) == target


def reconstruct_named_states(
    context: dict[str, object],
) -> dict[str, object]:
    program = context["program"]
    fixtures = context["fixtures"]
    word = orbit_word(program, (1, 6))
    compiled = compile_word(word)
    event_order = (0, 2, 1)
    states = tuple(
        bytes(K.A.apply_semantic(fixtures[event][2], word))
        for event in event_order
    )
    columns = pack_states(states)
    all_lanes = (1 << len(states)) - 1
    uniform_schedule = tuple(
        (*gate, all_lanes) for gate in compiled
    )
    capture_at = {
        14739: ("S_star", 0),
        14744: ("funnel_weight_51", 0),
        14748: ("funnel_weight_57", 0),
        33190: ("S2", 1),
        51110: ("S1", 2),
    }
    named: dict[str, State] = {}
    for moment in range(1, max(capture_at) + 1):
        advance_packed(columns, uniform_schedule)
        if moment in capture_at:
            name, lane = capture_at[moment]
            named[name] = unpack_lane(columns, lane)
    s0_prime = bytearray(named["S1"])
    s0_prime[K.M.R12.BANK_BASES[0] + K.A.HEAD[1]] ^= 1
    named["S0_prime"] = bytes(s0_prime)
    named["pulse_coincidence_state"] = bytes(fixtures[3][2])
    rows = {
        name: {
            "weight": sum(state),
            "sha256": state_sha256(state),
            "expected_weight": EXPECTED_NAMED[name][0],
            "expected_sha256": EXPECTED_NAMED[name][1],
        }
        for name, state in named.items()
    }
    exact = all(
        row["weight"] == row["expected_weight"]
        and (
            row["expected_sha256"] is None
            or row["sha256"] == row["expected_sha256"]
        )
        for row in rows.values()
    )
    return {
        "states": named,
        "rows": rows,
        "pass": exact and len(named) == len(EXPECTED_NAMED),
    }


def build_initial_family(
    keys: tuple[Key, ...],
    context: dict[str, object],
) -> tuple[
    tuple[State, ...],
    dict[tuple[int, ...], tuple[object, ...]],
    dict[tuple[int, ...], tuple[CompiledGate, ...]],
    tuple[dict[str, object], ...],
]:
    program = context["program"]
    fixtures = context["fixtures"]
    words = {
        positions: orbit_word(program, positions)
        for positions in sorted({key[1] for key in keys})
    }
    compiled = {
        positions: compile_word(word)
        for positions, word in words.items()
    }
    states = []
    rows = []
    for key in keys:
        k, positions, event = key
        state, rail_a, rail_b, _trace = K.run_orbit(
            fixtures[event][2],
            program,
            token_positions=positions,
        )
        state_bytes = bytes(state)
        expected_rail = tuple(
            int(station in positions)
            for station in range(RING_STATIONS)
        )
        semantic = bytes(
            K.A.apply_semantic(fixtures[event][2], words[positions])
        )
        states.append(state_bytes)
        rows.append({
            "key": key,
            "k_matches": k == len(positions),
            "rail_A_exact": rail_a == expected_rail,
            "rail_B_zero": not any(rail_b),
            "composition_exact": state_bytes == semantic,
        })
    return tuple(states), words, compiled, tuple(rows)


def record_resolution(
    key: Key,
    outcome: str,
    moment: int,
    state: State,
    prefix_nonclean: int,
    initial_state: State,
    indices: tuple[int, ...],
) -> dict[str, object]:
    if outcome == "TRANSIENT":
        verification = {
            "all_earlier_integer_moments_nonclean":
                prefix_nonclean == moment,
            "terminal_clean": is_clean(state, indices),
            "terminal_not_initial": state != initial_state,
        }
        period = None
    elif outcome == "CYCLE":
        verification = {
            "all_cycle_phases_nonclean":
                prefix_nonclean == moment and not is_clean(state, indices),
            "exact_return_to_t0": state == initial_state,
            "minimal_period_by_every_earlier_return_rejected": True,
        }
        period = moment
    else:
        raise AssertionError(("unknown resolution", outcome))
    verification["pass"] = all(verification.values())
    return {
        "key": key,
        "outcome": outcome,
        "resolution_moment": moment,
        "first_clean_t": moment if outcome == "TRANSIENT" else None,
        "minimal_state_period": period,
        "state_sha256": state_sha256(state),
        "component_weights": component_weights(state),
        "verification": verification,
    }


def scan_station_zero_family(
    context: dict[str, object],
    indices: tuple[int, ...],
    named: dict[str, object],
) -> dict[str, object]:
    """Scan eight station-zero keys plus one declared duplicate lane."""

    duplicate_key = PAIR_KEYS[0]
    lanes: tuple[Lane, ...] = (
        tuple((key, "primary") for key in STATION_ZERO_KEYS)
        + ((duplicate_key, "determinism_duplicate"),)
    )
    lane_keys = tuple(key for key, _role in lanes)
    initial, words, compiled, construction_rows = build_initial_family(
        lane_keys, context
    )
    columns = pack_states(initial)
    schedule = compile_masked_schedule(context["program"], lanes)
    one_step = columns.copy()
    advance_packed(one_step, schedule)
    one_step_exact = all(
        unpack_lane(one_step, lane)
        == bytes(K.A.apply_semantic(
            initial[lane], words[key[1]]
        ))
        for lane, (key, _role) in enumerate(lanes)
    )
    primary_count = len(STATION_ZERO_KEYS)
    active = (1 << primary_count) - 1
    initial_nonclean = nonclean_mask(columns, indices)
    prefix_nonclean = [1] * primary_count
    records: dict[Key, dict[str, object]] = {}
    pair_lanes = (0, 1)
    captured: dict[int, dict[int, State]] = {
        lane: {} for lane in pair_lanes
    }
    target_states = named["states"]
    watch_names = (
        "funnel_weight_51",
        "funnel_weight_57",
        "S0_prime",
        "pulse_coincidence_state",
    )
    watch_windows = {
        name: watch_window(target_states[name]) for name in watch_names
    }
    watch_stats = {
        (lane, name): {
            "key": lanes[lane][0],
            "target": name,
            "moments_tested": 0,
            "window_candidates": 0,
            "exact_hits": [],
        }
        for lane in pair_lanes
        for name in watch_names
        if lane == 0 or name.startswith("funnel_")
    }
    determinism = {
        "declared_slice": duplicate_key,
        "primary_lane": 0,
        "duplicate_lane": primary_count,
        "checkpoints_tested": 0,
        "all_checkpoint_states_equal": True,
        "first_mismatch": None,
    }
    scalar_post: dict[int, list[int]] = {}
    scalar_post_rows: dict[int, list[dict[str, object]]] = {
        lane: [] for lane in pair_lanes
    }

    def update_watches(moment: int) -> None:
        for (lane, name), row in watch_stats.items():
            row["moments_tested"] += 1
            candidate, exact = watch_matches(
                columns,
                lane,
                target_states[name],
                watch_windows[name],
            )
            row["window_candidates"] += int(candidate)
            if exact:
                row["exact_hits"].append(moment)

    def update_determinism(moment: int) -> None:
        determinism["checkpoints_tested"] += 1
        equal = all(
            ((column >> determinism["primary_lane"]) & 1)
            == ((column >> determinism["duplicate_lane"]) & 1)
            for column in columns
        )
        determinism["all_checkpoint_states_equal"] &= equal
        if not equal and determinism["first_mismatch"] is None:
            determinism["first_mismatch"] = moment

    update_watches(0)
    update_determinism(0)
    started = monotonic()
    for moment in range(1, PAIR_STOP + 1):
        advance_packed(columns, schedule)
        current_nonclean = nonclean_mask(columns, indices)
        update_watches(moment)
        if (
            moment % CHECKPOINT_STRIDE == 0
            or moment in (PAIR_RESOLUTION - 5, PAIR_RESOLUTION, PAIR_STOP)
        ):
            update_determinism(moment)
        if moment >= PAIR_RESOLUTION - 10:
            for lane in pair_lanes:
                captured[lane][moment] = unpack_lane(columns, lane)

        clean_hits = active & ~current_nonclean
        recurrence_hits = equality_mask(
            columns, initial, active & ~clean_hits
        )
        for lane in lane_mask_rows(clean_hits):
            state = unpack_lane(columns, lane)
            key = STATION_ZERO_KEYS[lane]
            records[key] = record_resolution(
                key,
                "TRANSIENT",
                moment,
                state,
                prefix_nonclean[lane],
                initial[lane],
                indices,
            )
        for lane in lane_mask_rows(recurrence_hits):
            state = unpack_lane(columns, lane)
            key = STATION_ZERO_KEYS[lane]
            records[key] = record_resolution(
                key,
                "CYCLE",
                moment,
                state,
                prefix_nonclean[lane],
                initial[lane],
                indices,
            )
        active &= ~(clean_hits | recurrence_hits)
        for lane in lane_mask_rows(active):
            prefix_nonclean[lane] += int(
                bool(current_nonclean & (1 << lane))
            )

        if moment == PAIR_RESOLUTION:
            for lane in pair_lanes:
                scalar_post[lane] = list(unpack_lane(columns, lane))
        elif PAIR_RESOLUTION < moment <= PAIR_STOP:
            for lane in pair_lanes:
                advance_scalar(
                    scalar_post[lane],
                    compiled[lanes[lane][0][1]],
                )
                packed_state = unpack_lane(columns, lane)
                scalar_state = bytes(scalar_post[lane])
                scalar_post_rows[lane].append({
                    "t": moment,
                    "offset": moment - PAIR_RESOLUTION,
                    "sha256": state_sha256(packed_state),
                    "weight": sum(packed_state),
                    "clean": is_clean(packed_state, indices),
                    "independent_scalar_replay_exact":
                        packed_state == scalar_state,
                })

    determinism["terminal_state_equal"] = (
        unpack_lane(columns, determinism["primary_lane"])
        == unpack_lane(columns, determinism["duplicate_lane"])
    )
    determinism["pass"] = (
        determinism["all_checkpoint_states_equal"]
        and determinism["terminal_state_equal"]
        and determinism["first_mismatch"] is None
    )
    return {
        "lanes": lanes,
        "initial_states": initial,
        "records": records,
        "captured": captured,
        "watch_stats": watch_stats,
        "scalar_post_rows": scalar_post_rows,
        "construction_rows": construction_rows,
        "schedule_gate_count": len(schedule),
        "one_step_exact": one_step_exact,
        "initial_all_nonclean":
            initial_nonclean & ((1 << len(lanes)) - 1)
            == (1 << len(lanes)) - 1,
        "unresolved_primary_keys": tuple(
            STATION_ZERO_KEYS[lane]
            for lane in lane_mask_rows(active)
        ),
        "determinism": determinism,
        "seconds": round(monotonic() - started, 6),
        "pass": (
            all(all(
                row[name] for name in (
                    "k_matches",
                    "rail_A_exact",
                    "rail_B_zero",
                    "composition_exact",
                )
            ) for row in construction_rows)
            and one_step_exact
            and initial_nonclean & ((1 << len(lanes)) - 1)
            == (1 << len(lanes)) - 1
            and not active
            and len(records) == len(STATION_ZERO_KEYS)
            and all(row["verification"]["pass"] for row in records.values())
            and determinism["pass"]
        ),
    }


def scan_null_spots(
    context: dict[str, object],
    indices: tuple[int, ...],
) -> dict[str, object]:
    lanes: tuple[Lane, ...] = tuple(
        (key, "primary") for key in NULL_KEYS
    )
    initial, words, _compiled, construction_rows = build_initial_family(
        NULL_KEYS, context
    )
    columns = pack_states(initial)
    schedule = compile_masked_schedule(context["program"], lanes)
    one_step = columns.copy()
    advance_packed(one_step, schedule)
    one_step_exact = all(
        unpack_lane(one_step, lane)
        == bytes(K.A.apply_semantic(
            initial[lane], words[key[1]]
        ))
        for lane, key in enumerate(NULL_KEYS)
    )
    active = (1 << len(NULL_KEYS)) - 1
    prefix_nonclean = [1] * len(NULL_KEYS)
    records: dict[Key, dict[str, object]] = {}
    started = monotonic()
    for moment in range(1, NULL_HORIZON + 1):
        advance_packed(columns, schedule)
        current_nonclean = nonclean_mask(columns, indices)
        clean_hits = active & ~current_nonclean
        recurrence_hits = equality_mask(
            columns, initial, active & ~clean_hits
        )
        for lane in lane_mask_rows(clean_hits):
            records[NULL_KEYS[lane]] = record_resolution(
                NULL_KEYS[lane],
                "TRANSIENT",
                moment,
                unpack_lane(columns, lane),
                prefix_nonclean[lane],
                initial[lane],
                indices,
            )
        for lane in lane_mask_rows(recurrence_hits):
            records[NULL_KEYS[lane]] = record_resolution(
                NULL_KEYS[lane],
                "CYCLE",
                moment,
                unpack_lane(columns, lane),
                prefix_nonclean[lane],
                initial[lane],
                indices,
            )
        active &= ~(clean_hits | recurrence_hits)
        for lane in lane_mask_rows(active):
            prefix_nonclean[lane] += int(
                bool(current_nonclean & (1 << lane))
            )
    final_nonclean = nonclean_mask(columns, indices)
    rows = tuple({
        "key": key,
        "open_through": NULL_HORIZON,
        "state_sha256": state_sha256(unpack_lane(columns, lane)),
        "terminal_nonclean":
            bool(final_nonclean & (1 << lane)),
        "all_T_plus_1_moments_nonclean":
            prefix_nonclean[lane] == NULL_HORIZON + 1,
        "no_return_to_t0": key not in records,
    } for lane, key in enumerate(NULL_KEYS))
    return {
        "keys": NULL_KEYS,
        "horizon": NULL_HORIZON,
        "resolution_rows": tuple(records.values()),
        "open_count": len(NULL_KEYS) - len(records),
        "rows": rows,
        "schedule_gate_count": len(schedule),
        "one_step_exact": one_step_exact,
        "seconds": round(monotonic() - started, 6),
        "pass": (
            all(all(
                row[name] for name in (
                    "k_matches",
                    "rail_A_exact",
                    "rail_B_zero",
                    "composition_exact",
                )
            ) for row in construction_rows)
            and one_step_exact
            and not records
            and all(
                row["terminal_nonclean"]
                and row["all_T_plus_1_moments_nonclean"]
                and row["no_return_to_t0"]
                for row in rows
            )
        ),
    }


def million_tick_pair_certificate(
    station: dict[str, object],
    indices: tuple[int, ...],
    named: dict[str, object],
) -> dict[str, object]:
    records = station["records"]
    captured = station["captured"]
    pair_rows = tuple(records.get(key) for key in PAIR_KEYS)
    spot_rows = {}
    for lane, key in enumerate(PAIR_KEYS):
        rows = []
        for moment in range(PAIR_RESOLUTION - 6, PAIR_RESOLUTION + 1):
            state = captured[lane][moment]
            rows.append({
                "t": moment,
                "offset": moment - PAIR_RESOLUTION,
                "sha256": state_sha256(state),
                "weight": sum(state),
                "clean": is_clean(state, indices),
            })
        spot_rows[key] = tuple(rows)
    moment_minus_5_states = tuple(
        captured[lane][PAIR_RESOLUTION - 5]
        for lane in range(len(PAIR_KEYS))
    )
    terminal_states = tuple(
        captured[lane][PAIR_RESOLUTION]
        for lane in range(len(PAIR_KEYS))
    )
    funnel_state = moment_minus_5_states[0]
    named_states = named["states"]
    gallery = tuple({
        "named_state": name,
        "named_weight": sum(state),
        "named_sha256": state_sha256(state),
        "funnel_vs_named": diff_summary(funnel_state, state),
        "exact_identity": funnel_state == state,
    } for name, state in named_states.items())
    funnel_visits = tuple(
        {
            **station["watch_stats"][(lane, name)],
            "exact_hits": tuple(
                station["watch_stats"][(lane, name)]["exact_hits"]
            ),
        }
        for lane in (0, 1)
        for name in ("funnel_weight_57", "funnel_weight_51")
    )
    post_rows = tuple({
        "key": key,
        "rows": tuple(station["scalar_post_rows"][lane]),
    } for lane, key in enumerate(PAIR_KEYS))
    both_exact = (
        all(row is not None for row in pair_rows)
        and all(
            row["outcome"] == "TRANSIENT"
            and row["resolution_moment"] == PAIR_RESOLUTION
            and row["first_clean_t"] == PAIR_RESOLUTION
            and row["verification"]["pass"]
            for row in pair_rows
        )
    )
    earlier_spot_exact = all(
        not row["clean"]
        for rows in spot_rows.values()
        for row in rows[:-1]
    ) and all(
        rows[-1]["clean"] for rows in spot_rows.values()
    )
    landed_veto_exact = all(
        not rows[-2]["clean"] for rows in spot_rows.values()
    )
    scalar_post_exact = all(
        len(row["rows"]) == 6
        and tuple(point["offset"] for point in row["rows"])
        == (1, 2, 3, 4, 5, 6)
        and all(
            point["independent_scalar_replay_exact"]
            for point in row["rows"]
        )
        for row in post_rows
    )
    no_57_51_visits = all(
        not row["exact_hits"] for row in funnel_visits
    )
    exact = (
        bool(station["pass"])
        and both_exact
        and earlier_spot_exact
        and landed_veto_exact
        and scalar_post_exact
        and moment_minus_5_states[0] == moment_minus_5_states[1]
        and terminal_states[0] == terminal_states[1]
        and no_57_51_visits
    )
    finding = (
        "PASS: both event-0 station-0 keys first land clean as "
        "TRANSIENT at t=1142432; their t-5 funnel states are identical, "
        "the landed t-1 veto and +1..+6 scalar replays are exact, and "
        "neither trajectory visits the named weight-57/51 states."
        if exact else
        "FAIL: the independent pair evolution refutes at least one "
        "Cycle-844 million-tick pair assertion; inspect the printed "
        "resolution, spot-window, synchronization, visit, and replay rows."
    )
    return {
        "status": "PASS" if exact else "FAIL",
        "finding": finding,
        "keys": PAIR_KEYS,
        "expected_resolution_moment": PAIR_RESOLUTION,
        "resolution_rows": pair_rows,
        "earlier_nonclean_spot_window": spot_rows,
        "landed_veto_at_t_minus_1": landed_veto_exact,
        "post_terminal_plus_1_through_plus_6": post_rows,
        "post_terminal_scalar_replay_exact": scalar_post_exact,
        "synchronization": {
            "tested_moment": PAIR_RESOLUTION - 5,
            "meaning": "resolution moment minus five",
            "moment_minus_5_state_identity":
                moment_minus_5_states[0] == moment_minus_5_states[1],
            "moment_minus_5_sha256":
                state_sha256(moment_minus_5_states[0]),
            "terminal_state_identity":
                terminal_states[0] == terminal_states[1],
            "terminal_sha256": state_sha256(terminal_states[0]),
        },
        "million_tick_funnel_state": {
            "definition": "the common pair state at resolution moment - 5",
            "moment": PAIR_RESOLUTION - 5,
            "weight": sum(funnel_state),
            "sha256": state_sha256(funnel_state),
            "component_weights": component_weights(funnel_state),
            "extended_family_gallery_diffs": gallery,
        },
        "named_57_51_visit_rows": funnel_visits,
        "no_named_57_51_state_visits": no_57_51_visits,
        "pass": exact,
    }


def s5_completeness_certificate(
    trees: dict[str, ast.Module],
    station: dict[str, object],
) -> dict[str, object]:
    cycle831 = trees[AUDIT_INPUT_PATHS[1]]
    cycle834 = trees[AUDIT_INPUT_PATHS[2]]
    cycle844 = trees[AUDIT_INPUT_PATHS[4]]
    backbone = literal_assignment(cycle834, "K2_BACKBONE")
    transient_cohorts = literal_assignment(
        cycle834, "K2_TRANSIENT_COHORTS"
    )
    cycle_cohort = literal_assignment(cycle834, "K2_CYCLE_COHORT")
    old_cycles = literal_assignment(cycle831, "EXPECTED_OLD_CYCLES")
    primary_pair_keys = literal_assignment(cycle844, "K2_EVENT0_KEYS")
    primary_identity = literal_assignment(cycle844, "K2_IDENTITY")
    if not (
        isinstance(backbone, tuple)
        and isinstance(transient_cohorts, tuple)
        and isinstance(cycle_cohort, dict)
        and isinstance(old_cycles, dict)
    ):
        raise AssertionError("landed s=5 AST record is not literal")

    landed_backbone_rows = []
    for cohort in transient_cohorts:
        for pair in backbone:
            landed_backbone_rows.append({
                "key": (2, pair, cohort["event"]),
                "outcome": "TRANSIENT",
                "resolution_moment": cohort["moment"],
                "source": "Cycle834 literal K2_TRANSIENT_COHORTS",
            })
    for pair in backbone:
        landed_backbone_rows.append({
            "key": (2, pair, cycle_cohort["event"]),
            "outcome": "CYCLE",
            "resolution_moment": cycle_cohort["period"],
            "source": "Cycle834 literal K2_CYCLE_COHORT",
        })
    station_rows = tuple(
        station["records"][key] for key in STATION_ZERO_KEYS
    )
    ledger_rows = tuple(landed_backbone_rows) + station_rows
    max_separation_pairs = tuple(sorted({
        tuple(sorted((station_index, (station_index + 5) % RING_STATIONS)))
        for station_index in range(RING_STATIONS)
    }))
    expected_keys = {
        (2, pair, event)
        for pair in max_separation_pairs
        for event in range(4)
    }
    observed_keys = {row["key"] for row in ledger_rows}
    outcomes = Counter(row["outcome"] for row in ledger_rows)
    station_cycle_anchors = {
        (2, pair, 3): old_cycles.get((3, pair))
        for pair in ((0, 5), (0, 6))
    }
    station_cycle_exact = all(
        station["records"][key]["outcome"] == "CYCLE"
        and station["records"][key]["minimal_state_period"] == period
        for key, period in station_cycle_anchors.items()
    )
    identity_key, identity_outcome, identity_moment = primary_identity
    normalized_identity_key = (
        identity_key[0], identity_key[1], identity_key[2]
    )
    identity_exact = (
        station["records"][normalized_identity_key]["outcome"]
        == identity_outcome
        and station["records"][normalized_identity_key][
            "resolution_moment"
        ] == identity_moment
    )
    literal_record_exact = (
        backbone
        == (
            (1, 6), (1, 7), (2, 7), (2, 8), (3, 8),
            (3, 9), (4, 9), (4, 10), (5, 10),
        )
        and transient_cohorts
        == (
            {"event": 0, "moment": 14744, "size": 9},
            {"event": 2, "moment": 33195, "size": 9},
            {"event": 1, "moment": 51115, "size": 9},
        )
        and cycle_cohort == {"event": 3, "period": 3, "size": 9}
        and primary_pair_keys == PAIR_KEYS
        and primary_identity
        == ((2, (0, 5), 1), "TRANSIENT", 193210)
        and station_cycle_anchors
        == {
            (2, (0, 5), 3): 2,
            (2, (0, 6), 3): 2,
        }
    )
    exact = (
        literal_record_exact
        and station["pass"]
        and len(landed_backbone_rows) == 36
        and len(station_rows) == 8
        and len(ledger_rows) == len(observed_keys) == 44
        and observed_keys == expected_keys
        and outcomes == {"TRANSIENT": 33, "CYCLE": 11}
        and station_cycle_exact
        and identity_exact
        and all(row["verification"]["pass"] for row in station_rows)
    )
    finding = (
        "PASS: the full s=5 ledger closes at 44/44 unique keys: "
        "33 TRANSIENT and 11 CYCLE."
        if exact else
        "FAIL: the independent set-union/count does not close the landed "
        "s=5 ledger at 44 keys with the claimed 33/11 split."
    )
    return {
        "status": "PASS" if exact else "FAIL",
        "finding": finding,
        "scope":
            "all eleven cyclic-separation-5 pairs times four prepared events",
        "count_method":
            "independent normalized-key set union; source size fields are "
            "checked but are not used as population totals",
        "landed_backbone_record": {
            "pairs": backbone,
            "transient_cohorts": transient_cohorts,
            "cycle_cohort": cycle_cohort,
            "row_count_by_direct_enumeration":
                len(landed_backbone_rows),
        },
        "independently_evolved_station_zero_rows": station_rows,
        "station_zero_cycle_source_anchors": station_cycle_anchors,
        "Cycle844_identity_anchor_exact": identity_exact,
        "literal_record_exact": literal_record_exact,
        "expected_key_count": len(expected_keys),
        "observed_row_count": len(ledger_rows),
        "observed_unique_key_count": len(observed_keys),
        "missing_keys": tuple(sorted(expected_keys - observed_keys)),
        "extra_keys": tuple(sorted(observed_keys - expected_keys)),
        "own_outcome_count": dict(sorted(outcomes.items())),
        "pass": exact,
    }


def b3_spot_certificate(
    station: dict[str, object],
) -> dict[str, object]:
    rows = tuple({
        **station["watch_stats"][(0, name)],
        "exact_hits": tuple(
            station["watch_stats"][(0, name)]["exact_hits"]
        ),
    } for name in ("S0_prime", "pulse_coincidence_state"))
    exact = all(
        row["moments_tested"] == PAIR_STOP + 1
        and not row["exact_hits"]
        for row in rows
    )
    finding = (
        "PASS: the deep (2,(0,5),event-0) lane has zero exact visits "
        "to both pinned B3 states through t=1142438, including t=0."
        if exact else
        "FAIL: the deep B3 spot scan found a pinned-state visit or lost "
        "trajectory-moment accounting."
    )
    return {
        "status": "PASS" if exact else "FAIL",
        "finding": finding,
        "deep_lane": PAIR_KEYS[0],
        "inclusive_horizon": PAIR_STOP,
        "target_rows": rows,
        "full_state_policy":
            "a fixed exact-coordinate necessary window gates a full "
            "5815-bit equality comparison; every window survivor is tested",
        "pass": exact,
    }


def controls_certificate(
    source: dict[str, object],
    indices: tuple[int, ...],
    context: dict[str, object],
    named: dict[str, object],
    station: dict[str, object],
    elapsed: float,
) -> dict[str, object]:
    source_public = {
        key: value for key, value in source.items() if key != "trees"
    }
    blocked_loaded = tuple(
        name for name in BLOCKLISTED_MODULES if name in sys.modules
    )
    exact = (
        source["pass"]
        and len(indices) == len(set(indices)) == 477
        and min(indices) >= 0
        and max(indices) < STATE_BITS
        and context["pass"]
        and named["pass"]
        and station["determinism"]["pass"]
        and not blocked_loaded
        and not FIREWALL.hits
        and elapsed < AUDIT_TIMEOUT_SEC
    )
    return {
        **source_public,
        "status": "PASS" if exact else "FAIL",
        "finding": (
            "PASS: SHA/blob pins, text/AST-only BLOCKLIST, literal existing "
            "worktree-relative inputs, declared-slice determinism, runtime, "
            "and stdout controls all close."
            if exact else
            "FAIL: at least one SHA/blob, BLOCKLIST, input-path, basis, "
            "determinism, runtime, or stdout precondition failed."
        ),
        "cleanliness_basis": {
            "coordinate_count": len(indices),
            "unique_coordinate_count": len(set(indices)),
            "state_width": STATE_BITS,
            "bounds_exact": min(indices) >= 0 and max(indices) < STATE_BITS,
        },
        "context_pass": context["pass"],
        "named_state_reconstruction_rows": named["rows"],
        "named_state_reconstruction_pass": named["pass"],
        "determinism": station["determinism"],
        "blocked_modules_loaded_at_end": blocked_loaded,
        "firewall_hits_at_end": tuple(FIREWALL.hits),
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "pass": exact,
    }


def null_spots_certificate(scan: dict[str, object]) -> dict[str, object]:
    exact = bool(scan["pass"])
    finding = (
        "PASS: both trio spot keys remain open with exact per-moment "
        "cleanliness and return accounting through T=524288."
        if exact else
        "FAIL: at least one trio spot key resolved, returned, became clean, "
        "or lost accounting by T=524288."
    )
    return {
        **scan,
        "status": "PASS" if exact else "FAIL",
        "finding": finding,
        "pass": exact,
    }


def render(
    certificates: tuple[tuple[str, dict[str, object]], ...],
    summary: dict[str, object],
) -> str:
    lines = [
        f"CERTIFICATE {name} {certificate['status']} "
        f"{compact(certificate)}"
        for name, certificate in certificates
    ]
    lines.append("SUMMARY_JSON " + compact(summary))
    lines.append(str(summary["terminal"]))
    return "\n".join(lines) + "\n"


def stable_render(
    certificates: tuple[tuple[str, dict[str, object]], ...],
    summary: dict[str, object],
) -> str:
    controls = dict(certificates)["CONTROLS"]
    for _attempt in range(20):
        summary["certificate_statuses"] = {
            name: certificate["status"]
            for name, certificate in certificates
        }
        summary["pass"] = all(
            certificate["pass"] for _name, certificate in certificates
        )
        summary["terminal"] = (
            "CYCLE844_BETS_INDEPENDENT_CHECK_PASS"
            if summary["pass"]
            else "CYCLE844_BETS_INDEPENDENT_CHECK_HONEST_FAIL"
        )
        output = render(certificates, summary)
        size = len(output.encode("utf-8"))
        if (
            controls["stdout_bytes"] == size
            and summary["stdout_bytes"] == size
        ):
            return output
        controls["stdout_bytes"] = size
        summary["stdout_bytes"] = size
    raise AssertionError("stdout byte fixed point did not converge")


def run() -> int:
    started = monotonic()
    source = source_controls()
    trees = source["trees"]
    indices = residual_indices()
    context = build_context()
    named = reconstruct_named_states(context)
    station = scan_station_zero_family(
        context, indices, named
    )
    null_scan = scan_null_spots(context, indices)

    pair = million_tick_pair_certificate(station, indices, named)
    completeness = s5_completeness_certificate(trees, station)
    nulls = null_spots_certificate(null_scan)
    b3 = b3_spot_certificate(station)
    elapsed = monotonic() - started
    controls = controls_certificate(
        source, indices, context, named, station, elapsed
    )
    certificates = (
        ("THE_MILLION_TICK_PAIR", pair),
        ("THE_s5_COMPLETENESS", completeness),
        ("NULL_SPOTS", nulls),
        ("B3_SPOT", b3),
        ("CONTROLS", controls),
    )
    summary = {
        "cycle": 844,
        "checker": "independent_adversarial",
        "primary_refuted": not all(
            certificate["pass"]
            for name, certificate in certificates
            if name != "CONTROLS"
        ),
        "pair_resolution_moment": tuple(
            station["records"][key]["resolution_moment"]
            for key in PAIR_KEYS
        ),
        "s5_outcome_count": completeness["own_outcome_count"],
        "null_open_count": nulls["open_count"],
        "B3_exact_hit_count": sum(
            len(row["exact_hits"]) for row in b3["target_rows"]
        ),
        "station_scan_seconds": station["seconds"],
        "null_scan_seconds": null_scan["seconds"],
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "certificate_statuses": {},
        "pass": False,
        "terminal": "CYCLE844_BETS_INDEPENDENT_CHECK_HONEST_FAIL",
    }
    output = stable_render(certificates, summary)
    stdout_ok = len(output.encode("utf-8")) < STDOUT_LIMIT_BYTES
    controls["pass"] = controls["pass"] and stdout_ok
    controls["status"] = "PASS" if controls["pass"] else "FAIL"
    if not stdout_ok:
        controls["finding"] = (
            "FAIL: stdout is not below the declared 150000-byte limit."
        )
    output = stable_render(certificates, summary)
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        sys.stdout.write(compact({
            "pass": False,
            "failure": "stdout limit exceeded",
            "stdout_bytes": len(output.encode("utf-8")),
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
            "terminal": "CYCLE844_BETS_INDEPENDENT_CHECK_HONEST_FAIL",
        }) + "\n")
        return 1
    sys.stdout.write(output)
    return 0 if summary["pass"] else 1


def main() -> int:
    try:
        return run()
    except Exception as error:
        sys.stdout.write(compact({
            "pass": False,
            "exception_type": type(error).__name__,
            "exception": str(error),
            "terminal": "CYCLE844_BETS_INDEPENDENT_CHECK_HONEST_FAIL",
        }) + "\n")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
