#!/usr/bin/env python3
"""Cycle 769: census first-event Record formation before any rate law.

The bounded universe is exactly the six origin-zero branches on which Cycle
719 executes its compiled controller word.  This runner separates three
questions that the landed surfaces keep distinct:

* did the controller data change and leave a decoded EventCell;
* is that output shaped like the landed Record/accepted-cell surfaces; and
* is there a physical permanence/locking witness that makes it a Record?

The first two questions are executable.  The third is not answered by the
reversible Cycle-719 history surface.  Consequently, an absent positive
witness is retained as ``None`` rather than silently changed to nonformation.
No endpoint-column sweep, probability, fit, time denominator, or rate law is
performed.
"""

from __future__ import annotations

from dataclasses import fields
from hashlib import sha256
import json
from pathlib import Path
import sys
from time import perf_counter


AUDIT_TIMEOUT_SEC = 1800
NOTE_PATH = "docs/FORMATION_CENSUS_CYCLE769_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/physical_record_readout_carrier_three_way_split_cycle693_2026_07_25.py",
    "scripts/frontier_cycle719_recurrent_matter_history_controller_2026_07_26.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_record_readout_carrier_three_way_split_cycle693_2026_07_25 as R693
import frontier_cycle719_recurrent_matter_history_controller_2026_07_26 as C719
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


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


def canonical_digest(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)
    return sha256(encoded.encode()).hexdigest()


def decoded_cell_surface(data_basis: int) -> dict[str, object]:
    """Read the landed accepted-cell surface, retaining dirty intermediates."""
    banks, links = C719.M.unpack_state(C719.int_to_tuple(data_basis), C719.BANKS)
    try:
        chain, order = C719.B.decode_local_graph(banks, links)
    except ValueError as error:
        return {
            "acceptance_readable": False,
            "cell_rows": [],
            "decode_order": [],
            "decode_refusal": str(error),
        }
    return {
        "acceptance_readable": True,
        "cell_rows": C719.B.cell_rows(chain),
        "decode_order": order,
        "decode_refusal": None,
    }


def initial_origin_zero_branches() -> tuple[int, ...]:
    banks, links = C719.B.chain_genesis(C719.BANKS)
    initial_data = C719.tuple_to_int(
        C719.M.pack_state(banks, links, matter=1)
    )
    state = C719.C713.apply_sparse_word(
        {initial_data: 1.0 + 0.0j}, C719.MATTER_WORD
    )
    # Amplitudes are deliberately discarded: this is an event-indexed census,
    # not a probability or weight calculation.
    return tuple(sorted(state))


def compiled_branch_trace(
    source_basis: int,
    anchor_row: dict[str, object],
    pointer_site: tuple[int, int, int],
) -> dict[str, object]:
    """Trace the literal compiled H word through all 130 circuit ordinals."""
    source_mode = (source_basis & 4095).bit_length() - 1
    full = C719.controller_full_input(source_basis)
    data_writes = []
    record_pipeline = []

    for orbit_step in range(C719.CONTROLLER_STATIONS):
        before_registers = C719.controller_register_rows(full)
        live_a = tuple(
            index for index, value in enumerate(before_registers["A"]) if value
        )
        before_data = int(before_registers["data"])
        full = C719.apply_fast_int(full, C719.CONTROLLER_H_FAST)
        after_registers = C719.controller_register_rows(full)
        after_data = int(after_registers["data"])
        if before_data == after_data:
            continue

        station = live_a[0] if len(live_a) == 1 else None
        program_kind = (
            C719.PROGRAM[station][0] if station is not None else "invalid-sector"
        )
        program_index = (
            C719.PROGRAM[station][1] if station is not None else None
        )
        decoded_after = decoded_cell_surface(after_data)
        point = {
            "orbit_step": orbit_step,
            "live_A_station": station,
            "program_kind": program_kind,
            "program_index": program_index,
            "changed_data_bits": (before_data ^ after_data).bit_count(),
            "accepted_cell_readable_after": decoded_after["acceptance_readable"],
            "accepted_cell_rows_after": decoded_after["cell_rows"],
            "decode_refusal_after": decoded_after["decode_refusal"],
        }
        data_writes.append(point)

        if program_kind == "bank":
            record_pipeline.append({
                "orbit_step": orbit_step,
                "program_kind": program_kind,
                "role": "packet_payload_written_to_bank; auxiliaries still dirty",
                "accepted_cell_readable_after": False,
            })
        if decoded_after["cell_rows"]:
            record_pipeline.append({
                "orbit_step": orbit_step,
                "program_kind": program_kind,
                "role": "accepted EventCell becomes exactly decodable after finalizer",
                "accepted_cell_readable_after": True,
                "cell_rows": decoded_after["cell_rows"],
            })

    observed = C719.controller_register_rows(full)
    observed_data = int(observed["data"])
    host_data, host_a, host_b, _trace = K.run_orbit(
        C719.int_to_tuple(source_basis), C719.PROGRAM
    )
    decoded = decoded_cell_surface(observed_data)
    cell_rows = list(decoded["cell_rows"])
    accepted_equivalent = bool(cell_rows) and all(
        row["binder"] == row["valid"] == 1 for row in cell_rows
    )

    # The compiled inverse is an unchanged Cycle-719 anchor.  It establishes
    # reversibility, not permanence; therefore neither a positive nor a
    # negative formation witness is manufactured here.
    formation_witness = {
        "positive_permanent_lock": None,
        "negative_nonformation": None,
        "decision": None,
        "reason": (
            "The landed output is exactly invertible reversible packet history; "
            "no physical permanence/locking Record bridge is supplied."
        ),
    }
    return {
        "branch_key": f"origin0->mode{source_mode}",
        "origin": 0,
        "source_matter_mode": source_mode,
        "candidate_record_site": pointer_site,
        "R693_six_neighbor_pattern": None,
        "R693_neighbor_reason": (
            "Cycle719 supplies no R693 six-neighbor occupancy on this chart."
        ),
        "endpoint_pointer_antecedent": (
            source_basis >> C719.R3_SOURCE_POINTER()
        ) & 1,
        "lawful_compiled_branch": bool(
            anchor_row["compiled_equals_host"]
            and anchor_row["A0_return"]
            and anchor_row["B_vacuum_return"]
            and anchor_row["work_return"]
            and anchor_row["inverse_exact"]
        ),
        "conditioning_is_supplied_not_formation": {
            "BINDER": 1,
            "ACTUAL": 1,
            "ADMISS": 1,
            "LAW": 1,
            "clean_bank_link_route_genesis": True,
            "token_sector": "one A0 token; B/work vacuum",
            "local_refusal_truth": "A AND NOT (B OR work)",
        },
        "compiled_equals_host": observed_data == C719.tuple_to_int(host_data),
        "A0_return": observed["A"] == host_a
        == (1,) + (0,) * (C719.CONTROLLER_STATIONS - 1),
        "B_vacuum_return": observed["B"] == host_b
        == (0,) * C719.CONTROLLER_STATIONS,
        "work_return": not any(observed["work"]),
        "inverse_exact_anchor": bool(anchor_row["inverse_exact"]),
        "data_write_points": data_writes,
        "record_cell_pipeline_points": record_pipeline,
        "decoded_EventCell_rows": cell_rows,
        "accepted_cell_equivalent_present": accepted_equivalent,
        "reversible_record_shaped_write": accepted_equivalent,
        "durable_permanent_record_write": None,
        "formation_witness": formation_witness,
        "formation_decision": None,
    }


def run_census(
    compiled_anchor: dict[str, object],
    pointer_site: tuple[int, int, int],
) -> list[dict[str, object]]:
    anchor_by_mode = {
        int(row["source_matter_mode"]): row
        for row in compiled_anchor["rows"]
    }
    return [
        compiled_branch_trace(
            source_basis,
            anchor_by_mode[(source_basis & 4095).bit_length() - 1],
            pointer_site,
        )
        for source_basis in initial_origin_zero_branches()
    ]


def classify_formation_census(
    rows: list[dict[str, object]],
) -> tuple[str, dict[str, object]]:
    decisions = [row["formation_decision"] for row in rows]
    if any(value is None for value in decisions):
        classification = "unidentified"
    elif not any(decisions):
        classification = "empty"
    elif all(decisions):
        classification = "all"
    else:
        classification = "structured"
    return classification, {
        "decidable_rows": sum(value is not None for value in decisions),
        "positive_rows": sum(value is True for value in decisions),
        "negative_rows": sum(value is False for value in decisions),
        "unidentified_rows": sum(value is None for value in decisions),
        "classification_rule": {
            "empty": "every row has a landed negative nonformation witness",
            "all": "every lawful row has a landed positive permanence witness",
            "structured": (
                "positive permanence witnesses form a proper, exactly frozen subset"
            ),
            "unidentified": (
                "at least one row lacks both positive permanence and negative "
                "nonformation evidence"
            ),
        },
    }


def main() -> int:
    started = perf_counter()

    record_fields = tuple(field.name for field in fields(R693.Record))
    event_cell_fields = tuple(
        field.name for field in fields(C719.B.C704.C610.EventCell)
    )
    event_chain_fields = tuple(
        field.name for field in fields(C719.B.C704.C610.EventChain)
    )
    pointer_site = tuple(
        C719.M.R12.full_wire_layout()["wire_sites"][
            C719.R3_SOURCE_POINTER()
        ]
    )
    operationalization = {
        "R693_record_cell": {
            "type": "Record",
            "fields": record_fields,
            "site_type": "tuple[int,int,int]",
            "content_type": "M2 represented by a four-entry Matrix tuple",
        },
        "Cycle719_acceptance_locked_equivalent": {
            "type": "EventCell",
            "fields": event_cell_fields,
            "container": "EventChain",
            "container_fields": event_chain_fields,
            "accepted_shape_test": "decoded cell has binder == valid == 1",
        },
        "record_shaped_write_test": (
            "the literal compiled branch changes the controller bank pipeline "
            "and ends with an exactly decoded binder=valid=1 EventCell"
        ),
        "positive_formation_test": (
            "record-shaped output plus a physical witness that one possibility "
            "is permanently locked at its candidate site"
        ),
        "negative_formation_test": (
            "a landed witness that formation does not occur; absence of a "
            "positive witness is not such a witness"
        ),
        "reversibility_boundary": (
            "compiled exact inverse is evidence against calling the packet "
            "history a permanence witness"
        ),
        "candidate_site": pointer_site,
        "R693_available_and_trace_are_formation_tests": False,
        "supplied_acceptance_flags_are_formation_tests": False,
    }
    print("OPERATIONALIZATION", json.dumps(
        operationalization, sort_keys=True, separators=(",", ":")
    ))

    # Certificate A: call the branch surface's own literal compiled-word
    # certificate without modifying its controller, program, or six branches.
    compiled_anchor = C719.compiled_H_orbit_certificate()
    sectors = C719.controller_sector_controls()
    refusal = C719.local_refusal_primitive()
    matter = K.H.inherited_matter_certificate()
    matter_diagnostics = {
        key: matter[key]
        for key in (
            "coin_QR_residual",
            "mass_residual",
            "coin_matrix_residual",
            "FSWAP_matrix_residual",
            "onsite_64_state_contact_residual",
            "internal_depth_two_stream_residual",
            "coin_stage_residual",
            "reverse_stage_residual",
            "seam_stage_residual",
            "contact_stage_residual",
            "single_FSWAP_falsifier_residual",
        )
    }

    first_census = run_census(compiled_anchor, pointer_site)
    second_census = run_census(compiled_anchor, pointer_site)
    first_digest = canonical_digest(first_census)
    second_digest = canonical_digest(second_census)
    formation_class, classification_evidence = classify_formation_census(
        first_census
    )

    branch_keys = [row["branch_key"] for row in first_census]
    record_shaped = [
        row["branch_key"]
        for row in first_census
        if row["reversible_record_shaped_write"]
    ]
    no_record_shaped = [
        row["branch_key"]
        for row in first_census
        if not row["reversible_record_shaped_write"]
    ]
    frozen_antecedent_pattern = {
        "reversible_record_shaped_write_branches": record_shaped,
        "no_reversible_record_shaped_write_branches": no_record_shaped,
        "formation_subset": None,
        "formation_subset_reason": (
            "No row has a physical permanence/locking decision."
        ),
    }

    anchor_rows = compiled_anchor["rows"]
    anchor_modes = [row["source_matter_mode"] for row in anchor_rows]
    compiled_anchor_pass = (
        compiled_anchor["Cycle713_origin0_branches"] == 6
        and compiled_anchor["semantic_gates_per_H"] == 61562
        and compiled_anchor["H_applications_per_orbit"] == 130
        and compiled_anchor["semantic_gate_applications_per_branch"] == 8003060
        and compiled_anchor["compiled_host_equality_failures"] == 0
        and compiled_anchor["compiled_inverse_failures"] == 0
        and compiled_anchor["controller_register_return_failures"] == 0
        and compiled_anchor["suffix_decoded_domain_failures"] == 0
        and compiled_anchor["compiled_packet_deletion_data_bit_differences"] == 35
        and compiled_anchor["compiled_finalizer_deletion_data_bit_differences"] == 3
        and compiled_anchor[
            "compiled_source_handoff_deletion_data_bit_differences"
        ] > 0
        and anchor_modes == [0, 2, 3, 4, 5, 6]
        and all(
            row["compiled_equals_host"]
            and row["A0_return"]
            and row["B_vacuum_return"]
            and row["work_return"]
            and row["inverse_exact"]
            for row in anchor_rows
        )
    )
    diagnostics_pass = (
        all(
            matter_diagnostics[key] < K.H.TOL
            for key in (
                "coin_QR_residual",
                "mass_residual",
                "coin_matrix_residual",
                "FSWAP_matrix_residual",
                "onsite_64_state_contact_residual",
                "internal_depth_two_stream_residual",
                "coin_stage_residual",
                "reverse_stage_residual",
                "seam_stage_residual",
                "contact_stage_residual",
            )
        )
        and matter_diagnostics["single_FSWAP_falsifier_residual"] > 1
    )
    branch_scope_pass = (
        branch_keys
        == [
            "origin0->mode0",
            "origin0->mode2",
            "origin0->mode3",
            "origin0->mode4",
            "origin0->mode5",
            "origin0->mode6",
        ]
        and all(row["lawful_compiled_branch"] for row in first_census)
    )
    landed_write_pattern_pass = (
        record_shaped == ["origin0->mode6"]
        and no_record_shaped
        == [
            "origin0->mode0",
            "origin0->mode2",
            "origin0->mode3",
            "origin0->mode4",
            "origin0->mode5",
        ]
        and [
            point["orbit_step"]
            for row in first_census
            for point in row["data_write_points"]
        ] == [0, 1, 125]
        and first_census[-1]["decoded_EventCell_rows"]
        == [{
            "identity": 0,
            "rotor": 15,
            "carry": 0,
            "predecessor": None,
            "binder": 1,
            "valid": 1,
            "orientation": 1,
        }]
    )
    operationalization_pass = (
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
    )
    controls_pass = (
        sectors["lawful_token_return_failures"] == 0
        and sectors["lawful_inverse_residual"] < C719.TOL
        and sectors["lawful_inverse_token_failures"] == 0
        and sectors["zero_token_residual_from_lawful"] > 1e-3
        and sectors["adjacent_two_token_residual_from_lawful"] > 1e-3
        and sectors["distant_two_token_residual_from_lawful"] > 1e-3
        and sectors["offset_token_residual_from_lawful"] > 1e-3
        and refusal["truth_failures"] == refusal["route_failures"] == 0
        and refusal["invalid_live_token_rows_refused"] == 6
    )
    classification_pass = (
        formation_class == "unidentified"
        and classification_evidence["decidable_rows"] == 0
        and classification_evidence["unidentified_rows"] == 6
        and all(row["formation_decision"] is None for row in first_census)
        and all(
            row["durable_permanent_record_write"] is None
            for row in first_census
        )
    )
    determinism_pass = first_census == second_census and first_digest == second_digest

    supplies = [
        "exact six origin-zero compiled Cycle719 branches",
        "landed Cycle719 matter word, pointer site, program, and one-token controller",
        "clean bank/link/route/syndrome genesis and fresh output cells",
        "BINDER/ACTUAL/ADMISS/LAW values as conditioning inputs, not formation labels",
        "candidate Record site (-8,-1,1) for each branch",
        "owner-fixed positive witness: one possibility permanently locked at that site",
    ]
    endpoint_anchor = {
        "cited_columns": 4096,
        "role": "independent antecedent anchor only",
        "swept_by_cycle769": False,
        "joint_event_coverage_claimed": False,
    }
    census_feeds = (
        "event-ensemble support upstream of W6; supplies no weights"
    )
    honest_boundary_pass = (
        endpoint_anchor["cited_columns"] == 4096
        and not endpoint_anchor["swept_by_cycle769"]
        and not endpoint_anchor["joint_event_coverage_claimed"]
        and census_feeds
        == "event-ensemble support upstream of W6; supplies no weights"
    )

    checks = {
        "A_R693_record_surface_anchor": operationalization_pass,
        "A_compiled_six_branch_certificates_unchanged": compiled_anchor_pass,
        "A_landed_mass_contact_diagnostics_unchanged": diagnostics_pass,
        "B_operationalization_printed_from_landed_definitions": (
            operationalization_pass
            and not operationalization[
                "R693_available_and_trace_are_formation_tests"
            ]
            and not operationalization[
                "supplied_acceptance_flags_are_formation_tests"
            ]
        ),
        "C_six_branch_census_exhaustive": branch_scope_pass,
        "C_exact_reversible_write_pattern_frozen": landed_write_pattern_pass,
        "D_unidentified_class_has_exact_evidence": classification_pass,
        "E_branch_rerun_census_deterministic": determinism_pass,
        "E_lawful_and_hostile_sector_controls": controls_pass,
        "F_honest_supplies_anchor_and_W6_interface": honest_boundary_pass,
    }

    report = {
        "audit_input_paths": AUDIT_INPUT_PATHS,
        "audit_timeout_sec": AUDIT_TIMEOUT_SEC,
        "note_path": NOTE_PATH,
        "checks": checks,
        "pass": all(checks.values()),
        "certificate_A_anchors": {
            "compiled_controller": {
                key: compiled_anchor[key]
                for key in (
                    "Cycle713_origin0_branches",
                    "semantic_gates_per_H",
                    "H_applications_per_orbit",
                    "semantic_gate_applications_per_branch",
                    "compiled_host_equality_failures",
                    "compiled_inverse_failures",
                    "controller_register_return_failures",
                    "suffix_decoded_domain_failures",
                    "compiled_packet_deletion_data_bit_differences",
                    "compiled_finalizer_deletion_data_bit_differences",
                    "compiled_source_handoff_deletion_data_bit_differences",
                    "controller_H_word_sha256",
                )
            },
            "compiled_branch_rows": anchor_rows,
            "matter_diagnostics": matter_diagnostics,
            "controller_sector_controls": sectors,
            "local_refusal": refusal,
        },
        "certificate_B_operationalization": operationalization,
        "certificate_C_formation_census": first_census,
        "certificate_D_classification_evidence": classification_evidence,
        "certificate_E_determinism": {
            "first_census_sha256": first_digest,
            "rerun_census_sha256": second_digest,
            "exactly_equal": determinism_pass,
        },
        "certificate_F_honest_boundary": {
            "supplies": supplies,
            "census_feeds": census_feeds,
            "endpoint_anchor": endpoint_anchor,
            "no_rate_law": True,
            "no_probability_or_fit": True,
            "no_weights": True,
        },
        "formation_census_class": formation_class,
        "frozen_antecedent_write_pattern": frozen_antecedent_pattern,
        "supplies": supplies,
        "census_feeds": census_feeds,
        "runtime_sec": perf_counter() - started,
    }
    provisional_size = len(
        json.dumps(report, sort_keys=True, separators=(",", ":"), default=str)
        .encode()
    )
    checks["stdout_under_150KB"] = provisional_size < 145_000
    report["checks"] = checks
    report["pass"] = all(checks.values())
    report["final_json_bytes"] = len(
        json.dumps(report, sort_keys=True, separators=(",", ":"), default=str)
        .encode()
    )
    report["report_sha256"] = canonical_digest(report)

    for label, passed in checks.items():
        check(label, passed, passed)
    print(json.dumps(report, sort_keys=True, separators=(",", ":"), default=str))
    return 0 if report["pass"] and FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
