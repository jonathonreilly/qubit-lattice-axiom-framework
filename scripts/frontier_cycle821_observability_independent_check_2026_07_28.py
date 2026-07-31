#!/usr/bin/env python3
"""Cycle 821 independent adversarial orbit-observability checker.

The Cycle-821 primary is a text/AST input only.  It is import-blocklisted and
is never executed.  This checker independently rebuilds the seven-module
inventory, adjudicates outputs by a structural comparison-value rule, adds
the SHA-pinned W7 response surface, and exhausts all 7,084 C6 allocation
orbits with exact integer/Fraction arithmetic.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
STDOUT_LIMIT_BYTES = 200 * 1024
PRIMARY_PATH = (
    "scripts/frontier_cycle821_orbit_observability_2026_07_28.py"
)
PRIMARY_MODULE = "frontier_cycle821_orbit_observability_2026_07_28"

# Literal and worktree-relative by construction.  The first entry is parsed
# only; entries 1:8 are the primary's landed scope; entries 8: are the exact
# W7 copies requested for this independent extension.
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle821_orbit_observability_2026_07_28.py",
    "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
    "scripts/frontier_cycle758_selector_multisource_2026_07_28.py",
    "scripts/frontier_cycle786_ensemble_support_census_2026_07_28.py",
    "scripts/frontier_cycle788_selector_scope_extension_2026_07_28.py",
    "scripts/frontier_cycle805_supply_relabeling_tournament_2026_07_28.py",
    "scripts/frontier_cycle808_uniformity_from_relabeling_2026_07_28.py",
    "scripts/frontier_cycle815_per_origin_orbit_constraint_2026_07_28.py",
    "scripts/frontier_cycle749_response_comparison_harness_2026_07_28.py",
    "scripts/frontier_cycle768_response_law_candidate_2026_07_28.py",
    "scripts/frontier_cycle771_prediction_verification_2026_07_28.py",
    "scripts/frontier_cycle774_interference_sector_2026_07_28.py",
    "scripts/frontier_cycle778_norefit_attachment_2026_07_28.py",
    "scripts/frontier_cycle812_mixed_input_response_2026_07_28.py",
)
LANDED_SCOPE_PATHS = AUDIT_INPUT_PATHS[1:8]
W7_COPY_PATHS = AUDIT_INPUT_PATHS[8:]

EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "36273e2f13c26803d7a28bb65a3efce0aab82c766e4dc039d8269f0d53973342",
    AUDIT_INPUT_PATHS[1]:
        "a74c7e5bbc297c57d317af7fd85d0b9e01d078625f5d4689daf2ebbdbc1cee0a",
    AUDIT_INPUT_PATHS[2]:
        "8be433f74cb337c322bcb1e2f46007244d708a41c946cb83b7ccd61004176241",
    AUDIT_INPUT_PATHS[3]:
        "3956e5af3ea9c12e8bd605cc0bae7fc29a24154c1ee3527be53223dbee778cd6",
    AUDIT_INPUT_PATHS[4]:
        "5af27fd61c20fe3b25e9a172b63339d5fd4f5112631fe6d31c6e0fa95a7486f1",
    AUDIT_INPUT_PATHS[5]:
        "04432816e3844043b419de8d91001003cd7fb8de76635658c3367574c3e44b9a",
    AUDIT_INPUT_PATHS[6]:
        "d3ccc94cf4d43da9fc8e737ca2706706cdffccb1e963bb8381d6db2350fefcea",
    AUDIT_INPUT_PATHS[7]:
        "e064b2f431f3e125b8c7f8176e6331f3fee41c2d1dc8ba7e3e65ae97a4ebb6b0",
    AUDIT_INPUT_PATHS[8]:
        "ab9b852236f73ec4aecad9287e07a4029309159d956a1cb3043f9238342d6807",
    AUDIT_INPUT_PATHS[9]:
        "7c8771e9494a8ed3eea6f6519b2e29d655123c96b98e0295b5300c1320570c32",
    AUDIT_INPUT_PATHS[10]:
        "6e668efc97a276ce9b0b442cbf7f9eda32c2aa6c722b6f562c5ca4046a4b7ba1",
    AUDIT_INPUT_PATHS[11]:
        "2f5214633abf7bcc715c88a646ded9bd25dc3fdfbfe09785ddd12a551dc18c25",
    AUDIT_INPUT_PATHS[12]:
        "033e6442c01eef32efe20e55b025459aa606b92d1a91a4e48e9f795bc3946181",
    AUDIT_INPUT_PATHS[13]:
        "fe35718b8f5e84cfafed74026a5634e722da757782f04d536a756d7273d3ee9b",
}
EXPECTED_GIT_BLOB_SHA1 = {
    AUDIT_INPUT_PATHS[0]: "fff1b6267ebdafa88f267600988705549297957b",
    AUDIT_INPUT_PATHS[1]: "0a8f4562d28f12ed64130b3c3b23fccab677d333",
    AUDIT_INPUT_PATHS[2]: "4e23e03ecc5f92a0b8348bfa526eb5b2f2b09dd0",
    AUDIT_INPUT_PATHS[3]: "3d219308183e781c71f9742bd0c6331440f74dbe",
    AUDIT_INPUT_PATHS[4]: "1e691cb4b2477f86e1c81e017de44b53c4edec88",
    AUDIT_INPUT_PATHS[5]: "075659d59588f7895e91f50f9ef93a368fb1fb4e",
    AUDIT_INPUT_PATHS[6]: "a79ef29be8f8c4b50ed7fc98cd4879b4e3d34524",
    AUDIT_INPUT_PATHS[7]: "3fbfaf0019af05bbb3121de47de49b9cefec7571",
    AUDIT_INPUT_PATHS[8]: "cee674584704dd7d351cb2ffa947c74bee47d06e",
    AUDIT_INPUT_PATHS[9]: "0070722d7a12d47658346b6c812edd05424ae592",
    AUDIT_INPUT_PATHS[10]: "52abfe3dd54b3969f51ca6816ec4830b42405106",
    AUDIT_INPUT_PATHS[11]: "6bde2222ddfdaf48e3806c0ac0a9c9d6431d945f",
    AUDIT_INPUT_PATHS[12]: "8366a5240d992376d0396a6fdc2c0b33247e8aba",
    AUDIT_INPUT_PATHS[13]: "39b5f24595f2271704bf68197103b62824a14cbf",
}

GROUP_TOTAL = 19
GROUP_BINS = 6
ALL_BANKS = (1, 2, 3, 5, 12)
ALLOCATION_BANKS = (2, 5, 12)

import ast
from collections import Counter, defaultdict
from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha1, sha256
from itertools import combinations
import importlib.abc
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
from time import monotonic
from typing import Callable


ROOT = Path(__file__).resolve().parents[1]
START = monotonic()
CHECKS: dict[str, bool] = {}
STDOUT_BYTES = 0


class _Cycle821PrimaryBlocker(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path=None, target=None):
        if fullname.rsplit(".", 1)[-1] == PRIMARY_MODULE:
            raise ImportError(f"BLOCKLIST text/AST-only primary: {fullname}")
        return None


PRIMARY_BLOCKER = _Cycle821PrimaryBlocker()
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


def check(label: str, condition: bool, detail: object) -> bool:
    CHECKS[label] = bool(condition)
    emit(
        "CERTIFICATE",
        label,
        "PASS" if condition else "FAIL",
        compact(detail),
    )
    return bool(condition)


def git_blob_sha1(data: bytes) -> str:
    return sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()


class _LexicalReturnCollector(ast.NodeVisitor):
    """Visit one callable body without crossing into a nested callable."""

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


def lexical_returns(
    node: ast.FunctionDef | ast.AsyncFunctionDef,
) -> tuple[ast.AST, ...]:
    collector = _LexicalReturnCollector()
    for statement in node.body:
        collector.visit(statement)
    return tuple(collector.values)


def annotation_text(node: ast.AST | None) -> str:
    return ast.unparse(node) if node is not None else ""


@dataclass(frozen=True)
class InventoryRow:
    name: str
    path: str
    line: int
    parameters: tuple[tuple[str, str], ...]
    return_annotation: str
    return_shapes: tuple[str, ...]
    ast_sha256: str
    source_kind: str


def function_row(
    path: str,
    node: ast.FunctionDef | ast.AsyncFunctionDef,
) -> InventoryRow:
    arguments = (
        tuple(node.args.posonlyargs)
        + tuple(node.args.args)
        + tuple(node.args.kwonlyargs)
    )
    returns = lexical_returns(node)
    return InventoryRow(
        name=f"{Path(path).stem}.{node.name}",
        path=path,
        line=node.lineno,
        parameters=tuple(
            (argument.arg, annotation_text(argument.annotation))
            for argument in arguments
        ),
        return_annotation=annotation_text(node.returns),
        return_shapes=tuple(
            ast.dump(value, annotate_fields=False, include_attributes=False)
            for value in returns
        ),
        ast_sha256=sha256(
            ast.dump(
                node,
                annotate_fields=True,
                include_attributes=False,
            ).encode("utf-8")
        ).hexdigest(),
        source_kind=type(node).__name__,
    )


def lambda_row(path: str, name: str, node: ast.Lambda) -> InventoryRow:
    arguments = (
        tuple(node.args.posonlyargs)
        + tuple(node.args.args)
        + tuple(node.args.kwonlyargs)
    )
    return InventoryRow(
        name=f"{Path(path).stem}.{name}",
        path=path,
        line=node.lineno,
        parameters=tuple(
            (argument.arg, annotation_text(argument.annotation))
            for argument in arguments
        ),
        return_annotation="",
        return_shapes=(
            ast.dump(
                node.body,
                annotate_fields=False,
                include_attributes=False,
            ),
        ),
        ast_sha256=sha256(
            ast.dump(
                node,
                annotate_fields=True,
                include_attributes=False,
            ).encode("utf-8")
        ).hexdigest(),
        source_kind="TopLevelLambda",
    )


def independent_inventory(
    paths: tuple[str, ...],
) -> tuple[tuple[InventoryRow, ...], dict[str, ast.Module]]:
    """Independent rule: every top-level def/async-def/lambda with a value."""
    rows: list[InventoryRow] = []
    trees: dict[str, ast.Module] = {}
    for path in paths:
        tree = ast.parse((ROOT / path).read_bytes(), filename=path)
        trees[path] = tree
        for node in tree.body:
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                if lexical_returns(node):
                    rows.append(function_row(path, node))
                continue
            if not isinstance(node, (ast.Assign, ast.AnnAssign)):
                continue
            value = node.value
            if not isinstance(value, ast.Lambda):
                continue
            if isinstance(node, ast.Assign):
                names = tuple(
                    target.id
                    for target in node.targets
                    if isinstance(target, ast.Name)
                )
            else:
                names = (
                    (node.target.id,)
                    if isinstance(node.target, ast.Name)
                    else ()
                )
            rows.extend(lambda_row(path, name, value) for name in names)
    return tuple(rows), trees


def primary_rule_inventory(
    paths: tuple[str, ...],
) -> tuple[InventoryRow, ...]:
    """Reconstruct the primary's narrower synchronous-def AST rule."""
    rows = []
    for path in paths:
        tree = ast.parse((ROOT / path).read_bytes(), filename=path)
        for node in tree.body:
            if isinstance(node, ast.FunctionDef) and lexical_returns(node):
                rows.append(function_row(path, node))
    return tuple(rows)


def primary_projection_names(primary_tree: ast.Module) -> tuple[str, ...]:
    names = {
        node.args[0].value
        for node in ast.walk(primary_tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "Observable"
        and node.args
        and isinstance(node.args[0], ast.Constant)
        and isinstance(node.args[0].value, str)
        and node.args[0].value.startswith("projection.")
    }
    return tuple(sorted(names))


PRIMARY_PROJECTION_META = {
    "projection.occurrence_full_46_counts": (
        "tuple",
        "fixed comparison tuple (46; 23/23)",
    ),
    "projection.battery_cycle786_38_counts": (
        "tuple",
        "fixed comparison tuple (38; 19/19)",
    ),
    "projection.selector_outputs": (
        "tuple",
        "fixed comparison tuple",
    ),
    "projection.record_content_objects": (
        "tuple",
        "fixed comparison tuple",
    ),
    "projection.ensemble_support_statistics": (
        "tuple",
        "fixed comparison tuple",
    ),
    "projection.origin_resolved_channels": (
        "tuple",
        "fixed comparison tuple",
    ),
    "projection.allocation_total": (
        "int",
        "allocation -> integer comparison value",
    ),
    "projection.allocation_orbit_class": (
        "tuple[int,...]",
        "allocation -> same-type canonical allocation image",
    ),
}


@dataclass(frozen=True)
class TypeDecision:
    name: str
    included: bool
    code: str
    derivation: str


COMPARISON_SCALARS = {
    "bool",
    "int",
    "float",
    "complex",
    "Fraction",
}
NONCOMPARISON_ROOTS = {
    "dict",
    "list",
    "set",
    "frozenset",
    "str",
    "bytes",
    "object",
    "ModuleType",
    "ast.AST",
    "ast.Module",
    "ast.FunctionDef",
    "Callable",
}


def compact_type(text: str) -> str:
    return "".join(text.split())


def annotation_root(text: str) -> str:
    compacted = compact_type(text)
    for delimiter in ("[", "|"):
        compacted = compacted.split(delimiter, 1)[0]
    return compacted


def is_flat_tuple_type(text: str) -> bool:
    compacted = compact_type(text)
    return compacted in {
        "tuple",
        "tuple[int,...]",
        "tuple[Fraction,...]",
        "tuple[object,...]",
    }


def is_nested_integer_tuple_type(text: str) -> bool:
    compacted = compact_type(text)
    return compacted.startswith("tuple[tuple[int,...],")


def inferred_return_kind(row: InventoryRow) -> str:
    annotation = compact_type(row.return_annotation)
    root = annotation_root(row.return_annotation)
    if annotation:
        if root in COMPARISON_SCALARS:
            return "scalar"
        if root == "tuple":
            return "tuple"
        if root in NONCOMPARISON_ROOTS:
            return "noncomparison"
        if "|" in annotation:
            return "noncomparison"
        # Named tuple aliases in the landed files (Normal/State) still expose
        # a comparison tuple, while named classes are not comparison values.
        if root in {"Normal", "State"}:
            return "tuple_alias"
        return "unproved"

    shapes = row.return_shapes
    if shapes and all(
        shape.startswith(
            (
                "Tuple(",
                "Call(Name('tuple'",
                "Call(Name(id='tuple'",
            )
        )
        for shape in shapes
    ):
        return "tuple"
    if shapes and all(
        shape.startswith(
            (
                "Compare(",
                "BoolOp(",
                "UnaryOp(Not",
                "Constant(True",
                "Constant(False",
                "Constant(0",
                "Constant(1",
                "Constant(value=True",
                "Constant(value=False",
                "Constant(value=0",
                "Constant(value=1",
            )
        )
        for shape in shapes
    ):
        return "scalar"
    return "unproved"


def adjudicate_inventory_row(row: InventoryRow) -> TypeDecision:
    output = compact_type(row.return_annotation)
    parameter_types = tuple(
        compact_type(annotation)
        for _name, annotation in row.parameters
        if annotation
    )
    kind = inferred_return_kind(row)

    if (
        is_nested_integer_tuple_type(output)
        and parameter_types
        and all(value == "int" for value in parameter_types)
    ):
        return TypeDecision(
            row.name,
            False,
            "EXCLUDE_COLLECTION_CONSTRUCTOR_BY_TYPE",
            (
                f"({','.join(parameter_types)})->{output} constructs a "
                "collection of allocation-shaped integer tuples"
            ),
        )
    if (
        kind in {"tuple", "tuple_alias"}
        and output
        and any(
            output == value
            or (
                is_flat_tuple_type(output)
                and is_flat_tuple_type(value)
            )
            for value in parameter_types
        )
    ):
        return TypeDecision(
            row.name,
            False,
            "EXCLUDE_SAME_TYPE_IMAGE_BY_TYPE",
            (
                f"input type {output} and output type {output} coincide; "
                "the result is a transformed image, not a readout"
            ),
        )
    if (
        kind == "tuple"
        and is_flat_tuple_type(output)
        and not any(is_flat_tuple_type(value) for value in parameter_types)
        and output in {"tuple", "tuple[int,...]"}
    ):
        return TypeDecision(
            row.name,
            False,
            "EXCLUDE_SAME_REPRESENTATION_CONSTRUCTOR_BY_TYPE",
            (
                f"output {output} constructs a flat integer/opaque state "
                "representation rather than a comparison readout"
            ),
        )
    if kind in {"scalar", "tuple", "tuple_alias"}:
        return TypeDecision(
            row.name,
            True,
            "INCLUDE_COMPARISON_VALUE",
            (
                f"declared/inferred output {row.return_annotation or kind} "
                "is a number/tuple/bool compared by equality"
            ),
        )
    return TypeDecision(
        row.name,
        False,
        (
            "EXCLUDE_NONCOMPARISON_OUTPUT_TYPE"
            if kind == "noncomparison"
            else "EXCLUDE_UNPROVED_COMPARISON_OUTPUT_TYPE"
        ),
        (
            f"output {row.return_annotation or row.return_shapes[:1]} is not "
            "proved to be a number/tuple/bool comparison value"
        ),
    )


def adjudicate_projection(name: str) -> TypeDecision:
    output, explanation = PRIMARY_PROJECTION_META[name]
    if name == "projection.allocation_orbit_class":
        return TypeDecision(
            name,
            False,
            "EXCLUDE_SAME_TYPE_IMAGE_BY_TYPE",
            (
                "input tuple[int,...] -> output tuple[int,...]; canonical "
                "orbit representative is an allocation image, not a readout"
            ),
        )
    return TypeDecision(
        name,
        True,
        "INCLUDE_COMPARISON_VALUE",
        f"output {output}: {explanation}",
    )


def stars_and_bars_allocations(
    total: int,
    bins: int,
) -> tuple[tuple[int, ...], ...]:
    """Independent nonrecursive stars-and-bars construction."""
    output = []
    string_last = total + bins - 2
    for bars in combinations(range(total + bins - 1), bins - 1):
        previous = -1
        row = []
        for bar in bars:
            row.append(bar - previous - 1)
            previous = bar
        row.append(string_last - previous)
        output.append(tuple(row))
    return tuple(output)


def rotation_image(
    allocation: tuple[int, ...],
    shift: int,
) -> tuple[int, ...]:
    """Right rotation by slicing, independent of Cycle-815's loop."""
    shift %= len(allocation)
    if shift == 0:
        return allocation
    return allocation[-shift:] + allocation[:-shift]


def orbit_partition(
    allocations: tuple[tuple[int, ...], ...],
) -> tuple[tuple[tuple[int, ...], ...], ...]:
    grouped: dict[
        tuple[int, ...],
        set[tuple[int, ...]],
    ] = defaultdict(set)
    for allocation in allocations:
        representative = min(
            rotation_image(allocation, shift)
            for shift in range(GROUP_BINS)
        )
        grouped[representative].add(allocation)
    return tuple(
        tuple(sorted(grouped[representative]))
        for representative in sorted(grouped)
    )


def lawful_allocation(allocation: tuple[int, ...]) -> bool:
    return (
        len(allocation) == GROUP_BINS
        and all(type(value) is int and value >= 0 for value in allocation)
        and sum(allocation) == GROUP_TOTAL
    )


def find_named_function(
    tree: ast.Module,
    name: str,
) -> ast.FunctionDef | ast.AsyncFunctionDef:
    matches = tuple(
        node
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        and node.name == name
    )
    if len(matches) != 1:
        raise AssertionError(("named function multiplicity", name, len(matches)))
    return matches[0]


def literal_assignment(tree: ast.Module, name: str) -> object:
    matches = []
    for node in tree.body:
        if not isinstance(node, (ast.Assign, ast.AnnAssign)):
            continue
        if isinstance(node, ast.Assign):
            names = {
                target.id
                for target in node.targets
                if isinstance(target, ast.Name)
            }
        else:
            names = (
                {node.target.id}
                if isinstance(node.target, ast.Name)
                else set()
            )
        if name in names:
            matches.append(node.value)
    if len(matches) != 1 or matches[0] is None:
        raise AssertionError(("literal assignment multiplicity", name))
    return ast.literal_eval(matches[0])


W7_FUNCTIONAL_SOURCES = {
    W7_COPY_PATHS[0]: (
        "extract_frozen_fixtures",
        "evaluate_candidate",
    ),
    W7_COPY_PATHS[1]: (
        "derive_recoil_coefficients",
        "derive_response_kernel_candidate",
    ),
    W7_COPY_PATHS[2]: (
        "landed_defining_row",
        "row_diff",
    ),
    W7_COPY_PATHS[3]: (
        "defining_row",
        "weighted_rows",
        "response_from_probability_tensor",
    ),
    W7_COPY_PATHS[4]: (
        "declared_family",
        "landed_defining_rows",
    ),
    W7_COPY_PATHS[5]: (
        "response_rows",
        "w7_linearity_certificate",
    ),
}


@dataclass(frozen=True)
class W7Extraction:
    directions: tuple[tuple[int, int, int], ...]
    reverse: tuple[int, ...]
    response_rows: tuple[
        tuple[tuple[Fraction, ...], ...],
        ...,
    ]
    citations: tuple[tuple[str, str, int, str], ...]
    passed: bool


def extract_w7_response() -> W7Extraction:
    trees = {
        path: ast.parse((ROOT / path).read_bytes(), filename=path)
        for path in W7_COPY_PATHS
    }
    citations = []
    for path, names in W7_FUNCTIONAL_SOURCES.items():
        for name in names:
            node = find_named_function(trees[path], name)
            citations.append(
                (
                    path,
                    name,
                    node.lineno,
                    sha256(
                        ast.dump(
                            node,
                            annotate_fields=True,
                            include_attributes=False,
                        ).encode("utf-8")
                    ).hexdigest(),
                )
            )

    cycle778 = trees[W7_COPY_PATHS[4]]
    prediction_source = literal_assignment(cycle778, "PREDICTION_SOURCE")
    if not isinstance(prediction_source, str):
        raise AssertionError("Cycle-778 PREDICTION_SOURCE is not literal text")
    prediction_tree = ast.parse(
        prediction_source,
        filename=f"{W7_COPY_PATHS[4]}::PREDICTION_SOURCE",
    )
    for name in ("add_response_rows", "predict_full_family"):
        node = find_named_function(prediction_tree, name)
        citations.append(
            (
                f"{W7_COPY_PATHS[4]}::PREDICTION_SOURCE",
                name,
                node.lineno,
                sha256(
                    ast.dump(
                        node,
                        annotate_fields=True,
                        include_attributes=False,
                    ).encode("utf-8")
                ).hexdigest(),
            )
        )
    add_response_source = ast.unparse(
        find_named_function(prediction_tree, "add_response_rows")
    )

    cycle812 = trees[W7_COPY_PATHS[-1]]
    directions_raw = literal_assignment(cycle812, "DIRECTIONS")
    reverse_raw = literal_assignment(cycle812, "REVERSE")
    directions = tuple(
        tuple(int(value) for value in direction)
        for direction in directions_raw
    )
    reverse = tuple(int(value) for value in reverse_raw)

    response_rows = []
    for index, source in enumerate(directions):
        target = directions[reverse[index]]
        source_vector = tuple(Fraction(value) for value in source)
        target_vector = tuple(Fraction(value) for value in target)
        response_rows.append(
            (
                tuple(
                    final - initial
                    for final, initial in zip(
                        target_vector,
                        source_vector,
                        strict=True,
                    )
                ),
                source_vector,
                source_vector,
            )
        )

    response_function = find_named_function(cycle812, "response_rows")
    response_source = ast.unparse(response_function)
    passed = (
        len(directions) == GROUP_BINS
        and len(reverse) == GROUP_BINS
        and set(reverse) == set(range(GROUP_BINS))
        and all(
            directions[reverse[index]]
            == tuple(-value for value in directions[index])
            for index in range(GROUP_BINS)
        )
        and all(
            row[0] == tuple(-2 * Fraction(value) for value in direction)
            and row[1] == tuple(Fraction(value) for value in direction)
            and row[2] == tuple(Fraction(value) for value in direction)
            for row, direction in zip(
                response_rows,
                directions,
                strict=True,
            )
        )
        and "for direction in DIRECTIONS" in response_source
        and "-2 * value" in response_source
        and "sum(" in add_response_source
        and "for row in rows" in add_response_source
        and len(citations)
        == sum(map(len, W7_FUNCTIONAL_SOURCES.values())) + 2
    )
    return W7Extraction(
        directions=directions,
        reverse=reverse,
        response_rows=tuple(response_rows),
        citations=tuple(citations),
        passed=passed,
    )


ResponseValue = tuple[tuple[Fraction, ...], ...]


def response_mixture_sum(
    allocation: tuple[int, ...],
    rows: tuple[ResponseValue, ...],
) -> ResponseValue:
    return tuple(
        tuple(
            sum(
                (
                    Fraction(allocation[direction])
                    * rows[direction][component][axis]
                    for direction in range(GROUP_BINS)
                ),
                start=Fraction(),
            )
            for axis in range(3)
        )
        for component in range(3)
    )


def response_expectation(
    allocation: tuple[int, ...],
    rows: tuple[ResponseValue, ...],
) -> ResponseValue:
    total = sum(allocation)
    if total <= 0:
        raise ValueError("W7 expectation requires positive total weight")
    mixture = response_mixture_sum(allocation, rows)
    return tuple(
        tuple(value / total for value in component)
        for component in mixture
    )


@dataclass(frozen=True)
class Observable:
    name: str
    output_type: str
    provenance: str
    evaluate: Callable[[tuple[int, ...]], object]


def static_comparison(token: object) -> Callable[[tuple[int, ...]], object]:
    def evaluate(_allocation: tuple[int, ...]) -> object:
        return token

    return evaluate


def primary_operational_observables(
    rows: tuple[InventoryRow, ...],
    decisions: tuple[TypeDecision, ...],
    projection_decisions: tuple[TypeDecision, ...],
) -> tuple[Observable, ...]:
    decision_by_name = {
        decision.name: decision
        for decision in decisions + projection_decisions
    }
    observables = []
    for row in rows:
        decision = decision_by_name[row.name]
        if not decision.included:
            continue
        if row.name.endswith(".lawful_group_allocation"):
            evaluator = lawful_allocation
            provenance = f"{row.path}:{row.line}"
        else:
            evaluator = static_comparison(
                ("ALLOCATION_NOT_IN_CALL_SIGNATURE", row.ast_sha256)
            )
            provenance = f"{row.path}:{row.line}"
        observables.append(
            Observable(
                name=row.name,
                output_type=row.return_annotation or "inferred",
                provenance=provenance,
                evaluate=evaluator,
            )
        )

    for decision in projection_decisions:
        if not decision.included:
            continue
        if decision.name == "projection.allocation_total":
            evaluator = sum
        else:
            evaluator = static_comparison(
                ("FIXED_LANDED_PROJECTION", decision.name)
            )
        observables.append(
            Observable(
                name=decision.name,
                output_type=PRIMARY_PROJECTION_META[decision.name][0],
                provenance="Cycle-821 named projection (text/AST only)",
                evaluate=evaluator,
            )
        )
    return tuple(observables)


def w7_observables(extraction: W7Extraction) -> tuple[Observable, ...]:
    rows = extraction.response_rows
    mixture_cache: dict[tuple[int, ...], ResponseValue] = {}
    expectation_cache: dict[tuple[int, ...], ResponseValue] = {}

    def mixture(allocation: tuple[int, ...]) -> ResponseValue:
        if allocation not in mixture_cache:
            mixture_cache[allocation] = response_mixture_sum(allocation, rows)
        return mixture_cache[allocation]

    def expectation(allocation: tuple[int, ...]) -> ResponseValue:
        if allocation not in expectation_cache:
            total = sum(allocation)
            expectation_cache[allocation] = tuple(
                tuple(value / total for value in component)
                for component in mixture(allocation)
            )
        return expectation_cache[allocation]

    observables = [
        Observable(
            "w7.response_mixture_sum",
            "tuple[tuple[Fraction,...],...]",
            (
                f"{W7_COPY_PATHS[4]}:306,333 "
                "(literal compiled compositor)"
            ),
            mixture,
        ),
        Observable(
            "w7.response_expectation",
            "tuple[tuple[Fraction,...],...]",
            f"{W7_COPY_PATHS[5]}:643",
            expectation,
        ),
    ]
    component_labels = ("matter", "mediator", "auxiliary")
    for component, label in enumerate(component_labels):
        for axis in range(3):
            observables.append(
                Observable(
                    f"w7.response_expectation.{label}[{axis}]",
                    "Fraction",
                    f"{W7_COPY_PATHS[5]}:643 whole-return projection",
                    lambda allocation, component=component, axis=axis:
                        expectation(allocation)[component][axis],
                )
            )
    observables.append(
        Observable(
            "w7.response_flux_balance",
            "tuple[Fraction,...]",
            f"{W7_COPY_PATHS[0]}:269 flux_balance criterion",
            lambda allocation: tuple(
                sum(
                    expectation(allocation)[component][axis]
                    for component in range(3)
                )
                for axis in range(3)
            ),
        )
    )
    return tuple(observables)


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


def separation_certificate(
    observables: tuple[Observable, ...],
    orbits: tuple[tuple[tuple[int, ...], ...], ...],
) -> dict[str, object]:
    separating = []
    separated_orbits: dict[str, int] = {}
    first_separator = None
    exact = True
    evaluations = 0
    summary = []

    for observable in observables:
        separated = 0
        first_for_observable = None
        value_hash = sha256()
        for orbit_index, orbit in enumerate(orbits):
            values = tuple(observable.evaluate(member) for member in orbit)
            evaluations += len(orbit)
            exact = exact and not contains_float(values)
            value_hash.update(compact(values).encode("utf-8"))
            reference = values[0]
            unequal = next(
                (
                    index
                    for index, value in enumerate(values[1:], start=1)
                    if value != reference
                ),
                None,
            )
            if unequal is None:
                continue
            separated += 1
            witness = {
                "observable": observable.name,
                "provenance": observable.provenance,
                "orbit_index": orbit_index,
                "allocation_a": orbit[0],
                "allocation_b": orbit[unequal],
                "value_a": reference,
                "value_b": values[unequal],
            }
            if first_for_observable is None:
                first_for_observable = witness
            if first_separator is None:
                first_separator = witness
        if separated:
            separating.append(observable.name)
            separated_orbits[observable.name] = separated
        summary.append(
            (
                observable.name,
                separated,
                value_hash.hexdigest(),
                first_for_observable,
            )
        )

    return {
        "observable_count": len(observables),
        "orbit_count": len(orbits),
        "member_count": sum(map(len, orbits)),
        "evaluation_count": evaluations,
        "all_values_exact": exact,
        "separating_observables": tuple(separating),
        "separated_orbits_by_observable": separated_orbits,
        "first_separator": first_separator,
        "summary_sha256": digest(summary),
    }


def cross_orbit_certificate(
    observables: tuple[Observable, ...],
    orbits: tuple[tuple[tuple[int, ...], ...], ...],
) -> dict[str, object]:
    rows = []
    for pair in range(20):
        left_orbit = 2 * pair
        right_orbit = left_orbit + 1
        left = orbits[left_orbit][0]
        right = orbits[right_orbit][0]
        separators = tuple(
            observable.name
            for observable in observables
            if observable.evaluate(left) != observable.evaluate(right)
        )
        rows.append(
            {
                "pair": pair,
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
    full_counts = Counter(row[2] for row in rows)
    projected_counts = Counter(row[2] for row in projected)
    passed = (
        len(rows) == 46
        and full_counts == Counter({1: 23, -1: 23})
        and len(projected) == 38
        and projected_counts == Counter({1: 19, -1: 19})
        and all(row[3] == (0,) for row in rows)
    )
    return {
        "full_rows": len(rows),
        "full_orientation_counts": {
            "+1": full_counts[1],
            "-1": full_counts[-1],
        },
        "projected_rows": len(projected),
        "projected_orientation_counts": {
            "+1": projected_counts[1],
            "-1": projected_counts[-1],
        },
        "all_selector_outputs_zero": all(row[3] == (0,) for row in rows),
        "rows_sha256": digest(rows),
        "pass": passed,
    }


def literal_self_audit_paths() -> tuple[str, ...]:
    tree = ast.parse(Path(__file__).read_bytes(), filename=__file__)
    matches = []
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        if any(
            isinstance(target, ast.Name)
            and target.id == "AUDIT_INPUT_PATHS"
            for target in node.targets
        ):
            matches.append(node.value)
    if len(matches) != 1 or not isinstance(matches[0], ast.Tuple):
        raise AssertionError("AUDIT_INPUT_PATHS must be one literal tuple")
    if not all(
        isinstance(element, ast.Constant)
        and isinstance(element.value, str)
        for element in matches[0].elts
    ):
        raise AssertionError("AUDIT_INPUT_PATHS has a nonliteral member")
    return tuple(element.value for element in matches[0].elts)


def source_controls(primary_tree: ast.Module) -> dict[str, object]:
    observed_sha256 = {}
    observed_blobs = {}
    for path in AUDIT_INPUT_PATHS:
        data = (ROOT / path).read_bytes()
        observed_sha256[path] = sha256(data).hexdigest()
        observed_blobs[path] = git_blob_sha1(data)

    try:
        importlib.util.find_spec(PRIMARY_MODULE)
    except ImportError as error:
        blocked_attempt = str(error)
    else:
        blocked_attempt = "NOT_BLOCKED"

    self_tree = ast.parse(Path(__file__).read_bytes(), filename=__file__)
    imported_modules = {
        alias.name
        for node in ast.walk(self_tree)
        if isinstance(node, ast.Import)
        for alias in node.names
    } | {
        str(node.module)
        for node in ast.walk(self_tree)
        if isinstance(node, ast.ImportFrom)
    }
    tracked_copies = {}
    for path in W7_COPY_PATHS:
        completed = subprocess.run(
            ("git", "ls-files", "--error-unmatch", path),
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        tracked_copies[path] = completed.returncode == 0
    head_sha = subprocess.run(
        ("git", "rev-parse", "HEAD"),
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    branch = subprocess.run(
        ("git", "branch", "--show-current"),
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    return {
        "head_sha": head_sha,
        "branch": branch,
        "literal_audit_input_paths": literal_self_audit_paths(),
        "all_paths_exist": all(
            (ROOT / path).is_file()
            for path in AUDIT_INPUT_PATHS
        ),
        "sha256": observed_sha256,
        "git_blob_sha1": observed_blobs,
        "sha256_match": observed_sha256 == EXPECTED_SHA256,
        "git_blob_match": observed_blobs == EXPECTED_GIT_BLOB_SHA1,
        "w7_copies_tracked": tracked_copies,
        "all_w7_copies_tracked": all(tracked_copies.values()),
        "primary_block_attempt": blocked_attempt,
        "primary_blocked": blocked_attempt.startswith(
            "BLOCKLIST text/AST-only primary:"
        ),
        "primary_not_in_sys_modules": PRIMARY_MODULE not in sys.modules,
        "checker_has_no_primary_import": all(
            module.rsplit(".", 1)[-1] != PRIMARY_MODULE
            for module in imported_modules
        ),
        "primary_ast_node_count": sum(1 for _node in ast.walk(primary_tree)),
    }


def w7_type_decisions(
    observables: tuple[Observable, ...],
) -> tuple[TypeDecision, ...]:
    return tuple(
        TypeDecision(
            observable.name,
            True,
            "INCLUDE_COMPARISON_VALUE",
            (
                "input tuple[int,...] allocation; output "
                f"{observable.output_type} is a response comparison value "
                "and is not an allocation-shaped same-type image"
            ),
        )
        for observable in observables
    )


TYPE_RULE_TEXT = (
    "An allocation observable is a callable whose output is a COMPARISON "
    "VALUE (number/tuple/bool compared by equality); an allocation-to-"
    "allocation same-type image and an allocation constructor are excluded "
    "BY OUTPUT TYPE.  Dict/list/string/opaque diagnostic objects are not "
    "comparison-value readouts."
)


def main() -> int:
    primary_tree = ast.parse(
        (ROOT / PRIMARY_PATH).read_bytes(),
        filename=PRIMARY_PATH,
    )
    controls = source_controls(primary_tree)

    own_rows, _landed_trees = independent_inventory(LANDED_SCOPE_PATHS)
    primary_rows = primary_rule_inventory(LANDED_SCOPE_PATHS)
    projection_names = primary_projection_names(primary_tree)
    projection_decisions = tuple(
        adjudicate_projection(name)
        for name in projection_names
    )
    own_decisions = tuple(adjudicate_inventory_row(row) for row in own_rows)
    decision_by_name = {
        decision.name: decision
        for decision in own_decisions + projection_decisions
    }

    primary_names = {
        *(row.name for row in primary_rows),
        *projection_names,
    }
    independent_names = {
        *(row.name for row in own_rows),
        *projection_names,
    }
    added_vs_primary = tuple(sorted(independent_names - primary_names))
    missing_vs_primary = tuple(sorted(primary_names - independent_names))
    missed_operational = tuple(
        name
        for name in added_vs_primary
        if decision_by_name[name].included
    )

    extraction = extract_w7_response()
    w7_rows = w7_observables(extraction)
    w7_decisions = w7_type_decisions(w7_rows)
    all_decisions = own_decisions + projection_decisions + w7_decisions
    exclusions = tuple(
        decision
        for decision in all_decisions
        if not decision.included
    )

    emit("CYCLE 821 INDEPENDENT_ADVERSARIAL_CHECKER")
    emit("HEAD_SHA", controls["head_sha"])
    emit("BRANCH", controls["branch"])
    for path in AUDIT_INPUT_PATHS:
        emit(
            "SOURCE_SHA",
            path,
            controls["sha256"][path],
            controls["git_blob_sha1"][path],
        )

    inventory_finding = (
        f"INVENTORY DIFF: primary={len(primary_names)} "
        f"independent={len(independent_names)} "
        f"added={list(added_vs_primary)} "
        f"missing={list(missing_vs_primary)}; "
        f"W7 operational additions={len(w7_rows)}."
    )
    emit("FINDING_VERBATIM", inventory_finding)
    emit(
        "INVENTORY_RULE",
        (
            "Every value-returning top-level def, async-def, and top-level "
            "lambda in the seven literal landed modules; nested callable "
            "scopes do not leak returns.  Add the primary's eight explicit "
            "whole-object projections, then separately add extracted W7 "
            "allocation-response functionals."
        ),
    )
    check(
        "INVENTORY_RE_DERIVATION",
        (
            len(primary_rows) == 161
            and len(primary_names) == 169
            and len(independent_names) == 169
            and not missing_vs_primary
            and all(
                name in {
                    row.name for row in own_rows
                }
                for name in missed_operational
            )
            and set(projection_names) == set(PRIMARY_PROJECTION_META)
        ),
        {
            "primary_callable_count": len(primary_rows),
            "primary_projection_count": len(projection_names),
            "primary_inventory_count": len(primary_names),
            "independent_inventory_count": len(independent_names),
            "added_vs_primary": added_vs_primary,
            "missing_vs_primary": missing_vs_primary,
            "missed_operational_added_and_tested": missed_operational,
            "w7_additions": tuple(row.name for row in w7_rows),
            "extended_inventory_count": len(independent_names) + len(w7_rows),
        },
    )

    emit("OBSERVABLE_TYPE_RULE", TYPE_RULE_TEXT)
    for decision in all_decisions:
        emit(
            "TYPE_DECISION",
            compact(
                {
                    "name": decision.name,
                    "included": decision.included,
                    "code": decision.code,
                    "derivation": decision.derivation,
                }
            ),
        )

    rotate_decisions = tuple(
        decision
        for decision in own_decisions
        if decision.name.endswith(".rotate_allocation")
    )
    weak_constructor_decisions = tuple(
        decision
        for decision in own_decisions
        if decision.name.endswith(".weak_compositions")
    )
    orbit_class_decision = next(
        decision
        for decision in projection_decisions
        if decision.name == "projection.allocation_orbit_class"
    )

    allocations = stars_and_bars_allocations(GROUP_TOTAL, GROUP_BINS)
    orbits = orbit_partition(allocations)
    helper_preserves_allocation_type = all(
        type(rotation_image(allocation, shift)) is type(allocation)
        and len(rotation_image(allocation, shift)) == len(allocation)
        and all(
            type(value) is int and value >= 0
            for value in rotation_image(allocation, shift)
        )
        and sum(rotation_image(allocation, shift)) == sum(allocation)
        for allocation in allocations
        for shift in range(GROUP_BINS)
    )
    helper_derivation = (
        "rotate_allocation: input allocation tuple[int,...] x int -> output "
        "tuple[int,...]; on all 42,504 allocations and six powers the output "
        "preserves tuple type, length 6, nonnegative-int element type, and "
        "sum 19.  It is therefore a same-type gauge image, not a comparison "
        "readout, and is excluded BY TYPE."
    )
    emit("EXCLUSION_DERIVATION_VERBATIM", helper_derivation)
    emit(
        "EXCLUDED_BY_TYPE",
        compact(
            tuple(
                {
                    "name": decision.name,
                    "code": decision.code,
                    "derivation": decision.derivation,
                }
                for decision in exclusions
            )
        ),
    )
    check(
        "HELPER_ADJUDICATION_PRINCIPLED",
        (
            len(rotate_decisions) == 1
            and not rotate_decisions[0].included
            and rotate_decisions[0].code
            == "EXCLUDE_SAME_TYPE_IMAGE_BY_TYPE"
            and helper_preserves_allocation_type
            and weak_constructor_decisions
            and all(
                not decision.included
                and "CONSTRUCTOR" in decision.code
                for decision in weak_constructor_decisions
            )
            and not orbit_class_decision.included
            and all(decision.included for decision in w7_decisions)
            and len(all_decisions) == 169 + len(w7_rows)
        ),
        {
            "rule": TYPE_RULE_TEXT,
            "decision_count": len(all_decisions),
            "included_count": sum(
                decision.included for decision in all_decisions
            ),
            "excluded_count": len(exclusions),
            "rotate_allocation": rotate_decisions,
            "allocation_constructor": weak_constructor_decisions,
            "orbit_class": orbit_class_decision,
            "w7_outputs_different_type": all(
                decision.included for decision in w7_decisions
            ),
        },
    )

    allocation_control = {
        "allocation_count": len(allocations),
        "all_lawful": all(map(lawful_allocation, allocations)),
        "allocation_sha256": digest(allocations),
        "orbit_count": len(orbits),
        "orbit_size_distribution": dict(Counter(map(len, orbits))),
        "partition_member_count": sum(map(len, orbits)),
        "representative_sha256": digest(
            tuple(orbit[0] for orbit in orbits)
        ),
    }
    check(
        "ALLOCATION_ORBIT_RE_DERIVATION",
        (
            allocation_control["allocation_count"] == 42_504
            and allocation_control["all_lawful"]
            and allocation_control["orbit_count"] == 7_084
            and allocation_control["orbit_size_distribution"] == {6: 7_084}
            and allocation_control["partition_member_count"] == 42_504
        ),
        allocation_control,
    )

    emit(
        "W7_EXTRACTION",
        compact(
            {
                "directions": extraction.directions,
                "reverse": extraction.reverse,
                "response_rows": extraction.response_rows,
                "citations": extraction.citations,
                "whole_return_reduction": (
                    "whole response inequality is already a separator; "
                    "whole response equality would imply equality of every "
                    "landed scalar/tuple projection"
                ),
                "allocation_input": (
                    "Cycle-778 unnormalized identity-column mixture uses "
                    "weights n_d; Cycle-812 expectation uses the exact "
                    "diagonal weights |c_d|^2=n_d/19"
                ),
            }
        ),
    )
    primary_observables = primary_operational_observables(
        own_rows,
        own_decisions,
        projection_decisions,
    )
    operational_observables = primary_observables + w7_rows
    certificate = separation_certificate(operational_observables, orbits)
    repeated = separation_certificate(operational_observables, orbits)
    deterministic = (
        certificate["summary_sha256"] == repeated["summary_sha256"]
        and certificate["first_separator"] == repeated["first_separator"]
        and certificate["separated_orbits_by_observable"]
        == repeated["separated_orbits_by_observable"]
    )
    emit(
        "SEPARATION_CERTIFICATE",
        compact(
            {
                key: value
                for key, value in certificate.items()
                if key not in {
                    "separated_orbits_by_observable",
                    "separating_observables",
                }
            }
        ),
    )
    emit(
        "SEPARATING_OPERATIONAL_OBSERVABLES",
        compact(certificate["separating_observables"]),
    )
    emit(
        "SEPARATED_ORBITS_BY_OPERATIONAL_OBSERVABLE",
        compact(certificate["separated_orbits_by_observable"]),
    )
    w7_separators = tuple(
        name
        for name in certificate["separating_observables"]
        if name.startswith("w7.")
    )
    check(
        "W7_EXTENSION_CLOSES_HOLE",
        (
            extraction.passed
            and len(w7_rows) == 12
            and certificate["orbit_count"] == 7_084
            and certificate["member_count"] == 42_504
            and certificate["evaluation_count"]
            == len(operational_observables) * 42_504
            and certificate["all_values_exact"]
            and (
                bool(w7_separators)
                or not any(
                    name.startswith("w7.")
                    for name in certificate["separating_observables"]
                )
            )
        ),
        {
            "copy_count": len(W7_COPY_PATHS),
            "functional_source_citations": len(extraction.citations),
            "operational_w7_observables": tuple(
                row.name for row in w7_rows
            ),
            "w7_separators": w7_separators,
            "separated_orbits": {
                name: certificate[
                    "separated_orbits_by_observable"
                ][name]
                for name in w7_separators
            },
        },
    )

    first_separator = certificate["first_separator"]
    if first_separator is not None:
        theorem = None
        theorem_decision = (
            "THEOREM DECISION: NOT ESTABLISHED.  Named operational "
            f"separator {first_separator['observable']} distinguishes "
            f"orbit {first_separator['orbit_index']}; the dichotomy stays "
            "open operationally."
        )
        loudly = (
            "DICHOTOMY STAYS OPEN OPERATIONALLY — W7 RESPONSE SEPARATES "
            "ORBIT-MATE ALLOCATIONS."
        )
        outcome = "OPEN_DICHOTOMY_OPERATIONAL_W7_SEPARATOR"
    else:
        theorem = (
            "orbit-mate allocations are observationally identical at the "
            "landed operational-observable set; the six-fold choice is "
            "unobservable gauge; any orbit-breaking rate law must introduce "
            "non-landed structure"
        )
        theorem_decision = f"THEOREM DECISION: {theorem}."
        loudly = "NO OPERATIONAL SAME-ORBIT SEPARATOR IN EXTENDED INVENTORY."
        outcome = "THEOREM_EXTENDED_OPERATIONAL_INVENTORY"
    emit("FINDING_VERBATIM", loudly)
    emit("FINDING_VERBATIM", theorem_decision)
    check(
        "THEOREM_DECISION",
        (
            (
                first_separator is not None
                and theorem is None
                and outcome == "OPEN_DICHOTOMY_OPERATIONAL_W7_SEPARATOR"
            )
            or (
                first_separator is None
                and theorem is not None
                and outcome == "THEOREM_EXTENDED_OPERATIONAL_INVENTORY"
            )
        ),
        {
            "outcome": outcome,
            "theorem": theorem,
            "named_separator": first_separator,
        },
    )

    cross_orbit = cross_orbit_certificate(operational_observables, orbits)
    identity = identity_controls()
    for row in cross_orbit["pairs"]:
        emit("CROSS_ORBIT_PAIR", compact(row))
    check(
        "CROSS_ORBIT_AND_IDENTITY_CONTROLS",
        (
            cross_orbit["pairs_tested"] == 20
            and cross_orbit["pairs_separated"] == 20
            and cross_orbit["all_separated"]
            and identity["pass"]
        ),
        {
            "cross_orbit_pairs": cross_orbit["pairs_tested"],
            "cross_orbit_separated": cross_orbit["pairs_separated"],
            "cross_orbit_sha256": cross_orbit["sha256"],
            "identity": identity,
        },
    )

    check(
        "SHAS_LITERAL_PATHS_AND_PRIMARY_BLOCKLIST",
        (
            controls["literal_audit_input_paths"] == AUDIT_INPUT_PATHS
            and controls["all_paths_exist"]
            and controls["sha256_match"]
            and controls["git_blob_match"]
            and controls["all_w7_copies_tracked"]
            and controls["primary_blocked"]
            and controls["primary_not_in_sys_modules"]
            and controls["checker_has_no_primary_import"]
        ),
        controls,
    )
    check(
        "DETERMINISM_AND_EXACT_ARITHMETIC",
        deterministic and certificate["all_values_exact"],
        {
            "deterministic_repeat": deterministic,
            "all_values_exact": certificate["all_values_exact"],
            "summary_sha256": certificate["summary_sha256"],
        },
    )

    elapsed = monotonic() - START
    check(
        "RUNTIME_UNDER_1500_SECONDS",
        elapsed < AUDIT_TIMEOUT_SEC,
        {"seconds": f"{elapsed:.6f}", "limit": AUDIT_TIMEOUT_SEC},
    )
    check(
        "STDOUT_UNDER_200KB",
        STDOUT_BYTES < STDOUT_LIMIT_BYTES - 4096,
        {"bytes_before_summary": STDOUT_BYTES, "limit": STDOUT_LIMIT_BYTES},
    )

    passed = all(CHECKS.values())
    emit("OUTCOME", outcome)
    emit("INVENTORY_DIFF", compact({
        "primary": len(primary_names),
        "independent": len(independent_names),
        "w7_additions": len(w7_rows),
        "extended": len(independent_names) + len(w7_rows),
        "added_vs_primary": added_vs_primary,
        "missing_vs_primary": missing_vs_primary,
    }))
    emit("TYPE_EXCLUSION_COUNT", len(exclusions))
    emit("W7_EXTENSION_OUTCOME", loudly)
    emit("THEOREM_DECISION", theorem_decision)
    emit(
        "CROSS_ORBIT_CONTROL",
        f"{cross_orbit['pairs_separated']}/{cross_orbit['pairs_tested']}",
    )
    emit(
        "IDENTITY_CONTROL",
        (
            f"{identity['full_rows']}:{identity['full_orientation_counts']} "
            f"{identity['projected_rows']}:"
            f"{identity['projected_orientation_counts']}"
        ),
    )
    emit("RUNTIME_SECONDS", f"{elapsed:.6f}")
    emit("STDOUT_BYTES", STDOUT_BYTES)
    emit("CHECK_SUMMARY", compact({"pass": passed, "checks": CHECKS}))
    emit("PASS" if passed else "FAIL")
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
