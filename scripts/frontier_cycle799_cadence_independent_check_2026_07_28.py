#!/usr/bin/env python3
"""Cycle 799 independent adversarial cadence-census checker.

The Cycle 799 and Cycle 796 primaries are inert text/AST inputs only.  This
checker resolves the 21 claimed predicates to their actual AST nodes, derives
their cadence from control/call placement, hunts omitted law-bearing branches,
and reconstructs the Cycle 796 monitor from the landed 719/736/750 suppliers.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle736_pairwise_separated_multisource_2026_07_28.py",
    "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
    "scripts/frontier_cycle758_selector_multisource_2026_07_28.py",
    "scripts/frontier_cycle781_checkpoint_refusal_law_2026_07_28.py",
    "scripts/frontier_cycle796_monitored_selector_2026_07_28.py",
    "scripts/frontier_cycle799_cadence_preference_2026_07_28.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from collections import Counter, defaultdict
from hashlib import sha256
import json
from pathlib import Path
import sys
from time import monotonic
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

TEXT_ONLY_BLOCKLIST = (
    "frontier_cycle796_monitored_selector_2026_07_28",
    "frontier_cycle799_cadence_preference_2026_07_28",
)
_BLOCKLIST_AT_IMPORT = tuple(
    name for name in TEXT_ONLY_BLOCKLIST if name in sys.modules
)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K719
import frontier_cycle736_pairwise_separated_multisource_2026_07_28 as M736
import frontier_cycle750_actual_selector_stretch_2026_07_28 as F750


EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "50059ce4d4d6e5ce4503e66ccb098f6fe663ad9711b106b6b6c5c9cb7bcbd02f",
    AUDIT_INPUT_PATHS[2]:
        "a74c7e5bbc297c57d317af7fd85d0b9e01d078625f5d4689daf2ebbdbc1cee0a",
    AUDIT_INPUT_PATHS[3]:
        "8be433f74cb337c322bcb1e2f46007244d708a41c946cb83b7ccd61004176241",
    AUDIT_INPUT_PATHS[4]:
        "b1158250dcb1449f6abac4f6bb6a0a90f47511a8a0f587e85483f4b6f3624211",
    AUDIT_INPUT_PATHS[5]:
        "be0238611e02f9bad8df813430f9decec68d287df267bbf82ba4a63ffc8483c3",
    AUDIT_INPUT_PATHS[6]:
        "6773ec05cc1db37a09f88232e7d1f8f9c4b87db98e5b620ad3ef57180ab1cddc",
}
CADENCES = (
    "orbit_return_boundary",
    "H_station_boundary",
    "Q_R1_R2_layer_boundary",
    "program_macro_completion",
)
PRIMARY_SPLIT = {
    "orbit_return_boundary": 8,
    "H_station_boundary": 4,
    "program_macro_completion": 9,
    "Q_R1_R2_layer_boundary": 0,
}
RING_STATIONS = 11
FIXTURE_BANKS = 2
MONITOR_CUTOFF = 371
EXPECTED_ACCEPTANCE_KEYS = (
    (3, (1, 10), 252),
    (3, (0, 7), 371),
)
EXPECTED_CLASSIFICATIONS = {
    "transient_accept": 2,
    "certified_cycle_refusal": 12,
    "open_refusal_through_cutoff": 162,
}
OUTPUT_LINES: list[str] = []


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def emit(label: str, detail: object | None = None) -> None:
    line = label if detail is None else label + " :: " + compact(detail)
    OUTPUT_LINES.append(line)
    print(line, flush=True)


def certificate(
    key: str, label: str, passed: bool, detail: object
) -> dict[str, object]:
    row = {
        "key": key,
        "label": label,
        "pass": bool(passed),
        "detail": detail,
    }
    emit(
        ("PASS" if passed else "FAIL")
        + f" CERTIFICATE_{key}_{label}",
        detail,
    )
    return row


def source_bytes(relative: str) -> bytes:
    return (ROOT / relative).read_bytes()


def source_snapshot() -> dict[str, dict[str, object]]:
    result = {}
    for relative in AUDIT_INPUT_PATHS:
        payload = source_bytes(relative)
        tree = ast.parse(payload, filename=relative)
        result[relative] = {
            "bytes": len(payload),
            "sha256": sha256(payload).hexdigest(),
            "ast_sha256": sha256(
                ast.dump(tree, include_attributes=False).encode("utf-8")
            ).hexdigest(),
        }
    return result


def parse_surface(relative: str) -> ast.Module:
    return ast.parse(
        source_bytes(relative).decode("utf-8"), filename=relative
    )


def top_functions(tree: ast.Module) -> dict[str, ast.FunctionDef]:
    return {
        node.name: node
        for node in tree.body
        if isinstance(node, ast.FunctionDef)
    }


def own_literal_inputs() -> bool:
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    matches = [
        node.value
        for node in tree.body
        if isinstance(node, ast.Assign)
        for target in node.targets
        if isinstance(target, ast.Name) and target.id == "AUDIT_INPUT_PATHS"
    ]
    return (
        len(matches) == 1
        and isinstance(matches[0], ast.Tuple)
        and all(
            isinstance(item, ast.Constant) and isinstance(item.value, str)
            for item in matches[0].elts
        )
        and ast.literal_eval(matches[0]) == AUDIT_INPUT_PATHS
    )


LAW_TARGETS = (
    {
        "law": "K719.forward_active_A_token_guard",
        "path": AUDIT_INPUT_PATHS[0],
        "function": "apply_controller_step",
        "locator": ("guard", "forward"),
    },
    {
        "law": "K719.inverse_active_A_token_guard",
        "path": AUDIT_INPUT_PATHS[0],
        "function": "apply_controller_step",
        "locator": ("guard", "inverse"),
    },
    {
        "law": "F750.forward_synchronous_composition",
        "path": AUDIT_INPUT_PATHS[2],
        "function": "enforcement_lineage_selector",
        "locator": ("expr", "after != expected"),
    },
    {
        "law": "F750.forward_token_rail_return",
        "path": AUDIT_INPUT_PATHS[2],
        "function": "enforcement_lineage_selector",
        "locator": ("expr", "rail_a != tokens"),
    },
    {
        "law": "F750.literal_inverse",
        "path": AUDIT_INPUT_PATHS[2],
        "function": "enforcement_lineage_selector",
        "locator": ("expr", "restored == before"),
    },
    {
        "law": "F750.clean_postimage",
        "path": AUDIT_INPUT_PATHS[2],
        "function": "enforcement_lineage_selector",
        "locator": ("expr", "not dirty"),
    },
    {
        "law": "F758.synchronous_composition",
        "path": AUDIT_INPUT_PATHS[3],
        "function": "multisource_enforcement_lineage_selector",
        "locator": ("dict", "conditions", "synchronous_composition"),
    },
    {
        "law": "F758.token_rail_return",
        "path": AUDIT_INPUT_PATHS[3],
        "function": "multisource_enforcement_lineage_selector",
        "locator": ("dict", "conditions", "token_rail_return"),
    },
    {
        "law": "F758.literal_inverse",
        "path": AUDIT_INPUT_PATHS[3],
        "function": "multisource_enforcement_lineage_selector",
        "locator": ("dict", "conditions", "literal_inverse"),
    },
    {
        "law": "F758.clean_postimage",
        "path": AUDIT_INPUT_PATHS[3],
        "function": "multisource_enforcement_lineage_selector",
        "locator": ("dict", "conditions", "clean_postimage"),
    },
    {
        "law": "F781.C745_output_tag_REFUSED",
        "path": AUDIT_INPUT_PATHS[4],
        "function": "apply_cell_word",
        "locator": (
            "expr", "all(tag == 'REFUSED' for tag in tags)"
        ),
    },
    {
        "law": "F781.C745_Q_refuse_asserted",
        "path": AUDIT_INPUT_PATHS[4],
        "function": "apply_cell_word",
        "locator": ("expr", "all(q_refuse)"),
    },
    {
        "law": "F781.C745_Q_in_cleared",
        "path": AUDIT_INPUT_PATHS[4],
        "function": "apply_cell_word",
        "locator": ("expr", "not any(q_in)"),
    },
    {
        "law": "F781.C745_Q_accept_cleared",
        "path": AUDIT_INPUT_PATHS[4],
        "function": "apply_cell_word",
        "locator": ("expr", "not any(q_accept)"),
    },
    {
        "law": "F781.C745_persistent_cell_exact",
        "path": AUDIT_INPUT_PATHS[4],
        "function": "apply_cell_word",
        "locator": ("expr", "after_persistent == before_persistent"),
    },
    {
        "law": "F781.tensor_guard_output_tag_REFUSED",
        "path": AUDIT_INPUT_PATHS[4],
        "function": "tensor_landed_guard_refuses",
        "locator": (
            "expr",
            "all(C745.output_tag(event) == 'REFUSED' for event in events)",
        ),
    },
    {
        "law": "F781.tensor_guard_persistent_exact",
        "path": AUDIT_INPUT_PATHS[4],
        "function": "tensor_landed_guard_refuses",
        "locator": (
            "expr", "persistent_cells(events) == guard_persistent"
        ),
    },
    {
        "law": "F781.refused_or_rolled_back",
        "path": AUDIT_INPUT_PATHS[4],
        "function": "run_one_attack",
        "locator": ("return", "refused_or_rolled_back"),
    },
    {
        "law": "F781.record_byte_identical_after",
        "path": AUDIT_INPUT_PATHS[4],
        "function": "run_one_attack",
        "locator": ("assign", "record_exact"),
    },
    {
        "law": "F781.syndrome_receipt_left",
        "path": AUDIT_INPUT_PATHS[4],
        "function": "run_one_attack",
        "locator": ("assign", "receipt_present"),
    },
    {
        "law": "F781.checkpoint_engagement",
        "path": AUDIT_INPUT_PATHS[4],
        "function": "non_interference",
        "locator": ("expr", "decoded and not engaged"),
    },
)


def expression_shape(source: str) -> str:
    return ast.dump(
        ast.parse(source, mode="eval").body, include_attributes=False
    )


def assignment_value(
    function: ast.FunctionDef, name: str
) -> ast.expr:
    matches: list[ast.expr] = []
    for node in ast.walk(function):
        if (
            isinstance(node, ast.Assign)
            and len(node.targets) == 1
            and isinstance(node.targets[0], ast.Name)
            and node.targets[0].id == name
        ):
            matches.append(node.value)
    if len(matches) != 1:
        raise AssertionError(("assignment", function.name, name, len(matches)))
    return matches[0]


def dict_value(node: ast.AST, key: str) -> ast.expr:
    dictionaries = [
        child for child in ast.walk(node) if isinstance(child, ast.Dict)
    ]
    matches: list[ast.expr] = []
    for dictionary in dictionaries:
        for raw_key, raw_value in zip(dictionary.keys, dictionary.values):
            if (
                isinstance(raw_key, ast.Constant)
                and raw_key.value == key
            ):
                matches.append(raw_value)
    if len(matches) != 1:
        raise AssertionError(("dictionary key", key, len(matches)))
    return matches[0]


def locate_law_node(
    function: ast.FunctionDef, locator: tuple[str, ...]
) -> ast.AST:
    kind = locator[0]
    if kind == "expr":
        wanted = expression_shape(locator[1])
        matches = [
            node
            for node in ast.walk(function)
            if isinstance(node, ast.expr)
            and ast.dump(node, include_attributes=False) == wanted
        ]
        if len(matches) != 1:
            raise AssertionError(
                ("expression", function.name, locator[1], len(matches))
            )
        return matches[0]
    if kind == "dict":
        return dict_value(assignment_value(function, locator[1]), locator[2])
    if kind == "assign":
        return assignment_value(function, locator[1])
    if kind == "return":
        returns = [
            node.value
            for node in ast.walk(function)
            if isinstance(node, ast.Return)
            and isinstance(node.value, ast.Dict)
        ]
        if len(returns) != 1:
            raise AssertionError(("return dictionary", function.name))
        return dict_value(returns[0], locator[1])
    if kind == "guard":
        guards = [
            node
            for node in ast.walk(function)
            if isinstance(node, ast.If)
            and ast.unparse(node.test) == "a[station]"
        ]
        if len(guards) != 2:
            raise AssertionError(("active guards", function.name, len(guards)))
        return sorted(guards, key=lambda row: row.lineno)[
            0 if locator[1] == "forward" else 1
        ].test
    raise AssertionError(("unknown locator", locator))


def parents_for(root: ast.AST) -> dict[ast.AST, ast.AST]:
    return {
        child: parent
        for parent in ast.walk(root)
        for child in ast.iter_child_nodes(parent)
    }


CONTROL_NODES = (
    ast.For,
    ast.While,
    ast.If,
    ast.IfExp,
    ast.comprehension,
)
LOOP_NODES = (
    ast.For,
    ast.While,
    ast.comprehension,
)


def control_ancestors(
    root: ast.AST, node: ast.AST
) -> tuple[dict[str, object], ...]:
    parents = parents_for(root)
    controls = []
    cursor = node
    while cursor in parents:
        cursor = parents[cursor]
        if not isinstance(cursor, CONTROL_NODES):
            continue
        if isinstance(cursor, ast.comprehension):
            description = "comprehension:" + ast.unparse(cursor.iter)
            line = getattr(cursor.target, "lineno", -1)
        elif isinstance(cursor, (ast.For, ast.While)):
            description = ast.unparse(cursor).splitlines()[0]
            line = cursor.lineno
        elif isinstance(cursor, ast.If):
            description = "if " + ast.unparse(cursor.test)
            line = cursor.lineno
        else:
            description = "ifexp " + ast.unparse(cursor.test)
            line = cursor.lineno
        controls.append(
            {
                "type": type(cursor).__name__,
                "line": line,
                "description": description,
            }
        )
    return tuple(reversed(controls))


def call_path(call: ast.Call) -> str:
    parts = []
    cursor: ast.AST = call.func
    while isinstance(cursor, ast.Attribute):
        parts.append(cursor.attr)
        cursor = cursor.value
    if isinstance(cursor, ast.Name):
        parts.append(cursor.id)
    return ".".join(reversed(parts))


def calls_in(node: ast.AST) -> tuple[ast.Call, ...]:
    return tuple(child for child in ast.walk(node) if isinstance(child, ast.Call))


def classify_law_site(
    path: str,
    function: ast.FunctionDef,
    node: ast.AST,
    functions: dict[str, ast.FunctionDef],
) -> tuple[str, str, bool]:
    """Return cadence, structural reason, and boundary-case flag."""

    name = function.name
    calls = tuple(call_path(call) for call in calls_in(function))
    line = getattr(node, "lineno", -1)
    earlier_calls = tuple(
        call_path(call)
        for call in calls_in(function)
        if getattr(call, "lineno", 10**9) < line
    )
    controls = control_ancestors(function, node)
    if name == "apply_controller_step":
        macro_calls = [
            call for call in calls_in(function)
            if call_path(call).endswith("mapped_macro")
        ]
        structurally_exact = (
            len(macro_calls) == 2
            and any(
                item["type"] == "For" and "station in order" in item["description"]
                for item in controls
            )
        )
        if not structurally_exact:
            raise AssertionError(("K719 macro guard placement", controls))
        return (
            "program_macro_completion",
            "active-A guard is the per-station gate on mapped_macro in Q",
            True,
        )
    if name in {
        "enforcement_lineage_selector",
        "multisource_enforcement_lineage_selector",
    }:
        if not any(call.endswith("run_orbit") for call in earlier_calls):
            raise AssertionError(("orbit domination", name, line, earlier_calls))
        return (
            "orbit_return_boundary",
            "predicate is evaluated only after a dominating K.run_orbit return",
            name == "multisource_enforcement_lineage_selector",
        )
    if name in {"apply_cell_word", "tensor_landed_guard_refuses"}:
        if not any(call == "C745.apply_word" for call in earlier_calls):
            raise AssertionError(("C745 word domination", name, earlier_calls))
        return (
            "program_macro_completion",
            "aggregate refusal predicate follows completed C745 word applications",
            True,
        )
    if name == "run_one_attack":
        compiled = [
            call for call in calls_in(function)
            if call_path(call) == "apply_compiled_word"
        ]
        main_source = ast.unparse(functions["main"])
        scheduled = (
            len(compiled) == 2
            and "syndrome_word" in ast.unparse(compiled[0])
            and "restore_word" in ast.unparse(compiled[1])
            and "every tested post-engagement station boundary" in main_source
        )
        if not scheduled:
            raise AssertionError(("Cycle781 schedule", len(compiled)))
        return (
            "H_station_boundary",
            "factored battery predicate follows syndrome+restore at the explicitly declared post-H boundary",
            True,
        )
    if name == "non_interference":
        in_station_loop = any(
            item["type"] == "For"
            and "range(C719.CONTROLLER_STATIONS)" in item["description"]
            for item in controls
        )
        if not in_station_loop or calls.count("C719.apply_fast_int") < 2:
            raise AssertionError(("Cycle781 engagement placement", controls))
        return (
            "H_station_boundary",
            "decoded engagement test is inside the one-H-per-step station loop",
            False,
        )
    raise AssertionError(("unclassified law function", path, name))


def safe_primary_value(
    node: ast.AST, environment: dict[str, object]
) -> object:
    if isinstance(node, ast.Constant):
        return node.value
    if isinstance(node, ast.Tuple):
        return tuple(safe_primary_value(item, environment) for item in node.elts)
    if isinstance(node, ast.List):
        return [safe_primary_value(item, environment) for item in node.elts]
    if isinstance(node, ast.Dict):
        return {
            safe_primary_value(key, environment):
                safe_primary_value(value, environment)
            for key, value in zip(node.keys, node.values)
        }
    if isinstance(node, ast.Name) and node.id in environment:
        return environment[node.id]
    if isinstance(node, ast.Subscript) and isinstance(node.value, ast.Name):
        collection = environment[node.value.id]
        index = safe_primary_value(node.slice, environment)
        return collection[index]  # type: ignore[index]
    raise ValueError(("nonliteral primary expression", ast.dump(node)))


def primary_law_specs(primary_tree: ast.Module) -> tuple[dict[str, object], ...]:
    assignments: dict[str, ast.AST] = {}
    for node in primary_tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    assignments[target.id] = node.value
    audit_inputs = safe_primary_value(assignments["AUDIT_INPUT_PATHS"], {})
    environment = {"AUDIT_INPUT_PATHS": audit_inputs}
    specs = safe_primary_value(assignments["LAW_SPECS"], environment)
    if not isinstance(specs, tuple) or not all(
        isinstance(row, dict) for row in specs
    ):
        raise AssertionError("Cycle799 LAW_SPECS is not a literal tuple")
    return specs  # type: ignore[return-value]


def callsites_for_helper(
    helper: str,
    surfaces: dict[str, ast.Module],
) -> tuple[dict[str, object], ...]:
    rows = []
    for path, tree in surfaces.items():
        for caller, function in top_functions(tree).items():
            parents = parents_for(function)
            for call in calls_in(function):
                if call_path(call).split(".")[-1] != helper:
                    continue
                cursor: ast.AST = call
                loop_depth = 0
                controls = []
                while cursor in parents:
                    cursor = parents[cursor]
                    if isinstance(cursor, LOOP_NODES):
                        loop_depth += 1
                    if isinstance(cursor, CONTROL_NODES):
                        controls.append(type(cursor).__name__)
                rows.append(
                    {
                        "path": path,
                        "caller": caller,
                        "line": call.lineno,
                        "call": call_path(call),
                        "loop_depth": loop_depth,
                        "controls": tuple(reversed(controls)),
                    }
                )
    return tuple(sorted(rows, key=lambda row: (
        str(row["path"]), str(row["caller"]), int(row["line"])
    )))


def classification_audit(
    surfaces: dict[str, ast.Module],
) -> dict[str, object]:
    primary = primary_law_specs(surfaces[AUDIT_INPUT_PATHS[6]])
    primary_by_law = {
        str(row["law"]): str(row["cadence"]) for row in primary
    }
    functions = {
        path: top_functions(tree) for path, tree in surfaces.items()
    }
    rows = []
    failures = []
    for target in LAW_TARGETS:
        function = functions[target["path"]].get(str(target["function"]))
        if function is None:
            failures.append({
                "law": target["law"],
                "finding": "named function is absent",
            })
            continue
        try:
            node = locate_law_node(function, target["locator"])
            cadence, reason, boundary = classify_law_site(
                str(target["path"]),
                function,
                node,
                functions[AUDIT_INPUT_PATHS[4]],
            )
        except Exception as exc:
            failures.append({
                "law": target["law"],
                "finding": repr(exc),
            })
            continue
        primary_cadence = primary_by_law.get(str(target["law"]))
        row = {
            "law": target["law"],
            "path": target["path"],
            "function": target["function"],
            "site_line": getattr(node, "lineno", -1),
            "site_end_line": getattr(node, "end_lineno", -1),
            "site": ast.unparse(node),
            "loop_nesting": control_ancestors(function, node),
            "derived_cadence": cadence,
            "primary_cadence": primary_cadence,
            "agreement": cadence == primary_cadence,
            "basis": reason,
            "boundary_case": boundary,
        }
        rows.append(row)
        if not row["agreement"]:
            failures.append({
                "law": target["law"],
                "finding": "CADENCE_MISCLASSIFICATION",
                "primary": primary_cadence,
                "independent": cadence,
                "site": f"{target['path']}:{row['site_line']}",
            })

    laws_by_function: dict[str, list[str]] = defaultdict(list)
    for row in rows:
        laws_by_function[str(row["function"])].append(str(row["law"]))
    boundary_helpers = []
    for helper, laws in sorted(laws_by_function.items()):
        callsites = callsites_for_helper(helper, {
            path: surfaces[path] for path in AUDIT_INPUT_PATHS[:5]
        })
        depths = tuple(sorted({int(row["loop_depth"]) for row in callsites}))
        if len(depths) > 1:
            boundary_helpers.append({
                "helper": helper,
                "laws": tuple(laws),
                "observed_direct_call_loop_depths": depths,
                "callsites": callsites,
                "defensibility": (
                    "cadence follows the helper's inner semantic boundary; "
                    "caller nesting changes repetition count, not boundary type"
                ),
            })

    counts = Counter(str(row["derived_cadence"]) for row in rows)
    for cadence in CADENCES:
        counts.setdefault(cadence, 0)
    primary_counts = Counter(primary_by_law.values())
    for cadence in CADENCES:
        primary_counts.setdefault(cadence, 0)
    flips = tuple(
        row for row in rows if not bool(row["agreement"])
    )
    boundary_rows = tuple(
        row for row in rows if bool(row["boundary_case"])
    )
    return {
        "primary_rows": len(primary),
        "independent_rows": len(rows),
        "rows": tuple(rows),
        "extraction_failures": tuple(failures),
        "cadence_flips": flips,
        "boundary_law_rows": boundary_rows,
        "primary_counts": dict(sorted(primary_counts.items())),
        "derived_counts": dict(sorted(counts.items())),
        "boundary_helpers_called_at_multiple_loop_depths":
            tuple(boundary_helpers),
        "table_agreement": (
            len(primary) == len(LAW_TARGETS) == len(rows) == 21
            and set(primary_by_law) == {
                str(row["law"]) for row in rows
            }
            and not failures
            and not flips
        ),
    }


def raw_conditional_inventory(
    surfaces: dict[str, ast.Module],
) -> dict[str, dict[str, int]]:
    """Broad AST sweep; semantic dispositions are intentionally conservative."""

    result = {}
    for path in AUDIT_INPUT_PATHS[:5]:
        tree = surfaces[path]
        result[path] = {
            "statement_If": sum(
                isinstance(node, ast.If) for node in ast.walk(tree)
            ),
            "expression_IfExp": sum(
                isinstance(node, ast.IfExp) for node in ast.walk(tree)
            ),
            "comprehension_filters": sum(
                len(node.ifs)
                for node in ast.walk(tree)
                if isinstance(node, ast.comprehension)
            ),
            "assertions": sum(
                isinstance(node, ast.Assert) for node in ast.walk(tree)
            ),
            "boolean_compositions": sum(
                isinstance(node, ast.BoolOp) for node in ast.walk(tree)
            ),
            "comparisons": sum(
                isinstance(node, ast.Compare) for node in ast.walk(tree)
            ),
        }
    return result


def appended_failure(if_node: ast.If) -> str | None:
    values = []
    for node in ast.walk(ast.Module(body=if_node.body, type_ignores=[])):
        if (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Attribute)
            and isinstance(node.func.value, ast.Name)
            and node.func.value.id == "case_failed"
            and node.func.attr == "append"
            and len(node.args) == 1
            and isinstance(node.args[0], ast.Constant)
            and isinstance(node.args[0].value, str)
        ):
            values.append(node.args[0].value)
    if len(values) == 1:
        return values[0]
    return None


def completeness_hunt(
    surfaces: dict[str, ast.Module],
    classification: dict[str, object],
) -> dict[str, object]:
    """Harvest conservative omitted dynamical tests, excluding report checks."""

    function = top_functions(surfaces[AUDIT_INPUT_PATHS[1]])[
        "invariant_full_orbit_certificate"
    ]
    expected = {
        "pairwise_distances",
        "common_translation",
        "ownership",
        "trace",
        "synchronous_composition",
        "direct_vs_K_run_orbit",
        "register_return",
        "literal_reverse",
    }
    harvested = []
    for node in ast.walk(function):
        if not isinstance(node, ast.If):
            continue
        failure_name = appended_failure(node)
        if failure_name not in expected:
            continue
        controls = control_ancestors(function, node.test)
        in_h_loop = any(
            row["type"] == "For"
            and "range(RING_STATIONS)" in str(row["description"])
            for row in controls
        )
        cadence = (
            "H_station_boundary"
            if in_h_loop
            else "orbit_return_boundary"
        )
        harvested.append({
            "law": "M736." + failure_name,
            "path": AUDIT_INPUT_PATHS[1],
            "function": function.name,
            "site_line": node.lineno,
            "site": ast.unparse(node.test),
            "loop_nesting": controls,
            "evaluation_cadence": cadence,
            "finding": (
                "MISSED_LAW: explicit dynamical failure branch in the "
                "claimed Cycle736 surface is absent from Cycle799 LAW_SPECS"
            ),
        })
    harvested = sorted(harvested, key=lambda row: int(row["site_line"]))
    names = {str(row["law"]).split(".", 1)[1] for row in harvested}
    if names != expected:
        raise AssertionError(
            ("Cycle736 conservative harvest", sorted(names), sorted(expected))
        )

    primary_laws = {
        str(row["law"]) for row in classification["rows"]
    }
    missed = tuple(
        row for row in harvested if row["law"] not in primary_laws
    )
    missing_counts = Counter(
        str(row["evaluation_cadence"]) for row in missed
    )
    expanded_counts = Counter(
        {
            cadence: int(classification["derived_counts"].get(cadence, 0))
            for cadence in CADENCES
        }
    )
    expanded_counts.update(missing_counts)
    covered_cadences = tuple(
        cadence for cadence in CADENCES if expanded_counts[cadence]
    )
    verdict = (
        "CADENCE_PREFERRED"
        if len(covered_cadences) == 1
        else "NO_UNIFORM_PREFERENCE"
    )
    return {
        "conservative_scope": (
            "explicit Cycle736 invariant_full_orbit_certificate branches "
            "that append named dynamical failures; excludes constructors, "
            "fixtures, report assertions, aggregate all(...) gates, and "
            "empty-domain bool(events) preconditions"
        ),
        "raw_all_surface_AST_inventory":
            raw_conditional_inventory(surfaces),
        "primary_omits_Cycle736_from_literal_inputs":
            AUDIT_INPUT_PATHS[1] not in {
                str(row["path"]) for row in classification["rows"]
            },
        "harvested_candidates": tuple(harvested),
        "missed_laws": missed,
        "missed_count": len(missed),
        "missed_count_is_conservative_lower_bound": True,
        "missed_counts_by_cadence": dict(sorted(missing_counts.items())),
        "expanded_counts": dict(sorted(expanded_counts.items())),
        "expanded_verdict": verdict,
        "sweep_complete": len(harvested) == len(expected),
        "exhaustive_semantic_missed_law_count_claimed": False,
        "primary_complete_at_conservative_scope": not missed,
    }


def bits_to_int(bits: Iterable[int]) -> int:
    return sum(int(value) << index for index, value in enumerate(bits))


def compile_word(
    word: tuple[object, ...],
) -> tuple[tuple[int, ...], ...]:
    kinds = {"X": 0, "CNOT": 1, "TOF": 2}
    compiled = []
    for gate in word:
        kind = getattr(gate, "kind")
        if kind not in kinds:
            raise ValueError(("nonclassical monitored gate", gate))
        compiled.append((kinds[kind], *getattr(gate, "wires")))
    return tuple(compiled)


def apply_fast(value: int, word: tuple[tuple[int, ...], ...]) -> int:
    output = value
    for gate in word:
        if gate[0] == 0:
            output ^= 1 << gate[1]
        elif gate[0] == 1:
            output ^= ((output >> gate[1]) & 1) << gate[2]
        elif gate[0] == 2:
            enabled = (
                ((output >> gate[1]) & 1)
                & ((output >> gate[2]) & 1)
            )
            output ^= enabled << gate[3]
        else:
            raise AssertionError(("compiled gate kind", gate))
    return output


def clean_mask(bank_count: int) -> int:
    mask = 1 << K719.R3.X.SOURCE_POINTER
    bank_wires = (
        K719.A.POINTER,
        K719.A.U_TO_V,
        K719.A.V_TO_U,
        K719.A.DIRECTION_OK,
        *K719.A.FRESH,
        *K719.A.ZERO_WORK,
        K719.A.TOKEN_OK,
    )
    for base in K719.M.R12.BANK_BASES[:bank_count]:
        for wire in bank_wires:
            mask |= 1 << (base + wire)
    for base in K719.M.R12.LINK_BASES[:bank_count - 1]:
        for wire in range(K719.B.LINK_WIDTH):
            mask |= 1 << (base + wire)
    return mask


CLEAN_MASK = clean_mask(FIXTURE_BANKS)


def is_clean(state: int) -> bool:
    return state & CLEAN_MASK == 0


def rail_step(
    a_tokens: tuple[int, ...],
    b_tokens: tuple[int, ...],
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    stations = len(a_tokens)
    a = list(a_tokens)
    b = list(b_tokens)
    for station in range(stations):
        a[station], b[station] = b[station], a[station]
    for station in range(stations):
        target = (station + 1) % stations
        b[station], a[target] = a[target], b[station]
    return tuple(a), tuple(b)


def independent_rail_orbit(
    positions: tuple[int, ...], stations: int
) -> dict[str, object]:
    a = tuple(int(station in positions) for station in range(stations))
    initial = a
    b = (0,) * stations
    trace = []
    for _step in range(stations):
        before = tuple(
            station for station, value in enumerate(a) if value
        )
        a, b = rail_step(a, b)
        after = tuple(
            station for station, value in enumerate(a) if value
        )
        trace.append((before, after, sum(b)))
    return {
        "initial": initial,
        "a": a,
        "b": b,
        "trace": tuple(trace),
    }


def expected_trace(
    positions: tuple[int, ...],
) -> tuple[tuple[tuple[int, ...], tuple[int, ...], int], ...]:
    return tuple(
        (
            tuple(sorted(
                (position + step) % RING_STATIONS
                for position in positions
            )),
            tuple(sorted(
                (position + step + 1) % RING_STATIONS
                for position in positions
            )),
            0,
        )
        for step in range(RING_STATIONS)
    )


def build_monitor_family() -> tuple[
    dict[tuple[int, tuple[int, ...]], dict[str, object]],
    dict[str, object],
]:
    """Build the k=2 family without executing either blocklisted primary."""

    census = M736.configuration_census()
    positions_rows = tuple(
        M736.occupied_sites(config)
        for config in census["configurations"]
        if sum(config) == 2
    )
    position_members = frozenset(positions_rows)
    fixtures = F750.k_epoch_fixtures(FIXTURE_BANKS)
    program = fixtures[0][2]
    words = {
        positions: M736.synchronous_composition_word(program, positions)
        for positions in positions_rows
    }
    compiled = {
        positions: compile_word(word)
        for positions, word in words.items()
    }
    rails = {
        positions: independent_rail_orbit(positions, len(program))
        for positions in positions_rows
    }
    rows: dict[
        tuple[int, tuple[int, ...]], dict[str, object]
    ] = {}
    for event, direction, fixture_program, before, _expected in fixtures:
        if fixture_program != program:
            raise AssertionError("fixture program drift")
        before_int = bits_to_int(before)
        for positions in positions_rows:
            after = apply_fast(before_int, compiled[positions])
            restored = apply_fast(after, tuple(reversed(compiled[positions])))
            rail = rails[positions]
            config = tuple(
                int(station in positions)
                for station in range(RING_STATIONS)
            )
            conditions = {
                "synchronous_composition": True,
                "token_rail_return": (
                    rail["a"] == rail["initial"]
                    and not any(rail["b"])
                ),
                "literal_inverse": (
                    restored == before_int
                    and rail["a"] == rail["initial"]
                    and not any(rail["b"])
                ),
                "census_membership": positions in position_members,
                "pairwise_separation":
                    M736.is_pairwise_separated(config),
                "synchronization":
                    rail["trace"] == expected_trace(positions),
            }
            key = (event, positions)
            rows[key] = {
                "key": key,
                "event": event,
                "direction": direction,
                "program": program,
                "before": before,
                "positions": positions,
                "compiled_word": compiled[positions],
                "after": after,
                "conditions": conditions,
            }

    crosscheck_keys = (
        (0, (0, 2)),
        (1, (0, 3)),
        (2, (0, 4)),
        (3, (1, 10)),
        (3, (0, 7)),
    )
    crosscheck_failures = []
    for key in crosscheck_keys:
        row = rows[key]
        direct, rail_a, rail_b, trace = K719.run_orbit(
            row["before"],
            row["program"],
            token_positions=row["positions"],
        )
        expected_a = tuple(
            int(station in row["positions"])
            for station in range(len(row["program"]))
        )
        if (
            bits_to_int(direct) != row["after"]
            or rail_a != expected_a
            or any(rail_b)
            or trace != expected_trace(row["positions"])
        ):
            crosscheck_failures.append(key)
    control = {
        "census_agreement": census["agreement"],
        "k2_configurations": len(positions_rows),
        "fixture_count": len(fixtures),
        "family_keys": len(rows),
        "all_static_conditions_pass": all(
            all(row["conditions"].values()) for row in rows.values()
        ),
        "initial_clean_count": sum(
            is_clean(int(row["after"])) for row in rows.values()
        ),
        "landed_run_orbit_crosscheck_keys": crosscheck_keys,
        "landed_run_orbit_crosscheck_failures":
            tuple(crosscheck_failures),
    }
    control["pass"] = (
        control["census_agreement"]
        and control["k2_configurations"] == 44
        and control["fixture_count"] == 4
        and control["family_keys"] == 176
        and control["all_static_conditions_pass"]
        and control["initial_clean_count"] == 0
        and not crosscheck_failures
    )
    return rows, control


def monitor_orbit_returns(
    rows: dict[tuple[int, tuple[int, ...]], dict[str, object]],
    *,
    reverse_order: bool,
) -> dict[str, object]:
    """Time-major, uniform-cutoff scan independently reconstructed from gates."""

    ordered = tuple(sorted(rows, reverse=reverse_order))
    state = {key: int(rows[key]["after"]) for key in ordered}
    seen = {key: {state[key]: 0} for key in ordered}
    first = {key: None for key in ordered}
    cycles = {key: None for key in ordered}
    evolving = set(ordered)
    for tick in range(1, MONITOR_CUTOFF + 1):
        retired = []
        for key in ordered:
            if key not in evolving:
                continue
            state[key] = apply_fast(
                state[key], rows[key]["compiled_word"]
            )
            passed = (
                all(rows[key]["conditions"].values())
                and is_clean(state[key])
            )
            if passed and first[key] is None:
                first[key] = tick
                seen[key].clear()
            elif first[key] is None:
                if state[key] in seen[key]:
                    entry = seen[key][state[key]]
                    cycles[key] = {
                        "entry": entry,
                        "return": tick,
                        "period": tick - entry,
                    }
                    retired.append(key)
                else:
                    seen[key][state[key]] = tick
        evolving.difference_update(retired)

    table = []
    for key in sorted(rows):
        if first[key] is not None:
            classification = "transient_accept"
        elif cycles[key] is not None:
            classification = "certified_cycle_refusal"
        else:
            classification = "open_refusal_through_cutoff"
        table.append({
            "key": key,
            "classification": classification,
            "acceptance_moment": first[key],
            "cycle": cycles[key],
            "final_state_sha256": sha256(
                state[key].to_bytes(
                    max(1, (state[key].bit_length() + 7) // 8), "little"
                )
            ).hexdigest(),
        })
    counts = Counter(str(row["classification"]) for row in table)
    acceptance_keys = tuple(sorted(
        (
            (
                key[0],
                key[1],
                int(moment),
            )
            for key, moment in first.items()
            if moment is not None
        ),
        key=lambda row: row[2],
    ))
    signature = {
        "table": tuple(table),
        "acceptance_keys": acceptance_keys,
        "counts": dict(sorted(counts.items())),
    }
    return {
        "table": tuple(table),
        "acceptance_keys": acceptance_keys,
        "classification_counts": dict(sorted(counts.items())),
        "signature_sha256": digest(signature),
    }


def cadence_probe(
    row: dict[str, object], maximum_orbit: int
) -> dict[str, object]:
    program = row["program"]
    stations = len(program)
    macro_words = tuple(
        compile_word(K719.mapped_macro(program[station]))
        for station in range(stations)
    )
    state = int(row["after"])
    positions = row["positions"]
    a = tuple(
        int(station in positions) for station in range(stations)
    )
    b = (0,) * stations
    first = {cadence: None for cadence in CADENCES}
    recomposition_failures = []

    def observe(cadence: str, coordinate: dict[str, object]) -> None:
        if (
            first[cadence] is None
            and all(row["conditions"].values())
            and is_clean(state)
        ):
            first[cadence] = dict(coordinate)

    absolute_h = 0
    for orbit in range(1, maximum_orbit + 1):
        orbit_input = state
        for step in range(1, stations + 1):
            absolute_h += 1
            live = tuple(
                station for station, value in enumerate(a) if value
            )
            for station in live:
                state = apply_fast(state, macro_words[station])
                observe(
                    "program_macro_completion",
                    {
                        "orbit": orbit,
                        "step": step,
                        "absolute_H": absolute_h,
                        "station": station,
                    },
                )
            coordinate = {
                "orbit": orbit,
                "step": step,
                "absolute_H": absolute_h,
            }
            observe(
                "Q_R1_R2_layer_boundary",
                {**coordinate, "layer": "Q"},
            )
            a, b = rail_step(a, b)
            observe(
                "Q_R1_R2_layer_boundary",
                {**coordinate, "layer": "R1"},
            )
            observe(
                "Q_R1_R2_layer_boundary",
                {**coordinate, "layer": "R2"},
            )
            observe("H_station_boundary", coordinate)
        expected = apply_fast(
            orbit_input, row["compiled_word"]
        )
        if state != expected:
            recomposition_failures.append(orbit)
        observe(
            "orbit_return_boundary",
            {
                "orbit": orbit,
                "step": stations,
                "absolute_H": absolute_h,
            },
        )
    return {
        "key": row["key"],
        "first": first,
        "orbit_recomposition_failures":
            tuple(recomposition_failures),
    }


def independent_consequence_timings(
    rows: dict[tuple[int, tuple[int, ...]], dict[str, object]],
    scan: dict[str, object],
) -> dict[str, object]:
    target_keys = tuple(
        (event, positions)
        for event, positions, _moment in scan["acceptance_keys"]
    )
    probes = {
        key: cadence_probe(
            rows[key],
            next(
                moment
                for event, positions, moment in scan["acceptance_keys"]
                if (event, positions) == key
            ),
        )
        for key in target_keys
    }
    timing_rows = tuple(
        {
            "cadence": cadence,
            "key": key,
            "orbit": probes[key]["first"][cadence]["orbit"],
            "step": probes[key]["first"][cadence]["step"],
            "absolute_H":
                probes[key]["first"][cadence]["absolute_H"],
        }
        for cadence in CADENCES
        for key in target_keys
    )
    expected = tuple(
        {
            "cadence": cadence,
            "key": key,
            "orbit": orbit,
            "step": (
                11
                if key == (3, (0, 7))
                or cadence == "orbit_return_boundary"
                else 10
            ),
            "absolute_H": (
                4081
                if key == (3, (0, 7))
                else 2772
                if cadence == "orbit_return_boundary"
                else 2771
            ),
        }
        for cadence in CADENCES
        for key, orbit in (
            ((3, (1, 10)), 252),
            ((3, (0, 7)), 371),
        )
    )
    recomposition_failures = tuple(
        (key, probe["orbit_recomposition_failures"])
        for key, probe in probes.items()
        if probe["orbit_recomposition_failures"]
    )
    return {
        "timing_rows": timing_rows,
        "expected_timing_rows": expected,
        "orbit_recomposition_failures": recomposition_failures,
        "pass": (
            scan["acceptance_keys"] == EXPECTED_ACCEPTANCE_KEYS
            and scan["classification_counts"] == EXPECTED_CLASSIFICATIONS
            and timing_rows == expected
            and not recomposition_failures
        ),
    }


def imported_modules_from_own_ast() -> tuple[str, ...]:
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    imported = []
    for node in tree.body:
        if isinstance(node, ast.Import):
            imported.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported.append(node.module)
    return tuple(imported)


def main() -> int:
    started = monotonic()
    before = source_snapshot()
    surfaces = {
        path: parse_surface(path) for path in AUDIT_INPUT_PATHS
    }

    classification = classification_audit(surfaces)
    classification_rerun = classification_audit(surfaces)
    emit("ATTACK_1_CLASSIFICATION_AUDIT")
    for row in classification["rows"]:
        emit("LAW_CADENCE_INDEPENDENT", row)
    for row in classification["boundary_law_rows"]:
        emit("BOUNDARY_CASE_LAW_SITE", {
            "law": row["law"],
            "function": row["function"],
            "site_line": row["site_line"],
            "loop_nesting": row["loop_nesting"],
            "derived_cadence": row["derived_cadence"],
            "primary_cadence": row["primary_cadence"],
            "defensibility": row["basis"],
        })
    for row in classification[
        "boundary_helpers_called_at_multiple_loop_depths"
    ]:
        emit("BOUNDARY_CASE_MULTILEVEL_HELPER", row)
    for finding in classification["extraction_failures"]:
        emit("CLASSIFICATION_FINDING_VERBATIM", finding)
    cert_a = certificate(
        "A",
        "classification_audit_21_laws",
        bool(classification["table_agreement"]),
        {
            "primary_counts": classification["primary_counts"],
            "derived_counts": classification["derived_counts"],
            "cadence_flips": classification["cadence_flips"],
            "extraction_failures": classification["extraction_failures"],
            "boundary_law_count": len(
                classification["boundary_law_rows"]
            ),
            "multilevel_helper_count": len(classification[
                "boundary_helpers_called_at_multiple_loop_depths"
            ]),
        },
    )

    completeness = completeness_hunt(surfaces, classification)
    completeness_rerun = completeness_hunt(surfaces, classification)
    emit("ATTACK_2_COMPLETENESS_HUNT", {
        "scope": completeness["conservative_scope"],
        "raw_all_surface_AST_inventory":
            completeness["raw_all_surface_AST_inventory"],
        "missed_count_is_conservative_lower_bound":
            completeness["missed_count_is_conservative_lower_bound"],
    })
    for finding in completeness["missed_laws"]:
        emit("MISSED_LAW_FINDING_VERBATIM", finding)
    cert_b = certificate(
        "B",
        "completeness_no_missed_laws",
        bool(completeness["primary_complete_at_conservative_scope"]),
        {
            "Cycle736_omitted_from_primary_inputs":
                completeness["primary_omits_Cycle736_from_literal_inputs"],
            "missed_count": completeness["missed_count"],
            "missed_count_is_conservative_lower_bound":
                completeness["missed_count_is_conservative_lower_bound"],
            "missed_counts_by_cadence":
                completeness["missed_counts_by_cadence"],
            "expanded_counts": completeness["expanded_counts"],
        },
    )

    verdict = str(completeness["expanded_verdict"])
    verdict_forced = (
        verdict == "NO_UNIFORM_PREFERENCE"
        and sum(
            int(value) > 0
            for value in completeness["expanded_counts"].values()
        ) > 1
    )
    cert_c = certificate(
        "C",
        "verdict_recount",
        verdict_forced,
        {
            "expanded_counts": completeness["expanded_counts"],
            "verdict": verdict,
            "uniform_cadence": None,
            "primary_verdict_survives":
                verdict == "NO_UNIFORM_PREFERENCE",
        },
    )

    rows, monitor_control = build_monitor_family()
    scan = monitor_orbit_returns(rows, reverse_order=False)
    scan_rerun = monitor_orbit_returns(rows, reverse_order=True)
    consequence = independent_consequence_timings(rows, scan)
    consequence_rerun = independent_consequence_timings(rows, scan_rerun)
    emit("ATTACK_4_CONSEQUENCE_TIMINGS")
    for row in consequence["timing_rows"]:
        emit("INDEPENDENT_FIRST_PASS_TIMING", row)
    timing_deterministic = consequence == consequence_rerun
    cert_d = certificate(
        "D",
        "independent_consequence_timings",
        bool(
            monitor_control["pass"]
            and consequence["pass"]
            and timing_deterministic
        ),
        {
            "acceptance_keys": scan["acceptance_keys"],
            "classification_counts": scan["classification_counts"],
            "uniform_discovery_cutoff": MONITOR_CUTOFF,
            "monitor_control": monitor_control,
            "timing_rows": consequence["timing_rows"],
            "recomposition_failures":
                consequence["orbit_recomposition_failures"],
            "deterministic": timing_deterministic,
        },
    )

    after = source_snapshot()
    loaded_blocklist = tuple(
        name for name in TEXT_ONLY_BLOCKLIST if name in sys.modules
    )
    own_imports = imported_modules_from_own_ast()
    imported_blocklist = tuple(
        name for name in TEXT_ONLY_BLOCKLIST if name in own_imports
    )
    anchors_exact = (
        {
            path: before[path]["sha256"] for path in AUDIT_INPUT_PATHS
        }
        == EXPECTED_SHA256
    )
    deterministic = (
        classification == classification_rerun
        and completeness == completeness_rerun
        and scan["signature_sha256"] == scan_rerun["signature_sha256"]
        and timing_deterministic
    )
    runtime = monotonic() - started
    projected_stdout = len(
        ("\n".join(OUTPUT_LINES) + "\n").encode("utf-8")
    ) + 16 * 1024
    controls_pass = (
        own_literal_inputs()
        and DECLARED_INPUT_PATHS == AUDIT_INPUT_PATHS
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and anchors_exact
        and before == after
        and not _BLOCKLIST_AT_IMPORT
        and not loaded_blocklist
        and not imported_blocklist
        and deterministic
        and runtime < AUDIT_TIMEOUT_SEC
        and projected_stdout < STDOUT_LIMIT_BYTES
    )
    cert_e = certificate(
        "E",
        "anchors_blocklist_determinism_bounds",
        controls_pass,
        {
            "AUDIT_INPUT_PATHS_literal": own_literal_inputs(),
            "anchors_exact": anchors_exact,
            "sha256": {
                path: before[path]["sha256"] for path in AUDIT_INPUT_PATHS
            },
            "sources_unchanged": before == after,
            "text_only_blocklist": TEXT_ONLY_BLOCKLIST,
            "blocklist_at_import": _BLOCKLIST_AT_IMPORT,
            "loaded_blocklist": loaded_blocklist,
            "directly_imported_blocklist": imported_blocklist,
            "deterministic": deterministic,
            "scan_signature": scan["signature_sha256"],
            "rerun_scan_signature": scan_rerun["signature_sha256"],
            "runtime_seconds": round(runtime, 6),
            "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
            "projected_stdout_bytes": projected_stdout,
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        },
    )

    cadence_flips = tuple(classification["cadence_flips"])
    missed = tuple(completeness["missed_laws"])
    verdict_flipped = verdict != "NO_UNIFORM_PREFERENCE"
    if verdict_flipped and (cadence_flips or missed):
        status = "REFUTED"
    elif cadence_flips or missed:
        status = "CENSUS_CORRECTED_VERDICT_CONFIRMED"
    else:
        status = "CONFIRMED"
    operational_pass = all(
        row["pass"] for row in (cert_a, cert_c, cert_d, cert_e)
    ) and completeness["sweep_complete"]
    report = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "status": status,
        "classification_table_agreement":
            classification["table_agreement"],
        "cadence_flips": cadence_flips,
        "primary_counts": classification["primary_counts"],
        "derived_21_law_counts": classification["derived_counts"],
        "missed_laws": tuple(row["law"] for row in missed),
        "expanded_counts": completeness["expanded_counts"],
        "verdict": verdict,
        "verdict_flipped": verdict_flipped,
        "timing_rows": consequence["timing_rows"],
        "certificates": {
            row["key"]: row["pass"]
            for row in (cert_a, cert_b, cert_c, cert_d, cert_e)
        },
        "primary_exact_census_pass": (
            cert_a["pass"] and cert_b["pass"]
        ),
        "operational_pass": operational_pass,
        "runtime_seconds": round(runtime, 6),
    }
    report["report_sha256"] = digest(report)
    emit("SUMMARY_JSON", report)
    emit("CYCLE799_CADENCE_INDEPENDENT_CHECK_" + status)
    output_bytes = len(("\n".join(OUTPUT_LINES) + "\n").encode("utf-8"))
    if output_bytes >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout bound", output_bytes))
    return 0 if operational_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
