#!/usr/bin/env python3
"""Cycle 841 independent adversarial check of clocks and consumers.

The Cycle 841 and Cycle 835 primaries are SHA-pinned text/AST inputs only and
are protected by an import firewall.  Register-entry times are recomputed by a
fresh replay from the landed Cycle 719 core; neither primary is executed.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1190
STDOUT_LIMIT_BYTES = 149 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle796_monitored_selector_2026_07_28.py",
    "scripts/frontier_cycle832_cohort_moment_law_2026_07_28.py",
    "scripts/frontier_cycle833_funnel_family_2026_07_28.py",
    "scripts/frontier_cycle835_register_mechanism_2026_07_28.py",
    "scripts/frontier_cycle841_deciding_the_tick_2026_07_28.py",
)

import ast
from hashlib import sha1, sha256
import importlib.abc
from itertools import combinations
import json
from math import lcm
from pathlib import Path
import subprocess
import sys
from time import monotonic
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
CORE_PATH, PATH_796, PATH_832, PATH_833, PATH_835, PATH_841 = (
    AUDIT_INPUT_PATHS
)
TRACKED_TIMING_MODULES = (PATH_796, PATH_832, PATH_833, PATH_835)
TEXT_AST_ONLY_PATHS = AUDIT_INPUT_PATHS[1:]
BLOCKLISTED_MODULES = (
    Path(PATH_835).stem,
    Path(PATH_841).stem,
)

EXPECTED_SHA256 = {
    CORE_PATH:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    PATH_796:
        "be0238611e02f9bad8df813430f9decec68d287df267bbf82ba4a63ffc8483c3",
    PATH_832:
        "0db01e80084af4dbb52c74a0a055984edf8ab818f2c8ba8a99c1f6a3fc15bb3e",
    PATH_833:
        "bd08f5f503e532c724e6ae28915ba2f0b4202360bbe01458924d689e27c79174",
    PATH_835:
        "6b8c26ff77d99225aaa985c645aeee9fa1fb3db19517aec727ff38e0cbcc03f5",
    PATH_841:
        "9879f900590b2a9cdded11d2b691d48adf5c5baff96af4f88b7483bfc98a0b54",
}
EXPECTED_GIT_BLOBS = {
    CORE_PATH: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    PATH_796: "eb2f34cd78fae3ce579d426df2ffe62832003504",
    PATH_832: "d666f5c301ffe6b6508f3636b15814a662bfbe8e",
    PATH_833: "b3512e0c3e8acdec7bc3f1cfb4e5bf1a236f8fda",
    PATH_835: "a9bfc3d151a591b3d0a4ba06acaa30ed04ff7e67",
    PATH_841: "379bbe1f4d7ae3432488359fbf3009adfe2a5984",
}


class _PrimaryFirewall(importlib.abc.MetaPathFinder):
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


EVENT_ORDER = (0, 2, 1)
TRANSITIONS = ((0, 2), (2, 1))
FIXTURE_BANKS = 2
RING_STATIONS = 11
WITNESS_PAIR = (1, 6)
LCM_SKELETON = lcm(4464, 5952)
RESIDUALS = (595, 64)


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(
        f"blob {len(payload)}\0".encode("ascii") + payload
    ).hexdigest()


def literal_assignment(tree: ast.Module, name: str) -> object | None:
    matches: list[ast.expr] = []
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
        return None
    try:
        return ast.literal_eval(matches[0])
    except (TypeError, ValueError):
        return None


def function_node(tree: ast.Module, name: str) -> ast.FunctionDef:
    rows = [
        node for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    if len(rows) != 1:
        raise AssertionError((name, len(rows)))
    return rows[0]


def loaded_names(node: ast.AST) -> set[str]:
    return {
        child.id for child in ast.walk(node)
        if isinstance(child, ast.Name) and isinstance(child.ctx, ast.Load)
    }


def called_names(node: ast.AST) -> set[str]:
    rows: set[str] = set()
    for child in ast.walk(node):
        if not isinstance(child, ast.Call):
            continue
        if isinstance(child.func, ast.Name):
            rows.add(child.func.id)
        elif isinstance(child.func, ast.Attribute):
            rows.add(child.func.attr)
    return rows


def string_literals(node: ast.AST) -> set[str]:
    return {
        child.value for child in ast.walk(node)
        if isinstance(child, ast.Constant) and isinstance(child.value, str)
    }


def raw_catchup(times: dict[int, int]) -> tuple[int, ...]:
    return tuple(
        times[target] - times[source] - LCM_SKELETON
        for source, target in TRANSITIONS
    )


DIRECT_ENTRY_KEYS = frozenset({
    "final_projection_entry_time",
    "final_entry_times",
    "source_final_entry",
    "target_final_entry",
    "register_final_entry_times",
    "raw_register_catchup",
})
EQUIVALENT_ENTRY_KEYS = frozenset({"terminal_dwell_ticks"})


class _ClockReadVisitor(ast.NodeVisitor):
    def __init__(self, source: str, path: str) -> None:
        self.source = source
        self.path = path
        self.functions: list[str] = []
        self.rows: list[dict[str, object]] = []

    def visit_FunctionDef(self, node: ast.FunctionDef) -> Any:
        self.functions.append(node.name)
        self.generic_visit(node)
        self.functions.pop()
        return None

    def visit_Subscript(self, node: ast.Subscript) -> Any:
        key = (
            node.slice.value
            if isinstance(node.slice, ast.Constant)
            and isinstance(node.slice.value, str)
            else None
        )
        if (
            isinstance(node.ctx, ast.Load)
            and key in DIRECT_ENTRY_KEYS | EQUIVALENT_ENTRY_KEYS
        ):
            self.rows.append({
                "path": self.path,
                "function": (
                    self.functions[-1] if self.functions else "<module>"
                ),
                "line": node.lineno,
                "key": key,
                "kind": (
                    "DIRECT_REGISTER_ENTRY_READ"
                    if key in DIRECT_ENTRY_KEYS
                    else "ALGEBRAIC_EQUIVALENT_DWELL_READ"
                ),
                "verbatim": ast.get_source_segment(
                    self.source, node
                ),
            })
        self.generic_visit(node)
        return None


def zero_consumer_hunt(
    payloads: dict[str, bytes],
    trees: dict[str, ast.Module],
) -> dict[str, object]:
    findings = []
    function_counts = {}
    ast_node_counts = {}
    for path in TRACKED_TIMING_MODULES:
        source = payloads[path].decode("utf-8")
        tree = trees[path]
        visitor = _ClockReadVisitor(source, path)
        visitor.visit(tree)
        findings.extend(visitor.rows)
        function_counts[path] = sum(
            isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
            for node in ast.walk(tree)
        )
        ast_node_counts[path] = sum(1 for _node in ast.walk(tree))

    producer_function = "track_register_trajectories"
    consumer_findings = tuple(
        row for row in findings
        if row["function"] != producer_function
    )
    strong_consumer_functions = tuple(sorted({
        str(row["function"]) for row in consumer_findings
        if row["function"] in {
            "residual_certificate",
            "raw_near_miss_certificate",
            "timeline_convention_certificate",
        }
    }))
    return {
        "claim_under_attack":
            "REGISTER_ENTRY_CLOCK_HAS_ZERO_LANDED_CONSUMERS",
        "scan_scope": {
            "declaration":
                "exhaustive AST walk of every node in the four SHA-pinned "
                "tracked landed timing modules named below",
            "paths": TRACKED_TIMING_MODULES,
            "function_counts": function_counts,
            "ast_node_counts": ast_node_counts,
            "read_keys": tuple(sorted(DIRECT_ENTRY_KEYS)),
            "equivalent_keys": tuple(sorted(EQUIVALENT_ENTRY_KEYS)),
            "producer_exclusion":
                "track_register_trajectories creates the clock and is not "
                "counted as its own consumer",
        },
        "findings_verbatim": consumer_findings,
        "strong_consumer_functions": strong_consumer_functions,
        "consumer_count": len(consumer_findings),
        "zero_consumer_claim_holds": not consumer_findings,
        "finding":
            "REFUTED: landed Cycle 835 reads the register-entry clock in "
            "residual_certificate and timeline_convention_certificate."
            if consumer_findings else
            "NOT REFUTED: no register-entry read was found in scope.",
        "pass": not consumer_findings,
    }


def forcing_table(
    trees: dict[str, ast.Module],
    consumer_hunt: dict[str, object],
) -> dict[str, object]:
    monitor = function_node(trees[PATH_796], "monitor_family")
    boundary = function_node(trees[PATH_796], "advance_one_boundary")
    main_796 = function_node(trees[PATH_796], "main")
    evolve = function_node(trees[PATH_832], "evolve_funnels")
    reconstruct = function_node(trees[PATH_833], "reconstruct_funnels")
    field_map = function_node(
        trees[PATH_833], "rank_edge_field_map_certificate"
    )
    pulse = function_node(trees[PATH_835], "pulse_replay")
    pulse_phase = function_node(
        trees[PATH_835], "pulse_phase_certificate"
    )

    lock_ok = (
        {"RESOLUTION_MOMENTS", "previous_nonclean"}
        <= loaded_names(evolve)
        and {"advance", "nonclean_mask", "support_at_lane"}
        <= called_names(evolve)
        and {
            "every_earlier_moment_nonclean",
            "veto_at_t_minus_1",
            "all_landed_clean",
        } <= string_literals(evolve)
    )
    cycle796_ok = (
        {"advance_one_boundary", "clean_postimage"}
        <= called_names(monitor)
        and {"first_clean", "horizon"} <= loaded_names(monitor)
        and "apply_semantic" in called_names(boundary)
        and any(
            "orbit_return_boundary governs" in value
            for value in string_literals(main_796)
        )
    )
    funnel_ok = (
        "FUNNEL_MOMENTS" in loaded_names(reconstruct)
        and "advance" in called_names(reconstruct)
        and {"xor_support", "apply_named_xor_update"}
        <= called_names(field_map)
        and "arrival_rank_edge" in string_literals(field_map)
    )
    absolute_clock_names = {
        "RESOLUTION_MOMENTS",
        "FUNNEL_MOMENTS",
        "MOMENT_MINUS_FIVE",
        "final_projection_entry_time",
        "entry_times",
    }
    pulse_absolute_names = tuple(sorted(
        (
            loaded_names(pulse)
            | loaded_names(pulse_phase)
        ) & absolute_clock_names
    ))
    pulse_ok = (
        not pulse_absolute_names
        and {"movement", "gate_index"} <= loaded_names(pulse)
        and {"checkpoint", "boundary_row"} <= called_names(pulse)
        and "canonical_phase_mod_3" in string_literals(pulse)
    )
    rows = (
        {
            "row": "lock law",
            "clock": "MOMENT",
            "module_function": f"{PATH_832}::evolve_funnels",
            "ast_and_behavior_pass": lock_ok,
            "behavior":
                "one landed orbit update per integer moment; the first "
                "all-clean boundary is RESOLUTION_MOMENTS with an m-1 veto",
        },
        {
            "row": "Cycle 796",
            "clock": "MOMENT",
            "module_function": f"{PATH_796}::monitor_family",
            "ast_and_behavior_pass": cycle796_ok,
            "behavior":
                "horizon increments only after advance_one_boundary applies "
                "the complete orbit-return composition word",
        },
        {
            "row": "funnel map",
            "clock": "MOMENT-5",
            "module_function": f"{PATH_833}::reconstruct_funnels",
            "ast_and_behavior_pass": funnel_ok,
            "behavior":
                "the state is advanced through FUNNEL_MOMENTS and then "
                "consumed by the named-field rank-edge XOR map",
        },
        {
            "row": "pulse",
            "clock": "ORIGIN-NEUTRAL_RELATIVE_PHASE",
            "module_function": f"{PATH_835}::pulse_replay",
            "ast_and_behavior_pass": pulse_ok,
            "behavior":
                "movement modulo three and aligned gate checkpoints define "
                "phase; no absolute clock variable is read",
            "absolute_clock_names_read": pulse_absolute_names,
        },
    )
    advertised_rows_verified = all(
        bool(row["ast_and_behavior_pass"]) for row in rows
    )
    complete = bool(consumer_hunt["zero_consumer_claim_holds"])
    return {
        "advertised_rows": rows,
        "advertised_rows_verified": advertised_rows_verified,
        "table_complete_over_declared_scan_scope": complete,
        "omitted_register_entry_consumers":
            consumer_hunt["strong_consumer_functions"],
        "finding":
            "REFUTED AS A COMPLETE FORCING TABLE: all four advertised rows "
            "classify as claimed, but landed Cycle 835 register-entry "
            "consumers were omitted."
            if not complete else
            "VERIFIED: advertised rows pass and no omitted consumer exists.",
        "pass": advertised_rows_verified and complete,
    }


def cyclic_separation(pair: tuple[int, int]) -> int:
    return min(
        (pair[1] - pair[0]) % RING_STATIONS,
        (pair[0] - pair[1]) % RING_STATIONS,
    )


def orbit_word(
    program: tuple[object, ...],
    pair: tuple[int, int],
) -> tuple[object, ...]:
    rows: list[object] = []
    for step in range(len(program)):
        live = {
            (pair[0] + step) % len(program),
            (pair[1] + step) % len(program),
        }
        for station, program_row in enumerate(program):
            if station in live:
                rows.extend(K.mapped_macro(program_row))
    return tuple(rows)


def independent_witness_states() -> tuple[
    tuple[object, ...], dict[int, tuple[int, ...]], dict[str, object]
]:
    program = K.interleaved_program(FIXTURE_BANKS)
    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    state = K.M.pack_state(banks, links)
    allocator = K.M.global_allocator_word(FIXTURE_BANKS)
    states = {}
    epoch_failures = 0
    witness_failures = 0
    for event in range(2 * FIXTURE_BANKS):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = K.M.prepare_endpoint(state, direction)
        after, rail_a, rail_b, trace = K.run_orbit(before, program)
        epoch_failures += int(
            after != K.A.apply_semantic(before, allocator)
        )
        epoch_failures += int(
            rail_a != (1,) + (0,) * (len(program) - 1)
        )
        epoch_failures += int(any(rail_b))
        epoch_failures += int(len(trace) != len(program))

        witness, witness_a, witness_b, _ = K.run_orbit(
            before, program, token_positions=WITNESS_PAIR
        )
        expected_rail = tuple(
            int(station in WITNESS_PAIR)
            for station in range(RING_STATIONS)
        )
        witness_failures += int(witness_a != expected_rail)
        witness_failures += int(any(witness_b))
        states[event] = witness
        state = after
    return program, states, {
        "epoch_failures": epoch_failures,
        "witness_rail_failures": witness_failures,
        "event_count": len(states),
        "pass": (
            epoch_failures == 0
            and witness_failures == 0
            and len(states) == 4
        ),
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


def wire_name(wire: int, state_bits: int) -> str:
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
    if wire >= state_bits:
        raise AssertionError((wire, state_bits))
    return f"unused_padding.wire[{wire}]"


def register_wires(
    register_fields: tuple[str, ...],
    state_bits: int,
) -> tuple[int, ...]:
    by_name = {
        wire_name(wire, state_bits): wire
        for wire in range(state_bits)
    }
    if len(by_name) != state_bits:
        raise AssertionError("wire-name decoder is not injective")
    return tuple(by_name[name] for name in register_fields)


def pack_states(states: tuple[tuple[int, ...], ...]) -> list[int]:
    return [
        sum(state[wire] << lane for lane, state in enumerate(states))
        for wire in range(len(states[0]))
    ]


def unpack_lane(columns: list[int], lane: int) -> tuple[int, ...]:
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


def compile_word(
    word: tuple[object, ...],
) -> tuple[tuple[int, int, int, int], ...]:
    rows = []
    for gate in word:
        if len(set(gate.wires)) != len(gate.wires):
            raise AssertionError(("repeated gate wire", gate))
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


def independent_register_replay(
    funnel_times: dict[int, int],
    register_fields: tuple[str, ...],
) -> dict[str, object]:
    program, event_states, family_check = independent_witness_states()
    word = orbit_word(program, WITNESS_PAIR)
    compiled = compile_word(word)
    lane_rows = tuple(
        (event, role)
        for event in EVENT_ORDER
        for role in ("primary", "determinism_duplicate")
    )
    initial_states = tuple(
        event_states[event] for event, _role in lane_rows
    )
    columns = pack_states(initial_states)
    state_bits = len(initial_states[0])
    wires = register_wires(register_fields, state_bits)
    primary_index = {
        event: lane
        for lane, (event, role) in enumerate(lane_rows)
        if role == "primary"
    }
    duplicate_index = {
        event: lane
        for lane, (event, role) in enumerate(lane_rows)
        if role == "determinism_duplicate"
    }
    histories = {
        event: [
            projected_int(columns, primary_index[event], wires)
        ]
        for event in EVENT_ORDER
    }
    active_mask = (1 << len(lane_rows)) - 1
    duplicate_exact = all(
        initial_states[primary_index[event]]
        == initial_states[duplicate_index[event]]
        for event in EVENT_ORDER
    )
    endpoint_sha256 = {}
    endpoint_weights = {}

    for tick in range(1, max(funnel_times.values()) + 1):
        for kind, first, second, third in compiled:
            if kind == 0:
                columns[first] ^= active_mask
            elif kind == 1:
                columns[second] ^= columns[first] & active_mask
            else:
                columns[third] ^= (
                    columns[first] & columns[second] & active_mask
                )
        for event in EVENT_ORDER:
            if tick > funnel_times[event]:
                continue
            primary = projected_int(
                columns, primary_index[event], wires
            )
            duplicate = projected_int(
                columns, duplicate_index[event], wires
            )
            duplicate_exact &= primary == duplicate
            histories[event].append(primary)
            if tick == funnel_times[event]:
                endpoint = unpack_lane(
                    columns, primary_index[event]
                )
                endpoint_duplicate = unpack_lane(
                    columns, duplicate_index[event]
                )
                duplicate_exact &= endpoint == endpoint_duplicate
                endpoint_sha256[event] = sha256(
                    bytes(endpoint)
                ).hexdigest()
                endpoint_weights[event] = sum(endpoint)
                active_mask &= ~(
                    (1 << primary_index[event])
                    | (1 << duplicate_index[event])
                )

    entry_times = {}
    trailing_dwell = {}
    sequence_sha256 = {}
    for event in EVENT_ORDER:
        history = histories[event]
        terminal = history[-1]
        entry = len(history) - 1
        while entry > 0 and history[entry - 1] == terminal:
            entry -= 1
        entry_times[event] = entry
        trailing_dwell[event] = funnel_times[event] - entry
        sequence_sha256[event] = sha256(b"".join(
            value.to_bytes(5, "little") for value in history
        )).hexdigest()

    expected_funnel_sha = {
        0: "cdf7e03092c6278b686c1f0edb9ebd716f4a285b1eabc8a7e2780695284a8f1a",
        2: "0015151ee4b751c35a5671fbb4f301d8569e78fc5a7ebe9f77372865b153c99b",
        1: "797fa122a629177c00c707aff4857d01bbad16b078983e3a6f1f5b632e094a41",
    }
    return {
        "construction":
            "fresh six-lane replay from Cycle 719: three event witnesses "
            "plus exact duplicates; 39-field histories retained at every "
            "landed orbit boundary",
        "family_check": family_check,
        "state_bits": state_bits,
        "register_field_count": len(register_fields),
        "register_wires": wires,
        "word_gate_count": len(compiled),
        "history_lengths": {
            event: len(histories[event]) for event in EVENT_ORDER
        },
        "history_sequence_sha256": sequence_sha256,
        "funnel_state_sha256": endpoint_sha256,
        "funnel_state_weights": endpoint_weights,
        "final_entry_times": entry_times,
        "trailing_terminal_dwell": trailing_dwell,
        "duplicate_exact_at_every_tick": duplicate_exact,
        "pass": (
            family_check["pass"]
            and state_bits == 5815
            and len(register_fields) == len(wires) == 39
            and len(compiled) == 6212
            and endpoint_sha256 == expected_funnel_sha
            and duplicate_exact
            and active_mask == 0
        ),
    }


def clock_values(
    trees: dict[str, ast.Module],
) -> tuple[dict[str, object], dict[str, object]]:
    moments_raw = literal_assignment(
        trees[PATH_832], "RESOLUTION_MOMENTS"
    )
    funnel_832_raw = literal_assignment(
        trees[PATH_832], "FUNNEL_MOMENTS"
    )
    funnel_833_raw = literal_assignment(
        trees[PATH_833], "FUNNEL_MOMENTS"
    )
    funnel_835_raw = literal_assignment(
        trees[PATH_835], "FUNNEL_MOMENTS"
    )
    register_fields_raw = literal_assignment(
        trees[PATH_835], "REGISTER_FIELDS"
    )
    if not all(
        isinstance(row, dict)
        for row in (
            moments_raw, funnel_832_raw,
            funnel_833_raw, funnel_835_raw,
        )
    ) or not isinstance(register_fields_raw, tuple):
        raise AssertionError("required landed literals not recovered")
    moments = {
        int(event): int(value)
        for event, value in moments_raw.items()
    }
    funnel_832 = {
        int(event): int(value)
        for event, value in funnel_832_raw.items()
    }
    funnel_833 = {
        int(event): int(value)
        for event, value in funnel_833_raw.items()
    }
    funnel_835 = {
        int(event): int(value)
        for event, value in funnel_835_raw.items()
    }
    derived_minus_five = {
        event: moments[event] - 5 for event in EVENT_ORDER
    }
    register_fields = tuple(map(str, register_fields_raw))
    replay = independent_register_replay(
        funnel_832, register_fields
    )
    entries = replay["final_entry_times"]
    certificate = {
        "method":
            "MOMENT parsed from the landed first-clean law; MOMENT-5 "
            "subtracted independently and cross-checked against both funnel "
            "modules; REGISTER-ENTRY recomputed from full 39-field histories",
        "MOMENT_event_order_0_2_1":
            tuple(moments[event] for event in EVENT_ORDER),
        "MOMENT_MINUS_FIVE_event_order_0_2_1":
            tuple(derived_minus_five[event] for event in EVENT_ORDER),
        "REGISTER_ENTRY_event_order_0_2_1":
            tuple(entries[event] for event in EVENT_ORDER),
        "funnel_literals_cross_module_exact":
            funnel_832 == funnel_833 == funnel_835,
        "moment_minus_five_exact":
            derived_minus_five == funnel_832,
        "register_replay": replay,
    }
    certificate["pass"] = (
        certificate["MOMENT_event_order_0_2_1"]
        == (14744, 33195, 51115)
        and certificate["MOMENT_MINUS_FIVE_event_order_0_2_1"]
        == (14739, 33190, 51110)
        and certificate["REGISTER_ENTRY_event_order_0_2_1"]
        == (14739, 33189, 51110)
        and certificate["funnel_literals_cross_module_exact"]
        and certificate["moment_minus_five_exact"]
        and replay["pass"]
    )
    clocks = {
        "MOMENT": moments,
        "MOMENT-5": derived_minus_five,
        "REGISTER-ENTRY": entries,
    }
    return clocks, certificate


def accounting_restatement(
    clocks: dict[str, dict[int, int]],
    replay: dict[str, object],
) -> dict[str, object]:
    rows = tuple({
        "clock": name,
        "times_event_order_0_2_1":
            tuple(times[event] for event in EVENT_ORDER),
        "raw_target_blind_catchup": raw_catchup(times),
    } for name, times in clocks.items())
    by_name = {row["clock"]: row for row in rows}
    raw_node = function_node(
        ast.parse(
            Path(__file__).read_text(encoding="utf-8"),
            filename=Path(__file__).name,
        ),
        "raw_catchup",
    )
    raw_loaded = loaded_names(raw_node)
    target_blind = "RESIDUALS" not in raw_loaded
    return {
        "formula":
            "raw(s,t)=time[target]-time[source]-lcm(4464,5952)",
        "lcm_rederived_stdlib": LCM_SKELETON,
        "rows": rows,
        "register_sequence_evidence": {
            "history_lengths": replay["history_lengths"],
            "history_sequence_sha256":
                replay["history_sequence_sha256"],
            "register_entry_times": replay["final_entry_times"],
        },
        "raw_function_loaded_names": tuple(sorted(raw_loaded)),
        "residual_targets_absent_from_raw_computation": target_blind,
        "fitted_terms": (),
        "comparison_after_raw_computation": {
            "withheld_residuals": RESIDUALS,
            "MOMENT_equals_residuals":
                by_name["MOMENT"]["raw_target_blind_catchup"]
                == RESIDUALS,
            "MOMENT-5_equals_residuals":
                by_name["MOMENT-5"]["raw_target_blind_catchup"]
                == RESIDUALS,
            "REGISTER-ENTRY_signed_difference": tuple(
                observed - target
                for observed, target in zip(
                    by_name["REGISTER-ENTRY"][
                        "raw_target_blind_catchup"
                    ],
                    RESIDUALS,
                )
            ),
        },
        "finding":
            "MOMENT and MOMENT-5 independently give raw {595,64}; "
            "REGISTER-ENTRY gives raw {594,65}. No fitted term is present.",
        "pass": (
            LCM_SKELETON == 17856
            and target_blind
            and by_name["MOMENT"]["raw_target_blind_catchup"]
            == RESIDUALS
            and by_name["MOMENT-5"]["raw_target_blind_catchup"]
            == RESIDUALS
            and by_name["REGISTER-ENTRY"][
                "raw_target_blind_catchup"
            ] == (594, 65)
            and replay["pass"]
        ),
    }


def source_controls(
    payloads: dict[str, bytes],
    trees: dict[str, ast.Module],
    self_tree: ast.Module,
) -> dict[str, object]:
    sha_rows = {
        path: sha256(payload).hexdigest()
        for path, payload in payloads.items()
    }
    blob_rows = {
        path: git_blob(payload) for path, payload in payloads.items()
    }
    tracked = subprocess.run(
        ("git", "ls-files", "--error-unmatch", *AUDIT_INPUT_PATHS),
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    tracked_paths = tuple(
        line for line in tracked.stdout.splitlines() if line
    )
    direct_frontier_imports = tuple(sorted(
        alias.name
        for node in self_tree.body
        if isinstance(node, ast.Import)
        for alias in node.names
        if alias.name.startswith("frontier_cycle")
    ))
    direct_frontier_from_imports = tuple(sorted(
        node.module
        for node in self_tree.body
        if isinstance(node, ast.ImportFrom)
        and node.module is not None
        and node.module.startswith("frontier_cycle")
    ))
    dangerous_dynamic_calls = tuple(sorted({
        child.func.id
        for child in ast.walk(self_tree)
        if isinstance(child, ast.Call)
        and isinstance(child.func, ast.Name)
        and child.func.id in {"eval", "exec", "compile", "__import__"}
    }))
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_INPUT_PATHS_literal":
            literal_assignment(self_tree, "AUDIT_INPUT_PATHS")
            == AUDIT_INPUT_PATHS,
        "existing_worktree_relative": (
            len(payloads) == len(AUDIT_INPUT_PATHS)
            and all(
                not Path(path).is_absolute()
                and (ROOT / path).is_file()
                for path in AUDIT_INPUT_PATHS
            )
        ),
        "read_scope_count_including_self": len(AUDIT_INPUT_PATHS) + 1,
        "read_scope_limit": 8,
        "tracked_input_paths": tracked_paths,
        "all_inputs_git_tracked":
            tracked.returncode == 0
            and set(tracked_paths) == set(AUDIT_INPUT_PATHS),
        "sha256": sha_rows,
        "expected_sha256": EXPECTED_SHA256,
        "git_blobs": blob_rows,
        "expected_git_blobs": EXPECTED_GIT_BLOBS,
        "source_modes": {
            path: (
                "DYNAMIC_IMPORT_LANDED_CORE"
                if path == CORE_PATH
                else (
                    "TEXT_AST_ONLY_BLOCKLISTED"
                    if path in {PATH_835, PATH_841}
                    else "TEXT_AST_ONLY"
                )
            )
            for path in AUDIT_INPUT_PATHS
        },
        "blocklisted_modules": BLOCKLISTED_MODULES,
        "blocklisted_modules_loaded": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits": tuple(FIREWALL.hits),
        "direct_frontier_imports": direct_frontier_imports,
        "direct_frontier_from_imports": direct_frontier_from_imports,
        "dangerous_dynamic_calls": dangerous_dynamic_calls,
        "timeout_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "self_sha256": sha256(
            Path(__file__).read_bytes()
        ).hexdigest(),
        "parsed_input_count": len(trees),
    }
    result["pass"] = (
        result["AUDIT_INPUT_PATHS_literal"]
        and result["existing_worktree_relative"]
        and result["read_scope_count_including_self"] <= 8
        and result["all_inputs_git_tracked"]
        and sha_rows == EXPECTED_SHA256
        and blob_rows == EXPECTED_GIT_BLOBS
        and not result["blocklisted_modules_loaded"]
        and not result["firewall_hits"]
        and direct_frontier_imports == (
            "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26",
        )
        and not direct_frontier_from_imports
        and not dangerous_dynamic_calls
        and AUDIT_TIMEOUT_SEC < 1200
        and STDOUT_LIMIT_BYTES < 150 * 1024
        and len(trees) == len(AUDIT_INPUT_PATHS)
    )
    return result


def render(
    certificates: tuple[tuple[str, bool, dict[str, object]], ...],
    summary: dict[str, object],
) -> str:
    lines = []
    for name, passed, detail in certificates:
        lines.append(
            f"{'PASS' if passed else 'FAIL'} {name} :: {compact(detail)}"
        )
    lines.append("SUMMARY :: " + compact(summary))
    lines.append(str(summary["terminal"]))
    return "\n".join(lines) + "\n"


def main() -> int:
    started = monotonic()
    payloads = {
        path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS
    }
    trees = {
        path: ast.parse(payload, filename=path)
        for path, payload in payloads.items()
    }
    self_tree = ast.parse(
        Path(__file__).read_bytes(), filename=Path(__file__).name
    )

    consumer_hunt = zero_consumer_hunt(payloads, trees)
    table = forcing_table(trees, consumer_hunt)
    clocks, clock_certificate = clock_values(trees)
    replay = clock_certificate["register_replay"]
    accounting = accounting_restatement(clocks, replay)
    accounting_duplicate = accounting_restatement(clocks, replay)
    deterministic = (
        replay["duplicate_exact_at_every_tick"]
        and digest(accounting) == digest(accounting_duplicate)
    )
    controls = source_controls(payloads, trees, self_tree)
    elapsed = monotonic() - started
    controls["determinism"] = {
        "register_duplicate_exact_at_every_tick":
            replay["duplicate_exact_at_every_tick"],
        "duplicate_accounting_digest_exact":
            digest(accounting) == digest(accounting_duplicate),
        "accounting_digest": digest(accounting),
    }
    controls["runtime_seconds"] = round(elapsed, 6)
    controls["runtime_below_1200_seconds"] = elapsed < 1200
    controls["runtime_below_declared_timeout"] = (
        elapsed < AUDIT_TIMEOUT_SEC
    )
    controls["stdout_bytes"] = 0
    controls["stdout_below_150KB"] = False
    controls["pass"] = bool(
        controls["pass"]
        and deterministic
        and elapsed < AUDIT_TIMEOUT_SEC
    )
    controls_base = bool(controls["pass"])

    # A clean checker execution is expected to return zero when the scoped
    # primary claim is successfully refuted, even though claim certificates
    # are printed as FAIL.
    refutation_established = (
        table["advertised_rows_verified"]
        and not table["table_complete_over_declared_scan_scope"]
        and not consumer_hunt["zero_consumer_claim_holds"]
        and {
            "residual_certificate",
            "timeline_convention_certificate",
        } <= set(consumer_hunt["strong_consumer_functions"])
    )
    summary = {
        "cycle": 841,
        "primary_verdict":
            "REFUTED_ZERO_CONSUMER_AND_COMPLETE_FORCING_TABLE_FALSE",
        "advertised_forcing_rows_verified":
            table["advertised_rows_verified"],
        "landed_register_entry_consumers_found":
            consumer_hunt["strong_consumer_functions"],
        "clocks": {
            name: tuple(times[event] for event in EVENT_ORDER)
            for name, times in clocks.items()
        },
        "raw_catchup": {
            name: raw_catchup(times)
            for name, times in clocks.items()
        },
        "checker_pass": False,
        "stdout_bytes": 0,
        "terminal":
            "CYCLE841_INDEPENDENT_ADVERSARIAL_CHECK_HONEST_FAIL",
    }
    certificate_specs = (
        ("THE_FORCING_TABLE", bool(table["pass"]), table),
        (
            "THE_ZERO_CONSUMER_HUNT",
            bool(consumer_hunt["pass"]),
            consumer_hunt,
        ),
        (
            "THE_CLOCK_VALUES",
            bool(clock_certificate["pass"]),
            clock_certificate,
        ),
        (
            "THE_ACCOUNTING_RESTATEMENT",
            bool(accounting["pass"]),
            accounting,
        ),
        ("CONTROLS", bool(controls["pass"]), controls),
    )

    for _attempt in range(20):
        certificates = tuple(
            (
                name,
                bool(controls["pass"]) if name == "CONTROLS" else passed,
                detail,
            )
            for name, passed, detail in certificate_specs
        )
        output = render(certificates, summary)
        size = len(output.encode("utf-8"))
        stdout_ok = size < STDOUT_LIMIT_BYTES
        checker_pass = bool(
            refutation_established
            and clock_certificate["pass"]
            and accounting["pass"]
            and controls_base
            and stdout_ok
        )
        terminal = (
            "CYCLE841_PRIMARY_ZERO_CONSUMER_REFUTED_PASS"
            if checker_pass else
            "CYCLE841_INDEPENDENT_ADVERSARIAL_CHECK_HONEST_FAIL"
        )
        stable = (
            controls["stdout_bytes"] == size
            and controls["stdout_below_150KB"] == stdout_ok
            and controls["pass"] == (controls_base and stdout_ok)
            and summary["stdout_bytes"] == size
            and summary["checker_pass"] == checker_pass
            and summary["terminal"] == terminal
        )
        controls["stdout_bytes"] = size
        controls["stdout_below_150KB"] = stdout_ok
        controls["pass"] = controls_base and stdout_ok
        summary["stdout_bytes"] = size
        summary["checker_pass"] = checker_pass
        summary["terminal"] = terminal
        if stable:
            break

    certificates = tuple(
        (
            name,
            bool(controls["pass"]) if name == "CONTROLS" else passed,
            detail,
        )
        for name, passed, detail in certificate_specs
    )
    output = render(certificates, summary)
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        return 2
    sys.stdout.write(output)
    return 0 if summary["checker_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
