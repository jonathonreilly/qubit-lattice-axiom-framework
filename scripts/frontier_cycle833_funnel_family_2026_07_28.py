#!/usr/bin/env python3
"""Cycle 833: exact census of the three k=2 cohort funnel states.

The Cycle-805/815/820/822/830/831 source primaries are SHA-pinned text/AST
controls only and are blocked from import.  Dynamics are rebuilt from the
landed Cycle-719 controller core.  Two entrants per cohort (plus exact
determinism duplicates) reconstruct the three funnel states, while the full
176-key catalog supplies the two-direction entry-predicate census.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
STDOUT_LIMIT_BYTES = 200 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle805_supply_relabeling_tournament_2026_07_28.py",
    "scripts/frontier_cycle815_per_origin_orbit_constraint_2026_07_28.py",
    "scripts/frontier_cycle820_shared_moment_mechanism_2026_07_28.py",
    "scripts/frontier_cycle822_sstar_basin_2026_07_28.py",
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
TEXT_AST_ONLY_PATHS = AUDIT_INPUT_PATHS[1:]
BLOCKLISTED_MODULES = tuple(Path(path).stem for path in TEXT_AST_ONLY_PATHS)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "04432816e3844043b419de8d91001003cd7fb8de76635658c3367574c3e44b9a",
    AUDIT_INPUT_PATHS[2]:
        "e064b2f431f3e125b8c7f8176e6331f3fee41c2d1dc8ba7e3e65ae97a4ebb6b0",
    AUDIT_INPUT_PATHS[3]:
        "7344bee5d5f0bcbddcea7b9d83f40a552c90188bf30b4905f2649a49e4bf1649",
    AUDIT_INPUT_PATHS[4]:
        "269d235c4981eaa4b94cfc200a0d472bf9f1ca8b57c2e14880afe754a9d41c56",
    AUDIT_INPUT_PATHS[5]:
        "b14262f6d54dc4f853bda13f321c816b3e762fa37b0b8276a2bec4955c51c481",
    AUDIT_INPUT_PATHS[6]:
        "624dad4d841e10e24891810dbc500cc4d6ebe871d6f09dd96f89e3189e52e2ff",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    AUDIT_INPUT_PATHS[1]: "075659d59588f7895e91f50f9ef93a368fb1fb4e",
    AUDIT_INPUT_PATHS[2]: "3fbfaf0019af05bbb3121de47de49b9cefec7571",
    AUDIT_INPUT_PATHS[3]: "6385dfa0dce58e86345483cc521ffa325e0d1cce",
    AUDIT_INPUT_PATHS[4]: "56fd26ec1f09e3690aa0e9cacd1447c289fd7ac0",
    AUDIT_INPUT_PATHS[5]: "1afe4941812f83f5e1fd5cc7c04e57231d703e8d",
    AUDIT_INPUT_PATHS[6]: "ef24edda08118c4e14439b899790fff6c6f94175",
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
            {"cyclic_map", "event_transport_rows", "mapping_table"},
        AUDIT_INPUT_PATHS[2]:
            {"origin_fiber_rotation", "origin_action_certificate"},
        AUDIT_INPUT_PATHS[3]:
            {"population_state_at_entry", "five_step_image",
             "mechanism_candidates"},
        AUDIT_INPUT_PATHS[4]:
            {"evolve_sstar_pair", "sstar_anatomy", "entry_predictors"},
        AUDIT_INPUT_PATHS[5]:
            {"decode_fixtures", "preimage_tree_certificate"},
        AUDIT_INPUT_PATHS[6]:
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
        "maximum_named_files": 7,
        "sha256": sha_rows,
        "expected_sha256": EXPECTED_SHA256,
        "git_blobs": blob_rows,
        "expected_git_blobs": EXPECTED_GIT_BLOBS,
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
        "funnel_moment": FUNNEL_MOMENTS[event],
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
