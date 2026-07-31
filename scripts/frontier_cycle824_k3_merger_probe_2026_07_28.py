#!/usr/bin/env python3
"""Cycle 824: exact k=3 merger, cycle-shift, and cross-stratum probe.

Only the landed Cycle-719 controller core is executable science input.  The
Cycle-798/801/814/820 source primaries are pinned worktree files, parsed only
as text/AST, and blocked from import.  All trajectory evolution and equality
tests are independently reimplemented here.

Horizon indices count complete fixed-word controller orbits after the
canonical postimage.  Full-state equality is exact byte-tuple equality;
SHA-256 values are compact labels only and never establish equality.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
STDOUT_LIMIT_BYTES = 200 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle798_higher_k_horizon_scan_2026_07_28.py",
    "scripts/frontier_cycle801_silent_strata_deep_scan_2026_07_28.py",
    "scripts/frontier_cycle814_deep_silence_probe_2026_07_28.py",
    "scripts/frontier_cycle820_shared_moment_mechanism_2026_07_28.py",
)

import ast
import gc
from hashlib import sha1, sha256
import importlib.abc
from itertools import combinations
import json
from pathlib import Path
import sys
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

REFERENCE_PRIMARY_PATHS = AUDIT_INPUT_PATHS[1:]
BLOCKLISTED_MODULES = tuple(
    Path(path).stem for path in REFERENCE_PRIMARY_PATHS
)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "f6ec49636ecb7ec09808eed7d38f2085f6145cd383c306370502c547741942b1",
    AUDIT_INPUT_PATHS[2]:
        "55edc0cc8b3e51de3863819f10303d506e0652dbc031a1f2647c3a11e51cb115",
    AUDIT_INPUT_PATHS[3]:
        "f023d10784506e0c9ffbb39b17c3f120af78f377f27c5dab93de9a9aebaa98c0",
    AUDIT_INPUT_PATHS[4]:
        "7344bee5d5f0bcbddcea7b9d83f40a552c90188bf30b4905f2649a49e4bf1649",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    AUDIT_INPUT_PATHS[1]: "9de34ad5adcbf484d4f0c7e6aec13375ed465aab",
    AUDIT_INPUT_PATHS[2]: "8807587899a5664d39a06901b02b22041682c5cc",
    AUDIT_INPUT_PATHS[3]: "19ba617ad1f6be9f8fdc637b764dc7b38cae8d7b",
    AUDIT_INPUT_PATHS[4]: "6385dfa0dce58e86345483cc521ffa325e0d1cce",
}
REQUIRED_REFERENCE_FUNCTIONS = {
    AUDIT_INPUT_PATHS[1]: {
        "build_zero_survivor_catalog",
        "scan_key",
        "synchronous_composition_word",
    },
    AUDIT_INPUT_PATHS[2]: {
        "advance_one_record",
        "initialise_catalog_records",
    },
    AUDIT_INPUT_PATHS[3]: {
        "apply_bit_sliced_word",
        "verify_terminal_event",
    },
    AUDIT_INPUT_PATHS[4]: {
        "evolve_nine",
        "mechanism_candidates",
    },
}


class _BlocklistFinder(importlib.abc.MetaPathFinder):
    """Fail closed if any source primary is imported."""

    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(
        self,
        fullname: str,
        path: object = None,
        target: object = None,
    ) -> None:
        if fullname in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids import of {fullname}")
        return None


IMPORT_FIREWALL = _BlocklistFinder()
sys.meta_path.insert(0, IMPORT_FIREWALL)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


RING_STATIONS = 11
FIXTURE_BANKS = 2
STATE_WIDTH_EXPECTED = 5815
K3_EXPECTED_ZERO_ROWS = 18
K3_EXPECTED_TRANSIENT_MOMENTS = (444, 532, 681, 1385)
TRANSIENT_SCAN_END = max(K3_EXPECTED_TRANSIENT_MOMENTS)
FUNNEL_LAGS = tuple(range(1, 9))
K3_CYCLE_PERIOD = 5952
K3_CYCLE_KEYS = (
    (3, (0, 2, 5), 1),
    (3, (0, 2, 6), 1),
    (3, (0, 2, 7), 1),
    (3, (0, 2, 8), 1),
)
K2_SSTAR_KEY = (2, (1, 6), 0)
K2_SSTAR_TIME = 14739

Key = tuple[int, tuple[int, ...], int]
CompiledWord = tuple[tuple[int, int, int, int], ...]
StateBytes = bytes


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def state_sha256(state: StateBytes) -> str:
    return sha256(state).hexdigest()


def git_blob_sha(payload: bytes) -> str:
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


def source_certificate() -> dict[str, object]:
    payloads = {
        path: (ROOT / path).read_bytes()
        for path in AUDIT_INPUT_PATHS
        if (ROOT / path).is_file()
    }
    trees = {
        path: ast.parse(payload, filename=path)
        for path, payload in payloads.items()
    }
    actual_sha = {
        path: sha256(payload).hexdigest()
        for path, payload in payloads.items()
    }
    actual_blobs = {
        path: git_blob_sha(payload)
        for path, payload in payloads.items()
    }
    reference_ast_rows = {}
    for path in REFERENCE_PRIMARY_PATHS:
        names = {
            node.name
            for node in trees[path].body
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        }
        reference_ast_rows[path] = {
            "required_functions":
                tuple(sorted(REQUIRED_REFERENCE_FUNCTIONS[path])),
            "required_functions_present":
                REQUIRED_REFERENCE_FUNCTIONS[path] <= names,
            "mode": "TEXT_AST_ONLY_BLOCKLISTED",
        }

    self_payload = Path(__file__).read_bytes()
    self_tree = ast.parse(self_payload, filename=Path(__file__).name)
    direct_frontier_imports = {
        alias.name
        for node in self_tree.body
        if isinstance(node, ast.Import)
        for alias in node.names
        if alias.name.startswith("frontier_cycle")
    }
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_INPUT_PATHS_literal":
            literal_assignment(self_tree, "AUDIT_INPUT_PATHS")
            == AUDIT_INPUT_PATHS,
        "path_count": len(AUDIT_INPUT_PATHS),
        "maximum_path_count": 6,
        "existing_worktree_relative": (
            len(payloads) == len(AUDIT_INPUT_PATHS)
            and all(
                not Path(path).is_absolute() and (ROOT / path).is_file()
                for path in AUDIT_INPUT_PATHS
            )
        ),
        "sha256": actual_sha,
        "expected_sha256": EXPECTED_SHA256,
        "git_blobs": actual_blobs,
        "expected_git_blobs": EXPECTED_GIT_BLOBS,
        "cycle820_copy": {
            "path": AUDIT_INPUT_PATHS[4],
            "sha256": actual_sha.get(AUDIT_INPUT_PATHS[4]),
            "git_blob": actual_blobs.get(AUDIT_INPUT_PATHS[4]),
            "provenance":
                "../born-harness-worktree/scripts/"
                "frontier_cycle820_shared_moment_mechanism_2026_07_28.py",
            "tracked_copy_required": True,
        },
        "reference_AST": reference_ast_rows,
        "blocked_modules": BLOCKLISTED_MODULES,
        "blocked_modules_loaded": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits": tuple(IMPORT_FIREWALL.hits),
        "direct_frontier_imports": tuple(sorted(direct_frontier_imports)),
        "runner_dependency_policy":
            "stdlib direct imports plus sole landed repository core Cycle-719",
    }
    result["pass"] = (
        result["AUDIT_INPUT_PATHS_literal"]
        and result["path_count"] <= result["maximum_path_count"]
        and result["existing_worktree_relative"]
        and actual_sha == EXPECTED_SHA256
        and actual_blobs == EXPECTED_GIT_BLOBS
        and all(
            row["required_functions_present"]
            for row in reference_ast_rows.values()
        )
        and direct_frontier_imports
        == {
            "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26"
        }
        and not result["blocked_modules_loaded"]
        and not result["firewall_hits"]
    )
    return result


def rotate_positions(
    positions: tuple[int, ...], shift: int
) -> tuple[int, ...]:
    return tuple(sorted(
        (position + shift) % RING_STATIONS for position in positions
    ))


def pairwise_separated(positions: tuple[int, ...]) -> bool:
    occupied = frozenset(positions)
    return all(
        (position + 1) % RING_STATIONS not in occupied
        for position in occupied
    )


def k3_families(
) -> dict[tuple[int, ...], tuple[tuple[int, ...], ...]]:
    grouped: dict[tuple[int, ...], set[tuple[int, ...]]] = {}
    for mask in range(1 << RING_STATIONS):
        positions = tuple(
            station
            for station in range(RING_STATIONS)
            if (mask >> station) & 1
        )
        if len(positions) != 3 or not pairwise_separated(positions):
            continue
        representative = min(
            rotate_positions(positions, shift)
            for shift in range(RING_STATIONS)
        )
        grouped.setdefault(representative, set()).add(positions)
    return {
        representative: tuple(sorted(alternatives))
        for representative, alternatives in sorted(grouped.items())
    }


def build_fixtures(
    program: tuple[object, ...],
) -> tuple[tuple[int, tuple[int, int], tuple[int, ...]], ...]:
    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    state = K.M.pack_state(banks, links)
    rows = []
    allocator = K.M.global_allocator_word(FIXTURE_BANKS)
    for event in range(2 * FIXTURE_BANKS):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = K.M.prepare_endpoint(state, direction)
        rows.append((event, direction, before))
        state = K.A.apply_semantic(before, allocator)
    return tuple(rows)


def synchronous_word(
    program: tuple[object, ...],
    token_positions: tuple[int, ...],
) -> tuple[object, ...]:
    positions = tuple(token_positions)
    word = []
    for _step in range(len(program)):
        live = set(positions)
        for station, row in enumerate(program):
            if station in live:
                word.extend(K.mapped_macro(row))
        positions = tuple(
            (station + 1) % len(program) for station in positions
        )
    return tuple(word)


def compile_word(word: tuple[object, ...]) -> CompiledWord:
    compiled = []
    for gate in word:
        kind = str(gate.kind)
        wires = tuple(int(wire) for wire in gate.wires)
        if kind == "X" and len(wires) == 1:
            compiled.append((1, wires[0], -1, -1))
        elif kind == "CNOT" and len(wires) == 2:
            compiled.append((2, wires[0], wires[1], -1))
        elif kind == "TOF" and len(wires) == 3:
            compiled.append((3, wires[0], wires[1], wires[2]))
        else:
            raise AssertionError(("unsupported exact gate", kind, wires))
    return tuple(compiled)


def apply_bit_sliced_word(
    wire_values: list[int],
    compiled: CompiledWord,
    live_lane_mask: int,
) -> None:
    for kind, first, second, third in compiled:
        if kind == 1:
            wire_values[first] ^= live_lane_mask
        elif kind == 2:
            wire_values[second] ^= wire_values[first]
        else:
            wire_values[third] ^= (
                wire_values[first] & wire_values[second]
            )


def bit_slice_states(
    states: tuple[tuple[int, ...], ...],
) -> list[int]:
    if not states:
        raise AssertionError("empty bit slice")
    width = len(states[0])
    if any(len(state) != width for state in states):
        raise AssertionError("inconsistent state widths")
    return [
        sum(int(state[wire]) << lane for lane, state in enumerate(states))
        for wire in range(width)
    ]


def lane_bytes(wire_values: list[int], lane: int) -> StateBytes:
    mask = 1 << lane
    return bytes(int(bool(value & mask)) for value in wire_values)


def state_hex(state: StateBytes) -> str:
    packed = 0
    for coordinate, bit in enumerate(state):
        packed |= int(bit) << coordinate
    return format(packed, "x")


def one_changed_coordinate(
    left: tuple[int, ...], right: tuple[int, ...]
) -> int:
    changed = tuple(
        index
        for index, (left_bit, right_bit) in enumerate(zip(left, right))
        if left_bit != right_bit
    )
    if len(left) != len(right) or len(changed) != 1:
        raise AssertionError(("coordinate basis failure", len(changed)))
    return changed[0]


def watched_coordinate_basis() -> dict[str, object]:
    banks0, links0 = K.B.chain_genesis(FIXTURE_BANKS)
    packed = K.M.pack_state(banks0, links0)
    banks, links = K.M.unpack_state(packed, FIXTURE_BANKS)
    labels: dict[int, tuple[str, str, int]] = {
        K.R3.X.SOURCE_POINTER: ("source", "SOURCE_POINTER", 0)
    }
    watched_registers = (
        ("POINTER", K.A.POINTER),
        ("U_TO_V", K.A.U_TO_V),
        ("V_TO_U", K.A.V_TO_U),
        ("DIRECTION_OK", K.A.DIRECTION_OK),
        *tuple(
            (f"FRESH_{index}", wire)
            for index, wire in enumerate(K.A.FRESH)
        ),
        *tuple(
            (f"ZERO_WORK_{index}", wire)
            for index, wire in enumerate(K.A.ZERO_WORK)
        ),
        ("TOKEN_OK", K.A.TOKEN_OK),
    )
    for bank_index in range(FIXTURE_BANKS):
        for name, wire in watched_registers:
            changed_banks = [list(bank) for bank in banks]
            changed_links = [list(link) for link in links]
            changed_banks[bank_index][wire] ^= 1
            changed = K.M.pack_state(
                tuple(tuple(bank) for bank in changed_banks),
                tuple(tuple(link) for link in changed_links),
            )
            coordinate = one_changed_coordinate(packed, changed)
            labels[coordinate] = ("bank", name, bank_index)
    for link_index, link in enumerate(links):
        for wire in range(len(link)):
            changed_banks = [list(bank) for bank in banks]
            changed_links = [list(item) for item in links]
            changed_links[link_index][wire] ^= 1
            changed = K.M.pack_state(
                tuple(tuple(bank) for bank in changed_banks),
                tuple(tuple(item) for item in changed_links),
            )
            coordinate = one_changed_coordinate(packed, changed)
            labels[coordinate] = (
                "link", f"WIRE_{wire}", link_index
            )
    indices = tuple(sorted(labels))
    return {
        "indices": indices,
        "labels": labels,
        "state_width": len(packed),
        "watched_coordinate_count": len(indices),
        "pass": (
            len(packed) == STATE_WIDTH_EXPECTED
            and len(indices) == 477
            and len(labels) == len(indices)
        ),
    }


def clean_lane(
    wire_values: list[int],
    lane: int,
    watched_indices: tuple[int, ...],
) -> bool:
    lane_mask = 1 << lane
    return not any(
        wire_values[coordinate] & lane_mask
        for coordinate in watched_indices
    )


def clean_state(
    state: tuple[int, ...] | StateBytes,
    watched_indices: tuple[int, ...],
) -> bool:
    return not any(state[coordinate] for coordinate in watched_indices)


def state_support(
    state: StateBytes,
    basis: dict[str, object],
) -> tuple[tuple[str, str, int], ...]:
    labels = basis["labels"]
    return tuple(
        labels[coordinate]
        for coordinate in basis["indices"]
        if state[coordinate]
    )


def initial_state(
    before: tuple[int, ...],
    word: tuple[object, ...],
) -> tuple[int, ...]:
    return K.A.apply_semantic(before, word)


def discover_zero_rows_and_transients(
    program: tuple[object, ...],
    fixtures: tuple[tuple[int, tuple[int, int], tuple[int, ...]], ...],
    families: dict[
        tuple[int, ...], tuple[tuple[int, ...], ...]
    ],
    watched_indices: tuple[int, ...],
) -> tuple[
    tuple[Key, ...],
    dict[tuple[int, ...], tuple[object, ...]],
    dict[tuple[int, ...], CompiledWord],
    dict[Key, int],
    dict[str, object],
]:
    all_positions = tuple(sorted({
        positions
        for alternatives in families.values()
        for positions in alternatives
    }))
    words = {
        positions: synchronous_word(program, positions)
        for positions in all_positions
    }
    zero_rows = []
    for representative, alternatives in families.items():
        for event, _direction, before in fixtures:
            alternative_cleanliness = tuple(
                clean_state(
                    initial_state(before, words[positions]),
                    watched_indices,
                )
                for positions in alternatives
            )
            if not any(alternative_cleanliness):
                zero_rows.append((3, representative, event))

    representative_words = {
        representative: words[representative]
        for representative in families
    }
    compiled = {
        representative: compile_word(word)
        for representative, word in representative_words.items()
    }
    transient_moments: dict[Key, int] = {}
    zero_set = set(zero_rows)
    fixture_by_event = {event: before for event, _direction, before in fixtures}
    for representative in families:
        states = tuple(
            initial_state(
                fixture_by_event[event],
                representative_words[representative],
            )
            for event in range(2 * FIXTURE_BANKS)
        )
        wires = bit_slice_states(states)
        for horizon_t in range(TRANSIENT_SCAN_END + 1):
            for event in range(2 * FIXTURE_BANKS):
                key = (3, representative, event)
                if (
                    key in zero_set
                    and key not in transient_moments
                    and clean_lane(wires, event, watched_indices)
                ):
                    transient_moments[key] = horizon_t
            if horizon_t < TRANSIENT_SCAN_END:
                apply_bit_sliced_word(
                    wires,
                    compiled[representative],
                    (1 << (2 * FIXTURE_BANKS)) - 1,
                )

    selected = tuple(sorted(
        (
            key for key, moment in transient_moments.items()
            if moment in K3_EXPECTED_TRANSIENT_MOMENTS
        ),
        key=lambda key: (transient_moments[key], key),
    ))
    catalog = {
        "k3_family_count": len(families),
        "k3_configuration_count": len(all_positions),
        "zero_row_count": len(zero_rows),
        "zero_rows": tuple(zero_rows),
        "discovered_transients": tuple(
            (key, transient_moments[key])
            for key in sorted(
                transient_moments,
                key=lambda key: (transient_moments[key], key),
            )
        ),
        "selected_keys": selected,
    }
    catalog["pass"] = (
        len(families) == 7
        and len(all_positions) == 77
        and len(zero_rows) == K3_EXPECTED_ZERO_ROWS
        and len(selected) == 4
        and tuple(transient_moments[key] for key in selected)
        == K3_EXPECTED_TRANSIENT_MOMENTS
        and len(transient_moments) == 4
    )
    return (
        selected,
        representative_words,
        compiled,
        transient_moments,
        catalog,
    )


def capture_trajectory(
    initial: tuple[int, ...],
    compiled: CompiledWord,
    end_t: int,
) -> tuple[StateBytes, ...]:
    wires = [int(bit) for bit in initial]
    rows = []
    for horizon_t in range(end_t + 1):
        rows.append(bytes(wires))
        if horizon_t < end_t:
            apply_bit_sliced_word(wires, compiled, 1)
    return tuple(rows)


def equality_groups(
    states: tuple[StateBytes, ...],
) -> tuple[tuple[int, ...], ...]:
    groups: dict[StateBytes, list[int]] = {}
    for index, state in enumerate(states):
        groups.setdefault(state, []).append(index)
    return tuple(sorted(
        tuple(indices)
        for indices in groups.values()
        if len(indices) >= 2
    ))


def transient_certificate(
    keys: tuple[Key, ...],
    moments: dict[Key, int],
    fixtures: tuple[tuple[int, tuple[int, int], tuple[int, ...]], ...],
    words: dict[tuple[int, ...], tuple[object, ...]],
    compiled: dict[tuple[int, ...], CompiledWord],
    basis: dict[str, object],
) -> tuple[dict[str, object], dict[Key, tuple[StateBytes, ...]]]:
    fixture_by_event = {
        event: before for event, _direction, before in fixtures
    }
    trajectories = {}
    for key in keys:
        _k, positions, event = key
        initial = initial_state(
            fixture_by_event[event], words[positions]
        )
        trajectories[key] = capture_trajectory(
            initial, compiled[positions], moments[key]
        )

    same_time_rows = []
    for left_index, right_index in combinations(range(len(keys)), 2):
        left_key = keys[left_index]
        right_key = keys[right_index]
        shared_stop = min(moments[left_key], moments[right_key])
        exact_times = tuple(
            horizon_t
            for horizon_t in range(shared_stop)
            if trajectories[left_key][horizon_t]
            == trajectories[right_key][horizon_t]
        )
        same_time_rows.append({
            "key_indices": (left_index, right_index),
            "strict_pre_moment_shared_domain": (0, shared_stop - 1),
            "exact_full_state_coincidence_times": exact_times,
        })

    lag_rows = []
    all_four_lags = []
    for lag in FUNNEL_LAGS:
        states = tuple(
            trajectories[key][moments[key] - lag] for key in keys
        )
        groups = equality_groups(states)
        all_equal = len(set(states)) == 1
        if all_equal:
            all_four_lags.append(lag)
        lag_rows.append({
            "lag": lag,
            "times": tuple(moments[key] - lag for key in keys),
            "state_sha256": tuple(state_sha256(state) for state in states),
            "exact_equality_groups": groups,
            "all_four_exactly_equal": all_equal,
        })

    minus_five_rows = []
    for key in keys:
        state = trajectories[key][moments[key] - 5]
        minus_five_rows.append({
            "key": key,
            "time": moments[key] - 5,
            "state_width": len(state),
            "state_hex_little_endian_bit_coordinates": state_hex(state),
            "state_sha256_label_only": state_sha256(state),
            "residual_support": state_support(state, basis),
        })

    identity_rows = []
    for key in keys:
        moment = moments[key]
        trajectory = trajectories[key]
        clean_times = tuple(
            horizon_t
            for horizon_t, state in enumerate(trajectory)
            if clean_state(state, basis["indices"])
        )
        identity_rows.append({
            "key": key,
            "expected_moment": moment,
            "all_strictly_earlier_nonclean":
                all(
                    not clean_state(state, basis["indices"])
                    for state in trajectory[:-1]
                ),
            "clean_times_through_moment": clean_times,
            "moment_minus_1_sha256":
                state_sha256(trajectory[moment - 1]),
            "moment_sha256": state_sha256(trajectory[moment]),
        })

    same_time_any = any(
        row["exact_full_state_coincidence_times"]
        for row in same_time_rows
    )
    result = {
        "key_index": tuple(enumerate(keys)),
        "moments": tuple((key, moments[key]) for key in keys),
        "same_time_definition":
            "pairwise exact full-state equality at the same horizon t, "
            "strictly before both moments",
        "same_time_coincidence_map": tuple(same_time_rows),
        "same_time_any": same_time_any,
        "time_shifted_definition":
            "compare key i at its own moment_i-d for common d=1..8",
        "time_shifted_funnel_map": tuple(lag_rows),
        "all_four_common_funnel_lags": tuple(all_four_lags),
        "moment_minus_5_exact_states": tuple(minus_five_rows),
        "trajectory_sha256": digest(tuple(
            (
                key,
                tuple(state_sha256(state) for state in trajectories[key]),
            )
            for key in keys
        )),
        "identity_rows": tuple(identity_rows),
    }
    result["pass"] = (
        len(keys) == 4
        and tuple(moments[key] for key in keys)
        == K3_EXPECTED_TRANSIENT_MOMENTS
        and len(same_time_rows) == 6
        and len(lag_rows) == len(FUNNEL_LAGS)
        and all(
            row["clean_times_through_moment"]
            == (row["expected_moment"],)
            and row["all_strictly_earlier_nonclean"]
            for row in identity_rows
        )
    )
    return result, trajectories


def cycle_trajectory(
    initial: tuple[int, ...],
    compiled: CompiledWord,
    watched_indices: tuple[int, ...],
) -> tuple[tuple[StateBytes, ...], dict[str, object]]:
    wires = [int(bit) for bit in initial]
    initial_bytes = bytes(wires)
    rows = []
    clean_times = []
    return_times = []
    for horizon_t in range(K3_CYCLE_PERIOD + 1):
        state = bytes(wires)
        if horizon_t < K3_CYCLE_PERIOD:
            rows.append(state)
        if clean_state(state, watched_indices):
            clean_times.append(horizon_t)
        if horizon_t > 0 and state == initial_bytes:
            return_times.append(horizon_t)
        if horizon_t < K3_CYCLE_PERIOD:
            apply_bit_sliced_word(wires, compiled, 1)
    sequence = tuple(rows)
    control = {
        "clean_times_through_closure": tuple(clean_times),
        "exact_return_times_through_closure": tuple(return_times),
        "initial_state_sha256": state_sha256(initial_bytes),
        "closure_state_sha256": state_sha256(bytes(wires)),
        "trajectory_sha256": digest(tuple(
            state_sha256(state) for state in sequence
        )),
        "pass": (
            not clean_times
            and tuple(return_times) == (K3_CYCLE_PERIOD,)
            and bytes(wires) == initial_bytes
            and len(set(sequence)) == K3_CYCLE_PERIOD
        ),
    }
    return sequence, control


def cycle_certificate(
    program: tuple[object, ...],
    fixtures: tuple[tuple[int, tuple[int, int], tuple[int, ...]], ...],
    watched_indices: tuple[int, ...],
) -> tuple[
    dict[str, object],
    dict[Key, tuple[StateBytes, ...]],
]:
    fixture_by_event = {
        event: before for event, _direction, before in fixtures
    }
    sequences = {}
    controls = {}
    composition_controls = []
    for key in K3_CYCLE_KEYS:
        _k, positions, event = key
        word = synchronous_word(program, positions)
        compiled = compile_word(word)
        initial = initial_state(fixture_by_event[event], word)
        orbit_initial, rail_a, rail_b, _trace = K.run_orbit(
            fixture_by_event[event],
            program,
            token_positions=positions,
        )
        expected_rail = tuple(
            int(station in positions)
            for station in range(len(program))
        )
        composition_controls.append({
            "key": key,
            "initial_composition_exact": orbit_initial == initial,
            "initial_rails_exact":
                rail_a == expected_rail and not any(rail_b),
        })
        sequence, control = cycle_trajectory(
            initial, compiled, watched_indices
        )
        sequences[key] = sequence
        controls[key] = control

    shift_rows = []
    for left_index, right_index in combinations(
        range(len(K3_CYCLE_KEYS)), 2
    ):
        left_key = K3_CYCLE_KEYS[left_index]
        right_key = K3_CYCLE_KEYS[right_index]
        left = sequences[left_key]
        right = sequences[right_key]
        candidate_offsets = tuple(
            offset
            for offset, state in enumerate(right)
            if state == left[0]
        )
        exact_offsets = tuple(
            offset
            for offset in candidate_offsets
            if all(
                left[horizon_t]
                == right[(horizon_t + offset) % K3_CYCLE_PERIOD]
                for horizon_t in range(K3_CYCLE_PERIOD)
            )
        )
        shift_rows.append({
            "key_indices": (left_index, right_index),
            "definition":
                "state_left(t)=state_right((t+offset) mod 5952)",
            "initial_exact_match_candidate_offsets": candidate_offsets,
            "exact_full_trajectory_offsets": exact_offsets,
            "time_shifted_copies": bool(exact_offsets),
        })

    all_pairwise_shifted = all(
        row["time_shifted_copies"] for row in shift_rows
    )
    all_pairwise_zero_offset = (
        all_pairwise_shifted
        and all(
            row["exact_full_trajectory_offsets"] == (0,)
            for row in shift_rows
        )
    )
    result = {
        "key_index": tuple(enumerate(K3_CYCLE_KEYS)),
        "period": K3_CYCLE_PERIOD,
        "composition_controls": tuple(composition_controls),
        "cycle_controls": tuple(
            (key, controls[key]) for key in K3_CYCLE_KEYS
        ),
        "pairwise_shift_map": tuple(shift_rows),
        "all_pairwise_time_shifted_copies": all_pairwise_shifted,
        "all_pairwise_zero_offset_identical":
            all_pairwise_zero_offset,
        "one_orbit_under_time_plus_position_family":
            all_pairwise_shifted,
        "trajectory_family_sha256": digest(tuple(
            (
                key,
                controls[key]["trajectory_sha256"],
            )
            for key in K3_CYCLE_KEYS
        )),
    }
    result["pass"] = (
        len(shift_rows) == 6
        and all(
            row["initial_composition_exact"]
            and row["initial_rails_exact"]
            for row in composition_controls
        )
        and all(control["pass"] for control in controls.values())
    )
    return result, sequences


def k2_sstar(
    program: tuple[object, ...],
    fixtures: tuple[tuple[int, tuple[int, int], tuple[int, ...]], ...],
) -> StateBytes:
    _k, positions, event = K2_SSTAR_KEY
    before = next(
        before
        for fixture_event, _direction, before in fixtures
        if fixture_event == event
    )
    word = synchronous_word(program, positions)
    compiled = compile_word(word)
    wires = list(initial_state(before, word))
    for _horizon_t in range(K2_SSTAR_TIME):
        apply_bit_sliced_word(wires, compiled, 1)
    return bytes(wires)


def cross_stratum_certificate(
    sstar: StateBytes,
    transient_trajectories: dict[Key, tuple[StateBytes, ...]],
    cycle_sequences: dict[Key, tuple[StateBytes, ...]],
) -> dict[str, object]:
    transient_visits = tuple(
        (key, tuple(
            horizon_t
            for horizon_t, state in enumerate(trajectory)
            if state == sstar
        ))
        for key, trajectory in transient_trajectories.items()
    )
    cycle_visits = tuple(
        (key, tuple(
            horizon_t
            for horizon_t, state in enumerate(sequence)
            if state == sstar
        ))
        for key, sequence in cycle_sequences.items()
    )
    all_widths = (
        {len(sstar)}
        | {
            len(state)
            for trajectory in transient_trajectories.values()
            for state in trajectory[:1]
        }
        | {
            len(state)
            for sequence in cycle_sequences.values()
            for state in sequence[:1]
        }
    )
    comparable = all_widths == {STATE_WIDTH_EXPECTED}
    exact_visit_count = sum(
        len(times) for _key, times in transient_visits + cycle_visits
    )
    result = {
        "k2_state": {
            "key": K2_SSTAR_KEY,
            "time": K2_SSTAR_TIME,
            "state_width": len(sstar),
            "state_sha256_label_only": state_sha256(sstar),
        },
        "state_space_audit": {
            "k2_fixture_banks": FIXTURE_BANKS,
            "k3_fixture_banks": FIXTURE_BANKS,
            "observed_state_widths": tuple(sorted(all_widths)),
            "same_pack_unpack_coordinate_space": True,
            "token_count_changes_fixed_words_not_state_layout": True,
            "exact_full_state_comparison_legitimate": comparable,
            "projection_required": False,
        },
        "transient_exact_Sstar_visits": transient_visits,
        "cycle_exact_Sstar_visits_one_complete_period": cycle_visits,
        "exact_Sstar_visit_count": exact_visit_count,
        "outcome": (
            "EXACT_CROSS_STRATUM_SSTAR_VISITS"
            if exact_visit_count
            else "NO_EXACT_CROSS_STRATUM_SSTAR_VISIT_IN_SCOPED_TRAJECTORIES"
        ),
    }
    result["pass"] = comparable
    return result


def choose_verdict(
    transient: dict[str, object],
    cycles: dict[str, object],
    cross_stratum: dict[str, object],
) -> dict[str, object]:
    funnel_lags = transient["all_four_common_funnel_lags"]
    if funnel_lags:
        verdict = "MERGER_RECURS"
        named_pattern = (
            "K3_ALL_FOUR_TIME_SHIFTED_COMMON_FUNNEL_AT_LAGS_"
            + "_".join(str(lag) for lag in funnel_lags)
        )
    elif cycles["all_pairwise_time_shifted_copies"]:
        verdict = "STRATUM_STRUCTURE_FOUND"
        named_pattern = (
            "K3_5952_CYCLES_IDENTICAL_IN_PHASE_OFFSET_0"
            if cycles["all_pairwise_zero_offset_identical"]
            else "K3_5952_CYCLES_ONE_EXACT_TIME_SHIFT_ORBIT"
        )
    elif transient["same_time_any"]:
        verdict = "STRATUM_STRUCTURE_FOUND"
        named_pattern = "K3_PARTIAL_SAME_TIME_FULL_STATE_COINCIDENCE"
    elif cross_stratum["exact_Sstar_visit_count"]:
        verdict = "STRATUM_STRUCTURE_FOUND"
        named_pattern = "K2_SSTAR_EXACTLY_REVISITED_BY_SCOPED_K3_KEY"
    else:
        verdict = "NO_RECURRENCE"
        named_pattern = "K2_MERGER_STRATUM_LOCAL_AT_CURRENT_SCOPE"
    return {
        "verdict": verdict,
        "exact_pattern": named_pattern,
        "decision_order": (
            "all-four common transient funnel lag; else all-pair cycle "
            "time-shift orbit; else partial same-time merger; else exact "
            "cross-stratum S* visit; else no recurrence"
        ),
        "k3_all_four_common_funnel_lags": funnel_lags,
        "k3_same_time_any": transient["same_time_any"],
        "k3_cycles_one_shift_orbit":
            cycles["all_pairwise_time_shifted_copies"],
        "k3_cycles_identical_in_phase_offset_0":
            cycles["all_pairwise_zero_offset_identical"],
        "k2_Sstar_exact_k3_visit_count":
            cross_stratum["exact_Sstar_visit_count"],
        "pass": verdict in {
            "MERGER_RECURS",
            "STRATUM_STRUCTURE_FOUND",
            "NO_RECURRENCE",
        },
    }


def run_science_probe() -> dict[str, object]:
    program = K.interleaved_program(FIXTURE_BANKS)
    fixtures = build_fixtures(program)
    basis = watched_coordinate_basis()
    families = k3_families()
    (
        transient_keys,
        words,
        compiled,
        transient_moments,
        catalog,
    ) = discover_zero_rows_and_transients(
        program, fixtures, families, basis["indices"]
    )
    transient, transient_trajectories = transient_certificate(
        transient_keys,
        transient_moments,
        fixtures,
        words,
        compiled,
        basis,
    )
    cycles, cycle_sequences = cycle_certificate(
        program, fixtures, basis["indices"]
    )
    sstar = k2_sstar(program, fixtures)
    cross_stratum = cross_stratum_certificate(
        sstar, transient_trajectories, cycle_sequences
    )
    verdict = choose_verdict(transient, cycles, cross_stratum)
    identity = {
        "k3_transient_reverified": transient["identity_rows"][0],
        "period_5952_cycle_reproduced":
            dict(cycles["cycle_controls"])[K3_CYCLE_KEYS[0]],
    }
    identity["pass"] = (
        identity["k3_transient_reverified"][
            "clean_times_through_moment"
        ] == (
            identity["k3_transient_reverified"]["expected_moment"],
        )
        and identity["k3_transient_reverified"][
            "all_strictly_earlier_nonclean"
        ]
        and identity["period_5952_cycle_reproduced"]["pass"]
    )
    result = {
        "catalog": catalog,
        "basis": {
            key: value for key, value in basis.items() if key != "labels"
        },
        "A": transient,
        "B": cycles,
        "C": cross_stratum,
        "D": verdict,
        "E": identity,
    }
    result["pass"] = (
        catalog["pass"]
        and basis["pass"]
        and transient["pass"]
        and cycles["pass"]
        and cross_stratum["pass"]
        and verdict["pass"]
        and identity["pass"]
    )
    return result


def stable_render(
    certificates: dict[str, object],
    report: dict[str, object],
) -> str:
    lines = [
        "CYCLE824_K3_MERGER_PROBE",
        *(
            f"CERTIFICATE_{name}={compact(value)}"
            for name, value in certificates.items()
        ),
        f"REPORT={compact(report)}",
    ]
    return "\n".join(lines) + "\n"


def run() -> int:
    started = monotonic()
    sources = source_certificate()
    primary = run_science_probe()
    gc.collect()
    replay = run_science_probe()
    deterministic = primary == replay
    elapsed = monotonic() - started

    checks = {
        "A_K3_TRANSIENT_PRE_MOMENT_STRUCTURE": primary["A"]["pass"],
        "B_K3_PERIOD_5952_CYCLE_STRUCTURE": primary["B"]["pass"],
        "C_K2_SSTAR_CROSS_STRATUM": primary["C"]["pass"],
        "D_VERDICT_EXACT_BRANCH": primary["D"]["pass"],
        "E_TRANSIENT_AND_CYCLE_IDENTITIES": primary["E"]["pass"],
        "F_SHAS_BLOCKLIST_DETERMINISM_BOUNDS": False,
    }
    controls_base = (
        sources["pass"]
        and primary["pass"]
        and deterministic
        and elapsed < AUDIT_TIMEOUT_SEC
        and not any(
            name in sys.modules for name in BLOCKLISTED_MODULES
        )
        and not IMPORT_FIREWALL.hits
    )
    controls = {
        **sources,
        "determinism_scope":
            "complete catalog rediscovery, four transient trajectories, "
            "four full 5952-cycle trajectories, k2 S* evolution, exact "
            "equality maps, identities, cross-stratum test, and verdict",
        "primary_science_sha256": digest(primary),
        "replay_science_sha256": digest(replay),
        "deterministic_exact_certificate_equality": deterministic,
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "blocked_modules_loaded_at_end": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits_at_end": tuple(IMPORT_FIREWALL.hits),
        "pass": False,
    }
    certificates = {
        "A_TRANSIENT": primary["A"],
        "B_CYCLES": primary["B"],
        "C_CROSS_STRATUM": primary["C"],
        "D_VERDICT": primary["D"],
        "E_IDENTITIES": primary["E"],
        "F_CONTROLS": controls,
    }
    report = {
        "cycle": 824,
        "verdict": primary["D"]["verdict"],
        "exact_pattern": primary["D"]["exact_pattern"],
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "checks": {},
        "pass": False,
        "terminal": "CYCLE824_K3_MERGER_PROBE_HONEST_FAIL",
    }
    for _iteration in range(6):
        controls["pass"] = controls_base
        checks["F_SHAS_BLOCKLIST_DETERMINISM_BOUNDS"] = controls["pass"]
        report["checks"] = dict(checks)
        report["pass"] = all(checks.values())
        report["terminal"] = (
            "CYCLE824_K3_MERGER_PROBE_EXACT_PASS"
            if report["pass"]
            else "CYCLE824_K3_MERGER_PROBE_HONEST_FAIL"
        )
        output = stable_render(certificates, report)
        stdout_bytes = len(output.encode("utf-8"))
        controls["stdout_bytes"] = stdout_bytes
        controls["pass"] = (
            controls_base and stdout_bytes < STDOUT_LIMIT_BYTES
        )
        report["stdout_bytes"] = stdout_bytes
    output = stable_render(certificates, report)
    final_bytes = len(output.encode("utf-8"))
    if final_bytes >= STDOUT_LIMIT_BYTES:
        failure = {
            "pass": False,
            "terminal": "CYCLE824_K3_MERGER_PROBE_HONEST_FAIL",
            "failure": "stdout bound exceeded",
            "stdout_bytes": final_bytes,
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        }
        sys.stdout.write(compact(failure) + "\n")
        return 1
    sys.stdout.write(output)
    return 0 if report["pass"] else 1


def main() -> int:
    try:
        return run()
    except Exception as error:
        failure = {
            "pass": False,
            "terminal": "CYCLE824_K3_MERGER_PROBE_HONEST_FAIL",
            "exception_type": type(error).__name__,
            "exception": str(error),
        }
        sys.stdout.write(compact(failure) + "\n")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
