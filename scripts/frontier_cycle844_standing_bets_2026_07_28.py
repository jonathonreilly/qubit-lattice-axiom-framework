#!/usr/bin/env python3
"""Cycle 844: every standing bet on one exact deep continuation.

The landed Cycle-719 controller core is the sole executable science
dependency.  Cycles 834, 838, and 843 are SHA-pinned text/AST-only source
primaries and are import-blocklisted.  The runner sweeps the ten literal
landed open k=3 keys and the two named station-0 event-0 k=2 keys.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
EXECUTION_BUDGET_SEC = 1450
STDOUT_LIMIT_BYTES = 200 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle834_k3_backbone_2026_07_28.py",
    "scripts/frontier_cycle838_k3_trio_forecast_2026_07_28.py",
    "scripts/frontier_cycle843_pulse_phase_2026_07_28.py",
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
BLOCKLISTED_MODULES = tuple(Path(path).stem for path in TEXT_AST_ONLY_PATHS)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "8ed75c4e6f19fa5e8a9492225aae681ab85017dcfac00f8ab109b7c587aeddaa",
    AUDIT_INPUT_PATHS[2]:
        "ea668b4d0be960622cd10d4e16b3cd1056d343db80ee6845407ca6ddb3e604c0",
    AUDIT_INPUT_PATHS[3]:
        "68116221b3451aefd294d939b788cd3dbf518a190eaebd996b43fba5e8a54de9",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    AUDIT_INPUT_PATHS[1]: "89d4506c6df9738bf0458027ab76cc9d2f9710ab",
    AUDIT_INPUT_PATHS[2]: "2f89c8eb911375bed58b1126e9f5f7b860ead20a",
    AUDIT_INPUT_PATHS[3]: "cd500d58847c3c1046c500b73b25911920db0ce0",
}
EXPECTED_BRANCH = "physics-loop/toe-close-blockC26-20260729"
EXPECTED_BASE = "a902a8204b43e616272be79b18ca337f078d84d0"


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


Key = tuple[int, tuple[int, ...], int]
State = bytes
MaskedGate = tuple[int, int, int, int, int]
RING_STATIONS = 11
FIXTURE_BANKS = 2
STATE_BITS = 5815
WATCHED_COORDINATE_COUNT = 477
LANDED_HORIZON = 262144
K3_TARGET_CHOICES = (524288, 262144, 131072)
K2_TARGET_HORIZON = 2097152
PILOT_TICKS = 256
SAFETY_FACTOR = 1.16
RESERVE_SECONDS = 105.0
CHECKPOINT_INTERVAL = 1024
DETERMINISM_KEYS_PER_FAMILY = 1

K3_KEYS: tuple[Key, ...] = (
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
    key for key in K3_KEYS
    if key[1] in ((0, 2, 6), (0, 2, 7), (0, 2, 8))
)
OTHER_K3_KEYS: tuple[Key, ...] = tuple(
    key for key in K3_KEYS if key not in TRIO_KEYS
)
K2_EVENT0_KEYS: tuple[Key, ...] = (
    (2, (0, 5), 0),
    (2, (0, 6), 0),
)
K3_IDENTITY = ((3, (0, 2, 5), 2), "TRANSIENT", 444)
K2_IDENTITY = ((2, (0, 5), 1), "TRANSIENT", 193210)
EXPECTED_TARGETS = {
    "S0_prime": {
        "sha256":
            "d874aeeb1d4e5ca29b806886314c796ac32e6658b21f888d8e2aa01044905c12",
        "weight": 47,
    },
    "pulse_coincidence_state": {
        "sha256":
            "4a7ce9fd4e9ebfdbd8580c33122d9e87c3896b24ef196e34bec49e233d044375",
        "weight": 59,
    },
}


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def state_sha256(state: State | tuple[int, ...]) -> str:
    return sha256(bytes(state)).hexdigest()


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
        elif (
            isinstance(node, ast.AnnAssign)
            and isinstance(node.target, ast.Name)
            and node.target.id == name
            and node.value is not None
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
    self_tree = ast.parse(
        Path(__file__).read_bytes(), filename=Path(__file__).name
    )
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
    landed_keys = literal_assignment(
        trees[AUDIT_INPUT_PATHS[1]], "LANDED_K3_OPEN_THROUGH_65536"
    )
    branch = git_value("branch", "--show-current")
    base_is_ancestor = (
        git_value("merge-base", "HEAD", EXPECTED_BASE) == EXPECTED_BASE
    )
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_INPUT_PATHS_literal":
            literal_assignment(self_tree, "AUDIT_INPUT_PATHS")
            == AUDIT_INPUT_PATHS,
        "named_input_count": len(AUDIT_INPUT_PATHS),
        "maximum_named_inputs": 7,
        "all_paths_existing_worktree_relative":
            len(payloads) == len(AUDIT_INPUT_PATHS)
            and all(row["exists_worktree_relative"] for row in source_rows),
        "source_rows": source_rows,
        "text_AST_only_paths": TEXT_AST_ONLY_PATHS,
        "blocked_modules": BLOCKLISTED_MODULES,
        "direct_frontier_imports": direct_frontier_imports,
        "landed_k3_keys": landed_keys,
        "literal_k3_surface_exact": landed_keys == K3_KEYS,
        "git_branch": branch,
        "expected_git_branch": EXPECTED_BRANCH,
        "expected_base": EXPECTED_BASE,
        "expected_base_is_ancestor": base_is_ancestor,
    }
    result["pass"] = (
        result["AUDIT_INPUT_PATHS_literal"]
        and result["named_input_count"] <= result["maximum_named_inputs"]
        and result["all_paths_existing_worktree_relative"]
        and all(
            row["sha256_exact"] and row["git_blob_exact"]
            and row["AST_valid"] for row in source_rows
        )
        and direct_frontier_imports
        == (
            "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26",
        )
        and result["literal_k3_surface_exact"]
        and branch == EXPECTED_BRANCH
        and base_is_ancestor
        and not any(name in sys.modules for name in BLOCKLISTED_MODULES)
        and not FIREWALL.hits
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
    genesis = bytes(K.M.pack_state(banks, links))
    result = {
        "state_width": len(genesis),
        "watched_coordinate_count": len(indices),
        "unique_coordinate_count": len(set(indices)),
        "coordinate_bounds_exact":
            min(indices) >= 0 and max(indices) < len(genesis),
        "zero_state_clean": clean_postimage(bytes(len(genesis))),
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


def un_slice(
    columns: list[int] | tuple[int, ...],
    lane: int,
) -> State:
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


def advance_uniform(
    columns: list[int],
    compiled: tuple[tuple[int, int, int, int], ...],
    lane_mask: int,
) -> None:
    for kind, first, second, third in compiled:
        if kind == 0:
            columns[first] ^= lane_mask
        elif kind == 1:
            columns[second] ^= columns[first] & lane_mask
        else:
            columns[third] ^= (
                columns[first] & columns[second] & lane_mask
            )


def reconstruct_named_states(
    context: dict[str, object],
) -> dict[str, object]:
    program = context["program"]
    fixtures = context["fixtures"]
    witness = (1, 6)
    word = synchronous_word(program, witness)
    compiled = compile_word(word)
    event0 = K.A.apply_semantic(fixtures[0][2], word)
    event1 = K.A.apply_semantic(fixtures[1][2], word)
    columns = bit_slice((event0, event1))
    captured: dict[str, State] = {}
    capture_at = {
        14744: ("funnel_weight_51", 0),
        14748: ("funnel_weight_57", 0),
        51110: ("event1_funnel", 1),
    }
    for moment in range(1, max(capture_at) + 1):
        advance_uniform(columns, compiled, 0b11)
        if moment in capture_at:
            name, lane = capture_at[moment]
            captured[name] = un_slice(columns, lane)
    s0_bits = list(captured.pop("event1_funnel"))
    head1 = K.M.R12.BANK_BASES[0] + K.A.HEAD[1]
    s0_bits[head1] ^= 1
    captured["S0_prime"] = bytes(s0_bits)
    captured["pulse_coincidence_state"] = bytes(fixtures[3][2])
    rows = {
        name: {
            "sha256": state_sha256(state),
            "weight": sum(state),
        }
        for name, state in captured.items()
    }
    exact = (
        rows["S0_prime"] == EXPECTED_TARGETS["S0_prime"]
        and rows["pulse_coincidence_state"]
        == EXPECTED_TARGETS["pulse_coincidence_state"]
        and rows["funnel_weight_51"]["weight"] == 51
        and rows["funnel_weight_57"]["weight"] == 57
    )
    return {
        "states": captured,
        "rows": rows,
        "construction": {
            "witness": witness,
            "event0_captures": (14744, 14748),
            "S0_prime":
                "event-1 witness state at t=51110 XOR bank0.HEAD[1]",
            "pulse_coincidence_state": "event-3 prepared epoch state",
        },
        "pass": exact,
    }


def target_windows(state: State) -> tuple[tuple[int, ...], ...]:
    active = tuple(wire for wire, bit in enumerate(state) if bit)
    inactive = tuple(wire for wire, bit in enumerate(state) if not bit)
    chosen = []
    for window in range(4):
        on = active[window * 6:(window + 1) * 6]
        offset = window * 193
        off = inactive[offset:offset + 6]
        chosen.append(tuple(sorted((*on, *off))))
    return tuple(chosen)


def make_watch_definitions(
    named: dict[str, object],
) -> dict[str, dict[str, object]]:
    states = named["states"]
    definitions = {}
    for name, state in states.items():
        windows = target_windows(state)
        definitions[name] = {
            "state": state,
            "windows": windows,
            "window_sha256": tuple(
                sha256(bytes(state[wire] for wire in window)).hexdigest()
                for window in windows
            ),
        }
    return definitions


def nonclean_mask(
    columns: list[int] | tuple[int, ...],
    residual_rows: tuple[tuple[str, int], ...],
) -> int:
    mask = 0
    for _name, wire in residual_rows:
        mask |= columns[wire]
    return mask


def equality_mask(
    columns: list[int] | tuple[int, ...],
    target: State | tuple[int, ...],
    candidates: int,
    indices: tuple[int, ...] | None = None,
) -> int:
    matches = candidates
    wires = range(len(columns)) if indices is None else indices
    for wire in wires:
        matches &= (
            columns[wire] if target[wire] else ~columns[wire]
        )
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


def component_weights(state: State) -> dict[str, object]:
    banks, links = K.M.unpack_state(state, FIXTURE_BANKS)
    source_width = K.M.R12.SOURCE_WIDTH
    return {
        "full": sum(state),
        "source": sum(state[:source_width]),
        "banks": tuple(map(sum, banks)),
        "links": tuple(map(sum, links)),
    }


def diff_summary(left: State, right: State) -> dict[str, object]:
    source_width = K.M.R12.SOURCE_WIDTH
    bank0 = K.M.R12.BANK_BASES[0]
    bank1 = K.M.R12.BANK_BASES[1]
    link0 = K.M.R12.LINK_BASES[0]
    counts: Counter[str] = Counter()
    total = 0
    for wire, (a, b) in enumerate(zip(left, right)):
        if a == b:
            continue
        total += 1
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
        "xor_weight": total,
        "component_xor_weights": dict(sorted(counts.items())),
    }


def make_engine(
    name: str,
    keys: tuple[Key, ...],
    context: dict[str, object],
    residual_rows: tuple[tuple[str, int], ...],
    watches: dict[str, dict[str, object]],
    duplicate_keys: tuple[Key, ...] = (),
) -> dict[str, object]:
    program = context["program"]
    fixtures = context["fixtures"]
    fixture_by_event = {
        event: before for event, _direction, before in fixtures
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
        k, positions0, event = key
        before = fixture_by_event[event]
        initial, rail_a, rail_b, _trace = K.run_orbit(
            before, program, token_positions=positions0
        )
        expected_rail = tuple(
            int(station in positions0) for station in range(RING_STATIONS)
        )
        semantic = K.A.apply_semantic(before, words[positions0])
        state = tuple(map(int, initial))
        initial_states.append(state)
        initial_rows.append({
            "key": key,
            "role": role,
            "k_matches_positions": k == len(positions0),
            "composition_exact": initial == semantic,
            "rail_A_exact": rail_a == expected_rail,
            "rail_B_zero": not any(rail_b),
            "initial_nonclean": not clean_postimage(state),
            "initial_sha256": state_sha256(state),
        })
    initial_states_tuple = tuple(initial_states)
    columns = bit_slice(initial_states_tuple)
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
    watch_rows = {
        watch_name: {
            "state": definition["state"],
            "windows": definition["windows"],
            "window_sha256": definition["window_sha256"],
            "trajectory_moments_tested": 0,
            "stage_candidate_counts":
                [0] * len(definition["windows"]),
            "full_state_confirmations": 0,
            "hits": [],
        }
        for watch_name, definition in watches.items()
    }
    active_mask = (1 << len(keys)) - 1
    initial_nonclean = nonclean_mask(columns, residual_rows)
    engine = {
        "name": name,
        "keys": keys,
        "lanes": lanes,
        "words": words,
        "compiled_words": compiled_words,
        "columns": columns,
        "initial_columns": tuple(columns),
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
        "last_t": 0,
        "checkpoints": {
            0: tuple(bytes(state) for state in initial_states_tuple[:len(keys)])
        },
        "boundary_snapshots": {},
        "watch_rows": watch_rows,
        "initial_rows": tuple(initial_rows),
        "one_step_rows": one_step_rows,
    }
    duplicate_exact = all(
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
    engine["duplicate_initial_exact"] = duplicate_exact
    engine["duplicate_masks_exact"] = duplicate_masks_exact
    engine["construction_pass"] = (
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
        and duplicate_exact
        and duplicate_masks_exact
    )
    update_watches(engine, 0, active_mask)
    return engine


def update_watches(
    engine: dict[str, object],
    moment: int,
    candidates: int,
) -> None:
    columns = engine["columns"]
    keys = engine["keys"]
    for watch_name, watch in engine["watch_rows"].items():
        watch["trajectory_moments_tested"] += candidates.bit_count()
        stage = candidates
        for index, window in enumerate(watch["windows"]):
            stage = equality_mask(
                columns, watch["state"], stage, window
            )
            watch["stage_candidate_counts"][index] += stage.bit_count()
            if not stage:
                break
        if not stage:
            continue
        exact = equality_mask(columns, watch["state"], stage)
        watch["full_state_confirmations"] += stage.bit_count()
        for lane in lane_numbers(exact):
            watch["hits"].append({
                "moment": moment,
                "key": keys[lane],
                "state_sha256": state_sha256(un_slice(columns, lane)),
            })


def recover_state(
    engine: dict[str, object],
    lane: int,
    target_t: int,
) -> State:
    checkpoint_t = max(
        moment for moment in engine["checkpoints"] if moment <= target_t
    )
    state = list(engine["checkpoints"][checkpoint_t][lane])
    key = engine["keys"][lane]
    compiled = engine["compiled_words"][key[1]]
    for _moment in range(checkpoint_t, target_t):
        advance_scalar(state, compiled)
    return bytes(state)


def resolution_window(
    engine: dict[str, object],
    lane: int,
    moment: int,
    residual_rows: tuple[tuple[str, int], ...],
) -> tuple[dict[str, object], ...]:
    comparators = {
        name: row["state"]
        for name, row in engine["watch_rows"].items()
        if name in ("funnel_weight_51", "funnel_weight_57")
    }
    rows = []
    for at in range(max(0, moment - 9), moment + 1):
        state = recover_state(engine, lane, at)
        rows.append({
            "t": at,
            "sha256": state_sha256(state),
            "component_weights": component_weights(state),
            "clean": clean_postimage(state),
            "comparator_diffs": {
                name: diff_summary(state, target)
                for name, target in comparators.items()
            },
        })
    return tuple(rows)


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
        }
        verification["pass"] = all(verification[key] for key in (
            "earlier_moments_all_nonclean",
            "landed_veto_at_moment_minus_1",
            "terminal_is_clean",
            "direct_clean_agreement",
        ))
        period = None
    elif outcome == "CYCLE":
        verification = {
            "method":
                "EXACT_RETURN_TO_T0_TESTED_AT_EVERY_INTEGER_MOMENT",
            "exact_recurrence_to_initial":
                state == bytes(engine["initial_states"][lane]),
            "earlier_returns_checked": moment - 1,
            "every_earlier_return_rejected":
                inequality_counts[lane] == moment - 1,
            "minimal_period":
                inequality_counts[lane] == moment - 1,
            "all_cycle_phases_nonclean":
                nonclean_counts[lane] == moment,
            "terminal_direct_nonclean": not clean_postimage(state),
            "reversibility_basis":
                "landed update is distinct-wire X/CNOT/TOF only",
        }
        verification["pass"] = all(verification[key] for key in (
            "exact_recurrence_to_initial",
            "every_earlier_return_rejected",
            "minimal_period",
            "all_cycle_phases_nonclean",
            "terminal_direct_nonclean",
        ))
        period = moment
    else:
        raise AssertionError(("unknown outcome", outcome))
    row = {
        "key": key,
        "outcome": outcome,
        "resolution_moment": moment,
        "first_clean_t": moment if outcome == "TRANSIENT" else None,
        "cycle_entry_t": 0 if outcome == "CYCLE" else None,
        "minimal_state_period": period,
        "terminal_state_sha256": state_sha256(state),
        "terminal_component_weights": component_weights(state),
        "landed_support_at_terminal":
            support_at_lane(engine["columns"], lane, residual_rows),
        "preterminal_window":
            resolution_window(engine, lane, moment, residual_rows),
        "verification": verification,
    }
    engine["records"][key] = row
    engine["resolution_states"][key] = state


def boundary_snapshot(
    engine: dict[str, object],
    horizon: int,
    residual_rows: tuple[tuple[str, int], ...],
) -> dict[str, object]:
    active_mask = int(engine["active_mask"])
    lanes = lane_numbers(active_mask)
    columns = engine["columns"]
    keys = engine["keys"]
    current_nonclean = nonclean_mask(columns, residual_rows)
    recurrence = equality_mask(
        columns, engine["initial_columns"], active_mask
    )
    rows = tuple({
        "key": keys[lane],
        "state_sha256": state_sha256(un_slice(columns, lane)),
        "support_weight":
            len(support_at_lane(columns, lane, residual_rows)),
        "compiled_nonclean":
            bool(current_nonclean & (1 << lane)),
        "direct_nonclean": not clean_postimage(un_slice(columns, lane)),
    } for lane in lanes)
    result = {
        "horizon": horizon,
        "open_count": len(lanes),
        "resolved_count": len(engine["records"]),
        "open_keys": tuple(keys[lane] for lane in lanes),
        "state_rows": rows,
        "state_rows_sha256": digest(rows),
        "support_weight_census": dict(sorted(Counter(
            row["support_weight"] for row in rows
        ).items())),
        "population_accounting":
            len(lanes) + len(engine["records"]) == len(keys),
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
    result["pass"] = all(result[key] for key in (
        "population_accounting",
        "all_open_landed_nonclean",
        "all_open_direct_nonclean",
        "compiled_direct_cleanliness_agreement",
        "no_open_state_equals_t0",
        "all_prior_cleanliness_tests_certified",
        "all_prior_cycle_returns_excluded",
    ))
    return result


def evolve(
    engine: dict[str, object],
    stop: int,
    residual_rows: tuple[tuple[str, int], ...],
    boundaries: tuple[int, ...] = (),
    stop_when_resolved: bool = True,
) -> dict[str, object]:
    start = int(engine["last_t"])
    started = monotonic()
    start_mask = int(engine["active_mask"])
    logical_transitions = 0
    resolved_keys = []
    ended_reason = "SEARCH_CEILING_REACHED"
    for moment in range(start + 1, stop + 1):
        active_before = int(engine["active_mask"])
        if not active_before and stop_when_resolved:
            ended_reason = "ALL_KEYS_RESOLVED"
            break
        for lane in lane_numbers(active_before):
            engine["transition_counts"][lane] += 1
        logical_transitions += active_before.bit_count()
        advance(engine["columns"], engine["schedule"])
        current_nonclean = nonclean_mask(
            engine["columns"], residual_rows
        )
        update_watches(engine, moment, active_before)
        clean_hits = active_before & ~current_nonclean
        recurrence_hits = equality_mask(
            engine["columns"],
            engine["initial_columns"],
            active_before & ~clean_hits,
        )
        for lane in lane_numbers(clean_hits):
            record_resolution(
                engine, lane, "TRANSIENT", moment,
                current_nonclean, residual_rows,
            )
            resolved_keys.append(engine["keys"][lane])
        for lane in lane_numbers(recurrence_hits):
            record_resolution(
                engine, lane, "CYCLE", moment,
                current_nonclean, residual_rows,
            )
            resolved_keys.append(engine["keys"][lane])
        engine["active_mask"] = (
            active_before & ~(clean_hits | recurrence_hits)
        )
        for lane in lane_numbers(int(engine["active_mask"])):
            engine["nonclean_prefix_counts"][lane] += int(
                bool(current_nonclean & (1 << lane))
            )
            engine["initial_inequality_counts"][lane] += 1
        engine["previous_nonclean"] = current_nonclean
        if moment % CHECKPOINT_INTERVAL == 0:
            engine["checkpoints"][moment] = tuple(
                un_slice(engine["columns"], lane)
                for lane in range(len(engine["keys"]))
            )
        engine["last_t"] = moment
        if moment in boundaries:
            engine["boundary_snapshots"][moment] = boundary_snapshot(
                engine, moment, residual_rows
            )
        if not engine["active_mask"] and stop_when_resolved:
            ended_reason = "ALL_KEYS_RESOLVED"
            break
    end = int(engine["last_t"])
    if end == stop and engine["active_mask"]:
        ended_reason = "SEARCH_CEILING_REACHED"
    upper = start_mask.bit_count() * (end - start)
    savings = sum(
        end - int(engine["records"][key]["resolution_moment"])
        for key in resolved_keys
    )
    return {
        "start_horizon": start,
        "search_ceiling": stop,
        "end_horizon": end,
        "end_reason": ended_reason,
        "active_keys_before": start_mask.bit_count(),
        "active_keys_after": int(engine["active_mask"]).bit_count(),
        "resolutions_in_phase": len(resolved_keys),
        "resolved_keys": tuple(resolved_keys),
        "logical_transitions_executed": logical_transitions,
        "logical_transition_upper_if_no_terminals": upper,
        "logical_transitions_saved_by_terminals": upper - logical_transitions,
        "expected_savings_from_resolution_moments": savings,
        "transition_accounting_exact":
            upper - logical_transitions == savings,
        "physical_global_updates": end - start,
        "complete": (
            end == stop or (
                not engine["active_mask"]
                and ended_reason == "ALL_KEYS_RESOLVED"
            )
        ),
        "seconds": round(monotonic() - started, 6),
    }


def benchmark(engine: dict[str, object]) -> dict[str, object]:
    columns = engine["columns"].copy()
    started = monotonic()
    for _tick in range(PILOT_TICKS):
        advance(columns, engine["schedule"])
    seconds = monotonic() - started
    return {
        "ticks": PILOT_TICKS,
        "schedule_instructions_per_tick": len(engine["schedule"]),
        "seconds": round(seconds, 6),
        "seconds_per_tick": seconds / PILOT_TICKS,
        "result_sha256": digest(tuple(columns)),
    }


def select_k3_horizon(
    k3_pilot: dict[str, object],
    k2_pilot: dict[str, object],
    script_started: float,
) -> tuple[int, dict[str, object]]:
    elapsed = monotonic() - script_started
    rows = tuple({
        "k3_horizon": candidate,
        "k2_search_ceiling": K2_TARGET_HORIZON,
        "projected_total_seconds": round(
            elapsed + SAFETY_FACTOR * (
                float(k3_pilot["seconds_per_tick"]) * candidate
                + float(k2_pilot["seconds_per_tick"]) * K2_TARGET_HORIZON
            ) + RESERVE_SECONDS,
            6,
        ),
        "fits_execution_budget": (
            elapsed + SAFETY_FACTOR * (
                float(k3_pilot["seconds_per_tick"]) * candidate
                + float(k2_pilot["seconds_per_tick"]) * K2_TARGET_HORIZON
            ) + RESERVE_SECONDS
            < EXECUTION_BUDGET_SEC
        ),
    } for candidate in K3_TARGET_CHOICES)
    selected = next(
        (
            int(row["k3_horizon"])
            for row in rows if row["fits_execution_budget"]
        ),
        K3_TARGET_CHOICES[-1],
    )
    return selected, {
        "policy":
            "deepest complete power-of-two k3 candidate whose measured "
            "k3 plus worst-case T=2097152 k2 schedule cost, multiplied by "
            "1.16 with 105 seconds reserve, fits 1450 seconds",
        "k3_pilot": k3_pilot,
        "k2_pilot": k2_pilot,
        "elapsed_before_selection": round(elapsed, 6),
        "candidate_rows": rows,
        "selected_k3_horizon": selected,
        "never_partial": True,
    }


def main() -> int:
    print(compact({
        "cycle": 844,
        "status": "INCREMENTAL_SCAFFOLD",
        "terminal": "CYCLE844_STANDING_BETS_HONEST_FAIL",
    }))
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
