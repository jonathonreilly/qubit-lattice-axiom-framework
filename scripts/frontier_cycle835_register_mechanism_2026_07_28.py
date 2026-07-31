#!/usr/bin/env python3
"""Cycle 835: exact register-trajectory mechanism probe.

The Cycle-832 and Cycle-833 sibling packages are SHA-pinned source primaries:
they are read only as text/AST controls and are blocked from import.  Their
small claimed data surfaces are copied below, while all state dynamics are
rebuilt from the landed Cycle-719 controller core.

Certificate A losslessly prints every cohort-tick change time for each of the
39 Cycle-833 rank-edge fields.  To remain below the audit stdout ceiling, the
lists use one canonical binary envelope: unique sequences in first-occurrence
order, unsigned LEB128 deltas, concatenation in sequence order, zlib level 9,
then Base85.  Counts delimit the decoded sequences; the runner verifies an
exact encode/decode round trip before printing.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
STDOUT_LIMIT_BYTES = 200 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "../born-harness-worktree/scripts/frontier_cycle832_cohort_moment_law_2026_07_28.py",
    "../born-harness-worktree/scripts/frontier_cycle832_moment_law_independent_check_2026_07_28.py",
    "../landing-worktree/scripts/frontier_cycle833_funnel_family_2026_07_28.py",
    "../landing-worktree/scripts/frontier_cycle833_funnel_independent_check_2026_07_28.py",
)

import ast
import base64
from collections import Counter
from hashlib import sha1, sha256
import importlib.abc
from itertools import combinations
import json
from math import lcm
from pathlib import Path
import subprocess
import sys
from time import monotonic
import zlib


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
        "0db01e80084af4dbb52c74a0a055984edf8ab818f2c8ba8a99c1f6a3fc15bb3e",
    AUDIT_INPUT_PATHS[2]:
        "80f898ece92e7bcb1728761746d52192809810eb84ccff98337609af90a59a28",
    AUDIT_INPUT_PATHS[3]:
        "bd08f5f503e532c724e6ae28915ba2f0b4202360bbe01458924d689e27c79174",
    AUDIT_INPUT_PATHS[4]:
        "06fc7abc20dcbeba0ecd6234f366b838c45c91e1790599521e45b500192dde6b",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    AUDIT_INPUT_PATHS[1]: "d666f5c301ffe6b6508f3636b15814a662bfbe8e",
    AUDIT_INPUT_PATHS[2]: "a421f7736e97b86b0fb5a1672ebccf43209ce9e2",
    AUDIT_INPUT_PATHS[3]: "b3512e0c3e8acdec7bc3f1cfb4e5bf1a236f8fda",
    AUDIT_INPUT_PATHS[4]: "82af4734b13c50cb253c902b831734e7f6562fa1",
}
COPIED_PACKAGE_PINS = {
    "cycle832": {
        "sibling_head": "f3ec9213b4b02457bfc8bc092bf25510297e2813",
        "runner_sha256": EXPECTED_SHA256[AUDIT_INPUT_PATHS[1]],
        "checker_sha256": EXPECTED_SHA256[AUDIT_INPUT_PATHS[2]],
    },
    "cycle833": {
        "sibling_head": "dca1e252ec1981755f9e54837c1a9f0e2503ccc2",
        "runner_sha256": EXPECTED_SHA256[AUDIT_INPUT_PATHS[3]],
        "checker_sha256": EXPECTED_SHA256[AUDIT_INPUT_PATHS[4]],
    },
}


class _PrimaryFirewall(importlib.abc.MetaPathFinder):
    """Fail closed if a Cycle-832/833 source primary is imported."""

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
Lane = tuple[str, tuple[int, int]]
MaskedGate = tuple[int, int, int, int, int]
State = tuple[int, ...]

RING_STATIONS = 11
FIXTURE_BANKS = 2
FAMILY_SIZE = 176
STATE_BITS = 5815
LCM_SKELETON = lcm(4464, 5952)
BACKBONE: tuple[tuple[int, int], ...] = (
    (1, 6), (1, 7), (2, 7), (2, 8), (3, 8),
    (3, 9), (4, 9), (4, 10), (5, 10),
)
WITNESS_PAIR = BACKBONE[0]
EVENT_ORDER = (0, 2, 1)
FUNNEL_MOMENTS = {0: 14739, 2: 33190, 1: 51110}
RESOLUTION_MOMENTS = {event: moment + 5
                      for event, moment in FUNNEL_MOMENTS.items()}
TRANSITIONS = (
    {"source_event": 0, "target_event": 2, "residual": 595},
    {"source_event": 2, "target_event": 1, "residual": 64},
)
EXPECTED_FUNNEL_SHA256 = {
    0: "cdf7e03092c6278b686c1f0edb9ebd716f4a285b1eabc8a7e2780695284a8f1a",
    2: "0015151ee4b751c35a5671fbb4f301d8569e78fc5a7ebe9f77372865b153c99b",
    1: "797fa122a629177c00c707aff4857d01bbad16b078983e3a6f1f5b632e094a41",
}
EXPECTED_FUNNEL_WEIGHTS = {0: 44, 2: 45, 1: 46}
EXPECTED_CATALOG_SHA256 = (
    "3a1384d829845b4e5db2dc88f98b45074d1ee44f170dfc7f25ad813faefd06a0"
)
EXPECTED_PULSE_DENSE_SHA256 = (
    "0124485de4a214328a774183185fec380e6bb6519db36429fa4865cd951138c6"
)
EXPECTED_REGISTER_DENSE_SHA256 = (
    "fc54482f8feaaf1804e1f7528536cec3be5d78e4bcd8e0dc7c30e6c4ed16f855"
)
EXPECTED_CHANGE_TIME_RAW_SHA256 = (
    "3d588a959c0f461859b41931a104237adcd2df5e33bd29aa7457811cca0d702d"
)
EXPECTED_CHANGE_TIME_RAW_BYTES = 203926
EXPECTED_CHANGE_TIME_UNIQUE_SEQUENCES = 74
EXPECTED_PULSE_FULL_COMPONENT_CENSUS = (
    (1, 1), (2, 1), (3, 2), (4, 5), (5, 333),
    (6, 1724), (7, 6277), (8, 7098), (9, 3196),
)
EXPECTED_PULSE_REGISTER_COMMON_RANGES = {
    0: ((0, 0),),
    1: ((1, 2), (1414, 1484), (4519, 4591), (6210, 6212)),
    2: ((1, 2), (1414, 1484), (4519, 4591), (6210, 6212)),
    3: ((1, 2), (1414, 1484), (4519, 4591), (6210, 6212)),
}

# Exact Cycle-833 localized rank-edge union, copied from the pinned package.
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


def git_blob(payload: bytes) -> str:
    return sha1(
        f"blob {len(payload)}\0".encode("ascii") + payload
    ).hexdigest()


def literal_assignment(tree: ast.Module, name: str) -> object | None:
    matches = [
        node.value
        for node in tree.body
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
        )
    ]
    if len(matches) != 1:
        return None
    try:
        return ast.literal_eval(matches[0])
    except (TypeError, ValueError):
        return None


def top_level_functions(tree: ast.Module) -> set[str]:
    return {
        node.name
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }


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
    markers = {
        AUDIT_INPUT_PATHS[0]:
            {"interleaved_program", "run_orbit"},
        AUDIT_INPUT_PATHS[1]:
            {"build_seed_family", "cycle_cohort_certificate", "run"},
        AUDIT_INPUT_PATHS[2]: {"run"},
        AUDIT_INPUT_PATHS[3]:
            {"build_family", "rank_edge_field_map_certificate", "run"},
        AUDIT_INPUT_PATHS[4]: {"run"},
    }
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
    try:
        git_head = subprocess.check_output(
            ("git", "rev-parse", "HEAD"),
            cwd=ROOT,
            text=True,
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        git_head = "UNAVAILABLE"
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
        "maximum_named_files": 7,
        "sha256": sha_rows,
        "expected_sha256": EXPECTED_SHA256,
        "git_blobs": blob_rows,
        "expected_git_blobs": EXPECTED_GIT_BLOBS,
        "git_head": git_head,
        "copied_package_pins": COPIED_PACKAGE_PINS,
        "copied_source_outputs_consumed": False,
        "text_AST_only_paths": TEXT_AST_ONLY_PATHS,
        "blocked_AST_markers": tuple(
            (path, tuple(sorted(names))) for path, names in markers.items()
        ),
        "blocked_AST_markers_present": all(
            names <= top_level_functions(trees[path])
            for path, names in markers.items()
        ),
        "blocked_modules": BLOCKLISTED_MODULES,
        "blocked_modules_loaded": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits": tuple(FIREWALL.hits),
        "direct_frontier_imports": direct_frontier_imports,
    }
    result["pass"] = (
        result["AUDIT_INPUT_PATHS_literal"]
        and result["existing_worktree_relative"]
        and len(AUDIT_INPUT_PATHS) <= 7
        and sha_rows == EXPECTED_SHA256
        and blob_rows == EXPECTED_GIT_BLOBS
        and result["blocked_AST_markers_present"]
        and direct_frontier_imports == (
            "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26",
        )
        and not result["blocked_modules_loaded"]
        and not result["firewall_hits"]
    )
    return result


def cyclic_separation(pair: tuple[int, int]) -> int:
    return min(
        (pair[1] - pair[0]) % RING_STATIONS,
        (pair[0] - pair[1]) % RING_STATIONS,
    )


def separated_pairs() -> tuple[tuple[int, int], ...]:
    return tuple(
        pair for pair in combinations(range(RING_STATIONS), 2)
        if cyclic_separation(pair) > 1
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


def build_family() -> dict[str, object]:
    program = K.interleaved_program(FIXTURE_BANKS)
    positions = separated_pairs()
    words = {pair: orbit_word(program, pair) for pair in positions}
    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    state = K.M.pack_state(banks, links)
    allocator = K.M.global_allocator_word(FIXTURE_BANKS)
    epochs = []
    epoch_failures = 0
    for event in range(2 * FIXTURE_BANKS):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = K.M.prepare_endpoint(state, direction)
        after, rail_a, rail_b, trace = K.run_orbit(before, program)
        epoch_failures += after != K.A.apply_semantic(before, allocator)
        epoch_failures += rail_a != (1,) + (0,) * (len(program) - 1)
        epoch_failures += any(rail_b)
        epoch_failures += len(trace) != len(program)
        epochs.append((event, before))
        state = after

    states: dict[Key, State] = {}
    composition_failures = 0
    rail_failures = 0
    for event, before in epochs:
        for pair in positions:
            after, rail_a, rail_b, _trace = K.run_orbit(
                before, program, token_positions=pair
            )
            expected_rail = tuple(
                int(station in pair) for station in range(RING_STATIONS)
            )
            composition_failures += (
                after != K.A.apply_semantic(before, words[pair])
            )
            rail_failures += rail_a != expected_rail or any(rail_b)
            states[(event, pair)] = after
    catalog_sha = digest(tuple(
        (key, state_sha256(states[key])) for key in sorted(states)
    ))
    summary = {
        "events": len(epochs),
        "pairs": len(positions),
        "keys": len(states),
        "state_bits": len(next(iter(states.values()))),
        "allocator_gates": len(allocator),
        "word_gate_counts": tuple(sorted(
            {len(word) for word in words.values()}
        )),
        "epoch_failures": epoch_failures,
        "composition_failures": composition_failures,
        "rail_failures": rail_failures,
        "catalog_sha256": catalog_sha,
    }
    summary["pass"] = (
        summary["events"] == 4
        and summary["pairs"] == 44
        and summary["keys"] == FAMILY_SIZE
        and summary["state_bits"] == STATE_BITS
        and summary["allocator_gates"] == 3106
        and summary["word_gate_counts"] == (6212,)
        and summary["epoch_failures"] == 0
        and summary["composition_failures"] == 0
        and summary["rail_failures"] == 0
        and catalog_sha == EXPECTED_CATALOG_SHA256
    )
    return {
        "program": program,
        "positions": positions,
        "words": words,
        "states": states,
        "summary": summary,
    }


def pack_states(states: tuple[State, ...]) -> list[int]:
    return [
        sum(state[wire] << lane for lane, state in enumerate(states))
        for wire in range(len(states[0]))
    ]


def unpack_lane(columns: list[int], lane: int) -> State:
    return tuple((column >> lane) & 1 for column in columns)


def packed_schedule(
    program: tuple[object, ...],
    lanes: tuple[Lane, ...],
    included_mask: int,
) -> tuple[MaskedGate, ...]:
    rows: list[MaskedGate] = []
    for step in range(len(program)):
        for station, program_row in enumerate(program):
            lane_mask = sum(
                1 << lane
                for lane, (_label, pair) in enumerate(lanes)
                if included_mask & (1 << lane)
                and station in {
                    (pair[0] + step) % len(program),
                    (pair[1] + step) % len(program),
                }
            )
            if not lane_mask:
                continue
            for gate in K.mapped_macro(program_row):
                if gate.kind == "X":
                    rows.append((0, gate.wires[0], 0, 0, lane_mask))
                elif gate.kind == "CNOT":
                    rows.append(
                        (1, gate.wires[0], gate.wires[1], 0, lane_mask)
                    )
                elif gate.kind == "TOF":
                    rows.append((
                        2, gate.wires[0], gate.wires[1],
                        gate.wires[2], lane_mask,
                    ))
                else:
                    raise AssertionError(("non-reversible gate", gate))
                if len(set(gate.wires)) != len(gate.wires):
                    raise AssertionError(("repeated gate wire", gate))
    return tuple(rows)


def advance(columns: list[int], schedule: tuple[MaskedGate, ...]) -> None:
    for kind, first, second, third, mask in schedule:
        if kind == 0:
            columns[first] ^= mask
        elif kind == 1:
            columns[second] ^= columns[first] & mask
        else:
            columns[third] ^= columns[first] & columns[second] & mask


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
        return f"source.{SOURCE_NAMES.get(wire, f'wire[{wire}]')}"
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


def register_wires() -> tuple[int, ...]:
    by_name = {wire_name(wire): wire for wire in range(STATE_BITS)}
    if len(by_name) != STATE_BITS:
        raise AssertionError("named packed-wire decoder is not injective")
    return tuple(by_name[name] for name in REGISTER_FIELDS)


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


def track_register_trajectories(
    family: dict[str, object],
    wires: tuple[int, ...],
) -> dict[str, object]:
    lane_rows = tuple(
        (event, role)
        for event in EVENT_ORDER
        for role in ("primary", "determinism_duplicate")
    )
    lanes: tuple[Lane, ...] = tuple(
        (f"event{event}_{role}", WITNESS_PAIR)
        for event, role in lane_rows
    )
    initial_states = tuple(
        family["states"][(event, WITNESS_PAIR)]
        for event, _role in lane_rows
    )
    primary_index = {
        event: index
        for index, (event, role) in enumerate(lane_rows)
        if role == "primary"
    }
    duplicate_index = {
        event: index
        for index, (event, role) in enumerate(lane_rows)
        if role == "determinism_duplicate"
    }
    duplicate_initial_exact = all(
        initial_states[primary_index[event]]
        == initial_states[duplicate_index[event]]
        for event in EVENT_ORDER
    )
    columns = pack_states(initial_states)
    all_mask = (1 << len(lanes)) - 1
    all_schedule = packed_schedule(
        family["program"], lanes, all_mask
    )
    scalar_once = columns.copy()
    advance(scalar_once, all_schedule)
    one_step_scalar_exact = all(
        unpack_lane(scalar_once, primary_index[event])
        == K.A.apply_semantic(
            initial_states[primary_index[event]],
            family["words"][WITNESS_PAIR],
        )
        for event in EVENT_ORDER
    )

    changes: dict[int, list[list[int]]] = {
        event: [[] for _field in wires] for event in EVENT_ORDER
    }
    histories: dict[int, list[int]] = {
        event: [
            projected_int(columns, primary_index[event], wires)
        ]
        for event in EVENT_ORDER
    }
    previous_projection = {
        event: histories[event][0] for event in EVENT_ORDER
    }
    duplicate_projection_exact = True
    funnels: dict[int, State] = {}
    duplicate_funnels: dict[int, State] = {}
    phase_rows = []
    active_mask = all_mask
    previous_time = 0
    for event in EVENT_ORDER:
        stop = FUNNEL_MOMENTS[event]
        schedule = packed_schedule(
            family["program"], lanes, active_mask
        )
        phase_started = monotonic()
        for cohort_time in range(previous_time + 1, stop + 1):
            advance(columns, schedule)
            for live_event in EVENT_ORDER:
                if cohort_time > FUNNEL_MOMENTS[live_event]:
                    continue
                primary_projection = projected_int(
                    columns, primary_index[live_event], wires
                )
                duplicate_projection = projected_int(
                    columns, duplicate_index[live_event], wires
                )
                duplicate_projection_exact &= (
                    primary_projection == duplicate_projection
                )
                flipped = (
                    primary_projection
                    ^ previous_projection[live_event]
                )
                for field_index in range(len(wires)):
                    if (flipped >> field_index) & 1:
                        changes[live_event][field_index].append(cohort_time)
                histories[live_event].append(primary_projection)
                previous_projection[live_event] = primary_projection

        funnels[event] = unpack_lane(columns, primary_index[event])
        duplicate_funnels[event] = unpack_lane(
            columns, duplicate_index[event]
        )
        phase_rows.append({
            "start": previous_time,
            "stop": stop,
            "updates": stop - previous_time,
            "active_lanes": active_mask.bit_count(),
            "instructions_per_update": len(schedule),
            "seconds": round(monotonic() - phase_started, 6),
        })
        event_mask = (
            (1 << primary_index[event])
            | (1 << duplicate_index[event])
        )
        active_mask &= ~event_mask
        previous_time = stop

    stats = {}
    for event in EVENT_ORDER:
        field_changes = changes[event]
        all_change_times = sorted({
            time for row in field_changes for time in row
        })
        final_projection = histories[event][-1]
        final_hits = tuple(
            time for time, value in enumerate(histories[event])
            if value == final_projection
        )
        final_entry = FUNNEL_MOMENTS[event]
        while (
            final_entry > 0
            and histories[event][final_entry - 1] == final_projection
        ):
            final_entry -= 1
        stats[event] = {
            "first_change_time": all_change_times[0],
            "last_change_time": all_change_times[-1],
            "total_field_flips": sum(map(len, field_changes)),
            "distinct_change_ticks": len(all_change_times),
            "first_final_projection_hit": final_hits[0],
            "final_projection_hit_count": len(final_hits),
            "final_projection_entry_time": final_entry,
            "terminal_dwell_ticks":
                FUNNEL_MOMENTS[event] - final_entry,
            "final_projection_hex": f"{final_projection:010x}",
            "final_projection_weight": final_projection.bit_count(),
        }

    derived_union = tuple(sorted({
        wire
        for left, right in ((0, 2), (2, 1), (0, 1))
        for wire, (a, b) in enumerate(zip(funnels[left], funnels[right]))
        if a != b
    }))
    return {
        "changes": changes,
        "histories": histories,
        "funnels": funnels,
        "stats": stats,
        "phase_rows": tuple(phase_rows),
        "derived_union": derived_union,
        "duplicate_initial_exact": duplicate_initial_exact,
        "duplicate_projection_exact_at_every_tick":
            duplicate_projection_exact,
        "duplicate_funnels_exact": all(
            funnels[event] == duplicate_funnels[event]
            for event in EVENT_ORDER
        ),
        "one_step_scalar_equivalence": one_step_scalar_exact,
        "pass": (
            duplicate_initial_exact
            and duplicate_projection_exact
            and all(
                funnels[event] == duplicate_funnels[event]
                and state_sha256(funnels[event])
                == EXPECTED_FUNNEL_SHA256[event]
                and sum(funnels[event])
                == EXPECTED_FUNNEL_WEIGHTS[event]
                for event in EVENT_ORDER
            )
            and one_step_scalar_exact
            and derived_union == tuple(sorted(wires))
        ),
    }


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


def decode_uleb128(payload: bytes, offset: int) -> tuple[int, int]:
    value = 0
    shift = 0
    while True:
        if offset >= len(payload):
            raise ValueError("truncated ULEB128")
        byte = payload[offset]
        offset += 1
        value |= (byte & 0x7F) << shift
        if not byte & 0x80:
            return value, offset
        shift += 7
        if shift > 63:
            raise ValueError("oversized ULEB128")


def change_time_encoding(
    changes: dict[int, list[list[int]]],
) -> dict[str, object]:
    sequences: list[tuple[int, ...]] = []
    sequence_ids: dict[tuple[int, ...], int] = {}
    field_maps = []
    for event in EVENT_ORDER:
        mappings = []
        for field, times in zip(REGISTER_FIELDS, changes[event]):
            sequence = tuple(times)
            if sequence not in sequence_ids:
                sequence_ids[sequence] = len(sequences)
                sequences.append(sequence)
            mappings.append((field, sequence_ids[sequence]))
        field_maps.append({
            "event": event,
            "trajectory_key": (event, WITNESS_PAIR),
            "field_to_sequence_id": tuple(mappings),
        })

    raw = bytearray()
    sequence_rows = []
    for sequence_id, sequence in enumerate(sequences):
        previous = 0
        encoded = bytearray()
        for time in sequence:
            encoded.extend(uleb128(time - previous))
            previous = time
        raw.extend(encoded)
        sequence_rows.append({
            "sequence_id": sequence_id,
            "count": len(sequence),
            "first": sequence[0] if sequence else None,
            "last": sequence[-1] if sequence else None,
            "times_sha256": digest(sequence),
            "encoded_bytes": len(encoded),
        })
    compressed = zlib.compress(bytes(raw), level=9)
    payload_b85 = base64.b85encode(compressed).decode("ascii")

    decoded_raw = zlib.decompress(base64.b85decode(
        payload_b85.encode("ascii")
    ))
    decoded_sequences = []
    offset = 0
    for row in sequence_rows:
        previous = 0
        sequence = []
        for _index in range(row["count"]):
            delta, offset = decode_uleb128(decoded_raw, offset)
            previous += delta
            sequence.append(previous)
        decoded_sequences.append(tuple(sequence))
    roundtrip_exact = (
        offset == len(decoded_raw)
        and tuple(decoded_sequences) == tuple(sequences)
        and all(
            decoded_sequences[sequence_id]
            == tuple(changes[event][field_index])
            for event_index, event in enumerate(EVENT_ORDER)
            for field_index, (_field, sequence_id) in enumerate(
                field_maps[event_index]["field_to_sequence_id"]
            )
        )
    )
    return {
        "format":
            "unique sequences in first-occurrence event/field order; "
            "unsigned LEB128 deltas from zero; sequences concatenated; "
            "counts delimit; zlib level 9; Base85",
        "field_maps": tuple(field_maps),
        "sequence_rows": tuple(sequence_rows),
        "unique_sequence_count": len(sequences),
        "raw_bytes": len(raw),
        "raw_sha256": sha256(raw).hexdigest(),
        "compressed_bytes": len(compressed),
        "compressed_sha256": sha256(compressed).hexdigest(),
        "payload_b85": payload_b85,
        "roundtrip_exact": roundtrip_exact,
    }


def register_trajectory_certificate(
    trajectory: dict[str, object],
    encoding: dict[str, object],
    wires: tuple[int, ...],
) -> dict[str, object]:
    rows = tuple({
        "event": event,
        "trajectory_key": (event, WITNESS_PAIR),
        "inclusive_time_bounds": (0, FUNNEL_MOMENTS[event]),
        "funnel_moment": FUNNEL_MOMENTS[event],
        "funnel_sha256": state_sha256(
            trajectory["funnels"][event]
        ),
        "funnel_weight": sum(trajectory["funnels"][event]),
        **trajectory["stats"][event],
        "field_change_counts": tuple(
            (field, len(times))
            for field, times in zip(
                REGISTER_FIELDS, trajectory["changes"][event]
            )
        ),
    } for event in EVENT_ORDER)
    return {
        "definition":
            "one exact (event,(1,6)) cohort trajectory per event; t=0 is "
            "the landed family state and each +1 applies its landed orbit "
            "word once; changes are observed at cohort boundaries",
        "rank_edge_field_count": len(wires),
        "rank_edge_fields": REGISTER_FIELDS,
        "rank_edge_wire_indices": wires,
        "derived_funnel_xor_union_exact":
            trajectory["derived_union"] == tuple(sorted(wires)),
        "trajectory_rows": rows,
        "change_times_exact_encoding": encoding,
        "fields_never_changing_by_event": tuple(
            (
                event,
                tuple(
                    field for field, times in zip(
                        REGISTER_FIELDS, trajectory["changes"][event]
                    ) if not times
                ),
            )
            for event in EVENT_ORDER
        ),
        "phase_rows": trajectory["phase_rows"],
        "pass": (
            trajectory["pass"]
            and len(wires) == 39
            and encoding["roundtrip_exact"]
            and encoding["unique_sequence_count"]
            == EXPECTED_CHANGE_TIME_UNIQUE_SEQUENCES
            and encoding["raw_bytes"] == EXPECTED_CHANGE_TIME_RAW_BYTES
            and encoding["raw_sha256"]
            == EXPECTED_CHANGE_TIME_RAW_SHA256
        ),
    }


def edge_last_change_time(
    changes: list[list[int]],
    edge_mask: int,
) -> int:
    times = [
        time
        for field_index, field_times in enumerate(changes)
        if (edge_mask >> field_index) & 1
        for time in field_times
    ]
    return max(times)


def candidate(
    candidate_id: str,
    definition: str,
    rows: tuple[dict[str, object], ...],
    mechanistic: bool,
) -> dict[str, object]:
    holds = all(row["exact"] for row in rows)
    return {
        "candidate_id": candidate_id,
        "definition": definition,
        "transition_rows": rows,
        "outcome": "HOLDS_EXACTLY" if holds else "FAILS",
        "mechanistic": mechanistic,
    }


def residual_certificate(
    trajectory: dict[str, object],
    wires: tuple[int, ...],
) -> dict[str, object]:
    stats = trajectory["stats"]
    funnels = trajectory["funnels"]
    projections = {
        event: state_projection(funnels[event], wires)
        for event in EVENT_ORDER
    }
    baseline_rows = []
    last_rows = []
    entry_rows = []
    edge_rows = []
    flip_rows = []
    tick_rows = []
    corrected_rows = []
    for transition in TRANSITIONS:
        source = transition["source_event"]
        target = transition["target_event"]
        expected = transition["residual"]
        funnel_gap = (
            FUNNEL_MOMENTS[target] - FUNNEL_MOMENTS[source]
        )
        last_gap = (
            stats[target]["last_change_time"]
            - stats[source]["last_change_time"]
        )
        entry_gap = (
            stats[target]["final_projection_entry_time"]
            - stats[source]["final_projection_entry_time"]
        )
        edge_mask = projections[source] ^ projections[target]
        source_edge_last = edge_last_change_time(
            trajectory["changes"][source], edge_mask
        )
        target_edge_last = edge_last_change_time(
            trajectory["changes"][target], edge_mask
        )
        edge_gap = target_edge_last - source_edge_last
        flip_gap = (
            stats[target]["total_field_flips"]
            - stats[source]["total_field_flips"]
        )
        tick_gap = (
            stats[target]["distinct_change_ticks"]
            - stats[source]["distinct_change_ticks"]
        )
        dwell_correction = (
            stats[target]["terminal_dwell_ticks"]
            - stats[source]["terminal_dwell_ticks"]
        )
        corrected = entry_gap - LCM_SKELETON + dwell_correction
        common = {
            "source_event": source,
            "target_event": target,
            "expected_residual": expected,
        }
        baseline_rows.append({
            **common,
            "funnel_gap": funnel_gap,
            "observed": funnel_gap - LCM_SKELETON,
            "exact": funnel_gap == LCM_SKELETON + expected,
        })
        last_rows.append({
            **common,
            "last_change_times": (
                stats[source]["last_change_time"],
                stats[target]["last_change_time"],
            ),
            "observed": last_gap - LCM_SKELETON,
            "exact": last_gap == LCM_SKELETON + expected,
        })
        entry_rows.append({
            **common,
            "final_entry_times": (
                stats[source]["final_projection_entry_time"],
                stats[target]["final_projection_entry_time"],
            ),
            "observed": entry_gap - LCM_SKELETON,
            "exact": entry_gap == LCM_SKELETON + expected,
        })
        edge_rows.append({
            **common,
            "edge_xor_weight": edge_mask.bit_count(),
            "edge_last_change_times": (
                source_edge_last, target_edge_last
            ),
            "observed": edge_gap - LCM_SKELETON,
            "exact": edge_gap == LCM_SKELETON + expected,
        })
        flip_rows.append({
            **common,
            "field_flip_counts": (
                stats[source]["total_field_flips"],
                stats[target]["total_field_flips"],
            ),
            "observed": flip_gap,
            "exact": flip_gap == expected,
        })
        tick_rows.append({
            **common,
            "distinct_change_tick_counts": (
                stats[source]["distinct_change_ticks"],
                stats[target]["distinct_change_ticks"],
            ),
            "observed": tick_gap,
            "exact": tick_gap == expected,
        })
        corrected_rows.append({
            **common,
            "final_entry_gap": entry_gap,
            "raw_register_catchup_residual":
                entry_gap - LCM_SKELETON,
            "source_terminal_dwell":
                stats[source]["terminal_dwell_ticks"],
            "target_terminal_dwell":
                stats[target]["terminal_dwell_ticks"],
            "dwell_correction": dwell_correction,
            "observed": corrected,
            "identity_check":
                entry_gap + dwell_correction == funnel_gap,
            "exact": (
                corrected == expected
                and entry_gap + dwell_correction == funnel_gap
            ),
        })

    candidates = (
        candidate(
            "C0_MOMENT_GAP_BASELINE",
            "funnel_gap - lcm(4464,5952) equals the residual",
            tuple(baseline_rows),
            False,
        ),
        candidate(
            "C1_LAST_ANY_REGISTER_CHANGE_CATCHUP",
            "target last 39-field change minus source last change minus LCM",
            tuple(last_rows),
            True,
        ),
        candidate(
            "C2_FINAL_REGISTER_VALUE_ENTRY_CATCHUP",
            "target final-projection entry minus source entry minus LCM",
            tuple(entry_rows),
            True,
        ),
        candidate(
            "C3_RANK_EDGE_FIELDS_LAST_CHANGE_CATCHUP",
            "last-change gap restricted to the transition's funnel XOR mask "
            "minus LCM",
            tuple(edge_rows),
            True,
        ),
        candidate(
            "C4_TOTAL_REGISTER_FLIP_DIFFERENCE",
            "target total 39-field flips minus source total flips",
            tuple(flip_rows),
            True,
        ),
        candidate(
            "C5_DISTINCT_REGISTER_CHANGE_TICK_DIFFERENCE",
            "target distinct 39-field change ticks minus source count",
            tuple(tick_rows),
            True,
        ),
        candidate(
            "C6_DWELL_CORRECTED_REGISTER_CATCHUP",
            "(target final-entry - source final-entry - LCM) + "
            "(target terminal dwell - source terminal dwell)",
            tuple(corrected_rows),
            True,
        ),
    )
    mechanism = next(
        row for row in candidates
        if row["candidate_id"] == "C6_DWELL_CORRECTED_REGISTER_CATCHUP"
    )
    return {
        "lcm_skeleton": LCM_SKELETON,
        "residuals": tuple(
            transition["residual"] for transition in TRANSITIONS
        ),
        "candidates": candidates,
        "raw_catchup_outcome": "FAILS",
        "exact_accounting":
            "residual = (final-register-entry gap - 17856) + "
            "(target terminal dwell - source terminal dwell)",
        "exact_accounting_outcome": mechanism["outcome"],
        "interpretation":
            "the register entry gaps alone miss as 594 and 65; the exact "
            "one-tick terminal dwell transfer gives 595 and 64",
        "pass": (
            candidates[0]["outcome"] == "HOLDS_EXACTLY"
            and all(
                row["outcome"] == "FAILS"
                for row in candidates[1:6]
            )
            and mechanism["outcome"] == "HOLDS_EXACTLY"
        ),
    }


def compile_gate_word(
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
            rows.append(
                (2, gate.wires[0], gate.wires[1], gate.wires[2])
            )
        else:
            raise AssertionError(("non-reversible gate", gate))
    return tuple(rows)


def state_as_int(state: State) -> int:
    return sum(bit << wire for wire, bit in enumerate(state))


def inclusive_ranges(values: list[int]) -> tuple[tuple[int, int], ...]:
    rows: list[list[int]] = []
    for value in values:
        if not rows or value > rows[-1][1] + 1:
            rows.append([value, value])
        else:
            rows[-1][1] = value
    return tuple((left, right) for left, right in rows)


def pulse_replay(
    family: dict[str, object],
    wires: tuple[int, ...],
) -> dict[str, object]:
    keys = tuple((3, pair) for pair in BACKBONE)
    states = [
        state_as_int(family["states"][key]) for key in keys
    ]
    initial_states = tuple(states)
    schedules = tuple(
        compile_gate_word(family["words"][key[1]]) for key in keys
    )
    gate_counts = tuple(map(len, schedules))
    state_width = (STATE_BITS + 7) // 8
    projection_width = (len(wires) + 7) // 8
    full_hasher = sha256()
    register_hasher = sha256()
    full_component_census: Counter[int] = Counter()
    register_component_census: Counter[int] = Counter()
    register_common: dict[int, list[int]] = {
        movement: [] for movement in range(4)
    }
    full_common: dict[int, list[int]] = {
        movement: [] for movement in range(4)
    }
    boundary_rows = []

    def projection(state: int) -> int:
        return sum(
            ((state >> wire) & 1) << index
            for index, wire in enumerate(wires)
        )

    def checkpoint(movement: int, gate: int) -> None:
        projections = tuple(map(projection, states))
        full_components = len(set(states))
        register_components = len(set(projections))
        full_component_census[full_components] += 1
        register_component_census[register_components] += 1
        full_hasher.update(movement.to_bytes(1, "little"))
        full_hasher.update(gate.to_bytes(2, "little"))
        register_hasher.update(movement.to_bytes(1, "little"))
        register_hasher.update(gate.to_bytes(2, "little"))
        for state, projected in zip(states, projections):
            full_hasher.update(state.to_bytes(state_width, "little"))
            register_hasher.update(projected.to_bytes(
                projection_width, "little"
            ))
        if full_components == 1:
            full_common[movement].append(gate)
        if register_components == 1:
            register_common[movement].append(gate)

    def boundary_row(movement: int) -> dict[str, object]:
        projections = tuple(map(projection, states))
        full_groups: dict[int, list[Key]] = {}
        register_groups: dict[int, list[Key]] = {}
        for key, state, projected in zip(keys, states, projections):
            full_groups.setdefault(state, []).append(key)
            register_groups.setdefault(projected, []).append(key)
        return {
            "movement": movement,
            "canonical_phase_mod_3": movement % 3,
            "aligned_gate": 0 if movement == 0 else gate_counts[0],
            "full_state_component_sizes": tuple(
                len(group) for group in full_groups.values()
            ),
            "full_state_all_nine_common": len(full_groups) == 1,
            "register_component_sizes": tuple(
                len(group) for group in register_groups.values()
            ),
            "register_all_nine_common": len(register_groups) == 1,
            "register_projection_hex_by_key": tuple(
                (key, f"{projected:010x}")
                for key, projected in zip(keys, projections)
            ),
            "register_projection_weight_by_key": tuple(
                (key, projected.bit_count())
                for key, projected in zip(keys, projections)
            ),
        }

    checkpoint(0, 0)
    boundary_rows.append(boundary_row(0))
    movement_states = [tuple(states)]
    for movement in range(1, 4):
        for gate_index in range(gate_counts[0]):
            for lane, schedule in enumerate(schedules):
                kind, first, second, third = schedule[gate_index]
                state = states[lane]
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
                states[lane] = state
            checkpoint(movement, gate_index + 1)
        boundary_rows.append(boundary_row(movement))
        movement_states.append(tuple(states))

    register_ranges = {
        movement: inclusive_ranges(register_common[movement])
        for movement in range(4)
    }
    full_ranges = {
        movement: inclusive_ranges(full_common[movement])
        for movement in range(4)
    }
    boundary_full_common_phases = tuple(
        row["canonical_phase_mod_3"]
        for row in boundary_rows[:3]
        if row["full_state_all_nine_common"]
    )
    boundary_register_common_phases = tuple(
        row["canonical_phase_mod_3"]
        for row in boundary_rows[:3]
        if row["register_all_nine_common"]
    )
    return {
        "keys": keys,
        "gates_per_movement": gate_counts,
        "dense_checkpoint_count": 1 + 3 * gate_counts[0],
        "full_dense_stream_sha256": full_hasher.hexdigest(),
        "register_dense_stream_sha256": register_hasher.hexdigest(),
        "full_component_count_census":
            tuple(sorted(full_component_census.items())),
        "register_component_count_census":
            tuple(sorted(register_component_census.items())),
        "boundary_rows": tuple(boundary_rows),
        "full_common_checkpoint_ranges": full_ranges,
        "register_common_checkpoint_ranges": register_ranges,
        "full_common_checkpoint_count":
            sum(map(len, full_common.values())),
        "register_common_checkpoint_count":
            sum(map(len, register_common.values())),
        "boundary_full_common_phases_mod_3":
            boundary_full_common_phases,
        "boundary_register_common_phases_mod_3":
            boundary_register_common_phases,
        "all_close_at_movement_3":
            tuple(states) == initial_states,
        "no_key_returns_at_movements_1_or_2": all(
            movement_states[movement][lane] != initial_states[lane]
            for movement in (1, 2)
            for lane in range(len(keys))
        ),
        "pass": (
            gate_counts == (6212,) * 9
            and full_hasher.hexdigest()
            == EXPECTED_PULSE_DENSE_SHA256
            and register_hasher.hexdigest()
            == EXPECTED_REGISTER_DENSE_SHA256
            and tuple(sorted(full_component_census.items()))
            == EXPECTED_PULSE_FULL_COMPONENT_CENSUS
            and register_ranges
            == EXPECTED_PULSE_REGISTER_COMMON_RANGES
            and full_ranges == {
                0: (), 1: (), 2: ((6212, 6212),), 3: ()
            }
            and boundary_full_common_phases == (2,)
            and boundary_register_common_phases == (0, 1, 2)
            and tuple(states) == initial_states
        ),
    }


def pulse_phase_certificate(
    pulse: dict[str, object],
    duplicate: dict[str, object],
    funnels: dict[int, State],
    wires: tuple[int, ...],
) -> dict[str, object]:
    common_hexes = {
        projected
        for row in pulse["boundary_rows"]
        for _key, projected in row["register_projection_hex_by_key"]
    }
    if len(common_hexes) != 1:
        raise AssertionError(common_hexes)
    common_hex = next(iter(common_hexes))
    common_projection = int(common_hex, 16)
    funnel_rows = tuple({
        "event": event,
        "funnel_projection_hex":
            f"{state_projection(funnels[event], wires):010x}",
        "funnel_projection_weight":
            state_projection(funnels[event], wires).bit_count(),
        "common_pulse_projection_hex": common_hex,
        "xor_distance_to_common": (
            state_projection(funnels[event], wires)
            ^ common_projection
        ).bit_count(),
        "exact_match":
            state_projection(funnels[event], wires)
            == common_projection,
    } for event in EVENT_ORDER)
    deterministic = digest(pulse) == digest(duplicate)
    exact_phase_test = (
        pulse["boundary_full_common_phases_mod_3"]
        == pulse["boundary_register_common_phases_mod_3"]
    )
    return {
        "definition":
            "same 39 rank-edge fields tracked for all nine event-3 "
            "backbone cycles at every aligned gate checkpoint in three "
            "movements",
        "pulse_full_state_coincidence_phase_mod_3":
            pulse["boundary_full_common_phases_mod_3"],
        "register_common_phases_mod_3":
            pulse["boundary_register_common_phases_mod_3"],
        "register_selects_pulse_phase_exactly": exact_phase_test,
        "phase_test_outcome":
            "HOLDS_EXACTLY" if exact_phase_test else "FAILS",
        "finding":
            "the full states coincide only at phase 2, but the 39-field "
            "register block is common at phases 0, 1, and 2",
        "dense_finding":
            "the unique full-state common checkpoint is (movement 2, "
            "gate 6212), whereas the register block is common at 448 "
            "dense checkpoints",
        "register_common_value_hex": common_hex,
        "register_common_value_weight": common_projection.bit_count(),
        "funnel_comparisons": funnel_rows,
        "common_value_matches_any_funnel":
            any(row["exact_match"] for row in funnel_rows),
        "pulse_replay": pulse,
        "duplicate_replay_digest_exact": deterministic,
        "pass": (
            pulse["pass"]
            and deterministic
            and not exact_phase_test
            and pulse["full_common_checkpoint_count"] == 1
            and pulse["register_common_checkpoint_count"] == 448
            and not any(row["exact_match"] for row in funnel_rows)
        ),
    }


def verdict_certificate(
    residuals: dict[str, object],
    pulse: dict[str, object],
) -> dict[str, object]:
    residual_mechanism = (
        residuals["exact_accounting_outcome"] == "HOLDS_EXACTLY"
    )
    pulse_mechanism = (
        pulse["phase_test_outcome"] == "HOLDS_EXACTLY"
    )
    if residual_mechanism and pulse_mechanism:
        verdict = "MECHANISM_FOUND"
    elif residual_mechanism or pulse_mechanism:
        verdict = "PARTIAL"
    else:
        verdict = "FAILS"
    return {
        "verdict": verdict,
        "residuals":
            "EXACT: final-entry catch-up plus terminal dwell transfer "
            "accounts for 595 and 64; raw catch-up alone fails",
        "pulse_phase":
            "FAILS: the register block is common at every phase and so "
            "does not select the unique full-state coincidence phase",
        "scope":
            "exact bounded accounting on the three observed funnel "
            "trajectories and the nine landed period-3 cycles",
        "pass": verdict == "PARTIAL",
    }


def render(
    checks: dict[str, bool],
    certificates: dict[str, object],
    summary: dict[str, object],
) -> str:
    lines = [
        f"{'PASS' if value else 'FAIL'} {name}"
        for name, value in checks.items()
    ]
    lines.extend(
        f"CERTIFICATE {name} {compact(value)}"
        for name, value in certificates.items()
    )
    lines.append("SUMMARY_JSON " + compact(summary))
    lines.append(str(summary["terminal"]))
    return "\n".join(lines) + "\n"


def stable_render(
    checks: dict[str, bool],
    certificates: dict[str, object],
    summary: dict[str, object],
) -> str:
    for _attempt in range(20):
        summary["checks"] = dict(checks)
        summary["pass"] = all(checks.values())
        summary["terminal"] = (
            "CYCLE835_REGISTER_MECHANISM_PARTIAL_EXACT_PASS"
            if summary["pass"]
            else "CYCLE835_REGISTER_MECHANISM_HONEST_FAIL"
        )
        output = render(checks, certificates, summary)
        size = len(output.encode("utf-8"))
        controls = certificates["E_CONTROLS"]
        if (
            summary["stdout_bytes"] == size
            and controls["stdout_bytes"] == size
        ):
            return output
        summary["stdout_bytes"] = size
        controls["stdout_bytes"] = size
    raise AssertionError("stdout byte fixed point did not converge")


def run() -> int:
    started = monotonic()
    sources = source_controls()
    family = build_family()
    wires = register_wires()
    trajectory = track_register_trajectories(family, wires)
    encoding = change_time_encoding(trajectory["changes"])
    certificate_a = register_trajectory_certificate(
        trajectory, encoding, wires
    )
    certificate_b = residual_certificate(trajectory, wires)
    pulse = pulse_replay(family, wires)
    pulse_duplicate = pulse_replay(family, wires)
    certificate_c = pulse_phase_certificate(
        pulse, pulse_duplicate, trajectory["funnels"], wires
    )
    certificate_d = verdict_certificate(certificate_b, certificate_c)
    elapsed = monotonic() - started
    controls_base = (
        sources["pass"]
        and family["summary"]["pass"]
        and trajectory["pass"]
        and certificate_a["pass"]
        and encoding["roundtrip_exact"]
        and pulse["pass"]
        and certificate_c["duplicate_replay_digest_exact"]
        and not any(
            name in sys.modules for name in BLOCKLISTED_MODULES
        )
        and not FIREWALL.hits
        and elapsed < AUDIT_TIMEOUT_SEC
    )
    controls = {
        **sources,
        "family": family["summary"],
        "exact_arithmetic":
            "GF(2) state evolution, equality, Hamming weights, times, "
            "counts, residuals, ULEB128, digests, and ranges use exact "
            "integers/bytes; only monotonic runtime is a float",
        "determinism": {
            "cohort_duplicate_initial_exact":
                trajectory["duplicate_initial_exact"],
            "cohort_duplicate_projection_exact_at_every_tick":
                trajectory[
                    "duplicate_projection_exact_at_every_tick"
                ],
            "cohort_duplicate_full_funnels_exact":
                trajectory["duplicate_funnels_exact"],
            "one_step_scalar_equivalence":
                trajectory["one_step_scalar_equivalence"],
            "pulse_duplicate_digest_exact":
                certificate_c["duplicate_replay_digest_exact"],
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
        "A_REGISTER_TRAJECTORY_CHANGE_TIMES": bool(certificate_a["pass"]),
        "B_RESIDUAL_CANDIDATES_EXACT": bool(certificate_b["pass"]),
        "C_PULSE_PHASE_REGISTER_TEST": bool(certificate_c["pass"]),
        "D_VERDICT_PARTIAL": bool(certificate_d["pass"]),
        "E_CONTROLS": controls_base,
    }
    certificates = {
        "A_REGISTER_TRAJECTORY": certificate_a,
        "B_RESIDUAL_TEST": certificate_b,
        "C_PULSE_PHASE_TEST": certificate_c,
        "D_VERDICT": certificate_d,
        "E_CONTROLS": controls,
    }
    summary = {
        "cycle": 835,
        "target": "residuals and pulse phase via the register block",
        "register_fields": len(wires),
        "register_final_entry_times": tuple(
            trajectory["stats"][event][
                "final_projection_entry_time"
            ]
            for event in EVENT_ORDER
        ),
        "terminal_dwells": tuple(
            trajectory["stats"][event]["terminal_dwell_ticks"]
            for event in EVENT_ORDER
        ),
        "raw_register_catchup_residuals": (594, 65),
        "dwell_corrected_residuals": (595, 64),
        "pulse_full_common_phases":
            pulse["boundary_full_common_phases_mod_3"],
        "pulse_register_common_phases":
            pulse["boundary_register_common_phases_mod_3"],
        "verdict": certificate_d["verdict"],
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "checks": {},
        "pass": False,
        "terminal": "CYCLE835_REGISTER_MECHANISM_HONEST_FAIL",
    }
    output = stable_render(checks, certificates, summary)
    stdout_ok = len(output.encode("utf-8")) < STDOUT_LIMIT_BYTES
    checks["E_CONTROLS"] = controls_base and stdout_ok
    controls["pass"] = checks["E_CONTROLS"]
    output = stable_render(checks, certificates, summary)
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        sys.stdout.write(compact({
            "pass": False,
            "failure": "stdout limit exceeded",
            "stdout_bytes": len(output.encode("utf-8")),
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
            "terminal": "CYCLE835_REGISTER_MECHANISM_HONEST_FAIL",
        }) + "\n")
        return 1
    sys.stdout.write(output)
    return 0 if summary["pass"] else 1


def main() -> int:
    return run()


if __name__ == "__main__":
    raise SystemExit(main())
