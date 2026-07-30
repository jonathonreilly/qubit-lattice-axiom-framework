#!/usr/bin/env python3
"""Cycle 818: exact period-structure census across the landed strata.

The named Cycle-790/791/797/814 primaries are provenance-only inputs:
they are SHA-pinned, parsed as text/AST, and blocked from import.  Dynamics
are independently reconstructed from the landed Cycle-719 controller core.

The named caches contain a material lineage discrepancy that this runner
keeps visible.  The strict 14-row inventory is the twelve Cycle-797
certifications (eleven inherited from Cycle 790 and one from Cycle 791) plus
the two Cycle-814 certifications.  Cycle 801 separately records four
k=3 cycles of period 5952 and the same two k=4 keys later certified by
Cycle 814; adding those k=3 rows would make 18 distinct keys, not 14.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1200
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle814_deep_silence_probe_2026_07_28.py",
    "logs/runner-cache/frontier_cycle814_deep_silence_probe_2026_07_28.txt",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from collections import Counter, defaultdict
from fractions import Fraction
from hashlib import sha1, sha256
import importlib.abc
import json
from math import gcd
from pathlib import Path
import subprocess
import sys
from time import monotonic
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

REFERENCE_PRIMARIES = (
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
        "cycle": 797,
        "commit": "3cf5931aa901fb45cbb2030eb119c5a09dd32c02",
        "path":
            "scripts/frontier_cycle797_deep_horizon_continuation_2026_07_28.py",
        "blob": "5d70ba232efcbd4f8c0a2d798f735907d4207b81",
        "sha256":
            "7ece6f7c818a4dcffb3019c610ca0861998f19cfae0287e23fe98562c1a09698",
    },
    {
        "cycle": 814,
        "commit": "6cb13f88f3430a201374b5f1d8b01cf000bc6b35",
        "path":
            "scripts/frontier_cycle814_deep_silence_probe_2026_07_28.py",
        "blob": "19ba617ad1f6be9f8fdc637b764dc7b38cae8d7b",
        "sha256":
            "f023d10784506e0c9ffbb39b17c3f120af78f377f27c5dab93de9a9aebaa98c0",
    },
)

REFERENCE_CACHES = (
    {
        "cycle": 790,
        "commit": "935e46cac19230caf123c8810af367d7cd843469",
        "path":
            "logs/runner-cache/frontier_cycle790_horizon_extension_2026_07_28.txt",
        "blob": "f58caebdd7a3e519b679dd0cdd098c1c80c05e34",
        "sha256":
            "2f428ebba168dc9f9e2602c43409ab7e80b24587f873d895ab54d6ebf26c8634",
    },
    {
        "cycle": 791,
        "commit": "6255426f36a48494de43ccc8bd3eb9592e584c00",
        "path":
            "logs/runner-cache/frontier_cycle791_open_keys_resolution_2026_07_28.txt",
        "blob": "460cb3ae346ef10440d5a3ef03a3c19299374edf",
        "sha256":
            "9ab66b127341c63a664ae1631527ae803358a1dd2d2dcacc4639f49aaeadfc8d",
    },
    {
        "cycle": 797,
        "commit": "3cf5931aa901fb45cbb2030eb119c5a09dd32c02",
        "path":
            "logs/runner-cache/frontier_cycle797_deep_horizon_continuation_2026_07_28.txt",
        "blob": "cb956f584b81899965d961aa356e14dd98a32d38",
        "sha256":
            "e44f1b3739b7f78680c963462a4d2e1ae3277f5b75118a1b2cc2b3ba74c8005a",
    },
    {
        "cycle": 801,
        "commit": "d42048111b5eb75f7a283db2e9039d57017a26cf",
        "path":
            "logs/runner-cache/frontier_cycle801_silent_strata_deep_scan_2026_07_28.txt",
        "blob": "b50059cfb5123439a8848cd32dc17515ae364712",
        "sha256":
            "33c10abc491b78bd2e346263d70ccf77f9b82227a5dcfa8fbe86fa62e891bf3d",
    },
    {
        "cycle": 814,
        "commit": "6cb13f88f3430a201374b5f1d8b01cf000bc6b35",
        "path":
            "logs/runner-cache/frontier_cycle814_deep_silence_probe_2026_07_28.txt",
        "blob": "a81e0f017f68a71af48329eb7d139dba21d0648b",
        "sha256":
            "521e1217d0e36440220fb6226e4872638dbe0abfda3df36986337a06acf4e89c",
    },
)

EXPECTED_AUDIT_SHA256 = {
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py":
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    "scripts/frontier_cycle814_deep_silence_probe_2026_07_28.py":
        "f023d10784506e0c9ffbb39b17c3f120af78f377f27c5dab93de9a9aebaa98c0",
    "logs/runner-cache/frontier_cycle814_deep_silence_probe_2026_07_28.txt":
        "521e1217d0e36440220fb6226e4872638dbe0abfda3df36986337a06acf4e89c",
}

BLOCKLISTED_MODULES = tuple(
    Path(row["path"]).stem for row in REFERENCE_PRIMARIES
)


class _BlocklistFinder(importlib.abc.MetaPathFinder):
    """Fail closed if any provenance-only primary is imported."""

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


def git_payload(commit: str, path: str) -> bytes:
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


def source_controls() -> dict[str, object]:
    audit_rows = []
    for relative in AUDIT_INPUT_PATHS:
        path = ROOT / relative
        payload = path.read_bytes()
        audit_rows.append(
            {
                "path": relative,
                "exists": path.is_file(),
                "worktree_relative": (
                    not Path(relative).is_absolute()
                    and path.is_relative_to(ROOT)
                ),
                "sha256": sha256(payload).hexdigest(),
                "expected_sha256": EXPECTED_AUDIT_SHA256[relative],
                "match":
                    sha256(payload).hexdigest()
                    == EXPECTED_AUDIT_SHA256[relative],
            }
        )

    primary_rows = []
    for reference in REFERENCE_PRIMARIES:
        payload = git_payload(
            str(reference["commit"]), str(reference["path"])
        )
        tree = ast.parse(payload.decode("utf-8"))
        primary_rows.append(
            {
                **reference,
                "actual_blob": git_blob_sha(payload),
                "actual_sha256": sha256(payload).hexdigest(),
                "ast_body_nodes": len(tree.body),
                "TEXT_AST_ONLY_BLOCKLISTED":
                    Path(str(reference["path"])).stem
                    in BLOCKLISTED_MODULES,
                "match": (
                    git_blob_sha(payload) == reference["blob"]
                    and sha256(payload).hexdigest() == reference["sha256"]
                ),
            }
        )

    cache_rows = []
    cache_payloads: dict[int, str] = {}
    for reference in REFERENCE_CACHES:
        payload = git_payload(
            str(reference["commit"]), str(reference["path"])
        )
        cache_payloads[int(reference["cycle"])] = payload.decode("utf-8")
        cache_rows.append(
            {
                **reference,
                "actual_blob": git_blob_sha(payload),
                "actual_sha256": sha256(payload).hexdigest(),
                "match": (
                    git_blob_sha(payload) == reference["blob"]
                    and sha256(payload).hexdigest() == reference["sha256"]
                ),
            }
        )

    passed = (
        literal_audit_paths()
        and all(
            row["exists"] and row["worktree_relative"] and row["match"]
            for row in audit_rows
        )
        and all(row["match"] for row in primary_rows)
        and all(row["match"] for row in cache_rows)
        and not IMPORT_FIREWALL.hits
    )
    return {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "literal_tuple": literal_audit_paths(),
        "all_paths_existing_worktree_relative": all(
            row["exists"] and row["worktree_relative"]
            for row in audit_rows
        ),
        "audit_rows": tuple(audit_rows),
        "primary_rows": tuple(primary_rows),
        "cache_rows": tuple(cache_rows),
        "cache_payloads": cache_payloads,
        "blocked_modules": BLOCKLISTED_MODULES,
        "blocked_runtime_modules": tuple(IMPORT_FIREWALL.hits),
        "pass": passed,
    }


def main() -> int:
    started = monotonic()
    source = source_controls()
    source_public = {
        key: value
        for key, value in source.items()
        if key != "cache_payloads"
    }
    check(
        "CERTIFICATE_E1_SOURCE_SHA_AST_BLOCKLIST_LITERAL_PATHS",
        bool(source["pass"]),
        source_public,
    )
    elapsed = monotonic() - started
    check(
        "CYCLE818_SCAFFOLD",
        elapsed < AUDIT_TIMEOUT_SEC,
        {
            "status": "PROVENANCE_SCAFFOLD_READY",
            "runtime_seconds": round(elapsed, 6),
        },
    )
    output = "\n".join(OUTPUT_LINES) + "\n"
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout limit", len(output.encode("utf-8"))))
    sys.stdout.write(output)
    return 0 if all(CHECKS.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
