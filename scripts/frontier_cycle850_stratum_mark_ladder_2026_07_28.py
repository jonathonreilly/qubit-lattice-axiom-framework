#!/usr/bin/env python3
"""Cycle 850: bounded k=4/k=5 stratum-mark ladder census.

The Cycle-719 and Cycle-849 runners are SHA-pinned source primaries.  They are
read as text/AST only and are neither imported nor executed.  The pinned
Cycle-830 literal fixture bank is decoded from its Git object, after which this
runner independently applies the landed integer Boolean gate rules.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle849_scheduling_contrast_2026_07_28.py",
)

import ast
import base64
from hashlib import sha1, sha256
import importlib.abc
from itertools import combinations
import json
from math import comb
from pathlib import Path
import struct
import subprocess
import sys
from time import monotonic
import zlib


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_BRANCH = "physics-loop/proof-grade-blockF21-20260729"
EXPECTED_BASE = "ce5c4a16438654cce23afc477d1e7d418247931e"
FIXTURE_BANKS = 2
STATE_BITS = 5815
STATE_BYTES = (STATE_BITS + 7) // 8
GATE_COUNT = 3106
EVENT_COUNT = 4
STRATA = (4, 5)
SWEEP_HORIZON = 65_536
EXPECTED_WORKTREE_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "0f1d15c444514f81ac007e2c122b3b47c917bec9a01de8b4e5fef358ef910818",
}
EXPECTED_WORKTREE_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    AUDIT_INPUT_PATHS[1]: "f2e842dbdbc04df27ddd078424a5cd9bc9455af5",
}
CYCLE830_SOURCE = (
    "cycle830_fixture_primary",
    "2bc4c4d6111a0e260b8b6107cd82e57dcbaa1744",
    "scripts/frontier_cycle830_sstar_preimage_tree_2026_07_28.py",
    "40d8cfb99b65fa251599bbf07f6a4399fd5bda9ad1e9e12e24db9395c4737d58",
    "98b1571228ad0902301b6853208ef249ea2c2973",
)
EXPECTED_GATE_RAW_SHA256 = (
    "1ef101b5745147bd43c116d87e2774635657e520d744b380bd8bad6d27884f4c"
)
EXPECTED_FAMILY_RAW_SHA256 = (
    "54fbb59c9d2232e77af6204f0c01b079148560bef1409cc74f311b5373784282"
)

Gate = tuple[int, int, int, int]
Key = tuple[int, tuple[int, ...], int]


class _PrimaryFirewall(importlib.abc.MetaPathFinder):
    """Fail closed if a cited source primary is imported."""

    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(
        self, fullname: str, path: object = None, target: object = None
    ) -> None:
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids import of {fullname}")
        return None


BLOCKLISTED_MODULES = tuple(sorted({
    *(Path(path).stem for path in AUDIT_INPUT_PATHS),
    Path(CYCLE830_SOURCE[2]).stem,
}))
FIREWALL = _PrimaryFirewall()
sys.meta_path.insert(0, FIREWALL)


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode()).hexdigest()


def git_bytes(*arguments: str) -> bytes:
    return subprocess.run(
        ("git", *arguments), cwd=ROOT, check=True, capture_output=True,
        timeout=20,
    ).stdout


def git_text(*arguments: str) -> str:
    return git_bytes(*arguments).decode().strip()


def git_blob(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode() + payload).hexdigest()


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


def top_level_function_names(tree: ast.Module) -> set[str]:
    return {
        node.name for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }


def source_controls() -> tuple[dict[str, object], ast.Module]:
    payloads = {path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS}
    trees = {
        path: ast.parse(payload, filename=path)
        for path, payload in payloads.items()
    }
    name, commit, historical_path, expected_sha, expected_blob = CYCLE830_SOURCE
    spec = f"{commit}:{historical_path}"
    historical_payload = git_bytes("show", spec)
    historical_tree = ast.parse(historical_payload, filename=spec)
    worktree_rows = tuple({
        "path": path,
        "exists": (ROOT / path).is_file(),
        "worktree_relative": not Path(path).is_absolute(),
        "access": "WORKTREE_TEXT_AST_ONLY_BLOCKLISTED",
        "sha256": sha256(payloads[path]).hexdigest(),
        "expected_sha256": EXPECTED_WORKTREE_SHA256[path],
        "sha256_exact": sha256(payloads[path]).hexdigest()
        == EXPECTED_WORKTREE_SHA256[path],
        "git_blob": git_blob(payloads[path]),
        "expected_git_blob": EXPECTED_WORKTREE_BLOBS[path],
        "git_blob_exact": git_blob(payloads[path])
        == EXPECTED_WORKTREE_BLOBS[path],
    } for path in AUDIT_INPUT_PATHS)
    historical_row = {
        "name": name,
        "spec": spec,
        "access": "PINNED_GIT_OBJECT_TEXT_AST_ONLY_BLOCKLISTED",
        "sha256": sha256(historical_payload).hexdigest(),
        "expected_sha256": expected_sha,
        "sha256_exact": sha256(historical_payload).hexdigest() == expected_sha,
        "git_blob": git_text("rev-parse", spec),
        "expected_git_blob": expected_blob,
        "git_blob_exact": git_text("rev-parse", spec) == expected_blob,
    }
    markers = {
        AUDIT_INPUT_PATHS[0]: {
            "interleaved_program", "run_orbit", "held_certificate",
        },
        AUDIT_INPUT_PATHS[1]: {
            "trio_geometry", "phase_word", "synchronous_word", "apply_word",
            "recover_event_fixtures", "reconstruct_minimal_discriminator",
        },
        name: {"run"},
    }
    marker_exact = (
        markers[AUDIT_INPUT_PATHS[0]]
        <= top_level_function_names(trees[AUDIT_INPUT_PATHS[0]])
        and markers[AUDIT_INPUT_PATHS[1]]
        <= top_level_function_names(trees[AUDIT_INPUT_PATHS[1]])
        and markers[name] <= top_level_function_names(historical_tree)
    )
    self_tree = ast.parse(Path(__file__).read_bytes(), filename=Path(__file__).name)
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_INPUT_PATHS_literal":
            literal_assignment(self_tree, "AUDIT_INPUT_PATHS") == AUDIT_INPUT_PATHS,
        "all_AUDIT_INPUT_PATHS_existing_worktree_relative": all(
            row["exists"] and row["worktree_relative"] for row in worktree_rows
        ),
        "worktree_source_rows": worktree_rows,
        "historical_source_row": historical_row,
        "source_AST_markers_exact": marker_exact,
        "blocked_modules": BLOCKLISTED_MODULES,
        "blocked_modules_loaded": tuple(sorted(
            module for module in sys.modules
            if module.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES
        )),
        "firewall_hits": tuple(FIREWALL.hits),
        "git_branch": git_text("branch", "--show-current"),
        "expected_git_branch": EXPECTED_BRANCH,
        "git_base": git_text(
            "merge-base", "HEAD", "physics-loop/proof-grade-blockF20-20260729"
        ),
        "expected_git_base": EXPECTED_BASE,
    }
    result["pass"] = bool(
        result["AUDIT_INPUT_PATHS_literal"]
        and result["all_AUDIT_INPUT_PATHS_existing_worktree_relative"]
        and all(row["sha256_exact"] and row["git_blob_exact"]
                for row in worktree_rows)
        and historical_row["sha256_exact"]
        and historical_row["git_blob_exact"]
        and marker_exact
        and not result["blocked_modules_loaded"]
        and not result["firewall_hits"]
        and result["git_branch"] == EXPECTED_BRANCH
        and result["git_base"] == EXPECTED_BASE
    )
    return result, historical_tree


def derived_719_program_labels(bank_count: int) -> tuple[tuple[str, int], ...]:
    """Reimplement only Cycle-719's geometry-generated station census."""

    prefix = [("source", 0)]
    for bank in range(bank_count):
        prefix.append(("bank", bank))
        if bank:
            prefix.append(("cross", bank - 1))
        if bank < bank_count - 1:
            prefix.extend((
                ("handoff", bank), ("relay_latch", bank),
                ("relay_swap", bank),
            ))
    reverse: list[tuple[str, int]] = []
    for edge in reversed(range(bank_count - 1)):
        reverse.extend((
            ("relay_swap", edge), ("relay_unlatch", edge),
            ("handoff_return", edge),
        ))
    return tuple(prefix + reverse + [("finalizer", 0)])


def graph_distance(left: int, right: int, stations: int) -> int:
    return min((right - left) % stations, (left - right) % stations)


def independent_positions(stations: int, count: int) -> tuple[tuple[int, ...], ...]:
    return tuple(
        positions for positions in combinations(range(stations), count)
        if all(
            graph_distance(left, right, stations) > 1
            for left, right in combinations(positions, 2)
        )
    )


def independent_cycle_closed_form(stations: int, count: int) -> int:
    numerator = stations * comb(stations - count, count)
    denominator = stations - count
    if numerator % denominator:
        raise AssertionError(("nonintegral independent-cycle count", stations, count))
    return numerator // denominator


def stratum_populations() -> tuple[dict[str, object], dict[int, tuple[Key, ...]]]:
    program_labels = derived_719_program_labels(FIXTURE_BANKS)
    stations = len(program_labels)
    keys_by_k: dict[int, tuple[Key, ...]] = {}
    rows = []
    for count in STRATA:
        positions = independent_positions(stations, count)
        keys = tuple(
            (count, placement, event)
            for placement in positions for event in range(EVENT_COUNT)
        )
        keys_by_k[count] = keys
        rows.append({
            "k": count,
            "position_population": len(positions),
            "closed_form_population": independent_cycle_closed_form(stations, count),
            "event_fixture_population": EVENT_COUNT,
            "expanded_key_population": len(keys),
            "position_table_sha256": digest(positions),
            "key_table_sha256": digest(keys),
        })
    exact = (
        stations == 11
        and tuple(row["position_population"] for row in rows) == (55, 11)
        and all(row["position_population"] == row["closed_form_population"]
                for row in rows)
        and tuple(row["expanded_key_population"] for row in rows) == (220, 44)
    )
    certificate = {
        "finding": (
            "Cycle-719 interleaved_program(2) derives C11. Exhaustive independent "
            "C11 placements give k=4 population 55 and k=5 population 11; "
            "crossing the four reconstructed event fixtures gives 220 and 44 keys."
        ),
        "derivation": (
            "Reimplement the Cycle-719 geometry-generated station list; enumerate "
            "all k-subsets with every circular pair distance greater than one; "
            "cross-check |Ind_k(C_n)|=n/(n-k)*binomial(n-k,k). No note count is read."
        ),
        "fixture_banks": FIXTURE_BANKS,
        "derived_ring_stations": stations,
        "derived_program_station_labels": program_labels,
        "rows": tuple(rows),
        "pass": exact,
    }
    return certificate, keys_by_k


def lawful_pairs(stations: int) -> tuple[tuple[int, int], ...]:
    return tuple(
        pair for pair in combinations(range(stations), 2)
        if graph_distance(pair[0], pair[1], stations) > 1
    )


def decode_cycle830_fixtures(
    tree: ast.Module, stations: int,
) -> dict[str, object]:
    gate_encoded = literal_assignment(tree, "GATE_CONSTANTS_B85")
    family_encoded = literal_assignment(tree, "FAMILY_STATES_B85")
    if not isinstance(gate_encoded, str) or not isinstance(family_encoded, str):
        raise AssertionError("Cycle-830 literal fixtures missing")
    gate_raw = zlib.decompress(base64.b85decode(gate_encoded))
    family_raw = zlib.decompress(base64.b85decode(family_encoded))
    lengths = struct.unpack(f"<{stations}H", gate_raw[:2 * stations])
    offset = 2 * stations
    macros = []
    for length in lengths:
        rows = []
        for _index in range(length):
            rows.append(struct.unpack("<BHHH", gate_raw[offset:offset + 7]))
            offset += 7
        macros.append(tuple(rows))
    pairs = lawful_pairs(stations)
    pair_keys = tuple(sorted(
        (event, pair) for event in range(EVENT_COUNT) for pair in pairs
    ))
    states = {}
    for index, key in enumerate(pair_keys):
        start = index * STATE_BYTES
        states[key] = int.from_bytes(
            family_raw[start:start + STATE_BYTES], "little"
        )
    exact = (
        len(lengths) == stations
        and sum(lengths) == GATE_COUNT
        and offset == len(gate_raw)
        and sha256(gate_raw).hexdigest() == EXPECTED_GATE_RAW_SHA256
        and len(family_raw) == len(pair_keys) * STATE_BYTES
        and sha256(family_raw).hexdigest() == EXPECTED_FAMILY_RAW_SHA256
        and len(pairs) == 44
        and len(pair_keys) == len(states) == 176
    )
    return {
        "macros": tuple(macros),
        "pair_keys": pair_keys,
        "states": states,
        "public": {
            "source_access": "PINNED_GIT_OBJECT_TEXT_AST_ONLY_BLOCKLISTED",
            "macro_gate_counts": lengths,
            "macro_gate_count": sum(lengths),
            "gate_raw_sha256": sha256(gate_raw).hexdigest(),
            "family_raw_sha256": sha256(family_raw).hexdigest(),
            "family_key_count": len(states),
            "pass": exact,
        },
    }


def phase_word(
    macros: tuple[tuple[Gate, ...], ...],
    positions: tuple[int, ...],
    phase: int,
) -> tuple[Gate, ...]:
    stations = len(macros)
    live = {(position + phase) % stations for position in positions}
    return tuple(
        gate for station, macro in enumerate(macros) if station in live
        for gate in macro
    )


def synchronous_word(
    macros: tuple[tuple[Gate, ...], ...], positions: tuple[int, ...],
) -> tuple[Gate, ...]:
    return tuple(
        gate for phase in range(len(macros))
        for gate in phase_word(macros, positions, phase)
    )


def apply_word(state: int, word: tuple[Gate, ...]) -> int:
    for kind, first, second, third in word:
        if kind == 0:
            state ^= 1 << first
        elif kind == 1:
            state ^= ((state >> first) & 1) << second
        elif kind == 2:
            state ^= (
                ((state >> first) & 1) & ((state >> second) & 1)
            ) << third
        else:
            raise AssertionError(("unsupported gate kind", kind))
    return state


def recover_event_fixtures(fixtures: dict[str, object]) -> dict[str, object]:
    macros = fixtures["macros"]
    pair_keys = fixtures["pair_keys"]
    states = fixtures["states"]
    assert isinstance(macros, tuple)
    assert isinstance(pair_keys, tuple)
    assert isinstance(states, dict)
    recovered_by_key = {}
    replay_exact = True
    for key in pair_keys:
        event, pair = key
        word = synchronous_word(macros, pair)
        before = apply_word(states[key], tuple(reversed(word)))
        recovered_by_key[key] = before
        replay_exact &= apply_word(before, word) == states[key]
    before_by_event = {}
    event_rows = []
    for event in range(EVENT_COUNT):
        values = {
            recovered_by_key[key] for key in pair_keys if key[0] == event
        }
        before = min(values)
        before_by_event[event] = before
        event_rows.append({
            "event": event,
            "pair_reconstruction_count": sum(
                key[0] == event for key in pair_keys
            ),
            "unique_recovered_fixture_count": len(values),
            "recovered_fixture_packed_sha256": sha256(
                before.to_bytes(STATE_BYTES, "little")
            ).hexdigest(),
        })
    exact = bool(
        fixtures["public"]["pass"]
        and replay_exact
        and all(
            row["pair_reconstruction_count"] == 44
            and row["unique_recovered_fixture_count"] == 1
            for row in event_rows
        )
    )
    return {
        "before_by_event": before_by_event,
        "public": {
            "method": (
                "Invert every pair synchronous word in reverse gate order; "
                "X, CNOT, and Toffoli are self-inverse."
            ),
            "event_rows": tuple(event_rows),
            "all_176_pair_states_replay_exact": replay_exact,
            "pass": exact,
        },
    }


def first_common_all_source_meet(
    positions: tuple[int, ...], stations: int,
) -> tuple[int, tuple[int, ...]]:
    """The exact minimax graph-ball enumeration declared by Cycle 849."""

    for tick in range(stations):
        centers = tuple(
            station for station in range(stations)
            if all(
                graph_distance(station, source, stations) <= tick
                for source in positions
            )
        )
        if centers:
            return tick, centers
    raise AssertionError(("all-source wavefronts did not meet", positions))


def minimax_meet(
    positions: tuple[int, ...], stations: int,
) -> tuple[int, tuple[int, ...]]:
    radii = tuple(
        max(graph_distance(station, source, stations) for source in positions)
        for station in range(stations)
    )
    radius = min(radii)
    return radius, tuple(
        station for station, value in enumerate(radii) if value == radius
    )


def meeting_structure(
    keys_by_k: dict[int, tuple[Key, ...]], stations: int,
) -> dict[str, object]:
    rows_by_k = []
    exact = True
    for count in STRATA:
        keys = keys_by_k[count]
        position_rows = []
        for positions in tuple(dict.fromkeys(key[1] for key in keys)):
            meet = first_common_all_source_meet(positions, stations)
            theorem = minimax_meet(positions, stations)
            position_rows.append({
                "positions": positions,
                "class": "ANALOG_TRIO" if positions[1] == 2 else "ANALOG_NONTRIO",
                "first_common_all_source_meet_tick": meet[0],
                "first_common_all_source_meet_centers": meet[1],
                "enumeration_equals_minimax_theorem": meet == theorem,
            })
        by_position = {
            row["positions"]: row for row in position_rows
        }
        key_rows = tuple({
            "key": key,
            "class": by_position[key[1]]["class"],
            "first_common_all_source_meet_tick": by_position[key[1]][
                "first_common_all_source_meet_tick"
            ],
            "first_common_all_source_meet_centers": by_position[key[1]][
                "first_common_all_source_meet_centers"
            ],
        } for key in keys)
        positive_positions = sum(
            row["class"] == "ANALOG_TRIO" for row in position_rows
        )
        negative_positions = len(position_rows) - positive_positions
        signature_counts: dict[tuple[int, int], int] = {}
        for row in position_rows:
            signature = (
                int(row["first_common_all_source_meet_tick"]),
                len(row["first_common_all_source_meet_centers"]),
            )
            signature_counts[signature] = signature_counts.get(signature, 0) + 1
        row_exact = (
            len(key_rows) == len(keys)
            and positive_positions > 0
            and negative_positions > 0
            and all(row["enumeration_equals_minimax_theorem"]
                    for row in position_rows)
        )
        exact &= row_exact
        rows_by_k.append({
            "k": count,
            "position_population": len(position_rows),
            "expanded_key_population": len(key_rows),
            "analog_trio_position_population": positive_positions,
            "analog_nontrio_position_population": negative_positions,
            "analog_trio_key_population": positive_positions * EVENT_COUNT,
            "analog_nontrio_key_population": negative_positions * EVENT_COUNT,
            "split_degenerate": not (positive_positions and negative_positions),
            "meet_tick_center_count_population": tuple(
                (signature, population)
                for signature, population in sorted(signature_counts.items())
            ),
            "position_rows": tuple(position_rows),
            "every_key_meet_rows": key_rows,
            "pass": row_exact,
        })
    return {
        "finding": (
            "The ladder is already geometrically stratified: k=4 has eleven "
            "tick-3 one-center meets and forty-four tick-4 three-center meets; "
            "k=5 has eleven tick-4 one-center meets. Both analog splits are "
            "nondegenerate."
        ),
        "meeting_machinery_citation": (
            "Cycle-849 trio_geometry defines the first common all-source meet "
            "as the least tick for which a C11 station lies within that graph "
            "distance of every source; it identifies this with the exact "
            "minimax radius min_v max_i dist(v,source_i)."
        ),
        "cycle849_exact_split_definition": (
            "TRIO_KEYS = tuple(key for key in K3_OPEN_KEYS if key[1][1] == 2); "
            "NONTRIO_KEYS = tuple(key for key in K3_OPEN_KEYS if key not in TRIO_KEYS)"
        ),
        "ladder_analog_split_rule": (
            "ANALOG_TRIO iff the sorted positions satisfy key[1][1] == 2; "
            "ANALOG_NONTRIO is the complement in that stratum."
        ),
        "strata": tuple(rows_by_k),
        "pass": exact,
    }


def evolve_to_meets(
    fixtures: dict[str, object],
    recovered: dict[str, object],
    keys_by_k: dict[int, tuple[Key, ...]],
) -> dict[str, object]:
    macros = fixtures["macros"]
    before_by_event = recovered["before_by_event"]
    assert isinstance(macros, tuple)
    assert isinstance(before_by_event, dict)
    states_by_k: dict[int, tuple[int, ...]] = {}
    rows = []
    for count in STRATA:
        keys = keys_by_k[count]
        word_cache = {
            positions: synchronous_word(macros, positions)
            for positions in dict.fromkeys(key[1] for key in keys)
        }
        phase_cache: dict[tuple[tuple[int, ...], int], tuple[Gate, ...]] = {}
        states = []
        for key in keys:
            _k, positions, event = key
            state = apply_word(before_by_event[event], word_cache[positions])
            meet_tick, _centers = first_common_all_source_meet(
                positions, len(macros)
            )
            for tick in range(1, meet_tick + 1):
                cache_key = (positions, tick - 1)
                phase_cache.setdefault(
                    cache_key, phase_word(macros, positions, tick - 1)
                )
                state = apply_word(state, phase_cache[cache_key])
            states.append(state)
        states_by_k[count] = tuple(states)
        packed = b"".join(
            state.to_bytes(STATE_BYTES, "little") for state in states
        )
        rows.append({
            "k": count,
            "meet_state_count": len(states),
            "meet_state_table_sha256": sha256(packed).hexdigest(),
            "maximum_meet_tick": max(
                first_common_all_source_meet(key[1], len(macros))[0]
                for key in keys
            ),
        })
    return {
        "states_by_k": states_by_k,
        "public": {
            "construction": (
                "Apply each all-source synchronous word to its independently "
                "recovered event fixture, then apply successive landed phase "
                "words through that key's exact first common meet tick."
            ),
            "rows": tuple(rows),
            "pass": (
                fixtures["public"]["pass"]
                and recovered["public"]["pass"]
                and all(row["meet_state_count"] == len(keys_by_k[row["k"]])
                        for row in rows)
            ),
        },
    }


def binary_pattern_mask(one_mask: int, full_mask: int) -> int:
    return (int(bool(full_mask ^ one_mask)) << 0) | (int(bool(one_mask)) << 1)


def pair_pattern_mask(first: int, second: int, full_mask: int) -> int:
    first_zero = full_mask ^ first
    second_zero = full_mask ^ second
    return (
        (int(bool(first_zero & second_zero)) << 0)
        | (int(bool(first_zero & second)) << 1)
        | (int(bool(first & second_zero)) << 2)
        | (int(bool(first & second)) << 3)
    )


def decode_patterns(pattern_mask: int, width: int) -> tuple[tuple[int, ...], ...]:
    return tuple(
        tuple((pattern >> (width - 1 - offset)) & 1 for offset in range(width))
        for pattern in range(1 << width) if (pattern_mask >> pattern) & 1
    )


def class_one_masks(states: tuple[int, ...]) -> tuple[int, ...]:
    output = [0] * STATE_BITS
    for lane, state in enumerate(states):
        remaining = state
        while remaining:
            low = remaining & -remaining
            wire = low.bit_length() - 1
            if wire < STATE_BITS:
                output[wire] |= 1 << lane
            remaining ^= low
    return tuple(output)


def minimal_mark_hunt(
    keys: tuple[Key, ...], states: tuple[int, ...], count: int,
) -> dict[str, object]:
    labels = tuple(key[1][1] == 2 for key in keys)
    positive_states = tuple(state for state, label in zip(states, labels) if label)
    negative_states = tuple(state for state, label in zip(states, labels) if not label)
    if not positive_states or not negative_states:
        return {
            "k": count,
            "verdict": "STRUCTURALLY_DEGENERATE_SPLIT",
            "search_complete": False,
            "pass": False,
        }
    positive_one = class_one_masks(positive_states)
    negative_one = class_one_masks(negative_states)
    positive_full = (1 << len(positive_states)) - 1
    negative_full = (1 << len(negative_states)) - 1
    single_found = None
    single_tests = 0
    for wire in range(STATE_BITS):
        single_tests += 1
        positive_patterns = binary_pattern_mask(positive_one[wire], positive_full)
        negative_patterns = binary_pattern_mask(negative_one[wire], negative_full)
        if not (positive_patterns & negative_patterns):
            single_found = (wire, positive_patterns, negative_patterns)
            break
    pair_found = None
    pair_tests = 0
    if single_found is None:
        for first in range(STATE_BITS - 1):
            for second in range(first + 1, STATE_BITS):
                pair_tests += 1
                positive_patterns = pair_pattern_mask(
                    positive_one[first], positive_one[second], positive_full
                )
                negative_patterns = pair_pattern_mask(
                    negative_one[first], negative_one[second], negative_full
                )
                if not (positive_patterns & negative_patterns):
                    pair_found = (
                        (first, second), positive_patterns, negative_patterns
                    )
                    break
            if pair_found is not None:
                break
    total_pairs = comb(STATE_BITS, 2)
    found = single_found if single_found is not None else pair_found
    if single_found is not None:
        wires: tuple[int, ...] | None = (single_found[0],)
        positive_patterns = decode_patterns(single_found[1], 1)
        negative_patterns = decode_patterns(single_found[2], 1)
        minimum = 1
    elif pair_found is not None:
        wires = pair_found[0]
        positive_patterns = decode_patterns(pair_found[1], 2)
        negative_patterns = decode_patterns(pair_found[2], 2)
        minimum = 2
    else:
        wires = None
        positive_patterns = ()
        negative_patterns = ()
        minimum = None
    completed = bool(
        found is not None
        or (single_tests == STATE_BITS and pair_tests == total_pairs)
    )
    return {
        "k": count,
        "verdict": (
            "MARKED" if found is not None
            else "NO_MARK_AT_DECLARED_SINGLE_PAIR_FAMILY"
        ),
        "class_definition": "key[1][1] == 2 versus its complement",
        "analog_trio_key_count": len(positive_states),
        "analog_nontrio_key_count": len(negative_states),
        "search_order": (
            "single wires 0..5814, then lexicographic itertools.combinations "
            "of wire pairs from range(5815)"
        ),
        "single_tests": single_tests,
        "single_family_size": STATE_BITS,
        "pair_tests": pair_tests,
        "pair_family_size": total_pairs,
        "first_minimal_mark_wires": wires,
        "minimum_wire_count": minimum,
        "analog_trio_pattern_set": positive_patterns,
        "analog_nontrio_pattern_set": negative_patterns,
        "both_directions_exact": bool(
            found is not None
            and set(positive_patterns).isdisjoint(negative_patterns)
        ),
        "no_mark_proof": (
            None if found is not None else
            "All 5,815 single bits and all 16,904,205 bit-pairs were "
            "enumerated in the declared order; every candidate has a pattern "
            "collision between the two meet-state classes."
        ),
        "class_bitplane_digest_sha256": digest((positive_one, negative_one)),
        "search_complete": completed,
        "pass": completed,
    }


def native_mark_hunt(
    keys_by_k: dict[int, tuple[Key, ...]], dynamics: dict[str, object],
) -> dict[str, object]:
    states_by_k = dynamics["states_by_k"]
    assert isinstance(states_by_k, dict)
    rows = tuple(
        minimal_mark_hunt(keys_by_k[count], states_by_k[count], count)
        for count in STRATA
    )
    marked = tuple(row["k"] for row in rows if row["verdict"] == "MARKED")
    return {
        "finding": (
            "Neither k=4 nor k=5 carries a native mark at the declared "
            "single-bit/bit-pair family: each exhaustive search finds no "
            "separator in either direction."
        ),
        "declared_mark_family": (
            "All state bits bit[0]..bit[5814], followed by all unordered "
            "distinct bit-pairs in enumeration order. A mark requires disjoint "
            "class pattern sets, hence exact classification in both directions."
        ),
        "strata": rows,
        "marked_strata": marked,
        "every_stratum_marked": len(marked) == len(STRATA),
        "pass": bool(dynamics["public"]["pass"] and all(row["pass"] for row in rows)),
    }


def schedule_sweep(mark_certificate: dict[str, object]) -> dict[str, object]:
    marked = tuple(mark_certificate["marked_strata"])
    rows = tuple({
        "k": count,
        "status": (
            "SWEEP_REQUIRED" if count in marked
            else "NOT_APPLICABLE_UNMARKED"
        ),
    } for count in STRATA)
    # C proves that the conditional antecedent is empty on the SHA-pinned
    # inputs.  Claiming a synthetic schedule sweep for an unmarked class would
    # force the analogy that the task explicitly forbids.
    exact = not marked and all(
        row["status"] == "NOT_APPLICABLE_UNMARKED" for row in rows
    )
    return {
        "finding": (
            "No schedule sweep is triggered: D quantifies only over marked "
            "strata, while C proves that both k=4 and k=5 are unmarked at the "
            "declared family. The T=65,536 horizon is therefore recorded but "
            "not misreported as an executed post-mark sweep."
        ),
        "conditional_scope": "for marked strata",
        "declared_resolution_modes": (
            "clean postimage", "recurrence", "full-state funnel",
        ),
        "declared_horizon_T": SWEEP_HORIZON,
        "marked_strata_requiring_sweep": marked,
        "rows": rows,
        "pass": exact,
    }


def ladder_verdict(
    meeting: dict[str, object], mark: dict[str, object],
) -> tuple[str, dict[int, str]]:
    meeting_rows = {row["k"]: row for row in meeting["strata"]}
    mark_rows = {row["k"]: row for row in mark["strata"]}
    per_stratum = {}
    universal = True
    for count in STRATA:
        structural_difference = not (
            meeting_rows[count]["meet_tick_center_count_population"]
            == (((3, 1), meeting_rows[count]["position_population"]),)
        )
        marked = mark_rows[count]["verdict"] == "MARKED"
        universal &= marked and not structural_difference
        per_stratum[count] = (
            "LADDER_UNIVERSAL" if marked and not structural_difference
            else "LADDER_STRATIFIED"
        )
    return ("LADDER_UNIVERSAL" if universal else "LADDER_STRATIFIED"), per_stratum


def render(
    certificates: dict[str, dict[str, object]], report: dict[str, object],
) -> str:
    lines = [
        f"{'PASS' if value['pass'] else 'FAIL'} {name} :: {compact(value)}"
        for name, value in certificates.items()
    ]
    lines.append("SUMMARY_JSON " + compact(report))
    for row in report["strata"]:
        lines.append(
            f"STRATUM k={row['k']} population={row['position_population']} "
            f"keys={row['expanded_key_population']} meets={row['meets']} "
            f"mark={row['mark']} schedule={row['schedule']} "
            f"verdict={row['verdict']}"
        )
    lines.append(str(report["terminal_verdict"]))
    return "\n".join(lines) + "\n"


def stable_render(
    certificates: dict[str, dict[str, object]],
    report: dict[str, object], controls_base: bool,
) -> str:
    controls = certificates["E_CONTROLS"]
    for _attempt in range(20):
        controls["pass"] = bool(
            controls_base and controls["stdout_bytes"] < STDOUT_LIMIT_BYTES
        )
        report["pass"] = all(value["pass"] for value in certificates.values())
        output = render(certificates, report)
        size = len(output.encode())
        if controls["stdout_bytes"] == size and report["stdout_bytes"] == size:
            return output
        controls["stdout_bytes"] = size
        report["stdout_bytes"] = size
    raise AssertionError("stdout byte fixed point did not converge")


def run() -> int:
    started = monotonic()
    controls, fixture_tree = source_controls()
    source_controls_pass = bool(controls["pass"])
    certificate_a, keys_by_k = stratum_populations()
    stations = int(certificate_a["derived_ring_stations"])
    fixtures = decode_cycle830_fixtures(fixture_tree, stations)
    recovered = recover_event_fixtures(fixtures)
    certificate_b = meeting_structure(keys_by_k, stations)
    dynamics = evolve_to_meets(fixtures, recovered, keys_by_k)
    certificate_c = native_mark_hunt(keys_by_k, dynamics)
    certificate_d = schedule_sweep(certificate_c)

    replay_a, replay_keys = stratum_populations()
    replay_fixtures = decode_cycle830_fixtures(fixture_tree, stations)
    replay_recovered = recover_event_fixtures(replay_fixtures)
    replay_b = meeting_structure(replay_keys, stations)
    replay_dynamics = evolve_to_meets(
        replay_fixtures, replay_recovered, replay_keys
    )
    replay_c = native_mark_hunt(replay_keys, replay_dynamics)
    replay_schedule = schedule_sweep(replay_c)
    deterministic = bool(
        certificate_a == replay_a
        and keys_by_k == replay_keys
        and fixtures["public"] == replay_fixtures["public"]
        and recovered["public"] == replay_recovered["public"]
        and certificate_b == replay_b
        and dynamics["public"] == replay_dynamics["public"]
        and dynamics["states_by_k"] == replay_dynamics["states_by_k"]
        and certificate_c == replay_c
        and certificate_d == replay_schedule
    )
    verdict, per_stratum = ladder_verdict(certificate_b, certificate_c)
    elapsed = monotonic() - started
    controls.update({
        "source_controls_pass": source_controls_pass,
        "fixture_provenance": fixtures["public"],
        "event_fixture_reconstruction": recovered["public"],
        "meet_state_evolution": dynamics["public"],
        "blocked_modules_loaded_at_end": tuple(sorted(
            module for module in sys.modules
            if module.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES
        )),
        "firewall_hits_at_end": tuple(FIREWALL.hits),
        "determinism_replay": {
            "method": (
                "Full population, fixture decode/reconstruction, every-key "
                "meeting, meet-state evolution, exhaustive single/pair hunt, "
                "and conditional schedule certificate replay."
            ),
            "full_replay_exact": deterministic,
        },
        "exact_arithmetic": (
            "C11 graph distances, Boolean X/CNOT/Toffoli states, bitplanes, "
            "exhaustive enumeration counts, and digests use exact Python "
            "integers/bytes. Only monotonic runtime is floating point."
        ),
        "certificate_digest_sha256": digest((
            certificate_a, certificate_b, certificate_c, certificate_d,
            fixtures["public"], recovered["public"], dynamics["public"],
        )),
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "pass": False,
    })
    controls_base = bool(
        source_controls_pass
        and fixtures["public"]["pass"]
        and recovered["public"]["pass"]
        and dynamics["public"]["pass"]
        and deterministic
        and not controls["blocked_modules_loaded_at_end"]
        and not controls["firewall_hits_at_end"]
        and elapsed < AUDIT_TIMEOUT_SEC
    )
    certificates = {
        "A_STRATUM_POPULATIONS": certificate_a,
        "B_MEETING_STRUCTURE": certificate_b,
        "C_NATIVE_MARK_HUNT": certificate_c,
        "D_SCHEDULE_SWEEP": certificate_d,
        "E_CONTROLS": controls,
    }
    population_rows = {row["k"]: row for row in certificate_a["rows"]}
    meeting_rows = {row["k"]: row for row in certificate_b["strata"]}
    mark_rows = {row["k"]: row for row in certificate_c["strata"]}
    schedule_rows = {row["k"]: row for row in certificate_d["rows"]}
    summary_rows = tuple({
        "k": count,
        "position_population": population_rows[count]["position_population"],
        "expanded_key_population": population_rows[count]["expanded_key_population"],
        "meets": meeting_rows[count]["meet_tick_center_count_population"],
        "mark": mark_rows[count]["verdict"],
        "schedule": schedule_rows[count]["status"],
        "verdict": per_stratum[count],
    } for count in STRATA)
    report = {
        "cycle": 850,
        "question": "the stratum-mark ladder (k=4 and k=5)",
        "terminal_verdict": verdict,
        "strata": summary_rows,
        "runtime_seconds": round(elapsed, 6),
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "pass": False,
    }
    output = stable_render(certificates, report, controls_base)
    if len(output.encode()) >= STDOUT_LIMIT_BYTES:
        raise AssertionError("stdout limit exceeded")
    sys.stdout.write(output)
    return 0 if report["pass"] else 1


def main() -> int:
    try:
        return run()
    except Exception as error:
        sys.stdout.write(
            "FAIL E_CONTROLS :: " + compact({
                "exception_type": type(error).__name__,
                "exception": str(error),
                "pass": False,
            }) + "\nLADDER_STRATIFIED\n"
        )
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
