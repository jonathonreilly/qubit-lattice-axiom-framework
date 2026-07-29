#!/usr/bin/env python3
"""Cycle 744 independent, adversarial receiver checker."""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/WEIGHT_RECEIVER_SHARPENING_CYCLE744_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18.py",
    "scripts/physical_contact_ternary_born_forcing_release_cycle317_2026_07_18.py",
)
BLOCKLIST = (
    "scripts/frontier_cycle744_weight_receiver_sharpening_2026_07_28.py",
)

import ast
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from time import perf_counter
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18 as B317
import physical_contact_ternary_born_forcing_release_cycle317_2026_07_18 as R317


PRIMARY_PATH = BLOCKLIST[0]
PRIMARY_MODULE = Path(PRIMARY_PATH).stem
PASS = 0
FAIL = 0

RECEIVER_TERMS = (
    "count",
    "frequenc",
    "exposure",
    "occurrence",
    "record",
    "row",
)

OWN_RELEASE_SIGNATURES = {
    "check": ("label", "condition", "detail"),
    "freshness_and_baseline_controls": ("note",),
    "line_has": ("path", "line_number", "fragment"),
    "main": (),
    "n1_controls": ("note",),
    "n2_controls": ("note",),
    "n3_controls": (),
    "n4_controls": ("note",),
    "n5_to_n8_and_broad_controls": ("note",),
    "science_cold_run": (),
    "section": ("body", "start", "end"),
}

OWN_COMPONENT_REQUIREMENTS = {
    "menu_program_identity": (
        "program eligibility",
        "cross-program pooling exclusion",
    ),
    "ordered_effect_identities": (
        "N-slot count-to-effect map",
        "fixed N",
        "fixed order",
    ),
    "typed_records": (
        "lawful occurrence evidence",
        "construction of n in N^N",
    ),
    "exposure_sampling_declaration": (
        "denominator",
        "per-effect eligibility",
        "units",
    ),
    "record_and_exposure_provenance": (
        "Record typing",
        "auditability",
        "apparatus-source identity",
    ),
    "coarse_graining_metadata": (
        "additive component-count rule",
    ),
    "same_effect_identity_metadata": (
        "repeated-presentation identity checks",
        "cross-program identity checks",
    ),
    "calibration_map": (
        "per-effect weights beyond an empirical simplex/comparator",
    ),
}

OWN_NECESSITY_SENTENCES = {
    "menu_program_identity": (
        "dropping it breaks program eligibility and permits cross-program pooling"
    ),
    "ordered_effect_identities": (
        "dropping it breaks the N-slot count-to-effect map and fixes neither N nor order"
    ),
    "typed_records": (
        "dropping it breaks lawful occurrence evidence and the construction of n in N^N"
    ),
    "exposure_sampling_declaration": (
        "dropping it breaks the denominator, per-effect eligibility, and units"
    ),
    "record_and_exposure_provenance": (
        "dropping it breaks Record typing, auditability, and apparatus-source identity"
    ),
    "coarse_graining_metadata": (
        "dropping it breaks the required additive component-count rule"
    ),
    "same_effect_identity_metadata": (
        "dropping it breaks repeated-presentation and cross-program identity checks"
    ),
    "calibration_map": (
        "dropping it leaves only an empirical simplex/comparator, not per-effect weights"
    ),
}

OWN_BOUNDARY = {
    "born_law_selected": False,
    "next_mechanism": "repeated-apparatus calibration bridge",
    "port_is_comparator_only": True,
    "receiver_hole_interface_frozen": True,
    "supplies": {
        "calibration_map": False,
        "coarse_graining_metadata": True,
        "exposure_and_provenance": True,
        "held_fixed_sigma_candidate_for_comparison": True,
        "ordered_effect_identities": True,
        "same_effect_identity_metadata": True,
        "selected_occurrence_law": False,
        "typed_declared_test_Record_rows": True,
    },
    "w6_closed": False,
}


def check(label: str, condition: bool, detail: object = "") -> bool:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", _compact(detail))
    else:
        FAIL += 1
        print("FAIL", label, "::", _compact(detail))
    return condition


def _compact(value: object, limit: int = 1600) -> str:
    try:
        rendered = json.dumps(value, sort_keys=True, default=str, separators=(",", ":"))
    except (TypeError, ValueError):
        rendered = repr(value)
    if len(rendered) > limit:
        rendered = rendered[: limit - 18] + "...[detail clipped]"
    return rendered


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _binding(module: ast.Module, name: str) -> ast.AST:
    matches = []
    for node in module.body:
        if (
            isinstance(node, ast.Assign)
            and any(isinstance(target, ast.Name) and target.id == name for target in node.targets)
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
        raise ValueError(f"expected one top-level binding for {name}, found {len(matches)}")
    return matches[0]


def _literal(module: ast.Module, name: str) -> object:
    return ast.literal_eval(_binding(module, name))


def _top_function(module: ast.Module, name: str) -> ast.FunctionDef:
    matches = [
        node
        for node in module.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == name
    ]
    if len(matches) != 1 or not isinstance(matches[0], ast.FunctionDef):
        raise ValueError(f"expected one synchronous top-level function {name}")
    return matches[0]


def _parameters(node: ast.FunctionDef) -> tuple[ast.arg, ...]:
    return tuple(node.args.posonlyargs + node.args.args + node.args.kwonlyargs)


def _public_signatures(module: ast.Module) -> dict[str, tuple[str, ...]]:
    inventory = {}
    for node in module.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and not node.name.startswith("_"):
            inventory[node.name] = tuple(argument.arg for argument in _parameters(node))
    return dict(sorted(inventory.items()))


def _public_annotations(
    module: ast.Module,
) -> dict[str, tuple[tuple[str, str], ...]]:
    inventory = {}
    for node in module.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and not node.name.startswith("_"):
            inventory[node.name] = tuple(
                (
                    argument.arg,
                    ast.unparse(argument.annotation)
                    if argument.annotation is not None
                    else "",
                )
                for argument in _parameters(node)
            )
    return dict(sorted(inventory.items()))


def _local_value(function: ast.FunctionDef, name: str) -> ast.AST:
    matches = []
    for node in ast.walk(function):
        if (
            isinstance(node, ast.Assign)
            and any(isinstance(target, ast.Name) and target.id == name for target in node.targets)
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
        raise ValueError(f"expected one local binding {function.name}.{name}")
    return matches[0]


def _comparison_literal(function: ast.FunctionDef, left_name: str) -> object:
    matches = []
    for node in ast.walk(function):
        if (
            isinstance(node, ast.Compare)
            and isinstance(node.left, ast.Name)
            and node.left.id == left_name
            and len(node.ops) == 1
            and isinstance(node.ops[0], ast.Eq)
            and len(node.comparators) == 1
        ):
            try:
                matches.append(ast.literal_eval(node.comparators[0]))
            except (ValueError, TypeError):
                pass
    if len(matches) != 1:
        raise ValueError(
            f"expected one literal equality for {function.name}.{left_name}"
        )
    return matches[0]


def extraction(
    primary_source: str,
    primary_tree: ast.Module,
    landed_sources: dict[str, str],
) -> dict[str, object]:
    audit_node = _binding(primary_tree, "AUDIT_INPUT_PATHS")
    pure_audit_tuple = isinstance(audit_node, ast.Tuple) and all(
        isinstance(item, ast.Constant) and type(item.value) is str
        for item in audit_node.elts
    )
    audit_inputs = ast.literal_eval(audit_node)

    port_function = _top_function(primary_tree, "comparator_flow_certificate")
    expected_per_profile = _comparison_literal(port_function, "censuses")
    expected_overall = _comparison_literal(port_function, "overall")

    construction = _top_function(primary_tree, "port_construction_certificate")
    malformed_node = _local_value(construction, "malformed")
    if not isinstance(malformed_node, ast.Tuple):
        raise ValueError("malformed witness declaration is not a tuple")
    refusal_labels = []
    for row in malformed_node.elts:
        if not isinstance(row, ast.Tuple) or len(row.elts) != 2:
            raise ValueError("malformed witness declaration changed shape")
        refusal_labels.append(ast.literal_eval(row.elts[0]))

    boundary_function = _top_function(primary_tree, "honest_boundary")
    returns = [
        node
        for node in boundary_function.body
        if isinstance(node, ast.Return) and node.value is not None
    ]
    if len(returns) != 1:
        raise ValueError("honest_boundary must have one direct return")
    boundary = ast.literal_eval(returns[0].value)

    extracted = {
        "audit_timeout": _literal(primary_tree, "AUDIT_TIMEOUT_SEC"),
        "note_path": _literal(primary_tree, "NOTE_PATH"),
        "audit_inputs": audit_inputs,
        "frozen_inventory": _literal(primary_tree, "FROZEN_PORT_INVENTORY"),
        "frozen_annotations": _literal(primary_tree, "FROZEN_PORT_ANNOTATIONS"),
        "frozen_type_arguments": _literal(
            primary_tree, "FROZEN_PORT_TYPE_ARGUMENTS"
        ),
        "held_form": _literal(primary_tree, "FROZEN_HELD_WEIGHT_FORM"),
        "bridge_signature": _literal(primary_tree, "REQUIRED_BRIDGE_SIGNATURE"),
        "component_necessity": _literal(primary_tree, "COMPONENT_NECESSITY"),
        "interface_stages": _literal(primary_tree, "INTERFACE_STAGES"),
        "declared_family": _literal(
            primary_tree, "DECLARED_APPARATUS_DATA_FAMILY"
        ),
        "declared_effect_ids": _literal(primary_tree, "DECLARED_EFFECT_IDS"),
        "expected_per_profile": expected_per_profile,
        "expected_overall": expected_overall,
        "refusal_labels": tuple(refusal_labels),
        "boundary": boundary,
        "primary_source": primary_source,
        "primary_tree": primary_tree,
        "landed_sources": landed_sources,
    }
    condition = (
        pure_audit_tuple
        and audit_inputs == AUDIT_INPUT_PATHS
        and extracted["audit_timeout"] == AUDIT_TIMEOUT_SEC
        and extracted["note_path"] == NOTE_PATH
        and len(extracted["frozen_inventory"]) == 20
        and len(extracted["bridge_signature"]) == 8
        and expected_overall == {"agreement": 6, "disagreement": 2}
        and len(refusal_labels) == 5
        and boundary == OWN_BOUNDARY
        and boundary["w6_closed"] is False
        and boundary["born_law_selected"] is False
    )
    check(
        "extraction: frozen census, weight form, interface, port census, and boundary",
        condition,
        {
            "audit_tuple_is_pure_literal": pure_audit_tuple,
            "census": len(extracted["frozen_inventory"]),
            "interface": len(extracted["bridge_signature"]),
            "port": expected_overall,
            "refusals": len(refusal_labels),
            "boundary": {
                "w6_closed": boundary.get("w6_closed"),
                "born_law_selected": boundary.get("born_law_selected"),
            },
        },
    )
    return extracted


def _call_name(node: ast.AST) -> str:
    try:
        return ast.unparse(node)
    except (ValueError, TypeError):
        return type(node).__name__


def _parameter_usage(function: ast.FunctionDef, parameter: ast.arg) -> dict[str, object]:
    parents = {
        child: parent
        for parent in ast.walk(function)
        for child in ast.iter_child_nodes(parent)
    }
    attributes = set()
    calls = set()
    for node in ast.walk(function):
        if not (
            isinstance(node, ast.Name)
            and isinstance(node.ctx, ast.Load)
            and node.id == parameter.arg
        ):
            continue
        current: ast.AST = node
        while isinstance(parents.get(current), ast.Attribute):
            current = parents[current]
            attributes.add(ast.unparse(current))
        parent = parents.get(current)
        if isinstance(parent, ast.Call):
            calls.add(_call_name(parent.func))
    annotation = (
        ast.unparse(parameter.annotation) if parameter.annotation is not None else ""
    )
    searchable = (parameter.arg, annotation, *sorted(attributes), *sorted(calls))
    forbidden = tuple(
        item
        for item in searchable
        if any(term in item.lower() for term in RECEIVER_TERMS)
    )
    return {
        "name": parameter.arg,
        "annotation": annotation,
        "attributes": tuple(sorted(attributes)),
        "calls": tuple(sorted(calls)),
        "forbidden": forbidden,
    }


def census_recount(
    extracted: dict[str, object],
    landed_trees: dict[str, ast.Module],
) -> dict[str, object]:
    bridge_tree = landed_trees[AUDIT_INPUT_PATHS[0]]
    release_tree = landed_trees[AUDIT_INPUT_PATHS[1]]
    bridge_signatures = _public_signatures(bridge_tree)
    release_signatures = _public_signatures(release_tree)
    bridge_annotations = _public_annotations(bridge_tree)

    usage_rows = {}
    for surface, tree in landed_trees.items():
        for node in tree.body:
            if isinstance(node, ast.FunctionDef) and not node.name.startswith("_"):
                for argument in _parameters(node):
                    key = f"{Path(surface).name}:{node.name}.{argument.arg}"
                    usage_rows[key] = _parameter_usage(node, argument)
    forbidden_usage = {
        key: row["forbidden"]
        for key, row in usage_rows.items()
        if row["forbidden"]
    }
    check_detail_sink = usage_rows[
        f"{Path(AUDIT_INPUT_PATHS[0]).name}:check.detail"
    ]
    no_variadics = all(
        node.args.vararg is None and node.args.kwarg is None
        for tree in landed_trees.values()
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and not node.name.startswith("_")
    )
    condition = (
        len(bridge_signatures) == 20
        and bridge_signatures
        == dict(sorted(extracted["frozen_inventory"].items()))
        and bridge_annotations
        == dict(sorted(extracted["frozen_annotations"].items()))
        and set(extracted["frozen_type_arguments"]) == set(bridge_signatures)
        and release_signatures == OWN_RELEASE_SIGNATURES
        and not forbidden_usage
        and check_detail_sink["calls"] == ("print",)
        and no_variadics
    )
    detail = {
        "bridge_public_signatures": bridge_signatures,
        "bridge_count": len(bridge_signatures),
        "release_public_signatures": release_signatures,
        "release_count": len(release_signatures),
        "parameter_arguments_audited": len(usage_rows),
        "forbidden_type_name_usage_hits": forbidden_usage,
        "check_detail_sink_calls": check_detail_sink["calls"],
    }
    check(
        "census recount: 20 frozen bridge ports and both landed surfaces audited",
        condition,
        detail,
    )
    return detail


def _direct_assignment(
    function: ast.FunctionDef, target_name: str
) -> ast.Assign | None:
    matches = [
        node
        for node in function.body
        if isinstance(node, ast.Assign)
        and len(node.targets) == 1
        and isinstance(node.targets[0], ast.Name)
        and node.targets[0].id == target_name
    ]
    return matches[0] if len(matches) == 1 else None


def weight_location_recount(
    extracted: dict[str, object],
    landed_trees: dict[str, ast.Module],
) -> dict[str, object]:
    source = extracted["landed_sources"][AUDIT_INPUT_PATHS[0]]
    tree = landed_trees[AUDIT_INPUT_PATHS[0]]
    outer = _top_function(tree, "mixed_projective_forcing_basis_controls")
    born_functions = [
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef) and node.name == "born_weight"
    ]
    born = born_functions[0] if len(born_functions) == 1 else None
    bloch_assignment = _direct_assignment(outer, "bloch")
    sigma_assignment = _direct_assignment(outer, "sigma")
    returned = (
        next(
            (node for node in born.body if isinstance(node, ast.Return)),
            None,
        )
        if born is not None
        else None
    )
    located = {
        "bloch": ast.get_source_segment(source, bloch_assignment)
        if bloch_assignment is not None
        else None,
        "sigma": ast.get_source_segment(source, sigma_assignment)
        if sigma_assignment is not None
        else None,
        "function": source.splitlines()[born.lineno - 1].strip()
        if born is not None
        else None,
        "return": ast.get_source_segment(source, returned).strip()
        if returned is not None
        else None,
    }
    vector = None
    dtype_is_float = False
    if (
        bloch_assignment is not None
        and isinstance(bloch_assignment.value, ast.Call)
        and bloch_assignment.value.args
    ):
        vector = ast.literal_eval(bloch_assignment.value.args[0])
        dtype_is_float = any(
            keyword.arg == "dtype"
            and isinstance(keyword.value, ast.Name)
            and keyword.value.id == "float"
            for keyword in bloch_assignment.value.keywords
        )
    expected_return_ast = ast.parse(
        "float(np.trace(sigma @ effect).real)", mode="eval"
    ).body
    return_shape_exact = (
        returned is not None
        and ast.dump(returned.value, include_attributes=False)
        == ast.dump(expected_return_ast, include_attributes=False)
    )
    stores = {
        name: sum(
            isinstance(node, ast.Name)
            and isinstance(node.ctx, ast.Store)
            and node.id == name
            for node in ast.walk(outer)
        )
        for name in ("bloch", "sigma")
    }
    condition = (
        born is not None
        and isinstance(born, ast.FunctionDef)
        and located == extracted["held_form"]
        and vector == (0.21, -0.32, 0.41)
        and dtype_is_float
        and return_shape_exact
        and tuple(argument.arg for argument in _parameters(born)) == ("effect",)
        and stores == {"bloch": 1, "sigma": 1}
    )
    detail = {
        "location": "mixed_projective_forcing_basis_controls.<locals>.born_weight",
        "form": located,
        "bloch_vector": vector,
        "byte_exact": located == extracted["held_form"],
        "store_counts": stores,
    }
    check("weight-location recount: exact Tr(sigma E) and Bloch vector", condition, detail)
    return detail


def interface_necessity_recount(extracted: dict[str, object]) -> dict[str, object]:
    signature = tuple(OWN_COMPONENT_REQUIREMENTS)
    universe = tuple(
        requirement
        for requirements in OWN_COMPONENT_REQUIREMENTS.values()
        for requirement in requirements
    )
    supports = {
        requirement: {
            component
            for component, requirements in OWN_COMPONENT_REQUIREMENTS.items()
            if requirement in requirements
        }
        for requirement in universe
    }
    broken_by_drop = {}
    for dropped in signature:
        remaining = set(signature) - {dropped}
        broken_by_drop[dropped] = tuple(
            requirement
            for requirement in universe
            if not (supports[requirement] & remaining)
        )
    expected_breaks = {
        component: requirements
        for component, requirements in OWN_COMPONENT_REQUIREMENTS.items()
    }
    condition = (
        signature == extracted["bridge_signature"]
        and broken_by_drop == expected_breaks
        and OWN_NECESSITY_SENTENCES == extracted["component_necessity"]
        and len(universe) == len(set(universe))
        and all(broken_by_drop.values())
    )
    detail = {
        "component_count": len(signature),
        "drop_rederivation": broken_by_drop,
        "primary_theorem_match": (
            OWN_NECESSITY_SENTENCES == extracted["component_necessity"]
        ),
        "stages": extracted["interface_stages"],
    }
    check(
        "interface necessity recount: every one-component drop breaks named requirements",
        condition,
        detail,
    )
    return detail


def _target_names(target: ast.AST) -> set[str]:
    if isinstance(target, ast.Name):
        return {target.id}
    if isinstance(target, (ast.Tuple, ast.List)):
        return set().union(*(_target_names(item) for item in target.elts))
    return set()


def _loaded_names(node: ast.AST | None) -> set[str]:
    if node is None:
        return set()
    return {
        item.id
        for item in ast.walk(node)
        if isinstance(item, ast.Name) and isinstance(item.ctx, ast.Load)
    }


def _tainted_names(function: ast.FunctionDef, seeds: Iterable[str]) -> set[str]:
    tainted = set(seeds)
    changed = True
    while changed:
        changed = False
        for node in ast.walk(function):
            targets: set[str] = set()
            value: ast.AST | None = None
            if isinstance(node, ast.Assign):
                targets = set().union(*(_target_names(item) for item in node.targets))
                value = node.value
            elif isinstance(node, ast.AnnAssign):
                targets = _target_names(node.target)
                value = node.value
            elif isinstance(node, ast.NamedExpr):
                targets = _target_names(node.target)
                value = node.value
            elif isinstance(node, (ast.For, ast.comprehension)):
                targets = _target_names(node.target)
                value = node.iter
            if targets and (_loaded_names(value) & tainted):
                additions = targets - tainted
                if additions:
                    tainted.update(additions)
                    changed = True
    return tainted


def _attribute_root(node: ast.AST) -> str | None:
    current = node
    while isinstance(current, (ast.Attribute, ast.Subscript)):
        current = current.value
    return current.id if isinstance(current, ast.Name) else None


def _assignment_targets(tree: ast.AST) -> tuple[ast.AST, ...]:
    result = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            result.extend(node.targets)
        elif isinstance(node, (ast.AnnAssign, ast.AugAssign, ast.NamedExpr)):
            result.append(node.target)
    return tuple(result)


def _comparator_firewall(primary_tree: ast.Module) -> dict[str, object]:
    relevant_seeds = {
        "receive_occurrence_records": {
            "identity",
            "ordered_effect_ids",
            "records",
            "exposure",
            "metadata",
        },
        "compare_empirical_to_landed": {"empirical"},
        "port_construction_certificate": set(),
        "comparator_flow_certificate": {"empirical"},
    }
    taint_rows = {}
    dangerous_tainted_targets = []
    dangerous_calls = []
    for name, seeds in relevant_seeds.items():
        function = _top_function(primary_tree, name)
        tainted = _tainted_names(function, seeds)
        taint_rows[name] = tuple(sorted(tainted))
        for target in _assignment_targets(function):
            for target_name in _target_names(target):
                if target_name in tainted and any(
                    token in target_name.lower()
                    for token in ("weight", "sigma", "bloch", "calibration")
                ):
                    dangerous_tainted_targets.append(f"{name}:{ast.unparse(target)}")
        for call in (
            node for node in ast.walk(function) if isinstance(node, ast.Call)
        ):
            call_name = _call_name(call.func)
            if any(
                token in call_name.lower()
                for token in ("weight", "calibrat", "_held_landed_candidate_values")
            ) and any(_loaded_names(argument) & tainted for argument in call.args):
                dangerous_calls.append(f"{name}:{ast.unparse(call)}")

    receiver = _top_function(primary_tree, "receive_occurrence_records")
    comparator = _top_function(primary_tree, "compare_empirical_to_landed")
    receiver_calls = {
        _call_name(node.func)
        for node in ast.walk(receiver)
        if isinstance(node, ast.Call)
    }
    comparator_attribute_writes = tuple(
        ast.unparse(target)
        for target in _assignment_targets(comparator)
        if isinstance(target, (ast.Attribute, ast.Subscript))
    )
    landed_writes = tuple(
        ast.unparse(target)
        for target in _assignment_targets(primary_tree)
        if _attribute_root(target) in {"B317", "R317"}
    )
    landed_setattrs = tuple(
        ast.unparse(node)
        for node in ast.walk(primary_tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "setattr"
        and node.args
        and isinstance(node.args[0], ast.Name)
        and node.args[0].id in {"B317", "R317"}
    )
    flow = _top_function(primary_tree, "comparator_flow_certificate")
    flow_taint = set(taint_rows["comparator_flow_certificate"])
    held_value_assignments = [
        node
        for node in ast.walk(flow)
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name) and target.id == "held_values"
            for target in node.targets
        )
    ]
    held_values_separate = (
        len(held_value_assignments) == 1
        and not (_loaded_names(held_value_assignments[0].value) & flow_taint)
        and "held_values" not in flow_taint
    )
    return {
        "tainted_names": taint_rows,
        "dangerous_tainted_targets": tuple(dangerous_tainted_targets),
        "dangerous_weight_calls": tuple(dangerous_calls),
        "receiver_calls_comparator": "compare_empirical_to_landed" in receiver_calls,
        "receiver_calls_held_weight": "_held_landed_candidate_values" in receiver_calls,
        "comparator_attribute_writes": comparator_attribute_writes,
        "landed_module_writes": landed_writes,
        "landed_setattrs": landed_setattrs,
        "held_values_separate_from_port_data": held_values_separate,
    }


def port_recount(extracted: dict[str, object]) -> dict[str, object]:
    environment = os.environ.copy()
    environment["PYTHONPATH"] = "scripts"
    blocklist_clean_before = PRIMARY_MODULE not in sys.modules
    try:
        completed = subprocess.run(
            [sys.executable, "-m", PRIMARY_MODULE],
            cwd=ROOT,
            env=environment,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=AUDIT_TIMEOUT_SEC,
            check=False,
        )
        output = completed.stdout
        returncode: int | str = completed.returncode
    except subprocess.TimeoutExpired as exc:
        raw = exc.stdout or ""
        output = raw.decode("utf-8", errors="replace") if isinstance(raw, bytes) else raw
        returncode = "timeout"

    comparator_payload = None
    final_boundary = None
    for line in output.splitlines():
        if line.startswith("DATA comparator_verdict_census "):
            try:
                comparator_payload = json.loads(
                    line.removeprefix("DATA comparator_verdict_census ")
                )
            except json.JSONDecodeError:
                comparator_payload = None
    for line in reversed(output.splitlines()):
        if line.startswith("{") and '"w6_closed"' in line:
            try:
                final_boundary = json.loads(line)
                break
            except json.JSONDecodeError:
                pass

    summary_matches = re.findall(
        r"^SUMMARY PASS\s+(\d+)\s+FAIL\s+(\d+)\s+RUNTIME_SEC\s+([0-9.]+)$",
        output,
        re.MULTILINE,
    )
    summary = summary_matches[-1] if summary_matches else None
    per_profile = (
        comparator_payload.get("per_profile", {})
        if isinstance(comparator_payload, dict)
        else {}
    )
    recounted = {}
    for census in per_profile.values():
        for verdict, count in census.items():
            recounted[verdict] = recounted.get(verdict, 0) + count
    recounted = dict(sorted(recounted.items()))
    refusal_count = (
        final_boundary.get("malformed_intake_witnesses_refused")
        if isinstance(final_boundary, dict)
        else None
    )
    firewall = _comparator_firewall(extracted["primary_tree"])
    firewall_clean = (
        not firewall["dangerous_tainted_targets"]
        and not firewall["dangerous_weight_calls"]
        and not firewall["receiver_calls_comparator"]
        and not firewall["receiver_calls_held_weight"]
        and not firewall["comparator_attribute_writes"]
        and not firewall["landed_module_writes"]
        and not firewall["landed_setattrs"]
        and firewall["held_values_separate_from_port_data"]
    )
    output_bytes = len(output.encode("utf-8"))
    condition = (
        returncode == 0
        and summary is not None
        and int(summary[1]) == 0
        and comparator_payload is not None
        and per_profile == extracted["expected_per_profile"]
        and recounted == extracted["expected_overall"]
        and recounted == {"agreement": 6, "disagreement": 2}
        and refusal_count == len(extracted["refusal_labels"]) == 5
        and firewall_clean
        and output_bytes < 150 * 1024
        and blocklist_clean_before
        and PRIMARY_MODULE not in sys.modules
    )
    detail = {
        "returncode": returncode,
        "primary_summary": summary,
        "declared_family": extracted["declared_family"],
        "per_profile": per_profile,
        "recounted": recounted,
        "refusals": refusal_count,
        "comparator_firewall": firewall,
        "primary_stdout_bytes": output_bytes,
        "blocklist_parent_process_clean": (
            blocklist_clean_before and PRIMARY_MODULE not in sys.modules
        ),
    }
    check(
        "port recount: subprocess module entry gives 6/2 verdicts, five refusals, comparator-only flow",
        condition,
        detail,
    )
    return detail


def discipline(
    extracted: dict[str, object],
    hashes_before: dict[str, str],
) -> dict[str, object]:
    all_paths = (PRIMARY_PATH,) + AUDIT_INPUT_PATHS
    hashes_after = {
        relative: _sha256(ROOT / relative)
        for relative in all_paths
    }
    imports_exact = (
        Path(B317.__file__).resolve() == (ROOT / AUDIT_INPUT_PATHS[0]).resolve()
        and Path(R317.__file__).resolve() == (ROOT / AUDIT_INPUT_PATHS[1]).resolve()
    )
    boundary = extracted["boundary"]
    condition = (
        hashes_before == hashes_after
        and imports_exact
        and PRIMARY_MODULE not in sys.modules
        and boundary == OWN_BOUNDARY
        and boundary["w6_closed"] is False
        and boundary["born_law_selected"] is False
        and boundary["supplies"]["selected_occurrence_law"] is False
        and boundary["supplies"]["calibration_map"] is False
    )
    detail = {
        "landed_hashes_stable": hashes_before == hashes_after,
        "imports_exact": imports_exact,
        "blocklist": BLOCKLIST,
        "blocklist_imported": PRIMARY_MODULE in sys.modules,
        "boundary": boundary,
    }
    check(
        "discipline: no landed writes, blocklist clean, boundary language verbatim",
        condition,
        detail,
    )
    print("BOUNDARY", json.dumps(boundary, sort_keys=True, separators=(",", ":")))
    return detail


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    started = perf_counter()
    all_paths = (PRIMARY_PATH,) + AUDIT_INPUT_PATHS
    hashes_before = {
        relative: _sha256(ROOT / relative)
        for relative in all_paths
    }
    try:
        primary_source = (ROOT / PRIMARY_PATH).read_text(encoding="utf-8")
        primary_tree = ast.parse(primary_source, filename=PRIMARY_PATH)
        landed_sources = {
            relative: (ROOT / relative).read_text(encoding="utf-8")
            for relative in AUDIT_INPUT_PATHS
        }
        landed_trees = {
            relative: ast.parse(source, filename=relative)
            for relative, source in landed_sources.items()
        }

        extracted = extraction(
            primary_source,
            primary_tree,
            landed_sources,
        )
        census_recount(extracted, landed_trees)
        weight_location_recount(extracted, landed_trees)
        interface_necessity_recount(extracted)
        port_recount(extracted)
        discipline(extracted, hashes_before)
    except Exception as exc:
        check(
            "independent checker completed without an internal exception",
            False,
            {"type": type(exc).__name__, "message": str(exc)},
        )
    runtime = perf_counter() - started
    print(
        "SUMMARY PASS",
        PASS,
        "FAIL",
        FAIL,
        "RUNTIME_SEC",
        f"{runtime:.6f}",
    )
    print(
        "RESULT",
        "CYCLE744_RECEIVER_INDEPENDENT_CHECK_GREEN"
        if FAIL == 0
        else "CYCLE744_RECEIVER_INDEPENDENT_CHECK_FAILED",
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
