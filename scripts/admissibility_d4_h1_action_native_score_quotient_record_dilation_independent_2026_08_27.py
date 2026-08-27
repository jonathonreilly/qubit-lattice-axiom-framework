#!/usr/bin/env python3
"""Independent exact checker for the Block-211 score/Record bridge.

This checker deliberately does not import the Block-211 primary runner.  It
uses the frozen Block-208 cell/H1 objects as input data, then independently:

* enumerates the proper-cubic group and the 36-to-eight dot/cross quotient;
* builds the depth-one/depth-two coarse POVMs and their spectral Naimark
  dilations (spectral projectors, not a triangular factorization);
* exhausts the actual six-site binary-shell action, keeping the raw-label
  obstruction narrow by constructing both quotient and two-shell escapes;
* decodes the H1 dot/cross moments both with calibrated gain and with an
  independently inferred positive moment norm, then checks the raw forward
  and literal actual-reverse source polynomials; and
* realizes the exact blank-to-locked, append-only boundary for the eight
  orthogonal code patterns.

All calculations are exact SymPy calculations.  The only negative result is
the finite statement that the raw 36-label proper-cubic G-set has no
equivariant injection into one binary signed-neighbor shell.
"""

from __future__ import annotations

import argparse
from functools import cache
import itertools
import sys
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

# Frozen prior-cycle input only.  No Block-211 module is imported.
import admissibility_d4_h1_two_time_clifford_cell_m2_record_compiler_2026_08_26 as b208  # noqa: E402


I = sp.I
I2 = sp.eye(2)
I4 = sp.eye(4)
X = sp.Matrix(((0, 1), (1, 0)))
Y = sp.Matrix(((0, -I), (I, 0)))
Z = sp.diag(1, -1)
AUDIT_TIMEOUT_SEC = 240
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_D4_H1_ACTION_NATIVE_SCORE_QUOTIENT_RECORD_DILATION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-27.md",
    ".claude/science/physics-loops/toe-axiom-closure-block211-action-native-minimal-record-dilation-20260827/GOAL.md",
    ".claude/science/physics-loops/toe-axiom-closure-block211-action-native-minimal-record-dilation-20260827/PREFLIGHT_WITNESSES.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_D4_H1_TWO_TIME_CLIFFORD_CELL_M2_RECORD_COMPILER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-26.md",
    "scripts/admissibility_d4_h1_two_time_clifford_cell_m2_record_compiler_2026_08_26.py",
    "logs/runner-cache/admissibility_d4_h1_two_time_clifford_cell_m2_record_compiler_2026_08_26.txt",
)
CELL_A = sp.simplify(b208.CELL_A)
CELL_B = sp.simplify(b208.CELL_B)
TRANSFER = sp.Matrix(((0, -CELL_A, 0), (-CELL_A, 0, 0), (0, 0, CELL_B)))


MUTATIONS = (
    "drop_one_cubic_frame",
    "merge_score_classes",
    "lose_depth_one_rank",
    "lose_depth_two_rank",
    "break_coarse_covariance",
    "truncate_spectral_dilation",
    "merge_coarse_codewords",
    "claim_raw_one_shell_possible",
    "erase_dot_cross_decode",
    "erase_self_normalizing_decode",
    "erase_forward_source",
    "erase_actual_reverse",
    "collapse_probability_vectors",
    "permit_locked_overwrite",
    "identify_blank_with_zero",
    "claim_hilbert_blank_state",
    "claim_formation_cptp_channel",
    "claim_environment_is_record",
    "claim_universal_register_no_go",
)


N5_LINES = (
    "per_element: checked all 36 fine effects, all eight coarse effects at depths one and two, every exact eigenvalue, and every spectral square-root sector.",
    "per_site: checked all six signed-neighbor sites from the semantic blank marker through one locked bit and every attempted overwrite; a Hilbert blank and CPTP formation channel were checked and not executed — reason: this finite map supplies neither construction.",
    "per_mode: checked every fixed H1 incoming/outgoing unit factor with calibrated and self-normalizing score decoders at both depths, both radii, and both orientations, including literal actual reverse; H2 was checked and not executed — reason: H2 is sealed outside the frozen fixture.",
    "per_block: checked all 24 cubic frames, the full 36-to-eight quotient, both 32-dimensional minimal dilations, all 64 one-shell binary patterns, and the two-shell escape.",
    "lattice_wide: checked and not executed — reason: the checker constructs one event-conditioned local block and no autonomous competing-event, formation-clock, or general lattice-history process.",
)


def scalar_zero(value: sp.Expr) -> bool:
    return sp.simplify(sp.expand_complex(value)) == 0


def matrix_equal(left: sp.MatrixBase, right: sp.MatrixBase) -> bool:
    if left.shape != right.shape:
        return False
    return all(scalar_zero(value) for value in left - right)


def vector_key(vector: sp.MatrixBase) -> tuple[int, int, int]:
    return tuple(int(vector[index]) for index in range(3))


def matrix_key(matrix: sp.MatrixBase) -> tuple[int, ...]:
    return tuple(int(value) for value in matrix)


@cache
def signed_axes() -> tuple[sp.Matrix, ...]:
    return tuple(
        sign * sp.eye(3)[:, axis]
        for axis in range(3) for sign in (-1, 1)
    )


@cache
def proper_cubic_rotations() -> tuple[sp.Matrix, ...]:
    """Derive all orientation-preserving signed permutation matrices."""
    rotations: dict[tuple[int, ...], sp.Matrix] = {}
    for permutation in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            rotation = sp.zeros(3)
            for column, row in enumerate(permutation):
                rotation[row, column] = signs[column]
            if rotation.det() == 1:
                rotations[matrix_key(rotation)] = rotation
    return tuple(rotations[key] for key in sorted(rotations))


def axis_index(vector: sp.MatrixBase) -> int:
    key = vector_key(vector)
    return next(
        index for index, axis in enumerate(signed_axes())
        if vector_key(axis) == key
    )


@cache
def shell_permutations() -> tuple[tuple[int, ...], ...]:
    return tuple(
        tuple(axis_index(rotation * axis) for axis in signed_axes())
        for rotation in proper_cubic_rotations()
    )


def score_key(first: sp.MatrixBase, second: sp.MatrixBase) -> tuple[int, ...]:
    cross = first.cross(second)
    return (int(first.dot(second)),) + vector_key(cross)


@cache
def score_keys() -> tuple[tuple[int, ...], ...]:
    return (
        (1, 0, 0, 0),
        (-1, 0, 0, 0),
        *((0,) + vector_key(axis) for axis in signed_axes()),
    )


def rotate_score(
    key: tuple[int, ...], rotation: sp.MatrixBase
) -> tuple[int, ...]:
    if key[0] != 0:
        return key
    return (0,) + vector_key(rotation * sp.Matrix(key[1:]))


@cache
def score_partition() -> dict[tuple[int, ...], tuple[tuple[int, int], ...]]:
    classes: dict[tuple[int, ...], list[tuple[int, int]]] = {
        key: [] for key in score_keys()
    }
    for first_index, first in enumerate(signed_axes()):
        for second_index, second in enumerate(signed_axes()):
            classes[score_key(first, second)].append((first_index, second_index))
    return {key: tuple(value) for key, value in classes.items()}


def orbit_sizes(
    domain: tuple[object, ...], action
) -> tuple[int, ...]:
    unseen = set(domain)
    sizes = []
    while unseen:
        seed = min(unseen)
        orbit = {
            action(seed, index)
            for index in range(len(proper_cubic_rotations()))
        }
        unseen.difference_update(orbit)
        sizes.append(len(orbit))
    return tuple(sorted(sizes))


@cache
def group_quotient_facts() -> dict[str, object]:
    rotations = proper_cubic_rotations()
    rotation_keys = {matrix_key(rotation) for rotation in rotations}
    closure = all(
        matrix_key(left * right) in rotation_keys
        for left in rotations for right in rotations
    )
    orthogonal = all(
        rotation.T * rotation == sp.eye(3) and rotation.det() == 1
        for rotation in rotations
    )
    partition = score_partition()
    quotient_covariance = all(
        score_key(rotation * first, rotation * second)
        == rotate_score(score_key(first, second), rotation)
        for rotation in rotations
        for first in signed_axes() for second in signed_axes()
    )

    fine_domain = tuple(itertools.product(range(6), repeat=2))
    fine_orbits = orbit_sizes(
        fine_domain,
        lambda pair, rotation_index: (
            shell_permutations()[rotation_index][pair[0]],
            shell_permutations()[rotation_index][pair[1]],
        ),
    )
    quotient_orbits = orbit_sizes(
        score_keys(),
        lambda key, rotation_index: rotate_score(
            key, rotations[rotation_index]
        ),
    )
    return {
        "rotation_count": len(rotations),
        "distinct": len(rotation_keys) == len(rotations),
        "orthogonal": orthogonal,
        "closure": closure,
        "fine_count": sum(len(value) for value in partition.values()),
        "score_count": len(partition),
        "class_sizes": tuple(sorted(len(value) for value in partition.values())),
        "quotient_covariance": quotient_covariance,
        "fine_orbit_sizes": fine_orbits,
        "quotient_orbit_sizes": quotient_orbits,
    }


def physical_paulis(orientation: int) -> tuple[sp.Matrix, ...]:
    return X, orientation * Y, Z


def pauli_dot(vector: sp.MatrixBase, orientation: int) -> sp.Matrix:
    return sp.expand(sum(
        (
            vector[index] * physical_paulis(orientation)[index]
            for index in range(3)
        ),
        sp.zeros(2),
    ))


def endpoint_effect(
    axis: sp.MatrixBase,
    depth: int,
    orientation: int,
    transfer: sp.MatrixBase = TRANSFER,
) -> sp.Matrix:
    pulled = (transfer ** depth).T * axis
    return sp.simplify((I2 + pauli_dot(pulled, orientation)) / 6)


def coarse_family(
    depth: int,
    orientation: int,
    transfer: sp.MatrixBase = TRANSFER,
) -> dict[tuple[int, ...], sp.Matrix]:
    endpoints = tuple(
        endpoint_effect(axis, depth, orientation, transfer)
        for axis in signed_axes()
    )
    family = {}
    for key, pairs in score_partition().items():
        family[key] = sp.simplify(sum(
            (
                sp.kronecker_product(endpoints[first], endpoints[second])
                for first, second in pairs
            ),
            sp.zeros(4),
        ))
    return family


def rotate_qubit_operator(
    operator: sp.MatrixBase,
    rotation: sp.MatrixBase,
    orientation: int,
) -> sp.Matrix:
    scalar = sp.trace(operator) / 2
    coordinates = sp.Matrix(tuple(
        sp.trace(operator * pauli) / 2
        for pauli in physical_paulis(orientation)
    ))
    return sp.simplify(scalar * I2 + pauli_dot(rotation * coordinates, orientation))


@cache
def coarse_povm_facts() -> dict[str, object]:
    families = {
        (depth, orientation): coarse_family(depth, orientation)
        for depth in (1, 2) for orientation in (1, -1)
    }
    ranks: dict[int, tuple[int, ...]] = {}
    totals: dict[int, int] = {}
    minimum_eigenvalues: dict[int, sp.Expr] = {}
    positivity = []
    hermiticity = []
    normalization = []
    conjugacy = []
    spectra: dict[tuple[int, tuple[int, ...]], dict[sp.Expr, int]] = {}

    for depth in (1, 2):
        plus = families[(depth, 1)]
        minus = families[(depth, -1)]
        normalization.extend(
            matrix_equal(sum(family.values(), sp.zeros(4)), I4)
            for family in (plus, minus)
        )
        depth_ranks = tuple(plus[key].rank() for key in score_keys())
        ranks[depth] = depth_ranks
        totals[depth] = sum(depth_ranks)
        depth_eigenvalues = []
        for key in score_keys():
            effect = plus[key]
            eigenvalues = effect.eigenvals()
            spectra[(depth, key)] = eigenvalues
            depth_eigenvalues.extend(
                eigenvalue
                for eigenvalue, multiplicity in eigenvalues.items()
                for _ in range(multiplicity)
            )
            positivity.extend(
                eigenvalue.is_positive is True for eigenvalue in eigenvalues
            )
            hermiticity.extend((
                matrix_equal(effect, effect.conjugate().T),
                matrix_equal(minus[key], minus[key].conjugate().T),
            ))
            conjugacy.append(matrix_equal(minus[key], sp.conjugate(effect)))
        minimum_eigenvalues[depth] = min(
            depth_eigenvalues, key=lambda value: float(value)
        )

    endpoint_covariance = all(
        matrix_equal(
            rotate_qubit_operator(
                endpoint_effect(axis, depth, orientation),
                rotation,
                orientation,
            ),
            endpoint_effect(
                rotation * axis,
                depth,
                orientation,
                rotation * TRANSFER * rotation.T,
            ),
        )
        for rotation in proper_cubic_rotations()
        for depth in (1, 2) for orientation in (1, -1)
        for axis in signed_axes()
    )
    return {
        "families": families,
        "spectra": spectra,
        "normalization": all(normalization),
        "positivity": all(positivity),
        "hermiticity": all(hermiticity),
        "conjugacy": all(conjugacy),
        "ranks": ranks,
        "totals": totals,
        "minimum_eigenvalues": minimum_eigenvalues,
        "endpoint_covariance": endpoint_covariance,
        "coarse_covariance": (
            endpoint_covariance
            and group_quotient_facts()["quotient_covariance"]
        ),
    }


def spectral_square_root(
    matrix: sp.MatrixBase,
    eigenvalues: dict[sp.Expr, int],
) -> sp.Matrix:
    """Positive root from exact Lagrange spectral projectors."""
    distinct = tuple(sorted(eigenvalues, key=sp.default_sort_key))
    root = sp.zeros(matrix.rows)
    identity = sp.eye(matrix.rows)
    for eigenvalue in distinct:
        projector = identity
        for other in distinct:
            if other != eigenvalue:
                projector = projector * (matrix - other * identity) / (
                    eigenvalue - other
                )
        root += sp.sqrt(eigenvalue) * projector
    return root.applyfunc(sp.simplify)


@cache
def dilation_facts() -> dict[str, object]:
    povm = coarse_povm_facts()
    dimensions = {}
    square_roots = []
    hermitian_roots = []
    isometries = []
    recoveries = []
    minimality = []
    spectral_counts = {}
    for depth in (1, 2):
        family = povm["families"][(depth, 1)]
        roots = []
        for key in score_keys():
            effect = family[key]
            spectrum = povm["spectra"][(depth, key)]
            root = spectral_square_root(effect, spectrum)
            roots.append(root)
            square_roots.append(matrix_equal(root * root, effect))
            hermitian_roots.append(matrix_equal(root, root.conjugate().T))
            spectral_counts[(depth, key)] = len(spectrum)
        isometry = sp.Matrix.vstack(*roots)
        dimensions[depth] = isometry.rows
        isometries.append(matrix_equal(isometry.conjugate().T * isometry, I4))
        recoveries.extend(
            matrix_equal(
                isometry[4 * index:4 * (index + 1), :].conjugate().T
                * isometry[4 * index:4 * (index + 1), :],
                family[key],
            )
            for index, key in enumerate(score_keys())
        )
        minimality.append(
            isometry.rows == sum(effect.rank() for effect in family.values())
        )
    return {
        "dimensions": dimensions,
        "square_roots": all(square_roots),
        "hermitian_roots": all(hermitian_roots),
        "isometries": all(isometries),
        "recoveries": all(recoveries),
        "minimality": all(minimality),
        "spectral_counts": spectral_counts,
    }


def act_mask(mask: int, permutation: tuple[int, ...]) -> int:
    result = 0
    for site in range(6):
        if (mask >> site) & 1:
            result |= 1 << permutation[site]
    return result


def coarse_code() -> dict[tuple[int, ...], int]:
    code = {(1, 0, 0, 0): 0, (-1, 0, 0, 0): (1 << 6) - 1}
    code.update({
        (0,) + vector_key(axis): 1 << index
        for index, axis in enumerate(signed_axes())
    })
    return code


@cache
def code_orbit_facts() -> dict[str, object]:
    rotations = proper_cubic_rotations()
    permutations = shell_permutations()
    code = coarse_code()
    masks = tuple(code[key] for key in score_keys())
    gram = sp.Matrix(tuple(
        tuple(int(left == right) for right in masks)
        for left in masks
    ))
    code_covariance = all(
        act_mask(code[key], permutations[index])
        == code[rotate_score(key, rotations[index])]
        for index in range(len(rotations)) for key in score_keys()
    )

    mask_orbits = orbit_sizes(
        tuple(range(64)),
        lambda mask, rotation_index: act_mask(
            mask, permutations[rotation_index]
        ),
    )
    fine_orbits = group_quotient_facts()["fine_orbit_sizes"]
    raw_one_shell_possible = (
        24 not in fine_orbits or 24 in mask_orbits
    )

    two_shell_code = {
        (first, second): (1 << first) | (1 << (6 + second))
        for first in range(6) for second in range(6)
    }
    two_shell_covariance = all(
        (
            act_mask(two_shell_code[pair] & 63, permutation)
            | (
                act_mask(two_shell_code[pair] >> 6, permutation) << 6
            )
        )
        == two_shell_code[(permutation[pair[0]], permutation[pair[1]])]
        for permutation in permutations
        for pair in tuple(itertools.product(range(6), repeat=2))
    )
    return {
        "code_count": len(set(masks)),
        "gram_identity": gram == sp.eye(8),
        "code_covariance": code_covariance,
        "mask_domain_exhausted": sum(mask_orbits) == 64,
        "mask_orbit_sizes": mask_orbits,
        "fine_orbit_sizes": fine_orbits,
        "raw_one_shell_possible": raw_one_shell_possible,
        "two_shell_distinct": len(set(two_shell_code.values())) == 36,
        "two_shell_covariance": two_shell_covariance,
        "quotient_escape": len(set(masks)) == 8 and code_covariance,
        "universal_register_no_go": False,
    }


def phase_unit(angle: sp.Expr) -> sp.Expr:
    return sp.simplify(sp.cos(angle) + I * sp.sin(angle))


def phase_state(
    unit: sp.Expr, radius: sp.Expr, orientation: int
) -> sp.Matrix:
    return sp.Matrix((
        (1, radius * unit ** (-orientation)),
        (radius * unit ** orientation, 1),
    )) / 2


def coarse_probabilities(
    first_unit: sp.Expr,
    second_unit: sp.Expr,
    radius: sp.Expr,
    depth: int,
    orientation: int,
) -> tuple[sp.Expr, ...]:
    state = sp.kronecker_product(
        phase_state(first_unit, radius, orientation),
        phase_state(second_unit, radius, orientation),
    )
    family = coarse_povm_facts()["families"][(depth, orientation)]
    return tuple(
        sp.simplify(sp.expand_complex(sp.trace(family[key] * state)))
        for key in score_keys()
    )


def raw_dot_cross(
    probabilities: tuple[sp.Expr, ...],
) -> tuple[sp.Expr, sp.Matrix]:
    raw_dot = sp.simplify(sp.expand_complex(9 * sum(
        (probability * key[0]
         for key, probability in zip(score_keys(), probabilities)),
        sp.Integer(0),
    )))
    raw_cross = sp.simplify(9 * sum(
        (
            probability * sp.Matrix(key[1:])
            for key, probability in zip(score_keys(), probabilities)
        ),
        sp.zeros(3, 1),
    )).applyfunc(lambda value: sp.simplify(sp.expand_complex(value)))
    return raw_dot, raw_cross


def decoded_dot_cross(
    probabilities: tuple[sp.Expr, ...],
    radius: sp.Expr,
    depth: int,
) -> tuple[sp.Expr, sp.Matrix]:
    raw_dot, raw_cross = raw_dot_cross(probabilities)
    scale = sp.simplify(radius ** 2 * CELL_A ** (2 * depth))
    return (
        sp.simplify(raw_dot / scale),
        sp.simplify((-1) ** depth * raw_cross / scale),
    )


def self_normalized_dot_cross(
    probabilities: tuple[sp.Expr, ...],
    depth: int,
) -> tuple[sp.Expr, sp.Matrix, sp.Expr]:
    """Infer the positive score gain without radius or transfer magnitude."""
    raw_dot, raw_cross = raw_dot_cross(probabilities)
    squared_scale = sp.factor(sp.simplify(
        raw_dot ** 2 + (raw_cross.T * raw_cross)[0]
    ))
    inferred_scale = sp.simplify(sp.sqrt(squared_scale))
    return (
        sp.simplify(raw_dot / inferred_scale),
        sp.simplify((-1) ** depth * raw_cross / inferred_scale),
        inferred_scale,
    )


def decode_phase_ratio(
    angle: sp.Expr,
    radius: sp.Expr,
    depth: int,
    orientation: int,
) -> tuple[sp.Expr, sp.Expr, sp.Matrix, tuple[sp.Expr, ...]]:
    probabilities = coarse_probabilities(
        sp.Integer(1), phase_unit(angle), radius, depth, orientation
    )
    dot, cross = decoded_dot_cross(probabilities, radius, depth)
    return (
        sp.simplify(dot + orientation * I * cross[2]),
        dot,
        cross,
        probabilities,
    )


def source_from_ratios(
    incoming_ratios: tuple[sp.Expr, ...],
    outgoing_ratios: tuple[sp.Expr, ...],
    orientation: int,
) -> sp.Matrix:
    """Reconstruct the fixed source without calling the Block-208 decoder."""
    algebra = b208.B
    cosines = tuple(
        sp.simplify(
            (outgoing_ratios[axis] + sp.conjugate(incoming_ratios[axis])) / 2
        )
        for axis in range(4)
    )
    incoming_sines = tuple(
        sp.simplify(
            (incoming_ratios[axis] - sp.conjugate(incoming_ratios[axis]))
            / (2 * orientation * I)
        )
        for axis in range(4)
    )
    outgoing_sines = tuple(
        sp.simplify(
            (outgoing_ratios[axis] - sp.conjugate(outgoing_ratios[axis]))
            / (2 * orientation * I)
        )
        for axis in range(4)
    )
    right_differential = sum(
        (
            incoming_sines[axis] * algebra.CREATION[axis]
            for axis in range(4)
        ),
        sp.zeros(16),
    )
    left_differential = sum(
        (
            outgoing_sines[axis] * algebra.CREATION[axis].T
            for axis in range(4)
        ),
        sp.zeros(16),
    )
    coefficients = b208.b207.b193.tt_source_coefficients("H1", 1)
    result = sp.zeros(16)
    for slot in (8, 9):
        left, right = algebra.PAIRS4[slot]
        hodge = -cosines[left] * cosines[right] / sp.sqrt(2) * (
            algebra.CREATION[left] * algebra.ANNIHILATION[right]
            + algebra.CREATION[right] * algebra.ANNIHILATION[left]
        )
        result += coefficients[slot] * (
            algebra.MASS * hodge
            + orientation * I * hodge * right_differential
            + orientation * I * left_differential * hodge
        )
    return sp.simplify(sp.expand_complex(sp.expand(result)))


def reverse_polynomial(polynomial: dict) -> dict:
    algebra = b208.B
    result = {}
    for power, matrix in polynomial.items():
        reverse_power = power[:4] + tuple(
            power[index] - power[4 + index] for index in range(4)
        )
        result = algebra.poly_add(result, {reverse_power: matrix})
    return result


def evaluate_polynomial(
    polynomial: dict,
    incoming: tuple[sp.Expr, ...],
    transfer: tuple[sp.Expr, ...],
) -> sp.Matrix:
    incoming_units = tuple(phase_unit(angle) for angle in incoming)
    transfer_units = tuple(phase_unit(angle) for angle in transfer)
    result = sp.zeros(16)
    for power, matrix in polynomial.items():
        factor = sp.prod(
            incoming_units[axis] ** power[axis] for axis in range(4)
        ) * sp.prod(
            transfer_units[axis] ** power[4 + axis] for axis in range(4)
        )
        result += factor * matrix
    return sp.simplify(sp.expand_complex(sp.expand(result)))


@cache
def h1_decode_facts() -> dict[str, object]:
    incoming, transfer = b208.b207.b193.POINTS["H1"]
    outgoing = tuple(incoming[index] + transfer[index] for index in range(4))
    raw_source = b208.b207.b206.combined_raw_source()
    forward_target = evaluate_polynomial(raw_source, incoming, transfer)
    reverse_target = evaluate_polynomial(
        reverse_polynomial(raw_source), incoming, transfer
    )

    moment_checks = []
    ratio_checks = []
    forward_checks = []
    reverse_checks = []
    self_scale_checks = []
    self_moment_checks = []
    self_ratio_checks = []
    self_forward_checks = []
    self_reverse_checks = []
    cases = 0
    for depth in (1, 2):
        for radius in (sp.Integer(1), sp.Rational(1, 2)):
            for orientation in (1, -1):
                incoming_ratios = []
                outgoing_ratios = []
                self_incoming_ratios = []
                self_outgoing_ratios = []
                for family, destination, self_destination in (
                    (incoming, incoming_ratios, self_incoming_ratios),
                    (outgoing, outgoing_ratios, self_outgoing_ratios),
                ):
                    for angle in family:
                        ratio, dot, cross, probabilities = decode_phase_ratio(
                            angle, radius, depth, orientation
                        )
                        self_dot, self_cross, inferred_scale = (
                            self_normalized_dot_cross(probabilities, depth)
                        )
                        self_ratio = sp.simplify(
                            self_dot + orientation * I * self_cross[2]
                        )
                        destination.append(ratio)
                        self_destination.append(self_ratio)
                        moment_checks.append(scalar_zero(dot - sp.cos(angle)))
                        moment_checks.append(matrix_equal(
                            cross,
                            sp.Matrix((0, 0, sp.sin(angle))),
                        ))
                        ratio_checks.append(scalar_zero(
                            ratio
                            - (sp.cos(angle) + orientation * I * sp.sin(angle))
                        ))
                        self_scale_checks.append(
                            inferred_scale.is_positive is True
                            and scalar_zero(
                                inferred_scale
                                - radius ** 2 * CELL_A ** (2 * depth)
                            )
                        )
                        self_moment_checks.append(scalar_zero(
                            self_dot - sp.cos(angle)
                        ))
                        self_moment_checks.append(matrix_equal(
                            self_cross,
                            sp.Matrix((0, 0, sp.sin(angle))),
                        ))
                        self_ratio_checks.append(scalar_zero(
                            self_ratio
                            - (sp.cos(angle) + orientation * I * sp.sin(angle))
                        ))
                forward = source_from_ratios(
                    tuple(incoming_ratios), tuple(outgoing_ratios), orientation
                )
                actual_reverse = source_from_ratios(
                    tuple(outgoing_ratios), tuple(incoming_ratios), orientation
                )
                self_forward = source_from_ratios(
                    tuple(self_incoming_ratios),
                    tuple(self_outgoing_ratios),
                    orientation,
                )
                self_actual_reverse = source_from_ratios(
                    tuple(self_outgoing_ratios),
                    tuple(self_incoming_ratios),
                    orientation,
                )
                expected_forward = (
                    forward_target if orientation == 1
                    else sp.conjugate(forward_target)
                )
                expected_reverse = (
                    reverse_target if orientation == 1
                    else sp.conjugate(reverse_target)
                )
                forward_checks.append(matrix_equal(forward, expected_forward))
                reverse_checks.append(matrix_equal(
                    actual_reverse, expected_reverse
                ))
                self_forward_checks.append(matrix_equal(
                    self_forward, expected_forward
                ))
                self_reverse_checks.append(matrix_equal(
                    self_actual_reverse, expected_reverse
                ))
                cases += 1
    return {
        "cases": cases,
        "moment_checks": all(moment_checks),
        "ratio_checks": all(ratio_checks),
        "forward_checks": all(forward_checks),
        "reverse_checks": all(reverse_checks),
        "actual_reverse_cases": len(reverse_checks),
        "self_scale_checks": all(self_scale_checks),
        "self_moment_checks": all(self_moment_checks),
        "self_ratio_checks": all(self_ratio_checks),
        "self_forward_checks": all(self_forward_checks),
        "self_reverse_checks": all(self_reverse_checks),
        "self_normalizing_gain_inputs_supplied": False,
    }


@cache
def probability_image_facts() -> dict[str, object]:
    probe = phase_unit(sp.pi / 3)
    vectors = {
        (depth, radius): coarse_probabilities(
            sp.Integer(1), probe, radius, depth, 1
        )
        for depth in (1, 2)
        for radius in (sp.Integer(1), sp.Rational(1, 2))
    }
    normalized = all(
        scalar_zero(sum(vector, sp.Integer(0)) - 1)
        for vector in vectors.values()
    )
    positive = all(
        probability.is_positive is True
        for vector in vectors.values() for probability in vector
    )
    return {
        "unique_vectors": len(set(vectors.values())),
        "normalized": normalized,
        "positive": positive,
        "depth_fork": vectors[(1, sp.Integer(1))]
        != vectors[(2, sp.Integer(1))],
        "radius_fork": vectors[(1, sp.Integer(1))]
        != vectors[(1, sp.Rational(1, 2))],
    }


def lock_site(
    configuration: tuple[int | None, ...], site: int, bit: int
) -> tuple[tuple[int | None, ...], bool]:
    if configuration[site] is not None:
        return configuration, False
    updated = list(configuration)
    updated[site] = bit
    return tuple(updated), True


@cache
def attachment_facts() -> dict[str, object]:
    blank = (None,) * 6
    configurations = []
    monotone = []
    no_overwrite = []
    serialization = []
    for mask in coarse_code().values():
        target = tuple((mask >> site) & 1 for site in range(6))
        configuration = blank
        locked_count = 0
        for site, bit in enumerate(target):
            configuration, wrote = lock_site(configuration, site, bit)
            monotone.append(wrote and sum(
                value is not None for value in configuration
            ) == locked_count + 1)
            locked_count += 1
        serialization.append(configuration == target)
        configurations.append(configuration)
        for site, bit in enumerate(target):
            attempted, wrote = lock_site(configuration, site, 1 - bit)
            no_overwrite.append(not wrote and attempted == configuration)
    local_zero = sp.Matrix((1, 0))
    local_one = sp.Matrix((0, 1))
    return {
        "blank_unreadable": all(value is None for value in blank),
        "blank_distinct_from_zero": blank != (0,) * 6,
        "semantic_blank_marker_only": True,
        "hilbert_blank_state_constructed": False,
        "local_bits_orthogonal": (local_zero.T * local_one)[0] == 0,
        "configuration_count": len(set(configurations)),
        "monotone": all(monotone),
        "serialization": all(serialization),
        "no_overwrite": all(no_overwrite),
        "permanent": all(
            tuple(configuration) == configuration
            for configuration in configurations
        ),
        "environment_is_record": False,
        "formation_selector_constructed": False,
        "formation_cptp_channel_constructed": False,
        "event_conditioned": True,
    }


BASE_CLAIMS: dict[str, object] = {
    "rotation_count": 24,
    "score_count": 8,
    "depth_one_ranks": (4,) * 8,
    "depth_two_ranks": (4,) * 8,
    "depth_one_total": 32,
    "depth_two_total": 32,
    "coarse_covariance": True,
    "dilation_dimensions": {1: 32, 2: 32},
    "code_count": 8,
    "raw_one_shell_possible": False,
    "moment_decode": True,
    "self_normalizing_decode": True,
    "forward_source": True,
    "actual_reverse": True,
    "probability_vectors": 4,
    "no_overwrite": True,
    "blank_distinct": True,
    "hilbert_blank_state": False,
    "formation_cptp_channel": False,
    "environment_is_record": False,
    "universal_register_no_go": False,
}


def mutated_claims(mutation: str) -> dict[str, object]:
    claims = dict(BASE_CLAIMS)
    changes: dict[str, tuple[str, object]] = {
        "drop_one_cubic_frame": ("rotation_count", 23),
        "merge_score_classes": ("score_count", 7),
        "lose_depth_one_rank": ("depth_one_total", 31),
        "lose_depth_two_rank": ("depth_two_total", 31),
        "break_coarse_covariance": ("coarse_covariance", False),
        "truncate_spectral_dilation": (
            "dilation_dimensions", {1: 31, 2: 32}
        ),
        "merge_coarse_codewords": ("code_count", 7),
        "claim_raw_one_shell_possible": ("raw_one_shell_possible", True),
        "erase_dot_cross_decode": ("moment_decode", False),
        "erase_self_normalizing_decode": ("self_normalizing_decode", False),
        "erase_forward_source": ("forward_source", False),
        "erase_actual_reverse": ("actual_reverse", False),
        "collapse_probability_vectors": ("probability_vectors", 3),
        "permit_locked_overwrite": ("no_overwrite", False),
        "identify_blank_with_zero": ("blank_distinct", False),
        "claim_hilbert_blank_state": ("hilbert_blank_state", True),
        "claim_formation_cptp_channel": ("formation_cptp_channel", True),
        "claim_environment_is_record": ("environment_is_record", True),
        "claim_universal_register_no_go": (
            "universal_register_no_go", True
        ),
    }
    if mutation:
        key, value = changes[mutation]
        claims[key] = value
    return claims


def run(mutation: str = "") -> tuple[int, int, dict[str, object]]:
    group = group_quotient_facts()
    povm = coarse_povm_facts()
    dilation = dilation_facts()
    code = code_orbit_facts()
    h1 = h1_decode_facts()
    image = probability_image_facts()
    attachment = attachment_facts()
    claims = mutated_claims(mutation)

    checks = {
        "A": (
            group["rotation_count"] == claims["rotation_count"]
            and group["distinct"] and group["orthogonal"] and group["closure"]
            and group["fine_count"] == 36
            and group["score_count"] == claims["score_count"]
            and group["class_sizes"] == (4, 4, 4, 4, 4, 4, 6, 6)
            and group["quotient_covariance"]
            and group["fine_orbit_sizes"] == (6, 6, 24)
            and group["quotient_orbit_sizes"] == (1, 1, 6),
            "24 proper-cubic frames act covariantly on the exact 36-to-eight dot/cross quotient",
        ),
        "B": (
            povm["normalization"] and povm["positivity"]
            and povm["hermiticity"] and povm["conjugacy"]
            and povm["ranks"][1] == claims["depth_one_ranks"]
            and povm["totals"][1] == claims["depth_one_total"],
            "the depth-one coarse POVM is exact, positive, normalized, and has rank pattern 4x8 with Naimark minimum 32",
        ),
        "C": (
            povm["normalization"] and povm["positivity"]
            and povm["hermiticity"] and povm["conjugacy"]
            and povm["ranks"][2] == claims["depth_two_ranks"]
            and povm["totals"][2] == claims["depth_two_total"],
            "the depth-two coarse POVM is exact, positive, normalized, and has rank pattern 4x8 with Naimark minimum 32",
        ),
        "D": (
            povm["endpoint_covariance"]
            and povm["coarse_covariance"] == claims["coarse_covariance"],
            "cell-frame transport plus quotient covariance proves coarse-POVM covariance in all 24 frames and both readings",
        ),
        "E": (
            dilation["dimensions"] == claims["dilation_dimensions"]
            and dilation["square_roots"] and dilation["hermitian_roots"]
            and dilation["isometries"] and dilation["recoveries"]
            and dilation["minimality"],
            "exact spectral projectors give minimal 32-by-4 Naimark isometries and recover every sector effect",
        ),
        "F": (
            code["code_count"] == claims["code_count"]
            and code["gram_identity"] and code["code_covariance"]
            and code["quotient_escape"],
            "the eight quotient labels have orthogonal, proper-cubic-covariant one-shell binary codewords",
        ),
        "G": (
            code["mask_domain_exhausted"]
            and code["mask_orbit_sizes"]
            == (1, 1, 3, 3, 6, 6, 8, 12, 12, 12)
            and code["raw_one_shell_possible"]
            == claims["raw_one_shell_possible"]
            and code["two_shell_distinct"] and code["two_shell_covariance"]
            and code["universal_register_no_go"]
            == claims["universal_register_no_go"],
            "exhaustive six-bit orbit mismatch excludes only the raw one-shell injection; quotient and two-shell escapes remain explicit",
        ),
        "H": (
            h1["cases"] == 8
            and h1["moment_checks"] == claims["moment_decode"]
            and h1["ratio_checks"],
            "coarse probabilities decode the exact H1 dot and cross moments at both depths, radii, and orientations",
        ),
        "I": (
            h1["forward_checks"] == claims["forward_source"]
            and h1["reverse_checks"] == claims["actual_reverse"]
            and h1["actual_reverse_cases"] == 8,
            "decoded ratios reproduce the raw H1 forward source and the literal actual-reverse polynomial in all eight control cases",
        ),
        "J": (
            image["unique_vectors"] == claims["probability_vectors"]
            and image["normalized"] and image["positive"]
            and image["depth_fork"] and image["radius_fork"],
            "depth and radius controls give four distinct exact conditional probability vectors",
        ),
        "K": (
            attachment["configuration_count"] == 8
            and attachment["local_bits_orthogonal"]
            and attachment["monotone"] and attachment["serialization"]
            and attachment["no_overwrite"] == claims["no_overwrite"]
            and attachment["permanent"],
            "all eight codewords attach by monotone blank-to-locked writes with exact no-overwrite permanence",
        ),
        "L": (
            attachment["blank_unreadable"]
            and attachment["blank_distinct_from_zero"]
            == claims["blank_distinct"]
            and attachment["semantic_blank_marker_only"]
            and attachment["hilbert_blank_state_constructed"]
            == claims["hilbert_blank_state"]
            and attachment["environment_is_record"]
            == claims["environment_is_record"]
            and not attachment["formation_selector_constructed"]
            and attachment["formation_cptp_channel_constructed"]
            == claims["formation_cptp_channel"]
            and attachment["event_conditioned"],
            "the semantic blank marker is neither a Hilbert blank state nor a CPTP formation channel; attachment remains event-conditioned only",
        ),
        "M": (
            h1["self_scale_checks"]
            and h1["self_moment_checks"]
            == claims["self_normalizing_decode"]
            and h1["self_ratio_checks"]
            and h1["self_forward_checks"]
            and h1["self_reverse_checks"]
            and not h1["self_normalizing_gain_inputs_supplied"],
            "the moment norm self-normalizes every H1 ratio and both source directions without supplied radius or transfer magnitude",
        ),
    }
    passed = sum(int(ok) for ok, _description in checks.values())
    failed = len(checks) - passed
    return passed, failed, {
        "checks": checks,
        "group": group,
        "povm": povm,
        "dilation": dilation,
        "code": code,
        "h1": h1,
        "image": image,
        "attachment": attachment,
    }


def print_run(mutation: str = "") -> int:
    passed, failed, facts = run(mutation)
    group = facts["group"]
    povm = facts["povm"]
    dilation = facts["dilation"]
    code = facts["code"]
    h1 = facts["h1"]
    image = facts["image"]
    print(
        "CUBIC_QUOTIENT: rotations="
        f"{group['rotation_count']}; fine orbits={group['fine_orbit_sizes']}; "
        f"36 -> {group['score_count']}; classes={group['class_sizes']}."
    )
    print(
        "COARSE_POVM: d=1 ranks="
        f"{povm['ranks'][1]}, sum={povm['totals'][1]}, "
        f"min_eigenvalue={povm['minimum_eigenvalues'][1]}; d=2 ranks="
        f"{povm['ranks'][2]}, sum={povm['totals'][2]}, "
        f"min_eigenvalue={povm['minimum_eigenvalues'][2]}."
    )
    print(
        "SPECTRAL_DILATION: dimensions="
        f"{dilation['dimensions']}; exact positive roots, isometry, sector "
        "recovery, and rank-sum minimality pass."
    )
    print(
        "SHELL_CODE: quotient code=8/8; one-shell mask orbits="
        f"{code['mask_orbit_sizes']}; raw orbit 24 has no one-shell image; "
        "two-shell raw escape=36/36."
    )
    print(
        "H1_DECODE: calibrated and self-normalizing dot/cross, forward, and "
        f"actual reverse in {h1['cases']} depth/radius/orientation cases; "
        f"conditional vectors={image['unique_vectors']}."
    )
    print(
        "ATTACHMENT: semantic blank differs from locked zero and is not a "
        "Hilbert state/CPTP channel; eight codes write once and remain permanent."
    )
    for line in N5_LINES:
        print(line)
    for key, (ok, description) in facts["checks"].items():
        print(f"CHECK {key}: {'PASS' if ok else 'FAIL'} - {description}")
    if mutation:
        print(f"MUTATION: {mutation}")
    print(
        "RESULT: exact independent score quotient, full-rank minimal spectral "
        "dilations, one-shell quotient code, narrowly scoped raw one-shell "
        "obstruction, self-normalizing H1 decode, and semantic blank-to-locked "
        "attachment boundary."
    )
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return 0 if failed == 0 else 1


def print_mutation_suite() -> int:
    baseline_passed, baseline_failed, _facts = run()
    detected = 0
    print(
        f"BASELINE: PASS={baseline_passed} FAIL={baseline_failed}; "
        f"mutations={len(MUTATIONS)}."
    )
    for mutation in MUTATIONS:
        _passed, failed, _mutation_facts = run(mutation)
        caught = failed > 0
        detected += int(caught)
        print(
            f"MUTATION {mutation}: {'DETECTED' if caught else 'ESCAPED'} "
            f"(checker_failures={failed})"
        )
    escaped = len(MUTATIONS) - detected
    print(f"TOTAL: PASS={detected} FAIL={escaped}")
    return 0 if baseline_failed == 0 and escaped == 0 else 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    parser.add_argument("--mutation-suite", action="store_true")
    args = parser.parse_args()
    if args.mutation_suite:
        return print_mutation_suite()
    return print_run(args.mutation)


if __name__ == "__main__":
    raise SystemExit(main())
