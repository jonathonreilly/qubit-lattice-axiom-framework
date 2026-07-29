#!/usr/bin/env python3
"""Independent checker for the Cycle-725 coherent source-lift tournament.

The Cycle-725 primary is never imported.  Its tables, frozen dispositions,
pin paths, and rerun declarations are read only through Python's AST.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/COHERENT_SOURCE_LIFT_TOURNAMENT_CYCLE725_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle725_coherent_source_lift_tournament_2026_07_28.py",
    "scripts/frontier_cycle722_epoch_fed_endpoint_interval_harness_2026_07_28.py",
    )
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from time import perf_counter
from typing import Callable


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
PRIMARY_PATH = AUDIT_INPUT_PATHS[0]
PRIMARY_MODULE = "frontier_cycle725_coherent_source_lift_tournament_2026_07_28"
TOP_LEVEL_BLOCKLIST = {PRIMARY_MODULE}

if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import frontier_cycle722_epoch_fed_endpoint_interval_harness_2026_07_28 as F722


_BLOCKED_AFTER_IMPORTS = sorted(TOP_LEVEL_BLOCKLIST & set(sys.modules))
assert not _BLOCKED_AFTER_IMPORTS, (
    f"Cycle-725 primary imported transitively: {_BLOCKED_AFTER_IMPORTS}"
)

VARIANTS = ("primary", "alternate_port")
STAGES = ("A", "B", "C", "D", "E")
SHAPE = (2, 2, 2)
PACKET_FIELDS = (
    "certificate",
    "binder",
    "actuality",
    "admissibility",
    "law_domain",
)
EXPECTED_PRIMARY_INPUTS = (
    "scripts/frontier_cycle722_epoch_fed_endpoint_interval_harness_2026_07_28.py",
    "scripts/signed_gravity_oriented_tensor_source_lift.py",
    "scripts/two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18.py",
    "scripts/unit_weight_carried_link_recoil_cycle320_2026_07_18.py",
    "scripts/physical_m2_gravity_source_bridge_tournament_synthesis_cycle294_2026_07_17.py",
)
EXPECTED_STAGE_VECTOR = (225, 9, 112, 17304, 24, 225, 18, 0, 17304, 24)
EXPECTED_WARD_VALUES = (
    "residuals(+,-,0)=['1.9e+04', '1.9e+04', '0.0e+00']"
)
HARNESS_EXPECTATIONS = (
    {
        "path": "scripts/signed_gravity_oriented_tensor_source_lift.py",
        "pass_line_count": 7,
        "marker": (
            "FINAL_TAG: "
            "SIGNED_GRAVITY_ORIENTED_TENSOR_SOURCE_LIFT_FINITE_CONDITIONAL"
        ),
    },
    {
        "path": (
            "scripts/"
            "two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18.py"
        ),
        "pass_line_count": 20,
        "marker": "RESULT TWO_CELL_TWO_SOURCE_RECOIL_RECIPROCITY_CERTIFIED",
    },
    {
        "path": (
            "scripts/"
            "physical_m2_gravity_source_bridge_tournament_synthesis_"
            "cycle294_2026_07_17.py"
        ),
        "pass_line_count": 5,
        "marker": None,
    },
)
CHECKS: list[dict[str, object]] = []


def module_assignment(tree: ast.Module, name: str) -> ast.AST:
    values = []
    for node in tree.body:
        if isinstance(node, ast.Assign):
            targets = node.targets
            value = node.value
        elif isinstance(node, ast.AnnAssign):
            targets = (node.target,)
            value = node.value
        else:
            continue
        if value is not None and any(
            isinstance(target, ast.Name) and target.id == name
            for target in targets
        ):
            values.append(value)
    if len(values) != 1:
        raise ValueError(("module assignment", name, len(values)))
    return values[0]


def function_definition(tree: ast.Module, name: str) -> ast.FunctionDef:
    rows = [
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    if len(rows) != 1:
        raise ValueError(("function definition", name, len(rows)))
    return rows[0]


def literal_assignment(
    tree: ast.Module,
    name: str,
) -> tuple[object | None, str | None, ast.AST]:
    node = module_assignment(tree, name)
    try:
        return ast.literal_eval(node), None, node
    except (ValueError, TypeError, SyntaxError) as exc:
        return None, f"{type(exc).__name__}: {exc}", node


def call_path(node: ast.AST) -> str | None:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        prefix = call_path(node.value)
        return f"{prefix}.{node.attr}" if prefix else node.attr
    return None


def assignment_targets(node: ast.AST) -> tuple[ast.AST, ...]:
    if isinstance(node, (ast.Tuple, ast.List)):
        return tuple(
            child
            for element in node.elts
            for child in assignment_targets(element)
        )
    if isinstance(node, ast.Starred):
        return assignment_targets(node.value)
    return (node,)


def attribute_root(node: ast.AST) -> str | None:
    while isinstance(node, (ast.Attribute, ast.Subscript)):
        node = node.value
    return node.id if isinstance(node, ast.Name) else None


def source_tree() -> tuple[str, ast.Module]:
    source = (ROOT / PRIMARY_PATH).read_text(encoding="utf-8")
    return source, ast.parse(source, filename=PRIMARY_PATH)


def git_head_bytes(relative: str) -> tuple[bytes | None, dict[str, object]]:
    run = subprocess.run(
        ["git", "-C", str(ROOT), "show", f"HEAD:{relative}"],
        capture_output=True,
        check=False,
    )
    detail = {
        "returncode": run.returncode,
        "stderr_tail": run.stderr.decode(
            "utf-8", errors="replace"
        ).splitlines()[-4:],
    }
    return (run.stdout if run.returncode == 0 else None), detail


def extracted_harness_calls(tree: ast.Module) -> tuple[dict[str, object], ...]:
    main_node = function_definition(tree, "main")
    rows = []
    for node in ast.walk(main_node):
        if (
            isinstance(node, ast.Call)
            and call_path(node.func) == "run_unchanged"
            and node.args
            and isinstance(node.args[0], ast.Constant)
            and isinstance(node.args[0].value, str)
        ):
            marker = None
            if len(node.args) >= 2 and isinstance(node.args[1], ast.Constant):
                marker = node.args[1].value
            rows.append({
                "path": node.args[0].value,
                "marker": marker,
                "line": node.lineno,
            })
    return tuple(sorted(rows, key=lambda row: int(row["line"])))


def schema_extraction() -> dict[str, object]:
    _source, tree = source_tree()
    names = (
        "AUDIT_INPUT_PATHS",
        "CENSUS_SCHEMA_TABLE",
        "CENSUS_TO_TENSOR_REDUCTION",
        "STAGE_RESOLVED_TO_TENSOR_REDUCTION",
        "S1_STAGE_RESOLVED_FROZEN_DISPOSITION",
    )
    extracted: dict[str, object] = {}
    literal_errors: dict[str, str] = {}
    literal_nodes: dict[str, ast.AST] = {}
    for name in names:
        value, error, node = literal_assignment(tree, name)
        extracted[name] = value
        literal_nodes[name] = node
        if error is not None:
            literal_errors[name] = error

    own_source = Path(__file__).read_text(encoding="utf-8")
    own_tree = ast.parse(own_source, filename=str(Path(__file__)))
    own_audit, own_error, own_node = literal_assignment(
        own_tree, "AUDIT_INPUT_PATHS"
    )
    if own_error is not None:
        literal_errors["checker.AUDIT_INPUT_PATHS"] = own_error

    primary_audit = extracted["AUDIT_INPUT_PATHS"]
    census_schema = extracted["CENSUS_SCHEMA_TABLE"]
    role_reduction = extracted["CENSUS_TO_TENSOR_REDUCTION"]
    stage_reduction = extracted["STAGE_RESOLVED_TO_TENSOR_REDUCTION"]
    disposition = extracted["S1_STAGE_RESOLVED_FROZEN_DISPOSITION"]

    audit_literals_valid = bool(
        isinstance(literal_nodes["AUDIT_INPUT_PATHS"], ast.Tuple)
        and isinstance(primary_audit, tuple)
        and primary_audit == EXPECTED_PRIMARY_INPUTS
        and isinstance(own_node, ast.Tuple)
        and isinstance(own_audit, tuple)
        and own_audit == AUDIT_INPUT_PATHS
    )
    schema_fields = (
        tuple(row["field"] for row in census_schema)
        if isinstance(census_schema, tuple)
        and all(isinstance(row, dict) and "field" in row for row in census_schema)
        else ()
    )
    expected_schema_fields = (
        "variant",
        "shape",
        "role_stats.<packet_field>.retained_register",
        "role_stats.<packet_field>.retained_witness_valid",
        "role_stats.<packet_field>.total_register_touches",
        "role_stats.<packet_field>.admitted_stage_e_read_touches",
        "stage_e_admissions",
        "walk",
    )
    census_schema_valid = schema_fields == expected_schema_fields

    role_reduction_valid = bool(
        isinstance(role_reduction, tuple)
        and len(role_reduction) == 10
        and tuple(int(row["canonical_slot"]) for row in role_reduction)
        == tuple(range(10))
        and {
            (str(row["variant"]), str(row["packet_role"]))
            for row in role_reduction
        }
        == {
            (variant, role)
            for variant in VARIANTS
            for role in PACKET_FIELDS
        }
        and all(
            row["census_field"] == "admitted_stage_e_read_touches"
            and row["coefficient"]
            == (
                "S1.tensor_source_with_constraints()[0]"
                f"[{int(row['canonical_slot'])}]"
            )
            for row in role_reduction
        )
    )
    stage_reduction_valid = bool(
        isinstance(stage_reduction, tuple)
        and len(stage_reduction) == 10
        and tuple(int(row["canonical_slot"]) for row in stage_reduction)
        == tuple(range(10))
        and {
            (str(row["variant"]), str(row["stage"]))
            for row in stage_reduction
        }
        == {(variant, stage) for variant in VARIANTS for stage in STAGES}
        and all(
            row["stage_statistic"] == "slot_count"
            and float(row["coefficient"]) == 1.0
            for row in stage_reduction
        )
        and sum("declared_zero_reason" in row for row in stage_reduction) == 1
        and next(
            row for row in stage_reduction
            if "declared_zero_reason" in row
        )["variant"] == "alternate_port"
        and next(
            row for row in stage_reduction
            if "declared_zero_reason" in row
        )["stage"] == "C"
    )
    disposition_checks = (
        tuple(str(row["check"]) for row in disposition)
        if isinstance(disposition, tuple)
        and all(isinstance(row, dict) and "check" in row for row in disposition)
        else ()
    )
    disposition_valid = bool(
        disposition_checks
        == (
            "projector_algebra",
            "orientation_twist",
            "ward_constraint",
            "response_locking",
            "scalar_only_no_overclaim",
            "free_tensor_carrier",
            "no_claim",
        )
        and [
            str(row["check"])
            for row in disposition
            if not bool(row["expected_pass"])
        ]
        == ["ward_constraint"]
    )

    byte_pin_function = function_definition(tree, "byte_pins")
    pin_loop_uses_audit_tuple = any(
        isinstance(node, ast.For)
        and isinstance(node.iter, ast.Name)
        and node.iter.id == "AUDIT_INPUT_PATHS"
        for node in ast.walk(byte_pin_function)
    )
    head_anchor_present = any(
        isinstance(node, ast.Constant)
        and isinstance(node.value, str)
        and node.value == "HEAD:"
        for node in ast.walk(byte_pin_function)
    )
    sha_calls = [
        node
        for node in ast.walk(byte_pin_function)
        if isinstance(node, ast.Call) and call_path(node.func) == "sha256"
    ]
    pinning_convention_valid = bool(
        pin_loop_uses_audit_tuple
        and head_anchor_present
        and len(sha_calls) >= 2
        and primary_audit == EXPECTED_PRIMARY_INPUTS
    )
    landed_sha256_pins: dict[str, str | None] = {}
    landed_pin_details: dict[str, object] = {}
    if isinstance(primary_audit, tuple):
        for relative in primary_audit:
            landed_bytes, detail = git_head_bytes(str(relative))
            landed_sha256_pins[str(relative)] = (
                sha256(landed_bytes).hexdigest()
                if landed_bytes is not None
                else None
            )
            landed_pin_details[str(relative)] = detail

    harness_calls = extracted_harness_calls(tree)
    expected_calls = tuple(
        {"path": row["path"], "marker": row["marker"]}
        for row in HARNESS_EXPECTATIONS
    )
    observed_calls = tuple(
        {"path": row["path"], "marker": row["marker"]}
        for row in harness_calls
    )
    harness_declarations_valid = observed_calls == expected_calls

    blocked_present = sorted(TOP_LEVEL_BLOCKLIST & set(sys.modules))
    passed = bool(
        not literal_errors
        and audit_literals_valid
        and census_schema_valid
        and role_reduction_valid
        and stage_reduction_valid
        and disposition_valid
        and pinning_convention_valid
        and len(landed_sha256_pins) == 5
        and all(landed_sha256_pins.values())
        and harness_declarations_valid
        and not blocked_present
    )
    return {
        "pass": passed,
        "primary_read_as_data_only": True,
        "literal_errors": literal_errors,
        "primary_AUDIT_INPUT_PATHS_literal_tuple": audit_literals_valid,
        "primary_AUDIT_INPUT_PATHS": primary_audit,
        "checker_AUDIT_INPUT_PATHS": own_audit,
        "census_schema_table": census_schema,
        "census_schema_valid": census_schema_valid,
        "role_uniform_reduction": role_reduction,
        "role_uniform_reduction_valid": role_reduction_valid,
        "stage_resolved_reduction": stage_reduction,
        "stage_resolved_reduction_valid": stage_reduction_valid,
        "frozen_stage_resolved_disposition": disposition,
        "frozen_disposition_valid": disposition_valid,
        "landed_sha256_pins": landed_sha256_pins,
        "landed_pin_details": landed_pin_details,
        "primary_HEAD_pinning_convention_valid": pinning_convention_valid,
        "harness_declarations": harness_calls,
        "harness_declarations_valid": harness_declarations_valid,
        "blocked_primary_imports_present": blocked_present,
    }


def stage_resolved_statistics(
    slots: list[object],
    admissions: list[dict[str, object]],
    walk: dict[str, object],
) -> dict[str, object]:
    rows = {
        stage: {
            "slot_count": 0,
            "word_count": 0,
            "register_touch_count": 0,
            "read_touch_count": 0,
            "write_touch_count": 0,
            "retain_after_declaration_count": 0,
            "declared_handoff_count": 0,
            "admitted_packet_word_count": 0,
        }
        for stage in STAGES
    }
    register_state: dict[int, str] = {}
    for slot in slots:
        stage = str(slot.stage)
        if stage not in rows:
            raise ValueError(f"undeclared epoch stage {stage!r}")
        stage_row = rows[stage]
        stage_row["slot_count"] += 1
        for word in slot.words:
            stage_row["word_count"] += 1
            stage_row["retain_after_declaration_count"] += len(
                word.retain_after
            )
            for register, (_role, mode) in word.accesses.items():
                register = int(register)
                stage_row["register_touch_count"] += 1
                if mode == "read":
                    stage_row["read_touch_count"] += 1
                elif mode == "write":
                    stage_row["write_touch_count"] += 1
                else:
                    raise ValueError(
                        f"undeclared register access mode {mode!r}"
                    )
                if register_state.get(register) == "retained":
                    stage_row["declared_handoff_count"] += 1
            for register in word.accesses:
                register = int(register)
                register_state[register] = (
                    "retained" if register in word.retain_after else "clean"
                )
    rows["E"]["admitted_packet_word_count"] = sum(
        int(row["admitted"]) for row in admissions
    )
    totals = {
        statistic: sum(int(rows[stage][statistic]) for stage in STAGES)
        for statistic in rows["A"]
    }
    return {
        "stages": rows,
        "totals": totals,
        "walk_handoffs_declared": int(walk["handoffs_declared"]),
        "walk_register_touches": int(walk["register_touches"]),
        "handoff_total_matches_walk": (
            totals["declared_handoff_count"]
            == int(walk["handoffs_declared"])
        ),
        "register_touch_total_matches_walk": (
            totals["register_touch_count"] == int(walk["register_touches"])
        ),
    }


def canonical_source_in_fresh_process() -> dict[str, object]:
    code = (
        "import json;"
        "import signed_gravity_oriented_tensor_source_lift as S1;"
        "source,_constraint=S1.tensor_source_with_constraints();"
        "print(json.dumps({'source':source.tolist(),'tol':float(S1.TOL)}))"
    )
    env = os.environ.copy()
    scripts_path = str(SCRIPTS)
    env["PYTHONPATH"] = (
        scripts_path
        if not env.get("PYTHONPATH")
        else scripts_path + os.pathsep + env["PYTHONPATH"]
    )
    run = subprocess.run(
        [sys.executable, "-c", code],
        cwd=ROOT,
        env=env,
        capture_output=True,
        text=True,
        errors="replace",
        timeout=AUDIT_TIMEOUT_SEC,
        check=False,
    )
    lines = [line for line in run.stdout.splitlines() if line.strip()]
    payload = json.loads(lines[-1]) if run.returncode == 0 and lines else {}
    return {
        "pass": (
            run.returncode == 0
            and isinstance(payload.get("source"), list)
            and len(payload["source"]) == 10
        ),
        "source": payload.get("source"),
        "tol": payload.get("tol"),
        "returncode": run.returncode,
        "stderr_tail": run.stderr.splitlines()[-6:],
    }


def census_recomputation(schema: dict[str, object]) -> dict[str, object]:
    stage_reduction = schema["stage_resolved_reduction"]
    role_reduction = schema["role_uniform_reduction"]

    atlas = F722.EPOCH.P.build_private_atlases()
    primary = F722.EPOCH.build_epoch(SHAPE, "primary", atlas)
    alternate = F722.EPOCH.build_epoch(
        SHAPE,
        "alternate_port",
        atlas,
        recurrent_override=primary.recurrent,
    )
    bundles = {"primary": primary, "alternate_port": alternate}

    role_counts: dict[str, dict[str, int]] = {}
    retained_witnesses: dict[str, dict[str, bool]] = {}
    stage_statistics: dict[str, object] = {}
    lawful: dict[str, bool] = {}
    admissions_by_variant: dict[str, int] = {}
    for variant in VARIANTS:
        extension = F722.extend_and_walk(bundles[variant])
        feed = F722.feed_unchanged_chain(extension["table"])
        admissions = [
            {
                "tick_identity": int(row["tick_identity"]),
                "stage_e_word": str(row["stage_e_word"]),
                "admitted": status == "admitted",
            }
            for row, status in zip(
                extension["table"], feed["statuses"], strict=True
            )
        ]
        admitted_words = {
            row["stage_e_word"] for row in admissions if row["admitted"]
        }
        counts = {field: 0 for field in PACKET_FIELDS}
        for slot in extension["slots"]:
            for word in slot.words:
                if word.word_id not in admitted_words:
                    continue
                for role, mode in word.accesses.values():
                    if role in counts and mode == "read":
                        counts[str(role)] += 1
        role_counts[variant] = counts
        retained_witnesses[variant] = {
            str(source["field"]): bool(source["retained_witness"]["valid"])
            for source in extension["sources"]
        }
        stage_statistics[variant] = stage_resolved_statistics(
            extension["slots"], admissions, extension["walk"]
        )
        lawful[variant] = bool(extension["lawful"] and feed["pass"])
        admissions_by_variant[variant] = len(admitted_words)

    stage_vector = [0.0] * 10
    stage_reduction_rows = []
    for row in stage_reduction:
        slot = int(row["canonical_slot"])
        variant = str(row["variant"])
        stage = str(row["stage"])
        statistic = str(row["stage_statistic"])
        count = int(
            stage_statistics[variant]["stages"][stage][statistic]
        )
        contribution = float(row["coefficient"]) * count
        stage_vector[slot] = contribution
        stage_reduction_rows.append({
            **row,
            "observed_integer_count": count,
            "real_contribution": contribution,
        })

    canonical = canonical_source_in_fresh_process()
    canonical_source = canonical.get("source") or []
    role_uniform_vector = [0.0] * 10
    role_reduction_rows = []
    if canonical["pass"]:
        for row in role_reduction:
            slot = int(row["canonical_slot"])
            variant = str(row["variant"])
            role = str(row["packet_role"])
            count = int(role_counts[variant][role])
            coefficient = float(canonical_source[slot])
            contribution = count * coefficient
            role_uniform_vector[slot] = contribution
            role_reduction_rows.append({
                **row,
                "observed_integer_count": count,
                "canonical_fixture_coefficient": coefficient,
                "real_contribution": contribution,
            })

    ratios = [
        stage / uniform
        for stage, uniform in zip(
            stage_vector, role_uniform_vector, strict=True
        )
        if abs(uniform) > 1.0e-12
    ]
    ratio_min = min(ratios) if ratios else None
    ratio_max = max(ratios) if ratios else None
    ratio_spread = (
        float(ratio_max - ratio_min)
        if ratio_min is not None and ratio_max is not None
        else None
    )
    stage_rows = [
        {
            "variant": variant,
            "stage": stage,
            **stage_statistics[variant]["stages"][stage],
        }
        for variant in VARIANTS
        for stage in STAGES
    ]
    stage_nonuniform = all(
        len({int(row[statistic]) for row in stage_rows}) > 1
        for statistic in (
            "slot_count",
            "declared_handoff_count",
            "register_touch_count",
        )
    )
    all_role_counts_24 = all(
        role_counts[variant][role] == 24
        for variant in VARIANTS
        for role in PACKET_FIELDS
    )
    stage_accounting_exact = all(
        stage_statistics[variant]["handoff_total_matches_walk"]
        and stage_statistics[variant]["register_touch_total_matches_walk"]
        for variant in VARIANTS
    )
    passed = bool(
        schema["pass"]
        and all(lawful.values())
        and admissions_by_variant == {
            "primary": 24,
            "alternate_port": 24,
        }
        and all_role_counts_24
        and all(
            retained_witnesses[variant].get(role, False)
            for variant in VARIANTS
            for role in PACKET_FIELDS
        )
        and stage_accounting_exact
        and stage_nonuniform
        and tuple(int(value) for value in stage_vector)
        == EXPECTED_STAGE_VECTOR
        and canonical["pass"]
        and len(ratios) == 10
        and ratio_spread is not None
        and ratio_spread > 1.0e3
    )
    return {
        "pass": passed,
        "shape": SHAPE,
        "builds_per_variant": 1,
        "lawful": lawful,
        "admissions_by_variant": admissions_by_variant,
        "role_counts": role_counts,
        "all_role_counts_equal_24": all_role_counts_24,
        "retained_witnesses": retained_witnesses,
        "stage_resolved_statistics": stage_statistics,
        "stage_statistics_nonuniform": stage_nonuniform,
        "stage_accounting_exact": stage_accounting_exact,
        "stage_resolved_vector": stage_vector,
        "expected_stage_resolved_vector": EXPECTED_STAGE_VECTOR,
        "stage_reduction_rows": stage_reduction_rows,
        "canonical_source_fresh_process": canonical,
        "role_uniform_reduced_vector": role_uniform_vector,
        "role_reduction_rows": role_reduction_rows,
        "stage_to_role_uniform_slot_ratios": ratios,
        "ratio_min": ratio_min,
        "ratio_max": ratio_max,
        "ratio_spread": ratio_spread,
        "required_ratio_spread_strictly_above": 1.0e3,
        "numerically_nonproportional": bool(
            ratio_spread is not None and ratio_spread > 1.0e3
        ),
        "blocked_primary_imports_present": sorted(
            TOP_LEVEL_BLOCKLIST & set(sys.modules)
        ),
    }


def sha_pin_certificate(schema: dict[str, object]) -> dict[str, object]:
    expected_pins = schema["landed_sha256_pins"]
    rows: dict[str, object] = {}
    for relative in EXPECTED_PRIMARY_INPUTS:
        observed = sha256((ROOT / relative).read_bytes()).hexdigest()
        expected = expected_pins.get(relative)
        rows[relative] = {
            "observed_sha256": observed,
            "primary_landed_HEAD_sha256": expected,
            "pass": observed == expected,
        }
    return {
        "pass": (
            schema["primary_HEAD_pinning_convention_valid"]
            and set(expected_pins) == set(EXPECTED_PRIMARY_INPUTS)
            and all(bool(row["pass"]) for row in rows.values())
        ),
        "pins": rows,
        "matched_pin_count": sum(
            bool(row["pass"]) for row in rows.values()
        ),
        "expected_pin_count": 5,
    }


def subprocess_text(value: str | bytes | None) -> str:
    if value is None:
        return ""
    if isinstance(value, bytes):
        return value.decode("utf-8", errors="replace")
    return value


def run_landed_harness(expectation: dict[str, object]) -> dict[str, object]:
    env = os.environ.copy()
    scripts_path = str(SCRIPTS)
    env["PYTHONPATH"] = (
        scripts_path
        if not env.get("PYTHONPATH")
        else scripts_path + os.pathsep + env["PYTHONPATH"]
    )
    started = perf_counter()
    try:
        run = subprocess.run(
            [sys.executable, str(ROOT / str(expectation["path"]))],
            cwd=ROOT,
            env=env,
            capture_output=True,
            text=True,
            errors="replace",
            timeout=AUDIT_TIMEOUT_SEC,
            check=False,
        )
        stdout = run.stdout
        stderr = run.stderr
        returncode = run.returncode
        timed_out = False
    except subprocess.TimeoutExpired as exc:
        stdout = subprocess_text(exc.stdout)
        stderr = subprocess_text(exc.stderr)
        returncode = None
        timed_out = True
    lines = stdout.splitlines()
    pass_lines = [
        line
        for line in lines
        if line.startswith("PASS ") or line.startswith("[PASS]")
    ]
    fail_lines = [
        line
        for line in lines
        if line.startswith("FAIL ") or line.startswith("[FAIL]")
    ]
    marker = expectation["marker"]
    marker_found = marker is None or str(marker) in stdout
    passed = bool(
        returncode == 0
        and not timed_out
        and len(pass_lines) == int(expectation["pass_line_count"])
        and not fail_lines
        and marker_found
    )
    return {
        "pass": passed,
        "path": expectation["path"],
        "execution": "fresh subprocess of the landed main with no arguments",
        "returncode": returncode,
        "timed_out": timed_out,
        "expected_pass_line_count": expectation["pass_line_count"],
        "observed_pass_line_count": len(pass_lines),
        "observed_fail_line_count": len(fail_lines),
        "fail_lines": fail_lines,
        "required_marker": marker,
        "required_marker_found": marker_found,
        "summary_lines": [
            line
            for line in lines
            if "SUMMARY" in line or "RESULT " in line or "FINAL_TAG:" in line
        ],
        "stdout_sha256": sha256(stdout.encode()).hexdigest(),
        "stderr_tail": stderr.splitlines()[-8:],
        "runtime_seconds": perf_counter() - started,
    }


def harness_rerun_certificate(
    schema: dict[str, object],
) -> dict[str, object]:
    rows = [
        run_landed_harness(expectation)
        for expectation in HARNESS_EXPECTATIONS
    ]
    return {
        "pass": bool(
            schema["harness_declarations_valid"]
            and all(row["pass"] for row in rows)
        ),
        "expected_pass_counts": [7, 20, 5],
        "observed_pass_counts": [
            row["observed_pass_line_count"] for row in rows
        ],
        "observed_fail_counts": [
            row["observed_fail_line_count"] for row in rows
        ],
        "harnesses": rows,
        "runtime_seconds": sum(
            float(row["runtime_seconds"]) for row in rows
        ),
    }


def zero_refit_declarations(tree: ast.Module) -> list[dict[str, object]]:
    rows = []
    required_keys = {
        "optimizer_calls",
        "fitted_parameters",
        "normalization_applied",
    }
    for node in ast.walk(tree):
        if not isinstance(node, ast.Dict):
            continue
        items: dict[str, object] = {}
        for key_node, value_node in zip(node.keys, node.values, strict=True):
            if (
                isinstance(key_node, ast.Constant)
                and isinstance(key_node.value, str)
                and key_node.value in required_keys
            ):
                try:
                    items[key_node.value] = ast.literal_eval(value_node)
                except (ValueError, TypeError, SyntaxError):
                    items[key_node.value] = "<nonliteral>"
        if set(items) == required_keys:
            rows.append({"line": node.lineno, **items})
    return rows


def primary_source_discipline() -> dict[str, object]:
    _source, tree = source_tree()
    imported_s_aliases = {
        alias.asname
        for node in tree.body
        if isinstance(node, ast.Import)
        for alias in node.names
        if alias.asname is not None and alias.asname.startswith("S")
    }
    attribute_injections = []
    for node in ast.walk(tree):
        targets: tuple[ast.AST, ...] = ()
        if isinstance(node, ast.Assign):
            targets = tuple(
                target
                for raw in node.targets
                for target in assignment_targets(raw)
            )
        elif isinstance(node, (ast.AnnAssign, ast.AugAssign)):
            targets = assignment_targets(node.target)
        elif isinstance(node, ast.Delete):
            targets = tuple(
                target
                for raw in node.targets
                for target in assignment_targets(raw)
            )
        for target in targets:
            if attribute_root(target) in imported_s_aliases:
                attribute_injections.append({
                    "line": target.lineno,
                    "target": ast.unparse(target),
                })
        if (
            isinstance(node, ast.Call)
            and call_path(node.func) in {"setattr", "delattr"}
            and node.args
            and attribute_root(node.args[0]) in imported_s_aliases
        ):
            attribute_injections.append({
                "line": node.lineno,
                "target": ast.unparse(node),
            })

    optimizer_leaf_names = {
        "fit",
        "minimize",
        "least_squares",
        "curve_fit",
        "polyfit",
        "differential_evolution",
        "basinhopping",
        "optimizer",
        "optimize",
    }
    optimizer_calls = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        name = call_path(node.func)
        pieces = tuple((name or "").lower().split("."))
        if any(
            piece in optimizer_leaf_names or piece in {"optim", "optimizers"}
            for piece in pieces
        ):
            optimizer_calls.append({
                "line": node.lineno,
                "call": ast.unparse(node.func),
            })

    allowed_reduction_calls = {
        "np.zeros",
        "tuple",
        "range",
        "zip",
        "str",
        "int",
        "float",
        "rows.append",
    }
    reduction_details: dict[str, object] = {}
    reductions_pure_arithmetic = True
    for function_name in (
        "reduce_census_to_tensor",
        "reduce_stage_resolved_census",
    ):
        function = function_definition(tree, function_name)
        calls = sorted({
            call_path(node.func) or ast.unparse(node.func)
            for node in ast.walk(function)
            if isinstance(node, ast.Call)
        })
        arithmetic_ops = sorted({
            type(node.op).__name__
            for node in ast.walk(function)
            if isinstance(node, (ast.BinOp, ast.AugAssign))
        })
        forbidden_ops = [
            {
                "line": node.lineno,
                "operator": type(node.op).__name__,
            }
            for node in ast.walk(function)
            if (
                isinstance(node, ast.BinOp)
                and isinstance(
                    node.op,
                    (ast.Div, ast.FloorDiv, ast.Pow, ast.MatMult),
                )
            )
        ]
        unexpected_calls = sorted(
            call for call in calls if call not in allowed_reduction_calls
        )
        pure = not unexpected_calls and not forbidden_ops
        reductions_pure_arithmetic = reductions_pure_arithmetic and pure
        reduction_details[function_name] = {
            "line": function.lineno,
            "calls": calls,
            "arithmetic_operators": arithmetic_ops,
            "unexpected_calls": unexpected_calls,
            "division_power_or_matrix_operations": forbidden_ops,
            "pure_declared_arithmetic": pure,
        }

    zero_refit_rows = zero_refit_declarations(tree)
    zero_refit_valid = bool(
        len(zero_refit_rows) >= 2
        and all(
            row["optimizer_calls"] == 0
            and row["fitted_parameters"] == 0
            and row["normalization_applied"] is False
            for row in zero_refit_rows
        )
    )

    disposition, disposition_error, _node = literal_assignment(
        tree, "S1_STAGE_RESOLVED_FROZEN_DISPOSITION"
    )
    ward_rows = (
        [
            row
            for row in disposition
            if isinstance(row, dict) and row.get("check") == "ward_constraint"
        ]
        if isinstance(disposition, tuple)
        else []
    )
    ward = ward_rows[0] if len(ward_rows) == 1 else {}
    ward_value_text = str(ward.get("expected_values", ""))
    ward_number_strings = tuple(re.findall(r"'([^']+)'", ward_value_text))
    try:
        ward_numbers = tuple(float(value) for value in ward_number_strings)
    except ValueError:
        ward_numbers = ()
    frozen_ward_valid = bool(
        disposition_error is None
        and len(ward_rows) == 1
        and ward.get("expected_pass") is False
        and ward_value_text == EXPECTED_WARD_VALUES
        and ward_number_strings == ("1.9e+04", "1.9e+04", "0.0e+00")
        and ward_numbers == (19000.0, 19000.0, 0.0)
    )
    blocked_present = sorted(TOP_LEVEL_BLOCKLIST & set(sys.modules))
    passed = bool(
        imported_s_aliases == {"S1", "S2"}
        and not attribute_injections
        and not optimizer_calls
        and reductions_pure_arithmetic
        and zero_refit_valid
        and frozen_ward_valid
        and not blocked_present
    )
    return {
        "pass": passed,
        "primary_read_as_data_only": True,
        "imported_S_module_aliases": sorted(imported_s_aliases),
        "attribute_assignments_onto_imported_S_modules": attribute_injections,
        "optimizer_calls": optimizer_calls,
        "reduction_functions": reduction_details,
        "reductions_are_pure_arithmetic": reductions_pure_arithmetic,
        "zero_refit_declarations": zero_refit_rows,
        "zero_refit_declarations_valid": zero_refit_valid,
        "frozen_Ward_failure": {
            "expected_pass": ward.get("expected_pass"),
            "exact_expected_values": ward_value_text,
            "exact_number_strings": ward_number_strings,
            "numeric_values": ward_numbers,
            "contains_two_1p9e4_scale_residuals": frozen_ward_valid,
        },
        "blocked_primary_imports_present": blocked_present,
    }


def check(label: str, condition: bool, detail: object = "") -> None:
    passed = bool(condition)
    CHECKS.append({"label": label, "pass": passed, "detail": detail})
    print("PASS" if passed else "FAIL", label)


def run_certificate(
    label: str,
    function: Callable[[], dict[str, object]],
) -> dict[str, object]:
    try:
        result = function()
    except Exception as exc:
        result = {
            "pass": False,
            "error": f"{type(exc).__name__}: {exc}",
        }
    check(label, bool(result.get("pass")), result)
    return result


def main() -> int:
    started = perf_counter()
    CHECKS.clear()
    schema = run_certificate("schema_extraction", schema_extraction)
    census = run_certificate(
        "census_recomputation",
        lambda: census_recomputation(schema),
    )
    pins = run_certificate(
        "sha_pin_certificate",
        lambda: sha_pin_certificate(schema),
    )
    harnesses = run_certificate(
        "harness_rerun_certificate",
        lambda: harness_rerun_certificate(schema),
    )
    discipline = run_certificate(
        "primary_source_discipline",
        primary_source_discipline,
    )

    blocked_present = sorted(TOP_LEVEL_BLOCKLIST & set(sys.modules))
    passing = all(row["pass"] for row in CHECKS) and not blocked_present
    report = {
        "status": "PASS" if passing else "FAIL",
        "authority": "none",
        "audit": "unset",
        "audit_timeout_seconds": AUDIT_TIMEOUT_SEC,
        "audit_input_paths": AUDIT_INPUT_PATHS,
        "top_level_blocklist": sorted(TOP_LEVEL_BLOCKLIST),
        "blocked_primary_imports_present": blocked_present,
        "checks": CHECKS,
        "check_summary": {
            "passing": sum(row["pass"] for row in CHECKS),
            "total": len(CHECKS),
        },
        "certificates": {
            "schema_extraction": schema,
            "census_recomputation": census,
            "sha_pin_certificate": pins,
            "harness_rerun_certificate": harnesses,
            "primary_source_discipline": discipline,
        },
        "runtime_seconds": perf_counter() - started,
    }
    report["report_sha256"] = sha256(json.dumps(
        report,
        sort_keys=True,
        separators=(",", ":"),
    ).encode()).hexdigest()
    print(json.dumps(report, indent=2, sort_keys=True))
    print(
        "CYCLE725_CSLT_INDEPENDENT_CHECK_PASS"
        if passing
        else "CYCLE725_CSLT_INDEPENDENT_CHECK_FAIL"
    )
    return 0 if passing else 1


if __name__ == "__main__":
    raise SystemExit(main())
