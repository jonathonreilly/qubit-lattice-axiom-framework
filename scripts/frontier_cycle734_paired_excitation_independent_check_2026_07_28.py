#!/usr/bin/env python3
"""Independent bounded checker for the Cycle-734 logical pair template.

Cycle 734 is parsed as inert data and executed only in a child process. The
finite pair algebra, charge recurrence, deletions, current Cycle-731
comparator, and Cycle-724 guard provenance are checked by separate routes.
"""
from __future__ import annotations

import ast
import json
from pathlib import Path
import subprocess
import sys
from time import perf_counter
from typing import Any

import frontier_cycle731_token_count_certificate_2026_07_28 as C731
import frontier_cycle724_local_token_row_enforcement_2026_07_28 as C724
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = (
    "docs/PAIRED_EXCITATION_GENESIS_CYCLE734_BOUNDED_THEOREM_NOTE_2026-07-28.md"
)
SELF_PATH = (
    "scripts/frontier_cycle734_paired_excitation_independent_check_2026_07_28.py"
)
PRIMARY_PATH = (
    "scripts/frontier_cycle734_paired_excitation_genesis_2026_07_28.py"
)
DIRECT_INPUT_PATHS = (
    NOTE_PATH,
    PRIMARY_PATH,
    "docs/RECURRENT_MATTER_HISTORY_CONTROLLER_CYCLE719_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/LOCAL_TOKEN_ROW_ENFORCEMENT_CYCLE724_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "docs/CHARGE_ROW_ENFORCEMENT_CYCLE730_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "docs/TOKEN_COUNT_CERTIFICATE_CYCLE731_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "docs/GENESIS_WORD_SELF_VERIFICATION_CYCLE732_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
AUDIT_INPUT_PATHS = (
    "docs/CHARGE_ROW_ENFORCEMENT_CYCLE730_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "docs/FULL128_LOCAL_M64_SEAM_M2_BARE_FRAME_INTERTWINER_BOUNDED_THEOREM_NOTE_2026-07-24.md",
    "docs/GENESIS_WORD_SELF_VERIFICATION_CYCLE732_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "docs/JOINT_TWO_CELL_FULL_UPDATE_PHYSICAL_M2_COMPILER_CYCLE712_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/LITERAL_PATCHGRAPH_Z3_M2_PLACEMENT_AND_FIXED_CONTROLLER_CYCLE707_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/LOCAL_SEAM_SIGNED_CLIFFORD_PHYSICAL_M2_COMPILER_CYCLE709_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/LOCAL_TOKEN_ROW_ENFORCEMENT_CYCLE724_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "docs/OPENREFERENCE_PATCHGRAPH_FOUR_RAIL_SIGNED_CLIFFORD_EQUIVALENCE_CYCLE706_NOTE_2026-07-26.md",
    "docs/PAIRED_EXCITATION_GENESIS_CYCLE734_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "docs/PHYSICAL_CYCLE704_FSWAP_ENDPOINT_CUBE_BRIDGE_CYCLE708_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/PHYSICAL_M2_ENDPOINT_INSTRUMENT_CYCLE704_CYCLE612_BRIDGE_CYCLE713_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/PHYSICAL_M2_FULL34_FIXED_PACKET_COMPOSITION_CYCLE714_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/PHYSICAL_M2_SPATIAL_ACK_CYCLE612_INTERVAL_BRIDGE_CYCLE718_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/RECURRENT_DIRECTIONAL_PACKET_BANK_CYCLE715_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/RECURRENT_MATTER_HISTORY_CONTROLLER_CYCLE719_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/REFUSAL_WRAPPED_CONTROLLER_CYCLE723_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "docs/TOKEN_COUNT_CERTIFICATE_CYCLE731_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "docs/work_history/repo/review_feedback/CYCLE704_LOCAL_GAUSS_CYCLE612_ENDPOINT_BRIDGE_NOTE_2026-07-25.md",
    "docs/work_history/repo/review_feedback/INFINITE_REVERSIBLE_RECORD_EXPORT_QCA_CYCLE11_NOTE_2026-07-14.md",
    "docs/work_history/repo/review_feedback/PHYSICAL_INTRINSIC_TICK_EVENT_RELATIONAL_DURATION_TOURNAMENT_CYCLE610_NOTE_2026-07-22.md",
    "docs/work_history/repo/review_feedback/PHYSICAL_TICK_ECHO_ASSOCIATION_CAUSAL_ORDER_TOURNAMENT_CYCLE612_NOTE_2026-07-22.md",
    "scripts/ROUTE2_LOCAL_GAUGE_CAR_COMPILER_CYCLE232_2026_07_17.py",
    "scripts/active_cubic_source_response_cycle211_2026_07_16.py",
    "scripts/archive_carrier_source_ledger_cycle227_2026_07_17.py",
    "scripts/autonomous_cubic_field_emission_cycle214_2026_07_16.py",
    "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py",
    "scripts/finite_coin_scalar_wave_dilation_cycle215_2026_07_16.py",
    "scripts/fock_modular_boundary_current_cycle229_2026_07_17.py",
    "scripts/frontier_cycle703_local_gauss_reference_adversary_2026_07_25.py",
    "scripts/frontier_cycle704_local_gauss_cycle612_endpoint_bridge_2026_07_25.py",
    "scripts/frontier_cycle706_openreference_patchgraph_four_rail_equivalence_2026_07_26.py",
    "scripts/frontier_cycle708_cube_basis_gauge_core_2026_07_26.py",
    "scripts/frontier_cycle708_endpoint_cube_tableau_core_2026_07_26.py",
    "scripts/frontier_cycle708_physical_endpoint_cube_core_2026_07_26.py",
    "scripts/frontier_cycle709_local_seam_clifford_2026_07_26.py",
    "scripts/frontier_cycle709_local_seam_clifford_core_2026_07_26.py",
    "scripts/frontier_cycle709_local_seam_physical_core_2026_07_26.py",
    "scripts/frontier_cycle712_joint_two_cell_full_update_independent_check_2026_07_26.py",
    "scripts/frontier_cycle712_joint_two_cell_full_update_physical_m2_2026_07_26.py",
    "scripts/frontier_cycle713_physical_m2_endpoint_instrument_bridge_2026_07_26.py",
    "scripts/frontier_cycle714_fixed_packet_coherent_composition_check_2026_07_26.py",
    "scripts/frontier_cycle714_full34_fixed_packet_independent_route_replay_2026_07_26.py",
    "scripts/frontier_cycle714_full34_fixed_packet_physical_m2_core_2026_07_26.py",
    "scripts/frontier_cycle715_recurrent_directional_packet_bank_2026_07_26.py",
    "scripts/frontier_cycle718_carrier_return_core_2026_07_26.py",
    "scripts/frontier_cycle718_cycle612_interval_bridge_2026_07_26.py",
    "scripts/frontier_cycle718_cycle713_carrier_return_composition_core_2026_07_26.py",
    "scripts/frontier_cycle718_spatial_ack_export_core_2026_07_26.py",
    "scripts/frontier_cycle718_spatial_ack_physical_m2_route_2026_07_26.py",
    "scripts/frontier_cycle718_three_bank_physical_route_core_2026_07_26.py",
    "scripts/frontier_cycle718_token_relative_relay_core_2026_07_26.py",
    "scripts/frontier_cycle719_local_handshake_controller_core_2026_07_26.py",
    "scripts/frontier_cycle719_recurrent_cycle612_bank_core_2026_07_26.py",
    "scripts/frontier_cycle719_recurrent_matter_history_controller_2026_07_26.py",
    "scripts/frontier_cycle719_recurrent_physical_route_core_2026_07_26.py",
    "scripts/frontier_cycle719_source_local_finalizer_core_2026_07_26.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle723_refusal_wrapped_controller_2026_07_28.py",
    "scripts/frontier_cycle724_local_token_row_enforcement_2026_07_28.py",
    "scripts/frontier_cycle728_bksf_holonomy_compression_2026_07_28.py",
    "scripts/frontier_cycle730_charge_row_enforcement_2026_07_28.py",
    "scripts/frontier_cycle731_token_count_certificate_2026_07_28.py",
    "scripts/frontier_cycle732_genesis_independent_check_2026_07_28.py",
    "scripts/frontier_cycle732_genesis_word_self_verification_2026_07_28.py",
    "scripts/frontier_cycle734_paired_excitation_genesis_2026_07_28.py",
    "scripts/frontier_full128_25site_nn_circuit_core_2026_07_24.py",
    "scripts/frontier_full128_bare_frame_pair_cocycle_2026_07_24.py",
    "scripts/frontier_full128_code_projectors_2026_07_24.py",
    "scripts/frontier_full128_cycle_cocycle_intertwiner_2026_07_24.py",
    "scripts/frontier_full128_cycle_encoder_2026_07_24.py",
    "scripts/frontier_full128_two_rail_fixed_law_core_2026_07_24.py",
    "scripts/frontier_literal_patchgraph_cycle656_projected_trace_cycle707_2026_07_26.py",
    "scripts/frontier_literal_patchgraph_z3_m2_placement_core_cycle707_2026_07_26.py",
    "scripts/infinite_reversible_record_export_qca_cycle11_2026_07_14.py",
    "scripts/local_conservative_commit_resource_gravity_cycle9_2026_07_14.py",
    "scripts/local_generator_source_tournament_cycle228_2026_07_17.py",
    "scripts/physical_autonomous_bound_branch_preparation_tournament_cycle611_2026_07_22.py",
    "scripts/physical_autonomous_localized_refocused_matter_transition_tournament_cycle575_2026_07_22.py",
    "scripts/physical_contact_dimer_infinite_internal_content_tournament_cycle583_2026_07_22.py",
    "scripts/physical_intrinsic_contact_bound_moving_transition_tournament_cycle578_2026_07_22.py",
    "scripts/physical_intrinsic_tick_event_relational_duration_tournament_cycle610_2026_07_22.py",
    "scripts/physical_matter_transition_clock_equivalence_tournament_cycle573_2026_07_22.py",
    "scripts/physical_tick_echo_association_causal_order_tournament_cycle612_2026_07_22.py",
    "scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py",
    "scripts/retarded_cubic_mass_field_cycle213_2026_07_16.py",
    "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py",
    "scripts/virtual_exchange_green_kernel_cycle216_2026_07_16.py",
)
REPO_ROOT = Path(__file__).resolve().parents[1]
STDOUT_LIMIT_BYTES = 150 * 1024
EXPECTED_PAIR_TEMPLATE = (
    ("a_base", 0),
    ("a_base", 1),
    ("ref_base", 1),
)
EXPECTED_ADJACENT_CONVENTION = (
    "positive-oriented pair (position, position+1 mod 11), "
    "with reference segment at position+1 and h=0"
)
EXPECTED_DECLARED_LAW = (
    "A_count=2 AND popcount(A) mod 2=h in the B=0,h=0 sector"
)
EXPECTED_COUNT2_CONTROLLER_GATES = 11_206
EXPECTED_COUNT2_CONTROLLER_SHA256 = (
    "3c1316fc5e83112093ed7bca9d61779d4a90a9ba5265fc8d2145b65be6c902a3"
)
EXPECTED_PRIMARY_AUDIT_INPUTS = tuple(
    sorted(
        tuple(
            path for path in AUDIT_INPUT_PATHS if path != PRIMARY_PATH
        )
        + (SELF_PATH,)
    )
)
EXPECTED_REFUSED_COUNTS = (0, 1, 3, 4)
EXPECTED_OBSTRUCTION_NAME = "ownership_uniqueness_at_adjacent_Q_sites"
EXPECTED_OBSTRUCTION_INVARIANT = (
    "an occupied A station requires own B/work and both neighboring "
    "A/B rails blank at the Q boundary"
)
EXPECTED_GUARD_LAYER = (
    "Cycle724 radius-one Q guard inherited by the Cycle731 composition"
)
EXPECTED_MINIMAL_WITNESS = (
    ("ring_stations", 11),
    ("A_count", 2),
    ("A_sites", (0, 1)),
    ("B_count", 0),
    ("work_count", 0),
    ("single_token_control_violations", 0),
)
EXPECTED_REMAINING_SUPPLIED_COMPONENTS = (
    "external application-position parameter",
    "finite oriented geometry",
    "program content/order",
    "passive-only covariance",
)
EXPECTED_CLAIM_SCOPE = (
    "externally positioned translation-covariant logical pair template, "
    "static charge rows, and A-count-two comparator-prefix behavior on the "
    "supplied ring-11 fixture; plus one inherited Cycle724/Cycle731 "
    "adjacent-guard witness"
)
EXPECTED_PRIMARY_CHECKS = (
    "A_Cycle732_regression_anchor",
    "B_pair_word_exactness",
    "C_translation_covariance",
    "D_count2_enforcement",
    "E_supplied_position_template_audit",
    "F_inherited_guard_and_bare_transport_probe",
    "G_pair_word_deletion_controls",
    "H_honest_boundary_keys",
    "I_recursive_input_and_paired_runner_closure",
    "OUTPUT_stdout_under_150KB",
)
BLOCKLISTED_CYCLES = (734,)
K_ATTRIBUTE_BASELINE = tuple(
    sorted((name, id(value)) for name, value in vars(K).items())
)


def declared_input_closure(
    direct_paths: tuple[str, ...],
) -> tuple[str, ...]:
    """Recover recursive literal input declarations, excluding this runner."""

    seen: set[str] = set()
    pending = list(direct_paths)
    while pending:
        relative = pending.pop()
        if relative == SELF_PATH or relative in seen:
            continue
        path = REPO_ROOT / relative
        if not path.is_file():
            raise FileNotFoundError(relative)
        seen.add(relative)
        if not (relative.startswith("scripts/") and relative.endswith(".py")):
            continue
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        nested: tuple[str, ...] = ()
        for node in tree.body:
            if not isinstance(node, (ast.Assign, ast.AnnAssign)):
                continue
            targets = (
                node.targets if isinstance(node, ast.Assign) else (node.target,)
            )
            if not any(
                isinstance(target, ast.Name)
                and target.id == "AUDIT_INPUT_PATHS"
                for target in targets
            ):
                continue
            value = ast.literal_eval(node.value)
            if (
                not isinstance(value, (tuple, list))
                or not value
                or not all(isinstance(item, str) for item in value)
            ):
                raise ValueError(("invalid AUDIT_INPUT_PATHS", relative))
            nested = tuple(value)
            break
        pending.extend(nested)
    return tuple(sorted(seen))


def input_contract_certificate() -> dict[str, object]:
    recovered = declared_input_closure(DIRECT_INPUT_PATHS)
    required_parent_notes = (
        "docs/RECURRENT_MATTER_HISTORY_CONTROLLER_CYCLE719_BOUNDED_THEOREM_NOTE_2026-07-26.md",
        "docs/LOCAL_TOKEN_ROW_ENFORCEMENT_CYCLE724_BOUNDED_THEOREM_NOTE_2026-07-28.md",
        "docs/CHARGE_ROW_ENFORCEMENT_CYCLE730_BOUNDED_THEOREM_NOTE_2026-07-28.md",
        "docs/TOKEN_COUNT_CERTIFICATE_CYCLE731_BOUNDED_THEOREM_NOTE_2026-07-28.md",
        "docs/GENESIS_WORD_SELF_VERIFICATION_CYCLE732_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    )
    missing_rejected = False
    try:
        declared_input_closure(
            DIRECT_INPUT_PATHS
            + ("scripts/__cycle734_independent_missing_control__.py",)
        )
    except FileNotFoundError:
        missing_rejected = True
    all_exist = all(
        (REPO_ROOT / path).is_file() for path in AUDIT_INPUT_PATHS
    )
    parent_notes_present = all(
        path in recovered for path in required_parent_notes
    )
    return {
        "declared_count": len(AUDIT_INPUT_PATHS),
        "recovered_count": len(recovered),
        "exact_recursive_closure": recovered == AUDIT_INPUT_PATHS,
        "all_exist": all_exist,
        "note_in_closure": NOTE_PATH in recovered,
        "primary_in_closure": PRIMARY_PATH in recovered,
        "all_parent_notes_in_closure": parent_notes_present,
        "primary_declares_paired_runner":
            SELF_PATH in EXPECTED_PRIMARY_AUDIT_INPUTS,
        "missing_path_rejected": missing_rejected,
        "pass": (
            recovered == AUDIT_INPUT_PATHS
            and all_exist
            and NOTE_PATH in recovered
            and PRIMARY_PATH in recovered
            and parent_notes_present
            and SELF_PATH in EXPECTED_PRIMARY_AUDIT_INPUTS
            and missing_rejected
        ),
    }


def primary_liveness_certificate() -> dict[str, object]:
    """Require current-parent primary execution and its complete check schema."""

    completed = subprocess.run(
        (sys.executable, PRIMARY_PATH),
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        timeout=AUDIT_TIMEOUT_SEC,
        check=False,
    )
    stdout_lines = tuple(
        line for line in completed.stdout.splitlines() if line.strip()
    )
    if not stdout_lines:
        raise AssertionError(("primary emitted no stdout", completed.stderr))
    report = json.loads(stdout_lines[-1])
    checks = report.get("checks")
    if not isinstance(checks, dict):
        raise AssertionError("primary report has no checks object")
    boundary = report.get("honest_boundary")
    if not isinstance(boundary, dict):
        raise AssertionError("primary report has no honest boundary")
    observed_checks = tuple(sorted(checks))
    expected_checks = tuple(sorted(EXPECTED_PRIMARY_CHECKS))
    return {
        "returncode": completed.returncode,
        "stderr": completed.stderr,
        "observed_check_names": observed_checks,
        "expected_check_names": expected_checks,
        "checks_passed": sum(bool(value) for value in checks.values()),
        "checks_total": len(checks),
        "primary_report_pass": report.get("pass"),
        "no_hardcoded_absolute_site_in_template":
            boundary.get("no_hardcoded_absolute_site_in_template"),
        "source_selection_remains_supplied":
            boundary.get("source_selection_remains_supplied"),
        "generalized_controller_no_go_claimed":
            boundary.get("generalized_controller_no_go_claimed"),
        "pass": (
            completed.returncode == 0
            and not completed.stderr
            and report.get("pass") is True
            and observed_checks == expected_checks
            and all(value is True for value in checks.values())
            and boundary.get("no_hardcoded_absolute_site_in_template")
            is True
            and boundary.get("source_selection_remains_supplied") is True
            and boundary.get("generalized_controller_no_go_claimed")
            is False
        ),
    }


def _function(tree: ast.Module, name: str) -> ast.FunctionDef:
    matches = [
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    if len(matches) != 1:
        raise AssertionError(("function census", name, len(matches)))
    return matches[0]


def _assignment_value(scope: ast.Module | ast.FunctionDef, name: str) -> ast.expr:
    matches: list[ast.expr] = []
    for node in scope.body:
        if isinstance(node, ast.Assign):
            if any(
                isinstance(target, ast.Name) and target.id == name
                for target in node.targets
            ):
                matches.append(node.value)
        elif (
            isinstance(node, ast.AnnAssign)
            and isinstance(node.target, ast.Name)
            and node.target.id == name
            and node.value is not None
        ):
            matches.append(node.value)
    if len(matches) != 1:
        raise AssertionError(("assignment census", name, len(matches)))
    return matches[0]


def _return_dict(function: ast.FunctionDef) -> ast.Dict:
    matches = [
        node.value
        for node in function.body
        if isinstance(node, ast.Return) and isinstance(node.value, ast.Dict)
    ]
    if len(matches) != 1:
        raise AssertionError(("return dict census", function.name, len(matches)))
    return matches[0]


def _dict_items(node: ast.Dict) -> dict[str, ast.expr]:
    output: dict[str, ast.expr] = {}
    for key_node, value_node in zip(node.keys, node.values):
        if key_node is None:
            raise AssertionError("dictionary unpacking is outside the audit grammar")
        key = ast.literal_eval(key_node)
        if not isinstance(key, str) or key in output:
            raise AssertionError(("non-string or duplicate dictionary key", key))
        output[key] = value_node
    return output


def _qualified_name(node: ast.expr) -> str:
    parts: list[str] = []
    while isinstance(node, ast.Attribute):
        parts.append(node.attr)
        node = node.value
    if not isinstance(node, ast.Name):
        raise AssertionError("non-name attribute root")
    parts.append(node.id)
    return ".".join(reversed(parts))


def _layout_key(node: ast.expr) -> str:
    if not (
        isinstance(node, ast.Subscript)
        and isinstance(node.value, ast.Name)
        and node.value.id == "layout"
    ):
        raise AssertionError(("not a layout subscript", ast.dump(node)))
    key = ast.literal_eval(node.slice)
    if not isinstance(key, str):
        raise AssertionError(("non-string layout key", key))
    return key


def _position_offset(node: ast.expr) -> int:
    if not (
        isinstance(node, ast.BinOp)
        and isinstance(node.op, ast.Mod)
        and isinstance(node.right, ast.Name)
        and node.right.id == "stations"
    ):
        raise AssertionError(("non-modular position expression", ast.dump(node)))
    numerator = node.left
    if isinstance(numerator, ast.Name) and numerator.id == "position":
        return 0
    if (
        isinstance(numerator, ast.BinOp)
        and isinstance(numerator.op, ast.Add)
        and isinstance(numerator.left, ast.Name)
        and numerator.left.id == "position"
    ):
        offset = ast.literal_eval(numerator.right)
        if isinstance(offset, int) and not isinstance(offset, bool):
            return offset
    raise AssertionError(("unsupported position numerator", ast.dump(numerator)))


def _extract_pair_template(function: ast.FunctionDef) -> tuple[tuple[str, int], ...]:
    returns = [
        node
        for node in function.body
        if isinstance(node, ast.Return) and isinstance(node.value, ast.Tuple)
    ]
    if len(returns) != 1:
        raise AssertionError(("pair return census", len(returns)))
    descriptors: list[tuple[str, int]] = []
    for gate in returns[0].value.elts:
        if not (
            isinstance(gate, ast.Call)
            and _qualified_name(gate.func) == "K.A.x"
            and len(gate.args) == 1
            and not gate.keywords
        ):
            raise AssertionError(("pair gate is not a unary K.A.x", ast.dump(gate)))
        wire = gate.args[0]
        if not (
            isinstance(wire, ast.BinOp)
            and isinstance(wire.op, ast.Add)
        ):
            raise AssertionError(("pair wire grammar", ast.dump(wire)))
        descriptors.append((_layout_key(wire.left), _position_offset(wire.right)))
    return tuple(descriptors)


def _static_int(node: ast.expr, names: dict[str, int]) -> int:
    if (
        isinstance(node, ast.Constant)
        and isinstance(node.value, int)
        and not isinstance(node.value, bool)
    ):
        return node.value
    if isinstance(node, ast.Name) and node.id in names:
        return names[node.id]
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Pow):
        return _static_int(node.left, names) ** _static_int(node.right, names)
    raise AssertionError(("unsupported static integer expression", ast.dump(node)))


def _subscript_path(node: ast.expr) -> tuple[str, tuple[str, ...]] | None:
    keys: list[str] = []
    while isinstance(node, ast.Subscript):
        try:
            key = ast.literal_eval(node.slice)
        except (ValueError, TypeError):
            return None
        if not isinstance(key, str):
            return None
        keys.append(key)
        node = node.value
    if not isinstance(node, ast.Name):
        return None
    return node.id, tuple(reversed(keys))


def _comparison_literals(
    expression: ast.expr, root: str
) -> dict[tuple[str, ...], object]:
    output: dict[tuple[str, ...], object] = {}
    for node in ast.walk(expression):
        if not (
            isinstance(node, ast.Compare)
            and len(node.ops) == 1
            and len(node.comparators) == 1
        ):
            continue
        path = _subscript_path(node.left)
        if path is None or path[0] != root:
            continue
        try:
            value = ast.literal_eval(node.comparators[0])
        except (ValueError, TypeError):
            continue
        output[path[1]] = value
    return output


def extraction() -> tuple[dict[str, object], dict[str, object]]:
    """Extract only inert syntax/data from Cycle 734; never import it."""

    source = Path(PRIMARY_PATH).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=PRIMARY_PATH)
    module_literals = {
        name: ast.literal_eval(_assignment_value(tree, name))
        for name in (
            "AUDIT_INPUT_PATHS",
            "RING_STATIONS",
            "EXPECTED_COUNT",
            "EXPECTED_PAIR_GATES",
            "FIXTURE_BANKS",
        )
    }
    ring = module_literals["RING_STATIONS"]
    if not isinstance(ring, int) or isinstance(ring, bool):
        raise AssertionError(("non-integer ring census", ring))

    pair_function = _function(tree, "pair_creation_word")
    pair_template = _extract_pair_template(pair_function)
    pair_exactness_items = _dict_items(
        _return_dict(_function(tree, "pair_word_exactness_certificate"))
    )
    adjacent_convention = ast.literal_eval(
        pair_exactness_items["adjacent_pair_convention"]
    )

    covariance_items = _dict_items(
        _return_dict(_function(tree, "translation_covariance_certificate"))
    )
    covariance_count = _static_int(
        covariance_items["expected_identities"],
        {"RING_STATIONS": ring},
    )

    count_function = _function(tree, "count2_enforcement_certificate")
    refused_counts = ast.literal_eval(
        _assignment_value(count_function, "witness_counts")
    )
    count_return_items = _dict_items(_return_dict(count_function))
    accepted_key_present = (
        "all_11_templates_count_prefix_accepted" in count_return_items
    )
    refused_key_present = (
        "all_0_1_3_4_count_witnesses_refused" in count_return_items
    )
    law_items = _dict_items(
        _return_dict(_function(tree, "h0_b0_theorem_recount"))
    )
    declared_law = ast.literal_eval(
        law_items["static_count_and_charge_law"]
    )
    exhaustive_count2 = ast.literal_eval(
        law_items["expected_static_count2_and_charge_pass_cases"]
    )

    controller_function = _function(tree, "controller_two_token_probe")
    witness_node = _assignment_value(controller_function, "guard_witness")
    if not isinstance(witness_node, ast.Dict):
        raise AssertionError("guard witness is not a dictionary literal")
    witness_items = _dict_items(witness_node)
    obstruction_name = ast.literal_eval(witness_items["name"])
    obstruction_invariant = ast.literal_eval(witness_items["invariant"])
    guard_layer = ast.literal_eval(witness_items["guard_layer"])
    minimal_node = witness_items["minimal_reproducing_census"]
    if not isinstance(minimal_node, ast.Dict):
        raise AssertionError("minimal witness is not a dictionary literal")
    minimal_items = _dict_items(minimal_node)
    exact_comparisons = _comparison_literals(
        _assignment_value(controller_function, "guard_witness_exact"),
        "guard_witness",
    )
    first_step = exact_comparisons[("first_step",)]
    first_stations = exact_comparisons[("first_stations",)]
    minimal_witness = (
        ("ring_stations", ring),
        (
            "A_count",
            exact_comparisons[("minimal_reproducing_census", "A_count")],
        ),
        (
            "A_sites",
            exact_comparisons[("minimal_reproducing_census", "A_sites")],
        ),
        (
            "B_count",
            exact_comparisons[("minimal_reproducing_census", "B_count")],
        ),
        ("work_count", ast.literal_eval(minimal_items["work_count"])),
        (
            "single_token_control_violations",
            exact_comparisons[
                (
                    "minimal_reproducing_census",
                    "single_token_control_violations",
                )
            ],
        ),
    )
    controller_return = _dict_items(_return_dict(controller_function))
    adjacent_macro_key_present = (
        "adjacent_data_macros_executed" in controller_return
    )

    main_function = _function(tree, "main")
    remaining_supplied = tuple(
        ast.literal_eval(
            _assignment_value(
                main_function, "remaining_supplied_components"
            )
        )
    )
    boundary_node = _assignment_value(main_function, "boundary")
    if not isinstance(boundary_node, ast.Dict):
        raise AssertionError("boundary is not a dictionary literal")
    boundary_items = _dict_items(boundary_node)
    claim_scope = ast.literal_eval(boundary_items["claim_scope"])
    guard_boundary_node = _assignment_value(
        main_function, "guard_boundary"
    )
    if not isinstance(guard_boundary_node, ast.Dict):
        raise AssertionError("guard boundary is not a dictionary literal")
    guard_boundary_items = _dict_items(guard_boundary_node)
    boundary_keys_present = all(
        key in boundary_items
        for key in (
            "no_hardcoded_absolute_site_in_template",
            "source_selection_remains_supplied",
            "guard_observation",
            "generalized_controller_no_go_claimed",
        )
    )
    no_go_literal = ast.literal_eval(
        boundary_items["generalized_controller_no_go_claimed"]
    )

    public = {
        "pair_template": pair_template,
        "adjacent_pair_convention": adjacent_convention,
        "covariance_identity_census": covariance_count,
        "accepted_adjacent_pair_census": ring if accepted_key_present else -1,
        "refused_count_census": refused_counts,
        "declared_count_parity_law": declared_law,
        "exhaustive_count2_census": exhaustive_count2,
        "obstruction_name": obstruction_name,
        "obstruction_invariant": obstruction_invariant,
        "guard_layer": guard_layer,
        "first_step": first_step,
        "first_stations": first_stations,
        "minimal_witness": minimal_witness,
        "boundary_keys_present": boundary_keys_present,
        "generalized_controller_no_go_claimed": no_go_literal,
        "remaining_supplied_components": remaining_supplied,
        "claim_scope": claim_scope,
        "genesis_AUDIT_INPUT_PATHS_literal": module_literals[
            "AUDIT_INPUT_PATHS"
        ],
    }
    passed = (
        module_literals["AUDIT_INPUT_PATHS"]
        == EXPECTED_PRIMARY_AUDIT_INPUTS
        and module_literals["EXPECTED_COUNT"] == 2
        and module_literals["EXPECTED_PAIR_GATES"] == 3
        and module_literals["FIXTURE_BANKS"] == 2
        and pair_template == EXPECTED_PAIR_TEMPLATE
        and adjacent_convention == EXPECTED_ADJACENT_CONVENTION
        and covariance_count == 121
        and public["accepted_adjacent_pair_census"] == 11
        and refused_key_present
        and refused_counts == EXPECTED_REFUSED_COUNTS
        and declared_law == EXPECTED_DECLARED_LAW
        and exhaustive_count2 == 55
        and obstruction_name == EXPECTED_OBSTRUCTION_NAME
        and obstruction_invariant == EXPECTED_OBSTRUCTION_INVARIANT
        and guard_layer == EXPECTED_GUARD_LAYER
        and first_step == 0
        and first_stations == (0, 1)
        and minimal_witness == EXPECTED_MINIMAL_WITNESS
        and adjacent_macro_key_present
        and boundary_keys_present
        and no_go_literal is False
        and "adjacent_data_macros_executed" in guard_boundary_items
        and "inherited_guard_witness" in guard_boundary_items
        and remaining_supplied
        == EXPECTED_REMAINING_SUPPLIED_COMPONENTS
        and claim_scope == EXPECTED_CLAIM_SCOPE
    )
    public["pass"] = passed
    internal = {
        "ring_stations": ring,
        "expected_count": module_literals["EXPECTED_COUNT"],
        "fixture_banks": module_literals["FIXTURE_BANKS"],
        "pair_template": pair_template,
        "refused_counts": refused_counts,
        "obstruction_name": obstruction_name,
        "obstruction_invariant": obstruction_invariant,
        "guard_layer": guard_layer,
        "first_step": first_step,
        "first_stations": first_stations,
        "minimal_witness": minimal_witness,
        "remaining_supplied_components": remaining_supplied,
        "claim_scope": claim_scope,
    }
    return public, internal


def _pair_word(
    template: tuple[tuple[str, int], ...],
    layout: dict[str, int],
    position: int,
) -> tuple[tuple[str, int], ...]:
    stations = layout["stations"]
    return tuple(
        ("X", layout[base] + ((position + offset) % stations))
        for base, offset in template
    )


def _apply_x_word(value: int, word: tuple[tuple[str, int], ...]) -> int:
    output = value
    for kind, wire in word:
        if kind != "X" or wire < 0:
            raise AssertionError(("unsupported independent gate", kind, wire))
        output ^= 1 << wire
    return output


def _translate_wire(wire: int, layout: dict[str, int], shift: int) -> int:
    stations = layout["stations"]
    for base_name in ("a_base", "b_base", "ref_base"):
        base = layout[base_name]
        if base <= wire < base + stations:
            return base + ((wire - base + shift) % stations)
    return wire


def pair_word_recount(extracted: dict[str, object]) -> dict[str, object]:
    """Independent integer-bit simulator and all 121 covariance identities."""

    stations = int(extracted["ring_stations"])
    template = extracted["pair_template"]
    if not isinstance(template, tuple):
        raise AssertionError("extracted pair template is not a literal tuple")
    layout = {
        "stations": stations,
        "a_base": 0,
        "b_base": stations,
        "ref_base": 2 * stations,
        "h_wire": 3 * stations,
    }
    exact_failures: list[int] = []
    outputs: list[int] = []
    for position in range(stations):
        word = _pair_word(template, layout, position)
        output = _apply_x_word(0, word)
        following = (position + 1) % stations
        expected = (
            (1 << (layout["a_base"] + position))
            | (1 << (layout["a_base"] + following))
            | (1 << (layout["ref_base"] + following))
        )
        mask = (1 << stations) - 1
        a_mask = (output >> layout["a_base"]) & mask
        b_mask = (output >> layout["b_base"]) & mask
        refs_mask = (output >> layout["ref_base"]) & mask
        h = (output >> layout["h_wire"]) & 1
        exact = (
            output == expected
            and a_mask.bit_count() == 2
            and b_mask == 0
            and refs_mask == 1 << following
            and h == 0
        )
        if not exact:
            exact_failures.append(position)
        outputs.append(output)

    covariance_failures: list[tuple[int, int]] = []
    covariance_count = 0
    for position in range(stations):
        source = _pair_word(template, layout, position)
        for shift in range(stations):
            conjugated = tuple(
                (kind, _translate_wire(wire, layout, shift))
                for kind, wire in source
            )
            target = _pair_word(
                template, layout, (position + shift) % stations
            )
            covariance_count += 1
            if conjugated != target:
                covariance_failures.append((position, shift))
    base = _pair_word(template, layout, 0)
    position0_failures = tuple(
        position
        for position in range(stations)
        if tuple(
            (kind, _translate_wire(wire, layout, position))
            for kind, wire in base
        )
        != _pair_word(template, layout, position)
    )
    return {
        "positions_recounted": stations,
        "bit_exact_outputs": len(outputs) - len(exact_failures),
        "bit_exact_failure_positions": tuple(exact_failures),
        "covariance_identities_recounted": covariance_count,
        "covariance_failures": tuple(covariance_failures),
        "position0_conjugation_failures": position0_failures,
        "pass": (
            len(outputs) == 11
            and not exact_failures
            and covariance_count == 121
            and covariance_count
            == int(extracted["ring_stations"]) ** 2
            and not covariance_failures
            and not position0_failures
        ),
    }


def _declared_count_parity_law(
    a_mask: int, b_mask: int, h: int, expected_count: int
) -> tuple[bool, bool, bool]:
    if b_mask != 0 or h not in (0, 1):
        return False, False, False
    count_ok = a_mask.bit_count() == expected_count
    parity_ok = a_mask.bit_count() % 2 == h
    return count_ok, parity_ok, count_ok and parity_ok


def _reference_from_charge_recurrence(
    a_mask: int, h: int, stations: int
) -> int | None:
    """Solve r_(s+1)=r_s xor A_s xor h*[s=0] with r_0 fixed to zero."""

    current = 0
    refs = 0
    for station in range(stations):
        refs |= current << station
        following = (
            current
            ^ ((a_mask >> station) & 1)
            ^ (h if station == 0 else 0)
        )
        if station == stations - 1:
            return refs if following == 0 else None
        current = following
    raise AssertionError("unreachable recurrence exit")


def count2_law_recount(extracted: dict[str, object]) -> dict[str, object]:
    """Recount static charge algebra and the actual current comparator prefix."""

    stations = int(extracted["ring_stations"])
    expected_count = int(extracted["expected_count"])
    adjacent_rows = []
    for position in range(stations):
        mask = (1 << position) | (1 << ((position + 1) % stations))
        count_ok, parity_ok, lawful = _declared_count_parity_law(
            mask, 0, 0, expected_count
        )
        adjacent_rows.append(
            (position, mask.bit_count(), count_ok, parity_ok, lawful)
        )

    refused_rows = []
    refused_counts = extracted["refused_counts"]
    if not isinstance(refused_counts, tuple):
        raise AssertionError("refusal census is not a literal tuple")
    for count in refused_counts:
        mask = (1 << int(count)) - 1
        h = int(count) & 1
        count_ok, parity_ok, lawful = _declared_count_parity_law(
            mask, 0, h, expected_count
        )
        refused_rows.append(
            (int(count), h, count_ok, parity_ok, not lawful)
        )

    exhaustive_lawful = tuple(
        mask
        for mask in range(1 << stations)
        if _declared_count_parity_law(
            mask, 0, 0, expected_count
        )[2]
    )
    accepted = tuple(row[0] for row in adjacent_rows if row[-1])
    refused = tuple(row[0] for row in refused_rows if row[-1])

    charge_pass = 0
    recurrence_failures = 0
    charge_equivalence_failures = 0
    ring_mask = (1 << stations) - 1
    for a_mask in range(1 << stations):
        refs = _reference_from_charge_recurrence(a_mask, 0, stations)
        charge_ok = refs is not None
        charge_pass += charge_ok
        charge_equivalence_failures += (
            charge_ok != (a_mask.bit_count() % 2 == 0)
        )
        if refs is not None:
            next_refs = (refs >> 1) | ((refs & 1) << (stations - 1))
            recurrence_failures += (
                (a_mask ^ refs ^ next_refs) & ring_mask
            ) != 0

    program = K.interleaved_program(int(extracted["fixture_banks"]))
    word, layout, _blocks, metadata = (
        C731.count_certified_controller_build(
            program, C731.DATA_WIDTH, expected_count
        )
    )
    prefix = word[:int(metadata["comparison_compute_stop"])]
    sources = tuple(
        a_mask << int(layout["a_base"])
        for a_mask in range(1 << stations)
    )
    compared = C731.literal_apply(
        sources, prefix, int(layout["full_width"]), 1
    )
    actual_acceptances = 0
    actual_mismatches = []
    for a_mask, value in enumerate(compared):
        rows = C731.controller_rows(value, layout)
        counter = sum(
            int(bit) << index
            for index, bit in enumerate(rows["counter"])
        )
        observed = counter == expected_count and rows["refusal_latch"] == 0
        expected = a_mask.bit_count() == expected_count
        actual_acceptances += observed
        if observed != expected or counter != a_mask.bit_count():
            actual_mismatches.append(a_mask)

    return {
        "declared_form": EXPECTED_DECLARED_LAW,
        "expected_count": expected_count,
        "adjacent_acceptance_rows": tuple(adjacent_rows),
        "accepted_positions": accepted,
        "refusal_rows": tuple(refused_rows),
        "refused_counts": refused,
        "exhaustive_B0_h0_count2_cases": len(exhaustive_lawful),
        "manual_charge_pass_cases": charge_pass,
        "manual_charge_equivalence_failures":
            charge_equivalence_failures,
        "manual_charge_recurrence_failures": recurrence_failures,
        "actual_parent_comparator_gates": len(word),
        "actual_parent_comparator_sha256": K.gate_digest(word),
        "actual_parent_prefix_acceptances": actual_acceptances,
        "actual_parent_prefix_mismatches": tuple(actual_mismatches),
        "pass": (
            extracted["ring_stations"] == 11
            and expected_count == 2
            and accepted == tuple(range(11))
            and refused == EXPECTED_REFUSED_COUNTS
            and all(row[3] for row in refused_rows)
            and len(exhaustive_lawful) == 55
            and charge_pass == 1_024
            and charge_equivalence_failures == 0
            and recurrence_failures == 0
            and len(word) == EXPECTED_COUNT2_CONTROLLER_GATES
            and K.gate_digest(word)
            == EXPECTED_COUNT2_CONTROLLER_SHA256
            and actual_acceptances == 55
            and not actual_mismatches
        ),
    }


def deletion_control_recount(
    extracted: dict[str, object],
) -> dict[str, object]:
    """Independently reconstruct and test all 33 one-X deletions."""

    stations = int(extracted["ring_stations"])
    expected_count = int(extracted["expected_count"])
    template = extracted["pair_template"]
    if not isinstance(template, tuple):
        raise AssertionError("pair template is not a literal tuple")
    program = K.interleaved_program(int(extracted["fixture_banks"]))
    word, layout, _blocks, metadata = (
        C731.count_certified_controller_build(
            program, C731.DATA_WIDTH, expected_count
        )
    )
    prefix = word[:int(metadata["comparison_compute_stop"])]
    damaged_values = []
    case_rows = []
    for position in range(stations):
        full_word = _pair_word(template, layout, position)
        full_value = _apply_x_word(0, full_word)
        for deleted_index in range(len(full_word)):
            damaged_word = (
                full_word[:deleted_index]
                + full_word[deleted_index + 1:]
            )
            damaged = _apply_x_word(0, damaged_word)
            mask = (1 << stations) - 1
            a_mask = (damaged >> int(layout["a_base"])) & mask
            refs_mask = (damaged >> int(layout["ref_base"])) & mask
            next_refs = (
                (refs_mask >> 1)
                | ((refs_mask & 1) << (stations - 1))
            )
            charge_ok = ((a_mask ^ refs_mask ^ next_refs) & mask) == 0
            static_ok = (
                a_mask.bit_count() == expected_count
                and a_mask.bit_count() % 2 == 0
                and charge_ok
            )
            damaged_values.append(damaged)
            case_rows.append(
                {
                    "position": position,
                    "deleted_index": deleted_index,
                    "output_changed": damaged != full_value,
                    "static_count_and_charge_rejected": not static_ok,
                }
            )
    compared = C731.literal_apply(
        tuple(damaged_values), prefix, int(layout["full_width"]), 1
    )
    count_refusals = 0
    for case, value in zip(case_rows, compared):
        rows = C731.controller_rows(value, layout)
        case["count_prefix_refused"] = rows["refusal_latch"] == 1
        count_refusals += case["count_prefix_refused"]
    return {
        "cases": len(case_rows),
        "output_changes": sum(row["output_changed"] for row in case_rows),
        "static_count_and_charge_refusals":
            sum(row["static_count_and_charge_rejected"] for row in case_rows),
        "count_prefix_refusals": count_refusals,
        "case_rows": tuple(case_rows),
        "pass": (
            len(case_rows) == 33
            and all(row["output_changed"] for row in case_rows)
            and all(
                row["static_count_and_charge_rejected"]
                for row in case_rows
            )
            and count_refusals == 22
        ),
    }


def _occupied(bits: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(index for index, bit in enumerate(bits) if bit)


def _ownership_violations(
    a: tuple[int, ...],
    b: tuple[int, ...],
    work: tuple[int, ...],
) -> tuple[tuple[int, tuple[str, ...]], ...]:
    if not (len(a) == len(b) == len(work)):
        raise AssertionError("rail-length disagreement")
    stations = len(a)
    failures = []
    for station, occupied in enumerate(a):
        if not occupied:
            continue
        left = (station - 1) % stations
        right = (station + 1) % stations
        dirty = (
            ("own_B", b[station]),
            ("own_work", work[station]),
            ("left_A", a[left]),
            ("left_B", b[left]),
            ("right_A", a[right]),
            ("right_B", b[right]),
        )
        reasons = tuple(name for name, bit in dirty if bit)
        if reasons:
            failures.append((station, reasons))
    return tuple(failures)


def guard_witness_reproduction(
    extracted: dict[str, object],
) -> dict[str, object]:
    """Separate bare Cycle 719 from the inherited Cycle-724/731 guard."""

    stations = int(extracted["ring_stations"])
    program = K.interleaved_program(int(extracted["fixture_banks"]))
    banks, links = K.B.chain_genesis(int(extracted["fixture_banks"]))
    data = K.M.prepare_endpoint(K.M.pack_state(banks, links), (1, 0))
    a = (1, 1) + (0,) * (stations - 2)
    b = (0,) * stations
    work = (0,) * stations

    step0_violations = _ownership_violations(a, b, work)
    step0_cycle724_dirty = tuple(
        station
        for station, occupied in enumerate(a)
        if occupied and C724.local_dirty(a, b, work, station)
    )
    step_data, step_a, step_b = K.apply_controller_step(
        data, program, a, b
    )
    orbit_data, orbit_a, orbit_b, orbit_trace = K.run_orbit(
        data, program, token_positions=(0, 1)
    )

    control_rows = []
    for position in (0, 1):
        single_a = tuple(
            int(index == position) for index in range(stations)
        )
        control_rows.append(
            (position, _ownership_violations(single_a, b, work))
        )
    control_violation_count = sum(
        len(violations) for _, violations in control_rows
    )
    cycle724_singleton_dirty = sum(
        C724.local_dirty(
            tuple(int(index == position) for index in range(stations)),
            b,
            work,
            position,
        )
        for position in range(stations)
    )
    observed_witness = (
        ("ring_stations", len(program)),
        ("A_count", sum(a)),
        ("A_sites", _occupied(a)),
        ("B_count", sum(b)),
        ("work_count", sum(work)),
        ("single_token_control_violations", control_violation_count),
    )
    observed_stations = tuple(row[0] for row in step0_violations)
    expected_reasons = (
        (0, ("right_A",)),
        (1, ("left_A",)),
    )
    first_trace = orbit_trace[0] if orbit_trace else None

    count_word, layout, _blocks, _metadata = (
        C731.count_certified_controller_build(
            program, C731.DATA_WIDTH, int(extracted["expected_count"])
        )
    )
    data_value = sum(int(bit) << index for index, bit in enumerate(data))
    refs = tuple(int(station == 1) for station in range(stations))
    source = C731.controller_full_input(
        data_value, layout, a=(0, 1), refs=refs, h=0
    )
    guarded_output = C731.literal_apply(
        (source,), count_word, int(layout["full_width"]), 1
    )[0]
    guarded_rows = C731.controller_rows(guarded_output, layout)
    guarded_data_suppressed = guarded_rows["data"] == data_value
    guarded_aux_clean = C731.all_auxiliary_clean(guarded_rows)

    return {
        "name": extracted["obstruction_name"],
        "guard_layer": extracted["guard_layer"],
        "invariant": extracted["obstruction_invariant"],
        "first_step": 0,
        "first_stations": observed_stations,
        "violation_reasons": step0_violations,
        "minimal_witness": observed_witness,
        "single_token_controls": tuple(control_rows),
        "singleton_controls_clean":
            control_violation_count == cycle724_singleton_dirty == 0,
        "Cycle724_step0_dirty_occupied_sites": step0_cycle724_dirty,
        "Cycle724_manual_recount_agrees":
            step0_cycle724_dirty == observed_stations,
        "K_program_stations": len(program),
        "K_step_A_after": _occupied(step_a),
        "K_step_B_after": _occupied(step_b),
        "K_orbit_first_trace": first_trace,
        "K_direct_step_matches_orbit_first_step": (
            first_trace == ((0, 1), (1, 2), 0)
            and _occupied(step_a) == first_trace[1]
            and sum(step_b) == first_trace[2]
        ),
        "K_orbit_token_return": (
            _occupied(orbit_a) == (0, 1) and not any(orbit_b)
        ),
        "K_public_outputs_were_computed": (
            isinstance(step_data, tuple) and isinstance(orbit_data, tuple)
        ),
        "Cycle731_guarded_data_macros_suppressed":
            guarded_data_suppressed,
        "Cycle731_guarded_A_after": _occupied(guarded_rows["A"]),
        "Cycle731_guarded_B_after": _occupied(guarded_rows["B"]),
        "Cycle731_guarded_auxiliaries_clean": guarded_aux_clean,
        "pass": (
            len(program) == stations == 11
            and extracted["obstruction_name"] == EXPECTED_OBSTRUCTION_NAME
            and extracted["guard_layer"] == EXPECTED_GUARD_LAYER
            and extracted["obstruction_invariant"]
            == EXPECTED_OBSTRUCTION_INVARIANT
            and extracted["first_step"] == 0
            and extracted["first_stations"] == (0, 1)
            and observed_stations == (0, 1)
            and step0_violations == expected_reasons
            and step0_cycle724_dirty == (0, 1)
            and observed_witness == EXPECTED_MINIMAL_WITNESS
            and observed_witness == extracted["minimal_witness"]
            and control_violation_count == 0
            and cycle724_singleton_dirty == 0
            and first_trace == ((0, 1), (1, 2), 0)
            and _occupied(step_a) == (1, 2)
            and not any(step_b)
            and _occupied(orbit_a) == (0, 1)
            and not any(orbit_b)
            and guarded_data_suppressed
            and _occupied(guarded_rows["A"]) == (1, 2)
            and not any(guarded_rows["B"])
            and guarded_aux_clean
        ),
    }


def _immutable_literal(value: object) -> bool:
    if value is None or type(value) in (bool, int, float, str):
        return True
    return type(value) is tuple and all(_immutable_literal(item) for item in value)


def discipline(
    extracted: dict[str, object],
    no_hardcoded_absolute_site: bool,
) -> dict[str, object]:
    """Check import/module discipline and publish the exact honest boundary."""

    loaded_blocklisted = tuple(
        sorted(
            name
            for name in sys.modules
            if any(
                name == f"frontier_cycle{cycle}"
                or name.startswith(f"frontier_cycle{cycle}_")
                for cycle in BLOCKLISTED_CYCLES
            )
        )
    )
    current_k_attributes = tuple(
        sorted((name, id(value)) for name, value in vars(K).items())
    )
    immutable_tables = (
        AUDIT_INPUT_PATHS,
        EXPECTED_PAIR_TEMPLATE,
        EXPECTED_PRIMARY_AUDIT_INPUTS,
        EXPECTED_REFUSED_COUNTS,
        EXPECTED_MINIMAL_WITNESS,
        EXPECTED_REMAINING_SUPPLIED_COMPONENTS,
        BLOCKLISTED_CYCLES,
    )
    boundary = {
        "no_hardcoded_absolute_site_in_template":
            no_hardcoded_absolute_site,
        "source_selection_remains_supplied": (
            "external application-position parameter"
            in extracted["remaining_supplied_components"]
        ),
        "generalized_controller_no_go_claimed": False,
        "remaining_supplied_components":
            extracted["remaining_supplied_components"],
        "claim_scope": extracted["claim_scope"],
    }
    return {
        "K_attribute_writes": current_k_attributes != K_ATTRIBUTE_BASELINE,
        "blocklisted_imports": loaded_blocklisted,
        "tables_are_immutable_literals": all(
            _immutable_literal(table) for table in immutable_tables
        ),
        "AUDIT_INPUT_PATHS_is_pure_literal_tuple": (
            type(AUDIT_INPUT_PATHS) is tuple
            and AUDIT_INPUT_PATHS
            == declared_input_closure(DIRECT_INPUT_PATHS)
        ),
        "honest_boundary": boundary,
        "pass": (
            current_k_attributes == K_ATTRIBUTE_BASELINE
            and not loaded_blocklisted
            and all(_immutable_literal(table) for table in immutable_tables)
            and no_hardcoded_absolute_site
            and boundary["source_selection_remains_supplied"]
            and not boundary["generalized_controller_no_go_claimed"]
            and boundary["remaining_supplied_components"]
            == EXPECTED_REMAINING_SUPPLIED_COMPONENTS
            and boundary["claim_scope"] == EXPECTED_CLAIM_SCOPE
        ),
    }


def _honest_failure(label: str, error: BaseException) -> dict[str, object]:
    return {
        "pass": False,
        "certificate": label,
        "error": f"{type(error).__name__}: {error}",
    }


def main() -> int:
    started = perf_counter()
    checks: dict[str, bool] = {}
    certificates: dict[str, dict[str, object]] = {}
    extracted: dict[str, object] = {}

    try:
        input_contract = input_contract_certificate()
    except BaseException as error:
        input_contract = _honest_failure("input_contract", error)
    certificates["input_contract"] = input_contract
    checks["input_contract"] = bool(input_contract.get("pass"))

    try:
        extraction_public, extracted = extraction()
    except BaseException as error:
        extraction_public = _honest_failure("extraction", error)
    certificates["extraction"] = extraction_public
    checks["extraction"] = bool(extraction_public.get("pass"))

    try:
        pair = pair_word_recount(extracted)
    except BaseException as error:
        pair = _honest_failure("pair_word_recount", error)
    certificates["pair_word_recount"] = pair
    checks["pair_word_recount"] = bool(pair.get("pass"))

    try:
        law = count2_law_recount(extracted)
    except BaseException as error:
        law = _honest_failure("count2_law_recount", error)
    certificates["count2_law_recount"] = law
    checks["count2_law_recount"] = bool(law.get("pass"))

    try:
        deletions = deletion_control_recount(extracted)
    except BaseException as error:
        deletions = _honest_failure("deletion_control_recount", error)
    certificates["deletion_control_recount"] = deletions
    checks["deletion_control_recount"] = bool(deletions.get("pass"))

    try:
        guard = guard_witness_reproduction(extracted)
    except BaseException as error:
        guard = _honest_failure("guard_witness_reproduction", error)
    certificates["guard_witness_reproduction"] = guard
    checks["guard_witness_reproduction"] = bool(guard.get("pass"))

    no_hardcoded_absolute_site = (
        checks["extraction"] and checks["pair_word_recount"]
    )
    try:
        disciplined = discipline(extracted, no_hardcoded_absolute_site)
    except BaseException as error:
        disciplined = _honest_failure("discipline", error)
    certificates["discipline"] = disciplined
    checks["discipline"] = bool(disciplined.get("pass"))

    try:
        primary_liveness = primary_liveness_certificate()
    except BaseException as error:
        primary_liveness = _honest_failure("primary_liveness", error)
    certificates["primary_liveness"] = primary_liveness
    checks["primary_liveness"] = bool(primary_liveness.get("pass"))

    elapsed = perf_counter() - started
    all_pass = all(checks.values()) and elapsed < AUDIT_TIMEOUT_SEC
    report: dict[str, Any] = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "NOTE_PATH": NOTE_PATH,
        "audit_timeout_seconds": AUDIT_TIMEOUT_SEC,
        "checks": checks,
        "checks_passed": sum(checks.values()),
        "checks_total": len(checks),
        "pass": all_pass,
        "runtime_seconds": round(elapsed, 6),
        "certificates": certificates,
        "terminal": (
            "CYCLE734_PAIRED_EXCITATION_INDEPENDENT_CHECK_PASS"
            if all_pass
            else "CYCLE734_PAIRED_EXCITATION_INDEPENDENT_CHECK_HONEST_FAIL"
        ),
    }
    lines = [
        f"{'PASS' if passed else 'FAIL'} {label} :: {passed}"
        for label, passed in checks.items()
    ]
    payload = json.dumps(
        report, sort_keys=True, separators=(",", ":"), default=str
    )
    text = "\n".join(lines) + "\nSUMMARY_JSON " + payload + "\n"
    if len(text.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        compact = {
            "checks": checks,
            "checks_passed": sum(checks.values()),
            "checks_total": len(checks),
            "pass": False,
            "runtime_seconds": round(elapsed, 6),
            "stdout_bytes_before_compaction": len(text.encode("utf-8")),
            "terminal": (
                "CYCLE734_PAIRED_EXCITATION_INDEPENDENT_CHECK_HONEST_FAIL"
            ),
        }
        text = (
            "\n".join(lines)
            + "\nFAIL stdout_under_150KB :: False\nSUMMARY_JSON "
            + json.dumps(compact, sort_keys=True, separators=(",", ":"))
            + "\n"
        )
        all_pass = False
    sys.stdout.write(text)
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
