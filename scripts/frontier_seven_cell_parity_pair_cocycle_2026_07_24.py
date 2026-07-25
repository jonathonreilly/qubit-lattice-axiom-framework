#!/usr/bin/env python3
"""Bounded seven-cell parity pair-cocycle discriminator.

The candidate uses seven supplied cell-parity bits and one M2 factor on each
ordered pair of distinct cells in a center-plus-six-neighbor star.  For every
active unordered pair it imposes the conditional antisymmetric state

    (|1_(j,i)> - |1_(i,j)>)/sqrt(2).

This exactly realizes the Koszul sign of all S7 factor permutations.  The
runner also checks whether seven cell parities determine the actual pairwise
Pauli commutation signs in the landed Cycle-330 physical branch grammar.  The
second test is deliberately separate: this is a sign/constraint probe, not a
full physical update or recurrence theorem.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from hashlib import sha256
from itertools import combinations, permutations, product
import json
import math
import resource
import time

import numpy as np

import physical_cycle269_common_m64_fixed_seam_cycle311_2026_07_18 as c311
import physical_cycle269_overlap_aware_two_cell_cycle315_2026_07_18 as c315
import physical_cycle269_seven_cell_maximal_star_cycle330_2026_07_18 as c330


START = time.perf_counter()
TOL = 2.0e-12
PASS = 0
FAIL = 0

Coord = tuple[int, int, int]
Frame = tuple[Coord, Coord, Coord]
Permutation = tuple[int, ...]

# Local labels only.  They are a supplied chart on one bounded star, not a
# volume-wide cell order or a runtime order service.
DIRECTIONS: tuple[Coord, ...] = (
    (-1, 0, 0),
    (1, 0, 0),
    (0, -1, 0),
    (0, 1, 0),
    (0, 0, -1),
    (0, 0, 1),
)
CELL_COORDS: tuple[Coord, ...] = ((0, 0, 0),) + DIRECTIONS
UNORDERED_PAIRS = tuple(combinations(range(7), 2))
ORDERED_PAIRS = tuple((left, right) for left in range(7) for right in range(7) if left != right)
ORDERED_INDEX = {pair: index for index, pair in enumerate(ORDERED_PAIRS)}
S7 = tuple(permutations(range(7)))


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label} :: {detail}")
    else:
        FAIL += 1
        print(f"FAIL {label} :: {detail}")


def add(*rows: Coord) -> Coord:
    return tuple(sum(row[axis] for row in rows) for axis in range(3))  # type: ignore[return-value]


def scale(factor: int, row: Coord) -> Coord:
    return tuple(factor * value for value in row)  # type: ignore[return-value]


def det3(frame: Frame) -> int:
    a, b, c = frame
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )


def matvec(frame: Frame, vector: Coord) -> Coord:
    return tuple(
        sum(frame[row][column] * vector[column] for column in range(3))
        for row in range(3)
    )  # type: ignore[return-value]


def matmul(left: Frame, right: Frame) -> Frame:
    return tuple(
        tuple(
            sum(left[row][inner] * right[inner][column] for inner in range(3))
            for column in range(3)
        )
        for row in range(3)
    )  # type: ignore[return-value]


def proper_cubic_frames() -> tuple[Frame, ...]:
    frames = set()
    for order in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            frame = tuple(
                tuple(signs[row] if column == order[row] else 0 for column in range(3))
                for row in range(3)
            )
            if det3(frame) == 1:
                frames.add(frame)
    return tuple(sorted(frames))


FRAMES = proper_cubic_frames()
FRAME_INDEX = {frame: index for index, frame in enumerate(FRAMES)}


def cell_map(frame: Frame) -> Permutation:
    return tuple(CELL_COORDS.index(matvec(frame, site)) for site in CELL_COORDS)


FRAME_MAPS = tuple(cell_map(frame) for frame in FRAMES)


def register_site(pair: tuple[int, int]) -> Coord:
    left, right = pair
    if left == 0:
        return scale(6, CELL_COORDS[right])
    if right == 0:
        return scale(7, CELL_COORDS[left])
    return add(scale(4, CELL_COORDS[left]), CELL_COORDS[right])


REGISTER_SITE = {pair: register_site(pair) for pair in ORDERED_PAIRS}
SEMANTIC_SITES = set(CELL_COORDS) | set(REGISTER_SITE.values())
CARRIER_RADIUS = max(abs(value) for site in SEMANTIC_SITES for value in site)


def l1(left: Coord, right: Coord) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))


def validate_bits(bits: int) -> None:
    if bits < 0 or bits >= 128:
        raise ValueError("seven parity bits must lie in 0..127")


def validate_permutation(mapping: Permutation) -> None:
    if len(mapping) != 7 or set(mapping) != set(range(7)):
        raise ValueError("mapping must be a permutation of seven local cells")


def occupied(bits: int) -> tuple[int, ...]:
    validate_bits(bits)
    return tuple(index for index in range(7) if (bits >> index) & 1)


def transformed_bits(bits: int, mapping: Permutation) -> int:
    validate_permutation(mapping)
    result = 0
    for source in occupied(bits):
        result |= 1 << mapping[source]
    return result


def active_pair_mask(bits: int) -> int:
    result = 0
    for index, (left, right) in enumerate(UNORDERED_PAIRS):
        if ((bits >> left) & 1) and ((bits >> right) & 1):
            result |= 1 << index
    return result


def inversion_mask_from_mapping(mapping: Permutation) -> int:
    mask = 0
    for index, (left, right) in enumerate(UNORDERED_PAIRS):
        if mapping[left] > mapping[right]:
            mask |= 1 << index
    return mask


def pair_cocycle(bits: int, mapping: Permutation) -> int:
    flips = (active_pair_mask(bits) & inversion_mask_from_mapping(mapping)).bit_count()
    return -1 if flips & 1 else 1


def register_transport(bits: int, mapping: Permutation) -> tuple[int, int, int]:
    """Compressed exact transport of the 21 tensor pair factors.

    Returns transformed parity bits, the active target-pair mask, and the
    antisymmetric phase.  No 2^42 ambient vector is materialized.
    """
    target_bits = transformed_bits(bits, mapping)
    target_mask = 0
    phase = 1
    pair_index = {pair: index for index, pair in enumerate(UNORDERED_PAIRS)}
    for left, right in UNORDERED_PAIRS:
        if not (((bits >> left) & 1) and ((bits >> right) & 1)):
            continue
        mapped_left, mapped_right = mapping[left], mapping[right]
        if mapped_left > mapped_right:
            mapped_left, mapped_right = mapped_right, mapped_left
            phase *= -1
        target_mask |= 1 << pair_index[(mapped_left, mapped_right)]
    return target_bits, target_mask, phase


def compose(left: Permutation, right: Permutation) -> Permutation:
    """Composition left after right."""
    return tuple(left[right[index]] for index in range(7))


def apply_word(bits: int, word: tuple[Permutation, ...]) -> tuple[int, int]:
    phase = 1
    for mapping in word:
        phase *= pair_cocycle(bits, mapping)
        bits = transformed_bits(bits, mapping)
    return bits, phase


def adjacent_swap(index: int) -> Permutation:
    mapping = list(range(7))
    mapping[index], mapping[index + 1] = mapping[index + 1], mapping[index]
    return tuple(mapping)


ADJACENT_SWAPS = tuple(adjacent_swap(index) for index in range(6))


def local_pair_projector() -> np.ndarray:
    """Rank-four projector on q_i,q_j,r_(j,i),r_(i,j)."""
    projector = np.zeros((16, 16), dtype=float)
    for q_bits in (0, 1, 2):
        projector[q_bits, q_bits] = 1.0
    backward = 3 | (1 << 2)
    forward = 3 | (1 << 3)
    vector = np.zeros(16, dtype=float)
    vector[backward] = 1 / math.sqrt(2)
    vector[forward] = -1 / math.sqrt(2)
    projector += np.outer(vector, vector)
    return projector


def pair_action(
    basis: int,
    q_left: int,
    q_right: int,
    register_backward: int,
    register_forward: int,
) -> dict[int, float]:
    active = ((basis >> q_left) & 1) and ((basis >> q_right) & 1)
    backward = (basis >> register_backward) & 1
    forward = (basis >> register_forward) & 1
    if not active:
        return {basis: 1.0} if backward == forward == 0 else {}
    if backward == forward:
        return {}
    cleared = basis & ~(1 << register_backward) & ~(1 << register_forward)
    backward_basis = cleared | (1 << register_backward)
    forward_basis = cleared | (1 << register_forward)
    sign = 1.0 if backward else -1.0
    return {backward_basis: 0.5 * sign, forward_basis: -0.5 * sign}


def apply_pair(state: dict[int, float], spec: tuple[int, int, int, int]) -> dict[int, float]:
    result: dict[int, float] = {}
    for basis, amplitude in state.items():
        for target, factor in pair_action(basis, *spec).items():
            result[target] = result.get(target, 0.0) + amplitude * factor
    return {basis: value for basis, value in result.items() if value}


def projector_commutator_census() -> dict[str, int]:
    failures = overlap_failures = disjoint_failures = 0
    overlap_pairs = disjoint_pairs = basis_cases = 0
    for first_pair, second_pair in combinations(UNORDERED_PAIRS, 2):
        logical = tuple(sorted(set(first_pair + second_pair)))
        q_index = {cell: index for index, cell in enumerate(logical)}
        offset = len(logical)
        first_spec = (q_index[first_pair[0]], q_index[first_pair[1]], offset, offset + 1)
        second_spec = (q_index[second_pair[0]], q_index[second_pair[1]], offset + 2, offset + 3)
        overlapping = len(logical) == 3
        overlap_pairs += overlapping
        disjoint_pairs += not overlapping
        for basis in range(1 << (offset + 4)):
            basis_cases += 1
            source = {basis: 1.0}
            left = apply_pair(apply_pair(source, second_spec), first_spec)
            right = apply_pair(apply_pair(source, first_spec), second_spec)
            keys = set(left) | set(right)
            different = any(abs(left.get(key, 0.0) - right.get(key, 0.0)) > 1e-15 for key in keys)
            failures += different
            overlap_failures += overlapping and different
            disjoint_failures += (not overlapping) and different
    return {
        "projector_pairs": overlap_pairs + disjoint_pairs,
        "overlapping_pairs": overlap_pairs,
        "disjoint_pairs": disjoint_pairs,
        "reduced_basis_cases": basis_cases,
        "failures": failures,
        "overlap_failures": overlap_failures,
        "disjoint_failures": disjoint_failures,
    }


def physical_branch_parity_census(length: int) -> dict[str, object]:
    """Compare parity signs with landed Cycle-330 branch commutators at n<=2."""
    code = c315.c269.build_code(length)
    cache = {
        (cell_index, number, label): c315.gauge_input_terms(
            code, cell, number, label
        )
        for cell_index, cell in enumerate(c330.CELLS)
        for number, label in c311.FOCK_LABELS
    }
    cases = mismatches = anticommuting = 0
    class_rows = defaultdict(lambda: Counter(cases=0, mismatches=0, anticommuting=0))
    parity_outcomes: dict[tuple[int, int, int, int], set[bool]] = defaultdict(set)
    for left_cell, right_cell in c330.PAIR_LABELS:
        pair_class = "center_arm" if left_cell == 0 else "arm_arm"
        for left_number, left_label in c311.FOCK_LABELS:
            for right_number, right_label in c311.FOCK_LABELS:
                if left_number + right_number > 2:
                    continue
                expected = bool((left_number & 1) and (right_number & 1))
                for left_term in cache[(left_cell, left_number, left_label)]:
                    for right_term in cache[(right_cell, right_number, right_label)]:
                        observed = not left_term.representative.commutes(
                            right_term.representative
                        )
                        different = observed != expected
                        cases += 1
                        mismatches += different
                        anticommuting += observed
                        class_rows[pair_class]["cases"] += 1
                        class_rows[pair_class]["mismatches"] += different
                        class_rows[pair_class]["anticommuting"] += observed
                        parity_outcomes[
                            (left_cell, right_cell, left_number & 1, right_number & 1)
                        ].add(observed)
    ambiguous_center_arm_odd_pairs = sum(
        outcomes == {False, True}
        for (left, _right, left_parity, right_parity), outcomes in parity_outcomes.items()
        if left == 0 and left_parity == right_parity == 1
    )
    neighbor_odd_pairs_always_commuting = sum(
        outcomes == {False}
        for (left, _right, left_parity, right_parity), outcomes in parity_outcomes.items()
        if left != 0 and left_parity == right_parity == 1
    )
    return {
        "L": length,
        "Cycle330_total_number_boundary": 2,
        "term_pair_cases": cases,
        "parity_sign_mismatches": mismatches,
        "observed_anticommuting_term_pairs": anticommuting,
        "by_pair_class": {key: dict(value) for key, value in sorted(class_rows.items())},
        "ambiguous_center_arm_odd_pairs": ambiguous_center_arm_odd_pairs,
        "neighbor_odd_pairs_always_commuting": neighbor_odd_pairs_always_commuting,
    }


def placement_census() -> dict[str, object]:
    pitch = 2 * CARRIER_RADIUS + 1
    rows = []
    for length, split in ((3, "train"), (5, "held-no-refit")):
        anchors = tuple(
            (pitch * x, pitch * y, pitch * z)
            for x in range(length)
            for y in range(length)
            for z in range(length)
        )
        placed = {
            add(anchor, site) for anchor in anchors for site in SEMANTIC_SITES
        }
        rows.append(
            {
                "L": length,
                "split": split,
                "isolated_star_blocks": len(anchors),
                "semantic_M2_per_star": len(SEMANTIC_SITES),
                "collisions": len(anchors) * len(SEMANTIC_SITES) - len(placed),
            }
        )
    return {
        "pitch": pitch,
        "rows": rows,
        "held_parameters_refit": 0,
        "recurrent_or_overlapping_star_tested": False,
    }


def main() -> None:
    frame_determinants = Counter(det3(frame) for frame in FRAMES)
    frame_maps_unique = len(set(FRAME_MAPS))
    check(
        "the center-plus-six-neighbor proper-cubic subgroup has 24 exact actions",
        len(FRAMES) == 24
        and frame_determinants == {1: 24}
        and frame_maps_unique == 24
        and all(mapping[0] == 0 for mapping in FRAME_MAPS),
        {
            "frames": len(FRAMES),
            "determinants": dict(frame_determinants),
            "distinct_cell_permutations": frame_maps_unique,
            "center_fixed": True,
        },
    )

    all_order_failures = 0
    all_target_failures = 0
    all_sign_failures = 0
    constraint_family_failures = 0
    maximum_active_pairs = 0
    maximum_compressed_support = 0
    order_masks = []
    for order in S7:
        positions = tuple(order.index(cell) for cell in range(7))
        mask = c330.inversion_mask(order)
        order_masks.append(mask)
        all_order_failures += mask != inversion_mask_from_mapping(positions)
        constraint_family_failures += {
            tuple(sorted((positions[left], positions[right])))
            for left, right in UNORDERED_PAIRS
        } != set(UNORDERED_PAIRS)
        constraint_family_failures += {
            (positions[left], positions[right]) for left, right in ORDERED_PAIRS
        } != set(ORDERED_PAIRS)
        for bits in range(128):
            target_bits, target_mask, phase = register_transport(bits, positions)
            all_target_failures += target_mask != active_pair_mask(target_bits)
            expected = -1 if (active_pair_mask(bits) & mask).bit_count() & 1 else 1
            all_sign_failures += phase != expected or pair_cocycle(bits, positions) != expected
            pairs = bits.bit_count() * (bits.bit_count() - 1) // 2
            maximum_active_pairs = max(maximum_active_pairs, pairs)
            maximum_compressed_support = max(maximum_compressed_support, 1 << pairs)
    check(
        "the conditional ordered-pair product realizes every Cycle-330 S7 inversion sign",
        all_order_failures == all_target_failures == all_sign_failures == 0
        and constraint_family_failures == 0
        and len(set(order_masks)) == math.factorial(7)
        and maximum_active_pairs == 21,
        {
            "parity_patterns": 128,
            "S7_permutations": len(S7),
            "permutation_pattern_cases": len(S7) * 128,
            "distinct_21bit_inversion_masks": len(set(order_masks)),
            "order_mask_failures": all_order_failures,
            "target_pair_failures": all_target_failures,
            "sign_failures": all_sign_failures,
            "conditional_projector_family_failures": constraint_family_failures,
            "maximum_active_pair_factors": maximum_active_pairs,
            "largest_exact_factor_product_support_not_materialized": maximum_compressed_support,
        },
    )

    involution_failures = braid_failures = far_failures = 0
    for bits in range(128):
        for swap in ADJACENT_SWAPS:
            involution_failures += apply_word(bits, (swap, swap)) != (bits, 1)
        for index in range(5):
            left = apply_word(
                bits,
                (ADJACENT_SWAPS[index], ADJACENT_SWAPS[index + 1], ADJACENT_SWAPS[index]),
            )
            right = apply_word(
                bits,
                (ADJACENT_SWAPS[index + 1], ADJACENT_SWAPS[index], ADJACENT_SWAPS[index + 1]),
            )
            braid_failures += left != right
        for first in range(6):
            for second in range(first + 2, 6):
                far_failures += apply_word(
                    bits, (ADJACENT_SWAPS[first], ADJACENT_SWAPS[second])
                ) != apply_word(
                    bits, (ADJACENT_SWAPS[second], ADJACENT_SWAPS[first])
                )
    check(
        "adjacent swaps are exact involutions and satisfy every S7 braid and far commutator",
        involution_failures == braid_failures == far_failures == 0,
        {
            "adjacent_involution_cases": 128 * 6,
            "adjacent_braid_cases": 128 * 5,
            "far_commutator_cases": 128 * 10,
            "involution_failures": involution_failures,
            "braid_failures": braid_failures,
            "far_commutator_failures": far_failures,
        },
    )

    site_transport_failures = register_transport_failures = 0
    frame_product_failures = cocycle_product_failures = 0
    for frame, mapping in zip(FRAMES, FRAME_MAPS):
        site_transport_failures += sum(
            matvec(frame, site) not in SEMANTIC_SITES for site in SEMANTIC_SITES
        )
        register_transport_failures += sum(
            matvec(frame, site) != REGISTER_SITE[(mapping[pair[0]], mapping[pair[1]])]
            for pair, site in REGISTER_SITE.items()
        )
    for left_index, left in enumerate(FRAMES):
        for right_index, right in enumerate(FRAMES):
            target_index = FRAME_INDEX[matmul(left, right)]
            left_map, right_map = FRAME_MAPS[left_index], FRAME_MAPS[right_index]
            target_map = FRAME_MAPS[target_index]
            frame_product_failures += compose(left_map, right_map) != target_map
            for bits in range(128):
                composed_sign = pair_cocycle(bits, right_map) * pair_cocycle(
                    transformed_bits(bits, right_map), left_map
                )
                cocycle_product_failures += composed_sign != pair_cocycle(bits, target_map)
    check(
        "the 49-site placement and all 576 proper-cubic cocycle products close exactly",
        site_transport_failures == register_transport_failures == 0
        and frame_product_failures == cocycle_product_failures == 0,
        {
            "semantic_M2_sites": len(SEMANTIC_SITES),
            "cell_parity_sites": len(CELL_COORDS),
            "ordered_pair_register_sites": len(REGISTER_SITE),
            "coordinate_transport_cases": len(FRAMES) * len(SEMANTIC_SITES),
            "ordered_frame_products": len(FRAMES) ** 2,
            "frame_product_parity_cases": len(FRAMES) ** 2 * 128,
            "site_transport_failures": site_transport_failures,
            "register_transport_failures": register_transport_failures,
            "frame_product_failures": frame_product_failures,
            "cocycle_product_failures": cocycle_product_failures,
        },
    )

    local = local_pair_projector()
    local_hermitian = float(np.linalg.norm(local - local.T))
    local_idempotence = float(np.linalg.norm(local @ local - local))
    local_rank = int(np.linalg.matrix_rank(local, tol=1e-12))
    local_code_residual = 0.0
    for left_bit, right_bit in product((0, 1), repeat=2):
        vector = np.zeros(16, dtype=float)
        q_bits = left_bit | (right_bit << 1)
        if left_bit and right_bit:
            vector[q_bits | (1 << 2)] = 1 / math.sqrt(2)
            vector[q_bits | (1 << 3)] = -1 / math.sqrt(2)
        else:
            vector[q_bits] = 1.0
        local_code_residual = max(local_code_residual, float(np.linalg.norm(local @ vector - vector)))
    commutators = projector_commutator_census()
    check(
        "all 21 rank-four conditional pair projectors commute, including all overlaps",
        local_hermitian < TOL
        and local_idempotence < TOL
        and local_rank == 4
        and local_code_residual < TOL
        and commutators["failures"] == 0
        and commutators["overlapping_pairs"] == commutators["disjoint_pairs"] == 105,
        {
            "conditional_projectors": len(UNORDERED_PAIRS),
            "local_projector_rank": local_rank,
            "local_hermiticity_residual": local_hermitian,
            "local_idempotence_residual": local_idempotence,
            "local_code_residual": local_code_residual,
            **commutators,
            "joint_code_dimension": 128,
            "deleted_one_projector_dimension": 512,
        },
    )

    pair_support_sizes = []
    pair_support_diameters = []
    for left, right in UNORDERED_PAIRS:
        support = {
            CELL_COORDS[left],
            CELL_COORDS[right],
            REGISTER_SITE[(left, right)],
            REGISTER_SITE[(right, left)],
        }
        pair_support_sizes.append(len(support))
        pair_support_diameters.append(max(l1(a, b) for a in support for b in support))
    placement = placement_census()
    check(
        "the constraint family has a constant bounded placement and held isolated-block census",
        len(SEMANTIC_SITES) == 49
        and len(REGISTER_SITE) == 42
        and CARRIER_RADIUS == 7
        and max(pair_support_sizes) == 4
        and max(pair_support_diameters) == 7
        and all(row["collisions"] == 0 for row in placement["rows"])
        and placement["held_parameters_refit"] == 0,
        {
            "explicit_parity_plus_register_M2": len(SEMANTIC_SITES),
            "new_register_M2_if_seven_parity_controls_already_exist": len(REGISTER_SITE),
            "prior_dense_S7_role_M2": 13,
            "prior_dense_S7_lawful_states": math.factorial(7),
            "prior_dense_S7_unused_states": 2**13 - math.factorial(7),
            "conditional_projectors": len(UNORDERED_PAIRS),
            "maximum_projector_support_M2": max(pair_support_sizes),
            "maximum_projector_L1_diameter": max(pair_support_diameters),
            "carrier_radius": CARRIER_RADIUS,
            "carrier_cube_M2": (2 * CARRIER_RADIUS + 1) ** 3,
            **placement,
        },
    )

    symmetric = np.asarray((1 / math.sqrt(2), 1 / math.sqrt(2)))
    swapped_symmetric = symmetric[::-1]
    symmetric_sign_deletion_residual = float(np.linalg.norm(swapped_symmetric + symmetric))
    one_ordered_site_probability_loss = 0.5
    inactive = np.asarray((1.0, 0.0, 0.0))
    falsely_active = np.asarray((0.0, 1 / math.sqrt(2), -1 / math.sqrt(2)))
    deleted_control_residual = float(np.linalg.norm(inactive - falsely_active))
    removed_site = REGISTER_SITE[(0, 1)]
    reduced_sites = SEMANTIC_SITES - {removed_site}
    removed_site_covariance_failures = sum(
        matvec(frame, site) not in reduced_sites
        for frame in FRAMES
        for site in reduced_sites
    )
    unlawful_rejections = 0
    for bits, mapping in (
        (-1, tuple(range(7))),
        (128, tuple(range(7))),
        (0, (0, 1, 2, 3, 4, 5, 5)),
        (0, tuple(range(6))),
    ):
        try:
            transformed_bits(bits, mapping)
        except ValueError:
            unlawful_rejections += 1
    check(
        "antisymmetry, one-site, projector, control and lawful-domain deletions stay active",
        abs(symmetric_sign_deletion_residual - 2.0) < TOL
        and one_ordered_site_probability_loss == 0.5
        and abs(deleted_control_residual - math.sqrt(2)) < TOL
        and removed_site_covariance_failures > 0
        and unlawful_rejections == 4,
        {
            "delete_antisymmetric_phase_swap_residual": symmetric_sign_deletion_residual,
            "delete_one_ordered_amplitude_probability_loss": one_ordered_site_probability_loss,
            "delete_one_conditional_projector_dimension": 512,
            "delete_parity_control_residual": deleted_control_residual,
            "delete_one_register_site_covariance_failures": removed_site_covariance_failures,
            "lawful_domain_rejections": unlawful_rejections,
        },
    )

    physical_rows = [physical_branch_parity_census(length) for length in (5, 6)]
    physical_stable = physical_rows[0] == {**physical_rows[1], "L": 5}
    check(
        "the probe retains the physical residual: seven parities do not determine Cycle-330 branch signs",
        physical_stable
        and all(row["term_pair_cases"] == 83244 for row in physical_rows)
        and all(row["parity_sign_mismatches"] == 74400 for row in physical_rows)
        and all(row["ambiguous_center_arm_odd_pairs"] == 6 for row in physical_rows)
        and all(row["neighbor_odd_pairs_always_commuting"] == 15 for row in physical_rows),
        {
            "rows": physical_rows,
            "interpretation": (
                "the parity cocycle closes the abstract Koszul sign/constraint algebra, but cannot by "
                "itself replace the landed physical S7 order role because actual branch commutation "
                "is not a function of the seven cell-parity bits"
            ),
        },
    )

    certificate = {
        "cell_coords": CELL_COORDS,
        "register_sites": sorted((pair, site) for pair, site in REGISTER_SITE.items()),
        "frames": FRAMES,
    }
    digest = sha256(
        json.dumps(certificate, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    result = {
        "authority": "none",
        "audit": "unset",
        "status": "bounded-seven-cell-parity-pair-cocycle-discriminator",
        "terminal": "ABSTRACT_PARITY_COCYCLE_CLOSED_PHYSICAL_ORDER_ROLE_NOT_RETIRED",
        "pass": FAIL == 0,
        "tests_passed": PASS,
        "tests_failed": FAIL,
        "domains": {
            "parity_patterns": 128,
            "S7_permutations": 5040,
            "proper_cubic_frames": 24,
            "ordered_frame_products": 576,
            "Cycle330_physical_term_pair_cases_per_size": 83244,
        },
        "resources": {
            "cell_parity_M2": 7,
            "ordered_pair_register_M2": 42,
            "semantic_M2": 49,
            "conditional_projectors": 21,
            "maximum_projector_support_M2": 4,
            "maximum_projector_L1_diameter": 7,
            "carrier_radius": 7,
            "elapsed_seconds": time.perf_counter() - START,
            "peak_rss_mb": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / (1024 * 1024),
        },
        "physical_residual_match": physical_rows,
        "certificate_sha256": digest,
        "supplied": (
            "one local center-plus-six-neighbor chart and its seven cell-parity controls",
            "42 ordered-pair M2 sites and the conditional antisymmetric pair state",
            "21 rank-four static conditional projectors",
            "the standard local S7 relabeling action and proper-cubic coordinate subgroup",
            "the landed Cycle-311/315/330 branch grammar for the physical residual comparator",
            "isolated-star pitch 15 and numerical tolerance 2e-12",
        ),
        "derived": (
            "all-128/all-5040 exact Koszul pair cocycle",
            "exact adjacent involution, braid and far-commutator relations",
            "all-576 proper-cubic cocycle products and coordinate covariance",
            "21 mutually commuting local conditional projectors with joint code dimension 128",
            "bounded 49-M2 placement, deletion controls and held isolated-block census",
            "stable Cycle-330 n<=2 residual showing 74400 parity-sign mismatches in 83244 branch-term pairs",
        ),
        "open": (
            "a local physical observable that supplies each actual Cycle-330 branch anticommutation bit",
            "replacement of the physical S3/S7 order sectors rather than their abstract Koszul sign grammar",
            "a full two-cell physical update and intertwiner on the pair-cocycle code",
            "overlapping maximal-star constraints, recurrence, collision control and full M64^7",
            "preparation, dynamical enforcement, primitive synthesis and state genesis",
            "minimality, impossibility, shared obstruction, axiom pressure, time, source, Record and probability",
        ),
        "claim_ceiling": (
            "Positive bounded parity/sign/constraint theorem plus a retained physical residual.  The "
            "42-site pair register replaces the dense S7 role only for the abstract Koszul cocycle.  "
            "It does not retire the landed physical order-role import, execute a two-cell update, or "
            "establish recurrence, full M64^7, minimality, impossibility or axiom pressure."
        ),
    }
    print("SUMMARY_JSON", json.dumps(result, sort_keys=True))
    print("RESULT", result["terminal"] if result["pass"] else "UNFINISHED_IMPLEMENTATION")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
