#!/usr/bin/env python3
"""
Independent witnesses for the finite Wilson transfer/source theorem.

The companion note contains the exact SU(N) proof.  This runner keeps the
exact SU(3) character recurrence visible and builds a separate finite-group
one-plaquette lattice witness with:

* a genuine gauge-invariant positive transfer kernel;
* trace/path-sum identities;
* spatial multiplication insertions;
* mixed two-slice source kernels and their Schur-power derivatives; and
* hostile controls for the old pointwise-positivity argument, recurrence
  boundaries, plaquette word, slice placement, half-weight, and Haar
  normalization.

The S3 carrier and all floating evaluations below are SUPPORT for the exact
SU(N) proof, not replacements for it.
"""

from __future__ import annotations

import cmath
import math
from collections import defaultdict
from itertools import permutations, product

import numpy as np


THEOREM_PASS = 0
SUPPORT_PASS = 0
FAIL = 0

NMAX_TENSOR = 8
RECURRENCE_BOX = 5
GRAM_SIZE = 18
GRAM_BETA = 1.7
S3_MIXED_COUPLING = 0.61
S3_SPATIAL_COUPLING = 0.37
S3_SPATIAL_SOURCE = -0.29
S3_MIXED_SOURCE = 0.23
S3_LT = 3
TOL = 3.0e-11

TORUS_SAMPLES = [
    (0.37, -0.91),
    (1.11, 0.43),
    (-0.64, 1.27),
    (0.82, -1.44),
]


def check(name: str, condition: bool, detail: str = "", bucket: str = "SUPPORT") -> None:
    global THEOREM_PASS, SUPPORT_PASS, FAIL
    status = "PASS" if condition else "FAIL"
    if condition:
        if bucket == "SUPPORT":
            SUPPORT_PASS += 1
        else:
            THEOREM_PASS += 1
    else:
        FAIL += 1
    print(f"  [{status}] [{bucket}] {name}")
    if detail:
        print(f"         {detail}")


# ---------------------------------------------------------------------------
# Exact SU(3) representation-ring and recurrence data
# ---------------------------------------------------------------------------


def su3_dimension(weight: tuple[int, int]) -> int:
    p, q = weight
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def fundamental_neighbors(weight: tuple[int, int]) -> list[tuple[int, int]]:
    p, q = weight
    out = [(p + 1, q)]
    if p > 0:
        out.append((p - 1, q + 1))
    if q > 0:
        out.append((p, q - 1))
    return out


def antifundamental_neighbors(weight: tuple[int, int]) -> list[tuple[int, int]]:
    p, q = weight
    out = [(p, q + 1)]
    if q > 0:
        out.append((p + 1, q - 1))
    if p > 0:
        out.append((p - 1, q))
    return out


def recurrence_neighbors(weight: tuple[int, int]) -> list[tuple[int, int]]:
    return fundamental_neighbors(weight) + antifundamental_neighbors(weight)


def unpruned_recurrence_neighbors(
    weight: tuple[int, int],
) -> list[tuple[int, int]]:
    p, q = weight
    return [
        (p + 1, q),
        (p - 1, q + 1),
        (p, q - 1),
        (p, q + 1),
        (p + 1, q - 1),
        (p - 1, q),
    ]


def tensor_multiplicities(nmax: int) -> list[dict[tuple[int, int], int]]:
    levels: list[dict[tuple[int, int], int]] = [{(0, 0): 1}]
    for _ in range(nmax):
        next_level: defaultdict[tuple[int, int], int] = defaultdict(int)
        for weight, multiplicity in levels[-1].items():
            for target in recurrence_neighbors(weight):
                next_level[target] += multiplicity
        levels.append(dict(next_level))
    return levels


def truncated_wilson_coefficients(
    levels: list[dict[tuple[int, int], int]], beta: float
) -> dict[tuple[int, int], float]:
    coefficients: defaultdict[tuple[int, int], float] = defaultdict(float)
    t = beta / 6.0
    for n, level in enumerate(levels):
        scale = t**n / math.factorial(n)
        for weight, multiplicity in level.items():
            coefficients[weight] += scale * multiplicity
    return dict(coefficients)


def torus_point(theta1: float, theta2: float) -> np.ndarray:
    return np.array(
        [
            cmath.exp(1j * theta1),
            cmath.exp(1j * theta2),
            cmath.exp(-1j * (theta1 + theta2)),
        ],
        dtype=complex,
    )


def su3_character(p: int, q: int, z: np.ndarray) -> complex:
    lam = [p + q, q, 0]
    numerator = np.array(
        [[z[i] ** (lam[j] + 2 - j) for j in range(3)] for i in range(3)],
        dtype=complex,
    )
    denominator = np.array(
        [[z[i] ** (2 - j) for j in range(3)] for i in range(3)],
        dtype=complex,
    )
    return np.linalg.det(numerator) / np.linalg.det(denominator)


def recurrence_matrix(nmax: int) -> np.ndarray:
    weights = list(product(range(nmax + 1), repeat=2))
    index = {weight: i for i, weight in enumerate(weights)}
    matrix = np.zeros((len(weights), len(weights)), dtype=float)
    for weight, column in index.items():
        for target in recurrence_neighbors(weight):
            if target in index:
                matrix[index[target], column] += 1.0 / 6.0
    return matrix


def recurrence_errors() -> tuple[float, float, float]:
    fundamental_error = 0.0
    antifundamental_error = 0.0
    combined_error = 0.0
    for theta1, theta2 in TORUS_SAMPLES:
        z = torus_point(theta1, theta2)
        chi_3 = su3_character(1, 0, z)
        chi_3bar = su3_character(0, 1, z)
        source = (chi_3 + chi_3bar) / 6.0
        for p, q in product(range(4), repeat=2):
            chi = su3_character(p, q, z)
            rhs_3 = sum(
                su3_character(a, b, z)
                for a, b in fundamental_neighbors((p, q))
            )
            rhs_3bar = sum(
                su3_character(a, b, z)
                for a, b in antifundamental_neighbors((p, q))
            )
            fundamental_error = max(fundamental_error, abs(chi_3 * chi - rhs_3))
            antifundamental_error = max(
                antifundamental_error, abs(chi_3bar * chi - rhs_3bar)
            )
            combined_error = max(
                combined_error, abs(source * chi - (rhs_3 + rhs_3bar) / 6.0)
            )
    return fundamental_error, antifundamental_error, combined_error


def haar_su3_samples(count: int, seed: int = 20260716) -> list[np.ndarray]:
    rng = np.random.default_rng(seed)
    samples: list[np.ndarray] = []
    for _ in range(count):
        gaussian = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
        q, r = np.linalg.qr(gaussian)
        phases = np.diag(r)
        phases = phases / np.abs(phases)
        unitary = q @ np.diag(np.conjugate(phases))
        unitary = unitary / np.linalg.det(unitary) ** (1.0 / 3.0)
        samples.append(unitary)
    return samples


def wilson_gram(samples: list[np.ndarray], beta: float) -> np.ndarray:
    size = len(samples)
    gram = np.zeros((size, size), dtype=float)
    for i, left in enumerate(samples):
        for j, right in enumerate(samples):
            difference = left @ right.conj().T
            gram[i, j] = math.exp(beta * float(np.trace(difference).real) / 3.0)
    return gram


# ---------------------------------------------------------------------------
# Exact finite S3 one-plaquette spatial carrier
# ---------------------------------------------------------------------------


Permutation = tuple[int, int, int]


def permutation_compose(left: Permutation, right: Permutation) -> Permutation:
    return tuple(left[right[i]] for i in range(3))


def permutation_inverse(permutation: Permutation) -> Permutation:
    inverse = [0, 0, 0]
    for i, image in enumerate(permutation):
        inverse[image] = i
    return tuple(inverse)


def permutation_sign(permutation: Permutation) -> int:
    inversions = sum(
        permutation[i] > permutation[j] for i in range(3) for j in range(i + 1, 3)
    )
    return -1 if inversions % 2 else 1


def standard_character(permutation: Permutation) -> int:
    return sum(permutation[i] == i for i in range(3)) - 1


def normalized_standard_character(permutation: Permutation) -> float:
    return standard_character(permutation) / 2.0


S3: list[Permutation] = list(permutations(range(3)))
S3_INDEX = {permutation: i for i, permutation in enumerate(S3)}
S3_ORDER = len(S3)

# Square vertices 0,1,2,3 and positively stored edges
# e0: 0->1, e1: 1->2, e2: 3->2, e3: 0->3.
SQUARE_EDGES = [(0, 1), (1, 2), (3, 2), (0, 3)]
S3_CONFIGURATIONS = list(product(S3, repeat=4))
S3_CONFIG_COUNT = len(S3_CONFIGURATIONS)


def plaquette_holonomy(configuration: tuple[Permutation, ...]) -> Permutation:
    return permutation_compose(
        permutation_compose(configuration[0], configuration[1]),
        permutation_compose(
            permutation_inverse(configuration[2]),
            permutation_inverse(configuration[3]),
        ),
    )


def wrong_plaquette_word(configuration: tuple[Permutation, ...]) -> Permutation:
    return permutation_compose(
        permutation_compose(configuration[0], configuration[1]),
        permutation_compose(configuration[2], configuration[3]),
    )


def gauge_transform_configuration(
    configuration: tuple[Permutation, ...],
    gauge: tuple[Permutation, ...],
) -> tuple[Permutation, ...]:
    return tuple(
        permutation_compose(
            permutation_compose(gauge[source], link),
            permutation_inverse(gauge[target]),
        )
        for link, (source, target) in zip(configuration, SQUARE_EDGES)
    )


def s3_class_characters() -> list:
    return [
        lambda permutation: 1,
        permutation_sign,
        standard_character,
    ]


def plaquette_pullback_basis() -> np.ndarray:
    characters = s3_class_characters()
    return np.array(
        [
            [character(plaquette_holonomy(configuration)) for character in characters]
            for configuration in S3_CONFIGURATIONS
        ],
        dtype=float,
    ) / math.sqrt(S3_CONFIG_COUNT)


def group_class_basis() -> np.ndarray:
    characters = s3_class_characters()
    return np.array(
        [[character(group_element) for character in characters] for group_element in S3],
        dtype=float,
    ) / math.sqrt(S3_ORDER)


def one_link_kernel(coupling: float, derivative_order: int = 0) -> np.ndarray:
    matrix = np.zeros((S3_ORDER, S3_ORDER), dtype=float)
    for i, left in enumerate(S3):
        for j, right in enumerate(S3):
            difference = permutation_compose(left, permutation_inverse(right))
            source = normalized_standard_character(difference)
            matrix[i, j] = (
                source**derivative_order
                * math.exp(coupling * source)
                / S3_ORDER
            )
    return matrix


def apply_link_product(
    link_operators: list[np.ndarray], vectors: np.ndarray
) -> np.ndarray:
    tensor = vectors.reshape(S3_ORDER, S3_ORDER, S3_ORDER, S3_ORDER, -1)
    for axis, operator in enumerate(link_operators):
        tensor = np.tensordot(operator, tensor, axes=(1, axis))
        tensor = np.moveaxis(tensor, 0, axis)
    return tensor.reshape(S3_CONFIG_COUNT, -1)


def reduced_link_product(
    pullback: np.ndarray, link_operators: list[np.ndarray]
) -> np.ndarray:
    return pullback.T @ apply_link_product(link_operators, pullback)


def reduced_multiplication(
    pullback: np.ndarray, values: np.ndarray
) -> np.ndarray:
    return pullback.T @ (values[:, None] * pullback)


def square_transfer_objects(
    mixed_coupling: float,
    spatial_coupling: float,
    marked_derivative_order: int | None = None,
    marked_coupling: float | None = None,
) -> dict[str, np.ndarray]:
    if marked_derivative_order is not None and marked_coupling is not None:
        raise ValueError("choose a marked derivative or a marked coupling, not both")
    pullback = plaquette_pullback_basis()
    base_link = one_link_kernel(mixed_coupling)
    link_operators = [base_link] * 4
    if marked_derivative_order is not None:
        link_operators = [
            one_link_kernel(mixed_coupling, marked_derivative_order),
            base_link,
            base_link,
            base_link,
        ]
    if marked_coupling is not None:
        link_operators = [
            one_link_kernel(marked_coupling),
            base_link,
            base_link,
            base_link,
        ]
    q_operator = reduced_link_product(pullback, link_operators)
    half_values = np.array(
        [
            math.exp(
                spatial_coupling
                * normalized_standard_character(plaquette_holonomy(configuration))
                / 2.0
            )
            for configuration in S3_CONFIGURATIONS
        ],
        dtype=float,
    )
    half_weight = reduced_multiplication(pullback, half_values)
    transfer = half_weight @ q_operator @ half_weight
    return {
        "pullback": pullback,
        "q": q_operator,
        "half": half_weight,
        "transfer": transfer,
    }


def group_multiplication_operator(function) -> np.ndarray:
    basis = group_class_basis()
    values = np.array([function(group_element) for group_element in S3], dtype=float)
    return basis.T @ (values[:, None] * basis)


def group_value_matrix(reduced_operator: np.ndarray) -> np.ndarray:
    basis = group_class_basis()
    return basis @ reduced_operator @ basis.T


def explicit_path_sum(
    step_matrices: list[np.ndarray],
    site_weight=None,
) -> float:
    total = 0.0
    length = len(step_matrices)
    for states in product(range(S3_ORDER), repeat=length):
        weight = 1.0
        for time, matrix in enumerate(step_matrices):
            current = states[time]
            following = states[(time + 1) % length]
            weight *= matrix[following, current]
        if site_weight is not None:
            weight *= site_weight(states)
        total += weight
    return total


def temporal_kernel_from_gauge_sum(
    later: tuple[Permutation, ...],
    earlier: tuple[Permutation, ...],
    coupling: float,
) -> float:
    total = 0.0
    for temporal_links in product(S3, repeat=4):
        weight = 1.0
        for later_link, earlier_link, (source, target) in zip(
            later, earlier, SQUARE_EDGES
        ):
            mixed_holonomy = permutation_compose(
                permutation_compose(later_link, temporal_links[target]),
                permutation_compose(
                    permutation_inverse(earlier_link),
                    permutation_inverse(temporal_links[source]),
                ),
            )
            weight *= math.exp(
                coupling * normalized_standard_character(mixed_holonomy)
            )
        total += weight
    return total / (S3_ORDER**4)


def projected_convolution_kernel(
    later: tuple[Permutation, ...],
    earlier: tuple[Permutation, ...],
    coupling: float,
) -> float:
    total = 0.0
    for gauge in product(S3, repeat=4):
        gauged_earlier = gauge_transform_configuration(earlier, gauge)
        weight = 1.0
        for later_link, earlier_link in zip(later, gauged_earlier):
            difference = permutation_compose(
                later_link, permutation_inverse(earlier_link)
            )
            weight *= math.exp(
                coupling * normalized_standard_character(difference)
            )
        total += weight
    return total / (S3_ORDER**4)


def orientation_gauge_errors() -> tuple[float, float]:
    correct_error = 0.0
    wrong_error = 0.0
    identity = S3[0]
    for configuration in S3_CONFIGURATIONS:
        correct_value = normalized_standard_character(plaquette_holonomy(configuration))
        wrong_value = normalized_standard_character(wrong_plaquette_word(configuration))
        for vertex in range(4):
            for group_element in S3[1:]:
                gauge = [identity] * 4
                gauge[vertex] = group_element
                transformed = gauge_transform_configuration(configuration, tuple(gauge))
                correct_error = max(
                    correct_error,
                    abs(
                        normalized_standard_character(plaquette_holonomy(transformed))
                        - correct_value
                    ),
                )
                wrong_error = max(
                    wrong_error,
                    abs(
                        normalized_standard_character(wrong_plaquette_word(transformed))
                        - wrong_value
                    ),
                )
    return correct_error, wrong_error


def main() -> int:
    # Exact SU(3) identities and finite positive-type support.
    levels = tensor_multiplicities(NMAX_TENSOR)
    dimension_sums = [
        sum(
            multiplicity * su3_dimension(weight)
            for weight, multiplicity in level.items()
        )
        for level in levels
    ]
    coefficients = truncated_wilson_coefficients(levels, GRAM_BETA)
    coefficient_minimum = min(coefficients.values())
    fundamental_error, antifundamental_error, combined_error = recurrence_errors()
    recurrence = recurrence_matrix(RECURRENCE_BOX)
    recurrence_symmetry_error = float(np.max(np.abs(recurrence - recurrence.T)))
    recurrence_eigenvalues = np.linalg.eigvalsh(recurrence)
    boundary_weights = [(0, 0), (1, 0), (0, 1), (1, 1)]
    boundary_counts = {
        weight: len(recurrence_neighbors(weight)) for weight in boundary_weights
    }
    boundary_omissions_ok = all(
        recurrence_neighbors(weight)
        == [
            target
            for target in unpruned_recurrence_neighbors(weight)
            if min(target) >= 0
        ]
        for weight in boundary_weights
    ) and [boundary_counts[weight] for weight in boundary_weights] == [2, 4, 4, 6]
    su3_samples = haar_su3_samples(GRAM_SIZE)
    positive_gram_minimum = float(
        np.linalg.eigvalsh(wilson_gram(su3_samples, GRAM_BETA)).min()
    )

    # Genuine finite one-plaquette gauge carrier.
    square = square_transfer_objects(
        S3_MIXED_COUPLING, S3_SPATIAL_COUPLING
    )
    pullback = square["pullback"]
    q_operator = square["q"]
    half_weight = square["half"]
    transfer = square["transfer"]
    group_basis = group_class_basis()
    transfer_group = group_value_matrix(transfer)
    plaquette_operator = group_multiplication_operator(
        normalized_standard_character
    )

    pullback_error = float(np.max(np.abs(pullback.T @ pullback - np.eye(3))))
    group_basis_error = float(
        np.max(np.abs(group_basis.T @ group_basis - np.eye(3)))
    )
    q_minimum = float(np.linalg.eigvalsh(q_operator).min())
    transfer_minimum = float(np.linalg.eigvalsh(transfer).min())
    q_eigenvalues, q_eigenvectors = np.linalg.eigh(q_operator)
    q_square_root = (
        q_eigenvectors
        @ np.diag(np.sqrt(np.clip(q_eigenvalues, 0.0, None)))
        @ q_eigenvectors.T
    )
    gram_factor = q_square_root @ half_weight
    factorization_error = float(
        np.max(np.abs(transfer - gram_factor.T @ gram_factor))
    )

    selected_pairs = [
        (S3_CONFIGURATIONS[0], S3_CONFIGURATIONS[17]),
        (S3_CONFIGURATIONS[103], S3_CONFIGURATIONS[411]),
        (S3_CONFIGURATIONS[777], S3_CONFIGURATIONS[1211]),
    ]
    temporal_kernel_error = max(
        abs(
            temporal_kernel_from_gauge_sum(later, earlier, S3_MIXED_COUPLING)
            - projected_convolution_kernel(later, earlier, S3_MIXED_COUPLING)
        )
        for later, earlier in selected_pairs
    )

    trace_value = float(np.trace(np.linalg.matrix_power(transfer, S3_LT)))
    trace_path = explicit_path_sum([transfer_group] * S3_LT)
    marked_value = float(
        np.trace(np.linalg.matrix_power(transfer, S3_LT) @ plaquette_operator)
    )
    marked_path = explicit_path_sum(
        [transfer_group] * S3_LT,
        site_weight=lambda states: normalized_standard_character(S3[states[0]]),
    )

    spatial_source_half = group_multiplication_operator(
        lambda group_element: math.exp(
            S3_SPATIAL_SOURCE
            * normalized_standard_character(group_element)
            / 2.0
        )
    )
    spatial_sourced_transfer = (
        spatial_source_half @ transfer @ spatial_source_half
    )
    spatial_repeated_value = float(
        np.trace(np.linalg.matrix_power(spatial_sourced_transfer, S3_LT))
    )
    spatial_repeated_path = explicit_path_sum(
        [transfer_group] * S3_LT,
        site_weight=lambda states: math.exp(
            S3_SPATIAL_SOURCE
            * sum(normalized_standard_character(S3[state]) for state in states)
        ),
    )
    spatial_single_source = group_multiplication_operator(
        lambda group_element: math.exp(
            S3_SPATIAL_SOURCE * normalized_standard_character(group_element)
        )
    )
    spatial_single_value = float(
        np.trace(
            np.linalg.matrix_power(transfer, S3_LT)
            @ spatial_single_source
        )
    )
    spatial_single_path = explicit_path_sum(
        [transfer_group] * S3_LT,
        site_weight=lambda states: math.exp(
            S3_SPATIAL_SOURCE
            * normalized_standard_character(S3[states[0]])
        ),
    )
    wrong_slice_placement_value = spatial_repeated_value

    # Mixed two-slice source and Schur-power derivatives.
    mixed_square = square_transfer_objects(
        S3_MIXED_COUPLING,
        S3_SPATIAL_COUPLING,
        marked_coupling=S3_MIXED_COUPLING + S3_MIXED_SOURCE,
    )
    mixed_transfer = mixed_square["transfer"]
    mixed_transfer_group = group_value_matrix(mixed_transfer)
    mixed_source_minimum = float(np.linalg.eigvalsh(mixed_transfer).min())
    mixed_single_value = float(
        np.trace(
            np.linalg.matrix_power(transfer, S3_LT - 1)
            @ mixed_transfer
        )
    )
    mixed_single_path = explicit_path_sum(
        [mixed_transfer_group] + [transfer_group] * (S3_LT - 1)
    )
    mixed_repeated_value = float(
        np.trace(np.linalg.matrix_power(mixed_transfer, S3_LT))
    )
    mixed_repeated_path = explicit_path_sum(
        [mixed_transfer_group] * S3_LT
    )

    derivative_operators = []
    derivative_minima = []
    schur_errors = []
    source_gram = np.zeros((S3_ORDER, S3_ORDER), dtype=float)
    for i, left in enumerate(S3):
        for j, right in enumerate(S3):
            source_gram[i, j] = normalized_standard_character(
                permutation_compose(left, permutation_inverse(right))
            )
    source_gram_minimum = float(np.linalg.eigvalsh(source_gram).min())
    exponential_gram = np.exp(S3_MIXED_COUPLING * source_gram) / S3_ORDER
    for order in range(5):
        direct = one_link_kernel(S3_MIXED_COUPLING, order)
        schur = (
            np.power(source_gram, order)
            * exponential_gram
        )
        schur_errors.append(float(np.max(np.abs(direct - schur))))
        derivative_minima.append(float(np.linalg.eigvalsh(direct).min()))
        derivative_operators.append(
            square_transfer_objects(
                S3_MIXED_COUPLING,
                S3_SPATIAL_COUPLING,
                marked_derivative_order=order,
            )["transfer"]
        )
    derivative_transfer_minima = [
        float(np.linalg.eigvalsh(operator).min())
        for operator in derivative_operators
    ]
    mixed_derivative = derivative_operators[1]
    mixed_derivative_group = group_value_matrix(mixed_derivative)
    mixed_marked_value = float(
        np.trace(
            np.linalg.matrix_power(transfer, S3_LT - 1)
            @ mixed_derivative
        )
    )
    mixed_marked_path = explicit_path_sum(
        [mixed_derivative_group] + [transfer_group] * (S3_LT - 1)
    )
    finite_difference = (
        float(
            np.trace(
                np.linalg.matrix_power(transfer, S3_LT - 1)
                @ square_transfer_objects(
                    S3_MIXED_COUPLING,
                    S3_SPATIAL_COUPLING,
                    marked_coupling=S3_MIXED_COUPLING + 1.0e-5,
                )["transfer"]
            )
        )
        - float(
            np.trace(
                np.linalg.matrix_power(transfer, S3_LT - 1)
                @ square_transfer_objects(
                    S3_MIXED_COUPLING,
                    S3_SPATIAL_COUPLING,
                    marked_coupling=S3_MIXED_COUPLING - 1.0e-5,
                )["transfer"]
            )
        )
    ) / (2.0e-5)
    # Hostile controls.
    pointwise_counterexample = np.array([[1.0, 2.0], [2.0, 1.0]])
    counterexample_minimum = float(
        np.linalg.eigvalsh(pointwise_counterexample).min()
    )
    correct_orientation_error, wrong_orientation_error = orientation_gauge_errors()

    full_spatial_values = np.array(
        [
            math.exp(
                S3_SPATIAL_COUPLING
                * normalized_standard_character(plaquette_holonomy(configuration))
            )
            for configuration in S3_CONFIGURATIONS
        ],
        dtype=float,
    )
    wrong_half_weight = reduced_multiplication(pullback, full_spatial_values)
    wrong_half_transfer = wrong_half_weight @ q_operator @ wrong_half_weight
    wrong_half_trace = float(
        np.trace(np.linalg.matrix_power(wrong_half_transfer, S3_LT))
    )
    missing_half_weight = reduced_multiplication(
        pullback, np.ones(S3_CONFIG_COUNT, dtype=float)
    )
    missing_half_transfer = missing_half_weight @ q_operator @ missing_half_weight
    missing_half_trace = float(
        np.trace(np.linalg.matrix_power(missing_half_transfer, S3_LT))
    )
    wrong_haar_trace = float(
        np.trace(np.linalg.matrix_power((S3_ORDER**4) * transfer, S3_LT))
    )

    negative_effective_square = square_transfer_objects(
        S3_MIXED_COUPLING,
        S3_SPATIAL_COUPLING,
        marked_coupling=-0.39,
    )
    negative_effective_minimum = float(
        np.linalg.eigvalsh(negative_effective_square["transfer"]).min()
    )

    print("=" * 88)
    print("GAUGE-VACUUM WILSON TRANSFER / SPATIAL-MIXED SOURCE SUPPORT")
    print("=" * 88)
    print()
    print("Exact SU(3) character data")
    print(f"  tensor levels checked                    = 0..{NMAX_TENSOR}")
    print(f"  dimension sums                           = {dimension_sums}")
    print(f"  minimum truncated coefficient            = {coefficient_minimum:.6e}")
    print(f"  recurrence errors (3,3bar,real)          = "
          f"{fundamental_error:.3e}, {antifundamental_error:.3e}, {combined_error:.3e}")
    print(f"  recurrence symmetry error                = {recurrence_symmetry_error:.3e}")
    print(f"  recurrence boundary counts               = {boundary_counts}")
    print(f"  recurrence compressed spectrum           = "
          f"[{recurrence_eigenvalues.min():.6f}, {recurrence_eigenvalues.max():.6f}]")
    print(f"  sampled SU(3) Wilson Gram min eigenvalue = {positive_gram_minimum:.6e}")
    print()
    print("Finite S3 one-plaquette gauge carrier (SUPPORT)")
    print(f"  link configurations                      = {S3_CONFIG_COUNT}")
    print(f"  physical class-function dimension        = {pullback.shape[1]}")
    print(f"  pullback/group basis errors              = {pullback_error:.3e}, {group_basis_error:.3e}")
    print(f"  Q / T minimum eigenvalues                = {q_minimum:.6e}, {transfer_minimum:.6e}")
    print(f"  transfer Gram-factorization error        = {factorization_error:.3e}")
    print(f"  temporal-link/projected-kernel error     = {temporal_kernel_error:.3e}")
    print(f"  trace / path sum                         = {trace_value:.12f} / {trace_path:.12f}")
    print(f"  spatial mark / path sum                  = {marked_value:.12f} / {marked_path:.12f}")
    print(f"  selected spatial source / path sum       = {spatial_single_value:.12f} / {spatial_single_path:.12f}")
    print(f"  repeated spatial source / path sum       = {spatial_repeated_value:.12f} / {spatial_repeated_path:.12f}")
    print()
    print("Mixed two-slice source (SUPPORT)")
    print(f"  sourced transfer minimum eigenvalue      = {mixed_source_minimum:.6e}")
    print(f"  selected mixed source / path sum         = {mixed_single_value:.12f} / {mixed_single_path:.12f}")
    print(f"  repeated mixed source / path sum         = {mixed_repeated_value:.12f} / {mixed_repeated_path:.12f}")
    print(f"  H Gram minimum eigenvalue                = {source_gram_minimum:.6e}")
    print(f"  Schur derivative kernel minima m=0..4   = {[round(x, 12) for x in derivative_minima]}")
    print(f"  sourced derivative T minima m=0..4      = {[round(x, 12) for x in derivative_transfer_minima]}")
    print(f"  mixed marked trace / path sum            = {mixed_marked_value:.12f} / {mixed_marked_path:.12f}")
    print(f"  mixed derivative / finite difference     = {mixed_marked_value:.12f} / {finite_difference:.12f}")
    print()
    print("Hostile controls")
    print(f"  pointwise-positive symmetric min eig      = {counterexample_minimum:.6e}")
    print(f"  correct/wrong plaquette gauge errors      = {correct_orientation_error:.3e}, {wrong_orientation_error:.3e}")
    print(f"  selected-vs-repeated slice mismatch       = {abs(spatial_single_value-wrong_slice_placement_value):.6e}")
    print(f"  selected-vs-repeated mixed mismatch       = {abs(mixed_single_value-mixed_repeated_value):.6e}")
    print(f"  correct/doubled half-weight mismatch      = {abs(trace_value-wrong_half_trace):.6e}")
    print(f"  correct/missing half-weight mismatch      = {abs(trace_value-missing_half_trace):.6e}")
    print(f"  correct/wrong Haar trace mismatch         = {abs(trace_value-wrong_haar_trace):.6e}")
    print(f"  negative effective-coupling min eig       = {negative_effective_minimum:.6e}")
    print()

    check(
        "tensor powers of 3 direct-sum 3bar have exact nonnegative integer multiplicities",
        all(
            isinstance(multiplicity, int) and multiplicity >= 0
            for level in levels
            for multiplicity in level.values()
        ),
        detail=f"checked all dominant weights through tensor level {NMAX_TENSOR}",
    )
    check(
        "the representation-ring decomposition preserves dimension 6^n",
        dimension_sums == [6**n for n in range(NMAX_TENSOR + 1)],
        detail=f"dimension sums = {dimension_sums}",
    )
    check(
        "positive Taylor weights give nonnegative truncated Wilson coefficients",
        coefficient_minimum >= 0.0,
        detail=f"minimum checked partial coefficient = {coefficient_minimum:.6e}",
    )
    check(
        "multiplication by chi_(1,0) obeys the exact SU(3) recurrence",
        fundamental_error < 1.0e-10,
        detail=f"maximum error = {fundamental_error:.3e}",
    )
    check(
        "multiplication by chi_(0,1) obeys the exact conjugate recurrence",
        antifundamental_error < 1.0e-10,
        detail=f"maximum error = {antifundamental_error:.3e}",
    )
    check(
        "the real plaquette source obeys the exact six-neighbor recurrence",
        combined_error < 1.0e-10 and recurrence_symmetry_error < TOL,
        detail=(
            f"combined error = {combined_error:.3e}, "
            f"symmetry error = {recurrence_symmetry_error:.3e}"
        ),
    )
    check(
        "dominant-weight boundary terms omit exactly the negative labels",
        boundary_omissions_ok,
        detail=(
            "neighbor counts at (0,0),(1,0),(0,1),(1,1) = "
            f"{list(boundary_counts.values())}"
        ),
    )

    check(
        "sampled SU(3) Wilson positive-type Gram matrices are positive semidefinite",
        positive_gram_minimum >= -TOL,
        detail=f"minimum eigenvalue = {positive_gram_minimum:.6e}",
        bucket="SUPPORT",
    )
    check(
        "the finite square pullback is an isometry onto the three class functions",
        pullback_error < TOL and group_basis_error < TOL,
        detail=f"errors={pullback_error:.3e}, {group_basis_error:.3e}",
        bucket="SUPPORT",
    )
    check(
        "the finite gauge-projected transfer is positive and has the explicit Gram factorization",
        q_minimum >= -TOL
        and transfer_minimum >= -TOL
        and factorization_error < TOL,
        detail=(
            f"lambda_min(Q)={q_minimum:.3e}, "
            f"lambda_min(T)={transfer_minimum:.3e}, "
            f"factor error={factorization_error:.3e}"
        ),
        bucket="SUPPORT",
    )
    check(
        "projected convolution equals temporal-link integration on selected square configurations",
        temporal_kernel_error < TOL,
        detail=f"maximum selected-pair error = {temporal_kernel_error:.3e}",
        bucket="SUPPORT",
    )
    check(
        "finite transfer trace and marked spatial insertion equal explicit path sums",
        abs(trace_value - trace_path) < TOL
        and abs(marked_value - marked_path) < TOL,
        detail=(
            f"trace error={abs(trace_value-trace_path):.3e}, "
            f"mark error={abs(marked_value-marked_path):.3e}"
        ),
        bucket="SUPPORT",
    )
    check(
        "selected and repeated spatial sources obey their distinct insertion formulas",
        abs(spatial_single_value - spatial_single_path) < TOL
        and abs(spatial_repeated_value - spatial_repeated_path) < TOL,
        detail=(
            f"selected error={abs(spatial_single_value-spatial_single_path):.3e}, "
            f"repeated error={abs(spatial_repeated_value-spatial_repeated_path):.3e}"
        ),
        bucket="SUPPORT",
    )
    check(
        "selected and repeated mixed sources match their distinct two-slice path sums",
        mixed_source_minimum >= -TOL
        and abs(mixed_single_value - mixed_single_path) < TOL
        and abs(mixed_repeated_value - mixed_repeated_path) < TOL
        and abs(mixed_single_value - mixed_repeated_value) > 1.0e-5,
        detail=(
            f"lambda_min={mixed_source_minimum:.3e}, "
            f"selected error={abs(mixed_single_value-mixed_single_path):.3e}, "
            f"repeated error={abs(mixed_repeated_value-mixed_repeated_path):.3e}"
        ),
        bucket="SUPPORT",
    )
    check(
        "mixed source derivatives have H^(circle m) circle exp(gamma H) Schur-power form",
        source_gram_minimum >= -TOL
        and max(schur_errors) < TOL
        and min(derivative_minima) >= -TOL
        and min(derivative_transfer_minima) >= -TOL,
        detail=(
            f"lambda_min(H)={source_gram_minimum:.3e}, "
            f"max form error={max(schur_errors):.3e}"
        ),
        bucket="SUPPORT",
    )
    check(
        "the marked mixed insertion matches its path sum and source derivative",
        abs(mixed_marked_value - mixed_marked_path) < TOL
        and abs(mixed_marked_value - finite_difference) < 2.0e-9,
        detail=(
            f"path error={abs(mixed_marked_value-mixed_marked_path):.3e}, "
            f"finite-difference error={abs(mixed_marked_value-finite_difference):.3e}"
        ),
        bucket="SUPPORT",
    )
    check(
        "pointwise positive symmetry alone does not imply quadratic-form positivity",
        np.all(pointwise_counterexample > 0.0) and counterexample_minimum < 0.0,
        detail=f"counterexample minimum eigenvalue = {counterexample_minimum:.1f}",
        bucket="SUPPORT",
    )
    check(
        "the wrong plaquette word fails gauge invariance while the oriented word passes",
        correct_orientation_error < TOL and wrong_orientation_error > 0.1,
        detail=(
            f"correct error={correct_orientation_error:.3e}, "
            f"wrong error={wrong_orientation_error:.3e}"
        ),
        bucket="SUPPORT",
    )
    check(
        "wrong slice placement, half weighting, or Haar normalization changes the path sum",
        abs(spatial_single_value - wrong_slice_placement_value) > 1.0e-5
        and abs(trace_value - wrong_half_trace) > 1.0e-5
        and abs(trace_value - missing_half_trace) > 1.0e-5
        and abs(trace_value - wrong_haar_trace) > 1.0,
        detail=(
            f"slice={abs(spatial_single_value-wrong_slice_placement_value):.3e}, "
            f"half(doubled/missing)={abs(trace_value-wrong_half_trace):.3e}/"
            f"{abs(trace_value-missing_half_trace):.3e}, "
            f"Haar={abs(trace_value-wrong_haar_trace):.3e}"
        ),
        bucket="SUPPORT",
    )
    check(
        "negative effective mixed coupling is detected outside the source-positivity domain",
        negative_effective_minimum < -1.0e-6,
        detail=f"minimum eigenvalue = {negative_effective_minimum:.6e}",
        bucket="SUPPORT",
    )
    check(
        "the compressed recurrence spectrum stays inside the plaquette support interval",
        recurrence_eigenvalues.min() >= -0.5 - TOL
        and recurrence_eigenvalues.max() <= 1.0 + TOL,
        detail=(
            f"spectrum=[{recurrence_eigenvalues.min():.6f}, "
            f"{recurrence_eigenvalues.max():.6f}]"
        ),
        bucket="SUPPORT",
    )

    print()
    print("=" * 88)
    print(f"SUMMARY: THEOREM PASS={THEOREM_PASS} SUPPORT={SUPPORT_PASS} FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
