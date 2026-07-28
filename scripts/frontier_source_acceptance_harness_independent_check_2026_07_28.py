#!/usr/bin/env python3
"""Independent, data-only adversary for the frozen source-acceptance harness."""

AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/SOURCE_ACCEPTANCE_HARNESS_SUPPORT_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_source_acceptance_harness_2026_07_28.py",
    "scripts/signed_gravity_oriented_tensor_source_lift.py",
    "scripts/two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18.py",
)

import ast
from contextlib import redirect_stdout
import hashlib
import io
import json
import math
from pathlib import Path
import re
import sys
import time
from typing import Any

import numpy as np


HARNESS_MODULE = "frontier_source_acceptance_harness_2026_07_28"
assert HARNESS_MODULE not in sys.modules

import signed_gravity_oriented_tensor_source_lift as S1
import two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18 as S2

assert HARNESS_MODULE not in sys.modules


ROOT = Path(__file__).resolve().parents[1]
START = time.monotonic()
PASS_COUNT = 0
FAIL_COUNT = 0


class ExtractionError(RuntimeError):
    """The frozen surface was not representable as inert literal data."""


def _jsonable(value: Any) -> Any:
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, np.generic):
        return value.item()
    if isinstance(value, dict):
        return {str(key): _jsonable(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [_jsonable(item) for item in value]
    if isinstance(value, (str, int, float, bool)) or value is None:
        return value
    raise TypeError(f"not JSONable: {type(value).__name__}")


def _digest(value: Any) -> str:
    payload = json.dumps(
        _jsonable(value), sort_keys=True, separators=(",", ":"), allow_nan=False
    )
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _check(label: str, condition: bool, detail: Any) -> bool:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        status = "PASS"
    else:
        FAIL_COUNT += 1
        status = "FAIL"
    rendered = json.dumps(_jsonable(detail), sort_keys=True, allow_nan=False)
    print(f"{status} {label} :: {rendered}")
    return condition


def _safe_data(
    node: ast.AST, names: dict[str, Any], local_names: dict[str, Any] | None = None
) -> Any:
    """Evaluate only the small literal-data grammar used by frozen records."""

    local_names = {} if local_names is None else local_names
    if isinstance(node, ast.Constant):
        return node.value
    if isinstance(node, ast.Name):
        if node.id in local_names:
            return local_names[node.id]
        if node.id in names:
            return names[node.id]
        raise ExtractionError(f"unresolved data name {node.id}")
    if isinstance(node, ast.Tuple):
        return tuple(_safe_data(item, names, local_names) for item in node.elts)
    if isinstance(node, ast.List):
        return [_safe_data(item, names, local_names) for item in node.elts]
    if isinstance(node, ast.Dict):
        return {
            _safe_data(key, names, local_names): _safe_data(value, names, local_names)
            for key, value in zip(node.keys, node.values)
        }
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
        value = _safe_data(node.operand, names, local_names)
        if not isinstance(value, (int, float)):
            raise ExtractionError("unary sign applied to non-number")
        return value if isinstance(node.op, ast.UAdd) else -value
    if isinstance(node, ast.Call):
        if (
            isinstance(node.func, ast.Name)
            and node.func.id == "dict"
            and len(node.args) == 1
            and not node.keywords
        ):
            return dict(_safe_data(node.args[0], names, local_names))
        raise ExtractionError(f"non-data call {ast.unparse(node)}")
    if isinstance(node, ast.ListComp):
        if len(node.generators) != 1:
            raise ExtractionError("only one-clause literal list comprehensions allowed")
        clause = node.generators[0]
        if (
            clause.is_async
            or clause.ifs
            or not isinstance(clause.target, ast.Name)
        ):
            raise ExtractionError("non-literal list-comprehension clause")
        rows = []
        for item in _safe_data(clause.iter, names, local_names):
            nested = dict(local_names)
            nested[clause.target.id] = item
            rows.append(_safe_data(node.elt, names, nested))
        return rows
    raise ExtractionError(f"non-data AST node {type(node).__name__}")


def _assignment_nodes(tree: ast.Module) -> dict[str, ast.AST]:
    assignments: dict[str, ast.AST] = {}
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1:
            target = node.targets[0]
            if isinstance(target, ast.Name):
                assignments[target.id] = node.value
        elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            assignments[node.target.id] = node.value
    return assignments


def _extract_named_data(
    tree: ast.Module, wanted: tuple[str, ...]
) -> dict[str, Any]:
    assignments = _assignment_nodes(tree)
    values: dict[str, Any] = {}
    pending = set(wanted)
    while pending:
        progressed = False
        for name in tuple(pending):
            node = assignments.get(name)
            if node is None:
                raise ExtractionError(f"missing frozen assignment {name}")
            try:
                values[name] = _safe_data(node, values)
            except ExtractionError as exc:
                if "unresolved data name" in str(exc):
                    continue
                raise
            pending.remove(name)
            progressed = True
        if not progressed:
            unresolved = ", ".join(sorted(pending))
            raise ExtractionError(f"cyclic or unresolved frozen data: {unresolved}")
    return values


def _class_method(tree: ast.Module, class_name: str, method_name: str) -> ast.FunctionDef:
    for node in tree.body:
        if isinstance(node, ast.ClassDef) and node.name == class_name:
            for member in node.body:
                if isinstance(member, ast.FunctionDef) and member.name == method_name:
                    return member
    raise ExtractionError(f"missing {class_name}.{method_name}")


def _function(tree: ast.Module, name: str) -> ast.FunctionDef:
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == name:
            return node
    raise ExtractionError(f"missing function {name}")


def _accepted_expression(verdict: ast.FunctionDef) -> ast.AST:
    for node in verdict.body:
        if (
            isinstance(node, ast.Assign)
            and len(node.targets) == 1
            and isinstance(node.targets[0], ast.Name)
            and node.targets[0].id == "accepted"
        ):
            return node.value
    raise ExtractionError("tensor verdict has no accepted expression")


def _return_expression(function: ast.FunctionDef) -> ast.AST:
    returns = [
        node.value
        for node in function.body
        if isinstance(node, ast.Return) and node.value is not None
    ]
    if len(returns) != 1:
        raise ExtractionError(
            f"{function.name} does not have one top-level return expression"
        )
    return returns[0]


def _corrupted_vector_length(tree: ast.Module) -> int:
    main = _function(tree, "main")
    for node in ast.walk(main):
        if (
            isinstance(node, ast.Assign)
            and len(node.targets) == 1
            and isinstance(node.targets[0], ast.Name)
            and node.targets[0].id == "corrupted_tensor_record"
            and isinstance(node.value, ast.Call)
            and node.value.args
        ):
            vector_call = node.value.args[0]
            if (
                isinstance(vector_call, ast.Call)
                and isinstance(vector_call.func, ast.Attribute)
                and isinstance(vector_call.func.value, ast.Name)
                and vector_call.func.value.id == "np"
                and vector_call.func.attr == "zeros"
                and vector_call.args
            ):
                length = ast.literal_eval(vector_call.args[0])
                if isinstance(length, int) and length > 0:
                    return length
    raise ExtractionError("harness corrupted vector is not a literal np.zeros call")


def _operator_name(operator: ast.cmpop) -> str:
    names = {
        ast.Eq: "==",
        ast.NotEq: "!=",
        ast.Lt: "<",
        ast.LtE: "<=",
        ast.Gt: ">",
        ast.GtE: ">=",
    }
    for kind, name in names.items():
        if isinstance(operator, kind):
            return name
    raise ExtractionError(f"unsupported comparison {type(operator).__name__}")


def _resolved_number(node: ast.AST, s1_tol: float) -> float | None:
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return float(node.value)
    if isinstance(node, ast.Name) and node.id == "TOL":
        return float(s1_tol)
    if (
        isinstance(node, ast.Attribute)
        and isinstance(node.value, ast.Name)
        and node.value.id == "S1"
        and node.attr == "TOL"
    ):
        return float(s1_tol)
    return None


def _comparison_rows(expression: ast.AST, s1_tol: float) -> list[dict[str, Any]]:
    rows = []
    for node in ast.walk(expression):
        if isinstance(node, ast.Compare) and len(node.ops) == len(node.comparators) == 1:
            rows.append(
                {
                    "left": ast.unparse(node.left),
                    "operator": _operator_name(node.ops[0]),
                    "right": ast.unparse(node.comparators[0]),
                    "number": _resolved_number(node.comparators[0], s1_tol),
                }
            )
    return rows


def _threshold(
    rows: list[dict[str, Any]], left: str, operator: str
) -> float:
    matches = [
        row["number"]
        for row in rows
        if row["left"] == left
        and row["operator"] == operator
        and row["number"] is not None
    ]
    if len(matches) != 1:
        raise ExtractionError(
            f"expected one threshold for {left} {operator}, got {matches}"
        )
    return float(matches[0])


def _threshold_spec(rows: list[dict[str, Any]]) -> dict[str, float]:
    return {
        "block_nonnegative": _threshold(
            rows, "max(twist['block_norms'].values())", ">="
        ),
        "block_floor": _threshold(rows, "value", ">"),
        "twist_residual": _threshold(rows, "twist['twist_residual']", "<"),
        "ward_max": _threshold(rows, "max(ward['residuals'])", "<"),
        "ward_null": _threshold(rows, "ward['residuals'][2]", "<"),
        "field_flip": _threshold(rows, "locking['field_flip_residual']", "<"),
        "field_null": _threshold(rows, "locking['field_null_residual']", "<"),
        "positive_self": _threshold(rows, "locking['positive_self']", ">"),
        "scalar_complement": _threshold(rows, "scalar['complement_norm']", "<"),
        "carrier_shift": _threshold(
            rows, "carrier['tensor_source_blocks']['shift']", ">"
        ),
        "carrier_shear": _threshold(
            rows, "carrier['tensor_source_blocks']['shear']", ">"
        ),
        "chi_shift": _threshold(rows, "carrier['chi_only_blocks']['shift']", "=="),
        "chi_shear": _threshold(rows, "carrier['chi_only_blocks']['shear']", "=="),
    }


def _extract_claims(s1_tree: ast.Module) -> dict[str, bool]:
    gate = _function(s1_tree, "no_claim_gate")
    for node in gate.body:
        if (
            isinstance(node, ast.Assign)
            and len(node.targets) == 1
            and isinstance(node.targets[0], ast.Name)
            and node.targets[0].id == "claims"
        ):
            claims = ast.literal_eval(node.value)
            if not isinstance(claims, dict):
                break
            return claims
    raise ExtractionError("S1 no_claim_gate claims are not literal data")


def frozen_extraction() -> dict[str, Any]:
    harness_path = ROOT / AUDIT_INPUT_PATHS[0]
    s1_path = ROOT / AUDIT_INPUT_PATHS[1]
    s2_path = ROOT / AUDIT_INPUT_PATHS[2]
    harness_tree = ast.parse(
        harness_path.read_text(encoding="utf-8"), filename=AUDIT_INPUT_PATHS[0]
    )
    s1_tree = ast.parse(
        s1_path.read_text(encoding="utf-8"), filename=AUDIT_INPUT_PATHS[1]
    )
    s2_tree = ast.parse(
        s2_path.read_text(encoding="utf-8"), filename=AUDIT_INPUT_PATHS[2]
    )

    wanted = (
        "TENSOR_LIFT_SHA256",
        "RECOIL_RECIPROCITY_SHA256",
        "TENSOR_FROZEN_EXPECTED",
        "RECOIL_OUTCOME_LABELS",
        "RECOIL_FIXTURE_INVARIANTS",
        "RECOIL_FROZEN_EXPECTED",
    )
    frozen = _extract_named_data(harness_tree, wanted)
    s1_data = _extract_named_data(s1_tree, ("TOL",))
    verdict = _class_method(harness_tree, "TensorLiftAcceptance", "verdict")
    drift_logic = _class_method(
        harness_tree, "_PinnedAcceptance", "_record_is_drifted"
    )
    flipped_logic = _function(harness_tree, "_flipped_labels")
    accepted = _accepted_expression(verdict)
    flip_expression = _return_expression(flipped_logic)
    corrupted_length = _corrupted_vector_length(harness_tree)
    comparison_rows = _comparison_rows(accepted, float(s1_data["TOL"]))
    thresholds = _threshold_spec(comparison_rows)
    actual_pins = {
        "tensor_lift": _sha256(s1_path),
        "recoil": _sha256(s2_path),
    }
    expected_pins = {
        "tensor_lift": frozen["TENSOR_LIFT_SHA256"],
        "recoil": frozen["RECOIL_RECIPROCITY_SHA256"],
    }
    records = {
        "tensor_lift": frozen["TENSOR_FROZEN_EXPECTED"],
        "recoil": frozen["RECOIL_FROZEN_EXPECTED"],
    }
    digests = {name: _digest(record) for name, record in records.items()}
    pin_agreement = (
        actual_pins == expected_pins
        and records["tensor_lift"]["source_sha256"] == actual_pins["tensor_lift"]
        and records["recoil"]["source_sha256"] == actual_pins["recoil"]
    )
    logic_digest = hashlib.sha256(
        "\n".join(
            ast.dump(node, include_attributes=False)
            for node in (verdict, drift_logic, flipped_logic)
        ).encode("utf-8")
    ).hexdigest()
    _check(
        "frozen_extraction",
        pin_agreement and HARNESS_MODULE not in sys.modules,
        {
            "pins": {
                name: {
                    "expected": expected_pins[name],
                    "actual": actual_pins[name],
                    "verified": expected_pins[name] == actual_pins[name],
                }
                for name in expected_pins
            },
            "frozen_record_digests": digests,
            "tensor_verdict_logic_digest": logic_digest,
            "corrupted_vector_length": corrupted_length,
            "thresholds": thresholds,
        },
    )
    return {
        "harness_tree": harness_tree,
        "s1_tree": s1_tree,
        "s2_tree": s2_tree,
        "records": records,
        "digests": digests,
        "actual_pins": actual_pins,
        "expected_pins": expected_pins,
        "accepted_expression": accepted,
        "flip_expression": flip_expression,
        "corrupted_vector_length": corrupted_length,
        "comparison_rows": comparison_rows,
        "thresholds": thresholds,
        "claims": _extract_claims(s1_tree),
        "logic_digest": logic_digest,
    }


def _tensor_outcomes(
    source: np.ndarray, constraint: np.ndarray, claims: dict[str, bool]
) -> dict[str, Any]:
    projectors = S1.canonical_projectors()
    landed_calls = (
        ("projector_algebra", lambda: S1.projector_algebra_check(projectors)),
        (
            "orientation_twist",
            lambda: S1.orientation_twist_check(source, projectors),
        ),
        ("ward_constraints", lambda: S1.ward_constraint_check(source, constraint)),
        ("response_locking", lambda: S1.response_locking_check(source)),
        (
            "scalar_only_no_overclaim",
            lambda: S1.scalar_only_no_overclaim_check(projectors),
        ),
        ("free_tensor_carrier", lambda: S1.free_tensor_carrier_gate(source)),
        ("no_claim", S1.no_claim_gate),
    )
    statuses: dict[str, bool] = {}
    for name, call in landed_calls:
        try:
            passed, _detail = call()
            statuses[name] = bool(passed)
        except Exception:
            statuses[name] = False

    plus = S1.oriented(source, +1)
    minus = S1.oriented(source, -1)
    block_norms = S1.block_norms(plus, projectors)
    inverse_operator = np.linalg.inv(S1.universal_block_operator())
    field_plus = inverse_operator @ plus
    field_minus = inverse_operator @ minus
    field_null = inverse_operator @ S1.oriented(source, 0)
    locking_signs = {}
    for eta_a in (+1, -1):
        for eta_b in (+1, -1):
            coupling = float(
                S1.oriented(source, eta_a)
                @ inverse_operator
                @ S1.oriented(source, eta_b)
            )
            locking_signs[f"{eta_a:+d},{eta_b:+d}"] = math.copysign(1.0, coupling)
    scalar_complement = (
        projectors.shift + projectors.shear
    ) @ S1.oriented(S1.scalar_a1_source(), -1)
    chi_only = np.zeros(10, dtype=float)
    chi_only[0] = 1.0
    chi_only[4] = 0.5
    values = {
        "projector_algebra": {
            "ranks": {
                name: int(np.linalg.matrix_rank(projector))
                for name, projector in projectors.blocks.items()
            }
        },
        "orientation_twist": {
            "block_norms": block_norms,
            "twist_residual": max(
                float(np.linalg.norm(projector @ plus + projector @ minus))
                for projector in projectors.blocks.values()
            ),
        },
        "ward_constraints": {
            "residuals": [
                float(np.linalg.norm(constraint @ S1.oriented(source, eta)))
                for eta in (+1, -1, 0)
            ]
        },
        "response_locking": {
            "field_flip_residual": float(np.linalg.norm(field_plus + field_minus)),
            "field_null_residual": float(np.linalg.norm(field_null)),
            "positive_self": float(source @ inverse_operator @ source),
            "locking_signs": locking_signs,
        },
        "scalar_only_no_overclaim": {
            "complement_norm": float(np.linalg.norm(scalar_complement))
        },
        "free_tensor_carrier": {
            "tensor_source_blocks": S1.block_norms(source, projectors),
            "chi_only_blocks": S1.block_norms(chi_only, projectors),
        },
        "no_claim": dict(claims),
    }
    return {
        name: {
            "check": "PASS" if statuses[name] else "FAIL",
            "values": _jsonable(values[name]),
        }
        for name in values
    }


def _recoil_record(source_sha256: str) -> tuple[dict[str, Any], list[dict[str, str]]]:
    coin, fswap, contact, _update, _details = S2.c315.logical_update_controls(
        S2.LABELS
    )
    factors = (coin, fswap, contact)
    calls = (
        ("note_contract", S2.note_contract, ()),
        ("local_operator_controls", S2.local_operator_controls, ()),
        ("seam_number_contact_controls", S2.seam_number_contact_controls, (factors,)),
        ("physical_intertwiner_controls", S2.physical_intertwiner_controls, (factors,)),
        ("emission_absorption_controls", S2.emission_absorption_controls, ()),
        ("response_reciprocity_controls", S2.response_reciprocity_controls, (factors,)),
        (
            "covariance_translation_support_controls",
            S2.covariance_translation_support_controls,
            (factors,),
        ),
        (
            "deletion_mass_contact_domain_controls",
            S2.deletion_mass_contact_domain_controls,
            (factors,),
        ),
        ("inventory_controls", S2.inventory_controls, ()),
        ("methodology_controls", S2.methodology_controls, ()),
    )
    stream = io.StringIO()
    exceptions = []
    with redirect_stdout(stream):
        for name, call, arguments in calls:
            try:
                call(*arguments)
            except Exception as exc:
                exceptions.append(
                    {"entry_point": name, "exception": f"{type(exc).__name__}: {exc}"}
                )
    pattern = re.compile(r"^(PASS|FAIL) (.*?) :: ?(.*)$")
    outcomes = []
    for line in stream.getvalue().splitlines():
        match = pattern.match(line)
        if match:
            status, label, _detail = match.groups()
            outcomes.append({"check": label, "pass": status == "PASS"})
    record = {
        "outcomes": outcomes,
        "fixture_invariants": {
            "cells": len(S2.ENDPOINTS),
            "directions_per_cell": [
                len(S2.REVERSE) for _cell in S2.ENDPOINTS
            ],
            "emission_absorption_channels": len(S2.ENDPOINTS) * len(S2.REVERSE),
            "ordered_recoil_pairs": len(S2.REVERSE),
        },
        "model_port": "no Cycle-322 certificate model-dict port",
        "source_sha256": source_sha256,
    }
    return record, exceptions


def independent_expected(extracted: dict[str, Any]) -> dict[str, Any]:
    canonical_source, canonical_constraint = S1.tensor_source_with_constraints()
    tensor_record = {
        "outcomes": _tensor_outcomes(
            canonical_source, canonical_constraint, extracted["claims"]
        ),
        "source_sha256": extracted["actual_pins"]["tensor_lift"],
    }
    recoil_record, recoil_exceptions = _recoil_record(
        extracted["actual_pins"]["recoil"]
    )
    tensor_equal = tensor_record == extracted["records"]["tensor_lift"]
    recoil_equal = recoil_record == extracted["records"]["recoil"]
    _check(
        "independent_expected",
        tensor_equal and recoil_equal and not recoil_exceptions,
        {
            "tensor_fieldwise_equal": tensor_equal,
            "tensor_outcome_digest": _digest(tensor_record),
            "recoil_fieldwise_equal": recoil_equal,
            "recoil_outcome_digest": _digest(recoil_record),
            "recoil_labels": len(recoil_record["outcomes"]),
            "recoil_exceptions": recoil_exceptions,
        },
    )
    return {
        "source": canonical_source,
        "constraint": canonical_constraint,
        "tensor_record": tensor_record,
        "recoil_record": recoil_record,
    }


def independent_verdict(
    record: dict[str, Any],
    frozen: dict[str, Any],
    expected_pin: str,
    thresholds: dict[str, float],
) -> str:
    if (
        record.get("pin_verified") is not True
        or record.get("source_sha256") != expected_pin
        or record.get("expected_sha256") != expected_pin
    ):
        return "DRIFT"
    outcomes = record.get("outcomes", {})
    expected = frozen["outcomes"]
    if set(outcomes) != set(expected):
        return "REJECT"
    if any(outcomes[name].get("check") != "PASS" for name in expected):
        return "REJECT"
    projector = outcomes["projector_algebra"]["values"]
    twist = outcomes["orientation_twist"]["values"]
    ward = outcomes["ward_constraints"]["values"]
    locking = outcomes["response_locking"]["values"]
    scalar = outcomes["scalar_only_no_overclaim"]["values"]
    carrier = outcomes["free_tensor_carrier"]["values"]
    no_claim = outcomes["no_claim"]["values"]
    accepted = (
        projector["ranks"]
        == expected["projector_algebra"]["values"]["ranks"]
        and max(twist["block_norms"].values()) >= thresholds["block_nonnegative"]
        and all(
            value > thresholds["block_floor"]
            for value in twist["block_norms"].values()
        )
        and twist["twist_residual"] < thresholds["twist_residual"]
        and max(ward["residuals"]) < thresholds["ward_max"]
        and ward["residuals"][2] < thresholds["ward_null"]
        and locking["field_flip_residual"] < thresholds["field_flip"]
        and locking["field_null_residual"] < thresholds["field_null"]
        and locking["positive_self"] > thresholds["positive_self"]
        and locking["locking_signs"]
        == expected["response_locking"]["values"]["locking_signs"]
        and scalar["complement_norm"] < thresholds["scalar_complement"]
        and carrier["tensor_source_blocks"]["shift"] > thresholds["carrier_shift"]
        and carrier["tensor_source_blocks"]["shear"] > thresholds["carrier_shear"]
        and carrier["chi_only_blocks"]["shift"] == thresholds["chi_shift"]
        and carrier["chi_only_blocks"]["shear"] == thresholds["chi_shear"]
        and no_claim == expected["no_claim"]["values"]
    )
    return "ACCEPT" if accepted else "REJECT"


def _interpret_expression(node: ast.AST, environment: dict[str, Any]) -> Any:
    """Restricted interpreter for the extracted frozen accepted-expression."""

    if isinstance(node, ast.Constant):
        return node.value
    if isinstance(node, ast.Name):
        if node.id in environment:
            return environment[node.id]
        raise ExtractionError(f"unbound verdict name {node.id}")
    if isinstance(node, ast.Tuple):
        return tuple(_interpret_expression(item, environment) for item in node.elts)
    if isinstance(node, ast.List):
        return [_interpret_expression(item, environment) for item in node.elts]
    if isinstance(node, ast.Dict):
        return {
            _interpret_expression(key, environment): _interpret_expression(
                value, environment
            )
            for key, value in zip(node.keys, node.values)
        }
    if isinstance(node, ast.Attribute):
        value = _interpret_expression(node.value, environment)
        if isinstance(value, dict) and node.attr in value:
            return value[node.attr]
        raise ExtractionError(f"forbidden verdict attribute {ast.unparse(node)}")
    if isinstance(node, ast.Subscript):
        value = _interpret_expression(node.value, environment)
        key = _interpret_expression(node.slice, environment)
        return value[key]
    if isinstance(node, ast.Call):
        if isinstance(node.func, ast.Name) and node.func.id in {"max", "all"}:
            argument = _interpret_expression(node.args[0], environment)
            return max(argument) if node.func.id == "max" else all(argument)
        if (
            isinstance(node.func, ast.Attribute)
            and node.func.attr in {"values", "items"}
            and not node.args
            and not node.keywords
        ):
            value = _interpret_expression(node.func.value, environment)
            if not isinstance(value, dict):
                raise ExtractionError(f"{node.func.attr}() applied to non-dict")
            return value.values() if node.func.attr == "values" else value.items()
        if (
            isinstance(node.func, ast.Attribute)
            and node.func.attr == "get"
            and 1 <= len(node.args) <= 2
            and not node.keywords
        ):
            value = _interpret_expression(node.func.value, environment)
            if not isinstance(value, dict):
                raise ExtractionError("get() applied to non-dict")
            arguments = [
                _interpret_expression(argument, environment)
                for argument in node.args
            ]
            return value.get(*arguments)
        raise ExtractionError(f"forbidden verdict call {ast.unparse(node)}")
    if isinstance(node, ast.BoolOp):
        values = [_interpret_expression(value, environment) for value in node.values]
        return all(values) if isinstance(node.op, ast.And) else any(values)
    if isinstance(node, ast.Compare) and len(node.ops) == len(node.comparators) == 1:
        left = _interpret_expression(node.left, environment)
        right = _interpret_expression(node.comparators[0], environment)
        operator = node.ops[0]
        if isinstance(operator, ast.Eq):
            return left == right
        if isinstance(operator, ast.NotEq):
            return left != right
        if isinstance(operator, ast.Lt):
            return left < right
        if isinstance(operator, ast.LtE):
            return left <= right
        if isinstance(operator, ast.Gt):
            return left > right
        if isinstance(operator, ast.GtE):
            return left >= right
        raise ExtractionError("forbidden verdict comparison")
    if isinstance(node, ast.GeneratorExp) and len(node.generators) == 1:
        clause = node.generators[0]
        if (
            clause.is_async
            or clause.ifs
            or not isinstance(clause.target, ast.Name)
        ):
            raise ExtractionError("forbidden verdict generator")
        items = _interpret_expression(clause.iter, environment)
        values = []
        for item in items:
            nested = dict(environment)
            nested[clause.target.id] = item
            values.append(_interpret_expression(node.elt, nested))
        return values
    if isinstance(node, ast.ListComp) and len(node.generators) == 1:
        clause = node.generators[0]
        if clause.is_async:
            raise ExtractionError("forbidden async verdict comprehension")
        items = _interpret_expression(clause.iter, environment)
        values = []
        for item in items:
            nested = dict(environment)
            if isinstance(clause.target, ast.Name):
                nested[clause.target.id] = item
            elif (
                isinstance(clause.target, (ast.Tuple, ast.List))
                and isinstance(item, (tuple, list))
                and len(clause.target.elts) == len(item)
                and all(isinstance(target, ast.Name) for target in clause.target.elts)
            ):
                for target, value in zip(clause.target.elts, item):
                    nested[target.id] = value
            else:
                raise ExtractionError("forbidden verdict comprehension target")
            if all(_interpret_expression(condition, nested) for condition in clause.ifs):
                values.append(_interpret_expression(node.elt, nested))
        return values
    raise ExtractionError(f"forbidden verdict node {type(node).__name__}")


def frozen_logic_verdict(
    record: dict[str, Any],
    frozen: dict[str, Any],
    expected_pin: str,
    accepted_expression: ast.AST,
) -> str:
    drifted = (
        record.get("pin_verified") is not True
        or record.get("source_sha256") != expected_pin
        or record.get("expected_sha256") != expected_pin
    )
    if drifted:
        return "DRIFT"
    outcomes = record.get("outcomes", {})
    expected = frozen["outcomes"]
    if set(outcomes) != set(expected):
        return "REJECT"
    if any(outcomes[name].get("check") != "PASS" for name in expected):
        return "REJECT"
    environment = {
        "projector": outcomes["projector_algebra"]["values"],
        "twist": outcomes["orientation_twist"]["values"],
        "ward": outcomes["ward_constraints"]["values"],
        "locking": outcomes["response_locking"]["values"],
        "scalar": outcomes["scalar_only_no_overclaim"]["values"],
        "carrier": outcomes["free_tensor_carrier"]["values"],
        "no_claim": outcomes["no_claim"]["values"],
        "frozen": expected,
        "expected_signs": expected["response_locking"]["values"]["locking_signs"],
        "S1": {"TOL": float(S1.TOL)},
    }
    accepted = bool(_interpret_expression(accepted_expression, environment))
    return "ACCEPT" if accepted else "REJECT"


def _with_pin(outcomes: dict[str, Any], actual: str, expected: str) -> dict[str, Any]:
    return {
        "source_sha256": actual,
        "expected_sha256": expected,
        "pin_verified": actual == expected,
        "outcomes": outcomes,
    }


def verdict_semantics(
    extracted: dict[str, Any], independent: dict[str, Any]
) -> dict[str, Any]:
    expected_pin = extracted["expected_pins"]["tensor_lift"]
    frozen = extracted["records"]["tensor_lift"]
    canonical = _with_pin(
        independent["tensor_record"]["outcomes"], expected_pin, expected_pin
    )
    corrupted_outcomes = _tensor_outcomes(
        np.zeros(extracted["corrupted_vector_length"], dtype=float),
        independent["constraint"],
        extracted["claims"],
    )
    corrupted = _with_pin(corrupted_outcomes, expected_pin, expected_pin)
    wrong_pin = "0" * 64
    drift = _with_pin({}, extracted["actual_pins"]["tensor_lift"], wrong_pin)
    vectors = {
        "canonical": (canonical, "ACCEPT"),
        "corrupted": (corrupted, "REJECT"),
        "wrong_pin": (drift, "DRIFT"),
    }
    rows = {}
    for name, (record, expected_verdict) in vectors.items():
        pin = wrong_pin if name == "wrong_pin" else expected_pin
        own = independent_verdict(
            record, frozen, pin, extracted["thresholds"]
        )
        frozen_logic = frozen_logic_verdict(
            record, frozen, pin, extracted["accepted_expression"]
        )
        rows[name] = {
            "expected": expected_verdict,
            "independent": own,
            "frozen_logic": frozen_logic,
        }
    expected_flips = [
        name
        for name, expected in frozen["outcomes"].items()
        if corrupted_outcomes.get(name, {}).get("check") != expected["check"]
    ]
    harness_reported_flips = _interpret_expression(
        extracted["flip_expression"],
        {
            "expected_outcomes": frozen["outcomes"],
            "actual_outcomes": corrupted_outcomes,
        },
    )
    agreement = all(
        row["independent"] == row["frozen_logic"] == row["expected"]
        for row in rows.values()
    )
    _check(
        "verdict_semantics",
        agreement and expected_flips == harness_reported_flips,
        {
            "vectors": rows,
            "corrupted_flipped_checks": expected_flips,
            "harness_corrupted_flipped_checks": harness_reported_flips,
        },
    )
    return {
        "agreement": agreement,
        "vectors": rows,
        "corrupted_flipped_checks": expected_flips,
    }


def _attribute_root(node: ast.AST) -> str | None:
    while isinstance(node, ast.Attribute):
        node = node.value
    return node.id if isinstance(node, ast.Name) else None


def _landed_attribute_writes(tree: ast.Module) -> list[dict[str, Any]]:
    rows = []
    for node in ast.walk(tree):
        targets: list[ast.AST] = []
        if isinstance(node, ast.Assign):
            targets = list(node.targets)
        elif isinstance(node, ast.AnnAssign):
            targets = [node.target]
        elif isinstance(node, ast.AugAssign):
            targets = [node.target]
        elif isinstance(node, ast.Delete):
            targets = list(node.targets)
        else:
            continue
        for target in targets:
            for child in ast.walk(target):
                if (
                    isinstance(child, ast.Attribute)
                    and _attribute_root(child) in {"S1", "S2"}
                ):
                    rows.append(
                        {
                            "target": ast.unparse(child),
                            "line": node.lineno,
                            "operation": type(node).__name__,
                        }
                    )
    return rows


def _numeric_comparison_values(
    functions: list[ast.FunctionDef], s1_tol: float
) -> set[float]:
    values = set()
    for function in functions:
        for node in ast.walk(function):
            if isinstance(node, ast.Compare):
                for comparator in node.comparators:
                    number = _resolved_number(comparator, s1_tol)
                    if number is not None:
                        values.add(number)
    return values


def discipline(extracted: dict[str, Any]) -> dict[str, Any]:
    harness_tree = extracted["harness_tree"]
    audit_node = _assignment_nodes(harness_tree).get("AUDIT_INPUT_PATHS")
    if audit_node is None:
        raise ExtractionError("harness AUDIT_INPUT_PATHS missing")
    harness_audit_tuple = ast.literal_eval(audit_node)
    harness_thresholds = {
        float(row["number"])
        for row in extracted["comparison_rows"]
        if row["number"] is not None
    }
    landed_check_names = (
        "projector_algebra_check",
        "orientation_twist_check",
        "ward_constraint_check",
        "response_locking_check",
        "scalar_only_no_overclaim_check",
        "free_tensor_carrier_gate",
        "no_claim_gate",
    )
    landed_functions = [
        _function(extracted["s1_tree"], name) for name in landed_check_names
    ]
    landed_thresholds = _numeric_comparison_values(
        landed_functions, float(S1.TOL)
    )
    new_tolerances = sorted(harness_thresholds - landed_thresholds)
    module_writes = _landed_attribute_writes(harness_tree)
    condition = (
        isinstance(harness_audit_tuple, tuple)
        and not new_tolerances
        and not module_writes
    )
    _check(
        "discipline",
        condition,
        {
            "harness_audit_tuple_literal": harness_audit_tuple,
            "harness_thresholds": sorted(harness_thresholds),
            "landed_S1_thresholds": sorted(landed_thresholds),
            "new_tolerances": new_tolerances,
            "landed_module_attribute_writes": module_writes,
        },
    )
    return {
        "audit_tuple": harness_audit_tuple,
        "new_tolerances": new_tolerances,
        "module_writes": module_writes,
    }


def main() -> int:
    result: dict[str, Any] = {}
    try:
        extracted = frozen_extraction()
        independent = independent_expected(extracted)
        verdicts = verdict_semantics(extracted, independent)
        discipline_result = discipline(extracted)
        result = {
            "frozen_record_digests": extracted["digests"],
            "digest_agreement": {
                "tensor_lift": independent["tensor_record"]
                == extracted["records"]["tensor_lift"],
                "recoil": independent["recoil_record"]
                == extracted["records"]["recoil"],
            },
            "verdict_agreement": verdicts["agreement"],
            "discipline": discipline_result,
        }
    except Exception as exc:
        _check(
            "independent_checker_exception",
            False,
            {"exception": f"{type(exc).__name__}: {exc}"},
        )
        result["exception"] = f"{type(exc).__name__}: {exc}"

    assert HARNESS_MODULE not in sys.modules
    runtime = time.monotonic() - START
    summary = {
        "checks": {"pass": PASS_COUNT, "fail": FAIL_COUNT},
        **result,
        "runtime_seconds": round(runtime, 6),
    }
    print(json.dumps(_jsonable(summary), indent=2, sort_keys=True, allow_nan=False))
    print(
        f"SUMMARY PASS={PASS_COUNT} FAIL={FAIL_COUNT} "
        f"RUNTIME={runtime:.3f}s"
    )
    return int(FAIL_COUNT != 0)


if __name__ == "__main__":
    raise SystemExit(main())
