#!/usr/bin/env python3
"""Cycle 832: cohort-moment law hunt with pre-registered continuations.

The runner independently rebuilds the landed k=2 family from the Cycle-719
core.  Cycle-818/819/820/822 sources are SHA-pinned text/AST controls and are
blocked from import.  Only compact, explicitly SHA-pinned observations are
copied from the sibling Cycle-830/831 packages; all three funnel states used
by the census are reconstructed here.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
STDOUT_LIMIT_BYTES = 200 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle818_period_structure_census_2026_07_28.py",
    "scripts/frontier_cycle819_deep_k2_continuation_2026_07_28.py",
    "scripts/frontier_cycle820_shared_moment_mechanism_2026_07_28.py",
    "scripts/frontier_cycle822_basin_independent_check_2026_07_28.py",
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
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    AUDIT_INPUT_PATHS[1]: "9c2657e5fa98c4d2bbb561a0f428cf59fca20973",
    AUDIT_INPUT_PATHS[2]: "c3a071835a61e78a4919decfede8534cbf95e1d9",
    AUDIT_INPUT_PATHS[3]: "6385dfa0dce58e86345483cc521ffa325e0d1cce",
    AUDIT_INPUT_PATHS[4]: "6d48f5d86006a5f6718b5993eaecd5ec69d86112",
}

TEXT_AST_ONLY_PATHS = AUDIT_INPUT_PATHS[1:]
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


def source_controls() -> dict[str, object]:
    payloads = {
        path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS
    }
    trees = {
        path: ast.parse(payload.decode(), filename=path)
        for path, payload in payloads.items()
    }
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
        "parseable_ast": isinstance(trees[path], ast.Module),
        "access": "DYNAMIC_IMPORT" if path == AUDIT_INPUT_PATHS[0]
                  else "TEXT_AST_ONLY_BLOCKLISTED",
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
            and row["parseable_ast"]
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
                    "PREDICTED" if residual is not None
                    else "OUTSIDE_LAW_DOMAIN",
            })
        laws.append({
            "law": law,
            "status": "PRE_REGISTERED_CANDIDATE",
            "two_point_warning":
                "Two points cannot prove this law; rival exact lookups are "
                "deliberately retained to expose underdetermination.",
            "predictions_from_current_event_1": tuple(predictions),
        })
    backbone_open = tuple(
        row for row in open_keys if row[0] in set(BACKBONE)
    )
    return {
        "order_statement":
            "This entire PRE_REGISTRATION block is emitted before checks or "
            "verification certificates.",
        "known_last_moment": MOMENTS[-1],
        "lcm_skeleton": LCM_SKELETON,
        "prediction_base": base,
        "fallback_bounded_forecast": {
            "residual_interval_inclusive": (0, 596),
            "moment_interval_inclusive": (base, base + 596),
        },
        "open_key_count": len(open_keys),
        "open_pair_event_keys": open_keys,
        "open_keys_on_nine_pair_backbone": backbone_open,
        "backbone_open_reading":
            "No key on the literal nine-pair backbone remains open; all 133 "
            "open keys are on the other separated pairs.",
        "candidate_laws": tuple(laws),
    }


def render_scaffold(
    preregistration: dict[str, object],
    sources: dict[str, object],
) -> str:
    return "\n".join((
        "PRE_REGISTRATION " + compact(preregistration),
        "CHECK SCAFFOLD_COMPLETE=false",
        "CERTIFICATE E_SCAFFOLD_CONTROLS " + compact(sources),
        "CYCLE832_COHORT_MOMENT_LAW_SCAFFOLD",
    )) + "\n"


def main() -> int:
    preregistration = build_preregistration()
    sources = source_controls()
    sys.stdout.write(render_scaffold(preregistration, sources))
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
