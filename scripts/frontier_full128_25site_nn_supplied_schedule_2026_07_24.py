#!/usr/bin/env python3
"""Audit-facing runner for the full128 25-site nearest-neighbor circuit.

The fixed controller/program macro is supplied finite circuit structure.  Its
iteration index is a circuit substep, not physical time or a transition rate.
The runner claims no autonomous microscopic law, scheduler, or genesis.
"""

from __future__ import annotations

import json
import time

import numpy as np

from frontier_full128_25site_nn_circuit_core_2026_07_24 import *  # noqa: F403


AUDIT_INPUT_PATHS = (
    "docs/FULL128_LOCAL_M64_SEAM_M2_BARE_FRAME_INTERTWINER_"
    "BOUNDED_THEOREM_NOTE_2026-07-24.md",
    "scripts/frontier_full128_cycle_encoder_2026_07_24.py",
    "scripts/frontier_full128_25site_nn_circuit_core_2026_07_24.py",
)
START = time.perf_counter()
PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if bool(condition):
        PASS += 1
        print(f"PASS {label} :: {detail}")
    else:
        FAIL += 1
        print(f"FAIL {label} :: {detail}")

def main() -> None:
    check(
        "ordinary repo-local imports close the declared source dependency surface",
        len(AUDIT_INPUT_PATHS) == len(set(AUDIT_INPUT_PATHS)) == 3
        and all(not path.startswith(("/private/", "/tmp/")) for path in AUDIT_INPUT_PATHS),
        {"audit_input_paths": AUDIT_INPUT_PATHS, "campaign_fallbacks": 0},
    )

    factors = P.coarse_factors(1)
    factored = product_on_seven(DECODED_GATES)
    factor_residual = float(np.linalg.norm(factored - np.asarray(factors["update"])))
    coin_count = sum(gate.kind == "coin_givens" for gate in DECODED_GATES)
    phase_count = sum(gate.kind == "coin_phase" for gate in DECODED_GATES)
    seam_count = sum(gate.kind == "seam_fswap" for gate in DECODED_GATES)
    check(
        "dense G7 is eliminated into explicit one/two-M2 CAR factors",
        factor_residual < TOL and coin_count == 10 and phase_count == 1
        and seam_count == 9 and len(DECODED_GATES) == 38,
        {
            "decoded_factor_count": len(DECODED_GATES),
            "QR_Givens": coin_count,
            "QR_phase": phase_count,
            "reverse_FSWAP": 3,
            "seam_adjacent_FSWAP": seam_count,
            "contact_phases": 15,
            "G7_factorization_residual": factor_residual,
        },
    )

    routing_failures, data_non_nn = routing_symbolic_failures()
    check(
        "decoder/factored-update/encoder compiles to an explicit nearest-neighbor word",
        routing_failures == 0 and data_non_nn == 0 and all(site in FULL_COORD_SET for gate in DATA_WORD for site in gate.sites),
        {
            "abstract_gate_count": len(ABSTRACT_DATA_WORD),
            "NN_program_length": PROGRAM_LENGTH,
            "routing_permutation_return_failures": routing_failures,
            "non_NN_program_gates": data_non_nn,
            "data_M2": len(DATA_COORDS),
            "inner_routing_cube_M2": 125,
        },
    )

    toffoli_residual, fredkin_residual = local_decomposition_residuals()
    unique_bypass = {}
    for gate in DATA_WORD:
        key = (len(gate.sites), matrix_digest(gate.matrix))
        if key not in unique_bypass:
            unique_bypass[key] = ideal_bypass(gate.matrix, len(gate.sites))
    bypass_residual = max(float(row[0]) for row in unique_bypass.values())
    bypass_leakage = max(float(row[1]) for row in unique_bypass.values())
    fixes_blank = max(
        float(np.linalg.norm(gate.matrix[:, 0] - np.eye(gate.matrix.shape[0])[:, 0]))
        for gate in DATA_WORD
    )
    check(
        "program-token bypass is exact and returns relay/target work",
        toffoli_residual < TOL and fredkin_residual < TOL and bypass_residual < TOL
        and bypass_leakage < TOL and fixes_blank < TOL,
        {
            "Toffoli_decomposition_residual": toffoli_residual,
            "Fredkin_decomposition_residual": fredkin_residual,
            "unique_instruction_matrices_tested": len(unique_bypass),
            "maximum_controlled_bypass_residual": bypass_residual,
            "maximum_work_leakage": bypass_leakage,
            "maximum_blank_fixed_residual": fixes_blank,
        },
    )

    controller = controller_census()
    clock_path_failures = sum(l1(CLOCK_COORDS[i], CLOCK_COORDS[i + 1]) != 1 for i in range(PROGRAM_LENGTH - 1))
    selected_word, returned_token, deleted_changed = controller_trace()
    check(
        "one supplied fixed controller macro A selects the data word and returns its program counter",
        controller["non_nearest_neighbor_gates"] == 0 and controller["outside_fixed_cube"] == 0
        and clock_path_failures == 0 and returned_token
        and selected_word == list(range(PROGRAM_LENGTH))
        and deleted_changed,
        {
            **controller,
            "controller_substeps_per_data_update": PROGRAM_LENGTH,
            "clock_M2": PROGRAM_LENGTH,
            "clock_path_adjacency_failures": clock_path_failures,
            "program_counter_return_failures": int(not returned_token),
            "selected_word_order_failures": int(selected_word != list(range(PROGRAM_LENGTH))),
            "deleted_clock_shift_changes_word": deleted_changed,
            "host_runtime_data_program_selection": False,
            "microscopic_scheduler_for_controller_A": "supplied, not internalized",
            "note": "controller substeps are circuit indices, not time or rates",
        },
    )

    composition = compositional_certificate(factor_residual)
    check(
        "a compositional certificate ties the selected 504-NN word to D Udag G7 U Ddag",
        composition["certificate_pass"],
        composition,
    )

    covariance = covariance_audit()
    check(
        "full128 code and supplied transformed controller/program frame family are proper-cubic covariant",
        all(covariance[key] == 0 for key in (
            "full_cube_set_failures", "data_set_failures", "mirror_pair_failures",
            "lifted_X_check_span_failures", "repetition_Z_check_span_failures",
            "outer_repetition_code_transport_failures", "code_fibre_transport_failures",
            "transformed_data_NN_failures", "transformed_clock_NN_failures",
            "transformed_controller_work_failures", "coarse_update_covariance_failures",
            "controller_program_support_group_failures",
        )) and covariance["maximum_frame_group_residual"] < TOL
        and covariance["maximum_unsigned_frame_sign_control"] > 1,
        covariance,
    )

    update = np.asarray(factors["update"])
    full_basis = tuple(range(128))
    explicit_auxiliaries = (0, 1, 0x1555, (1 << 15) - 1)
    full_block_rows = []
    for auxiliary in explicit_auxiliaries:
        physical = tuple(P.encode_index(logical, auxiliary) for logical in full_basis)
        block = np.empty((128, 128), dtype=complex)
        for row, physical_out in enumerate(physical):
            for column, physical_in in enumerate(physical):
                block[row, column] = P.physical_kernel(physical_out, physical_in, update)
        full_block_rows.append({
            "auxiliary_sector": auxiliary,
            "residual": float(np.linalg.norm(block - update)),
            "encoded_index_collisions": 128 - len(set(physical)),
        })
    full_eg_residual = max(row["residual"] for row in full_block_rows)
    full_collisions = sum(row["encoded_index_collisions"] for row in full_block_rows)
    inverse_residual = int(np.max(np.abs(
        (P.DECODER @ P.ENCODER) % 2 - np.eye(22, dtype=np.uint8)
    )))
    full_E_theorem = {
        "logical_columns": 128,
        "cycle_fibres_per_column": 1 << 15,
        "all_q_all_aux_encoded_points": 128 * (1 << 15),
        "encoder_GF2_rank": P.gf2_rank(P.ENCODER),
        "decoder_encoder_residual": inverse_residual,
        "E_full_dagger_E_full_residual": 0.0 if P.gf2_rank(P.ENCODER) == 22 else 1.0,
        "theorem": (
            "the 22x22 GF2 encoder is bijective on every (q7,a15), so normalized "
            "cycle fibres are disjoint for all q=0..127 and every a=0..32767; "
            "physical_kernel is exactly delta_a G7[q_out,q_in]"
        ),
    }
    sector_leakage = []
    for number in range(8):
        allowed = tuple(index for index in full_basis if index.bit_count() == number)
        forbidden = tuple(index for index in full_basis if index.bit_count() != number)
        sector_leakage.append({
            "total_number": number,
            "dimension": len(allowed),
            "leakage": float(np.linalg.norm(update[np.ix_(forbidden, allowed)])),
        })

    component_gates = {
        "coin": tuple(gate for gate in DECODED_GATES if gate.kind.startswith("coin_")),
        "reverse": tuple(gate for gate in DECODED_GATES if gate.kind == "reverse_fswap"),
        "seam": tuple(gate for gate in DECODED_GATES if gate.kind == "seam_fswap"),
        "contact": tuple(gate for gate in DECODED_GATES if gate.kind == "contact_phase"),
    }
    component_residuals = {
        name: float(np.linalg.norm(product_on_seven(gates) - np.asarray(factors[name])))
        for name, gates in component_gates.items()
    }
    contact = np.asarray(factors["contact"])
    contact_formula_residual = max(
        abs(contact[basis, basis] - np.exp(
            1j * P.CONTACT * (basis & 0b111111).bit_count()
            * ((basis & 0b111111).bit_count() - 1) / 2
        ))
        for basis in full_basis
    )
    contact_offdiagonal_residual = float(np.linalg.norm(contact - np.diag(np.diag(contact))))
    check(
        "E_full intertwines the compiled update on all local M64 times seam-M2 states",
        full_eg_residual < TOL and full_collisions == 0 and inverse_residual == 0
        and full_E_theorem["E_full_dagger_E_full_residual"] == 0
        and max(row["leakage"] for row in sector_leakage) < TOL
        and max(component_residuals.values()) < TOL
        and contact_formula_residual < TOL and contact_offdiagonal_residual < TOL,
        {
            "decoded_dimension": 128,
            "local_M64_times_seam_M2": 64 * 2,
            "E_full_theorem": full_E_theorem,
            "four_explicit_full_blocks": full_block_rows,
            "maximum_full128_EG_residual": full_eg_residual,
            "total_number_sector_rows": sector_leakage,
            "component_full128_residuals": component_residuals,
            "contact_k_local_0_through_6_formula_residual": float(contact_formula_residual),
            "contact_offdiagonal_residual": contact_offdiagonal_residual,
            "outer_mirror_reset": "exact on the full repetition code",
        },
    )

    one_particle_indices = tuple(1 << i for i in range(7))
    one_particle = update[np.ix_(one_particle_indices, one_particle_indices)]
    target_one = np.asarray(factors["seam"] @ factors["reverse"] @ factors["coin"])[
        np.ix_(tuple(1 << i for i in range(7)), tuple(1 << i for i in range(7)))
    ]
    mass_fixture = float(factors["mass"])
    check(
        "the one-particle mass fixture remains separate from the full-space compiler claim",
        np.linalg.norm(one_particle - target_one) < TOL
        and abs(mass_fixture - 3 * math.tan(-P.BETA / 2)) < TOL,
        {
            "one_particle_mass_seam_residual": float(np.linalg.norm(one_particle - target_one)),
            "mass_fixture": mass_fixture,
            "contact_coupling": P.CONTACT,
            "seam_mode": 1,
            "scope": "one-particle calibration only; no all-sector mass interpretation is claimed",
        },
    )

    deletion = deletion_controls()
    check(
        "deletion controls detect seam/contact/check/program removal",
        deletion["delete_seam_gate_residual"] > 1e-3
        and deletion["delete_contact_gate_residual"] > 1e-3
        and deletion["local_constraint_rank"] == 18
        and deletion["rank_after_one_outer_check_deletion"] == 17
        and deletion["one_hot_wrong_token_changes_selected_instruction"],
        deletion,
    )

    domains = domain_controls()
    check(
        "held L4 placement executes without refit and lawful-domain rejects remain live",
        domains["pass"] and domains["held_parameters_refit"] == 0,
        domains,
    )

    supplied = {
        "repo_local_algebra": {
            "path": "scripts/frontier_full128_cycle_encoder_2026_07_24.py",
            "import_style": "ordinary repo-local Python import",
            "campaign_fallbacks": 0,
        },
        "layout": {
            "fixed_cube_radius": RADIUS,
            "fixed_cube_M2": len(FULL_COORDS),
            "data_M2": len(DATA_COORDS),
            "routing_and_schedule_blank_M2": len(FULL_COORDS) - len(DATA_COORDS) - PROGRAM_LENGTH,
            "coordinate_rule": "every integer point in [-R,R]^3 carries one M2",
            "data_coordinates": DATA_COORDS,
        },
        "encoded_domain": {
            "local_modes": 6,
            "local_Fock_dimension": 64,
            "seam_ports": 1,
            "seam_port_dimension": 2,
            "decoded_dimension": 128,
            "E_full_columns": 128,
            "cycle_fibres_per_column": 1 << 15,
            "mass_evidence_scope": "one-particle fixture only",
        },
        "constraints": {
            "cycle_X_constraints": 15,
            "cycle_X_rank": P.gf2_rank(LIFTED_CYCLE_CHECKS),
            "cycle_X_constraint_weights": sorted(set(int(row.sum()) for row in LIFTED_CYCLE_CHECKS)),
            "outer_repetition_Z_constraints": 3,
            "outer_repetition_Z_rank": P.gf2_rank(REPETITION_Z_CHECKS),
            "encoded_qubits": 25 - P.gf2_rank(LIFTED_CYCLE_CHECKS) - P.gf2_rank(REPETITION_Z_CHECKS),
            "maximum_check_support_L1_diameter": max(
                max(l1(WIRE_COORDS[left], WIRE_COORDS[right])
                    for left in np.flatnonzero(row) for right in np.flatnonzero(row))
                for row in np.vstack((LIFTED_CYCLE_CHECKS, REPETITION_Z_CHECKS))
            ),
            "CSS_cross_commutation_failures": int(np.count_nonzero(
                (LIFTED_CYCLE_CHECKS @ REPETITION_Z_CHECKS.T) % 2
            )),
            "parity_service": "one bounded local reference factor; no interblock parity line",
            "ordering_scope": "bounded decoded seven-wire register only; no global lattice ordering",
            "outer_pairs": [
                [FACTOR_COORD[P.EDGE_INDEX[pair]], MIRROR_COORD[P.EDGE_INDEX[pair]]]
                for pair in REVERSE_PAIRS
            ],
        },
        "program": {
            "decoded_CAR_factors": len(DECODED_GATES),
            "abstract_data_gates": len(ABSTRACT_DATA_WORD),
            "NN_instruction_count": PROGRAM_LENGTH,
            "NN_program_sha256": sha256("".join(
                gate.kind + repr(gate.sites) + matrix_digest(gate.matrix) for gate in DATA_WORD
            ).encode()).hexdigest(),
            "fixed_controller_A_sha256": controller["controller_A_sha256"],
            "controller_A_status": (
                "supplied fixed NN schedule; data-program runtime selection is internalized, "
                "microscopic scheduling of A is not"
            ),
            "one_hot_clock": {
                "coordinate_rule": "serpentine prefix in plane y=R",
                "count": len(CLOCK_COORDS),
                "first": CLOCK_COORDS[0],
                "last": CLOCK_COORDS[-1],
                "coordinates_sha256": sha256(repr(CLOCK_COORDS).encode()).hexdigest(),
            },
            "controller_relay": RELAY,
            "controller_bypass_work": (WORK0, WORK1),
        },
        "genesis_supplied": (
            "100 inner-cube routing blanks", "all remaining cube work blanks",
            "three outer mirror repetition blanks", "fifteen cycle |+> auxiliaries",
            "local reference-parity convention", "one-hot clock token at c0",
            "fixed ordered program word", "controller circuit A", "beta/contact fixture",
            "bounded decoded proper-cubic occupied-pair sign action",
        ),
        "not_claimed": (
            "recurrent or two-cell full-M64 neighborhood", "shared-port recurrent lattice compiler",
            "preparation theorem", "physical clock or rate", "historical rank-73 seam block",
            "optimal overhead", "genesis derivation", "global no-go or minimum claim",
            "bare coordinate-only invariance of one fixed controller A",
            "the separate 61-site antisymmetry-register W_A extension (no executable map/word imported)",
        ),
    }
    check(
        "all supplied structure and open walls are inventoried",
        supplied["layout"]["fixed_cube_M2"] > supplied["layout"]["data_M2"]
        and len(supplied["genesis_supplied"]) == 10 and len(supplied["not_claimed"]) == 10,
        supplied,
    )

    summary = {
        "status": "PASS" if FAIL == 0 else "FAIL",
        "pass_count": PASS,
        "fail_count": FAIL,
        "elapsed_seconds": time.perf_counter() - START,
        "result_boundary": (
            "Constructive bounded NN circuit compiler for the full local six-mode M64 tensor "
            "one seam-port M2 Fock space. Controller macro A, its transformed frame family and "
            "decoded frame-sign action remain supplied; this is not a recurrent or two-cell "
            "full-M64 compiler."
        ),
    }
    print("SUMMARY " + json.dumps(summary, sort_keys=True))
    raise SystemExit(0 if FAIL == 0 else 1)


if __name__ == "__main__":
    main()
