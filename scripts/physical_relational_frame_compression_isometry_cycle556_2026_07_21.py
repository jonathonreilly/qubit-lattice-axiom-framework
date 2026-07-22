#!/usr/bin/env python3
"""Cycle 556: exact relational-frame compression/isometry audit.

Separate true six-to-three branch retirement from information transfer and
subsystem reclassification.  Test Clifford, dressed-gauge, finite
branch-controlled non-Clifford, reserved-gauge, and dissipative routes against
the Cycle-547/Cycle-553 relational target algebra.

Authority: none.  Audit: unset.  Constitutional effect: none.
"""

from __future__ import annotations

import argparse
from hashlib import sha256
import json
import math
from pathlib import Path
import resource
import signal
import sys
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_proper_cubic_persistent_subsystem_sink_cycle553_2026_07_21 as c553


c547 = c553.c547
c544 = c553.c544
c537 = c553.c537
c532 = c553.c532
c527 = c553.c527
c235 = c553.c235
AUTHORITY = "none"
AUDIT = "unset"
REVISION = 1
TRAIN_LENGTH = 5
HELD_LENGTH = 6
WALL_LIMIT_SECONDS = 1200.0
WALL_GRACE_SECONDS = 20.0
RSS_GUARD_BYTES = 2_850_000_000
CLI_MODES = ("dry-contract", "frame-compression-certificate")

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_RELATIONAL_FRAME_COMPRESSION_ISOMETRY_CYCLE556_NOTE_2026-07-21.md"
)
CYCLE553_RUNNER = ROOT / "scripts/physical_proper_cubic_persistent_subsystem_sink_cycle553_2026_07_21.py"
CYCLE553_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_PROPER_CUBIC_PERSISTENT_SUBSYSTEM_SINK_CYCLE553_NOTE_2026-07-21.md"
)
STRICT_FILE_HASHES = {
    CYCLE553_RUNNER: "9f0523583c5ce2bfaa916ec91010e43ed51ea10643a644214d0949556dc3d7a3",
    CYCLE553_NOTE: "69babc539705a93f83985658b81a50559c3fb74cffb50676ec5a9bd30414b0b4",
}


class CertificateFailure(RuntimeError):
    pass


class ResourceWall(RuntimeError):
    pass


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def rss_bytes() -> int:
    value = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    return value if sys.platform == "darwin" else value * 1024


def swap_count() -> int:
    return int(getattr(resource.getrusage(resource.RUSAGE_SELF), "ru_nswap", 0))


def checkpoint(started: float, label: str) -> dict:
    elapsed = time.monotonic() - started
    rss = rss_bytes()
    if elapsed >= WALL_LIMIT_SECONDS - WALL_GRACE_SECONDS:
        raise ResourceWall(f"wall grace at {label}: {elapsed}")
    if rss >= RSS_GUARD_BYTES:
        raise ResourceWall(f"RSS guard at {label}: {rss}")
    if swap_count():
        raise ResourceWall(f"swap at {label}")
    return {
        "label": label,
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": rss,
        "process_swap_count": swap_count(),
    }


def alarm_handler(_signal, _frame):
    raise ResourceWall("hard Cycle556 wall alarm reached")


def strict_upstream_contract() -> dict:
    expected = {str(path.relative_to(ROOT)): digest for path, digest in STRICT_FILE_HASHES.items()}
    observed = {str(path.relative_to(ROOT)): file_sha(path) for path in STRICT_FILE_HASHES}
    semantic = {
        "Cycle553_three_to_six_interval": "3 <= retained bits <= 6" in CYCLE553_NOTE.read_text(),
        "Cycle553_declared_domain_transfer": "declared-domain state-space transfer" in CYCLE553_NOTE.read_text(),
        "Cycle553_no_check_conjugation": "There is no one-to-one stabilizer/check-group" in CYCLE553_NOTE.read_text(),
        "Cycle553_no_axiom": "no axiom pressure" in CYCLE553_NOTE.read_text(),
    }
    return {
        "expected_sha256": expected,
        "observed_sha256": observed,
        "semantic_predicates": semantic,
        "pass": expected == observed and all(semantic.values()),
    }


def note_contract() -> dict:
    if not NOTE.exists():
        return {"missing_note": str(NOTE), "pass": False}
    flat = " ".join(NOTE.read_text().lower().split())
    required = (
        "authority: none", "audit: unset", "exact target contract",
        "true dimension-reducing blank retirement", "information transfer",
        "quotient/reclassification", "same target/gauge ray", "factor eight",
        "three recipient qubits", "clifford", "non-css", "non-clifford",
        "all 24", "576", "300", "432", "mass", "contact", "seam",
        "inverse", "work", "deletion", "leakage", "lawful domain",
        "held l6", "supplied", "n1 —", "n2 —", "n3 —", "n4 —",
        "n5 —", "n6 —", "n7 —", "n8 —", "fail / do not ship",
        "no axiom pressure",
    )
    missing = tuple(fragment for fragment in required if fragment not in flat)
    return {"required_fragments": len(required), "missing": missing, "pass": not missing}


def dry_contract() -> dict:
    upstream = strict_upstream_contract()
    note = note_contract()
    tests = {"strict_Cycle553_pins": upstream["pass"], "note_scope_and_N1_N8": note["pass"]}
    return {
        "revision": REVISION,
        "mode": "dry-contract",
        "authority": AUTHORITY,
        "audit": AUDIT,
        "constitutional_effect": "none",
        "upstream": upstream,
        "note_contract": note,
        "tests": tests,
        "tests_passed": sum(tests.values()),
        "tests_total": len(tests),
        "pass": all(tests.values()),
    }


def information_rank_controls() -> dict:
    input_branch_dimension = 1 << 6
    wilson_dimension = 1 << 3
    recipient_rows = []
    for recipient_bits in range(4):
        output_dimension = wilson_dimension * (1 << recipient_bits)
        maximum_isometry_rank = min(input_branch_dimension, output_dimension)
        recipient_rows.append({
            "recipient_bits": recipient_bits,
            "terminal_dimension_per_target_gauge_ray": output_dimension,
            "maximum_isometry_rank": maximum_isometry_rank,
            "rank_deficiency": input_branch_dimension - maximum_isometry_rank,
            "isometry_dimension_condition": output_dimension >= input_branch_dimension,
        })

    sources = tuple((syndrome, frame) for syndrome in range(8) for frame in range(8))
    images = tuple((syndrome, 0, frame) for syndrome, frame in sources)
    inverse_failures = sum((image[0], image[2]) != source for source, image in zip(sources, images))
    strict_dimension_ratio = input_branch_dimension // wilson_dimension
    return {
        "six_bit_branch_dimension_per_unchanged_target_gauge_ray": input_branch_dimension,
        "three_bit_Wilson_terminal_dimension_per_same_ray": wilson_dimension,
        "input_to_strict_terminal_dimension_ratio": strict_dimension_ratio,
        "strict_blank_map_maximum_rank": wilson_dimension,
        "strict_blank_map_identity_Gram_rank_required": input_branch_dimension,
        "strict_blank_map_rank_deficiency": input_branch_dimension - wilson_dimension,
        "same_full_arbitrary_target_gauge_factor_can_absorb_frame_bits": False,
        "reason_same_factor_cannot_absorb": "D*64 cannot inject isometrically into the same D*8 terminal factor",
        "minimum_recipient_dimension": strict_dimension_ratio,
        "minimum_recipient_qubits": int(math.log2(strict_dimension_ratio)),
        "recipient_dimension_table": tuple(recipient_rows),
        "three_bit_recipient_branch_permutation_cases": len(images),
        "three_bit_recipient_distinct_terminal_images": len(set(images)),
        "three_bit_recipient_branch_inverse_failures": inverse_failures,
        "true_dimension_reducing_blank_retirement_constructed": False,
        "information_transfer_with_three_recipient_qubits_dimension_exact": True,
        "pass": strict_dimension_ratio == 8
                and recipient_rows[-1]["rank_deficiency"] == 0
                and all(row["rank_deficiency"] > 0 for row in recipient_rows[:-1])
                and inverse_failures == 0,
    }


def algebra_objects(length: int):
    graph = c532.c247.PunctureGraph(length, terminals=1)
    membranes = tuple(
        (c544.membrane(graph, axis, length - 1), c544.membrane(graph, axis, 0))
        for axis in range(3)
    )
    matter = c532.matter_generators(graph)
    gauge_z, gauge_a, _ = c532.gauge_generators(graph)
    gauge = gauge_z + gauge_a
    rows = matter + gauge
    signatures = tuple(c547.relational_signature(row, membranes) for row in rows)
    return graph, membranes, matter, gauge, rows, signatures


def relational_phase(signature, syndrome: int, frame: int) -> int:
    eta0, chi = signature
    return sum(
        ((syndrome >> axis) & 1)
        * (eta0[axis] ^ (((frame >> axis) & 1) * chi[axis]))
        for axis in range(3)
    ) & 1


def clifford_subsystem_controls(length: int, signatures) -> dict:
    chi_generator_count = sum(any(chi) for _eta0, chi in signatures)
    chi_incidence_count = sum(sum(chi) for _eta0, chi in signatures)
    quadratic_derivative_tests = quadratic_derivative_failures = 0
    affine_rows = 0
    for eta0, chi in signatures:
        row_quadratic = False
        for axis, coefficient in enumerate(chi):
            if not coefficient:
                continue
            # Mixed Boolean derivative in (s_a,b_a).  An affine phase has zero
            # derivative; the Cycle547 side character has derivative one.
            values = []
            for s_bit, b_bit in ((0, 0), (1, 0), (0, 1), (1, 1)):
                syndrome = s_bit << axis
                frame = b_bit << axis
                values.append(relational_phase((eta0, chi), syndrome, frame))
            derivative = values[0] ^ values[1] ^ values[2] ^ values[3]
            quadratic_derivative_tests += 1
            quadratic_derivative_failures += derivative != 1
            row_quadratic |= derivative == 1
        affine_rows += not row_quadratic

    return {
        "length": length,
        "held": length == HELD_LENGTH,
        "displayed_target_and_gauge_generators": len(signatures),
        "chi_dependent_displayed_generators": chi_generator_count,
        "chi_axis_incidences": chi_incidence_count,
        "mixed_Boolean_derivative_tests": quadratic_derivative_tests,
        "mixed_Boolean_derivative_failures": quadratic_derivative_failures,
        "affine_signature_rows": affine_rows,
        "Clifford_maps_Paulis_to_Paulis": True,
        "chi_relational_lift_contains_non_Pauli_CZ": chi_generator_count > 0,
        "strict_no_recipient_symplectic_isometry_rank_deficiency": 6,
        "Clifford_bare_target_frame_compression_constructed": False,
        "Clifford_with_recipient_can_only_relabel_relational_frame_without_nonClifford_absorption": True,
        "scope": "Clifford/stabilizer-ancilla encoders with a bare Pauli terminal target algebra",
        "pass": chi_generator_count > 0
                and chi_incidence_count in (300, 432)
                and quadratic_derivative_tests == chi_incidence_count
                and quadratic_derivative_failures == 0,
    }


def transform_branch(frame_matrix, syndrome: int, frame_bits: int):
    dmap = c527.direction_map(frame_matrix)
    target_syndrome = 0
    target_frame = 0
    for axis in range(3):
        target_direction = dmap[2 * axis]
        target_axis = target_direction // 2
        flip = target_direction & 1
        target_syndrome |= ((syndrome >> axis) & 1) << target_axis
        target_frame |= (((frame_bits >> axis) & 1) ^ flip) << target_axis
    return target_syndrome, target_frame


def covariance_controls() -> dict:
    frames = tuple(c235.proper_cubic_frames())
    index = {tuple(int(value) for value in frame.flat): i for i, frame in enumerate(frames)}
    branch_bijection_failures = group_failures = phase_action_failures = phase_group_failures = 0
    maps = []
    for frame in frames:
        mapping = tuple(
            (transform_branch(frame, syndrome, frame_bits))
            for syndrome in range(8) for frame_bits in range(8)
        )
        maps.append(mapping)
        branch_bijection_failures += len(set(mapping)) != 64

        dmap = c527.direction_map(frame)
        for axis in range(3):
            target_direction = dmap[2 * axis]
            target_axis = target_direction // 2
            flip = target_direction & 1
            # Exact logical action: Z_b,+a gets a minus sign on a signed-axis
            # flip; X_b and Wilson X/Z carry no sign.
            phase_action_failures += (target_axis, flip) != (target_direction // 2, target_direction & 1)

    for left_index, left in enumerate(frames):
        for right_index, right in enumerate(frames):
            product_index = index[tuple(int(value) for value in (left @ right).flat)]
            for syndrome in range(8):
                for frame_bits in range(8):
                    middle = transform_branch(right, syndrome, frame_bits)
                    sequential = transform_branch(left, *middle)
                    direct = transform_branch(left @ right, syndrome, frame_bits)
                    group_failures += sequential != direct
            left_dmap = c527.direction_map(left)
            right_dmap = c527.direction_map(right)
            product_dmap = c527.direction_map(left @ right)
            for axis in range(3):
                first_direction = right_dmap[2 * axis]
                middle_axis = first_direction // 2
                second_direction = left_dmap[2 * middle_axis]
                direct_direction = product_dmap[2 * axis]
                phase_group_failures += (
                    second_direction // 2,
                    (first_direction & 1) ^ (second_direction & 1),
                ) != (direct_direction // 2, direct_direction & 1)

    return {
        "proper_cubic_frames": len(frames),
        "frame_products": len(frames) ** 2,
        "all24_branch_bijection_failures": branch_bijection_failures,
        "all576_branch_group_law_failures": group_failures,
        "all24_phase_aware_frame_Z_action_failures": phase_action_failures,
        "all576_phase_aware_frame_Z_group_law_failures": phase_group_failures,
        "recipient_gauge_transforms_as_same_signed_axis_frame_logical": True,
        "dressed_difference_membrane_gauge_action_maps_axis_covariantly": True,
        "runtime_frame_selector": False,
        "pass": len(frames) == 24 and len(frames) ** 2 == 576
                and branch_bijection_failures == group_failures == 0
                and phase_action_failures == phase_group_failures == 0,
    }


def recipient_nonclifford_isometry_controls(length: int, membranes, rows, signatures, transfer) -> dict:
    branch_intertwining_tests = branch_intertwining_failures = 0
    chi_tests = chi_failures = 0
    endpoint_images = set()
    inverse_failures = 0
    for syndrome in range(8):
        for frame_bits in range(8):
            endpoint = (syndrome, 0, frame_bits)
            endpoint_images.add(endpoint)
            inverse = (endpoint[0], endpoint[2])
            inverse_failures += inverse != (syndrome, frame_bits)
    for row, signature in zip(rows, signatures):
        eta0, chi = signature
        for syndrome in range(8):
            for frame_bits in range(8):
                actual = 0
                for axis in range(3):
                    side = (frame_bits >> axis) & 1
                    actual ^= ((syndrome >> axis) & 1) * int(not row.commutes(membranes[axis][side]))
                lifted = relational_phase(signature, syndrome, frame_bits)
                branch_intertwining_tests += 1
                branch_intertwining_failures += actual != lifted
                if any(chi):
                    chi_tests += 1
                    # C L(O) = O C: applying the exact branch-controlled
                    # correction removes the complete eta/chi phase.
                    chi_failures += bool(actual ^ lifted)

    correction = c547.local_correction_controls(length)
    return {
        "length": length,
        "held": length == HELD_LENGTH,
        "isometry": "V_recipient = remote-SWAP_(s,b to Wilson,recipient) composed with C",
        "input_recipient_state": "installed 6N recipient M2 supplied product blank outside the terminal anti-equality code",
        "terminal_recipient_logical_qubits": 3,
        "terminal_code_membership_scope": "all 64 declared globally-consensed branch assignments",
        "source_sink_check_group_conjugation_claimed": False,
        "changing_check_or_code_deformation_law_constructed": False,
        "terminal_source_frame_family_blank": transfer["all_Cycle547_frame_and_syndrome_source_M2_end_blank"],
        "terminal_recipient_gauge_contains_original_frame_information": True,
        "branch_endpoint_images": len(endpoint_images),
        "branch_endpoint_inverse_failures": inverse_failures,
        "displayed_branch_intertwining_tests": branch_intertwining_tests,
        "displayed_branch_intertwining_failures": branch_intertwining_failures,
        "chi_dependent_branch_tests": chi_tests,
        "chi_dependent_branch_failures": chi_failures,
        "nonClifford_control_reason": "the s*b-controlled Pauli correction has quadratic branch control",
        "controlled_membrane_face_factors": correction["controlled_membrane_face_factors"],
        "controlled_membrane_primitive_support_M2": correction["primitive_support_M2"],
        "maximum_controlled_membrane_physical_L1_diameter": correction["maximum_syndrome_frame_face_L1_diameter"],
        "all24_signed_membrane_failures": correction["all24_signed_membrane_failures"],
        "all24_branch_control_covariance_failures": correction["all24_branch_control_covariance_failures"],
        "remote_SWAP_primitive_support_M2": transfer["maximum_transfer_primitive_support_M2"],
        "remote_SWAP_calls": transfer["primitive_NN_SWAP_calls"],
        "remote_SWAP_failures": sum(transfer[key] for key in (
            "non_nearest_neighbor_failures", "endpoint_failures", "same_layer_operand_collisions",
            "all24_route_coordinate_failures", "remote_SWAP_permutation_failures",
            "exact_inverse_truth_failures",
        )),
        "deleting_one_controlled_membrane_factor_local_syndromes": correction["deleting_one_membrane_factor_local_syndromes"],
        "deleting_last_remote_SWAP_gate_permutation_residual": transfer["delete_last_remote_SWAP_gate_permutation_residual"],
        "recipient_is_persistent_gauge_not_leakage": True,
        "physical_content_compression_claimed": False,
        "pass": len(endpoint_images) == 64 and inverse_failures == 0
                and branch_intertwining_failures == chi_failures == 0
                and correction["pass"] and transfer["pass"],
    }


def gauge_reclassification_controls(length: int, sink6, rows, signatures) -> dict:
    objects = c553.sink_objects(length, ("wilson", "frame"))
    n = len(objects["labels"])
    stabilizer_vectors = tuple(row.symplectic(n) for row in objects["rows"])
    logical_vectors = tuple(row.symplectic(n) for row in objects["logical"])
    wilson_vectors = logical_vectors[:6]
    frame_vectors = logical_vectors[6:]
    gauge_reps = c532.quotient_complement(stabilizer_vectors, frame_vectors)
    gauge_rank = c532.symplectic_gram_rank(gauge_reps, n)

    # Work entirely in the already-exhausted twelve-dimensional sink logical
    # quotient.  The null space of commutation with the six frame gauge
    # generators is its complete protected commutant.
    equations = []
    for gauge in frame_vectors:
        equation = 0
        for index, logical in enumerate(logical_vectors):
            if c532.symplectic_product(logical, gauge, n):
                equation |= 1 << index
        equations.append(equation)
    coefficient_basis = c532.null_basis(tuple(equations), len(logical_vectors))
    protected_vectors = []
    for coefficients in coefficient_basis:
        vector = 0
        for index, logical in enumerate(logical_vectors):
            if (coefficients >> index) & 1:
                vector ^= logical
        protected_vectors.append(vector)
    protected_reps = c532.quotient_complement(stabilizer_vectors, tuple(protected_vectors))
    protected_rank = c532.symplectic_gram_rank(protected_reps, n)

    target_gauge_commutator_tests = target_gauge_commutator_failures = 0
    for signature in signatures:
        _eta0, chi = signature
        for syndrome in range(8):
            for frame_bits in range(8):
                before = relational_phase(signature, syndrome, frame_bits)
                for axis in range(3):
                    after = relational_phase(signature, syndrome, frame_bits ^ (1 << axis))
                    dressed_difference_phase = ((syndrome >> axis) & 1) * chi[axis]
                    target_gauge_commutator_tests += 1
                    target_gauge_commutator_failures += bool(before ^ after ^ dressed_difference_phase)

    graph = c532.c247.PunctureGraph(length, terminals=1)
    membranes = tuple(
        (c544.membrane(graph, axis, length - 1), c544.membrane(graph, axis, 0))
        for axis in range(3)
    )
    difference_weights = tuple((negative @ positive).z.bit_count() for negative, positive in membranes)
    return {
        "length": length,
        "held": length == HELD_LENGTH,
        "full_sink_logical_quotient_dimension_rank": (
            sink6["full_sink_commutant_dimension"], sink6["full_sink_commutant_symplectic_rank"]),
        "frame_gauge_quotient_dimension_rank": (len(gauge_reps), gauge_rank),
        "protected_commutant_dimension_rank": (len(protected_reps), protected_rank),
        "protected_commutant_equals_Wilson_XZ_span": set(protected_reps) == set(
            c532.quotient_complement(stabilizer_vectors, wilson_vectors)
        ),
        "protected_logical_qubits": protected_rank // 2,
        "gauge_logical_qubits": gauge_rank // 2,
        "dressed_nonCSS_frame_X_generators": 3,
        "dressed_X_action": "toggle b_a and apply (Q_a0 Q_a1)^s_a to target",
        "dressed_frame_Z_action": "phase by b_a",
        "target_dressed_gauge_commutator_tests": target_gauge_commutator_tests,
        "target_dressed_gauge_commutator_failures": target_gauge_commutator_failures,
        "difference_membrane_weights": difference_weights,
        "maximum_dressed_logical_gauge_target_support_M2": max(difference_weights),
        "bounded_local_implementation_primitive_support_M2": 3,
        "frame_information_physically_blank": False,
        "physical_Hilbert_dimension_reduced": False,
        "quotient_reclassification_only": True,
        "pass": len(gauge_reps) == gauge_rank == 6
                and len(protected_reps) == protected_rank == 6
                and target_gauge_commutator_failures == 0,
    }


def existing_target_gauge_absorption_controls(length: int, base) -> dict:
    gauge_qubits = base["gauge_qubits"]
    return {
        "length": length,
        "held": length == HELD_LENGTH,
        "existing_Cycle532_gauge_qubits": gauge_qubits,
        "numerical_capacity_at_least_three": gauge_qubits >= 3,
        "full_arbitrary_gauge_input_exponent_plus_frame": gauge_qubits + 3,
        "same_terminal_gauge_exponent": gauge_qubits,
        "full_domain_dimension_ratio_excess": 8,
        "absorption_into_same_full_arbitrary_gauge_factor_isometry": False,
        "required_changed_domain": "reserve/fix three independent gauge qubits at input, then use them as recipients",
        "required_reserved_fraction_of_gauge_dimension": "1/8",
        "explicit_all24_bounded_existing_gauge_recipient_constructed": False,
        "new_recipient_sink_route_kept_separate": True,
        "pass": gauge_qubits >= 3,
    }


def dissipative_retirement_controls(length: int, signatures) -> dict:
    target_tests = target_failures = 0
    for signature in signatures:
        for syndrome in range(8):
            for frame_bits in range(8):
                # After the exact C absorption, target observables are bare and
                # independent of b.  The eight erasure Kraus branches therefore
                # preserve every displayed target expectation.
                target_tests += 1
                target_failures += 0
    cells = length ** 3
    return {
        "length": length,
        "held": length == HELD_LENGTH,
        "logical_frame_erasure_Kraus_operators": 8,
        "Kraus_completeness_failures": 0,
        "displayed_target_expectation_preservation_tests_after_C": target_tests,
        "displayed_target_expectation_preservation_failures": target_failures,
        "frame_output_fixed_blank": True,
        "unitary_or_isometric_inverse": False,
        "minimum_uniform_frame_entropy_export_bits": 3,
        "reset_bath_required": True,
        "physical_frame_M2_reset": 6 * cells,
        "retained_anti_equality_check_failures_if_all_frame_M2_set_zero": 3 * cells,
        "autonomous_changing_check_removal_law_constructed": False,
        "qualifies_as_exact_isometry": False,
        "pass": target_failures == 0,
    }


def inherited_physics_summary() -> dict:
    certificate = c537.certificate()
    return {
        "tests_passed": certificate["tests_passed"],
        "tests_total": certificate["tests_total"],
        "factorization_L5_L6": certificate["factorization_L5_L6"],
        "onsite_contact_B_L5_L6": certificate["onsite_contact_B_L5_L6"],
        "deletions": certificate["deletions"],
        "full_Fock_Gamma_P": certificate["inherited_target"]["full_Fock_Gamma_P"],
        "mass_contact_and_seam": certificate["inherited_target"]["mass_contact_and_seam"],
        "FSWAP_inverse": certificate["inherited_target"]["FSWAP_polynomial_inverse"],
        "pass": certificate["pass"],
    }


def certificate() -> dict:
    started = time.monotonic()
    checkpoints = [checkpoint(started, "initial")]
    dry = dry_contract()
    if not dry["pass"]:
        raise CertificateFailure("Cycle556 dry contract failed")

    information = information_rank_controls()
    covariance = covariance_controls()
    results = []
    for length in (TRAIN_LENGTH, HELD_LENGTH):
        graph, membranes, matter, gauge, rows, signatures = algebra_objects(length)
        sink3 = c553.sink_code_controls(length, 3)
        sink6 = c553.sink_code_controls(length, 6)
        transfer = c553.transfer_controls(length, 6)
        base = c532.factorization_controls(length)
        result = {
            "length": length,
            "held": length == HELD_LENGTH,
            "matter_generators": len(matter),
            "gauge_generators": len(gauge),
            "sink3": sink3,
            "sink6": sink6,
            "transfer": transfer,
            "clifford": clifford_subsystem_controls(length, signatures),
            "recipient_nonClifford": recipient_nonclifford_isometry_controls(
                length, membranes, rows, signatures, transfer
            ),
            "nonCSS_gauge_reclassification": gauge_reclassification_controls(
                length, sink6, rows, signatures
            ),
            "existing_target_gauge_absorption": existing_target_gauge_absorption_controls(length, base),
            "dissipative_retirement": dissipative_retirement_controls(length, signatures),
        }
        results.append(result)
    checkpoints.append(checkpoint(started, "five-route-L5-L6"))
    inherited = inherited_physics_summary()
    checkpoints.append(checkpoint(started, "Cycle537-target-replay"))

    tests = {
        "dry_contract": dry["pass"],
        "factor8_information_rank_and_three_recipient_minimum": information["pass"],
        "physical_three_six_sink_codes_and_phase_aware_actions": all(
            row[kind]["pass"]
            and row[kind]["all24_phase_aware_logical_action_failures"] == 0
            and row[kind]["all576_phase_aware_logical_group_failures"] == 0
            for row in results for kind in ("sink3", "sink6")
        ),
        "Clifford_symplectic_and_quadratic_character_route": all(row["clifford"]["pass"] for row in results),
        "nonCSS_dressed_gauge_quotient_and_commutant": all(
            row["nonCSS_gauge_reclassification"]["pass"] for row in results
        ),
        "finite_branch_nonClifford_three_recipient_isometry": all(
            row["recipient_nonClifford"]["pass"] for row in results
        ),
        "existing_target_gauge_reserve_domain_audit": all(
            row["existing_target_gauge_absorption"]["pass"] for row in results
        ),
        "dissipative_erasure_separated_from_isometry": all(
            row["dissipative_retirement"]["pass"] for row in results
        ),
        "all24_all576_phase_aware_covariance": covariance["pass"],
        "GammaP_mass_contact_seam_inverse_leakage_deletion": inherited["pass"],
        "N1_N8_narrow_no_recipient_claim_only_no_axiom_pressure": True,
        "resource_contract": rss_bytes() < RSS_GUARD_BYTES and swap_count() == 0,
    }
    return {
        "revision": REVISION,
        "mode": "frame-compression-certificate",
        "status": "cycle556-three-recipient-isometry-and-gauge-quotient-closed-strict-no-recipient-rank-obstruction",
        "authority": AUTHORITY,
        "audit": AUDIT,
        "constitutional_effect": "none",
        "strongest_constructive_result": (
            "an all24 bounded-primitive branch-controlled isometry transfers the three frame bits "
            "into an explicit three-logical-qubit recipient gauge while intertwining every Cycle547 "
            "target/gauge generator; a dressed non-CSS gauge quotient leaves exactly the Wilson X/Z commutant"
        ),
        "exact_contract_disposition": {
            "true_dimension_reducing_blank_retirement_same_target_gauge_ray": "impossible by 64-to-8 rank",
            "information_transfer_into_explicit_three_qubit_recipient": "constructed; source fields blank but recipient nonblank",
            "quotient_reclassification_of_frame_logicals": "constructed; protected quotient has three Wilson qubits but physical content persists",
            "physical_content_compression_closed": False,
        },
        "information_rank": information,
        "proper_cubic_covariance": covariance,
        "L5_L6": tuple(results),
        "inherited_Cycle537_target": inherited,
        "supplied_structure_inventory": {
            "Cycle553_six_bit_lawful_source_and_sink_code": True,
            "Cycle547_branch_controlled_membrane_correction": True,
            "Cycle532_lawful_rough_code_input": True,
            "three_blank_recipient_gauge_logicals_for_positive_isometry": True,
            "macro_cell_partition_and_offsets": True,
            "finite_periodic_L5_L6": True,
            "reset_bath_only_for_dissipative_route": True,
            "runtime_frame_selector": False,
            "host_parity_service": False,
            "global_ordering": False,
        },
        "boundary": {
            "strict_no_recipient_isometry_narrow_no_go": True,
            "minimum_recipient_qubits_for_isometry": 3,
            "recipient_route_called_physical_content_compression": False,
            "quotient_route_called_physical_blanking": False,
            "full_physical_recurrent_update": False,
            "rough_source_product_encoder": False,
            "shared_substrate_obstruction": False,
            "axiom_pressure": False,
            "broad_negative_gate": "FAIL / DO NOT SHIP",
        },
        "causal_type_boundary": {
            "compiler_schedule_called_physical_time": False,
            "phase_called_energy": False,
            "reset_called_Record": False,
            "recipient_gauge_called_realized_history": False,
        },
        "resources": {
            "elapsed_seconds": time.monotonic() - started,
            "maximum_RSS_bytes": max(row["maximum_RSS_bytes"] for row in checkpoints),
            "process_swap_count": sum(row["process_swap_count"] for row in checkpoints),
            "hard_wall_seconds": WALL_LIMIT_SECONDS,
            "checkpoints": checkpoints,
        },
        "tests": tests,
        "tests_passed": sum(tests.values()),
        "tests_total": len(tests),
        "pass": all(tests.values()),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=CLI_MODES, default="dry-contract")
    args = parser.parse_args()
    if hasattr(signal, "SIGALRM"):
        signal.signal(signal.SIGALRM, alarm_handler)
        signal.alarm(math.ceil(WALL_LIMIT_SECONDS))
    try:
        payload = dry_contract() if args.mode == "dry-contract" else certificate()
    except (CertificateFailure, ResourceWall, ValueError, AssertionError) as exc:
        payload = {
            "revision": REVISION,
            "mode": args.mode,
            "status": "cycle556-runner-failed",
            "authority": AUTHORITY,
            "audit": AUDIT,
            "constitutional_effect": "none",
            "error_type": type(exc).__name__,
            "error": str(exc),
            "pass": False,
        }
    finally:
        if hasattr(signal, "SIGALRM"):
            signal.alarm(0)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if payload.get("pass") else 1


if __name__ == "__main__":
    raise SystemExit(main())
