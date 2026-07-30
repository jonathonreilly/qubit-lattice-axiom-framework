#!/usr/bin/env python3
"""Cycle 785: formation census on every Cycle-719 matter-origin chart.

This runner changes only the chart enumeration around Cycle 769.  Every
branch is passed through Cycle 769's compiled_branch_trace unchanged; for
nonzero origins only the returned chart labels are replaced.  No amplitude,
probability, weight, rate, or formation-totality assumption is introduced.
"""

from __future__ import annotations

from dataclasses import fields
from hashlib import sha256
import json
from pathlib import Path
import sys
from time import perf_counter


AUDIT_TIMEOUT_SEC = 1500
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_recurrent_matter_history_controller_2026_07_26.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle769_formation_census_2026_07_28.py",
    "scripts/physical_record_readout_carrier_three_way_split_cycle693_2026_07_25.py",
)
PINNED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "ef9398b3f27dcbb540446d6c5c165c5803014cffa37da59071751810a7ac9978",
    AUDIT_INPUT_PATHS[1]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[2]:
        "249a9f84eb3a89b2a261801e8e2bb15cc0ba1919a61ac6a8e4c731b3ecaedb32",
    AUDIT_INPUT_PATHS[3]:
        "d5403ebbf51d8ecfaf621d5e0983d333b8df9a7d589145095b598c530ac15ab4",
}
STDOUT_LIMIT_BYTES = 150_000

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle719_recurrent_matter_history_controller_2026_07_26 as C719
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K
import frontier_cycle769_formation_census_2026_07_28 as C769
import physical_record_readout_carrier_three_way_split_cycle693_2026_07_25 as R693


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def canonical_bytes(value: object) -> bytes:
    return compact(value).encode()


def canonical_digest(value: object) -> str:
    return sha256(canonical_bytes(value)).hexdigest()


def clean_origin_branches(origin: int) -> tuple[int, ...]:
    """The Cycle-769 branch preparation, with only matter origin generalized."""
    banks, links = C719.B.chain_genesis(C719.BANKS)
    initial_data = C719.tuple_to_int(
        C719.M.pack_state(banks, links, matter=1 << origin)
    )
    state = C719.C713.apply_sparse_word(
        {initial_data: 1.0 + 0.0j}, C719.MATTER_WORD
    )
    # As in Cycle 769, amplitudes are discarded: this is a branch census.
    return tuple(sorted(state))


def origin_catalog() -> tuple[
    list[dict[str, object]],
    dict[int, tuple[int, ...]],
    dict[str, object],
]:
    transition, evidence = C719.instrument_transition()
    families: dict[int, tuple[int, ...]] = {}
    catalog = []
    for origin in sorted(transition):
        family = clean_origin_branches(origin)
        families[origin] = family
        orientation_by_mode = {
            target: orientation
            for target, orientation, _coefficient in transition[origin]
        }
        branches = []
        for basis in family:
            mode = (basis & 4095).bit_length() - 1
            branches.append({
                "source_matter_mode": mode,
                "orientation": orientation_by_mode[mode],
                "endpoint_pointer": (
                    basis >> C719.R3_SOURCE_POINTER()
                ) & 1,
            })
        catalog.append({
            "origin": origin,
            "branch_count": len(family),
            "branches_in_physical_basis_order": branches,
            "module_evidence": {
                "function": "instrument_transition",
                "declared_source_modes": evidence["source_modes"],
                "declared_transition_entries": evidence["transition_entries"],
                "transition_failures": evidence["failures"],
                "endpoint_aux_cleanup_failures":
                    evidence["endpoint_aux_cleanup_failures"],
            },
        })
    return catalog, families, evidence


def generic_compiled_anchor_row(source_basis: int) -> dict[str, object]:
    """Apply the unchanged compiled/host/inverse anchor to one branch."""
    host_data, host_a, host_b, _trace = K.run_orbit(
        C719.int_to_tuple(source_basis), C719.PROGRAM
    )
    source_full = C719.controller_full_input(source_basis)
    observed_full = C719.repeated_fast_word(
        source_full, C719.CONTROLLER_H_FAST
    )
    observed = C719.controller_register_rows(observed_full)
    restored_full = C719.repeated_fast_word(
        observed_full, C719.CONTROLLER_H_INVERSE_FAST
    )
    return {
        "source_matter_mode": (source_basis & 4095).bit_length() - 1,
        "endpoint_pointer": (
            source_basis >> C719.R3_SOURCE_POINTER()
        ) & 1,
        "compiled_equals_host":
            observed["data"] == C719.tuple_to_int(host_data),
        "A0_return": observed["A"] == host_a
        == (1,) + (0,) * (C719.CONTROLLER_STATIONS - 1),
        "B_vacuum_return": observed["B"] == host_b
        == (0,) * C719.CONTROLLER_STATIONS,
        "work_return": not any(observed["work"]),
        "inverse_exact": restored_full == source_full,
    }


def branch_anchors(
    families: dict[int, tuple[int, ...]],
    origin_zero_anchor: dict[str, object],
) -> dict[int, dict[str, object]]:
    origin_zero_by_mode = {
        int(row["source_matter_mode"]): row
        for row in origin_zero_anchor["rows"]
    }
    anchors = {}
    origin_zero_family = set(families[0])
    for basis in sorted({basis for family in families.values() for basis in family}):
        mode = (basis & 4095).bit_length() - 1
        anchors[basis] = (
            origin_zero_by_mode[mode]
            if basis in origin_zero_family
            else generic_compiled_anchor_row(basis)
        )
    return anchors


def run_multiorigin_census(
    origins: tuple[int, ...],
    families: dict[int, tuple[int, ...]],
    anchors: dict[int, dict[str, object]],
    pointer_site: tuple[int, int, int],
) -> list[dict[str, object]]:
    rows = []
    for origin in origins:
        for source_basis in families[origin]:
            # This call is the Cycle-769 operationalization verbatim.
            row = C769.compiled_branch_trace(
                source_basis, anchors[source_basis], pointer_site
            )
            if origin:
                # Only chart metadata changes outside origin zero.
                row = dict(row)
                row["branch_key"] = (
                    f"origin{origin}->mode{row['source_matter_mode']}"
                )
                row["origin"] = origin
            rows.append(row)
    return rows


def classification_name(decisions: list[object]) -> str:
    if any(value is None for value in decisions):
        return "unidentified"
    if not any(decisions):
        return "empty"
    if all(decisions):
        return "all"
    return "structured"


def dual_classification(rows: list[dict[str, object]]) -> dict[str, object]:
    """Print both Cycle-770-v2 readings without changing Cycle 769 rows."""
    strict = [row["formation_decision"] for row in rows]
    exhaustive = [
        row["formation_decision"]
        if row["reversible_record_shaped_write"]
        else False
        for row in rows
    ]

    def evidence(decisions: list[object]) -> dict[str, object]:
        return {
            "classification": classification_name(decisions),
            "decidable_rows": sum(value is not None for value in decisions),
            "positive_rows": sum(value is True for value in decisions),
            "negative_rows": sum(value is False for value in decisions),
            "unidentified_rows": sum(value is None for value in decisions),
        }

    return {
        "reading_1_exhaustive_no_write_counts_as_negative": {
            **evidence(exhaustive),
            "discipline": (
                "an exhaustively censused branch with no record-shaped write "
                "is counted negative on this reading"
            ),
        },
        "reading_2_no_write_does_not_count_as_negative_evidence": {
            **evidence(strict),
            "discipline": (
                "Cycle 769 verbatim: negative requires a landed nonformation "
                "witness; no-write alone does not supply it"
            ),
        },
    }


def nonzero_sector_controls(origin: int) -> dict[str, object]:
    """Cycle-719 lawful/hostile token controls on a nonzero origin chart."""
    banks, links = C719.B.chain_genesis(C719.BANKS)
    initial = {
        C719.tuple_to_int(
            C719.M.pack_state(banks, links, matter=1 << origin)
        ): 1.0 + 0.0j
    }
    matter = C719.C713.apply_sparse_word(initial, C719.MATTER_WORD)
    lawful, lawful_row = C719.sparse_controller_orbit(matter, C719.PROGRAM)
    zero, zero_row = C719.sparse_controller_orbit(
        matter, C719.PROGRAM, token_positions=()
    )
    adjacent, adjacent_row = C719.sparse_controller_orbit(
        matter, C719.PROGRAM, token_positions=(0, 1)
    )
    distant, distant_row = C719.sparse_controller_orbit(
        matter, C719.PROGRAM,
        token_positions=(0, len(C719.PROGRAM) // 2),
    )
    offset, offset_row = C719.sparse_controller_orbit(
        matter, C719.PROGRAM, token_positions=(1,)
    )
    restored, restored_row = C719.sparse_controller_orbit(
        lawful, C719.PROGRAM, reverse=True
    )
    return {
        "origin": origin,
        "lawful_token_return_failures": (
            lawful_row["token_return_failures"]
            + lawful_row["B_vacuum_return_failures"]
        ),
        "lawful_inverse_residual": C719.state_residual(restored, matter),
        "lawful_inverse_token_failures": (
            restored_row["token_return_failures"]
            + restored_row["B_vacuum_return_failures"]
        ),
        "zero_token_data_residual_from_unallocated_matter":
            C719.state_residual(zero, matter),
        "zero_token_residual_from_lawful":
            C719.state_residual(zero, lawful),
        "adjacent_two_token_residual_from_lawful":
            C719.state_residual(adjacent, lawful),
        "distant_two_token_residual_from_lawful":
            C719.state_residual(distant, lawful),
        "offset_token_residual_from_lawful":
            C719.state_residual(offset, lawful),
        "hostile_token_return_failures": sum(
            row["token_return_failures"] + row["B_vacuum_return_failures"]
            for row in (
                zero_row, adjacent_row, distant_row, offset_row
            )
        ),
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

    # Verbatim Cycle-769 operationalization.
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

    actual_sha256 = {
        path: sha256((ROOT / path).read_bytes()).hexdigest()
        for path in AUDIT_INPUT_PATHS
    }
    catalog, families, instrument_evidence = origin_catalog()
    origins = tuple(row["origin"] for row in catalog)
    origin_zero_anchor = C719.compiled_H_orbit_certificate()
    anchors = branch_anchors(families, origin_zero_anchor)

    first_started = perf_counter()
    first_census = run_multiorigin_census(
        origins, families, anchors, pointer_site
    )
    first_elapsed = perf_counter() - first_started
    second_census = run_multiorigin_census(
        origins, families, anchors, pointer_site
    )
    first_digest = canonical_digest(first_census)
    second_digest = canonical_digest(second_census)

    # The control calls the landed Cycle-769 run_census itself.
    cycle769_origin_zero = C769.run_census(
        origin_zero_anchor, pointer_site
    )
    origin_zero_rows = [
        row for row in first_census if row["origin"] == 0
    ]
    origin_zero_bytes = canonical_bytes(origin_zero_rows)
    cycle769_origin_zero_bytes = canonical_bytes(cycle769_origin_zero)
    identity_pass = origin_zero_bytes == cycle769_origin_zero_bytes

    rows_by_origin = {
        origin: [
            row for row in first_census if row["origin"] == origin
        ]
        for origin in origins
    }
    structure_rows = []
    classification_rows = []
    for origin in origins:
        rows = rows_by_origin[origin]
        record_rows = [
            row for row in rows
            if row["reversible_record_shaped_write"]
        ]
        structure_rows.append({
            "origin": origin,
            "record_shaped_branch_count": len(record_rows),
            "record_shaped_modes": [
                row["source_matter_mode"] for row in record_rows
            ],
            "data_write_steps": [
                point["orbit_step"]
                for row in record_rows
                for point in row["data_write_points"]
            ],
            "record_pipeline_steps": [
                point["orbit_step"]
                for row in record_rows
                for point in row["record_cell_pipeline_points"]
            ],
            "decoded_cell_content": [
                cell
                for row in record_rows
                for cell in row["decoded_EventCell_rows"]
            ],
        })
        formation_class, formation_evidence = (
            C769.classify_formation_census(rows)
        )
        classification_rows.append({
            "origin": origin,
            "verbatim_769": {
                "classification": formation_class,
                **formation_evidence,
            },
            "dual_reading_770_v2": dual_classification(rows),
        })

    record_rows = [
        row for row in first_census
        if row["reversible_record_shaped_write"]
    ]
    write_step_distribution: dict[str, int] = {}
    for row in record_rows:
        for point in row["data_write_points"]:
            key = str(point["orbit_step"])
            write_step_distribution[key] = (
                write_step_distribution.get(key, 0) + 1
            )
    pipeline_step_distribution: dict[str, int] = {}
    for row in record_rows:
        for point in row["record_cell_pipeline_points"]:
            key = str(point["orbit_step"])
            pipeline_step_distribution[key] = (
                pipeline_step_distribution.get(key, 0) + 1
            )
    cross_origin = {
        "origins_censused": len(origins),
        "branches_censused": len(first_census),
        "record_shaped_branches_total": len(record_rows),
        "record_shaped_branches_per_origin": {
            str(row["origin"]): row["record_shaped_branch_count"]
            for row in structure_rows
        },
        "record_shaped_modes_per_origin": {
            str(row["origin"]): row["record_shaped_modes"]
            for row in structure_rows
        },
        "record_shaped_data_write_step_distribution":
            write_step_distribution,
        "record_pipeline_step_distribution":
            pipeline_step_distribution,
        "origin_zero_pattern_assessment": (
            "universal exactly-one-record-shaped-branch count; varying endpoint "
            "role: mode 6 with orientation +1 on origins 0-5, mode 1 with "
            "orientation -1 on origins 6-11"
        ),
        "mode_6_role_universal": False,
        "exactly_one_record_shaped_branch_per_origin": all(
            row["record_shaped_branch_count"] == 1
            for row in structure_rows
        ),
    }
    global_formation_class, global_formation_evidence = (
        C769.classify_formation_census(first_census)
    )
    global_classification = {
        "verbatim_769": {
            "classification": global_formation_class,
            **global_formation_evidence,
        },
        "dual_reading_770_v2":
            dual_classification(first_census),
    }

    sectors = nonzero_sector_controls(6)
    refusal = C719.local_refusal_primitive()

    compiled_anchor_pass = (
        origin_zero_anchor["Cycle713_origin0_branches"] == 6
        and origin_zero_anchor["semantic_gates_per_H"] == 61562
        and origin_zero_anchor["H_applications_per_orbit"] == 130
        and origin_zero_anchor[
            "semantic_gate_applications_per_branch"
        ] == 8003060
        and origin_zero_anchor["compiled_host_equality_failures"] == 0
        and origin_zero_anchor["compiled_inverse_failures"] == 0
        and origin_zero_anchor[
            "controller_register_return_failures"
        ] == 0
        and origin_zero_anchor["suffix_decoded_domain_failures"] == 0
        and origin_zero_anchor[
            "compiled_packet_deletion_data_bit_differences"
        ] == 35
        and origin_zero_anchor[
            "compiled_finalizer_deletion_data_bit_differences"
        ] == 3
        and origin_zero_anchor[
            "compiled_source_handoff_deletion_data_bit_differences"
        ] > 0
    )
    catalog_pass = (
        instrument_evidence == {
            "source_modes": 12,
            "transition_entries": 72,
            "failures": 0,
            "endpoint_aux_cleanup_failures": 0,
        }
        and origins == tuple(range(12))
        and len(catalog) == 12
        and all(row["branch_count"] == 6 for row in catalog)
        and sum(row["branch_count"] for row in catalog) == 72
    )
    operationalization_pass = (
        record_fields == ("site", "content")
        and event_cell_fields == (
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
        and not operationalization[
            "R693_available_and_trace_are_formation_tests"
        ]
        and not operationalization[
            "supplied_acceptance_flags_are_formation_tests"
        ]
    )
    row_keys = set(cycle769_origin_zero[0])
    census_pass = (
        len(first_census) == 72
        and all(set(row) == row_keys for row in first_census)
        and all(row["lawful_compiled_branch"] for row in first_census)
        and all(row["compiled_equals_host"] for row in first_census)
        and all(row["A0_return"] for row in first_census)
        and all(row["B_vacuum_return"] for row in first_census)
        and all(row["work_return"] for row in first_census)
        and all(row["inverse_exact_anchor"] for row in first_census)
        and all(
            row["formation_witness"]["positive_permanent_lock"] is None
            and row["formation_witness"]["negative_nonformation"] is None
            and row["formation_decision"] is None
            and row["durable_permanent_record_write"] is None
            for row in first_census
        )
    )
    expected_modes = {
        origin: ([6] if origin < 6 else [1])
        for origin in origins
    }
    structure_pass = (
        len(record_rows) == 12
        and all(
            row["record_shaped_branch_count"] == 1
            and row["record_shaped_modes"]
            == expected_modes[row["origin"]]
            and row["data_write_steps"] == [0, 1, 125]
            and row["record_pipeline_steps"] == [1, 125]
            and len(row["decoded_cell_content"]) == 1
            and row["decoded_cell_content"][0]["binder"] == 1
            and row["decoded_cell_content"][0]["valid"] == 1
            and row["decoded_cell_content"][0]["orientation"]
            == (1 if row["origin"] < 6 else -1)
            for row in structure_rows
        )
        and write_step_distribution
        == {"0": 12, "1": 12, "125": 12}
        and pipeline_step_distribution == {"1": 12, "125": 12}
    )
    classification_pass = (
        global_formation_class == "unidentified"
        and global_formation_evidence["unidentified_rows"] == 72
        and all(
            row["verbatim_769"]["classification"] == "unidentified"
            and row["verbatim_769"]["unidentified_rows"] == 6
            and row["dual_reading_770_v2"][
                "reading_1_exhaustive_no_write_counts_as_negative"
            ]["negative_rows"] == 5
            and row["dual_reading_770_v2"][
                "reading_1_exhaustive_no_write_counts_as_negative"
            ]["unidentified_rows"] == 1
            and row["dual_reading_770_v2"][
                "reading_2_no_write_does_not_count_as_negative_evidence"
            ]["unidentified_rows"] == 6
            for row in classification_rows
        )
        and global_classification["dual_reading_770_v2"][
            "reading_1_exhaustive_no_write_counts_as_negative"
        ]["negative_rows"] == 60
        and global_classification["dual_reading_770_v2"][
            "reading_1_exhaustive_no_write_counts_as_negative"
        ]["unidentified_rows"] == 12
        and global_classification["dual_reading_770_v2"][
            "reading_2_no_write_does_not_count_as_negative_evidence"
        ]["unidentified_rows"] == 72
    )
    sector_pass = (
        sectors["origin"] == 6
        and sectors["lawful_token_return_failures"] == 0
        and sectors["lawful_inverse_residual"] < C719.TOL
        and sectors["lawful_inverse_token_failures"] == 0
        and sectors[
            "zero_token_data_residual_from_unallocated_matter"
        ] < C719.TOL
        and sectors["zero_token_residual_from_lawful"] > 1e-3
        and sectors[
            "adjacent_two_token_residual_from_lawful"
        ] > 1e-3
        and sectors[
            "distant_two_token_residual_from_lawful"
        ] > 1e-3
        and sectors["offset_token_residual_from_lawful"] > 1e-3
        and sectors["hostile_token_return_failures"] == 0
        and refusal["truth_failures"] == refusal["route_failures"] == 0
        and refusal["invalid_live_token_rows_refused"] == 6
    )
    determinism_pass = (
        first_census == second_census
        and first_digest == second_digest
    )
    sha_pass = actual_sha256 == PINNED_SHA256
    coverage = {
        "declared_origins": len(catalog),
        "censused_origins": len(origins),
        "declared_branches": sum(
            row["branch_count"] for row in catalog
        ),
        "censused_branches": len(first_census),
        "partial": False,
        "statement": (
            "full declared 12-origin/72-branch catalog censused; no prefix "
            "reduction required"
        ),
        "measured_first_census_sec": first_elapsed,
        "measured_sec_per_branch": first_elapsed / len(first_census),
    }
    coverage_pass = (
        not coverage["partial"]
        and coverage["declared_origins"] == coverage["censused_origins"]
        and coverage["declared_branches"] == coverage["censused_branches"]
    )

    runtime_sec = perf_counter() - started
    payload_lines = [
        "OPERATIONALIZATION " + compact(operationalization),
        "SHA_ANCHORS " + compact({
            "audit_input_paths": AUDIT_INPUT_PATHS,
            "actual_sha256": actual_sha256,
            "pinned_sha256": PINNED_SHA256,
            "controller_H_word_sha256":
                origin_zero_anchor["controller_H_word_sha256"],
        }),
        "ORIGIN_CATALOG " + compact(catalog),
    ]
    payload_lines.extend(
        "CENSUS_ROW " + compact(row) for row in first_census
    )
    payload_lines.extend(
        "STRUCTURE_ROW " + compact(row) for row in structure_rows
    )
    payload_lines.extend(
        "CLASSIFICATION_ROW " + compact(row)
        for row in classification_rows
    )
    payload_lines.extend([
        "CROSS_ORIGIN_AGGREGATE " + compact(cross_origin),
        "GLOBAL_CLASSIFICATION " + compact(global_classification),
        "ORIGIN0_IDENTITY " + compact({
            "byte_match": identity_pass,
            "cycle769_bytes": len(cycle769_origin_zero_bytes),
            "cycle785_origin0_bytes": len(origin_zero_bytes),
            "cycle769_sha256": sha256(
                cycle769_origin_zero_bytes
            ).hexdigest(),
            "cycle785_origin0_sha256": sha256(
                origin_zero_bytes
            ).hexdigest(),
        }),
        "NONZERO_ORIGIN_SECTOR_CONTROLS " + compact({
            "controller": sectors,
            "local_refusal": refusal,
        }),
        "DETERMINISM " + compact({
            "first_census_sha256": first_digest,
            "rerun_census_sha256": second_digest,
            "exactly_equal": determinism_pass,
        }),
        "COVERAGE " + compact(coverage),
        "RUNTIME " + compact({
            "runtime_sec": runtime_sec,
            "limit_sec": AUDIT_TIMEOUT_SEC,
        }),
    ])

    certificate_conditions = {
        "A": sha_pass and compiled_anchor_pass and catalog_pass,
        "B": operationalization_pass and census_pass,
        "C": identity_pass,
        "D": structure_pass and classification_pass,
    }
    nonstdout_e_pass = (
        sector_pass
        and determinism_pass
        and coverage_pass
        and runtime_sec < AUDIT_TIMEOUT_SEC
    )
    stdout_bytes = 0
    final_lines = payload_lines
    for _iteration in range(12):
        stdout_pass = stdout_bytes < STDOUT_LIMIT_BYTES
        certificate_conditions["E"] = nonstdout_e_pass and stdout_pass
        details = {
            "A": {
                "anchors": sha_pass and compiled_anchor_pass,
                "origin_catalog": catalog_pass,
                "origins": len(origins),
                "branches": len(first_census),
            },
            "B": {
                "all_769_format_rows_lawful": census_pass,
                "operationalization_verbatim": operationalization_pass,
            },
            "C": {
                "origin0_byte_match_cycle769": identity_pass,
                "sha256": sha256(origin_zero_bytes).hexdigest(),
            },
            "D": {
                "structure": structure_pass,
                "classification": classification_pass,
                "global": global_formation_class,
            },
            "E": {
                "nonzero_sector_controls": sector_pass,
                "determinism": determinism_pass,
                "full_coverage": coverage_pass,
                "runtime_sec": runtime_sec,
                "runtime_under_1500s": runtime_sec < AUDIT_TIMEOUT_SEC,
                "stdout_bytes": stdout_bytes,
                "stdout_under_150KB": stdout_pass,
            },
        }
        certificate_lines = [
            (
                ("PASS" if certificate_conditions[name] else "FAIL")
                + f" CERTIFICATE_{name} :: "
                + compact(details[name])
            )
            for name in ("A", "B", "C", "D", "E")
        ]
        final_lines = payload_lines + certificate_lines
        next_size = sum(
            len(line.encode()) + 1 for line in final_lines
        )
        if next_size == stdout_bytes:
            break
        stdout_bytes = next_size

    # Rebuild once with the converged exact size.
    stdout_pass = stdout_bytes < STDOUT_LIMIT_BYTES
    certificate_conditions["E"] = nonstdout_e_pass and stdout_pass
    certificate_details = {
        "A": {
            "anchors": sha_pass and compiled_anchor_pass,
            "origin_catalog": catalog_pass,
            "origins": len(origins),
            "branches": len(first_census),
        },
        "B": {
            "all_769_format_rows_lawful": census_pass,
            "operationalization_verbatim": operationalization_pass,
        },
        "C": {
            "origin0_byte_match_cycle769": identity_pass,
            "sha256": sha256(origin_zero_bytes).hexdigest(),
        },
        "D": {
            "structure": structure_pass,
            "classification": classification_pass,
            "global": global_formation_class,
        },
        "E": {
            "nonzero_sector_controls": sector_pass,
            "determinism": determinism_pass,
            "full_coverage": coverage_pass,
            "runtime_sec": runtime_sec,
            "runtime_under_1500s": runtime_sec < AUDIT_TIMEOUT_SEC,
            "stdout_bytes": stdout_bytes,
            "stdout_under_150KB": stdout_pass,
        },
    }
    certificate_lines = [
        (
            ("PASS" if certificate_conditions[name] else "FAIL")
            + f" CERTIFICATE_{name} :: "
            + compact(certificate_details[name])
        )
        for name in ("A", "B", "C", "D", "E")
    ]
    final_lines = payload_lines + certificate_lines
    exact_stdout_bytes = sum(
        len(line.encode()) + 1 for line in final_lines
    )
    if exact_stdout_bytes != stdout_bytes:
        raise AssertionError((exact_stdout_bytes, stdout_bytes))

    print("\n".join(final_lines))
    return 0 if all(certificate_conditions.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
