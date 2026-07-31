#!/usr/bin/env python3
"""Cycle 823: fixed-b discharge of H_TEMPLATE_PREIMAGE_ZONE_CLASS.

The Cycle-817 primary/checker pair and constructor witnesses are inert audit
inputs: this stdlib-only runner reads their bytes/text and parses their ASTs,
but never imports or executes them.  The finite template signatures used by
the discharge are frozen below as a literal certificate and checked against
independent digests before use.
"""
from __future__ import annotations

import ast
import base64
from collections import Counter
from hashlib import sha1, sha256
import json
from pathlib import Path
import sys
from time import perf_counter
import zlib


AUDIT_TIMEOUT_SEC = 1500
STDOUT_LIMIT_BYTES = 200 * 1024
ROOT = Path(__file__).resolve().parents[1]
SELF_PATH = (
    "scripts/frontier_cycle823_hypothesis_discharge_2026_07_28.py"
)

PRIMARY_817 = (
    "scripts/frontier_cycle817_general_b_sector_theorem_2026_07_28.py"
)
CHECKER_817 = (
    "scripts/frontier_cycle817_theorem_independent_check_2026_07_28.py"
)
CYCLE719 = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py"
)
CYCLE719_LOCAL = (
    "scripts/frontier_cycle719_local_handshake_controller_core_2026_07_26.py"
)
CYCLE739 = "scripts/frontier_cycle739_identity_discharge_2026_07_28.py"
SOURCE_FINALIZER = (
    "scripts/frontier_cycle719_source_local_finalizer_core_2026_07_26.py"
)

AUDIT_INPUT_PATHS = (
    PRIMARY_817,
    CHECKER_817,
    CYCLE719,
    CYCLE719_LOCAL,
    CYCLE739,
    SOURCE_FINALIZER,
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

# The Cycle-817 pair are evidence only and are forbidden executable imports.
BLOCKLIST = tuple(Path(path).stem for path in (PRIMARY_817, CHECKER_817))
BLOCKED_DYNAMIC_CALLS = frozenset(
    ("__import__", "compile", "eval", "exec", "run_module", "run_path")
)

EXPECTED_PROVENANCE = {
    PRIMARY_817: {
        "sha256":
            "469a0af17b19bb6a35ac5356b5c143f6027af05c412f92a5b349f09c0452c7a4",
        "blob": "01045658578074e6d3c496ff09b3169381596728",
    },
    CHECKER_817: {
        "sha256":
            "91180f1f16400f9056a8ee1076cf8b2dda7dd8151a4e8e755a3ecbd581c313f7",
        "blob": "3c5a32dd91681db119692140d826a1e7063dd1e5",
    },
    CYCLE719: {
        "sha256":
            "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
        "blob": "c123b8d681c3d76fce08ef13d7673622deac64ad",
    },
    CYCLE719_LOCAL: {
        "sha256":
            "0008837e938fdc589473967763c5319aeb5fc4996bd8380d5d33c3ec61062691",
        "blob": "3add288d1b7de5bcc45f5ef8f88f3cfb98105b8f",
    },
    CYCLE739: {
        "sha256":
            "c4fe65ae06f77665379c5e96f4951fb9a73919a000d6e18004b9e244beb6b88e",
        "blob": "ea7dbca69ea7ebf860573395053d2089626d4c36",
    },
    SOURCE_FINALIZER: {
        "sha256":
            "b514b0e20197bb0ce5e5440b4b0c1f2a0f74a1962b127e8a4e4a2e97c8f86a1a",
        "blob": "97cc3de7b95e341326c404047a321dbe2c825eda",
    },
}

HYPOTHESIS_NAME = "H_TEMPLATE_PREIMAGE_ZONE_CLASS"
EXPECTED_HYPOTHESIS = {
    "name": HYPOTHESIS_NAME,
    "predicate": (
        "the actual fixed source/finalizer words lie in the capacity-"
        "independent source support; every bank-template operand lies in "
        "one 131-wire bank block; every pair-template operand lies in its "
        "declared left-bank/right-bank/191-wire link-half zone; the cross "
        "predecessor offset is in [0,131); and the finalizer word is bank-"
        "count independent"
    ),
    "role": (
        "exact condition for promoting the verified affine zone relabeling "
        "and the Cycle-738 transfer to the actual emitted words"
    ),
    "mechanical_fixed_b": True,
    "general_b_status": "OPEN",
}
EXPECTED_CHECKER_IDENTITY = (
    "The actual fixed source/finalizer words lie in the capacity-independent "
    "source support; every bank template operand lies in one 131-wire bank "
    "block; every pair-template operand lies in its declared left-bank/"
    "right-bank/191-wire link-half zone; the cross predecessor offset is in "
    "[0,131); and the finalizer word is bank-count independent."
)

SOURCE_WIDTH = 41
BANK_WIDTH = 131
LINK_AUX_WIDTH = 191
LINK_WIDTH = 2 * LINK_AUX_WIDTH
SOURCE_ANCHOR_SUPPORT = (0, SOURCE_WIDTH + BANK_WIDTH)
CROSS_PREDECESSOR_OFFSET = 1
ARITY = {"X": 1, "CNOT": 2, "TOF": 3}
PAIR_TEMPLATE_KIND = {
    "handoff_forward": "handoff",
    "relay_latch": "relay",
    "relay_swap": "relay",
    "relay_unlatch": "relay",
    "handoff_return": "handoff",
}
DISCHARGE_BANKS = tuple(range(3, 11))
PATTERN_TEST_BANK = 11

EXPECTED_TEMPLATE_METADATA = {
    "bank_packet": {
        "digest":
            "e29feaeadd5e036830a4b269b235dec0ff0fb788ab3ee6e25eac7197de8377cc",
        "gates": 492,
        "operands": 1173,
    },
    "finalizer": {
        "digest":
            "13924ee1e0079c38c8ccb00d519ac0896d4c8b886802e857632ccaed3cbcacff",
        "gates": 11,
        "operands": 29,
    },
    "handoff_forward": {
        "digest":
            "1dec5f1fce15076cee9b40a8af734e67914ce2e2850a29f5ad5d25b717e3fe08",
        "gates": 752,
        "operands": 1542,
    },
    "handoff_return": {
        "digest":
            "0dbbea684594a8c77e95c060635e7a9d9a970dedb5ebea85e93638a106b30765",
        "gates": 593,
        "operands": 1223,
    },
    "relay_latch": {
        "digest":
            "a808ac9e7354239a8f718e50619df96ed3345edf0ec48afc0a2fa37c538fe7bf",
        "gates": 369,
        "operands": 755,
    },
    "relay_swap": {
        "digest":
            "21127bbeee2260bbcc8b1c52d97410de58438b90eb0f00981a6e03fe691dedc4",
        "gates": 12,
        "operands": 28,
    },
    "relay_unlatch": {
        "digest":
            "fcdd745953d6bbe5a4add33ecfac6cc806c30f6c59a53a9e423a93550d33eab8",
        "gates": 367,
        "operands": 749,
    },
    "source": {
        "digest":
            "b8f5ca17203c5f5eff0289642998f9118e843474bd8cf318891b75dc91cf68b6",
        "gates": 5,
        "operands": 12,
    },
}

# Filled by the next incremental certificate commit.
TEMPLATE_PREIMAGE_B85 = ""


def stable_json_bytes(value: object) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    ).encode()


def stable_digest(value: object) -> str:
    return sha256(stable_json_bytes(value)).hexdigest()


def git_blob_sha1(data: bytes) -> str:
    return sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def call_name(node: ast.AST) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        prefix = call_name(node.value)
        return f"{prefix}.{node.attr}" if prefix else node.attr
    return ""


def function_node(tree: ast.Module, name: str) -> ast.FunctionDef:
    matches = [
        node for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    if len(matches) != 1:
        raise AssertionError(("function", name, len(matches)))
    return matches[0]


def assigned_literal(tree: ast.Module, name: str) -> object:
    matches: list[ast.AST] = []
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
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
        raise AssertionError(("literal", name, len(matches)))
    return ast.literal_eval(matches[0])


def named_dict_constant(
    tree: ast.Module,
    identity_name: str,
    requested_key: str,
) -> object:
    matches = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Dict):
            continue
        pairs = {
            key.value: value
            for key, value in zip(node.keys, node.values)
            if isinstance(key, ast.Constant)
            and isinstance(key.value, str)
        }
        name_node = pairs.get("name")
        value_node = pairs.get(requested_key)
        if (
            isinstance(name_node, ast.Constant)
            and name_node.value == identity_name
            and isinstance(value_node, ast.Constant)
        ):
            matches.append(value_node.value)
    if len(matches) != 1:
        raise AssertionError(
            ("named dict constant", identity_name, requested_key, len(matches))
        )
    return matches[0]


def load_inert_packet() -> tuple[
    dict[str, object], dict[str, str], dict[str, ast.Module]
]:
    rows = {}
    sources = {}
    trees = {}
    for path in AUDIT_INPUT_PATHS:
        absolute = ROOT / path
        data = absolute.read_bytes()
        text = data.decode("utf-8")
        observed_sha = sha256(data).hexdigest()
        observed_blob = git_blob_sha1(data)
        expected = EXPECTED_PROVENANCE[path]
        exact = (
            absolute.is_file()
            and observed_sha == expected["sha256"]
            and observed_blob == expected["blob"]
        )
        rows[path] = {
            **expected,
            "observed_sha256": observed_sha,
            "observed_blob": observed_blob,
            "bytes": len(data),
            "exact": exact,
        }
        sources[path] = text
        trees[path] = ast.parse(text, filename=path)
    literal_relative = all(
        not Path(path).is_absolute()
        and ".." not in Path(path).parts
        for path in AUDIT_INPUT_PATHS
    )
    exact = (
        len(rows) == 6
        and literal_relative
        and all(row["exact"] for row in rows.values())
    )
    return {
        "literal_paths": AUDIT_INPUT_PATHS,
        "literal_worktree_relative": literal_relative,
        "paths_existing": all((ROOT / path).is_file()
                              for path in AUDIT_INPUT_PATHS),
        "rows": rows,
        "access": "bytes/text/ast.parse only; never imported or executed",
        "exact": exact,
    }, sources, trees


def certificate_a(trees: dict[str, ast.Module]) -> dict[str, object]:
    primary_hypothesis = assigned_literal(
        trees[PRIMARY_817], HYPOTHESIS_NAME
    )
    checker_identity = named_dict_constant(
        trees[CHECKER_817], HYPOTHESIS_NAME, "identity"
    )
    finalizer = function_node(
        trees[SOURCE_FINALIZER], "source_finalizer_word"
    )
    finalizer_argument_loads = tuple(
        node.lineno for node in ast.walk(finalizer)
        if isinstance(node, ast.Name)
        and isinstance(node.ctx, ast.Load)
        and node.id == "_bank_count"
    )
    exact = (
        primary_hypothesis == EXPECTED_HYPOTHESIS
        and checker_identity == EXPECTED_CHECKER_IDENTITY
        and not finalizer_argument_loads
    )
    return {
        "certificate_name": "A_MECHANICAL_RESTATEMENT",
        "Cycle817_primary_exact_statement": primary_hypothesis,
        "Cycle817_checker_exact_identity": checker_identity,
        "fixed_b_decidability": "FINITE_DECIDABLE",
        "quantified_objects_at_fixed_b": (
            "the 8*b-5 emitted program rows; each selected finite gate word; "
            "every gate operand; the finite bank/edge indices in those rows; "
            "the one cross predecessor offset; and finalizer outputs"
        ),
        "decision_procedure": (
            "authenticate the eight literal constructor words; expand all "
            "8*b-5 rows; classify every operand in the source anchor, one "
            "bank block, adjacent bank blocks, or the declared 191-wire "
            "link half; check cross offset 0<=1<131; and prove the finalizer "
            "_bank_count parameter has no AST loads"
        ),
        "capacity_quantifier_ruling": (
            "No infinite C enumeration is needed: the check is on local "
            "preimages, and the affine formulas symbolically map each typed "
            "preimage into the same declared zone for every C>=b."
        ),
        "bounded_surrogate": None,
        "source_anchor_support": {
            "half_open": SOURCE_ANCHOR_SUPPORT,
            "reason": (
                "the source interval plus bank[0] are capacity-independent "
                "under BANK_BASE(i)=41+131*i"
            ),
        },
        "finalizer_bank_count_AST_loads": finalizer_argument_loads,
        "exact": exact,
    }


def main() -> int:
    started = perf_counter()
    source_inputs, _sources, trees = load_inert_packet()
    cert_a = certificate_a(trees)
    elapsed = perf_counter() - started
    report = {
        "version": 1,
        "status": "INCREMENTAL_CERTIFICATE_A_ONLY",
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "BLOCKLIST": BLOCKLIST,
        "source_inputs": source_inputs,
        "certificate_A": cert_a,
        "runtime_seconds": round(elapsed, 6),
        "runner_exact": source_inputs["exact"] and cert_a["exact"],
    }
    report["report_sha256"] = stable_digest(report)
    output = json.dumps(report, sort_keys=True, separators=(",", ":")) + "\n"
    if len(output.encode()) >= STDOUT_LIMIT_BYTES:
        print("CYCLE823_INCREMENTAL_STDOUT_LIMIT_FAIL")
        return 1
    sys.stdout.write(output)
    return 0 if report["runner_exact"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
