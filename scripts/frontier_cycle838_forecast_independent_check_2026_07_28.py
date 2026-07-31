#!/usr/bin/env python3
"""Cycle 838 independent adversarial checker: station 0 and the deep null.

The Cycle-831/834/838 science primaries are SHA-pinned text/AST inputs only.
Only the landed Cycle-719 controller core is executable.  Evolution,
bit-slicing, terminal detection, state comparisons, and accounting below are
implemented independently in this checker.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle831_deep_k2_forecast_tests_2026_07_28.py",
    "scripts/frontier_cycle834_k3_backbone_2026_07_28.py",
    "scripts/frontier_cycle838_k3_trio_forecast_2026_07_28.py",
)

import ast
from hashlib import sha1, sha256
import importlib.abc
import json
from pathlib import Path
import sys
from time import monotonic


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
        "ea668b4d0be960622cd10d4e16b3cd1056d343db80ee6845407ca6ddb3e604c0",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    AUDIT_INPUT_PATHS[1]: "ef24edda08118c4e14439b899790fff6c6f94175",
    AUDIT_INPUT_PATHS[2]: "89d4506c6df9738bf0458027ab76cc9d2f9710ab",
    AUDIT_INPUT_PATHS[3]: "2f89c8eb911375bed58b1126e9f5f7b860ead20a",
}
REQUIRED_AST_FUNCTIONS = {
    AUDIT_INPUT_PATHS[0]: {
        "interleaved_program", "mapped_macro", "run_orbit",
    },
    AUDIT_INPUT_PATHS[1]: {"build_family", "boundary_snapshot"},
    AUDIT_INPUT_PATHS[2]: {
        "forecast_surface", "cycle_cohort_probe",
    },
    AUDIT_INPUT_PATHS[3]: {
        "make_engine", "evolve", "optional_k2_certificate",
    },
}


class _PrimaryFirewall(importlib.abc.MetaPathFinder):
    """Fail closed if an AST-only science primary is imported."""

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


RING_STATIONS = 11
FIXTURE_BANKS = 2
STATE_BITS = 5815
WATCHED_COORDINATE_COUNT = 477
LANDED_HORIZON = 65536
TARGET_HORIZON = 262144

Key = tuple[int, tuple[int, ...], int]
State = bytes
MaskedGate = tuple[int, int, int, int, int]

EXPECTED_K3_OPEN: tuple[Key, ...] = (
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
EXPECTED_TRIO_KEYS: tuple[Key, ...] = tuple(
    key for key in EXPECTED_K3_OPEN if key[1][1] == 2
)
EXPECTED_NONTRIO_KEYS: tuple[Key, ...] = tuple(
    key for key in EXPECTED_K3_OPEN if key not in EXPECTED_TRIO_KEYS
)
TRIO_SPOT_KEYS: tuple[Key, ...] = (
    (3, (0, 2, 6), 2),
    (3, (0, 2, 8), 3),
)
NONTRIO_SPOT_KEYS: tuple[Key, ...] = (
    (3, (0, 3, 6), 2),
    (3, (0, 3, 7), 3),
)
STATION0_S5_KEYS: tuple[Key, ...] = tuple(
    (2, pair, event)
    for event in range(4)
    for pair in ((0, 5), (0, 6))
)
STATION0_S5_OLD_OPEN: tuple[Key, ...] = (
    (2, (0, 5), 0),
    (2, (0, 5), 1),
    (2, (0, 5), 2),
    (2, (0, 6), 0),
    (2, (0, 6), 1),
    (2, (0, 6), 2),
)
EXPECTED_NEW_TRANSIENTS: dict[Key, int] = {
    (2, (0, 5), 1): 193210,
    (2, (0, 6), 1): 193210,
    (2, (0, 5), 2): 246669,
    (2, (0, 6), 2): 246669,
}
EXPECTED_STATION0_EVENT3_PERIOD = 2
REFERENCE_LABEL_BY_EVENT = {0: "S*", 2: "S2", 1: "S1"}
REFERENCE_MOMENT_BY_EVENT = {0: 14744, 2: 33195, 1: 51115}
REFERENCE_POSITIONS = ((1, 6), (5, 10))
DETERMINISM_KEYS: tuple[Key, ...] = (
    (2, (0, 5), 1),
    (3, (0, 2, 6), 2),
)
DETERMINISM_TIMES = (
    0, LANDED_HORIZON, 193210, 246669, TARGET_HORIZON,
)


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def state_sha256(state: State) -> str:
    return sha256(state).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(
        f"blob {len(payload)}\0".encode("ascii") + payload
    ).hexdigest()


def literal_assignment(tree: ast.Module, name: str) -> object | None:
    values = []
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


def top_level_functions(tree: ast.Module) -> set[str]:
    return {
        node.name
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }


def source_controls() -> tuple[dict[str, object], dict[str, ast.Module]]:
    payloads = {
        path: (ROOT / path).read_bytes()
        for path in AUDIT_INPUT_PATHS
        if (ROOT / path).is_file()
    }
    trees = {
        path: ast.parse(payload, filename=path)
        for path, payload in payloads.items()
    }
    self_tree = ast.parse(
        Path(__file__).read_bytes(), filename=Path(__file__).name
    )
    rows = tuple({
        "path": path,
        "exists": (ROOT / path).is_file(),
        "worktree_relative": not Path(path).is_absolute(),
        "sha256": sha256(payloads[path]).hexdigest()
            if path in payloads else None,
        "expected_sha256": EXPECTED_SHA256[path],
        "sha256_exact": (
            path in payloads
            and sha256(payloads[path]).hexdigest()
            == EXPECTED_SHA256[path]
        ),
        "git_blob": git_blob(payloads[path]) if path in payloads else None,
        "expected_git_blob": EXPECTED_GIT_BLOBS[path],
        "git_blob_exact": (
            path in payloads
            and git_blob(payloads[path]) == EXPECTED_GIT_BLOBS[path]
        ),
        "required_AST_functions":
            tuple(sorted(REQUIRED_AST_FUNCTIONS[path])),
        "required_AST_functions_present": (
            path in trees
            and REQUIRED_AST_FUNCTIONS[path] <= top_level_functions(trees[path])
        ),
        "access": (
            "EXECUTABLE_LANDED_CORE"
            if path == CORE_PATH else "TEXT_AST_ONLY_BLOCKLISTED"
        ),
    } for path in AUDIT_INPUT_PATHS)
    direct_frontier_imports = tuple(sorted(
        alias.name
        for node in self_tree.body
        if isinstance(node, ast.Import)
        for alias in node.names
        if alias.name.startswith("frontier_cycle")
    ))
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_INPUT_PATHS_literal":
            literal_assignment(self_tree, "AUDIT_INPUT_PATHS")
            == AUDIT_INPUT_PATHS,
        "named_file_count": len(AUDIT_INPUT_PATHS),
        "read_cap": 6,
        "all_paths_existing_worktree_relative": (
            len(payloads) == len(AUDIT_INPUT_PATHS)
            and all(
                row["exists"] and row["worktree_relative"] for row in rows
            )
        ),
        "source_rows": rows,
        "text_AST_only_paths": TEXT_AST_ONLY_PATHS,
        "blocked_modules": BLOCKLISTED_MODULES,
        "blocked_modules_loaded": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits": tuple(FIREWALL.hits),
        "direct_frontier_imports": direct_frontier_imports,
    }
    result["pass"] = (
        result["AUDIT_INPUT_PATHS_literal"]
        and result["named_file_count"] <= result["read_cap"]
        and result["all_paths_existing_worktree_relative"]
        and all(
            row["sha256_exact"]
            and row["git_blob_exact"]
            and row["required_AST_functions_present"]
            for row in rows
        )
        and direct_frontier_imports
        == (
            "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26",
        )
        and not result["blocked_modules_loaded"]
        and not result["firewall_hits"]
    )
    return result, trees


def watched_rows() -> tuple[tuple[str, int], ...]:
    named = (
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
            for name, wire in named
        )
    for link_index, base in enumerate(
        K.M.R12.LINK_BASES[:FIXTURE_BANKS - 1]
    ):
        rows.extend(
            (f"link{link_index}.WIRE_{wire}", int(base + wire))
            for wire in range(K.B.LINK_WIDTH)
        )
    return tuple(rows)


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


def cleanliness_basis(
    rows: tuple[tuple[str, int], ...],
) -> dict[str, object]:
    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    state = bytes(K.M.pack_state(banks, links))
    indices = tuple(wire for _name, wire in rows)
    result = {
        "state_bits": len(state),
        "watched_coordinate_count": len(indices),
        "unique_coordinate_count": len(set(indices)),
        "all_indices_in_bounds":
            min(indices) >= 0 and max(indices) < len(state),
        "zero_state_clean": direct_clean(bytes(len(state))),
        "basis_sha256": digest(rows),
    }
    result["pass"] = (
        result["state_bits"] == STATE_BITS
        and result["watched_coordinate_count"]
        == WATCHED_COORDINATE_COUNT
        and result["unique_coordinate_count"]
        == WATCHED_COORDINATE_COUNT
        and result["all_indices_in_bounds"]
        and result["zero_state_clean"]
    )
    return result


def build_context() -> dict[str, object]:
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
    result = {
        "program": program,
        "fixtures": tuple(fixtures),
        "program_stations": len(program),
        "events": tuple(row[0] for row in fixtures),
        "allocator_gate_count": len(allocator),
    }
    result["pass"] = (
        result["program_stations"] == RING_STATIONS
        and result["events"] == (0, 1, 2, 3)
        and result["allocator_gate_count"] == 3106
    )
    return result


def synchronous_word(
    program: tuple[object, ...],
    positions0: tuple[int, ...],
) -> tuple[object, ...]:
    positions = tuple(positions0)
    word = []
    for _step in range(len(program)):
        live = set(positions)
        for station, row in enumerate(program):
            if station in live:
                word.extend(K.mapped_macro(row))
        positions = tuple(
            (position + 1) % len(program) for position in positions
        )
    return tuple(word)


def bit_slice(states: tuple[tuple[int, ...], ...]) -> list[int]:
    return [
        sum(int(state[wire]) << lane for lane, state in enumerate(states))
        for wire in range(len(states[0]))
    ]


def un_slice(columns: list[int] | tuple[int, ...], lane: int) -> State:
    return bytes((column >> lane) & 1 for column in columns)


def masked_schedule(
    program: tuple[object, ...],
    lanes: tuple[tuple[Key, str], ...],
) -> tuple[MaskedGate, ...]:
    schedule: list[MaskedGate] = []
    for step in range(len(program)):
        live_by_lane = tuple(
            {
                (position + step) % len(program)
                for position in key[1]
            }
            for key, _role in lanes
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
                wires = tuple(int(wire) for wire in gate.wires)
                if len(wires) != len(set(wires)):
                    raise AssertionError(("repeated gate wire", gate))
                if gate.kind == "X" and len(wires) == 1:
                    schedule.append((0, wires[0], 0, 0, mask))
                elif gate.kind == "CNOT" and len(wires) == 2:
                    schedule.append((1, wires[0], wires[1], 0, mask))
                elif gate.kind == "TOF" and len(wires) == 3:
                    schedule.append(
                        (2, wires[0], wires[1], wires[2], mask)
                    )
                else:
                    raise AssertionError(("unsupported landed gate", gate))
    return tuple(schedule)


def advance(columns: list[int], schedule: tuple[MaskedGate, ...]) -> None:
    for kind, first, second, third, mask in schedule:
        if kind == 0:
            columns[first] ^= mask
        elif kind == 1:
            columns[second] ^= columns[first] & mask
        else:
            columns[third] ^= columns[first] & columns[second] & mask


def nonclean_mask(
    columns: list[int] | tuple[int, ...],
    rows: tuple[tuple[str, int], ...],
) -> int:
    result = 0
    for _name, wire in rows:
        result |= columns[wire]
    return result


def equality_to_initial_mask(
    columns: list[int],
    initial_columns: tuple[int, ...],
    candidates: int,
) -> int:
    result = candidates
    for current, initial in zip(columns, initial_columns):
        result &= candidates ^ ((current ^ initial) & candidates)
        if not result:
            return 0
    return result


def lane_numbers(mask: int) -> tuple[int, ...]:
    result = []
    while mask:
        bit = mask & -mask
        result.append(bit.bit_length() - 1)
        mask ^= bit
    return tuple(result)


def state_row(
    state: State,
    watched: tuple[tuple[str, int], ...],
) -> dict[str, object]:
    support = tuple(name for name, wire in watched if state[wire])
    return {
        "state_sha256": state_sha256(state),
        "full_state_hamming_weight": sum(state),
        "landed_residual_weight": len(support),
        "landed_residual_support": support,
        "direct_clean": direct_clean(state),
    }


def make_engine(
    name: str,
    keys: tuple[Key, ...],
    context: dict[str, object],
    watched: tuple[tuple[str, int], ...],
    duplicate_keys: tuple[Key, ...] = (),
) -> dict[str, object]:
    program = context["program"]
    fixtures = context["fixtures"]
    fixture_by_event = {
        event: before for event, _direction, before in fixtures
    }
    positions = tuple(sorted({key[1] for key in keys}))
    words = {
        position: synchronous_word(program, position)
        for position in positions
    }
    lanes = (
        tuple((key, "primary") for key in keys)
        + tuple((key, "determinism_duplicate") for key in duplicate_keys)
    )
    initial_states = []
    construction_rows = []
    for key, role in lanes:
        _k, positions0, event = key
        before = fixture_by_event[event]
        initial, rail_a, rail_b, _trace = K.run_orbit(
            before, program, token_positions=positions0
        )
        semantic = K.A.apply_semantic(before, words[positions0])
        expected_rail = tuple(
            int(station in positions0)
            for station in range(RING_STATIONS)
        )
        state = tuple(int(bit) for bit in initial)
        initial_states.append(state)
        construction_rows.append({
            "key": key,
            "role": role,
            "k_matches_positions": key[0] == len(positions0),
            "run_orbit_equals_landed_semantic": initial == semantic,
            "rail_A_exact": rail_a == expected_rail,
            "rail_B_zero": not any(rail_b),
            "initial_nonclean": not direct_clean(state),
        })
    initial_tuple = tuple(initial_states)
    columns = bit_slice(initial_tuple)
    initial_columns = tuple(columns)
    schedule = masked_schedule(program, lanes)
    one_step = columns.copy()
    advance(one_step, schedule)
    one_step_rows = tuple({
        "key": key,
        "role": role,
        "own_bit_slice_equals_landed_scalar_semantic":
            un_slice(one_step, lane)
            == bytes(K.A.apply_semantic(
                initial_tuple[lane], words[key[1]]
            )),
    } for lane, (key, role) in enumerate(lanes))
    primary_index = {key: lane for lane, key in enumerate(keys)}
    duplicate_index = {
        key: len(keys) + offset
        for offset, key in enumerate(duplicate_keys)
    }
    initial_nonclean = nonclean_mask(columns, watched)
    engine = {
        "name": name,
        "keys": keys,
        "lanes": lanes,
        "words": words,
        "columns": columns,
        "initial_columns": initial_columns,
        "initial_states": initial_tuple,
        "schedule": schedule,
        "primary_index": primary_index,
        "duplicate_index": duplicate_index,
        "active_mask": (1 << len(keys)) - 1,
        "first_clean": {key: None for key in keys},
        "first_return": {key: None for key in keys},
        "terminal_states": {},
        "terminal_outcomes": {},
        "nonclean_prefix_counts": [
            int(bool(initial_nonclean & (1 << lane)))
            for lane in range(len(keys))
        ],
        "inequality_prefix_counts": [0 for _key in keys],
        "snapshots": {0: tuple(bytes(row) for row in initial_tuple)},
        "determinism_rows": [],
        "construction_rows": tuple(construction_rows),
        "one_step_rows": one_step_rows,
        "last_t": 0,
    }
    duplicate_initial_exact = all(
        initial_tuple[primary_index[key]]
        == initial_tuple[duplicate_index[key]]
        for key in duplicate_keys
    )
    duplicate_masks_exact = all(
        ((mask >> primary_index[key]) & 1)
        == ((mask >> duplicate_index[key]) & 1)
        for _kind, _first, _second, _third, mask in schedule
        for key in duplicate_keys
    )
    engine["duplicate_initial_exact"] = duplicate_initial_exact
    engine["duplicate_masks_exact"] = duplicate_masks_exact
    engine["construction_pass"] = (
        bool(schedule)
        and len(columns) == STATE_BITS
        and all(
            row["k_matches_positions"]
            and row["run_orbit_equals_landed_semantic"]
            and row["rail_A_exact"]
            and row["rail_B_zero"]
            and row["initial_nonclean"]
            for row in construction_rows
        )
        and all(
            row["own_bit_slice_equals_landed_scalar_semantic"]
            for row in one_step_rows
        )
        and duplicate_initial_exact
        and duplicate_masks_exact
    )
    return engine


def snapshot(
    engine: dict[str, object],
    moment: int,
) -> tuple[State, ...]:
    states = tuple(
        un_slice(engine["columns"], lane)
        for lane in range(len(engine["lanes"]))
    )
    engine["snapshots"][moment] = states
    rows = []
    for key, duplicate_lane in engine["duplicate_index"].items():
        primary_lane = engine["primary_index"][key]
        rows.append({
            "moment": moment,
            "key": key,
            "primary_sha256": state_sha256(states[primary_lane]),
            "duplicate_sha256": state_sha256(states[duplicate_lane]),
            "exact_state_equal":
                states[primary_lane] == states[duplicate_lane],
        })
    if rows and moment in DETERMINISM_TIMES:
        engine["determinism_rows"].extend(rows)
    return states


def scan_engine(
    engine: dict[str, object],
    horizon: int,
    watched: tuple[tuple[str, int], ...],
    capture_times: tuple[int, ...],
) -> dict[str, object]:
    if engine["last_t"] != 0:
        raise AssertionError("scan_engine is a one-shot independent scan")
    capture = set(capture_times)
    capture.add(0)
    started = monotonic()
    snapshot(engine, 0)
    physical_updates = 0
    logical_active_updates = 0
    for moment in range(1, horizon + 1):
        active_before = int(engine["active_mask"])
        logical_active_updates += active_before.bit_count()
        advance(engine["columns"], engine["schedule"])
        physical_updates += 1
        current_nonclean = nonclean_mask(engine["columns"], watched)
        clean_hits = active_before & ~current_nonclean
        recurrence_hits = equality_to_initial_mask(
            engine["columns"],
            engine["initial_columns"],
            active_before & ~clean_hits,
        )
        for lane in lane_numbers(clean_hits):
            key = engine["keys"][lane]
            engine["first_clean"][key] = moment
            engine["terminal_outcomes"][key] = "TRANSIENT"
            engine["terminal_states"][key] = un_slice(
                engine["columns"], lane
            )
        for lane in lane_numbers(recurrence_hits):
            key = engine["keys"][lane]
            engine["first_return"][key] = moment
            engine["terminal_outcomes"][key] = "CYCLE"
            engine["terminal_states"][key] = un_slice(
                engine["columns"], lane
            )
        engine["active_mask"] = (
            active_before & ~(clean_hits | recurrence_hits)
        )
        for lane in lane_numbers(int(engine["active_mask"])):
            engine["nonclean_prefix_counts"][lane] += int(
                bool(current_nonclean & (1 << lane))
            )
            engine["inequality_prefix_counts"][lane] += 1
        if moment in capture:
            snapshot(engine, moment)
    engine["last_t"] = horizon
    return {
        "horizon": horizon,
        "primary_key_count": len(engine["keys"]),
        "physical_global_updates": physical_updates,
        "expected_physical_global_updates": horizon,
        "physical_update_accounting_exact": physical_updates == horizon,
        "logical_active_updates": logical_active_updates,
        "resolved_count": len(engine["terminal_outcomes"]),
        "open_count": int(engine["active_mask"]).bit_count(),
        "population_accounting_exact":
            len(engine["keys"])
            == len(engine["terminal_outcomes"])
            + int(engine["active_mask"]).bit_count(),
        "seconds": round(monotonic() - started, 6),
    }


def lane_state(
    engine: dict[str, object],
    moment: int,
    key: Key,
) -> State:
    return engine["snapshots"][moment][engine["primary_index"][key]]


def terminal_row(
    engine: dict[str, object],
    key: Key,
    watched: tuple[tuple[str, int], ...],
) -> dict[str, object]:
    lane = engine["primary_index"][key]
    outcome = engine["terminal_outcomes"].get(key)
    moment = (
        engine["first_clean"].get(key)
        if outcome == "TRANSIENT"
        else engine["first_return"].get(key)
        if outcome == "CYCLE"
        else None
    )
    row = {
        "key": key,
        "outcome": outcome or "OPEN_AT_HORIZON",
        "resolution_moment": moment,
        "first_clean": engine["first_clean"].get(key),
        "first_return_to_t0": engine["first_return"].get(key),
        "nonclean_prefix_count":
            engine["nonclean_prefix_counts"][lane],
        "initial_inequality_prefix_count":
            engine["inequality_prefix_counts"][lane],
    }
    if outcome:
        row["terminal_state"] = state_row(
            engine["terminal_states"][key], watched
        )
    else:
        final = lane_state(engine, engine["last_t"], key)
        row["horizon_state"] = state_row(final, watched)
        row["horizon_state_equals_t0"] = (
            final == bytes(engine["initial_states"][lane])
        )
    return row


def catalog_certificate(
    trees: dict[str, ast.Module],
) -> dict[str, object]:
    cycle834 = trees[AUDIT_INPUT_PATHS[2]]
    cycle838 = trees[AUDIT_INPUT_PATHS[3]]
    landed = literal_assignment(
        cycle834, "LANDED_K3_OPEN_THROUGH_65536"
    )
    primary_catalog = literal_assignment(
        cycle838, "K3_OPEN_THROUGH_T65536"
    )
    primary_station0 = literal_assignment(
        cycle838, "K2_STATION0_S5_OPEN_THROUGH_T65536"
    )
    backbone = literal_assignment(cycle834, "K2_BACKBONE")
    cohorts = literal_assignment(
        cycle834, "K2_TRANSIENT_COHORTS"
    )
    cycle_cohort = literal_assignment(
        cycle834, "K2_CYCLE_COHORT"
    )
    expected_cohorts = (
        {"event": 0, "moment": 14744, "size": 9},
        {"event": 2, "moment": 33195, "size": 9},
        {"event": 1, "moment": 51115, "size": 9},
    )
    trio = tuple(
        key for key in landed
        if key[1] in ((0, 2, 6), (0, 2, 7), (0, 2, 8))
    ) if isinstance(landed, tuple) else ()
    nontrio = tuple(
        key for key in landed if key not in trio
    ) if isinstance(landed, tuple) else ()
    result = {
        "Cycle834_literal_open_inventory": landed,
        "Cycle834_literal_open_count":
            len(landed) if isinstance(landed, tuple) else None,
        "supplied_context_count": 33,
        "supplied_context_count_matches_literal": False,
        "Cycle838_literal_catalog": primary_catalog,
        "catalogs_exact": (
            landed == primary_catalog == EXPECTED_K3_OPEN
        ),
        "six_trio_keys": trio,
        "six_trio_keys_exact": trio == EXPECTED_TRIO_KEYS,
        "four_nontrio_keys": nontrio,
        "four_nontrio_keys_exact": nontrio == EXPECTED_NONTRIO_KEYS,
        "station0_s5_old_open_literal": primary_station0,
        "station0_s5_old_open_exact":
            primary_station0 == STATION0_S5_OLD_OPEN,
        "landed_k2_backbone": backbone,
        "landed_k2_backbone_exact":
            isinstance(backbone, tuple)
            and len(backbone) == 9
            and backbone[0] == (1, 6)
            and backbone[-1] == (5, 10),
        "landed_reference_cohorts": cohorts,
        "landed_reference_cohorts_exact": cohorts == expected_cohorts,
        "landed_origin_free_backbone_cycle_cohort": cycle_cohort,
        "landed_origin_free_backbone_cycle_cohort_exact":
            cycle_cohort == {"event": 3, "period": 3, "size": 9},
        "finding": (
            "Cycle 834 literally records 10 open k=3 keys, not 33: "
            "six registered-trio keys and four non-trio keys."
        ),
    }
    result["pass"] = (
        result["Cycle834_literal_open_count"] == 10
        and result["catalogs_exact"]
        and result["six_trio_keys_exact"]
        and result["four_nontrio_keys_exact"]
        and result["station0_s5_old_open_exact"]
        and result["landed_k2_backbone_exact"]
        and result["landed_reference_cohorts_exact"]
        and result["landed_origin_free_backbone_cycle_cohort_exact"]
    )
    return result


def reference_funnel_certificate(
    engine: dict[str, object],
    watched: tuple[tuple[str, int], ...],
) -> dict[str, object]:
    rows = []
    states: dict[str, State] = {}
    for event in (0, 2, 1):
        label = REFERENCE_LABEL_BY_EVENT[event]
        moment = REFERENCE_MOMENT_BY_EVENT[event]
        keys = tuple(
            (2, positions, event) for positions in REFERENCE_POSITIONS
        )
        lag_states = tuple(
            lane_state(engine, moment - 5, key) for key in keys
        )
        terminal_states = tuple(
            engine["terminal_states"].get(key) for key in keys
        )
        states[label] = lag_states[0]
        rows.append({
            "label": label,
            "event": event,
            "witness_keys": keys,
            "expected_first_clean": moment,
            "observed_first_clean": tuple(
                engine["first_clean"].get(key) for key in keys
            ),
            "no_prior_return": all(
                engine["first_return"].get(key) is None for key in keys
            ),
            "moment_minus_5": moment - 5,
            "witness_states_exactly_equal":
                lag_states[0] == lag_states[1],
            "terminal_states_exactly_equal":
                terminal_states[0] == terminal_states[1],
            "state": state_row(lag_states[0], watched),
        })
    result = {
        "definition": (
            "S*, S2, and S1 are independently reconstructed as the exact "
            "full states five moments before the landed event-0, event-2, "
            "and event-1 backbone cohort transients."
        ),
        "rows": tuple(rows),
        "states": states,
    }
    result["pass"] = all(
        row["observed_first_clean"]
        == (row["expected_first_clean"],) * 2
        and row["no_prior_return"]
        and row["witness_states_exactly_equal"]
        and row["terminal_states_exactly_equal"]
        for row in rows
    )
    return result


def four_transients_certificate(
    engine: dict[str, object],
    references: dict[str, object],
    watched: tuple[tuple[str, int], ...],
) -> dict[str, object]:
    rows = []
    for key, expected in EXPECTED_NEW_TRANSIENTS.items():
        lane = engine["primary_index"][key]
        minus5 = lane_state(engine, expected - 5, key)
        terminal = engine["terminal_states"].get(key)
        rows.append({
            "key": key,
            "expected_first_clean": expected,
            "observed_first_clean": engine["first_clean"].get(key),
            "first_return_to_t0": engine["first_return"].get(key),
            "all_t0_through_t_minus_1_nonclean":
                engine["nonclean_prefix_counts"][lane] == expected,
            "all_t1_through_t_minus_1_not_t0":
                engine["inequality_prefix_counts"][lane]
                == expected - 1,
            "moment_minus_5_t": expected - 5,
            "moment_minus_5_state": state_row(minus5, watched),
            "terminal_state": (
                state_row(terminal, watched)
                if isinstance(terminal, bytes) else None
            ),
            "terminal_direct_clean":
                isinstance(terminal, bytes) and direct_clean(terminal),
        })
    event_rows = []
    new_funnels: dict[int, State] = {}
    for event in (1, 2):
        moment = next(
            value
            for key, value in EXPECTED_NEW_TRANSIENTS.items()
            if key[2] == event
        )
        keys = tuple(
            key for key in EXPECTED_NEW_TRANSIENTS if key[2] == event
        )
        minus5_states = tuple(
            lane_state(engine, moment - 5, key) for key in keys
        )
        terminal_states = tuple(
            engine["terminal_states"].get(key) for key in keys
        )
        new_funnels[event] = minus5_states[0]
        event_rows.append({
            "event": event,
            "keys": keys,
            "resolution_moment": moment,
            "same_resolution_moment": all(
                engine["first_clean"].get(key) == moment for key in keys
            ),
            "same_moment_minus_5_full_state":
                minus5_states[0] == minus5_states[1],
            "same_terminal_full_state":
                terminal_states[0] == terminal_states[1],
            "funnel_state": state_row(minus5_states[0], watched),
        })
    reference_states = references["states"]
    named_states = {
        "new_event1": new_funnels[1],
        "new_event2": new_funnels[2],
        **reference_states,
    }
    comparisons = tuple({
        "left": left_name,
        "right": right_name,
        "exact_full_state_different": left != right,
    } for left_index, (left_name, left) in enumerate(named_states.items())
      for right_name, right in tuple(named_states.items())[left_index + 1:])
    result = {
        "method": (
            "Own masked bit-slice evolution; landed scalar semantics checked "
            "for one step; cleanliness and exact return tested online at "
            "every integer moment."
        ),
        "rows": tuple(rows),
        "within_event_pairs": tuple(event_rows),
        "reference_funnels": tuple(
            {
                "label": label,
                "state": state_row(state, watched),
            }
            for label, state in reference_states.items()
        ),
        "five_state_pairwise_comparisons": comparisons,
        "five_funnel_states_all_distinct":
            len(set(named_states.values())) == 5,
        "finding": (
            "Four new station-0 s=5 transients are verified: the event-1 "
            "pair first cleans at t=193210 and the event-2 pair at "
            "t=246669.  Each pair has one exact moment-minus-5 full state; "
            "the two new funnel states differ from each other and from "
            "S*/S2/S1."
        ),
    }
    result["pass"] = (
        references["pass"]
        and all(
            row["observed_first_clean"] == row["expected_first_clean"]
            and row["first_return_to_t0"] is None
            and row["all_t0_through_t_minus_1_nonclean"]
            and row["all_t1_through_t_minus_1_not_t0"]
            and row["terminal_direct_clean"]
            for row in rows
        )
        and all(
            row["same_resolution_moment"]
            and row["same_moment_minus_5_full_state"]
            and row["same_terminal_full_state"]
            for row in event_rows
        )
        and result["five_funnel_states_all_distinct"]
        and all(
            row["exact_full_state_different"] for row in comparisons
        )
    )
    return result


def open_key_certificate(
    catalog: dict[str, object],
    engine: dict[str, object],
    watched: tuple[tuple[str, int], ...],
) -> dict[str, object]:
    rows = tuple(
        terminal_row(engine, key, watched) for key in TRIO_SPOT_KEYS
    )
    result = {
        "catalog_literal_count": catalog["Cycle834_literal_open_count"],
        "registered_trio_key_count": len(EXPECTED_TRIO_KEYS),
        "registered_trio_keys": EXPECTED_TRIO_KEYS,
        "claimed_complete_horizon": TARGET_HORIZON,
        "independent_spot_resweep_keys": TRIO_SPOT_KEYS,
        "independent_spot_resweep_rows": rows,
        "spot_design":
            "one event-2 and one event-3 trio key, at distinct geometries",
        "finding": (
            "The disclosed catalog correction is exact: 10 Cycle-834 open "
            "keys, including six trio keys.  Independent event-2/event-3 "
            "spot resweeps remain nonclean and nonrecurrent through complete "
            "T=262144."
        ),
    }
    result["pass"] = (
        catalog["pass"]
        and result["registered_trio_key_count"] == 6
        and all(
            row["outcome"] == "OPEN_AT_HORIZON"
            and row["nonclean_prefix_count"] == TARGET_HORIZON + 1
            and row["initial_inequality_prefix_count"]
            == TARGET_HORIZON
            and row["horizon_state"]["direct_clean"] is False
            and not row["horizon_state_equals_t0"]
            for row in rows
        )
    )
    return result


def null_certificate(
    engine: dict[str, object],
    watched: tuple[tuple[str, int], ...],
) -> dict[str, object]:
    rows = tuple(
        terminal_row(engine, key, watched) for key in NONTRIO_SPOT_KEYS
    )
    result = {
        "nontrio_catalog": EXPECTED_NONTRIO_KEYS,
        "nontrio_catalog_count": len(EXPECTED_NONTRIO_KEYS),
        "independent_spot_resweep_keys": NONTRIO_SPOT_KEYS,
        "independent_spot_resweep_rows": rows,
        "null_scope": (
            "Two declared non-trio spot keys have no cleanliness or exact "
            "t0-return terminal at any integer t through 262144."
        ),
        "finding": (
            "The deep non-trio null survives its declared two-key adversarial "
            "spot resweep: both sampled keys are open through complete "
            "T=262144."
        ),
    }
    result["pass"] = (
        result["nontrio_catalog_count"] == 4
        and all(
            row["outcome"] == "OPEN_AT_HORIZON"
            and row["nonclean_prefix_count"] == TARGET_HORIZON + 1
            and row["initial_inequality_prefix_count"]
            == TARGET_HORIZON
            and row["horizon_state"]["direct_clean"] is False
            and not row["horizon_state_equals_t0"]
            for row in rows
        )
    )
    return result


def biconditional_update_certificate(
    engine: dict[str, object],
    watched: tuple[tuple[str, int], ...],
) -> dict[str, object]:
    rows = tuple(
        terminal_row(engine, key, watched) for key in STATION0_S5_KEYS
    )
    row_by_key = {row["key"]: row for row in rows}
    event_rows = []
    for event in range(4):
        keys = tuple(
            key for key in STATION0_S5_KEYS if key[2] == event
        )
        event_rows.append({
            "event": event,
            "keys": keys,
            "statuses": tuple(
                row_by_key[key]["outcome"] for key in keys
            ),
            "moments": tuple(
                row_by_key[key]["resolution_moment"] for key in keys
            ),
        })
    new_keys = tuple(
        sorted(
            (
                key for key in STATION0_S5_OLD_OPEN
                if row_by_key[key]["outcome"] == "TRANSIENT"
                and row_by_key[key]["resolution_moment"] > LANDED_HORIZON
            ),
            key=lambda key: (key[2], key[1]),
        )
    )
    expected_new = tuple(sorted(
        EXPECTED_NEW_TRANSIENTS,
        key=lambda key: (key[2], key[1]),
    ))
    event0_open = all(
        row_by_key[key]["outcome"] == "OPEN_AT_HORIZON"
        and row_by_key[key]["nonclean_prefix_count"]
        == TARGET_HORIZON + 1
        and row_by_key[key]["initial_inequality_prefix_count"]
        == TARGET_HORIZON
        for key in STATION0_S5_KEYS if key[2] == 0
    )
    event3_period2 = all(
        row_by_key[key]["outcome"] == "CYCLE"
        and row_by_key[key]["resolution_moment"]
        == EXPECTED_STATION0_EVENT3_PERIOD
        and row_by_key[key]["first_clean"] is None
        and row_by_key[key]["nonclean_prefix_count"]
        == EXPECTED_STATION0_EVENT3_PERIOD
        and row_by_key[key]["initial_inequality_prefix_count"]
        == EXPECTED_STATION0_EVENT3_PERIOD - 1
        for key in STATION0_S5_KEYS if key[2] == 3
    )
    result = {
        "station0_s5_fiber_rows": rows,
        "per_event_status": tuple(event_rows),
        "new_post_65536_transient_keys": new_keys,
        "expected_new_transient_keys": expected_new,
        "new_keys_precisely_event1_and_event2_pairs":
            new_keys == expected_new,
        "remaining_old_open_keys": tuple(
            key for key in STATION0_S5_OLD_OPEN
            if row_by_key[key]["outcome"] == "OPEN_AT_HORIZON"
        ),
        "remaining_old_open_are_exactly_event0_pair": (
            event0_open
            and tuple(
                key for key in STATION0_S5_OLD_OPEN
                if row_by_key[key]["outcome"] == "OPEN_AT_HORIZON"
            )
            == (
                (2, (0, 5), 0),
                (2, (0, 6), 0),
            )
        ),
        "station0_event3_pair_is_minimal_period2": event3_period2,
        "station0_s5_events_1_2_3_all_resolved": all(
            row_by_key[key]["outcome"] != "OPEN_AT_HORIZON"
            for key in STATION0_S5_KEYS if key[2] in (1, 2, 3)
        ),
        "station0_s5_complete_four_event_fibers_at_T262144": (),
        "Cycle837_historical_T65536_biconditional":
            "SURVIVES_AS_THE_LANDED_FINITE_HORIZON_STATEMENT",
        "Cycle837_global_T262144_biconditional":
            "NOT_REESTABLISHED_WITHOUT_A_COMPLETE_NON_S5_RESWEEP",
        "sharp_surviving_update": (
            "Within the two station-0 s=5 fibers, events 1, 2, and 3 are "
            "resolved at T=262144, but event 0 remains open; event 3 has "
            "minimal period 2 rather than the origin-free backbone's period "
            "3.  Origin absence therefore is not a no-resolution law; on "
            "the checked extension it marks delay and continued failure of "
            "complete-fiber closure."
        ),
        "finding": (
            "Cycle 837 survives exactly as its landed T=65536 finite-horizon "
            "biconditional, not as a newly exhaustive T=262144 theorem.  The "
            "station-0 s=5 update is: event-1 resolves at 193210, event-2 at "
            "246669, event-3 has minimal period 2, and only event-0 remains "
            "open.  "
            "Thus the checked s=5 surface supports an origin-delays reading; "
            "a global deep biconditional still requires a complete non-s=5 "
            "resweep."
        ),
    }
    result["pass"] = (
        result["new_keys_precisely_event1_and_event2_pairs"]
        and result["remaining_old_open_are_exactly_event0_pair"]
        and result["station0_event3_pair_is_minimal_period2"]
        and result["station0_s5_events_1_2_3_all_resolved"]
        and not result[
            "station0_s5_complete_four_event_fibers_at_T262144"
        ]
    )
    return result


def render(
    checks: dict[str, bool],
    certificates: dict[str, object],
    report: dict[str, object],
) -> str:
    lines = [
        f"{'PASS' if passed else 'FAIL'} {name}"
        for name, passed in checks.items()
    ]
    for name, certificate in certificates.items():
        if "finding" in certificate:
            lines.append(f"FINDING {name} {certificate['finding']}")
        lines.append(f"CERTIFICATE {name} {compact(certificate)}")
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
            "CYCLE838_FORECAST_INDEPENDENT_CHECK_PASS"
            if report["pass"]
            else "CYCLE838_FORECAST_INDEPENDENT_CHECK_HONEST_FAIL"
        )
        output = render(checks, certificates, report)
        size = len(output.encode("utf-8"))
        controls = certificates["E_CONTROLS"]
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
    sources, trees = source_controls()
    watched = watched_rows()
    basis = cleanliness_basis(watched)
    context = build_context()
    catalog = catalog_certificate(trees)

    reference_keys = tuple(
        (2, positions, event)
        for event in (0, 2, 1)
        for positions in REFERENCE_POSITIONS
    )
    reference_engine = make_engine(
        "reference_funnels",
        reference_keys,
        context,
        watched,
    )
    reference_capture = tuple(sorted({
        moment - 5
        for moment in REFERENCE_MOMENT_BY_EVENT.values()
    }))
    reference_phase = scan_engine(
        reference_engine,
        max(REFERENCE_MOMENT_BY_EVENT.values()),
        watched,
        reference_capture,
    )
    references = reference_funnel_certificate(
        reference_engine, watched
    )

    candidate_keys = (
        STATION0_S5_KEYS + TRIO_SPOT_KEYS + NONTRIO_SPOT_KEYS
    )
    candidate_engine = make_engine(
        "station0_and_k3_spots",
        candidate_keys,
        context,
        watched,
        DETERMINISM_KEYS,
    )
    candidate_capture = tuple(sorted({
        LANDED_HORIZON,
        TARGET_HORIZON,
        *DETERMINISM_TIMES,
        *(moment - 5 for moment in EXPECTED_NEW_TRANSIENTS.values()),
        *EXPECTED_NEW_TRANSIENTS.values(),
    }))
    candidate_phase = scan_engine(
        candidate_engine,
        TARGET_HORIZON,
        watched,
        candidate_capture,
    )

    four = four_transients_certificate(
        candidate_engine, references, watched
    )
    opened = open_key_certificate(catalog, candidate_engine, watched)
    null = null_certificate(candidate_engine, watched)
    update = biconditional_update_certificate(
        candidate_engine, watched
    )
    baseline_rows = tuple({
        "key": key,
        "first_terminal_after_landed_horizon_or_none": (
            candidate_engine["first_clean"].get(key)
            or candidate_engine["first_return"].get(key)
        ),
        "state_at_T65536_direct_nonclean":
            not direct_clean(lane_state(
                candidate_engine, LANDED_HORIZON, key
            )),
        "state_at_T65536_not_t0": (
            lane_state(candidate_engine, LANDED_HORIZON, key)
            != bytes(candidate_engine["initial_states"][
                candidate_engine["primary_index"][key]
            ])
        ),
    } for key in STATION0_S5_OLD_OPEN)
    baseline_exact = all(
        (
            row["first_terminal_after_landed_horizon_or_none"] is None
            or row["first_terminal_after_landed_horizon_or_none"]
            > LANDED_HORIZON
        )
        and row["state_at_T65536_direct_nonclean"]
        and row["state_at_T65536_not_t0"]
        for row in baseline_rows
    )
    update["T65536_station0_old_open_recheck"] = baseline_rows
    update["T65536_station0_old_open_recheck_exact"] = baseline_exact
    update["pass"] = bool(update["pass"] and baseline_exact)

    determinism_rows = tuple(candidate_engine["determinism_rows"])
    deterministic = (
        candidate_engine["duplicate_initial_exact"]
        and candidate_engine["duplicate_masks_exact"]
        and len(determinism_rows)
        == len(DETERMINISM_KEYS) * len(DETERMINISM_TIMES)
        and all(row["exact_state_equal"] for row in determinism_rows)
    )
    elapsed = monotonic() - started
    blocklist_clean_at_end = (
        not any(
            name in sys.modules for name in BLOCKLISTED_MODULES
        )
        and not FIREWALL.hits
    )
    controls_base = (
        sources["pass"]
        and basis["pass"]
        and context["pass"]
        and catalog["pass"]
        and reference_engine["construction_pass"]
        and candidate_engine["construction_pass"]
        and reference_phase["physical_update_accounting_exact"]
        and reference_phase["population_accounting_exact"]
        and candidate_phase["physical_update_accounting_exact"]
        and candidate_phase["population_accounting_exact"]
        and deterministic
        and blocklist_clean_at_end
        and elapsed < AUDIT_TIMEOUT_SEC
    )
    controls = {
        **sources,
        "cleanliness_basis": basis,
        "context": {
            key: value for key, value in context.items()
            if key not in {"program", "fixtures"}
        },
        "dependency_policy": (
            "Cycle-719 is the sole executable science dependency; "
            "Cycles 831/834/838 are SHA-pinned text/AST-only and blocklisted."
        ),
        "independent_evolution": {
            "implementation":
                "checker-local masked bit-slice compiler and updater",
            "landed_scalar_one_step_crosscheck":
                "all lanes exactly equal K.A.apply_semantic for one step",
            "reference_engine_construction_pass":
                reference_engine["construction_pass"],
            "candidate_engine_construction_pass":
                candidate_engine["construction_pass"],
            "reference_phase": reference_phase,
            "candidate_phase": candidate_phase,
            "candidate_schedule_instructions_per_tick":
                len(candidate_engine["schedule"]),
        },
        "determinism_scope": {
            "declaration": (
                "Two declared keys are carried as distinct duplicate lanes "
                "from t=0 through T=262144 and compared at five boundaries."
            ),
            "keys": DETERMINISM_KEYS,
            "times": DETERMINISM_TIMES,
            "duplicate_initial_exact":
                candidate_engine["duplicate_initial_exact"],
            "duplicate_schedule_masks_exact":
                candidate_engine["duplicate_masks_exact"],
            "rows": determinism_rows,
            "deterministic": deterministic,
        },
        "exact_arithmetic": (
            "All state updates, cleanliness tests, recurrence tests, counts, "
            "full-state identities, Hamming weights, and hashes are exact; "
            "only monotonic runtime is floating point."
        ),
        "blocked_modules_loaded_at_end": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits_at_end": tuple(FIREWALL.hits),
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "finding": (
            "SHA, AST-only blocklist, literal input-path, exact one-step "
            "crosscheck, declared-slice determinism, runtime, and stdout "
            "controls are enforced."
        ),
    }
    checks = {
        "A_THE_FOUR_TRANSIENTS": bool(four["pass"]),
        "B_THE_OPEN_KEY_CATALOG": bool(opened["pass"]),
        "C_THE_NULL": bool(null["pass"]),
        "D_THE_BICONDITIONAL_UPDATE": bool(update["pass"]),
        "E_CONTROLS": controls_base,
    }
    certificates = {
        "A_THE_FOUR_TRANSIENTS": four,
        "B_THE_OPEN_KEY_CATALOG": opened,
        "C_THE_NULL": null,
        "D_THE_BICONDITIONAL_UPDATE": update,
        "E_CONTROLS": controls,
    }
    report = {
        "cycle": 838,
        "checker": "independent_adversarial",
        "catalog_open_k3_count": catalog["Cycle834_literal_open_count"],
        "trio_claimed_open_count": len(EXPECTED_TRIO_KEYS),
        "trio_independent_spot_count": len(TRIO_SPOT_KEYS),
        "nontrio_independent_spot_count": len(NONTRIO_SPOT_KEYS),
        "new_station0_s5_transient_count":
            len(update["new_post_65536_transient_keys"]),
        "remaining_station0_s5_old_open_count":
            len(update["remaining_old_open_keys"]),
        "deep_global_biconditional_status":
            update["Cycle837_global_T262144_biconditional"],
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "checks": {},
        "pass": False,
        "terminal":
            "CYCLE838_FORECAST_INDEPENDENT_CHECK_HONEST_FAIL",
    }
    output = stable_render(checks, certificates, report)
    stdout_ok = len(output.encode("utf-8")) < STDOUT_LIMIT_BYTES
    checks["E_CONTROLS"] = controls_base and stdout_ok
    controls["pass"] = checks["E_CONTROLS"]
    output = stable_render(checks, certificates, report)
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        sys.stdout.write(compact({
            "pass": False,
            "failure": "stdout limit exceeded",
            "stdout_bytes": len(output.encode("utf-8")),
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
            "terminal":
                "CYCLE838_FORECAST_INDEPENDENT_CHECK_HONEST_FAIL",
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
            "terminal":
                "CYCLE838_FORECAST_INDEPENDENT_CHECK_HONEST_FAIL",
        }) + "\n")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
