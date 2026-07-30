#!/usr/bin/env python3
"""Independent two-cell parity-superselected even-CAR checker.

This runner deliberately does not import the Cycle-813 construction, a new
primary/core module, or any scratch runner.  Landed modules provide only the
two-cell fixture and its signed proper-cubic generator images.  All Pauli
arithmetic, image application, GF(2) solving, stabilizer evolution, marginal
extraction, and signed-span comparison below use a separate ``(phase,x,z)``
tuple/bit-vector implementation.

The checked channel is the rank-23 even-CAR character channel on shape
``(2,1,1)``.  Total parity is superselected but its eigenvalue is not fixed:
both parity sectors and arbitrary mixtures are in scope.  The final diagnostic
constructs two opposite odd extensions only to prove that their restrictions
to the even algebra coincide; it makes no odd-covariance or odd-closure claim.
"""

from __future__ import annotations

from hashlib import sha256
from itertools import product
import json
from pathlib import Path

import numpy as np

import frontier_cycle708_endpoint_cube_tableau_core_2026_07_26 as T708
import frontier_cycle720_companion_checkerboard_frame_cocycle_2026_07_27 as Q720
import frontier_cycle720_companion_local_choi_tree_plaquette_pump_2026_07_27 as P720
import frontier_cycle720_overlap_star_mixed_gauge_choi_2026_07_27 as O720


AUDIT_TIMEOUT_SEC = 900
IMPLEMENTATION_IMPORT_PATHS = (
    "scripts/frontier_cycle708_endpoint_cube_tableau_core_2026_07_26.py",
    "scripts/frontier_cycle720_companion_checkerboard_frame_cocycle_2026_07_27.py",
    "scripts/frontier_cycle720_companion_local_choi_tree_plaquette_pump_2026_07_27.py",
    "scripts/frontier_cycle720_overlap_star_mixed_gauge_choi_2026_07_27.py",
)
AUDIT_INPUT_PATHS = (
    "docs/FULL128_TWO_CELL_PARITY_SUPERSELECTED_EVEN_CAR_COVARIANCE_CYCLE820_BOUNDED_THEOREM_NOTE_2026-07-30.md",
    "scripts/frontier_cycle820_full128_two_cell_parity_superselected_even_car_covariance_2026_07_30.py",
    "scripts/frontier_cycle820_full128_two_cell_parity_superselected_even_car_independent_2026_07_30.py",
) + IMPLEMENTATION_IMPORT_PATHS
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS
SHAPE = (2, 1, 1)
ZERO = (0, 0, 0)
ORIGINS = tuple(product(range(2), repeat=3))

# A Pauli is i**phase X**x Z**z.  This representation and every operation on
# it are local to this checker and intentionally distinct from the landed
# Pauli classes used only at the geometry/image boundary.
Row = tuple[int, int, int]


def fields(row: Row) -> Row:
    return row[0] % 4, int(row[1]), int(row[2])


def imported_row(row) -> Row:
    return int(row.phase) % 4, int(row.x), int(row.z)


def multiply(left: Row, right: Row) -> Row:
    phase = (left[0] + right[0] + 2 * (left[2] & right[1]).bit_count()) % 4
    return phase, left[1] ^ right[1], left[2] ^ right[2]


def product_rows(rows) -> Row:
    output: Row = (0, 0, 0)
    for row in rows:
        output = multiply(output, row)
    return output


def canonical(x: int, z: int, negative: bool = False) -> Row:
    return ((x & z).bit_count() + 2 * int(negative)) % 4, x, z


def shift(row: Row, offset: int) -> Row:
    return row[0] % 4, row[1] << offset, row[2] << offset


def transpose(row: Row) -> Row:
    return (row[0] + 2 * (row[1] & row[2]).bit_count()) % 4, row[1], row[2]


def hermitian_sign(row: Row) -> int:
    delta = (row[0] - (row[1] & row[2]).bit_count()) % 4
    if delta not in (0, 2):
        raise ValueError(("anti-Hermitian row", row))
    return delta // 2


def symplectic_vector(row: Row, width: int) -> int:
    return row[1] | (row[2] << width)


def anticommutes(left: Row, right: Row) -> int:
    return ((left[1] & right[2]).bit_count() ^ (left[2] & right[1]).bit_count()) & 1


def gf2_rank(rows) -> int:
    pivots: dict[int, int] = {}
    for original in rows:
        row = int(original)
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                break
    return len(pivots)


def gf2_solution(equations: tuple[tuple[int, int], ...]) -> tuple[int, int, int]:
    """Return one zero-free-variable solution, rank, and contradictions."""
    pivots: dict[int, tuple[int, int]] = {}
    contradictions = 0
    for original_mask, original_rhs in equations:
        mask = int(original_mask)
        rhs = int(original_rhs) & 1
        while mask:
            pivot = mask.bit_length() - 1
            if pivot in pivots:
                prior_mask, prior_rhs = pivots[pivot]
                mask ^= prior_mask
                rhs ^= prior_rhs
            else:
                pivots[pivot] = (mask, rhs)
                break
        if not mask and rhs:
            contradictions += 1
    solution = 0
    for pivot in sorted(pivots):
        mask, rhs = pivots[pivot]
        lower = mask & ((1 << pivot) - 1)
        value = rhs ^ ((solution & lower).bit_count() & 1)
        if value:
            solution |= 1 << pivot
    return solution, len(pivots), contradictions


def relation_masks(vectors: tuple[int, ...]) -> tuple[int, ...]:
    """Basis of coefficient masks whose selected vectors xor to zero."""
    pivots: dict[int, tuple[int, int]] = {}
    relations = []
    for index, original in enumerate(vectors):
        vector = int(original)
        combination = 1 << index
        while vector:
            pivot = vector.bit_length() - 1
            if pivot in pivots:
                prior_vector, prior_combination = pivots[pivot]
                vector ^= prior_vector
                combination ^= prior_combination
            else:
                pivots[pivot] = (vector, combination)
                break
        if not vector:
            relations.append(combination)
    return tuple(relations)


def span_pivots(basis: tuple[Row, ...], width: int):
    pivots: dict[int, tuple[int, int]] = {}
    for index, original in enumerate(basis):
        vector = symplectic_vector(original, width)
        combination = 1 << index
        while vector:
            pivot = vector.bit_length() - 1
            if pivot in pivots:
                prior_vector, prior_combination = pivots[pivot]
                vector ^= prior_vector
                combination ^= prior_combination
            else:
                pivots[pivot] = (vector, combination)
                break
    return pivots


def span_combination(target: Row, width: int, pivots) -> int | None:
    vector = symplectic_vector(target, width)
    combination = 0
    while vector:
        pivot = vector.bit_length() - 1
        if pivot not in pivots:
            return None
        prior_vector, prior_combination = pivots[pivot]
        vector ^= prior_vector
        combination ^= prior_combination
    return combination


def rows_from_mask(rows: tuple[Row, ...], mask: int) -> Row:
    output: Row = (0, 0, 0)
    while mask:
        bit = mask & -mask
        output = multiply(output, rows[bit.bit_length() - 1])
        mask ^= bit
    return output


def signed_span_failures(
    targets: tuple[Row, ...], basis: tuple[Row, ...], width: int
) -> tuple[int, int]:
    pivots = span_pivots(basis, width)
    binary = signed = 0
    for target in targets:
        combination = span_combination(target, width, pivots)
        if combination is None:
            binary += 1
            signed += 1
            continue
        replay = rows_from_mask(basis, combination)
        signed += fields(replay) != fields(target)
    return binary, signed


def apply_images(row: Row, images: tuple[tuple[Row, ...], tuple[Row, ...]]) -> Row:
    output: Row = (row[0] % 4, 0, 0)
    x_images, z_images = images
    mask = row[1]
    while mask:
        bit = mask & -mask
        output = multiply(output, x_images[bit.bit_length() - 1])
        mask ^= bit
    mask = row[2]
    while mask:
        bit = mask & -mask
        output = multiply(output, z_images[bit.bit_length() - 1])
        mask ^= bit
    return output


def frame_key(frame: np.ndarray) -> tuple[tuple[int, int, int], ...]:
    return tuple(tuple(int(value) for value in row) for row in frame)


def target_fixture(source, frame: np.ndarray):
    return O720.arbitrary_fixture(Q720.affine_cells(source.cells, frame, ZERO))


def physical_images(source, target, frame: np.ndarray, target_seed) -> tuple[tuple[Row, ...], tuple[Row, ...]]:
    solution = Q720.seeded_sheet_solution(
        frame, Q720.predicted_sheet_solution(frame), target_seed
    )
    x_images, z_images = Q720.corrected_images(
        source, target, frame, ZERO, solution
    )
    return tuple(map(imported_row, x_images)), tuple(map(imported_row, z_images))


def choi_images(source, target, frame: np.ndarray, target_seed) -> tuple[tuple[Row, ...], tuple[Row, ...]]:
    physical_x, physical_z = physical_images(source, target, frame, target_seed)
    matter_x, matter_z = Q720.matter_images(source, target, frame, ZERO)
    return (
        physical_x + tuple(shift(imported_row(row), target.qubits) for row in matter_x),
        physical_z + tuple(shift(imported_row(row), target.qubits) for row in matter_z),
    )


def base_rows(fixture) -> dict[str, object]:
    graph, tags = P720.direct_graph_basis(fixture)
    q = fixture.qubits
    m = fixture.matter_qubits
    q_mask = (1 << q) - 1
    m_mask = (1 << m) - 1
    choi = tuple(map(imported_row, graph))
    physical = tuple(
        canonical(row[1] & q_mask, row[2] & q_mask) for row in choi
    )
    target = tuple(
        canonical((row[1] >> q) & m_mask, (row[2] >> q) & m_mask)
        for row in choi
    )
    return {"choi": choi, "physical": physical, "target": target, "tags": tags}


def parity_and_product_certificate(fixture, rows, frames) -> dict[str, object]:
    q = fixture.qubits
    m = fixture.matter_qubits
    matter_mask = (1 << m) - 1
    frame_origin_rows = 0
    physical_parity_failures = target_parity_failures = 0
    origin_image_rank_failures = 0
    per_frame_origin_digests = set()

    for frame in frames:
        target = target_fixture(fixture, frame)
        for origin in ORIGINS:
            target_seed = Q720.transported_seed(frame, ZERO, origin)
            images = choi_images(fixture, target, frame, target_seed)
            mapped = tuple(apply_images(row, images) for row in rows["choi"])
            origin_image_rank_failures += (
                gf2_rank(symplectic_vector(row, q + m) for row in mapped) != 23
            )
            for row in mapped:
                physical_parity_failures += (
                    (row[1] & matter_mask).bit_count() & 1
                )
                target_parity_failures += (
                    ((row[1] >> q) & matter_mask).bit_count() & 1
                )
                frame_origin_rows += 1
            per_frame_origin_digests.add(sha256(repr(mapped).encode()).hexdigest())

    frame_index = {frame_key(frame): index for index, frame in enumerate(frames)}
    origin_binary_failures = origin_signed_failures = 0
    collapsed_binary_failures: set[tuple[int, int, int]] = set()
    collapsed_signed_failures: set[tuple[int, int, int]] = set()
    first_failure = None
    origin_comparisons = 0
    for left_id, left in enumerate(frames):
        for right_id, right in enumerate(frames):
            product_frame = left @ right
            product_id = frame_index[frame_key(product_frame)]
            middle = target_fixture(fixture, right)
            final = target_fixture(fixture, product_frame)
            for origin in ORIGINS:
                middle_seed = Q720.transported_seed(right, ZERO, origin)
                final_seed = Q720.transported_seed(left, ZERO, middle_seed)
                direct_seed = Q720.transported_seed(product_frame, ZERO, origin)
                right_images = choi_images(
                    fixture, middle, right, middle_seed
                )
                left_images = choi_images(
                    middle, final, left, final_seed
                )
                direct_images = choi_images(
                    fixture, final, product_frame, direct_seed
                )
                for row_id, row in enumerate(rows["choi"]):
                    sequential = apply_images(
                        apply_images(row, right_images), left_images
                    )
                    direct = apply_images(row, direct_images)
                    binary_failure = sequential[1:] != direct[1:]
                    signed_failure = fields(sequential) != fields(direct)
                    origin_binary_failures += binary_failure
                    origin_signed_failures += signed_failure
                    if binary_failure:
                        collapsed_binary_failures.add((left_id, right_id, row_id))
                    if signed_failure:
                        collapsed_signed_failures.add((left_id, right_id, row_id))
                    if signed_failure and first_failure is None:
                        first_failure = {
                            "left": left_id,
                            "right": right_id,
                            "product": product_id,
                            "origin": origin,
                            "row": row_id,
                            "sequential": fields(sequential),
                            "direct": fields(direct),
                        }
                    origin_comparisons += 1

    return {
        "proper_frames": len(frames),
        "origin_sectors": len(ORIGINS),
        "frame_origin_contexts": len(frames) * len(ORIGINS),
        "frame_origin_rows_checked": frame_origin_rows,
        "origin_image_rank_failures": origin_image_rank_failures,
        "physical_half_parity_even_failures": physical_parity_failures,
        "target_half_parity_even_failures": target_parity_failures,
        "distinct_frame_origin_signed_images": len(per_frame_origin_digests),
        "ordered_frame_products": len(frames) ** 2,
        "signed_product_comparisons": 23 * len(frames) ** 2,
        "origin_expanded_signed_product_comparisons": origin_comparisons,
        "binary_product_failures": len(collapsed_binary_failures),
        "signed_product_failures": len(collapsed_signed_failures),
        "origin_expanded_binary_product_failures": origin_binary_failures,
        "origin_expanded_signed_product_failures": origin_signed_failures,
        "first_product_failure": first_failure,
    }


def private_duals(rows: tuple[Row, ...], q: int) -> tuple[tuple[Row, ...], dict[str, int]]:
    duals = []
    contradictions = rank_failures = one_hot_failures = 0
    for desired in range(len(rows)):
        equations = tuple(
            (row[2] | (row[1] << q), int(index == desired))
            for index, row in enumerate(rows)
        )
        vector, rank, local_contradictions = gf2_solution(equations)
        contradictions += local_contradictions
        rank_failures += rank != len(rows)
        x = vector & ((1 << q) - 1)
        z = vector >> q
        dual = canonical(x, z)
        duals.append(dual)
        one_hot_failures += sum(
            anticommutes(dual, row) != int(index == desired)
            for index, row in enumerate(rows)
        )
    return tuple(duals), {
        "solve_contradictions": contradictions,
        "solve_rank_failures": rank_failures,
        "one_hot_failures": one_hot_failures,
    }


def pair_same(row: Row, left: int, right: int) -> Row:
    x = (row[1] << left) | (row[1] << right)
    z = (row[2] << left) | (row[2] << right)
    return canonical(x, z)


def conjugate_h(row: Row, qubit: int) -> Row:
    bit = 1 << qubit
    x = int(bool(row[1] & bit))
    z = int(bool(row[2] & bit))
    output_x = (row[1] & ~bit) | (bit if z else 0)
    output_z = (row[2] & ~bit) | (bit if x else 0)
    return (row[0] + 2 * x * z) % 4, output_x, output_z


def conjugate_z_sign(row: Row, qubit: int) -> Row:
    return (row[0] + 2 * ((row[1] >> qubit) & 1)) % 4, row[1], row[2]


def letter_row(qubit: int, letter: str) -> Row:
    if letter == "X":
        return 0, 1 << qubit, 0
    if letter == "Z":
        return 0, 0, 1 << qubit
    if letter == "Y":
        return 1, 1 << qubit, 1 << qubit
    raise ValueError(letter)


def letter_at(row: Row, qubit: int) -> str:
    x = (row[1] >> qubit) & 1
    z = (row[2] >> qubit) & 1
    return ("I", "X", "Z", "Y")[x + 2 * z]


def conjugate_controlled_letter(
    row: Row, control: int, target: int, letter: str
) -> Row:
    if control == target:
        raise ValueError("control equals target")
    local_mask = (1 << control) | (1 << target)
    rest = row[0], row[1] & ~local_mask, row[2] & ~local_mask
    target_pauli = letter_row(target, letter)
    xc_image = multiply((0, 1 << control, 0), target_pauli)
    zc_image: Row = (0, 0, 1 << control)
    xt: Row = (0, 1 << target, 0)
    zt: Row = (0, 0, 1 << target)
    xt_image = multiply(zc_image, xt) if target_pauli[2] & (1 << target) else xt
    zt_image = multiply(zc_image, zt) if target_pauli[1] & (1 << target) else zt
    local: Row = (0, 0, 0)
    if row[1] & (1 << control):
        local = multiply(local, xc_image)
    if row[1] & (1 << target):
        local = multiply(local, xt_image)
    if row[2] & (1 << control):
        local = multiply(local, zc_image)
    if row[2] & (1 << target):
        local = multiply(local, zt_image)
    return multiply(rest, local)


Gate = tuple[str, int] | tuple[str, int, int, str]


def signed_controlled_gates(control: int, row: Row) -> tuple[Gate, ...]:
    gates: list[Gate] = []
    if hermitian_sign(row):
        gates.append(("Z_SIGN", control))
    mask = row[1] | row[2]
    while mask:
        bit = mask & -mask
        qubit = bit.bit_length() - 1
        gates.append(("CP", control, qubit, letter_at(row, qubit)))
        mask ^= bit
    return tuple(gates)


def conjugate_basis(rows: tuple[Row, ...], gates: tuple[Gate, ...]) -> tuple[Row, ...]:
    output = list(rows)
    for gate in gates:
        if gate[0] == "H":
            output = [conjugate_h(row, gate[1]) for row in output]
        elif gate[0] == "Z_SIGN":
            output = [conjugate_z_sign(row, gate[1]) for row in output]
        elif gate[0] == "CP":
            output = [
                conjugate_controlled_letter(row, gate[1], gate[2], gate[3])
                for row in output
            ]
        else:
            raise ValueError(gate)
    return tuple(output)


def channel_word(
    physical: tuple[Row, ...],
    duals: tuple[Row, ...],
    q: int,
    *,
    delete_correction: int | None = None,
    flip_measurement_sign: int | None = None,
) -> tuple[Gate, ...]:
    rank = len(physical)
    gates: list[Gate] = []
    syndrome = 4 * q
    for index, row in enumerate(physical):
        bell = pair_same(row, q, 2 * q)
        if index == flip_measurement_sign:
            bell = (bell[0] + 2) % 4, bell[1], bell[2]
        control = syndrome + index
        gates.append(("H", control))
        gates.extend(signed_controlled_gates(control, bell))
        gates.append(("H", control))
    for index, dual in enumerate(duals):
        if index == delete_correction:
            continue
        gates.extend(signed_controlled_gates(syndrome + index, shift(dual, 0)))
    return tuple(gates)


def output_reference_marginal(
    final: tuple[Row, ...], width: int, q: int
) -> tuple[Row, ...]:
    allowed = ((1 << q) - 1) | (((1 << q) - 1) << (3 * q))
    outside = ((1 << width) - 1) ^ allowed
    outside_vectors = tuple(
        (row[1] & outside) | ((row[2] & outside) << width)
        for row in final
    )
    return tuple(rows_from_mask(final, mask) for mask in relation_masks(outside_vectors))


def channel_failure(
    initial: tuple[Row, ...],
    expected: tuple[Row, ...],
    gates: tuple[Gate, ...],
    width: int,
    q: int,
) -> tuple[int, int]:
    final = conjugate_basis(initial, gates)
    marginal = output_reference_marginal(final, width, q)
    left_binary, left_signed = signed_span_failures(expected, marginal, width)
    right_binary, right_signed = signed_span_failures(marginal, expected, width)
    return left_binary + right_binary, left_signed + right_signed


def exhaustive_channel_mutations(fixture, rows, frames) -> dict[str, object]:
    q = fixture.qubits
    rank = len(rows["physical"])
    width = 4 * q + rank
    baseline_binary = baseline_signed = 0
    dual_solve_contradictions = dual_rank_failures = dual_one_hot_failures = 0
    initial_commutator_failures = 0
    correction_tests = correction_undetected = 0
    sign_tests = sign_undetected = 0
    minimum_correction_failure = None
    minimum_sign_failure = None
    per_frame = []

    for frame_id, frame in enumerate(frames):
        target = target_fixture(fixture, frame)
        target_seed = Q720.transported_seed(frame, ZERO, ORIGINS[0])
        images = physical_images(fixture, target, frame, target_seed)
        physical = tuple(apply_images(row, images) for row in rows["physical"])
        duals, dual_report = private_duals(physical, q)
        dual_solve_contradictions += dual_report["solve_contradictions"]
        dual_rank_failures += dual_report["solve_rank_failures"]
        dual_one_hot_failures += dual_report["one_hot_failures"]

        resource = tuple(pair_same(row, 0, q) for row in physical)
        live_reference = tuple(pair_same(row, 2 * q, 3 * q) for row in physical)
        ancilla = tuple((0, 0, 1 << (4 * q + index)) for index in range(rank))
        expected = tuple(pair_same(row, 0, 3 * q) for row in physical)
        initial = resource + live_reference + ancilla
        initial_commutator_failures += sum(
            anticommutes(initial[left], initial[right])
            for left in range(len(initial))
            for right in range(left)
        )

        binary, signed = channel_failure(
            initial, expected, channel_word(physical, duals, q), width, q
        )
        baseline_binary += binary
        baseline_signed += signed
        local_correction_min = local_sign_min = None
        for index in range(rank):
            correction_failure = sum(channel_failure(
                initial,
                expected,
                channel_word(
                    physical, duals, q, delete_correction=index
                ),
                width,
                q,
            ))
            sign_failure = sum(channel_failure(
                initial,
                expected,
                channel_word(
                    physical, duals, q, flip_measurement_sign=index
                ),
                width,
                q,
            ))
            correction_tests += 1
            sign_tests += 1
            correction_undetected += correction_failure == 0
            sign_undetected += sign_failure == 0
            local_correction_min = (
                correction_failure if local_correction_min is None
                else min(local_correction_min, correction_failure)
            )
            local_sign_min = (
                sign_failure if local_sign_min is None
                else min(local_sign_min, sign_failure)
            )
        minimum_correction_failure = (
            local_correction_min if minimum_correction_failure is None
            else min(minimum_correction_failure, local_correction_min)
        )
        minimum_sign_failure = (
            local_sign_min if minimum_sign_failure is None
            else min(minimum_sign_failure, local_sign_min)
        )
        per_frame.append({
            "frame": frame_id,
            "physical_rank": gf2_rank(
                symplectic_vector(row, q) for row in physical
            ),
            "correction_mutations": rank,
            "sign_mutations": rank,
            "minimum_correction_failure": local_correction_min,
            "minimum_sign_failure": local_sign_min,
        })

    return {
        "frames": len(frames),
        "rank": rank,
        "initial_commutator_failures": initial_commutator_failures,
        "dual_solve_contradictions": dual_solve_contradictions,
        "dual_rank_failures": dual_rank_failures,
        "dual_one_hot_failures": dual_one_hot_failures,
        "baseline_binary_failures": baseline_binary,
        "baseline_signed_failures": baseline_signed,
        "correction_deletions_tested": correction_tests,
        "undetected_correction_deletions": correction_undetected,
        "minimum_detected_correction_failure": minimum_correction_failure,
        "Bell_sign_flips_tested": sign_tests,
        "undetected_Bell_sign_flips": sign_undetected,
        "minimum_detected_Bell_sign_failure": minimum_sign_failure,
        "per_frame": tuple(per_frame),
    }


def opposite_odd_extension_diagnostic(rows, matter_modes: int) -> dict[str, object]:
    even = tuple(pair_same(row, 0, matter_modes) for row in rows["target"])
    odd_positive = canonical(1 | (1 << matter_modes), 0)
    odd_negative = (
        (odd_positive[0] + 2) % 4,
        odd_positive[1],
        odd_positive[2],
    )
    positive = even + (odd_positive,)
    negative = even + (odd_negative,)
    width = 2 * matter_modes
    return {
        "even_algebra_rank": gf2_rank(
            symplectic_vector(row, width) for row in even
        ),
        "positive_extension_rank": gf2_rank(
            symplectic_vector(row, width) for row in positive
        ),
        "negative_extension_rank": gf2_rank(
            symplectic_vector(row, width) for row in negative
        ),
        "odd_representative_is_odd_on_each_half": (
            (odd_positive[1] & ((1 << matter_modes) - 1)).bit_count() & 1,
            ((odd_positive[1] >> matter_modes) & ((1 << matter_modes) - 1)).bit_count() & 1,
        ),
        "odd_extension_commutator_failures": sum(
            anticommutes(odd_positive, row) for row in even
        ),
        "opposite_odd_phase_difference": (
            odd_negative[0] - odd_positive[0]
        ) % 4,
        "even_basis_restriction_mismatches": sum(
            fields(left) != fields(right)
            for left, right in zip(positive[:23], negative[:23])
        ),
        "interpretation": (
            "the two opposite eigenvalue extensions agree on the complete "
            "rank-23 even algebra; this is a parity-superselection diagnostic, "
            "not an odd-frame closure or odd-cocycle claim"
        ),
    }


def main() -> None:
    fixture = O720.arbitrary_fixture(Q720.shape_cells(SHAPE))
    frames = tuple(T708.proper_cubic_frames())
    rows = base_rows(fixture)
    base_rank = gf2_rank(
        symplectic_vector(row, fixture.qubits + fixture.matter_qubits)
        for row in rows["choi"]
    )
    physical_rank = gf2_rank(
        symplectic_vector(row, fixture.qubits) for row in rows["physical"]
    )
    target_rank = gf2_rank(
        symplectic_vector(row, fixture.matter_qubits) for row in rows["target"]
    )

    products = parity_and_product_certificate(fixture, rows, frames)
    channel = exhaustive_channel_mutations(fixture, rows, frames)
    odd = opposite_odd_extension_diagnostic(rows, fixture.matter_qubits)

    checks = {
        "landed_import_boundary": all(
            "scratch" not in path and "cycle813" not in path
            for path in IMPLEMENTATION_IMPORT_PATHS
        ),
        "two_cell_shape_and_rank23": (
            SHAPE == (2, 1, 1)
            and len(fixture.cells) == 2
            and len(fixture.edges) == 1
            and len(rows["choi"]) == 23
            and base_rank == physical_rank == target_rank == 23
        ),
        "all_frame_origin_rows_are_parity_even": (
            products["proper_frames"] == 24
            and products["origin_sectors"] == 8
            and products["frame_origin_contexts"] == 192
            and products["frame_origin_rows_checked"] == 4416
            and products["origin_image_rank_failures"] == 0
            and products["physical_half_parity_even_failures"] == 0
            and products["target_half_parity_even_failures"] == 0
        ),
        "all_13248_signed_products_close_in_all_origins": (
            products["ordered_frame_products"] == 576
            and products["signed_product_comparisons"] == 13248
            and products["origin_expanded_signed_product_comparisons"] == 105984
            and products["binary_product_failures"] == 0
            and products["signed_product_failures"] == 0
            and products["origin_expanded_binary_product_failures"] == 0
            and products["origin_expanded_signed_product_failures"] == 0
        ),
        "rank23_channel_and_private_duals_are_exact": (
            channel["rank"] == 23
            and channel["initial_commutator_failures"] == 0
            and channel["dual_solve_contradictions"] == 0
            and channel["dual_rank_failures"] == 0
            and channel["dual_one_hot_failures"] == 0
            and channel["baseline_binary_failures"] == 0
            and channel["baseline_signed_failures"] == 0
        ),
        "all_correction_and_sign_mutations_are_detected": (
            channel["correction_deletions_tested"] == 552
            and channel["undetected_correction_deletions"] == 0
            and channel["minimum_detected_correction_failure"] > 0
            and channel["Bell_sign_flips_tested"] == 552
            and channel["undetected_Bell_sign_flips"] == 0
            and channel["minimum_detected_Bell_sign_failure"] > 0
        ),
        "opposite_odd_extensions_have_identical_even_restriction": (
            odd["even_algebra_rank"] == 23
            and odd["positive_extension_rank"] == 24
            and odd["negative_extension_rank"] == 24
            and odd["odd_representative_is_odd_on_each_half"] == (1, 1)
            and odd["odd_extension_commutator_failures"] == 0
            and odd["opposite_odd_phase_difference"] == 2
            and odd["even_basis_restriction_mismatches"] == 0
        ),
    }
    artifact = Path(__file__)
    report = {
        "artifact": artifact.name,
        "artifact_sha256": sha256(artifact.read_bytes()).hexdigest(),
        "scope": (
            "independent bounded two-cell parity-superselected even-CAR check; "
            "total parity value is not fixed; no odd closure claim"
        ),
        "landed_inputs": IMPLEMENTATION_IMPORT_PATHS,
        "implementation_route": (
            "landed geometry/images converted immediately to local "
            "(phase,x,z) tuples; all subsequent arithmetic is independent"
        ),
        "shape": SHAPE,
        "cells": len(fixture.cells),
        "edges": len(fixture.edges),
        "physical_M2": fixture.qubits,
        "matter_modes": fixture.matter_qubits,
        "basis_rows": len(rows["choi"]),
        "Choi_rank": base_rank,
        "physical_rank": physical_rank,
        "target_even_algebra_rank": target_rank,
        "parity_and_products": products,
        "rank23_channel_mutations": channel,
        "opposite_odd_extensions": odd,
        "checks": checks,
        "diagnostic_status": "PASS" if all(checks.values()) else "FAIL",
        "claim_verdict": (
            "BOUNDED_TWO_CELL_PARITY_SUPERSELECTED_EVEN_CAR_INDEPENDENT_PASS__"
            "NO_ODD_CLOSURE_CLAIM"
        ),
    }
    print(json.dumps(report, indent=2, sort_keys=True, default=list))
    if not all(checks.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
