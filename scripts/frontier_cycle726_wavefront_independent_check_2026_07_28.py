#!/usr/bin/env python3
"""Independent checker for the Cycle-726 supplied-table wavefront compiler.

The Cycle-726 primary is never imported.  Its transition ROM, phase encoding,
gating declarations, constants, and compiler structure are read only as AST
data.  All transition replay and Fredkin/sandwich semantics below are
independent implementations.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/WAVEFRONT_CONTROLLER_M2_COMPILER_CYCLE726_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle726_wavefront_controller_m2_compiler_2026_07_28.py",
    "scripts/frontier_cycle718_spatial_ack_physical_m2_route_2026_07_26.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from hashlib import sha256
import json
from pathlib import Path
import sys
from time import perf_counter
from typing import Callable

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
PRIMARY_PATH = AUDIT_INPUT_PATHS[0]
PRIMARY_MODULE = "frontier_cycle726_wavefront_controller_m2_compiler_2026_07_28"
TOP_LEVEL_BLOCKLIST = {PRIMARY_MODULE}

if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import frontier_cycle718_spatial_ack_physical_m2_route_2026_07_26 as P


_BLOCKED_AFTER_IMPORTS = sorted(TOP_LEVEL_BLOCKLIST & set(sys.modules))
assert not _BLOCKED_AFTER_IMPORTS, (
    f"Cycle-726 primary imported transitively: {_BLOCKED_AFTER_IMPORTS}"
)

EXPECTED_PHASE_ENCODING = {
    "IDLE": (0, 0),
    "DOWN": (1, 0),
    "ACK": (0, 1),
}
EXPECTED_PREDICATE_FIELDS = (
    "pointer",
    "endpoint",
    "law0",
    "law1",
    "law2",
    "law3",
    "allocator_TOKEN",
    "allocator_FRESH",
    "allocator_HEAD",
    "allocator_ROTOR",
    "allocator_valid",
    "allocator_interface",
    "destination_blank",
    "link_latch_clean",
    "link_work_clean",
    "pending",
    "rail_start",
    "rail_valid",
    "rail_cleanup",
    "retry_echo",
    "exhausted",
    "boundary",
    "prewrap",
    "wrap",
)
EXPECTED_MACRO_FAMILIES = (
    "shield",
    "decoded",
    "commit",
    "pending_refusal",
    "handoff_relay",
    "shift",
    "return",
    "source_cleanup",
)
EXPECTED_ROW_NAMES = (
    "down_boundary",
    "down_wrap",
    "down_exhaustion",
    "down_prewrap",
    "down_empty_event",
    "down_bad_endpoint",
    "down_bad_law0",
    "down_bad_law1",
    "down_bad_law2",
    "down_bad_law3",
    "down_bad_allocator",
    "down_bad_interface",
    "down_dirty_link",
    "down_pending_refusal",
    "down_dirty_destination",
    "down_dirty_rail",
    "down_commit",
    "ack_return",
    "ack_source_cleanup",
)
REQUIRED_D7_CASE_CLASSES = {
    "commit",
    "pending/refusal",
    "empty event",
    "dirty/unlawful destination",
    "exhaustion",
    "boundary",
    "pre-wrap/wrap",
}
EXPECTED_GATING_PATHS = {
    "shield": "classical extra-control lift",
    "commit": "classical extra-control lift",
    "pending_refusal": "classical extra-control lift",
    "handoff_relay": "classical extra-control lift",
    "shift": "classical extra-control lift",
    "return": "classical extra-control lift",
    "source_cleanup": "classical extra-control lift",
    "decoded_H_T_word": "enable-latched Fredkin spectator rerouting",
}
EXPECTED_PRIMARY_AUDIT_INPUTS = (
    "scripts/frontier_cycle718_spatial_ack_physical_m2_route_2026_07_26.py",
    "scripts/frontier_cycle718_token_relative_relay_core_2026_07_26.py",
    "scripts/frontier_cycle718_carrier_return_core_2026_07_26.py",
)
CHECKS: list[dict[str, object]] = []
_PRIMARY_CACHE: tuple[str, ast.Module] | None = None
_FIXTURE_13_LAYOUT: dict[str, object] | None = None


def call_path(node: ast.AST) -> str | None:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        prefix = call_path(node.value)
        return f"{prefix}.{node.attr}" if prefix else node.attr
    return None


def source_tree() -> tuple[str, ast.Module]:
    global _PRIMARY_CACHE
    if _PRIMARY_CACHE is None:
        source = (ROOT / PRIMARY_PATH).read_text(encoding="utf-8")
        _PRIMARY_CACHE = (
            source,
            ast.parse(source, filename=PRIMARY_PATH),
        )
    return _PRIMARY_CACHE


def module_assignment(tree: ast.Module, name: str) -> ast.AST:
    matches: list[ast.AST] = []
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
            matches.append(value)
    if len(matches) != 1:
        raise ValueError(("module assignment", name, len(matches)))
    return matches[0]


def function_definitions(tree: ast.Module) -> dict[str, ast.FunctionDef]:
    return {
        node.name: node
        for node in tree.body
        if isinstance(node, ast.FunctionDef)
    }


def literal_assignment(tree: ast.Module, name: str) -> object:
    return ast.literal_eval(module_assignment(tree, name))


def extract_transition_rows(tree: ast.Module) -> tuple[dict[str, object], ...]:
    table_node = module_assignment(tree, "TRANSITION_TABLE")
    if not isinstance(table_node, (ast.Tuple, ast.List)):
        raise ValueError("TRANSITION_TABLE is not a literal sequence")
    rows: list[dict[str, object]] = []
    for index, element in enumerate(table_node.elts):
        if (
            not isinstance(element, ast.Call)
            or call_path(element.func) != "TransitionRow"
            or len(element.args) not in (6, 7)
        ):
            raise ValueError(("non-data transition row", index))
        values = [ast.literal_eval(argument) for argument in element.args]
        keywords = {
            keyword.arg: ast.literal_eval(keyword.value)
            for keyword in element.keywords
            if keyword.arg is not None
        }
        if len(keywords) != len(element.keywords):
            raise ValueError(("expanded transition keyword", index))
        unknown = set(keywords) - {"site_role"}
        if unknown:
            raise ValueError(("unknown transition keywords", index, unknown))
        name, case_class, phase, pattern, enables, next_action = values[:6]
        positional_site_role = values[6] if len(values) == 7 else "any"
        if "site_role" in keywords and len(values) == 7:
            raise ValueError(("duplicate site_role", index))
        rows.append({
            "name": str(name),
            "case_class": str(case_class),
            "phase": str(phase),
            "pattern": tuple(
                (str(field), int(value)) for field, value in pattern
            ),
            "enables": tuple(str(family) for family in enables),
            "next_action": str(next_action),
            "site_role": str(keywords.get(
                "site_role", positional_site_role
            )),
            "source_line": element.lineno,
        })
    return tuple(rows)


def extract_named_dict(tree: ast.Module, key_name: str) -> dict[str, str]:
    matches: list[ast.AST] = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Dict):
            continue
        for key, value in zip(node.keys, node.values, strict=True):
            if (
                isinstance(key, ast.Constant)
                and key.value == key_name
            ):
                matches.append(value)
    if len(matches) != 1:
        raise ValueError(("named dict", key_name, len(matches)))
    value = ast.literal_eval(matches[0])
    if not isinstance(value, dict):
        raise ValueError(("named value is not dict", key_name))
    return {str(key): str(item) for key, item in value.items()}


def table_extraction() -> dict[str, object]:
    _source, tree = source_tree()
    rows = extract_transition_rows(tree)
    phases = {
        label: literal_assignment(tree, f"PHASE_{label}")
        for label in EXPECTED_PHASE_ENCODING
    }
    predicates = literal_assignment(tree, "PREDICATE_FIELDS")
    macro_families = literal_assignment(tree, "MACRO_FAMILIES")
    fixture_lengths = literal_assignment(tree, "FIXTURE_LENGTHS")
    primary_timeout = literal_assignment(tree, "AUDIT_TIMEOUT_SEC")
    primary_note = literal_assignment(tree, "NOTE_PATH")
    primary_audit_node = module_assignment(tree, "AUDIT_INPUT_PATHS")
    primary_audit = ast.literal_eval(primary_audit_node)
    declared_node = module_assignment(tree, "DECLARED_INPUT_PATHS")
    gating_paths = extract_named_dict(tree, "paths_by_family")

    canonical_rows = [
        {
            "name": row["name"],
            "case_class": row["case_class"],
            "phase": row["phase"],
            "pattern": row["pattern"],
            "enables": row["enables"],
            "next_action": row["next_action"],
            "site_role": row["site_role"],
        }
        for row in rows
    ]
    table_digest = sha256(json.dumps(
        canonical_rows,
        sort_keys=True,
        separators=(",", ":"),
    ).encode()).hexdigest()
    case_classes = {str(row["case_class"]) for row in rows}
    row_names = tuple(str(row["name"]) for row in rows)
    table_well_formed = bool(
        row_names == EXPECTED_ROW_NAMES
        and len(set(row_names)) == len(rows)
        and all(row["phase"] in {"DOWN", "ACK"} for row in rows)
        and all(
            row["next_action"] in {
                "advance_down",
                "convert_ack",
                "propagate_ack",
                "hold_ack",
            }
            for row in rows
        )
        and all(
            row["site_role"] in {
                "any",
                "source",
                "interior_or_boundary",
            }
            for row in rows
        )
        and all(
            len({field for field, _value in row["pattern"]})
            == len(row["pattern"])
            and all(
                field in EXPECTED_PREDICATE_FIELDS and value in (0, 1)
                for field, value in row["pattern"]
            )
            and all(
                family in EXPECTED_MACRO_FAMILIES
                for family in row["enables"]
            )
            for row in rows
        )
    )
    normalized_gating_families = {
        "decoded" if family == "decoded_H_T_word" else family
        for family in gating_paths
    }
    audit_literal_valid = bool(
        isinstance(primary_audit_node, ast.Tuple)
        and isinstance(primary_audit, tuple)
        and primary_audit == EXPECTED_PRIMARY_AUDIT_INPUTS
        and isinstance(declared_node, ast.Name)
        and declared_node.id == "AUDIT_INPUT_PATHS"
    )
    pinned_constants_valid = bool(
        phases == EXPECTED_PHASE_ENCODING
        and predicates == EXPECTED_PREDICATE_FIELDS
        and macro_families == EXPECTED_MACRO_FAMILIES
        and fixture_lengths == (13, 17)
        and primary_timeout == 900
        and primary_note == NOTE_PATH
    )
    passed = bool(
        table_well_formed
        and REQUIRED_D7_CASE_CLASSES <= case_classes
        and audit_literal_valid
        and pinned_constants_valid
        and gating_paths == EXPECTED_GATING_PATHS
        and normalized_gating_families == set(EXPECTED_MACRO_FAMILIES)
        and not (TOP_LEVEL_BLOCKLIST & set(sys.modules))
    )
    return {
        "pass": passed,
        "primary_read_as_data_only": True,
        "transition_rows": rows,
        "row_count": len(rows),
        "row_names": row_names,
        "table_well_formed": table_well_formed,
        "table_sha256": table_digest,
        "case_classes": sorted(case_classes),
        "required_D7_case_classes": sorted(REQUIRED_D7_CASE_CLASSES),
        "required_D7_case_classes_present": (
            REQUIRED_D7_CASE_CLASSES <= case_classes
        ),
        "phase_encoding": phases,
        "phase_encoding_valid": phases == EXPECTED_PHASE_ENCODING,
        "gating_paths_by_family": gating_paths,
        "gating_paths_valid": gating_paths == EXPECTED_GATING_PATHS,
        "primary_AUDIT_INPUT_PATHS": primary_audit,
        "primary_AUDIT_tuple_literal_valid": audit_literal_valid,
        "pinned_constants": {
            "AUDIT_TIMEOUT_SEC": primary_timeout,
            "NOTE_PATH": primary_note,
            "FIXTURE_LENGTHS": fixture_lengths,
            "PREDICATE_FIELDS": predicates,
            "MACRO_FAMILIES": macro_families,
        },
        "pinned_constants_valid": pinned_constants_valid,
        "blocked_primary_imports_present": sorted(
            TOP_LEVEL_BLOCKLIST & set(sys.modules)
        ),
    }


def apply_classical_gate(
    state: np.ndarray,
    n: int,
    kind: str,
    wires: tuple[int, ...],
) -> np.ndarray:
    output = np.zeros_like(state)
    for basis, amplitude in enumerate(state):
        target = basis
        if kind == "X":
            target ^= 1 << wires[0]
        elif kind == "CNOT":
            if (basis >> wires[0]) & 1:
                target ^= 1 << wires[1]
        elif kind == "TOF":
            if ((basis >> wires[0]) & 1) and ((basis >> wires[1]) & 1):
                target ^= 1 << wires[2]
        else:
            raise ValueError(("unknown classical gate", kind))
        output[target] += amplitude
    if len(output) != 1 << n:
        raise AssertionError((len(output), n))
    return output


def fredkin_word(
    control: int,
    left: int,
    right: int,
) -> tuple[tuple[str, tuple[int, ...]], ...]:
    return (
        ("CNOT", (right, left)),
        ("TOF", (control, left, right)),
        ("CNOT", (right, left)),
    )


def apply_classical_word(
    state: np.ndarray,
    n: int,
    word: tuple[tuple[str, tuple[int, ...]], ...],
) -> np.ndarray:
    for kind, wires in word:
        state = apply_classical_gate(state, n, kind, wires)
    return state


def apply_local_unitary(
    state: np.ndarray,
    n: int,
    wires: tuple[int, ...],
    unitary: np.ndarray,
) -> np.ndarray:
    width = len(wires)
    if unitary.shape != (1 << width, 1 << width):
        raise ValueError(("unitary shape", unitary.shape, width))
    output = np.zeros_like(state)
    clear_mask = sum(1 << wire for wire in wires)
    for basis, amplitude in enumerate(state):
        if amplitude == 0:
            continue
        local_input = sum(
            ((basis >> wire) & 1) << index
            for index, wire in enumerate(wires)
        )
        base = basis & ~clear_mask
        for local_output in range(1 << width):
            coefficient = unitary[local_output, local_input]
            if coefficient == 0:
                continue
            target = base
            for index, wire in enumerate(wires):
                target |= ((local_output >> index) & 1) << wire
            output[target] += coefficient * amplitude
    return output


def signed_paulis(width: int) -> tuple[tuple[str, np.ndarray], ...]:
    one_qubit = {
        "I": np.asarray(((1, 0), (0, 1)), dtype=complex),
        "X": np.asarray(((0, 1), (1, 0)), dtype=complex),
        "Y": np.asarray(((0, -1j), (1j, 0)), dtype=complex),
        "Z": np.asarray(((1, 0), (0, -1)), dtype=complex),
    }
    rows: list[tuple[str, np.ndarray]] = []
    if width == 1:
        for name, matrix in one_qubit.items():
            for sign in (1, -1):
                rows.append((f"{sign:+d}{name}", sign * matrix))
        return tuple(rows)
    if width == 2:
        for left_name, left in one_qubit.items():
            for right_name, right in one_qubit.items():
                # Local wire zero is the least-significant tensor factor.
                matrix = np.kron(right, left)
                for sign in (1, -1):
                    rows.append((
                        f"{sign:+d}{left_name}x{right_name}",
                        sign * matrix,
                    ))
        return tuple(rows)
    raise ValueError(width)


def spectator_wrapper(
    state: np.ndarray,
    n: int,
    enable: int,
    data: tuple[int, ...],
    spectators: tuple[int, ...],
    unitary: np.ndarray,
) -> np.ndarray:
    swaps = tuple(
        gate
        for data_wire, spectator_wire in zip(
            data, spectators, strict=True
        )
        for gate in fredkin_word(enable, data_wire, spectator_wire)
    )
    state = apply_classical_word(state, n, swaps)
    state = apply_local_unitary(state, n, spectators, unitary)
    return apply_classical_word(state, n, tuple(reversed(swaps)))


def expected_spectator_action(
    state: np.ndarray,
    n: int,
    enable: int,
    data: tuple[int, ...],
    spectators: tuple[int, ...],
    unitary: np.ndarray,
) -> np.ndarray:
    output = np.zeros_like(state)
    for branch in (0, 1):
        projected = state.copy()
        for basis in range(1 << n):
            if ((basis >> enable) & 1) != branch:
                projected[basis] = 0
        target_wires = data if branch else spectators
        output += apply_local_unitary(
            projected, n, target_wires, unitary
        )
    return output


def apply_bit_gate(
    bits: list[int],
    kind: str,
    wires: tuple[int, ...],
) -> None:
    if kind == "X":
        bits[wires[0]] ^= 1
    elif kind == "CNOT":
        bits[wires[1]] ^= bits[wires[0]]
    elif kind == "TOF":
        bits[wires[2]] ^= bits[wires[0]] & bits[wires[1]]
    else:
        raise ValueError(kind)


def apply_bit_word(
    bits: list[int],
    word: tuple[tuple[str, tuple[int, ...]], ...],
) -> None:
    for kind, wires in word:
        apply_bit_gate(bits, kind, wires)


def predicate_toggle(
    bits: list[int],
    positive: tuple[int, ...],
    negative: tuple[int, ...],
    target: int,
) -> None:
    for wire in negative:
        bits[wire] ^= 1
    controls = positive + negative
    if all(bits[wire] for wire in controls):
        bits[target] ^= 1
    for wire in reversed(negative):
        bits[wire] ^= 1


def latch_sandwich_case(
    *,
    hold: bool,
    address: int,
    opposite: int,
    source: int,
    action: int,
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    # address, opposite phase, source phase, selector, enable, destination,
    # action port.  Destination is supplied clean; in the hold case it is the
    # source rail itself.
    bits = [address, opposite, source, 0, 0, 0, action]
    selector = 3
    enable = 4
    destination = 2 if hold else 5
    predicate_toggle(bits, (0,), (1,), selector)
    apply_bit_word(bits, fredkin_word(selector, 2, enable))
    predicate_toggle(bits, (0,), (1,), selector)
    apply_bit_gate(bits, "CNOT", (enable, 6))
    phase_negative = (1,) if hold else (2,)
    predicate_toggle(bits, (0,), phase_negative, selector)
    apply_bit_word(bits, fredkin_word(selector, enable, destination))
    predicate_toggle(bits, (0,), phase_negative, selector)
    expected_fire = address & (1 - opposite) & source
    expected = [
        address,
        opposite,
        source if hold else 0 if expected_fire else source,
        0,
        0,
        0 if hold else expected_fire,
        action ^ expected_fire,
    ]
    return tuple(bits), tuple(expected)


def sandwich_and_fredkin_semantics() -> dict[str, object]:
    size_rows: dict[int, dict[str, object]] = {}
    total_cases = total_failures = 0
    maximum_residual = 0.0
    for n in (3, 4, 5):
        width = 2 if n == 5 else 1
        enable = 0
        data = tuple(range(1, 1 + width))
        spectators = tuple(range(1 + width, 1 + 2 * width))
        macros = signed_paulis(width)
        failures = 0
        local_maximum = 0.0
        for _name, unitary in macros:
            for basis in range(1 << n):
                before = np.zeros(1 << n, dtype=complex)
                before[basis] = 1.0
                observed = spectator_wrapper(
                    before, n, enable, data, spectators, unitary
                )
                expected = expected_spectator_action(
                    before, n, enable, data, spectators, unitary
                )
                residual = float(np.linalg.norm(observed - expected))
                local_maximum = max(local_maximum, residual)
                failures += residual > 1.0e-12
        cases = len(macros) * (1 << n)
        total_cases += cases
        total_failures += failures
        maximum_residual = max(maximum_residual, local_maximum)
        size_rows[n] = {
            "operand_width": width,
            "signed_Pauli_macros": len(macros),
            "all_basis_states": 1 << n,
            "identity_cases": cases,
            "failures": failures,
            "maximum_residual": local_maximum,
        }

    unsigned_two_qubit = tuple(
        matrix for index, (_name, matrix) in enumerate(signed_paulis(2))
        if index % 2 == 0
    )
    pauli_span_rank = int(np.linalg.matrix_rank(np.stack([
        matrix.reshape(-1) for matrix in unsigned_two_qubit
    ])))
    latch_rows = latch_failures = 0
    for hold in (False, True):
        for address in (0, 1):
            for opposite in (0, 1):
                for source in (0, 1):
                    for action in (0, 1):
                        observed, expected = latch_sandwich_case(
                            hold=hold,
                            address=address,
                            opposite=opposite,
                            source=source,
                            action=action,
                        )
                        latch_failures += observed != expected
                        latch_rows += 1
    passed = bool(
        total_failures == 0
        and maximum_residual < 1.0e-12
        and pauli_span_rank == 16
        and latch_failures == 0
        and latch_rows == 32
    )
    return {
        "pass": passed,
        "simulator": (
            "independent dense state-vector simulator with explicit "
            "CNOT-Toffoli-CNOT Fredkin words"
        ),
        "qubit_sizes": size_rows,
        "signed_Pauli_identity_cases": total_cases,
        "identity_failures": total_failures,
        "maximum_identity_residual": maximum_residual,
        "unsigned_two_qubit_Pauli_operator_span_rank": pauli_span_rank,
        "arbitrary_two_qubit_U_justification": (
            "the 16 unsigned two-qubit Pauli tensors span all 4x4 "
            "operators, and the wrapper equality is linear in U"
        ),
        "enable_latch_sandwich_rows": latch_rows,
        "enable_latch_sandwich_failures": latch_failures,
        "clean_latch_genesis_and_destination_assumed": True,
    }


def fixture_13_layout() -> dict[str, object]:
    global _FIXTURE_13_LAYOUT
    if _FIXTURE_13_LAYOUT is None:
        _FIXTURE_13_LAYOUT = P.physical_layout(13)
    return _FIXTURE_13_LAYOUT


def row_applies(
    row: dict[str, object],
    site: int,
    length: int,
) -> bool:
    if row["site_role"] == "source":
        return site == 0
    if row["site_role"] == "interior_or_boundary":
        return site > 0
    if row["next_action"] == "advance_down":
        return site + 1 < length
    return True


def row_matches(
    row: dict[str, object],
    down: list[int],
    ack: list[int],
    predicates: list[dict[str, int]],
    site: int,
    length: int,
) -> bool:
    if not row_applies(row, site, length):
        return False
    if row["phase"] == "DOWN":
        if (down[site], ack[site]) != (1, 0):
            return False
    elif row["phase"] == "ACK":
        if (down[site], ack[site]) != (0, 1):
            return False
    else:
        return False
    return all(
        predicates[site][field] == value
        for field, value in row["pattern"]
    )


def owner_location(
    down: list[int],
    ack: list[int],
) -> tuple[str, int] | None:
    owners = [
        ("DOWN", site) for site, value in enumerate(down) if value
    ] + [
        ("ACK", site) for site, value in enumerate(ack) if value
    ]
    return owners[0] if len(owners) == 1 else None


def semantic_step(
    rows: tuple[dict[str, object], ...],
    down: list[int],
    ack: list[int],
    predicates: list[dict[str, int]],
) -> dict[str, object]:
    before_owner = owner_location(down, ack)
    if before_owner is None:
        raise ValueError(("semantic step needs one owner", down, ack))
    _phase, site = before_owner
    matches = [
        row for row in rows
        if row_matches(row, down, ack, predicates, site, len(down))
    ]
    if len(matches) != 1:
        raise ValueError((
            "semantic transition is not unique",
            before_owner,
            tuple(row["name"] for row in matches),
        ))
    row = matches[0]
    enabled = tuple(row["enables"])
    if row["phase"] == "DOWN":
        down[site] = 0
    else:
        ack[site] = 0
    action = row["next_action"]
    if action == "advance_down":
        down[site + 1] = 1
    elif action == "convert_ack":
        ack[site] = 1
    elif action == "propagate_ack":
        ack[site - 1] = 1
    elif action == "hold_ack":
        ack[site] = 1
    else:
        raise ValueError(("unknown next action", action))
    after_owner = owner_location(down, ack)
    return {
        "row": row["name"],
        "site": site,
        "phase": row["phase"],
        "macros": enabled,
        "next_action": action,
        "owner_before": before_owner,
        "owner_after": after_owner,
        "one_hot_after": after_owner is not None,
    }


def row_fixture_site(row: dict[str, object], length: int) -> int:
    if row["site_role"] == "source":
        return 0
    if row["site_role"] == "interior_or_boundary":
        return length - 1
    if row["name"] == "down_boundary":
        return length - 1
    return 0


def expected_owner_after(
    row: dict[str, object],
    site: int,
) -> tuple[str, int]:
    action = row["next_action"]
    if action == "advance_down":
        return ("DOWN", site + 1)
    if action == "convert_ack":
        return ("ACK", site)
    if action == "propagate_ack":
        return ("ACK", site - 1)
    if action == "hold_ack":
        return ("ACK", site)
    raise ValueError(action)


def blank_predicates(length: int) -> list[dict[str, int]]:
    return [
        {field: 0 for field in EXPECTED_PREDICATE_FIELDS}
        for _site in range(length)
    ]


def controller_replay(
    extraction: dict[str, object],
) -> dict[str, object]:
    rows = tuple(extraction["transition_rows"])
    layout = fixture_13_layout()
    length = int(layout["length"])
    isolated: dict[str, object] = {}
    row_failures = ownership_failures = 0
    family_sites: dict[str, list[int]] = {
        family: [] for family in EXPECTED_MACRO_FAMILIES
    }
    isolated_action_events = 0
    for row in rows:
        site = row_fixture_site(row, length)
        predicates = blank_predicates(length)
        predicates[site].update(dict(row["pattern"]))
        down = [0] * length
        ack = [0] * length
        if row["phase"] == "DOWN":
            down[site] = 1
        else:
            ack[site] = 1
        event = semantic_step(rows, down, ack, predicates)
        expected_owner = expected_owner_after(row, site)
        event_ok = bool(
            event["row"] == row["name"]
            and event["macros"] == row["enables"]
            and event["next_action"] == row["next_action"]
            and event["owner_after"] == expected_owner
            and event["one_hot_after"]
        )
        row_failures += not event_ok
        ownership_failures += not event["one_hot_after"]
        isolated_action_events += len(event["macros"])
        for family in event["macros"]:
            family_sites[family].append(site)
        isolated[str(row["name"])] = {
            **event,
            "declared_case_class": row["case_class"],
            "expected_macros": row["enables"],
            "expected_owner_after": expected_owner,
            "row_output_equal": event_ok,
        }

    predicates = blank_predicates(length)
    commit = next(row for row in rows if row["name"] == "down_commit")
    boundary = next(row for row in rows if row["name"] == "down_boundary")
    for site in range(length - 1):
        predicates[site].update(dict(commit["pattern"]))
    predicates[length - 1].update(dict(boundary["pattern"]))
    for site in range(length):
        predicates[site]["link_latch_clean"] = 1
        predicates[site]["link_work_clean"] = 1
    down = [0] * length
    ack = [0] * length
    down[0] = 1
    trace: list[dict[str, object]] = []
    full_family_sites: dict[str, list[int]] = {
        family: [] for family in EXPECTED_MACRO_FAMILIES
    }
    full_ownership_failures = 0
    boundary_conversion_seen = False
    for _step in range(2 * length):
        event = semantic_step(rows, down, ack, predicates)
        trace.append(event)
        full_ownership_failures += not event["one_hot_after"]
        for family in event["macros"]:
            full_family_sites[family].append(int(event["site"]))
        boundary_conversion_seen |= bool(
            event["row"] == "down_boundary"
            and event["owner_before"] == ("DOWN", length - 1)
            and event["owner_after"] == ("ACK", length - 1)
        )
        if event["row"] == "ack_source_cleanup":
            break

    expected_sequence = (
        ("down_commit",) * (length - 1)
        + ("down_boundary",)
        + ("ack_return",) * (length - 1)
        + ("ack_source_cleanup",)
    )
    observed_sequence = tuple(str(event["row"]) for event in trace)
    expected_full_sites = {
        "shield": list(range(length - 1)),
        "decoded": list(range(length - 1)),
        "commit": list(range(length - 1)),
        "pending_refusal": [],
        "handoff_relay": list(range(length - 1)),
        "shift": list(range(length - 1)),
        "return": list(reversed(range(1, length))),
        "source_cleanup": [0],
    }
    full_action_events = sum(
        len(event["macros"]) for event in trace
    )
    fixture_valid = bool(
        length == 13
        and int(layout["placement_collisions"]) == 0
        and int(layout["source_collisions"]) == 0
        and len(layout["assigned_sites"]) > 0
    )
    passed = bool(
        extraction["pass"]
        and fixture_valid
        and len(isolated) == len(rows) == 19
        and row_failures == 0
        and ownership_failures == 0
        and isolated_action_events == 38
        and observed_sequence == expected_sequence
        and full_family_sites == expected_full_sites
        and full_action_events == 73
        and full_ownership_failures == 0
        and boundary_conversion_seen
        and owner_location(down, ack) == ("ACK", 0)
    )
    return {
        "pass": passed,
        "fixture": {
            "entry_point": "P.physical_layout(13)",
            "length": length,
            "assigned_M2": len(layout["assigned_sites"]),
            "rail_M2": len(layout["rail_sites"]),
            "source_collisions": layout["source_collisions"],
            "placement_collisions": layout["placement_collisions"],
            "valid": fixture_valid,
        },
        "declared_lawful_phase_input_rows": len(rows),
        "row_output_matches": len(rows) - row_failures,
        "row_output_failures": row_failures,
        "isolated_ownership_failures": ownership_failures,
        "isolated_action_events": isolated_action_events,
        "isolated_family_sites": family_sites,
        "isolated_rows": isolated,
        "full_replay_steps": len(trace),
        "full_action_events": full_action_events,
        "full_family_sites": full_family_sites,
        "full_row_sequence": observed_sequence,
        "full_row_sequence_expected": expected_sequence,
        "full_ownership_failures": full_ownership_failures,
        "boundary_DOWN_to_ACK_conversion": boundary_conversion_seen,
        "final_owner": owner_location(down, ack),
        "trace": trace,
    }


def unchanged_surface_spot() -> dict[str, object]:
    structured = P.structured_commit_certificate()
    layout = fixture_13_layout()
    built = P.full_physical_word(layout)
    routed, route = P.C712.c707.route_word(built["word"])
    covariance = P.active_covariance(layout, built["word"], routed)
    structured_criteria = {
        "packet_failures": structured["packet_failures"] == 0,
        "full_34_raw_payload_failures": (
            structured["full_34_raw_payload_failures"] == 0
        ),
        "controller_failures": structured["controller_failures"] == 0,
        "transient_or_work_failures": (
            structured["transient_or_work_failures"] == 0
        ),
        "one_decoded_event_failures": (
            structured["one_decoded_event_failures"] == 0
        ),
        "exact_inverse_failures": (
            structured["exact_inverse_failures"] == 0
        ),
        "dirty_and_unlawful_refusal_failures": (
            structured["dirty_and_unlawful_refusal_failures"] == 0
        ),
        "pending_latch_failures": (
            structured["pending_latch_failures"] == 0
        ),
        "arbitrary_inverse_failures": (
            structured["arbitrary_inverse_failures"] == 0
        ),
        "all_deletions_detected": bool(
            structured["all_deletions_detected"]
        ),
    }
    covariance_criteria = {
        "proper_cubic_frames": covariance["proper_cubic_frames"] == 24,
        "ordered_frame_products": (
            covariance["ordered_frame_products"] == 576
        ),
        "active_endpoint_direction_failures": (
            covariance["active_endpoint_direction_failures"] == 0
        ),
        "instruction_coordinate_failures": (
            covariance["instruction_coordinate_failures"] == 0
        ),
        "routed_NN_frame_failures": (
            covariance["routed_NN_frame_failures"] == 0
        ),
        "direction_product_failures": (
            covariance["direction_product_failures"] == 0
        ),
        "translation_failures": (
            covariance["translation_failures"] == 0
        ),
    }
    passed = bool(
        all(structured_criteria.values())
        and all(covariance_criteria.values())
    )
    return {
        "pass": passed,
        "calls": (
            "P.structured_commit_certificate()",
            "P.active_covariance(layout, word, routed)",
        ),
        "structured_commit_own_criteria": structured_criteria,
        "structured_commit": structured,
        "active_covariance_own_criteria": covariance_criteria,
        "active_covariance": covariance,
        "route_for_covariance": {
            "routed_gates": len(routed),
            "non_NN_failures": route["non_NN_failures"],
            "operand_order_failures": route["operand_order_failures"],
            "route_return_failures": route["route_return_failures"],
        },
    }


def assignment_targets(node: ast.AST) -> tuple[ast.AST, ...]:
    if isinstance(node, (ast.Tuple, ast.List)):
        return tuple(
            target
            for element in node.elts
            for target in assignment_targets(element)
        )
    if isinstance(node, ast.Starred):
        return assignment_targets(node.value)
    return (node,)


def attribute_root(node: ast.AST) -> str | None:
    while isinstance(node, (ast.Attribute, ast.Subscript)):
        node = node.value
    return node.id if isinstance(node, ast.Name) else None


def reachable_local_functions(
    functions: dict[str, ast.FunctionDef],
    entry: str,
) -> set[str]:
    reached: set[str] = set()
    pending = [entry]
    while pending:
        name = pending.pop()
        if name in reached:
            continue
        if name not in functions:
            raise ValueError(("missing compiler entry", name))
        reached.add(name)
        for node in ast.walk(functions[name]):
            if not isinstance(node, ast.Call):
                continue
            called = call_path(node.func)
            if called in functions and called not in reached:
                pending.append(called)
    return reached


def branch_conditions(function: ast.FunctionDef) -> list[ast.AST]:
    conditions: list[ast.AST] = []
    for node in ast.walk(function):
        if isinstance(node, ast.If):
            conditions.append(node.test)
        elif isinstance(node, ast.IfExp):
            conditions.append(node.test)
        elif isinstance(node, ast.comprehension):
            conditions.extend(node.ifs)
    return conditions


def primary_source_discipline() -> dict[str, object]:
    _source, tree = source_tree()
    functions = function_definitions(tree)
    compiler_functions = reachable_local_functions(
        functions, "wavefront_controller_word"
    )
    static_condition_names = {
        "_row_applies_at",
        "controls",
        "layout",
        "len",
        "length",
        "needed",
        "row",
        "site",
        "transition_table",
        "value",
        "work",
    }
    branch_rows: list[dict[str, object]] = []
    runtime_branch_references: list[dict[str, object]] = []
    loop_rows: list[dict[str, object]] = []
    runtime_state_calls: list[dict[str, object]] = []
    forbidden_state_calls = {
        "A.apply_semantic",
        "P.C713.apply_sparse_word",
        "_set_row_pattern",
        "_owner_count",
        "_action_values",
    }
    while_rows: list[dict[str, object]] = []
    for function_name in sorted(compiler_functions):
        function = functions[function_name]
        for condition in branch_conditions(function):
            names = sorted({
                node.id for node in ast.walk(condition)
                if isinstance(node, ast.Name)
            })
            unexpected = sorted(set(names) - static_condition_names)
            row = {
                "function": function_name,
                "line": condition.lineno,
                "condition": ast.unparse(condition),
                "referenced_names": names,
                "non_static_names": unexpected,
            }
            branch_rows.append(row)
            if unexpected:
                runtime_branch_references.append(row)
        for node in ast.walk(function):
            if isinstance(node, (ast.For, ast.comprehension)):
                iterator = node.iter
                loop_rows.append({
                    "function": function_name,
                    "line": getattr(node, "lineno", iterator.lineno),
                    "iterator": ast.unparse(iterator),
                })
            elif isinstance(node, ast.While):
                while_rows.append({
                    "function": function_name,
                    "line": node.lineno,
                    "condition": ast.unparse(node.test),
                })
            elif isinstance(node, ast.Call):
                path = call_path(node.func)
                if path in forbidden_state_calls:
                    runtime_state_calls.append({
                        "function": function_name,
                        "line": node.lineno,
                        "call": path,
                    })

    word_function = functions["wavefront_controller_word"]
    stages_function = functions["wavefront_controller_stages"]
    fixed_flattening = bool(
        any(isinstance(node, ast.GeneratorExp) for node in ast.walk(word_function))
        and sum(
            isinstance(node, ast.For)
            for node in ast.walk(stages_function)
        ) >= 4
        and not while_rows
        and not runtime_state_calls
    )

    module_aliases = {
        alias.asname
        for node in tree.body
        if isinstance(node, ast.Import)
        for alias in node.names
        if alias.asname in {"P", "T", "C"}
    }
    attribute_assignments: list[dict[str, object]] = []
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
            if attribute_root(target) in {"P", "T", "C"}:
                attribute_assignments.append({
                    "line": target.lineno,
                    "target": ast.unparse(target),
                })
        if (
            isinstance(node, ast.Call)
            and call_path(node.func) in {"setattr", "delattr"}
            and node.args
            and attribute_root(node.args[0]) in {"P", "T", "C"}
        ):
            attribute_assignments.append({
                "line": node.lineno,
                "target": ast.unparse(node),
            })

    passed = bool(
        compiler_functions == {
            "_and_toggle",
            "_controlled_predicate",
            "_row_applies_at",
            "_row_phase_update_predicate",
            "_row_predicate",
            "_row_stage_word",
            "wavefront_controller_stages",
            "wavefront_controller_word",
        }
        and branch_rows
        and not runtime_branch_references
        and not runtime_state_calls
        and not while_rows
        and fixed_flattening
        and module_aliases == {"P", "T", "C"}
        and not attribute_assignments
        and not (TOP_LEVEL_BLOCKLIST & set(sys.modules))
    )
    return {
        "pass": passed,
        "primary_read_as_data_only": True,
        "compiler_entry": "wavefront_controller_word",
        "runtime_map_functions_checked": sorted(compiler_functions),
        "branch_predicates_checked": branch_rows,
        "branch_predicate_count": len(branch_rows),
        "branch_references_to_nonstatic_or_runtime_names": (
            runtime_branch_references
        ),
        "runtime_state_executor_calls_in_compiler_path": runtime_state_calls,
        "while_loops_in_compiler_path": while_rows,
        "fixed_unrolling_loop_iterators": loop_rows,
        "fixed_generator_flattening_and_unrolling": fixed_flattening,
        "imported_P_T_C_aliases": sorted(module_aliases),
        "attribute_assignments_onto_P_T_C": attribute_assignments,
        "blocked_primary_imports_present": sorted(
            TOP_LEVEL_BLOCKLIST & set(sys.modules)
        ),
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
    table = run_certificate("table_extraction", table_extraction)
    semantics = run_certificate(
        "sandwich_and_fredkin_semantics",
        sandwich_and_fredkin_semantics,
    )
    replay = run_certificate(
        "controller_replay",
        lambda: controller_replay(table),
    )
    surfaces = run_certificate(
        "unchanged_surface_spot",
        unchanged_surface_spot,
    )
    discipline = run_certificate(
        "primary_source_discipline",
        primary_source_discipline,
    )

    blocked_present = sorted(TOP_LEVEL_BLOCKLIST & set(sys.modules))
    passing = bool(
        all(row["pass"] for row in CHECKS)
        and not blocked_present
    )
    runtime = perf_counter() - started
    report = {
        "cycle": 726,
        "status": "PASS" if passing else "FAIL",
        "authority": "none",
        "audit": "unset",
        "audit_timeout_seconds": AUDIT_TIMEOUT_SEC,
        "note_path": NOTE_PATH,
        "audit_input_paths": AUDIT_INPUT_PATHS,
        "declared_input_paths": DECLARED_INPUT_PATHS,
        "primary_read_as_data_only": True,
        "top_level_blocklist": sorted(TOP_LEVEL_BLOCKLIST),
        "blocked_primary_imports_present": blocked_present,
        "checks": CHECKS,
        "check_summary": {
            "passing": sum(bool(row["pass"]) for row in CHECKS),
            "total": len(CHECKS),
        },
        "certificates": {
            "table_extraction": table,
            "sandwich_and_fredkin_semantics": semantics,
            "controller_replay": replay,
            "unchanged_surface_spot": surfaces,
            "primary_source_discipline": discipline,
        },
        "runtime_seconds": runtime,
    }
    report["report_sha256"] = sha256(json.dumps(
        report,
        sort_keys=True,
        separators=(",", ":"),
        default=str,
    ).encode()).hexdigest()
    print(json.dumps(report, indent=2, sort_keys=True, default=str))

    passing_count = report["check_summary"]["passing"]
    total_count = report["check_summary"]["total"]
    print("CHECK_SUMMARY", f"{passing_count}/{total_count}")
    print(
        "TABLE",
        table.get("table_sha256", "<unavailable>"),
        "ROWS",
        table.get("row_count", 0),
    )
    print(
        "FREDKIN_IDENTITY_CENSUS",
        semantics.get("signed_Pauli_identity_cases", 0),
        "FAILURES",
        semantics.get("identity_failures", "<unavailable>"),
    )
    print(
        "REPLAY_CENSUS",
        f"{replay.get('row_output_matches', 0)}/"
        f"{replay.get('declared_lawful_phase_input_rows', 0)}",
        "FULL_STEPS",
        replay.get("full_replay_steps", 0),
        "ACTION_EVENTS",
        replay.get("full_action_events", 0),
    )
    print("RUNTIME_SECONDS", f"{runtime:.6f}")
    print(
        "CYCLE726_WAVEFRONT_INDEPENDENT_CHECK_PASS"
        if passing
        else "CYCLE726_WAVEFRONT_INDEPENDENT_CHECK_FAIL"
    )
    return 0 if passing else 1


if __name__ == "__main__":
    raise SystemExit(main())
