#!/usr/bin/env python3
"""Cycle 829: first typed contact between the new compiler and frozen harnesses.

This runner is deliberately stdlib-only.  It treats all materialized compiler
and acceptance modules as byte-pinned text/AST.  It never imports or executes a
source primary.  Pure endpoint/interface functions are extracted unchanged
from the compiler AST to print the exact values available at first contact.
"""

from __future__ import annotations

import ast
import copy
import hashlib
import json
from pathlib import Path
import sys
import time
from typing import Any


AUDIT_TIMEOUT_SEC = 1500
RUNNER_PATH = "scripts/frontier_cycle829_csource_first_contact_2026_07_28.py"
AUDIT_INPUT_PATHS = (
    RUNNER_PATH,
    "scripts/frontier_cycle822_routec_staggered_radius_one_parity_even_transport_2026_07_30.py",
    "scripts/frontier_cycle823_companion_full_seam_endpoint_instrument_2026_07_30.py",
    "scripts/frontier_cycle826_companion_endpoint_cycle719_history_interface_2026_07_30.py",
    "scripts/frontier_source_acceptance_harness_2026_07_28.py",
    "scripts/frontier_source_acceptance_harness_independent_check_2026_07_28.py",
    "scripts/frontier_born_acceptance_harness_2026_07_28.py",
    "scripts/frontier_born_acceptance_independent_check_2026_07_28.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

ROOT = Path(__file__).resolve().parents[1]
BASE_HEAD = "14965c9adbd8c4beda671cf0aa5b485289c4fee6"
ORIGIN_MAIN_AT_MATERIALIZATION = "ae8a02b62a435716388607a8b50300ee038ad909"
MAX_STDOUT_BYTES = 200_000

R822 = AUDIT_INPUT_PATHS[1]
R823 = AUDIT_INPUT_PATHS[2]
R826 = AUDIT_INPUT_PATHS[3]
SOURCE_HARNESS = AUDIT_INPUT_PATHS[4]
SOURCE_INDEPENDENT = AUDIT_INPUT_PATHS[5]
BORN_HARNESS = AUDIT_INPUT_PATHS[6]
BORN_INDEPENDENT = AUDIT_INPUT_PATHS[7]

# These are the four executable source-law surfaces pinned by the two frozen
# acceptance programs.  Cycle 829 never imports or executes any of them.
SOURCE_PRIMARY_BLOCKLIST = (
    "scripts/signed_gravity_oriented_tensor_source_lift.py",
    "scripts/two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18.py",
    "scripts/physical_m2_gravity_source_bridge_tournament_synthesis_cycle294_2026_07_17.py",
    "scripts/physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18.py",
)

PROVENANCE = {
    R822: {
        "role": "Cycle 822 typed radius-one physical-M2 compiler tournament",
        "origin_commit": "18b67b6a0e433f26e02be40ba09020bbb3b6375d",
        "git_blob_sha1": "4e7182370841585ac60650bc49858c559b96fc94",
        "sha256": "17af3e27463c94a1e98f6bfe578b6d7b1a575af50bccd96b472ab0ede44f775c",
    },
    R823: {
        "role": "Cycle 823 companion full-seam endpoint instrument",
        "origin_commit": "8b1bc218dd4596d4666620228ce7d33a532e6ca6",
        "git_blob_sha1": "8386ea0aa07dd473e99da903c492a66fe5589925",
        "sha256": "1c70bf782005bbf90608c99417470dcb0f964749644849c8835ef6314c61a737",
    },
    R826: {
        "role": "Cycle 826 endpoint/history composition interface",
        "origin_commit": "23632f5f47b631ea0c62bc9376b8282d239f9def",
        "git_blob_sha1": "c3cab48bf6e02c77ebcc4b83da9922b223d664fd",
        "sha256": "7132c530e8ff55e9015094b3eaba48b50eabf3ebf85aee31d4b126a5879e8af5",
    },
    SOURCE_HARNESS: {
        "role": "frozen source acceptance harness",
        "origin_commit": "b28cddc98285055274d63e3cbbc24be8b6b6b76d",
        "git_blob_sha1": "907327f3055581c84d708b9fd2dc6e00d8565237",
        "sha256": "fe6be7e6cbe9d0e3cd0b88f72a5126f10e81c41223f3b3b130199fad92b3c359",
    },
    SOURCE_INDEPENDENT: {
        "role": "frozen independent source-harness check",
        "origin_commit": "b28cddc98285055274d63e3cbbc24be8b6b6b76d",
        "git_blob_sha1": "ae210cd6b781d91f4d2293f2aa95785c15bc6239",
        "sha256": "31fce3c033475788888e552beb7814d23e5c19c2bf6779d58b8dd88d39c92d26",
    },
    BORN_HARNESS: {
        "role": "frozen Born acceptance harness",
        "origin_commit": "33ddfdcac593810db79332a0fe3b67a2627de2fd",
        "git_blob_sha1": "01980b601fc9445a065c059c719f0e889515ad4b",
        "sha256": "1228ac30140af0fd7344dd8a955aa7c455eb9070d9b7e5d989dbc007332c7b0f",
    },
    BORN_INDEPENDENT: {
        "role": "frozen independent Born-harness check",
        "origin_commit": "33ddfdcac593810db79332a0fe3b67a2627de2fd",
        "git_blob_sha1": "59c1a741d34ddac113543375bba287fda407afca",
        "sha256": "e2ca79d40591b4d8fcacc8a064c41c5acc60468c56b9d4099b22da99294b2221",
    },
}


def _bytes(relative_path: str) -> bytes:
    return (ROOT / relative_path).read_bytes()


def _sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _git_blob_sha1(payload: bytes) -> str:
    header = f"blob {len(payload)}\0".encode("ascii")
    return hashlib.sha1(header + payload).hexdigest()


def _tree(relative_path: str) -> ast.Module:
    return ast.parse(
        _bytes(relative_path),
        filename=relative_path,
        mode="exec",
    )


def _assignment_literal(tree: ast.Module, name: str) -> Any:
    for node in ast.walk(tree):
        if (
            isinstance(node, (ast.Assign, ast.AnnAssign))
            and (
                (
                    isinstance(node, ast.Assign)
                    and any(
                        isinstance(target, ast.Name) and target.id == name
                        for target in node.targets
                    )
                )
                or (
                    isinstance(node, ast.AnnAssign)
                    and isinstance(node.target, ast.Name)
                    and node.target.id == name
                )
            )
        ):
            return ast.literal_eval(node.value)
    raise ValueError(f"literal assignment {name!r} not found")


def _function_node(tree: ast.Module, name: str) -> ast.FunctionDef:
    matches = [
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    if len(matches) != 1:
        raise ValueError(f"expected one top-level function {name!r}")
    return matches[0]


def _method_node(
    tree: ast.Module, class_name: str, method_name: str
) -> ast.FunctionDef:
    classes = [
        node
        for node in tree.body
        if isinstance(node, ast.ClassDef) and node.name == class_name
    ]
    if len(classes) != 1:
        raise ValueError(f"expected one class {class_name!r}")
    matches = [
        node
        for node in classes[0].body
        if isinstance(node, ast.FunctionDef) and node.name == method_name
    ]
    if len(matches) != 1:
        raise ValueError(f"expected one method {class_name}.{method_name}")
    return matches[0]


def _arguments(node: ast.FunctionDef) -> list[str]:
    return [
        argument.arg
        for argument in (
            node.args.posonlyargs + node.args.args + node.args.kwonlyargs
        )
    ]


def _return_expressions(node: ast.FunctionDef) -> list[str]:
    return [
        ast.unparse(child.value)
        for child in ast.walk(node)
        if isinstance(child, ast.Return) and child.value is not None
    ]


def _extract_unchanged_function(
    tree: ast.Module, name: str
) -> tuple[Any, str]:
    """Compile exactly one pure compiler function from its frozen AST."""
    node = copy.deepcopy(_function_node(tree, name))
    node.decorator_list = []
    module = ast.fix_missing_locations(ast.Module(body=[node], type_ignores=[]))
    namespace: dict[str, Any] = {}
    exec(compile(module, filename=f"<frozen:{name}>", mode="exec"), namespace)
    normalized = ast.dump(node, annotate_fields=True, include_attributes=False)
    return namespace[name], hashlib.sha256(normalized.encode()).hexdigest()


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


def _self_import_roots(tree: ast.Module) -> tuple[str, ...]:
    roots = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            roots.update(alias.name.split(".", 1)[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            roots.add(node.module.split(".", 1)[0])
    return tuple(sorted(roots))


def _inventory() -> list[dict[str, Any]]:
    rows = []
    for path, expected in PROVENANCE.items():
        payload = _bytes(path)
        rows.append(
            {
                "path": path,
                **expected,
                "observed_git_blob_sha1": _git_blob_sha1(payload),
                "observed_sha256": _sha256(payload),
                "bytes": len(payload),
                "byte_exact": (
                    _git_blob_sha1(payload) == expected["git_blob_sha1"]
                    and _sha256(payload) == expected["sha256"]
                ),
            }
        )
    return rows


def _compiler_values_and_contracts() -> tuple[dict[str, Any], dict[str, Any]]:
    tree822 = _tree(R822)
    tree823 = _tree(R823)
    tree826 = _tree(R826)

    expected_output, expected_output_ast_sha256 = _extract_unchanged_function(
        tree823, "expected_instrument_output"
    )
    interface_key, interface_key_ast_sha256 = _extract_unchanged_function(
        tree826, "interface_key"
    )
    expected_orientation, expected_orientation_ast_sha256 = (
        _extract_unchanged_function(tree826, "expected_orientation")
    )

    endpoint_rows = []
    for input_basis in range(4):
        instrumented = expected_output(
            {input_basis: 1.0 + 0.0j},
            input_basis,
            0,
            1,
            2,
        )
        outputs = []
        for matter_basis, amplitude in sorted(instrumented.items()):
            clean_matter, coefficient, interface = interface_key(
                matter_basis, amplitude, 0, 1, 2
            )
            left, right, pointer = interface
            outputs.append(
                {
                    "clean_matter_basis": clean_matter,
                    "amplitude": _jsonable(coefficient),
                    "endpoint_interface": [left, right, pointer],
                    "history": list(
                        expected_orientation(left, right, pointer)
                    ),
                }
            )
        endpoint_rows.append(
            {
                "input_basis": input_basis,
                "instrumented_sparse_state": _jsonable(instrumented),
                "outputs": outputs,
            }
        )

    fixed_compile = _function_node(tree822, "fixed_typed_compile")
    instrument_sparse = _function_node(tree823, "instrument_sparse")
    interface_node = _function_node(tree826, "interface_key")
    values = {
        "held_representative_endpoint_rows": endpoint_rows,
        "value_origin": (
            "unchanged frozen AST functions "
            "Cycle823.expected_instrument_output -> "
            "Cycle826.interface_key -> Cycle826.expected_orientation"
        ),
    }
    contracts = {
        "cycle822.fixed_typed_compile": {
            "arguments": _arguments(fixed_compile),
            "return_expressions": _return_expressions(fixed_compile),
        },
        "cycle823.instrument_sparse": {
            "arguments": _arguments(instrument_sparse),
            "declared_runtime_output": "dict[int, complex] sparse basis state",
            "endpoint_pointer_rule": "post_left XOR post_right on wire width+2",
        },
        "cycle826.interface_key": {
            "arguments": _arguments(interface_node),
            "return_expressions": _return_expressions(interface_node),
            "declared_runtime_output": (
                "tuple[clean_matter_basis:int, amplitude:complex, "
                "tuple[post_left:int, post_right:int, pointer:int]]"
            ),
        },
        "cycle826.history": {
            "declared_runtime_output": "tuple[orientation:int, ...]",
            "reachable_values_on_four_endpoint_rows": [[], [-1], [1]],
        },
        "extracted_function_ast_sha256": {
            "cycle823.expected_instrument_output": expected_output_ast_sha256,
            "cycle826.interface_key": interface_key_ast_sha256,
            "cycle826.expected_orientation": expected_orientation_ast_sha256,
        },
    }
    return values, contracts


def _harness_contracts() -> tuple[dict[str, Any], list[dict[str, Any]]]:
    source_tree = _tree(SOURCE_HARNESS)
    born_tree = _tree(BORN_HARNESS)

    tensor_args = _arguments(
        _method_node(source_tree, "TensorLiftAcceptance", "accept")
    )
    recoil_args = _arguments(
        _method_node(source_tree, "RecoilReciprocityAcceptance", "accept")
    )
    bridge_args = _arguments(
        _method_node(source_tree, "TypedBridgeAcceptance", "accept")
    )
    born_args = _arguments(_function_node(born_tree, "run_acceptance"))
    honest_keys = _assignment_literal(source_tree, "honest_keys")
    lawful = _assignment_literal(born_tree, "FROZEN_LAWFUL_PROBES")
    rejects = _assignment_literal(born_tree, "FROZEN_REJECT_WITNESSES")

    contracts = {
        "source.tensor_lift": {
            "call": "TensorLiftAcceptance.accept(source_vector)",
            "arguments": tensor_args,
            "candidate_input_port": honest_keys["harness_input_ports"][
                "tensor_lift"
            ],
            "required_input": (
                "one-dimensional shape-(10,) vector; every element real, "
                "finite, numeric, and non-Boolean"
            ),
        },
        "source.recoil_reciprocity": {
            "call": "RecoilReciprocityAcceptance.accept(fixture_selector)",
            "arguments": recoil_args,
            "candidate_input_port": honest_keys["harness_input_ports"]["recoil"],
            "required_input": (
                "internal frozen Cycle322 primary; optional literal selector "
                "'canonical' or 'swap_coin_fswap' is not a candidate data port"
            ),
        },
        "source.typed_bridge": {
            "call": "TypedBridgeAcceptance.accept()",
            "arguments": bridge_args,
            "candidate_input_port": honest_keys["harness_input_ports"][
                "typed_bridge"
            ],
            "required_input": (
                "no external port; internally executes the byte-pinned "
                "Cycle294 source-bridge primary"
            ),
        },
        "born.projector": {
            "call": "run_acceptance(feed)",
            "arguments": born_args,
            "candidate_input_port": True,
            "required_input": (
                "exact registered object {probe_id:str, "
                "kind:'bloch_projector', direction:list[3]}; lawful feeds are "
                "the four frozen axes and reject feeds are four frozen "
                "malformations"
            ),
            "lawful_probe_ids": [row["probe_id"] for row in lawful],
            "reject_probe_ids": [row["probe_id"] for row in rejects],
        },
        "independent_checks": {
            "candidate_input_port": False,
            "role": (
                "frozen implementation audits; they consume the primary "
                "harnesses and source primaries, not compiler candidate data"
            ),
        },
    }

    tests = [
        {
            "test_id": "source.tensor_lift.candidate",
            "harness": SOURCE_HARNESS,
            "required_input": contracts["source.tensor_lift"]["required_input"],
        },
        {
            "test_id": "source.recoil_reciprocity.canonical",
            "harness": SOURCE_HARNESS,
            "required_input": contracts["source.recoil_reciprocity"][
                "required_input"
            ],
        },
        {
            "test_id": "source.typed_bridge.fixed_contract",
            "harness": SOURCE_HARNESS,
            "required_input": contracts["source.typed_bridge"]["required_input"],
        },
    ]
    for row in lawful + rejects:
        tests.append(
            {
                "test_id": f"born.{row['probe_id']}",
                "harness": BORN_HARNESS,
                "required_input": json.dumps(
                    row["feed"],
                    allow_nan=False,
                    separators=(",", ":"),
                    sort_keys=True,
                ),
            }
        )
    return contracts, tests


def _correspondence_table() -> list[dict[str, Any]]:
    return [
        {
            "compiler_surface": "Cycle823.instrument_sparse",
            "compiler_supplies": "dict[int, complex] sparse endpoint state",
            "harness_port": "source.tensor_lift.source_vector",
            "harness_requires": "real finite non-Boolean shape-(10,) vector",
            "typed_match": False,
            "exact_mismatch": (
                "no compiler source/gravity projection, Ward tensor basis, or "
                "ten-component source-vector constructor exists"
            ),
        },
        {
            "compiler_surface": "Cycle826.interface_key",
            "compiler_supplies": (
                "(clean_matter_basis:int, amplitude:complex, "
                "(left:int,right:int,pointer:int))"
            ),
            "harness_port": "source.recoil_reciprocity",
            "harness_requires": (
                "no candidate port; frozen internal Cycle322 execution"
            ),
            "typed_match": False,
            "exact_mismatch": (
                "endpoint/event values cannot replace the internally pinned "
                "recoil primary or its literal fixture selector"
            ),
        },
        {
            "compiler_surface": "Cycle822.fixed_typed_compile",
            "compiler_supplies": (
                "compiled context/routes/words and bounded seam certificates"
            ),
            "harness_port": "source.typed_bridge",
            "harness_requires": (
                "no candidate port; frozen internal Cycle294 subprocess"
            ),
            "typed_match": False,
            "exact_mismatch": (
                "the harness has no injection point for compiled routes or "
                "endpoint values"
            ),
        },
        {
            "compiler_surface": (
                "Cycle826.interface_key + expected_orientation"
            ),
            "compiler_supplies": (
                "endpoint triple and history tuple in {(),(-1,),(1,)}"
            ),
            "harness_port": "born.projector.feed",
            "harness_requires": (
                "exact registered probe_id/kind/direction[3] Bloch object"
            ),
            "typed_match": False,
            "exact_mismatch": (
                "no Bloch direction, projector probe identity, Born weight, "
                "or registry feed is emitted; inventing them would be new law"
            ),
        },
        {
            "compiler_surface": "Cycle826 history/controller hook",
            "compiler_supplies": (
                "one fixed controller composition and decoded orientation tuple"
            ),
            "harness_port": "source/Born evolution hooks",
            "harness_requires": (
                "none exposed: frozen source primaries and Born bridge own "
                "their execution internally"
            ),
            "typed_match": False,
            "exact_mismatch": (
                "the acceptance APIs expose no evolution-hook injection port"
            ),
        },
    ]


def _unreachable_tests(
    tests: list[dict[str, Any]]
) -> list[dict[str, Any]]:
    reason_by_prefix = {
        "source.tensor_lift": (
            "missing typed compiler map to the ten-component tensor source"
        ),
        "source.recoil": (
            "harness has no candidate data port and internally owns Cycle322"
        ),
        "source.typed_bridge": (
            "harness has no candidate data port and internally owns Cycle294"
        ),
        "born.": (
            "compiler emits no exact registered Bloch feed or direction"
        ),
    }
    rows = []
    for test in tests:
        reason = next(
            value
            for prefix, value in reason_by_prefix.items()
            if test["test_id"].startswith(prefix)
        )
        rows.append({**test, "gap": reason})
    return rows


def _science_payload() -> dict[str, Any]:
    compiler_values, compiler_contracts = _compiler_values_and_contracts()
    harness_contracts, tests = _harness_contracts()
    correspondence = _correspondence_table()
    matched = [row for row in correspondence if row["typed_match"]]
    runnable = []
    unreachable = _unreachable_tests(tests)
    verdict = (
        "NOT_YET_COMPOSABLE"
        if not matched
        else (
            "FIRST_CONTACT_CLEAN"
            if all(row["status"] == "PASS" for row in runnable)
            else "FIRST_CONTACT_MIXED"
        )
    )
    return {
        "certificate_B_identification_map": {
            "compiler_contracts": compiler_contracts,
            "compiler_values": compiler_values,
            "harness_contracts": harness_contracts,
            "correspondence_table": correspondence,
            "typed_matches": matched,
            "typed_match_count": len(matched),
        },
        "certificate_C_run": {
            "rule": (
                "execute frozen harness logic only when a compiler output "
                "exactly inhabits its declared candidate input type"
            ),
            "runnable_count": len(runnable),
            "pass": 0,
            "fail": 0,
            "results": runnable,
            "unchanged_harness_execution": "none: no typed input correspondence",
        },
        "certificate_D_unreachable_census": {
            "count": len(unreachable),
            "tests": unreachable,
        },
        "certificate_E_verdict": {
            "verdict": verdict,
            "exact_reason": (
                "The identification map is empty: endpoint sparse states, "
                "endpoint/XOR triples, and history tuples inhabit none of the "
                "frozen source-vector or registered-Bloch-feed ports; the "
                "other source harnesses expose no candidate injection port."
            ),
            "runnable": len(runnable),
            "pass": 0,
            "fail": 0,
            "unreachable": len(unreachable),
        },
    }


def main() -> int:
    started = time.monotonic()
    inventory = _inventory()
    science_first = _science_payload()
    science_second = _science_payload()
    science_json = json.dumps(
        science_first,
        allow_nan=False,
        separators=(",", ":"),
        sort_keys=True,
    )
    deterministic_sha256 = _sha256(science_json.encode("utf-8"))

    self_tree = _tree(RUNNER_PATH)
    import_roots = _self_import_roots(self_tree)
    blocklisted_module_names = {
        Path(path).stem for path in SOURCE_PRIMARY_BLOCKLIST
    }
    declared_paths_exist = all(
        not Path(path).is_absolute() and (ROOT / path).is_file()
        for path in AUDIT_INPUT_PATHS
    )
    blocklist_paths_exist = all(
        not Path(path).is_absolute() and (ROOT / path).is_file()
        for path in SOURCE_PRIMARY_BLOCKLIST
    )
    byte_exact = all(row["byte_exact"] for row in inventory)
    only_stdlib_imports = all(
        root == "__future__" or root in sys.stdlib_module_names
        for root in import_roots
    )
    no_blocklisted_imports = not (
        set(import_roots) & blocklisted_module_names
    )

    report = {
        "cycle": 829,
        "wall": "C_source",
        "certificate_A_inventory": {
            "base_head": BASE_HEAD,
            "origin_main_at_materialization": ORIGIN_MAIN_AT_MATERIALIZATION,
            "materialization": (
                "exact origin/main blobs copied to tracked scripts paths"
            ),
            "files": inventory,
        },
        **science_first,
        "certificate_F_controls": {
            "status": "PENDING",
            "audit_timeout_seconds": AUDIT_TIMEOUT_SEC,
            "runtime_seconds": None,
            "runtime_under_1500_seconds": None,
            "stdout_bytes": None,
            "stdout_under_200KB": None,
            "audit_input_paths": list(AUDIT_INPUT_PATHS),
            "audit_input_paths_literal_unique_existing_worktree_relative": (
                len(AUDIT_INPUT_PATHS) == len(set(AUDIT_INPUT_PATHS))
                and declared_paths_exist
            ),
            "materialized_sha256_and_git_blob_sha1_exact": byte_exact,
            "runner_sha256": _sha256(_bytes(RUNNER_PATH)),
            "source_primary_blocklist": list(SOURCE_PRIMARY_BLOCKLIST),
            "source_primary_blocklist_paths_existing": blocklist_paths_exist,
            "source_primary_policy": (
                "BLOCKLIST: never imported or executed; acceptance/compiler "
                "copies are text/AST only; glue is local and declared"
            ),
            "runner_import_roots": list(import_roots),
            "runner_stdlib_only": only_stdlib_imports,
            "no_blocklisted_primary_import": no_blocklisted_imports,
            "determinism_replay_equal": science_first == science_second,
            "deterministic_science_payload_sha256": deterministic_sha256,
            "harness_code_frozen": byte_exact,
        },
    }

    elapsed = time.monotonic() - started
    controls = report["certificate_F_controls"]
    controls["runtime_seconds"] = round(elapsed, 6)
    controls["runtime_under_1500_seconds"] = elapsed < AUDIT_TIMEOUT_SEC

    for _ in range(8):
        encoded = (
            json.dumps(
                report,
                allow_nan=False,
                separators=(",", ":"),
                sort_keys=True,
            )
            + "\n"
        ).encode("utf-8")
        controls["stdout_bytes"] = len(encoded)
        controls["stdout_under_200KB"] = len(encoded) < MAX_STDOUT_BYTES

    control_booleans = (
        controls[
            "audit_input_paths_literal_unique_existing_worktree_relative"
        ],
        controls["materialized_sha256_and_git_blob_sha1_exact"],
        controls["source_primary_blocklist_paths_existing"],
        controls["runner_stdlib_only"],
        controls["no_blocklisted_primary_import"],
        controls["determinism_replay_equal"],
        controls["harness_code_frozen"],
        controls["runtime_under_1500_seconds"],
        controls["stdout_under_200KB"],
    )
    controls["status"] = "PASS" if all(control_booleans) else "FAIL"
    encoded = (
        json.dumps(
            report,
            allow_nan=False,
            separators=(",", ":"),
            sort_keys=True,
        )
        + "\n"
    ).encode("utf-8")
    controls["stdout_bytes"] = len(encoded)
    controls["stdout_under_200KB"] = len(encoded) < MAX_STDOUT_BYTES
    encoded = (
        json.dumps(
            report,
            allow_nan=False,
            separators=(",", ":"),
            sort_keys=True,
        )
        + "\n"
    ).encode("utf-8")
    sys.stdout.buffer.write(encoded)
    return int(controls["status"] != "PASS")


if __name__ == "__main__":
    raise SystemExit(main())
