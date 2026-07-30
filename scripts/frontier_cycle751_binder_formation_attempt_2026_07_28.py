#!/usr/bin/env python3
"""Exact finite net-endpoint-delta census and conditional API adapter.

This runner assigns no physical meaning to the newly defined
``net_delta_nonempty`` bit. In particular, it does not derive framework
``BINDER`` or construct framework Records.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = (
    "docs/BINDER_FORMATION_ATTEMPT_CYCLE751_"
    "BOUNDED_THEOREM_NOTE_2026-07-28.md"
)
AUDIT_INPUT_PATHS = (
    "docs/BINDER_FORMATION_ATTEMPT_CYCLE751_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
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
    "scripts/frontier_cycle709_local_seam_clifford_core_2026_07_26.py",
    "scripts/frontier_cycle709_local_seam_physical_core_2026_07_26.py",
    "scripts/frontier_cycle712_joint_two_cell_full_update_independent_check_2026_07_26.py",
    "scripts/frontier_cycle712_joint_two_cell_full_update_physical_m2_2026_07_26.py",
    "scripts/frontier_cycle713_physical_m2_endpoint_instrument_bridge_2026_07_26.py",
    "scripts/frontier_cycle714_fixed_packet_coherent_composition_check_2026_07_26.py",
    "scripts/frontier_cycle714_full34_fixed_packet_physical_m2_core_2026_07_26.py",
    "scripts/frontier_cycle715_recurrent_directional_packet_bank_2026_07_26.py",
    "scripts/frontier_cycle718_carrier_return_core_2026_07_26.py",
    "scripts/frontier_cycle718_cycle713_carrier_return_composition_core_2026_07_26.py",
    "scripts/frontier_cycle718_spatial_ack_export_core_2026_07_26.py",
    "scripts/frontier_cycle718_spatial_ack_physical_m2_route_2026_07_26.py",
    "scripts/frontier_cycle718_three_bank_physical_route_core_2026_07_26.py",
    "scripts/frontier_cycle718_token_relative_relay_core_2026_07_26.py",
    "scripts/frontier_cycle719_recurrent_cycle612_bank_core_2026_07_26.py",
    "scripts/frontier_full128_25site_nn_circuit_core_2026_07_24.py",
    "scripts/frontier_full128_bare_frame_pair_cocycle_2026_07_24.py",
    "scripts/frontier_full128_code_projectors_2026_07_24.py",
    "scripts/frontier_full128_cycle_cocycle_intertwiner_2026_07_24.py",
    "scripts/frontier_full128_cycle_encoder_2026_07_24.py",
    "scripts/frontier_full128_two_rail_fixed_law_core_2026_07_24.py",
    "scripts/frontier_literal_patchgraph_cycle656_projected_trace_cycle707_2026_07_26.py",
    "scripts/frontier_literal_patchgraph_z3_m2_placement_core_cycle707_2026_07_26.py",
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
    "scripts/frontier_cycle719_recurrent_physical_route_core_2026_07_26.py",
    "scripts/frontier_cycle719_source_local_finalizer_core_2026_07_26.py",
    "scripts/frontier_cycle719_local_handshake_controller_core_2026_07_26.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from dataclasses import dataclass
from hashlib import sha256
import inspect
import json
from pathlib import Path
from time import perf_counter

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


ROOT = Path(__file__).resolve().parents[1]
FIXTURE_BANK_COUNTS = (2, 5, 12)
EXPECTED_COUNTS = {
    2: (32, 22, 18, 17),
    5: (32, 22, 18, 17, 22, 19, 22, 19, 26, 21),
    12: (
        32, 22, 18, 17, 22, 19, 22, 19, 26, 21, 22, 19,
        26, 21, 26, 21, 30, 22, 18, 17, 22, 19, 22, 19,
    ),
}
EXPECTED_PROGRAM_STATIONS = {2: 11, 5: 35, 12: 91}
EXPECTED_TOTAL_CHANGES = {2: 89, 5: 218, 12: 522}
STDOUT_LIMIT_BYTES = 150 * 1024
CHECKS: dict[str, bool] = {}
OUTPUT_LINES: list[str] = []


@dataclass(frozen=True)
class EndpointTransition:
    """One supplied trajectory row and its net endpoint support."""

    bank_count: int
    tick_id: int
    direction: tuple[int, int]
    support: tuple[int, ...]


def check(label: str, condition: bool, detail: object = "") -> bool:
    if label in CHECKS:
        raise AssertionError(("duplicate check", label))
    passed = bool(condition)
    CHECKS[label] = passed
    suffix = "" if detail == "" else f" {json.dumps(detail, sort_keys=True)}"
    OUTPUT_LINES.append(
        f"{'PASS' if passed else 'FAIL'} {label} :: {passed}{suffix}"
    )
    return passed


def stable_json(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(stable_json(value).encode()).hexdigest()


def normalized_text(relative: str) -> str:
    body = (ROOT / relative).read_text(encoding="utf-8").lower()
    return " ".join(body.replace("`", "").replace("*", "").split())


def note_contract() -> dict[str, object]:
    required = (
        "claim type: bounded_theorem",
        "net_delta_nonempty is a newly defined finite indicator",
        "does not identify net_delta_nonempty with framework binder",
        "ships no authored pass transcript or claim-status receipt",
    )
    forbidden = (
        "the binder flag derived",
        "binding turned out to be",
        "no lawful pure-transport",
        "three of w3",
        "checker-audited",
        "cycle-742 embedding",
    )
    text = normalized_text(NOTE_PATH)
    return {
        "missing": tuple(phrase for phrase in required if phrase not in text),
        "forbidden": tuple(phrase for phrase in forbidden if phrase in text),
    }


def declared_input_closure() -> dict[str, object]:
    expected = (
        NOTE_PATH,
        "docs/MINIMAL_AXIOMS_2026-06-29.md",
        *K.AUDIT_INPUT_PATHS,
    )
    return {
        "declared_count": len(AUDIT_INPUT_PATHS),
        "expected_count": len(expected),
        "exact": AUDIT_INPUT_PATHS == expected,
    }


def held_admit_shape() -> dict[str, object]:
    tree = ast.parse(inspect.getsource(K.held_certificate))
    calls = tuple(
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr == "admit"
    )
    keywords = (
        {
            keyword.arg: ast.unparse(keyword.value)
            for keyword in calls[0].keywords
            if keyword.arg is not None
        }
        if len(calls) == 1
        else {}
    )
    supplied = {
        name: keywords.get(name)
        for name in (
            "certificate",
            "binder",
            "actuality",
            "admissibility",
            "law_domain",
        )
    }
    return {
        "admit_calls": len(calls),
        "supplied_gate_expressions": supplied,
        "pass": len(calls) == 1 and all(value == "1" for value in supplied.values()),
    }


def trajectory(bank_count: int) -> dict[str, object]:
    program = K.interleaved_program(bank_count)
    banks, links = K.B.chain_genesis(bank_count)
    persistent = K.M.pack_state(banks, links)
    rows: list[EndpointTransition] = []
    fixed_word_failures = token_return_failures = 0

    for tick_id in range(2 * bank_count):
        direction = (1, 0) if tick_id % 2 == 0 else (0, 1)
        prepared = K.M.prepare_endpoint(persistent, direction)
        post_state, a_tokens, b_tokens, _trace = K.run_orbit(prepared, program)
        fixed = K.A.apply_semantic(
            prepared, K.M.global_allocator_word(bank_count)
        )
        fixed_word_failures += post_state != fixed
        token_return_failures += (
            a_tokens != (1,) + (0,) * (len(program) - 1) or any(b_tokens)
        )
        support = tuple(
            wire
            for wire, (before, after) in enumerate(zip(persistent, post_state))
            if before != after
        )
        rows.append(EndpointTransition(bank_count, tick_id, direction, support))
        persistent = post_state

    return {
        "bank_count": bank_count,
        "program_stations": len(program),
        "rows": tuple(rows),
        "fixed_word_failures": fixed_word_failures,
        "token_return_failures": token_return_failures,
    }


def finite_census(families: tuple[dict[str, object], ...]) -> dict[str, object]:
    by_family: dict[int, dict[str, object]] = {}
    all_counts: list[int] = []
    for family in families:
        bank_count = int(family["bank_count"])
        rows = family["rows"]
        if not isinstance(rows, tuple):
            raise TypeError("trajectory rows must be a tuple")
        counts = tuple(len(row.support) for row in rows)
        all_counts.extend(counts)
        by_family[bank_count] = {
            "events": len(rows),
            "program_stations": family["program_stations"],
            "support_cardinalities": counts,
            "total_endpoint_changes": sum(counts),
            "minimum_support": min(counts),
            "maximum_support": max(counts),
            "count_sha256": digest(counts),
        }

    expected_events = sum(2 * n for n in FIXTURE_BANK_COUNTS)
    return {
        "by_family": by_family,
        "events": len(all_counts),
        "total_endpoint_changes": sum(all_counts),
        "minimum_support": min(all_counts),
        "maximum_support": max(all_counts),
        "net_delta_nonempty_ones": sum(bool(count) for count in all_counts),
        "pass": (
            len(all_counts) == expected_events == 38
            and sum(all_counts) == 829
            and min(all_counts) == 17
            and max(all_counts) == 32
            and all(
                by_family[n]["support_cardinalities"] == EXPECTED_COUNTS[n]
                and by_family[n]["program_stations"]
                == EXPECTED_PROGRAM_STATIONS[n]
                and by_family[n]["total_endpoint_changes"]
                == EXPECTED_TOTAL_CHANGES[n]
                for n in FIXTURE_BANK_COUNTS
            )
        ),
    }


def net_delta_nonempty(row: EndpointTransition) -> int:
    """New finite indicator: one exactly when endpoint support is nonempty."""

    return int(bool(row.support))


def admit(
    chain: object,
    row: EndpointTransition,
    binder_api_value: int,
) -> str:
    """Call the lower-case Cycle-610 API under four supplied one-bits."""

    return chain.admit(
        tick_id=row.tick_id,
        orientation=1 if row.direction == (1, 0) else -1,
        certificate=1,
        binder=binder_api_value,
        actuality=1,
        admissibility=1,
        law_domain=1,
    )


def conditional_adapter(
    families: tuple[dict[str, object], ...],
) -> dict[str, object]:
    by_family: dict[int, dict[str, object]] = {}
    status_mismatches = row_mismatches = indicator_zeroes = 0

    for family in families:
        bank_count = int(family["bank_count"])
        rows = family["rows"]
        if not isinstance(rows, tuple):
            raise TypeError("trajectory rows must be a tuple")
        literal_chain = K.B.C704.C610.EventChain(bank=2 * bank_count)
        indicator_chain = K.B.C704.C610.EventChain(bank=2 * bank_count)
        literal_trace: list[object] = []
        indicator_trace: list[object] = []
        for row in rows:
            indicator = net_delta_nonempty(row)
            indicator_zeroes += indicator == 0
            literal_status = admit(literal_chain, row, 1)
            indicator_status = admit(indicator_chain, row, indicator)
            literal_rows = K.B.cell_rows(literal_chain)
            indicator_rows = K.B.cell_rows(indicator_chain)
            status_mismatches += literal_status != indicator_status
            row_mismatches += literal_rows != indicator_rows
            literal_trace.append((literal_status, literal_rows))
            indicator_trace.append((indicator_status, indicator_rows))
        literal_bytes = stable_json(literal_trace).encode()
        indicator_bytes = stable_json(indicator_trace).encode()
        by_family[bank_count] = {
            "events": len(rows),
            "byte_exact": literal_bytes == indicator_bytes,
            "trace_sha256": sha256(indicator_bytes).hexdigest(),
        }

    empty_row = EndpointTransition(2, 0, (1, 0), ())
    empty_indicator_chain = K.B.C704.C610.EventChain(bank=1)
    literal_control_chain = K.B.C704.C610.EventChain(bank=1)
    synthetic_control = {
        "fixture_member": False,
        "endpoint_support_size": 0,
        "net_delta_nonempty": net_delta_nonempty(empty_row),
        "indicator_status": admit(
            empty_indicator_chain, empty_row, net_delta_nonempty(empty_row)
        ),
        "literal_one_status": admit(literal_control_chain, empty_row, 1),
    }
    return {
        "by_family": by_family,
        "indicator_zeroes_on_enumerated_rows": indicator_zeroes,
        "status_mismatches": status_mismatches,
        "cell_row_mismatches": row_mismatches,
        "synthetic_nonfixture_control": synthetic_control,
        "pass": (
            indicator_zeroes == 0
            and status_mismatches == 0
            and row_mismatches == 0
            and all(row["byte_exact"] for row in by_family.values())
            and synthetic_control["net_delta_nonempty"] == 0
            and synthetic_control["indicator_status"] == "no_opportunity"
            and synthetic_control["literal_one_status"] == "admitted"
        ),
    }


def main() -> int:
    started = perf_counter()
    contract = note_contract()
    check(
        "A_note_contract",
        not contract["missing"] and not contract["forbidden"],
        contract,
    )

    closure = declared_input_closure()
    check("B_complete_declared_input_closure", closure["exact"], closure)

    held_shape = held_admit_shape()
    check("C_upstream_literal_one_API_shape", held_shape["pass"], held_shape)

    families = tuple(trajectory(n) for n in FIXTURE_BANK_COUNTS)
    trajectory_integrity = {
        "fixed_word_failures": sum(
            int(family["fixed_word_failures"]) for family in families
        ),
        "token_return_failures": sum(
            int(family["token_return_failures"]) for family in families
        ),
    }
    check(
        "D_controller_trajectory_integrity",
        not any(trajectory_integrity.values()),
        trajectory_integrity,
    )

    census = finite_census(families)
    check("E_exact_endpoint_delta_census", census["pass"], {
        "events": census["events"],
        "total_endpoint_changes": census["total_endpoint_changes"],
        "minimum_support": census["minimum_support"],
        "maximum_support": census["maximum_support"],
    })

    adapter = conditional_adapter(families)
    check("F_conditional_API_adapter", adapter["pass"], {
        "indicator_zeroes": adapter["indicator_zeroes_on_enumerated_rows"],
        "status_mismatches": adapter["status_mismatches"],
        "cell_row_mismatches": adapter["cell_row_mismatches"],
    })

    boundary = {
        "framework_binder_derived": False,
        "record_formation_claimed": False,
        "physical_write_claimed": False,
        "spatial_locality_claimed": False,
        "all_lawful_events_exhausted": False,
        "negative_or_no_go_claimed": False,
        "semantic_identification": "supplied labeling convention or open bridge",
    }
    check(
        "G_honest_boundary",
        not any(
            boundary[key]
            for key in (
                "framework_binder_derived",
                "record_formation_claimed",
                "physical_write_claimed",
                "spatial_locality_claimed",
                "all_lawful_events_exhausted",
                "negative_or_no_go_claimed",
            )
        ),
        boundary,
    )

    report = {
        "cycle": 751,
        "claim": "finite net-endpoint-delta census and conditional API adapter",
        "bounded": True,
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "DECLARED_INPUT_PATHS": DECLARED_INPUT_PATHS,
        "NOTE_PATH": NOTE_PATH,
        "census": census,
        "adapter": adapter,
        "boundary": boundary,
        "checks": CHECKS,
        "checks_passed": sum(CHECKS.values()),
        "checks_failed": sum(not value for value in CHECKS.values()),
        "runtime_seconds": perf_counter() - started,
    }
    report["report_sha256"] = digest(report)
    report["pass"] = all(CHECKS.values())

    projected = "\n".join((*OUTPUT_LINES, stable_json(report))).encode()
    check(
        "OUTPUT_stdout_under_150KB",
        len(projected) < STDOUT_LIMIT_BYTES,
        {"bytes": len(projected), "limit": STDOUT_LIMIT_BYTES},
    )
    report["checks"] = CHECKS
    report["checks_passed"] = sum(CHECKS.values())
    report["checks_failed"] = sum(not value for value in CHECKS.values())
    report["pass"] = all(CHECKS.values())
    terminal = (
        "CYCLE751_NET_DELTA_FINITE_ADAPTER_PASS"
        if report["pass"]
        else "CYCLE751_NET_DELTA_FINITE_ADAPTER_FAIL"
    )
    report["terminal"] = terminal

    print("\n".join(OUTPUT_LINES))
    print(stable_json(report))
    print(terminal)
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
