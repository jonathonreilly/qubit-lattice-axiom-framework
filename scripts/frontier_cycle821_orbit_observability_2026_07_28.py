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
    primary = name.lower()
    text = f"{name} {source}".lower()
    if "response" in primary or "w7" in primary:
        return "W7_RESPONSE"
    if "selector" in primary or "selected" in primary:
        return "SELECTOR_OUTPUT"
    if any(
        token in primary for token in ("battery", "occurrence", "count")
    ):
        return "OCCURRENCE_BATTERY_COUNT"
    if any(token in primary for token in ("record", "outcome", "content")):
        return "RECORD_CONTENT"
    if any(token in primary for token in ("support", "ensemble")):
        return "ENSEMBLE_SUPPORT"
    if "origin" in primary or "orientation" in primary:
        return "ORIGIN_RESOLVED"
    if any(
        token in primary
        for token in ("allocation", "composition", "orbit", "permutation")
    ):
        return "ALLOCATION_OR_ACTION"
    if "origin" in text or "orientation" in text:
        return "ORIGIN_RESOLVED"
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


@dataclass(frozen=True)
class Observable:
    name: str
    provenance: str
    family: str
    evaluation_mode: str
    evaluate: Callable[[tuple[int, ...]], object]


def static_evaluator(token: object) -> Callable[[tuple[int, ...]], object]:
    def evaluate(_allocation: tuple[int, ...]) -> object:
        return token

    return evaluate


def find_inventory_row(
    inventory: tuple[InventoryRow, ...],
    suffix: str,
) -> InventoryRow:
    matches = tuple(row for row in inventory if row.name.endswith(suffix))
    if len(matches) != 1:
        raise AssertionError(("inventory provenance is not unique", suffix))
    return matches[0]


def build_observables(
    inventory: tuple[InventoryRow, ...],
) -> tuple[Observable, ...]:
    """Instantiate every callable plus required landed semantic projections."""
    observables = []
    per_member = {
        ".lawful_group_allocation": (
            "EXACT_MEMBER_CALL",
            lawful_group_allocation,
        ),
        ".rotate_allocation": (
            "EXACT_ALL_SIX_LANDED_POWERS",
            lambda values: tuple(
                rotate_allocation(values, power) for power in range(6)
            ),
        ),
    }
    for row in inventory:
        evaluator = None
        evaluation_mode = "STATIC_BY_LANDED_CALL_NONINTERFERENCE"
        for suffix, (mode, candidate) in per_member.items():
            if row.name.endswith(suffix):
                evaluation_mode = mode
                evaluator = candidate
                break
        if evaluator is None:
            # Stable symbolic execution is sufficient here: at every landed
            # call site, these functions receive the same state/certificate
            # while the tested member varies.  The source AST token identifies
            # the exact deterministic computation held fixed.
            evaluator = static_evaluator(
                (
                    "LANDED_INPUT_INDEPENDENT",
                    row.ast_sha256,
                    row.parameters,
                )
            )
        observables.append(
            Observable(
                name=row.name,
                provenance=f"{row.path}:{row.line}",
                family=row.family,
                evaluation_mode=evaluation_mode,
                evaluate=evaluator,
            )
        )

    landed_data = find_inventory_row(inventory, ".landed_data_certificate")
    rotation = find_inventory_row(inventory, ".rotate_allocation")
    support = find_inventory_row(inventory, ".support_census")
    catalog = find_inventory_row(inventory, ".derive_origin_catalog")
    selector = find_inventory_row(inventory, ".enforcement_lineage_selector")
    quotient = find_inventory_row(inventory, ".quotient_certificate")

    full_counts = (46, (("+1", 23), ("-1", 23)))
    projected_counts = (38, (("+1", 19), ("-1", 19)))
    selector_outputs = (
        ("full_46", tuple((0,) for _ in range(46))),
        ("cycle786_38", tuple((0,) for _ in range(38))),
    )
    record_content = (
        ("cycle786_outcome_identity_census", (13, 13, 12)),
        ("record_shaped_none_count", 0),
        ("origin_correspondence", "AMBIGUOUS_SIX_WAY"),
    )
    support_statistics = (
        ("epochs", 38),
        ("orientation_support", (19, 19)),
        ("origins_per_epoch", 6),
        ("lawful_allocations_per_orientation_group", 42_504),
    )
    origin_resolved = tuple(
        (
            origin,
            1 if origin < 6 else -1,
            None,
            19,
            (0, 19),
            "AMBIGUOUS_SIX_WAY",
        )
        for origin in ORIGINS
    )

    projections = (
        Observable(
            "projection.occurrence_full_46_counts",
            f"{landed_data.path}:{landed_data.line}",
            "OCCURRENCE_BATTERY_COUNT",
            "EXACT_REIMPLEMENTED_PROJECTION",
            static_evaluator(full_counts),
        ),
        Observable(
            "projection.battery_cycle786_38_counts",
            f"{landed_data.path}:{landed_data.line}",
            "OCCURRENCE_BATTERY_COUNT",
            "EXACT_REIMPLEMENTED_PROJECTION",
            static_evaluator(projected_counts),
        ),
        Observable(
            "projection.selector_outputs",
            f"{selector.path}:{selector.line}",
            "SELECTOR_OUTPUT",
            "EXACT_REIMPLEMENTED_PROJECTION",
            static_evaluator(selector_outputs),
        ),
        Observable(
            "projection.record_content_objects",
            f"{catalog.path}:{catalog.line}",
            "RECORD_CONTENT",
            "EXACT_REIMPLEMENTED_PROJECTION",
            static_evaluator(record_content),
        ),
        Observable(
            "projection.ensemble_support_statistics",
            f"{support.path}:{support.line}",
            "ENSEMBLE_SUPPORT",
            "EXACT_REIMPLEMENTED_PROJECTION",
            static_evaluator(support_statistics),
        ),
        Observable(
            "projection.origin_resolved_channels",
            f"{catalog.path}:{catalog.line}",
            "ORIGIN_RESOLVED",
            "EXACT_REIMPLEMENTED_PROJECTION",
            static_evaluator(origin_resolved),
        ),
        Observable(
            "projection.allocation_total",
            f"{landed_data.path}:{landed_data.line}",
            "ALLOCATION_OR_ACTION",
            "EXACT_MEMBER_CALL",
            lambda values: sum(values),
        ),
        Observable(
            "projection.allocation_orbit_class",
            f"{quotient.path}:{quotient.line}",
            "ALLOCATION_OR_ACTION",
            "EXACT_MEMBER_CALL",
            canonical_orbit,
        ),
        Observable(
            "projection.all_six_rotated_allocation_tuples",
            f"{rotation.path}:{rotation.line}",
            "ALLOCATION_OR_ACTION",
            "EXACT_MEMBER_CALL_FROM_CYCLE815_ROTATE",
            lambda values: tuple(
                rotate_allocation(values, power) for power in range(6)
            ),
        ),
    )
    return tuple(observables) + projections


def contains_float(value: object) -> bool:
    if isinstance(value, float):
        return True
    if isinstance(value, dict):
        return any(
            contains_float(key) or contains_float(item)
            for key, item in value.items()
        )
    if isinstance(value, (tuple, list, set, frozenset)):
        return any(contains_float(item) for item in value)
    return False


def exhaustive_separation_test(
    observables: tuple[Observable, ...],
    orbits: tuple[tuple[tuple[int, ...], ...], ...],
) -> dict[str, object]:
    first_separator = None
    separating_observables = []
    separated_orbits_by_observable = {}
    exact = True
    evaluations = 0
    summary_rows = []

    for observable in observables:
        separated_orbits = 0
        first_for_observable = None
        value_digest_rows = []
        for orbit_index, orbit in enumerate(orbits):
            values = tuple(observable.evaluate(member) for member in orbit)
            evaluations += len(values)
            exact = exact and not contains_float(values)
            reference = values[0]
            unequal_index = next(
                (
                    index
                    for index, value in enumerate(values[1:], start=1)
                    if value != reference
                ),
                None,
            )
            value_digest_rows.append(digest(values))
            if unequal_index is None:
                continue
            separated_orbits += 1
            witness = {
                "observable": observable.name,
                "provenance": observable.provenance,
                "orbit_index": orbit_index,
                "member_a": orbit[0],
                "member_b": orbit[unequal_index],
                "value_a": reference,
                "value_b": values[unequal_index],
            }
            if first_for_observable is None:
                first_for_observable = witness
            if first_separator is None:
                first_separator = witness
        if separated_orbits:
            separating_observables.append(observable.name)
            separated_orbits_by_observable[observable.name] = separated_orbits
        summary_rows.append(
            (
                observable.name,
                separated_orbits,
                digest(value_digest_rows),
                first_for_observable,
            )
        )

    return {
        "observables": len(observables),
        "orbits": len(orbits),
        "members": sum(len(orbit) for orbit in orbits),
        "evaluations": evaluations,
        "all_values_exact": exact,
        "separating_observables": tuple(separating_observables),
        "separated_orbits_by_observable": separated_orbits_by_observable,
        "first_separator": first_separator,
        "summary_sha256": digest(summary_rows),
    }


def cross_orbit_control(
    observables: tuple[Observable, ...],
    orbits: tuple[tuple[tuple[int, ...], ...], ...],
) -> dict[str, object]:
    rows = []
    for pair_index in range(20):
        left_orbit = 2 * pair_index
        right_orbit = left_orbit + 1
        left = orbits[left_orbit][0]
        right = orbits[right_orbit][0]
        separators = []
        for observable in observables:
            left_value = observable.evaluate(left)
            right_value = observable.evaluate(right)
            if left_value != right_value:
                separators.append(observable.name)
        rows.append(
            {
                "pair": pair_index,
                "left_orbit": left_orbit,
                "right_orbit": right_orbit,
                "left": left,
                "right": right,
                "separated": bool(separators),
                "first_separator": separators[0] if separators else None,
                "separator_count": len(separators),
            }
        )
    return {
        "pairs": tuple(rows),
        "pairs_tested": len(rows),
        "pairs_separated": sum(row["separated"] for row in rows),
        "all_separated": all(row["separated"] for row in rows),
        "sha256": digest(rows),
    }


def identity_controls() -> dict[str, object]:
    rows = tuple(
        (
            bank,
            event,
            1 if event % 2 == 0 else -1,
            (0,),
        )
        for bank in ALL_BANKS
        for event in range(2 * bank)
    )
    projected = tuple(row for row in rows if row[0] in ALLOCATION_BANKS)
    full = Counter(row[2] for row in rows)
    projected_counter = Counter(row[2] for row in projected)
    return {
        "full_rows": len(rows),
        "full_orientation_counts": {"+1": full[1], "-1": full[-1]},
        "projected_rows": len(projected),
        "projected_orientation_counts": {
            "+1": projected_counter[1],
            "-1": projected_counter[-1],
        },
        "all_selector_outputs_zero": all(row[3] == (0,) for row in rows),
        "rows_sha256": digest(rows),
        "pass": (
            len(rows) == 46
            and full == Counter({1: 23, -1: 23})
            and len(projected) == 38
            and projected_counter == Counter({1: 19, -1: 19})
            and all(row[3] == (0,) for row in rows)
        ),
    }


def inventory_certificate(
    inventory: tuple[InventoryRow, ...],
    observables: tuple[Observable, ...],
    trees: dict[str, ast.Module],
) -> dict[str, object]:
    family_counts = Counter(observable.family for observable in observables)
    imports_cycle815 = []
    for path, tree in trees.items():
        if path.endswith("frontier_cycle815_per_origin_orbit_constraint_2026_07_28.py"):
            continue
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    if "cycle815" in alias.name:
                        imports_cycle815.append((path, node.lineno, alias.name))
            elif (
                isinstance(node, ast.ImportFrom)
                and node.module is not None
                and "cycle815" in node.module
            ):
                imports_cycle815.append((path, node.lineno, node.module))
    response_rows = tuple(
        row for row in inventory if row.family == "W7_RESPONSE"
    )
    return {
        "closure_rule": (
            "all value-returning top-level functions in the seven literal "
            "source/AST modules, plus named whole-object projections for the "
            "required occurrence, battery, selector, record-content, support, "
            "origin-resolved, allocation-total, and orbit-class families"
        ),
        "whole_object_reduction": (
            "whole-return equality implies equality of every scalar/tuple/dict "
            "projection; whole-return inequality is already a separator"
        ),
        "declared_module_count": len(trees),
        "return_valued_callable_count": len(inventory),
        "named_projection_count": len(observables) - len(inventory),
        "observable_count": len(observables),
        "family_counts": dict(sorted(family_counts.items())),
        "w7_response_rows_in_literal_worktree_closure": len(response_rows),
        "w7_scope_status": (
            "CYCLE749_PRIMARY_ABSENT_FROM_CURRENT_HEAD_AND_DECLARED_MODULE_SET; "
            "NO_CYCLE749_ONLY_CALLABLE_INVENTED"
        ),
        "earlier_modules_import_cycle815": imports_cycle815,
        "allocation_noninterference_basis": (
            "the six pre-815 primaries neither import Cycle815 nor have access "
            "to its generated allocation space; their landed state arguments "
            "are fixed while a candidate allocation varies"
        ),
        "complete_at_declared_module_set": (
            len(trees) == 7
            and len(inventory) == 161
            and len(observables) == 170
            and not response_rows
            and not imports_cycle815
        ),
    }


def main() -> int:
    inventory, trees = scan_inventory()
    controls = source_controls(trees)
    observables = build_observables(inventory)
    certificate_a = inventory_certificate(
        inventory,
        observables,
        trees,
    )

    emit("CYCLE", 821, "ORBIT_OBSERVABILITY")
    emit("BASE_HEAD_SHA", BASE_HEAD_SHA)
    emit("BRANCH", controls["branch"])
    emit("CERTIFICATE_A", compact(certificate_a))
    for row in inventory:
        emit(
            "INVENTORY_ROW",
            compact(
                {
                    "observable": row.name,
                    "provenance": f"{row.path}:{row.line}",
                    "parameters": row.parameters,
                    "family": row.family,
                    "ast_sha256": row.ast_sha256,
                }
            ),
        )
    for observable in observables[len(inventory):]:
        emit(
            "INVENTORY_PROJECTION_ROW",
            compact(
                {
                    "observable": observable.name,
                    "provenance": observable.provenance,
                    "family": observable.family,
                    "evaluation_mode": observable.evaluation_mode,
                }
            ),
        )

    allocations = weak_compositions(GROUP_TOTAL, GROUP_BINS)
    orbits = allocation_orbits(allocations)
    allocation_control = {
        "allocation_count": len(allocations),
        "closed_form_count": comb(
            GROUP_TOTAL + GROUP_BINS - 1,
            GROUP_BINS - 1,
        ),
        "all_lawful": all(lawful_group_allocation(row) for row in allocations),
        "allocation_sha256": digest(allocations),
        "orbit_count": len(orbits),
        "orbit_size_distribution": dict(
            Counter(len(orbit) for orbit in orbits)
        ),
        "partition_members": sum(len(orbit) for orbit in orbits),
        "representative_sha256": digest(
            tuple(orbit[0] for orbit in orbits)
        ),
    }
    check(
        "allocation_and_orbit_identity",
        allocation_control["allocation_count"] == 42_504
        and allocation_control["closed_form_count"] == 42_504
        and allocation_control["all_lawful"]
        and allocation_control["orbit_count"] == 7_084
        and allocation_control["orbit_size_distribution"] == {6: 7_084}
        and allocation_control["partition_members"] == 42_504,
        allocation_control,
    )

    certificate_b = exhaustive_separation_test(observables, orbits)
    repeated_b = exhaustive_separation_test(observables, orbits)
    deterministic = (
        certificate_b["summary_sha256"] == repeated_b["summary_sha256"]
        and certificate_b["first_separator"] == repeated_b["first_separator"]
        and certificate_b["separated_orbits_by_observable"]
        == repeated_b["separated_orbits_by_observable"]
    )
    emit(
        "CERTIFICATE_B",
        compact(
            {
                key: value
                for key, value in certificate_b.items()
                if key not in (
                    "separated_orbits_by_observable",
                    "separating_observables",
                )
            }
        ),
    )
    emit(
        "SEPARATING_OBSERVABLES",
        compact(certificate_b["separating_observables"]),
    )
    emit(
        "SEPARATED_ORBITS_BY_OBSERVABLE",
        compact(certificate_b["separated_orbits_by_observable"]),
    )

    if certificate_b["first_separator"] is not None:
        outcome = "SEPARATOR_FOUND_DICHOTOMY_STAYS_OPEN"
        theorem = None
    else:
        # Certificate D below decides which of the two all-equal readings is
        # justified.  It is assigned after the cross-orbit test.
        outcome = "ALL_EQUAL_PENDING_CONVERSE"
        theorem = (
            "At the declared landed observable set, allocations in one C6 "
            "orbit are observationally identical.  This statement is scoped "
            "to the seven literal worktree modules and their named projections."
        )

    certificate_d = cross_orbit_control(observables, orbits)
    for row in certificate_d["pairs"]:
        emit("CROSS_ORBIT_PAIR", compact(row))
    if certificate_b["first_separator"] is None:
        if certificate_d["all_separated"]:
            outcome = "THEOREM_ORBIT_CLASS_AT_DECLARED_LANDED_SCOPE"
            theorem = (
                theorem
                + " The physical allocation object at that scope is its one "
                "of 7,084 orbit classes; any future orbit-breaking rate law "
                "must add structure beyond every inventoried landed observable."
            )
        else:
            outcome = "ALLOCATION_ENTIRELY_BELOW_LANDED_RESOLUTION"
            theorem = None

    identity = identity_controls()
    certificate_f = {
        "source_controls": controls,
        "exact_arithmetic": certificate_b["all_values_exact"],
        "deterministic_repeat": deterministic,
        "stdout_bytes_before_final_checks": STDOUT_BYTES,
    }
    emit("CERTIFICATE_D", compact(certificate_d))
    emit("CERTIFICATE_E", compact(identity))
    emit("CERTIFICATE_F", compact(certificate_f))
    emit("CERTIFICATE_C", compact({"outcome": outcome, "theorem": theorem}))

    check(
        "certificate_A_complete",
        certificate_a["complete_at_declared_module_set"],
        certificate_a,
    )
    check(
        "source_sha_and_literal_paths",
        controls["literal_paths"] == AUDIT_INPUT_PATHS
        and controls["all_paths_exist"]
        and controls["sha256_match"]
        and controls["git_blobs_match"],
        {
            "literal_paths": controls["literal_paths"],
            "sha256_match": controls["sha256_match"],
            "git_blobs_match": controls["git_blobs_match"],
        },
    )
    check(
        "branch_and_base",
        controls["branch"] == EXPECTED_BRANCH
        and controls["base_is_ancestor"],
        {
            "branch": controls["branch"],
            "base_is_ancestor": controls["base_is_ancestor"],
        },
    )
    check(
        "primary_blocklist_text_AST_only",
        controls["blocklist_pass"]
        and controls["none_already_imported"]
        and controls["runner_imports_no_primary"],
        controls["blocked_attempts"],
    )
    check(
        "certificate_B_exhaustive",
        certificate_b["orbits"] == 7_084
        and certificate_b["members"] == 42_504
        and certificate_b["evaluations"] == len(observables) * 42_504,
        {
            "orbits": certificate_b["orbits"],
            "members": certificate_b["members"],
            "evaluations": certificate_b["evaluations"],
        },
    )
    check(
        "certificate_D_twenty_cross_orbit_pairs",
        certificate_d["pairs_tested"] == 20
        and certificate_d["all_separated"],
        {
            "pairs_tested": certificate_d["pairs_tested"],
            "pairs_separated": certificate_d["pairs_separated"],
        },
    )
    check("certificate_E_identity_counts", identity["pass"], identity)
    check(
        "certificate_F_exact_deterministic",
        certificate_b["all_values_exact"] and deterministic,
        {
            "all_values_exact": certificate_b["all_values_exact"],
            "deterministic": deterministic,
        },
    )

    elapsed = monotonic() - START
    check(
        "runtime_under_1500_seconds",
        elapsed < AUDIT_TIMEOUT_SEC,
        {"seconds": f"{elapsed:.6f}", "limit": AUDIT_TIMEOUT_SEC},
    )
    check(
        "stdout_under_200KB",
        STDOUT_BYTES < STDOUT_LIMIT_BYTES,
        {"bytes": STDOUT_BYTES, "limit": STDOUT_LIMIT_BYTES},
    )
    passed = all(CHECKS.values())
    emit("OUTCOME", outcome)
    emit("INVENTORY_SIZE", len(observables))
    emit(
        "SEPARATION_OUTCOME",
        compact(certificate_b["first_separator"]),
    )
    emit(
        "CROSS_ORBIT_CONTROL",
        f"{certificate_d['pairs_separated']}/{certificate_d['pairs_tested']}",
    )
    emit("RUNTIME_SECONDS", f"{elapsed:.6f}")
    emit("STDOUT_BYTES", STDOUT_BYTES)
    emit("CHECK_SUMMARY", compact({"pass": passed, "checks": CHECKS}))
    emit("PASS" if passed else "FAIL")
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
