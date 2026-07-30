#!/usr/bin/env python3
"""Cycle 815: apply the Cycle-808 G' label symmetry to Cycle-786 origins.

The Cycle-786 and Cycle-808 pairs are SHA-pinned text/AST inputs and are
runtime-blocklisted.  Their finite allocation and label-action consequences
are reimplemented here.  The landed 46-event battery is rebuilt only from the
lower Cycle-719/750 machinery.

Boundary: exact finite counts and support only; no probability or split rule.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1200
STDOUT_LIMIT_BYTES = 200 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle786_ensemble_support_census_2026_07_28.py",
    "scripts/frontier_cycle786_support_independent_check_2026_07_28.py",
    "scripts/frontier_cycle808_uniformity_from_relabeling_2026_07_28.py",
    "scripts/frontier_cycle808_uniformity_independent_check_2026_07_28.py",
    "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "3956e5af3ea9c12e8bd605cc0bae7fc29a24154c1ee3527be53223dbee778cd6",
    AUDIT_INPUT_PATHS[1]:
        "7fdb18bba74a6163a7eae6d080f666a95dbe71f93d88ba9f44da6efc157af7b9",
    AUDIT_INPUT_PATHS[2]:
        "d3ccc94cf4d43da9fc8e737ca2706706cdffccb1e963bb8381d6db2350fefcea",
    AUDIT_INPUT_PATHS[3]:
        "8a717469dfb092ff0fc4e1b39be98c85ceea2ff8256bcaead73a93664867fdac",
    AUDIT_INPUT_PATHS[4]:
        "a74c7e5bbc297c57d317af7fd85d0b9e01d078625f5d4689daf2ebbdbc1cee0a",
    AUDIT_INPUT_PATHS[5]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
}
EXPECTED_GIT_BLOB_SHA1 = {
    AUDIT_INPUT_PATHS[0]: "3d219308183e781c71f9742bd0c6331440f74dbe",
    AUDIT_INPUT_PATHS[1]: "6d45253baab8040af57582b2fe64bbf49e7ab8e4",
    AUDIT_INPUT_PATHS[2]: "a79ef29be8f8c4b50ed7fc98cd4879b4e3d34524",
    AUDIT_INPUT_PATHS[3]: "3a5062ecaba514fda64440c1517c0dfefcfcb6e5",
    AUDIT_INPUT_PATHS[4]: "0a8f4562d28f12ed64130b3c3b23fccab677d333",
    AUDIT_INPUT_PATHS[5]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
}
SOURCE_COMMITS = {
    "cycle786_pair": "6a4d3a49f68808236403fe6310097459c2f7c07a",
    "cycle808_pair": "74eddf76c0759366eba0b4f245768a627aa41379",
}
BLOCKLISTED_MODULES = (
    "frontier_cycle786_ensemble_support_census_2026_07_28",
    "frontier_cycle786_support_independent_check_2026_07_28",
    "frontier_cycle808_uniformity_from_relabeling_2026_07_28",
    "frontier_cycle808_uniformity_independent_check_2026_07_28",
)

import ast
from collections import Counter, deque
from hashlib import sha1, sha256
import importlib.abc
import json
from math import comb
from pathlib import Path
import sys
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
START = monotonic()


class _CarriedPairBlocker(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path=None, target=None):
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            raise ImportError(f"BLOCKLIST forbids import of {fullname}")
        return None


PAIR_BLOCKER = _CarriedPairBlocker()
sys.meta_path.insert(0, PAIR_BLOCKER)
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle750_actual_selector_stretch_2026_07_28 as S750
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K719


ORIGINS = tuple(range(12))
POSITIVE_ORIGINS = tuple(range(6))
NEGATIVE_ORIGINS = tuple(range(6, 12))
ALLOCATION_BANKS = (2, 5, 12)
ALL_BANKS = (1, 2, 3, 5, 12)
GROUP_TOTAL = 19
GROUP_BINS = 6
G_ORDER = 58_599_022_482_000
G_PRIME_ORDER = 117_198_044_964_000
G_PRIME_GENERATORS = (
    "I1_SOURCE_1",
    "I1_SOURCE_LAST",
    "I2_ROTATE_1",
    "I2_ROTATE_LAST",
    "I3_Q_THEN_R_DESCENDING",
    "I3_Q_THEN_R_EVEN_THEN_ODD",
    "I3_R_THEN_Q_ASCENDING",
    "I3_R_THEN_Q_DESCENDING",
    "I3_R_THEN_Q_EVEN_THEN_ODD",
    "F_XOR_LIFT",
)


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def file_sha256(path: str) -> str:
    return sha256((ROOT / path).read_bytes()).hexdigest()


def git_blob_sha1(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("ascii")
    return sha1(header + data).hexdigest()


def top_level_assignments(tree: ast.Module) -> dict[str, ast.AST]:
    output: dict[str, ast.AST] = {}
    for node in tree.body:
        if isinstance(node, ast.Assign):
            targets = node.targets
            value = node.value
        elif isinstance(node, ast.AnnAssign):
            targets = (node.target,)
            value = node.value
        else:
            continue
        for target in targets:
            if isinstance(target, ast.Name):
                output[target.id] = value
    return output


def function_node(tree: ast.Module, name: str) -> ast.FunctionDef:
    matches = [
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    if len(matches) != 1:
        raise AssertionError(("function cardinality", name, len(matches)))
    return matches[0]


def source_controls() -> dict[str, object]:
    sources = {
        path: (ROOT / path).read_text(encoding="utf-8")
        for path in AUDIT_INPUT_PATHS
    }
    trees = {
        path: ast.parse(source, filename=path)
        for path, source in sources.items()
    }
    own_tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    own_assignments = top_level_assignments(own_tree)
    imported: list[str] = []
    dynamic: list[str] = []
    for node in ast.walk(own_tree):
        if isinstance(node, ast.Import):
            imported.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imported.append(node.module or "")
        elif (
            isinstance(node, ast.Call)
            and node.args
            and isinstance(node.args[0], ast.Constant)
            and isinstance(node.args[0].value, str)
            and (
                (isinstance(node.func, ast.Name) and node.func.id == "__import__")
                or (
                    isinstance(node.func, ast.Attribute)
                    and node.func.attr == "import_module"
                )
            )
        ):
            dynamic.append(node.args[0].value)

    runtime_attempts = {}
    for module in BLOCKLISTED_MODULES:
        try:
            __import__(module)
        except ImportError as exc:
            runtime_attempts[module] = (
                str(exc) == f"BLOCKLIST forbids import of {module}"
            )
        else:
            runtime_attempts[module] = False

    primary786 = sources[AUDIT_INPUT_PATHS[0]]
    checker786 = sources[AUDIT_INPUT_PATHS[1]]
    primary808 = sources[AUDIT_INPUT_PATHS[2]]
    checker808 = sources[AUDIT_INPUT_PATHS[3]]
    g_map = function_node(
        trees[AUDIT_INPUT_PATHS[2]], "map_occurrence_by_g"
    )
    flip_map = function_node(
        trees[AUDIT_INPUT_PATHS[2]], "map_occurrence_by_flip"
    )
    orbit_builder = function_node(
        trees[AUDIT_INPUT_PATHS[2]], "all_label_orbits"
    )
    moved_action_names = {
        node.id
        for function in (g_map, flip_map)
        for node in ast.walk(function)
        if isinstance(node, ast.Name)
    }
    orbit_literals = {
        node.value
        for node in ast.walk(orbit_builder)
        if isinstance(node, ast.Constant) and isinstance(node.value, str)
    }
    audit_node = own_assignments["AUDIT_INPUT_PATHS"]
    declared_node = own_assignments["DECLARED_INPUT_PATHS"]
    return {
        "literal_AUDIT_INPUT_PATHS": (
            isinstance(audit_node, ast.Tuple)
            and all(
                isinstance(item, ast.Constant) and isinstance(item.value, str)
                for item in audit_node.elts
            )
            and tuple(ast.literal_eval(audit_node)) == AUDIT_INPUT_PATHS
        ),
        "DECLARED_INPUT_PATHS_alias": (
            isinstance(declared_node, ast.Name)
            and declared_node.id == "AUDIT_INPUT_PATHS"
        ),
        "paths_worktree_relative": all(
            not Path(path).is_absolute() and ".." not in Path(path).parts
            for path in AUDIT_INPUT_PATHS
        ),
        "all_paths_exist": all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
        "all_sources_parse": all(isinstance(tree, ast.Module) for tree in trees.values()),
        "blocklisted_not_AST_imported": not any(
            name.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES
            for name in imported
        ),
        "blocklisted_not_literal_dynamic_imported": not any(
            name.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES
            for name in dynamic
        ),
        "blocklisted_not_loaded": all(
            name not in sys.modules for name in BLOCKLISTED_MODULES
        ),
        "runtime_blocker_installed": PAIR_BLOCKER in sys.meta_path,
        "runtime_attempts": runtime_attempts,
        "cycle786_allocation_anchors": all(
            token in checker786
            for token in (
                "range_audit = weak_composition_audit(19, 6)",
                'range_audit["weak_compositions_enumerated"] == 42_504',
                '"orientation_counts": {"+1": 19, "-1": 19}',
            )
        ),
        "cycle786_origin_partition_anchors": all(
            token in primary786
            for token in (
                "for origin in range(12)",
                '"orientation": 1 if origin < 6 else -1',
                '"origin": origin',
            )
        ),
        "cycle808_exact_group_anchors": all(
            token in primary808 + checker808
            for token in (
                "58_599_022_482_000",
                "117198044964000",
                "EXPECTED_STATIONS = {1: 3, 2: 11, 3: 19, 5: 35, 12: 91}",
            )
        ),
        "cycle808_action_has_no_origin_coordinate": (
            "origin" not in moved_action_names
            and "origin" not in orbit_literals
            and "return bank, epoch, direction, orientation, mapped_selected"
            in primary808
            and (
                "return bank, int(epoch) ^ 1, swapped, "
                "-int(orientation), selected"
            ) in primary808
        ),
        "cycle808_scope_excludes_global_state_action": (
            "not a global automorphism claim on all binary states"
            in primary808
            and "landed 46-event forward/inverse complete-step checkpoint"
            in primary808
        ),
    }


def weak_compositions(total: int, bins: int) -> tuple[tuple[int, ...], ...]:
    output: list[tuple[int, ...]] = []

    def visit(remaining: int, positions: int, prefix: tuple[int, ...]) -> None:
        if positions == 1:
            output.append(prefix + (remaining,))
            return
        for value in range(remaining + 1):
            visit(remaining - value, positions - 1, prefix + (value,))

    visit(total, bins, ())
    return tuple(output)


def lawful_group_allocation(values: tuple[int, ...]) -> bool:
    return (
        len(values) == GROUP_BINS
        and all(type(value) is int and value >= 0 for value in values)
        and sum(values) == GROUP_TOTAL
    )


def allocation_certificate() -> dict[str, object]:
    allocations = weak_compositions(GROUP_TOTAL, GROUP_BINS)
    possible_values = tuple(
        tuple(sorted({row[index] for row in allocations}))
        for index in range(GROUP_BINS)
    )
    return {
        "origins": ORIGINS,
        "orientation_groups": {
            "+1": POSITIVE_ORIGINS,
            "-1": NEGATIVE_ORIGINS,
        },
        "total_per_group": GROUP_TOTAL,
        "bins_per_group": GROUP_BINS,
        "lawfulness": "six nonnegative integer counts summing to 19",
        "allocations": allocations,
        "allocation_count": len(allocations),
        "closed_form_count": comb(GROUP_TOTAL + GROUP_BINS - 1, GROUP_BINS - 1),
        "possible_values_by_origin": possible_values,
        "all_lawful": all(lawful_group_allocation(row) for row in allocations),
        "allocation_sha256": digest(allocations),
    }
