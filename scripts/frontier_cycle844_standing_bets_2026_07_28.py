#!/usr/bin/env python3
"""Cycle 844: every standing bet on one exact deep continuation.

The landed Cycle-719 controller core is the sole executable science
dependency.  Cycles 834, 838, and 843 are SHA-pinned text/AST-only source
primaries and are import-blocklisted.  The runner sweeps the ten literal
landed open k=3 keys and the two named station-0 event-0 k=2 keys.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
EXECUTION_BUDGET_SEC = 1450
STDOUT_LIMIT_BYTES = 200 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle834_k3_backbone_2026_07_28.py",
    "scripts/frontier_cycle838_k3_trio_forecast_2026_07_28.py",
    "scripts/frontier_cycle843_pulse_phase_2026_07_28.py",
)

import ast
from collections import Counter
from hashlib import sha1, sha256
import importlib.abc
from itertools import combinations
import json
from pathlib import Path
import subprocess
import sys
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
CORE_PATH = AUDIT_INPUT_PATHS[0]
TEXT_AST_ONLY_PATHS = AUDIT_INPUT_PATHS[1:]
BLOCKLISTED_MODULES = tuple(Path(path).stem for path in TEXT_AST_ONLY_PATHS)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "8ed75c4e6f19fa5e8a9492225aae681ab85017dcfac00f8ab109b7c587aeddaa",
    AUDIT_INPUT_PATHS[2]:
        "ea668b4d0be960622cd10d4e16b3cd1056d343db80ee6845407ca6ddb3e604c0",
    AUDIT_INPUT_PATHS[3]:
        "68116221b3451aefd294d939b788cd3dbf518a190eaebd996b43fba5e8a54de9",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    AUDIT_INPUT_PATHS[1]: "89d4506c6df9738bf0458027ab76cc9d2f9710ab",
    AUDIT_INPUT_PATHS[2]: "2f89c8eb911375bed58b1126e9f5f7b860ead20a",
    AUDIT_INPUT_PATHS[3]: "cd500d58847c3c1046c500b73b25911920db0ce0",
}
EXPECTED_BRANCH = "physics-loop/toe-close-blockC26-20260729"
EXPECTED_BASE = "a902a8204b43e616272be79b18ca337f078d84d0"


class _PrimaryFirewall(importlib.abc.MetaPathFinder):
    """Fail closed if a source-only primary is imported."""

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


Key = tuple[int, tuple[int, ...], int]
State = bytes
MaskedGate = tuple[int, int, int, int, int]
RING_STATIONS = 11
FIXTURE_BANKS = 2
STATE_BITS = 5815
WATCHED_COORDINATE_COUNT = 477
LANDED_HORIZON = 262144
K3_TARGET_CHOICES = (524288, 262144, 131072)
K2_TARGET_HORIZON = 2097152
PILOT_TICKS = 256
SAFETY_FACTOR = 1.16
RESERVE_SECONDS = 105.0
CHECKPOINT_INTERVAL = 1024
DETERMINISM_KEYS_PER_FAMILY = 1

K3_KEYS: tuple[Key, ...] = (
    (3, (0, 2, 6), 2),
    (3, (0, 2, 6), 3),
    (3, (0, 2, 7), 2),
    (3, (0, 2, 7), 3),
    (3, (0, 2, 8), 2),
    (3, (0, 2, 8), 3),
    (3, (0, 3, 6), 2),
    (3, (0, 3, 6), 3),
    (3, (0, 3, 7), 2),
    (3, (0, 3, 7), 3),
)
TRIO_KEYS: tuple[Key, ...] = tuple(
    key for key in K3_KEYS
    if key[1] in ((0, 2, 6), (0, 2, 7), (0, 2, 8))
)
OTHER_K3_KEYS: tuple[Key, ...] = tuple(
    key for key in K3_KEYS if key not in TRIO_KEYS
)
K2_EVENT0_KEYS: tuple[Key, ...] = (
    (2, (0, 5), 0),
    (2, (0, 6), 0),
)
K3_IDENTITY = ((3, (0, 2, 5), 2), "TRANSIENT", 444)
K2_IDENTITY = ((2, (0, 5), 1), "TRANSIENT", 193210)
EXPECTED_TARGETS = {
    "S0_prime": {
        "sha256":
            "d874aeeb1d4e5ca29b806886314c796ac32e6658b21f888d8e2aa01044905c12",
        "weight": 47,
    },
    "pulse_coincidence_state": {
        "sha256":
            "4a7ce9fd4e9ebfdbd8580c33122d9e87c3896b24ef196e34bec49e233d044375",
        "weight": 59,
    },
}


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def state_sha256(state: State | tuple[int, ...]) -> str:
    return sha256(bytes(state)).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(
        f"blob {len(payload)}\0".encode("ascii") + payload
    ).hexdigest()


def literal_assignment(tree: ast.Module, name: str) -> object | None:
    matches = []
    for node in tree.body:
        if (
            isinstance(node, ast.Assign)
            and any(
                isinstance(target, ast.Name) and target.id == name
                for target in node.targets
            )
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


def git_value(*arguments: str) -> str:
    completed = subprocess.run(
        ("git", *arguments),
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
        timeout=15,
    )
    return completed.stdout.strip()


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
        Path(__file__).read_bytes(), filename=Path(__file__).name
    )
    source_rows = tuple({
        "path": path,
        "exists_worktree_relative":
            not Path(path).is_absolute() and (ROOT / path).is_file(),
        "sha256": sha256(payloads[path]).hexdigest(),
        "expected_sha256": EXPECTED_SHA256[path],
        "sha256_exact":
            sha256(payloads[path]).hexdigest() == EXPECTED_SHA256[path],
        "git_blob": git_blob(payloads[path]),
        "expected_git_blob": EXPECTED_GIT_BLOBS[path],
        "git_blob_exact":
            git_blob(payloads[path]) == EXPECTED_GIT_BLOBS[path],
        "access": (
            "EXECUTABLE_LANDED_CORE"
            if path == CORE_PATH else "TEXT_AST_ONLY_BLOCKLISTED"
        ),
        "AST_valid": isinstance(trees[path], ast.Module),
    } for path in AUDIT_INPUT_PATHS)
    direct_frontier_imports = tuple(
        alias.name
        for node in self_tree.body if isinstance(node, ast.Import)
        for alias in node.names
        if alias.name.startswith("frontier_cycle")
    )
    landed_keys = literal_assignment(
        trees[AUDIT_INPUT_PATHS[1]], "LANDED_K3_OPEN_THROUGH_65536"
    )
    branch = git_value("branch", "--show-current")
    base_is_ancestor = (
        git_value("merge-base", "HEAD", EXPECTED_BASE) == EXPECTED_BASE
    )
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_INPUT_PATHS_literal":
            literal_assignment(self_tree, "AUDIT_INPUT_PATHS")
            == AUDIT_INPUT_PATHS,
        "named_input_count": len(AUDIT_INPUT_PATHS),
        "maximum_named_inputs": 7,
        "all_paths_existing_worktree_relative":
            len(payloads) == len(AUDIT_INPUT_PATHS)
            and all(row["exists_worktree_relative"] for row in source_rows),
        "source_rows": source_rows,
        "text_AST_only_paths": TEXT_AST_ONLY_PATHS,
        "blocked_modules": BLOCKLISTED_MODULES,
        "direct_frontier_imports": direct_frontier_imports,
        "landed_k3_keys": landed_keys,
        "literal_k3_surface_exact": landed_keys == K3_KEYS,
        "git_branch": branch,
        "expected_git_branch": EXPECTED_BRANCH,
        "expected_base": EXPECTED_BASE,
        "expected_base_is_ancestor": base_is_ancestor,
    }
    result["pass"] = (
        result["AUDIT_INPUT_PATHS_literal"]
        and result["named_input_count"] <= result["maximum_named_inputs"]
        and result["all_paths_existing_worktree_relative"]
        and all(
            row["sha256_exact"] and row["git_blob_exact"]
            and row["AST_valid"] for row in source_rows
        )
        and direct_frontier_imports
        == (
            "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26",
        )
        and result["literal_k3_surface_exact"]
        and branch == EXPECTED_BRANCH
        and base_is_ancestor
        and not any(name in sys.modules for name in BLOCKLISTED_MODULES)
        and not FIREWALL.hits
    )
    return result


def main() -> int:
    print(compact({
        "cycle": 844,
        "status": "INCREMENTAL_SCAFFOLD",
        "terminal": "CYCLE844_STANDING_BETS_HONEST_FAIL",
    }))
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
