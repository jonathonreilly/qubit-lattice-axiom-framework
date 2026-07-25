#!/usr/bin/env python3
"""Integrate the sparse qutrit edge gauge with Route C's 12-cell update.

The runner constructs one explicit qutrit-augmented Cycle-311 branch encoding
for the complete two-overlapping-star vacuum/one/two basis.  It then tests the
earliest physical stage of Route C's free/seam/contact word: the landed local
Cycle-311 coin with the factor-feature copies left unchanged.  That bounded
unitary leaks from the common code, so later seam/contact stages are not
presented as an end-to-end physical update.

The failure is route-specific.  The runner makes no minimum, impossibility,
shared-obstruction, or axiom-pressure claim.
"""

from __future__ import annotations

from collections import defaultdict
from hashlib import sha256
from itertools import product
import json
import resource
import time

import numpy as np
from scipy import sparse

import physical_cycle269_common_m64_fixed_seam_cycle311_2026_07_18 as c311
import physical_cycle269_overlap_aware_two_cell_cycle315_2026_07_18 as c315
import frontier_two_overlapping_star_sparse_qutrit_edge_gauge_core_2026_07_25 as qcore
import frontier_two_star_staggered_endpoint_feature_route_c_2026_07_25 as route_c


START = time.perf_counter()
TOL = 4.0e-10
PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label} :: {detail}")
    else:
        FAIL += 1
        print(f"FAIL {label} :: {detail}")


def periodic_body(cell, length: int):
    return tuple(value % length for value in cell)


def feature_block_inventory():
    rows = []
    by_cell_mode = defaultdict(list)
    for star, center in enumerate((route_c.ORIGIN, route_c.BASE_AXIS)):
        for direction in route_c.DIRECTIONS:
            arm = route_c.add(center, direction)
            center_mode = route_c.DIRECTION_INDEX[direction]
            arm_mode = route_c.DIRECTION_INDEX[tuple(-value for value in direction)]
            for endpoint, (cell, mode) in enumerate(
                ((center, center_mode), (arm, arm_mode))
            ):
                block = len(rows)
                rows.append((star, direction, endpoint, cell, mode))
                by_cell_mode[(cell, mode)].append(block)
    duplicate_rows = {
        key: tuple(value) for key, value in by_cell_mode.items() if len(value) > 1
    }
    return tuple(rows), dict(by_cell_mode), duplicate_rows


FEATURE_BLOCKS, BLOCKS_BY_CELL_MODE, DUPLICATE_ROWS = feature_block_inventory()


def factor_terms(code, length: int, cell, number: int, label: tuple[int, ...], base: int):
    body = periodic_body(cell, length)
    rows = []
    for branch in c311.common_branches(code, body, number, label, 0):
        representative = c311.branch_representative(code, body, branch, 0)
        x_word = representative.x
        for mode in range(6):
            copy_blocks = BLOCKS_BY_CELL_MODE.get((cell, mode), ())
            if not copy_blocks:
                continue
            vertex = c311.c305.body_vertices(code, body)[mode]
            _arrival, outer_edge = c311.local.old.outer_partner(code, vertex)
            outer = (representative.x >> outer_edge) & 1
            tag = (representative.x >> (code.qubits + vertex)) & 1
            qcore.qutrit_word(outer, tag)
            for block in copy_blocks:
                x_word |= tag << (base + 2 * block)
                x_word |= outer << (base + 2 * block + 1)
        rows.append(
            (
                c315.c235.Pauli(
                    representative.phase, x_word, representative.z
                ),
                branch.amplitude,
            )
        )
    return tuple(rows)


def copy_words_from_aux(auxiliary: int, offset: int):
    return tuple(
        (auxiliary >> (offset + 2 * block)) & 0b11
        for block in range(len(FEATURE_BLOCKS))
    )


def full_patch_encoding(length: int):
    code = c315.c269.build_code(length)
    base = code.qubits + len(code.graph.vertices) + 2 * length**3
    offset = base - code.qubits
    cache = {}
    reducer = c315.RayReducer(code)
    row_indices = []
    column_indices = []
    data = []
    maximum_column_branches = 0

    for column, label in enumerate(route_c.FOCK_BASIS):
        occupied_by_cell = defaultdict(list)
        for mode in label:
            cell_index, direction = divmod(mode, 6)
            occupied_by_cell[cell_index].append(direction)
        local_rows = []
        for cell_index, cell in enumerate(route_c.BASE_CELLS):
            local_label = tuple(occupied_by_cell.get(cell_index, ()))
            local_rows.append(
                cache.setdefault(
                    (cell_index, local_label),
                    factor_terms(
                        code,
                        length,
                        cell,
                        len(local_label),
                        local_label,
                        base,
                    ),
                )
            )
        amplitudes = defaultdict(complex)
        branch_count = 0
        for factors in product(*local_rows):
            representative, amplitude = factors[0]
            for target, coefficient in factors[1:]:
                representative = representative @ target
                amplitude *= coefficient
            row, phase = reducer.reduce(representative)
            amplitudes[row] += amplitude * phase
            branch_count += 1
        maximum_column_branches = max(maximum_column_branches, branch_count)
        for row, amplitude in amplitudes.items():
            if abs(amplitude) > 2e-13:
                row_indices.append(row)
                column_indices.append(column)
                data.append(amplitude)

    encoding = sparse.coo_matrix(
        (data, (row_indices, column_indices)),
        shape=(len(reducer.row_by_aux), len(route_c.FOCK_BASIS)),
        dtype=complex,
    ).tocsc()
    identity = sparse.eye(len(route_c.FOCK_BASIS), format="csc")
    gram_difference = encoding.conj().T @ encoding - identity
    invalid_words = equality_failures = 0
    for auxiliary in reducer.row_by_aux:
        words = copy_words_from_aux(auxiliary, offset)
        invalid_words += sum(word not in qcore.LAWFUL_QUTRIT_WORDS for word in words)
        for blocks in DUPLICATE_ROWS.values():
            equality_failures += words[blocks[0]] != words[blocks[1]]
    details = {
        "L": length,
        "split": "train" if length == 5 else "held-no-refit",
        "logical_columns_n_le_2": len(route_c.FOCK_BASIS),
        "physical_branch_rays": encoding.shape[0],
        "encoding_nonzeros": encoding.nnz,
        "maximum_branches_per_column": maximum_column_branches,
        "feature_qutrit_blocks": len(FEATURE_BLOCKS),
        "feature_copy_M2": 2 * len(FEATURE_BLOCKS),
        "shared_physical_half_edges_with_two_star_views": len(DUPLICATE_ROWS),
        "invalid_qutrit_words": invalid_words,
        "shared_copy_equality_failures": equality_failures,
        "Gram_residual": c315.largest_singular(gram_difference),
        "Gram_raw_maximum": c315.raw_maximum_abs(gram_difference),
        "zero_columns": sum(encoding.getcol(column).nnz == 0 for column in range(encoding.shape[1])),
    }
    return details, encoding


def local_frozen_copy_coin(length: int, body, duplicate_mode: int | None):
    """First physical intertwiner attempt on one embedded patch cell."""
    code = c315.c269.build_code(length)
    specs = tuple(spec for spec in c311.FOCK_LABELS if spec[0] <= 2)
    branches = []
    rows_by_column = []
    for number, label in specs:
        rows = c311.common_branches(code, body, number, label, 0)
        rows_by_column.append(tuple(range(len(branches), len(branches) + len(rows))))
        branches.extend(rows)

    local_encoding = np.zeros((len(branches), len(specs)), dtype=complex)
    signatures = []
    modes = tuple(range(6)) + (() if duplicate_mode is None else (duplicate_mode,))
    for column, rows in enumerate(rows_by_column):
        for row in rows:
            local_encoding[row, column] = branches[row].amplitude
    for branch in branches:
        representative = c311.branch_representative(code, body, branch, 0)
        signature = []
        for mode in modes:
            vertex = c311.c305.body_vertices(code, body)[mode]
            _arrival, outer_edge = c311.local.old.outer_partner(code, vertex)
            outer = (representative.x >> outer_edge) & 1
            tag = (representative.x >> (code.qubits + vertex)) & 1
            signature.append(qcore.qutrit_word(outer, tag))
        signatures.append(tuple(signature))

    signature_rows = tuple(sorted(set(signatures)))
    signature_index = {signature: index for index, signature in enumerate(signature_rows)}
    logical_coin = np.zeros((len(specs), len(specs)), dtype=complex)
    coin = c311.c219.common_species(-0.3).coin
    for number in range(3):
        indices = [index for index, spec in enumerate(specs) if spec[0] == number]
        logical_coin[np.ix_(indices, indices)] = c311.exterior_matrix(coin, number)

    projector = local_encoding @ local_encoding.conj().T
    physical_coin = (
        local_encoding @ logical_coin @ local_encoding.conj().T
        + np.eye(len(branches))
        - projector
    )
    ambient_dimension = len(branches) * len(signature_rows)
    row_indices = []
    column_indices = []
    data = []
    for column, rows in enumerate(rows_by_column):
        for row in rows:
            row_indices.append(
                signature_index[signatures[row]] * len(branches) + row
            )
            column_indices.append(column)
            data.append(branches[row].amplitude)
    augmented_encoding = sparse.coo_matrix(
        (data, (row_indices, column_indices)),
        shape=(ambient_dimension, len(specs)),
        dtype=complex,
    ).tocsc()
    frozen_coin = sparse.block_diag(
        tuple(physical_coin for _signature in signature_rows), format="csc"
    )
    difference = frozen_coin @ augmented_encoding - augmented_encoding @ sparse.csc_matrix(
        logical_coin
    )
    code_projector = augmented_encoding @ augmented_encoding.conj().T
    leakage = (
        sparse.eye(ambient_dimension, format="csc") - code_projector
    ) @ frozen_coin @ augmented_encoding
    return {
        "L": length,
        "cell_class": "shared_center" if duplicate_mode is not None else "outer_arm",
        "local_logical_columns_n_le_2": len(specs),
        "local_branch_microsectors": len(branches),
        "distinct_feature_signatures": len(signature_rows),
        "augmented_ambient_dimension": ambient_dimension,
        "local_encoding_Gram_residual": float(
            np.linalg.norm(
                local_encoding.conj().T @ local_encoding - np.eye(len(specs))
            )
        ),
        "bounded_physical_coin_unitarity_residual": float(
            np.linalg.norm(
                physical_coin.conj().T @ physical_coin - np.eye(len(branches))
            )
        ),
        "first_coin_intertwiner_residual": c315.largest_singular(difference),
        "first_coin_intertwiner_raw_maximum": c315.raw_maximum_abs(difference),
        "first_coin_code_leakage": c315.largest_singular(leakage),
        "first_coin_code_leakage_raw_maximum": c315.raw_maximum_abs(leakage),
        "feature_copies_updated_by_candidate": False,
    }


def main() -> None:
    check(
        "the integration has exactly 24 star-private qutrit blocks and two shared-view equalities",
        len(FEATURE_BLOCKS) == 24
        and len(DUPLICATE_ROWS) == 2
        and sorted(map(len, DUPLICATE_ROWS.values())) == [2, 2],
        {
            "feature_qutrit_blocks": len(FEATURE_BLOCKS),
            "feature_copy_M2": 2 * len(FEATURE_BLOCKS),
            "duplicate_shared_half_edges": DUPLICATE_ROWS,
        },
    )

    encoding_rows = []
    for length in (5, 6):
        details, _encoding = full_patch_encoding(length)
        encoding_rows.append(details)
    check(
        "one common qutrit-augmented physical E is an exact 2629-column isometry at L5 and held L6",
        all(
            row["logical_columns_n_le_2"] == 2629
            and row["physical_branch_rays"] == 59941
            and row["encoding_nonzeros"] == 59941
            and row["maximum_branches_per_column"] == 25
            and row["invalid_qutrit_words"] == 0
            and row["shared_copy_equality_failures"] == 0
            and row["Gram_residual"] < TOL
            and row["Gram_raw_maximum"] < TOL
            and row["zero_columns"] == 0
            for row in encoding_rows
        ),
        encoding_rows,
    )

    update_rows, logical_update = route_c.build_patch_update(route_c.BASE_AXIS)
    check(
        "Route C's actual 12-cell free/11-seam/contact update and deletion fixtures execute unchanged",
        update_rows["cells"] == 12
        and update_rows["unique_star_edges"] == 11
        and update_rows["shared_edge_occurrences"] == 1
        and update_rows["logical_columns_n_le_2"] == 2629
        and update_rows["contact_nontrivial_columns"] == 180
        and max(
            update_rows["coin_unitarity_raw_maximum"],
            update_rows["stream_unitarity_raw_maximum"],
            update_rows["contact_unitarity_raw_maximum"],
            update_rows["update_unitarity_raw_maximum"],
            update_rows["two_particle_update_unitarity_raw_maximum"],
            update_rows["one_particle_mass_residual"],
            update_rows["uniform_one_particle_eigen_residual"],
        )
        < TOL
        and update_rows["delete_shared_seam_update_residual"] > 1
        and update_rows["duplicate_shared_seam_update_residual"] > 1
        and update_rows["delete_contact_update_residual"] > 0.3,
        update_rows,
    )

    schedule = route_c.shared_edge_and_schedule_inventory()
    module = route_c.qutrit_module_controls()
    check(
        "the fixed feature schedule owns the common edge once and returns all declared work",
        schedule["unique_union_edges"] == 11
        and schedule["shared_edge_program_owners"] == 1
        and schedule["runtime_parity_queries"] == 0
        and schedule["runtime_order_queries"] == 0
        and schedule["runtime_measurements"] == 0
        and module["lawful_failures"] == 0
        and module["work_return_failures"] == 0
        and module["coherent_intertwiner_residual"] < TOL,
        {"schedule": schedule, "module": module},
    )

    symmetry = route_c.frame_and_translation_controls(logical_update)
    check(
        "the supplied logical update and feature schedule retain all 24 frames, 576 products, L5 and L6 placements",
        symmetry["proper_cubic_frames"] == 24
        and symmetry["ordered_frame_products"] == 576
        and symmetry["maximum_update_covariance_residual"] < TOL
        and symmetry["maximum_update_covariance_raw_maximum"] < TOL
        and symmetry["program_edge_frame_failures"] == 0
        and symmetry["qutrit_endpoint_reversal_failures"] == 0
        and symmetry["frame_group_mapping_failures"] == 0
        and symmetry["frame_group_phase_failures"] == 0
        and symmetry["program_edge_product_failures"] == 0
        and all(row["failures"] == 0 for row in symmetry["translation_rows"])
        and symmetry["held_parameters_refit"] == 0,
        symmetry,
    )

    first_failures = []
    for length in (5, 6):
        first_failures.append(
            local_frozen_copy_coin(length, (1, 1, 1), duplicate_mode=0)
        )
        first_failures.append(
            local_frozen_copy_coin(length, (0, 1, 1), duplicate_mode=None)
        )
    check(
        "the first bounded physical-coin attempt is unitary but fails the same-E intertwiner by stale qutrit copies",
        all(
            row["local_encoding_Gram_residual"] < TOL
            and row["bounded_physical_coin_unitarity_residual"] < TOL
            and row["first_coin_intertwiner_residual"] > 1.9
            and row["first_coin_intertwiner_raw_maximum"] > 0.34
            and row["first_coin_code_leakage"] > 0.99
            and row["first_coin_code_leakage_raw_maximum"] > 0.34
            and not row["feature_copies_updated_by_candidate"]
            for row in first_failures
        ),
        {
            "equation_attempted": "E C_patch = K_physical,frozen-copy E",
            "rows": first_failures,
            "first_failed_stage": "the first local free coin, before any seam or contact gate",
            "reason": (
                "the landed Cycle-311 coin changes branch endpoint features while Route C's "
                "feature word consumes supplied qutrits but does not derive/recompute them"
            ),
        },
    )

    domain = route_c.unlawful_domain_controls()
    projector = qcore.four_copy_projectors()
    check(
        "shared-copy deletion, dirty-work and unlawful-domain controls remain active",
        projector["joint_equality_rank"] == 9
        and projector["delete_one_equality_rank"] == 27
        and domain["invalid_qutrit_rejections"] == domain["invalid_qutrit_rows"] == 4
        and domain["invalid_fock_rejections"] == domain["invalid_fock_rows"] == 4
        and domain["dirty_work_genesis_nonreturn"] == 1
        and module["deleted_phase_gate_failures"] > 0,
        {"projector": projector, "domain": domain},
    )

    certificate = {
        "feature_blocks": FEATURE_BLOCKS,
        "encoding_rows": encoding_rows,
        "update_rows": update_rows,
        "first_failures": first_failures,
        "symmetry": symmetry,
    }
    digest = sha256(
        json.dumps(certificate, sort_keys=True, separators=(",", ":"), default=str).encode()
    ).hexdigest()
    result = {
        "authority": "none",
        "audit": "unset",
        "status": "two-star-qutrit-physical-update-integration-attempt",
        "terminal": "COMMON_PHYSICAL_E_CLOSED_FIRST_COIN_INTERTWINER_OPEN",
        "pass": FAIL == 0,
        "tests_passed": PASS,
        "tests_failed": FAIL,
        "route_disposition": (
            "constructive common physical encoding E; integration remains open because the first "
            "bounded free-coin candidate leaves the factor-feature copies stale and leaks from E"
        ),
        "encoding": encoding_rows,
        "logical_update": update_rows,
        "first_failed_intertwiner": first_failures,
        "symmetry": symmetry,
        "resources": {
            "coarse_cells": 12,
            "coarse_modes": 72,
            "logical_columns_n_le_2": 2629,
            "physical_branch_rays": 59941,
            "feature_qutrit_blocks": 24,
            "feature_copy_M2": 48,
            "shared_copy_projector_support_M2": 4,
            "global_ordering_M2": 0,
            "Jordan_Wigner_string_M2": 0,
            "host_queries": 0,
            "elapsed_seconds": time.perf_counter() - START,
            "peak_rss_mb": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
            / (1024 * 1024),
        },
        "supplied": (
            "the landed Cycle-311 stream-zero branch representatives and local physical coin completion",
            "Route C's 12-cell/72-mode/n<=2 basis and actual free/11-seam/contact logical update",
            "Route C's fixed eleven-owner feature schedule, 24-frame family and 576 exterior products",
            "the Route-B factor-contribution qutrit chart, two shared-view equality projectors and local sign circuit",
            "one bounded sorted patch chart, L5 training size, held L6 size and tolerance",
        ),
        "derived": (
            "one explicit 2629-column qutrit-augmented physical encoding with 59941 rays/nonzeros and zero Gram residual at L5 and held L6",
            "zero invalid qutrit words and zero shared-copy equality violations on the full physical branch-ray encoding",
            "unchanged Route-C mass, seam/contact deletions, 24-frame and 576-product logical-update fixtures",
            "an exact first-stage residual: intertwiner 1.925139450722642, raw 0.34045188744302635, leakage 0.9951085423852697",
            "stability of that first failure across L5/L6 and both shared-center and outer-arm cell classes",
        ),
        "open": (
            "a sparse physical extractor/recomputer that updates each qutrit copy coherently when the local coin changes branch features",
            "a fixed bounded physical free/seam/contact word satisfying E G_logical = G_physical E for this same E",
            "proper-cubic covariance of the physical encoding itself after the first coin issue is repaired",
            "primitive dynamical enforcement/preparation of the branch-ray copy projectors",
            "n>2, full M64^12, recurrent overlap, collision control, state genesis and volume scaling",
            "minimality, impossibility, shared obstruction, axiom pressure, time, source, Record and probability",
        ),
        "claim_ceiling": (
            "Positive full-patch physical encoding and exact route-specific first-failure diagnostic.  "
            "The logical update and feature circuit remain separate because no supplied sparse operation "
            "recomputes the factor qutrits under the coin.  This is not evidence for a shared obstruction."
        ),
        "certificate_sha256": digest,
    }
    print("SUMMARY_JSON", json.dumps(result, sort_keys=True))
    print("RESULT", result["terminal"] if result["pass"] else "UNFINISHED_IMPLEMENTATION")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
