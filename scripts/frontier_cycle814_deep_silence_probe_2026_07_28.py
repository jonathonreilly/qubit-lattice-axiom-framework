#!/usr/bin/env python3
"""Cycle 814: complete deep-horizon probe of the 24 Cycle-813 silent keys.

Only the landed Cycle-719 controller core is executable science input.
The Cycle-798/801/813 primaries are SHA-pinned text/AST references and are
blocked from import.  Their cleanliness, cycle, and silence-catalog tests are
reimplemented here, with bit-sliced evolution across the four landed epochs.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1400
TARGET_BUDGET_SEC = 1100
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from hashlib import sha1, sha256
import importlib.abc
import inspect
import json
from pathlib import Path
import subprocess
import sys
from time import monotonic
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

REFERENCE_PRIMARIES = (
    {
        "cycle": 798,
        "commit": "c9073485c5eb446d417434416c015da9e0a1cff5",
        "path":
            "scripts/frontier_cycle798_higher_k_horizon_scan_2026_07_28.py",
        "blob": "9de34ad5adcbf484d4f0c7e6aec13375ed465aab",
        "sha256":
            "f6ec49636ecb7ec09808eed7d38f2085f6145cd383c306370502c547741942b1",
    },
    {
        "cycle": 801,
        "commit": "d42048111b5eb75f7a283db2e9039d57017a26cf",
        "path":
            "scripts/frontier_cycle801_silent_strata_deep_scan_2026_07_28.py",
        "blob": "8807587899a5664d39a06901b02b22041682c5cc",
        "sha256":
            "55edc0cc8b3e51de3863819f10303d506e0652dbc031a1f2647c3a11e51cb115",
    },
    {
        "cycle": 813,
        "commit": "fb951745a44b1e32fa6a13003294a632fbae3213",
        "path":
            "scripts/frontier_cycle813_silence_theorem_2026_07_28.py",
        "blob": "2106c04a17cdb9e7a2b12efbf5115b9f0b19c99b",
        "sha256":
            "2cc32c3bf06d0e93bd594288509e3d6f54cbb50a7eeee023932316ae979e64f2",
    },
)
BLOCKLISTED_MODULES = tuple(
    Path(row["path"]).stem for row in REFERENCE_PRIMARIES
)
EXPECTED_719_SHA256 = (
    "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4"
)
EXPECTED_719_BLOB = "c123b8d681c3d76fce08ef13d7673622deac64ad"


class _BlocklistFinder(importlib.abc.MetaPathFinder):
    """Fail closed if a text/AST-only primary is imported."""

    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(
        self,
        fullname: str,
        path: object = None,
        target: object = None,
    ) -> None:
        if fullname in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids import of {fullname}")
        return None


IMPORT_FIREWALL = _BlocklistFinder()
sys.meta_path.insert(0, IMPORT_FIREWALL)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


RING_STATIONS = 11
FIXTURE_BANKS = 2
BASELINE_T = 8192
TARGET_CHOICES = (65536, 32768, 16384, 8192)
PILOT_T = 256
DETERMINISM_SLICE_T = 8192
BATCH_LANES = 4
EXPECTED_SILENT_FAMILY_REPRESENTATIVES = {
    4: (
        (0, 2, 4, 6),
        (0, 2, 4, 7),
        (0, 2, 4, 8),
        (0, 2, 5, 7),
        (0, 2, 5, 8),
    ),
    5: ((0, 2, 4, 6, 8),),
}
EXPECTED_TRANSIENT_CONTROLS = (
    {"k": 2, "positions": (1, 10), "event": 3, "moment": 252},
    {"k": 3, "positions": (0, 2, 5), "event": 2, "moment": 444},
)
EXPECTED_CYCLE_CONTROL = {
    "k": 2,
    "positions": (0, 5),
    "event": 3,
    "period": 2,
}

CHECKS: dict[str, bool] = {}
OUTPUT_LINES: list[str] = []


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob_sha(payload: bytes) -> str:
    header = f"blob {len(payload)}\0".encode("ascii")
    return sha1(header + payload).hexdigest()


def emit(label: str, value: object) -> None:
    OUTPUT_LINES.append(f"{label} {compact(value)}")


def check(label: str, condition: bool, detail: object) -> bool:
    if label in CHECKS:
        raise AssertionError(("duplicate certificate", label))
    passed = bool(condition)
    CHECKS[label] = passed
    OUTPUT_LINES.append(
        f"{'PASS' if passed else 'FAIL'} {label} :: {compact(detail)}"
    )
    return passed


def git_reference_payload(commit: str, path: str) -> bytes:
    completed = subprocess.run(
        ("git", "show", f"{commit}:{path}"),
        cwd=ROOT,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return completed.stdout


def literal_audit_paths() -> bool:
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    assignments = [
        node
        for node in tree.body
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name)
            and target.id == "AUDIT_INPUT_PATHS"
            for target in node.targets
        )
    ]
    return (
        len(assignments) == 1
        and isinstance(assignments[0].value, ast.Tuple)
        and all(
            isinstance(item, ast.Constant)
            and isinstance(item.value, str)
            for item in assignments[0].value.elts
        )
        and tuple(ast.literal_eval(assignments[0].value))
        == AUDIT_INPUT_PATHS
    )


def named_function(tree: ast.Module, name: str) -> ast.FunctionDef:
    rows = [
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    if len(rows) != 1:
        raise AssertionError(("named function", name, len(rows)))
    return rows[0]


def watched_bank_registers() -> tuple[tuple[str, int], ...]:
    rows = [
        ("POINTER", K.A.POINTER),
        ("U_TO_V", K.A.U_TO_V),
        ("V_TO_U", K.A.V_TO_U),
        ("DIRECTION_OK", K.A.DIRECTION_OK),
    ]
    rows.extend(
        (f"FRESH_{index}", wire)
        for index, wire in enumerate(K.A.FRESH)
    )
    rows.extend(
        (f"ZERO_WORK_{index}", wire)
        for index, wire in enumerate(K.A.ZERO_WORK)
    )
    rows.append(("TOKEN_OK", K.A.TOKEN_OK))
    return tuple(rows)


def clean_postimage(after: int, bank_count: int) -> bool:
    banks, links = K.M.unpack_state(after, bank_count)
    return not any(
        (
            after[K.R3.X.SOURCE_POINTER],
            any(
                bank[wire]
                for bank in banks
                for wire in (
                    K.A.POINTER,
                    K.A.U_TO_V,
                    K.A.V_TO_U,
                    K.A.DIRECTION_OK,
                    *K.A.FRESH,
                    *K.A.ZERO_WORK,
                    K.A.TOKEN_OK,
                )
            ),
            any(any(link) for link in links),
        )
    )


def cycle_test_ast_basis(tree: ast.Module) -> dict[str, object]:
    function = named_function(tree, "advance_one_record")
    comparisons = [
        node
        for node in ast.walk(function)
        if isinstance(node, ast.Compare)
        and len(node.ops) == 1
        and isinstance(node.ops[0], ast.Eq)
    ]
    exact_initial_return = any(
        isinstance(node.left, ast.Name)
        and node.left.id == "state"
        and isinstance(node.comparators[0], ast.Subscript)
        and isinstance(node.comparators[0].value, ast.Name)
        and node.comparators[0].value.id == "record"
        and isinstance(node.comparators[0].slice, ast.Constant)
        and node.comparators[0].slice.value == "initial_state"
        for node in comparisons
    )
    source = ast.unparse(function)
    return {
        "function": "advance_one_record",
        "exact_full_state_return_to_T0": exact_initial_return,
        "clean_test_precedes_cycle_test": (
            source.find("if not support") >= 0
            and source.find('state == record["initial_state"]')
            > source.find("if not support")
        ),
        "landed_granularity": "one complete fixed semantic word per horizon_t",
        "ast_sha256":
            sha256(
                ast.dump(function, include_attributes=False).encode("utf-8")
            ).hexdigest(),
    }


def source_controls() -> dict[str, object]:
    audit_rows = []
    for relative in AUDIT_INPUT_PATHS:
        path = ROOT / relative
        payload = path.read_bytes() if path.is_file() else b""
        audit_rows.append(
            {
                "path": relative,
                "exists": path.is_file(),
                "worktree_relative": not Path(relative).is_absolute(),
                "sha256": sha256(payload).hexdigest(),
                "git_blob": git_blob_sha(payload),
            }
        )

    reference_rows = []
    reference_trees: dict[int, ast.Module] = {}
    for reference in REFERENCE_PRIMARIES:
        payload = git_reference_payload(
            str(reference["commit"]), str(reference["path"])
        )
        tree = ast.parse(
            payload.decode("utf-8"), filename=str(reference["path"])
        )
        reference_trees[int(reference["cycle"])] = tree
        actual_sha = sha256(payload).hexdigest()
        actual_blob = git_blob_sha(payload)
        reference_rows.append(
            {
                **reference,
                "actual_sha256": actual_sha,
                "actual_blob": actual_blob,
                "TEXT_AST_ONLY_BLOCKLISTED": True,
                "match": (
                    actual_sha == reference["sha256"]
                    and actual_blob == reference["blob"]
                ),
            }
        )

    landed_clean = named_function(
        reference_trees[798], "clean_postimage"
    )
    local_clean = ast.parse(inspect.getsource(clean_postimage)).body[0]
    clean_ast_exact = (
        ast.dump(landed_clean, include_attributes=False)
        == ast.dump(local_clean, include_attributes=False)
    )
    cycle_basis = cycle_test_ast_basis(reference_trees[801])
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "literal_tuple": literal_audit_paths(),
        "existing_worktree_relative": all(
            row["exists"] and row["worktree_relative"]
            for row in audit_rows
        ),
        "audit_rows": audit_rows,
        "reference_rows": reference_rows,
        "clean_postimage_798_AST_exact": clean_ast_exact,
        "cycle801_basis": cycle_basis,
        "blocked_modules": BLOCKLISTED_MODULES,
        "blocked_runtime_modules": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits": tuple(IMPORT_FIREWALL.hits),
    }
    result["pass"] = (
        result["literal_tuple"]
        and result["existing_worktree_relative"]
        and len(audit_rows) == 1
        and audit_rows[0]["sha256"] == EXPECTED_719_SHA256
        and audit_rows[0]["git_blob"] == EXPECTED_719_BLOB
        and len(reference_rows) == 3
        and all(row["match"] for row in reference_rows)
        and clean_ast_exact
        and cycle_basis["exact_full_state_return_to_T0"]
        and cycle_basis["clean_test_precedes_cycle_test"]
        and not result["blocked_runtime_modules"]
        and not result["firewall_hits"]
    )
    return result


def main() -> int:
    started = monotonic()
    controls = source_controls()
    check(
        "SCAFFOLD_SOURCE_CONTROLS",
        controls["pass"],
        {
            "source_controls": controls,
            "runtime_seconds": round(monotonic() - started, 6),
        },
    )
    output = "\n".join(OUTPUT_LINES) + "\n"
    sys.stdout.write(output)
    return 0 if all(CHECKS.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
