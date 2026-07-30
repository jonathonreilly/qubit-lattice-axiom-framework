#!/usr/bin/env python3
"""Bounded two-cell covariance certificate for 23 parity-even CAR rows.

The runner joins the landed Cycle655 seven-mode encoder, the landed Cycle720
proper-frame/origin action, and the landed Cycle789 three-register channel on
the fixed two-cell shape ``(2, 1, 1)``.  It directly checks every one of the
23 parity-even rows in every declared frame, origin, and ordered frame
product.  The scope is the parity-even observable algebra only.  No odd
section, cross-parity coherence, runtime frame selector, literal prefix, or
recurrent-G executor is constructed here.
"""

from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path

import numpy as np

import frontier_companion_bank_bell_character_dilation_2026_07_28 as B
import frontier_cycle720_companion_2cube_m2_stinespring_covariance_2026_07_27 as S720
import frontier_cycle720_companion_checkerboard_frame_cocycle_2026_07_27 as Q720
import frontier_cycle789_three_register_even_car_channel_2026_07_30 as C789
import frontier_full128_cycle_encoder_2026_07_24 as F655
import frontier_full128_two_cell_even_car_frame_core_2026_07_30 as E


AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/FULL128_TWO_CELL_PARITY_SUPERSELECTED_EVEN_CAR_COVARIANCE_CYCLE820_BOUNDED_THEOREM_NOTE_2026-07-30.md",
    "scripts/frontier_cycle820_full128_two_cell_parity_superselected_even_car_covariance_2026_07_30.py",
    "scripts/frontier_cycle820_full128_two_cell_parity_superselected_even_car_independent_2026_07_30.py",
    "scripts/frontier_full128_two_cell_even_car_frame_core_2026_07_30.py",
    "scripts/frontier_full128_cycle_encoder_2026_07_24.py",
    "scripts/frontier_cycle720_companion_checkerboard_frame_cocycle_2026_07_27.py",
    "scripts/frontier_cycle720_companion_2cube_m2_stinespring_covariance_2026_07_27.py",
    "scripts/frontier_cycle720_companion_fixed_sector_live_input_teleportation_2026_07_27.py",
    "scripts/frontier_companion_bank_bell_character_dilation_2026_07_28.py",
    "scripts/frontier_cycle789_three_register_even_car_channel_2026_07_30.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS
IMPORT_MODULES = (
    "frontier_companion_bank_bell_character_dilation_2026_07_28",
    "frontier_cycle720_companion_2cube_m2_stinespring_covariance_2026_07_27",
    "frontier_cycle720_companion_checkerboard_frame_cocycle_2026_07_27",
    "frontier_cycle789_three_register_even_car_channel_2026_07_30",
    "frontier_full128_cycle_encoder_2026_07_24",
    "frontier_full128_two_cell_even_car_frame_core_2026_07_30",
)


def file_sha256(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def add_graph_counts(total: dict[str, int], row: dict[str, int]) -> None:
    for key in ("comparisons", "binary_failures", "signed_failures"):
        total[key] += int(row[key])


def pauli_commutator_failures(
    rows: tuple[E.Pauli, ...],
    parity: E.Pauli,
    width: int,
) -> int:
    return sum(
        B.M.symplectic(
            row.symplectic(width),
            parity.symplectic(width),
            width,
        )
        for row in rows
    )


def two_cell_hostile_controls(atlas) -> dict[str, object]:
    """Delete every correction and flip every retained Bell-ancilla sign."""
    obj = C789.circuit_objects(E.SHAPE, atlas)
    rank = int(obj["rank"])
    q = int(obj["q"])
    width = int(obj["width"])
    initial = tuple(obj["resource"] + obj["live_reference"] + obj["ancilla_z"])
    baseline = C789.conjugate_basis(initial, obj["gates"])
    baseline_binary, baseline_signed = C789.signed_span_failures(
        obj["output_reference"],
        baseline,
        width,
    )

    deletion_rows = []
    for deleted_index in range(rank):
        ancilla = 4 * q + deleted_index
        deleted_gates = tuple(
            gate for gate in obj["gates"]
            if not (
                gate[0] == "CP"
                and gate[1] == ancilla
                and gate[2] < q
            )
        )
        final = C789.conjugate_basis(initial, deleted_gates)
        binary, signed = C789.signed_span_failures(
            obj["output_reference"],
            final,
            width,
        )
        deletion_rows.append((binary, signed))

    sign_rows = []
    for changed_index in range(rank):
        changed_initial = list(initial)
        position = 2 * rank + changed_index
        row = changed_initial[position]
        changed_initial[position] = E.Pauli(
            (row.phase + 2) % 4,
            row.x,
            row.z,
        )
        final = C789.conjugate_basis(
            tuple(changed_initial),
            obj["gates"],
        )
        binary, signed = C789.signed_span_failures(
            obj["output_reference"],
            final,
            width,
        )
        sign_rows.append((binary, signed))

    return {
        "rank": rank,
        "baseline_binary_failures": baseline_binary,
        "baseline_signed_failures": baseline_signed,
        "correction_deletions_tested": len(deletion_rows),
        "correction_deletions_detected": sum(
            binary + signed > 0 for binary, signed in deletion_rows
        ),
        "minimum_correction_deletion_failures": min(
            binary + signed for binary, signed in deletion_rows
        ),
        "Bell_ancilla_sign_mutations_tested": len(sign_rows),
        "Bell_ancilla_sign_mutations_detected": sum(
            binary + signed > 0 for binary, signed in sign_rows
        ),
        "minimum_Bell_ancilla_sign_mutation_failures": min(
            binary + signed for binary, signed in sign_rows
        ),
        "sign_mutation_binary_failures": sum(
            binary for binary, _signed in sign_rows
        ),
    }


def main() -> None:
    frames = tuple(F655.FRAMES)
    frame_index = {
        E.frame_key(frame): index for index, frame in enumerate(frames)
    }
    atlas = B.P.build_private_atlases()
    base = B.O.arbitrary_fixture(B.Q.shape_cells(E.SHAPE))
    base_even = E.transformed_even_basis_and_duals(base, atlas)
    rank = len(base_even["physical"])
    tree_indices = E.even_source_tree_indices(tuple(base_even["tags"]))
    source_choi = E.compact_source_choi(base_even, tree_indices)
    source_parity = E.pauli_product(base_even["physical"][:base.matter_qubits])
    target_parity = E.pauli_product(base_even["targets"][:base.matter_qubits])

    cycle789 = C789.channel_certificate(E.SHAPE, atlas)
    hostile = two_cell_hostile_controls(atlas)

    raw_encoder_images = E.encoder_images()
    raw_decoder_images = E.decoder_images()
    raw_encoder_inverse_failures = sum((
        not Q720.images_equal(
            S720.compose_images(raw_encoder_images, raw_decoder_images),
            S720.identity_images(F655.PHYSICAL_M2),
        ),
        not Q720.images_equal(
            S720.compose_images(raw_decoder_images, raw_encoder_images),
            S720.identity_images(F655.PHYSICAL_M2),
        ),
    ))

    cache = {}

    def rotated(frame: np.ndarray):
        cells = Q720.affine_cells(base.cells, frame, E.ZERO)
        if cells not in cache:
            fixture = B.O.arbitrary_fixture(cells)
            even = E.transformed_even_basis_and_duals(fixture, atlas)
            cache[cells] = (fixture, even)
        return cache[cells]

    frame_graph = {
        "comparisons": 0,
        "binary_failures": 0,
        "signed_failures": 0,
    }
    frame_origin_contexts = 0
    frame_parity_comparisons = 0
    frame_parity_commutator_failures = 0
    direction_map_failures = 0
    role_embedding_bijection_failures = 0
    role_embedding_signed_failures = 0
    raw_code_constraint_frame_failures = 0
    source_choi_frame_comparisons = 0
    source_choi_frame_binary_failures = 0
    source_choi_frame_signed_failures = 0
    rotated_basis_replay_failures = 0
    frame_data = []

    for frame in frames:
        fixture, even = rotated(frame)
        direction_map = Q720.direction_permutation(frame)
        direction_map_failures += direction_map != F655.mode_map(frame)
        abstract_images = E.mode_images(E.role_action(frame))
        embedding = E.candidate_role_embedding(base, fixture, frame)
        embedding_images = E.mode_images(embedding)
        role_embedding_bijection_failures += len(set(embedding)) != 12
        target_images = Q720.matter_images(base, fixture, frame, E.ZERO)
        role_embedding_signed_failures += not Q720.images_equal(
            target_images,
            S720.compose_images(embedding_images, abstract_images),
        )

        decoded7_images = E.mode_images(F655.mode_map(frame) + (6,))
        raw22_images = E.decoded22_images(decoded7_images)
        raw_frame_images = S720.compose_images(
            raw_encoder_images,
            S720.compose_images(raw22_images, raw_decoder_images),
        )
        for decoded in range(F655.LOGICAL_MODES, F655.PHYSICAL_M2):
            transformed_raw = S720.apply_images(
                S720.cpauli(E.encoded_x(decoded)),
                raw_frame_images,
            )
            raw_code_constraint_frame_failures += (
                E.fields(E.as_pauli(transformed_raw))
                != E.fields(E.encoded_x(decoded))
            )

        comparisons, binary, signed = E.source_choi_failures(
            source_choi,
            E.direct_sum_images(decoded7_images, F655.LOGICAL_MODES),
        )
        source_choi_frame_comparisons += comparisons
        source_choi_frame_binary_failures += binary
        source_choi_frame_signed_failures += signed

        rotated_basis_replay_failures += sum(
            int(even[key]) for key in (
                "signed_target_replay_failures",
                "signed_physical_replay_failures",
                "signed_graph_replay_failures",
                "private_dual_syndrome_failures",
            )
        )
        comparison_basis = E.graph_basis(
            even["physical"],
            even["targets"],
            fixture.qubits,
        )
        mapped_target_rows = tuple(
            E.apply_pauli_images(row, target_images)
            for row in base_even["targets"]
        )
        mapped_target_parity = E.apply_pauli_images(
            target_parity,
            target_images,
        )
        zero_physical_images = E.corrected_action(
            base,
            fixture,
            frame,
            E.ZERO,
        )
        zero_physical_rows = tuple(
            E.apply_pauli_images(row, zero_physical_images)
            for row in base_even["physical"]
        )

        for source_seed in E.ORIGIN_SECTORS:
            frame_origin_contexts += 1
            target_seed = Q720.transported_seed(
                frame,
                E.ZERO,
                source_seed,
            )
            physical_images = E.corrected_action(
                base,
                fixture,
                frame,
                target_seed,
            )
            add_graph_counts(
                frame_graph,
                E.compare_even_graph_transport(
                    base_even,
                    target_images,
                    physical_images,
                    comparison_basis,
                    fixture.qubits,
                ),
            )
            mapped_physical_rows = tuple(
                E.apply_pauli_images(row, physical_images)
                for row in base_even["physical"]
            )
            mapped_physical_parity = E.apply_pauli_images(
                source_parity,
                physical_images,
            )
            frame_parity_comparisons += 2 * rank
            frame_parity_commutator_failures += pauli_commutator_failures(
                mapped_physical_rows,
                mapped_physical_parity,
                fixture.qubits,
            )
            frame_parity_commutator_failures += pauli_commutator_failures(
                mapped_target_rows,
                mapped_target_parity,
                fixture.matter_qubits,
            )

        frame_data.append({
            "fixture": fixture,
            "even": even,
            "target_images": target_images,
            "embedding_images": embedding_images,
            "abstract_images": abstract_images,
            "decoded7_images": decoded7_images,
            "raw_frame_images": raw_frame_images,
            "comparison_basis": comparison_basis,
            "zero_physical_rows": zero_physical_rows,
            "zero_target_rows": mapped_target_rows,
        })

    product_graph = {
        "comparisons": 0,
        "binary_failures": 0,
        "signed_failures": 0,
    }
    ordered_products = 0
    product_origin_contexts = 0
    product_parity_comparisons = 0
    product_parity_commutator_failures = 0
    source_product_image_failures = 0
    raw22_product_image_failures = 0
    source_choi_product_comparisons = 0
    source_choi_product_binary_failures = 0
    source_choi_product_signed_failures = 0
    role_embedding_product_failures = 0
    origin_seed_product_failures = 0
    corrected_physical_product_failures = 0
    even_Bell_product_comparisons = 0
    even_Bell_product_binary_failures = 0
    even_Bell_product_signed_failures = 0

    for left_id, left in enumerate(frames):
        for right_id, right in enumerate(frames):
            ordered_products += 1
            product_frame = left @ right
            product_id = frame_index[E.frame_key(product_frame)]
            left_data = frame_data[left_id]
            middle_data = frame_data[right_id]
            final_data = frame_data[product_id]
            middle = middle_data["fixture"]
            final = final_data["fixture"]

            composed_source = S720.compose_images(
                left_data["decoded7_images"],
                middle_data["decoded7_images"],
            )
            source_product_image_failures += not Q720.images_equal(
                composed_source,
                final_data["decoded7_images"],
            )
            raw22_product_image_failures += not Q720.images_equal(
                S720.compose_images(
                    left_data["raw_frame_images"],
                    middle_data["raw_frame_images"],
                ),
                final_data["raw_frame_images"],
            )
            comparisons, binary, signed = E.source_choi_failures(
                source_choi,
                E.direct_sum_images(
                    composed_source,
                    F655.LOGICAL_MODES,
                ),
            )
            source_choi_product_comparisons += comparisons
            source_choi_product_binary_failures += binary
            source_choi_product_signed_failures += signed

            left_target_images = Q720.matter_images(
                middle,
                final,
                left,
                E.ZERO,
            )
            bridge_left = S720.compose_images(
                left_target_images,
                middle_data["embedding_images"],
            )
            bridge_right = S720.compose_images(
                final_data["embedding_images"],
                left_data["abstract_images"],
            )
            role_embedding_product_failures += not Q720.images_equal(
                bridge_left,
                bridge_right,
            )

            left_zero_physical = E.corrected_action(
                middle,
                final,
                left,
                E.ZERO,
            )
            for row_id in range(rank):
                transported_physical = E.apply_pauli_images(
                    middle_data["zero_physical_rows"][row_id],
                    left_zero_physical,
                )
                transported_transpose_target = E.apply_pauli_images(
                    E.transpose(middle_data["zero_target_rows"][row_id]),
                    left_target_images,
                )
                transported_bell = E.multiply(
                    E.shift(transported_physical, 0),
                    E.shift(transported_transpose_target, final.qubits),
                )
                direct_bell = E.multiply(
                    E.shift(final_data["zero_physical_rows"][row_id], 0),
                    E.shift(
                        E.transpose(final_data["zero_target_rows"][row_id]),
                        final.qubits,
                    ),
                )
                even_Bell_product_comparisons += 1
                even_Bell_product_binary_failures += (
                    transported_bell.x,
                    transported_bell.z,
                ) != (direct_bell.x, direct_bell.z)
                even_Bell_product_signed_failures += (
                    E.fields(transported_bell) != E.fields(direct_bell)
                )

            target_product_images = final_data["target_images"]
            mapped_target_rows = tuple(
                E.apply_pauli_images(row, target_product_images)
                for row in base_even["targets"]
            )
            mapped_target_parity = E.apply_pauli_images(
                target_parity,
                target_product_images,
            )
            for source_seed in E.ORIGIN_SECTORS:
                product_origin_contexts += 1
                middle_seed = Q720.transported_seed(
                    right,
                    E.ZERO,
                    source_seed,
                )
                final_seed = Q720.transported_seed(
                    left,
                    E.ZERO,
                    middle_seed,
                )
                direct_seed = Q720.transported_seed(
                    product_frame,
                    E.ZERO,
                    source_seed,
                )
                origin_seed_product_failures += final_seed != direct_seed
                right_action = E.corrected_action(
                    base,
                    middle,
                    right,
                    middle_seed,
                )
                left_action = E.corrected_action(
                    middle,
                    final,
                    left,
                    final_seed,
                )
                composed_physical = S720.compose_images(
                    left_action,
                    right_action,
                )
                direct_physical = E.corrected_action(
                    base,
                    final,
                    product_frame,
                    direct_seed,
                )
                corrected_physical_product_failures += not Q720.images_equal(
                    composed_physical,
                    direct_physical,
                )
                add_graph_counts(
                    product_graph,
                    E.compare_even_graph_transport(
                        base_even,
                        target_product_images,
                        composed_physical,
                        final_data["comparison_basis"],
                        final.qubits,
                    ),
                )
                mapped_physical_rows = tuple(
                    E.apply_pauli_images(row, composed_physical)
                    for row in base_even["physical"]
                )
                mapped_physical_parity = E.apply_pauli_images(
                    source_parity,
                    composed_physical,
                )
                product_parity_comparisons += 2 * rank
                product_parity_commutator_failures += (
                    pauli_commutator_failures(
                        mapped_physical_rows,
                        mapped_physical_parity,
                        final.qubits,
                    )
                )
                product_parity_commutator_failures += (
                    pauli_commutator_failures(
                        mapped_target_rows,
                        mapped_target_parity,
                        final.matter_qubits,
                    )
                )

    base_replay_failures = sum(
        int(base_even[key]) for key in (
            "signed_target_replay_failures",
            "signed_physical_replay_failures",
            "signed_graph_replay_failures",
            "private_dual_syndrome_failures",
        )
    )
    forbidden_imports = tuple(
        name for name in IMPORT_MODULES
        if "scratch" in name or any(
            cycle in name for cycle in (
                "cycle804", "cycle805", "cycle812", "cycle813"
            )
        )
    )
    checks = {
        "landed_import_firewall": not forbidden_imports,
        "proper_frame_and_origin_counts": (
            len(frames) == 24
            and len(frame_index) == 24
            and len(E.ORIGIN_SECTORS) == 8
            and frame_origin_contexts == 24 * 8
            and ordered_products == 24 * 24
            and product_origin_contexts == 24 * 24 * 8
        ),
        "Cycle789_two_cell_rank23_channel_is_exact": (
            cycle789["cells"] == 2
            and cycle789["edges"] == 1
            and cycle789["character_rank"] == 23
            and cycle789["private_dual_failures"] == 0
            and cycle789["output_reference_binary_span_failures"] == 0
            and cycle789["output_reference_signed_span_failures"] == 0
            and cycle789["output_even_CAR_channel_exact"]
        ),
        "signed_even_basis_and_private_duals_replay": (
            rank == 23
            and base_replay_failures == 0
            and rotated_basis_replay_failures == 0
        ),
        "Cycle655_source_action_and_Choi_close": (
            len(source_choi) == 13
            and direction_map_failures == 0
            and raw_encoder_inverse_failures == 0
            and raw_code_constraint_frame_failures == 0
            and source_product_image_failures == 0
            and raw22_product_image_failures == 0
            and source_choi_frame_comparisons == 13 * 24
            and source_choi_product_comparisons == 13 * 24 * 24
            and source_choi_frame_binary_failures == 0
            and source_choi_frame_signed_failures == 0
            and source_choi_product_binary_failures == 0
            and source_choi_product_signed_failures == 0
        ),
        "moving_role_embedding_closes_frames_and_products": (
            role_embedding_bijection_failures == 0
            and role_embedding_signed_failures == 0
            and role_embedding_product_failures == 0
        ),
        "all_frame_origin_even_graph_rows_close": (
            frame_graph["comparisons"] == 23 * 24 * 8
            and frame_graph["binary_failures"] == 0
            and frame_graph["signed_failures"] == 0
        ),
        "all_product_origin_even_graph_rows_close": (
            product_graph["comparisons"] == 23 * 24 * 24 * 8
            and product_graph["binary_failures"] == 0
            and product_graph["signed_failures"] == 0
            and origin_seed_product_failures == 0
            and corrected_physical_product_failures == 0
        ),
        "all_13248_signed_even_Bell_products_close": (
            even_Bell_product_comparisons == 23 * 24 * 24
            and even_Bell_product_binary_failures == 0
            and even_Bell_product_signed_failures == 0
        ),
        "all_even_rows_commute_with_total_parity": (
            frame_parity_comparisons == 2 * 23 * 24 * 8
            and product_parity_comparisons == 2 * 23 * 24 * 24 * 8
            and frame_parity_commutator_failures == 0
            and product_parity_commutator_failures == 0
        ),
        "every_correction_deletion_is_detected": (
            hostile["baseline_binary_failures"] == 0
            and hostile["baseline_signed_failures"] == 0
            and hostile["correction_deletions_tested"] == 23
            and hostile["correction_deletions_detected"] == 23
            and hostile["minimum_correction_deletion_failures"] > 0
        ),
        "every_Bell_sign_mutation_is_detected": (
            hostile["Bell_ancilla_sign_mutations_tested"] == 23
            and hostile["Bell_ancilla_sign_mutations_detected"] == 23
            and hostile["minimum_Bell_ancilla_sign_mutation_failures"] > 0
        ),
    }

    script_dir = Path(__file__).resolve().parent
    input_hashes = {
        path: file_sha256(script_dir.parent / path)
        for path in AUDIT_INPUT_PATHS
    }
    report = {
        "status": "PASS" if all(checks.values()) else "FAIL",
        "authority": "none",
        "audit": "unset",
        "artifact": Path(__file__).name,
        "claim_scope": (
            "fixed two-cell shape, supplied proper-cubic frames, retained "
            "origin blocks, and parity-even observable algebra only"
        ),
        "counts": {
            "proper_frames": len(frames),
            "origin_sectors": len(E.ORIGIN_SECTORS),
            "frame_origin_contexts": frame_origin_contexts,
            "ordered_frame_products": ordered_products,
            "product_origin_contexts": product_origin_contexts,
            "even_rows": rank,
            "source_Choi_rows": len(source_choi),
            "frame_origin_graph_comparisons": frame_graph["comparisons"],
            "product_origin_graph_comparisons": product_graph["comparisons"],
            "signed_even_Bell_product_comparisons": even_Bell_product_comparisons,
            "parity_commutator_comparisons": (
                frame_parity_comparisons + product_parity_comparisons
            ),
        },
        "failures": {
            "frame_origin_graph_binary": frame_graph["binary_failures"],
            "frame_origin_graph_signed": frame_graph["signed_failures"],
            "product_origin_graph_binary": product_graph["binary_failures"],
            "product_origin_graph_signed": product_graph["signed_failures"],
            "signed_even_Bell_product_binary": even_Bell_product_binary_failures,
            "signed_even_Bell_product_signed": even_Bell_product_signed_failures,
            "parity_commutators": (
                frame_parity_commutator_failures
                + product_parity_commutator_failures
            ),
            "role_embedding_frame": role_embedding_signed_failures,
            "role_embedding_product": role_embedding_product_failures,
            "origin_seed_products": origin_seed_product_failures,
            "corrected_physical_products": corrected_physical_product_failures,
        },
        "Cycle789_two_cell_certificate": cycle789,
        "hostile_controls": hostile,
        "forbidden_imports": forbidden_imports,
        "checks": checks,
        "boundary": {
            "parity_superselection": (
                "the certificate acts on the 23-row even algebra and is "
                "independent of a chosen total-parity value"
            ),
            "not_claimed": (
                "coherent cross-parity transport, an odd Bell row or cocycle, "
                "a runtime frame controller, bare-input genesis, or a literal "
                "prefix-plus-recurrent-G executor"
            ),
        },
        "input_sha256": input_hashes,
        "claim_verdict": (
            "BOUNDED_PARITY_SUPERSELECTED_EVEN_CAR_PASS"
            if all(checks.values())
            else "BOUNDED_CERTIFICATE_FAILED"
        ),
    }
    print(json.dumps(report, indent=2, sort_keys=True, default=list))
    if not all(checks.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
