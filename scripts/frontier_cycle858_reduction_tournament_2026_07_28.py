#!/usr/bin/env python3
"""Cycle 858: exact reduction tournament for the 748 multi-source setups.

Only the landed Cycle-719 controller core is executable science input.  The
four later lineage primaries are SHA-pinned, parsed as text/AST controls, and
blocked from import.  The runner independently rebuilds the independent-set
census on C_11, derives the free rotation quotient, tests exact trajectory
conjugacy under the wire permutations that preserve every ordered core
generator, and tests whether each k=2 representative is a composition of its
two single-source trajectories.

The dynamical ladder is deliberately lazy but exact.  Reversibility proves
zero dynamical preperiod for every orbit.  Exact E1/E2 weight prefixes and
state-orbit signatures are evaluated only until a pair is separated.  The
only pairs not separated by t=2 are then followed through their exact minimal
period, with every state compared.  No unresolved numerical period is used
to decide a class.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150_000
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle736_pairwise_separated_multisource_2026_07_28.py",
    "scripts/frontier_cycle801_silent_strata_deep_scan_2026_07_28.py",
    "scripts/frontier_cycle831_deep_k2_forecast_tests_2026_07_28.py",
    "scripts/frontier_cycle847_trio_to_a_million_2026_07_28.py",
)

import ast
from collections import Counter, defaultdict
from hashlib import sha1, sha256
import importlib.abc
from itertools import combinations
import json
from math import ceil, comb, factorial, log2
from pathlib import Path
import subprocess
import sys
from time import monotonic
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
CORE_PATH = AUDIT_INPUT_PATHS[0]
TEXT_AST_ONLY_PATHS = AUDIT_INPUT_PATHS[1:]
BLOCKLISTED_MODULES = tuple(Path(path).stem for path in TEXT_AST_ONLY_PATHS)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "50059ce4d4d6e5ce4503e66ccb098f6fe663ad9711b106b6b6c5c9cb7bcbd02f",
    AUDIT_INPUT_PATHS[2]:
        "55edc0cc8b3e51de3863819f10303d506e0652dbc031a1f2647c3a11e51cb115",
    AUDIT_INPUT_PATHS[3]:
        "624dad4d841e10e24891810dbc500cc4d6ebe871d6f09dd96f89e3189e52e2ff",
    AUDIT_INPUT_PATHS[4]:
        "dab7567b80c9f70488581a9387e654d9bf5e053afcade822576e5a3bd47bba95",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    AUDIT_INPUT_PATHS[1]: "8ddd84104dc0729107cebfb0d0cd694fe78af1af",
    AUDIT_INPUT_PATHS[2]: "8807587899a5664d39a06901b02b22041682c5cc",
    AUDIT_INPUT_PATHS[3]: "ef24edda08118c4e14439b899790fff6c6f94175",
    AUDIT_INPUT_PATHS[4]: "c18478b434b962a42df0b9a46ebc50e50fb30f81",
}
EXPECTED_BRANCH = "physics-loop/toe-close-blockC28-20260729"
EXPECTED_BASE = "ecdd7a73a6"


class _PrimaryFirewall(importlib.abc.MetaPathFinder):
    """Fail closed if a cited source-only primary is imported."""

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
State = tuple[int, ...]
RING_STATIONS = 11
FIXTURE_BANKS = 2
STRATA = (2, 3, 4, 5)
EXPECTED_CONFIGURATION_COUNTS = {2: 44, 3: 77, 4: 55, 5: 11}
EXPECTED_SETUP_COUNTS = {2: 176, 3: 308, 4: 220, 5: 44}
EXPECTED_ORBIT_COUNTS = {2: 16, 3: 28, 4: 20, 5: 4}
EXPECTED_TOTAL_SETUPS = 748
EXPECTED_TOTAL_REPRESENTATIVES = 68
PROFILE_PREFIX_END = 2


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


def function_names(tree: ast.Module) -> set[str]:
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
    markers = {
        AUDIT_INPUT_PATHS[0]: {
            "interleaved_program", "mapped_macro", "run_orbit",
        },
        AUDIT_INPUT_PATHS[1]: {
            "configuration_census", "rotate_config",
        },
        AUDIT_INPUT_PATHS[2]: {
            "initialise_catalog_records", "advance_one_record",
        },
        AUDIT_INPUT_PATHS[3]: {"build_family", "synchronous_word"},
        AUDIT_INPUT_PATHS[4]: {"universal_braid", "run"},
    }
    direct_frontier_imports = tuple(
        alias.name
        for node in self_tree.body if isinstance(node, ast.Import)
        for alias in node.names
        if alias.name.startswith("frontier_cycle")
    )
    rows = tuple({
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
        "AST_valid": isinstance(trees[path], ast.Module),
        "required_AST_markers_present":
            markers[path] <= function_names(trees[path]),
        "access": (
            "EXECUTABLE_LANDED_CORE"
            if path == CORE_PATH else "TEXT_AST_ONLY_BLOCKLISTED_PRIMARY"
        ),
    } for path in AUDIT_INPUT_PATHS)
    branch = git_value("branch", "--show-current")
    base = git_value("rev-parse", EXPECTED_BASE)
    base_is_ancestor = git_value("merge-base", "HEAD", base) == base
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_INPUT_PATHS_literal":
            literal_assignment(self_tree, "AUDIT_INPUT_PATHS")
            == AUDIT_INPUT_PATHS,
        "path_count": len(AUDIT_INPUT_PATHS),
        "read_cap": 6,
        "all_existing_worktree_relative":
            len(payloads) == len(AUDIT_INPUT_PATHS)
            and all(row["exists_worktree_relative"] for row in rows),
        "source_rows": rows,
        "core_path": CORE_PATH,
        "text_AST_only_paths": TEXT_AST_ONLY_PATHS,
        "BLOCKLIST": BLOCKLISTED_MODULES,
        "direct_frontier_imports": direct_frontier_imports,
        "branch": branch,
        "expected_branch": EXPECTED_BRANCH,
        "expected_base": base,
        "expected_base_is_ancestor": base_is_ancestor,
    }
    result["pass"] = (
        result["AUDIT_INPUT_PATHS_literal"]
        and result["path_count"] <= result["read_cap"]
        and result["all_existing_worktree_relative"]
        and all(
            row["sha256_exact"]
            and row["git_blob_exact"]
            and row["AST_valid"]
            and row["required_AST_markers_present"]
            for row in rows
        )
        and direct_frontier_imports == (
            "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26",
        )
        and branch == EXPECTED_BRANCH
        and base_is_ancestor
        and not any(name in sys.modules for name in BLOCKLISTED_MODULES)
        and not FIREWALL.hits
    )
    return result


def independent_positions(count: int) -> tuple[tuple[int, ...], ...]:
    return tuple(
        positions
        for positions in combinations(range(RING_STATIONS), count)
        if all(
            (station + 1) % RING_STATIONS not in positions
            for station in positions
        )
    )


def rotate_positions(
    positions: tuple[int, ...], shift: int
) -> tuple[int, ...]:
    return tuple(sorted(
        (station + shift) % RING_STATIONS for station in positions
    ))


def canonical_rotation(
    positions: tuple[int, ...],
) -> tuple[int, ...]:
    return min(
        rotate_positions(positions, shift)
        for shift in range(RING_STATIONS)
    )


def closed_form_independent_count(stations: int, count: int) -> int:
    numerator = stations * comb(stations - count - 1, count - 1)
    if numerator % count:
        raise AssertionError((stations, count, numerator))
    return numerator // count


def representatives_certificate() -> tuple[
    tuple[Key, ...], dict[str, object]
]:
    representatives: list[Key] = []
    stratum_rows = []
    every_orbit_free = True
    complete_partition = True
    for count in STRATA:
        positions = independent_positions(count)
        expected_configurations = closed_form_independent_count(
            RING_STATIONS, count
        )
        orbit_map: dict[tuple[int, ...], tuple[tuple[int, ...], ...]] = {}
        for representative in sorted({
            canonical_rotation(row) for row in positions
        }):
            orbit = tuple(sorted({
                rotate_positions(representative, shift)
                for shift in range(RING_STATIONS)
            }))
            orbit_map[representative] = orbit
            every_orbit_free &= len(orbit) == RING_STATIONS
        union = {row for orbit in orbit_map.values() for row in orbit}
        complete_partition &= (
            union == set(positions)
            and sum(map(len, orbit_map.values())) == len(positions)
        )
        for event in range(2 * FIXTURE_BANKS):
            representatives.extend(
                (count, representative, event)
                for representative in orbit_map
            )
        stratum_rows.append({
            "k": count,
            "direct_configurations": len(positions),
            "closed_form_configurations": expected_configurations,
            "events": 2 * FIXTURE_BANKS,
            "starting_setups": len(positions) * 2 * FIXTURE_BANKS,
            "C11_orbits_per_event": len(orbit_map),
            "C11_orbits_all_events":
                len(orbit_map) * 2 * FIXTURE_BANKS,
            "orbit_sizes": tuple(sorted(set(map(len, orbit_map.values())))),
            "canonical_representatives": tuple(orbit_map),
        })
    result = {
        "derivation": (
            "Ind_k(C_n)=n/k*binomial(n-k-1,k-1); direct enumeration; "
            "four Cycle-719 fixture events; canonical minimum rotation"
        ),
        "stratum_rows": tuple(stratum_rows),
        "configuration_counts": {
            row["k"]: row["direct_configurations"] for row in stratum_rows
        },
        "setup_counts": {
            row["k"]: row["starting_setups"] for row in stratum_rows
        },
        "orbit_counts": {
            row["k"]: row["C11_orbits_all_events"]
            for row in stratum_rows
        },
        "per_stratum_orbit_counts_printed": "16+28+20+4",
        "starting_setup_total": sum(
            row["starting_setups"] for row in stratum_rows
        ),
        "representative_total": len(representatives),
        "C11_action_free": every_orbit_free,
        "orbits_partition_each_stratum": complete_partition,
        "representatives_sha256": digest(tuple(representatives)),
    }
    result["pass"] = (
        result["configuration_counts"] == EXPECTED_CONFIGURATION_COUNTS
        and result["setup_counts"] == EXPECTED_SETUP_COUNTS
        and result["orbit_counts"] == EXPECTED_ORBIT_COUNTS
        and result["starting_setup_total"] == EXPECTED_TOTAL_SETUPS
        and result["representative_total"]
        == EXPECTED_TOTAL_REPRESENTATIVES
        and every_orbit_free
        and complete_partition
    )
    return tuple(representatives), result
