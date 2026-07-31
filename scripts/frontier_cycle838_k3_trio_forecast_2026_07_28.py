#!/usr/bin/env python3
"""Cycle 838: deep k=3 continuation and the registered trio forecast.

The sole executable science dependency is the landed Cycle-719 controller
core.  Cycles 831 and 834 are SHA-pinned text/AST-only source primaries and
are blocked from import.

Cycle 834 literally lands ten open canonical k=3 representative/event keys,
six of which are the two registered event trios.  It does not literally land
a 33-key open catalog.  This runner exposes that supplied-count mismatch and
never invents 23 keys.  The complete sweep is over all ten literal landed
open keys.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
EXECUTION_BUDGET_SEC = 1425
STDOUT_LIMIT_BYTES = 200 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle831_deep_k2_forecast_tests_2026_07_28.py",
    "scripts/frontier_cycle834_k3_backbone_2026_07_28.py",
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
BLOCKLISTED_MODULES = tuple(
    Path(path).stem for path in TEXT_AST_ONLY_PATHS
)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "624dad4d841e10e24891810dbc500cc4d6ebe871d6f09dd96f89e3189e52e2ff",
    AUDIT_INPUT_PATHS[2]:
        "8ed75c4e6f19fa5e8a9492225aae681ab85017dcfac00f8ab109b7c587aeddaa",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    AUDIT_INPUT_PATHS[1]: "ef24edda08118c4e14439b899790fff6c6f94175",
    AUDIT_INPUT_PATHS[2]: "89d4506c6df9738bf0458027ab76cc9d2f9710ab",
}
EXPECTED_BRANCH = "physics-loop/toe-close-blockC24-20260729"
EXPECTED_BASE = "575254ee97d73f3db6cc11b90bd7333033d38494"


class _PrimaryFirewall(importlib.abc.MetaPathFinder):
    """Fail closed if a source-only primary is imported."""

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
TARGET_CHOICES = (262144, 131072, 65536)
PILOT_TICKS = 256
SAFETY_FACTOR = 1.40
RESERVE_SECONDS = 60.0
SUPPLIED_K3_FAMILY_COUNT = 33
DETERMINISM_KEYS = 2

Key = tuple[int, tuple[int, ...], int]
State = bytes
MaskedGate = tuple[int, int, int, int, int]

K3_OPEN_THROUGH_T65536: tuple[Key, ...] = (
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
TRIO_KEYS: tuple[Key, ...] = tuple(
    key for key in K3_OPEN_THROUGH_T65536
    if key[1] in ((0, 2, 6), (0, 2, 7), (0, 2, 8))
)
NONTRIO_KEYS: tuple[Key, ...] = tuple(
    key for key in K3_OPEN_THROUGH_T65536 if key not in TRIO_KEYS
)
K2_STATION0_S5_OPEN_THROUGH_T65536: tuple[Key, ...] = (
    (2, (0, 5), 0),
    (2, (0, 5), 1),
    (2, (0, 5), 2),
    (2, (0, 6), 0),
    (2, (0, 6), 1),
    (2, (0, 6), 2),
)
IDENTITY_TRANSIENT: tuple[Key, int] = (
    (3, (0, 2, 5), 2),
    444,
)
IDENTITY_CYCLE: tuple[Key, int] = (
    (3, (0, 2, 6), 1),
    5952,
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
    self_tree = ast.parse(
        Path(__file__).read_bytes(), filename=Path(__file__).name
    )
    actual_sha = {
        path: sha256(payload).hexdigest()
        for path, payload in payloads.items()
    }
    actual_blobs = {
        path: git_blob(payload) for path, payload in payloads.items()
    }
    markers = {
        AUDIT_INPUT_PATHS[0]:
            {"interleaved_program", "mapped_macro", "run_orbit"},
        AUDIT_INPUT_PATHS[1]:
            {"build_family", "boundary_snapshot"},
        AUDIT_INPUT_PATHS[2]:
            {"forecast_surface", "cycle_cohort_probe"},
    }
    landed_k3 = literal_assignment(
        trees[AUDIT_INPUT_PATHS[2]],
        "LANDED_K3_OPEN_THROUGH_65536",
    )
    landed_trios = literal_assignment(
        trees[AUDIT_INPUT_PATHS[2]], "LANDED_K3_TRANSIENTS"
    )
    landed_cycles = literal_assignment(
        trees[AUDIT_INPUT_PATHS[2]], "LANDED_K3_CYCLES"
    )
    direct_frontier_imports = tuple(sorted(
        alias.name
        for node in self_tree.body
        if isinstance(node, ast.Import)
        for alias in node.names
        if alias.name.startswith("frontier_cycle")
    ))
    branch = git_value("branch", "--show-current")
    base = git_value(
        "merge-base", "HEAD", "physics-loop/toe-close-blockC23-20260729"
    )
    rows = tuple({
        "path": path,
        "exists": (ROOT / path).is_file(),
        "worktree_relative": not Path(path).is_absolute(),
        "sha256": actual_sha.get(path),
        "expected_sha256": EXPECTED_SHA256[path],
        "sha256_exact": actual_sha.get(path) == EXPECTED_SHA256[path],
        "git_blob": actual_blobs.get(path),
        "expected_git_blob": EXPECTED_GIT_BLOBS[path],
        "git_blob_exact":
            actual_blobs.get(path) == EXPECTED_GIT_BLOBS[path],
        "access": (
            "EXECUTABLE_LANDED_CORE"
            if path == CORE_PATH else "TEXT_AST_ONLY_BLOCKLISTED"
        ),
    } for path in AUDIT_INPUT_PATHS)
    provenance = {
        "Cycle834_literal_open_keys": landed_k3,
        "Cycle834_literal_open_count":
            len(landed_k3) if isinstance(landed_k3, tuple) else None,
        "runner_open_keys": K3_OPEN_THROUGH_T65536,
        "literal_catalog_exact":
            landed_k3 == K3_OPEN_THROUGH_T65536,
        "supplied_family_count": SUPPLIED_K3_FAMILY_COUNT,
        "supplied_33_matches_literal_open_count":
            isinstance(landed_k3, tuple)
            and len(landed_k3) == SUPPLIED_K3_FAMILY_COUNT,
        "disposition":
            "COUNT_MISMATCH_EXPOSED_NO_KEYS_INVENTED",
        "identity_transient_landed":
            IDENTITY_TRANSIENT in landed_trios
            if isinstance(landed_trios, tuple) else False,
        "identity_cycle_landed":
            IDENTITY_CYCLE in landed_cycles
            if isinstance(landed_cycles, tuple) else False,
    }
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_INPUT_PATHS_literal":
            literal_assignment(self_tree, "AUDIT_INPUT_PATHS")
            == AUDIT_INPUT_PATHS,
        "named_input_count": len(AUDIT_INPUT_PATHS),
        "maximum_named_inputs": 7,
        "all_paths_existing_worktree_relative": (
            len(payloads) == len(AUDIT_INPUT_PATHS)
            and all(
                row["exists"] and row["worktree_relative"]
                for row in rows
            )
        ),
        "source_rows": rows,
        "AST_markers_present": all(
            markers[path] <= top_level_functions(trees[path])
            for path in AUDIT_INPUT_PATHS
        ),
        "text_AST_only_paths": TEXT_AST_ONLY_PATHS,
        "blocked_modules": BLOCKLISTED_MODULES,
        "blocked_modules_loaded": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits": tuple(FIREWALL.hits),
        "direct_frontier_imports": direct_frontier_imports,
        "provenance": provenance,
        "git_branch": branch,
        "expected_git_branch": EXPECTED_BRANCH,
        "git_branch_exact": branch == EXPECTED_BRANCH,
        "git_base": base,
        "expected_git_base": EXPECTED_BASE,
        "git_base_exact": base == EXPECTED_BASE,
    }
    result["pass"] = (
        result["AUDIT_INPUT_PATHS_literal"]
        and result["named_input_count"] <= result["maximum_named_inputs"]
        and result["all_paths_existing_worktree_relative"]
        and all(row["sha256_exact"] and row["git_blob_exact"] for row in rows)
        and result["AST_markers_present"]
        and direct_frontier_imports
        == (
            "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26",
        )
        and provenance["literal_catalog_exact"]
        and provenance["identity_transient_landed"]
        and provenance["identity_cycle_landed"]
        and not result["blocked_modules_loaded"]
        and not result["firewall_hits"]
        and result["git_branch_exact"]
        and result["git_base_exact"]
    )
    return result


def clean_postimage(state: State | tuple[int, ...]) -> bool:
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


def watched_residual_rows() -> tuple[tuple[str, int], ...]:
    bank_named = (
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
            for name, wire in bank_named
        )
    for link_index, base in enumerate(
        K.M.R12.LINK_BASES[:FIXTURE_BANKS - 1]
    ):
        rows.extend(
            (f"link{link_index}.WIRE_{wire}", int(base + wire))
            for wire in range(K.B.LINK_WIDTH)
        )
    return tuple(rows)


def basis_certificate(
    residual_rows: tuple[tuple[str, int], ...],
) -> dict[str, object]:
    indices = tuple(wire for _name, wire in residual_rows)
    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    zero = bytes(K.M.pack_state(banks, links))
    result = {
        "state_width": len(zero),
        "watched_coordinate_count": len(indices),
        "unique_coordinate_count": len(set(indices)),
        "coordinate_bounds_exact":
            min(indices) >= 0 and max(indices) < len(zero),
        "zero_state_clean": clean_postimage(bytes(len(zero))),
        "basis_sha256": digest(residual_rows),
        "definition":
            "source pointer; both banks' POINTER/U_TO_V/V_TO_U/"
            "DIRECTION_OK/FRESH/ZERO_WORK/TOKEN_OK; every link bit",
    }
    result["pass"] = (
        result["state_width"] == STATE_BITS
        and result["watched_coordinate_count"] == WATCHED_COORDINATE_COUNT
        and result["unique_coordinate_count"] == WATCHED_COORDINATE_COUNT
        and result["coordinate_bounds_exact"]
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
        "events": tuple(event for event, _direction, _before in fixtures),
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
    positions = positions0
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


def compile_word(
    word: tuple[object, ...],
) -> tuple[tuple[int, int, int, int], ...]:
    rows = []
    for gate in word:
        wires = tuple(int(wire) for wire in gate.wires)
        if len(set(wires)) != len(wires):
            raise AssertionError(("repeated gate wire", gate))
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
    compiled: tuple[tuple[int, int, int, int], ...],
) -> None:
    for kind, first, second, third in compiled:
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


def un_slice(columns: list[int] | tuple[int, ...], lane: int) -> State:
    return bytes((column >> lane) & 1 for column in columns)


def lane_numbers(mask: int) -> tuple[int, ...]:
    rows = []
    while mask:
        bit = mask & -mask
        rows.append(bit.bit_length() - 1)
        mask ^= bit
    return tuple(rows)


def masked_schedule(
    program: tuple[object, ...],
    lanes: tuple[tuple[Key, str], ...],
) -> tuple[MaskedGate, ...]:
    rows: list[MaskedGate] = []
    for step in range(len(program)):
        for station, program_row in enumerate(program):
            lane_mask = sum(
                1 << lane
                for lane, (key, _role) in enumerate(lanes)
                if station in {
                    (position + step) % len(program)
                    for position in key[1]
                }
            )
            if not lane_mask:
                continue
            for gate in K.mapped_macro(program_row):
                wires = tuple(int(wire) for wire in gate.wires)
                if len(set(wires)) != len(wires):
                    raise AssertionError(("repeated landed gate wire", gate))
                if gate.kind == "X":
                    rows.append((0, wires[0], 0, 0, lane_mask))
                elif gate.kind == "CNOT":
                    rows.append(
                        (1, wires[0], wires[1], 0, lane_mask)
                    )
                elif gate.kind == "TOF":
                    rows.append(
                        (2, wires[0], wires[1], wires[2], lane_mask)
                    )
                else:
                    raise AssertionError(("unsupported landed gate", gate))
    return tuple(rows)


def advance(
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


def nonclean_mask(
    columns: list[int] | tuple[int, ...],
    residual_rows: tuple[tuple[str, int], ...],
) -> int:
    mask = 0
    for _name, wire in residual_rows:
        mask |= columns[wire]
    return mask


def equality_to_initial_mask(
    columns: list[int],
    initial_columns: tuple[int, ...],
    candidates: int,
) -> int:
    matches = candidates
    for current, initial in zip(columns, initial_columns):
        matches &= candidates ^ ((current ^ initial) & candidates)
        if not matches:
            return 0
    return matches


def support_at_lane(
    columns: list[int],
    lane: int,
    residual_rows: tuple[tuple[str, int], ...],
) -> tuple[str, ...]:
    return tuple(
        name for name, wire in residual_rows
        if (columns[wire] >> lane) & 1
    )


def make_engine(
    name: str,
    keys: tuple[Key, ...],
    context: dict[str, object],
    residual_rows: tuple[tuple[str, int], ...],
    duplicate_keys: tuple[Key, ...] = (),
) -> dict[str, object]:
    program = context["program"]
    fixtures = context["fixtures"]
    fixture_by_event = {
        event: (direction, before)
        for event, direction, before in fixtures
    }
    positions = tuple(sorted({key[1] for key in keys}))
    words = {
        row: synchronous_word(program, row) for row in positions
    }
    compiled_words = {
        row: compile_word(words[row]) for row in positions
    }
    lanes = (
        tuple((key, "primary") for key in keys)
        + tuple((key, "determinism_duplicate") for key in duplicate_keys)
    )
    initial_states = []
    initial_rows = []
    for key, role in lanes:
        k, token_positions, event = key
        direction, before = fixture_by_event[event]
        initial, rail_a, rail_b, _trace = K.run_orbit(
            before, program, token_positions=token_positions
        )
        expected_rail = tuple(
            int(station in token_positions)
            for station in range(RING_STATIONS)
        )
        semantic = K.A.apply_semantic(before, words[token_positions])
        initial_state = tuple(int(bit) for bit in initial)
        initial_states.append(initial_state)
        initial_rows.append({
            "key": key,
            "role": role,
            "k_matches_positions": k == len(token_positions),
            "composition_exact": initial == semantic,
            "rail_A_exact": rail_a == expected_rail,
            "rail_B_zero": not any(rail_b),
            "initial_nonclean": not clean_postimage(initial_state),
            "initial_sha256": state_sha256(bytes(initial_state)),
        })
    initial_states_tuple = tuple(initial_states)
    columns = bit_slice(initial_states_tuple)
    initial_columns = tuple(columns)
    schedule = masked_schedule(program, lanes)
    one_step = columns.copy()
    advance(one_step, schedule)
    one_step_rows = tuple({
        "lane": lane,
        "key": key,
        "role": role,
        "exact":
            un_slice(one_step, lane)
            == bytes(K.A.apply_semantic(
                initial_states_tuple[lane], words[key[1]]
            )),
    } for lane, (key, role) in enumerate(lanes))
    primary_index = {key: lane for lane, key in enumerate(keys)}
    duplicate_index = {
        key: len(keys) + offset
        for offset, key in enumerate(duplicate_keys)
    }
    duplicate_initial_exact = all(
        initial_states_tuple[primary_index[key]]
        == initial_states_tuple[duplicate_index[key]]
        for key in duplicate_keys
    )
    duplicate_masks_exact = all(
        ((mask >> primary_index[key]) & 1)
        == ((mask >> duplicate_index[key]) & 1)
        for _kind, _first, _second, _third, mask in schedule
        for key in duplicate_keys
    )
    active_mask = (1 << len(keys)) - 1
    initial_nonclean = nonclean_mask(columns, residual_rows)
    engine = {
        "name": name,
        "keys": keys,
        "lanes": lanes,
        "words": words,
        "compiled_words": compiled_words,
        "columns": columns,
        "initial_columns": initial_columns,
        "initial_states": initial_states_tuple,
        "schedule": schedule,
        "primary_index": primary_index,
        "duplicate_index": duplicate_index,
        "active_mask": active_mask,
        "previous_nonclean": initial_nonclean,
        "nonclean_prefix_counts": [
            int(bool(initial_nonclean & (1 << lane)))
            for lane in range(len(keys))
        ],
        "initial_inequality_counts": [0] * len(keys),
        "transition_counts": [0] * len(keys),
        "records": {},
        "resolution_states": {},
        "minus5_states": {},
        "last_t": 0,
        "checkpoint_interval": 1024,
        "checkpoints": {
            0: tuple(
                bytes(state) for state in initial_states_tuple[:len(keys)]
            )
        },
        "initial_rows": tuple(initial_rows),
        "one_step_rows": one_step_rows,
        "duplicate_initial_exact": duplicate_initial_exact,
        "duplicate_masks_exact": duplicate_masks_exact,
        "construction_pass": (
            bool(schedule)
            and len(columns) == STATE_BITS
            and all(
                row["k_matches_positions"]
                and row["composition_exact"]
                and row["rail_A_exact"]
                and row["rail_B_zero"]
                and row["initial_nonclean"]
                for row in initial_rows
            )
            and all(row["exact"] for row in one_step_rows)
            and active_mask & ~initial_nonclean == 0
            and duplicate_initial_exact
            and duplicate_masks_exact
        ),
    }
    return engine


def recover_state(
    engine: dict[str, object],
    lane: int,
    target_t: int,
) -> State:
    interval = int(engine["checkpoint_interval"])
    checkpoint_t = target_t // interval * interval
    checkpoint = engine["checkpoints"][checkpoint_t][lane]
    state = [int(bit) for bit in checkpoint]
    key = engine["keys"][lane]
    compiled = engine["compiled_words"][key[1]]
    for _moment in range(checkpoint_t, target_t):
        advance_scalar(state, compiled)
    return bytes(state)


def record_resolution(
    engine: dict[str, object],
    lane: int,
    outcome: str,
    moment: int,
    current_nonclean: int,
    residual_rows: tuple[tuple[str, int], ...],
) -> None:
    key = engine["keys"][lane]
    state = un_slice(engine["columns"], lane)
    initial = bytes(engine["initial_states"][lane])
    previous_nonclean = int(engine["previous_nonclean"])
    nonclean_counts = engine["nonclean_prefix_counts"]
    inequality_counts = engine["initial_inequality_counts"]
    if outcome == "TRANSIENT":
        verification = {
            "method":
                "ONLINE_EXACT_LANDED_CLEANLINESS_AT_EVERY_INTEGER_MOMENT",
            "earlier_moments_checked": moment,
            "earlier_moments_all_nonclean":
                nonclean_counts[lane] == moment,
            "landed_veto_at_moment_minus_1":
                bool(previous_nonclean & (1 << lane)),
            "terminal_is_clean":
                not bool(current_nonclean & (1 << lane)),
            "direct_clean_agreement": clean_postimage(state),
            "terminal_state_sha256": state_sha256(state),
        }
        verification["pass"] = (
            verification["earlier_moments_all_nonclean"]
            and verification["landed_veto_at_moment_minus_1"]
            and verification["terminal_is_clean"]
            and verification["direct_clean_agreement"]
        )
        period = None
    elif outcome == "CYCLE":
        verification = {
            "method":
                "EXACT_RETURN_TO_T0_TESTED_AT_EVERY_INTEGER_MOMENT",
            "entry_t": 0,
            "closure_t": moment,
            "exact_recurrence_to_initial": state == initial,
            "earlier_returns_checked": moment - 1,
            "every_earlier_return_rejected":
                inequality_counts[lane] == moment - 1,
            "minimal_period":
                inequality_counts[lane] == moment - 1,
            "all_cycle_phases_nonclean":
                nonclean_counts[lane] == moment,
            "terminal_direct_nonclean": not clean_postimage(state),
            "reversibility_basis":
                "landed update is a composition solely of distinct-wire "
                "X/CNOT/TOF gates",
            "terminal_state_sha256": state_sha256(state),
        }
        verification["pass"] = (
            verification["exact_recurrence_to_initial"]
            and verification["every_earlier_return_rejected"]
            and verification["minimal_period"]
            and verification["all_cycle_phases_nonclean"]
            and verification["terminal_direct_nonclean"]
        )
        period = moment
    else:
        raise AssertionError(("unknown resolution outcome", outcome))
    minus5 = recover_state(engine, lane, max(0, moment - 5))
    row = {
        "key": key,
        "outcome": outcome,
        "resolution_moment": moment,
        "first_clean_t": moment if outcome == "TRANSIENT" else None,
        "cycle_entry_t": 0 if outcome == "CYCLE" else None,
        "minimal_state_period": period,
        "terminal_state_sha256": state_sha256(state),
        "moment_minus_5_t": max(0, moment - 5),
        "moment_minus_5_state_sha256": state_sha256(minus5),
        "landed_support_at_terminal":
            support_at_lane(engine["columns"], lane, residual_rows),
        "verification": verification,
    }
    engine["records"][key] = row
    engine["resolution_states"][key] = state
    engine["minus5_states"][key] = minus5


def evolve(
    engine: dict[str, object],
    stop: int,
    residual_rows: tuple[tuple[str, int], ...],
) -> dict[str, object]:
    start = int(engine["last_t"])
    if stop < start:
        raise AssertionError(("backwards evolution", start, stop))
    started = monotonic()
    start_mask = int(engine["active_mask"])
    phase_keys = []
    logical_transitions = 0
    physical_updates = 0
    interval = int(engine["checkpoint_interval"])
    for moment in range(start + 1, stop + 1):
        active_before = int(engine["active_mask"])
        for lane in lane_numbers(active_before):
            engine["transition_counts"][lane] += 1
        logical_transitions += active_before.bit_count()
        advance(engine["columns"], engine["schedule"])
        physical_updates += 1
        current_nonclean = nonclean_mask(
            engine["columns"], residual_rows
        )
        clean_hits = active_before & ~current_nonclean
        recurrence_hits = equality_to_initial_mask(
            engine["columns"],
            engine["initial_columns"],
            active_before & ~clean_hits,
        )
        for lane in lane_numbers(clean_hits):
            record_resolution(
                engine, lane, "TRANSIENT", moment,
                current_nonclean, residual_rows,
            )
            phase_keys.append(engine["keys"][lane])
        for lane in lane_numbers(recurrence_hits):
            record_resolution(
                engine, lane, "CYCLE", moment,
                current_nonclean, residual_rows,
            )
            phase_keys.append(engine["keys"][lane])
        engine["active_mask"] = (
            active_before & ~(clean_hits | recurrence_hits)
        )
        for lane in lane_numbers(int(engine["active_mask"])):
            engine["nonclean_prefix_counts"][lane] += int(
                bool(current_nonclean & (1 << lane))
            )
            engine["initial_inequality_counts"][lane] += 1
        engine["previous_nonclean"] = current_nonclean
        if moment % interval == 0:
            engine["checkpoints"][moment] = tuple(
                un_slice(engine["columns"], lane)
                for lane in range(len(engine["keys"]))
            )
    engine["last_t"] = stop
    upper = start_mask.bit_count() * (stop - start)
    expected_savings = sum(
        stop - int(engine["records"][key]["resolution_moment"])
        for key in phase_keys
    )
    return {
        "start_horizon": start,
        "end_horizon": stop,
        "active_keys_before": start_mask.bit_count(),
        "active_keys_after": int(engine["active_mask"]).bit_count(),
        "resolutions_in_phase": len(phase_keys),
        "resolved_keys": tuple(phase_keys),
        "logical_transitions_executed": logical_transitions,
        "logical_transition_upper_if_no_terminals": upper,
        "logical_transitions_saved_by_terminals":
            upper - logical_transitions,
        "expected_savings_from_resolution_moments":
            expected_savings,
        "transition_accounting_exact":
            upper - logical_transitions == expected_savings,
        "physical_global_updates": physical_updates,
        "expected_physical_global_updates": stop - start,
        "complete_population":
            physical_updates == stop - start,
        "population_accounting":
            start_mask.bit_count()
            == int(engine["active_mask"]).bit_count() + len(phase_keys),
        "seconds": round(monotonic() - started, 6),
    }


def boundary_snapshot(
    engine: dict[str, object],
    horizon: int,
    residual_rows: tuple[tuple[str, int], ...],
) -> dict[str, object]:
    active_mask = int(engine["active_mask"])
    lanes = lane_numbers(active_mask)
    keys = engine["keys"]
    columns = engine["columns"]
    current_nonclean = nonclean_mask(columns, residual_rows)
    recurrence = equality_to_initial_mask(
        columns, engine["initial_columns"], active_mask
    )
    rows = tuple({
        "key": keys[lane],
        "state_sha256": state_sha256(un_slice(columns, lane)),
        "landed_support": support_at_lane(
            columns, lane, residual_rows
        ),
        "compiled_nonclean":
            bool(current_nonclean & (1 << lane)),
        "direct_nonclean":
            not clean_postimage(un_slice(columns, lane)),
    } for lane in lanes)
    result = {
        "horizon": horizon,
        "open_count": len(lanes),
        "resolved_count": len(engine["records"]),
        "population_accounting":
            len(lanes) + len(engine["records"]) == len(keys),
        "open_keys": tuple(keys[lane] for lane in lanes),
        "open_key_sha256": digest(tuple(keys[lane] for lane in lanes)),
        "state_rows": rows,
        "state_rows_sha256": digest(rows),
        "support_weight_census": dict(sorted(Counter(
            len(row["landed_support"]) for row in rows
        ).items())),
        "all_open_landed_nonclean":
            active_mask & ~current_nonclean == 0,
        "all_open_direct_nonclean":
            all(row["direct_nonclean"] for row in rows),
        "compiled_direct_cleanliness_agreement":
            all(
                row["compiled_nonclean"] == row["direct_nonclean"]
                for row in rows
            ),
        "no_open_state_equals_t0": recurrence == 0,
        "all_prior_cleanliness_tests_certified": all(
            engine["nonclean_prefix_counts"][lane] == horizon + 1
            for lane in lanes
        ),
        "all_prior_cycle_returns_excluded": all(
            engine["initial_inequality_counts"][lane] == horizon
            for lane in lanes
        ),
    }
    result["pass"] = (
        result["population_accounting"]
        and result["all_open_landed_nonclean"]
        and result["all_open_direct_nonclean"]
        and result["compiled_direct_cleanliness_agreement"]
        and result["no_open_state_equals_t0"]
        and result["all_prior_cleanliness_tests_certified"]
        and result["all_prior_cycle_returns_excluded"]
    )
    return result


def determinism_snapshot(
    engine: dict[str, object],
    horizon: int,
) -> dict[str, object]:
    rows = tuple({
        "key": key,
        "primary_sha256": state_sha256(un_slice(
            engine["columns"], engine["primary_index"][key]
        )),
        "duplicate_sha256": state_sha256(un_slice(
            engine["columns"], engine["duplicate_index"][key]
        )),
        "exact_state_equal":
            un_slice(
                engine["columns"], engine["primary_index"][key]
            )
            == un_slice(
                engine["columns"], engine["duplicate_index"][key]
            ),
    } for key in engine["duplicate_index"])
    return {
        "horizon": horizon,
        "rows": rows,
        "rows_sha256": digest(rows),
        "all_exact": all(row["exact_state_equal"] for row in rows),
    }


def benchmark(
    engine: dict[str, object],
    ticks: int = PILOT_TICKS,
) -> dict[str, object]:
    columns = engine["columns"].copy()
    started = monotonic()
    for _tick in range(ticks):
        advance(columns, engine["schedule"])
    seconds = monotonic() - started
    instructions = len(engine["schedule"]) * ticks
    return {
        "ticks": ticks,
        "schedule_instructions_per_tick": len(engine["schedule"]),
        "instructions": instructions,
        "seconds": round(seconds, 6),
        "seconds_per_instruction":
            seconds / instructions if instructions else 0.0,
        "result_sha256": digest(tuple(columns)),
    }


def select_horizon(
    pilot: dict[str, object],
    script_started: float,
    choices: tuple[int, ...],
) -> tuple[int | None, dict[str, object]]:
    seconds_per_instruction = float(pilot["seconds_per_instruction"])
    per_tick = int(pilot["schedule_instructions_per_tick"])
    elapsed = monotonic() - script_started
    rows = tuple({
        "horizon": candidate,
        "projected_total_seconds": round(
            elapsed
            + SAFETY_FACTOR
            * seconds_per_instruction
            * per_tick
            * candidate
            + RESERVE_SECONDS,
            6,
        ),
        "fits_execution_budget": (
            elapsed
            + SAFETY_FACTOR
            * seconds_per_instruction
            * per_tick
            * candidate
            + RESERVE_SECONDS
            < EXECUTION_BUDGET_SEC
        ),
    } for candidate in choices)
    selected = next(
        (
            int(row["horizon"])
            for row in rows if row["fits_execution_budget"]
        ),
        None,
    )
    return selected, {
        "policy":
            "deepest complete candidate whose measured schedule rate, "
            "multiplied by 1.40 with 60 seconds reserve, fits 1425 seconds",
        "pilot": pilot,
        "elapsed_before_selection": round(elapsed, 6),
        "candidate_rows": rows,
        "selected_horizon": selected,
        "never_partial": True,
    }


def pairwise_separations(positions: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sorted(
        min(
            (right - left) % RING_STATIONS,
            (left - right) % RING_STATIONS,
        )
        for left, right in combinations(positions, 2)
    ))


def geometry_row(key: Key) -> dict[str, object]:
    profile = pairwise_separations(key[1])
    return {
        "key": key,
        "pairwise_cyclic_separation_profile": profile,
        "minimum_separation": min(profile),
        "contains_saturated_gap_2": 2 in profile,
        "trio_forecast_key": key in TRIO_KEYS,
    }


def pair_battery(
    rows: tuple[dict[str, object], ...],
    resolution_states: dict[Key, State],
    minus5_states: dict[Key, State],
) -> dict[str, object]:
    tests = tuple({
        "left_key": left["key"],
        "right_key": right["key"],
        "same_event": left["key"][2] == right["key"][2],
        "same_resolution_moment":
            left["resolution_moment"] == right["resolution_moment"],
        "same_outcome": left["outcome"] == right["outcome"],
        "same_terminal_full_state":
            resolution_states[left["key"]]
            == resolution_states[right["key"]],
        "same_moment_minus_5_full_state":
            minus5_states[left["key"]]
            == minus5_states[right["key"]],
        "same_minimal_period":
            left["minimal_state_period"]
            == right["minimal_state_period"],
    } for left, right in combinations(rows, 2))
    return {
        "resolution_count": len(rows),
        "tested_pair_count": len(tests),
        "expected_pair_count": len(rows) * (len(rows) - 1) // 2,
        "rows": tests,
        "rows_sha256": digest(tests),
        "pair_accounting_exact":
            len(tests) == len(rows) * (len(rows) - 1) // 2,
    }


def forecast_certificate(
    engine: dict[str, object],
    horizon: int,
) -> dict[str, object]:
    records = engine["records"]
    event_rows = []
    for event in (2, 3):
        keys = tuple(
            key for key in TRIO_KEYS if key[2] == event
        )
        resolved = tuple(
            records[key] for key in keys if key in records
        )
        all_resolved = len(resolved) == 3
        shared_moment = (
            all_resolved
            and len({
                row["resolution_moment"] for row in resolved
            }) == 1
        )
        shared_outcome = (
            all_resolved
            and len({row["outcome"] for row in resolved}) == 1
        )
        shared_terminal = (
            all_resolved
            and len({
                engine["resolution_states"][row["key"]]
                for row in resolved
            }) == 1
        )
        shared_minus5 = (
            all_resolved
            and len({
                engine["minus5_states"][row["key"]]
                for row in resolved
            }) == 1
        )
        periods = tuple(
            row["minimal_state_period"] for row in resolved
        )
        shared_period_if_cycles = (
            shared_outcome
            and (
                resolved[0]["outcome"] != "CYCLE"
                or len(set(periods)) == 1
            )
        ) if resolved else False
        if not resolved:
            outcome = "UNTESTED-AT-HORIZON"
        elif (
            all_resolved
            and shared_moment
            and shared_outcome
            and shared_minus5
            and shared_period_if_cycles
        ):
            outcome = "FORECAST_CONFIRMED"
        else:
            outcome = "FORECAST_REFUTED"
        event_rows.append({
            "event": event,
            "keys": keys,
            "resolved_count": len(resolved),
            "resolved_rows": resolved,
            "all_three_resolved": all_resolved,
            "shared_resolution_moment": shared_moment,
            "shared_outcome": shared_outcome,
            "shared_terminal_full_state": shared_terminal,
            "shared_moment_minus_5_full_state": shared_minus5,
            "shared_minimal_period_if_cycles":
                shared_period_if_cycles,
            "event_outcome": outcome,
        })
    if any(
        row["event_outcome"] == "FORECAST_REFUTED"
        for row in event_rows
    ):
        outcome = "FORECAST_REFUTED"
    elif any(
        row["event_outcome"] == "FORECAST_CONFIRMED"
        for row in event_rows
    ):
        outcome = "FORECAST_CONFIRMED"
    else:
        outcome = "UNTESTED-AT-HORIZON"
    resolved_rows = tuple(
        records[key] for key in TRIO_KEYS if key in records
    )
    battery = pair_battery(
        resolved_rows,
        engine["resolution_states"],
        engine["minus5_states"],
    )
    result = {
        "registered_surface": TRIO_KEYS,
        "horizon": horizon,
        "resolution_count": len(resolved_rows),
        "event_rows": tuple(event_rows),
        "full_cohort_battery": battery,
        "forecast_outcome": outcome,
        "allowed_exact_outcomes": (
            "FORECAST_CONFIRMED",
            "FORECAST_REFUTED",
            "UNTESTED-AT-HORIZON",
        ),
    }
    result["pass"] = (
        outcome in result["allowed_exact_outcomes"]
        and battery["pair_accounting_exact"]
        and all(
            row["resolved_count"] + sum(
                key not in records for key in row["keys"]
            ) == 3
            for row in event_rows
        )
        and all(
            row["verification"]["pass"] for row in resolved_rows
        )
    )
    return result


def nontrio_certificate(
    engine: dict[str, object],
    horizon: int,
) -> dict[str, object]:
    records = engine["records"]
    rows = tuple(
        records[key] for key in NONTRIO_KEYS if key in records
    )
    structure_rows = tuple({
        **geometry_row(row["key"]),
        "outcome": row["outcome"],
        "resolution_moment": row["resolution_moment"],
        "terminal_state_sha256": row["terminal_state_sha256"],
        "moment_minus_5_state_sha256":
            row["moment_minus_5_state_sha256"],
        "verification_pass": row["verification"]["pass"],
    } for row in rows)
    battery = pair_battery(
        rows,
        engine["resolution_states"],
        engine["minus5_states"],
    )
    null_applies = not rows
    transition_rows = tuple({
        "key": key,
        "transitions_t0_to_horizon":
            engine["transition_counts"][engine["primary_index"][key]],
        "expected_if_open": horizon,
        "exact":
            engine["transition_counts"][engine["primary_index"][key]]
            == horizon,
    } for key in NONTRIO_KEYS)
    result = {
        "nontrio_keys": NONTRIO_KEYS,
        "resolution_count": len(rows),
        "resolution_rows": rows,
        "structure_rows": structure_rows,
        "full_cohort_battery": battery,
        "null_applies": null_applies,
        "null_statement": (
            f"NO NONTRIO RESOLUTION FROM T={LANDED_HORIZON + 1} "
            f"THROUGH COMPLETE T={horizon}"
            if null_applies else
            "NULL DOES NOT APPLY; ALL NONTRIO RESOLUTIONS ARE PRINTED"
        ),
        "transition_rows": transition_rows,
    }
    result["pass"] = (
        battery["pair_accounting_exact"]
        and all(row["verification_pass"] for row in structure_rows)
        and (
            not null_applies
            or all(row["exact"] for row in transition_rows)
        )
    )
    return result


def identity_certificate(
    context: dict[str, object],
    residual_rows: tuple[tuple[str, int], ...],
) -> dict[str, object]:
    keys = (IDENTITY_TRANSIENT[0], IDENTITY_CYCLE[0])
    engine = make_engine(
        "identity_controls", keys, context, residual_rows
    )
    phase = evolve(
        engine, IDENTITY_CYCLE[1], residual_rows
    )
    transient = engine["records"].get(IDENTITY_TRANSIENT[0])
    cycle = engine["records"].get(IDENTITY_CYCLE[0])
    result = {
        "transient_expected": IDENTITY_TRANSIENT,
        "transient_observed": transient,
        "cycle_expected": IDENTITY_CYCLE,
        "cycle_observed": cycle,
        "phase": phase,
        "engine_construction_pass": engine["construction_pass"],
    }
    result["pass"] = (
        engine["construction_pass"]
        and transient is not None
        and transient["outcome"] == "TRANSIENT"
        and transient["resolution_moment"] == IDENTITY_TRANSIENT[1]
        and transient["verification"]["pass"]
        and cycle is not None
        and cycle["outcome"] == "CYCLE"
        and cycle["resolution_moment"] == IDENTITY_CYCLE[1]
        and cycle["minimal_state_period"] == IDENTITY_CYCLE[1]
        and cycle["verification"]["pass"]
        and phase["complete_population"]
        and phase["transition_accounting_exact"]
    )
    return result


def optional_k2_certificate(
    script_started: float,
    context: dict[str, object],
    residual_rows: tuple[tuple[str, int], ...],
) -> dict[str, object]:
    pilot_engine = make_engine(
        "k2_station0_pilot",
        K2_STATION0_S5_OPEN_THROUGH_T65536,
        context,
        residual_rows,
    )
    pilot = benchmark(pilot_engine)
    selected, declaration = select_horizon(
        pilot,
        script_started,
        (262144, 131072),
    )
    if selected is None:
        return {
            "declaration": "SKIPPED_AFTER_K3_BUDGET_PROJECTION",
            "keys": K2_STATION0_S5_OPEN_THROUGH_T65536,
            "selection": declaration,
            "partial_science_sweep_reported": False,
            "pass": True,
        }
    engine = make_engine(
        "k2_station0_complete",
        K2_STATION0_S5_OPEN_THROUGH_T65536,
        context,
        residual_rows,
    )
    baseline_phase = evolve(engine, LANDED_HORIZON, residual_rows)
    baseline = boundary_snapshot(
        engine, LANDED_HORIZON, residual_rows
    )
    deep_phase = evolve(engine, selected, residual_rows)
    final = boundary_snapshot(engine, selected, residual_rows)
    rows = tuple(sorted(
        (
            row for row in engine["records"].values()
            if row["resolution_moment"] > LANDED_HORIZON
        ),
        key=lambda row: (row["resolution_moment"], row["key"]),
    ))
    battery = pair_battery(
        rows, engine["resolution_states"], engine["minus5_states"]
    )
    baseline_exact = (
        not engine["records"]
        if selected == LANDED_HORIZON else
        baseline_phase["resolutions_in_phase"] == 0
    )
    result = {
        "declaration": "RUN_AFTER_K3_WITHIN_BUDGET",
        "keys": K2_STATION0_S5_OPEN_THROUGH_T65536,
        "selection": declaration,
        "landed_horizon": LANDED_HORIZON,
        "target_horizon": selected,
        "baseline_phase": baseline_phase,
        "baseline_boundary": baseline,
        "deep_phase": deep_phase,
        "final_boundary": final,
        "new_resolution_count": len(rows),
        "new_resolutions": rows,
        "cohort_battery": battery,
        "null_applies": not rows,
        "partial_science_sweep_reported": False,
    }
    result["pass"] = (
        pilot_engine["construction_pass"]
        and engine["construction_pass"]
        and baseline_exact
        and baseline["pass"]
        and baseline["open_count"] == 6
        and deep_phase["complete_population"]
        and deep_phase["transition_accounting_exact"]
        and final["pass"]
        and battery["pair_accounting_exact"]
        and all(row["verification"]["pass"] for row in rows)
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
    lines.extend(
        f"CERTIFICATE {name} {compact(value)}"
        for name, value in certificates.items()
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
            "CYCLE838_K3_TRIO_FORECAST_PASS"
            if report["pass"]
            else "CYCLE838_K3_TRIO_FORECAST_HONEST_FAIL"
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
    script_started = monotonic()
    sources = source_controls()
    residual_rows = watched_residual_rows()
    basis = basis_certificate(residual_rows)
    context = build_context()
    identity = identity_certificate(context, residual_rows)

    pilot_engine = make_engine(
        "k3_pilot",
        K3_OPEN_THROUGH_T65536,
        context,
        residual_rows,
        K3_OPEN_THROUGH_T65536[:DETERMINISM_KEYS],
    )
    k3_pilot = benchmark(pilot_engine)
    selected, horizon_declaration = select_horizon(
        k3_pilot, script_started, TARGET_CHOICES
    )
    if selected is None:
        selected = LANDED_HORIZON
        horizon_declaration["selected_horizon"] = selected
        horizon_declaration["fallback"] = (
            "no projected candidate fit; replay landed boundary only"
        )

    engine = make_engine(
        "k3_complete",
        K3_OPEN_THROUGH_T65536,
        context,
        residual_rows,
        K3_OPEN_THROUGH_T65536[:DETERMINISM_KEYS],
    )
    baseline_phase = evolve(engine, LANDED_HORIZON, residual_rows)
    baseline_boundary = boundary_snapshot(
        engine, LANDED_HORIZON, residual_rows
    )
    baseline_determinism = determinism_snapshot(
        engine, LANDED_HORIZON
    )
    deep_phase = evolve(engine, selected, residual_rows)
    final_boundary = boundary_snapshot(
        engine, selected, residual_rows
    )
    final_determinism = determinism_snapshot(engine, selected)

    new_resolutions = tuple(sorted(
        (
            row for row in engine["records"].values()
            if row["resolution_moment"] > LANDED_HORIZON
        ),
        key=lambda row: (row["resolution_moment"], row["key"]),
    ))
    baseline_exact = (
        baseline_phase["resolutions_in_phase"] == 0
        and baseline_boundary["pass"]
        and baseline_boundary["open_count"]
        == len(K3_OPEN_THROUGH_T65536)
    )
    certificate_a = {
        "continuation_surface":
            "all literal Cycle834 open canonical k=3 "
            "representative/event keys",
        "literal_open_key_count": len(K3_OPEN_THROUGH_T65536),
        "literal_open_keys": K3_OPEN_THROUGH_T65536,
        "supplied_33_key_count": SUPPLIED_K3_FAMILY_COUNT,
        "count_reconciliation":
            "Cycle834 literal is 10, not 33; no keys invented",
        "landed_horizon": LANDED_HORIZON,
        "horizon_declaration": horizon_declaration,
        "deepest_complete_power_of_two": selected,
        "target_T262144_reached": selected == 262144,
        "partial_horizon_reported": False,
        "engine": {
            "primary_lanes": len(K3_OPEN_THROUGH_T65536),
            "determinism_duplicate_lanes": DETERMINISM_KEYS,
            "state_bits": len(engine["columns"]),
            "schedule_instructions_per_tick":
                len(engine["schedule"]),
            "construction_pass": engine["construction_pass"],
            "one_step_scalar_equivalence":
                all(row["exact"] for row in engine["one_step_rows"]),
        },
        "baseline_phase": baseline_phase,
        "baseline_boundary": baseline_boundary,
        "deep_phase": deep_phase,
        "final_boundary": final_boundary,
        "baseline_exact": baseline_exact,
        "new_resolution_count": len(new_resolutions),
        "new_resolutions": new_resolutions,
        "all_resolution_verifications_pass": all(
            row["verification"]["pass"] for row in new_resolutions
        ),
        "final_population_accounting":
            final_boundary["open_count"] + len(new_resolutions)
            == len(K3_OPEN_THROUGH_T65536),
    }
    certificate_a["pass"] = (
        sources["pass"]
        and basis["pass"]
        and context["pass"]
        and pilot_engine["construction_pass"]
        and engine["construction_pass"]
        and baseline_exact
        and selected >= LANDED_HORIZON
        and deep_phase["complete_population"]
        and deep_phase["transition_accounting_exact"]
        and final_boundary["pass"]
        and certificate_a["all_resolution_verifications_pass"]
        and certificate_a["final_population_accounting"]
    )

    forecast = forecast_certificate(engine, selected)
    nontrio = nontrio_certificate(engine, selected)
    optional_k2 = optional_k2_certificate(
        script_started, context, residual_rows
    )

    deterministic = (
        engine["duplicate_initial_exact"]
        and engine["duplicate_masks_exact"]
        and baseline_determinism["all_exact"]
        and final_determinism["all_exact"]
    )
    elapsed = monotonic() - script_started
    controls_base = (
        sources["pass"]
        and basis["pass"]
        and context["pass"]
        and identity["pass"]
        and deterministic
        and not any(
            name in sys.modules for name in BLOCKLISTED_MODULES
        )
        and not FIREWALL.hits
        and elapsed < AUDIT_TIMEOUT_SEC
    )
    controls = {
        **sources,
        "cleanliness_basis": basis,
        "context": {
            key: value for key, value in context.items()
            if key not in {"program", "fixtures"}
        },
        "dependency_policy":
            "Python stdlib plus sole executable landed Cycle719 core; "
            "Cycles831/834 are SHA-pinned text/AST-only and blocklisted",
        "exact_arithmetic":
            "all dynamics, cleanliness, recurrence, state equality, "
            "counts, geometry, and hashes are exact; only runtime is float",
        "determinism_scope": {
            "declaration":
                "first two literal k3 open keys carried as independent "
                "duplicate lanes from t=0 through both complete boundaries",
            "keys": K3_OPEN_THROUGH_T65536[:DETERMINISM_KEYS],
            "duplicate_initial_exact":
                engine["duplicate_initial_exact"],
            "duplicate_schedule_masks_exact":
                engine["duplicate_masks_exact"],
            "boundary_rows": (
                baseline_determinism,
                final_determinism,
            ),
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
    }
    checks = {
        "A_DEEP_CONTINUATION_COMPLETE_AND_CERTIFIED":
            bool(certificate_a["pass"]),
        "B_REGISTERED_TRIO_FORECAST_EXACT":
            bool(forecast["pass"]),
        "C_NONTRIO_EVENTS_OR_NULL_EXACT":
            bool(nontrio["pass"]),
        "D_IDENTITY_TRANSIENT_AND_CYCLE":
            bool(identity["pass"]),
        "E_SHAS_BLOCKLIST_DETERMINISM_PATHS_RUNTIME_STDOUT":
            controls_base,
    }
    certificates = {
        "A_DEEP_CONTINUATION": certificate_a,
        "B_FORECAST_TEST": forecast,
        "C_NONTRIO_RESOLUTIONS_OR_NULL": nontrio,
        "D_IDENTITY_CONTROLS": identity,
        "E_CONTROLS": controls,
        "OPTIONAL_K2_STATION0_S5": optional_k2,
    }
    report = {
        "cycle": 838,
        "k3_landed_open_count": len(K3_OPEN_THROUGH_T65536),
        "supplied_k3_family_count": SUPPLIED_K3_FAMILY_COUNT,
        "supplied_count_matches_literal": False,
        "horizon_reached": selected,
        "horizon_complete": True,
        "target_T262144_reached": selected == 262144,
        "forecast_outcome": forecast["forecast_outcome"],
        "trio_resolution_count": forecast["resolution_count"],
        "nontrio_resolution_count": nontrio["resolution_count"],
        "k3_new_resolution_count": len(new_resolutions),
        "k3_final_open_count": final_boundary["open_count"],
        "optional_k2_declaration": optional_k2["declaration"],
        "optional_k2_target_horizon":
            optional_k2.get("target_horizon"),
        "optional_k2_new_resolution_count":
            optional_k2.get("new_resolution_count"),
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "checks": {},
        "pass": False,
        "terminal": "CYCLE838_K3_TRIO_FORECAST_HONEST_FAIL",
    }
    output = stable_render(checks, certificates, report)
    stdout_ok = len(output.encode("utf-8")) < STDOUT_LIMIT_BYTES
    checks[
        "E_SHAS_BLOCKLIST_DETERMINISM_PATHS_RUNTIME_STDOUT"
    ] = controls_base and stdout_ok
    controls["pass"] = checks[
        "E_SHAS_BLOCKLIST_DETERMINISM_PATHS_RUNTIME_STDOUT"
    ]
    output = stable_render(checks, certificates, report)
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        sys.stdout.write(compact({
            "pass": False,
            "failure": "stdout limit exceeded",
            "stdout_bytes": len(output.encode("utf-8")),
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
            "terminal": "CYCLE838_K3_TRIO_FORECAST_HONEST_FAIL",
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
            "terminal": "CYCLE838_K3_TRIO_FORECAST_HONEST_FAIL",
        }) + "\n")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
