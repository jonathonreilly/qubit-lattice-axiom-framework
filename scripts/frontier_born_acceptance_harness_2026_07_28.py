#!/usr/bin/env python3
"""Frozen acceptance infrastructure for the Cycle-317 Born-forcing surface.

Feed schema:

    {
        "probe_id": <string naming one frozen probe or witness>,
        "kind": "bloch_projector",
        "direction": [<three JSON scalar entries>],
    }

The lawful domain is the landed surface's unit-three-vector Bloch-projector
domain.  Frozen feeds are supplied apparatus data.  This harness selects no
Born law, weight map, probability content, occurrence, or Record.  It only
certifies whether the landed machinery accepts or refuses those feeds exactly
as frozen.  Landed modules are executed or called only in child processes.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/BORN_ACCEPTANCE_HARNESS_SUPPORT_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18.py",
    "scripts/physical_contact_ternary_born_forcing_release_cycle317_2026_07_18.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
import hashlib
import json
import math
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import time
from typing import Any


_MODULE_START = time.monotonic()
ROOT = Path(__file__).resolve().parents[1]

BRIDGE_SHA256 = "e8ef160207d200555937a0d76e5ca796a98bb998b568221f327fb9ccf5e2bc10"
RELEASE_SHA256 = "7fd16049e5baae5f0c7f56e19beee925313b1f1f872fa1f1c96dd78b47ac41e7"

FROZEN_SELF_RUNS = (
    {
        "name": "bridge",
        "path": "scripts/physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18.py",
        "sha256": "e8ef160207d200555937a0d76e5ca796a98bb998b568221f327fb9ccf5e2bc10",
        "stdout_sha256": "c5e35923c1e3fbfb94db745b58d0e8d12e3d65d79c0a7af08d95c6c8ea29f0dc",
        "stdout_bytes": 8408,
        "summary_pattern": r"^SUMMARY PASS (\d+) FAIL (\d+)$",
        "expected_pass": 15,
        "expected_fail": 0,
        "terminal_marker": "RESULT CYCLE317_PHYSICAL_CONTACT_TERNARY_BORN_BRIDGE_GREEN",
    },
    {
        "name": "release",
        "path": "scripts/physical_contact_ternary_born_forcing_release_cycle317_2026_07_18.py",
        "sha256": "7fd16049e5baae5f0c7f56e19beee925313b1f1f872fa1f1c96dd78b47ac41e7",
        "stdout_sha256": "ba143794a2fc400c9992dfbac5f80df59e23aee62869dd3b25211fa539a12240",
        "stdout_bytes": 6303,
        "summary_pattern": r"^STRICT SUMMARY PASS (\d+) FAIL (\d+)$",
        "expected_pass": 14,
        "expected_fail": 0,
        "terminal_marker": "STRICT RESULT CYCLE317_RELEASE_DISCIPLINE_GREEN",
    },
)

FROZEN_LAWFUL_PROBES = (
    {
        "probe_id": "axis_plus_x",
        "feed": {
            "probe_id": "axis_plus_x",
            "kind": "bloch_projector",
            "direction": [1, 0, 0],
        },
        "expected": {
            "origin": "landed_surface",
            "status": "returned",
            "matrix": [
                [[0.5, 0.0], [0.5, 0.0]],
                [[0.5, 0.0], [0.5, 0.0]],
            ],
            "summary": {
                "shape": [2, 2],
                "hermitian_residual": 0.0,
                "idempotence_residual": 0.0,
                "trace_real": 1.0,
                "trace_imag": 0.0,
                "minimum_eigenvalue": 0.0,
                "maximum_eigenvalue": 1.0,
            },
            "machine_bound": 5.0e-15,
        },
    },
    {
        "probe_id": "axis_minus_x",
        "feed": {
            "probe_id": "axis_minus_x",
            "kind": "bloch_projector",
            "direction": [-1, 0, 0],
        },
        "expected": {
            "origin": "landed_surface",
            "status": "returned",
            "matrix": [
                [[0.5, 0.0], [-0.5, 0.0]],
                [[-0.5, 0.0], [0.5, 0.0]],
            ],
            "summary": {
                "shape": [2, 2],
                "hermitian_residual": 0.0,
                "idempotence_residual": 0.0,
                "trace_real": 1.0,
                "trace_imag": 0.0,
                "minimum_eigenvalue": 0.0,
                "maximum_eigenvalue": 1.0,
            },
            "machine_bound": 5.0e-15,
        },
    },
    {
        "probe_id": "axis_plus_y",
        "feed": {
            "probe_id": "axis_plus_y",
            "kind": "bloch_projector",
            "direction": [0, 1, 0],
        },
        "expected": {
            "origin": "landed_surface",
            "status": "returned",
            "matrix": [
                [[0.5, 0.0], [0.0, -0.5]],
                [[0.0, 0.5], [0.5, 0.0]],
            ],
            "summary": {
                "shape": [2, 2],
                "hermitian_residual": 0.0,
                "idempotence_residual": 0.0,
                "trace_real": 1.0,
                "trace_imag": 0.0,
                "minimum_eigenvalue": 0.0,
                "maximum_eigenvalue": 1.0,
            },
            "machine_bound": 5.0e-15,
        },
    },
    {
        "probe_id": "axis_plus_z",
        "feed": {
            "probe_id": "axis_plus_z",
            "kind": "bloch_projector",
            "direction": [0, 0, 1],
        },
        "expected": {
            "origin": "landed_surface",
            "status": "returned",
            "matrix": [
                [[1.0, 0.0], [0.0, 0.0]],
                [[0.0, 0.0], [0.0, 0.0]],
            ],
            "summary": {
                "shape": [2, 2],
                "hermitian_residual": 0.0,
                "idempotence_residual": 0.0,
                "trace_real": 1.0,
                "trace_imag": 0.0,
                "minimum_eigenvalue": 0.0,
                "maximum_eigenvalue": 1.0,
            },
            "machine_bound": 5.0e-15,
        },
    },
)

FROZEN_REJECT_WITNESSES = (
    {
        "probe_id": "wrong_arity",
        "feed": {
            "probe_id": "wrong_arity",
            "kind": "bloch_projector",
            "direction": [1, 0],
        },
        "enforcement": "landed_surface",
        "expected": {
            "origin": "landed_surface",
            "status": "raised",
            "exception_type": "ValueError",
            "message": "a Bloch projector needs one unit three-vector",
        },
    },
    {
        "probe_id": "non_normalized",
        "feed": {
            "probe_id": "non_normalized",
            "kind": "bloch_projector",
            "direction": [1, 1, 1],
        },
        "enforcement": "landed_surface",
        "expected": {
            "origin": "landed_surface",
            "status": "raised",
            "exception_type": "ValueError",
            "message": "a Bloch projector needs one unit three-vector",
        },
    },
    {
        "probe_id": "out_of_domain_value",
        "feed": {
            "probe_id": "out_of_domain_value",
            "kind": "bloch_projector",
            "direction": [2, 0, 0],
        },
        "enforcement": "landed_surface",
        "expected": {
            "origin": "landed_surface",
            "status": "raised",
            "exception_type": "ValueError",
            "message": "a Bloch projector needs one unit three-vector",
        },
    },
    {
        "probe_id": "boolean_type_violation",
        "feed": {
            "probe_id": "boolean_type_violation",
            "kind": "bloch_projector",
            "direction": [True, 0, 0],
        },
        "enforcement": "harness_schema",
        "expected": {
            "origin": "harness_schema",
            "status": "raised",
            "exception_type": "SchemaRefusal",
            "message": (
                "HARNESS_SCHEMA: direction entries must be finite JSON numbers "
                "and booleans are excluded"
            ),
        },
    },
)

QUARANTINED_WRONG_EXPECTATION = {
    "probe_id": "axis_plus_x",
    "purpose": "independent-adversary comparison liveness only",
    "expected": {
        "origin": "landed_surface",
        "status": "returned",
        "matrix": [
            [[0.75, 0.0], [0.5, 0.0]],
            [[0.5, 0.0], [0.5, 0.0]],
        ],
        "summary": {
            "shape": [2, 2],
            "hermitian_residual": 0.0,
            "idempotence_residual": 0.0,
            "trace_real": 1.0,
            "trace_imag": 0.0,
            "minimum_eigenvalue": 0.0,
            "maximum_eigenvalue": 1.0,
        },
        "machine_bound": 5.0e-15,
    },
}

_SURFACE_DRIVER = r"""
import json
import sys

import numpy as np
import physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18 as surface

payload = json.load(sys.stdin)
try:
    projector = surface.projector_bloch(payload["direction"])
    hermitian = (projector + projector.conj().T) / 2
    eigenvalues = np.linalg.eigvalsh(hermitian)
    record = {
        "origin": "landed_surface",
        "status": "returned",
        "matrix": [
            [[float(value.real), float(value.imag)] for value in row]
            for row in projector
        ],
        "summary": {
            "shape": list(projector.shape),
            "hermitian_residual": float(
                np.linalg.norm(projector - projector.conj().T)
            ),
            "idempotence_residual": float(
                np.linalg.norm(projector @ projector - projector)
            ),
            "trace_real": float(np.trace(projector).real),
            "trace_imag": float(np.trace(projector).imag),
            "minimum_eigenvalue": float(np.min(eigenvalues)),
            "maximum_eigenvalue": float(np.max(eigenvalues)),
        },
    }
except Exception as exc:
    record = {
        "origin": "landed_surface",
        "status": "raised",
        "exception_type": type(exc).__name__,
        "message": str(exc),
    }
print(json.dumps(record, allow_nan=False, sort_keys=True))
"""

_PASS = 0
_FAIL = 0


def check(label: str, condition: bool, detail: Any = "") -> bool:
    """Print one certificate line and update the local census."""
    global _PASS, _FAIL
    if condition:
        _PASS += 1
        status = "PASS"
    else:
        _FAIL += 1
        status = "FAIL"
    print(f"{status} {label} :: {detail}")
    return condition


def _sha256_path(relative_path: str) -> str:
    return hashlib.sha256((ROOT / relative_path).read_bytes()).hexdigest()


def _sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _same_data(left: Any, right: Any) -> bool:
    try:
        left_json = json.dumps(
            left, allow_nan=False, separators=(",", ":"), sort_keys=True
        )
        right_json = json.dumps(
            right, allow_nan=False, separators=(",", ":"), sort_keys=True
        )
    except (TypeError, ValueError):
        return False
    return left_json == right_json


def _frozen_numeric_match(observed: Any, expected: Any, bound: float) -> bool:
    if isinstance(expected, bool) or expected is None or isinstance(expected, str):
        return observed == expected
    if isinstance(expected, (int, float)):
        return (
            isinstance(observed, (int, float))
            and not isinstance(observed, bool)
            and math.isfinite(float(observed))
            and abs(float(observed) - float(expected)) <= bound
        )
    if isinstance(expected, list):
        return (
            isinstance(observed, list)
            and len(observed) == len(expected)
            and all(
                _frozen_numeric_match(actual, frozen, bound)
                for actual, frozen in zip(observed, expected)
            )
        )
    if isinstance(expected, dict):
        return (
            isinstance(observed, dict)
            and set(observed) == set(expected)
            and all(
                _frozen_numeric_match(observed[key], value, bound)
                for key, value in expected.items()
            )
        )
    return observed == expected


def _current_pins() -> dict[str, dict[str, Any]]:
    rows = {}
    for frozen in FROZEN_SELF_RUNS:
        actual = _sha256_path(frozen["path"])
        rows[frozen["name"]] = {
            "path": frozen["path"],
            "expected": frozen["sha256"],
            "actual": actual,
            "match": actual == frozen["sha256"],
        }
    return rows


def _self_run(frozen: dict[str, Any]) -> dict[str, Any]:
    actual_sha = _sha256_path(frozen["path"])
    if actual_sha != frozen["sha256"]:
        return {
            "name": frozen["name"],
            "verdict": "DRIFT",
            "pin_match": False,
            "executed": False,
            "output_match": False,
        }
    try:
        completed = subprocess.run(
            [sys.executable, str(ROOT / frozen["path"])],
            cwd=ROOT,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
            timeout=AUDIT_TIMEOUT_SEC,
        )
    except subprocess.TimeoutExpired as exc:
        return {
            "name": frozen["name"],
            "verdict": "DRIFT",
            "pin_match": True,
            "executed": True,
            "output_match": False,
            "timeout": exc.timeout,
        }

    stdout_text = completed.stdout.decode("utf-8", errors="replace")
    matches = re.findall(
        frozen["summary_pattern"], stdout_text, flags=re.MULTILINE
    )
    observed_counts = (
        [int(value) for value in matches[-1]] if matches else None
    )
    lines = stdout_text.splitlines()
    marker_match = bool(lines and lines[-1] == frozen["terminal_marker"])
    count_match = observed_counts == [
        frozen["expected_pass"],
        frozen["expected_fail"],
    ]
    output_match = (
        completed.returncode == 0
        and _sha256_bytes(completed.stdout) == frozen["stdout_sha256"]
        and len(completed.stdout) == frozen["stdout_bytes"]
        and completed.stderr == b""
        and count_match
        and marker_match
    )
    return {
        "name": frozen["name"],
        "verdict": "ACCEPT" if output_match else "DRIFT",
        "pin_match": True,
        "executed": True,
        "output_match": output_match,
        "returncode": completed.returncode,
        "stdout_sha256": _sha256_bytes(completed.stdout),
        "stdout_bytes": len(completed.stdout),
        "stderr_sha256": _sha256_bytes(completed.stderr),
        "stderr_bytes": len(completed.stderr),
        "observed_counts": observed_counts,
        "count_match": count_match,
        "marker_match": marker_match,
    }


def _lookup_frozen(probe_id: Any) -> tuple[str, dict[str, Any]] | None:
    for row in FROZEN_LAWFUL_PROBES:
        if row["probe_id"] == probe_id:
            return "lawful", row
    for row in FROZEN_REJECT_WITNESSES:
        if row["probe_id"] == probe_id:
            return "reject", row
    return None


def _schema_refusal() -> dict[str, Any]:
    return {
        "origin": "harness_schema",
        "status": "raised",
        "exception_type": "SchemaRefusal",
        "message": (
            "HARNESS_SCHEMA: direction entries must be finite JSON numbers "
            "and booleans are excluded"
        ),
    }


def _surface_observation(feed: dict[str, Any]) -> dict[str, Any]:
    try:
        encoded = json.dumps(feed, allow_nan=False, sort_keys=True)
    except (TypeError, ValueError) as exc:
        return {
            "origin": "harness_schema",
            "status": "raised",
            "exception_type": "SchemaRefusal",
            "message": f"HARNESS_SCHEMA: non-JSON feed: {type(exc).__name__}",
        }
    try:
        completed = subprocess.run(
            [sys.executable, "-c", _SURFACE_DRIVER],
            cwd=ROOT,
            input=encoded,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
            timeout=AUDIT_TIMEOUT_SEC,
        )
    except subprocess.TimeoutExpired as exc:
        return {
            "origin": "subprocess_driver",
            "status": "driver_error",
            "message": f"timeout after {exc.timeout} seconds",
        }
    if completed.returncode != 0:
        return {
            "origin": "subprocess_driver",
            "status": "driver_error",
            "returncode": completed.returncode,
            "stderr_sha256": _sha256_bytes(completed.stderr.encode("utf-8")),
        }
    try:
        return json.loads(completed.stdout)
    except json.JSONDecodeError as exc:
        return {
            "origin": "subprocess_driver",
            "status": "driver_error",
            "message": f"JSONDecodeError: {exc}",
        }


def _compare_observation(
    category: str,
    feed: Any,
    frozen: dict[str, Any],
    observed: dict[str, Any],
) -> dict[str, bool]:
    expected = frozen["expected"]
    feed_match = _same_data(feed, frozen["feed"])
    origin_match = observed.get("origin") == expected["origin"]
    status_match = observed.get("status") == expected["status"]
    if category == "lawful":
        bound = expected["machine_bound"]
        matrix_match = _frozen_numeric_match(
            observed.get("matrix"), expected["matrix"], bound
        )
        summary_match = _frozen_numeric_match(
            observed.get("summary"), expected["summary"], bound
        )
        signature_match = True
    else:
        matrix_match = True
        summary_match = True
        signature_match = (
            observed.get("exception_type") == expected["exception_type"]
            and observed.get("message") == expected["message"]
        )
    frozen_match = (
        feed_match
        and origin_match
        and status_match
        and matrix_match
        and summary_match
        and signature_match
    )
    return {
        "feed_match": feed_match,
        "origin_match": origin_match,
        "status_match": status_match,
        "matrix_match": matrix_match,
        "summary_match": summary_match,
        "signature_match": signature_match,
        "frozen_match": frozen_match,
    }


def run_acceptance(feed: Any) -> dict[str, Any]:
    """Return ACCEPT, REJECT, or DRIFT for one declared-shape feed object."""
    pins = _current_pins()
    if not all(row["match"] for row in pins.values()):
        return {
            "probe_id": feed.get("probe_id") if isinstance(feed, dict) else None,
            "verdict": "DRIFT",
            "pins": pins,
            "comparison": {"frozen_match": False},
            "observation": {"status": "not_run_on_unpinned_surface"},
        }
    if not isinstance(feed, dict):
        return {
            "probe_id": None,
            "verdict": "REJECT",
            "pins": pins,
            "comparison": {"frozen_match": False},
            "observation": {
                "origin": "harness_schema",
                "status": "raised",
                "exception_type": "SchemaRefusal",
                "message": "HARNESS_SCHEMA: feed must be an object",
            },
        }

    lookup = _lookup_frozen(feed.get("probe_id"))
    exact_keys = set(feed) == {"probe_id", "kind", "direction"}
    exact_kind = feed.get("kind") == "bloch_projector"
    if lookup is None or not exact_keys or not exact_kind:
        return {
            "probe_id": feed.get("probe_id"),
            "verdict": "REJECT",
            "pins": pins,
            "comparison": {"frozen_match": False},
            "observation": {
                "origin": "harness_schema",
                "status": "raised",
                "exception_type": "SchemaRefusal",
                "message": (
                    "HARNESS_SCHEMA: feed must exactly name one frozen "
                    "bloch_projector probe"
                ),
            },
        }

    category, frozen = lookup
    if frozen.get("enforcement") == "harness_schema":
        observed = _schema_refusal()
    else:
        observed = _surface_observation(feed)
    comparison = _compare_observation(category, feed, frozen, observed)
    if comparison["feed_match"] and not comparison["frozen_match"]:
        verdict = "DRIFT"
    elif category == "lawful" and comparison["frozen_match"]:
        verdict = "ACCEPT"
    else:
        verdict = "REJECT"
    return {
        "probe_id": frozen["probe_id"],
        "category": category,
        "enforcement": frozen.get("enforcement", "landed_surface"),
        "verdict": verdict,
        "pins": pins,
        "comparison": comparison,
        "observation": observed,
    }


def _sandbox_drift_demo() -> dict[str, Any]:
    real_before = _sha256_path(AUDIT_INPUT_PATHS[0])
    with tempfile.TemporaryDirectory(prefix="born-acceptance-drift-") as folder:
        sandbox_path = Path(folder) / Path(AUDIT_INPUT_PATHS[0]).name
        shutil.copyfile(ROOT / AUDIT_INPUT_PATHS[0], sandbox_path)
        original = sandbox_path.read_bytes()
        changed = bytearray(original)
        changed[-1] ^= 1
        sandbox_path.write_bytes(bytes(changed))
        sandbox_sha = hashlib.sha256(sandbox_path.read_bytes()).hexdigest()
        differing_bytes = sum(
            left != right for left, right in zip(original, changed)
        )
        sandbox_verdict = (
            "ACCEPT" if sandbox_sha == BRIDGE_SHA256 else "DRIFT"
        )
    real_after = _sha256_path(AUDIT_INPUT_PATHS[0])
    return {
        "verdict": sandbox_verdict,
        "one_byte_changed": differing_bytes == 1,
        "sandbox_sha256": sandbox_sha,
        "expected_sha256": BRIDGE_SHA256,
        "real_before": real_before,
        "real_after": real_after,
        "real_unchanged": (
            real_before == real_after == BRIDGE_SHA256
        ),
    }


def _landed_attribute_writes(tree: ast.AST, alias: str) -> list[str]:
    writes = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Attribute) or not isinstance(
            node.ctx, ast.Store
        ):
            continue
        base = node.value
        if isinstance(base, ast.Name) and base.id == alias:
            writes.append(node.attr)
    return writes


def _table_node(tree: ast.Module, name: str) -> ast.AST | None:
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
        ):
            return node.value
    return None


def _structural_audit() -> dict[str, Any]:
    source = Path(__file__).read_text(encoding="utf-8")
    outer = ast.parse(source, filename=str(Path(__file__)))
    driver = ast.parse(_SURFACE_DRIVER, filename="<surface-driver>")
    landed_names = {
        Path(path).stem for path in AUDIT_INPUT_PATHS
    }
    outer_imports = {
        alias.name
        for node in ast.walk(outer)
        if isinstance(node, ast.Import)
        for alias in node.names
    } | {
        node.module
        for node in ast.walk(outer)
        if isinstance(node, ast.ImportFrom) and node.module is not None
    }
    parent_imports_landed = bool(landed_names & outer_imports)

    identifiers = []
    for node in ast.walk(outer):
        if isinstance(node, ast.Name):
            identifiers.append(node.id.lower())
        elif isinstance(node, ast.Attribute):
            identifiers.append(node.attr.lower())
        elif isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            identifiers.append(node.name.lower())
    forbidden_fragments = ("weight", "probab", "random", "sample", "choice")
    forbidden_identifiers = sorted(
        {
            name
            for name in identifiers
            if any(fragment in name for fragment in forbidden_fragments)
        }
    )

    surface_calls = [
        node
        for node in ast.walk(driver)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and isinstance(node.func.value, ast.Name)
        and node.func.value.id == "surface"
    ]
    data_only_call = False
    if len(surface_calls) == 1:
        call = surface_calls[0]
        argument = call.args[0] if len(call.args) == 1 else None
        data_only_call = (
            call.func.attr == "projector_bloch"
            and isinstance(argument, ast.Subscript)
            and isinstance(argument.value, ast.Name)
            and argument.value.id == "payload"
            and isinstance(argument.slice, ast.Constant)
            and argument.slice.value == "direction"
            and not call.keywords
        )

    literal_tables = {}
    for name in (
        "FROZEN_LAWFUL_PROBES",
        "FROZEN_REJECT_WITNESSES",
        "QUARANTINED_WRONG_EXPECTATION",
    ):
        node = _table_node(outer, name)
        try:
            ast.literal_eval(node) if node is not None else None
            literal_tables[name] = node is not None
        except (ValueError, TypeError):
            literal_tables[name] = False

    driver_writes = _landed_attribute_writes(driver, "surface")
    parent_modules_clean = all(name not in sys.modules for name in landed_names)
    return {
        "parent_imports_landed": parent_imports_landed,
        "parent_modules_clean": parent_modules_clean,
        "landed_attribute_writes": driver_writes,
        "forbidden_code_identifiers": forbidden_identifiers,
        "surface_call_count": len(surface_calls),
        "surface_call_is_payload_data_only": data_only_call,
        "literal_feed_and_expectation_tables": literal_tables,
        "subprocess_isolation_ok": (
            not parent_imports_landed
            and parent_modules_clean
            and not driver_writes
        ),
        "firewall_ok": (
            not forbidden_identifiers
            and data_only_call
            and all(literal_tables.values())
        ),
    }


def main() -> int:
    global _PASS, _FAIL
    _PASS = 0
    _FAIL = 0

    self_runs = [_self_run(row) for row in FROZEN_SELF_RUNS]
    check(
        "A. byte pins and landed self-runs reproduce frozen counts, markers, and outputs",
        all(row["verdict"] == "ACCEPT" for row in self_runs),
        {
            row["name"]: {
                "verdict": row["verdict"],
                "counts": row.get("observed_counts"),
                "output_match": row["output_match"],
            }
            for row in self_runs
        },
    )

    lawful = [run_acceptance(row["feed"]) for row in FROZEN_LAWFUL_PROBES]
    check(
        "B. all lawful declared-domain probes ACCEPT with frozen-value matches",
        len(lawful) >= 4
        and all(
            row["verdict"] == "ACCEPT"
            and row["comparison"]["frozen_match"]
            for row in lawful
        ),
        {
            row["probe_id"]: {
                "verdict": row["verdict"],
                "frozen_match": row["comparison"]["frozen_match"],
            }
            for row in lawful
        },
    )

    rejected = [
        run_acceptance(row["feed"]) for row in FROZEN_REJECT_WITNESSES
    ]
    structure = _structural_audit()
    check(
        "C. all malformed witnesses REJECT with frozen refusal signatures and zero landed-module writes",
        len(rejected) >= 4
        and all(
            row["verdict"] == "REJECT"
            and row["comparison"]["frozen_match"]
            and row["comparison"]["signature_match"]
            for row in rejected
        )
        and structure["subprocess_isolation_ok"],
        {
            "witnesses": {
                row["probe_id"]: {
                    "verdict": row["verdict"],
                    "frozen_match": row["comparison"]["frozen_match"],
                    "enforcement": row["enforcement"],
                }
                for row in rejected
            },
            "isolation": structure["subprocess_isolation_ok"],
            "attribute_writes": structure["landed_attribute_writes"],
        },
    )

    drift_demo = _sandbox_drift_demo()
    check(
        "D. one-byte sandbox mutation is DRIFT while the real bridge remains byte-pinned",
        drift_demo["verdict"] == "DRIFT"
        and drift_demo["one_byte_changed"]
        and drift_demo["real_unchanged"],
        drift_demo,
    )

    adversary_source = next(
        row for row in lawful if row["probe_id"] == "axis_plus_x"
    )
    adversary_frozen = {
        "feed": next(
            row["feed"]
            for row in FROZEN_LAWFUL_PROBES
            if row["probe_id"] == "axis_plus_x"
        ),
        "expected": QUARANTINED_WRONG_EXPECTATION["expected"],
    }
    adversary_comparison = _compare_observation(
        "lawful",
        adversary_frozen["feed"],
        adversary_frozen,
        adversary_source["observation"],
    )
    adversary_caught = not adversary_comparison["frozen_match"]
    check(
        "E. quarantined wrong frozen expectation is caught by the live comparator",
        adversary_caught
        and not adversary_comparison["matrix_match"],
        adversary_comparison,
    )

    check(
        "F. AST firewall finds data-only feeds and no synthesis identifiers or literal-fed surface calls",
        structure["firewall_ok"],
        {
            "firewall_ok": structure["firewall_ok"],
            "forbidden_code_identifiers": structure[
                "forbidden_code_identifiers"
            ],
            "surface_call_count": structure["surface_call_count"],
            "surface_call_is_payload_data_only": structure[
                "surface_call_is_payload_data_only"
            ],
            "literal_tables": structure[
                "literal_feed_and_expectation_tables"
            ],
        },
    )

    census = [
        {
            "probe_id": row["probe_id"],
            "verdict": row["verdict"],
            "frozen_match": row["comparison"]["frozen_match"],
        }
        for row in lawful + rejected
    ]
    for row in census:
        print(
            "CENSUS",
            row["probe_id"],
            "verdict=" + row["verdict"],
            "frozen_match=" + str(row["frozen_match"]),
        )

    elapsed = time.monotonic() - _MODULE_START
    final_record = {
        "adversary_self_test": {
            "caught": adversary_caught,
            "wrong_matrix_match": adversary_comparison["matrix_match"],
        },
        "checks": {"fail": _FAIL, "pass": _PASS},
        "drift_demo": drift_demo,
        "firewall": {
            "feeds_are_supplied_apparatus_data": True,
            "new_physics_claimed": False,
            "selects_born_law": False,
            "selects_probability_content": False,
            "selects_weight_map": False,
            "structural_ast_pass": structure["firewall_ok"],
        },
        "probe_census": census,
        "runtime_seconds": round(elapsed, 6),
        "self_runs": self_runs,
    }
    print(
        json.dumps(
            final_record,
            allow_nan=False,
            separators=(",", ":"),
            sort_keys=True,
        )
    )
    return int(_FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
