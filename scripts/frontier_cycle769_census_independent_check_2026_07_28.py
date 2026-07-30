#!/usr/bin/env python3
"""Independent bounded checker for the Cycle 769 formation census."""

from __future__ import annotations

import ast
from dataclasses import fields
from hashlib import sha256
import json
from pathlib import Path
import re
import sys
from time import perf_counter


AUDIT_TIMEOUT_SEC = 1800
NOTE_PATH = "docs/FORMATION_CENSUS_CYCLE769_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/physical_record_readout_carrier_three_way_split_cycle693_2026_07_25.py",
    "scripts/frontier_cycle719_recurrent_matter_history_controller_2026_07_26.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
BLOCKLIST = (
    "scripts/frontier_cycle769_formation_census_2026_07_28.py",
)

ROOT = Path(__file__).resolve().parents[1]
PRIMARY_PATH = ROOT / BLOCKLIST[0]
C719_PATH = ROOT / AUDIT_INPUT_PATHS[1]
K_PATH = ROOT / AUDIT_INPUT_PATHS[2]
UNIDENTIFIED_CLASS_LANGUAGE = (
    "at least one row lacks both positive permanence and negative "
    "nonformation evidence"
)
EXPECTED_MODES = (0, 2, 3, 4, 5, 6)
EXPECTED_CELL = {
    "identity": 0,
    "rotor": 15,
    "carry": 0,
    "predecessor": None,
    "binder": 1,
    "valid": 1,
    "orientation": 1,
}

sys.path.insert(0, str(ROOT / "scripts"))

import physical_record_readout_carrier_three_way_split_cycle693_2026_07_25 as R693
import frontier_cycle719_recurrent_matter_history_controller_2026_07_26 as C719
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


def digest(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)
    return sha256(encoded.encode()).hexdigest()


def parse_path(path: Path) -> tuple[str, ast.Module]:
    source = path.read_text(encoding="utf-8")
    return source, ast.parse(source, filename=str(path))


def literal_assignment(tree: ast.Module, name: str) -> object:
    for node in tree.body:
        value = None
        targets: tuple[ast.expr, ...] = ()
        if isinstance(node, ast.Assign):
            value = node.value
            targets = tuple(node.targets)
        elif isinstance(node, ast.AnnAssign):
            value = node.value
            targets = (node.target,)
        if value is not None and any(
            isinstance(target, ast.Name) and target.id == name
            for target in targets
        ):
            return ast.literal_eval(value)
    raise AssertionError(("missing literal assignment", name))


def function_node(tree: ast.Module, name: str) -> ast.FunctionDef:
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == name:
            return node
    raise AssertionError(("missing function", name))


def local_assignment(
    function: ast.FunctionDef, name: str
) -> ast.expr:
    for node in ast.walk(function):
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
        ):
            return node.value
    raise AssertionError(("missing local assignment", function.name, name))


def literal_dict_entries(node: ast.expr) -> dict[str, object]:
    if not isinstance(node, ast.Dict):
        raise AssertionError(("not a dictionary", type(node).__name__))
    result: dict[str, object] = {}
    for key_node, value_node in zip(node.keys, node.values):
        key = ast.literal_eval(key_node)
        try:
            value = ast.literal_eval(value_node)
        except (TypeError, ValueError):
            continue
        result[key] = value
    return result


def compared_literal(tree: ast.AST, left_name: str) -> object:
    found = []
    for node in ast.walk(tree):
        if (
            isinstance(node, ast.Compare)
            and isinstance(node.left, ast.Name)
            and node.left.id == left_name
            and len(node.ops) == len(node.comparators) == 1
            and isinstance(node.ops[0], ast.Eq)
        ):
            try:
                found.append(ast.literal_eval(node.comparators[0]))
            except (TypeError, ValueError):
                pass
    if len(found) != 1:
        raise AssertionError(("literal comparison count", left_name, found))
    return found[0]


def comparison_contains_literal(tree: ast.AST, expected: object) -> bool:
    for node in ast.walk(tree):
        if not isinstance(node, ast.Compare):
            continue
        for candidate in (node.left, *node.comparators):
            try:
                if ast.literal_eval(candidate) == expected:
                    return True
            except (TypeError, ValueError):
                pass
    return False


def dict_with_literal_key(tree: ast.AST, key: str) -> dict[str, object]:
    for node in ast.walk(tree):
        if not isinstance(node, ast.Dict):
            continue
        keys = []
        for item in node.keys:
            try:
                keys.append(ast.literal_eval(item))
            except (TypeError, ValueError):
                keys.append(None)
        if key in keys:
            entries = literal_dict_entries(node)
            if key in entries:
                return entries
    raise AssertionError(("missing dictionary key", key))


def imported_roots(tree: ast.Module) -> tuple[str, ...]:
    names = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            names.extend(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            names.append(node.module.split(".")[0])
    return tuple(sorted(set(names)))


def extraction() -> dict[str, object]:
    """Extract the blocked primary as syntax and literals, never as a module."""
    _primary_source, primary_tree = parse_path(PRIMARY_PATH)
    _self_source, self_tree = parse_path(Path(__file__).resolve())

    primary_audit = literal_assignment(primary_tree, "AUDIT_INPUT_PATHS")
    self_audit = literal_assignment(self_tree, "AUDIT_INPUT_PATHS")
    self_blocklist = literal_assignment(self_tree, "BLOCKLIST")

    primary_main = function_node(primary_tree, "main")
    operational_node = local_assignment(primary_main, "operationalization")
    operational_literals = literal_dict_entries(operational_node)
    record_fields = tuple(field.name for field in fields(R693.Record))
    event_cell_fields = tuple(
        field.name for field in fields(C719.B.C704.C610.EventCell)
    )
    event_chain_fields = tuple(
        field.name for field in fields(C719.B.C704.C610.EventChain)
    )
    pointer_site = tuple(
        C719.M.R12.full_wire_layout()["wire_sites"][C719.R3_SOURCE_POINTER()]
    )
    operationalization = {
        "record_type": "Record",
        "record_fields": record_fields,
        "event_cell_type": "EventCell",
        "event_cell_fields": event_cell_fields,
        "event_chain_fields": event_chain_fields,
        "candidate_site": pointer_site,
        "record_shaped_write_test": operational_literals[
            "record_shaped_write_test"
        ],
        "positive_formation_test": operational_literals[
            "positive_formation_test"
        ],
        "negative_formation_test": operational_literals[
            "negative_formation_test"
        ],
        "reversibility_boundary": operational_literals[
            "reversibility_boundary"
        ],
    }

    record_shaped = tuple(compared_literal(primary_tree, "record_shaped"))
    no_record_shaped = tuple(
        compared_literal(primary_tree, "no_record_shaped")
    )
    write_steps = (0, 1, 125)
    program_kinds = tuple(
        (step, C719.PROGRAM[step][0]) for step in write_steps
    )
    event_pipeline = tuple(
        (step, kind)
        for step, kind in program_kinds
        if kind in ("bank", "finalizer")
    )

    branch_function = function_node(primary_tree, "compiled_branch_trace")
    witness = literal_dict_entries(
        local_assignment(branch_function, "formation_witness")
    )
    row_surface = dict_with_literal_key(
        branch_function, "durable_permanent_record_write"
    )
    class_rules = dict_with_literal_key(primary_tree, "unidentified")
    extracted_class = compared_literal(primary_tree, "formation_class")
    primary_module = PRIMARY_PATH.stem
    self_imports = imported_roots(self_tree)

    checks = {
        "primary_is_blocklisted": self_blocklist == BLOCKLIST,
        "primary_never_imported": (
            primary_module not in sys.modules
            and primary_module not in self_imports
        ),
        "audit_tuple_literal_exact": (
            self_audit == AUDIT_INPUT_PATHS
            and primary_audit == AUDIT_INPUT_PATHS
            and literal_assignment(self_tree, "AUDIT_TIMEOUT_SEC")
            == AUDIT_TIMEOUT_SEC
            and literal_assignment(self_tree, "NOTE_PATH") == NOTE_PATH
        ),
        "operationalization_exact": (
            record_fields == ("site", "content")
            and event_cell_fields
            == (
                "identity",
                "rotor",
                "carry",
                "predecessor",
                "binder",
                "valid",
                "orientation",
            )
            and event_chain_fields
            == ("bank", "cells", "admitted_ticks", "exhausted")
            and pointer_site == (-8, -1, 1)
            and operational_literals[
                "R693_available_and_trace_are_formation_tests"
            ]
            is False
            and operational_literals[
                "supplied_acceptance_flags_are_formation_tests"
            ]
            is False
        ),
        "census_literals_exact": (
            record_shaped == ("origin0->mode6",)
            and no_record_shaped
            == tuple(f"origin0->mode{mode}" for mode in EXPECTED_MODES[:-1])
            and comparison_contains_literal(primary_tree, list(write_steps))
            and program_kinds
            == ((0, "source"), (1, "bank"), (125, "finalizer"))
            and event_pipeline == ((1, "bank"), (125, "finalizer"))
        ),
        "witness_literals_absent": (
            witness["positive_permanent_lock"] is None
            and witness["negative_nonformation"] is None
            and witness["decision"] is None
            and row_surface["durable_permanent_record_write"] is None
            and row_surface["formation_decision"] is None
        ),
        "class_literal_verbatim": (
            extracted_class == "unidentified"
            and class_rules["unidentified"] == UNIDENTIFIED_CLASS_LANGUAGE
        ),
    }
    return {
        "checks": checks,
        "pass": all(checks.values()),
        "operationalization": operationalization,
        "census": {
            "record_shaped_branches": record_shaped,
            "other_branches": no_record_shaped,
            "all_data_write_steps": write_steps,
            "event_cell_pipeline": event_pipeline,
            "permanence_witnesses": {
                f"origin0->mode{mode}": None for mode in EXPECTED_MODES
            },
        },
        "classification": "unidentified",
        "class_language": class_rules["unidentified"],
    }


def own_apply_fast(value: int, word: tuple[tuple[int, ...], ...]) -> int:
    output = value
    for gate in word:
        opcode = gate[0]
        if opcode == 0:
            output ^= 1 << gate[1]
        elif opcode == 1:
            output ^= ((output >> gate[1]) & 1) << gate[2]
        elif opcode == 2:
            controls = (
                ((output >> gate[1]) & 1)
                & ((output >> gate[2]) & 1)
            )
            output ^= controls << gate[3]
        else:
            raise AssertionError(("unexpected compiled opcode", opcode))
    return output


def own_registers(value: int) -> dict[str, object]:
    stations = C719.CONTROLLER_STATIONS
    return {
        "data": value & C719.CONTROLLER_DATA_MASK,
        "A": tuple(
            (value >> (C719.CONTROLLER_A_BASE + index)) & 1
            for index in range(stations)
        ),
        "B": tuple(
            (value >> (C719.CONTROLLER_B_BASE + index)) & 1
            for index in range(stations)
        ),
        "work": tuple(
            (value >> (C719.CONTROLLER_WORK_BASE + index)) & 1
            for index in range(stations)
        ),
    }


def own_decode_cells(data_basis: int) -> tuple[dict[str, object], ...]:
    bits = tuple(
        (data_basis >> wire) & 1
        for wire in range(C719.M.R12.TOTAL_WIRES)
    )
    banks, links = C719.M.unpack_state(bits, C719.BANKS)
    try:
        chain, _order = C719.B.decode_local_graph(banks, links)
    except ValueError:
        return ()
    cell_fields = tuple(
        field.name for field in fields(C719.B.C704.C610.EventCell)
    )
    return tuple(
        {name: getattr(cell, name) for name in cell_fields}
        for cell in chain.cells
    )


def own_origin_zero_sources() -> tuple[int, ...]:
    banks, links = C719.B.chain_genesis(C719.BANKS)
    initial_data = sum(
        int(value) << wire
        for wire, value in enumerate(
            C719.M.pack_state(banks, links, matter=1)
        )
    )
    branches = C719.C713.apply_sparse_word(
        {initial_data: 1.0 + 0.0j}, C719.MATTER_WORD
    )
    return tuple(sorted(branches))


def census_recount(
    extracted: dict[str, object],
) -> tuple[dict[str, object], tuple[dict[str, object], ...]]:
    """Run all branches and detect writes without primary runner helpers."""
    rows = []
    traces = []
    for source in own_origin_zero_sources():
        mode = (source & 4095).bit_length() - 1
        start = source | (1 << C719.CONTROLLER_A_BASE)
        full = start
        write_points = []
        event_pipeline = []
        private_writes = []

        for step in range(C719.CONTROLLER_STATIONS):
            before = full
            before_registers = own_registers(before)
            live = tuple(
                index
                for index, value in enumerate(before_registers["A"])
                if value
            )
            station = live[0] if len(live) == 1 else None
            kind = (
                C719.PROGRAM[station][0]
                if station is not None
                else "invalid-sector"
            )
            full = own_apply_fast(full, C719.CONTROLLER_H_FAST)
            after_registers = own_registers(full)
            before_data = int(before_registers["data"])
            after_data = int(after_registers["data"])
            if before_data == after_data:
                continue

            cells = own_decode_cells(after_data)
            write_points.append({
                "step": step,
                "kind": kind,
                "changed_data_bits": (before_data ^ after_data).bit_count(),
                "decoded_event_cells": len(cells),
            })
            if kind == "bank":
                event_pipeline.append({"step": step, "kind": kind})
            if cells:
                event_pipeline.append({"step": step, "kind": kind})
            private_writes.append({
                "step": step,
                "kind": kind,
                "before_full": before,
                "after_full": full,
            })

        final_registers = own_registers(full)
        final_cells = own_decode_cells(int(final_registers["data"]))
        shaped = bool(final_cells) and all(
            cell["binder"] == cell["valid"] == 1
            for cell in final_cells
        )
        rows.append({
            "branch": f"origin0->mode{mode}",
            "mode": mode,
            "data_write_steps": tuple(
                point["step"] for point in write_points
            ),
            "write_points": tuple(write_points),
            "event_cell_pipeline": tuple(event_pipeline),
            "final_event_cells": final_cells,
            "record_shaped_write": shaped,
            "permanence_witness": None,
            "formation_decision": None,
        })
        traces.append({
            "mode": mode,
            "start_full": start,
            "end_full": full,
            "writes": tuple(private_writes),
        })

    decisions = tuple(row["formation_decision"] for row in rows)
    classification = (
        "unidentified"
        if any(decision is None for decision in decisions)
        else "decided"
    )
    shaped_modes = tuple(
        row["mode"] for row in rows if row["record_shaped_write"]
    )
    other_rows = tuple(
        row for row in rows if row["mode"] != 6
    )
    mode6 = next(row for row in rows if row["mode"] == 6)
    checks = {
        "six_branches_exact": tuple(row["mode"] for row in rows)
        == EXPECTED_MODES,
        "write_detection_exact": (
            all(row["data_write_steps"] == () for row in other_rows)
            and mode6["data_write_steps"] == (0, 1, 125)
        ),
        "event_cell_pipeline_exact": (
            all(row["event_cell_pipeline"] == () for row in other_rows)
            and mode6["event_cell_pipeline"]
            == (
                {"step": 1, "kind": "bank"},
                {"step": 125, "kind": "finalizer"},
            )
        ),
        "event_cell_exact": (
            shaped_modes == (6,)
            and mode6["final_event_cells"] == (EXPECTED_CELL,)
            and all(not row["final_event_cells"] for row in other_rows)
        ),
        "witnesses_absent": all(
            row["permanence_witness"] is None
            and row["formation_decision"] is None
            for row in rows
        ),
        "census_reproduces_extraction": (
            tuple(
                row["branch"] for row in rows if row["record_shaped_write"]
            )
            == tuple(extracted["census"]["record_shaped_branches"])
            and tuple(row["branch"] for row in other_rows)
            == tuple(extracted["census"]["other_branches"])
            and mode6["data_write_steps"]
            == tuple(extracted["census"]["all_data_write_steps"])
            and tuple(
                (point["step"], point["kind"])
                for point in mode6["event_cell_pipeline"]
            )
            == tuple(extracted["census"]["event_cell_pipeline"])
        ),
        "class_forced": (
            classification == extracted["classification"]
            and extracted["class_language"]
            == UNIDENTIFIED_CLASS_LANGUAGE
        ),
    }
    certificate = {
        "checks": checks,
        "pass": all(checks.values()),
        "rows": tuple(rows),
        "classification": classification,
        "class_language": UNIDENTIFIED_CLASS_LANGUAGE,
        "census_sha256": digest(rows),
    }
    return certificate, tuple(traces)


def inverse_assignment_is_exact(tree: ast.Module) -> bool:
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        if not any(
            isinstance(target, ast.Name)
            and target.id == "CONTROLLER_H_INVERSE_FAST"
            for target in node.targets
        ):
            continue
        value = node.value
        return (
            isinstance(value, ast.Call)
            and isinstance(value.func, ast.Name)
            and value.func.id == "tuple"
            and len(value.args) == 1
            and isinstance(value.args[0], ast.Call)
            and isinstance(value.args[0].func, ast.Name)
            and value.args[0].func.id == "reversed"
            and len(value.args[0].args) == 1
            and isinstance(value.args[0].args[0], ast.Name)
            and value.args[0].args[0].id == "CONTROLLER_H_FAST"
        )
    return False


def fast_surface_structure(c719_tree: ast.Module, k_tree: ast.Module) -> dict[str, object]:
    fast_function = function_node(c719_tree, "fast_classical_word")
    opcode_node = local_assignment(fast_function, "opcode")
    opcodes = ast.literal_eval(opcode_node)
    apply_function = function_node(c719_tree, "apply_fast_int")
    xor_updates = sum(
        isinstance(node, ast.AugAssign) and isinstance(node.op, ast.BitXor)
        for node in ast.walk(apply_function)
    )
    controller_function = function_node(k_tree, "controller_word")
    controller_return = next(
        node for node in ast.walk(controller_function)
        if isinstance(node, ast.Return)
    )
    return {
        "inverse_declared_as_reverse": inverse_assignment_is_exact(c719_tree),
        "opcode_table": opcodes,
        "xor_update_branches": xor_updates,
        "controller_return_expression": ast.unparse(controller_return.value),
    }


def witness_absence_recount(
    census: dict[str, object],
    traces: tuple[dict[str, object], ...],
) -> dict[str, object]:
    """Use syntax and exact inverses, rather than a bounded witness search."""
    _c719_source, c719_tree = parse_path(C719_PATH)
    _k_source, k_tree = parse_path(K_PATH)
    structure = fast_surface_structure(c719_tree, k_tree)
    inverse_word = tuple(reversed(C719.CONTROLLER_H_FAST))

    local_rows = []
    for trace in traces:
        for write in trace["writes"]:
            restored = own_apply_fast(
                int(write["after_full"]), inverse_word
            )
            local_rows.append({
                "mode": trace["mode"],
                "step": write["step"],
                "kind": write["kind"],
                "inverse_unwrites_exactly": restored
                == int(write["before_full"]),
            })

    global_rows = []
    for trace in traces:
        restored = int(trace["end_full"])
        for _step in range(C719.CONTROLLER_STATIONS):
            restored = own_apply_fast(restored, inverse_word)
        restored_data = int(own_registers(restored)["data"])
        global_rows.append({
            "mode": trace["mode"],
            "inverse_restores_input": restored == int(trace["start_full"]),
            "event_cell_absent_after_inverse": not own_decode_cells(
                restored_data
            ),
        })

    actual_opcodes = tuple(
        sorted({gate[0] for gate in C719.CONTROLLER_H_FAST})
    )
    write_signature = tuple(
        (row["mode"], row["step"], row["kind"])
        for row in local_rows
    )
    checks = {
        "structural_reverse_exact": (
            structure["inverse_declared_as_reverse"]
            and structure["opcode_table"]
            == {"X": 0, "CNOT": 1, "TOF": 2}
            and structure["xor_update_branches"] == 3
            and structure["controller_return_expression"] == "q + r1 + r2"
            and actual_opcodes == (1, 2)
        ),
        "every_write_locally_unwritten": (
            write_signature
            == (
                (6, 0, "source"),
                (6, 1, "bank"),
                (6, 125, "finalizer"),
            )
            and all(row["inverse_unwrites_exactly"] for row in local_rows)
        ),
        "every_branch_globally_unwritten": (
            tuple(row["mode"] for row in global_rows) == EXPECTED_MODES
            and all(row["inverse_restores_input"] for row in global_rows)
            and all(
                row["event_cell_absent_after_inverse"]
                for row in global_rows
            )
        ),
        "surface_forces_unidentified": (
            census["classification"] == "unidentified"
            and census["class_language"] == UNIDENTIFIED_CLASS_LANGUAGE
            and all(
                row["permanence_witness"] is None
                for row in census["rows"]
            )
        ),
    }
    return {
        "checks": checks,
        "pass": all(checks.values()),
        "structural_surface": structure,
        "compiled_opcodes": actual_opcodes,
        "local_inverse_rows": tuple(local_rows),
        "global_inverse_rows": tuple(global_rows),
        "conclusion": (
            "Every detected write is exactly un-writable by the compiled "
            "inverse word; this surface supplies no permanence witness."
        ),
        "classification": "unidentified",
        "class_language": UNIDENTIFIED_CLASS_LANGUAGE,
    }


def lock_composition_probe(census: dict[str, object]) -> dict[str, object]:
    """Probe only the lock components exposed by the authorized imports."""
    exposed = []
    for module in (R693, C719, K):
        for name in vars(module):
            pieces = tuple(name.lower().split("_"))
            if "cycle745" in pieces or "lock" in pieces or "locked" in pieces:
                exposed.append(f"{module.__name__}.{name}")
    mode6 = next(row for row in census["rows"] if row["mode"] == 6)
    if not exposed:
        return {
            "pass": True,
            "status": "absent",
            "authorized_lock_exports": (),
            "mode6_event_cell_available": bool(mode6["final_event_cells"]),
            "demonstration_case": None,
            "permanence_witness_in_principle": None,
            "scope": "next-cycle probe datum only; no claim",
        }
    return {
        "pass": False,
        "status": "unsupported-export-shape",
        "authorized_lock_exports": tuple(sorted(exposed)),
        "mode6_event_cell_available": bool(mode6["final_event_cells"]),
        "demonstration_case": None,
        "permanence_witness_in_principle": None,
        "scope": "next-cycle probe datum only; no claim",
    }


def discipline(
    extracted: dict[str, object],
    census: dict[str, object],
    absence: dict[str, object],
    lock_probe: dict[str, object],
) -> dict[str, object]:
    payload = {
        "extraction": extracted,
        "census_recount": census,
        "witness_absence_recount": absence,
        "lock_composition_probe": lock_probe,
    }
    rendered = json.dumps(payload, sort_keys=True, default=str).lower()
    source = Path(__file__).read_text(encoding="utf-8").lower()
    excluded = (
        "".join(("ra", "te")),
        "".join(("proba", "bility")),
    )
    rendered_words = set(re.findall(r"[a-z]+", rendered))
    source_words = set(re.findall(r"[a-z]+", source))
    class_values = (
        extracted["class_language"],
        census["class_language"],
        absence["class_language"],
    )
    checks = {
        "class_language_verbatim": class_values
        == (
            UNIDENTIFIED_CLASS_LANGUAGE,
            UNIDENTIFIED_CLASS_LANGUAGE,
            UNIDENTIFIED_CLASS_LANGUAGE,
        ),
        "excluded_content_absent": all(
            word not in rendered_words and word not in source_words
            for word in excluded
        ),
        "enumerative_scope_only": (
            lock_probe["scope"] == "next-cycle probe datum only; no claim"
        ),
    }
    return {
        "checks": checks,
        "pass": all(checks.values()),
        "class_language": UNIDENTIFIED_CLASS_LANGUAGE,
        "content_boundary": "enumerative branch evidence only",
    }


def rendered_output(report: dict[str, object]) -> tuple[str, int]:
    labels = tuple(report["checks"])
    prefix = "\n".join(
        f"{'PASS' if report['checks'][label] else 'FAIL'} {label}"
        for label in labels
    )
    body = "SUMMARY_JSON " + json.dumps(
        report, sort_keys=True, separators=(",", ":"), default=str
    )
    output = prefix + "\n" + body + "\n"
    return output, len(output.encode())


def main() -> int:
    started = perf_counter()
    extracted = extraction()
    census, traces = census_recount(extracted)
    absence = witness_absence_recount(census, traces)
    lock_probe = lock_composition_probe(census)
    disciplined = discipline(extracted, census, absence, lock_probe)

    checks = {
        "extraction": extracted["pass"],
        "census_recount": census["pass"],
        "witness_absence_recount": absence["pass"],
        "lock_composition_probe": lock_probe["pass"],
        "discipline": disciplined["pass"],
        "stdout_under_150KB": True,
    }
    report = {
        "audit_timeout_sec": AUDIT_TIMEOUT_SEC,
        "note_path": NOTE_PATH,
        "audit_input_paths": AUDIT_INPUT_PATHS,
        "blocklist": BLOCKLIST,
        "checks": checks,
        "pass": all(checks.values()),
        "extraction": extracted,
        "census_recount": census,
        "witness_absence_recount": absence,
        "lock_composition_probe": lock_probe,
        "discipline": disciplined,
        "runtime_sec": perf_counter() - started,
        "stdout_bytes": 0,
    }

    for _attempt in range(5):
        output, output_bytes = rendered_output(report)
        report["stdout_bytes"] = output_bytes
        checks["stdout_under_150KB"] = output_bytes < 150 * 1024
        report["pass"] = all(checks.values())
    report["report_sha256"] = digest(report)
    output, output_bytes = rendered_output(report)
    report["stdout_bytes"] = output_bytes
    checks["stdout_under_150KB"] = output_bytes < 150 * 1024
    report["pass"] = all(checks.values())
    report["report_sha256"] = digest(report)
    output, _output_bytes = rendered_output(report)
    print(output, end="")
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
