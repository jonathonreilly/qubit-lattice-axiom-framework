#!/usr/bin/env python3
"""Cycle 813: exact invariant-level test of the k>=4 silence.

Only the landed Cycle-719 controller core is executable science input.
Cycle-736/758/790/791/792/794/798 primaries are SHA-pinned text/AST
references and are blocked from import.  The runner independently reconstructs
the synchronous word, the clean-postimage predicate, the separated translation
families, and the exact Boolean gate interpreter.

The terminal is deliberately three-way.  A bounded-horizon silence is never
promoted to an all-time theorem unless a proven conserved necessary condition
excludes the key.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
STDOUT_LIMIT_BYTES = 200 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from collections import Counter
from hashlib import sha1, sha256
import importlib.abc
import json
from pathlib import Path
import subprocess
import sys
from time import monotonic
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

LINEAGE_REFERENCES = (
    {
        "cycle": 736,
        "commit": "723d0c20cb15f8a40bb3c997339978764f61c6bf",
        "path":
            "scripts/frontier_cycle736_pairwise_separated_multisource_2026_07_28.py",
        "blob": "8ddd84104dc0729107cebfb0d0cd694fe78af1af",
        "sha256":
            "50059ce4d4d6e5ce4503e66ccb098f6fe663ad9711b106b6b6c5c9cb7bcbd02f",
    },
    {
        "cycle": 758,
        "commit": "7a120caef64c8aacccb4c350594b8e91cca2f9c2",
        "path":
            "scripts/frontier_cycle758_selector_multisource_2026_07_28.py",
        "blob": "4e23e03ecc5f92a0b8348bfa526eb5b2f2b09dd0",
        "sha256":
            "8be433f74cb337c322bcb1e2f46007244d708a41c946cb83b7ccd61004176241",
    },
    {
        "cycle": 790,
        "commit": "935e46cac19230caf123c8810af367d7cd843469",
        "path":
            "scripts/frontier_cycle790_horizon_extension_2026_07_28.py",
        "blob": "c322bb975900b2611c3f42d19da347a1dd5bfc56",
        "sha256":
            "bc1a47b591e4b308ef3e57ea7776a56223c76c0eca3867816d408f5021e86ac6",
    },
    {
        "cycle": 791,
        "commit": "6255426f36a48494de43ccc8bd3eb9592e584c00",
        "path":
            "scripts/frontier_cycle791_open_keys_resolution_2026_07_28.py",
        "blob": "f026960526f2f2a8d990a5a7856b02217ea798ce",
        "sha256":
            "3380b3f0820a74e0f538b54144bb926a2a4be9041ed21ae5181216f481c8a98a",
    },
    {
        "cycle": 792,
        "commit": "04499b425103ba4635900a56f7370123a59345a4",
        "path":
            "scripts/frontier_cycle792_extended_horizon_selector_2026_07_28.py",
        "blob": "63948b09c41dd02b14350084ec33f7df9ad83b47",
        "sha256":
            "7f7470b3d759c84ccc0c2c6559d62448340fb8a0b0915eb98d450635a72730df",
    },
    {
        "cycle": 794,
        "commit": "0f4bace05de9b2830ea0b9a3f8a99f42a56cc301",
        "path":
            "scripts/frontier_cycle794_second_selection_2026_07_28.py",
        "blob": "a6debf306793270a4cda61638b619d4ad55dea69",
        "sha256":
            "5fcb9f015b7690df833a3b3d1dc7bdc81162e066f1f25d34d420d8779c563582",
    },
    {
        "cycle": 798,
        "commit": "c9073485c5eb446d417434416c015da9e0a1cff5",
        "path":
            "scripts/frontier_cycle798_higher_k_horizon_scan_2026_07_28.py",
        "blob": "9de34ad5adcbf484d4f0c7e6aec13375ed465aab",
        "sha256":
            "f6ec49636ecb7ec09808eed7d38f2085f6145cd383c306370502c547741942b1",
    },
)

BLOCKLISTED_MODULES = tuple(
    Path(row["path"]).stem for row in LINEAGE_REFERENCES
)
EXPECTED_719_SHA256 = (
    "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4"
)
EXPECTED_719_BLOB = "c123b8d681c3d76fce08ef13d7673622deac64ad"


class _BlocklistFinder(importlib.abc.MetaPathFinder):
    """Fail closed if a text/AST-only lineage primary is imported."""

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
    assignment = next(
        node
        for node in tree.body
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name)
            and target.id == "AUDIT_INPUT_PATHS"
            for target in node.targets
        )
    )
    return (
        isinstance(assignment.value, ast.Tuple)
        and all(
            isinstance(item, ast.Constant)
            and isinstance(item.value, str)
            for item in assignment.value.elts
        )
        and tuple(ast.literal_eval(assignment.value)) == AUDIT_INPUT_PATHS
    )


def source_controls() -> dict[str, object]:
    audit_rows = []
    for relative in AUDIT_INPUT_PATHS:
        path = ROOT / relative
        payload = path.read_bytes() if path.is_file() else b""
        audit_rows.append(
            {
                "path": relative,
                "exists": path.is_file(),
                "sha256": sha256(payload).hexdigest(),
                "git_blob": git_blob_sha(payload),
            }
        )

    reference_rows = []
    for reference in LINEAGE_REFERENCES:
        payload = git_reference_payload(
            str(reference["commit"]), str(reference["path"])
        )
        tree = ast.parse(
            payload.decode("utf-8"), filename=str(reference["path"])
        )
        reference_rows.append(
            {
                "cycle": reference["cycle"],
                "commit": reference["commit"],
                "path": reference["path"],
                "sha256": sha256(payload).hexdigest(),
                "git_blob": git_blob_sha(payload),
                "expected_sha256": reference["sha256"],
                "expected_blob": reference["blob"],
                "top_level_function_count": sum(
                    isinstance(node, ast.FunctionDef) for node in tree.body
                ),
                "AST_TEXT_ONLY_BLOCKLISTED": True,
                "match": (
                    sha256(payload).hexdigest() == reference["sha256"]
                    and git_blob_sha(payload) == reference["blob"]
                ),
            }
        )

    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "literal_tuple": literal_audit_paths(),
        "existing_worktree_relative": all(
            (ROOT / relative).is_file()
            and not Path(relative).is_absolute()
            for relative in AUDIT_INPUT_PATHS
        ),
        "audit_rows": audit_rows,
        "lineage_reference_rows": reference_rows,
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
        and len(reference_rows) == 7
        and all(row["match"] for row in reference_rows)
        and not result["blocked_runtime_modules"]
        and not result["firewall_hits"]
    )
    return result


def main() -> int:
    started = monotonic()
    controls = source_controls()
    check("CERTIFICATE_E_SOURCE_SHA_AST_BLOCKLIST", controls["pass"], controls)
    elapsed = monotonic() - started
    terminal = {
        "terminal": "CYCLE813_SKELETON",
        "pass": all(CHECKS.values()),
        "runtime_seconds": round(elapsed, 6),
    }
    output = "\n".join(OUTPUT_LINES) + "\nFINAL " + compact(terminal) + "\n"
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        raise AssertionError("stdout limit")
    sys.stdout.write(output)
    return 0 if terminal["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
