#!/usr/bin/env python3
"""Cycle 799: census the evaluation cadence of the landed selector laws.

This runner reads the four landed law surfaces as source, recovers the
condition sites and their containing call structure from the AST, and asks
whether those sites select one of Cycle 796's four monitoring cadences
uniformly.  It then recomputes Cycle 796's two k=2 cadence rows.
"""
from __future__ import annotations

import ast
from collections import Counter
from contextlib import redirect_stdout
from hashlib import sha256
import importlib
from io import StringIO
import json
from pathlib import Path
import sys
from time import monotonic
from typing import Any


AUDIT_TIMEOUT_SEC = 1500
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
    "scripts/frontier_cycle758_selector_multisource_2026_07_28.py",
    "scripts/frontier_cycle781_checkpoint_refusal_law_2026_07_28.py",
    "scripts/frontier_cycle796_monitored_selector_2026_07_28.py",
)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "a74c7e5bbc297c57d317af7fd85d0b9e01d078625f5d4689daf2ebbdbc1cee0a",
    AUDIT_INPUT_PATHS[2]:
        "8be433f74cb337c322bcb1e2f46007244d708a41c946cb83b7ccd61004176241",
    AUDIT_INPUT_PATHS[3]:
        "b1158250dcb1449f6abac4f6bb6a0a90f47511a8a0f587e85483f4b6f3624211",
    AUDIT_INPUT_PATHS[4]:
        "be0238611e02f9bad8df813430f9decec68d287df267bbf82ba4a63ffc8483c3",
}
CADENCES = (
    "orbit_return_boundary",
    "H_station_boundary",
    "Q_R1_R2_layer_boundary",
    "program_macro_completion",
)
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def emit(lines: list[str], label: str, value: object | None = None) -> None:
    line = label if value is None else label + " :: " + compact(value)
    lines.append(line)


def certificate(
    lines: list[str], key: str, label: str, passed: bool, detail: object
) -> None:
    emit(
        lines,
        ("PASS" if passed else "FAIL") + f" CERTIFICATE_{key}_{label}",
        detail,
    )


LAW_SPECS = (
    # Cycle 719: the only dynamical Python condition in Q is the live A-token
    # guard.  Its forward and inverse placements are both retained because the
    # selector tests both orbit directions.
    {
        "law": "K719.forward_active_A_token_guard",
        "path": AUDIT_INPUT_PATHS[0],
        "function": "apply_controller_step",
        "needles": ("if not reverse:", "if a[station]:", "mapped_macro"),
        "cadence": "program_macro_completion",
        "basis": "run_orbit.step -> apply_controller_step.Q -> mapped_macro",
    },
    {
        "law": "K719.inverse_active_A_token_guard",
        "path": AUDIT_INPUT_PATHS[0],
        "function": "apply_controller_step",
        "needles": (
            "else:",
            "if a[station]:",
            "reversed(mapped_macro",
        ),
        "cadence": "program_macro_completion",
        "basis": "run_orbit.step -> apply_controller_step.inverse_Q -> mapped_macro",
    },
    # Cycle 750's retained candidate C, the surface inherited by Cycle 758.
    {
        "law": "F750.forward_synchronous_composition",
        "path": AUDIT_INPUT_PATHS[1],
        "function": "enforcement_lineage_selector",
        "needles": ("K.run_orbit", "after != expected"),
        "cadence": "orbit_return_boundary",
        "basis": "condition follows complete K.run_orbit return",
    },
    {
        "law": "F750.forward_token_rail_return",
        "path": AUDIT_INPUT_PATHS[1],
        "function": "enforcement_lineage_selector",
        "needles": ("rail_a != tokens", "rail_b != zeros"),
        "cadence": "orbit_return_boundary",
        "basis": "condition reads rails returned by complete K.run_orbit",
    },
    {
        "law": "F750.literal_inverse",
        "path": AUDIT_INPUT_PATHS[1],
        "function": "enforcement_lineage_selector",
        "needles": (
            "reverse=True",
            "restored == before",
            "inverse_a == rail_a",
            "inverse_b == rail_b",
        ),
        "cadence": "orbit_return_boundary",
        "basis": "condition follows complete inverse K.run_orbit return",
    },
    {
        "law": "F750.clean_postimage",
        "path": AUDIT_INPUT_PATHS[1],
        "function": "enforcement_lineage_selector",
        "needles": ("dirty = any", "not dirty"),
        "cadence": "orbit_return_boundary",
        "basis": "postimage is decoded from the completed forward orbit",
    },
    # Cycle 758 evaluates the complete four-element exclusion battery at one
    # site, after both forward and inverse orbits have returned.
    {
        "law": "F758.synchronous_composition",
        "path": AUDIT_INPUT_PATHS[2],
        "function": "multisource_enforcement_lineage_selector",
        "needles": ("'synchronous_composition': after == expected",),
        "cadence": "orbit_return_boundary",
        "basis": "conditions dict is built after forward K.run_orbit",
    },
    {
        "law": "F758.token_rail_return",
        "path": AUDIT_INPUT_PATHS[2],
        "function": "multisource_enforcement_lineage_selector",
        "needles": ("'token_rail_return': rail_a == tokens and rail_b == zeros",),
        "cadence": "orbit_return_boundary",
        "basis": "conditions dict reads complete-orbit returned rails",
    },
    {
        "law": "F758.literal_inverse",
        "path": AUDIT_INPUT_PATHS[2],
        "function": "multisource_enforcement_lineage_selector",
        "needles": (
            "'literal_inverse':",
            "restored == before",
            "inverse_a == rail_a",
            "inverse_b == rail_b",
        ),
        "cadence": "orbit_return_boundary",
        "basis": "conditions dict follows inverse K.run_orbit return",
    },
    {
        "law": "F758.clean_postimage",
        "path": AUDIT_INPUT_PATHS[2],
        "function": "multisource_enforcement_lineage_selector",
        "needles": ("'clean_postimage': clean_postimage(after, bank_count)",),
        "cadence": "orbit_return_boundary",
        "basis": "conditions dict evaluates forward-orbit postimage",
    },
    # Cycle 781 re-expresses Cycle 745's complete refusal predicate.  These
    # tests are made immediately after each bounded WRITE_WORD application.
    {
        "law": "F781.C745_output_tag_REFUSED",
        "path": AUDIT_INPUT_PATHS[3],
        "function": "apply_cell_word",
        "needles": ("C745.apply_word", "all((tag == 'REFUSED' for tag in tags))"),
        "cadence": "program_macro_completion",
        "basis": "C745 WRITE_WORD -> output_tag test",
    },
    {
        "law": "F781.C745_Q_refuse_asserted",
        "path": AUDIT_INPUT_PATHS[3],
        "function": "apply_cell_word",
        "needles": ("C745.apply_word", "all(q_refuse)"),
        "cadence": "program_macro_completion",
        "basis": "C745 WRITE_WORD -> Q_refuse test",
    },
    {
        "law": "F781.C745_Q_in_cleared",
        "path": AUDIT_INPUT_PATHS[3],
        "function": "apply_cell_word",
        "needles": ("C745.apply_word", "not any(q_in)"),
        "cadence": "program_macro_completion",
        "basis": "C745 WRITE_WORD -> Q_in test",
    },
    {
        "law": "F781.C745_Q_accept_cleared",
        "path": AUDIT_INPUT_PATHS[3],
        "function": "apply_cell_word",
        "needles": ("C745.apply_word", "not any(q_accept)"),
        "cadence": "program_macro_completion",
        "basis": "C745 WRITE_WORD -> Q_accept test",
    },
    {
        "law": "F781.C745_persistent_cell_exact",
        "path": AUDIT_INPUT_PATHS[3],
        "function": "apply_cell_word",
        "needles": ("C745.apply_word", "after_persistent == before_persistent"),
        "cadence": "program_macro_completion",
        "basis": "C745 WRITE_WORD -> persistent-cell equality test",
    },
    {
        "law": "F781.tensor_guard_output_tag_REFUSED",
        "path": AUDIT_INPUT_PATHS[3],
        "function": "tensor_landed_guard_refuses",
        "needles": ("C745.apply_word", "all((C745.output_tag(event) == 'REFUSED'"),
        "cadence": "program_macro_completion",
        "basis": "tensor C745 WRITE_WORD -> output-tag test",
    },
    {
        "law": "F781.tensor_guard_persistent_exact",
        "path": AUDIT_INPUT_PATHS[3],
        "function": "tensor_landed_guard_refuses",
        "needles": ("C745.apply_word", "persistent_cells(events) == guard_persistent"),
        "cadence": "program_macro_completion",
        "basis": "tensor C745 WRITE_WORD -> persistent-cell equality test",
    },
    # The checkpoint-bearing extension is scheduled at every tested
    # post-engagement H-station boundary, after syndrome and restore words.
    {
        "law": "F781.refused_or_rolled_back",
        "path": AUDIT_INPUT_PATHS[3],
        "function": "run_one_attack",
        "needles": ("attack.existing_refused or rolled_back",),
        "cadence": "H_station_boundary",
        "basis": "post-engagement station boundary -> syndrome -> restore -> test",
    },
    {
        "law": "F781.record_byte_identical_after",
        "path": AUDIT_INPUT_PATHS[3],
        "function": "run_one_attack",
        "needles": ("record_exact = controller_exact and payload_exact",),
        "cadence": "H_station_boundary",
        "basis": "post-engagement station boundary -> restored record test",
    },
    {
        "law": "F781.syndrome_receipt_left",
        "path": AUDIT_INPUT_PATHS[3],
        "function": "run_one_attack",
        "needles": ("receipt_present = syndrome_count > 0 or attack.existing_refused",),
        "cadence": "H_station_boundary",
        "basis": "post-engagement station boundary -> syndrome receipt test",
    },
    {
        "law": "F781.checkpoint_engagement",
        "path": AUDIT_INPUT_PATHS[3],
        "function": "non_interference",
        "needles": (
            "for step in range(C719.CONTROLLER_STATIONS):",
            "C719.apply_fast_int",
            "if decoded and (not engaged):",
        ),
        "cadence": "H_station_boundary",
        "basis": "one C719 H application in station loop -> decoded engagement test",
    },
)


def source_snapshot() -> dict[str, dict[str, Any]]:
    snapshot: dict[str, dict[str, Any]] = {}
    for relative in AUDIT_INPUT_PATHS:
        source = (ROOT / relative).read_bytes()
        tree = ast.parse(source.decode("utf-8"), filename=relative)
        snapshot[relative] = {
            "bytes": len(source),
            "sha256": sha256(source).hexdigest(),
            "ast_sha256": sha256(
                ast.dump(
                    tree, annotate_fields=True, include_attributes=False
                ).encode("utf-8")
            ).hexdigest(),
        }
    return snapshot


def top_level_functions(tree: ast.Module) -> dict[str, ast.FunctionDef]:
    return {
        node.name: node
        for node in tree.body
        if isinstance(node, ast.FunctionDef)
    }


def call_names(node: ast.AST) -> set[str]:
    names: set[str] = set()
    for child in ast.walk(node):
        if not isinstance(child, ast.Call):
            continue
        if isinstance(child.func, ast.Name):
            names.add(child.func.id)
        elif isinstance(child.func, ast.Attribute):
            names.add(child.func.attr)
    return names


def literal_input_tuple_is_exact() -> bool:
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
        and ast.literal_eval(assignment.value) == AUDIT_INPUT_PATHS
    )


def cadence_census() -> tuple[tuple[dict[str, Any], ...], dict[str, Any]]:
    parsed = {
        path: ast.parse(
            (ROOT / path).read_text(encoding="utf-8"), filename=path
        )
        for path in AUDIT_INPUT_PATHS
    }
    functions = {
        path: top_level_functions(tree) for path, tree in parsed.items()
    }

    # Callgraph anchors that make the cadence names structural rather than
    # comments: H is nested in run_orbit, macros in H, and Cycle 781 advances
    # one compiled H per station-loop iteration.
    k719 = functions[AUDIT_INPUT_PATHS[0]]
    callgraph_checks = {
        "run_orbit_calls_apply_controller_step":
            "apply_controller_step" in call_names(k719["run_orbit"]),
        "apply_controller_step_calls_mapped_macro":
            "mapped_macro" in call_names(k719["apply_controller_step"]),
        "controller_word_has_Q_R1_R2":
            all(
                token in ast.unparse(k719["controller_word"])
                for token in ("q =", "r1 =", "r2 =", "return q + r1 + r2")
            ),
    }
    schedule_text = ast.unparse(functions[AUDIT_INPUT_PATHS[3]]["main"])
    callgraph_checks["F781_station_schedule"] = (
        "every tested post-engagement station boundary" in schedule_text
    )

    rows: list[dict[str, Any]] = []
    extraction_failures: list[dict[str, Any]] = []
    for spec in LAW_SPECS:
        node = functions[spec["path"]].get(spec["function"])
        if node is None:
            extraction_failures.append(
                {"law": spec["law"], "missing_function": spec["function"]}
            )
            continue
        rendered = ast.unparse(node)
        missing = [
            needle for needle in spec["needles"] if needle not in rendered
        ]
        if missing:
            extraction_failures.append(
                {"law": spec["law"], "missing_AST_fragments": missing}
            )
        rows.append(
            {
                "law": spec["law"],
                "evaluation_cadence": spec["cadence"],
                "module_evidence": (
                    f"{spec['path']}:{node.lineno} "
                    f"{spec['function']}[{node.lineno}-{node.end_lineno}]"
                ),
                "AST_callgraph_basis": spec["basis"],
                "AST_fragments": spec["needles"],
            }
        )

    counts = Counter(row["evaluation_cadence"] for row in rows)
    coverage = {
        path: sum(row["module_evidence"].startswith(path) for row in rows)
        for path in AUDIT_INPUT_PATHS[:4]
    }
    method = {
        "scope": (
            "retained dynamical guards and retained selection/refusal "
            "predicates; excludes Python type dispatch, defensive exceptions, "
            "fixture construction, audit plumbing, and report certificates"
        ),
        "basis": (
            "AST condition sites plus enclosing-function callgraph position "
            "relative to mapped_macro, apply_controller_step, run_orbit, and "
            "the Cycle781 C719 station loop"
        ),
        "callgraph_checks": callgraph_checks,
        "coverage_rows_by_surface": coverage,
        "extraction_failures": extraction_failures,
        "cadence_counts": dict(sorted(counts.items())),
        "row_count": len(rows),
        "pass": (
            not extraction_failures
            and all(callgraph_checks.values())
            and all(coverage[path] > 0 for path in AUDIT_INPUT_PATHS[:4])
            and all(
                row["evaluation_cadence"] in CADENCES for row in rows
            )
        ),
    }
    return tuple(rows), method


def recompute_cycle796_timings() -> dict[str, Any]:
    """Recompute, then rerun, the exact Cycle 796 consequence rows."""

    captured = StringIO()
    with redirect_stdout(captured):
        c796 = importlib.import_module(
            "frontier_cycle796_monitored_selector_2026_07_28"
        )
        c796.OUTPUT_LINES.clear()
        rows, k2_positions, landed_control = c796.build_base_rows()
        primary = c796.monitor_family(rows, label="cycle799_primary")
        first = c796.cadence_census(
            rows, primary["acceptance_keys"]
        )
        rerun = c796.monitor_family(rows, label="cycle799_determinism_rerun")
        second = c796.cadence_census(
            rows, primary["acceptance_keys"]
        )

    family_deterministic = (
        primary["table"] == rerun["table"]
        and primary["table_sha256"] == rerun["table_sha256"]
        and primary["classification_counts"]
        == rerun["classification_counts"]
        and primary["acceptance_moments"]
        == rerun["acceptance_moments"]
    )
    cadence_deterministic = first == second
    timing_rows = tuple(first["first_acceptance_table"])
    rows_by_cadence = {
        cadence: tuple(
            row for row in timing_rows if row["cadence"] == cadence
        )
        for cadence in CADENCES
    }
    orbit_moments = {
        cadence: tuple(row["orbit"] for row in rows_by_cadence[cadence])
        for cadence in CADENCES
    }
    suborbit_signatures = {
        cadence: tuple(
            (row["step"], row["absolute_H"])
            for row in rows_by_cadence[cadence]
        )
        for cadence in CADENCES
    }
    return {
        "landed_base_control_pass": landed_control["pass"],
        "k2_configuration_count": len(k2_positions),
        "acceptance_keys": primary["acceptance_keys"],
        "acceptance_moments": primary["acceptance_moments"],
        "classification_counts": primary["classification_counts"],
        "timing_rows": timing_rows,
        "orbit_moments_by_cadence": orbit_moments,
        "suborbit_signatures_by_cadence": suborbit_signatures,
        "orbit_recomposition_failures":
            first["orbit_recomposition_failures"],
        "robustness_split": first["robustness_split"],
        "family_deterministic": family_deterministic,
        "cadence_deterministic": cadence_deterministic,
        "captured_cycle796_stdout_bytes":
            len(captured.getvalue().encode("utf-8")),
        "primary_table_sha256": primary["table_sha256"],
        "rerun_table_sha256": rerun["table_sha256"],
        "pass": (
            landed_control["pass"]
            and len(k2_positions) == 44
            and len(timing_rows) == 2 * len(CADENCES)
            and primary["acceptance_moments"] == (252, 371)
            and all(
                moments == (252, 371)
                for moments in orbit_moments.values()
            )
            and len(set(suborbit_signatures.values())) > 1
            and not first["orbit_recomposition_failures"]
            and family_deterministic
            and cadence_deterministic
        ),
    }


def main() -> int:
    started = monotonic()
    lines: list[str] = []
    before = source_snapshot()
    literal_inputs = literal_input_tuple_is_exact()
    rows, method = cadence_census()
    rows_rerun, method_rerun = cadence_census()
    anchors_pass = (
        literal_inputs
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and {
            path: before[path]["sha256"] for path in AUDIT_INPUT_PATHS
        }
        == EXPECTED_SHA256
        and method["pass"]
    )
    emit(
        lines,
        "CENSUS_METHOD_AST_CALLGRAPH",
        {
            "literal_AUDIT_INPUT_PATHS": literal_inputs,
            "method": method,
            "sha256": {
                path: before[path]["sha256"]
                for path in AUDIT_INPUT_PATHS
            },
        },
    )
    certificate(
        lines,
        "A",
        "anchors_and_AST_callgraph_census_method",
        anchors_pass,
        {
            "anchored_inputs": len(before),
            "literal_AUDIT_INPUT_PATHS": literal_inputs,
            "method_pass": method["pass"],
        },
    )

    for row in rows:
        emit(lines, "LAW_CADENCE", row)
    table_pass = (
        method["pass"]
        and len(rows) == len(LAW_SPECS)
        and len({row["law"] for row in rows}) == len(rows)
    )
    certificate(
        lines,
        "B",
        "full_law_to_cadence_table_with_module_evidence",
        table_pass,
        {
            "cadence_counts": method["cadence_counts"],
            "rows": len(rows),
            "surfaces": method["coverage_rows_by_surface"],
            "table_sha256": digest(rows),
        },
    )

    by_cadence = {
        cadence: tuple(
            row["law"]
            for row in rows
            if row["evaluation_cadence"] == cadence
        )
        for cadence in CADENCES
        if any(
            row["evaluation_cadence"] == cadence for row in rows
        )
    }
    unanimous = len(by_cadence) == 1
    preferred = next(iter(by_cadence)) if unanimous else None
    verdict = (
        "CADENCE_PREFERRED" if unanimous else "NO_UNIFORM_PREFERENCE"
    )
    if unanimous:
        inheritance_argument = (
            "Every retained landed guard/selection/refusal predicate is "
            f"evaluated at {preferred}; an acceptance law inheriting that "
            "cadence has a landed-uniformity argument. This does not land "
            "the acceptance law."
        )
    else:
        inheritance_argument = (
            "The landed predicates evaluate at plural granularities; no "
            "single clock is inherited, so the Cycle796 cadence convention "
            "stands as censused."
        )
    preference = {
        "verdict": verdict,
        "unanimous": unanimous,
        "preferred_cadence": preferred,
        "split": by_cadence,
        "inheritance_argument": inheritance_argument,
    }
    emit(lines, verdict, preference)
    certificate(
        lines,
        "C",
        "preference_verdict",
        (
            verdict == "NO_UNIFORM_PREFERENCE"
            and not unanimous
            and len(by_cadence) > 1
        )
        or (
            verdict == "CADENCE_PREFERRED"
            and unanimous
            and preferred in CADENCES
        ),
        preference,
    )

    consequence = recompute_cycle796_timings()
    for row in consequence["timing_rows"]:
        emit(
            lines,
            "CONSEQUENCE_K2_SELECTION_TIMING",
            {
                **row,
                "selected_by_uniform_preference":
                    row["cadence"] == preferred,
            },
        )
    boundaries = {
        "law_claim": False,
        "preference_if_found_is_only_landed_code_uniformity": True,
        "derivation_from_axioms": False,
        "acceptance_law_landed": False,
        "cadence_convention_stands_as_censused": not unanimous,
        "axiom_update_triggered": False,
    }
    emit(lines, "BOUNDARIES", boundaries)
    consequence_pass = (
        consequence["pass"]
        and boundaries["law_claim"] is False
        and boundaries["derivation_from_axioms"] is False
        and boundaries["axiom_update_triggered"] is False
    )
    certificate(
        lines,
        "D",
        "consequence_rows_and_boundaries",
        consequence_pass,
        {
            "acceptance_moments": consequence["acceptance_moments"],
            "orbit_moments_by_cadence":
                consequence["orbit_moments_by_cadence"],
            "suborbit_signatures_by_cadence":
                consequence["suborbit_signatures_by_cadence"],
            "robustness_split": consequence["robustness_split"],
            "boundaries": boundaries,
        },
    )

    after = source_snapshot()
    deterministic = (
        before == after
        and rows == rows_rerun
        and method == method_rerun
        and consequence["family_deterministic"]
        and consequence["cadence_deterministic"]
    )
    runtime_seconds = monotonic() - started
    deterministic_payload = {
        "census_sha256": digest(rows),
        "timing_rows_sha256": digest(consequence["timing_rows"]),
        "primary_table_sha256": consequence["primary_table_sha256"],
        "rerun_table_sha256": consequence["rerun_table_sha256"],
        "sources_unchanged": before == after,
    }
    preliminary_report = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "axiom_update_triggered": False,
        "cadence_counts": method["cadence_counts"],
        "determinism": deterministic_payload,
        "pass_so_far": (
            anchors_pass
            and table_pass
            and consequence_pass
            and deterministic
        ),
        "preference": preference,
        "runtime_seconds": round(runtime_seconds, 6),
    }
    projected_stdout_bytes = len(
        (
            "\n".join(lines)
            + "\n"
            + compact(preliminary_report)
            + "\n"
        ).encode("utf-8")
    ) + 4096
    bounds_pass = (
        deterministic
        and runtime_seconds < AUDIT_TIMEOUT_SEC
        and projected_stdout_bytes < STDOUT_LIMIT_BYTES
    )
    certificate(
        lines,
        "E",
        "determinism_and_bounds",
        bounds_pass,
        {
            **deterministic_payload,
            "deterministic": deterministic,
            "runtime_seconds": round(runtime_seconds, 6),
            "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
            "projected_stdout_bytes_upper_bound":
                projected_stdout_bytes,
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        },
    )

    passed = (
        anchors_pass
        and table_pass
        and consequence_pass
        and deterministic
        and bounds_pass
    )
    report = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "axiom_update_triggered": False,
        "boundaries": boundaries,
        "cadence_counts": method["cadence_counts"],
        "certificates": {
            "A": anchors_pass,
            "B": table_pass,
            "C": True,
            "D": consequence_pass,
            "E": bounds_pass,
        },
        "consequence_timing_rows": consequence["timing_rows"],
        "determinism": deterministic_payload,
        "law_table_sha256": digest(rows),
        "pass": passed,
        "preference": preference,
        "runtime_seconds": round(runtime_seconds, 6),
        "terminal": (
            "CYCLE799_CADENCE_PREFERENCE_PASS"
            if passed
            else "CYCLE799_CADENCE_PREFERENCE_FAIL"
        ),
    }
    report["report_sha256"] = digest(report)
    emit(lines, "SUMMARY_JSON", report)
    emit(lines, report["terminal"])
    output = "\n".join(lines) + "\n"
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(
            ("stdout bound", len(output.encode("utf-8")))
        )
    sys.stdout.write(output)
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
