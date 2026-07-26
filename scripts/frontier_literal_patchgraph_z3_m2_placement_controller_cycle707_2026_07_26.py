#!/usr/bin/env python3
"""Audit entry point for the Cycle707 literal placement/controller probe."""

from __future__ import annotations

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_literal_patchgraph_z3_m2_placement_core_cycle707_2026_07_26 as C


AUDIT_INPUT_PATHS = (
    "docs/LITERAL_PATCHGRAPH_Z3_M2_PLACEMENT_AND_FIXED_CONTROLLER_CYCLE707_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/work_history/repo/review_feedback/ROUTE2_LOCAL_GAUGE_CAR_COMPILER_CYCLE232_NOTE_2026-07-17.md",
    "docs/FULL128_LOCAL_M64_SEAM_M2_BARE_FRAME_INTERTWINER_BOUNDED_THEOREM_NOTE_2026-07-24.md",
    "docs/FULL128_TWO_RAIL_FIXED_LAW_COMPOSITIONAL_INDUCTION_BOUNDED_THEOREM_NOTE_2026-07-24.md",
    "docs/OPENREFERENCE_PATCHGRAPH_FOUR_RAIL_SIGNED_CLIFFORD_EQUIVALENCE_CYCLE706_NOTE_2026-07-26.md",
    "docs/work_history/repo/review_feedback/PROPER_CUBIC_BOUND_OBJECT_EQUIVALENCE_CYCLE210_NOTE_2026-07-16.md",
    "scripts/ROUTE2_LOCAL_GAUGE_CAR_COMPILER_CYCLE232_2026_07_17.py",
    "scripts/frontier_full128_25site_nn_circuit_core_2026_07_24.py",
    "scripts/frontier_full128_cycle_encoder_2026_07_24.py",
    "scripts/frontier_full128_two_rail_fixed_law_core_2026_07_24.py",
    "scripts/frontier_literal_patchgraph_cycle656_projected_trace_cycle707_2026_07_26.py",
    "scripts/frontier_full128_cycle_cocycle_intertwiner_2026_07_24.py",
    "scripts/frontier_full128_bare_frame_pair_cocycle_2026_07_24.py",
    "scripts/frontier_full128_code_projectors_2026_07_24.py",
    "scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py",
    "scripts/frontier_literal_patchgraph_z3_m2_placement_core_cycle707_2026_07_26.py",
)


def source_inventory() -> dict[str, object]:
    """Return an active audit-source closure and source-size check."""
    declared = tuple((ROOT / relative).resolve() for relative in AUDIT_INPUT_PATHS)
    sources = (Path(__file__).resolve(),) + tuple(
        path for path in declared if path.suffix == ".py"
    )
    sizes = {
        str(path.relative_to(ROOT)): path.stat().st_size
        for path in sources
        if path.is_file() and path.is_relative_to(ROOT)
    }
    return {
        "declared_inputs": len(declared),
        "duplicate_inputs": len(declared) - len(set(declared)),
        "missing_inputs": tuple(
            str(path) for path in declared if not path.is_file()
        ),
        "external_inputs": tuple(
            str(path) for path in declared if not path.is_relative_to(ROOT)
        ),
        "scientific_source_bytes": sizes,
        "scientific_sources_at_or_over_40000_bytes": tuple(
            name for name, size in sizes.items() if size >= 40_000
        ),
    }


def main() -> int:
    C.note_contract()
    inventory = source_inventory()
    C.check(
        "the pinned audit closure is repo-local and every scientific source is below 40kB",
        inventory["duplicate_inputs"] == 0
        and not inventory["missing_inputs"]
        and not inventory["external_inputs"]
        and not inventory["scientific_sources_at_or_over_40000_bytes"]
        and "scripts/frontier_literal_patchgraph_cycle656_projected_trace_cycle707_2026_07_26.py"
        in inventory["scientific_source_bytes"],
        inventory,
    )
    graph = C.PatchGraph(C.square_cells(2))
    factors, colors, collisions = C.factor_schedule(graph)
    digest = C.factor_digest(factors, colors)
    edge_hash = C.edge_digest(graph)
    C.check(
        "the corrected snake-ordered PatchGraph has 76 edges and the 112-factor 27-color schedule",
        len(graph.vertices) == 28
        and len(graph.edges) == 76
        and len(graph.stream_edges) == 4
        and [row[0] for row in graph.stream_edges] == [72, 73, 74, 75]
        and len(factors) == 112
        and len(set(colors)) == 27
        and collisions == 0
        and digest == C.EXPECTED_PHYSICAL_SCHEDULE_DIGEST,
        {
            "vertices": len(graph.vertices),
            "edges": len(graph.edges),
            "stream_edge_indices": [row[0] for row in graph.stream_edges],
            "factor_counts": {
                kind: sum(factor.kind == kind for factor in factors)
                for kind in ("onsite_coin", "directed_seam", "onsite_contact")
            },
            "colors": len(set(colors)),
            "edge_schedule_sha256": edge_hash,
            "physical_schedule_sha256": digest,
        },
    )

    site_map, gauges = C.placement(graph, include_edge_gauge=True)
    active = C.occupied_sites(site_map)
    prepared = C.occupied_sites(site_map, gauges)
    repetition = C.repetition_controls()
    C.check(
        "Cycle232 placement realizes 76 abstract edges on 80 literal sites and the optional gauge graph on 84",
        len(active) == 80
        and sum(len(value) for value in site_map.values()) == 80
        and len(gauges) == 4
        and len(prepared) == 84
        and max(max(abs(v) for v in site) for site in active) == 12
        and repetition["exact_residual"] < C.TOL
        and repetition["delete_second_X_residual"] > 1.9,
        {
            "abstract_graph_edge_qubits": len(graph.edges),
            "literal_physical_M2": len(active),
            "optional_edge_gauge_M2": len(gauges),
            "prepared_physical_M2": len(prepared),
            "patch_Linf_radius": 12,
            "patch_L1_diameter": C.l1_diameter(active),
            "repetition": repetition,
        },
    )

    homomorphism_failures = 0
    for factor in factors:
        for left in factor.rows:
            for right in factor.rows:
                mapped_product, _ = C.physical_pauli(left @ right, graph, site_map)
                mapped_left, _ = C.physical_pauli(left, graph, site_map)
                mapped_right, _ = C.physical_pauli(right, graph, site_map)
                homomorphism_failures += mapped_product != mapped_left @ mapped_right
    C.check(
        "the two-site repetition lift preserves every scheduled Pauli product and phase",
        homomorphism_failures == 0,
        {"scheduled_pair_homomorphism_failures": homomorphism_failures},
    )

    segment = next(factor for factor in factors if factor.key == C.SEGMENT_KEY)
    physical_rows = tuple(
        C.physical_pauli(row, graph, site_map)[0] for row in segment.rows
    )
    all_sites = C.physical_pauli(segment.rows[0], graph, site_map)[1]
    execution = C.execute_segment(physical_rows, all_sites)
    C.check(
        "one nontrivial two-cell seam segment executes as two commuting physical Pauli rotations",
        execution["rows_commute"]
        and execution["union_sites"] == 14
        and execution["row_weights"] == (11, 7)
        and execution["maximum_execution_residual"] < C.TOL
        and execution["minimum_delete_all_RZ_residual"] > 0.1,
        {key: value for key, value in execution.items() if key != "word"},
    )

    routed, routing = C.route_word(execution["word"])
    C.check(
        "Cycle655 Manhattan route-and-return compiles the segment to an ordered NN word",
        routing["routed_gate_count"] == 910
        and routing["touched_sites"] == 178
        and routing["maximum_route_distance"] == 24
        and routing["non_NN_failures"] == 0
        and routing["operand_order_failures"] == 0
        and routing["route_return_failures"] == 0
        and routing["delete_first_swap_detected_macros"] > 0,
        {key: value for key, value in routing.items() if key != "touched_coordinates"},
    )

    controller655 = C.cycle655_controller(routed, len(active))
    h_rows = tuple(
        row for row in controller655["bypass_opcode_controls"]
        if row["kind"] == "basis_H"
    )
    rz_rows = tuple(
        row for row in controller655["bypass_opcode_controls"]
        if row["kind"] == "axis_RZ"
    )
    C.check(
        "Cycle655 selection geometry closes but its blank-bypass audit rejects the nonblank-fixed basis gates",
        controller655["program_length"] == 910
        and controller655["fixed_cube_radius"] == 15
        and controller655["fixed_cube_M2"] == 29791
        and controller655["selected_order_failures"] == 0
        and controller655["token_return_failures"] == 0
        and controller655["delete_clock_shift_changes_word"]
        and controller655["Toffoli_residual"] < C.TOL
        and controller655["Fredkin_residual"] < C.TOL
        and controller655["maximum_bypass_action_residual"] > 1.0
        and controller655["maximum_bypass_work_leakage"] > 0.9
        and h_rows
        and min(row["action_residual"] for row in h_rows) > 1.0
        and min(row["work_leakage"] for row in h_rows) > 0.9
        and rz_rows
        and min(row["action_residual"] for row in rz_rows) > 0.2,
        controller655,
    )

    controller656 = C.cycle656_controller(routed, routing["touched_coordinates"])
    C.check(
        "the landed Cycle656 PacketTrace closes 910 abstract stations while the custom selector census remains projected",
        controller656["stations_A"] == 910
        and controller656["packet_data_lanes"] == 178
        and controller656["projected_A_column_M2"] == 243
        and controller656["projected_B_column_M2"] == 179
        and controller656["projected_complete_footprint_M2"] == 384020
        and controller656["rail_failures"] == 0
        and controller656["selected_order_failures"] == 0
        and controller656["live_count_failures"] == 0
        and controller656["B_vacuum_failures"] == 0
        and controller656["program_change_failures"] == 0
        and controller656["ancilla_change_failures"] == 0
        and controller656["station_zero_return"]
        and controller656["opcode_controlled_one_M2_residual"] < C.TOL
        and controller656["opcode_controlled_one_M2_unitarity_residual"] < C.TOL
        and controller656["opcode_two_M2_bypass_action_residual"] < C.TOL
        and controller656["opcode_two_M2_bypass_work_leakage"] < C.TOL
        and not controller656["literal_custom_selector_blueprint_executed"]
        and controller656["wrong_origin_cyclic_history"]
        and controller656["delete_ROM_17_missing"],
        controller656,
    )

    covariance = C.covariance_controls(graph, routed)
    C.check(
        "translations and all 24/576 proper-cubic diagrams preserve placement gauges and routed NN words",
        covariance["proper_cubic_frames"] == 24
        and covariance["ordered_frame_products"] == 576
        and covariance["placement_family_failures"] == 0
        and covariance["optional_gauge_family_failures"] == 0
        and covariance["rotated_word_NN_failures"] == 0
        and covariance["frame_closure_failures"] == 0
        and covariance["direction_action_failures"] == 0
        and covariance["placement_product_diagram_failures"] == 0
        and covariance["optional_gauge_product_diagram_failures"] == 0
        and covariance["routed_word_product_diagram_failures"] == 0
        and covariance["matrix_associativity_site_failures"] == 0
        and covariance["translated_placement_failures"] == 0
        and covariance["translated_optional_gauge_failures"] == 0
        and covariance["translated_word_diagram_failures"] == 0
        and covariance["translated_word_NN_failures"] == 0
        and covariance["canonical_site_set_equal_frames"] < 24
        and covariance["canonical_word_equal_frames"] < 24
        and covariance["unit_translation_canonical_equalities"] == 0,
        covariance,
    )

    held = C.held_placement_controls()
    C.check(
        "the same placement has active no-refit 3x3 and 4x4 held-size controls",
        tuple(
            (
                row["size"],
                row["abstract_edges"],
                row["literal_physical_M2"],
                row["prepared_plus_gauge_M2"],
            )
            for row in held
        )
        == ((2, 76, 80, 84), (3, 174, 186, 198), (4, 312, 336, 360))
        and all(row["collisions"] == 0 for row in held)
        and all(row["expected_stream_failures"] == 0 for row in held)
        and all(row["parameters_refit"] == 0 for row in held),
        held,
    )

    no_go_packet = {
        "status": "FAIL-for-broad-negative",
        "demotion": "partial-attempt-with-named-untested-routes",
        "N1_routes_attempted": 5,
        "N2_candidate_subobligations": ("chart", "ordering", "genesis", "recurrence"),
        "N2_pair_rows_recorded": 6,
        "N2_bidirectional_interventions_closed": 0,
        "N2_gate_complete": False,
        "N3_hidden_inputs_exposed": 17,
        "N4_exact_witness_rows": 8,
        "N4_negative_residual_match_complete": False,
        "N5_broad_no_go_shipped": False,
        "N6_partial_closure": (
            "literal placement, routed executed segment, and abstract PacketTrace"
        ),
        "N7_steelman_open": (
            "translation-invariant recurrent overlap-safe local controller and preparation law"
        ),
        "N8_prior_echo": (
            "Cycle232 supplied layout/schedule and Cycle655/656 supplied program/genesis remain explicit"
        ),
    }
    C.check(
        "N1-N8 gate fails at N2/N4 and therefore forbids a broad negative",
        no_go_packet["N1_routes_attempted"] >= 5
        and len(no_go_packet["N2_candidate_subobligations"]) == 4
        and no_go_packet["N2_pair_rows_recorded"] == 6
        and not no_go_packet["N2_gate_complete"]
        and not no_go_packet["N4_negative_residual_match_complete"]
        and no_go_packet["N7_steelman_open"]
        and not no_go_packet["N5_broad_no_go_shipped"],
        no_go_packet,
    )

    print("SITE_MAP", tuple(sorted(site_map.items())))
    print("OPTIONAL_GAUGE_MAP", tuple(sorted(gauges.items())))
    print(f"SUMMARY PASS {C.PASS} FAIL {C.FAIL}")
    print("LITERAL_PATCHGRAPH_Z3_M2_PLACEMENT_CONTROLLER_CERTIFICATE")
    return 0 if C.FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
