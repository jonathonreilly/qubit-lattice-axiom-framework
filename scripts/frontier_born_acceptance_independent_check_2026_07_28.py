#!/usr/bin/env python3
"""Independent checker for the frozen Cycle-317 Born acceptance harness."""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/BORN_ACCEPTANCE_HARNESS_SUPPORT_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18.py",
    "scripts/physical_contact_ternary_born_forcing_release_cycle317_2026_07_18.py",
)

import ast
import hashlib
import json
import math
import os
from pathlib import Path
import re
import subprocess
import sys
import time
from typing import Any, Callable


_START = time.monotonic()
ROOT = Path(__file__).resolve().parents[1]
HARNESS_PATH = ROOT / "scripts/frontier_born_acceptance_harness_2026_07_28.py"
BLOCKLIST = ("frontier_born_acceptance_harness_2026_07_28",)
_HARNESS_WAS_PRELOADED = any(name in sys.modules for name in BLOCKLIST)
_EXTRACTED: dict[str, Any] | None = None
_HONEST_LABEL_RESULT = "not verified"


class _HarnessImportBlocker:
    """Make an accidental harness import fail closed."""

    @staticmethod
    def find_spec(
        fullname: str, path: object = None, target: object = None
    ) -> None:
        del path, target
        if fullname in BLOCKLIST:
            raise ImportError(f"blocklisted data-only module: {fullname}")
        return None


_IMPORT_BLOCKER = _HarnessImportBlocker()
sys.meta_path.insert(0, _IMPORT_BLOCKER)


class CertificateError(RuntimeError):
    """A certificate could not establish its claimed fact."""


def _assignment_node(tree: ast.Module, name: str) -> ast.AST:
    matches: list[ast.AST] = []
    for statement in tree.body:
        if isinstance(statement, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == name
            for target in statement.targets
        ):
            matches.append(statement.value)
        elif (
            isinstance(statement, ast.AnnAssign)
            and isinstance(statement.target, ast.Name)
            and statement.target.id == name
        ):
            matches.append(statement.value)
    if len(matches) != 1:
        raise CertificateError(
            f"{name}: expected one top-level assignment, found {len(matches)}"
        )
    return matches[0]


def _literal(tree: ast.Module, name: str) -> Any:
    node = _assignment_node(tree, name)
    try:
        return ast.literal_eval(node)
    except (TypeError, ValueError, SyntaxError) as exc:
        raise CertificateError(f"{name} is not a pure literal") from exc


def _sha256(relative_path: str) -> str:
    return hashlib.sha256((ROOT / relative_path).read_bytes()).hexdigest()


def _same_json(left: Any, right: Any) -> bool:
    try:
        return json.dumps(
            left, allow_nan=False, separators=(",", ":"), sort_keys=True
        ) == json.dumps(
            right, allow_nan=False, separators=(",", ":"), sort_keys=True
        )
    except (TypeError, ValueError):
        return False


def _numeric_match(observed: Any, expected: Any, bound: float) -> bool:
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
                _numeric_match(actual, frozen, bound)
                for actual, frozen in zip(observed, expected)
            )
        )
    if isinstance(expected, dict):
        return (
            isinstance(observed, dict)
            and set(observed) == set(expected)
            and all(
                _numeric_match(observed[key], value, bound)
                for key, value in expected.items()
            )
        )
    return observed == expected


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise CertificateError(message)


def extraction() -> str:
    """AST-extract and validate every frozen datum used by later certificates."""
    global _EXTRACTED

    source = HARNESS_PATH.read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(HARNESS_PATH))
    audit_paths = _literal(tree, "AUDIT_INPUT_PATHS")
    note_path = _literal(tree, "NOTE_PATH")
    bridge_pin = _literal(tree, "BRIDGE_SHA256")
    release_pin = _literal(tree, "RELEASE_SHA256")
    self_runs = _literal(tree, "FROZEN_SELF_RUNS")
    lawful = _literal(tree, "FROZEN_LAWFUL_PROBES")
    rejected = _literal(tree, "FROZEN_REJECT_WITNESSES")

    _require(
        isinstance(audit_paths, tuple) and audit_paths == AUDIT_INPUT_PATHS,
        "harness AUDIT_INPUT_PATHS is not the checker header tuple",
    )
    _require(note_path == NOTE_PATH, "harness NOTE_PATH does not match")
    _require(
        isinstance(self_runs, tuple) and len(self_runs) == 2,
        "FROZEN_SELF_RUNS must contain exactly two literal rows",
    )
    _require(
        isinstance(lawful, tuple) and len(lawful) == 4,
        "FROZEN_LAWFUL_PROBES must contain exactly four literal rows",
    )
    _require(
        isinstance(rejected, tuple) and len(rejected) == 4,
        "FROZEN_REJECT_WITNESSES must contain exactly four literal rows",
    )

    expected_counts = {"bridge": (15, 0), "release": (14, 0)}
    expected_pins = {"bridge": bridge_pin, "release": release_pin}
    expected_paths = dict(zip(("bridge", "release"), AUDIT_INPUT_PATHS))
    rows_by_name = {
        row.get("name"): row for row in self_runs if isinstance(row, dict)
    }
    _require(
        set(rows_by_name) == set(expected_counts),
        "self-run labels are not exactly bridge/release",
    )
    for name, counts in expected_counts.items():
        row = rows_by_name[name]
        _require(
            (row.get("expected_pass"), row.get("expected_fail")) == counts,
            f"{name} frozen count is not {counts[0]}/{counts[1]}",
        )
        _require(row.get("path") == expected_paths[name], f"{name} path drift")
        _require(row.get("sha256") == expected_pins[name], f"{name} pin split")
        _require(
            isinstance(expected_pins[name], str)
            and re.fullmatch(r"[0-9a-f]{64}", expected_pins[name]) is not None,
            f"{name} pin is not a lowercase sha256",
        )

    lawful_labels = tuple(row.get("probe_id") for row in lawful)
    _require(
        lawful_labels
        == ("axis_plus_x", "axis_minus_x", "axis_plus_y", "axis_plus_z"),
        "lawful probe labels/order drifted",
    )
    for row in lawful:
        _require(
            isinstance(row, dict)
            and row.get("feed", {}).get("probe_id") == row.get("probe_id"),
            "lawful feed label is not intact",
        )
        expected = row.get("expected")
        _require(
            isinstance(expected, dict)
            and expected.get("origin") == "landed_surface"
            and expected.get("status") == "returned"
            and isinstance(expected.get("matrix"), list)
            and isinstance(expected.get("summary"), dict)
            and isinstance(expected.get("machine_bound"), float),
            f"{row.get('probe_id')} has no frozen returned-value expectation",
        )

    expected_reject_labels = {
        "wrong_arity": "landed_surface",
        "non_normalized": "landed_surface",
        "out_of_domain_value": "landed_surface",
        "boolean_type_violation": "harness_schema",
    }
    rejected_by_label = {
        row.get("probe_id"): row for row in rejected if isinstance(row, dict)
    }
    _require(
        tuple(rejected_by_label) == tuple(expected_reject_labels),
        "reject witness labels/order drifted",
    )
    for label, enforcement in expected_reject_labels.items():
        row = rejected_by_label[label]
        expected = row.get("expected")
        _require(row.get("enforcement") == enforcement, f"{label} label is false")
        _require(
            row.get("feed", {}).get("probe_id") == label,
            f"{label} feed label is not intact",
        )
        _require(
            isinstance(expected, dict)
            and expected.get("origin") == enforcement
            and expected.get("status") == "raised"
            and isinstance(expected.get("exception_type"), str)
            and isinstance(expected.get("message"), str),
            f"{label} has no frozen refusal signature",
        )

    _EXTRACTED = {
        "source": source,
        "tree": tree,
        "audit_paths": audit_paths,
        "bridge_pin": bridge_pin,
        "release_pin": release_pin,
        "self_runs": self_runs,
        "lawful": lawful,
        "rejected": rejected,
    }
    return "literal AUDIT/NOTE; pins=2; self-runs=15/0,14/0; ACCEPT=4; REJECT=4"


def _frozen() -> dict[str, Any]:
    if _EXTRACTED is None:
        raise CertificateError("frozen harness data was not extracted")
    return _EXTRACTED


def byte_pin_recount() -> str:
    """Recompute both landed-surface hashes from disk."""
    frozen = _frozen()
    rows = {row["name"]: row for row in frozen["self_runs"]}
    observed = {
        name: _sha256(row["path"]) for name, row in rows.items()
    }
    _require(
        observed["bridge"] == rows["bridge"]["sha256"]
        == frozen["bridge_pin"],
        "bridge byte pin mismatch",
    )
    _require(
        observed["release"] == rows["release"]["sha256"]
        == frozen["release_pin"],
        "release byte pin mismatch",
    )
    return (
        f"bridge={observed['bridge'][:12]}…; "
        f"release={observed['release'][:12]}…"
    )


def self_run_recount() -> str:
    """Run each landed module independently and count its PASS/FAIL lines."""
    frozen = _frozen()
    observed_rows: list[str] = []
    for row in frozen["self_runs"]:
        current_pin = _sha256(row["path"])
        _require(
            current_pin == row["sha256"],
            f"{row['name']} drifted before its self-run",
        )
        try:
            completed = subprocess.run(
                [sys.executable, str(ROOT / row["path"])],
                cwd=ROOT,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=False,
                timeout=AUDIT_TIMEOUT_SEC,
            )
        except subprocess.TimeoutExpired as exc:
            raise CertificateError(
                f"{row['name']} self-run timed out after {exc.timeout}s"
            ) from exc
        stdout = completed.stdout.decode("utf-8", errors="replace")
        pass_count = sum(
            re.match(r"^(?:STRICT )?PASS ", line) is not None
            for line in stdout.splitlines()
        )
        fail_count = sum(
            re.match(r"^(?:STRICT )?FAIL ", line) is not None
            for line in stdout.splitlines()
        )
        expected = (row["expected_pass"], row["expected_fail"])
        _require(
            completed.returncode == 0,
            f"{row['name']} self-run exit={completed.returncode}",
        )
        _require(
            completed.stderr == b"",
            f"{row['name']} self-run emitted {len(completed.stderr)} stderr bytes",
        )
        _require(
            (pass_count, fail_count) == expected,
            (
                f"{row['name']} line recount {pass_count}/{fail_count} "
                f"!= {expected[0]}/{expected[1]}"
            ),
        )
        _require(
            _sha256(row["path"]) == current_pin,
            f"{row['name']} self-run changed its source bytes",
        )
        observed_rows.append(f"{row['name']}={pass_count}/{fail_count}")
    return "; ".join(observed_rows)


_PROBE_DRIVER = r"""
import json
import sys

import numpy as np
import physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18 as landed

records = []
for feed in json.load(sys.stdin):
    try:
        projector = landed.projector_bloch(feed["direction"])
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
    records.append({"probe_id": feed["probe_id"], "observation": record})
print(json.dumps(records, allow_nan=False, separators=(",", ":"), sort_keys=True))
"""


def probe_verdict_recount() -> str:
    """Drive the landed projector and independently compare all eight probes."""
    global _HONEST_LABEL_RESULT

    frozen = _frozen()
    bridge_row = next(
        row for row in frozen["self_runs"] if row["name"] == "bridge"
    )
    _require(
        _sha256(bridge_row["path"]) == bridge_row["sha256"],
        "bridge drifted before probe recount",
    )
    rows = list(frozen["lawful"]) + list(frozen["rejected"])
    feeds = [row["feed"] for row in rows]
    try:
        completed = subprocess.run(
            [sys.executable, "-c", _PROBE_DRIVER],
            cwd=ROOT,
            input=json.dumps(feeds, allow_nan=False),
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
            timeout=AUDIT_TIMEOUT_SEC,
        )
    except subprocess.TimeoutExpired as exc:
        raise CertificateError(
            f"landed probe driver timed out after {exc.timeout}s"
        ) from exc
    _require(completed.returncode == 0, f"probe driver exit={completed.returncode}")
    _require(
        completed.stderr == "",
        f"probe driver emitted {len(completed.stderr)} stderr characters",
    )
    try:
        decoded = json.loads(completed.stdout)
    except json.JSONDecodeError as exc:
        raise CertificateError("probe driver did not return one JSON record") from exc
    _require(
        isinstance(decoded, list) and len(decoded) == len(rows),
        "probe driver result count mismatch",
    )
    observations = {
        item.get("probe_id"): item.get("observation")
        for item in decoded
        if isinstance(item, dict)
    }
    _require(
        len(observations) == len(rows),
        "probe driver returned duplicate or malformed labels",
    )

    lawful_pass = 0
    for row in frozen["lawful"]:
        expected = row["expected"]
        expected_value = {
            key: value for key, value in expected.items() if key != "machine_bound"
        }
        if _numeric_match(
            observations.get(row["probe_id"]),
            expected_value,
            expected["machine_bound"],
        ):
            lawful_pass += 1
    _require(lawful_pass == 4, f"lawful frozen-value matches={lawful_pass}/4")

    landed_reject_pass = 0
    schema_row: dict[str, Any] | None = None
    for row in frozen["rejected"]:
        if row["enforcement"] == "landed_surface":
            if _same_json(observations.get(row["probe_id"]), row["expected"]):
                landed_reject_pass += 1
        elif row["enforcement"] == "harness_schema":
            schema_row = row
    _require(
        landed_reject_pass == 3,
        f"landed refusal signature matches={landed_reject_pass}/3",
    )
    _require(schema_row is not None, "missing harness-schema witness")
    schema_observed = observations.get(schema_row["probe_id"])
    honest = (
        schema_row["expected"].get("origin") == "harness_schema"
        and schema_row["expected"].get("exception_type") == "SchemaRefusal"
        and isinstance(schema_observed, dict)
        and schema_observed.get("origin") == "landed_surface"
        and schema_observed.get("status") == "returned"
    )
    _HONEST_LABEL_RESULT = (
        "PASS harness_schema witness is accepted by landed surface"
        if honest
        else "FAIL harness_schema witness was not shown to be harness-only"
    )
    _require(honest, "harness-schema witness enforcement label is not honest")
    _require(
        _sha256(bridge_row["path"]) == bridge_row["sha256"],
        "probe driver changed the bridge source bytes",
    )
    return "ACCEPT=4/4; landed REJECT=3/3; harness-only=1/1"


def _imported_names(tree: ast.AST) -> set[str]:
    names: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            names.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module is not None:
            names.add(node.module)
    return names


def _root_name(node: ast.AST) -> str | None:
    while isinstance(node, (ast.Attribute, ast.Subscript)):
        node = node.value
    return node.id if isinstance(node, ast.Name) else None


def _attribute_mutations(tree: ast.AST, alias: str) -> list[str]:
    mutations: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Attribute) and isinstance(
            node.ctx, (ast.Store, ast.Del)
        ) and _root_name(node) == alias:
            mutations.append(node.attr)
        elif (
            isinstance(node, ast.Subscript)
            and isinstance(node.ctx, (ast.Store, ast.Del))
            and _root_name(node) == alias
        ):
            mutations.append("<subscript>")
        elif (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id in {"setattr", "delattr"}
            and node.args
            and isinstance(node.args[0], ast.Name)
            and node.args[0].id == alias
        ):
            mutations.append(node.func.id)
    return mutations


def _function(tree: ast.Module, name: str) -> ast.FunctionDef:
    matches = [
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    if len(matches) != 1:
        raise CertificateError(f"{name}: expected one function definition")
    return matches[0]


def _contains_name(node: ast.AST, name: str) -> bool:
    return any(
        isinstance(child, ast.Name) and child.id == name
        for child in ast.walk(node)
    )


def _drift_path_audit(tree: ast.Module) -> tuple[bool, str]:
    function = _function(tree, "_sandbox_drift_demo")
    temp_names: set[str] = set()
    for node in ast.walk(function):
        if not isinstance(node, ast.With):
            continue
        for item in node.items:
            call = item.context_expr
            if (
                isinstance(call, ast.Call)
                and isinstance(call.func, ast.Attribute)
                and isinstance(call.func.value, ast.Name)
                and call.func.value.id == "tempfile"
                and call.func.attr == "TemporaryDirectory"
                and isinstance(item.optional_vars, ast.Name)
            ):
                temp_names.add(item.optional_vars.id)
    if not temp_names:
        return False, "no TemporaryDirectory-bound sandbox"

    sandbox_names: set[str] = set()
    for node in ast.walk(function):
        if not isinstance(node, ast.Assign):
            continue
        targets = [
            target.id for target in node.targets if isinstance(target, ast.Name)
        ]
        if (
            targets
            and any(_contains_name(node.value, name) for name in temp_names)
            and _contains_name(node.value, "AUDIT_INPUT_PATHS")
        ):
            sandbox_names.update(targets)
    if "sandbox_path" not in sandbox_names:
        return False, "sandbox copy path is not derived from temp dir and input name"

    copy_calls = [
        node
        for node in ast.walk(function)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and isinstance(node.func.value, ast.Name)
        and node.func.value.id == "shutil"
        and node.func.attr == "copyfile"
    ]
    copy_ok = (
        len(copy_calls) == 1
        and len(copy_calls[0].args) >= 2
        and _contains_name(copy_calls[0].args[0], "AUDIT_INPUT_PATHS")
        and isinstance(copy_calls[0].args[1], ast.Name)
        and copy_calls[0].args[1].id in sandbox_names
    )
    if not copy_ok:
        return False, "DRIFT copy is not landed-source to sandbox-destination"

    mutation_methods = {
        "chmod",
        "hardlink_to",
        "mkdir",
        "rename",
        "replace",
        "rmdir",
        "symlink_to",
        "touch",
        "unlink",
        "write_bytes",
        "write_text",
    }
    path_mutations: list[ast.Call] = []
    forbidden_open = False
    for node in ast.walk(function):
        if not isinstance(node, ast.Call):
            continue
        if (
            isinstance(node.func, ast.Attribute)
            and node.func.attr in mutation_methods
        ):
            path_mutations.append(node)
        if (
            (isinstance(node.func, ast.Name) and node.func.id == "open")
            or (isinstance(node.func, ast.Attribute) and node.func.attr == "open")
        ):
            mode_node = (
                node.args[1]
                if len(node.args) >= 2
                else next(
                    (
                        keyword.value
                        for keyword in node.keywords
                        if keyword.arg == "mode"
                    ),
                    None,
                )
            )
            if mode_node is None:
                continue
            try:
                mode = ast.literal_eval(mode_node)
            except (TypeError, ValueError, SyntaxError):
                forbidden_open = True
            else:
                forbidden_open |= isinstance(mode, str) and any(
                    marker in mode for marker in "wax+"
                )
    mutations_ok = (
        len(path_mutations) == 1
        and isinstance(path_mutations[0].func, ast.Attribute)
        and isinstance(path_mutations[0].func.value, ast.Name)
        and path_mutations[0].func.value.id in sandbox_names
        and path_mutations[0].func.attr == "write_bytes"
        and not forbidden_open
    )
    if not mutations_ok:
        return False, "a DRIFT write is not confined to sandbox_path.write_bytes"

    real_hash_reads = [
        node
        for node in ast.walk(function)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "_sha256_path"
        and node.args
        and _contains_name(node.args[0], "AUDIT_INPUT_PATHS")
    ]
    if len(real_hash_reads) < 2:
        return False, "real landed path is not hashed before and after sandbox demo"
    return True, "TemporaryDirectory copy; sole write=sandbox_path.write_bytes"


def discipline() -> str:
    """Audit literal tables, import isolation, and sandbox-only DRIFT writes."""
    frozen = _frozen()
    tree = frozen["tree"]
    landed_names = {Path(path).stem for path in AUDIT_INPUT_PATHS}
    outer_landed_imports = _imported_names(tree) & landed_names
    _require(not outer_landed_imports, "harness imports landed module in parent")

    driver_source = _literal(tree, "_SURFACE_DRIVER")
    _require(isinstance(driver_source, str), "_SURFACE_DRIVER is not literal text")
    driver_tree = ast.parse(driver_source, filename="<frozen-surface-driver>")
    bridge_name = Path(AUDIT_INPUT_PATHS[0]).stem
    landed_aliases = [
        alias.asname or alias.name
        for node in ast.walk(driver_tree)
        if isinstance(node, ast.Import)
        for alias in node.names
        if alias.name == bridge_name
    ]
    _require(
        landed_aliases == ["surface"],
        "surface driver does not have one explicit landed alias",
    )
    _require(
        not _attribute_mutations(driver_tree, "surface"),
        "surface driver writes through its landed-module alias",
    )

    literal_names = (
        "AUDIT_INPUT_PATHS",
        "FROZEN_SELF_RUNS",
        "FROZEN_LAWFUL_PROBES",
        "FROZEN_REJECT_WITNESSES",
        "QUARANTINED_WRONG_EXPECTATION",
    )
    for name in literal_names:
        _literal(tree, name)

    drift_ok, drift_detail = _drift_path_audit(tree)
    _require(drift_ok, drift_detail)
    _require(
        not _HARNESS_WAS_PRELOADED
        and all(name not in sys.modules for name in BLOCKLIST),
        "blocklisted harness appeared in sys.modules",
    )
    _require(
        all(name not in sys.modules for name in landed_names),
        "landed module escaped a child process into checker sys.modules",
    )
    return (
        "no landed attribute writes; frozen tables literal; "
        f"DRIFT={drift_detail}; blocklist clean"
    )


def _one_line(value: object, limit: int = 700) -> str:
    text = " ".join(str(value).split())
    return text if len(text) <= limit else text[: limit - 1] + "…"


def _run_certificate(
    index: int, name: str, function: Callable[[], str]
) -> bool:
    try:
        detail = function()
    except Exception as exc:
        print(
            f"FAIL {index}/5 {name} :: "
            f"{type(exc).__name__}: {_one_line(exc)}"
        )
        return False
    print(f"PASS {index}/5 {name} :: {_one_line(detail)}")
    return True


def main() -> int:
    checks = (
        ("extraction", extraction),
        ("byte_pin_recount", byte_pin_recount),
        ("self_run_recount", self_run_recount),
        ("probe_verdict_recount", probe_verdict_recount),
        ("discipline", discipline),
    )
    results = [
        _run_certificate(index, name, function)
        for index, (name, function) in enumerate(checks, start=1)
    ]
    passed = sum(results)
    print(f"SUMMARY {passed}/{len(results)} {'PASS' if passed == len(results) else 'FAIL'}")
    print(f"HONEST_LABEL {_HONEST_LABEL_RESULT}")
    print(f"RUNTIME {time.monotonic() - _START:.6f}s")
    return int(passed != len(results))


if __name__ == "__main__":
    raise SystemExit(main())
