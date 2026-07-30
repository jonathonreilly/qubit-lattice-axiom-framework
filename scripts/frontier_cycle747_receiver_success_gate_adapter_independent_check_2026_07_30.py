#!/usr/bin/env python3
"""Independent finite-state reconstruction of the Cycle-747 salvage theorem.

This checker imports none of the repository modules used by the primary. It
reconstructs the certificate, controlled swap, and admission decision tree,
then invokes the primary only as a clean black-box subprocess.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120
PRIMARY_PATH = "scripts/frontier_cycle747_receiver_success_gate_adapter_2026_07_30.py"
NOTE_PATH = (
    "docs/CYCLE332_RECEIVER_SUCCESS_CYCLE610_GATE_ADAPTER_"
    "BOUNDED_THEOREM_NOTE_2026-07-30.md"
)
AUDIT_INPUT_PATHS = (
    "docs/CYCLE332_RECEIVER_SUCCESS_CYCLE610_GATE_ADAPTER_BOUNDED_THEOREM_NOTE_2026-07-30.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/ROUTE2_LOCAL_GAUGE_CAR_COMPILER_CYCLE232_2026_07_17.py",
    "scripts/active_cubic_source_response_cycle211_2026_07_16.py",
    "scripts/archive_carrier_source_ledger_cycle227_2026_07_17.py",
    "scripts/autonomous_cubic_field_emission_cycle214_2026_07_16.py",
    "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py",
    "scripts/connected_edge_autonomous_apparatus_law_cycle282_2026_07_17.py",
    "scripts/connected_edge_same_code_local_instrument_cycle278_2026_07_17.py",
    "scripts/contact_close_typed_record_dag_cycle287_2026_07_17.py",
    "scripts/contractible_lightcone_wilson_quotient_cycle271_2026_07_17.py",
    "scripts/exact_3d_higher_form_bosonization_cycle235_2026_07_17.py",
    "scripts/finite_coin_scalar_wave_dilation_cycle215_2026_07_16.py",
    "scripts/fock_modular_boundary_current_cycle229_2026_07_17.py",
    "scripts/frontier_cycle747_receiver_success_gate_adapter_2026_07_30.py",
    "scripts/local_conservative_commit_resource_gravity_cycle9_2026_07_14.py",
    "scripts/local_generator_source_tournament_cycle228_2026_07_17.py",
    "scripts/locally_matched_wilson_sector_states_cycle275_2026_07_17.py",
    "scripts/matter_coupling_faithful_close_record_candidate_cycle281_2026_07_17.py",
    "scripts/outgoing_carrier_nonrecurrence_cycle286_2026_07_17.py",
    "scripts/physical_autonomous_localized_refocused_matter_transition_tournament_cycle575_2026_07_22.py",
    "scripts/physical_contact_dimer_infinite_internal_content_tournament_cycle583_2026_07_22.py",
    "scripts/physical_cycle269_coherent_cubic_pair_orbit_2026_07_17.py",
    "scripts/physical_cycle269_coin_stream_contact_common_refinement_cycle304_2026_07_17.py",
    "scripts/physical_cycle269_collision_safe_auxiliary_ports_2026_07_17.py",
    "scripts/physical_cycle269_common_m64_fixed_seam_cycle311_2026_07_18.py",
    "scripts/physical_cycle269_full_two_particle_sector_interface_cycle305_2026_07_17.py",
    "scripts/physical_cycle269_higher_number_fixed_seam_cycle308_2026_07_17.py",
    "scripts/physical_cycle269_joint_six_mode_coin_lift_cycle302_2026_07_17.py",
    "scripts/physical_cycle269_local_contact_intertwiner_2026_07_17.py",
    "scripts/physical_cycle269_local_fock_extension_cycle312_2026_07_18.py",
    "scripts/physical_cycle269_position_growing_recurrent_compiler_cycle307_2026_07_17.py",
    "scripts/physical_cycle269_reference_relative_localized_pair_lift_2026_07_17.py",
    "scripts/physical_cycle269_staggered_reservoir_catchup_2026_07_17.py",
    "scripts/physical_event_to_append_commit_candidate_cycle326_2026_07_18.py",
    "scripts/physical_intrinsic_contact_bound_moving_transition_tournament_cycle578_2026_07_22.py",
    "scripts/physical_intrinsic_tick_event_relational_duration_tournament_cycle610_2026_07_22.py",
    "scripts/physical_m64_reversible_event_sidecar_cycle314_2026_07_18.py",
    "scripts/physical_matter_transition_clock_equivalence_tournament_cycle573_2026_07_22.py",
    "scripts/physical_support_matcher_predecessor_controls_cycle329_2026_07_18.py",
    "scripts/physical_tick_echo_association_causal_order_tournament_cycle612_2026_07_22.py",
    "scripts/physical_transition_occurrence_close_tournament_cycle332_2026_07_18.py",
    "scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py",
    "scripts/retarded_cubic_mass_field_cycle213_2026_07_16.py",
    "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py",
    "scripts/virtual_exchange_green_kernel_cycle216_2026_07_16.py",
    "scripts/wilson_subsystem_sector_free_compiler_cycle269_2026_07_17.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from hashlib import sha256
from itertools import product
import json
import os
from pathlib import Path
import subprocess
import sys
from time import perf_counter


ROOT = Path(__file__).resolve().parents[1]
SOURCE_PINS = {
    "scripts/physical_event_to_append_commit_candidate_cycle326_2026_07_18.py":
        "8762609f9e9e85fb9311ed467bbc91fd5905f2ac5d160997555e8623c5e7f44c",
    "scripts/physical_intrinsic_tick_event_relational_duration_tournament_cycle610_2026_07_22.py":
        "36fcb1655bbdcd758b69ea1e273821e5c820f738eb63199570c8f36c7e294bac",
    "scripts/physical_support_matcher_predecessor_controls_cycle329_2026_07_18.py":
        "2cf6370f72cd4025fcfba8f0edefff1c577ad2bf5c5b93f996ef23c5affbab0b",
    "scripts/physical_transition_occurrence_close_tournament_cycle332_2026_07_18.py":
        "de7883fe45ce248427e8e44294d77fce56394e5ed14724e9056a65b43e0a4415",
}
PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def digest(relative: str) -> str:
    return sha256((ROOT / relative).read_bytes()).hexdigest()


def progressive_certificate(values: tuple[int, ...]) -> int:
    """Independent fresh-rail reconstruction of a five-stage certificate."""

    rail = [1] + [0] * len(values)
    for index, value in enumerate(values):
        rail[index + 1] ^= rail[index] & value
    return rail[-1]


def controlled_close(
    event_ready: int,
    match: int,
    ready: int,
    transition: int,
    certificate: int,
) -> tuple[int, int]:
    """Independent seven-bit permutation reconstruction on fresh/candidate."""

    fresh, candidate = 1, 0
    if all((event_ready, match, ready, transition, certificate)):
        fresh, candidate = candidate, fresh
    return fresh, candidate


def receiver_model(bits: tuple[int, ...]) -> tuple[int, int]:
    event_ready, pre_code, post_code, match, ready, transition = bits
    certificate = progressive_certificate(
        (pre_code, transition, post_code, match, ready)
    )
    receiver = int(
        controlled_close(
            event_ready,
            match,
            ready,
            transition,
            certificate,
        )
        == (0, 1)
    )
    return receiver, certificate


def admission_model(
    *,
    certificate: int,
    binder: int,
    actuality: int,
    admissibility: int,
    law_domain: int,
    fresh: int,
    capacity: int,
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


def independent_receiver_table() -> dict[str, object]:
    mismatches = 0
    certificate_ones = 0
    receiver_ones = 0
    for bits in product((0, 1), repeat=6):
        receiver, certificate = receiver_model(bits)
        expected = 1
        for value in bits:
            expected &= value
        mismatches += receiver != expected
        certificate_ones += certificate
        receiver_ones += receiver
    return {
        "rows": 64,
        "mismatches": mismatches,
        "certificate_ones": certificate_ones,
        "receiver_ones": receiver_ones,
    }


def complete_admission_table() -> dict[str, object]:
    counts: dict[str, int] = {}
    precedence_mismatches = 0
    for values in product((0, 1), repeat=7):
        certificate, binder, actuality, admissibility, law_domain, fresh, capacity = values
        observed = admission_model(
            certificate=certificate,
            binder=binder,
            actuality=actuality,
            admissibility=admissibility,
            law_domain=law_domain,
            fresh=fresh,
            capacity=capacity,
        )
        if not (certificate and binder):
            expected = "no_opportunity"
        elif not fresh:
            expected = "refused_fresh"
        elif not (actuality and admissibility and law_domain):
            expected = "refused_supplied"
        elif not capacity:
            expected = "exhausted"
        else:
            expected = "admitted"
        precedence_mismatches += observed != expected
        counts[observed] = counts.get(observed, 0) + 1
    adapter_rows = {
        str(bit): admission_model(
            certificate=1,
            binder=1,
            actuality=1,
            admissibility=bit,
            law_domain=1,
            fresh=1,
            capacity=1,
        )
        for bit in (0, 1)
    }
    return {
        "rows": 128,
        "precedence_mismatches": precedence_mismatches,
        "status_counts": counts,
        "adapter_rows": adapter_rows,
    }


def source_and_input_contract() -> dict[str, object]:
    observed = {path: digest(path) for path in SOURCE_PINS}
    primary_source = (ROOT / PRIMARY_PATH).read_text(encoding="utf-8")
    tree = ast.parse(primary_source, filename=PRIMARY_PATH)
    assignments = [
        node
        for node in tree.body
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name) and target.id == "AUDIT_INPUT_PATHS"
            for target in node.targets
        )
    ]
    if len(assignments) != 1:
        primary_inputs: tuple[str, ...] = ()
    else:
        primary_inputs = tuple(ast.literal_eval(assignments[0].value))
    checker_inputs_without_primary = tuple(
        path for path in AUDIT_INPUT_PATHS if path != PRIMARY_PATH
    )
    note = (ROOT / NOTE_PATH).read_text(encoding="utf-8").lower()
    return {
        "pins_match": observed == SOURCE_PINS,
        "primary_inputs_match_checker": primary_inputs == checker_inputs_without_primary,
        "note_semantic_firewall": (
            "framework admissibility and objective physical admission are outside the conclusion"
            in " ".join(note.replace("`", "").replace("*", "").split())
        ),
        "observed_pins": observed,
    }


def run_primary() -> tuple[int, dict[str, object], str]:
    environment = dict(os.environ)
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    completed = subprocess.run(
        [sys.executable, PRIMARY_PATH],
        cwd=ROOT,
        env=environment,
        text=True,
        capture_output=True,
        timeout=AUDIT_TIMEOUT_SEC,
        check=False,
    )
    summaries = [
        line.removeprefix("SUMMARY_JSON ")
        for line in completed.stdout.splitlines()
        if line.startswith("SUMMARY_JSON ")
    ]
    summary = json.loads(summaries[0]) if len(summaries) == 1 else {}
    return completed.returncode, summary, completed.stderr


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    started = perf_counter()

    receiver = independent_receiver_table()
    check(
        "independent receiver reconstruction covers all 64 rows",
        receiver
        == {
            "rows": 64,
            "mismatches": 0,
            "certificate_ones": 2,
            "receiver_ones": 1,
        },
        receiver,
    )

    admission = complete_admission_table()
    check(
        "independent admission decision tree covers all 128 rows",
        admission["rows"] == 128
        and admission["precedence_mismatches"] == 0
        and admission["adapter_rows"]
        == {"0": "refused_supplied", "1": "admitted"},
        admission,
    )

    contract = source_and_input_contract()
    check(
        "source pins, cache-input closure, and note firewall are bound",
        contract["pins_match"]
        and contract["primary_inputs_match_checker"]
        and contract["note_semantic_firewall"],
        contract,
    )

    returncode, primary, stderr = run_primary()
    check(
        "primary black-box result agrees with the independent reconstruction",
        returncode == 0
        and not stderr
        and primary.get("all_pass") is True
        and primary.get("receiver_rows") == receiver["rows"]
        and primary.get("receiver_mismatches") == receiver["mismatches"]
        and primary.get("receiver_successes") == receiver["receiver_ones"]
        and primary.get("adapter_rows") == admission["adapter_rows"],
        {"returncode": returncode, "summary": primary, "stderr": stderr},
    )

    runtime = perf_counter() - started
    check(
        "runtime remains within the declared audit timeout",
        runtime <= AUDIT_TIMEOUT_SEC,
        {"runtime_sec": round(runtime, 6), "timeout_sec": AUDIT_TIMEOUT_SEC},
    )

    summary = {
        "all_pass": FAIL == 0,
        "admission_rows": admission["rows"],
        "audit_input_count": len(AUDIT_INPUT_PATHS),
        "fail": FAIL,
        "independent": True,
        "pass": PASS,
        "receiver_mismatches": receiver["mismatches"],
        "receiver_rows": receiver["rows"],
        "runtime_sec": round(runtime, 6),
        "scope": "independent finite-state reconstruction of the Boolean adapter",
    }
    print("SUMMARY_JSON", json.dumps(summary, sort_keys=True, separators=(",", ":")))
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
