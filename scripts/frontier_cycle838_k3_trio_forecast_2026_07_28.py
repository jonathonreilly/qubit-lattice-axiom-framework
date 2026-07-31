#!/usr/bin/env python3
"""Cycle 838: deep k=3 continuation and the registered trio forecast.

The sole executable science dependency is the landed Cycle-719 controller
core.  Cycles 831 and 834 are SHA-pinned text/AST-only source primaries and
are blocked from import.

Cycle 834 literally lands ten open canonical k=3 representative/event keys,
six of which are the two registered event trios.  It does not literally land
a 33-key open catalog.  This runner exposes that supplied-count mismatch and
never invents 23 keys.  The complete sweep is over all ten literal landed
open keys.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
EXECUTION_BUDGET_SEC = 1425
STDOUT_LIMIT_BYTES = 200 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle831_deep_k2_forecast_tests_2026_07_28.py",
    "scripts/frontier_cycle834_k3_backbone_2026_07_28.py",
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
BLOCKLISTED_MODULES = tuple(
    Path(path).stem for path in TEXT_AST_ONLY_PATHS
)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "624dad4d841e10e24891810dbc500cc4d6ebe871d6f09dd96f89e3189e52e2ff",
    AUDIT_INPUT_PATHS[2]:
        "8ed75c4e6f19fa5e8a9492225aae681ab85017dcfac00f8ab109b7c587aeddaa",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    AUDIT_INPUT_PATHS[1]: "ef24edda08118c4e14439b899790fff6c6f94175",
    AUDIT_INPUT_PATHS[2]: "89d4506c6df9738bf0458027ab76cc9d2f9710ab",
}
EXPECTED_BRANCH = "physics-loop/toe-close-blockC24-20260729"
EXPECTED_BASE = "575254ee97d73f3db6cc11b90bd7333033d38494"


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


RING_STATIONS = 11
FIXTURE_BANKS = 2
STATE_BITS = 5815
WATCHED_COORDINATE_COUNT = 477
LANDED_HORIZON = 65536
TARGET_CHOICES = (262144, 131072, 65536)
PILOT_TICKS = 256
SAFETY_FACTOR = 1.40
RESERVE_SECONDS = 60.0
SUPPLIED_K3_FAMILY_COUNT = 33
DETERMINISM_KEYS = 2

Key = tuple[int, tuple[int, ...], int]
State = bytes
MaskedGate = tuple[int, int, int, int, int]

K3_OPEN_THROUGH_T65536: tuple[Key, ...] = (
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
    key for key in K3_OPEN_THROUGH_T65536
    if key[1] in ((0, 2, 6), (0, 2, 7), (0, 2, 8))
)
NONTRIO_KEYS: tuple[Key, ...] = tuple(
    key for key in K3_OPEN_THROUGH_T65536 if key not in TRIO_KEYS
)
K2_STATION0_S5_OPEN_THROUGH_T65536: tuple[Key, ...] = (
    (2, (0, 5), 0),
    (2, (0, 5), 1),
    (2, (0, 5), 2),
    (2, (0, 6), 0),
    (2, (0, 6), 1),
    (2, (0, 6), 2),
)
IDENTITY_TRANSIENT: tuple[Key, int] = (
    (3, (0, 2, 5), 2),
    444,
)
IDENTITY_CYCLE: tuple[Key, int] = (
    (3, (0, 2, 6), 1),
    5952,
)


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def state_sha256(state: State) -> str:
    return sha256(state).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(
        f"blob {len(payload)}\0".encode("ascii") + payload
    ).hexdigest()


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


def top_level_functions(tree: ast.Module) -> set[str]:
    return {
        node.name
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }


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
    actual_sha = {
        path: sha256(payload).hexdigest()
        for path, payload in payloads.items()
    }
    actual_blobs = {
        path: git_blob(payload) for path, payload in payloads.items()
    }
    markers = {
        AUDIT_INPUT_PATHS[0]:
            {"interleaved_program", "mapped_macro", "run_orbit"},
        AUDIT_INPUT_PATHS[1]:
            {"build_family", "boundary_snapshot"},
        AUDIT_INPUT_PATHS[2]:
            {"forecast_surface", "cycle_cohort_probe"},
    }
    landed_k3 = literal_assignment(
        trees[AUDIT_INPUT_PATHS[2]],
        "LANDED_K3_OPEN_THROUGH_65536",
    )
    landed_trios = literal_assignment(
        trees[AUDIT_INPUT_PATHS[2]], "LANDED_K3_TRANSIENTS"
    )
    landed_cycles = literal_assignment(
        trees[AUDIT_INPUT_PATHS[2]], "LANDED_K3_CYCLES"
    )
    direct_frontier_imports = tuple(sorted(
        alias.name
        for node in self_tree.body
        if isinstance(node, ast.Import)
        for alias in node.names
        if alias.name.startswith("frontier_cycle")
    ))
    branch = git_value("branch", "--show-current")
    base = git_value(
        "merge-base", "HEAD", "physics-loop/toe-close-blockC23-20260729"
    )
    rows = tuple({
        "path": path,
        "exists": (ROOT / path).is_file(),
        "worktree_relative": not Path(path).is_absolute(),
        "sha256": actual_sha.get(path),
        "expected_sha256": EXPECTED_SHA256[path],
        "sha256_exact": actual_sha.get(path) == EXPECTED_SHA256[path],
        "git_blob": actual_blobs.get(path),
        "expected_git_blob": EXPECTED_GIT_BLOBS[path],
        "git_blob_exact":
            actual_blobs.get(path) == EXPECTED_GIT_BLOBS[path],
        "access": (
            "EXECUTABLE_LANDED_CORE"
            if path == CORE_PATH else "TEXT_AST_ONLY_BLOCKLISTED"
        ),
    } for path in AUDIT_INPUT_PATHS)
    provenance = {
        "Cycle834_literal_open_keys": landed_k3,
        "Cycle834_literal_open_count":
            len(landed_k3) if isinstance(landed_k3, tuple) else None,
        "runner_open_keys": K3_OPEN_THROUGH_T65536,
        "literal_catalog_exact":
            landed_k3 == K3_OPEN_THROUGH_T65536,
        "supplied_family_count": SUPPLIED_K3_FAMILY_COUNT,
        "supplied_33_matches_literal_open_count":
            isinstance(landed_k3, tuple)
            and len(landed_k3) == SUPPLIED_K3_FAMILY_COUNT,
        "disposition":
            "COUNT_MISMATCH_EXPOSED_NO_KEYS_INVENTED",
        "identity_transient_landed":
            IDENTITY_TRANSIENT in landed_trios
            if isinstance(landed_trios, tuple) else False,
        "identity_cycle_landed":
            IDENTITY_CYCLE in landed_cycles
            if isinstance(landed_cycles, tuple) else False,
    }
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_INPUT_PATHS_literal":
            literal_assignment(self_tree, "AUDIT_INPUT_PATHS")
            == AUDIT_INPUT_PATHS,
        "named_input_count": len(AUDIT_INPUT_PATHS),
        "maximum_named_inputs": 7,
        "all_paths_existing_worktree_relative": (
            len(payloads) == len(AUDIT_INPUT_PATHS)
            and all(
                row["exists"] and row["worktree_relative"]
                for row in rows
            )
        ),
        "source_rows": rows,
        "AST_markers_present": all(
            markers[path] <= top_level_functions(trees[path])
            for path in AUDIT_INPUT_PATHS
        ),
        "text_AST_only_paths": TEXT_AST_ONLY_PATHS,
        "blocked_modules": BLOCKLISTED_MODULES,
        "blocked_modules_loaded": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits": tuple(FIREWALL.hits),
        "direct_frontier_imports": direct_frontier_imports,
        "provenance": provenance,
        "git_branch": branch,
        "expected_git_branch": EXPECTED_BRANCH,
        "git_branch_exact": branch == EXPECTED_BRANCH,
        "git_base": base,
        "expected_git_base": EXPECTED_BASE,
        "git_base_exact": base == EXPECTED_BASE,
    }
    result["pass"] = (
        result["AUDIT_INPUT_PATHS_literal"]
        and result["named_input_count"] <= result["maximum_named_inputs"]
        and result["all_paths_existing_worktree_relative"]
        and all(row["sha256_exact"] and row["git_blob_exact"] for row in rows)
        and result["AST_markers_present"]
        and direct_frontier_imports
        == (
            "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26",
        )
        and provenance["literal_catalog_exact"]
        and provenance["identity_transient_landed"]
        and provenance["identity_cycle_landed"]
        and not result["blocked_modules_loaded"]
        and not result["firewall_hits"]
        and result["git_branch_exact"]
        and result["git_base_exact"]
    )
    return result


def main() -> int:
    """Scaffold entry point; completed by the next incremental commit."""

    sys.stdout.write(compact({
        "cycle": 838,
        "status": "IMPLEMENTATION_SCAFFOLD",
        "pass": False,
    }) + "\n")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
