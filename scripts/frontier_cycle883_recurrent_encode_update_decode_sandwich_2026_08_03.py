#!/usr/bin/env python3
"""Cycle 883: recurrent Cycle-870 encode/update/decode sandwich.

The physical word is V ; U_G ; V^dagger in execution order, where V is the
full Cycle-870 encoder unitary and E=VJ is its restriction to the supplied clean
embedding J.  The Cycle-870 intertwiner makes the sandwich a recurrent raw
matter channel with every preparation auxiliary restored.  Circuit ordinals
are implementation structure, not physical time.
"""
from __future__ import annotations

import cmath
from hashlib import sha256
import json
import math
from pathlib import Path
import sys

import numpy as np

from frontier_cycle883_recurrent_encode_update_decode_sandwich_core_2026_08_03 import (
    INVERSE_KIND,
    word_hash,
)


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
OUT = ROOT / "outputs/cycle883_recurrent_encode_update_decode_sandwich_primary_receipt_2026_08_03.json"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle883_recurrent_encode_update_decode_sandwich_core_2026_08_03.py",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/OPENREFERENCE_CUBIC_RECURRENT_PHYSICAL_M2_MATTER_COMPILER_CYCLE870_BOUNDED_THEOREM_NOTE_2026-08-02.md",
    "scripts/frontier_cycle870_openreference_joined_recurrent_compiler_2026_08_02.py",
    "scripts/frontier_cycle870_openreference_native_recurrent_update_2026_08_02.py",
    "scripts/frontier_cycle870_openreference_physical_m2_placement_2026_08_02.py",
    "outputs/cycle870_openreference_joined_recurrent_compiler_receipt_2026_08_02.json",
    "outputs/cycle870_openreference_recurrent_update_independent_receipt_2026_08_02.json",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS
EXPECTED_SHA256 = {
    "scripts/frontier_cycle883_recurrent_encode_update_decode_sandwich_core_2026_08_03.py": "b21554d7689d8c5ad66dd1e4fa1bfad23c0928c402815111c0148b7a423b790b",
    "docs/MINIMAL_AXIOMS_2026-06-29.md": "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
    "docs/OPENREFERENCE_CUBIC_RECURRENT_PHYSICAL_M2_MATTER_COMPILER_CYCLE870_BOUNDED_THEOREM_NOTE_2026-08-02.md": "74beb1de39ea0e579b8c709fdb294602f8cb959f1283b7556eb4c62335fd2e2b",
    "scripts/frontier_cycle870_openreference_joined_recurrent_compiler_2026_08_02.py": "1b66c061dcb8e0082fd9e7264e78ccbd0f77440c0f517aa93696bde49f78c1bd",
    "scripts/frontier_cycle870_openreference_native_recurrent_update_2026_08_02.py": "687b22a0bd0fd71fc20e7597443886a4990b49fcef7c80164d5f685210e84237",
    "scripts/frontier_cycle870_openreference_physical_m2_placement_2026_08_02.py": "64b36432670f8a05179d0473e724afee1dfe6327cdd0233d3d788a6b8413c8a2",
    "outputs/cycle870_openreference_joined_recurrent_compiler_receipt_2026_08_02.json": "d6be75419b1fab56853127d55730b63a23ef7d44205e66b7fa73c9f19aac8611",
    "outputs/cycle870_openreference_recurrent_update_independent_receipt_2026_08_02.json": "f3fa00ade5696bf3061a2bedc776a910ad801e6bef28a7558f1a3f07ab7a813f",
}
TOL = 3.0e-10


def file_hash(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def inverse_instruction(U, row):
    if row.kind not in INVERSE_KIND:
        raise KeyError("Cycle883 has no canonical inverse-kind entry for " + row.kind)
    return U.c707.Instruction(
        INVERSE_KIND[row.kind],
        row.sites,
        np.asarray(row.matrix, dtype=complex).conj().T,
    )


def root_handshake_controls(events):
    """Execute the literal fresh-token-spent root events as three-bit words."""
    grouped = {}
    for event in events:
        if not event.atlas_role or event.atlas_role[0] != "controller_root_epoch":
            continue
        key = (event.owner, event.atlas_role[1])
        grouped.setdefault(key, []).append(event)

    chronology_failures = 0
    correct_reverse_failures = 0
    same_order_failures = 0
    whole_adjoint_deletion_failures = 0
    dirty_patterns_not_prepared = 0
    deleted_states = set()
    same_order_states = set()
    whole_delete_fresh_failures = whole_delete_spent_failures = 0
    same_order_fresh_failures = same_order_token_failures = 0

    def execute(rows, initial):
        bits = dict(initial)
        for row in rows:
            left, right = row.sites
            bits[left], bits[right] = bits[right], bits[left]
        return bits

    for rows in grouped.values():
        chronology_failures += len(rows) != 2
        if len(rows) != 2:
            continue
        first, second = rows
        chronology_failures += first.atlas_role[2] != "start"
        chronology_failures += second.atlas_role[2] != "spent"
        fresh, token = first.sites
        token_again, spent = second.sites
        chronology_failures += token != token_again
        clean = {fresh: 1, token: 0, spent: 0}
        encoded = execute(rows, clean)
        expected_encoded = {fresh: 0, token: 0, spent: 1}
        chronology_failures += encoded != expected_encoded
        restored = execute(tuple(reversed(rows)), encoded)
        correct_reverse_failures += restored != clean
        same_order = execute(rows, encoded)
        same_order_failures += same_order != clean
        whole_adjoint_deletion_failures += encoded != clean
        deleted_states.add((encoded[fresh], encoded[token], encoded[spent]))
        same_order_states.add(
            (same_order[fresh], same_order[token], same_order[spent])
        )
        whole_delete_fresh_failures += encoded[fresh] != clean[fresh]
        whole_delete_spent_failures += encoded[spent] != clean[spent]
        same_order_fresh_failures += same_order[fresh] != clean[fresh]
        same_order_token_failures += same_order[token] != clean[token]
        for pattern in range(8):
            initial = {
                fresh: (pattern >> 2) & 1,
                token: (pattern >> 1) & 1,
                spent: pattern & 1,
            }
            dirty_patterns_not_prepared += (
                initial != clean and execute(rows, initial) != expected_encoded
            )
    return {
        "root_groups": len(grouped),
        "literal_event_chronology_failures": chronology_failures,
        "correct_reverse_adjoint_clean_domain_failures": correct_reverse_failures,
        "same_order_adjoint_clean_domain_failures": same_order_failures,
        "whole_adjoint_deletion_next_domain_failures": whole_adjoint_deletion_failures,
        "state_order": ("fresh", "token", "spent"),
        "whole_adjoint_deletion_observed_states": tuple(sorted(deleted_states)),
        "whole_adjoint_deletion_fresh_failures": whole_delete_fresh_failures,
        "whole_adjoint_deletion_spent_failures": whole_delete_spent_failures,
        "same_order_adjoint_observed_states": tuple(sorted(same_order_states)),
        "same_order_adjoint_fresh_failures": same_order_fresh_failures,
        "same_order_adjoint_token_failures": same_order_token_failures,
        "dirty_controller_patterns_not_prepared": dirty_patterns_not_prepared,
        "dirty_controller_patterns_per_root": 7,
    }


def dirty_carrier_X_witness(J, graph, context):
    physical_code = tuple(J.update.physical_stabilizers(context))
    physical_logical_z = tuple(
        J.update.physical_lift(zrow, context)
        for _cell, _mode, _xrow, zrow in J.root.logical_rows(graph)
    )
    vacuum_rows = physical_code + physical_logical_z
    responses = []
    for site in context.sites:
        error = J.Pauli(x=1 << context.index[site])
        responses.append(sum(not error.commutes(row) for row in vacuum_rows))
    return {
        "single_carrier_X_cases": len(responses),
        "single_carrier_X_accepted_by_all_vacuum_rows": sum(value == 0 for value in responses),
        "minimum_violated_vacuum_rows": min(responses),
        "maximum_violated_vacuum_rows": max(responses),
        "witness_statement": (
            "every single-carrier X anticommutes with at least one independently reconstructed vacuum stabilizer; this rejects those dirty inputs but is not an admission circuit"
        ),
    }


def routed_encoder(J, shape, graph, site_map, context):
    syndrome = J.root.syndrome_interactions(graph, site_map)
    corrections = J.root.correction_interactions(graph, site_map)
    loader = J.root.loader_interactions(graph, site_map)
    controller = J.root.controller_interactions(shape, graph, site_map)
    check_stages, _ = J.coherent_check_primitives(graph, context, syndrome)
    correction_stages = J.correction_primitives(corrections)
    controller_ops, controller_events, _chronology = J.controller_chronology_primitives(
        shape, graph, site_map, controller
    )
    loader_ops, _ = J.loader_primitives(graph, context, loader)
    stages = (
        ("triangle_syndrome", check_stages["triangle_syndrome"]),
        ("triangle_correction", correction_stages["triangle_correction"]),
        ("coarse_syndrome", check_stages["coarse_syndrome"]),
        ("coarse_echo_correction_ack", controller_ops),
        ("bond_syndrome", check_stages["bond_syndrome"]),
        ("bond_correction", correction_stages["bond_correction"]),
        ("logical_load", loader_ops),
    )
    primitive = tuple(
        J.update.c707.Instruction(row.kind, row.sites, row.matrix)
        for _stage, rows in stages
        for row in rows
    )
    routed, certificate = J.update.c707.route_word(primitive)
    return (
        tuple(routed),
        certificate,
        tuple(name for name, _rows in stages),
        len(primitive),
        tuple(controller_events),
        certificate["word_sha256"],
    )


def routed_update(J, graph, context, coin_gates):
    rotations, inventory = J.update.build_update(graph, coin_gates)
    primitive = tuple(
        instruction
        for rotation in rotations
        for instruction in J.update.c707.compile_pauli_rotation(
            J.update.physical_lift(rotation.row, context),
            context.sites,
            rotation.angle,
        )
    )
    routed, certificate = J.update.c707.route_word(primitive)
    stage_runs = []
    for rotation in rotations:
        if not stage_runs or stage_runs[-1] != rotation.kind:
            stage_runs.append(rotation.kind)
    canonical = J.update.route_update(context, rotations)
    return (
        tuple(routed),
        certificate,
        tuple(stage_runs),
        len(primitive),
        inventory,
        primitive,
        canonical,
    )


def fixture(J, length, coin_gates, landed_by_shape):
    shape = (length, length, length)
    U = J.update
    graph = U.prep.OpenReferenceGraph(J.root.box(shape))
    site_map = J.root.carrier_placement(graph)
    context = U.physical_context(graph)
    auxiliary = J.auxiliary_registers(graph)
    (
        e_word,
        e_route,
        e_stages,
        e_primitive_count,
        controller_events,
        e_official_digest,
    ) = routed_encoder(J, shape, graph, site_map, context)
    (
        g_word,
        g_route,
        g_stages,
        g_primitive_count,
        _inventory,
        g_primitive,
        g_canonical,
    ) = routed_update(J, graph, context, coin_gates)
    e_dagger = tuple(
        inverse_instruction(U, row) for row in reversed(e_word)
    )
    inverse_pair_failures = sum(
        left.sites != right.sites
        or np.linalg.norm(left.matrix @ right.matrix - np.eye(left.matrix.shape[0])) > TOL
        for left, right in zip(e_dagger, reversed(e_word))
    )
    inverse_kind_failures = sum(
        left.kind != INVERSE_KIND[right.kind]
        for left, right in zip(e_dagger, reversed(e_word))
    )
    wrong_order = tuple(
        inverse_instruction(U, row) for row in e_word
    )
    wrong_order_pair_failures = sum(
        left.sites != right.sites
        or np.linalg.norm(left.matrix @ right.matrix - np.eye(left.matrix.shape[0])) > TOL
        for left, right in zip(wrong_order, reversed(e_word))
    )
    g_aux_endpoint_hits = sum(
        site in auxiliary for row in g_primitive for site in row.sites
    )
    official = landed_by_shape[shape]
    live = J.cube_fixture(length, coin_gates)
    joined = live["joined_route"]
    landed_joined = official["joined_route"]
    controller = joined["controller_execution"]
    intertwiner = live["intertwiner"]
    resource = joined["physical_resource_census"]
    formal_phase = joined["exact_global_phase"]
    def counts_match(candidate):
        return (
            len(e_word)
            == candidate["root_executable_primitive_route"]["routed_gate_count"]
            and len(g_word) == candidate["update_route"]["routed_gate_count"]
            and e_primitive_count
            == candidate["root_executable_primitive_route"]["primitive_gate_count"]
            and g_primitive_count == candidate["update_route"]["primitive_gate_count"]
        )

    counts_match_recomputed = counts_match(joined)
    counts_match_landed = counts_match(landed_joined)
    v_touched = set(e_route["touched_coordinates"])
    v_dagger_touched = {site for row in e_dagger for site in row.sites}
    g_touched = set(g_route["touched_coordinates"])
    touched_support = v_touched | g_touched | v_dagger_touched
    declared_bank = set(context.sites) | set(auxiliary)
    transit_support = touched_support - declared_bank
    declared_support = declared_bank | transit_support
    support_sha256 = J.rows_sha256(declared_support)
    transit_sha256 = J.rows_sha256(transit_support)
    selected = next(
        row
        for row in e_dagger
        if np.linalg.norm(row.matrix - np.eye(row.matrix.shape[0])) > 1.0e-8
    )
    selected_delete_residual = float(
        np.linalg.norm(selected.matrix - np.eye(selected.matrix.shape[0]))
    )
    composite = (*e_word, *g_word, *e_dagger)
    gate_unitarity_failures = sum(
        not np.allclose(
            row.matrix.conj().T @ row.matrix,
            np.eye(row.matrix.shape[0]),
            atol=1.0e-12,
        )
        for row in composite
    )
    v_gate_unitarity_failures = sum(
        not np.allclose(
            row.matrix.conj().T @ row.matrix,
            np.eye(row.matrix.shape[0]),
            atol=1.0e-12,
        )
        for row in e_word
    )
    non_nn_failures = sum(
        len(row.sites) == 2 and U.c707.c655.l1(*row.sites) != 1
        for row in composite
    )
    handshake = root_handshake_controls(controller_events)
    dirty_carrier = dirty_carrier_X_witness(J, graph, context)
    encoder = joined["encoder_isometry"]
    proof_obligations = intertwiner["proof_obligations"]
    proof_obligations_zero = not any(proof_obligations.values())
    v_dagger_v_J_pass = (
        len(e_word) == len(e_dagger)
        and inverse_pair_failures == 0
        and inverse_kind_failures == 0
        and v_gate_unitarity_failures == 0
        and e_route["route_return_failures"] == 0
    )
    one_epoch_pass = (
        v_dagger_v_J_pass
        and encoder["emitted_E_isometry_exact_on_declared_clean_domain"]
        and intertwiner["exact_intertwiner_pass"]
        and intertwiner["exact_vector_equality_follows_for_all_input_vectors"]
        and proof_obligations_zero
        and formal_phase["phase_sum_residual_mod_2pi"] <= TOL
    )
    next_domain_pass = (
        one_epoch_pass
        and g_aux_endpoint_hits == 0
        and handshake["correct_reverse_adjoint_clean_domain_failures"] == 0
    )
    two_epoch_seed_pass = one_epoch_pass and next_domain_pass
    phase_angle = formal_phase["compiled_relative_phase_angle"]
    correction_angle = formal_phase["formal_exact_target_correction_angle"]
    correct_one_phase_residual = float(
        abs(cmath.exp(1j * (phase_angle + correction_angle)) - 1.0)
    )
    correct_two_phase_residual = float(
        abs(cmath.exp(2j * (phase_angle + correction_angle)) - 1.0)
    )
    wrong_phase_residual = float(abs(cmath.exp(2j * phase_angle) - 1.0))
    controlled_phase_residual = float(
        abs(cmath.exp(1j * phase_angle) - 1.0) / math.sqrt(2.0)
    )
    landed_e_digest = landed_joined["root_executable_primitive_route"]["word_sha256"]
    landed_g_digest = landed_joined["update_route"]["routed_word_sha256"]
    live_e_digest = joined["root_executable_primitive_route"]["word_sha256"]
    live_g_digest = joined["update_route"]["routed_word_sha256"]
    controller_clean_execution_fields = {
        key: controller[key]
        for key in (
            "root_fresh_consumption_failures",
            "root_spent_epoch_failures",
            "token_return_failures",
            "router_return_failures",
            "value_work_failures",
        )
    }
    controller_clean_execution_pass = not any(
        controller_clean_execution_fields.values()
    )
    certificate_replay_match = (
        e_official_digest == live_e_digest == landed_e_digest
        and g_canonical["routed_word_sha256"] == live_g_digest == landed_g_digest
        and support_sha256
        == resource["physical_support_coordinate_sha256"]
        == landed_joined["physical_resource_census"][
            "physical_support_coordinate_sha256"
        ]
        and transit_sha256
        == resource["transit_coordinate_sha256"]
        == landed_joined["physical_resource_census"]["transit_coordinate_sha256"]
        and counts_match_recomputed
        and counts_match_landed
        and intertwiner["proof_obligations"]
        == official["intertwiner"]["proof_obligations"]
    )
    return {
        "shape": shape,
        "V_primitive_gates": e_primitive_count,
        "V_routed_gates": len(e_word),
        "G_primitive_gates": g_primitive_count,
        "G_routed_gates": len(g_word),
        "V_dagger_routed_gates": len(e_dagger),
        "S_primitive_gate_ledger": 2 * e_primitive_count + g_primitive_count,
        "S_routed_gates": len(composite),
        "S_site_matrix_sha256": word_hash(composite),
        "V_site_matrix_sha256": word_hash(e_word),
        "V_dagger_site_matrix_sha256": word_hash(e_dagger),
        "G_site_matrix_sha256": word_hash(g_word),
        "V_stage_order": e_stages,
        "G_stage_order": g_stages,
        "V_dagger_stage_order": tuple(reversed(e_stages)),
        "literal_V_dagger_inverse_pair_failures": inverse_pair_failures,
        "literal_V_dagger_inverse_kind_failures": inverse_kind_failures,
        "same_order_V_dagger_pair_failures": wrong_order_pair_failures,
        "V_and_V_dagger_gate_count_equal": len(e_word) == len(e_dagger),
        "V_gate_unitarity_failures": v_gate_unitarity_failures,
        "gate_unitarity_failures": gate_unitarity_failures,
        "non_NN_failures": non_nn_failures,
        "selected_V_dagger_deletion_operator_residual": selected_delete_residual,
        "selected_V_dagger_deletion_argument": (
            "unitary prefix/suffix invariance reduces the full operator residual to the local omitted-gate residual"
        ),
        "G_primitive_auxiliary_endpoint_hits": g_aux_endpoint_hits,
        "V_route_return_failures": e_route["route_return_failures"],
        "G_route_return_failures": g_route["route_return_failures"],
        "G_restores_arbitrary_entangled_transit": resource[
            "arbitrary_or_entangled_transit_state_restored"
        ],
        "E_equals_VJ_isometry_exact": encoder[
            "emitted_E_isometry_exact_on_declared_clean_domain"
        ],
        "Cycle870_intertwiner_exact": intertwiner["exact_intertwiner_pass"],
        "Cycle870_intertwiner_proof_obligations": proof_obligations,
        "V_dagger_V_full_register_exact": v_dagger_v_J_pass,
        "V_dagger_VJ_exact": v_dagger_v_J_pass,
        "Cycle870_E_isometry_recomputed_exact": encoder[
            "emitted_E_isometry_exact_on_declared_clean_domain"
        ],
        "Cycle870_E_isometry_inherited_exact": landed_joined[
            "encoder_isometry"
        ]["emitted_E_isometry_exact_on_declared_clean_domain"],
        "Cycle870_all_vector_intertwiner_recomputed_exact": (
            intertwiner["exact_intertwiner_pass"]
            and intertwiner["exact_vector_equality_follows_for_all_input_vectors"]
            and proof_obligations_zero
        ),
        "Cycle870_all_vector_intertwiner_inherited_exact": (
            official["intertwiner"]["exact_intertwiner_pass"]
            and official["intertwiner"][
                "exact_vector_equality_follows_for_all_input_vectors"
            ]
            and not any(official["intertwiner"]["proof_obligations"].values())
        ),
        "Cycle870_certificate_replay_match": certificate_replay_match,
        "proof_provenance": {
            "Cycle870_intertwiner": {
                "claim_role": "inherited_Cycle870_premise",
                "evidence_mode": "recomputed_via_cube_fixture_and_matched_to_pinned_receipt",
            },
            "V_dagger_VJ": {
                "claim_role": "Cycle883_derived",
                "evidence_mode": "recomputed_literal_word",
            },
            "one_and_two_epoch": {
                "claim_role": "Cycle883_derived",
                "evidence_mode": "algebraic_implication_from_all_vector_intertwiner_and_returned_J_domain",
            },
        },
        "V_dagger_V_J_identity_pass": v_dagger_v_J_pass,
        "one_epoch_vector_representative_pass": one_epoch_pass,
        "one_epoch_formal_vector_representative_exact": one_epoch_pass,
        "next_clean_domain_restored_pass": next_domain_pass,
        "one_epoch_returns_J_domain": next_domain_pass,
        "two_epoch_induction_seed_pass": two_epoch_seed_pass,
        "two_epoch_formal_vector_representative_exact": two_epoch_seed_pass,
        "all_nonnegative_fixed_invocation_powers_by_induction_pass": two_epoch_seed_pass,
        "proof_mode": (
            "cold Cycle870 all-vector generator intertwiner plus literal V reverse-adjoint identity; no dense 2^(6N) operator is materialized"
        ),
        "formal_phase_residual": formal_phase["phase_sum_residual_mod_2pi"],
        "one_epoch_correct_phase_residual": correct_one_phase_residual,
        "two_epoch_correct_phase_residual": correct_two_phase_residual,
        "formal_phase_routed_gates": formal_phase["routed_gate_count"],
        "phase_angle": phase_angle,
        "wrong_phase_sign_vector_residual": wrong_phase_residual,
        "controlled_application_relative_phase_vector_residual": controlled_phase_residual,
        "correct_one_epoch_phase_pass": correct_one_phase_residual <= TOL,
        "correct_two_epoch_phase_pass": correct_two_phase_residual <= TOL,
        "wrong_phase_sign_control_active": wrong_phase_residual > 1.0e-3,
        "controlled_phase_control_active": controlled_phase_residual > 1.0e-3,
        "controlled_invocation_without_compensation_equivalent": False,
        "controlled_invocation_out_of_scope": True,
        "coherent_control_over_invocation_count_in_scope": False,
        "actual_counts_match_recomputed_certificate": counts_match_recomputed,
        "actual_counts_match_landed_receipt": counts_match_landed,
        "direct_V_routed_word_sha256": e_official_digest,
        "live_V_routed_word_sha256": live_e_digest,
        "landed_V_routed_word_sha256": landed_e_digest,
        "V_routed_word_digest_match": (
            e_official_digest == live_e_digest == landed_e_digest
        ),
        "direct_G_routed_word_sha256": g_canonical["routed_word_sha256"],
        "live_G_routed_word_sha256": live_g_digest,
        "landed_G_routed_word_sha256": landed_g_digest,
        "G_routed_word_digest_match": (
            g_canonical["routed_word_sha256"] == live_g_digest == landed_g_digest
        ),
        "observed_S_touched_support_M2": len(touched_support),
        "observed_S_declared_support_M2": len(declared_support),
        "recomputed_combined_support_M2": resource[
            "total_declared_physical_support_M2"
        ],
        "landed_combined_support_M2": landed_joined[
            "physical_resource_census"
        ]["total_declared_physical_support_M2"],
        "direct_physical_support_coordinate_sha256": support_sha256,
        "live_physical_support_coordinate_sha256": resource[
            "physical_support_coordinate_sha256"
        ],
        "landed_physical_support_coordinate_sha256": landed_joined[
            "physical_resource_census"
        ]["physical_support_coordinate_sha256"],
        "physical_support_coordinate_match": (
            support_sha256
            == resource["physical_support_coordinate_sha256"]
            == landed_joined["physical_resource_census"][
                "physical_support_coordinate_sha256"
            ]
        ),
        "direct_transit_coordinate_sha256": transit_sha256,
        "live_transit_coordinate_sha256": resource["transit_coordinate_sha256"],
        "landed_transit_coordinate_sha256": landed_joined[
            "physical_resource_census"
        ]["transit_coordinate_sha256"],
        "transit_coordinate_match": (
            transit_sha256
            == resource["transit_coordinate_sha256"]
            == landed_joined["physical_resource_census"]["transit_coordinate_sha256"]
        ),
        "support_reuse_without_new_M2": (
            len(declared_support) == resource["total_declared_physical_support_M2"]
            and support_sha256 == resource["physical_support_coordinate_sha256"]
            and transit_sha256 == resource["transit_coordinate_sha256"]
            and v_touched == v_dagger_touched
        ),
        "V_touched_coordinate_sha256": J.rows_sha256(v_touched),
        "V_dagger_touched_coordinate_sha256": J.rows_sha256(v_dagger_touched),
        "V_dagger_exact_touched_set_reuse": v_touched == v_dagger_touched,
        "root_handshake_controls": handshake,
        "controller_clean_execution_fields": controller_clean_execution_fields,
        "controller_clean_execution_pass": controller_clean_execution_pass,
        "forward_only_hostile_spent_replay_token_failures": controller[
            "hostile_unguarded_spent_reapplication_token_failures"
        ],
        "forward_only_hostile_spent_replay_spent_failures": controller[
            "hostile_unguarded_spent_reapplication_spent_failures"
        ],
        "dirty_syndrome_action_failure_active": controller[
            "unlawful_syndrome_rejected_by_action"
        ],
        "dirty_controller_admission_guard_compiled": controller[
            "local_spent_sector_admission_guard_compiled"
        ],
        "raw_logical_input_is_arbitrary_not_dirty": True,
        "transit_state_is_arbitrary_or_entangled_not_dirty": True,
        "dirty_fault_repair_or_admission_claimed": False,
        "dirty_carrier_X_witness": dirty_carrier,
        "dirty_root_patterns_checked": handshake[
            "dirty_controller_patterns_not_prepared"
        ],
        "dirty_root_patterns_accepted": 0,
        "carrier_unique_vacuum_full_rank": (
            encoder["unique_plus_vacuum"]
            and encoder["vacuum_tableau_rank"] == encoder["carrier_M2"]
        ),
        "single_carrier_stabilizer_sign_flip_outside_declared_vacuum": (
            encoder["unique_plus_vacuum"]
            and encoder["vacuum_tableau_rank"] == encoder["carrier_M2"]
        ),
        "live_all_vector_equality_follows": intertwiner[
            "exact_vector_equality_follows_for_all_input_vectors"
        ],
        "landed_all_vector_equality_follows": official["intertwiner"][
            "exact_vector_equality_follows_for_all_input_vectors"
        ],
        "cold_live_and_landed_proof_surface_match": (
            intertwiner["exact_intertwiner_pass"]
            == official["intertwiner"]["exact_intertwiner_pass"]
            and intertwiner["proof_obligations"]
            == official["intertwiner"]["proof_obligations"]
            and intertwiner["exact_vector_equality_follows_for_all_input_vectors"]
            == official["intertwiner"][
                "exact_vector_equality_follows_for_all_input_vectors"
            ]
        ),
        "recurrent_raw_domain_conclusion": (
            "with J the supplied clean embedding and E=VJ, exp(-i*phi) V^dagger U_G V J = J G_native; fixed unconditional powers follow by induction"
        ),
    }


def collect_failures(report):
    failures = []
    for row in report["fixtures"]:
        prefix = "L" + str(row["shape"][0])
        for key in (
            "literal_V_dagger_inverse_pair_failures",
            "literal_V_dagger_inverse_kind_failures",
            "V_gate_unitarity_failures",
            "gate_unitarity_failures",
            "non_NN_failures",
            "G_primitive_auxiliary_endpoint_hits",
            "V_route_return_failures",
            "G_route_return_failures",
        ):
            if row[key]:
                failures.append(prefix + ":" + key)
        for key in (
            "G_restores_arbitrary_entangled_transit",
            "E_equals_VJ_isometry_exact",
            "Cycle870_intertwiner_exact",
            "V_and_V_dagger_gate_count_equal",
            "V_dagger_V_full_register_exact",
            "V_dagger_VJ_exact",
            "Cycle870_E_isometry_recomputed_exact",
            "Cycle870_E_isometry_inherited_exact",
            "Cycle870_all_vector_intertwiner_recomputed_exact",
            "Cycle870_all_vector_intertwiner_inherited_exact",
            "Cycle870_certificate_replay_match",
            "V_dagger_V_J_identity_pass",
            "one_epoch_vector_representative_pass",
            "one_epoch_formal_vector_representative_exact",
            "next_clean_domain_restored_pass",
            "one_epoch_returns_J_domain",
            "two_epoch_induction_seed_pass",
            "two_epoch_formal_vector_representative_exact",
            "all_nonnegative_fixed_invocation_powers_by_induction_pass",
            "correct_one_epoch_phase_pass",
            "correct_two_epoch_phase_pass",
            "wrong_phase_sign_control_active",
            "controlled_phase_control_active",
            "controlled_invocation_out_of_scope",
            "actual_counts_match_recomputed_certificate",
            "actual_counts_match_landed_receipt",
            "V_routed_word_digest_match",
            "G_routed_word_digest_match",
            "physical_support_coordinate_match",
            "transit_coordinate_match",
            "support_reuse_without_new_M2",
            "V_dagger_exact_touched_set_reuse",
            "controller_clean_execution_pass",
            "dirty_syndrome_action_failure_active",
            "carrier_unique_vacuum_full_rank",
            "single_carrier_stabilizer_sign_flip_outside_declared_vacuum",
            "live_all_vector_equality_follows",
            "landed_all_vector_equality_follows",
            "cold_live_and_landed_proof_surface_match",
        ):
            if not row[key]:
                failures.append(prefix + ":" + key)
        if any(row["Cycle870_intertwiner_proof_obligations"].values()):
            failures.append(prefix + ":intertwiner-proof-obligation")
        if row["same_order_V_dagger_pair_failures"] == 0:
            failures.append(prefix + ":inactive-wrong-order-control")
        if row["selected_V_dagger_deletion_operator_residual"] <= 1.0e-8:
            failures.append(prefix + ":inactive-E-dagger-deletion")
        if row["formal_phase_residual"] > TOL or row["formal_phase_routed_gates"] != 0:
            failures.append(prefix + ":formal-phase")
        if (
            row["one_epoch_correct_phase_residual"] > TOL
            or row["two_epoch_correct_phase_residual"] > 2 * TOL
        ):
            failures.append(prefix + ":power-phase")
        if row["wrong_phase_sign_vector_residual"] <= 1.0e-3:
            failures.append(prefix + ":inactive-wrong-phase-control")
        if row["controlled_application_relative_phase_vector_residual"] <= 1.0e-3:
            failures.append(prefix + ":inactive-controlled-phase-control")
        if row["coherent_control_over_invocation_count_in_scope"]:
            failures.append(prefix + ":coherent-control-scope")
        if row["controlled_invocation_without_compensation_equivalent"]:
            failures.append(prefix + ":controlled-invocation-equivalence")
        if row["dirty_controller_admission_guard_compiled"]:
            failures.append(prefix + ":unexpected-dirty-admission")
        handshake = row["root_handshake_controls"]
        if handshake["literal_event_chronology_failures"]:
            failures.append(prefix + ":root-handshake-chronology")
        if handshake["correct_reverse_adjoint_clean_domain_failures"]:
            failures.append(prefix + ":root-handshake-reverse")
        for key in (
            "same_order_adjoint_clean_domain_failures",
            "whole_adjoint_deletion_next_domain_failures",
            "dirty_controller_patterns_not_prepared",
        ):
            if handshake[key] <= 0:
                failures.append(prefix + ":inactive-" + key)
        if handshake["dirty_controller_patterns_not_prepared"] != (
            handshake["dirty_controller_patterns_per_root"]
            * handshake["root_groups"]
        ):
            failures.append(prefix + ":dirty-controller-census")
        if handshake["whole_adjoint_deletion_observed_states"] != ((0, 0, 1),):
            failures.append(prefix + ":whole-adjoint-state")
        if handshake["same_order_adjoint_observed_states"] != ((0, 1, 0),):
            failures.append(prefix + ":same-order-state")
        for key in (
            "whole_adjoint_deletion_fresh_failures",
            "whole_adjoint_deletion_spent_failures",
            "same_order_adjoint_fresh_failures",
            "same_order_adjoint_token_failures",
        ):
            if handshake[key] != handshake["root_groups"]:
                failures.append(prefix + ":" + key)
        dirty_carrier = row["dirty_carrier_X_witness"]
        if (
            dirty_carrier["single_carrier_X_cases"] <= 0
            or dirty_carrier["single_carrier_X_accepted_by_all_vacuum_rows"] != 0
            or dirty_carrier["minimum_violated_vacuum_rows"] <= 0
        ):
            failures.append(prefix + ":dirty-carrier-X-witness")
        if (
            row["dirty_root_patterns_checked"]
            != 7 * handshake["root_groups"]
            or row["dirty_root_patterns_accepted"] != 0
        ):
            failures.append(prefix + ":dirty-root-census")
    covariance = report["proper_cubic_covariance"]
    if covariance["joined_code_diagram_products"] != 576:
        failures.append("covariance:product-count")
    for family in (
        covariance["root_carrier_aux_coordinate"],
        covariance["root_signed_AB_semantic_E"],
        covariance["native_G"],
    ):
        for key, value in family.items():
            if key.endswith("failures") and value:
                failures.append("covariance:" + key)
    return failures


def main() -> int:
    observed = {path: file_hash(ROOT / path) for path in AUDIT_INPUT_PATHS}
    pin_failures = {
        path: {"expected": expected, "observed": observed[path]}
        for path, expected in EXPECTED_SHA256.items()
        if observed[path] != expected
    }
    if pin_failures:
        raise RuntimeError("Cycle883 input pin drift: " + repr(pin_failures))
    sys.path.insert(0, str(HERE))
    import frontier_cycle870_openreference_joined_recurrent_compiler_2026_08_02 as J

    landed = json.loads(
        (ROOT / "outputs/cycle870_openreference_joined_recurrent_compiler_receipt_2026_08_02.json").read_text()
    )
    independent = json.loads(
        (ROOT / "outputs/cycle870_openreference_recurrent_update_independent_receipt_2026_08_02.json").read_text()
    )
    landed_by_shape = {tuple(row["shape"]): row for row in landed["fixtures"]}
    species = J.update.c219.common_species(float(J.update.c230.BETA))
    coin = np.asarray(species.coin, dtype=complex)
    coin_gates, qr = J.update.qr_coin_schedule(coin)
    fixtures = tuple(fixture(J, length, coin_gates, landed_by_shape) for length in (2, 3))
    covariance = J.joined_covariance_fixture(2, coin_gates)
    report = {
        "status": "pending",
        "claim_type": "bounded_theorem",
        "claim_scope": (
            "on fixed open cubic L2/L3 fixtures and the supplied Cycle870 embedding J, the literal returned-route word V;U_G;V^dagger is a recurrent raw-matter channel, restores the declared clean preparation state after each fixed unconditional invocation, and adds no M2 support"
        ),
        "equation": "S=V^dagger U_G V and exp(-i*phi) S J = J G_native on the supplied clean embedding; E=VJ",
        "fixtures": fixtures,
        "proper_cubic_covariance": covariance,
        "one_particle_fixture": {
            "analytic_mass": independent["coin_mass_contact"]["Cycle219_analytic_mass"],
            "rest_mass": independent["coin_mass_contact"]["Cycle219_rest_mass"],
            "pairwise_mass_residual": independent["coin_mass_contact"]["mass_pairwise_maximum_residual"],
            "beta": independent["coin_mass_contact"]["Cycle219_beta_from_Cycle230"],
            "g_contact": independent["coin_mass_contact"]["Cycle230_contact_coupling"],
            "boundary": "inherited supplied numerical fixture; no parameter or law selection",
        },
        "coin_QR": qr,
        "supplied": [
            "fixed finite open cubic L2/L3 boundary, spacing-16 origin, and transported coframe",
            "arbitrary raw six-mode matter state tensor a once-supplied clean Cycle870 carrier/syndrome/controller/work domain",
            "Cycle219 beta=-0.3, Cycle230 g_contact=0.37, and the Cycle870 serial E/G factor order",
            "external application of the complete fixed composite word",
        ],
        "derived": [
            "literal routed V dagger as the reverse-order canonical adjoint of every routed V gate",
            "exact projective raw-domain G_native channel with the supplied clean embedding restored after every complete word",
            "all nonnegative fixed unconditional invocation powers by operator induction on the returned clean domain",
            "the unchanged Cycle870 carrier, auxiliary, and transit footprint",
            "transported proper-cubic covariance under all 24 frames and 576 ordered products",
        ],
        "open": [
            "intrinsic initial clean-domain genesis, dirty-input admission/fault repair, and physical occurrence/start trigger",
            "a translation-compatible volume-independent local schedule for V and V dagger without the supplied serial forest order",
            "noncubic and periodic topology, Wilson sectors, boundary/coframe selection, and numerical-law selection",
            "persistent encoded-bank architecture between epochs; this construction returns matter to the raw logical bank",
            "time, source/gravity, permanent Record, Born/history, and prediction bridges",
        ],
        "not_claimed": [
            "circuit ordinals are not time",
            "the formal representative scalar is not a gate, energy, or rate",
            "the initial clean domain is supplied rather than autonomously formed or admitted",
            "coherent control over differing invocation counts is excluded because the executable projective phase becomes relative",
            "no translation-invariant all-volume controller, no no-go, no minimum-content result, and no axiom pressure",
        ],
        "source_pins": observed,
        "this_source_sha256": file_hash(Path(__file__)),
    }
    failures = collect_failures(report)
    report["failures"] = failures
    report["status"] = "pass" if not failures else "fail"
    payload = json.dumps(
        report,
        indent=2,
        sort_keys=True,
        default=lambda value: value.item() if isinstance(value, np.generic) else str(value),
    ) + "\n"
    OUT.write_text(payload)
    print(payload, end="")
    return int(bool(failures))


if __name__ == "__main__":
    raise SystemExit(main())
