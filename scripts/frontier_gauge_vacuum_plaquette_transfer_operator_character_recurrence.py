#!/usr/bin/env python3
"""
Independent witnesses for the finite-volume Wilson transfer positivity repair.

The proof in the companion note is analytic. This runner checks its distinct
algebraic components: SU(3) representation-ring multiplicities and recurrence,
sampled Wilson positive-type Gram matrices, and an exhaustive finite
nonabelian transfer model including marked and repeated spatial sources.
"""

from __future__ import annotations

import cmath
import math
from collections import defaultdict
from itertools import product

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
S3_SOURCE = -0.29
S3_LT = 2
TOL = 2.0e-11

TORUS_SAMPLES = [
    (0.37, -0.91),
    (1.11, 0.43),
    (-0.64, 1.27),
    (0.82, -1.44),
]


def check(name: str, condition: bool, detail: str = "", bucket: str = "THEOREM") -> None:
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
# SU(3) representation-ring and character checks
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


def tensor_multiplicities(nmax: int) -> list[dict[tuple[int, int], int]]:
    levels: list[dict[tuple[int, int], int]] = [{(0, 0): 1}]
    for _ in range(nmax):
        next_level: defaultdict[tuple[int, int], int] = defaultdict(int)
        for weight, multiplicity in levels[-1].items():
            for target in fundamental_neighbors(weight):
                next_level[target] += multiplicity
            for target in antifundamental_neighbors(weight):
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


def recurrence_neighbors(weight: tuple[int, int]) -> list[tuple[int, int]]:
    return fundamental_neighbors(weight) + antifundamental_neighbors(weight)


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
            rhs_3 = sum(su3_character(a, b, z) for a, b in fundamental_neighbors((p, q)))
            rhs_3bar = sum(
                su3_character(a, b, z) for a, b in antifundamental_neighbors((p, q))
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
            group_difference = left @ right.conj().T
            gram[i, j] = math.exp(beta * float(np.trace(group_difference).real) / 3.0)
    return gram


# ---------------------------------------------------------------------------
# Exhaustive finite nonabelian transfer model on S3
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


S3: list[Permutation] = list(product(range(3), repeat=3))
S3 = [permutation for permutation in S3 if len(set(permutation)) == 3]
S3_INDEX = {permutation: i for i, permutation in enumerate(S3)}
S3_ORDER = len(S3)


def s3_weight(permutation: Permutation) -> float:
    return math.exp(S3_MIXED_COUPLING * standard_character(permutation))


def s3_convolution_matrix() -> np.ndarray:
    matrix = np.zeros((S3_ORDER, S3_ORDER), dtype=float)
    for i, left in enumerate(S3):
        for j, right in enumerate(S3):
            difference = permutation_compose(left, permutation_inverse(right))
            matrix[i, j] = s3_weight(difference) / S3_ORDER
    return matrix


def s3_gauge_projector() -> np.ndarray:
    projector = np.zeros((S3_ORDER, S3_ORDER), dtype=float)
    for i, configuration in enumerate(S3):
        for gauge_element in S3:
            transformed = permutation_compose(
                permutation_compose(gauge_element, configuration),
                permutation_inverse(gauge_element),
            )
            projector[i, S3_INDEX[transformed]] += 1.0 / S3_ORDER
    return projector


def s3_half_weight() -> np.ndarray:
    diagonal = [
        math.exp(S3_SPATIAL_COUPLING * standard_character(configuration) / 2.0)
        for configuration in S3
    ]
    return np.diag(diagonal)


def s3_source_half_weight() -> np.ndarray:
    diagonal = [
        math.exp(S3_SOURCE * standard_character(configuration) / 2.0)
        for configuration in S3
    ]
    return np.diag(diagonal)


def s3_q_kernel(left: Permutation, right: Permutation) -> float:
    total = 0.0
    for gauge_element in S3:
        gauged_right = permutation_compose(
            permutation_compose(
                permutation_inverse(gauge_element), right
            ),
            gauge_element,
        )
        difference = permutation_compose(left, permutation_inverse(gauged_right))
        total += s3_weight(difference)
    return total / S3_ORDER


def explicit_s3_path_sums() -> tuple[float, float, float]:
    partition = 0.0
    marked = 0.0
    repeated = 0.0
    normalization = float(S3_ORDER ** (2 * S3_LT))
    for configurations in product(S3, repeat=S3_LT):
        for gauges in product(S3, repeat=S3_LT):
            path_weight = 1.0
            for time in range(S3_LT):
                current = configurations[time]
                following = configurations[(time + 1) % S3_LT]
                gauge_element = gauges[time]
                gauged_current = permutation_compose(
                    permutation_compose(
                        permutation_inverse(gauge_element), current
                    ),
                    gauge_element,
                )
                difference = permutation_compose(
                    following, permutation_inverse(gauged_current)
                )
                spatial_weight = math.exp(
                    S3_SPATIAL_COUPLING * standard_character(current)
                )
                path_weight *= spatial_weight * s3_weight(difference)
            partition += path_weight
            marked += path_weight * standard_character(configurations[0])
            repeated += path_weight * math.exp(
                S3_SOURCE
                * sum(standard_character(configuration) for configuration in configurations)
            )
    return (
        partition / normalization,
        marked / normalization,
        repeated / normalization,
    )


def s3_plaquette_pullback_gram() -> np.ndarray:
    characters = [
        lambda permutation: 1,
        permutation_sign,
        standard_character,
    ]
    gram = np.zeros((3, 3), dtype=float)
    normalization = float(S3_ORDER**4)
    for links in product(S3, repeat=4):
        holonomy = permutation_compose(
            permutation_compose(links[0], links[1]),
            permutation_compose(
                permutation_inverse(links[2]),
                permutation_inverse(links[3]),
            ),
        )
        values = np.array([character(holonomy) for character in characters], dtype=float)
        gram += np.outer(values, values) / normalization
    return gram


def main() -> int:
    levels = tensor_multiplicities(NMAX_TENSOR)
    dimension_sums = [
        sum(multiplicity * su3_dimension(weight) for weight, multiplicity in level.items())
        for level in levels
    ]
    coefficients = truncated_wilson_coefficients(levels, GRAM_BETA)
    coefficient_minimum = min(coefficients.values())

    fundamental_error, antifundamental_error, combined_error = recurrence_errors()
    recurrence = recurrence_matrix(RECURRENCE_BOX)
    recurrence_symmetry_error = float(np.max(np.abs(recurrence - recurrence.T)))
    recurrence_eigenvalues = np.linalg.eigvalsh(recurrence)

    su3_samples = haar_su3_samples(GRAM_SIZE)
    positive_gram = wilson_gram(su3_samples, GRAM_BETA)
    negative_beta_gram = wilson_gram(su3_samples, -GRAM_BETA)
    positive_gram_minimum = float(np.linalg.eigvalsh(positive_gram).min())
    negative_beta_minimum = float(np.linalg.eigvalsh(negative_beta_gram).min())

    convolution = s3_convolution_matrix()
    projector = s3_gauge_projector()
    half_weight = s3_half_weight()
    q_operator = convolution @ projector
    transfer = half_weight @ q_operator @ half_weight
    source_half_weight = s3_source_half_weight()
    sourced_transfer = source_half_weight @ transfer @ source_half_weight

    convolution_minimum = float(np.linalg.eigvalsh(convolution).min())
    projector_error = float(np.max(np.abs(projector @ projector - projector)))
    commutator_error = float(np.max(np.abs(convolution @ projector - projector @ convolution)))
    q_minimum = float(np.linalg.eigvalsh(q_operator).min())
    transfer_minimum = float(np.linalg.eigvalsh(transfer).min())
    sourced_transfer_minimum = float(np.linalg.eigvalsh(sourced_transfer).min())

    q_eigenvalues, q_eigenvectors = np.linalg.eigh(q_operator)
    q_square_root = (
        q_eigenvectors
        @ np.diag(np.sqrt(np.clip(q_eigenvalues, 0.0, None)))
        @ q_eigenvectors.T
    )
    gram_factor = q_square_root @ half_weight
    factorization_error = float(np.max(np.abs(transfer - gram_factor.T @ gram_factor)))

    q_kernel_error = 0.0
    for i, left in enumerate(S3):
        for j, right in enumerate(S3):
            q_kernel_error = max(
                q_kernel_error,
                abs(S3_ORDER * q_operator[i, j] - s3_q_kernel(left, right)),
            )

    partition_trace = float(np.trace(np.linalg.matrix_power(transfer, S3_LT)))
    source_operator = np.diag([standard_character(configuration) for configuration in S3])
    marked_trace = float(
        np.trace(np.linalg.matrix_power(transfer, S3_LT) @ source_operator)
    )
    repeated_trace = float(
        np.trace(np.linalg.matrix_power(sourced_transfer, S3_LT))
    )
    partition_path, marked_path, repeated_path = explicit_s3_path_sums()

    pullback_gram = s3_plaquette_pullback_gram()
    pullback_error = float(np.max(np.abs(pullback_gram - np.eye(3))))

    pointwise_counterexample = np.array([[1.0, 2.0], [2.0, 1.0]])
    counterexample_minimum = float(np.linalg.eigvalsh(pointwise_counterexample).min())

    print("=" * 78)
    print("GAUGE-VACUUM POSITIVE TRANSFER / CHARACTER-RECURRENCE REPAIR")
    print("=" * 78)
    print()
    print("SU(3) representation-ring witnesses")
    print(f"  tensor levels checked                 = 0..{NMAX_TENSOR}")
    print(f"  dimension sums                        = {dimension_sums}")
    print(f"  expected dimensions                   = {[6**n for n in range(NMAX_TENSOR + 1)]}")
    print(f"  minimum truncated coefficient         = {coefficient_minimum:.6e}")
    print(f"  sampled Wilson Gram minimum eigenvalue= {positive_gram_minimum:.6e}")
    print(f"  negative-beta Gram minimum eigenvalue = {negative_beta_minimum:.6e}")
    print()
    print("SU(3) marked-plaquette recurrence witnesses")
    print(f"  chi_(1,0) recurrence error            = {fundamental_error:.3e}")
    print(f"  chi_(0,1) recurrence error            = {antifundamental_error:.3e}")
    print(f"  combined source recurrence error      = {combined_error:.3e}")
    print(f"  compressed recurrence symmetry error  = {recurrence_symmetry_error:.3e}")
    print(
        "  compressed recurrence spectrum        = "
        f"[{recurrence_eigenvalues.min():.6f}, {recurrence_eigenvalues.max():.6f}]"
    )
    print()
    print("Exhaustive S3 transfer-factorization witness")
    print(f"  convolution minimum eigenvalue        = {convolution_minimum:.6e}")
    print(f"  gauge-projector idempotence error      = {projector_error:.3e}")
    print(f"  convolution/projector commutator      = {commutator_error:.3e}")
    print(f"  Q minimum eigenvalue                  = {q_minimum:.6e}")
    print(f"  transfer minimum eigenvalue           = {transfer_minimum:.6e}")
    print(f"  sourced transfer minimum eigenvalue   = {sourced_transfer_minimum:.6e}")
    print(f"  transfer Gram-factorization error     = {factorization_error:.3e}")
    print(f"  projected mixed-kernel error          = {q_kernel_error:.3e}")
    print(f"  transfer trace / path sum             = {partition_trace:.12f} / {partition_path:.12f}")
    print(f"  marked trace / path sum               = {marked_trace:.12f} / {marked_path:.12f}")
    print(f"  repeated source trace / path sum      = {repeated_trace:.12f} / {repeated_path:.12f}")
    print(f"  four-link pullback isometry error      = {pullback_error:.3e}")
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
        "sampled SU(3) Wilson positive-type Gram matrices are positive semidefinite",
        positive_gram_minimum >= -TOL,
        detail=f"minimum eigenvalue = {positive_gram_minimum:.6e}",
        bucket="SUPPORT",
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
        "finite nonabelian character-exponential convolution is positive and commutes with gauge projection",
        convolution_minimum >= -TOL and commutator_error < TOL and projector_error < TOL,
        detail=(
            f"lambda_min(C)={convolution_minimum:.3e}, "
            f"||[C,P]||_max={commutator_error:.3e}"
        ),
        bucket="SUPPORT",
    )
    check(
        "finite-model gauge-projected Q and half-weight transfer are positive",
        q_minimum >= -TOL and transfer_minimum >= -TOL,
        detail=f"lambda_min(Q)={q_minimum:.3e}, lambda_min(T)={transfer_minimum:.3e}",
        bucket="SUPPORT",
    )
    check(
        "the finite-model transfer equals its explicit Gram factorization",
        factorization_error < TOL,
        detail=f"maximum entry error = {factorization_error:.3e}",
        bucket="SUPPORT",
    )
    check(
        "the finite-model periodic transfer trace equals the exhaustive path sum",
        abs(partition_trace - partition_path) < TOL and q_kernel_error < TOL,
        detail=(
            f"|trace-path|={abs(partition_trace-partition_path):.3e}, "
            f"kernel error={q_kernel_error:.3e}"
        ),
        bucket="SUPPORT",
    )
    check(
        "finite-model marked and repeated sources match path sums and preserve positivity",
        abs(marked_trace - marked_path) < TOL
        and abs(repeated_trace - repeated_path) < TOL
        and sourced_transfer_minimum >= -TOL,
        detail=(
            f"marked error={abs(marked_trace-marked_path):.3e}, "
            f"repeated error={abs(repeated_trace-repeated_path):.3e}"
        ),
        bucket="SUPPORT",
    )

    check(
        "negative beta is detected outside the nonnegative-coefficient theorem",
        negative_beta_minimum < -1.0e-6,
        detail=f"sampled minimum eigenvalue = {negative_beta_minimum:.6e}",
        bucket="SUPPORT",
    )
    check(
        "pointwise positive symmetry alone does not imply quadratic-form positivity",
        np.all(pointwise_counterexample > 0.0) and counterexample_minimum < 0.0,
        detail=f"counterexample minimum eigenvalue = {counterexample_minimum:.1f}",
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
    check(
        "the four-link plaquette pullback preserves class-character inner products",
        pullback_error < TOL,
        detail=f"maximum Gram error = {pullback_error:.3e}",
        bucket="SUPPORT",
    )

    print()
    print("=" * 78)
    print(f"SUMMARY: THEOREM PASS={THEOREM_PASS} SUPPORT={SUPPORT_PASS} FAIL={FAIL}")
    print("=" * 78)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
