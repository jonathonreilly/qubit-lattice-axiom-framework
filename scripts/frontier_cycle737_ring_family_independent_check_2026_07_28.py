#!/usr/bin/env python3
"""Independent joint-live checker for the bounded Cycle-737 diagnostics.

The primary runner is never imported.  This checker first requires a fresh
successful primary execution, then asks that same executable for literal gate
streams and independently evaluates those streams with a small bit-plane
interpreter.  It separately rederives the four cycle-graph censuses and the
marked-cut reference identities.

The checker does not certify framework Admissibility, constructor uniqueness,
controller lawfulness, preparation, a full guarded word, a uniform family
theorem, an adjacency wall, or a no-go result.
"""
from __future__ import annotations

import ast
from collections import Counter
from hashlib import sha256
import json
from math import comb
from pathlib import Path
import subprocess
import sys
from time import perf_counter
from typing import Any, Iterable


sys.dont_write_bytecode = True

AUDIT_TIMEOUT_SEC = 900
STDOUT_LIMIT_BYTES = 150 * 1024
PRIMARY_PATH = (
    "scripts/frontier_cycle737_ring_family_uniformity_2026_07_28.py"
)
NOTE_PATH = (
    "docs/RING_FAMILY_UNIFORMITY_CYCLE737_"
    "BOUNDED_THEOREM_NOTE_2026-07-28.md"
)

# The primary plus its complete literal mutable input closure.  The checker
# verifies this tuple against the primary's own AST and fresh JSON report.
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle737_ring_family_uniformity_2026_07_28.py",
    "docs/FULL128_LOCAL_M64_SEAM_M2_BARE_FRAME_INTERTWINER_BOUNDED_THEOREM_NOTE_2026-07-24.md",
    "docs/JOINT_TWO_CELL_FULL_UPDATE_PHYSICAL_M2_COMPILER_CYCLE712_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/LITERAL_PATCHGRAPH_Z3_M2_PLACEMENT_AND_FIXED_CONTROLLER_CYCLE707_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/LOCAL_SEAM_SIGNED_CLIFFORD_PHYSICAL_M2_COMPILER_CYCLE709_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/LOCAL_TOKEN_ROW_ENFORCEMENT_CYCLE724_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "docs/OPENREFERENCE_PATCHGRAPH_FOUR_RAIL_SIGNED_CLIFFORD_EQUIVALENCE_CYCLE706_NOTE_2026-07-26.md",
    "docs/PHYSICAL_CYCLE704_FSWAP_ENDPOINT_CUBE_BRIDGE_CYCLE708_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/PHYSICAL_M2_ENDPOINT_INSTRUMENT_CYCLE704_CYCLE612_BRIDGE_CYCLE713_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/PHYSICAL_M2_FULL34_FIXED_PACKET_COMPOSITION_CYCLE714_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/PHYSICAL_M2_SPATIAL_ACK_CYCLE612_INTERVAL_BRIDGE_CYCLE718_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/RECURRENT_DIRECTIONAL_PACKET_BANK_CYCLE715_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/RECURRENT_MATTER_HISTORY_CONTROLLER_CYCLE719_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/REFUSAL_WRAPPED_CONTROLLER_CYCLE723_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "docs/RING_FAMILY_UNIFORMITY_CYCLE737_BOUNDED_THEOREM_NOTE_2026-07-28.md",
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
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

SELECTED_FIXTURES = ((1, 3), (2, 11), (3, 19), (4, 27))
EXPECTED_COUNTS = {
    3: (1, 3),
    11: (1, 11, 44, 77, 55, 11),
    19: (1, 19, 152, 665, 1729, 2717, 2508, 1254, 285, 19),
    27: (
        1, 27, 324, 2277, 10395, 32319, 69768, 104652,
        107406, 72930, 30888, 7371, 819, 27,
    ),
}
EXPECTED_COVARIANCE_IDENTITIES = {3: 12, 11: 649, 19: 3401, 27: 9801}
EXPECTED_ORBIT_STEPS = {3: 12, 11: 2189, 19: 177631, 27: 11858508}

CHECKS: dict[str, bool] = {}
OUTPUT_LINES: list[str] = []


def check(label: str, condition: bool) -> bool:
    if label in CHECKS:
        raise AssertionError(("duplicate check", label))
    passed = bool(condition)
    CHECKS[label] = passed
    OUTPUT_LINES.append(f"{'PASS' if passed else 'FAIL'} {label} :: {passed}")
    return passed


def digest_json(value: Any) -> str:
    return sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def top_level_literal(path: Path, name: str) -> Any:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    for node in tree.body:
        if isinstance(node, ast.Assign):
            targets = node.targets
            value = node.value
        elif isinstance(node, ast.AnnAssign):
            targets = (node.target,)
            value = node.value
        else:
            continue
        if any(
            isinstance(target, ast.Name) and target.id == name
            for target in targets
        ):
            return ast.literal_eval(value)
    raise KeyError((str(path), name))


def run_primary(root: Path, export: bool = False) -> tuple[dict[str, Any], dict[str, Any]]:
    command = [sys.executable, PRIMARY_PATH]
    if export:
        command.append("--export-gates")
    completed = subprocess.run(
        command,
        cwd=root,
        check=False,
        capture_output=True,
        text=True,
        timeout=600,
    )
    evidence = {
        "command": command,
        "returncode": completed.returncode,
        "stdout_bytes": len(completed.stdout.encode()),
        "stderr": completed.stderr[-1000:],
    }
    if completed.returncode != 0:
        raise RuntimeError(("primary execution failed", evidence))
    lines = [line for line in completed.stdout.splitlines() if line.strip()]
    if not lines:
        raise RuntimeError("primary emitted no JSON")
    return json.loads(lines[-1]), evidence


def independent_masks(stations: int) -> tuple[int, ...]:
    masks: list[int] = []

    def visit(site: int, first: bool, previous: bool, mask: int) -> None:
        if site == stations:
            if not (first and previous):
                masks.append(mask)
            return
        visit(site + 1, first, False, mask)
        if not previous and not (site == stations - 1 and first):
            visit(site + 1, first or site == 0, True, mask | (1 << site))

    visit(0, False, False, 0)
    return tuple(masks)


def closed_cycle_count(stations: int, count: int) -> int:
    if count == 0:
        return 1
    if count > stations // 2:
        return 0
    return stations * comb(stations - count, count) // (stations - count)


def rotate_mask(mask: int, shift: int, stations: int) -> int:
    shift %= stations
    full = (1 << stations) - 1
    if not shift:
        return mask & full
    return ((mask << shift) & full) | (mask >> (stations - shift))


def canonical_reference(mask: int, stations: int) -> int:
    parity = mask.bit_count() & 1
    reference = 0
    current = 0
    for site in range(stations - 1):
        current ^= (mask >> site) & 1
        if site == 0:
            current ^= parity
        reference |= current << (site + 1)
    return reference


def reference_failures(mask: int, stations: int) -> int:
    reference = canonical_reference(mask, stations)
    parity = mask.bit_count() & 1
    return sum(
        (
            ((mask >> site) & 1)
            ^ ((reference >> site) & 1)
            ^ ((reference >> ((site + 1) % stations)) & 1)
            ^ (parity if site == 0 else 0)
        )
        != 0
        for site in range(stations)
    )


def gauge_translate(reference: int, parity: int, shift: int, stations: int) -> int:
    translated = rotate_mask(reference, shift, stations)
    if parity:
        for site in range(1, shift + 1):
            translated ^= 1 << site
    if translated & 1:
        translated ^= (1 << stations) - 1
    return translated


def static_check(stations: int, masks: tuple[int, ...]) -> dict[str, Any]:
    counts = tuple(
        sum(mask.bit_count() == count for mask in masks)
        for count in range(stations // 2 + 1)
    )
    formula = tuple(
        closed_cycle_count(stations, count)
        for count in range(stations // 2 + 1)
    )
    first_by_count: dict[int, int] = {}
    for mask in masks:
        first_by_count.setdefault(mask.bit_count(), mask)
    sample = {mask for mask in masks if mask.bit_count() <= 2}
    sample.update(first_by_count.values())
    covariance_failures = 0
    for mask in sample:
        reference = canonical_reference(mask, stations)
        for shift in range(stations):
            covariance_failures += gauge_translate(
                reference, mask.bit_count() & 1, shift, stations
            ) != canonical_reference(rotate_mask(mask, shift, stations), stations)
    identities = len(sample) * stations
    marked_failures = sum(reference_failures(mask, stations) for mask in masks)
    return {
        "counts": counts,
        "formula": formula,
        "total": len(masks),
        "marked_edge_reference_failures": marked_failures,
        "covariance_identities": identities,
        "covariance_failures": covariance_failures,
        "n3_multi_token_degenerate": (
            stations != 3 or not any(mask.bit_count() >= 2 for mask in masks)
        ),
        "exact": (
            counts == formula == EXPECTED_COUNTS[stations]
            and marked_failures == 0
            and identities == EXPECTED_COVARIANCE_IDENTITIES[stations]
            and covariance_failures == 0
        ),
    }


def mask_planes(masks: tuple[int, ...], stations: int) -> tuple[int, ...]:
    planes = [0] * stations
    for row, mask in enumerate(masks):
        row_bit = 1 << row
        while mask:
            low = mask & -mask
            planes[low.bit_length() - 1] |= row_bit
            mask -= low
    return tuple(planes)


def count_planes(masks: tuple[int, ...], width: int) -> tuple[int, ...]:
    planes = [0] * width
    for row, mask in enumerate(masks):
        row_bit = 1 << row
        for bit in range(width):
            if (mask.bit_count() >> bit) & 1:
                planes[bit] |= row_bit
    return tuple(planes)


def apply_rows(
    gates: Iterable[list[Any]], planes: dict[int, int], full: int
) -> None:
    for gate in gates:
        kind = gate[0]
        wires = gate[1:]
        if kind == "X":
            planes[wires[0]] = planes.get(wires[0], 0) ^ full
        elif kind == "CNOT":
            planes[wires[1]] = (
                planes.get(wires[1], 0) ^ planes.get(wires[0], 0)
            )
        elif kind == "TOF":
            planes[wires[2]] = (
                planes.get(wires[2], 0)
                ^ (planes.get(wires[0], 0) & planes.get(wires[1], 0))
            )
        else:
            raise AssertionError(("unsupported exported gate", kind))


def prefix_check(
    fixture: dict[str, Any], masks: tuple[int, ...]
) -> dict[str, Any]:
    stations = int(fixture["ring"])
    rows = len(masks)
    maximum = stations // 2
    full = (1 << rows) - 1
    a_planes = mask_planes(masks, stations)
    accepts = refusals = failures = reversibility_failures = 0
    prefixes = fixture["count_prefixes"]
    for expected_count, exported in enumerate(prefixes):
        if int(exported["expected_count"]) != expected_count:
            failures += 1
        layout = exported["layout"]
        gates = exported["gates"]
        initial = {
            int(layout["a_base"]) + site: plane
            for site, plane in enumerate(a_planes)
            if plane
        }
        planes = dict(initial)
        apply_rows(gates, planes, full)
        expected_counts = count_planes(masks, int(layout["counter_width"]))
        for bit, expected_plane in enumerate(expected_counts):
            failures += (
                planes.get(int(layout["counter_base"]) + bit, 0)
                ^ expected_plane
            ).bit_count()
        expected_refusal = 0
        for row, mask in enumerate(masks):
            expected_refusal |= (mask.bit_count() != expected_count) << row
        refusal = planes.get(int(layout["refusal_latch"]), 0)
        failures += (refusal ^ expected_refusal).bit_count()
        accepts += rows - refusal.bit_count()
        refusals += refusal.bit_count()
        for site, expected_plane in enumerate(a_planes):
            failures += (
                planes.get(int(layout["a_base"]) + site, 0) ^ expected_plane
            ).bit_count()
        apply_rows(reversed(gates), planes, full)
        reversibility_failures += sum(
            (
                planes.get(wire, 0) ^ initial.get(wire, 0)
            ).bit_count()
            for wire in set(planes) | set(initial)
        )
    return {
        "prefixes": len(prefixes),
        "accepts": accepts,
        "refusals": refusals,
        "failures": failures,
        "reversibility_failures": reversibility_failures,
        "exact": (
            len(prefixes) == maximum + 1
            and accepts == rows
            and refusals == rows * maximum
            and failures == reversibility_failures == 0
        ),
    }


def bare_check(
    fixture: dict[str, Any], masks: tuple[int, ...]
) -> dict[str, Any]:
    stations = int(fixture["ring"])
    data = tuple(int(bit) for bit in fixture["data"])
    gates = fixture["bare_word"]
    rows = len(masks)
    full = (1 << rows) - 1
    a_base = len(data)
    b_base = a_base + stations
    work_base = b_base + stations
    a_planes = mask_planes(masks, stations)
    initial = {wire: full for wire, bit in enumerate(data) if bit}
    initial.update(
        {
            a_base + site: plane
            for site, plane in enumerate(a_planes)
            if plane
        }
    )
    planes = dict(initial)
    failures = 0
    for step in range(stations):
        apply_rows(gates, planes, full)
        for site in range(stations):
            failures += (
                planes.get(a_base + site, 0)
                ^ a_planes[(site - step - 1) % stations]
            ).bit_count()
        for site in range(stations):
            failures += planes.get(b_base + site, 0).bit_count()
            failures += planes.get(work_base + site, 0).bit_count()
            failures += (
                planes.get(a_base + site, 0)
                & planes.get(a_base + ((site + 1) % stations), 0)
            ).bit_count()
    changed = 0
    for wire, bit in enumerate(data):
        changed |= planes.get(wire, 0) ^ (full if bit else 0)
    for _step in range(stations):
        apply_rows(reversed(gates), planes, full)
    inverse_failures = sum(
        (
            planes.get(wire, 0) ^ initial.get(wire, 0)
        ).bit_count()
        for wire in set(planes) | set(initial)
    )
    return {
        "configuration_steps": rows * stations,
        "rail_or_adjacency_failures": failures,
        "inverse_failures": inverse_failures,
        "data_changed_configurations": changed.bit_count(),
        "exact": (
            rows * stations == EXPECTED_ORBIT_STEPS[stations]
            and failures == inverse_failures == 0
        ),
    }


def expected_kind_counts(banks: int) -> Counter[str]:
    return Counter(
        {
            "source": 1,
            "bank": banks,
            "cross": banks - 1,
            "handoff": 2 * (banks - 1),
            "relay": 4 * (banks - 1),
            "finalizer": 1,
        }
    )


def main() -> int:
    if sys.argv[1:]:
        raise SystemExit("usage: independent-check")
    started = perf_counter()
    root = Path(__file__).resolve().parents[1]

    primary_report, live_evidence = run_primary(root)
    check(
        "JOINT_LIVE_primary_passes",
        live_evidence["returncode"] == 0
        and primary_report.get("pass") is True
        and primary_report.get("terminal")
        == "CYCLE737_SELECTED_CONSTRUCTOR_CENSUS_DIAGNOSTICS_PASS",
    )

    export, export_evidence = run_primary(root, export=True)
    supplied_digest = export.pop("export_sha256", None)
    check(
        "EXPORT_literal_gate_stream_integrity",
        export_evidence["returncode"] == 0
        and export.get("schema") == "cycle737_selected_gate_export_v1"
        and supplied_digest == digest_json(export),
    )

    primary_inputs = tuple(
        top_level_literal(root / PRIMARY_PATH, "AUDIT_INPUT_PATHS")
    )
    check(
        "INPUT_complete_literal_closure",
        AUDIT_INPUT_PATHS == (PRIMARY_PATH,) + primary_inputs
        and tuple(primary_report["AUDIT_INPUT_PATHS"]) == primary_inputs
        and len(AUDIT_INPUT_PATHS) == len(set(AUDIT_INPUT_PATHS)),
    )

    constructor_rows = export["constructor_witnesses"]
    constructor_exact = len(constructor_rows) == 8
    for banks, row in enumerate(constructor_rows, start=1):
        kinds = Counter(str(kind) for kind in row["program_kinds"])
        constructor_exact &= (
            int(row["banks"]) == banks
            and len(row["program_kinds"]) == 8 * banks - 5
            and kinds == expected_kind_counts(banks)
        )
    check("A_supplied_constructor_length", constructor_exact)

    fixture_reports: dict[str, Any] = {}
    fixtures = export["fixtures"]
    fixture_shape = len(fixtures) == len(SELECTED_FIXTURES)
    for expected, fixture in zip(SELECTED_FIXTURES, fixtures):
        banks, stations = expected
        fixture_shape &= (
            int(fixture["banks"]) == banks
            and int(fixture["ring"]) == stations
            and len(fixture["program_kinds"]) == stations
        )
        masks = independent_masks(stations)
        static = static_check(stations, masks)
        prefix = prefix_check(fixture, masks)
        bare = bare_check(fixture, masks)
        check(f"B_independent_census_static_n{stations}", static["exact"])
        check(f"C_exported_count_prefix_n{stations}", prefix["exact"])
        check(f"D_exported_bare_transport_n{stations}", bare["exact"])
        fixture_reports[str(stations)] = {
            "static": static,
            "prefix": prefix,
            "bare": bare,
        }

    boundary = primary_report["boundary"]
    check(
        "E_honest_boundary",
        fixture_shape
        and boundary["selected_fixtures"]
        == [list(row) for row in SELECTED_FIXTURES]
        and boundary["n3_multi_token_degenerate"] is True
        and all(
            boundary[key] is False
            for key in (
                "framework_admissibility_claimed",
                "constructor_uniqueness_claimed",
                "family_uniform_finite_diagnostics_claimed",
                "controller_lawfulness_claimed",
                "autonomous_preparation_claimed",
                "full_guarded_word_claimed",
                "adjacency_wall_or_no_go_claimed",
                "nonfamily_failure_claimed",
            )
        ),
    )

    runtime = perf_counter() - started
    check("TIMEOUT_runtime_under_900_seconds", runtime < AUDIT_TIMEOUT_SEC)
    report: dict[str, Any] = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "NOTE_PATH": NOTE_PATH,
        "PRIMARY_PATH": PRIMARY_PATH,
        "audit_timeout_seconds": AUDIT_TIMEOUT_SEC,
        "bounded": True,
        "checks": CHECKS,
        "checks_passed": sum(CHECKS.values()),
        "checks_failed": sum(not value for value in CHECKS.values()),
        "fixture_reports": fixture_reports,
        "joint_live_primary": {
            **live_evidence,
            "report_sha256": primary_report.get("report_sha256"),
        },
        "gate_export": {
            **export_evidence,
            "export_sha256": supplied_digest,
        },
        "runtime_seconds": runtime,
        "scope": (
            "selected constructor counts and four finite census/static/prefix/"
            "bare diagnostics; no framework or controller theorem"
        ),
        "terminal": "CYCLE737_SELECTED_DIAGNOSTICS_INDEPENDENT_PASS",
    }
    provisional = "\n".join(
        OUTPUT_LINES
        + [json.dumps(report, sort_keys=True, separators=(",", ":"))]
    ) + "\n"
    check(
        "OUTPUT_stdout_under_150KB",
        len(provisional.encode()) < STDOUT_LIMIT_BYTES,
    )
    report["checks"] = CHECKS
    report["checks_passed"] = sum(CHECKS.values())
    report["checks_failed"] = sum(not value for value in CHECKS.values())
    report["pass"] = all(CHECKS.values())
    report["report_sha256"] = digest_json(
        {
            key: value
            for key, value in report.items()
            if key != "report_sha256"
        }
    )
    print("\n".join(OUTPUT_LINES))
    print(json.dumps(report, sort_keys=True, separators=(",", ":")))
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
