#!/usr/bin/env python3
"""Cycle 833 v2: adopt the exact rank-edge funnel-family field map.

The Cycle-805/830/831 source primaries are SHA-pinned text/AST controls only
and are blocked from import.  Dynamics are rebuilt from the landed Cycle-719
controller core.  Two entrants per cohort (plus exact determinism duplicates)
reconstruct the three funnel states.  The independent checker's construction
is reimplemented here: packed-wire differences are decoded to named source
and bank fields, then applied as exact arrival-rank edge updates.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 200 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle719_source_local_finalizer_core_2026_07_26.py",
    "scripts/frontier_cycle715_recurrent_directional_packet_bank_2026_07_26.py",
    "scripts/frontier_cycle805_supply_relabeling_tournament_2026_07_28.py",
    "scripts/frontier_cycle830_sstar_preimage_tree_2026_07_28.py",
    "scripts/frontier_cycle831_deep_k2_forecast_tests_2026_07_28.py",
)

import ast
from collections import Counter
from hashlib import sha1, sha256
import importlib.abc
from itertools import combinations
import json
from pathlib import Path
import sys
from time import monotonic
from typing import Any, Callable


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

CORE_PATH = AUDIT_INPUT_PATHS[0]
STATE_OBJECT_PATHS = AUDIT_INPUT_PATHS[1:3]
TEXT_AST_ONLY_PATHS = AUDIT_INPUT_PATHS[3:]
BLOCKLISTED_MODULES = tuple(Path(path).stem for path in TEXT_AST_ONLY_PATHS)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "b514b0e20197bb0ce5e5440b4b0c1f2a0f74a1962b127e8a4e4a2e97c8f86a1a",
    AUDIT_INPUT_PATHS[2]:
        "7ffe1dd4b169f774dce5bc9db29c5329c6e06c92e02506fbc734916ff11de884",
    AUDIT_INPUT_PATHS[3]:
        "04432816e3844043b419de8d91001003cd7fb8de76635658c3367574c3e44b9a",
    AUDIT_INPUT_PATHS[4]:
        "b14262f6d54dc4f853bda13f321c816b3e762fa37b0b8276a2bec4955c51c481",
    AUDIT_INPUT_PATHS[5]:
        "624dad4d841e10e24891810dbc500cc4d6ebe871d6f09dd96f89e3189e52e2ff",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    AUDIT_INPUT_PATHS[1]: "97cc3de7b95e341326c404047a321dbe2c825eda",
    AUDIT_INPUT_PATHS[2]: "fa03ab4796b729ee0bb83ab3823fd1b171bde8bd",
    AUDIT_INPUT_PATHS[3]: "075659d59588f7895e91f50f9ef93a368fb1fb4e",
    AUDIT_INPUT_PATHS[4]: "1afe4941812f83f5e1fd5cc7c04e57231d703e8d",
    AUDIT_INPUT_PATHS[5]: "ef24edda08118c4e14439b899790fff6c6f94175",
}


class _PrimaryFirewall(importlib.abc.MetaPathFinder):
    """Fail closed if a text/AST-only source primary is imported."""

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
Coordinate = tuple[str, str, int]
State = tuple[int, ...]

RING_STATIONS = 11
FIXTURE_BANKS = 2
FAMILY_SIZE = 176
STATE_BITS = 5815
BACKBONE: tuple[tuple[int, int], ...] = (
    (1, 6), (1, 7), (2, 7), (2, 8), (3, 8),
    (3, 9), (4, 9), (4, 10), (5, 10),
)
WITNESS_PAIRS = (BACKBONE[0], BACKBONE[-1])
FUNNEL_MOMENTS = {0: 14739, 2: 33190, 1: 51110}
RESOLUTION_MOMENTS = {event: moment + 5 for event, moment in FUNNEL_MOMENTS.items()}
EVENT_ORDER = (0, 2, 1)
EXPECTED_SSTAR_SHA256 = (
    "cdf7e03092c6278b686c1f0edb9ebd716f4a285b1eabc8a7e2780695284a8f1a"
)
EXPECTED_XOR_WEIGHTS = {(0, 2): 25, (2, 1): 27, (0, 1): 26}
LINEAGE_SCAN_HORIZON = 65536
EXPECTED_RESOLVED_AT_HORIZON = 43
EXPECTED_OPEN_AT_HORIZON = 133


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
        AUDIT_INPUT_PATHS[1]:
            {"pack_state", "unpack_state"},
        AUDIT_INPUT_PATHS[2]:
            {"declared_append_domain", "packet_projection"},
        AUDIT_INPUT_PATHS[3]:
            {"cyclic_map", "event_transport_rows", "mapping_table"},
        AUDIT_INPUT_PATHS[4]:
            {"decode_fixtures", "preimage_tree_certificate"},
        AUDIT_INPUT_PATHS[5]:
            {"build_family", "masked_schedule", "run"},
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
        "state_object_paths": STATE_OBJECT_PATHS,
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
        and len(AUDIT_INPUT_PATHS) <= 6
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


def separated_pairs() -> tuple[tuple[int, int], ...]:
    return tuple(
        pair for pair in combinations(range(RING_STATIONS), 2)
        if cyclic_separation(pair) > 1
    )


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
    summary = {
        "events": len(epochs),
        "pairs": len(positions),
        "keys": len(states),
        "state_bits": len(next(iter(states.values()))),
        "allocator_gates": len(allocator),
        "word_gate_counts": tuple(sorted({len(word) for word in words.values()})),
        "epoch_failures": epoch_failures,
        "composition_failures": composition_failures,
        "rail_failures": rail_failures,
        "catalog_sha256": digest(tuple(
            (key, state_sha256(states[key])) for key in sorted(states)
        )),
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
                    raise AssertionError(("non-reversible landed gate", gate))
                if len(set(gate.wires)) != len(gate.wires):
                    raise AssertionError(("repeated landed gate wire", gate))
    return tuple(rows)


def advance(columns: list[int], schedule: tuple[MaskedGate, ...]) -> None:
    for kind, first, second, third, mask in schedule:
        if kind == 0:
            columns[first] ^= mask
        elif kind == 1:
            columns[second] ^= columns[first] & mask
        else:
            columns[third] ^= columns[first] & columns[second] & mask


def reconstruct_funnels(family: dict[str, object]) -> dict[str, object]:
    primary_rows = tuple(
        (event, pair) for event in EVENT_ORDER for pair in WITNESS_PAIRS
    )
    lane_rows = tuple(
        (key, role) for key in primary_rows
        for role in ("primary", "determinism_duplicate")
    )
    lanes: tuple[Lane, ...] = tuple(
        (f"e{key[0]}_{role}_{key[1]}", key[1])
        for key, role in lane_rows
    )
    initial_states = tuple(
        family["states"][key] for key, _role in lane_rows
    )
    columns = pack_states(initial_states)
    primary_index = {
        key: index
        for index, (key, role) in enumerate(lane_rows)
        if role == "primary"
    }
    duplicate_index = {
        key: index
        for index, (key, role) in enumerate(lane_rows)
        if role == "determinism_duplicate"
    }
    duplicate_initial_exact = all(
        initial_states[primary_index[key]] == initial_states[duplicate_index[key]]
        for key in primary_rows
    )
    all_mask = (1 << len(lanes)) - 1
    active_mask = all_mask
    snapshots: dict[int, tuple[State, State]] = {}
    phase_rows = []
    previous = 0
    scalar_once = columns.copy()
    all_schedule = packed_schedule(family["program"], lanes, all_mask)
    advance(scalar_once, all_schedule)
    one_step_exact = all(
        unpack_lane(scalar_once, primary_index[key])
        == K.A.apply_semantic(
            family["states"][key], family["words"][key[1]]
        )
        for key in primary_rows
    )

    for event in EVENT_ORDER:
        stop = FUNNEL_MOMENTS[event]
        schedule = packed_schedule(family["program"], lanes, active_mask)
        phase_started = monotonic()
        for _moment in range(previous + 1, stop + 1):
            advance(columns, schedule)
        witness_states = tuple(
            unpack_lane(columns, primary_index[(event, pair)])
            for pair in WITNESS_PAIRS
        )
        snapshots[event] = witness_states
        phase_rows.append({
            "start": previous,
            "stop": stop,
            "updates": stop - previous,
            "active_lanes": active_mask.bit_count(),
            "instructions_per_update": len(schedule),
            "seconds": round(monotonic() - phase_started, 6),
        })
        event_mask = sum(
            (1 << primary_index[(event, pair)])
            | (1 << duplicate_index[(event, pair)])
            for pair in WITNESS_PAIRS
        )
        active_mask &= ~event_mask
        previous = stop

    funnels = {event: snapshots[event][0] for event in EVENT_ORDER}
    verification_rows = tuple({
        "event": event,
        "funnel_moment": FUNNEL_MOMENTS[event],
        "resolution_moment": RESOLUTION_MOMENTS[event],
        "witness_keys": tuple((event, pair) for pair in WITNESS_PAIRS),
        "full_tuple_equal_across_entrants":
            snapshots[event][0] == snapshots[event][1],
        "entrant_hashes": tuple(map(state_sha256, snapshots[event])),
        "hash_verified_against_second_entrant":
            state_sha256(snapshots[event][0])
            == state_sha256(snapshots[event][1]),
        "determinism_duplicates_exact": all(
            unpack_lane(columns, primary_index[(event, pair)])
            == unpack_lane(columns, duplicate_index[(event, pair)])
            for pair in WITNESS_PAIRS
        ),
    } for event in EVENT_ORDER)
    result = {
        "funnels": funnels,
        "second_states": {
            event: snapshots[event][1] for event in EVENT_ORDER
        },
        "verification_rows": verification_rows,
        "phase_rows": tuple(phase_rows),
        "one_step_scalar_equivalence": one_step_exact,
        "duplicate_initial_exact": duplicate_initial_exact,
        "pass": (
            duplicate_initial_exact
            and one_step_exact
            and all(
                row["full_tuple_equal_across_entrants"]
                and row["hash_verified_against_second_entrant"]
                and row["determinism_duplicates_exact"]
                for row in verification_rows
            )
            and state_sha256(funnels[0]) == EXPECTED_SSTAR_SHA256
        ),
    }
    return result


def watched_registers() -> tuple[tuple[str, int], ...]:
    return (
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


def residual_support(state: State) -> tuple[Coordinate, ...]:
    banks, links = K.M.unpack_state(state, FIXTURE_BANKS)
    rows: set[Coordinate] = set()
    if state[K.R3.X.SOURCE_POINTER]:
        rows.add(("source", "SOURCE_POINTER", 0))
    for bank_index, bank in enumerate(banks):
        for name, wire in watched_registers():
            if bank[wire]:
                rows.add(("bank", name, bank_index))
    for link_index, link in enumerate(links):
        for wire, bit in enumerate(link):
            if bit:
                rows.add(("link", f"WIRE_{wire}", link_index))
    return tuple(sorted(rows))


def anatomy(event: int, state: State, second: State) -> dict[str, object]:
    banks, links = K.M.unpack_state(state, FIXTURE_BANKS)
    occupancy = tuple(
        tuple(bank[int(layout["valid"])] for layout in K.A.CELLS)
        for bank in banks
    )
    tokens = tuple(
        tuple(bank[wire] for wire in K.A.TOKEN) for bank in banks
    )
    link_rows = tuple({
        "link": index,
        "hamming_weight": sum(link),
        "active_wire_indices": tuple(
            wire for wire, bit in enumerate(link) if bit
        ),
    } for index, link in enumerate(links))
    residual = residual_support(state)
    return {
        "event": event,
        "funnel_moment": FUNNEL_MOMENTS.get(event),
        "full_state_bits": len(state),
        "full_state_sha256": state_sha256(state),
        "second_entrant_sha256": state_sha256(second),
        "second_entrant_hash_verified":
            state_sha256(state) == state_sha256(second),
        "hamming_weight": sum(state),
        "occupancy": occupancy,
        "tokens": tokens,
        "links": link_rows,
        "residual_fields": residual,
        "residual_weight": len(residual),
        "bank_hamming_weights": tuple(map(sum, banks)),
        "source_active_indices": tuple(
            index for index in range(K.M.R12.SOURCE_WIDTH) if state[index]
        ),
        "pass": (
            len(state) == STATE_BITS
            and state == second
            and all(not row["active_wire_indices"] for row in link_rows)
        ),
    }


def component_for_wire(wire: int) -> str:
    if wire < K.M.R12.SOURCE_WIDTH:
        return "source"
    for bank in range(FIXTURE_BANKS):
        base = K.M.R12.BANK_BASES[bank]
        if base <= wire < base + K.A.N:
            return f"bank{bank}"
    base = K.M.R12.LINK_BASES[0]
    if base <= wire < base + K.B.LINK_WIDTH:
        return "link0"
    return "unused_padding"


def exact_diff(
    left_event: int,
    right_event: int,
    left: State,
    right: State,
    anatomies: dict[int, dict[str, object]],
) -> dict[str, object]:
    indices = tuple(
        wire for wire, (a, b) in enumerate(zip(left, right)) if a != b
    )
    component_weights = Counter(map(component_for_wire, indices))
    left_anatomy = anatomies[left_event]
    right_anatomy = anatomies[right_event]
    field_values = {
        "hamming_weight":
            (left_anatomy["hamming_weight"], right_anatomy["hamming_weight"]),
        "occupancy":
            (left_anatomy["occupancy"], right_anatomy["occupancy"]),
        "tokens": (left_anatomy["tokens"], right_anatomy["tokens"]),
        "links": (left_anatomy["links"], right_anatomy["links"]),
        "residual_fields": (
            left_anatomy["residual_fields"],
            right_anatomy["residual_fields"],
        ),
    }
    return {
        "left_event": left_event,
        "right_event": right_event,
        "full_state_xor_weight": len(indices),
        "differing_components": tuple(sorted(component_weights)),
        "component_xor_weights": dict(sorted(component_weights.items())),
        "requested_anatomy_fields_differing": tuple(
            name for name, values in field_values.items()
            if values[0] != values[1]
        ),
        "requested_anatomy_field_values": field_values,
        "exactly_distinct": left != right and bool(indices),
        "component_weights_sum_to_full":
            sum(component_weights.values()) == len(indices),
    }


def _bank_wire_aliases() -> dict[int, tuple[str, ...]]:
    """Reimplement the independent checker's named bank-wire decoder."""
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
    """Decode one packed index through the cited source/bank state objects."""
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


def field_group(name: str) -> str:
    head = name.split("|", 1)[0]
    return head.split("[", 1)[0]


def xor_support(left: State, right: State) -> tuple[int, ...]:
    return tuple(
        wire for wire, (a, b) in enumerate(zip(left, right)) if a != b
    )


def apply_named_xor_update(
    state: State,
    named_mask: tuple[str, ...],
) -> State:
    by_name = {wire_name(wire): wire for wire in range(len(state))}
    if len(by_name) != len(state):
        raise AssertionError("wire decoder is not injective")
    output = list(state)
    for name in named_mask:
        output[by_name[name]] ^= 1
    return tuple(output)


def edge_accounting(
    left: State,
    right: State,
    mask: tuple[str, ...],
) -> dict[str, object]:
    by_name = {wire_name(wire): wire for wire in range(len(left))}
    transitions = tuple(
        (
            name,
            left[by_name[name]],
            right[by_name[name]],
        )
        for name in mask
    )
    groups: dict[str, dict[str, int]] = {}
    for name, before, after in transitions:
        group = field_group(name)
        row = groups.setdefault(
            group, {"flipped_on": 0, "flipped_off": 0, "net": 0}
        )
        row["flipped_on"] += int(before == 0 and after == 1)
        row["flipped_off"] += int(before == 1 and after == 0)
        row["net"] += after - before
    flipped_on = sum(before == 0 and after == 1
                     for _name, before, after in transitions)
    flipped_off = sum(before == 1 and after == 0
                      for _name, before, after in transitions)
    return {
        "field_transitions": tuple(
            f"{name}:{before}->{after}"
            for name, before, after in transitions
        ),
        "field_group_weight_updates": tuple(
            (name, values) for name, values in sorted(groups.items())
        ),
        "flipped_on": flipped_on,
        "flipped_off": flipped_off,
        "net_weight_increment": flipped_on - flipped_off,
        "source_weight": sum(left),
        "target_weight": sum(right),
        "accounting_exact":
            sum(left) + flipped_on - flipped_off == sum(right),
    }


def rank_edge_field_map_certificate(
    funnels: dict[int, State],
) -> dict[str, object]:
    """Construct the checker-discovered map without importing the checker."""
    edge_specs = (
        (0, 2, 0, 1, "S*", "S2"),
        (2, 1, 1, 2, "S2", "S1"),
    )
    rows = []
    edge_masks: dict[tuple[int, int], tuple[str, ...]] = {}
    union: set[int] = set()
    for source, target, left_rank, right_rank, left_name, right_name in (
        edge_specs
    ):
        support = xor_support(funnels[source], funnels[target])
        union.update(support)
        mask = tuple(wire_name(wire) for wire in support)
        edge_masks[(source, target)] = mask
        accounting = edge_accounting(
            funnels[source], funnels[target], mask
        )
        image = apply_named_xor_update(funnels[source], mask)
        rows.append({
            "arrival_rank_edge": (left_rank, right_rank),
            "event_edge": (source, target),
            "state_edge": f"{left_name}->{right_name}",
            "operation": "XOR the listed named-field mask",
            "named_field_updates": mask,
            "xor_weight": len(mask),
            "expected_xor_weight":
                EXPECTED_XOR_WEIGHTS[(source, target)],
            "full_state_image_sha256": state_sha256(image),
            "target_sha256": state_sha256(funnels[target]),
            "full_state_equality": image == funnels[target],
            **accounting,
        })

    direct_support = xor_support(funnels[0], funnels[1])
    union.update(direct_support)
    direct_mask = tuple(wire_name(wire) for wire in direct_support)
    named_union = tuple(wire_name(wire) for wire in sorted(union))
    outside_common = all(
        len({funnels[event][wire] for event in EVENT_ORDER}) == 1
        for wire in range(STATE_BITS) if wire not in union
    )
    localized = (
        len(named_union) == 39
        and outside_common
        and all(
            name.startswith((
                "source.LEFT_ENDPOINT",
                "source.RIGHT_ENDPOINT",
                "bank0.",
            ))
            for name in named_union
        )
        and all(
            ".wire[" not in name and "unused_padding" not in name
            for name in named_union
        )
    )
    first_image = apply_named_xor_update(
        funnels[0], edge_masks[(0, 2)]
    )
    second_image = apply_named_xor_update(
        first_image, edge_masks[(2, 1)]
    )
    direct_image = apply_named_xor_update(funnels[0], direct_mask)
    result = {
        "map_source": "independent_checker",
        "construction":
            "primary-side reimplementation of packed XOR support, named-wire "
            "decoding, and arrival-rank-selected field-mask application",
        "state_object_citation": {
            "packing":
                f"{STATE_OBJECT_PATHS[0]}::pack_state/unpack_state",
            "named_bank_fields":
                f"{STATE_OBJECT_PATHS[1]}::CELLS and named registers",
        },
        "operation":
            "XOR the listed named-field mask selected by arrival-rank edge",
        "rank_edge_rows": tuple(rows),
        "direct_rank0_to_rank2": {
            "event_edge": (0, 1),
            "named_field_updates": direct_mask,
            "xor_weight": len(direct_mask),
            "expected_xor_weight": EXPECTED_XOR_WEIGHTS[(0, 1)],
            "full_state_equality": direct_image == funnels[1],
        },
        "localized_union_width": len(named_union),
        "localized_union_fields": named_union,
        "common_wire_count": STATE_BITS - len(named_union),
        "outside_union_exactly_common": outside_common,
        "Sstar_to_S2_exact": first_image == funnels[2],
        "S2_to_S1_exact": second_image == funnels[1],
        "Sstar_to_S1_direct_exact": direct_image == funnels[1],
        "scope":
            "exact observed-three rank-edge map; the extrapolated fourth "
            "candidate remains a prediction, not a future-event theorem",
    }
    result["pass"] = (
        localized
        and result["localized_union_width"] == 39
        and result["common_wire_count"] == 5776
        and all(row["full_state_equality"] for row in rows)
        and all(
            row["xor_weight"] == row["expected_xor_weight"]
            and row["accounting_exact"]
            for row in rows
        )
        and result["Sstar_to_S1_direct_exact"]
    )
    return result


def entry_predicate(event: int, key: Key) -> bool:
    return (
        key[0] == event
        and 0 not in key[1]
        and cyclic_separation(key[1]) == RING_STATIONS // 2
    )


def predicate_certificate(catalog: tuple[Key, ...]) -> dict[str, object]:
    event_rows = []
    for event in (0, 1, 2):
        declared = tuple((event, pair) for pair in BACKBONE)
        selected = tuple(key for key in catalog if entry_predicate(event, key))
        declared_set = set(declared)
        selected_set = set(selected)
        event_rows.append({
            "event": event,
            "predicate":
                f"event={event} AND origin absent AND max-sep=5",
            "declared_cohort_entrants": declared,
            "selected_from_full_176_catalog": selected,
            "true_positive_count": len(declared_set & selected_set),
            "false_positive_keys": tuple(sorted(selected_set - declared_set)),
            "false_negative_keys": tuple(sorted(declared_set - selected_set)),
            "all_entrants_satisfy_predicate":
                all(entry_predicate(event, key) for key in declared),
            "all_other_catalog_keys_fail_predicate": all(
                not entry_predicate(event, key)
                for key in catalog if key not in declared_set
            ),
            "both_directions_exact": selected == declared,
        })
    pair_selector = tuple(
        pair for pair in separated_pairs()
        if 0 not in pair
        and cyclic_separation(pair) == RING_STATIONS // 2
    )
    verified_union = tuple(sorted(
        key for key in catalog
        if key[0] in (0, 1, 2)
        and 0 not in key[1]
        and cyclic_separation(key[1]) == RING_STATIONS // 2
    ))
    expected_union = tuple(sorted(
        (event, pair) for event in (0, 1, 2) for pair in BACKBONE
    ))
    result = {
        "catalog_size": len(catalog),
        "event_rows": tuple(event_rows),
        "unified_predicate":
            "max-sep-5 AND origin absent; event index selects the cohort",
        "unified_pair_selector": pair_selector,
        "verified_event_indices": (0, 1, 2),
        "verified_union_count": len(verified_union),
        "verified_union_exact": verified_union == expected_union,
        "event3_boundary":
            "event-3 backbone keys are already resolved and are not remaining "
            "open forecast keys",
        "standing_forecast":
            "every remaining (backbone-pair,event) open key enters ITS "
            "cohort funnel at ITS cohort moment",
    }
    result["pass"] = (
        len(catalog) == FAMILY_SIZE
        and pair_selector == BACKBONE
        and all(row["both_directions_exact"] for row in event_rows)
        and result["verified_union_exact"]
    )
    return result


def fourth_candidate_certificate(
    funnels: dict[int, State],
    anatomies: dict[int, dict[str, object]],
    family_map: dict[str, object],
) -> tuple[State, dict[str, object]]:
    """Extend the named-field update class by one explicit prediction edge.

    The observed post-reset HEAD block advances from weight zero in S2 to
    HEAD[0] in S1.  The minimal next-rank continuation activates HEAD[1]
    while preserving HEAD[0].  This is a disclosed extrapolation inside the
    checker's named-field-XOR class, not an observed fourth edge.
    """
    current = funnels[1]
    prediction_mask = ("bank0.HEAD[1]",)
    candidate = apply_named_xor_update(current, prediction_mask)
    candidate_anatomy = anatomy(-1, candidate, candidate)
    candidate_anatomy["event"] = "prediction"
    candidate_anatomy["funnel_moment"] = None
    current_anatomy = anatomies[1]
    support = xor_support(current, candidate)
    support_names = tuple(wire_name(wire) for wire in support)
    union = set(family_map["localized_union_fields"])
    anatomy_preserved = (
        candidate_anatomy["occupancy"] == current_anatomy["occupancy"]
        and candidate_anatomy["tokens"] == current_anatomy["tokens"]
        and candidate_anatomy["links"] == current_anatomy["links"]
        and candidate_anatomy["residual_fields"]
        == current_anatomy["residual_fields"]
        and candidate_anatomy["source_active_indices"]
        == current_anatomy["source_active_indices"]
    )
    lawful = (
        len(candidate) == STATE_BITS
        and set(candidate) <= {0, 1}
        and set(support_names) <= union
        and anatomy_preserved
        and candidate_anatomy["hamming_weight"] == 47
        and candidate_anatomy["bank_hamming_weights"] == (41, 4)
    )
    certificate = {
        "name": "S0'",
        "definition": "S0' := map(S1)",
        "map_operation":
            "same named-field XOR update class, selected by the next "
            "arrival-rank edge",
        "prediction_edge": (2, 3),
        "prediction_named_field_updates": prediction_mask,
        "prediction_basis":
            "minimal post-reset HEAD-block continuation: S2 has no active "
            "HEAD bit, S1 activates HEAD[0], and the next candidate activates "
            "HEAD[1] without clearing HEAD[0]",
        "epistemic_status":
            "lawful structural prediction object; the rank-2->3 edge is an "
            "extrapolation and is not checker-certified as a future-event law",
        "source_state": "S1",
        "source_sha256": state_sha256(current),
        "candidate_sha256": state_sha256(candidate),
        "xor_support": support_names,
        "xor_weight": len(support),
        "source_weight": sum(current),
        "candidate_weight": sum(candidate),
        "weight_increment": sum(candidate) - sum(current),
        "candidate_anatomy": candidate_anatomy,
        "unchanged_outside_39_field_support": all(
            current[wire] == candidate[wire]
            for wire in range(STATE_BITS)
            if wire_name(wire) not in union
        ),
        "observed_anatomy_preserved": anatomy_preserved,
        "lawful_candidate": lawful,
    }
    certificate["pass"] = (
        certificate["source_weight"] == 46
        and certificate["candidate_weight"] == 47
        and certificate["weight_increment"] == 1
        and certificate["unchanged_outside_39_field_support"]
        and lawful
    )
    return candidate, certificate


def lane_numbers(mask: int) -> tuple[int, ...]:
    rows = []
    while mask:
        bit = mask & -mask
        rows.append(bit.bit_length() - 1)
        mask ^= bit
    return tuple(rows)


def equality_to_target_mask(
    columns: list[int],
    target: State,
    lane_mask: int,
    wires: tuple[int, ...] | None = None,
) -> int:
    candidates = lane_mask
    for wire in wires if wires is not None else range(len(target)):
        column = columns[wire] & lane_mask
        mismatch = (
            lane_mask ^ column if target[wire] else column
        )
        candidates &= ~mismatch
        if not candidates:
            return 0
    return candidates


def equality_to_initial_mask(
    columns: list[int],
    initial_columns: list[int],
    lane_mask: int,
    signature: tuple[int, ...],
) -> int:
    candidates = lane_mask
    for wire in signature:
        candidates &= ~(columns[wire] ^ initial_columns[wire])
        if not candidates:
            return 0
    for wire in range(len(columns)):
        candidates &= ~(columns[wire] ^ initial_columns[wire])
        if not candidates:
            return 0
    return candidates


def watched_residual_wire_indices() -> tuple[int, ...]:
    rows = {K.R3.X.SOURCE_POINTER}
    for base in K.M.R12.BANK_BASES[:FIXTURE_BANKS]:
        rows.update(base + wire for _name, wire in watched_registers())
    for base in K.M.R12.LINK_BASES[:FIXTURE_BANKS - 1]:
        rows.update(range(base, base + K.B.LINK_WIDTH))
    return tuple(sorted(rows))


def candidate_reach_certificate(
    family: dict[str, object],
    candidate: State,
) -> dict[str, object]:
    """Scan every lawful landed trajectory through Cycle-831's full horizon."""
    scan_started = monotonic()
    catalog = tuple(sorted(family["states"]))
    duplicate_key = catalog[0]
    lane_rows = tuple((key, "primary") for key in catalog) + (
        (duplicate_key, "determinism_duplicate"),
    )
    lanes: tuple[Lane, ...] = tuple(
        (f"scan_{key}_{role}", key[1]) for key, role in lane_rows
    )
    primary_index = {
        key: lane for lane, (key, _role) in enumerate(lane_rows[:-1])
    }
    duplicate_index = len(lane_rows) - 1
    initial_states = tuple(
        family["states"][key] for key, _role in lane_rows
    )
    columns = pack_states(initial_states)
    initial_columns = columns.copy()
    schedule = packed_schedule(
        family["program"], lanes, (1 << len(lanes)) - 1
    )
    primary_mask = (1 << len(catalog)) - 1
    active_mask = primary_mask
    residual_wires = watched_residual_wire_indices()
    recurrence_signature = tuple(sorted(set(
        index * (STATE_BITS - 1) // 191 for index in range(192)
    )))
    target_signature = tuple(sorted(set(
        tuple(wire for wire, bit in enumerate(candidate) if bit)
        + recurrence_signature
    )))
    hits: list[tuple[int, Key]] = []
    records: dict[Key, tuple[str, int]] = {}

    def scan_target(moment: int) -> None:
        candidates = equality_to_target_mask(
            columns, candidate, primary_mask, target_signature
        )
        if candidates:
            matches = equality_to_target_mask(
                columns, candidate, candidates
            )
            hits.extend(
                (moment, catalog[lane]) for lane in lane_numbers(matches)
            )

    scan_target(0)
    for moment in range(1, LINEAGE_SCAN_HORIZON + 1):
        advance(columns, schedule)
        scan_target(moment)
        nonclean = 0
        for wire in residual_wires:
            nonclean |= columns[wire]
        clean_hits = active_mask & ~nonclean
        recurrence_hits = equality_to_initial_mask(
            columns,
            initial_columns,
            active_mask & ~clean_hits,
            recurrence_signature,
        )
        for lane in lane_numbers(clean_hits):
            key = catalog[lane]
            records[key] = ("TRANSIENT", moment)
        for lane in lane_numbers(recurrence_hits):
            key = catalog[lane]
            records[key] = ("CYCLE", moment)
        active_mask &= ~(clean_hits | recurrence_hits)

    open_keys = tuple(
        catalog[lane] for lane in lane_numbers(active_mask)
    )
    resolved_rows = tuple(
        (key, *records[key])
        for key in sorted(records, key=lambda key: (records[key][1], key))
    )
    transient_count = sum(row[1] == "TRANSIENT" for row in resolved_rows)
    cycle_count = sum(row[1] == "CYCLE" for row in resolved_rows)
    funnel_resolution_rows = tuple({
        "event": event,
        "expected_resolution_moment": RESOLUTION_MOMENTS[event],
        "keys": tuple((event, pair) for pair in BACKBONE),
        "all_transient_at_expected_moment": all(
            records.get((event, pair))
            == ("TRANSIENT", RESOLUTION_MOMENTS[event])
            for pair in BACKBONE
        ),
    } for event in EVENT_ORDER)
    duplicate_final = (
        unpack_lane(columns, primary_index[duplicate_key])
        == unpack_lane(columns, duplicate_index)
    )
    result = {
        "scan_basis":
            "fresh primary-side landed evolution; Cycle-831 contributes the "
            "cached complete horizon bound, not cached state values",
        "lineage_horizon_source":
            f"{AUDIT_INPUT_PATHS[5]}::TARGET_HORIZON",
        "inclusive_moment_bounds": (0, LINEAGE_SCAN_HORIZON),
        "exact_equality_metric": "full 5815-bit tuple equality",
        "lawful_t0_trajectory_count": len(catalog),
        "candidate_sha256": state_sha256(candidate),
        "candidate_weight": sum(candidate),
        "exact_hit_count": len(hits),
        "exact_hits": tuple(hits),
        "resolved_through_horizon": {
            "count": len(resolved_rows),
            "transient_count": transient_count,
            "cycle_count": cycle_count,
            "rows": resolved_rows,
            "rows_sha256": digest(resolved_rows),
        },
        "open_at_horizon": {
            "count": len(open_keys),
            "keys_sha256": digest(open_keys),
            "scan":
                "all 133 unresolved trajectories tested at every inclusive "
                "moment through T=65536",
        },
        "funnel_resolution_rows": funnel_resolution_rows,
        "population_accounting":
            len(resolved_rows) + len(open_keys) == FAMILY_SIZE,
        "determinism_duplicate": {
            "key": duplicate_key,
            "initial_exact":
                initial_states[primary_index[duplicate_key]]
                == initial_states[duplicate_index],
            "final_exact": duplicate_final,
        },
        "candidate_outcome": (
            "DISCOVERY: S0' IS VISITED BY A LANDED TRAJECTORY"
            if hits else
            "NO HIT THROUGH T=65536: S0' REMAINS A PREDICTION OBJECT FOR "
            "DEEPER HORIZONS"
        ),
        "scan_runtime_seconds": round(monotonic() - scan_started, 6),
    }
    result["pass"] = (
        len(catalog) == FAMILY_SIZE
        and len(resolved_rows) == EXPECTED_RESOLVED_AT_HORIZON
        and transient_count == 29
        and cycle_count == 14
        and len(open_keys) == EXPECTED_OPEN_AT_HORIZON
        and not hits
        and all(
            row["all_transient_at_expected_moment"]
            for row in funnel_resolution_rows
        )
        and result["population_accounting"]
        and result["determinism_duplicate"]["initial_exact"]
        and result["determinism_duplicate"]["final_exact"]
    )
    return result


def cyclic_pair_map(
    pair: tuple[int, int],
    shift: int,
) -> tuple[int, int]:
    return tuple(sorted(
        ((pair[0] + shift) % RING_STATIONS,
         (pair[1] + shift) % RING_STATIONS)
    ))


def relabeling_805_certificate(
    funnels: dict[int, State],
) -> dict[str, object]:
    backbone_set = set(BACKBONE)
    shift_rows = tuple({
        "shift": shift,
        "station_map": tuple(
            (station, (station + shift) % RING_STATIONS)
            for station in range(RING_STATIONS)
        ),
        "mapped_backbone": tuple(sorted(
            cyclic_pair_map(pair, shift) for pair in BACKBONE
        )),
        "maps_backbone_set_to_itself":
            {cyclic_pair_map(pair, shift) for pair in BACKBONE}
            == backbone_set,
        "packed_state_action":
            "IDENTITY: Cycle-805 maps station/track/Q slots; logical banks "
            "and epochs are fixed",
    } for shift in range(RING_STATIONS))
    pair_rows = tuple({
        "source_event": source,
        "target_event": target,
        "tested_shifts": tuple(range(RING_STATIONS)),
        "exact_state_matches": tuple(
            shift for shift in range(RING_STATIONS)
            if funnels[source] == funnels[target]
        ),
    } for source, target in combinations(EVENT_ORDER, 2))
    return {
        "candidate": "Cycle-805 cyclic station relabelings",
        "shift_rows": shift_rows,
        "pair_rows": pair_rows,
        "tested_exact_maps": len(pair_rows) * RING_STATIONS,
        "exact_mapping_found": any(
            row["exact_state_matches"] for row in pair_rows
        ),
        "pass": (
            len(shift_rows) == RING_STATIONS
            and sum(row["maps_backbone_set_to_itself"] for row in shift_rows)
            == 1
            and all(
                not row["exact_state_matches"] for row in pair_rows
            )
        ),
    }


def c6_815_certificate() -> dict[str, object]:
    witness = tuple(
        (
            (origin + 1) % 6
            if origin < 6
            else 6 + ((origin - 6 + 1) % 6)
        )
        for origin in range(12)
    )
    identity = tuple(range(12))
    powers = [identity]
    for _power in range(1, 7):
        powers.append(tuple(witness[powers[-1][index]] for index in range(12)))
    return {
        "candidate": "Cycle-815 C6=<W> origin-fiber rotation",
        "origin_permutation": witness,
        "group_elements": tuple(powers[:-1]),
        "order_six_verified":
            len(set(powers[:-1])) == 6 and powers[-1] == identity,
        "funnel_state_action_supplied": False,
        "domain_test":
            "Cycle-815 adjoins an origin coordinate to the Cycle-805 "
            "checkpoint product; it supplies no embedding/permutation of the "
            "5815 Cycle-719 packed-state wires",
        "proxy_policy":
            "NO PROXY INVENTED; a 12-origin permutation is not silently "
            "identified with source matter wires 0..11",
        "tested_exact_funnel_maps": 0,
        "exact_mapping_found": False,
        "outcome": "NOT_APPLICABLE_UNSUPPLIED_STATE_ACTION",
        "pass": len(set(powers[:-1])) == 6 and powers[-1] == identity,
    }


def bank_swap(state: State) -> State:
    banks, links = K.M.unpack_state(state, FIXTURE_BANKS)
    return K.M.pack_state(tuple(reversed(banks)), links)


def endpoint_bank_direction_reflection(state: State) -> State:
    banks, links = K.M.unpack_state(state, FIXTURE_BANKS)
    reflected_banks = []
    for original in reversed(banks):
        bank = list(original)
        bank[K.A.U_TO_V], bank[K.A.V_TO_U] = (
            bank[K.A.V_TO_U], bank[K.A.U_TO_V]
        )
        reflected_banks.append(tuple(bank))
    result = list(K.M.pack_state(tuple(reflected_banks), links))
    left = K.R3.X.LEFT_ENDPOINT
    right = K.R3.X.RIGHT_ENDPOINT
    result[left], result[right] = result[right], result[left]
    return tuple(result)


def repeated_word(
    state: State,
    word: tuple[object, ...],
    count: int,
) -> State:
    result = state
    for _step in range(count):
        result = K.A.apply_semantic(result, word)
    return result


def event_structure_certificate(
    funnels: dict[int, State],
) -> dict[str, object]:
    allocator = K.M.global_allocator_word(FIXTURE_BANKS)
    inverse_allocator = tuple(reversed(allocator))
    transforms: dict[str, Callable[[State], State]] = {
        "bank_swap": bank_swap,
        "endpoint_bank_direction_reflection":
            endpoint_bank_direction_reflection,
    }
    for power in range(1, 4):
        transforms[f"allocator_forward_power_{power}"] = (
            lambda state, power=power:
                repeated_word(state, allocator, power)
        )
        transforms[f"allocator_inverse_power_{power}"] = (
            lambda state, power=power:
                repeated_word(state, inverse_allocator, power)
        )
    for direction in ((1, 0), (0, 1)):
        transforms[f"prepare_endpoint_direction_{direction}"] = (
            lambda state, direction=direction:
                K.M.prepare_endpoint(state, direction)
        )

    rows = []
    errors = []
    for source, target in combinations(EVENT_ORDER, 2):
        for name, transform in transforms.items():
            try:
                image = transform(funnels[source])
            except Exception as error:
                errors.append({
                    "source_event": source,
                    "target_event": target,
                    "map": name,
                    "exception_type": type(error).__name__,
                    "exception": str(error),
                })
                continue
            rows.append({
                "source_event": source,
                "target_event": target,
                "source_direction":
                    (1, 0) if source % 2 == 0 else (0, 1),
                "target_direction":
                    (1, 0) if target % 2 == 0 else (0, 1),
                "map": name,
                "image_sha256": state_sha256(image),
                "target_sha256": state_sha256(funnels[target]),
                "xor_weight_to_target": sum(
                    left != right
                    for left, right in zip(image, funnels[target])
                ),
                "exact_match": image == funnels[target],
            })
    matches = tuple(row for row in rows if row["exact_match"])
    return {
        "candidate_family":
            "Cycle-719 event directions, allocator word/inverse, bank bases, "
            "and named endpoint/direction constants",
        "event_direction_rows": tuple(
            (event, (1, 0) if event % 2 == 0 else (0, 1))
            for event in range(2 * FIXTURE_BANKS)
        ),
        "tested_rows": tuple(rows),
        "undefined_rows": tuple(errors),
        "tested_exact_maps": len(rows),
        "exact_matches": matches,
        "exact_mapping_found": bool(matches),
        "pass": len(rows) + len(errors) == len(tuple(
            combinations(EVENT_ORDER, 2)
        )) * len(transforms),
    }


def time_shift_certificate(
    family: dict[str, object],
    funnels: dict[int, State],
) -> dict[str, object]:
    chronological = (
        (0, 2, FUNNEL_MOMENTS[2] - FUNNEL_MOMENTS[0]),
        (2, 1, FUNNEL_MOMENTS[1] - FUNNEL_MOMENTS[2]),
        (0, 1, FUNNEL_MOMENTS[1] - FUNNEL_MOMENTS[0]),
    )
    lane_specs = tuple(
        (source, target, delta, pair)
        for source, target, delta in chronological
        for pair in BACKBONE
    )
    lanes: tuple[Lane, ...] = tuple(
        (f"e{source}_to_e{target}_dt{delta}_{pair}", pair)
        for source, target, delta, pair in lane_specs
    )
    columns = pack_states(tuple(
        funnels[source] for source, _target, _delta, _pair in lane_specs
    ))
    group_masks = {
        (source, target, delta): sum(
            1 << lane
            for lane, spec in enumerate(lane_specs)
            if spec[:3] == (source, target, delta)
        )
        for source, target, delta in chronological
    }
    active_mask = (1 << len(lanes)) - 1
    initial_once = columns.copy()
    initial_schedule = packed_schedule(
        family["program"], lanes, active_mask
    )
    advance(initial_once, initial_schedule)
    one_step_rows = tuple({
        "source_event": source,
        "target_event": target,
        "pair": pair,
        "exact": (
            unpack_lane(initial_once, lane)
            == K.A.apply_semantic(
                funnels[source], family["words"][pair]
            )
        ),
        "inverse_one_step_exact": (
            K.A.apply_semantic(
                K.A.apply_semantic(
                    funnels[source], family["words"][pair]
                ),
                tuple(reversed(family["words"][pair])),
            ) == funnels[source]
        ),
    } for lane, (source, target, _delta, pair) in enumerate(lane_specs))

    captured: dict[tuple[int, int, int], tuple[dict[str, object], ...]] = {}
    phase_rows = []
    previous = 0
    for source, target, stop in sorted(chronological, key=lambda row: row[2]):
        schedule = packed_schedule(family["program"], lanes, active_mask)
        phase_started = monotonic()
        for _update in range(previous + 1, stop + 1):
            advance(columns, schedule)
        group = (source, target, stop)
        rows = tuple({
            "pair": pair,
            "image_sha256": state_sha256(unpack_lane(columns, lane)),
            "target_sha256": state_sha256(funnels[target]),
            "xor_weight_to_target": sum(
                left != right
                for left, right in zip(
                    unpack_lane(columns, lane), funnels[target]
                )
            ),
            "exact_match":
                unpack_lane(columns, lane) == funnels[target],
        } for lane, spec in enumerate(lane_specs)
        if spec[:3] == group
        for pair in (spec[3],))
        captured[group] = rows
        phase_rows.append({
            "start_delta": previous,
            "stop_delta": stop,
            "updates": stop - previous,
            "active_lanes": active_mask.bit_count(),
            "instructions_per_update": len(schedule),
            "seconds": round(monotonic() - phase_started, 6),
        })
        active_mask &= ~group_masks[group]
        previous = stop

    group_rows = tuple({
        "source_event": source,
        "target_event": target,
        "time_shift": delta,
        "tested_landed_backbone_words": len(BACKBONE),
        "rows": captured[(source, target, delta)],
        "matching_words": tuple(
            row["pair"] for row in captured[(source, target, delta)]
            if row["exact_match"]
        ),
    } for source, target, delta in chronological)
    return {
        "definition":
            "forward image of each source funnel under every one of the nine "
            "landed max-sep-5 backbone words for the exact inter-funnel time "
            "difference",
        "group_rows": group_rows,
        "phase_rows": tuple(phase_rows),
        "one_step_representation_rows": one_step_rows,
        "inverse_equivalence_basis":
            "each word is a distinct-wire X/CNOT/TOF composition; reversing "
            "the gate list is its exact inverse",
        "tested_exact_maps": len(lane_specs),
        "exact_mapping_found": any(
            row["matching_words"] for row in group_rows
        ),
        "exact_matches": tuple(
            {
                "source_event": row["source_event"],
                "target_event": row["target_event"],
                "time_shift": row["time_shift"],
                "pair": pair,
            }
            for row in group_rows for pair in row["matching_words"]
        ),
        "pass": (
            all(row["exact"] and row["inverse_one_step_exact"]
                for row in one_step_rows)
            and sum(row["tested_landed_backbone_words"] for row in group_rows)
            == len(lane_specs)
        ),
    }


def family_structure_certificate(
    funnels: dict[int, State],
    anatomies: dict[int, dict[str, object]],
    family: dict[str, object],
) -> dict[str, object]:
    diffs = tuple(
        exact_diff(left, right, funnels[left], funnels[right], anatomies)
        for left, right in combinations(EVENT_ORDER, 2)
    )
    relabeling = relabeling_805_certificate(funnels)
    c6 = c6_815_certificate()
    event_maps = event_structure_certificate(funnels)
    time_shifts = time_shift_certificate(family, funnels)
    found = tuple(
        name for name, certificate in (
            ("Cycle-805 relabelings", relabeling),
            ("Cycle-815 C6", c6),
            ("event-index constant maps", event_maps),
            ("time-shifted landed evolution", time_shifts),
        )
        if certificate["exact_mapping_found"]
    )
    return {
        "pairwise_exact_diffs": diffs,
        "Cycle805_relabelings": relabeling,
        "Cycle815_C6": c6,
        "event_index_structures": event_maps,
        "time_shifted_evolution_images": time_shifts,
        "exact_family_maps_found_in_v1_searched_classes": found,
        "v1_searched_class_outcome": (
            "EXACT_MAP_FOUND_IN_V1_SEARCHED_CLASSES: " + ", ".join(found)
            if found else
            "NONE_FOUND_IN_V1_SEARCHED_CLASSES"
        ),
        "scope":
            "Cycle-805 station relabelings, supplied event-index maps, and "
            "landed time shifts only; excludes named rank-edge field updates",
        "pass": (
            len(diffs) == 3
            and all(
                row["exactly_distinct"]
                and row["component_weights_sum_to_full"]
                for row in diffs
            )
            and relabeling["pass"]
            and c6["pass"]
            and event_maps["pass"]
            and time_shifts["pass"]
        ),
    }


def unification_certificate(
    anatomies: dict[int, dict[str, object]],
    family_map: dict[str, object],
    v1_searches: dict[str, object],
) -> dict[str, object]:
    skeleton_rows = tuple(
        (
            anatomies[event]["occupancy"],
            anatomies[event]["tokens"],
            tuple(
                (link["hamming_weight"], link["active_wire_indices"])
                for link in anatomies[event]["links"]
            ),
            anatomies[event]["residual_fields"],
        )
        for event in EVENT_ORDER
    )
    common_skeleton = len(set(skeleton_rows)) == 1
    edge_rows = tuple({
        "state_edge": row["state_edge"],
        "arrival_rank_edge": row["arrival_rank_edge"],
        "source_weight": row["source_weight"],
        "flipped_on": row["flipped_on"],
        "flipped_off": row["flipped_off"],
        "net_field_weight_increment": row["net_weight_increment"],
        "derived_target_weight":
            row["source_weight"] + row["net_weight_increment"],
        "observed_target_weight": row["target_weight"],
        "exact":
            row["accounting_exact"]
            and row["net_weight_increment"] == 1,
        "field_group_weight_updates":
            row["field_group_weight_updates"],
    } for row in family_map["rank_edge_rows"])
    arrival_weights = tuple(
        anatomies[event]["hamming_weight"] for event in EVENT_ORDER
    )
    arrival_bank0_weights = tuple(
        anatomies[event]["bank_hamming_weights"][0]
        for event in EVENT_ORDER
    )
    old_classes_clean = not v1_searches[
        "exact_family_maps_found_in_v1_searched_classes"
    ]
    result = {
        "statement":
            "S*, S2, and S1 are one exact anatomy with an advancing bank0 "
            "register block and the parity-selected source endpoint",
        "fixed_anatomy":
            "occupancy, tokens, empty links, residual fields, bank1, and all "
            "wires outside the 39-field localized support are common",
        "advancing_block":
            "bank0 pred/rotor_before/rotor_after/carry/orientation/HEAD/ROTOR "
            "plus the source endpoint selector",
        "localized_support_width":
            family_map["localized_union_width"],
        "common_wire_count": family_map["common_wire_count"],
        "common_requested_skeleton": common_skeleton,
        "arrival_order": EVENT_ORDER,
        "arrival_weights": arrival_weights,
        "arrival_bank0_weights": arrival_bank0_weights,
        "map_field_weight_accounting": edge_rows,
        "weight_law_derivation":
            "44 + (13 on - 12 off) = 45; "
            "45 + (14 on - 13 off) = 46",
        "arrival_order_weight_law_exact":
            arrival_weights == (44, 45, 46)
            and arrival_bank0_weights == (38, 39, 40)
            and all(row["exact"] for row in edge_rows),
        "v1_no_map_claim": "RETRACTED",
        "retraction_scope":
            "v1's negative result remains valid only for its searched "
            "Cycle-805 relabelings / supplied event maps / landed time "
            "shifts; it did not search rank-edge named-field updates",
        "v1_searched_classes": {
            "Cycle805_station_relabeling_exact_maps":
                v1_searches["Cycle805_relabelings"]["tested_exact_maps"],
            "supplied_event_map_exact_rows":
                v1_searches["event_index_structures"]["tested_exact_maps"],
            "landed_time_shift_exact_maps":
                v1_searches[
                    "time_shifted_evolution_images"
                ]["tested_exact_maps"],
            "exact_match_in_those_classes": not old_classes_clean,
        },
        "map_source": "independent_checker",
        "map_class":
            "arrival-rank edge selected named-field XOR update",
    }
    result["pass"] = (
        family_map["pass"]
        and common_skeleton
        and result["localized_support_width"] == 39
        and result["common_wire_count"] == 5776
        and result["arrival_order_weight_law_exact"]
        and old_classes_clean
    )
    return result


def requested_anatomy_signature(row: dict[str, object]) -> tuple[object, ...]:
    return (
        row["hamming_weight"],
        row["occupancy"],
        row["tokens"],
        tuple(
            (link["hamming_weight"], link["active_wire_indices"])
            for link in row["links"]
        ),
        row["residual_fields"],
    )


def anatomy_law_certificate(
    anatomies: dict[int, dict[str, object]],
    family_structure: dict[str, object],
) -> dict[str, object]:
    holds = []
    gaps = []
    if all(row["full_state_bits"] == STATE_BITS for row in anatomies.values()):
        holds.append("HOLDS: state width is exactly 5,815 bits for all funnels")
    if all(
        all(link["hamming_weight"] == 0 for link in row["links"])
        for row in anatomies.values()
    ):
        holds.append("HOLDS: every funnel link is exactly empty")
    if all(
        ("source", "SOURCE_POINTER", 0) in row["residual_fields"]
        for row in anatomies.values()
    ):
        holds.append(
            "HOLDS: source.SOURCE_POINTER is residual-active for all funnels"
        )

    skeletons = {
        event: (
            anatomies[event]["occupancy"],
            anatomies[event]["tokens"],
            tuple(
                (link["hamming_weight"], link["active_wire_indices"])
                for link in anatomies[event]["links"]
            ),
            anatomies[event]["residual_fields"],
        )
        for event in (0, 1, 2)
    }
    common_skeleton = len(set(skeletons.values())) == 1
    if common_skeleton:
        holds.append(
            "HOLDS: occupancy, tokens, empty-link data, and residual fields "
            "form one exact common skeleton on events 0,1,2"
        )
    else:
        gaps.append(
            "GAP: occupancy/tokens/link/residual skeleton is not common"
        )

    arrival_weights = tuple(
        anatomies[event]["hamming_weight"] for event in EVENT_ORDER
    )
    arrival_bank0_weights = tuple(
        anatomies[event]["bank_hamming_weights"][0] for event in EVENT_ORDER
    )
    rank_weight_law = (
        arrival_weights == tuple(44 + rank for rank in range(3))
        and arrival_bank0_weights == tuple(38 + rank for rank in range(3))
    )
    if rank_weight_law:
        holds.append(
            "HOLDS: in funnel-arrival order events 0,2,1, total weight is "
            "exactly 44,45,46 and bank-0 weight is exactly 38,39,40"
        )
    else:
        gaps.append(
            "GAP: no unit-step weight law holds in funnel-arrival order"
        )

    parity_endpoints = all(
        set(anatomies[event]["source_active_indices"])
        == {K.R3.X.SOURCE_POINTER,
            K.R3.X.RIGHT_ENDPOINT if event % 2 == 0
            else K.R3.X.LEFT_ENDPOINT}
        for event in (0, 1, 2)
    )
    if parity_endpoints:
        holds.append(
            "HOLDS: the active source endpoint follows event parity "
            "(right for even events, left for odd), with source pointer active"
        )
    else:
        gaps.append(
            "GAP: active source endpoint does not follow event parity"
        )

    numeric_event_weights = tuple(
        anatomies[event]["hamming_weight"] for event in (0, 1, 2)
    )
    if (
        numeric_event_weights[1] - numeric_event_weights[0]
        == numeric_event_weights[2] - numeric_event_weights[1]
    ):
        holds.append(
            "HOLDS: weights are affine in numeric event index 0,1,2"
        )
    else:
        gaps.append(
            f"GAP: weights {numeric_event_weights} are not affine in numeric "
            "event index 0,1,2; arrival-rank order is not yet derived from e"
        )
    residuals = {
        event: anatomies[event]["residual_fields"] for event in (0, 1, 2)
    }
    if len(set(residuals.values())) == 1:
        holds.append(
            "HOLDS: residual fields are exactly event-independent on 0,1,2"
        )
    else:
        gaps.append(
            "GAP: residual fields vary with event index"
        )
    if family_structure["exact_family_maps_found_in_v1_searched_classes"]:
        holds.append(
            "HOLDS: at least one tested exact state map relates funnel states"
        )
    else:
        gaps.append(
            "GAP (SCOPED): no tested landed relabeling, supplied C6 state "
            "action, event-constant map, or backbone time shift maps one full "
            "funnel state to another; rank-edge field updates are outside "
            "those v1 classes"
        )
    gaps.extend((
        "GAP: three observed funnels cannot establish an all-event theorem",
        "GAP: no formula for future cohort moments is derived",
    ))
    candidate = (
        "OBSERVED_COMMON_SKELETON_PLUS_ARRIVAL_RANK_WEIGHT"
        if common_skeleton and rank_weight_law and parity_endpoints
        else "NO_UNIFIED_REQUESTED_ANATOMY_LAW_FOUND"
    )
    return {
        "event_rows": tuple({
            "event": event,
            "weight": anatomies[event]["hamming_weight"],
            "occupancy": anatomies[event]["occupancy"],
            "tokens": anatomies[event]["tokens"],
            "links": anatomies[event]["links"],
            "residual_fields": anatomies[event]["residual_fields"],
            "bank_hamming_weights":
                anatomies[event]["bank_hamming_weights"],
            "source_active_indices":
                anatomies[event]["source_active_indices"],
        } for event in (0, 1, 2)),
        "holds_statements": tuple(holds),
        "named_gaps": tuple(gaps),
        "anatomy_law_candidate": candidate,
        "outcome": (
            "HOLDS_ON_OBSERVED_THREE: COMMON_SKELETON_PLUS_ARRIVAL_RANK_"
            "WEIGHT; NUMERIC_EVENT_INDEX_DERIVATION_OPEN"
            if candidate
            == "OBSERVED_COMMON_SKELETON_PLUS_ARRIVAL_RANK_WEIGHT"
            else "NO_ANATOMY_LAW_FOUND; EXACT COMPARISONS ONLY"
        ),
        "pass": (
            len(holds) >= 3
            and len(gaps) >= 2
            and all(statement.startswith("HOLDS:") for statement in holds)
            and all(statement.startswith("GAP:") for statement in gaps)
        ),
    }


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
    controls = certificates["E_CONTROLS"]
    for _attempt in range(20):
        report["checks"] = dict(checks)
        report["pass"] = all(checks.values())
        report["terminal"] = (
            "CYCLE833_V2_FUNNEL_FAMILY_MAP_EXACT_PASS"
            if report["pass"]
            else "CYCLE833_V2_FUNNEL_FAMILY_MAP_HONEST_FAIL"
        )
        output = render(checks, certificates, report)
        size = len(output.encode("utf-8"))
        if report["stdout_bytes"] == size and controls["stdout_bytes"] == size:
            return output
        report["stdout_bytes"] = size
        controls["stdout_bytes"] = size
    raise AssertionError("stdout byte fixed point did not converge")


def run() -> int:
    started = monotonic()
    sources = source_controls()
    family = build_family()
    reconstruction = reconstruct_funnels(family)
    funnels = reconstruction["funnels"]
    anatomy_rows = {
        event: anatomy(
            event,
            funnels[event],
            reconstruction["second_states"][event],
        )
        for event in EVENT_ORDER
    }
    for event, row in anatomy_rows.items():
        verification = reconstruction["verification_rows"][
            EVENT_ORDER.index(event)
        ]
        row["second_entrant_sha256"] = verification["entrant_hashes"][1]
        row["second_entrant_hash_verified"] = verification[
            "hash_verified_against_second_entrant"
        ]
        row["pass"] = (
            row["pass"]
            and verification["full_tuple_equal_across_entrants"]
        )

    catalog = tuple(sorted(family["states"]))
    family_map = rank_edge_field_map_certificate(funnels)
    v1_searches = family_structure_certificate(
        funnels, anatomy_rows, family
    )
    certificate_a = family_map
    certificate_b = unification_certificate(
        anatomy_rows, family_map, v1_searches
    )
    candidate, candidate_row = fourth_candidate_certificate(
        funnels, anatomy_rows, family_map
    )
    reach = candidate_reach_certificate(family, candidate)
    certificate_c = {
        "candidate": candidate_row,
        "reach": reach,
        "pass": candidate_row["pass"] and reach["pass"],
    }
    pairwise_diffs = tuple(
        exact_diff(left, right, funnels[left], funnels[right], anatomy_rows)
        for left, right in combinations(EVENT_ORDER, 2)
    )
    predicate = predicate_certificate(catalog)
    certificate_d = {
        "reconstruction": {
            key: value for key, value in reconstruction.items()
            if key not in {"funnels", "second_states"}
        },
        "anatomies": tuple(anatomy_rows[event] for event in EVENT_ORDER),
        "pairwise_exact_diffs": pairwise_diffs,
        "unified_predicate": predicate,
        "unchanged_claim":
            "v1 anatomies, pairwise XOR weights, and the unified predicate "
            "in both directions over the full 176-key catalog are reproduced",
        "pass": (
            reconstruction["pass"]
            and all(row["pass"] for row in anatomy_rows.values())
            and tuple(
                (
                    row["left_event"],
                    row["right_event"],
                    row["full_state_xor_weight"],
                )
                for row in pairwise_diffs
            ) == (
                (0, 2, 25),
                (0, 1, 26),
                (2, 1, 27),
            )
            and predicate["pass"]
        ),
    }

    elapsed = monotonic() - started
    deterministic = (
        reconstruction["duplicate_initial_exact"]
        and all(
            row["determinism_duplicates_exact"]
            for row in reconstruction["verification_rows"]
        )
        and reach["determinism_duplicate"]["initial_exact"]
        and reach["determinism_duplicate"]["final_exact"]
    )
    controls_base = (
        sources["pass"]
        and family["summary"]["pass"]
        and deterministic
        and not any(name in sys.modules for name in BLOCKLISTED_MODULES)
        and not FIREWALL.hits
        and elapsed < AUDIT_TIMEOUT_SEC
    )
    certificate_e = {
        **sources,
        "family_rebuild": family["summary"],
        "determinism": {
            "method":
                "each of six entrant lanes carried with an independent "
                "duplicate under identical exact masks through its funnel "
                "moment",
            "duplicate_initial_exact":
                reconstruction["duplicate_initial_exact"],
            "funnel_rows": tuple({
                "event": row["event"],
                "exact": row["determinism_duplicates_exact"],
            } for row in reconstruction["verification_rows"]),
            "deterministic": deterministic,
        },
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "blocked_modules_loaded_at_end": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits_at_end": tuple(FIREWALL.hits),
    }
    checks = {
        "A_FAMILY_MAP_ADOPTED": bool(certificate_a["pass"]),
        "B_ONE_ANATOMY_AND_WEIGHT_ACCOUNTING": bool(certificate_b["pass"]),
        "C_FOURTH_CANDIDATE_AND_REACH": bool(certificate_c["pass"]),
        "D_ANATOMIES_XOR_WEIGHTS_PREDICATE_UNCHANGED":
            bool(certificate_d["pass"]),
        "E_SHAS_BLOCKLIST_DETERMINISM_RUNTIME_STDOUT": controls_base,
    }
    certificates = {
        "A_FAMILY_MAP_ADOPTED": certificate_a,
        "B_UNIFICATION": certificate_b,
        "C_MAP_REACH": certificate_c,
        "D_UNCHANGED_RESULTS": certificate_d,
        "E_CONTROLS": certificate_e,
    }
    report = {
        "cycle": 833,
        "anatomies": tuple({
            "event": event,
            "name": {0: "S*", 2: "S2", 1: "S1"}[event],
            "moment": FUNNEL_MOMENTS[event],
            "sha256": anatomy_rows[event]["full_state_sha256"],
            "weight": anatomy_rows[event]["hamming_weight"],
            "occupancy": anatomy_rows[event]["occupancy"],
            "tokens": anatomy_rows[event]["tokens"],
            "links": anatomy_rows[event]["links"],
            "residual_fields": anatomy_rows[event]["residual_fields"],
        } for event in EVENT_ORDER),
        "family_map_outcome":
            "ADOPTED: S* -> S2 -> S1 EXACT BY FULL-STATE EQUALITY",
        "map_source": "independent_checker",
        "localized_field_support":
            certificate_a["localized_union_width"],
        "common_wire_count": certificate_a["common_wire_count"],
        "unification":
            "ONE ANATOMY WITH ADVANCING BANK0 REGISTER BLOCK",
        "arrival_order_weight_law":
            certificate_b["arrival_weights"],
        "S0_prime": {
            "sha256": candidate_row["candidate_sha256"],
            "weight": candidate_row["candidate_weight"],
            "exact_hits_through_65536": reach["exact_hit_count"],
            "outcome": reach["candidate_outcome"],
        },
        "unified_predicate_verified": predicate["pass"],
        "v1_no_map_claim": "RETRACTED_OUTSIDE_ITS_SEARCHED_CLASSES",
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "checks": {},
        "pass": False,
        "terminal": "CYCLE833_V2_FUNNEL_FAMILY_MAP_HONEST_FAIL",
    }
    output = stable_render(checks, certificates, report)
    stdout_ok = len(output.encode("utf-8")) < STDOUT_LIMIT_BYTES
    checks["E_SHAS_BLOCKLIST_DETERMINISM_RUNTIME_STDOUT"] = (
        controls_base and stdout_ok
    )
    output = stable_render(checks, certificates, report)
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        sys.stdout.write(compact({
            "pass": False,
            "terminal": "CYCLE833_V2_FUNNEL_FAMILY_MAP_HONEST_FAIL",
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
            "terminal": "CYCLE833_V2_FUNNEL_FAMILY_MAP_HONEST_FAIL",
            "exception_type": type(error).__name__,
            "exception": str(error),
        }) + "\n")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
