#!/usr/bin/env python3
"""Independent reconstruction of the finite net-endpoint-delta census and
conditional Cycle-610 API adapter.

The checker imports no symbol from the primary. It reconstructs the endpoints
through the Cycle-719 closed-form allocator word, validates the Boolean adapter
decision tree, and runs the primary only as a black-box subprocess.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 900
PRIMARY_PATH = "scripts/frontier_cycle751_binder_formation_attempt_2026_07_28.py"
NOTE_PATH = (
    "docs/BINDER_FORMATION_ATTEMPT_CYCLE751_"
    "BOUNDED_THEOREM_NOTE_2026-07-28.md"
)
AUDIT_INPUT_PATHS = (
    "docs/BINDER_FORMATION_ATTEMPT_CYCLE751_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/frontier_cycle751_binder_formation_attempt_2026_07_28.py",
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
BLOCKLIST = (PRIMARY_PATH,)

import ast
from hashlib import sha256
from itertools import product
import json
import os
from pathlib import Path
import subprocess
import sys
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
CHECKS: dict[str, bool] = {}
OUTPUT_LINES: list[str] = []
STDOUT_LIMIT_BYTES = 150 * 1024


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


def declared_input_closure() -> dict[str, object]:
    expected = (
        NOTE_PATH,
        "docs/MINIMAL_AXIOMS_2026-06-29.md",
        PRIMARY_PATH,
        *K.AUDIT_INPUT_PATHS,
    )
    return {
        "declared_count": len(AUDIT_INPUT_PATHS),
        "expected_count": len(expected),
        "exact": AUDIT_INPUT_PATHS == expected,
    }


def source_contract() -> dict[str, object]:
    source = (ROOT / PRIMARY_PATH).read_text(encoding="utf-8")
    checker_source = Path(__file__).read_text(encoding="utf-8")
    checker_tree = ast.parse(checker_source)
    imported_modules = tuple(
        sorted(
            alias.name
            for node in ast.walk(checker_tree)
            if isinstance(node, ast.Import)
            for alias in node.names
        )
    )
    required = (
        "def net_delta_nonempty",
        '"framework_binder_derived": False',
        '"record_formation_claimed": False',
        '"negative_or_no_go_claimed": False',
        "CYCLE751_NET_DELTA_FINITE_ADAPTER_PASS",
    )
    forbidden = (
        "BINDER_PREDICATE",
        "RecordCell",
        "formation_event_from_k",
        "physical_record_readout_carrier",
    )
    return {
        "missing": tuple(token for token in required if token not in source),
        "forbidden": tuple(token for token in forbidden if token in source),
        "primary_imported_by_checker": any(
            name == Path(PRIMARY_PATH).stem for name in imported_modules
        ),
    }


def reconstruct_counts() -> dict[str, object]:
    by_family: dict[int, dict[str, object]] = {}
    all_counts: list[int] = []
    for bank_count in FIXTURE_BANK_COUNTS:
        banks, links = K.B.chain_genesis(bank_count)
        persistent = K.M.pack_state(banks, links)
        word = K.M.global_allocator_word(bank_count)
        counts: list[int] = []
        for tick_id in range(2 * bank_count):
            direction = (1, 0) if tick_id % 2 == 0 else (0, 1)
            prepared = K.M.prepare_endpoint(persistent, direction)
            post_state = K.A.apply_semantic(prepared, word)
            counts.append(
                sum(
                    before != after
                    for before, after in zip(persistent, post_state)
                )
            )
            persistent = post_state
        counts_tuple = tuple(counts)
        all_counts.extend(counts)
        by_family[bank_count] = {
            "events": len(counts),
            "counts": counts_tuple,
            "total": sum(counts),
            "sha256": digest(counts_tuple),
        }

    return {
        "by_family": by_family,
        "events": len(all_counts),
        "total": sum(all_counts),
        "minimum": min(all_counts),
        "maximum": max(all_counts),
        "nonempty": sum(bool(count) for count in all_counts),
        "pass": (
            len(all_counts) == 38
            and sum(all_counts) == 829
            and min(all_counts) == 17
            and max(all_counts) == 32
            and all(
                by_family[n]["counts"] == EXPECTED_COUNTS[n]
                for n in FIXTURE_BANK_COUNTS
            )
        ),
    }


def exhaustive_indicator_identity() -> dict[str, object]:
    rows = mismatches = 0
    for before in product((0, 1), repeat=3):
        for after in product((0, 1), repeat=3):
            support = tuple(
                index
                for index, (left, right) in enumerate(zip(before, after))
                if left != right
            )
            observed = int(bool(support))
            expected = int(before != after)
            rows += 1
            mismatches += observed != expected
    return {"rows": rows, "mismatches": mismatches, "pass": rows == 64 and not mismatches}


def admission_model(
    *,
    certificate: int,
    binder: int,
    actuality: int,
    admissibility: int,
    law_domain: int,
    fresh: int = 1,
    capacity: int = 1,
) -> str:
    if not (certificate & binder):
        return "no_opportunity"
    if not fresh:
        return "refused_fresh"
    if not (actuality & admissibility & law_domain):
        return "refused_supplied"
    if not capacity:
        return "exhausted"
    return "admitted"


def independent_admission_table() -> dict[str, object]:
    rows = mismatches = 0
    for bits in product((0, 1), repeat=5):
        certificate, binder, actuality, admissibility, law_domain = bits
        chain = K.B.C704.C610.EventChain(bank=1)
        observed = chain.admit(
            tick_id=0,
            orientation=1,
            certificate=certificate,
            binder=binder,
            actuality=actuality,
            admissibility=admissibility,
            law_domain=law_domain,
        )
        expected = admission_model(
            certificate=certificate,
            binder=binder,
            actuality=actuality,
            admissibility=admissibility,
            law_domain=law_domain,
        )
        rows += 1
        mismatches += observed != expected

    fresh_chain = K.B.C704.C610.EventChain(bank=2)
    first = fresh_chain.admit(
        tick_id=0,
        orientation=1,
        certificate=1,
        binder=1,
        actuality=1,
        admissibility=1,
        law_domain=1,
    )
    repeated = fresh_chain.admit(
        tick_id=0,
        orientation=1,
        certificate=1,
        binder=1,
        actuality=1,
        admissibility=1,
        law_domain=1,
    )
    exhausted = K.B.C704.C610.EventChain(bank=0).admit(
        tick_id=0,
        orientation=1,
        certificate=1,
        binder=1,
        actuality=1,
        admissibility=1,
        law_domain=1,
    )
    return {
        "truth_table_rows": rows,
        "truth_table_mismatches": mismatches,
        "fresh_first": first,
        "repeated_tick": repeated,
        "zero_capacity": exhausted,
        "pass": (
            rows == 32
            and mismatches == 0
            and first == "admitted"
            and repeated == "refused_fresh"
            and exhausted == "exhausted"
        ),
    }


def black_box_primary() -> dict[str, object]:
    env = os.environ.copy()
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    env["PYTHONPATH"] = str(ROOT / "scripts")
    completed = subprocess.run(
        [sys.executable, PRIMARY_PATH],
        cwd=ROOT,
        env=env,
        capture_output=True,
        text=True,
        timeout=AUDIT_TIMEOUT_SEC,
        check=False,
    )
    terminal = "CYCLE751_NET_DELTA_FINITE_ADAPTER_PASS"
    stdout_lines = completed.stdout.rstrip().splitlines()
    return {
        "returncode": completed.returncode,
        "terminal_line_matches": bool(stdout_lines)
        and stdout_lines[-1] == terminal,
        "stdout_bytes": len(completed.stdout.encode()),
        "stderr": completed.stderr,
        "pass": (
            completed.returncode == 0
            and bool(stdout_lines)
            and stdout_lines[-1] == terminal
            and len(completed.stdout.encode()) < STDOUT_LIMIT_BYTES
            and not completed.stderr
        ),
    }


def main() -> int:
    started = perf_counter()

    closure = declared_input_closure()
    check("A_complete_declared_input_closure", closure["exact"], closure)

    contract = source_contract()
    check(
        "B_primary_source_boundary_and_independence",
        not contract["missing"]
        and not contract["forbidden"]
        and not contract["primary_imported_by_checker"],
        contract,
    )

    recount = reconstruct_counts()
    check("C_independent_closed_form_recount", recount["pass"], {
        "events": recount["events"],
        "total": recount["total"],
        "minimum": recount["minimum"],
        "maximum": recount["maximum"],
    })

    indicator = exhaustive_indicator_identity()
    check("D_exhaustive_indicator_identity", indicator["pass"], indicator)

    decision_tree = independent_admission_table()
    check(
        "E_independent_Cycle610_decision_tree",
        decision_tree["pass"],
        decision_tree,
    )

    primary = black_box_primary()
    check("F_primary_black_box", primary["pass"], primary)

    report = {
        "cycle": 751,
        "claim": "independent finite net-endpoint-delta reconstruction",
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "DECLARED_INPUT_PATHS": DECLARED_INPUT_PATHS,
        "NOTE_PATH": NOTE_PATH,
        "PRIMARY_PATH": PRIMARY_PATH,
        "BLOCKLIST": BLOCKLIST,
        "recount": recount,
        "indicator_identity": indicator,
        "admission_decision_tree": decision_tree,
        "primary_black_box": primary,
        "boundary": {
            "framework_binder_derived": False,
            "record_formation_claimed": False,
            "physical_write_claimed": False,
            "finite_indicator_only": True,
        },
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
        "CYCLE751_NET_DELTA_INDEPENDENT_CHECK_PASS"
        if report["pass"]
        else "CYCLE751_NET_DELTA_INDEPENDENT_CHECK_FAIL"
    )
    report["terminal"] = terminal

    print("\n".join(OUTPUT_LINES))
    print(stable_json(report))
    print(terminal)
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
