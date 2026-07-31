#!/usr/bin/env python3
"""Independent adversarial check of the Cycle-836 deep null and S0' watch.

Cycle 833 and Cycle 836 are SHA-pinned text/AST controls only and are
blocklisted from import.  The landed Cycle-719 controller core supplies the
gate definitions; family construction, evolution, event tests, and accounting
are reimplemented here.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle833_funnel_family_2026_07_28.py",
    "scripts/frontier_cycle836_offbackbone_depth_2026_07_28.py",
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

CORE_PATH = AUDIT_INPUT_PATHS[0]
TEXT_AST_ONLY_PATHS = AUDIT_INPUT_PATHS[1:]
BLOCKLISTED_MODULES = tuple(Path(path).stem for path in TEXT_AST_ONLY_PATHS)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "bd08f5f503e532c724e6ae28915ba2f0b4202360bbe01458924d689e27c79174",
    AUDIT_INPUT_PATHS[2]:
        "b5f59ed04984d8c1956ff82a1f9af165b35ac2dcac99db4b929dbe3d8dc2e0b5",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    AUDIT_INPUT_PATHS[1]: "b3512e0c3e8acdec7bc3f1cfb4e5bf1a236f8fda",
    AUDIT_INPUT_PATHS[2]: "8e4cb3071ac2be62b1de91c900d30d493675b87d",
}


class _PrimaryFirewall(importlib.abc.MetaPathFinder):
    """Fail closed if either text/AST-only primary is imported."""

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


Key = tuple[int, tuple[int, int]]
State = tuple[int, ...]
MaskedGate = tuple[int, int, int, int, int]

RING_STATIONS = 11
FIXTURE_BANKS = 2
STATE_BITS = 5815
BASELINE_HORIZON = 65536
TARGET_HORIZON = 131072
EXPECTED_OPEN_COUNT = 133
EXPECTED_S0_PRIME_SHA256 = (
    "d874aeeb1d4e5ca29b806886314c796ac32e6658b21f888d8e2aa01044905c12"
)
EXPECTED_S0_PRIME_WEIGHT = 47
S0_SOURCE_KEY: Key = (1, (1, 6))
S0_SOURCE_MOMENT = 51110
DECLARED_PAIRS = ((0, 2), (0, 3), (0, 4))
DECLARED_KEYS: tuple[Key, ...] = tuple(
    (event, pair) for event in range(4) for pair in DECLARED_PAIRS
)


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def state_sha256(state: State) -> str:
    return sha256(bytes(state)).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(
        f"blob {len(payload)}\0".encode("ascii") + payload
    ).hexdigest()


def literal_assignment(tree: ast.Module, name: str) -> object | None:
    values: list[ast.expr] = []
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
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


def function_node(tree: ast.Module, name: str) -> ast.FunctionDef | None:
    matches = [
        node for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    return matches[0] if len(matches) == 1 else None


def named_assignment(
    function: ast.FunctionDef,
    name: str,
) -> ast.expr | None:
    matches = [
        node.value for node in ast.walk(function)
        if isinstance(node, ast.Assign)
        and len(node.targets) == 1
        and isinstance(node.targets[0], ast.Name)
        and node.targets[0].id == name
    ]
    return matches[0] if len(matches) == 1 else None


def is_name(node: ast.AST, name: str) -> bool:
    return isinstance(node, ast.Name) and node.id == name


def is_call(
    node: ast.AST,
    name: str,
    arg_names: tuple[str, ...],
) -> bool:
    return (
        isinstance(node, ast.Call)
        and is_name(node.func, name)
        and len(node.args) == len(arg_names)
        and all(
            is_name(arg, expected)
            for arg, expected in zip(node.args, arg_names)
        )
        and not node.keywords
    )


def cycle833_definition_audit(tree: ast.Module) -> dict[str, object]:
    function = function_node(tree, "fourth_candidate_certificate")
    if function is None:
        return {"pass": False, "reason": "definition function missing"}
    current = named_assignment(function, "current")
    mask = named_assignment(function, "prediction_mask")
    candidate = named_assignment(function, "candidate")
    current_ok = (
        isinstance(current, ast.Subscript)
        and is_name(current.value, "funnels")
        and isinstance(current.slice, ast.Constant)
        and current.slice.value == 1
    )
    mask_ok = (
        isinstance(mask, ast.Tuple)
        and len(mask.elts) == 1
        and isinstance(mask.elts[0], ast.Constant)
        and mask.elts[0].value == "bank0.HEAD[1]"
    )
    candidate_ok = (
        isinstance(candidate, ast.Call)
        and is_name(candidate.func, "apply_named_xor_update")
        and len(candidate.args) == 2
        and is_name(candidate.args[0], "current")
        and is_name(candidate.args[1], "prediction_mask")
    )
    constants = {
        node.value for node in ast.walk(function)
        if isinstance(node, ast.Constant)
        and isinstance(node.value, (str, int))
    }
    result = {
        "definition_function": function.name,
        "source_is_funnels_event_1": current_ok,
        "prediction_mask_is_bank0_HEAD_1": mask_ok,
        "candidate_applies_named_XOR": candidate_ok,
        "declares_name_S0_prime": "S0'" in constants,
        "declares_weight_47": 47 in constants,
    }
    result["pass"] = all(
        value for key, value in result.items()
        if key not in {"definition_function", "pass"}
    )
    return result


def primary_window_audit(tree: ast.Module) -> dict[str, object]:
    equality = function_node(tree, "equality_to_target_mask")
    run_function = function_node(tree, "run")
    nested = {
        node.name: node for node in ast.walk(run_function)
        if isinstance(node, ast.FunctionDef)
    } if run_function is not None else {}
    scan = nested.get("scan_s0_prime")
    evolve = nested.get("evolve_phase")
    if equality is None or run_function is None or scan is None or evolve is None:
        return {
            "pass": False,
            "reason": "required primary watch function missing",
        }

    wires_default_none = (
        equality.args.args[-1].arg == "wires"
        and len(equality.args.defaults) >= 1
        and isinstance(equality.args.defaults[-1], ast.Constant)
        and equality.args.defaults[-1].value is None
    )
    selected = named_assignment(equality, "selected")
    full_range_if_omitted = (
        isinstance(selected, ast.IfExp)
        and isinstance(selected.test, ast.Compare)
        and is_name(selected.test.left, "wires")
        and len(selected.test.ops) == 1
        and isinstance(selected.test.ops[0], ast.Is)
        and len(selected.test.comparators) == 1
        and isinstance(selected.test.comparators[0], ast.Constant)
        and selected.test.comparators[0].value is None
        and isinstance(selected.body, ast.Call)
        and is_name(selected.body.func, "range")
        and len(selected.body.args) == 1
        and isinstance(selected.body.args[0], ast.Call)
        and is_name(selected.body.args[0].func, "len")
        and len(selected.body.args[0].args) == 1
        and is_name(selected.body.args[0].args[0], "columns")
        and is_name(selected.orelse, "wires")
    )
    monotone_narrow = any(
        isinstance(node, ast.AugAssign)
        and is_name(node.target, "matches")
        and isinstance(node.op, ast.BitAnd)
        for node in ast.walk(equality)
    )
    returns_matches = any(
        isinstance(node, ast.Return) and is_name(node.value, "matches")
        for node in equality.body
    )

    window = named_assignment(scan, "window_matches")
    full = named_assignment(scan, "full_matches")
    selected_window_call = is_call(
        window,
        "equality_to_target_mask",
        ("columns", "s0_prime", "primary_mask", "s0_window_wires"),
    )
    full_compare_call = (
        isinstance(full, ast.IfExp)
        and is_name(full.test, "window_matches")
        and is_call(
            full.body,
            "equality_to_target_mask",
            ("columns", "s0_prime", "window_matches"),
        )
        and isinstance(full.orelse, ast.Constant)
        and full.orelse.value == 0
    )
    survivor_unpacked = any(
        isinstance(node, ast.Call)
        and is_name(node.func, "un_slice")
        and len(node.args) == 2
        and is_name(node.args[0], "columns")
        and is_name(node.args[1], "lane")
        for node in ast.walk(scan)
    )
    survivor_hashed = any(
        isinstance(node, ast.Call)
        and is_name(node.func, "state_sha256")
        and len(node.args) == 1
        and is_name(node.args[0], "state")
        for node in ast.walk(scan)
    )
    zero_scan = any(
        isinstance(node, ast.Call)
        and is_name(node.func, "scan_s0_prime")
        and len(node.args) == 1
        and isinstance(node.args[0], ast.Constant)
        and node.args[0].value == 0
        for node in ast.walk(run_function)
    )
    per_moment_scan = any(
        isinstance(node, ast.Call)
        and is_name(node.func, "scan_s0_prime")
        and len(node.args) == 1
        and is_name(node.args[0], "moment")
        for node in ast.walk(evolve)
    )
    phase_calls = {
        tuple(ast.unparse(arg) for arg in node.args)
        for node in ast.walk(run_function)
        if isinstance(node, ast.Call)
        and is_name(node.func, "evolve_phase")
    }
    phases_cover_without_gap = {
        ("0", "BASELINE_HORIZON"),
        ("BASELINE_HORIZON", "TARGET_HORIZON"),
    } <= phase_calls
    inclusive_loop = any(
        isinstance(node, ast.For)
        and isinstance(node.iter, ast.Call)
        and is_name(node.iter.func, "range")
        and tuple(ast.unparse(arg) for arg in node.iter.args)
        == ("start + 1", "stop + 1")
        for node in ast.walk(evolve)
    )
    result = {
        "wires_default_to_none": wires_default_none,
        "omitted_wires_select_all_columns": full_range_if_omitted,
        "comparison_monotonically_narrows_lane_mask": monotone_narrow,
        "comparison_returns_narrowed_mask": returns_matches,
        "selected_wire_window_call": selected_window_call,
        "survivors_receive_full_5815_bit_call": full_compare_call,
        "full_survivors_are_unpacked": survivor_unpacked,
        "full_survivors_are_SHA256_hashed": survivor_hashed,
        "moment_zero_scanned": zero_scan,
        "each_evolved_moment_scanned": per_moment_scan,
        "inclusive_evolution_loop": inclusive_loop,
        "two_phases_cover_1_through_131072_without_gap":
            phases_cover_without_gap,
        "soundness_argument":
            "Full equality implies equality on every selected wire; the "
            "first call only intersects the candidate mask, and the second "
            "call omits wires so it compares range(len(columns)).",
    }
    result["pass"] = all(
        value for key, value in result.items()
        if key not in {"soundness_argument", "pass"}
    )
    return result


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
        Path(__file__).read_text(encoding="utf-8"),
        filename=Path(__file__).name,
    )
    sha_rows = {
        path: sha256(payload).hexdigest()
        for path, payload in payloads.items()
    }
    blob_rows = {
        path: git_blob(payload) for path, payload in payloads.items()
    }
    direct_frontier_imports = tuple(sorted(
        alias.name
        for node in self_tree.body
        if isinstance(node, ast.Import)
        for alias in node.names
        if alias.name.startswith("frontier_cycle")
    ))
    primary_tree = trees.get(AUDIT_INPUT_PATHS[2])
    cycle833_tree = trees.get(AUDIT_INPUT_PATHS[1])
    primary_literals = {
        name: literal_assignment(primary_tree, name)
        if primary_tree is not None else None
        for name in (
            "BASELINE_HORIZON",
            "TARGET_HORIZON",
            "EXPECTED_BASELINE_OPEN_COUNT",
            "EXPECTED_S0_PRIME_SHA256",
            "EXPECTED_S0_PRIME_WEIGHT",
            "BASELINE_RESOLVED_ROWS",
        )
    }
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_INPUT_PATHS_literal":
            literal_assignment(self_tree, "AUDIT_INPUT_PATHS")
            == AUDIT_INPUT_PATHS,
        "existing_worktree_relative": (
            len(payloads) == len(AUDIT_INPUT_PATHS)
            and all(
                not Path(path).is_absolute() and (ROOT / path).is_file()
                for path in AUDIT_INPUT_PATHS
            )
        ),
        "plain_reading_named_files": len(AUDIT_INPUT_PATHS),
        "maximum_named_files": 6,
        "sha256": sha_rows,
        "expected_sha256": EXPECTED_SHA256,
        "git_blobs": blob_rows,
        "expected_git_blobs": EXPECTED_GIT_BLOBS,
        "text_AST_only_paths": TEXT_AST_ONLY_PATHS,
        "blocked_modules": BLOCKLISTED_MODULES,
        "blocked_modules_loaded": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits": tuple(FIREWALL.hits),
        "direct_frontier_imports": direct_frontier_imports,
        "cycle833_S0_prime_definition":
            cycle833_definition_audit(cycle833_tree)
            if cycle833_tree is not None else {"pass": False},
        "cycle836_windowing": primary_window_audit(primary_tree)
            if primary_tree is not None else {"pass": False},
        "cycle836_literals": primary_literals,
    }
    result["pass"] = (
        result["AUDIT_INPUT_PATHS_literal"]
        and result["existing_worktree_relative"]
        and len(AUDIT_INPUT_PATHS) <= 6
        and sha_rows == EXPECTED_SHA256
        and blob_rows == EXPECTED_GIT_BLOBS
        and direct_frontier_imports == (
            "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26",
        )
        and not result["blocked_modules_loaded"]
        and not result["firewall_hits"]
        and result["cycle833_S0_prime_definition"]["pass"]
        and result["cycle836_windowing"]["pass"]
        and primary_literals["BASELINE_HORIZON"] == BASELINE_HORIZON
        and primary_literals["TARGET_HORIZON"] == TARGET_HORIZON
        and primary_literals["EXPECTED_BASELINE_OPEN_COUNT"]
        == EXPECTED_OPEN_COUNT
        and primary_literals["EXPECTED_S0_PRIME_SHA256"]
        == EXPECTED_S0_PRIME_SHA256
        and primary_literals["EXPECTED_S0_PRIME_WEIGHT"]
        == EXPECTED_S0_PRIME_WEIGHT
    )
    return result


def separated_pairs() -> tuple[tuple[int, int], ...]:
    return tuple(
        pair for pair in combinations(range(RING_STATIONS), 2)
        if min(
            (pair[1] - pair[0]) % RING_STATIONS,
            (pair[0] - pair[1]) % RING_STATIONS,
        ) > 1
    )


def synchronous_word(
    program: tuple[object, ...],
    positions0: tuple[int, int],
) -> tuple[object, ...]:
    positions = positions0
    word: list[object] = []
    for _step in range(len(program)):
        live = set(positions)
        for station, row in enumerate(program):
            if station in live:
                word.extend(K.mapped_macro(row))
        positions = tuple(
            (position + 1) % len(program) for position in positions
        )
    return tuple(word)


def build_epoch_states() -> tuple[
    tuple[object, ...],
    dict[int, State],
    dict[str, object],
]:
    program = K.interleaved_program(FIXTURE_BANKS)
    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    state = K.M.pack_state(banks, links)
    allocator = K.M.global_allocator_word(FIXTURE_BANKS)
    epochs: dict[int, State] = {}
    rows = []
    for event in range(2 * FIXTURE_BANKS):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = K.M.prepare_endpoint(state, direction)
        after, rail_a, rail_b, trace = K.run_orbit(before, program)
        row = {
            "event": event,
            "allocator_exact":
                after == K.A.apply_semantic(before, allocator),
            "rail_a_exact":
                rail_a == (1,) + (0,) * (len(program) - 1),
            "rail_b_clear": not any(rail_b),
            "trace_complete": len(trace) == len(program),
        }
        row["pass"] = all(
            value for key, value in row.items()
            if key not in {"event", "pass"}
        )
        rows.append(row)
        epochs[event] = before
        state = after
    certificate = {
        "program_stations": len(program),
        "events": len(epochs),
        "rows": tuple(rows),
    }
    certificate["pass"] = (
        len(program) == RING_STATIONS
        and len(epochs) == 4
        and all(row["pass"] for row in rows)
    )
    return program, epochs, certificate


def build_initial_states(
    program: tuple[object, ...],
    epochs: dict[int, State],
    keys: tuple[Key, ...],
) -> tuple[dict[Key, State], dict[tuple[int, int], tuple[object, ...]], dict[str, object]]:
    words = {
        pair: synchronous_word(program, pair)
        for pair in sorted({key[1] for key in keys})
    }
    states: dict[Key, State] = {}
    rows = []
    for key in keys:
        event, pair = key
        state, rail_a, rail_b, trace = K.run_orbit(
            epochs[event], program, token_positions=pair
        )
        expected_rail = tuple(
            int(station in pair) for station in range(RING_STATIONS)
        )
        row = {
            "key": key,
            "semantic_exact":
                state == K.A.apply_semantic(epochs[event], words[pair]),
            "rail_a_exact": rail_a == expected_rail,
            "rail_b_clear": not any(rail_b),
            "trace_complete": len(trace) == len(program),
            "state_bits": len(state),
        }
        row["pass"] = (
            row["semantic_exact"]
            and row["rail_a_exact"]
            and row["rail_b_clear"]
            and row["trace_complete"]
            and row["state_bits"] == STATE_BITS
        )
        rows.append(row)
        states[key] = state
    certificate = {
        "keys": keys,
        "word_gate_counts": tuple(sorted({
            len(word) for word in words.values()
        })),
        "rows": tuple(rows),
    }
    certificate["pass"] = (
        len(states) == len(keys)
        and all(row["pass"] for row in rows)
    )
    return states, words, certificate


def bit_slice(states: tuple[State, ...]) -> list[int]:
    return [
        sum(state[wire] << lane for lane, state in enumerate(states))
        for wire in range(len(states[0]))
    ]


def un_slice(columns: list[int], lane: int) -> State:
    return tuple((column >> lane) & 1 for column in columns)


def lane_numbers(mask: int) -> tuple[int, ...]:
    rows = []
    while mask:
        bit = mask & -mask
        rows.append(bit.bit_length() - 1)
        mask ^= bit
    return tuple(rows)


def independent_schedule(
    program: tuple[object, ...],
    keys: tuple[Key, ...],
) -> tuple[MaskedGate, ...]:
    """Compile a gate schedule without calling either source primary."""
    schedule: list[MaskedGate] = []
    for step in range(len(program)):
        for station, program_row in enumerate(program):
            mask = 0
            for lane, key in enumerate(keys):
                left, right = key[1]
                if station in (
                    (left + step) % len(program),
                    (right + step) % len(program),
                ):
                    mask |= 1 << lane
            if not mask:
                continue
            for gate in K.mapped_macro(program_row):
                if len(set(gate.wires)) != len(gate.wires):
                    raise AssertionError(("repeated landed gate wire", gate))
                if gate.kind == "X":
                    schedule.append((0, gate.wires[0], 0, 0, mask))
                elif gate.kind == "CNOT":
                    schedule.append(
                        (1, gate.wires[0], gate.wires[1], 0, mask)
                    )
                elif gate.kind == "TOF":
                    schedule.append((
                        2, gate.wires[0], gate.wires[1],
                        gate.wires[2], mask,
                    ))
                else:
                    raise AssertionError(("non-reversible landed gate", gate))
    return tuple(schedule)


def advance(columns: list[int], schedule: tuple[MaskedGate, ...]) -> None:
    for kind, first, second, third, mask in schedule:
        if kind == 0:
            columns[first] ^= mask
        elif kind == 1:
            columns[second] ^= columns[first] & mask
        else:
            columns[third] ^= columns[first] & columns[second] & mask


def equality_to_initial_mask(
    columns: list[int],
    initial_columns: list[int],
    candidates: int,
    wires: tuple[int, ...],
) -> int:
    matches = candidates
    for wire in wires:
        matches &= candidates ^ (
            (columns[wire] ^ initial_columns[wire]) & candidates
        )
        if not matches:
            return 0
    return matches


def equality_to_state_mask(
    columns: list[int],
    target: State,
    candidates: int,
    wires: tuple[int, ...],
) -> int:
    matches = candidates
    for wire in wires:
        matches &= (
            columns[wire]
            if target[wire]
            else candidates ^ (columns[wire] & candidates)
        )
        if not matches:
            return 0
    return matches


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
    rows = [("source.SOURCE_POINTER", K.R3.X.SOURCE_POINTER)]
    for bank_index, base in enumerate(
        K.M.R12.BANK_BASES[:FIXTURE_BANKS]
    ):
        rows.extend(
            (f"bank{bank_index}.{name}", base + wire)
            for name, wire in bank_named
        )
    for link_index, base in enumerate(
        K.M.R12.LINK_BASES[:FIXTURE_BANKS - 1]
    ):
        rows.extend(
            (f"link{link_index}.WIRE_{wire}", base + wire)
            for wire in range(K.B.LINK_WIDTH)
        )
    return tuple(rows)


def nonclean_mask(
    columns: list[int],
    residual_rows: tuple[tuple[str, int], ...],
) -> int:
    result = 0
    for _name, wire in residual_rows:
        result |= columns[wire]
    return result


def reconstruct_s0_prime(
    program: tuple[object, ...],
    epochs: dict[int, State],
) -> tuple[State, dict[str, object]]:
    states, words, build = build_initial_states(
        program, epochs, (S0_SOURCE_KEY,)
    )
    initial = states[S0_SOURCE_KEY]
    columns = bit_slice((initial,))
    schedule = independent_schedule(program, (S0_SOURCE_KEY,))
    one_step = columns.copy()
    advance(one_step, schedule)
    one_step_exact = (
        un_slice(one_step, 0)
        == K.A.apply_semantic(initial, words[S0_SOURCE_KEY[1]])
    )
    for _moment in range(S0_SOURCE_MOMENT):
        advance(columns, schedule)
    source = un_slice(columns, 0)
    candidate = list(source)
    target_wire = K.M.R12.BANK_BASES[0] + K.A.HEAD[1]
    candidate[target_wire] ^= 1
    s0_prime = tuple(candidate)
    certificate = {
        "source_primary": AUDIT_INPUT_PATHS[1],
        "source_primary_sha256": EXPECTED_SHA256[AUDIT_INPUT_PATHS[1]],
        "definition":
            "Cycle-833 S1 at t=51110 for key (1,(1,6)), XOR "
            "bank0.HEAD[1]",
        "source_build": build,
        "source_key": S0_SOURCE_KEY,
        "source_moment": S0_SOURCE_MOMENT,
        "schedule_instructions": len(schedule),
        "one_step_scalar_equivalence": one_step_exact,
        "source_weight": sum(source),
        "candidate_weight": sum(s0_prime),
        "candidate_sha256": state_sha256(s0_prime),
        "expected_candidate_sha256": EXPECTED_S0_PRIME_SHA256,
        "target_wire": target_wire,
    }
    certificate["pass"] = (
        build["pass"]
        and one_step_exact
        and certificate["source_weight"] == 46
        and certificate["candidate_weight"] == EXPECTED_S0_PRIME_WEIGHT
        and certificate["candidate_sha256"] == EXPECTED_S0_PRIME_SHA256
    )
    return s0_prime, certificate


def render(
    checks: dict[str, bool],
    certificates: dict[str, dict[str, object]],
    report: dict[str, object],
) -> str:
    lines = [
        f"{'PASS' if passed else 'FAIL'} {name}"
        for name, passed in checks.items()
    ]
    lines.extend(
        f"FINDING {name}: {certificate['finding']}"
        for name, certificate in certificates.items()
    )
    lines.extend(
        f"CERTIFICATE {name} {compact(certificate)}"
        for name, certificate in certificates.items()
    )
    lines.append("SUMMARY_JSON " + compact(report))
    lines.append(str(report["terminal"]))
    return "\n".join(lines) + "\n"


def stable_output(
    checks: dict[str, bool],
    certificates: dict[str, dict[str, object]],
    report: dict[str, object],
    controls_base: bool,
) -> str:
    for _attempt in range(20):
        controls = certificates["CONTROLS"]
        report["checks"] = dict(checks)
        report["pass"] = all(checks.values())
        report["terminal"] = (
            "CYCLE836_DEPTH_INDEPENDENT_CHECK_PASS"
            if report["pass"]
            else "CYCLE836_DEPTH_INDEPENDENT_CHECK_HONEST_FAIL"
        )
        output = render(checks, certificates, report)
        size = len(output.encode("utf-8"))
        stdout_ok = size < STDOUT_LIMIT_BYTES
        new_controls_pass = controls_base and stdout_ok
        stable = (
            controls["stdout_bytes"] == size
            and controls["stdout_below_limit"] == stdout_ok
            and checks["CONTROLS"] == new_controls_pass
        )
        controls["stdout_bytes"] = size
        controls["stdout_below_limit"] = stdout_ok
        controls["pass"] = new_controls_pass
        checks["CONTROLS"] = new_controls_pass
        controls["finding"] = (
            "All SHA/blob pins, literal input paths, primary import "
            "firewalls, declared-slice determinism, runtime, and stdout "
            "bounds passed."
            if new_controls_pass else
            "Control failure: inspect SHA/blob pins, AST-only firewall, "
            "determinism, runtime, or stdout fields."
        )
        if stable:
            return output
    raise AssertionError("stdout byte fixed point did not converge")


def run() -> int:
    started = monotonic()
    sources = source_controls()
    program, epochs, epoch_build = build_epoch_states()
    s0_prime, s0_build = reconstruct_s0_prime(program, epochs)
    initial_states, words, initial_build = build_initial_states(
        program, epochs, DECLARED_KEYS
    )

    primary_literals = sources["cycle836_literals"]
    baseline_rows = primary_literals["BASELINE_RESOLVED_ROWS"]
    resolved_keys = {
        row[0] for row in baseline_rows
    } if isinstance(baseline_rows, tuple) else set()
    catalog = {
        (event, pair)
        for event in range(4)
        for pair in separated_pairs()
    }
    declared_open = (
        len(DECLARED_KEYS) == 12
        and len(set(DECLARED_KEYS)) == len(DECLARED_KEYS)
        and all(key in catalog and key not in resolved_keys
                for key in DECLARED_KEYS)
    )
    declared_offbackbone = all(
        0 in key[1] for key in DECLARED_KEYS
    )
    primary_population_exact = (
        len(catalog) == 176
        and len(resolved_keys) == 43
        and len(catalog - resolved_keys) == EXPECTED_OPEN_COUNT
    )

    duplicate_key = DECLARED_KEYS[0]
    lane_keys = DECLARED_KEYS + (duplicate_key,)
    lane_states = tuple(initial_states[key] for key in lane_keys)
    columns = bit_slice(lane_states)
    initial_columns = columns.copy()
    schedule = independent_schedule(program, lane_keys)
    primary_mask = (1 << len(DECLARED_KEYS)) - 1
    duplicate_lane = len(DECLARED_KEYS)
    duplicate_masks_identical = all(
        ((mask >> 0) & 1) == ((mask >> duplicate_lane) & 1)
        for _kind, _first, _second, _third, mask in schedule
    )
    one_step = columns.copy()
    advance(one_step, schedule)
    one_step_exact = all(
        un_slice(one_step, lane)
        == K.A.apply_semantic(
            initial_states[key], words[key[1]]
        )
        for lane, key in enumerate(lane_keys)
    )

    residual_rows = watched_residual_rows()
    recurrence_window_wires = tuple(sorted(
        {wire for _name, wire in residual_rows}
        | {
            index * (STATE_BITS - 1) // 127
            for index in range(128)
        }
    ))
    all_wires = tuple(range(STATE_BITS))
    s0_active_wires = tuple(
        wire for wire, bit in enumerate(s0_prime) if bit
    )

    nonclean_counts = [0] * len(DECLARED_KEYS)
    inequality_counts = [0] * len(DECLARED_KEYS)
    clean_event_count = 0
    cycle_return_count = 0
    clean_examples: list[dict[str, object]] = []
    cycle_examples: list[dict[str, object]] = []
    recurrence_window_survivors = 0
    s0_trajectory_moments = 0
    s0_window_survivors = 0
    s0_full_hit_count = 0
    s0_hit_examples: list[dict[str, object]] = []
    logical_transitions = 0
    boundaries: dict[int, dict[str, object]] = {}

    def record_clean(moment: int, mask: int) -> None:
        nonlocal clean_event_count
        clean_event_count += mask.bit_count()
        if len(clean_examples) < 32:
            for lane in lane_numbers(mask):
                if len(clean_examples) >= 32:
                    break
                clean_examples.append({
                    "key": DECLARED_KEYS[lane],
                    "moment": moment,
                })

    def record_cycle(moment: int, mask: int) -> None:
        nonlocal cycle_return_count
        cycle_return_count += mask.bit_count()
        if len(cycle_examples) < 32:
            for lane in lane_numbers(mask):
                if len(cycle_examples) >= 32:
                    break
                cycle_examples.append({
                    "key": DECLARED_KEYS[lane],
                    "moment": moment,
                })

    def scan_s0(moment: int) -> None:
        nonlocal s0_trajectory_moments
        nonlocal s0_window_survivors
        nonlocal s0_full_hit_count
        s0_trajectory_moments += len(DECLARED_KEYS)
        window = equality_to_state_mask(
            columns, s0_prime, primary_mask, s0_active_wires
        )
        s0_window_survivors += window.bit_count()
        full = (
            equality_to_state_mask(
                columns, s0_prime, window, all_wires
            )
            if window else 0
        )
        s0_full_hit_count += full.bit_count()
        if len(s0_hit_examples) < 32:
            for lane in lane_numbers(full):
                if len(s0_hit_examples) >= 32:
                    break
                state = un_slice(columns, lane)
                s0_hit_examples.append({
                    "key": DECLARED_KEYS[lane],
                    "moment": moment,
                    "full_5815_bit_equal": state == s0_prime,
                    "sha256": state_sha256(state),
                })

    initial_nonclean = nonclean_mask(columns, residual_rows)
    initial_clean = primary_mask & ~initial_nonclean
    record_clean(0, initial_clean)
    for lane in range(len(DECLARED_KEYS)):
        nonclean_counts[lane] += int(
            bool(initial_nonclean & (1 << lane))
        )
    scan_s0(0)

    for moment in range(1, TARGET_HORIZON + 1):
        advance(columns, schedule)
        logical_transitions += len(DECLARED_KEYS)
        scan_s0(moment)

        current_nonclean = nonclean_mask(columns, residual_rows)
        clean = primary_mask & ~current_nonclean
        record_clean(moment, clean)
        for lane in range(len(DECLARED_KEYS)):
            nonclean_counts[lane] += int(
                bool(current_nonclean & (1 << lane))
            )

        recurrence_window = equality_to_initial_mask(
            columns,
            initial_columns,
            primary_mask,
            recurrence_window_wires,
        )
        recurrence_window_survivors += recurrence_window.bit_count()
        recurrence = (
            equality_to_initial_mask(
                columns,
                initial_columns,
                recurrence_window,
                all_wires,
            )
            if recurrence_window else 0
        )
        record_cycle(moment, recurrence)
        for lane in range(len(DECLARED_KEYS)):
            inequality_counts[lane] += int(
                not bool(recurrence & (1 << lane))
            )

        if moment in (BASELINE_HORIZON, TARGET_HORIZON):
            rows = tuple({
                "key": key,
                "state_sha256": state_sha256(un_slice(columns, lane)),
                "residual_support_weight": sum(
                    (columns[wire] >> lane) & 1
                    for _name, wire in residual_rows
                ),
            } for lane, key in enumerate(DECLARED_KEYS))
            boundaries[moment] = {
                "horizon": moment,
                "rows": rows,
                "all_landed_nonclean":
                    all(row["residual_support_weight"] > 0 for row in rows),
                "determinism_duplicate_exact":
                    un_slice(columns, 0)
                    == un_slice(columns, duplicate_lane),
            }

    slice_inclusive_moments = (
        len(DECLARED_KEYS) * (TARGET_HORIZON + 1)
    )
    null_pass = (
        sources["pass"]
        and epoch_build["pass"]
        and initial_build["pass"]
        and declared_open
        and declared_offbackbone
        and primary_population_exact
        and one_step_exact
        and clean_event_count == 0
        and cycle_return_count == 0
        and all(
            count == TARGET_HORIZON + 1
            for count in nonclean_counts
        )
        and all(
            count == TARGET_HORIZON
            for count in inequality_counts
        )
        and all(
            boundary["all_landed_nonclean"]
            for boundary in boundaries.values()
        )
    )
    if clean_examples or cycle_examples:
        first_event = (
            clean_examples[0] if clean_examples else cycle_examples[0]
        )
        null_finding = (
            "REFUTATION: independent landed-event scan found "
            f"{compact(first_event)}; the claimed deep null is false."
        )
    elif null_pass:
        null_finding = (
            "Re-swept 12 declared Cycle-836-open off-backbone keys through "
            "complete T=131072; all 1,572,876 inclusive trajectory-moments "
            "were landed-nonclean and no exact return to t0 occurred."
        )
    else:
        null_finding = (
            "No resolution was observed, but a provenance, construction, "
            "coverage, or landed-test invariant failed."
        )
    null_certificate: dict[str, object] = {
        "finding": null_finding,
        "declared_keys": DECLARED_KEYS,
        "declared_key_count": len(DECLARED_KEYS),
        "declared_open_by_primary_AST": declared_open,
        "all_declared_offbackbone": declared_offbackbone,
        "primary_population_accounting": {
            "catalog": len(catalog),
            "resolved": len(resolved_keys),
            "open": len(catalog - resolved_keys),
            "pass": primary_population_exact,
        },
        "epoch_build": epoch_build,
        "initial_state_build": initial_build,
        "own_evolution": {
            "method":
                "independently compiled bit-sliced landed X/CNOT/TOF schedule",
            "schedule_instructions_per_step": len(schedule),
            "one_step_scalar_equivalence_all_lanes": one_step_exact,
            "logical_transitions_0_to_131072": logical_transitions,
        },
        "inclusive_trajectory_moments": slice_inclusive_moments,
        "landed_nonclean_counts_by_key": tuple(
            (key, nonclean_counts[lane])
            for lane, key in enumerate(DECLARED_KEYS)
        ),
        "exact_initial_inequality_counts_by_key": tuple(
            (key, inequality_counts[lane])
            for lane, key in enumerate(DECLARED_KEYS)
        ),
        "recurrence_prefilter_wire_count": len(recurrence_window_wires),
        "recurrence_prefilter_survivor_count":
            recurrence_window_survivors,
        "clean_event_count": clean_event_count,
        "clean_event_examples": tuple(clean_examples),
        "exact_return_to_t0_count": cycle_return_count,
        "cycle_return_examples": tuple(cycle_examples),
        "complete_boundaries": tuple(boundaries.values()),
        "pass": null_pass,
    }

    s0_expected_moments = (
        len(DECLARED_KEYS) * (TARGET_HORIZON + 1)
    )
    primary_window = sources["cycle836_windowing"]
    s0_pass = (
        sources["cycle833_S0_prime_definition"]["pass"]
        and sources["sha256"][AUDIT_INPUT_PATHS[1]]
        == EXPECTED_SHA256[AUDIT_INPUT_PATHS[1]]
        and s0_build["pass"]
        and len(s0_active_wires) == EXPECTED_S0_PRIME_WEIGHT
        and s0_trajectory_moments == s0_expected_moments
        and s0_full_hit_count == 0
        and primary_window["pass"]
    )
    if s0_full_hit_count:
        s0_finding = (
            "REFUTATION: independent full-state scan found S0' at "
            f"{compact(s0_hit_examples[0])}."
        )
    elif not s0_build["pass"]:
        s0_finding = (
            "REFUTATION: S0' reconstructed from the SHA-pinned Cycle-833 "
            "definition does not match the claimed weight/hash pin."
        )
    elif not primary_window["pass"]:
        s0_finding = (
            "REFUTATION: the Cycle-836 AST does not establish a sound "
            "selected-wire window followed by a full-state comparison."
        )
    else:
        s0_finding = (
            "Reconstructed weight-47 S0' with SHA-256 "
            f"{EXPECTED_S0_PRIME_SHA256} from the SHA-pinned Cycle-833 "
            "definition; zero visits occurred in 1,572,876 independently "
            "scanned trajectory-moments, and Cycle-836 windowing is sound."
        )
    s0_certificate: dict[str, object] = {
        "finding": s0_finding,
        "cycle833_definition_AST":
            sources["cycle833_S0_prime_definition"],
        "reconstruction": s0_build,
        "independent_watch": {
            "method":
                "target-one-bit necessary-condition window, then exact all-"
                "5815-bit comparison for every survivor",
            "soundness":
                "Any exact S0' equality contains every active S0' bit, so "
                "the active-bit intersection cannot reject a true hit.",
            "inclusive_bounds": (0, TARGET_HORIZON),
            "trajectory_count": len(DECLARED_KEYS),
            "trajectory_moments_tested": s0_trajectory_moments,
            "active_window_wire_count": len(s0_active_wires),
            "window_survivor_count": s0_window_survivors,
            "full_equality_hit_count": s0_full_hit_count,
            "hit_examples": tuple(s0_hit_examples),
        },
        "cycle836_primary_window_AST": primary_window,
        "pass": s0_pass,
    }

    transition_arithmetic = (
        EXPECTED_OPEN_COUNT * (TARGET_HORIZON - BASELINE_HORIZON)
    )
    trajectory_moment_arithmetic = (
        EXPECTED_OPEN_COUNT * (TARGET_HORIZON + 1)
    )
    accounting_pass = (
        transition_arithmetic == 8_716_288
        and trajectory_moment_arithmetic == 17_432_709
        and logical_transitions
        == len(DECLARED_KEYS) * TARGET_HORIZON
        and s0_trajectory_moments
        == len(DECLARED_KEYS) * (TARGET_HORIZON + 1)
        and primary_window["moment_zero_scanned"]
        and primary_window["each_evolved_moment_scanned"]
        and primary_window["inclusive_evolution_loop"]
        and primary_window[
            "two_phases_cover_1_through_131072_without_gap"
        ]
    )
    accounting_certificate: dict[str, object] = {
        "finding":
            "133 × 65,536 = 8,716,288 continuation transitions; "
            "133 × (131,072 + 1) = 17,432,709 trajectory-moments, "
            "matching the primary's inclusive two-phase scan."
            if accounting_pass else
            "REFUTATION: the primary's transition or inclusive-moment "
            "arithmetic/coverage does not close.",
        "primary_constants_from_AST": {
            "open_keys": primary_literals["EXPECTED_BASELINE_OPEN_COUNT"],
            "baseline_horizon": primary_literals["BASELINE_HORIZON"],
            "target_horizon": primary_literals["TARGET_HORIZON"],
        },
        "continuation_formula": "133 * (131072 - 65536)",
        "continuation_transitions": transition_arithmetic,
        "trajectory_moment_formula": "133 * (131072 + 1)",
        "trajectory_moments": trajectory_moment_arithmetic,
        "primary_scan_coverage_AST": {
            key: primary_window[key] for key in (
                "moment_zero_scanned",
                "each_evolved_moment_scanned",
                "inclusive_evolution_loop",
                "two_phases_cover_1_through_131072_without_gap",
            )
        },
        "independent_slice_accounting": {
            "transitions_observed": logical_transitions,
            "transitions_expected":
                len(DECLARED_KEYS) * TARGET_HORIZON,
            "inclusive_trajectory_moments_observed":
                s0_trajectory_moments,
            "inclusive_trajectory_moments_expected":
                len(DECLARED_KEYS) * (TARGET_HORIZON + 1),
        },
        "pass": accounting_pass,
    }

    deterministic = (
        lane_states[0] == lane_states[duplicate_lane]
        and duplicate_masks_identical
        and one_step_exact
        and len(boundaries) == 2
        and all(
            boundary["determinism_duplicate_exact"]
            for boundary in boundaries.values()
        )
    )
    elapsed = monotonic() - started
    blocked_at_end = tuple(
        name for name in BLOCKLISTED_MODULES if name in sys.modules
    )
    controls_base = (
        sources["pass"]
        and deterministic
        and not blocked_at_end
        and not FIREWALL.hits
        and elapsed < AUDIT_TIMEOUT_SEC
    )
    controls_certificate: dict[str, object] = {
        "finding": "",
        "source_controls": sources,
        "blocklisted_modules_loaded_at_end": blocked_at_end,
        "firewall_hits_at_end": tuple(FIREWALL.hits),
        "determinism": {
            "declared_slice_key": duplicate_key,
            "initial_exact":
                lane_states[0] == lane_states[duplicate_lane],
            "identical_schedule_masks": duplicate_masks_identical,
            "one_step_scalar_equivalence": one_step_exact,
            "boundary_exact": tuple(
                (horizon, boundary["determinism_duplicate_exact"])
                for horizon, boundary in boundaries.items()
            ),
            "pass": deterministic,
        },
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "runtime_below_limit": elapsed < AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "stdout_below_limit": True,
        "pass": controls_base,
    }

    checks = {
        "NULL SPOT-COVERAGE": null_pass,
        "THE S0' WATCH": s0_pass,
        "ACCOUNTING": accounting_pass,
        "CONTROLS": controls_base,
    }
    certificates = {
        "NULL SPOT-COVERAGE": null_certificate,
        "THE S0' WATCH": s0_certificate,
        "ACCOUNTING": accounting_certificate,
        "CONTROLS": controls_certificate,
    }
    report = {
        "cycle": 836,
        "checker": "independent_adversarial",
        "declared_key_count": len(DECLARED_KEYS),
        "horizon_reached": TARGET_HORIZON,
        "horizon_complete": True,
        "resolution_event_count":
            clean_event_count + cycle_return_count,
        "S0_prime_hit_count": s0_full_hit_count,
        "primary_refuted":
            bool(clean_event_count or cycle_return_count or s0_full_hit_count)
            or not s0_build["pass"]
            or not primary_window["pass"]
            or not accounting_pass,
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "checks": {},
        "pass": False,
        "terminal": "CYCLE836_DEPTH_INDEPENDENT_CHECK_HONEST_FAIL",
    }
    output = stable_output(
        checks, certificates, report, controls_base
    )
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        sys.stdout.write(compact({
            "pass": False,
            "terminal": "CYCLE836_DEPTH_INDEPENDENT_CHECK_HONEST_FAIL",
            "failure": "stdout limit exceeded",
            "stdout_bytes": len(output.encode("utf-8")),
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
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
            "terminal": "CYCLE836_DEPTH_INDEPENDENT_CHECK_HONEST_FAIL",
            "exception_type": type(error).__name__,
            "exception": str(error),
        }) + "\n")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
