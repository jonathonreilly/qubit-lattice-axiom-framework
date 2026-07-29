#!/usr/bin/env python3
"""Independent, data-only checker for the full-Fock acceptance port."""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/FULL_FOCK_ACCEPTANCE_PORT_SUPPORT_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_full_fock_unit_weight_source_2026_07_28.py",
)

import ast
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time


ROOT = Path(__file__).resolve().parents[1]
PORT_PATH = ROOT / "scripts/frontier_full_fock_acceptance_port_2026_07_28.py"
SURFACE_PATH = ROOT / AUDIT_INPUT_PATHS[0]
BLOCKLIST = ("frontier_full_fock_acceptance_port_2026_07_28",)


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _module_assignments(tree: ast.Module) -> dict[str, ast.AST]:
    assignments: dict[str, ast.AST] = {}
    for statement in tree.body:
        if (
            isinstance(statement, ast.Assign)
            and len(statement.targets) == 1
            and isinstance(statement.targets[0], ast.Name)
        ):
            assignments[statement.targets[0].id] = statement.value
        elif (
            isinstance(statement, ast.AnnAssign)
            and isinstance(statement.target, ast.Name)
            and statement.value is not None
        ):
            assignments[statement.target.id] = statement.value
    return assignments


def _static_value(
    node: ast.AST,
    assignments: dict[str, ast.AST],
    resolving: frozenset[str] = frozenset(),
) -> object:
    """Evaluate literals and references to other module-level literals only."""
    if isinstance(node, ast.Constant):
        return node.value
    if isinstance(node, ast.Tuple):
        return tuple(_static_value(item, assignments, resolving) for item in node.elts)
    if isinstance(node, ast.List):
        return [_static_value(item, assignments, resolving) for item in node.elts]
    if isinstance(node, ast.Set):
        return {_static_value(item, assignments, resolving) for item in node.elts}
    if isinstance(node, ast.Dict):
        return {
            _static_value(key, assignments, resolving): _static_value(
                value, assignments, resolving
            )
            for key, value in zip(node.keys, node.values, strict=True)
            if key is not None
        }
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
        value = _static_value(node.operand, assignments, resolving)
        if not isinstance(value, (int, float, complex)):
            raise ValueError("unary sign applied to a non-number")
        return value if isinstance(node.op, ast.UAdd) else -value
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
        return _static_value(node.left, assignments, resolving) + _static_value(
            node.right, assignments, resolving
        )
    if isinstance(node, ast.Name):
        if node.id in resolving or node.id not in assignments:
            raise ValueError(f"non-literal or cyclic name: {node.id}")
        return _static_value(
            assignments[node.id], assignments, resolving | {node.id}
        )
    raise ValueError(f"dynamic frozen expression: {type(node).__name__}")


def _function(tree: ast.Module, name: str) -> ast.FunctionDef:
    matches = [
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    if len(matches) != 1:
        raise ValueError(f"expected one function {name}, observed {len(matches)}")
    return matches[0]


def _root_name(node: ast.AST) -> str | None:
    while isinstance(node, (ast.Attribute, ast.Subscript, ast.Starred)):
        node = node.value
    return node.id if isinstance(node, ast.Name) else None


def _subscript_chain(node: ast.AST) -> tuple[str, tuple[object, ...]] | None:
    keys: list[object] = []
    while isinstance(node, ast.Subscript):
        try:
            keys.append(ast.literal_eval(node.slice))
        except (ValueError, TypeError):
            return None
        node = node.value
    if not isinstance(node, ast.Name):
        return None
    return node.id, tuple(reversed(keys))


def _extract_conventions(tree: ast.Module) -> dict[str, object]:
    drift = _function(tree, "drift_demo")
    verdict = _function(tree, "verdict_against")
    main = _function(tree, "main")

    xor_masks = [
        ast.literal_eval(node.value)
        for node in ast.walk(drift)
        if isinstance(node, ast.AugAssign)
        and isinstance(node.op, ast.BitXor)
        and _root_name(node.target) == "mutated"
    ]
    write_receivers = [
        _root_name(node.func.value)
        for node in ast.walk(drift)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr == "write_bytes"
    ]
    sandbox_constructor = any(
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "FullFockAcceptance"
        and any(
            keyword.arg == "source_path"
            and isinstance(keyword.value, ast.Name)
            and keyword.value.id == "sandbox_path"
            for keyword in node.keywords
        )
        for node in ast.walk(drift)
    )
    temporary_directory = any(
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and isinstance(node.func.value, ast.Name)
        and node.func.value.id == "tempfile"
        and node.func.attr == "TemporaryDirectory"
        for node in ast.walk(drift)
    )
    verdict_constants = {
        node.value
        for node in ast.walk(verdict)
        if isinstance(node, ast.Constant) and isinstance(node.value, str)
    }

    adversary_override = None
    quarantined_value = None
    wrong_expected_is_copy = False
    wrong_verdict_is_comparison = False
    for node in ast.walk(main):
        if isinstance(node, ast.Assign) and len(node.targets) == 1:
            chain = _subscript_chain(node.targets[0])
            if chain == (
                "wrong_expected",
                ("accept", "anchor", "emitted_weight"),
            ):
                adversary_override = ast.literal_eval(node.value)
            if (
                isinstance(node.targets[0], ast.Name)
                and node.targets[0].id == "wrong_expected"
                and isinstance(node.value, ast.Call)
                and isinstance(node.value.func, ast.Attribute)
                and node.value.func.attr == "frozen_expected"
            ):
                wrong_expected_is_copy = True
        if isinstance(node, ast.Compare) and len(node.ops) == 1:
            chain = _subscript_chain(node.left)
            if chain == (
                "FROZEN_EXPECTED",
                ("accept", "anchor", "emitted_weight"),
            ):
                quarantined_value = ast.literal_eval(node.comparators[0])
            if (
                isinstance(node.left, ast.Name)
                and node.left.id == "wrong_verdict"
                and isinstance(node.ops[0], ast.Eq)
                and ast.literal_eval(node.comparators[0]) == "REJECT"
            ):
                wrong_verdict_is_comparison = True

    return {
        "adversary_override": adversary_override,
        "adversary_verdict_is_reject": wrong_verdict_is_comparison,
        "drift_sandbox_constructor": sandbox_constructor,
        "drift_temporary_directory": temporary_directory,
        "drift_verdict_present": "DRIFT" in verdict_constants,
        "drift_write_receivers": tuple(write_receivers),
        "drift_xor_masks": tuple(xor_masks),
        "quarantined_value": quarantined_value,
        "wrong_expected_is_copy": wrong_expected_is_copy,
    }


def extraction() -> dict[str, object]:
    """AST-extract every frozen port expectation without importing the port."""
    port_source = PORT_PATH.read_text(encoding="utf-8")
    port_tree = ast.parse(port_source, filename=str(PORT_PATH))
    assignments = _module_assignments(port_tree)
    frozen = _static_value(assignments["FROZEN_EXPECTED"], assignments)
    pin = _static_value(assignments["FULL_FOCK_SHA256"], assignments)
    labels = _static_value(assignments["SELF_RUN_LABELS"], assignments)

    own_tree = ast.parse(
        Path(__file__).read_text(encoding="utf-8"), filename=str(__file__)
    )
    own_assignments = _module_assignments(own_tree)
    audit_node = own_assignments["AUDIT_INPUT_PATHS"]
    audit_paths = ast.literal_eval(audit_node)

    accept = frozen["accept"]
    reject = frozen["reject"]
    conventions = _extract_conventions(port_tree)
    tables_literal_backed = all(
        _static_value(assignments[name], assignments) is not None
        for name in ("SELF_RUN_LABELS", "FROZEN_EXPECTED")
    )
    passed = (
        pin == frozen["source_sha256"]
        and frozen["self_run"]["pass"] == 8
        and frozen["self_run"]["fail"] == 0
        and frozen["self_run"]["total"] == 8
        and frozen["self_run"]["summary"] == {"pass": 8, "fail": 0}
        and tuple(frozen["self_run"]["labels"]) == tuple(labels)
        and len(labels) == 8
        and set(accept) == {
            "anchor",
            "layer_channels",
            "probe_mode",
            "recoil_triples",
        }
        and len(reject) == 3
        and {
            name: row["label"] for name, row in reject.items()
        }
        == {
            "malformed_feed": "port-schema",
            "misembedded_layer": "landed-control",
            "out_of_domain": "port-schema",
        }
        and audit_paths == AUDIT_INPUT_PATHS
        and len(audit_paths) == 1
        and isinstance(audit_node, ast.Tuple)
        and tables_literal_backed
        and conventions["drift_verdict_present"] is True
        and conventions["adversary_verdict_is_reject"] is True
    )
    return {
        "accept_count": 3,
        "audit_paths": audit_paths,
        "conventions": conventions,
        "frozen": frozen,
        "literal_tables": tables_literal_backed,
        "passed": passed,
        "pin": pin,
        "port_source": port_source,
        "port_tree": port_tree,
        "reject_count": len(reject),
    }


def _run_surface(
    extra_arguments: tuple[str, ...] = (),
    stdin_text: str | None = None,
) -> dict[str, object]:
    environment = os.environ.copy()
    scripts_path = str(ROOT / "scripts")
    environment["PYTHONPATH"] = (
        scripts_path
        if not environment.get("PYTHONPATH")
        else scripts_path + os.pathsep + environment["PYTHONPATH"]
    )
    started = time.monotonic()
    completed = subprocess.run(
        [sys.executable, str(SURFACE_PATH), *extra_arguments],
        cwd=ROOT,
        env=environment,
        input=stdin_text,
        capture_output=True,
        check=False,
        text=True,
        timeout=AUDIT_TIMEOUT_SEC,
    )
    elapsed = time.monotonic() - started
    rows: list[dict[str, object]] = []
    terminals: list[dict[str, object] | None] = []
    row_pattern = re.compile(r"^(PASS|FAIL) (.*?) :: (.*)$")
    for line in completed.stdout.splitlines():
        match = row_pattern.match(line)
        if match:
            status, label, detail_text = match.groups()
            try:
                detail = ast.literal_eval(detail_text)
            except (SyntaxError, ValueError):
                detail = None
            rows.append(
                {"detail": detail, "label": label, "pass": status == "PASS"}
            )
        if line.startswith("FINAL_JSON "):
            try:
                terminals.append(json.loads(line[len("FINAL_JSON ") :]))
            except json.JSONDecodeError:
                terminals.append(None)
    return {
        "arguments": extra_arguments,
        "returncode": completed.returncode,
        "rows": rows,
        "runtime_seconds": elapsed,
        "stderr_empty": completed.stderr == "",
        "stdout_bytes": len(completed.stdout.encode("utf-8")),
        "terminal": terminals[0] if len(terminals) == 1 else None,
        "terminal_count": len(terminals),
    }


def _clean_surface_run(
    run: dict[str, object], frozen_self_run: dict[str, object]
) -> bool:
    rows = run["rows"]
    terminal = run["terminal"]
    labels = tuple(row["label"] for row in rows)
    return (
        run["returncode"] == 0
        and run["stderr_empty"] is True
        and len(rows) == frozen_self_run["total"]
        and sum(row["pass"] is True for row in rows) == frozen_self_run["pass"]
        and sum(row["pass"] is False for row in rows) == frozen_self_run["fail"]
        and labels == tuple(frozen_self_run["labels"])
        and run["terminal_count"] == 1
        and isinstance(terminal, dict)
        and terminal.get("summary") == frozen_self_run["summary"]
        and terminal.get("full_fock_construction_achieved") is True
    )


def pin_and_selfrun_recount(extracted: dict[str, object]) -> dict[str, object]:
    """Recompute the byte pin and independently recount the surface certificate."""
    before = _sha256(SURFACE_PATH)
    run = _run_surface()
    after = _sha256(SURFACE_PATH)
    frozen = extracted["frozen"]
    expected_pin = extracted["pin"]
    clean = _clean_surface_run(run, frozen["self_run"])
    passed = before == expected_pin == after and clean
    return {
        "after": after,
        "before": before,
        "clean": clean,
        "fail": sum(row["pass"] is False for row in run["rows"]),
        "pass": sum(row["pass"] is True for row in run["rows"]),
        "passed": passed,
        "run": run,
        "terminal": frozen["self_run"]["terminal_marker"],
        "total": len(run["rows"]),
    }


def _detail_containing(
    run: dict[str, object], fragment: str
) -> tuple[bool, object]:
    matches = [
        row
        for row in run["rows"]
        if fragment in str(row["label"])
    ]
    if len(matches) != 1:
        return False, None
    return matches[0]["pass"] is True, matches[0]["detail"]


def _axis_direction_keys() -> tuple[str, ...]:
    vectors = []
    for axis in range(3):
        for sign in (-1, 1):
            vector = [0, 0, 0]
            vector[axis] = sign
            vectors.append(",".join(str(component) for component in vector))
    return tuple(sorted(vectors))


def _parse_recoil_multipliers(equation: str) -> dict[str, int] | None:
    match = re.fullmatch(
        r"Delta P_matter=([+-]?\d+) d; P_F=([+-])d; P_A=([+-])d",
        equation,
    )
    if not match:
        return None
    matter, mediator_sign, auxiliary_sign = match.groups()
    return {
        "auxiliary": 1 if auxiliary_sign == "+" else -1,
        "matter": int(matter),
        "mediator": 1 if mediator_sign == "+" else -1,
    }


def probe_recount(
    extracted: dict[str, object],
    canonical: dict[str, object],
) -> dict[str, object]:
    """Re-derive ACCEPT tables and directly classify every REJECT witness."""
    frozen = extracted["frozen"]
    accept = frozen["accept"]
    frozen_self_run = frozen["self_run"]

    anchor_ok, anchor_detail = _detail_containing(
        canonical, "reproduces all six landed"
    )
    anchor_expected = accept["anchor"]
    anchor_range = (
        tuple(anchor_detail.get("emitted_weight_range", ()))
        if isinstance(anchor_detail, dict)
        else ()
    )
    anchor_residual = (
        anchor_detail.get("maximum_component_residual")
        if isinstance(anchor_detail, dict)
        else None
    )
    anchor_matches = (
        anchor_ok
        and anchor_expected["directions"] == 6
        and len(anchor_range) == 2
        and all(
            abs(float(weight) - anchor_expected["emitted_weight"])
            <= anchor_expected["weight_absolute_tolerance"]
            for weight in anchor_range
        )
        and isinstance(anchor_residual, (int, float))
        and anchor_residual < anchor_expected["component_residual_upper_bound"]
    )

    layers_ok, layers_detail = _detail_containing(
        canonical, "every allowed channel through n_max"
    )
    output_layers = (
        layers_detail.get("layers", [])
        if isinstance(layers_detail, dict)
        else []
    )
    numbers = tuple(row.get("number") for row in output_layers)
    channels = tuple(row.get("active_channels") for row in output_layers)
    layer_matches = (
        layers_ok
        and numbers == tuple(accept["layer_channels"]["numbers"])
        and channels == tuple(accept["layer_channels"]["active_channels"])
        and all(row.get("generator_ledger_residual") == 0.0 for row in output_layers)
    )

    equation = (
        layers_detail.get("recoil_equation", "")
        if isinstance(layers_detail, dict)
        else ""
    )
    multipliers = _parse_recoil_multipliers(equation)
    direction_keys = _axis_direction_keys()
    derived_layers = []
    for row in output_layers:
        active = row.get("active_channels")
        number = row.get("number")
        residual = row.get("generator_ledger_residual")
        if not isinstance(active, int) or active < 0 or active % 6:
            multiplicities = None
        elif active == 0:
            multiplicities = {}
        else:
            multiplicities = {
                key: active // 6 for key in direction_keys
            }
        derived_layers.append(
            {
                "active_channels": active,
                "direction_multiplicities": multiplicities,
                "exact_triples": active if residual == 0.0 else 0,
                "number": number,
            }
        )
    derived_recoil = {
        "layers": tuple(derived_layers),
        "maximum_component_residual": max(
            (
                float(row.get("generator_ledger_residual", float("inf")))
                for row in output_layers
            ),
            default=float("inf"),
        ),
        "multipliers": multipliers,
    }
    recoil_matches = derived_recoil == accept["recoil_triples"]

    out_of_domain = _run_surface(("--n-max", "3"))
    malformed_feed = _run_surface(
        ("--feed-shape", "2,6"),
        stdin_text=json.dumps([[1] * 6 for _ in range(2)]),
    )
    misembedded_ok, misembedded_detail = _detail_containing(
        canonical, "deliberate n=2 to n=1 mis-embedding"
    )
    misembedded_signature = (
        "LANDED_CONTROL:MIS_EMBEDDING_DETECTED:"
        f"number={misembedded_detail.get('source_number')}"
        f"->{misembedded_detail.get('target_number')}"
        if isinstance(misembedded_detail, dict)
        else ""
    )
    schema_surface_ignores = {
        "out_of_domain": _clean_surface_run(out_of_domain, frozen_self_run),
        "malformed_feed": _clean_surface_run(malformed_feed, frozen_self_run),
    }
    reject = frozen["reject"]
    label_honesty = {
        "malformed_feed": (
            "PORT_SCHEMA_HONEST"
            if schema_surface_ignores["malformed_feed"]
            and reject["malformed_feed"]["label"] == "port-schema"
            and reject["malformed_feed"]["signature"]
            == "PORT_SCHEMA:MALFORMED_FEED_SHAPE:"
            "expected=[3, 6]:observed=[2, 6]"
            else "DISHONEST"
        ),
        "misembedded_layer": (
            "SURFACE_CONTROL_HONEST"
            if misembedded_ok
            and isinstance(misembedded_detail, dict)
            and misembedded_detail.get("source_number") == 2
            and misembedded_detail.get("target_number") == 1
            and misembedded_detail.get("cross_layer_generator_amplitude") == 1.0
            and misembedded_detail.get("number_commutator_frobenius", 0.0) > 1.4
            and reject["misembedded_layer"]["label"] == "landed-control"
            and reject["misembedded_layer"]["signature"] == misembedded_signature
            else "DISHONEST"
        ),
        "out_of_domain": (
            "PORT_SCHEMA_HONEST"
            if schema_surface_ignores["out_of_domain"]
            and reject["out_of_domain"]["label"] == "port-schema"
            and reject["out_of_domain"]["signature"]
            == "PORT_SCHEMA:N_MAX_OUT_OF_SCOPE:requested=3:declared=2"
            else "DISHONEST"
        ),
    }
    passed = (
        anchor_matches
        and layer_matches
        and recoil_matches
        and all(verdict != "DISHONEST" for verdict in label_honesty.values())
        and _sha256(SURFACE_PATH) == extracted["pin"]
    )
    return {
        "anchor": anchor_range,
        "anchor_matches": anchor_matches,
        "channels": channels,
        "label_honesty": label_honesty,
        "layer_matches": layer_matches,
        "multipliers": multipliers,
        "passed": passed,
        "recoil_matches": recoil_matches,
        "schema_run_seconds": (
            out_of_domain["runtime_seconds"] + malformed_feed["runtime_seconds"]
        ),
    }


def _assignment_targets(node: ast.AST) -> tuple[ast.AST, ...]:
    if isinstance(node, ast.Assign):
        return tuple(node.targets)
    if isinstance(node, ast.AnnAssign):
        return (node.target,)
    if isinstance(node, ast.AugAssign):
        return (node.target,)
    if isinstance(node, ast.NamedExpr):
        return (node.target,)
    if isinstance(node, ast.Delete):
        return tuple(node.targets)
    return ()


def discipline(extracted: dict[str, object]) -> dict[str, object]:
    """Prove port immutability, literal freezing, and sandbox-only drift."""
    tree = extracted["port_tree"]
    surface_aliases = {
        alias.asname or alias.name.rsplit(".", 1)[-1]
        for node in tree.body
        if isinstance(node, ast.Import)
        for alias in node.names
        if alias.name
        == "frontier_full_fock_unit_weight_source_2026_07_28"
    }
    attribute_writes = sorted(
        {
            ast.unparse(target)
            for node in ast.walk(tree)
            for target in _assignment_targets(node)
            if _root_name(target) in surface_aliases
        }
    )
    dynamic_attribute_writes = sorted(
        {
            ast.unparse(node)
            for node in ast.walk(tree)
            if isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id in {"setattr", "delattr"}
            and node.args
            and _root_name(node.args[0]) in surface_aliases
        }
    )

    own_tree = ast.parse(
        Path(__file__).read_text(encoding="utf-8"), filename=str(__file__)
    )
    blocked_imports = sorted(
        {
            imported
            for node in ast.walk(own_tree)
            for imported in (
                [alias.name for alias in node.names]
                if isinstance(node, ast.Import)
                else [node.module]
                if isinstance(node, ast.ImportFrom) and node.module
                else []
            )
            if imported in BLOCKLIST
        }
    )
    runtime_blocked_imports = sorted(set(BLOCKLIST) & set(sys.modules))

    conventions = extracted["conventions"]
    drift_sandbox_only = (
        conventions["drift_temporary_directory"] is True
        and conventions["drift_sandbox_constructor"] is True
        and conventions["drift_xor_masks"] == (1,)
        and conventions["drift_write_receivers"] == (
            "sandbox_path",
            "sandbox_path",
        )
        and conventions["drift_verdict_present"] is True
    )
    adversary_quarantined = (
        conventions["wrong_expected_is_copy"] is True
        and conventions["adversary_override"] == 0.2258992161287137
        and conventions["quarantined_value"] == 0.1258992161287137
        and conventions["adversary_verdict_is_reject"] is True
    )
    passed = (
        bool(surface_aliases)
        and not attribute_writes
        and not dynamic_attribute_writes
        and extracted["literal_tables"] is True
        and drift_sandbox_only
        and adversary_quarantined
        and not blocked_imports
        and not runtime_blocked_imports
    )
    return {
        "adversary_quarantined": adversary_quarantined,
        "attribute_writes": attribute_writes,
        "blocked_imports": blocked_imports,
        "drift_sandbox_only": drift_sandbox_only,
        "dynamic_attribute_writes": dynamic_attribute_writes,
        "literal_tables": extracted["literal_tables"],
        "passed": passed,
        "runtime_blocked_imports": runtime_blocked_imports,
        "surface_aliases": tuple(sorted(surface_aliases)),
    }


def _result_line(name: str, passed: bool, detail: str) -> str:
    status = "PASS" if passed else "FAIL"
    return f"{status} {name} :: {detail}"


def main() -> int:
    started = time.monotonic()
    results: list[tuple[str, bool, str]] = []
    extracted: dict[str, object] | None = None
    selfrun: dict[str, object] | None = None
    probes: dict[str, object] | None = None

    try:
        extracted = extraction()
        results.append(
            (
                "extraction",
                bool(extracted["passed"]),
                f"pin={extracted['pin']} self=8/8 accept=3 reject=3 "
                f"audit_tuple={len(extracted['audit_paths'])}",
            )
        )
    except Exception as exc:
        results.append(
            ("extraction", False, f"{type(exc).__name__}:{str(exc)[:240]}")
        )

    if extracted is not None:
        try:
            selfrun = pin_and_selfrun_recount(extracted)
            results.append(
                (
                    "pin_and_selfrun_recount",
                    bool(selfrun["passed"]),
                    f"sha256={selfrun['after']} rows={selfrun['pass']}/"
                    f"{selfrun['total']} fail={selfrun['fail']} "
                    f"terminal={selfrun['terminal']}",
                )
            )
        except Exception as exc:
            results.append(
                (
                    "pin_and_selfrun_recount",
                    False,
                    f"{type(exc).__name__}:{str(exc)[:240]}",
                )
            )
    else:
        results.append(
            ("pin_and_selfrun_recount", False, "blocked_by_extraction")
        )

    if extracted is not None and selfrun is not None:
        try:
            probes = probe_recount(extracted, selfrun["run"])
            honesty = ",".join(
                f"{name}={verdict}"
                for name, verdict in sorted(probes["label_honesty"].items())
            )
            results.append(
                (
                    "probe_recount",
                    bool(probes["passed"]),
                    f"anchor={probes['anchor']} channels={probes['channels']} "
                    f"recoil={probes['multipliers']} labels={honesty}",
                )
            )
        except Exception as exc:
            results.append(
                ("probe_recount", False, f"{type(exc).__name__}:{str(exc)[:240]}")
            )
    else:
        results.append(("probe_recount", False, "blocked_by_selfrun"))

    if extracted is not None:
        try:
            disciplined = discipline(extracted)
            results.append(
                (
                    "discipline",
                    bool(disciplined["passed"]),
                    f"surface_writes={len(disciplined['attribute_writes']) + len(disciplined['dynamic_attribute_writes'])} "
                    f"drift_sandbox_only={disciplined['drift_sandbox_only']} "
                    f"literal_tables={disciplined['literal_tables']} "
                    f"port_imported={bool(disciplined['runtime_blocked_imports'])}",
                )
            )
        except Exception as exc:
            results.append(
                ("discipline", False, f"{type(exc).__name__}:{str(exc)[:240]}")
            )
    else:
        results.append(("discipline", False, "blocked_by_extraction"))

    for name, passed, detail in results:
        print(_result_line(name, passed, detail))

    passed_count = sum(passed for _name, passed, _detail in results)
    runtime = time.monotonic() - started
    recount = (
        f"{selfrun['pass']}/{selfrun['total']}"
        if selfrun is not None
        else "unavailable"
    )
    labels = (
        ",".join(
            f"{name}:{verdict}"
            for name, verdict in sorted(probes["label_honesty"].items())
        )
        if probes is not None
        else "unavailable"
    )
    print(
        f"FINAL {passed_count}/{len(results)} | recount={recount} | "
        f"labels={labels} | runtime_seconds={runtime:.6f}"
    )
    return int(passed_count != len(results))


if __name__ == "__main__":
    raise SystemExit(main())
