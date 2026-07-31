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


def main() -> int:
    """The complete certificate pipeline is added in the next increment."""

    controls, _tree = source_controls()
    certificate, _keys = stratum_populations()
    print("PASS" if certificate["pass"] else "FAIL", "A_STRATUM_POPULATIONS", "::", compact(certificate))
    print("PASS" if controls["pass"] else "FAIL", "E_CONTROLS_SCAFFOLD", "::", compact(controls))
    return 0 if certificate["pass"] and controls["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
