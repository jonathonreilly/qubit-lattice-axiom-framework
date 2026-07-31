#!/usr/bin/env python3
"""Cycle 846: reduced pair braids and the completed-family delay law.

The runner independently decodes the landed Cycle-830 literal fixture bank
and reimplements the Boolean X/CNOT/Toffoli evolution with Python integers.
Named source primaries are SHA-pinned, import-blocklisted, and consumed only
as text/AST.  Sibling lineage is pinned by commit and git-blob identity.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
STDOUT_LIMIT_BYTES = 200 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle830_sstar_preimage_tree_2026_07_28.py",
    "scripts/frontier_cycle833_funnel_family_2026_07_28.py",
    "scripts/frontier_cycle841_deciding_the_tick_2026_07_28.py",
)

import ast
import base64
from fractions import Fraction
from hashlib import sha1, sha256
import importlib.abc
from itertools import combinations
import json
from math import lcm
from pathlib import Path
import struct
import subprocess
import sys
from time import monotonic
import zlib


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_BRANCH = "physics-loop/proof-grade-blockP19-20260729"
EXPECTED_BASE = "e71b3b8ae91a72dcaad68f7efacc97874776f834"
RING_STATIONS = 11
STATE_BITS = 5815
STATE_BYTES = (STATE_BITS + 7) // 8
FAMILY_SIZE = 176
GATE_COUNT = 3106
WORD_GATE_COUNT = 6212
MEET_CONTROLLER_TICK = 3
NORMALIZED_DEPTH = 64
LCM_SKELETON = lcm(4464, 5952)
EVENT_ORDER = (0, 2, 1)
CHRONOLOGICAL_PAIR_ORDER = (1, 2, 0)
NINE_MOMENTS = {0: 14744, 2: 33195, 1: 51115}
NINE_FUNNEL_MOMENTS = {
    event: moment - 5 for event, moment in NINE_MOMENTS.items()
}
PAIR_MOMENTS = {1: 193210, 2: 246669, 0: 1142432}
PAIR_FUNNEL_MOMENTS = {
    event: moment - 5 for event, moment in PAIR_MOMENTS.items()
}
NINE_WEIGHTS = {0: 44, 2: 45, 1: 46}
PAIR_WEIGHTS = {0: 49, 2: 51, 1: 57}
PULSE_WEIGHT = 59
S0_PRIME_WEIGHT = 47
COHORT_RESIDUALS = (595, 64)
PAIR_POSITIONS = ((0, 5), (0, 6))
BACKBONE = (
    (1, 6), (1, 7), (2, 7), (2, 8), (3, 8),
    (3, 9), (4, 9), (4, 10), (5, 10),
)
REGISTER_WIRES = (
    1, 6, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51,
    52, 53, 54, 55, 71, 75, 76, 77, 78, 79, 80, 82, 83,
    84, 86, 87, 89, 105, 109, 110, 111, 112, 113, 114, 116,
    117,
)

EXPECTED_SOURCE_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "b14262f6d54dc4f853bda13f321c816b3e762fa37b0b8276a2bec4955c51c481",
    AUDIT_INPUT_PATHS[1]:
        "bd08f5f503e532c724e6ae28915ba2f0b4202360bbe01458924d689e27c79174",
    AUDIT_INPUT_PATHS[2]:
        "9879f900590b2a9cdded11d2b691d48adf5c5baff96af4f88b7483bfc98a0b54",
}
EXPECTED_SOURCE_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "1afe4941812f83f5e1fd5cc7c04e57231d703e8d",
    AUDIT_INPUT_PATHS[1]: "b3512e0c3e8acdec7bc3f1cfb4e5bf1a236f8fda",
    AUDIT_INPUT_PATHS[2]: "379bbe1f4d7ae3432488359fbf3009adfe2a5984",
}
COPIED_LINEAGE_PINS = {
    "cycle830": {
        "commit": "2bc4c4d6111a0e260b8b6107cd82e57dcbaa1744",
        "path": AUDIT_INPUT_PATHS[0],
        "git_blob": "98b1571228ad0902301b6853208ef249ea2c2973",
    },
    "cycle838": {
        "commit": "7a42ba01f4f549550b1dcfadbefb9aaedce1c0c3",
        "path": "scripts/frontier_cycle838_k3_trio_forecast_2026_07_28.py",
        "git_blob": "2f89c8eb911375bed58b1126e9f5f7b860ead20a",
    },
    "cycle844": {
        "commit": "d6f32365378db0a714a7111ed69cdee68e86cc6c",
        "path": "scripts/frontier_cycle844_standing_bets_2026_07_28.py",
        "git_blob": "a12245720a7e866134978c25629e19ba57596929",
    },
    "cycle845": {
        "commit": "4f97118a3a5b0831e075d5050d538658abaad115",
        "path": "scripts/frontier_cycle845_partition_route_2026_07_28.py",
        "git_blob": "3c7a6e61bbc656b7c6b69b96be36066d0ad1e8e8",
    },
}
EXPECTED_GATE_RAW_SHA256 = (
    "1ef101b5745147bd43c116d87e2774635657e520d744b380bd8bad6d27884f4c"
)
EXPECTED_FAMILY_RAW_SHA256 = (
    "54fbb59c9d2232e77af6204f0c01b079148560bef1409cc74f311b5373784282"
)
EXPECTED_SSTAR_PACKED_SHA256 = (
    "aa15cde162d859356852859309ddbaba74c502ce385212abd476b97405326320"
)

Pair = tuple[int, int]
Key = tuple[int, Pair]
Gate = tuple[int, int, int, int]
MaskedGate = tuple[int, int, int, int, int]
Partition = tuple[tuple[int, ...], ...]

BLOCKLISTED_MODULES = tuple(Path(path).stem for path in AUDIT_INPUT_PATHS)


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
        node.name for node in tree.body
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
    imports = set()
    for node in self_tree.body:
        if isinstance(node, ast.Import):
            imports.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imports.add(node.module.split(".")[0])
    stdlib_roots = set(sys.stdlib_module_names) | {"__future__"}
    lineage_observed = {
        name: git_text(
            "rev-parse", f"{row['commit']}:{row['path']}"
        )
        for name, row in COPIED_LINEAGE_PINS.items()
    }
    lineage_expected = {
        name: row["git_blob"] for name, row in COPIED_LINEAGE_PINS.items()
    }
    ast_basis = {
        "cycle830": {
            "decode_fixtures", "build_words", "apply_word",
            "partition_keys", "trajectory_and_mechanism_certificates",
        } <= function_names(trees[AUDIT_INPUT_PATHS[0]]),
        "cycle833": {
            "reconstruct_funnels", "edge_accounting",
            "rank_edge_field_map_certificate", "unification_certificate",
        } <= function_names(trees[AUDIT_INPUT_PATHS[1]]),
        "cycle841": {
            "clock_definitions", "raw_catchup", "accounting_consequence",
        } <= function_names(trees[AUDIT_INPUT_PATHS[2]]),
    }
    literal_cross_checks = {
        "cycle833_FUNNEL_MOMENTS":
            literal_assignment(
                trees[AUDIT_INPUT_PATHS[1]], "FUNNEL_MOMENTS"
            ) == NINE_FUNNEL_MOMENTS,
        "cycle841_LCM_SKELETON":
            literal_assignment(
                trees[AUDIT_INPUT_PATHS[2]], "COHORT_RESIDUALS"
            ) == COHORT_RESIDUALS,
    }
    blocked_loaded = tuple(sorted(
        name for name in sys.modules
        if name.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES
    ))
    branch = git_text("branch", "--show-current")
    base_is_ancestor = subprocess.run(
        ("git", "merge-base", "--is-ancestor", EXPECTED_BASE, "HEAD"),
        cwd=ROOT,
        check=False,
        timeout=20,
    ).returncode == 0
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
        "maximum_named_files": 8,
        "source_sha256": source_sha,
        "expected_source_sha256": EXPECTED_SOURCE_SHA256,
        "source_git_blobs": source_blobs,
        "expected_source_git_blobs": EXPECTED_SOURCE_GIT_BLOBS,
        "copied_lineage_pins": COPIED_LINEAGE_PINS,
        "copied_lineage_observed_git_blobs": lineage_observed,
        "copied_lineage_expected_git_blobs": lineage_expected,
        "AST_basis": ast_basis,
        "literal_cross_checks": literal_cross_checks,
        "blocked_modules": BLOCKLISTED_MODULES,
        "blocked_modules_loaded_at_start": blocked_loaded,
        "firewall_hits_at_start": tuple(FIREWALL.hits),
        "direct_import_roots": tuple(sorted(imports)),
        "stdlib_only": imports <= stdlib_roots,
        "git_head": git_text("rev-parse", "HEAD"),
        "git_branch": branch,
        "expected_git_branch": EXPECTED_BRANCH,
        "expected_base": EXPECTED_BASE,
        "expected_base_is_ancestor": base_is_ancestor,
        "self_sha256": sha256(self_payload).hexdigest(),
        "self_git_blob": git_blob(self_payload),
    }
    result["pass"] = (
        result["AUDIT_INPUT_PATHS_literal"]
        and result["existing_worktree_relative"]
        and len(AUDIT_INPUT_PATHS) <= 8
        and source_sha == EXPECTED_SOURCE_SHA256
        and source_blobs == EXPECTED_SOURCE_GIT_BLOBS
        and lineage_observed == lineage_expected
        and all(ast_basis.values())
        and all(literal_cross_checks.values())
        and not blocked_loaded
        and not FIREWALL.hits
        and result["stdlib_only"]
        and branch == EXPECTED_BRANCH
        and base_is_ancestor
    )
    return result, trees


def scaffold() -> int:
    source, _trees = source_controls()
    print(compact({
        "cycle": 846,
        "phase": "CONTROL_SCAFFOLD",
        "source_controls": source,
        "pass": source["pass"],
    }))
    return 0 if source["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(scaffold())
