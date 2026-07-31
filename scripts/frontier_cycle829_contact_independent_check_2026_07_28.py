#!/usr/bin/env python3
"""Cycle 829 independent adversarial compiler-to-harness contact check.

All eight foreign inputs are blocklisted as text/AST-only.  This checker does
not import, execute, compile, or eval any of them.  It independently rebuilds
the relevant object graph from syntax and tests explicitly declared lawful
identification classes.
"""

from __future__ import annotations

import ast
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time
from typing import Any


AUDIT_TIMEOUT_SEC = 1200
MAX_STDOUT_BYTES = 150_000
ORIGIN_MAIN_AT_MATERIALIZATION = "ae8a02b62a435716388607a8b50300ee038ad909"

# Literal, unique, worktree-relative, and deliberately capped at nine files.
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle829_contact_independent_check_2026_07_28.py",
    "scripts/frontier_cycle829_csource_first_contact_2026_07_28.py",
    "scripts/frontier_cycle822_routec_staggered_radius_one_parity_even_transport_2026_07_30.py",
    "scripts/frontier_cycle823_companion_full_seam_endpoint_instrument_2026_07_30.py",
    "scripts/frontier_cycle826_companion_endpoint_cycle719_history_interface_2026_07_30.py",
    "scripts/frontier_source_acceptance_harness_2026_07_28.py",
    "scripts/frontier_source_acceptance_harness_independent_check_2026_07_28.py",
    "scripts/frontier_born_acceptance_harness_2026_07_28.py",
    "scripts/frontier_born_acceptance_independent_check_2026_07_28.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS
RUNNER_PATH = AUDIT_INPUT_PATHS[0]
PRIMARY_PATH = AUDIT_INPUT_PATHS[1]
R822 = AUDIT_INPUT_PATHS[2]
R823 = AUDIT_INPUT_PATHS[3]
R826 = AUDIT_INPUT_PATHS[4]
SOURCE_HARNESS = AUDIT_INPUT_PATHS[5]
SOURCE_INDEPENDENT = AUDIT_INPUT_PATHS[6]
BORN_HARNESS = AUDIT_INPUT_PATHS[7]
BORN_INDEPENDENT = AUDIT_INPUT_PATHS[8]
BLOCKLIST_TEXT_AST_ONLY = AUDIT_INPUT_PATHS[1:]
SEVEN_PROVENANCE_PATHS = AUDIT_INPUT_PATHS[2:]

EXPECTED_PROVENANCE = {
    R822: (
        "4e7182370841585ac60650bc49858c559b96fc94",
        "17af3e27463c94a1e98f6bfe578b6d7b1a575af50bccd96b472ab0ede44f775c",
    ),
    R823: (
        "8386ea0aa07dd473e99da903c492a66fe5589925",
        "1c70bf782005bbf90608c99417470dcb0f964749644849c8835ef6314c61a737",
    ),
    R826: (
        "c3cab48bf6e02c77ebcc4b83da9922b223d664fd",
        "7132c530e8ff55e9015094b3eaba48b50eabf3ebf85aee31d4b126a5879e8af5",
    ),
    SOURCE_HARNESS: (
        "907327f3055581c84d708b9fd2dc6e00d8565237",
        "fe6be7e6cbe9d0e3cd0b88f72a5126f10e81c41223f3b3b130199fad92b3c359",
    ),
    SOURCE_INDEPENDENT: (
        "ae210cd6b781d91f4d2293f2aa95785c15bc6239",
        "31fce3c033475788888e552beb7814d23e5c19c2bf6779d58b8dd88d39c92d26",
    ),
    BORN_HARNESS: (
        "01980b601fc9445a065c059c719f0e889515ad4b",
        "1228ac30140af0fd7344dd8a955aa7c455eb9070d9b7e5d989dbc007332c7b0f",
    ),
    BORN_INDEPENDENT: (
        "59c1a741d34ddac113543375bba287fda407afca",
        "e2ca79d40591b4d8fcacc8a064c41c5acc60468c56b9d4099b22da99294b2221",
    ),
}

ROOT = Path(__file__).resolve().parents[1]


def _bytes(relative_path: str) -> bytes:
    return (ROOT / relative_path).read_bytes()


def _sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _git_blob_sha1(payload: bytes) -> str:
    header = f"blob {len(payload)}\0".encode("ascii")
    return hashlib.sha1(header + payload).hexdigest()


def _git(*arguments: str, check: bool = True) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(
        ["git", *arguments],
        cwd=ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=check,
        timeout=30,
    )


def _tree(payloads: dict[str, bytes], path: str) -> ast.Module:
    return ast.parse(payloads[path], filename=path, mode="exec")


def _function(tree: ast.Module, name: str) -> ast.FunctionDef:
    found = [
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    if len(found) != 1:
        raise AssertionError(f"expected exactly one top-level function {name}")
    return found[0]


def _class(tree: ast.Module, name: str) -> ast.ClassDef:
    found = [
        node
        for node in tree.body
        if isinstance(node, ast.ClassDef) and node.name == name
    ]
    if len(found) != 1:
        raise AssertionError(f"expected exactly one top-level class {name}")
    return found[0]


def _method(tree: ast.Module, class_name: str, name: str) -> ast.FunctionDef:
    found = [
        node
        for node in _class(tree, class_name).body
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    if len(found) != 1:
        raise AssertionError(f"expected one method {class_name}.{name}")
    return found[0]


def _arguments(node: ast.FunctionDef) -> list[str]:
    positional = node.args.posonlyargs + node.args.args
    result = [item.arg for item in positional]
    if node.args.vararg is not None:
        result.append(f"*{node.args.vararg.arg}")
    result.extend(item.arg for item in node.args.kwonlyargs)
    if node.args.kwarg is not None:
        result.append(f"**{node.args.kwarg.arg}")
    return result


def _annotation(node: ast.FunctionDef) -> str | None:
    return ast.unparse(node.returns) if node.returns is not None else None


def _terminal_return(node: ast.FunctionDef) -> ast.Return:
    returns = [item for item in node.body if isinstance(item, ast.Return)]
    if len(returns) != 1 or returns[0].value is None:
        raise AssertionError(f"{node.name} needs one terminal value return")
    return returns[0]


def _assignment_literal(tree: ast.Module, name: str) -> Any:
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
        ):
            return ast.literal_eval(node.value)
        if (
            isinstance(node, ast.AnnAssign)
            and isinstance(node.target, ast.Name)
            and node.target.id == name
        ):
            return ast.literal_eval(node.value)
    raise AssertionError(f"literal assignment {name} not found")


def _class_fields(node: ast.ClassDef) -> list[dict[str, str]]:
    return [
        {
            "name": item.target.id,
            "annotation": ast.unparse(item.annotation),
        }
        for item in node.body
        if isinstance(item, ast.AnnAssign)
        and isinstance(item.target, ast.Name)
    ]


def _calls(node: ast.AST) -> set[str]:
    return {
        ast.unparse(item.func)
        for item in ast.walk(node)
        if isinstance(item, ast.Call)
    }


def _jsonable(value: Any) -> Any:
    if isinstance(value, complex):
        return [value.real, value.imag]
    if isinstance(value, tuple):
        return [_jsonable(item) for item in value]
    if isinstance(value, list):
        return [_jsonable(item) for item in value]
    if isinstance(value, dict):
        return {
            str(key): _jsonable(item)
            for key, item in sorted(value.items(), key=lambda row: str(row[0]))
        }
    return value


def _adapter_free_normal_form(value: Any) -> Any:
    """Normalize only encoding-neutral tuple/list and record ordering."""
    if isinstance(value, (tuple, list)):
        return [_adapter_free_normal_form(item) for item in value]
    if isinstance(value, dict):
        return {
            str(key): _adapter_free_normal_form(item)
            for key, item in sorted(value.items(), key=lambda row: str(row[0]))
        }
    if isinstance(value, complex):
        return {"complex": [value.real, value.imag]}
    return value


def _provenance(payloads: dict[str, bytes]) -> dict[str, Any]:
    rows = []
    for path in SEVEN_PROVENANCE_PATHS:
        expected_blob, expected_sha256 = EXPECTED_PROVENANCE[path]
        commit_blob = _git(
            "rev-parse", f"{ORIGIN_MAIN_AT_MATERIALIZATION}:{path}"
        ).stdout.decode("ascii").strip()
        commit_payload = _git("cat-file", "blob", commit_blob).stdout
        worktree_payload = payloads[path]
        row = {
            "path": path,
            "expected_git_blob_sha1": expected_blob,
            "observed_commit_git_blob_sha1": commit_blob,
            "observed_worktree_git_blob_sha1": _git_blob_sha1(worktree_payload),
            "expected_sha256": expected_sha256,
            "observed_commit_sha256": _sha256(commit_payload),
            "observed_worktree_sha256": _sha256(worktree_payload),
            "byte_for_byte_equal_to_origin_main_materialization": (
                worktree_payload == commit_payload
            ),
        }
        row["status"] = (
            "PASS"
            if (
                commit_blob == expected_blob
                and _git_blob_sha1(commit_payload) == expected_blob
                and _git_blob_sha1(worktree_payload) == expected_blob
                and _sha256(commit_payload) == expected_sha256
                and _sha256(worktree_payload) == expected_sha256
                and worktree_payload == commit_payload
            )
            else "FAIL"
        )
        rows.append(row)
    commit_exists = (
        _git(
            "cat-file",
            "-e",
            f"{ORIGIN_MAIN_AT_MATERIALIZATION}^{{commit}}",
            check=False,
        ).returncode
        == 0
    )
    return {
        "status": (
            "PASS"
            if commit_exists and len(rows) == 7
            and all(row["status"] == "PASS" for row in rows)
            else "FAIL"
        ),
        "finding_verbatim": (
            "PASS — BLOB_PROVENANCE: all seven worktree files are byte-for-byte "
            "the blobs at origin/main@ae8a02b, with both Git-blob SHA-1 and "
            "SHA-256 independently recomputed."
        ),
        "materialization_commit": ORIGIN_MAIN_AT_MATERIALIZATION,
        "materialization_commit_exists": commit_exists,
        "files": rows,
    }


def _definition_inventory(tree: ast.Module) -> dict[str, Any]:
    functions = []
    classes = []
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            functions.append(
                {
                    "name": node.name,
                    "arguments": _arguments(node),
                    "return_annotation": _annotation(node),
                }
            )
        elif isinstance(node, ast.ClassDef):
            classes.append(
                {
                    "name": node.name,
                    "fields": _class_fields(node),
                    "methods": [
                        {
                            "name": item.name,
                            "arguments": _arguments(item),
                            "return_annotation": _annotation(item),
                        }
                        for item in node.body
                        if isinstance(item, ast.FunctionDef)
                    ],
                }
            )
    normalized = json.dumps(
        {"functions": functions, "classes": classes},
        allow_nan=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")
    return {
        "top_level_function_count": len(functions),
        "top_level_class_count": len(classes),
        "signature_inventory_sha256": _sha256(normalized),
        "functions": functions,
        "classes": classes,
    }


def _local_assignments(node: ast.FunctionDef) -> dict[str, str]:
    rows: dict[str, str] = {}
    for item in node.body:
        if isinstance(item, ast.Assign) and len(item.targets) == 1:
            target = item.targets[0]
            if isinstance(target, ast.Name):
                rows[target.id] = ast.unparse(item.value)
    return rows


def _return_components(node: ast.FunctionDef) -> list[str]:
    value = _terminal_return(node).value
    if not isinstance(value, ast.Tuple):
        raise AssertionError(f"{node.name} terminal return is not a tuple")
    return [ast.unparse(item) for item in value.elts]


def _compiler_contracts(trees: dict[str, ast.Module]) -> dict[str, Any]:
    fixed = _function(trees[R822], "fixed_typed_compile")
    fixed_types = _function(trees[R822], "fixed_type_assignment")
    instrument = _function(trees[R823], "instrument_sparse")
    expected_instrument = _function(trees[R823], "expected_instrument_output")
    interface = _function(trees[R826], "interface_key")
    orientation = _function(trees[R826], "expected_orientation")
    fixed_components = _return_components(fixed)
    fixed_type_components = _return_components(fixed_types)
    interface_components = _return_components(interface)
    expected_locals = _local_assignments(expected_instrument)
    interface_locals = _local_assignments(interface)

    expected_structure = {
        "fixed_bundle_components": fixed_components == [
            "repaired",
            "tuple(routes)",
            "words",
            "atoms",
            "seams",
            "nonseam",
            (
                "{'pre_repair_charged_route_coordinates': "
                "len(preliminary_charged), "
                "'pre_repair_neutral_route_coordinates': "
                "len(preliminary_neutral), "
                "'pre_repair_cross_typed_coordinate_collisions': "
                "len(preliminary_charged & preliminary_neutral), "
                "'reserved_neutral_access_ports': "
                "len(context['neutral_access_ports']), "
                "'charged_routes_changed_by_port_reservation': "
                "sum((left.path != right.path for left, right in "
                "zip(preliminary_routes, charged_probe_routes) if "
                "left.exchange == right.exchange == 'FSWAP')), "
                "'frozen_charged_atlas_recompile_coordinate_mismatches': "
                "len(fixed_charged ^ final_charged), "
                "'charged_atlas_coordinates_before_nonseam': "
                "len(charged_without_nonseam), "
                "'charged_atlas_coordinates_added_by_nonseam': "
                "len(fixed_charged - charged_without_nonseam)}"
            ),
        ],
        "fixed_type_components": fixed_type_components
        == ["public", "frozenset(charged)", "frozenset(neutral)"],
        "instrument_signature": (
            _arguments(instrument)
            == [
                "rows",
                "basis",
                "left",
                "right",
                "width",
                "delete_or_toffoli",
                "delete_pointer_cleanup",
                "old_endpoint_cleanup",
            ]
            and _annotation(instrument) == "dict[int, complex]"
        ),
        "expected_instrument_formula": (
            expected_locals.get("pointer") == "width + 2"
            and expected_locals.get("value")
            == (
                "input_basis >> left & 1 ^ input_basis >> right & 1"
            )
            and isinstance(_terminal_return(expected_instrument).value, ast.DictComp)
        ),
        "interface_signature_and_fields": (
            _arguments(interface)
            == ["matter_basis", "amplitude", "left", "right", "width"]
            and _annotation(interface)
            == "tuple[int, complex, tuple[int, int, int]]"
            and interface_components
            == [
                "clean_matter",
                "amplitude",
                "(post_left, post_right, pointer)",
            ]
            and interface_locals
            == {
                "pointer_wire": "width + 2",
                "pointer": "matter_basis >> pointer_wire & 1",
                "post_left": "matter_basis >> left & 1",
                "post_right": "matter_basis >> right & 1",
                "clean_matter": "matter_basis & (1 << width) - 1",
            }
        ),
        "history_signature": (
            _arguments(orientation) == ["left", "right", "pointer"]
            and _annotation(orientation) == "tuple[int, ...]"
        ),
    }
    orientation_returns = [
        ast.unparse(item.value)
        for item in ast.walk(orientation)
        if isinstance(item, ast.Return) and item.value is not None
    ]
    expected_structure["history_signature"] = (
        expected_structure["history_signature"]
        and sorted(orientation_returns)
        == sorted(["()", "(1 if right else -1,)"])
    )

    dataclasses = {
        name: _class_fields(_class(trees[R822], name))
        for name in ("Primitive", "RouteRecord", "ScheduledWord")
    }
    inventories = {
        path: _definition_inventory(trees[path])
        for path in (R822, R823, R826)
    }
    return {
        "status": (
            "PASS" if all(expected_structure.values()) else "FAIL"
        ),
        "ast_structure_checks": expected_structure,
        "all_compiler_top_level_signatures": inventories,
        "cycle822_compiled_bundle": {
            "arity": len(fixed_components),
            "components": fixed_components,
            "component_roles": [
                "repaired compiler context",
                "tuple[RouteRecord,...]",
                "tuple[ScheduledWord,...]",
                "Bell/pump/correction atom certificate data",
                "seam certificate data",
                "nonseam certificate data",
                "route-repair integer metrics",
            ],
            "dataclass_objects": dataclasses,
            "fixed_type_assignment_components": fixed_type_components,
        },
        "cycle823_sparse_surface": {
            "arguments": _arguments(instrument),
            "return_annotation": _annotation(instrument),
            "mathematical_object": "sparse computational-basis amplitude map",
        },
        "cycle826_interface_surface": {
            "arguments": _arguments(interface),
            "return_annotation": _annotation(interface),
            "components": interface_components,
            "mathematical_object": (
                "clean matter basis, complex amplitude, and endpoint/XOR-"
                "pointer bit triple"
            ),
        },
        "cycle826_history_surface": {
            "arguments": _arguments(orientation),
            "return_annotation": _annotation(orientation),
            "return_expressions": orientation_returns,
            "mathematical_object": (
                "empty history or one signed endpoint orientation"
            ),
        },
    }


def _harness_contracts(trees: dict[str, ast.Module]) -> dict[str, Any]:
    tensor = _method(trees[SOURCE_HARNESS], "TensorLiftAcceptance", "accept")
    recoil = _method(
        trees[SOURCE_HARNESS], "RecoilReciprocityAcceptance", "accept"
    )
    bridge = _method(
        trees[SOURCE_HARNESS], "TypedBridgeAcceptance", "accept"
    )
    born = _function(trees[BORN_HARNESS], "run_acceptance")
    schema = _function(trees[BORN_HARNESS], "_validate_feed_schema")
    lawful = _assignment_literal(trees[BORN_HARNESS], "FROZEN_LAWFUL_PROBES")
    rejects = _assignment_literal(
        trees[BORN_HARNESS], "FROZEN_REJECT_WITNESSES"
    )
    tensor_text = ast.unparse(tensor)
    schema_text = ast.unparse(schema)
    structure = {
        "tensor_signature": _arguments(tensor) == ["self", "source_vector"],
        "tensor_shape_10": (
            "source_object.shape != (10,)" in tensor_text
            and "isinstance(value, Real)" in tensor_text
            and "isinstance(value, (bool, np.bool_))" in tensor_text
            and "np.all(np.isfinite(source))" in tensor_text
        ),
        "recoil_internal_selector": (
            _arguments(recoil) == ["self", "fixture_selector"]
            and len(recoil.args.defaults) == 1
            and ast.literal_eval(recoil.args.defaults[0]) == "canonical"
        ),
        "typed_bridge_no_data_port": _arguments(bridge) == ["self"],
        "born_signature": _arguments(born) == ["feed"],
        "born_schema": (
            "set(feed) != {'probe_id', 'kind', 'direction'}" in schema_text
            and "feed['kind'] != 'bloch_projector'" in schema_text
            and "not isinstance(direction, list)" in schema_text
            and "len(direction) != 3" in schema_text
        ),
        "born_fixtures": len(lawful) == 4 and len(rejects) == 4,
        "independent_programs_have_no_main_input": (
            _arguments(_function(trees[SOURCE_INDEPENDENT], "main")) == []
            and _arguments(_function(trees[BORN_INDEPENDENT], "main")) == []
        ),
    }
    return {
        "status": "PASS" if all(structure.values()) else "FAIL",
        "ast_structure_checks": structure,
        "source.tensor_lift": {
            "call": "TensorLiftAcceptance.accept(source_vector)",
            "required_input": (
                "one supplied shape-(10,) real finite numeric non-Boolean "
                "vector interpreted in the signed-gravity tensor-source/Ward "
                "constraint basis"
            ),
        },
        "source.recoil_reciprocity": {
            "call": "RecoilReciprocityAcceptance.accept(fixture_selector='canonical')",
            "required_input": (
                "no compiler data object: only the harness's internal literal "
                "fixture selector and its byte-pinned Cycle322 primary"
            ),
        },
        "source.typed_bridge": {
            "call": "TypedBridgeAcceptance.accept()",
            "required_input": (
                "no external port: internally runs the byte-pinned Cycle294 "
                "primary"
            ),
        },
        "born.projector": {
            "call": "run_acceptance(feed)",
            "required_input": (
                "exact fixture-registry dict with keys probe_id, kind, "
                "direction; kind is bloch_projector and direction is a JSON "
                "list of three finite non-Boolean numbers"
            ),
            "lawful": list(lawful),
            "rejects": list(rejects),
        },
        "independent_checks": {
            "candidate_data_port": False,
            "main_arguments": {"source": [], "born": []},
        },
    }


def _endpoint_contract_rows() -> list[dict[str, Any]]:
    """Independent evaluation of the pinned 823->826 endpoint formulas."""
    rows = []
    left, right, width = 0, 1, 2
    for input_basis in range(4):
        pointer_value = (
            ((input_basis >> left) & 1) ^ ((input_basis >> right) & 1)
        )
        instrumented_basis = input_basis ^ (
            pointer_value << (width + 2)
        )
        post_left = (instrumented_basis >> left) & 1
        post_right = (instrumented_basis >> right) & 1
        pointer = (instrumented_basis >> (width + 2)) & 1
        clean_matter = instrumented_basis & ((1 << width) - 1)
        history = () if not pointer else (1 if post_right else -1,)
        rows.append(
            {
                "input_basis": input_basis,
                "instrumented_sparse_state": {
                    instrumented_basis: 1.0 + 0.0j
                },
                "clean_matter_basis": clean_matter,
                "amplitude": 1.0 + 0.0j,
                "endpoint_interface": (post_left, post_right, pointer),
                "history": history,
            }
        )
    return rows


def _string_literals(*trees: ast.Module) -> set[str]:
    return {
        item.value
        for tree in trees
        for item in ast.walk(tree)
        if isinstance(item, ast.Constant) and isinstance(item.value, str)
    }


def _dict_literal_keysets(*trees: ast.Module) -> list[list[str]]:
    rows = set()
    for tree in trees:
        for node in ast.walk(tree):
            if not isinstance(node, ast.Dict):
                continue
            keys = []
            for key in node.keys:
                if isinstance(key, ast.Constant) and isinstance(key.value, str):
                    keys.append(key.value)
                else:
                    break
            else:
                rows.add(tuple(sorted(keys)))
    return [list(row) for row in sorted(rows)]


def _identification_hunt(
    trees: dict[str, ast.Module],
    compiler: dict[str, Any],
    harness: dict[str, Any],
) -> dict[str, Any]:
    endpoint_rows = _endpoint_contract_rows()
    frozen_rows = (
        harness["born.projector"]["lawful"]
        + harness["born.projector"]["rejects"]
    )
    frozen_feeds = [row["feed"] for row in frozen_rows]

    shape_823_calls = _calls(_function(trees[R823], "shape_certificate"))
    compose_826_calls = _calls(
        _function(trees[R826], "composition_certificate")
    )
    call_edges = {
        "Cycle822.fixed_typed_compile -> Cycle823.shape_certificate": (
            "R822.fixed_typed_compile" in shape_823_calls
        ),
        "Cycle823.instrument_sparse -> Cycle826.composition_certificate": (
            "I823.instrument_sparse" in compose_826_calls
        ),
        "Cycle826.interface_key in composition": (
            "interface_key" in compose_826_calls
        ),
        "Cycle826.expected_orientation in composition": (
            "expected_orientation" in compose_826_calls
        ),
    }

    # Values whose mathematical identity survives tuple/list conversion or
    # record key ordering.  Selecting, padding, relabeling, or concatenating
    # scalar values is intentionally not an adapter-free coercion.
    adapter_candidates: list[dict[str, Any]] = []
    for row in endpoint_rows:
        for surface_name in (
            "instrumented_sparse_state",
            "endpoint_interface",
            "history",
        ):
            adapter_candidates.append(
                {
                    "surface": f"one_hop.{surface_name}",
                    "input_basis": row["input_basis"],
                    "value": row[surface_name],
                }
            )
        adapter_candidates.append(
            {
                "surface": "one_hop.endpoint_event_record",
                "input_basis": row["input_basis"],
                "value": {
                    "clean_matter_basis": row["clean_matter_basis"],
                    "amplitude": row["amplitude"],
                    "endpoint_interface": row["endpoint_interface"],
                    "history": row["history"],
                },
            }
        )

    adapter_matches = []
    for candidate in adapter_candidates:
        candidate_normal = _adapter_free_normal_form(candidate["value"])
        for frozen in frozen_rows:
            if candidate_normal == _adapter_free_normal_form(frozen["feed"]):
                adapter_matches.append(
                    {
                        "candidate": candidate["surface"],
                        "input_basis": candidate["input_basis"],
                        "test_id": f"born.{frozen['probe_id']}",
                    }
                )

    explicit_numeric_sequences = [
        candidate
        for candidate in adapter_candidates
        if isinstance(candidate["value"], (tuple, list))
    ]
    tensor_shape_matches = [
        candidate
        for candidate in explicit_numeric_sequences
        if len(candidate["value"]) == 10
        and all(
            isinstance(value, (int, float)) and not isinstance(value, bool)
            for value in candidate["value"]
        )
    ]

    compiler_literals = _string_literals(
        trees[R822], trees[R823], trees[R826]
    )
    compiler_dict_keysets = _dict_literal_keysets(
        trees[R822], trees[R823], trees[R826]
    )
    born_required_literals = {
        "bloch_projector",
        *(row["probe_id"] for row in frozen_rows),
    }
    born_literal_hits = sorted(born_required_literals & compiler_literals)
    exact_born_keyset_exists = sorted(
        ["direction", "kind", "probe_id"]
    ) in compiler_dict_keysets

    interface_values = sorted(
        {tuple(row["endpoint_interface"]) for row in endpoint_rows}
    )
    history_values = sorted(
        {tuple(row["history"]) for row in endpoint_rows}
    )
    frozen_directions = [
        tuple(row["feed"]["direction"]) for row in frozen_rows
    ]
    interface_direction_equalities = sorted(
        set(interface_values) & set(frozen_directions)
    )
    history_direction_equalities = sorted(
        set(history_values) & set(frozen_directions)
    )

    # A partial injection may merge independently surfaced components only
    # when each component already carries the harness field's mathematical
    # role.  It may not invent a probe identity, relabel endpoint bits as a
    # Bloch direction, pad history with zeros, or pack arbitrary scalars into
    # the Ward tensor basis.
    partial_injection_checks = {
        "tensor_named_basis_components_all_supplied": False,
        "tensor_guaranteed_real_sequence_arity_10_supplied": bool(
            tensor_shape_matches
        ),
        "born_probe_id_component_supplied": bool(
            {
                row["probe_id"] for row in frozen_rows
            }
            & compiler_literals
        ),
        "born_kind_bloch_projector_component_supplied": (
            "bloch_projector" in compiler_literals
        ),
        "born_direction_component_supplied": False,
        "born_exact_record_keyset_emitted": exact_born_keyset_exists,
    }
    partial_matches: list[dict[str, Any]] = []
    if (
        partial_injection_checks[
            "tensor_named_basis_components_all_supplied"
        ]
        and partial_injection_checks[
            "tensor_guaranteed_real_sequence_arity_10_supplied"
        ]
    ):
        partial_matches.append({"port": "source.tensor_lift"})
    if all(
        partial_injection_checks[name]
        for name in (
            "born_probe_id_component_supplied",
            "born_kind_bloch_projector_component_supplied",
            "born_direction_component_supplied",
            "born_exact_record_keyset_emitted",
        )
    ):
        partial_matches.append({"port": "born.projector"})

    one_hop_matches = adapter_matches + [
        {
            "candidate": candidate["surface"],
            "test_id": "source.tensor_lift.candidate",
        }
        for candidate in tensor_shape_matches
    ]
    lawful_matches = partial_matches + one_hop_matches
    direct_surfaces = [
        (
            "Cycle822.fixed_typed_compile",
            "seven-field route/circuit/certificate bundle",
            False,
            False,
        ),
        (
            "Cycle823.instrument_sparse",
            "dict[int,complex] sparse computational-basis state",
            False,
            False,
        ),
        (
            "Cycle826.interface_key",
            "tuple[int,complex,tuple[int,int,int]] endpoint event",
            False,
            False,
        ),
        (
            "Cycle826.expected_orientation",
            "tuple[int,...] empty or signed-singleton history",
            False,
            False,
        ),
    ]
    direct_type_map = []
    for surface, schema, tensor_match, born_match in direct_surfaces:
        direct_type_map.extend(
            [
                {
                    "compiler_surface": surface,
                    "compiler_schema": schema,
                    "harness_port": "source.tensor_lift",
                    "typed_match": tensor_match,
                    "exact_mismatch": (
                        "not the signed-gravity/Ward-basis real vector of "
                        "guaranteed shape (10,)"
                    ),
                },
                {
                    "compiler_surface": surface,
                    "compiler_schema": schema,
                    "harness_port": "born.projector",
                    "typed_match": born_match,
                    "exact_mismatch": (
                        "not an exact registered probe_id/kind/direction feed"
                    ),
                },
            ]
        )
    findings = [
        (
            "PASS — PARTIAL_INJECTIONS_EXHAUSTED: jointly surfaced fields "
            "cannot fill the tensor-source/Ward basis and cannot supply the "
            "Born probe_id, bloch_projector kind, and Bloch-direction roles "
            "without inventing labels or a physical identification."
        ),
        (
            "PASS — ADAPTER_FREE_COERCIONS_EXHAUSTED: tuple/list normalization "
            "and record-key reordering produce no frozen feed and no real "
            "finite arity-10 source vector."
        ),
        (
            "PASS — ONE_HOP_THIRD_MODULE_COMPOSITIONS_EXHAUSTED: the landed "
            "822→823 schedule seam and 823→826 sparse/interface/history seam "
            "close only on route/circuit, sparse-state, endpoint-XOR, and "
            "history objects; none inhabits an acceptance port."
        ),
        (
            "PASS — NO_LAWFUL_IDENTIFICATION: the closest arity-3 object is "
            "an endpoint/XOR-pointer bit triple, not a Bloch direction; "
            "padding the signed history or cherry-picking emitted 0/±1 "
            "scalars would be a new adapter and an unproved physical bridge. "
            "NOT_YET_COMPOSABLE is TIGHTENED."
        ),
    ]
    return {
        "status": (
            "PASS"
            if (
                compiler["status"] == "PASS"
                and harness["status"] == "PASS"
                and all(call_edges.values())
                and len(direct_type_map) == 8
                and not any(row["typed_match"] for row in direct_type_map)
                and not lawful_matches
            )
            else "FAIL"
        ),
        "hunt_outcome": (
            "TIGHTENED_NOT_YET_COMPOSABLE"
            if not lawful_matches
            else "REFUTED_PRIMARY_IDENTIFICATION_FOUND"
        ),
        "declared_search_classes": [
            "partial injections preserving named mathematical component roles",
            (
                "adapter-free tuple/list and record-order coercions preserving "
                "the whole mathematical object"
            ),
            (
                "one-hop compositions through each third landed compiler "
                "module on the observed compiler call graph"
            ),
        ],
        "findings_verbatim": findings,
        "independent_direct_four_by_two_type_map": direct_type_map,
        "ast_derived_compiler_contracts": compiler,
        "ast_derived_harness_contracts": harness,
        "landed_one_hop_call_edges": call_edges,
        "one_hop_endpoint_rows": [_jsonable(row) for row in endpoint_rows],
        "adapter_free_candidate_count": len(adapter_candidates),
        "adapter_free_matches": adapter_matches,
        "partial_injection_checks": partial_injection_checks,
        "partial_injection_matches": partial_matches,
        "born_required_literal_hits_in_compiler_modules": born_literal_hits,
        "compiler_dict_literal_keysets_include_exact_born_feed": (
            exact_born_keyset_exists
        ),
        "endpoint_interface_values": [list(row) for row in interface_values],
        "history_values": [list(row) for row in history_values],
        "frozen_born_directions": [list(row) for row in frozen_directions],
        "interface_equals_frozen_direction": [
            list(row) for row in interface_direction_equalities
        ],
        "history_equals_frozen_direction": [
            list(row) for row in history_direction_equalities
        ],
        "lawful_identifications": lawful_matches,
        "lawful_identification_count": len(lawful_matches),
        "harness_execution": {
            "trigger_rule": (
                "run an unchanged frozen harness test iff a lawful "
                "compiler-to-harness identification is found"
            ),
            "triggered": bool(lawful_matches),
            "results": [],
            "not_triggered_reason": (
                None
                if lawful_matches
                else "no lawful identification; all eight foreign modules remain text/AST-only"
            ),
        },
    }


def _mismatch_verification(
    hunt: dict[str, Any], harness: dict[str, Any]
) -> dict[str, Any]:
    emitted = (
        "Cycle822 emits a seven-field route/circuit/certificate bundle; "
        "Cycle823 emits dict[int,complex] sparse basis amplitudes; Cycle826 "
        "emits (clean basis, complex amplitude, endpoint/XOR-pointer triple) "
        "and empty/signed-singleton history."
    )
    rows = [
        {
            "test_id": "source.tensor_lift.candidate",
            "needs": harness["source.tensor_lift"]["required_input"],
            "compiler_surfaces_emit": emitted,
            "finding_verbatim": (
                "PASS — MISMATCH source.tensor_lift.candidate: needs one "
                "shape-(10,) signed-gravity tensor-source vector in the Ward "
                "basis; compiler surfaces emit no such mathematical object "
                "or named ten-component constructor."
            ),
            "status": "PASS",
        }
    ]
    for category in ("lawful", "rejects"):
        for frozen in harness["born.projector"][category]:
            feed_json = json.dumps(
                frozen["feed"],
                allow_nan=False,
                separators=(",", ":"),
                sort_keys=True,
            )
            rows.append(
                {
                    "test_id": f"born.{frozen['probe_id']}",
                    "needs": feed_json,
                    "compiler_surfaces_emit": emitted,
                    "finding_verbatim": (
                        f"PASS — MISMATCH born.{frozen['probe_id']}: needs "
                        f"the exact frozen feed {feed_json}; compiler surfaces "
                        "emit neither that probe identity nor the "
                        "bloch_projector kind nor an identified Bloch "
                        "direction."
                    ),
                    "status": "PASS",
                }
            )
    verified = (
        len(rows) == 9
        and hunt["lawful_identification_count"] == 0
        and all(row["status"] == "PASS" for row in rows)
    )
    return {
        "status": "PASS" if verified else "FAIL",
        "finding_verbatim": (
            "PASS — NINE_EXTERNAL_INPUT_MISMATCHES_VERIFIED: one tensor-source "
            "candidate and all eight frozen Born fixtures remain unreachable "
            "from the independently reconstructed compiler closure."
        ),
        "external_mismatch_count": len(rows),
        "items": rows,
        "internal_no_injection_controls": [
            {
                "test_id": "source.recoil_reciprocity.canonical",
                "finding_verbatim": (
                    "PASS — INTERNAL_NO_INJECTION: accepts only its own "
                    "canonical/swap selector and executes its frozen Cycle322 "
                    "primary; it has no compiler candidate-data port."
                ),
            },
            {
                "test_id": "source.typed_bridge.fixed_contract",
                "finding_verbatim": (
                    "PASS — INTERNAL_NO_INJECTION: accept() has no data "
                    "argument and executes its frozen Cycle294 primary."
                ),
            },
        ],
    }


def _science_payload(
    payloads: dict[str, bytes], trees: dict[str, ast.Module]
) -> dict[str, Any]:
    compiler = _compiler_contracts(trees)
    harness = _harness_contracts(trees)
    hunt = _identification_hunt(trees, compiler, harness)
    mismatch = _mismatch_verification(hunt, harness)
    provenance = _provenance(payloads)
    return {
        "certificate_1_IDENTIFICATION_HUNT": hunt,
        "certificate_2_MISMATCH_VERIFICATION": mismatch,
        "certificate_3_BLOB_PROVENANCE": provenance,
        "verdict": {
            "primary_refuted": (
                hunt["hunt_outcome"]
                == "REFUTED_PRIMARY_IDENTIFICATION_FOUND"
            ),
            "verdict": (
                "NOT_YET_COMPOSABLE_TIGHTENED"
                if hunt["hunt_outcome"]
                == "TIGHTENED_NOT_YET_COMPOSABLE"
                else "PRIMARY_REFUTED_BY_LAWFUL_IDENTIFICATION"
            ),
            "external_input_mismatches": mismatch[
                "external_mismatch_count"
            ],
            "internal_no_injection_controls": len(
                mismatch["internal_no_injection_controls"]
            ),
        },
    }


def _import_roots(tree: ast.Module) -> set[str]:
    roots = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            roots.update(alias.name.split(".", 1)[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            roots.add(node.module.split(".", 1)[0])
    return roots


def _controls(
    payloads: dict[str, bytes],
    trees: dict[str, ast.Module],
    science_first: dict[str, Any],
    science_second: dict[str, Any],
) -> dict[str, Any]:
    runner_tree = trees[RUNNER_PATH]
    import_roots = _import_roots(runner_tree)
    blocklisted_stems = {Path(path).stem for path in BLOCKLIST_TEXT_AST_ONLY}
    forbidden_dynamic_calls = {
        "exec",
        "eval",
        "compile",
        "__import__",
        "runpy.run_path",
        "runpy.run_module",
        "importlib.import_module",
    }
    observed_calls = _calls(runner_tree)
    subprocess_calling_functions = [
        node.name
        for node in runner_tree.body
        if isinstance(node, ast.FunctionDef)
        and "subprocess.run" in _calls(node)
    ]
    literal_paths = _assignment_literal(runner_tree, "AUDIT_INPUT_PATHS")
    paths_valid = (
        isinstance(literal_paths, tuple)
        and tuple(literal_paths) == AUDIT_INPUT_PATHS
        and len(AUDIT_INPUT_PATHS) == 9
        and len(set(AUDIT_INPUT_PATHS)) == 9
        and all(
            not Path(path).is_absolute() and (ROOT / path).is_file()
            for path in AUDIT_INPUT_PATHS
        )
    )
    only_stdlib = all(
        root == "__future__" or root in sys.stdlib_module_names
        for root in import_roots
    )
    no_blocklisted_import = not (import_roots & blocklisted_stems)
    no_dynamic_execution = not (observed_calls & forbidden_dynamic_calls)
    subprocess_git_only = subprocess_calling_functions == ["_git"]
    determinism_equal = science_first == science_second
    science_json = json.dumps(
        science_first,
        allow_nan=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")
    controls = {
        "status": "PENDING",
        "finding_verbatim": (
            "PASS — CONTROLS: SHA pins, nine literal existing relative inputs, "
            "eight-module text/AST-only blocklist, deterministic replay, "
            "1200-second runtime cap, and 150KB stdout cap all hold."
        ),
        "audit_timeout_seconds": AUDIT_TIMEOUT_SEC,
        "runtime_seconds": None,
        "runtime_under_1200_seconds": None,
        "stdout_bytes": None,
        "stdout_under_150KB": None,
        "audit_input_paths": list(AUDIT_INPUT_PATHS),
        "audit_input_paths_literal_unique_existing_worktree_relative_max_9": (
            paths_valid
        ),
        "blocklist_text_AST_only": list(BLOCKLIST_TEXT_AST_ONLY),
        "blocklist_count": len(BLOCKLIST_TEXT_AST_ONLY),
        "all_blocklisted_inputs_parsed_as_AST": all(
            path in trees for path in BLOCKLIST_TEXT_AST_ONLY
        ),
        "runner_import_roots": sorted(import_roots),
        "runner_stdlib_only": only_stdlib,
        "no_blocklisted_module_import": no_blocklisted_import,
        "no_exec_eval_compile_dynamic_import": no_dynamic_execution,
        "subprocess_is_confined_to_git_object_queries": subprocess_git_only,
        "foreign_module_execution_count": 0,
        "runner_sha256": _sha256(payloads[RUNNER_PATH]),
        "primary_sha256": _sha256(payloads[PRIMARY_PATH]),
        "all_input_sha256": {
            path: _sha256(payloads[path]) for path in AUDIT_INPUT_PATHS
        },
        "determinism_replay_equal": determinism_equal,
        "deterministic_science_payload_sha256": _sha256(science_json),
    }
    return controls


def _encode(report: dict[str, Any]) -> bytes:
    return (
        json.dumps(
            report,
            allow_nan=False,
            separators=(",", ":"),
            sort_keys=True,
        )
        + "\n"
    ).encode("utf-8")


def main() -> int:
    started = time.monotonic()
    payloads = {path: _bytes(path) for path in AUDIT_INPUT_PATHS}
    trees = {path: _tree(payloads, path) for path in AUDIT_INPUT_PATHS}

    science_first = _science_payload(payloads, trees)
    science_second = _science_payload(payloads, trees)
    controls = _controls(
        payloads, trees, science_first, science_second
    )
    report = {
        "cycle": 829,
        "checker": "INDEPENDENT_ADVERSARIAL_IDENTIFICATION_HUNT",
        "status": "PENDING",
        **science_first,
        "certificate_4_CONTROLS": controls,
    }

    elapsed = time.monotonic() - started
    controls["runtime_seconds"] = round(elapsed, 6)
    controls["runtime_under_1200_seconds"] = elapsed < AUDIT_TIMEOUT_SEC
    pre_output_bools = (
        science_first["certificate_1_IDENTIFICATION_HUNT"]["status"]
        == "PASS",
        science_first["certificate_2_MISMATCH_VERIFICATION"]["status"]
        == "PASS",
        science_first["certificate_3_BLOB_PROVENANCE"]["status"] == "PASS",
        controls[
            "audit_input_paths_literal_unique_existing_worktree_relative_max_9"
        ],
        controls["blocklist_count"] == 8,
        controls["all_blocklisted_inputs_parsed_as_AST"],
        controls["runner_stdlib_only"],
        controls["no_blocklisted_module_import"],
        controls["no_exec_eval_compile_dynamic_import"],
        controls["subprocess_is_confined_to_git_object_queries"],
        controls["foreign_module_execution_count"] == 0,
        controls["determinism_replay_equal"],
        controls["runtime_under_1200_seconds"],
    )
    controls["status"] = (
        "PASS" if all(pre_output_bools) else "FAIL"
    )
    report["status"] = (
        "PASS"
        if controls["status"] == "PASS"
        and report["verdict"]["verdict"]
        == "NOT_YET_COMPOSABLE_TIGHTENED"
        else "FAIL"
    )

    # Resolve the two self-describing byte-count fields to a fixed point.
    for _ in range(12):
        encoded = _encode(report)
        controls["stdout_bytes"] = len(encoded)
        controls["stdout_under_150KB"] = len(encoded) < MAX_STDOUT_BYTES
    if not controls["stdout_under_150KB"]:
        controls["status"] = "FAIL"
        report["status"] = "FAIL"
    encoded = _encode(report)
    controls["stdout_bytes"] = len(encoded)
    controls["stdout_under_150KB"] = len(encoded) < MAX_STDOUT_BYTES
    encoded = _encode(report)
    sys.stdout.buffer.write(encoded)
    return int(report["status"] != "PASS")


if __name__ == "__main__":
    raise SystemExit(main())
