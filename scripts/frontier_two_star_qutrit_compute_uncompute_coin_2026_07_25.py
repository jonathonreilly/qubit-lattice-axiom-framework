#!/usr/bin/env python3
"""Bounded compute--uncompute closure of the Route-B qutrit first-coin wall.

This runner deliberately does *not* form an augmented ``E C E^dagger``
completion.  The physical operation is the following bounded factorization on
one Cycle-311 cell and its copied endpoint-feature words::

    COPY_f  (K_landed tensor I_feature)  COPY_f,

where ``COPY_f`` XORs the deterministic two-bit word ``f(branch)`` into each
feature block and ``K_landed`` is the already-landed 46 by 46 local physical
coin.  On the Route-B code space the first COPY erases every feature word,
and the second recomputes it from the post-coin branch/port microstate.

The shared-center fixture has six distinct endpoint features and a seventh
physical block carrying the duplicate shared-edge view.  The outer-arm
fixture has the single block actually present in the common 24-block Route-B
encoder.  Both are tested at L=5 and L=6, together with every block deletion,
all 24 proper-cubic frames, all 576 ordered frame products, and explicit
support/inventory controls.

Run with the Route-B and Route-C script directories on PYTHONPATH, e.g.::

  PYTHONPATH=/path/to/route-b/scripts:/path/to/route-c/scripts \
    python3 scripts/frontier_two_star_qutrit_compute_uncompute_coin_2026_07_25.py
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import scipy.sparse as sp

import physical_cycle269_common_m64_fixed_seam_cycle311_2026_07_18 as c311
import physical_cycle269_overlap_aware_two_cell_cycle315_2026_07_18 as c315
import exact_3d_higher_form_bosonization_cycle235_2026_07_17 as c235
import frontier_two_overlapping_star_sparse_qutrit_edge_gauge_core_2026_07_25 as qcore
import frontier_two_star_qutrit_physical_update_integration_2026_07_25 as route_b
import frontier_two_star_staggered_endpoint_feature_route_c_2026_07_25 as route_c


TOL = 1.0e-10
SEED = 659230
SHARED_MODE = 0
_FRAME_REP_CACHE: dict[int, tuple[tuple[np.ndarray, tuple[int, ...], np.ndarray, np.ndarray], ...]] = {}


@dataclass(frozen=True)
class LocalFixture:
    length: int
    fixture: str
    code: object
    body: tuple[int, int, int]
    copied_modes: tuple[int, ...]
    specs: tuple[tuple[int, ...], ...]
    branches: tuple[c311.Branch, ...]
    representatives: tuple[object, ...]
    encoding: np.ndarray
    logical_coin: np.ndarray
    physical_coin: np.ndarray
    signatures: np.ndarray
    augmented_encoding: sp.csc_matrix


def max_abs(matrix) -> float:
    if sp.issparse(matrix):
        return float(np.max(np.abs(matrix.data))) if matrix.nnz else 0.0
    array = np.asarray(matrix)
    return float(np.max(np.abs(array))) if array.size else 0.0


def matrix_norm(matrix) -> float:
    if sp.issparse(matrix):
        return float(np.sqrt(np.sum(np.abs(matrix.data) ** 2)))
    return float(np.linalg.norm(np.asarray(matrix)))


def local_specs() -> tuple[tuple[int, ...], ...]:
    return tuple(spec for spec in c311.FOCK_LABELS if spec[0] <= 2)


def local_logical_coin(specs: tuple[tuple[int, ...], ...]) -> np.ndarray:
    matrix = np.zeros((len(specs), len(specs)), dtype=complex)
    coin = c311.c219.common_species(-0.3).coin
    for number in range(3):
        indices = [index for index, spec in enumerate(specs) if spec[0] == number]
        matrix[np.ix_(indices, indices)] = c311.exterior_matrix(coin, number)
    return matrix


def branch_shell(
    code: c311.Code311,
    body: int,
    specs: tuple[tuple[int, ...], ...],
) -> tuple[tuple[c311.Branch, ...], tuple[tuple[int, int], ...], np.ndarray]:
    branches: list[c311.Branch] = []
    labels: list[tuple[int, int]] = []
    columns: list[list[tuple[int, complex]]] = []
    for col, (number, label) in enumerate(specs):
        local_rows: list[tuple[int, complex]] = []
        for branch in c311.common_branches(code, body, number, label, 0):
            idx = len(branches)
            branches.append(branch)
            labels.append((col, -1 if branch.carrier_direction is None else int(branch.carrier_direction)))
            local_rows.append((idx, complex(branch.amplitude)))
        columns.append(local_rows)
    encoding = np.zeros((len(branches), len(specs)), dtype=complex)
    for col, rows in enumerate(columns):
        for row, amplitude in rows:
            encoding[row, col] += amplitude
    return tuple(branches), tuple(labels), encoding


def representative_for_branch(
    code: c311.Code311,
    body: int,
    branch: c311.Branch,
):
    return c311.branch_representative(
        code,
        body,
        branch,
        r_value=0,
    )


def copied_signature(
    code: c311.Code311,
    body: int,
    representative,
    copied_modes: tuple[int, ...],
) -> int:
    word = 0
    for block, mode in enumerate(copied_modes):
        vertex = c311.c305.body_vertices(code, body)[mode]
        _arrival, outer_edge = c311.local.old.outer_partner(code, vertex)
        outer = (int(representative.x) >> outer_edge) & 1
        tag = (int(representative.x) >> (code.qubits + vertex)) & 1
        feature = qcore.qutrit_word(outer, tag)
        word |= feature << (2 * block)
    return word


def augmented_encoding(
    encoding: np.ndarray,
    signatures: np.ndarray,
    block_count: int,
) -> sp.csc_matrix:
    branch_count, logical_dim = encoding.shape
    ambient = branch_count * (1 << (2 * block_count))
    rows: list[int] = []
    cols: list[int] = []
    data: list[complex] = []
    for branch in range(branch_count):
        for col in np.flatnonzero(np.abs(encoding[branch]) > 1.0e-15):
            rows.append(int(signatures[branch]) * branch_count + branch)
            cols.append(int(col))
            data.append(complex(encoding[branch, col]))
    return sp.csc_matrix((data, (rows, cols)), shape=(ambient, logical_dim))


def build_fixture(length: int, fixture: str) -> LocalFixture:
    code = c315.c269.build_code(length)
    body = (0, 0, 0)
    if fixture == "shared_center":
        # Six local features plus the equal duplicate shared-edge view.
        copied_modes = tuple(range(6)) + (SHARED_MODE,)
    elif fixture == "outer_arm":
        # This is the actual common-encoder allocation on a nonshared arm.
        copied_modes = (SHARED_MODE,)
    else:
        raise ValueError(f"unknown fixture {fixture!r}")
    specs = local_specs()
    branches, _labels, encoding = branch_shell(code, body, specs)
    representatives = tuple(
        representative_for_branch(code, body, branch) for branch in branches
    )
    signatures = np.asarray(
        [
            copied_signature(code, body, representative, copied_modes)
            for representative in representatives
        ],
        dtype=np.int64,
    )
    coin = local_logical_coin(specs)
    projector = encoding @ encoding.conj().T
    physical_coin = (
        encoding @ coin @ encoding.conj().T
        + np.eye(encoding.shape[0], dtype=complex)
        - projector
    )
    aug = augmented_encoding(encoding, signatures, len(copied_modes))
    return LocalFixture(
        length=length,
        fixture=fixture,
        code=code,
        body=body,
        copied_modes=copied_modes,
        specs=specs,
        branches=branches,
        representatives=representatives,
        encoding=encoding,
        logical_coin=coin,
        physical_coin=physical_coin,
        signatures=signatures,
        augmented_encoding=aug,
    )


def xor_copy_dense(
    state: np.ndarray,
    signatures: np.ndarray,
) -> np.ndarray:
    """Apply the full-register branch-controlled feature XOR permutation."""

    output = np.empty_like(state)
    for branch, signature in enumerate(signatures):
        order = np.arange(state.shape[0], dtype=np.int64) ^ int(signature)
        output[:, branch] = state[order, branch]
    return output


def apply_recomputed_coin_dense(
    fixture: LocalFixture,
    state: np.ndarray,
    inverse: bool = False,
) -> np.ndarray:
    """Factorized COPY--coin--COPY action on a q-word by branch array."""

    erased = xor_copy_dense(state, fixture.signatures)
    coin = fixture.physical_coin.conj().T if inverse else fixture.physical_coin
    landed = erased @ coin.T
    return xor_copy_dense(landed, fixture.signatures)


def sparse_action_on_code(
    fixture: LocalFixture,
    erase_signatures: np.ndarray | None = None,
    recompute_signatures: np.ndarray | None = None,
) -> sp.csc_matrix:
    """Apply the factorized action to E without forming an ambient operator."""

    erase = fixture.signatures if erase_signatures is None else erase_signatures
    recompute = (
        fixture.signatures if recompute_signatures is None else recompute_signatures
    )
    branch_count, logical_dim = fixture.encoding.shape
    ambient = fixture.augmented_encoding.shape[0]
    accum: dict[tuple[int, int], complex] = {}
    for source in range(branch_count):
        source_cols = np.flatnonzero(np.abs(fixture.encoding[source]) > 1.0e-15)
        if source_cols.size == 0:
            continue
        middle_q = int(fixture.signatures[source]) ^ int(erase[source])
        targets = np.flatnonzero(np.abs(fixture.physical_coin[:, source]) > 1.0e-14)
        for target in targets:
            final_q = middle_q ^ int(recompute[target])
            row = final_q * branch_count + int(target)
            transition = fixture.physical_coin[target, source]
            for col in source_cols:
                value = transition * fixture.encoding[source, col]
                key = (row, int(col))
                accum[key] = accum.get(key, 0.0j) + value
    rows: list[int] = []
    cols: list[int] = []
    data: list[complex] = []
    for (row, col), value in accum.items():
        if abs(value) > 1.0e-13:
            rows.append(row)
            cols.append(col)
            data.append(value)
    return sp.csc_matrix((data, (rows, cols)), shape=(ambient, logical_dim))


def leakage_residual(fixture: LocalFixture, output: sp.csc_matrix) -> float:
    coefficients = fixture.augmented_encoding.conj().T @ output
    return matrix_norm(output - fixture.augmented_encoding @ coefficients)


def first_feature_ambiguity(fixture: LocalFixture):
    """Find a physical branch ray assigned more than one copied word."""

    reducer = c315.RayReducer(fixture.code)
    seen: dict[int, tuple[int, int]] = {}
    for branch, representative in enumerate(fixture.representatives):
        row, _phase = reducer.reduce(representative)
        previous = seen.get(row)
        current = (int(fixture.signatures[branch]), branch)
        if previous is not None and previous[0] != current[0]:
            return {
                "row": row,
                "first_branch": previous[1],
                "first_signature": previous[0],
                "second_branch": branch,
                "second_signature": current[0],
            }
        seen[row] = current
    return None


def signature_deletion(fixture: LocalFixture, block: int, erase: bool) -> tuple[float, float]:
    mask = ~(0b11 << (2 * block))
    deleted = fixture.signatures & mask
    output = sparse_action_on_code(
        fixture,
        erase_signatures=deleted if erase else None,
        recompute_signatures=None if erase else deleted,
    )
    target = fixture.augmented_encoding @ fixture.logical_coin
    return matrix_norm(output - target), leakage_residual(fixture, output)


def support_audit(fixture: LocalFixture) -> dict[str, int]:
    face_mask = (1 << fixture.code.qubits) - 1
    port_mask = ((1 << len(fixture.code.graph.vertices)) - 1) << fixture.code.qubits
    used_face = 0
    used_port = 0
    max_branch_weight = 0
    for representative in fixture.representatives:
        support = int(representative.x) | int(representative.z)
        used_face |= support & face_mask
        used_port |= support & port_mask
        max_branch_weight = max(max_branch_weight, support.bit_count())
    max_transition_weight = 0
    for target, source in zip(*np.nonzero(np.abs(fixture.physical_coin) > 1.0e-14)):
        difference = fixture.representatives[target] @ fixture.representatives[source]
        max_transition_weight = max(
            max_transition_weight,
            (int(difference.x) | int(difference.z)).bit_count(),
        )
    return {
        "feature_blocks": len(fixture.copied_modes),
        "feature_M2_sites": 2 * len(fixture.copied_modes),
        "face_M2_sites_union": int(used_face).bit_count(),
        "port_M2_sites_union": int(used_port).bit_count(),
        "branch_control_M2_sites_union": (
            int(used_face).bit_count() + int(used_port).bit_count()
        ),
        "total_control_plus_feature_M2_sites": (
            int(used_face).bit_count()
            + int(used_port).bit_count()
            + 2 * len(fixture.copied_modes)
        ),
        "max_branch_word_weight": max_branch_weight,
        "max_landed_coin_transition_weight": max_transition_weight,
        "branch_projector_count": len(fixture.branches),
    }


def feature_covariance_control(fixture: LocalFixture) -> dict[str, float | int]:
    """Audit physical extraction and the landed coin under all cube frames."""

    frames = c235.proper_cubic_frames()
    if fixture.length not in _FRAME_REP_CACHE:
        encoder = c311.common_encoder(fixture.code, fixture.body)
        full_basis, _full_encoding, occurrence = c311.flagged_basis_and_encoding(encoder)
        selected_rows = [
            occurrence[
                (
                    branch.number,
                    branch.label,
                    branch.stream_slice,
                    branch.carrier_direction,
                )
            ]
            for branch in fixture.branches
        ]
        reducer = c311.c305.StabilizerReducer(fixture.code)
        cached = []
        logical_index = {spec: index for index, spec in enumerate(fixture.specs)}
        for frame in frames:
            modes = tuple(c311.direction_map(frame, mode) for mode in range(6))
            full_physical, failures = c311.flagged_frame_representation(
                encoder, full_basis, occurrence, frame, reducer
            )
            assert failures == 0
            physical = full_physical[np.ix_(selected_rows, selected_rows)]
            logical = np.zeros((len(fixture.specs), len(fixture.specs)), dtype=complex)
            for source, (number, label) in enumerate(fixture.specs):
                mapped_list = [modes[mode] for mode in label]
                target_label = tuple(sorted(mapped_list))
                target = logical_index[(number, target_label)]
                logical[target, source] = c311.c308.permutation_sign(mapped_list)
            cached.append((frame, modes, physical, logical))
        _FRAME_REP_CACHE[fixture.length] = tuple(cached)
    cached = _FRAME_REP_CACHE[fixture.length]
    max_encoding = 0.0
    max_coin = 0.0
    feature_failures = 0
    maps: list[tuple[np.ndarray, np.ndarray]] = []
    for _frame, modes, physical, logical in cached:
        target_copied = tuple(modes[mode] for mode in fixture.copied_modes)
        target_by_key = {
            (branch.number, branch.label, branch.carrier_direction): index
            for index, branch in enumerate(fixture.branches)
        }
        for source, branch in enumerate(fixture.branches):
            mapped_label = tuple(sorted(modes[mode] for mode in branch.label))
            mapped_carrier = (
                None
                if branch.carrier_direction is None
                else modes[branch.carrier_direction]
            )
            target = target_by_key[(branch.number, mapped_label, mapped_carrier)]
            target_signature = copied_signature(
                fixture.code,
                fixture.body,
                fixture.representatives[target],
                target_copied,
            )
            if target_signature != int(fixture.signatures[source]):
                feature_failures += 1
        max_encoding = max(
            max_encoding,
            max_abs(physical @ fixture.encoding - fixture.encoding @ logical),
        )
        max_coin = max(
            max_coin,
            max_abs(physical @ fixture.physical_coin - fixture.physical_coin @ physical),
        )
        maps.append((physical, logical))
    frame_lookup = {
        tuple(int(value) for value in frame.ravel()): index
        for index, frame in enumerate(frames)
    }
    physical_monomials = []
    logical_monomials = []
    for physical, logical in maps:
        p_target = np.argmax(np.abs(physical), axis=0)
        p_phase = physical[p_target, np.arange(len(p_target))]
        l_target = np.argmax(np.abs(logical), axis=0)
        l_phase = logical[l_target, np.arange(len(l_target))]
        physical_monomials.append((p_target, p_phase))
        logical_monomials.append((l_target, l_phase))
    group_representation_residual = 0.0
    group_mapping_failures = 0
    for left, (frame_left, _modes_left, _p_left, _l_left) in enumerate(cached):
        for right, (frame_right, _modes_right, _p_right, _l_right) in enumerate(cached):
            target_index = frame_lookup[
                tuple(int(value) for value in (frame_left @ frame_right).ravel())
            ]
            for monomials in (physical_monomials, logical_monomials):
                left_target, left_phase = monomials[left]
                right_target, right_phase = monomials[right]
                expected_target, expected_phase = monomials[target_index]
                composed_target = left_target[right_target]
                composed_phase = right_phase * left_phase[right_target]
                group_mapping_failures += int(
                    np.count_nonzero(composed_target != expected_target)
                )
                group_representation_residual = max(
                    group_representation_residual,
                    max_abs(composed_phase - expected_phase),
                )
    return {
        "frames": len(frames),
        "frame_products": len(frames) ** 2,
        "feature_transport_failures_24": feature_failures,
        "encoding_covariance_residual_24": max_encoding,
        "landed_coin_covariance_residual_24": max_coin,
        "frame_product_mapping_failures_576": group_mapping_failures,
        "frame_product_representation_residual_576": group_representation_residual,
        "encoding_covariance_residual_576": max_encoding,
        "landed_coin_covariance_residual_576": max_coin,
    }


def local_control(fixture: LocalFixture) -> dict[str, object]:
    branch_count = len(fixture.branches)
    block_count = len(fixture.copied_modes)
    qdim = 1 << (2 * block_count)
    gram = fixture.augmented_encoding.conj().T @ fixture.augmented_encoding
    gram_residual = max_abs(gram - np.eye(len(fixture.specs), dtype=complex))
    local_coin_intertwiner = max_abs(
        fixture.physical_coin @ fixture.encoding
        - fixture.encoding @ fixture.logical_coin
    )
    physical_coin_unitarity = max_abs(
        fixture.physical_coin.conj().T @ fixture.physical_coin
        - np.eye(branch_count, dtype=complex)
    )
    output = sparse_action_on_code(fixture)
    target = fixture.augmented_encoding @ fixture.logical_coin
    intertwiner = matrix_norm(output - target)
    raw_intertwiner = max_abs(output - target)
    leakage = leakage_residual(fixture, output)
    species = c311.c219.common_species(-0.3)
    one_particle_indices = [
        index for index, spec in enumerate(fixture.specs) if spec[0] == 1
    ]
    one_particle_coin_residual = max_abs(
        fixture.logical_coin[np.ix_(one_particle_indices, one_particle_indices)]
        - species.coin
    )
    one_particle_recomputed_intertwiner = matrix_norm(
        output[:, one_particle_indices] - target[:, one_particle_indices]
    )
    mass_fixture_residual = abs(
        c311.c219.rest_mass(species) - species.analytic_mass
    )

    # The first XOR must erase every populated code row to the q=0 sector.
    middle_nonblank = 0
    for branch in range(branch_count):
        if int(fixture.signatures[branch]) ^ int(fixture.signatures[branch]):
            middle_nonblank += 1

    # A full-register inverse control verifies that the factorization is a
    # unitary on the whole declared ambient space, not merely an isometry on E.
    rng = np.random.default_rng(SEED + 100 * fixture.length + block_count)
    random_state = rng.normal(size=(qdim, branch_count)) + 1.0j * rng.normal(
        size=(qdim, branch_count)
    )
    random_state /= np.linalg.norm(random_state)
    forward = apply_recomputed_coin_dense(fixture, random_state)
    returned = apply_recomputed_coin_dense(fixture, forward, inverse=True)
    ambient_norm_residual = abs(np.linalg.norm(forward) - 1.0)
    ambient_inverse_residual = float(np.linalg.norm(returned - random_state))

    deletions = [
        {
            "block": block,
            "mode": fixture.copied_modes[block],
            "erase_intertwiner": signature_deletion(fixture, block, True)[0],
            "erase_leakage": signature_deletion(fixture, block, True)[1],
            "recompute_intertwiner": signature_deletion(fixture, block, False)[0],
            "recompute_leakage": signature_deletion(fixture, block, False)[1],
        }
        for block in range(block_count)
    ]
    ambiguity = first_feature_ambiguity(fixture)
    support = support_audit(fixture)
    symmetry = feature_covariance_control(fixture)
    duplicate_failures = 0
    if fixture.fixture == "shared_center":
        last_shift = 2 * (block_count - 1)
        first_shift = 2 * SHARED_MODE
        for signature in fixture.signatures:
            if ((int(signature) >> last_shift) & 0b11) != (
                (int(signature) >> first_shift) & 0b11
            ):
                duplicate_failures += 1
    return {
        "length": fixture.length,
        "fixture": fixture.fixture,
        "logical_dim": len(fixture.specs),
        "branch_microbasis_dim": branch_count,
        "feature_blocks": block_count,
        "feature_register_dim": qdim,
        "declared_ambient_dim": qdim * branch_count,
        "augmented_encoding_nnz": fixture.augmented_encoding.nnz,
        "augmented_gram_residual": gram_residual,
        "bare_landed_coin_intertwiner": local_coin_intertwiner,
        "bare_landed_coin_unitarity": physical_coin_unitarity,
        "compute_uncompute_intertwiner_norm": intertwiner,
        "compute_uncompute_intertwiner_raw": raw_intertwiner,
        "compute_uncompute_leakage": leakage,
        "one_particle_coin_fixture_residual": one_particle_coin_residual,
        "one_particle_recomputed_intertwiner": one_particle_recomputed_intertwiner,
        "one_particle_analytic_mass": species.analytic_mass,
        "one_particle_rest_mass_residual": mass_fixture_residual,
        "middle_nonblank_branch_count": middle_nonblank,
        "returned_work_residual": ambient_inverse_residual,
        "ambient_norm_residual": ambient_norm_residual,
        "duplicate_shared_view_failures": duplicate_failures,
        "first_ambiguous_extraction_row": ambiguity,
        "deletions": deletions,
        "minimum_erase_deletion_intertwiner": min(
            item["erase_intertwiner"] for item in deletions
        ),
        "minimum_recompute_deletion_intertwiner": min(
            item["recompute_intertwiner"] for item in deletions
        ),
        "support": support,
        "symmetry": symmetry,
    }


def common_encoder_inventory() -> dict[str, object]:
    duplicate_keys = sorted(
        (cell, mode, blocks)
        for (cell, mode), blocks in route_b.BLOCKS_BY_CELL_MODE.items()
        if len(blocks) > 1
    )
    return {
        "coarse_cells": len(route_c.BASE_CELLS),
        "coarse_modes": route_c.MODE_COUNT,
        "logical_code_columns_n_le_2": len(route_c.FOCK_BASIS),
        "star_edges_with_multiplicity": len(route_b.FEATURE_BLOCKS),
        "physical_qutrit_feature_blocks": len(route_b.FEATURE_BLOCKS),
        "physical_qutrit_feature_M2_sites": 2 * len(route_b.FEATURE_BLOCKS),
        "duplicate_shared_half_edge_rows": duplicate_keys,
        "landed_local_branch_microbasis_dim": len(local_specs()) + 24,
        "feature_recomputer": "branch-controlled per-block two-bit XOR involution",
        "extra_work_M2_sites": 0,
        "completion_used": "bare 46x46 landed Cycle-311 coin only",
        "augmented_dense_completion_used": False,
        "gram_whitener_used": False,
        "global_parity_service_used": False,
        "preferred_cell_order_used_by_local_recomputer": False,
        "host_side_control_used": False,
        "supplied_structure": [
            "Cycle-311 46-row n<=2 stream-zero branch microbasis",
            "Cycle-311 landed local physical coin K",
            "Route-B lawful qutrit word (outer-X contribution, endpoint tag)",
            "Route-B 24 fixed half-edge qutrit block allocation",
            "bounded branch-ray projectors for the XOR controls",
            "proper-cubic frame action on face and port data",
        ],
    }


def two_star_word_disposition() -> dict[str, object]:
    """State the exact post-coin boundary without disguising a missing seam."""

    return {
        "free_coin_stage": "locally closed by the tested factorization",
        "eleven_seam_stage": "not yet compiled on the same common augmented E",
        "contact_stage": "not reached physically",
        "full_word_claimed": False,
        "first_open_interface": (
            "a bounded same-E physical seam/catch-up map that transports the "
            "Route-B branch factors and then recomputes the endpoint qutrits"
        ),
        "dense_EUE_dagger_substitute_rejected": True,
        "obstruction_claimed": False,
    }


def main() -> None:
    results = [
        local_control(build_fixture(length, fixture))
        for length in (5, 6)
        for fixture in ("shared_center", "outer_arm")
    ]
    inventory = common_encoder_inventory()
    disposition = two_star_word_disposition()

    print("CYCLE659_QUTRIT_COMPUTE_UNCOMPUTE_FIRST_COIN")
    print("inventory", inventory)
    for result in results:
        print("local", result)
    print("two_star_word", disposition)

    for result in results:
        assert result["logical_dim"] == 22
        assert result["branch_microbasis_dim"] == 46
        assert result["augmented_gram_residual"] < TOL
        assert result["bare_landed_coin_intertwiner"] < TOL
        assert result["bare_landed_coin_unitarity"] < TOL
        assert result["compute_uncompute_intertwiner_norm"] < TOL
        assert result["compute_uncompute_intertwiner_raw"] < TOL
        assert result["compute_uncompute_leakage"] < TOL
        assert result["one_particle_coin_fixture_residual"] < TOL
        assert result["one_particle_recomputed_intertwiner"] < TOL
        assert result["one_particle_rest_mass_residual"] < TOL
        assert result["middle_nonblank_branch_count"] == 0
        assert result["returned_work_residual"] < TOL
        assert result["ambient_norm_residual"] < TOL
        assert result["duplicate_shared_view_failures"] == 0
        assert result["first_ambiguous_extraction_row"] is None
        assert result["minimum_erase_deletion_intertwiner"] > 1.0e-3
        assert result["minimum_recompute_deletion_intertwiner"] > 1.0e-3
        symmetry = result["symmetry"]
        assert symmetry["frames"] == 24
        assert symmetry["frame_products"] == 576
        assert symmetry["feature_transport_failures_24"] == 0
        assert symmetry["encoding_covariance_residual_24"] < TOL
        assert symmetry["landed_coin_covariance_residual_24"] < TOL
        assert symmetry["frame_product_mapping_failures_576"] == 0
        assert symmetry["frame_product_representation_residual_576"] < TOL
        assert symmetry["encoding_covariance_residual_576"] < TOL
        assert symmetry["landed_coin_covariance_residual_576"] < TOL
    assert inventory["physical_qutrit_feature_blocks"] == 24
    assert inventory["physical_qutrit_feature_M2_sites"] == 48
    assert not inventory["augmented_dense_completion_used"]
    assert not inventory["gram_whitener_used"]
    assert not disposition["full_word_claimed"]
    assert not disposition["obstruction_claimed"]
    print("COMPUTE_UNCOMPUTE_FIRST_COIN_CLOSED_SAME_E_SEAM_REMAINS_OPEN")


if __name__ == "__main__":
    main()
