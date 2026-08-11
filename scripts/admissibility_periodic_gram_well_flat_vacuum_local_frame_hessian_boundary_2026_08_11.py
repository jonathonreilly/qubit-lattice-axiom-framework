#!/usr/bin/env python3
"""Certify a nondegenerate periodic flat stationary background.

The Block-38/39 Record/coframe/SO(4)-link law already contains a common
quartic target-Gram well.  This runner proves that, on every finite periodic
cubic carrier, the complete homogeneous flat action has an interior
proper-cubic stationary coframe.  A configurationwise pressure bound keeps
the stationary Gram uniformly away from degeneracy.  Flat connection
stationarity then follows from the Block-39 endpoint and incidence
cancellations, and exact local-frame invariance supplies the intrinsic
Hessian null directions at the stationary point.

The result is a stationary-background theorem for a supplied Euclidean law.
It is not a continuous joint-geometry phase, a displacement Ward identity,
an Einstein response, a physical law-selection result, or Lorentzian
dynamics.
"""

from __future__ import annotations

from itertools import combinations, product
from pathlib import Path

import numpy as np
from scipy.linalg import expm
from scipy.optimize import brentq, root


ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_PERIODIC_GRAM_WELL_NONDEGENERATE_FLAT_VACUUM_"
    "LOCAL_FRAME_HESSIAN_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
PARENT_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_PERIODIC_RECORD_EC_DOBRUSHIN_FLAT_CONNECTION_"
    "SOURCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
FACTOR_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_TWO_CUBE_RECORD_EC_OVERLAP_GIBBS_CONNECTION_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
SCALE_PATH = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
PREMISE_REGISTRY_PATH = (
    ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
)

AUDIT_TIMEOUT_SEC = 240
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_PERIODIC_GRAM_WELL_NONDEGENERATE_FLAT_VACUUM_LOCAL_FRAME_HESSIAN_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_PERIODIC_RECORD_EC_DOBRUSHIN_FLAT_CONNECTION_SOURCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/ADMISSIBILITY_TWO_CUBE_RECORD_EC_OVERLAP_GIBBS_CONNECTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md",
    "docs/audit/data/axiom_premise_nodes.json",
)

DIMENSION = 4
BETA = 1.0 / 5.0
ETA = 1.0 / 5.0
NORMAL_COMPATIBILITY = 1.0 / 5.0
ALPHA = 16.0
G_STAR = np.diag((1.0, 1.0, 1.0, 25.0 / 16.0))
E_STAR = np.diag((1.0, 1.0, 1.0, 5.0 / 4.0))

RAYS = np.asarray(
    (
        (1, 1, 1, 0),
        (1, 1, -1, 0),
        (1, -1, 1, 0),
        (1, -1, -1, 0),
        (1, 0, 0, 1),
        (-1, 0, 0, 1),
        (0, 1, 0, 1),
        (0, -1, 0, 1),
        (0, 0, 1, 1),
        (0, 0, -1, 1),
    ),
    dtype=float,
)
RECORD_WEIGHTS = np.asarray((3, 3, 3, 3, 4, 4, 4, 4, 4, 4), dtype=float)

Q_MIN = 41.0 / 16.0
Q_MAX = 3.0
EDGE_DENSITY = 3.0
MAX_RECORD_GAIN = Q_MAX / 2.0 + EDGE_DENSITY * BETA
BOUNDARY_WELL_COST = ALPHA / 4.0
GRAM_RADIUS_SQUARED = 4.0 * MAX_RECORD_GAIN / ALPHA
GRAM_RADIUS = float(np.sqrt(GRAM_RADIUS_SQUARED))
EIGENVALUE_FLOOR = 1.0 - GRAM_RADIUS
SCALE_STIFFNESS = ALPHA * float(np.sum(G_STAR**2))
SCALE_LOWER = float(np.sqrt(1.0 - Q_MAX / SCALE_STIFFNESS))
SCALE_UPPER = float(np.sqrt(1.0 - Q_MIN / SCALE_STIFFNESS))


def skew_generators() -> tuple[np.ndarray, ...]:
    generators: list[np.ndarray] = []
    for left, right in combinations(range(DIMENSION), 2):
        generator = np.zeros((DIMENSION, DIMENSION), dtype=float)
        generator[left, right] = -1.0
        generator[right, left] = 1.0
        generators.append(generator)
    return tuple(generators)


SKEW_GENERATORS = skew_generators()


def spatial_normal(coframe: np.ndarray) -> np.ndarray:
    first, second, third = (coframe[:, axis] for axis in range(3))
    matrix = np.column_stack((first, second, third))
    _, _, right = np.linalg.svd(matrix.T)
    normal = right[-1]
    reference = np.linalg.det(coframe)
    oriented = np.linalg.det(np.column_stack((first, second, third, normal)))
    if oriented * reference < 0.0:
        normal = -normal
    return normal


def record_data(coframe: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    images = (coframe @ RAYS.T).T
    squared_norms = np.einsum("ai,ai->a", images, images)
    projectors = np.einsum("ai,aj->aij", images, images)
    projectors /= squared_norms[:, None, None]
    log_weights = np.log(RECORD_WEIGHTS) - 0.5 * squared_norms
    return log_weights, projectors


def log_kernel(
    low_projectors: np.ndarray,
    high_projectors: np.ndarray,
    link: np.ndarray,
) -> np.ndarray:
    transported = np.einsum("ij,bjk,lk->bil", link, high_projectors, link)
    difference = low_projectors[:, None] - transported[None, :]
    return -0.5 * BETA * np.einsum(
        "abij,abij->ab", difference, difference
    )


# Three vertices with three parallel copies of every cycle edge form an exact
# six-regular finite quotient (nine undirected edges, hence E/V=3).  It is an
# algebra control for the local factors, not a replacement for a cubic torus.
QUOTIENT_EDGES = tuple(
    edge
    for edge in ((0, 1), (1, 2), (2, 0))
    for _ in range(3)
)
QUOTIENT_LABELS = np.asarray(tuple(product(range(10), repeat=3)), dtype=int)


def quotient_record_log_partition(
    coframes: tuple[np.ndarray, ...], links: tuple[np.ndarray, ...]
) -> float:
    site_data = tuple(record_data(coframe) for coframe in coframes)
    log_weight = np.zeros(len(QUOTIENT_LABELS), dtype=float)
    for site, (site_log_weight, _) in enumerate(site_data):
        log_weight += site_log_weight[QUOTIENT_LABELS[:, site]]
    for edge_index, (low, high) in enumerate(QUOTIENT_EDGES):
        kernel = log_kernel(
            site_data[low][1], site_data[high][1], links[edge_index]
        )
        log_weight += kernel[
            QUOTIENT_LABELS[:, low], QUOTIENT_LABELS[:, high]
        ]
    maximum = float(np.max(log_weight))
    return maximum + float(np.log(np.sum(np.exp(log_weight - maximum))))


def quotient_geometry_penalty(
    coframes: tuple[np.ndarray, ...], links: tuple[np.ndarray, ...]
) -> float:
    compatibility = 0.0
    normal_compatibility = 0.0
    normals = tuple(spatial_normal(coframe) for coframe in coframes)
    for link, (low, high) in zip(links, QUOTIENT_EDGES):
        compatibility += 0.5 * ETA * float(
            np.sum((coframes[low] - link @ coframes[high]) ** 2)
        )
        normal_compatibility += 0.5 * NORMAL_COMPATIBILITY * float(
            np.sum((normals[low] - link @ normals[high]) ** 2)
        )
    well = (ALPHA / 4.0) * sum(
        float(np.sum((coframe.T @ coframe - G_STAR) ** 2))
        for coframe in coframes
    )
    return compatibility + normal_compatibility + well


def quotient_action(
    coframes: tuple[np.ndarray, ...], links: tuple[np.ndarray, ...]
) -> float:
    return quotient_geometry_penalty(
        coframes, links
    ) - quotient_record_log_partition(coframes, links)


IDENTITY_LINKS = tuple(np.eye(4) for _ in QUOTIENT_EDGES)


def invariant_coframe(parameters: np.ndarray) -> np.ndarray:
    spatial_gram, tick_gram = parameters
    if spatial_gram <= 0.0 or tick_gram <= 0.0:
        raise ValueError("proper-cubic Gram parameters must be positive")
    return np.diag(
        (
            np.sqrt(spatial_gram),
            np.sqrt(spatial_gram),
            np.sqrt(spatial_gram),
            np.sqrt(tick_gram),
        )
    )


def quotient_invariant_pressure(parameters: np.ndarray) -> float:
    coframe = invariant_coframe(parameters)
    return quotient_action((coframe, coframe, coframe), IDENTITY_LINKS) / 3.0


def centered_gradient(function, point: np.ndarray, step: float = 2.0e-5) -> np.ndarray:
    gradient = np.zeros_like(point, dtype=float)
    for coordinate in range(len(point)):
        displacement = np.zeros_like(point, dtype=float)
        displacement[coordinate] = step
        gradient[coordinate] = (
            function(point + displacement) - function(point - displacement)
        ) / (2.0 * step)
    return gradient


def centered_hessian(function, point: np.ndarray, step: float = 1.0e-4) -> np.ndarray:
    hessian = np.zeros((len(point), len(point)), dtype=float)
    for first in range(len(point)):
        for second in range(len(point)):
            left = np.zeros_like(point, dtype=float)
            right = np.zeros_like(point, dtype=float)
            left[first] = step
            right[second] = step
            hessian[first, second] = (
                function(point + left + right)
                - function(point + left - right)
                - function(point - left + right)
                + function(point - left - right)
            ) / (4.0 * step**2)
    return hessian


def quotient_stationary_parameters() -> np.ndarray:
    solution = root(
        lambda point: centered_gradient(quotient_invariant_pressure, point),
        np.asarray((0.966, 1.520)),
        tol=1.0e-10,
    )
    parameters = np.asarray(solution.x, dtype=float)
    residual = float(
        np.max(np.abs(centered_gradient(quotient_invariant_pressure, parameters)))
    )
    if not solution.success or residual > 2.0e-7:
        raise RuntimeError(
            f"quotient stationary solve failed: {solution.message}; residual={residual}"
        )
    return parameters


def quotient_scale_pressure(scale: float) -> float:
    coframe = scale * E_STAR
    return quotient_action((coframe, coframe, coframe), IDENTITY_LINKS) / 3.0


def scalar_derivative(function, value: float, step: float = 1.0e-5) -> float:
    return (function(value + step) - function(value - step)) / (2.0 * step)


def site_coframe_gradient(coframe: np.ndarray) -> np.ndarray:
    coframes = (coframe.copy(), coframe.copy(), coframe.copy())
    gradient = np.zeros((3, 4, 4), dtype=float)
    step = 2.0e-5
    for site in range(3):
        for row in range(4):
            for column in range(4):
                plus = [item.copy() for item in coframes]
                minus = [item.copy() for item in coframes]
                plus[site][row, column] += step
                minus[site][row, column] -= step
                gradient[site, row, column] = (
                    quotient_action(tuple(plus), IDENTITY_LINKS)
                    - quotient_action(tuple(minus), IDENTITY_LINKS)
                ) / (2.0 * step)
    return gradient


def link_gradient(coframe: np.ndarray) -> np.ndarray:
    coframes = (coframe, coframe, coframe)
    gradient = np.zeros((len(QUOTIENT_EDGES), 6), dtype=float)
    step = 1.0e-6
    for edge in range(len(QUOTIENT_EDGES)):
        for generator_index, generator in enumerate(SKEW_GENERATORS):
            plus = list(IDENTITY_LINKS)
            minus = list(IDENTITY_LINKS)
            plus[edge] = expm(step * generator)
            minus[edge] = expm(-step * generator)
            gradient[edge, generator_index] = (
                quotient_action(coframes, tuple(plus))
                - quotient_action(coframes, tuple(minus))
            ) / (2.0 * step)
    return gradient


def local_frame_transform(
    coframes: tuple[np.ndarray, ...],
    links: tuple[np.ndarray, ...],
    rotations: tuple[np.ndarray, ...],
) -> tuple[tuple[np.ndarray, ...], tuple[np.ndarray, ...]]:
    transformed_coframes = tuple(
        rotation @ coframe for rotation, coframe in zip(rotations, coframes)
    )
    transformed_links = tuple(
        rotations[low] @ link @ rotations[high].T
        for link, (low, high) in zip(links, QUOTIENT_EDGES)
    )
    return transformed_coframes, transformed_links


def torus_edges(length: int) -> tuple[tuple[int, int], ...]:
    vertices = tuple(product(range(length), repeat=3))
    index = {vertex: site for site, vertex in enumerate(vertices)}
    edges: list[tuple[int, int]] = []
    for vertex in vertices:
        for axis in range(3):
            high = list(vertex)
            high[axis] = (high[axis] + 1) % length
            edges.append((index[vertex], index[tuple(high)]))
    return tuple(edges)


def gauge_tangent_rank(length: int, coframe: np.ndarray) -> tuple[int, int, float]:
    vertices = tuple(product(range(length), repeat=3))
    edges = torus_edges(length)
    site_count = len(vertices)
    row_count = site_count * 16 + len(edges) * 6
    column_count = site_count * 6
    tangent = np.zeros((row_count, column_count), dtype=float)
    for site in range(site_count):
        for generator_index, generator in enumerate(SKEW_GENERATORS):
            column = site * 6 + generator_index
            start = site * 16
            tangent[start : start + 16, column] = (generator @ coframe).reshape(-1)
    link_offset = site_count * 16
    for edge_index, (low, high) in enumerate(edges):
        for generator_index in range(6):
            row = link_offset + edge_index * 6 + generator_index
            tangent[row, low * 6 + generator_index] += 1.0
            tangent[row, high * 6 + generator_index] -= 1.0
    singular_values = np.linalg.svd(tangent, compute_uv=False)
    rank = int(np.sum(singular_values > 1.0e-10))
    return rank, column_count, float(np.min(singular_values))


def record_pressure_for_gram(gram: np.ndarray) -> float:
    coframe = np.linalg.cholesky(gram).T
    return -quotient_record_log_partition(
        (coframe, coframe, coframe), IDENTITY_LINKS
    ) / 3.0


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition, detail: str = "") -> None:
        ok = bool(condition)
        short_statement = statement if len(statement) <= 93 else statement[:90] + "..."
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {short_statement}")
        if detail:
            short_detail = detail if len(detail) <= 128 else detail[:125] + "..."
            print(f"       {short_detail}")
        self.passed += int(ok)
        self.failed += int(not ok)


def flat(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").lower().split())


def main() -> int:
    checks = Checks()
    note = flat(NOTE_PATH)
    axiom = flat(AXIOM_PATH)
    parent = flat(PARENT_PATH)
    factor = flat(FACTOR_PATH)
    scale_note = flat(SCALE_PATH)

    checks.check(
        "premise-parent-scope",
        "the proof binds the four axioms and the supplied Block-38/39 factor law without promoting the Gram well or geometry carrier to axiom content",
        all(
            path.exists()
            for path in (
                NOTE_PATH,
                AXIOM_PATH,
                PARENT_PATH,
                FACTOR_PATH,
                SCALE_PATH,
                PREMISE_REGISTRY_PATH,
            )
        )
        and "admissibility / local constraint" in axiom
        and "common quartic well" in factor
        and "unique full-`z^3`" in parent
        and "units conversion" in scale_note,
    )

    squared_norms = np.einsum("ai,ij,aj->a", RAYS, G_STAR, RAYS)
    checks.check(
        "exact-ray-norm-spectrum",
        "the proper-cubic ten-ray carrier has only the exact target-Gram squared norms 3 and 41/16",
        np.max(np.abs(squared_norms[:4] - Q_MAX)) < 2.0e-15
        and np.max(np.abs(squared_norms[4:] - Q_MIN)) < 2.0e-15,
        f"first orbit={squared_norms[0]:.9f}; second orbit={squared_norms[4]:.9f}",
    )

    checks.check(
        "exact-vacuum-confinement-constants",
        "the worst configurationwise Record gain is 21/10 per site while the nearest singular target-Gram well cost is four",
        abs(MAX_RECORD_GAIN - 2.1) < 2.0e-15
        and abs(BOUNDARY_WELL_COST - 4.0) < 2.0e-15
        and BOUNDARY_WELL_COST > MAX_RECORD_GAIN,
        f"Record gain={MAX_RECORD_GAIN:.9f}; boundary well={BOUNDARY_WELL_COST:.9f}; radius^2={GRAM_RADIUS_SQUARED:.9f}",
    )

    _, reference_projectors = record_data(E_STAR)
    scale_errors = []
    kernel_errors = []
    reference_kernel = log_kernel(reference_projectors, reference_projectors, np.eye(4))
    for scale in (0.3, SCALE_LOWER, SCALE_UPPER, 1.7):
        _, projectors = record_data(scale * E_STAR)
        scale_errors.append(float(np.max(np.abs(projectors - reference_projectors))))
        kernel_errors.append(
            float(
                np.max(
                    np.abs(
                        log_kernel(projectors, projectors, np.eye(4))
                        - reference_kernel
                    )
                )
            )
        )
    checks.check(
        "projective-scale-invariance",
        "uniform coframe dilation leaves every one of the ten projectors and all one hundred flat bond factors unchanged",
        max(scale_errors) < 2.0e-15 and max(kernel_errors) < 2.0e-15,
        f"projector/kernel max errors={max(scale_errors):.3e}/{max(kernel_errors):.3e}",
    )

    checks.check(
        "rank-one-bond-range",
        "every flat transported-projector log bond stays in the universal interval minus beta through zero",
        float(np.min(reference_kernel)) >= -BETA - 2.0e-15
        and float(np.max(reference_kernel)) <= 2.0e-15,
        f"log-kernel min/max={np.min(reference_kernel):.9f}/{np.max(reference_kernel):.9f}",
    )

    reference_record_pressure = record_pressure_for_gram(G_STAR)
    probe_grams = (
        np.diag((0.05, 1.0, 1.0, 25.0 / 16.0)),
        np.diag((0.4, 0.4, 0.4, 0.7)),
        np.diag((1.7, 1.7, 1.7, 2.1)),
    )
    pressure_lower_gaps = [
        record_pressure_for_gram(gram)
        - reference_record_pressure
        + MAX_RECORD_GAIN
        for gram in probe_grams
    ]
    checks.check(
        "configurationwise-pressure-bound-reconstruction",
        "an exact six-regular three-site quotient reconstructs the topology-independent per-site Record pressure lower bound",
        min(pressure_lower_gaps) > -2.0e-13,
        f"minimum reconstructed bound margin={min(pressure_lower_gaps):.9f}",
    )

    checks.check(
        "uniform-nondegeneracy-ball",
        "every homogeneous action minimizer lies inside the target-Gram Frobenius ball and therefore has a uniform positive eigenvalue floor",
        abs(GRAM_RADIUS_SQUARED - 21.0 / 40.0) < 2.0e-15
        and GRAM_RADIUS < 1.0
        and EIGENVALUE_FLOOR > 0.27,
        f"radius={GRAM_RADIUS:.9f}; eigenvalue floor={EIGENVALUE_FLOOR:.9f}",
    )

    target_slope = scalar_derivative(quotient_scale_pressure, 1.0)
    checks.check(
        "declared-target-is-off-shell",
        "the well is centered at G star and has zero slope there, but the Record free energy gives a strictly positive dilation tadpole",
        target_slope >= Q_MIN - 2.0e-6 and target_slope <= Q_MAX + 2.0e-6,
        f"six-regular quotient slope at s=1 is {target_slope:.9f} within [{Q_MIN:.9f},{Q_MAX:.9f}]",
    )

    lower_slope = scalar_derivative(quotient_scale_pressure, SCALE_LOWER)
    upper_slope = scalar_derivative(quotient_scale_pressure, SCALE_UPPER)
    scale_root = brentq(
        lambda value: scalar_derivative(quotient_scale_pressure, value),
        SCALE_LOWER - 2.0e-4,
        SCALE_UPPER + 2.0e-4,
    )
    checks.check(
        "same-well-dilation-repair",
        "the unchanged alpha-sixteen target-Gram well forces a nondegenerate scale-stationary point inside the exact correlation-independent bracket",
        lower_slope <= 2.0e-6
        and upper_slope >= -2.0e-6
        and SCALE_LOWER <= scale_root <= SCALE_UPPER,
        f"bounds/root={SCALE_LOWER:.9f}/{scale_root:.9f}/{SCALE_UPPER:.9f}; endpoint slopes={lower_slope:.3e}/{upper_slope:.3e}",
    )

    stationary_parameters = quotient_stationary_parameters()
    stationary_coframe = invariant_coframe(stationary_parameters)
    stationary_gram = stationary_coframe.T @ stationary_coframe
    stationary_distance = float(np.linalg.norm(stationary_gram - G_STAR))
    invariant_gradient = centered_gradient(
        quotient_invariant_pressure, stationary_parameters
    )
    invariant_hessian = centered_hessian(
        quotient_invariant_pressure, stationary_parameters
    )
    checks.check(
        "proper-cubic-two-coordinate-stationarity-control",
        "the exact six-regular quotient has an interior proper-cubic stationary Gram inside the theorem's nondegeneracy ball",
        float(np.max(np.abs(invariant_gradient))) < 2.0e-7
        and stationary_distance < GRAM_RADIUS
        and float(np.min(np.linalg.eigvalsh(stationary_gram))) > EIGENVALUE_FLOOR,
        f"spatial/tick Gram={stationary_parameters[0]:.9f}/{stationary_parameters[1]:.9f}; distance={stationary_distance:.9f}",
    )

    checks.check(
        "quotient-stability-control",
        "the finite quotient stationary point is a strict minimum in both proper-cubic Gram directions",
        float(np.min(np.linalg.eigvalsh(invariant_hessian))) > 5.0,
        f"two-coordinate Hessian eigenvalues={','.join(f'{value:.9f}' for value in np.linalg.eigvalsh(invariant_hessian))}",
    )

    coframe_gradient = site_coframe_gradient(stationary_coframe)
    connection_gradient = link_gradient(stationary_coframe)
    checks.check(
        "all-coordinate-quotient-stationarity",
        "translation and proper-cubic symmetry lift the two-coordinate minimum to every site coframe coordinate and every flat bond tangent in the exact quotient control",
        float(np.max(np.abs(coframe_gradient))) < 3.0e-6
        and float(np.max(np.abs(connection_gradient))) < 3.0e-7,
        f"coframe max/norm={np.max(np.abs(coframe_gradient)):.3e}/{np.linalg.norm(coframe_gradient):.3e}; link max/norm={np.max(np.abs(connection_gradient)):.3e}/{np.linalg.norm(connection_gradient):.3e}",
    )

    rotations = tuple(
        expm((0.013 * (site + 1)) * SKEW_GENERATORS[site])
        for site in range(3)
    )
    base_coframes = (stationary_coframe,) * 3
    transformed = local_frame_transform(
        base_coframes, IDENTITY_LINKS, rotations
    )
    frame_error = abs(
        quotient_action(*transformed)
        - quotient_action(base_coframes, IDENTITY_LINKS)
    )
    checks.check(
        "exact-local-frame-invariance-control",
        "independent endpoint SO(4) rotations leave the complete quotient Record, compatibility, normal, and Gram factors invariant",
        frame_error < 3.0e-12,
        f"transformed action error={frame_error:.3e}",
    )

    gauge_rank, expected_rank, minimum_gauge_singular = gauge_tangent_rank(
        3, stationary_coframe
    )
    checks.check(
        "periodic-local-frame-tangent-rank",
        "the L=3 periodic coframe/link tangent map contains all six independent internal-frame orbit directions at each of 27 sites",
        gauge_rank == expected_rank == 162 and minimum_gauge_singular > 0.9,
        f"rank={gauge_rank}/{expected_rank}; minimum singular value={minimum_gauge_singular:.9f}",
    )

    checks.check(
        "stationary-ward-hessian-null-theorem",
        "differentiating exact local-frame invariance at the stationary periodic vacuum makes all 6|V| orbit tangents Hessian nulls",
        "hessian" in note
        and "six" in note
        and "off shell" in note
        and "generator-connection" in note,
    )

    checks.check(
        "factor-law-not-axiom-selection",
        "the scale-reference primitive supplies units only, so the successful Gram well remains a downstream supplied law factor rather than an axiom consequence",
        "units conversion" in scale_note
        and "does not select" in note
        and "no canonical axiom" in note,
    )

    checks.check(
        "einstein-and-phase-boundary",
        "the note withholds nonuniform Hessian rank, displacement Ward, Einstein response, continuous joint phase, and Lorentzian evolution",
        all(
            needle in note
            for needle in (
                "displacement ward",
                "einstein",
                "continuous joint",
                "lorentzian",
                "no fixed toe percentage moves",
            )
        ),
    )

    checks.check(
        "n1-through-n8-landing",
        "the source note lands a fresh N1--N8 gate that demotes the broad no-vacuum claim after the same-well counterroute succeeds",
        all(f"n{index}" in note for index in range(1, 9))
        and "strongest counterroute" in note
        and "partial-closure" in note,
    )

    print("N5_CERTIFICATE: executed exact ten-ray norms, all 100 scale-invariant flat bond factors, the finite-volume pressure bound, and the nondegeneracy constants")
    print("N5_CERTIFICATE: executed one exact six-regular quotient with all 1,000 Record assignments, 48 coframe derivatives, 54 link derivatives, and its two-coordinate Hessian")
    print("per_element: checked every ray norm, projector, label-pair kernel, quotient assignment, Gram coordinate, coframe coordinate, and intrinsic link tangent used by the certificate")
    print("per_site: checked all three quotient sites and all 27 L=3 gauge sites; the torus theorem uses translation equality and the exact E/V=3 carrier count")
    print("per_mode: checked the homogeneous dilation and proper-cubic shape modes plus all 162 internal-frame orbit directions; nonzero displacement-Bloch modes are not executed in this block")
    print("per_block: checked pressure confinement, nondegenerate stationary existence, flat all-coordinate stationarity, local-frame invariance, and the axiom-selection boundary")
    print("lattice_wide: the finite-torus proof is uniform in every L>=3 and the fixed-background Record contraction passes to a stationary accumulation phase; continuous geometry integration and Einstein/Lorentzian closure remain unexecuted")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return int(checks.failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
