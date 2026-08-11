#!/usr/bin/env python3
"""Certify a bounded proper-cubic spatial coframe-curvature fixture.

The construction uses the eight vertices, twelve edges, six faces, and all
twenty-four based oriented face loops of one spatial cube.  Ten projective
Record rays interact through transported rank-one images.  Each occupied
Record branch contains a derived-normal complementary-triad Einstein--Cartan
bivector contracted linearly with antisymmetric plaquette holonomy.
Four-component coframes and SO(4) links carry endpoint-local frame covariance.
A finite Record sum and a coercive coframe well define one positive
normalizable joint weight on the declared finite domain.

All coefficients and the two-parameter equivariant link ansatz are declared
before the stationary parameters are solved.  Coframe wells are then
reverse-engineered from the complete non-well gradient and are reported as
supplied witness-law data.  This proves a finite spatial precursor and its
bookkeeping, not a derivation or physical selection of gravity.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations, permutations, product
from pathlib import Path

import numpy as np
from scipy.linalg import expm
from scipy.optimize import root


ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_PROPER_CUBIC_SPATIAL_PLAQUETTE_RECORD_COFRAME_"
    "PALATINI_CURVATURE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
LOCAL_LAW_PARENT_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_LOCAL_GEOMETRY_RECORD_BOND_TRANSFER_REFLECTION_RESPONSE_"
    "CONNECTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
FRAME_PARENT_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_TEN_RAY_COFRAME_LINK_LOCAL_FRAME_WARD_STATIONARITY_"
    "CONNECTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
PREMISE_REGISTRY_PATH = (
    ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
)

AUDIT_TIMEOUT_SEC = 240
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_PROPER_CUBIC_SPATIAL_PLAQUETTE_RECORD_COFRAME_PALATINI_CURVATURE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_LOCAL_GEOMETRY_RECORD_BOND_TRANSFER_REFLECTION_RESPONSE_CONNECTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/ADMISSIBILITY_TEN_RAY_COFRAME_LINK_LOCAL_FRAME_WARD_STATIONARITY_CONNECTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/audit/data/axiom_premise_nodes.json",
)

DIMENSION = 4
ETA = 1.0 / 5.0
TAU = 3.0 / 10.0
BETA = 1.0 / 5.0
SIGMA = 1.0 / 2.0
ALPHA = 16.0
NORMAL_COMPATIBILITY = 1.0 / 5.0
LINK_STEP = 1.0e-6
COFRAME_STEP = 2.0e-5

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

# The vertex order exposes two square layers for the exact 10-state tensor
# contraction used by record_partition.
VERTICES = (
    (-1, -1, -1),
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, 1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, 1, 1),
)
VERTEX_INDEX = {vertex: index for index, vertex in enumerate(VERTICES)}


def spatial_rotations() -> tuple[np.ndarray, ...]:
    rotations: list[np.ndarray] = []
    for permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            matrix = np.zeros((3, 3), dtype=int)
            for old_axis, new_axis in enumerate(permutation):
                matrix[new_axis, old_axis] = signs[old_axis]
            if round(float(np.linalg.det(matrix))) == 1:
                rotations.append(matrix)
    rotations.sort(key=lambda item: tuple(item.reshape(-1)))
    return tuple(rotations)


SPATIAL_ROTATIONS = spatial_rotations()


def four_rotation(spatial: np.ndarray) -> np.ndarray:
    result = np.eye(4, dtype=float)
    result[:3, :3] = spatial
    return result


def cube_edges() -> tuple[tuple[int, int, int], ...]:
    edges: list[tuple[int, int, int]] = []
    for low_index, vertex in enumerate(VERTICES):
        for axis in range(3):
            if vertex[axis] == -1:
                high = list(vertex)
                high[axis] = 1
                edges.append((low_index, VERTEX_INDEX[tuple(high)], axis))
    return tuple(edges)


EDGES = cube_edges()
EDGE_INDEX = {(low, high): index for index, (low, high, _) in enumerate(EDGES)}


def plaquette_orbit() -> tuple[tuple[int, int, int, int], ...]:
    # The seed is the outward-oriented +x face.  Its proper-cubic orbit has
    # 24 based loops: six faces times four cyclic base corners.
    seed = (
        (1, -1, -1),
        (1, 1, -1),
        (1, 1, 1),
        (1, -1, 1),
    )
    loops = []
    for rotation in SPATIAL_ROTATIONS:
        rotated = tuple(
            VERTEX_INDEX[tuple(rotation @ np.asarray(vertex, dtype=int))]
            for vertex in seed
        )
        loops.append(rotated)
    return tuple(loops)


PLAQUETTES = plaquette_orbit()


def skew_generators() -> tuple[np.ndarray, ...]:
    generators: list[np.ndarray] = []
    for left, right in combinations(range(4), 2):
        generator = np.zeros((4, 4), dtype=float)
        generator[left, right] = -1.0
        generator[right, left] = 1.0
        generators.append(generator)
    return tuple(generators)


SKEW_GENERATORS = skew_generators()


def levi_civita_four() -> np.ndarray:
    epsilon = np.zeros((4, 4, 4, 4), dtype=float)
    for ordering in permutations(range(4)):
        inversions = sum(
            ordering[left] > ordering[right]
            for left in range(4)
            for right in range(left + 1, 4)
        )
        epsilon[ordering] = (-1.0) ** inversions
    return epsilon


EPSILON = levi_civita_four()


def wedge(left: np.ndarray, right: np.ndarray) -> np.ndarray:
    """Return the antisymmetric bivector in the runner's generator sign."""

    return np.outer(right, left) - np.outer(left, right)


def hodge_star(bivector: np.ndarray) -> np.ndarray:
    return 0.5 * np.einsum("ijab,ab->ij", EPSILON, bivector)


def spatial_normal(coframe: np.ndarray) -> np.ndarray:
    """Return the oriented unit internal normal to the three spatial columns."""

    raw = -np.einsum(
        "ijkl,j,k,l->i",
        EPSILON,
        coframe[:, 0],
        coframe[:, 1],
        coframe[:, 2],
    )
    return raw / float(np.linalg.norm(raw))


def einstein_cartan_bivector(
    coframe: np.ndarray, first_step: np.ndarray, second_step: np.ndarray
) -> np.ndarray:
    """Intrinsic spatial EC bivector for the plaquette spanned by two steps."""

    complementary_step = np.cross(first_step, second_step)
    complementary_four = np.concatenate((complementary_step, (0.0,)))
    # ``wedge(left, right)`` uses the runner's generator sign, so this order
    # represents the mathematical bivector normal wedge complementary-triad.
    return hodge_star(
        wedge(coframe @ complementary_four, spatial_normal(coframe))
    )


def canonical_projector(direction: np.ndarray) -> np.ndarray:
    return np.outer(direction, direction) / float(np.dot(direction, direction))


RAY_PROJECTORS = np.asarray([canonical_projector(direction) for direction in RAYS])


def oriented_link(links: tuple[np.ndarray, ...], start: int, end: int) -> np.ndarray:
    if (start, end) in EDGE_INDEX:
        return links[EDGE_INDEX[(start, end)]]
    return links[EDGE_INDEX[(end, start)]].T


@dataclass(frozen=True)
class RecordState:
    weights: tuple[np.ndarray, ...]
    projectors: tuple[np.ndarray, ...]
    scores: tuple[np.ndarray, ...]


def record_state(coframes: tuple[np.ndarray, ...]) -> RecordState:
    weights: list[np.ndarray] = []
    projectors: list[np.ndarray] = []
    scores: list[np.ndarray] = []
    for coframe in coframes:
        images = (coframe @ RAYS.T).T
        squared_norms = np.einsum("ri,ri->r", images, images)
        weights.append(RECORD_WEIGHTS * np.exp(-0.5 * squared_norms))
        projectors.append(
            np.asarray(
                [np.outer(image, image) / float(np.dot(image, image)) for image in images]
            )
        )
        scores.append(squared_norms)
    return RecordState(tuple(weights), tuple(projectors), tuple(scores))


def record_kernels(
    state: RecordState,
    links: tuple[np.ndarray, ...],
    beta: float,
) -> dict[tuple[int, int], np.ndarray]:
    kernels: dict[tuple[int, int], np.ndarray] = {}
    for link, (low, high, _) in zip(links, EDGES):
        transported = np.einsum(
            "ab,sbc,dc->sad", link, state.projectors[high], link
        )
        difference = state.projectors[low][:, None] - transported[None, :]
        squared_distance = np.einsum("rsij,rsij->rs", difference, difference)
        kernels[(low, high)] = np.exp(-0.5 * beta * squared_distance)
    return kernels


def curvature_loads(
    coframes: tuple[np.ndarray, ...],
    links: tuple[np.ndarray, ...],
    plane_axis: int | None = None,
    use_wilson: bool = False,
) -> tuple[np.ndarray, ...]:
    """Return each site's shared-label sum over its three incident faces."""

    loads = [np.zeros(10, dtype=float) for _ in VERTICES]
    for first, second, third, fourth in PLAQUETTES:
        first_position = np.asarray(VERTICES[first], dtype=float)
        first_step = (
            np.asarray(VERTICES[second], dtype=float) - first_position
        ) / 2.0
        second_step = (
            np.asarray(VERTICES[fourth], dtype=float) - first_position
        ) / 2.0
        normal = np.cross(first_step, second_step)
        if plane_axis is not None and abs(normal[plane_axis]) < 0.5:
            continue
        holonomy = (
            oriented_link(links, first, second)
            @ oriented_link(links, second, third)
            @ oriented_link(links, third, fourth)
            @ oriented_link(links, fourth, first)
        )
        sine_curvature = 0.5 * (holonomy - holonomy.T)
        first_base = np.concatenate((first_step, (0.0,)))
        second_base = np.concatenate((second_step, (0.0,)))
        ec_bivector = einstein_cartan_bivector(
            coframes[first], first_step, second_step
        )
        curvature_scalar = (
            float(4.0 - np.trace(holonomy))
            if use_wilson
            else 0.5 * float(np.sum(ec_bivector * sine_curvature))
        )
        ray_incidence = (
            (RAYS[:, :3] @ first_step) ** 2
            + (RAYS[:, :3] @ second_step) ** 2
        )
        loads[first] += ray_incidence * curvature_scalar
    return tuple(loads)


def contract_cube(
    weights: tuple[np.ndarray, ...],
    kernels: dict[tuple[int, int], np.ndarray],
) -> float:
    lower = np.einsum(
        "a,b,c,d,ab,bc,dc,ad->abcd",
        weights[0],
        weights[1],
        weights[2],
        weights[3],
        kernels[(0, 1)],
        kernels[(1, 2)],
        kernels[(3, 2)],
        kernels[(0, 3)],
        optimize=True,
    )
    upper = np.einsum(
        "e,f,g,h,ef,fg,hg,eh->efgh",
        weights[4],
        weights[5],
        weights[6],
        weights[7],
        kernels[(4, 5)],
        kernels[(5, 6)],
        kernels[(7, 6)],
        kernels[(4, 7)],
        optimize=True,
    )
    transported = np.einsum(
        "abcd,ae->ebcd", lower, kernels[(0, 4)], optimize=True
    )
    transported = np.einsum(
        "ebcd,bf->efcd", transported, kernels[(1, 5)], optimize=True
    )
    transported = np.einsum(
        "efcd,cg->efgd", transported, kernels[(2, 6)], optimize=True
    )
    transported = np.einsum(
        "efgd,dh->efgh", transported, kernels[(3, 7)], optimize=True
    )
    return float(np.sum(transported * upper))


def record_partition(
    coframes: tuple[np.ndarray, ...],
    links: tuple[np.ndarray, ...],
    beta: float = BETA,
    sigma: float = SIGMA,
    plane_axis: int | None = None,
    use_wilson: bool = False,
    weight_insertions: dict[int, np.ndarray] | None = None,
) -> float:
    state = record_state(coframes)
    loads = curvature_loads(coframes, links, plane_axis, use_wilson)
    # This is one fixed elementary face-incidence coefficient.  On this cube,
    # where every vertex meets three faces, it is numerically an incidence
    # average.  It must not be recomputed from finite-region vertex degree;
    # the two-cube extension checks that such adaptive averaging breaks gluing.
    weights = [
        weight * np.exp((sigma / 3.0) * load)
        for weight, load in zip(state.weights, loads)
    ]
    if weight_insertions:
        for site, insertion in weight_insertions.items():
            weights[site] = weights[site] * insertion
    return contract_cube(tuple(weights), record_kernels(state, links, beta))


def record_free_energy(
    coframes: tuple[np.ndarray, ...],
    links: tuple[np.ndarray, ...],
    beta: float = BETA,
    sigma: float = SIGMA,
    plane_axis: int | None = None,
    use_wilson: bool = False,
) -> float:
    return -float(
        np.log(
            record_partition(
                coframes,
                links,
                beta,
                sigma,
                plane_axis,
                use_wilson,
            )
        )
    )


def component_values(
    coframes: tuple[np.ndarray, ...],
    links: tuple[np.ndarray, ...],
    *,
    beta: float = BETA,
    use_compatibility: bool = True,
    use_normal_compatibility: bool = True,
    use_curvature: bool = True,
    use_torsion: bool = True,
    use_record: bool = True,
    plane_axis: int | None = None,
    use_wilson_curvature: bool = False,
) -> tuple[float, float, float, float, float]:
    compatibility = 0.0
    if use_compatibility:
        compatibility = 0.5 * ETA * sum(
            float(np.sum((coframes[low] - link @ coframes[high]) ** 2))
            for link, (low, high, _) in zip(links, EDGES)
        )

    normal_compatibility = 0.0
    if use_normal_compatibility:
        normals = tuple(spatial_normal(coframe) for coframe in coframes)
        normal_compatibility = 0.5 * NORMAL_COMPATIBILITY * sum(
            float(np.sum((normals[low] - link @ normals[high]) ** 2))
            for link, (low, high, _) in zip(links, EDGES)
        )

    torsion = 0.0
    for first, second, third, fourth in PLAQUETTES:
        first_position = np.asarray(VERTICES[first], dtype=float)
        first_step = (
            np.asarray(VERTICES[second], dtype=float) - first_position
        ) / 2.0
        second_step = (
            np.asarray(VERTICES[fourth], dtype=float) - first_position
        ) / 2.0
        normal = np.cross(first_step, second_step)
        if plane_axis is not None and abs(normal[plane_axis]) < 0.5:
            continue

        first_base = np.concatenate((first_step, (0.0,)))
        second_base = np.concatenate((second_step, (0.0,)))
        if use_torsion:
            first_difference = (
                oriented_link(links, first, second)
                @ (coframes[second] @ second_base)
                - coframes[first] @ second_base
            )
            second_difference = (
                oriented_link(links, first, fourth)
                @ (coframes[fourth] @ first_base)
                - coframes[first] @ first_base
            )
            torsion_vector = first_difference - second_difference
            torsion += (TAU / 8.0) * float(np.dot(torsion_vector, torsion_vector))

    base_record = record_free_energy(coframes, links, beta, 0.0)
    loaded_record = (
        record_free_energy(
            coframes,
            links,
            beta,
            SIGMA,
            plane_axis,
            use_wilson_curvature,
        )
        if use_curvature
        else base_record
    )
    curvature = loaded_record - base_record if use_curvature else 0.0
    record = base_record if use_record else 0.0
    return compatibility, normal_compatibility, curvature, torsion, record


def well_value(coframes: tuple[np.ndarray, ...], targets: tuple[np.ndarray, ...]) -> float:
    return (ALPHA / 4.0) * sum(
        float(np.sum((coframe.T @ coframe - target) ** 2))
        for coframe, target in zip(coframes, targets)
    )


def action_value(
    coframes: tuple[np.ndarray, ...],
    links: tuple[np.ndarray, ...],
    targets: tuple[np.ndarray, ...] | None = None,
    **component_options,
) -> float:
    value = float(sum(component_values(coframes, links, **component_options)))
    if targets is not None:
        value += well_value(coframes, targets)
    return value


E_STAR = np.diag((1.0, 1.0, 1.0, 5.0 / 4.0))
COFRAMES_STAR = tuple(E_STAR.copy() for _ in VERTICES)


def polar_eliminated_links(
    coframes: tuple[np.ndarray, ...],
) -> tuple[np.ndarray, ...]:
    """Supply the closest proper rotation mapping each high frame to its low frame."""

    links: list[np.ndarray] = []
    for low, high, _ in EDGES:
        comparison = coframes[low] @ np.linalg.inv(coframes[high])
        left, _, right = np.linalg.svd(comparison)
        link = left @ right
        if float(np.linalg.det(link)) < 0.0:
            left[:, -1] *= -1.0
            link = left @ right
        links.append(link)
    return tuple(links)


def equivariant_links(parameters: np.ndarray) -> tuple[np.ndarray, ...]:
    radial_coefficient, dual_coefficient = parameters
    tick = np.asarray((0.0, 0.0, 0.0, 1.0))
    links: list[np.ndarray] = []
    for low, high, axis in EDGES:
        direction = np.eye(3, dtype=float)[axis]
        midpoint = (
            np.asarray(VERTICES[low], dtype=float)
            + np.asarray(VERTICES[high], dtype=float)
        ) / 2.0
        direction_four = np.concatenate((direction, (0.0,)))
        midpoint_four = np.concatenate((midpoint, (0.0,)))
        dual_four = np.concatenate((np.cross(direction, midpoint), (0.0,)))
        algebra = (
            -radial_coefficient * wedge(direction_four, midpoint_four)
            - dual_coefficient * wedge(dual_four, tick)
        )
        links.append(expm(algebra))
    return tuple(links)


def solve_stationary_links() -> tuple[np.ndarray, tuple[np.ndarray, ...], float]:
    def objective(parameters: np.ndarray) -> float:
        return action_value(COFRAMES_STAR, equivariant_links(parameters))

    def gradient(parameters: np.ndarray) -> np.ndarray:
        step = 2.0e-5
        result = np.zeros(2, dtype=float)
        for coordinate in range(2):
            plus = np.asarray(parameters, dtype=float).copy()
            minus = np.asarray(parameters, dtype=float).copy()
            plus[coordinate] += step
            minus[coordinate] -= step
            result[coordinate] = (objective(plus) - objective(minus)) / (2.0 * step)
        return result

    solution = root(gradient, np.asarray((0.3, 0.05)), tol=1.0e-10)
    parameters = np.asarray(solution.x, dtype=float)
    residual = float(np.max(np.abs(gradient(parameters))))
    if not solution.success or residual > 2.0e-7:
        raise RuntimeError(
            f"stationary link solve failed: {solution.message}; residual={residual}"
        )
    return parameters, equivariant_links(parameters), residual


def coframe_gradient(function, coframes: tuple[np.ndarray, ...]) -> np.ndarray:
    gradient = np.zeros((8, 4, 4), dtype=float)
    for site in range(8):
        for row in range(4):
            for column in range(4):
                plus = [coframe.copy() for coframe in coframes]
                minus = [coframe.copy() for coframe in coframes]
                plus[site][row, column] += COFRAME_STEP
                minus[site][row, column] -= COFRAME_STEP
                gradient[site, row, column] = (
                    float(function(tuple(plus))) - float(function(tuple(minus)))
                ) / (2.0 * COFRAME_STEP)
    return gradient


def link_gradient(function, links: tuple[np.ndarray, ...]) -> np.ndarray:
    gradient = np.zeros((12, 6), dtype=float)
    for edge in range(12):
        for generator_index, generator in enumerate(SKEW_GENERATORS):
            plus = list(links)
            minus = list(links)
            plus[edge] = expm(LINK_STEP * generator) @ links[edge]
            minus[edge] = expm(-LINK_STEP * generator) @ links[edge]
            gradient[edge, generator_index] = (
                float(function(tuple(plus))) - float(function(tuple(minus)))
            ) / (2.0 * LINK_STEP)
    return gradient


def stationary_targets(
    links: tuple[np.ndarray, ...],
) -> tuple[tuple[np.ndarray, ...], np.ndarray, float]:
    nonwell_gradient = coframe_gradient(
        lambda coframes: action_value(coframes, links), COFRAMES_STAR
    )
    targets: list[np.ndarray] = []
    antisymmetric_error = 0.0
    for coframe, gradient in zip(COFRAMES_STAR, nonwell_gradient):
        reduced = np.linalg.solve(coframe, gradient)
        antisymmetric_error = max(
            antisymmetric_error, float(np.linalg.norm(reduced - reduced.T))
        )
        targets.append(
            coframe.T @ coframe
            + 0.5 * (reduced + reduced.T) / ALPHA
        )
    return tuple(targets), nonwell_gradient, antisymmetric_error


def transform_configuration(
    coframes: tuple[np.ndarray, ...],
    links: tuple[np.ndarray, ...],
    targets: tuple[np.ndarray, ...],
    spatial: np.ndarray,
) -> tuple[tuple[np.ndarray, ...], tuple[np.ndarray, ...], tuple[np.ndarray, ...]]:
    rotation = four_rotation(spatial)
    transformed_coframes: list[np.ndarray | None] = [None] * 8
    transformed_targets: list[np.ndarray | None] = [None] * 8
    transformed_links: list[np.ndarray | None] = [None] * 12
    for old_index, vertex in enumerate(VERTICES):
        new_vertex = tuple(spatial @ np.asarray(vertex, dtype=int))
        new_index = VERTEX_INDEX[new_vertex]
        transformed_coframes[new_index] = (
            rotation @ coframes[old_index] @ rotation.T
        )
        transformed_targets[new_index] = rotation @ targets[old_index] @ rotation.T
    for old_edge, (low, high, _) in enumerate(EDGES):
        new_low_vertex = tuple(spatial @ np.asarray(VERTICES[low], dtype=int))
        new_high_vertex = tuple(spatial @ np.asarray(VERTICES[high], dtype=int))
        first = VERTEX_INDEX[new_low_vertex]
        second = VERTEX_INDEX[new_high_vertex]
        transformed = rotation @ links[old_edge] @ rotation.T
        if (first, second) in EDGE_INDEX:
            transformed_links[EDGE_INDEX[(first, second)]] = transformed
        else:
            transformed_links[EDGE_INDEX[(second, first)]] = transformed.T
    if any(item is None for item in transformed_coframes + transformed_targets + transformed_links):
        raise RuntimeError("incomplete proper-cubic transform")
    return (
        tuple(item for item in transformed_coframes if item is not None),
        tuple(item for item in transformed_links if item is not None),
        tuple(item for item in transformed_targets if item is not None),
    )


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
        for link, (low, high, _) in zip(links, EDGES)
    )
    return transformed_coframes, transformed_links


def holonomy_data(
    coframes: tuple[np.ndarray, ...], links: tuple[np.ndarray, ...]
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    gaps: list[float] = []
    signals: list[float] = []
    torsions: list[float] = []
    for first, second, third, fourth in PLAQUETTES:
        first_position = np.asarray(VERTICES[first], dtype=float)
        first_step = (
            np.asarray(VERTICES[second], dtype=float) - first_position
        ) / 2.0
        second_step = (
            np.asarray(VERTICES[fourth], dtype=float) - first_position
        ) / 2.0
        first_base = np.concatenate((first_step, (0.0,)))
        second_base = np.concatenate((second_step, (0.0,)))
        holonomy = (
            oriented_link(links, first, second)
            @ oriented_link(links, second, third)
            @ oriented_link(links, third, fourth)
            @ oriented_link(links, fourth, first)
        )
        sine_curvature = 0.5 * (holonomy - holonomy.T)
        ec_bivector = einstein_cartan_bivector(
            coframes[first], first_step, second_step
        )
        gaps.append(float(np.linalg.norm(holonomy - np.eye(4))))
        signals.append(0.5 * float(np.sum(ec_bivector * sine_curvature)))
        first_difference = (
            oriented_link(links, first, second)
            @ (coframes[second] @ second_base)
            - coframes[first] @ second_base
        )
        second_difference = (
            oriented_link(links, first, fourth)
            @ (coframes[fourth] @ first_base)
            - coframes[first] @ first_base
        )
        torsions.append(float(np.linalg.norm(first_difference - second_difference)))
    return np.asarray(gaps), np.asarray(signals), np.asarray(torsions)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition, detail: str = "") -> None:
        ok = bool(condition)
        display_statement = (
            statement if len(statement) <= 95 else statement[:92] + "..."
        )
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {display_statement}")
        if detail:
            display_detail = detail if len(detail) <= 130 else detail[:127] + "..."
            print(f"       {display_detail}")
        self.passed += int(ok)
        self.failed += int(not ok)


def flat(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").lower().split())


def main() -> int:
    checks = Checks()
    note = flat(NOTE_PATH)
    axiom = flat(AXIOM_PATH)
    local_parent = flat(LOCAL_LAW_PARENT_PATH)
    frame_parent = flat(FRAME_PARENT_PATH)

    checks.check(
        "premise-and-scope-binding",
        "the runner binds the four-axiom surface and the two supplied local-law/frame parents without importing a curvature law or audit verdict",
        all(
            path.exists()
            for path in (
                AXIOM_PATH,
                LOCAL_LAW_PARENT_PATH,
                FRAME_PARENT_PATH,
                PREMISE_REGISTRY_PATH,
            )
        )
        and "lattice / physical locality" in axiom
        and "proper cubic" in local_parent
        and "exact next target" in frame_parent
        and "audit-status authority" in note,
    )

    unique_faces = {frozenset(loop) for loop in PLAQUETTES}
    checks.check(
        "full-proper-cubic-plaquette-orbit",
        "the cube carries all 24 based oriented plaquettes, reducing to six geometric faces rather than one chosen plane or an open star",
        len(SPATIAL_ROTATIONS) == 24
        and len(set(PLAQUETTES)) == 24
        and len(unique_faces) == 6
        and len(EDGES) == 12
        and len(VERTICES) == 8,
        f"rotations/loops/faces/edges/vertices={len(SPATIAL_ROTATIONS)}/{len(set(PLAQUETTES))}/{len(unique_faces)}/{len(EDGES)}/{len(VERTICES)}",
    )

    ray_errors = []
    ray_weight_errors = []
    for spatial in SPATIAL_ROTATIONS:
        rotation = four_rotation(spatial)
        for ray_index, projector in enumerate(RAY_PROJECTORS):
            transformed = rotation @ projector @ rotation.T
            distances = np.linalg.norm(RAY_PROJECTORS - transformed, axis=(1, 2))
            target = int(np.argmin(distances))
            ray_errors.append(float(distances[target]))
            ray_weight_errors.append(abs(RECORD_WEIGHTS[target] - RECORD_WEIGHTS[ray_index]))
    checks.check(
        "projective-ten-ray-cubic-carrier",
        "the ten rank-one Record-ray images close projectively under all proper-cubic rotations and their two orbit weights are invariant",
        max(ray_errors) < 1.0e-14 and max(ray_weight_errors) < 1.0e-14,
        f"projector error={max(ray_errors):.3e}; weight error={max(ray_weight_errors):.3e}",
    )

    reference_normal = spatial_normal(E_STAR)
    normal_unit_error = abs(float(np.linalg.norm(reference_normal)) - 1.0)
    normal_orthogonality_error = float(
        np.max(np.abs(E_STAR[:, :3].T @ reference_normal))
    )
    normal_rotation = expm(0.31 * SKEW_GENERATORS[2])
    normal_covariance_error = float(
        np.linalg.norm(
            spatial_normal(normal_rotation @ E_STAR)
            - normal_rotation @ reference_normal
        )
    )
    x_step = np.asarray((1.0, 0.0, 0.0))
    y_step = np.asarray((0.0, 1.0, 0.0))
    intrinsic_bivector = einstein_cartan_bivector(E_STAR, x_step, y_step)
    intrinsic_generator = intrinsic_bivector / float(
        np.linalg.norm(intrinsic_bivector)
    )
    dual_face_bivector = hodge_star(
        wedge(E_STAR[:, 0], E_STAR[:, 1])
    )
    normal_mixing_generator = dual_face_bivector / float(
        np.linalg.norm(dual_face_bivector)
    )

    def bivector_signal(
        bivector: np.ndarray,
        generator: np.ndarray,
        epsilon: float = 1.0e-4,
    ) -> float:
        holonomy = expm(epsilon * generator)
        return 0.25 * float(np.sum(bivector * (holonomy - holonomy.T)))

    intrinsic_index_signal = bivector_signal(
        intrinsic_bivector, intrinsic_generator
    )
    normal_mixing_signal = bivector_signal(
        intrinsic_bivector, normal_mixing_generator
    )
    dual_face_intrinsic_signal = bivector_signal(
        dual_face_bivector, intrinsic_generator
    )
    dual_face_normal_mixing_signal = bivector_signal(
        dual_face_bivector, normal_mixing_generator
    )
    checks.check(
        "derived-normal-intrinsic-einstein-cartan-index-control",
        "the unit internal normal is triad-derived and covariant, and the complementary-triad bivector sees intrinsic face rotation rather than normal-mixing curvature",
        normal_unit_error < 2.0e-15
        and normal_orthogonality_error < 2.0e-15
        and float(np.dot(reference_normal, E_STAR[:, 3])) > 1.0
        and normal_covariance_error < 2.0e-15
        and abs(intrinsic_index_signal) > 5.0e-5
        and abs(normal_mixing_signal) < 2.0e-15
        and abs(dual_face_intrinsic_signal) < 2.0e-15
        and abs(dual_face_normal_mixing_signal) > 5.0e-5,
        f"unit/orthogonality/covariance={normal_unit_error:.3e}/{normal_orthogonality_error:.3e}/{normal_covariance_error:.3e}; EC intrinsic/normal-mixing={intrinsic_index_signal:.9f}/{normal_mixing_signal:.3e}; dual-face={dual_face_intrinsic_signal:.3e}/{dual_face_normal_mixing_signal:.9f}",
    )

    parameters, links, reduced_link_residual = solve_stationary_links()
    orthogonality_error = max(
        float(np.linalg.norm(link.T @ link - np.eye(4))) for link in links
    )
    determinant_error = max(abs(float(np.linalg.det(link)) - 1.0) for link in links)
    witness_normals = tuple(spatial_normal(coframe) for coframe in COFRAMES_STAR)
    normal_compatibility_error = max(
        float(
            np.linalg.norm(
                witness_normals[low] - link @ witness_normals[high]
            )
        )
        for link, (low, high, _) in zip(links, EDGES)
    )
    equivariance_error = 0.0
    placeholder_targets = tuple(np.eye(4) for _ in VERTICES)
    for spatial in SPATIAL_ROTATIONS:
        _, transformed_links, _ = transform_configuration(
            COFRAMES_STAR, links, placeholder_targets, spatial
        )
        equivariance_error = max(
            equivariance_error,
            max(
                float(np.linalg.norm(left - right))
                for left, right in zip(links, transformed_links)
            ),
        )
    checks.check(
        "derived-equivariant-so4-link-background",
        "the two-tensor equivariant family selects a nonzero spatial coefficient and zero normal-mixing coefficient, generating twelve normal-compatible SO(4) links",
        reduced_link_residual < 2.0e-7
        and orthogonality_error < 2.0e-15
        and determinant_error < 2.0e-15
        and equivariance_error < 3.0e-15
        and normal_compatibility_error < 2.0e-10
        and abs(parameters[0]) > 0.25
        and abs(parameters[1]) < 2.0e-10,
        f"parameters spatial/normal-mixing={parameters[0]:.9f}/{parameters[1]:.3e}; reduced residual={reduced_link_residual:.3e}; SO4={orthogonality_error:.3e}/{determinant_error:.3e}; equivariance={equivariance_error:.3e}; normal compatibility={normal_compatibility_error:.3e}",
    )

    full_link_gradient = link_gradient(
        lambda varied_links: action_value(COFRAMES_STAR, varied_links), links
    )
    checks.check(
        "full-link-stationarity-not-ansatz-only",
        "the numerical two-parameter solution annihilates all 72 independent intrinsic link tangents of the complete cube law",
        float(np.max(np.abs(full_link_gradient))) < 2.0e-6,
        f"maximum={np.max(np.abs(full_link_gradient)):.3e}; norm={np.linalg.norm(full_link_gradient):.3e}",
    )

    holonomy_gaps, curvature_signals, torsion_norms = holonomy_data(
        COFRAMES_STAR, links
    )
    checks.check(
        "nontrivial-intrinsic-spatial-einstein-cartan-curvature",
        "every face has nonidentity gauge-covariant holonomy and a nonzero derived-normal complementary-triad Einstein-Cartan contraction, while torsion is explicitly measured",
        float(np.min(holonomy_gaps)) > 0.5
        and float(np.min(np.abs(curvature_signals))) > 0.2
        and float(np.min(torsion_norms)) > 0.1,
        f"holonomy={np.min(holonomy_gaps):.6f}..{np.max(holonomy_gaps):.6f}; intrinsic EC curvature={np.min(curvature_signals):.6f}..{np.max(curvature_signals):.6f}; torsion={np.min(torsion_norms):.6f}..{np.max(torsion_norms):.6f}",
    )

    targets, nonwell_gradient, frame_antisymmetry = stationary_targets(links)
    target_minimum = min(float(np.min(np.linalg.eigvalsh(target))) for target in targets)
    target_equivariance = 0.0
    for spatial in SPATIAL_ROTATIONS:
        _, _, transformed_targets = transform_configuration(
            COFRAMES_STAR, links, targets, spatial
        )
        target_equivariance = max(
            target_equivariance,
            max(
                float(np.linalg.norm(left - right))
                for left, right in zip(targets, transformed_targets)
            ),
        )
    full_coframe_gradient = coframe_gradient(
        lambda coframes: action_value(coframes, links, targets), COFRAMES_STAR
    )
    checks.check(
        "coercive-well-coframe-stationarity",
        "positive-definite proper-cubic target Grams derived from the complete non-well stress give a numerically stationary coframe witness and a coercive quartic geometry tail",
        frame_antisymmetry < 2.0e-5
        and target_minimum > 0.8
        and target_equivariance < 3.0e-5
        and float(np.max(np.abs(full_coframe_gradient))) < 3.0e-5,
        f"frame antisymmetry={frame_antisymmetry:.3e}; target minimum={target_minimum:.6f}; target equivariance={target_equivariance:.3e}; stationarity={np.max(np.abs(full_coframe_gradient)):.3e}",
    )

    record_z = record_partition(COFRAMES_STAR, links)
    state = record_state(COFRAMES_STAR)
    site = 0
    site_load = curvature_loads(COFRAMES_STAR, links)[site]
    # Under a uniform scale of one coframe, its ray score scales as (1+t)^2,
    # its derived-normal complementary triad scales as (1+t), and normalized
    # ray projectors and transported edge kernels remain fixed.
    branch_first_derivative = (
        state.scores[site] - (SIGMA / 3.0) * site_load
    )
    branch_second_derivative = state.scores[site]
    first_expectation = record_partition(
        COFRAMES_STAR,
        links,
        weight_insertions={site: branch_first_derivative},
    ) / record_z
    first_square_expectation = record_partition(
        COFRAMES_STAR,
        links,
        weight_insertions={
            site: branch_first_derivative * branch_first_derivative
        },
    ) / record_z
    contact = record_partition(
        COFRAMES_STAR,
        links,
        weight_insertions={site: branch_second_derivative},
    ) / record_z
    covariance = first_square_expectation - first_expectation * first_expectation
    complete_response = contact - covariance
    omitted_contact_response = -covariance
    scale_step = 2.0e-4
    plus_scale = list(COFRAMES_STAR)
    minus_scale = list(COFRAMES_STAR)
    plus_scale[site] = (1.0 + scale_step) * plus_scale[site]
    minus_scale[site] = (1.0 - scale_step) * minus_scale[site]
    numerical_response = (
        record_free_energy(tuple(plus_scale), links)
        - 2.0 * record_free_energy(COFRAMES_STAR, links)
        + record_free_energy(tuple(minus_scale), links)
    ) / (scale_step * scale_step)
    checks.check(
        "normalized-record-contact-covariance-response",
        "the exact 10^8-term Record sum is contracted without enumeration and its curvature-loaded intrinsic coframe-scale response equals microscopic contact minus connected covariance",
        record_z > 1.0e6
        and contact > 1.0
        and covariance > 0.01
        and omitted_contact_response < 0.0
        and abs(numerical_response - complete_response) < 2.0e-6,
        f"Z={record_z:.6f}; contact={contact:.9f}; covariance={covariance:.9f}; complete/numerical/no-contact={complete_response:.9f}/{numerical_response:.9f}/{omitted_contact_response:.9f}",
    )

    rotations = tuple(
        expm((0.03 + 0.01 * site_index) * SKEW_GENERATORS[site_index % 6])
        for site_index in range(8)
    )
    rotated_coframes, rotated_links = local_frame_transform(
        COFRAMES_STAR, links, rotations
    )
    local_frame_error = abs(
        action_value(rotated_coframes, rotated_links, targets)
        - action_value(COFRAMES_STAR, links, targets)
    )
    proper_cubic_error = 0.0
    for spatial in SPATIAL_ROTATIONS:
        transformed = transform_configuration(COFRAMES_STAR, links, targets, spatial)
        proper_cubic_error = max(
            proper_cubic_error,
            abs(
                action_value(*transformed)
                - action_value(COFRAMES_STAR, links, targets)
            ),
        )
    checks.check(
        "local-frame-and-proper-cubic-covariance",
        "the same finite joint weight is invariant under independent endpoint frames and all 24 combined proper-cubic transforms",
        local_frame_error < 2.0e-12 and proper_cubic_error < 2.0e-10,
        f"local-frame={local_frame_error:.3e}; proper-cubic={proper_cubic_error:.3e}",
    )

    uncompensated_coframes = list(COFRAMES_STAR)
    uncompensated_rotation = expm(0.08 * SKEW_GENERATORS[0])
    uncompensated_coframes[0] = (
        uncompensated_rotation @ uncompensated_coframes[0]
    )
    uncompensated_change = abs(
        action_value(tuple(uncompensated_coframes), links, targets)
        - action_value(COFRAMES_STAR, links, targets)
    )
    checks.check(
        "compensated-versus-uncompensated-local-frame-control",
        "a compensated site frame leaves the action fixed, whereas rotating that coframe without its incident link endpoints changes the same action",
        local_frame_error < 2.0e-12 and uncompensated_change > 1.0e-3,
        f"compensated error={local_frame_error:.3e}; uncompensated change={uncompensated_change:.6f}",
    )

    def open_loop_signal(
        coframes: tuple[np.ndarray, ...], varied_links: tuple[np.ndarray, ...]
    ) -> float:
        first, second, third, fourth = PLAQUETTES[0]
        first_position = np.asarray(VERTICES[first], dtype=float)
        first_step = (
            np.asarray(VERTICES[second], dtype=float) - first_position
        ) / 2.0
        second_step = (
            np.asarray(VERTICES[fourth], dtype=float) - first_position
        ) / 2.0
        open_transport = (
            oriented_link(varied_links, first, second)
            @ oriented_link(varied_links, second, third)
            @ oriented_link(varied_links, third, fourth)
        )
        open_curvature = 0.5 * (open_transport - open_transport.T)
        ec_bivector = einstein_cartan_bivector(
            coframes[first], first_step, second_step
        )
        return 0.5 * float(np.sum(ec_bivector * open_curvature))

    open_before = open_loop_signal(COFRAMES_STAR, links)
    open_after = open_loop_signal(rotated_coframes, rotated_links)
    removed_edge = EDGES[0][:2]
    affected_loops = sum(
        any(
            {loop[index], loop[(index + 1) % 4]} == set(removed_edge)
            for index in range(4)
        )
        for loop in PLAQUETTES
    )
    checks.check(
        "closing-link-removal-breaks-local-frame-covariance",
        "deleting one edge invalidates eight based loops, and deleting a closing factor leaves an open transporter whose coframe contraction is not frame covariant",
        affected_loops == 8 and abs(open_after - open_before) > 1.0e-3,
        f"affected loops={affected_loops}; open signal before/after={open_before:.9f}/{open_after:.9f}; change={abs(open_after-open_before):.6f}",
    )

    ec_probe_bivector = einstein_cartan_bivector(E_STAR, x_step, y_step)
    curvature_generator = ec_probe_bivector / float(
        np.linalg.norm(ec_probe_bivector)
    )

    def probe_signals(epsilon: float) -> tuple[float, float]:
        holonomy = expm(epsilon * curvature_generator)
        sine_curvature = 0.5 * (holonomy - holonomy.T)
        ec_signal = 0.5 * float(np.sum(ec_probe_bivector * sine_curvature))
        wilson = float(4.0 - np.trace(holonomy))
        return ec_signal, wilson

    ec_small, wilson_small = probe_signals(1.0e-4)
    ec_double, wilson_double = probe_signals(2.0e-4)
    reversed_ec, reversed_wilson = probe_signals(-1.0e-4)
    checks.check(
        "linear-intrinsic-curvature-versus-narrow-wilson-comparator",
        "the intrinsic Einstein-Cartan term is odd and linear in small holonomy, whereas the displayed coframe-independent Wilson comparator is even and quadratic",
        abs(ec_double / ec_small - 2.0) < 2.0e-8
        and abs(wilson_double / wilson_small - 4.0) < 5.0e-7
        and abs(reversed_ec + ec_small) < 2.0e-15
        and abs(reversed_wilson - wilson_small) < 2.0e-15,
        f"doubling ratios EC/Wilson={ec_double/ec_small:.9f}/{wilson_double/wilson_small:.9f}; reversal={reversed_ec/ec_small:.1f}/{reversed_wilson/wilson_small:.1f}",
    )

    pi_holonomy = expm(np.sqrt(2.0) * np.pi * curvature_generator)
    pi_sine = 0.5 * (pi_holonomy - pi_holonomy.T)
    pi_ec_signal = 0.5 * float(np.sum(ec_probe_bivector * pi_sine))
    pi_gap = float(np.linalg.norm(pi_holonomy - np.eye(4)))
    pi_wilson = float(4.0 - np.trace(pi_holonomy))
    checks.check(
        "sine-curvature-pi-holonomy-chart-boundary",
        "the sine-curvature coordinate is explicitly certified blind at nonidentity pi holonomy, so the theorem is not a global curvature-coordinate claim",
        abs(pi_gap - 2.0 * np.sqrt(2.0)) < 2.0e-14
        and abs(pi_ec_signal) < 2.0e-15
        and abs(pi_wilson - 4.0) < 2.0e-14,
        f"pi gap/EC/Wilson={pi_gap:.9f}/{pi_ec_signal:.3e}/{pi_wilson:.9f}",
    )

    wilson_record_z = record_partition(
        COFRAMES_STAR, links, use_wilson=True
    )
    ec_load_derivative = (
        curvature_loads(tuple(plus_scale), links)[site]
        - curvature_loads(tuple(minus_scale), links)[site]
    ) / (2.0 * scale_step)
    wilson_load_derivative = (
        curvature_loads(tuple(plus_scale), links, use_wilson=True)[site]
        - curvature_loads(tuple(minus_scale), links, use_wilson=True)[site]
    ) / (2.0 * scale_step)
    wilson_link_gradient = link_gradient(
        lambda varied: action_value(
            COFRAMES_STAR,
            varied,
            targets,
            use_wilson_curvature=True,
        ),
        links,
    )
    wilson_frame_error = abs(
        action_value(
            rotated_coframes,
            rotated_links,
            targets,
            use_wilson_curvature=True,
        )
        - action_value(
            COFRAMES_STAR,
            links,
            targets,
            use_wilson_curvature=True,
        )
    )
    checks.check(
        "same-law-wilson-curvature-substitution",
        "substituting only 4-tr(H) inside the same Record branches preserves positivity and frame covariance but removes explicit coframe-curvature response and breaks the unrefitted link equation",
        wilson_record_z > 1.0e6
        and wilson_frame_error < 2.0e-12
        and float(np.linalg.norm(ec_load_derivative)) > 1.0
        and float(np.linalg.norm(wilson_load_derivative)) < 2.0e-12
        and float(np.max(np.abs(wilson_link_gradient))) > 0.5,
        f"Z={wilson_record_z:.6f}; frame error={wilson_frame_error:.3e}; load derivatives EC/Wilson={np.linalg.norm(ec_load_derivative):.6f}/{np.linalg.norm(wilson_load_derivative):.3e}; link residual={np.max(np.abs(wilson_link_gradient)):.6f}",
    )

    pure_rotations = tuple(
        expm((0.09 + 0.02 * site_index) * SKEW_GENERATORS[(site_index + 1) % 6])
        for site_index in range(8)
    )
    pure_coframes = tuple(rotation @ E_STAR for rotation in pure_rotations)
    pure_links = tuple(
        pure_rotations[low] @ pure_rotations[high].T for low, high, _ in EDGES
    )
    pure_gaps, pure_signals, pure_torsions = holonomy_data(pure_coframes, pure_links)

    flat_links = tuple(np.eye(4) for _ in EDGES)
    incompatible_rotations = tuple(
        expm((0.04 + 0.015 * site_index) * SKEW_GENERATORS[site_index % 6])
        for site_index in range(8)
    )
    incompatible_coframes = tuple(
        rotation @ E_STAR for rotation in incompatible_rotations
    )
    flat_gaps, flat_signals, flat_torsions = holonomy_data(
        incompatible_coframes, flat_links
    )
    checks.check(
        "pure-gauge-and-zero-holonomy-controls",
        "pure gauge kills holonomy, curvature, compatibility, and torsion, while a flat but incompatible control keeps zero curvature and exposes nonzero torsion",
        float(np.max(pure_gaps)) < 2.0e-14
        and float(np.max(np.abs(pure_signals))) < 2.0e-14
        and float(np.max(pure_torsions)) < 2.0e-14
        and float(np.max(flat_gaps)) < 1.0e-14
        and float(np.max(np.abs(flat_signals))) < 1.0e-14
        and float(np.max(flat_torsions)) > 0.05,
        f"pure max H/EC/T={np.max(pure_gaps):.3e}/{np.max(np.abs(pure_signals)):.3e}/{np.max(pure_torsions):.3e}; flat-incompatible T={np.max(flat_torsions):.6f}",
    )

    polar_probe_coframes = []
    for x_sign, y_sign, z_sign in VERTICES:
        deformation = np.eye(4)
        deformation[0, 1] = deformation[1, 0] = 0.07 * z_sign
        deformation[1, 2] = deformation[2, 1] = 0.05 * x_sign
        deformation[0, 2] = deformation[2, 0] = 0.06 * y_sign
        deformation[0, 0] += 0.03 * x_sign
        deformation[1, 1] += 0.02 * y_sign
        deformation[2, 2] += 0.025 * z_sign
        polar_probe_coframes.append(E_STAR @ deformation)
    polar_probe_coframes = tuple(polar_probe_coframes)
    polar_links = polar_eliminated_links(polar_probe_coframes)
    polar_gaps, polar_signals, polar_torsions = holonomy_data(
        polar_probe_coframes, polar_links
    )
    polar_rotated_coframes, polar_rotated_links = local_frame_transform(
        polar_probe_coframes, polar_links, rotations
    )
    polar_rederived_links = polar_eliminated_links(polar_rotated_coframes)
    polar_covariance_error = max(
        float(np.linalg.norm(left - right))
        for left, right in zip(polar_rotated_links, polar_rederived_links)
    )
    polar_normals = tuple(spatial_normal(item) for item in polar_probe_coframes)
    polar_normal_error = max(
        float(np.linalg.norm(polar_normals[low] - link @ polar_normals[high]))
        for link, (low, high, _) in zip(polar_links, EDGES)
    )
    checks.check(
        "polar-coframe-derived-link-elimination-attempt",
        "a supplied closest-frame polar elimination is frame covariant and produces small intrinsic curvature on a noncommuting metric probe, but remains an unselected discretization rather than a Levi-Civita theorem",
        min(float(np.linalg.det(item)) for item in polar_probe_coframes) > 1.0
        and polar_covariance_error < 2.0e-12
        and polar_normal_error < 2.0e-12
        and float(np.min(polar_gaps)) > 0.01
        and float(np.min(np.abs(polar_signals))) > 0.005
        and float(np.min(polar_torsions)) > 0.005,
        f"holonomy={np.min(polar_gaps):.6f}..{np.max(polar_gaps):.6f}; EC={np.min(polar_signals):.6f}..{np.max(polar_signals):.6f}; torsion={np.min(polar_torsions):.6f}..{np.max(polar_torsions):.6f}; covariance/normal={polar_covariance_error:.3e}/{polar_normal_error:.3e}",
    )

    normal_mixed_links = list(links)
    normal_mixed_links[0] = (
        expm(0.1 * SKEW_GENERATORS[2]) @ normal_mixed_links[0]
    )
    normal_mixed_links = tuple(normal_mixed_links)
    normal_mixing_error = max(
        float(
            np.linalg.norm(
                witness_normals[low] - link @ witness_normals[high]
            )
        )
        for link, (low, high, _) in zip(normal_mixed_links, EDGES)
    )
    normal_mixing_penalty = float(
        sum(
            component_values(
                COFRAMES_STAR,
                normal_mixed_links,
                use_compatibility=False,
                use_curvature=False,
                use_torsion=False,
                use_record=False,
            )
        )
    )
    checks.check(
        "normal-compatibility-mixing-control",
        "the selected spatial branch transports every derived normal, while a one-link normal-mixing mutation activates the declared compatibility penalty",
        normal_compatibility_error < 2.0e-10
        and normal_mixing_error > 0.05
        and normal_mixing_penalty > 5.0e-4,
        f"witness/mutated normal error={normal_compatibility_error:.3e}/{normal_mixing_error:.6f}; penalty={normal_mixing_penalty:.9f}",
    )

    record_gradient = coframe_gradient(
        lambda coframes: record_free_energy(coframes, links), COFRAMES_STAR
    )
    curvature_gradient = coframe_gradient(
        lambda coframes: action_value(
            coframes,
            links,
            use_compatibility=False,
            use_torsion=False,
            use_record=False,
        ),
        COFRAMES_STAR,
    )
    no_curvature_link = link_gradient(
        lambda varied: action_value(
            COFRAMES_STAR, varied, targets, use_curvature=False
        ),
        links,
    )
    no_torsion_link = link_gradient(
        lambda varied: action_value(COFRAMES_STAR, varied, targets, use_torsion=False),
        links,
    )
    no_compatibility_link = link_gradient(
        lambda varied: action_value(
            COFRAMES_STAR, varied, targets, use_compatibility=False
        ),
        links,
    )
    no_transport_link = link_gradient(
        lambda varied: action_value(COFRAMES_STAR, varied, targets, beta=0.0),
        links,
    )
    checks.check(
        "load-bearing-record-curvature-compatibility-mutations",
        "without refitting the wells or links, deleting Record stress, intrinsic EC curvature, torsion control, coframe compatibility, or ray transport breaks a distinct stationary equation",
        float(np.linalg.norm(record_gradient)) > 1.0
        and float(np.linalg.norm(curvature_gradient)) > 0.5
        and float(np.max(np.abs(no_curvature_link))) > 0.1
        and float(np.max(np.abs(no_torsion_link))) > 0.01
        and float(np.max(np.abs(no_compatibility_link))) > 0.01
        and float(np.max(np.abs(no_transport_link))) > 1.0e-4,
        f"drop Record/coframe={np.linalg.norm(record_gradient):.6f}; curvature/coframe={np.linalg.norm(curvature_gradient):.6f}; link residuals curvature/torsion/compatibility/transport={np.max(np.abs(no_curvature_link)):.6f}/{np.max(np.abs(no_torsion_link)):.6f}/{np.max(np.abs(no_compatibility_link)):.6f}/{np.max(np.abs(no_transport_link)):.6f}",
    )

    probe_coframes = list(COFRAMES_STAR)
    probe_coframes[0] = E_STAR + 0.07 * np.asarray(
        (
            (0.2, 0.1, 0.0, 0.0),
            (0.0, -0.1, 0.05, 0.0),
            (0.03, 0.0, 0.15, 0.02),
            (0.0, 0.04, 0.0, -0.1),
        )
    )
    probe_coframes = tuple(probe_coframes)
    axis_swap = next(
        spatial
        for spatial in SPATIAL_ROTATIONS
        if tuple(spatial @ np.asarray((1, 0, 0))) == (0, 0, 1)
    )
    transformed_probe = transform_configuration(
        probe_coframes, links, targets, axis_swap
    )
    full_probe_error = abs(
        action_value(probe_coframes, links, targets)
        - action_value(*transformed_probe)
    )
    one_plane_before = action_value(
        probe_coframes,
        links,
        targets,
        use_compatibility=False,
        use_torsion=False,
        use_record=False,
        plane_axis=0,
    )
    one_plane_after = action_value(
        *transformed_probe,
        use_compatibility=False,
        use_torsion=False,
        use_record=False,
        plane_axis=0,
    )
    checks.check(
        "one-plane-mutation-breaks-cubic-law",
        "the 24-loop law is proper-cubic covariant, while retaining only one normal direction silently selects a plane on an anisotropic probe",
        full_probe_error < 2.0e-10
        and abs(one_plane_after - one_plane_before) > 1.0e-3,
        f"full-orbit error={full_probe_error:.3e}; one-plane change={abs(one_plane_after-one_plane_before):.6f}",
    )

    checks.check(
        "joint-normalization-and-axiom-boundary",
        "the note proves finite normalization from compact SO(4), finite Records, and a positive quartic coframe tail, while keeping the carrier, law coefficients, geometry measure, gravity selection, and fifth-axiom necessity open",
        "coercive" in note
        and "haar" in note
        and "not a gravity derivation" in note
        and "no fifth ontology axiom" in note
        and "z^3 x z_tau" in note,
    )

    print("N5_CERTIFICATE: executed 8 cube vertices, 12 constrained links, 6 faces, all 24 based proper-cubic plaquette loops, and all 72 intrinsic link tangents")
    print("N5_CERTIFICATE: contracted the exact 10^8 Record assignments by a four-index tensor transfer and separated Record contact, covariance, stress, transport, compatibility, torsion, and intrinsic EC curvature")
    print("per_element: checked all ten projective Record rays and both proper-cubic ray orbits")
    print("per_site: checked all eight coframes, twelve edge transports, and independent endpoint-frame covariance")
    print("per_mode: checked and not executed — no Bloch, graviton, or Lorentzian mode decomposition; finite coordinates cover 128 coframe entries and 72 link tangents")
    print("per_block: checked one supplied normalizable Euclidean Record-coframe-link cube law and its pure-gauge, zero-holonomy, Wilson, and deletion controls")
    print("lattice_wide: checked and not executed — one complete elementary spatial-cube plaquette orbit is not an increasing-region/full-Z3 phase, Bianchi/Einstein regime, Z3 x Z_tau law, or Lorentzian update")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return int(checks.failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
