#!/usr/bin/env python3
"""Cycle 837: why separation five?  Exact bounded derivation probe.

This stdlib-only runner reads every landed Python primary as SHA-pinned
text/AST only.  It separates three facts which must not be conflated:
landed key status, literal common-translation controller dynamics, and the
auxiliary undirected radius-one wavefront model on C11.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 200 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle736_pairwise_separated_multisource_2026_07_28.py",
    "scripts/frontier_cycle822_basin_independent_check_2026_07_28.py",
    "scripts/frontier_cycle832_cohort_moment_law_2026_07_28.py",
    "logs/runner-cache/frontier_cycle818_period_structure_census_2026_07_28.txt",
    "logs/runner-cache/frontier_cycle832_cohort_moment_law_2026_07_28.txt",
)

import ast
from hashlib import sha1, sha256
import importlib.abc
import json
from pathlib import Path
import subprocess
import sys
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
PYTHON_PRIMARY_PATHS = AUDIT_INPUT_PATHS[:4]
TEXT_LOG_PATHS = AUDIT_INPUT_PATHS[4:]
BLOCKLISTED_MODULES = tuple(
    Path(path).stem for path in PYTHON_PRIMARY_PATHS
)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "50059ce4d4d6e5ce4503e66ccb098f6fe663ad9711b106b6b6c5c9cb7bcbd02f",
    AUDIT_INPUT_PATHS[2]:
        "c2fd23a7bb47caff70e9561fc9da46feef422c053954fa1af925901a1884ed0b",
    AUDIT_INPUT_PATHS[3]:
        "0db01e80084af4dbb52c74a0a055984edf8ab818f2c8ba8a99c1f6a3fc15bb3e",
    AUDIT_INPUT_PATHS[4]:
        "94bc32640518f097cb09060f9c378d26d73e263539573e3b8e75ed2aab1b857e",
    AUDIT_INPUT_PATHS[5]:
        "89640947e097728e73cbd58a0039364e684dc2e81d840a087fdddd69598bd450",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    AUDIT_INPUT_PATHS[1]: "8ddd84104dc0729107cebfb0d0cd694fe78af1af",
    AUDIT_INPUT_PATHS[2]: "6d48f5d86006a5f6718b5993eaecd5ec69d86112",
    AUDIT_INPUT_PATHS[3]: "d666f5c301ffe6b6508f3636b15814a662bfbe8e",
    AUDIT_INPUT_PATHS[4]: "3544e3beada65b3480d352e2701f6e21b3f9ae2d",
    AUDIT_INPUT_PATHS[5]: "86d14cac924d71a6d4702ffac3dbeacc5c5d0f52",
}
EXPECTED_HEAD = "f3ec9213b4b02457bfc8bc092bf25510297e2813"
EXPECTED_BRANCH = "physics-loop/proof-grade-blockR20-20260729"


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


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode()).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode() + payload).hexdigest()


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


def git_value(*arguments: str) -> str:
    completed = subprocess.run(
        ("git", *arguments),
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
        timeout=10,
    )
    return completed.stdout.strip()


def source_controls() -> tuple[
    dict[str, object],
    dict[str, bytes],
    dict[str, ast.Module],
]:
    payloads = {
        path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS
    }
    trees = {
        path: ast.parse(payloads[path], filename=path)
        for path in PYTHON_PRIMARY_PATHS
    }
    self_tree = ast.parse(
        Path(__file__).read_bytes(), filename=Path(__file__).name
    )
    sha_rows = {
        path: sha256(payload).hexdigest()
        for path, payload in payloads.items()
    }
    blob_rows = {
        path: git_blob(payload) for path, payload in payloads.items()
    }
    branch = git_value("branch", "--show-current")
    head = git_value("rev-parse", "HEAD")
    rows = tuple({
        "path": path,
        "exists": (ROOT / path).is_file(),
        "worktree_relative": not Path(path).is_absolute(),
        "sha256": sha_rows[path],
        "expected_sha256": EXPECTED_SHA256[path],
        "sha256_exact": sha_rows[path] == EXPECTED_SHA256[path],
        "git_blob": blob_rows[path],
        "expected_git_blob": EXPECTED_GIT_BLOBS[path],
        "git_blob_exact": blob_rows[path] == EXPECTED_GIT_BLOBS[path],
        "access": (
            "TEXT_AST_ONLY_BLOCKLISTED"
            if path in PYTHON_PRIMARY_PATHS
            else "TEXT_JSON_LINES_ONLY"
        ),
    } for path in AUDIT_INPUT_PATHS)
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_INPUT_PATHS_literal":
            literal_assignment(self_tree, "AUDIT_INPUT_PATHS")
            == AUDIT_INPUT_PATHS,
        "named_input_count": len(AUDIT_INPUT_PATHS),
        "read_cap": 6,
        "all_paths_existing_worktree_relative": all(
            row["exists"] and row["worktree_relative"] for row in rows
        ),
        "source_rows": rows,
        "python_primaries": PYTHON_PRIMARY_PATHS,
        "python_primary_access": "TEXT_AST_ONLY_BLOCKLISTED",
        "blocked_modules": BLOCKLISTED_MODULES,
        "blocked_modules_loaded": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits": tuple(FIREWALL.hits),
        "git_head": head,
        "expected_git_head": EXPECTED_HEAD,
        "git_head_exact": head == EXPECTED_HEAD,
        "git_branch": branch,
        "expected_git_branch": EXPECTED_BRANCH,
        "git_branch_exact": branch == EXPECTED_BRANCH,
    }
    result["pass"] = (
        result["AUDIT_INPUT_PATHS_literal"]
        and result["named_input_count"] <= result["read_cap"]
        and result["all_paths_existing_worktree_relative"]
        and all(
            row["sha256_exact"] and row["git_blob_exact"] for row in rows
        )
        and not result["blocked_modules_loaded"]
        and not result["firewall_hits"]
        and result["git_head_exact"]
        and result["git_branch_exact"]
    )
    return result, payloads, trees


def main() -> int:
    started = monotonic()
    controls, _payloads, _trees = source_controls()
    elapsed = monotonic() - started
    controls["runtime_seconds"] = round(elapsed, 6)
    controls["runtime_limit_seconds"] = AUDIT_TIMEOUT_SEC
    controls["stdout_limit_bytes"] = STDOUT_LIMIT_BYTES
    controls["pass"] = bool(
        controls["pass"] and elapsed < AUDIT_TIMEOUT_SEC
    )
    output = (
        "CERTIFICATE D_CONTROLS " + compact(controls) + "\n"
        + (
            "CYCLE837_SCAFFOLD_PASS\n"
            if controls["pass"]
            else "CYCLE837_SCAFFOLD_HONEST_FAIL\n"
        )
    )
    sys.stdout.write(output)
    return 0 if controls["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
