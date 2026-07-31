#!/usr/bin/env python3
"""Cycle 845: partition-refinement route for the merged-why question.

All named source primaries are blocked from import and are consumed only as
text/AST.  The landed Cycle-830 literal fixture bank is decoded independently,
and the Boolean X/CNOT/Toffoli evolution is reimplemented with Python integers.

Certificate A computes the full event-0 nine-trajectory partition sequence
from the tick-3 meet to S*, at the declared complete-movement stride, as an
exact reconstructible run-length encoding.  Certificate B compares the last
64 complete movements across cohorts and cross-references every partition
event against the Cycle-835 39-field register change-times.  Certificate C
gives the narrow partition-law verdict.  Certificate D enforces provenance,
BLOCKLIST, determinism, runtime, and stdout controls.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
STDOUT_LIMIT_BYTES = 200 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle830_sstar_preimage_tree_2026_07_28.py",
    "scripts/frontier_cycle835_register_mechanism_2026_07_28.py",
    "scripts/frontier_cycle842_local_causal_theorem_2026_07_28.py",
)

import ast
import base64
from hashlib import sha1, sha256
import importlib.abc
from itertools import combinations
import json
from pathlib import Path
import struct
import subprocess
import sys
from time import monotonic
import zlib


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_BRANCH = "physics-loop/proof-grade-blockR23-20260729"
RING_STATIONS = 11
FIXTURE_BANKS = 2
FAMILY_SIZE = 176
STATE_BITS = 5815
STATE_BYTES = (STATE_BITS + 7) // 8
GATE_COUNT = 3106
WORD_GATE_COUNT = 6212
MEET_CONTROLLER_TICK = 3
PARTITION_STRIDE_CONTROLLER_TICKS = RING_STATIONS
CROSS_COHORT_WINDOW_MOVEMENTS = 64
EVENT_ORDER = (0, 2, 1)
FUNNEL_MOMENTS = {0: 14739, 2: 33190, 1: 51110}
BACKBONE = (
    (1, 6), (1, 7), (2, 7), (2, 8), (3, 8),
    (3, 9), (4, 9), (4, 10), (5, 10),
)
WITNESS_PAIR = BACKBONE[0]
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
# Mechanically copied from the SHA-pinned Cycle-835 trajectory certificate.
REGISTER_WIRES = (
    1, 6, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51,
    52, 53, 54, 55, 71, 75, 76, 77, 78, 79, 80, 82, 83,
    84, 86, 87, 89, 105, 109, 110, 111, 112, 113, 114, 116,
    117,
)
EXPECTED_FUNNEL_SHA256 = {
    0: "cdf7e03092c6278b686c1f0edb9ebd716f4a285b1eabc8a7e2780695284a8f1a",
    2: "0015151ee4b751c35a5671fbb4f301d8569e78fc5a7ebe9f77372865b153c99b",
    1: "797fa122a629177c00c707aff4857d01bbad16b078983e3a6f1f5b632e094a41",
}
EXPECTED_FUNNEL_WEIGHTS = {0: 44, 2: 45, 1: 46}
EXPECTED_CHANGE_TIME_UNIQUE_SEQUENCES = 74
EXPECTED_CHANGE_TIME_RAW_BYTES = 203926
EXPECTED_CHANGE_TIME_RAW_SHA256 = (
    "3d588a959c0f461859b41931a104237adcd2df5e33bd29aa7457811cca0d702d"
)
EXPECTED_GATE_RAW_SHA256 = (
    "1ef101b5745147bd43c116d87e2774635657e520d744b380bd8bad6d27884f4c"
)
EXPECTED_FAMILY_RAW_SHA256 = (
    "54fbb59c9d2232e77af6204f0c01b079148560bef1409cc74f311b5373784282"
)
EXPECTED_SSTAR_PACKED_SHA256 = (
    "aa15cde162d859356852859309ddbaba74c502ce385212abd476b97405326320"
)
EXPECTED_SOURCE_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "40d8cfb99b65fa251599bbf07f6a4399fd5bda9ad1e9e12e24db9395c4737d58",
    AUDIT_INPUT_PATHS[2]:
        "6b8c26ff77d99225aaa985c645aeee9fa1fb3db19517aec727ff38e0cbcc03f5",
    AUDIT_INPUT_PATHS[3]:
        "65ced87db73db177c561e0dd293ae88963c15929d820f6dd99417a27ba647def",
}
EXPECTED_SOURCE_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    AUDIT_INPUT_PATHS[1]: "98b1571228ad0902301b6853208ef249ea2c2973",
    AUDIT_INPUT_PATHS[2]: "a9bfc3d151a591b3d0a4ba06acaa30ed04ff7e67",
    AUDIT_INPUT_PATHS[3]: "a1836d84d8dda74c4f79cc1bbc60ef798d86a2e3",
}
COPIED_LINEAGE_PINS = {
    "cycle830": {
        "commit": "2bc4c4d6111a0e260b8b6107cd82e57dcbaa1744",
        "source_sha256": EXPECTED_SOURCE_SHA256[AUDIT_INPUT_PATHS[1]],
        "git_blob": EXPECTED_SOURCE_GIT_BLOBS[AUDIT_INPUT_PATHS[1]],
    },
    "cycle835": {
        "commit": "1522d92ec6",
        "source_sha256": EXPECTED_SOURCE_SHA256[AUDIT_INPUT_PATHS[2]],
        "git_blob": EXPECTED_SOURCE_GIT_BLOBS[AUDIT_INPUT_PATHS[2]],
    },
}

Pair = tuple[int, int]
Key = tuple[int, Pair]
Gate = tuple[int, int, int, int]
MaskedGate = tuple[int, int, int, int, int]
Partition = tuple[tuple[int, ...], ...]

BLOCKLISTED_MODULES = tuple(Path(path).stem for path in AUDIT_INPUT_PATHS)


class _PrimaryFirewall(importlib.abc.MetaPathFinder):
    """Fail closed if any text/AST-only source primary is imported."""

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


def git_text(*arguments: str) -> str:
    return subprocess.run(
        ("git", *arguments),
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
        timeout=20,
    ).stdout.strip()


def literal_assignment(tree: ast.Module, name: str) -> object | None:
    values = []
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


def function_names(tree: ast.Module) -> set[str]:
    return {
        node.name
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }


def source_controls() -> tuple[dict[str, object], dict[str, ast.Module]]:
    payloads = {
        path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS
    }
    trees = {
        path: ast.parse(payload, filename=path)
        for path, payload in payloads.items()
    }
    self_payload = Path(__file__).read_bytes()
    self_tree = ast.parse(self_payload, filename=Path(__file__).name)
    source_sha = {
        path: sha256(payload).hexdigest()
        for path, payload in payloads.items()
    }
    source_blobs = {
        path: git_blob(payload) for path, payload in payloads.items()
    }
    ast_basis = {
        "cycle719_core": {
            "interleaved_program", "run_orbit",
        } <= function_names(trees[AUDIT_INPUT_PATHS[0]]),
        "cycle830_partition_lineage": {
            "decode_fixtures", "partition_keys",
            "trajectory_and_mechanism_certificates",
        } <= function_names(trees[AUDIT_INPUT_PATHS[1]]),
        "cycle835_register_lineage": {
            "track_register_trajectories", "change_time_encoding",
            "register_wires",
        } <= function_names(trees[AUDIT_INPUT_PATHS[2]]),
        "cycle842_meet_lineage": {
            "meeting_geometry", "evolve_bounded_forward",
            "certificate_b_forward_argument",
        } <= function_names(trees[AUDIT_INPUT_PATHS[3]]),
    }
    imports = set()
    for node in self_tree.body:
        if isinstance(node, ast.Import):
            imports.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imports.add(node.module.split(".")[0])
    stdlib_roots = set(sys.stdlib_module_names) | {"__future__"}
    literal_cross_checks = {
        "cycle835_REGISTER_FIELDS":
            literal_assignment(
                trees[AUDIT_INPUT_PATHS[2]], "REGISTER_FIELDS"
            ) == REGISTER_FIELDS,
        "cycle835_FUNNEL_MOMENTS":
            literal_assignment(
                trees[AUDIT_INPUT_PATHS[2]], "FUNNEL_MOMENTS"
            ) == FUNNEL_MOMENTS,
        "cycle835_BACKBONE":
            literal_assignment(
                trees[AUDIT_INPUT_PATHS[2]], "BACKBONE"
            ) == BACKBONE,
        "cycle842_MEET_CONTROLLER_TICK":
            literal_assignment(
                trees[AUDIT_INPUT_PATHS[3]], "MEET_CONTROLLER_TICK"
            ) == MEET_CONTROLLER_TICK,
        "cycle842_EXPECTED_REACHING_KEYS":
            literal_assignment(
                trees[AUDIT_INPUT_PATHS[3]], "EXPECTED_REACHING_KEYS"
            ) == tuple((0, pair) for pair in BACKBONE),
    }
    blocked_loaded = tuple(sorted(
        name for name in sys.modules
        if name.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES
    ))
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_INPUT_PATHS_literal":
            literal_assignment(self_tree, "AUDIT_INPUT_PATHS")
            == AUDIT_INPUT_PATHS,
        "existing_worktree_relative": all(
            not Path(path).is_absolute() and (ROOT / path).is_file()
            for path in AUDIT_INPUT_PATHS
        ),
        "plain_reading_named_files": len(AUDIT_INPUT_PATHS),
        "maximum_named_files": 7,
        "source_sha256": source_sha,
        "expected_source_sha256": EXPECTED_SOURCE_SHA256,
        "source_git_blobs": source_blobs,
        "expected_source_git_blobs": EXPECTED_SOURCE_GIT_BLOBS,
        "copied_lineage_pins": COPIED_LINEAGE_PINS,
        "AST_basis": ast_basis,
        "literal_cross_checks": literal_cross_checks,
        "blocked_modules": BLOCKLISTED_MODULES,
        "blocked_modules_loaded_at_start": blocked_loaded,
        "firewall_hits_at_start": tuple(FIREWALL.hits),
        "direct_import_roots": tuple(sorted(imports)),
        "stdlib_only": imports <= stdlib_roots,
        "git_head": git_text("rev-parse", "HEAD"),
        "git_branch": git_text("branch", "--show-current"),
        "expected_git_branch": EXPECTED_BRANCH,
        "self_sha256": sha256(self_payload).hexdigest(),
        "self_git_blob": git_blob(self_payload),
    }
    result["pass"] = (
        result["AUDIT_INPUT_PATHS_literal"]
        and result["existing_worktree_relative"]
        and len(AUDIT_INPUT_PATHS) <= 7
        and source_sha == EXPECTED_SOURCE_SHA256
        and source_blobs == EXPECTED_SOURCE_GIT_BLOBS
        and all(ast_basis.values())
        and all(literal_cross_checks.values())
        and not blocked_loaded
        and not FIREWALL.hits
        and result["stdlib_only"]
        and result["git_branch"] == EXPECTED_BRANCH
    )
    return result, trees


def cyclic_separation(pair: Pair) -> int:
    return min(
        (pair[1] - pair[0]) % RING_STATIONS,
        (pair[0] - pair[1]) % RING_STATIONS,
    )


def lawful_pairs() -> tuple[Pair, ...]:
    return tuple(
        pair for pair in combinations(range(RING_STATIONS), 2)
        if cyclic_separation(pair) > 1
    )


def state_sha256(state: int) -> str:
    return sha256(bytes(
        (state >> wire) & 1 for wire in range(STATE_BITS)
    )).hexdigest()


def packed_sha256(state: int) -> str:
    return sha256(
        state.to_bytes(STATE_BYTES, "little")
    ).hexdigest()


def decode_cycle830_fixtures(
    tree: ast.Module,
) -> dict[str, object]:
    gate_encoded = literal_assignment(tree, "GATE_CONSTANTS_B85")
    family_encoded = literal_assignment(tree, "FAMILY_STATES_B85")
    target_encoded = literal_assignment(tree, "SSTAR_PACKED_B85")
    if not all(isinstance(value, str) for value in (
        gate_encoded, family_encoded, target_encoded
    )):
        raise AssertionError("Cycle-830 literal fixtures not found")
    gate_raw = zlib.decompress(base64.b85decode(gate_encoded))
    family_raw = zlib.decompress(base64.b85decode(family_encoded))
    target_raw = zlib.decompress(base64.b85decode(target_encoded))
    lengths = struct.unpack("<11H", gate_raw[:22])
    offset = 22
    macros = []
    for length in lengths:
        rows = []
        for _index in range(length):
            rows.append(struct.unpack(
                "<BHHH", gate_raw[offset:offset + 7]
            ))
            offset += 7
        macros.append(tuple(rows))
    pairs = lawful_pairs()
    keys = tuple(sorted(
        (event, pair)
        for event in range(2 * FIXTURE_BANKS)
        for pair in pairs
    ))
    states = {}
    for index, key in enumerate(keys):
        start = index * STATE_BYTES
        states[key] = int.from_bytes(
            family_raw[start:start + STATE_BYTES], "little"
        )
    target = int.from_bytes(target_raw, "little")
    public = {
        "macro_gate_counts": lengths,
        "macro_gate_count": sum(lengths),
        "family_key_count": len(states),
        "target_hamming_weight": target.bit_count(),
        "target_state_sha256": state_sha256(target),
        "target_packed_sha256": packed_sha256(target),
        "gate_raw_sha256": sha256(gate_raw).hexdigest(),
        "family_raw_sha256": sha256(family_raw).hexdigest(),
        "pass": (
            len(lengths) == RING_STATIONS
            and sum(lengths) == GATE_COUNT
            and offset == len(gate_raw)
            and sha256(gate_raw).hexdigest() == EXPECTED_GATE_RAW_SHA256
            and len(family_raw) == FAMILY_SIZE * STATE_BYTES
            and sha256(family_raw).hexdigest()
            == EXPECTED_FAMILY_RAW_SHA256
            and len(target_raw) == STATE_BYTES
            and sha256(target_raw).hexdigest()
            == EXPECTED_SSTAR_PACKED_SHA256
            and len(pairs) == 44
            and len(states) == FAMILY_SIZE
            and target.bit_count() == EXPECTED_FUNNEL_WEIGHTS[0]
            and state_sha256(target) == EXPECTED_FUNNEL_SHA256[0]
        ),
    }
    return {
        "macros": tuple(macros),
        "keys": keys,
        "states": states,
        "target": target,
        "public": public,
    }
