#!/usr/bin/env python3
"""Independent data/behavior adversary for the source-acceptance tool."""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/SOURCE_ACCEPTANCE_HARNESS_SUPPORT_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_source_acceptance_harness_2026_07_28.py",
    "scripts/signed_gravity_oriented_tensor_source_lift.py",
    "scripts/two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18.py",
    "scripts/physical_m2_gravity_source_bridge_tournament_synthesis_cycle294_2026_07_17.py",
    "docs/SIGNED_GRAVITY_ORIENTED_TENSOR_SOURCE_LIFT_NOTE.md",
    "docs/work_history/repo/review_feedback/DIRECT_GATEWISE_MATTER_MEDIATOR_CURRENT_LEDGER_ROUTE_A_CYCLE293_NOTE_2026-07-17.md",
    "docs/work_history/repo/review_feedback/GRAVITY_ROUTE_C_BOUNDED_DIRECT_CURRENT_SEARCH_NOTE_2026-07-17.md",
    "docs/work_history/repo/review_feedback/LOCAL_M2_MASS_SCALAR_DEFORMATION_RESPONSE_ROUTE_B_NOTE_2026-07-17.md",
    "docs/work_history/repo/review_feedback/PHYSICAL_CYCLE269_OVERLAP_AWARE_TWO_CELL_CYCLE315_NOTE_2026-07-18.md",
    "docs/work_history/repo/review_feedback/PHYSICAL_M2_GRAVITY_SOURCE_BRIDGE_TOURNAMENT_SYNTHESIS_CYCLE294_NOTE_2026-07-17.md",
    "docs/work_history/repo/review_feedback/PROPER_CUBIC_RECOIL_BALANCED_CARRIED_SOURCE_CYCLE318_NOTE_2026-07-18.md",
    "docs/work_history/repo/review_feedback/TWO_CELL_TWO_SOURCE_RECOIL_RECIPROCITY_CYCLE322_NOTE_2026-07-18.md",
    "docs/work_history/repo/review_feedback/UNIT_WEIGHT_CARRIED_LINK_RECOIL_CYCLE320_NOTE_2026-07-18.md",
    "scripts/active_cubic_source_response_cycle211_2026_07_16.py",
    "scripts/archive_carrier_source_ledger_cycle227_2026_07_17.py",
    "scripts/autonomous_cubic_field_emission_cycle214_2026_07_16.py",
    "scripts/carried_internal_species_source_field_ledger_repair_2026_07_17.py",
    "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py",
    "scripts/connected_edge_same_code_local_instrument_cycle278_2026_07_17.py",
    "scripts/contractible_lightcone_wilson_quotient_cycle271_2026_07_17.py",
    "scripts/direct_gatewise_matter_mediator_current_ledger_route_a_cycle293_2026_07_17.py",
    "scripts/exact_3d_higher_form_bosonization_cycle235_2026_07_17.py",
    "scripts/finite_coin_scalar_wave_dilation_cycle215_2026_07_16.py",
    "scripts/fock_modular_boundary_current_cycle229_2026_07_17.py",
    "scripts/gravity_route_c_bounded_direct_current_search_2026_07_17.py",
    "scripts/local_conservative_commit_resource_gravity_cycle9_2026_07_14.py",
    "scripts/local_generator_source_tournament_cycle228_2026_07_17.py",
    "scripts/local_m2_mass_scalar_deformation_response_route_b_2026_07_17.py",
    "scripts/local_rough_puncture_odd_sector_cycle247_2026_07_17.py",
    "scripts/locally_matched_wilson_sector_states_cycle275_2026_07_17.py",
    "scripts/numpy_replay_bootstrap.py",
    "scripts/physical_cycle269_collision_safe_auxiliary_ports_2026_07_17.py",
    "scripts/physical_cycle269_common_m64_fixed_seam_cycle311_2026_07_18.py",
    "scripts/physical_cycle269_full_two_particle_sector_interface_cycle305_2026_07_17.py",
    "scripts/physical_cycle269_higher_number_fixed_seam_cycle308_2026_07_17.py",
    "scripts/physical_cycle269_overlap_aware_two_cell_cycle315_2026_07_18.py",
    "scripts/physical_cycle269_reference_relative_localized_pair_lift_2026_07_17.py",
    "scripts/physical_cycle269_staggered_reservoir_catchup_2026_07_17.py",
    "scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py",
    "scripts/retarded_cubic_mass_field_cycle213_2026_07_16.py",
    "scripts/signed_gravity_source_character_uniqueness_theorem.py",
    "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py",
    "scripts/virtual_exchange_green_kernel_cycle216_2026_07_16.py",
    "scripts/wilson_subsystem_sector_free_compiler_cycle269_2026_07_17.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
import copy
from contextlib import redirect_stdout
import hashlib
import io
import json
import math
from pathlib import Path
import re
import subprocess
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
HARNESS_PATH = AUDIT_INPUT_PATHS[0]
TENSOR_PATH = AUDIT_INPUT_PATHS[1]
RECOIL_PATH = AUDIT_INPUT_PATHS[2]
BRIDGE_PATH = AUDIT_INPUT_PATHS[3]
START = time.monotonic()
PASS_COUNT = 0
FAIL_COUNT = 0


class ExtractionError(RuntimeError):
    """The reviewed surface was not representable as inert literal data."""


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


def _finite_data(value: Any) -> bool:
    if isinstance(value, bool) or value is None or isinstance(value, str):
        return True
    if isinstance(value, int):
        return True
    if isinstance(value, float):
        return math.isfinite(value)
    if isinstance(value, np.generic):
        return _finite_data(value.item())
    if isinstance(value, np.ndarray):
        return bool(
            np.issubdtype(value.dtype, np.number)
            and not np.issubdtype(value.dtype, np.complexfloating)
            and np.all(np.isfinite(value))
        )
    if isinstance(value, dict):
        return all(
            isinstance(key, (str, int, float, bool))
            and _finite_data(key)
            and _finite_data(item)
            for key, item in value.items()
        )
    if isinstance(value, (tuple, list)):
        return all(_finite_data(item) for item in value)
    return False


def _digest(value: Any) -> str:
    payload = json.dumps(
        _jsonable(value), sort_keys=True, separators=(",", ":"), allow_nan=False
    )
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def _sha256(path: str) -> str:
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def _check(label: str, condition: bool, detail: Any) -> bool:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        status = "PASS"
    else:
        FAIL_COUNT += 1
        status = "FAIL"
    print(
        f"{status} {label} :: "
        f"{json.dumps(_jsonable(detail), sort_keys=True, allow_nan=False)}"
    )
    return condition


def _assignments(tree: ast.Module) -> dict[str, ast.AST]:
    rows: dict[str, ast.AST] = {}
    for node in tree.body:
        if (
            isinstance(node, ast.Assign)
            and len(node.targets) == 1
            and isinstance(node.targets[0], ast.Name)
        ):
            rows[node.targets[0].id] = node.value
        elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            rows[node.target.id] = node.value
    return rows


def _safe_data(
    node: ast.AST,
    names: dict[str, Any],
    local_names: dict[str, Any] | None = None,
) -> Any:
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
            _safe_data(key, names, local_names): _safe_data(
                value, names, local_names
            )
            for key, value in zip(node.keys, node.values)
        }
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
        value = _safe_data(node.operand, names, local_names)
        if not isinstance(value, (int, float)):
            raise ExtractionError("unary sign applied to non-number")
        return value if isinstance(node.op, ast.UAdd) else -value
    if (
        isinstance(node, ast.BinOp)
        and isinstance(node.op, ast.Mult)
        and isinstance(node.left, ast.Constant)
        and isinstance(node.right, ast.Constant)
    ):
        return node.left.value * node.right.value
    if (
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "dict"
        and len(node.args) == 1
        and not node.keywords
    ):
        return dict(_safe_data(node.args[0], names, local_names))
    if isinstance(node, ast.ListComp) and len(node.generators) == 1:
        clause = node.generators[0]
        if clause.is_async or clause.ifs or not isinstance(clause.target, ast.Name):
            raise ExtractionError("non-literal list comprehension")
        rows = []
        for item in _safe_data(clause.iter, names, local_names):
            nested = dict(local_names)
            nested[clause.target.id] = item
            rows.append(_safe_data(node.elt, names, nested))
        return rows
    raise ExtractionError(f"non-data AST node {type(node).__name__}")


def _extract_named(tree: ast.Module, wanted: tuple[str, ...]) -> dict[str, Any]:
    nodes = _assignments(tree)
    values: dict[str, Any] = {}
    pending = set(wanted)
    while pending:
        progressed = False
        for name in tuple(pending):
            if name not in nodes:
                raise ExtractionError(f"missing assignment {name}")
            try:
                values[name] = _safe_data(nodes[name], values)
            except ExtractionError as exc:
                if "unresolved data name" in str(exc):
                    continue
                raise
            pending.remove(name)
            progressed = True
        if not progressed:
            raise ExtractionError(
                "cyclic/unresolved assignments: " + ", ".join(sorted(pending))
            )
    return values


def _class_method(
    tree: ast.Module, class_name: str, method_name: str
) -> ast.FunctionDef:
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
    for node in ast.walk(verdict):
        if (
            isinstance(node, ast.Assign)
            and len(node.targets) == 1
            and isinstance(node.targets[0], ast.Name)
            and node.targets[0].id == "accepted"
        ):
            return node.value
    raise ExtractionError("tensor verdict has no accepted expression")


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


def _predicate_spec(expression: ast.AST) -> tuple[tuple[str, str, str], ...]:
    rows = []
    for node in ast.walk(expression):
        if isinstance(node, ast.Compare) and len(node.ops) == len(node.comparators) == 1:
            rows.append(
                (
                    ast.unparse(node.left),
                    _operator_name(node.ops[0]),
                    ast.unparse(node.comparators[0]),
                )
            )
    return tuple(sorted(rows))


EXPECTED_TENSOR_PREDICATES = tuple(
    sorted(
        (
            (
                "projector['ranks']",
                "==",
                "frozen['projector_algebra']['values']['ranks']",
            ),
            ("value", ">", "0.05"),
            ("twist['twist_residual']", "<", "S1.TOL"),
            ("max(ward['residuals'])", "<", "1e-10"),
            ("ward['source_null_residual']", "<", "S1.TOL"),
            ("locking['field_flip_residual']", "<", "S1.TOL"),
            ("locking['field_null_residual']", "<", "S1.TOL"),
            ("locking['positive_self']", ">", "0.0"),
            ("locking['locking_signs']", "==", "expected_signs"),
            ("scalar['complement_norm']", "<", "S1.TOL"),
            ("carrier['tensor_source_blocks']['shift']", ">", "0.05"),
            ("carrier['tensor_source_blocks']['shear']", ">", "0.05"),
            ("carrier['chi_only_blocks']['shift']", "==", "0.0"),
            ("carrier['chi_only_blocks']['shear']", "==", "0.0"),
            ("no_claim", "==", "frozen['no_claim']['values']"),
        )
    )
)

EXPECTED_VERDICT_AST_SHA256 = {
    "tensor_lift": "f8814817840928446ee3c413b3fdb1f4a52aac668e4d5c2402fc9ac2c631b7ce",
    "recoil": "cc9f218290b2d784411ce00e251e8edffa1c3cdd3f52cbda523be865f885fbd1",
    "typed_bridge": "3dd1f832da9c95694aeb3daf0fe65ad32277f8a7742e324ed95ff6ff9cc5791c",
}
EXPECTED_INPUT_PORT_AST_SHA256 = {
    "tensor_lift": "05cef49eb0b12c0a9590481f5e6ab8cc155d484b80c326181d53542f7821544c",
    "recoil": "8c56c5051758af57145d1ade9db7511467973265d47b09cccf7f29e17f46535e",
}


def _normalized_ast_sha256(node: ast.AST) -> str:
    normalized = ast.dump(
        node, annotate_fields=True, include_attributes=False
    )
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


def _extract_bridge_routes(tree: ast.Module) -> list[dict[str, Any]]:
    node = _assignments(tree).get("ROUTES")
    if not isinstance(node, (ast.Tuple, ast.List)):
        raise ExtractionError("Cycle-294 ROUTES is not a literal container")
    rows = []
    for item in node.elts:
        if not isinstance(item, (ast.Tuple, ast.List)) or len(item.elts) != 4:
            raise ExtractionError("Cycle-294 ROUTES row is malformed")
        route_node, path_node, pass_node, pattern_node = item.elts
        paths = [
            child.value
            for child in ast.walk(path_node)
            if isinstance(child, ast.Constant)
            and isinstance(child.value, str)
            and child.value.endswith(".py")
        ]
        if len(paths) != 1:
            raise ExtractionError("Cycle-294 route path is not unique")
        if (
            not isinstance(pattern_node, ast.Call)
            or not pattern_node.args
            or not isinstance(pattern_node.args[0], ast.Constant)
        ):
            raise ExtractionError("Cycle-294 route regex is not literal")
        rows.append(
            {
                "route": ast.literal_eval(route_node),
                "script": paths[0],
                "expected_pass": ast.literal_eval(pass_node),
                "pattern": pattern_node.args[0].value,
            }
        )
    return rows


def frozen_extraction() -> dict[str, Any]:
    trees = {
        "harness": ast.parse(
            (ROOT / HARNESS_PATH).read_text(encoding="utf-8"),
            filename=HARNESS_PATH,
        ),
        "tensor": ast.parse(
            (ROOT / TENSOR_PATH).read_text(encoding="utf-8"),
            filename=TENSOR_PATH,
        ),
        "recoil": ast.parse(
            (ROOT / RECOIL_PATH).read_text(encoding="utf-8"),
            filename=RECOIL_PATH,
        ),
        "bridge": ast.parse(
            (ROOT / BRIDGE_PATH).read_text(encoding="utf-8"),
            filename=BRIDGE_PATH,
        ),
    }
    wanted = (
        "TENSOR_LIFT_SHA256",
        "RECOIL_RECIPROCITY_SHA256",
        "TYPED_BRIDGE_SHA256",
        "TENSOR_FROZEN_EXPECTED",
        "RECOIL_OUTCOME_LABELS",
        "RECOIL_FIXTURE_INVARIANTS",
        "RECOIL_FROZEN_EXPECTED",
        "RECOIL_SWAP_FLIPPED_LABELS",
        "BRIDGE_CONTRACT_ROWS",
        "BRIDGE_OUTCOME_LABELS",
        "BRIDGE_FROZEN_EXPECTED",
    )
    values = _extract_named(trees["harness"], wanted)
    actual_pins = {
        "tensor_lift": _sha256(TENSOR_PATH),
        "recoil": _sha256(RECOIL_PATH),
        "typed_bridge": _sha256(BRIDGE_PATH),
    }
    expected_pins = {
        "tensor_lift": values["TENSOR_LIFT_SHA256"],
        "recoil": values["RECOIL_RECIPROCITY_SHA256"],
        "typed_bridge": values["TYPED_BRIDGE_SHA256"],
    }
    records = {
        "tensor_lift": values["TENSOR_FROZEN_EXPECTED"],
        "recoil": values["RECOIL_FROZEN_EXPECTED"],
        "typed_bridge": values["BRIDGE_FROZEN_EXPECTED"],
    }
    verdict_methods = {
        "tensor_lift": _class_method(
            trees["harness"], "TensorLiftAcceptance", "verdict"
        ),
        "recoil": _class_method(
            trees["harness"], "RecoilReciprocityAcceptance", "verdict"
        ),
        "typed_bridge": _class_method(
            trees["harness"], "TypedBridgeAcceptance", "verdict"
        ),
    }
    verdict_ast_sha256 = {
        name: _normalized_ast_sha256(method)
        for name, method in verdict_methods.items()
    }
    predicate_spec = _predicate_spec(
        _accepted_expression(verdict_methods["tensor_lift"])
    )
    bridge_rows = _extract_bridge_routes(trees["bridge"])
    condition = (
        actual_pins == expected_pins
        and all(
            records[name]["source_sha256"] == actual_pins[name]
            for name in records
        )
        and bridge_rows == records["typed_bridge"]["contract_rows"]
        and predicate_spec == EXPECTED_TENSOR_PREDICATES
        and verdict_ast_sha256 == EXPECTED_VERDICT_AST_SHA256
        and HARNESS_MODULE not in sys.modules
    )
    _check(
        "frozen_extraction",
        condition,
        {
            "pins": {
                name: {
                    "expected": expected_pins[name],
                    "actual": actual_pins[name],
                    "verified": expected_pins[name] == actual_pins[name],
                }
                for name in expected_pins
            },
            "frozen_record_digests": {
                name: _digest(record) for name, record in records.items()
            },
            "typed_bridge_contract_rows": bridge_rows,
            "tensor_predicates": predicate_spec,
            "verdict_ast_sha256": verdict_ast_sha256,
        },
    )
    return {
        "trees": trees,
        "values": values,
        "records": records,
        "actual_pins": actual_pins,
        "expected_pins": expected_pins,
        "bridge_rows": bridge_rows,
        "predicate_spec": predicate_spec,
        "verdict_ast_sha256": verdict_ast_sha256,
    }


def _tensor_outcomes(
    source: np.ndarray, constraint: np.ndarray
) -> dict[str, Any]:
    projectors = S1.canonical_projectors()
    calls = (
        ("projector_algebra", lambda: S1.projector_algebra_check(projectors)),
        ("orientation_twist", lambda: S1.orientation_twist_check(source, projectors)),
        ("ward_constraints", lambda: S1.ward_constraint_check(source, constraint)),
        ("response_locking", lambda: S1.response_locking_check(source)),
        (
            "scalar_only_no_overclaim",
            lambda: S1.scalar_only_no_overclaim_check(projectors),
        ),
        ("free_tensor_carrier", lambda: S1.free_tensor_carrier_gate(source)),
        ("no_claim", S1.no_claim_gate),
    )
    statuses = {}
    for name, call in calls:
        try:
            passed, _detail = call()
            statuses[name] = bool(passed)
        except Exception:
            statuses[name] = False
    plus = S1.oriented(source, +1)
    minus = S1.oriented(source, -1)
    inverse = np.linalg.inv(S1.universal_block_operator())
    projective = S1.block_norms(plus, projectors)
    signs = {}
    for eta_a in (+1, -1):
        for eta_b in (+1, -1):
            coupling = float(
                S1.oriented(source, eta_a)
                @ inverse
                @ S1.oriented(source, eta_b)
            )
            signs[f"{eta_a:+d},{eta_b:+d}"] = math.copysign(1.0, coupling)
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
            "block_norms": projective,
            "twist_residual": max(
                float(np.linalg.norm(projector @ plus + projector @ minus))
                for projector in projectors.blocks.values()
            ),
        },
        "ward_constraints": {
            "residuals": [
                float(np.linalg.norm(constraint @ S1.oriented(source, eta)))
                for eta in (+1, -1, 0)
            ],
            "source_null_residual": float(
                np.linalg.norm(S1.oriented(source, 0))
            ),
        },
        "response_locking": {
            "field_flip_residual": float(
                np.linalg.norm(inverse @ plus + inverse @ minus)
            ),
            "field_null_residual": float(
                np.linalg.norm(inverse @ S1.oriented(source, 0))
            ),
            "positive_self": float(source @ inverse @ source),
            "locking_signs": signs,
        },
        "scalar_only_no_overclaim": {
            "complement_norm": float(
                np.linalg.norm(
                    (projectors.shift + projectors.shear)
                    @ S1.oriented(S1.scalar_a1_source(), -1)
                )
            )
        },
        "free_tensor_carrier": {
            "tensor_source_blocks": S1.block_norms(source, projectors),
            "chi_only_blocks": S1.block_norms(chi_only, projectors),
        },
        "no_claim": {
            "negative_inertial_mass": False,
            "shielding": False,
            "propulsion": False,
            "reactionless_force": False,
            "physical_signed_gravity_prediction": False,
        },
    }
    return {
        name: {
            "check": "PASS" if statuses[name] else "FAIL",
            "values": _jsonable(values[name]),
        }
        for name in values
    }


def _run_recoil_fixture(
    fixture_selector: str, source_sha256: str
) -> tuple[dict[str, Any], list[dict[str, str]]]:
    coin, fswap, contact, _update, _details = S2.c315.logical_update_controls(
        S2.LABELS
    )
    factors = (
        (coin, fswap, contact)
        if fixture_selector == "canonical"
        else (fswap, coin, contact)
    )
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
                    {
                        "entry_point": name,
                        "exception": f"{type(exc).__name__}: {exc}",
                    }
                )
    pattern = re.compile(r"^(PASS|FAIL) (.*?) :: ?(.*)$")
    outcomes = []
    for line in stream.getvalue().splitlines():
        match = pattern.match(line)
        if match:
            status, label, _detail = match.groups()
            outcomes.append({"check": label, "pass": status == "PASS"})
    return (
        {
            "outcomes": outcomes,
            "fixture_invariants": {
                "cells": len(S2.ENDPOINTS),
                "directions_per_cell": [
                    len(S2.REVERSE) for _cell in S2.ENDPOINTS
                ],
                "emission_absorption_channels": len(S2.ENDPOINTS)
                * len(S2.REVERSE),
                "ordered_recoil_pairs": len(S2.REVERSE),
            },
            "fixture_selector": fixture_selector,
            "returncode": 0,
            "exceptions": exceptions,
            "source_sha256": source_sha256,
        },
        exceptions,
    )


def _run_bridge(
    source_sha256: str, contract_rows: list[dict[str, Any]]
) -> tuple[dict[str, Any], dict[str, Any]]:
    completed = subprocess.run(
        [sys.executable, str(ROOT / BRIDGE_PATH)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
        timeout=AUDIT_TIMEOUT_SEC,
    )
    pattern = re.compile(r"^(PASS|FAIL) (.*?) :: ?(.*)$")
    outcomes = []
    for line in completed.stdout.splitlines():
        match = pattern.match(line)
        if match:
            status, label, _detail = match.groups()
            outcomes.append({"check": label, "pass": status == "PASS"})
    record = {
        "outcomes": outcomes,
        "counts": {
            "pass": sum(row["pass"] for row in outcomes),
            "fail": sum(not row["pass"] for row in outcomes),
        },
        "contract_rows": copy.deepcopy(contract_rows),
        "contract_scope": "not one combined law",
        "source_sha256": source_sha256,
    }
    operational = {
        "returncode": completed.returncode,
        "stderr": completed.stderr,
    }
    return record, operational


def independent_expected(extracted: dict[str, Any]) -> dict[str, Any]:
    source, constraint = S1.tensor_source_with_constraints()
    tensor = {
        "outcomes": _tensor_outcomes(source, constraint),
        "source_sha256": extracted["actual_pins"]["tensor_lift"],
    }
    recoil, recoil_exceptions = _run_recoil_fixture(
        "canonical", extracted["actual_pins"]["recoil"]
    )
    swapped, swapped_exceptions = _run_recoil_fixture(
        "swap_coin_fswap", extracted["actual_pins"]["recoil"]
    )
    bridge, bridge_operational = _run_bridge(
        extracted["actual_pins"]["typed_bridge"],
        extracted["bridge_rows"],
    )
    equal = {
        "tensor_lift": tensor == extracted["records"]["tensor_lift"],
        "recoil": recoil == extracted["records"]["recoil"],
        "typed_bridge": bridge == extracted["records"]["typed_bridge"],
    }
    swapped_flips = tuple(
        row["check"] for row in swapped["outcomes"] if not row["pass"]
    )
    condition = (
        all(equal.values())
        and not recoil_exceptions
        and not swapped_exceptions
        and len(swapped["outcomes"]) == 20
        and swapped_flips == extracted["values"]["RECOIL_SWAP_FLIPPED_LABELS"]
        and bridge_operational["returncode"] == 0
        and not bridge_operational["stderr"]
    )
    _check(
        "independent_expected",
        condition,
        {
            "fieldwise_equal": equal,
            "record_digests": {
                "tensor_lift": _digest(tensor),
                "recoil": _digest(recoil),
                "typed_bridge": _digest(bridge),
            },
            "recoil_swapped_flips": swapped_flips,
            "bridge_operational": bridge_operational,
        },
    )
    return {
        "source": source,
        "constraint": constraint,
        "tensor": tensor,
        "recoil": recoil,
        "swapped": swapped,
        "bridge": bridge,
    }


def _drifted(record: dict[str, Any], expected_pin: str) -> bool:
    return (
        record.get("pin_verified") is not True
        or record.get("source_sha256") != expected_pin
        or record.get("expected_sha256") != expected_pin
    )


def tensor_verdict(
    record: Any, frozen: dict[str, Any], expected_pin: str
) -> str:
    try:
        if not isinstance(record, dict):
            return "REJECT"
        if _drifted(record, expected_pin):
            return "DRIFT"
        if not _finite_data(record):
            return "REJECT"
        outcomes = record.get("outcomes")
        expected = frozen["outcomes"]
        if not isinstance(outcomes, dict) or set(outcomes) != set(expected):
            return "REJECT"
        if any(
            not isinstance(outcomes.get(name), dict)
            or not isinstance(outcomes[name].get("values"), dict)
            for name in expected
        ):
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
            and all(value > 0.05 for value in twist["block_norms"].values())
            and twist["twist_residual"] < S1.TOL
            and max(ward["residuals"]) < 1.0e-10
            and ward["source_null_residual"] < S1.TOL
            and locking["field_flip_residual"] < S1.TOL
            and locking["field_null_residual"] < S1.TOL
            and locking["positive_self"] > 0.0
            and locking["locking_signs"]
            == expected["response_locking"]["values"]["locking_signs"]
            and scalar["complement_norm"] < S1.TOL
            and carrier["tensor_source_blocks"]["shift"] > 0.05
            and carrier["tensor_source_blocks"]["shear"] > 0.05
            and carrier["chi_only_blocks"]["shift"] == 0.0
            and carrier["chi_only_blocks"]["shear"] == 0.0
            and no_claim == expected["no_claim"]["values"]
        )
        return "ACCEPT" if accepted else "REJECT"
    except (
        AttributeError,
        KeyError,
        TypeError,
        ValueError,
        IndexError,
        OverflowError,
    ):
        return "REJECT"


def recoil_verdict(
    record: Any, frozen: dict[str, Any], expected_pin: str
) -> str:
    try:
        if not isinstance(record, dict):
            return "REJECT"
        if _drifted(record, expected_pin):
            return "DRIFT"
        if not _finite_data(record):
            return "REJECT"
        outcomes = record.get("outcomes")
        if not isinstance(outcomes, list) or any(
            not isinstance(row, dict) for row in outcomes
        ):
            return "REJECT"
        observed = [
            {"check": row.get("check"), "pass": row.get("pass")}
            for row in outcomes
        ]
        accepted = (
            observed == frozen["outcomes"]
            and record.get("fixture_invariants") == frozen["fixture_invariants"]
            and record.get("fixture_selector") == frozen["fixture_selector"]
            and record.get("returncode") == 0
            and not record.get("exceptions")
        )
        return "ACCEPT" if accepted else "REJECT"
    except (AttributeError, KeyError, TypeError, ValueError, IndexError):
        return "REJECT"


def bridge_verdict(
    record: Any, frozen: dict[str, Any], expected_pin: str
) -> str:
    try:
        if not isinstance(record, dict):
            return "REJECT"
        if _drifted(record, expected_pin):
            return "DRIFT"
        if not _finite_data(record):
            return "REJECT"
        outcomes = record.get("outcomes")
        if not isinstance(outcomes, list) or any(
            not isinstance(row, dict) for row in outcomes
        ):
            return "REJECT"
        observed = [
            {"check": row.get("check"), "pass": row.get("pass")}
            for row in outcomes
        ]
        accepted = (
            record.get("returncode") == 0
            and observed == frozen["outcomes"]
            and record.get("counts") == frozen["counts"]
            and record.get("contract_rows") == frozen["contract_rows"]
            and record.get("contract_scope") == frozen["contract_scope"]
        )
        return "ACCEPT" if accepted else "REJECT"
    except (AttributeError, KeyError, TypeError, ValueError, IndexError):
        return "REJECT"


def _with_pin(record: dict[str, Any], pin: str) -> dict[str, Any]:
    return {
        **copy.deepcopy(record),
        "expected_sha256": pin,
        "pin_verified": record.get("source_sha256") == pin,
    }


def verdict_semantics(
    extracted: dict[str, Any], independent: dict[str, Any]
) -> dict[str, Any]:
    rows: dict[str, dict[str, str]] = {}
    classes = (
        ("tensor_lift", tensor_verdict, independent["tensor"]),
        ("recoil", recoil_verdict, independent["recoil"]),
        ("typed_bridge", bridge_verdict, independent["bridge"]),
    )
    for name, classifier, semantic_record in classes:
        pin = extracted["expected_pins"][name]
        frozen = extracted["records"][name]
        canonical = _with_pin(semantic_record, pin)
        if name == "typed_bridge":
            canonical["returncode"] = 0
        corrupted = copy.deepcopy(canonical)
        if name == "tensor_lift":
            corrupted["outcomes"]["response_locking"]["values"][
                "positive_self"
            ] = -1.0
        else:
            corrupted["outcomes"][0]["pass"] = False
        nonfinite_nested = copy.deepcopy(canonical)
        if name == "tensor_lift":
            nonfinite_nested["outcomes"]["response_locking"]["values"][
                "positive_self"
            ] = math.inf
        else:
            nonfinite_nested["outcomes"][0]["values"] = {
                "landed_detail": math.inf
            }
        malformed_outcome = copy.deepcopy(canonical)
        if name == "tensor_lift":
            malformed_outcome["outcomes"]["projector_algebra"] = 1
        else:
            malformed_outcome["outcomes"][0] = 1
        wrong_pin = _with_pin(semantic_record, "0" * 64)
        tampered_record_pin = copy.deepcopy(canonical)
        tampered_record_pin["expected_sha256"] = "0" * 64
        rows[name] = {
            "canonical": classifier(canonical, frozen, pin),
            "corrupted": classifier(corrupted, frozen, pin),
            "nonfinite_nested": classifier(
                nonfinite_nested, frozen, pin
            ),
            "malformed_nonobject": classifier(None, frozen, pin),
            "malformed_outcome": classifier(
                malformed_outcome, frozen, pin
            ),
            "wrong_pin": classifier(wrong_pin, frozen, "0" * 64),
            "tampered_record_pin": classifier(
                tampered_record_pin, frozen, pin
            ),
        }
    swapped = _with_pin(
        independent["swapped"], extracted["expected_pins"]["recoil"]
    )
    rows["recoil"]["swapped_fixture"] = recoil_verdict(
        swapped,
        extracted["records"]["recoil"],
        extracted["expected_pins"]["recoil"],
    )
    expected = {
        name: {
            "canonical": "ACCEPT",
            "corrupted": "REJECT",
            "nonfinite_nested": "REJECT",
            "malformed_nonobject": "REJECT",
            "malformed_outcome": "REJECT",
            "wrong_pin": "DRIFT",
            "tampered_record_pin": "DRIFT",
            **({"swapped_fixture": "REJECT"} if name == "recoil" else {}),
        }
        for name in ("tensor_lift", "recoil", "typed_bridge")
    }
    agreement = rows == expected
    _check(
        "verdict_semantics",
        agreement,
        {"observed": rows, "expected": expected},
    )
    return {"agreement": agreement, "vectors": rows}


def _landed_attribute_writes(tree: ast.Module) -> list[str]:
    writes = []
    for node in ast.walk(tree):
        targets: list[ast.AST] = []
        if isinstance(node, ast.Assign):
            targets = list(node.targets)
        elif isinstance(node, ast.AnnAssign):
            targets = [node.target]
        elif isinstance(node, ast.AugAssign):
            targets = [node.target]
        for target in targets:
            for child in ast.walk(target):
                if isinstance(child, ast.Attribute):
                    root = child
                    while isinstance(root, ast.Attribute):
                        root = root.value
                    if isinstance(root, ast.Name) and root.id in {"S1", "S2"}:
                        writes.append(ast.unparse(child))
    return writes


def discipline(extracted: dict[str, Any]) -> dict[str, Any]:
    harness_tree = extracted["trees"]["harness"]
    audit_node = _assignments(harness_tree).get("AUDIT_INPUT_PATHS")
    if audit_node is None:
        raise ExtractionError("main AUDIT_INPUT_PATHS missing")
    main_inputs = ast.literal_eval(audit_node)
    tensor_accept = _class_method(
        harness_tree, "TensorLiftAcceptance", "accept"
    )
    recoil_accept = _class_method(
        harness_tree, "RecoilReciprocityAcceptance", "accept"
    )
    pin_init = _class_method(harness_tree, "_PinnedAcceptance", "__init__")
    tensor_args = tuple(argument.arg for argument in tensor_accept.args.args)
    recoil_args = tuple(argument.arg for argument in recoil_accept.args.args)
    pin_args = tuple(argument.arg for argument in pin_init.args.args)
    input_port_ast_sha256 = {
        "tensor_lift": _normalized_ast_sha256(tensor_accept),
        "recoil": _normalized_ast_sha256(recoil_accept),
    }
    source_text = (ROOT / HARNESS_PATH).read_text(encoding="utf-8")
    closure_ok = (
        isinstance(main_inputs, tuple)
        and len(main_inputs) == len(set(main_inputs))
        and set(main_inputs).issubset(set(AUDIT_INPUT_PATHS))
        and all((ROOT / path).is_file() for path in main_inputs)
    )
    api_ok = (
        tensor_args == ("self", "source_vector")
        and recoil_args == ("self", "fixture_selector")
        and pin_args == ("self",)
        and "model_port" not in source_text
        and "operator_triple" not in source_text
        and "expected_sha256: str | None" not in source_text
        and input_port_ast_sha256 == EXPECTED_INPUT_PORT_AST_SHA256
    )
    writes = _landed_attribute_writes(harness_tree)
    condition = (
        closure_ok
        and api_ok
        and extracted["predicate_spec"] == EXPECTED_TENSOR_PREDICATES
        and extracted["verdict_ast_sha256"]
        == EXPECTED_VERDICT_AST_SHA256
        and not writes
    )
    _check(
        "discipline",
        condition,
        {
            "main_input_count": len(main_inputs),
            "independent_input_count": len(AUDIT_INPUT_PATHS),
            "closure_ok": closure_ok,
            "tensor_accept_args": tensor_args,
            "recoil_accept_args": recoil_args,
            "pin_init_args": pin_args,
            "input_port_ast_sha256": input_port_ast_sha256,
            "predicate_mapping_exact": (
                extracted["predicate_spec"] == EXPECTED_TENSOR_PREDICATES
            ),
            "verdict_structure_exact": (
                extracted["verdict_ast_sha256"]
                == EXPECTED_VERDICT_AST_SHA256
            ),
            "landed_module_attribute_writes": writes,
        },
    )
    return {
        "main_input_count": len(main_inputs),
        "independent_input_count": len(AUDIT_INPUT_PATHS),
        "closure_ok": closure_ok,
        "api_ok": api_ok,
        "input_port_structure_exact": (
            input_port_ast_sha256 == EXPECTED_INPUT_PORT_AST_SHA256
        ),
        "predicate_mapping_exact": (
            extracted["predicate_spec"] == EXPECTED_TENSOR_PREDICATES
        ),
        "verdict_structure_exact": (
            extracted["verdict_ast_sha256"]
            == EXPECTED_VERDICT_AST_SHA256
        ),
        "module_writes": writes,
    }


def main() -> int:
    result: dict[str, Any] = {}
    try:
        extracted = frozen_extraction()
        independent = independent_expected(extracted)
        verdicts = verdict_semantics(extracted, independent)
        discipline_result = discipline(extracted)
        result = {
            "frozen_record_digests": {
                name: _digest(record)
                for name, record in extracted["records"].items()
            },
            "digest_agreement": {
                "tensor_lift": independent["tensor"]
                == extracted["records"]["tensor_lift"],
                "recoil": independent["recoil"]
                == extracted["records"]["recoil"],
                "typed_bridge": independent["bridge"]
                == extracted["records"]["typed_bridge"],
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
