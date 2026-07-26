#!/usr/bin/env python3
"""Primary acceptance runner for the bounded Cycle708 endpoint-cube bridge."""

from __future__ import annotations

import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle708_physical_endpoint_cube_core_2026_07_26 as C


PASS = 0
FAIL = 0
ACTIVE_SOURCE_PATHS = (
    "scripts/frontier_cycle708_physical_endpoint_cube_2026_07_26.py",
    "scripts/frontier_cycle708_physical_endpoint_cube_core_2026_07_26.py",
    "scripts/frontier_cycle708_endpoint_cube_tableau_core_2026_07_26.py",
    "scripts/frontier_cycle708_cube_basis_gauge_core_2026_07_26.py",
    "scripts/frontier_literal_patchgraph_z3_m2_placement_core_cycle707_2026_07_26.py",
    "scripts/frontier_literal_patchgraph_cycle656_projected_trace_cycle707_2026_07_26.py",
    "scripts/frontier_full128_25site_nn_circuit_core_2026_07_24.py",
    "scripts/frontier_full128_cycle_encoder_2026_07_24.py",
    "scripts/frontier_full128_two_rail_fixed_law_core_2026_07_24.py",
    "scripts/frontier_full128_cycle_cocycle_intertwiner_2026_07_24.py",
    "scripts/frontier_full128_bare_frame_pair_cocycle_2026_07_24.py",
    "scripts/frontier_full128_code_projectors_2026_07_24.py",
    "scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py",
)
NOTE_PATH = (
    "docs/PHYSICAL_CYCLE704_FSWAP_ENDPOINT_CUBE_BRIDGE_"
    "CYCLE708_BOUNDED_THEOREM_NOTE_2026-07-26.md"
)
AUDIT_INPUT_PATHS = (
    "docs/PHYSICAL_CYCLE704_FSWAP_ENDPOINT_CUBE_BRIDGE_"
    "CYCLE708_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/OPENREFERENCE_PATCHGRAPH_FOUR_RAIL_SIGNED_CLIFFORD_"
    "EQUIVALENCE_CYCLE706_NOTE_2026-07-26.md",
    "docs/LITERAL_PATCHGRAPH_Z3_M2_PLACEMENT_AND_FIXED_CONTROLLER_"
    "CYCLE707_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "scripts/frontier_cycle708_physical_endpoint_cube_2026_07_26.py",
    "scripts/frontier_cycle708_physical_endpoint_cube_core_2026_07_26.py",
    "scripts/frontier_cycle708_endpoint_cube_tableau_core_2026_07_26.py",
    "scripts/frontier_cycle708_cube_basis_gauge_core_2026_07_26.py",
    "scripts/frontier_literal_patchgraph_z3_m2_placement_core_cycle707_2026_07_26.py",
    "scripts/frontier_literal_patchgraph_cycle656_projected_trace_cycle707_2026_07_26.py",
    "scripts/frontier_full128_25site_nn_circuit_core_2026_07_24.py",
    "scripts/frontier_full128_cycle_encoder_2026_07_24.py",
    "scripts/frontier_full128_two_rail_fixed_law_core_2026_07_24.py",
    "scripts/frontier_full128_cycle_cocycle_intertwiner_2026_07_24.py",
    "scripts/frontier_full128_bare_frame_pair_cocycle_2026_07_24.py",
    "scripts/frontier_full128_code_projectors_2026_07_24.py",
    "scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if bool(condition):
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def source_inventory() -> dict[str, object]:
    declared = tuple((ROOT / relative).resolve() for relative in DECLARED_INPUT_PATHS)
    paths = tuple((ROOT / relative).resolve() for relative in ACTIVE_SOURCE_PATHS)
    sizes = {
        str(path.relative_to(ROOT)): path.stat().st_size
        for path in paths if path.is_file() and path.is_relative_to(ROOT)
    }
    return {
        "declared_inputs": len(declared),
        "declared_duplicates": len(declared) - len(set(declared)),
        "declared_missing": tuple(
            str(path) for path in declared if not path.is_file()
        ),
        "declared_external": tuple(
            str(path) for path in declared if not path.is_relative_to(ROOT)
        ),
        "active_sources": len(paths),
        "duplicates": len(paths) - len(set(paths)),
        "missing": tuple(str(path) for path in paths if not path.is_file()),
        "external": tuple(str(path) for path in paths if not path.is_relative_to(ROOT)),
        "source_bytes": sizes,
        "sources_at_or_over_40000_bytes": tuple(
            name for name, size in sizes.items() if size >= 40_000
        ),
        "over_ceiling_Cycle706_runtime_imported": (
            "scripts/frontier_cycle706_openreference_patchgraph_four_rail_equivalence_2026_07_26.py"
            in ACTIVE_SOURCE_PATHS
        ),
    }


def note_contract() -> dict[str, object]:
    text = (ROOT / NOTE_PATH).read_text()
    required = (
        "**Type:** bounded_theorem",
        "**Authority:** none",
        "**Audit:** unset",
        "The dense abstract tableau `T_g` is not executed",
        "## Supplied, derived, and open structure",
        "## No-Go Discipline Gate",
        "### N1",
        "### N8",
        "FAIL for a broad negative",
        "SUMMARY PASS 18 FAIL 0",
    )
    forbidden = (
        "Authority: retained",
        "**Audit:** pass",
        "route-independent obstruction survives",
        "factor count is physical time",
        "opportunity pointer is a Record",
    )
    return {
        "required_missing": tuple(row for row in required if row not in text),
        "forbidden_present": tuple(row for row in forbidden if row in text),
    }


def main() -> int:
    print("CYCLE708 BOUNDED PHYSICAL ENDPOINT CUBE BRIDGE")
    note = note_contract()
    check(
        "the theorem note preserves the bounded claim, authority-none surface, and N1-N8 boundary",
        not note["required_missing"] and not note["forbidden_present"],
        note,
    )
    inventory = source_inventory()
    check(
        "the explicit active runtime closure is repo-local and every scientific source is below 40kB",
        inventory["declared_inputs"] == 16
        and inventory["declared_duplicates"] == 0
        and not inventory["declared_missing"]
        and not inventory["declared_external"]
        and inventory["active_sources"] == 13
        and inventory["duplicates"] == 0
        and not inventory["missing"]
        and not inventory["external"]
        and not inventory["sources_at_or_over_40000_bytes"]
        and not inventory["over_ceiling_Cycle706_runtime_imported"],
        inventory,
    )
    pins = C.dependency_pins()
    check(
        "all active landed dependencies and nonruntime Cycle706 evidence are byte-pinned",
        len(pins["expected"]) == 9
        and not pins["failures"]
        and len(pins["nonruntime_evidence_expected"]) == 1
        and not pins["nonruntime_evidence_failures"],
        pins,
    )

    certificate = C.cube_certificate()
    report = C.summarize_cube(certificate)
    drops = report["drop_choices"]
    check(
        "the open cube is 168 Open edges versus 156 PatchGraph edges plus twelve prepared rails",
        report["resources"] == {
            "open_graph_edge_qubits": 168,
            "patch_graph_edge_qubits": 156,
            "prepared_Z_rails": 12,
            "literal_active_M2": 168,
            "literal_plus_midpoint_rails_M2": 180,
        },
        report["resources"],
    )
    check(
        "deleting any one of six coarse-plaquette rows leaves exact rank-168 signed bases",
        len(drops) == 6
        and all(row["full_rows"] == 169 for row in drops)
        and all(row["full_source_rank"] == 168 for row in drops)
        and all(row["full_target_rank"] == 168 for row in drops)
        and all(row["coarse_source_rank_alone"] == 6 for row in drops)
        and all(row["coarse_target_rank_alone"] == 6 for row in drops)
        and all(row["source_canonical_failures"] == 0 for row in drops)
        and all(row["target_canonical_failures"] == 0 for row in drops),
        drops,
    )
    check(
        "all 36 endpoint B/B/product images are choice-independent pure-Z PatchGraph rows with no rails",
        all(row["endpoint_rows"] == 36 for row in drops)
        and all(row["endpoint_expected_failures"] == 0 for row in drops)
        and all(row["endpoint_inverse_failures"] == 0 for row in drops)
        and all(row["endpoint_image_differences_from_first_drop"] == 0 for row in drops)
        and report["endpoint"]["seams"] == 12
        and report["endpoint"]["mapped_rows"] == 36
        and report["endpoint"]["abstract_weight_tuples"] == [(6, 6, 10)]
        and report["endpoint"]["rail_weight_tuples"] == [(0, 0, 0)]
        and report["endpoint"]["pure_Z_failures"] == 0
        and report["endpoint"]["cell_diameter_tuples"] == [(1, 1, 1)],
        report["endpoint"],
    )
    check(
        "the literal Cycle707 lift preserves weights 6/6/10 and bounded cube diameters",
        report["endpoint"]["physical_weight_tuples"] == [(6, 6, 10)]
        and report["endpoint"]["maximum_physical_L1_by_word"] == (11, 13, 24)
        and report["endpoint"]["maximum_physical_Linf_by_word"] == (11, 13, 24),
        report["endpoint"],
    )

    extraction = report["extraction"]
    check(
        "twelve distinct blank pointers each extract one selected seam parity in 242 NN factors",
        extraction["pointer_collisions"] == 0
        and extraction["distinct_pointers"] == 12
        and extraction["pairwise_pointer_collisions"] == 0
        and extraction["selected_seam_routed_compute_factors"] == 242
        and extraction["all_12_independent_certificate_factors"] == 2904
        and extraction["routed_compute_factor_counts"] == [242]
        and extraction["nearest_neighbor_failures"] == 0
        and extraction["maximum_pointer_distance"] == 13
        and extraction["touched_sites_by_axis"] == {"0": [115], "1": [77], "2": [47]}
        and extraction["selected_rails_traversed"] == 8
        and extraction["selected_rails_untraversed"] == 4
        and extraction["all_selected_rails_final_return_failures"] == 0
        and extraction["complete_routed_coordinates"] == 812
        and extraction["carrier_and_prepared_rail_sites"] == 180
        and extraction["routed_plus_carrier_rail_union"] == 832
        and extraction["execution_scope"].startswith("one selected seam"),
        extraction,
    )
    check(
        "12x1024 truth rows, arbitrary spectators, and every protected rail return exactly",
        extraction["exhaustive_rows"] == 12 * 1024
        and extraction["truth_or_return_failures"] == 0
        and extraction["symbolic_GF2_basis_rows"] == 960
        and extraction["symbolic_arbitrary_spectator_or_return_failures"] == 0
        and extraction["protected_rails_symbolically_returned"] == 12,
        extraction,
    )
    check(
        "all 120 active-CNOT deletions are detected",
        extraction["active_CNOTs"] == 120
        and extraction["active_CNOT_deletions_detected"] == 120
        and extraction["first_route_SWAP_deletions_detected"] == 12,
        extraction,
    )

    bridge = C.cycle704_bridge_certificate()
    check(
        "on the exact dressed-FSWAP domain the extracted B_u B_v eigenspace bit equals n_u XOR n_v and Cycle704 P_B",
        len(bridge["lawful_truth_rows"]) == 4
        and bridge["truth_relation_failures"] == 0
        and bridge["unitarity_residual"] == 0.0
        and bridge["blank_pointer_isometry_residual"] == 0.0
        and bridge["projector_relation_residual"] == 0.0
        and bridge["domain_controls"] == {
            "dressed_FSWAP_mismatches": 0,
            "dressed_FSWAP_rows": 4,
            "unrestricted_before_after_mismatches": 8,
            "unrestricted_before_after_rows": 16,
            "unchanged_diagonal_false_fires": 2,
            "unchanged_diagonal_rows": 4,
        }
        and "coherently entangled" in bridge["superposition_semantics"]
        and "no measurement, occurrence, or Record" in bridge["classification"],
        bridge,
    )
    check(
        "the eigenspace intertwiner is conditional on already applying the abstract tableau and literal code map",
        bridge["conditional_eigenspace_intertwiner"].startswith("V(E_lit T")
        and "abstract/dense signed tableau map" in bridge["map_boundary"]
        and "executes only V" in bridge["map_boundary"],
        {
            "intertwiner": bridge["conditional_eigenspace_intertwiner"],
            "boundary": bridge["map_boundary"],
        },
    )

    gauge = C.basis_gauge_certificate()
    check(
        "the unique cube W relation has 30 rows and exactly those 30 deletions are rank-168 endpoint gauges",
        gauge["full_W_rows"] == 169
        and gauge["full_source_rank"] == 168
        and gauge["full_target_rank"] == 168
        and gauge["relation_dimension"] == 1
        and gauge["unique_relation_weight"] == 30
        and gauge["relation_kind_counts"] == {"cell_triangle": 24, "coarse_plaquette": 6}
        and gauge["source_relation_identity"] == (0, 0, 0)
        and gauge["target_relation_identity"] == (0, 0, 0)
        and gauge["eligible_deletion_rows"] == 30
        and gauge["eligible_source_rank_failures"] == 0
        and gauge["eligible_target_rank_failures"] == 0
        and gauge["eligible_canonical_failures"] == 0
        and gauge["eligible_endpoint_maps"] == 1080
        and gauge["eligible_endpoint_map_failures"] == 0
        and gauge["outside_deletion_rows"] == 139
        and gauge["outside_deletion_rank_values"] == (167,),
        gauge,
    )
    check(
        "eligible basis gauges form two proper-cubic orbits and no deletion row is globally fixed",
        gauge["proper_cubic_frames"] == 24
        and gauge["relation_row_action_failures"] == 0
        and gauge["relation_row_orbit_sizes"] == (6, 24)
        and gauge["globally_fixed_eligible_rows"] == 0,
        gauge,
    )

    covariance = C.covariance_certificate(certificate)
    literal = covariance["literal_full_extraction_word"]
    check(
        "all endpoint semantics and the complete routed certificate family close under 24/576 covariance and translations",
        covariance["proper_cubic_frames"] == 24
        and covariance["ordered_frame_products"] == 576
        and covariance["oriented_endpoint_rows"] == 864
        and covariance["oriented_endpoint_failures"] == 0
        and covariance["endpoint_label_product_tests"] == 13824
        and covariance["endpoint_label_product_failures"] == 0
        and covariance["literal_translation_vectors"] == 4
        and covariance["claim_scope"] == "endpoint subalgebra and physical routed word only"
        and not covariance["tableau_drop_covariance_claimed"]
        and literal["proper_cubic_frames"] == 24
        and literal["ordered_frame_products"] == 576
        and all(
            literal[key] == 0
            for key in (
                "placement_family_failures",
                "optional_gauge_family_failures",
                "rotated_word_NN_failures",
                "frame_closure_failures",
                "direction_action_failures",
                "placement_product_diagram_failures",
                "optional_gauge_product_diagram_failures",
                "routed_word_product_diagram_failures",
                "matrix_associativity_site_failures",
                "translated_placement_failures",
                "translated_optional_gauge_failures",
                "translated_word_diagram_failures",
                "translated_word_NN_failures",
            )
        )
        and literal["canonical_word_equal_frames"] < 24
        and literal["unit_translation_canonical_equalities"] == 0,
        covariance,
    )

    held = C.held_controls()
    check(
        "the frozen greedy rank repair passes a no-refit 3x2x2 held box",
        tuple(
            (
                row["shape"], row["open_edges"], row["patch_edges"], row["rails"],
                row["coarse_rows"], row["dropped_coarse_rows"], row["endpoint_rows"],
            ) for row in held
        ) == (
            ((2, 2, 2), 168, 156, 12, 6, 1, 36),
            ((3, 2, 2), 256, 236, 20, 11, 2, 60),
        )
        and all(row["source_canonical_failures"] == 0 for row in held)
        and all(row["target_canonical_failures"] == 0 for row in held)
        and all(row["endpoint_failures"] == 0 for row in held)
        and all(row["parameters_refit"] == 0 for row in held),
        held,
    )
    unlawful = C.unlawful_controls()
    check(
        "invalid graph, drop-set, support, and pointer domains are actively rejected",
        len(unlawful["cases"]) == 8
        and unlawful["rejected"] == unlawful["cases"]
        and not unlawful["failures"],
        unlawful,
    )

    boundary = C.boundary_inventory()
    check(
        "supplied, derived, open, and not-claimed surfaces stay explicit",
        all(boundary.values())
        and any("simultaneous" in row for row in boundary["open"])
        and any("execution of the abstract/dense" in row for row in boundary["open"])
        and any("one selected seam" in row for row in boundary["not_claimed"])
        and any("not an executed local circuit" in row for row in boundary["not_claimed"])
        and any("not called a Record" in row for row in boundary["not_claimed"]),
        boundary,
    )
    print("REPORT", json.dumps({
        "cube": report,
        "cycle704_bridge": bridge,
        "basis_gauge": gauge,
        "covariance": covariance,
        "held": held,
        "unlawful": unlawful,
        "boundary": boundary,
    }, sort_keys=True, default=str))
    print(f"SUMMARY PASS {PASS} FAIL {FAIL}")
    print("CYCLE708_PHYSICAL_ENDPOINT_CUBE_CERTIFICATE")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
