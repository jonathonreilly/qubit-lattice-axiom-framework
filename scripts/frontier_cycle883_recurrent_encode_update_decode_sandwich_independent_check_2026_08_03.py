#!/usr/bin/env python3
"""Independent Cycle-883 inverse-routing and proof-obligation check.

This checker does not import the Cycle-883 primary runner. It constructs
V^dagger from the unrouted primitive word, routes that inverse independently,
re-executes the Cycle-870 all-vector proof obligations, and compares only the
final receipt surface.
"""
from __future__ import annotations

import cmath
from hashlib import sha256
import json
import math
from pathlib import Path
import sys

import numpy as np


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
PRIMARY_SOURCE = HERE / "frontier_cycle883_recurrent_encode_update_decode_sandwich_2026_08_03.py"
PRIMARY_RECEIPT = ROOT / "outputs/cycle883_recurrent_encode_update_decode_sandwich_primary_receipt_2026_08_03.json"
OUT = ROOT / "outputs/cycle883_recurrent_encode_update_decode_sandwich_independent_receipt_2026_08_03.json"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle883_recurrent_encode_update_decode_sandwich_core_2026_08_03.py",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/OPENREFERENCE_CUBIC_RECURRENT_PHYSICAL_M2_MATTER_COMPILER_CYCLE870_BOUNDED_THEOREM_NOTE_2026-08-02.md",
    "scripts/frontier_cycle870_openreference_joined_recurrent_compiler_2026_08_02.py",
    "scripts/frontier_cycle870_openreference_native_recurrent_update_2026_08_02.py",
    "scripts/frontier_cycle870_openreference_physical_m2_placement_2026_08_02.py",
    "outputs/cycle870_openreference_joined_recurrent_compiler_receipt_2026_08_02.json",
    "scripts/frontier_cycle883_recurrent_encode_update_decode_sandwich_2026_08_03.py",
    "outputs/cycle883_recurrent_encode_update_decode_sandwich_primary_receipt_2026_08_03.json",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS
TOL = 3.0e-10

INVERSE_KIND = {
    "route_swap": "route_swap",
    "check_parity_CNOT": "check_parity_CNOT",
    "check_basis_H": "check_basis_H",
    "loader_controlled_Z": "loader_controlled_Z",
    "loader_parity_CNOT": "loader_parity_CNOT",
    "syndrome_controlled_Z": "syndrome_controlled_Z",
    "controller_Toffoli_CNOT": "controller_Toffoli_CNOT",
    "check_sign_X": "check_sign_X",
    "controller_Toffoli_T": "controller_Toffoli_Tdg",
    "check_basis_Sdg": "check_basis_S",
    "check_basis_S": "check_basis_Sdg",
    "controller_Toffoli_Tdg": "controller_Toffoli_T",
    "controller_Toffoli_H": "controller_Toffoli_H",
    "loader_target_Sdg": "loader_target_S",
    "loader_controlled_X_for_Y": "loader_controlled_X_for_Y",
    "loader_target_S": "loader_target_Sdg",
    "controller_CCZ_H": "controller_CCZ_H",
    "controller_router_CNOT_right_left": "controller_router_CNOT_right_left",
    "controller_router_X_right_pre": "controller_router_X_right_pre",
    "controller_router_X_right_post": "controller_router_X_right_post",
    "controller_token_SWAP_down": "controller_token_SWAP_down",
    "controller_token_SWAP_up": "controller_token_SWAP_up",
    "controller_root_fresh_to_token_SWAP": "controller_root_fresh_to_token_SWAP",
    "controller_root_token_to_spent_SWAP": "controller_root_token_to_spent_SWAP",
    "controller_router_X_left": "controller_router_X_left",
    "controller_router_CNOT_left_right": "controller_router_CNOT_left_right",
    "controller_router_X_right": "controller_router_X_right",
}


def file_hash(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def canonical_matrix_digest(matrix) -> str:
    matrix = np.asarray(matrix, dtype=complex)
    real = np.round(matrix.real, 14)
    imag = np.round(matrix.imag, 14)
    real[np.abs(real) < 1.0e-14] = 0.0
    imag[np.abs(imag) < 1.0e-14] = 0.0
    return sha256(np.asarray(real + 1j * imag, dtype=complex).tobytes()).hexdigest()


def signature_hash(word) -> str:
    output = sha256()
    for row in word:
        output.update(repr((row.sites, canonical_matrix_digest(row.matrix))).encode())
    return output.hexdigest()


def independent_handshake_controls(events):
    grouped = {}
    for event in events:
        if event.atlas_role and event.atlas_role[0] == "controller_root_epoch":
            grouped.setdefault((event.owner, event.atlas_role[1]), []).append(event)

    chronology_failures = reverse_failures = same_order_failures = 0
    no_adjoint_failures = dirty_failures = 0
    deleted_states = set()
    same_order_states = set()
    delete_fresh_failures = delete_spent_failures = 0
    same_fresh_failures = same_token_failures = 0

    def run(rows, bits):
        bits = dict(bits)
        for event in rows:
            left, right = event.sites
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
        token2, spent = second.sites
        chronology_failures += token != token2
        clean = {fresh: 1, token: 0, spent: 0}
        target = {fresh: 0, token: 0, spent: 1}
        encoded = run(rows, clean)
        chronology_failures += encoded != target
        reverse_failures += run(tuple(reversed(rows)), encoded) != clean
        same = run(rows, encoded)
        same_order_failures += same != clean
        no_adjoint_failures += encoded != clean
        deleted_states.add((encoded[fresh], encoded[token], encoded[spent]))
        same_order_states.add((same[fresh], same[token], same[spent]))
        delete_fresh_failures += encoded[fresh] != clean[fresh]
        delete_spent_failures += encoded[spent] != clean[spent]
        same_fresh_failures += same[fresh] != clean[fresh]
        same_token_failures += same[token] != clean[token]
        for value in range(8):
            candidate = {
                fresh: (value >> 2) & 1,
                token: (value >> 1) & 1,
                spent: value & 1,
            }
            dirty_failures += candidate != clean and run(rows, candidate) != target
    return {
        "root_groups": len(grouped),
        "literal_event_chronology_failures": chronology_failures,
        "correct_reverse_adjoint_clean_domain_failures": reverse_failures,
        "same_order_adjoint_clean_domain_failures": same_order_failures,
        "whole_adjoint_deletion_next_domain_failures": no_adjoint_failures,
        "state_order": ("fresh", "token", "spent"),
        "whole_adjoint_deletion_observed_states": tuple(sorted(deleted_states)),
        "whole_adjoint_deletion_fresh_failures": delete_fresh_failures,
        "whole_adjoint_deletion_spent_failures": delete_spent_failures,
        "same_order_adjoint_observed_states": tuple(sorted(same_order_states)),
        "same_order_adjoint_fresh_failures": same_fresh_failures,
        "same_order_adjoint_token_failures": same_token_failures,
        "dirty_controller_patterns_not_prepared": dirty_failures,
    }


def independent_dirty_carrier_X_witness(J, graph, context):
    rows = tuple(J.update.physical_stabilizers(context)) + tuple(
        J.update.physical_lift(zrow, context)
        for _cell, _mode, _xrow, zrow in J.root.logical_rows(graph)
    )
    violations = tuple(
        sum(
            not J.Pauli(x=1 << context.index[site]).commutes(row)
            for row in rows
        )
        for site in context.sites
    )
    return {
        "single_carrier_X_cases": len(violations),
        "single_carrier_X_accepted_by_all_vacuum_rows": sum(
            value == 0 for value in violations
        ),
        "minimum_violated_vacuum_rows": min(violations),
        "maximum_violated_vacuum_rows": max(violations),
    }


def encoder_primitive(J, length, graph, site_map, context):
    shape = (length, length, length)
    syndrome = J.root.syndrome_interactions(graph, site_map)
    corrections = J.root.correction_interactions(graph, site_map)
    loader = J.root.loader_interactions(graph, site_map)
    controller = J.root.controller_interactions(shape, graph, site_map)
    checks, _ = J.coherent_check_primitives(graph, context, syndrome)
    correction = J.correction_primitives(corrections)
    controller_ops, controller_events, _chronology = J.controller_chronology_primitives(
        shape, graph, site_map, controller
    )
    loader_ops, _ = J.loader_primitives(graph, context, loader)
    stages = (
        checks["triangle_syndrome"],
        correction["triangle_correction"],
        checks["coarse_syndrome"],
        controller_ops,
        checks["bond_syndrome"],
        correction["bond_correction"],
        loader_ops,
    )
    return (
        tuple(
            J.update.c707.Instruction(row.kind, row.sites, row.matrix)
            for stage in stages
            for row in stage
        ),
        tuple(controller_events),
    )


def update_primitive(J, graph, context, coin_gates):
    rotations, _inventory = J.update.build_update(graph, coin_gates)
    return tuple(
        instruction
        for rotation in rotations
        for instruction in J.update.c707.compile_pauli_rotation(
            J.update.physical_lift(rotation.row, context),
            context.sites,
            rotation.angle,
        )
    )


def fixture(J, length, coin_gates, primary_row):
    shape = (length, length, length)
    graph = J.update.prep.OpenReferenceGraph(J.root.box(shape))
    site_map = J.root.carrier_placement(graph)
    context = J.update.physical_context(graph)
    auxiliary = J.auxiliary_registers(graph)
    e_primitive, controller_events = encoder_primitive(
        J, length, graph, site_map, context
    )
    g_primitive = update_primitive(J, graph, context, coin_gates)
    d_primitive = tuple(
        J.update.c707.Instruction(
            INVERSE_KIND[row.kind],
            row.sites,
            np.asarray(row.matrix, dtype=complex).conj().T,
        )
        for row in reversed(e_primitive)
    )
    routed_e, cert_e = J.update.c707.route_word(e_primitive)
    routed_g, cert_g = J.update.c707.route_word(g_primitive)
    routed_d, cert_d = J.update.c707.route_word(d_primitive)
    expected_d = tuple(reversed(routed_e))
    inverse_site_failures = sum(
        left.sites != right.sites
        for left, right in zip(routed_d, expected_d)
    ) + abs(len(routed_d) - len(expected_d))
    inverse_matrix_failures = sum(
        not np.allclose(left.matrix, right.matrix.conj().T, atol=1.0e-12)
        for left, right in zip(routed_d, expected_d)
    ) + abs(len(routed_d) - len(expected_d))
    inverse_kind_failures = sum(
        left.kind != INVERSE_KIND[right.kind]
        for left, right in zip(routed_d, expected_d)
    ) + abs(len(routed_d) - len(expected_d))
    live = J.cube_fixture(length, coin_gates)
    joined = live["joined_route"]
    obligations = live["intertwiner"]["proof_obligations"]
    proof_failures = {key: value for key, value in obligations.items() if value}
    g_aux_hits = sum(site in auxiliary for row in g_primitive for site in row.sites)
    composite = (*routed_e, *routed_g, *routed_d)
    composite_hash = signature_hash(composite)
    selected = next(
        row
        for row in routed_d
        if np.linalg.norm(row.matrix - np.eye(row.matrix.shape[0])) > 1.0e-8
    )
    deletion_residual = float(
        np.linalg.norm(selected.matrix - np.eye(selected.matrix.shape[0]))
    )
    touched = (
        set(cert_e["touched_coordinates"])
        | set(cert_g["touched_coordinates"])
        | set(cert_d["touched_coordinates"])
    )
    declared_bank = set(context.sites) | set(auxiliary)
    transit = touched - declared_bank
    support = declared_bank | transit
    support_sha256 = J.rows_sha256(support)
    transit_sha256 = J.rows_sha256(transit)
    rotations, _inventory = J.update.build_update(graph, coin_gates)
    canonical_g = J.update.route_update(context, rotations)
    handshake = independent_handshake_controls(controller_events)
    dirty_carrier = independent_dirty_carrier_X_witness(J, graph, context)
    v_touched = {site for row in routed_e for site in row.sites}
    v_dagger_touched = {site for row in routed_d for site in row.sites}
    phase = joined["exact_global_phase"]
    phase_angle = phase["compiled_relative_phase_angle"]
    correction_angle = phase["formal_exact_target_correction_angle"]
    correct_one = float(
        abs(cmath.exp(1j * (phase_angle + correction_angle)) - 1.0)
    )
    correct_two = float(
        abs(cmath.exp(2j * (phase_angle + correction_angle)) - 1.0)
    )
    v_dagger_v_J_pass = (
        len(routed_e) == len(routed_d)
        and inverse_site_failures == 0
        and inverse_matrix_failures == 0
        and inverse_kind_failures == 0
        and cert_e["route_return_failures"] == 0
    )
    one_epoch_pass = (
        v_dagger_v_J_pass
        and live["intertwiner"]["exact_intertwiner_pass"]
        and live["intertwiner"][
            "exact_vector_equality_follows_for_all_input_vectors"
        ]
        and not proof_failures
        and joined["encoder_isometry"][
            "emitted_E_isometry_exact_on_declared_clean_domain"
        ]
        and phase["phase_sum_residual_mod_2pi"] <= TOL
    )
    next_domain_pass = (
        one_epoch_pass
        and g_aux_hits == 0
        and handshake["correct_reverse_adjoint_clean_domain_failures"] == 0
    )
    two_epoch_seed_pass = one_epoch_pass and next_domain_pass
    return {
        "shape": shape,
        "independent_V_routed_gates": len(routed_e),
        "independent_G_routed_gates": len(routed_g),
        "independent_V_dagger_routed_gates": len(routed_d),
        "independent_S_routed_gates": len(composite),
        "independent_S_site_matrix_sha256": composite_hash,
        "primary_S_site_matrix_sha256": primary_row["S_site_matrix_sha256"],
        "primary_word_match": composite_hash == primary_row["S_site_matrix_sha256"],
        "inverse_route_site_failures": inverse_site_failures,
        "inverse_route_matrix_failures": inverse_matrix_failures,
        "inverse_route_kind_failures": inverse_kind_failures,
        "V_route_return_failures": cert_e["route_return_failures"],
        "G_route_return_failures": cert_g["route_return_failures"],
        "V_dagger_route_return_failures": cert_d["route_return_failures"],
        "G_primitive_auxiliary_endpoint_hits": g_aux_hits,
        "independent_V_routed_word_sha256": cert_e["word_sha256"],
        "live_V_routed_word_sha256": joined[
            "root_executable_primitive_route"
        ]["word_sha256"],
        "primary_V_routed_word_sha256": primary_row[
            "direct_V_routed_word_sha256"
        ],
        "V_routed_word_digest_match": (
            cert_e["word_sha256"]
            == joined["root_executable_primitive_route"]["word_sha256"]
            == primary_row["direct_V_routed_word_sha256"]
        ),
        "independent_G_routed_word_sha256": canonical_g["routed_word_sha256"],
        "live_G_routed_word_sha256": joined["update_route"]["routed_word_sha256"],
        "primary_G_routed_word_sha256": primary_row[
            "direct_G_routed_word_sha256"
        ],
        "G_routed_word_digest_match": (
            canonical_g["routed_word_sha256"]
            == joined["update_route"]["routed_word_sha256"]
            == primary_row["direct_G_routed_word_sha256"]
        ),
        "independent_physical_support_coordinate_sha256": support_sha256,
        "live_physical_support_coordinate_sha256": joined[
            "physical_resource_census"
        ]["physical_support_coordinate_sha256"],
        "primary_physical_support_coordinate_sha256": primary_row[
            "direct_physical_support_coordinate_sha256"
        ],
        "physical_support_coordinate_match": (
            support_sha256
            == joined["physical_resource_census"][
                "physical_support_coordinate_sha256"
            ]
            == primary_row["direct_physical_support_coordinate_sha256"]
        ),
        "independent_transit_coordinate_sha256": transit_sha256,
        "live_transit_coordinate_sha256": joined["physical_resource_census"][
            "transit_coordinate_sha256"
        ],
        "primary_transit_coordinate_sha256": primary_row[
            "direct_transit_coordinate_sha256"
        ],
        "transit_coordinate_match": (
            transit_sha256
            == joined["physical_resource_census"]["transit_coordinate_sha256"]
            == primary_row["direct_transit_coordinate_sha256"]
        ),
        "independent_V_touched_coordinate_sha256": J.rows_sha256(v_touched),
        "independent_V_dagger_touched_coordinate_sha256": J.rows_sha256(
            v_dagger_touched
        ),
        "V_dagger_exact_touched_set_reuse": v_touched == v_dagger_touched,
        "live_Cycle870_intertwiner_exact": live["intertwiner"]["exact_intertwiner_pass"],
        "live_all_vector_equality_follows": live["intertwiner"][
            "exact_vector_equality_follows_for_all_input_vectors"
        ],
        "live_Cycle870_proof_failures": proof_failures,
        "live_E_equals_VJ_isometry_exact": joined["encoder_isometry"][
            "emitted_E_isometry_exact_on_declared_clean_domain"
        ],
        "independent_V_dagger_V_J_identity_pass": v_dagger_v_J_pass,
        "independent_one_epoch_vector_representative_pass": one_epoch_pass,
        "independent_next_clean_domain_restored_pass": next_domain_pass,
        "independent_two_epoch_induction_seed_pass": two_epoch_seed_pass,
        "primary_theorem_boolean_match": all(
            (
                primary_row["V_dagger_V_J_identity_pass"] == v_dagger_v_J_pass,
                primary_row["one_epoch_vector_representative_pass"] == one_epoch_pass,
                primary_row["next_clean_domain_restored_pass"] == next_domain_pass,
                primary_row["two_epoch_induction_seed_pass"] == two_epoch_seed_pass,
            )
        ),
        "independent_root_handshake_controls": handshake,
        "independent_dirty_carrier_X_witness": dirty_carrier,
        "one_epoch_correct_phase_residual": correct_one,
        "two_epoch_correct_phase_residual": correct_two,
        "wrong_phase_sign_vector_residual": float(
            abs(cmath.exp(2j * phase_angle) - 1.0)
        ),
        "controlled_application_relative_phase_vector_residual": float(
            abs(cmath.exp(1j * phase_angle) - 1.0) / math.sqrt(2.0)
        ),
        "selected_inverse_gate_deletion_operator_residual": deletion_residual,
        "power_proof_boundary": (
            "fixed unconditional powers follow from the independently reconstructed one-epoch equality and returned J domain; no zero residual is self-awarded for an unexecuted dense matrix"
        ),
    }


def collect_failures(report):
    failures = []
    for row in report["fixtures"]:
        prefix = "L" + str(row["shape"][0])
        for key in (
            "inverse_route_site_failures",
            "inverse_route_matrix_failures",
            "inverse_route_kind_failures",
            "V_route_return_failures",
            "G_route_return_failures",
            "V_dagger_route_return_failures",
            "G_primitive_auxiliary_endpoint_hits",
        ):
            if row[key]:
                failures.append(prefix + ":" + key)
        if not row["primary_word_match"]:
            failures.append(prefix + ":primary-word")
        if not row["live_Cycle870_intertwiner_exact"]:
            failures.append(prefix + ":intertwiner")
        if row["live_Cycle870_proof_failures"]:
            failures.append(prefix + ":proof-obligations")
        for key in (
            "V_routed_word_digest_match",
            "G_routed_word_digest_match",
            "physical_support_coordinate_match",
            "transit_coordinate_match",
            "V_dagger_exact_touched_set_reuse",
            "live_all_vector_equality_follows",
            "live_E_equals_VJ_isometry_exact",
            "independent_V_dagger_V_J_identity_pass",
            "independent_one_epoch_vector_representative_pass",
            "independent_next_clean_domain_restored_pass",
            "independent_two_epoch_induction_seed_pass",
            "primary_theorem_boolean_match",
        ):
            if not row[key]:
                failures.append(prefix + ":" + key)
        handshake = row["independent_root_handshake_controls"]
        if handshake["literal_event_chronology_failures"]:
            failures.append(prefix + ":handshake-chronology")
        if handshake["correct_reverse_adjoint_clean_domain_failures"]:
            failures.append(prefix + ":handshake-reverse")
        for key in (
            "same_order_adjoint_clean_domain_failures",
            "whole_adjoint_deletion_next_domain_failures",
            "dirty_controller_patterns_not_prepared",
        ):
            if handshake[key] <= 0:
                failures.append(prefix + ":inactive-" + key)
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
        dirty = row["independent_dirty_carrier_X_witness"]
        if (
            dirty["single_carrier_X_cases"] <= 0
            or dirty["single_carrier_X_accepted_by_all_vacuum_rows"] != 0
            or dirty["minimum_violated_vacuum_rows"] <= 0
        ):
            failures.append(prefix + ":dirty-carrier-X")
        if (
            row["one_epoch_correct_phase_residual"] > TOL
            or row["two_epoch_correct_phase_residual"] > 2 * TOL
        ):
            failures.append(prefix + ":power-phase")
        if row["wrong_phase_sign_vector_residual"] <= 1.0e-3:
            failures.append(prefix + ":inactive-wrong-phase")
        if row["controlled_application_relative_phase_vector_residual"] <= 1.0e-3:
            failures.append(prefix + ":inactive-controlled-phase")
        if row["selected_inverse_gate_deletion_operator_residual"] <= 1.0e-8:
            failures.append(prefix + ":inactive-inverse-deletion")
    return failures


def main() -> int:
    if not PRIMARY_RECEIPT.exists():
        raise RuntimeError("run the Cycle883 primary first")
    source_text = PRIMARY_SOURCE.read_text()
    required_anchors = (
        "e_word, *g_word, *e_dagger",
        "literal_V_dagger_inverse_pair_failures",
        "V_dagger_V_J_identity_pass",
        "two_epoch_induction_seed_pass",
        "Cycle870_intertwiner_proof_obligations",
        "the formal representative scalar is not a gate, energy, or rate",
    )
    anchor_failures = tuple(anchor for anchor in required_anchors if anchor not in source_text)
    sys.path.insert(0, str(HERE))
    import frontier_cycle870_openreference_joined_recurrent_compiler_2026_08_02 as J

    primary = json.loads(PRIMARY_RECEIPT.read_text())
    primary_by_shape = {tuple(row["shape"]): row for row in primary["fixtures"]}
    species = J.update.c219.common_species(float(J.update.c230.BETA))
    coin_gates, _qr = J.update.qr_coin_schedule(np.asarray(species.coin, dtype=complex))
    before = {path: file_hash(ROOT / path) for path in AUDIT_INPUT_PATHS}
    fixtures = tuple(
        fixture(J, length, coin_gates, primary_by_shape[(length, length, length)])
        for length in (2, 3)
    )
    after = {path: file_hash(ROOT / path) for path in AUDIT_INPUT_PATHS}
    report = {
        "status": "pending",
        "claim_scope": (
            "independent primitive-level inverse routing plus live Cycle870 all-vector proof-obligation reconstruction for the fixed L2/L3 recurrent sandwich"
        ),
        "fixtures": fixtures,
        "primary_source_sha256": file_hash(PRIMARY_SOURCE),
        "primary_receipt_sha256": file_hash(PRIMARY_RECEIPT),
        "primary_anchor_failures": anchor_failures,
        "sources_stable_through_execution": before == after,
        "source_sha256": before,
        "boundary": (
            "this independently verifies the bounded V^dagger U_G V raw-domain sandwich for E=VJ, not clean genesis, autonomous invocation, coherent control over invocation count, a translation-compatible all-volume V schedule, time, Record, Born, or gravity"
        ),
    }
    failures = collect_failures(report)
    if anchor_failures:
        failures.append("primary-source-anchors")
    if before != after:
        failures.append("source-drift")
    report["failures"] = failures
    report["status"] = "pass" if not failures else "fail"
    payload = json.dumps(report, indent=2, sort_keys=True) + "\n"
    OUT.write_text(payload)
    print(payload, end="")
    return int(bool(failures))


if __name__ == "__main__":
    raise SystemExit(main())
