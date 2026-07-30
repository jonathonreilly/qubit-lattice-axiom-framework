#!/usr/bin/env python3
"""Cycle-794 literal local input prefix plus recurrent Cycle-720 G.

The public Cycle-789 three-bank channel and fixed-coframe router are composed
with the landed recurrent Cycle-720 physical update on the same O registers.
The executed equality is a complete signed Choi-graph plus factorwise
postcomposition theorem.  It is not a dense full-physical-width matrix test.
Fixed circuit and colour slots are schedule data, not physical time.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1200
NOTE_PATH = (
    "docs/LITERAL_THREE_BANK_PREFIX_RECURRENT_G_ACTUAL_SHEAR_"
    "CYCLE794_BOUNDED_THEOREM_NOTE_2026-07-30.md"
)
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle794_literal_three_bank_prefix_core_2026_07_30.py",
    "scripts/frontier_cycle794_actual_frame_shear_three_bank_schedule_2026_07_30.py",
    "scripts/frontier_cycle789_three_register_even_car_channel_2026_07_30.py",
    "scripts/frontier_cycle789_three_bank_fixed_coframe_schedule_2026_07_30.py",
    "scripts/frontier_cycle789_two_bank_input_collision_discriminator_2026_07_30.py",
    "scripts/frontier_cycle720_companion_recurrent_overlap_update_2026_07_27.py",
    "scripts/frontier_cycle712_joint_two_cell_full_update_physical_m2_2026_07_26.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

from hashlib import sha256
import json
from pathlib import Path

import numpy as np

import frontier_cycle712_joint_two_cell_full_update_physical_m2_2026_07_26 as C712
import frontier_cycle720_companion_recurrent_overlap_update_2026_07_27 as R720
import frontier_cycle789_three_bank_fixed_coframe_schedule_2026_07_30 as S788
import frontier_cycle789_three_register_even_car_channel_2026_07_30 as C788
import frontier_cycle789_two_bank_input_collision_discriminator_2026_07_30 as D788
import frontier_cycle794_actual_frame_shear_three_bank_schedule_2026_07_30 as SHEAR
import frontier_cycle794_literal_three_bank_prefix_core_2026_07_30 as CORE


TOL = 4.0e-10
IDENTITY_FRAME = ((1, 0, 0), (0, 1, 0), (0, 0, 1))


def json_safe(value):
    if isinstance(value, dict):
        return {str(key): json_safe(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [json_safe(item) for item in value]
    if isinstance(value, np.ndarray):
        return json_safe(value.tolist())
    if isinstance(value, np.generic):
        return value.item()
    if isinstance(value, complex):
        return [value.real, value.imag]
    return value


def matrix_digest(matrix) -> str:
    return sha256(
        np.round(np.asarray(matrix, dtype=complex), 14).tobytes()
    ).hexdigest()


def program_digest(prefix_primitives, routed_G):
    word = tuple(
        ("prefix_" + primitive.kind, primitive.sites)
        for primitive in prefix_primitives
    ) + tuple(
        (
            "G_" + gate.kind,
            tuple(tuple(site) for site in gate.sites),
            matrix_digest(gate.matrix),
        )
        for gate in routed_G
    )
    return {
        "prefix_primitives": len(prefix_primitives),
        "routed_G_primitives": len(routed_G),
        "total_primitives": len(word),
        "program_sha256": sha256(repr(word).encode()).hexdigest(),
    }


def dirty_ancilla_control(atlas):
    obj = C788.circuit_objects((1, 1, 1), atlas)
    initial = obj["resource"] + obj["live_reference"] + obj["ancilla_z"]
    dirty = list(initial)
    first = len(obj["resource"]) + len(obj["live_reference"])
    dirty[first] = C788.Pauli(x=1 << (4 * obj["q"]))
    clean_final = C788.conjugate_basis(initial, obj["gates"])
    dirty_final = C788.conjugate_basis(tuple(dirty), obj["gates"])
    clean_binary, clean_signed = C788.signed_span_failures(
        obj["output_reference"], clean_final, obj["width"]
    )
    dirty_binary, dirty_signed = C788.signed_span_failures(
        obj["output_reference"], dirty_final, obj["width"]
    )
    return {
        "clean_binary_failures": clean_binary,
        "clean_signed_failures": clean_signed,
        "dirty_X_for_first_Z_ancilla_binary_failures": dirty_binary,
        "dirty_X_for_first_Z_ancilla_signed_failures": dirty_signed,
    }


def live_bank_control():
    states = {
        "zero": D788.ZERO,
        "one": D788.ONE,
        "plus": (D788.ZERO + D788.ONE) / np.sqrt(2),
        "plus_i": (D788.ZERO + 1j * D788.ONE) / np.sqrt(2),
    }
    old = {
        key: D788.character_channel(state, repaired=False)
        for key, state in states.items()
    }
    repaired = {
        key: D788.character_channel(state, repaired=True)
        for key, state in states.items()
    }
    targets = {
        key: np.outer(state, state.conj()) for key, state in states.items()
    }
    return {
        "states": tuple(states),
        "two_bank_pairwise_residual": float(max(
            np.linalg.norm(old[left] - old[right])
            for left in states for right in states
        )),
        "two_bank_identity_residual": float(max(
            np.linalg.norm(old[key] - targets[key]) for key in states
        )),
        "three_bank_identity_residual": float(max(
            np.linalg.norm(repaired[key] - targets[key]) for key in states
        )),
    }


def target_update_certificate():
    word, qr_residual = C712.decoded_word(2)
    basis = C712.subspace(12, 2)
    _direct, _coin, free_one = C712.direct_restricted_update(basis, 2)
    return {
        "decoded_word_gates": len(word),
        "coin_QR_residual": qr_residual,
        "sector_complete": C712.sector_complete_certificate(
            word, free_one, 2, active_columns=True
        ),
        "stages": C712.stage_and_falsifier_certificate(
            word, basis, free_one
        ),
        "Cycle230_semantics": C712.cycle230_semantic_certificate(word),
    }


def box_certificate(shape, atlas, powers):
    route_report, scratch = S788.box_certificate(shape, atlas)
    obj = C788.circuit_objects(shape, atlas)
    channel = C788.channel_certificate(shape, atlas)
    order = CORE.order_for(scratch, IDENTITY_FRAME)
    abstract_word, _inversions = CORE.abstract_prefix_word(
        obj, scratch, order, repair=True
    )
    physical = CORE.physical_prefix(scratch, order)
    physical_structure_failures = CORE.physical_structure_failures(
        scratch, order, physical
    )
    semantic_signature_failures = int(
        CORE.semantic_signature_from_abstract(abstract_word, obj["q"])
        != CORE.semantic_signature_from_physical(
            obj, scratch, order, physical
        )
    )
    graph = CORE.graph_and_tableau_certificate(obj, scratch, order)
    contexts = CORE.context_graph_certificate(obj, scratch)
    geometry = S788.covariance_certificate(scratch)
    order_covariance = S788.schedule_order_certificate(
        scratch, include_products=True
    )
    firewall_covariance = CORE.firewall_path_covariance_certificate(scratch)

    fixture = scratch["fixture"]
    placed = S788.U.placement(fixture)
    G_word, G_update = S788.U.physical_word(fixture, placed)
    routed_G, G_route = S788.U.c707.route_word(G_word)
    recurrent = R720.recurrent_box_certificate(shape, powers=powers)
    output_sites = tuple(placed["sites_by_qubit"])
    persistent_classes = (
        "O_matter", "O_companion", "coframe", "I", "L", "bell_ancilla"
    )
    persistent = set().union(*(
        scratch["classes"][name] for name in persistent_classes
    ))
    persistent_count = sum(
        len(scratch["classes"][name]) for name in persistent_classes
    )
    prefix_support = persistent | {
        site
        for primitive in physical["primitives"]
        for site in primitive.sites
    }
    G_touched = {
        tuple(site) for gate in routed_G for site in gate.sites
    }
    non_output_persistent = persistent - set(output_sites) - set(
        scratch["classes"]["coframe"]
    )
    route_return_failures = sum(
        S788.label_return_failures(macro) for macro in physical["macros"]
    )
    route_target_failures = sum(
        S788.routed_target_failures(macro) for macro in physical["macros"]
    )
    route_NN_failures = sum(
        S788.manhattan(left, right) != 1
        for macro in physical["macros"]
        for left, right in zip(macro.path, macro.path[1:])
    )
    deleted_return_mismatches = next((
        S788.label_return_failures(macro, True)
        for macro in physical["macros"]
        if any(p.kind == "SWAP" for p in macro.primitives)
    ), 0)
    coordinate = recurrent["coordinate_intertwiner"]
    prefix_exact = (
        channel["character_rank"] == 2 * fixture.matter_qubits - 1
        and channel["output_reference_binary_span_failures"] == 0
        and channel["output_reference_signed_span_failures"] == 0
        and graph["repaired_output_binary_span_failures"] == 0
        and graph["repaired_output_signed_span_failures"] == 0
        and graph["repaired_full_tableau_differences_from_canonical"] == 0
        and semantic_signature_failures == 0
        and physical_structure_failures == 0
        and route_return_failures == 0
        and route_target_failures == 0
        and route_NN_failures == 0
    )
    recurrent_exact = all(
        coordinate[key] == 0 for key in (
            "logical_coordinate_failures",
            "gauge_coordinate_failures",
            "parity_coordinate_failures",
            "both_sector_phase_failures",
            "physical_generator_gauge_commutator_failures",
            "physical_generator_center_commutator_failures",
        )
    ) and all(
        row["intertwiner_induction_failures"] == 0
        and row["gauge_identity_induction_failures"] == 0
        for row in recurrent["recurrent_powers"]
    )
    return {
        "shape": shape,
        "cells": len(fixture.cells),
        "edges": len(fixture.edges),
        "matter_modes": fixture.matter_qubits,
        "character_rank": channel["character_rank"],
        "expected_complete_even_CAR_rank": 2 * fixture.matter_qubits - 1,
        "channel": channel,
        "literal_local_prefix": {
            "local_order": order,
            "semantic_signature_failures": semantic_signature_failures,
            "physical_structure_failures": physical_structure_failures,
            "graph": graph,
            "frame_origin_signed_graph": contexts,
            "physical_primitives": len(physical["primitives"]),
            "route_macros": len(physical["macros"]),
            "inversion_CZ_macros": len(physical["firewall_macros"]),
            "route_return_failures": route_return_failures,
            "route_target_reconstruction_failures": route_target_failures,
            "route_NN_failures": route_NN_failures,
            "deleted_return_label_mismatches": deleted_return_mismatches,
            "persistent_M2": persistent_count,
            "expected_fixed_palette_persistent_47N": 47 * len(fixture.cells),
            "persistent_collisions": persistent_count - len(persistent),
            "coordinate_support_M2": len(prefix_support),
            "maximum_route_distance": max((
                len(macro.path) - 1 for macro in physical["macros"]
            ), default=0),
            "non_output_persistent_G_collisions": len(
                non_output_persistent & G_touched
            ),
            "returned_prefix_route_coordinates_reused_by_G": len(
                prefix_support & G_touched
            ),
        },
        "geometry_covariance": geometry,
        "order_covariance": order_covariance,
        "firewall_path_covariance": firewall_covariance,
        "recurrent": recurrent,
        "G_update": G_update,
        "G_route": G_route,
        "single_coordinate_program": program_digest(
            physical["primitives"], routed_G
        ),
        "interface": {
            "literal_output_equals_Cycle720_output_coordinates": (
                set(scratch["classes"]["O_matter"])
                | set(scratch["classes"]["O_companion"])
            ) == set(output_sites),
            "recurrent_retained_M2": recurrent["total_retained_M2_sites"],
            "recurrent_retained_M2_per_cell": recurrent[
                "retained_M2_sites_per_cell"
            ],
            "prefix_routes_return_before_G": route_return_failures == 0,
        },
        "substitution": {
            "literal_complete_signed_Choi_graph_exact": prefix_exact,
            "recurrent_coordinate_and_gauge_intertwiner_exact": recurrent_exact,
            "shared_output_register_exact": (
                set(scratch["classes"]["O_matter"])
                | set(scratch["classes"]["O_companion"])
            ) == set(output_sites),
            "postcomposition_substitution_failures": int(not (
                prefix_exact and recurrent_exact
                and (
                    set(scratch["classes"]["O_matter"])
                    | set(scratch["classes"]["O_companion"])
                ) == set(output_sites)
            )),
            "proof": (
                "the rank-(2m-1) signed Choi graph fixes the complete even-CAR "
                "channel; literal returned-route replacement and the local "
                "inversion-CZ cocycle reproduce that graph; equality survives "
                "linear postcomposition; Cycle 720 supplies the factorwise "
                "physical/logical G intertwiner on the identical O registers"
            ),
        },
        "route_report_boundary": route_report,
    }


def source_hashes():
    modules = (CORE, SHEAR, C788, S788, D788, R720, C712)
    return {
        Path(module.__file__).name: sha256(
            Path(module.__file__).read_bytes()
        ).hexdigest()
        for module in modules
    }


def main():
    atlas = S788.P.build_private_atlases()
    boxes = (
        box_certificate((2, 1, 1), atlas, powers=(1, 2, 3, 5, 8)),
        box_certificate((3, 1, 1), atlas, powers=(1, 2, 3)),
    )
    deletion = C788.deletion_controls(atlas)
    dirty = dirty_ancilla_control(atlas)
    live = live_bank_control()
    order_attack = S788.ordered_channel_attack(atlas)
    target = target_update_certificate()
    recurrent_covariance = R720.update_covariance_certificate((2, 1, 1))

    checks = {
        "literal_local_prefix_plus_actual_recurrent_G_substitution_is_exact_on_two_cells_and_held_three": all(
            row["substitution"]["postcomposition_substitution_failures"] == 0
            for row in boxes
        ),
        "literal_physical_words_are_NN_returned_semantic_replacements_with_active_deletion": all(
            row["literal_local_prefix"]["semantic_signature_failures"] == 0
            and row["literal_local_prefix"]["physical_structure_failures"] == 0
            and row["literal_local_prefix"]["route_return_failures"] == 0
            and row["literal_local_prefix"]["route_target_reconstruction_failures"] == 0
            and row["literal_local_prefix"]["route_NN_failures"] == 0
            and row["literal_local_prefix"]["deleted_return_label_mismatches"] > 0
            for row in boxes
        ),
        "fixed_local_prefix_palette_and_recurrent_resources_have_constant_census": all(
            row["literal_local_prefix"]["persistent_M2"]
            == row["literal_local_prefix"]["expected_fixed_palette_persistent_47N"]
            and row["literal_local_prefix"]["persistent_collisions"] == 0
            and row["literal_local_prefix"]["non_output_persistent_G_collisions"] == 0
            and row["interface"]["recurrent_retained_M2_per_cell"] == 12
            for row in boxes
        ),
        "local_order_plus_inversion_CZ_reproduces_full_signed_prefix_in_24x8_contexts_and_576_products": all(
            row["literal_local_prefix"]["frame_origin_signed_graph"]["proper_cubic_frames"] == 24
            and row["literal_local_prefix"]["frame_origin_signed_graph"]["frame_origin_contexts"] == 192
            and row["literal_local_prefix"]["frame_origin_signed_graph"]["ordered_frame_products"] == 576
            and row["literal_local_prefix"]["frame_origin_signed_graph"]["repaired_output_binary_span_failures"] == 0
            and row["literal_local_prefix"]["frame_origin_signed_graph"]["repaired_output_signed_span_failures"] == 0
            and row["literal_local_prefix"]["frame_origin_signed_graph"]["repaired_full_tableau_differences_from_canonical"] == 0
            and row["literal_local_prefix"]["frame_origin_signed_graph"]["frame_product_order_outside_checked_contexts"] == 0
            and row["order_covariance"]["frame_origin_target_reconstruction_failures"] == 0
            and row["order_covariance"]["frame_product_target_reconstruction_failures"] == 0
            for row in boxes
        ),
        "prefix_geometry_firewall_and_recurrent_update_are_covariant_on_declared_surfaces": all(
            all(
                value == 0 for key, value in row["geometry_covariance"].items()
                if key.endswith("failures")
            )
            and all(
                value == 0 for key, value in row["firewall_path_covariance"].items()
                if key.endswith("failures")
            )
            for row in boxes
        ) and recurrent_covariance["proper_cubic_frames"] == 24
        and recurrent_covariance["operator_family_binary_multiset_failures"] == 0
        and recurrent_covariance["operator_family_signed_multiset_failures"] == 0
        and recurrent_covariance["seam_block_factor_order_covariance_failures"] == 0
        and recurrent_covariance["maximum_coin_frame_covariance_residual"] < TOL,
        "free_seam_contact_mass_and_leakage_target_regressions_pass": (
            target["sector_complete"]["second_quantized_local_factor_residual"] < TOL
            and target["sector_complete"]["compiled_one_particle_residual"] < TOL
            and target["sector_complete"]["local_number_leakage_amplitude"] == 0
            and target["sector_complete"]["contact_all_basis_phase_residual"] < TOL
            and target["sector_complete"]["maximum_active_column_residual"] < TOL
            and target["stages"]["coin_stage_residual"] < TOL
            and target["stages"]["reverse_stage_residual"] < TOL
            and target["stages"]["landed_seam_stage_residual"] < TOL
            and target["stages"]["contact_stage_residual"] < TOL
            and target["Cycle230_semantics"]["mass_residual"] < TOL
            and all(row["recurrent"]["one_particle_mass_residual"] < TOL for row in boxes)
        ),
        "deletion_dirty_live_bank_and_hostile_order_controls_are_active": (
            deletion["deleted_private_dual_output_binary_failures"] > 0
            or deletion["deleted_private_dual_output_signed_failures"] > 0
        ) and (
            deletion["self_comparison_output_binary_failures"] > 0
            or deletion["self_comparison_output_signed_failures"] > 0
        ) and dirty["clean_binary_failures"] == 0
        and dirty["clean_signed_failures"] == 0
        and (
            dirty["dirty_X_for_first_Z_ancilla_binary_failures"] > 0
            or dirty["dirty_X_for_first_Z_ancilla_signed_failures"] > 0
        )
        and live["two_bank_pairwise_residual"] < 1e-12
        and live["two_bank_identity_residual"] > 0.5
        and live["three_bank_identity_residual"] < 1e-12
        and order_attack["hostile_reversal_full_signed_generator_mismatches"] > 0
        and order_attack["CZ_repaired_full_signed_generator_mismatches"] == 0
        and target["stages"]["single_nonadjacent_tensor_FSWAP_residual"] > 1.0,
    }
    report = {
        "status": "PASS" if all(checks.values()) else "FAIL",
        "authority": "none",
        "audit": "unset",
        "checks": checks,
        "boxes": boxes,
        "target_free_seam_contact": target,
        "recurrent_update_covariance": recurrent_covariance,
        "deletion_controls": deletion,
        "dirty_ancilla_control": dirty,
        "live_bank_control": live,
        "hostile_order_control": order_attack,
        "source_sha256": source_hashes(),
        "supplied": [
            "one prepared companion-encoded O-I Choi resource",
            "an independent companion-encoded live L bank and diagnostic R reference",
            "clean Bell ancillas, fixed private-dual atlas, fixed parity/center sector and mixed-gauge domain",
            "the Cycle-789 O/I/L/coframe palettes, mod-3 colour origin, signed-port slots, and transported fixed schedule",
            "the Cycle-720 local factor dictionary, recurrent O/coframe placement and code domain",
            "the Cycle-230 coin/contact parameters and landed Cycle-712 seam convention",
        ],
        "derived": [
            "a literal local NN returned Bell-plus-correction prefix followed by the actual routed Cycle-720 G on the identical O coordinates",
            "an exact rank-(2m-1) complete signed even-CAR Choi graph and factorwise postcomposition theorem on two cells and held three cells",
            "an exact local-order inversion-CZ firewall on all 24x8 order contexts and all 576 frame-product orders",
            "a fixed prefix-persistent 47 M2/cell palette, bounded route support, and recurrent 12 retained M2/cell census",
            "free, seam, contact, mass, leakage, route-return, deletion, dirty-domain, two-bank and hostile-order controls",
        ],
        "open": [
            "autonomous non-postselected genesis of O-I, the independent encoded L bank, clean Bell ancillas and the coframe/domain sector",
            "a translation-invariant local law enforcing those genesis/domain conditions instead of supplying them",
            "full frame-sheared signed-channel covariance under transformed generator identities; Cycle794 proves every transported local order on the fixed signed graph plus separate geometry/operator-family covariance",
            "a dense full-physical-width monolithic matrix execution; exactness instead uses literal route substitution, complete signed Choi graph and the landed factorwise G theorem",
            "bridges to occurrence/admission, source/gravity, Record permanence and Born/history selection",
        ],
        "claim_boundary": (
            "Positive fixed-schedule two-cell and held-size physical compiler composition on a supplied clean companion-encoded genesis domain. It is not bare-input genesis, physical time, a source/gravity law, Record/Born selection, a minimum, a no-go, or axiom pressure."
        ),
    }
    safe = json_safe(report)
    safe["report_sha256"] = sha256(json.dumps(
        safe, sort_keys=True, separators=(",", ":")
    ).encode()).hexdigest()
    print("SUMMARY_JSON", json.dumps(safe, sort_keys=True))
    if report["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
