#!/usr/bin/env python3
"""Cycle 832 v2: the 36-key backbone and cycle-cohort hypothesis.

The runner independently rebuilds the landed k=2 family from the Cycle-719
core.  It cross-checks the event-3 backbone against the SHA-pinned landed
Cycle-818 strict table, replays every event-3 trajectory at every aligned gate
checkpoint through its full period, and retracts the v1 27-key exhaustion and
backbone-target prediction claims.  Cycle-818/819/820/822 sources remain
text/AST-only and blocked from import.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 200 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle818_period_structure_census_2026_07_28.py",
    "scripts/frontier_cycle819_deep_k2_continuation_2026_07_28.py",
    "scripts/frontier_cycle820_shared_moment_mechanism_2026_07_28.py",
    "scripts/frontier_cycle822_basin_independent_check_2026_07_28.py",
    "logs/runner-cache/frontier_cycle818_period_structure_census_2026_07_28.txt",
)

import ast
from collections import Counter
from hashlib import sha1, sha256
import importlib.abc
from itertools import combinations
import json
from math import gcd, lcm
from pathlib import Path
import sys
from time import monotonic
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "918ae9d1f5b29a4cee437dac8af4bfb27ee0aceee3a7abd0c6bdaaa6fb10d24c",
    AUDIT_INPUT_PATHS[2]:
        "e1c18187a4082fc534b9bd94055258a9aedc05c8dda37bb84f6a0d84592308fe",
    AUDIT_INPUT_PATHS[3]:
        "7344bee5d5f0bcbddcea7b9d83f40a552c90188bf30b4905f2649a49e4bf1649",
    AUDIT_INPUT_PATHS[4]:
        "c2fd23a7bb47caff70e9561fc9da46feef422c053954fa1af925901a1884ed0b",
    AUDIT_INPUT_PATHS[5]:
        "94bc32640518f097cb09060f9c378d26d73e263539573e3b8e75ed2aab1b857e",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    AUDIT_INPUT_PATHS[1]: "9c2657e5fa98c4d2bbb561a0f428cf59fca20973",
    AUDIT_INPUT_PATHS[2]: "c3a071835a61e78a4919decfede8534cbf95e1d9",
    AUDIT_INPUT_PATHS[3]: "6385dfa0dce58e86345483cc521ffa325e0d1cce",
    AUDIT_INPUT_PATHS[4]: "6d48f5d86006a5f6718b5993eaecd5ec69d86112",
    AUDIT_INPUT_PATHS[5]: "3544e3beada65b3480d352e2701f6e21b3f9ae2d",
}

PYTHON_INPUT_PATHS = AUDIT_INPUT_PATHS[:5]
TEXT_AST_ONLY_PATHS = AUDIT_INPUT_PATHS[1:5]
CYCLE818_CATALOG_CACHE_PATH = AUDIT_INPUT_PATHS[5]
COPIED_PRIMARY_MODULES = (
    "frontier_cycle830_sstar_preimage_tree_2026_07_28",
    "frontier_cycle831_deep_k2_forecast_tests_2026_07_28",
    "frontier_cycle831_cohorts_independent_check_2026_07_28",
)
BLOCKLISTED_MODULES = (
    *(Path(path).stem for path in TEXT_AST_ONLY_PATHS),
    *COPIED_PRIMARY_MODULES,
)


class _PrimaryFirewall(importlib.abc.MetaPathFinder):
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


FIREWALL = _PrimaryFirewall()
sys.meta_path.insert(0, FIREWALL)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


Key = tuple[int, tuple[int, int]]
Lane = tuple[Key, str]
PackedGate = tuple[int, int, int, int, int]

RING_STATIONS = 11
FIXTURE_BANKS = 2
FAMILY_SIZE = 176
STATE_BITS = 5815
LCM_SKELETON = 17856
MOMENTS = (14744, 33195, 51115)
EVENTS = (0, 2, 1)
LAWFUL_EVENTS = (0, 1, 2, 3)
TRANSITIONS = (
    {"source_event": 0, "target_event": 2, "left": 14744,
     "right": 33195, "residual": 595},
    {"source_event": 2, "target_event": 1, "left": 33195,
     "right": 51115, "residual": 64},
)
LANDED_CLOCKS = (2, 3, 288, 4464, 5952, 8928, 8930)
SMALL_CLOCKS = (2, 3, 288)
FUNNEL_MOMENTS = {0: 14739, 2: 33190, 1: 51110}
RESOLUTION_MOMENTS = {0: 14744, 2: 33195, 1: 51115}
BACKBONE: tuple[tuple[int, int], ...] = (
    (1, 6), (1, 7), (2, 7), (2, 8), (3, 8),
    (3, 9), (4, 9), (4, 10), (5, 10),
)
COHORT_KEYS = {
    event: tuple((event, pair) for pair in BACKBONE)
    for event in EVENTS
}
BACKBONE_KEYS = tuple(
    (event, pair) for pair in BACKBONE for event in LAWFUL_EVENTS
)
EVENT3_BACKBONE_KEYS = tuple((3, pair) for pair in BACKBONE)
V1_EXHAUSTION_CLAIM_VERBATIM = (
    "The literal nine-pair backbone is exhausted by the 27 keys in the "
    "three event cohorts (0, 2, 1)."
)

EARLIER_RESOLVED = frozenset({
    (3, (1, 10)), (3, (0, 7)),
    (3, (0, 5)), (3, (0, 6)),
    (3, (1, 6)), (3, (1, 7)), (3, (2, 7)),
    (3, (2, 8)), (3, (3, 8)), (3, (3, 9)),
    (3, (4, 9)), (3, (4, 10)), (3, (5, 10)),
    (2, (0, 9)), (1, (0, 9)), (0, (0, 9)),
    *COHORT_KEYS[0],
})

# These summaries are copied, not executed.  Their exact source-worktree
# provenance and a content digest are printed in Certificate E.
COPIED_830_ANATOMY = {
    "sibling_head": "050d8de96479cb2db5429e3cc7da6caf18a29213",
    "source_path":
        "scripts/frontier_cycle830_sstar_preimage_tree_2026_07_28.py",
    "source_worktree_sha256":
        "40d8cfb99b65fa251599bbf07f6a4399fd5bda9ad1e9e12e24db9395c4737d58",
    "source_worktree_git_blob": "98b1571228ad0902301b6853208ef249ea2c2973",
    "head_tree_git_blob": "1afe4941812f83f5e1fd5cc7c04e57231d703e8d",
    "Sstar_sha256":
        "cdf7e03092c6278b686c1f0edb9ebd716f4a285b1eabc8a7e2780695284a8f1a",
    "Sstar_hamming_weight": 44,
    "node_occupancy_reverse_depth_0_through_8":
        (1, 3, 4, 5, 3, 5, 5, 5, 4),
    "shared_pair_counts_reverse_depth_0_through_8":
        (36, 13, 11, 5, 13, 5, 5, 5, 7),
    "key_distinguishing_wires_reverse_depth_0_through_8":
        (0, 15, 19, 23, 19, 23, 21, 12, 11),
    "forward_partition_relations_depth_8_through_0": (
        "SPLIT_TO_FINER", "UNCHANGED", "UNCHANGED",
        "COALESCE_TO_COARSER", "SPLIT_TO_FINER",
        "COALESCE_TO_COARSER", "COALESCE_TO_COARSER",
        "COALESCE_TO_COARSER",
    ),
}
COPIED_831_COHORTS = {
    "sibling_head": "dc365128b0be38302a7c8b3cfda615c30a360a86",
    "primary_source_sha256":
        "624dad4d841e10e24891810dbc500cc4d6ebe871d6f09dd96f89e3189e52e2ff",
    "primary_source_git_blob": "ef24edda08118c4e14439b899790fff6c6f94175",
    "checker_source_sha256":
        "0144e7c899959b4f29df3cc513ca47079717004f358ffd40fd7dd5773fd182f1",
    "checker_source_git_blob": "d48d2f48ba72b624bd02cb63649247922b03ef4e",
    "funnel_state_sha256": {
        0: "cdf7e03092c6278b686c1f0edb9ebd716f4a285b1eabc8a7e2780695284a8f1a",
        2: "0015151ee4b751c35a5671fbb4f301d8569e78fc5a7ebe9f77372865b153c99b",
        1: "797fa122a629177c00c707aff4857d01bbad16b078983e3a6f1f5b632e094a41",
    },
    "pairwise_funnel_diff_weights": {
        "event2_vs_event1": 27,
        "event2_vs_event0": 25,
        "event1_vs_event0": 26,
    },
}
EXPECTED_COPIED_DATA_SHA256 = (
    "8b9add8bd401057cd2fe8d27c5975e0ec023335ff4eeb53e6fec098809b05eb6"
)


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode()).hexdigest()


def git_blob(payload: bytes) -> str:
    prefix = f"blob {len(payload)}\0".encode()
    return sha1(prefix + payload).hexdigest()


def state_sha256(state: tuple[int, ...]) -> str:
    return sha256(bytes(state)).hexdigest()


def literal_assignment(tree: ast.Module, name: str) -> object | None:
    candidates = []
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
        ):
            candidates.append(node.value)
    if len(candidates) != 1:
        return None
    try:
        return ast.literal_eval(candidates[0])
    except (ValueError, TypeError):
        return None


def cycle818_period_rows(payload: bytes) -> tuple[dict[str, object], ...]:
    prefix = "PERIOD_TABLE_ROW "
    rows = tuple(
        json.loads(line[len(prefix):])
        for line in payload.decode("utf-8").splitlines()
        if line.startswith(prefix)
    )
    return rows


def source_controls() -> dict[str, object]:
    payloads = {
        path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS
    }
    trees = {
        path: ast.parse(payload.decode(), filename=path)
        for path, payload in payloads.items()
        if path in PYTHON_INPUT_PATHS
    }
    catalog_rows = cycle818_period_rows(
        payloads[CYCLE818_CATALOG_CACHE_PATH]
    )
    cache_terminal_exact = any(
        line.startswith("FINAL ")
        and json.loads(line[6:]).get("terminal")
        == "CYCLE818_PERIOD_STRUCTURE_CENSUS_PASS"
        for line in payloads[CYCLE818_CATALOG_CACHE_PATH].decode(
            "utf-8"
        ).splitlines()
    )
    self_tree = ast.parse(
        Path(__file__).read_text(encoding="utf-8"), filename=__file__
    )
    rows = tuple({
        "path": path,
        "exists": (ROOT / path).is_file(),
        "sha256": sha256(payloads[path]).hexdigest(),
        "expected_sha256": EXPECTED_SHA256[path],
        "sha256_exact":
            sha256(payloads[path]).hexdigest() == EXPECTED_SHA256[path],
        "git_blob": git_blob(payloads[path]),
        "expected_git_blob": EXPECTED_GIT_BLOBS[path],
        "git_blob_exact":
            git_blob(payloads[path]) == EXPECTED_GIT_BLOBS[path],
        "structured_input_valid": (
            isinstance(trees[path], ast.Module)
            if path in PYTHON_INPUT_PATHS
            else len(catalog_rows) == 14 and cache_terminal_exact
        ),
        "access": (
            "DYNAMIC_IMPORT"
            if path == AUDIT_INPUT_PATHS[0]
            else (
                "TEXT_AST_ONLY_BLOCKLISTED"
                if path in TEXT_AST_ONLY_PATHS
                else "TEXT_JSON_LINES_ONLY"
            )
        ),
    } for path in AUDIT_INPUT_PATHS)
    copied_digest = digest((COPIED_830_ANATOMY, COPIED_831_COHORTS))
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_INPUT_PATHS_literal":
            literal_assignment(self_tree, "AUDIT_INPUT_PATHS")
            == AUDIT_INPUT_PATHS,
        "all_paths_existing": all(
            (ROOT / path).is_file() for path in AUDIT_INPUT_PATHS
        ),
        "plain_reading_named_files": len(AUDIT_INPUT_PATHS) + 1,
        "read_cap": 7,
        "cycle818_catalog_cache_path": CYCLE818_CATALOG_CACHE_PATH,
        "cycle818_strict_row_count": len(catalog_rows),
        "cycle818_cache_terminal_exact": cache_terminal_exact,
        "cycle818_period_rows": catalog_rows,
        "source_rows": rows,
        "blocked_modules": BLOCKLISTED_MODULES,
        "blocked_modules_loaded_at_source_check": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "copied_source_records": {
            "cycle830": COPIED_830_ANATOMY,
            "cycle831": COPIED_831_COHORTS,
        },
        "copied_data_sha256": copied_digest,
        "expected_copied_data_sha256": EXPECTED_COPIED_DATA_SHA256,
        "copied_data_sha256_exact":
            copied_digest == EXPECTED_COPIED_DATA_SHA256,
    }
    result["pass"] = (
        result["AUDIT_INPUT_PATHS_literal"]
        and result["all_paths_existing"]
        and result["plain_reading_named_files"] <= result["read_cap"]
        and all(
            row["sha256_exact"]
            and row["git_blob_exact"]
            and row["structured_input_valid"]
            for row in rows
        )
        and not result["blocked_modules_loaded_at_source_check"]
        and result["copied_data_sha256_exact"]
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


def open_pair_event_keys() -> tuple[tuple[tuple[int, int], int], ...]:
    resolved = (
        set(EARLIER_RESOLVED)
        | set(COHORT_KEYS[2])
        | set(COHORT_KEYS[1])
    )
    return tuple(
        (pair, event)
        for pair in separated_pairs()
        for event in range(2 * FIXTURE_BANKS)
        if (event, pair) not in resolved
    )


def candidate_residual(
    law: str,
    source_event: int,
    target_event: int,
) -> int | None:
    if law == "TARGET_PARITY_LOOKUP":
        return 595 if target_event % 2 == 0 else 64
    if law == "ABS_EVENT_JUMP_LOOKUP":
        return {1: 64, 2: 595}.get(abs(target_event - source_event))
    raise ValueError(law)


def build_preregistration() -> dict[str, object]:
    historical_v1_status = "PRE_REGISTERED_CANDIDATE"
    open_keys = open_pair_event_keys()
    base = MOMENTS[-1] + LCM_SKELETON
    laws = []
    for law in ("TARGET_PARITY_LOOKUP", "ABS_EVENT_JUMP_LOOKUP"):
        predictions = []
        for next_event in range(2 * FIXTURE_BANKS):
            residual = candidate_residual(law, EVENTS[-1], next_event)
            predictions.append({
                "next_event": next_event,
                "residual_prediction": residual,
                "predicted_next_cohort_moment":
                    None if residual is None else base + residual,
                "status":
                    "HISTORICAL_V1_PREDICTION_RETRACTED"
                    if residual is not None
                    else "OUTSIDE_LAW_DOMAIN",
            })
        laws.append({
            "law": law,
            "status": "RETRACTED_NO_K2_BACKBONE_TARGET",
            "historical_v1_status": historical_v1_status,
            "two_point_warning":
                "Two points cannot prove this law; rival exact lookups are "
                "retained only as a record of v1 underdetermination.",
            "predictions_from_current_event_1": tuple(predictions),
        })
    backbone_open = tuple(
        row for row in open_keys if row[0] in set(BACKBONE)
    )
    return {
        "order_statement":
            "Historical v1 pre-registration, reproduced but retracted by "
            "Certificate C because the complete k=2 backbone has no next "
            "transient cohort-moment target.",
        "known_last_moment": MOMENTS[-1],
        "lcm_skeleton": LCM_SKELETON,
        "prediction_base": base,
        "fallback_bounded_forecast": {
            "residual_interval_inclusive": (0, 596),
            "moment_interval_inclusive": (base, base + 596),
            "status": "RETRACTED_NO_CURRENT_TARGET",
        },
        "open_key_count": len(open_keys),
        "open_pair_event_keys": open_keys,
        "open_keys_on_nine_pair_backbone": backbone_open,
        "backbone_open_reading":
            "No key on the literal nine-pair backbone remains open; all 133 "
            "open keys are off-backbone.  This is the complete 36-key "
            "reading, not the retracted v1 27-key inventory.",
        "candidate_laws": tuple(laws),
    }


def factorization(value: int) -> tuple[tuple[int, int], ...]:
    if value < 1:
        raise ValueError(value)
    rows = []
    remaining = value
    prime = 2
    while prime * prime <= remaining:
        exponent = 0
        while remaining % prime == 0:
            remaining //= prime
            exponent += 1
        if exponent:
            rows.append((prime, exponent))
        prime = 3 if prime == 2 else prime + 2
    if remaining > 1:
        rows.append((remaining, 1))
    return tuple(rows)


def factor_product(rows: tuple[tuple[int, int], ...]) -> int:
    result = 1
    for prime, exponent in rows:
        result *= prime ** exponent
    return result


def divisors(value: int) -> tuple[int, ...]:
    small = []
    large = []
    candidate = 1
    while candidate * candidate <= value:
        if value % candidate == 0:
            small.append(candidate)
            if candidate * candidate != value:
                large.append(value // candidate)
        candidate += 1
    return tuple(small + list(reversed(large)))


def orbit_word(
    program: tuple[object, ...],
    pair: tuple[int, int],
) -> tuple[object, ...]:
    word = []
    for step in range(len(program)):
        live = {
            (pair[0] + step) % len(program),
            (pair[1] + step) % len(program),
        }
        for station, macro in enumerate(program):
            if station in live:
                word.extend(K.mapped_macro(macro))
    return tuple(word)


def build_seed_family() -> dict[str, object]:
    program = K.interleaved_program(FIXTURE_BANKS)
    pairs = separated_pairs()
    words = {pair: orbit_word(program, pair) for pair in pairs}
    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    state = K.M.pack_state(banks, links)
    allocator = K.M.global_allocator_word(FIXTURE_BANKS)
    epochs = []
    for event in range(2 * FIXTURE_BANKS):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = K.M.prepare_endpoint(state, direction)
        epochs.append((event, before))
        state = K.A.apply_semantic(before, allocator)
    states = {
        (event, pair): K.A.apply_semantic(before, words[pair])
        for event, before in epochs
        for pair in pairs
    }
    summary = {
        "events": len(epochs),
        "pairs": len(pairs),
        "keys": len(states),
        "state_bits": len(next(iter(states.values()))),
        "allocator_gates": len(allocator),
        "word_gate_counts": tuple(sorted({
            len(word) for word in words.values()
        })),
    }
    summary["pass"] = summary == {
        "events": 4,
        "pairs": 44,
        "keys": FAMILY_SIZE,
        "state_bits": STATE_BITS,
        "allocator_gates": 3106,
        "word_gate_counts": (6212,),
    }
    return {
        "program": program,
        "pairs": pairs,
        "words": words,
        "states": states,
        "summary": summary,
    }


def watched_residual_wires() -> tuple[tuple[str, int], ...]:
    bank_rows = (
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
            for name, wire in bank_rows
        )
    for link_index, base in enumerate(
        K.M.R12.LINK_BASES[:FIXTURE_BANKS - 1]
    ):
        rows.extend(
            (f"link{link_index}.WIRE_{wire}", base + wire)
            for wire in range(K.B.LINK_WIDTH)
        )
    return tuple(rows)


def pack_states(states: tuple[tuple[int, ...], ...]) -> list[int]:
    return [
        sum(state[wire] << lane for lane, state in enumerate(states))
        for wire in range(len(states[0]))
    ]


def unpack_lane(columns: list[int], lane: int) -> tuple[int, ...]:
    return tuple((column >> lane) & 1 for column in columns)


def lane_numbers(mask: int) -> tuple[int, ...]:
    result = []
    while mask:
        bit = mask & -mask
        result.append(bit.bit_length() - 1)
        mask ^= bit
    return tuple(result)


def packed_schedule(
    program: tuple[object, ...],
    lanes: tuple[Lane, ...],
) -> tuple[PackedGate, ...]:
    all_lanes = (1 << len(lanes)) - 1
    schedule = []
    for step in range(len(program)):
        station_masks = [0] * len(program)
        for lane in lane_numbers(all_lanes):
            pair = lanes[lane][0][1]
            station_masks[(pair[0] + step) % len(program)] |= 1 << lane
            station_masks[(pair[1] + step) % len(program)] |= 1 << lane
        for station, macro in enumerate(program):
            mask = station_masks[station]
            if not mask:
                continue
            for gate in K.mapped_macro(macro):
                if len(set(gate.wires)) != len(gate.wires):
                    raise AssertionError(("repeated landed gate wire", gate))
                if gate.kind == "X":
                    schedule.append((0, gate.wires[0], 0, 0, mask))
                elif gate.kind == "CNOT":
                    schedule.append(
                        (1, gate.wires[0], gate.wires[1], 0, mask)
                    )
                elif gate.kind == "TOF":
                    schedule.append(
                        (2, gate.wires[0], gate.wires[1],
                         gate.wires[2], mask)
                    )
                else:
                    raise AssertionError(("non-reversible gate", gate))
    return tuple(schedule)


def advance(columns: list[int], schedule: tuple[PackedGate, ...]) -> None:
    for kind, first, second, third, mask in schedule:
        if kind == 0:
            columns[first] ^= mask
        elif kind == 1:
            columns[second] ^= columns[first] & mask
        else:
            columns[third] ^= columns[first] & columns[second] & mask


def nonclean_mask(
    columns: list[int],
    residual_rows: tuple[tuple[str, int], ...],
) -> int:
    result = 0
    for _name, wire in residual_rows:
        result |= columns[wire]
    return result


def support_at_lane(
    columns: list[int],
    lane: int,
    residual_rows: tuple[tuple[str, int], ...],
) -> tuple[str, ...]:
    return tuple(
        name for name, wire in residual_rows
        if (columns[wire] >> lane) & 1
    )


def state_partition(
    keys: tuple[Key, ...],
    states: tuple[tuple[int, ...], ...],
) -> tuple[dict[str, object], ...]:
    groups: dict[tuple[int, ...], list[Key]] = {}
    for key, state in zip(keys, states):
        groups.setdefault(state, []).append(key)
    return tuple({
        "keys": tuple(group),
        "size": len(group),
        "state_sha256": state_sha256(state),
    } for state, group in sorted(
        groups.items(), key=lambda item: (item[1][0], len(item[1]))
    ))


def evolve_funnels(family: dict[str, object]) -> dict[str, object]:
    primary_keys = tuple(
        key for event in EVENTS for key in COHORT_KEYS[event]
    )
    duplicate_keys = tuple(
        (event, BACKBONE[0]) for event in EVENTS
    )
    primary_lanes: tuple[Lane, ...] = tuple(
        (key, "primary") for key in primary_keys
    )
    duplicate_lanes: tuple[Lane, ...] = tuple(
        (key, "determinism_duplicate") for key in duplicate_keys
    )
    lanes = primary_lanes + duplicate_lanes
    primary_index = {
        key: lane for lane, (key, _role) in enumerate(primary_lanes)
    }
    duplicate_index = {
        key: len(primary_lanes) + offset
        for offset, key in enumerate(duplicate_keys)
    }
    family_states = family["states"]
    assert isinstance(family_states, dict)
    initial_states = tuple(
        family_states[key] for key, _role in lanes
    )
    columns = pack_states(initial_states)
    initial_columns = columns.copy()
    residual_rows = watched_residual_wires()
    program = family["program"]
    assert isinstance(program, tuple)
    schedule = packed_schedule(program, lanes)
    initial_nonclean = nonclean_mask(columns, residual_rows)
    previous_nonclean = initial_nonclean
    earlier_nonclean_counts = {
        key: int(bool(initial_nonclean & (1 << primary_index[key])))
        for key in primary_keys
    }
    snapshots: dict[int, dict[Key, tuple[int, ...]]] = {}
    resolution_rows: dict[int, dict[str, object]] = {}
    recurrence_candidates = divisors(LCM_SKELETON)
    recurrence_rows: dict[int, dict[str, object]] = {}
    representative = COHORT_KEYS[0][0]
    representative_lane = primary_index[representative]
    determinism_rows = []

    def determinism_checkpoint(moment: int) -> None:
        rows = tuple({
            "key": key,
            "primary_sha256":
                state_sha256(unpack_lane(columns, primary_index[key])),
            "duplicate_sha256":
                state_sha256(unpack_lane(columns, duplicate_index[key])),
            "exact_tuple_equal": (
                unpack_lane(columns, primary_index[key])
                == unpack_lane(columns, duplicate_index[key])
            ),
        } for key in duplicate_keys)
        determinism_rows.append({
            "moment": moment,
            "rows": rows,
            "all_exact": all(row["exact_tuple_equal"] for row in rows),
        })

    determinism_checkpoint(0)
    one_step = columns.copy()
    advance(one_step, schedule)
    words = family["words"]
    assert isinstance(words, dict)
    one_step_rows = tuple({
        "key": key,
        "packed_sha256":
            state_sha256(unpack_lane(one_step, primary_index[key])),
        "scalar_sha256": state_sha256(K.A.apply_semantic(
            family_states[key], words[key[1]]
        )),
        "exact": (
            unpack_lane(one_step, primary_index[key])
            == K.A.apply_semantic(family_states[key], words[key[1]])
        ),
    } for key in primary_keys)
    duplicate_initial_exact = all(
        initial_states[primary_index[key]]
        == initial_states[duplicate_index[key]]
        for key in duplicate_keys
    )
    duplicate_masks_identical = all(
        ((mask >> primary_index[key]) & 1)
        == ((mask >> duplicate_index[key]) & 1)
        for _kind, _first, _second, _third, mask in schedule
        for key in duplicate_keys
    )

    for moment in range(1, max(RESOLUTION_MOMENTS.values()) + 1):
        advance(columns, schedule)
        nonclean = nonclean_mask(columns, residual_rows)
        if moment in set(FUNNEL_MOMENTS.values()):
            event = next(
                row for row, target in FUNNEL_MOMENTS.items()
                if target == moment
            )
            snapshots[event] = {
                key: unpack_lane(columns, primary_index[key])
                for key in COHORT_KEYS[event]
            }
            determinism_checkpoint(moment)
        if moment in recurrence_candidates and moment <= FUNNEL_MOMENTS[0]:
            state = unpack_lane(columns, representative_lane)
            recurrence_rows[moment] = {
                "candidate_period": moment,
                "divides_lcm_skeleton":
                    LCM_SKELETON % moment == 0,
                "bounded_test": "state(0) == state(period)",
                "exact_return_to_initial":
                    state == family_states[representative],
                "observed_state_sha256": state_sha256(state),
                "initial_state_sha256":
                    state_sha256(family_states[representative]),
                "verdict":
                    "HIT" if state == family_states[representative]
                    else "FAIL",
            }
        if moment in set(RESOLUTION_MOMENTS.values()):
            event = next(
                row for row, target in RESOLUTION_MOMENTS.items()
                if target == moment
            )
            keys = COHORT_KEYS[event]
            resolution_rows[event] = {
                "event": event,
                "moment": moment,
                "keys": keys,
                "earlier_nonclean_counts": tuple(
                    earlier_nonclean_counts[key] for key in keys
                ),
                "every_earlier_moment_nonclean": all(
                    earlier_nonclean_counts[key] == moment for key in keys
                ),
                "veto_at_t_minus_1": all(
                    previous_nonclean & (1 << primary_index[key])
                    for key in keys
                ),
                "supports_at_resolution": tuple(
                    support_at_lane(
                        columns, primary_index[key], residual_rows
                    )
                    for key in keys
                ),
                "all_landed_clean": all(
                    not support_at_lane(
                        columns, primary_index[key], residual_rows
                    )
                    for key in keys
                ),
            }
            resolution_rows[event]["pass"] = (
                resolution_rows[event]["every_earlier_moment_nonclean"]
                and resolution_rows[event]["veto_at_t_minus_1"]
                and resolution_rows[event]["all_landed_clean"]
            )
            determinism_checkpoint(moment)
        for key in primary_keys:
            if moment < RESOLUTION_MOMENTS[key[0]]:
                earlier_nonclean_counts[key] += int(
                    bool(nonclean & (1 << primary_index[key]))
                )
        previous_nonclean = nonclean

    for candidate in recurrence_candidates:
        if candidate > FUNNEL_MOMENTS[0]:
            recurrence_rows[candidate] = {
                "candidate_period": candidate,
                "divides_lcm_skeleton":
                    LCM_SKELETON % candidate == 0,
                "bounded_test": None,
                "exact_return_to_initial": None,
                "verdict": "UNTESTABLE_ABOVE_DECLARED_PRE_FUNNEL_BOUND",
            }
    determinism_checkpoint(max(RESOLUTION_MOMENTS.values()))
    return {
        "primary_keys": primary_keys,
        "duplicate_keys": duplicate_keys,
        "schedule_instruction_count": len(schedule),
        "one_step_rows": one_step_rows,
        "duplicate_initial_exact": duplicate_initial_exact,
        "duplicate_masks_identical": duplicate_masks_identical,
        "determinism_rows": tuple(determinism_rows),
        "snapshots": snapshots,
        "resolution_rows": tuple(
            resolution_rows[event] for event in EVENTS
        ),
        "recurrence_rows": tuple(
            recurrence_rows[candidate]
            for candidate in recurrence_candidates
        ),
        "residual_rows": residual_rows,
        "pass": (
            all(row["exact"] for row in one_step_rows)
            and duplicate_initial_exact
            and duplicate_masks_identical
            and all(row["all_exact"] for row in determinism_rows)
            and all(row["pass"] for row in resolution_rows.values())
        ),
    }


def funnel_anatomies(
    dynamics: dict[str, object],
) -> dict[str, object]:
    snapshots = dynamics["snapshots"]
    assert isinstance(snapshots, dict)
    residual_rows = dynamics["residual_rows"]
    assert isinstance(residual_rows, tuple)
    rows = []
    representative_states = {}
    for event in EVENTS:
        state_map = snapshots[event]
        keys = COHORT_KEYS[event]
        states = tuple(state_map[key] for key in keys)
        representative = states[0]
        representative_states[event] = representative
        support = tuple(
            name for name, wire in residual_rows if representative[wire]
        )
        partition = state_partition(keys, states)
        rows.append({
            "event": event,
            "funnel_moment": FUNNEL_MOMENTS[event],
            "resolution_moment": RESOLUTION_MOMENTS[event],
            "state_sha256": state_sha256(representative),
            "full_state_hamming_weight": sum(representative),
            "landed_residual_support": support,
            "landed_residual_support_weight": len(support),
            "landed_support_component_counts": dict(sorted(Counter(
                name.split(".", 1)[0] for name in support
            ).items())),
            "nine_key_exact_state_partition": partition,
            "synchronization_component_count": len(partition),
            "synchronization_component_sizes":
                tuple(row["size"] for row in partition),
            "all_nine_exactly_synchronized": len(partition) == 1,
        })
    pairwise = {
        "event2_vs_event1": sum(
            left != right for left, right in zip(
                representative_states[2], representative_states[1]
            )
        ),
        "event2_vs_event0": sum(
            left != right for left, right in zip(
                representative_states[2], representative_states[0]
            )
        ),
        "event1_vs_event0": sum(
            left != right for left, right in zip(
                representative_states[1], representative_states[0]
            )
        ),
    }
    expected_hashes = COPIED_831_COHORTS["funnel_state_sha256"]
    return {
        "rows": tuple(rows),
        "pairwise_funnel_diff_weights": pairwise,
        "cycle830_component_structure": {
            key: value for key, value in COPIED_830_ANATOMY.items()
            if key in {
                "node_occupancy_reverse_depth_0_through_8",
                "shared_pair_counts_reverse_depth_0_through_8",
                "key_distinguishing_wires_reverse_depth_0_through_8",
                "forward_partition_relations_depth_8_through_0",
            }
        },
        "copied_hashes_reconstructed_exactly": all(
            row["state_sha256"] == expected_hashes[row["event"]]
            for row in rows
        ),
        "copied_pairwise_diff_weights_reconstructed_exactly":
            pairwise
            == COPIED_831_COHORTS["pairwise_funnel_diff_weights"],
        "cycle830_Sstar_weight_reconstructed_exactly":
            next(
                row for row in rows if row["event"] == 0
            )["full_state_hamming_weight"]
            == COPIED_830_ANATOMY["Sstar_hamming_weight"],
        "all_three_nine_key_synchronizations_exact":
            all(row["all_nine_exactly_synchronized"] for row in rows),
    }


def backbone_classification_certificate(
    sources: dict[str, object],
) -> dict[str, object]:
    strict_rows = sources["cycle818_period_rows"]
    assert isinstance(strict_rows, tuple)
    strict_period3_keys = tuple(sorted(
        (
            int(row["event"]),
            tuple(int(position) for position in row["positions"]),
        )
        for row in strict_rows
        if int(row["k"]) == 2 and int(row["period"]) == 3
    ))
    catalog_by_key = {
        (
            int(row["event"]),
            tuple(int(position) for position in row["positions"]),
        ): row
        for row in strict_rows
    }
    landed_resolved = (
        set(EARLIER_RESOLVED)
        | set(COHORT_KEYS[2])
        | set(COHORT_KEYS[1])
    )
    classification_rows = []
    for event, pair in BACKBONE_KEYS:
        if event in EVENTS:
            classification_rows.append({
                "key": (event, pair),
                "classification": "TRANSIENT_COHORT",
                "cohort_event": event,
                "resolution_moment": RESOLUTION_MOMENTS[event],
                "landed_resolution_provenance": (
                    "EARLIER_RESOLVED"
                    if event == 0 else f"COHORT_KEYS[{event}]"
                ),
                "resolved": (event, pair) in landed_resolved,
            })
        else:
            catalog_row = catalog_by_key.get((event, pair))
            classification_rows.append({
                "key": (event, pair),
                "classification": "CERTIFIED_PERIOD_3_CYCLE",
                "cohort_event": event,
                "period": (
                    None if catalog_row is None
                    else int(catalog_row["period"])
                ),
                "preperiod": (
                    None if catalog_row is None
                    else int(catalog_row["preperiod"])
                ),
                "landed_resolution_provenance":
                    "Cycle818 strict PERIOD_TABLE_ROW",
                "resolved": (
                    (event, pair) in landed_resolved
                    and catalog_row is not None
                    and bool(catalog_row["pass"])
                ),
            })
    open_keys = open_pair_event_keys()
    open_backbone = tuple(
        row for row in open_keys if row[0] in set(BACKBONE)
    )
    event_census = dict(sorted(Counter(
        event for _pair, event in open_keys
    ).items()))
    period_census = dict(sorted(Counter(
        int(row["period"]) for row in strict_rows
    ).items()))
    transient_rows = tuple(
        row for row in classification_rows
        if row["classification"] == "TRANSIENT_COHORT"
    )
    cyclic_rows = tuple(
        row for row in classification_rows
        if row["classification"] == "CERTIFIED_PERIOD_3_CYCLE"
    )
    exact = (
        len(BACKBONE_KEYS) == 36
        and len(set(BACKBONE_KEYS)) == 36
        and len(transient_rows) == 27
        and len(cyclic_rows) == 9
        and all(row["resolved"] for row in classification_rows)
        and strict_period3_keys == tuple(sorted(EVENT3_BACKBONE_KEYS))
        and len(strict_rows) == 14
        and period_census == {2: 2, 3: 9, 288: 1, 4464: 2}
        and all(
            row["period"] == 3 and row["preperiod"] == 0
            for row in cyclic_rows
        )
        and len(open_keys) == 133
        and event_census == {0: 34, 1: 34, 2: 34, 3: 31}
        and not open_backbone
    )
    return {
        "verdict": "PASS" if exact else "FAIL",
        "finding": (
            "The complete k=2 nine-pair backbone has 36 keys: 27 are "
            "the three landed transient cohorts and the event-3 nine are "
            "exactly the nine period-3 rows in the Cycle818 strict table."
        ),
        "lawful_events": LAWFUL_EVENTS,
        "backbone_pairs": BACKBONE,
        "backbone_key_count": len(BACKBONE_KEYS),
        "backbone_keys": BACKBONE_KEYS,
        "classification_rows": tuple(classification_rows),
        "classification_census": {
            "TRANSIENT_COHORT": len(transient_rows),
            "CERTIFIED_PERIOD_3_CYCLE": len(cyclic_rows),
        },
        "cycle818_catalog_provenance": {
            "source_path": AUDIT_INPUT_PATHS[1],
            "source_sha256": EXPECTED_SHA256[AUDIT_INPUT_PATHS[1]],
            "source_git_blob": EXPECTED_GIT_BLOBS[AUDIT_INPUT_PATHS[1]],
            "cache_path": CYCLE818_CATALOG_CACHE_PATH,
            "cache_sha256":
                EXPECTED_SHA256[CYCLE818_CATALOG_CACHE_PATH],
            "cache_git_blob":
                EXPECTED_GIT_BLOBS[CYCLE818_CATALOG_CACHE_PATH],
            "strict_row_count": len(strict_rows),
            "strict_period_census": period_census,
        },
        "cycle818_strict_period3_keys": strict_period3_keys,
        "event3_backbone_keys": EVENT3_BACKBONE_KEYS,
        "catalog_period3_keys_equal_event3_backbone":
            strict_period3_keys == tuple(sorted(EVENT3_BACKBONE_KEYS)),
        "all_36_resolved": all(
            row["resolved"] for row in classification_rows
        ),
        "open_key_count": len(open_keys),
        "open_event_census": event_census,
        "open_keys_on_backbone": open_backbone,
        "all_133_open_keys_off_backbone": (
            len(open_keys) == 133 and not open_backbone
        ),
        "event3_open_off_backbone_key_count": event_census.get(3, 0),
        "pass": exact,
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


def state_as_int(state: tuple[int, ...]) -> int:
    return sum(bit << wire for wire, bit in enumerate(state))


def int_state_sha256(state: int) -> str:
    width = (STATE_BITS + 7) // 8
    return sha256(state.to_bytes(width, "little")).hexdigest()


def cycle_cohort_certificate(
    family: dict[str, object],
    catalog: dict[str, object],
    anatomies: dict[str, object],
) -> dict[str, object]:
    keys = EVENT3_BACKBONE_KEYS
    family_states = family["states"]
    words = family["words"]
    assert isinstance(family_states, dict)
    assert isinstance(words, dict)
    states = [state_as_int(family_states[key]) for key in keys]
    initial_states = tuple(states)
    schedules = tuple(
        compile_gate_word(words[key[1]]) for key in keys
    )
    gate_counts = tuple(len(schedule) for schedule in schedules)
    if len(set(gate_counts)) != 1:
        raise AssertionError(("unaligned cycle word lengths", gate_counts))
    gates_per_movement = gate_counts[0]
    state_width = (STATE_BITS + 7) // 8
    dense_hasher = sha256()
    component_count_census: Counter[int] = Counter()
    pairwise_all_checkpoint_equal = {
        (left, right): True
        for left in range(len(keys))
        for right in range(left + 1, len(keys))
    }

    def exact_partition() -> tuple[tuple[Key, ...], ...]:
        groups: dict[int, list[Key]] = {}
        for key, state in zip(keys, states):
            groups.setdefault(state, []).append(key)
        return tuple(tuple(group) for group in groups.values())

    def dense_checkpoint(movement: int, gate: int) -> None:
        partition = exact_partition()
        component_count_census[len(partition)] += 1
        dense_hasher.update(movement.to_bytes(1, "little"))
        dense_hasher.update(gate.to_bytes(2, "little"))
        for state in states:
            dense_hasher.update(state.to_bytes(state_width, "little"))
        for pair in pairwise_all_checkpoint_equal:
            pairwise_all_checkpoint_equal[pair] &= (
                states[pair[0]] == states[pair[1]]
            )

    def phase_boundary_row(movement: int) -> dict[str, object]:
        partition = exact_partition()
        return {
            "movement": movement,
            "aligned_gate": 0 if movement == 0 else gates_per_movement,
            "state_sha256_by_key": tuple(
                (key, int_state_sha256(state))
                for key, state in zip(keys, states)
            ),
            "state_hamming_weight_by_key": tuple(
                (key, state.bit_count())
                for key, state in zip(keys, states)
            ),
            "exact_state_partition": partition,
            "component_count": len(partition),
            "component_sizes": tuple(
                len(group) for group in partition
            ),
            "all_nine_exactly_synchronized": len(partition) == 1,
        }

    phase_rows = [phase_boundary_row(0)]
    phase_state_vectors = [tuple(states)]
    dense_checkpoint(0, 0)
    for movement in range(1, 4):
        for gate_index in range(gates_per_movement):
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
            dense_checkpoint(movement, gate_index + 1)
        phase_rows.append(phase_boundary_row(movement))
        phase_state_vectors.append(tuple(states))

    trajectory_groups = []
    remaining = set(range(len(keys)))
    while remaining:
        representative = min(remaining)
        group_indices = tuple(
            lane for lane in sorted(remaining)
            if lane == representative
            or pairwise_all_checkpoint_equal[
                (min(representative, lane), max(representative, lane))
            ]
        )
        trajectory_groups.append(tuple(keys[lane] for lane in group_indices))
        remaining.difference_update(group_indices)

    anatomy_by_event = {
        int(row["event"]): row for row in anatomies["rows"]
    }
    movement_table = tuple(
        {
            "movement": index,
            "event": event,
            "class": "TRANSIENT_COHORT",
            "key_count": 9,
            "funnel_state_hamming_weight":
                anatomy_by_event[event]["full_state_hamming_weight"],
            "resolution_moment": RESOLUTION_MOMENTS[event],
            "period": None,
        }
        for index, event in enumerate(EVENTS, start=1)
    ) + ({
        "movement": 4,
        "event": 3,
        "class": "CYCLIC_PERIOD_3_NOT_IDENTICAL_IN_PHASE",
        "key_count": 9,
        "funnel_state_hamming_weight": None,
        "resolution_moment": None,
        "period": 3,
        "phase_boundary_component_sizes": tuple(
            row["component_sizes"] for row in phase_rows
        ),
        "phase_boundary_weight_vectors": tuple(
            tuple(weight for _key, weight in row[
                "state_hamming_weight_by_key"
            ])
            for row in phase_rows
        ),
    },)
    catalog_period3_keys = tuple(
        catalog["cycle818_strict_period3_keys"]
    )
    dense_checkpoint_count = 1 + 3 * gates_per_movement
    all_close_at_three = tuple(states) == initial_states
    no_earlier_return = all(
        phase_state_vectors[movement][lane] != initial_states[lane]
        for movement in (1, 2)
        for lane in range(len(keys))
    )
    identical_in_phase = len(trajectory_groups) == 1
    exact_structure = (
        tuple(row["component_sizes"] for row in phase_rows)
        == ((1, 3, 3, 2), (1, 3, 3, 2), (9,), (1, 3, 3, 2))
        and tuple(sorted(component_count_census.items()))
        == (
            (1, 1), (2, 1), (3, 2), (4, 5), (5, 333),
            (6, 1724), (7, 6277), (8, 7098), (9, 3196),
        )
        and len(trajectory_groups) == 9
    )
    exact = (
        catalog_period3_keys == tuple(sorted(keys))
        and gate_counts == (6212,) * 9
        and dense_checkpoint_count == 18637
        and sum(component_count_census.values()) == dense_checkpoint_count
        and all_close_at_three
        and no_earlier_return
        and not identical_in_phase
        and exact_structure
        and tuple(
            anatomy_by_event[event]["full_state_hamming_weight"]
            for event in EVENTS
        ) == (44, 45, 46)
    )
    return {
        "verdict": "PASS" if exact else "FAIL",
        "hypothesis": (
            "The nine event-3 period-3 backbone trajectories are one "
            "identical-in-phase object at every aligned gate checkpoint."
        ),
        "hypothesis_outcome": (
            "FAILS_EXACTLY" if not identical_in_phase else "HOLDS"
        ),
        "finding": (
            "All nine keys are minimal period-3 cycles, but not one "
            "identical-in-phase trajectory.  The movement-boundary "
            "partition is 1+3+3+2 -> 1+3+3+2 -> 9 -> 1+3+3+2; only the "
            "phase-2 boundary is common, and dense trajectories are nine "
            "singletons."
        ),
        "keys": keys,
        "catalog_period3_keys_exact": (
            catalog_period3_keys == tuple(sorted(keys))
        ),
        "gates_per_movement_by_key": tuple(zip(keys, gate_counts)),
        "full_period_dense_checkpoint_count": dense_checkpoint_count,
        "dense_checkpoint_definition": (
            "initial full 5815-bit state plus every aligned gate boundary "
            "for 6212 gates in each of three movements"
        ),
        "dense_state_stream_sha256": dense_hasher.hexdigest(),
        "dense_component_count_census":
            dict(sorted(component_count_census.items())),
        "phase_boundary_rows": tuple(phase_rows),
        "all_nine_close_at_movement_3": all_close_at_three,
        "no_key_returns_at_movements_1_or_2": no_earlier_return,
        "minimal_period_3_live_replay": (
            all_close_at_three and no_earlier_return
        ),
        "identical_in_phase": identical_in_phase,
        "dense_trajectory_partition": tuple(trajectory_groups),
        "dense_trajectory_component_sizes": tuple(
            len(group) for group in trajectory_groups
        ),
        "exact_structure_found": exact_structure,
        "four_movement_table": movement_table,
        "pass": exact,
    }


def arithmetic_certificate() -> dict[str, object]:
    gaps = tuple({
        "left": row["left"],
        "right": row["right"],
        "gap": row["right"] - row["left"],
        "lcm_skeleton": LCM_SKELETON,
        "residual": row["residual"],
        "reconstruction": LCM_SKELETON + row["residual"],
        "exact": (
            row["right"] - row["left"]
            == LCM_SKELETON + row["residual"]
        ),
    } for row in TRANSITIONS)
    factorizations = tuple({
        "value": value,
        "factorization": factorization(value),
        "reconstruction": factor_product(factorization(value)),
    } for value in (4464, 5952, LCM_SKELETON, 595, 64))
    clock_rows = tuple({
        "clock": clock,
        "quotient": divmod(LCM_SKELETON, clock)[0],
        "remainder": divmod(LCM_SKELETON, clock)[1],
        "divides_17856": LCM_SKELETON % clock == 0,
        "verdict": "HIT" if LCM_SKELETON % clock == 0 else "FAIL",
    } for clock in LANDED_CLOCKS)
    result = {
        "gap_decompositions": gaps,
        "gcd_4464_5952": gcd(4464, 5952),
        "stdlib_lcm_4464_5952": lcm(4464, 5952),
        "factorizations": factorizations,
        "landed_clock_divisibility_rows": clock_rows,
        "dividing_clocks": tuple(
            row["clock"] for row in clock_rows if row["divides_17856"]
        ),
        "nondividing_clocks": tuple(
            row["clock"] for row in clock_rows if not row["divides_17856"]
        ),
    }
    result["pass"] = (
        all(row["exact"] for row in gaps)
        and result["gcd_4464_5952"] == 1488
        and result["stdlib_lcm_4464_5952"] == LCM_SKELETON
        and all(
            row["reconstruction"] == row["value"]
            for row in factorizations
        )
        and result["dividing_clocks"]
        == (2, 3, 288, 4464, 5952, 8928)
        and result["nondividing_clocks"] == (8930,)
        and factorization(595) == ((5, 1), (7, 1), (17, 1))
        and factorization(64) == ((2, 6),)
    )
    return result


def exact_test(
    scope: str,
    transition: dict[str, int],
    relation: str,
    left: int,
    right: int,
) -> dict[str, object]:
    return {
        "scope": scope,
        "transition":
            (transition["source_event"], transition["target_event"]),
        "residual": transition["residual"],
        "relation": relation,
        "left": left,
        "right": right,
        "verdict": "HIT" if left == right else "FAIL",
    }


def residual_certificate(
    anatomies: dict[str, object],
) -> dict[str, object]:
    event_rows = []
    for transition in TRANSITIONS:
        residual = transition["residual"]
        source = transition["source_event"]
        target = transition["target_event"]
        comparisons = (
            ("residual_equals_source_event", residual, source),
            ("residual_equals_target_event", residual, target),
            ("residual_equals_absolute_event_jump",
             residual, abs(target - source)),
            ("residual_mod_4_equals_target_event", residual % 4, target),
            ("residual_parity_equals_target_parity",
             residual % 2, target % 2),
        )
        event_rows.extend(
            exact_test("EVENT_INDICES", transition, label, left, right)
            for label, left, right in comparisons
        )

    anatomy_values = []
    anatomy_rows = anatomies["rows"]
    assert isinstance(anatomy_rows, tuple)
    for row in anatomy_rows:
        event = row["event"]
        anatomy_values.extend((
            (f"event{event}.full_state_hamming_weight",
             row["full_state_hamming_weight"]),
            (f"event{event}.landed_residual_support_weight",
             row["landed_residual_support_weight"]),
            (f"event{event}.synchronization_component_count",
             row["synchronization_component_count"]),
        ))
        anatomy_values.extend(
            (f"event{event}.synchronization_component_size[{index}]", value)
            for index, value in enumerate(
                row["synchronization_component_sizes"]
            )
        )
    for label, value in (
        anatomies["pairwise_funnel_diff_weights"].items()
    ):
        anatomy_values.append((f"pairwise_diff.{label}", value))
    for label in (
        "node_occupancy_reverse_depth_0_through_8",
        "shared_pair_counts_reverse_depth_0_through_8",
        "key_distinguishing_wires_reverse_depth_0_through_8",
    ):
        for depth, value in enumerate(COPIED_830_ANATOMY[label]):
            anatomy_values.append((f"cycle830.{label}[{depth}]", value))
    anatomy_relation_rows = tuple(
        exact_test(
            "FUNNEL_ANATOMY", transition,
            f"residual_equals_{label}", transition["residual"], int(value)
        )
        for transition in TRANSITIONS
        for label, value in anatomy_values
    )

    landed_rows = []
    for transition in TRANSITIONS:
        residual = transition["residual"]
        for clock in LANDED_CLOCKS:
            landed_rows.extend((
                {
                    "scope": "LANDED_CONSTANTS",
                    "transition": (
                        transition["source_event"],
                        transition["target_event"],
                    ),
                    "residual": residual,
                    "clock": clock,
                    "relation": "residual_equals_clock",
                    "verdict": "HIT" if residual == clock else "FAIL",
                },
                {
                    "scope": "LANDED_CONSTANTS",
                    "transition": (
                        transition["source_event"],
                        transition["target_event"],
                    ),
                    "residual": residual,
                    "clock": clock,
                    "relation": "residual_divides_clock",
                    "quotient": divmod(clock, residual)[0],
                    "remainder": divmod(clock, residual)[1],
                    "verdict": "HIT" if clock % residual == 0 else "FAIL",
                },
                {
                    "scope": "LANDED_CONSTANTS",
                    "transition": (
                        transition["source_event"],
                        transition["target_event"],
                    ),
                    "residual": residual,
                    "clock": clock,
                    "relation": "clock_divides_residual",
                    "quotient": divmod(residual, clock)[0],
                    "remainder": divmod(residual, clock)[1],
                    "verdict": "HIT" if residual % clock == 0 else "FAIL",
                },
            ))

    moment_mod_rows = tuple({
        "scope": "MOMENT_RESIDUES_SMALL_CLOCKS",
        "subject_kind": subject_kind,
        "subject_label": label,
        "value": value,
        "clock": clock,
        "quotient": divmod(value, clock)[0],
        "remainder": divmod(value, clock)[1],
        "verdict": "HIT" if value % clock == 0 else "FAIL",
    } for subject_kind, label, value in (
        *(("moment", f"event{event}", moment)
          for event, moment in zip(EVENTS, MOMENTS)),
        *(("residual", f"{row['source_event']}->{row['target_event']}",
           row["residual"]) for row in TRANSITIONS),
    ) for clock in SMALL_CLOCKS)
    transition_mod_rows = tuple({
        "scope": "MOMENT_RESIDUE_TRANSITION_IDENTITY",
        "transition": (
            row["source_event"], row["target_event"]
        ),
        "clock": clock,
        "left_moment_remainder": row["left"] % clock,
        "right_moment_remainder": row["right"] % clock,
        "observed_modular_increment":
            (row["right"] - row["left"]) % clock,
        "residual_remainder": row["residual"] % clock,
        "verdict": (
            "HIT"
            if (row["right"] - row["left"]) % clock
            == row["residual"] % clock
            else "FAIL"
        ),
    } for row in TRANSITIONS for clock in SMALL_CLOCKS)

    candidate_rows = tuple({
        "law": law,
        "transition_rows": tuple({
            "source_event": row["source_event"],
            "target_event": row["target_event"],
            "observed_residual": row["residual"],
            "law_residual":
                candidate_residual(
                    law, row["source_event"], row["target_event"]
                ),
            "verdict": (
                "HIT"
                if candidate_residual(
                    law, row["source_event"], row["target_event"]
                ) == row["residual"]
                else "FAIL"
            ),
        } for row in TRANSITIONS),
        "status": "CANDIDATE_TWO_POINTS_CANNOT_PROVE",
    } for law in ("TARGET_PARITY_LOOKUP", "ABS_EVENT_JUMP_LOOKUP"))
    candidate_rows = tuple({
        **row,
        "survives": all(
            test["verdict"] == "HIT"
            for test in row["transition_rows"]
        ),
    } for row in candidate_rows)
    survivors = tuple(
        row["law"] for row in candidate_rows if row["survives"]
    )
    result = {
        "residual_factorizations": tuple({
            "residual": row["residual"],
            "factorization": factorization(row["residual"]),
        } for row in TRANSITIONS),
        "event_index_relation_rows": tuple(event_rows),
        "funnel_anatomies": anatomies,
        "anatomy_numeric_universe": tuple(anatomy_values),
        "anatomy_equality_rows": anatomy_relation_rows,
        "landed_constant_relation_rows": tuple(landed_rows),
        "moment_and_residual_small_clock_rows": moment_mod_rows,
        "transition_modular_identity_rows": transition_mod_rows,
        "candidate_law_rows": candidate_rows,
        "surviving_candidate_laws": survivors,
        "interpretation":
            "Every declared equality/divisibility/zero-remainder test prints "
            "HIT or FAIL.  The two lookup candidates each interpolate only "
            "two points and are not promoted to laws.",
    }
    result["pass"] = (
        all(
            row["verdict"] in {"HIT", "FAIL"}
            for row in (
                *result["event_index_relation_rows"],
                *result["anatomy_equality_rows"],
                *result["landed_constant_relation_rows"],
                *result["moment_and_residual_small_clock_rows"],
                *result["transition_modular_identity_rows"],
            )
        )
        and all(
            row["verdict"] == "HIT"
            for row in result["transition_modular_identity_rows"]
        )
        and survivors
        == ("TARGET_PARITY_LOOKUP", "ABS_EVENT_JUMP_LOOKUP")
        and anatomies["copied_hashes_reconstructed_exactly"]
        and anatomies[
            "copied_pairwise_diff_weights_reconstructed_exactly"
        ]
        and anatomies["cycle830_Sstar_weight_reconstructed_exactly"]
        and anatomies["all_three_nine_key_synchronizations_exact"]
    )
    return result


def prediction_certificate(
    preregistration: dict[str, object],
    residuals: dict[str, object],
    family: dict[str, object],
) -> dict[str, object]:
    historical_v1_prediction_status = (
        "PREDICTED_PRE_REGISTERED_AND_SURVIVED_B"
    )
    open_keys = open_pair_event_keys()
    family_states = family["states"]
    assert isinstance(family_states, dict)
    catalog_pair_event = tuple(
        (key[1], key[0]) for key in sorted(
            family_states, key=lambda key: (key[1], key[0])
        )
    )
    resolved = (
        set(EARLIER_RESOLVED)
        | set(COHORT_KEYS[2])
        | set(COHORT_KEYS[1])
    )
    reconstructed = tuple(
        row for row in catalog_pair_event
        if (row[1], row[0]) not in resolved
    )
    prereg_laws = {
        row["law"]: row
        for row in preregistration["candidate_laws"]
    }
    survivors = residuals["surviving_candidate_laws"]
    historical_predictions = tuple({
        "law": law,
        "historical_v1_status": historical_v1_prediction_status,
        "v2_status": "RETRACTED_AS_VACUOUS_AT_K2_BACKBONE",
        "event3_row": next(
            row for row in prereg_laws[law][
                "predictions_from_current_event_1"
            ]
            if row["next_event"] == 3
        ),
    } for law in survivors)
    backbone_open = tuple(
        row for row in open_keys if row[0] in set(BACKBONE)
    )
    event3_open_off_backbone = tuple(
        row for row in open_keys if row[1] == 3
    )
    prediction_values = {
        row["law"]:
            row["event3_row"]["predicted_next_cohort_moment"]
        for row in historical_predictions
    }
    result = {
        "verdict": "PASS",
        "open_pair_event_keys": open_keys,
        "open_key_count": len(open_keys),
        "open_event_census": dict(sorted(Counter(
            event for _pair, event in open_keys
        ).items())),
        "open_keys_on_nine_pair_backbone": backbone_open,
        "literal_backbone_result":
            "NO TRANSIENT TARGET: the event-3 backbone nine are period-3 "
            "cycles and the event-0/2/1 backbone cohorts are resolved.",
        "candidate_laws_surviving_B": survivors,
        "historical_v1_event3_predictions": historical_predictions,
        "historical_live_conflict": prediction_values,
        "prediction_reruling":
            "RETRACTED_AS_VACUOUS_AT_K2_BACKBONE",
        "reruling_reason": (
            "Completing the 36-key backbone removes the assumed next "
            "transient cohort-moment target.  The event-3 backbone keys "
            "are cycles and therefore have no transient resolution moment."
        ),
        "lawful_rescope": "NONE_ON_THE_CURRENT_LANDED_SURFACE",
        "lawful_rescope_detail": (
            "The 31 open event-3 keys are off-backbone individual keys; "
            "no landed certificate groups them into a common cohort with "
            "one resolution moment or a transition from the event-1 "
            "backbone cohort.  Thus neither 69035 nor 69566 currently has "
            "an observable cohort-moment target."
        ),
        "event3_open_off_backbone_keys": event3_open_off_backbone,
        "fallback_lcm_skeleton_if_candidates_fail":
            preregistration["fallback_bounded_forecast"],
        "enumeration_reconstructed_from_176_key_family_exactly":
            reconstructed == open_keys,
        "pre_registered_open_enumeration_unchanged":
            preregistration["open_pair_event_keys"] == open_keys,
    }
    result["pass"] = (
        len(open_keys) == 133
        and not backbone_open
        and len(event3_open_off_backbone) == 31
        and reconstructed == open_keys
        and result["pre_registered_open_enumeration_unchanged"]
        and len(historical_predictions) == len(survivors) == 2
        and prediction_values == {
            "TARGET_PARITY_LOOKUP": 69035,
            "ABS_EVENT_JUMP_LOOKUP": 69566,
        }
        and result["lawful_rescope"]
        == "NONE_ON_THE_CURRENT_LANDED_SURFACE"
    )
    return result


def recurrence_certificate(
    dynamics: dict[str, object],
) -> dict[str, object]:
    rows = dynamics["recurrence_rows"]
    assert isinstance(rows, tuple)
    tested = tuple(
        row for row in rows if row["exact_return_to_initial"] is not None
    )
    hits = tuple(
        row["candidate_period"] for row in tested
        if row["exact_return_to_initial"]
    )
    untestable = tuple(
        row["candidate_period"] for row in rows
        if row["exact_return_to_initial"] is None
    )
    result = {
        "key": COHORT_KEYS[0][0],
        "configuration": "full landed 5815-bit data state",
        "pre_funnel_window_inclusive": (0, FUNNEL_MOMENTS[0]),
        "candidate_period_rule": "every positive divisor of 17856",
        "autonomous_reversible_equivalence":
            "For the fixed reversible update, any state(t)=state(t+p) "
            "implies state(0)=state(p); testing returns to t=0 is therefore "
            "an exact recurrence-period test, not a hash surrogate.",
        "candidate_rows": rows,
        "tested_candidate_count": len(tested),
        "exact_recurrence_hits": hits,
        "untestable_above_bound": untestable,
        "mechanism_candidate": (
            {"status": "CANDIDATE", "periods": hits}
            if hits else
            {
                "status": "HONEST_OPEN",
                "reading":
                    "No state-recurrence period dividing 17856 was found "
                    "within the declared pre-funnel bound.",
            }
        ),
    }
    result["pass"] = (
        tuple(row["candidate_period"] for row in rows)
        == divisors(LCM_SKELETON)
        and all(row["divides_lcm_skeleton"] for row in rows)
        and not hits
        and untestable == (LCM_SKELETON,)
    )
    return result


def moment_prediction_reruling_certificate(
    arithmetic: dict[str, object],
    residuals: dict[str, object],
    predictions: dict[str, object],
    recurrence: dict[str, object],
) -> dict[str, object]:
    exact = (
        bool(arithmetic["pass"])
        and bool(residuals["pass"])
        and bool(predictions["pass"])
        and bool(recurrence["pass"])
        and arithmetic["stdlib_lcm_4464_5952"] == LCM_SKELETON
        and tuple(
            row["residual"]
            for row in arithmetic["gap_decompositions"]
        ) == (595, 64)
        and predictions["prediction_reruling"]
        == "RETRACTED_AS_VACUOUS_AT_K2_BACKBONE"
        and predictions["lawful_rescope"]
        == "NONE_ON_THE_CURRENT_LANDED_SURFACE"
    )
    return {
        "verdict": "PASS" if exact else "FAIL",
        "finding": (
            "The v1 arithmetic survives unchanged: 17856 is the LCM "
            "skeleton and the observed residuals are 595 and 64.  The "
            "parity/jump extrapolations do not survive as predictions: "
            "their conflicting event-3 values 69035 and 69566 have no "
            "k=2 backbone cohort-moment target and no current lawful "
            "off-backbone rescope."
        ),
        "lcm_structure_v1_reproduced": arithmetic,
        "residual_census_v1_reproduced": residuals,
        "prediction_reruling": predictions,
        "bounded_recurrence_probe_v1_reproduced": recurrence,
        "pass": exact,
    }


def v1_retraction_certificate(
    catalog: dict[str, object],
    family: dict[str, object],
) -> dict[str, object]:
    exact = (
        V1_EXHAUSTION_CLAIM_VERBATIM
        == (
            "The literal nine-pair backbone is exhausted by the 27 keys "
            "in the three event cohorts (0, 2, 1)."
        )
        and family["summary"]["events"] == 2 * FIXTURE_BANKS == 4
        and tuple(range(2 * FIXTURE_BANKS)) == LAWFUL_EVENTS
        and catalog["backbone_key_count"] == 36
        and catalog["classification_census"] == {
            "TRANSIENT_COHORT": 27,
            "CERTIFIED_PERIOD_3_CYCLE": 9,
        }
        and catalog["all_36_resolved"]
    )
    return {
        "verdict": "PASS" if exact else "FAIL",
        "v1_claim_retracted_verbatim": V1_EXHAUSTION_CLAIM_VERBATIM,
        "disposition": "RETRACTED",
        "corrected_statement": (
            "At k=2 there are four events per pair.  The literal nine-pair "
            "backbone therefore has 36 keys: 27 transient-cohort keys and "
            "nine event-3 period-3 cycle keys; all 36 are resolved."
        ),
        "four_event_module_provenance": {
            "path": AUDIT_INPUT_PATHS[0],
            "sha256": EXPECTED_SHA256[AUDIT_INPUT_PATHS[0]],
            "git_blob": EXPECTED_GIT_BLOBS[AUDIT_INPUT_PATHS[0]],
            "module": (
                "frontier_cycle719_two_rail_recurrent_controller_core_"
                "2026_07_26"
            ),
            "function": "held_certificate(bank_count)",
            "event_loop_expression": "range(2 * bank_count)",
            "event_chain_bank_expression": "2 * bank_count",
            "reported_events_expression": "2 * bank_count",
            "cycle832_live_seed_function": "build_seed_family()",
            "cycle832_seed_event_loop_expression":
                "range(2 * FIXTURE_BANKS)",
            "fixture_banks": FIXTURE_BANKS,
            "lawful_events": LAWFUL_EVENTS,
            "live_family_event_count": family["summary"]["events"],
        },
        "pass": exact,
    }


def render(
    preregistration: dict[str, object],
    checks: dict[str, bool],
    certificates: dict[str, object],
    report: dict[str, object],
) -> str:
    lines = [
        "V1_HISTORICAL_PRE_REGISTRATION_RETRACTED "
        + compact(preregistration),
    ]
    lines.extend(
        f"CHECK {name}={str(value).lower()}"
        for name, value in checks.items()
    )
    lines.extend(
        f"CERTIFICATE {name} " + compact(value)
        for name, value in certificates.items()
    )
    lines.append("SUMMARY_JSON " + compact(report))
    lines.append(str(report["terminal"]))
    return "\n".join(lines) + "\n"


def stable_render(
    preregistration: dict[str, object],
    checks: dict[str, bool],
    certificates: dict[str, object],
    report: dict[str, object],
) -> str:
    for _attempt in range(20):
        report["checks"] = dict(checks)
        report["pass"] = all(checks.values())
        report["terminal"] = (
            "CYCLE832_V2_36_KEY_BACKBONE_EXACT_PASS"
            if report["pass"]
            else "CYCLE832_V2_36_KEY_BACKBONE_HONEST_FAIL"
        )
        output = render(
            preregistration, checks, certificates, report
        )
        size = len(output.encode())
        controls = certificates["E_CONTROLS"]
        if report["stdout_bytes"] == size and controls["stdout_bytes"] == size:
            return output
        report["stdout_bytes"] = size
        controls["stdout_bytes"] = size
    raise AssertionError("stdout byte fixed point did not converge")


def run() -> int:
    started = monotonic()
    # Historical v1 bookkeeping is frozen before v2 verification.
    preregistration = build_preregistration()
    sources = source_controls()
    family = build_seed_family()
    dynamics = evolve_funnels(family)
    anatomies = funnel_anatomies(dynamics)
    certificate_a = backbone_classification_certificate(sources)
    certificate_b = cycle_cohort_certificate(
        family, certificate_a, anatomies
    )
    cycle_replay_duplicate = cycle_cohort_certificate(
        family, certificate_a, anatomies
    )
    arithmetic = arithmetic_certificate()
    residuals = residual_certificate(anatomies)
    predictions = prediction_certificate(
        preregistration, residuals, family
    )
    recurrence = recurrence_certificate(dynamics)
    certificate_c = moment_prediction_reruling_certificate(
        arithmetic, residuals, predictions, recurrence
    )
    certificate_d = v1_retraction_certificate(certificate_a, family)
    elapsed = monotonic() - started
    cycle_replay_deterministic = (
        digest(certificate_b) == digest(cycle_replay_duplicate)
        and certificate_b["dense_state_stream_sha256"]
        == cycle_replay_duplicate["dense_state_stream_sha256"]
    )
    deterministic = (
        dynamics["duplicate_initial_exact"]
        and dynamics["duplicate_masks_identical"]
        and all(
            row["all_exact"] for row in dynamics["determinism_rows"]
        )
        and cycle_replay_deterministic
    )
    controls_base = (
        sources["pass"]
        and family["summary"]["pass"]
        and dynamics["pass"]
        and deterministic
        and not any(
            name in sys.modules for name in BLOCKLISTED_MODULES
        )
        and not FIREWALL.hits
        and elapsed < AUDIT_TIMEOUT_SEC
    )
    public_sources = {
        key: value for key, value in sources.items()
        if key != "cycle818_period_rows"
    }
    controls = {
        **public_sources,
        "family": family["summary"],
        "exact_arithmetic":
            "All moments, factors, residues, GF(2) state evolution, state "
            "equality, Hamming weights, and component counts use exact "
            "Python integers; only monotonic runtime is a float.",
        "independent_dynamics": {
            "direct_dynamic_imports": (
                "frontier_cycle719_two_rail_recurrent_controller_core_"
                "2026_07_26",
            ),
            "source_primary_outputs_consumed": False,
            "primary_lanes": len(dynamics["primary_keys"]),
            "duplicate_lanes": len(dynamics["duplicate_keys"]),
            "packed_schedule_instructions":
                dynamics["schedule_instruction_count"],
            "one_step_scalar_equivalence_rows":
                dynamics["one_step_rows"],
            "resolution_rows": dynamics["resolution_rows"],
        },
        "determinism": {
            "keys": dynamics["duplicate_keys"],
            "initial_exact": dynamics["duplicate_initial_exact"],
            "all_schedule_masks_identical":
                dynamics["duplicate_masks_identical"],
            "checkpoints": dynamics["determinism_rows"],
            "cycle_replay_first_sha256":
                certificate_b["dense_state_stream_sha256"],
            "cycle_replay_second_sha256":
                cycle_replay_duplicate["dense_state_stream_sha256"],
            "cycle_replay_certificates_exact":
                digest(certificate_b) == digest(cycle_replay_duplicate),
            "cycle_replay_deterministic": cycle_replay_deterministic,
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
        "pass": controls_base,
    }
    checks = {
        "A_36_KEY_BACKBONE_CLASSIFIED": bool(certificate_a["pass"]),
        "B_CYCLE_COHORT_HYPOTHESIS_RERULED": bool(certificate_b["pass"]),
        "C_MOMENT_PREDICTIONS_RERULED": bool(certificate_c["pass"]),
        "D_V1_EXHAUSTION_RETRACTED": bool(certificate_d["pass"]),
        "E_CONTROLS": controls_base,
    }
    certificates = {
        "A_36_KEY_BACKBONE": certificate_a,
        "B_CYCLE_COHORT_HYPOTHESIS": certificate_b,
        "C_MOMENT_PREDICTION_RERULING": certificate_c,
        "D_V1_RETRACTION": certificate_d,
        "E_CONTROLS": controls,
    }
    report = {
        "cycle": 832,
        "version": 2,
        "target": "36-key backbone and cycle-cohort hypothesis",
        "backbone_keys": certificate_a["backbone_key_count"],
        "backbone_classification":
            certificate_a["classification_census"],
        "all_backbone_keys_resolved": certificate_a["all_36_resolved"],
        "cycle_cohort_hypothesis":
            certificate_b["hypothesis_outcome"],
        "cycle_exact_structure": certificate_b["finding"],
        "lcm_skeleton": LCM_SKELETON,
        "residuals": tuple(row["residual"] for row in TRANSITIONS),
        "prediction_reruling":
            predictions["prediction_reruling"],
        "prediction_lawful_rescope": predictions["lawful_rescope"],
        "historical_prediction_conflict":
            predictions["historical_live_conflict"],
        "open_keys": certificate_a["open_key_count"],
        "v1_exhaustion_claim": certificate_d["disposition"],
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "checks": {},
        "pass": False,
        "terminal": "CYCLE832_V2_36_KEY_BACKBONE_HONEST_FAIL",
    }
    output = stable_render(
        preregistration, checks, certificates, report
    )
    stdout_ok = len(output.encode()) < STDOUT_LIMIT_BYTES
    checks["E_CONTROLS"] = controls_base and stdout_ok
    controls["pass"] = checks["E_CONTROLS"]
    output = stable_render(
        preregistration, checks, certificates, report
    )
    if len(output.encode()) >= STDOUT_LIMIT_BYTES:
        sys.stdout.write(compact({
            "pass": False,
            "failure": "stdout limit exceeded",
            "stdout_bytes": len(output.encode()),
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
            "terminal": "CYCLE832_V2_36_KEY_BACKBONE_HONEST_FAIL",
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
            "terminal": "CYCLE832_COHORT_MOMENT_LAW_HONEST_FAIL",
        }) + "\n")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
