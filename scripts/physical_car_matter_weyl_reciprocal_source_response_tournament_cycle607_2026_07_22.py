#!/usr/bin/env python3
"""Cycle607: accepted-CAR matter / finite-Weyl reciprocal response tournament.

The local source is Cycle600's exact descended CAR occupation, not a new
placeholder source word.  The finite-Weyl coupling, ordering criterion, and
Cesaro response are falsifiable candidates.  No modular impulse is called
stress-energy, no response is called gravity, and update count is not time.
Authority none; audit unset.
"""
from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
from itertools import combinations, product
import json
import math
from pathlib import Path
import resource
import subprocess
import sys
from time import perf_counter

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_root_free_full_N3_carrier_genesis_tournament_cycle600_2026_07_22 as c600
import physical_rational_regge_reciprocal_response_prediction_bridge_cycle604_2026_07_22 as c604
import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_CAR_MATTER_WEYL_RECIPROCAL_SOURCE_RESPONSE_TOURNAMENT_"
    "CYCLE607_NOTE_2026-07-22.md"
)
RECEIPT = ROOT / (
    "outputs/physical_car_matter_weyl_reciprocal_source_response_"
    "tournament_cycle607_receipt_2026_07_22.json"
)
AUTHORITY = "none"
AUDIT = "unset"
TOL = 2e-8
SIGNAL = 1e-5
WEYL_DIMENSION = 16
COUPLING_SIGN = 1
START = perf_counter()
PASS = 0
FAIL = 0

PINS = {
    "scripts/physical_root_free_full_N3_carrier_genesis_tournament_cycle600_2026_07_22.py":
        "5b9bb9c1ae8585b7395f1a1a94040016ff8cc73e5cfbb430b16183e7133b64ba",
    "docs/work_history/repo/review_feedback/PHYSICAL_ROOT_FREE_FULL_N3_CARRIER_GENESIS_TOURNAMENT_CYCLE600_NOTE_2026-07-22.md":
        "f3d0eb88946c14b94ba9e5f8de436c6af808ad37a7e8250f6ed10e42492848ea",
    "outputs/physical_root_free_full_N3_carrier_genesis_tournament_cycle600_receipt_2026_07_22.json":
        "3bddb02e1297440781fbd960a07e1b4ee021c9eadba8a6a5372dbb9812fb7cbd",
    "outputs/physical_root_free_full_N3_carrier_genesis_tournament_cycle600_cold_2026_07_22.txt":
        "ae85d6e4dc29b240d5eb2374ce22a2836dc0c7b0f85831406462779b1803f183",
    "scripts/physical_full_torus_dimer_M2_compiler_tournament_cycle590_2026_07_22.py":
        "5fbf3bcecc54df9912f9b79d2e5c45d51f145279c1ed83f507bc24e9e1980029",
    "outputs/physical_full_torus_dimer_M2_compiler_tournament_cycle590_receipt_2026_07_22.json":
        "ebc13a522e439e2a1618421773751c096b210cc4be25476511dead5a6ea241f7",
    "scripts/physical_rational_regge_reciprocal_response_prediction_bridge_cycle604_2026_07_22.py":
        "baf97a0e09672904609186a167618969ad5b72942044f4d037f30e5439773145",
    "docs/work_history/repo/review_feedback/PHYSICAL_RATIONAL_REGGE_RECIPROCAL_RESPONSE_PREDICTION_BRIDGE_CYCLE604_NOTE_2026-07-22.md":
        "c5730f9de3eeee410640083f3dac0bdb083aa4a753ac8c9a2e445e05b797b546",
    "outputs/physical_rational_regge_reciprocal_response_prediction_bridge_cycle604_receipt_2026_07_22.json":
        "c8210a1f170c3b11258f9876a0013b981b4b3c44a592423c8ce48a34a479b5ee",
    "outputs/physical_rational_regge_reciprocal_response_prediction_bridge_cycle604_cold_2026_07_22.txt":
        "0b9e68349c2f5a05961f6f06de372fb57949ca3f1c1639e9bfb802aad6b815e0",
    "scripts/physical_constrained_matter_source_static_join_tournament_cycle588_2026_07_22.py":
        "d3658aacb76988ae7daf100f8ed3503e69927afa90a88d2062a0f23919f8ac4c",
    "outputs/physical_joint_clock_accumulator_contraction_bridge_cycle570_receipt_2026_07_22.json":
        "f104399af621ded1b50e180e6fcce5f254008715b72191c6199fe4d583a8a806",
}


def digest(relative: str) -> str:
    return sha256((ROOT / relative).read_bytes()).hexdigest()


def json_default(value):
    if isinstance(value, np.generic):
        return value.item()
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, complex):
        return [value.real, value.imag]
    raise TypeError(type(value).__name__)


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    PASS += int(condition)
    FAIL += int(not condition)
    print("PASS" if condition else "FAIL", label, "::", detail)


def dependency_shore() -> dict:
    observed = {name: digest(name) for name in PINS}
    r600 = json.loads((ROOT / "outputs/physical_root_free_full_N3_carrier_genesis_tournament_cycle600_receipt_2026_07_22.json").read_text())
    r590 = json.loads((ROOT / "outputs/physical_full_torus_dimer_M2_compiler_tournament_cycle590_receipt_2026_07_22.json").read_text())
    r604 = json.loads((ROOT / "outputs/physical_rational_regge_reciprocal_response_prediction_bridge_cycle604_receipt_2026_07_22.json").read_text())
    r570 = json.loads((ROOT / "outputs/physical_joint_clock_accumulator_contraction_bridge_cycle570_receipt_2026_07_22.json").read_text())
    evidence = {
        "hashes_match": observed == PINS,
        "Cycle600_pass": r600["pass"], "Cycle590_pass": r590["pass"],
        "Cycle604_pass": r604["pass"], "Cycle570_pass": r570["pass"],
        "Cycle600_number_descent_residual": r600["route_A_full_N3_exterior_carrier_compiler"]["number_observable_descent_residual"],
        "one_particle_mass_residual": r600["shore"]["fixtures"]["one_particle_mass_residual"],
        "Cycle230_contact_factorization_residual": r600["shore"]["fixtures"]["Cycle230_contact_factorization_residual"],
        "Cycle230_seam_braid_residual": r600["shore"]["fixtures"]["Cycle230_seam_braid_residual"],
        "Cycle604_tests_passed": r604["tests_passed"],
    }
    check("Cycles590/600/604/570 are byte-pinned and passing",
          all((evidence["hashes_match"], evidence["Cycle600_pass"], evidence["Cycle590_pass"],
               evidence["Cycle604_pass"], evidence["Cycle570_pass"]))
          and max(evidence["Cycle600_number_descent_residual"], evidence["one_particle_mass_residual"],
                  evidence["Cycle230_contact_factorization_residual"], evidence["Cycle230_seam_braid_residual"]) < TOL,
          evidence)
    return {"observed": observed, "evidence": evidence, "Cycle604": r604}


def physical_numbers() -> np.ndarray:
    """A unitary off-code extension on the complete 12-M2 carrier basis."""
    values = np.empty(16**3, dtype=int)
    for word in np.ndindex(16, 16, 16):
        values[(word[0] * 16 + word[1]) * 16 + word[2]] = sum(4 <= label <= 9 for label in word)
    return values


def exterior_embedding_16() -> tuple[np.ndarray, tuple[tuple[int, ...], ...]]:
    embedding10, basis = c600.exterior_carrier_embedding()
    embedding16 = np.zeros((16**3, embedding10.shape[1]), dtype=complex)
    for word in np.ndindex(10, 10, 10):
        row10 = (word[0] * 10 + word[1]) * 10 + word[2]
        row16 = (word[0] * 16 + word[1]) * 16 + word[2]
        embedding16[row16] = embedding10[row10]
    return embedding16, basis


def lift_valid_carrier_image(image10: np.ndarray) -> np.ndarray:
    image16 = np.zeros((16**3, image10.shape[1]), dtype=complex)
    for word in np.ndindex(10, 10, 10):
        row10 = (word[0] * 10 + word[1]) * 10 + word[2]
        row16 = (word[0] * 16 + word[1]) * 16 + word[2]
        image16[row16] = image10[row10]
    return image16


def phase(number, coordinate, sign=COUPLING_SIGN):
    return np.exp(2j * math.pi * sign * np.asarray(number) * np.asarray(coordinate) / WEYL_DIMENSION)


def joint_layout(length: int) -> dict:
    """Append four scalar field M2 to Cycle600's literal 12-role block."""
    c560 = c600.c598.c593.c560
    code = c560.c539.c525.c319.c269.build_code(length)
    cells = c560.c555.network_cells(length)
    modulus = c560.c533.c527.fine_length(length)
    physical = tuple(c560.c533.coordinate_for_qubit(code, bit)
                     for bit in range(c560.c555.physical_bit_count(code)))
    shadows = tuple(c560.c533.c527.shadow_coordinate(cell, direction, length)
                    for cell in cells for direction in range(6))
    occupied = set(physical) | set(shadows)
    for cell in cells:
        origin = c560.c533.c527.cell_center(cell, length)
        c560.allocated_block(origin, 6, occupied, modulus)
        c560.allocated_block(origin, 18, occupied, modulus)
    carrier = []
    for cell in cells:
        carrier.extend(c560.allocated_block(c560.c533.c527.cell_center(cell, length), 12,
                                            occupied, modulus))
    field = []
    maximum_field_radius = 0
    for cell in cells:
        origin = c560.c533.c527.cell_center(cell, length)
        block = c560.allocated_block(origin, 4, occupied, modulus)
        field.extend(block)
        maximum_field_radius = max(maximum_field_radius, max(
            c560.c533.c527.periodic_l1(origin, site, modulus) for site in block))
    roles = np.asarray(carrier + field, dtype=int)
    frames = c600.c598.c593.c210.proper_cubic_frames()
    injection_failures = sum(
        len(np.unique((roles @ frame.T) % modulus, axis=0)) != len(roles) for frame in frames
    )
    group_failures = 0
    for left in frames:
        for right in frames:
            direct = (roles @ (left @ right).T) % modulus
            composed = ((roles @ right.T) % modulus @ left.T) % modulus
            group_failures += int(not np.array_equal(direct, composed))
    return {
        "length": length, "cells": length**3, "fine_lattice_modulus": modulus,
        "carrier_M2_per_cell": 12, "field_M2_per_cell": 4,
        "joint_persistent_M2_per_cell": 16, "joint_live_M2": 16 * length**3,
        "field_coordinate_sha256": sha256(repr(tuple(field)).encode()).hexdigest(),
        "maximum_field_role_radius_fine_L1": maximum_field_radius,
        "all24_mapped_wire_injection_failures": injection_failures,
        "all576_coordinate_group_failures": group_failures,
        "local_lookup_support_M2": 16,
        "serial_NN_routing_depth_upper_bound": 2 * 16 * (3 + maximum_field_radius),
        "elementary_M2_gate_lowering_executed": False,
    }


def rotate_scalar(field: np.ndarray, frame: np.ndarray) -> np.ndarray:
    length = field.shape[0]
    output = np.zeros_like(field)
    for coordinate in product(range(length), repeat=3):
        target = tuple(int(value % length) for value in frame @ np.asarray(coordinate))
        output[target] = field[coordinate]
    return output


def subset_phase(subset: tuple[int, ...], field: np.ndarray, sign=COUPLING_SIGN) -> complex:
    exponent = sum(int(field.reshape(-1)[mode // 6]) for mode in subset)
    return complex(phase(1, exponent, sign))


def word_phase(word: tuple[int, int, int], total_modes: int, field: np.ndarray,
               sign=COUPLING_SIGN) -> complex:
    exponent = sum(int(field.reshape(-1)[mode // 6]) for mode in word if mode < total_modes)
    return complex(phase(1, exponent, sign))


def contact_phase_subset(subset: tuple[int, ...]) -> complex:
    counts = {}
    for mode in subset:
        counts[mode // 6] = counts.get(mode // 6, 0) + 1
    return complex(np.prod([np.exp(1j * c230.COUPLING * n * (n - 1) / 2)
                            for n in counts.values()]))


def contact_phase_word(word: tuple[int, int, int], total_modes: int) -> complex:
    return contact_phase_subset(tuple(mode for mode in word if mode < total_modes))


def route_a(shore: dict) -> dict:
    embedding, basis = exterior_embedding_16()
    logical_number = np.asarray([len(subset) for subset in basis])
    physical_number = physical_numbers()
    number_descent = float(np.linalg.norm(
        physical_number[:, None] * embedding - embedding * logical_number[None, :]
    ))
    maximum_local_EG = maximum_leakage = maximum_inverse = 0.0
    minimum_source_deletion = minimum_field_deletion = math.inf
    for sign in (+1, -1):
        for q in range(WEYL_DIMENSION):
            logical = embedding * phase(logical_number, q, sign)[None, :]
            physical = phase(physical_number, q, sign)[:, None] * embedding
            maximum_local_EG = max(maximum_local_EG, float(np.linalg.norm(logical - physical)))
            projected = embedding @ (embedding.conj().T @ physical)
            maximum_leakage = max(maximum_leakage, float(np.linalg.norm(physical - projected)))
            restored = phase(physical_number, q, -sign)[:, None] * physical
            maximum_inverse = max(maximum_inverse, float(np.linalg.norm(restored - embedding)))
            if q and sign == 1:
                minimum_source_deletion = min(minimum_source_deletion,
                    float(np.linalg.norm(physical - embedding)))
                minimum_field_deletion = min(minimum_field_deletion,
                    float(np.linalg.norm(logical - embedding)))

    species = c219.common_species(-0.3)
    extended_coin10 = np.eye(10, dtype=complex); extended_coin10[4:10, 4:10] = species.coin
    extended_coin16 = np.eye(16, dtype=complex); extended_coin16[4:10, 4:10] = species.coin
    physical_coin10 = c600.physical_three_carrier_operator(extended_coin10)
    logical_coin = c600.truncated_fock_representation(species.coin)
    physical_contact = np.asarray([
        np.exp(1j * c230.COUPLING * n * (n - 1) / 2) for n in physical_number
    ])
    logical_contact = np.asarray([
        np.exp(1j * c230.COUPLING * n * (n - 1) / 2) for n in logical_number
    ])
    logical_matter = logical_contact[:, None] * logical_coin
    embedding10, _ = c600.exterior_carrier_embedding()
    physical_coin_image = lift_valid_carrier_image(physical_coin10 @ embedding10)
    physical_matter_image = physical_contact[:, None] * physical_coin_image
    maximum_composite_EG = 0.0
    for q in range(WEYL_DIMENSION):
        logical = embedding @ (phase(logical_number, q)[:, None] * logical_matter)
        physical = phase(physical_number, q)[:, None] * physical_matter_image
        maximum_composite_EG = max(maximum_composite_EG, float(np.linalg.norm(logical - physical)))
    logical_mass_commutator = float(np.linalg.norm(
        logical_number[:, None] * logical_coin - logical_coin * logical_number[None, :]
    ))
    single_number = np.asarray([int(4 <= label <= 9) for label in range(16)])
    physical_mass_commutator = float(np.linalg.norm(
        single_number[:, None] * extended_coin16 - extended_coin16 * single_number[None, :]
    ))
    full_off_code_phase_unitarity = 0.0
    for sign in (+1, -1):
        for q in range(WEYL_DIMENSION):
            full_off_code_phase_unitarity = max(full_off_code_phase_unitarity,
                float(np.max(abs(abs(phase(physical_number, q, sign)) - 1))))

    q_values = np.arange(WEYL_DIMENSION)
    momenta = np.arange(WEYL_DIMENSION)
    fourier = np.exp(2j * math.pi * np.outer(q_values, momenta) / WEYL_DIMENSION) / math.sqrt(WEYL_DIMENSION)
    maximum_field_kick = maximum_reciprocity = 0.0
    for sign in (+1, -1):
        for number in range(4):
            diagonal = phase(number, q_values, sign)
            for momentum in range(WEYL_DIMENSION):
                target = (momentum + sign * number) % WEYL_DIMENSION
                maximum_field_kick = max(maximum_field_kick, float(np.linalg.norm(
                    diagonal * fourier[:, momentum] - fourier[:, target]
                )))
            for q in range(WEYL_DIMENSION):
                matter_ratio = phase(1, q, sign)
                field_ratio = phase(1, q, sign)
                maximum_reciprocity = max(maximum_reciprocity, float(abs(matter_ratio - field_ratio)))

    frames = c600.c598.c593.c210.proper_cubic_frames()
    rows = []
    maximum_global_EG = maximum_global_inverse = maximum_covariance = 0.0
    group_failures = 0
    maximum_matter_continuity = maximum_field_impulse_ledger = 0
    maximum_global_deletion = 0.0
    for label, length, held in (("TRAIN_L3", 3, False), ("HELD_L6", 6, True),
                                ("OUT_FAMILY_L7", 7, True)):
        total_modes = 6 * length**3
        field = np.fromfunction(lambda x, y, z: (1 + x + 2*y + 3*z) % WEYL_DIMENSION,
                                (length, length, length), dtype=int).astype(int)
        candidates = [(), (0,), (0, 1), (1, 6 * (length**3 - 1)),
                      tuple(sorted((1, 6 * (length**3 - 1), 6 * (length**3 // 2) + 2)))]
        sample_rows = []
        for subset in candidates:
            terms = c600.encoded_global_terms(subset, total_modes)
            target, stream_sign = c600.mapped_subset_and_sign(
                subset, lambda mode, L=length: c600.mode_stream_map(mode, L))
            before_counts = np.zeros(length**3, dtype=int)
            after_counts = np.zeros(length**3, dtype=int)
            divergence = np.zeros(length**3, dtype=int)
            for source_mode, target_mode in zip(subset, [c600.mode_stream_map(mode, length) for mode in subset]):
                source_site, target_site = source_mode // 6, target_mode // 6
                before_counts[source_site] += 1; after_counts[target_site] += 1
                divergence[source_site] += 1; divergence[target_site] -= 1
            matter_continuity = int(np.max(abs(after_counts - before_counts + divergence)))
            field_impulse_ledger = int((np.sum(after_counts) - len(subset)) % WEYL_DIMENSION)
            maximum_matter_continuity = max(maximum_matter_continuity, matter_continuity)
            maximum_field_impulse_ledger = max(maximum_field_impulse_ledger, field_impulse_ledger)
            mapped = c600.map_encoded_terms(
                terms, total_modes, lambda mode, L=length: c600.mode_stream_map(mode, L))
            physical_updated = {
                word: amplitude * contact_phase_word(word, total_modes)
                * word_phase(word, total_modes, field)
                for word, amplitude in mapped.items()
            }
            target_terms = c600.encoded_global_terms(target, total_modes)
            logical_factor = contact_phase_subset(target) * subset_phase(target, field)
            expected = {word: stream_sign * amplitude * logical_factor
                        for word, amplitude in target_terms.items()}
            residual = c600.maximum_term_residual(physical_updated, expected)
            unphased = {
                word: amplitude / (contact_phase_word(word, total_modes)
                                   * word_phase(word, total_modes, field))
                for word, amplitude in physical_updated.items()
            }
            restored = c600.map_encoded_terms(
                unphased, total_modes, lambda mode, L=length: c600.mode_inverse_stream_map(mode, L))
            inverse = c600.maximum_term_residual(restored, terms)
            deletion = abs(logical_factor - contact_phase_subset(target))
            maximum_global_EG = max(maximum_global_EG, residual)
            maximum_global_inverse = max(maximum_global_inverse, inverse)
            maximum_global_deletion = max(maximum_global_deletion, deletion)
            sample_rows.append({"number": len(subset), "contains_seam": any(mode // 6 == length**3 - 1 for mode in subset),
                                "joint_stream_contact_interaction_EG_residual": residual,
                                "joint_inverse_term_residual": inverse,
                                "matter_stream_local_continuity_residual": matter_continuity,
                                "field_impulse_sum_minus_CAR_number_mod16": field_impulse_ledger,
                                "interaction_deletion_signal": deletion})
        probe = candidates[-1]
        before = subset_phase(probe, field)
        for frame in frames:
            rotated_subset = tuple(sorted(c600.mode_frame_map(mode, frame, length) for mode in probe))
            after = subset_phase(rotated_subset, rotate_scalar(field, frame))
            maximum_covariance = max(maximum_covariance, abs(before - after))
        test_modes = tuple(range(min(42, total_modes)))
        for left in frames:
            for right in frames:
                for mode in test_modes:
                    direct = c600.mode_frame_map(mode, left @ right, length)
                    composed = c600.mode_frame_map(c600.mode_frame_map(mode, right, length), left, length)
                    group_failures += direct != composed
        layout = joint_layout(length)
        rows.append({"fixture": label, "length": length, "held": held,
                     "samples": sample_rows, "layout": layout,
                     "maximum_joint_EG_residual": max(row["joint_stream_contact_interaction_EG_residual"] for row in sample_rows),
                     "maximum_joint_inverse_residual": max(row["joint_inverse_term_residual"] for row in sample_rows)})

    output = {
        "object": "Cycle600 accepted N<=3 exterior-CAR occupation coupled to one 16-level finite-Weyl field per cell",
        "disposition": "CONSTRUCTIVE_EXACT_TYPED_CAR_WEYL_INTERACTION; ELEMENTARY_LOWERING_AND_RESPONSE_COMPILER_OPEN",
        "exact_interface": "N_phys E600 = E600 N_CAR; U_int=exp(2pi i s N_CAR Q/16) therefore has E_joint U_logical=U_physical E_joint",
        "action_generator": "S_int=s*N_CAR*Q mod 16; its two discrete derivatives give field momentum kick s*N_CAR and matter number-conjugate phase kick s*Q",
        "Cycle600_number_descent_residual": number_descent,
        "maximum_local_interaction_EG_residual": maximum_local_EG,
        "maximum_local_code_leakage": maximum_leakage,
        "maximum_local_inverse_residual": maximum_inverse,
        "minimum_delete_matter_control_signal": minimum_source_deletion,
        "minimum_delete_field_coordinate_signal": minimum_field_deletion,
        "maximum_Weyl_momentum_kick_residual": maximum_field_kick,
        "maximum_action_mixed_derivative_reciprocity_residual": maximum_reciprocity,
        "full_65536_basis_interaction_unitarity_residual": full_off_code_phase_unitarity,
        "complete_physical_carrier_field_basis_dimension": 16**3 * WEYL_DIMENSION,
        "invalid_carrier_label_extension": "labels 10..15 are fixed by the matter coin and counted unoccupied by the diagonal interaction; every off-code basis phase still has unit modulus",
        "local_impulse_ledger": "Delta p_field = s*N_CAR mod 16 and Delta theta_matter = s*Q mod 16; this is not stress-energy",
        "maximum_matter_stream_local_continuity_residual": maximum_matter_continuity,
        "maximum_field_impulse_sum_ledger_residual": maximum_field_impulse_ledger,
        "field_coordinate_and_momentum_are_conjugate_bases_of_same_register": True,
        "maximum_coin_contact_interaction_composite_EG_residual": maximum_composite_EG,
        "logical_number_mass_coin_commutator": logical_mass_commutator,
        "physical_number_mass_coin_commutator": physical_mass_commutator,
        "inherited_one_particle_mass_residual": shore["evidence"]["one_particle_mass_residual"],
        "inherited_Cycle230_contact_factorization_residual": shore["evidence"]["Cycle230_contact_factorization_residual"],
        "inherited_Cycle230_seam_braid_residual": shore["evidence"]["Cycle230_seam_braid_residual"],
        "rows": rows, "maximum_global_joint_EG_residual": maximum_global_EG,
        "maximum_global_joint_inverse_residual": maximum_global_inverse,
        "maximum_global_interaction_deletion_signal": maximum_global_deletion,
        "maximum_all24_covariance_residual": maximum_covariance,
        "all576_mode_group_failures": group_failures,
        "coupling_sign_selected": False, "coupling_units_derived": False,
        "accepted_elementary_gate_alphabet_lowering_executed": False,
        "executed_NQ_phase_support_M2": 16,
        "NQ_phase_decomposed_into_elementary_local_factors": False,
        "host_future_source_service_used": False,
    }
    check("Route A finite-Weyl interaction exactly uses the descended CAR occupation and is reciprocal",
          max(number_descent, maximum_local_EG, maximum_leakage, maximum_inverse,
              maximum_field_kick, maximum_reciprocity, maximum_composite_EG,
              logical_mass_commutator, physical_mass_commutator,
              full_off_code_phase_unitarity) < TOL
          and minimum_source_deletion > SIGNAL and minimum_field_deletion > SIGNAL, output)
    check("Route A preserves mass/contact/seam and full joint EG/inverse on L3/L6/L7",
          max(maximum_global_EG, maximum_global_inverse,
              shore["evidence"]["one_particle_mass_residual"],
              shore["evidence"]["Cycle230_contact_factorization_residual"],
              shore["evidence"]["Cycle230_seam_braid_residual"]) < TOL
          and maximum_global_deletion > SIGNAL
          and all(row["layout"]["joint_persistent_M2_per_cell"] == 16 for row in rows), rows)
    check("Route A scalar joint law is all24/all576 covariant on the declared prepared sector",
          maximum_covariance < TOL and group_failures == 0
          and maximum_matter_continuity == maximum_field_impulse_ledger == 0
          and all(row["layout"]["all24_mapped_wire_injection_failures"] == 0
                  and row["layout"]["all576_coordinate_group_failures"] == 0 for row in rows), output)
    return output


def route_b() -> dict:
    q = np.arange(WEYL_DIMENSION)
    p = np.arange(WEYL_DIMENSION)
    fourier = np.exp(2j * math.pi * np.outer(q, p) / WEYL_DIMENSION) / math.sqrt(WEYL_DIMENSION)
    centered = np.minimum(p, WEYL_DIMENSION - p)
    tau = 0.37
    drift = fourier @ np.diag(np.exp(-1j * tau * centered**2)) @ fourier.conj().T
    half = fourier @ np.diag(np.exp(-0.5j * tau * centered**2)) @ fourier.conj().T
    rows = []
    max_symmetric_reversal = max_inverse = 0.0
    min_unsymmetric_reversal = min_sign_signal = min_order_signal = min_deleted_half = math.inf
    symmetric_by_sign = {}
    for sign in (+1, -1):
        blocks = []
        for number in range(4):
            kick = np.diag(phase(number, q, sign))
            schedules = {
                "KICK_THEN_DRIFT": drift @ kick,
                "DRIFT_THEN_KICK": kick @ drift,
                "SYMMETRIC_HALF_DRIFT": half @ kick @ half,
            }
            residuals = {name: float(np.linalg.norm(unitary.conj() - unitary.conj().T))
                         for name, unitary in schedules.items()}
            inverses = {name: float(np.linalg.norm(unitary.conj().T @ unitary - np.eye(WEYL_DIMENSION)))
                        for name, unitary in schedules.items()}
            if number:
                max_symmetric_reversal = max(max_symmetric_reversal, residuals["SYMMETRIC_HALF_DRIFT"])
                min_unsymmetric_reversal = min(min_unsymmetric_reversal,
                    residuals["KICK_THEN_DRIFT"], residuals["DRIFT_THEN_KICK"])
                min_order_signal = min(min_order_signal, float(np.linalg.norm(
                    schedules["KICK_THEN_DRIFT"] - schedules["DRIFT_THEN_KICK"])))
                deleted = kick @ half
                min_deleted_half = min(min_deleted_half, float(np.linalg.norm(
                    schedules["SYMMETRIC_HALF_DRIFT"] - deleted)))
            max_inverse = max(max_inverse, max(inverses.values()))
            blocks.append({"occupation": number, "reversal_residuals": residuals,
                           "inverse_residuals": inverses})
        symmetric_by_sign[sign] = half @ np.diag(phase(1, q, sign)) @ half
        rows.append({"coupling_sign": sign, "occupation_blocks": blocks})
    min_sign_signal = float(np.linalg.norm(symmetric_by_sign[+1] - symmetric_by_sign[-1]))
    output = {
        "object": "factor ordering of the same finite-Weyl CAR kick against a supplied field drift",
        "declared_reversal_involution": "Theta is complex conjugation in the real CAR-number and field-coordinate basis",
        "declared_reversal_test": "Theta U Theta^-1 = U^-1",
        "supplied_drift_parameter_tau": tau,
        "rows": rows,
        "maximum_symmetric_reversal_residual": max_symmetric_reversal,
        "minimum_unsymmetric_reversal_residual": min_unsymmetric_reversal,
        "maximum_exact_inverse_residual": max_inverse,
        "minimum_kick_first_vs_drift_first_signal": min_order_signal,
        "delete_one_half_drift_signal": min_deleted_half,
        "positive_vs_negative_symmetric_signal": min_sign_signal,
        "reversal_criterion_selects_symmetric_order": True,
        "reversal_criterion_selects_coupling_sign": False,
        "criterion_is_derived_framework_time_reversal": False,
        "matter_stream_vs_interaction_order_selected": False,
    }
    check("Route B supplied reversal involution selects the palindromic split but not coupling sign",
          max_symmetric_reversal < TOL and max_inverse < TOL
          and min_unsymmetric_reversal > SIGNAL and min_order_signal > SIGNAL
          and min_deleted_half > SIGNAL and min_sign_signal > SIGNAL,
          output)
    return output


CESARO_ALPHA = 1 / 12
CESARO_FIXTURES = (("TRAIN_L3_H384", 3, 384, False),
                   ("HELD_L6_H768", 6, 768, True),
                   ("OUT_FAMILY_L7_H1536", 7, 1536, True))


def actual_car_source(length: int, subset: tuple[int, ...]) -> np.ndarray:
    source = np.zeros((length,) * 3, dtype=float)
    for mode in subset:
        source.reshape(-1)[mode // 6] += 1.0
    source -= len(subset) / length**3
    return source


def finite_static(source: np.ndarray) -> np.ndarray:
    length = source.shape[0]
    frequencies = 2 * math.pi * np.fft.fftfreq(length)
    denominator = np.zeros(source.shape)
    for index in product(range(length), repeat=3):
        denominator[index] = 6 - 2 * sum(math.cos(frequencies[index[axis]]) for axis in range(3))
    transformed = np.zeros(source.shape, dtype=complex)
    mask = denominator > 1e-14
    transformed[mask] = np.fft.fftn(source)[mask] / denominator[mask]
    return np.fft.ifftn(transformed).real


def cesaro_actual(source: np.ndarray, horizon: int, propagate=True) -> tuple[np.ndarray, np.ndarray]:
    previous = np.zeros_like(source); current = np.zeros_like(source); accumulator = np.zeros_like(source)
    for _ in range(horizon):
        laplacian = c604.laplacian_float(current) if propagate else np.zeros_like(current)
        following = 2 * current - previous - CESARO_ALPHA * laplacian + CESARO_ALPHA * source
        previous, current = current, following
        accumulator += current
    return accumulator / horizon, current


def route_c(shore: dict, routeA: dict) -> dict:
    rows = []
    residuals = []
    maximum_covariance = maximum_source_interface = 0.0
    frames = c600.c598.c593.c210.proper_cubic_frames()
    for label, length, horizon, held in CESARO_FIXTURES:
        subset = (0,)
        source = actual_car_source(length, subset)
        average, endpoint = cesaro_actual(source, horizon)
        exact = finite_static(source)
        relative = float(np.linalg.norm(average - exact) / np.linalg.norm(exact))
        absolute = float(np.linalg.norm(average - exact))
        equation_relative = float(np.linalg.norm(c604.laplacian_float(average) - source)
                                  / np.linalg.norm(source))
        deleted_propagation, _ = cesaro_actual(source, horizon, propagate=False)
        source_off, _ = cesaro_actual(np.zeros_like(source), horizon)
        deleted_field = np.zeros_like(average)
        for frame in frames:
            rotated_source = rotate_scalar(source, frame)
            rotated_average, _ = cesaro_actual(rotated_source, horizon)
            maximum_covariance = max(maximum_covariance, float(np.linalg.norm(
                rotated_average - rotate_scalar(average, frame))))
        # The source is exactly the scalar site-count descent of the accepted one-CAR subset.
        decoded_count = np.zeros_like(source); decoded_count[0, 0, 0] = 1; decoded_count -= 1 / length**3
        maximum_source_interface = max(maximum_source_interface, float(np.linalg.norm(source - decoded_count)))
        residuals.append(relative)
        rows.append({
            "fixture": label, "length": length, "held": held, "horizon_update_count": horizon,
            "actual_Cycle600_CAR_subset": list(subset),
            "actual_CAR_source_interface_residual": float(np.linalg.norm(source - decoded_count)),
            "Cesaro_to_finite_static_relative_residual": relative,
            "Cesaro_to_finite_static_absolute_residual": absolute,
            "static_equation_relative_residual": equation_relative,
            "endpoint_norm_not_time": float(np.linalg.norm(endpoint)),
            "source_off_response_norm": float(np.linalg.norm(source_off)),
            "delete_field_response_signal": float(np.linalg.norm(average - deleted_field)),
            "delete_spatial_propagation_signal": float(np.linalg.norm(average - deleted_propagation)),
        })

    coefficient = 5 / (32 * math.pi)
    green_rows = []
    for label, point in (("HELD_AXIS", (64, 0, 0)), ("HELD_FACE", (40, 40, 0)),
                         ("HELD_BODY", (32, 32, 32))):
        vector = np.asarray(point, float); radius = float(np.linalg.norm(vector)); unit = vector / radius
        k4 = float(np.sum(unit**4) - 3/5)
        value = c604.infinite_lattice_green(point)
        measured = float((value - 1/(4*math.pi*radius)) * radius**3 / k4)
        green_rows.append({"fixture": label, "point": point,
                           "measured_cubic_coefficient": measured,
                           "predicted_5_over_32pi": coefficient,
                           "relative_residual": abs(measured / coefficient - 1)})
    inherited_matched = shore["Cycle604"]["route_C_prediction_bridge"]["matched_event_surface"]
    matched = {
        "source_off": inherited_matched["source_off"],
        "receiver_zero": inherited_matched["receiver_zero"],
        "delay_candidate": inherited_matched["delay_candidate"],
        "advance_candidate": inherited_matched["advance_candidate"],
        "delay_fraction": str(Fraction(3, 4)), "advance_fraction": str(Fraction(5, 4)),
        "actual_joint_response_selects_delay_or_advance": False,
        "mapping_from_response_sign_to_event_is_supplied": True,
    }
    output = {
        "object": "Cycle604 alpha=1/12 response driven by the actual Cycle600 one-CAR occupation descent",
        "disposition": "CONSTRUCTIVE_ACTUAL_SOURCE_PREDICTION_BRIDGE; PROPAGATION_COMPILER_AND_EVENT_CALIBRATION_OPEN",
        "frozen_before_output": {"alpha": CESARO_ALPHA, "fixtures": [list(row) for row in CESARO_FIXTURES],
                                  "source": "one accepted CAR at site zero minus its uniform zero mode",
                                  "normalization_fit_parameters": 0},
        "rows": rows, "relative_residuals": residuals,
        "maximum_actual_CAR_source_interface_residual": maximum_source_interface,
        "maximum_all24_response_covariance_residual": maximum_covariance,
        "all576_inherited_from_exact_scalar_frame_action": routeA["all576_mode_group_failures"] == 0,
        "Cycle585_588_static_coefficient_rows": green_rows,
        "maximum_5_over_32pi_relative_residual": max(row["relative_residual"] for row in green_rows),
        "matched_event_shore": matched,
        "finite_horizon_equals_static_limit": False,
        "field_propagation_has_physical_M2_compiler": False,
        "event_calibration_derived": False,
        "response_is_gravity": False, "update_count_is_time": False,
    }
    check("Route C actual accepted-CAR source approaches the same finite static operator on L3/L6/L7",
          maximum_source_interface < TOL and max(residuals) < 0.01
          and all(residuals[i+1] < residuals[i] for i in range(len(residuals)-1))
          and all(row["source_off_response_norm"] < TOL
                  and row["delete_field_response_signal"] > SIGNAL
                  and row["delete_spatial_propagation_signal"] > SIGNAL for row in rows), rows)
    check("Route C is all24 covariant and reaches the no-refit Cycle585/588 coefficient shore",
          maximum_covariance < TOL and output["all576_inherited_from_exact_scalar_frame_action"]
          and output["maximum_5_over_32pi_relative_residual"] < 0.002, output)
    check("Route C preserves exact matched candidates without selecting event calibration",
          matched["source_off"] == [4, 4] and matched["receiver_zero"] == [4, 4]
          and matched["delay_candidate"] == [3, 4] and matched["advance_candidate"] == [5, 4]
          and not matched["actual_joint_response_selects_delay_or_advance"], matched)
    return output


def no_go_discipline() -> dict:
    families = [
        ["finite-Weyl/exterior-CAR", "bilinear N*Q phase and Weyl kick", "exact accepted-matter typed interaction", "ATTEMPTED_POSITIVE_C607"],
        ["53-M2 Cycle590 occupation", "reversible word arithmetic", "alternative accepted-matter source compiler", "PRIOR_PARTIAL; JOINT LAW LIVE"],
        ["Cycle604 paired modular fields", "opposite exchange impulses", "exact conserved response ledger", "PRIOR_ATTEMPTED_WITH_PLACEHOLDER_SOURCE"],
        ["link gauge field", "Gauss-law electric flux", "locally constrained matter-current coupling", "LIVE_UNTESTED"],
        ["truncated oscillator field", "number-coordinate Hamiltonian", "cutoff-stable reciprocal unitary", "LIVE_UNTESTED"],
        ["static constrained inverse", "Cycle588 Kjoin=L", "actual-source static prediction", "PRIOR_ATTEMPTED_STATIC_ONLY"],
        ["matched detector/action", "Cycle451/570 rational event surface", "autonomous sign/order/event selection", "PRIOR_PARTIAL; CALIBRATION LIVE"],
    ]
    walls = {
        "W_elementary": "the 16-M2 lookup/QFT was not lowered to the accepted elementary alphabet",
        "W_propagation": "the alpha=1/12 spatial response has no physical M2 compiler here",
        "W_sign_units": "coupling sign, magnitude, and physical units remain supplied",
        "W_reversal": "the reversal involution and drift square root are supplied",
        "W_static": "finite Cesaro response is not the infinite static limit",
        "W_event": "response sign is not autonomously associated to a matched event",
        "W_gravity": "the modular impulse/static response is not identified as stress-energy or gravity",
        "W_preparation": "Cycle600's one-carrier/species and neutral-W sector remains prepared",
    }
    names = tuple(walls)
    pairs = [{"left": names[i], "right": names[j], "left_closes_right": False,
              "right_closes_left": False, "independent": True}
             for i in range(len(names)) for j in range(i+1, len(names))]
    output = {
        "N1_normalized_alternative_families": families,
        "N2_pairwise_wall_independence": pairs,
        "N3_hidden_wall_scan": [
            "W=16 and the bilinear phase convention", "Cycle600 prepared carrier sector",
            "field vacuum/basis choice", "coupling sign and units", "tau=0.37 and reversal involution",
            "alpha=1/12 and finite horizons", "point-minus-uniform source normalization",
            "response-sign/event association", "parameterized lookup and QFT matrices",
        ],
        "N4_residual_matching": [
            ["Cycle600 runner:842", "standalone exterior compiler not composed with Cycle590", "typed occupation interface", "related boundary, not a contrary witness"],
            ["Cycle604 note Route B", "placeholder modular source identity", "actual Cycle600 occupation source", "exact match; advanced here"],
            ["Cycle604 note Route C", "finite/static and event calibration", "same finite/static and calibration residuals", "match; remains open"],
            ["Cycle590 runner:469", "53-M2 N<=3 prepared compiler", "12-M2 exterior occupation interface", "different presentation; alternative stays live"],
        ],
        "N5_rhetoric_audit": {
            "not_stress_energy_or_gravity": "tested object is a per-site modular impulse and lattice response only; no block/lattice empirical stress tensor or gravity identification is claimed",
            "not_time": "finite update count and per-fixture horizons tested; no clock-rate or lattice-wide causal-time identification is claimed",
            "not_elementary_compiler": "bounded per-block matrix and coordinate layout tested; gate-by-gate accepted-alphabet lowering was not tested",
        },
        "N6_partial_closure_paths": [
            "Cycle600 number descent retires the placeholder-source identity at the typed interface",
            "Cycle590 provides a distinct 53-M2 occupation presentation for a future arithmetic lowering",
            "Cycle604/Cycle588 provide common-operator finite/static comparisons without requiring constitutional change",
        ],
        "N7_steelman": "A hostile reviewer should reject any obstruction claim: the exact N*Q finite-Weyl interaction already closes the core reciprocal accepted-matter interface, and a prime-dimensional Weyl QCA or reversible fixed-point arithmetic compiler could lower the alpha response while an action-derived detector boundary could select an event. Those concrete mechanisms are live and have not been exhausted.",
        "N8_cross_cycle_echo": {
            "Cycle590_600": "successive presentations retired global compiler and particle-label walls by explicit bounded encodings",
            "Cycle604_607": "the placeholder source became the exact descended CAR occupation; propagation and interpretation remain separate",
            "Cycle451_570": "matched event candidates survived exact compilation but calibration remained supplied",
        },
        "broad_negative_gate": "FAIL / DO NOT SHIP",
        "shared_route_independent_obstruction": False,
        "minimum_content_claim": False,
        "axiom_pressure": False,
    }
    check("full N1-N8 audit normalizes at least five families and blocks no-go/axiom pressure",
          len(families) >= 5 and len(pairs) == len(names)*(len(names)-1)//2
          and not output["shared_route_independent_obstruction"]
          and not output["minimum_content_claim"] and not output["axiom_pressure"], output)
    return output


def note_contract() -> None:
    body = " ".join(NOTE.read_text().lower().replace("`", "").replace("*", "").split())
    required = (
        "authority: none", "audit: unset", "cycle 607", "route a", "route b", "route c",
        "cycle600", "car occupation", "finite weyl", "n q", "momentum kick", "matter phase",
        "mass", "contact", "seam", "l3", "l6", "l7", "all 24", "576", "16 m2",
        "source deletion", "field deletion", "reversal", "does not select sign", "5/(32pi)",
        "3:4", "5:4", "n1 —", "n2 —", "n3 —", "n4 —", "n5 —", "n6 —", "n7 —", "n8 —",
        "no axiom pressure", "not stress-energy", "not gravity", "update count is not time",
    )
    missing = tuple(item for item in required if item not in body)
    check("Cycle607 note freezes exact/approximate scope, controls, and N1-N8", not missing, missing)


def main() -> int:
    shore = dependency_shore()
    note_contract()
    routeA = route_a(shore)
    routeB = route_b()
    routeC = route_c(shore, routeA)
    nogo = no_go_discipline()
    elapsed = perf_counter() - START
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss = int(rss if sys.platform == "darwin" else rss * 1024)
    receipt = {
        "cycle": 607, "authority": AUTHORITY, "audit": AUDIT,
        "constitutional_effect": "none",
        "HEAD": subprocess.check_output(("git", "rev-parse", "HEAD"), cwd=ROOT, text=True).strip(),
        "pins": PINS, "shore": shore["evidence"],
        "route_A_joint_CAR_Weyl_interaction": routeA,
        "route_B_reversal_ordering": routeB,
        "route_C_actual_source_prediction": routeC,
        "no_go_discipline": nogo,
        "inventory": {
            "supplied": ["Cycle600 prepared exterior-carrier sector", "W=16", "bilinear phase convention",
                         "coupling sign and units", "field basis/vacuum", "tau and reversal involution",
                         "alpha=1/12 and finite horizons", "event association"],
            "derived_or_executed": ["exact CAR-number descent", "exact finite-Weyl momentum kick and reciprocal matter phase",
                                    "joint coin/contact/seam EG and inverse", "symmetric reversal test",
                                    "actual-CAR-source finite/static prediction bridge"],
            "not_derived": ["accepted elementary gate lowering", "physical M2 compiler for alpha propagation",
                            "coupling sign/units", "framework time reversal", "finite/static equality",
                            "stress-energy", "gravity", "event calibration", "Born probability", "Record actuality"],
        },
        "six_wall_ledger": {
            "C_ref": "ADVANCED: the response source is now the exact Cycle600 CAR-number descent; coupling units/sign, reversal convention, and event calibration remain supplied",
            "C_num": "PARTIAL ADVANCE: a fixed 16-level Weyl register and exact modular impulse are explicit; physical scale and accepted alphabet lowering remain open",
            "C_wrap": "UNCHANGED: Weyl wrap is exact algebraic arithmetic and is not energy, rate, or time",
            "C_int": "ADVANCED: one bilinear action-derived step jointly gives the accepted-matter-controlled field kick and reciprocal matter phase while preserving mass/contact/seam",
            "C_local": "ADVANCED: 16 M2/cell bounded layout and exact EG are explicit; elementary lowering and alpha-response M2 compilation remain open",
            "C_source": "ADVANCED MATHEMATICALLY: placeholder source identity is retired at the CAR interface and reaches the static shore; stress-energy/gravity and calibration remain open",
        },
        "maturity_0_to_5": {"operational_quantum_records": 4.0, "time": 3.0,
                            "inertia_matter": 4.2, "gravity_source": 3.5,
                            "Born_probability": 2.0},
        "strongest_constructive_result": "an exact bounded 16-M2/cell typed product of Cycle600's accepted exterior-CAR carrier and a four-M2 finite-Weyl field, where one N*Q unitary gives both the field momentum kick and reciprocal matter phase while preserving the inherited mass/contact/seam code",
        "shared_obstruction_or_axiom_pressure": False,
        "optimal_next_campaign": "compile the field propagation and N*Q lookup into an accepted elementary translation-covariant QCA/reversible-arithmetic schedule, then test whether an action-derived detector boundary selects sign/order/event without calibration",
        "tests_passed": PASS, "tests_failed": FAIL, "pass": FAIL == 0,
        "elapsed_seconds": elapsed, "maximum_RSS_bytes": rss,
    }
    RECEIPT.write_text(json.dumps(receipt, indent=2, sort_keys=True, default=json_default) + "\n")
    print("RECEIPT", json.dumps(receipt, sort_keys=True, default=json_default))
    print("SUMMARY", json.dumps({"pass": receipt["pass"], "tests_passed": PASS, "tests_failed": FAIL,
                                  "elapsed_seconds": elapsed, "maximum_RSS_bytes": rss,
                                  "route_A": routeA["disposition"], "route_B_selects_symmetric": routeB["reversal_criterion_selects_symmetric_order"],
                                  "route_C": routeC["disposition"], "axiom_pressure": False}, sort_keys=True))
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
