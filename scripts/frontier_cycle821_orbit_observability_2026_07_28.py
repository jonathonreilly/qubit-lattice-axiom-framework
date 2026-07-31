#!/usr/bin/env python3
"""Cycle 821: exhaustive orbit-observability test at landed worktree scope.

The inventory rule is deliberately conservative.  The declared module set is
the seven worktree-resident primaries carrying the Cycle-750/758/786/788 and
Cycle-805/808/815 lineage at the Cycle-821 base SHA.  Every top-level function
in those files having a value-bearing ``return`` is inventoried.  This is a
superset closure: audit helpers and group-action helpers remain visible, so a
physical-looking theorem cannot be obtained by silently classifying a
separating tuple functional as "mere machinery".

For a callable whose landed calls have no per-allocation channel, allocation
independence is certified syntactically and represented by a stable AST token.
The Cycle-815 callables that consume one allocation are reimplemented and
evaluated exactly.  Whole returned objects are compared; equality of a whole
object is a proven-sufficient reduction for every numeric/tuple/dict projection
of that object.  Conversely, inequality of any whole object is a separator.

The Cycle-749 W7 response primary is not present in the declared worktree
module set.  That absence is an explicit scope result, not silently repaired
from another branch or Git object.  Consequently no Cycle-749-only callable is
called "landed" here; the Cycle-750/758 downstream selector lineage is scanned.

The Cycle-786/805/808/815 primaries are source/AST inputs only.  Imports are
runtime-blocked and their finite allocation/action/count consequences are
reimplemented below with integers and tuples.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
STDOUT_LIMIT_BYTES = 200 * 1024
BASE_HEAD_SHA = "42f8eeec2414cbca9e6a8a3f8b67caa097383bb7"
EXPECTED_BRANCH = "physics-loop/proof-grade-blockP13-20260729"

AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
    "scripts/frontier_cycle758_selector_multisource_2026_07_28.py",
    "scripts/frontier_cycle786_ensemble_support_census_2026_07_28.py",
    "scripts/frontier_cycle788_selector_scope_extension_2026_07_28.py",
    "scripts/frontier_cycle805_supply_relabeling_tournament_2026_07_28.py",
    "scripts/frontier_cycle808_uniformity_from_relabeling_2026_07_28.py",
    "scripts/frontier_cycle815_per_origin_orbit_constraint_2026_07_28.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "a74c7e5bbc297c57d317af7fd85d0b9e01d078625f5d4689daf2ebbdbc1cee0a",
    AUDIT_INPUT_PATHS[1]:
        "8be433f74cb337c322bcb1e2f46007244d708a41c946cb83b7ccd61004176241",
    AUDIT_INPUT_PATHS[2]:
        "3956e5af3ea9c12e8bd605cc0bae7fc29a24154c1ee3527be53223dbee778cd6",
    AUDIT_INPUT_PATHS[3]:
        "5af27fd61c20fe3b25e9a172b63339d5fd4f5112631fe6d31c6e0fa95a7486f1",
    AUDIT_INPUT_PATHS[4]:
        "04432816e3844043b419de8d91001003cd7fb8de76635658c3367574c3e44b9a",
    AUDIT_INPUT_PATHS[5]:
        "d3ccc94cf4d43da9fc8e737ca2706706cdffccb1e963bb8381d6db2350fefcea",
    AUDIT_INPUT_PATHS[6]:
        "e064b2f431f3e125b8c7f8176e6331f3fee41c2d1dc8ba7e3e65ae97a4ebb6b0",
}
EXPECTED_GIT_BLOB_SHA1 = {
    AUDIT_INPUT_PATHS[0]: "0a8f4562d28f12ed64130b3c3b23fccab677d333",
    AUDIT_INPUT_PATHS[1]: "4e23e03ecc5f92a0b8348bfa526eb5b2f2b09dd0",
    AUDIT_INPUT_PATHS[2]: "3d219308183e781c71f9742bd0c6331440f74dbe",
    AUDIT_INPUT_PATHS[3]: "1e691cb4b2477f86e1c81e017de44b53c4edec88",
    AUDIT_INPUT_PATHS[4]: "075659d59588f7895e91f50f9ef93a368fb1fb4e",
    AUDIT_INPUT_PATHS[5]: "a79ef29be8f8c4b50ed7fc98cd4879b4e3d34524",
    AUDIT_INPUT_PATHS[6]: "3fbfaf0019af05bbb3121de47de49b9cefec7571",
}

BLOCKLISTED_MODULES = (
    "frontier_cycle786_ensemble_support_census_2026_07_28",
    "frontier_cycle805_supply_relabeling_tournament_2026_07_28",
    "frontier_cycle808_uniformity_from_relabeling_2026_07_28",
    "frontier_cycle815_per_origin_orbit_constraint_2026_07_28",
)

ALL_BANKS = (1, 2, 3, 5, 12)
ALLOCATION_BANKS = (2, 5, 12)
ORIGINS = tuple(range(12))
GROUP_TOTAL = 19
GROUP_BINS = 6

import ast
from collections import Counter
from dataclasses import dataclass
from hashlib import sha1, sha256
import importlib.abc
import importlib.util
import json
from math import comb
from pathlib import Path
import subprocess
import sys
from time import monotonic
from typing import Callable


ROOT = Path(__file__).resolve().parents[1]
START = monotonic()
CHECKS: dict[str, bool] = {}
STDOUT_BYTES = 0


class _PrimaryBlocker(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path=None, target=None):
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            raise ImportError(f"BLOCKLIST forbids import of {fullname}")
        return None


PRIMARY_BLOCKER = _PrimaryBlocker()
sys.meta_path.insert(0, PRIMARY_BLOCKER)


def compact(value: object) -> str:
    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        default=str,
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def emit(*parts: object) -> None:
    global STDOUT_BYTES
    line = " ".join(str(part) for part in parts)
    encoded = (line + "\n").encode("utf-8")
    STDOUT_BYTES += len(encoded)
    if STDOUT_BYTES > STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout limit exceeded", STDOUT_BYTES))
    print(line)


def check(label: str, condition: bool, detail: object = "") -> bool:
    CHECKS[label] = bool(condition)
    emit("CHECK", label, "PASS" if condition else "FAIL", compact(detail))
    return bool(condition)


def git_blob_sha1(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("ascii")
    return sha1(header + data).hexdigest()


class _ReturnVisitor(ast.NodeVisitor):
    """Collect returns in one function without descending into nested scopes."""

    def __init__(self) -> None:
        self.values: list[ast.AST] = []

    def visit_Return(self, node: ast.Return) -> None:  # noqa: N802
        if node.value is not None and not (
            isinstance(node.value, ast.Constant) and node.value.value is None
        ):
            self.values.append(node.value)

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:  # noqa: N802
        return

    def visit_AsyncFunctionDef(  # noqa: N802
        self,
        node: ast.AsyncFunctionDef,
    ) -> None:
        return

    def visit_Lambda(self, node: ast.Lambda) -> None:  # noqa: N802
        return


def direct_return_values(function: ast.FunctionDef) -> tuple[ast.AST, ...]:
    visitor = _ReturnVisitor()
    for statement in function.body:
        visitor.visit(statement)
    return tuple(visitor.values)


def call_name(node: ast.Call) -> str:
    target = node.func
    if isinstance(target, ast.Name):
        return target.id
    if isinstance(target, ast.Attribute):
        parts = [target.attr]
        owner = target.value
        while isinstance(owner, ast.Attribute):
            parts.append(owner.attr)
            owner = owner.value
        if isinstance(owner, ast.Name):
            parts.append(owner.id)
        return ".".join(reversed(parts))
    return type(target).__name__


def semantic_family(name: str, source: str) -> str:
    text = f"{name} {source}".lower()
    if "response" in text or "w7" in text:
        return "W7_RESPONSE"
    if "selector" in text or "selected" in text:
        return "SELECTOR_OUTPUT"
    if any(token in text for token in ("battery", "occurrence", "count")):
        return "OCCURRENCE_BATTERY_COUNT"
    if any(token in text for token in ("record", "outcome", "content")):
        return "RECORD_CONTENT"
    if any(token in text for token in ("support", "ensemble")):
        return "ENSEMBLE_SUPPORT"
    if "origin" in text or "orientation" in text:
        return "ORIGIN_RESOLVED"
    if any(
        token in text
        for token in ("allocation", "composition", "orbit", "permutation")
    ):
        return "ALLOCATION_OR_ACTION"
    return "OTHER_RETURN_VALUE"


@dataclass(frozen=True)
class InventoryRow:
    name: str
    path: str
    line: int
    parameters: tuple[str, ...]
    family: str
    ast_sha256: str
    calls: tuple[str, ...]


def scan_inventory() -> tuple[tuple[InventoryRow, ...], dict[str, ast.Module]]:
    rows = []
    trees = {}
    for relative in AUDIT_INPUT_PATHS:
        source = (ROOT / relative).read_bytes()
        tree = ast.parse(source, filename=relative)
        trees[relative] = tree
        for node in tree.body:
            if not isinstance(node, ast.FunctionDef):
                continue
            returns = direct_return_values(node)
            if not returns:
                continue
            parameters = tuple(
                argument.arg
                for argument in (
                    tuple(node.args.posonlyargs)
                    + tuple(node.args.args)
                    + tuple(node.args.kwonlyargs)
                )
            )
            calls = tuple(
                sorted(
                    {
                        call_name(child)
                        for child in ast.walk(node)
                        if isinstance(child, ast.Call)
                    }
                )
            )
            rows.append(
                InventoryRow(
                    name=f"{Path(relative).stem}.{node.name}",
                    path=relative,
                    line=node.lineno,
                    parameters=parameters,
                    family=semantic_family(node.name, ast.unparse(node)),
                    ast_sha256=sha256(
                        ast.dump(
                            node,
                            annotate_fields=True,
                            include_attributes=False,
                        ).encode("utf-8")
                    ).hexdigest(),
                    calls=calls,
                )
            )
    return tuple(rows), trees


def literal_audit_tuple() -> tuple[str, ...]:
    tree = ast.parse(Path(__file__).read_bytes(), filename=__file__)
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        if any(
            isinstance(target, ast.Name)
            and target.id == "AUDIT_INPUT_PATHS"
            for target in node.targets
        ):
            value = ast.literal_eval(node.value)
            if not isinstance(value, tuple):
                raise AssertionError("AUDIT_INPUT_PATHS is not a literal tuple")
            return value
    raise AssertionError("missing literal AUDIT_INPUT_PATHS")


def source_controls(
    trees: dict[str, ast.Module],
) -> dict[str, object]:
    observed_sha256 = {}
    observed_blobs = {}
    for relative in AUDIT_INPUT_PATHS:
        data = (ROOT / relative).read_bytes()
        observed_sha256[relative] = sha256(data).hexdigest()
        observed_blobs[relative] = git_blob_sha1(data)

    blocked_attempts = {}
    for module in BLOCKLISTED_MODULES:
        try:
            importlib.util.find_spec(module)
        except ImportError as error:
            blocked_attempts[module] = str(error)
        else:
            blocked_attempts[module] = "NOT_BLOCKED"

    imports_in_runner = {
        alias.name
        for node in ast.parse(Path(__file__).read_bytes()).body
        if isinstance(node, ast.Import)
        for alias in node.names
    }
    from_imports_in_runner = {
        str(node.module)
        for node in ast.parse(Path(__file__).read_bytes()).body
        if isinstance(node, ast.ImportFrom)
    }
    imported_roots = imports_in_runner | from_imports_in_runner

    branch = subprocess.run(
        ("git", "branch", "--show-current"),
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    base_is_ancestor = subprocess.run(
        ("git", "merge-base", "--is-ancestor", BASE_HEAD_SHA, "HEAD"),
        cwd=ROOT,
        check=False,
        capture_output=True,
    ).returncode == 0

    literal_paths = literal_audit_tuple()
    controls = {
        "literal_paths": literal_paths,
        "all_paths_exist": all((ROOT / path).is_file() for path in literal_paths),
        "sha256": observed_sha256,
        "git_blob_sha1": observed_blobs,
        "sha256_match": observed_sha256 == EXPECTED_SHA256,
        "git_blobs_match": observed_blobs == EXPECTED_GIT_BLOB_SHA1,
        "blocked_attempts": blocked_attempts,
        "blocklist_pass": all(
            value.startswith("BLOCKLIST forbids import")
            for value in blocked_attempts.values()
        ),
        "none_already_imported": all(
            module not in sys.modules for module in BLOCKLISTED_MODULES
        ),
        "runner_imports_no_primary": all(
            module not in imported_roots for module in BLOCKLISTED_MODULES
        ),
        "parsed_module_count": len(trees),
        "branch": branch,
        "base_is_ancestor": base_is_ancestor,
    }
    return controls


def weak_compositions(total: int, bins: int) -> tuple[tuple[int, ...], ...]:
    rows: list[tuple[int, ...]] = []

    def visit(
        remaining: int,
        positions: int,
        prefix: tuple[int, ...],
    ) -> None:
        if positions == 1:
            rows.append(prefix + (remaining,))
            return
        for value in range(remaining + 1):
            visit(remaining - value, positions - 1, prefix + (value,))

    visit(total, bins, ())
    return tuple(rows)


def lawful_group_allocation(values: tuple[int, ...]) -> bool:
    return (
        len(values) == GROUP_BINS
        and all(type(value) is int and value >= 0 for value in values)
        and sum(values) == GROUP_TOTAL
    )


def rotate_allocation(
    values: tuple[int, ...],
    shift: int,
) -> tuple[int, ...]:
    output = [0] * len(values)
    for source, value in enumerate(values):
        output[(source + shift) % len(values)] = value
    return tuple(output)


def allocation_orbits(
    allocations: tuple[tuple[int, ...], ...],
) -> tuple[tuple[tuple[int, ...], ...], ...]:
    remaining = set(allocations)
    orbits = []
    while remaining:
        seed = min(remaining)
        orbit = tuple(
            sorted({rotate_allocation(seed, power) for power in range(6)})
        )
        orbits.append(orbit)
        remaining.difference_update(orbit)
    return tuple(orbits)


def canonical_orbit(values: tuple[int, ...]) -> tuple[int, ...]:
    return min(rotate_allocation(values, power) for power in range(6))

